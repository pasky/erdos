#!/usr/bin/env python3
"""Check a catalogue of exact polynomial cofactor inequalities for index seven.

Each full symmetric jet rank yields a finite integer polynomial family with
nonzero evaluation at every physical point off the diagonal.
The central column must be excluded separately before diagonal factors are used. This module certifies only those
polynomial implications; separate source inequalities and exact coverage are
needed for a whole-index theorem.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path

import erdos_699_index_13_interpolation_gcd as interpolation

INDEX = 7
DATA = Path(__file__).with_suffix('.json')


def polynomial_degree(record):
    return (2*sum(record['line_exponents'])+record.get('diagonal_power',0)
            +sum(record.get('row_line_exponents',[0]*INDEX))
            +max(0,record['interpolation_degree']
                     +(0 if record.get('nonvanishing_method')=='coprime_kernel' else 1)))


def necessary_cut(record, positions):
    """Return integer lhs,rhs for distinct selected small-prime positions.

    For sufficiently large bad rows with j<n/2,
    sum(lhs[k]*e[k]) <= rhs+epsilon,
    with e[k]=log(u_p)/log(n-6). See threshold_power for an explicit
    bound for the coefficient term and common_zero_threshold_power for
    coprime sections' simultaneous zeros.
    """
    assert len(positions)==3 and len(set(positions))==3
    assert all(type(t)is int and 0<=t<INDEX for t in positions)
    m=record['row_multiplicities']
    return [m[t]for t in positions], polynomial_degree(record)-sum(
        m[t]for t in range(INDEX)if t not in positions)


def coefficient_bound(record):
    """Bound 2 ||F||_1 (7!)^max(m) by 10^E for a nonzero family member."""
    h,m=record['line_exponents'],record['row_multiplicities']
    r,d=record['symmetric_jet_count'],record['interpolation_degree']
    assert r<100000 and d<1000 and max(h+m)<10**6
    # Matrix entries <=2*7^d<10^(d+1); r!<10^(5r).
    # ||H||_1<10^(2 sum h); ||(X-Y)^k||_1=2^k; 7!<10^4.
    return (r*(max(d,0)+6)+2*sum(h)+record.get('diagonal_power',0)
            +sum(record.get('row_line_exponents',[0]*INDEX))+4*max(m)
            +(20 if record.get('nonvanishing_method')=='coprime_kernel' else 9))


def threshold_power(record, epsilon):
    """Bound the coefficient contribution to the necessary cut.

    Coprime-kernel records additionally require the numerical common-zero
    bound returned by common_zero_threshold_power.
    """
    epsilon=Fraction(epsilon)
    assert epsilon>0
    # For n>=10^10 the bounded shifts cost less than a factor two,
    # already included in coefficient_bound. h<=n only weakens the
    # coefficient contribution E log(10)/log(h).
    m=record['row_multiplicities']
    assert 1000*(polynomial_degree(record)+sum(m))<10**10
    return max(10,coefficient_bound(record)*epsilon.denominator//epsilon.numerator+1)


def common_zero_threshold_power(record):
    """Return B excluding the coprime residual sections' common integer zeros.

    Cramer lifts have L1 norm <10^A, A=r(D+6)+15. Substituting
    Y=Z-X multiplies this bound by at most2^D. The nonzero resultant
    in X has L1 norm at most(2D)! (2^D 10^A)^(2D). Cauchy's bound,
    D<1000, and (2D)!<10^(8D) give the returned integer exponent.
    If both substituted polynomials are independent of X, coprimality
    already excludes every common zero and the same bound is vacuous.
    """
    if record.get('nonvanishing_method')!='coprime_kernel':
        return 0
    r=record['symmetric_jet_count']
    d=record['interpolation_degree']
    n=record['symmetric_monomial_count']
    assert 0<=d<1000 and r<100000 and n<10**6 and record['modular_prime']==251
    exponent=r*(d+6)+15
    return 2*d*exponent+d*d+8*d+2


def check_record(record, ranks=True):
    h,m=record['line_exponents'],record['row_multiplicities']
    assert len(h)==len(m)==INDEX
    assert all(type(x)is int and x>=0 for x in h+m)
    interpolation.LINE_EXPONENTS=h
    interpolation.ROW_MULTIPLICITIES=m
    interpolation.DEGREE=record['interpolation_degree']
    interpolation.PRIME=record['modular_prime']
    diagonal_power=record.get('diagonal_power',0)
    assert type(diagonal_power)is int and diagonal_power>=0
    row_lines=record.get('row_line_exponents',[0]*INDEX)
    assert len(row_lines)==INDEX and all(type(x)is int and x>=0 for x in row_lines)
    interpolation.residual=lambda x,y:max(0,m[x+y]-h[x]-h[y]-row_lines[x+y]
                                           -(diagonal_power if x==y else 0))
    assert interpolation.PRIME==251
    jets=interpolation.symmetric_jets()
    assert len(jets)==record['symmetric_jet_count']
    if jets:
        basis=interpolation.symmetric_basis()
        assert len(basis)==record['symmetric_monomial_count'] and len(jets)<=len(basis)
        coprime=record.get('nonvanishing_method')=='coprime_kernel'
        if ranks or coprime:
            matrix=interpolation.jet_matrix(basis,jets)
            if ranks:
                print(f"Rank {record['name']}: {len(jets)} x {len(basis)}",flush=True)
                assert matrix.rank()==len(jets)
            if coprime:
                from flint import nmod_mat,nmod_mpoly_ctx
                sections=record['kernel_sections']
                assert len(sections)==2 and all(len(v)==len(basis) for v in sections)
                assert all(type(x)is int and 0<=x<251 for v in sections for x in v)
                section_matrix=nmod_mat(len(basis),2,[x for pair in zip(*sections) for x in pair],251)
                assert matrix*section_matrix==nmod_mat(len(jets),2,251)
                context=nmod_mpoly_ctx.get(('X','Y'),modulus=251)
                f,g=[interpolation.polynomial(context,basis,v) for v in sections]
                degrees=[int(f.total_degree()),int(g.total_degree())]
                assert degrees==record['section_degrees']
                assert max(degrees)==interpolation.DEGREE and f.gcd(g).is_one()
    else:
        assert interpolation.DEGREE>=-1
        expected=(interpolation.DEGREE+2)**2//4 if interpolation.DEGREE>=0 else 0
        assert record['symmetric_monomial_count']==expected
    assert coefficient_bound(record)==record['coefficient_power_of_ten']


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--arithmetic-only',action='store_true')
    args=parser.parse_args()
    data=json.loads(DATA.read_text())
    for record in data['certificates']:
        assert record['rank_verified']
        check_record(record,not args.arithmetic_only)
    epsilon=Fraction(data['cut_slack'])
    maximum=max(threshold_power(r,epsilon)for r in data['certificates'])
    assert maximum==data['coefficient_threshold_power_of_ten']
    print(json.dumps({
        'index':INDEX,'certificates':len(data['certificates']),
        'line_products':sum(r['symmetric_jet_count']==0 for r in data['certificates']),
        'maximum_jet_rows':max(r['symmetric_jet_count']for r in data['certificates']),
        'cut_slack':str(epsilon),'coefficient_threshold_power_of_ten':maximum,
        'common_zero_threshold_power_of_ten':max(common_zero_threshold_power(r)
                                                   for r in data['certificates']),
        'ranks_checked':not args.arithmetic_only,
        'scope':'Polynomial necessary conditions; no whole-index conclusion in this file.',
    },indent=2))


if __name__=='__main__':main()

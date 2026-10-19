#!/usr/bin/env python3
"""Exact universal interpolation certificate making Erdos 699, i=14 effective.

The finite computations concern prime-cofactor alternatives and polynomial
jets. No rows or columns of Pascal's triangle are enumerated.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
from math import comb, isqrt
from pathlib import Path
import numpy as np

import erdos_699_index_13_interpolation_gcd as interpolation
from erdos_699_off_diagonal_pairs import certified_edges
from erdos_699_weighted_ramps import capacities

HERE = Path(__file__).resolve().parent
DATA = Path(__file__).with_suffix('.json')
INDEX = 14
PRIMES = (2, 3, 5, 7, 11, 13)
SCALE = 10000
LINE_EXPONENTS = (33,29,26,22,19,15,10,5,0,0,0,0,0,0)
ROW_MULTIPLICITIES = (66,65,62,58,55,53,51,46,41,37,33,30,27,24)
DEGREE = 56
PRIME = 65521


def normalize(edge):
    p,q = edge[:2]
    a,b = edge[2], edge[3] if len(edge)==4 else edge[2]
    return (p,q,a,b) if p<q else (q,p,b,a)


def available_edges():
    from erdos_699_prime_pair_savings import EDGES
    from erdos_699_bft_more_pairs import NEW_EDGES
    edges = [normalize(edge) for edge in EDGES+NEW_EDGES]
    old = json.loads((HERE/'erdos_699_bft_asymmetric_pair_table.json').read_text())
    for family in ('published_gcd_pairs','effective_gcd_pairs'):
        for row in old[family]:
            assert row['verified']
            edges.append(normalize(row['pair']+row['endpoints_scaled']))
    return set(edges+certified_edges())


def minimal_vectors(primes, edges):
    """Exact induction over disjunctions, retaining all minimal witnesses."""
    ids = {p:k for k,p in enumerate(primes)}
    vectors = np.zeros((1,len(primes)), dtype=np.int32)
    for p,q,a,b in sorted(edges):
        if p not in ids or q not in ids:
            continue
        left,right = ids[p],ids[q]
        satisfied = (vectors[:,left]>=a)|(vectors[:,right]>=b)
        rest = vectors[~satisfied]
        one,two = rest.copy(),rest.copy()
        one[:,left],two[:,right] = a,b
        candidates = np.unique(np.vstack([vectors[satisfied],one,two]),axis=0)
        candidates = candidates[np.argsort(np.sum(candidates,axis=1))]
        keep=[]
        for vector in candidates:
            if not keep or not np.any(np.all(np.array(keep)<=vector,axis=1)):
                keep.append(vector)
        vectors=np.array(keep)
    result = sorted(tuple(map(int,row)) for row in vectors)
    assert all(v[ids[p]]>=a or v[ids[q]]>=b
               for v in result for p,q,a,b in edges if p in ids and q in ids)
    return result


def certify(data, ranks=True):
    edges = list(map(tuple,data['pair_edges_scaled']))
    assert set(edges)<=available_edges()
    assert len(edges)==len(set(edges))==312
    assert all(a+b<SCALE for p,q,a,b in edges)
    vectors = minimal_vectors(PRIMES,edges)
    assert [list(v) for v in vectors]==data['minimal_vectors_scaled']
    h,m=LINE_EXPONENTS,ROW_MULTIPLICITIES
    assert all(type(x)is int and x>=0 for x in h+m)
    assert all(a>=b for a,b in zip(m,m[1:]))
    total_degree=2*sum(h)+DEGREE+1
    checked=0;worst=None
    for vector in vectors:
        for capacity in capacities(vector):
            checked+=1
            gain=SCALE*(sum(m)-total_degree)-sum(a*b for a,b in zip(m,capacity))
            candidate=(gain,vector,capacity)
            if worst is None or candidate<worst:worst=candidate
    gain_scaled,vector,capacity=worst
    assert gain_scaled==298 and gain_scaled>0
    interpolation.DEGREE=DEGREE
    interpolation.PRIME=PRIME
    interpolation.LINE_EXPONENTS=h
    interpolation.ROW_MULTIPLICITIES=m
    basis=interpolation.symmetric_basis();jets=interpolation.symmetric_jets()
    assert (len(jets),len(basis))==(831,841)
    assert all(PRIME%p for p in range(2,isqrt(PRIME)+1))
    if ranks:
        assert interpolation.jet_matrix(basis,jets).rank()==len(jets)
    # The same explicit adjugate/Hadamard estimate as the retained
    # interpolation-extensions proof, with index<100 and rank<100000.
    generator_factor=1+(INDEX*(INDEX+1)//2+INDEX+4)*comb(DEGREE+2,2)
    assert generator_factor<10**7
    constant_power=(len(jets)*(6+2*DEGREE)+1+len(PRIMES)*m[0]
                    +2*(INDEX-1)*m[0]+4*sum(h)+7)
    cap=3_400_000
    assert cap*gain_scaled>constant_power*SCALE
    assert 2*max(sum(t*x for t,x in enumerate(m)),INDEX-1)<10**10
    return {
        'index':INDEX,'prime_order':list(PRIMES),
        'line_exponents':list(h),'row_multiplicities':list(m),
        'interpolation_degree':DEGREE,'total_polynomial_degree':total_degree,
        'symmetric_jet_count':len(jets),'symmetric_monomial_count':len(basis),
        'modular_prime':PRIME,'symmetric_rank':len(jets),
        'pair_alternatives':len(edges),'minimal_vector_count':len(vectors),
        'capacity_configurations_checked':checked,
        'minimum_gain':str(Fraction(gain_scaled,SCALE)),
        'worst_vector_scaled':list(vector),'worst_capacities_scaled':list(capacity),
        'coefficient_bound_power_of_ten':constant_power,
        'algebraic_power_of_ten':cap,
        'source_thresholds':'Effective; not all numerically evaluated.',
        'conclusion':'All bad triples at index 14 lie below an effectively computable row bound.'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--arithmetic-only',action='store_true')
    parser.add_argument('--write',action='store_true')
    args=parser.parse_args()
    assert not(args.write and args.arithmetic_only)
    data=json.loads(DATA.read_text())
    result=certify(data,ranks=not args.arithmetic_only)
    if args.write:
        data['certificate']=result
        DATA.write_text(json.dumps(data,indent=2)+'\n')
    else:
        assert data['certificate']==result
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()

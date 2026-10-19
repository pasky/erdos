#!/usr/bin/env python3
"""Exact source, polynomial, and polyhedral certificates for Erdos 699, i=7.

The default run repeats every modular rank. --arithmetic-only verifies the
retained sources, every rational Farkas leaf, and complete case coverage.
The resulting stopping threshold is effective, not numerically evaluated.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from itertools import permutations
import json
from pathlib import Path

import erdos_699_index_13_interpolation_gcd as interpolation
from erdos_699_off_diagonal_clauses import rational_joint_clause
from erdos_699_rational_farkas import verify_infeasibility_certificate

HERE = Path(__file__).resolve().parent
DATA = Path(__file__).with_suffix('.json')
PRIMES = (2, 3, 5)
INDEX = 7
SCALE = 10000


def minimal_vectors(edges):
    vectors = [(0, 0, 0)]
    for p, q, a, b in edges:
        choices = ((PRIMES.index(p), a), (PRIMES.index(q), b))
        extended = set()
        for v in vectors:
            if any(v[k] >= value for k, value in choices):
                extended.add(v)
            else:
                for k, value in choices:
                    w = list(v); w[k] = value; extended.add(tuple(w))
        vectors = []
        for v in sorted(extended, key=lambda x: (sum(x), x)):
            if not any(all(a <= b for a, b in zip(u, v)) for u in vectors):
                vectors.append(v)
    return vectors


def total_degree(record):
    return (2*sum(record['line_exponents'])
            + sum(record.get('row_line_exponents', [0]*INDEX))
            + record.get('diagonal_power', 0)
            + max(0, record['interpolation_degree']+(0 if record.get('nonvanishing_method')=='coprime_kernel' else 1)))


def coefficient_exponent(record):
    """Conservative log10 bound for the polynomial divisibility constant."""
    h, m = record['line_exponents'], record['row_multiplicities']
    r, d = record['symmetric_jet_count'], record['interpolation_degree']
    assert r < 100000 and d < 1000 and max(h+m) < 10000
    return (r*(max(d,0)+6) + 2*sum(h)
            + sum(record.get('row_line_exponents', [0]*INDEX))
            + record.get('diagonal_power',0) + total_degree(record)
            + 7*max(m) + (20 if record.get('nonvanishing_method')=='coprime_kernel' else 9))


def common_zero_exponent(record):
    if record.get('nonvanishing_method') != 'coprime_kernel':
        return 0
    r, d = record['symmetric_jet_count'], record['interpolation_degree']
    assert 0 <= d < 1000 and r < 100000
    lifted_coefficient_exponent = r*(d+6)+15
    return 2*d*lifted_coefficient_exponent+d*d+8*d+2


def check_polynomial(record, ranks):
    h, m = record['line_exponents'], record['row_multiplicities']
    row_lines = record.get('row_line_exponents', [0]*INDEX)
    diagonal = record.get('diagonal_power', 0)
    assert len(h) == len(m) == len(row_lines) == INDEX
    assert all(type(x) is int and x >= 0 for x in h+m+row_lines+[diagonal])
    d = record['interpolation_degree']
    assert type(d) is int and d >= -1 and record['modular_prime'] == 251
    interpolation.LINE_EXPONENTS = h
    interpolation.ROW_MULTIPLICITIES = m
    interpolation.DEGREE = d
    interpolation.PRIME = 251
    interpolation.residual = lambda x,y: max(
        0, m[x+y]-h[x]-h[y]-row_lines[x+y]-(diagonal if x==y else 0))
    jets = interpolation.symmetric_jets()
    assert len(jets) == record['symmetric_jet_count']
    if jets:
        basis = interpolation.symmetric_basis()
        assert len(basis) == record['symmetric_monomial_count']
        assert len(jets) <= len(basis)
        matrix = None
        if ranks or record.get('nonvanishing_method') == 'coprime_kernel':
            matrix = interpolation.jet_matrix(basis,jets)
        if ranks:
            print(f"Rank {record['name']}: {len(jets)} x {len(basis)}", flush=True)
            assert matrix.rank() == len(jets)
        if record.get('nonvanishing_method') == 'coprime_kernel':
            from flint import nmod_mat, nmod_mpoly_ctx
            sections = record['kernel_sections']
            assert len(sections) == 2
            assert all(len(section)==len(basis) and all(type(c)is int and 0<=c<251 for c in section) for section in sections)
            section_matrix = nmod_mat(len(basis),2,[section[row] for row in range(len(basis)) for section in sections],251)
            assert matrix*section_matrix == nmod_mat(len(jets),2,251)
            ctx = nmod_mpoly_ctx.get(('X','Y'),modulus=251)
            ff,gg = [interpolation.polynomial(ctx,basis,section) for section in sections]
            assert not ff.is_zero() and not gg.is_zero() and ff.gcd(gg).is_one()
            degrees = [int(ff.total_degree()),int(gg.total_degree())]
            assert max(degrees) == d
            assert degrees == record['section_degrees']

    else:
        assert d >= -1
        assert record['symmetric_monomial_count'] == ((d+2)**2//4 if d>=0 else 0)
    if 'total_polynomial_degree' in record:
        assert total_degree(record) == record['total_polynomial_degree']
    return coefficient_exponent(record)


def check_pair_sources(edges):
    from erdos_699_prime_pair_savings import EDGES
    from erdos_699_bft_more_pairs import NEW_EDGES
    available = [(p,q,w,w) for p,q,w in EDGES+NEW_EDGES if p in PRIMES and q in PRIMES]
    rows = json.loads((HERE/'erdos_699_bft_asymmetric_pair_table.json').read_text())
    for family in ('published_gcd_pairs','effective_gcd_pairs'):
        for row in rows[family]:
            if set(row['pair']) <= set(PRIMES):
                assert row['verified']
                available.append(tuple(row['pair']+row['endpoints_scaled']))
    for p,q,a,b in edges:
        assert any((p,q)==(u,v) and a<=x and b<=y for u,v,x,y in available)


def check_joint_source(row):
    cert = row['certificate']; src = cert['source']; seed = src['seed']
    regenerated = rational_joint_clause(
        (seed['P'],seed['Q'],seed['a'],seed['b']), src['directions'],
        src['gcd_log_rate'], cert['components'], degree=cert['product_degree'],
        terms=src['gcd_terms'], block=cert['block_parameter'],
        scale=cert['rounding_scale'],
        gcd_sum_scale=src.get('gcd_sum_rounding_denominator'))
    for key in ('components','block_parameter','positive_part_intercepts',
                'positive_part_threshold','strict_source_margin_at_least','clauses'):
        assert regenerated[key] == cert[key], (row['id'],key)
    assert F(cert['positive_part_threshold']) > 0
    comp = cert['components']; powers = {p:(a,w,s) for p,a,w,s in comp}
    assert set(powers) <= set(PRIMES)
    hyp = row['hypothesis']
    if hyp['kind'] == 'pair':
        assert cert['product_degree'] == 1 and len(comp) == 2
        assert all(w==1 for p,a,w,s in comp)
    else:
        assert hyp['kind'] == 'ap' and cert['product_degree'] == 2
        middle, ends = hyp['middle'], hyp['endpoints']
        assert len(set([middle]+ends)) == 3 and set([middle]+ends)==set(powers)
        assert powers[middle][1] == 2
        assert all(powers[p][1]==1 and powers[p][2]!=powers[middle][2] for p in ends)


def source_active(row, positions):
    hyp = row['hypothesis']
    if hyp['kind'] == 'pair': return True
    at = dict(zip(PRIMES,positions)); middle = at[hyp['middle']]
    left,right = [at[p] for p in hyp['endpoints']]
    if left+right != 2*middle: return False
    assert 0 < abs(left*right-middle*middle) <= 36
    return True


def source_weights(row):
    cert = row['certificate']
    g = [F(cert['positive_part_intercepts'].get(str(p),'0')) for p in PRIMES]
    w = [next((c[2] for c in cert['components'] if c[0]==p),0) for p in PRIMES]
    return g,w,F(cert['positive_part_threshold'])


def source_branch_rows(row, mask):
    g,w,threshold = source_weights(row)
    members = [k for k in range(3) if w[k]]
    assert 0 < mask < 1 << len(members)
    rows = []; summed = [F(0)]*3; bound = -threshold
    for bit,k in enumerate(members):
        a = [F(0)]*3
        if mask >> bit & 1:
            a[k] = -w[k]; b = g[k]; summed[k] = -w[k]; bound += g[k]
        else:
            a[k] = w[k]; b = -g[k]
        rows.append((tuple(a),b))
    rows.append((tuple(summed),bound))
    return rows


def polynomial_rows(polynomials, positions, slack):
    rows = []
    for record in polynomials:
        m = record['row_multiplicities']
        rhs = total_degree(record)-sum(m[t] for t in range(INDEX) if t not in positions)+slack
        rows.append((tuple(F(m[t]) for t in positions),rhs))
    return rows


def check_forest(data):
    vectors = minimal_vectors(data['pair_edges_scaled'])
    assert [list(v) for v in vectors] == data['minimal_vectors_scaled']
    expected = {(p,v) for p in permutations(range(INDEX),3) if 0 in p for v in vectors}
    sources = {r['id']:r for r in data['sources']}
    assert len(sources) == len(data['sources'])
    polys = data['polynomials']; slack = F(data['polynomial_slack'])
    assert slack == F(1,10000) and data['upper_exponent'] == '1'
    seen = set(); counts = {'nodes':0,'leaves':0,'branches':0}; used_sources=set(); used_polys=set()
    for root in data['forest']:
        positions = tuple(root['positions']); vector = tuple(root['vector'])
        key = positions,vector
        assert key in expected and key not in seen; seen.add(key)
        base = polynomial_rows(polys,positions,slack)
        for k,value in enumerate(vector):
            lo = [F(0)]*3; lo[k] = -1; hi = [F(0)]*3; hi[k] = 1
            base.extend([(tuple(lo),F(-value,SCALE)),(tuple(hi),F(1))])
        stack = [(root['tree'],[])]
        while stack:
            node,region = stack.pop(); counts['nodes'] += 1
            if 'farkas' in node:
                assert set(node) == {'farkas'}
                assert verify_infeasibility_certificate(base+region,node['farkas'])
                used_polys.update(i for i in node['farkas']['support'] if i<len(polys))
                counts['leaves'] += 1
            else:
                assert set(node) == {'source','children'}
                source = sources[node['source']]
                assert source_active(source,positions)
                used_sources.add(node['source']); counts['branches'] += 1
                _,w,_ = source_weights(source)
                masks = set(range(1,1 << sum(bool(x) for x in w)))
                assert set(node['children']) == set(map(str,masks))
                for mask in masks:
                    stack.append((node['children'][str(mask)],region+source_branch_rows(source,mask)))
    assert seen == expected
    assert used_sources == set(sources)
    assert used_polys == set(range(len(polys)))
    return {'root_cases':len(seen),**counts,'used_joint_sources':len(used_sources),
            'used_polynomial_cuts':len(used_polys)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--arithmetic-only',action='store_true')
    args = parser.parse_args(); data = json.loads(DATA.read_text())
    assert data['index'] == INDEX and data['primes'] == list(PRIMES)
    from erdos_699_low_crt_row_zero import verify_index
    position_record = verify_index(INDEX)
    assert position_record['case_count'] == 780 and not position_record['surviving_candidates']
    check_pair_sources(data['pair_edges_scaled'])
    for source in data['sources']: check_joint_source(source)
    records = data['polynomials']+[data['collision_certificate']]
    bounds = [check_polynomial(row,not args.arithmetic_only) for row in records]
    collision = data['collision_certificate']; m = collision['row_multiplicities']
    assert collision.get('diagonal_power',0) == 0
    assert all(a>=b for a,b in zip(m,m[1:]))
    assert sum(m)-total_degree(collision)-m[0]-m[1] > 0
    result = check_forest(data)
    result.update({'index':INDEX,'polynomial_certificate_count':len(records),
                   'ranks_checked':not args.arithmetic_only,
                   'polynomial_slack':data['polynomial_slack'],
                   'maximum_jet_rows':max(r['symmetric_jet_count'] for r in records),
                   'algebraic_height_power_of_ten':max(max(bounds)//F(data['polynomial_slack'])+1,max(map(common_zero_exponent,records))),
                   'maximum_coprime_zero_power_of_ten':max(map(common_zero_exponent,records)),
                   'conclusion':'Every bad triple at index 7 has an effectively computable row bound.'})
    result['algebraic_height_power_of_ten'] = int(result['algebraic_height_power_of_ten'])
    print(json.dumps(result,indent=2))


if __name__ == '__main__': main()

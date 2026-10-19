#!/usr/bin/env python3
"""Exact interpolation and complete cofactor coverage for Erdos 699, i=12.

Default: recompute the modular ranks. --arithmetic-only checks exact coverage,
source matching, and coefficient estimates without repeating the ranks.
The remaining effective pair-source thresholds are not all numerically
instantiated here; the algebraic part of the stopping bound is explicit.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import permutations
import json
from math import prod
from pathlib import Path

import erdos_699_index_13_interpolation_gcd as interpolation

HERE = Path(__file__).resolve().parent
DATA = Path(__file__).with_suffix('.json')
PRIMES = (2, 3, 5, 7, 11)
SCALE = 10000
INDEX = 12


def extend(vectors, clause):
    expanded = set()
    for vector in vectors:
        if any(vector[k] >= value for k, value in clause):
            expanded.add(vector)
        else:
            for k, value in clause:
                updated = list(vector)
                updated[k] = value
                expanded.add(tuple(updated))
    result = []
    for vector in sorted(expanded, key=lambda v: (sum(v), v)):
        if not any(all(a <= b for a, b in zip(old, vector)) for old in result):
            result.append(vector)
    return result


def minimal_vectors(edges):
    vectors = [(0,) * len(PRIMES)]
    for p, q, a, b in edges:
        vectors = extend(vectors, [(PRIMES.index(p), a), (PRIMES.index(q), b)])
    return vectors


def degree(record):
    return 2*sum(record['line_exponents']) + max(0, record['interpolation_degree']+1)


def coefficient_bound(record):
    h, m = record['line_exponents'], record['row_multiplicities']
    r, d = record['symmetric_jet_count'], record['interpolation_degree']
    assert r < 100000 and d < 1000 and max(h+m) < 1000
    return r*(2*max(d,0)+7) + 3*sum(h) + 8*max(m) + 9


def gain_scaled(record, capacities):
    m = record['row_multiplicities']
    return SCALE*(sum(m)-degree(record))-sum(a*b for a,b in zip(m,capacities))


def capacities(positions, vector):
    result = [0]*INDEX
    groups = {}
    for k,t in enumerate(positions):
        groups.setdefault(t, []).append(k)
    for t, members in groups.items():
        result[t] = SCALE if len(members)>1 else SCALE-vector[members[0]]
    return result


def partitions(n):
    """Each set partition once, with blocks in order of their least members."""
    if n == 0:
        yield []
        return
    for blocks in partitions(n-1):
        for k in range(len(blocks)):
            yield [b+[n-1] if j==k else b[:] for j,b in enumerate(blocks)]
        yield blocks+[[n-1]]


def active_clause(rule, positions):
    at = dict(zip(PRIMES, positions))
    hypothesis = rule['hypothesis']
    if hypothesis['kind'] == 'AP':
        middle = hypothesis['middle_prime']
        left,right = hypothesis['endpoint_primes']
        if at[left]+at[right] != 2*at[middle]:
            return None
        gap = at[left]*at[right]-at[middle]**2
    else:
        left,right = hypothesis['equal_position_sums']
        if sum(at[p] for p in left) != sum(at[p] for p in right):
            return None
        gap = prod(at[p] for p in left)-prod(at[p] for p in right)
    if not gap:
        return None
    assert abs(gap) <= 121
    return [(PRIMES.index(int(p)), value) for p,value in rule['targets_scaled'].items()]


def check_sources(data):
    from erdos_699_prime_pair_savings import EDGES
    from erdos_699_bft_more_pairs import NEW_EDGES
    from erdos_699_bft_pair_extension import rational
    from erdos_699_product_thresholds import product_bound

    available = [(p,q,w,w) for p,q,w in EDGES+NEW_EDGES if p in PRIMES and q in PRIMES]
    pairs = json.loads((HERE/'erdos_699_bft_asymmetric_pair_table.json').read_text())
    for family in ('published_gcd_pairs','effective_gcd_pairs'):
        for row in pairs[family]:
            if set(row['pair']) <= set(PRIMES):
                assert row['verified']
                available.append(tuple(row['pair']+row['endpoints_scaled']))
    newer = json.loads((HERE/'erdos_699_twelve_rational_pairs.json').read_text())
    for row in newer['choices']:
        if 'ordinary_target_exponents' in row:
            targets = {int(p):Fraction(value) for p,value in row['ordinary_target_exponents'].items()}
            p,q = sorted(targets)
            scaled = [targets[p]*SCALE,targets[q]*SCALE]
            assert all(value.denominator == 1 for value in scaled)
            available.append((p,q,*map(int,scaled)))
    for edge in data['pair_edges_scaled']:
        p,q,a,b = edge
        assert any((p,q)==(u,v) and a<=x and b<=y for u,v,x,y in available), edge

    for rule in data['conditional_rules']:
        source = json.loads((HERE/Path(rule['source_file']).name).read_text())
        row = source[rule['source_kind']][rule['source_index']]
        assert row['seed'] == rule['seed']
        assert {p:int(Fraction(v)*SCALE) for p,v in row['targets'].items()} == rule['targets_scaled']
        hypothesis = rule['hypothesis']
        if rule['source_kind'] == 'choices':
            assert hypothesis['kind']=='AP'
            assert hypothesis['middle_prime']==row['middle_prime']
            assert set(hypothesis['endpoint_primes'])==set(map(int,row['endpoint_powers']))
        else:
            assert hypothesis['kind']=='equal_sums'
            assert hypothesis['equal_position_sums']==row['equal_position_sums']
        supplied = rule['numerical_product_bound']
        assert {str(component[0]):Fraction(component[-1])*SCALE
                for component in supplied['components']} == rule['targets_scaled']
        gcd = row['gcd_certificate']
        recomputed = product_bound(tuple(row['seed']), rational(gcd['ell_lower']), gcd['m0'],
                                   121,supplied['components'],degree=2,shift=11)
        assert recomputed == supplied
        assert recomputed['threshold_power_of_ten']==rule['threshold_power_of_ten']
    assert data['product_input_threshold_power_of_ten'] == max(
        rule['threshold_power_of_ten'] for rule in data['conditional_rules'])


def check_record(record, ranks):
    h,m = record['line_exponents'],record['row_multiplicities']
    assert len(h)==len(m)==INDEX and all(type(x)is int and x>=0 for x in h+m)
    interpolation.LINE_EXPONENTS=h
    interpolation.ROW_MULTIPLICITIES=m
    interpolation.DEGREE=record['interpolation_degree']
    interpolation.PRIME=record['modular_prime']
    rows=interpolation.symmetric_jets()
    assert len(rows)==record['symmetric_jet_count']
    if rows:
        basis=interpolation.symmetric_basis()
        assert len(basis)==record['symmetric_monomial_count'] and len(rows)<=len(basis)
        if ranks:
            print(f"Rank {record['name']}: {len(rows)} x {len(basis)}",flush=True)
            assert interpolation.jet_matrix(basis,rows).rank()==len(rows)
    else:
        assert record['interpolation_degree']==-1 and record['symmetric_monomial_count']==0
    assert coefficient_bound(record)==record['constant_power_of_ten']
    # For n>=10^10 the n versus n-11 correction costs less than a factor2,
    # included in the coefficient estimate's final constant.
    assert 1000*(sum(t*w for t,w in enumerate(m))+55*max(m)) < 10**10


def check_coverage(data):
    vectors=minimal_vectors(data['pair_edges_scaled'])
    assert [list(v)for v in vectors]==data['minimal_vectors_scaled']
    critical=set(map(tuple,data['critical_vectors_scaled']))
    assert critical<=set(vectors)
    records={row['name']:row for row in data['certificates']}
    assert len(records)==len(data['certificates'])
    used=set();minima={};largest_bound=0;applications=0

    def use(record,caps):
        nonlocal applications,largest_bound
        gain=gain_scaled(record,caps)
        assert gain>0,(record['name'],caps,gain)
        exponent=coefficient_bound(record)
        bound=exponent*SCALE//gain+1
        largest_bound=max(largest_bound,bound)
        minima[record['name']]=min(minima.get(record['name'],gain),gain)
        used.add(record['name']);applications+=1

    for name in ('universal_collisions','universal_outside','universal_others'):
        m=records[name]['row_multiplicities']
        assert all(a>=b for a,b in zip(m,m[1:]))
    partition_count=0
    for vector in vectors:
        for blocks in partitions(len(PRIMES)):
            if len(blocks)==len(PRIMES):
                continue
            group_caps=sorted([SCALE if len(block)>1 else SCALE-vector[block[0]]
                               for block in blocks],reverse=True)
            use(records['universal_collisions'],group_caps+[0]*(INDEX-len(group_caps)))
            partition_count+=1
        ordered=sorted([SCALE-value for value in vector],reverse=True)
        outside=[0]*INDEX
        for t,value in zip((0,1,2,3,5),ordered):outside[t]=value
        use(records['universal_outside'],outside)
        if vector not in critical:
            use(records['universal_others'],ordered+[0]*(INDEX-len(ordered)))

    branches=0;position_cases=0;expanded_cases=0
    candidates=list(records.values())
    def find(caps):
        suitable=[r for r in candidates if gain_scaled(r,caps)>0]
        return min(suitable,key=lambda r:Fraction(coefficient_bound(r),gain_scaled(r,caps))) if suitable else None
    for vector in sorted(critical):
        for positions in permutations(range(5)):
            position_cases+=1
            caps=capacities(positions,vector)
            record=find(caps)
            if record:
                use(record,caps);branches+=1
                continue
            descendants=[vector]
            for rule in data['conditional_rules']:
                clause=active_clause(rule,positions)
                if clause:descendants=extend(descendants,clause)
            expanded_cases+=1
            for descendant in descendants:
                caps=capacities(positions,descendant)
                record=find(caps)
                assert record is not None,(positions,vector,descendant)
                use(record,caps);branches+=1
    assert largest_bound<=data['algebraic_power_of_ten']
    return {
        'index':INDEX,'minimal_vectors':len(vectors),'critical_vectors':len(critical),
        'collision_partition_cases':partition_count,'labelled_position_cases':position_cases,
        'expanded_position_cases':expanded_cases,'position_certificate_applications':branches,
        'total_certificate_applications':applications,'used_certificate_count':len(used),
        'certificate_count':len(records),'minimum_gain':str(Fraction(min(minima.values()),SCALE)),
        'computed_algebraic_power_of_ten':largest_bound,
        'algebraic_power_of_ten':data['algebraic_power_of_ten'],
        'product_input_threshold_power_of_ten':data['product_input_threshold_power_of_ten'],
        'pair_threshold_scope':data['pair_threshold_scope'],
        'conclusion':'Every bad row for index12 is below an effectively computable threshold.',
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--arithmetic-only',action='store_true')
    args=parser.parse_args()
    data=json.loads(DATA.read_text())
    check_sources(data)
    for record in data['certificates']:check_record(record,not args.arithmetic_only)
    result=check_coverage(data)
    result['ranks_checked']=not args.arithmetic_only
    result['maximum_jet_matrix']=data['summary']['maximum_jet_matrix']
    result['distinct_pair_sources']=len(data['pair_edges_scaled'])
    result['conditional_product_sources']=len(data['conditional_rules'])
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()

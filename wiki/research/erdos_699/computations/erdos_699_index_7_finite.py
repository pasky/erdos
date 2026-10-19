#!/usr/bin/env python3
"""Combine the retained finite certificates at index seven.

This proves exclusion through10^100000001. An independently evaluated tail
at or below that exponent would give complete exclusion; no such tail is
assumed or supplied here. Existing modular ranks are reused, not recomputed.
"""
from fractions import Fraction as F
from itertools import combinations,permutations
import json
from pathlib import Path

import erdos_699_index_7_effective as polynomial

HERE=Path(__file__).resolve().parent
TAIL_POWER=100_000_001


def check_continuation(row):
    continuation=row['continuation']
    name=continuation['source_file']
    assert Path(name).name==name
    path=HERE/name
    previous=[r for r in json.loads(path.read_text())['records'] if r['pair']==row['pair']]
    assert len(previous)==1
    previous=previous[0]
    count=continuation['retained_anchor_count']
    assert count==previous['anchor_count']
    assert row['anchors'][:count]==previous['anchors']
    assert len(row['anchors'])==count+continuation['new_anchor_count']
    assert continuation['previous_height_cap_power_of_ten']==previous['height_cap_power_of_ten']
    assert continuation['all_retained_boundaries_certified_untruncated']
    r=row['cofactor_exponent_numerator'];s=row['cofactor_exponent_denominator'];c=s-r
    p,q=row['pair']
    for anchor in previous['anchors']:
        if anchor['method']=='exact boundary lines':
            A=p**anchor['p_exponent'];B=q**anchor['q_exponent']
            bits=max(A.bit_length(),B.bit_length())
            # height <2*max(A,B)^(1+s/c)<2^(3*oldcap)<10^oldcap.
            assert c+(c+s)*bits <3*c*previous['height_cap_power_of_ten']
    if continuation['new_anchor_count']:
        anchor=row['anchors'][count]
        assert [anchor['p_exponent'],anchor['q_exponent']]==previous['final_exponents']


def cofactor_stage(source_path,delta,source_cap,records,collision):
    data=json.loads(source_path.read_text());rows=data['records']
    expected=set(combinations((2,3,5),2))
    assert {tuple(r['pair']) for r in rows}==expected
    for row in rows:
        if 'continuation' in row:check_continuation(row)
        assert row['maximum_difference']>=6 and row['height_cap_power_of_ten']>=source_cap
        target=F(row.get('cofactor_exponent_numerator',1),
                 row.get('cofactor_exponent_denominator',row.get('reciprocal_exponent_denominator')))
        assert target>=delta
    constants={r['name']:polynomial.coefficient_exponent(r) for r in records}
    maximum=F(0);cases=[];used=set()
    for positions in permutations(range(7),3):
        if 0 not in positions:continue
        for zero in range(3):
            vector=[delta]*3;vector[zero]=F(0);options=[]
            for row in records:
                m=row['row_multiplicities']
                gain=(sum(m[t] for t in range(7) if t not in positions)
                      -polynomial.total_degree(row)+sum(m[t]*e for t,e in zip(positions,vector)))
                if gain>0:options.append((F(constants[row['name']],gain),row['name'],gain))
            assert options,(positions,vector)
            bound,name,gain=min(options);maximum=max(maximum,bound);used.add(name)
            cases.append({'positions':list(positions),'zero_cofactor_coordinate':zero,
                          'polynomial':name,'gain':str(gain),'height_exponent_bound':str(bound)})
    # A second decimal power safely absorbs n=h+6.
    distinct_row_cap=maximum.numerator//maximum.denominator+2
    m=collision['row_multiplicities'];gain=sum(m)-polynomial.total_degree(collision)-m[0]-m[1]
    assert gain>0 and all(a>=b for a,b in zip(m,m[1:]))
    collision_row_cap=polynomial.coefficient_exponent(collision)//gain+1
    row_cap=max(distinct_row_cap,collision_row_cap)
    assert max(r['height_threshold']+6 for r in rows)<10**row_cap
    assert row_cap<source_cap
    return {'source_file':source_path.name,
            'cofactor_exponent':str(delta),'input_cap_power_of_ten':source_cap,
            'position_cases':len(cases),'used_polynomials':sorted(used),
            'maximum_height_exponent_bound':str(maximum),'distinct_row_cap_power_of_ten':distinct_row_cap,
            'collision_row_cap_power_of_ten':collision_row_cap,'row_cap_power_of_ten':row_cap,'cases':cases}


def main():
    polypath=HERE/'erdos_699_index_7_effective.json'
    original=json.loads(polypath.read_text())
    records=[r for r in original['polynomials'] if r.get('nonvanishing_method')!='coprime_kernel']
    collision=original['collision_certificate']
    assert all(r.get('rank_verified') and r['actual_rank']==r['symmetric_jet_count'] for r in records+[collision])
    first=cofactor_stage(HERE/'erdos_699_prime_pair_strips_7_extended.json',F(11,25),TAIL_POWER,records,collision)
    assert first['row_cap_power_of_ten']==132427
    second=cofactor_stage(HERE/'erdos_699_prime_pair_strips_7_middle.json',F(47,100),first['row_cap_power_of_ten'],records,collision)
    assert second['row_cap_power_of_ten']==2057
    interval_path=HERE/'erdos_699_index_7_finite_intervals.json';intervals=json.loads(interval_path.read_text())
    assert intervals['i']==7 and intervals['supplied_tail_power_of_ten']>=second['row_cap_power_of_ten']
    assert F(intervals['minimum_certified_log_margin'])>0
    assert intervals['visited_intervals']==2*intervals['total_partition_leaves']-1
    for source in intervals['source_certificates']+intervals['triple_sources']:
        assert (HERE/source['file']).is_file(),source['file']
    output={'index':7,'finite_row_cap_power_of_ten':TAIL_POWER,
            'original_polynomial_file':polypath.name,
            'stages':[first,second],'interval_file':interval_path.name,
            'interval_cap_power_of_ten':intervals['inclusive_interval_cap_power_of_ten'],
            'certified_intervals':intervals['certified_intervals'],
            'row_congruence_intervals':intervals['intervals_excluded_by_row_congruences'],
            'exact_singleton_rows':intervals['exact_singleton_rows'],
            'exact_columns_checked':intervals['exact_columns_checked'],
            'new_ranks_recomputed':False,
            'conclusion':'No admissible bad triples at index7 have n<=10^100000001. The infinite tail is a separate theorem.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k not in ['stages']},indent=2))


if __name__=='__main__':main()

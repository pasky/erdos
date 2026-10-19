#!/usr/bin/env python3
"""Combine the retained finite index-nine proof through10^241547629.

The numerical infinite tail is separate and is not claimed by this file.
"""
from fractions import Fraction
from itertools import combinations
import json
from pathlib import Path

from erdos_699_weighted_ramps import certify

HERE=Path(__file__).resolve().parent
CAP=241_547_629


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


def main():
    path=HERE/'erdos_699_prime_pair_strips_9_extended.json'
    rows=json.loads(path.read_text())['records'];pairs=set(combinations((2,3,5,7),2))
    assert len(rows)==6 and {tuple(r['pair'])for r in rows}==pairs
    for row in rows:check_continuation(row)
    assert all(r['height_cap_power_of_ten']>=CAP and r['maximum_difference']>=8
               and (r['cofactor_exponent_numerator'],r['cofactor_exponent_denominator'])==(41,100) for r in rows)
    ramp=certify(9,6,[(*pair,4100)for pair in sorted(pairs)],'Finite K4 cofactor exponent41/100.')
    assert ramp['algebraic_cap_power_of_ten']==122 and ramp['minimum_gain']=='3/10'
    assert max(r['height_threshold']+8 for r in rows)<10**122
    interval_path=HERE/'erdos_699_index_9_finite_intervals.json';intervals=json.loads(interval_path.read_text())
    assert intervals['i']==9 and intervals['supplied_tail_power_of_ten']>=122
    assert intervals['visited_intervals']==2*intervals['total_partition_leaves']-1
    assert Fraction(intervals['minimum_certified_log_margin'])>0
    for source in intervals['source_certificates']:
        assert (HERE/source['file']).is_file(),source['file']
    result={'index':9,'finite_row_cap_power_of_ten':CAP,'initial_pair_file':path.name,
            'weighted_ramp_reduction':ramp,
            'interval_file':interval_path.name,
            'interval_cap_power_of_ten':intervals['inclusive_interval_cap_power_of_ten'],
            'certified_intervals':intervals['certified_intervals'],'exact_singleton_rows':intervals['exact_singleton_rows'],
            'exact_columns_checked':intervals['exact_columns_checked'],
            'conclusion':'No admissible bad index-nine triple has n<=10^241547629. A larger numerical tail remains separate.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()

#!/usr/bin/env python3
"""Bind the 790 index-nine joint sources to 647 sparse-cover direction groups.

This is input preparation only: no new gcd bounds, numerical thresholds,
height coverage, or whole-index assertion is computed here. The weakening
is exactly per_source_half_budget from the retained source-weakening file.
The old numerical tails remain available by explicit record and gcd indices.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
import gzip
import json
from pathlib import Path

HERE = Path(__file__).parent
DATA = Path(__file__).with_suffix('.json')
SOURCE_FILE = 'erdos_699_nine_cofactor_clauses.json.gz'
WEAKENING_FILE = 'erdos_699_nine_source_weakening.json'
OLD_NUMERICAL_FILE = 'erdos_699_index_9_joint_numerical.json.gz'
TARGET_HEIGHT_POWER = 241547627


def read_json(path):
    if path.suffix == '.gz':
        with gzip.open(path,'rt') as handle:
            return json.load(handle)
    return json.loads(path.read_text())


def build_inputs(directory=HERE):
    paths = {name:directory/name for name in (SOURCE_FILE,WEAKENING_FILE,OLD_NUMERICAL_FILE)}
    sources = read_json(paths[SOURCE_FILE])
    weakening = read_json(paths[WEAKENING_FILE])
    numerical = read_json(paths[OLD_NUMERICAL_FILE])
    assert sources['index'] == weakening['index'] == numerical['index'] == 9
    assert numerical['source_file'] == SOURCE_FILE
    assert numerical['weakening_file'] == WEAKENING_FILE
    assert SOURCE_FILE in weakening['input_files']
    assert numerical['proof_file'] in weakening['input_files']
    source_rows = sources['records']
    numeric_rows = numerical['records']
    gcd_rows = numerical['gcd_certificates']
    eta_by_source = {sid:Fraction(value) for sid,value in weakening['per_source_half_budget'].items()}
    assert len(source_rows) == len(numeric_rows) == len(eta_by_source) == 790
    old_by_id = {row['source_id']:(index,row) for index,row in enumerate(numeric_rows)}
    assert len(old_by_id) == 790
    assert {row['id'] for row in source_rows} == set(old_by_id) == set(eta_by_source)

    groups = defaultdict(list)
    source_record_index = {}
    old_numerical_record_index = {}
    old_gcd_certificate_index = {}
    old_tail_power_by_source = {}
    source_eta = {}
    for source_index,row in enumerate(source_rows):
        sid = row['id']
        assert sid not in source_record_index
        certificate = row['certificate']
        source = certificate['source']
        old_index,old = old_by_id[sid]
        gcd_index = old['gcd_certificate_index']
        gcd = gcd_rows[gcd_index]
        directions = tuple(source['directions'])
        eta = eta_by_source[sid]
        assert eta > 0
        assert tuple(old['directions']) == tuple(gcd['directions']) == directions
        assert old['seed'] == source['seed']
        assert old['components'] == certificate['components']
        assert old['hypothesis'] == row['hypothesis']
        assert Fraction(old['threshold_weakening']) == eta
        assert Fraction(old['original_positive_part_threshold']) == Fraction(certificate['positive_part_threshold'])
        assert Fraction(old['positive_part_threshold']) == Fraction(certificate['positive_part_threshold'])-eta
        assert Fraction(old['block_parameter']) == Fraction(certificate['block_parameter'])
        assert Fraction(old['original_gcd_log_rate']) == Fraction(source['gcd_log_rate'])
        assert Fraction(old['gcd_log_rate']) <= Fraction(gcd['ell_lower'])
        assert old['gcd_m0'] == gcd['m0']
        assert old['maximum_shift'] == 8
        kind = row['hypothesis']['kind']
        assert kind in ('pair','ap','four')
        assert old['gap_bound'] == (8 if kind == 'pair' else 64)
        binding = {
            'source_id':sid,'source_record_index':source_index,
            'source_eta':str(eta),'block_parameter':str(Fraction(certificate['block_parameter'])),
            'hypothesis_kind':kind,'product_degree':certificate['product_degree'],
            'gap_bound':old['gap_bound'],'maximum_shift':8,
            'old_numerical_record_index':old_index,'old_gcd_certificate_index':gcd_index,
            'old_tail_power_of_ten':old['threshold_power_of_ten'],
            'old_gcd_m0':old['gcd_m0'],'old_gcd_log_rate':str(Fraction(old['gcd_log_rate'])),
        }
        groups[directions].append(binding)
        source_record_index[sid] = source_index
        old_numerical_record_index[sid] = old_index
        old_gcd_certificate_index[sid] = gcd_index
        old_tail_power_by_source[sid] = old['threshold_power_of_ten']
        source_eta[sid] = str(eta)
    assert len(groups) == 647
    records = []
    group_index_by_source = {}
    for group_index,directions in enumerate(sorted(groups)):
        bindings = groups[directions]
        ids = [binding['source_id'] for binding in bindings]
        for sid in ids:
            assert sid not in group_index_by_source
            group_index_by_source[sid] = group_index
        records.append({
            'group_index':group_index,'directions':list(directions),
            'direction_key':','.join(map(str,directions)),
            'source_ids':ids,'source_bindings':bindings,
            'source_count':len(bindings),
            'minimum_eta':str(min(Fraction(binding['source_eta']) for binding in bindings)),
            'maximum_old_tail_power_of_ten':max(binding['old_tail_power_of_ten'] for binding in bindings),
            'old_gcd_certificate_indices':sorted({binding['old_gcd_certificate_index'] for binding in bindings}),
        })
    assert len(group_index_by_source) == 790
    return {
        'index':9,'height_variable':sources['height_variable'],
        'scope':'Input bindings for a future sparse height cover; no new coverage is claimed.',
        'target_global_height_power_of_ten':TARGET_HEIGHT_POWER,
        'source_file':SOURCE_FILE,'weakening_file':WEAKENING_FILE,
        'old_numerical_file':OLD_NUMERICAL_FILE,'input_files':list(paths),
        'weakening_field':'per_source_half_budget',
        'source_count':790,'direction_group_count':647,
        'old_gcd_certificate_count':len(gcd_rows),
        'source_eta':source_eta,
        'source_record_index_by_id':source_record_index,
        'old_numerical_record_index_by_id':old_numerical_record_index,
        'old_gcd_certificate_index_by_id':old_gcd_certificate_index,
        'old_tail_power_of_ten_by_id':old_tail_power_by_source,
        'group_index_by_source_id':group_index_by_source,
        'records':records,
    }


def summary(data):
    return {
        'source_count':data['source_count'],
        'direction_group_count':data['direction_group_count'],
        'old_gcd_certificate_count':data['old_gcd_certificate_count'],
        'target_global_height_power_of_ten':data['target_global_height_power_of_ten'],
        'maximum_old_tail_power_of_ten':max(data['old_tail_power_of_ten_by_id'].values()),
        'old_tails_already_below_target':sum(cap <= TARGET_HEIGHT_POWER for cap in data['old_tail_power_of_ten_by_id'].values()),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write',action='store_true')
    args = parser.parse_args()
    result = build_inputs()
    if args.write:
        DATA.write_text(json.dumps(result,indent=2)+'\n')
    else:
        assert json.loads(DATA.read_text()) == result
    print(json.dumps(summary(result),indent=2))


if __name__ == '__main__':
    main()

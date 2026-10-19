"""Shorter witness blocks for all 790 frozen index-nine joint clauses.

The intercepts and per_source_half_budget weakenings stay unchanged.
--check regenerates the retained uniform gcd and numerical certificates.
"""
from collections import defaultdict
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
import argparse
import gzip
import json
import time

from mpmath import iv
from erdos_699_nine_block_adjustment import prepare, joint_clause_threshold
from erdos_699_off_diagonal_gcd_sharp import gcd_exponent_lower
from erdos_699_off_diagonal_pade import rational

HERE = Path(__file__).parent
SOURCE = 'erdos_699_nine_cofactor_clauses.json.gz'
WEAKENING = 'erdos_699_nine_source_weakening.json'
OLD = 'erdos_699_index_9_joint_numerical.json.gz'
OUTPUT = Path(__file__).with_suffix('.json.gz')
TARGET = 241547627
TERMS = 10000
HELPERS = ('erdos_699_nine_block_adjustment.py', 'erdos_699_off_diagonal_gcd_sharp.py')


def load(name):
    path = HERE / name
    return json.loads(gzip.decompress(path.read_bytes())) if name.endswith('.gz') else json.loads(path.read_text())


def save(result):
    payload = (json.dumps(result, sort_keys=True, separators=(',', ':')) + '\n').encode()
    OUTPUT.write_bytes(gzip.compress(payload, mtime=0))


def inputs():
    source, weakening, old = map(load, (SOURCE, WEAKENING, OLD))
    assert source['index'] == weakening['index'] == old['index'] == 9
    sources = {row['id']: row for row in source['records']}
    previous = {row['source_id']: row for row in old['records']}
    eta = weakening['per_source_half_budget']
    assert len(sources) == len(source['records']) == len(previous) == len(eta) == 790
    assert set(sources) == set(previous) == set(eta)
    for name, row in sources.items():
        assert name.startswith('source_') and len(name) == 11
        assert F(row['certificate']['positive_part_threshold']) - F(eta[name]) == F(weakening['modified_thresholds'][name])
        assert row['hypothesis']['kind'] in ('pair', 'ap', 'four')
    return sources, eta, previous


def evaluate(source, prepared, analytic, eta):
    kind = source['hypothesis']['kind']
    return joint_clause_threshold(source['certificate'], analytic['m0'],
        gap=8 if kind == 'pair' else 64, maximum_shift=8,
        gcd_log_rate=analytic['ell_lower'], threshold_weakening=eta,
        prepared=prepared)


def build(target_only=False):
    sources, eta, previous = inputs()
    print(json.dumps({'index': 9, 'source_count': len(sources), 'target_K': TARGET,
                      'maximum_shift': 8, 'gap_bounds': [8, 64]}), flush=True)
    started = time.monotonic()
    records = []
    result = {'index': 9, 'height_variable': 'h=n-8',
        'scope': 'Unchanged frozen index-nine joint clauses using shorter integer Pade witnesses.',
        'target_height_power_of_ten': TARGET,
        'input_files': [SOURCE, WEAKENING, OLD],
        'helper_files': list(HELPERS),
        'records': records}
    direct = 0
    for name, source in sources.items():
        prepared = prepare(source['certificate'], threshold_weakening=eta[name])
        product = rational(F(prepared['witness_block_parameter'])) * TARGET * iv.log(10)
        m0 = int(product.a) - 1
        assert product >= m0 + 1 and m0 >= 2
        analytic = gcd_exponent_lower(*prepared['directions'], terms=TERMS, m0=m0)
        row = {'source_id': name, 'prepared': prepared, 'target_gcd_certificate': analytic,
               'old_threshold_power_of_ten': previous[name]['threshold_power_of_ten']}
        # This lower margin is sufficient; a failure only means that this
        # inexpensive target test did not certify the source.
        available = F(prepared['new_uniform_margin_lower']) + F(prepared['witness_block_parameter']) * (
            F(analytic['ell_lower']) - F(prepared['original_gcd_log_rate']))
        bound = evaluate(source, prepared, analytic, eta[name]) if available > 0 else None
        success = bound is not None and bound['threshold_power_of_ten'] <= TARGET
        row['directly_valid_at_target'] = success
        if bound is not None:
            row['target_numerical_certificate'] = bound
        direct += success
        records.append(row)
        if len(records) % 50 == 0:
            save(result)
            print(json.dumps({'target_sources': len(records), 'direct': direct,
                              'seconds': round(time.monotonic()-started, 1)}), flush=True)
    result['target_summary'] = {'sources': len(records), 'directly_valid': direct,
        'remaining_source_ids': [r['source_id'] for r in records if not r['directly_valid_at_target']],
        'improved_source_margin_count': sum(F(r['prepared']['new_uniform_margin_lower']) > F(r['prepared']['old_uniform_margin_lower']) for r in records),
        'maximum_margin_factor': max(float(F(r['prepared']['new_uniform_margin_lower']) / F(r['prepared']['old_uniform_margin_lower'])) for r in records)}
    save(result)
    print(json.dumps({k:v for k,v in result['target_summary'].items() if k != 'remaining_source_ids'}), flush=True)
    if target_only:
        return result
    grouped = defaultdict(list)
    for row in records:
        grouped[tuple(row['prepared']['directions'])].append(row)
    gcd_records = []
    result['uniform_gcd_records'] = gcd_records
    for directions, rows in sorted(grouped.items()):
        required = max(F(row['prepared']['requested_gcd_log_rate']) for row in rows)
        for exponent in range(5, 19):
            analytic = gcd_exponent_lower(*directions, terms=TERMS, m0=10**exponent)
            if F(analytic['ell_lower']) > required:
                break
        else:
            raise AssertionError(('No uniform rate', directions, str(required)))
        upper = analytic['m0']
        for m0 in (2*(upper//10), 5*(upper//10)):
            if m0 < 10**5:
                continue
            trial = gcd_exponent_lower(*directions, terms=TERMS, m0=m0)
            if F(trial['ell_lower']) > required:
                analytic = trial
                break
        gcd_records.append({'directions': list(directions), 'required_log_rate': str(required),
                            'analytic_certificate': analytic, 'source_ids': [r['source_id'] for r in rows]})
        for row in rows:
            row['uniform_numerical_certificate'] = evaluate(sources[row['source_id']], row['prepared'], analytic, eta[row['source_id']])
        if len(gcd_records) % 50 == 0:
            save(result)
            print(json.dumps({'uniform_directions': len(gcd_records), 'seconds': round(time.monotonic()-started, 1)}), flush=True)
    maximum = max(r['uniform_numerical_certificate']['threshold_power_of_ten'] for r in records)
    result['uniform_summary'] = {'directions': len(gcd_records), 'sources': len(records),
        'maximum_threshold_power_of_ten': maximum,
        'maximum_m0': max(r['analytic_certificate']['m0'] for r in gcd_records),
        'improved_threshold_count': sum(r['uniform_numerical_certificate']['threshold_power_of_ten'] < r['old_threshold_power_of_ten'] for r in records),
        'maximizing_sources': [r['source_id'] for r in records if r['uniform_numerical_certificate']['threshold_power_of_ten'] == maximum]}
    save(result)
    print(json.dumps(result['uniform_summary'], indent=2), flush=True)
    return result


def check():
    sources, eta, previous = inputs()
    result = load(OUTPUT.name)
    assert result['index'] == 9 and result['target_height_power_of_ten'] == TARGET
    for key in ('input_files', 'helper_files'):
        for name in result[key]:
            assert (HERE/name).is_file(), name
    groups = {tuple(r['directions']): r for r in result['uniform_gcd_records']}
    assert len(groups) == result['uniform_summary']['directions']
    for group in groups.values():
        analytic = group['analytic_certificate']
        replay = gcd_exponent_lower(*analytic['directions'], terms=analytic['terms'], m0=analytic['m0'],
            scale=analytic['rounding_denominator'], root_scale=analytic['root_scale'])
        assert replay == analytic and F(analytic['ell_lower']) > F(group['required_log_rate'])
    assert {r['source_id'] for r in result['records']} == set(sources)
    assert len(result['records']) == 790
    for row in result['records']:
        name = row['source_id']
        prepared = prepare(sources[name]['certificate'], threshold_weakening=eta[name])
        assert prepared == row['prepared']
        group = groups[tuple(prepared['directions'])]
        assert name in group['source_ids']
        assert evaluate(sources[name], prepared, group['analytic_certificate'], eta[name]) == row['uniform_numerical_certificate']
        if row['directly_valid_at_target']:
            direct_gcd = row['target_gcd_certificate']
            assert gcd_exponent_lower(*direct_gcd['directions'], terms=direct_gcd['terms'],
                m0=direct_gcd['m0'], scale=direct_gcd['rounding_denominator'],
                root_scale=direct_gcd['root_scale']) == direct_gcd
            direct = evaluate(sources[name], prepared, direct_gcd, eta[name])
            assert direct == row['target_numerical_certificate']
            assert direct['threshold_power_of_ten'] <= TARGET
    maximum = max(r['uniform_numerical_certificate']['threshold_power_of_ten'] for r in result['records'])
    assert maximum == result['uniform_summary']['maximum_threshold_power_of_ten']
    print(json.dumps({'index': 9, 'sources_checked': 790, 'gcd_directions_checked': len(groups), 'maximum_K': maximum}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--target-only', action='store_true')
    args = parser.parse_args()
    if args.check:
        check()
    else:
        build(target_only=args.target_only)

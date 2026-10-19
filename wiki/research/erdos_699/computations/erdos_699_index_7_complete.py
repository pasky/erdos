# evidence: entry
"""Join the index-seven finite exclusion to all numerical source covers.

This checker requires complete source-cover data: a partial run or any gap
fails. It reuses retained interpolation ranks and the completed finite row
certificates. The individual source drivers expose full gcd/chain replay.
"""
import argparse
from fractions import Fraction as F
import gzip
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).parent
OUTPUT = Path(__file__).with_suffix('.json')
TMP = Path(__file__).resolve().parents[4]/'tmp'/'erdos699'
COMPACT_CACHE = TMP/'compact-prime-prefix-10000000000'
JOINT = 'erdos_699_index_7_height_cover.json'


def load(name):
    if name.endswith('.gz'):
        with gzip.open(HERE/name, 'rt') as handle:
            return json.load(handle)
    return json.loads((HERE/name).read_text())


def report():
    original_name = 'erdos_699_index_7_effective.json'
    forest_name = 'erdos_699_index_7_relaxed_sources.json'
    initial_name = 'erdos_699_index_7_initial_height_cover.json.gz'
    joint_name = JOINT
    direct_name = 'erdos_699_index_7_reblocked_numerical.json'
    finite_name = 'erdos_699_index_7_finite.json'
    original, forest, initial, joint, direct, finite = map(load, (
        original_name, forest_name, initial_name, joint_name, direct_name, finite_name))
    sources = {row['id']: row for row in original['sources']}
    assert len(sources) == 258
    assert joint['selection_directions'] is None
    assert joint['summary']['gaps'] == []

    from erdos_699_index_7_initial_height_cover import check as check_initial
    initial_result = check_initial(initial)
    from erdos_699_index_7_height_cover import verify as check_joint
    joint_result = check_joint(joint)
    assert joint['direct_source_file'] == direct_name

    # These directly valid sources are omitted from the finite chains.
    # Verify their target-height gcd and finite-constant certificates here.
    from erdos_699_off_diagonal_gcd_sharp import gcd_exponent_lower
    from erdos_699_off_diagonal_reblocking import joint_clause_threshold
    direct_ids = set()
    direct_caps = []
    for row in direct['records']:
        if not row['directly_valid_at_target']:
            continue
        sid = row['source_id']
        assert sid not in direct_ids
        direct_ids.add(sid)
        source = sources[sid]
        analytic = row['target_gcd_certificate']
        assert analytic['directions'] == source['certificate']['source']['directions']
        replay = gcd_exponent_lower(*analytic['directions'],
            terms=analytic['terms'], m0=analytic['m0'],
            scale=analytic['rounding_denominator'], root_scale=analytic['root_scale'])
        assert replay == analytic
        numeric = joint_clause_threshold(source['certificate'], analytic['m0'],
            gap=6 if source['hypothesis']['kind'] == 'pair' else 36,
            maximum_shift=6, gcd_log_rate=analytic['ell_lower'],
            threshold_weakening=forest['source_eta'][sid], prepared=row['prepared'])
        assert numeric == row['target_numerical_certificate']
        assert numeric['threshold_power_of_ten'] <= direct['target_height_power_of_ten']
        direct_caps.append(numeric['threshold_power_of_ten'])
    assert len(direct_ids) == direct['target_summary']['directly_valid']
    sparse_ids = {sid for row in joint['records'] for sid in row['source_ids']}
    assert sparse_ids.isdisjoint(direct_ids)
    assert sparse_ids | direct_ids == set(sources)
    assert sparse_ids == set(joint['all_remaining_source_ids'])
    assert joint_result['verified_sparse_sources'] == len(sparse_ids)

    from erdos_699_index_7_relaxed_sources import certify as check_forest
    polynomial = check_forest(forest)
    assert json.loads(json.dumps(polynomial)) == forest['certificate']
    initial_pairs = load(initial['source_file'])
    assert [row['edge'] for row in initial_pairs['records']] == forest['certificate']['baseline_edges_scaled']
    assert initial_result['all_initial_alternatives'] == 5
    height_cap = max(initial_result['source_height_exponent'],
        joint_result['source_threshold_power_of_ten'], max(direct_caps, default=0),
        polynomial['algebraic_height_power_of_ten'])

    # Bind the completed finite calculation, including its two cofactor
    # reductions and every retained source for the final interval partition.
    assert finite['index'] == 7
    assert finite['original_polynomial_file'] == original_name
    intervals = load(finite['interval_file'])
    assert F(intervals['minimum_certified_log_margin']) > 0
    assert finite['certified_intervals'] == intervals['certified_intervals']
    assert finite['exact_singleton_rows'] == intervals['exact_singleton_rows']
    assert finite['exact_columns_checked'] == intervals['exact_columns_checked']
    assert intervals['visited_intervals'] == 2*intervals['total_partition_leaves']-1
    for source in intervals['source_certificates'] + intervals['triple_sources']:
        assert (HERE/source['file']).is_file(), source['file']
    finite_cap = finite['finite_row_cap_power_of_ten']
    current_cap = finite_cap
    for stage in finite['stages']:
        assert (HERE/stage['source_file']).is_file(), stage['source_file']
        assert stage['input_cap_power_of_ten'] == current_cap
        assert stage['row_cap_power_of_ten'] < current_cap
        current_cap = stage['row_cap_power_of_ten']
    assert current_cap <= intervals['supplied_tail_power_of_ten']
    assert height_cap >= 1 and finite_cap >= height_cap+1
    # n>10^(height_cap+1) implies n-6>10^height_cap, since 9*10^K>6.
    assert 9*10 > 6
    inputs = (original_name, forest_name, initial_name, joint_name, direct_name,
        finite_name, finite['interval_file'],
        'erdos_699_index_7_initial_height_cover.py',
        'erdos_699_index_7_height_cover.py',
        'erdos_699_index_7_relaxed_sources.py',
        'erdos_699_index_7_finite.py',
        'erdos_699_off_diagonal_reblocking.py',
        'erdos_699_index_7_polynomial_bounds.json',
        'erdos_699_index_7_nonvanishing.json')
    return {
        'index': 7, 'prime_threshold': 'p>=7',
        'height_variable': 'h=n-6', 'initial_pair_alternatives': 5,
        'joint_sources': len(sources), 'direct_joint_sources': len(direct_ids),
        'sparse_joint_sources': len(sparse_ids),
        'initial_witness_count': initial_result['witness_count'],
        'joint_witness_count': joint['summary']['witness_count'],
        'initial_source_height_power_of_ten': initial_result['source_height_exponent'],
        'joint_source_height_power_of_ten': joint_result['source_threshold_power_of_ten'],
        'polynomial_height_power_of_ten': polynomial['algebraic_height_power_of_ten'],
        'complete_tail_height_power_of_ten': height_cap,
        'finite_row_cap_power_of_ten': finite_cap,
        'farkas_leaf_count': polynomial['coverage']['leaves'],
        'certified_finite_intervals': finite['certified_intervals'],
        'exact_residual_rows': len(finite['exact_singleton_rows']),
        'exact_columns_checked': finite['exact_columns_checked'],
        'input_files': list(inputs),
        'conclusion': 'Every admissible triple (n,7,j) has a prime p>=7 dividing both binomial coefficients.',
    }


def replay_joint(cache, workers):
    """Regenerate every joint witness sequence and compare it with the record.

    The compact prime-log cache is built on first use. The joint driver's
    replay mode compares each regenerated witness count and sequence digest
    with the retained record; the same comparison is repeated here.
    """
    if not (cache/'metadata.json').is_file():
        from erdos_699_compact_prime_prefix import CompactPrimeLogIntervals
        CompactPrimeLogIntervals(10**10, base_limit=10**8).save(cache)
    output = TMP/'erdos_699_index_7_height_cover_replay.json'
    output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([sys.executable, str(HERE/'erdos_699_index_7_height_cover.py'),
        '--replay', '--reuse', str(HERE/JOINT), '--output', str(output),
        '--compact-cache', str(cache), '--workers', str(workers)], check=True, cwd=HERE)
    retained = load(JOINT)
    replayed = json.loads(output.read_text())
    by_direction = {tuple(row['directions']): row for row in replayed['records']}
    for row in retained['records']:
        fresh = by_direction[tuple(row['directions'])]
        assert fresh['witness_count'] == row['witness_count'], row['directions']
        assert fresh['witness_sequence_sha256'] == row['witness_sequence_sha256'], row['directions']
    assert replayed['summary']['witness_count'] == retained['summary']['witness_count']
    return {'replayed_directions': len(retained['records']),
            'replayed_witnesses': retained['summary']['witness_count']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    parser.add_argument('--quick', action='store_true',
        help='check the retained joint record bindings and endpoints only, without regenerating the witness sequences')
    parser.add_argument('--compact-cache', type=Path, default=COMPACT_CACHE)
    parser.add_argument('--workers', type=int, default=8)
    args = parser.parse_args()
    result = report()
    if args.write:
        OUTPUT.write_text(json.dumps(result, indent=2)+'\n')
    else:
        retained = load(OUTPUT.name)
        assert result == retained
    print(json.dumps(result, indent=2))
    if args.quick:
        print('quick: joint witness sequences not regenerated; the source and endpoint bindings of the retained joint record were checked')
    else:
        print(json.dumps(replay_joint(args.compact_cache, args.workers), indent=2))


if __name__ == '__main__':
    main()

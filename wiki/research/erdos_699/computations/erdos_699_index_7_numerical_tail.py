"""Combine the fully numerical source and polynomial bounds for index seven.

The default checks source bindings and every exact relaxed Farkas leaf.
--sources also regenerates the analytic gcd and finite-constant estimates.
Neither mode repeats interpolation ranks or enumerates binomial rows.
"""
import argparse
import contextlib
from fractions import Fraction as F
import io
import json
from pathlib import Path

HERE = Path(__file__).parent
OUTPUT = Path(__file__).with_suffix('.json')
JOINT = 'erdos_699_index_7_joint_numerical.json'


def load(name):
    return json.loads((HERE/name).read_text())


def report(*, sources=False):
    original_name = 'erdos_699_index_7_effective.json'
    relaxed_name = 'erdos_699_index_7_relaxed_sources.json'
    gcd_name = 'erdos_699_index_7_gcd_numerical.json'
    initial_name = 'erdos_699_index_7_base_pairs_numerical_relaxed.json'
    original, relaxed, gcd, initial = map(load,
        (original_name, relaxed_name, gcd_name, initial_name))
    joint = load(JOINT)
    for kind in ('source', 'relaxation', 'theta_helper'):
        assert (HERE/gcd[f'{kind}_file']).is_file(), kind
    assert gcd['source_file'] == original_name
    assert gcd['relaxation_file'] == relaxed_name
    assert gcd['source_eta'] == relaxed['source_eta']
    from erdos_699_index_7_gcd_numerical import shared_requirements
    expected = shared_requirements(original['sources'], relaxed['source_eta'])
    assert len(expected) == len(gcd['records']) == 210
    for group, required in zip(gcd['records'], expected):
        assert all(group[key] == value for key, value in required.items())
        analytic = group['analytic_gcd_certificate']
        assert analytic['directions'] == group['directions']
        assert F(analytic['ell_lower']) > F(group['requested_log_rate'])
        assert F(group['analytic_strict_rate_margin']) == (
            F(analytic['ell_lower'])-F(group['requested_log_rate']))
        if sources:
            from erdos_699_off_diagonal_gcd_sharp import gcd_exponent_lower
            replay = gcd_exponent_lower(*analytic['directions'],
                terms=analytic['terms'], m0=analytic['m0'],
                scale=analytic['rounding_denominator'],
                root_scale=analytic['root_scale'])
            assert replay == analytic
    by_direction = {tuple(row['directions']): row for row in gcd['records']}
    by_source = {row['source_id']: row for row in joint}
    assert len(joint) == len(by_source) == len(original['sources']) == 258
    assert set(by_source) == set(relaxed['source_eta'])
    for source in original['sources']:
        name, clause = source['id'], source['certificate']
        row = by_source[name]
        group = by_direction[tuple(clause['source']['directions'])]
        assert row['directions'] == group['directions']
        assert row['gcd_m0'] == group['analytic_gcd_certificate']['m0']
        assert F(row['gcd_log_rate']) == F(group['requested_log_rate'])
        assert F(row['threshold_weakening']) == F(relaxed['source_eta'][name])
        assert F(row['positive_part_threshold']) == (
            F(clause['positive_part_threshold'])-F(relaxed['source_eta'][name]))
        assert row['positive_part_intercepts'] == clause['positive_part_intercepts']
        assert F(row['block_parameter']) == F(clause['block_parameter'])
        assert row['gap_bound'] == (6 if source['hypothesis']['kind'] == 'pair' else 36)
        assert row['maximum_shift'] == 6
        if sources:
            from erdos_699_off_diagonal_explicit_clauses import joint_clause_threshold
            replay = joint_clause_threshold(clause, row['gcd_m0'],
                gap=row['gap_bound'], maximum_shift=6,
                gcd_log_rate=row['gcd_log_rate'],
                threshold_weakening=row['threshold_weakening'])
            assert replay == {key: value for key, value in row.items() if key != 'source_id'}
    from erdos_699_index_7_relaxed_sources import certify as certify_forest
    forest = certify_forest(relaxed)
    # JSON represents the checker's edge tuples as lists.
    assert json.loads(json.dumps(forest)) == relaxed['certificate']
    assert [row['edge'] for row in initial['records']] == relaxed['certificate']['baseline_edges_scaled']
    if sources:
        from erdos_699_index_7_base_pairs_numerical_relaxed import certify as certify_initial
        certify_initial(initial)
    initial_cap = max(row['numerical_threshold']['threshold_power_of_ten']
                      for row in initial['records'])
    assert initial_cap == initial['maximum_threshold_power_of_ten']
    original_joint_cap = max(row['threshold_power_of_ten'] for row in joint)
    adjusted_name = 'erdos_699_index_7_reblocked_numerical.json'
    adjusted = load(adjusted_name)
    for kind in ('original', 'relaxed', 'old_numerical'):
        assert (HERE/adjusted[f'{kind}_file']).is_file(), kind
    for name in adjusted['helper_files']:
        assert (HERE/name).is_file(), name
    assert {row['source_id'] for row in adjusted['records']} == set(by_source)
    assert len(adjusted['records']) == 258
    for row in adjusted['records']:
        numeric = row['uniform_numerical_certificate']
        old = by_source[row['source_id']]
        assert numeric['positive_part_intercepts'] == old['positive_part_intercepts']
        assert F(numeric['positive_part_threshold']) == F(old['positive_part_threshold'])
        assert F(numeric['threshold_weakening']) == F(old['threshold_weakening'])
        assert 0 < F(numeric['witness_block_parameter']) <= F(old['block_parameter'])
        assert F(numeric['denominator_cost_rate']) == max(F(0),
            F(numeric['positive_part_threshold'])-F(numeric['kappa_lower'])*(
                F(old['block_parameter'])-F(numeric['witness_block_parameter'])))
    if sources:
        from erdos_699_index_7_reblocked_numerical import check as check_adjustment
        with contextlib.redirect_stdout(io.StringIO()):
            check_adjustment()
    joint_cap = max(row['uniform_numerical_certificate']['threshold_power_of_ten']
                    for row in adjusted['records'])
    assert joint_cap == adjusted['uniform_summary']['maximum_threshold_power_of_ten']
    polynomial_cap = forest['algebraic_height_power_of_ten']
    height_cap = max(initial_cap, joint_cap, polynomial_cap)
    inputs = (original_name, relaxed_name, gcd_name, initial_name, JOINT,
        adjusted_name, 'erdos_699_index_7_reblocked_numerical.py',
        'erdos_699_off_diagonal_reblocking.py',
        'erdos_699_index_7_relaxed_sources.py',
        'erdos_699_index_7_gcd_numerical.py',
        'erdos_699_index_7_base_pairs_numerical_relaxed.py',
        'erdos_699_index_7_polynomial_bounds.py',
        'erdos_699_index_7_polynomial_bounds.json',
        'erdos_699_index_7_nonvanishing.py',
        'erdos_699_index_7_nonvanishing.json',
        'erdos_699_off_diagonal_explicit_clauses.py',
        'erdos_699_off_diagonal_gcd_sharp.py')
    return {
        'index': 7, 'height_variable': 'h=n-6',
        'covered_root_cases': forest['coverage']['roots'],
        'farkas_leaf_count': forest['coverage']['leaves'],
        'initial_pair_edges': 5, 'joint_source_count': 258,
        'gcd_direction_count': 210,
        'initial_pair_endpoint_weakening': relaxed['baseline_weakening'],
        'initial_source_threshold_power_of_ten': initial_cap,
        'joint_source_threshold_power_of_ten': joint_cap,
        'original_joint_source_threshold_power_of_ten': original_joint_cap,
        'polynomial_height_threshold_power_of_ten': polynomial_cap,
        'complete_height_cap_power_of_ten': height_cap,
        'complete_row_cap_power_of_ten': height_cap+1,
        'limiting_source': max(adjusted['records'], key=lambda row:
            row['uniform_numerical_certificate']['threshold_power_of_ten'])['source_id'],
        'input_files': list(inputs),
        'conclusion': 'Every bad triple at index seven has n below 10 raised to complete_row_cap_power_of_ten. The finite range below this bound is not excluded here.',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sources', action='store_true')
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    result = report(sources=args.sources)
    if args.write:
        OUTPUT.write_text(json.dumps(result, indent=2)+'\n')
    else:
        assert result == load(OUTPUT.name)
    print(json.dumps({key: result[key] for key in (
        'index', 'initial_source_threshold_power_of_ten',
        'joint_source_threshold_power_of_ten',
        'polynomial_height_threshold_power_of_ten',
        'complete_row_cap_power_of_ten')}, indent=2))


if __name__ == '__main__':
    main()

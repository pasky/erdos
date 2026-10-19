"""Combine all numerical source and polynomial bounds for index nine.

The exact relaxed baseline and branch forest are checked independently.
--sources also regenerates the analytic source constants; no option
recomputes interpolation ranks or scans binomial rows.
"""
from fractions import Fraction
from pathlib import Path
import argparse
import contextlib
import gzip
import io
import json

ROOT = Path(__file__).parent
OUTPUT = Path(__file__).with_suffix('.json')


def load(name):
    path = ROOT/name
    if name.endswith('.gz'):
        with gzip.open(path,'rt') as handle:
            return json.load(handle)
    return json.loads(path.read_text())


def report(*, sources=False):
    initial_name = 'erdos_699_index_9_initial_relaxed_numerical.json'
    joint_name = 'erdos_699_index_9_joint_numerical.json.gz'
    weakening_name = 'erdos_699_nine_source_weakening.json'
    initial, joint, weakening = map(load, (initial_name,joint_name,weakening_name))
    proof_name = 'erdos_699_nine_relaxed_forest.json.gz'
    baseline_name = 'erdos_699_index_9_relaxed_baseline.json'
    proof, baseline = map(load,(proof_name,baseline_name))
    assert initial['index'] == joint['index'] == weakening['index'] == proof['index'] == 9
    for data in (initial,weakening):
        for name in data['input_files']:
            assert (ROOT/name).is_file(), name
    for kind in ('source','proof','weakening'):
        assert (ROOT/joint[f'{kind}_file']).is_file(), kind
    assert joint['weakening_file'] == weakening_name
    assert joint['source_count'] == weakening['source_count'] == proof['joint_source_count'] == 790
    assert initial['baseline_pair_edge_count'] == 19
    assert initial['ordinary_source_count'] == proof['ordinary_source_count'] == 4
    assert initial['weakened_baseline_edges_scaled'] == baseline['pair_edges_scaled']
    assert Fraction(initial['baseline_endpoint_weakening']) == Fraction(
        proof['initial_pair_endpoint_weakening']) == Fraction(baseline['pair_weakening'])
    assert {name:Fraction(value) for name,value in proof['source_threshold_weakenings'].items()} == {
        name:Fraction(value) for name,value in weakening['per_source_half_budget'].items()}
    assert {row['source_id'] for row in joint['records']} == set(weakening['per_source_half_budget'])
    for row in joint['records']:
        name = row['source_id']
        assert row['threshold_weakening'] == weakening['per_source_half_budget'][name]
        assert Fraction(row['positive_part_threshold']) == Fraction(weakening['modified_thresholds'][name])
    if sources:
        from erdos_699_index_9_initial_relaxed_numerical import report as initial_report
        from erdos_699_index_9_joint_numerical import build as joint_report
        assert initial_report() == initial
        assert joint_report() == joint
    # Replay the exact weakened coverage, including every Farkas leaf.
    # This calls no interpolation-rank calculation.
    from erdos_699_nine_relaxed_forest import main as verify_forest
    with contextlib.redirect_stdout(io.StringIO()):
        verify_forest()
    polynomial_cap = proof['height_power_of_ten']
    initial_cap = initial['maximum_initial_threshold_power_of_ten']
    joint_cap = joint['maximum_joint_threshold_power_of_ten']
    assert initial_cap == max(row['threshold_power_of_ten'] for row in initial['records'])
    assert joint_cap == max(row['threshold_power_of_ten'] for row in joint['records'])
    original_initial_cap, original_joint_cap = initial_cap, joint_cap
    initial_cover_name = 'erdos_699_index_9_initial_height_cover.json.gz'
    adjusted_name = 'erdos_699_index_9_reblocked_numerical.json.gz'
    initial_cover, adjusted = map(load, (initial_cover_name, adjusted_name))
    from erdos_699_index_9_initial_height_cover import check as check_initial_cover
    initial_cover_result = check_initial_cover(initial_cover)
    initial_cap = initial_cover_result['source_height_exponent']
    assert initial_cover_result['initial_pair_sources'] == 11
    assert initial_cover_result['ordinary_AP_sources'] == 4
    assert adjusted['index'] == 9
    for key in ('input_files', 'helper_files'):
        for name in adjusted[key]:
            assert (ROOT/name).is_file(), name
    old_rows = {row['source_id']: row for row in joint['records']}
    assert len(adjusted['records']) == 790
    assert {row['source_id'] for row in adjusted['records']} == set(old_rows)
    for row in adjusted['records']:
        numeric, old = row['uniform_numerical_certificate'], old_rows[row['source_id']]
        assert numeric['positive_part_intercepts'] == old['positive_part_intercepts']
        assert numeric['directions'] == old['directions']
        assert Fraction(numeric['positive_part_threshold']) == Fraction(old['positive_part_threshold'])
        assert Fraction(numeric['threshold_weakening']) == Fraction(old['threshold_weakening'])
        assert 0 < Fraction(numeric['witness_block_parameter']) <= Fraction(old['block_parameter'])
        assert Fraction(numeric['denominator_cost_rate']) == max(Fraction(0),
            Fraction(numeric['positive_part_threshold'])-Fraction(numeric['kappa_lower'])*(
                Fraction(old['block_parameter'])-Fraction(numeric['witness_block_parameter'])))
    if sources:
        from erdos_699_index_9_reblocked_numerical import check as check_adjusted
        with contextlib.redirect_stdout(io.StringIO()):
            check_adjusted()
    joint_cap = max(row['uniform_numerical_certificate']['threshold_power_of_ten']
                    for row in adjusted['records'])
    assert joint_cap == adjusted['uniform_summary']['maximum_threshold_power_of_ten']
    height_cap = max(initial_cap,joint_cap,polynomial_cap)
    assert height_cap >= 1
    inputs = (initial_name,joint_name,weakening_name,
              initial_cover_name, adjusted_name,
              'erdos_699_index_9_initial_height_cover.py',
              'erdos_699_index_9_reblocked_numerical.py',
              'erdos_699_nine_block_adjustment.py',
              proof_name,baseline_name,
              'erdos_699_nine_relaxed_forest.py',
              'erdos_699_index_9_relaxed_baseline.py',
              'erdos_699_nine_newton_farkas_bound.json',
              'erdos_699_nine_newton_source_weakening.json',
              'erdos_699_index_9_nonvanishing.py',
              'erdos_699_index_9_nonvanishing.json',
              'erdos_699_nine_source_weakening.py',
              'erdos_699_index_9_initial_relaxed_numerical.py',
              'erdos_699_index_9_joint_numerical.py',
              'erdos_699_off_diagonal_explicit_clauses.py',
              'erdos_699_off_diagonal_gcd_sharp.py')
    return {
        'index':9, 'height_variable':'h=n-8',
        'covered_root_cases':proof['root_case_count'],
        'baseline_covered_root_cases':proof['baseline_covered_count'],
        'residual_root_cases':proof['residual_count'],
        'farkas_leaf_count':proof['farkas_leaf_count'],
        'initial_pair_edges':19, 'ordinary_product_sources':4,
        'joint_source_count':790,
        'initial_pair_endpoint_weakening':proof['initial_pair_endpoint_weakening'],
        'initial_source_threshold_power_of_ten':initial_cap,
        'joint_source_threshold_power_of_ten':joint_cap,
        'original_initial_source_threshold_power_of_ten':original_initial_cap,
        'original_joint_source_threshold_power_of_ten':original_joint_cap,
        'initial_source_witness_count':initial_cover_result['witness_count'],
        'polynomial_height_threshold_power_of_ten':polynomial_cap,
        'complete_height_cap_power_of_ten':height_cap,
        'complete_row_cap_power_of_ten':height_cap+1,
        'input_files':list(inputs),
        'conclusion':'Every bad triple at index nine has n below 10 raised to complete_row_cap_power_of_ten. The finite range below this bound is not excluded here.',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sources',action='store_true')
    parser.add_argument('--write',action='store_true')
    args = parser.parse_args()
    result = report(sources=args.sources)
    if args.write:
        OUTPUT.write_text(json.dumps(result,indent=2)+'\n')
    else:
        assert result == json.loads(OUTPUT.read_text())
    print(json.dumps({key:result[key] for key in (
        'index','initial_source_threshold_power_of_ten',
        'joint_source_threshold_power_of_ten','polynomial_height_threshold_power_of_ten',
        'complete_row_cap_power_of_ten')},indent=2))


if __name__=='__main__':
    main()

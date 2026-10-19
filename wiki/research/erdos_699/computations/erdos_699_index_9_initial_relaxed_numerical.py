#!/usr/bin/env python3
"""Numerical initial sources for the 1/10000 index-nine weakening.

This certifies source inequalities; whole-index coverage is checked
separately by the relaxed baseline and forest checkers.
Every baseline pair endpoint is lowered by exactly one scaled unit; the
four ordinary AP sources keep their original targets.
"""

from fractions import Fraction
import gzip
import json
from pathlib import Path

from erdos_699_index_9_initial_numerical import ordinary_records, baseline_bindings
from erdos_699_off_diagonal_clauses import rational_joint_clause
from erdos_699_off_diagonal_explicit_clauses import joint_clause_threshold
from erdos_699_off_diagonal_gcd_sharp import gcd_exponent_lower

HERE = Path(__file__).resolve().parent
DATA = Path(__file__).with_suffix('.json')

# Edge, oriented seed, components, directions, m0, rational block (or default).
PARAMETERS = (
    ((2, 7, 2756, 2756), (8, 7, 1, 1), ((2, 3, 1, 0), (7, 1, 1, 1)),
     (2, 1, 2), 10**8, None),
    ((2, 7, 2751, 3217), (8, 7, 1, 1), ((2, 3, 1, 0), (7, 1, 1, 1)),
     (32, 15, 32), 10**10, '3364970351/453677996022'),
    ((3, 7, 504, 504), (49, 243, 5, 1), ((3, 5, 1, 1), (7, 2, 1, 0)),
     (47, 32, 24), 10**6, None),
    ((3, 7, 501, 3270), (49, 243, 5, 1), ((7, 2, 1, 0), (3, 5, 1, 1)),
     (17, 11, 17), 10**9, '2246267374/363710676597'),
    ((5, 7, 2666, 2666), (25, 49, 2, 1), ((5, 2, 1, 0), (7, 2, 1, 1)),
     (2, 1, 2), 10**9, None),
    ((5, 7, 3930, 2662), (25, 49, 2, 1), ((5, 2, 1, 0), (7, 2, 1, 1)),
     (2, 1, 2), 10**10, '13832030462/220050684331'),
    ((2, 5, 2678, 2678), (128, 125, 1, 1), ((2, 7, 1, 0), (5, 3, 1, 1)),
     (79, 18, 79), 10**10, None),
)


def boxed_cost(clause, edge):
    targets = {str(p): Fraction(a, 10000) for p, a in zip(edge[:2], edge[2:])}
    assert clause['product_degree'] == 1
    assert all(m == 1 for p, power, m, side in clause['components'])
    assert {str(p) for p, power, m, side in clause['components']} == set(targets)
    return sum((max(Fraction(0), Fraction(value)+targets[p])
                for p, value in clause['positive_part_intercepts'].items()), Fraction(0))


def numerical_record(edge, clause, gcd, *, gcd_rate=None, provenance):
    cost = boxed_cost(clause, edge)
    old_threshold = Fraction(clause['positive_part_threshold'])
    assert cost < old_threshold
    weakening = (old_threshold-cost)/2
    new_threshold = old_threshold-weakening
    assert cost < new_threshold < old_threshold
    requested = Fraction(clause['source']['gcd_log_rate']) if gcd_rate is None else Fraction(gcd_rate)
    assert Fraction(gcd['ell_lower']) > requested
    numeric = joint_clause_threshold(
        clause, gcd['m0'], gap=8, maximum_shift=8,
        gcd_log_rate=requested, threshold_weakening=weakening)
    assert Fraction(numeric['positive_part_threshold']) > cost
    clause['source'].pop('gcd_eligible_t', None)
    return {
        'id': 'pair:'+':'.join(map(str, edge)), 'kind': 'pair',
        'edge_scaled': list(edge), 'provenance': provenance,
        'boxed_positive_part_upper_bound': str(cost),
        'threshold_weakening': str(weakening),
        'clause': clause, 'gcd_certificate': gcd,
        'numerical_clause_bound': numeric,
        'threshold_power_of_ten': numeric['threshold_power_of_ten'],
    }


def seven_records():
    records = []
    for edge, seed, components, directions, m0, block in PARAMETERS:
        gcd = gcd_exponent_lower(*directions, terms=10000, m0=m0)
        rate = Fraction(gcd['ell_lower'])-Fraction(1, 10**9)
        clause = rational_joint_clause(
            seed, directions, rate, components, terms=10000,
            scale=10**12, gcd_sum_scale=10**12,
            block=None if block is None else Fraction(block))
        row = numerical_record(edge, clause, gcd,
                               provenance='Explicit directed positive-part construction.')
        print(json.dumps({'source': row['id'], 'cap': row['threshold_power_of_ten']}), flush=True)
        records.append(row)
    return records


def other_pair_records():
    filename = 'erdos_699_index_7_base_pairs_numerical.json'
    source_data = json.loads((HERE/filename).read_text())
    records = []
    assert len(source_data['records']) == 5
    for original in source_data['records']:
        p, q, a, b = original['edge']
        edge = (p, q, a-1, b-1)
        if edge == (2, 5, 2678, 2678):
            # The coarser explicit construction above has a smaller cap.
            continue
        clause = original['clause']
        source = clause['source']
        cost = boxed_cost(clause, edge)
        gap = Fraction(clause['positive_part_threshold'])-cost
        assert gap > 0
        # The numerical clause loses gap/2 in its threshold. Spending
        # half of that gain on the gcd rate still leaves positive decay.
        requested = (Fraction(source['gcd_log_rate'])
                     - gap/(4*Fraction(clause['block_parameter'])))
        assert requested > 0
        for exponent in range(6, 15):
            gcd = gcd_exponent_lower(*source['directions'],
                                     terms=source['gcd_terms'], m0=10**exponent)
            if Fraction(gcd['ell_lower']) > requested:
                break
        else:
            raise AssertionError(('No sharp gcd start through 10^14', edge))
        row = numerical_record(edge, clause, gcd, gcd_rate=requested,
                               provenance={'file': filename, 'original_edge': original['edge']})
        print(json.dumps({'source': row['id'], 'cap': row['threshold_power_of_ten']}), flush=True)
        records.append(row)
    return records


def report():
    baseline = json.loads((HERE/'erdos_699_index_9_baseline.json').read_text())
    with gzip.open(HERE/'erdos_699_index_9_effective.json.gz', 'rt') as handle:
        proof = json.load(handle)
    original_edges = baseline['pair_edges_scaled']
    baseline['pair_edges_scaled'] = [[p, q, a-1, b-1] for p, q, a, b in original_edges]
    relaxed = json.loads((HERE/'erdos_699_index_9_relaxed_baseline.json').read_text())
    assert relaxed['index'] == 9
    assert relaxed['pair_edges_scaled'] == baseline['pair_edges_scaled']
    pairs = seven_records()+other_pair_records()
    bindings = baseline_bindings(baseline, pairs)
    ordinary = ordinary_records(proof)
    files = (
        'erdos_699_index_9_baseline.json', 'erdos_699_index_9_effective.json.gz',
        'erdos_699_index_9_relaxed_baseline.json',
        'erdos_699_index_7_base_pairs_numerical.json',
        'erdos_699_index_9_initial_numerical.py',
        'erdos_699_ap_cofactors.json', 'erdos_699_additional_product_cofactors.json',
        'erdos_699_bft_gcd_bounds.py', 'erdos_699_bft_explicit_thresholds.py',
        'erdos_699_product_thresholds.py', 'erdos_699_off_diagonal_clauses.py',
        'erdos_699_off_diagonal_explicit_clauses.py',
        'erdos_699_off_diagonal_gcd_sharp.py', 'erdos_699_off_diagonal_pade.py',
    )
    return {
        'index': 9, 'height_variable': 'h=n-8',
        'scope': 'Numerical sources for the relaxed index-nine proof; whole-index coverage is checked separately.',
        'coverage_checked_separately': True,
        'coverage_checkers': ['erdos_699_index_9_relaxed_baseline.py',
                              'erdos_699_nine_relaxed_forest.py'],
        'baseline_endpoint_weakening': '1/10000',
        'original_baseline_edges_scaled': original_edges,
        'weakened_baseline_edges_scaled': baseline['pair_edges_scaled'],
        'input_files': list(files),
        'baseline_pair_edge_count': len(bindings),
        'numerical_pair_source_count': len(pairs),
        'ordinary_source_count': len(ordinary),
        'baseline_bindings': bindings, 'records': pairs+ordinary,
        'maximum_initial_threshold_power_of_ten': max(row['threshold_power_of_ten'] for row in pairs+ordinary),
        'conclusion': 'The nineteen weakened initial pair edges and four unchanged ordinary AP sources all hold above the displayed numerical height.',
    }


if __name__ == '__main__':
    result = report()
    DATA.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'output': str(DATA),
                      'maximum_initial_threshold_power_of_ten': result['maximum_initial_threshold_power_of_ten'],
                      'coverage_checked_separately': True}, indent=2))

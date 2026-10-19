#!/usr/bin/env python3
"""Numerical thresholds for every initial source in the index-nine proof.

The height is h=n-8. Pair certificates use input gaps and shifts at most
eight. The four ordinary AP sources use (n-r-d)(n-r+d)-(n-r)^2=-d^2,
where 1<=|d|<=4, hence product gap at most sixteen.

This checks analytic parameters and exact source coverage, not polynomial
ranks or binomial rows. All endpoints of the retained proof are preserved.
"""

from fractions import Fraction
import gzip
import json
from pathlib import Path

from erdos_699_bft_gcd_bounds import gcd_exponent_lower as bft_gcd_bound
from erdos_699_bft_pair_extension import rational
from erdos_699_off_diagonal_explicit_clauses import joint_clause_threshold
from erdos_699_off_diagonal_explicit_pairs import pair_threshold
from erdos_699_off_diagonal_gcd_sharp import gcd_exponent_lower as sharp_gcd_bound
from erdos_699_off_diagonal_pade import growth_parameters
from erdos_699_product_thresholds import product_bound


HERE = Path(__file__).resolve().parent
DATA = Path(__file__).with_suffix('.json')

# These stronger alternatives each imply all retained edges for their pair.
# Prime labels follow the oriented seed; the final edge is sorted.
SEVEN_PARAMETERS = (
    ((2, 7, 2757, 3218), (2, 7), (8, 7, 1, 1), (152, 71, 152), 10**13),
    ((3, 7, 505, 3271), (7, 3), (49, 243, 5, 1), (65, 42, 65), 10**11),
    ((5, 7, 3931, 2667), (5, 7), (25, 49, 2, 1), (159, 79, 159), 10**12),
)


def pair_record(edge, primes, seed, directions, *, terms, m0):
    gcd = sharp_gcd_bound(*directions, terms=terms, m0=m0)
    rate = Fraction(gcd['ell_lower'])-Fraction(1, 10**9)
    _, _, source = growth_parameters(*seed, *directions, rate,
                                     terms=terms, sum_scale=10**12)
    source['primes'] = list(primes)
    bound = pair_threshold(source, edge, m0, gap=8, maximum_shift=8,
                           separate_terms=True,
                           integral_trim=Fraction(2, directions[1]),
                           near_limit=True)
    assert Fraction(gcd['ell_lower']) > rate
    assert edge[2]+edge[3] < 10000
    # If the two numerator positions coincide, coprimality of their prime
    # powers gives u_p*u_q>=h, which also excludes both upper bounds.
    source.pop('gcd_eligible_t')
    source['height_scope'] = 'Numerical threshold recorded below.'
    return {
        'id': 'pair:'+':'.join(map(str, edge)), 'kind': 'pair',
        'edge_scaled': list(edge), 'source': source,
        'gcd_certificate': gcd, 'numerical_pair_bound': bound,
        'threshold_power_of_ten': bound['threshold_power_of_ten'],
        'coincident_positions': 'u_p*u_q>=h and the two targets sum to less than one',
    }


def ordinary_records(proof):
    used = {node['source'] for root in proof['roots'] for node in root['tree']
            if 'source' in node}
    records = []
    for filename in ('erdos_699_ap_cofactors.json',
                     'erdos_699_additional_product_cofactors.json'):
        data = json.loads((HERE/filename).read_text())
        for key in ('choices', 'four_factor_choices'):
            for index, row in enumerate(data[key]):
                identifier = f'{filename}:{key}:{index}'
                if identifier not in used:
                    continue
                assert key == 'choices'
                gcd = row['gcd_certificate']
                assert bft_gcd_bound(
                    gcd['c'], gcd['d'], terms=gcd['terms'], m0=gcd['m0'],
                    scale=gcd['rounding_denominator'],
                    root_scale=gcd['root_scale']) == gcd
                middle, exponent = row['middle_prime'], row['middle_power']
                side = 0 if row['seed'][0] == middle**exponent else 1
                assert row['seed'][side] == middle**exponent
                assert row['seed'][2:4] == [1, 1]
                components = [
                    (middle, exponent, 2, side, row['targets'][str(middle)])
                ] + [
                    (int(prime), power, 1, 1-side, row['targets'][prime])
                    for prime, power in row['endpoint_powers'].items()
                ]
                bound = product_bound(
                    row['seed'], rational(gcd['ell_lower']), gcd['m0'],
                    16, components, degree=2, shift=8)
                records.append({
                    'id': identifier, 'kind': 'ordinary_ap',
                    'hypothesis': {'kind': 'ap', 'middle': middle,
                                   'endpoints': list(map(int, row['endpoint_powers']))},
                    'targets': row['targets'], 'gcd_certificate': gcd,
                    'numerical_product_bound': bound,
                    'threshold_power_of_ten': bound['threshold_power_of_ten'],
                })
    assert {row['id'] for row in records} == {
        'erdos_699_ap_cofactors.json:choices:0',
        'erdos_699_ap_cofactors.json:choices:1',
        'erdos_699_ap_cofactors.json:choices:3',
        'erdos_699_additional_product_cofactors.json:choices:10',
    }
    assert len(records) == proof['ordinary_source_count'] == 4
    return records


def baseline_bindings(baseline, pair_records):
    result = []
    for index, edge in enumerate(baseline['pair_edges_scaled']):
        choices = [row for row in pair_records
                   if row['edge_scaled'][:2] == edge[:2]
                   and all(a >= b for a, b in zip(row['edge_scaled'][2:], edge[2:]))]
        assert choices, ('Uncovered initial pair source', edge)
        chosen = min(choices, key=lambda row: row['threshold_power_of_ten'])
        result.append({'baseline_edge_index': index, 'edge_scaled': edge,
                       'numerical_source_id': chosen['id']})
    assert len(result) == 19
    return result


def reused_pair_records():
    """Recheck the five sources shared with index seven at gap/shift eight."""
    filename = 'erdos_699_index_7_base_pairs_numerical.json'
    data = json.loads((HERE/filename).read_text())
    assert len(data['records']) == 5
    records = []
    for row in data['records']:
        edge = row['edge']
        p, q, a, b = edge
        targets = {str(p): Fraction(a, 10000), str(q): Fraction(b, 10000)}
        clause = row['clause']
        source = clause['source']
        assert clause['product_degree'] == 1
        assert all(m == 1 for _, _, m, _ in clause['components'])
        assert {str(p) for p, _, _, _ in clause['components']} == set(targets)
        cost = sum((max(Fraction(0), Fraction(value)+targets[prime])
                    for prime, value in clause['positive_part_intercepts'].items()),
                   Fraction(0))
        assert cost == Fraction(row['boxed_positive_part_upper_bound'])
        assert cost < Fraction(clause['positive_part_threshold'])
        # Reuse only the clause parameters. Its new uniform gcd proof is
        # independent of index seven's finite bootstrap and source caps.
        for exponent in range(8, 16):
            analytic = sharp_gcd_bound(*source['directions'],
                                       terms=source['gcd_terms'], m0=10**exponent)
            if Fraction(analytic['ell_lower']) > Fraction(source['gcd_log_rate']):
                break
        else:
            raise AssertionError(('No numerical gcd start through 10^15', edge))
        numeric = joint_clause_threshold(
            clause, analytic['m0'],
            gap=8, maximum_shift=8, gcd_log_rate=Fraction(analytic['ell_lower']))
        records.append({
            'id': 'pair:'+':'.join(map(str, edge)), 'kind': 'pair',
            'edge_scaled': edge, 'source_file': filename,
            'source_edge': edge,
            'boxed_positive_part_upper_bound': row['boxed_positive_part_upper_bound'],
            'positive_part_threshold': row['clause']['positive_part_threshold'],
            'gcd_certificate': analytic,
            'numerical_clause_bound': numeric,
            'threshold_power_of_ten': numeric['threshold_power_of_ten'],
        })
    return records


def report():
    baseline = json.loads((HERE/'erdos_699_index_9_baseline.json').read_text())
    with gzip.open(HERE/'erdos_699_index_9_effective.json.gz', 'rt') as handle:
        proof = json.load(handle)
    assert baseline['index'] == proof['index'] == 9
    pairs = reused_pair_records()
    for edge, primes, seed, directions, m0 in SEVEN_PARAMETERS:
        pairs.append(pair_record(edge, primes, seed, directions,
                                 terms=100000, m0=m0))
    bindings = baseline_bindings(baseline, pairs)
    ordinary = ordinary_records(proof)
    files = (
        'erdos_699_index_9_baseline.json',
        'erdos_699_index_9_effective.json.gz',
        'erdos_699_index_7_base_pairs_numerical.py',
        'erdos_699_index_7_base_pairs_numerical.json',
        'erdos_699_ap_cofactors.json',
        'erdos_699_additional_product_cofactors.json',
        'erdos_699_bft_gcd_bounds.py',
        'erdos_699_bft_explicit_thresholds.py',
        'erdos_699_product_thresholds.py',
        'erdos_699_off_diagonal_explicit_pairs.py',
        'erdos_699_off_diagonal_explicit_clauses.py',
        'erdos_699_off_diagonal_gcd_numeric.py',
        'erdos_699_off_diagonal_gcd_sharp.py',
        'erdos_699_off_diagonal_pade.py',
    )
    return {
        'index': 9, 'height_variable': 'h=n-8',
        'scope': 'Every baseline pair edge and each ordinary source used in the retained index-nine branch trees.',
        'input_files': list(files),
        'baseline_pair_edge_count': len(bindings),
        'numerical_pair_source_count': len(pairs),
        'ordinary_source_count': len(ordinary),
        'baseline_bindings': bindings,
        'records': pairs+ordinary,
        'maximum_initial_threshold_power_of_ten': max(
            row['threshold_power_of_ten'] for row in pairs+ordinary),
        'conclusion': 'Every listed initial source holds for all h=n-8 at least 10 to the displayed common power; all constants are numerical.',
    }


if __name__ == '__main__':
    result = report()
    DATA.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({
        'output': str(DATA),
        'baseline_pair_edge_count': result['baseline_pair_edge_count'],
        'ordinary_source_count': result['ordinary_source_count'],
        'maximum_initial_threshold_power_of_ten': result['maximum_initial_threshold_power_of_ten'],
        'thresholds': [[row['id'], row['threshold_power_of_ten']]
                       for row in result['records']],
    }, indent=2))

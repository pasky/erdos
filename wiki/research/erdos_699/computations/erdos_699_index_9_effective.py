"""Check complete effective coverage for Erdős 699 at index nine.

The adjacent proof data must contain one exact rational branch tree for each
residual case of the complete 9**4 * 16 baseline enumeration. Every leaf is
an exact Farkas contradiction. Sources are reconstructed with directed
intervals; no floating LP answer is accepted by this checker.

--ranks additionally repeats the modular polynomial-rank calculations.
Those calculations were already performed when constructing the retained
polynomial catalogues. The ordinary run checks their integer metadata,
cofactor sources, and all rational coverage certificates.
"""
from collections import Counter
from fractions import Fraction
import argparse
import gzip
import json
from pathlib import Path

import erdos_699_index_9_baseline as baseline_checker
import erdos_699_nine_cofactor_clauses as source_checker
import erdos_699_nine_polynomial_cuts as polynomial_checker
from erdos_699_rational_farkas import verify_infeasibility_certificate

ROOT = Path(__file__).parent
DATA = Path(__file__).with_suffix('.json.gz')
PRIMES = (2, 3, 5, 7)
SLACK = Fraction(1, 10**6)


def ordinary_sources():
    result = {}
    for filename in ('erdos_699_ap_cofactors.json',
                     'erdos_699_additional_product_cofactors.json'):
        data = json.loads((ROOT / filename).read_text())
        for key in ('choices', 'four_factor_choices'):
            for index, row in enumerate(data[key]):
                targets = {int(p): Fraction(v) for p, v in row['targets'].items()}
                if not set(targets) <= set(PRIMES):
                    continue
                if key == 'choices':
                    hypothesis = {'kind': 'ap', 'middle': row['middle_prime'],
                                  'endpoints': list(map(int, row['endpoint_powers']))}
                else:
                    hypothesis = {'kind': 'four', 'groups': row['equal_position_sums']}
                identifier = f'{filename}:{key}:{index}'
                result[identifier] = {'id': identifier, 'hypothesis': hypothesis,
                                      'targets': targets}
    return result


def polynomial_degree(record):
    return record['degree'] if 'degree' in record else record['certificate_degree']


def base_rows(case, polynomials):
    positions = case['positions']
    counts = Counter(positions)
    rows = []
    for record in polynomials:
        multiplicities = record['row_multiplicities']
        coefficients = tuple(Fraction(multiplicities[t]) if counts[t] == 1
                             else Fraction(0) for t in positions)
        rhs = (polynomial_degree(record)
               - sum(multiplicities[t] for t in range(9) if t not in counts))
        rows.append((coefficients, Fraction(rhs) + SLACK))
    for k, lower in enumerate(case['vector_scaled']):
        coefficients = [Fraction(0)] * 4
        coefficients[k] = -1
        rows.append((tuple(coefficients), -Fraction(lower, 10000)))
        coefficients = [Fraction(0)] * 4
        coefficients[k] = 1
        rows.append((tuple(coefficients), Fraction(1)))
    for position, count in sorted(counts.items()):
        if count > 1:
            rows.append((tuple(Fraction(-1) if t == position else Fraction(0)
                               for t in positions), Fraction(1-count)))
    return rows


def branch_rows(identifier, mask, sources, ordinary):
    if identifier in ordinary:
        prime, target = sorted(ordinary[identifier]['targets'].items())[mask]
        coefficients = [Fraction(0)] * 4
        coefficients[PRIMES.index(prime)] = -1
        return [(tuple(coefficients), -target)]
    certificate = sources[identifier]['certificate']
    intercepts = {int(p): Fraction(value)
                  for p, value in certificate['positive_part_intercepts'].items()}
    weights = {p: m for p, exponent, m, side in certificate['components']}
    rows = []
    coefficients = [Fraction(0)] * 4
    rhs = -Fraction(certificate['positive_part_threshold'])
    for bit, prime in enumerate(sorted(intercepts)):
        k = PRIMES.index(prime)
        sign = [Fraction(0)] * 4
        if mask >> bit & 1:
            sign[k] = -weights[prime]
            bound = intercepts[prime]
            coefficients[k] = -weights[prime]
            rhs += intercepts[prime]
        else:
            sign[k] = weights[prime]
            bound = -intercepts[prime]
        rows.append((tuple(sign), bound))
    rows.append((tuple(coefficients), rhs))
    return rows


def verify_tree(proof, case, polynomials, sources, ordinary):
    selected = [polynomials[name] for name in proof['polynomial_ids']]
    assert len({p['name'] for p in selected}) == len(selected)
    base = base_rows(case, selected)
    nodes = proof['tree']
    assert nodes and proof['node_count'] == len(nodes)
    stack = [(0, [])]
    visited = set()
    leaves = 0
    while stack:
        index, region = stack.pop()
        assert 0 <= index < len(nodes) and index not in visited
        visited.add(index)
        node = nodes[index]
        if 'farkas' in node:
            assert set(node) == {'farkas'}
            assert verify_infeasibility_certificate(base + region, node['farkas'])
            leaves += 1
            continue
        assert set(node) == {'source', 'masks', 'children'}
        identifier = node['source']
        record = ordinary.get(identifier, sources.get(identifier))
        assert record is not None and source_checker.applicable(record, case['positions'])
        if identifier in ordinary:
            masks = list(range(len(record['targets'])))
        else:
            masks = list(range(1, 1 << len(record['certificate']['components'])))
        assert node['masks'] == masks and len(node['children']) == len(masks)
        for mask, child in zip(masks, node['children']):
            stack.append((child, region + branch_rows(identifier, mask, sources, ordinary)))
    assert visited == set(range(len(nodes)))
    return leaves


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ranks', action='store_true')
    args = parser.parse_args()
    with gzip.open(DATA, 'rt') as handle:
        proof = json.load(handle)
    baseline = json.loads((ROOT / 'erdos_699_index_9_baseline.json').read_text())
    extra = json.loads((ROOT / 'erdos_699_nine_polynomial_cuts.json').read_text())
    with gzip.open(ROOT / 'erdos_699_nine_cofactor_clauses.json.gz', 'rt') as handle:
        source_data = json.load(handle)
    assert proof['index'] == baseline['index'] == extra['index'] == source_data['index'] == 9
    baseline_checker.verify_certificates(baseline['certificates'], ranks=args.ranks)
    baseline_checker.verify_coverage(baseline)
    polynomials = {r['name']: r for r in baseline['certificates'] + extra['certificates']}
    assert len(polynomials) == len(baseline['certificates']) + len(extra['certificates'])
    used_polynomials = {name for row in proof['roots'] for name in row['polynomial_ids']}
    needed_extra = [row for row in extra['certificates'] if row['name'] in used_polynomials]
    for row in extra['certificates']:
        if row['name'] in used_polynomials:
            polynomial_checker.verify(row, check_rank=args.ranks)
    sources = {row['id']: row for row in source_data['records']}
    ordinary = ordinary_sources()
    used_sources = {node['source'] for row in proof['roots'] for node in row['tree']
                    if 'source' in node}
    for identifier in sorted(used_sources - set(ordinary)):
        source_checker.verify(sources[identifier])
    assert proof['directed_rational_source_count'] == len(used_sources - set(ordinary))
    assert proof['ordinary_source_count'] == len(used_sources & set(ordinary))
    assert proof['baseline_polynomial_count'] == len(baseline['certificates'])
    assert proof['additional_polynomials_used'] == len(needed_extra)
    needed_polynomials = baseline['certificates'] + needed_extra
    assert proof['largest_used_jet_matrix_row_count'] == max(
        row['symmetric_jet_count'] for row in needed_polynomials)
    height_power = 0
    for row in needed_polynomials:
        normalized = dict(row)
        normalized.setdefault('row_factor_exponents', [0]*9)
        normalized.setdefault('diagonal_power', 0)
        bound = polynomial_checker.constant_power(normalized)*10**6 + 1
        if normalized.get('nonvanishing_method') == 'coprime_kernel':
            bound = max(bound, polynomial_checker.basepoint_bound(normalized) + 1)
        height_power = max(height_power, bound)
    assert proof['polynomial_height_threshold_power_of_ten'] == height_power
    assert all(value is None or Fraction(value, 10000) > SLACK
               for value in baseline['certificate_first_use_min_gains_scaled'])
    assert sorted(row['root_index'] for row in proof['roots']) == list(range(baseline['residual_count']))
    leaves = 0
    for row in proof['roots']:
        assert row['status'] == 'covered'
        case = baseline['residual_cases'][row['root_index']]
        leaves += verify_tree(row, case, polynomials, sources, ordinary)
    assert proof['covered_root_cases'] == baseline['case_count'] == 104976
    assert proof['residual_root_cases'] == baseline['residual_count'] == 917
    assert proof['farkas_leaf_count'] == leaves
    assert proof['branch_tree_node_count'] == sum(row['node_count'] for row in proof['roots'])
    print(json.dumps({'index': 9, 'root_cases': baseline['case_count'],
                      'residual_roots': baseline['residual_count'],
                      'farkas_leaves': leaves, 'ranks_recomputed': args.ranks,
                      'conclusion': 'Every bad triple at index nine lies below an effectively computable row bound.'}, indent=2))


if __name__ == '__main__':
    main()

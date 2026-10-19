"""Exact index-nine forest with weaker initial endpoints and numerical polynomial rows.

All initial positive pair endpoints are lowered by 1/10000. Polynomial rows
use their retained Newton coefficient constants E/K, and each joint source
uses its specified half-budget weakening while leaving sign rows unchanged.
The analytic source inequalities remain explicit hypotheses: their numerical
starting heights are checked by separate source calculations. No ranks are
recomputed here.
"""
from fractions import Fraction
from pathlib import Path
import gzip
import json

import erdos_699_index_9_effective as original
import erdos_699_index_9_relaxed_baseline as relaxed_baseline
import erdos_699_index_9_nonvanishing as arithmetic_nonvanishing
from erdos_699_rational_farkas import verify_infeasibility_certificate

ROOT = Path(__file__).parent
DATA = Path(__file__).with_suffix('.json.gz')


def base_rows(case, ids, polynomials, constants, K):
    rows = original.base_rows(case, [polynomials[name] for name in ids])
    return [(a, b-original.SLACK+Fraction(constants[ids[k]], K))
            if k < len(ids) else (a, b)
            for k, (a, b) in enumerate(rows)]


def branch_rows(identifier, mask, sources, ordinary, budgets):
    rows = original.branch_rows(identifier, mask, sources, ordinary)
    if identifier not in ordinary:
        a, b = rows[-1]
        rows[-1] = (a, b+Fraction(budgets[identifier]))
    return rows


def verify_root(root, case, polynomials, sources, ordinary, constants, budgets, K,
                actual_height=None):
    # Stored certificates may use a larger E/K row allowance. Their exact
    # multipliers also give the sharper weighted height threshold below.
    actual_height = K if actual_height is None else actual_height
    ids = root['polynomial_ids']
    assert len(ids) == len(set(ids)) and set(ids) <= set(constants)
    base = base_rows(case, ids, polynomials, constants, K)
    nodes = root['tree']
    assert root['node_count'] == len(nodes) and nodes
    stack = [(0, [])]
    visited = set()
    leaves = 0
    maximum = Fraction(0)
    while stack:
        index, region = stack.pop()
        assert type(index) is int and 0 <= index < len(nodes) and index not in visited
        visited.add(index)
        node = nodes[index]
        if 'farkas' in node:
            assert set(node) == {'farkas'}
            certificate = node['farkas']
            assert verify_infeasibility_certificate(base+region, certificate)
            weighted_height = sum((Fraction(weight)*constants[ids[i]]
                                   for i, weight in zip(certificate['support'],
                                                        certificate['multipliers'])
                                   if i < len(ids)), Fraction(0))
            alpha = -Fraction(certificate['weighted_rhs'])+weighted_height/K
            assert alpha > 0
            assert -alpha+weighted_height/actual_height < 0
            maximum = max(maximum, weighted_height/alpha)
            leaves += 1
            continue
        assert set(node) == {'source', 'masks', 'children'}
        identifier = node['source']
        record = ordinary.get(identifier, sources.get(identifier))
        assert record is not None and original.source_checker.applicable(record, case['positions'])
        if identifier in ordinary:
            masks = list(range(len(record['targets'])))
        else:
            assert identifier in budgets
            threshold = Fraction(record['certificate']['positive_part_threshold'])
            assert 0 < Fraction(budgets[identifier]) < threshold
            masks = list(range(1, 1 << len(record['certificate']['components'])))
        assert node['masks'] == masks and len(node['children']) == len(masks)
        for mask, child in zip(masks, node['children']):
            stack.append((child, region+branch_rows(identifier, mask, sources, ordinary, budgets)))
    assert visited == set(range(len(nodes)))
    return leaves, maximum


def main():
    with gzip.open(DATA, 'rt') as stream:
        proof = json.load(stream)
    baseline = relaxed_baseline.certify()
    old = json.loads((ROOT/'erdos_699_index_9_baseline.json').read_text())
    extra = json.loads((ROOT/'erdos_699_nine_polynomial_cuts.json').read_text())
    bounds = json.loads((ROOT/'erdos_699_nine_newton_farkas_bound.json').read_text())
    weakening = json.loads((ROOT/'erdos_699_nine_newton_source_weakening.json').read_text())
    with gzip.open(ROOT/'erdos_699_nine_cofactor_clauses.json.gz', 'rt') as stream:
        sources = {r['id']: r for r in json.load(stream)['records']}
    ordinary = original.ordinary_sources()
    polynomials = {r['name']: r for r in old['certificates']+extra['certificates']}
    newton = {r['name']: r for r in bounds['polynomial_bounds']}
    constants = proof['polynomial_constants']
    budgets = proof['source_threshold_weakenings']
    K = proof['height_power_of_ten']
    certificate_K = proof.get('certificate_rows_height_power_of_ten', K)
    assert type(K) is int and K > 0 and proof['index'] == 9
    assert type(certificate_K) is int and certificate_K > 0
    nonvanishing_records = arithmetic_nonvanishing.verify()
    arithmetic_names = {row['name'] for row in nonvanishing_records
                        if row['common_integer_zeros_outside_support'] is False}
    assert arithmetic_names == {'round3_000', 'round3_001'}
    assert proof['arithmetic_nonvanishing_polynomials'] == sorted(arithmetic_names)
    assert Fraction(proof['initial_pair_endpoint_weakening']) == Fraction(1, 10000)
    assert set(constants) == set(baseline['polynomial_names'])
    common_zero_power = 0
    for name, E in constants.items():
        assert type(E) is int and E >= newton[name]['constant_power']
        bound = 0 if name in arithmetic_names else newton[name]['basepoint_power']
        assert K > bound
        common_zero_power = max(common_zero_power, bound)
    assert proof['retained_common_zero_power'] == common_zero_power
    assert K > Fraction(baseline['maximum_coefficient_ratio'])
    assert {sid: Fraction(value) for sid, value in budgets.items()} == {
        sid: Fraction(value) for sid, value in weakening['per_source_half_budget'].items()}
    assert sorted(row['root_index'] for row in proof['roots']) == list(range(baseline['residual_count']))
    leaves = 0
    maximum = Fraction(0)
    used_sources = set()
    for row in proof['roots']:
        assert row['status'] == 'covered'
        count, cap = verify_root(row, baseline['residual_cases'][row['root_index']],
                                 polynomials, sources, ordinary, constants, budgets,
                                 certificate_K, actual_height=K)
        leaves += count
        maximum = max(maximum, cap)
        used_sources.update(node['source'] for node in row['tree'] if 'source' in node)
    assert maximum == Fraction(proof['maximum_weighted_leaf_cap']) and K > maximum
    assert proof['root_case_count'] == baseline['case_count'] == 104976
    assert proof['baseline_covered_count'] == baseline['covered_count'] == 104148
    assert proof['residual_count'] == baseline['residual_count'] == 828
    assert proof['farkas_leaf_count'] == leaves
    assert proof['node_count'] == sum(r['node_count'] for r in proof['roots'])
    assert proof['joint_source_count'] == len(used_sources-set(ordinary))
    assert proof['ordinary_source_count'] == len(used_sources & set(ordinary))
    print(json.dumps({'index': 9, 'initial_pair_endpoint_weakening': '1/10000',
                      'root_cases': 104976, 'residual_roots': 828,
                      'exact_farkas_leaves': leaves, 'height_power_of_ten': K,
                      'certificate_rows_height_power_of_ten': certificate_K,
                      'remaining_common_zero_power': common_zero_power,
                      'maximum_weighted_leaf_cap': str(maximum),
                      'ranks_recomputed': False,
                      'scope': 'Conditional on the stated weakened analytic inequalities.'}, indent=2))


if __name__ == '__main__':
    main()

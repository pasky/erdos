"""Exact simultaneous weakening budgets for the 790 index-9 joint sources.

Only the combined positive-part row is weakened: R becomes R-eta. Its sign
rows retain the original intercepts. At each leaf remove the old polynomial
slack, giving margin alpha; at most half of alpha is spent on all analytic
weakenings together. The remaining margin gives a new weighted algebraic
height threshold. No rank or analytic interval calculations are repeated.
"""
from fractions import Fraction
import gzip
import json
from pathlib import Path

import erdos_699_index_9_effective as proof_checker
import erdos_699_nine_polynomial_cuts as polynomial_checker
import erdos_699_nine_weighted_farkas_bound as weighted_checker

ROOT = Path(__file__).parent


def main():
    weighted = weighted_checker.main_bound()
    proof = json.load(gzip.open(proof_checker.DATA, 'rt'))
    baseline = json.loads((ROOT/'erdos_699_index_9_baseline.json').read_text())
    extra = json.loads((ROOT/'erdos_699_nine_polynomial_cuts.json').read_text())
    source_data = json.load(gzip.open(ROOT/'erdos_699_nine_cofactor_clauses.json.gz', 'rt'))
    sources = {row['id']: row for row in source_data['records']}
    ordinary = proof_checker.ordinary_sources()
    polynomials = {row['name']: row for row in baseline['certificates'] + extra['certificates']}
    constants = {}
    for name, row in polynomials.items():
        normalized = dict(row)
        normalized.setdefault('row_factor_exponents', [0]*9)
        normalized.setdefault('diagonal_power', 0)
        constants[name] = polynomial_checker.constant_power(normalized)
    used = {node['source'] for root in proof['roots'] for node in root['tree']
            if 'source' in node} - set(ordinary)
    budgets = {name: Fraction(sources[name]['certificate']['positive_part_threshold'])/2
               for name in used}
    records = []
    uniform = None
    for root in proof['roots']:
        ids = root['polynomial_ids']
        case = baseline['residual_cases'][root['root_index']]
        base = proof_checker.base_rows(case, [polynomials[name] for name in ids])
        stack = [(0, [], [])]
        while stack:
            node_index, region, tags = stack.pop()
            node = root['tree'][node_index]
            if 'farkas' not in node:
                name = node['source']
                for mask, child in zip(node['masks'], node['children']):
                    added = proof_checker.branch_rows(name, mask, sources, ordinary)
                    annotation = ([None]*len(added) if name in ordinary
                                  else [None]*(len(added)-1) + [name])
                    stack.append((child, region+added, tags+annotation))
                continue
            certificate = node['farkas']
            assert proof_checker.verify_infeasibility_certificate(base+region, certificate)
            alpha = -Fraction(certificate['weighted_rhs'])
            height_constant = Fraction(0)
            source_weights = {}
            for index, weight in zip(certificate['support'], certificate['multipliers']):
                weight = Fraction(weight)
                if index < len(ids):
                    alpha += proof_checker.SLACK*weight
                    height_constant += constants[ids[index]]*weight
                elif index >= len(base):
                    name = tags[index-len(base)]
                    if name is not None:
                        source_weights[name] = source_weights.get(name, Fraction(0))+weight
            assert alpha > 0
            if source_weights:
                candidate = alpha/(2*sum(source_weights.values()))
                uniform = candidate if uniform is None else min(uniform, candidate)
                count = len(source_weights)
                for name, weight in source_weights.items():
                    budgets[name] = min(budgets[name], alpha/(2*count*weight))
            records.append({'root_index': root['root_index'], 'node_index': node_index,
                            'alpha': alpha, 'height_constant': height_constant,
                            'source_weights': source_weights})
    assert len(records) == proof['farkas_leaf_count']
    uniform = min(uniform, *(Fraction(sources[name]['certificate']['positive_part_threshold'])/2
                             for name in used))
    maximum = Fraction(0)
    limiting_leaf = None
    for record in records:
        cost = sum((weight*budgets[name] for name, weight in record['source_weights'].items()),
                   Fraction(0))
        assert cost <= record['alpha']/2
        remaining = record['alpha']-cost
        cap = record['height_constant']/remaining
        if cap > maximum:
            maximum = cap
            limiting_leaf = {
                'root_index': record['root_index'], 'node_index': record['node_index'],
                'original_margin_without_polynomial_slack': str(record['alpha']),
                'analytic_weakening_cost': str(cost),
                'remaining_margin': str(remaining),
                'weighted_height_constant': str(record['height_constant']),
                'weighted_cap': str(cap),
                'source_weights': {name: str(weight) for name, weight in record['source_weights'].items()},
            }
    overall = max(maximum, Fraction(weighted['baseline_max']['cap']),
                  Fraction(weighted['basepoint_max']['cap']))
    result = {
        'index': 9, 'height_variable': 'h=n-8',
        'meaning': 'All listed threshold weakenings may be applied simultaneously, keeping every original sign row unchanged.',
        'source_count': len(budgets), 'leaf_count': len(records),
        'uniform_half_budget': str(uniform),
        'per_source_half_budget': {name: str(value) for name, value in sorted(budgets.items())},
        'modified_thresholds': {name: str(Fraction(sources[name]['certificate']['positive_part_threshold'])-value)
                                for name, value in sorted(budgets.items())},
        'maximum_weakening_ratio': str(max(value/Fraction(sources[name]['certificate']['positive_part_threshold'])
                                          for name, value in budgets.items())),
        'limiting_weighted_leaf': limiting_leaf,
        'baseline_max': weighted['baseline_max'], 'basepoint_max': weighted['basepoint_max'],
        'overall_exact_cap': str(overall),
        'polynomial_height_threshold_power_of_ten': overall.numerator//overall.denominator+1,
        'source_threshold_scope': 'The modified analytic source thresholds must be proved separately.',
        'input_files': weighted['input_files'], 'ranks_recomputed': False,
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in ('source_count', 'leaf_count', 'uniform_half_budget',
                     'limiting_weighted_leaf', 'overall_exact_cap', 'polynomial_height_threshold_power_of_ten')}, indent=2))


if __name__ == '__main__':
    main()

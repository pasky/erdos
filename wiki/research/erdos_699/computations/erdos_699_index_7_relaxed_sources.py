"""Exact index-seven coverage with numerically friendlier source margins.

The verified polynomial family and source directions remain unchanged.
Only rational clause thresholds and the five initial pair endpoints are
weakened. Every leaf is checked with exact Farkas arithmetic.
"""

import argparse
from fractions import Fraction as F
from itertools import permutations
import json
from pathlib import Path

import erdos_699_index_7_effective as original
from erdos_699_rational_farkas import verify_infeasibility_certificate

HERE = Path(__file__).parent
DATA = Path(__file__).with_suffix('.json')


def certify(data):
    input_path = HERE/data['input_file']
    bounds_path = HERE/data['polynomial_bounds_file']
    proof = json.loads(input_path.read_text())
    bounds = json.loads(bounds_path.read_text())
    assert bounds['input_file'] == data['input_file']
    polynomials = proof['polynomials']
    E = [r['coefficient_power_of_ten'] for r in bounds['polynomial_bounds']]
    assert [p['name'] for p in polynomials] == [r['name'] for r in bounds['polynomial_bounds']]
    sources = {r['id']: r for r in proof['sources']}
    eta = {key: F(value) for key, value in data['source_eta'].items()}
    assert set(eta) == set(sources)
    baseline = F(data['baseline_weakening'])
    assert baseline == F(1,10000)
    assert all(0 < eta[key] < F(source['certificate']['positive_part_threshold'])
               for key, source in sources.items())
    old_vectors = original.minimal_vectors(proof['pair_edges_scaled'])
    assert [list(v) for v in old_vectors] == proof['minimal_vectors_scaled']
    relaxed_edges = [(p,q,a-1,b-1) for p,q,a,b in proof['pair_edges_scaled']]
    relaxed_vectors = original.minimal_vectors(relaxed_edges)
    assert set(relaxed_vectors) == {tuple(max(0,a-1) for a in v) for v in old_vectors}
    expected = {(p,v) for p in permutations(range(7),3) if 0 in p for v in old_vectors}
    seen = set()
    evaluation_cap = data['evaluation_height_power_of_ten']
    assert evaluation_cap == 100000000
    counts = {'roots':0, 'nodes':0, 'branches':0, 'leaves':0}
    worst = (F(0), None)
    used_sources = set()
    for root_number, root in enumerate(data['forest']):
        positions, vector = tuple(root['positions']), tuple(root['vector'])
        key = positions, vector
        assert key in expected and key not in seen
        seen.add(key)
        counts['roots'] += 1
        base = []
        for polynomial, bound in zip(polynomials,E):
            m = polynomial['row_multiplicities']
            rhs = original.total_degree(polynomial)-sum(m[t] for t in range(7) if t not in positions)
            base.append((tuple(F(m[t]) for t in positions), rhs+F(bound,evaluation_cap)))
        for k, value in enumerate(vector):
            lo, hi = [F(0)]*3, [F(0)]*3
            lo[k], hi[k] = -1, 1
            base.extend([(tuple(lo), -max(F(0),F(value,10000)-baseline)),
                         (tuple(hi), F(1))])
        stack = [('', root['tree'], [])]
        while stack:
            path, node, region = stack.pop()
            counts['nodes'] += 1
            if 'farkas' in node:
                assert set(node) == {'farkas'}
                certificate = node['farkas']
                assert verify_infeasibility_certificate(base+region, certificate)
                constant = F(sum(F(weight)*E[k] for k,weight in zip(
                    certificate['support'],certificate['multipliers']) if k<len(E)))
                alpha = -F(certificate['weighted_rhs'])+constant/evaluation_cap
                assert alpha > 0
                ratio = constant/alpha
                if ratio > worst[0]:
                    worst = (ratio, {'root':root_number, 'path':path,
                                     'margin_without_polynomial_error':str(alpha),
                                     'weighted_coefficient_power':str(constant)})
                counts['leaves'] += 1
                continue
            assert set(node) == {'source','children'}
            source = sources[node['source']]
            assert original.source_active(source, positions)
            used_sources.add(node['source'])
            members = sum(bool(w) for w in original.source_weights(source)[1])
            masks = set(range(1,1<<members))
            assert set(node['children']) == set(map(str,masks))
            for mask in masks:
                added = original.source_branch_rows(source,mask)
                coefficients, rhs = added[-1]
                added[-1] = coefficients, rhs+eta[node['source']]
                stack.append((path+'/'+str(mask),node['children'][str(mask)],region+added))
            counts['branches'] += 1
    assert seen == expected and len(seen) == 540
    assert used_sources == set(sources)
    weighted_cap = worst[0].numerator//worst[0].denominator+1
    algebraic_cap = max(weighted_cap,bounds['collision_power_of_ten'],
                        bounds['maximum_common_zero_power_of_ten'],10)
    assert algebraic_cap <= evaluation_cap
    return {
        'index':7, 'height_variable':'h=n-6', 'coverage':counts,
        'baseline_edges_scaled':relaxed_edges,
        'used_joint_sources':len(used_sources),
        'source_weakenings':{key:str(value) for key,value in sorted(eta.items())
                             if value != F(1,10000)},
        'usual_source_weakening':'1/10000',
        'maximum_weighted_ratio':str(worst[0]), 'worst_leaf':worst[1],
        'weighted_polynomial_power_of_ten':weighted_cap,
        'algebraic_height_power_of_ten':algebraic_cap,
        'source_threshold_scope':'Numerical analytic thresholds must be supplied separately.',
        'conclusion':'The weakened pair and joint-source inequalities exclude every bad index-seven triple above the displayed polynomial height.',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write',action='store_true')
    args = parser.parse_args()
    data = json.loads(DATA.read_text())
    result = certify(data)
    if args.write:
        data['certificate'] = result
        DATA.write_text(json.dumps(data,indent=2)+'\n')
    else:
        assert data['certificate'] == result
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()

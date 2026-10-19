#!/usr/bin/env python3
"""Exact index-nine baseline coverage with pair endpoints lowered by 10^-4.

Use all 128 polynomial certificates already required by the effective proof.
Select the best coefficient-bound/gain ratio in each covered case. Remaining
cases require separate exact branch trees. No modular ranks are recomputed.
"""
import argparse
from fractions import Fraction
from hashlib import sha256
from itertools import product
import gzip
import json
from pathlib import Path

import numpy as np

import erdos_699_index_9_effective as original
from erdos_699_index_10_effective import minimal_vectors

HERE = Path(__file__).parent
DATA = Path(__file__).with_suffix('.json')


def certify():
    paths = [HERE/name for name in (
        'erdos_699_index_9_baseline.json', 'erdos_699_nine_polynomial_cuts.json',
        'erdos_699_index_9_effective.json.gz', 'erdos_699_nine_newton_farkas_bound.json')]
    baseline = json.loads(paths[0].read_text())
    extra = json.loads(paths[1].read_text())
    with gzip.open(paths[2], 'rt') as stream:
        proof = json.load(stream)
    bound_data = json.loads(paths[3].read_text())
    by_name = {r['name']: r for r in bound_data['polynomial_bounds']}
    used = {name for root in proof['roots'] for name in root['polynomial_ids']}
    used.update(p['name'] for p in baseline['certificates'])
    polynomials = [p for p in baseline['certificates']+extra['certificates']
                   if p['name'] in used]
    assert len(polynomials) == 128 and len(used) == 128
    constants = np.array([by_name[p['name']]['constant_power'] for p in polynomials],
                         dtype=np.int64)
    multiplicities = np.array([p['row_multiplicities'] for p in polynomials],
                              dtype=np.int64).T
    degrees = 10000*np.array([original.polynomial_degree(p) for p in polynomials],
                             dtype=np.int64)
    edges = [(p, q, a-1, b-1) for p, q, a, b in baseline['pair_edges_scaled']]
    assert all(min(a,b) > 0 for p,q,a,b in edges)
    vectors = minimal_vectors(edges)
    assert len(vectors) == 16
    assert set(vectors) == {tuple(max(0,x-1) for x in v)
                            for v in baseline['minimal_vectors_scaled']}
    capacities, cases = [], []
    for positions in product(range(9), repeat=4):
        for vector in vectors:
            alpha = [10000]*9
            for t in set(positions):
                members = [k for k,x in enumerate(positions) if x == t]
                alpha[t] = vector[members[0]] if len(members) == 1 else 0
            capacities.append(alpha)
            cases.append((positions, tuple(vector)))
    gains = np.array(capacities, dtype=np.int64) @ multiplicities-degrees
    assert len(cases) == 104976
    assert int(np.max(constants))*int(np.max(np.abs(gains))) < 2**63
    best = np.zeros(len(cases), dtype=np.int64)
    selected_gain = np.zeros(len(cases), dtype=np.int64)
    selected_constant = np.ones(len(cases), dtype=np.int64)
    # Compare rational gains/constants by exact integer cross multiplication.
    for k, constant in enumerate(constants):
        improve = gains[:,k]*selected_constant > selected_gain*constant
        best[improve] = k
        selected_gain[improve] = gains[improve,k]
        selected_constant[improve] = constant
    old_lookup = {(tuple(c['positions']), tuple(c['vector_scaled'])): k
                  for k,c in enumerate(baseline['residual_cases'])}
    old_vectors = set(map(tuple, baseline['minimal_vectors_scaled']))
    residual, counts, minimum = [], [0]*len(polynomials), [None]*len(polynomials)
    digest = sha256()
    for number, (positions, vector) in enumerate(cases):
        gain, k = int(selected_gain[number]), int(best[number])
        if gain > 0:
            counts[k] += 1
            minimum[k] = gain if minimum[k] is None else min(minimum[k], gain)
            digest.update(f'{positions}:{vector}:{k}:{gain}\n'.encode())
        else:
            old_vector = tuple(x+1 if x else 0 for x in vector)
            assert old_vector in old_vectors
            residual.append({'positions': list(positions), 'vector_scaled': list(vector),
                             'alpha_scaled': capacities[number],
                             'collision': len(set(positions)) < 4,
                             'old_root_index': old_lookup.get((positions, old_vector))})
    ratios = [(Fraction(10000*int(constants[k]), gain), k)
              for k,gain in enumerate(minimum) if gain is not None]
    largest, limiting = max(ratios)
    assert sum(counts)+len(residual) == len(cases)
    return {'index': 9, 'pair_weakening': '1/10000', 'pair_edges_scaled': edges,
            'minimal_vectors_scaled': vectors, 'case_count': len(cases),
            'covered_count': sum(counts), 'residual_count': len(residual),
            'residual_cases': residual,
            'new_roots': [c for c in residual if c['old_root_index'] is None],
            'polynomial_names': [p['name'] for p in polynomials],
            'coefficient_powers_of_ten': constants.tolist(),
            'selected_counts': counts, 'minimum_selected_gains_scaled': minimum,
            'coverage_sha256': digest.hexdigest(),
            'maximum_coefficient_ratio': str(largest),
            'coefficient_height_power_of_ten': largest.numerator//largest.denominator+1,
            'limiting_polynomial': polynomials[limiting]['name'],
            'input_files': [p.name for p in paths],
            'scope': 'Conditional polynomial coverage using the stated weakened pair inequalities. Analytic source thresholds, common-zero bounds or arithmetic nonvanishing, and the residual branch trees must be supplied separately.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    result = certify()
    if args.write:
        DATA.write_text(json.dumps(result, indent=2)+'\n')
    else:
        # JSON converts tuples to lists.
        assert json.loads(DATA.read_text()) == json.loads(json.dumps(result))
    keys = ('index','case_count','covered_count','residual_count','new_roots',
            'maximum_coefficient_ratio','coefficient_height_power_of_ten',
            'limiting_polynomial','coverage_sha256')
    print(json.dumps({key: result[key] for key in keys}, indent=2))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Exact polynomial coverage of the full index-9 position/witness space.

Default: also recompute every modular full-row-rank certificate.
--arithmetic-only: verify the sources, integer data and complete coverage.
The residual cases are cofactor/position configurations, not binomial triples.
"""
from __future__ import annotations

import argparse
import hashlib
from itertools import product
import json
from pathlib import Path

import numpy as np
import erdos_699_index_13_interpolation_gcd as interpolation
from erdos_699_index_10_effective import minimal_vectors
from erdos_699_weighted_ramps import EDGES
from erdos_699_bft_more_pairs import NEW_EDGES

HERE = Path(__file__).resolve().parent
DATA = HERE / 'erdos_699_index_9_baseline.json'


def source_edges():
    edges = [(p, q, e, e) for p, q, e in EDGES + NEW_EDGES if p < 9 and q < 9]
    source = json.loads((HERE / 'erdos_699_bft_asymmetric_pair_table.json').read_text())
    for key in ('published_gcd_pairs', 'effective_gcd_pairs'):
        for row in source[key]:
            p, q = row['pair']
            if p < 9 and q < 9:
                assert row['verified']
                edges.append((p, q, *row['endpoints_scaled']))
    return edges


def verify_certificates(records, ranks):
    names = set()
    for record in records:
        assert record['name'] not in names
        names.add(record['name'])
        h, m = record['line_exponents'], record['row_multiplicities']
        assert len(h) == len(m) == 9
        assert all(type(x) is int and x >= 0 for x in h + m)
        d = record['interpolation_degree']
        assert type(d) is int and d >= -1
        assert record['degree'] == 2 * sum(h) + max(0, d + 1)
        assert record['modular_prime'] == 251
        interpolation.LINE_EXPONENTS = h
        interpolation.ROW_MULTIPLICITIES = m
        interpolation.DEGREE = d
        interpolation.PRIME = 251
        jets = interpolation.symmetric_jets()
        basis = interpolation.symmetric_basis() if jets else []
        assert len(jets) == record['symmetric_jet_count'] == record['rank']
        assert len(basis) == record['symmetric_monomial_count']
        assert len(jets) <= len(basis)
        if jets:
            assert d >= 0
            if ranks:
                print(f"Rank {record['name']}: {len(jets)} x {len(basis)}", flush=True)
                assert interpolation.jet_matrix(basis, jets).rank() == len(jets)
        else:
            assert d == -1


def verify_coverage(data):
    edges = source_edges()
    assert [list(e) for e in edges] == data['pair_edges_scaled']
    vectors = minimal_vectors(edges)
    assert [list(v) for v in vectors] == data['minimal_vectors_scaled']
    assert len(vectors) == 16
    records = data['certificates']
    multiplicities = np.array([r['row_multiplicities'] for r in records], dtype=np.int64).T
    degrees = 10000 * np.array([r['degree'] for r in records], dtype=np.int64)
    # These bounds also justify signed int64 arithmetic below.
    assert np.max(multiplicities) < 10000 and np.max(degrees) < 10**9
    residual = []
    count = 0
    uses = np.zeros(len(records), dtype=np.int64)
    minima = np.full(len(records), 2**62, dtype=np.int64)
    digest = hashlib.sha256()
    for positions in product(range(9), repeat=4):
        for vector in vectors:
            alpha = np.full(9, 10000, dtype=np.int64)
            for t in set(positions):
                members = [k for k, pos in enumerate(positions) if pos == t]
                alpha[t] = vector[members[0]] if len(members) == 1 else 0
            gains = alpha @ multiplicities - degrees
            available = np.flatnonzero(gains > 0)
            count += 1
            if len(available):
                k = int(available[0])
                uses[k] += 1
                minima[k] = min(minima[k], gains[k])
                digest.update(f'{positions}:{vector}:{k}:{int(gains[k])}\n'.encode())
            else:
                residual.append(dict(positions=list(positions), vector_scaled=list(vector),
                                     alpha_scaled=alpha.tolist(), collision=len(set(positions)) < 4))
    assert count == data['case_count'] == 104976
    assert int(uses.sum()) == data['covered_count']
    assert residual == data['residual_cases']
    assert len(residual) == data['residual_count']
    assert sum(r['collision'] for r in residual) == data['collision_residual_count']
    assert uses.tolist() == data['certificate_first_use_counts']
    assert [int(x) if x < 2**62 else None for x in minima] == data['certificate_first_use_min_gains_scaled']
    assert digest.hexdigest() == data['coverage_sha256']
    return dict(index=9, certificates=len(records), root_cases=count,
                polynomially_covered=int(uses.sum()), residual_cases=len(residual),
                residual_collision_cases=sum(r['collision'] for r in residual),
                unique_residual_capacities=len({tuple(r['alpha_scaled']) for r in residual}),
                coverage_sha256=digest.hexdigest())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--arithmetic-only', action='store_true')
    args = parser.parse_args()
    data = json.loads(DATA.read_text())
    assert (data['index'], data['primes'], data['scale']) == (9, [2, 3, 5, 7], 10000)
    verify_certificates(data['certificates'], ranks=not args.arithmetic_only)
    print(json.dumps(verify_coverage(data), indent=2))


if __name__ == '__main__':
    main()

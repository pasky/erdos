#!/usr/bin/env python3
"""Check arithmetic nonvanishing for the two critical index-nine kernels.

The proof is the local p-adic argument in the index-seven nonvanishing
note. No large jet rank calculation or binomial-row search is repeated.
Dependencies: numpy and python-flint.
"""
from __future__ import annotations

import json
from math import comb
from pathlib import Path

import numpy as np
from flint import nmod_mat, nmod_poly

DATA = Path(__file__).with_suffix('.json')
SOURCE = DATA.with_name('erdos_699_nine_polynomial_cuts.json')


def verify_record(data, source):
    p, d = source['modular_prime'], source['interpolation_degree']
    assert p == data['prime'] == 251 and d == data['degree']
    h, m = source['line_exponents'], source['row_multiplicities']
    assert h == data['line_exponents'] and m == data['row_multiplicities']
    assert not any(source.get('row_factor_exponents', []))
    assert source.get('diagonal_power', 0) == 0
    residual = lambda x, y: max(0, m[x+y]-h[x]-h[y])
    support = [(x, y) for x in range(9) for y in range(9-x) if residual(x, y)]
    basis = [(a, t-a) for t in range(d+1) for a in range(t//2+1)]
    jet_count = sum(1 for x, y in support if x <= y
                    for order in range(residual(x, y))
                    for a in range(order+1) if x != y or a <= order-a)
    assert [jet_count, len(basis)] == data['matrix_shape']
    assert source['symmetric_rank'] == source['symmetric_jet_count'] == jet_count
    assert source['symmetric_monomial_count'] == len(basis)
    columns = data['kernel_basis']
    assert columns[:2] == source['kernel_vectors']
    assert len(columns) == len(basis)-jet_count == data['nullity']
    assert all(len(c) == len(basis) for c in columns)
    assert all(type(v) is int and 0 <= v < p for c in columns for v in c)
    small = nmod_mat(len(basis), len(columns),
                     [v for row in zip(*columns) for v in row], p)
    assert small.rank() == len(columns)

    matrices = []
    for column in columns:
        matrix = np.zeros((d+1, d+1), dtype=np.int64)
        for (a, b), value in zip(basis, column, strict=True):
            matrix[a, b] = matrix[b, a] = value
        matrices.append(matrix)
    maximum = max(residual(x, y) for x, y in support)
    powers = [np.array([
        [(comb(e, r)*pow(x, e-r, p)) % p if e >= r else 0 for e in range(d+1)]
        for r in range(maximum+2)], dtype=np.int64) for x in range(9)]
    orders = np.arange(maximum+2)
    jets = {}
    for k, matrix in enumerate(matrices):
        left = [power @ matrix % p for power in powers]
        for x, y in support:
            table = left[x] @ powers[y].T % p
            assert not np.any(table[orders[:, None]+orders[None, :] < residual(x, y)])
            if k < 2:
                jets[k, x, y] = table

    common = []
    for x in range(p):
        px = np.array([pow(x, e, p) for e in range(d+1)], dtype=np.int64)
        f, g = [nmod_poly([int(v) for v in px @ matrix % p], p)
                for matrix in matrices[:2]]
        common.extend((x, int(y)) for y, _ in f.gcd(g).roots())
    assert set(support).issubset(common)
    extra = sorted(set(common)-set(support))
    assert extra == [tuple(point) for point in data['extra_residue_points']]
    if extra:
        values = []
        assert len(matrices) >= 3
        for x, y in extra:
            px = np.array([pow(x, e, p) for e in range(d+1)], dtype=np.int64)
            py = np.array([pow(y, e, p) for e in range(d+1)], dtype=np.int64)
            value = int((px @ matrices[2] % p) @ py % p)
            assert value
            values.append(value)
        assert values == data['third_section_values']

    exceptional = {tuple(c['point']): c for c in data['exceptional_tangents']}
    for x, y in support:
        r = residual(x, y)
        cones = [[int(jets[k, x, y][u, r-u]) for u in range(r+1)] for k in range(2)]
        assert cones[0][-1] or cones[1][-1]
        f, g = [nmod_poly(cone, p) for cone in cones]
        tangent = f.gcd(g)
        if (x, y) not in exceptional:
            assert tangent.is_one()
            continue
        record = exceptional[x, y]
        assert x == y and r % 2 == 1 and r == record['multiplicity']
        assert list(map(int, tangent.coeffs())) == [1, 1]
        forms = []
        for k in range(2):
            w = sum(cones[k][u]*(r-u)*pow(-1, r-u-1, p) for u in range(r)) % p
            t = sum(int(jets[k, x, y][u, r+1-u])*pow(-1, r+1-u, p)
                    for u in range(r+2)) % p
            forms.append([t, w])
        determinant = (forms[0][0]*forms[1][1]-forms[1][0]*forms[0][1]) % p
        assert forms == record['second_linear_forms']
        assert determinant == record['determinant'] and determinant
    return {
        'name': data['name'], 'degree': d, 'support_points': len(support),
        'kernel_columns': len(columns), 'extra_residue_points': len(extra),
        'second_blowup_determinants': [c['determinant'] for c in exceptional.values()],
        'common_integer_zeros_outside_support': False,
        'large_rank_repeated': False,
    }


def verify():
    data = json.loads(DATA.read_text())
    sources = {c['name']: c for c in json.loads(SOURCE.read_text())['certificates']}
    return [verify_record(c, sources[c['name']]) for c in data['certificates']]


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2))

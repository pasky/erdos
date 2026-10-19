#!/usr/bin/env python3
"""Verify the index-seven arithmetic nonvanishing certificate.

This checks polynomial jets, all residue classes over F_251, and tangent
directions. It enumerates no binomial rows or columns and does not repeat
the 9792-row rank calculation. Dependencies: numpy and python-flint.
"""
from __future__ import annotations

import json
from math import comb
from pathlib import Path

import numpy as np
from flint import nmod_mat, nmod_poly

DATA = Path(__file__).with_suffix('.json')


def verify():
    data = json.loads(DATA.read_text())
    prime, degree = data['prime'], data['degree']
    assert (prime, degree) == (251, 196)
    h, m = data['line_exponents'], data['row_multiplicities']
    residual = lambda x, y: max(0, m[x+y]-h[x]-h[y])
    support = [(x, y) for x in range(7) for y in range(7-x)
               if residual(x, y)]
    basis = [(a, t-a) for t in range(degree+1) for a in range(t//2+1)]
    jet_count = sum(1 for x, y in support if x <= y
                    for order in range(residual(x, y))
                    for a in range(order+1) if x != y or a <= order-a)
    assert [jet_count, len(basis)] == data['matrix_shape'] == [9792, 9801]
    assert data['rank'] == jet_count and data['nullity'] == 9

    prior = json.loads(DATA.with_name('erdos_699_index_7_polynomials.json').read_text())
    prior = next(c for c in prior['certificates']
                 if c['name'] == data['certificate_name'])
    assert prior['actual_rank'] == jet_count and prior['rank_verified']
    assert prior['line_exponents'] == h and prior['row_multiplicities'] == m
    assert prior['interpolation_degree'] == degree and prior['modular_prime'] == prime

    columns = data['kernel_basis']
    assert len(columns) == 9 and columns[:2] == prior['kernel_sections']
    assert all(len(c) == len(basis) for c in columns)
    assert all(type(v) is int and 0 <= v < prime for c in columns for v in c)
    # This is only a nine-column independence check, not the large jet rank.
    small_matrix = nmod_mat(len(basis), 9,
                           [v for row in zip(*columns) for v in row], prime)
    assert small_matrix.rank() == 9

    matrices = []
    for column in columns:
        matrix = np.zeros((degree+1, degree+1), dtype=np.int64)
        for (a, b), value in zip(basis, column, strict=True):
            matrix[a, b] = matrix[b, a] = value
        matrices.append(matrix)

    maximum = max(residual(x, y) for x, y in support)
    powers = [np.array([
        [(comb(e, r)*pow(x, e-r, prime)) % prime if e >= r else 0
         for e in range(degree+1)]
        for r in range(maximum+2)], dtype=np.int64) for x in range(7)]
    jets = {}
    orders = np.arange(maximum+2)
    for k, matrix in enumerate(matrices):
        left = [power @ matrix % prime for power in powers]
        for x, y in support:
            table = left[x] @ powers[y].T % prime
            mask = orders[:, None] + orders[None, :] < residual(x, y)
            assert not np.any(table[mask])
            if k < 2:
                jets[k, x, y] = table

    assert data['selected_columns'] == [0, 1, 2]
    common = []
    for x in range(prime):
        powers_x = np.array([pow(x, e, prime) for e in range(degree+1)],
                            dtype=np.int64)
        f, g = [nmod_poly([int(v) for v in powers_x @ matrix % prime], prime)
                for matrix in matrices[:2]]
        common.extend((x, int(y)) for y, _ in f.gcd(g).roots())
    common = sorted(common)
    extra = sorted(set(common)-set(support))
    assert set(support).issubset(common)
    assert extra == [tuple(p) for p in data['off_grid_common_points_first_two']]
    third_values = []
    for x, y in extra:
        px = np.array([pow(x, e, prime) for e in range(degree+1)], dtype=np.int64)
        py = np.array([pow(y, e, prime) for e in range(degree+1)], dtype=np.int64)
        value = int((px @ matrices[2] % prime) @ py % prime)
        assert value
        third_values.append(value)
    assert third_values == data['third_section_values']

    exceptional = {tuple(c['point']): c for c in data['exceptional_tangents']}
    for x, y in support:
        r = residual(x, y)
        cones = [[int(jets[k, x, y][u, r-u]) for u in range(r+1)]
                 for k in range(2)]
        # Affine tangent coordinate U/V; check the omitted point V=0 too.
        assert cones[0][-1] or cones[1][-1]
        f, g = [nmod_poly(cone, prime) for cone in cones]
        tangent_gcd = f.gcd(g)
        if (x, y) not in exceptional:
            assert tangent_gcd.is_one()
            continue
        record = exceptional[x, y]
        assert x == y and r % 2 == 1 and r == record['multiplicity']
        assert list(map(int, tangent_gcd.coeffs())) == record['affine_tangent_gcd'] == [1, 1]
        forms = []
        for k in range(2):
            w_coefficient = sum(cones[k][u]*(r-u)*pow(-1, r-u-1, prime)
                                for u in range(r)) % prime
            t_coefficient = sum(int(jets[k, x, y][u, r+1-u])
                                * pow(-1, r+1-u, prime)
                                for u in range(r+2)) % prime
            forms.append([t_coefficient, w_coefficient])
        determinant = (forms[0][0]*forms[1][1]-forms[1][0]*forms[0][1]) % prime
        assert forms == record['second_linear_forms']
        assert determinant == record['determinant'] and determinant

    return {
        'prime': prime,
        'degree': degree,
        'support_points': len(support),
        'retained_kernel_columns': len(columns),
        'selected_columns': data['selected_columns'],
        'extra_residue_points': len(extra),
        'extra_points_excluded_by_third_section': True,
        'ordinary_tangent_checks': len(support)-len(exceptional),
        'second_blowup_determinants': [c['determinant'] for c in exceptional.values()],
        'large_rank_repeated': False,
        'conclusion': 'Three p-integral symmetric lifts have no common integer zero outside the support.',
    }


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2))

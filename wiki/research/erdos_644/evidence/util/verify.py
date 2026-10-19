#!/usr/bin/env python3
"""Exact rational certificate for the three-point composition lemma.

No external packages are used. The vertices of Q_3 are exhaustively enumerated
from all seven-active-inequality bases, and the supplied convex decompositions
are verified with fractions.Fraction. Run this file from any directory.
"""

from fractions import Fraction as F
from itertools import combinations, permutations
import json
from pathlib import Path


N = 3
M = 1 << N
weights = [I.bit_count() for I in range(M)]

# All inequalities have the form row . alpha >= 0. The first eight impose
# alpha_I >= 0. The last seven impose
# 4 |D| sum_{I disjoint D} alpha_I >= 3 sum_I |I| alpha_I.
inequalities = [[int(i == j) for j in range(M)] for i in range(M)]
inequalities += [
    [4 * D.bit_count() * int(not (D & I)) - 3 * weights[I]
     for I in range(M)]
    for D in range(1, M)
]


def solve_basis(rows):
    """Solve rows[0] . x = 1 and rows[i] . x = 0 for i > 0."""
    matrix = [[F(x) for x in row] + [F(i == 0)]
              for i, row in enumerate(rows)]
    for j in range(M):
        pivot = next((i for i in range(j, M) if matrix[i][j]), None)
        if pivot is None:
            return None
        matrix[j], matrix[pivot] = matrix[pivot], matrix[j]
        coefficient = matrix[j][j]
        matrix[j] = [x / coefficient for x in matrix[j]]
        for i in range(j + 1, M):
            if matrix[i][j]:
                coefficient = matrix[i][j]
                matrix[i] = [x - coefficient * y
                             for x, y in zip(matrix[i], matrix[j])]
    answer = [F(0)] * M
    for i in range(M - 1, -1, -1):
        answer[i] = matrix[i][-1] - sum(
            matrix[i][j] * answer[j] for j in range(i + 1, M)
        )
    return tuple(answer)


vertices = set()
for active in combinations(range(len(inequalities)), M - 1):
    vertex = solve_basis([[1] * M] + [inequalities[i] for i in active])
    if vertex is not None and all(
        sum(x * y for x, y in zip(row, vertex)) >= 0
        for row in inequalities
    ):
        vertices.add(vertex)

data = json.loads(
    (Path(__file__).resolve().parent.parent / "assets" / "couplings.json").read_text())
certified_vertices = set()
for row in data:
    alpha = tuple(map(F, row["alpha"]))
    assert len(alpha) == M
    assert all(x >= 0 for x in alpha) and sum(alpha) == 1
    combination = [F(0)] * M
    coefficient_sum = F(0)
    for coefficient_string, sets in row["coupling"]:
        coefficient = F(coefficient_string)
        assert coefficient >= 0
        assert len(sets) == 3 and all(0 <= I < M for I in sets)
        I, J, K = sets
        assert not (I & J or I & K or J & K)
        coefficient_sum += coefficient
        for state, multiplicity in zip(sets, [4, 2, 1]):
            combination[state] += coefficient * F(multiplicity, 7)
    assert coefficient_sum == 1
    assert tuple(combination) == alpha

    orbit = set()
    for permutation in permutations(range(N)):
        image = [F(0)] * M
        for I, coefficient in enumerate(alpha):
            J = sum(((I >> j) & 1) << permutation[j] for j in range(N))
            image[J] = coefficient
        orbit.add(tuple(image))
    assert len(orbit) == row["orbit_size"]
    certified_vertices.update(orbit)

assert len(data) == 16
assert len(vertices) == 52
assert vertices == certified_vertices
print("Verified exactly: 52 vertices, 16 symmetry orbits, all in the template polytope.")

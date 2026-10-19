"""Check the one labeled nine-point configuration in L30.

Recompute all 36 pair distances, 84 triple determinants, 126 circle
determinants, all 28 equality derivatives and the exact 14 by 14 minor.
Inputs: assets/configuration.json, including the complete expected matrix.
Arithmetic: Python integers and Fraction. Runtime: a few seconds or less.
Run from the repository root with uv run --no-sync python and this path.
No search, global exclusion, floating tolerance or independent review.
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path

from tools import Checker, evidence_parser


def q(a, b):
    return a * a + a * b + b * b


def determinant(matrix):
    rows = [[Fraction(value) for value in row] for row in matrix]
    value = Fraction(1)
    for column in range(len(rows)):
        pivot = next((i for i in range(column, len(rows)) if rows[i][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            value = -value
        entry = rows[column][column]
        value *= entry
        for i in range(column + 1, len(rows)):
            factor = rows[i][column] / entry
            for j in range(column + 1, len(rows)):
                rows[i][j] -= factor * rows[column][j]
            rows[i][column] = 0
    return value


def independent_rows(matrix):
    pivots = {}
    chosen = []
    for index, row in enumerate(matrix):
        row = [Fraction(value) for value in row]
        for column, basis in sorted(pivots.items()):
            coefficient = row[column]
            row = [a - coefficient * b for a, b in zip(row, basis)]
        column = next((i for i, value in enumerate(row) if value), None)
        if column is not None:
            entry = row[column]
            pivots[column] = [value / entry for value in row]
            chosen.append(index)
    return chosen


def derivative(points, edge):
    i, j = edge
    a, b = (points[i][axis] - points[j][axis] for axis in (0, 1))
    row = [0] * 18
    row[2 * i], row[2 * i + 1] = 2 * a + b, a + 2 * b
    row[2 * j], row[2 * j + 1] = -2 * a - b, -a - 2 * b
    return row


def main():
    evidence_parser(__doc__, quick=False).parse_args()
    expected = json.loads(
        (Path(__file__).parent / 'assets' / 'configuration.json').read_text()
    )
    points = expected['points']
    check = Checker()
    valid = (
        len(points) == 9
        and all(len(point) == 2 and all(type(v) is int for v in point) for point in points)
        and len(set(map(tuple, points))) == 9
    )
    check.check('nine distinct integer triangular-coordinate points', valid)
    if not valid:
        return check.finish()

    classes = defaultdict(list)
    for i, j in combinations(range(9), 2):
        classes[q(points[i][0] - points[j][0], points[i][1] - points[j][1])].append((i, j))
    spectrum = {str(distance): len(edges) for distance, edges in classes.items()}
    check.check(
        'all 36 pairs have the eight positive lengths and stated multiplicities',
        sum(spectrum.values()) == 36
        and min(classes) > 0
        and spectrum == expected['multiplicities'],
    )
    collinear = [
        list(triple) for triple in combinations(range(9), 3)
        if determinant([[1, *points[i]] for i in triple]) == 0
    ]
    cyclic = [
        list(quadruple) for quadruple in combinations(range(9), 4)
        if determinant([[1, *points[i], q(*points[i])] for i in quadruple]) == 0
    ]
    check.check('exact collinear triple list', collinear == expected['collinear'] == [[1, 2, 3]])
    check.check('exact circle quadruple list', cyclic == expected['concyclic'])
    check.check(
        'each circle quadruple is a genuine circle',
        all(
            determinant([[1, *points[i]] for i in triple]) != 0
            for quadruple in cyclic for triple in combinations(quadruple, 3)
        ),
    )
    labels, jacobian = [], []
    for _, edges in sorted(classes.items()):
        base = edges[0]
        for edge in edges[1:]:
            labels.append([list(edge), list(base)])
            jacobian.append([
                x - y for x, y in zip(derivative(points, edge), derivative(points, base))
            ])
    check.check('all 28 exact equality labels', len(labels) == 28 and labels == expected['constraint_labels'])
    gauge = [row[4:] for row in jacobian]
    chosen = independent_rows(gauge)
    check.check('first fourteen rows give the stated gauge basis', chosen == expected['independent_row_indices'] == list(range(14)))
    square = [gauge[i] for i in chosen]
    check.check('complete square matrix matches the retained input', square == expected['square_matrix'])
    minor = determinant(square) if len(square) == 14 else Fraction(0)
    check.check('exact nonsingular determinant', minor == Fraction(expected['square_minor']) == -1102248)
    check.check('full and gauge ranks both fourteen', len(independent_rows(jacobian)) == len(chosen) == 14)
    print(json.dumps({'square_minor': str(minor), 'full_rank': len(independent_rows(jacobian)), 'gauge_rank': len(chosen)}))
    return check.finish()


if __name__ == '__main__':
    sys.exit(main())

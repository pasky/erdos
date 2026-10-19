"""Check the displayed 8- and 20-column prime-tensor circuits.

Only two prescribed matrices and three prescribed minors are constructed:
the eight-point seed in S_3 x S_3 x S_3 with its coefficient vector and a
unit 7-by-7 minor, and the twenty-point lift in S_3 x S_5 x S_7 with its
coefficient vector and two 19-by-19 minors of determinants 2 and -1. A
nonzero (n-1)-minor together with a full-support relation proves a rational
circuit; a coefficient of absolute value one makes the displayed integer
relation primitive, and its coefficient two excludes every nonzero ternary
relation. Arithmetic is exact Bareiss elimination; no search runs.

Run from the repository root:
    uv run --no-sync python wiki/research/erdos_774/evidence/prime_circuit/main.py

Dependencies are the standard library and the installed root ``tools``
package. There are no file inputs, output files, random choices or reduced
modes. Expected runtime is under a second. Failed obligations exit nonzero,
including under ``python -O``. This finite check proves no chromatic
growth.
"""

from __future__ import annotations

import sys

import tools

__all__ = [
    'main',
]

# fix the eight-point seed, its relation and the unit minor selection
_SEED = [(0, 0, 0), (0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 1, 0), (2, 1, 1), (2, 2, 2), (0, 0, 1)]
_SEED_COEFFICIENTS = [-1, 1, -1, 1, -1, 1, -1, -2]
_SEED_ROWS = [0, 1, 2, 3, 4, 6, 7]
_SEED_COLUMNS = [0, 1, 2, 3, 4, 5, 7]

# fix the twenty-point lift, its relation and the two minor selections
_J_SET, _K_SET = [0, 3, 4, 5, 6], [2, 3, 4]
_LIFT = (
    [(0, 0, z) for z in _J_SET] + [(0, 1, 2)]
    + [(0, y, 1) for y in _K_SET] + [(1, 0, 2)]
    + [(1, 1, z) for z in _J_SET] + [(2, 1, 1)]
    + [(2, y, 2) for y in _K_SET] + [(0, 0, 1)]
)
_LIFT_COEFFICIENTS = [-1] * 5 + [1] + [-1] * 3 + [1] + [-1] * 5 + [1] + [-1] * 3 + [-2]
_LIFT_ROWS = [0, 1, 2, 3, 4, 5, 7, 8, 13, 14, 19, 20, 26, 30, 31, 32, 33, 34, 35]


def _simplex_column(p: int, symbol: int) -> list[int]:
    """Return the simplex column of one symbol in dimension p-1."""
    if symbol == p - 1:
        return [-1] * (p - 1)
    return [int(i == symbol) for i in range(p - 1)]


def _tensor_matrix(sides: tuple[int, ...], labels: list[tuple[int, ...]]) -> list[list[int]]:
    """Return the integer matrix whose columns are the tensor columns of the labels."""
    columns = []
    for label in labels:
        column = [1]
        for p, symbol in zip(sides, label):
            column = [a * b for a in column for b in _simplex_column(p, symbol)]
        columns.append(column)
    return [list(row) for row in zip(*columns)]


def _determinant(matrix: list[list[int]]) -> int:
    """Return the determinant by Bareiss elimination with row pivoting."""
    a = [row[:] for row in matrix]
    n = len(a)
    if any(len(row) != n for row in a):
        raise ValueError('determinant of a nonsquare matrix')
    previous, sign = 1, 1
    for k in range(n - 1):
        pivot_row = next((r for r in range(k, n) if a[r][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                value = a[i][j] * pivot - a[i][k] * a[k][j]
                if value % previous:
                    raise ValueError('Bareiss exact division failed')
                a[i][j] = value // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def _minor(matrix: list[list[int]], rows: list[int], columns: list[int]) -> int:
    """Return the determinant of a selected submatrix."""
    return _determinant([[matrix[i][j] for j in columns] for i in rows])


def _zero_relation(matrix: list[list[int]], coefficients: list[int]) -> bool:
    """Decide whether a coefficient vector lies in the kernel."""
    return all(sum(a * b for a, b in zip(row, coefficients)) == 0 for row in matrix)


def main() -> int:
    """Run every finite obligation and return the shared checker's exit code."""
    # parse the fixed-domain interface and check the eight-point seed
    parser = tools.evidence_parser('Check the displayed prime-tensor circuits.', quick=False)
    parser.parse_args()
    checker = tools.Checker()
    seed_matrix = _tensor_matrix((3, 3, 3), _SEED)
    checker.check('seed matrix is 8 by 8', len(seed_matrix) == 8 and len(seed_matrix[0]) == 8)
    checker.check('seed coefficients give a zero relation', _zero_relation(seed_matrix, _SEED_COEFFICIENTS))
    seed_minor = _minor(seed_matrix, _SEED_ROWS, _SEED_COLUMNS)
    checker.check('seed unit minor equals -1', seed_minor == -1, f'observed {seed_minor}')

    # check the twenty-point lift, its relation and its two minors
    checker.check('lift has twenty distinct labels and coefficients', len(_LIFT) == len(set(_LIFT)) == len(_LIFT_COEFFICIENTS) == 20)
    lift_matrix = _tensor_matrix((3, 5, 7), _LIFT)
    checker.check('lift matrix is 48 by 20', len(lift_matrix) == 48 and len(lift_matrix[0]) == 20)
    checker.check('lift coefficients give a zero relation', _zero_relation(lift_matrix, _LIFT_COEFFICIENTS))
    minor_two = _minor(lift_matrix, _LIFT_ROWS, list(range(19)))
    minor_unit = _minor(lift_matrix, _LIFT_ROWS, list(range(18)) + [19])
    checker.check('lift minor on columns 0..18 equals 2', minor_two == 2, f'observed {minor_two}')
    checker.check('lift minor on columns 0..17,19 equals -1', minor_unit == -1, f'observed {minor_unit}')

    # check that both relations have full support, a unit coefficient and a coefficient two
    checker.check(
        'both relations are full-support, primitive and nonternary',
        all(all(rel) and 1 in rel and -2 in rel for rel in (_SEED_COEFFICIENTS, _LIFT_COEFFICIENTS)),
    )
    print('seed rank 7, lift rank 19; primitive coefficient-two kernels; unit minors -1, -1')
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

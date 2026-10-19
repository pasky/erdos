"""Check the affine-fiber threshold on small simplex tensors.

Run from the repository root:
    uv run --no-sync python wiki/theory/integer_sequences/L269_simplex_affine_fiber_threshold/evidence/main.py

The fixed domain comprises q=3,4, every k<q, every fiber value, and
two specified nonzero normal vectors. Independence is certified by
full column rank modulo 65521, which implies rational independence.
At k=q and k=q+1, explicit ternary trades are mapped through the
original integer tensor matrix. GF(4) uses X^2+X+1. The whole run
uses exact arithmetic, the standard library and tools, takes under
ten seconds and uses less than 32 MiB. --quick has identical coverage.
These diagnostics do not reduce the infinite theorem to finite cases.
"""

from __future__ import annotations

import itertools
from collections import defaultdict

import tools

__all__ = ['main']


def _add(q: int, a: int, b: int) -> int:
    return (a + b) % q if q == 3 else a ^ b


def _mul(q: int, a: int, b: int) -> int:
    if q == 3:
        return a * b % q
    value = 0
    while b:
        if b & 1:
            value ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7
    return value


def _dot(q: int, a: tuple[int, ...], b: tuple[int, ...]) -> int:
    value = 0
    for x, y in zip(a, b, strict=True):
        value = _add(q, value, _mul(q, x, y))
    return value


def _column(q: int, point: tuple[int, ...]) -> dict[tuple[int, ...], int]:
    choices = [range(q - 1) if x == q - 1 else (x,) for x in point]
    sign = (-1) ** point.count(q - 1)
    return dict.fromkeys(itertools.product(*choices), sign)


def _image(
    q: int, coefficients: dict[tuple[int, ...], int]
) -> dict[tuple[int, ...], int]:
    result: dict[tuple[int, ...], int] = defaultdict(int)
    for point, value in coefficients.items():
        for row, sign in _column(q, point).items():
            result[row] += value * sign
    return {row: value for row, value in result.items() if value}


def _rank(rows: list[list[int]]) -> int:
    prime = 65521
    rows = [[x % prime for x in row] for row in rows]
    rank = 0
    for j in range(len(rows[0]) if rows else 0):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][j]), None)
        if pivot is None:
            continue
        rows[pivot], rows[rank] = rows[rank], rows[pivot]
        inverse = pow(rows[rank][j], -1, prime)
        rows[rank] = [x * inverse % prime for x in rows[rank]]
        for i in range(rank + 1, len(rows)):
            factor = rows[i][j]
            if factor:
                rows[i] = [
                    (x - factor * y) % prime
                    for x, y in zip(rows[i], rows[rank], strict=True)
                ]
        rank += 1
    return rank


def main() -> int:
    """Check small independent fibers and the actual integer trades."""
    tools.evidence_parser(__doc__).parse_args()
    check = tools.Checker()
    check.check('the rank modulus is prime', all(65521 % d for d in range(2, 256)))
    field_valid = True
    for q in (3, 4):
        for a, b, c in itertools.product(range(q), repeat=3):
            field_valid &= _mul(q, a, _add(q, b, c)) == _add(
                q, _mul(q, a, b), _mul(q, a, c)
            )
        field_valid &= all(
            any(_mul(q, a, b) == 1 for b in range(1, q)) for a in range(1, q)
        )
    check.check(
        'the specified F3 and F4 arithmetic has distributivity and inverses',
        field_valid,
    )
    independent_cases = 0
    for q in (3, 4):
        for k in range(1, q):
            normals = {(1,) * k, tuple(1 + i % (q - 1) for i in range(k))}
            for normal in sorted(normals):
                for value in range(q):
                    points = [
                        x
                        for x in itertools.product(range(q), repeat=k)
                        if _dot(q, normal, x) == value
                    ]
                    columns = [_column(q, x) for x in points]
                    rows = [
                        [col.get(row, 0) for col in columns]
                        for row in itertools.product(range(q - 1), repeat=k)
                    ]
                    check.check(
                        f'q={q}, k={k}, normal={normal}, fiber={value}: rational independence',
                        _rank(rows) == len(points) == q ** (k - 1),
                    )
                    independent_cases += 1
    trade_cases = 0
    for q in (3, 4):
        for k in (q, q + 1):
            for normal in ((1,) * q, tuple(1 + i % (q - 1) for i in range(q))):
                second = tuple(_mul(q, i, normal[i]) for i in range(q))
                for value in range(q):
                    plus = {}
                    minus = {}
                    for x in itertools.product(range(q), repeat=q):
                        if _dot(q, normal, x) != value:
                            continue
                        b = _dot(q, second, x)
                        point = x + (0,) * (k - q)
                        if b == 0:
                            plus[point] = 1
                        elif b == 1:
                            minus[point] = -1
                    trade = plus | minus
                    label = f'q={q}, k={k}, normal={normal}, fiber={value}'
                    check.check(
                        f'{label}: exact support and fiber',
                        len(trade) == 2 * q ** (q - 2)
                        and not (plus.keys() & minus.keys()),
                    )
                    check.check(
                        f'{label}: the integer tensor image vanishes',
                        not _image(q, trade),
                    )
                    check.check(
                        f'{label}: the two separate terms have nonzero image',
                        bool(_image(q, plus)) and bool(_image(q, minus)),
                    )
                    trade_cases += 1
    check.check(
        'all 29 independent fibers and 28 trades were covered',
        independent_cases == 29 and trade_cases == 28,
    )
    return check.finish()


if __name__ == '__main__':
    raise SystemExit(main())

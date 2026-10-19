"""Exact finite checks for powerful numbers and products; runtime a few seconds.

Run from the repository root:
uv run --no-sync python wiki/research/powerful_numbers_and_products/evidence/main.py

Inputs are assets/finite_cases.json relative to this file. Python integers and
integer square/cube roots are used throughout. The seven square-quotient
instances exhaust all k=2 representations for each listed root, by the divisor
reduction proved on the owning research page. The Pell check exhausts the one CLOSED interval
specified in the input, via the unique a^2 b^3 representation with b squarefree.
Other checks concern only the listed witnesses. No unbounded catalog statement,
recurrence tail, different block length, or numerical logarithm is certified.
"""

from __future__ import annotations

import json
import sys
from math import isqrt, prod
from pathlib import Path

from tools import Checker, evidence_parser


def icbrt(n: int) -> int:
    """Return the integer cube root of a nonnegative integer."""
    lo, hi = 0, n + 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid**3 <= n:
            lo = mid
        else:
            hi = mid
    return lo


def squarefree(n: int) -> bool:
    """Test squarefreeness by exhausting every possible square divisor."""
    return all(n % (p * p) for p in range(2, isqrt(n) + 1))


def square_quotients(a: int) -> list[list[int]]:
    """Exhaust the divisor domain for a fixed square quotient at length two."""
    d = a * a - 1
    out = []
    for u in range(1, isqrt(d) + 1):
        if d % u:
            continue
        v = d // u
        if (u + v) % (2 * a) or (v - u) % 2:
            continue
        y, x = (u + v) // (2 * a), (v - u) // 2
        if y >= 3 and y % 2 and x % 2 and x >= y + 4:
            out.append([(y - 3) // 2, (x - 3) // 2])
    return sorted(out)


def powerful_interval(lo: int, hi: int) -> list[int]:
    """Enumerate every powerful integer in a positive closed interval."""
    out = []
    for b in range(1, icbrt(hi) + 1):
        if not squarefree(b):
            continue
        b3 = b**3
        lower = isqrt((lo - 1) // b3) + 1
        upper = isqrt(hi // b3)
        out.extend(a * a * b3 for a in range(lower, upper + 1))
    return sorted(out)


def valuation(n: int, p: int) -> int:
    """Return the exponent of a prime in a positive integer."""
    if n <= 0 or p < 2:
        raise ValueError('valuation requires n > 0 and p >= 2')
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def main() -> int:
    """Run all retained finite certificates and return a failing status on disagreement."""
    evidence_parser(__doc__, quick=False).parse_args()
    data = json.loads((Path(__file__).parent / 'assets/finite_cases.json').read_text())
    check = Checker()
    check.check(
        'exact inventory of seven square-quotient roots',
        sorted(row['root'] for row in data['square_quotients_k2'])
        == [2, 3, 4, 5, 6, 10, 35],
    )
    check.check(
        'exact inventory of three adjacent-block witnesses',
        sorted(data['divisibility_witnesses']) == [[1, 1], [2, 5], [3, 4]],
    )
    for row in data['square_quotients_k2']:
        a = row['root']
        actual = square_quotients(a)
        check.check(
            f'k=2 full divisor domain for square root {a}', actual == row['pairs']
        )
        for n, m in actual:
            check.check(
                f'original quotient and disjointness for {a}, {n}, {m}',
                n >= 0
                and m >= n + 2
                and (m + 1) * (m + 2) == a * a * (n + 1) * (n + 2),
            )
    row = data['pell_progression']
    x, y, b = row['x'], row['y'], row['core']
    lo, hi = row['interval']
    check.check(
        'Pell seed and exact progression',
        x * x - b**3 * y * y == 2
        and lo == (x - 2) ** 2
        and hi == x * x - 2
        and (x - 1) ** 2 - lo == hi - (x - 1) ** 2,
    )
    check.check(
        'exhaustive powerful values in the specified closed interval',
        powerful_interval(lo, hi) == row['powerful_values'],
    )
    check.check(
        'four extra powerful values defeat consecutiveness at the seed',
        len(set(row['powerful_values']) - {lo, (x - 1) ** 2, hi}) == 4,
    )
    row = data['smooth_part_counterexample']
    n = row['n']
    check.check(
        'exact 2,3 valuations at the retained counterexample',
        valuation(n * (n + 1), 2) == row['v2']
        and valuation(n * (n + 1), 3) == row['v3'],
    )
    check.check(
        'integer inequalities proving ratio exceeds 3/log(2)',
        n == 311 * 3**14 and n < 2**31 and 2**15 > 3 * 311 * 31,
    )
    for n, k in data['divisibility_witnesses']:
        lower = prod(range(n, n + k))
        upper = prod(range(n + k, n + 2 * k))
        check.check(f'adjacent blocks at n={n}, k={k}', upper % lower == 0)
    row = data['separated_blocks']
    blocks = row['blocks']
    products = [prod(range(a, b + 1)) for a, b in blocks]
    check.check(
        'disjoint length-three nonsquare blocks with square combined product',
        blocks[0][1] < blocks[1][0]
        and all(b - a + 1 == 3 for a, b in blocks)
        and all(isqrt(v) ** 2 != v for v in products)
        and prod(products) == row['square_root'] ** 2,
    )
    return check.finish()


if __name__ == '__main__':
    sys.exit(main())

"""Check finite spectral diagnostics for repeated simplex lattices.

Run from the repository root:
    uv run --no-sync python wiki/theory/integer_sequences/L271_repeated_simplex_extraction/evidence/main.py

The fixed full-lattice domain is (b,k)=(1,1..5),(2,1..3),(3,1..2).
All 254 nonempty spectral subfamilies are checked at (1,3),(2,2).
Every nonempty downset is checked at (1,3),(1,4),(2,2),(3,2).
Arithmetic is exact: integer Smith forms, Bareiss determinants and
rational comparisons. Dependencies are tools, the standard library,
and the named retained Smith helper. No private inputs are used.
Runtime is under thirty seconds and memory below 64 MiB. --quick
has the same coverage. No numerical theta estimate is asserted, and
these finite diagnostics do not replace the unbounded author proof.
"""

from __future__ import annotations

import importlib.util
from fractions import Fraction
from pathlib import Path

import tools

__all__ = ['main']

_WIKI = Path(__file__).resolve().parents[4]
_SMITH = _WIKI / 'research/erdos_774/evidence/moment_band_determinants/main.py'
_SPEC = importlib.util.spec_from_file_location('simplex_smith_helper', _SMITH)
if _SPEC is None or _SPEC.loader is None:
    raise ImportError(f'Cannot load the retained Smith helper: {_SMITH}')
_MODULE = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_MODULE)


def _frequencies(b: int, k: int) -> list[int]:
    block = (1 << b) - 1
    return [
        s
        for s in range(1 << (b * k))
        if any(not (s & (block << (b * i))) for i in range(k))
    ]


def _exponent(d: int, frequencies: list[int]) -> Fraction:
    rows = [[(-1) ** (s & x).bit_count() for x in range(1 << d)] for s in frequencies]
    invariants = _MODULE.smith_invariants(rows)
    if len(invariants) != len(frequencies) or any(
        v <= 0 or v & (v - 1) for v in invariants
    ):
        raise ValueError(
            'The Walsh rows lack full rank or a Smith invariant is not a power of two'
        )
    return Fraction(d * len(frequencies), 2) - sum(
        v.bit_length() - 1 for v in invariants
    )


def _determinant(matrix: list[list[int]]) -> int:
    a = [row[:] for row in matrix]
    previous = 1
    for k in range(len(a) - 1):
        pivot = a[k][k]
        if not pivot:
            raise ValueError('A positive definite Gram matrix has a zero leading pivot')
        for i in range(k + 1, len(a)):
            for j in range(k + 1, len(a)):
                numerator = pivot * a[i][j] - a[i][k] * a[k][j]
                value, remainder = divmod(numerator, previous)
                if remainder:
                    raise ValueError('Bareiss division is not exact')
                a[i][j] = value
            a[i][k] = 0
        previous = pivot
    return a[-1][-1] if a else 1


def _downsets(frequencies: list[int], d: int) -> tuple[int, bool]:
    index = {s: i for i, s in enumerate(frequencies)}
    required = []
    for s in frequencies:
        required.append(sum(1 << index[s ^ (1 << j)] for j in range(d) if s & (1 << j)))
    count = 0
    valid = True
    full_degree = sum(s.bit_count() for s in frequencies)
    for mask in range(1, 1 << len(frequencies)):
        members = [i for i in range(len(frequencies)) if mask & (1 << i)]
        if any(required[i] & mask != required[i] for i in members):
            continue
        count += 1
        total_degree = sum(frequencies[i].bit_count() for i in members)
        valid &= total_degree * len(frequencies) <= full_degree * len(members)
    return count, valid


def main() -> int:
    """Check determinant formulas, small spectral minima and all small downsets."""
    tools.evidence_parser(__doc__).parse_args()
    check = tools.Checker()
    pairs = (
        [(1, k) for k in range(1, 6)]
        + [(2, k) for k in range(1, 4)]
        + [(3, k) for k in range(1, 3)]
    )
    for b, k in pairs:
        d, q = b * k, 1 << b
        frequencies = _frequencies(b, k)
        expected = Fraction(b * k * (q - 1) ** (k - 1), 2)
        exponent = _exponent(d, frequencies)
        label = f'q={q}, k={k}'
        check.check(
            f'{label}: spectral dimension', len(frequencies) == q**k - (q - 1) ** k
        )
        check.check(f'{label}: saturated Smith covolume', exponent == expected)
        gram = [
            [1 << (d - (s | t).bit_count()) for t in frequencies] for s in frequencies
        ]
        check.check(
            f'{label}: monomial Gram determinant',
            _determinant(gram) == 1 << int(2 * expected),
        )
    total = 0
    for b, k in ((1, 3), (2, 2)):
        d = b * k
        frequencies = _frequencies(b, k)
        full = _exponent(d, frequencies) / len(frequencies)
        violations = []
        for mask in range(1, 1 << len(frequencies)):
            family = [s for i, s in enumerate(frequencies) if mask & (1 << i)]
            if _exponent(d, family) / len(family) < full:
                violations.append(mask)
            total += 1
        check.check(
            f'b={b}, k={k}: every nonempty spectral subfamily has at least the full normalized covolume',
            not violations,
        )
    check.check('all 254 nonempty spectral subfamilies were checked', total == 254)
    for b, k, expected_count in ((1, 3, 18), (1, 4, 166), (2, 2, 25), (3, 2, 361)):
        count, valid = _downsets(_frequencies(b, k), b * k)
        check.check(
            f'b={b}, k={k}: all {expected_count} nonempty downsets obey the mean-degree bound',
            count == expected_count and valid,
        )
    return check.finish()


if __name__ == '__main__':
    raise SystemExit(main())

"""Check a candidate scalar determinant bound on ten moment-lattice pairs.

The full domain is the ten pairs (d, ell) = (8,5), (8,6), (10,6), (10,7),
(12,7), (12,8), (16,9), (16,10), (20,11), (20,12) and every nonempty
pattern A of degrees in {0, ..., ell}, 16,694 patterns in total. For each
pattern the scalar expression on the owning page, built from the layer
multiplicities h_j = binom(d, j) - binom(d, j-1), the truncated sets
A_j = A intersect [j, d-j], and the binary valuation sums nu_j, is
compared with the full normalized covolume (d - ell) binom(d, ell) / (2
sum_(s <= ell) binom(d, s)). The checks are that no pattern gives a value
below the full normalized covolume, that the full prefix attains each
minimum, and that the ten recorded minima are reproduced. Arithmetic is
exact rational arithmetic; no search runs.

Run from the repository root:
    uv run --no-sync python wiki/research/erdos_774/evidence/moment_scalar_bound/main.py

Dependencies are the standard library and the installed root ``tools``
package. There are no file inputs, output files, random choices or reduced
modes. Expected runtime is a few seconds. Failed obligations exit nonzero,
including under ``python -O``. The expression is a diagnostic, not a
theorem: the compression proof on the owning lemma page supersedes it.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from math import comb

import tools

__all__ = [
    'lower',
    'main',
]

# fix the ten pairs and the recorded minima, each equal to the full covolume
_PAIRS = [(8, 5), (8, 6), (10, 6), (10, 7), (12, 7), (12, 8), (16, 9), (16, 10), (20, 11), (20, 12)]
_MINIMA = {
    (8, 5): Fraction(28, 73), (8, 6): Fraction(28, 247), (10, 6): Fraction(105, 212),
    (10, 7): Fraction(45, 242), (12, 7): Fraction(990, 1651), (12, 8): Fraction(990, 3797),
    (16, 9): Fraction(40040, 50643), (16, 10): Fraction(24024, 58651),
    (20, 11): Fraction(125970, 130771), (20, 12): Fraction(41990, 75883),
}
_PATTERNS = 16_694


def _v2(x: int) -> int:
    """Return the binary valuation of a positive integer."""
    return (x & -x).bit_length() - 1


def lower(d: int, levels: list[int]) -> Fraction:
    """Evaluate the candidate scalar expression for one degree pattern."""
    twice = rank = 0
    for j in range(d // 2 + 1):
        h = comb(d, j) - (comb(d, j - 1) if j else 0)
        lev = [s for s in levels if j <= s <= d - j]
        size = len(lev)
        vv = sum(_v2(t - s) for a, s in enumerate(lev) for t in lev[a + 1:]) - sum(_v2(b) for a in range(size) for b in range(1, a + 1))
        twice += h * ((d - 2 * j) * size - size * (size - 1) - 2 * vv)
        rank += h * size
    return Fraction(twice, 2 * rank)


def main() -> int:
    """Run every finite obligation and return the shared checker's exit code."""
    # parse the fixed-domain interface and scan every pattern of every pair
    parser = tools.evidence_parser('Check the candidate scalar bound on ten pairs.', quick=False)
    parser.parse_args()
    checker = tools.Checker()
    total = 0
    for d, ell in _PAIRS:
        full = Fraction((d - ell) * comb(d, ell), 2 * sum(comb(d, s) for s in range(ell + 1)))
        best, failures, patterns = full, 0, 0
        prefix_value = None
        for mask in range(1, 1 << (ell + 1)):
            levels = [s for s in range(ell + 1) if mask >> s & 1]
            value = lower(d, levels)
            patterns += 1
            if value < full:
                failures += 1
            if value < best:
                best = value
            if levels == list(range(ell + 1)):
                prefix_value = value
        total += patterns
        label = f'(d, ell) = ({d}, {ell})'
        checker.check(f'{label}: no pattern is below the full normalized covolume', failures == 0, f'{failures} violations')
        checker.check(f'{label}: the full prefix attains the minimum {_MINIMA[(d, ell)]}', prefix_value == best == full == _MINIMA[(d, ell)], f'observed {best}')
    checker.check('16,694 patterns in total', total == _PATTERNS, f'observed {total}')
    print(f'{total} patterns scanned; zero violations of the tested comparison')
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

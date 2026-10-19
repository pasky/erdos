"""Check the finite rare-distance examples in the owning research note.

Enumerate every nonempty subset of {0, 1, 2, 3}^2. Count distances after
(x, y) -> (x, (1 + sqrt(2)) y) by exact integer coefficient pairs, then
check the quarter bound and the more precise midline bound. Also count
distances after (x, y) -> (x + sqrt(2) y, (1 + sqrt(3)) y), using the
coefficients of 1, sqrt(2), sqrt(3), and check its all-rare conclusion.
Check the complete seven-point spectrum retained in the research note.

Run from the repository root:
    uv run --no-sync python wiki/research/leads/number_field_rare_distances/evidence/main.py

Dependencies are the standard library and the installed root tools package.
There are no file inputs, random choices, output files, or reduced modes.
Runtime is a few seconds. Failure exits nonzero, including with python -O.
This finite check does not establish a theorem for arbitrary configurations.
"""

from __future__ import annotations

import sys
from collections import Counter
from itertools import combinations

import tools

__all__ = ['spectra', 'main']

# fix the complete finite search domain and the retained seven-point witness
_GRID = tuple((x, y) for x in range(4) for y in range(4))
_WITNESS = ((0, 0), (0, 2), (1, 1), (1, 3), (2, 0), (2, 2), (3, 1))
_WITNESS_SPECTRUM = {
    (4, 0): 3,
    (4, 2): 8,
    (12, 2): 2,
    (12, 8): 3,
    (16, 8): 3,
    (28, 18): 2,
}


def spectra(
    points: tuple[tuple[int, int], ...],
) -> tuple[Counter[tuple[int, int]], Counter[tuple[int, int, int]]]:
    """Count unordered squared distances by their exact field coefficients."""
    rectangle: Counter[tuple[int, int]] = Counter()
    shear: Counter[tuple[int, int, int]] = Counter()
    for (x, y), (u, v) in combinations(points, 2):
        dx, dy = x - u, y - v
        rectangle[(dx * dx + 3 * dy * dy, 2 * dy * dy)] += 1
        shear[(dx * dx + 6 * dy * dy, 2 * dx * dy, 2 * dy * dy)] += 1
    return rectangle, shear


def main() -> int:
    """Run the stated finite domain and report any failing configuration."""
    parser = tools.evidence_parser('Check finite rare-distance bounds.', quick=False)
    parser.parse_args()
    checker = tools.Checker()
    failures: dict[str, tuple[tuple[int, int], ...]] = {}
    count = 0

    # enumerate actual pair distances independently of the anchor-counting proof
    for mask in range(1, 1 << len(_GRID)):
        points = tuple(point for i, point in enumerate(_GRID) if mask >> i & 1)
        n = len(points)
        rectangle, shear = spectra(points)
        rare = sum(multiplicity <= n for multiplicity in rectangle.values())
        left = min(x for x, _ in points)
        right = max(x for x, _ in points)
        midline = sum(2 * x == left + right for x, _ in points)
        bound = (n - midline + 3) // 4 + max(midline - 1, 0)

        if 4 * rare < n - 1:
            failures.setdefault('quarter bound', points)
        if rare < bound:
            failures.setdefault('midline bound', points)
        if any(multiplicity > n - 1 for multiplicity in shear.values()):
            failures.setdefault('shear multiplicities', points)
        if len(shear) < n - 1:
            failures.setdefault('shear distinct distances', points)
        if sum(rectangle.values()) != n * (n - 1) // 2:
            failures.setdefault('unordered pair coverage', points)
        count += 1

    checker.check('all 65,535 nonempty subsets visited', count == 65_535)
    for name in (
        'quarter bound',
        'midline bound',
        'shear multiplicities',
        'shear distinct distances',
        'unordered pair coverage',
    ):
        checker.check(name, name not in failures, f'witness: {failures.get(name)}')

    # this witness rules out the stronger claim that every stretched distance is rare
    rectangle, _ = spectra(_WITNESS)
    checker.check(
        'complete seven-point spectrum',
        rectangle == _WITNESS_SPECTRUM,
        f'observed {dict(rectangle)}',
    )
    checker.check(
        'seven-point example has a distance occurring eight times',
        rectangle[(4, 2)] == 8 > len(_WITNESS),
    )
    print(f'checked {count} subsets and the retained seven-point spectrum')
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

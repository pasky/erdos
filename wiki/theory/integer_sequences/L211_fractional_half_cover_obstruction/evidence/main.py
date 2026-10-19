"""Check L211's fixed thirteen-point configuration using exact arithmetic.

Run from the repository root:
    uv run --no-sync python wiki/theory/integer_sequences/L211_fractional_half_cover_obstruction/evidence/main.py

The standard library and the root tools package suffice. The default run
checks all 8192 subsets, all ternary relations (by a split enumeration),
all two-color partitions, and both fractional certificates. No solver or
random search is used. Runtime is a few seconds and memory is below 32 MiB.
``--quick`` has the same complete coverage for this small input.
"""

from __future__ import annotations

import itertools
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

import tools

__all__ = ['main']

_HERE = Path(__file__).resolve().parent


def _subset_relations(vectors: list[list[int]]) -> set[int]:
    """Find every relation support through collisions of subset sums."""
    n = len(vectors)
    sums = [tuple(0 for _ in vectors[0])] * (1 << n)
    buckets: dict[tuple[int, ...], list[int]] = defaultdict(list)
    supports: set[int] = set()
    for mask in range(1 << n):
        if mask:
            bit = mask & -mask
            row = vectors[bit.bit_length() - 1]
            sums[mask] = tuple(
                a + b for a, b in zip(sums[mask ^ bit], row, strict=True)
            )
        key = sums[mask]
        for other in buckets[key]:
            supports.add(mask ^ other)
        buckets[key].append(mask)
    return supports


def _ternary_half(
    vectors: list[list[int]], dimension: int
) -> dict[tuple[int, ...], list[int]]:
    """Index every half-word by its vector sum, retaining multiplicity."""
    buckets: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for coefficients in itertools.product((-1, 0, 1), repeat=len(vectors)):
        value = tuple(
            sum(c * v[j] for c, v in zip(coefficients, vectors, strict=True))
            for j in range(dimension)
        )
        mask = sum(1 << i for i, c in enumerate(coefficients) if c)
        buckets[value].append(mask)
    return buckets


def _ternary_relations(vectors: list[list[int]]) -> tuple[set[int], int]:
    """Enumerate all zero ternary sums by joining the two half-word tables."""
    split = len(vectors) // 2
    left = _ternary_half(vectors[:split], len(vectors[0]))
    right = _ternary_half(vectors[split:], len(vectors[0]))
    supports: set[int] = set()
    count = 0
    for value, masks in left.items():
        opposite = tuple(-x for x in value)
        for first in masks:
            for second in right.get(opposite, []):
                mask = first | (second << split)
                if mask:
                    supports.add(mask)
                    count += 1
    return supports, count


def _independence(n: int, supports: set[int]) -> list[bool]:
    """Mark all supersets of a nonzero relation as dependent."""
    dependent = [False] * (1 << n)
    for support in supports:
        dependent[support] = True
    for i in range(n):
        bit = 1 << i
        for mask in range(1 << n):
            if mask & bit and dependent[mask ^ bit]:
                dependent[mask] = True
    return [not value for value in dependent]


def _two_colorable(mask: int, independent: list[bool]) -> bool:
    submask = mask
    while True:
        if independent[submask] and independent[mask ^ submask]:
            return True
        if not submask:
            return False
        submask = (submask - 1) & mask


def main() -> int:
    """Recompute every finite obligation and return a nonzero code on failure."""
    tools.evidence_parser(__doc__).parse_args()
    checker = tools.Checker()
    data = json.loads((_HERE / 'assets' / 'configuration.json').read_text())
    vectors = data['vectors']
    valid = (
        len(vectors) == 13
        and all(len(row) == 5 and all(x in (0, 1) for x in row) for row in vectors)
        and len({tuple(row) for row in vectors}) == 13
        and all(any(row) for row in vectors)
    )
    checker.check('thirteen distinct nonzero binary vectors in five coordinates', valid)
    if not valid:
        return checker.finish()
    n = len(vectors)
    full = (1 << n) - 1
    scalars = [sum(x * 16**j for j, x in enumerate(row)) for row in vectors]
    checker.check(
        'base-sixteen scalars agree with the stated integer set',
        sorted(scalars) == data['integers'],
    )
    checker.check(
        'the base is larger than the maximum ternary coordinate sum plus one',
        n + 1 < 16,
    )

    supports = _subset_relations(vectors)
    other_supports, relation_count = _ternary_relations(vectors)
    checker.check(
        'subset collisions and full ternary enumeration give identical supports',
        supports == other_supports,
    )
    checker.check(
        'there are 724 nonzero ternary words and 216 supports',
        relation_count == 724 and len(supports) == 216,
    )
    scalar_supports = _subset_relations([[a] for a in scalars])
    checker.check(
        'the scalar encoding preserves the complete relation-support family',
        scalar_supports == supports,
    )
    independent = _independence(n, supports)
    counts = [
        sum(independent[m] and m.bit_count() == size for m in range(1 << n))
        for size in range(n + 1)
    ]
    checker.check(
        'the complete independence profile agrees with the proof',
        counts == [1, 13, 78, 284, 673, 982, 652, 16, 0, 0, 0, 0, 0, 0],
    )
    ranks = [mask.bit_count() if independent[mask] else 0 for mask in range(1 << n)]
    for i in range(n):
        bit = 1 << i
        for mask in range(1 << n):
            if mask & bit:
                ranks[mask] = max(ranks[mask], ranks[mask ^ bit])
    eta = min(Fraction(ranks[mask], mask.bit_count()) for mask in range(1, 1 << n))
    checker.check(
        'every nonempty subset has extraction ratio at least 7/13, with equality',
        eta == Fraction(7, 13),
    )
    checker.check(
        'the full configuration has largest dissociated size seven', ranks[full] == 7
    )
    checker.check(
        'none of the 8192 two-color partitions is proper',
        not _two_colorable(full, independent),
    )
    colors = [sum(1 << i for i in block) for block in data['three_colors']]
    checker.check(
        'the retained three classes form a proper partition',
        len(colors) == 3
        and sum(colors) == full
        and all(independent[c] for c in colors)
        and all(not (a & b) for a, b in itertools.combinations(colors, 2)),
    )
    checker.check(
        'deleting any one point gives a proper two-coloring',
        all(_two_colorable(full ^ (1 << i), independent) for i in range(n)),
    )

    dual = data['dual_numerators']
    checker.check(
        'the dual certificate has thirteen nonnegative entries totaling 37',
        len(dual) == n and min(dual) >= 0 and sum(dual) == 37,
    )
    if len(dual) != n:
        return checker.finish()
    checker.check(
        'every dissociated subset has dual numerator at most nineteen',
        all(
            sum(dual[i] for i in range(n) if mask & (1 << i)) <= 19
            for mask in range(1 << n)
            if independent[mask]
        ),
    )
    primal = data['primal_numerators']
    valid_primal = all(0 <= mask <= full and weight >= 0 for mask, weight in primal)
    checker.check(
        'the primal certificate has valid nonnegative weights and masks', valid_primal
    )
    if not valid_primal:
        return checker.finish()
    checker.check(
        'every positive primal weight is on a dissociated subset',
        all(not weight or independent[mask] for mask, weight in primal),
    )
    checker.check(
        'the primal numerators total 37', sum(weight for _, weight in primal) == 37
    )
    coverage = [
        sum(weight for mask, weight in primal if mask & (1 << i)) for i in range(n)
    ]
    checker.check(
        'each point has primal coverage exactly nineteen', coverage == [19] * n
    )
    return checker.finish()


if __name__ == '__main__':
    raise SystemExit(main())

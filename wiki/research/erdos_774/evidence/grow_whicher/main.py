"""Check the Grow--Whicher 15-point example and its fractional certificate.

The fixed input is E = {3^j + kj : 1 <= j <= 5, 0 <= k <= 2}. The full domain
is all 2**15 subsets, tabulated by exact subset-sum bitsets and dynamic
programming. The checks are: hereditary extraction ratio two, dissociated
rank eight, no proper two-coloring, the one-point deletion's ratio 13/7 and
two-coloring, the fractional dissociated coloring number 27/13 (an integer
weighting and an explicit 27-set cover), fourteen signed relations of rank
fourteen, and the no-clone certificate around this numerical realization.
Arithmetic is exact integer and rational arithmetic; no search or solver
runs.

Run from the repository root:
    uv run --no-sync python wiki/research/erdos_774/evidence/grow_whicher/main.py

Dependencies are the standard library and the installed root ``tools``
package. There are no file inputs, output files, random choices or reduced
modes. Expected runtime is a few seconds. Failed obligations exit nonzero,
including under ``python -O``. This finite check proves no unbounded
coloring theorem.
"""

from __future__ import annotations

import sys
from fractions import Fraction

import tools

__all__ = [
    'main',
]

# fix the numerical realization and the expected finite parameters
_E = sorted({3**j + k * j for j in range(1, 6) for k in range(3)})
_DISSOCIATED_SUBSETS = 7_568
_RANK = 8
_LOW_RANK = 6

# fix the one-point deletion and its proper two-coloring
_A_PARTITION = ([5, 9, 11, 13, 30, 85, 243], [4, 27, 33, 81, 89, 248, 253])

# retain the 27-set cover with multiplicities as bitmasks over E
_COVER = [
    (4, 0x132D), (2, 0x14E6), (1, 0x18B6), (2, 0x24A7),
    (2, 0x29CC), (3, 0x2D19), (1, 0x4565), (2, 0x45E2),
    (3, 0x4699), (1, 0x49AC), (6, 0x7A52),
]

# retain fourteen signed relations as (positive side, negative side)
_RELATIONS = [
    ([9], [4, 5]),
    ([3, 11], [5, 9]),
    ([5, 11], [3, 4, 9]),
    ([13], [4, 9]),
    ([4, 13], [3, 5, 9]),
    ([27], [3, 4, 9, 11]),
    ([30], [3, 5, 9, 13]),
    ([33], [4, 5, 11, 13]),
    ([81], [4, 9, 11, 27, 30]),
    ([85], [3, 5, 9, 11, 27, 30]),
    ([89], [3, 4, 5, 9, 11, 27, 30]),
    ([243], [4, 5, 11, 27, 30, 81, 85]),
    ([248], [5, 9, 11, 27, 30, 81, 85]),
    ([253], [3, 5, 9, 13, 27, 30, 81, 85]),
]

# retain two minimal dependent supports through each point for the clone test
_TWIN_SUPPORTS = {
    3: ([3, 27, 30], [3, 30, 33]),
    4: ([4, 5, 9], [4, 9, 13]),
    5: ([4, 5, 9], [5, 243, 248]),
    9: ([4, 5, 9], [4, 9, 13]),
    11: ([3, 5, 9, 11], [3, 5, 11, 13]),
    13: ([4, 9, 13], [3, 5, 11, 13]),
    27: ([3, 27, 30], [5, 9, 13, 27]),
    30: ([3, 27, 30], [3, 30, 33]),
    33: ([3, 30, 33], [9, 11, 13, 33]),
    81: ([4, 81, 85], [3, 5, 81, 89]),
    85: ([4, 81, 85], [4, 85, 89]),
    89: ([4, 85, 89], [3, 5, 81, 89]),
    243: ([5, 243, 248], [3, 13, 243, 253]),
    248: ([5, 243, 248], [5, 248, 253]),
    253: ([5, 248, 253], [3, 13, 243, 253]),
}


def _mask(points: list[int]) -> int:
    """Return the bitmask of a point list over E."""
    return sum(1 << _E.index(x) for x in points)


def main() -> int:
    """Run every finite obligation and return the shared checker's exit code."""
    # parse the fixed-domain interface and tabulate every subset
    parser = tools.evidence_parser('Check the Grow--Whicher 15-point example.', quick=False)
    parser.parse_args()
    checker = tools.Checker()
    count = 1 << len(_E)
    full = count - 1
    low = (1 << 12) - 1
    # a positive bitset stores all subset sums exactly when the set is dissociated
    sums = [0] * count
    sums[0] = 1
    rank = [0] * count
    for mask in range(1, count):
        bit = mask & -mask
        i = bit.bit_length() - 1
        smaller = mask ^ bit
        if sums[smaller] and not (sums[smaller] & (sums[smaller] << _E[i])):
            sums[mask] = sums[smaller] | (sums[smaller] << _E[i])
            rank[mask] = mask.bit_count()
        else:
            rest = mask
            while rest:
                bit = rest & -rest
                rest ^= bit
                rank[mask] = max(rank[mask], rank[mask ^ bit])
    independent = [mask for mask in range(1, count) if sums[mask]]

    # check the extraction, rank and coloring facts of the full example
    checker.check('7568 nonempty dissociated subsets', len(independent) == _DISSOCIATED_SUBSETS, f'observed {len(independent)}')
    checker.check('dissociated rank eight', rank[full] == _RANK, f'observed {rank[full]}')
    checker.check('the first twelve points have rank six', rank[low] == _LOW_RANK, f'observed {rank[low]}')
    checker.check('hereditary extraction ratio two', all(mask.bit_count() <= 2 * rank[mask] for mask in range(count)))
    checker.check('no proper two-coloring', not any(sums[full ^ mask] for mask in independent))
    checker.check(
        'each of the three five-point rows is dissociated',
        all(sums[_mask([3**j + k * j for j in range(1, 6)])] for k in range(3)),
    )

    # check the one-point deletion used by the anchor-gluing construction
    a_mask = full ^ (1 << _E.index(3))
    ratio = max(Fraction(mask.bit_count(), rank[mask]) for mask in range(1, count) if not (mask & ~a_mask))
    checker.check('deleting 3 gives hereditary ratio 13/7', ratio == Fraction(13, 7), f'observed {ratio}')
    checker.check(
        'the displayed partition of the deletion covers it',
        sorted(_A_PARTITION[0] + _A_PARTITION[1]) == [x for x in _E if x != 3],
    )
    checker.check('both partition classes are dissociated', all(sums[_mask(part)] for part in _A_PARTITION))
    checker.check('the deletion itself is not dissociated', not sums[a_mask])
    anchor_failures = 0
    for mask in independent:
        if mask & ~a_mask or not sums[a_mask ^ mask]:
            continue
        if not (sums[mask] & (sums[mask] << 3)) or not (sums[a_mask ^ mask] & (sums[a_mask ^ mask] << 3)):
            anchor_failures += 1
    checker.check('every class of every proper two-coloring of the deletion represents 3', anchor_failures == 0)

    # check the fractional coloring number from both sides
    weight = max(2 * (mask & low).bit_count() + (mask >> 12).bit_count() for mask in independent)
    checker.check('every dissociated set has weight at most 13', weight == 13, f'observed {weight}')
    checker.check('all cover members are dissociated', all(sums[mask] for _, mask in _COVER))
    checker.check('the cover has total multiplicity 27', sum(multiplicity for multiplicity, _ in _COVER) == 27)
    checker.check(
        'the cover meets every point exactly 13 times',
        all(sum(mult for mult, mask in _COVER if (mask >> i) & 1) == 13 for i in range(15)),
    )

    # check that fourteen listed signed relations have rational rank fourteen
    basis: dict[int, list[Fraction]] = {}
    relation_failures = 0
    for left, right in _RELATIONS:
        if len(set(left + right)) != len(left + right) or sum(left) != sum(right):
            relation_failures += 1
            continue
        row = [Fraction(int(x in left) - int(x in right)) for x in _E]
        for pivot, old in sorted(basis.items()):
            coefficient = row[pivot]
            row = [x - coefficient * y for x, y in zip(row, old)]
        pivot = next((i for i, x in enumerate(row) if x), None)
        if pivot is None:
            relation_failures += 1
            continue
        coefficient = row[pivot]
        basis[pivot] = [x / coefficient for x in row]
    checker.check('fourteen listed relations are genuine and independent', relation_failures == 0 and len(basis) == 14)

    # check the no-clone certificate around this numerical realization
    clone_failures = 0
    for n, supports in _TWIN_SUPPORTS.items():
        candidates = None
        for support in supports:
            mask = _mask(support)
            if sums[mask] or not all(sums[mask ^ (1 << _E.index(x))] for x in support):
                clone_failures += 1
            signed = {0}
            for x in support:
                if x != n:
                    signed = {s + sign * x for s in signed for sign in (-1, 1)}
            positive = {x for x in signed if x > 0}
            candidates = positive if candidates is None else candidates & positive
        if candidates != {n}:
            clone_failures += 1
    checker.check('no distinct positive clone around the fixed realization', clone_failures == 0, f'{clone_failures} failures')
    print('hereditary ratio 2; chromatic number 3; fractional chromatic number 27/13; relation rank 14')
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

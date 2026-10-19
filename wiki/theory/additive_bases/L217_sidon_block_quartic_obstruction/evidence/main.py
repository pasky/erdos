"""Check the exact finite witness for the block-law quartic obstruction.

Domain: s=3, W=21, N=63, k=9, D=20; every subset of sizes two, three
and four, and every one of the W distinct block rotations. Exact integer
accumulation and Fraction arithmetic give the original, zeroed and uniformly
renormalized expectations of the centered short-pair square. This checks a
finite witness, not the asymptotic theorem, which has a written proof.
The same exhaustive calculation checks the largest admixture with the uniform
fixed-size law allowed by difference 1. A separate exact graph formula checks
the uniform endpoint's mean and variance. The signed cyclic test is positive
at this small mixture, an exact control against interpreting its asymptotic
obstruction as a theorem for every finite size.

A separate control enumerates every outcome of the small block law with
B=3, m=2, W=4, including every rotation, and compares its direct mean,
variance and repeated-difference mass with the moment calculation.

Run from the repository root:
    uv run --no-sync python \
      wiki/theory/additive_bases/L217_sidon_block_quartic_obstruction/evidence/main.py

Dependencies: numpy and the repository tools package. No external inputs,
network or output files. Both default and --quick exhaust the same finite
witness. Expected runtime under ten seconds, memory under 300 MB, one thread.
"""

from __future__ import annotations

import itertools
import math
from dataclasses import dataclass
from fractions import Fraction

import numpy as np

import tools


@dataclass(frozen=True)
class Moments:
    """Exact values of the specified functional and the original law."""

    mean: Fraction
    variance: Fraction
    repeated_mass: Fraction
    zeroed_variance: Fraction
    renormalized_variance: Fraction
    totals: dict[int, Fraction]
    allowed_totals: dict[int, Fraction]
    coverage: dict[int, int]


def exact_dot(left: np.ndarray, right: np.ndarray) -> int:
    """Use bounded int64 accumulation or Python integers, including signed weights."""
    bound = (
        int(left.max()) * max(abs(int(right.min())), abs(int(right.max()))) * len(left)
    )
    if bound < 2**63:
        return int(np.dot(left, right))
    return sum(int(a) * int(b) for a, b in zip(left, right, strict=True))


def block_moments(
    blocks: int,
    occupancy: int,
    width: int,
    uniform_weight: Fraction = Fraction(0),
    cyclic_weighted: bool = False,
) -> Moments:
    """Sum every moment of degrees two to four over all block rotations."""
    size = blocks * width
    marks = blocks * occupancy
    distance = width - 1
    if not (blocks >= 3 and 1 <= occupancy <= width and width >= 4):
        raise ValueError('unsupported block parameters')
    if not 0 <= uniform_weight <= 1:
        raise ValueError('mixture weight')
    falling = {
        degree: Fraction(
            math.prod(range(occupancy - degree + 1, occupancy + 1)),
            math.prod(range(width - degree + 1, width + 1)),
        )
        for degree in range(1, 5)
    }
    density = falling[1]
    # The number of same-block pairs distinguishes the occupancy partitions
    # of any set of at most four positions.
    weights = {
        2: {0: density**2, 1: falling[2]},
        3: {0: density**3, 1: falling[2] * density, 3: falling[3]},
        4: {
            0: density**4,
            1: falling[2] * density**2,
            2: falling[2] ** 2,
            3: falling[3] * density,
            6: falling[4],
        },
    }
    for degree, table in weights.items():
        uniform_moment = Fraction(math.comb(marks, degree), math.comb(size, degree))
        weights[degree] = {
            score: (1 - uniform_weight) * value + uniform_weight * uniform_moment
            for score, value in table.items()
        }
    mean = Fraction(0)
    second = Fraction(0)
    second_zeroed = Fraction(0)
    second_renormalized = Fraction(0)
    repeated = Fraction(0)
    totals: dict[int, Fraction] = {}
    allowed: dict[int, Fraction] = {}
    coverage: dict[int, int] = {}
    for degree in (2, 3, 4):
        table = weights[degree]
        denominator = math.lcm(*(value.denominator for value in table.values()))
        positions = np.array(
            list(itertools.combinations(range(size), degree)), dtype=np.int64
        )
        pairs = list(itertools.combinations(range(degree), 2))
        numerators = np.zeros(len(positions), dtype=np.int64)
        largest_weight = max(int(value * denominator) for value in table.values())
        # Moment numerators remain in int64; weighted dot products are
        # separately bounded and fall back to exact Python integers.
        if len(positions) * width * largest_weight >= 2**63:
            raise ValueError('integer accumulator could overflow')
        for rotation in range(width):
            block_ids = ((positions + rotation) % size) // width
            same_pairs = np.zeros(len(positions), dtype=np.int8)
            for left, right in pairs:
                same_pairs += block_ids[:, left] == block_ids[:, right]
            for score, value in table.items():
                numerators[same_pairs == score] += int(value * denominator)

        denominator *= width
        totals[degree] = Fraction(int(numerators.sum()), denominator)
        coverage[degree] = len(positions)
        differences = np.stack(
            [positions[:, right] - positions[:, left] for left, right in pairs],
            axis=1,
        )
        ordered = np.sort(differences, axis=1)
        forbidden = np.any(ordered[:, 1:] == ordered[:, :-1], axis=1)
        allowed[degree] = Fraction(int(numerators[~forbidden].sum()), denominator)
        if allowed[degree] <= 0:
            raise ValueError('renormalization denominator is not positive')
        factor = Fraction(math.comb(marks, degree), 1) / allowed[degree]

        def edge_weight(difference: np.ndarray) -> np.ndarray:
            if not cyclic_weighted:
                return (difference <= distance).astype(np.int64)
            cyclic_distance = np.minimum(difference, size - difference)
            return np.where(cyclic_distance <= distance, 3 * cyclic_distance - width, 0)

        scale = 3 * width if cyclic_weighted else 1
        edge_values = edge_weight(differences)
        if degree == 2:
            mean = Fraction(
                exact_dot(numerators, edge_values[:, 0]), denominator * scale
            )
            coefficient = edge_values[:, 0] ** 2
            repeated_coefficient = np.zeros(len(positions), dtype=np.int64)
        elif degree == 3:
            coefficient = edge_values.sum(axis=1) ** 2 - (edge_values**2).sum(axis=1)
            repeated_coefficient = (
                2
                * edge_values[:, 0] ** 2
                * (
                    positions[:, 1] - positions[:, 0]
                    == positions[:, 2] - positions[:, 1]
                )
            )
        else:
            coefficient = np.zeros(len(positions), dtype=np.int64)
            repeated_coefficient = np.zeros(len(positions), dtype=np.int64)
            for a, b, c, d in ((0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)):
                first = positions[:, b] - positions[:, a]
                other = positions[:, d] - positions[:, c]
                first_weight, other_weight = edge_weight(first), edge_weight(other)
                coefficient += 2 * first_weight * other_weight
                repeated_coefficient += 2 * (first == other) * first_weight**2

        degree_second = Fraction(
            exact_dot(numerators, coefficient), denominator * scale**2
        )
        degree_zeroed = Fraction(
            exact_dot(numerators, coefficient * (~forbidden)), denominator * scale**2
        )
        second += degree_second
        second_zeroed += degree_zeroed
        second_renormalized += factor * degree_zeroed
        repeated += Fraction(
            exact_dot(numerators, repeated_coefficient), denominator * scale**2
        )
    return Moments(
        mean,
        second - mean**2,
        repeated,
        second_zeroed - mean**2,
        second_renormalized - mean**2,
        totals,
        allowed,
        coverage,
    )


def direct_small_law(
    cyclic_weighted: bool = False,
) -> tuple[Fraction, Fraction, Fraction]:
    """Enumerate the independent B=3, m=2, W=4 sample space directly."""
    width, blocks, occupancy = 4, 3, 2
    size = width * blocks
    scale = 3 * width if cyclic_weighted else 1
    weights = [0] * size
    for difference in range(1, size):
        if cyclic_weighted:
            cyclic_distance = min(difference, size - difference)
            if cyclic_distance < width:
                weights[difference] = 3 * cyclic_distance - width
        elif difference < width:
            weights[difference] = 1
    choices = list(itertools.combinations(range(width), occupancy))
    count = first = second = repeated = 0
    for cells in itertools.product(choices, repeat=blocks):
        base = [
            width * block + point for block, cell in enumerate(cells) for point in cell
        ]
        for rotation in range(size):
            points = sorted((point + rotation) % size for point in base)
            multiplicities = [0] * size
            for left, right in itertools.combinations(points, 2):
                difference = right - left
                multiplicities[difference] += 1
            short_pairs = sum(
                w * r for w, r in zip(weights, multiplicities, strict=True)
            )
            count += 1
            first += short_pairs
            second += short_pairs**2
            repeated += sum(
                w * w * r * (r - 1)
                for w, r in zip(weights, multiplicities, strict=True)
            )
    if count != math.comb(width, occupancy) ** blocks * size:
        raise ValueError('direct sample coverage')
    mean = Fraction(first, count * scale)
    return (
        mean,
        Fraction(second, count * scale**2) - mean**2,
        Fraction(repeated, count * scale**2),
    )


def main() -> int:
    """Check the finite negative square and a direct enumeration control."""
    parser = tools.evidence_parser('Check the exact block-law quartic witness.')
    parser.parse_args()
    checker = tools.Checker()
    small = block_moments(3, 2, 4)
    direct = direct_small_law()
    checker.check(
        'moment calculation agrees with every outcome of the small block law',
        (small.mean, small.variance, small.repeated_mass) == direct,
    )
    small_weighted = block_moments(3, 2, 4, cyclic_weighted=True)
    checker.check(
        'signed cyclic moments agree with independent direct enumeration',
        (small_weighted.mean, small_weighted.variance, small_weighted.repeated_mass)
        == direct_small_law(cyclic_weighted=True),
    )
    witness = block_moments(3, 3, 21)
    for degree in (2, 3, 4):
        checker.check(
            f'every {degree}-subset and every distinct rotation is included',
            witness.coverage[degree] == math.comb(63, degree),
        )
        checker.check(
            f'original degree-{degree} total equals binom(9,{degree})',
            witness.totals[degree] == math.comb(9, degree),
        )
    checker.check('short-pair mean', witness.mean == Fraction(883, 49))
    checker.check(
        'original variance is positive', witness.variance == Fraction(259248, 60025)
    )
    checker.check(
        'repeated short-difference mass',
        witness.repeated_mass == Fraction(2885503, 228095),
    )
    checker.check(
        'zeroing gives the stated negative centered square',
        witness.zeroed_variance == Fraction(-5178216, 162925),
    )
    expected = Fraction(-941730900101847658, 109020148158776379)
    checker.check(
        'degreewise renormalization leaves the exact negative square',
        witness.renormalized_variance == expected and expected < 0,
        str(witness.renormalized_variance),
    )
    # Independent graph intersection counts for the uniform endpoint.
    size, marks, distance = 63, 9, 20
    degrees = [min(i, distance) + min(size - 1 - i, distance) for i in range(size)]
    edges = sum(degrees) // 2
    adjacent = sum(d * (d - 1) for d in degrees)
    p = {t: Fraction(math.comb(marks, t), math.comb(size, t)) for t in (2, 3, 4)}
    uniform = block_moments(3, 3, 21, Fraction(1))
    graph_variance = (
        edges * (p[2] - p[4]) + adjacent * (p[3] - p[4]) + edges**2 * (p[4] - p[2] ** 2)
    )
    checker.check(
        'uniform endpoint agrees with independent graph mean and variance',
        uniform.mean == edges * p[2] and uniform.variance == graph_variance,
    )
    weight = Fraction(33, 82)
    mixed = block_moments(3, 3, 21, weight)
    checker.check(
        'mixture mean and variance agree with the law of total variance',
        mixed.mean == (1 - weight) * witness.mean + weight * uniform.mean
        and mixed.variance
        == (1 - weight) * witness.variance
        + weight * uniform.variance
        + weight * (1 - weight) * (uniform.mean - witness.mean) ** 2,
    )
    density = Fraction(1, 7)
    depletion = (density - density**2) / (21 * 20)
    pair = lambda d: (
        (1 - weight) * (density**2 - depletion * max(21 - min(d, 63 - d), 0))
        + weight * p[2]
    )
    checker.check(
        'mixture satisfies every difference capacity with equality at difference 1',
        62 * pair(1) == 1 and all((63 - d) * pair(d) <= 1 for d in range(1, 63)),
    )
    checker.check(
        'mixture satisfies every sum capacity, including diagonals',
        all(
            sum(
                pair(total - 2 * i) for i in range(max(0, total - 62), (total + 1) // 2)
            )
            + (density if total % 2 == 0 else 0)
            <= 1
            for total in range(125)
        ),
    )
    checker.check(
        'capacity-limited uniform admixture still gives a negative centered square',
        mixed.renormalized_variance < 0,
        str(mixed.renormalized_variance),
    )
    weighted = block_moments(3, 3, 21, weight, cyclic_weighted=True)
    finite_positive = Fraction(
        26206418542771452345267619483, 89042295412084245797931582420
    )
    checker.check(
        'small-size control: the signed cyclic square is still positive at N=63',
        weighted.renormalized_variance == finite_positive and finite_positive > 0,
        str(weighted.renormalized_variance),
    )
    return checker.finish()


if __name__ == '__main__':
    raise SystemExit(main())

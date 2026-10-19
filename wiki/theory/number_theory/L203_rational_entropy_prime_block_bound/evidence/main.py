"""Certify the rational entropy inequality used by L203.

The fixed seven-point measure is in assets/measure.json. Recompute its
three marginals, check injective differences, and enclose every logarithm
by exact fractions using 32 terms of the atanh series with a proved tail
bound. Fail unless max projection entropy / joint entropy < 56213/100000.
This checks only the finite entropy inequality; the type-class and prime
realization arguments are in the proof. Python standard library and the
repository Checker; one thread, a few seconds, well under 100 MB.
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

from tools import Checker, evidence_parser

TERMS = 32


def series_bounds(v: Fraction) -> tuple[Fraction, Fraction]:
    """Enclose log((1+v)/(1-v)) for rational 0<=v<=1/3."""
    if not 0 <= v <= Fraction(1, 3):
        raise ValueError('Series argument is outside its certified range')
    square = v * v
    power = v
    partial = Fraction(0)
    for j in range(TERMS):
        partial += 2 * power / (2 * j + 1)
        power *= square
    tail = 2 * power / ((2 * TERMS + 1) * (1 - square))
    return partial, partial + tail


LOG_TWO = series_bounds(Fraction(1, 3))


def log_bounds(value: Fraction) -> tuple[Fraction, Fraction]:
    """Enclose the logarithm of a positive rational by reducing to [1,2)."""
    if value <= 0:
        raise ValueError('Logarithm input must be positive')
    exponent = 0
    reduced = Fraction(value)
    while reduced >= 2:
        reduced /= 2
        exponent += 1
    while reduced < 1:
        reduced *= 2
        exponent -= 1
    lower, upper = series_bounds((reduced - 1) / (reduced + 1))
    if exponent >= 0:
        return lower + exponent * LOG_TWO[0], upper + exponent * LOG_TWO[1]
    return lower + exponent * LOG_TWO[1], upper + exponent * LOG_TWO[0]


def entropy_bounds(weights: list[int], denominator: int) -> tuple[Fraction, Fraction]:
    """Enclose the entropy of a rational probability vector."""
    lower = Fraction(0)
    upper = Fraction(0)
    for weight in weights:
        probability = Fraction(weight, denominator)
        log_lower, log_upper = log_bounds(probability)
        lower -= probability * log_upper
        upper -= probability * log_lower
    return lower, upper


def main() -> int:
    """Check the retained witness and its strict entropy inequality."""
    evidence_parser(__doc__, quick=False).parse_args()
    checker = Checker()
    path = Path(__file__).resolve().parent / 'assets' / 'measure.json'
    data = json.loads(path.read_text())
    points = [tuple(point) for point in data['points']]
    weights = data['weights']
    denominator = data['denominator']
    shape_ok = (
        len(points) == len(weights) == 7
        and all(len(point) == 2 for point in points)
        and all(type(v) is int for point in points for v in point)
        and all(type(w) is int and w > 0 for w in weights)
        and type(denominator) is int
        and denominator > 0
        and sum(weights) == denominator
    )
    checker.check(
        'seven integer points with positive rational masses summing to one', shape_ok
    )
    if not shape_ok:
        return checker.finish()
    checker.check(
        'the retained witness is the one stated in L203',
        points == [(0, 1), (1, 1), (1, 0), (2, 0), (2, -1), (3, -1), (3, -2)]
        and weights == [250, 28156, 224250, 494688, 224250, 28156, 250]
        and denominator == 1000000,
    )
    checker.check(
        'the seven differences a-b are distinct', len({a - b for a, b in points}) == 7
    )
    marginals = []
    for coordinate in range(3):
        marginal = defaultdict(int)
        for (a, b), weight in zip(points, weights):
            marginal[(a, b, a + b)[coordinate]] += weight
        marginals.append([weight for _, weight in sorted(marginal.items())])
    checker.check(
        'the three marginal mass lists match the proof',
        marginals == [[250, 252406, 718938, 28406]] * 2 + [[449000, 551000]],
    )
    cells = [(2 * b, a + b) for a, b in points]
    checker.check(
        'the cell transformation preserves the required projections and differences',
        all(
            (y - x, x, y, 2 * y - x) == (a - b, 2 * b, a + b, 2 * a)
            for (a, b), (x, y) in zip(points, cells)
        ),
    )
    joint_lower, joint_upper = entropy_bounds(weights, denominator)
    projection_bounds = [entropy_bounds(m, denominator) for m in marginals]
    max_lower = max(lower for lower, _ in projection_bounds)
    max_upper = max(upper for _, upper in projection_bounds)
    checker.check(
        'joint entropy has the stated rational enclosure',
        Fraction('1.2238605') < joint_lower <= joint_upper < Fraction('1.2238606'),
    )
    checker.check(
        'maximum projection entropy has the stated rational enclosure',
        Fraction('0.6879584') < max_lower <= max_upper < Fraction('0.6879585'),
    )
    checker.check(
        'the certified exponent is strictly below 56213/100000',
        joint_lower > 0 and 100000 * max_upper < 56213 * joint_lower,
    )
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

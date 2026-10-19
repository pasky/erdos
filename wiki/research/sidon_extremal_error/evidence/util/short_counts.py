"""Exact controls for the short-count covariance formulas.

Every outcome of the unrotated block law is enumerated at (s,W)=(2,4),
(3,4), (3,6), (4,6). Integer edge counts and Fraction arithmetic compare all
means and every covariance entry with the formulas in short_count_covariance.
This is finite coverage of those identities, not an asymptotic PSD claim.
Largest sample space: C(6,4)^4=50625, each with 16 points. One thread,
under 50 MB, expected runtime under ten seconds. The owning main.py runs it.
"""

from __future__ import annotations

import itertools
import math
from fractions import Fraction

from tools import Checker


def formula(s: int, width: int, d: int, e: int) -> Fraction:
    """Count internal, crossing and adjacent-boundary edge intersections."""
    f = {
        t: Fraction(
            math.prod(s - j for j in range(t)), math.prod(width - j for j in range(t))
        )
        for t in range(1, 5)
    }
    u = lambda a: (width - a) * f[2]
    v = lambda a: a * f[1] ** 2
    if d == e:
        count = max(width - 2 * d, 0)
        g = (
            (width - d) * f[2]
            + 2 * count * f[3]
            + ((width - d) ** 2 - (width - d) - 2 * count) * f[4]
            - u(d) ** 2
        )
        h = d * f[1] ** 2 + (d * d - d) * f[2] ** 2 - v(d) ** 2
    else:
        n = 2 * (width - max(d, e)) + 2 * max(width - d - e, 0)
        g = ((width - d) * (width - e) - n) * f[4] + n * f[3] - u(d) * u(e)
        h = (
            2 * min(d, e) * f[1] * f[2]
            + (d * e - 2 * min(d, e)) * f[2] ** 2
            - v(d) * v(e)
        )

    def j(a: int, b: int) -> Fraction:
        r = max(b - a, 0) + min(width - a, b)
        return f[1] * (r * f[2] + ((width - a) * b - r) * f[3]) - u(a) * v(b)

    t = max(d + e - width, 0)
    q = f[1] ** 2 * (t * f[1] + (d * e - t) * f[2]) - v(d) * v(e)
    return s * g + (s - 1) * h + 2 * (s - 1) * (j(d, e) + j(e, d)) + 2 * (s - 2) * q


def check_short_counts(checker: Checker) -> None:
    """Compare the formula with direct complete sample spaces."""
    for s, width in ((2, 4), (3, 4), (3, 6), (4, 6)):
        choices = list(itertools.combinations(range(width), s))
        first = [0] * (width - 1)
        second = [[0] * (width - 1) for _ in first]
        samples = 0
        for cells in itertools.product(choices, repeat=s):
            points = [b * width + x for b, cell in enumerate(cells) for x in cell]
            counts = [0] * (width - 1)
            for a, b in itertools.combinations(points, 2):
                difference = b - a
                if difference < width:
                    counts[difference - 1] += 1
            for d, a in enumerate(counts):
                first[d] += a
                for e, b in enumerate(counts):
                    second[d][e] += a * b
            samples += 1
        expected_samples = math.comb(width, s) ** s
        checker.check(
            f'short counts ({s},{width}): complete sample space',
            samples == expected_samples,
        )
        means = [Fraction(total, samples) for total in first]
        cov = [
            [
                Fraction(second[d][e], samples) - means[d] * means[e]
                for e in range(width - 1)
            ]
            for d in range(width - 1)
        ]
        f = {
            t: Fraction(
                math.prod(s - j for j in range(t)),
                math.prod(width - j for j in range(t)),
            )
            for t in range(1, 5)
        }
        checker.check(
            f'short counts ({s},{width}): all means and covariances',
            all(
                means[d - 1] == s * (width - d) * f[2] + (s - 1) * d * f[1] ** 2
                for d in range(1, width)
            )
            and all(
                cov[d - 1][e - 1] == formula(s, width, d, e)
                for d in range(1, width)
                for e in range(1, width)
            ),
        )
        kd = (
            -s * (f[3] - f[4])
            - (s - 1) * (f[1] * f[2] - f[2] ** 2)
            + 2 * (s - 1) * f[1] * (f[2] - f[3])
        )
        ka = (
            s * (f[3] - f[4])
            - 2 * (s - 1) * f[1] * (f[2] - f[3])
            + (s - 2) * f[1] ** 2 * (f[1] - f[2])
        )

        residual = [
            [
                cov[d - 1][e - 1] - kd * abs(d - e) - ka * abs(d + e - width)
                for e in range(1, width)
            ]
            for d in range(1, width)
        ]
        step1 = residual[0][2] - residual[0][1]
        step2 = residual[1][2] - residual[0][2]
        a2 = (step2 - step1) / 2
        a1 = step1 - a2
        a0 = residual[0][1] - 3 * a1 - 2 * a2
        checker.check(
            f'short counts ({s},{width}): exact two-kernel decomposition',
            all(
                residual[d - 1][e - 1] == a0 + a1 * (d + e) + a2 * d * e
                for d in range(1, width)
                for e in range(1, width)
                if d != e
            ),
        )

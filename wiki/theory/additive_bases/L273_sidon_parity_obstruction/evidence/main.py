"""Exact finite controls for the parity obstruction.

Domain: every subset of sizes two, three and four for (s,W)=(2,4), (2,8)
and (3,18), both unrotated and uniformly rotated block laws, and mixtures
with the uniform k-set law at weights 0, 1/2, 1. All arithmetic used for
decisions is integer or Fraction arithmetic. Integer vector accumulators
have explicit overflow guards. The largest support census is C(54,4).

Checks: full moment totals, direct Boolean-square coefficients, the parity
zeroing identity, independent balanced-hypergeometric genuine moments,
positive renormalization denominators and degreewise normalization. At
(s,W)=(2,4), a separate enumeration of every outcome evaluates the original
and zeroed polynomials and the surviving degree totals directly.

This is finite supplementary evidence. It does not certify the asymptotic
bound or require the square to be negative at these small parameters.

Run from the repository root:
    uv run --no-sync python \
      wiki/theory/additive_bases/L273_sidon_parity_obstruction/evidence/main.py

Dependencies: numpy and the root tools package. No external inputs, network,
or output files. Default and --quick have identical exhaustive coverage.
Expected runtime under thirty seconds and memory under 300 MB, one thread.
"""

from __future__ import annotations

import itertools
import math
from fractions import Fraction

import numpy as np

import tools


def falling(a: int, t: int) -> int:
    """Integer falling factorial, including a zero factor when t>a."""
    return math.prod(a - j for j in range(t))


def balanced_moments(size: int, marks: int) -> tuple[Fraction, Fraction]:
    """Compute the second and fourth moments from the sample distribution."""
    numerator2 = numerator4 = total = 0
    half = size // 2
    for evens in range(max(0, marks - half), min(marks, half) + 1):
        weight = math.comb(half, evens) * math.comb(half, marks - evens)
        imbalance = 2 * evens - marks
        total += weight
        numerator2 += weight * imbalance**2
        numerator4 += weight * imbalance**4
    if total != math.comb(size, marks):
        raise ValueError('hypergeometric sample space is incomplete')
    return Fraction(numerator2, total), Fraction(numerator4, total)


def exact_dot(values: np.ndarray, coefficients: np.ndarray) -> int:
    """Accumulate in int64 only after bounding every possible partial sum."""
    bound = int(np.max(np.abs(coefficients))) * int(values.max()) * len(values)
    if bound >= 2**63:
        return sum(int(a) * int(b) for a, b in zip(values, coefficients, strict=True))
    return int(values @ coefficients)


def census(s: int, width: int, checker: tools.Checker) -> dict:
    """Return exact totals for all three base laws at each degree."""
    size, marks = s * width, s * s
    f = {t: Fraction(falling(s, t), falling(width, t)) for t in range(1, 5)}
    weights = {
        2: {0: f[1] ** 2, 1: f[2]},
        3: {0: f[1] ** 3, 1: f[2] * f[1], 3: f[3]},
        4: {
            0: f[1] ** 4,
            1: f[2] * f[1] ** 2,
            2: f[2] ** 2,
            3: f[3] * f[1],
            6: f[4],
        },
    }
    result: dict = {}
    for degree in (2, 3, 4):
        positions = np.array(
            list(itertools.combinations(range(size), degree)), dtype=np.int64
        )
        pairs = list(itertools.combinations(range(degree), 2))
        signs = 1 - 2 * (positions % 2)
        differences = np.stack(
            [positions[:, b] - positions[:, a] for a, b in pairs], axis=1
        )
        ordered = np.sort(differences, axis=1)
        bad = np.any(ordered[:, 1:] == ordered[:, :-1], axis=1)
        edges = np.stack([signs[:, a] * signs[:, b] for a, b in pairs], axis=1)
        if degree == 2:
            coefficient = edges[:, 0] ** 2
            expected = np.ones(len(positions), dtype=np.int64)
        elif degree == 3:
            coefficient = edges.sum(axis=1) ** 2 - (edges**2).sum(axis=1)
            expected = 2 * edges.sum(axis=1)
        else:
            coefficient = np.zeros(len(positions), dtype=np.int64)
            for a, b, c, d in ((0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)):
                coefficient += 2 * signs[:, a] * signs[:, b] * signs[:, c] * signs[:, d]
            expected = 6 * signs.prod(axis=1)
        checker.check(
            f'N={size}, degree {degree}: full census and square coefficients',
            len(positions) == math.comb(size, degree)
            and bool(np.array_equal(coefficient, expected)),
        )
        denominator = math.lcm(*(p.denominator for p in weights[degree].values()))
        table = {score: int(p * denominator) for score, p in weights[degree].items()}
        if len(positions) * width * max(table.values()) >= 2**63:
            raise ValueError('moment accumulator might overflow')
        rotated = np.zeros(len(positions), dtype=np.int64)
        unrotated = np.zeros_like(rotated)
        for rotation in range(width):
            blocks = ((positions + rotation) % size) // width
            same = np.zeros(len(positions), dtype=np.int8)
            for a, b in pairs:
                same += blocks[:, a] == blocks[:, b]
            contribution = np.zeros(len(positions), dtype=np.int64)
            for score, numerator in table.items():
                contribution[same == score] = numerator
            rotated += contribution
            if rotation == 0:
                unrotated = contribution
        uniform = Fraction(math.comb(marks, degree), math.comb(size, degree))
        laws = (
            (unrotated, denominator),
            (rotated, denominator * width),
            (
                np.full(len(positions), uniform.numerator, dtype=np.int64),
                uniform.denominator,
            ),
        )
        for law, (values, den) in enumerate(laws):
            if int(values.max()) * len(values) >= 2**63:
                raise ValueError('total moment accumulator might overflow')
            total = Fraction(int(values.sum()), den)
            allowed = Fraction(int(values[~bad].sum()), den)
            second = Fraction(exact_dot(values, coefficient), den)
            zeroed = Fraction(exact_dot(values, coefficient * (~bad)), den)
            erased = Fraction(exact_dot(values, expected * bad), den)
            first = (
                Fraction(exact_dot(values, edges[:, 0]), den)
                if degree == 2
                else Fraction(0)
            )
            result[law, degree] = (total, allowed, second, zeroed, erased, first)
            checker.check(
                f'N={size}, law {law}, degree {degree}: totals and denominators',
                total == math.comb(marks, degree) and allowed > 0,
            )
    return result


def direct_small(rotated: bool, uniform: bool) -> tuple:
    """Average the actual polynomials over every outcome at s=2,W=4."""
    size, marks, width = 8, 4, 4
    if uniform:
        outcomes = list(itertools.combinations(range(size), marks))
    else:
        choices = list(itertools.combinations(range(width), 2))
        outcomes = []
        for left, right in itertools.product(choices, repeat=2):
            base = left + tuple(x + width for x in right)
            for rotation in range(size) if rotated else (0,):
                outcomes.append(tuple(sorted((x + rotation) % size for x in base)))
    first = second = zeroed = 0
    allowed = {3: 0, 4: 0}
    for points in outcomes:
        edges = list(itertools.combinations(points, 2))
        value = sum((-1) ** (b - a) for a, b in edges)
        first += value
        second += value**2
        for edge1, edge2 in itertools.product(edges, repeat=2):
            support = sorted(set(edge1 + edge2))
            sums = [
                a + b for a, b in itertools.combinations_with_replacement(support, 2)
            ]
            if len(set(sums)) == len(sums):
                zeroed += (-1) ** (sum(edge1) + sum(edge2))
        for degree in (3, 4):
            for support in itertools.combinations(points, degree):
                sums = [
                    a + b
                    for a, b in itertools.combinations_with_replacement(support, 2)
                ]
                allowed[degree] += len(set(sums)) == len(sums)
    expected = (
        math.comb(8, 4) if uniform else math.comb(4, 2) ** 2 * (8 if rotated else 1)
    )
    if len(outcomes) != expected:
        raise ValueError('direct sample-space census')
    return tuple(
        Fraction(v, expected) for v in (first, second, zeroed, allowed[3], allowed[4])
    )


def main() -> int:
    """Compare the exact moments with separate distribution calculations."""
    tools.evidence_parser(
        'Check the parity obstruction at finite parameters.'
    ).parse_args()
    checker = tools.Checker()
    for s, width in ((2, 4), (2, 8), (3, 18)):
        size, marks = s * width, s * s
        data = census(s, width, checker)
        block2, block4 = balanced_moments(width, s)
        mu2 = s * block2
        mu4 = s * block4 + 3 * s * (s - 1) * block2**2
        nu2, nu4 = balanced_moments(size, marks)
        for law in (0, 1):
            for alpha in (Fraction(0), Fraction(1, 2), Fraction(1)):
                rows = {
                    t: tuple(
                        (1 - alpha) * u + alpha * v
                        for u, v in zip(data[law, t], data[2, t], strict=True)
                    )
                    for t in (2, 3, 4)
                }
                mean = rows[2][5]
                second = sum(row[2] for row in rows.values())
                zeroed = sum(row[3] for row in rows.values())
                b2 = (1 - alpha) * mu2 + alpha * nu2
                b4 = (1 - alpha) * mu4 + alpha * nu4
                checker.check(
                    f'N={size}, rotated={bool(law)}, alpha={alpha}: genuine moments and zeroing identity',
                    2 * mean == b2 - marks
                    and 4 * (second - mean**2) == b4 - b2**2
                    and 4 * (zeroed - mean**2)
                    == b4 - b2**2 - 4 * (rows[3][4] + rows[4][4]),
                )
                factors = {
                    t: Fraction(math.comb(marks, t), 1) / rows[t][1] for t in (3, 4)
                }
                repaired = rows[2][3] + sum(factors[t] * rows[t][3] for t in (3, 4))
                checker.check(
                    f'N={size}, rotated={bool(law)}, alpha={alpha}: renormalization',
                    all(factors[t] * rows[t][1] == math.comb(marks, t) for t in (3, 4))
                    and repaired - zeroed
                    == sum((factors[t] - 1) * rows[t][3] for t in (3, 4)),
                )
        if (s, width) == (2, 4):
            for law in (0, 1, 2):
                calculated = (
                    data[law, 2][5],
                    sum(data[law, t][2] for t in (2, 3, 4)),
                    sum(data[law, t][3] for t in (2, 3, 4)),
                    data[law, 3][1],
                    data[law, 4][1],
                )
                checker.check(
                    f'law {law}: independent enumeration of every N=8 outcome',
                    calculated == direct_small(rotated=law == 1, uniform=law == 2),
                )
    return checker.finish()


if __name__ == '__main__':
    raise SystemExit(main())

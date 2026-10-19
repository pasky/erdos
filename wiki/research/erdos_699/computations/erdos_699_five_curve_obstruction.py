#!/usr/bin/env python3
"""Check the exact five-row curve obstruction using rational arithmetic.

Bézout and factorization turn the checked incidence inequalities into
sum_P w_P ord_P(F) <= deg(F) for every nonzero polynomial F.  This is an
obstruction to fixed curve factors plus residual dimension counting at one
capacity profile, not an assertion that an Erdős 699 counterexample exists.
"""

from fractions import Fraction
import json
from pathlib import Path


POINT_DENOMINATOR = 3100
HALF_POINT_NUMERATORS = {
    (0, 0): 403,
    (0, 1): 527,
    (0, 2): 1031,
    (0, 3): 676,
    (0, 4): 463,
    (1, 1): 1038,
    (1, 2): 874,
    (1, 3): 661,
    (2, 2): 852,
}
COVER_DENOMINATOR = 15500
# A triple (a,b,c) denotes the line ax+by+c=0.
LINE_COVER = [
    ((1, 0, 0), 1376),
    ((0, 1, 0), 1376),
    ((1, 0, -1), 1259),
    ((0, 1, -1), 1259),
    ((1, 0, -2), 1107),
    ((0, 1, -2), 1107),
    ((1, 1, -2), 2672),
    ((1, 1, -3), 2004),
    ((1, 1, -4), 2046),
]


def on_line(point, line):
    x, y = point
    a, b, c = line
    return a * x + b * y + c == 0


def report():
    points = [(a, r - a) for r in range(5) for a in range(r + 1)]
    numerators = {
        point: HALF_POINT_NUMERATORS[tuple(sorted(point))] for point in points
    }
    weights = {
        point: Fraction(numerator, POINT_DENOMINATOR)
        for point, numerator in numerators.items()
    }
    capacities = [Fraction(13, 100), Fraction(34, 100)] + [Fraction(1)] * 3
    row_sums = [
        sum(weights[point] for point in points if sum(point) == r)
        for r in range(5)
    ]
    assert row_sums == capacities

    cover_total = Fraction(sum(value for _, value in LINE_COVER), COVER_DENOMINATOR)
    assert cover_total == Fraction(7103, 7750) < 1
    point_records = []
    for point in points:
        cover_numerator = sum(
            value for line, value in LINE_COVER if on_line(point, line)
        )
        slack = Fraction(cover_numerator, COVER_DENOMINATOR) - weights[point]
        assert slack >= 0
        point_records.append({
            "point": list(point),
            "weight_numerator": numerators[point],
            "cover_numerator": cover_numerator,
            "cover_slack": str(slack),
        })
    assert {
        tuple(item["point"]): Fraction(item["cover_slack"])
        for item in point_records if Fraction(item["cover_slack"])
    } == {
        (0, 0): Fraction(737, 15500),
        (0, 4): Fraction(1107, 15500),
        (4, 0): Fraction(1107, 15500),
    }

    line_records = []
    for line, cover_numerator in LINE_COVER:
        incidence_weight = sum(
            weights[point] for point in points if on_line(point, line)
        )
        assert incidence_weight <= 1
        expected = Fraction(2757, 3100) if line in ((1, 0, -2), (0, 1, -2)) else 1
        assert incidence_weight == expected
        line_records.append({
            "coefficients": list(line),
            "cover_numerator": cover_numerator,
            "own_weighted_incidence": str(incidence_weight),
        })

    norm_squared = sum(weight * weight for weight in weights.values())
    assert norm_squared == Fraction(270691, 310000)
    q = 1 / norm_squared
    assert q == Fraction(310000, 270691) > 1

    # A matching primal solution uses only x=0,y=0,x=1,y=1 as factors.
    # Its residual at P is q*w_P; its capacity gain is exactly one.
    row_multiplicities = [q * Fraction(value, 3100) for value in (1181, 1107, 1420, 1065, 852)]
    factors = [
        ((1, 0, 0), q * Fraction(389, 3100)),
        ((0, 1, 0), q * Fraction(389, 3100)),
        ((1, 0, -1), q * Fraction(191, 3100)),
        ((0, 1, -1), q * Fraction(191, 3100)),
    ]
    residuals = {}
    for point in points:
        residual = row_multiplicities[sum(point)] - sum(
            multiplicity for line, multiplicity in factors if on_line(point, line)
        )
        assert residual == q * weights[point] > 0
        residuals[point] = residual
    gain = sum(a * m for a, m in zip(capacities, row_multiplicities)) - sum(
        multiplicity for _, multiplicity in factors
    )
    objective = sum(value * value for value in residuals.values())
    assert gain == 1
    assert objective == q

    return {
        "scope": "An exact obstruction to fixed curve factors plus residual dimension counting at one five-row capacity profile; no bad triple or whole-index result is claimed.",
        "point_weight_denominator": POINT_DENOMINATOR,
        "line_cover_denominator": COVER_DENOMINATOR,
        "points": point_records,
        "row_capacities": [str(value) for value in capacities],
        "row_weight_sums": [str(value) for value in row_sums],
        "line_cover": line_records,
        "cover_total": str(cover_total),
        "universal_polynomial_inequality": "sum_P w_P ord_P(F) <= deg(F) for every nonzero F",
        "noncover_irreducible_curve_bound": "sum_P w_P mult_P(C) <= (7103/7750) deg(C)",
        "weight_norm_squared": str(norm_squared),
        "minimum_quadratic_objective": str(q),
        "matching_primal": {
            "row_multiplicities": [str(value) for value in row_multiplicities],
            "line_factors": [
                {"coefficients": list(line), "multiplicity": str(value)}
                for line, value in factors
            ],
            "residual_rule": "residual_P = q*w_P",
            "capacity_gain": str(gain),
            "quadratic_objective": str(objective),
        },
        "checks": "All incidence, covering, row-sum, norm, and primal identities passed using exact fractions.",
    }


if __name__ == "__main__":
    result = report()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "cover_total": result["cover_total"],
        "minimum_quadratic_objective": result["minimum_quadratic_objective"],
        "checks": result["checks"],
    }, indent=2))

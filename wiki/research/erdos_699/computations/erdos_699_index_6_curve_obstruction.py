"""Check an exact all-degree obstruction for the hard index-six profile.

Bézout and factorization turn these finite rational incidence checks into
a degree bound for every nonzero polynomial. No optimization solver or
finite degree search is needed to verify the certificate.
"""

from fractions import Fraction
import json
from pathlib import Path


DENOMINATOR = 16000
ROW_WEIGHTS = [
    [4960],
    [2880, 2880],
    [1121, 2718, 1121],
    [3635, 4365, 4365, 3635],
    [3404, 2283, 4626, 2283, 3404],
    [0, 3754, 4246, 4246, 3754, 0],
]
LINE_COVER = [
    ((1, 0, 0), 2480), ((0, 1, 0), 2480),
    ((1, 0, -1), 1359), ((0, 1, -1), 1359),
    ((1, 0, -2), 1851), ((0, 1, -2), 1851),
    ((1, 1, -3), 1155),
    ((1, 1, -4), 924),
    ((1, 1, -5), 2395),
]


def on_line(point, line):
    x, y = point
    a, b, c = line
    return a * x + b * y + c == 0


def report():
    weights = {
        (x, r - x): weight
        for r, row in enumerate(ROW_WEIGHTS)
        for x, weight in enumerate(row)
    }
    assert len(weights) == 21
    assert all(weight >= 0 for weight in weights.values())
    assert all(weights[(y, x)] == weight for (x, y), weight in weights.items())
    capacities = [Fraction(31, 100), Fraction(9, 25), Fraction(31, 100)] + [Fraction(1)] * 3
    row_sums = [
        Fraction(sum(weight for point, weight in weights.items() if sum(point) == r), DENOMINATOR)
        for r in range(6)
    ]
    assert row_sums == capacities

    cover_total = Fraction(sum(value for _, value in LINE_COVER), DENOMINATOR)
    assert cover_total == Fraction(7927, 8000) < 1
    points = []
    for point, weight in weights.items():
        covered = sum(value for line, value in LINE_COVER if on_line(point, line))
        assert weight <= covered
        points.append({
            "point": list(point), "weight_numerator": weight,
            "cover_numerator": covered, "slack_numerator": covered - weight,
        })

    lines = []
    for line, coefficient in LINE_COVER:
        incidence = sum(weight for point, weight in weights.items() if on_line(point, line))
        assert incidence <= DENOMINATOR
        expected = Fraction(7179, 8000) if line in ((1, 0, -2), (0, 1, -2)) else Fraction(1)
        assert Fraction(incidence, DENOMINATOR) == expected
        lines.append({
            "coefficients": list(line), "cover_numerator": coefficient,
            "own_incidence_numerator": incidence,
        })

    return {
        "scope": "An all-degree obstruction to strict weighted-degree gain at one index-six capacity profile; no bad triple or whole-index result is claimed.",
        "index": 6,
        "denominator": DENOMINATOR,
        "selected_positions_in_prime_order_2_3_5": [2, 1, 0],
        "cofactor_exponents": ["31/100", "9/25", "31/100"],
        "row_capacities": [str(value) for value in capacities],
        "row_weight_sums": [str(value) for value in row_sums],
        "point_weights": points,
        "line_cover": lines,
        "cover_total": str(cover_total),
        "universal_polynomial_inequality": "sum_P w_P ord_P(F) <= deg(F) for every nonzero F in C[X,Y]",
        "row_multiplicity_consequence": "deg(F) >= (31/100)m_0 + (9/25)m_1 + (31/100)m_2 + m_3 + m_4 + m_5",
        "checks": "All 21 point weights, nine covering-line incidences, row sums, and reflection identities passed using exact arithmetic.",
    }


if __name__ == "__main__":
    result = report()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "cover_total": result["cover_total"],
        "consequence": result["row_multiplicity_consequence"],
        "checks": result["checks"],
    }, indent=2))

"""Check an exact all-degree polynomial obstruction for the hard index-eight profile.

The proof uses only incidence inequalities, Bézout, and factorization.
No optimization solver, finite degree search, or polynomial rank assumption
is part of this certificate.
"""
from fractions import Fraction
import json
from pathlib import Path


HALF_POINTS = {
    (0, 0): 30,
    (0, 1): 15,
    (0, 2): 11, (1, 1): 8,
    (0, 3): 3, (1, 2): 12,
    (0, 4): 15, (1, 3): 20, (2, 2): 30,
    (0, 5): 16, (1, 4): 15, (2, 3): 19,
    (0, 6): 10, (1, 5): 13, (2, 4): 11, (3, 3): 32,
    (0, 7): 0, (1, 6): 17, (2, 5): 16, (3, 4): 17,
}
LINE_COVER = [
    ((1, 0, 0), 8), ((0, 1, 0), 8),
    ((1, 0, -1), 7), ((0, 1, -1), 7),
    ((1, 0, -2), 5), ((0, 1, -2), 5),
    ((1, 0, -3), 6), ((0, 1, -3), 6),
    ((1, 1, -4), 7), ((1, 1, -5), 8),
    ((1, 1, -6), 6), ((1, 1, -7), 11),
    ((1, -1, 0), 14),
]


def on_line(point, line):
    x, y = point
    a, b, c = line
    return a*x + b*y + c == 0


def main():
    points = [(x, r-x) for r in range(8) for x in range(r+1)]
    weights = {p: HALF_POINTS[tuple(sorted(p))] for p in points}
    capacities = [30]*4 + [100]*4
    assert [sum(w for p, w in weights.items() if sum(p) == r)
            for r in range(8)] == capacities
    cover_total = sum(value for _, value in LINE_COVER)
    assert cover_total == 98 < 100
    point_records = []
    for point, weight in weights.items():
        covered = sum(value for line, value in LINE_COVER if on_line(point, line))
        assert weight <= covered
        point_records.append({"point": list(point), "weight_numerator": weight,
                              "cover_numerator": covered})
    line_records = []
    for line, coefficient in LINE_COVER:
        incidence = sum(weight for point, weight in weights.items() if on_line(point, line))
        assert incidence <= 100
        line_records.append({"coefficients": list(line), "cover_numerator": coefficient,
                             "own_incidence_numerator": incidence})
    result = {
        "index": 8, "denominator": 100,
        "selected_positions_in_prime_order_2_3_5_7": [1, 3, 0, 2],
        "cofactor_exponents": ["3/10"]*4,
        "row_capacities": [str(Fraction(a, 100)) for a in capacities],
        "points": point_records, "line_cover": line_records,
        "cover_total": "49/50",
        "universal_polynomial_inequality": "sum_P w_P ord_P(F) <= deg(F) for every nonzero complex polynomial F",
        "row_multiplicity_consequence": "deg(F) >= 3/10*(m0+m1+m2+m3)+m4+m5+m6+m7",
        "noncover_irreducible_bound": "sum_P w_P mult_P(C) <= 49/50*deg(C)",
        "scope": "An obstruction to strict weighted-multiplicity versus total-degree gain at this cofactor profile; no bad triple or whole-index result is claimed.",
    }
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"checked_points": len(points), "checked_lines": len(LINE_COVER),
                      "cover_total": result["cover_total"],
                      "consequence": result["row_multiplicity_consequence"]}, indent=2))


if __name__ == "__main__":
    main()

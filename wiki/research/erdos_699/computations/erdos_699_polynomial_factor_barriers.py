#!/usr/bin/env python3
"""Check exact certificates limiting factor-plus-dimension interpolation.

The accompanying mathematical lemma uses Bezout and Cauchy--Schwarz. This
checker only uses rational arithmetic; no numerical optimizer is required.
These are limitations of a sufficient criterion, not candidate bad triples.
"""
from fractions import Fraction
from functools import reduce
from itertools import combinations
import json
from math import gcd
from pathlib import Path


def line_through(p, q):
    x, y = p
    u, v = q
    line = (y - v, u - x, x * v - y * u)
    divisor = reduce(gcd, line)
    line = tuple(c // divisor for c in line)
    if next(c for c in line if c) < 0:
        line = tuple(-c for c in line)
    return line


def check(record):
    i = record["i"]
    points = [tuple(p) for p in record["points"]]
    assert points == [(x, y) for x in range(i) for y in range(i - x)]
    weights = list(map(Fraction, record["weights"]))
    alpha = [Fraction(1)] * i
    for row, numerator in zip(record["prime_positions"], record["cofactor_numerators"]):
        alpha[row] = Fraction(numerator, record["cofactor_denominator"])
    assert len(weights) == len(points) and all(w >= 0 for w in weights)
    for t in range(i):
        assert sum(w for (x, y), w in zip(points, weights) if x + y == t) == alpha[t]

    # Every affine line with at least two grid points is represented. A line
    # through only one point has weight <= 1 because that point's row does.
    lines = {line_through(p, q) for p, q in combinations(points, 2)}
    for a, b, c in lines:
        assert sum(w for (x, y), w in zip(points, weights) if a * x + b * y + c == 0) <= 1
    cover_lines = record["cover_lines"]
    cover_weights = list(map(Fraction, record["cover_weights"]))
    assert len(cover_lines) == len(cover_weights)
    assert all(w >= 0 for w in cover_weights)
    cover_degree = sum(cover_weights)
    assert cover_degree == Fraction(record["cover_degree"]) < 1
    for (x, y), w in zip(points, weights):
        assert sum(v for (a, b, c), v in zip(cover_lines, cover_weights)
                   if a * x + b * y + c == 0) >= w
    norm = sum(w * w for w in weights)
    assert norm == Fraction(record["weight_norm_squared"]) < 1
    return {"i": i, "squared_weight_norm": float(norm),
            "line_cover_degree": float(cover_degree),
            "residual_squared_norm_lower_bound": float(1 / norm)}


def main():
    path = Path(__file__).with_suffix(".json")
    data = json.loads(path.read_text())
    print(json.dumps({"exact_checks_passed": True,
                      "records": [check(record) for record in data["records"]]}, indent=2))


if __name__ == "__main__":
    main()

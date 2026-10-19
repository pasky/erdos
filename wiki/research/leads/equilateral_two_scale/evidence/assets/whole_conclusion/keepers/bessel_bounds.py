#!/usr/bin/env python3
"""Exact finite inequalities in the E0173 spectral exclusion, 2026-10-17.

Subject: wiki/research/leads/equilateral_two_scale/spectral_exclusion.md,
Bessel Lemma 1, as frozen on 2026-10-17. This checks the nine displayed
rational enclosures and their scalar margins, not the analytic remainder,
zero-spacing, spectral-transfer, or whole-plane conclusions.

All mathematical inputs are the ROWS tuple below, transcribed from the frozen
excerpt. Evaluate each Taylor polynomial by Horner's rule over Fraction; no
floating-point Bessel library, repository import, or cached result is used.

Run with Python 3 and -I. The default check exits 0 on success. The deliberate
--negative-control replaces the first upper bound by -2601/10000, which is
strictly below the recomputed polynomial and must exit 1. Runtime is normally
a few seconds or less. There are no file outputs or background workers.
"""

import argparse
from fractions import Fraction
from math import factorial
import sys


ROWS = (
    (0, "3", "-261/1000", "-260/1000"),
    (0, "16/5", "-321/1000", "-320/1000"),
    (0, "19/5", "-4026/10000", "-4025/10000"),
    (1, "19/5", "128/10000", "129/10000"),
    (1, "4", "-67/1000", "-66/1000"),
    (0, "9/2", "-321/1000", "-320/1000"),
    (0, "24/5", "-241/1000", "-240/1000"),
    (0, "10", "-246/1000", "-245/1000"),
    (1, "10", "43/1000", "44/1000"),
)


def polynomial(nu, degree, q):
    """Return S_(nu,degree)(q) by descending Horner evaluation in q^2/4."""
    y = q * q / 4
    result = Fraction(0)
    for k in range(degree, -1, -1):
        coefficient = Fraction((-1) ** k, factorial(k) * factorial(k + nu))
        result = result * y + coefficient
    return (q / 2) ** nu * result


def failures(rows):
    errors = []
    for index, (nu, q_text, lower_text, upper_text) in enumerate(rows):
        q, lower, upper = map(Fraction, (q_text, lower_text, upper_text))
        if nu not in (0, 1) or not 0 < q <= 10 or not lower < upper:
            errors.append(f"row {index}: invalid stated input domain")
            continue
        low_sum, high_sum = polynomial(nu, 21, q), polynomial(nu, 20, q)
        if not lower < low_sum:
            errors.append(f"row {index}: lower < S_21 fails")
        if not low_sum < high_sum:
            errors.append(f"row {index}: S_21 < S_20 fails")
        if not high_sum < upper:
            errors.append(f"row {index}: S_20 < upper fails")
        # This is the first omitted-term ratio after S_20. Subsequent ratios
        # decrease because both denominator factors increase with the index.
        if not q * q / (4 * 22 * (22 + nu)) < 1:
            errors.append(f"row {index}: alternating-tail ratio is not below 1")

    y = Fraction(9, 4)
    p = 1 - y / 2 + y * y / 12 - y * y * y / 144
    if p != Fraction(223, 1024) or not p > 0:
        errors.append("small-argument polynomial endpoint fails")
    energy_a = Fraction(403, 1000) ** 2 - (
        Fraction(4026, 10000) ** 2 + Fraction(129, 10000) ** 2
    )
    energy_b = Fraction(1, 16) - (
        Fraction(246, 1000) ** 2 + Fraction(44, 1000) ** 2
    )
    if not energy_a > 0:
        errors.append("energy margin at 19/5 fails")
    if not energy_b > 0:
        errors.append("energy margin at 10 fails")
    if Fraction(261 + 403, 1000) != Fraction(83, 125):
        errors.append("global two-argument constant fails")
    if not Fraction(642, 1000) < Fraction(83, 125):
        errors.append("middle-interval margin fails")
    if Fraction(2, 3) - Fraction(83, 125) != Fraction(1, 375):
        errors.append("strict exclusion gap fails")
    return errors, energy_a, energy_b


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--negative-control", action="store_true")
    args = parser.parse_args()
    rows = list(ROWS)
    if args.negative_control:
        nu, q, lower, _ = rows[0]
        rows[0] = (nu, q, lower, "-2601/10000")
    errors, energy_a, energy_b = failures(rows)
    if errors:
        for error in errors:
            print("FAIL:", error)
        return 1
    print("Nine rational Bessel enclosures and scalar margins verified.")
    print(f"Energy margins: {energy_a}, {energy_b}; exclusion gap: 1/375.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

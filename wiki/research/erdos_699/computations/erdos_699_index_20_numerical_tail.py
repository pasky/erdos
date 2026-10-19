#!/usr/bin/env python3
"""A fully numerical upper endpoint for all bad triples with index 20.

Uses twelve numerically instantiated asymmetric cofactor inequalities,
exact collision-capacity enumeration, and a fixed symmetric jet rank.
No binomial rows or columns are enumerated.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import comb
from pathlib import Path

import erdos_699_index_13_interpolation_gcd as interpolation
from erdos_699_interpolation_extensions import minimal_vectors
from erdos_699_weighted_ramps import capacities


DIRECTORY = Path(__file__).parent
PRIMES = (2, 3, 5, 7, 11, 13, 17, 19)
H = (32, 30, 28, 26, 24, 21, 19, 16, 12, 8, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0)
M = (64, 63, 63, 63, 61, 59, 57, 56, 56, 54, 50, 46, 42, 39, 37, 34, 32, 30, 28, 26)
DEGREE = 118
PUBLISHED = (
    (2, 11, 1197, 1879), (3, 5, 2412, 3648), (5, 13, 1638, 3337),
    (7, 13, 987, 2080), (3, 19, 1162, 2104), (7, 19, 4299, 1374),
)
OPTIMIZED = (
    (3, 11, 3414, 4249), (5, 7, 3869, 2589), (5, 11, 2051, 2105),
    (11, 13, 1260, 652), (2, 17, 3643, 3505), (17, 19, 2442, 2146),
)


def sources():
    published = json.loads((DIRECTORY / "erdos_699_bft_asymmetric_pair_table.json").read_text())
    optimized = json.loads((DIRECTORY / "erdos_699_interpolation_numeric_pairs.json").read_text())
    rows = []
    for edge in PUBLISHED:
        record = next(row for row in published["published_gcd_pairs"]
                      if tuple(row["asymmetric_edge_scaled"]) == edge)
        assert record["verified"] and record["numerical_threshold"]["gap"] == 100
        rows.append({
            "kind": "published",
            "edge": list(edge),
            "input_threshold_power_of_ten": record["numerical_threshold"]["threshold_power_of_ten"],
        })
    for edge in OPTIMIZED:
        record = next(row for row in optimized if tuple(row["edge"]) == edge)
        assert record["threshold"]["gap"] == 100
        rows.append({
            "kind": "optimized",
            "edge": list(edge),
            "input_threshold_power_of_ten": record["threshold"]["threshold_power_of_ten"],
        })
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    source_rows = sources()
    vectors = minimal_vectors(PRIMES, PUBLISHED + OPTIMIZED)
    assert len(vectors) == 60 and all(a >= b for a, b in zip(M, M[1:]))
    total_degree = 2 * sum(H) + DEGREE + 1
    assert total_degree == 559
    worst = None
    configurations = 0
    for vector in vectors:
        for caps in capacities(vector):
            configurations += 1
            gain_scaled = 10000 * (sum(M) - total_degree) - sum(
                M[t] * cap for t, cap in enumerate(caps))
            candidate = (gain_scaled, vector, caps)
            if worst is None or candidate < worst:
                worst = candidate
    gain_scaled, vector, caps = worst
    gain = Fraction(gain_scaled, 10000)
    assert gain == Fraction(319, 1250)

    interpolation.DEGREE = DEGREE
    interpolation.PRIME = 65521
    interpolation.LINE_EXPONENTS = H
    interpolation.ROW_MULTIPLICITIES = M
    basis = interpolation.symmetric_basis()
    jets = interpolation.symmetric_jets()
    assert (len(jets), len(basis)) == (3599, 3600)
    matrix = interpolation.jet_matrix(basis, jets)
    rank = matrix.rank()
    assert rank == len(jets)

    # The same cofactor-minor norm estimate as in the general interpolation
    # note gives C < 10^(r(6+2D)), U < 10^7, and the following total constant.
    monomials = comb(DEGREE + 2, 2)
    generator_factor = 1 + (210 + 20 + 4) * monomials
    assert generator_factor < 10**7 and rank < 100000
    constant_exponent = (rank * (6 + 2 * DEGREE) + 1 + 8 * M[0]
                         + 2 * 19 * M[0] + 4 * sum(H) + 7)
    assert constant_exponent == 874790
    algebraic_cap = 4_000_000
    assert algebraic_cap * gain.numerator > constant_exponent * gain.denominator
    source_cap = max(row["input_threshold_power_of_ten"] for row in source_rows)
    assert source_cap == 27_027_658
    final_cap = max(algebraic_cap, source_cap + 1)
    assert final_cap == 27_027_659

    result = {
        "i": 20,
        "line_exponents": list(H),
        "row_multiplicities": list(M),
        "interpolation_degree": DEGREE,
        "nonvanishing_generator_degree": DEGREE + 1,
        "certificate_degree": total_degree,
        "primes": list(PRIMES),
        "sources": source_rows,
        "minimal_vector_count": len(vectors),
        "capacity_configurations_checked": configurations,
        "minimum_gain": str(gain),
        "worst_vector_scaled": list(vector),
        "worst_capacities_scaled": list(caps),
        "symmetric_jet_count": len(jets),
        "symmetric_monomial_count": len(basis),
        "modular_prime": 65521,
        "symmetric_rank": rank,
        "generator_coefficient_factor_bound": generator_factor,
        "constant_power_of_ten_bound": constant_exponent,
        "algebraic_tail_power_of_ten": algebraic_cap,
        "maximum_input_source_power_of_ten": source_cap,
        "full_numerical_tail_power_of_ten": final_cap,
        "conclusion": "Every bad triple with i=20 has n < 10^27027659",
    }
    if args.write:
        Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: result[key] for key in
                      ("i", "minimum_gain", "symmetric_rank",
                       "capacity_configurations_checked", "conclusion")}, indent=2))


if __name__ == "__main__":
    main()

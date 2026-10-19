#!/usr/bin/env python3
"""Fully numerical whole-index bound for Erdős 699 at i=18.

Verify the published-parameter asymmetric BFT sources, the exact modular
interpolation rank, every minimal cofactor vector and collision capacity,
and the integer coefficient comparison giving n < 10**700000.
No binomial rows or columns are enumerated.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import comb, factorial
from pathlib import Path

from erdos_699_index_18_effective import PRIMES, minimal_vectors
from erdos_699_index_18_interpolation_rank import (
    DEGREE, LINE_EXPONENTS, ROW_MULTIPLICITIES, report as rank_report,
)
from erdos_699_index_18_pair_sources import report as source_report
from erdos_699_prime_pair_savings import EXPLICIT_EDGES, SCALE
from erdos_699_weighted_ramps import capacities


INDEX = 18
ROW_CAP = 700_000
CERTIFICATE = Path(__file__).with_suffix(".json")


def report():
    sources = source_report()
    rank = rank_report()
    assert PRIMES == (2, 3, 5, 7, 11, 13, 17)
    edges = [(p, q, w, w) for p, q, w in EXPLICIT_EDGES]
    edges.extend(tuple(edge) for edge in sources["asymmetric_edges_scaled"])
    vectors = minimal_vectors(edges)
    weights = ROW_MULTIPLICITIES
    h = LINE_EXPONENTS
    total_degree = DEGREE + 1 + 2 * sum(h)
    assert total_degree == 589 and sum(weights) == 998
    worst = None
    configurations = 0
    for vector in vectors:
        for caps in capacities(vector):
            configurations += 1
            gain_scaled = SCALE * (sum(weights) - total_degree) - sum(
                weight * capacity for weight, capacity in zip(weights, caps)
            )
            item = gain_scaled, vector, caps
            if worst is None or item < worst:
                worst = item
    gain_scaled, worst_vector, worst_caps = worst
    gain = Fraction(gain_scaled, SCALE)
    assert (len(vectors), configurations, gain) == (123, 11932, Fraction(5241, 5000))

    # C = r! * (2*18**D)**r bounds every relevant maximal minor and
    # adjugate coefficient.  These small exact powers bound log_10 C.
    r = rank["symmetric_rank"]
    assert r == 4355 and r < 10**4
    assert 2**500 < 10**151 and 18**500 < 10**628
    assert r * (2000 + 151 + 628 * DEGREE) < 500 * 730_000
    monomials = comb(DEGREE + 2, 2)
    support = INDEX * (INDEX + 1) // 2
    generator_factor = 1 + (support + INDEX + 4) * monomials
    assert generator_factor < 10**7
    assert INDEX ** (2 * sum(h)) < 10**576
    assert factorial(INDEX - 1) ** weights[0] < 10**1065
    assert 2 ** (1 + len(PRIMES) * weights[0]) < 10**151
    right_side_exponent = 730_000 + 7 + 576 + 1065 + 151
    assert right_side_exponent == 731_799
    assert ROW_CAP * gain.numerator > 731_800 * gain.denominator

    moment = sum(t * weight for t, weight in enumerate(weights))
    elementary_threshold = 1000 * (
        moment + weights[0] * len(PRIMES) * (INDEX - 1)
    )
    assert moment == 7189 and elementary_threshold < 10**8
    assert sources["common_row_threshold_power_of_ten"] <= 1733 < ROW_CAP
    return {
        "scope": "Whole-index numerical bound; no binomial rows enumerated.",
        "i": INDEX,
        "primes": list(PRIMES),
        "line_exponents": list(h),
        "row_multiplicities": list(weights),
        "interpolation_degree": DEGREE,
        "generator_degree": DEGREE + 1,
        "total_polynomial_degree": total_degree,
        "modular_prime": rank["prime"],
        "symmetric_jet_count": rank["symmetric_jet_count"],
        "symmetric_monomial_count": rank["symmetric_monomial_count"],
        "symmetric_rank": r,
        "edges_scaled": [list(edge) for edge in edges],
        "weight_denominator": SCALE,
        "minimal_vectors_scaled": [list(vector) for vector in vectors],
        "minimal_vector_count": len(vectors),
        "collision_capacity_lists_checked": configurations,
        "minimum_gain": str(gain),
        "worst_vector_scaled": list(worst_vector),
        "worst_capacities_scaled": list(worst_caps),
        "minor_constant_power_of_ten": 730_000,
        "generator_factor_bound": generator_factor,
        "comparison_constant_power_of_ten": 731_800,
        "elementary_threshold": elementary_threshold,
        "common_source_row_threshold_power_of_ten": sources["common_row_threshold_power_of_ten"],
        "row_bound_power_of_ten": ROW_CAP,
        "exclusive_row_bound": "n < 10^700000",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--regenerate", action="store_true")
    args = parser.parse_args()
    result = report()
    if args.regenerate:
        CERTIFICATE.write_text(json.dumps(result, indent=2) + "\n")
    else:
        assert json.loads(CERTIFICATE.read_text()) == result
    print(json.dumps({key: result[key] for key in (
        "i", "symmetric_rank", "minimal_vector_count",
        "collision_capacity_lists_checked", "minimum_gain", "exclusive_row_bound",
    )}, indent=2))


if __name__ == "__main__":
    main()

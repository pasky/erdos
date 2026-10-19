#!/usr/bin/env python3
"""A fully numerical tail for index15 using its retained interpolation map.

Only analytic parameter choices and finite cofactor vectors are checked.
No binomial rows or columns are enumerated.
"""

from fractions import Fraction
import json
from pathlib import Path

from erdos_699_bft_asymmetric import asymmetric_bound
from erdos_699_bft_gcd_bounds import gcd_exponent_lower
from erdos_699_bft_pair_extension import rational
from erdos_699_index_13_effective import asymmetric_vectors
from erdos_699_prime_pair_savings import EXPLICIT_EDGES, SCALE
from erdos_699_weighted_ramps import capacities


PRIMES = (2, 3, 5, 7, 11, 13)
PUBLISHED = ((2, 7, 2734, 3201), (2, 11, 1197, 1879),
             (5, 7, 3613, 2277), (7, 13, 987, 2080))
# pair, oriented seed P,Q,a,b,c,d, sorted-prime endpoint targets.
NEW_PARAMETERS = (
    ((2, 5), (128, 125, 1, 1, 53, 43), (2638, 2674)),
    ((3, 11), (243, 121, 1, 2, 34, 25), (3414, 4249)),
    ((11, 13), (13, 11, 1, 1, 69, 49), (1260, 652)),
)
M0 = 100_000
TERMS = 4000


def is_power(value, prime):
    while value % prime == 0:
        value //= prime
    return value == 1


def report():
    directory = Path(__file__).parent
    published = json.loads((directory / "erdos_699_bft_asymmetric_pair_table.json").read_text())
    source_rows = []
    for edge in PUBLISHED:
        row = next(row for row in published["published_gcd_pairs"]
                   if tuple(row["asymmetric_edge_scaled"]) == edge)
        assert row["verified"]
        source_rows.append({
            "kind": "retained published-GCD certificate",
            "edge_scaled": list(edge),
            "threshold_power_of_ten": row["numerical_threshold"]["threshold_power_of_ten"],
        })
    for pair, seed, endpoints in NEW_PARAMETERS:
        gcd_bound = gcd_exponent_lower(seed[-2], seed[-1], terms=TERMS, m0=M0)
        targets = [Fraction(value, SCALE) for value in endpoints]
        if not is_power(seed[0], pair[0]):
            assert is_power(seed[0], pair[1])
            targets.reverse()
        bound = asymmetric_bound(*seed, rational(Fraction(gcd_bound["ell_lower"])),
                                 M0, 100, *targets)
        source_rows.append({
            "kind": "new finite-prime-interval GCD certificate",
            "edge_scaled": list(pair + endpoints),
            "seed": list(seed), "gcd_bound": gcd_bound,
            "asymmetric_bound": bound,
            "threshold_power_of_ten": bound["threshold_power_of_ten"],
        })

    edges = EXPLICIT_EDGES + tuple(tuple(row["edge_scaled"]) for row in source_rows)
    vectors = asymmetric_vectors(PRIMES, edges)
    family_data = json.loads((directory / "erdos_699_interpolation_extensions.json").read_text())
    family = next(row for row in family_data["certificates"] if row["i"] == 15)
    assert (family["interpolation_degree"], family["symmetric_rank"],
            family["symmetric_jet_count"], family["certificate_degree"]) == (257, 16768, 16768, 962)
    weights = family["row_multiplicities"]
    assert all(weights[t] >= weights[t + 1] for t in range(14))
    configurations = 0
    worst = None
    for vector in vectors:
        assert all(0 <= value < SCALE // 2 for value in vector)
        for cap in capacities(vector):
            configurations += 1
            gain = sum(weights) - 962 - sum(
                Fraction(value, SCALE) * weights[t] for t, value in enumerate(cap))
            row = (gain, vector, cap)
            if worst is None or row < worst:
                worst = row
    gain, vector, cap = worst
    assert gain == Fraction(7993, 10000)
    constant_power = family["constant_power_of_ten_bound"]
    assert constant_power == 8_725_502
    algebraic_power = constant_power // gain + 1
    source_power = max(row["threshold_power_of_ten"] for row in source_rows) + 1
    complete_power = max(algebraic_power, source_power)
    assert complete_power == 15_170_264
    assert complete_power * gain > constant_power
    return {
        "source": "BFT Section7 asymmetric inequalities and finite-prime-interval GCD bounds",
        "scope": "Uniform numerical tail, no binomial rows enumerated.",
        "i": 15, "source_certificates": source_rows,
        "minimal_vector_count": len(vectors),
        "capacity_configurations_checked": configurations,
        "minimum_gain": str(gain),
        "worst_vector_scaled": list(vector),
        "worst_capacities_scaled": list(cap),
        "constant_power_of_ten_bound": constant_power,
        "algebraic_power_of_ten": algebraic_power,
        "source_power_of_ten_including_row_shift": source_power,
        "complete_row_bound_power_of_ten": complete_power,
    }


if __name__ == "__main__":
    result = report()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: result[key] for key in (
        "i", "minimum_gain", "algebraic_power_of_ten",
        "source_power_of_ten_including_row_shift", "complete_row_bound_power_of_ten")}, indent=2))

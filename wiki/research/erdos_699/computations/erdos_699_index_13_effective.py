#!/usr/bin/env python3
"""Exact arithmetic and coefficient-height bounds for all of index 13.

The separate interpolation checker verifies the required full row rank
over F_65521. This script checks all prime-pair vectors, collision patterns,
monotone multiplicities, and the explicit final row bound.
"""

from fractions import Fraction
import json
from math import factorial
from pathlib import Path

from erdos_699_prime_pair_savings import EXPLICIT_EDGES, SCALE
from erdos_699_weighted_ramps import capacities


PRIMES = (2, 3, 5, 7, 11)
H = (57, 54, 45, 39, 32, 24, 13, 3, 0, 0, 0, 0, 0)
M = (114, 111, 111, 103, 99, 99, 89, 78, 70, 63, 57, 51, 46)
EXTRA_EDGE = (5, 7, 3500, 2200)


def asymmetric_vectors(primes, edges):
    positions = {p: j for j, p in enumerate(primes)}
    vectors = [(0,) * len(primes)]
    used = []
    for edge in edges:
        p, q = edge[:2]
        if p not in positions or q not in positions:
            continue
        a, b = positions[p], positions[q]
        wa, wb = edge[2], edge[3] if len(edge) == 4 else edge[2]
        used.append((a, b, wa, wb))
        candidates = set()
        for vector in vectors:
            if vector[a] >= wa or vector[b] >= wb:
                candidates.add(vector)
            else:
                for target, weight in ((a, wa), (b, wb)):
                    extension = list(vector)
                    extension[target] = weight
                    candidates.add(tuple(extension))
        vectors = []
        for vector in sorted(candidates, key=lambda v: (sum(v), v)):
            if not any(all(a <= b for a, b in zip(old, vector))
                       for old in vectors):
                vectors.append(vector)
        assert all(any(all(a <= b for a, b in zip(old, vector))
                       for old in vectors) for vector in candidates)
    assert all(vector[a] >= wa or vector[b] >= wb
               for vector in vectors for a, b, wa, wb in used)
    return vectors


def report():
    directory = Path(__file__).parent
    jet = json.loads((directory / "erdos_699_index_13_interpolation_gcd.json").read_text())
    assert jet["degree"] == 106
    assert jet["line_exponents"] == list(H)
    assert jet["row_multiplicities"] == list(M)
    assert (jet["symmetric_jet_count"], jet["symmetric_monomial_count"],
            jet["symmetric_rank"]) == (2911, 2916, 2911)
    assert all(M[t] >= M[t + 1] for t in range(12))
    assert 2 * sum(H) == 534
    degree = 534 + 106 + 1
    vectors = asymmetric_vectors(PRIMES, EXPLICIT_EDGES + (EXTRA_EDGE,))
    assert len(vectors) == 18
    worst = None
    configurations = 0
    for vector in vectors:
        for cap in capacities(vector):
            configurations += 1
            gain = sum(M) - degree - sum(
                Fraction(c, SCALE) * M[t] for t, c in enumerate(cap))
            record = (gain, vector, cap)
            if worst is None or record < worst:
                worst = record
    gain, vector, cap = worst
    assert gain == Fraction(1287, 200)

    source = json.loads((directory / "erdos_699_bft_asymmetric.json").read_text())
    pair = next(row for row in source["pairs"] if row["pair"] == [5, 7]
                and list(map(Fraction, row["targets"])) == [Fraction(35, 100), Fraction(22, 100)])
    assert pair["gap"] >= 12 and pair["threshold_power_of_ten"] == 1731

    rank, residual_degree = 2911, 106
    # These exact integer comparisons bound log10(2911), log10(2), log10(13).
    assert rank ** 2 < 10 ** 7
    assert 2 ** 500 < 10 ** 151
    assert 13 ** 200 < 10 ** 223
    determinant_exponent = rank * (
        Fraction(7, 2) + Fraction(151, 500) + residual_degree * Fraction(223, 200))
    assert determinant_exponent < 355119
    assert Fraction(534 * 223, 200) < 596
    assert Fraction(114 * 223, 200) < 128
    assert factorial(12) < 10 ** 9
    # Norms of the integer jet generators are <10^6 times the minor bound.
    assert 22 * 6000 < 10 ** 6
    assert 1 + 49 * 6000 < 10 ** 6
    evaluation_exponent = 355119 + 6 + 596 + 128 + 114 * 9 + 1
    assert evaluation_exponent == 356876
    cap_power = 56000
    assert cap_power * gain > evaluation_exponent
    moment = sum(t * multiplicity for t, multiplicity in enumerate(M))
    elementary_threshold = 1000 * (moment + max(M) * len(PRIMES) * 12)
    assert elementary_threshold < 10 ** 8
    assert cap_power > 1731 + 1 and cap_power > 8

    return {
        "scope": "Finite exact polynomial certificate; no binomial rows searched.",
        "i": 13, "degree": degree,
        "symmetric_jet_matrix": [2911, 2916],
        "modular_rank": 2911, "modulus": 65521,
        "minimum_gain": str(gain),
        "minimal_vector_count": len(vectors),
        "capacity_configurations_checked": configurations,
        "worst_vector_scaled": list(vector),
        "worst_capacities_scaled": list(cap),
        "source_asymmetric_edge_scaled": list(EXTRA_EDGE),
        "source_threshold_power_of_ten": 1731,
        "elementary_threshold": elementary_threshold,
        "evaluation_constant_less_than_power_of_ten": evaluation_exponent,
        "complete_row_bound_power_of_ten": cap_power,
    }


if __name__ == "__main__":
    result = report()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))

#!/usr/bin/env python3
"""Exact interpolation certificates making indices 15 and 20 effective.

The finite enumeration concerns cofactor exponents, collision capacities,
and polynomial jets. No binomial rows or columns are enumerated.

Requires NumPy, python-flint, and the dependencies of the retained BFT
checkers. The index-15 modular rank calculation takes about three minutes
on the machine used to produce this certificate. Use --arithmetic-only
to check the finite inequalities without repeating that rank calculation.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import comb, isqrt
from pathlib import Path

from mpmath import iv

import erdos_699_index_13_interpolation_gcd as interpolation
from erdos_699_bft_asymmetric import asymmetric_bound
from erdos_699_bft_more_pairs import NEW_EDGES
from erdos_699_bft_pair_extension import rational
from erdos_699_weighted_ramps import EDGES, PRIMES, SCALE, capacities


DATA = {
    15: {
        "h": (69, 63, 57, 51, 43, 34, 24, 11, 0, 0, 0, 0, 0, 0, 0),
        "m": (139, 139, 138, 137, 127, 127, 127, 119, 106, 95, 87, 79, 73, 68, 63),
        "degree": 257,
        "prime": 251,
        "rank": 16768,
        "columns": 16770,
        "gain": Fraction(43, 5000),
        "algebraic_power_of_ten": 1_100_000_000,
    },
    20: {
        "h": (34, 32, 30, 27, 25, 22, 19, 16, 13, 9, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0),
        "m": (67, 65, 65, 65, 62, 60, 58, 57, 57, 54, 50, 46, 42, 39, 37, 34, 32, 30, 28, 26),
        "degree": 96,
        "prime": 65521,
        "rank": 2399,
        "columns": 2401,
        "gain": Fraction(713, 5000),
        "algebraic_power_of_ten": 4_000_000,
    },
}

ASYMMETRIC_EDGES = ((5, 7, 3613, 2277), (7, 13, 987, 2080))
OUTPUT = Path(__file__).with_suffix(".json")


def minimal_vectors(primes, edges=None):
    """Exact minimal witnesses for symmetric and asymmetric disjunctions."""
    positions = {prime: at for at, prime in enumerate(primes)}
    vectors = [(0,) * len(primes)]
    used = []
    if edges is None:
        edges = EDGES + NEW_EDGES + ASYMMETRIC_EDGES
    for edge in edges:
        p, q = edge[:2]
        if p not in positions or q not in positions:
            continue
        left, right = positions[p], positions[q]
        a, b = edge[2], edge[3] if len(edge) == 4 else edge[2]
        used.append((left, right, a, b))
        extensions = set()
        for vector in vectors:
            if vector[left] >= a or vector[right] >= b:
                extensions.add(vector)
            else:
                for at, weight in ((left, a), (right, b)):
                    new = list(vector)
                    new[at] = weight
                    extensions.add(tuple(new))
        vectors = []
        for vector in sorted(extensions, key=lambda value: (sum(value), value)):
            if not any(all(a <= b for a, b in zip(old, vector)) for old in vectors):
                vectors.append(vector)
        assert all(any(all(a <= b for a, b in zip(old, value)) for old in vectors)
                   for value in extensions)
    assert all(vector[a] >= x or vector[b] >= y
               for vector in vectors for a, b, x, y in used)
    assert all(0 <= value < SCALE // 2 for vector in vectors for value in vector)
    return vectors


def asymmetric_thresholds():
    choices = (
        ((5, 7), (25, 49, 2, 1, 8, 5), "1.5407", 53, ".3613", ".2277"),
        ((7, 13), (343, 169, 1, 2, 7, 5), "1.4135", 74, ".0987", ".2080"),
    )
    rows = []
    for pair, seed, l1, m0, target_p, target_q in choices:
        result = asymmetric_bound(*seed, iv.log(rational(l1)), m0, 100,
                                  target_p, target_q)
        rows.append({"pair": list(pair), "L1": l1, **result})
    return rows


def certify(index, check_rank=True):
    data = DATA[index]
    h, m, degree = data["h"], data["m"], data["degree"]
    assert len(h) == len(m) == index
    assert all(a >= b for a, b in zip(m, m[1:]))
    assert all(type(value) is int and value >= 0 for value in h + m)
    primes = tuple(prime for prime in PRIMES if prime < index)
    vectors = minimal_vectors(primes)
    certificate_degree = 2 * sum(h) + degree + 1
    configurations = 0
    worst = None
    for vector in vectors:
        for caps in capacities(vector):
            configurations += 1
            gain_scaled = SCALE * (sum(m) - certificate_degree) - sum(
                m[at] * cap for at, cap in enumerate(caps))
            record = (gain_scaled, vector, caps)
            if worst is None or record < worst:
                worst = record
    gain_scaled, vector, caps = worst
    gain = Fraction(gain_scaled, SCALE)
    assert gain == data["gain"] and gain > 0

    interpolation.DEGREE = degree
    interpolation.PRIME = data["prime"]
    interpolation.LINE_EXPONENTS = h
    interpolation.ROW_MULTIPLICITIES = m
    basis = interpolation.symmetric_basis()
    jets = interpolation.symmetric_jets()
    assert len(basis) == data["columns"] and len(jets) == data["rank"]
    prime = data["prime"]
    assert prime > 1 and all(prime % p for p in range(2, isqrt(prime) + 1))
    if check_rank:
        print(f"Checking index {index}: {len(jets)} x {len(basis)} over F_{prime}",
              flush=True)
        matrix = interpolation.jet_matrix(basis, jets)
        assert matrix.rank() == len(jets)

    # A coarse, completely integer certificate for the algebraic part of
    # the row bound; the effective symmetric BFT thresholds remain separate.
    rank = len(jets)
    monomials = comb(degree + 2, 2)
    support_bound = index * (index + 1) // 2
    generator_factor = 1 + (support_bound + index + 4) * monomials
    assert index < 100 and rank < 100_000 and generator_factor < 10**7
    constant_power = (rank * (6 + 2 * degree)
                      + 1 + len(primes) * m[0]
                      + 2 * (index - 1) * m[0]
                      + 4 * sum(h) + 7)
    cap = data["algebraic_power_of_ten"]
    assert cap * gain.numerator > constant_power * gain.denominator
    moment = sum(t * value for t, value in enumerate(m))
    assert cap >= 10 and 2 * max(moment, index - 1) < 10**10

    return {
        "i": index,
        "line_exponents": list(h),
        "row_multiplicities": list(m),
        "interpolation_degree": degree,
        "nonvanishing_generator_degree": degree + 1,
        "line_factor_degree": 2 * sum(h),
        "certificate_degree": certificate_degree,
        "minimal_vector_count": len(vectors),
        "capacity_configurations_checked": configurations,
        "minimum_gain": str(gain),
        "worst_vector_scaled": list(vector),
        "worst_capacities_scaled": list(caps),
        "modular_prime": prime,
        "symmetric_jet_count": len(jets),
        "symmetric_monomial_count": len(basis),
        "symmetric_rank": len(jets),
        "full_jet_count": sum(comb(interpolation.residual(x, y) + 1, 2)
                              for x in range(index) for y in range(index - x)),
        "generator_coefficient_factor_bound": generator_factor,
        "constant_power_of_ten_bound": constant_power,
        "algebraic_power_of_ten": cap,
        "source_threshold": "Maximum of effective symmetric BFT thresholds at gap 100",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("indices", nargs="*", type=int, choices=tuple(DATA))
    parser.add_argument("--arithmetic-only", action="store_true")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    assert not (args.write and args.arithmetic_only)
    indices = args.indices or list(DATA)
    pairs = asymmetric_thresholds()
    rows = [certify(index, check_rank=not args.arithmetic_only) for index in indices]
    for row in rows:
        assert row["algebraic_power_of_ten"] > max(
            pair["threshold_power_of_ten"] for pair in pairs) + 1
    output = {"asymmetric_thresholds": pairs, "certificates": rows}
    if args.write:
        assert set(indices) == set(DATA), "The retained artifact contains both indices"
        OUTPUT.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({
        "rank_checked": not args.arithmetic_only,
        "certificates": [{key: row[key] for key in
                          ("i", "certificate_degree", "minimum_gain", "symmetric_rank",
                           "algebraic_power_of_ten")} for row in rows],
    }, indent=2))


if __name__ == "__main__":
    main()

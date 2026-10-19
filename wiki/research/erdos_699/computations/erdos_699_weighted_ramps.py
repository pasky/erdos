#!/usr/bin/env python3
"""Exact weighted certificates, including all collisions of maximal positions.

This enumerates finite exponent vectors and subsets of small primes, not
rows or columns of Pascal's triangle. Source thresholds remain separate
from the algebraic powers of ten computed here.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import log
from pathlib import Path

from erdos_699_prime_pair_savings import EDGES, EXPLICIT_EDGES, SCALE


PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23)
INDEX_21_EDGES = ((2, 17, 3560), (17, 19, 2176))
INDEX_24_EDGES = ((17, 19, 2100), (11, 23, 1450))


def minimal_vectors(primes, edges):
    """Exact minimal vectors of max(v_p,v_q) >= edge weight, by induction."""
    positions = {p: j for j, p in enumerate(primes)}
    vectors = [(0,) * len(primes)]
    used_edges = []
    for p, q, weight in edges:
        if p not in positions or q not in positions:
            continue
        a, b = positions[p], positions[q]
        used_edges.append((a, b, weight))
        extensions = set()
        for vector in vectors:
            if max(vector[a], vector[b]) >= weight:
                extensions.add(vector)
            else:
                for target in (a, b):
                    new = list(vector)
                    new[target] = weight
                    extensions.add(tuple(new))
        vectors = []
        for vector in sorted(extensions, key=lambda v: (sum(v), v)):
            if not any(all(a <= b for a, b in zip(old, vector))
                       for old in vectors):
                vectors.append(vector)
        assert all(any(all(a <= b for a, b in zip(old, vector))
                       for old in vectors) for vector in extensions)
    assert all(max(vector[a], vector[b]) >= weight
               for vector in vectors for a, b, weight in used_edges)
    assert all(0 <= entry < SCALE // 2 for v in vectors for entry in v)
    return vectors


def capacities(vector):
    """Worst row capacities for every possible set of singleton positions.

    A position occupied by at least two primes has capacity one. For a
    fixed set of singletons, maximizing the number of other occupied
    positions is worst; it is floor(number of other primes / 2).
    """
    size = len(vector)
    result = set()
    for mask in range(1 << size):
        singles = [SCALE - vector[p] for p in range(size) if mask >> p & 1]
        other_count = size - len(singles)
        if other_count == 1:
            continue
        result.add(tuple(sorted([SCALE] * (other_count // 2) + singles,
                                reverse=True)))
    return sorted(result)


def valuation(value, prime):
    assert value > 0
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def off_maximum_constant(index, weights, primes):
    factors = []
    value = 1
    for prime in primes:
        exponents = [sum(weights[t] * valuation(abs(t - r), prime)
                         for t in range(index) if t != r)
                     for r in range(index)]
        maximum = max(exponents)
        value *= prime ** maximum
        factors.append({"prime": prime, "exponent": maximum,
                        "maximizing_positions": [r for r, e in enumerate(exponents)
                                                 if e == maximum]})
    return value, factors


def exact_power_of_ten(constant, exponent, lower_threshold):
    """Floating point only suggests a cap; integer powers certify it."""
    numerator, denominator = constant.numerator, constant.denominator
    power = max(1, int((log(numerator) - log(denominator)) /
                       (float(exponent) * log(10))) + 1)
    n_power, c_power = exponent.numerator, exponent.denominator
    right = numerator ** c_power
    denominator_power = denominator ** c_power

    def valid(candidate):
        return (10 ** candidate >= lower_threshold and
                10 ** (candidate * n_power) * denominator_power > right)

    while not valid(power):
        power += 1
    while power > 1 and valid(power - 1):
        power -= 1
    assert valid(power)
    return power


def certify(index, k, edges, threshold_description):
    primes = tuple(p for p in PRIMES if p < index)
    size = len(primes)
    assert 1 <= k <= index and 2 * k >= index - 1
    weights = [2 * k - t for t in range(index)]
    degree = k * (k + 1)
    total = sum(weights)
    moment = sum(t * weight for t, weight in enumerate(weights))
    vectors = minimal_vectors(primes, edges)
    worst = None
    configurations = 0
    for vector in vectors:
        for caps in capacities(vector):
            configurations += 1
            gain_scaled = SCALE * (total - degree) - sum(
                (2 * k - r) * cap for r, cap in enumerate(caps))
            record = (gain_scaled, vector, caps)
            if worst is None or record < worst:
                worst = record
    gain_scaled, vector, caps = worst
    gain = Fraction(gain_scaled, SCALE)
    assert gain > 0
    off_maximum, factors = off_maximum_constant(index, weights, primes)
    is_prime = all(index % p for p in primes if p * p <= index)
    rough_denominator = index if is_prime else 1
    constant = Fraction(1000 * rough_denominator ** (2 * k) * off_maximum,
                        999 * 2 ** degree)
    lower_threshold = 1000 * (moment + 2 * k * size * (index - 1))
    power = exact_power_of_ten(constant, gain, lower_threshold)
    return {
        "i": index, "k": k, "primes": list(primes),
        "degree": degree, "total_multiplicity": total,
        "weighted_moment": moment,
        "minimal_vector_count": len(vectors),
        "capacity_configurations_checked": configurations,
        "minimum_gain": str(gain),
        "worst_vector_scaled": [exact_scalar(v) for v in vector],
        "worst_row_capacities_scaled": [exact_scalar(v) for v in caps],
        "off_maximum_factors": factors,
        "rough_denominator": rough_denominator,
        "elementary_threshold": lower_threshold,
        "algebraic_cap_power_of_ten": power,
        "source_threshold": threshold_description,
        "full_bound": f"max(10^{power}, {threshold_description})",
    }


def exact_scalar(value):
    value = Fraction(value)
    return value.numerator if value.denominator == 1 else str(value)


def numerical_records():
    """Use only targets and thresholds retained by the source checkers."""
    directory = Path(__file__).parent
    gcd_source = json.loads((directory / "erdos_699_bft_gcd_bounds.json").read_text())
    new_source = json.loads((directory / "erdos_699_bft_explicit_thresholds.json").read_text())

    def select(pair, target):
        return next(row for row in new_source
                    if tuple(row["pair"]) == pair
                    and Fraction(row["target"]) == Fraction(target))

    def numerical(index, k, rows, published_base, route):
        edges = EXPLICIT_EDGES if published_base else ()
        edges += tuple((*row["pair"], Fraction(row["target"]) * SCALE) for row in rows)
        cap = 7 if published_base else 0
        for row in rows:
            if row.get("row_threshold_maximum_position", -1) >= index - 1:
                cap = max(cap, row["row_threshold_power_of_ten"])
            else:
                # 10**(K+1) - (i-1) > 10**K for these indices and K >= 1.
                assert row["threshold_power_of_ten"] >= 1 and index < 90
                cap = max(cap, row["threshold_power_of_ten"] + 1)
        result = certify(index, k, edges, f"10^{cap}")
        result["route"] = route
        result["numerical_source_cap_power_of_ten"] = cap
        result["full_numerical_cap_power_of_ten"] = max(
            cap, result["algebraic_cap_power_of_ten"])
        result["full_bound"] = f"10^{result['full_numerical_cap_power_of_ten']}"
        return result

    coarse_2_17 = select((2, 17), "0.3259")
    coarse_17_19 = select((17, 19), "0.1855")
    coarse_11_23 = select((11, 23), "0.1068")
    results = [
        numerical(19, 12, [coarse_2_17], True, "one new prime pair"),
        numerical(22, 15, [coarse_17_19], True, "one new prime pair"),
        numerical(25, 17, [coarse_17_19], True, "one new prime pair"),
        numerical(24, 16, [coarse_2_17, coarse_17_19, coarse_11_23], True,
                  "three new prime pairs"),
    ]
    base = gcd_source["proposition_5_1_pairs"]
    improved = gcd_source["improved_pairs"]
    results.append(numerical(
        21, 14, base + improved + [select((2, 17), "0.3379"),
                                  select((17, 19), "0.1925")],
        False, "improved GCD bounds and two new prime pairs"))
    results.append(numerical(16, 10, gcd_source["index_16_pairs"], True,
                             "two targeted explicit improvements"))
    return results


def report():
    records = [certify(i, k, EDGES, "X_BFT(33) + 33")
               for i, k in ((16, 11), (19, 13), (22, 15), (25, 17))]
    records.append(certify(24, 16, EDGES + INDEX_24_EDGES, "X_24 + 23"))
    records.append(certify(21, 14, EDGES + INDEX_21_EDGES, "X_21 + 20"))
    expected = {16: Fraction(693, 500), 19: Fraction(711, 500),
                22: Fraction(729, 500), 25: Fraction(747, 500),
                24: Fraction(21893, 10000), 21: Fraction(7683, 5000)}
    assert all(Fraction(row["minimum_gain"]) == expected[row["i"]]
               for row in records)
    return {
        "scope": "Exact finite weighted certificates; no binomial rows searched.",
        "weight_denominator": SCALE,
        "index_21_additional_edges": [list(edge) for edge in INDEX_21_EDGES],
        "index_24_additional_edges": [list(edge) for edge in INDEX_24_EDGES],
        "records": records,
        "numerical_records": numerical_records(),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_suffix(".json"))
    args = parser.parse_args()
    result = report()
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps([{key: row[key] for key in
                       ("i", "minimum_gain", "algebraic_cap_power_of_ten", "full_bound")}
                      for row in result["records"] + result["numerical_records"]], indent=2))

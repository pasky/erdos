"""Further BFT parameter certificates and exact cofactor exponent bounds.

This checks fixed analytic parameters and finite max-constraint systems,
not rows of Pascal's triangle. The resulting algebraic bounds still require
the effective thresholds in BFT Theorem 2.2; those are not evaluated here.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import lcm
from pathlib import Path

from erdos_699_bft_pair_extension import certify
from erdos_699_prime_pair_savings import EDGES, EXPLICIT_EDGES, SCALE, rough_exponent


# p, q, weight; oriented seed P,Q,a,b; s=c/d; epsilon denominator.
PARAMETERS = (
    (2, 11, 1399, 32768, 14641, 21, 47, 13, 6, 100_000),
    (3, 5, 2543, 625, 2187, 7, 2, 13, 8, 100_000),
    (2, 17, 3560, 17, 16, 1, 1, 34, 25, 100_000),
    (3, 17, 1190, 9, 17, 2, 1, 31, 18, 100_000),
    (5, 17, 93, 17, 25, 3, 2, 57, 26, 100_000),
    (3, 19, 1268, 729, 361, 1, 2, 35, 27, 100_000),
    (7, 19, 1588, 343, 6859, 20, 1, 67, 40, 100_000),
    (11, 19, 2077, 121, 361, 3, 1, 53, 37, 100_000),
    (17, 19, 2176, 289, 361, 5, 4, 32, 17, 1_000_000),
    (2, 23, 245, 529, 512, 1, 1, 45, 38, 100_000),
    (5, 23, 2144, 25, 23, 1, 1, 41, 31, 100_000),
    (11, 23, 1478, 23, 11, 1, 2, 5, 3, 100_000),
)
NEW_EDGES = tuple((p, q, weight) for p, q, weight, *_ in PARAMETERS)
PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23)


def minimal_vectors(primes, edges):
    """Keep all componentwise minimal witnesses after each max constraint."""
    positions = {p: k for k, p in enumerate(primes)}
    vectors = [tuple(0 for _ in primes)]
    for p, q, weight in edges:
        if p not in positions or q not in positions:
            continue
        a, b = positions[p], positions[q]
        extensions = set()
        for values in vectors:
            if max(values[a], values[b]) >= weight:
                extensions.add(values)
            else:
                for vertex in (a, b):
                    new = list(values)
                    new[vertex] = weight
                    extensions.add(tuple(new))
        vectors = []
        for values in sorted(extensions, key=lambda v: (sum(v), v)):
            if not any(all(a <= b for a, b in zip(old, values)) for old in vectors):
                vectors.append(values)
    assert all(
        max(v[positions[p]], v[positions[q]]) >= weight
        for v in vectors for p, q, weight in edges
        if p in positions and q in positions
    )
    return vectors


def algebraic_cap(i, saving):
    """Exact bound from n**eta < 2**saving * i**i / [i]_S."""
    small_primes = tuple(p for p in PRIMES if p < i)
    divisor = i if any(i % p == 0 for p in small_primes) else 1
    eta = i - rough_exponent(i) - len(small_primes) + saving
    assert eta > 0
    # Clear all exponent denominators; only integer powers certify the cap.
    common = lcm(eta.denominator, saving.denominator)
    n_power = int(common * eta)
    rhs = 2 ** int(common * saving) * (i**i // divisor) ** common
    power_of_ten = 0
    while 10 ** (power_of_ten * n_power) < rhs:
        power_of_ten += 1
    return eta, power_of_ten


def report():
    edges = EDGES + NEW_EDGES
    graphs = []
    for largest in (13, 17, 19, 23):
        primes = tuple(p for p in PRIMES if p <= largest)
        vectors = minimal_vectors(primes, edges)
        minimum = min(map(sum, vectors))
        graphs.append({
            "primes": list(primes),
            "minimal_vector_count": len(vectors),
            "minimum_scaled": minimum,
            "saving": str(Fraction(minimum, SCALE)),
            "minimizers_scaled": [list(v) for v in vectors if sum(v) == minimum],
            "minimal_vectors_scaled": [list(v) for v in vectors],
        })
    bounds = []
    for i in (19, 22, 24, 25):
        primes = tuple(p for p in PRIMES if p < i)
        saving = Fraction(min(map(sum, minimal_vectors(primes, edges))), SCALE)
        eta, exponent = algebraic_cap(i, saving)
        bounds.append({
            "i": i,
            "saving": str(saving),
            "exponent_gap": str(eta),
            "algebraic_cap_power_of_ten": exponent,
            "scope": "Applies beyond the effective BFT thresholds, not numerically evaluated here.",
        })
    # The explicit 17,19 estimate is disjoint from the six-prime source
    # table. Its instantiated threshold therefore gives complete numerical
    # bounds at both indices below, without the other new effective pairs.
    source_rows = json.loads(Path(__file__).with_name(
        "erdos_699_bft_explicit_thresholds.json").read_text())
    source_pair = next(row for row in source_rows
                       if row["pair"] == [17, 19]
                       and Fraction(row["target"]) == Fraction(371, 2000))
    assert source_pair["row_threshold_maximum_position"] >= 24
    old_saving = Fraction(min(map(sum, minimal_vectors(PRIMES[:6], EXPLICIT_EDGES))), SCALE)
    assert old_saving == Fraction(913, 1000)
    numerical_saving = old_saving + Fraction(source_pair["target"])
    numerical_bounds = []
    for i in (22, 25):
        eta, algebraic = algebraic_cap(i, numerical_saving)
        numerical_bounds.append({
            "i": i,
            "saving": str(numerical_saving),
            "exponent_gap": str(eta),
            "algebraic_cap_power_of_ten": algebraic,
            "source_cap_power_of_ten": source_pair["row_threshold_power_of_ten"],
            "full_row_cap_power_of_ten": max(algebraic, 7, source_pair["row_threshold_power_of_ten"]),
        })
    return {
        "source": "Bennett–Filaseta–Trifonov, Theorem 2.2 and Corollary 2.3",
        "new_parameters": [list(row) for row in PARAMETERS],
        "weight_denominator": SCALE,
        "graphs": graphs,
        "algebraic_bounds": bounds,
        "fully_numerical_bounds": numerical_bounds,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_suffix(".json"))
    args = parser.parse_args()
    for p, q, weight, p_power, q_power, a, b, c, d, denominator in PARAMETERS:
        certify(p_power, q_power, a, b, c, d, Fraction(weight, SCALE), Fraction(1, denominator))
    result = report()
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "graph_savings": {row["primes"][-1]: row["saving"] for row in result["graphs"]},
        "algebraic_bounds": result["algebraic_bounds"],
    }, indent=2))

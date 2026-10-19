"""Exact prime-pair savings for the small indices of Erdős problem 699.

This checks a finite optimization in the proof, not a search through rows.
The edge weights are the lambda_2 entries of Bennett--Filaseta--Trifonov,
Corollary 2.3, and the explicit lambda entries of Theorem 2.1,
DOI 10.1515/CRELLE.2009.030. See the accompanying lead note.

For each edge pq of weight w, its two cofactor exponents satisfy
max(x_p, x_q) >= w. Choose an endpoint witnessing each constraint. The
least possible value at a vertex is then its largest assigned edge weight.
Enumerating orientations therefore computes the exact minimum of sum(x_p).
All arithmetic in the certificate and index comparison is rational.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


SCALE = 10_000
EDGES = (
    (2, 3, 2921),
    (2, 5, 2679),
    (2, 7, 2757),
    (2, 11, 698),
    (2, 13, 798),
    (3, 5, 2238),
    (3, 7, 505),
    (3, 11, 3453),
    (3, 13, 2372),
    (5, 7, 2667),
    (5, 11, 2091),
    (5, 13, 1838),
    (7, 13, 1243),
    (11, 13, 729),
)
EXPLICIT_EDGES = (
    (2, 3, 2850),
    (2, 5, 2580),
    (2, 7, 2590),
    (2, 11, 590),
    (2, 13, 540),
    (3, 5, 2160),
    (3, 7, 380),
    (3, 11, 3290),
    (3, 13, 2310),
    (5, 7, 2270),
    (5, 11, 1990),
    (5, 13, 1630),
    (7, 13, 980),
    (11, 13, 370),
)
TABLE_PRIMES = (2, 3, 5, 7, 11, 13)
SMALL_PRIMES = TABLE_PRIMES + (17, 19, 23, 29, 31)
PREVIOUSLY_EFFECTIVE = {28, 29, 31, 34, 35}


def graph_minimum(primes: tuple[int, ...], table: tuple = EDGES) -> dict:
    """Exhaust all choices of a witnessing endpoint for each max constraint."""
    positions = {p: j for j, p in enumerate(primes)}
    edges = [
        (positions[p], positions[q], weight)
        for p, q, weight in table
        if p in positions and q in positions
    ]
    minimum = sum(weight for _, _, weight in edges) + 1
    minimizers: set[tuple[int, ...]] = set()
    for orientation in range(1 << len(edges)):
        values = [0] * len(primes)
        for bit, (p, q, weight) in enumerate(edges):
            vertex = q if orientation & (1 << bit) else p
            values[vertex] = max(values[vertex], weight)
        value = sum(values)
        if value < minimum:
            minimum = value
            minimizers.clear()
        if value == minimum:
            minimizers.add(tuple(values))
    for values in minimizers:
        assert all(max(values[p], values[q]) >= w for p, q, w in edges)
    return {
        "primes": list(primes),
        "edge_count": len(edges),
        "orientations_checked": 1 << len(edges),
        "minimum_scaled": minimum,
        "minimum": str(Fraction(minimum, SCALE)),
        "minimizers_scaled": [list(values) for values in sorted(minimizers)],
    }


def rough_exponent(i: int) -> Fraction:
    if i == 4:
        return Fraction(17, 6)
    k = 2 * i // 3
    return Fraction(3 * k * (k + 1), 2 * (3 * k - i + 1))


def ceiling(value: Fraction) -> int:
    return -(-value.numerator // value.denominator)


def binary_bound(i: int, gamma: Fraction, eta: Fraction) -> int:
    """Bound n**eta < 2**gamma * i**i, using only integer arithmetic."""
    exponent = ceiling(
        Fraction(ceiling(gamma) + i * (i - 1).bit_length()) / eta
    )
    assert exponent * eta >= gamma + i * (i - 1).bit_length()
    return exponent


def report() -> dict:
    graphs = [graph_minimum(TABLE_PRIMES[:length]) for length in range(2, 7)]
    explicit_graphs = [
        graph_minimum(TABLE_PRIMES[:length], EXPLICIT_EDGES)
        for length in range(2, 7)
    ]
    savings = {tuple(row["primes"]): Fraction(row["minimum"]) for row in graphs}
    explicit_savings = {
        tuple(row["primes"]): Fraction(row["minimum"])
        for row in explicit_graphs
    }
    indices = []
    for i in range(4, 36):
        primes = tuple(p for p in TABLE_PRIMES if p < i)
        gamma = savings[primes]
        explicit_gamma = explicit_savings[primes]
        s = sum(p < i for p in SMALL_PRIMES)
        rho = rough_exponent(i)
        eta = i - rho - s + gamma
        explicit_eta = i - rho - s + explicit_gamma
        row = {
            "i": i,
            "small_prime_count": s,
            "table_primes": list(primes),
            "rho": str(rho),
            "saving": str(gamma),
            "remaining_exponent": str(eta),
            "effective_by_prime_pairs": eta > 0,
            "newly_effective": eta > 0 and i not in PREVIOUSLY_EFFECTIVE,
            "explicit_saving": str(explicit_gamma),
            "explicit_remaining_exponent": str(explicit_eta),
            "numerical_bound_by_prime_pairs": explicit_eta > 0,
        }
        if eta > 0:
            # Once the BFT thresholds hold and n >= 2(i-1), badness gives
            # n**eta < 2**gamma * i**i. Since i <= 2**ceil(log_2 i),
            # the following integer exponent is a certified upper bound.
            row["algebraic_bound_power_of_two"] = binary_bound(i, gamma, eta)
        if explicit_eta > 0:
            # Theorem 2.1 applies with D <= 100 once all selected factors
            # exceed 1,771,561, the largest entry in its exceptional list.
            # For i <= 35, n >= 2**21 implies this and n >= 2(i-1).
            row["full_row_bound_power_of_two"] = max(
                21, binary_bound(i, explicit_gamma, explicit_eta)
            )
        indices.append(row)
    return {
        "source": {
            "authors": "Bennett, Filaseta and Trifonov",
            "title": "On the factorization of consecutive integers",
            "doi": "10.1515/CRELLE.2009.030",
            "locator": "Corollary 2.3, lambda_2 column",
            "weight_denominator": SCALE,
            "edges": [list(edge) for edge in EDGES],
            "explicit_locator": "Theorem 2.1, lambda column",
            "explicit_edges": [list(edge) for edge in EXPLICIT_EDGES],
            "explicit_maximum_gap": 100,
            "explicit_largest_exception": 1_771_561,
        },
        "scope": "Finite exact proof optimization; no rows or columns enumerated.",
        "bound_scope": (
            "algebraic_bound_power_of_two uses Corollary 2.3 and still needs "
            "its effective x_0(i-1). full_row_bound_power_of_two uses the "
            "smaller Theorem 2.1 weights and already includes its numerical "
            "threshold and all exceptional pairs."
        ),
        "graphs": graphs,
        "explicit_graphs": explicit_graphs,
        "newly_effective_indices": [row["i"] for row in indices if row["newly_effective"]],
        "new_numerical_bounds": {
            str(row["i"]): row["full_row_bound_power_of_two"]
            for row in indices
            if row["newly_effective"] and row["numerical_bound_by_prime_pairs"]
        },
        "previously_effective_now_numerical_bounds": {
            str(row["i"]): row["full_row_bound_power_of_two"]
            for row in indices
            if row["i"] in {28, 31, 34}
        },
        "indices": indices,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_suffix(".json"))
    args = parser.parse_args()
    result = report()
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "graph_minima": {",".join(map(str, row["primes"])): row["minimum"] for row in result["graphs"]},
        "newly_effective_indices": result["newly_effective_indices"],
        "new_numerical_bounds": result["new_numerical_bounds"],
        "previously_effective_now_numerical_bounds": result["previously_effective_now_numerical_bounds"],
        "output": str(args.output),
    }, indent=2))


if __name__ == "__main__":
    main()

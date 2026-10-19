#!/usr/bin/env python3
"""Exact weighted-prime-pair certificate for index 11; no row search."""

from fractions import Fraction
from math import factorial
import json

from erdos_699_prime_pair_savings import EDGES, SCALE


def minimal_vectors(primes):
    positions = {p: j for j, p in enumerate(primes)}
    edges = [(positions[p], positions[q], weight)
             for p, q, weight in EDGES if p in positions and q in positions]
    vectors = set()
    for choices in range(1 << len(edges)):
        vector = [0] * len(primes)
        for bit, (p, q, weight) in enumerate(edges):
            target = q if choices & (1 << bit) else p
            vector[target] = max(vector[target], weight)
        vectors.add(tuple(vector))
    minimal = sorted(vector for vector in vectors if not any(
        other != vector and all(a <= b for a, b in zip(other, vector))
        for other in vectors))
    assert all(any(all(a <= b for a, b in zip(other, vector))
                   for other in minimal) for vector in vectors)
    assert all(all(max(vector[p], vector[q]) >= weight
                   for p, q, weight in edges) for vector in minimal)
    return edges, minimal


def gains(index, primes, k):
    edges, vectors = minimal_vectors(primes)
    size = len(primes)
    constant = (2 * k * (index - size) - k * (k + 1)
                - index * (index - 1) // 2 + size * (size - 1) // 2)
    rows = []
    for vector in vectors:
        gain = constant + sum(Fraction((2 * k - r) * v, SCALE)
                              for r, v in enumerate(sorted(vector)))
        rows.append({"vector_scaled": list(vector), "gain": str(gain)})
    return {"i": index, "k": k, "orientations": 1 << len(edges),
            "minimal_vector_count": len(vectors), "rows": rows}


def report():
    eleven = gains(11, (2, 3, 5, 7), 7)
    assert eleven["orientations"] == 64
    assert eleven["minimal_vector_count"] == 8
    assert min(Fraction(row["gain"]) for row in eleven["rows"]) == Fraction(7, 100)
    weights = [14 - t for t in range(11)]
    assert sum(weights) == 99
    assert sum(t * weight for t, weight in enumerate(weights)) == 385
    assert 10 ** (1525 * 7) > (2 * factorial(11) ** 14) ** 100
    assert 10 ** (22 * 4) * 4 ** 28 > (2 * factorial(11)) ** 11

    thirteen = gains(13, (2, 3, 5, 7, 11), 8)
    failures = [row for row in thirteen["rows"] if Fraction(row["gain"]) <= 0]
    assert failures == [{"vector_scaled": [2757, 3453, 2667, 0, 0],
                         "gain": "-1077/2000"}]
    return {"proof_scope": "Exact finite certificate, no binomial rows searched.",
            "index_11": eleven,
            "index_11_algebraic_bound": "10^1525",
            "index_11_full_bound": "max(10^1525, 10 + max_pair x0_pair(10))",
            "index_13_remaining_vector": failures[0]}


if __name__ == "__main__":
    print(json.dumps(report(), indent=2))

#!/usr/bin/env python3
"""Exact weighted-certificate identities; no enumeration of binomial rows."""

from fractions import Fraction
from math import factorial


def partition_counts(limit: int) -> list[int]:
    counts = [1] + [0] * limit
    for part in range(1, limit + 1):
        for total in range(part, limit + 1):
            counts[total] += counts[total - part]
    return counts


def position_patterns(size: int, cap: int):
    """Increasing nonnegative positions of fixed size and bounded sum."""
    def extend(prefix, first, budget):
        remaining = size - len(prefix)
        if not remaining:
            yield tuple(prefix)
            return
        next_position = first
        while (remaining * next_position
               + remaining * (remaining - 1) // 2 <= budget):
            yield from extend(prefix + [next_position], next_position + 1,
                              budget - next_position)
            next_position += 1
    yield from extend([], 0, cap)


def verify(size: int) -> dict:
    index = 3 * size
    k = 2 * size - 1
    degree = k * (k + 1)
    weights = [2 * k - t for t in range(index)]
    moment = sum(t * weight for t, weight in enumerate(weights))
    critical_sum = size * (size + 1) // 2
    assert min(weights) == size - 1
    assert sum(weights) - degree == 2 * k * size - critical_sum
    constant = Fraction(factorial(index - 1) ** (2 * k), 2 ** (degree - 1))
    assert constant > 1

    patterns = list(position_patterns(size, critical_sum - 1))
    assert len(patterns) == sum(partition_counts(size - 1))
    assert max(max(pattern) for pattern in patterns) == 2 * size - 2
    for pattern in patterns:
        assert len(set(pattern)) == size
        exponent = sum(weight for t, weight in enumerate(weights)
                       if t not in pattern) - degree
        assert exponent == sum(pattern) - critical_sum < 0
    for pattern in position_patterns(size, critical_sum):
        if sum(pattern) == critical_sum:
            assert min(weights[t] for t in pattern) >= k
    return {"i": index, "s": size, "k": k, "degree": degree,
            "n_threshold": 2 * moment, "remaining_patterns": len(patterns),
            "maximum_position": 2 * size - 2,
            "constant": f"({index - 1}!)^{2 * k}/2^{degree - 1}"}


if __name__ == "__main__":
    import json
    print(json.dumps([verify(size) for size in (9, 10, 11)], indent=2))

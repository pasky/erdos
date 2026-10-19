#!/usr/bin/env python3
"""Exact divisor certificate for the row-zero reductions at indices 4 and 5.

At index 5, a hypothetical bad pair with 8 not dividing n and 9 not
dividing n has j/n = a/q with q dividing 60.  The certificate checks
61 fixed rational-slope/residue cases, never an interval of binomial rows.
Only three candidate pairs survive the resulting fixed divisor conditions.
"""

import argparse
import json
from math import gcd, isqrt, prod
from pathlib import Path


def divisors(value):
    """Enumerate the divisors of one fixed positive certificate constant."""
    small = []
    large = []
    for d in range(1, isqrt(value) + 1):
        if value % d == 0:
            small.append(d)
            if d * d != value:
                large.append(value // d)
    return small + large[::-1]


def binomial_valuation(n, k, prime):
    def factorial_valuation(value):
        result = 0
        while value:
            value //= prime
            result += value
        return result
    return (factorial_valuation(n) - factorial_valuation(k)
            - factorial_valuation(n - k))


def certificate():
    candidates = set()
    cases = []
    for q in divisors(60):
        for a in range(1, q // 2 + 1):
            if gcd(a, q) != 1:
                continue
            for residue in range(6):
                if residue % gcd(q, 6):
                    continue
                choices = []
                for t in range(1, 5):
                    value = prod(a * t - q * r for r in range(t + 1))
                    if value and gcd(residue - t, 6) == 1:
                        choices.append((abs(value), t, value))
                assert choices, (a, q, residue)
                _, t, value = min(choices)
                survivors = []
                for divisor in divisors(5 * abs(value)):
                    n = divisor + t
                    if n % q or n % 6 != residue:
                        continue
                    j = a * (n // q)
                    if not 5 < j <= n // 2:
                        continue
                    if n % 8 == 0 or n % 9 == 0:
                        continue
                    candidates.add((n, j))
                    survivors.append([n, j])
                cases.append({"a": a, "q": q, "n_mod_6": residue,
                              "t": t, "farey_product": value,
                              "candidates": survivors})
    assert len(cases) == 61
    assert sorted(candidates) == [(28, 7), (210, 77), (780, 247)]
    witnesses = []
    for n, j, prime in [(28, 7, 5), (210, 77, 7), (780, 247, 7)]:
        valuations = [binomial_valuation(n, k, prime) for k in (5, j)]
        assert min(valuations) >= 1
        witnesses.append({"n": n, "j": j, "common_prime": prime,
                          "binomial_valuations": valuations})
    return {
        "scope": "61 fixed-slope divisor cases; no interval of rows searched",
        "conclusion_index_4": "Every bad triple has 4|n or 9|n (elementary proof in note)",
        "conclusion_index_5": "Every bad triple has 8|n or 9|n",
        "case_count": len(cases),
        "largest_fixed_divisor_constant": max(5 * abs(c["farey_product"])
                                              for c in cases),
        "surviving_candidates_and_common_primes": witnesses,
        "cases": cases,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = certificate()
    rendered = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()

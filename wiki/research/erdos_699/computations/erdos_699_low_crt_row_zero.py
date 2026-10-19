#!/usr/bin/env python3
"""Exact fixed-slope exclusions for indices 6 and 7; no row-interval scan."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def divisors_from_factors(factors: dict[int, int]) -> list[int]:
    result = [1]
    for p, exponent in sorted(factors.items()):
        old = result[:]
        power = 1
        for _ in range(exponent):
            power *= p
            result.extend(d * power for d in old)
    return sorted(result)


def factor_small(value: int) -> dict[int, int]:
    value = abs(value)
    assert value > 0
    factors = {}
    p = 2
    while p * p <= value:
        while value % p == 0:
            factors[p] = factors.get(p, 0) + 1
            value //= p
        p += 1
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def divisors(value: int) -> list[int]:
    return divisors_from_factors(factor_small(value))


def polynomial(a: int, q: int, t: int) -> int:
    return math.prod(a * t - q * r for r in range(t + 1))


def constant_data(a: int, q: int, t: int, denominator_prime: int):
    factors = factor_small(denominator_prime)
    for r in range(t + 1):
        for p, exponent in factor_small(a * t - q * r).items():
            factors[p] = factors.get(p, 0) + exponent
    value = denominator_prime * abs(polynomial(a, q, t))
    assert math.prod(p**exponent for p, exponent in factors.items()) == value
    return value, divisors_from_factors(factors)


def rough_part(value: int) -> int:
    for p in (2, 3, 5):
        while value % p == 0:
            value //= p
    return value


def verify_index(index: int) -> dict:
    assert index in (6, 7)
    denominator_prime = 1 if index == 6 else 7
    denominator_cap = 60 * denominator_prime
    records = []
    surviving_rows = set()
    raw_count = 0
    for q in divisors(denominator_cap):
        if q < 2:
            continue
        for a in range(1, q // 2 + 1):
            if math.gcd(a, q) != 1:
                continue
            for s in range(30):
                if s % math.gcd(q, 30):
                    continue
                choices = []
                for t in range(1, index):
                    if math.gcd(s - t, 30) == 1 and t % q:
                        value, possible_divisors = constant_data(a, q, t, denominator_prime)
                        choices.append((len(possible_divisors), value, t, possible_divisors))
                assert choices, (index, q, a, s)
                _, value, t, possible_divisors = min(choices)
                residual = []
                for d in possible_divisors:
                    n = d + t
                    if n % q or n % 30 != s:
                        continue
                    j = a * (n // q)
                    if not index < j <= n // 2:
                        continue
                    raw_count += 1
                    for shift in range(1, index):
                        rough = rough_part(n - shift)
                        rough //= math.gcd(rough, denominator_prime)
                        if polynomial(a, q, shift) % rough:
                            residual.append({"n": n, "j": j, "excluded_at_shift": shift,
                                             "required_divisor": rough,
                                             "polynomial_value": polynomial(a, q, shift)})
                            break
                    else:
                        surviving_rows.add((n, j))
                records.append({"q": q, "a": a, "residue_mod_30": s, "shift": t,
                                "constant": value, "residual_candidates": residual})
    assert not surviving_rows, sorted(surviving_rows)
    return {"index": index, "denominator_cap": denominator_cap,
            "case_count": len(records), "largest_constant": max(r["constant"] for r in records),
            "candidate_count_after_first_divisor": raw_count,
            "surviving_candidates": [], "cases": records}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_suffix(".json"))
    args = parser.parse_args()
    result = {"theorem": "For a bad triple, n/gcd(n,j) does not divide 60 at index 6 or 420 at index 7. Thus some p in {2,3,5} has v_p(n)-v_p(j) at least 3,2,2 respectively.",
              "arithmetic": "Exact integers only; fixed slope constants, no row-interval scan.",
              "records": [verify_index(index) for index in (6, 7)]}
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    for record in result["records"]:
        print({key: value for key, value in record.items() if key != "cases"})


if __name__ == "__main__":
    main()

"""Exact prime-power certificates for pair bounds on a finite height range.

Enumerates prime-power exponents and bounded differences, not binomial rows.
For p,q fixed and height at most 10**K, find every exception to
max(u,v)**3 >= min(p**a*u,q**b*v), with 0<|p**a*u-q**b*v|<=D.
Only minimal positive solutions require testing; the accompanying proof
explains why every other positive solution satisfies the inequality.
"""

from __future__ import annotations

import argparse
import json
from math import isqrt
from pathlib import Path
import sys


def powers(prime: int, bound: int) -> list[tuple[int, int]]:
    result = []
    exponent, power = 1, prime
    while power <= bound:
        result.append((exponent, power))
        exponent += 1
        power *= prime
    return result


def certify(p: int, q: int, cap: int, difference: int) -> dict:
    bound = 10 ** cap
    p_powers = powers(p, bound)
    q_powers = powers(q, bound)
    exceptions = []
    pair_count = checked_pairs = checked_signed_differences = 0
    exact_candidate_tests = 0
    for b, Q in q_powers:
        if Q <= difference:
            continue
        # If I is the inverse of p**(a-1) modulo Q, then
        # (I+kQ)/p is the inverse of p**a, where 0<=k<p makes it integral.
        # This computes all inverses using only arithmetic by small integers.
        inverse = 1
        inverse_Q_mod_p = pow(Q, -1, p)
        for a, P in p_powers:
            k = (-inverse * inverse_Q_mod_p) % p
            inverse = (inverse + k * Q) // p
            if P <= difference:
                continue
            pair_count += 1
            A, B = max(P, Q), min(P, Q)
            # A violation would require (A-D)**2 < B**3. These bit-length
            # bounds rigorously reject most impossible exponent pairs.
            if 2 * ((A - difference).bit_length() - 1) >= 3 * B.bit_length():
                continue
            checked_pairs += 1
            residue = 0
            for d in range(1, difference + 1):
                residue += inverse
                if residue >= Q:
                    residue -= Q
                for sign, u in ((1, residue), (-1, Q - residue)):
                    checked_signed_differences += 1
                    # If u**2 >= P, then u**3 >= P*u >= min(P*u,Q*v).
                    if 2 * (u.bit_length() - 1) >= P.bit_length():
                        continue
                    if u * u >= P:
                        continue
                    v = (P * u - sign * d) // Q
                    assert 0 < u < Q and 0 < v < P
                    if v * v >= Q:
                        continue
                    x, y = P * u, Q * v
                    if max(x, y) > bound:
                        continue
                    exact_candidate_tests += 1
                    if max(u, v) ** 3 < min(x, y):
                        record = {
                            "p_exponent": a, "q_exponent": b,
                            "signed_difference": sign * d,
                            "p_cofactor": u, "q_cofactor": v,
                            "smaller_height": min(x, y),
                            "larger_height": max(x, y),
                        }
                        exceptions.append(record)
        if b % 200 == 0:
            print(f"pair {p},{q}: completed {b}/{len(q_powers)} q-exponents", file=sys.stderr, flush=True)
    small_power_threshold = isqrt(difference ** 3) + 1
    maximum_exception = max((r["smaller_height"] for r in exceptions), default=0)
    height_threshold = max(small_power_threshold, maximum_exception + 1)
    return {
        "pair": [p, q], "height_cap_power_of_ten": cap,
        "maximum_difference": difference,
        "reciprocal_exponent_denominator": 3,
        "height_threshold": height_threshold,
        "p_power_count": len(p_powers), "q_power_count": len(q_powers),
        "exponent_pairs_considered": pair_count,
        "exponent_pairs_after_safe_filter": checked_pairs,
        "signed_differences_considered": checked_signed_differences,
        "exact_candidate_tests": exact_candidate_tests,
        "exception_count": len(exceptions),
        "exceptions": exceptions,
        "conclusion": "max(u,v)^3 >= min(p^a*u,q^b*v) throughout the stated height range",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pairs", nargs="+", default=[
        "17,19", "2,17", "11,23", "5,17", "7,17", "2,3", "2,5", "3,5", "3,7", "5,7",
    ])
    parser.add_argument("--cap", type=int, default=976)
    parser.add_argument("--difference", type=int, default=24)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_suffix(".json"))
    args = parser.parse_args()
    records = []
    for pair in args.pairs:
        p, q = map(int, pair.split(","))
        row = certify(p, q, args.cap, args.difference)
        records.append(row)
        print(json.dumps({k: v for k, v in row.items() if k != "exceptions"}), flush=True)
        args.output.write_text(json.dumps({
            "scope": "Exact finite exponent-pair certificate; no binomial rows enumerated.",
            "records": records,
        }, indent=2) + "\n")


if __name__ == "__main__":
    main()

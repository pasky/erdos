"""Check the cubic reduction and search its sparse remaining rows.

The accompanying proof shows that a bad triple with i=3 must have
    n = 2**h * u, h>=2, u odd, 3*u**3 < 2**h, and 4<=j<n/2.
All factorization here is exact trial division by a complete prime list.
The default bounded search reaches n=10**12; it is not a global finiteness proof.
Requires Python 3.11 or later and only the standard library.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from functools import lru_cache
import json
from math import comb, gcd, isqrt
import sys

from erdos_699_effectivity import lucas_nonzero, primes_through


def factor(n: int, primes: list[int]) -> dict[int, int]:
    result = {}
    for p in primes:
        if p * p > n:
            break
        if n % p:
            continue
        exponent = 0
        while n % p == 0:
            n //= p
            exponent += 1
        result[p] = exponent
    if n > 1:
        result[n] = 1
    return result


def columns(n: int, factorizations: list[dict], threshold: int = 3, upper: int | None = None) -> tuple[list[int], list[int]]:
    """Return full prime-power residue candidates and actual bad columns."""
    upper = n // 2 if upper is None else upper
    conditions = []
    for residue, factors in enumerate(factorizations):
        for p, exponent in factors.items():
            if p < threshold or (p == 3 and exponent == 1):
                continue
            conditions.append((p**exponent, residue, p))
    conditions.sort(key=lambda item: Fraction(item[0], item[1] + 1), reverse=True)
    modulus = 1
    residues = [0]
    for power, t, _ in conditions:
        inverse = pow(modulus, -1, power)
        new_modulus = modulus * power
        new_residues = []
        for old in residues:
            for r in range(t + 1):
                x = old + modulus * (((r - old) * inverse) % power)
                first = x + max(0, (4 - x + new_modulus - 1) // new_modulus) * new_modulus
                if first <= upper:
                    new_residues.append(x)
        modulus, residues = new_modulus, new_residues
        if not residues:
            return [], []
    candidates = []
    for x in residues:
        first = x + max(0, (4 - x + modulus - 1) // modulus) * modulus
        candidates.extend(range(first, upper + 1, modulus))
    candidates.sort()
    bad = [j for j in candidates if all(lucas_nonzero(n, j, p) for _, _, p in conditions)]
    return candidates, bad


def bounded_checks(limit: int = 200) -> dict:
    primes = primes_through(limit)
    cases = 0
    for n in range(8, limit + 1):
        factors = [factor(n - r, primes) for r in range(3)]
        for threshold in (3, 5):
            _, actual = columns(n, factors, threshold)
            expected = []
            for j in range(4, n // 2 + 1):
                common = gcd(comb(n, 3), comb(n, j))
                for p in primes:
                    if p >= threshold:
                        break
                    while common % p == 0:
                        common //= p
                if common == 1:
                    expected.append(j)
                cases += 1
            assert actual == expected, (n, threshold, actual, expected)
        for j in range(4, n // 2 + 1):
            c = n - j
            a3, a2, a1, a0 = comb(c, 3), j * comb(c, 2), c * comb(j, 2), comb(j, 3)
            disc = a2*a2*a1*a1 - 4*a3*a1**3 - 4*a2**3*a0 - 27*a3*a3*a0*a0 + 18*a3*a2*a1*a0
            f = j*j*c*c*(j-1)*(c-1)*(n-1)*(n-2)**2
            assert 12 * disc == f
            if n % 4 == 0:
                assert disc % 8 == 0
    controls = []
    for n, j in [(10, 5), (28, 14), (244, 122), (2188, 1094)]:
        factors = [factor(n - r, primes_through(isqrt(n))) for r in range(3)]
        _, strict_bad = columns(n, factors, 5)
        _, weak_bad = columns(n, factors, 3)
        assert j in strict_bad and j not in weak_bad
        controls.append([n, 3, j])
    return {
        "small_n_limit": limit,
        "binomial_gcd_comparisons": cases,
        "cubic_discriminant_identity": "verified on every admissible tested pair",
        "strict_threshold_positive_controls": controls,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=10**12)
    args = parser.parse_args()
    if args.limit < 8:
        parser.error("--limit must be at least 8")
    checks = bounded_checks()
    primes = primes_through(isqrt(args.limit))

    @lru_cache(maxsize=None)
    def odd_factors(n: int) -> dict[int, int]:
        return {p: e for p, e in factor(n, primes).items() if p != 2}

    rows = 0
    candidate_count = 0
    candidate_examples = []
    bad = []
    by_h = []
    for h in range(2, args.limit.bit_length()):
        power = 2**h
        rows_h = 0
        u = 1
        while power * u <= args.limit and 3 * u**3 < power:
            n = power * u
            if n >= 8:
                fs = [odd_factors(u), odd_factors(n - 1), odd_factors((n - 2) // 2)]
                candidates, exceptions = columns(n, fs, upper=n // 2 - 1)
                rows += 1
                rows_h += 1
                candidate_count += len(candidates)
                for j in candidates:
                    if len(candidate_examples) < 20:
                        candidate_examples.append([n, 3, j])
                bad.extend([n, 3, j] for j in exceptions)
            u += 2
        by_h.append({"v2_n": h, "rows": rows_h})
        if h % 10 == 0:
            print(f"h<={h}: {rows} rows, {candidate_count} residue candidates", file=sys.stderr, flush=True)
    print(json.dumps({
        "threshold": "p>=3",
        "n_at_most": args.limit,
        "necessary_row_conditions": "n=2^h*u, h>=2, u odd, 3*u^3<2^h",
        "excluded_columns": "j=n/2 is good; admissibility requires j>=4",
        "rows_requiring_search": rows,
        "prime_power_residue_candidates": candidate_count,
        "first_residue_candidates": candidate_examples,
        "bad_triples": bad,
        "by_v2_n": by_h,
        "checks": checks,
        "scope": "Exhaustive for the stated row bound using the proved reductions; no global finiteness claim.",
    }, indent=2))


if __name__ == "__main__":
    main()

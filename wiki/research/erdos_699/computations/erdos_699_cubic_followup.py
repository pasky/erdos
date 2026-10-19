"""Certify complete ranges of v_2(n) in the cubic case of Erdos 699.

Run with:
    uv run --with sympy==1.14.0 python \
        wiki/research/erdos_699/computations/erdos_699_cubic_followup.py

SymPy discovers factorizations. Every returned prime is proved separately by
an exact sieve or a recursive, fully factored n-1 primality certificate, and
every factorization is checked by multiplication. No probable-prime result is
accepted as a proof. The search uses the earlier proved cubic row restriction.
This is a finite computation, not a proof for unbounded v_2(n).
"""

from __future__ import annotations

import argparse
from collections import Counter
import json
from math import comb, gcd, prod
import sys

import sympy

from erdos_699_i_eq_3 import bounded_checks, columns, primes_through


class CertifiedFactorization:
    """Find factors with SymPy; verify them using only integer arithmetic."""

    def __init__(self) -> None:
        self.sieve_limit = 100_000
        self.sieve_primes = set(primes_through(self.sieve_limit))
        self.proved_primes: set[int] = set()
        self.factorizations: dict[int, dict[int, int]] = {1: {}}
        self.witnesses = 0

    def factor(self, n: int) -> dict[int, int]:
        if n in self.factorizations:
            return self.factorizations[n]
        assert n >= 2
        factors = dict(sorted((int(p), int(e)) for p, e in sympy.factorint(n).items()))
        assert all(p >= 2 and e >= 1 for p, e in factors.items())
        assert prod(p**e for p, e in factors.items()) == n
        for p in factors:
            self.prove_prime(p)
        self.factorizations[n] = factors
        return factors

    def prove_prime(self, p: int) -> None:
        if p <= self.sieve_limit:
            assert p in self.sieve_primes, ("composite factor", p)
            return
        if p in self.proved_primes:
            return
        factors = self.factor(p - 1)
        witnesses = []
        for q in factors:
            for a in range(2, 1002):
                if pow(a, p - 1, p) == 1 and gcd(pow(a, (p - 1) // q, p) - 1, p) == 1:
                    witnesses.append((q, a))
                    break
            else:
                raise ArithmeticError(f"No primality witness certified for {p}, q={q}")
        # For every prime divisor r of p, these witnesses force p-1 | r-1:
        # the order of a mod r contains the full q-part of p-1, for each q.
        # Hence r >= p, which proves p is prime.
        self.witnesses += len(witnesses)
        self.proved_primes.add(p)


def active_powers(factors: dict[int, int]) -> list[int]:
    return [p**e for p, e in factors.items() if p > 2 and (p != 3 or e >= 2)]


def endpoint_checks() -> dict:
    """Check the factor-free endpoint criterion against the earlier CRT code."""
    factorer = CertifiedFactorization()
    comparisons = 0
    column_family_checks = 0
    for n in range(8, 301, 4):
        u = n // (n & -n)
        odd_binomial = comb(n, 3) // (n & -n)
        fs = [factorer.factor(u), factorer.factor(n - 1), factorer.factor((n - 2) // 2)]
        residues, _ = columns(n, fs, upper=n)
        endpoints = []
        for j in range(4, n + 1):
            c = n - j
            d = n - 2 * j
            alternating = comb(j, 3) - c * comb(j, 2) + j * comb(c, 2) - comb(c, 3)
            assert 6 * alternating == -d * (d*d - 3*n + 2)
            if j < n // 2 and d // (d & -d) <= u:
                common = gcd(comb(n, 3), comb(n, j))
                assert common // (common & -common) > 1
                column_family_checks += 1
            by_endpoints = comb(j, 3) % odd_binomial == 0 and comb(c, 3) % odd_binomial == 0
            by_products = (3 * j * c) % (u * (n - 1)) == 0 and (
                j * (j - 1) * (j - 2)
            ) % (u * (n - 1) * (n - 2)) == 0
            assert by_endpoints == by_products
            if by_endpoints:
                endpoints.append(j)
            comparisons += 1
        assert residues == endpoints

    # Nontrivial positive controls for the last two labels alone. They are
    # not cubic counterexamples: the odd part of n supplies another condition.
    controls = [(76672, 26775), (175492, 60606)]
    for n, j in controls:
        f1, f2 = factorer.factor(n - 1), factorer.factor((n - 2) // 2)
        residues, _ = columns(n, [{}, f1, f2], upper=n // 2 - 1)
        assert j in residues
        assert all(p**3 < 3 * n*n for p in active_powers(f1))
        assert all(p*p < 6 * n for p in active_powers(f2))
    return {
        "endpoint_comparisons": comparisons,
        "alternating_cubic_identity_checks": comparisons,
        "proved_column_family_gcd_checks": column_family_checks,
        "last_two_label_positive_controls": controls,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    bounds = parser.add_mutually_exclusive_group()
    bounds.add_argument("--max-v2", type=int, help="Check every possible row with v_2(n) at most this value.")
    bounds.add_argument("--limit", type=int, help="Check every possible row n at most this value.")
    parser.add_argument("--min-v2", type=int, default=2, help="Start at this valuation; values above 2 give a partial range.")
    args = parser.parse_args()
    if args.limit is not None and args.limit < 8:
        parser.error("--limit must be at least 8")
    max_h = args.max_v2 if args.max_v2 is not None else (args.limit.bit_length() - 1 if args.limit else 48)
    if max_h < 3:
        parser.error("--max-v2 must be at least 3")
    if not 2 <= args.min_v2 <= max_h:
        parser.error("--min-v2 must be between 2 and the upper valuation bound")
    checks = bounded_checks()
    checks.update(endpoint_checks())
    factorer = CertifiedFactorization()
    totals: Counter = Counter()
    by_h = []
    maximum_n = 0
    survivors = []
    bad = []
    for h in range(args.min_v2, max_h + 1):
        power = 2**h
        counts: Counter = Counter()
        u = 1
        while 3 * u**3 < power and (args.limit is None or power * u <= args.limit):
            n = power * u
            if n < 8:
                u += 2
                continue
            maximum_n = max(maximum_n, n)
            f1 = factorer.factor(n - 1)
            f2 = None
            if any(p**3 >= 3 * n*n for p in active_powers(f1)):
                reason = "large_prime_power_in_n_minus_1"
            else:
                f2 = factorer.factor((n - 2) // 2)
                if any(p*p >= 6 * n for p in active_powers(f2)):
                    reason = "large_prime_power_in_n_minus_2"
                else:
                    candidates, exceptions = columns(
                        n, [factorer.factor(u), f1, f2], upper=n // 2 - 1
                    )
                    if candidates:
                        survivors.extend([n, j] for j in candidates)
                        bad.extend([n, 3, j] for j in exceptions)
                        reason = "full_lucas_test"
                    else:
                        reason = "incompatible_prime_power_residues"
            counts["rows"] += 1
            counts[reason] += 1
            u += 2
        totals.update(counts)
        by_h.append({"v2_n": h, **counts})
        print(f"h={h}: {totals['rows']} rows checked", file=sys.stderr, flush=True)
    print(json.dumps({
        "threshold": "p>=3",
        "min_v2_n": args.min_v2,
        "max_v2_n": max_h,
        "n_at_most": args.limit,
        "necessary_row_conditions": "n=2^h*u, h>=2, u odd, 3*u^3<2^h",
        "maximum_row_requiring_search": maximum_n,
        "totals": dict(totals),
        "prime_power_residue_candidates": survivors,
        "bad_triples": bad,
        "by_v2_n": by_h,
        "checks": checks,
        "factorization_discovery": f"SymPy {sympy.__version__}; results checked by multiplication and exact primality certificates",
        "sieve_primality_limit": factorer.sieve_limit,
        "recursive_prime_certificates": len(factorer.proved_primes),
        "primality_witnesses": factorer.witnesses,
        "scope": "Exhaustive for the stated bound, using the proved reductions. No conclusion for unbounded v_2(n).",
    }, indent=2))
    if bad:
        raise SystemExit("Counterexamples found; the requested range is not excluded.")


if __name__ == "__main__":
    main()

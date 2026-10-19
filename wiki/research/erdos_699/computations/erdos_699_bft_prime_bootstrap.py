"""Finite prime-interval bootstrap for BFT coefficient-gcd lower bounds.

All certification arithmetic is integral. Log-prime weights are bounded
using a directed-interval lookup table, then summed as fixed-point integers.
The finite sieve stops at 10**8 by default; retained BFT and Dusart theta
bounds cover larger arguments. This enumerates no binomial rows.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from math import isqrt
from pathlib import Path
import time

import numpy as np
from mpmath import iv

from erdos_699_bft_dusart_gcd import gcd_exponent_lower

SCALE = 1 << 32
BUCKETS = 1 << 14


def ceil_div(a: int, b: int) -> int:
    return -(-a // b)


class PrimeLogIntervals:
    def __init__(self, limit: int = 10**8):
        self.limit = limit
        iv.dps = 60
        lo = np.empty(BUCKETS + 1, dtype=np.uint64)
        hi = np.empty(BUCKETS + 1, dtype=np.uint64)
        for k in range(BUCKETS, 2 * BUCKETS + 1):
            value = iv.log(iv.mpf(k) / BUCKETS) * SCALE
            lo[k - BUCKETS] = int(value.a)
            hi[k - BUCKETS] = int(value.b) + 1
        self.log_lo, self.log_hi = lo, hi
        self.log2_lo, self.log2_hi = int(lo[-1]), int(hi[-1])
        sieve = np.ones(limit + 1, dtype=np.bool_)
        sieve[:2] = False
        for p in range(2, isqrt(limit) + 1):
            if sieve[p]:
                sieve[p * p::p] = False
        primes = np.flatnonzero(sieve).astype(np.int64)
        del sieve
        assert int(primes[-1]) * SCALE < 2**64
        powers = np.array([1 << k for k in range(limit.bit_length() + 1)],
                          dtype=np.int64)
        exponents = np.searchsorted(powers, primes, side="right") - 1
        buckets = (primes << 14) >> exponents
        offsets = (buckets - BUCKETS).astype(np.int64)
        weights_lo = exponents.astype(np.uint64) * self.log2_lo + lo[offsets]
        weights_hi = exponents.astype(np.uint64) * self.log2_hi + hi[offsets + 1]
        # Each weight is between 0 and SCALE*log(limit)+1. This coarse
        # bound proves that both cumulative sums fit in uint64.
        assert len(primes) * (limit.bit_length() * SCALE + 2) < 2**64
        self.primes = primes
        self.prefix_lo = np.r_[np.uint64(0), np.cumsum(weights_lo, dtype=np.uint64)]
        self.prefix_hi = np.r_[np.uint64(0), np.cumsum(weights_hi, dtype=np.uint64)]
        self.metadata = {
            "sieve_limit": limit, "prime_count": len(primes),
            "fixed_point_scale": SCALE, "logarithm_buckets": BUCKETS,
            "prime_array_sha256": hashlib.sha256(primes.tobytes()).hexdigest(),
            "lower_prefix_sha256": hashlib.sha256(self.prefix_lo.tobytes()).hexdigest(),
            "upper_prefix_sha256": hashlib.sha256(self.prefix_hi.tobytes()).hexdigest(),
            "log_table_lower_sha256": hashlib.sha256(lo.tobytes()).hexdigest(),
            "log_table_upper_sha256": hashlib.sha256(hi.tobytes()).hexdigest(),
        }

    def log_lower(self, x: int) -> int:
        b = x.bit_length() - 1
        k = (x * BUCKETS) >> b
        return b * self.log2_lo + int(self.log_lo[k - BUCKETS])

    def theta_bounds(self, x: int) -> tuple[int, int]:
        if x <= self.limit:
            k = int(np.searchsorted(self.primes, x, side="right"))
            return int(self.prefix_lo[k]), int(self.prefix_hi[k])
        assert 1 <= x <= 10**11
        # BFT Lemma 5.4: x - 2.072*sqrt(x) < theta(x) < x.
        root = isqrt(x * SCALE**2)
        if root * root < x * SCALE**2:
            root += 1
        error = ceil_div(259 * root, 125)
        # Dusart (2010), Theorem 5.2, absolute theta errors eta*x/log(x)^k.
        log_x = self.log_lower(x)
        for power, eta_num, eta_den, threshold in (
            (3, 1, 1, 89967803),
            (2, 1, 20, 122568683),
            (3, 39, 50, 158822621),
            (1, 1, 1000, 908994923),
            (2, 1, 100, 7713133853),
        ):
            if x >= threshold:
                error = min(error, ceil_div(
                    eta_num * x * SCALE**(power + 1),
                    eta_den * log_x**power))
        return max(0, x * SCALE - error), x * SCALE

    def interval_sum_lower(self, uppers: np.ndarray, lowers: np.ndarray) -> int:
        keep = uppers > lowers
        uppers, lowers = uppers[keep], lowers[keep]
        assert len(uppers) == 0 or int(uppers.max()) * SCALE < 2**64
        exact = uppers <= self.limit
        iu = np.searchsorted(self.primes, uppers[exact], side="right")
        il = np.searchsorted(self.primes, lowers[exact], side="right")
        # Using the same LOWER prefix at both ends directly sums lower
        # bounds for just the primes in the interval. There is no subtraction
        # of two unrelated lower estimates here.
        total = int(np.sum(self.prefix_lo[iu] - self.prefix_lo[il], dtype=np.uint64))
        for upper, lower in zip(uppers[~exact], lowers[~exact]):
            hi_lower, _ = self.theta_bounds(int(upper))
            _, lo_upper = self.theta_bounds(int(lower))
            total += max(0, hi_lower - lo_upper)
        return total


def prime_intervals(c: int, d: int, terms: int):
    ts, numerators, denominators = [], [], []
    h = c + d
    for t in range(1, terms + 1):
        k, r = divmod(d * t, h)
        if 2 * r <= h:
            continue
        a, b = d, k + 1
        e, f = c - d, t - 2 * k - 1
        assert b > 0 and f > 0
        if e * b > a * f:
            a, b = e, f
        ts.append(t)
        numerators.append(a)
        denominators.append(b)
    return (np.array(ts, dtype=np.int64),
            np.array(numerators, dtype=np.int64),
            np.array(denominators, dtype=np.int64))


def bootstrap(row: dict, theta: PrimeLogIntervals, lower_start: int = 1000,
              terms: int = 4000) -> dict:
    c, d = row["seed"][-2:]
    analytic = row["gcd_certificate"]
    upper_end = analytic["m0"] - 1
    target = Fraction(analytic["ell_lower"])
    regenerated = gcd_exponent_lower(
        c, d, terms=analytic["terms"], m0=analytic["m0"],
        scale=analytic["rounding_denominator"],
        root_scale=analytic["root_scale"])
    assert Fraction(regenerated["ell_lower"]) == target
    ts, vn, vd = prime_intervals(c, d, terms)
    digest = hashlib.sha256()
    leaves = visited = 0
    min_margin = None
    unsupported = None
    stack = [(lower_start, upper_end)]
    covered_right = upper_end
    started = time.monotonic()
    while stack:
        left, right = stack.pop()
        visited += 1
        valid = 2 * ts <= left
        upper_args = ((c + d) * left - 2) // ts[valid]
        lower_args = vn[valid] * right // vd[valid]
        lower_sum = theta.interval_sum_lower(upper_args, lower_args)
        margin_num = (lower_sum * target.denominator
                      - d * right * SCALE * target.numerator)
        if margin_num >= 0:
            assert right == covered_right
            covered_right = left - 1
            leaves += 1
            if leaves % 20000 == 0:
                print(json.dumps({"pair": row["pair"], "leaves": leaves, "left": left, "elapsed_seconds": round(time.monotonic() - started, 1)}), flush=True)
            margin = Fraction(margin_num, d * right * SCALE * target.denominator)
            min_margin = margin if min_margin is None else min(min_margin, margin)
            digest.update(f"{left},{right},{lower_sum}\n".encode())
        elif left == right:
            unsupported = left
            assert covered_right == left
            break
        else:
            middle = (left + right) // 2
            # Right-first traversal lets us stop at the largest unsupported
            # singleton. Every larger integer has already been certified.
            stack.append((left, middle))
            stack.append((middle + 1, right))
    effective_start = unsupported + 1 if unsupported is not None else lower_start
    assert covered_right == effective_start - 1
    result = {
        "pair": row["pair"], "seed": row["seed"],
        "targets_by_prime": row["targets_by_prime"],
        "ell_lower": str(target), "finite_interval_start": effective_start,
        "finite_interval_end": upper_end,
        "analytic_gcd_certificate": analytic,
        "terms": terms, "certified_intervals": leaves, "visited_nodes": visited,
        "largest_unsupported_singleton": unsupported,
        "minimum_margin": str(min_margin),
        "partition_sha256": digest.hexdigest(),
        "elapsed_seconds": round(time.monotonic() - started, 3),
        "conclusion": "G(c,d,dm-delta) >= exp(d*m*ell) for every m >= finite_interval_start and delta in {0,1}",
    }
    print(json.dumps({key: result[key] for key in
                     ("pair", "finite_interval_start", "certified_intervals",
                      "visited_nodes", "elapsed_seconds")}), flush=True)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--pairs", default="")
    parser.add_argument("--sieve-limit", type=int, default=10**8)
    parser.add_argument("--lower-start", type=int, default=1000)
    args = parser.parse_args()
    rows = json.loads(args.input.read_text())
    if args.pairs:
        keep = {tuple(map(int, pair.split(','))) for pair in args.pairs.split(';')}
        rows = [row for row in rows if tuple(row["pair"]) in keep]
    theta = PrimeLogIntervals(args.sieve_limit)
    print(json.dumps(theta.metadata), flush=True)
    output = {
        "input_file": args.input.name,
        "prime_log_certificate": theta.metadata,
        "records": [],
    }
    for row in rows:
        output["records"].append(bootstrap(row, theta, args.lower_start))
        if args.output:
            args.output.write_text(json.dumps(output, indent=2) + "\n")


if __name__ == "__main__":
    main()

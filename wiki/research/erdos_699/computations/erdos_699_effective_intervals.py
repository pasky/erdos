"""Try the retained interval certificate at newly effective small indices.

The numerical tail uses the .913 prime-pair saving documented in
../archive/previous_bounds/small_index_effective.md.  The interval engine is
the unchanged engine of erdos_699_i_ge_35.py.  This does not iterate through
individual rows.  An unexcluded singleton means only that these inequalities
do not exclude that row; it is not evidence of a bad triple.
"""

from __future__ import annotations

import argparse
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
import hashlib
import json
from math import log
from pathlib import Path
import sys

import erdos_699_i_ge_35 as intervals
from erdos_699_effectivity import primes_through
from erdos_699_prime_pair_savings import EXPLICIT_EDGES, SCALE, TABLE_PRIMES


PAIR_THRESHOLD = 1_771_595
PAIR_SAVING = Decimal(".913")
ELIGIBLE = [17, 23, 26, 27, 28, 30, 31, 32, 33, 34]


def pair_vectors() -> list[tuple[int, ...]]:
    """All minimal endpoint assignments, under componentwise comparison."""
    positions = {p: k for k, p in enumerate(TABLE_PRIMES)}
    edges = [(positions[p], positions[q], w) for p, q, w in EXPLICIT_EDGES]
    assignments = set()
    for orientation in range(1 << len(edges)):
        values = [0] * len(TABLE_PRIMES)
        for bit, (p, q, weight) in enumerate(edges):
            vertex = q if orientation & (1 << bit) else p
            values[vertex] = max(values[vertex], weight)
        assignments.add(tuple(values))
    result = []
    for values in sorted(assignments, key=lambda v: (sum(v), v)):
        if not any(all(a <= b for a, b in zip(old, values)) for old in result):
            result.append(values)
    return result


def prime_valuation(n: int, p: int) -> int:
    result = 0
    while n % p == 0:
        result += 1
        n //= p
    return result


def check_index_with_pairs(i: int, primes: list[int], records: list[list[int]], max_nodes: int,
                           singleton_checker=None) -> dict:
    """The same interval proof, with pair bounds also applied inside intervals."""
    lower = min(start for gap, start in records if gap > i)
    primes = [p for p in primes if p < i]
    c = intervals.constants(i, lower)
    cap, exponent = inclusive_row_cap(i, primes, c)
    data = intervals.prime_power_data(i, cap, primes)
    vectors = pair_vectors()
    float_vectors = [tuple(v / SCALE for v in values) for values in vectors]
    lower_logs = [intervals.log_bounds(p)[0] for p in primes]
    denominator_valuations = [prime_valuation(i, p) for p in primes]
    stack = [(lower, cap)]
    visited = leaves = pair_leaves = 0
    exact_singletons = []
    minimum = Decimal("Infinity")
    leaf_hash = hashlib.sha256()
    fat_exponent = c["fat_exponent_numerator"] / c["multiplicity"]
    fat_constant = float(c["fat_constant_lo"])
    orbit_constant = float(c["orbit_constant_lo"])
    while stack:
        left, right = stack.pop()
        visited += 1
        if visited > max_nodes:
            raise RuntimeError(f"node limit reached at i={i}; proof incomplete; next interval [{left},{right}]")
        if visited % 100_000 == 0:
            print(f"i={i}: visited {visited} intervals; current lower endpoint {left}", file=sys.stderr, flush=True)
        counts = intervals.valuation_upper_counts(left, right, data)
        individual = [e * item[1] for e, item in zip(counts, data)]
        guide_upper = sum(individual)
        guide_lower = max(
            fat_exponent * log(left) + fat_constant,
            i / 4 * log(left) + orbit_constant,
        )
        margin = Decimal(0)
        used_pair = False
        if guide_lower > guide_upper:
            margin = intervals.certified_margin(i, left, counts, data, c)
        elif left >= PAIR_THRESHOLD:
            log_numerator = log(right)
            log_base = log(left - i + 1)
            guide_pair_upper = max(
                sum(min(individual[k], log_numerator - v * log_base - denominator_valuations[k] * data[k][1])
                    for k, v in enumerate(values)) + sum(individual[len(TABLE_PRIMES):])
                for values in float_vectors
            )
            if guide_lower > guide_pair_upper:
                log_numerator_hi = intervals.log_bounds(right)[1]
                log_base_lo = intervals.log_bounds(left - i + 1)[0]
                log_left_lo = intervals.log_bounds(left)[0]
                with localcontext() as ctx:
                    ctx.prec = intervals.PRECISION
                    ctx.rounding = ROUND_FLOOR
                    deductions = [
                        [Decimal(v) * log_base_lo / SCALE + denominator_valuations[k] * lower_logs[k]
                         for k, v in enumerate(values)]
                        for values in vectors
                    ]
                with localcontext() as ctx:
                    ctx.prec = intervals.PRECISION
                    ctx.rounding = ROUND_CEILING
                    ordinary_upper = [e * item[2] for e, item in zip(counts, data)]
                    pair_upper = max(
                        sum((min(ordinary_upper[k],
                                 log_numerator_hi - deduction)
                             for k, deduction in enumerate(values)), Decimal(0))
                        + sum(ordinary_upper[len(TABLE_PRIMES):], Decimal(0))
                        for values in deductions
                    )
                with localcontext() as ctx:
                    ctx.prec = intervals.PRECISION
                    ctx.rounding = ROUND_FLOOR
                    fat = c["fat_exponent_numerator"] * log_left_lo / c["multiplicity"] + c["fat_constant_lo"]
                    orbit = i * log_left_lo / 4 + c["orbit_constant_lo"]
                    margin = max(fat, orbit) - pair_upper
                used_pair = margin > 0
        if margin > 0:
            minimum = min(minimum, margin)
            leaves += 1
            pair_leaves += used_pair
            leaf_hash.update(f"{left}:{right}\n".encode())
            continue
        if left == right:
            if singleton_checker is not None and singleton_checker(left, i):
                exact_singletons.append(left)
                leaves += 1
                leaf_hash.update(f"{left}:{right}\n".encode())
                continue
            raise RuntimeError(f"unexcluded row n={left} at i={i}; proof incomplete")
        middle = (left + right) // 2
        stack.extend([(left, middle), (middle + 1, right)])
    return {
        "i": i,
        "terminal_prime_lower_row": lower,
        "inclusive_cap_power_of_ten": exponent,
        "visited_intervals": visited,
        "certified_intervals": leaves,
        "intervals_requiring_local_prime_pairs": pair_leaves,
        "minimal_prime_pair_vectors": len(vectors),
        "minimum_certified_log_margin": str(minimum),
        "interval_partition_sha256": leaf_hash.hexdigest(),
        **({"exact_singleton_rows": exact_singletons,
            "certified_intervals": leaves - len(exact_singletons),
            "total_partition_leaves": leaves}
           if singleton_checker is not None else {}),
        "conclusion": "no bad triples",
    }


def inclusive_row_cap(i: int, primes: list[int], c: dict) -> tuple[int, int]:
    """A conservative cap, using the lower-row constants of the interval run.

    For n >= PAIR_THRESHOLD, the small-prime part U satisfies
    U <= 2**.913 * n**(s-.913) / [i]_S.  Compare this with the retained
    fat-point and symmetric discriminant lower bounds, with directed rounding.
    """
    if i not in ELIGIBLE:
        raise ValueError("the .913 bound has only been established here for i>=17")
    s = len(primes)
    divisor = 1 if all(i % p for p in primes) else i
    divisor_log_lo = intervals.log_bounds(divisor)[0] if divisor > 1 else Decimal(0)
    bounds = []
    with localcontext() as ctx:
        ctx.prec = intervals.PRECISION
        ctx.rounding = ROUND_CEILING
        upper_constant = PAIR_SAVING * intervals.log_bounds(2)[1] - divisor_log_lo
    for numerator, denominator, lower_constant in [
        (c["fat_exponent_numerator"], c["multiplicity"], c["fat_constant_lo"]),
        (i, 4, c["orbit_constant_lo"]),
    ]:
        with localcontext() as ctx:
            ctx.prec = intervals.PRECISION
            ctx.rounding = ROUND_FLOOR
            exponent_gap_lo = Decimal(numerator) / denominator - s + PAIR_SAVING
        if exponent_gap_lo > 0:
            with localcontext() as ctx:
                ctx.prec = intervals.PRECISION
                ctx.rounding = ROUND_CEILING
                bounds.append((upper_constant - lower_constant) / exponent_gap_lo)
    if not bounds:
        raise ValueError(f"no positive exponent gap at i={i}")
    with localcontext() as ctx:
        ctx.prec = intervals.PRECISION
        ctx.rounding = ROUND_CEILING
        bound = max(min(bounds), intervals.log_bounds(PAIR_THRESHOLD)[1])
        exponent = int((bound / intervals.log_bounds(10)[0]).to_integral_value(rounding=ROUND_CEILING))
    return 10**exponent, exponent


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--indices", type=int, nargs="+", default=[34, 31, 30, 28, 27])
    parser.add_argument("--max-nodes", type=int, default=1_500_000)
    parser.add_argument("--local-pairs", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    records = json.loads(intervals.GAP_DATA.read_text())["records"]
    primes = primes_through(max(args.indices))
    # Inject only the new uniform tail bound; leave the valuation and directed
    # interval certification code identical to the retained i>=35 certificate.
    intervals.inclusive_row_cap = inclusive_row_cap
    results = []
    for i in args.indices:
        lower = min(start for gap, start in records if gap > i)
        _, exponent = inclusive_row_cap(i, [p for p in primes if p < i], intervals.constants(i, lower))
        try:
            checker = check_index_with_pairs if args.local_pairs else intervals.check_index
            row = checker(i, primes, records, args.max_nodes)
        except RuntimeError as error:
            row = {
                "i": i,
                "terminal_prime_lower_row": lower,
                "inclusive_cap_power_of_ten": exponent,
                "conclusion": "interval proof incomplete",
                "reason": str(error),
            }
        row["local_prime_pairs"] = args.local_pairs
        results.append(row)
        print(json.dumps(row), flush=True)
    if args.output:
        args.output.write_text(json.dumps({
            "description": "Uniform row caps with an attempted interval exclusion; no row scan.",
            "prime_pair_saving": str(PAIR_SAVING),
            "prime_pair_threshold": PAIR_THRESHOLD,
            "max_nodes_per_index": args.max_nodes,
            "local_prime_pairs": args.local_pairs,
            "gap_data_file": intervals.GAP_DATA.name,
            "records": results,
        }, indent=2) + "\n")


if __name__ == "__main__":
    main()

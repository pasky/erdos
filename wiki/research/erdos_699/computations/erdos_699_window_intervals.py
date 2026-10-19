"""Interval certificates with the exact exceptional row windows of each edge.

The numerical tail is supplied from a separately proved theorem. Finite
prime-pair edges may have different exponents and height caps. An edge is
used only where its complete exception list proves that it holds throughout
the interval. Small exact checks are limited to unresolved singleton rows.
"""

from __future__ import annotations

import argparse
from bisect import bisect_right
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from fractions import Fraction
import hashlib
import json
from math import comb, gcd, log
from pathlib import Path
import sys

import erdos_699_further_intervals as previous
from erdos_699_effectivity import primes_through
from erdos_699_prime_pair_savings import EXPLICIT_EDGES, SCALE
from erdos_699_weighted_ramps import minimal_vectors


ordinary = previous.base.intervals
BFT_THRESHOLD = 1_771_595


def floor_root(n: int, degree: int) -> int:
    low, high = 0, 1 << ((n.bit_length() + degree - 1) // degree)
    while high - low > 1:
        middle = (low + high) // 2
        if middle ** degree <= n:
            low = middle
        else:
            high = middle
    return high if high ** degree <= n else low


def prepare_edge(row: dict, index: int) -> dict:
    if "cofactor_exponent_numerator" in row:
        target = Fraction(row["cofactor_exponent_numerator"], row["cofactor_exponent_denominator"])
    else:
        target = Fraction(1, row["reciprocal_exponent_denominator"])
    assert 0 < target < Fraction(1, 2)
    assert row["maximum_difference"] >= index - 1
    assert len(row["exceptions"]) == row["exception_count"]
    small_height = floor_root(row["maximum_difference"] ** target.denominator,
                              target.denominator - target.numerator) + 1
    windows = []
    for exception in row["exceptions"]:
        left = exception["larger_height"]
        right = exception["smaller_height"] + index - 1
        if left <= right:
            windows.append((left, right))
    merged = []
    for left, right in sorted(windows):
        if merged and left <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(right, merged[-1][1]))
        else:
            merged.append((left, right))
    return {
        "pair": tuple(row["pair"]),
        "weight": SCALE * target.numerator // target.denominator,
        "minimum_row": small_height + index - 1,
        "coarse_minimum_row": row["height_threshold"] + index - 1,
        "height_cap_power_of_ten": row["height_cap_power_of_ten"],
        "windows": merged,
        "starts": [left for left, _ in merged],
    }


def intersects(edge: dict, left: int, right: int) -> bool:
    candidate = bisect_right(edge["starts"], right) - 1
    return candidate >= 0 and edge["windows"][candidate][1] >= left


def run(index: int, tail_power: int, sources: list[Path], max_nodes: int,
        exact_limit: int) -> dict:
    primes = primes_through(index - 1)
    gaps = json.loads(ordinary.GAP_DATA.read_text())["records"]
    lower = min(start for gap, start in gaps if gap > index)
    constants = ordinary.constants(index, lower)
    edges = [prepare_edge(row, index)
             for path in sources for row in json.loads(path.read_text())["records"]
             if all(p < index for p in row["pair"])]
    if not edges:
        raise ValueError("no applicable finite prime-pair certificate")
    coarse_edges = [edge for edge in edges if edge["height_cap_power_of_ten"] >= tail_power]
    coarse_vectors = minimal_vectors(primes, EXPLICIT_EDGES + tuple(
        (*edge["pair"], edge["weight"]) for edge in coarse_edges))
    saving = min(map(sum, coarse_vectors))
    previous.CAPS[index] = tail_power
    previous.base.PAIR_THRESHOLD = max(
        BFT_THRESHOLD, max((e["coarse_minimum_row"] for e in coarse_edges), default=0))
    # The two historical fixed-cap cases are not targets of this generic tool.
    if index in (22, 25):
        raise ValueError("use the retained fixed-cap certificates for indices 22 and 25")
    cap, cap_power = previous.reduced_cap(index, primes, constants, saving)
    if cap_power > 10_000:
        raise RuntimeError("the analytic cap is still too large for this interval engine")
    for edge in edges:
        edge["maximum_row"] = (None if edge["height_cap_power_of_ten"] >= cap_power
                               else 10 ** edge["height_cap_power_of_ten"])
    basis_cache = {}

    def basis(left, right):
        weights = {(p, q): w for p, q, w in EXPLICIT_EDGES
                   if p < index and q < index and left >= BFT_THRESHOLD}
        for edge in edges:
            if (left >= edge["minimum_row"] and
                    (edge["maximum_row"] is None or right <= edge["maximum_row"]) and
                    not intersects(edge, left, right)):
                pair = edge["pair"]
                weights[pair] = max(weights.get(pair, 0), edge["weight"])
        key = tuple((p, q, w) for (p, q), w in sorted(weights.items()))
        if key not in basis_cache:
            vectors = minimal_vectors(primes, key)
            basis_cache[key] = (vectors, [tuple(v / SCALE for v in vector) for vector in vectors])
        return basis_cache[key]

    data = [(*row, [q for q, _ in row[3]])
            for row in ordinary.prime_power_data(index, cap, primes)]
    lower_logs = [ordinary.log_bounds(p)[0] for p in primes]
    valuations_i = [previous.base.prime_valuation(index, p) for p in primes]
    fat_exponent = constants["fat_exponent_numerator"] / constants["multiplicity"]
    fat_constant = float(constants["fat_constant_lo"])
    orbit_constant = float(constants["orbit_constant_lo"])
    stack = [(lower, cap)]
    visited = leaves = pair_leaves = exact_columns = 0
    minimum = Decimal("Infinity")
    partition_hash = hashlib.sha256()
    exact_rows = []

    while stack:
        left, right = stack.pop()
        visited += 1
        if visited > max_nodes:
            raise RuntimeError(f"node budget exhausted at [{left},{right}]; proof incomplete")
        if visited % 100_000 == 0:
            print(f"i={index}: {visited} intervals visited; current lower endpoint {left}", file=sys.stderr, flush=True)
        counts = previous.fast_valuation_upper_counts(left, right, data)
        individual = [count * row[1] for count, row in zip(counts, data)]
        guide_lower = max(fat_exponent * log(left) + fat_constant,
                          index / 4 * log(left) + orbit_constant)
        margin = Decimal(0)
        used_pair = False
        if guide_lower > sum(individual):
            margin = ordinary.certified_margin(index, left, counts, data, constants)
        else:
            vectors, float_vectors = basis(left, right)
            log_right, log_base = log(right), log(left - index + 1)
            guide_upper = max(sum(min(individual[k], log_right - weight * log_base
                                      - valuations_i[k] * data[k][1])
                                  for k, weight in enumerate(vector))
                              for vector in float_vectors)
            if guide_lower > guide_upper:
                right_hi = ordinary.log_bounds(right)[1]
                base_lo = ordinary.log_bounds(left - index + 1)[0]
                left_lo = ordinary.log_bounds(left)[0]
                with localcontext() as context:
                    context.prec = ordinary.PRECISION
                    context.rounding = ROUND_FLOOR
                    deductions = [[Decimal(weight) * base_lo / SCALE + valuations_i[k] * lower_logs[k]
                                   for k, weight in enumerate(vector)] for vector in vectors]
                with localcontext() as context:
                    context.prec = ordinary.PRECISION
                    context.rounding = ROUND_CEILING
                    ordinary_upper = [count * row[2] for count, row in zip(counts, data)]
                    upper = max(sum((min(ordinary_upper[k], right_hi - deduction)
                                     for k, deduction in enumerate(vector)), Decimal(0))
                                for vector in deductions)
                with localcontext() as context:
                    context.prec = ordinary.PRECISION
                    context.rounding = ROUND_FLOOR
                    fat = constants["fat_exponent_numerator"] * left_lo / constants["multiplicity"] + constants["fat_constant_lo"]
                    orbit = index * left_lo / 4 + constants["orbit_constant_lo"]
                    margin = max(fat, orbit) - upper
                used_pair = margin > 0
        if margin > 0:
            leaves += 1
            pair_leaves += used_pair
            minimum = min(minimum, margin)
            partition_hash.update(f"{left}:{right}\n".encode())
            continue
        if left == right:
            if left > exact_limit:
                raise RuntimeError(f"unexcluded singleton n={left}; proof incomplete")
            fixed, current = comb(left, index), 1
            for j in range(1, left // 2 + 1):
                current = current * (left - j + 1) // j
                if j <= index:
                    continue
                common = gcd(fixed, current)
                for p in primes:
                    while common % p == 0:
                        common //= p
                assert common > 1, f"Bad triple found: {(left, index, j)}"
                exact_columns += 1
            exact_rows.append(left)
            partition_hash.update(f"{left}:{right}\n".encode())
            continue
        middle = (left + right) // 2
        stack.extend([(left, middle), (middle + 1, right)])
    return {
        "i": index, "supplied_tail_power_of_ten": tail_power,
        "inclusive_interval_cap_power_of_ten": cap_power,
        "terminal_prime_lower_row": lower, "coarse_cofactor_saving_scaled": saving,
        "visited_intervals": visited, "certified_intervals": leaves,
        "intervals_requiring_prime_pairs": pair_leaves,
        "total_partition_leaves": leaves + len(exact_rows),
        "minimum_certified_log_margin": str(minimum),
        "interval_partition_sha256": partition_hash.hexdigest(),
        "active_cofactor_graphs_used": len(basis_cache),
        "finite_pair_constraints": len(edges),
        "exceptional_row_windows": sum(len(edge["windows"]) for edge in edges),
        "exact_singleton_rows": exact_rows, "exact_columns_checked": exact_columns,
        "source_certificates": [{"file": str(path)} for path in sources],
        "gap_data_file": ordinary.GAP_DATA.name,
        "conclusion": "All rows are excluded under the separately supplied numerical tail theorem.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", type=int, required=True)
    parser.add_argument("--tail-power", type=int, required=True)
    parser.add_argument("--pair-certificate", type=Path, nargs="+", required=True)
    parser.add_argument("--max-nodes", type=int, default=2_000_000)
    parser.add_argument("--exact-singleton-limit", type=int, default=10_000)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run(args.index, args.tail_power, args.pair_certificate,
                 args.max_nodes, args.exact_singleton_limit)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

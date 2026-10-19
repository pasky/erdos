# evidence: entry manual
"""Seek low-cost witnesses of the aggregated carry criterion by lattice reduction.

Optional discovery dependency: fpylll. For each order k, leading coefficient c
and support endpoint R, the columns n=k..R carry the pair (Phi_n mod 2^k,
U_k(n)); an embedded lattice forces both aggregated conditions and LLL/BKZ
propose short weighted vectors. Every proposal is checked in exact integer
arithmetic before output, and up to eight exact improving passes along
retained kernel directions follow. No minimum-cost property is claimed; the
independent consumer is carry.py.
"""

from __future__ import annotations

import argparse
import json
import time
from fractions import Fraction
from pathlib import Path

from fpylll import BKZ, LLL, IntegerMatrix

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / 'output'
ORDERS = (16, 24, 32, 48, 64, 96, 128)


def sieve(limit: int) -> list[int]:
    """Return the totients 0..limit by the multiplicative sieve."""
    phi = list(range(limit + 1))
    for p in range(2, limit + 1):
        if phi[p] == p:
            for m in range(p, limit + 1, p):
                phi[m] -= phi[m] // p
    return phi


def partial_sums(phi: list[int]) -> list[int]:
    """Return Phi_n = 2 Phi_(n-1) + phi(n) for every n up to the sieve limit."""
    result = [0] * len(phi)
    for n in range(1, len(phi)):
        result[n] = 2 * result[n - 1] + phi[n]
    return result


def weighted_cost(y: dict[int, int], k: int, c: int) -> int:
    """Return |c|(k+2) + sum |y_n| (n+k+2)."""
    return abs(c) * (k + 2) + sum(abs(v) * (n + k + 2) for n, v in y.items())


def satisfies(y: dict[int, int], k: int, c: int, Phi: list[int]) -> bool:
    """Check both aggregated conditions exactly."""
    v = sum(value * Phi[n] for n, value in y.items())
    W = c * Phi[k] + sum(
        value * (Phi[n + k] - (1 << k) * Phi[n]) for n, value in y.items()
    )
    return v % (1 << k) == 0 and W == 0 and min(y) >= k


def improve_l1(y: list[int], basis: list[list[int]], weights: list[int]) -> list[int]:
    """Make up to eight exact improving passes along retained kernel vectors."""

    def cost(vector: list[int]) -> int:
        return sum(abs(value) * weight for value, weight in zip(vector, weights))

    current = cost(y)
    for _ in range(8):
        improved = False
        for row in basis:
            # A weighted median minimizes sum w_i |y_i + a row_i| over real a.
            knots = sorted(
                (Fraction(-value, direction), weight * abs(direction))
                for value, direction, weight in zip(y, row, weights)
                if direction
            )
            if not knots:
                continue
            total = sum(weight for _, weight in knots)
            cumulative = 0
            lower = 0
            for knot, weight in knots:
                cumulative += weight
                if 2 * cumulative >= total:
                    lower = knot.numerator // knot.denominator
                    break
            for multiple in (lower, lower + 1):
                if multiple == 0:
                    continue
                candidate = [
                    value + multiple * direction for value, direction in zip(y, row)
                ]
                candidate_cost = cost(candidate)
                if candidate_cost < current:
                    y, current, improved = candidate, candidate_cost, True
        if not improved:
            break
    return y


def reduce_order(k: int, c: int, R: int, block: int, Phi: list[int]) -> dict | None:
    """Reduce one embedded lattice and return the best exactly checked witness."""
    indices = list(range(k, R + 1))
    M = len(indices)
    weights = [n + k + 2 for n in indices]
    modulus = 1 << k
    scale = 1 << (k + 80)
    marker = R * M
    columns = M + 3
    rows = []
    for i, n in enumerate(indices):
        row = [0] * columns
        row[i] = weights[i]
        row[M] = scale * (Phi[n] % modulus)
        row[M + 1] = scale * (Phi[n + k] - modulus * Phi[n])
        rows.append(row)
    row = [0] * columns
    row[M] = scale * modulus
    rows.append(row)
    row = [0] * columns
    row[M + 1] = scale * c * Phi[k]
    row[M + 2] = marker
    rows.append(row)
    matrix = IntegerMatrix.from_matrix(rows)
    LLL.reduction(matrix)
    if block:
        BKZ.reduction(matrix, BKZ.Param(block_size=block))
    kernel = []
    witnesses = []
    for i in range(matrix.nrows):
        vector = [matrix[i, j] for j in range(columns)]
        if vector[M] or vector[M + 1]:
            continue
        coefficients = [value // weight for value, weight in zip(vector[:M], weights)]
        if any(value % weight for value, weight in zip(vector[:M], weights)):
            continue
        if vector[M + 2] == 0:
            kernel.append(coefficients)
        elif abs(vector[M + 2]) == marker:
            sign = 1 if vector[M + 2] > 0 else -1
            witnesses.append([sign * value for value in coefficients])
    best = None
    for candidate in witnesses:
        candidate = improve_l1(candidate, kernel, weights)
        y = {n: value for n, value in zip(indices, candidate) if value}
        if not y or not satisfies(y, k, c, Phi):
            continue
        cost = weighted_cost(y, k, c)
        if best is None or cost < best['cost']:
            best = {
                'k': k,
                'c': c,
                'R': R,
                'method': f'lll_bkz{block}_R{R}',
                'coefficients': sorted([n, value] for n, value in y.items()),
                'cost': cost,
            }
    return best


def main() -> int:
    """Run the reductions and write candidate witnesses to ignored output."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--orders', type=int, nargs='+', default=list(ORDERS))
    parser.add_argument('--factors', type=int, nargs='+', default=[2, 3, 4])
    parser.add_argument('--leading', type=int, nargs='+', default=[1, 2])
    parser.add_argument('--block', type=int, default=20)
    parser.add_argument('--out', type=Path, default=OUTPUT / 'carry_candidates.json')
    args = parser.parse_args()
    limit = 2 * max(args.orders) * (max(args.factors) + 2) + 8
    phi = sieve(limit)
    Phi = partial_sums(phi)
    results = []
    for k in args.orders:
        for c in args.leading:
            for factor in args.factors:
                R = factor * k + 2
                started = time.time()
                best = reduce_order(k, c, R, args.block, Phi)
                elapsed = time.time() - started
                if best is None:
                    print(f'k={k} c={c} R={R}: no checked witness ({elapsed:.1f}s)')
                    continue
                best['seconds'] = round(elapsed, 1)
                results.append(best)
                print(
                    f'k={k} c={c} R={R}: cost {best["cost"]} '
                    f'ratio {best["cost"] / 2**k:.3g} support {len(best["coefficients"])} '
                    f'max|y| {max(abs(v) for _, v in best["coefficients"])} ({elapsed:.1f}s)',
                    flush=True,
                )
    args.out.parent.mkdir(exist_ok=True)
    args.out.write_text(json.dumps(results, indent=1))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

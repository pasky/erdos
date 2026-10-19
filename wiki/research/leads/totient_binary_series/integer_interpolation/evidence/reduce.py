# evidence: entry manual
"""Seek lower-cost integer solutions in the exact interpolation coset.

Optional discovery dependencies: python-flint and fpylll. HNF supplies one
solution and an integer kernel basis. Weighted LLL and MPFR nearest-plane
proposals choose integer kernel combinations; all equations are checked in
exact arithmetic before candidate output. No shortest-vector or minimum-cost
property is claimed. main.py is the independent, dependency-light consumer.
"""

from __future__ import annotations

import argparse
import gzip
import json
import time
from fractions import Fraction
from pathlib import Path

from flint import ctx, fmpz_mat
from fpylll import FPLLL, GSO, IntegerMatrix

from produce import (
    CAP,
    ORDERS,
    full_image,
    matrix,
    sieve,
    solution_record,
    write_certificate,
)


def weighted_cost(y: list[int], weights: list[int]) -> int:
    """Return the variable part of the exact tail cost."""
    return sum(abs(value) * weight for value, weight in zip(y, weights))


def improve_l1(y: list[int], basis: list[list[int]], weights: list[int]) -> list[int]:
    """Make up to eight exact improving passes along retained kernel vectors."""
    cost = weighted_cost(y, weights)
    for _ in range(8):
        improved = False
        for row in basis:
            # A weighted median minimizes sum w_i |y_i + a row_i| over real a.
            knots = sorted(
                (Fraction(-value, direction), weight * abs(direction))
                for value, direction, weight in zip(y, row, weights)
                if direction
            )
            total = sum(weight for _, weight in knots)
            cumulative = 0
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
                candidate_cost = weighted_cost(candidate, weights)
                if candidate_cost < cost:
                    y, cost = candidate, candidate_cost
                    improved = True
                    break
        if not improved:
            break
    return y


def reduce_solution(k: int, endpoint: int, phi: list[int]) -> dict:
    """Reduce one exact affine lattice at a declared support endpoint."""
    started = time.monotonic()
    m = matrix(k, endpoint, phi)
    h, transform = m.hnf(transform=True)
    if transform * m != h or not full_image(h, 2 * k):
        raise ValueError('support does not have a checked full-image transform')
    target = [0 if s <= 0 else -phi[s] for s in range(1 - k, k + 1)]
    y = [
        sum(int(transform[j, i]) * target[j] for j in range(2 * k))
        for i in range(m.nrows())
    ]
    weights = [n + k + 2 for n in range(k + 2, endpoint + 1)]
    weighted = fmpz_mat(
        [
            [transform[i, j] * weights[j] for j in range(m.nrows())]
            for i in range(2 * k, m.nrows())
        ]
    )
    print(
        f'k={k}, R={endpoint}: reducing kernel of rank {weighted.nrows()}', flush=True
    )
    reduced = weighted.lll()
    rows = [
        [int(reduced[i, j]) for j in range(reduced.ncols())]
        for i in range(reduced.nrows())
    ]
    if any(value % weight for row in rows for value, weight in zip(row, weights)):
        raise ValueError('weighted lattice lost integral coordinates')
    kernel = [[value // weight for value, weight in zip(row, weights)] for row in rows]
    if fmpz_mat(kernel) * m != fmpz_mat(len(kernel), 2 * k):
        raise ValueError('reduced rows are not in the exact integer kernel')
    # High precision affects discovery quality only, never acceptance.
    weighted_target = [value * weight for value, weight in zip(y, weights)]
    precision = max(
        128, max(abs(value).bit_length() for value in weighted_target) + 128
    )
    FPLLL.set_precision(precision)
    gram = GSO.Mat(
        IntegerMatrix.from_matrix(rows), float_type='mpfr', flags=GSO.INT_GRAM
    )
    gram.update_gso()
    multiples = gram.babai(weighted_target)
    y = [
        value - sum(int(a) * row[i] for a, row in zip(multiples, kernel))
        for i, value in enumerate(y)
    ]
    y = improve_l1(y, kernel, weights)
    if fmpz_mat([y]) * m != fmpz_mat([target]):
        raise ValueError('coset reduction changed the exact target')
    record = solution_record(k, endpoint, y, f'coset_R{endpoint}')
    print(
        f'k={k}, R={endpoint}: C={record["cost"]}, '
        f'max|y|={record["max_abs_coefficient"]}, '
        f'elapsed={time.monotonic() - started:.3f}s',
        flush=True,
    )
    return record


def main() -> None:
    """Append candidate reductions to existing certificates in ignored output."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--orders', type=int, nargs='+', choices=ORDERS, default=ORDERS)
    parser.add_argument(
        '--factors',
        type=int,
        nargs='+',
        default=[4, 6, 8],
        help='support endpoints factor*k+2, all at most 4096',
    )
    parser.add_argument(
        '--output', type=Path, default=Path(__file__).resolve().parent / 'output'
    )
    args = parser.parse_args()
    if any(
        factor < 4 or factor * max(args.orders) + 2 > CAP for factor in args.factors
    ):
        parser.error('support factors must give endpoints between 4k+2 and 4096')
    ctx.threads = 1
    FPLLL.set_threads(1)
    phi = sieve(CAP + max(ORDERS))
    for k in args.orders:
        path = args.output / f'k{k:03d}.json.gz'
        with gzip.open(path, 'rt') as stream:
            certificate = json.load(stream)
        for factor in args.factors:
            solution = reduce_solution(k, factor * k + 2, phi)
            certificate['solutions'] = [
                item
                for item in certificate['solutions']
                if item['label'] != solution['label']
            ]
            certificate['solutions'].append(solution)
            write_certificate(path, certificate)


if __name__ == '__main__':
    main()

"""Discover exact interpolation certificates using optional python-flint.

This producer is not the acceptance checker. It writes candidates to ignored
output/ by default; main.py replays accepted assets with Python integers alone.
Hermite transforms construct witnesses, but their names or library verdicts
have no standing without those replayed relations. See computation.md.
"""

from __future__ import annotations

import argparse
import gzip
import json
import math
import time
from fractions import Fraction
from pathlib import Path

from flint import ctx, fmpz_mat

ORDERS = (3, 4, 8, 12, 16, 24, 32, 48, 64)
CAP = 4096


def sieve(limit: int) -> list[int]:
    """Compute discovery totients by a sieve, separate from the checker."""
    phi = list(range(limit + 1))
    for p in range(2, limit + 1):
        if phi[p] == p:
            for n in range(p, limit + 1, p):
                phi[n] -= phi[n] // p
    return phi


def matrix(k: int, endpoint: int, phi: list[int]) -> fmpz_mat:
    """Return A_R transposed; row n is one normalized totient column."""
    return fmpz_mat(
        [
            [phi[n + s] // 2 for s in range(1 - k, k + 1)]
            for n in range(k + 2, endpoint + 1)
        ]
    )


def full_image(h: fmpz_mat, dimension: int) -> bool:
    """Use HNF only for discovery; the retained relation is checked separately."""
    return h.nrows() >= dimension and all(
        h[i, j] == int(i == j) for i in range(dimension) for j in range(dimension)
    )


def first_endpoint(k: int, phi: list[int]) -> int | None:
    """Bracket and bisect monotone full-image prefixes inside the fixed cap."""
    lower = 3 * k
    upper = lower + 1
    while not full_image(matrix(k, upper, phi).hnf(), 2 * k):
        print(f'k={k}: HNF discovery proper at R={upper}', flush=True)
        lower = upper
        if upper == CAP:
            return None
        upper = min(CAP, 2 * upper - (k + 2) + 1)
    while lower + 1 < upper:
        middle = (lower + upper) // 2
        if full_image(matrix(k, middle, phi).hnf(), 2 * k):
            upper = middle
        else:
            lower = middle
    return upper


def modular_nullvector(rows: list[list[int]], p: int, dimension: int) -> list[int]:
    """Find a nonzero vector in the right nullspace modulo the prime p."""
    pivots = {}
    for original in rows:
        row = [value % p for value in original]
        for pivot, basis in sorted(pivots.items()):
            factor = row[pivot]
            if factor:
                row = [(x - factor * y) % p for x, y in zip(row, basis)]
        pivot = next((i for i, value in enumerate(row) if value), None)
        if pivot is not None:
            inverse = pow(row[pivot], -1, p)
            pivots[pivot] = [value * inverse % p for value in row]
    free = next((i for i in range(dimension) if i not in pivots), None)
    if free is None:
        raise ValueError('no modular obstruction for chosen prime')
    result = [0] * dimension
    result[free] = 1
    for pivot, row in sorted(pivots.items(), reverse=True):
        result[pivot] = (
            -sum(row[j] * result[j] for j in range(pivot + 1, dimension)) % p
        )
    return result


def annihilator(k: int, endpoint: int, phi: list[int]) -> dict:
    """Construct a proper-image certificate, then check it over the full prefix."""
    m = matrix(k, endpoint, phi)
    h = m.hnf()
    rows = [[int(m[i, j]) for j in range(2 * k)] for i in range(m.nrows())]
    if h.nrows() >= 2 * k and all(h[i, i] != 0 for i in range(2 * k)):
        basis = fmpz_mat([[h[i, j] for j in range(2 * k)] for i in range(2 * k)])
        dual = basis.inv()
        column = next(
            (
                j
                for j in range(2 * k)
                if any(dual[i, j].denominator != 1 for i in range(2 * k))
            ),
            None,
        )
        if column is None:
            raise ValueError('requested obstruction for a full image')
        modulus = math.lcm(*(int(dual[i, column].denominator) for i in range(2 * k)))
        row = [int(dual[i, column] * modulus) % modulus for i in range(2 * k)]
    else:
        modulus = 2
        row = modular_nullvector(rows, modulus, 2 * k)
    if not any(row) or any(
        sum(a * b for a, b in zip(row, column)) % modulus for column in rows
    ):
        raise ValueError('constructed obstruction is invalid')
    return {'R': endpoint, 'modulus': modulus, 'row': row}


def solution_record(k: int, endpoint: int, y: list[int], label: str) -> dict:
    """Record exact sparse coefficients and candidate metadata for replay."""
    pairs = [[n, value] for n, value in enumerate(y, start=k + 2) if value]
    cost = 2 * (k + 2) + sum(abs(value) * (n + k + 2) for n, value in pairs)
    ratio = Fraction(cost, 1 << k)
    return {
        'label': label,
        'R': endpoint,
        'coefficients': pairs,
        'cost': cost,
        'max_abs_coefficient': max(abs(value) for _, value in pairs),
        'support': [pairs[0][0], pairs[-1][0], len(pairs)],
        'ratio': [ratio.numerator, ratio.denominator],
        'excluded_denominators_through': ((1 << k) - 1) // cost,
    }


def produce(k: int, phi: list[int]) -> dict:
    """Construct endpoint, obstruction, and a first inhomogeneous witness."""
    started = time.monotonic()
    endpoint = first_endpoint(k, phi)
    if endpoint is None:
        raise ValueError(f'k={k}: proper at cap; retain obstruction before proceeding')
    print(f'k={k}: first full-image candidate R={endpoint}', flush=True)
    m = matrix(k, endpoint, phi)
    h, transform = m.hnf(transform=True)
    if transform * m != h or not full_image(h, 2 * k):
        raise ValueError('invalid HNF transform')
    inverse = [[int(transform[j, i]) for j in range(2 * k)] for i in range(m.nrows())]
    target = [0 if s <= 0 else -phi[s] for s in range(1 - k, k + 1)]
    y = [sum(a * b for a, b in zip(row, target)) for row in inverse]
    certificate = {
        'schema': 1,
        'k': k,
        'B': k + 2,
        'cap': CAP,
        'shifts': list(range(1 - k, k + 1)),
        'status': 'full_image',
        'minimal_R': endpoint,
        'right_inverse': inverse,
        'predecessor': annihilator(k, endpoint - 1, phi),
        'solutions': [solution_record(k, endpoint, y, 'right_inverse')],
    }
    print(
        f'k={k}: constructed in {time.monotonic() - started:.3f}s; '
        f'initial C={certificate["solutions"][0]["cost"]}',
        flush=True,
    )
    return certificate


def write_certificate(path: Path, certificate: dict) -> None:
    """Write deterministic gzip bytes with no embedded timestamp or filename."""
    data = (json.dumps(certificate, separators=(',', ':')) + '\n').encode()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(gzip.compress(data, mtime=0))


def main() -> None:
    """Run a selected finite discovery workload on one numerical thread."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--orders', type=int, nargs='+', choices=ORDERS, default=ORDERS)
    parser.add_argument(
        '--output', type=Path, default=Path(__file__).resolve().parent / 'output'
    )
    args = parser.parse_args()
    ctx.threads = 1
    phi = sieve(CAP + max(ORDERS))
    for k in args.orders:
        write_certificate(args.output / f'k{k:03d}.json.gz', produce(k, phi))


if __name__ == '__main__':
    main()

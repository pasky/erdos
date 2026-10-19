"""Replay exact witnesses of the aggregated carry criterion.

Each retained witness is a leading coefficient c and finitely supported
integers y_n, n >= k, and must satisfy the two aggregated conditions of the
owning carry_criterion page exactly: sum y_n Phi_n == 0 (mod 2^k) and
c Phi_k + sum y_n (Phi_(n+k) - 2^k Phi_n) == 0. The cost
|c|(k+2) + sum |y_n| (n+k+2) is recomputed from the coefficients. The
default replays every witness in assets/carry_witnesses.json; --quick
replays only k <= 8; --box-minima additionally re-derives every declared
exhaustive box minimum by enumeration (minutes). Python integers and the
standard library perform every mathematical check; tools supplies reporting.
The required collection has thirteen specified boxes and twenty lattice
witnesses. Missing witnesses or changed box specifications fail acceptance,
including before the reduced --quick mathematical replay.
"""

from __future__ import annotations

import itertools
import json
import math
import sys
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

from tools import Checker, evidence_parser

ASSETS = Path(__file__).resolve().parent / 'assets' / 'carry_witnesses.json'
QUICK_LIMIT = 8
BOXES = {
    (3, 2): (10, 1),
    (4, 2): (14, 2),
    (5, 2): (16, 2),
    (6, 2): (16, 2),
    (8, 2): (18, 2),
    (10, 2): (22, 1),
    (12, 2): (24, 1),
    (14, 2): (26, 1),
    (16, 2): (28, 1),
    (4, 1): (10, 1),
    (5, 1): (12, 1),
    (6, 1): (14, 1),
    (8, 1): (18, 1),
}
LATTICE_ORDERS = (16, 24, 32, 48, 64, 96, 128, 192, 256, 384)


def require(condition: bool, message: str) -> None:
    """Reject a failed obligation even when Python optimization is enabled."""
    if not condition:
        raise ValueError(message)


def integer(value: object, message: str) -> int:
    """Require an actual integer, excluding booleans and decimal coercion."""
    require(type(value) is int, message)
    return value


def totient(n: int) -> int:
    """Compute one totient by trial division, independently of discovery."""
    require(n >= 1, 'totient argument must be positive')
    result = n
    divisor = 2
    remaining = n
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            result -= result // divisor
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        result -= result // remaining
    return result


def partial_sums(limit: int) -> list[int]:
    """Return Phi_0..Phi_limit from the recurrence Phi_n = 2 Phi_(n-1) + phi(n)."""
    result = [0] * (limit + 1)
    for n in range(1, limit + 1):
        result[n] = 2 * result[n - 1] + totient(n)
    return result


def check_roster(witnesses: list[dict]) -> None:
    """Require the full mathematical domain and the declared enumeration boxes."""
    expected = {('exhaustive', k, c) for k, c in BOXES}
    expected.update(('lattice', k, c) for k in LATTICE_ORDERS for c in (1, 2))
    keys = []
    for witness in witnesses:
        require(type(witness) is dict, 'witness must be an object')
        method = witness['method']
        require(type(method) is str, 'witness method')
        k = integer(witness['k'], 'order')
        c = integer(witness['c'], 'leading coefficient')
        require(c != 0, 'leading coefficient must be nonzero')
        key = (method, k, c)
        require(key in expected, 'unexpected witness specification')
        require(key not in keys, 'duplicate witness specification')
        keys.append(key)
        box = witness.get('box')
        if method == 'exhaustive':
            require(type(box) is dict, 'missing enumeration box')
            actual = (
                integer(box['M'], 'box length'),
                integer(box['h'], 'box height'),
            )
            require(actual == BOXES[k, c], 'wrong declared box specification')
        else:
            require(box is None, 'lattice witness has an unexpected enumeration box')
    require(set(keys) == expected, 'missing witness specification')


def unique_object(pairs: list) -> dict:
    """Reject ambiguous duplicate JSON keys."""
    result = {}
    for key, value in pairs:
        require(key not in result, f'duplicate JSON key: {key}')
        result[key] = value
    return result


def aggregates(
    k: int, c: int, y: list[list[int]], Phi: list[int]
) -> tuple[int, int, int]:
    """Return (v mod 2^k centered, W, C) for a leading coefficient and support."""
    modulus = 1 << k
    v = sum(value * Phi[n] for n, value in y)
    W = c * Phi[k] + sum(value * (Phi[n + k] - modulus * Phi[n]) for n, value in y)
    C = abs(c) * (k + 2) + sum(abs(value) * (n + k + 2) for n, value in y)
    residue = v % modulus
    if residue > modulus // 2:
        residue -= modulus
    return residue, W, C


def check_witness(data: dict, Phi: list[int]) -> dict:
    """Check both aggregated conditions and every recomputed statistic."""
    require(type(data) is dict, 'witness must be an object')
    require(type(data['label']) is str and bool(data['label']), 'witness label')
    k = integer(data['k'], 'order k')
    require(k >= 3, 'order must be at least three')
    c = integer(data['c'], 'leading coefficient')
    require(c != 0, 'leading coefficient must be nonzero')
    coefficients = data['coefficients']
    require(type(coefficients) is list and bool(coefficients), 'empty witness')
    previous = k - 1
    for pair in coefficients:
        require(type(pair) is list and len(pair) == 2, 'coefficient pair')
        n = integer(pair[0], 'support index')
        value = integer(pair[1], 'coefficient')
        require(previous < n, 'unsorted, repeated, or invalid support')
        require(value != 0, 'sparse support contains zero')
        previous = n
    require(previous + k < len(Phi), 'support exceeds the prepared table')
    residue, W, C = aggregates(k, c, coefficients, Phi)
    require(residue == 0, f'v is not divisible by 2^k (centred residue {residue})')
    require(W == 0, f'aggregated tail integer W={W} is not zero')
    modulus = 1 << k
    require(k <= 8 or modulus > C, 'cost reaches 2^k at an order above eight')
    ratio = Fraction(C, modulus)
    expected = {
        'cost': C,
        'max_abs_coefficient': max(abs(value) for _, value in coefficients),
        'support': [coefficients[0][0], coefficients[-1][0], len(coefficients)],
        'ratio': [ratio.numerator, ratio.denominator],
        'excluded_denominators_through': ((1 << k) - 1) // C,
    }
    # Check types as well as equality: JSON booleans are not integer witnesses.
    for key in ('cost', 'max_abs_coefficient', 'excluded_denominators_through'):
        integer(data[key], f'witness {key}')
    for key in ('support', 'ratio'):
        require(type(data[key]) is list, f'witness {key} array')
        for value in data[key]:
            integer(value, f'witness {key} entry')
    for key, value in expected.items():
        require(data[key] == value, f'wrong recomputed witness {key}')
    return {'label': data['label'], 'k': k, 'c': c, **expected}


def box_minimum(k: int, c: int, M: int, h: int, Phi: list[int]) -> int | None:
    """Return the least cost over |y_n| <= h on k <= n < k+M, or None if empty."""
    indices = list(range(k, k + M))
    modulus = 1 << k
    U = {n: Phi[n + k] - modulus * Phi[n] for n in indices}
    weights = {n: n + k + 2 for n in indices}
    half = M // 2
    left, right = indices[:half], indices[half:]
    values = range(-h, h + 1)

    def enumerate_half(ns: list[int]) -> list[tuple[int, int, int]]:
        out = []
        for ys in itertools.product(values, repeat=len(ns)):
            v = sum(y * Phi[n] for y, n in zip(ys, ns)) % modulus
            W = sum(y * U[n] for y, n in zip(ys, ns))
            cost = sum(abs(y) * weights[n] for y, n in zip(ys, ns))
            out.append((v, W, cost))
        return out

    table: dict[tuple[int, int], int] = defaultdict(lambda: None)
    for v, W, cost in enumerate_half(right):
        if table[(v, W)] is None or cost < table[(v, W)]:
            table[(v, W)] = cost
    best = None
    for v, W, cost in enumerate_half(left):
        other = table.get(((-v) % modulus, -(W + c * Phi[k])))
        if other is not None:
            total = abs(c) * (k + 2) + cost + other
            if best is None or total < best:
                best = total
    return best


def main() -> int:
    """Replay the declared witnesses; missing or corrupt inputs fail nonzero."""
    parser = evidence_parser(__doc__)
    parser.add_argument('--assets', type=Path, default=ASSETS, help='witness file')
    parser.add_argument(
        '--box-minima',
        action='store_true',
        help='re-derive every declared exhaustive box minimum by enumeration',
    )
    args = parser.parse_args()
    checker = Checker()
    print(
        'Aggregated carry criterion witnesses: exact replay of v = 0 (mod 2^k), '
        'W = 0 and the weighted cost; finite results only, no minimum-cost or '
        'asymptotic claim beyond any declared enumeration box.'
    )
    try:
        with open(args.assets, encoding='utf-8') as stream:
            data = json.load(stream, object_pairs_hook=unique_object)
        require(type(data) is dict, 'asset must be an object')
        require(integer(data['schema'], 'schema') == 1, 'unsupported schema')
        witnesses = data['witnesses']
        require(type(witnesses) is list and bool(witnesses), 'no witnesses')
        check_roster(witnesses)
        checker.check('complete witness roster and declared enumeration boxes', True)
        limit = max(
            integer(w['k'], 'order')
            + max(integer(p[0], 'index') for p in w['coefficients'])
            for w in witnesses
        )
        Phi = partial_sums(limit + 2)
        for n in (1, 2, 3, 4, 5, 8, 9, 16, 65, 66, limit):
            counted = sum(math.gcd(n, j) == 1 for j in range(1, n + 1))
            require(totient(n) == counted, f'totient counting control at {n}')
        checker.check('small and boundary totients agree with coprime counts', True)
    except (OSError, ValueError, KeyError, TypeError) as error:
        checker.check('witness file acceptance', False, str(error))
        return checker.finish()
    labels = set()
    for witness in witnesses:
        try:
            k = integer(witness['k'], 'order')
            if args.quick and k > QUICK_LIMIT:
                continue
            summary = check_witness(witness, Phi)
            require(summary['label'] not in labels, 'duplicate witness label')
            labels.add(summary['label'])
            checker.check(
                f'k={k} c={summary["c"]} {summary["label"]}: v, W, support, exact cost',
                True,
            )
            print(
                f'    C={summary["cost"]}, ratio={Fraction(*summary["ratio"])}, '
                f'support={summary["support"]}, max|y|={summary["max_abs_coefficient"]}, '
                f'denominators excluded through {summary["excluded_denominators_through"]}'
            )
            box = witness.get('box')
            if box is not None:
                M = integer(box['M'], 'box length')
                h = integer(box['h'], 'box height')
                require(
                    all(
                        abs(value) <= h and n < k + M
                        for n, value in witness['coefficients']
                    ),
                    'witness lies outside its declared box',
                )
                if args.box_minima:
                    minimum = box_minimum(k, summary['c'], M, h, Phi)
                    require(minimum == summary['cost'], f'box minimum is {minimum}')
                    checker.check(f'k={k}: exhaustive box minimum M={M}, h={h}', True)
        except (ValueError, KeyError, TypeError) as error:
            label = witness.get('label', '?') if type(witness) is dict else '?'
            checker.check(f'witness {label} acceptance', False, str(error))
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

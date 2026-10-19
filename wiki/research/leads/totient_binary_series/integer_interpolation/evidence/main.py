"""Replay finite integer-image and inhomogeneous totient certificates.

The default checks every commissioned k; --quick checks only k=3,4. Inputs
are the JSON gzip files in assets, resolved relative to this file. Python
integers and the standard library perform every mathematical check; tools
supplies reporting only. Discovery packages are not imported. See the owning
computation.md for the schema, coverage semantics, commands, and limitations.
"""

from __future__ import annotations

import gzip
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

from tools import Checker, evidence_parser

ORDERS = (3, 4, 8, 12, 16, 24, 32, 48, 64)
CAP = 4096
ASSETS = Path(__file__).resolve().parent / 'assets'


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


def unique_object(pairs: list) -> dict:
    """Reject ambiguous duplicate JSON keys."""
    result = {}
    for key, value in pairs:
        require(key not in result, f'duplicate JSON key: {key}')
        result[key] = value
    return result


def read_certificate(path: Path) -> dict:
    """Read exact certificate data; there is no cached-verdict field."""
    with gzip.open(path, 'rt', encoding='utf-8') as stream:
        result = json.load(stream, object_pairs_hook=unique_object)
    require(type(result) is dict, 'certificate must be an object')
    return result


def check_annihilator(data: dict, k: int, endpoint: int, phi: list[int]) -> None:
    """Check a nontrivial homomorphism vanishing on every prefix column."""
    require(type(data) is dict, 'annihilator must be an object')
    require(
        integer(data['R'], 'annihilator R') == endpoint,
        'annihilator is not at the required endpoint',
    )
    modulus = integer(data['modulus'], 'annihilator modulus')
    require(modulus >= 2, 'annihilator modulus must be at least two')
    row = data['row']
    require(type(row) is list and len(row) == 2 * k, 'annihilator row dimension')
    for value in row:
        integer(value, 'annihilator entry')
    require(any(value % modulus for value in row), 'zero modular annihilator')
    for n in range(k + 2, endpoint + 1):
        value = sum(a * (phi[n + s] // 2) for a, s in zip(row, range(1 - k, k + 1)))
        require(value % modulus == 0, f'annihilator fails at n={n}')


def check_solution(data: dict, k: int, phi: list[int]) -> dict:
    """Check the full target and recompute cost and support from coefficients."""
    require(type(data) is dict, 'solution must be an object')
    require(type(data['label']) is str and bool(data['label']), 'solution label')
    endpoint = integer(data['R'], 'solution support endpoint')
    require(k + 2 <= endpoint <= CAP, 'solution endpoint outside domain')
    coefficients = data['coefficients']
    require(
        type(coefficients) is list and bool(coefficients),
        'empty inhomogeneous solution',
    )
    previous = k + 1
    for pair in coefficients:
        require(type(pair) is list and len(pair) == 2, 'coefficient pair')
        n = integer(pair[0], 'support index')
        value = integer(pair[1], 'coefficient')
        require(previous < n <= endpoint, 'unsorted, repeated, or invalid support')
        require(value != 0, 'sparse support contains zero')
        previous = n
    for s in range(1 - k, k + 1):
        product = sum(value * phi[n + s] for n, value in coefficients)
        target = 0 if s <= 0 else -2 * phi[s]
        require(product == target, f'inhomogeneous target fails at shift {s}')
    cost = 2 * (k + 2) + sum(abs(value) * (n + k + 2) for n, value in coefficients)
    maximum = max(abs(value) for _, value in coefficients)
    support = [coefficients[0][0], coefficients[-1][0], len(coefficients)]
    ratio = Fraction(cost, 1 << k)
    denominator_exclusion = ((1 << k) - 1) // cost
    expected = {
        'cost': cost,
        'max_abs_coefficient': maximum,
        'support': support,
        'ratio': [ratio.numerator, ratio.denominator],
        'excluded_denominators_through': denominator_exclusion,
    }
    # Check types as well as equality: JSON booleans are not integer witnesses.
    for key in ('cost', 'max_abs_coefficient', 'excluded_denominators_through'):
        integer(data[key], f'solution {key}')
    for key in ('support', 'ratio'):
        require(type(data[key]) is list, f'solution {key} array')
        for value in data[key]:
            integer(value, f'solution {key} entry')
    for key, value in expected.items():
        require(data[key] == value, f'wrong recomputed solution {key}')
    return {'label': data['label'], 'R': endpoint, **expected}


def check_certificate(data: dict, k: int, checker: Checker) -> dict:
    """Verify one full-image/minimality certificate and every target witness."""
    require(integer(data['schema'], 'schema') == 1, 'unsupported schema')
    require(integer(data['k'], 'k') == k, 'wrong k')
    require(integer(data['B'], 'B') == k + 2, 'wrong lower cutoff')
    require(integer(data['cap'], 'cap') == CAP, 'wrong commissioned cap')
    shifts = data['shifts']
    require(type(shifts) is list, 'shifts must be an array')
    for shift in shifts:
        integer(shift, 'shift')
    require(shifts == list(range(1 - k, k + 1)), 'wrong ordered shifts')
    phi = [0] + [totient(n) for n in range(1, CAP + k + 1)]
    require(
        all(phi[n] % 2 == 0 for n in range(3, CAP + k + 1)),
        'normalization is not integral',
    )
    require(data['status'] in ('full_image', 'proper_at_cap'), 'uncertified status')
    if data['status'] == 'full_image':
        endpoint = integer(data['minimal_R'], 'minimal endpoint')
        require(3 * k + 1 <= endpoint <= CAP, 'endpoint violates dimension or cap')
        inverse = data['right_inverse']
        columns = endpoint - (k + 2) + 1
        require(
            type(inverse) is list and len(inverse) == columns, 'right inverse row count'
        )
        for row in inverse:
            require(
                type(row) is list and len(row) == 2 * k, 'right inverse column count'
            )
            for entry in row:
                integer(entry, 'right inverse entry')
        for i, s in enumerate(shifts):
            product = [0] * (2 * k)
            for n, row in enumerate(inverse, start=k + 2):
                entry = phi[n + s] // 2
                for j, value in enumerate(row):
                    product[j] += entry * value
            require(
                product == [int(i == j) for j in range(2 * k)],
                f'right inverse identity fails in row {i}',
            )
        checker.check(f'k={k}: exact A_R Y=I at R={endpoint}', True)
        check_annihilator(data['predecessor'], k, endpoint - 1, phi)
        checker.check(
            f'k={k}: proper image at R={endpoint - 1}; minimum certified', True
        )
    else:
        endpoint = None
        check_annihilator(data['cap_obstruction'], k, CAP, phi)
        checker.check(f'k={k}: proper image for every prefix through {CAP}', True)
    solutions = data['solutions']
    require(type(solutions) is list and bool(solutions), 'no inhomogeneous witness')
    labels = set()
    summaries = []
    for solution in solutions:
        summary = check_solution(solution, k, phi)
        require(summary['label'] not in labels, 'duplicate solution label')
        labels.add(summary['label'])
        summaries.append(summary)
        checker.check(
            f'k={k}: {summary["label"]} target, support, and exact cost', True
        )
    best = min(summaries, key=lambda item: item['cost'])
    return {'k': k, 'minimal_R': endpoint, 'best': best, 'solutions': summaries}


def boundary_checks(checker: Checker) -> None:
    """Cross-check trial totients against their elementary counting definition."""
    for n in (1, 2, 3, 4, 5, 8, 9, 16, 65, 66, 4095, 4096, 4160):
        counted = sum(math.gcd(n, j) == 1 for j in range(1, n + 1))
        require(totient(n) == counted, f'totient counting control at {n}')
    checker.check('small and cap-boundary totients agree with coprime counts', True)


def main() -> int:
    """Replay the declared scope; missing or corrupt inputs fail nonzero."""
    parser = evidence_parser(__doc__)
    parser.add_argument(
        '--assets',
        type=Path,
        default=ASSETS,
        help='certificate directory (default: adjacent assets)',
    )
    args = parser.parse_args()
    checker = Checker()
    orders = ORDERS[:2] if args.quick else ORDERS
    print(
        f'Exact certificate scope: k={list(orders)}, cap={CAP}; '
        'finite results only, no coefficient optimality or asymptotic claim.'
    )
    try:
        boundary_checks(checker)
    except ValueError as error:
        checker.check('totient boundary controls', False, str(error))
    for k in orders:
        try:
            certificate = read_certificate(args.assets / f'k{k:03d}.json.gz')
            summary = check_certificate(certificate, k, checker)
            best = summary['best']
            print(
                f'  k={k}: minimum R={summary["minimal_R"]}; best retained '
                f'C={best["cost"]}, ratio={Fraction(*best["ratio"])}, '
                f'support={best["support"]}, max|y|={best["max_abs_coefficient"]}, '
                f'denominators excluded through {best["excluded_denominators_through"]}'
            )
        except (OSError, EOFError, ValueError, KeyError, TypeError) as error:
            checker.check(f'k={k}: complete certificate acceptance', False, str(error))
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

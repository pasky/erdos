#!/usr/bin/env python3
"""Directed, finite-gcd certificates for off-diagonal prime-pair alternatives.

Each endpoint is an exact rational scaled by 10000. The source theorem
has a computable starting height, not numerically evaluated here.
"""
from fractions import Fraction
import json
from pathlib import Path

from erdos_699_off_diagonal_pade import growth_parameters, rational, iv

DATA = Path(__file__).with_suffix('.json')
SCALE = 10000


def normalized_edge(record):
    p, q = record['primes']
    a, b = record['endpoints_scaled']
    return (p, q, a, b) if p < q else (q, p, b, a)


def certify_record(record):
    seed = record['seed']
    c0, k0, regenerated = growth_parameters(
        seed['P'], seed['Q'], seed['a'], seed['b'],
        *record['directions'], Fraction(record['gcd_log_rate']),
        terms=record['gcd_terms'])
    assert c0 > 0 and k0 > 0
    assert {key: record[key] for key in regenerated} == regenerated
    limits = {}
    for prime, endpoint, base, block in zip(
            record['primes'], record['endpoints_scaled'],
            (seed['P'], seed['Q']),
            (record['left_block'], record['right_block'])):
        assert prime > 1 and all(prime % d for d in range(2, prime))
        power = 0
        while base % prime == 0:
            base //= prime
            power += 1
        assert base == 1 and power > 0
        alpha = 1 - block * power * iv.log(prime) / k0
        assert alpha > rational(Fraction(endpoint + 1, SCALE))
        assert 0 < endpoint < SCALE
        limits[str(prime)] = iv.nstr(alpha, 35)
    assert limits == record['limiting_exponents']
    # If the two selected factors coincide, their coprime prime-power
    # divisors imply u_p*u_q >= h. This handles the zero-gap case.
    assert sum(record['endpoints_scaled']) < SCALE
    return normalized_edge(record)


def certified_edges():
    data = json.loads(DATA.read_text())
    result = sorted(certify_record(record) for record in data['records'])
    assert [list(edge) for edge in result] == data['edges_scaled']
    assert len(result) == len(set(result))
    return result


def main():
    edges = certified_edges()
    print(json.dumps({'certified_pair_alternatives': len(edges),
                      'gap_bound': 13,
                      'endpoint_scale': SCALE,
                      'threshold': 'effective, not numerically evaluated'}, indent=2))


if __name__ == '__main__':
    main()

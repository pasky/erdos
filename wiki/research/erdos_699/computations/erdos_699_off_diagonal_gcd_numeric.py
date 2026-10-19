#!/usr/bin/env python3
"""Exact uniform coefficient-gcd bounds for both off-diagonal rectangles.

Directions (A,B,C) give rectangles (Am,Bm-1,Cm) and
(Am+1,Bm-2,Cm+1).  Write H=A+B+C and k_X=floor(X*t/H).
For eligible t, sum(k_X)=t-2, and both rectangles have these same
floors for every m at least the explicitly calculated stability bound.
The common prime interval is contained in both BFT Lemma 5.2 intervals:

 U_t(m)=(H*m-1)/t,
 V_t(m)=m*max((A+1/m0)/(k_A+1),B/(k_B+1),(C+1/m0)/(k_C+1)).

For m>=m0 the interval (V_t(m),U_t(m)] therefore divides both gcds.
The intervals are disjoint because each is a subset of the corresponding
interval for the first rectangle, and BFT's intervals are disjoint.

Dusart's theta upper bound (1+1/36260)x and the retained lower bound
x*(1-max(2.072/sqrt(x),1/60000)) give an exact rational lower rate for
log(G)/m. All divisions in the final sum round down to a fixed grid.
Only integer arithmetic is used in the certificate itself.
"""
from __future__ import annotations

from fractions import Fraction
import json
from math import isqrt
from pathlib import Path

RECTANGLE_SHIFTS = ((0, -1, 0), (1, -2, 1))


def floor_stability_bound(directions, t):
    """Least nonnegative m ensuring the selected three floors, both shifts."""
    H = sum(directions)
    floors = [X*t//H for X in directions]
    assert sum(floors) == t-2
    bound = 1
    for shifts in RECTANGLE_SHIFTS:
        total_shift = sum(shifts)
        for X, k, shift in zip(directions, floors, shifts):
            remainder = X*t-k*H
            assert 0 < remainder < H
            # k <= ((X*m+shift)*t)/(H*m+total_shift):
            rhs = k*total_shift-t*shift
            if rhs > 0:
                bound = max(bound, (rhs+remainder-1)//remainder)
            # ((X*m+shift)*t)/(H*m+total_shift) < k+1:
            rhs = t*shift-(k+1)*total_shift
            if rhs >= 0:
                bound = max(bound, rhs//(H-remainder)+1)
    return bound


def gcd_exponent_lower(A, B, C, *, terms=4000, m0=10**8,
                       scale=10**12, root_scale=10**6, theta_mode="fixed"):
    """Certify G >= exp(ell_lower*m) for both rectangles, every m>=m0.

    Returns a JSON-ready record. The caller compares ell_lower with its
    desired rate using Fraction. m0 must satisfy the exact floor bounds.
    """
    assert min(A, B, C, terms, m0, scale, root_scale) > 0
    assert theta_mode in ("fixed", "log")
    assert B*m0 >= 2
    directions = (A, B, C)
    H = sum(directions)
    total = eligible = positive = largest = 0
    floor_bound = 1
    for t in range(1, terms+1):
        floors = [X*t//H for X in directions]
        if sum(floors) != t-2:
            continue
        eligible += 1
        stable = floor_stability_bound(directions, t)
        floor_bound = max(floor_bound, stable)
        assert m0 >= stable, (directions, t, m0, stable)
        # Values V_t(m0) of the common lower endpoint; dividing by m0
        # bounds V_t(m)/m above for both shifted rectangles.
        candidates = [(A*m0+1, floors[0]+1),
                      (B*m0, floors[1]+1),
                      (C*m0+1, floors[2]+1)]
        v_num, v_den = candidates[0]
        for numerator, denominator in candidates[1:]:
            if numerator*v_den > v_num*denominator:
                v_num, v_den = numerator, denominator
        root = isqrt((H*m0-1)*root_scale**2//t)
        assert root > 0
        err_num, err_den = 259*root_scale, 125*root
        if err_num*60000 < err_den:
            err_num, err_den = 1, 60000
        if err_num >= err_den:
            continue
        upper_err_num, upper_err_den = 1, 36260
        if theta_mode == "log":
            # BFT theta(x)<x through 10^11 and Dusart above it give
            # the global upper error 1/60000. For an endpoint >=10^11,
            # log(x)>=floor(log2(x))*.69, since log(2)>.69.
            upper_err_num, upper_err_den = 1, 60000
            def log_error(numerator, denominator):
                k = numerator.bit_length()-denominator.bit_length()
                if denominator*(1 << k) > numerator:
                    k -= 1
                assert k >= 36
                return 100, 4761*k*k
            if H*m0-1 >= 10**11*t:
                en, ed = log_error(H*m0-1, t)
                if en*err_den < err_num*ed:
                    err_num, err_den = en, ed
            if v_num >= 10**11*v_den:
                en, ed = log_error(v_num, v_den)
                if en*upper_err_den < upper_err_num*ed:
                    upper_err_num, upper_err_den = en, ed
        numerator = ((err_den-err_num)*(H*m0-1)*upper_err_den*v_den
                     - err_den*(upper_err_den+upper_err_num)*v_num*t)
        denominator = err_den*upper_err_den*m0*t*v_den
        if numerator <= 0:
            continue
        positive += 1
        largest = t
        total += numerator*scale//denominator
    lower = Fraction(total, scale)
    assert lower > 0
    record = {
        'directions': list(directions), 'rectangular_shifts': [list(x) for x in RECTANGLE_SHIFTS],
        'terms': terms, 'm0': m0, 'floor_stability_bound': floor_bound,
        'rounding_denominator': scale, 'root_scale': root_scale,
        'eligible_terms': eligible, 'positive_terms': positive,
        'largest_positive_t': largest, 'ell_lower': str(lower),
        'upper_relative_error': '1/36260',
        'lower_relative_error_floor': '1/60000',
        'source': 'BFT Lemma 5.2; Dusart 2010 Proposition 5.1 and Theorem 5.2; retained BFT theta lower bound through 10^11',
        'conclusion': 'For every integer m>=m0, both coefficient gcds are at least exp(ell_lower*m).',
    }
    if theta_mode == "log":
        record.update({'theta_mode':'log',
                       'upper_relative_error':'min(1/60000, .01/log(x0)^2) when x0>=10^11',
                       'logarithm_lower_bound':'log(2)>69/100; 2^k<=x0 gives log(x0)>69k/100'})
    return record


def normalized_edge(record):
    p, q = record['primes']
    a, b = record['endpoints_scaled']
    return (p, q, a, b) if p < q else (q, p, b, a)


def main():
    directory = Path(__file__).parent
    ramp_path = directory/'erdos_699_index_12_ramp.json'
    ramp = json.loads(ramp_path.read_text())
    source_path = directory/ramp['source_file']
    sources = json.loads(source_path.read_text())
    by_edge = {normalized_edge(row): row for row in sources['records']}
    records = []
    for binding in ramp['source_bindings']:
        source = by_edge[tuple(binding['source_edge'])]
        requested = Fraction(source['gcd_log_rate'])
        for exponent in range(6, 13):
            record = gcd_exponent_lower(*source['directions'], m0=10**exponent)
            if Fraction(record['ell_lower']) > requested:
                break
        else:
            raise AssertionError(('No bound found through 10^12', binding))
        record.update({'edge': binding['edge'], 'source_edge': binding['source_edge'],
                       'requested_log_rate': str(requested),
                       'strict_rate_margin': str(Fraction(record['ell_lower'])-requested)})
        records.append(record)
    result = {
        'scope': 'Numerical coefficient-gcd starting indices for the twenty index-twelve ramp sources.',
        'ramp_file': ramp_path.name,
        'source_file': source_path.name,
        'records': records,
    }
    output = Path(__file__).with_suffix('.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'output': str(output), 'source_count': len(records),
                      'maximum_m0': max(row['m0'] for row in records),
                      'm0_by_edge': [[row['edge'], row['m0']] for row in records]}, indent=2))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Finite prime-interval bootstrap for both off-diagonal coefficient gcds.

For m in [L,U] and each stable eligible t, use the common interval
 ((max((A*U+1)/(kA+1),B*U/(kB+1),(C*U+1)/(kC+1))),
  (H*L-1)/t]. Every prime there divides both coefficient gcds for
 every m in [L,U]. BFT Lemma 5.2 makes these intervals disjoint.

Below the sieve cutoff, directed lower log-prime weights are summed.
For larger endpoints x<=10^11, BFT Lemma 5.4 gives
 theta(x)>x-2.072*sqrt(x) and theta(x)<x. Above10^11 we use Dusart's
 absolute error .01*x/log(x)^2 and log(x)>floor(log2(x))*.69.
 Square roots and logarithms only propose integers; exact comparisons
 certify each proposal before integer error bounds are used.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time

import numpy as np

from erdos_699_bft_prime_bootstrap import PrimeLogIntervals, SCALE
from erdos_699_off_diagonal_gcd_numeric import gcd_exponent_lower, floor_stability_bound


def interval_arrays(directions, terms):
    H = sum(directions)
    ts, dens, floors = [], [], []
    for t in range(1, terms+1):
        k = [X*t//H for X in directions]
        if sum(k) != t-2:
            continue
        ts.append(t)
        dens.append([x+1 for x in k])
        floors.append(floor_stability_bound(directions, t))
    return (np.array(ts, dtype=np.int64), np.array(dens, dtype=np.int64),
            np.array(floors, dtype=np.int64))


def prime_sum_lower(theta, uppers, lowers):
    keep = uppers > lowers
    uppers, lowers = uppers[keep], lowers[keep]
    if len(uppers) == 0:
        return 0
    assert int(uppers.max()) < 2**62
    # All common intervals are disjoint and contained in (0,max(uppers)].
    assert np.all(uppers[1:] <= lowers[:-1])
    exact = uppers <= theta.limit
    iu = np.searchsorted(theta.primes, uppers[exact], side='right')
    il = np.searchsorted(theta.primes, lowers[exact], side='right')
    total = int(np.sum(theta.prefix_lo[iu]-theta.prefix_lo[il], dtype=np.uint64))
    u, v = uppers[~exact], lowers[~exact]
    if len(u):
        roots = np.sqrt(u).astype(np.int64)
        # Correct the proposed integer ceil(sqrt(u)) in either direction.
        while np.any(roots*roots < u):
            roots += (roots*roots < u)
        while np.any((roots-1)*(roots-1) >= u):
            roots -= ((roots-1)*(roots-1) >= u)
        assert np.all(roots*roots >= u)
        assert np.all((roots-1)*(roots-1) < u)
        errors = (259*roots+124)//125
        def dusart_error(values):
            # log(values)>=k*log(2)>69*k/100. Exact comparisons
            # certify the floor-log2 proposal before it is used.
            k = np.floor(np.log2(values)).astype(np.int64)
            powers = np.left_shift(np.int64(1), k)
            while np.any(powers > values):
                k -= powers > values
                powers = np.left_shift(np.int64(1), k)
            while np.any(2*powers <= values):
                k += 2*powers <= values
                powers = np.left_shift(np.int64(1), k)
            assert np.all(powers <= values) and np.all(values < 2*powers)
            den = 4761*k*k
            # ceil(100*values/den), arranged to avoid intermediate overflow.
            return 100*(values//den)+(100*(values%den)+den-1)//den
        large = u > 10**11
        errors[large] = dusart_error(u[large])
        upper_theta_at_lower = v.copy()
        large_lower = v > 10**11
        upper_theta_at_lower[large_lower] += dusart_error(v[large_lower])
        cross = v <= theta.limit
        jj = np.searchsorted(theta.primes, v[cross], side='right')
        upper_theta_at_lower[cross] = ((theta.prefix_hi[jj]+SCALE-1)//SCALE).astype(np.int64)
        lower_logs = np.maximum(0, u-errors-upper_theta_at_lower)
        # Sum before multiplying by SCALE: endpoints through10^11 would
        # overflow a uint64 after multiplication, but Python integers do not.
        total += int(np.sum(lower_logs, dtype=np.int64))*SCALE
    return total


def bootstrap(row, theta, *, lower_start=1000, terms=4000):
    analytic = {key: row[key] for key in (
        'directions','terms','m0','rounding_denominator','root_scale','ell_lower')}
    A, B, C = row['directions']
    regenerated = gcd_exponent_lower(A,B,C,terms=analytic['terms'],m0=analytic['m0'],
        scale=analytic['rounding_denominator'],root_scale=analytic['root_scale'],
        theta_mode=row.get('theta_mode','fixed'))
    assert regenerated['ell_lower'] == analytic['ell_lower']
    target = Fraction(row['requested_log_rate'])
    assert Fraction(analytic['ell_lower']) > target
    ts, den, stable = interval_arrays((A,B,C),terms)
    H = A+B+C
    top = analytic['m0']-1
    stack = [(lower_start,top)]
    covered_right = top
    leaves = visited = 0
    minimum = None
    unsupported = None
    digest = hashlib.sha256()
    started = time.monotonic()
    while stack:
        left,right = stack.pop()
        visited += 1
        valid = stable <= left
        tv,dv = ts[valid],den[valid]
        uppers = (H*left-1)//tv
        lowers = np.maximum.reduce(((A*right+1)//dv[:,0], B*right//dv[:,1],
                                     (C*right+1)//dv[:,2]))
        lower_sum = prime_sum_lower(theta,uppers,lowers)
        margin_num = lower_sum*target.denominator-right*SCALE*target.numerator
        if margin_num >= 0:
            assert right == covered_right
            covered_right = left-1
            leaves += 1
            margin = Fraction(margin_num,right*SCALE*target.denominator)
            if minimum is None or margin < minimum:
                minimum = margin
            digest.update(f'{left},{right},{lower_sum}\n'.encode())
            if leaves%20000 == 0:
                print(json.dumps({'edge':row['edge'],'leaves':leaves,'left':left,
                                  'elapsed_seconds':round(time.monotonic()-started,1)}),flush=True)
        elif left == right:
            unsupported = left
            assert covered_right == left
            break
        else:
            middle = (left+right)//2
            stack.append((left,middle))
            stack.append((middle+1,right))
    effective_start = unsupported+1 if unsupported is not None else lower_start
    assert covered_right == effective_start-1
    result = {
        'edge':row['edge'],'source_edge':row['source_edge'],'directions':row['directions'],
        'requested_log_rate':str(target),'finite_interval_start':effective_start,
        'finite_interval_end':top,'analytic_gcd_certificate':row,
        'terms':terms,'certified_intervals':leaves,'visited_nodes':visited,
        'largest_unsupported_singleton':unsupported,'minimum_margin':str(minimum),
        'partition_sha256':digest.hexdigest(),
        'elapsed_seconds':round(time.monotonic()-started,3),
        'conclusion':'For every integer m>=finite_interval_start, both rectangle coefficient gcds are at least exp(requested_log_rate*m).',
    }
    print(json.dumps({k:result[k] for k in ('edge','finite_interval_start','certified_intervals',
                     'visited_nodes','elapsed_seconds')}),flush=True)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,default=Path(__file__).with_name('erdos_699_off_diagonal_gcd_numeric.json'))
    parser.add_argument('--output',type=Path,default=Path(__file__).with_suffix('.json'))
    parser.add_argument('--sieve-limit',type=int,default=10**8)
    parser.add_argument('--lower-start',type=int,default=1000)
    parser.add_argument('--records',type=str,default='')
    args=parser.parse_args()
    data=json.loads(args.input.read_text())
    rows=data['records']
    if args.records:
        indices=list(map(int,args.records.split(',')))
        rows=[rows[i] for i in indices]
    theta=PrimeLogIntervals(args.sieve_limit)
    print(json.dumps(theta.metadata),flush=True)
    result={'input_file':args.input.name,
            'prime_log_certificate':theta.metadata,'records':[]}
    for row in rows:
        result['records'].append(bootstrap(row,theta,lower_start=args.lower_start))
        args.output.write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()

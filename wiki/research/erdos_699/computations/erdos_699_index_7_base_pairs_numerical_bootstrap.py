"""Finite gcd bootstrap for the initial index-seven pair sources.

This retains the exact BFT prime intervals and directed prime-log sieve.
For endpoints through 10^19, theta(x)<x, and the lower bounds are
x-2.072*sqrt(x) through 10^11 and x-1.96*sqrt(x) above 10^11.
The latter two extensions are justified in the retained sharp-gcd note.
All square-root proposals are corrected by exact integer comparisons.
"""
from fractions import Fraction
import json
from pathlib import Path
import numpy as np
from mpmath import iv

import erdos_699_off_diagonal_gcd_bootstrap as base
from erdos_699_off_diagonal_gcd_numeric import gcd_exponent_lower as old_gcd
from erdos_699_off_diagonal_gcd_sharp import gcd_exponent_lower as sharp_gcd
from erdos_699_off_diagonal_explicit_clauses import joint_clause_threshold


def gcd_exponent_lower(*args, theta_mode='fixed', **kwargs):
    if theta_mode == 'broadbent_johnston_yang':
        return sharp_gcd(*args, **kwargs)
    return old_gcd(*args, theta_mode=theta_mode, **kwargs)


def prime_sum_lower(theta, uppers, lowers):
    keep = uppers > lowers
    uppers, lowers = uppers[keep], lowers[keep]
    if len(uppers) == 0:
        return 0
    assert int(uppers.max()) < min(10**19,2**62)
    assert np.all(uppers[1:] <= lowers[:-1])
    exact = uppers <= theta.limit
    iu = np.searchsorted(theta.primes, uppers[exact], side='right')
    il = np.searchsorted(theta.primes, lowers[exact], side='right')
    total = int(np.sum(theta.prefix_lo[iu]-theta.prefix_lo[il], dtype=np.uint64))
    u,v = uppers[~exact], lowers[~exact]
    if len(u):
        roots = np.sqrt(u).astype(np.int64)
        while np.any(roots*roots < u):
            roots += roots*roots < u
        while np.any((roots-1)*(roots-1) >= u):
            roots -= (roots-1)*(roots-1) >= u
        assert np.all(roots*roots >= u)
        assert np.all((roots-1)*(roots-1) < u)
        errors = (259*roots+124)//125
        large = u > 10**11
        errors[large] = (49*roots[large]+24)//25
        upper_theta_at_lower = v.copy()
        cross = v <= theta.limit
        jj = np.searchsorted(theta.primes,v[cross],side='right')
        upper_theta_at_lower[cross] = ((theta.prefix_hi[jj]+base.SCALE-1)//base.SCALE).astype(np.int64)
        lower_logs = np.maximum(0,u-errors-upper_theta_at_lower)
        total += int(np.sum(lower_logs,dtype=np.int64))*base.SCALE
    return total


def bootstrap(row, theta, **kwargs):
    old_sum, old_lower = base.prime_sum_lower, base.gcd_exponent_lower
    base.prime_sum_lower, base.gcd_exponent_lower = prime_sum_lower, gcd_exponent_lower
    try:
        result = base.bootstrap(row,theta,**kwargs)
    finally:
        base.prime_sum_lower, base.gcd_exponent_lower = old_sum,old_lower
    result['finite_theta_mode'] = 'broadbent_sqrt_10_19'
    return result


if __name__ == '__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--indices',default='')
    args=parser.parse_args()
    data=json.loads(args.input.read_text())
    indices=list(map(int,args.indices.split(','))) if args.indices else list(range(len(data['records'])))
    theta=base.PrimeLogIntervals()
    iv.dps=80
    out={'input_file':args.input.name,'prime_log_certificate':theta.metadata,'records':[]}
    for ix in indices:
        row=data['records'][ix]
        analytic=row['analytic_gcd_certificate']
        finite=bootstrap(analytic,theta,terms=analytic['terms'])
        numeric=joint_clause_threshold(row['clause'],finite['finite_interval_start'],gap=6,maximum_shift=6)
        out['records'].append({'edge':row['edge'],'bootstrap':finite,'numeric':numeric})
        args.output.write_text(json.dumps(out,indent=2)+'\n')
        print('CAP',row['edge'],numeric['threshold_power_of_ten'],flush=True)

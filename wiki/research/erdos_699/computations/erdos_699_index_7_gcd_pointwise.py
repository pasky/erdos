#!/usr/bin/env python3
"""Pointwise coefficient-gcd lower bounds for both adjacent Pade rectangles.

A finite-prime prefix and exact proper-prime-power addendum are combined
with the retained BFT and Broadbent theta bounds. The prime-power interval
lemma permits every selected t without a floor-stability restriction.
All returned logarithmic bounds are integer multiples of 2^(-32).
"""
from fractions import Fraction
from functools import lru_cache
import json
import numpy as np

from erdos_699_bft_prime_bootstrap import PrimeLogIntervals, SCALE
from erdos_699_off_diagonal_gcd_bootstrap import interval_arrays
from erdos_699_off_diagonal_gcd_sharp import TABLE
from erdos_699_prime_power_addendum import PrimePowerAddendum

def _ceil_product_ratio(values,numerator,denominator):
    """Vectorized ceil(numerator*values/denominator), without overflow."""
    assert numerator>0 and denominator>0
    if len(values)==0:return values.copy()
    assert numerator*min(denominator-1,int(values.max()))<2**63
    return numerator*(values//denominator)+(numerator*(values%denominator)+denominator-1)//denominator


def sharp_prime_sum_lower(theta,uppers,lowers):
    keep=uppers>lowers
    uppers,lowers=uppers[keep],lowers[keep]
    if not len(uppers):return 0
    largest=int(uppers.max())
    assert largest<2**62 and largest<=10**19
    assert np.all(uppers[1:]<=lowers[:-1])
    exact=uppers<=theta.limit
    iu=np.searchsorted(theta.primes,uppers[exact],side='right')
    il=np.searchsorted(theta.primes,lowers[exact],side='right')
    total=int(np.sum(theta.prefix_lo[iu]-theta.prefix_lo[il],dtype=np.uint64))
    u,v=uppers[~exact],lowers[~exact]
    if len(u):
        root_scale=64
        while largest*root_scale*root_scale>=2**62:
            root_scale//=2
        assert root_scale>=1 and SCALE%root_scale==0
        squares=u*(root_scale*root_scale)
        roots=np.sqrt(squares).astype(np.int64)
        while np.any(roots*roots<squares):roots+=roots*roots<squares
        while np.any((roots-1)*(roots-1)>=squares):roots-=(roots-1)*(roots-1)>=squares
        assert np.all(roots*roots>=squares) and np.all((roots-1)*(roots-1)<squares)
        errors=(259*roots+124)//125
        improved=u>=10**11
        errors[improved]=(49*roots[improved]+24)//25
        units=u*root_scale
        for threshold,_upper,error in TABLE:
            if threshold>largest:break
            selected=u>=threshold
            candidate=_ceil_product_ratio(units[selected],error.numerator,error.denominator)
            errors[selected]=np.minimum(errors[selected],candidate)
        # Broadbent (3.17): theta(v)<v-.05*sqrt(v) through10^19.
        lower_squares=v*(root_scale*root_scale)
        lower_roots=np.sqrt(lower_squares).astype(np.int64)
        while np.any(lower_roots*lower_roots>lower_squares):
            lower_roots-=lower_roots*lower_roots>lower_squares
        while np.any((lower_roots+1)*(lower_roots+1)<=lower_squares):
            lower_roots+=(lower_roots+1)*(lower_roots+1)<=lower_squares
        assert np.all(lower_roots*lower_roots<=lower_squares)
        assert np.all((lower_roots+1)*(lower_roots+1)>lower_squares)
        upper_theta_at_lower=v*root_scale-lower_roots//20
        cross=v<=theta.limit
        jj=np.searchsorted(theta.primes,v[cross],side='right')
        divisor=SCALE//root_scale
        exact_upper=((theta.prefix_hi[jj]+divisor-1)//divisor).astype(np.int64)
        upper_theta_at_lower[cross]=np.minimum(upper_theta_at_lower[cross],exact_upper)
        lower_units=np.maximum(0,units-errors-upper_theta_at_lower)
        assert largest*root_scale<2**63
        total+=int(np.sum(lower_units,dtype=np.int64))*(SCALE//root_scale)
    return total


class PointwiseGcdLower:
    """Reusable exact evaluator; share theta and powers across directions.

    evaluator.log_lower(m) returns an integer L with log(G)>=L/SCALE
    for each of (Am,Bm-1,Cm) and (Am+1,Bm-2,Cm+1).
    evaluator.rate_lower(m) returns the exact Fraction L/(SCALE*m).
    """
    def __init__(self,theta,directions,*,terms=4000,powers=None):
        self.theta=theta
        self.directions=tuple(map(int,directions))
        assert len(self.directions)==3 and min(self.directions)>0
        self.terms=terms
        self.ts,self.den,_unused=interval_arrays(self.directions,terms)
        self.powers=powers if powers is not None else PrimePowerAddendum(theta,power_limit=10**14)

    @lru_cache(maxsize=512)
    def log_lower(self,m):
        A,B,C=self.directions
        H=A+B+C
        assert isinstance(m,int) and m>=1 and B*m>=2 and H*m<2**62
        # The prime-power interval lemma applies without filtering t by m.
        uppers=(H*m-1)//self.ts
        lowers=np.maximum.reduce(((A*m+1)//self.den[:,0],B*m//self.den[:,1],
                                  (C*m+1)//self.den[:,2]))
        return (sharp_prime_sum_lower(self.theta,uppers,lowers)
                +self.powers.interval_sum_lower(uppers,lowers))

    def rate_lower(self,m):
        return Fraction(self.log_lower(m),SCALE*m)

    def certificate(self,m):
        return {'directions':list(self.directions),'m':m,'terms':self.terms,
                'log_gcd_lower_scaled':self.log_lower(m),'fixed_point_scale':SCALE,
                'ell_lower':str(self.rate_lower(m)),
                'rectangles':[[self.directions[0]*m,self.directions[1]*m-1,self.directions[2]*m],
                              [self.directions[0]*m+1,self.directions[1]*m-2,self.directions[2]*m+1]],
                'uses_all_prime_powers_in_retained_prefix':True}


def main():
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('A',type=int);parser.add_argument('B',type=int);parser.add_argument('C',type=int)
    parser.add_argument('m',type=int);parser.add_argument('--terms',type=int,default=4000)
    args=parser.parse_args()
    theta=PrimeLogIntervals()
    powers=PrimePowerAddendum(theta,power_limit=10**14)
    evaluator=PointwiseGcdLower(theta,(args.A,args.B,args.C),terms=args.terms,powers=powers)
    print(json.dumps({'prime_log_certificate':theta.metadata,'prime_power_certificate':powers.metadata,
                      'point':evaluator.certificate(args.m)},indent=2))


if __name__=='__main__':main()

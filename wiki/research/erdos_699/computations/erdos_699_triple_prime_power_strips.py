#!/usr/bin/env python3
"""Exact three-prime CRT strip certificates for nearby numerator factors.

The covered exponent orthant advances by certified coordinate slabs.
At anchors with no available slab, its three boundary planes are checked
inside explicit finite boxes. Only minimal CRT solutions need inspection.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import product
import json
from math import log, log2
from pathlib import Path
import time


def certify(primes=(2,3,5), cap=1000, difference=6,
            exponent=Fraction(61,100), max_boundary_triples=3000000,
            backend='gmpy2'):
    numerator, denominator=exponent.numerator,exponent.denominator
    complement=denominator-numerator
    assert len(primes)==3 and len(set(primes))==3
    assert 0<numerator and 3*numerator<2*denominator
    assert difference>=1 and cap>=1
    if backend=='gmpy2':
        import gmpy2
        Integer=gmpy2.mpz
        inverse=gmpy2.invert
        root=lambda value,degree:gmpy2.iroot(value,degree)[0]
    else:
        Integer=int
        inverse=lambda value,modulus:pow(value,-1,modulus)
        def root(value,degree):
            answer=1<<((value.bit_length()+degree-1)//degree)
            while True:
                following=((degree-1)*answer+value//answer**(degree-1))//degree
                if following>=answer:
                    while(answer+1)**degree<=value:answer+=1
                    while answer**degree>value:answer-=1
                    return answer
                answer=following
    bound=Integer(10)**cap
    height_start=1
    while not(height_start>=difference and
              Integer(height_start)**(3*complement)>=Integer(height_start+difference)**denominator and
              Integer(height_start)**complement>=Integer(difference)**denominator):
        height_start*=2
    row_start=height_start+difference
    positions=[r for r in product(range(difference+1),repeat=3)if min(r)==0]
    limits=[];exponents=[];powers=[]
    for p in primes:
        limit=max(0,int(cap*log(10)/log(p)));power=Integer(p)**limit
        while power>bound:limit-=1;power//=p
        while power*p<=bound:limit+=1;power*=p
        limits.append(limit)
        a=1;P=Integer(p)
        while P<=difference:a+=1;P*=p
        exponents.append(a);powers.append(P)
    initial_exponents=exponents[:]
    anchors=[];exceptions=[];boundary_count=0

    def crt_rows(ps):
        modulus=prod_int(ps)
        basis=[]
        for P in ps:
            other=modulus//P
            basis.append(other*inverse(other%P,P))
        multiples=[[r*b for r in range(difference+1)]for b in basis]
        for offsets in positions:
            n=sum(multiples[k][offsets[k]]for k in range(3))%modulus
            if n==0:
                assert offsets==(0,0,0)
                cofactors=[modulus//P for P in ps]
            else:
                assert n>=max(offsets)
                cofactors=[(n-r)//P for r,P in zip(offsets,ps)]
                assert all(u>0 for u in cofactors)
            yield offsets,n,cofactors

    def safe_steps(minimum,P,p):
        ratio=minimum**complement//P**numerator
        if ratio<1:return -1
        steps=max(0,int(ratio.bit_length()/(denominator*log2(p))))
        base=Integer(p)**denominator;test=base**steps
        while test>ratio:steps-=1;test//=base
        while test*base<=ratio:steps+=1;test*=base
        assert test<=ratio<test*base
        return steps

    def check_boundary(aa,ps,row_bound,fixed):
        nonlocal boundary_count
        boundary_count+=1
        if boundary_count>max_boundary_triples:
            raise RuntimeError('boundary-triple budget exhausted; proof incomplete')
        if boundary_count%10000==0:
            print(json.dumps({'boundary_triples':boundary_count,'anchors':len(anchors),
                              'exceptions':len(exceptions),'exponents':list(aa)}),flush=True)
        other=[k for k in range(3)if k!=fixed]
        left,right=other;Q,R=ps[left],ps[right]
        if Q*R>row_bound:
            # Only a minimal solution for the other two prime powers can
            # lie below this plane's row bound. Enumerate their small
            # signed difference, then test the remaining congruence.
            inv=inverse(Q%R,R)
            candidates=[]
            for diff in range(-difference,difference+1):
                if diff==0:continue
                X=Q*((diff*inv)%R)
                for t in range(max(0,-diff),min(difference,difference-diff)+1):
                    n=X+t
                    if n<row_start or n>row_bound:continue
                    offset=n%ps[fixed]
                    if offset>difference:continue
                    offsets=[0,0,0];offsets[fixed]=int(offset)
                    offsets[left]=t;offsets[right]=t+diff
                    if min(offsets)>0:continue
                    us=[(n-r)//P for r,P in zip(offsets,ps)]
                    candidates.append((offsets,n,us))
        else:
            candidates=crt_rows(ps)
        for offsets,n,us in candidates:
            if n<row_start or n>row_bound:continue
            height=n-difference
            if max(us)**denominator>=height**numerator:continue
            # The actual CRT row is retained; it is an exception to the
            # cofactor inequality, not a bad binomial triple.
            item={'exponents':list(aa),'positions':list(offsets),
                  'row':int(n),'cofactors':list(map(int,us))}
            exceptions.append(item)

    def powers_up_to(axis,start_a,start_P,cap_power):
        a=start_a;P=start_P
        while a<=limits[axis] and P<=cap_power:
            yield a,P
            a+=1;P*=primes[axis]

    while all(a<=limit for a,limit in zip(exponents,limits)):
        minima=[prod_int(powers)//P for P in powers]
        for _,_,us in crt_rows(powers):
            minima=[min(a,b)for a,b in zip(minima,us)]
        steps=[safe_steps(mu,P,p)for mu,P,p in zip(minima,powers,primes)]
        record={'exponents':exponents[:],
                'power_bits':[P.bit_length()for P in powers],
                'minimum_cofactor_bits':[u.bit_length()for u in minima]}
        if max(steps)<0:
            before=boundary_count
            # Plane0 includes its edges. Plane1 omits plane0, and plane2
            # omits both previous planes, so each boundary triple occurs once.
            for fixed in range(3):
                finite_bound=min(bound,root(powers[fixed]**denominator,complement)+difference)
                other=[k for k in range(3)if k!=fixed]
                starts=[]
                for k in other:
                    skip=int(k<fixed)
                    starts.append((k,exponents[k]+skip,powers[k]*primes[k]**skip))
                k,a0,P0=starts[0];l,b0,Q0=starts[1]
                for a,P in powers_up_to(k,a0,P0,finite_bound):
                    for b,Q in powers_up_to(l,b0,Q0,finite_bound):
                        aa=exponents[:];ps=powers[:]
                        aa[k]=a;ps[k]=P;aa[l]=b;ps[l]=Q
                        check_boundary(aa,ps,finite_bound,fixed)
            advance=[1,1,1]
            record.update(method='exact boundary planes',boundary_triples=boundary_count-before)
        else:
            advance=[step+1 if step>=0 else 0 for step in steps]
            for mu,P,p,step in zip(minima,powers,primes,steps):
                if step>=0:
                    assert mu**complement>=P**numerator*Integer(p)**(denominator*step)
            record.update(method='cofactor lower-bound slabs',safe_steps=steps)
        record['exponent_advance']=advance
        anchors.append(record)
        if len(anchors)%100==0:
            print(json.dumps({'anchors':len(anchors),'boundary_triples':boundary_count,
                              'exceptions':len(exceptions),'exponents':exponents}),flush=True)
        for k in range(3):
            exponents[k]+=advance[k];powers[k]*=Integer(primes[k])**advance[k]
    exceptions.sort(key=lambda item:(item['row'],item['positions'],item['exponents']))
    return {'primes':list(primes),'cap_power_of_ten':cap,'difference':difference,
            'cofactor_exponent':str(exponent),'height_variable':f'h=n-{difference}',
            'row_start':row_start,'position_pattern_count':len(positions),
            'position_scope':'All positions in [0,D] whose minimum is zero, including coincidences.',
            'initial_exponents':initial_exponents,'last_exponents':limits,
            'anchors':anchors,'anchor_count':len(anchors),'boundary_triples':boundary_count,
            'exceptions':exceptions,'exception_count':len(exceptions),
            'exceptional_rows':sorted({item['row']for item in exceptions}),
            'backend':backend,
            'conclusion':'Except at the listed CRT rows and position patterns, max(u_p)>=h^delta throughout the stated finite height range.'}


def prod_int(values):
    result=1
    for value in values:result*=value
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cap',type=int,default=1000)
    parser.add_argument('--exponent',type=Fraction,default=Fraction(61,100))
    parser.add_argument('--difference',type=int,default=6)
    parser.add_argument('--max-boundary-triples',type=int,default=3000000)
    parser.add_argument('--backend',choices=['builtin','gmpy2'],default='gmpy2')
    parser.add_argument('--output',type=Path,default=Path(__file__).with_suffix('.json'))
    args=parser.parse_args();start=time.monotonic()
    row=certify(cap=args.cap,difference=args.difference,exponent=args.exponent,
                max_boundary_triples=args.max_boundary_triples,backend=args.backend)
    args.output.write_text(json.dumps(row,indent=2)+'\n')
    print(json.dumps({k:v for k,v in row.items()if k not in('anchors','exceptions','exceptional_rows')}|
                     {'elapsed_seconds':time.monotonic()-start,'exceptional_row_count':len(row['exceptional_rows'])},indent=2))


if __name__=='__main__':main()

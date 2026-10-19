#!/usr/bin/env python3
"""Prime-pair strip certificates without materializing high integer powers.

CRT arithmetic is exact. Directed logarithms of leading integer bits certify
power comparisons; uncertain small comparisons fall back to exact powers.
One extended gcd supplies both modular coefficient progressions.
"""
from fractions import Fraction
from itertools import combinations
import argparse
import hashlib
import json
from math import floor, log
from pathlib import Path
import time

import gmpy2
from mpmath import iv

iv.dps = 80
Integer = gmpy2.mpz


def log_integer(value):
    assert value > 0
    bits = value.bit_length()
    kept = min(bits, max(32,int(iv.dps*3)))
    shift = bits-kept
    head = int(value >> shift)
    if not shift:
        return iv.log(head)
    lower = iv.log(head)+shift*iv.log(2)
    upper = iv.log(head+1)+shift*iv.log(2)
    return iv.mpf([lower.a,upper.b])


def power_ge(left, left_power, right, right_power):
    if max(left.bit_length()*left_power,right.bit_length()*right_power) < 200000:
        return left**left_power >= right**right_power
    original = iv.dps
    try:
        while True:
            gap = left_power*log_integer(left)-right_power*log_integer(right)
            if gap.a >= 0: return True
            if gap.b < 0: return False
            g = gmpy2.gcd(left_power,right_power)
            root1,exact1 = gmpy2.iroot(left,int(right_power//g))
            root2,exact2 = gmpy2.iroot(right,int(left_power//g))
            if exact1 and exact2 and root1==root2: return True
            iv.dps *= 2
    finally:
        iv.dps = original


def certify(p,q,cap,difference,backend='gmpy2',max_boundary_pairs=100000,
            exponent=Fraction(1,3),prefix=None,prefix_source=None):
    assert backend=='gmpy2'
    numerator,denominator = exponent.numerator,exponent.denominator
    complement = denominator-numerator
    assert 0 < 2*numerator <= denominator and cap > 0
    lp,lq,l10 = iv.log(p),iv.log(q),iv.log(10)
    def last_exponent(prime, logarithm):
        proposed = int(cap*log(10)/log(prime))
        while (proposed*logarithm-cap*l10).a > 0: proposed -= 1
        while ((proposed+1)*logarithm-cap*l10).b <= 0: proposed += 1
        assert (cap*l10-proposed*logarithm).a >= 0
        assert ((proposed+1)*logarithm-cap*l10).a > 0
        return proposed
    limits = [last_exponent(p,lp),last_exponent(q,lq)]
    a,P = 1,Integer(p)
    while P<=difference: a+=1;P*=p
    b,Q = 1,Integer(q)
    while Q<=difference: b+=1;Q*=q
    initial = [a,b];anchors=[];exceptions=[];boundary_pairs=0
    boundary_hash=hashlib.sha256()

    if prefix is not None:
        assert prefix['pair']==[p,q] and prefix['maximum_difference']==difference
        previous_exponent=Fraction(prefix.get('cofactor_exponent_numerator',1),
            prefix.get('cofactor_exponent_denominator',prefix.get('reciprocal_exponent_denominator')))
        assert previous_exponent==exponent and prefix['height_cap_power_of_ten']<cap
        assert prefix['initial_exponents']==initial
        assert prefix['anchor_count']==len(prefix['anchors'])
        cursor=initial[:]
        for record in prefix['anchors']:
            assert cursor==[record['p_exponent'],record['q_exponent']]
            if record['method']=='exact boundary lines':
                aa,bb=cursor
                A,B=Integer(p)**aa,Integer(q)**bb
                largest=log_integer(max(A,B))
                # On either boundary, a potentially bad minimal solution has
                # height < 2*max(P,Q)^(1+s/(s-r)). This proves that neither
                # the old prime-power cap nor its height filter cut a boundary.
                upper=iv.log(2)+(1+iv.mpf(denominator)/complement)*largest
                assert (prefix['height_cap_power_of_ten']*l10-upper).a>0
                before=boundary_pairs
                eb,V=bb,B
                while not power_ge(V-difference,complement,A,denominator):
                    boundary_hash.update(f'{aa}:{eb}\n'.encode())
                    boundary_pairs+=1;eb+=1;V*=q
                ea,U=aa+1,A*p
                while not power_ge(U-difference,complement,B,denominator):
                    boundary_hash.update(f'{ea}:{bb}\n'.encode())
                    boundary_pairs+=1;ea+=1;U*=p
                assert boundary_pairs-before==record['boundary_pairs']
                assert record['p_exponent_advance']==record['q_exponent_advance']==1
            else:
                assert record['method'] in ('coefficient lower-bound strips',
                    'CRT strips with directed logarithm comparisons')
            advances=[record['p_exponent_advance'],record['q_exponent_advance']]
            assert all(type(v)is int and v>=0 for v in advances) and max(advances)>0
            cursor=[x+y for x,y in zip(cursor,advances)]
        assert cursor==prefix['final_exponents']
        assert boundary_pairs==prefix['exact_boundary_pairs']
        assert boundary_hash.hexdigest()==prefix['boundary_pairs_sha256']
        assert prefix['exception_count']==len(prefix['exceptions'])
        anchors=list(prefix['anchors']);exceptions=list(prefix['exceptions'])
        a,b=cursor;P,Q=Integer(p)**a,Integer(q)**b

    def coefficients(A,B):
        common,s,t=gmpy2.gcdext(A,B)
        assert common==1
        first=s % B;second=(-t) % A
        u=v=Integer(0)
        for delta in range(1,difference+1):
            u+=first
            if u>=B:u-=B
            v+=second
            if v>=A:v-=A
            assert 0<u<B and 0<v<A
            yield delta,u,v
            yield -delta,B-u,A-v

    def safe_steps(minimum,prime,prime_exponent,logprime):
        original=iv.dps
        try:
            while True:
                lm=log_integer(minimum)
                gap=complement*lm-numerator*prime_exponent*logprime
                if gap.b<0:return -1
                proposed=max(0,floor(float((gap/(denominator*logprime)).mid)))
                def valid(step):
                    target=numerator*prime_exponent+denominator*step
                    value=complement*lm-target*logprime
                    if value.a>=0:return True
                    if value.b<0:return False
                    if target % complement==0 and minimum==Integer(prime)**(target//complement):return True
                    return None
                low=valid(proposed)
                high=valid(proposed+1)
                if low is None or high is None:
                    iv.dps*=2;logprime=iv.log(prime);continue
                while not low:
                    proposed-=1
                    if proposed<0:return -1
                    low=valid(proposed)
                    if low is None:break
                if low is None:
                    iv.dps*=2;logprime=iv.log(prime);continue
                while high:
                    proposed+=1;high=valid(proposed+1)
                    if high is None:break
                if high is None:
                    iv.dps*=2;logprime=iv.log(prime);continue
                assert valid(proposed) and valid(proposed+1) is False
                return proposed
        finally:
            iv.dps=original

    def check_boundary(aa,bb,A,B):
        nonlocal boundary_pairs
        boundary_pairs+=1
        if boundary_pairs>max_boundary_pairs:raise RuntimeError('Boundary budget exhausted; incomplete.')
        boundary_hash.update(f'{aa}:{bb}\n'.encode())
        for delta,u,v in coefficients(A,B):
            if power_ge(u,complement,A,numerator) or power_ge(v,complement,B,numerator):continue
            lx=aa*lp+log_integer(u);ly=bb*lq+log_integer(v)
            # Any borderline height comparison is resolved using the integers.
            if (lx-cap*l10).a>0 or (ly-cap*l10).a>0:continue
            x,y=A*u,B*v
            if not ((cap*l10-log_integer(max(x,y))).a>=0):
                if max(x,y)>Integer(10)**cap:continue
            if not power_ge(max(u,v),denominator,min(x,y),numerator):
                exceptions.append({'p_exponent':aa,'q_exponent':bb,'signed_difference':delta,
                    'p_cofactor':int(u),'q_cofactor':int(v),'smaller_height':int(min(x,y)),
                    'larger_height':int(max(x,y))})

    started=time.monotonic()
    while a<=limits[0] and b<=limits[1]:
        mu,mv=Q,P
        for _,u,v in coefficients(P,Q):mu=min(mu,u);mv=min(mv,v)
        sa=safe_steps(mu,p,a,lp);sb=safe_steps(mv,q,b,lq)
        record={'p_exponent':a,'q_exponent':b,'p_power_bits':P.bit_length(),
                'q_power_bits':Q.bit_length(),'minimum_u_bits':mu.bit_length(),
                'minimum_v_bits':mv.bit_length()}
        if sa<0 and sb<0:
            before=boundary_pairs;bb,B=b,Q
            while bb<=limits[1] and not power_ge(B-difference,complement,P,denominator):
                check_boundary(a,bb,P,B);bb+=1;B*=q
            aa,A=a+1,P*p
            while aa<=limits[0] and not power_ge(A-difference,complement,Q,denominator):
                check_boundary(aa,b,A,Q);aa+=1;A*=p
            da=db=1
            record.update(method='exact boundary lines',boundary_pairs=boundary_pairs-before)
        else:
            da=sa+1 if sa>=0 else 0;db=sb+1 if sb>=0 else 0
            record['method']='CRT strips with directed logarithm comparisons'
        record.update(p_exponent_advance=da,q_exponent_advance=db);anchors.append(record)
        a+=da;b+=db
        if a<=limits[0] and b<=limits[1]:P*=Integer(p)**da;Q*=Integer(q)**db
        if len(anchors)%50==0 or prefix is not None:
            print(f'Pair {p},{q}: {len(anchors)} anchors; bits {P.bit_length()},{Q.bit_length()}; {time.monotonic()-started:.1f}s',flush=True)
    exceptions.sort(key=lambda z:(z['p_exponent'],z['q_exponent'],z['signed_difference']))
    threshold=max(int(gmpy2.iroot(Integer(difference)**denominator,complement)[0])+1,
                  max((r['smaller_height']+1 for r in exceptions),default=1))
    result={'pair':[p,q],'height_cap_power_of_ten':cap,'maximum_difference':difference,
        **({'reciprocal_exponent_denominator':denominator} if numerator==1 else
           {'cofactor_exponent_numerator':numerator,'cofactor_exponent_denominator':denominator}),
        'height_threshold':threshold,'backend':'gmpy2',
        'arithmetic':'Exact extended gcd; directed leading-bit logarithm bounds for power comparisons.',
        'initial_exponents':initial,'maximum_exponents':limits,'final_exponents':[a,b],
        'anchor_count':len(anchors),'exact_boundary_pairs':boundary_pairs,
        'boundary_pairs_sha256':boundary_hash.hexdigest(),'exception_count':len(exceptions),
        'exceptions':exceptions,'anchors':anchors,
        'conclusion':f'max(u,v)^{denominator} >= min(p^a*u,q^b*v)^{numerator} throughout the stated height range'}
    if prefix is not None:
        assert prefix_source is not None
        result['continuation']={
            'source_file':prefix_source['file'],
            'previous_height_cap_power_of_ten':prefix['height_cap_power_of_ten'],
            'retained_anchor_count':prefix['anchor_count'],
            'new_anchor_count':len(anchors)-prefix['anchor_count'],
            'all_retained_boundaries_certified_untruncated':True,
        }
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--clique',nargs='+',type=int,required=True)
    parser.add_argument('--cap',type=int,required=True)
    parser.add_argument('--difference',type=int,required=True)
    parser.add_argument('--exponent',type=Fraction,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--resume',type=Path)
    args=parser.parse_args();records=[]
    prior={} if args.resume is None else {
        tuple(row['pair']):row for row in json.loads(args.resume.read_text())['records']}
    prefix_source=None if args.resume is None else {'file':args.resume.name}
    for p,q in combinations(args.clique,2):
        started=time.monotonic();r=certify(p,q,args.cap,args.difference,exponent=args.exponent,
            prefix=prior.get((p,q)),prefix_source=prefix_source);records.append(r)
        print(json.dumps({k:v for k,v in r.items() if k not in ('anchors','exceptions')}|{'elapsed_seconds':time.monotonic()-started}),flush=True)
        args.output.write_text(json.dumps({'scope':'Finite prime-pair CRT strips with certified logarithmic power comparisons.','records':records},indent=2)+'\n')


if __name__=='__main__':main()

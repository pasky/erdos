"""A line-product proof of effective finiteness at index twelve.

Twenty off-diagonal pair alternatives suffice. Source thresholds are
effective but unevaluated; the algebraic part of the bound is numerical.
No interpolation matrices or binomial-row searches are used.
"""

from fractions import Fraction
import json
from pathlib import Path

from erdos_699_off_diagonal_pairs import certify_record, normalized_edge
from erdos_699_weighted_ramps import capacities, off_maximum_constant

DATA=Path(__file__).with_suffix('.json')
SCALE=10000


def minimal_vectors(primes,edges):
    ids={p:i for i,p in enumerate(primes)}
    vectors=[(0,)*len(primes)]
    for p,q,a,b in edges:
        i,j=ids[p],ids[q];extended=set()
        for v in vectors:
            if v[i]>=a or v[j]>=b:
                extended.add(v)
            else:
                x=list(v);x[i]=a;extended.add(tuple(x))
                x=list(v);x[j]=b;extended.add(tuple(x))
        vectors=[]
        for v in sorted(extended,key=lambda v:(sum(v),v)):
            if not any(all(x<=y for x,y in zip(w,v)) for w in vectors):
                vectors.append(v)
        assert all(any(all(x<=y for x,y in zip(w,v)) for w in vectors)
                   for v in extended)
    assert all(v[ids[p]]>=a or v[ids[q]]>=b
               for v in vectors for p,q,a,b in edges)
    return vectors


def main():
    data=json.loads(DATA.read_text());directory=DATA.parent
    sources=json.loads((directory/data['source_file']).read_text())
    by_edge={normalized_edge(row):row for row in sources['records']}
    edges=[]
    for binding in data['source_bindings']:
        edge,source=tuple(binding['edge']),tuple(binding['source_edge'])
        assert certify_record(by_edge[source])==source
        assert edge[:2]==source[:2] and all(x<=y for x,y in zip(edge[2:],source[2:]))
        assert min(edge[2:])>0 and sum(edge[2:])<SCALE
        edges.append(edge)
    assert [list(e) for e in edges]==data['edges_scaled']
    primes=(2,3,5,7,11);index=12;k=8
    vectors=minimal_vectors(primes,edges)
    assert set(vectors)=={tuple(v) for v in data['minimal_vectors']}
    m=tuple(2*k-t for t in range(index));degree=k*(k+1)
    lists={c+(0,)*(index-len(c)) for v in vectors for c in capacities(v)}
    assert lists=={tuple(c) for c in data['capacity_lists']}
    cost=max(sum(a*b for a,b in zip(m,c)) for c in lists)
    gain=SCALE*(sum(m)-degree)-cost
    assert gain==data['gain_scaled']==1000
    assert all(m[t]>=m[t+1] for t in range(index-1))
    constant,factors=off_maximum_constant(index,m,primes)
    L=sum(t*w for t,w in enumerate(m))
    correction_threshold=1000*(L+2*k*len(primes)*(index-1))
    # Gain1/10 and weighted-ramp inequality: n^(1/10)<=1000*C/(999*2^72).
    numerator=(1000*constant)**10;denominator=(999*2**degree)**10
    cap=max(0,len(str(numerator))-len(str(denominator))+1)
    while 10**cap*denominator<=numerator:cap+=1
    assert 10**cap>=correction_threshold
    result={
        'index':index,'pair_alternatives':len(edges),'minimal_vectors':len(vectors),
        'capacity_lists':len(lists),'line_product_k':k,'total_degree':degree,
        'row_multiplicities':m,'minimum_gain':str(Fraction(gain,SCALE)),
        'off_maximum_prime_factors':factors,'correction_threshold':correction_threshold,
        'algebraic_power_of_ten':cap,
        'conclusion':'Every bad row is below max(10^B,X+11), where X is the maximum effective pair-source threshold.',
        'source_threshold_scope':'Effective but not numerically evaluated.'}
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()

"""Exact bounded enumeration of subsets of a 4-by-4 Eisenstein grid.

It is not a certificate for arbitrary planar sets. Running this file writes
the enumeration's results to the ignored output/ directory beside evidence/.
"""

import json
from pathlib import Path
from collections import Counter, defaultdict
P=[(a,b) for a in range(4) for b in range(4)]
D=sorted({(a-c)**2+(a-c)*(b-d)+(b-d)**2 for i,(a,b) in enumerate(P) for c,d in P[:i]})
nb=[[0]*len(D) for _ in P]
for i,(a,b) in enumerate(P):
    for j,(c,d) in enumerate(P):
        if i!=j:
            v=(a-c)**2+(a-c)*(b-d)+(b-d)**2
            nb[i][D.index(v)]|=1<<j

def canon(S):
    out=[]
    for flip in (False,True):
        Q=[(a+b,-b) if flip else (a,b) for a,b in S]
        for k in range(6):
            a0=min(a for a,b in Q);b0=min(b for a,b in Q)
            out.append(tuple(sorted((a-a0,b-b0) for a,b in Q)))
            Q=[(-b,a+b) for a,b in Q]
    return min(out)

def hull(S):
    S=sorted(S)
    def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lo=[];hi=[]
    for p in S:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    for p in reversed(S):
        while len(hi)>=2 and cross(hi[-2],hi[-1],p)<=0:hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]

counts=[None]*(1<<16);counts[0]=(0,)*len(D)
mins={};r2=defaultdict(dict);counterexamples=[];hist=defaultdict(Counter)
for mask in range(1,1<<16):
    low=mask&-mask;v=low.bit_length()-1;prev=mask^low
    c=tuple(x+(prev&n).bit_count() for x,n in zip(counts[prev],nb[v]))
    counts[mask]=c
    n=mask.bit_count()
    if n<5:continue
    assert sum(c)==n*(n-1)//2
    R=sum(0<x<=n for x in c)
    hist[n][R]+=1
    if n not in mins or R<mins[n]['R']:
        mins[n]={'R':R,'count':1,'sample_mask':mask}
    elif R==mins[n]['R']:mins[n]['count']+=1
    if R<=1:counterexamples.append({'mask':mask,'n':n,'counts':dict(zip(D,c))})
    if R==2:
        S=[p for i,p in enumerate(P) if mask>>i&1]
        key=canon(S)
        if key not in r2[n]:r2[n][key]={'points':key,'grid_occurrences':0,'multiplicities':{d:x for d,x in zip(D,c) if x},'hull_vertices':len(hull(S))}
        r2[n][key]['grid_occurrences']+=1
out={'domain_points':P,'distance_squares':D,'examined_nonempty':(1<<16)-1,'examined_n_ge_5':sum(sum(h.values()) for h in hist.values()),'minimum_R_by_n':mins,'counterexamples':counterexamples,'R2':{n:list(v.values()) for n,v in r2.items()},'histograms':{n:dict(h) for n,h in hist.items()}}
output=Path(__file__).resolve().parent.parent/'output'
output.mkdir(exist_ok=True)
with (output/'eisenstein_grid_results.json').open('w') as f:json.dump(out,f,indent=2)
print('Distance squares:',D)
print('Examined n>=5:',out['examined_n_ge_5'])
print('Counterexamples:',len(counterexamples))
print('n minR minimizers R2sets R2_congruence_classes')
for n,s in mins.items():
    print(n,s['R'],s['count'],hist[n][2],len(r2[n]))
print('R2 canonical representatives:')
for n,v in r2.items():
    for z in v.values():print(json.dumps({'n':n,**z}))

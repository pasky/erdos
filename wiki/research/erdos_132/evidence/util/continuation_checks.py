"""Exact bounded checks of a hexagram, a valuation spectrum and meanders."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations


def axial_spectrum(points):
    out = Counter()
    degrees = [Counter() for _ in points]
    for (i, (a, b)), (j, (c, d)) in combinations(enumerate(points), 2):
        x, y = a-c, b-d
        q = x*x+x*y+y*y
        assert q > 0
        out[q] += 1
        degrees[i][q] += 1
        degrees[j][q] += 1
    return out, degrees


hexagram = [(0,0),(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1),
            (1,1),(-1,2),(-2,1),(-1,-1),(1,-2),(2,-1)]
spec, deg = axial_spectrum(hexagram)
assert spec == {1:24, 3:18, 4:15, 7:12, 9:6, 12:3}
assert Counter(tuple(d[q] for q in sorted(spec)) for d in deg) == {
    (6,6,0,0,0,0):1, (5,2,3,2,0,0):6, (2,3,2,2,2,1):6}

t = (F(2,7), F(8,7))
valuation_example = [(0,0),(1,0),(0,1),t,(t[0]-1,t[1]),(t[0],t[1]-1)]
spec, _ = axial_spectrum(valuation_example)
assert spec == {F(1,7):2, F(3,7):2, F(4,7):1, F(1):8,
                F(12,7):1, F(16,7):1}


def meander(K):
    assert K >= 3 and K % 2 == 1
    points = {(x,4*j) for x in range(K+1) for j in range(K+1)}
    for j in range(K):
        x = K if j % 2 == 0 else 0
        points.update((x,4*j+t) for t in (1,2,3))
    points.update({(-1,0),(-1,4*K)})
    points.update((-2,y) for y in range(4*K+1))
    points.update({(K+1,4),(K+1,5),(K,5)})
    n = len(points)
    assert n == K*K+9*K+7
    edges, deg, diam = 0, Counter(), []
    D2 = (K+2)**2+16*K*K
    for p, q in combinations(points,2):
        d2 = sum((x-y)**2 for x,y in zip(p,q))
        assert 0 < d2 <= D2
        if d2 == 1:
            edges += 1
            deg[p] += 1
            deg[q] += 1
        if d2 == D2:
            diam.append(frozenset((p,q)))
    assert edges == n+1
    assert Counter(deg.values()) == {2:n-1,4:1}
    assert deg[(K,4)] == 4
    assert set(diam) == {frozenset(((-2,0),(K,4*K))),
                         frozenset(((-2,4*K),(K,0)))}


for K in (3,5,9):
    meander(K)
print('Checked: hexagram, six-point valuation spectrum, meanders K=3,5,9.')

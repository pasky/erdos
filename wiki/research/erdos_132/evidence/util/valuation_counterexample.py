"""Exact certificate refuting a valuation-maximum lemma, not Erdős 132."""
from collections import Counter
from fractions import Fraction
from itertools import combinations

# Coordinates in the basis 1, (1 + i*sqrt(3))/2.
points = [(0, 1), (0, 2), (1, 1), (1, 3), (2, 3), (3, 0)]
spectrum = Counter()
for (x, y), (u, v) in combinations(points, 2):
    a, b = x-u, y-v
    spectrum[a*a+a*b+b*b] += 1
assert dict(sorted(spectrum.items())) == {1: 4, 3: 2, 4: 1, 7: 7, 12: 1}
assert sum(spectrum.values()) == 15
odd_max = max(q for q in spectrum if q % 2)
assert odd_max == 7 and spectrum[odd_max] > len(points)
assert sum(1 <= m <= len(points) for m in spectrum.values()) == 4
print(dict(sorted(spectrum.items())))

# Both extremes of the odd shell can be rich.
points9 = [(0, 1), (0, 2), (1, 1), (1, 3), (2, 3), (3, 0),
           (-1, 4), (1, 2), (2, 2)]

def norm_spectrum(points):
    return Counter((x-u)**2 + (x-u)*(y-v) + (y-v)**2
                   for (x, y), (u, v) in combinations(points, 2))

sp9 = norm_spectrum(points9)
assert sp9 == {1: 10, 3: 8, 4: 4, 7: 12, 12: 1, 16: 1}
assert sum(sp9.values()) == 36
assert sp9[1] > 9 and sp9[7] > 9 and sp9[3] <= 9
print(dict(sorted(sp9.items())))

# Three F4 residue classes do not guarantee a rare shell maximum either.
F = Fraction
points5 = [(F(0), F(0)), (F(1), F(0)), (F(0), F(1)),
           (F(-55, 97), F(40, 97)), (F(42, 97), F(-57, 97))]
sp5 = norm_spectrum(points5)
assert sp5 == {F(25, 97): 1, F(27, 97): 1, F(1): 6,
               F(192, 97): 1, F(196, 97): 1}
assert sum(sp5.values()) == 10

def residue2(q):
    assert q.denominator % 2 == 1
    return q.numerator % 2

assert {(residue2(x), residue2(y)) for x, y in points5} == {
    (0, 0), (1, 0), (0, 1)}
odd = [q for q in sp5 if q.numerator % 2 and q.denominator % 2]
assert max(odd) == 1 and sp5[F(1)] == 6 > 5
print(dict(sorted(sp5.items())))

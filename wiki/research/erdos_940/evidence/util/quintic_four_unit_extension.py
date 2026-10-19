"""Exact additional calculation for the strengthened quintic mean floor.

Checks 70 four-unit coefficient profiles modulo 25 and rational arithmetic.
The earlier five-unit minimum 65 and other Euler factors are used from the
existing r5_first_moment.py certificate, not recomputed here.
"""

from fractions import Fraction as F
from itertools import combinations_with_replacement

Q = 25
arrays = []
for j in range(5):
    row = [0] * Q
    for x in range(5):
        row[pow(2, j, Q) * pow(x, 5, Q) % Q] += 1
    arrays.append(row)


def conv(a, b):
    return [sum(a[t] * b[(s - t) % Q] for t in range(Q))
            for s in range(Q)]


least = 5**4
arg = None
profiles = 0
for js in combinations_with_replacement(range(5), 4):
    profiles += 1
    counts = [1] + [0] * (Q - 1)
    for j in js:
        counts = conv(counts, arrays[j])
    counts[0] -= 1  # Exclude the singular all-zero active input pattern.
    value = min(counts)
    if value < least:
        least = value
        arg = (js, counts.index(value))

assert profiles == 70
assert least == 9
print("four-unit profiles, primitive minimum, minimizer:", profiles, least, arg)

u = F(18, 25)
assert 5 * u**5 < 1
z = sum((u**j for j in range(1, 5)), F(0)) / 5
base = (F(25000, 120) * F(1, 2) * F(3, 125) * F(13, 20)
        * F(2, 3) * F(99, 100))
bound = base * (1 + F(45, 13) * z)
assert base == F(429, 400)
assert z == F(734526, 1953125)
assert bound == F(385732347, 156250000)
assert bound > 2
print("strengthened uniform mean lower bound:", bound)

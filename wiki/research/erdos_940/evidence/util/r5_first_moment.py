"""Exact finite certificate for the quintic progression first-moment bound.

The three finite calculations below were run separately; this file
preserves their source combined into one script. Dependencies: numpy, sympy.

Observed exact comparisons:
  small-prime product > 3/125: True
    approximate value 0.02496026410022227
  finite weighted core factor > 25000: True
    floor of exact rational lower bound 26380
  middle-prime product > 13/20: True
    approximate value 0.6519469312995785
  elementary final-tail logarithmic bound < 2/5: True
  resulting uniform unordered mean lower bound: 429/400

NumPy convolution uses int64 arithmetic only, not FFT or floating point.
For p<=491, every intermediate coefficient is <=p**5<2**63.
All comparisons on products use fractions.Fraction.
"""

from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import comb, isqrt

import numpy as np
from sympy import integer_nthroot, primerange, primitive_root


# Part I. Every multiset of five unit-coefficient classes, at p=5 and
# at p == 1 (mod 5), p<=500. There are binomial(9,5)=126 multisets.
P = F(1)
certificate = []
for p, q in [(5, 25)] + [(p, p) for p in primerange(2, 501) if p % 5 == 1]:
    g = int(primitive_root(q))
    arrays = []
    for j in range(5):
        a = np.zeros(q, dtype=np.int64)
        for x in range(p):
            a[(pow(g, j, q) * pow(x, 5, q)) % q] += 1
        arrays.append(a)
    table = {(): np.eye(1, q, 0, dtype=np.int64)[0]}
    least = 10**100
    arg = None
    for k in range(1, 6):
        for t in combinations_with_replacement(range(5), k):
            c = np.convolve(table[t[:-1]], arrays[t[-1]])
            a = c[:q].copy()
            a[:q - 1] += c[q:]
            table[t] = a
            if k == 5:
                a = a.copy()
                a[0] -= 1   # Remove the all-zero, singular input pattern.
                m = int(a.min())
                if m < least:
                    least = m
                    arg = (t, int(a.argmin()))
    den = p ** (3 if q == 25 else 4)
    P *= F(least, den)
    certificate.append((p, least, den, arg))
for row in certificate:
    print(*row)
print('EXACT SMALL-PRIME PRODUCT > 3/125:', P > F(3, 125))
assert P > F(3, 125)


# Part II. Weighted finite canonical cores supported on eligible primes<=1000.
# v/R is an exact rational lower bound for p**(-1/5).
R = 10000
H = F(1)
for p in primerange(2, 1001):
    if p == 5 or p % 5 == 1:
        continue
    v = int(integer_nthroot(R**5 // p, 5)[0])
    assert p * v**5 <= R**5 < p * (v + 1)**5
    z = sum((F(v, R)**s for s in range(1, 5)), F(0)) / p
    H *= sum((comb(5, t) * z**(5 - t) * (1 - F(1, p**(t - 1)))
              for t in range(2, 6)), F(0))
print('EXACT CORE FACTOR > 25000:', H > 25000)
print('FLOOR OF EXACT CORE FACTOR:', H.numerator // H.denominator)
assert H > 25000


# Part III. The refined Gauss bound at 500<p<=5000, p == 1 (mod 5).
# k/R <= sqrt(p), so each factor below is a lower bound for gamma_p.
L = F(1)
for p in primerange(501, 5001):
    if p % 5 != 1:
        continue
    k = isqrt(p * R**2)
    assert k * k <= p * R**2 < (k + 1)**2
    L *= 1 - F(204 * R, p * k) - F(1, p**4)
print('EXACT MIDDLE-PRIME PRODUCT > 13/20:', L > F(13, 20))
assert L > F(13, 20)


# Part IV. Elementary analytic-tail estimates, using sqrt(5000)>70.
S = 2 * (204 * (F(1, 350000) + F(1, 1050))
         + F(1, 5000**4) + F(1, 90 * 5000**3))
print('FINAL-TAIL LOG BOUND < 2/5:', S * F(1000, 999) < F(2, 5))
assert S * F(1000, 999) < F(2, 5)

answer = F(25000, 120) * F(1, 2) * F(3, 125) * F(13, 20) * F(2, 3) * F(99, 100)
print('UNORDERED MEAN LOWER BOUND:', answer)
assert answer == F(429, 400)

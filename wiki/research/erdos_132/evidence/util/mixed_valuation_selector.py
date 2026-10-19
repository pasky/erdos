"""Exact six-point obstruction; not a counterexample to Erdos problem 132."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations


def valuation(q, p):
    a, b = q.numerator, q.denominator
    ans = 0
    while a % p == 0:
        a //= p
        ans += 1
    while b % p == 0:
        b //= p
        ans -= 1
    return ans


points = [
    (F(0), F(0)),
    (F(1), F(0)),
    (F(0), F(1)),
    (F(30, 43), F(48, 43)),
    (F(-815, 4687), F(4200, 4687)),
    (F(4302, 4687), F(115, 4687)),
]
expected_nonunit = {
    (0, 3): F(108, 43),
    (2, 3): F(25, 43),
    (0, 4): F(3175, 4687),
    (1, 4): F(5292, 4687),
    (2, 4): F(277, 4687),
    (0, 5): F(4057, 4687),
    (1, 5): F(25, 4687),
    (2, 5): F(4212, 4687),
}
counts = Counter()
for i, j in combinations(range(6), 2):
    x = points[i][0] - points[j][0]
    y = points[i][1] - points[j][1]
    q = x * x + x * y + y * y
    assert q == expected_nonunit.get((i, j), F(1))
    counts[q] += 1
assert sum(counts.values()) == 15
assert counts[F(1)] == 7 and len(counts) == 9
shell = [q for q in counts if valuation(q, 2) == 0]
assert len(shell) == 6
assert {valuation(q, 3) for q in shell} == {0}
assert max(shell) == 1 and counts[max(shell)] > len(points)
assert sum(m <= len(points) for m in counts.values()) == 8
for q, multiplicity in sorted(counts.items()):
    print(q, multiplicity, valuation(q, 2), valuation(q, 3))

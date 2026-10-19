"""Count actual three-layer blocks for type-class cell sets.

Exact integer and rational arithmetic; repository tools harness and Python
standard library. For each retained instance (m, alpha, q) the checker builds
the type class S_m of the cells (0,1), (2,1), (2,2) with base-three
coordinates, verifies its size, the injectivity of y-x and the three
projection sizes, checks the hypothesis (4-alpha)q>=16*27^m+1 of L198, keeps the
cells whose q+y-x is prime (trial division), solves the congruences, places
the block of floor(alpha P) positive integers from the proof and counts the
integers in it divisible by a kept prime directly, each once. It checks that
every kept prime has exactly three multiples in the block and that the count
equals |X|+|Y|+|W|. Runtime a few seconds at most. These finite instances
illustrate the lemma and its conventions; they prove no general statement.
"""
import json
import sys
from fractions import Fraction
from itertools import permutations
from math import comb, factorial, isqrt
from pathlib import Path
from tools import Checker, evidence_parser


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for divisor in range(3, isqrt(n) + 1, 2):
        if n % divisor == 0:
            return False
    return True


def type_class(base, m):
    cells = set()
    for word in set(permutations([0] * m + [1] * m + [2] * m)):
        x = sum(base[c][0] * 3 ** i for i, c in enumerate(word))
        y = sum(base[c][1] * 3 ** i for i, c in enumerate(word))
        cells.add((x, y))
    return sorted(cells)


def solve_congruences(pairs):
    z, modulus = 0, 1
    for residue, prime in pairs:
        step = ((residue - z) * pow(modulus, -1, prime)) % prime
        z, modulus = z + modulus * step, modulus * prime
    return z % modulus, modulus


def main():
    evidence_parser(__doc__, quick=False).parse_args()
    checker = Checker()
    assets = Path(__file__).resolve().parent / 'assets'
    data = json.loads((assets / 'instances.json').read_text())
    base = [tuple(cell) for cell in data['base_cells']]
    checker.check('base cells are the three cells of L201',
                  base == [(0, 1), (2, 1), (2, 2)])
    for row in data['instances']:
        m, q = row['m'], row['q']
        alpha = Fraction(row['alpha'])
        label = f'm={m} alpha={alpha} q={q}'
        cells = type_class(base, m)
        omega = 27 ** m
        X = {x for x, y in cells}
        Y = {y for x, y in cells}
        W = {2 * y - x for x, y in cells}
        checker.check(f'{label}: |S_m|=(3m)!/(m!)^3 with distinct y-x',
                      len(cells) == factorial(3 * m) // factorial(m) ** 3
                      and len({y - x for x, y in cells}) == len(cells))
        checker.check(f'{label}: each projection has C(3m,m) values',
                      len(X) == len(Y) == len(W) == comb(3 * m, m))
        checker.check(f'{label}: |x|,|y|<=27^m and (4-alpha)q>=16*27^m+1',
                      all(abs(x) <= omega and abs(y) <= omega for x, y in cells)
                      and Fraction(3) <= alpha < 4
                      and (4 - alpha) * q >= 16 * omega + 1)
        kept = [(x, y) for x, y in cells if is_prime(q + y - x)]
        primes = [q + y - x for x, y in kept]
        P = max(primes)
        K = (alpha * P).numerator // (alpha * P).denominator
        z, modulus = solve_congruences([((-x) % p, p) for (x, y), p in zip(kept, primes)])
        start = max(z - q + 3 * omega + 1, z + 2 * q + 3 * omega + 1 - K)
        feasible = start <= min(z - omega, z + 3 * q - 5 * omega - K)
        checker.check(f'{label}: block start satisfies the four endpoint inequalities', feasible)
        shift = 0 if start >= 1 else (1 - start + modulus - 1) // modulus
        z, start = z + shift * modulus, start + shift * modulus
        multiples = set()
        exactly_three = True
        for p in primes:
            first = -(-start // p) * p
            mine = list(range(first, start + K, p))
            exactly_three &= len(mine) == 3
            multiples.update(mine)
        Xs = {x for x, y in kept}
        Ys = {y for x, y in kept}
        Ws = {2 * y - x for x, y in kept}
        checker.check(f'{label}: block is positive with K=floor(alpha P)>=3P',
                      start >= 1 and 3 * P <= K <= alpha * P < K + 1)
        checker.check(f'{label}: every kept prime has exactly three multiples in the block',
                      exactly_three)
        checker.check(f'{label}: direct count equals |X|+|Y|+|W| of the kept cells',
                      len(multiples) == len(Xs) + len(Ys) + len(Ws))
        checker.check(f'{label}: retained prime and multiple counts reproduce',
                      (len(primes), len(multiples)) == (row['primes'], row['count']),
                      f'got {len(primes)} primes, {len(multiples)} multiples')
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

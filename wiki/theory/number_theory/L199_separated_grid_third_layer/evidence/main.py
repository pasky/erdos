"""Brute-force the separated-grid obstruction on small prime grids.

Exact integer and rational arithmetic; repository tools harness and Python
standard library. For each retained separated grid of primes q+a_i+b_j, cell
subset S and ratio alpha, the checker verifies the hypotheses of L199, solves
z = a_i modulo every prime of S, and counts directly, each integer once, the
multiples of the primes of S in every block of K=floor(alpha P) consecutive
integers that contains all row and column locations, and in every block
inside [z-2q+1, z+4q-1]. It checks |T_S|>=ceil(u/2), that the least count
over the first family is r_S+s_S+|T_S| and is attained by [z-q+1, z-q+K],
and that the least count over the second family is at least ceil(u/2). For
the full grids with arithmetic-progression offsets it also checks the
research page's equality |T|=rs-(r-1)floor(s/2). Runtime a few seconds at most.
These finite instances illustrate the claim; they prove nothing beyond them.
"""
import json
import sys
from fractions import Fraction
from math import isqrt
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


def solve_congruences(pairs):
    z, modulus = 0, 1
    for residue, prime in pairs:
        step = ((residue - z) * pow(modulus, -1, prime)) % prime
        z, modulus = z + modulus * step, modulus * prime
    return z % modulus, modulus


def count(start, length, primes):
    found = set()
    for p in primes:
        found.update(range(-(-start // p) * p, start + length, p))
    return len(found)


def main():
    evidence_parser(__doc__, quick=False).parse_args()
    checker = Checker()
    assets = Path(__file__).resolve().parent / 'assets'
    data = json.loads((assets / 'grids.json').read_text())
    for grid in data['grids']:
        q, A, B = grid['q'], grid['A'], grid['B']
        r, s = len(A), len(B)
        name = f'q={q} A={A} B={B}'
        full = [(i, j) for i in range(r) for j in range(s)]
        grid_primes = [q + A[i] + B[j] for i, j in full]
        checker.check(f'{name}: separated grid of distinct primes with 2a_r+3b_s<q',
                      all(is_prime(p) for p in grid_primes)
                      and len(set(grid_primes)) == len(grid_primes)
                      and A[0] == B[0] == 0 and A == sorted(set(A)) and B == sorted(set(B))
                      and all(A[i + 1] - A[i] > B[-1] for i in range(r - 1))
                      and 2 * A[-1] + 3 * B[-1] < q)
        if grid['ap_pattern']:
            T = {a + 2 * b for a in A for b in B}
            checker.check(f'{name}: full third layer has rs-(r-1)floor(s/2) values',
                          len(T) == r * s - (r - 1) * (s // 2))
        for subset in grid['subsets']:
            S = [tuple(cell) for cell in subset]
            u = len(S)
            primes = [q + A[i] + B[j] for i, j in S]
            P = max(primes)
            rows = {i for i, j in S}
            cols = {j for i, j in S}
            T = {A[i] + 2 * B[j] for i, j in S}
            z, _ = solve_congruences([(A[i] % p, p) for (i, j), p in zip(S, primes)])
            core = [z - A[i] for i in rows] + [z + q + B[j] for j in cols]
            target = len(rows) + len(cols) + len(T)
            for text in grid['alphas']:
                alpha = Fraction(text)
                K = (alpha * P).numerator // (alpha * P).denominator
                label = f'{name} S={subset} alpha={alpha}'
                checker.check(f'{label}: alpha>=3 and 3P<=K<4q', alpha >= 3 and 3 * P <= K < 4 * q)
                checker.check(f'{label}: |T_S|>=ceil(u/2)', 2 * len(T) >= u)
                core_counts = [count(L, K, primes)
                               for L in range(max(core) - K + 1, min(core) + 1)]
                checker.check(f'{label}: least count over core-containing blocks is r_S+s_S+|T_S|',
                              min(core_counts) == target,
                              f'least {min(core_counts)}, expected {target}')
                checker.check(f'{label}: block [z-q+1, z-q+K] attains it',
                              count(z - q + 1, K, primes) == target)
                window = [count(L, K, primes) for L in range(z - 2 * q + 1, z + 4 * q - K + 1)]
                checker.check(f'{label}: every block in the window has at least ceil(u/2)',
                              2 * min(window) >= u, f'least {min(window)}')
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

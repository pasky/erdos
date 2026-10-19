"""Formal power series in three variables and exact relation counts.

A series is a dict from exponent triples to integer coefficients reduced
modulo the prime ``PRIME``, truncated at total degree ``n``. The variables
``Y_p, Y_q, Y_r`` are independent of the slopes: each staircase exponent is
decided exactly by ``flog``. A finite family of series ``M_1, ..., M_t`` has a
polynomial relation ``sum_i c_i M_i = 0`` with ``c_i`` in ``Q[Y]`` of total
degree at most ``d`` exactly when the columns ``Y^alpha M_i`` (``|alpha| <= d``)
are linearly dependent over ``Q``. Truncation keeps every true relation, and
full column rank modulo ``PRIME`` implies full column rank over ``Q`` because
the matrix has integer entries. A positive relation count can therefore be a
truncation artifact, while a zero count proves that no relation exists.
"""

from __future__ import annotations

import itertools

import numpy as np

from smooth import flog

__all__ = [
    'PRIME',
    'Series',
    'staircase_series',
    'face_series',
    'prime_power_series',
    'pair_series',
    'two_prime_series',
    'multiply',
    'monomial_family',
    'relation_count',
]

# fix the prime modulus and the series type
PRIME = 2**31 - 1
Series = dict[tuple[int, int, int], int]


def _add(ser: Series, e: tuple[int, int, int], n: int) -> None:
    """Add one to the coefficient of Y**e when its total degree is at most n."""
    if sum(e) <= n:
        ser[e] = (ser.get(e, 0) + 1) % PRIME


def staircase_series(primes: tuple[int, int, int], n: int) -> Series:
    """Return S(Y) = sum over all smooth m of Y**phi(m), truncated at degree n.

    Here phi(m) is the exponent vector of the running lcm at m. Since phi(m)
    dominates the exponent vector of m, only exponents a + b + c <= n matter.
    """
    p, q, r = primes
    ser: Series = {}
    for a in range(n + 1):
        for b in range(n + 1 - a):
            for c in range(n + 1 - a - b):
                m = p**a * q**b * r**c
                _add(ser, (flog(p, m), flog(q, m), flog(r, m)), n)
    return ser


def face_series(
    primes: tuple[int, int, int], keep: tuple[int, int, int], n: int
) -> Series:
    """Return the part of S(Y) over smooth m whose zero-flagged exponents vanish."""
    p, q, r = primes
    ser: Series = {}
    for a in range(n + 1 if keep[0] else 1):
        for b in range(n + 1 - a if keep[1] else 1):
            for c in range(n + 1 - a - b if keep[2] else 1):
                m = p**a * q**b * r**c
                _add(ser, (flog(p, m), flog(q, m), flog(r, m)), n)
    return ser


def prime_power_series(primes: tuple[int, int, int], u: int, n: int) -> Series:
    """Return A_u(Y) = sum_{j >= 0} Y**phi(u**j) with the full three-prime lcm."""
    ser: Series = {}
    j = 0
    while True:
        t = u**j
        e = tuple(flog(w, t) for w in primes)
        if sum(e) > n:
            return ser
        _add(ser, e, n)
        j += 1


def pair_series(primes: tuple[int, int, int], u: int, v: int, n: int) -> Series:
    """Return A_{u;v}(Y) = sum_{j >= 0} Y_u**j Y_v**floor(log_v u**j)."""
    ser: Series = {}
    j = 0
    while True:
        e = [0, 0, 0]
        e[primes.index(u)] = j
        e[primes.index(v)] = flog(v, u**j)
        if sum(e) > n:
            return ser
        _add(ser, (e[0], e[1], e[2]), n)
        j += 1


def two_prime_series(primes: tuple[int, int, int], u: int, v: int, n: int) -> Series:
    """Return the two-prime running-lcm series of {u, v} in Y_u, Y_v."""
    ser: Series = {}
    iu, iv = primes.index(u), primes.index(v)
    for i in range(n + 1):
        for j in range(n + 1 - i):
            m = u**i * v**j
            e = [0, 0, 0]
            e[iu], e[iv] = flog(u, m), flog(v, m)
            _add(ser, (e[0], e[1], e[2]), n)
    return ser


def multiply(s1: Series, s2: Series, n: int) -> Series:
    """Return the product of two series truncated at total degree n."""
    out: Series = {}
    for e1, v1 in s1.items():
        for e2, v2 in s2.items():
            e = (e1[0] + e2[0], e1[1] + e2[1], e1[2] + e2[2])
            if sum(e) <= n:
                out[e] = (out.get(e, 0) + v1 * v2) % PRIME
    return out


def monomial_family(
    s: Series, base: dict[str, Series], degree: int, n: int
) -> list[tuple[str, Series]]:
    """Return S**k times each monomial of degree at most degree - k in base."""
    one: Series = {(0, 0, 0): 1}
    out = []
    power = one
    for k in range(degree + 1):
        for size in range(degree - k + 1):
            for combo in itertools.combinations_with_replacement(sorted(base), size):
                ser = power
                for name in combo:
                    ser = multiply(ser, base[name], n)
                out.append((f'S^{k}*' + '*'.join(combo), ser))
        power = multiply(power, s, n)
    return out


def relation_count(funcs: list[Series], d: int, n: int) -> tuple[int, int, int]:
    """Return (columns, rank modulo PRIME, equations met by some column).

    The columns are Y**alpha * M_i for every |alpha| <= d, truncated at total
    degree n; columns minus rank counts the relations over Z/PRIME.
    """
    # index the monomials of total degree at most n
    index = {}
    for total in range(n + 1):
        for a in range(total + 1):
            for b in range(total - a + 1):
                index[(a, b, total - a - b)] = len(index)
    shifts = [e for e in index if sum(e) <= d]
    # fill one row per column of the relation system
    rows = np.zeros((len(funcs) * len(shifts), len(index)), dtype=np.int64)
    k = 0
    for ser in funcs:
        for s in shifts:
            for e, v in ser.items():
                f = (e[0] + s[0], e[1] + s[1], e[2] + s[2])
                if sum(f) <= n:
                    rows[k, index[f]] = v
            k += 1
    met = int(np.count_nonzero(rows.any(axis=0)))
    # eliminate modulo PRIME, updating blocks of rows to bound memory
    rank = 0
    for c in range(rows.shape[1]):
        if rank == rows.shape[0]:
            break
        nz = np.nonzero(rows[rank:, c])[0]
        if nz.size == 0:
            continue
        piv = rank + int(nz[0])
        if piv != rank:
            rows[[rank, piv]] = rows[[piv, rank]]
        inv = pow(int(rows[rank, c]), PRIME - 2, PRIME)
        rows[rank, c:] = (rows[rank, c:] * inv) % PRIME
        prow = rows[rank, c:]
        others = np.nonzero(rows[rank + 1 :, c])[0] + rank + 1
        for start in range(0, others.size, 128):
            block = others[start : start + 128]
            factor = rows[block, c].reshape(-1, 1)
            rows[block, c:] = (rows[block, c:] - (factor * prow) % PRIME) % PRIME
        rank += 1
    return rows.shape[0], rank, met

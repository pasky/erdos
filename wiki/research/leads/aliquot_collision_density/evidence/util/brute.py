"""Compute the collision census directly from proper-divisor sums.

This is the independent small-range reference for ``census.cpp``. It sums
proper divisors by a divisor sieve (every d contributes to its proper
multiples), counts prime factors with multiplicity by repeated division,
and counts collisions with dictionaries, sharing no code with the compiled
census.
"""

from __future__ import annotations

from collections import Counter

__all__ = [
    'census',
]


def census(xs: list[int], hist_js: list[int], mode: int) -> dict[str, object]:
    """Return the census report for checkpoints ``xs`` in the parsed format.

    Args:
        xs: Increasing checkpoints; the last is the range ``X``.
        hist_js: Checkpoint indices at which fiber-size histograms are taken.
        mode: 0 flags inputs with at least three prime factors, 1 flags
            inputs whose largest prime factor exceeds their square root.

    Returns:
        A dict with ``R``, ``C`` and ``H`` keyed like the parsed C++ report,
        plus ``PRIMES`` and ``OMEGA2`` keyed by checkpoint index.

    """
    big = xs[-1]
    # proper divisor sums
    s = [0] * (big + 1)
    for d in range(1, big // 2 + 1):
        for m in range(2 * d, big + 1, d):
            s[m] += d
    # prime factors with multiplicity, by trial division with a smallest-factor table
    spf = list(range(big + 1))
    p = 2
    while p * p <= big:
        if spf[p] == p:
            for m in range(p * p, big + 1, p):
                if spf[m] == m:
                    spf[m] = p
        p += 1
    omega = [0] * (big + 1)
    largest = [1] * (big + 1)
    for n in range(2, big + 1):
        omega[n] = omega[n // spf[n]] + 1
        largest[n] = max(spf[n], largest[n // spf[n]])
    # classes of each composite input
    inputs = []
    for n in range(2, big + 1):
        if omega[n] < 2:
            continue
        ell = 0
        while (s[n] << ell) < n and ell < 15:
            ell += 1
        flag = omega[n] >= 3 if mode == 0 else largest[n] ** 2 > n
        inputs.append((n, s[n], ell, 1 if flag else 0))
    out_r: dict[tuple[str, int], int] = {}
    out_c: dict[tuple[str, int], int] = {}
    out_h: dict[tuple[int, str, int], int] = {}
    primes: dict[int, int] = {}
    omega2: dict[int, int] = {}
    for j, x in enumerate(xs):
        primes[j] = sum(1 for n in range(2, x + 1) if omega[n] == 1)
        omega2[j] = sum(1 for n in range(2, x + 1) if omega[n] == 2)
        for w, prefix in enumerate(('D', 'DF', 'DN')):
            for k in range(16):
                name = f'{prefix}{k}'
                fiber = Counter(
                    v
                    for n, v, ell, flag in inputs
                    if n <= x and ell <= k and (w == 0 or flag == (1 if w == 1 else 0))
                )
                out_r[name, j] = sum(fiber.values())
                out_c[name, j] = sum(t * t for t in fiber.values())
                if j in hist_js:
                    for t, cnt in Counter(fiber.values()).items():
                        out_h[j, name, t] = cnt
    return {'R': out_r, 'C': out_c, 'H': out_h, 'PRIMES': primes, 'OMEGA2': omega2}

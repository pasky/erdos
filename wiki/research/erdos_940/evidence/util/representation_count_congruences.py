"""Preserve the bounded representation-count diagnostic through 100000.

This calculation concerns unordered sums of exactly five fifth-powerful
positive integers. It is not an asymptotic certificate and excludes no
eventual congruence. It fails if any tested residue class lacks a witness.

Requires NumPy. For scope and the arithmetic bound preventing overflow,
see ../../representation_count_congruences.md.
"""

import numpy as np

X = 100000
A = [1]
for p in (2, 3, 5, 7):
    old = A[:]
    q = p**5
    while q <= X:
        A += [a * q for a in old if a * q <= X]
        q *= p
A = sorted(A)
assert len(A) == len(set(A))

dp = np.zeros((6, X + 1), dtype=np.int64)
dp[0, 0] = 1
for a in A:
    for k in range(1, 6):
        dp[k, a:] += dp[k - 1, : X + 1 - a]

print(
    "full_count", len(A),
    "max_U5", int(dp[5].max()),
    "total_U5", int(dp[5].sum()),
)
for modulus, ell in [(8, 2), (32, 2), (25, 5), (125, 5), (49, 7), (121, 11)]:
    missing = []
    witnesses = []
    for a in range(modulus):
        inds = np.arange(a, X + 1, modulus)
        ok = inds[(dp[5, inds] % ell) != 0]
        if not len(ok):
            missing.append(a)
        else:
            witnesses.append(int(ok[-1]))
    print(
        "target_modulus", modulus,
        "count_prime", ell,
        "classes_without_nonzero_witness", missing,
        "min_last_witness", min(witnesses) if witnesses else None,
    )
    assert not missing, (modulus, ell, missing)

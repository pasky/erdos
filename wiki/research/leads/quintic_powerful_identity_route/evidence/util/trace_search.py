"""Search for four-term identities of the Z/3-trace shape

    sum_{k=0}^{2} (Q o M^k)^5 = I^5,   M(U,V) = (-V, U-V),  M^3 = 1,

with Q a binary form of degree d (2 or 3) and I an M-invariant form of
degree d, over the complex or the real numbers. Every such identity is a
four-term identity of fifth powers of forms of degree d; over the rationals
all four terms would be rational.

Unknowns: the d+1 coefficients of Q and the coordinates of I in the space of
M-invariant forms of degree d (spanned by U^2-UV+V^2 for d=2, and by
UV(U-V) and 2U^3-3U^2V-3UV^2+2V^3 for d=3). Levenberg-Marquardt from random
starts; solutions with a small Q or small I are discarded.

Usage (needs numpy): python3 trace_search.py {complex|real} {2|3} [starts]
"""
import sys

import numpy as np

FIELD = sys.argv[1] if len(sys.argv) > 1 else 'complex'
DEG = int(sys.argv[2]) if len(sys.argv) > 2 else 3
NSTART = int(sys.argv[3]) if len(sys.argv) > 3 else 2000
rng = np.random.default_rng(int(sys.argv[4]) if len(sys.argv) > 4 else 0)
CPLX = FIELD == 'complex'
DT = complex if CPLX else float

# forms as coefficient arrays, highest power of U first
if DEG == 2:
    INV = [np.array([1, -1, 1], dtype=DT)]
else:
    INV = [np.array([0, 1, -1, 0], dtype=DT), np.array([2, -3, -3, 2], dtype=DT)]
NC = DEG + 1
NI = len(INV)
NU = NC + NI
NE = 5 * DEG + 1


def ppow(q, n):
    r = np.array([1], dtype=DT)
    for _ in range(n):
        r = np.convolve(r, q)
    return r


def compose_M(q):
    """Coefficients of Q(-V, U-V) for Q with coefficients q (degree DEG)."""
    # Q = sum q_k U^(d-k) V^k ; substitute U -> -V, V -> U - V
    out = np.zeros(NC, dtype=DT)
    Upow = [ppow(np.array([0, -1], dtype=DT), a) for a in range(NC)]   # (-V)^a
    Vpow = [ppow(np.array([1, -1], dtype=DT), b) for b in range(NC)]   # (U-V)^b
    for k in range(NC):
        term = q[k] * np.convolve(Upow[DEG - k], Vpow[k])
        out += term
    return out


def trace5(q):
    q1 = compose_M(q)
    q2 = compose_M(q1)
    return ppow(q, 5) + ppow(q1, 5) + ppow(q2, 5)


def residual(x):
    q = x[:NC]
    I = sum(x[NC + i] * INV[i] for i in range(NI))
    return trace5(q) - ppow(I, 5)


def jacobian(x, h=1e-7):
    J = np.zeros((NE, NU), dtype=DT)
    r0 = residual(x)
    for k in range(NU):
        e = np.zeros(NU, dtype=DT)
        e[k] = h
        J[:, k] = (residual(x + e) - r0) / h
    return J


def solve_from(x0, iters=400):
    x = x0.copy()
    lam = 1e-3
    for _ in range(iters):
        r = residual(x)
        nr = np.linalg.norm(r)
        if nr < 1e-14:
            break
        J = jacobian(x)
        A = J.conj().T @ J + lam * np.eye(NU)
        b = -J.conj().T @ r
        try:
            dx = np.linalg.solve(A, b)
        except np.linalg.LinAlgError:
            break
        xn = x + dx
        nrn = np.linalg.norm(residual(xn))
        if nrn < nr:
            x, lam = xn, max(lam / 3, 1e-15)
        else:
            lam = min(lam * 5, 1e6)
        if not np.all(np.isfinite(x)):
            return x, np.inf
    return x, np.linalg.norm(residual(x))


found = []
counts = {'fail': 0, 'degenerate': 0, 'clean': 0}
for _ in range(NSTART):
    x0 = rng.normal(size=NU).astype(DT)
    if CPLX:
        x0 = x0 + 1j * rng.normal(size=NU)
    x, nr = solve_from(x0)
    q = x[:NC]
    I = sum(x[NC + i] * INV[i] for i in range(NI))
    scale = max(np.linalg.norm(ppow(q, 5)), np.linalg.norm(ppow(I, 5)), 1e-300)
    if not np.isfinite(nr) or nr > 1e-12 * scale:
        counts['fail'] += 1
        continue
    if np.linalg.norm(q) < 1e-3 or np.linalg.norm(I) < 1e-3 * np.linalg.norm(q):
        counts['degenerate'] += 1
        continue
    # the three rotated forms must be pairwise non-proportional
    q1 = compose_M(q)
    if NC == 2 and abs(q[0] * q1[1] - q[1] * q1[0]) < 1e-8 * np.linalg.norm(q) ** 2:
        counts['degenerate'] += 1
        continue
    counts['clean'] += 1
    found.append((nr, x))
print(FIELD, 'degree', DEG, counts)
np.set_printoptions(precision=6, suppress=True, linewidth=160)
seen = []
for nr, x in found:
    q = x[:NC]
    # normalize by the scaling symmetry Q -> t Q, I -> t I
    t = q[np.argmax(np.abs(q))]
    key = np.abs(np.round(np.concatenate([q / t, x[NC:] / t]), 5))
    if any(np.allclose(key, s, atol=1e-4) for s in seen):
        continue
    seen.append(key)
    print(f'class {len(seen)} residual {nr:.1e}: Q = {q / t}, I-coordinates = {x[NC:] / t}')
    q1 = compose_M(q / t)
    q2 = compose_M(q1)
    print('   Q o M =', q1, ' Q o M^2 =', q2)
print('distinct classes:', len(seen))

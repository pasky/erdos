"""Exploratory multi-start search for four-term identities of fifth powers of
binary forms, Q1^5 + Q2^5 + Q3^5 + Q4^5 = 0, with Q1..Q4 binary forms of one
degree d over the complex or the real numbers.

Retained by the lead quintic_powerful_identity_route as an exploratory
computation, not as evidence for any claim. Every form of degree 5*d whose
linear factors all have multiplicity at least 5 is a constant times a fifth
power when d = 2, so at d = 2 the search covers all four-term identities of
5-powerful binary forms of degree 10 up to the identification of constants
with fifth powers (which is exact over the complex numbers and, for signs and
absolute values, over the reals). At d = 3 it covers only the shape "fifth
power of a cubic", not the mixed shapes L^6 M^9, L^7 M^8.

Method: Q4 is fixed to one representative of each orbit of the projective
linear group (three distinct roots, a conjugate pair, repeated roots), the
coefficients of Q1, Q2, Q3 are unknowns, and the vanishing of all 5d+1
coefficients of the sum of fifth powers is solved by Levenberg-Marquardt from
random starting points. A solution is kept as clean when its residual is
below 1e-13 relative to the size of the fifth powers, no form is smaller
than a tenth of the largest, no proper subsum Q_i^5 + Q_j^5 is below a
hundredth of the largest fifth power, the four forms are not nearly
proportional and they have no common root;
otherwise it is a degenerate limit (a vanishing subsum or a common factor,
which the iteration approaches but never reaches exactly). Clean solutions
are grouped by the gauge-invariant quantities printed at the end.

Usage (needs numpy):

    python3 quintic_identity_search.py complex 2 2000
    python3 quintic_identity_search.py real 2 2000
    python3 quintic_identity_search.py real 3 2000
"""
import sys

import numpy as np

FIELD = sys.argv[1] if len(sys.argv) > 1 else 'complex'
DEG = int(sys.argv[2]) if len(sys.argv) > 2 else 2
NSTART = int(sys.argv[3]) if len(sys.argv) > 3 else 1000
SEED = int(sys.argv[4]) if len(sys.argv) > 4 else 0
rng = np.random.default_rng(SEED)
CPLX = FIELD == 'complex'
DT = complex if CPLX else float

# A binary form of degree d is stored as its d+1 coefficients, highest power
# of U first: (c_0, ..., c_d) means sum c_k U^(d-k) V^k.
if DEG == 2:
    GAUGES = {'UV': [0, 1, 0], 'U^2': [1, 0, 0]}
    if not CPLX:
        GAUGES['U^2+V^2'] = [1, 0, 1]
elif DEG == 3:
    GAUGES = {'UV(U-V)': [0, 1, -1, 0], 'U^2V': [0, 1, 0, 0], 'U^3': [1, 0, 0, 0]}
    if not CPLX:
        GAUGES['V(U^2+V^2)'] = [0, 1, 0, 1]
else:
    raise SystemExit('degree 2 or 3 only')

NC = DEG + 1          # coefficients per form
NU = 3 * NC           # unknowns
NE = 5 * DEG + 1      # equations


def ppow(q, n):
    r = np.array([1], dtype=DT)
    for _ in range(n):
        r = np.convolve(r, q)
    return r


def run_gauge(name, q4):
    q4 = np.array(q4, dtype=DT)
    q4_5 = ppow(q4, 5)

    def forms(x):
        return [x[NC * i:NC * (i + 1)] for i in range(3)]

    def residual(x):
        return sum(ppow(q, 5) for q in forms(x)) + q4_5

    def jacobian(x):
        J = np.zeros((NE, NU), dtype=DT)
        for i, q in enumerate(forms(x)):
            q4p = 5 * ppow(q, 4)
            for k in range(NC):
                e = np.zeros(NC, dtype=DT)
                e[k] = 1
                J[:, NC * i + k] = np.convolve(q4p, e)
        return J

    def solve_from(x0, iters=300):
        x = x0.copy()
        lam = 1e-3
        for _ in range(iters):
            r = residual(x)
            nr = np.linalg.norm(r)
            if nr < 1e-15:
                return x, nr
            J = jacobian(x)
            A = J.conj().T @ J + lam * np.eye(NU)
            b = -J.conj().T @ r
            try:
                dx = np.linalg.solve(A, b)
            except np.linalg.LinAlgError:
                return x, nr
            xn = x + dx
            nrn = np.linalg.norm(residual(xn))
            if nrn < nr:
                x, lam = xn, max(lam / 3, 1e-15)
            else:
                lam = min(lam * 5, 1e6)
            if not np.all(np.isfinite(x)):
                return x, np.inf
        return x, np.linalg.norm(residual(x))

    def classify(x, nr):
        qs = forms(x) + [q4]
        p = [ppow(q, 5) for q in qs]
        pscale = max(np.linalg.norm(t) for t in p)
        if nr > 1e-13 * pscale:
            return 'inexact'
        qscale = max(np.linalg.norm(q) for q in qs)
        if min(np.linalg.norm(q) for q in qs) < 0.1 * qscale:
            return 'degenerate'
        for i in range(4):
            for j in range(i + 1, 4):
                if np.linalg.norm(p[i] + p[j]) < 1e-2 * pscale:
                    return 'degenerate'
        # all four forms nearly proportional (the limit shape of most runs)
        mat = np.array([q / np.linalg.norm(q) for q in qs])
        sv = np.linalg.svd(mat, compute_uv=False)
        if sv[1] < 1e-2 * sv[0]:
            return 'degenerate'
        # a common linear factor of all four forms divides Q4: test its roots
        lead = [i for i in range(NC) if abs(q4[i]) > 1e-12]
        roots = list(np.roots(q4[lead[0]:])) if len(lead) > 0 and lead[0] < NC - 1 else []
        at_infinity = lead[0] > 0 if lead else True
        for rho in roots:
            vals = [abs(np.polyval(q, rho)) / (np.linalg.norm(q) * max(1, abs(rho)) ** DEG) for q in forms(x)]
            if max(vals) < 1e-3:
                return 'degenerate'
        if at_infinity and max(abs(q[0]) / np.linalg.norm(q) for q in forms(x)) < 1e-3:
            return 'degenerate'
        return 'clean'

    counts = {'inexact': 0, 'degenerate': 0, 'clean': 0, 'fail': 0}
    clean = []
    for _ in range(NSTART):
        x0 = rng.normal(size=NU).astype(DT)
        if CPLX:
            x0 = x0 + 1j * rng.normal(size=NU)
        x0 = x0 * rng.choice([0.3, 1.0, 3.0])
        x, nr = solve_from(x0)
        if not np.isfinite(nr) or nr > 1e-9:
            counts['fail'] += 1
            continue
        c = classify(x, nr)
        counts[c] += 1
        if c == 'clean':
            clean.append((nr, x))
    print(f'gauge Q4 = {name}: {counts}')
    return clean


def invariants(x):
    """Quantities unchanged by the diagonal gauge U -> t U, V -> V / t and by
    multiplying a form by a fifth root of unity: for degree 2 the moduli of
    the middle coefficient, of the product of the outer coefficients, and of
    the discriminant of each of Q1, Q2, Q3."""
    out = []
    for i in range(3):
        q = x[NC * i:NC * (i + 1)]
        if DEG == 2:
            out.append((abs(q[1]), abs(q[0] * q[2]), abs(q[1] ** 2 - 4 * q[0] * q[2])))
        else:
            out.append(tuple(abs(v) for v in q))
    return sorted(out)


np.set_printoptions(precision=6, suppress=True, linewidth=160)
for name, q4 in GAUGES.items():
    clean = run_gauge(name, q4)
    seen = []
    for nr, x in clean:
        inv = np.array(invariants(x))
        if any(np.allclose(inv, s, atol=1e-6) for s in seen):
            continue
        seen.append(inv)
        print(f'  clean class {len(seen)} (residual {nr:.1e}):')
        for i in range(3):
            print(f'    Q{i+1} =', x[NC * i:NC * (i + 1)])
        print('    invariants:', inv.tolist())
    print(f'  distinct clean classes in this gauge: {len(seen)}')

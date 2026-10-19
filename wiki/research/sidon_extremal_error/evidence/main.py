"""Check the finite computations behind the Sidon extremal-error notes.

Checked clauses:

1. Exact pseudo-moments (Theorem 2 of the linear-capacity note). For sample
   pairs (N, k), including an additional feasible boundary point (48,8),
   the family x_i = y, X_ii = y,
   X_ij = y^2 - lambda*max(w - r(i,j), 0) satisfies every constraint of R(N,k)
   in exact rational arithmetic: the row identity, the Laplacian form of
   X - y^2 J (nonpositive off-diagonal entries, zero row sums), the pair
   literals, every difference capacity and every sum capacity. For small N the
   least eigenvalue of X - y^2 J is also computed in floating point as a
   control. The integer conditions (a)-(d) of the proof hold for every k in the
   closed-form range for every N from 48 to the run's bound. As a negative
   control, the first k beyond the family's limit violates the capacity at d=1.
2. Window inequality. Every sample point of clause 1 satisfies
   k^2 T <= (N+T-1)(k+T-1) for every T, as every point of R(N,k) must.
3. Rotated perturbed lattice (the alternative realization). For sample (N, k),
   the exact
   expected difference counts of the unconditioned process, multiplied by the
   conditioning factor phi of the proof, stay below 1 for every d; the expected
   number of colliding pairs is below 1/2 + 0.01; and the sum-capacity bound of
   the proof is below 1. The counts are integers divided by W^2 N.
   The autocorrelation is counted
   directly and its convolution with the triangular kernel is computed by
   exact integer second differences; every capacity comparison is rational.
4. Singer arcs. For each sample prime q a Singer set modulo q^2+q+1 is built
   from a primitive cubic, checked to be a perfect difference set, and every
   arc of every unit dilate is checked to lie within sqrt(q)(1 + ln(M/2)) of its
   mean; the largest deviation divided by sqrt(q) is checked to lie in
   [1.18, 1.43], the range quoted in the note.
5. Circulant linear program (full run only). For N = 1000 the feasibility
   linear program over circulant pseudo-moments (uniform first moments,
   X_ij depending only on cyclic distance, all Fourier modes nonnegative, row
   identity, difference capacities, pair-literal bounds) is reported feasible
   by the HiGHS solver at k = sqrt(N) + 0.583 N^(1/4) and infeasible at
   k = sqrt(N) + 0.596 N^(1/4). This is an uncertified floating-point
   computation. The program omits sum capacities; the bracket certifies
   nothing beyond the solver's reports for this auxiliary program.
6. Lattice short-pair statistics (Monte Carlo, fixed seed). For the rotated
   perturbed lattice with N = 4000, k = 65, W = 265 and 20000 samples, the
   sample variance of the number S_D of pairs with difference at most D = 398
   is below one fifth of the sample mean of sum_d P_d(P_d - 1), the number of
   ordered pairs of distinct pairs with a common difference at most D.
   The samples are unconditioned labeled positions, so coincidences are
   allowed. This diagnoses the model but does not certify a degree-four
   functional or the sign of its repaired moment matrix.
7. Short-count covariance. Enumerate every outcome of the unrotated block law
   at (s,W)=(2,4), (3,4), (3,6), (4,6), and compare every mean and covariance
   for 1<=d,e<W with the exact edge-intersection formulas and the two-kernel
   decomposition. These checks are rational and run in both modes.

Run from the repository root:
    uv run --no-sync python wiki/research/sidon_extremal_error/evidence/main.py

Dependencies: numpy, scipy and the installed root ``tools`` package. No inputs
or output files; deterministic. The full run uses under 3 GiB on its largest
sample and takes about a minute. ``--quick`` uses smaller samples and takes a
few seconds. Run with one thread. Limitation: clauses 1, 3 and 4
check finitely many parameters; the theorems for all N rest on the written
proofs, and clause 3 checks the unconditioned expectations with the proof's
bound for the conditioning, not the conditioned law directly.
"""

from __future__ import annotations

import itertools
import math
from fractions import Fraction

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix, csr_matrix, vstack
from util.short_counts import check_short_counts

import tools

__all__ = [
    'circulant_feasible',
    'family_ok',
    'lattice_bound',
    'main',
    'singer_set',
]


def family_conditions(N: int, k: int) -> bool:
    """Return the integer conditions (a)-(d) of the Theorem 2 proof."""
    w = k * k - N
    return (
        w >= 2
        and 2 * w <= N
        and k * (w + 1) >= N
        and w * w <= N * (k - 1)
        and 2 * k <= N
    )


def in_closed_form_range(N: int, k: int) -> bool:
    """Test sqrt(N)+1 <= k <= sqrt(N)+N^(1/4)/2-1/4 exactly."""
    if k < 1 or (k - 1) ** 2 < N:
        return False
    a = 4 * k + 1
    # a <= 4 sqrt(N)+2 N^(1/4), with a>4 sqrt(N) in this domain.
    return (a * a + 16 * N) ** 2 <= (8 * a + 4) ** 2 * N


def family_ok(N: int, k: int) -> tuple[bool, str]:
    """Check every constraint of R(N,k) for the explicit family, exactly."""
    w = k * k - N
    y = Fraction(k, N)
    lam = (y - y * y) / (w * (w - 1))
    half = N // 2
    f = [Fraction(0)] * (half + 1)
    for r in range(1, half + 1):
        f[r] = lam * max(w - r, 0)
    fr = lambda d: f[min(d, N - d)]
    # row identity: the off-diagonal weights of one row sum to y - y^2
    if sum(fr(j) for j in range(1, N)) != y - y * y:
        return False, 'row identity'
    # Laplacian form: nonnegative weights
    if any(v < 0 for v in f):
        return False, 'negative weight'
    # pair literals
    for r in range(1, half + 1):
        X = y * y - f[r]
        if not (0 <= X <= y and 1 - 2 * y + X >= 0):
            return False, f'literal at distance {r}'
    # difference capacities
    for d in range(1, N):
        if (N - d) * (y * y - fr(d)) > 1:
            return False, f'difference capacity at {d}'
    # sum capacities: X depends only on |i-j|, so sum over pairs i<j, i+j=s
    for s in range(0, 2 * N - 1):
        lo = max(0, s - (N - 1))
        tot = Fraction(0)
        for i in range(lo, (s + 1) // 2):
            j = s - i
            if j <= N - 1 and i < j:
                tot += y * y - fr(j - i)
        if s % 2 == 0 and s // 2 <= N - 1:
            tot += y
        if tot > 1:
            return False, f'sum capacity at {s}'
    return True, ''


def integer_tent_convolution(N: int, k: int, W: int) -> tuple[np.ndarray, np.ndarray]:
    """Return the exact cyclic autocorrelation convolved with the tent, and tent.

    If G = a*t and t(d)=(W-|d|)_+ cyclically, then
    G(d+1)-2G(d)+G(d-1)=a(d-W)-2a(d)+a(d+W).
    Two integer initial values and two prefix sums determine every entry.
    """
    if not (W >= 2 and 2 * W < N and 1 <= k <= N):
        raise ValueError('tent convolution parameters')
    if 6 * N * k * k >= 2**63:
        raise ValueError('integer convolution accumulator could overflow')
    lattice = (np.arange(k, dtype=np.int64) * N) // k
    differences = (lattice[:, None] - lattice[None, :]) % N
    auto = np.bincount(differences.ravel(), minlength=N).astype(np.int64)
    del differences
    tent = np.zeros(N, dtype=np.int64)
    offsets = np.arange(-(W - 1), W, dtype=np.int64)
    tent[offsets % N] = W - np.abs(offsets)
    initial = int(np.dot(auto, tent))
    first_step = int(np.dot(auto, np.roll(tent, 1) - tent))
    second_difference = np.roll(auto, W) + np.roll(auto, -W) - 2 * auto
    steps = np.empty(N - 1, dtype=np.int64)
    steps[0] = first_step
    steps[1:] = first_step + np.cumsum(second_difference[1:-1])
    result = np.empty(N, dtype=np.int64)
    result[0] = initial
    result[1:] = initial + np.cumsum(steps)
    # G is symmetric, so G(N-1)=G(1)=G(0)+first_step.
    if int(result[-1]) != initial + first_step:
        raise ValueError('cyclic convolution boundary identity')
    return result, tent


def lattice_bound(N: int, k: int) -> tuple[Fraction, Fraction, Fraction]:
    """Return exact max phi*E r(d), expected collisions, and sum bound."""
    # The integer correction makes the cube root choice exact even if the
    # floating estimate is one unit away from the correct ceiling.
    cube_ceiling = round((N * N) ** (1 / 3))
    while cube_ceiling**3 < N * N:
        cube_ceiling += 1
    while (cube_ceiling - 1) ** 3 >= N * N:
        cube_ceiling -= 1
    W = k * k - N + cube_ceiling
    convolution, tent = integer_tent_convolution(N, k, W)
    numerators = convolution - k * tent
    if int(numerators.min()) < 0 or N * int(numerators.max()) >= 2**63:
        raise ValueError('difference-count numerator or accumulator')
    maximum = int(((N - np.arange(1, N)) * numerators[1:]).max())
    s = Fraction(N, k)
    eps = s * s / (3 * W * W) + Fraction(2, W) + 2 * s / (W * W)
    collisions = Fraction(int(numerators[0]), 2 * W * W)
    pnc = 1 - collisions
    if pnc <= 0:
        raise ValueError('no positive conditioning bound')
    phi = 1 + 2 * (1 + eps) / (s * pnc)
    sum_bound = Fraction(k * k, 2 * N) * phi * (1 + eps) + Fraction(k, N) / pnc
    return phi * Fraction(maximum, N * W * W), collisions, sum_bound


def circulant_feasible(N: int, k: float) -> bool:
    """Return the solver's verdict on the circulant feasibility program at (N, k)."""
    y = k / N
    H = N // 2
    r = np.arange(1, H + 1)
    mult = np.where((N % 2 == 0) & (r == H), 1, 2).astype(float)
    xi = np.arange(1, N // 2 + 1)
    A_psd = mult[None, :] * np.cos(2 * np.pi * np.outer(xi, r) / N)
    d = np.arange(1, N)
    A_cap = coo_matrix(
        (-np.ones(N - 1), (d - 1, np.minimum(d, N - d) - 1)), shape=(N - 1, H)
    ).tocsr()
    A_ub = vstack([csr_matrix(A_psd), A_cap])
    b_ub = np.concatenate([np.full(len(xi), y - y * y), 1.0 / (N - d) - y * y])
    res = linprog(
        np.zeros(H),
        A_ub=A_ub,
        b_ub=b_ub,
        A_eq=mult[None, :],
        b_eq=[y - y * y],
        bounds=[(y * y - y, y * y)] * H,
        method='highs',
        options={'threads': 1, 'parallel': False},
    )
    if res.status not in (0, 2):
        raise RuntimeError(
            f'circulant solver did not decide feasibility: {res.message}'
        )
    return res.status == 0


def singer_set(q: int) -> tuple[int, list[int]]:
    """Return M = q^2+q+1 and a Singer set for prime q via a primitive cubic."""
    M = q * q + q + 1
    order = q**3 - 1

    def mul(u: tuple[int, int, int], a: int, b: int, c: int) -> tuple[int, int, int]:
        # multiply u0 + u1 x + u2 x^2 by x modulo x^3 + a x^2 + b x + c
        t = u[2]
        return ((-c * t) % q, (u[0] - b * t) % q, (u[1] - a * t) % q)

    for a, b, c in itertools.product(range(q), repeat=3):
        if c == 0 or any((r**3 + a * r * r + b * r + c) % q == 0 for r in range(q)):
            continue
        p = (1, 0, 0)
        S = set()
        primitive = True
        for i in range(order):
            if i > 0 and p == (1, 0, 0):
                primitive = False
                break
            if p[2] == 0:
                S.add(i % M)
            p = mul(p, a, b, c)
        if primitive and len(S) == q + 1:
            return M, sorted(S)
    raise ValueError(q)


def singer_arcs(q: int) -> tuple[bool, float, float]:
    """Return (perfect, max arc deviation / sqrt q, ceiling / sqrt q)."""
    M, S = singer_set(q)
    perfect = sorted((x - z) % M for x in S for z in S if x != z) == list(range(1, M))
    ind = np.zeros(M, dtype=np.int64)
    worst = 0.0
    for t in range(1, M):
        if math.gcd(t, M) != 1:
            continue
        ind[:] = 0
        ind[[(t * x) % M for x in S]] = 1
        cs = np.concatenate([[0], np.cumsum(np.concatenate([ind, ind]))])
        for L in range(1, M):
            dev = np.abs(cs[L : L + M] - cs[:M] - (q + 1) * L / M).max()
            worst = max(worst, float(dev))
    return perfect, worst / math.sqrt(q), (1 + math.log(M / 2))


def main() -> int:
    """Run the checks; return the exit code."""
    parser = tools.evidence_parser(
        'Check the finite computations behind the Sidon extremal-error notes.'
    )
    args = parser.parse_args()
    checker = tools.Checker()

    # clause 1: exact family at sample points and the closed-form range
    samples = (
        [(48, 8), (100, 11), (410, 22)]
        if args.quick
        else [(48, 8), (100, 11), (410, 22), (1000, 34), (2000, 48)]
    )
    for N, k in samples:
        ok, why = family_ok(N, k)
        checker.check(
            f'family satisfies R({N},{k}) exactly', family_conditions(N, k) and ok, why
        )
    for N in (48, 100):
        k = dict(samples)[N]
        w, y = k * k - N, k / N
        lam = (y - y * y) / (w * (w - 1))
        idx = np.arange(N)
        r = np.minimum(
            np.abs(idx[:, None] - idx[None, :]), N - np.abs(idx[:, None] - idx[None, :])
        )
        C = -lam * np.maximum(w - r, 0).astype(float)
        np.fill_diagonal(C, y - y * y)
        checker.check(
            f'X - y^2 J is positive semidefinite at N={N} (float control)',
            bool(np.linalg.eigvalsh(C).min() > -1e-12),
        )
    bound = 20000 if args.quick else 200000
    bad = [
        (N, k)
        for N in range(48, bound + 1)
        for k in range(
            math.isqrt(N) + 1,
            math.isqrt(N) + math.isqrt(math.isqrt(N)) // 2 + 2,
        )
        if in_closed_form_range(N, k) and not family_conditions(N, k)
    ]
    checker.check(
        f'conditions (a)-(d) hold on the closed-form range for 48 <= N <= {bound}',
        not bad,
        str(bad[:3]),
    )
    N, k = 2000, 48
    while family_conditions(N, k + 1):
        k += 1
    k += 1
    w, y = k * k - N, Fraction(k, N)
    lam = (y - y * y) / (w * (w - 1))
    checker.check(
        'negative control: beyond the family limit the capacity at d=1 fails',
        (N - 1) * (y * y - lam * (w - 1)) > 1,
    )

    # clause 2: window inequality at the sample points
    for N, k in samples:
        checker.check(
            f'window inequality holds for every T at ({N},{k})',
            all(k * k * T <= (N + T - 1) * (k + T - 1) for T in range(1, N + 1)),
        )

    # clause 3: perturbed lattice at sample parameters, with a small direct
    # convolution control independent of the second-difference recurrence.
    small_N, small_k, small_W = 101, 10, 21
    computed, tent = integer_tent_convolution(small_N, small_k, small_W)
    sites = [(j * small_N) // small_k for j in range(small_k)]
    direct = [
        sum(int(tent[(d - (b - a)) % small_N]) for a in sites for b in sites)
        for d in range(small_N)
    ]
    checker.check(
        'integer tent recurrence agrees with direct pair enumeration',
        computed.tolist() == direct,
    )
    lat = [(10**6, 0.35)] if args.quick else [(10**6, 0.35), (16 * 10**6, 0.395)]
    for N, coef in lat:
        k = math.floor(math.sqrt(N) + coef * N**0.25)
        top, coll, sb = lattice_bound(N, k)
        checker.check(
            f'lattice capacity maximum {float(top):.7f} < 1 at N={N}, k={k}',
            top < 1,
        )
        checker.check(
            f'expected colliding pairs below 0.51 at N={N}',
            coll < Fraction(51, 100),
            f'{float(coll):.10f}',
        )
        checker.check(
            f'sum-capacity bound below 1 at N={N}', sb < 1, f'{float(sb):.10f}'
        )
    if not args.quick:
        beyond, _, _ = lattice_bound(16000000, 4028)
        checker.check(
            f'finite conditioning bound exceeds one at (16000000,4028): {float(beyond):.7f}',
            beyond > 1,
        )

    # clause 4: Singer arcs
    primes = [5, 7] if args.quick else [5, 7, 11, 13, 17]
    for q in primes:
        perfect, ratio, ceiling = singer_arcs(q)
        checker.check(f'Singer set for q={q} is a perfect difference set', perfect)
        checker.check(
            f'arc deviations within the ceiling for q={q}',
            ratio < ceiling,
            f'{ratio} vs {ceiling}',
        )
        checker.check(
            f'largest deviation / sqrt(q) in [1.18, 1.43] for q={q}',
            1.18 <= ratio <= 1.43,
            f'{ratio}',
        )

    # clause 5: circulant linear program bracket (full run only)
    if not args.quick:
        N = 1000
        lo, hi = math.sqrt(N) + 0.583 * N**0.25, math.sqrt(N) + 0.596 * N**0.25
        checker.check(
            'circulant program feasible at coefficient 0.583 (N=1000, solver report)',
            circulant_feasible(N, lo),
        )
        checker.check(
            'circulant program infeasible at coefficient 0.596 (N=1000, solver report)',
            not circulant_feasible(N, hi),
        )

    # clause 6: short-pair variance against repeated differences (Monte Carlo)
    rng = np.random.default_rng(1)
    N, k, W, D = 4000, 65, 265, 398
    L = (np.arange(k) * N) // k
    S, R2 = [], []
    for _ in range(20000 if not args.quick else 4000):
        P = np.sort((rng.integers(N) + L + rng.integers(0, W, size=k)) % N)
        diff = P[None, :] - P[:, None]
        mask = (diff > 0) & (diff <= D)
        S.append(int(mask.sum()))
        cnt = np.bincount(diff[mask], minlength=D + 1)
        R2.append(int((cnt * (cnt - 1)).sum()))
    ratio = float(np.var(S) / np.mean(R2))
    checker.check(
        'lattice: Var(S_D) < 0.2 * E sum_d P_d(P_d-1)', ratio < 0.2, f'{ratio}'
    )

    check_short_counts(checker)
    return checker.finish()


if __name__ == '__main__':
    raise SystemExit(main())

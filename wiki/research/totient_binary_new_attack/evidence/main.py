"""Finite checks for the fresh attack on the binary totient series.

Checks, in exact integer and rational arithmetic (python-flint for LLL, Hermite
normal forms and ranks; Python integers elsewhere):

1. Column generation at powers of two. For J = 2^m, 3 <= m <= 13, the
   normalized columns (phi(k)/2, phi(k+J)/2), J < k <= 2J, generate Z^2;
   the columns at k = 3J/2 and k = 2J have minor -2^(2m-3); and, for
   6 <= m <= 13, explicit primes p in (J,2J) with p = 3 mod 4 and P in
   (2J,3J] with P = 3 mod 4, 15 | P-J, give an odd minor. (At m = 4, 5 no
   such P exists; generation there is the direct index check.)
2. Exact shadow image. For J in {8, 12, 16, 20, 24, 32, 48, 64}, a weighted
   LLL basis of the kernel lattice L_J on [J,2J] is verified to be a basis
   (Gram determinant equals |U|^2/gcd(U)^2) and its shadows (u,v) generate
   exactly 2^J Z x 2Z.
3. Structural vectors. For y in {5, 7, 13} and J in {16, 32, 48, 64}, the
   functional u(z) = sum z_n 2^n lies in the rational span of the
   y-structural constraints, so every y-structural vector on [J,2J] has
   u = 0; at J = 64, y = 5 the complementary pair of the proof is exhibited.
4. Kernel cost profile (finite observation). For J in {16, 32, 64, 128} the
   verified LLL basis of L_J has every cost at most 2 J^2 and contains an
   odd vector of cost at most 2 J^2.
5. Longer supports (control). For y in {7, 13} and J in {16, 24, 32}, on the
   support [4, 3J] the functional u is NOT in the span of the y-structural
   constraints, so the short-support hypothesis of the zero-shadow
   proposition cannot be dropped.
6. Perturbation construction on a prefix (perturbation_barrier.md). With
   c = 1/4, s(n) = floor(c log2 n), g(n) = max(1, s(n)), e_1 = 64 and
   e_(k+1) = e_k + g(e_k), the greedy choice of Proposition 1 is run in exact
   rational arithmetic for the targets r in {11/8, 4/3, 1, 3/2} through
   e_k <= 3000, with S replaced by its partial sum S_M, M = 3200; this is the
   exact construction for the target r + (S - S_M), itself an instance of
   Proposition 1. Every step k >= 2 is checked to satisfy
   delta_k = 0 mod 2^s(e_k), |delta_k| <= e_k^(1/2) and
   |eta_k| <= 2^(s(e_k) - e_k - 1). A control with g doubled must violate
   the size bound.
7. Coprime-pair identities (proof_sketch.md). For 2 <= n <= 2000,
   #{1 <= a < n : gcd(a, n - a) = 1} = phi(n); the coefficients of
   Z(x,y) = sum_{gcd(a,c)=1} x^a y^c satisfy Z = xy + Z(xy,y) + Z(x,xy)
   through total degree 80; and for (u,v) in {(1,1), (1,2), (2,3)} the
   Mobius sum sum_d mu(d)/((2^(du)-1)(2^(dv)-1)) agrees with the coprime-pair
   sum to within 2^-100, both truncated with explicit tail bounds.

8. Small dilation designs (dilation_designs.md). The six-point design with
   plus points (0,0), (4,10), (5,9) and minus points (1,1), (6,12), (2,6)
   cancels levels 1..3 and the twelve-point design listed in the code
   cancels levels 1..4; both have distinct first coordinates, and each fails
   to cancel the next level (control). The map (a,b) -> (43+30a,30b)
   realizes the three-level design with distinct primes; trial division
   verifies them, and exact CRT verifies compatible square congruences.
9. Fixed-prime robust witnesses (partial_multiplicativity.md). Five retained
   vectors in assets/robust_kernel_vectors.json are checked against every
   affine rough-part constraint, their totient kernel, parity and cost.
   These are returned vectors, not minima. Changing one coefficient is a
   control that must fail the kernel condition.
10. Complete smooth-orbit rounding (partial_multiplicativity.md, bound (4)).
   For y in {2,3}, use composite rough parts e=a+jQ, with (a,Q)=(15,30)
   or (35,210), and target binary sum zero modulo coefficient changes of
   four. Certified rational intervals for S and each full orbit weight
   determine eight or six rounding decisions. The uniform signed size
   bounds and the resulting fixed-prime laws, prime-power values and
   congruences are checked through n=10000. This tests a finite prefix of
   the signed construction; it does not compute the positive comparison
   interval of L220 or certify the infinite target by a finite sum.
11. Residue lifting (residue_lifting.md). For 2<=m<=64 and zero-block
   starts 0<=N<=128, exact partial sums with a certified positive tail
   bound verify D_m <= (m+2)2^-m and 2^N D_m >= m/2. The first altered
   coefficient is computed directly.

These are finite checks of the stated instances. The asymptotic statements
are proved on the owning pages; check 1 verifies the column lemma at the
listed J without the prime number theorem.

Command (repository root): uv run --no-sync python
wiki/research/totient_binary_new_attack/evidence/main.py [--quick]
Runtime: a few seconds; --quick restricts check 1 to m <= 8, check 2 to
J <= 24, checks 3 and 5 to J <= 32 and J = 16, check 4 to J <= 64, check 6
to e_k <= 1000 and check 7 to n <= 500; checks 8-11 are the same in both modes.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from math import gcd
from pathlib import Path

from flint import fmpq_mat, fmpz_mat

from tools import Checker, evidence_parser


def require(condition: bool, message: str) -> None:
    """Reject a failed internal obligation even under python -O."""
    if not condition:
        raise ValueError(message)


def totients(limit: int) -> list[int]:
    """Return phi(0..limit) by a sieve (phi(0) = 0 is unused)."""
    ph = list(range(limit + 1))
    for p in range(2, limit + 1):
        if ph[p] == p:
            for k in range(p, limit + 1, p):
                ph[k] -= ph[k] // p
    return ph


def is_prime(n: int) -> bool:
    """Trial division primality, adequate for the sizes used here."""
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def prefix(ph: list[int]) -> list[int]:
    """Return Phi_0..Phi_M with Phi_n = 2 Phi_(n-1) + phi(n)."""
    out = [0] * len(ph)
    for n in range(1, len(ph)):
        out[n] = 2 * out[n - 1] + ph[n]
    return out


def lattice_index_2d(vectors: list[tuple[int, int]]) -> int:
    """Index in Z^2 of the lattice generated by integer vectors (0 if rank < 2)."""
    rows = [list(v) for v in vectors if v != (0, 0)]
    if len(rows) < 2:
        return 0
    h = fmpz_mat(rows).hnf()
    piv = [(int(h[i, 0]), int(h[i, 1])) for i in range(h.nrows())]
    piv = [r for r in piv if r != (0, 0)]
    if len(piv) < 2:
        return 0
    return abs(piv[0][0] * piv[1][1] - piv[0][1] * piv[1][0])


def check_columns(chk: Checker, mmax: int) -> None:
    """Check 1: the normalized columns generate Z^2 at J = 2^m."""
    for m in range(3, mmax + 1):
        J = 1 << m
        ph = totients(3 * J)
        a = [x // 2 for x in ph]
        cols = [(a[k], a[k + J]) for k in range(J + 1, 2 * J + 1)]
        idx = lattice_index_2d(cols)
        chk.check(f'columns generate Z^2 at J=2^{m}', idx == 1, f'index {idx}')
        c1 = (a[3 * J // 2], a[5 * J // 2])
        c2 = (a[2 * J], a[3 * J])
        minor = c1[0] * c2[1] - c2[0] * c1[1]
        chk.check(
            f'power-of-two minor at J=2^{m}',
            minor == -(1 << (2 * m - 3)),
            f'minor {minor}',
        )
        if m < 6:
            continue
        p = next((q for q in range(J + 1, 2 * J) if q % 4 == 3 and is_prime(q)), None)
        P = next(
            (
                q
                for q in range(2 * J + 1, 3 * J + 1)
                if q % 4 == 3 and (q - J) % 15 == 0 and is_prime(q)
            ),
            None,
        )
        ok = p is not None and P is not None
        if ok:
            k = P - J
            odd_minor = a[p] * a[P] - a[k] * a[p + J]
            ok = (
                a[p] % 2 == 1 and a[P] % 2 == 1 and a[k] % 2 == 0 and odd_minor % 2 == 1
            )
        chk.check(f'explicit odd minor at J=2^{m}', ok, f'p={p} P={P}')


def kernel_basis(
    J: int, ph: list[int], Phi: list[int]
) -> tuple[list[int], list[int], list[list[int]]]:
    """Weighted LLL basis of L_J = {z on [J,2J] : sum z_n U_J(n) = 0}, verified."""
    ns = list(range(J, 2 * J + 1))
    U = [Phi[n + J] - (Phi[n] << J) for n in ns]
    w = [n + J + 2 for n in ns]
    d = len(ns)
    K = 1 << (J + 40)
    rows = [[w[i] if c == i else 0 for c in range(d)] + [K * U[i]] for i in range(d)]
    L = fmpz_mat(rows).lll(delta=0.999)
    basis = []
    for i in range(L.nrows()):
        if int(L[i, d]) == 0:
            z = [int(L[i, c]) // w[c] for c in range(d)]
            require(
                all(int(L[i, c]) == z[c] * w[c] for c in range(d)), 'weight division'
            )
            basis.append(z)
    return ns, U, basis


def is_kernel_basis(U: list[int], basis: list[list[int]]) -> bool:
    """A set of len(U)-1 kernel vectors is a basis iff its Gram determinant is |U|^2/g^2."""
    if len(basis) != len(U) - 1:
        return False
    if any(sum(x * y for x, y in zip(z, U)) != 0 for z in basis):
        return False
    g = 0
    for x in U:
        g = gcd(g, x)
    B = fmpz_mat(basis)
    gram = int((B * B.transpose()).det())
    return gram * g * g == sum(x * x for x in U)


def check_shadow_image(chk: Checker, Js: list[int]) -> None:
    """Check 2: the shadows of a verified kernel basis generate 2^J Z x 2Z."""
    for J in Js:
        ph = totients(3 * J + 4)
        Phi = prefix(ph)
        ns, U, basis = kernel_basis(J, ph, Phi)
        chk.check(f'verified kernel basis at J={J}', is_kernel_basis(U, basis))
        sh = [
            (sum(c << n for c, n in zip(z, ns)), sum(c * Phi[n] for c, n in zip(z, ns)))
            for z in basis
        ]
        h = fmpz_mat([list(s) for s in sh]).hnf()
        piv = [(int(h[i, 0]), int(h[i, 1])) for i in range(h.nrows())]
        piv = [r for r in piv if r != (0, 0)]
        ok = (
            len(piv) == 2
            and piv[0] == (1 << J, piv[0][1])
            and piv[1] == (0, 2)
            and piv[0][1] % 2 == 0
        )
        chk.check(f'shadow image is 2^J Z x 2Z at J={J}', ok, f'HNF {piv}')


def rough_split(m: int, primes: list[int]) -> tuple[int, int]:
    """Return (y-smooth part, y-rough part) of m."""
    s = 1
    for p in primes:
        while m % p == 0:
            m //= p
            s *= p
    return s, m


def u_in_structural_span(y: int, J: int, B: int, R: int) -> bool:
    """Test whether u lies in the span of the y-structural constraints.

    The functional is u = sum z_n 2^n for vectors z on [B,R] at depth J, whose
    window positions are [B+1,R+J]; the span is taken over the rationals.
    """
    primes = [p for p in range(2, y + 1) if is_prime(p)]
    ph = totients(R + J + 4)
    ns = list(range(B, R + 1))
    groups: dict[int, list[tuple[int, int]]] = {}
    for m in range(B + 1, R + J + 1):
        s, k = rough_split(m, primes)
        groups.setdefault(k, []).append((m, s))
    rows = []
    for G in groups.values():
        row = [0] * len(ns)
        for m, s in G:
            for i, n in enumerate(ns):
                if m - J <= n <= m - 1:
                    row[i] += ph[s] << (J - m + n)
        rows.append(row)
    return fmpq_mat(rows).rank() == fmpq_mat([*rows, [1 << n for n in ns]]).rank()


def check_structural(chk: Checker, ys: list[int], Js: list[int]) -> None:
    """Check 3: u lies in the span of the y-structural constraints on [J,2J]."""
    for y in ys:
        for J in Js:
            chk.check(
                f'u in span of {y}-structural constraints at J={J}',
                u_in_structural_span(y, J, J, 2 * J),
            )
    # the complementary pair used in the proof, at J = 64 >= 2*30, y = 5
    J, primes = 64, [2, 3, 5]
    pair = next(
        (
            r
            for r in range(J // 2 + 1, J + 1)
            if rough_split(J + r, primes)[0] == 1
            and rough_split(2 * J + r, primes)[0] == 1
        ),
        None,
    )
    chk.check(
        'complementary 5-rough pair exists at J=64', pair is not None, f'r={pair}'
    )


def check_profile(chk: Checker, Js: list[int]) -> None:
    """Check 4: every verified LLL basis vector costs at most 2 J^2; an odd one exists."""
    for J in Js:
        ph = totients(3 * J + 4)
        Phi = prefix(ph)
        ns, U, basis = kernel_basis(J, ph, Phi)
        require(is_kernel_basis(U, basis), f'basis at J={J}')
        costs = [sum(abs(c) * (n + J + 2) for c, n in zip(z, ns)) for z in basis]
        odd = [
            cst
            for cst, z in zip(costs, basis)
            if sum(c * Phi[n] for c, n in zip(z, ns)) % 4 == 2
        ]
        chk.check(
            f'basis costs at most 2J^2 at J={J}',
            max(costs) <= 2 * J * J,
            f'max {max(costs)}',
        )
        chk.check(
            f'odd basis vector of cost at most 2J^2 at J={J}',
            bool(odd) and min(odd) <= 2 * J * J,
            f'min odd {min(odd) if odd else None}',
        )


def check_long(chk: Checker, ys: list[int], Js: list[int]) -> None:
    """Check 5: on [4,3J] the functional u escapes the structural span."""
    for y in ys:
        for J in Js:
            chk.check(
                f'u not in span of {y}-structural constraints on [4,{3 * J}] at J={J}',
                not u_in_structural_span(y, J, 4, 3 * J),
            )


def greedy_steps(
    r: Fraction, S: Fraction, emax: int, gscale: int
) -> list[tuple[int, int, int, Fraction]]:
    """Run the greedy of Proposition 1; return (e_k, s(e_k), delta_k, eta_k) for k >= 1."""

    def s_of(n: int) -> int:
        return (n.bit_length() - 1) // 4

    def g_of(n: int) -> int:
        return gscale * max(1, s_of(n))

    out = []
    eta = r - S
    e = 64
    while e <= emax:
        s = s_of(e)
        x = eta * 2 ** (e - s)
        delta = (2**s) * round(x)
        eta = eta - Fraction(delta, 2**e)
        out.append((e, s, delta, eta))
        e += g_of(e)
    return out


def check_barrier(chk: Checker, emax: int) -> None:
    """Check 6: the inequality chain of Proposition 1 on a finite prefix."""
    M = 3200
    ph = totients(M)
    S = sum(Fraction(ph[n], 2**n) for n in range(1, M + 1))
    for r in (Fraction(11, 8), Fraction(4, 3), Fraction(1), Fraction(3, 2)):
        steps = greedy_steps(r, S, emax, 1)
        ok_res = all(d % (2**s) == 0 for _, s, d, _ in steps)
        ok_size = all(d * d <= e for e, _, d, _ in steps[1:])
        ok_eta = all(abs(eta) <= Fraction(2**s, 2 ** (e + 1)) for e, s, _, eta in steps)
        chk.check(
            f'greedy residues, sizes and errors for r={r} through e={emax}',
            ok_res and ok_size and ok_eta,
            f'{len(steps)} steps',
        )
    # control: doubling the gaps must break the size bound somewhere
    steps = greedy_steps(Fraction(11, 8), S, emax, 2)
    chk.check(
        'control: doubled gaps violate the size bound',
        any(d * d > e for e, _, d, _ in steps[1:]),
    )


def mobius(limit: int) -> list[int]:
    """Return mu(0..limit) by a sieve (mu(0) unused)."""
    mu = [1] * (limit + 1)
    is_comp = [False] * (limit + 1)
    for p in range(2, limit + 1):
        if not is_comp[p]:
            for k in range(2 * p, limit + 1, p):
                is_comp[k] = True
            for k in range(p, limit + 1, p):
                mu[k] = -mu[k]
            for k in range(p * p, limit + 1, p * p):
                mu[k] = 0
    return mu


def check_coprime(chk: Checker, nmax: int) -> None:
    """Check 7: the coprime-pair form of S and its Euclidean functional equation."""
    ph = totients(nmax)
    ok = all(
        sum(1 for a in range(1, n) if gcd(a, n - a) == 1) == ph[n]
        for n in range(2, nmax + 1)
    )
    chk.check(f'coprime pairs with sum n number phi(n) for 2<=n<={nmax}', ok)
    D = 80
    Z = {
        (a, c)
        for a in range(1, D)
        for c in range(1, D)
        if a + c <= D and gcd(a, c) == 1
    }
    rhs: dict[tuple[int, int], int] = {(1, 1): 1}
    for a, c in Z:
        for key in ((a, a + c), (a + c, c)):
            if sum(key) <= D:
                rhs[key] = rhs.get(key, 0) + 1
    chk.check(
        f'Z = xy + Z(xy,y) + Z(x,xy) through total degree {D}',
        rhs == dict.fromkeys(Z, 1),
    )
    L, K = 200, 300
    mu = mobius(L)
    for u, v in ((1, 1), (1, 2), (2, 3)):
        # both sums scaled by 2^K and truncated termwise: each term loses less than one unit
        direct = sum(
            1 << (K - a * u - c * v)
            for a in range(1, L)
            for c in range(1, L)
            if gcd(a, c) == 1 and a * u + c * v <= K
        )
        mob = sum(
            mu[d] * ((1 << K) // (((1 << (d * u)) - 1) * ((1 << (d * v)) - 1)))
            for d in range(1, L)
        )
        # truncation error at most L*L units; omitted pairs and divisors at most 2^(K-L+3) units
        bound = L * L + (1 << (K - L + 3))
        chk.check(
            f'Mobius sum equals coprime-pair sum to 2^-100 at (u,v)=({u},{v})',
            abs(direct - mob) <= bound and abs(direct - mob) + bound < (1 << (K - 100)),
        )


DESIGN_K3 = (
    [(0, 0), (4, 10), (5, 9)],
    [(1, 1), (6, 12), (2, 6)],
)
DESIGN_K4 = (
    [(0, 0), (-8, -20), (-1, 2), (2, 14), (7, 22), (-3, -12)],
    [(3, 6), (-6, -18), (4, 16), (-5, -14), (-4, -4), (5, 20)],
)


def cancels(plus: list[tuple[int, int]], minus: list[tuple[int, int]], h: int) -> bool:
    """Whether the signed points have zero weight on every fibre p*h - s = m."""
    fib: dict[int, int] = {}
    for sign, pts in ((1, plus), (-1, minus)):
        for p, s in pts:
            fib[p * h - s] = fib.get(p * h - s, 0) + sign
    return all(v == 0 for v in fib.values())


def check_designs(chk: Checker) -> None:
    """Check 8: explicit designs with fewer points than the cube."""
    for K, (plus, minus) in ((3, DESIGN_K3), (4, DESIGN_K4)):
        firsts = [p for p, _ in plus + minus]
        chk.check(
            f'K={K} design has {len(firsts)} distinct first coordinates',
            len(set(firsts)) == len(firsts),
        )
        chk.check(
            f'K={K} design cancels levels 1..{K}',
            all(cancels(plus, minus, h) for h in range(1, K + 1)),
        )
        chk.check(
            f'control: K={K} design does not cancel level {K + 1}',
            not cancels(plus, minus, K + 1),
        )
    plus, minus = ([(43 + 30 * a, 30 * b) for a, b in points] for points in DESIGN_K3)
    chk.check(
        'three-level six-prime realization',
        all(is_prime(p) and p > 3 for p, _ in plus + minus)
        and len({p for p, _ in plus + minus}) == 6
        and all(cancels(plus, minus, h) for h in (1, 2, 3)),
    )
    residue, modulus = 0, 1
    for p, s in plus + minus:
        residue += modulus * (((s - residue) * pow(modulus, -1, p * p)) % (p * p))
        modulus *= p * p
    n = residue + modulus
    chk.check(
        'six-prime design admits the square congruences',
        all(n > s and (n - s) % (p * p) == 0 for p, s in plus + minus),
    )


def prime_power(n: int) -> bool:
    """Whether n>1 is a prime power, by trial division."""
    if n < 2:
        return False
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            return n == 1
        p += 1
    return True


def check_robust_witnesses(chk: Checker) -> None:
    """Check 9: retained vectors satisfy all affine fixed-prime constraints."""
    path = Path(__file__).parent / 'assets' / 'robust_kernel_vectors.json'
    records = json.loads(path.read_text())['vectors']
    expected = {(8, 24, 2), (16, 48, 2), (32, 96, 2), (32, 96, 5), (32, 128, 7)}
    require(
        len(records) == len(expected)
        and {(r['J'], r['R'], r['y']) for r in records} == expected,
        'robust witness coverage',
    )
    for r in records:
        J, B, R, y, z = r['J'], r['B'], r['R'], r['y'], r['z']
        require(B == J and len(z) == R - B + 1, 'witness support')
        require(all(type(c) is int for c in z), 'integer coefficients')
        primes = [p for p in range(2, y + 1) if is_prime(p)]
        ph = totients(R + J)
        Phi = prefix(ph)
        U = [Phi[n + J] - (Phi[n] << J) for n in range(B, R + 1)]
        coefficients: dict[int, int] = {}
        constant = 0
        for m in range(B + 1, R + J + 1):
            w = sum(
                z[n - B] << (J - m + n) for n in range(max(B, m - J), min(R, m - 1) + 1)
            )
            s, k = rough_split(m, primes)
            if k == 1 or prime_power(k):
                constant += ph[m] * w
            else:
                coefficients[k] = coefficients.get(k, 0) + ph[s] * w
        label = f'J={J}, R={R}, y={y}'
        chk.check(
            f'fixed-prime robust cancellation at {label}',
            constant == 0 and all(c == 0 for c in coefficients.values()),
        )
        W = sum(c * t for c, t in zip(z, U))
        v = sum(c * Phi[n] for n, c in enumerate(z, B))
        cost = sum(abs(c) * (n + J + 2) for n, c in enumerate(z, B))
        chk.check(
            f'kernel, odd shadow and retained cost at {label}',
            W == 0 and v % 4 == 2 and cost == r['cost'],
            f'cost {cost}; no minimality claim',
        )
        chk.check(
            f'control: changing the first coefficient fails at {label}', W + U[0] != 0
        )


def orbit_enclosure(
    e: int, primes: list[int], ph: list[int], cutoff: int
) -> tuple[Fraction, Fraction]:
    """Bound the complete orbit sum by a smooth prefix and an all-integer tail."""
    N = cutoff // e
    lower = sum(
        (
            Fraction(ph[s], 1 << (s * e))
            for s in range(1, N + 1)
            if rough_split(s, primes)[1] == 1
        ),
        Fraction(0),
    )
    x = Fraction(1, 1 << e)
    tail = x ** (N + 1) * ((N + 1) - N * x) / (1 - x) ** 2
    return lower, lower + tail


def check_orbit_rounding(chk: Checker) -> None:
    """Check 10: certified finite decisions for the complete signed construction."""
    cutoff, nmax = 4096, 10000
    ph = totients(nmax)
    S0 = Fraction(prefix(ph[: cutoff + 1])[-1], 1 << cutoff)
    Stail = Fraction(cutoff + 2, 1 << cutoff)
    for y, a, Q, count in ((2, 15, 30, 8), (3, 35, 210, 6)):
        primes = [p for p in range(2, y + 1) if is_prime(p)]
        elo, ehi = -S0 - Stail, -S0
        changes = {}
        bounds_hold = True
        for j in range(count):
            e = a + j * Q
            require(
                rough_split(e, primes)[0] == 1 and not prime_power(e),
                'composite rough part',
            )
            alo, ahi = orbit_enclosure(e, primes, ph, cutoff)
            ratios = [v / (4 * w) for v in (elo, ehi) for w in (alo, ahi)]
            qlo, qhi = min(ratios), max(ratios)
            midpoint = (qlo + qhi) / 2 + Fraction(1, 2)
            digit = midpoint.numerator // midpoint.denominator
            require(
                qlo > digit - Fraction(1, 2) and qhi < digit + Fraction(1, 2),
                'interval does not determine the nearest integer',
            )
            delta = 4 * digit
            changes[e] = delta
            products = (delta * alo, delta * ahi)
            elo, ehi = elo - max(products), ehi - min(products)
            bounds_hold &= (
                max(abs(elo), abs(ehi)) <= 2 * alo
                and abs(delta) < (1 << (Q + 3))
                and delta % 4 == 0
                and alo >= Fraction(1, 1 << e)
                and ahi < Fraction(2, 1 << e)
            )
        chk.check(
            f'complete-orbit rounding bounds at y={y}',
            bounds_hold,
            f'{count} certified decisions',
        )
        f = [0] * (nmax + 1)
        for n in range(1, nmax + 1):
            s, k = rough_split(n, primes)
            f[n] = ph[n] + ph[s] * changes.get(k, 0)
        fixed = f[1] == 1 and all(
            f[n] == ph[n] for n in range(2, nmax + 1) if prime_power(n)
        )
        laws = all(
            f[p * n] == (p if n % p == 0 else p - 1) * f[n]
            for p in primes
            for n in range(1, nmax // p + 1)
        )
        size_residue = all(
            (f[n] - ph[n]) % 4 == 0 and abs(f[n]) <= (1 << (Q + 4)) * n
            for n in range(1, nmax + 1)
        )
        chk.check(
            f'fixed-prime laws, prime powers, size and residues through {nmax} at y={y}',
            fixed and laws and size_residue,
        )
        e = next(k for k, d in changes.items() if d)
        chk.check(
            f'control: omitting orbit propagation fails the law at y={y}',
            ph[2 * e] != ph[e] + changes[e],
        )


def check_residue_lifting(chk: Checker) -> None:
    """Check 11: zero-block positions amplify the positive residue error."""
    cutoff = 512
    ph = totients(cutoff)
    tail = Fraction(cutoff + 2, 1 << cutoff)
    for m in range(2, 65):
        n0 = next(n for n in range(1, cutoff + 1) if ph[n] >= m)
        D0 = sum(
            (Fraction(m * (ph[n] // m), 1 << n) for n in range(1, cutoff + 1)),
            Fraction(0),
        )
        starts = [N for N in range(129) if ph[N + 1] % m == 0]
        chk.check(
            f'residue error bounds at m={m}',
            Fraction(m, 1 << n0) <= D0
            and D0 + tail <= Fraction(m + 2, 1 << m)
            and all(n0 - 1 <= N and Fraction(m, 2) <= D0 * (1 << N) for N in starts),
        )


def main() -> int:
    """Run the eleven checks and return the exit status."""
    parser = evidence_parser(__doc__.splitlines()[0])
    args = parser.parse_args()
    chk = Checker()
    print('1. column generation at powers of two')
    check_columns(chk, 8 if args.quick else 13)
    print('2. exact shadow image')
    check_shadow_image(
        chk, [8, 12, 16, 20, 24] if args.quick else [8, 12, 16, 20, 24, 32, 48, 64]
    )
    print('3. structural vectors have u = 0')
    check_structural(chk, [5, 7, 13], [16, 32] if args.quick else [16, 32, 48, 64])
    print('4. kernel cost profile')
    check_profile(chk, [16, 32, 64] if args.quick else [16, 32, 64, 128])
    print('5. longer supports (control)')
    check_long(chk, [7, 13], [16] if args.quick else [16, 24, 32])
    print('6. perturbation construction on a prefix')
    check_barrier(chk, 1000 if args.quick else 3000)
    print('7. coprime-pair identities')
    check_coprime(chk, 500 if args.quick else 2000)
    print('8. small dilation designs')
    check_designs(chk)
    print('9. fixed-prime robust witnesses')
    check_robust_witnesses(chk)
    print('10. complete smooth-orbit rounding')
    check_orbit_rounding(chk)
    print('11. residue lifting')
    check_residue_lifting(chk)
    return chk.finish()


if __name__ == '__main__':
    sys.exit(main())

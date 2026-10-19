"""Exercise the shadow bridge of the shadows page with exact arithmetic.

At B = 8 and depths J = 32, 64, 128, 200 (only J = 32 under --quick) the
script realizes the shadows 2^B (q, p) of two consecutive convergents of S
as exact scalar-kernel vectors on [B, R], builds the N-3 cross-product
vectors of the shadow-zero sublattice, rounds a two-term odd vector against
that rank-(N-1) family, and checks every clause it uses: the exact kernel
identity sum z_n U_J(n) = 0, the shadows, the nonzero shadow determinant,
the cost bounds of the owning page, the parity of the rounded vector and
its 2-adic support. It checks determinant-scaled realization separately.
It replays the 40000-term continued-fraction enclosure consumed by the
finite corollary, checks the integer inequalities behind that corollary
corollary at every depth in its stated range, and runs failure
controls on corrupted inputs. All arithmetic is exact (Python integers and
fractions); S enters only through an exact truncation with a rigorous
enclosure, and every approximation bound is certified by the kernel
identity, not by that enclosure. Costs are upper bounds of one construction;
no minimum, asymptotic statement or irrationality claim follows. Standard
library only, plus the root reporting helpers. Full run about 15 seconds.
"""

from __future__ import annotations

import math
import sys
from fractions import Fraction

from tools import Checker, evidence_parser

B = 8
DEPTHS = (32, 64, 128, 200)
QUICK_DEPTHS = (32,)
TRUNCATION = 2400
EXPECTED = {
    # J: (R, N, bit lengths of q, costs of the two realized vectors,
    #     shadow determinant, max cross-vector cost, rounded odd cost,
    #     nonzero terms, max |z|, v2(u) of the odd vector)
    32: (60, 53, (45, 51), (37894, 32353), 65536, 321632, 459427, 45, 4524, 8),
    64: (92, 85, (80, 83), (894591, 127148), 65536, 1955928, 1563054, 76, 8182, 8),
    128: (155, 148, (143, 146), (267339, 917571), -65536, 10751440, 14707970, 131, 41850, 9),
    200: (226, 219, (215, 217), (2806263, 30824564), -65536, 30861984, 31343164, 199, 12168, 8),
}
# Fixed expectations agree with research/leads/totient_binary_series/evidence.
# The consumed continued-fraction enclosure is replayed below, without its
# unrelated ten-million-term valuation and arithmetic-window scan.
CERTIFIED_TRUNCATION = 40000
CERTIFIED_PREFIX_LENGTH = 11759
LARGEST_QUOTIENT = 15531
DENOMINATOR_DIGITS = 6018


def require(condition: bool, message: str) -> None:
    """Reject a failed obligation even when Python optimization is enabled."""
    if not condition:
        raise ValueError(message)


def totients(limit: int) -> list[int]:
    """Return phi(0..limit) by a sieve, cross-checked below by coprime counts."""
    phi = list(range(limit + 1))
    for p in range(2, limit + 1):
        if phi[p] == p:
            for m in range(p, limit + 1, p):
                phi[m] -= phi[m] // p
    return phi


def egcd(a: int, b: int) -> tuple[int, int, int]:
    """Return (g, x, y) with a x + b y = g = gcd(a, b) >= 0."""
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    if a < 0:
        a, x0, y0 = -a, -x0, -y0
    return a, x0, y0


def convergents(x: Fraction, qmax: int) -> list[tuple[int, int]]:
    """Return the convergents (p, q) of x with q <= qmax."""
    num, den = x.numerator, x.denominator
    p0, q0, p1, q1 = 0, 1, 1, 0
    out = []
    while den and q1 <= qmax:
        a = num // den
        num, den = den, num - a * den
        p0, p1 = p1, a * p1 + p0
        q0, q1 = q1, a * q1 + q0
        if q1 <= qmax:
            out.append((p1, q1))
    return out


def signed_digits(u: int, lo: int, hi: int) -> dict[int, int]:
    """Return z with z_m = nu_m - 2 nu_(m+1), nu_m = round(u / 2^m), on [lo, hi]."""
    nu = {m: (u + (1 << (m - 1))) >> m for m in range(lo, hi + 2)}
    z = {m: nu[m] - 2 * nu[m + 1] for m in range(lo, hi + 1)}
    require(nu[lo] << lo == u and nu[hi + 1] == 0, 'digits do not fit the support')
    require(sum(z[m] << m for m in z) == u, 'signed digits do not represent u')
    return z


def solve_two_rows(f: dict[int, int], g: dict[int, int], X: int, Y: int) -> dict[int, int]:
    """Return integers c with sum c_k f_k = X and sum c_k g_k = Y.

    Stage one uses two values f_k1, f_k2 with gcd 2 for X. Stage two keeps
    the f-value fixed with vectors (f_l/2) e_k - (f_k/2) e_l, whose g-values
    are halved 2x2 minors, and uses two of them whose gcd divides the g
    defect. Both stages are Bezout steps with a balancing reduction.
    """
    keys = sorted(f)
    pair = next(
        ((k1, k2) for i, k1 in enumerate(keys) for k2 in keys[i + 1:]
         if math.gcd(f[k1], f[k2]) == 2),
        None,
    )
    require(pair is not None and X % 2 == 0, 'first stage: no coprime-halved pair')
    k1, k2 = pair
    c = {k: 0 for k in keys}
    d, x1, x2 = egcd(f[k1], f[k2])
    t = X // 2
    c[k1], c[k2] = x1 * t, x2 * t
    m = f[k2] // 2
    s = c[k1] // m
    c[k1] -= s * m
    c[k2] += s * (f[k1] // 2)
    require(sum(c[k] * f[k] for k in keys) == X, 'first stage failed')
    Yp = Y - sum(c[k] * g[k] for k in keys)
    require(Yp % 2 == 0, 'second stage: odd defect')

    def half(a: int, b: int) -> int:
        return (f[b] * g[a] - f[a] * g[b]) // 2

    best = None
    for i, ka in enumerate(keys):
        for kb in keys[i + 1:]:
            m1 = half(ka, kb)
            if m1 == 0:
                continue
            for j, kc in enumerate(keys):
                for kd in keys[j + 1:]:
                    if (kc, kd) <= (ka, kb):
                        continue
                    m2 = half(kc, kd)
                    if m2 == 0:
                        continue
                    dd = math.gcd(m1, m2)
                    if Yp % dd == 0:
                        cand = (abs(m1) + abs(m2), ka, kb, kc, kd, m1, m2, dd)
                        if best is None or cand < best:
                            best = cand
            if best is not None:
                break
        if best is not None:
            break
    require(best is not None, 'second stage: no halved-minor pair divides the defect')
    _, ka, kb, kc, kd, m1, m2, dd = best
    d2, y1, y2 = egcd(m1, m2)
    require(d2 == dd, 'second stage gcd mismatch')
    t = Yp // dd
    t1, t2 = y1 * t, y2 * t
    mm = m2 // dd
    s = t1 // mm
    t1 -= s * mm
    t2 += s * (m1 // dd)
    c[ka] += t1 * (f[kb] // 2)
    c[kb] -= t1 * (f[ka] // 2)
    c[kc] += t2 * (f[kd] // 2)
    c[kd] -= t2 * (f[kc] // 2)
    require(sum(c[k] * f[k] for k in keys) == X, 'second stage broke the f-value')
    require(sum(c[k] * g[k] for k in keys) == Y, 'second stage failed')
    return c


class Depth:
    """Exact data of one depth: rows, weights and the linear functionals."""

    def __init__(self, J: int, R: int, phi: list[int], Phi: list[int]) -> None:
        self.J, self.R = J, R
        self.supp = list(range(B, R + 1))
        self.N = len(self.supp)
        self.U = {n: Phi[n + J] - (Phi[n] << J) for n in self.supp}
        self.w = {n: n + J + 2 for n in self.supp}
        self.Phi = Phi
        self.f = {k: phi[k] for k in range(B + 1, R + 1)}
        self.g = {k: phi[k + J] for k in range(B + 1, R + 1)}

    def zero(self) -> dict[int, int]:
        return {n: 0 for n in self.supp}

    def cost(self, z: dict[int, int]) -> int:
        return sum(abs(z[n]) * self.w[n] for n in self.supp)

    def W(self, z: dict[int, int]) -> int:
        return sum(z[n] * self.U[n] for n in self.supp)

    def u(self, z: dict[int, int]) -> int:
        return sum(z[n] << n for n in self.supp)

    def v(self, z: dict[int, int]) -> int:
        return sum(z[n] * self.Phi[n] for n in self.supp)

    def add_recurrence(self, z: dict[int, int], c: dict[int, int]) -> None:
        """Add sum c_k (e_k - 2 e_(k-1)) in place."""
        for k, ck in c.items():
            z[k] += ck
            z[k - 1] -= 2 * ck

    def realize(self, u: int, v: int) -> dict[int, int]:
        """Return z in the kernel with shadow (u, v), by digits plus correction."""
        z = self.zero()
        z.update(signed_digits(u, B, self.R))
        X = v - self.v(z)
        Y = (X << self.J) - self.W(z)
        c = solve_two_rows(self.f, self.g, X, Y)
        self.add_recurrence(z, c)
        require(self.W(z) == 0 and self.u(z) == u and self.v(z) == v, 'realization failed')
        return z

    def realize_scaled(self, u: int, v: int) -> tuple[dict[int, int], int]:
        """Realize (D u, D v) by an adjugate, with no lattice-image assumption."""
        z0 = signed_digits(u, B, self.R)
        X = v - self.v(z0)
        Y = (X << self.J) - self.W(z0)
        keys = sorted(self.f)
        a, b = next(
            (a, b) for i, a in enumerate(keys) for b in keys[i + 1:]
            if self.f[a] * self.g[b] - self.f[b] * self.g[a] != 0
        )
        D = self.f[a] * self.g[b] - self.f[b] * self.g[a]
        c = {
            a: self.g[b] * X - self.f[b] * Y,
            b: self.f[a] * Y - self.g[a] * X,
        }
        z = {n: D * z0[n] for n in self.supp}
        self.add_recurrence(z, c)
        require(self.W(z) == 0, 'scaled realization left the kernel')
        require((self.u(z), self.v(z)) == (D * u, D * v), 'scaled shadow mismatch')
        H = self.R + self.J + 2
        require(max(abs(X), abs(Y)) <= 1 + H**2, 'scaled correction size')
        require(self.cost(z) <= 30 * H**4, 'scaled cost bound')
        return z, D

    def cross_vectors(self) -> list[dict[int, int]]:
        """Return N-3 independent shadow-zero kernel vectors (Lemma on L_00)."""
        keys = sorted(self.f)
        f, g = self.f, self.g
        ka, kb = next(
            (a, b) for i, a in enumerate(keys) for b in keys[i + 1:]
            if f[a] * g[b] - f[b] * g[a] != 0
        )
        D = f[ka] * g[kb] - f[kb] * g[ka]
        out = []
        for k in keys:
            if k in (ka, kb):
                continue
            c = {k: D, ka: f[kb] * g[k] - f[k] * g[kb], kb: f[k] * g[ka] - f[ka] * g[k]}
            z = self.zero()
            self.add_recurrence(z, c)
            require(self.W(z) == 0 and self.u(z) == 0 and self.v(z) == 0, 'cross vector')
            out.append(z)
        return out

    def odd_start(self) -> dict[int, int]:
        """Return the two-index odd kernel vector of the two-depth page."""
        A = {n: self.Phi[n] // 2 for n in self.supp}
        V = {n: self.U[n] // 2 for n in self.supp}
        n1 = next(n for n in self.supp if A[n] % 2 == 1 and V[n] % 2 == 0)
        n2 = next(n for n in self.supp if A[n] % 2 == 0 and V[n] % 2 == 1)
        gg = math.gcd(V[n1], V[n2])
        z = self.zero()
        z[n1], z[n2] = V[n2] // gg, -V[n1] // gg
        require(self.W(z) == 0 and self.v(z) % 4 == 2, 'odd start vector')
        return z

    def round_against(self, z0: dict[int, int], basis: list[dict[int, int]]) -> dict[int, int]:
        """Write z0 in the rational span of the basis and subtract nearest integers."""
        cols = len(basis)
        M = [[Fraction(b[n]) for b in basis] + [Fraction(z0[n])] for n in self.supp]
        r = 0
        for col in range(cols):
            pr = next((i for i in range(r, self.N) if M[i][col] != 0), None)
            require(pr is not None, 'basis is linearly dependent')
            M[r], M[pr] = M[pr], M[r]
            inv = 1 / M[r][col]
            M[r] = [x * inv for x in M[r]]
            for i in range(self.N):
                if i != r and M[i][col] != 0:
                    fac = M[i][col]
                    M[i] = [a - fac * b for a, b in zip(M[i], M[r])]
            r += 1
        require(all(M[i][cols] == 0 for i in range(cols, self.N)), 'z0 outside the span')
        z = dict(z0)
        for i in range(cols):
            m = round(M[i][cols])
            if m:
                for n in self.supp:
                    z[n] -= m * basis[i][n]
        return z


def certified_prefix(checker: Checker) -> None:
    """Replay the exact continued-fraction dependency of the finite corollary."""
    phi = totients(CERTIFIED_TRUNCATION)
    scaled = 0
    for n in range(1, CERTIFIED_TRUNCATION + 1):
        scaled = 2 * scaled + phi[n]

    def quotients(num: int, den: int) -> list[int]:
        result = []
        while den:
            a, remainder = divmod(num, den)
            result.append(a)
            num, den = den, remainder
        return result

    denominator = 1 << CERTIFIED_TRUNCATION
    upper_num = scaled + CERTIFIED_TRUNCATION + 2
    lower = quotients(scaled, denominator)
    upper = quotients(upper_num, denominator)
    common = 0
    while common < min(len(lower), len(upper)) and lower[common] == upper[common]:
        common += 1
    prefix = lower[:common]
    p0, q0, p1, q1 = 0, 1, 1, 0
    for a in prefix:
        p0, p1 = p1, a * p1 + p0
        q0, q1 = q1, a * q1 + q0
    endpoints = sorted((Fraction(p1, q1), Fraction(p1 + p0, q1 + q0)))
    checker.check(
        'finite corollary: exact 40000-term enclosure certifies the consumed CF prefix',
        common == CERTIFIED_PREFIX_LENGTH
        and common < min(len(lower), len(upper))
        and max(prefix[1:]) == LARGEST_QUOTIENT
        and 10 ** (DENOMINATOR_DIGITS - 1) <= q1 < 10**DENOMINATOR_DIGITS
        and abs(p1 * q0 - p0 * q1) == 1
        and endpoints[0] < Fraction(scaled, denominator)
        < Fraction(upper_num, denominator) < endpoints[1],
    )


def finite_corollary(checker: Checker) -> None:
    """Check the integer inequalities behind the finite non-flatness corollary."""
    b = 4

    def data(J: int) -> tuple[int, int, int]:
        N = 3 * J - b + 1
        R = 3 * J
        return N, R, N**3 * (R + 2) ** 2 * (R + J + 2)

    def collision(J: int) -> bool:  # (H_J): 2^(2J-B) >= N (R+2)
        N, R, _ = data(J)
        return (1 << (2 * J - b)) >= N * (R + 2)

    def legendre(J: int) -> bool:  # N^3 (R+2)^2 (R+J+2) < 2^(2J-2B-4)
        _, _, poly = data(J)
        return poly < (1 << (2 * J - 2 * b - 4))

    def quotient(J: int) -> bool:  # 2^(2J-2B-3) >= (A+2) N^3 (R+2)^2 (R+J+2)
        _, _, poly = data(J)
        return (1 << (2 * J - 2 * b - 3)) >= (LARGEST_QUOTIENT + 2) * poly

    def denominator(J: int) -> bool:  # 2^(J+B+2) N (R+2) < 10^(digits-1)
        N, R, _ = data(J)
        return (1 << (J + b + 2)) * N * (R + 2) < 10 ** (DENOMINATOR_DIGITS - 1)

    lo, hi = 33, 19950
    checker.check(
        'finite corollary: collision and Legendre conditions hold at both ends',
        collision(lo) and legendre(lo) and collision(hi) and legendre(hi),
    )
    checker.check(
        'finite corollary: quotient bound holds at J=33 and fails at J=32',
        quotient(lo) and not quotient(lo - 1),
    )
    checker.check(
        'finite corollary: denominator bound holds at J=19950 and fails at J=19951',
        denominator(hi) and not denominator(hi + 1),
    )
    checker.check(
        'finite corollary: all four inequalities hold at every J=33..19950',
        all(
            collision(J) and legendre(J) and quotient(J) and denominator(J)
            for J in range(lo, hi + 1)
        ),
    )


def main() -> int:
    """Run the construction at the declared depths and the failure controls."""
    parser = evidence_parser(__doc__)
    args = parser.parse_args()
    checker = Checker()
    print(
        'Shadow bridge: exact realization of two convergent shadows as scalar-kernel '
        'vectors, cross vectors of the shadow-zero sublattice, and rounding to an odd '
        'vector; finite outcomes of one construction, no minimum or asymptotic claim.'
    )
    depths = QUICK_DEPTHS if args.quick else DEPTHS
    limit = max(EXPECTED[J][0] + J for J in depths) + 2
    phi = totients(max(limit, TRUNCATION))
    try:
        for n in (1, 2, 4, 9, 30, 97, 210, 1000, 2400):
            counted = sum(math.gcd(n, j) == 1 for j in range(1, n + 1))
            require(phi[n] == counted, f'totient sieve control at {n}')
        checker.check('sieve totients agree with coprime counts at control values', True)
    except ValueError as error:
        checker.check('totient controls', False, str(error))
        return checker.finish()
    Phi = [0] * (limit + 1)
    for n in range(1, limit + 1):
        Phi[n] = 2 * Phi[n - 1] + phi[n]
    # exact truncation of S with a rigorous enclosure: S_lo <= S <= S_lo + (T+2) 2^-T
    S_lo = sum(Fraction(phi[n], 1 << n) for n in range(1, TRUNCATION + 1))
    S_hi = S_lo + Fraction(TRUNCATION + 2, 1 << TRUNCATION)
    conv = convergents(S_lo, 1 << 420)
    upper_conv = convergents(S_hi, 1 << 420)
    for J in depths:
        R_exp, N_exp, bits_exp, costs_exp, det_exp, cross_exp, odd_exp, terms_exp, height_exp, v2_exp = EXPECTED[J]
        try:
            k = next(i for i in range(len(conv) - 2) if conv[i + 1][1].bit_length() >= J + B + 9)
            (p1, q1), (p2, q2) = conv[k], conv[k + 1]
            require(
                conv[:k + 2] == upper_conv[:k + 2],
                'the enclosure does not certify the selected consecutive convergents',
            )
            us = [q1 << B, q2 << B]
            vs = [p1 << B, p2 << B]
            R = max(u.bit_length() for u in us) + 1
            depth = Depth(J, R, phi, Phi)
            require((R, depth.N) == (R_exp, N_exp), f'support {(R, depth.N)}')
            require((q1.bit_length(), q2.bit_length()) == bits_exp, 'convergent sizes')
            neighbours = abs(p1 * q2 - p2 * q1) == 1
            tail = max(
                abs(q * bound - p) for (p, q) in ((p1, q1), (p2, q2)) for bound in (S_lo, S_hi)
            )
            require(neighbours and tail * (1 << (J + B)) <= Fraction(1, 256), 'approximation quality')
            checker.check(
                f'J={J}: consecutive convergents, 2^(J+B)|qS-p| <= 2^-8 on the enclosure', True
            )
            zs = [depth.realize(u, v) for u, v in zip(us, vs)]
            costs = tuple(depth.cost(z) for z in zs)
            require(costs == costs_exp, f'realized costs {costs}')
            require(all(depth.v(z) % 4 == 0 for z in zs), 'convergent shadows are even')
            checker.check(f'J={J}: two exact kernel vectors realize the shadows 2^B(q,p)', True)
            scaled = [depth.realize_scaled(u, v) for u, v in zip(us, vs)]
            (scaled1, D1), (scaled2, D2) = scaled
            require(D1 == D2 != 0, 'scaled realizations used different determinants')
            scaled_det = depth.u(scaled1) * depth.v(scaled2) - depth.u(scaled2) * depth.v(scaled1)
            require(scaled_det == D1**2 * (us[0] * vs[1] - us[1] * vs[0]), 'scaled determinant')
            checker.check(f'J={J}: adjugate realization preserves independent shadows within 30H^4', True)
            det = us[0] * vs[1] - us[1] * vs[0]
            require(det == det_exp and abs(det) == 1 << (2 * B), f'determinant {det}')
            checker.check(f'J={J}: shadow determinant is nonzero (+-2^(2B))', True)
            cross = depth.cross_vectors()
            bound_cross = 18 * (R + J + 2) ** 3
            max_cross = max(depth.cost(z) for z in cross)
            require(len(cross) == depth.N - 3 and max_cross <= bound_cross, 'cross vectors')
            require(max_cross == cross_exp, f'max cross cost {max_cross}')
            checker.check(f'J={J}: {depth.N - 3} shadow-zero cross vectors within 18(R+J+2)^3', True)
            z0 = depth.odd_start()
            basis = [*zs, *cross]
            zodd = depth.round_against(z0, basis)
            C = depth.cost(zodd)
            bound_odd = costs[0] + costs[1] + 9 * (depth.N - 3) * (R + J + 2) ** 3
            uo = depth.u(zodd)
            v2u = (uo & -uo).bit_length() - 1
            require(depth.W(zodd) == 0 and depth.v(zodd) % 4 == 2, 'rounded vector parity')
            require(C <= bound_odd, 'rounded cost exceeds the proposition bound')
            terms = sum(1 for n in depth.supp if zodd[n])
            height = max(abs(x) for x in zodd.values())
            require((C, terms, height, v2u) == (odd_exp, terms_exp, height_exp, v2_exp),
                    f'rounded odd vector {(C, terms, height, v2u)}')
            require(v2u >= B, 'odd vector support congruence')
            checker.check(f'J={J}: rounding gives an odd exact kernel vector within the bound', True)
            print(
                f'    costs {costs}, cross max {max_cross}, start cost {depth.cost(z0):.3e}, '
                f'odd cost {C} (bound {bound_odd}); two-shadow exclusion b < 2^J/C: '
                f'{((1 << J) - 1) // max(costs)}; odd exclusion b_odd < 2^(J+1)/C: '
                f'{((1 << (J + 1)) - 1) // C} with v2(b) < B-1'
            )
            if J == depths[0]:
                # failure controls on the same exact data
                bad = dict(zs[0])
                first = next(n for n in depth.supp if bad[n])
                bad[first] += 1
                checker.check('control: a corrupted vector leaves the kernel', depth.W(bad) != 0)
                doubled = {n: 2 * zs[0][n] for n in depth.supp}
                det0 = depth.u(zs[0]) * depth.v(doubled) - depth.u(doubled) * depth.v(zs[0])
                checker.check('control: proportional shadows have determinant zero', det0 == 0)
                try:
                    depth.round_against(z0, [zs[0], *cross])
                    dependent = False
                except ValueError as error:
                    dependent = 'outside the span' in str(error)
                checker.check('control: one shadow and the cross vectors do not span z0', dependent)
                # doubling the odd start gives an even kernel vector; rounding
                # against the basis must preserve that parity class
                even = depth.round_against({n: 2 * z0[n] for n in depth.supp}, basis)
                checker.check(
                    'control: an even vector stays even under rounding',
                    depth.v(even) % 4 == 0 and depth.W(even) == 0,
                )
        except (ValueError, TypeError, StopIteration) as error:
            checker.check(f'J={J}: construction', False, str(error))
    certified_prefix(checker)
    finite_corollary(checker)
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

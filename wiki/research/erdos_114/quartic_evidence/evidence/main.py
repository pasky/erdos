"""Bound the quartic deficit integral on both collision strata in ball arithmetic.

For a centered monic quartic F and a circle or line Gamma through its critical
values, the research page defines Itilde(F, Gamma): the integral over Gamma of
the inverse-derivative density G_F minus |sigma - sigma0|^(-3/4) for a point
sigma0 of Gamma. Its identity (10) gives l(p) - l(z^4 - 1) = lambda Itilde for
the polynomial p of scale lambda that the pair represents. On each collision
stratum F is fixed:

- double critical point: F5 = z^4 - (3/2) z^2 - z, with critical values -3/2
  (simple, at 1) and 3/16 (double, at -1/2);
- equal values: F6 = z^4 - 2 z^2, with critical values -1 (at 1 and -1) and 0
  (at 0).

Gamma runs over the pencil of circles through the two values and its line,
indexed by the tangent-chord angle beta at the first value fA: beta = 0 is
the line, the circle of angle beta has radius d/(2 sin beta) and center
(fA + fB)/2 + i R cos beta, and beta and pi - beta give conjugate circles with
the same integral, so beta in [0, pi/2] covers the pencil. The program proves Itilde < -1 for every beta in [0, pi/2] on both
strata, so every polynomial of the two strata has length below
l(z^4 - 1) - lambda.

Method, for each box of beta values:

- Large circles and the line (beta <= 1/2): Gamma is parametrized as
  sigma(x) = fA + e^(-i beta) x / (1 - i kappa x / 2), which is the line when
  the curvature kappa is 0, with sigma0 = fA subtracted pointwise. Windows
  around both critical values use the Crofton bound of 8 pi r per disc of
  radius r, valid because almost every line meets the preimage of Gamma, a
  real algebraic curve of degree at most 8, in at most 8 points. Pieces next to a critical value of multiplicity m bound
  |o|^(m/(m+1)) G_F through identity (13), with o the offset. Beyond |x| = 6
  the variable u = 1/x and the factorization (12) built on identity (11) are
  used; where |sigma - fA| >= 300 an explicit constant K bounds the bracket of
  (12) by K / |sigma - fA|, which integrates to K (8/3) U^(3/4) over |u| <= U.
- Small circles (beta >= 1/2): Gamma is parametrized by angle about its
  center, the integral of G_F over the whole circle is bounded from above with
  the same windows and weights, and R^(1/4) l(z^4 - 1) is subtracted.

Every root of F = sigma used in a bound lies in a disc certified by a Rouché
test against the linear term, and four pairwise disjoint certified discs
account for all four roots. Every accepted bound is a sum of piece widths
times enclosure ends, uniform over its box of beta values and its piece.
Pieces tile the curve exactly where the integrand is signed; over-coverage is
used only for the nonnegative density G_F. A box whose bound is not below -1,
or for which a certificate fails, is bisected, at most six times. On the box
[0, 1e-4], which contains the line, the controls require the two bounds to be
ordered, less than 1/2 apart, and to enclose the floating-point value of
Itilde on the line, so that no target below that value can pass there.

Arithmetic: python-flint arb and acb balls at 80 bits. numpy supplies only
approximate roots, which the Rouché tests certify. Runtime: about forty-five
minutes of one thread per stratum, so about ninety for the full check, with a
peak resident memory near 51 MB; --only runs one stratum, so the two can run
as separate processes; --quick checks four boxes on each stratum in a few
seconds. Run from the repository root with uv run --no-sync python and this
path.

Limitations: the program checks the two pencils only. It does not check
identity (10), the parametrization of the strata by the pencils, or the
written lemmas (a) to (d); the research page proves those.
"""

from __future__ import annotations

import sys
from collections.abc import Callable

import numpy as np
from flint import acb, arb, ctx

from tools import Checker, evidence_parser

ctx.prec = 80
ctx.threads = 1
PI = arb.pi()
L0 = arb(2).root(4) * arb(0.5).gamma() * (arb(1) / 8).gamma() / (arb(5) / 8).gamma()
ZERO = arb(0)
ONE = arb(1)

TARGET = arb(-1)
R_WIN = 2e-3  # Crofton disc radius
X_MID = 6.0  # end of the x-pieces in the large-circle regime
T_FAR = 300.0  # analytic far-field bound beyond |sigma - fA| = T_FAR
BETA_SPLIT = 0.5  # large circles below, small circles above
REL_TOL = 0.03  # adaptive piece tolerance (affects sharpness only)
MAX_SPLIT = 6
# floating-point values of Itilde on the line of each pencil, by quadrature
LINE_VALUE = {'double critical point': -1.7075, 'equal values': -2.3963}


def iv(lo, hi) -> arb:
    """A ball containing the real interval [lo, hi]."""
    lo = arb(lo)
    hi = arb(hi)
    return lo + (hi - lo) * arb(0.5, 0.5)


def up(x: arb) -> arb:
    """The upper end of a ball."""
    return x.upper()


def lo(x: arb) -> arb:
    """The lower end of a ball."""
    return x.lower()


def pos(x: arb) -> bool:
    """Whether a ball is certainly positive."""
    return bool(x > 0)


def mag_hi(z: acb) -> arb:
    """An upper bound for |z| over a complex box."""
    re = abs(z.real).upper()
    im = abs(z.imag).upper()
    return (re * re + im * im).sqrt().upper()


def mag_lo(z: acb) -> arb:
    """A lower bound for |z| over a complex box, clamped at 0."""
    re = abs(z.real).lower()
    im = abs(z.imag).lower()
    re = re if re > 0 else ZERO
    im = im if im > 0 else ZERO
    return (re * re + im * im).sqrt().lower()


def disc_box(center: complex, r: arb) -> acb:
    """A complex box containing the disc of radius r about center."""
    return acb(arb(center.real) + iv(-r, r), arb(center.imag) + iv(-r, r))


class Stratum:
    """A fixed quartic F(z) = z^4 + a z^2 + b z with two real critical values.

    crit maps 'A' and 'B' to the critical points (w, multiplicity m) whose value
    is fA or fB; mult counts critical points with multiplicity.
    """

    def __init__(
        self, name: str, a: float, b: float, fA: float, fB: float, crit_A, crit_B
    ):
        self.name = name
        self.a = arb(a)
        self.b = arb(b)
        self.af = a
        self.bf = b
        self.fval = {'A': arb(fA), 'B': arb(fB)}
        self.fA = arb(fA)
        self.fB = arb(fB)
        self.d = self.fB - self.fA
        self.crit = {
            'A': [(arb(w), m) for w, m in crit_A],
            'B': [(arb(w), m) for w, m in crit_B],
        }
        self.mult = {X: sum(m for _, m in self.crit[X]) for X in 'AB'}
        self.gam = {X: max(arb(m) / (m + 1) for _, m in self.crit[X]) for X in 'AB'}

    def F(self, z):
        z2 = z * z
        return (z2 + self.a) * z2 + self.b * z

    def dF(self, z):
        return (4 * z * z + 2 * self.a) * z + self.b

    def taylor(self, w):
        """c2 and c3 in F(w + t) = F(w) + F'(w) t + c2 t^2 + c3 t^3 + t^4."""
        return 6 * w * w + self.a, 4 * w

    def approx_roots(self, sig: complex):
        return np.roots([1.0, 0.0, self.af, self.bf, -sig])

    def rouche_disc(self, z0: complex, sig: acb):
        """A radius r with exactly one root of F - s in D(z0, r) for all s in sig.

        On |z - z0| = r, F - s differs from F'(z0)(z - z0) by at most
        |F(z0) - s| + |c2| r^2 + |c3| r^3 + r^4; Rouché needs this below |F'(z0)| r.
        """
        zc = acb(z0)
        ph = mag_hi(self.F(zc) - sig)
        pd = mag_lo(self.dF(zc))
        if not pos(pd):
            return None
        c2, c3 = self.taylor(zc)
        c2h = mag_hi(c2)
        c3h = mag_hi(c3)
        r = up(2 * ph / pd) + arb(1e-15) * (1 + abs(z0))
        for _ in range(16):
            if bool(ph + c2h * r * r + c3h * r**3 + r**4 < pd * r):
                return up(r)
            r = 2 * r
        return None

    def enclose_roots(self, sig: acb):
        """Four pairwise disjoint certified discs, one root of F - s each."""
        mid = complex(float(sig.real.mid()), float(sig.imag.mid()))
        out = []
        for z0 in self.approx_roots(mid):
            r = self.rouche_disc(complex(z0), sig)
            if r is None:
                return None
            out.append((complex(z0), r))
        if not disjoint(out):
            return None
        return out

    def inv_dF_bounds(self, zc: complex, r: arb):
        """Bounds of 1/|F'| on D(zc, r) from the Taylor expansion of F' at zc."""
        z = acb(zc)
        spread = mag_hi(12 * z * z + 2 * self.a) * r + 12 * mag_hi(z) * r * r + 4 * r**3
        lo_d = mag_lo(self.dF(z)) - spread
        if not pos(lo_d):
            return None
        return lo(1 / (mag_hi(self.dF(z)) + spread)), up(1 / lo_d)

    def window_eta(self, X: str, r: arb) -> arb | None:
        """A lower bound of |F - fX| on every circle |z - w| = r, w of value fX.

        A positive value also certifies, by Rouché against the leading term,
        that F - fX has m + 1 zeros in each disc D(w, r).
        """
        best = None
        for w, m in self.crit[X]:
            c2, c3 = self.taylor(acb(w))
            if m == 1:
                e = lo(mag_lo(c2) * r * r - mag_hi(c3) * r**3 - r**4)
            else:
                e = lo(mag_lo(c3) * r**3 - r**4)
            best = e if best is None or bool(e < best) else best
        return best


def disjoint(discs) -> bool:
    """Whether the discs (center, radius) are pairwise disjoint."""
    for i in range(len(discs)):
        for j in range(i + 1, len(discs)):
            gap = mag_lo(acb(discs[i][0]) - acb(discs[j][0]))
            if not bool(gap > discs[i][1] + discs[j][1]):
                return False
    return True


def strata() -> list[Stratum]:
    return [
        Stratum(
            'double critical point', -1.5, -1.0, -1.5, 0.1875, [(1.0, 1)], [(-0.5, 2)]
        ),
        Stratum(
            'equal values', -2.0, 0.0, -1.0, 0.0, [(1.0, 1), (-1.0, 1)], [(0.0, 1)]
        ),
    ]


# ---------------------------------------------------------------------------
# densities over a ball of sigma values


def near_bounds(S: Stratum, zc: complex, r: arb, w: arb, m: int, ratio_g: arb):
    """Bounds of |o|^g / |F'(z)|, g = m/(m+1), for a root z in D(zc, r).

    With F - f = (z - w)^(m+1) Q(z), identity (13) gives
    |F'(z)| = (|s - f| / |Q(z)|)^g |(m+1) Q(z) + (z - w) Q'(z)|, and ratio_g
    encloses (|o| / |s - f|)^g.
    """
    t = disc_box(zc, r) - w
    c2, c3 = S.taylor(w)
    if m == 1:
        Q = c2 + c3 * t + t * t
        Qd = c3 + 2 * t
    else:
        Q = c3 + t
        Qd = acb(1)
    g = arb(m) / (m + 1)
    den = (m + 1) * Q + t * Qd
    qlo = mag_lo(Q)
    dlo = mag_lo(den)
    if not (pos(qlo) and pos(dlo)):
        return None
    return lo(lo(ratio_g) * qlo**g / mag_hi(den)), up(
        up(ratio_g) * mag_hi(Q) ** g / dlo
    )


def weighted_density(S: Stratum, sig: acb, X: str, ratio: arb, o_lo: arb, o_hi: arb):
    """Bounds of |o|^gam G_F(s) for s in sig, o in [o_lo, o_hi], gam = gam[X].

    Roots within 1/2 of a critical point of value fX use identity (13); the
    others use the Taylor bound for 1/|F'| times o^gam.
    """
    rts = S.enclose_roots(sig)
    if rts is None:
        return None
    gam = S.gam[X]
    L = ZERO
    U = ZERO
    for zc, r in rts:
        done = False
        for w, m in S.crit[X]:
            if abs(zc - float(w.mid())) + float(r.mid()) < 0.5:
                g = arb(m) / (m + 1)
                v = near_bounds(S, zc, r, w, m, ratio**g)
                if v is None:
                    return None
                L = L + lo(v[0] * o_lo ** (gam - g))
                U = U + up(v[1] * o_hi ** (gam - g))
                done = True
                break
        if not done:
            v = S.inv_dF_bounds(zc, r)
            if v is None:
                return None
            L = L + lo(v[0] * o_lo**gam)
            U = U + up(v[1] * o_hi**gam)
    return lo(L), up(U)


def window(S: Stratum, X: str, r: arb, sig_ball: acb, length: arb):
    """Upper bound of the integral of G_F |ds| over a window arc near fX.

    The arc has sigma-length at most `length` and lies in sig_ball, within the
    distance window_eta(X, r) of fX. Each disc D(w, r) holds m + 1 roots and
    at most 8 pi r of the curve; the other roots lie in certified discs disjoint
    from those discs, and contribute length times a bound for 1/|F'|.
    """
    eta = S.window_eta(X, r)
    if not (pos(eta) and bool(mag_hi(sig_ball - acb(S.fval[X])) < eta)):
        return None
    crofton = [(complex(float(w.mid())), r) for w, _ in S.crit[X]]
    inner = sum(m + 1 for _, m in S.crit[X])
    outer = [
        z
        for z in S.approx_roots(float(S.fval[X].mid()))
        if min(abs(z - c) for c, _ in crofton) > 10 * float(r.mid())
    ]
    if len(outer) != 4 - inner:
        return None
    discs = []
    for z0 in outer:
        rr = S.rouche_disc(complex(z0), sig_ball)
        if rr is None:
            return None
        discs.append((complex(z0), rr))
    if not disjoint(discs + crofton):
        return None
    total = len(crofton) * 8 * PI * r
    for zc, rr in discs:
        v = S.inv_dF_bounds(zc, rr)
        if v is None:
            return None
        total = total + length * v[1]
    return up(total)


def weight_integral(o1: arb, o2: arb, g: arb):
    """Bounds of the integral of t^(-g) over [o1, o2]."""
    e = 1 - g
    return lo((lo(o2) ** e - up(o1) ** e) / e), up((up(o2) ** e - lo(o1) ** e) / e)


def geometric(start: float, end: float, q: float) -> list[float]:
    """Points start, start q, start q^2, ... and end, for 0 < start < end."""
    if not 0 < start < end:
        raise ValueError('geometric needs 0 < start < end')
    pts = [start]
    while pts[-1] * q < end:
        pts.append(pts[-1] * q)
    pts.append(end)
    return pts


def adapt(evalfn: Callable, pieces, rel=REL_TOL, absl=1e-5, maxdepth=40):
    """Sum piece bounds, bisecting a piece while its two bounds differ too much.

    evalfn(o1, o2) returns (lower, upper) bounds of the integral over [o1, o2],
    or None when a certificate fails. Pieces tile their range exactly. Returns
    (sum of uppers, sum of lowers, piece count) or None.
    """
    stack = [(p[0], p[1], 0) for p in pieces]
    SU = ZERO
    SL = ZERO
    n = 0
    while stack:
        o1, o2, dep = stack.pop()
        if not o1 < o2:
            raise ValueError('reversed piece')
        v = evalfn(o1, o2)
        if v is not None and not (
            v[0].is_finite() and v[1].is_finite() and bool(v[0] <= v[1])
        ):
            v = None
        if v is not None and (
            bool(v[1] - v[0] <= rel * abs(v[1]) + absl) or dep >= maxdepth
        ):
            SU = SU + v[1]
            SL = SL + v[0]
            n += 1
            continue
        if dep >= maxdepth or (v is None and dep >= 24):
            return None
        mid = (o1 * o2) ** 0.5 if o1 > 0 and o2 / o1 > 1.5 else 0.5 * (o1 + o2)
        stack.append((o1, mid, dep + 1))
        stack.append((mid, o2, dep + 1))
    return up(SU), lo(SL), n


# ---------------------------------------------------------------------------
# far field: identity (11) and the bracket of (12) with sigma0 = fA


def y_bounds(S: Stratum, sig: acb):
    """Enclosures of y_k = log(4 prod_j |s - f_j|^(1/4) / |F'(z_k)|), k = 1..4."""
    rts = S.enclose_roots(sig)
    if rts is None:
        return None
    vals = [(S.fA, S.mult['A']), (S.fB, S.mult['B'])]
    ls_lo = ZERO
    ls_hi = ZERO
    for f, m in vals:
        q = 1 - acb(f) / sig
        ls_lo = ls_lo + m * mag_lo(q).log()
        ls_hi = ls_hi + m * mag_hi(q).log()
    ys = []
    for zc, r in rts:
        Z = disc_box(zc, r)
        if abs(zc) - float(r.mid()) >= 2.0:
            # y = (1/4) sum_j log|1 - f_j/s| + (3/4) log|A(e)| - log|B(e)|, e = 1/z
            e = 1 / Z
            e2 = e * e
            A = 1 + S.a * e2 + S.b * e2 * e
            B = 1 + (S.a / 2) * e2 + (S.b / 4) * e2 * e
            if not (pos(mag_lo(A)) and pos(mag_lo(B))):
                return None
            yl = ls_lo / 4 + arb(3) / 4 * mag_lo(A).log() - mag_hi(B).log()
            yh = ls_hi / 4 + arb(3) / 4 * mag_hi(A).log() - mag_lo(B).log()
        else:
            base_lo = ZERO
            base_hi = ZERO
            for f, m in vals:
                q = sig - acb(f)
                base_lo = base_lo + m * mag_lo(q).log()
                base_hi = base_hi + m * mag_hi(q).log()
            fd = S.dF(Z)
            if not pos(mag_lo(fd)):
                return None
            yl = arb(4).log() + base_lo / 4 - mag_hi(fd).log()
            yh = arb(4).log() + base_hi / 4 - mag_lo(fd).log()
        ys.append((lo(yl), up(yh)))
    return ys


def bracket_bounds(S: Stratum, sig: acb, d_over_tau: acb):
    """Bounds of |1 - d/tau|^(-mB/4) (1 + Delta) - 1, tau = s - fA, d = fB - fA.

    Delta = (1/4) sum_k E(y_k) with E(y) = e^y - 1 - y, because sum_k y_k = 0.
    """
    ys = y_bounds(S, sig)
    if ys is None:
        return None
    Dl = ZERO
    Dh = ZERO
    for yl, yh in ys:
        a = yl.expm1() - yl
        b = yh.expm1() - yh
        Dh = Dh + (up(a) if bool(up(a) > up(b)) else up(b))
        if bool(yl > 0) or bool(yh < 0):
            low = lo(a) if bool(lo(a) < lo(b)) else lo(b)
            Dl = Dl + (low if pos(low) else ZERO)
    Dl = lo(Dl / 4)
    Dh = up(Dh / 4)
    q = 1 - d_over_tau
    e = -arb(S.mult['B']) / 4
    return lo(lo(mag_hi(q) ** e) * (1 + Dl) - 1), up(up(mag_lo(q) ** e) * (1 + Dh) - 1)


def far_constant(S: Stratum, T: arb):
    """K with |bracket| <= K / |tau| whenever |tau| = |s - fA| >= T.

    All roots satisfy |z| >= rho = (|s|/(1 + th))^(1/4), so e = 1/|z| obeys
    e^2 <= ce / |tau|^(1/2). Writing psi(e) = (a/4) e^2 + (b/2) e^3 + R(e) with
    |R| <= (3/8) u^2/(1-u) + v^2/(2(1-v)), and using the power sums
    p2 = b^2/s^2 + 2a/s, p3 = b^3/s^3 + 3ab/s^2, gives |y_k| <= Y0 (T/|tau|)^(1/2).
    Then |tau| Delta <= T Y0^2 e^Y0 / 2 and
    |tau| (|1 - d/tau|^(-mB/4) - 1) <= (mB/4) d (1 - d/T)^(-1 - mB/4).
    """
    A = abs(S.a)
    B = abs(S.b)
    sl = lo(T - abs(S.fA))
    rl = (sl / 2).root(4)
    th = A / rl**2 + B / rl**3
    if not bool(th <= 1):
        return None
    ce = ((1 + th) * T / sl).sqrt()
    e2 = ce / T.sqrt()
    e = e2.sqrt()
    um = A * e2 + B * e2 * e
    vm = A * e2 / 2 + B * e2 * e / 4
    if not (bool(um < 1) and bool(vm < 1)):
        return None
    Rm = arb(3) / 8 * um * um / (1 - um) + vm * vm / (2 * (1 - vm))
    p2 = B * B / sl**2 + 2 * A / sl
    p3 = B**3 / sl**3 + 3 * A * B / sl**2
    Y0 = (A / 4) * (e2 + p2 / 4) + (B / 2) * (e2 * e + p3 / 4) + 2 * Rm
    E0 = Y0.expm1() - Y0
    mu = S.d / T
    if not bool(mu < arb(1) / 2):
        return None
    mB = arb(S.mult['B'])
    K = (mB / 4) * S.d * (1 - mu) ** (-1 - mB / 4) * (
        1 + E0
    ) + T * Y0 * Y0 * Y0.exp() / 2
    return up(K)


# ---------------------------------------------------------------------------
# large circles and the line


def large_circles(S: Stratum, b_lo: float, b_hi: float):
    """Bounds (upper, lower, pieces) of Itilde for beta in [b_lo, b_hi], or None."""
    beta = iv(b_lo, b_hi)
    sb = beta.sin()
    cb = beta.cos()
    kap = 2 * sb / S.d
    if b_lo == 0.0:
        kap = iv(0, up(kap))
        sb = iv(0, up(sb))
    xB = S.d / cb
    eib = acb(cb, -sb)
    eipb = acb(cb, sb)
    ik2 = acb(0, kap / 2)
    kl = lo(kap) if pos(lo(kap)) else ZERO
    kh = up(kap)
    r = arb(R_WIN)
    TU = ZERO
    TL = ZERO
    N = 0

    def ref_near_A(o1, o2):
        # integral of o^(-3/4) (1 + kappa^2 o^2/4)^(-5/8) over [o1, o2]
        base = 4 * (o2 ** (arb(1) / 4) - o1 ** (arb(1) / 4))
        fl = (1 + kh * kh * o2 * o2 / 4) ** (-arb(5) / 8)
        fh = (1 + kl * kl * o1 * o1 / 4) ** (-arb(5) / 8)
        return lo(lo(base) * lo(fl)), up(up(base) * up(fh))

    def ref_at(x: arb):
        # |x|^(-3/4) (1 + kappa^2 x^2/4)^(-5/8) over a ball not containing 0
        ax = abs(x)
        hi_ = lo(ax) ** (-arb(3) / 4) * (1 + kl * kl * lo(ax) ** 2 / 4) ** (-arb(5) / 8)
        lo_ = up(ax) ** (-arb(3) / 4) * (1 + kh * kh * up(ax) ** 2 / 4) ** (-arb(5) / 8)
        return lo(lo_), up(hi_)

    # windows |x| <= hA and |x - xB| <= hB; |s - fX| <= |offset| there
    hs = {}
    for X in 'AB':
        hs[X] = float(lo(arb(0.6) * S.window_eta(X, r)).mid()) * (1 - 1e-12)
        h = arb(hs[X])
        wv = window(S, X, r, acb(S.fval[X]) + acb(iv(-h, h), iv(-h, h)), up(2 * h))
        if wv is None:
            return None
        if X == 'A':
            rl = lo(8 * h ** (arb(1) / 4) * (1 + kh * kh * h * h / 4) ** (-arb(5) / 8))
            rh = up(8 * h ** (arb(1) / 4))
        else:
            a_, b_ = ref_at(xB + iv(-h, h))
            rl = lo(2 * h * a_)
            rh = up(2 * h * b_)
        TU = TU + wv - rl
        TL = TL - rh

    def ev_A(o1f, o2f, sgn):
        o1 = arb(o1f)
        o2 = arb(o2f)
        x = sgn * iv(o1, o2)
        den = 1 - ik2 * x
        sig = acb(S.fA) + eib * x / den
        gb = weighted_density(S, sig, 'A', iv(mag_lo(den), mag_hi(den)), o1, o2)
        if gb is None:
            return None
        wl, wu = weight_integral(o1, o2, S.gam['A'])
        rl, rh = ref_near_A(o1, o2)
        w_hi = up(1 / (1 + kl * kl * o1 * o1 / 4))
        w_lo = lo(1 / (1 + kh * kh * o2 * o2 / 4))
        return lo(w_lo * gb[0] * wl - rh), up(w_hi * gb[1] * wu - rl)

    def ev_B(o1f, o2f, sgn):
        o1 = arb(o1f)
        o2 = arb(o2f)
        ob = iv(o1, o2)
        x = xB + sgn * ob
        den1 = 1 - ik2 * x
        den0 = 1 - ik2 * xB
        sig = acb(S.fB) + eib * (sgn * ob) / (den1 * den0)
        ratio = iv(mag_lo(den1) * mag_lo(den0), mag_hi(den1) * mag_hi(den0))
        gb = weighted_density(S, sig, 'B', ratio, o1, o2)
        if gb is None:
            return None
        wl, wu = weight_integral(o1, o2, S.gam['B'])
        rl, rh = ref_at(x)
        ax = abs(x)
        w_hi = up(1 / (1 + kl * kl * lo(ax) ** 2 / 4))
        w_lo = lo(1 / (1 + kh * kh * up(ax) ** 2 / 4))
        return lo(w_lo * gb[0] * wl - up(o2 - o1) * rh), up(
            w_hi * gb[1] * wu - lo(o2 - o1) * rl
        )

    def ev_u(u1f, u2f, sgn):
        # x = 1/u; the integrand is (u^2 + kappa^2/4)^(-5/8) times the bracket
        u1 = arb(u1f)
        u2 = arb(u2f)
        ub = sgn * iv(u1, u2)
        den = ub - ik2
        sig = acb(S.fA) + eib / den
        bb = bracket_bounds(S, sig, S.d * eipb * den)
        if bb is None:
            return None
        m2 = ub * ub + kap * kap / 4
        if not pos(lo(m2)):
            return None
        fac_h = lo(m2) ** (-arb(5) / 8)
        fac_l = up(m2) ** (-arb(5) / 8)
        lb, hb = bb
        if bool(hb < 0):
            ph = up(lo(fac_l) * hb)
        else:
            ph = up(up(fac_h) * up(hb)) if bool(up(hb) > 0) else ZERO
        if bool(lb > 0):
            pl = lo(lo(fac_l) * lb)
        else:
            pl = lo(up(fac_h) * lo(lb)) if bool(lo(lb) < 0) else ZERO
        wid_h = up(u2 - u1)
        wid_l = lo(u2 - u1)
        U = up(wid_h * ph) if bool(ph >= 0) else up(wid_l * ph)
        L = lo(wid_l * pl) if bool(pl >= 0) else lo(wid_h * pl)
        return L, U

    def run(evf, pieces, sgn):
        return adapt(lambda a, b: evf(a, b, sgn), pieces)

    hA = hs['A']
    hB = hs['B']
    J = float(lo(xB).mid()) / 2 * (1 - 1e-9)
    Jm = X_MID - float(up(xB).mid()) * (1 + 1e-9)
    if not (hA < J and hB < J and hB < Jm):
        return None
    jobs = [
        (ev_A, geometric(hA, J, 2.0), 1),
        (ev_A, geometric(hA, X_MID, 2.0), -1),
        (ev_B, geometric(hB, J, 2.0), -1),
        (ev_B, geometric(hB, Jm, 2.0), 1),
    ]
    for evf, pts, sgn in jobs:
        res = run(evf, [(pts[k], pts[k + 1]) for k in range(len(pts) - 1)], sgn)
        if res is None:
            return None
        TU = TU + res[0]
        TL = TL + res[1]
        N += res[2]
    # junctions [J, xB - J] and [xB + Jm, X_MID], of width below 2 rad(xB) + 1e-8
    for xa, xb in ((arb(J), xB - arb(J)), (xB + arb(Jm), arb(X_MID))):
        xball = iv(lo(xa), up(xb))
        wid = up(xb - xa)
        if not bool(lo(xb - xa) > -(arb(2) ** -60)):
            return None
        rts = S.enclose_roots(acb(S.fA) + eib * xball / (1 - ik2 * xball))
        if rts is None:
            return None
        gh = ZERO
        for zc, rr in rts:
            v = S.inv_dF_bounds(zc, rr)
            if v is None:
                return None
            gh = gh + v[1]
        wpos = wid if bool(wid > 0) else ZERO
        TU = TU + up(wpos * gh)
        TL = TL - up(wpos * ref_at(xball)[1])
    # |x| >= X_MID through u = 1/x
    # The x/u junction is the exact number 1/X_MID. Use a shared binary
    # endpoint below it and integrate the remaining sliver explicitly;
    # signed integrals cannot silently omit or double-count an overlap.
    u_end = ONE / arb(X_MID)
    U1 = float(np.nextafter(1.0 / X_MID, 0.0))
    if not bool(arb(U1) < u_end):
        return None
    Tf = arb(T_FAR)
    if bool(kh / 2 < 1 / Tf):
        # |u| <= Uf lies in |tau| >= T_FAR, where |integrand| <= K |u|^(-1/4)
        Uf = lo((1 / (Tf * Tf) - kh * kh / 4).sqrt())
        Kf = far_constant(S, Tf)
        if Kf is None:
            return None
        uf = float(Uf.mid()) * (1 - 1e-9)
        if not (uf > 0 and bool(arb(uf) < Uf)):
            return None
        # Both pieces meet at precisely arb(uf), not at different rounded
        # versions of the analytic threshold Uf.
        cf = up(Kf * arb(8) / 3 * arb(uf) ** (arb(3) / 4))
        TU = TU + cf
        TL = TL - cf
        pts = geometric(uf, U1, 2.0)
        far = [(pts[k], pts[k + 1]) for k in range(len(pts) - 1)]
    else:
        # the circle stays within |tau| < T_FAR: pieces run through the antipode u = 0
        if not pos(lo(kap)):
            return None
        uc = min(float(lo(kap).mid()) / 4, U1 / 2)
        pts = geometric(uc, U1, 2.0)
        far = [(pts[k], pts[k + 1]) for k in range(len(pts) - 1)] + [(0.0, uc)]
    for sgn in (1, -1):
        res = run(ev_u, far, sgn)
        if res is None:
            return None
        TU = TU + res[0]
        TL = TL + res[1]
        N += res[2]
        junction = ev_u(arb(U1), u_end, sgn)
        if junction is None:
            return None
        TU = TU + junction[1]
        TL = TL + junction[0]
        N += 1
    return up(TU), lo(TL), N


# ---------------------------------------------------------------------------
# small circles


def small_circles(S: Stratum, b_lo: float, b_hi: float):
    """Bounds (upper, None, pieces) of Itilde for beta in [b_lo, b_hi], or None.

    The circle has radius R = d/(2 sin beta) and center (fA + fB)/2 + i R cos beta,
    fA sits at angle -pi/2 - beta and fB at -pi/2 + beta. Pieces measured from each
    value reach the midpoints of both arcs, so they cover the circle for every
    beta of the box; G_F >= 0 makes the over-coverage harmless.
    """
    beta = iv(b_lo, b_hi)
    sb = beta.sin()
    cb = beta.cos()
    R = S.d / (2 * sb)
    rel = {'A': acb(-R * sb, -R * cb), 'B': acb(R * sb, -R * cb)}
    r = arb(R_WIN)
    TU = ZERO
    N = 0
    for X in 'AB':
        hf = float(lo(arb(0.6) * S.window_eta(X, r) / up(R)).mid()) * (1 - 1e-12)
        h = arb(hf)
        box = iv(-up(R) * h, up(R) * h)
        wv = window(S, X, r, acb(S.fval[X]) + acb(box, box), up(2 * R * h))
        if wv is None:
            return None
        TU = TU + wv
        long_end = float(np.nextafter(float((PI - arb(b_lo)).upper()), np.inf))
        if not bool(arb(long_end) > PI - arb(b_lo)):
            return None
        ends = {
            ('A', 1): b_hi,
            ('A', -1): long_end,
            ('B', -1): b_hi,
            ('B', 1): long_end,
        }
        for sgn in (1, -1):

            def ev(o1f, o2f, X=X, sgn=sgn):
                o1 = arb(o1f)
                o2 = arb(o2f)
                ob = iv(o1, o2)
                sig = acb(S.fval[X]) + rel[X] * (acb(0, sgn * ob).exp() - 1)
                half = ob / 2
                gb = weighted_density(S, sig, X, 1 / (R * half.sin() / half), o1, o2)
                if gb is None:
                    return None
                wl, wu = weight_integral(o1, o2, S.gam[X])
                return lo(lo(R) * gb[0] * wl), up(up(R) * gb[1] * wu)

            pts = geometric(hf, ends[(X, sgn)], 2.0)
            res = adapt(ev, [(pts[k], pts[k + 1]) for k in range(len(pts) - 1)])
            if res is None:
                return None
            TU = TU + res[0]
            N += res[2]
    return up(TU - lo(R) ** (arb(1) / 4) * L0), None, N


# ---------------------------------------------------------------------------
# covering the pencil


def bound_box(S: Stratum, b_lo: float, b_hi: float):
    if b_hi <= BETA_SPLIT:
        return large_circles(S, b_lo, b_hi)
    return small_circles(S, b_lo, b_hi)


def cover(S: Stratum, edges: list[float], checker: Checker):
    """Bound every box between consecutive edges, bisecting failed boxes."""
    worst = None
    leaves = []
    count = 0

    def visit(b_lo: float, b_hi: float, depth: int) -> bool:
        nonlocal worst, count
        res = bound_box(S, b_lo, b_hi)
        if res is not None and bool(res[0] < TARGET):
            leaves.append((b_lo, b_hi))
            count += res[2]
            worst = res[0] if worst is None or bool(res[0] > worst) else worst
            return True
        if depth >= MAX_SPLIT:
            detail = (
                'certificate failed' if res is None else f'upper bound {res[0].str(5)}'
            )
            checker.check(
                f'{S.name}: Itilde < -1 for beta in [{b_lo}, {b_hi}]', False, detail
            )
            return False
        mid = 0.5 * (b_lo + b_hi) if b_lo > 0 else b_hi / 10
        return visit(b_lo, mid, depth + 1) and visit(mid, b_hi, depth + 1)

    ok = True
    for k in range(len(edges) - 1):
        ok = visit(edges[k], edges[k + 1], 0) and ok
    tiled = (
        bool(leaves)
        and leaves[0][0] == edges[0]
        and leaves[-1][1] == edges[-1]
        and all(leaves[i][1] == leaves[i + 1][0] for i in range(len(leaves) - 1))
    )
    checker.check(f'{S.name}: boxes tile [{edges[0]}, {edges[-1]}]', ok and tiled)
    return leaves, worst, count


def full_edges() -> list[float]:
    edges = [0.0, 1e-4, 1e-3]
    while edges[-1] * 1.25 < BETA_SPLIT:
        edges.append(edges[-1] * 1.25)
    edges.append(BETA_SPLIT)
    b = BETA_SPLIT
    while b + 0.01 < 1.0 - 1e-9:
        b = round(b + 0.01, 10)
        edges.append(b)
    edges.append(1.0)
    b = 1.0
    while b + 0.02 < float(np.pi / 2):
        b = round(b + 0.02, 10)
        edges.append(b)
    # end above pi/2: beta slightly beyond pi/2 still indexes a circle of the pencil
    edges.append(float(np.pi / 2) + 1e-12)
    return edges


def main() -> int:
    """Cover the pencil of each stratum and run the controls."""
    parser = evidence_parser(
        'Bound the quartic deficit integral on both collision strata.'
    )
    parser.add_argument(
        '--only',
        choices=['double', 'equal'],
        help='check one stratum only (the default checks both)',
    )
    args = parser.parse_args()
    checker = Checker()
    beta_form = (
        arb(2).root(4)
        * (arb(1) / 2).gamma()
        * (arb(1) / 8).gamma()
        / (arb(5) / 8).gamma()
    )
    checker.check(
        'l(z^4 - 1) = 2^(1/4) B(1/2, 1/8) is near 11.0700',
        bool(abs(L0 - arb('11.0700205')) < arb(1e-6)) and L0.overlaps(beta_form),
    )
    checker.check('pi/2 lies below the last edge', bool(PI / 2 < arb(full_edges()[-1])))
    for S in strata():
        if args.only and not S.name.startswith(args.only):
            continue
        if args.quick:
            edges = [0.0, 1e-4, 1e-3, 1.3e-3]
            leaves, worst, count = cover(S, edges, checker)
            more, worst2, count2 = cover(S, [1.5, 1.52], checker)
            leaves += more
            count += count2
            worst = (
                worst2
                if worst is None or (worst2 is not None and bool(worst2 > worst))
                else worst
            )
        else:
            leaves, worst, count = cover(S, full_edges(), checker)
        if worst is not None:
            print(
                f'{S.name}: {len(leaves)} boxes, {count} pieces, largest upper bound {worst.str(5)}'
            )
        # control: on one box the two bounds bracket a narrow interval below -1
        res = large_circles(S, 0.0, 1e-4)
        ctrl = (
            res is not None
            and bool(res[1] <= res[0])
            and bool(res[0] - res[1] < arb(1) / 2)
        )
        detail = '' if res is None else f'{res[1].str(5)} .. {res[0].str(5)}'
        checker.check(
            f'{S.name}: control bounds at beta in [0, 1e-4] are ordered and within 1/2',
            ctrl,
            detail,
        )
        # negative control: the bounds enclose the line value, so no target below it passes there
        v = arb(LINE_VALUE[S.name])
        neg = res is not None and bool(res[1] < v) and bool(v < res[0])
        checker.check(
            f'{S.name}: control bounds at beta in [0, 1e-4] enclose the line value {LINE_VALUE[S.name]}',
            neg,
            detail,
        )
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

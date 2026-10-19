"""Check the cubic family length inequality of L144 in ball arithmetic.

For 0 < a <= 2^(-1/3) and c = sqrt(1 - 4a^6), let L(a) be the length of the
lemniscate |z^3 + 3a^2 z - c| = 1. The program proves L(a) < L0 for every such
a, where L0 = 2 pi Gamma(1/3) / Gamma(2/3)^2 is the length for z^3 - 1, using
the integral formulas derived in the proof page:

- Regime A, 0 < a <= 13/64: an upper bound below zero for the integral I(a)
  of g = G1 - |sigma|^(-2/3) over the scaled circle, with an explicit tail
  bound; then L(a) = Phi(c) + a I(a) < Phi(c) <= Phi(1) = L0.
- Regime B, beta = arcsin(2a^3) in [7/512, pi/2]: an upper bound below L0 for
  L(a) itself, uniformly on each parameter box, with an explicit window bound
  at the critical value on the circle.

Every integral bound is a sum of (supremum over a piece) times (piece width),
computed with arb balls through python-flint, so it is an upper bound for every
parameter in the box. Tolerances only affect sharpness. A coverage check joins
the two regimes. A control computes upper and lower bounds at one parameter
and checks that they bracket a narrow interval.

Arithmetic: python-flint arb and acb balls at 64 bits. Runtime: about five
minutes on one thread. No floating-point tolerance enters a conclusion.
Run from the repository root with uv run --no-sync python and this path.
"""

from __future__ import annotations

import sys
from collections.abc import Callable

from flint import acb, arb, ctx

from tools import Checker, evidence_parser

ctx.prec = 64
ctx.threads = 1
PI = arb.pi()
OMEGA = acb(arb(2) / 3).exp_pi_i()
OMEGAS = [acb(1), OMEGA, OMEGA * OMEGA]
I_UNIT = acb(0, 1)
L0 = 2 * PI * (arb(1) / 3).gamma() / ((arb(2) / 3).gamma() ** 2)

# exact dyadic breakpoints
A_END = arb(13) / 64
A_BOXES = 13
Y_CUT = arb(50)
ETA = arb(2) ** -10
DELTA_A = arb(2) ** -13
BETA_START = arb(7) / 512
B_INITIAL = 300
B_MARGIN = arb(1) / 100
TOL_A = arb(2) ** -9
TOL_B = arb(2) ** -7


def ball(lo: arb, hi: arb) -> arb:
    """Return a ball containing the interval [lo, hi]."""
    return arb.union(arb(lo), arb(hi))


def sqrt_safe(value: acb) -> acb:
    """Enclose a square root, rotating its cut off a straddled negative axis."""
    if value.real.upper() < 0 and value.imag.contains(0):
        return I_UNIT * (-value).sqrt()
    return value.sqrt()


def cbrt_safe(value: acb) -> acb:
    """A cube root, with the cut rotated off a straddled negative axis."""
    if value.real.upper() < 0 and value.imag.contains(0):
        return -((-value).root(3))
    return value.root(3)


def root_sum(s: acb, a2: arb, a6: arb) -> tuple[arb, arb]:
    """Enclose sum_j |u_j + a2/u_j| and |s^2 + 4 a6|^(1/2).

    Here U - a6/U = s and u_j runs over the cube roots of U, so the roots of
    z^3 + 3 a2 z = s are u_j - a2/u_j and z_j^2 + 4 a2 = (u_j + a2/u_j)^2.
    Either root U of the quadratic gives the same multiset of values.
    """
    disc = sqrt_safe(s * s + 4 * a6)
    first = (s + disc) / 2
    second = (s - disc) / 2
    big = first if abs(first.mid()) >= abs(second.mid()) else second
    root = cbrt_safe(big)
    total = arb(0)
    for unit in OMEGAS:
        u = root * unit
        total += abs(u + a2 / u)
    return total, abs(disc)


def g1(sigma: acb) -> arb:
    """Enclose G1(sigma), the scaled root sum over 3|sigma^2 + 4|^(1/2)."""
    total, disc = root_sum(sigma, arb(1), arb(1))
    return total / (3 * disc)


def piece_bound(value: arb, width: arb, upper: bool) -> arb:
    """Return a bound for value times width in the requested direction."""
    if upper:
        end = arb(value.upper())
        return end * (arb(width.upper()) if end >= 0 else arb(width.lower()))
    end = arb(value.lower())
    return end * (arb(width.lower()) if end >= 0 else arb(width.upper()))


def bound_integral(
    fun: Callable[[arb], arb],
    lo: arb,
    hi: arb,
    tol: arb,
    upper: bool = True,
    max_depth: int = 48,
) -> tuple[arb, int]:
    """Bound the integral of f over [lo, hi], where fun(J) encloses f on J.

    The pieces tile [lo, hi] exactly at dyadic midpoints. A piece stops when its
    spread is at most tol, when halving no longer reduces the spread, or at the
    depth limit; each accepted piece contributes its extreme value times width.
    A nonfinite enclosure at the depth limit is an error.
    """
    if not (lo.is_exact() and hi.is_exact() and lo <= hi):
        raise ArithmeticError('integration endpoints must be ordered exact dyadics')
    total = arb(0)
    count = 0
    stack = [(arb(lo), arb(hi), 0, None)]
    while stack:
        left_end, right_end, depth, known = stack.pop()
        value = known if known is not None else fun(ball(left_end, right_end))
        finite = value.is_finite()
        if finite and (2 * value.rad() <= tol or depth >= max_depth):
            total += piece_bound(value, right_end - left_end, upper)
            count += 1
            continue
        if not finite and depth >= max_depth:
            raise ArithmeticError('nonfinite enclosure at the depth limit')
        middle = arb(((left_end + right_end) / 2).mid())
        first = fun(ball(left_end, middle))
        second = fun(ball(middle, right_end))
        if finite and first.is_finite() and second.is_finite():
            if min(first.rad(), second.rad()) > 0.8 * value.rad():
                total += piece_bound(first, middle - left_end, upper)
                total += piece_bound(second, right_end - middle, upper)
                count += 2
                continue
        stack.append((left_end, middle, depth + 1, first))
        stack.append((middle, right_end, depth + 1, second))
    return total, count


def tail_constant(cut: arb) -> arb:
    """Return K with |g(sigma)| <= K (|sigma| - 1)^(-2) for |sigma| >= cut."""
    e = (cut - 1) ** (arb(-2) / 3)
    main = (e + 1 / (2 * (1 - e))) / (1 - e**3) + (arb(2) / 3) * e
    other = 2 * e / (1 - e**3)
    return arb(arb.union(main, other).upper())


def regime_a_box(a_lo: arb, a_hi: arb) -> tuple[arb, int]:
    """Return an upper bound for I(a), uniformly for a in [a_lo, a_hi]."""
    a = ball(a_lo, a_hi)
    a3 = a**3
    a6 = a3 * a3
    c = (1 - 4 * a6).sqrt()

    def curve(y: arb) -> tuple[acb, arb]:
        r = (1 - a6 * y * y).sqrt()
        return acb(a3 * (y * y - 4) / (c + r), y), 1 / r

    def gw(y: arb) -> arb:
        sigma, weight = curve(y)
        return (g1(sigma) - abs(sigma) ** (arb(-2) / 3)) * weight

    # the piece [0, ETA]: |sigma| <= X + y and weight >= 1
    sigma, weight = curve(ball(arb(0), ETA))
    x_max = arb(abs(sigma.real).upper())
    third = arb(1) / 3
    head = arb((g1(sigma) * weight).upper()) * ETA
    head -= 3 * ((x_max + ETA) ** third - x_max**third)
    # the regular pieces
    first, n1 = bound_integral(gw, ETA, 2 - DELTA_A, TOL_A)
    second, n2 = bound_integral(gw, 2 + DELTA_A, Y_CUT, TOL_A)
    # the window at sigma = 2i, where |sigma - 2i| >= |y - 2|
    sigma, weight = curve(ball(2 - DELTA_A, 2 + DELTA_A))
    roots, _ = root_sum(sigma, arb(1), arb(1))
    coeff = arb((roots * weight / (3 * abs(sigma + 2 * I_UNIT).sqrt())).upper())
    floor = arb(abs(sigma).upper()) ** (arb(-2) / 3)
    window = coeff * 4 * DELTA_A.sqrt() - 2 * DELTA_A * floor
    near = 2 * (head + first + second + window)
    tail = tail_constant(Y_CUT) * 2 / (arb(c.lower()) * Y_CUT * (1 - 1 / Y_CUT) ** 2)
    return arb((near + tail).upper()), n1 + n2


def regime_b_terms(beta: arb) -> tuple[arb, arb, arb, arb]:
    """Return sin(beta), cos(beta), a^2 and a^6 for a^3 = sin(beta)/2."""
    sb = beta.sin()
    a3 = sb / 2
    return sb, beta.cos(), a3.root(3) ** 2, a3 * a3


def regime_b_box(
    b_lo: arb, b_hi: arb, upper: bool = True, tol: arb = TOL_B
) -> tuple[arb, int]:
    """Bound L(a) for arcsin(2a^3) in [b_lo, b_hi]; the lower bound omits the window."""
    sb, cb, a2, a6 = regime_b_terms(ball(b_lo, b_hi))

    def density(theta: arb) -> arb:
        s = acb(cb) + acb(theta.cos(), theta.sin())
        roots, disc = root_sum(s, a2, a6)
        return roots / (3 * disc)

    # the window contains theta_+ = pi - beta for every beta in the box
    spread = b_hi - b_lo + arb(2) ** -20
    w_lo = arb((PI - b_hi - spread).lower())
    w_hi = arb((PI - b_lo + spread).upper())
    critical = PI - ball(b_lo, b_hi)
    if not (
        0 < w_lo < w_hi < PI and w_lo <= critical.lower() and critical.upper() <= w_hi
    ):
        raise ArithmeticError('critical-value window must lie inside [0, pi]')
    first, n1 = bound_integral(density, arb(0), w_lo, tol, upper)
    # Nonnegativity permits outward rounding only for an upper integral bound.
    # The lower bound omits both the singular window and [pi_lower, pi].
    endpoint = arb(PI.upper() if upper else PI.lower())
    second, n2 = bound_integral(density, w_hi, endpoint, tol, upper)
    if not upper:
        return 2 * (first + second), n1 + n2
    span = ball(w_lo, w_hi)
    s = acb(cb) + acb(span.cos(), span.sin())
    roots, _ = root_sum(s, a2, a6)
    coeff = arb((roots / (3 * abs(s + I_UNIT * sb).sqrt())).upper())
    window = coeff * (PI / 2).sqrt() * 2 * (2 * (w_hi - w_lo)).sqrt()
    return arb((2 * (first + second + window)).upper()), n1 + n2


def cover_b(start: arb, end: arb, checker: Checker) -> tuple[int, arb, int]:
    """Cover [start, end] by beta-boxes whose bound is below L0 - B_MARGIN."""
    queue = []
    for k in range(B_INITIAL):
        lo = start if k == 0 else arb((start + (end - start) * k / B_INITIAL).mid())
        hi = (
            end
            if k == B_INITIAL - 1
            else arb((start + (end - start) * (k + 1) / B_INITIAL).mid())
        )
        queue.append((lo, hi))
    boxes = 0
    pieces = 0
    worst = arb(10)
    previous = start
    contiguous = True
    while queue:
        lo, hi = queue.pop(0)
        bound, count = arb(0), 0
        try:
            bound, count = regime_b_box(lo, hi)
            good = bound < L0 - B_MARGIN
        except ArithmeticError:
            good = False
        if good:
            contiguous = contiguous and lo == previous
            previous = hi
            boxes += 1
            pieces += count
            margin = L0 - bound
            worst = margin if margin < worst else worst
            continue
        if hi - lo < arb(2) ** -40:
            checker.check('regime B box resolved', False, f'stuck at {lo}')
            return boxes, worst, pieces
        middle = arb(((lo + hi) / 2).mid())
        queue.insert(0, (middle, hi))
        queue.insert(0, (lo, middle))
    checker.check('regime B boxes tile the beta range', contiguous and previous == end)
    return boxes, worst, pieces


def main() -> int:
    """Run the two regimes, the coverage join and the sharpness control."""
    evidence_parser(
        'Check the cubic family length inequality of L144.', quick=False
    ).parse_args()
    checker = Checker()
    print(f'L0 = {L0.str(15)}')
    checker.check('regime A boxes tile [0, 13/64]', arb(A_BOXES) / 64 == A_END)
    checker.check(
        'regime A near arc is a graph over |y| <= 50', A_END**6 * Y_CUT**2 < 1
    )
    checker.check(
        'regime A far branch lies beyond |sigma| = 50',
        (1 - 4 * A_END**6).sqrt() / A_END**3 > Y_CUT,
    )
    beta_form = (
        arb(2).root(3)
        * (arb(1) / 2).gamma()
        * (arb(1) / 6).gamma()
        / (arb(2) / 3).gamma()
    )
    checker.check('L0 agrees with 2^(1/3) B(1/2, 1/6)', L0.overlaps(beta_form))
    # regime A
    worst_a = arb(-10)
    pieces_a = 0
    for k in range(A_BOXES):
        lo = arb(k) / 64
        hi = arb(k + 1) / 64
        bound, count = regime_a_box(lo, hi)
        pieces_a += count
        worst_a = bound if bound > worst_a else worst_a
        checker.check(
            f'I(a) < 0 for a in [{k}/64, {k + 1}/64]', bound < 0, bound.str(6)
        )
    print(f'regime A: largest upper bound for I(a) {worst_a.str(6)}, {pieces_a} pieces')
    # coverage join: arcsin(2 a^3) at a = 13/64 exceeds the start of regime B
    checker.check('regimes overlap', (2 * A_END**3).asin() > BETA_START)
    checker.check(
        'regime B starts at a below 13/64',
        arb(((BETA_START.sin() / 2).root(3)).upper()) < A_END,
    )
    # regime B
    end = arb((PI / 2).upper())
    boxes, worst_b, pieces_b = cover_b(BETA_START, end, checker)
    print(
        f'regime B: {boxes} boxes, smallest margin {worst_b.str(6)}, {pieces_b} pieces'
    )
    checker.check('regime B margins exceed 1/100', worst_b > B_MARGIN)
    # control: upper and lower bounds at the point a^3 = sin(1/2)/2 bracket a narrow interval
    point = arb(1) / 2
    fine = arb(2) ** -12
    upper_value, _ = regime_b_box(point, point, tol=fine)
    lower_value, _ = regime_b_box(point, point, upper=False, tol=fine)
    print(f'control at beta = 1/2: {lower_value.str(8)} <= L <= {upper_value.str(8)}')
    checker.check(
        'control bounds are ordered and within 0.05',
        lower_value <= upper_value and upper_value - lower_value < arb(5) / 100,
    )
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

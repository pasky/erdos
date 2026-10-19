"""Check the digit-sieve calibration on Problem 273 and the cube-free bound.

Part 1, calibration. Form the 149 moduli p-1 with 5<=p<=877 prime. Read the
digit order and the thresholds t (distortion delta = t/q) from
assets/e273_schedule.json. Run the exact digit-coordinate sieve bound on the
49 moduli whose prime factors are at most 7, and check that the certified
total loss is 115/126 < 1 with the Lemma 3.3 class-mass bound, and
538793/604800 < 1 with the compatibility-weighted bound. Check that each of
the 45 later digit coordinates completes fewer moduli than its size, so it
loses nothing. A control without distortion returns the union bound, which
exceeds one.

Part 2, implementation cross-check. On two small domains, compute the actual
distorted measures for fixed residue choices and check every computed step
loss and class-mass bound against them, for both class-mass recursions.

Part 3, cube-free test. Compute the delta-free lower bound kappa_0/mu_0 on
the tail ratio f_21 that first- and second-moment sieve bounds can certify
after a depth-two initial block. The model keeps the full prefix inventory
and charges every single and ordered pair its shape's maximum class-mass
bound, without compatibility pruning. Check rational intervals for the
floor, which exceeds 138877/1000 for initial blocks [], [3], [3,5], [3,5,7]
but not [3,5,7,11].

Part 4, the same test with the Lemma 3.3 class-mass bounds of the source. A
weak-duality bound over all distortion parameters, evaluated on 400 cells per
prime with monotone cell bounds and rational logarithm enclosures, shows that
no schedule reaches the threshold for the blocks {3,5,7}, {3,5,7,11},
{3,...,13} and {3,...,17}; when the class masses may also use the
compatibility-weighted recursion, the same holds for {3,5,7} and {3,5,7,11}.

Part 5, deeper digits. Repeat the delta-free floor of Part 3 at a uniform
depth D at every odd prime up to 73, in three digit orders: each prime's
digits consecutively, all first digits before all second digits (breadth
first), and each prime's first two digits consecutively followed by the
deeper digits breadth first. At D = 4 every initial block from [] to
[3,...,17] gives a certified mu_0 <= 0 or a floor above 146, in all three
orders. Depth 2 already excludes [] to [3,5,7] and depth 3 excludes
[3,5,7,11] and [3,...,13], in all three orders; at D = 3 the block
[3,...,17] is not excluded. For the block [3,...,19] in the consecutive
order, a bound valid at every depth keeps the floor below 136.74, so no
depth excludes it. Finally check the infinite-depth value of kappa_0 and its
ratio to the threshold.

Part 6, support concentration. Build 2470 distinct odd congruences covering
3Z by a finite valuation partition. Add one class modulo 3 and complete the
prime support through 73 at depth 16 while retaining an explicit uncovered
CRT point. The survivors have one fixed first 3-digit. Check the exact
averaged-kernel lower bound above 152.14, contradicting the universal
138.877 interface. A deleted-class control breaks the partition certificate.

Part 7, the exact-loss tail. Convolve lower atom probabilities with outward
rounded first and second moments. Charge every discarded atom through the
full first moment. With distortion 2/5 through prime 19997, any uniform
surviving density at least 1/4 in the reduced small-prime box meets the
source's termination criterion. An adapted product measure also handles the
16-class density extension. Rational logarithm bounds certify both margins.

Exact rational arithmetic throughout (fractions.Fraction). Python standard
library and the repository Checker; one thread, under a minute, well under
200 MB. Run from the repository root:

    uv run --no-sync python wiki/research/leads/odd_covering_distortion/evidence/main.py

The program checks finite computations only. The reductions that turn them
into the stated results are on the lead's pages (digit_sieve.md,
e273_calibration.md, cube_free_obstruction.md, deep_digit_obstruction.md and
support_concentration.md).
"""

from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path

from util.concentration import check_concentration
from util.tail_density import check_tail_density

from tools import Checker, evidence_parser

THRESHOLD = Fraction(138877, 1000)
LOG_TERMS = 40
LAGRANGE_CELLS = 400
SMALL_PRIMES = [p for p in range(3, 74) if all(p % a for a in range(2, p))]


def primes_upto(n: int) -> list[int]:
    """Return the primes at most n."""
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for a in range(2, int(n**0.5) + 1):
        if sieve[a]:
            for b in range(a * a, n + 1, a):
                sieve[b] = False
    return [a for a in range(n + 1) if sieve[a]]


def factor(n: int) -> dict[int, int]:
    """Return the prime factorization of n >= 1 by trial division."""
    result: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def new_moduli(moduli: list[int], depth: dict[int, int], q: int) -> list[int]:
    """Return the moduli completed when the digit (q, depth[q]) is exposed."""
    out = []
    for d in moduli:
        f = factor(d)
        if f.get(q, 0) == depth[q] and all(f.get(r, 0) <= depth[r] for r in depth):
            if all(r in depth for r in f):
                out.append(d)
    return out


def sieve_bound(
    moduli: list[int],
    primes: list[int],
    order: list[int],
    ts: list[int],
    weighted: bool,
    record: bool = False,
) -> tuple[Fraction, list, list]:
    """Return the certified total loss of the digit sieve.

    Coordinates are exposed in ``order`` (a list of primes; the j-th
    occurrence of q is the digit (q, j)). At a step with coordinate size q
    and threshold t, delta = t/q and the loss is bounded by the sum, over
    (t+1)-sets of completed moduli, of the class-mass bound of the union of
    their projections, divided by q - t. Class-mass bounds c(v) are indexed
    by exponent vectors v; ``weighted`` adds the compatibility-weighted
    recursion to the Lemma 3.3 recursion.
    """
    r = len(primes)
    vec = {d: tuple(factor(d).get(q, 0) for q in primes) for d in moduli}
    depth = [0] * r
    c = {tuple([0] * r): Fraction(1)}
    total = Fraction(0)
    steps = []
    history = []
    for k, q in enumerate(order):
        i = primes.index(q)
        e = depth[i] + 1
        depth[i] = e
        completed = [
            d
            for d in moduli
            if vec[d][i] == e and all(vec[d][j] <= depth[j] for j in range(r))
        ]
        proj = [
            tuple(e - 1 if j == i else vec[d][j] for j in range(r)) for d in completed
        ]
        t = ts[k]
        if not 0 <= t < q:
            raise ValueError('threshold outside 0 <= t < q')
        loss = Fraction(0)
        if len(completed) >= t + 1:
            mass = Fraction(0)
            for subset in itertools.combinations(range(len(completed)), t + 1):
                v = tuple(max(proj[s][j] for s in subset) for j in range(r))
                mass += c[v]
            loss = mass / (q - t)
        delta = Fraction(t, q)
        total += loss
        update = {}
        for v, val in c.items():
            if v[i] != e - 1:
                continue
            w = tuple(e if j == i else v[j] for j in range(r))
            bound = min(val, val / ((1 - delta) * q))
            if weighted:
                meet = sum(
                    (c[tuple(max(v[j], u[j]) for j in range(r))] for u in proj),
                    Fraction(0),
                )
                bound = min(bound, (val + meet / ((1 - delta) * q)) / q)
            update[w] = bound
        c.update(update)
        steps.append((q, e, completed, t, loss))
        if record:
            history.append(dict(c))
    return total, steps, history


def actual_measures(
    moduli: list[int],
    primes: list[int],
    order: list[int],
    ts: list[int],
    residues: dict[int, int],
) -> tuple[list, list]:
    """Return the actual step losses and largest class masses of the sieve.

    The measure after each step lives on Z/M for the current product M of
    exposed digits; fibres are the residues above a point modulo the previous
    product. The distortion follows the capped rule with delta = t/q.
    """
    r = len(primes)
    depth = [0] * r
    modulus = 1
    measure = {0: Fraction(1)}
    losses = []
    largest = []
    for k, q in enumerate(order):
        depth[primes.index(q)] += 1
        nxt = modulus * q
        completed = [d for d in moduli if nxt % d == 0 and modulus % d != 0]
        delta = Fraction(ts[k], q)
        new = {}
        loss = Fraction(0)
        for x in range(modulus):
            px = measure[x]
            fibre = [x + modulus * y for y in range(q)]
            covered = {z for z in fibre if any(z % d == residues[d] for d in completed)}
            alpha = Fraction(len(covered), q)
            for z in fibre:
                if z in covered:
                    if alpha > delta:
                        factor_z = (alpha - delta) / (alpha * (1 - delta))
                    else:
                        factor_z = Fraction(0)
                    new[z] = factor_z * px / q
                    loss += new[z]
                else:
                    new[z] = min(1 / (1 - alpha), 1 / (1 - delta)) * px / q
        measure = new
        modulus = nxt
        losses.append(loss)
        masses = {}
        for v in itertools.product(*[range(depth[j] + 1) for j in range(r)]):
            m = 1
            for j in range(r):
                m *= primes[j] ** v[j]
            classes = [Fraction(0)] * m
            for z, pz in measure.items():
                classes[z % m] += pz
            masses[v] = max(classes)
        largest.append(masses)
    return losses, largest


def check_calibration(checker: Checker) -> None:
    """Part 1: the Problem 273 domain with 5 <= p <= 877."""
    path = Path(__file__).resolve().parent / 'assets' / 'e273_schedule.json'
    data = json.loads(path.read_text())
    moduli = [p - 1 for p in primes_upto(877) if p >= 5]
    checker.check('the domain has 149 moduli p-1 with 5<=p<=877', len(moduli) == 149)
    tops: dict[int, int] = {}
    for d in moduli:
        for q, a in factor(d).items():
            tops[q] = max(tops.get(q, 0), a)
    checker.check(
        'the largest exponents are 2^8, 3^5, 5^3, 7^2, 11^2, 13^2 and one elsewhere',
        {q: a for q, a in tops.items() if a > 1}
        == {2: 8, 3: 5, 5: 3, 7: 2, 11: 2, 13: 2},
    )
    block = [d for d in moduli if max(factor(d)) <= 7]
    density = sum((Fraction(1, d) for d in block), Fraction(0))
    checker.check('the 7-smooth block has 49 moduli', len(block) == 49)
    checker.check(
        'the block reciprocal sum exceeds one, so a union bound fails', density > 1
    )
    primes = data['block_primes']
    order = data['block_order']
    checker.check(
        'the block order exposes every block digit once, in chain order',
        primes == [2, 3, 5, 7]
        and all(order.count(q) == tops[q] for q in primes)
        and len(order) == 18,
    )
    total, steps, _ = sieve_bound(
        block, primes, order, data['t_lemma_3_3'], weighted=False
    )
    checker.check(
        'Lemma 3.3 bound: certified block loss is 115/126 < 1',
        total == Fraction(115, 126) and total < 1,
        f'{total}',
    )
    covered = sorted(d for step in steps for d in step[2])
    checker.check(
        'the block steps complete each block modulus exactly once',
        covered == sorted(block),
    )
    total_w, _, _ = sieve_bound(block, primes, order, data['t_weighted'], weighted=True)
    checker.check(
        'weighted bound: certified block loss is 538793/604800 < 1',
        total_w == Fraction(538793, 604800) and total_w < 1,
        f'{total_w}',
    )
    zero, _, _ = sieve_bound(block, primes, order, [0] * 18, weighted=False)
    checker.check(
        'control: without distortion the bound is the union bound > 1',
        zero == density and zero > 1,
        f'{zero}',
    )
    later = [q for q in sorted(tops) if q > 7]
    depth = {q: tops[q] for q in primes}
    exposed = set(block)
    free = True
    count = 0
    for q in later:
        for _ in range(tops[q]):
            depth[q] = depth.get(q, 0) + 1
            completed = new_moduli(moduli, depth, q)
            exposed.update(completed)
            count += 1
            if len(completed) >= q:
                free = False
    checker.check('45 later digit coordinates follow the block', count == 45)
    checker.check('every later coordinate completes fewer moduli than its size', free)
    checker.check(
        'the later coordinates complete all remaining moduli', exposed == set(moduli)
    )


def check_implementation(checker: Checker) -> None:
    """Part 2: compare the bound recursions with actual distorted measures."""
    cases = [
        (
            [4, 6, 10, 12, 18, 20, 30, 36, 60, 90, 180, 8, 24, 40, 72, 120],
            [2, 3, 5],
            [2, 3, 2, 3, 5, 2],
        ),
        (
            [3, 5, 9, 15, 45, 7, 21, 35, 63, 105, 315, 25, 75],
            [3, 5, 7],
            [3, 5, 3, 7, 5],
        ),
    ]
    schedules = [[0, 1, 1, 2, 3, 1], [1, 0, 2, 4, 1]]
    ok = True
    runs = 0
    for (moduli, primes, order), ts in zip(cases, schedules):
        for weighted in (False, True):
            _, steps, history = sieve_bound(
                moduli, primes, order, ts, weighted, record=True
            )
            for shift in range(4):
                residues = {d: (shift * (j + 1)) % d for j, d in enumerate(moduli)}
                losses, largest = actual_measures(moduli, primes, order, ts, residues)
                runs += 1
                for k in range(len(order)):
                    if losses[k] > steps[k][4]:
                        ok = False
                    for v, mass in largest[k].items():
                        if mass > history[k][v]:
                            ok = False
    checker.check(
        '16 small-domain runs respect every loss and class-mass bound',
        ok and runs == 16,
    )


def cube_free_ratio(block: list[int]) -> tuple[Fraction, Fraction]:
    """Return kappa_0 and mu_0 for a depth-two block (consecutive digit order).

    For each prefix fixed set, its largest class mass is at least the
    reciprocal of the number of classes of that shape. This is a global
    maximum bound, not a conditional lower bound for every individual
    class. On the reduced box the factors are 1/(p-1) for depth one and
    1/(p(p-1)) for depth two. Losses are the smaller of the first- and
    second-moment bounds with 4 delta(1 - delta) <= 1.
    """

    def weight(p: int, z: int) -> Fraction:
        return [Fraction(1), Fraction(1, p - 1), Fraction(1, (p - 1) * p)][z]

    def sums(primes: list[int]) -> tuple[Fraction, Fraction]:
        k1 = Fraction(1)
        k3 = Fraction(1)
        for p in primes:
            k1 *= sum(weight(p, z) for z in range(3))
            k3 *= sum((2 * z + 1) * weight(p, z) for z in range(3))
        return k1, k3

    mu = Fraction(1)
    done = list(block)
    for p in SMALL_PRIMES:
        if p in block:
            continue
        k1, k3 = sums(done)
        first = min((k1 - 1) / (p - 1), (k3 - 2 * k1 + 1) / (p - 1) ** 2)
        second = min(k1 / (p * (p - 1)), k3 / (p * p * (p - 1)))
        mu -= first + second
        done.append(p)
    kappa = sums(SMALL_PRIMES)[1]
    return kappa, mu


def check_cube_free(checker: Checker) -> None:
    """Part 3: the delta-free lower bound on the attainable tail ratio."""
    cases = (([], 33644), ([3], 26321), ([3, 5], 19136), ([3, 5, 7], 14406))
    for block, hundredths in cases:
        kappa, mu = cube_free_ratio(block)
        lower = Fraction(hundredths, 100)
        upper = Fraction(hundredths + 1, 100)
        checker.check(
            f'block {block}: floor in ({lower}, {upper}), LP slack negative',
            mu > 0 and lower * mu < kappa < upper * mu and kappa > THRESHOLD * mu,
        )
    kappa, mu = cube_free_ratio([3, 5, 7, 11])
    checker.check(
        'scope: block [3, 5, 7, 11] has floor in (124.04, 124.05), below threshold',
        mu > 0
        and Fraction(12404, 100) * mu < kappa < Fraction(12405, 100) * mu
        and kappa < THRESHOLD * mu,
    )


def series(v: Fraction) -> tuple[Fraction, Fraction]:
    """Enclose log((1+v)/(1-v)) for rational 0 <= v <= 1/3."""
    if not 0 <= v <= Fraction(1, 3):
        raise ValueError('series argument outside its certified range')
    square = v * v
    power = v
    partial = Fraction(0)
    for j in range(LOG_TERMS):
        partial += 2 * power / (2 * j + 1)
        power *= square
    return partial, partial + 2 * power / ((2 * LOG_TERMS + 1) * (1 - square))


def log_bounds(value: Fraction) -> tuple[Fraction, Fraction]:
    """Enclose the logarithm of a positive rational by reducing to [1, 2)."""
    if value <= 0:
        raise ValueError('logarithm input must be positive')
    log_two = series(Fraction(1, 3))
    exponent = 0
    reduced = Fraction(value)
    while reduced >= 2:
        reduced /= 2
        exponent += 1
    while reduced < 1:
        reduced *= 2
        exponent -= 1
    lower, upper = series((reduced - 1) / (reduced + 1))
    if exponent >= 0:
        return lower + exponent * log_two[0], upper + exponent * log_two[1]
    return lower + exponent * log_two[1], upper + exponent * log_two[0]


def lagrangian_margin(
    block: list[int], lam: Fraction, cells: int, weighted: bool = False
) -> Fraction:
    """Return a certified lower bound for log f_21 minus log(138877/1000).

    Class-mass bounds follow Lemma 3.3 with its monotone cap: a medium first
    digit of p costs min(1, 1/((1 - delta)(p - 1))) and a second digit at
    least 1/p. With ``weighted`` the bounds may also use the
    compatibility-weighted recursion, whose first-digit factor is at least
    (1 + (K_1 - 1)/((1 - delta)(p - 1)))/(p - 1) with K_1 from the averaging
    floor. The block uses the averaging floor and loses nothing. Each
    first-digit loss is bounded below with all earlier distortions set to
    zero, the second-digit losses are dropped, and log(1 + y) >= 2y/(2 + y).
    Weak duality with multiplier lam then bounds log f_21 below by
    log kappa_B + sum_p h_p + 1 - lam + log lam, where h_p is minimized over a
    grid of delta-cells with monotone cell bounds.
    """
    k1 = Fraction(1)
    k3 = Fraction(1)
    for p in block:
        k1 *= 1 + Fraction(1, p - 1) + Fraction(1, (p - 1) * p)
        k3 *= 1 + Fraction(3, p - 1) + Fraction(5, (p - 1) * p)
    total = log_bounds(k3)[0] + 1 - lam + log_bounds(lam)[0]
    half = Fraction(1, 2)
    for p in SMALL_PRIMES:
        if p in block:
            continue
        first = (k1 - 1) / (p - 1)
        second = (k3 - 2 * k1 + 1) / (p - 1) ** 2
        cost = 3 + Fraction(5, p)
        values = []
        for i in range(cells):
            a = Fraction(i, cells)
            b = Fraction(i + 1, cells)
            peak = (
                Fraction(1) if a <= half <= b else max(4 * a * (1 - a), 4 * b * (1 - b))
            )
            nu = min(Fraction(1), 1 / ((1 - a) * (p - 1)))
            if weighted:
                nu = min(nu, (1 + (k1 - 1) / ((1 - a) * (p - 1))) / (p - 1))
            y = cost * nu
            values.append(2 * y / (2 + y) + lam * min(first, second / peak))
        total += min(values)
        k1 *= 1 + Fraction(1, p - 1) + Fraction(1, (p - 1) * p)
        k3 *= 1 + Fraction(3, p - 1) + Fraction(5, (p - 1) * p)
    return total - log_bounds(THRESHOLD)[1]


def check_lemma_3_3_cube_free(checker: Checker) -> None:
    """Part 4: no distortion schedule reaches the threshold."""
    cases = [
        ([3, 5, 7], Fraction(5, 2), False, 8643, 329),
        ([3, 5, 7, 11], Fraction(9, 4), False, 5810, 248),
        ([3, 5, 7, 11, 13], Fraction(2), False, 3302, 193),
        ([3, 5, 7, 11, 13, 17], Fraction(7, 4), False, 1536, 161),
        ([3, 5, 7], Fraction(2), True, 3028, 187),
        ([3, 5, 7, 11], Fraction(7, 4), True, 1091, 154),
    ]
    for block, lam, weighted, margin_numerator, ratio_lower in cases:
        margin = lagrangian_margin(block, lam, LAGRANGE_CELLS, weighted)
        gap_upper = log_bounds(Fraction(ratio_lower))[1] - log_bounds(THRESHOLD)[0]
        family = 'both recursions' if weighted else 'capped Lemma 3.3'
        checker.check(
            f'{family}, block {block}: log margin > {margin_numerator}/10000, '
            f'f_21 > {ratio_lower}',
            margin > Fraction(margin_numerator, 10000)
            and margin > gap_upper
            and ratio_lower > THRESHOLD,
        )


def deep_mass(p: int, t: int) -> Fraction:
    """Return the averaging floor of a depth-t shape at p on the reduced box."""
    return Fraction(1, (p - 1) * p ** (t - 1))


def deep_local(p: int, depth: int, weighted: bool) -> Fraction:
    """Return the local factor of K_1 (or of K_3 when weighted) at p."""
    return Fraction(1) + sum(
        ((2 * t + 1 if weighted else 1) * deep_mass(p, t) for t in range(1, depth + 1)),
        Fraction(0),
    )


def digit_orders(block: list[int], depth: int) -> dict[str, list[tuple[int, int]]]:
    """Return the three chain orders of the digits outside the block."""
    rest = [p for p in SMALL_PRIMES if p not in block]
    return {
        'consecutive': [(p, j) for p in rest for j in range(1, depth + 1)],
        'breadth-first': [(p, j) for j in range(1, depth + 1) for p in rest],
        'mixed': [(p, j) for p in rest for j in range(1, min(2, depth) + 1)]
        + [(p, j) for j in range(3, depth + 1) for p in rest],
    }


def deep_floor(
    block: list[int], depth: int, order: list[tuple[int, int]]
) -> tuple[Fraction, Fraction]:
    """Return kappa_0 and mu_0 at a uniform depth for a chain order.

    The block's digits are exposed from the start and lose nothing. At the
    digit (p, j) the completed classes have fixed sets Y together with the
    first j digits of p, where Y is a prefix set of the digits of the other
    primes exposed so far, nonempty when j = 1. Their projections have at
    least the averaging-floor masses, so the step's certified loss is at
    least the smaller of the floor first- and second-moment sums, using
    4 delta(1 - delta) <= 1.
    """
    exposed = {p: (depth if p in block else 0) for p in SMALL_PRIMES}
    mu = Fraction(1)
    for p, j in order:
        k1 = Fraction(1)
        k3 = Fraction(1)
        for q in SMALL_PRIMES:
            if q != p:
                k1 *= deep_local(q, exposed[q], False)
                k3 *= deep_local(q, exposed[q], True)
        if j == 1:
            mu -= min((k1 - 1) / (p - 1), (k3 - 2 * k1 + 1) / (p - 1) ** 2)
        else:
            mass = deep_mass(p, j - 1)
            mu -= min(k1 * mass / p, k3 * mass / p**2)
        exposed[p] = j
    kappa = Fraction(1)
    for q in SMALL_PRIMES:
        kappa *= deep_local(q, depth, True)
    return kappa, mu


def deep_limit_bound(block: list[int]) -> tuple[Fraction, Fraction]:
    """Return an upper bound for kappa_0 and a lower bound for mu_0 at every depth.

    Consecutive order. Every local factor is replaced by its infinite-depth
    value, which bounds all finite ones, and the losses of the digits beyond
    the first are bounded by their second-moment branch summed over all
    depths, K_3/(p(p-1)^2).
    """

    def first(q: int) -> Fraction:
        return 1 + Fraction(q, (q - 1) ** 2)

    def pairs(q: int) -> Fraction:
        return 1 + Fraction(q * (3 * q - 1), (q - 1) ** 3)

    k1 = Fraction(1)
    k3 = Fraction(1)
    for q in block:
        k1 *= first(q)
        k3 *= pairs(q)
    mu = Fraction(1)
    for p in SMALL_PRIMES:
        if p in block:
            continue
        mu -= min((k1 - 1) / (p - 1), (k3 - 2 * k1 + 1) / (p - 1) ** 2)
        mu -= k3 / (p * (p - 1) ** 2)
        k1 *= first(p)
        k3 *= pairs(p)
    kappa = Fraction(1)
    for q in SMALL_PRIMES:
        kappa *= pairs(q)
    return kappa, mu


def check_deep_digits(checker: Checker) -> None:
    """Part 5: the delta-free floor at uniform depth, in three digit orders."""
    cases = (
        ([], 0),
        ([3], 5662),
        ([3, 5], 583),
        ([3, 5, 7], 280),
        ([3, 5, 7, 11], 209),
        ([3, 5, 7, 11, 13], 167),
        ([3, 5, 7, 11, 13, 17], 146),
    )
    for block, ratio_lower in cases:
        orders = digit_orders(block, 4)
        ok = True
        for name, order in orders.items():
            kappa, mu = deep_floor(block, 4, order)
            if not block or (block == [3] and name == 'breadth-first'):
                ok = ok and mu <= 0
            elif block == [3]:
                ok = ok and mu > 0 and kappa > 5662 * mu
            else:
                ok = ok and (mu <= 0 or kappa > ratio_lower * mu)
        if not block:
            label = 'mu_0 <= 0'
        elif block == [3]:
            label = 'mu_0 <= 0 breadth-first; positive mu_0 and floor > 5662 otherwise'
        else:
            label = f'mu_0 <= 0 or floor > {ratio_lower}'
        checker.check(f'depth 4, block {block}, all three orders: {label}', ok)
    for depth, blocks in (
        (2, ([], [3], [3, 5], [3, 5, 7])),
        (3, ([3, 5, 7, 11], [3, 5, 7, 11, 13])),
    ):
        ok = True
        for block in blocks:
            for order in digit_orders(block, depth).values():
                kappa, mu = deep_floor(block, depth, order)
                ok = ok and (mu <= 0 or kappa > THRESHOLD * mu)
        checker.check(
            f'depth {depth}, blocks {list(blocks)}, all three orders: '
            'mu_0 <= 0 or floor above threshold',
            ok,
        )
    block = [3, 5, 7, 11, 13, 17]
    kappa, mu = deep_floor(block, 3, digit_orders(block, 3)['consecutive'])
    checker.check(
        'scope: depth 3, block [3, ..., 17], consecutive order: floor below threshold',
        mu > 0 and kappa < THRESHOLD * mu,
    )
    kappa, mu = deep_limit_bound([3, 5, 7, 11, 13, 17, 19])
    checker.check(
        'scope: block [3, ..., 19], consecutive order: floor < 136.74 at every depth',
        mu > 0
        and kappa < Fraction(13674, 100) * mu
        and Fraction(13674, 100) < THRESHOLD,
    )
    checker.check(
        'infinite-depth kappa_0 in (86.93, 86.94); threshold / kappa_0 in (1.597, 1.598)',
        Fraction(8693, 100) < kappa < Fraction(8694, 100)
        and Fraction(1597, 1000) * kappa < THRESHOLD < Fraction(1598, 1000) * kappa,
    )


def main() -> int:
    """Run the seven parts and return the exit status."""
    evidence_parser(__doc__, quick=False).parse_args()
    checker = Checker()
    check_calibration(checker)
    check_implementation(checker)
    check_cube_free(checker)
    check_lemma_3_3_cube_free(checker)
    check_deep_digits(checker)
    check_concentration(checker, SMALL_PRIMES)
    check_tail_density(checker, primes_upto(20000), log_bounds)
    return checker.finish()


if __name__ == '__main__':
    raise SystemExit(main())

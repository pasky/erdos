"""Certify greedy expansions of rationals as sums of distinct 1/(2^n - 1).

For the greedy-expansion sketch of Problem 257 in the parent folder. With
w_n = 1/(2^n - 1), T_n = sum_{k > n} w_k and E = T_0, the greedy expansion
of q in [0, E] selects n exactly when the residual r_{n-1} is at least w_n.
The point q passes the first N steps exactly when it lies in the level-N
cylinder [S_F, S_F + T_N] of the selected set F, S_F = sum_{k in F} w_k, and
q is outside the achievement set as soon as some F inside {1, ..., n-1} has
T_n < q - S_F < w_n (a gap at step n). The program checks ten things.

1. Census. Every reduced fraction p/Q in (0, E) with Q <= 200 is classified
   through step 1000: as a finite sum (q = S_F, confirmed in exact rationals,
   ending at a step that Lemma 9 of the sketch allows: 1, 6 or the order of 2
   modulo an odd prime factor of Q),
   as a gap at step n (confirmed in exact rationals by
   L_{n,J} + E_{n,J} < q - S_F < w_n, where L_{n,J} is the J-term partial sum
   of T_n = sum_{j >= 1} 2^{-jn}/(2^j - 1) and E_{n,J} bounds its tail), or
   as passing step 1000 (q in the level-1000 cylinder of its greedy set,
   certified by interval arithmetic, after every step at which Lemma 9 allows
   a finite representation of q to end). The counts are pinned: 41 finite sums,
   7395 gaps, every one at a step at most 12, with the pinned count at each
   step, and 12218 fractions passing.
2. Long orbits. q = 1/2 and q = 1/21 lie in the level-20000 cylinder of
   their greedy sets, every one of their first 20000 greedy decisions is
   certified, and neither expansion terminates (for 1/21 the last step at
   which Lemma 9 allows termination is 6). The program prints, for each, the
   least value of |2^n r_{n-1} - 1| over 15 <= n <= 20000 and the step where
   it occurs, with certified dyadic bounds and uniqueness of the minimizing
   step; a gap at step n needs a positive value below w_n.
3. Near misses. For the reduced fractions in (0, E) with Q <= 150 that pass
   step 400, the numbers of pairs (q, n) with 15 <= n <= 400, n > t + 2 and
   |2^n r_{n-1} - 1| < 2^{t-n} are pinned for t = 2, 4, 6, 8, 10, together
   with the numbers of distinct residuals among them (two fractions with the
   same residual at a step, decided exactly, share every later step); the
   counts expected if each 2^n r_{n-1} - 1 were uniform on [-1, 1] are printed
   beside them.
4. Periodic supports. For every M <= 10 and every nonempty residue set R mod
   M that is not periodic with a smaller period (1965 sets), the certified
   enclosure of sum_{n >= 1, n mod M in R} w_n contains no fraction with
   denominator below 2^1000.
5. Finite interfaces. The dyadic 4203/32768 first meets a gap at step 17,
   after its denominator exponent 15. For C = {1,2,3,4,6}, the two-state
   multiplier rule first proposes an invalid digit at step 108, whereas
   exact greedy for the truncated weights passes 108 using carry 3.
6. Window rule. The rule of Lemma 12 of the sketch (c_n = max(1, ceil F_n)
   with F_n = sum_{m=n+1}^{2n-1} f_m 2^{n-m}, eps_n = 2 c_{n-1} - f_n - c_n)
   gives bits through the long-orbit horizon and reproduces the certified
   greedy digits of 1/2 from check 2; at every step n >= 4 its digit equals
   the closed form floor((4k - 2 f_{2n-2} - f_{2n-1}) 2^{1-n}) of Lemma 12(b).
   With f_m restricted to the multipliers of C, it reproduces the exact
   truncated greedy digits for C = {1,2,3,4,6} and C = {1,...,8} through
   step 400, using the carries 1, 2, 3, 1 at steps 105 to 108 for the first.

7. Finite seeds. For C = (1), (1,2), (1,2,3), (1,2,3,4,6),
   (1,2,3,4,6,12), and (1,...,8), construct the exact integer seed of
   Lemma 13 at M = max(2, lcm(C)). Check its row sum, extend by four
   doubling blocks, and recompute all carries directly from the resulting
   digits, including carry 1 at each boundary and the carry-3 transition
   of check 5. Compare with exact truncated greedy through min(400, 16M).
   An altered seed is rejected. These checks run unchanged in both modes.

8. Seed repair. The two displayed seeds at M = 60 for C = {1,...,4} and
   C = {1,...,5} have the required exact row sums. Directly recomputed
   carries are positive, bounded by |C| and end at 1, but change from 2
   to 1 at position 29 on adjoining multiplier 5. Check the displayed
   three-row transition and the signed repair equation with all earlier
   divisor contributions. This refutes nonnegative carry changes as a
   general repair invariant, not Boolean seed extension. Both modes agree.

9. Multiplier sets. Every C = {1} u B with B inside {2, ..., 12} (2048
   sets) has the half seed of Lemma 13 at M = max(2, lcm(C)), and for the 1542 of
   them with M <= 2520 the extremal whole-word iteration (14) of the
   multiplier page stabilizes at that seed. For C = {1,2,3,4,6} and M = 12,
   at each of the 2048 targets t < 2^11 the iteration stabilizes either at
   the row solution or at a pair l < u (427 targets). For each such pair,
   with k its first differing position and Y the integer u truncated after
   position k, 2k <= M and u and l agree through position 2k - 1 with Y and
   Y - 1; at the 16 of these targets that have a row solution x,
   l <= x <= u and 9 |x - Y| 2^(4k) <= 16 2^M. All 427 pairs have unit
   mixed carry difference from k to 2k - 1. The 169 pairs with k >= 3
   rejoin at 2k, with ordinary carries one above and one below the common
   mixed carry, and satisfy the later forcing formulas (22)--(23).
   These different-target pairs do not test the half-target phase bound
   (17), whose terminal carry is 1. The weights
   2^-n + 4^-n + 3 8^-n, which dominate their tails, meet a gap at step 3
   for the target 1/2; multiplicities 3, 2, 1 at a = 3, 4, 5 beside the
   unit channel meet one at step 4, with mass 3/7 + 2/15 + 1/31 below
   sum_{a=2}^{8} 1/(2^a - 1); and one family of index-dependent sets B_m inside
   {2, ..., 10} for m <= 9, with pure binary weights after 9, represents
   1/2 by no support inside {2, 3, ...}. These finite checks construct no
   seed for an unbounded family. Both modes agree.

10. Full-weight doubling blocks. Along the certified greedy prefix of 1/2
   from check 2, at H = 2, 4, ..., 64 and N = 2H, the block word W of the
   digits in (H, N] satisfies s_N = 2^H s_H - W - G(W) exactly, with
   G(W) = sum_d eps_d 2^(N-d) w_d, 0 < 2^H s_H - W < 3/2, and the words
   W + 1 and W - 1 give scaled residuals below 0 and above sigma_N. For
   2 <= H <= 7 and every word W >= 1 with last one at k,
   1 + G(W) - G(W - 1) = 2^N (w_k - sum_{k < d <= N} w_d), which is
   2^N g_k + sigma_N. The selections through 32 are pinned; the old
   pending mass E_16 is 376801/344043 > 1 and the carry c_32 = 2 equals
   E_16 + G(W) + s_32. The only candidate terminal carries are computed
   from u = floor(E_H) + 1; exactly one of their words passes, and it is the
   certified word. Dyadic controls 3/8 at H = 2 and 155/256 at H = 4 test
   the two automatic word-boundary cases. The retained 4203/32768 prefix
   at H = 16 has both candidates fail. Subset enumeration at the exceptional
   renewal endpoints L = 2, 6 gives exactly the three identities of Lemma
   14. Bang--Zsigmondy and that lemma's written proof, not this check,
   exclude every other endpoint. Both modes agree. No later doubling block
   is decided.

Controls, in both modes: a non-gap must not certify as a gap, the floor and
ceiling enclosures bracket 2^P w_n, the enclosure of E meets an independent
one from sum tau(m) 2^{-m}, and the least-denominator routine agrees with a
direct search on every interval between fractions with denominator at most 10
in [0, 2]. Window classification handles endpoints and an enclosure spanning
the whole window, and closest-approach enclosures agree with exact rational
calculations for the two targets through step 40.

Arithmetic: exact rationals (fractions.Fraction) for the finite-sum and gap
certificates; elsewhere integers scaled by 2^P with floor and ceiling
enclosures, P = 2N + 64 for a run of N steps and P = 3200 in check 4. A
decision whose enclosure straddles its threshold is resolved in exact
rationals when it is an equality and otherwise fails the run; no
approximation is reported as certified.

These are finite statements. For the full Mersenne weights they prove no
membership of a rational with infinite support and no irrationality of any
sum: passing N steps leaves every later step open, and check 4 excludes only denominators below 2^1000
for the purely periodic sums. The near-miss counts are observations about a
model, not evidence for either answer.

Run from the repository root:
    uv run --no-sync python wiki/research/leads/reciprocal_mersenne_greedy/evidence/main.py

Dependencies: the Python standard library and the root ``tools`` package.
The full run takes about two minutes and well under 1 GiB of memory, most
of it in check 2.
``--quick`` reduces check 1 to Q <= 60 through step 200, check 2 and the
full-weight part of check 6 to 2000 steps, check 3 to Q <= 60, and check 4
to M <= 8, each with its own pinned counts. There are no input files and no outputs. Every check goes through the
shared ``Checker``, so failures exit nonzero under ``python -O`` as well.
"""

from __future__ import annotations

import math
import sys
from fractions import Fraction

import tools

__all__ = [
    'Run',
    'block_mass',
    'check_census',
    'check_controls',
    'check_finite_interfaces',
    'check_finite_seeds',
    'check_full_doubling',
    'check_long_orbits',
    'check_multiplier_sets',
    'check_near_misses',
    'check_periodic_supports',
    'check_seed_repair',
    'check_window_rule',
    'closest_approach',
    'double_seed',
    'finite_seed',
    'greedy',
    'same_residual',
    'main',
    'multiplicity_gap',
    'order_of_two',
    'prime_factors',
    'row_solution',
    'simplest_fraction',
    'stable_pair',
    'tail_enclosure',
    'termination_steps',
    'truncated_greedy',
    'window_rule',
    'word_spread',
]

# pinned outcomes for each mode: census counts, gap histogram, near misses
CENSUS = {
    False: {
        'qmax': 200,
        'steps': 1000,
        'finite': 41,
        'gap': 7395,
        'pass': 12218,
        'hist': {
            1: 4809,
            2: 1470,
            3: 600,
            4: 268,
            5: 132,
            6: 66,
            7: 32,
            8: 8,
            9: 6,
            12: 4,
        },
    },
    True: {
        'qmax': 60,
        'steps': 200,
        'finite': 15,
        'gap': 656,
        'pass': 1098,
        'hist': {1: 434, 2: 132, 3: 54, 4: 18, 5: 12, 6: 2, 7: 4},
    },
}
LONG_STEPS = {False: 20000, True: 2000}
# q -> (selected count, unique closest step, lower dyadic exponent)
LONG_OUTCOMES = {
    False: {2: (10028, 15999, -14), 21: (10006, 2215, -14)},
    True: {2: (980, 1135, -14), 21: (1000, 688, -13)},
}
NEAR = {False: {'qmax': 150, 'steps': 400}, True: {'qmax': 60, 'steps': 400}}
NEAR_COUNTS = {
    False: (
        6830,
        {2: 2, 4: 10, 6: 22, 8: 120, 10: 438},
        {2: 1, 4: 3, 6: 9, 8: 36, 10: 139},
    ),
    True: (1098, {2: 0, 4: 0, 6: 0, 8: 30, 10: 90}, {2: 0, 4: 0, 6: 0, 8: 6, 10: 27}),
}
THRESHOLDS = (2, 4, 6, 8, 10)
PERIODIC = {False: {'mmax': 10, 'sets': 1965}, True: {'mmax': 8, 'sets': 471}}
PERIODIC_PRECISION = 3200
DENOMINATOR_BITS = 1000
WINDOW_TRUNCATED_STEPS = 400


def tail_enclosure(n: int, terms: int) -> tuple[Fraction, Fraction]:
    """Return exact rationals L <= T_n <= L + E from the first ``terms`` terms."""
    # partial sum of T_n = sum_j 2^{-jn}/(2^j - 1) and the geometric tail bound
    low = sum(Fraction(1, ((1 << j) - 1) << (j * n)) for j in range(1, terms + 1))
    tail = Fraction(2, 1 << ((n + 1) * (terms + 1))) / (1 - Fraction(1, 1 << (n + 1)))
    return low, low + tail


def scaled_w(precision: int, n: int) -> tuple[int, int]:
    """Return floor and ceiling of 2^precision / (2^n - 1)."""
    # one integer division gives both ends of the enclosure
    d = (1 << n) - 1
    low = (1 << precision) // d
    return low, low if low * d == 1 << precision else low + 1


def scaled_e(precision: int) -> tuple[int, int]:
    """Return integers enclosing 2^precision * E."""
    # sum the first K = precision terms and bound the rest by 2^{1-K}
    low = high = 0
    for k in range(1, precision + 1):
        lo_k, hi_k = scaled_w(precision, k)
        low += lo_k
        high += hi_k
    return low, high + 2


class Run:
    """Outcome of a certified greedy run on one rational."""

    def __init__(self: Run, status: str, step: int, chosen: list[int]) -> None:
        """Record the status, the step where it was decided and the selected set."""
        # status is 'finite', 'gap', 'pass' or 'undecided'
        self.status = status
        self.step = step
        self.chosen = chosen


def greedy(
    q: Fraction,
    steps: int,
    e_scaled: tuple[int, int],
    precision: int,
    track: tuple[int, int] | None = None,
) -> tuple[Run, list[tuple[int, int, int]]]:
    """Run the certified greedy expansion of ``q`` for ``steps`` steps.

    Returns the run and, when ``track`` = (first, last) is given, the scaled
    enclosures (n, low, high) of 2^precision r_{n-1} for first <= n <= last.
    """
    # residual and tail enclosures, both scaled by 2^precision
    scale = 1 << precision
    r_low = (q.numerator * scale) // q.denominator
    r_high = -((-q.numerator * scale) // q.denominator)
    t_low, t_high = e_scaled
    chosen: list[int] = []
    tracked: list[tuple[int, int, int]] = []
    for n in range(1, steps + 1):
        if track is not None and track[0] <= n <= track[1]:
            tracked.append((n, r_low, r_high))
        w_low, w_high = scaled_w(precision, n)
        t_low, t_high = t_low - w_high, t_high - w_low
        if r_low >= w_high:
            # certified selection; a residual enclosure touching 0 may be exactly 0
            chosen.append(n)
            r_low, r_high = r_low - w_high, r_high - w_low
            if r_low == 0 and q == sum(Fraction(1, (1 << k) - 1) for k in chosen):
                return Run('finite', n, chosen), tracked
        elif r_high < w_low:
            # certified skip; the residual must not exceed T_n
            if r_high <= t_low:
                continue
            if r_low > t_high:
                return Run('gap', n, chosen), tracked
            return Run('undecided', n, chosen), tracked
        else:
            # straddle: only an exact equality r_{n-1} = w_n is acceptable
            residual = q - sum(Fraction(1, (1 << k) - 1) for k in chosen)
            if residual == Fraction(1, (1 << n) - 1):
                chosen.append(n)
                return Run('finite', n, chosen), tracked
            return Run('undecided', n, chosen), tracked
    return Run('pass', steps, chosen), tracked


def gap_certified(q: Fraction, run: Run) -> bool:
    """Confirm a gap in exact rationals: L + E < q - S_F < w_n for some J."""
    # the selected set below the gap step and the exact residual
    n = run.step
    residual = q - sum(Fraction(1, (1 << k) - 1) for k in run.chosen)
    if not residual < Fraction(1, (1 << n) - 1):
        return False
    for terms in range(1, 65):
        _, upper = tail_enclosure(n, terms)
        if upper < residual:
            return True
    return False


def cylinder_certified(
    q: Fraction, run: Run, precision: int, e_scaled: tuple[int, int]
) -> bool:
    """Certify 0 <= q - S_F <= T_N for the selected set F of a passing run."""
    # recompute S_F and T_N enclosures independently of the stepping loop
    scale = 1 << precision
    s_low = s_high = 0
    for k in run.chosen:
        lo_k, hi_k = scaled_w(precision, k)
        s_low += lo_k
        s_high += hi_k
    t_low, t_high = e_scaled
    for k in range(1, run.step + 1):
        lo_k, hi_k = scaled_w(precision, k)
        t_low -= hi_k
        t_high -= lo_k
    q_low = (q.numerator * scale) // q.denominator
    q_high = -((-q.numerator * scale) // q.denominator)
    return q_low - s_high >= 0 and q_high - s_low <= t_low


def reduced_fractions(
    q_max: int, e_scaled: tuple[int, int], precision: int
) -> list[Fraction]:
    """List the reduced p/Q with Q <= q_max in (0, E), certified against E."""
    # the comparison with E is certified by its enclosure
    scale = 1 << precision
    out = []
    for den in range(1, q_max + 1):
        for num in range(1, 2 * den):
            if math.gcd(num, den) != 1:
                continue
            if -((-num * scale) // den) < e_scaled[0]:
                out.append(Fraction(num, den))
            elif (num * scale) // den <= e_scaled[1]:
                raise ValueError('fraction too close to E to classify')
    return out


def prime_factors(n: int) -> list[int]:
    """Return the distinct prime factors of ``n`` by trial division."""
    # strip each prime factor completely before moving on
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def order_of_two(p: int) -> int:
    """Return the multiplicative order of 2 modulo the odd prime ``p``."""
    # repeated doubling modulo p until the residue returns to 1
    k, x = 1, 2 % p
    while x != 1:
        x = 2 * x % p
        k += 1
    return k


def termination_steps(den: int) -> set[int]:
    """Return the steps where a finite representation of a fraction can end (Lemma 9)."""
    # the Bang-Zsigmondy exceptions and the orders of 2 at the odd primes of den
    return {1, 6} | {order_of_two(p) for p in prime_factors(den) if p != 2}


def check_census(checker: tools.Checker, quick: bool) -> None:
    """Check 1: classify the reduced fractions with small denominators."""
    # one precision serves the whole census
    spec = CENSUS[quick]
    steps = spec['steps']
    precision = 2 * steps + 64
    e_scaled = scaled_e(precision)
    fractions = reduced_fractions(spec['qmax'], e_scaled, precision)
    counts = {'finite': 0, 'gap': 0, 'pass': 0, 'undecided': 0}
    hist: dict[int, int] = {}
    bad: list[str] = []
    early: list[str] = []
    for q in fractions:
        run, _ = greedy(q, steps, e_scaled, precision)
        counts[run.status] += 1
        if run.status == 'finite':
            if q != sum(Fraction(1, (1 << k) - 1) for k in run.chosen):
                bad.append(str(q))
            if run.step not in termination_steps(q.denominator):
                early.append(str(q))
        elif run.status == 'gap':
            hist[run.step] = hist.get(run.step, 0) + 1
            if not gap_certified(q, run):
                bad.append(str(q))
        elif run.status == 'pass':
            # passing beyond every allowed termination step rules out a finite sum
            if max(termination_steps(q.denominator)) >= steps:
                early.append(str(q))
            if not cylinder_certified(q, run, precision, e_scaled):
                bad.append(str(q))
        else:
            bad.append(str(q))
    print(
        f'  census Q <= {spec["qmax"]}, {steps} steps: {len(fractions)} fractions, '
        f'{counts["finite"]} finite sums, {counts["gap"]} gaps, {counts["pass"]} passing'
    )
    print(f'  gap steps: {dict(sorted(hist.items()))}')
    checker.check(
        'census: every classification certified',
        not bad and counts['undecided'] == 0,
        'uncertified: ' + ', '.join(bad[:10]),
    )
    checker.check(
        'census: finite subsums end at Lemma 9 steps; passing runs are past them',
        not early,
        'outside Lemma 9: ' + ', '.join(early[:10]),
    )
    if spec['finite'] is not None:
        checker.check(
            'census: pinned counts',
            (counts['finite'], counts['gap'], counts['pass'])
            == (spec['finite'], spec['gap'], spec['pass']),
            str(counts),
        )
        checker.check('census: pinned gap steps', hist == spec['hist'], str(hist))
    # independent of the pins: no gap after step 12 in the census
    checker.check(
        'census: every gap at a step at most 12', all(n <= 12 for n in hist), str(hist)
    )
    # witness rows: 1/2 passes, 1/3 is the finite sum w_2, 2/3 meets the first gap
    checker.check(
        'census: witness 1 = w_1 is a finite sum',
        greedy(Fraction(1), steps, e_scaled, precision)[0].status == 'finite',
    )
    checker.check(
        'census: witness 1/3 = w_2 is a finite sum',
        greedy(Fraction(1, 3), steps, e_scaled, precision)[0].status == 'finite',
    )
    checker.check(
        'census: witness Lemma 9 allows 1/21 to end only at steps 1, 2, 3, 6',
        termination_steps(21) == {1, 2, 3, 6},
    )
    gap_run, _ = greedy(Fraction(2, 3), steps, e_scaled, precision)
    checker.check(
        'census: witness 2/3 meets a gap at step 1',
        gap_run.status == 'gap' and gap_run.step == 1,
    )


def closest_approach(
    q: Fraction, chosen: list[int], first: int, last: int, precision: int
) -> tuple[int, int, int, bool]:
    """Enclose the least distance, scaled by 2^precision; certify its unique step.

    Return (step, low, high, isolated). If isolated is false, the proposed
    minimizing step is not certified and the caller must reject it.
    """
    # compare integer enclosures at one common scale, without floating-point decisions
    scale = 1 << precision
    r_low = (q.numerator * scale) // q.denominator
    r_high = -((-q.numerator * scale) // q.denominator)
    members = set(chosen)
    best_step, best_low, best_high = 0, 0, None
    other_low = None
    for n in range(1, last + 1):
        if n >= first:
            a, b = (r_low << n) - scale, (r_high << n) - scale
            low, high = max(0, a, -b), max(abs(a), abs(b))
            if best_high is None or high < best_high:
                if best_high is not None:
                    other_low = (
                        best_low if other_low is None else min(other_low, best_low)
                    )
                best_step, best_low, best_high = n, low, high
            else:
                other_low = low if other_low is None else min(other_low, low)
        if n in members:
            w_low, w_high = scaled_w(precision, n)
            r_low -= w_high
            r_high -= w_low
    if best_high is None:
        raise ValueError('empty closest-approach range')
    isolated = other_low is None or best_high < other_low
    return best_step, best_low, best_high, isolated


def check_long_orbits(checker: tools.Checker, quick: bool) -> dict[int, list[int]]:
    """Check 2: 1/2 and 1/21 pass the first N greedy steps.

    Returns the certified selected sets, keyed by denominator, for check 6.
    """
    # one precision and one E enclosure for both rationals
    steps = LONG_STEPS[quick]
    precision = 2 * steps + 64
    e_scaled = scaled_e(precision)
    selected: dict[int, list[int]] = {}
    for q in (Fraction(1, 2), Fraction(1, 21)):
        run, _ = greedy(q, steps, e_scaled, precision)
        selected[q.denominator] = run.chosen
        ok = (
            run.status == 'pass'
            and max(termination_steps(q.denominator)) < steps
            and cylinder_certified(q, run, precision, e_scaled)
        )
        step, low, high, isolated = closest_approach(
            q, run.chosen, 15, steps, precision
        )
        expected_count, expected_step, exponent = LONG_OUTCOMES[quick][q.denominator]
        bounded = (
            (1 << (precision + exponent))
            < low
            <= high
            < (1 << (precision + exponent + 1))
        )
        # The decimal logarithm is a display approximation, not a branch of a check.
        shift = max(0, low.bit_length() - 53)
        log_value = (
            math.log2(low >> shift) + shift - precision if low > 0 else -math.inf
        )
        print(
            f'  {q}: {run.status} through step {run.step}, {len(run.chosen)} selected; '
            f'least |2^n r_(n-1) - 1| over 15 <= n <= {steps} is approximately '
            f'2^{log_value:.1f} at n = {step}; bounds 2^{exponent} and 2^{exponent + 1}'
        )
        checker.check(
            f'long orbit: {q} lies in its level-{steps} cylinder',
            ok,
            f'{run.status} at step {run.step}',
        )
        checker.check(
            f'long orbit: {q} selected count, unique closest step and dyadic bounds',
            len(run.chosen) == expected_count
            and step == expected_step
            and isolated
            and bounded,
        )
    return selected


def same_residual(
    first: tuple[Fraction, tuple[int, ...]], second: tuple[Fraction, tuple[int, ...]]
) -> bool:
    """Decide exactly whether q - S_F = q' - S_F' from the symmetric difference."""
    # only the elements of F and F' outside their intersection enter the test
    (q, f), (q2, f2) = first, second
    a, b = set(f), set(f2)
    diff = sum(Fraction(1, (1 << k) - 1) for k in a - b) - sum(
        Fraction(1, (1 << k) - 1) for k in b - a
    )
    return q - q2 == diff


def classify_window(low: int, high: int, bound: int) -> str:
    """Classify [low, high] against (-bound, bound), refusing a partial overlap."""
    # Testing both endpoints for nonmembership would miss a window-spanning interval.
    if low > high or bound <= 0:
        raise ValueError('invalid interval or bound')
    if -bound < low and high < bound:
        return 'inside'
    if high <= -bound or low >= bound:
        return 'outside'
    return 'undecided'


def check_near_misses(checker: tools.Checker, quick: bool) -> None:
    """Check 3: count near misses of the gap windows among passing fractions."""
    # near miss at step n: |2^{2n} r_{n-1} - 2^n| < 2^t, certified by enclosure
    spec = NEAR[quick]
    steps = spec['steps']
    precision = 2 * steps + 64
    e_scaled = scaled_e(precision)
    counts = dict.fromkeys(THRESHOLDS, 0)
    events: dict[int, list[tuple[int, int, int, Fraction, tuple[int, ...]]]] = {}
    uncertified = 0
    passing = 0
    for q in reduced_fractions(spec['qmax'], e_scaled, precision):
        run, tracked = greedy(q, steps, e_scaled, precision, track=(15, steps))
        if run.status != 'pass':
            continue
        passing += 1
        for n, low, high in tracked:
            a = (low << (2 * n)) - (1 << (precision + n))
            b = (high << (2 * n)) - (1 << (precision + n))
            least = None
            for t in THRESHOLDS:
                if n <= t + 2:
                    continue
                bound = 1 << (precision + t)
                position = classify_window(a, b, bound)
                if position == 'undecided':
                    uncertified += 1
                elif position == 'inside':
                    counts[t] += 1
                    least = t if least is None else least
            if least is not None:
                prefix = tuple(k for k in run.chosen if k < n)
                events.setdefault(n, []).append((least, low, high, q, prefix))
    # events at one step with equal exact residuals share their whole future
    distinct = dict.fromkeys(THRESHOLDS, 0)
    for rows in events.values():
        rows.sort(key=lambda row: row[1])
        classes: list[tuple[int, int, int, Fraction, tuple[int, ...]]] = []
        for row in rows:
            if (
                classes
                and row[1] <= classes[-1][2]
                and same_residual((classes[-1][3], classes[-1][4]), (row[3], row[4]))
            ):
                continue
            if classes and row[1] <= classes[-1][2]:
                uncertified += 1
            classes.append(row)
        for row in classes:
            for t in THRESHOLDS:
                if t >= row[0]:
                    distinct[t] += 1
    expected = {
        t: passing * sum(2.0 ** (t - n) for n in range(max(15, t + 3), steps + 1))
        for t in THRESHOLDS
    }
    print(
        f'  near misses among {passing} passing fractions (Q <= {spec["qmax"]}, '
        f'{steps} steps):'
    )
    for t in THRESHOLDS:
        print(
            f'    t = {t:2d}: {counts[t]:4d} observed ({distinct[t]:4d} distinct residuals), '
            f'{expected[t]:7.1f} uniform-model expectation'
        )
    checker.check(
        'near misses: every comparison certified', uncertified == 0, str(uncertified)
    )
    pinned = NEAR_COUNTS[quick]
    if pinned is not None:
        checker.check(
            'near misses: pinned counts',
            (passing, counts, distinct) == pinned,
            str((passing, counts, distinct)),
        )


def simplest_fraction(
    low_num: int, low_den: int, high_num: int, high_den: int
) -> tuple[int, int]:
    """Return the fraction of least denominator in [low, high], 0 <= low <= high."""
    # continued-fraction descent; the floors are folded back at the end
    floors: list[int] = []
    a, b, c, d = low_num, low_den, high_num, high_den
    while True:
        f = a // b
        if f * b == a:
            last = f
            break
        if (f + 1) * d <= c:
            last = f + 1
            break
        floors.append(f)
        # both ends lie in (f, f + 1): pass to the reciprocals of the remainders
        a, b, c, d = d, c - f * d, b, a - f * b
    num, den = last, 1
    for f in reversed(floors):
        num, den = f * num + den, num
    return num, den


def check_periodic_supports(checker: tools.Checker, quick: bool) -> None:
    """Check 4: nonempty periodic supports have no rational sum of small denominator."""
    # enclosures of every w_n at the fixed precision, and the tail bound
    spec = PERIODIC[quick]
    precision = PERIODIC_PRECISION
    w = [None] + [scaled_w(precision, n) for n in range(1, precision + 1)]
    tail = 2  # 2^precision times the tail bound 2^{1 - precision}
    tested = 0
    small = []
    invalid = []
    for m in range(1, spec['mmax'] + 1):
        for mask in range(1, 1 << m):
            residues = {r for r in range(m) if mask >> r & 1}
            # skip residue sets periodic with a smaller period dividing m
            if any(
                m % e == 0 and all((r + e) % m in residues for r in residues)
                for e in range(1, m)
            ):
                continue
            tested += 1
            low = sum(w[n][0] for n in range(1, precision + 1) if n % m in residues)
            high = (
                sum(w[n][1] for n in range(1, precision + 1) if n % m in residues)
                + tail
            )
            num, den = simplest_fraction(low, 1 << precision, high, 1 << precision)
            if not (
                low * den <= num * (1 << precision) <= high * den
                and math.gcd(num, den) == 1
            ):
                invalid.append((m, sorted(residues)))
            if den.bit_length() <= DENOMINATOR_BITS:
                small.append((m, sorted(residues), den))
    print(
        f'  periodic supports with M <= {spec["mmax"]}: {tested} residue sets, '
        f'{len(small)} with a fraction of denominator below 2^{DENOMINATOR_BITS} '
        f'in the enclosure'
    )
    checker.check(
        'periodic supports: no small-denominator fraction in any enclosure',
        not small,
        str(small[:5]),
    )
    checker.check(
        'periodic supports: returned reduced fractions lie inside their enclosures',
        not invalid,
        str(invalid[:5]),
    )
    if spec['sets'] is not None:
        checker.check(
            'periodic supports: pinned number of residue sets',
            tested == spec['sets'],
            str(tested),
        )
    # control: the simplest-fraction routine finds 1/3 inside a tiny interval around it
    third = (1 << precision) // 3
    checker.check(
        'periodic supports: control finds 1/3',
        simplest_fraction(third, 1 << precision, third + 1, 1 << precision) == (1, 3),
    )


def check_finite_interfaces(checker: tools.Checker) -> None:
    """Check 5: an exact dyadic gap and the boundary of the two-state carry rule."""
    # The general dyadic-denominator cutoff fails for this explicit target.
    q = Fraction(4203, 32768)
    chosen = [4, 5, 6, 7, 8, 10, 11, 13, 14, 16]
    precision = 2 * 17 + 64
    run, _ = greedy(q, 17, scaled_e(precision), precision)
    residual = q - sum(Fraction(1, (1 << n) - 1) for n in chosen)
    _, tail_upper = tail_enclosure(17, 2)
    checker.check(
        'finite interfaces: dyadic witness first meets a gap at step 17',
        run.status == 'gap' and run.step == 17 and run.chosen == chosen,
    )
    checker.check(
        'finite interfaces: dyadic gap has an exact two-term tail certificate',
        tail_upper < residual < Fraction(1, (1 << 17) - 1),
    )

    # Apply the displayed two-state rule without assuming its hypothesis |B| <= 3.
    # Every forecast at stage n uses indices m/a < n, since m < 2n and a >= 2.
    multipliers = (1, 2, 3, 4, 6)
    steps = 108
    proposed = [0] * (steps + 1)
    carry = 1
    failure = None
    for n in range(2, steps + 1):
        forcing = {
            m: sum(proposed[m // a] for a in multipliers[1:] if m % a == 0)
            for m in range(n, 2 * n)
        }
        next_value = next(
            (forcing[m] for m in range(n + 1, 2 * n) if forcing[m] != 1),
            None,
        )
        if next_value is None:
            break
        next_carry = 1 + int(next_value >= 2)
        digit = 2 * carry - next_carry - forcing[n]
        if digit not in (0, 1):
            failure = (n, forcing[n], carry, next_carry, digit)
            break
        proposed[n] = digit
        carry = next_carry
    checker.check(
        'finite interfaces: two-state extension first fails at step 108',
        failure == (108, 4, 2, 1, -1),
        str(failure),
    )

    # All truncated weights through steps are exact integers at this scale.
    # The tail has small odd denominators, so every cylinder comparison is exact.
    precision = max(multipliers) * steps
    residual_scaled = 1 << (precision - 1)
    digits = [0] * (steps + 1)
    carry = 1
    passed = True
    trace = []
    for n in range(2, steps + 1):
        weight = sum(1 << (precision - a * n) for a in multipliers)
        digits[n] = int(residual_scaled >= weight)
        residual_scaled -= digits[n] * weight
        tail = sum(
            Fraction(1 << (precision - a * n), (1 << a) - 1) for a in multipliers
        )
        passed &= 0 < residual_scaled <= tail
        forcing_n = sum(digits[n // a] for a in multipliers[1:] if n % a == 0)
        next_carry = 2 * carry - forcing_n - digits[n]
        if n >= 106:
            trace.append((n, forcing_n, carry, digits[n], next_carry))
        carry = next_carry
    checker.check(
        'finite interfaces: actual truncated greedy passes 108 and uses carry 3',
        passed and trace == [(106, 0, 1, 0, 2), (107, 0, 2, 1, 3), (108, 4, 3, 1, 1)],
        str(trace),
    )
    checker.check(
        'finite interfaces: the two prefixes first differ at step 106',
        next((n for n in range(2, steps) if digits[n] != proposed[n]), None) == 106,
    )


def window_rule(
    steps: int, multipliers: tuple[int, ...] | None = None
) -> tuple[list[int], list[int], bool, int | None]:
    """Run the window rule of Lemma 12 of the sketch for the target 1/2.

    ``multipliers`` None means the full weights; otherwise the demand f_m
    counts only the multipliers a >= 2 of the given set. Returns the digits,
    the carries, whether the closed form of Lemma 12(b) matched the digit at
    every step n >= 4, and the first step whose digit is not a bit (None if
    there is none).
    """
    # demands at positions below 2n depend only on digits below n
    size = 2 * steps + 2
    demand = [0] * (size + 1)
    digits = [0] * (steps + 1)
    carries = [0] * (steps + 1)
    carries[1] = 1
    closed_form = True
    previous = 0
    for n in range(2, steps + 1):
        # window = 2^(n-1) F_n over the positions n+1, ..., 2n-1
        if n <= 3:
            window = sum(demand[m] << (2 * n - 1 - m) for m in range(n + 1, 2 * n))
        else:
            window = (
                4 * (previous - (demand[n] << (n - 3)))
                + 2 * demand[2 * n - 2]
                + demand[2 * n - 1]
            )
        carry = max(1, -((-window) >> (n - 1)))
        digit = 2 * carries[n - 1] - demand[n] - carry
        if n >= 4:
            # previous = 2^(n-2) F_{n-1}; k is its distance up to a multiple of 2^(n-2)
            k = (-previous) % (1 << (n - 2))
            entering = 2 * demand[2 * n - 2] + demand[2 * n - 1]
            closed_form &= (4 * k - entering) >> (n - 1) == digit
        if digit not in (0, 1):
            return digits, carries, closed_form, n
        digits[n] = digit
        carries[n] = carry
        if digit:
            if multipliers is None:
                for m in range(2 * n, size + 1, n):
                    demand[m] += 1
            else:
                for a in multipliers[1:]:
                    if a * n <= size:
                        demand[a * n] += 1
        previous = window
    return digits, carries, closed_form, None


def truncated_greedy(
    multipliers: tuple[int, ...], steps: int
) -> tuple[list[int], bool]:
    """Return exact greedy digits on indices n >= 2 for sum_{a in C} 2^(-an).

    The flag records that every residual lies in its cylinder (0, U_n], so no
    step through ``steps`` is a gap.
    """
    # all weights through steps are exact integers at this scale
    precision = max(multipliers) * steps
    residual = 1 << (precision - 1)
    digits = [0] * (steps + 1)
    inside = True
    for n in range(2, steps + 1):
        weight = sum(1 << (precision - a * n) for a in multipliers)
        digits[n] = int(residual >= weight)
        residual -= digits[n] * weight
        tail = sum(
            Fraction(1 << (precision - a * n), (1 << a) - 1) for a in multipliers
        )
        inside &= 0 < residual <= tail
    return digits, inside


def check_window_rule(
    checker: tools.Checker, quick: bool, half_selected: list[int]
) -> None:
    """Check 6: the window rule of Lemma 12 against certified greedy digits."""
    # full weights through the long-orbit horizon of check 2
    steps = LONG_STEPS[quick]
    digits, _, closed_form, failure = window_rule(steps)
    checker.check(
        f'window rule: full-weight digits are bits through step {steps}',
        failure is None,
        str(failure),
    )
    checker.check('window rule: closed form of Lemma 12(b) at every step', closed_form)
    checker.check(
        f'window rule: reproduces the certified greedy digits of 1/2 through step {steps}',
        [n for n in range(2, steps + 1) if digits[n]] == half_selected,
    )

    # truncated weights, including the carry-3 case of check 5
    for multipliers in ((1, 2, 3, 4, 6), tuple(range(1, 9))):
        digits, _, _, failure = window_rule(WINDOW_TRUNCATED_STEPS, multipliers)
        reference, inside = truncated_greedy(multipliers, WINDOW_TRUNCATED_STEPS)
        checker.check(
            f'window rule: C = {multipliers} reproduces the truncated greedy digits '
            f'through step {WINDOW_TRUNCATED_STEPS}',
            failure is None and inside and digits[2:] == reference[2:],
            str(failure),
        )
    _, carries, _, _ = window_rule(108, (1, 2, 3, 4, 6))
    checker.check(
        'window rule: C = (1, 2, 3, 4, 6) uses carries 1, 2, 3, 1 at steps 105 to 108',
        carries[105:109] == [1, 2, 3, 1],
        str(carries[105:109]),
    )


def finite_seed(multipliers: tuple[int, ...], boundary: int) -> list[int] | None:
    """Decide the finite integer seed equation of Lemma 13 by decreasing greedy."""
    if (
        boundary < 2
        or not multipliers
        or multipliers[0] != 1
        or tuple(sorted(set(multipliers))) != multipliers
        or any(boundary % a for a in multipliers)
    ):
        raise ValueError('boundary must be a common multiple, at least two')
    remainder = (1 << (boundary - 1)) - 1
    digits = [0] * (boundary + 1)
    for d in range(2, boundary + 1):
        weight = sum(1 << (boundary - a * d) for a in multipliers if a * d <= boundary)
        if remainder >= weight:
            digits[d] = 1
            remainder -= weight
    return digits if remainder == 0 else None


def double_seed(
    multipliers: tuple[int, ...], seed: list[int], blocks: int
) -> list[int]:
    """Extend a valid seed by the backward recurrence on doubling blocks."""
    boundary = len(seed) - 1
    if finite_seed(multipliers, boundary) != seed:
        raise ValueError('the supplied digits do not solve the seed equation')
    digits = seed.copy()
    for _ in range(blocks):
        first = len(digits) - 1
        forcing = [
            sum(digits[m // a] for a in multipliers[1:] if m % a == 0)
            for m in range(first + 1, 2 * first + 1)
        ]
        digits.extend([0] * first)
        carry = 1
        for m in range(2 * first, first, -1):
            demand = forcing[m - first - 1]
            previous = (demand + carry + 1) // 2
            digits[m] = 2 * previous - demand - carry
            carry = previous
        if carry != 1:
            raise ArithmeticError('the new block does not join the seed')
    return digits


def check_finite_seeds(checker: tools.Checker) -> None:
    """Check 7: finite seed equations and four exact doubling extensions."""
    cases = (
        ((1,), 1),
        ((1, 2), 1),
        ((1, 2, 3), 3),
        ((1, 2, 3, 4, 6), 5),
        ((1, 2, 3, 4, 6, 12), 5),
        (tuple(range(1, 9)), 411),
    )
    for multipliers, count in cases:
        boundary = max(2, math.lcm(*multipliers))
        seed = finite_seed(multipliers, boundary)
        if seed is None:
            checker.check(f'finite seed: C = {multipliers} has a seed', False)
            continue
        # Recompute the row sum and carries, without the constructor's forcing cache.
        row_sum = sum(
            1 << (boundary - a * d)
            for d in range(2, boundary + 1)
            if seed[d]
            for a in multipliers
            if a * d <= boundary
        )
        checker.check(
            f'finite seed: C = {multipliers}, M = {boundary}, exact row and size {count}',
            row_sum == (1 << (boundary - 1)) - 1 and sum(seed) == count,
        )
        digits = double_seed(multipliers, seed, 4)
        last = len(digits) - 1
        carries = [0, 1]
        valid = True
        for n in range(2, last + 1):
            coefficient = sum(digits[n // a] for a in multipliers if n % a == 0)
            carries.append(2 * carries[-1] - coefficient)
            bound = len(multipliers) if n <= boundary else max(1, len(multipliers) - 1)
            valid &= digits[n] in (0, 1) and 1 <= carries[n] <= bound
        checker.check(
            f'finite seed: C = {multipliers}, all divisor contributions through {last}',
            valid and all(carries[boundary << j] == 1 for j in range(5)),
        )
        horizon = min(WINDOW_TRUNCATED_STEPS, last)
        reference, inside = truncated_greedy(multipliers, horizon)
        checker.check(
            f'finite seed: C = {multipliers}, agrees with exact greedy through {horizon}',
            inside and digits[: horizon + 1] == reference,
        )
        if multipliers == (1, 2, 3, 4, 6):
            checker.check(
                'finite seed: stated M = 12 seed and the carry-3 transition',
                [d for d in range(2, boundary + 1) if seed[d]] == [2, 3, 6, 7, 10]
                and carries[105:109] == [1, 2, 3, 1],
            )
    altered = [0, 0, 0]
    rejected = False
    try:
        double_seed((1, 2), altered, 1)
    except ValueError:
        rejected = True
    checker.check('finite seed: an altered seed is rejected', rejected)


def check_seed_repair(checker: tools.Checker) -> None:
    """Check 8: exact seeds with a negative change of carry on adjoining 5."""
    supports = {
        4: {
            2,
            3,
            6,
            7,
            10,
            12,
            13,
            15,
            16,
            17,
            19,
            22,
            24,
            25,
            27,
            30,
            31,
            33,
            35,
            37,
            41,
            42,
            43,
            46,
            49,
            53,
            55,
            56,
            58,
            60,
        },
        5: {
            2,
            3,
            6,
            7,
            12,
            13,
            16,
            17,
            19,
            20,
            22,
            24,
            25,
            27,
            29,
            31,
            33,
            37,
            41,
            42,
            43,
            45,
            46,
            49,
            53,
            55,
            56,
            60,
        },
    }
    boundary = 60
    digits = {}
    forcing = {}
    carries = {}
    for j, support in supports.items():
        # Validate the displayed witnesses directly, without seed discovery.
        row = sum(
            1 << (boundary - a * n)
            for n in support
            for a in range(1, j + 1)
            if a * n <= boundary
        )
        checker.check(
            f'seed repair: displayed C_{j} witness at M = 60',
            all(2 <= n <= boundary for n in support)
            and row == (1 << (boundary - 1)) - 1,
        )
        digits[j] = [int(n in support) for n in range(boundary + 1)]
        forcing[j] = [0] * (boundary + 1)
        carries[j] = [0, 1]
        for n in range(2, boundary + 1):
            forcing[j][n] = sum(
                digits[j][n // a] for a in range(2, j + 1) if n % a == 0
            )
            carries[j].append(2 * carries[j][-1] - digits[j][n] - forcing[j][n])
    checker.check(
        'seed repair: positive bounded finite carries and terminal carry 1',
        all(
            all(1 <= c <= j for c in carries[j][1:]) and carries[j][-1] == 1
            for j in (4, 5)
        ),
    )
    actual = [
        (
            n,
            digits[4][n],
            digits[5][n],
            carries[4][n],
            carries[5][n],
            forcing[4][n],
            forcing[5][n],
        )
        for n in (28, 29, 30)
    ]
    checker.check(
        'seed repair: displayed transition with c_29 = 2 and new c_29 = 1',
        actual
        == [(28, 0, 0, 1, 1, 1, 1), (29, 0, 1, 2, 1, 0, 0), (30, 1, 0, 1, 1, 2, 1)],
        str(actual),
    )
    delta = [digits[5][n] - digits[4][n] for n in range(boundary + 1)]
    z = [carries[5][n] - carries[4][n] for n in range(boundary + 1)]
    repair_row = sum(
        delta[n]
        * sum(1 << (boundary - a * n) for a in range(1, 6) if a * n <= boundary)
        for n in range(2, boundary + 1)
    )
    added_row = sum(
        digits[4][n] * (1 << (boundary - 5 * n)) for n in range(2, boundary // 5 + 1)
    )
    checker.check(
        'seed repair: signed equation retains every divisor contribution',
        z[1] == z[boundary] == 0
        and repair_row == -added_row
        and all(
            delta[n]
            + sum(delta[n // a] for a in range(2, 5) if n % a == 0)
            + (digits[5][n // 5] if n % 5 == 0 else 0)
            == 2 * z[n - 1] - z[n]
            for n in range(2, boundary + 1)
        ),
    )


def word_spread(multipliers: tuple[int, ...], boundary: int, x: int) -> int:
    """Return H_C(x): every digit d of x moved to positions a*d, a in C minus 1."""
    word = format(x, f'0{boundary}b')
    total = 0
    for a in multipliers[1:]:
        chars = ['0'] * boundary
        for d in range(2, boundary // a + 1):
            if word[d - 1] == '1':
                chars[a * d - 1] = '1'
        total += int(''.join(chars), 2)
    return total


def stable_pair(
    multipliers: tuple[int, ...], boundary: int, target: int
) -> tuple[int, int]:
    """Iterate the extremal bounds (14) of the whole-word map until they repeat."""
    low, high = 0, target
    while True:
        pair = (
            target - word_spread(multipliers, boundary, high),
            target - word_spread(multipliers, boundary, low),
        )
        if pair == (low, high):
            return pair
        low, high = pair


def row_solution(
    multipliers: tuple[int, ...], boundary: int, target: int
) -> int | None:
    """Return the unique x with x + H_C(x) = target, by decreasing greedy, or None."""
    remainder, x = target, 0
    for d in range(2, boundary + 1):
        weight = sum(1 << (boundary - a * d) for a in multipliers if a * d <= boundary)
        if remainder >= weight:
            remainder -= weight
            x |= 1 << (boundary - d)
    return x if remainder == 0 else None


def multiplicity_gap(
    multiplicity: dict[int, int], steps: int
) -> tuple[int, list[int]] | None:
    """First gap of the half target for v_n = sum_a lambda_a 2^{-an}, exactly.

    Each weight must strictly exceed its tail, so the greedy decisions are
    forced; the selected prefix before the gap is returned with its step.
    """

    def weight(n: int) -> Fraction:
        return sum(
            (Fraction(m, 1 << a * n) for a, m in multiplicity.items()), Fraction(0)
        )

    def tail(n: int) -> Fraction:
        return sum(
            (Fraction(m, ((1 << a) - 1) << a * n) for a, m in multiplicity.items()),
            Fraction(0),
        )

    residual = Fraction(1, 2)
    chosen = []
    for n in range(1, steps + 1):
        if not weight(n) > tail(n):
            raise ArithmeticError('a weight does not dominate its tail')
        if residual >= weight(n):
            residual -= weight(n)
            chosen.append(n)
        elif residual > tail(n):
            return n, chosen
    return None


def check_multiplier_sets(checker: tools.Checker) -> None:
    """Check 9: the half target across multiplier sets, and two exact limits."""
    # every set C = {1} u B with B inside {2, ..., 12} has its half seed
    subsets = [
        (1, *(a for a in range(2, 13) if mask >> (a - 2) & 1))
        for mask in range(1 << 11)
    ]
    missing = [c for c in subsets if finite_seed(c, max(2, math.lcm(*c))) is None]
    checker.check(
        f'multiplier sets: all {len(subsets)} sets inside {{1,...,12}} have half seeds',
        len(subsets) == 2048 and not missing,
        str(missing[:3]),
    )
    # the extremal whole-word iteration collapses to that seed when M <= 2520
    small = [c for c in subsets if math.lcm(*c) <= 2520]
    open_pairs = []
    for c in small:
        boundary = max(2, math.lcm(*c))
        low, high = stable_pair(c, boundary, (1 << (boundary - 1)) - 1)
        if not low == high == row_solution(c, boundary, (1 << (boundary - 1)) - 1):
            open_pairs.append(c)
    checker.check(
        f'multiplier sets: (14) collapses to the seed for all {len(small)} sets with M <= 2520',
        len(small) == 1542 and not open_pairs,
        str(open_pairs[:3]),
    )
    # the stable-pair proposition on every target at C = {1,2,3,4,6}, M = 12
    c, boundary = (1, 2, 3, 4, 6), 12
    nontrivial = with_seed = 0
    ok = True
    rejoined = 0
    mixed_ok = True
    for target in range(1 << (boundary - 1)):
        low, high = stable_pair(c, boundary, target)
        if low == high:
            ok &= row_solution(c, boundary, target) == low
            continue
        nontrivial += 1
        k = next(
            d for d in range(2, boundary + 1) if (low ^ high) >> (boundary - d) & 1
        )
        point = high >> (boundary - k) << (boundary - k)
        shift = boundary - 2 * k + 1
        ok &= 2 * k <= boundary and high >> shift == point >> shift
        ok &= low >> shift == (point - 1) >> shift
        x = row_solution(c, boundary, target)
        if x is not None:
            with_seed += 1
            ok &= low <= x <= high
            ok &= 9 * abs(x - point) << (4 * k) <= 16 << boundary
        alpha = [0, 0] + [(low >> (boundary - d)) & 1 for d in range(2, boundary + 1)]
        beta = [0, 0] + [(high >> (boundary - d)) & 1 for d in range(2, boundary + 1)]
        minus = [0] * (boundary + 1)
        plus = [0] * (boundary + 1)
        p, q = [0, 1], [0, 1]
        for n in range(2, boundary + 1):
            minus[n] = sum(alpha[n // a] for a in c[1:] if n % a == 0)
            plus[n] = sum(beta[n // a] for a in c[1:] if n % a == 0)
            p.append(2 * p[-1] - alpha[n] - plus[n])
            q.append(2 * q[-1] - beta[n] - minus[n])
        terminal = (1 << (boundary - 1)) - target
        mixed_ok &= p[-1] == q[-1] == terminal
        mixed_ok &= all(p[n] - q[n] == 1 for n in range(k, 2 * k))
        if k >= 3:
            rejoined += 1
            mixed_ok &= beta[2 * k] - alpha[2 * k] == -1
            mixed_ok &= p[2 * k] == q[2 * k]
            # Ordinary carries are recomputed from coefficient sums, independently
            # of the mixed forward recurrence and of its boundary-offset formula.
            ordinary = []
            for word in (alpha, beta):
                coefficient_sum = sum(
                    word[d] << (2 * k - a * d)
                    for d in range(2, 2 * k + 1)
                    for a in c
                    if a * d <= 2 * k
                )
                ordinary.append((1 << (2 * k - 1)) - coefficient_sum)
            mixed_ok &= ordinary == [p[2 * k] + 1, q[2 * k] - 1]
            for n in range(2 * k + 1, min(4 * k, boundary) + 1):
                expected_difference = (
                    -int(n % 2 == 0)
                    + int(n == 3 * k)
                    - int(n % 3 == 0 and n > 3 * k)
                    + int(n == 4 * k)
                )
                common = sum(alpha[n // a] for a in c[1:] if n % a == 0 and n // a < k)
                expected_sum = (
                    2 * common
                    + int(n % 2 == 0)
                    + int(n % 3 == 0 and n >= 3 * k)
                    + int(n == 4 * k)
                )
                mixed_ok &= plus[n] - minus[n] == expected_difference
                mixed_ok &= plus[n] + minus[n] == expected_sum
    checker.check(
        'multiplier sets: stable pairs at all 2048 targets for C = {1,2,3,4,6}, M = 12',
        ok and (nontrivial, with_seed) == (427, 16),
        f'{nontrivial} nontrivial, {with_seed} with a seed',
    )
    checker.check(
        'multiplier sets: mixed rejoin, ordinary offsets and later forcing in 169 pairs',
        mixed_ok and rejoined == 169,
        f'{rejoined} different-target pairs; not a half-target collapse check',
    )
    # integer multiplicities: weights that dominate their tails can meet a gap
    cases = (({1: 1, 2: 1, 3: 3}, 3, [2]), ({1: 1, 3: 3, 4: 2, 5: 1}, 4, [2, 3]))
    for multiplicity, step, prefix in cases:
        got = multiplicity_gap(multiplicity, 40)
        checker.check(
            f'multiplier sets: multiplicities {multiplicity} meet a gap at step {step}',
            got == (step, prefix),
            str(got),
        )
    # its mass sum lambda_a/(2^a - 1) is below that of every multiplier at once
    checker.check(
        'multiplier sets: the second mass is below sum_{a >= 2} 1/(2^a - 1)',
        Fraction(3, 7) + Fraction(2, 15) + Fraction(1, 31)
        < sum(Fraction(1, (1 << a) - 1) for a in range(2, 9)),
    )
    # index-dependent sets B_m inside {2, ..., 10}, pure binary weights after 9
    family = {
        2: (6, 7, 8, 9),
        3: (4, 5, 6, 8, 9, 10),
        4: (3, 4, 8, 10),
        5: (2, 3, 4, 6, 7, 9, 10),
        6: (3, 4, 6, 8),
        7: (2, 3, 4, 5, 6, 8),
        8: (2, 5, 7, 9),
        9: tuple(range(2, 11)),
    }
    scale = 10 * 9 + 8
    values = [
        (1 << (scale - m)) + sum(1 << (scale - a * m) for a in family[m])
        for m in range(2, 10)
    ]
    sums = [0]
    for value in values:
        sums += [s + value for s in sums]
    half, binary_tail = 1 << (scale - 1), 1 << (scale - 9)
    checker.check(
        'multiplier sets: an index-dependent family represents no half',
        not any(0 <= half - s <= binary_tail for s in sums),
    )


def block_mass(start: int, word: int) -> Fraction:
    """Return the mass beyond 2 start of a block word on (start, 2 start]."""
    # bit 2 start - d of the word is the digit at position d
    end = 2 * start
    return sum(
        (
            Fraction(1 << (end - d), (1 << d) - 1)
            for d in range(start + 1, end + 1)
            if word >> (end - d) & 1
        ),
        Fraction(),
    )


def check_full_doubling(checker: tools.Checker, half_selected: list[int]) -> None:
    """Check 10: full-weight doubling blocks and exact renewals for 1/2."""
    # the certified greedy selections of 1/2 through 32, from check 2
    members = set(half_selected)
    chosen = [d for d in half_selected if d <= 32]
    checker.check(
        'full doubling: the selections of 1/2 through 32',
        chosen == [2, 3, 6, 7, 14, 20, 21, 26, 27, 32],
        str(chosen),
    )
    # block identity s_N = 2^H s_H - W - G(W) along the certified prefix; the
    # actual word lies in its window and both neighbours leave it
    ok = True
    candidates_ok = True
    for start in (2, 4, 8, 16, 32, 64):
        end = 2 * start
        r_start = Fraction(1, 2) - sum(
            (Fraction(1, (1 << d) - 1) for d in members if d <= start), Fraction()
        )
        word = sum(1 << (end - d) for d in members if start < d <= end)
        r_end = r_start - sum(
            (Fraction(1, (1 << d) - 1) for d in members if start < d <= end),
            Fraction(),
        )
        lifted = (1 << end) * r_start
        s_end = (1 << end) * r_end
        tail_low, tail_high = tail_enclosure(end, 4)
        sigma_low = (1 << end) * tail_low
        sigma_high = (1 << end) * tail_high
        ok &= s_end == lifted - word - block_mass(start, word)
        ok &= 0 < lifted - word < Fraction(3, 2) and 0 < s_end <= sigma_high
        if word + 1 < 1 << start:
            ok &= lifted - (word + 1) - block_mass(start, word + 1) < 0
        if word >= 1:
            ok &= lifted - (word - 1) - block_mass(start, word - 1) > sigma_high
        pending_old = sum(
            (Fraction(1 << (end % d), (1 << d) - 1) for d in members if d <= start),
            Fraction(),
        )
        carry_before_new_bits = lifted + pending_old
        candidates_ok &= carry_before_new_bits.denominator == 1
        upper_integer = pending_old.numerator // pending_old.denominator + 1
        first_word = carry_before_new_bits.numerator - upper_integer
        candidates_ok &= 0 <= first_word <= 1 << start
        candidates_ok &= word in (first_word, first_word - 1)
        passing = []
        for candidate in (first_word, first_word - 1):
            if not 0 <= candidate < 1 << start:
                continue
            residual = lifted - candidate - block_mass(start, candidate)
            if 0 < residual <= sigma_low:
                passing.append(candidate)
            else:
                # A straddling enclosure is not evidence of failure.
                candidates_ok &= residual < 0 or residual > sigma_high
        candidates_ok &= passing == [word]
        carry_direct = (1 << (end - 1)) - sum(
            sum(1 for d in members if d <= m and m % d == 0) << (end - m)
            for m in range(2, end + 1)
        )
        candidates_ok &= carry_direct == carry_before_new_bits - word
        candidates_ok &= carry_direct in (upper_integer, upper_integer + 1)
        if start == 32:
            candidates_ok &= pending_old < 1 and carry_direct == 2
            candidates_ok &= word == first_word - 1
    checker.check('full doubling: block identity and its two neighbours', ok)
    checker.check(
        'full doubling: explicit two terminal carries select the certified word',
        candidates_ok,
    )

    # Exact positive endpoint controls, and the existing dyadic failure.
    # q * 2^end is integral in each case, so the same carry algebra applies.
    controls = [
        (Fraction(3, 8), 2, [2], 0, 0),
        (Fraction(155, 256), 4, [2, 3, 4], 16, 15),
        (
            Fraction(4203, 32768),
            16,
            [4, 5, 6, 7, 8, 10, 11, 13, 14, 16],
            32768,
            None,
        ),
    ]
    for target, start, prefix, expected_first, expected_pass in controls:
        end = 2 * start
        r_start = target - sum((Fraction(1, (1 << d) - 1) for d in prefix), Fraction())
        low_start, _ = tail_enclosure(start, 4)
        low_end, high_end = tail_enclosure(end, 4)
        pending_old = sum(
            (Fraction(1 << (end % d), (1 << d) - 1) for d in prefix), Fraction()
        )
        lifted = (1 << end) * r_start
        integer_carry = lifted + pending_old
        upper_integer = pending_old.numerator // pending_old.denominator + 1
        first_word = integer_carry.numerator - upper_integer
        ok = 0 < r_start <= low_start and integer_carry.denominator == 1
        ok &= first_word == expected_first
        passing = []
        outcomes = []
        for candidate in (first_word, first_word - 1):
            if not 0 <= candidate < 1 << start:
                continue
            residual = lifted - candidate - block_mass(start, candidate)
            if 0 < residual <= (1 << end) * low_end:
                passing.append(candidate)
                outcomes.append('passes')
            elif residual < 0:
                outcomes.append('negative')
            elif residual > (1 << end) * high_end:
                outcomes.append('above tail')
            else:
                ok = False
                outcomes.append('undecided')
        ok &= passing == ([] if expected_pass is None else [expected_pass])
        if expected_pass is None:
            ok &= outcomes == ['negative', 'above tail']
        checker.check(
            f'full doubling: exact candidate control q={target}, H={start}',
            ok,
            str(outcomes),
        )
    # 1 + G(W) - G(W - 1) = 2^N (w_k - sum_{k < d <= N} w_d) = 2^N g_k + sigma_N
    ok = True
    for start in range(2, 8):
        end = 2 * start
        for word in range(1, 1 << start):
            last = end + 1 - (word & -word).bit_length()
            right = (1 << end) * (
                Fraction(1, (1 << last) - 1)
                - sum(
                    (Fraction(1, (1 << d) - 1) for d in range(last + 1, end + 1)),
                    Fraction(),
                )
            )
            ok &= 1 + block_mass(start, word) - block_mass(start, word - 1) == right
    checker.check('full doubling: separation by the scaled gap for H <= 7', ok)
    # old pending mass beyond 32 and the carry at 32
    pending = sum(
        (Fraction(1 << (32 % d), (1 << d) - 1) for d in chosen if d <= 16), Fraction()
    )
    carry = (1 << 31) - sum(
        sum(1 for d in members if m % d == 0) << (32 - m) for m in range(1, 33)
    )
    word = sum(1 << (32 - d) for d in chosen if d > 16)
    r_end = Fraction(1, 2) - sum(
        (Fraction(1, (1 << d) - 1) for d in chosen), Fraction()
    )
    checker.check(
        'full doubling: E_16 = 376801/344043 > 1 and c_32 = E_16 + G(W) + s_32 = 2',
        pending == Fraction(376801, 344043)
        and pending > 1
        and carry == 2
        and carry == pending + block_mass(16, word) + (1 << 32) * r_end,
        f'{pending} {carry}',
    )
    # Lemma 14 reduces every exact renewal to L = 2 or 6 by Bang--Zsigmondy.
    # Enumerate every subset in those exceptional cases, without claiming
    # that finite enumeration itself proves the reduction.
    found = []
    for last in (2, 6):
        for first in range(1, last):
            target = Fraction(1, 2 * ((1 << first) - 1)) - Fraction(
                1, 2 * ((1 << last) - 1)
            )
            span = list(range(first + 1, last + 1))
            for mask in range(1 << len(span)):
                subset = [k for i, k in enumerate(span) if mask >> i & 1]
                total = sum((Fraction(1, (1 << k) - 1) for k in subset), Fraction())
                if total == target:
                    found.append((first, last, tuple(subset)))
    checker.check(
        'full doubling: exactly three renewals at the exceptional endpoints L=2,6',
        found == [(1, 2, (2,)), (1, 6, (2, 3, 6)), (2, 6, (3, 6))],
        str(found),
    )


def check_controls(checker: tools.Checker) -> None:
    """Controls for the certificates and enclosures used by the checks."""
    # a non-gap with L_{3,1} < q - S_F < T_3 < w_3 must not certify as a gap
    checker.check(
        'controls: 16/125 at step 3 is not certified as a gap',
        not gap_certified(Fraction(16, 125), Run('gap', 3, [])),
    )
    # floor and ceiling of 2^P/(2^n - 1) bracket the exact value
    ok = True
    for precision in (10, 64, 333):
        for n in (1, 2, 3, 7, 31, 64):
            low, high = scaled_w(precision, n)
            d = (1 << n) - 1
            ok &= low * d <= 1 << precision <= high * d and high - low <= 1
    checker.check('controls: floor and ceiling enclosures of 2^P w_n', ok)
    # an independent enclosure of E from sum tau(m) 2^{-m} and the tail (m+2) 2^{-m}
    precision, m_max = 200, 400
    tau = [0] * (m_max + 1)
    for d in range(1, m_max + 1):
        for m in range(d, m_max + 1, d):
            tau[m] += 1
    low = sum(Fraction(tau[m], 1 << m) for m in range(1, m_max + 1))
    high = low + Fraction(m_max + 2, 1 << m_max)
    e_low, e_high = scaled_e(precision)
    checker.check(
        'controls: the enclosure of E meets an independent one',
        Fraction(e_low, 1 << precision) <= high
        and low <= Fraction(e_high, 1 << precision),
    )
    # least-denominator fractions in [x, y] against a direct search
    grid = sorted({Fraction(a, b) for b in range(1, 11) for a in range(0, 2 * b + 1)})
    wrong = []
    for i, x in enumerate(grid):
        for y in grid[i:]:
            den = 1
            while (
                -((-x.numerator * den) // x.denominator) * y.denominator
                > y.numerator * den
            ):
                den += 1
            num = -((-x.numerator * den) // x.denominator)
            got = simplest_fraction(
                x.numerator, x.denominator, y.numerator, y.denominator
            )
            if Fraction(*got) != Fraction(num, den) or got[1] != den:
                wrong.append((x, y))
    checker.check(
        f'controls: least-denominator fractions on {len(grid)} grid points',
        not wrong,
        str(wrong[:3]),
    )
    # boundary cases include two outside endpoints whose interval contains the window
    cases = (
        (-2, 2, 1, 'undecided'),
        (-1, 1, 1, 'undecided'),
        (-1, 0, 1, 'undecided'),
        (0, 1, 1, 'undecided'),
        (-1, -1, 1, 'outside'),
        (1, 1, 1, 'outside'),
        (2, 3, 1, 'outside'),
        (-3, -2, 1, 'outside'),
        (0, 0, 1, 'inside'),
        (-1, 1, 2, 'inside'),
    )
    checker.check(
        'controls: window boundaries and spanning enclosures',
        all(
            classify_window(a, b, bound) == expected for a, b, bound, expected in cases
        ),
    )
    # compare the enclosure's minimizer with exact Fraction arithmetic, including
    # a first-step zero distance for 1/2, where the absolute-value interval crosses 0
    ok = True
    steps, precision = 40, 160
    e_scaled = scaled_e(precision)
    for q in (Fraction(1, 2), Fraction(1, 21)):
        run, _ = greedy(q, steps, e_scaled, precision)
        r = q
        distances = []
        members = set(run.chosen)
        for n in range(1, steps + 1):
            distances.append((abs((1 << n) * r - 1), n))
            if n in members:
                r -= Fraction(1, (1 << n) - 1)
        for first in (1, 15):
            exact, exact_step = min(distances[first - 1 :])
            step, low, high, isolated = closest_approach(
                q, run.chosen, first, steps, precision
            )
            ok &= (
                run.status == 'pass'
                and isolated
                and step == exact_step
                and low <= (1 << precision) * exact <= high
            )
    checker.check('controls: closest approaches against exact rational residuals', ok)


def main() -> int:
    """Run every check and return the exit code."""
    # parse the interface and run the ten checks in order
    parser = tools.evidence_parser(
        'Certify greedy expansions of rationals as sums of distinct 1/(2^n - 1).',
    )
    args = parser.parse_args()
    checker = tools.Checker()
    check_census(checker, args.quick)
    selected = check_long_orbits(checker, args.quick)
    check_near_misses(checker, args.quick)
    check_periodic_supports(checker, args.quick)
    check_finite_interfaces(checker)
    check_window_rule(checker, args.quick, selected[2])
    check_finite_seeds(checker)
    check_seed_repair(checker)
    check_multiplier_sets(checker)
    check_full_doubling(checker, selected[2])
    check_controls(checker)
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

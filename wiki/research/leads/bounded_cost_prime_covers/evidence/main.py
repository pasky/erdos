"""Check explicit prime covers and run finite exploratory window probes.

Checked clauses:

1. The recipe of Proposition 1 (class 1 mod 2, residue 0 for the primes in
   (z, N/2] with z = N^(1/u) and u = 4 log log N, one prime of (N/2, N] for
   each remaining integer) is a valid cover of [1, N] for each tested N: the
   cleanup primes exist, the selected primes are distinct, and every integer
   in [1, N] lies in a selected class. The uncovered set before cleanup equals
   the even z-smooth integers, computed independently from largest prime
   factors.
2. The same design with z tuned (the largest tested prime cutoff up to
   sqrt(N) for which the cleanup primes suffice) is a valid cover. Integer
   arithmetic verifies cost < 33/20; a decimal approximation is also reported.
3. Window probe, primes in (N^(1/3), N], every class forced to have exactly
   floor(N/p) points in [1, N] (no boundary gain): the zero classes leave
   exactly the N^(1/3)-smooth integers, and no change of a single prime's
   class lowers that number. The same two checks run for the windows
   (N^(1/4), N] and (N^(1/5), N] with N^(1/4)- and N^(1/5)-smooth integers. A local search from a seeded random start ends
   with more survivors than the zero classes. Seeded Metropolis annealing
   by single-class moves, started at the zero classes, never reaches fewer
   survivors than the zero classes; started at random classes, it ends
   above them.
4. Union probe for Hypothesis H: for one full class modulo each prime in
   (L^(1/2), L^(9/10)], L = 3000, 10^4, 3*10^4, 10^5 and 3*10^5, the union sizes of
   the zero, seeded random, greedy and locally improved choices are
   reported; the maintained union counts are checked against a recount from
   the chosen classes.
5. A coordinated gain at N = 105: the classes 0 mod 5, 6 mod 7 and 0 mod 11
   cover 41 integers, against 40 for the zero classes. Every class has
   floor(N/p) members, every pair intersection has its zero-class size, and
   the new triple intersection is exactly {55}. The cost is exactly 167/385.
   This is an exact finite witness for a selected subset of the window,
   not a cover or an asymptotic claim.
6. Small-prime union probe for (22): for the primes in (N^(1/3), N^(1/2)],
   N = 10^6 and 10^7, with every class forced to have exactly floor(N/p)
   points, the union of the zero classes equals the inclusion-exclusion
   value sum floor(N/p) - sum floor(N/pq) exactly (every pair of these
   primes has product at most N, every triple above N). From a
   seeded random start, coordinate ascent gives each prime in turn the
   class covering the most integers that the other classes miss. The
   maintained counts are checked against a recount, and the ascent never
   lowers the union. At N = 10^6, seeded Metropolis annealing by
   single-class moves from another random start is a second search, with
   its maintained union checked against a recount. The reported excess of a
   union over the zero value is X_S of display (26) on the research page.
7. Centered construction: with b = floor(N/2) + 1, give every prime in
   (z, N/2] the class b modulo p, and use distinct primes in (N/2, N]
   for the survivors. At the tested N, check the exact survivor set by
   independently factoring |n-b|, the cleanup supply, and final coverage.
   Check both z = N^(1/(4 log log N)) and the largest tested prime cutoff
   up to sqrt(N) fitting that supply. The center itself is already covered.
   For each tuned cover check cost < 131/100 by integer arithmetic.

Clauses 3, 4 and 6 are finite heuristics. They bear on which side of the next
test to attack and prove nothing asymptotic; clauses 1 and 7 check finite
instances of recipes whose validity for all large N is proved on the
research page.

Run from the repository root:
    uv run --no-sync python wiki/research/leads/bounded_cost_prime_covers/evidence/main.py

Arithmetic: coverage and intersections use integer counts and exact sets.
Cutoff choices and exploratory probabilities use floating point; the checked
cover predicate and the rational cost upper bounds do not rely on its accuracy.
Dependencies: numpy and the installed root ``tools`` package. No inputs or
output files; deterministic (fixed seeds). The full run takes about two
minutes; ``--quick`` uses smaller N and L and takes a few seconds. Every
failed obligation exits nonzero, including under ``python -O``.
"""

from __future__ import annotations

import math
import random
import sys
from fractions import Fraction
from itertools import combinations, pairwise

import numpy as np

import tools

__all__ = [
    'main',
]


def largest_prime_factor(n: int) -> tuple[np.ndarray, np.ndarray]:
    """Return the primes up to n and the largest prime factor of 0..n (1 for 0, 1)."""
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, math.isqrt(n) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
    primes = np.nonzero(sieve)[0]
    lpf = np.ones(n + 1, dtype=np.int64)
    for p in primes:
        lpf[p::p] = p
    return primes, lpf


def coverage_count(n: int, classes: dict[int, int]) -> np.ndarray:
    """Return the number of selected classes containing each of 0..n (index 0 unused)."""
    cnt = np.zeros(n + 1, dtype=np.int32)
    for p, a in classes.items():
        start = a % p
        if start == 0:
            start = p
        cnt[start::p] += 1
    return cnt


def build_cover(
    n: int, z: float, primes: np.ndarray, lpf: np.ndarray
) -> tuple[dict[int, int], np.ndarray, np.ndarray] | None:
    """Return the classes of the design for cutoff z, the set S, and the top primes, or None."""
    classes = {2: 1}
    middle = primes[(primes > z) & (primes <= n // 2)]
    for p in middle:
        classes[int(p)] = 0
    cnt = coverage_count(n, classes)
    s = np.nonzero(cnt[1:] == 0)[0] + 1
    top = primes[(primes > n // 2) & (primes <= n)]
    if len(s) > len(top):
        return None
    for value, q in zip(s, top):
        classes[int(q)] = int(value) % int(q)
    return classes, s, top


def check_construction(checker: tools.Checker, n: int) -> None:
    """Check the recipe of Proposition 1 and its tuned variant at n."""
    primes, lpf = largest_prime_factor(n)
    u = 4 * math.log(math.log(n))
    z = n ** (1 / u)
    built = build_cover(n, z, primes, lpf)
    checker.check(
        f'N={n}: recipe has enough cleanup primes (z={z:.3f})', built is not None
    )
    if built is None:
        return
    classes, s, top = built
    evens = np.arange(2, n + 1, 2)
    expected = evens[lpf[evens] <= z]
    checker.check(
        f'N={n}: recipe survivors before cleanup are the even z-smooth integers',
        np.array_equal(s, expected),
    )
    cnt = coverage_count(n, classes)
    checker.check(
        f'N={n}: recipe covers every integer in [1,N]', bool(np.all(cnt[1:] >= 1))
    )
    cost = math.fsum(1.0 / p for p in classes)
    print(
        f'    recipe: z={z:.3f}, |S|={len(s)}, cleanup primes available={len(top)}, cost={cost:.6f}'
    )
    # Largest tested prime cutoff up to sqrt(n) with |S| fitting the top primes.
    evens_lpf = np.sort(lpf[evens])
    top_count = len(top)
    candidates = primes[primes <= math.isqrt(n)]
    best = None
    for p in candidates:
        if np.searchsorted(evens_lpf, p, side='right') <= top_count:
            best = int(p)
    checker.check(
        f'N={n}: some tuned cutoff fits the cleanup capacity', best is not None
    )
    if best is None:
        return
    tuned = build_cover(n, best, primes, lpf)
    checker.check(
        f'N={n}: tuned design (z={best}) has enough cleanup primes', tuned is not None
    )
    if tuned is None:
        return
    classes, s, top = tuned
    cnt = coverage_count(n, classes)
    checker.check(
        f'N={n}: tuned design covers every integer in [1,N]', bool(np.all(cnt[1:] >= 1))
    )
    scale = 10**9
    cost_upper = sum((scale + p - 1) // p for p in classes)
    checker.check(
        f'N={n}: tuned reciprocal cost is less than 33/20',
        20 * cost_upper < 33 * scale,
        f'exact upper bound {cost_upper}/{scale}',
    )
    cost = math.fsum(1.0 / p for p in classes)
    print(
        f'    tuned: z={best}, |S|={len(s)}, cleanup primes available={len(top)}, cost={cost:.6f}'
    )


def check_centered_construction(checker: tools.Checker, n: int) -> None:
    """Check the midpoint recipe and a tuned cutoff without a small-prime core."""
    primes, lpf = largest_prime_factor(n)
    center = n // 2 + 1
    distance = np.abs(np.arange(1, n + 1) - center)
    top = primes[primes > n // 2]
    distance_factors = np.sort(lpf[distance[distance > 0]])
    candidates = [
        int(p)
        for p in primes[primes <= math.isqrt(n)]
        if np.searchsorted(distance_factors, p, side='right') <= len(top)
    ]
    checker.check(f'centered N={n}: a tuned cutoff fits the supply', bool(candidates))
    if not candidates:
        return
    cutoffs = [('recipe', n ** (1 / (4 * math.log(math.log(n)))))]
    cutoffs.append(('tuned', candidates[-1]))
    for label, cutoff in cutoffs:
        classes = {int(p): center % int(p) for p in primes if cutoff < p <= n // 2}
        checker.check(f'centered N={n} {label}: middle set is nonempty', bool(classes))
        if not classes:
            continue
        counts = coverage_count(n, classes)
        survivors = np.flatnonzero(counts[1:] == 0) + 1
        expected = np.flatnonzero((distance > 0) & (lpf[distance] <= cutoff)) + 1
        checker.check(
            f'centered N={n} {label}: survivors are exactly the smooth distances',
            np.array_equal(survivors, expected) and counts[center] == len(classes),
        )
        enough = len(survivors) <= len(top)
        checker.check(f'centered N={n} {label}: cleanup supply suffices', enough)
        if not enough:
            continue
        for value, q in zip(survivors, top):
            classes[int(q)] = int(value) % int(q)
        counts = coverage_count(n, classes)
        checker.check(
            f'centered N={n} {label}: every integer is covered',
            bool(np.all(counts[1:] >= 1)),
        )
        if label == 'tuned':
            scale = 10**9
            cost_upper = sum((scale + p - 1) // p for p in classes)
            checker.check(
                f'centered N={n}: tuned cost is less than 131/100',
                100 * cost_upper < 131 * scale,
                f'exact upper bound {cost_upper}/{scale}',
            )
        print(
            f'    centered {label}: N={n}, z={cutoff:.3f}, '
            f'|S|={len(survivors)}, available={len(top)}, '
            f'cost={math.fsum(1.0 / p for p in classes):.6f}'
        )


def window_probe(
    checker: tools.Checker, n: int, passes: int, anneal_steps: int = 0, root: int = 3
) -> None:
    """Probe the window (N^(1/root), N] with classes of exactly floor(N/p) points.

    The local search runs only when passes is positive, and the annealing
    only when anneal_steps is positive as well.
    """
    primes, lpf = largest_prime_factor(n)
    cut = n ** (1 / root)
    window = primes[primes > cut]
    tag = f'window N={n}' if root == 3 else f'window u={root} N={n}'
    cnt = np.zeros(n + 1, dtype=np.int32)
    for p in window:
        cnt[p::p] += 1
    cnt[0] = 1
    zero = int(np.count_nonzero(cnt == 0))
    smooth = int(np.count_nonzero(lpf[1:] <= cut))
    checker.check(
        f'{tag}: zero classes leave exactly the N^(1/{root})-smooth integers',
        zero == smooth,
        f'{zero} vs {smooth}',
    )
    improving = 0
    for p in window:
        cnt[p::p] -= 1
        free = np.nonzero(cnt == 0)[0]
        gain = np.bincount(free % p, minlength=p)
        allowed = np.arange(n % p + 1, p + 1) % p
        if gain[allowed].max() > gain[0]:
            improving += 1
        cnt[p::p] += 1
    checker.check(
        f'{tag}: no single-prime class change improves the zero classes',
        improving == 0,
        f'{improving} improving moves',
    )
    if not passes:
        print(f'    {tag}: zero survivors {zero} ({zero / n:.4f} N)')
        return
    rng = np.random.default_rng(0)
    cls = {}
    cnt = np.zeros(n + 1, dtype=np.int32)
    for p in window:
        a = int(rng.integers(n % p + 1, p + 1))
        cls[int(p)] = a
        cnt[a::p] += 1
    cnt[0] = 1
    history = [int(np.count_nonzero(cnt == 0))]
    order = window.copy()
    for _ in range(passes):
        rng.shuffle(order)
        for p in order:
            p = int(p)
            a0 = cls[p]
            cnt[a0::p] -= 1
            free = np.nonzero(cnt == 0)[0]
            gain = np.bincount(free % p, minlength=p)
            cand = np.arange(n % p + 1, p + 1)
            best = int(cand[np.argmax(gain[cand % p])])
            if gain[best % p] <= gain[a0 % p]:
                best = a0
            cls[p] = best
            cnt[best::p] += 1
        history.append(int(np.count_nonzero(cnt == 0)))
    recount = np.zeros(n + 1, dtype=np.int32)
    for p, a in cls.items():
        recount[a::p] += 1
    recount[0] = 1
    checker.check(
        f'window N={n}: local-search counts match a recount',
        np.array_equal(recount, cnt),
    )
    checker.check(
        f'window N={n}: seeded local search ends above the zero classes',
        history[-1] > zero,
        f'{history[-1]} vs {zero}',
    )
    print(
        f'    window N={n}: zero survivors {zero} ({zero / n:.4f} N); random start then passes {history}'
    )
    if anneal_steps:
        z_first, z_best, z_end = anneal(n, window, 'zero', anneal_steps, seed=0)
        checker.check(
            f'window N={n}: annealing counts are consistent (zero start)', z_best >= 0
        )
        checker.check(
            f'window N={n}: annealing from the zero classes finds no fewer survivors',
            z_first == zero and z_best >= zero,
            f'{z_first}, best {z_best}',
        )
        r_first, r_best, r_end = anneal(n, window, 'random', 2 * anneal_steps, seed=1)
        checker.check(
            f'window N={n}: annealing counts are consistent (random start)', r_best >= 0
        )
        checker.check(
            f'window N={n}: annealing from random classes ends above the zero classes',
            r_end > zero,
            f'{r_end} vs {zero}',
        )
        print(
            f'    window N={n}: annealing from zero: best {z_best}, end {z_end}; from random: start {r_first}, best {r_best}, end {r_end}'
        )


def anneal(
    n: int, window: np.ndarray, start: str, steps: int, seed: int
) -> tuple[int, int, int]:
    """Return the start, best and final survivor counts of a seeded annealing run.

    A move picks an uncovered integer x and a window prime p, and proposes the
    class of x modulo p when that class has floor(n/p) points; it is accepted
    with the Metropolis rule at a temperature falling from 0.7 to 0.02.
    """
    gen = random.Random(seed)
    primes = [int(p) for p in window]
    cnt = np.zeros(n + 1, dtype=np.int32)
    cls = {}
    for p in primes:
        a = p if start == 'zero' else gen.randint(n % p + 1, p)
        cls[p] = a
        cnt[a::p] += 1
    cnt[0] = 1
    uncovered = set(np.nonzero(cnt == 0)[0].tolist())
    pool = list(uncovered)
    count = len(uncovered)
    first = best = count
    for t in range(steps):
        if not uncovered:
            break
        if t % 20000 == 0:
            pool = list(uncovered)
        x = gen.choice(pool)
        p = gen.choice(primes)
        if x not in uncovered:
            continue
        c = x % p or p
        if c != p and c <= n % p:
            continue
        a0 = cls[p]
        if c == a0:
            continue
        delta = int(np.count_nonzero(cnt[a0::p] == 1)) - int(
            np.count_nonzero(cnt[c::p] == 0)
        )
        temp = 0.7 * (0.02 / 0.7) ** (t / steps)
        if delta <= 0 or gen.random() < math.exp(-delta / temp):
            cnt[a0::p] -= 1
            freed = np.arange(a0, n + 1, p)[cnt[a0::p] == 0]
            uncovered.update(freed.tolist())
            hit = np.arange(c, n + 1, p)[cnt[c::p] == 0]
            uncovered.difference_update(hit.tolist())
            cnt[c::p] += 1
            cls[p] = c
            count += delta
            best = min(best, count)
    recount = np.zeros(n + 1, dtype=np.int32)
    for p, a in cls.items():
        recount[a::p] += 1
    recount[0] = 1
    if int(np.count_nonzero(recount == 0)) != count or len(uncovered) != count:
        return first, -1, -1
    return first, best, count


def union_probe(checker: tools.Checker, size: int, passes: int) -> None:
    """Report union sizes of one full class modulo each prime in (L^(1/2), L^(9/10)]."""
    primes, _ = largest_prime_factor(int(size**0.9) + 1)
    mods = primes[(primes > size**0.5) & (primes <= size**0.9)]
    kappa = math.fsum(1.0 / p for p in mods)
    rng = np.random.default_rng(1)
    results = {}
    cnt = np.zeros(size, dtype=np.int32)
    for r in mods:
        cnt[0::r] += 1
    results['zero'] = np.count_nonzero(cnt) / size
    cnt[:] = 0
    for r in mods:
        cnt[int(rng.integers(r)) :: r] += 1
    results['random'] = np.count_nonzero(cnt) / size
    cnt[:] = 0
    choice = {}
    order = mods[::-1]

    def best_class(r: int) -> int:
        """Return the class modulo r adding the fewest new points to the union."""
        used = np.nonzero(cnt)[0]
        hits = np.bincount(used % r, minlength=r)
        classes = np.arange(r)
        return int(np.argmin((size - 1 - classes) // r + 1 - hits))

    for r in order:
        r = int(r)
        choice[r] = best_class(r)
        cnt[choice[r] :: r] += 1
    results['greedy'] = np.count_nonzero(cnt) / size
    for _ in range(passes):
        for r in order:
            r = int(r)
            cnt[choice[r] :: r] -= 1
            choice[r] = best_class(r)
            cnt[choice[r] :: r] += 1
    results['local'] = np.count_nonzero(cnt) / size
    recount = np.zeros(size, dtype=np.int32)
    for r, c in choice.items():
        recount[c::r] += 1
    checker.check(
        f'union L={size}: maintained counts match a recount',
        np.array_equal(recount, cnt),
    )
    shown = ', '.join(f'{k} {v:.4f}' for k, v in results.items())
    print(
        f'    union L={size}: {len(mods)} primes, reciprocal sum {kappa:.4f}; union/L: {shown}; max multiplicity {int(cnt.max())}'
    )


def small_prime_anneal(
    n: int, small: list[int], steps: int, seed: int
) -> tuple[int, int]:
    """Return the final and best unions of a seeded annealing run, or (-1, -1).

    A move gives one prime a uniformly chosen class of floor(n/p) points
    and is accepted by the Metropolis rule at a temperature falling from 3
    to 0.05 (in units of integers covered).
    """
    gen = random.Random(seed)
    cnt = np.zeros(n + 1, dtype=np.int32)
    cls = {}
    for p in small:
        a = gen.randint(n % p + 1, p)
        cls[p] = a
        cnt[a::p] += 1
    cnt[0] = 1
    union = best = int(np.count_nonzero(cnt[1:]))
    for t in range(steps):
        p = gen.choice(small)
        a0 = cls[p]
        a1 = gen.randint(n % p + 1, p)
        if a1 == a0:
            continue
        delta = int(np.count_nonzero(cnt[a1::p] == 0)) - int(
            np.count_nonzero(cnt[a0::p] == 1)
        )
        temp = 3.0 * (0.05 / 3.0) ** (t / steps)
        if delta >= 0 or gen.random() < math.exp(delta / temp):
            cnt[a0::p] -= 1
            cnt[a1::p] += 1
            cls[p] = a1
            union += delta
            best = max(best, union)
    recount = np.zeros(n + 1, dtype=np.int32)
    for p, a in cls.items():
        recount[a::p] += 1
    if int(np.count_nonzero(recount[1:])) != union:
        return -1, -1
    return union, best


def small_prime_union_probe(
    checker: tools.Checker, n: int, passes: int, anneal_steps: int
) -> None:
    """Probe the union of floor-size classes modulo the primes in (N^(1/3), N^(1/2)]."""
    primes, _ = largest_prime_factor(math.isqrt(n))
    small = [int(p) for p in primes if p**3 > n]
    checker.check(
        f'small union N={n}: every pair product is at most N, every triple above N',
        small[-1] * small[-2] <= n and small[0] * small[1] * small[2] > n,
    )
    cnt = np.zeros(n + 1, dtype=np.int32)
    for p in small:
        cnt[p::p] += 1
    cnt[0] = 1
    zero = int(np.count_nonzero(cnt[1:]))
    s1 = sum(n // p for p in small)
    s2 = sum(n // (p * q) for p, q in combinations(small, 2))
    checker.check(
        f'small union N={n}: zero-class union equals S1 - S2',
        zero == s1 - s2,
        f'{zero} vs {s1 - s2}',
    )
    rng = np.random.default_rng(2)
    cls = {}
    cnt = np.zeros(n + 1, dtype=np.int32)
    for p in small:
        a = int(rng.integers(n % p + 1, p + 1))
        cls[p] = a
        cnt[a::p] += 1
    cnt[0] = 1
    history = [int(np.count_nonzero(cnt[1:]))]
    order = list(small)
    gen = random.Random(2)
    for _ in range(passes):
        gen.shuffle(order)
        for p in order:
            a0 = cls[p]
            cnt[a0::p] -= 1
            free = np.nonzero(cnt == 0)[0]
            gain = np.bincount(free % p, minlength=p)
            cand = np.arange(n % p + 1, p + 1)
            best = int(cand[np.argmax(gain[cand % p])])
            if gain[best % p] <= gain[a0 % p]:
                best = a0
            cls[p] = best
            cnt[best::p] += 1
        history.append(int(np.count_nonzero(cnt[1:])))
    recount = np.zeros(n + 1, dtype=np.int32)
    for p, a in cls.items():
        recount[a::p] += 1
    recount[0] = 1
    checker.check(
        f'small union N={n}: ascent counts match a recount',
        np.array_equal(recount, cnt),
    )
    checker.check(
        f'small union N={n}: coordinate ascent never lowers the union',
        all(b >= a for a, b in pairwise(history)),
        f'{history}',
    )
    rich = int(np.count_nonzero(cnt[1:] >= 4))
    expected = n * (1 - math.prod(1 - 1 / p for p in small))
    print(
        f'    small union N={n}: {len(small)} primes; union/N zero {zero / n:.5f}, '
        f'random-class mean {expected / n:.5f}, seeded start {history[0] / n:.5f}, '
        f'after ascent {history[-1] / n:.5f}; excess over zero {(history[-1] - zero) / n:.5f} N; '
        f'integers in four or more classes {rich}'
    )
    if not anneal_steps:
        return
    final, best = small_prime_anneal(n, small, anneal_steps, seed=3)
    checker.check(f'small union N={n}: annealing union matches a recount', final >= 0)
    print(
        f'    small union N={n}: annealing ({anneal_steps} moves) final excess '
        f'{(final - zero) / n:.5f} N, best {(best - zero) / n:.5f} N'
    )


def check_coordinated_gain(checker: tools.Checker) -> None:
    """Recount the three-prime witness by exact set operations."""
    n = 105
    classes = {5: 0, 7: 6, 11: 0}
    zero = {p: {x for x in range(1, n + 1) if x % p == 0} for p in classes}
    shifted = {
        p: {x for x in range(1, n + 1) if x % p == a} for p, a in classes.items()
    }
    checker.check(
        'coordinated gain: prime window and exact reciprocal cost',
        all(p**3 > n for p in classes)
        and sum((Fraction(1, p) for p in classes), Fraction()) == Fraction(167, 385),
    )
    checker.check(
        'coordinated gain: unchanged class and pair-intersection sizes',
        all(len(shifted[p]) == len(zero[p]) == n // p for p in classes)
        and all(
            p * q <= n and len(shifted[p] & shifted[q]) == len(zero[p] & zero[q])
            for p, q in combinations(classes, 2)
        ),
    )
    checker.check(
        'coordinated gain: exactly one new triple intersection, at 55',
        set.intersection(*zero.values()) == set()
        and set.intersection(*shifted.values()) == {55},
    )
    checker.check(
        'coordinated gain: union increases from 40 to 41, without covering [1,105]',
        len(set.union(*zero.values())) == 40
        and len(set.union(*shifted.values())) == 41 < n,
    )


def main() -> int:
    """Run every clause and return the exit code."""
    parser = tools.evidence_parser(__doc__.splitlines()[0])
    args = parser.parse_args()
    checker = tools.Checker()
    sizes = [10**4, 10**5] if args.quick else [10**4, 10**5, 10**6]
    print('Clauses 1-2: explicit covers')
    for n in sizes:
        check_construction(checker, n)
    print('Clause 3: window probe (heuristic)')
    for n in [30000] if args.quick else [30000, 100000]:
        steps = 0 if n > 30000 else (500000 if args.quick else 3000000)
        window_probe(checker, n, passes=3 if args.quick else 6, anneal_steps=steps)
    for root in (4, 5):
        for n in [30000] if args.quick else [30000, 100000]:
            window_probe(checker, n, passes=0, root=root)
    print('Clause 4: union probe for Hypothesis H (heuristic)')
    for size in [3000, 10**4] if args.quick else [3000, 10**4, 30000, 10**5, 300000]:
        union_probe(checker, size, passes=2 if args.quick else 3)
    print('Clause 5: exact coordinated-gain witness')
    check_coordinated_gain(checker)
    print('Clause 6: small-prime union probe for (22) (heuristic)')
    for n in [10**5] if args.quick else [10**6, 10**7]:
        steps = 200000 if args.quick else (1500000 if n == 10**6 else 0)
        small_prime_union_probe(
            checker, n, passes=2 if args.quick else 5, anneal_steps=steps
        )
    print('Clause 7: exact centered covers')
    for n in sizes:
        check_centered_construction(checker, n)
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

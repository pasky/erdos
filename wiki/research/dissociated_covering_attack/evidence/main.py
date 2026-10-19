"""Check the exact small cases of the twisted-layer note.

Scope, all by exact integer and rational arithmetic:

1. mu_15: its nonzero signed relations (446), their supports (127, of which 98
   are minimal, of sizes 3, 5, 6, 7, 8, 9), the largest dissociated size (8),
   the 1440 proper 2-colorings, their four orbits of 360 under the coordinate
   permutations Sym(3) x Sym(5), invariance of the minimal supports under
   those permutations, and the root-span counts of the color classes.
2. The nine retained layer colorings (assets/nine_layers.json) are proper
   2-colorings of mu_15 whose color classes have trivial signed-span
   intersection for both colors.
3. For M in {105, 165, 195, 1155, 15015} (and 255255 in the full run) and
   q in {3, 4}, the arc of ceil(M/q) consecutive roots lies below the rank
   phi(M) and no root outside it lies in its signed span.
4. For the q = 3 arc class at M = 105 and M = 1155, the probability that a
   uniform coordinate twist sends a signed pair of distinct roots into the
   arc's signed span, computed per agreement pattern and sign, is 1/3 for the
   pairs on one coset of mu_3 with sign +1 (a single root in disguise) and at
   most 2/15 for every other pattern and sign.
5. Phi_165 and Phi_195 have height two and (1 - x) Phi_165, (1 - x) Phi_195
   are flat, so D(165) = 81 and D(195) = 97.
6. For the q = 3 arc class at M = 105, every orbit of signed triples of
   distinct roots under the coordinate twists, other than the orbits whose
   values visibly reduce through cosets of mu_3 or mu_5, survives a uniform
   twist with probability at most 4/45, and needs no more layers than the
   roots: lambda <= |O|^(-log(1/kappa)/log M) for each such orbit O.
7. The numerical instances of Lemma 7: with p the next prime and |G_M| the
   product of p_i! over the primes of M, the lower bound
   (2^|C| - 1) / |G_M|^(p - 1) exceeds 2^12 for a class of ceil(M/2) roots
   at M = 1155, exceeds 2^2479 for classes of ceil(M/q) roots at M = 15015
   and q in {2, 3, 4}, and is below 1 for q = 3 at M = 1155.
8. Survival sets at M = 105 for the arc class of 35 roots, exhaustively over
   all 3628800 coordinate twists Sym(3) x Sym(5) x Sym(7): the sum of the
   whole arc, with all signs +1 and with alternating signs, survives exactly
   the identity and the reflection e -> 34 - e (Lemma 10); in the full run,
   twelve seeded signed sums on 20, 22 and 24 arc points have survival sets
   meeting fewer than 11 left cosets of the affine group (720 cosets in all;
   11 is the next prime, the threshold of Lemma 9 for the step to 1155),
   while each of four seeded signed sums on 10 arc points meets at least 11;
   among ten seeded signed sums on 17 arc points, one meets at least 11
   cosets and one has surviving twists that do not carry its support into
   the arc; the relation between such a twisted image and its
   representation inside the arc lies on at most three grid lines.
9. A seeded twisted layering of the three arcs of mu_15 over the seven layers
   of mu_105 is proper and robust; its three classes of 35 roots are linearly
   independent; the sum of each whole class survives only the identity among
   all 3628800 twists (class 0 only in quick mode); in the full run, six
   seeded signed sums on 20 class points each survive fewer than 11 twists
   and six on 10 class points each survive at least 11.

Run from the repository root:
    uv run --no-sync python wiki/research/dissociated_covering_attack/evidence/main.py

Dependencies are NumPy, the standard library and the installed root
``tools`` package. Integer arrays are int64 with an explicit overflow guard.
The full run takes about twenty minutes, dominated by the conductor 255255;
``--quick`` omits that conductor and the seeded parts of items 8 and 9 and
takes under a minute. Every failed
obligation exits nonzero, including under ``python -O``. These finite checks
prove no statement about larger conductors.
"""

from __future__ import annotations

import itertools
import json
import math
import pathlib
import random
import sys
from collections.abc import Callable
from fractions import Fraction
from functools import cache

import numpy as np

import tools

__all__ = [
    'main',
]

_HERE = pathlib.Path(__file__).resolve().parent

# bound every integer array entry well inside int64
_GUARD = 1 << 60


def _poly_div_exact(num: list[int], den: list[int]) -> list[int]:
    """Return num / den for integer polynomials (low degree first), exact."""
    num = list(num)
    out = [0] * (len(num) - len(den) + 1)
    for i in range(len(out) - 1, -1, -1):
        coef = num[i + len(den) - 1] // den[-1]
        if coef * den[-1] != num[i + len(den) - 1]:
            raise ValueError('inexact division')
        out[i] = coef
        if coef == 0:
            continue
        for j, d in enumerate(den):
            num[i + j] -= coef * d
    if any(num[: len(den) - 1]):
        raise ValueError('nonzero remainder')
    return out


def _poly_mul(a: list[int], b: list[int]) -> list[int]:
    """Return the product of two integer polynomials (low degree first)."""
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def _cyclotomic(n: int) -> list[int]:
    """Return Phi_n by recursive exact division of x^n - 1 by Phi_d, d | n, d < n."""
    poly = [-1] + [0] * (n - 1) + [1]
    for d in range(1, n):
        if n % d == 0:
            poly = _poly_div_exact(poly, _cyclotomic(d))
    return poly


def _coordinate_step(v: np.ndarray, low: np.ndarray, height: int) -> np.ndarray:
    """Multiply by x modulo a monic polynomial, bounding arithmetic first."""
    head = int(v[-1])
    bound = int(np.max(np.abs(v), initial=0)) + abs(head) * height
    if bound > _GUARD:
        raise OverflowError('coordinate step could overflow')
    return np.concatenate(([0], v[:-1])) - head * low


def _coordinates(phi: list[int], count: int) -> np.ndarray:
    """Return the power-basis coordinates of x^0, ..., x^(count-1) modulo phi."""
    deg = len(phi) - 1
    height = max(abs(c) for c in phi[:deg])
    if height > _GUARD:
        raise OverflowError('polynomial coefficients could overflow')
    low = np.array(phi[:deg], dtype=np.int64)
    out = np.zeros((count, deg), dtype=np.int64)
    v = np.zeros(deg, dtype=np.int64)
    v[0] = 1
    for e in range(count):
        out[e] = v
        v = _coordinate_step(v, low, height)
    # All later signed sums and differences use at most twice this many roots.
    if 2 * count * int(np.max(np.abs(out), initial=0)) > _GUARD:
        raise OverflowError('signed sums could overflow')
    return out


def _signed_sums(coords: np.ndarray, members: list[int]) -> set[bytes]:
    """Return all signed sums of the given roots, encoded as bytes."""
    sums = np.zeros((1, coords.shape[1]), dtype=np.int64)
    for e in members:
        sums = np.concatenate([sums - coords[e], sums, sums + coords[e]])
    return {row.tobytes() for row in sums}


def _check_mu15(checker: tools.Checker) -> tuple[np.ndarray, list[int]]:
    """Run item 1 and return the coordinates of mu_15 and its minimal supports."""
    n = 15
    coords = _coordinates(_cyclotomic(n), n)
    # enumerate every ternary vector on the 15 roots in chunks
    powers = np.array([3**i for i in range(n)], dtype=np.int64)
    zero_index = (3**n - 1) // 2
    relations = []
    for start in range(0, 3**n, 3**10):
        idx = np.arange(start, min(3**n, start + 3**10), dtype=np.int64)
        f = (idx[:, None] // powers[None, :]) % 3 - 1
        hits = np.flatnonzero(~(f @ coords).any(axis=1))
        relations.extend(f[i] for i in hits if idx[i] != zero_index)
    supports = sorted({sum(1 << e for e in range(n) if r[e]) for r in relations})
    minimal = [s for s in supports if not any(t != s and t & s == t for t in supports)]
    sizes = sorted({bin(s).count('1') for s in minimal})
    checker.check(
        'mu_15 has 446 nonzero signed relations',
        len(relations) == 446,
        f'observed {len(relations)}',
    )
    checker.check(
        'mu_15 has 127 relation supports',
        len(supports) == 127,
        f'observed {len(supports)}',
    )
    checker.check(
        'mu_15 has 98 minimal supports', len(minimal) == 98, f'observed {len(minimal)}'
    )
    checker.check(
        'minimal support sizes are 3, 5, 6, 7, 8, 9',
        sizes == [3, 5, 6, 7, 8, 9],
        f'observed {sizes}',
    )

    def dissociated(mask: int) -> bool:
        return not any(m & mask == m for m in minimal)

    full = (1 << n) - 1
    largest = max(bin(a).count('1') for a in range(1 << n) if dissociated(a))
    checker.check(
        'largest dissociated subset of mu_15 has 8 elements',
        largest == 8,
        f'observed {largest}',
    )
    proper = sorted(
        {
            min(a, full ^ a)
            for a in range(1 << n)
            if dissociated(a) and dissociated(full ^ a)
        }
    )
    checker.check(
        'mu_15 has 1440 proper 2-colorings',
        len(proper) == 1440,
        f'observed {len(proper)}',
    )
    class_sizes = sorted(
        {tuple(sorted((bin(a).count('1'), 15 - bin(a).count('1')))) for a in proper}
    )
    checker.check(
        'every proper 2-coloring has classes of sizes 7 and 8',
        class_sizes == [(7, 8)],
        f'{class_sizes}',
    )
    # coordinate permutations of Z/3 x Z/5 act on the exponents through the residues
    point = {(e % 3, e % 5): e for e in range(n)}
    group = [
        [point[(s3[e % 3], s5[e % 5])] for e in range(n)]
        for s3 in itertools.permutations(range(3))
        for s5 in itertools.permutations(range(5))
    ]

    def act(g: list[int], mask: int) -> int:
        return sum(1 << g[e] for e in range(n) if mask >> e & 1)

    minimal_set = set(minimal)
    invariant = all(act(g, m) in minimal_set for g in group for m in minimal)
    checker.check('minimal supports are invariant under Sym(3) x Sym(5)', invariant)
    remaining = set(proper)
    orbit_sizes = []
    while remaining:
        a = min(remaining)
        orbit = {min(act(g, a), full ^ act(g, a)) for g in group}
        orbit_sizes.append(len(orbit))
        remaining -= orbit
    checker.check(
        'the colorings form four orbits of 360',
        sorted(orbit_sizes) == [360] * 4,
        f'{orbit_sizes}',
    )
    roots = [coords[e].tobytes() for e in range(n)]
    tally: dict[tuple[int, int], int] = {}
    for a in proper:
        for cls in (a, full ^ a):
            sums = _signed_sums(coords, [e for e in range(n) if cls >> e & 1])
            key = (bin(cls).count('1'), sum(r in sums for r in roots))
            tally[key] = tally.get(key, 0) + 1
    expected = {(7, 9): 360, (7, 11): 1080, (8, 15): 1440}
    checker.check(
        'root spans: 8-classes span all 15 roots; 7-classes span 9 or 11',
        tally == expected,
        f'{tally}',
    )
    return coords, minimal


def _check_nine_layers(
    checker: tools.Checker, coords: np.ndarray, minimal: list[int]
) -> None:
    """Run item 2 on the retained certificate."""
    n = 15
    full = (1 << n) - 1
    data = json.loads((_HERE / 'assets' / 'nine_layers.json').read_text())
    layers = [sum(1 << e for e in cls) for cls in data['color0_classes']]
    checker.check(
        'the certificate has nine layers', len(layers) == 9, f'observed {len(layers)}'
    )
    proper = all(
        not any(m & cls == m for m in minimal) for a in layers for cls in (a, full ^ a)
    )
    checker.check('every certificate layer is a proper 2-coloring of mu_15', proper)
    zero = np.zeros(coords.shape[1], dtype=np.int64).tobytes()
    for color in (0, 1):
        common = None
        sizes = []
        for a in layers:
            cls = a if color == 0 else full ^ a
            sums = _signed_sums(coords, [e for e in range(n) if cls >> e & 1])
            common = sums if common is None else common & sums
            sizes.append(len(common))
        print(f'nine layers, color {color}: intersection sizes {sizes}')
        checker.check(
            f'color {color}: signed-span intersection is zero',
            common == {zero},
            f'sizes {sizes}',
        )


def _check_arcs(checker: tools.Checker, conductors: list[int]) -> None:
    """Run item 3: arc classes below the rank span no outside root."""
    for m in conductors:
        phi = _cyclotomic(m)
        deg = len(phi) - 1
        height = max(abs(c) for c in phi[:deg])
        if height > _GUARD:
            raise OverflowError('polynomial coefficients could overflow')
        low = np.array(phi[:deg], dtype=np.int64)
        lengths = {q: math.ceil(m / q) for q in (3, 4)}
        spanned = dict.fromkeys(lengths, 0)
        # stream the coordinates of x^0, ..., x^(m-1) modulo Phi_m without storing them
        v = np.zeros(deg, dtype=np.int64)
        v[0] = 1
        for _ in range(m):
            if int(np.abs(v).max()) <= 1:
                top = int(np.flatnonzero(v).max())
                for q, length in lengths.items():
                    spanned[q] += int(top < length)
            v = _coordinate_step(v, low, height)
        for q, length in lengths.items():
            ok = length <= deg and spanned[q] == length
            print(
                f'arc M={m} q={q}: length {length}, phi {deg}, roots spanned {spanned[q]}'
            )
            checker.check(
                f'M={m}, q={q}: arc below rank spans exactly its own roots', ok
            )


def _check_pairs(checker: tools.Checker, conductor: int) -> None:
    """Run item 4 for the q = 3 arc class at one conductor."""
    m = conductor
    coords = _coordinates(_cyclotomic(m), m)
    length = math.ceil(m / 3)
    primes = [
        p
        for p in range(3, m + 1, 2)
        if m % p == 0 and all(p % r for r in range(3, int(p**0.5) + 1, 2))
    ]
    total: dict[tuple[tuple[int, ...], int], int] = {}
    inside: dict[tuple[tuple[int, ...], int], int] = {}
    for z in range(m):
        pattern = [tuple(int(z % p == w % p) for p in primes) for w in range(m)]
        for sign in (1, -1):
            rows = coords[z][None, :] + sign * coords
            ok = (np.abs(rows).max(axis=1) <= 1) & ~rows[:, length:].any(axis=1)
            for w in range(m):
                if w == z:
                    continue
                key = (pattern[w], sign)
                total[key] = total.get(key, 0) + 1
                inside[key] = inside.get(key, 0) + int(ok[w])
    coset = tuple(int(p != 3) for p in primes)
    worst = Fraction(0)
    for key, count in total.items():
        frac = Fraction(inside[key], count)
        if key == (coset, 1):
            checker.check(
                f'M={m}: pairs on a mu_3 coset with sign +1 survive with probability 1/3',
                frac == Fraction(1, 3),
                f'{frac}',
            )
        else:
            worst = max(worst, frac)
    print(
        f'pairs M={m}: largest survival over the other patterns {worst} = {float(worst):.4f}'
    )
    checker.check(
        f'M={m}: every other signed-pair pattern survives with probability at most 2/15',
        worst <= Fraction(2, 15),
        f'{worst}',
    )


def _equality_type(a: int, b: int, c: int) -> int:
    """Return the equality type of three residues: 0 all equal, 1-3 one pair, 4 distinct."""
    if a == b == c:
        return 0
    if a == b:
        return 1
    if a == c:
        return 2
    if b == c:
        return 3
    return 4


# for each equality type, which of the pairs (0,1), (0,2), (1,2) agree
_PAIR_AGREES = {0: (1, 1, 1), 1: (1, 0, 0), 2: (0, 1, 0), 3: (0, 0, 1), 4: (0, 0, 0)}


def _lower_complexity(
    primes: list[int], pattern: tuple[int, ...], signs: tuple[int, int, int]
) -> bool:
    """Return whether a signed triple of this orbit visibly has lower complexity.

    That happens when two equally signed points lie on one coset of mu_3 (their sum is
    minus the third point of the coset), when the three points form a coset of mu_3, or
    when three equally signed points lie on one coset of mu_5.
    """
    three = primes.index(3)
    others_equal = all(t == 0 for i, t in enumerate(pattern) if i != three)
    for k, (i, j) in enumerate(((0, 1), (0, 2), (1, 2))):
        agree = [_PAIR_AGREES[t][k] for t in pattern]
        if not agree[three] and all(
            agree[i2] for i2 in range(len(primes)) if i2 != three
        ):
            if signs[i] == signs[j]:
                return True
    if pattern[three] == 4 and others_equal:
        return True
    if 5 in primes:
        five = primes.index(5)
        if pattern[five] == 4 and all(
            t == 0 for i, t in enumerate(pattern) if i != five
        ):
            if len(set(signs)) == 1:
                return True
    return False


@cache
def _log_bounds(value: Fraction) -> tuple[Fraction, Fraction]:
    """Enclose log(value) for value >= 1 by exact rational series bounds."""
    if value < 1:
        raise ValueError('The logarithm enclosure requires an argument at least one')
    exponent = 0
    while value >= 2:
        value /= 2
        exponent += 1

    def series(z: Fraction) -> tuple[Fraction, Fraction]:
        # log((1+z)/(1-z)); the omitted positive terms have a geometric bound.
        terms = 32
        lower = 2 * sum(z ** (2 * j + 1) / (2 * j + 1) for j in range(terms))
        tail = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
        return lower, lower + tail

    lower, upper = series((value - 1) / (value + 1))
    two_lower, two_upper = series(Fraction(1, 3))
    return lower + exponent * two_lower, upper + exponent * two_upper


def _check_triples(checker: tools.Checker, conductor: int) -> None:
    """Run item 6: signed triples of distinct roots for the q = 3 arc class, exactly."""
    m = conductor
    coords = _coordinates(_cyclotomic(m), m)
    length = math.ceil(m / 3)
    primes = [p for p in (3, 5, 7, 11, 13) if m % p == 0]
    residues = np.array([[z % p for p in primes] for z in range(m)])
    total: dict[tuple[tuple[int, ...], tuple[int, int, int]], int] = {}
    inside: dict[tuple[tuple[int, ...], tuple[int, int, int]], int] = {}
    sign_patterns = [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1)]
    for z1 in range(m):
        for z2 in range(m):
            if z2 == z1:
                continue
            rest = [z for z in range(m) if z not in (z1, z2)]
            patterns = [
                tuple(
                    _equality_type(residues[z1][i], residues[z2][i], residues[z3][i])
                    for i in range(len(primes))
                )
                for z3 in rest
            ]
            for signs in sign_patterns:
                rows = (
                    signs[0] * coords[z1]
                    + signs[1] * coords[z2]
                    + signs[2] * coords[rest]
                )
                ok = (np.abs(rows).max(axis=1) <= 1) & ~rows[:, length:].any(axis=1)
                for pattern, good in zip(patterns, ok):
                    key = (pattern, signs)
                    total[key] = total.get(key, 0) + 1
                    inside[key] = inside.get(key, 0) + int(good)
    kappa = Fraction(length, m)
    worst = Fraction(0)
    binding = True
    conductor_lower, _ = _log_bounds(Fraction(m))
    _, root_upper = _log_bounds(1 / kappa)
    for key, count in total.items():
        if _lower_complexity(primes, key[0], key[1]):
            continue
        frac = Fraction(inside[key], count)
        worst = max(worst, frac)
        # the orbit needs no more layers than the roots: lambda <= |O|^(-log(1/kappa)/log m)
        if frac > 0:
            _, count_upper = _log_bounds(Fraction(count))
            survival_lower, _ = _log_bounds(1 / frac)
            binding &= count_upper * root_upper <= conductor_lower * survival_lower
    print(
        f'triples M={m}: largest survival over the remaining orbits {worst} = {float(worst):.4f}'
    )
    checker.check(
        f'M={m}: remaining signed-triple orbits survive with probability at most 4/45',
        worst <= Fraction(4, 45),
        f'{worst}',
    )
    checker.check(
        f'M={m}: no remaining signed-triple orbit needs more layers than the roots',
        binding,
    )


def _check_short_arcs(checker: tools.Checker) -> None:
    """Run item 5: D(165) = 81 and D(195) = 97."""
    for n in (165, 195):
        phi = _cyclotomic(n)
        deg = len(phi) - 1
        height = max(abs(c) for c in phi)
        product = _poly_mul([1, -1], phi)
        flat = max(abs(c) for c in product) <= 1
        # a flat multiple of degree phi(n) is an integer multiple of Phi_n, hence +-Phi_n
        checker.check(
            f'Phi_{n} has degree {deg} and height 2', height == 2, f'height {height}'
        )
        checker.check(
            f'(1 - x) Phi_{n} is flat of degree {deg + 1}',
            flat and len(product) - 1 == deg + 1,
        )
        print(
            f'D({n}) = {deg + 1}; two arcs proper iff 2 D(N) >= N: {2 * (deg + 1) >= n}'
        )
        checker.check(f'two arcs are not proper for mu_{n}', 2 * (deg + 1) < n)


def _check_first_moment(checker: tools.Checker) -> None:
    """Run item 7: exact numerical instances of the first-moment lower bound of Lemma 7."""
    grids = {1155: ([3, 5, 7, 11], 13), 15015: ([3, 5, 7, 11, 13], 17)}
    cases = [(1155, 2, 12, True), (1155, 3, 0, False)] + [
        (15015, q, 2479, True) for q in (2, 3, 4)
    ]
    for m, q, exponent, above in cases:
        primes, p = grids[m]
        group = math.prod(math.factorial(r) for r in primes)
        size = -(-m // q)
        # compare (2^|C| - 1) / |G|^(p - 1) with 2^exponent by cross-multiplying exact integers
        lhs = 2**size - 1
        rhs = 2**exponent * group ** (p - 1)
        label = 'exceeds' if above else 'is below'
        checker.check(
            f'M={m}, q={q}, p={p}: the Lemma 7 bound {label} 2^{exponent}',
            (lhs > rhs) == above,
        )


def _arc_test(length: int) -> Callable[[np.ndarray], np.ndarray]:
    """Return the membership test for the signed span of the arc of the first `length` roots below the rank."""

    def inside(total: np.ndarray) -> np.ndarray:
        # the arc lies in the power basis, so membership is ternary coordinates inside the arc
        return (np.abs(total) <= 1).all(axis=1) & ~total[:, length:].any(axis=1)

    return inside


def _independent_test(basis: np.ndarray) -> Callable[[np.ndarray], np.ndarray]:
    """Test signed-span membership exactly using a modular right inverse.

    Full row rank modulo the prime supplies a right inverse. A genuine
    ternary representation must be the recovered modular coefficient vector;
    converting residues 0, 1, -1 back to integers and multiplying by the
    original matrix then proves membership. No numerical rejection is used.
    """
    prime = 65521
    count, width = basis.shape
    reduced = [[int(x) % prime for x in row] for row in basis]
    operations = [[int(i == j) for j in range(count)] for i in range(count)]
    pivots = []
    for col in range(width):
        rank = len(pivots)
        pivot = next((r for r in range(rank, count) if reduced[r][col]), None)
        if pivot is None:
            continue
        reduced[rank], reduced[pivot] = reduced[pivot], reduced[rank]
        operations[rank], operations[pivot] = operations[pivot], operations[rank]
        inverse = pow(reduced[rank][col], -1, prime)
        reduced[rank] = [(x * inverse) % prime for x in reduced[rank]]
        operations[rank] = [(x * inverse) % prime for x in operations[rank]]
        for row in range(count):
            if row != rank:
                factor = reduced[row][col]
                reduced[row] = [
                    (x - factor * y) % prime
                    for x, y in zip(reduced[row], reduced[rank])
                ]
                operations[row] = [
                    (x - factor * y) % prime
                    for x, y in zip(operations[row], operations[rank])
                ]
        pivots.append(col)
        if len(pivots) == count:
            break
    if len(pivots) != count:
        raise ValueError('the membership matrix lacks full row rank modulo 65521')
    solve = np.zeros((width, count), dtype=np.int64)
    solve[pivots] = np.array(operations, dtype=np.int64)
    if width * int(np.max(np.abs(basis))) * (prime - 1) >= _GUARD:
        raise OverflowError('modular right-inverse verification could overflow')
    if not np.array_equal((basis @ solve) % prime, np.eye(count, dtype=np.int64)):
        raise ValueError('invalid modular right inverse')

    def inside(total: np.ndarray) -> np.ndarray:
        if width * int(np.max(np.abs(total), initial=0)) * (prime - 1) >= _GUARD:
            raise OverflowError('modular coefficient recovery could overflow')
        coefficients = (total @ solve) % prime
        coefficients[coefficients == prime - 1] = -1
        mask = (np.abs(coefficients) <= 1).all(axis=1)
        for j in np.flatnonzero(mask):
            mask[j] = bool((coefficients[j] @ basis == total[j]).all())
        return mask

    return inside


def _survivors(
    coords: np.ndarray,
    inside: Callable[[np.ndarray], np.ndarray],
    members: list[int],
    signs: list[int],
) -> list[tuple]:
    """Return the coordinate twists of mu_105 sending the signed sum into the signed span tested by `inside`."""
    primes = (3, 5, 7)
    grid = np.zeros(primes, dtype=np.int64)
    for e in range(105):
        grid[e % 3, e % 5, e % 7] = e
    perms7 = np.array(list(itertools.permutations(range(7))), dtype=np.int64)
    points = [(e % 3, e % 5, e % 7) for e in members]
    found = []
    for g3 in itertools.permutations(range(3)):
        for g5 in itertools.permutations(range(5)):
            total = np.zeros((len(perms7), coords.shape[1]), dtype=np.int64)
            for (a, b, c), sign in zip(points, signs):
                total += sign * coords[grid[g3[a], g5[b]][perms7[:, c]]]
            found.extend(
                (g3, g5, tuple(int(t) for t in perms7[j]))
                for j in np.flatnonzero(inside(total))
            )
    return found


def _affine_coset(perm: tuple) -> tuple:
    """Return the representative of the left coset perm . AGL(1, p) sending 0 to 0 and 1 to 1."""
    p = len(perm)
    inverse = {value: i for i, value in enumerate(perm)}
    shift = inverse[0]
    scale = (inverse[1] - shift) % p
    return tuple(perm[(scale * t + shift) % p] for t in range(p))


def _line_cover(support: list[int]) -> int:
    """Return the least number of grid lines of mu_105 covering the given exponents (at most 4 tried)."""
    points = [(e % 3, e % 5, e % 7) for e in support]
    # a line fixes all coordinates but one: key (direction, the other two coordinates)
    lines = {}
    for point in points:
        for i in range(3):
            lines.setdefault((i, point[:i] + point[i + 1 :]), set()).add(point)
    everything = set(points)
    for size in range(1, 5):
        for choice in itertools.combinations(lines.values(), size):
            if set().union(*choice) == everything:
                return size
    return 5


def _check_survival_sets(checker: tools.Checker, seeded: bool) -> None:
    """Run item 8: exhaustive survival sets at M = 105 for the arc class of 35 roots."""
    m, length = 105, 35
    coords = _coordinates(_cyclotomic(m), m)

    def as_exponents(twist: tuple) -> list[int]:
        g3, g5, g7 = twist
        crt = {(e % 3, e % 5, e % 7): e for e in range(m)}
        return [crt[(g3[e % 3], g5[e % 5], g7[e % 7])] for e in range(m)]

    identity = list(range(m))
    reflection = [(length - 1 - e) % m for e in range(m)]
    for label, signs in (
        ('all signs +1', [1] * length),
        ('alternating signs', [(-1) ** e for e in range(length)]),
    ):
        maps = sorted(
            as_exponents(t)
            for t in _survivors(coords, _arc_test(length), list(range(length)), signs)
        )
        print(f'survival M={m}: whole arc, {label}: {len(maps)} twists')
        checker.check(
            f'M={m}: the whole arc sum with {label} survives exactly the identity and the reflection',
            maps == sorted([identity, reflection]),
        )
    if not seeded:
        return
    rng = random.Random(105)
    # 11 is the next prime after 7: Lemma 9 needs fewer than 11 cosets for the step to 1155
    for size, bound, above in (
        (20, 11, False),
        (22, 11, False),
        (24, 11, False),
        (10, 11, True),
    ):
        counts = []
        for _ in range(4):
            members = rng.sample(range(length), size)
            signs = [rng.choice((-1, 1)) for _ in members]
            twists = _survivors(coords, _arc_test(length), members, signs)
            counts.append(
                len({(_affine_coset(g5), _affine_coset(g7)) for _, g5, g7 in twists})
            )
        print(f'survival M={m}: {size} arc points, affine cosets met {counts}')
        if above:
            checker.check(
                f'M={m}: seeded sums on {size} arc points meet at least {bound} affine cosets',
                min(counts) >= bound,
                f'{counts}',
            )
        else:
            checker.check(
                f'M={m}: seeded sums on {size} arc points meet fewer than {bound} affine cosets',
                max(counts) < bound,
                f'{counts}',
            )
    # the transition: at 17 points some survival sets are spread or use other representations
    rng = random.Random(1717)
    crt = {(e % 3, e % 5, e % 7): e for e in range(m)}
    counts, unnatural, widths = [], [], []
    for _ in range(10):
        members = rng.sample(range(length), 17)
        signs = [rng.choice((-1, 1)) for _ in members]
        twists = _survivors(coords, _arc_test(length), members, signs)
        counts.append(
            len({(_affine_coset(g5), _affine_coset(g7)) for _, g5, g7 in twists})
        )
        moved = 0
        for g3, g5, g7 in twists:
            image = {
                crt[(g3[e % 3], g5[e % 5], g7[e % 7])]: sign
                for e, sign in zip(members, signs)
            }
            if all(e < length for e in image):
                continue
            moved += 1
            # the relation between the twisted image and the representation inside the arc
            value = sum(sign * coords[e] for e, sign in image.items())
            relation = dict(image)
            for e in range(length):
                relation[e] = relation.get(e, 0) - int(value[e])
            support = [e for e, c in relation.items() if c]
            widths.append(_line_cover(support))
        unnatural.append(moved)
    print(
        f'survival M={m}: 17 arc points, affine cosets met {counts}, survivors leaving the arc {unnatural}, '
        f'lines covering their relations {widths}'
    )
    checker.check(
        f'M={m}: some seeded sum on 17 arc points meets at least 11 affine cosets',
        max(counts) >= 11,
        f'{counts}',
    )
    checker.check(
        f'M={m}: some seeded sum on 17 arc points survives a twist that moves its support off the arc',
        max(unnatural) > 0,
        f'{unnatural}',
    )
    checker.check(
        f'M={m}: every relation behind such a survivor lies on at most three grid lines',
        bool(widths) and max(widths) <= 3,
        f'{widths}',
    )


def _rank_mod(rows: np.ndarray, prime: int = 2147483647) -> int:
    """Return the rank of an integer matrix modulo a prime, a lower bound for its rational rank."""
    matrix = [[int(x) % prime for x in row] for row in rows]
    rank, columns = 0, len(matrix[0])
    for col in range(columns):
        pivot = next((r for r in range(rank, len(matrix)) if matrix[r][col]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][col], prime - 2, prime)
        for r in range(len(matrix)):
            if r != rank and matrix[r][col]:
                factor = matrix[r][col] * inverse % prime
                matrix[r] = [
                    (x - factor * y) % prime for x, y in zip(matrix[r], matrix[rank])
                ]
        rank += 1
    return rank


def _check_layered_survival(checker: tools.Checker, seeded: bool) -> None:
    """Run item 9: survival sets at M = 105 for the classes of a twisted layering of three arcs of mu_15."""
    coords15 = _coordinates(_cyclotomic(15), 15)
    coords = _coordinates(_cyclotomic(105), 105)
    crt15 = {(e % 3, e % 5): e for e in range(15)}
    rng = random.Random(3)
    twists = [(rng.sample(range(3), 3), rng.sample(range(5), 5)) for _ in range(7)]

    def layer(t: int, color: int) -> list[int]:
        g3, g5 = twists[t]
        return [e for e in range(15) if crt15[(g3[e % 3], g5[e % 5])] // 5 == color]

    zero = np.zeros(coords15.shape[1], dtype=np.int64).tobytes()
    robust = True
    for color in range(3):
        for dropped in range(-1, 7):
            common = None
            for t in range(7):
                if t != dropped:
                    sums = _signed_sums(coords15, layer(t, color))
                    common = sums if common is None else common & sums
            robust &= common == {zero}
    checker.check(
        'the seeded twisted layering of three arcs of mu_15 into mu_105 is proper and robust',
        robust,
    )
    classes = [[] for _ in range(3)]
    for e in range(105):
        g3, g5 = twists[e % 7]
        classes[crt15[(g3[e % 3], g5[e % 5])] // 5].append(e)
    ranks = [_rank_mod(coords[c]) for c in classes]
    checker.check(
        'its three classes have 35 linearly independent roots each',
        [len(c) for c in classes] == [35] * 3 and ranks == [35] * 3,
        f'{ranks}',
    )
    identity = [(0, 1, 2), (0, 1, 2, 3, 4), (0, 1, 2, 3, 4, 5, 6)]
    for index in range(3 if seeded else 1):
        inside = _independent_test(coords[classes[index]])
        found = _survivors(coords, inside, classes[index], [1] * 35)
        print(f'layered survival M=105: whole class {index}: {len(found)} twists')
        checker.check(
            f'the whole sum of layered class {index} survives only the identity',
            [list(map(tuple, t)) for t in found] == [identity],
        )
    if not seeded:
        return
    rng = random.Random(2010)
    for size, bound, above in ((20, 11, False), (10, 11, True)):
        counts = []
        for index in range(3):
            inside = _independent_test(coords[classes[index]])
            for _ in range(2):
                members = rng.sample(classes[index], size)
                signs = [rng.choice((-1, 1)) for _ in members]
                counts.append(len(_survivors(coords, inside, members, signs)))
        print(f'layered survival M=105: {size} class points, survivors {counts}')
        if above:
            checker.check(
                f'seeded sums on {size} points of the layered classes each survive at least {bound} twists',
                min(counts) >= bound,
                f'{counts}',
            )
        else:
            checker.check(
                f'seeded sums on {size} points of the layered classes each survive fewer than {bound} twists',
                max(counts) < bound,
                f'{counts}',
            )


def main() -> int:
    """Run every finite obligation and return the shared checker's exit code."""
    # parse the interface; quick mode drops the largest arc conductor
    parser = tools.evidence_parser(
        'Check the exact small cases of the twisted-layer note.'
    )
    args = parser.parse_args()
    checker = tools.Checker()
    coords, minimal = _check_mu15(checker)
    _check_nine_layers(checker, coords, minimal)
    arcs = [105, 165, 195, 1155, 15015] + ([] if args.quick else [255255])
    _check_arcs(checker, arcs)
    for conductor in (105, 1155):
        _check_pairs(checker, conductor)
    _check_triples(checker, 105)
    _check_short_arcs(checker)
    _check_first_moment(checker)
    _check_survival_sets(checker, seeded=not args.quick)
    _check_layered_survival(checker, seeded=not args.quick)
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

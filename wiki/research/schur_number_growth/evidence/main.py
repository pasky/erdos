"""Exact checks for the Schur-growth obstructions and reductions.

All arithmetic is exact (integers and fractions). Checked clauses:

O1  For X = {4^0, ..., 4^(n-1)}, 2 <= n <= 8: the difference map is
    injective, and every relation a + b = c among positive differences
    (a = b allowed) is an endpoint triangle; there are exactly C(n, 3).
B   Sparse power cells: for 1 <= n <= 5, q in {3, 4, 8} and
    b = max(4, n+2, q+1), enumerate all 0 <= y < b^n and check that the
    digit and digit-sum constraints of L266 select exactly {1,b,...,b^(n-1)}.
    Also check the GF(16) three-coloring of K_16: no monochromatic triangle,
    and each six-vertex subset has an edge of each color. Its transferred
    coloring of differences of sixteen powers of 18 is Schur-free. The
    three-box argument in L266 then gives a counterexample at rho = 1/3.
A   Block composition: compose(psi, phi) is Schur-free on [1, sP + t]
    (P = 2t + 1, x = y allowed) and uses both palettes in full, for every
    pair of Schur tripling colorings with one to four colors and for the
    retained Bohr coloring composed with a three-color tripling coloring.
C   The retained 20-color coloring psi of [1, 800] (assets/bohr_psi_m20.json)
    has each class in its retained rational-frequency Bohr arc (1/3,2/3),
    and is Schur-free with every color in [1, 45]. Composed with the four-color
    tripling coloring of [1, 39] (P = 79, prime) it is a Schur-free
    24-coloring of [1, 63239] whose longest color-omitting dilated prefix
    M is below delta N' for delta = 46/800, as Lemma C of the refutation of
    L260 predicts.
E   Arc rescaling: every closed arc [a, b] of [0, 1) with endpoints in
    (1/120)Z that is sum-free on the circle is sent into [1/8, 7/8] mod 1
    by the multiplier n chosen in Lemma 2 of the proof of L262.
T   Schur's tripling coloring with k <= 7 colors: class j lies in the
    sum-free arc {x : x mod 3^(j+1) in [(3^j + 1)/2, 3^j]}, doubling the
    frequency 3^-(j+1) sends the class into [1/3, 2/3] mod 1, and
    N + 1 <= 3^k.
Q   Signed cube Q_r^+ (vectors in {-1, 0, 1}^r whose last nonzero entry is
    1): for r <= 5 and b in {4, 5} the base-b map is injective and
    positive and carries v + w = u exactly to the Schur triples among its
    values; for q in {3, 4} and r <= 4 the 0/1 digit cube in base q + 1 is
    the Bohr cell {y : q (y mod b^l) < b^l for l <= r} and its positive
    differences are the image of Q_r^+; for r <= 6 the binary value and
    the support map are additive on triples; Q_3^+ has no Schur-free
    2-coloring; and explicit Schur-free colorings give chi_4 <= 3 (cubic
    residue classes of GF(16) through the support map), chi_5 <= 4 and
    chi_6 <= 5 (tripling colorings through the binary value), and
    chi_7 <= 5 (the retained four-coloring of [1, 44] in
    assets/schur_44.json, composed by Lemma A with one color on [1, 1] into
    a Schur-free five-coloring of [1, 133], through the binary value).
K   Twisted blocks of {0,1}^4: the retained coloring of Q_4^+
    (assets/twisted_cube_r4.json) is Schur-free; with the four blocks
    {(x1, x2, y1, y2) : x1 + y1 = s1, x2 + y2 = s2 mod 2} and the retained
    palettes it obeys rule (R) of the palette-rule page; one block uses all
    four colors on its internal pairs, and the sum over blocks of 2^|U_B| is
    28 > 2^4, so the Kraft inequality fails for these blocks. The coloring
    is a function neither of the support nor of the binary value. A control
    puts an internal color into a palette and checks that rule (R) then
    fails.

Finite checks illustrate proved lemmas; they prove no asymptotic statement.
Runtime: a few seconds. Command, from the repository root:
    uv run --no-sync python wiki/research/schur_number_growth/evidence/main.py
"""

from __future__ import annotations

import itertools
import json
import sys
from fractions import Fraction
from math import comb
from pathlib import Path

import numpy as np

from tools import Checker, evidence_parser

ASSET = Path(__file__).parent / 'assets' / 'bohr_psi_m20.json'
SCHUR_44 = Path(__file__).parent / 'assets' / 'schur_44.json'
TWISTED = Path(__file__).parent / 'assets' / 'twisted_cube_r4.json'


def schur_violation(colors: list) -> tuple | None:
    """Return a monochromatic (x, y, x + y) with x <= y, or None.

    colors[x] is the color of x for 1 <= x <= N; colors[0] is ignored.
    """
    n = len(colors) - 1
    arr = np.array([-1, *colors[1:]])
    for col in set(colors[1:]):
        mask = arr == col
        elems = np.nonzero(mask)[0]
        for x in elems:
            ys = elems[elems >= x]
            zs = ys + x
            hit = zs[zs <= n]
            hit = hit[mask[hit]]
            if hit.size:
                return int(x), int(hit[0] - x), int(hit[0])
    return None


def tripling(k: int) -> list:
    """Return Schur's tripling coloring of [1, (3^k - 1)/2] with k colors."""
    colors = [None, 0]
    for col in range(1, k):
        n = len(colors) - 1
        colors = colors + [col] * (n + 1) + colors[1:]
    return colors


def compose(psi: list, phi: list, shift: int) -> list:
    """Return the block composition c'(aP + r) of Lemma A.

    psi colors [1, s], phi colors [1, t]; phi's colors are offset by shift so
    that the palettes are disjoint. Residues r lie in [-t, t].
    """
    s, t = len(psi) - 1, len(phi) - 1
    p = 2 * t + 1
    out = [None]
    for x in range(1, s * p + t + 1):
        a, r = divmod(x + t, p)
        r -= t
        out.append(phi[r] + shift if r >= 1 else psi[a])
    return out


def prefix_statistic(colors: list) -> int:
    """Return M: the longest dilated prefix d, 2d, ..., md omitting a used color."""
    n = len(colors) - 1
    used = set(colors[1:])
    best = 0
    for d in range(1, n + 1):
        length = n // d
        if length <= best:
            break
        first = {}
        for j in range(1, length + 1):
            first.setdefault(colors[j * d], j)
            if len(first) == len(used):
                break
        value = length if len(first) < len(used) else max(first.values()) - 1
        best = max(best, value)
    return best


def check_base_four(checker: Checker) -> None:
    """O1: relations among base-four differences are endpoint triangles."""
    for n in range(2, 9):
        pairs = {4**u - 4**v: (u, v) for u in range(n) for v in range(u)}
        injective = len(pairs) == comb(n, 2)
        relations = 0
        all_triangles = True
        diffs = sorted(pairs)
        for i, a in enumerate(diffs):
            for b in diffs[i:]:
                if a + b in pairs:
                    relations += 1
                    (ua, va), (ub, vb), (uc, vc) = pairs[a], pairs[b], pairs[a + b]
                    triangle = (va == ub and ua == uc and vb == vc) or (
                        vb == ua and ub == uc and va == vc
                    )
                    all_triangles = all_triangles and triangle
        checker.check(
            f'O1 n={n}: injective, all {relations} relations are triangles, count C(n,3)',
            injective and all_triangles and relations == comb(n, 3),
        )


def check_power_cells(checker: Checker) -> None:
    """B: exact cells and a finite Ramsey instance of the uniform obstruction."""
    for n, q in itertools.product(range(1, 6), (3, 4, 8)):
        base = max(4, n + 2, q + 1)
        moduli = [base**level for level in range(1, n + 1)]
        cell = {
            y
            for y in range(base**n)
            if all((base - 1) * (y % mod) < mod for mod in moduli)
            and y % (base - 1) == 1
        }
        powers = {base**j for j in range(n)}
        checker.check(
            f'B n={n}, q={q}, b={base}: digit-sum cell equals the {n} powers',
            cell == powers and base - 1 >= q,
        )

    classes = gf16_cubic_classes()
    valid = set(classes) == set(range(1, 16)) and set(classes.values()) == {0, 1, 2}
    checker.check(
        'B GF(16) rule colors all nonzero differences with three colors', valid
    )
    if not valid:
        return
    triangle_free = all(
        not (classes[a ^ b] == classes[a ^ c] == classes[b ^ c])
        for a, b, c in itertools.combinations(range(16), 3)
    )
    every_six = all(
        {classes[a ^ b] for a, b in itertools.combinations(vertices, 2)} == {0, 1, 2}
        for vertices in itertools.combinations(range(16), 6)
    )
    checker.check(
        'B K_16: no monochromatic triangle; all 8008 six-sets have every color',
        triangle_free and every_six,
    )
    diffs = {18**u - 18**v: classes[u ^ v] for u in range(16) for v in range(u)}
    relations = [
        (a, b, a + b) for a in diffs for b in diffs if a <= b and a + b in diffs
    ]
    checker.check(
        'B sixteen powers of 18: 120 differences, 560 Schur triples, none monochromatic',
        len(diffs) == 120
        and len(relations) == comb(16, 3)
        and all(not (diffs[a] == diffs[b] == diffs[c]) for a, b, c in relations),
    )


def check_composition(checker: Checker, psi_bohr: list) -> None:
    """A: block composition is Schur-free with both palettes in full."""
    for kp, kf in itertools.product(range(1, 5), repeat=2):
        psi, phi = tripling(kp), tripling(kf)
        out = compose(psi, phi, kp)
        s, t = len(psi) - 1, len(phi) - 1
        ok = schur_violation(out) is None and len(out) - 1 == s * (2 * t + 1) + t
        checker.check(
            f'A tripling {kp} + {kf} colors: Schur-free on [1,{len(out) - 1}], {kp + kf} colors',
            ok and len(set(out[1:])) == kp + kf,
        )
    out = compose(psi_bohr, tripling(3), 20)
    checker.check(
        f'A Bohr psi + tripling 3 colors: Schur-free on [1,{len(out) - 1}], 23 colors',
        schur_violation(out) is None and len(set(out[1:])) == 23,
    )


def check_lemma_c(checker: Checker, psi: list) -> None:
    """C: the composite has a small dilated-prefix statistic."""
    first = {}
    for x in range(1, len(psi)):
        first.setdefault(psi[x], x)
    depth = max(first.values())
    checker.check(
        'C psi Schur-free on [1,800], 20 colors, depth 45',
        schur_violation(psi) is None and len(first) == 20 and depth == 45,
    )
    phi = tripling(4)[:40]
    p = 2 * 39 + 1
    prime = all(p % q for q in range(2, p))
    out = compose(psi, phi, 20)
    n_out = len(out) - 1
    delta = Fraction(depth + 1, 800)
    checker.check(
        'C hypotheses: P=79 prime, delta*s >= depth+1, t+1 >= 1/delta',
        prime and delta * 800 >= depth + 1 and 1 / delta <= 40,
    )
    checker.check(
        f'C composite Schur-free on [1,{n_out}] with 24 colors',
        n_out == 63239 and schur_violation(out) is None and len(set(out[1:])) == 24,
    )
    m_value = prefix_statistic(out)
    checker.check(
        f"C M = {m_value} < delta N' = {float(delta * n_out):.1f}",
        m_value == 3515 and m_value < delta * n_out,
    )
    # negative control: the statistic sees the late color of a tripling coloring
    checker.check(
        'C control: M of tripling 4 colors on [1,40] is 13',
        prefix_statistic(tripling(4)) == 13,
    )


def check_arc_rescaling(checker: Checker) -> None:
    """E: the multiplier of L262's Lemma 2 sends each sum-free rational arc into [1/8, 7/8]."""
    q = 120
    tested = 0
    good = True
    for ia in range(q):
        for ib in range(ia, q):
            a, b = Fraction(ia, q), Fraction(ib, q)
            # a closed arc [a, b] is sum-free on the circle iff b < 2a and 2b < 1 + a
            if not (b < 2 * a and 2 * b < 1 + a):
                continue
            tested += 1
            lo, hi = (a, b) if a + b <= 1 else (1 - b, 1 - a)
            n = 1 if lo >= Fraction(1, 8) else int(1 / (4 * lo))
            u, v = n * lo, n * hi
            j = u.numerator // u.denominator
            good = good and u - j >= Fraction(1, 8) and v - j <= Fraction(7, 8)
    checker.check(
        f'E all {tested} sum-free arcs with denominator 120 are rescaled into [1/8,7/8]',
        good and tested > 0,
    )


def check_tripling_arcs(checker: Checker) -> None:
    """T: tripling classes lie in sum-free arcs; doubling gives radius 1/3."""
    for k in range(1, 8):
        colors = tripling(k)
        n = len(colors) - 1
        ok = True
        for x in range(1, n + 1):
            j = colors[x]
            mod = 3 ** (j + 1)
            res = x % mod
            ok = ok and (3**j + 1) <= 2 * res <= 2 * 3**j
            # doubling: 2 res / 3^(j+1) lies in [1/3, 2/3]
            ok = ok and mod <= 3 * ((2 * res) % mod) <= 2 * mod
        # the closed arc [alpha, 1/3] is sum-free iff 1/3 < 2 alpha and 2/3 < 1 + alpha
        alphas = [Fraction(3**j + 1, 2 * 3 ** (j + 1)) for j in range(k)]
        arcs_sum_free = all(
            Fraction(1, 3) < 2 * a and Fraction(2, 3) < 1 + a for a in alphas
        )
        checker.check(
            f'T k={k}: classes in arcs, doubled into [1/3,2/3], N+1={n + 1} <= 3^k',
            ok and arcs_sum_free and n + 1 <= 3**k,
        )


def cube(r: int) -> list:
    """Return Q_r^+: vectors in {-1,0,1}^r whose last nonzero entry is 1."""
    out = []
    for v in itertools.product((-1, 0, 1), repeat=r):
        nonzero = [x for x in v if x]
        if nonzero and nonzero[-1] == 1:
            out.append(v)
    return out


def cube_triples(r: int) -> list:
    """Return all (v, w, u) in Q_r^+ with v + w = u coordinatewise."""
    members = set(cube(r))
    out = []
    for v in members:
        for w in members:
            u = tuple(a + b for a, b in zip(v, w, strict=True))
            if u in members:
                out.append((v, w, u))
    return out


def value(v: tuple, base: int) -> int:
    """Return sum v_i base^i."""
    return sum(x * base**i for i, x in enumerate(v))


def support(v: tuple) -> int:
    """Return the bitmask of nonzero coordinates."""
    return sum(1 << i for i, x in enumerate(v) if x)


def colorable_cube(coloring: dict, triples: list) -> bool:
    """Return whether no triple is monochromatic."""
    return all(not (coloring[v] == coloring[w] == coloring[u]) for v, w, u in triples)


def gf16_cubic_classes() -> dict:
    """Return the coset index of each nonzero element of GF(16) modulo cubes."""
    # GF(16) = F_2[x]/(x^4 + x + 1), whose class of x is primitive
    elem, out = 1, {}
    for e in range(15):
        out[elem] = e % 3
        elem <<= 1
        if elem & 0b10000:
            elem ^= 0b10011
    return out


def check_cube(checker: Checker, schur_44: list) -> None:
    """Q: the signed-cube embeddings, the digit cell, the maps and witnesses."""
    for r, base in itertools.product(range(1, 6), (4, 5)):
        members = cube(r)
        member_set = set(members)
        image = {value(v, base): v for v in members}
        ok = (
            len(image) == len(members) and min(image) >= 1 and max(image) <= base**r - 1
        )
        for v in members:
            for w in members:
                z = value(v, base) + value(w, base)
                u = tuple(a + b for a, b in zip(v, w, strict=True))
                ok = (
                    ok
                    and ((z in image) == (u in member_set))
                    and (z not in image or image[z] == u)
                )
        checker.check(
            f'Q base {base}, r={r}: injective, positive, triples correspond exactly', ok
        )
    for q, r in itertools.product((3, 4), range(1, 5)):
        base = q + 1
        cell = {
            y
            for y in range(base**r)
            if all(q * (y % base**level) < base**level for level in range(1, r + 1))
        }
        digit_cube = {value(d, base) for d in itertools.product((0, 1), repeat=r)}
        differences = {y - x for x in digit_cube for y in digit_cube if y > x}
        image = {value(v, base) for v in cube(r)}
        checker.check(
            f'Q q={q}, r={r}: digit cube is the Bohr cell, differences are the cube image',
            cell == digit_cube and differences == image,
        )
    for r in range(1, 7):
        ok = True
        for v, w, u in cube_triples(r):
            ok = ok and value(v, 2) + value(w, 2) == value(u, 2)
            ok = ok and support(v) ^ support(w) == support(u)
        ok = ok and all(1 <= value(v, 2) <= 2**r - 1 and support(v) for v in cube(r))
        checker.check(f'Q r={r}: binary value and support are additive on triples', ok)
    members, triples = cube(3), cube_triples(3)
    two_colorable = any(
        colorable_cube(dict(zip(members, bits, strict=True)), triples)
        for bits in itertools.product((0, 1), repeat=len(members))
    )
    checker.check(
        'Q no Schur-free 2-coloring of Q_3^+ (chi_3 >= 3)',
        not two_colorable and len(members) == 13,
    )
    classes = gf16_cubic_classes()
    sum_free = all(
        classes[a ^ b] != classes[a]
        for a in classes
        for b in classes
        if classes[a] == classes[b] and a != b
    )
    coloring = {v: classes[support(v)] for v in cube(4)}
    checker.check(
        'Q chi_4 <= 3: GF(16) cubic classes are sum-free and pull back',
        sum_free and colorable_cube(coloring, cube_triples(4)),
    )
    for r, k in ((5, 4), (6, 5)):
        colors = tripling(k)
        coloring = {v: colors[value(v, 2)] for v in cube(r)}
        checker.check(
            f'Q chi_{r} <= {k}: tripling coloring of [1,{len(colors) - 1}] pulls back',
            2**r - 1 <= len(colors) - 1 and colorable_cube(coloring, cube_triples(r)),
        )
    checker.check(
        'Q retained coloring of [1,44] is Schur-free with 4 colors',
        schur_violation(schur_44) is None and len(set(schur_44[1:])) == 4,
    )
    colors = compose([None, 0], schur_44, 1)
    coloring = {v: colors[value(v, 2)] for v in cube(7)}
    checker.check(
        'Q chi_7 <= 5: Lemma A gives a Schur-free 5-coloring of [1,133] that pulls back',
        len(colors) - 1 == 133
        and schur_violation(colors) is None
        and len(set(colors[1:])) == 5
        and colorable_cube(coloring, cube_triples(7)),
    )


def canonical(v: tuple) -> tuple:
    """Return the representative of {v, -v} whose last nonzero entry is 1."""
    for x in reversed(v):
        if x:
            return v if x == 1 else tuple(-a for a in v)
    raise ValueError('zero vector')


def twisted_block(x: tuple) -> tuple:
    """Return s with x in {(x1, x2, y1, y2) : x1 + y1 = s1, x2 + y2 = s2 mod 2}."""
    return (x[0] ^ x[2], x[1] ^ x[3])


def rule_r_holds(coloring: dict, palettes: dict) -> bool:
    """Check rule (R) on every pair of {0,1}^4 for the twisted blocks."""
    points = list(itertools.product((0, 1), repeat=4))
    for x, y in itertools.combinations(points, 2):
        color = coloring[canonical(tuple(b - a for a, b in zip(x, y, strict=True)))]
        bx, by = twisted_block(x), twisted_block(y)
        if bx == by:
            if color in palettes[bx]:
                return False
        elif (color in palettes[bx]) == (color in palettes[by]):
            return False
    return True


def check_twisted_cube(checker: Checker, data: dict) -> None:
    """K: twisted blocks of {0,1}^4 escape the Kraft inequality."""
    members = cube(4)
    coloring = {tuple(v): c for v, c in data['coloring']}
    palettes = {
        tuple(int(ch) for ch in key): set(colors)
        for key, colors in data['palettes'].items()
    }
    colors = data['colors']
    valid = (
        data['r'] == 4
        and colors == 4
        and len(data['coloring']) == len(members) == 40
        and sorted(coloring) == sorted(members)
        and set(coloring.values()) == set(range(colors))
        and set(palettes) == set(itertools.product((0, 1), repeat=2))
        and all(p <= set(range(colors)) for p in palettes.values())
    )
    checker.check(
        'K input: one color in 0..3 for each of the 40 vectors, all used', valid
    )
    if not valid:
        return
    inside = {s: set() for s in palettes}
    points = list(itertools.product((0, 1), repeat=4))
    for x, y in itertools.combinations(points, 2):
        if twisted_block(x) == twisted_block(y):
            difference = tuple(b - a for a, b in zip(x, y, strict=True))
            inside[twisted_block(x)].add(coloring[canonical(difference)])
    kraft = sum(2 ** len(used) for used in inside.values())
    checker.check(
        'K the retained coloring of Q_4^+ is Schur-free',
        colorable_cube(coloring, cube_triples(4)),
    )
    checker.check(
        'K rule (R) holds for the twisted blocks and the retained palettes',
        rule_r_holds(coloring, palettes),
    )
    mutated = dict(palettes)
    mutated[(0, 0)] = palettes[(0, 0)] | {coloring[(0, 1, 0, 1)]}
    checker.check(
        'control: rule (R) fails once an internal color enters a palette',
        not rule_r_holds(coloring, mutated),
    )
    checker.check(
        f'K block (0,0) uses all four colors inside; sum of 2^|U_B| is {kraft} > 2^4',
        inside[(0, 0)] == set(range(colors)) and kraft == 28 > 2**colors,
    )
    checker.check(
        'K the coloring is not a function of the support or of the binary value',
        any(
            support(v) == support(w) and coloring[v] != coloring[w]
            for v in members
            for w in members
        )
        and any(
            value(v, 2) == value(w, 2) and coloring[v] != coloring[w]
            for v in members
            for w in members
        ),
    )


def main() -> int:
    """Check the retained inputs and all documented finite obligations."""
    evidence_parser(__doc__, quick=False).parse_args()
    checker = Checker()
    data = json.loads(ASSET.read_text())
    psi = [None, *data['colors']]
    valid = data['m'] == 20 and data['s'] == 800 and len(psi) == 801
    valid = valid and all(type(c) is int and 0 <= c < 20 for c in psi[1:])
    data_44 = json.loads(SCHUR_44.read_text())
    schur_44 = [None, *data_44['colors']]
    valid_44 = data_44['n'] == 44 and len(schur_44) == 45
    valid_44 = valid_44 and all(type(c) is int and 0 <= c < 4 for c in schur_44[1:])
    checker.check('input: 800 colors in 0..19', valid)
    checker.check('input: 44 colors in 0..3', valid_44)
    if not (valid and valid_44):
        return checker.finish()
    frequencies = data['frequencies']
    valid_frequencies = len(frequencies) == 20 and all(
        len(pair) == 2 and all(type(x) is int for x in pair) and 0 <= pair[0] < pair[1]
        for pair in frequencies
    )
    checker.check('input: 20 exact rational frequencies in [0,1)', valid_frequencies)
    if not valid_frequencies:
        return checker.finish()
    checker.check(
        'C each retained Bohr color lies in its exact rational arc (1/3,2/3)',
        all(
            den < 3 * ((num * x) % den) < 2 * den
            for x, color in enumerate(psi[1:], 1)
            for num, den in [frequencies[color]]
        ),
    )
    checker.check(
        'control: the Schur test counts equal summands',
        schur_violation([None, 0, 0]) == (1, 1, 2),
    )
    check_base_four(checker)
    check_power_cells(checker)
    check_composition(checker, psi)
    check_lemma_c(checker, psi)
    check_arc_rescaling(checker)
    check_tripling_arcs(checker)
    check_cube(checker, schur_44)
    check_twisted_cube(checker, json.loads(TWISTED.read_text()))
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

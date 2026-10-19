"""Check the finite data recorded on the bounded-blocking research account.

Checked clauses:

1. Cap-four witnesses. For each order q in {5, 7, 11}, the point set in
   ``assets/cap4_witnesses.json`` consists of distinct normalized points of
   PG(2, q), meets every one of the q^2 + q + 1 lines in at least one and at
   most four points, has the recorded size and the recorded numbers t_1, ...,
   t_4 of lines meeting it in 1, ..., 4 points, and satisfies the necessary
   size interval of the incidence-moment bound at cap four. For q = 11 every
   point of the set lies on exactly four lines of each of the sizes 1, 3 and 4.
2. Three conics. For h = 2, ..., 7 (q = 4, ..., 128), with g the class of the
   indeterminate in GF(2^h), the union S of the conics gamma X^2 = Y Z for
   gamma in {1, g, 1 + g} has 3q - 1 points and meets every line of PG(2, q)
   in at least one and at most six points, with six attained for h >= 3.
   Negative control: for h = 3, ..., 7 the conics with gamma in {1, g, g^2},
   whose coefficients do not sum to zero, leave at least one line uncovered.
3. Heuristic orders. The first-moment heuristic of ``util/heuristic.py``
   gives, for caps 5, 6, 7 and 8, maximizing mean loads 2.5, 2.95, 3.35 and
   3.75 and crossover orders that round to 23, 70, 168 and 360.
4. Singer-invariant sets. For each entry of ``assets/singer_witnesses.json``
   the cubic defines a Singer cycle of PG(2, p) (``util/singer.py``), the
   trace-zero set D is a planar difference set, and the union of the listed
   residue classes modulo M has |K| N / M distinct points meeting every line
   in 1 to cap points, by direct incidence counts. The multiset of these
   loads equals the multiset of the circulant loads sum_{r in K} mu(r - t),
   each taken N / M times, which checks the reduction to Z/M. For the
   recorded cases (p, M, cap) without a witness, the exact search of
   ``singer.cover_search`` exhausts the invariant sets and finds none. The
   symmetric first-moment estimates recorded on the account are reproduced
   to the quoted rounding.
5. Single orbits. For every prime p from 5 to 2000 and every divisor m >= 2 of N
   with m <= p + 1 <= 8 m, ``util/orbitscan.c`` computes the least and
   largest number of elements of D in a residue class modulo m. There are
   269 such pairs; in 68 every class is hit; and the pairs with every class
   hit at most 8 times are exactly (p, m, largest count) = (7, 3, 4),
   (13, 3, 7), (37, 7, 8), (67, 21, 6), (79, 21, 6), (83, 19, 8) and
   (283, 73, 8); for p > 1500 the least largest count among pairs with every
   class hit is 11. For p <= 100 the counts agree with ``util/singer.py``.
   ``--quick`` runs only the Python comparison range, p <= 100.
6. Maximal arcs. For h = 2, ..., 5 and every r = 1, ..., h - 1, construct
   the degree-d arc Q(x,y) in H of ``completion_obstruction.md``, where
   q = 2^h, d = 2^r, and H is the span of the first r polynomial basis
   vectors. Check its size, every line's load in {0,d}, its exact number
   of empty lines, and exactly q+1-q/d saturated lines through each outside
   point. These are finite incidence checks of the objects in the proof,
   not exhaustive checks of exchanges or a result for every order.
7. Pencil counts for conics. For p in {31, 37, 41, 43} and m in {1, 2, 3},
   take the first m distinct nondegenerate conics of a seeded generator
   (``util/pencil.py``) and count, by direct incidence, the lines missing
   their union Y and, for every point P off Y, the number N_P of those lines
   through P. Check that |N_P - (p + 1)/2^m| <= m sqrt(p) + 2m + 1 except at
   at most binom(2m(m - 1), 2) points; that for m = 1 every N_P is
   (p - 1)/2 or (p + 1)/2, and there are p(p - 1)/2 missed lines; and that
   the number of missed lines is at least the lower bound derived from these
   pencil bounds in the proof on ``pencil_threshold.md``. Control: for
   p = 151 the conics x^2 + y^2 = z^2 and x^2 + y^2 = 4 z^2 have at least
   (p - 3)/2 missed lines through the origin, outside the pencil bound, so
   the exceptional set is needed. ``--quick`` runs only p = 31.
8. Pencil counts for cubics. For p = 211 and the cubics x^3 + y^3 + z^3
   (Fermat), y^2 z - x^3 - x^2 z (nodal), y^2 z - x^3 (cuspidal) and
   y^2 z - x^3 - 3 x z^2 - 5 z^3 (smooth), every point P off the curve
   satisfies |N_P - p/3| <= 2 sqrt(p), except for exactly 3, 3, 1 and 0
   points respectively, each with N_P > p/2. For the Fermat cubic the
   exceptions are the three coordinate points, from which the projection
   is a cyclic cover. For two unions, Fermat with x^2 + y^2 - 3 z^2 and the
   smooth cubic with x^3 + 2 y^3 + 7 z^3 + x y z, every point off the union
   satisfies |N_P - alpha p| <= 2 sqrt(p), with alpha = 1/6 and 1/9, except
   exactly 2 and 0 points. ``util/pencil.curve_pencil_counts`` computes N_P with
   numpy integer arithmetic; for the Fermat cubic at p = 31 it is compared
   with the direct incidence counts of clause 7's routines.

Run from the repository root:
    uv run --no-sync python wiki/research/leads/projective_plane_bounded_blocking/evidence/main.py

Dependencies: the root ``tools`` package, and for clause 5 a C compiler on
PATH (``cc``, ``clang`` or ``gcc``). Clauses 1 and 2
use exact finite-field arithmetic by tables; clause 3 is floating point and
heuristic, so it checks the quoted rounded values only; clauses 4 and 5 are
exact apart from the heuristic estimates; clauses 6 and 7 are exact, apart
from the floating-point square roots in the bounds of clauses 7 and 8,
which are compared with integer counts. The full run takes under a minute
on one core and writes its compiled scanner to ignored ``output/``.
``--quick`` restricts clause 2 to h <= 5 and clause 5 to p <= 100, in about
twenty seconds. Limitation: clauses 1 and 2 are finite checks; the three-conic
statement for every h rests on the proof on the account's parity page, which
this program does not replace.
"""

from __future__ import annotations

import json
import math
import shutil
import subprocess
import sys
from pathlib import Path

from tools import Checker, evidence_parser

sys.path.insert(0, str(Path(__file__).resolve().parent / 'util'))
import geometry
import heuristic
import pencil
import singer

__all__ = [
    'main',
]

_HERE = Path(__file__).resolve().parent

# recorded sizes and line types (t_1, t_2, t_3, t_4) of the cap-four witnesses
_WITNESS = {
    5: (14, (7, 4, 11, 9)),
    7: (17, (21, 7, 15, 14)),
    11: (21, (84, 0, 28, 21)),
}

# recorded (cap, maximizing mean load, rounded crossover order)
_HEURISTIC = [(5, 2.5, 23), (6, 2.95, 70), (7, 3.35, 168), (8, 3.75, 360)]

# (p, M, cap) with no invariant set, by exhaustive search
_EXHAUSTED = [(11, 19, 3), (13, 61, 4), (37, 67, 5), (47, 61, 5), (61, 97, 6), (67, 93, 6)]

# single orbits: (pairs, pairs with every class hit, blocking pairs (p, m, largest count) with cap <= 8)
_ORBITS = (269, 68, {(7, 3, 4), (13, 3, 7), (37, 7, 8), (67, 21, 6), (79, 21, 6), (83, 19, 8), (283, 73, 8)})

# (p, M, cap, rounded log10 of the symmetric estimate)
_SYMMETRIC = [
    (11, 19, 4, -1.0),
    (13, 61, 4, -2.2),
    (23, 79, 5, 2.3),
    (29, 67, 5, -0.5),
    (37, 67, 5, -3.2),
    (47, 61, 5, -3.5),
    (31, 331, 6, 25.9),
    (37, 201, 6, 11.0),
    (61, 97, 6, 0.0),
    (67, 93, 6, -0.9),
    (67, 147, 6, -0.8),
]


def _witnesses(checker: Checker) -> None:
    """Check clause 1 on the retained witnesses."""
    data = json.loads((_HERE / 'assets' / 'cap4_witnesses.json').read_text())
    checker.check('witness orders are 5, 7, 11', sorted(int(k) for k in data) == sorted(_WITNESS))
    for q, (size, types) in _WITNESS.items():
        entry = data[str(q)]
        field = geometry.Field(q, 1)
        pts = [tuple(v) for v in entry['points']]
        valid = all(len(v) == 3 and all(0 <= c < q for c in v) and geometry.normalize(field, v) == v for v in pts)
        checker.check(f'q={q}: points are normalized', valid)
        checker.check(f'q={q}: points are distinct', len(set(pts)) == len(pts))
        checker.check(f'q={q}: size {size}', len(pts) == size, f'size {len(pts)}')
        loads = geometry.line_loads(field, pts)
        lo, hi = min(loads.values()), max(loads.values())
        checker.check(f'q={q}: every line meets the set in 1 to 4 points', lo >= 1 and hi <= 4, f'range {lo}..{hi}')
        counts = geometry.type_counts(loads)
        got = tuple(counts.get(i, 0) for i in range(1, 5))
        checker.check(f'q={q}: line types {types}', got == types, f'types {got}')
        # the moment bound s^2 - (4(q+1)+1)s + 4(q^2+q+1) <= 0
        s = len(pts)
        checker.check(f'q={q}: size lies in the cap-four interval', s * s - (4 * (q + 1) + 1) * s + 4 * (q * q + q + 1) <= 0)
        if q == 11:
            profiles = set()
            for x, y, z in pts:
                through = [ln for ln in loads if (ln[0] * x + ln[1] * y + ln[2] * z) % q == 0]
                profiles.add(tuple(sum(1 for ln in through if loads[ln] == i) for i in range(1, 5)))
            checker.check('q=11: every point lies on 4 lines of sizes 1, 3 and 4 each', profiles == {(4, 0, 4, 4)}, f'profiles {profiles}')


def _conic_union(field: geometry.Field, gammas: list[int]) -> list[tuple[int, int, int]]:
    """Return the points of PG(2, q) on gamma X^2 = Y Z for some listed gamma."""
    mul = field.mul
    return [(x, y, z) for x, y, z in geometry.plane_points(field) if any(mul[g][mul[x][x]] == mul[y][z] for g in gammas)]


def _three_conics(checker: Checker, top: int) -> None:
    """Check clause 2 for h = 2, ..., top."""
    for h in range(2, top + 1):
        field = geometry.Field(2, h)
        q, g = field.q, 2
        gammas = [1, g, field.add[1][g]]
        pts = _conic_union(field, gammas)
        loads = geometry.line_loads(field, pts)
        lo, hi = min(loads.values()), max(loads.values())
        checker.check(f'h={h}: three conics have 3q - 1 = {3 * q - 1} points', len(pts) == 3 * q - 1, f'{len(pts)} points')
        checker.check(f'h={h}: every line meets the union in 1 to 6 points', lo >= 1 and hi <= 6, f'range {lo}..{hi}')
        if h >= 3:
            checker.check(f'h={h}: six is attained', hi == 6, f'max {hi}')
            control = _conic_union(field, [1, g, field.mul[g][g]])
            uncovered = sum(1 for v in geometry.line_loads(field, control).values() if v == 0)
            checker.check(f'h={h}: control without the relation leaves a line uncovered', uncovered > 0, f'{uncovered} uncovered')


def _maximal_arcs(checker: Checker) -> None:
    """Check clause 6 by direct incidence counts, including all outside pencils."""
    for h in range(2, 6):
        field = geometry.Field(2, h)
        q, add, mul = field.q, field.add, field.mul

        def trace(x: int) -> int:
            value, term = 0, x
            for _ in range(h):
                value = add[value][term]
                term = mul[term][term]
            return value

        alpha = next(x for x in range(q) if trace(x) == 1)
        all_points = geometry.plane_points(field)
        for r in range(1, h):
            d = 2**r
            # With binary polynomial-basis encoding, 0 <= x < 2^r is
            # the additive span of 1, g, ..., g^(r-1).
            pts = [(x, y, 1) for x in range(q) for y in range(q) if add[add[mul[x][x]][mul[x][y]]][mul[alpha][mul[y][y]]] < d]
            loads = geometry.line_loads(field, pts)
            types = geometry.type_counts(loads)
            tag = f'q={q} d={d}: maximal arc'
            checker.check(f'{tag} size', len(pts) == (d - 1) * q + d, f'{len(pts)} points')
            checker.check(f'{tag} loads are 0 or d', set(types) == {0, d}, f'{types}')
            checker.check(f'{tag} number of empty lines', types.get(0) == q * (q + 1 - d) // d)
            outside = set(all_points) - set(pts)
            saturated = [line for line, load in loads.items() if load == d]
            degrees = {
                sum(add[add[mul[a][x]][mul[b][y]]][mul[c][z]] == 0 for a, b, c in saturated)
                for x, y, z in outside
            }
            checker.check(f'{tag} outside saturated pencils', degrees == {q + 1 - q // d}, f'{degrees}')


def _heuristic(checker: Checker) -> None:
    """Check clause 3."""
    for cap, k, q in _HEURISTIC:
        got_k, _, got_q = heuristic.heuristic_order(cap)
        checker.check(f'cap {cap}: mean load {k}, crossover order about {q}', abs(got_k - k) < 1e-9 and round(got_q) == q, f'K={got_k}, q*={got_q:.2f}')


def _planar(p: int, diff: list[int]) -> bool:
    """Return whether the nonzero differences of diff are the N - 1 nonzero residues, once each."""
    n = p * p + p + 1
    seen = sorted((x - y) % n for x in diff for y in diff if x != y)
    return seen == list(range(1, n))


def _singer(checker: Checker) -> None:
    """Check clause 4."""
    data = json.loads((_HERE / 'assets' / 'singer_witnesses.json').read_text())
    for w in data['witnesses']:
        p, cubic, m, cap, classes = w['p'], tuple(w['cubic']), w['M'], w['cap'], w['classes']
        n = p * p + p + 1
        tag = f'p={p} M={m} cap {cap}'
        checker.check(f'{tag}: cubic defines a Singer cycle', singer.singer_points(p, cubic) is not None)
        diff = singer.difference_set(p, cubic)
        checker.check(f'{tag}: trace-zero set is a planar difference set', len(diff) == p + 1 and _planar(p, diff))
        field = geometry.Field(p, 1)
        pts = {geometry.normalize(field, u) for u in singer.class_union(p, cubic, m, classes)}
        checker.check(f'{tag}: {len(classes) * n // m} distinct points', n % m == 0 and len(pts) == len(classes) * n // m, f'{len(pts)} points')
        loads = geometry.line_loads(field, sorted(pts))
        lo, hi = min(loads.values()), max(loads.values())
        checker.check(f'{tag}: every line meets the set in 1 to {cap} points', lo >= 1 and hi <= cap, f'range {lo}..{hi}')
        mu = singer.histogram(diff, m)
        circ = sorted(sum(mu[(r - t) % m] for r in classes) for t in range(m) for _ in range(n // m))
        checker.check(f'{tag}: direct and circulant loads agree', sorted(loads.values()) == circ)
    for p, m, cap in _EXHAUSTED:
        cubic = singer.singer_cubic(p)
        mu = singer.histogram(singer.difference_set(p, cubic), m)
        found, complete = singer.cover_search(mu, cap, 10**7)
        checker.check(f'p={p} M={m} cap {cap}: exhaustive search finds no invariant set', found is None and complete, f'found {found}, complete {complete}')
    for p, m, cap, value in _SYMMETRIC:
        mu = singer.histogram(singer.difference_set(p, singer.singer_cubic(p)), m)
        _, got = heuristic.symmetric_estimate(mu, p, cap)
        checker.check(f'p={p} M={m} cap {cap}: symmetric estimate 10^{value}', round(got, 1) == value or (value == 0.0 and abs(got) < 0.05), f'log10 {got:.3f}')


def _orbit_rows_python(top: int) -> list[tuple[int, int, int, int, int, int, int]]:
    """Return the clause-5 rows for primes p <= top, computed with util/singer.py."""
    rows = []
    for p in range(5, top + 1):
        if any(p % d == 0 for d in range(2, int(p**0.5) + 1)):
            continue
        n = p * p + p + 1
        cubic = singer.singer_cubic(p)
        diff = singer.difference_set(p, cubic)
        for m in range(2, p + 2):
            if n % m or p + 1 > 8 * m:
                continue
            mu = singer.histogram(diff, m)
            rows.append((p, *cubic, m, min(mu), max(mu)))
    return rows


def _orbit_rows_c(top: int) -> list[tuple[int, int, int, int, int, int, int]] | None:
    """Compile util/orbitscan.c into output/ and return its rows for 5 <= p <= top, or None."""
    compiler = next((shutil.which(c) for c in ('cc', 'clang', 'gcc') if shutil.which(c)), None)
    if compiler is None:
        return None
    out = _HERE / 'output'
    out.mkdir(exist_ok=True)
    exe = out / 'orbitscan'
    subprocess.run([compiler, '-O2', '-o', str(exe), str(_HERE / 'util' / 'orbitscan.c')], check=True)
    text = subprocess.run([str(exe), '5', str(top)], check=True, capture_output=True, text=True).stdout
    return [tuple(int(x) for x in line.split()) for line in text.splitlines()]


def _orbits(checker: Checker, quick: bool) -> None:
    """Check clause 5."""
    small = _orbit_rows_python(100)
    blocking_small = {(p, m, mx) for p, _, _, _, m, mn, mx in small if mn >= 1 and mx <= 8}
    checker.check('p <= 100: blocking single orbits with cap <= 8 as recorded', blocking_small == {r for r in _ORBITS[2] if r[0] <= 100}, f'{sorted(blocking_small)}')
    if quick:
        return
    rows = _orbit_rows_c(2000)
    checker.check('a C compiler is available for the full scan', rows is not None)
    if rows is None:
        return
    checker.check('C and Python scans agree for p <= 100', [r for r in rows if r[0] <= 100] == small)
    pairs, covering, blocking = _ORBITS
    checker.check(f'{pairs} pairs (p, m) for 5 <= p <= 2000', len(rows) == pairs, f'{len(rows)} pairs')
    hit = [r for r in rows if r[5] >= 1]
    checker.check(f'{covering} pairs with every class hit', len(hit) == covering, f'{len(hit)} pairs')
    got = {(p, m, mx) for p, _, _, _, m, mn, mx in rows if mn >= 1 and mx <= 8}
    checker.check('blocking single orbits with cap <= 8 as recorded', got == blocking, f'{sorted(got)}')
    late = min(r[6] for r in hit if r[0] > 1500)
    checker.check('for p > 1500 the least largest class count of a blocking orbit is 11', late == 11, f'{late}')


def _pencils(checker: Checker, quick: bool) -> None:
    """Check clause 7 by direct incidence counts."""
    for p in [31] if quick else [31, 37, 41, 43]:
        plane = pencil.Plane(p)
        for m in (1, 2, 3):
            on_y, missed = pencil.missed_lines(plane, pencil.random_conics(p, m, 1000 * p + m))
            counts = pencil.pencil_counts(plane, on_y, missed)
            mean, err = (p + 1) / 2**m, m * math.sqrt(p) + 2 * m + 1
            allowed = math.comb(2 * m * (m - 1), 2)
            outside = sum(1 for n in counts.values() if abs(n - mean) > err)
            checker.check(f'p={p}, m={m}: pencil bound off at most {allowed} points', outside <= allowed, f'{outside} outside')
            if m == 1:
                checker.check(f'p={p}: one conic, every N_P is (p - 1)/2 or (p + 1)/2', set(counts.values()) <= {(p - 1) // 2, (p + 1) // 2})
                checker.check(f'p={p}: one conic has p(p - 1)/2 external lines', len(missed) == p * (p - 1) // 2, f'{len(missed)}')
            # the lower bound for the missed lines in the proof of (4)
            bound = (p * p + p + 1 - m * (p + 1) - allowed) * (mean - err) / (p + 1)
            checker.check(f'p={p}, m={m}: missed lines at least the derived bound', len(missed) >= bound, f'{len(missed)} vs {bound:.1f}')
    # the homothetic pair has the same tangents from the origin
    p = 151
    conics = [pencil.diagonal_conic(p, 1, 1, -1), pencil.diagonal_conic(p, 1, 1, -4)]
    origin = (0, 0, 1)
    missing = 0
    for x, y in [(1, t) for t in range(p)] + [(0, 1)]:
        line_pts = [(x * s % p, y * s % p, 1) for s in range(p)] + [(x, y, 0)]
        missing += not any(sum(a[i][i] * v[i] * v[i] for i in range(3)) % p == 0 for a in conics for v in line_pts)
    checker.check('p=151: origin lies on at least (p - 3)/2 lines missing both conics', missing >= (p - 3) // 2, f'{missing}')
    checker.check('p=151: that count lies outside the pencil bound', missing - (p + 1) / 4 > 2 * math.sqrt(p) + 5, f'{missing}')
    checker.check('p=151: the origin is off both conics', all(sum(a[i][i] * origin[i] ** 2 for i in range(3)) % p for a in conics))


# cubics of clause 8: name, form, number of exceptional points at p = 211
_CUBICS = [
    ('Fermat', lambda x, y, z: x**3 + y**3 + z**3, 3),
    ('nodal', lambda x, y, z: y * y * z - x**3 - x * x * z, 3),
    ('cuspidal', lambda x, y, z: y * y * z - x**3, 1),
    ('smooth', lambda x, y, z: y * y * z - x**3 - 3 * x * z * z - 5 * z**3, 0),
]


# unions of clause 8: name, form, alpha, number of exceptional points at p = 211
_UNIONS = [
    ('Fermat cubic and conic', lambda x, y, z: (x**3 + y**3 + z**3) * ((x * x + y * y - 3 * z * z) % 211), 1 / 6, 2),
    ('two cubics', lambda x, y, z: ((y * y * z - x**3 - 3 * x * z * z - 5 * z**3) % 211) * ((x**3 + 2 * y**3 + 7 * z**3 + x * y * z) % 211), 1 / 9, 0),
]


def _cubic_pencils(checker: Checker) -> None:
    """Check clause 8 by vectorized incidence counts."""
    # agreement with the direct counts on a small plane
    p = 31
    plane = pencil.Plane(p)
    _, on, counts = pencil.curve_pencil_counts(p, _CUBICS[0][1])
    on_y = {i for i, (x, y, z) in enumerate(plane.points) if (x**3 + y**3 + z**3) % p == 0}
    missed = {j for j, pts in enumerate(plane.on_line) if not any(i in on_y for i in pts)}
    direct = pencil.pencil_counts(plane, on_y, missed)
    agree = set(int(i) for i in on.nonzero()[0]) == on_y and all(direct[i] == counts[i] for i in direct)
    checker.check('p=31: vectorized and direct pencil counts agree for the Fermat cubic', agree)
    p = 211
    for name, form, expected in _CUBICS:
        pts, on, counts = pencil.curve_pencil_counts(p, form)
        dev = abs(counts - p / 3)
        outside = [i for i in (~on & (dev > 2 * math.sqrt(p))).nonzero()[0]]
        checker.check(f'p={p}, {name} cubic: {expected} points outside the pencil bound', len(outside) == expected, f'{len(outside)}')
        checker.check(f'p={p}, {name} cubic: those points have N_P > p/2', all(counts[i] > p / 2 for i in outside))
        if name == 'Fermat':
            got = {tuple(int(c) for c in pts[i]) for i in outside}
            checker.check(f'p={p}: the Fermat exceptions are the coordinate points', got == {(0, 0, 1), (0, 1, 0), (1, 0, 0)}, f'{got}')
    # unions, which test the independence of the components
    for name, form, alpha, expected in _UNIONS:
        _, on, counts = pencil.curve_pencil_counts(p, form)
        outside = int((~on & (abs(counts - alpha * p) > 2 * math.sqrt(p))).sum())
        checker.check(f'p={p}, {name}: {expected} points outside the pencil bound', outside == expected, f'{outside}')


def main() -> int:
    """Run every clause and return the exit status."""
    args = evidence_parser(__doc__.splitlines()[0]).parse_args()
    checker = Checker()
    print('clause 1: cap-four witnesses')
    _witnesses(checker)
    print('clause 2: three conics in characteristic two')
    _three_conics(checker, 5 if args.quick else 7)
    print('clause 3: first-moment heuristic orders')
    _heuristic(checker)
    print('clause 4: Singer-invariant sets')
    _singer(checker)
    print('clause 5: single Singer-subgroup orbits')
    _orbits(checker, args.quick)
    print('clause 6: maximal-arc completion obstructions')
    _maximal_arcs(checker)
    print('clause 7: pencil counts for unions of conics')
    _pencils(checker, args.quick)
    print('clause 8: pencil counts for cubics')
    _cubic_pencils(checker)
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

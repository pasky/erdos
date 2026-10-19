"""Finite checks of the carry lemmas for integer lifts of Singer sets.

For p in {5, 7, 11, 13, 17, 19}, a Singer set B in [0, q), q = p^2+p+1, is
built from the trace-zero powers of a primitive element of F_(p^3) and its
perfect difference property is checked. The program then checks:
the half-set lemma (for 1 <= d < q exactly one of d, d - q is a difference
of B); the pointer lemma (for every residue c of a point u = c + q*s and
every residue rho != c, exactly one integer congruent to rho lies in
u + (B - B), at the height the lemma predicts); the coherence lemma for the
progression u_s = c + q*s, 1 <= s < M, M = p + 2, with c the least residue
outside B (main-type triples block every rho + q*s, rho != c,
2 <= s <= M - 2, while the progression is not strong Sidon); and, as a
reproducible record of the finite observation quoted on the analysis page,
the exact numbers of unblocked targets in [1, (p+2)q] for the anchored
lifts B u {b_i + q*i} with heights 1, ..., p+1 assigned in increasing and
in decreasing order of b_i, which are checked to be strong Sidon and to
block every target in the classes of B. Finally, for 3 <= m <= 9 it
searches exhaustively the Golomb rulers 0 = b_1 < ... < b_m <= m(m-1) and
checks that the largest L with every integer 1, ..., L a difference is
3, 6, 9, 13, 18, 21, 28 respectively, and that the retained rulers attain
these values; and it checks four retained longer Sidon rulers, with 12, 14,
18 and 20 marks, whose initial difference runs are 47, 55, 90 and 97.
Exact integer arithmetic; standard library and the repository
evidence harness only. Expected runtime about two minutes, almost all for
m = 9; --quick stops the ruler search at m = 8 and runs in seconds. Finite
cases only; no asymptotic conclusion is drawn here.

Also check the retained 40-point seed in [1,8001], its 399 initially
unblocked targets, and its maximal 48-point completion. For the fixed Singer
bases with p in {5,7,11,19,31,43}, enumerate every 0<=c<d<=q whose difference
is outside B-B, and count those for which (c+B-B) union (d+B-B) covers [0,q].
These checks run in both modes and use less than 256 MB.

For p in {11,19,31,43}, also count all three-point strong Sidon sets in
[0,q] whose pairwise distances avoid B-B, which contain no pair at distance
q, and whose three translates of B-B cover [0,q]. Integer bit masks exhaust
the domain by filtering the possible third points for each first pair.

Also check 26 retained multiple-height seeds and maximal completions with
p <= 23, N <= 53088, and at most 117 final marks. Recompute the seed's
prescribed columns, pair sums, all blockers, and residual classes and rows;
check the supplied additions rather than repeat their greedy discovery.
Finally enumerate all pairs 0 <= c < d < q for eleven fixed Singer bases
through p=43 and check the minimum number of misses in [0,q) of two
translates of B-B, without a pair-compatibility restriction. Both modes
include these checks, using exact integers and less than 256 MB.
"""
import json
import sys
from itertools import combinations_with_replacement
from pathlib import Path
from tools import Checker, evidence_parser

# unblocked targets of the anchored lifts: p -> (increasing, decreasing)
RECORDED = {5: (3, 2), 7: (0, 17), 11: (69, 80), 13: (54, 113),
            17: (339, 391), 19: (288, 405)}

# largest initial run of differences among Golomb rulers of length <= m(m-1)
RUNS = {3: (3, (0, 1, 3)), 4: (6, (0, 1, 4, 6)), 5: (9, (0, 2, 7, 8, 11)),
        6: (13, (0, 1, 4, 10, 12, 17)), 7: (18, (0, 5, 7, 13, 16, 17, 31)),
        8: (21, (0, 4, 5, 17, 19, 25, 28, 35)),
        9: (28, (0, 7, 10, 16, 18, 30, 31, 35, 57))}

# retained longer Sidon rulers with long initial runs (not claimed optimal)
LONG = {12: (47, (0, 2, 6, 24, 29, 40, 43, 55, 68, 75, 76, 85)),
        14: (55, (0, 4, 6, 20, 35, 52, 59, 77, 78, 86, 89, 99, 122, 127)),
        18: (90, (0, 2, 10, 22, 53, 56, 82, 83, 89, 98, 130, 148, 153, 167,
                  188, 192, 205, 216)),
        20: (97, (0, 1, 8, 11, 68, 77, 94, 116, 121, 156, 158, 179, 194,
                  208, 212, 228, 240, 253, 259, 283))}

# (misses, residual classes, residual rows, added points), inc then dec.
FIBER_COUNTS = {
    (3, 'explicit'): ((2, 2, 2, 1), (11, 7, 7, 2)),
    (5, 'explicit'): ((46, 22, 15, 4), (50, 23, 16, 3)),
    (7, 'explicit'): ((131, 49, 22, 9), (179, 49, 29, 7)),
    (11, 'explicit'): ((733, 121, 47, 16), (805, 121, 46, 17)),
    (13, 'explicit'): ((1222, 169, 55, 20), (1331, 169, 54, 19)),
    (17, 'explicit'): ((3129, 289, 71, 31), (3199, 289, 70, 31)),
    (19, 'explicit'): ((4199, 361, 79, 34), (4322, 361, 78, 35)),
    (23, 'explicit'): ((7887, 529, 95, 45), (8012, 529, 94, 44)),
    (3, 'skolem'): ((0, 0, 0, 0), (1, 1, 1, 1)),
    (7, 'skolem'): ((28, 24, 13, 5), (40, 29, 16, 3)),
    (11, 'skolem'): ((181, 104, 29, 11), (219, 104, 33, 11)),
    (19, 'skolem'): ((1205, 356, 59, 26), (1320, 357, 58, 26)),
    (23, 'skolem'): ((2401, 525, 72, 31), (2315, 521, 71, 33)),
}


def factor(n):
    primes, d = [], 2
    while d * d <= n:
        if n % d == 0:
            primes.append(d)
            while n % d == 0:
                n //= d
        d += 1
    return primes + ([n] if n > 1 else [])


def singer(p):
    """Perfect difference set modulo p^2+p+1 from trace-zero powers."""
    a, b = next((a, b) for a in range(p) for b in range(1, p)
                if all((x ** 3 + a * x + b) % p for x in range(p)))

    def mul(u, v):
        c = [0] * 5
        for i in range(3):
            for j in range(3):
                c[i + j] += u[i] * v[j]
        for d in (4, 3):
            c[d - 2] -= a * c[d]
            c[d - 3] -= b * c[d]
        return tuple(x % p for x in c[:3])

    def power(u, e):
        r = (1, 0, 0)
        while e:
            if e & 1:
                r = mul(r, u)
            u = mul(u, u)
            e >>= 1
        return r

    order = p ** 3 - 1
    primes = factor(order)
    g = next(v for v in ((n % p, n // p % p, n // p // p)
                         for n in range(2, p ** 3))
             if all(power(v, order // f) != (1, 0, 0) for f in primes))
    q = p * p + p + 1
    B, v = [], (1, 0, 0)
    for e in range(q):
        v1 = power(v, p)
        v2 = power(v1, p)
        if all((v[i] + v1[i] + v2[i]) % p == 0 for i in range(3)):
            B.append(e)
        v = mul(v, g)
    return q, B


def blocked_set(marks):
    sums = [x + y for x, y in combinations_with_replacement(marks, 2)]
    blocked = set(marks)
    for i, x in enumerate(marks):
        for y in marks[i:]:
            if (x + y) % 2 == 0:
                blocked.add((x + y) // 2)
            for z in marks:
                if z != x and z != y:
                    blocked.add(x + y - z)
    return sums, blocked


def initial_run(ruler):
    diffs = {y - x for i, x in enumerate(ruler) for y in ruler[i + 1:]}
    run = 0
    while run + 1 in diffs:
        run += 1
    return run, len(diffs) == len(ruler) * (len(ruler) - 1) // 2


def longest_run(m, length):
    """Exhaustive maximum of the initial difference run over Golomb rulers
    with m marks, first mark 0 and last mark at most length."""
    total = m * (m - 1) // 2
    best = [0]
    marks = [0]

    def dfs(mask, k):
        missing = ~mask >> 1
        run = (missing & -missing).bit_length() - 1
        if k == m:
            best[0] = max(best[0], run)
            return
        target = best[0] + 1
        have = bin(mask & ((1 << (target + 1)) - 2)).count('1')
        if target - have > total - k * (k - 1) // 2:
            return
        for x in range(marks[-1] + 1, length + 1):
            new, ok = 0, True
            for b in marks:
                bit = 1 << (x - b)
                if mask & bit or new & bit:
                    ok = False
                    break
                new |= bit
            if ok:
                marks.append(x)
                dfs(mask | new, k + 1)
                marks.pop()

    dfs(0, 1)
    return best[0]


def check_completion(checker):
    """Verify retained inputs by direct pair sums and all triple blockers."""
    asset = Path(__file__).parent / 'assets' / 'projective_completion.json'
    data = json.loads(asset.read_text())
    n, seed, addition = data['N'], data['seed'], data['addition']
    marks = seed + addition
    checker.check('completion witness: exact domain and cardinalities',
                  n == 8001 and len(seed) == 40 and len(addition) == 8
                  and len(set(marks)) == 48
                  and all(isinstance(x, int) and 1 <= x <= n for x in marks))
    sums, blocked = blocked_set(seed)
    checker.check('completion witness: seed is strong Sidon',
                  len(sums) == len(set(sums)))
    checker.check('completion witness: exactly 399 initial misses',
                  sum(x not in blocked for x in range(1, n + 1)) == 399)
    sums, blocked = blocked_set(marks)
    checker.check('completion witness: union is strong Sidon',
                  len(sums) == len(set(sums)))
    checker.check('completion witness: union is maximal throughout [1,8001]',
                  all(x in blocked for x in range(1, n + 1)))


def check_two_translate_templates(checker):
    """All admissible pairs in a fixed block, using exact bit masks."""
    expected = {5: (117, 13), 7: (151, 15), 11: (1, 1),
                19: (1, 1), 31: (1, 1), 43: (1, 1)}
    for p, (pair_count, gap_count) in expected.items():
        q, base = singer(p)
        differences = [((a - b) % q) for a in base for b in base if a != b]
        checker.check(f'p={p}: template base is a perfect difference set',
                      len(base) == p + 1
                      and sorted(differences) == list(range(1, q)))
        diffs = {a - b for a in base for b in base}
        full = (1 << (q + 1)) - 1
        raw = sum(1 << (d + q) for d in diffs)
        masks = [(raw >> (q - c)) & full for c in range(q + 1)]
        pairs = [(c, d) for c in range(q) for d in range(c + 1, q + 1)
                 if d - c not in diffs and (masks[c] | masks[d]) == full]
        checker.check(f'p={p}: complete two-translate template census',
                      len(pairs) == pair_count
                      and len({d - c for c, d in pairs}) == gap_count
                      and (0, q) in pairs)
        if p >= 11:
            checker.check(f'p={p}: only the separation-q pair covers',
                          pairs == [(0, q)])
        if p in (11, 19, 31, 43):
            expected_triples = {11: 1446, 19: 16572, 31: 3298, 43: 0}
            total = 0
            for a in range(q - 1):
                for b in range(a + 1, q):
                    if b - a in diffs:
                        continue
                    # c>b, and c-a,c-b are not differences of B.
                    candidates = (full ^ ((1 << (b + 1)) - 1))
                    candidates &= full ^ (masks[a] | masks[b])
                    if a == 0:
                        candidates &= full ^ (1 << q)
                    if 2 * b - a <= q:
                        candidates &= full ^ (1 << (2 * b - a))
                    missing = full ^ (masks[a] | masks[b])
                    while missing and candidates:
                        bit = missing & -missing
                        x = bit.bit_length() - 1
                        # D=-D, so x is in c+D exactly when c is in x+D.
                        candidates &= masks[x]
                        missing ^= bit
                    total += candidates.bit_count()
            checker.check(f'p={p}: complete three-translate template census',
                          total == expected_triples[p])


def check_multiple_heights(checker):
    """Check retained finite inputs by literal pair sums and blockers."""
    asset = Path(__file__).parent / 'assets' / 'multiple_height_completions.json'
    cases = json.loads(asset.read_text())['cases']
    expected_keys = {(p, family, order) for p, family in FIBER_COUNTS
                     for order in ('inc', 'dec')}
    keys = [(row['p'], row['family'], row['order']) for row in cases]
    checker.check('height fibers: exact 26-case domain without duplicates',
                  len(keys) == 26 and set(keys) == expected_keys)
    bases = {}
    for row in cases:
        p, family, order = row['p'], row['family'], row['order']
        if (p, family, order) not in expected_keys:
            continue
        if p not in bases:
            bases[p] = singer(p)
        q, base = bases[p]
        m = p + 1
        label = f'p={p}, {family}, {order}'
        checker.check(f'{label}: exact perfect-difference base',
                      row['base'] == base and len(base) == m
                      and sorted((a-b) % q for a in base for b in base
                                 if a != b) == list(range(1, q)))
        columns = row['columns']
        if family == 'explicit':
            valid_columns = columns == [[0, 2*i-1, 3*m+i-1]
                                        for i in range(1, m+1)]
            height = 4*m
        else:
            valid_columns = len(columns) == m
            pairs = []
            for i, column in enumerate(columns, 1):
                valid_columns &= (len(column) == 3 and column[:2] == [0, i])
                if len(column) == 3:
                    pairs.extend((column[2]-m-i, column[2]-m))
            valid_columns &= sorted(pairs) == list(range(1, 2*m+1))
            height = 3*m+1
        checker.check(f'{label}: prescribed columns and domain',
                      valid_columns and row['height'] == height)
        if not valid_columns:
            continue
        differences = [b-a for column in columns
                       for i, a in enumerate(column) for b in column[i+1:]]
        checker.check(f'{label}: disjoint positive height differences',
                      len(differences) == 3*m
                      and len(set(differences)) == 3*m
                      and min(differences) > 0)
        if family == 'skolem':
            checker.check(f'{label}: complete vertical difference interval',
                          sorted(differences) == list(range(1, 3*m+1)))
        ordered = base if order == 'inc' else base[::-1]
        seed = sorted(b+q*h for b, column in zip(ordered, columns)
                      for h in column)
        n = q*height
        sums, blocked = blocked_set(seed)
        checker.check(f'{label}: seed is strong Sidon in the interval',
                      len(seed) == 3*m and len(set(seed)) == 3*m
                      and 0 <= min(seed) <= max(seed) < n
                      and len(sums) == len(set(sums)))
        residual = {x for x in range(n) if x not in blocked}
        counts = (len(residual), len({x % q for x in residual}),
                  len({x // q for x in residual}), len(row['addition']))
        expected = FIBER_COUNTS[p, family][0 if order == 'inc' else 1]
        checker.check(f'{label}: exact residual and addition counts',
                      counts == expected
                      and counts[:3] == (row['misses'], row['miss_classes'],
                                         row['miss_rows']))
        checker.check(f'{label}: no occupied class has a miss',
                      all(x % q not in base for x in residual))
        marks = seed + row['addition']
        sums, blocked = blocked_set(marks)
        checker.check(f'{label}: completion is strong Sidon in the interval',
                      len(marks) == len(set(marks))
                      and all(type(x) is int and 0 <= x < n for x in marks)
                      and len(sums) == len(set(sums)))
        checker.check(f'{label}: completion blocks every interval point',
                      all(x in blocked for x in range(n)))


def check_same_row_pairs(checker):
    """All pairs in [0,q), without compatibility; pin one optimum too."""
    expected = {5: (0, 11, 2), 7: (0, 22, 11), 11: (2, 50, 30),
                13: (0, 57, 63), 17: (10, 77, 117), 19: (2, 80, 217),
                23: (31, 141, 247), 29: (12, 215, 428),
                31: (23, 222, 536), 37: (25, 249, 772),
                43: (109, 520, 770)}
    for p, (minimum, c, delta) in expected.items():
        q, base = singer(p)
        checker.check(f'p={p}: same-row base is a perfect difference set',
                      len(base) == p+1
                      and sorted((a-b) % q for a in base for b in base
                                 if a != b) == list(range(1, q)))
        differences = {a-b for a in base for b in base}
        raw = sum(1 << (d+q) for d in differences)
        full = (1 << q)-1
        masks = [(raw >> (q-a)) & full for a in range(q)]
        best = min((full ^ (masks[a] | masks[b])).bit_count()
                   for a in range(q) for b in range(a+1, q))
        checker.check(f'p={p}: exact minimum over all same-row pairs',
                      best == minimum)
        literal = sum(r-c not in differences and r-c-delta not in differences
                      for r in range(q))
        checker.check(f'p={p}: retained optimum checked without bit masks',
                      0 <= c < c+delta < q and literal == minimum)


def main():
    args = evidence_parser(__doc__).parse_args()
    checker = Checker()
    for p in sorted(RECORDED):
        q, B = singer(p)
        diffs = sorted((x - y) % q for x in B for y in B if x != y)
        checker.check(f'p={p}: perfect difference set modulo {q}',
                      len(B) == p + 1 and diffs == list(range(1, q)))
        D = {x - y for x in B for y in B}
        checker.check(f'p={p}: half-set lemma',
                      all((d in D) != (d - q in D) for d in range(1, q))
                      and 0 in D and all(-d in D for d in D))
        pointer = True
        for c in range(q):
            for rho in range(q):
                if rho == c:
                    continue
                hits = [k for k in (-1, 0, 1) if rho + q * k - c in D]
                if rho - c in D:
                    predicted = 0
                else:
                    predicted = -1 if rho > c else 1
                pointer &= hits == [predicted]
        checker.check(f'p={p}: pointer lemma for every residue pair', pointer)
        M = p + 2
        c = min(r for r in range(q) if r not in B)
        progression = [c + q * s for s in range(1, M)]
        covered = {u + d for u in progression for d in D if d != 0}
        checker.check(f'p={p}: progression blocks all interior heights',
                      all(rho + q * s in covered
                          for s in range(2, M - 1)
                          for rho in range(q) if rho != c))
        checker.check(f'p={p}: progression is not strong Sidon',
                      progression[0] + progression[2] == 2 * progression[1])
        for label, ordered in (('increasing', B), ('decreasing', B[::-1])):
            marks = sorted(B + [b + q * (i + 1)
                                for i, b in enumerate(ordered)])
            sums, blocked = blocked_set(marks)
            holes = [x for x in range(1, M * q + 1) if x not in blocked]
            checker.check(f'p={p}, {label}: anchored lift is strong Sidon',
                          len(sums) == len(set(sums)))
            checker.check(f'p={p}, {label}: classes of B fully blocked',
                          all(x % q not in B for x in holes))
            expected = RECORDED[p][0 if label == 'increasing' else 1]
            checker.check(f'p={p}, {label}: {len(holes)} unblocked targets',
                          len(holes) == expected)
    for m, (value, ruler) in sorted(RUNS.items()):
        if args.quick and m > 8:
            continue
        run, sidon = initial_run(ruler)
        checker.check(f'm={m}: retained ruler is Sidon with run {value}',
                      sidon and run == value and len(ruler) == m
                      and ruler[0] == 0 and ruler[-1] <= m * (m - 1))
        checker.check(f'm={m}: exhaustive maximum run is {value}',
                      longest_run(m, m * (m - 1)) == value)
    for m, (value, ruler) in sorted(LONG.items()):
        run, sidon = initial_run(ruler)
        checker.check(f'm={m}: retained Sidon ruler has run {value}',
                      sidon and run == value and len(ruler) == m)
    check_completion(checker)
    check_two_translate_templates(checker)
    check_multiple_heights(checker)
    check_same_row_pairs(checker)
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

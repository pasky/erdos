"""Check the weighted-count certificates that exclude bad 4-list assignments of order 26.

Checked clauses (the finite arithmetic of the L78 proof, ``../_proof.md``):

1. The compact weighting in ``assets/compact_certificate.json`` has the
   stated domain and gives the two displayed tables by Python integer binomial
   counts. Independently, subset transforms over all 2^17 palette subsets and
   all 2378 nonfixed four-subsets give Z = 83424, maxL = 4374, maxR = 2664.
   Therefore (a-2)*maxL + (26-a)*maxR <= 82746 < Z for 2 <= a <= 13.
2. The auxiliary ``assets/certificates.json`` has the stated domain: 17 colours, lists of
   size 4, order 26, fixed left lists {0,1,2,3} and {4,5,6,7}, and exactly one
   weighting for every side split (left, right) with left = 2, ..., 24 and
   left + right = 26; every row has t1, t2 >= 1 and a nonnegative integer weight.
3. For every split, with Z the total weight of the palette subsets and maxL,
   maxR the largest left and right event weights over all 2378 four-subsets of
   the palette other than the two fixed lists, (left - 2) * maxL + right * maxR
   < Z. The sums run over all 2^17 palette subsets in exact integer arithmetic
   (subset- and superset-sum transforms), without per-type formulas.

Controls, which use the same functions: the K_{2,4} assignment with 2-lists and
an assignment of 18 distinct 3-lists on 9 colours (``assets/controls.json``)
are checked bad by exhaustion; for each, two disjoint left lists are relabelled
as the fixed lists and, for the weighting concentrated on each single profile
and for the uniform weighting, the other lists' actual event weights sum to at
least Z, so no weighting can certify against an actual bad assignment. Deleting
one right list from the 9-colour assignment yields a colourable assignment,
whose colouring is exhibited and checked. The uniform weighting at the split
(13, 13) does not certify. Malformed profiles, weights and list assignments
are refused, including weights whose total would overflow int64. The total
is bounded with Python integers before allocating the fixed-width array.

Run from the repository root:
    uv run --no-sync python wiki/theory/combinatorics/L78_bipartite_order_26_four_choosable/evidence/main.py

Dependencies: numpy and the installed root ``tools`` package. Inputs: the three
JSON assets. Deterministic, no output files, no reduced mode; expected runtime
a few seconds. Every failed obligation exits nonzero, including under
``python -O``. Limitation: the program checks the arithmetic of the weighted
count only; the reduction to 17 colours with distinct lists and the two
disjoint left lists is the mathematical argument of ``../_proof.md``.
"""

from __future__ import annotations

import itertools
import json
import sys
from copy import deepcopy
from math import comb
from pathlib import Path

import tools

sys.path.insert(0, str(Path(__file__).resolve().parent / 'util'))

from certificate import assignment_masks, colouring_subset, event_weights, is_bad, mask, split_bound, weight_vector  # noqa: E402

__all__ = [
    'check_certificates',
    'check_compact',
    'check_controls',
    'main',
]

# locate the retained inputs
_ASSETS = Path(__file__).resolve().parent / 'assets'
_CERTIFICATES = _ASSETS / 'certificates.json'
_CONTROLS = _ASSETS / 'controls.json'
_COMPACT = _ASSETS / 'compact_certificate.json'


def check_compact(checker: tools.Checker) -> None:
    """Recompute both tables in the proof, then all event weights without formulas."""
    data = json.loads(_COMPACT.read_text())
    checker.check(
        'compact certificate domain and fixed lists',
        (data['colours'], data['list_size'], data['order']) == (17, 4, 26)
        and data['fixed_left'] == [[0, 1, 2, 3], [4, 5, 6, 7]],
    )
    rows = data['weights']
    wv = weight_vector(rows, 17, 4)
    weights = {(p, q, r): w for p, q, r, w in rows}
    checker.check('compact weighting is symmetric in the fixed lists', all(weights.get((q, p, r), 0) == w for p, q, r, w in rows))

    def C(n: int, k: int) -> int:
        return comb(n, k) if 0 <= k <= n else 0

    counts = [C(4, p) * C(4, q) * C(9, r) * (1 if p == q else 2) for p, q, r, _ in rows if p <= q]
    checker.check('six profile multiplicities in the proof', counts == [1344, 6048, 4032, 4032, 4032, 576])
    Z = sum(w * C(4, p) * C(4, q) * C(9, r) for p, q, r, w in rows)
    checker.check('total weight from profiles and subsets is 83424', Z == int(wv.sum()) == 83424)
    expected = [
        (0, 0, 4, 4304, 2576), (1, 0, 3, 4374, 2618),
        (1, 1, 2, 4347, 2651), (2, 0, 2, 4312, 2400),
        (2, 1, 1, 4284, 2458), (2, 2, 0, 4200, 2208),
        (3, 0, 1, 4200, 2656), (3, 1, 0, 4158, 2664),
    ]
    types = [(x, y, 4 - x - y) for x in range(4) for y in range(min(x, 4 - x) + 1)]
    checker.check('eight types exhaust all nonfixed four-subsets up to the interchange', types == [row[:3] for row in expected])
    for x, y, z, target_l, target_r in expected:
        ell = sum(w * C(4 - x, p) * C(4 - y, q) * C(9 - z, r) for p, q, r, w in rows)
        rr = sum(w * C(4 - x, p - x) * C(4 - y, q - y) * C(9 - z, r - z) for p, q, r, w in rows)
        checker.check(f'proof table at type {(x, y, z)}', (ell, rr) == (target_l, target_r))
    z, ml, mr, bound = split_bound(rows, 17, 4, 13, 13)
    checker.check('all 2378 list masks and all 131072 subsets give the stated maxima', (z, ml, mr, bound) == (83424, 4374, 2664, 82746))
    checker.check('one weighting excludes every split with 2 <= a <= 13', ml >= mr and all((a - 2) * ml + (26 - a) * mr < z for a in range(2, 14)))


def check_certificates(checker: tools.Checker) -> None:
    """Check the certificate domain and the strict inequality for every split."""
    # read the certificate file and check its declared domain
    data = json.loads(_CERTIFICATES.read_text())
    n, k, order = data['colours'], data['list_size'], data['order']
    checker.check('certificate domain: 17 colours, 4-lists, order 26', (n, k, order) == (17, 4, 26), f'{n=} {k=} {order=}')
    checker.check(
        'certificate fixed left lists are {0,1,2,3} and {4,5,6,7}',
        data['fixed_left'] == [[0, 1, 2, 3], [4, 5, 6, 7]],
        str(data['fixed_left']),
    )
    splits = [(s['left'], s['right']) for s in data['splits']]
    expected = [(a, order - a) for a in range(2, order - 1)]
    checker.check('one weighting for every split left = 2..24', sorted(splits) == expected, str(splits))

    # check the strict inequality for every split
    for s in data['splits']:
        a, b = s['left'], s['right']
        try:
            Z, maxL, maxR, bound = split_bound(s['weights'], n, k, a, b)
        except ValueError as exc:
            checker.check(f'split ({a},{b}) weighting in domain', False, str(exc))
            continue
        checker.check(
            f'split ({a},{b}): (a-2)*maxL + b*maxR < Z',
            bound < Z,
            f'Z={Z} maxL={maxL} maxR={maxR} bound={bound} ratio={bound / Z:.6f}' if Z else 'Z=0',
        )


def actual_event_total(left: list[int], right: list[int], rows: list[list[int]], n: int, k: int) -> tuple[int, int]:
    """Return ``(Z, S)``: total weight and the actual event weight of the lists other than the fixed two."""
    wv = weight_vector(rows, n, k)
    a1 = (1 << k) - 1
    a2 = a1 << k
    lw, _ = event_weights(wv, n, [X for X in left if X not in (a1, a2)])
    _, rw = event_weights(wv, n, right)
    return int(wv.sum()), sum(lw) + sum(rw)


def relabel(left: list[int], right: list[int], n: int) -> tuple[list[int], list[int]] | None:
    """Relabel colours so that two disjoint left lists become {0,...,k-1} and {k,...,2k-1}."""
    pair = next(((A, B) for A, B in itertools.combinations(left, 2) if A & B == 0), None)
    if pair is None:
        return None
    order = [c for c in range(n) if pair[0] >> c & 1] + [c for c in range(n) if pair[1] >> c & 1]
    order += [c for c in range(n) if not (pair[0] | pair[1]) >> c & 1]
    new = {c: i for i, c in enumerate(order)}

    def move(X: int) -> int:
        return sum(1 << new[c] for c in range(n) if X >> c & 1)

    return [move(X) for X in left], [move(X) for X in right]


def check_controls(checker: tools.Checker) -> None:
    """Run the controls on actual bad assignments, a colourable mutant and malformed inputs."""
    data = json.loads(_CONTROLS.read_text())
    for name in ('k2_k24', 'k3_nine'):
        ctl = data[name]
        n, k, left, right = assignment_masks(ctl)
        checker.check(f'control {name}: lists distinct and of size {k}', len(set(left + right)) == len(left + right) and all(bin(X).count('1') == k for X in left + right))
        checker.check(f'control {name}: bad by exhaustion over all {2 ** n} subsets', is_bad(left, right, n))
        moved = relabel(left, right, n)
        checker.check(f'control {name}: two disjoint left lists exist', moved is not None)
        if moved is None:
            continue
        left, right = moved

        # every single-profile weighting and the uniform weighting: actual events >= Z
        profs = [(p1, p2, p3) for p1 in range(1, k + 1) for p2 in range(1, k + 1) for p3 in range(n - 2 * k + 1)]
        worst = None
        for p in profs:
            Z, S = actual_event_total(left, right, [[*p, 1]], n, k)
            if worst is None or S * worst[1] < worst[0] * Z:
                worst = (S, Z, p)
        Z, S = actual_event_total(left, right, [[*p, 1] for p in profs], n, k)
        checker.check(
            f'control {name}: every single-profile weighting has events >= Z',
            worst is not None and worst[0] >= worst[1],
            f'tightest profile {worst[2]}: events {worst[0]} vs Z {worst[1]}' if worst else '',
        )
        checker.check(f'control {name}: uniform weighting has events >= Z', S >= Z, f'events {S} vs Z {Z}')

    # a colourable mutant: delete one right list of the 9-colour assignment
    ctl = data['k3_nine']
    n, _, left, right = assignment_masks(ctl)
    right = right[1:]
    T = colouring_subset(left, right, n)
    checker.check('mutant (one right list deleted) is colourable', T is not None)
    if T is not None:
        colours_left = [min(c for c in range(n) if A >> c & 1 and T >> c & 1) for A in left]
        colours_right = [min(c for c in range(n) if B >> c & 1 and not T >> c & 1) for B in right]
        proper = not set(colours_left) & set(colours_right)
        checker.check('mutant colouring is proper and uses list colours', proper, f'T={T:b} left={colours_left} right={colours_right}')

    # the uniform weighting does not certify the split (13,13)
    rows = [[p1, p2, p3, 1] for p1 in range(1, 5) for p2 in range(1, 5) for p3 in range(10)]
    Z, maxL, maxR, bound = split_bound(rows, 17, 4, 13, 13)
    checker.check('uniform weighting does not certify split (13,13)', bound >= Z, f'bound={bound} Z={Z}')

    # malformed rows are refused
    for label, bad_rows in [
        ('profile with t1 = 0', [[0, 1, 4, 1]]),
        ('negative weight', [[1, 1, 4, -1]]),
        ('repeated profile', [[1, 1, 4, 1], [1, 1, 4, 2]]),
        ('t3 out of range', [[1, 1, 10, 1]]),
        ('weight not an integer', [[1, 1, 4, 0.5]]),
        ('overflow before int64 conversion', [[1, 1, 6, 2**62]]),
    ]:
        try:
            weight_vector(bad_rows, 17, 4)
            refused = False
        except ValueError:
            refused = True
        checker.check(f'malformed weighting refused: {label}', refused)

    for label, changes in [
        ('wrong size', {'left': [[0]]}),
        ('repeated colour', {'left': [[0, 0]]}),
        ('colour outside palette', {'left': [[0, 4]]}),
        ('noninteger colour', {'left': [[0, True]]}),
        ('empty side', {'right': []}),
    ]:
        bad = deepcopy(data['k2_k24'])
        bad.update(changes)
        try:
            assignment_masks(bad)
            refused = False
        except ValueError:
            refused = True
        checker.check(f'malformed assignment refused: {label}', refused)


def main() -> int:
    """Run the certificate checks and the controls; return the exit code."""
    parser = tools.evidence_parser(
        'Check the weighted-count certificates excluding bad 4-list assignments of order 26 (L78).',
        quick=False,
    )
    parser.parse_args()
    checker = tools.Checker()
    check_compact(checker)
    check_certificates(checker)
    check_controls(checker)
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

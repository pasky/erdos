"""Check arithmetic in the retained order-26 examination by direct counting.

This grading check reads the three frozen JSON assets, never the author's
Python implementation. It enumerates palette subsets and tests disjointness
and containment directly for representatives of all eight list types. There
are no subset transforms or binomial formulas in that calculation. Permuting
colours within the two four-element parts and the nine-element part, and
interchanging the first two parts, proves that each representative covers its
whole type. The expected six-group tables are the examination's displayed
integer contributions, not values obtained from the author's program.

Run with --subject pointing to evidence/assets/review_subject. The optional
--mutate-weight changes the first compact weight from 7 to 6 in memory; that
run must exit 1 with a direct-count mismatch. No input is written. This is a
finite arithmetic check, not the all-graphs reduction or a replacement review.
Dependencies: Python standard library. Expected runtime: several seconds.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from itertools import combinations
import json
from pathlib import Path
import sys


TYPES = ((0, 0, 4), (1, 0, 3), (1, 1, 2), (2, 0, 2),
         (2, 1, 1), (2, 2, 0), (3, 0, 1), (3, 1, 0))
TYPE_COUNTS = (126, 672, 576, 432, 432, 36, 72, 32)
PROFILES = ((1, 1, 6), (1, 2, 5), (1, 2, 6),
            (1, 3, 4), (2, 3, 3), (3, 3, 2))
GROUP_COUNTS = (1344, 6048, 4032, 4032, 4032, 576)
GROUP_TOTALS = (9408, 18144, 4032, 32256, 16128, 3456)
MISS = (
    (0, 144, 0, 1280, 1920, 960),
    (84, 540, 30, 1920, 1440, 360),
    (441, 1134, 126, 1680, 840, 126),
    (392, 1008, 112, 2240, 560, 0),
    (1176, 1512, 252, 1120, 224, 0),
    (2352, 1512, 336, 0, 0, 0),
    (784, 1008, 168, 2240, 0, 0),
    (1764, 1134, 252, 1008, 0, 0),
)
CONTAIN = (
    (1120, 720, 480, 256, 0, 0),
    (560, 810, 360, 768, 120, 0),
    (245, 630, 210, 1008, 504, 54),
    (0, 420, 140, 1344, 448, 48),
    (0, 210, 56, 896, 1008, 288),
    (0, 0, 0, 0, 1344, 864),
    (0, 0, 0, 1792, 672, 192),
    (0, 0, 0, 1008, 1008, 648),
)


def mask(values):
    return sum(1 << v for v in values)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--subject', type=Path, required=True)
    parser.add_argument('--mutate-weight', action='store_true')
    args = parser.parse_args()
    assets = args.subject / 'evidence/assets'
    compact = json.loads((assets / 'compact_certificate.json').read_text())
    auxiliary = json.loads((assets / 'certificates.json').read_text())
    controls = json.loads((assets / 'controls.json').read_text())
    failures = []
    count = 0

    def check(name, condition):
        nonlocal count
        count += 1
        print(f"[{'ok' if condition else 'FAIL'}] {name}")
        if not condition:
            failures.append(name)

    if args.mutate_weight:
        compact['weights'][0][3] = 6
    weights = {tuple(row[:3]): row[3] for row in compact['weights']}
    check('ten distinct compact profiles with nonnegative integer weights',
          len(weights) == len(compact['weights']) == 10
          and all(type(w) is int and w >= 0 for w in weights.values()))
    check('compact weights invariant under interchange of fixed parts',
          all(weights.get((b, a, c)) == w for (a, b, c), w in weights.items()))
    group_for = {}
    for i, (a, b, c) in enumerate(PROFILES):
        group_for[(a, b, c)] = i
        group_for[(b, a, c)] = i
    check('positive profile support equals the six displayed groups',
          set(weights) == set(group_for))
    representatives = [mask(list(range(x)) + list(range(4, 4+y))
                            + list(range(8, 8+z))) for x, y, z in TYPES]
    counts = Counter()
    for values in combinations(range(17), 4):
        x = sum(v < 4 for v in values)
        y = sum(4 <= v < 8 for v in values)
        z = sum(v >= 8 for v in values)
        if (x, y) not in ((4, 0), (0, 4)):
            counts[(max(x, y), min(x, y), z)] += 1
    check('all 2378 admissible four-subsets partition into eight types',
          counts == dict(zip(TYPES, TYPE_COUNTS)) and sum(counts.values()) == 2378)

    group_counts = [0]*6
    group_totals = [0]*6
    miss = [[0]*6 for _ in TYPES]
    contain = [[0]*6 for _ in TYPES]
    support_size = 0
    for subset in range(1 << 17):
        profile = ((subset & 15).bit_count(),
                   ((subset >> 4) & 15).bit_count(),
                   (subset >> 8).bit_count())
        support_size += bool(profile[0] and profile[1])
        if profile not in weights:
            continue
        group = group_for[profile]
        weight = weights[profile]
        group_counts[group] += 1
        group_totals[group] += weight
        for i, target in enumerate(representatives):
            if not subset & target:
                miss[i][group] += weight
            if subset & target == target:
                contain[i][group] += weight
    check('direct count of subsets meeting both fixed lists is 115200',
          support_size == 115200)
    check('direct count of all six profile multiplicities',
          tuple(group_counts) == GROUP_COUNTS)
    check('direct-count total contributions equal the report',
          tuple(group_totals) == GROUP_TOTALS)
    for i, kind in enumerate(TYPES):
        check(f'direct-count miss contributions {kind}', tuple(miss[i]) == MISS[i])
        check(f'direct-count containment contributions {kind}',
              tuple(contain[i]) == CONTAIN[i])
    total = sum(group_totals)
    left_max = max(map(sum, miss))
    right_max = max(map(sum, contain))
    check('total and attained event maxima are 83424, 4374, 2664',
          (total, left_max, right_max) == (83424, 4374, 2664)
          and sum(miss[1]) == left_max and sum(contain[7]) == right_max)
    bounds = [(a-2)*left_max + (26-a)*right_max for a in range(2, 14)]
    check('all twelve side bounds are strict, with worst gap 678',
          all(b < total for b in bounds) and total-max(bounds) == 678)
    extended = [2+(a-2)*(left_max+1)+(26-a)*right_max for a in range(2, 14)]
    check('empty-set perturbation has total 83425 and maximum bound 82759',
          total+1 == 83425 and max(extended) == 82759
          and all(b < total+1 for b in extended))

    balanced = next(row for row in auxiliary['splits'] if row['left'] == 13)
    peak = max(row[3] for row in balanced['weights'])
    rounded = {}
    for a, b, c, w in balanced['weights']:
        value = Fraction(8*w, peak)
        nearest = (2*value.numerator + value.denominator)//(2*value.denominator)
        if nearest:
            rounded[(a, b, c)] = nearest
    check('exact rational rescaling and rounding gives the compact weights',
          rounded == weights)
    control = controls['k3_nine']
    left_colours = (4, 2, 2, 3, 3, 2, 3, 8)
    right_colours = (5, 5, 1, 5, 6, 0, 0, 5, 0)
    check('displayed deletion witness is a proper list colouring',
          len(control['left']) == len(left_colours)
          and len(control['right'][1:]) == len(right_colours)
          and all(c in row for c, row in zip(left_colours, control['left']))
          and all(c in row for c, row in zip(right_colours, control['right'][1:]))
          and set(left_colours).isdisjoint(right_colours))
    print(f'{count} obligations; {len(failures)} failures')
    return int(bool(failures))


if __name__ == '__main__':
    sys.exit(main())

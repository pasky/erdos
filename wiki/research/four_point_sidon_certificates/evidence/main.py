"""Replay Ma--Tang's fixed 14-point certificate using exact integers.

Full domain: all C(14,4)=1001 four-subsets, all C(14,9)=2002
nine-subsets, and the supplied eight-point witness. Heredity excludes
all larger Sidon subsets once every nine-subset fails. No discovery search,
and no claim about optimality of c*. Runtime: a few seconds or less.
Input is assets/fourteen_points.json beside this script. Requires repository tools harness.
"""
import json
import sys
from collections import Counter
from itertools import combinations, combinations_with_replacement
from pathlib import Path
from tools import Checker, evidence_parser


def sidon(points):
    sums = [a+b for a,b in combinations_with_replacement(points, 2)]
    return len(sums) == len(set(sums))


def difference_count(points):
    return len({abs(a-b) for a,b in combinations(points, 2)})


def main():
    evidence_parser(__doc__, quick=False).parse_args()
    checker = Checker()
    data = json.loads((Path(__file__).parent / 'assets' / 'fourteen_points.json').read_text())
    points = tuple(data['points'])
    witness = tuple(data['sidon_witness'])
    checker.check('Sidon test counts diagonal sums', not sidon((1,2,3)))
    checker.check('Sidon test accepts empty and singleton sets', sidon(()) and sidon((1,)))
    checker.check('local condition distinguishes weak Sidon examples', difference_count((1,2,3,5)) == 4 and difference_count((1,2,3,6)) == 5)
    valid = len(points) == 14 and len(set(points)) == 14 and all(type(x) is int for x in points)
    checker.check('input has fourteen distinct integers', valid)
    if not valid:
        return checker.finish()
    histogram = Counter(difference_count(b) for b in combinations(points,4))
    nine = list(combinations(points,9))
    passing_nine = [b for b in nine if sidon(b)]
    checker.check('all 1001 four-subsets have at least five absolute differences', sum(histogram.values()) == 1001 and min(histogram) >= 5)
    checker.check('supplied eight-point witness is contained and strong Sidon', len(witness) == 8 and len(set(witness)) == 8 and set(witness) <= set(points) and sidon(witness))
    checker.check('all 2002 nine-subsets fail strong Sidonicity', len(nine) == 2002 and not passing_nine)
    print(json.dumps({'quadruple_difference_histogram':dict(histogram),'nine_subsets_checked':len(nine),'sidon_nine_subsets':len(passing_nine),'sidon_witness':witness,'maximum_sidon_size':8 if not passing_nine and sidon(witness) else None}, sort_keys=True))
    return checker.finish()

if __name__ == '__main__':
    sys.exit(main())

"""Check exact arithmetic for one deterministic butterfly construction.

The owning page proves realization and extension to all large orders.
No optimization, random experiment or graph census is performed.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from itertools import combinations
from pathlib import Path

from tools import Checker, evidence_parser


def main() -> int:
    """Recompute the fixed certificate with exact rational arithmetic."""
    evidence_parser(__doc__, quick=False).parse_args()
    data = json.loads((Path(__file__).parent / 'assets/parameters.json').read_text())
    checker = Checker()
    denominator = data['denominator']
    weights = {
        part: Fraction(value, denominator)
        for part, value in data['part_numerators'].items()
    }
    pairs = {
        tuple(sorted(pair)): Fraction(value, denominator)
        for pair, value in data['pair_density_numerators'].items()
    }
    checker.check(
        'positive part proportions sum to one',
        sum(weights.values()) == 1 and all(weight > 0 for weight in weights.values()),
    )
    checker.check(
        'every pair density is in (0,1]',
        all(0 < density <= 1 for density in pairs.values()),
    )
    degrees = {part: Fraction(0) for part in weights}
    density = Fraction(0)
    for (left, right), value in pairs.items():
        degrees[left] += value * weights[right]
        degrees[right] += value * weights[left]
        density += value * weights[left] * weights[right]
    checker.check(
        'handshaking identity',
        sum(weights[v] * degrees[v] for v in weights) == 2 * density,
    )
    triangles = [
        triple
        for triple in combinations(sorted(weights), 3)
        if all(pair in pairs for pair in combinations(triple, 2))
    ]
    checker.check(
        'the only supported triples are ABC and ADE',
        triangles == [('A', 'B', 'C'), ('A', 'D', 'E')],
    )
    sums = [sum(degrees[v] for v in triangle) for triangle in triangles]
    checker.check(
        'exact triangle degree sums',
        sums
        == [
            Fraction(9149479, 6250000),
            Fraction(29278917, 20000000),
        ],
    )
    surplus = density - Fraction(1, 4)
    checker.check(
        'strict edge surplus with exact value',
        surplus == Fraction(3203943, 500000000000) and surplus > 0,
    )
    bound = Fraction(*data['triangle_sum_bound'])
    checker.check(
        'both triangle sums are strictly below the comparison bound',
        all(value < bound for value in sums),
    )
    checker.check(
        'comparison bound is below twice sqrt(3) minus two',
        bound + 2 > 0 and (bound + 2) ** 2 < 12,
    )
    unit = denominator**2
    cutoff = data['all_order_cutoff']
    checker.check('cutoff exceeds the construction unit', cutoff > unit)
    checker.check(
        'padding inequality at the all-order cutoff',
        density * (1 - Fraction(unit, cutoff)) ** 2 > Fraction(1, 4),
    )
    print(f'edge surplus = {surplus}; triangle sums = {sums}; unit = {unit}')
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

"""Recount the frozen E1033 certificate by integer cardinalities.

This checks the fixed support, input domain and exact integer inequalities.
It does not enumerate a graph or prove the residue/padding transfer. Those
arguments are in report.md. The default input is the retained reviewed input;
--parameters permits the explicit adversarial controls. Runtime is below a
second in the reviewed environment. Only the standard library and tools are
needed; no floating-point arithmetic or cached result is used.
"""

from __future__ import annotations

import json
from pathlib import Path

from tools import Checker, evidence_parser


def main() -> int:
    parser = evidence_parser(__doc__, quick=False)
    parser.add_argument(
        '--parameters',
        type=Path,
        default=Path(__file__).resolve().parents[2]
        / 'assets/review_subject/evidence/assets/parameters.json',
    )
    args = parser.parse_args()
    check = Checker()
    try:
        data = json.loads(args.parameters.read_text())
    except (OSError, ValueError) as error:
        check.check('readable JSON parameter input', False, str(error))
        return check.finish()
    if not check.check('parameter object', isinstance(data, dict)):
        return check.finish()

    m = data.get('denominator')
    if not check.check(
        'positive integer construction denominator', type(m) is int and m > 0
    ):
        return check.finish()
    weights = data.get('part_numerators')
    if not check.check(
        'part cardinalities partition the construction unit',
        isinstance(weights, dict)
        and set(weights) == set('ABCDE')
        and all(type(w) is int and w > 0 for w in weights.values())
        and sum(weights.values()) == m,
    ):
        return check.finish()
    pairs = data.get('pair_density_numerators')
    if not check.check(
        'exact six-pair support with full AB BC AD AE',
        isinstance(pairs, dict)
        and set(pairs) == {'AB', 'BC', 'AD', 'AE', 'AC', 'DE'}
        and all(pairs[pair] == m for pair in ('AB', 'BC', 'AD', 'AE')),
    ):
        return check.finish()
    if not check.check(
        'residue counts are integers between one and M',
        all(type(p) is int and 1 <= p <= m for p in pairs.values()),
    ):
        return check.finish()
    bound = data.get('triangle_sum_bound')
    if not check.check(
        'positive rational comparison bound',
        isinstance(bound, list)
        and len(bound) == 2
        and all(type(v) is int and v > 0 for v in bound),
    ):
        return check.finish()
    cutoff = data.get('all_order_cutoff')
    unit = m * m
    if not check.check(
        'integer cutoff exceeds the construction unit',
        type(cutoff) is int and cutoff > unit,
    ):
        return check.finish()

    # A vertex in part i has s * D_i neighbors. These are direct counts
    # of whole residue classes, not updates from a rational edge-density loop.
    a, b, c, d, e = (weights[part] for part in 'ABCDE')
    x, y = pairs['AC'], pairs['DE']
    degrees = {
        'A': m * (b + d + e) + x * c,
        'B': m * (a + c),
        'C': m * b + x * a,
        'D': m * a + y * e,
        'E': m * a + y * d,
    }

    # For s=1, there are m*S undirected edges. Each summand counts exactly
    # one cross-part edge class; no degree sum is used to obtain this total.
    edge_terms = {
        'AB': m * a * b,
        'BC': m * b * c,
        'AD': m * a * d,
        'AE': m * a * e,
        'AC': x * a * c,
        'DE': y * d * e,
    }
    total = sum(edge_terms.values())
    triangle_abc = degrees['A'] + degrees['B'] + degrees['C']
    triangle_ade = degrees['A'] + degrees['D'] + degrees['E']
    check.check(
        'displayed triangle degree sums from integer degrees',
        triangle_abc * 6250000 == 9149479 * unit
        and triangle_ade * 20000000 == 29278917 * unit,
    )
    surplus_numerator = 4 * total - m**3
    check.check(
        'displayed positive edge surplus from integer edge counts',
        surplus_numerator > 0
        and 500000000000 * surplus_numerator == 4 * m**3 * 3203943,
    )
    numerator, denominator = bound
    triangle_margins = [
        numerator * unit - denominator * triangle_abc,
        numerator * unit - denominator * triangle_ade,
    ]
    check.check(
        'strict triangle margins in integer units',
        all(margin > 0 for margin in triangle_margins),
    )
    irrational_margin = 12 * denominator**2 - (numerator + 2 * denominator) ** 2
    check.check(
        'positive irrational comparison after clearing denominators',
        numerator + 2 * denominator > 0 and irrational_margin > 0,
    )
    padding_margin = 4 * total * (cutoff - unit) ** 2 - m**3 * cutoff**2
    check.check(
        'strict cutoff padding margin in integer units', padding_margin > 0
    )
    print(
        json.dumps(
            {
                'degree_coefficients': degrees,
                'edge_terms': edge_terms,
                'edge_coefficient_S': total,
                'edges_at_s_one': m * total,
                'triangle_coefficients': [triangle_abc, triangle_ade],
                'edge_surplus_numerator_over_4M_cubed': surplus_numerator,
                'triangle_margin_numerators': triangle_margins,
                'irrational_margin_numerator': irrational_margin,
                'padding_margin_numerator_over_4M_cubed_cutoff_squared': padding_margin,
            },
            sort_keys=True,
        )
    )
    return check.finish()


if __name__ == '__main__':
    raise SystemExit(main())

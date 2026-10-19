"""Independent exact reproduction of the finite AP discrepancy claims.

Read claims.json beside this file, or --input. For each (k, claimed_minimum),
compute every length from zero to the claimed minimum. The supported bounded
domains are k=2, N<=3; k=3, N<=9; k=4, N<=13. All arithmetic is integral.

For k=2,3, inclusion-exclusion over monochromatic AP constraints is aggregated
by equivalence partitions. No sign-tuple enumeration is used. Partial-assignment
counts construct the first avoiding witness. For k=4, balanced consecutive
four-blocks force period four; a difference-two block reduces the seeds to
(u,v,-u,-v), and a difference-four block at length 13 eliminates them.
AP constraints use endpoint interpolation, not either author generator.

Outputs retain all counts, first witnesses, endpoint constraints and exact
inclusion-exclusion coefficient polynomials (or recurrence seeds). They are
mathematical data, not a substitute for executing this file. See report.md for
the proofs of the reductions and the precise scope.

Dependencies: Python standard library only. Typical runtime is under a minute,
one thread. Run from the repository root via uv run --no-sync python -B with
--output pointing to explicit scratch. negative_claims.json must fail with
exit status 1, including under python -O. No bare assertions carry checks.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
import json
from pathlib import Path
import sys


CONVENTION = 'ordinary positive-difference APs in [0,N), absolute signed sum >= 2'
CAPS = {2: 3, 3: 9, 4: 13}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def endpoints(k: int, n: int) -> tuple[tuple[int, ...], ...]:
    """A positive AP is uniquely determined by its first and last points."""
    edges = []
    for first in range(n):
        for last in range(first + 1, n):
            span = last - first
            if span % (k - 1) == 0:
                edges.append(tuple(first + j * span // (k - 1) for j in range(k)))
    return tuple(edges)


def progression_count(k: int, n: int) -> int:
    m = max(0, (n - 1) // (k - 1))
    return m * n - (k - 1) * m * (m + 1) // 2


def merge_classes(partition: tuple[int, ...], edge: tuple[int, ...]) -> tuple[int, ...]:
    labels = {partition[v] for v in edge}
    representative = min(labels)
    return tuple(representative if label in labels else label for label in partition)


def ie_partitions(n: int, edges: tuple[tuple[int, ...], ...]) -> dict[tuple[int, ...], int]:
    """Expand product_e (1 - indicator[e monochromatic]) symbolically."""
    terms = {tuple(range(n)): 1}
    for edge in edges:
        expanded = dict(terms)
        for partition, coefficient in terms.items():
            merged = merge_classes(partition, edge)
            expanded[merged] = expanded.get(merged, 0) - coefficient
        terms = {partition: c for partition, c in expanded.items() if c != 0}
    return terms


def conditional_count(terms: dict[tuple[int, ...], int], prefix: tuple[int, ...]) -> int:
    total = 0
    for partition, coefficient in terms.items():
        assigned: dict[int, int] = {}
        compatible = True
        for vertex, sign in enumerate(prefix):
            label = partition[vertex]
            if label in assigned and assigned[label] != sign:
                compatible = False
                break
            assigned[label] = sign
        if compatible:
            free_classes = len(set(partition)) - len(assigned)
            total += coefficient * (1 << free_classes)
    return total


def ie_row(k: int, n: int, edges: tuple[tuple[int, ...], ...]) -> tuple[int, tuple[int, ...] | None, dict]:
    terms = ie_partitions(n, edges)
    count = conditional_count(terms, ())
    require(0 <= count <= 1 << n, f'k={k}, N={n}: impossible inclusion-exclusion count')
    polynomial: dict[int, int] = defaultdict(int)
    for partition, coefficient in terms.items():
        polynomial[len(set(partition))] += coefficient
    coefficients = [[degree, coefficient] for degree, coefficient in sorted(polynomial.items()) if coefficient]
    require(sum(c * (1 << degree) for degree, c in coefficients) == count,
            f'k={k}, N={n}: coefficient polynomial evaluation mismatch')
    witness = None
    prefix_counts = []
    if count:
        prefix: tuple[int, ...] = ()
        parent_count = count
        for vertex in range(n):
            minus = conditional_count(terms, prefix + (-1,))
            plus = conditional_count(terms, prefix + (1,))
            capacity = 1 << (n - vertex - 1)
            require(0 <= minus <= capacity and 0 <= plus <= capacity,
                    f'k={k}, N={n}: impossible conditional count')
            require(minus + plus == parent_count,
                    f'k={k}, N={n}: conditional branches do not partition the parent')
            prefix_counts.append({'vertex': vertex, 'minus_count': minus, 'plus_count': plus})
            chosen = -1 if minus else 1
            prefix += (chosen,)
            parent_count = minus if chosen == -1 else plus
            require(parent_count > 0, f'k={k}, N={n}: witness branch is empty')
        require(parent_count == 1, f'k={k}, N={n}: complete witness has wrong multiplicity')
        witness = prefix
    certificate = {
        'route': 'inclusion-exclusion over monochromatic constraints',
        'nonzero_partition_terms': len(terms),
        'coefficient_polynomial': coefficients,
        'first_witness_prefix_counts': prefix_counts,
    }
    return count, witness, certificate


def recurrence_row(n: int) -> tuple[int, tuple[int, ...] | None, dict]:
    if n < 4:
        return 1 << n, (-1,) * n, {'route': 'no four-point progression', 'seeds': []}
    seeds = []
    if n <= 6:
        for u in (-1, 1):
            for v in (-1, 1):
                for w in (-1, 1):
                    z = -u - v - w
                    if z in (-1, 1):
                        seeds.append((u, v, w, z))
        require(len(seeds) == 6, 'balanced four-symbol seed calculation failed')
    elif n <= 12:
        seeds = [(u, v, -u, -v) for u in (-1, 1) for v in (-1, 1)]
    else:
        require(n == 13, 'four-term recurrence used outside the declared domain')
    sequences = [tuple(seed[i % 4] for i in range(n)) for seed in seeds]
    count = len(sequences)
    witness = min(sequences) if sequences else None
    return count, witness, {'route': 'balanced four-block recurrence', 'seeds': seeds}


def compute_case(k: int, bound: int) -> tuple[dict, dict, list[str]]:
    require(type(k) is int and k in CAPS, 'k must be one of 2, 3, 4')
    require(type(bound) is int and 0 <= bound <= CAPS[k], 'claimed bound outside the bounded input domain')
    rows = []
    certificates = []
    for n in range(bound + 1):
        edges = endpoints(k, n)
        ap_count = progression_count(k, n)
        require(len(edges) == ap_count and len(set(edges)) == ap_count,
                f'k={k}, N={n}: endpoint inventory disagrees with the closed count')
        require(all(len(e) == k and e[0] >= 0 and e[-1] < n and e[0] < e[-1]
                    for e in edges), f'k={k}, N={n}: bad endpoint inventory')
        if k < 4:
            count, witness, certificate = ie_row(k, n, edges)
        else:
            count, witness, certificate = recurrence_row(n)
        if witness is not None:
            require(len(witness) == n and all(s in (-1, 1) for s in witness),
                    f'k={k}, N={n}: malformed witness')
            require(all(abs(sum(witness[v] for v in edge)) < 2 for edge in edges),
                    f'k={k}, N={n}: returned witness has a large AP')
        require((witness is not None) == (count > 0), f'k={k}, N={n}: missing or spurious witness')
        certificate['N'] = n
        certificate['endpoint_progressions'] = edges
        certificates.append(certificate)
        rows.append({'N': n, 'ap_count': ap_count, 'colorings': 1 << n,
                     'avoiding_colorings': count, 'first_avoiding_coloring': witness})
    failures = []
    if rows[-1]['avoiding_colorings'] != 0:
        failures.append(f'k={k}: claimed minimum {bound} still has {rows[-1]["avoiding_colorings"]} avoiding colorings')
    if any(row['avoiding_colorings'] == 0 for row in rows[:-1]):
        failures.append(f'k={k}: a smaller length already has the universal property')
    return ({'k': k, 'claimed_minimum': bound, 'rows': rows},
            {'k': k, 'rows': certificates}, failures)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, default=Path(__file__).with_name('claims.json'))
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    specification = json.loads(args.input.read_text())
    require(specification.get('convention') == CONVENTION, 'input convention differs')
    cases = specification.get('cases')
    require(isinstance(cases, list) and bool(cases), 'input must contain cases')
    records = []
    certificates = []
    failures = []
    for case in cases:
        record, certificate, case_failures = compute_case(case['k'], case['claimed_minimum'])
        records.append(record)
        certificates.append(certificate)
        failures.extend(case_failures)
    result = {
        'coverage': 'exact constraint inclusion-exclusion and four-block recurrence',
        'total_colorings_represented': sum(row['colorings'] for r in records for row in r['rows']),
        'records': records,
        'certificates': certificates,
        'failures': failures,
    }
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    for record in records:
        counts = [row['avoiding_colorings'] for row in record['rows']]
        print(f'k={record["k"]}: avoiding counts {counts}')
    for failure in failures:
        print('FAIL: ' + failure)
    if failures:
        return 1
    print('Independent finite claims verified by the specified exact routes.')
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, KeyError, TypeError, OSError) as error:
        print('ERROR: ' + str(error), file=sys.stderr)
        raise SystemExit(2) from error

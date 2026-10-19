"""Recompute all divisor-prefix minima for target sums 2 through 64.

Exact integer arithmetic; repository tools harness and Python standard library.
The mathematical compression proof makes the search complete over original
integers n. All 83,691 distinct-part partitions are checked, independently
counted by subset-sum dynamic programming, and crosschecked by a divisor sieve
up to 10,000. Runtime less than one minute. No asymptotic conclusion.
Inputs resolve beside this script; no output is needed for a later run.
"""
import json
import sys
from math import lcm
from pathlib import Path
from tools import Checker, evidence_parser


def partitions(remaining, first=2, parts=()):
    if remaining == 0:
        yield parts
        return
    for part in range(first, remaining + 1):
        if remaining != part and remaining - part <= part:
            continue
        yield from partitions(remaining - part, part + 1, parts + (part,))


def prefix(candidate, maximum):
    return tuple(d for d in range(2, maximum + 1) if candidate % d == 0)


def main():
    evidence_parser(__doc__, quick=False).parse_args()
    checker = Checker()
    assets = Path(__file__).resolve().parent / 'assets'
    scope = json.loads((assets / 'input.json').read_text())
    expected = json.loads((assets / 'values.json').read_text())
    valid = scope == {'minimum_target': 2, 'maximum_target': 64,
                      'brute_crosscheck_limit': 10000}
    checker.check('input is the complete stated finite domain', valid)
    if not valid:
        return checker.finish()
    low, high, bound = 2, 64, 10000
    counts = [0] * (high + 1)
    counts[0] = 1
    for part in range(2, high + 1):
        for total in range(high, part - 1, -1):
            counts[total] += counts[total - part]
    rows = []
    partition_validity = True
    domain_complete = True
    for target in range(low, high + 1):
        domain = list(partitions(target))
        partition_validity &= all(sum(p) == target and min(p) >= 2
                                  and tuple(sorted(set(p))) == p for p in domain)
        domain_complete &= len(domain) == len(set(domain)) == counts[target]
        best = None
        witness = None
        for parts in domain:
            candidate = lcm(*parts)
            if prefix(candidate, parts[-1]) != parts:
                continue
            if best is None or candidate < best:
                best, witness = candidate, parts
        rows.append({'N': target, 'f': best,
                     'prefix': list(witness) if witness is not None else None,
                     'partitions_tested': len(domain)})
    checker.check('every enumerated partition is valid', partition_validity)
    checker.check('partition domain matches independent counts without repeats', domain_complete)
    checker.check('all minima and witnesses match the complete retained table', rows == expected['rows'])
    small = [None] * (high + 1)
    sums = [0] * (bound + 1)
    for divisor in range(2, bound + 1):
        for integer in range(divisor, bound + 1, divisor):
            sums[integer] += divisor
            target = sums[integer]
            if low <= target <= high:
                if small[target] is None or integer < small[target]:
                    small[target] = integer
    checker.check('independent divisor sieve agrees at every target',
                  all(row['f'] == small[row['N']] for row in rows))
    boundary = {2: 2, 3: 3, 4: None, 5: 5, 6: 4}
    checker.check('manual boundary cases and the missing value 4 agree',
                  all(row['f'] == boundary[row['N']] for row in rows if row['N'] in boundary)
                  and [row['N'] for row in rows if row['f'] is None] == [4])
    maxima = [row for row in rows if row['f'] == 265]
    checker.check('maximum finite minimum is 265 at target 58',
                  max(row['f'] or 0 for row in rows) == 265
                  and [row['N'] for row in maxima] == [58]
                  and maxima[0]['prefix'] == [5, 53])
    checker.check('full partition count is 83691',
                  sum(row['partitions_tested'] for row in rows) == 83691)
    print(json.dumps({'targets': len(rows), 'unrepresented': [4],
                      'maximum_minimum': 265, 'partitions': 83691}))
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

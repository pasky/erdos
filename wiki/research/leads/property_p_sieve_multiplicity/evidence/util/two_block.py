"""Exact two-block upper bound by exhaustive early subsets and edge matchings.

There are 14 early candidates in (125,187.5). Later intervals start at
625, 3125, 15625 and 78125. Each candidate is p*q with p in {2,3,5}
and q prime. Each block is automatically P.
For each of the 2**14 early subsets, remove every later vertex forbidden
by two early elements, then greedily match disjoint forbidden pairs of later
vertices. A matching loses at least the smaller weight on each edge. Rounding
reciprocals upward to multiples of 10**-9 gives a rigorous upper bound using
only integers. This relaxation does not assert the exact optimum.
"""

from __future__ import annotations

import json
from collections.abc import Callable
from fractions import Fraction
from pathlib import Path

from tools import Checker

from .normalization import harmonic, primes_up_to


def matching_bound(
    early: list[int], late: list[int], scale: int
) -> tuple[int, int, bool]:
    """Cover all early subsets by exact rounded upper bounds; check every edge."""
    weights = [(scale + n - 1) // n for n in late]
    early_weights = [(scale + n - 1) // n for n in early]
    valid = all(
        n * w >= scale and n * (w - 1) < scale
        for n, w in zip(early + late, early_weights + weights, strict=True)
    )
    all_late = (1 << len(late)) - 1
    residues: list[dict[int, int]] = []
    graph: list[list[int]] = []
    for a in early:
        bins: dict[int, int] = {}
        for j, n in enumerate(late):
            bins[n % a] = bins.get(n % a, 0) | (1 << j)
        residues.append(bins)
        graph.append([bins.get((-n) % a, 0) & ~(1 << j) for j, n in enumerate(late)])
    forbidden = [[0] * len(early) for _ in early]
    for i, a in enumerate(early):
        for j, b in enumerate(early):
            if a < b:
                forbidden[i][j] = residues[i].get((-b) % a, 0)

    best = 0
    examined = 0
    for mask in range(1 << len(early)):
        examined += 1
        indices = [i for i in range(len(early)) if mask >> i & 1]
        first = sum(early_weights[i] for i in indices)
        banned = 0
        for i in indices:
            for j in indices:
                if i < j:
                    banned |= forbidden[i][j]
        active = all_late & ~banned
        available = []
        bits = active
        while bits:
            bit = bits & -bits
            j = bit.bit_length() - 1
            bits ^= bit
            available.append(j)
        upper = first + sum(weights[j] for j in available)
        if upper <= best:
            continue
        remaining = active
        loss = 0
        while remaining:
            bit = remaining & -remaining
            j = bit.bit_length() - 1
            remaining ^= bit
            partners = 0
            for i in indices:
                partners |= graph[i][j]
            partners &= remaining
            if partners:
                partner = partners & -partners
                k = partner.bit_length() - 1
                remaining ^= partner
                valid &= j != k and any(
                    (late[j] + late[k]) % early[i] == 0 for i in indices
                )
                loss += min(weights[j], weights[k])
        best = max(best, upper - loss)
    return best, examined, valid


def check_two_blocks(checker: Checker, property_p: Callable[[list[int]], bool]) -> None:
    """Replay the feasible witness and all four exhaustive upper bounds."""
    scale = 10**9
    primes = primes_up_to(3 * 78125 // 4)

    def candidates(base: int) -> list[int]:
        return sorted(
            {
                p * q
                for p in (2, 3, 5)
                for q in primes
                if 2 * base < 2 * p * q < 3 * base
            }
        )

    early = candidates(125)
    checker.check('two blocks: complete early candidate count is 14', len(early) == 14)
    checker.check('two blocks: full early block has property P', property_p(early))
    witness_late = candidates(15625)
    checker.check(
        'two blocks: separate masses at start 15625 sum to more than 0.137',
        harmonic(early) + harmonic(witness_late) > Fraction(137, 1000),
    )

    asset = Path(__file__).resolve().parents[1] / 'assets' / 'two_block.json'
    row = json.loads(asset.read_text())
    chosen = row['selected']
    checker.check(
        'two blocks: retained witness has the specified domain',
        row['small_primes'] == [2, 3, 5]
        and row['interval_starts'] == [125, 15625]
        and len(set(chosen)) == len(chosen)
        and set(chosen) <= set(early + witness_late),
    )
    checker.check(
        'two blocks: direct property-P check of joint witness', property_p(chosen)
    )
    checker.check(
        'two blocks: exact retained mass exceeds 0.0929',
        harmonic(chosen) == Fraction(row['mass'])
        and harmonic(chosen) > Fraction(929, 10000),
    )

    # Starts, complete late counts, claimed upper numerators, rounded table masses.
    for base, count, upper, mass in (
        (625, 57, 111012802, 164102),
        (3125, 217, 105285764, 146748),
        (15625, 902, 101959737, 137276),
        (78125, 3852, 100627648, 130341),
    ):
        late = candidates(base)
        checker.check(
            f'two blocks {base}: complete late count {count}', len(late) == count
        )
        checker.check(
            f'two blocks {base}: automatic-P interval hypotheses',
            len(set(late)) == len(late)
            and all(2 * base < 2 * n < 3 * base for n in late),
        )
        if base <= 15625:
            checker.check(f'two blocks {base}: direct property P', property_p(late))
        checker.check(
            f'two blocks {base}: rounded separate mass in the table',
            abs(harmonic(early) + harmonic(late) - Fraction(mass, 10**6))
            < Fraction(1, 2 * 10**6),
        )
        best, examined, valid = matching_bound(early, late, scale)
        checker.check(
            f'two blocks {base}: every early subset covered', examined == 16384
        )
        checker.check(
            f'two blocks {base}: upward rounding and forbidden disjoint matching edges',
            valid,
        )
        checker.check(
            f'two blocks {base}: integer upper bound {upper}/{scale}', best <= upper
        )
        if base == 15625:
            checker.check(
                'two blocks: feasible exact mass lies below the exhaustive upper bound',
                harmonic(chosen) <= Fraction(best, scale),
            )

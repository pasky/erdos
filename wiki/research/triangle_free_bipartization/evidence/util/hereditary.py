"""Exact finite controls for the hereditary comparison identity.

For a maximum-cut colouring chi and every vertex set U, the source-dependent
comparison is 47 sum_U sigma - 94 cross_chi(G[U]) + 4 |U|^2 >= 0.
The general proof is in the owning sketch and imports the uniform source
bound; these finite controls do not reprove that source theorem. All subsets
of four small graphs are checked in integer arithmetic. A deliberately false
bound is rejected on C5, and the boundary-edge identity is checked separately.
Fractional selections on C5 and C7 and balanced optimal-cut mixtures on the
four transitive controls check the formulas in the weighted-extremal reduction;
they do not prove that a control weighting is a global weighted optimum.
"""
from __future__ import annotations

from fractions import Fraction

import numpy as np
from util.envelopes import all_cut_costs, cycle, edges_of, petersen
from util.mixtures import circulant
from util.switching_trap import profile_numerators, template

from tools import Checker


def hereditary_clauses(checker: Checker) -> None:
    """Check the finite identity and source-bound controls on all vertex subsets."""
    for name, adjacency in (
        ('C5', cycle(5)),
        ('C7', cycle(7)),
        ('Petersen', petersen()),
        ('C13(1,5)', circulant(13, {1, 5, 8, 12})),
    ):
        n = len(adjacency)
        cut_masks, costs = all_cut_costs(adjacency)
        mask = int(cut_masks[int(costs.argmin())])
        colour = (mask >> np.arange(n)) & 1
        same = colour[:, None] == colour[None, :]
        slack = (adjacency * np.where(same, -1, 1)).sum(axis=1)
        subsets = np.arange(1 << n, dtype=np.int64)
        inside = ((subsets[:, None] >> np.arange(n)) & 1).astype(np.int64)
        size = inside.sum(axis=1)
        cross_inside = np.zeros(len(subsets), dtype=np.int64)
        mono_inside = np.zeros_like(cross_inside)
        boundary = np.zeros_like(cross_inside)
        mono_boundary = np.zeros_like(cross_inside)
        for u, v in edges_of(adjacency):
            internal = inside[:, u] * inside[:, v]
            across = inside[:, u] != inside[:, v]
            boundary += across
            if same[u, v]:
                mono_inside += internal
                mono_boundary += across
            else:
                cross_inside += internal
        sigma = inside @ slack
        identity = np.array_equal(
            2 * cross_inside - sigma,
            2 * mono_inside + 2 * mono_boundary - boundary,
        )
        comparison = 47 * sigma - 94 * cross_inside + 4 * size**2
        checker.check(
            f'hereditary comparison: {name}, every one of {len(subsets)} subsets '
            'satisfies the boundary identity and the 4/47 comparison',
            identity and bool(np.all(comparison >= 0)),
        )
        # All minimum-cost cuts modulo colour complement form an invariant
        # finite set. The uniform mixture balances monochromatic degrees in
        # these vertex-transitive controls; this is not a test of global
        # optimality over vertex weights.
        active = cut_masks[costs == costs.min()]
        totals = np.zeros(n, dtype=np.int64)
        for active_mask in active:
            side = (int(active_mask) >> np.arange(n)) & 1
            totals += (adjacency * (side[:, None] == side[None, :])).sum(axis=1)
        target = 2 * int(costs.min()) * len(active)
        checker.check(
            f'weighted-extremal identity control: {name}, the uniform mixture '
            f'of {len(active)} optimal cuts has constant monochromatic degree',
            bool(np.all(n * totals == target)),
        )
        if name in {'C5', 'C7'}:
            # q_i in {0, 1/2, 1}; after multiplying R_(4/47) by 4*47*n^2
            # the formula is 94 q.sigma - 47 q^T C q + 4(sum q)^2,
            # where q now denotes the integer numerators and C is ordered.
            labels = np.arange(3**n, dtype=np.int64)
            selection = (labels[:, None] // (3 ** np.arange(n))) % 3
            cross_matrix = adjacency * ~same
            quadratic = np.einsum(
                'ai,ij,aj->a', selection, cross_matrix, selection,
            )
            comparison = (
                94 * (selection @ slack) - 47 * quadratic
                + 4 * selection.sum(axis=1)**2
            )
            checker.check(
                f'fractional hereditary control: {name}, all {3**n} selections '
                'with weights in {0,1/2,1} satisfy the 4/47 row',
                bool(np.all(comparison >= 0)),
            )
            # Ternary labels -1,0,1 fix the outside cut and leave label zero
            # for an optimal recursive cut. Twice its expected cost minus
            # 2 D2, multiplied by 47, has the following integer numerator.
            sides = selection - 1
            free = (sides == 0).astype(np.int64)
            edges_twice = int(adjacency.sum())
            fixed_quadratic = np.einsum('ai,ij,aj->a', sides, adjacency, sides)
            free_quadratic = np.einsum('ai,ij,aj->a', free, adjacency, free)
            numerator = (
                47 * (edges_twice + fixed_quadratic - free_quadratic
                      - 4 * int(costs.min()))
                + 8 * free.sum(axis=1)**2
            )
            checker.check(
                f'recursive partial-cut control: {name}, all {3**n} ternary '
                'assignments satisfy the 4/47 comparison',
                bool(np.all(numerator >= 0)),
            )
            four_labels = np.arange(4**n, dtype=np.int64)
            choices = (four_labels[:, None] // (4 ** np.arange(n))) % 4 - 1
            fixed = np.where(abs(choices) == 1, choices, 0)
            recursive = (choices == 0).astype(np.int64)
            fixed_term = np.einsum('ai,ij,aj->a', fixed, adjacency, fixed)
            recursive_term = np.einsum('ai,ij,aj->a', recursive, adjacency, recursive)
            randomized_row = (
                47 * (edges_twice + fixed_term - recursive_term - 4 * int(costs.min()))
                + 8 * recursive.sum(axis=1)**2
            )
            checker.check(
                f'randomized recursive control: {name}, all {4**n} assignments '
                'to two fixed sides, a recursive part, or independent fair coins',
                bool(np.all(randomized_row >= 0)),
            )
            six_labels = np.arange(6**n, dtype=np.int64)
            choices = (six_labels[:, None] // (6 ** np.arange(n))) % 6
            signs_twice = np.array([-2, -1, 0, 1, 2, 0], dtype=np.int64)[choices]
            recursive = (choices == 5).astype(np.int64)
            fixed_term = np.einsum('ai,ij,aj->a', signs_twice, adjacency, signs_twice)
            recursive_term = np.einsum('ai,ij,aj->a', recursive, adjacency, recursive)
            quarter_coin_row = (
                47 * (4 * edges_twice + fixed_term - 4 * recursive_term
                      - 16 * int(costs.min()))
                + 32 * recursive.sum(axis=1)**2
            )
            checker.check(
                f'quarter-coin recursive control: {name}, all {6**n} assignments '
                'to a recursive part or independent coins of bias 0,1/4,1/2,3/4,1',
                bool(np.all(quarter_coin_row >= 0)),
            )
            if name == 'C5':
                # At its weighted optimum B=2/25, the induction row is
                # e + z^T A z/2 - u^T A u/2 - B(n^2-|U|^2).
                induction = (
                    25 * (edges_twice + fixed_quadratic - free_quadratic)
                    - 4 * (n**2 - free.sum(axis=1)**2)
                )
                checker.check(
                    'recursive induction boundary control: every C5 ternary '
                    'assignment satisfies the 2/25 induction row',
                    bool(np.all(induction >= 0)) and int(induction.min()) == 0,
                )
        if name == 'C5':
            mono_degrees = []
            for active_mask in active:
                side = (int(active_mask) >> np.arange(n)) & 1
                mono_degrees.append(
                    (adjacency * (side[:, None] == side[None, :])).sum(axis=1),
                )
            degree_table = np.array(mono_degrees, dtype=np.int64)
            independent = Fraction(
                int((degree_table.sum(axis=0)**2).sum()), n**3 * len(active)**2,
            )
            dependent = Fraction(
                int((degree_table**2).sum()), n**3 * len(active),
            )
            checker.check(
                'independent active-cut control: C5 has mean product of '
                'monochromatic degrees 4/625',
                independent == Fraction(4, 625),
            )
            checker.check(
                'active-cut independence negative control: using the same '
                'C5 cut twice exceeds that product by 6/625',
                dependent - independent == Fraction(6, 625),
            )
            # For every ordered five-root tuple, explicitly enumerate the
            # 5 x 5 pairs of active cuts and compare with the outer product
            # of their integer pattern counts. Complementary patterns merge.
            roots = np.indices((5,)*5, dtype=np.int16).reshape(5, -1)
            pattern_counts = np.zeros((5**5, 16), dtype=np.int64)
            patterns = []
            for active_mask in active:
                side = (int(active_mask) >> np.arange(n)) & 1
                code = (side[roots].T * (1 << np.arange(5))).sum(axis=1)
                pattern = np.minimum(code, 31 ^ code)
                patterns.append(pattern)
                pattern_counts[np.arange(5**5), pattern] += 1
            joint = np.zeros((5**5, 16, 16), dtype=np.int64)
            for first in patterns:
                for second in patterns:
                    joint[np.arange(5**5), first, second] += 1
            checker.check(
                'cut-pattern Gram control: every C5 five-root tuple gives '
                'the exact outer product of independent pattern counts',
                np.array_equal(
                    joint,
                    pattern_counts[:, :, None] * pattern_counts[:, None, :],
                ),
            )
            checker.check(
                'weighted-extremal negative control: one maximum cut of C5 '
                'does not have constant monochromatic degree',
                len(set((adjacency * same).sum(axis=1).tolist())) > 1,
            )
            # B=7/100 is false: the whole-set row is B*n^2 - 2*D2(G).
            false_row = 100 * sigma[-1] - 200 * cross_inside[-1] + 7 * n**2
            checker.check(
                'hereditary comparison negative control: B=7/100 is rejected on C5',
                false_row == -25 and false_row < 0,
            )

    # A stronger global-optimality row excludes the limiting two-root trap.
    # Membership in U is mask 41 on the two-root coloured profiles.
    adjacency, colours = template()
    probabilities = profile_numerators(adjacency, colours, (2, 3), 7, 8)
    membership = probabilities[:, [0, 3, 5]].sum(axis=1)
    signed = adjacency * np.where(colours[:, None] == colours[None, :], -1, 1)
    crossing = adjacency * (colours[:, None] != colours[None, :])
    linear = int(membership @ signed.sum(axis=1))
    quadratic = int(membership @ crossing @ membership)
    total = int(membership.sum())
    numerator = 47 * 7 * (64 * linear - quadratic) + 32 * total**2
    value = Fraction(numerator, 47 * 16**2 * 8**5)
    checker.check(
        'hereditary comparison: roots (2,3), subset mask 41 give the exact '
        'limiting value -1077/1540096 on the two-root trap',
        value == Fraction(-1077, 1540096) < 0,
    )

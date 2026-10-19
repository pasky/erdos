"""Weighted minimum-uncut (maximum-cut) by mixed-integer programming.

Used for numerical optimality reports: scipy's HiGHS branch and bound on
integer data, with relative gap zero. The returned cut is re-evaluated
exactly by the caller; the optimality of its value rests on the solver.
"""

from __future__ import annotations

import math
import warnings
from collections import Counter

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix


def solver_minimum_uncut(table: Counter, seconds: float = 120) -> tuple[dict[int, int], bool]:
    """Return a proposed rule and whether HiGHS reported numerical optimality.

    A positive time bound and one HiGHS thread are used. Timeout is not
    optimality. Variables are one side bit per profile and one cut bit per weighted pair;
    a pair counts as cut only when its two side bits differ. The weights are
    divided by their greatest common divisor before solving.
    """
    if not math.isfinite(seconds) or seconds <= 0:
        raise ValueError('a finite positive solver time limit is required')
    nodes = sorted({x for pair in table for x in pair})
    position = {v: i for i, v in enumerate(nodes)}
    divisor = 0
    for weight in table.values():
        divisor = math.gcd(divisor, weight)
    pairs = [(position[a], position[b], w // divisor) for (a, b), w in table.items() if a != b]
    m, count = len(nodes), len(pairs)
    if count == 0:
        return dict.fromkeys(nodes, 0), True
    objective = np.concatenate([np.zeros(m), -np.array([w for _, _, w in pairs], dtype=float)])
    rows = lil_matrix((2 * count, m + count))
    upper = np.zeros(2 * count)
    for t, (i, j, _) in enumerate(pairs):
        rows[2 * t, m + t], rows[2 * t, i], rows[2 * t, j] = 1, -1, -1
        rows[2 * t + 1, m + t], rows[2 * t + 1, i], rows[2 * t + 1, j] = 1, 1, 1
        upper[2 * t + 1] = 2
    high = np.ones(m + count)
    high[0] = 0
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore', category=RuntimeWarning,
                                message='Unrecognized options detected')
        result = milp(
            objective,
            constraints=LinearConstraint(rows.tocsr(), -np.inf, upper),
            integrality=np.ones(m + count),
            bounds=Bounds(np.zeros(m + count), high),
            options={'disp': False, 'mip_rel_gap': 0, 'time_limit': seconds,
                     'threads': 1, 'parallel': False},
        )
    if result.x is None:
        return dict.fromkeys(nodes, 0), False
    sides = np.round(result.x[:m]).astype(int)
    return {v: int(sides[position[v]]) for v in nodes}, bool(result.status == 0)

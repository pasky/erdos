"""Explore two-colorings of the 3-subset boundaries of [7] by alternating solver calls.

This is a retained inconclusive diagnostic and it produces no evidence. The
only instance is (n, k, q) = (7, 3, 2). The script builds the complete
triangle-to-edge boundary matrix, starts from the elementary tetrahedral
boundary supports, and alternates a binary coloring feasibility problem
(every known support must meet both colors) with two ternary
relation-separation problems, one per color class, adding each monochromatic
relation found as a new support. Every returned relation is checked by exact
integer matrix multiplication before it is added. The caps are 100 rounds,
at most three solver calls per round and 10 seconds per call. In the
original run the round cap was reached with 156 support constraints and
neither a proper-color certificate nor an infeasibility certificate was
obtained. Progress lines go to standard output and the final state to the
ignored ``output/`` folder.

Run from the repository root:
    uv run --no-sync python wiki/research/erdos_774/evidence/simplicial_7_3/produce.py

Dependencies beyond the standard library are NumPy and SciPy (HiGHS through
``scipy.optimize.milp``), which the repository does not declare; install
them separately before running. Solver-dependent choices need not reproduce
the same intermediate constraints; the bounds and question are exact. There
is no mathematical conclusion from this test.
"""

from __future__ import annotations

import itertools
import json
import pathlib
import time

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import csc_array

__all__ = [
    'main',
]

# write disposable products beside this script under the ignored output folder
_OUTPUT = pathlib.Path(__file__).with_name('output') / 'simplicial_7_3.json'

# fix the single instance and the caps
_N, _K = 7, 3
_ROUNDS = 100
_TIME_LIMIT = 10


def main() -> int:
    """Run the alternating search and record its final state."""
    faces = list(itertools.combinations(range(_N), _K))
    position = {x: i for i, x in enumerate(faces)}
    rows = list(itertools.combinations(range(_N), _K - 1))
    row_position = {x: i for i, x in enumerate(rows)}
    boundary = np.zeros((len(rows), len(faces)), dtype=np.int64)
    for j, face in enumerate(faces):
        for t in range(_K):
            boundary[row_position[face[:t] + face[t + 1:]], j] = (-1) ** t
    supports: set[tuple[int, ...]] = set()
    for u in itertools.combinations(range(_N), _K + 1):
        supports.add(tuple(position[u[:t] + u[t + 1:]] for t in range(_K + 1)))
    started = time.time()
    outcome = 'RANGE_FINISHED'
    colors = None
    for round_index in range(_ROUNDS):
        # ask for a two-coloring meeting every known support in both colors
        constraints = np.zeros((len(supports) + 1, len(faces)))
        low, high = [], []
        for r, support in enumerate(supports):
            constraints[r, list(support)] = 1
            low.append(1)
            high.append(len(support) - 1)
        constraints[-1, 0] = 1
        low.append(0)
        high.append(0)
        solution = milp(
            np.zeros(len(faces)), integrality=np.ones(len(faces)), bounds=Bounds(0, 1),
            constraints=LinearConstraint(csc_array(constraints), low, high),
            options={'time_limit': _TIME_LIMIT},
        )
        if solution.x is None:
            outcome = f'COLOR_STATUS {solution.status} {solution.message}'
            print(outcome, flush=True)
            break
        colors = np.rint(solution.x).astype(int)
        if not all(1 <= sum(colors[list(support)]) <= len(support) - 1 for support in supports):
            raise ValueError('solver returned a coloring violating a known support')
        added = 0
        unresolved = False
        # look for a monochromatic ternary relation in each color class
        for color in (0, 1):
            chosen = np.flatnonzero(colors == color)
            s = len(chosen)
            block = boundary[:, chosen]
            matrix = np.vstack([np.hstack([block, -block]), np.hstack([np.eye(s), np.eye(s)]), np.ones((1, 2 * s))])
            lower = np.r_[np.zeros(len(rows)), np.zeros(s), 1]
            upper = np.r_[np.zeros(len(rows)), np.ones(s), s]
            relation = milp(
                np.zeros(2 * s), integrality=np.ones(2 * s), bounds=Bounds(0, 1),
                constraints=LinearConstraint(csc_array(matrix), lower, upper),
                options={'time_limit': _TIME_LIMIT},
            )
            if relation.x is not None:
                x = np.rint(relation.x).astype(int)
                z = x[:s] - x[s:]
                if not (np.any(z) and np.all(block @ z == 0) and np.all(abs(z) <= 1)):
                    raise ValueError('solver returned a vector that is not an exact ternary relation')
                supports.add(tuple(sorted(chosen[np.flatnonzero(z)])))
                added += 1
            elif relation.status != 2:
                unresolved = True
        if round_index % 5 == 0:
            print(
                'ROUND', round_index, 'events', len(supports), 'sizes', np.bincount(colors).tolist(),
                'added', added, 'unknown', unresolved, 'seconds', round(time.time() - started, 2), flush=True,
            )
        if not added:
            outcome = 'CANDIDATE' if unresolved else 'CERTIFIED_COLORING'
            print(outcome, colors.tolist(), flush=True)
            print('COLOR_ZERO', [tuple(i + 1 for i in faces[j]) for j in range(len(faces)) if colors[j] == 0], flush=True)
            break
    else:
        print(outcome, len(supports), flush=True)
    _OUTPUT.parent.mkdir(exist_ok=True)
    _OUTPUT.write_text(json.dumps({
        'outcome': outcome, 'supports': len(supports), 'seconds': time.time() - started,
        'colors': None if colors is None else colors.tolist(),
    }, indent=2) + '\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

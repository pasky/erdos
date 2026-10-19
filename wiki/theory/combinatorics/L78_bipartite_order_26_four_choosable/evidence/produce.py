"""Discover the weighted-count certificates of L78 by linear programming (discovery only).

For each side split (left, right), left + right = 26, solve the linear program:
minimize (left - 2) * u + right * v over nonnegative profile weights y(t1,t2,t3)
(t1, t2 in 1..4, t3 in 0..9) with total weight 1, subject to u >= the left event
weight and v >= the right event weight of every four-subset type
(|X cap A1|, |X cap A2|, |X cap W|) other than the types of A1 and A2. The event
weights per type are the closed counts
  left:  sum_y y * C(4-x1,t1) C(4-x2,t2) C(9-x3,t3)
  right: sum_y y * C(4-x1,t1-x1) C(4-x2,t2-x2) C(9-x3,t3-x3).
An optimum below 1 is rounded to integer weights (largest weight 10^6) and
written to ``output/certificates.json`` in the format of
``assets/certificates.json``. The written file is a proposal: ``main.py``
re-checks the retained asset exactly over all palette subsets, and nothing here
is evidence.

Run from the repository root:
    uv run --no-sync python wiki/theory/combinatorics/L78_bipartite_order_26_four_choosable/evidence/produce.py

Dependencies: numpy and scipy (HiGHS). Runtime: a few seconds.
"""

from __future__ import annotations

import json
from math import comb
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

__all__ = [
    'solve_split',
    'main',
]

_OUTPUT = Path(__file__).resolve().parent / 'output'


def C(n: int, k: int) -> int:
    """Return the binomial coefficient, zero outside 0 <= k <= n."""
    return comb(n, k) if 0 <= k <= n else 0


def solve_split(left: int, right: int, k: int = 4, n: int = 17) -> tuple[float, list[list[int]]]:
    """Return the LP optimum and the rounded integer weight rows for one split."""
    w = n - 2 * k
    types = [(x1, x2, k - x1 - x2) for x1 in range(k + 1) for x2 in range(k + 1 - x1) if k - x1 - x2 <= w]
    types = [t for t in types if t not in [(k, 0, 0), (0, k, 0)]]
    profs = [(t1, t2, t3) for t1 in range(1, k + 1) for t2 in range(1, k + 1) for t3 in range(w + 1)]
    P = len(profs)
    cost = np.zeros(P + 2)
    cost[P], cost[P + 1] = left - 2, right
    rows, rhs = [], []
    for side in (0, 1):
        for x1, x2, x3 in types:
            r = np.zeros(P + 2)
            for i, (t1, t2, t3) in enumerate(profs):
                if side == 0:
                    r[i] = C(k - x1, t1) * C(k - x2, t2) * C(w - x3, t3)
                else:
                    r[i] = C(k - x1, t1 - x1) * C(k - x2, t2 - x2) * C(w - x3, t3 - x3)
            r[P + side] = -1
            rows.append(r)
            rhs.append(0)
    total = np.zeros((1, P + 2))
    total[0, :P] = [C(k, t1) * C(k, t2) * C(w, t3) for t1, t2, t3 in profs]
    res = linprog(cost, A_ub=np.array(rows), b_ub=rhs, A_eq=total, b_eq=[1], bounds=[(0, None)] * (P + 2), method='highs')
    y = res.x[:P]
    scale = 10**6 / max(y)
    weights = [[*p, int(round(v * scale))] for p, v in zip(profs, y) if int(round(v * scale))]
    return float(res.fun), weights


def main() -> None:
    """Solve every split and write the proposed certificates to the ignored output folder."""
    splits = []
    for left in range(2, 25):
        value, weights = solve_split(left, 26 - left)
        print(f'split ({left},{26 - left}): LP optimum {value:.6f}, {len(weights)} weighted profiles')
        splits.append({'left': left, 'right': 26 - left, 'weights': sorted(weights)})
    _OUTPUT.mkdir(exist_ok=True)
    out = {'colours': 17, 'list_size': 4, 'order': 26, 'fixed_left': [[0, 1, 2, 3], [4, 5, 6, 7]], 'splits': splits}
    (_OUTPUT / 'certificates.json').write_text(json.dumps(out) + '\n')
    print(f'wrote {_OUTPUT / "certificates.json"}')


if __name__ == '__main__':
    main()

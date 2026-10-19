"""Search for localized rooted contradiction certificates on a density interval.

This is a discovery program, not evidence. For a triangle-free graphon W
with a <= p(W) <= b and d_mono(W) >= t, util/flaglp.py builds rows of
induced densities of order 7 or 8 that are nonnegative under that
hypothesis, and searches by floating-point linear programming for a
nonnegative combination that is negative on every triangle-free graph of
that order (a certificate that d_mono < t on [a, b]). It reports eps at the
start threshold, optional rounds of eigenvector squares, and a bisection
bracket for thresholds at which it finds a positive numerical margin. A
candidate certificate would still have to be recovered in exact rational arithmetic
and checked; nothing printed here is a proof or an obstruction.

With --game it also maximizes, over mixtures of a fixed library of genuine
triangle-free graphons with density in [a, b], the least cut row at the
start threshold, by cutting planes (order 7 only). A positive value would
propose a mixture of genuine graphons that no certificate from these rows
can exclude, to be checked exactly; a negative value only reports that this
library is excluded.

With --products it adds products of two cut rows on the same roots, valid
under the hypothesis because both factors are nonnegative.

Usage, from the repository root:

    uv run --no-sync python wiki/research/triangle_free_bipartization/evidence/produce.py \\
        --order 7 --interval 0.3 0.3125 [--eigen-rounds 25] [--game] [--products]

Runtime: a few minutes at order 7; at order 8 building the rows takes
about a minute, and each bisection step or eigenvector round several more.
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

sys.path.insert(0, str(Path(__file__).parent))

from util.envelopes import clebsch, petersen
from util.flaglp import FlagSystem, Program, coin_rules, cheapest_rule, same_side
from util.mixtures import circulant

START = time.time()


def log(message: str) -> None:
    """Print a message with the elapsed time."""
    print(f'[{time.time() - START:7.1f}s] {message}', flush=True)


def library(system: FlagSystem, low: float, high: float) -> list[tuple[str, np.ndarray]]:
    """Return density vectors of the library graphons whose density lies in [low, high]."""
    graphs = {'C13(1,5)': circulant(13, {1, 5, 8, 12}), 'Clebsch': clebsch(), 'Petersen': petersen()}
    out = []
    for name, adjacency in graphs.items():
        x = system.density_vector(adjacency)
        if low <= x @ system.p_vector <= high:
            out.append((name, x))
    pentagon = np.zeros((6, 6), dtype=np.int64)
    for i in range(5):
        pentagon[i, (i + 1) % 5] = pentagon[(i + 1) % 5, i] = 1
    for share in (0.875, 0.8775):
        x = system.density_vector(pentagon, [share / 5] * 5 + [1 - share])
        if low <= x @ system.p_vector <= high:
            out.append((f'C5 with isolated part, share {share}', x))
    rng = np.random.default_rng(7)
    for name, adjacency in graphs.items():
        found = 0
        for _ in range(4000):
            w = np.exp(0.2 * rng.standard_normal(len(adjacency)))
            w /= w.sum()
            if low <= w @ adjacency @ w <= high:
                out.append((f'{name} reweighted {found}', system.density_vector(adjacency, list(w))))
                found += 1
                if found == 2:
                    break
    return out


def game(program: Program, t: float, low: float, high: float) -> None:
    """Maximize the least cut row over library mixtures by cutting planes."""
    system = program.system
    components = library(system, low, high)
    log(f'library: {[(n, round(float(x @ system.p_vector), 4)) for n, x in components]}')
    vectors = np.array([x for _, x in components])
    lam = np.ones(len(components)) / len(components)
    pool = []
    worst = np.inf
    for it in range(60):
        y = lam @ vectors
        worst = np.inf
        for family, ti, g in program.mults:
            table, mass = system.aggregate(family, ti, g, y)
            profiles = family['profiles'][ti]
            candidates = [cheapest_rule(table, profiles) + (None,)]
            if family['m'] >= 1:
                candidates += coin_rules(table, profiles)
            for cost, mask, q in candidates:
                s, n = system.row(family, ti, g, same_side(family['k'], profiles, mask, q))
                values = vectors @ (s - t * n)
                pool.append(values)
                worst = min(worst, float(lam @ values))
        rows = np.array(pool)
        m = len(components)
        res = linprog(np.r_[np.zeros(m), -1], A_ub=np.hstack([-rows, np.ones((len(rows), 1))]),
                      b_ub=np.zeros(len(rows)), A_eq=np.r_[np.ones(m), 0][None, :], b_eq=[1],
                      bounds=[(0, 1)] * m + [(None, None)], method='highs')
        log(f'game iteration {it}: least row at the mixture {worst:.4e}, cutting-plane bound {res.x[-1]:.4e}')
        if res.x[-1] - worst < 1e-11:
            break
        lam = res.x[:m]
    weights = {name: round(float(v), 4) for (name, _), v in zip(components, lam) if v > 1e-6}
    log(f'game value {worst:.4e} at weights {weights}')


def main() -> int:
    """Run the requested search."""
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--order', type=int, choices=(7, 8), default=7)
    parser.add_argument('--interval', type=float, nargs=2, default=(0.3, 0.3125))
    parser.add_argument('--start', type=float, default=2 / 25)
    parser.add_argument('--eigen-rounds', type=int, default=0)
    parser.add_argument('--bracket', type=float, nargs=2, default=(2 / 25, 0.11))
    parser.add_argument('--steps', type=int, default=10)
    parser.add_argument('--rounds', type=int, default=30)
    parser.add_argument('--game', action='store_true')
    parser.add_argument('--products', action='store_true',
                        help='add products of two cut rows on the same roots (order 7)')
    args = parser.parse_args()
    low, high = args.interval
    system = FlagSystem(args.order, low, high)
    program = Program(system)
    log(f'order {args.order}: {system.count} graphs, {len(system.fixed)} fixed rows, '
        f'{len(system.blocks)} square blocks, {len(program.mults)} multipliers')
    if args.game:
        game(program, args.start, low, high)
    def search(t: float, rounds: int) -> tuple[float, np.ndarray]:
        """Column generation, alternating with product rows when requested."""
        if args.products:
            # product rows depend on the threshold; keep only those built at t
            program.squares = [sq for sq in program.squares if sq[0][0] != 'product' or sq[0][4] == t]
        eps, y = program.generate(t, rounds)
        while args.products and eps <= 1e-7 and program.products(y, t):
            eps, y = program.generate(t, rounds)
        return eps, y

    eps, y = search(args.start, args.rounds)
    positive_thresholds = [args.start] if eps > 1e-7 else []
    log(f'eps at t = {args.start:.5f}: {eps:.4e}; dual density {y @ system.p_vector:.4f}')
    for r in range(args.eigen_rounds):
        least = program.eigen_squares(y, r)
        eps, y = search(args.start, 15)
        log(f'eigenvector round {r}: least eigenvalue before {least:.3e}; eps {eps:.4e}; '
            f'{len(program.squares)} eigenvector squares')
        if eps > 1e-7:
            positive_thresholds.append(args.start)
            break
    lo, hi = args.bracket
    for _ in range(args.steps):
        mid = (lo + hi) / 2
        eps_mid, _ = search(mid, args.rounds)
        if eps_mid > 1e-7:
            hi = mid
            positive_thresholds.append(mid)
        else:
            lo = mid
        log(f'bisection t = {mid:.5f}: eps {eps_mid:.3e}; bracket [{lo:.5f}, {hi:.5f}]')
    log(f'search bracket [{lo:.5f}, {hi:.5f}]; incomplete pricing does not prove an optimum')
    if positive_thresholds:
        log(f'least tested threshold with positive numerical margin: {min(positive_thresholds):.5f}; '
            'exact certificate recovery is required')
    else:
        log('no tested threshold returned a positive numerical margin')
    return 0


if __name__ == '__main__':
    sys.exit(main())

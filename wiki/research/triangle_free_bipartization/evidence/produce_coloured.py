r"""Bound the monochromatic density of maximum-cut-coloured band graphons at order six.

This is a discovery program, not evidence. util/colouredflags.py builds the
order-six relaxation whose state is a triangle-free graphon coloured by a
maximum cut: vertex-stability rows, switching rows on one to four roots,
band rows and flag moment blocks. This program maximizes the monochromatic
edge density over that relaxation on a density interval by a log-barrier
method, alternating with exact pricing of switching rows (local search on
four roots). After each solve it prints the objective of a possibly relaxed
iterate, whose checks cover only rows priced so far, and optionally a
floating-point dual bound from util/colouredflags.py. The iterate need not
be feasible without its positive relaxation, and neither number certifies
the complete system. A dual bound below 2/25 would still have to be recovered as
an exact rational certificate. Nothing printed here is a proof or an
obstruction. --dual prints the bound after every round; --save writes the
last state and the added rows to an .npz, and --bound PATH prints the
objective and dual bound of such a saved state.

With --validate it first computes the exact states of the Petersen graph and
the circulant C13(1,5), each coloured by a maximum cut, and checks that they
satisfy every row and block, and that a one-colour cut of the Petersen graph
violates them; it exits nonzero otherwise.

With --traps it instead scans every cut of C5, C7, the Petersen graph, the
Clebsch graph and C13(1,5) for vertex-stable cuts above N^2/25 without an
improving two-root switching, then runs single-vertex and two-root
switching descent on seeded random triangle-free Cayley graphs of band
density on F_2^6, F_2^7 and cyclic groups, from random cuts, and reports the
smallest and largest monochromatic counts reached against N^2/25.

Usage, from the repository root:

    uv run --no-sync python wiki/research/triangle_free_bipartization/evidence/produce_coloured.py \\
        --interval 0.3 0.3125 [--rounds 12] [--limit 200] [--t4] [--products] \\
        [--validate] [--save PATH] [--traps]

Runtime: seconds to build; each round one to three minutes, about five with
--t4 --products, including about a minute for the dual bound's linear
program; --traps takes seconds.
"""

from __future__ import annotations

import argparse
import itertools
import sys
import time
from collections.abc import Callable
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from util.colouredflags import System

START = time.time()


def log(message: str) -> None:
    """Print a message with the elapsed time."""
    print(f'[{time.time() - START:7.1f}s] {message}', flush=True)


def graph(n: int, edge: Callable[[int, int], bool]) -> np.ndarray:
    """Adjacency matrix of a graph on range(n)."""
    return np.array([[int(i != j and edge(i, j)) for j in range(n)] for i in range(n)], dtype=np.int64)


def mono(adj: np.ndarray, x: np.ndarray) -> int:
    """Number of monochromatic edges of a cut."""
    return int((adj * (x[:, None] == x[None, :])).sum() // 2)


def best_cut(adj: np.ndarray) -> np.ndarray:
    """A maximum cut by scanning every cut."""
    n = len(adj)
    masks = np.arange(1 << (n - 1))
    X = (masks[:, None] >> np.arange(n)[None, :]) & 1
    cost = np.zeros(len(masks), dtype=np.int64)
    for i, j in itertools.combinations(range(n), 2):
        if adj[i, j]:
            cost += X[:, i] == X[:, j]
    return X[int(cost.argmin())]


def validate(system: System) -> bool:
    """Genuine maximum-cut states satisfy every row; a bad cut violates some."""
    pairs5 = list(itertools.combinations(range(5), 2))
    graphs = {
        'Petersen': graph(10, lambda i, j: not set(pairs5[i]) & set(pairs5[j])),
        'C13(1,5)': graph(13, lambda i, j: (i - j) % 13 in (1, 5, 8, 12)),
    }
    R = np.array(system.rows)
    ok = True
    cases = [(name, adj, best_cut(adj), True) for name, adj in graphs.items()]
    cases.append(('Petersen one colour', graphs['Petersen'], np.zeros(10, dtype=np.int64), False))
    for name, adj, x, optimal in cases:
        y = system.state(adj, x)
        n = len(x)
        least_row = float((R @ y).min())
        least_switch = min((fam.price(y, 1, tol=1e-12) or [(0.0,)])[0][0] for fam in system.switching.values())
        least_block = min(float(np.linalg.eigvalsh(np.tensordot(y[g], F, axes=1)).min())
                          for g, F in system.blocks)
        exact = 2 * mono(adj, x) / n ** 2
        log(f'{name}: density {adj.sum() / n ** 2:.4f}, objective {system.objective @ y:.6f} '
            f'(2M/N^2 = {exact:.6f}); least row {least_row:.2e}, least switching row '
            f'{least_switch:.2e}, least block eigenvalue {least_block:.2e}')
        satisfied = least_row > -1e-12 and least_switch > -1e-12 and least_block > -1e-9
        ok &= bool(abs(system.objective @ y - exact) < 1e-12)
        ok &= bool(satisfied) if optimal else not satisfied
    return ok


MASKS = ((np.arange(128)[:, None] >> np.arange(8)[None, :]) & 1).astype(np.int64)


def best_switch(adj: np.ndarray, x: np.ndarray) -> tuple[int, tuple[int, int, int] | None]:
    """Most improving two-root switch: change in monochromatic count and move."""
    n = len(x)
    signed = adj * (1 - 2 * (x[:, None] == x[None, :]).astype(np.int64))
    best = (0, None)
    for r1 in range(n):
        base = x + 2 * adj[:, r1]
        W = np.zeros((n, 8, 8), dtype=np.int64)
        for b in range(4):
            U = np.flatnonzero(base == b)
            for bb in range(4):
                V = np.flatnonzero(base == bb)
                if len(U) == 0 or len(V) == 0:
                    continue
                E = signed[np.ix_(U, V)]
                EA = E @ adj[V]
                d11 = (adj[U] * EA).sum(axis=0)
                d10 = adj[U].T @ E.sum(axis=1)
                d01 = EA.sum(axis=0)
                W[:, b + 4, bb + 4] = d11
                W[:, b + 4, bb] = d10 - d11
                W[:, b, bb + 4] = d01 - d11
                W[:, b, bb] = E.sum() - d10 - d01 + d11
        D = np.einsum('sc,rcd,sd->rs', MASKS, W, 1 - MASKS)
        k = np.unravel_index(D.argmin(), D.shape)
        if D[k] < best[0]:
            best = (int(D[k]), (r1, int(k[0]), int(k[1])))
    return best


def descend(adj: np.ndarray, x: np.ndarray) -> np.ndarray:
    """Single-vertex flips, then two-root switches, until neither improves."""
    x = x.copy()
    while True:
        sigma = (adj * (1 - 2 * (x[:, None] == x[None, :]).astype(np.int64))).sum(axis=1)
        v = int(sigma.argmin())
        if sigma[v] < 0:
            x[v] ^= 1
            continue
        _, move = best_switch(adj, x)
        if move is None:
            return x
        r1, r2, s = move
        flip = MASKS[s][x + 2 * adj[:, r1] + 4 * adj[:, r2]].astype(bool)
        x = np.where(flip, 1 - x, x)


def templates() -> None:
    """Every vertex-stable cut above N^2/25 of five small graphs has an improving switch."""
    pairs5 = list(itertools.combinations(range(5), 2))
    even = [i for i in range(32) if i.bit_count() % 2 == 0]
    for name, adj in {
        'C5': graph(5, lambda i, j: (i - j) % 5 in (1, 4)),
        'C7': graph(7, lambda i, j: (i - j) % 7 in (1, 6)),
        'Petersen': graph(10, lambda i, j: not set(pairs5[i]) & set(pairs5[j])),
        'Clebsch': graph(16, lambda i, j: (even[i] ^ even[j]).bit_count() == 4),
        'C13(1,5)': graph(13, lambda i, j: (i - j) % 13 in (1, 5, 8, 12)),
    }.items():
        n = len(adj)
        X = (np.arange(1 << (n - 1))[:, None] >> np.arange(n)[None, :]) & 1
        cost = np.zeros(len(X), dtype=np.int64)
        for i, j in itertools.combinations(range(n), 2):
            if adj[i, j]:
                cost += X[:, i] == X[:, j]
        same = X[:, :, None] == X[:, None, :]
        sigma = (adj[None] * np.where(same, -1, 1)).sum(axis=2)
        bad = np.flatnonzero((25 * cost > n * n) & (sigma.min(axis=1) >= 0))
        stuck = sum(best_switch(adj, X[c])[1] is None for c in bad)
        log(f'{name}: {len(X)} cuts up to complement, {int((25 * cost > n * n).sum())} above N^2/25, '
            f'{len(bad)} of them vertex-stable, {stuck} without an improving two-root switch')


def traps(seed: int) -> None:
    """Two-root switching descent on random band Cayley graphs."""
    templates()
    rng = np.random.default_rng(seed)
    low, high = 1243 / 5000, 3197 / 10000

    def cayley(n: int, add: Callable[[int, int], int], S: list[int]) -> np.ndarray:
        return np.array([[int(any(add(a, s) == b for s in S)) for b in range(n)] for a in range(n)],
                        dtype=np.int64)

    def sumfree_f2(n: int) -> list[int]:
        S = []
        for g in rng.permutation(np.arange(1, 1 << n)).tolist():
            if all((g ^ s) not in S for s in S):
                S.append(g)
        return S

    def sumfree_cyclic(n: int) -> list[int]:
        S = set()
        for g in rng.permutation(np.arange(1, n // 2 + 1)).tolist():
            T = S | {g, (-g) % n}
            if all((a + b) % n not in T for a in T for b in T):
                S = T
        return sorted(S)

    groups = [(1 << d, lambda a, b: a ^ b, lambda d=d: sumfree_f2(d), 6 if d == 6 else 3) for d in (6, 7)]
    groups += [(n, lambda a, b, n=n: (a + b) % n, lambda n=n: sumfree_cyclic(n), 2) for n in (41, 53, 67, 79, 97)]
    for n, add, draw, wanted in groups:
        found = 0
        for _ in range(400):
            S = draw()
            if not low < len(S) / n < high:
                continue
            adj = cayley(n, add, S)
            if np.any((adj @ adj) * adj):
                raise RuntimeError('triangle')
            reached = [mono(adj, descend(adj, rng.integers(0, 2, n))) for _ in range(6 if n < 100 else 3)]
            log(f'order {n}, connection set {S}: density {len(S) / n:.4f}, descent minima '
                f'{min(reached)}..{max(reached)} against N^2/25 = {n * n / 25:.2f}')
            found += 1
            if found == wanted:
                break


def main() -> int:
    """Run the requested computation."""
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--interval', type=float, nargs=2, default=(0.3, 0.3125))
    parser.add_argument('--rounds', type=int, default=12)
    parser.add_argument('--penalty', type=float, default=1e4)
    parser.add_argument('--limit', type=int, default=200, help='rows added per family per round')
    parser.add_argument('--seconds', type=float, default=180,
                        help='positive barrier time limit per round, in seconds')
    parser.add_argument('--lp-seconds', type=float, default=120,
                        help='positive time limit for each optional dual LP, in seconds')
    parser.add_argument('--t4', action='store_true', help='add four-rooted moment blocks')
    parser.add_argument('--products', action='store_true',
                        help='add sigma times switching rows and sigma times sigma rows')
    parser.add_argument('--validate', action='store_true')
    parser.add_argument('--traps', action='store_true')
    parser.add_argument('--seed', type=int, default=23)
    parser.add_argument('--save', type=Path, default=None,
                        help='write the last state and the added rows to this .npz (for example under output/)')
    parser.add_argument('--dual', action='store_true', help='print a dual bound after every round')
    parser.add_argument('--bound', type=Path, default=None,
                        help='print the objective and dual bound of a state saved by --save, and stop')
    args = parser.parse_args()
    if (
        not np.isfinite([args.seconds, args.lp_seconds]).all()
        or args.seconds <= 0 or args.lp_seconds <= 0 or args.rounds <= 0 or args.limit <= 0
    ):
        parser.error('solver time limits, rounds and row limits must be positive')
    if args.traps:
        traps(args.seed)
        return 0
    if args.bound is not None:
        data = np.load(args.bound)
        system = System(float(data['low']), float(data['high']), bool(data['t4']), bool(data['products']))
        for key, f, packed in zip(data['keys'], data['flags'], data['sides']):
            fam = system.switching[str(key)]
            system.add(fam.row(int(f), np.unpackbits(packed)[:fam.cells].astype(np.int64)))
        y = data['y']
        bound = system.dual_bound(y, float(data['tau']), 1e10, np.array(system.rows),
                                  seconds=args.lp_seconds)
        log(f'saved state on [{float(data["low"])}, {float(data["high"])}] with {len(system.rows)} rows: '
            f'objective {system.objective @ y:.6f}, dual bound {bound:.6f}')
        return 0
    low, high = args.interval
    system = System(low, high, args.t4, args.products)
    log(f'interval [{low}, {high}]: {system.table.count} coloured graphs, {len(system.rows)} rows, '
        f'{len(system.blocks)} blocks')
    if args.validate and not validate(system):
        log('validation failed')
        return 1
    recipes: list[tuple[str, int, np.ndarray]] = []
    for r in range(args.rounds):
        y, tau, value, bound = system.solve(args.penalty, dual=args.dual,
                                            seconds=args.seconds, lp_seconds=args.lp_seconds)
        if args.save is not None:
            args.save.parent.mkdir(parents=True, exist_ok=True)
            np.savez(args.save, y=y, tau=tau, value=value, bound=bound, low=low, high=high,
                     t4=args.t4, products=args.products,
                     keys=np.array([k for k, _, _ in recipes]), flags=np.array([f for _, f, _ in recipes]),
                     sides=np.array([np.packbits(np.pad(s, (0, 32 - len(s)))) for _, _, s in recipes]).reshape(-1, 4))
        added = 0
        least = {}
        for k, fam in system.switching.items():
            found = fam.price(y, args.limit)
            least[k] = found[0][0] if found else 0.0
            for _, f, side in found:
                system.add(fam.row(f, side))
                recipes.append((k, f, np.asarray(side, dtype=np.uint8)))
                added += 1
        log(f'round {r}: value {value:.6f}, dual bound {bound:.6f}, tau {tau:.1e}, '
            f'rows {len(system.rows)}, added {added}, '
            + ', '.join(f'least {k} row {v:.1e}' for k, v in least.items()))
        if added == 0:
            log('no switching row violated at the last state; four-root pricing is a local search')
            break
    return 0


if __name__ == '__main__':
    sys.exit(main())

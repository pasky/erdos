"""Bounded discovery with all combinations from a saved per-type cut pool.

The input is floating output of produce_coupled.py. Its rows are discovery
ingredients, never cached evidence. All seven-root cut coefficients are
rebuilt in integers. A nonnegative multiplier pool with equal total weight
on every root type represents a distribution of complete rooted cut
algorithms. This finite formulation replaces explicit algorithm columns.

A numerical bound at 2/25 is only a candidate: every other saved row,
positivity factor, multiplier and coefficient still needs exact recovery.
No mathematical obstruction follows from a larger bound or a solver limit.
The program writes only when --save names a directory.
"""
from __future__ import annotations

import argparse
import json
import math
import warnings
from pathlib import Path
from types import SimpleNamespace

import numpy as np
from produce_coupled import projections
from produce_recursive import log
from scipy import sparse
from scipy.optimize import OptimizeWarning, linprog
from util.lifted_flags import Nine
from util.paired_flags import Table


def main() -> None:
    """Rebuild the finite cut pool and solve its balanced-multiplier relaxation."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seed', type=Path, required=True)
    parser.add_argument('--seconds', type=float, default=120)
    parser.add_argument('--save', type=Path)
    args = parser.parse_args()
    if not np.isfinite(args.seconds) or args.seconds <= 0:
        parser.error('A finite positive solver time is required')
    metadata = json.loads((args.seed / 'recipes.json').read_text())
    R = sparse.load_npz(args.seed / 'uncoloured_rows.npz')
    S = sparse.load_npz(args.seed / 'coloured_rows.npz')
    nine = Nine(log)
    tb = Table(5)
    objective_row = tb.row(tb.adj(0, 1) * tb.same(0, 1))
    if (
        metadata['interval'] != ['1243/5000', '3197/10000']
        or R.shape[1] != nine.count or S.shape[1] != tb.count
    ):
        raise ValueError('Seed does not match the declared nine/five-point universe')
    project, forget = projections(nine, SimpleNamespace(tb=tb))
    project, forget = project[:-1], forget[:-1]
    by_code = {code: t for t, code in enumerate(nine.root_codes)}
    rules = {t: set() for t in range(len(by_code))}

    def retain(code: int, side: list[int]) -> None:
        """Keep a binary rule of the stated canonical root type."""
        if code not in by_code or len(side) != 128 or any(v not in (0, 1) for v in side):
            raise ValueError('Invalid saved seven-root cut rule')
        rules[by_code[code]].add(tuple(side))

    for recipe, _scale in metadata['uncoloured']:
        if recipe[0] == 'seven_root_cut':
            retain(recipe[1], recipe[2])
    for recipe in metadata.get('cross', []):
        if recipe[0] != 'global_seven_cut':
            raise ValueError('Unknown global-cut recipe')
        for code, side in recipe[1]:
            retain(code, side)
    rows, owners, recipes = [], [], []
    for t, d in enumerate(nine.cut_records):
        if not rules[t]:
            rules[t].add((0,) * 128)
        for saved in sorted(rules[t]):
            side = np.asarray(saved, np.int8)
            numerator = np.zeros(nine.count, np.int64)
            np.add.at(
                numerator, d['h'], nine.root_multiplicity[t] * d['count']
                * d['e'] * (side[d['x']] == side[d['y']]),
            )
            rows.append(numerator / math.factorial(9))
            owners.append(t)
            recipes.append((d['code'], list(saved), nine.root_multiplicity[t]))
    D = np.asarray(rows)
    owners = np.asarray(owners, np.int16)
    # Minimizing independently in each type checks every mixture of these
    # pool rules on the genuine C5 state, in exact integer arithmetic.
    control_total = 0
    for t, d in enumerate(nine.cut_records):
        costs = []
        for saved in rules[t]:
            side = np.asarray(saved, np.int8)
            value = (nine.root_multiplicity[t] * d['count'] * d['e']
                     * (side[d['x']] == side[d['y']]))
            costs.append(int(value @ nine.control_counts[d['h']]))
        control_total += min(costs)
    if 25 * control_total < 2 * math.factorial(9) * 5**9:
        raise RuntimeError('Integer type-pool C5 control failed')
    log(f'Balanced envelope: {len(D)} integer-rebuilt rules, {len(rules)} types; C5 control passes')
    m, n, k = R.shape[0], S.shape[0], len(D)
    count = m + n + k + 1
    main = sparse.block_diag((R.T, S.T), format='csc')
    pool = sparse.vstack((sparse.csr_matrix(D.T), sparse.csr_matrix((tb.count, k))), format='csc')
    gamma = sparse.csc_matrix(np.r_[np.zeros(nine.count), -objective_row][:, None])
    identity = sparse.vstack((sparse.csr_matrix(project.T), sparse.csr_matrix(-forget.T)), format='csc')
    constant = sparse.csc_matrix(np.r_[-np.ones(nine.count), np.ones(tb.count)][:, None])
    bound = sparse.csc_matrix(np.r_[np.zeros(nine.count), -np.ones(tb.count)][:, None])
    matrix = sparse.hstack((main, pool, gamma, identity, constant, bound), format='csc')
    groups = sparse.coo_matrix((np.ones(k), (owners, np.arange(k))), shape=(len(rules), k)).tocsr()
    equality = sparse.hstack((
        sparse.csr_matrix((len(rules), m+n)), groups,
        sparse.csr_matrix(-np.ones((len(rules), 1))),
        sparse.csr_matrix((len(rules), identity.shape[1] + 2)),
    ), format='csc')
    objective = np.zeros(matrix.shape[1])
    objective[-1] = 1
    bounds = [(0, None)] * count + [(None, None)] * (identity.shape[1] + 1) + [(0, None)]
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore', category=OptimizeWarning, message='Unrecognized options detected')
        result = linprog(
            objective, A_ub=matrix, b_ub=np.r_[np.zeros(nine.count), -objective_row],
            A_eq=equality, b_eq=np.zeros(len(rules)), bounds=bounds, method='highs-ipm',
            options={'time_limit': args.seconds, 'threads': 1, 'parallel': False},
        )
    log(f'Balanced-envelope LP status {result.status}: {result.message}')
    if result.status != 0 or result.x is None:
        log('Bounded solve incomplete; no mathematical verdict')
        return
    weights = np.maximum(result.x[:count], 0)
    free = result.x[count:count + identity.shape[1]]
    alpha = weights[m+n:m+n+k].copy()
    total = float(weights[count-1])
    if total > 1e-12:
        for t in range(len(rules)):
            take = owners == t
            subtotal = alpha[take].sum()
            if subtotal <= 1e-15:
                raise RuntimeError('Cannot repair a missing type weight')
            alpha[take] *= total / subtotal
    else:
        alpha[:] = 0
        total = 0
    first = R.T @ weights[:m] + D.T @ alpha + project.T @ free
    second = objective_row + S.T @ weights[m:m+n] - total * objective_row - forget.T @ free
    upper = float(first.max() + second.max())
    balance = float(abs(groups @ alpha - total).max())
    log(f'Balanced-envelope floating bound {result.x[-1]:.12g}; recomputed {upper:.12g}; balance residual {balance:.3g}')
    if args.save is not None:
        args.save.mkdir(parents=True, exist_ok=True)
        np.savez(args.save / 'candidate.npz', weights=weights[:m+n], alpha=alpha,
                 gamma=total, free=free, first=first, second=second,
                 state=-np.asarray(result.ineqlin.marginals))
        sparse.save_npz(args.save / 'uncoloured_rows.npz', R)
        sparse.save_npz(args.save / 'coloured_rows.npz', S)
        (args.save / 'recipes.json').write_text(json.dumps({
            'standing': 'floating discovery only', 'interval': metadata['interval'],
            'uncoloured': metadata['uncoloured'], 'coloured': metadata['coloured'],
            'type_pool': recipes, 'hypothesis': metadata['hypothesis'],
        }))
    if upper <= 2/25 + 1e-9:
        log('Possible whole-band certificate; exact reconstruction and balance checks required')


if __name__ == '__main__':
    main()

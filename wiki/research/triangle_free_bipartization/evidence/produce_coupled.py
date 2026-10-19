"""Bounded discovery with a common uncoloured five-vertex marginal.

The nine-point recursive system and the paired-cut five-point system must
come from the same hypothetical least-support weighted counterexample.
Their uncoloured five-point marginals therefore agree. This program joins
those relaxations and uses B-free active-cut balance identities and the
necessary interval b<=B<=B0. No target bound is assumed on an unrestricted
induced subset. Proper-support rows retain their explicit exclusions.

The default objective bounds monochromatic density directly; a sum of
coefficient maxima at most 2/25 would suffice after exact reconstruction.
The alternative contradiction objective seeks a strictly negative sum.
All searches here are floating, incomplete and bounded. A solver limit or
unsuccessful numerical search gives no mathematical obstruction. No files are written
unless --save specifies a directory. Optional --seed-eight is floating
output from produce_recursive.py; --seed-coupled restores selected floating
ingredients of this program. Neither supplies a mathematical certificate.
"""
from __future__ import annotations

import argparse
import gc
import json
import warnings
from itertools import combinations, permutations
from pathlib import Path

import networkx as nx
import numpy as np
from produce_extremal import Rows, control_state, psd_rows, validate, validate_proper
from produce_lifted import build_lifted
from produce_recursive import log
from scipy import sparse
from scipy.optimize import OptimizeWarning, linprog
from util.extremal_model import (
    B0,
    System,
    affine_hereditary_blocks,
    aggregate,
    b,
    cut_pattern_blocks,
    cut_scaled_horn_rows,
    moment,
)
from util.lifted_flags import Nine, codes


def projections(nine: Nine, paired: System) -> tuple[np.ndarray, np.ndarray]:
    """Exact deletion and colour-forgetting maps to the fourteen five-point classes."""
    lookup = np.full(1024, -1, np.int16)
    perm = np.array(list(permutations(range(5))), np.int16)
    size = 0
    for graph in nx.graph_atlas_g():
        if len(graph) != 5 or sum(nx.triangles(graph).values()):
            continue
        a = nx.to_numpy_array(graph, dtype=np.int8)
        lookup[codes(a[perm[:, :, None], perm[:, None, :]])] = size
        size += 1
    positions = np.array(list(combinations(range(9), 5)), np.int16)
    counts = np.zeros((size, nine.count), np.int16)
    for h, a in enumerate(nine.graphs):
        flag = lookup[codes(a[positions[:, :, None], positions[:, None, :]])]
        if flag.min() < 0:
            raise RuntimeError('Missing five-point graph')
        counts[:, h] = np.bincount(flag, minlength=size)
    owners = lookup[np.asarray(paired.tb.reps, np.int64) & 1023]
    if np.any(owners < 0) or np.any(counts.sum(axis=0) != 126):
        raise RuntimeError('Projection coverage failed')
    forget = np.zeros((size, paired.tb.count))
    forget[owners, np.arange(paired.tb.count)] = 1
    return counts / 126, forget


def static_rows(system: System, boundary: np.ndarray) -> Rows:
    """Valid paired inequalities for b<=B<=B0, plus exact B-free balances."""
    rows = Rows(system.tb.count)
    least = 0.0
    for r, d, recipe in zip(system.rows, system.derivatives, system.recipes):
        label = recipe[0]
        if label in {'degree', 'balanced_other_cut', 'm_equals_B'}:
            r = r + (b - B0) * d
        if not label.startswith('band_'):
            least = min(least, float((r @ boundary)[0]))
        rows.add(r, None, ('interval_consequence', recipe))
    tb = system.tb
    first = (tb.adj(0, 3) * tb.same(0, 3)).astype(np.int16)
    independent = (tb.adj(3, 4) * tb.same(3, 4)).astype(np.int16)
    flag, names = tb.flag((0, 1, 2), 1, 'second')
    equalities = aggregate(tb, flag, len(names), first - independent)
    error = float(abs(equalities @ boundary).max())
    negative = control_state(tb, isolate=True)
    negative_error = float(abs(equalities @ negative).max())
    for i in range(equalities.shape[0]):
        rows.add(equalities.getrow(i), None, ('B_free_balance', i, 1))
        rows.add(-equalities.getrow(i), None, ('B_free_balance', i, -1))
    flag, names = tb.flag((0, 1, 2), 1)
    degrees = aggregate(tb, flag, len(names), tb.adj(0, 3) - 2 * independent)
    least = min(least, float((degrees @ boundary).min()))
    for i in range(degrees.shape[0]):
        rows.add(degrees.getrow(i), None, ('B_free_degree', i))
    rows.add((B0 - system.c)[None, :], None, ('global_source_cap',))
    # Isolated padding to density 1243/5000 gives B <= (400/1243)p
    # throughout the counterexample band. Multiply by flags on disjoint
    # slots; both B and p are independent of the sampled active cuts.
    flag, names = tb.flag((0, 1, 2), 1)
    padding = aggregate(
        tb, flag, len(names), (400 / 1243) * tb.adj(3, 4) - independent
    )
    least = min(least, float((padding @ boundary).min()))
    for i in range(padding.shape[0]):
        rows.add(padding.getrow(i), None, ('isolated_padding', i, '400/1243'))
    log(f'Coupled B-free controls: least row {least}, balance error {error}, isolate error {negative_error}')
    if least < -1e-10 or error > 1e-12 or negative_error < 1e-7:
        raise RuntimeError('B-free identity controls failed')
    return rows


def prune_coloured(
    rows: Rows, weights: np.ndarray, state: np.ndarray, base: int, capacity: int
) -> Rows:
    """Keep base rows, used columns and a bounded pool of the least-slack rows."""
    if len(rows.r) < base + capacity + 350:
        return rows
    values = np.asarray(rows.matrices()[0] @ state)
    keep = weights > 1e-9
    keep[:base] = True
    keep[np.argsort(values[base:])[:capacity] + base] = True
    retained = Rows(rows.K)
    for row, (recipe, scale), use in zip(rows.r, rows.rec, keep):
        if use:
            retained.add(row * scale, None, tuple(recipe))
    log(f'Coupled coloured pruning retained {len(retained.r)} rows')
    return retained


def parameter_free_blocks(system: System, boundary: np.ndarray) -> None:
    """Localize degree and scalar parameter bounds without replacing B by b."""
    tb = system.tb
    independent = (tb.adj(3, 4) * tb.same(3, 4)).astype(np.int16)
    multipliers = (
        tb.adj(0, 3) - 2 * independent,
        independent - b,
        B0 - independent,
        (400 / 1243) * tb.adj(3, 4) - independent,
    )
    added = []
    for multiplier in multipliers:
        added.extend(moment(tb, 1, (0, 1), (0, 2), multiplier))
    # Uniform source-bound hereditary square blocks have B=B0 here.
    added.extend((M, n) for M, _D, n, _mask in affine_hereditary_blocks(system))
    least = 0.0
    for M, n in added:
        i, j = np.triu_indices(n)
        matrix = np.zeros((n, n))
        matrix[i, j] = (M @ boundary) / np.where(i == j, 1, np.sqrt(2))
        matrix[j, i] = matrix[i, j]
        least = min(least, float(np.linalg.eigvalsh(matrix).min()))
    log(f'Parameter-free and source hereditary square controls: {len(added)} blocks, least {least}')
    if least < -1e-9:
        raise RuntimeError('Additional localized square controls failed')
    system.blocks.extend(added)


def main() -> None:
    """Build, validate and search the common-marginal coefficient criteria."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seed-eight', type=Path)
    parser.add_argument('--seed-coupled', type=Path)
    parser.add_argument('--seed-all', action='store_true')
    parser.add_argument('--mode', choices=('bound', 'contradiction'), default='bound')
    parser.add_argument('--method', choices=('highs-ds', 'highs-ipm'), default='highs-ipm')
    parser.add_argument('--coloured-pool', type=int, default=350)
    parser.add_argument('--save', type=Path)
    parser.add_argument('--rounds', type=int, default=20)
    parser.add_argument('--seconds', type=float, default=60)
    parser.add_argument('--validate-only', action='store_true')
    parser.add_argument('--localized-squares', action='store_true')
    parser.add_argument('--pentagon-recursion', action='store_true')
    parser.add_argument('--global-cuts', action='store_true')
    args = parser.parse_args()
    if args.rounds <= 0 or args.coloured_pool <= 0 or not np.isfinite(args.seconds) or args.seconds <= 0:
        parser.error('Finite positive rounds and time limits required')
    nine, eight, lifted = build_lifted(args.seed_eight, True, args.localized_squares)
    paired = System(5)
    patterns = cut_pattern_blocks(paired)
    paired.blocks.extend((M, n) for M, n, _x, _q in patterns)
    boundary = validate(paired)
    validate_proper(paired, boundary)
    parameter_free_blocks(paired, boundary)
    coloured = static_rows(paired, boundary)
    base = len(coloured.r)
    project, forget = projections(nine, paired)
    if np.max(abs(project @ nine.control - forget @ boundary)) > 1e-12:
        raise RuntimeError('Common-marginal C5 control failed')
    log('Fourteen-class common-marginal C5 control passed')
    if args.validate_only:
        log('All coupled generation controls pass; no bound certified')
        return
    # The final marginal identity follows from equal total mass. Omitting it
    # removes a redundant free column; the two constant coefficient bounds
    # below enforce both probability normalizations in the dual.
    project, forget = project[:-1], forget[:-1]
    y, z = np.ones(nine.count) / nine.count, boundary
    cross_rows, cross_recipes, cross_seen = [], [], set()
    if args.seed_coupled is not None:
        source = args.seed_coupled
        metadata = json.loads((source / 'recipes.json').read_text())
        seed = np.load(source / 'candidate.npz')
        R = sparse.load_npz(source / 'uncoloured_rows.npz')
        S = sparse.load_npz(source / 'coloured_rows.npz')
        if (
            metadata['interval'] != ['1243/5000', '3197/10000']
            or R.shape[1] != nine.count or S.shape[1] != paired.tb.count
            or len(seed['weights']) != R.shape[0] + S.shape[0] + len(metadata.get('cross', []))
        ):
            raise ValueError('Coupled seed does not match the declared universe')
        for i, (recipe, scale) in enumerate(metadata['uncoloured']):
            if args.seed_all or seed['weights'][i] > 1e-10:
                lifted.add(R.getrow(i).toarray().ravel() * scale, tuple(recipe))
        for i, (recipe, scale) in enumerate(metadata['coloured']):
            if args.seed_all or seed['weights'][R.shape[0] + i] > 1e-10:
                coloured.add(S.getrow(i) * scale, None, tuple(recipe))
        if metadata.get('cross'):
            saved_cross = np.load(source / 'global_cuts.npz')['rows']
            for i, recipe in enumerate(metadata['cross']):
                if args.seed_all or seed['weights'][R.shape[0] + S.shape[0] + i] > 1e-10:
                    cross_rows.append(saved_cross[i])
                    cross_recipes.append(recipe)
                    cross_seen.add(np.round(saved_cross[i], 11).tobytes())
        state = np.maximum(seed['state'], 0)
        y, z = state[:nine.count], state[nine.count:]
        y, z = y / y.sum(), z / z.sum()
        del R, S, seed, metadata
        gc.collect()
        log('Restored floating coupled ingredients; no verdict accepted')
    for iteration in range(args.rounds):
        old = nine.projection @ y
        for family, ti, g in eight.mults:
            eight.price(family, ti, g, old)
        eight.localizers(old)
        eight.full_localizers(old)
        eight.products(old)
        lifted.lift(eight)
        lifted.price_seven(y, 1000 * iteration + 61)
        if args.global_cuts:
            cost = lifted.last_cut_cost
            log(f'Global cut comparison: algorithm {cost @ y:.12g}, paired optimum {paired.c @ z:.12g}')
            key = np.round(cost, 11).tobytes()
            if key not in cross_seen:
                cross_seen.add(key)
                cross_rows.append(cost.copy())
                cross_recipes.append(lifted.last_cut_recipe)
        if args.pentagon_recursion:
            lifted.price_pentagon(y)
        lifted.price_squares(y)
        for _value, row, recipe in psd_rows(paired.blocks, z):
            coloured.add(row[None, :], None, recipe)
        for _value, row, recipe in cut_scaled_horn_rows(patterns, z):
            coloured.add(row[None, :], None, recipe)
        for family in paired.families:
            for row, _der, recipe in family.price(z, limit=30):
                coloured.add(row[None, :], None, ('uniform_B0', recipe))
            for row, _der, recipe in family.switches(z, limit=30):
                coloured.add(row[None, :], None, recipe)
            for row, _der, recipe in family.recursive(z, limit=30):
                coloured.add(row[None, :], None, ('uniform_B0', recipe))
            for anchor in range(family.k):
                for mode in ('root', 'cross0', 'cross1'):
                    for row, _der, recipe in family.price(z, limit=12, proper_anchor=anchor, proper_mode=mode):
                        coloured.add(row[None, :], None, recipe)
                    for row, _der, recipe in family.recursive(z, limit=12, proper_anchor=anchor, proper_mode=mode):
                        coloured.add(row[None, :], None, recipe)
        R = sparse.csr_matrix(np.array(lifted.rows))
        S, _D = coloured.matrices()
        m, n = R.shape[0], S.shape[0]
        main = sparse.block_diag((R.T, S.T), format='csc')
        C = np.asarray(cross_rows).reshape(len(cross_rows), nine.count)
        if len(C):
            cross = sparse.vstack((
                sparse.csr_matrix(C.T),
                sparse.csr_matrix(-np.tile(paired.c[:, None], (1, len(C)))),
            ), format='csc')
            main = sparse.hstack((main, cross), format='csc')
        count = m + n + len(C)
        identity = sparse.vstack((sparse.csr_matrix(project.T), sparse.csr_matrix(-forget.T)), format='csc')
        constant = sparse.csc_matrix(np.r_[-np.ones(nine.count), np.ones(paired.tb.count)][:, None])
        bound_mode = args.mode == 'bound'
        sign = -1 if bound_mode else 1
        epsilon = sparse.csc_matrix(np.r_[np.zeros(nine.count), sign * np.ones(paired.tb.count)][:, None])
        matrix = sparse.hstack((main, identity, constant, epsilon), format='csc')
        objective = np.zeros(matrix.shape[1])
        objective[-1] = 1 if bound_mode else -1
        normal = np.r_[np.ones(count), np.zeros(identity.shape[1] + 2)][None, :]
        rhs = np.r_[np.zeros(nine.count), -paired.c] if bound_mode else np.zeros(matrix.shape[0])
        variable_bounds = [(0, None)] * count + [(None, None)] * (identity.shape[1] + 2)
        if bound_mode:
            # A negative bound would also imply the bound zero. This floor
            # loses no target certificate and avoids an unbounded objective
            # if the hypothetical-counterexample system is inconsistent.
            variable_bounds[-1] = (0, None)
        log(f'Coupled round {iteration}: {m} uncoloured, {n} coloured rows, matrix {matrix.shape}')
        with warnings.catch_warnings():
            warnings.filterwarnings('ignore', category=OptimizeWarning, message='Unrecognized options detected')
            result = linprog(
                objective, A_ub=matrix, b_ub=rhs,
                A_eq=None if bound_mode else normal, b_eq=None if bound_mode else [1],
                bounds=variable_bounds,
                method=args.method, options={'time_limit': args.seconds, 'threads': 1, 'parallel': False},
            )
        log(f'Coupled LP status {result.status}: {result.message}')
        if result.status != 0 or result.x is None:
            log('Bounded coupled solve incomplete; no mathematical verdict')
            break
        weights = np.maximum(result.x[:count], 0)
        free = result.x[count:count + identity.shape[1]]
        first = R.T @ weights[:m] + project.T @ free + C.T @ weights[m+n:]
        second = S.T @ weights[m:m+n] - forget.T @ free + (paired.c if bound_mode else 0)
        second -= paired.c * weights[m+n:].sum()
        gap = float(first.max() + second.max())
        log(f'Coupled floating {args.mode} objective {result.x[-1]:.12g}; sum of coefficient maxima {gap:.12g}')
        if args.save is not None:
            args.save.mkdir(parents=True, exist_ok=True)
            np.savez(args.save / 'candidate.npz', weights=weights, free=free,
                     first=first, second=second, state=-np.asarray(result.ineqlin.marginals))
            sparse.save_npz(args.save / 'uncoloured_rows.npz', R)
            sparse.save_npz(args.save / 'coloured_rows.npz', S)
            np.savez(args.save / 'global_cuts.npz', rows=C)
            (args.save / 'recipes.json').write_text(json.dumps({
                'standing': 'floating discovery only', 'interval': ['1243/5000', '3197/10000'],
                'uncoloured': lifted.recipes, 'coloured': coloured.rec,
                'hypothesis': 'least-support weighted counterexample, balanced independent active cuts',
                'mode': args.mode,
                'cross': cross_recipes,
            }))
        if (bound_mode and gap <= b + 1e-9) or (not bound_mode and gap < -1e-8 and result.x[-1] > 1e-7):
            log('Possible whole-band coupled certificate; exact reconstruction required')
            break
        state = np.maximum(-np.asarray(result.ineqlin.marginals), 0)
        y, z = state[:nine.count], state[nine.count:]
        if min(y.sum(), z.sum()) <= 1e-12:
            break
        y, z = y / y.sum(), z / z.sum()
        log(f'Coupled states: p={nine.p @ y:.12g}, m={paired.c @ z:.12g}, marginal error={abs(project @ y - forget @ z).max():.3g}')
        lifted.prune(weights[:m], y)
        coloured = prune_coloured(coloured, weights[m:m+n], z, base, args.coloured_pool)
        del matrix, main, identity, constant, epsilon, result, R, S, _D
        gc.collect()


if __name__ == '__main__':
    main()

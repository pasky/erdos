"""Bounded whole-band discovery at order nine by deletion lifting.

Lift valid order-eight recursive-induction rows, add seven-root cut rows
and new full flag-square bases, and seek a strictly negative combination.
The underlying hypothesis is the canonical sketch's weighted counterexample,
including its minimum-degree and recursive-induction consequences. A
positive numerical margin would still require exact row reconstruction,
nonnegative multipliers, positive semidefinite factors and every coefficient
check; this program awards no mathematical standing.

No full nine-point labeled graph table is stored. Independent-neighborhood
extensions exhaust the unlabeled universe, exact isomorphism removes duplicates,
and integer embedding counts define the seven-root rows. Every solve and
round count has a finite limit. Pricing is incomplete, and a negative margin,
time limit or locally stationary state is not a mathematical obstruction.

Optional --seed-eight consumes floating discovery output of
produce_recursive.py --order 8 --parts 3 --products --full-localizers.
Those rows are additional discovery ingredients, never cached evidence.
The program also works without a seed. --save is the only output writer.
"""
from __future__ import annotations

import argparse
import gc
import json
import math
import warnings
from itertools import combinations
from pathlib import Path

import numpy as np
from produce_recursive import Search, log
from scipy.optimize import OptimizeWarning, linprog
from util.flaglp import FlagSystem, cheapest_rule, independent_sets, pairs_of
from util.lifted_flags import Nine, flag_block, localizer_blocks


class Lifted:
    """Normalized nine-point rows and bounded separation procedures."""

    def __init__(self, nine: Nine, blocks: list) -> None:
        """Initialize an empty numerical row collection."""
        self.nine = nine
        self.blocks = blocks
        self.rows = []
        self.recipes = []
        self.cut = []
        self.seen = set()
        self.ternary_cache = {}

    def add(self, row: np.ndarray, recipe: tuple, cut: bool = False) -> bool:
        """Keep a distinct row with its normalization and reconstruction recipe."""
        scale = float(abs(row).max())
        if scale < 1e-13:
            return False
        row = row / scale
        key = np.round(row, 11).tobytes()
        if key in self.seen:
            return False
        self.seen.add(key)
        self.rows.append(row)
        self.recipes.append((recipe, scale))
        self.cut.append(cut)
        return True

    def lift(self, search: Search) -> int:
        """Lift and then release newly generated order-eight discovery rows."""
        added = 0
        for row, recipe, cut in zip(search.rows, search.labels, search.is_cut):
            added += self.add(row @ self.nine.projection, ('lift_eight', recipe), cut)
        search.rows = []
        search.labels = []
        search.is_cut = []
        search.seen.clear()
        return added

    def price_seven(self, y: np.ndarray, seed: int) -> int:
        """Search binary seven-root rules and rebuild each proposed row in integers."""
        added = 0
        cost_numerator = np.zeros(self.nine.count, np.int64)
        global_rules = []
        for t, d in enumerate(self.nine.cut_records):
            w = d['count'] * y[d['h']] / math.factorial(9)
            table = np.bincount(d['x'] * 128 + d['y'], weights=w * d['e'], minlength=128**2).reshape(128, 128)
            profiles = independent_sets(d['code'], 7)
            value, mask = cheapest_rule(table, profiles, limit=13, seed=seed + t)
            side = np.zeros(128, np.int8)
            side[profiles] = [(mask >> i) & 1 for i in range(len(profiles))]
            same = side[d['x']] == side[d['y']]
            np.add.at(
                cost_numerator, d['h'],
                self.nine.root_multiplicity[t] * d['count'] * d['e'] * same,
            )
            global_rules.append((d['code'], side.tolist()))
            if value - 2 / 25 * w.sum() >= -1e-11:
                continue
            numerator = np.zeros(self.nine.count, np.int64)
            np.add.at(numerator, d['h'], d['count'] * (25 * d['e'] * same - 2))
            if int(numerator @ self.nine.control_counts) < 0:
                raise RuntimeError('Integer seven-root C5 control failed')
            row = numerator / (25 * math.factorial(9))
            if abs(row @ y - (value - 2 / 25 * w.sum())) > 1e-10:
                raise RuntimeError('Seven-root pricing and rebuilt row disagree')
            added += self.add(row, ('seven_root_cut', d['code'], side.tolist()), True)
        if 25 * int(cost_numerator @ self.nine.control_counts) < 2 * math.factorial(9) * 5**9:
            raise RuntimeError('Global rooted-cut integer C5 control failed')
        self.last_cut_cost = cost_numerator / math.factorial(9)
        self.last_cut_recipe = ('global_seven_cut', global_rules, math.factorial(9))
        return added

    def price_squares(self, y: np.ndarray) -> int:
        """Add every negative eigenvector direction in each declared basis."""
        added = 0
        for block, (M, n, recipe) in enumerate(self.blocks):
            i, j = np.triu_indices(n)
            factor = np.where(i == j, 1, np.sqrt(2))
            matrix = np.zeros((n, n))
            matrix[i, j] = (M @ y) / factor
            matrix[j, i] = matrix[i, j]
            eig, vectors = np.linalg.eigh(matrix)
            for h in np.flatnonzero(eig < -1e-10):
                v = vectors[:, h]
                row = (v[i] * v[j] * factor) @ M
                added += self.add(
                    row, ('square_nine', block, recipe, v.tolist()),
                    recipe[0] == 'recursive_localizer_nine',
                )
        return added

    def price_pentagon(self, y: np.ndarray) -> int:
        """Enumerate all three-label pentagon-profile rules with seven-root multipliers."""
        added, least = 0, 0.0
        tested = 0
        for d in self.nine.cut_records:
            adjacency = np.zeros((7, 7), np.int8)
            for bit, (i, j) in enumerate(pairs_of(7)):
                adjacency[i, j] = adjacency[j, i] = (d['code'] >> bit) & 1
            for subset in combinations(range(7), 5):
                a = adjacency[np.ix_(subset, subset)]
                if np.any(a.sum(axis=1) != 2):
                    continue
                code = sum(int(a[i, j]) << bit for bit, (i, j) in enumerate(pairs_of(5)))
                profiles = independent_sets(code, 5)
                m = len(profiles)
                if m != 11:
                    raise RuntimeError('An induced pentagon must have eleven independent profiles')
                if m not in self.ternary_cache:
                    labels = np.indices((3,) * m, dtype=np.int8).reshape(m, -1).T.copy()
                    self.ternary_cache[m] = (labels, labels.astype(float) - 1, (labels == 1).astype(float))
                labels, z, u = self.ternary_cache[m]
                x = sum(((d['x'] >> old) & 1) << new for new, old in enumerate(subset))
                yy = sum(((d['y'] >> old) & 1) << new for new, old in enumerate(subset))
                lookup = np.full(32, -1, np.int8)
                lookup[profiles] = np.arange(m)
                px, py = lookup[x], lookup[yy]
                if min(px.min(), py.min()) < 0:
                    raise RuntimeError('A pentagon endpoint profile is not independent')
                weight = d['count'] * y[d['h']] / math.factorial(9)
                mass = np.bincount(px.astype(np.int64) * m + py, weights=weight, minlength=m*m).reshape(m, m)
                edge = np.bincount(px.astype(np.int64) * m + py, weights=weight * d['e'], minlength=m*m).reshape(m, m)
                mass, edge = (mass + mass.T) / 2, (edge + edge.T) / 2
                qz, qu = 0.5 * edge, (2 / 25) * mass - 0.5 * edge
                values = (
                    0.5 * edge.sum() - (2 / 25) * mass.sum()
                    + np.sum((z @ qz) * z, axis=1)
                    + np.sum((u @ qu) * u, axis=1)
                )
                choice = int(values.argmin())
                least = min(least, float(values[choice]))
                tested += 1
                if values[choice] >= -1e-11:
                    continue
                rule = labels[choice]
                zx, zy = rule[px].astype(np.int64) - 1, rule[py].astype(np.int64) - 1
                same_part = ((zx == 0) & (zy == 0)).astype(np.int64)
                value = 25 * d['e'] * (1 + zx * zy - same_part) - 4 * (1 - same_part)
                numerator = np.zeros(self.nine.count, np.int64)
                np.add.at(numerator, d['h'], d['count'] * value)
                if int(numerator @ self.nine.control_counts) < 0:
                    raise RuntimeError('Integer recursive-pentagon C5 control failed')
                row = numerator / (50 * math.factorial(9))
                if abs(row @ y - values[choice]) > 1e-10:
                    raise RuntimeError('Pentagon enumeration and rebuilt row disagree')
                added += self.add(
                    row, ('pentagon_recursive_seven', d['code'], list(subset), profiles, rule.tolist()), True
                )
        log(f'Pentagon recursion: {tested} type/subset pairs, all 3^11 rules each, least {least:.12g}, {added} rows')
        return added

    def prune(self, weights: np.ndarray, y: np.ndarray) -> None:
        """Discard unused slack columns; they may be rediscovered."""
        if len(self.rows) < 1800:
            return
        values = np.array(self.rows) @ y
        keep = (weights > 1e-9) | (values < 1e-7)
        for i, (recipe, _scale) in enumerate(self.recipes):
            if (
                recipe[0] == 'lift_eight' and recipe[1][0][0] == 'fixed'
                and recipe[1][0][1] in {'p-a', 'b-p', '(p-a)(b-p)'}
            ):
                keep[i] = True
        self.rows = [r for r, k in zip(self.rows, keep) if k]
        self.recipes = [r for r, k in zip(self.recipes, keep) if k]
        self.cut = [r for r, k in zip(self.cut, keep) if k]
        self.seen = {np.round(r, 11).tobytes() for r in self.rows}
        log(f'Nine-point pruning retained {len(self.rows)} rows')


def build_lifted(
    seed_eight: Path | None = None, three_root_squares: bool = False,
    localized_squares: bool = False,
) -> tuple[Nine, Search, Lifted]:
    """Build the declared tables and genuine-state controls for reuse in discovery."""
    low, high = 1243 / 5000, 3197 / 10000
    eight = FlagSystem(8, low, high)
    search = Search(eight, 3, True, True)
    # Every ordinary square and localizer remains available for separation.
    # Avoid carrying thousands of unused fixed directions into the first LP.
    keep = [i for i, (label, _scale) in enumerate(search.labels)
            if label[0] == 'fixed' and label[1] in {'p-a', 'b-p', '(p-a)(b-p)'}]
    search.rows = [search.rows[i] for i in keep]
    search.labels = [search.labels[i] for i in keep]
    search.is_cut = [search.is_cut[i] for i in keep]
    search.seen = {np.round(r, 11).tobytes() for r in search.rows}
    # All coefficient tables used below have already been split out.
    eight.records.clear()
    eight.codes = None
    eight.classes = None
    gc.collect()
    log('Built the order-eight induction and full-localizer generator')
    nine = Nine(log)
    if np.max(abs(nine.projection @ nine.control - search.control)) > 1e-12:
        raise RuntimeError('C5 deletion identity failed')
    blocks = flag_block(nine, 1, log)
    if three_root_squares:
        blocks += flag_block(nine, 3, log)
    if localized_squares:
        blocks += localizer_blocks(nine, log)
    least = 0.0
    for M, n, recipe in blocks:
        i, j = np.triu_indices(n)
        matrix = np.zeros((n, n))
        matrix[i, j] = (M @ nine.control) / np.where(i == j, 1, np.sqrt(2))
        matrix[j, i] = matrix[i, j]
        # C5 has p=2/5, outside the upper band. That multiplier is
        # negative on this control; check the reversed PSD sign.
        if recipe[0] == 'band_upper_nine':
            matrix = -matrix
        least = min(least, float(np.linalg.eigvalsh(matrix).min()))
    log(f'New nine-point square C5 controls: least eigenvalue {least}')
    if least < -1e-9:
        raise RuntimeError('New flag-square control failed')
    lifted = Lifted(nine, blocks)
    lifted.lift(search)
    if seed_eight is not None:
        metadata = json.loads((seed_eight / 'recipes.json').read_text())
        seed = np.load(seed_eight / 'candidate.npz')
        if (
            metadata['order'] != 8 or metadata['interval'] != [low, high]
            or metadata['target'] != '2/25' or seed['rows'].shape[1] != 410
        ):
            raise ValueError('The floating seed is not from the declared whole-band universe')
        cut_kinds = {'recursive', 'recursive_square', 'full_recursive_square', 'induction_product'}
        for row, recipe, weight in zip(seed['rows'], metadata['rows'], seed['weights']):
            if weight > 1e-10:
                lifted.add(row @ nine.projection, ('lift_eight', recipe), recipe[0][0] in cut_kinds)
        del seed, metadata
        gc.collect()
        log('Imported floating seed rows only; no saved evidence or verdict accepted')
    return nine, search, lifted


def main() -> None:
    """Generate, validate and search the declared lifted system."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seed-eight', type=Path)
    parser.add_argument('--seed-nine', type=Path)
    parser.add_argument('--save', type=Path)
    parser.add_argument('--rounds', type=int, default=30)
    parser.add_argument('--seconds', type=float, default=60)
    parser.add_argument('--three-root-squares', action='store_true')
    parser.add_argument('--localized-squares', action='store_true')
    parser.add_argument('--pentagon-recursion', action='store_true')
    parser.add_argument('--validate-only', action='store_true')
    args = parser.parse_args()
    if args.rounds <= 0 or not np.isfinite(args.seconds) or args.seconds <= 0:
        parser.error('Finite positive rounds and solver time are required')
    nine, search, lifted = build_lifted(
        args.seed_eight, args.three_root_squares, args.localized_squares
    )
    y = np.ones(nine.count) / nine.count
    if args.seed_nine is not None:
        metadata = json.loads((args.seed_nine / 'recipes.json').read_text())
        seed = np.load(args.seed_nine / 'candidate.npz')
        if (
            metadata['order'] != 9
            or metadata['interval'] != [search.system.low, search.system.high]
            or metadata['target'] != '2/25'
            or seed['rows'].shape[1] != nine.count
        ):
            raise ValueError('Nine-point seed does not match the declared universe')
        for row, recipe, weight in zip(seed['rows'], metadata['rows'], seed['weights']):
            if weight > 1e-10:
                label, scale = recipe
                cut = label[0] in {'seven_root_cut', 'pentagon_recursive_seven'} or (
                    label[0] == 'lift_eight' and label[1][0][0] in {
                        'recursive', 'recursive_square', 'full_recursive_square', 'induction_product'
                    }
                ) or (
                    label[0] == 'square_nine'
                    and label[2][0] == 'recursive_localizer_nine'
                )
                lifted.add(row * scale, tuple(label), cut)
        y = np.maximum(seed['state'], 0)
        y /= y.sum()
        del seed, metadata
        gc.collect()
        log('Restored nine-point floating discovery ingredients; no verdict accepted')
    # The exact rebuilt cut controls exercise all proposed root types before a solve.
    added = lifted.price_seven(y, 23)
    if args.pentagon_recursion:
        added += lifted.price_pentagon(y)
    log(f'Initial seven-root pricing added {added} integer-rebuilt rows')
    if args.validate_only:
        log('All declared generation controls pass; no bound certified')
        return
    for iteration in range(args.rounds):
        old = nine.projection @ y
        for family, ti, g in search.mults:
            search.price(family, ti, g, old)
        search.localizers(old)
        search.full_localizers(old)
        search.products(old)
        added = lifted.lift(search)
        added += lifted.price_seven(y, 1000 * iteration + 31)
        if args.pentagon_recursion:
            added += lifted.price_pentagon(y)
        added += lifted.price_squares(y)
        if not any(lifted.cut):
            raise RuntimeError('No cut row for normalization')
        matrix = np.column_stack([*lifted.rows, np.ones(nine.count)])
        objective = np.zeros(matrix.shape[1])
        objective[-1] = -1
        equality = np.r_[np.array(lifted.cut, float), 0][None, :]
        log(f'Nine-point round {iteration}: {len(lifted.rows)} rows; {added} added')
        with warnings.catch_warnings():
            warnings.filterwarnings('ignore', category=OptimizeWarning, message='Unrecognized options detected')
            result = linprog(
                objective, A_ub=matrix, b_ub=np.zeros(nine.count), A_eq=equality, b_eq=[1],
                bounds=[(0, None)] * len(lifted.rows) + [(None, None)], method='highs-ds',
                options={'time_limit': args.seconds, 'threads': 1, 'parallel': False},
            )
        log(f'Nine-point LP status {result.status}: {result.message}')
        if result.status != 0 or result.x is None:
            log('Bounded solve incomplete; no mathematical verdict')
            break
        weights = np.maximum(result.x[:-1], 0)
        margin = float(result.x[-1])
        coefficient = np.column_stack(lifted.rows) @ weights
        log(f'Nine-point floating margin {margin:.12g}; largest coefficient {coefficient.max():.12g}')
        if args.save is not None:
            args.save.mkdir(parents=True, exist_ok=True)
            np.savez(args.save / 'candidate.npz', rows=np.array(lifted.rows), weights=weights,
                     margin=margin, coefficient=coefficient, state=-np.asarray(result.ineqlin.marginals))
            (args.save / 'recipes.json').write_text(json.dumps({
                'standing': 'floating discovery only', 'order': 9,
                'interval': [search.system.low, search.system.high],
                'target': '2/25', 'rows': lifted.recipes,
            }))
        if margin > 1e-7 and coefficient.max() < -1e-8:
            log('Possible whole-band certificate; exact reconstruction and positivity checks required')
            break
        y = np.maximum(-np.asarray(result.ineqlin.marginals), 0)
        if y.sum() <= 0:
            break
        y /= y.sum()
        log(f'Nine-point separation-state density {nine.p @ y:.12g}')
        if added == 0:
            log('No new priced direction; not a complete feasibility result')
            break
        lifted.prune(weights, y)
        del matrix, result, coefficient, weights
        gc.collect()


if __name__ == '__main__':
    main()

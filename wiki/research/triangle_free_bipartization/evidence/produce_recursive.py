"""Discover zero-error certificates from recursive partial-cut inequalities.

This floating-point program uses the canonical sketch's hypothetical
weighted counterexample, not a claimed bound of 2/25 on induced subgraphs.
Its recursive row is alpha - (2/25)(1 - sum_j mass(U_j)^2) >= 0.
An exact negative combination over the entire density band would contradict
that hypothesis. A positive numerical margin is only a recovery candidate.

The program enumerates all uncoloured triangle-free states of order seven
or eight using util.flaglp. It prices profile assignments to fixed colour
biases and one or more independently recut parts. Searches for
assignments and products are incomplete. Degree localizers, ordinary flag
positivity and optional products provide additional valid rows. Neither a
nonpositive discovery margin nor an unfinished solve proves an obstruction.

Every LP has a positive time limit and the number of rounds is finite.
No files are written unless --save names an output directory. Examples:

  uv run --no-sync python wiki/research/triangle_free_bipartization/evidence/produce_recursive.py --order 7 --parts 3 --products
  uv run --no-sync python wiki/research/triangle_free_bipartization/evidence/produce_recursive.py --order 8 --rounds 60 --seconds 30
"""

from __future__ import annotations

import argparse
import json
import time
import warnings
from itertools import product
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.optimize import Bounds, LinearConstraint, OptimizeWarning, linprog, milp
from util.envelopes import cycle
from util.flaglp import FlagSystem
from util.recursive_flags import degree_blocks, degree_scalar_rows, recursive_blocks

TARGET = 2 / 25
START = time.monotonic()


def log(message: str) -> None:
    """Print bounded-discovery progress with elapsed wall time."""
    print(f'{time.monotonic() - START:.1f}s {message}', flush=True)


def integrand(
    side: np.ndarray, px: np.ndarray, py: np.ndarray, edge: np.ndarray
) -> np.ndarray:
    """Evaluate the induction integrand for a deterministic profile assignment.

    Labels -1 and 1 are the fixed sides; -2 gives independent fair coins,
    and -3 and -4 give mean signs -1/2 and 1/2, respectively.
    Label 0 and labels at least 2 designate independent recursive parts.
    Equal recursive labels receive the target mass term; other pairs have
    random relative orientation.
    """
    z = np.where(
        abs(side) == 1, side, np.where(side == -3, -0.5, np.where(side == -4, 0.5, 0))
    )
    same = (side[px] == side[py]) & ((side[px] == 0) | (side[px] >= 2))
    return 0.5 * edge * (1 + z[px] * z[py] - same) - TARGET * (1 - same)


class Search:
    """A finite column collection and incomplete separation procedures."""

    def __init__(
        self, system: FlagSystem, parts: int, products: bool, full: bool = False
    ) -> None:
        """Build the genuine boundary control and the declared fixed rows."""
        self.system = system
        self.parts = parts
        self.control = system.density_vector(cycle(5))
        self.product_tables = system.product_tables() if products else []
        self.rows: list[np.ndarray] = []
        self.labels: list[tuple] = []
        self.is_cut: list[bool] = []
        self.seen: set[bytes] = set()
        self.rules: dict[tuple, tuple[dict, int, np.ndarray]] = {}
        self.rng = np.random.default_rng(23017)
        for label, row in system.fixed:
            self.add(row, ('fixed', str(label)))
        self.mults = system.multipliers()
        self.degree_scalar = degree_scalar_rows(system) if full else []
        for row, recipe in self.degree_scalar:
            if row @ self.control < -1e-10:
                raise RuntimeError('C5 scalar degree control failed')
            self.add(row, ('full_degree_scalar', recipe))
        self.degree_full = degree_blocks(system) if full else []
        self.recursive_full = []
        for M, n, roots, rootcode, recipe in recursive_blocks(system) if full else []:
            cells = 1 << roots
            choices = [-1, 1, -2, -3, -4, 0, *range(2, parts + 1)]
            sides = np.array(list(product(choices, repeat=cells)), np.int8)
            keys = np.arange(2 * cells**2)
            px, py, edge = keys // (2 * cells), (keys // 2) % cells, keys % 2
            vectors = np.array([integrand(side, px, py, edge) for side in sides])
            width = n * (n + 1) // 2
            supported = (
                np.asarray(abs(M).sum(axis=1)).reshape(len(keys), width).sum(axis=1) > 0
            )
            _, keep = np.unique(
                np.round(vectors[:, supported], 12), axis=0, return_index=True
            )
            self.recursive_full.append(
                (M, n, vectors[keep], sides[keep], (roots, rootcode, recipe))
            )
        if full:
            log(
                f'Full localizers: {len(self.degree_full)} degree blocks, {sum(len(x[2]) for x in self.recursive_full)} recursive matrices'
            )
            self.check_full_controls()

    def check_full_controls(self) -> None:
        """Check every additional matrix against the genuine pentagon boundary state."""
        least = 0.0
        for M, n, _recipe in self.degree_full:
            i, j = np.triu_indices(n)
            factor = np.where(i == j, 1, np.sqrt(2))
            matrix = np.zeros((n, n))
            matrix[i, j] = (M @ self.control) / factor
            matrix[j, i] = matrix[i, j]
            least = min(least, float(np.linalg.eigvalsh(matrix).min()))
        for M, n, vectors, _sides, _recipe in self.recursive_full:
            i, j = np.triu_indices(n)
            factor = np.where(i == j, 1, np.sqrt(2))
            coefficients = vectors @ np.asarray(M @ self.control).reshape(
                vectors.shape[1], -1
            )
            matrices = np.zeros((len(vectors), n, n))
            matrices[:, i, j] = coefficients / factor
            matrices[:, j, i] = matrices[:, i, j]
            least = min(least, float(np.linalg.eigvalsh(matrices).min()))
        log(f'Full-localizer C5 control: least eigenvalue {least}')
        if least < -1e-9:
            raise RuntimeError('Full-localizer C5 boundary control failed')
        empty_index = next(i for i, a in enumerate(self.system.graphs) if not a.any())
        negative = min(float(row[empty_index]) for row, _recipe in self.degree_scalar)
        if negative >= -1e-6:
            raise RuntimeError('Empty graph was not rejected by the degree control')
        log(f'Full-localizer empty-graph negative control: scalar degree row {negative}')

    def add(self, row: np.ndarray, label: tuple, cut: bool = False) -> bool:
        """Retain a distinct normalized discovery row with a construction recipe."""
        scale = float(abs(row).max())
        if scale < 1e-13:
            return False
        row = row / scale
        key = np.round(row, 11).tobytes()
        if key in self.seen:
            return False
        # C5 is outside the band but is a genuine boundary extremizer.
        # Do not apply this control to rows that use a band hypothesis.
        if label[0] in {
            'degree_square',
            'recursive_square',
            'induction_product',
            'full_degree_square',
            'full_recursive_square',
        }:
            if row @ self.control < -1e-8:
                raise RuntimeError(f'C5 control failed for {label[0]}')
        self.seen.add(key)
        self.rows.append(row)
        self.labels.append((label, scale))
        self.is_cut.append(cut)
        return True

    def row(self, family: dict, ti: int, g: tuple, side: np.ndarray) -> np.ndarray:
        """Average an induction integrand times its declared rooted multiplier."""
        d = family['data'][ti]
        weight = self.system.multiplier(family, ti, g) * d['w']
        value = integrand(side, d['px'], d['py'], d['e'])
        return np.bincount(d['h'], weights=weight * value, minlength=self.system.count)

    def price(self, family: dict, ti: int, g: tuple, y: np.ndarray) -> bool:
        """Search profile assignments by coordinate minimization in floating arithmetic."""
        d = family['data'][ti]
        profiles = np.array(family['profiles'][ti])
        n = len(profiles)
        size = 1 << family['k']
        weight = self.system.multiplier(family, ti, g) * d['w'] * y[d['h']]
        position = d['px'] * size + d['py']
        adj = np.bincount(position, weights=weight * d['e'], minlength=size**2)
        mass = np.bincount(position, weights=weight, minlength=size**2)
        adj = adj.reshape(size, size)
        mass = mass.reshape(size, size)
        ix = np.ix_(profiles, profiles)
        adj = ((adj + adj.T) / 2)[ix]
        mass = ((mass + mass.T) / 2)[ix]
        Qz = adj / 2
        Qu = TARGET * mass - Qz
        dz, du = np.diag(Qz), np.diag(Qu)
        constant = 0.5 * adj.sum() - TARGET * mass.sum()
        freecodes = np.array([0, *range(2, self.parts + 1)])
        choiceset = np.r_[-1, 1, freecodes, -2, -3, -4]
        best, bestside = 0.0, None
        starts = self.rng.choice(choiceset, (24, n))
        starts[0], starts[1], starts[2] = 0, 1, -1
        for initial in starts:
            side = initial.copy()
            for _ in range(4 * n):
                z = np.where(
                    abs(side) == 1,
                    side,
                    np.where(side == -3, -0.5, np.where(side == -4, 0.5, 0)),
                )
                U = (side[:, None] == freecodes).astype(float)
                lz = 2 * (Qz @ z - dz * z)
                lu = 2 * (Qu @ U - du[:, None] * U)
                choices = np.column_stack(
                    (
                        dz - lz,
                        dz + lz,
                        du[:, None] + lu,
                        np.zeros(n),
                        0.25 * dz - 0.5 * lz,
                        0.25 * dz + 0.5 * lz,
                    )
                )
                current = dz * z * z + lz * z + (du[:, None] * U + lu * U).sum(axis=1)
                change = choices - current[:, None]
                i, j = np.unravel_index(change.argmin(), change.shape)
                if change[i, j] >= -1e-13:
                    break
                side[i] = choiceset[j]
            z = np.where(
                abs(side) == 1,
                side,
                np.where(side == -3, -0.5, np.where(side == -4, 0.5, 0)),
            )
            U = (side[:, None] == freecodes).astype(float)
            value = constant + z @ Qz @ z + np.sum(U * (Qu @ U))
            if value < best:
                best, bestside = float(value), side.copy()
        if bestside is None or best >= -1e-10:
            return False
        full = np.zeros(size, dtype=np.int8)
        full[profiles] = bestside
        row = self.row(family, ti, g, full)
        if g[0] not in ('p-a', 'b-p') and row @ self.control < -1e-10:
            raise RuntimeError('C5 recursive boundary control failed')
        if abs(row @ y - best) > 1e-9:
            raise RuntimeError('Pricing value and reconstructed row disagree')
        self.rules[(family['k'], ti, full.tobytes())] = (family, ti, full.copy())
        return self.add(row, ('recursive', family['k'], ti, g, full.tolist()), True)

    def localizers(self, y: np.ndarray) -> int:
        """Price ordinary squares and squares localized by degree or induction."""
        system = self.system
        added = 0
        for key, block in system.blocks.items():
            eig, vectors = np.linalg.eigh(system.block_matrix(block, y))
            for j in np.flatnonzero(eig < -1e-10)[:5]:
                v = vectors[:, j]
                added += self.add(
                    system.block_row(block, v), ('square', str(key), v.tolist())
                )
        family = system.families[2]
        k = family['k']
        size = 1 << k
        for ti, profiles in enumerate(family['profiles']):
            d = family['data'][ti]
            for root in range(k):
                value = (
                    0.5 * (((d['px'] >> root) & 1) + ((d['py'] >> root) & 1))
                    - 2 * TARGET
                )
                added += self.localize(
                    d, profiles, size, value, y, ('degree_square', k, ti, root), False
                )
        for family, ti, side in list(self.rules.values()):
            if family['m'] != 2:
                continue
            d = family['data'][ti]
            added += self.localize(
                d,
                family['profiles'][ti],
                1 << family['k'],
                integrand(side, d['px'], d['py'], d['e']),
                y,
                ('recursive_square', family['k'], ti, side.tolist()),
                True,
            )
        return added

    def binary_pricing(self, y: np.ndarray, seconds: float) -> int:
        """Price deterministic cuts on the largest root family with bounded MIPs.

        Any returned side assignment is checked by rebuilding its row;
        neither a time limit nor a locally or numerically optimal result
        is a claim of exhaustive cut pricing. Signed pair weights are
        allowed, so all four XOR inequalities are imposed.
        """
        if seconds <= 0 or not np.isfinite(seconds):
            raise ValueError('Binary pricing needs a finite positive time limit')
        family = self.system.families[0]
        added = 0
        incomplete = 0
        for ti, profiles in enumerate(family['profiles']):
            table, mass = self.system.aggregate(family, ti, ('one',), y)
            n = len(profiles)
            table = table[np.ix_(profiles, profiles)]
            i, j = np.triu_indices(n, 1)
            pair = (table + table.T)[i, j]
            keep = abs(pair) > 1e-14
            i, j, pair = i[keep], j[keep], pair[keep]
            count = len(pair)
            scale = float(abs(pair).sum())
            if count == 0 or scale < 1e-13 or mass < 1e-13:
                continue
            row = np.arange(count)[:, None] * 4 + np.arange(4)
            rr = np.repeat(row[:, :, None], 3, axis=2).ravel()
            cc = np.stack(
                (np.broadcast_to(i[:, None], row.shape),
                 np.broadcast_to(j[:, None], row.shape),
                 np.broadcast_to(n + np.arange(count)[:, None], row.shape)),
                axis=2,
            ).ravel()
            signs = np.array([[-1, -1, 1], [1, 1, 1], [1, -1, -1], [-1, 1, -1]])
            matrix = sparse.coo_matrix(
                (np.tile(signs, (count, 1)).ravel(), (rr, cc)),
                shape=(4 * count, n + count),
            ).tocsr()
            upper = np.tile([0, 2, 0, 0], count)
            high = np.ones(n + count)
            high[0] = 0
            with warnings.catch_warnings():
                warnings.filterwarnings(
                    'ignore', category=RuntimeWarning, message='Unrecognized options detected'
                )
                result = milp(
                    np.r_[np.zeros(n), -pair / scale],
                    integrality=np.r_[np.ones(n), np.zeros(count)],
                    bounds=Bounds(np.zeros(n + count), high),
                    constraints=LinearConstraint(matrix, -np.inf, upper),
                    options={
                        'time_limit': seconds, 'threads': 1, 'parallel': False,
                        'mip_rel_gap': 0,
                    },
                )
            incomplete += result.status != 0
            if result.x is None or not np.isfinite(result.x[:n]).all():
                continue
            side = np.zeros(1 << family['k'], np.int8)
            side[profiles] = np.where(result.x[:n] >= 0.5, 1, -1)
            candidate = self.row(family, ti, ('one',), side)
            if candidate @ self.control < -1e-10:
                raise RuntimeError('MIP-proposed cut fails the C5 control')
            if candidate @ y < -1e-11:
                self.rules[(family['k'], ti, side.tobytes())] = (family, ti, side.copy())
                added += self.add(
                    candidate, ('recursive', family['k'], ti, ('one',), side.tolist()), True
                )
        log(f'Bounded binary pricing: {added} new rows; {incomplete} unfinished solves')
        return added

    def ternary_pricing(self, y: np.ndarray, seconds: float, types: int) -> int:
        """Propose one-recursive-part rules on a bounded selection of root types.

        Binary variables a_i,b_i select the two outside colours; a_i+b_i<=1.
        The zero choice belongs to the recursive part. Pair products use
        McCormick inequalities and are exact for integral a,b. Returned
        proposals are rounded to a valid ternary rule and its actual row
        is rebuilt; numerical optimality is not used as a premise.
        """
        if seconds <= 0 or not np.isfinite(seconds) or types <= 0:
            raise ValueError('Positive bounded ternary pricing parameters required')
        family = self.system.families[0]
        masses = [float(d['w'] @ y[d['h']]) for d in family['data']]
        added = 0
        incomplete = 0
        for ti in np.argsort(masses)[-types:]:
            if masses[ti] < 1e-13:
                continue
            profiles = np.asarray(family['profiles'][ti])
            d = family['data'][ti]
            size = 1 << family['k']
            weight = d['w'] * y[d['h']]
            key = d['px'] * size + d['py']
            mass = np.bincount(key, weights=weight, minlength=size**2).reshape(size, size)
            adj = np.bincount(key, weights=weight * d['e'], minlength=size**2).reshape(size, size)
            take = np.ix_(profiles, profiles)
            mass = ((mass + mass.T) / 2)[take]
            adj = ((adj + adj.T) / 2)[take]
            qz, qu = adj / 2, TARGET * mass - adj / 2
            n = len(profiles)
            linear = np.diag(qz) + np.diag(qu) - 2 * qu.sum(axis=1)
            ii, jj = np.triu_indices(n, 1)
            i = np.r_[ii, n + ii, ii, n + ii]
            j = np.r_[jj, n + jj, n + jj, jj]
            coefficients = 2 * np.r_[
                (qu + qz)[ii, jj], (qu + qz)[ii, jj],
                (qu - qz)[ii, jj], (qu - qz)[ii, jj],
            ]
            keep = abs(coefficients) > 1e-14
            i, j, coefficients = i[keep], j[keep], coefficients[keep]
            count = len(i)
            objective = np.r_[linear, linear, coefficients]
            scale = float(abs(objective).sum())
            if scale < 1e-13:
                continue
            product_index = 2 * n + np.arange(count)
            matrix = sparse.lil_matrix((n + 3 * count, 2 * n + count))
            for h in range(n):
                matrix[h, h] = matrix[h, n + h] = 1
            for h in range(count):
                r = n + 3 * h
                matrix[r, i[h]] = matrix[r, j[h]] = 1
                matrix[r, product_index[h]] = -1
                matrix[r + 1, product_index[h]] = 1
                matrix[r + 1, i[h]] = -1
                matrix[r + 2, product_index[h]] = 1
                matrix[r + 2, j[h]] = -1
            upper = np.r_[np.ones(n), np.tile([1, 0, 0], count)]
            high = np.ones(2 * n + count)
            high[n] = 0  # Complement the outside colours if the first cell is negative.
            with warnings.catch_warnings():
                warnings.filterwarnings(
                    'ignore', category=RuntimeWarning, message='Unrecognized options detected'
                )
                result = milp(
                    objective / scale,
                    integrality=np.r_[np.ones(2 * n), np.zeros(count)],
                    bounds=Bounds(np.zeros(2 * n + count), high),
                    constraints=LinearConstraint(matrix.tocsr(), -np.inf, upper),
                    options={
                        'time_limit': seconds, 'threads': 1, 'parallel': False,
                        'mip_rel_gap': 0,
                    },
                )
            incomplete += result.status != 0
            if result.x is None or not np.isfinite(result.x[:2 * n]).all():
                continue
            side = np.zeros(size, np.int8)
            choices = np.column_stack((
                1 - result.x[:n] - result.x[n:2 * n],
                result.x[:n], result.x[n:2 * n],
            ))
            side[profiles] = np.array([0, 1, -1], np.int8)[choices.argmax(axis=1)]
            candidate = self.row(family, int(ti), ('one',), side)
            if candidate @ self.control < -1e-10:
                raise RuntimeError('Ternary proposal fails the C5 control')
            if candidate @ y < -1e-11:
                self.rules[(family['k'], int(ti), side.tobytes())] = (
                    family, int(ti), side.copy()
                )
                added += self.add(
                    candidate, ('recursive', family['k'], int(ti), ('one',), side.tolist()), True
                )
        log(f'Bounded ternary pricing: {added} new rows; {incomplete} unfinished solves')
        return added

    def full_localizers(self, y: np.ndarray) -> int:
        """Price full-flag degree and recursive square directions in the declared bases."""
        added = 0
        for row, recipe in self.degree_scalar:
            if row @ y < -1e-10:
                added += self.add(row, ('full_degree_scalar', recipe))
        for block, (M, n, recipe) in enumerate(self.degree_full):
            i, j = np.triu_indices(n)
            factor = np.where(i == j, 1, np.sqrt(2))
            matrix = np.zeros((n, n))
            matrix[i, j] = (M @ y) / factor
            matrix[j, i] = matrix[i, j]
            eig, V = np.linalg.eigh(matrix)
            for h in np.flatnonzero(eig < -1e-10)[:3]:
                v = V[:, h]
                row = np.asarray(M.T @ (v[i] * v[j] * factor)).ravel()
                added += self.add(
                    row, ('full_degree_square', block, recipe, v.tolist())
                )
        for block, (M, n, vectors, sides, recipe) in enumerate(self.recursive_full):
            i, j = np.triu_indices(n)
            factor = np.where(i == j, 1, np.sqrt(2))
            coefficients = vectors @ np.asarray(M @ y).reshape(vectors.shape[1], -1)
            matrices = np.zeros((len(vectors), n, n))
            matrices[:, i, j] = coefficients / factor
            matrices[:, j, i] = matrices[:, i, j]
            eig, V = np.linalg.eigh(matrices)
            for flat in np.argsort(eig, axis=None)[:30]:
                rule, h = np.unravel_index(flat, eig.shape)
                if eig[rule, h] >= -1e-10:
                    break
                v = V[rule, :, h]
                weights = vectors[rule, :, None] * (v[i] * v[j] * factor)[None, :]
                row = np.asarray(M.T @ weights.ravel()).ravel()
                added += self.add(
                    row,
                    (
                        'full_recursive_square',
                        block,
                        recipe,
                        sides[rule].tolist(),
                        v.tolist(),
                    ),
                    True,
                )
        return added

    def localize(
        self,
        d: dict,
        profiles: list[int],
        size: int,
        value: np.ndarray,
        y: np.ndarray,
        label: tuple,
        cut: bool,
    ) -> int:
        """Price at most three negative directions of one rooted profile block."""
        matrix = np.bincount(
            d['z1'] * size + d['z2'],
            weights=d['w'] * y[d['h']] * value,
            minlength=size**2,
        ).reshape(size, size)
        matrix = ((matrix + matrix.T) / 2)[np.ix_(profiles, profiles)]
        eig, vectors = np.linalg.eigh(matrix)
        added = 0
        for j in np.flatnonzero(eig < -1e-10)[:3]:
            v = np.zeros(size)
            v[profiles] = vectors[:, j]
            row = np.bincount(
                d['h'],
                weights=d['w'] * value * v[d['z1']] * v[d['z2']],
                minlength=self.system.count,
            )
            added += self.add(row, (*label, v.tolist()), cut)
        return added

    def products(self, y: np.ndarray) -> int:
        """Price products from a finite list of induction and degree factors."""
        family = self.system.families[2]
        k = family['k']
        size = 1 << k
        keys = np.arange(1 << (2 * k + 1))
        px, py, edge = keys >> (k + 1), (keys >> 1) & (size - 1), keys & 1
        added = 0
        for ti, d in enumerate(self.product_tables):
            options = []
            for f, t, side in self.rules.values():
                if f['k'] == k and t == ti:
                    options.append(
                        (
                            float(self.row(f, ti, ('one',), side) @ y),
                            ('cut', side.tolist()),
                            integrand(side, px, py, edge),
                        )
                    )
            options.sort(key=lambda x: x[0])
            options = options[:100]
            for root in range(k):
                value = 0.5 * (((px >> root) & 1) + ((py >> root) & 1)) - 2 * TARGET
                options.append((0, ('degree', root), value))
            if not options:
                continue
            V = np.array([x[2] for x in options])
            count = len(keys)
            joint = np.bincount(
                d['first'] * count + d['second'],
                weights=d['w'] * y[d['h']],
                minlength=count**2,
            ).reshape(count, count)
            values = V @ ((joint + joint.T) / 2) @ V.T
            for flat in np.argsort(values, axis=None)[:30]:
                a, b = np.unravel_index(flat, values.shape)
                if values[a, b] >= -1e-11:
                    break
                row = np.bincount(
                    d['h'],
                    weights=d['w'] * V[a, d['first']] * V[b, d['second']],
                    minlength=self.system.count,
                )
                added += self.add(
                    row,
                    ('induction_product', k, ti, options[a][1], options[b][1]),
                    True,
                )
        return added

    def prune(self, weights: np.ndarray, y: np.ndarray) -> None:
        """Drop unused positive-slack columns without asserting complete pricing."""
        if len(self.rows) <= 1000:
            return
        values = np.array(self.rows) @ y
        keep = (weights > 1e-8) | (values < 1e-7)
        # Keep the three explicit band inequalities even if currently slack.
        for i, (label, _scale) in enumerate(self.labels):
            if label[0] == 'fixed' and label[1] in {'p-a', 'b-p', '(p-a)(b-p)'}:
                keep[i] = True
        removed = int((~keep).sum())
        self.rows = [r for r, q in zip(self.rows, keep) if q]
        self.labels = [r for r, q in zip(self.labels, keep) if q]
        self.is_cut = [r for r, q in zip(self.is_cut, keep) if q]
        self.seen = {np.round(r, 11).tobytes() for r in self.rows}
        log(f'Pruned {removed} inactive discovery columns; retained {len(self.rows)}')


def main() -> None:
    """Run a bounded search and save only explicitly requested numerical data."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--order', type=int, choices=(7, 8), default=7)
    parser.add_argument('--parts', type=int, choices=range(1, 9), default=3)
    parser.add_argument('--rounds', type=int, default=60)
    parser.add_argument('--seconds', type=float, default=30)
    parser.add_argument(
        '--interval', nargs=2, type=float, default=(1243 / 5000, 3197 / 10000)
    )
    parser.add_argument('--products', action='store_true')
    parser.add_argument('--full-localizers', action='store_true')
    parser.add_argument('--keep-inactive', action='store_true')
    parser.add_argument('--mip-seconds', type=float, default=0)
    parser.add_argument('--ternary-seconds', type=float, default=0)
    parser.add_argument('--ternary-types', type=int, default=6)
    parser.add_argument('--save', type=Path)
    args = parser.parse_args()
    if args.rounds <= 0 or not np.isfinite(args.seconds) or args.seconds <= 0:
        parser.error('--rounds and --seconds must be finite and positive')
    if not np.isfinite(args.mip_seconds) or args.mip_seconds < 0:
        parser.error('--mip-seconds must be finite and nonnegative')
    if (
        not np.isfinite(args.ternary_seconds) or args.ternary_seconds < 0
        or args.ternary_types <= 0
    ):
        parser.error('--ternary-seconds must be finite and nonnegative; --ternary-types positive')
    low, high = args.interval
    if not np.isfinite([low, high]).all() or not 0 <= low < high <= 0.5:
        parser.error('the density interval must lie in [0,1/2] with distinct endpoints')
    system = FlagSystem(args.order, low, high)
    log(f'Built {system.count} uncoloured states and {len(system.blocks)} PSD blocks')
    search = Search(system, args.parts, args.products, args.full_localizers)
    y = np.ones(system.count) / system.count
    for iteration in range(args.rounds):
        added = sum(search.price(f, ti, g, y) for f, ti, g in search.mults)
        if args.mip_seconds:
            added += search.binary_pricing(y, args.mip_seconds)
        if args.ternary_seconds:
            added += search.ternary_pricing(y, args.ternary_seconds, args.ternary_types)
        added += search.localizers(y)
        added += search.full_localizers(y)
        added += search.products(y)
        log(
            f'Round {iteration}: {len(search.rows)} rows, {sum(search.is_cut)} normalized rows, {added} added'
        )
        if not any(search.is_cut):
            raise RuntimeError('No induction row is available for normalization')
        matrix = np.column_stack([*search.rows, np.ones(system.count)])
        objective = np.zeros(matrix.shape[1])
        objective[-1] = -1
        equality = np.r_[np.array(search.is_cut, dtype=float), 0][None, :]
        with warnings.catch_warnings():
            warnings.filterwarnings(
                'ignore',
                category=OptimizeWarning,
                message='Unrecognized options detected',
            )
            result = linprog(
                objective,
                A_ub=matrix,
                b_ub=np.zeros(system.count),
                A_eq=equality,
                b_eq=[1],
                bounds=[(0, None)] * len(search.rows) + [(None, None)],
                method='highs-ds',
                options={'time_limit': args.seconds, 'threads': 1, 'parallel': False},
            )
        log(f'LP status {result.status}: {result.message}')
        if result.status != 0 or result.x is None:
            log('Bounded solve incomplete; no mathematical verdict')
            break
        eps = float(result.x[-1])
        weights = np.maximum(result.x[:-1], 0)
        coefficient = np.column_stack(search.rows) @ weights
        log(f'Floating margin {eps:.12g}; largest coefficient {coefficient.max():.12g}')
        if args.save is not None:
            args.save.mkdir(parents=True, exist_ok=True)
            np.savez(
                args.save / 'candidate.npz',
                state=-np.asarray(result.ineqlin.marginals),
                weights=weights,
                rows=np.array(search.rows),
                margin=eps,
                coefficient=coefficient,
            )
            (args.save / 'recipes.json').write_text(
                json.dumps(
                    {
                        'standing': 'floating discovery only',
                        'order': args.order,
                        'interval': [low, high],
                        'parts': args.parts,
                        'products': args.products,
                        'full_localizers': args.full_localizers,
                        'binary_pricing_seconds': args.mip_seconds,
                        'ternary_pricing_seconds': args.ternary_seconds,
                        'ternary_pricing_types': args.ternary_types,
                        'target': '2/25',
                        'rows': search.labels,
                    }
                )
            )
        if eps > 1e-7 and coefficient.max() < -1e-8:
            log(
                'Possible zero-error certificate on the requested interval; exact recovery and all positivity checks remain required'
            )
            break
        y = np.maximum(-np.asarray(result.ineqlin.marginals), 0)
        if y.sum() <= 0:
            log('No usable numerical separation state')
            break
        y /= y.sum()
        log(f'Separation-state density {system.p_vector @ y:.12g}')
        if added == 0:
            log('Local pricing stopped; this is not an exact feasibility result')
            break
        if not args.keep_inactive:
            search.prune(weights, y)


if __name__ == '__main__':
    main()

"""Discover full-band certificates for the weighted-extremal paired-cut system.

This is floating-point discovery, not an evidence entry point. It builds
all sampled triangle-free states with two cut colours, applies the exact-valid
families defined in the canonical proof sketch, and seeks Bernstein-polynomial
nonnegative multipliers. The coefficient target is

  m <= B - (1-rho) (B-2/25)^d / (4/47-2/25)^(d-1),  rho < 1.

Such a certificate, recovered with exact rows, nonnegative multipliers and
positive semidefinite factors, would exclude every weighted counterexample.
This program does not do that exact recovery. Failure, a time limit, or a
state with no locally priced violation is not a mathematical obstruction.
Every LP has a positive time limit and the number of rounds is finite.

Examples from the repository root:
  uv run --no-sync python wiki/research/triangle_free_bipartization/evidence/produce_extremal.py --validate-only
  uv run --no-sync python wiki/research/triangle_free_bipartization/evidence/produce_extremal.py --degree 2 --rounds 12 --seconds 120

No files are written unless --save names an output directory. All runtime
state, numerical arrays and recipes then go into that directory. No saved
success flag is read, and no solver installation is required beyond SciPy.
"""

from __future__ import annotations

import argparse
import gc
import hashlib
import json
import warnings
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.optimize import OptimizeWarning, linprog
from util.extremal_model import (
    B0,
    Family,
    System,
    affine_hereditary_blocks,
    b,
    cut_horn_rows,
    cut_pattern_blocks,
    cut_scaled_horn_rows,
    cut_triangle_rows,
)
from util.paired_flags import Table, log, pairs

DELTA = B0 - b


class Rows:
    """Collect normalized affine inequalities and their reconstruction recipes."""

    def __init__(self, K: int) -> None:
        """Initialize an empty collection on K sampled graph classes."""
        self.K = K
        self.r = []
        self.d = []
        self.rec = []
        self.seen = set()

    def add(
        self,
        row: np.ndarray | sparse.spmatrix,
        der: np.ndarray | sparse.spmatrix | None,
        recipe: tuple,
    ) -> bool:
        """Retain a numerically distinct row and its derivative in B."""
        r = sparse.csr_matrix(row)
        d = sparse.csr_matrix(r.shape) if der is None else sparse.csr_matrix(der)
        scale = max(float(abs(r).max()), float(abs(r - DELTA * d).max()))
        if scale < 1e-14:
            return False
        r = r / scale
        d = d / scale
        r.eliminate_zeros()
        d.eliminate_zeros()
        r.sort_indices()
        d.sort_indices()
        key = hashlib.blake2b(
            r.indices.tobytes()
            + np.round(r.data, 12).tobytes()
            + d.indices.tobytes()
            + np.round(d.data, 12).tobytes(),
            digest_size=16,
        ).digest()
        if key in self.seen:
            return False
        self.seen.add(key)
        self.r.append(r)
        self.d.append(d)
        self.rec.append((recipe, scale))
        return True

    def matrices(self) -> tuple[sparse.csr_matrix, sparse.csr_matrix]:
        """Stack retained rows and derivatives in matching order."""
        return sparse.vstack(self.r, format='csr'), sparse.vstack(self.d, format='csr')


def control_state(
    tb: Table,
    isolate: bool = False,
    cycle_size: int = 5,
    dependent: bool = False,
) -> np.ndarray:
    """Sample uniform optimal cuts of an odd cycle, optionally with an isolate."""
    n = cycle_size + int(isolate)
    a = np.zeros((n, n), np.int64)
    for i in range(cycle_size):
        a[i, (i + 1) % cycle_size] = a[(i + 1) % cycle_size, i] = 1
    cuts = []
    for mask in range(1 << (n - 1)):
        c = (mask >> np.arange(n)) & 1
        if sum(c[i] == c[j] for i, j in pairs(n) if a[i, j]) == 1:
            cuts.append(c)
    order = tb.n
    edge_count = order * (order - 1) // 2
    pos = np.indices((n,) * order, dtype=np.int16).reshape(order, -1)
    edge = np.zeros(pos.shape[1], np.int64)
    for k, (i, j) in enumerate(pairs(order)):
        edge |= a[pos[i], pos[j]] << k
    lookup = np.full(
        1 << (edge_count + 2 * order), -1, np.int16 if tb.count < 32768 else np.int32
    )
    lookup[tb.codes] = tb.graph
    counts = np.zeros(tb.count, np.int64)
    for c in cuts:
        for d in [c] if dependent else cuts:
            code = edge.copy()
            for i in range(order):
                code |= (c[pos[i]] + 2 * d[pos[i]]) << (edge_count + 2 * i)
            indices = lookup[code]
            if indices.min() < 0:
                raise RuntimeError('genuine paired state missing')
            counts += np.bincount(indices, minlength=tb.count)
    return counts / counts.sum()


def validate(system: System) -> np.ndarray:
    """Check genuine C5 positivity and the unbalanced-isolate negative control."""
    tb = system.tb
    y = control_state(tb)
    negative = control_state(tb, True)
    lo = 1.0
    equality = 0.0
    for i, (r, d, _rc) in enumerate(
        zip(system.rows, system.derivatives, system.recipes)
    ):
        if i >= system.band_start:
            continue
        value = float((r @ y)[0]) + (b - B0) * (0 if d is None else float((d @ y)[0]))
        lo = min(lo, value)
    for M, n in (
        system.blocks[: system.ordinary_count + 1]
        + system.blocks[system.ordinary_count + 3 :]
    ):
        i, j = np.triu_indices(n)
        fac = np.where(i == j, 1, np.sqrt(2))
        mat = np.zeros((n, n))
        mat[i, j] = (M @ y) / fac
        mat[j, i] = mat[i, j]
        lo = min(lo, float(np.linalg.eigvalsh(mat).min()))
    bad = 0.0
    for r, d in zip(system.equalities, system.eqder):
        equality = max(equality, abs(float((r @ y)[0] + (b - B0) * (d @ y)[0])))
        bad = max(
            bad, abs(float((r @ negative)[0] + (2 / 36 - B0) * (d @ negative)[0]))
        )
    log(
        f'paired exact-density controls: C5 m={system.c @ y}, p={system.p @ y}, least valid row/block {lo}, equality {equality}; C5+isolate equality error {bad}'
    )
    if (
        abs(system.c @ y - 0.08) > 1e-12
        or abs(system.p @ y - 0.4) > 1e-12
        or lo < -1e-9
        or equality > 1e-12
        or bad < 1e-6
    ):
        raise RuntimeError('paired control failed')
    heptagon = control_state(tb, cycle_size=7)
    heptagon_bound = 2 / 49
    heptagon_min = 0.0
    for r, d in zip(system.rows, system.derivatives):
        value = float((r @ heptagon)[0])
        if d is not None:
            value += (heptagon_bound - B0) * float((d @ heptagon)[0])
        heptagon_min = min(heptagon_min, value)
    for M, n in system.blocks:
        i, j = np.triu_indices(n)
        factor = np.where(i == j, 1, np.sqrt(2))
        matrix = np.zeros((n, n))
        matrix[i, j] = (M @ heptagon) / factor
        matrix[j, i] = matrix[i, j]
        heptagon_min = min(heptagon_min, float(np.linalg.eigvalsh(matrix).min()))
    dependent = control_state(tb, dependent=True)
    dependent_error = max(
        abs(float((r @ dependent)[0] + (b - B0) * (d @ dependent)[0]))
        for r, d in zip(system.equalities, system.eqder)
    )
    log(
        f'C7 in-band control: m={system.c @ heptagon}, '
        f'p={system.p @ heptagon}, least row/block {heptagon_min}; '
        f'dependent C5-cut-pair equality error {dependent_error}'
    )
    if (
        abs(system.c @ heptagon - heptagon_bound) > 1e-12
        or abs(system.p @ heptagon - 2 / 7) > 1e-12
        or heptagon_min < -1e-9
        or dependent_error < 1e-6
    ):
        raise RuntimeError('C7 or dependent-cut control failed')
    return y


def psd_rows(
    blocks: list[tuple[sparse.spmatrix, int]],
    y: np.ndarray,
    initial: bool = False,
    limit: int = 1000,
) -> list[tuple[float, np.ndarray, tuple]]:
    """Price rank-one square inequalities against a numerical dual state."""
    out = []
    for bi, (M, n) in enumerate(blocks):
        i, j = np.triu_indices(n)
        fac = np.where(i == j, 1, np.sqrt(2))
        mat = np.zeros((n, n))
        mat[i, j] = (M @ y) / fac
        mat[j, i] = mat[i, j]
        ev, V = np.linalg.eigh(mat)
        take = range(min(3, n)) if initial else np.flatnonzero(ev < -1e-10)
        for h in take:
            v = V[:, h]
            row = np.asarray(M.T @ (v[i] * v[j] * fac)).ravel()
            scale = float(abs(row).max())
            if scale > 1e-14:
                out.append((ev[h] / scale, row / scale, ('psd', bi, v.tolist(), scale)))
    out.sort(key=lambda x: x[0])
    log(f'paired PSD separation {len(out)}, least {out[0][0] if out else 0}')
    return out[:limit]


def validate_proper(system: System, pentagon: np.ndarray) -> None:
    """Check proper-subset recipes against two exact-density cycle controls.

    A deterministic non-genuine state proposes rows. Every proposal must
    omit its named root, have zero derivative in B, and be nonnegative
    on independent optimal-cut pairs from C5 and C7. This tests the new
    implementation, not the general minimal-counterexample argument.
    """
    heptagon = control_state(system.tb, cycle_size=7)
    rng = np.random.default_rng(872)
    y = rng.dirichlet(np.ones(system.tb.count) / 10)
    count = 0
    least = 0.0
    for family in system.families:
        for anchor in range(family.k):
            for mode in ('root', 'cross0', 'cross1'):
                candidates = family.price(
                    y, limit=8, proper_anchor=anchor, proper_mode=mode
                )
                candidates += family.recursive(
                    y, limit=8, proper_anchor=anchor, proper_mode=mode
                )
                for row, derivative, recipe in candidates:
                    _, root, rule, _, code, selection = recipe
                    f = int(np.searchsorted(family.codes, code))
                    selected = np.asarray(selection)[
                        family.proper_exclusions(root, rule)[f]
                    ]
                    if (
                        (recipe[0] == 'proper_hereditary' and np.any(selected != 0))
                        or (
                            recipe[0] == 'proper_recursive_cut'
                            and np.any(selected == 0)
                        )
                        or np.any(derivative)
                    ):
                        raise RuntimeError('Proper-subset recipe retained its exclusion')
                    least = min(least, float(row @ pentagon), float(row @ heptagon))
                    count += 1
    log(f'Proper-support controls: {count} proposed rows, least cycle value {least}')
    if count == 0 or least < -1e-10:
        raise RuntimeError('Proper-support comparison control failed')


def affine_psd_rows(
    blocks: list[tuple[sparse.spmatrix, sparse.spmatrix, int, int]],
    y: np.ndarray,
    lower: np.ndarray | None = None,
    initial: bool = False,
    limit: int = 700,
) -> list[tuple[float, np.ndarray, np.ndarray, tuple]]:
    """Price affine hereditary square inequalities at a Bernstein dual slot."""
    out = []
    for bi, (M, D, n, mask) in enumerate(blocks):
        i, j = np.triu_indices(n)
        fac = np.where(i == j, 1, np.sqrt(2))
        value = M @ y
        if lower is not None:
            value -= DELTA * (D @ lower)
        mat = np.zeros((n, n))
        mat[i, j] = value / fac
        mat[j, i] = mat[i, j]
        ev, V = np.linalg.eigh(mat)
        take = range(min(2, n)) if initial else np.flatnonzero(ev < -1e-10)
        for h in take:
            v = V[:, h]
            weights = v[i] * v[j] * fac
            row = np.asarray(M.T @ weights).ravel()
            der = np.asarray(D.T @ weights).ravel()
            scale = max(float(abs(row).max()), float(abs(row - DELTA * der).max()))
            if scale > 1e-14:
                out.append(
                    (
                        ev[h] / scale,
                        row / scale,
                        der / scale,
                        ('affine_psd', bi, int(mask), v.tolist(), scale),
                    )
                )
    out.sort(key=lambda x: x[0])
    log(f'paired affine PSD separation {len(out)}, least {out[0][0] if out else 0}')
    return out[:limit]


def save_candidate(
    destination: Path | None,
    rows: Rows,
    R: sparse.spmatrix,
    D: sparse.spmatrix,
    weights: np.ndarray,
    rho: float,
    maxima: list[float],
    order: int,
    degree: int,
) -> None:
    """Save numerical ingredients for later reconstruction, never a verdict."""
    if destination is None:
        return
    destination.mkdir(parents=True, exist_ok=True)
    np.savez(destination / 'candidate.npz', weights=weights, rho=rho, maxima=maxima)
    sparse.save_npz(destination / 'rows.npz', R)
    sparse.save_npz(destination / 'derivatives.npz', D)
    (destination / 'recipes.json').write_text(
        json.dumps(
            {
                'order': order,
                'degree': degree,
                'rows': rows.rec,
                'band': ['1243/5000', '3197/10000'],
                'target': '2/25',
                'initial_bound': '4/47',
                'standing': 'floating discovery only',
                'proper_support_hypothesis': any(
                    recipe[0] in {'proper_hereditary', 'proper_recursive_cut'}
                    for recipe, _scale in rows.rec
                ),
            }
        )
    )


def main() -> None:
    """Run finite, bounded discovery or its genuine-state validation controls."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--order', type=int, choices=(5, 6), default=5)
    parser.add_argument('--degree', type=int, choices=(1, 2, 3, 4), default=1)
    parser.add_argument('--rounds', type=int, default=12)
    parser.add_argument('--seconds', type=float, default=120)
    parser.add_argument('--save', type=Path)
    parser.add_argument('--validate-only', action='store_true')
    parser.add_argument('--affine-squares', action='store_true')
    parser.add_argument('--minimal-support', action='store_true')
    parser.add_argument('--triangle-pricing-seconds', type=float, default=0)
    args = parser.parse_args()
    if args.rounds <= 0 or not np.isfinite(args.seconds) or args.seconds <= 0:
        parser.error('--rounds and --seconds must be finite and positive')
    if args.affine_squares and args.order != 5:
        parser.error('--affine-squares is implemented at order five only')
    if (
        not np.isfinite(args.triangle_pricing_seconds)
        or args.triangle_pricing_seconds < 0
    ):
        parser.error('--triangle-pricing-seconds must be finite and nonnegative')
    system = System(args.order)
    coupling = cut_pattern_blocks(system)
    system.blocks.extend((M, n) for M, n, _, _ in coupling)
    y = validate(system)
    if args.minimal_support:
        validate_proper(system, y)
    affine = affine_hereditary_blocks(system) if args.affine_squares else []
    for M, D, n, _mask in affine:
        i, j = np.triu_indices(n)
        factor = np.where(i == j, 1, np.sqrt(2))
        matrix = np.zeros((n, n))
        matrix[i, j] = ((M - DELTA * D) @ y) / factor
        matrix[j, i] = matrix[i, j]
        if np.linalg.eigvalsh(matrix).min() < -1e-9:
            raise RuntimeError('Genuine C5 state fails an affine square control')
    if args.validate_only:
        log('All declared numerical implementation controls pass; no bound certified')
        return
    K = len(system.c)
    rows = Rows(K)
    for row, derivative, recipe in zip(
        system.rows,
        system.derivatives,
        system.recipes,
    ):
        rows.add(row, derivative, recipe)
    cap = len(rows.r)
    if not rows.add((B0 - system.c)[None, :], np.ones((1, K)), ('global_cap',)):
        raise RuntimeError('Explicit feasible baseline was unexpectedly duplicated')
    for _, row, recipe in psd_rows(system.blocks, y, initial=True):
        rows.add(row[None, :], None, recipe)
    for _, row, derivative, recipe in affine_psd_rows(
        affine,
        y,
        y,
        initial=True,
    ):
        rows.add(row[None, :], derivative[None, :], recipe)
    system.rows = []
    system.derivatives = []
    system.equalities = []
    system.eqder = []
    states = [(y, y)]
    previous_count = None
    degree = args.degree
    for round_index in range(args.rounds):
        if not system.families:
            system.tb = Table(args.order)
            system.families = [Family(system.tb, k) for k in range(args.order - 1)]
        for y, lower in states:
            for _, row, recipe in psd_rows(system.blocks, y):
                rows.add(row[None, :], None, recipe)
            for _, row, derivative, recipe in affine_psd_rows(affine, y, lower):
                rows.add(row[None, :], derivative[None, :], recipe)
            for _, row, recipe in cut_horn_rows(coupling, y):
                rows.add(row[None, :], None, recipe)
            for _, row, recipe in cut_scaled_horn_rows(coupling, y):
                rows.add(row[None, :], None, recipe)
            if args.triangle_pricing_seconds > 0:
                for _, row, recipe in cut_triangle_rows(
                    coupling, y, args.triangle_pricing_seconds
                ):
                    rows.add(row[None, :], None, recipe)
            for family in system.families:
                for row, derivative, recipe in family.price(y, lower, limit=120):
                    rows.add(row[None, :], derivative[None, :], recipe)
                for row, _derivative, recipe in family.switches(y, limit=120):
                    rows.add(row[None, :], None, recipe)
                for row, derivative, recipe in family.recursive(y, lower, limit=120):
                    rows.add(row[None, :], derivative[None, :], recipe)
                if args.minimal_support:
                    for anchor in range(family.k):
                        for mode in ('root', 'cross0', 'cross1'):
                            for row, derivative, recipe in family.price(
                                y, limit=40, proper_anchor=anchor, proper_mode=mode
                            ):
                                rows.add(row[None, :], derivative[None, :], recipe)
                            for row, derivative, recipe in family.recursive(
                                y, limit=40, proper_anchor=anchor, proper_mode=mode
                            ):
                                rows.add(row[None, :], derivative[None, :], recipe)
        if previous_count == len(rows.r):
            log(
                'No new priced direction; separation is incomplete, not certified feasible'
            )
            break
        previous_count = len(rows.r)
        if args.order == 6:
            # The coefficient matrices suffice during an LP. Rebuild profile
            # tuples for the next pricing round instead of retaining them.
            system.families = []
            system.tb = None
            family = None
            gc.collect()
        R, D = rows.matrices()
        low = R - DELTA * D
        M = R.shape[0]
        zero = sparse.csr_matrix((K, M))
        blocks = []
        for i in range(degree + 1):
            parts = []
            for j in range(degree):
                block = zero
                if j == i:
                    block = block + (degree - i) / degree * low.T
                if j + 1 == i:
                    block = block + i / degree * R.T
                parts.append(block)
            parts.append(
                sparse.csr_matrix(
                    np.full((K, 1), -DELTA if i == degree else 0),
                )
            )
            blocks.append(sparse.hstack(parts, format='csr'))
        A = sparse.vstack(blocks, format='csc')
        rhs = np.concatenate(
            [
                np.full(K, b + DELTA * i / degree if i < degree else b) - system.c
                for i in range(degree + 1)
            ]
        )
        baseline = np.zeros(degree * M + 1)
        for j in range(degree):
            baseline[j * M + cap] = rows.rec[cap][1]
        baseline[-1] = 1
        residual = float((A @ baseline - rhs).max())
        if residual > 1e-12 or not np.isfinite(A.data).all():
            raise RuntimeError(f'Explicit rho=1 baseline failed: {residual}')
        # This only removes numerical noise from the discovery LP. Returned
        # coefficients are evaluated on the unmodified rows before reporting.
        A.data[abs(A.data) < 1e-12] = 0
        A.eliminate_zeros()
        log(
            f'round {round_index}, degree {degree}: {A.shape}, {A.nnz} entries; '
            f'positive LP time limit {args.seconds}s'
        )
        with warnings.catch_warnings():
            warnings.filterwarnings(
                'ignore',
                category=OptimizeWarning,
                message='Unrecognized options detected',
            )
            result = linprog(
                np.r_[np.zeros(degree * M), 1],
                A_ub=A,
                b_ub=rhs,
                bounds=[(0, None)] * (degree * M) + [(0, 1)],
                method='highs-ipm',
                options={
                    'time_limit': args.seconds,
                    'threads': 1,
                    'parallel': False,
                    'run_crossover': 'off',
                    'small_matrix_value': 1e-12,
                    'ipm_optimality_tolerance': 1e-9,
                },
            )
        log(f'LP status {result.status}: {result.message}')
        if result.status != 0 or result.x is None:
            log('Bounded solve incomplete; no bound or obstruction inferred')
            break
        weights = np.maximum(result.x[:-1], 0).reshape(degree, M)
        rho = float(result.x[-1])
        maxima = []
        for i in range(degree + 1):
            coefficient = system.c.copy()
            if i < degree:
                coefficient += (degree - i) / degree * (low.T @ weights[i])
            if i > 0:
                coefficient += i / degree * (R.T @ weights[i - 1])
            maxima.append(float(coefficient.max()))
        log(f'Floating rho={rho:.12g}; Bernstein coefficient maxima {maxima}')
        save_candidate(
            args.save,
            rows,
            R,
            D,
            weights,
            rho,
            maxima,
            args.order,
            degree,
        )
        allowed = [b + DELTA * i / degree for i in range(degree)] + [b + rho * DELTA]
        if rho < 1 - 1e-6 and max(x - y for x, y in zip(maxima, allowed)) < 1e-8:
            log(
                'Possible full-target certificate in floating arithmetic. '
                'Exact row, multiplier, PSD and coefficient recovery is required.'
            )
            break
        marginal = np.maximum(-np.asarray(result.ineqlin.marginals), 0)
        marginal = marginal.reshape(degree + 1, K)
        states = []
        for j in range(degree):
            lower = (degree - j) / degree * marginal[j]
            y = lower + (j + 1) / degree * marginal[j + 1]
            mass = float(y.sum())
            if mass <= 1e-10 or not np.isfinite(mass):
                continue
            y = y / mass
            lower = lower / mass
            states.append((y, lower))
        if not states:
            log('No usable state for further separation')
            break
        del A, blocks, low, R, D, result
        gc.collect()


if __name__ == '__main__':
    main()

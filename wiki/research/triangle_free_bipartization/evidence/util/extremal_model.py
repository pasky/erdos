"""Discovery rows on five or six points for paired active maximum cuts.

All scalar rows are R(B)=R(B0)+(B-B0)D; equality rows may have either sign.
The base PSD blocks are B-independent; a separate function builds affine
hereditary blocks. At order six, scalar pricing retains selected canonical
root types, and canonical four-colour flags when there are no roots. This
is a specified subset of the full rooted family. Local cut pricing is
bounded, and absence of a priced violation is not a feasibility proof.
"""

from __future__ import annotations

import itertools
import warnings

import numpy as np
from scipy import sparse
from scipy.optimize import Bounds, LinearConstraint, milp
from util.paired_flags import Table, decode, encode, log, permute, representatives

B0 = 4 / 47
b = 0.08


def aggregate(
    tb: Table, flag: np.ndarray, nf: int, value: int | np.ndarray
) -> sparse.csr_matrix:
    """Average one scalar row per rooted flag, using bounded-size batches."""
    result = sparse.csr_matrix((nf, tb.count))
    for start in range(0, tb.tuples, 1000000):
        stop = min(start + 1000000, tb.tuples)
        values = (
            np.full(stop - start, value, dtype=float)
            if np.isscalar(value)
            else value[start:stop].astype(float)
        )
        piece = sparse.coo_matrix(
            (values, (flag[start:stop], tb.graph[start:stop])), shape=result.shape
        ).tocsr()
        result = result + piece
    return result / tb.orderings


def normalize_block(M: sparse.spmatrix, n: int) -> tuple[sparse.csr_matrix, int]:
    """Apply positive congruence and scalar scaling for numerical conditioning."""
    i, j = np.triu_indices(n)
    diag = np.asarray(abs(M[i == j]).max(axis=1).toarray()).ravel()
    d = 1 / np.sqrt(np.maximum(diag, 1e-10))
    M = sparse.diags(d[i] * d[j]) @ M
    scale = np.sqrt(float(M.multiply(M).sum()) / M.shape[0])
    if scale > 0:
        M = M / scale
    return M.tocsr(), n


def moment(
    tb: Table,
    roots: int,
    first: tuple[int, ...],
    second: tuple[int, ...],
    multiplier: np.ndarray | None = None,
) -> list[tuple[sparse.csr_matrix, int]]:
    """Build ordinary or localized rooted moment matrices."""
    a, ca = tb.flag(first, roots)
    bb, cb = tb.flag(second, roots)
    codes = np.unique(np.r_[ca, cb])
    dtype = np.int16 if len(codes) < 32768 else np.int32
    fa = np.searchsorted(codes, ca[a]).astype(dtype)
    fb = np.searchsorted(codes, cb[bb]).astype(dtype)
    del a, bb
    rt, rc = tb.flag(tuple(range(roots)), roots)
    chosen = set(representatives(roots))
    out = []
    ftype = np.full(len(codes), -1, np.int32)
    ftype[fa] = rt
    local = np.empty(len(codes), np.int32)
    for t, rootcode in enumerate(rc):
        if int(rootcode) not in chosen:
            continue
        mem = np.flatnonzero(ftype == t)
        n = len(mem)
        local[mem] = np.arange(n)
        ix = np.flatnonzero(rt == t)
        M = sparse.csr_matrix((n * (n + 1) // 2, tb.count))
        for start in range(0, len(ix), 1000000):
            sel = ix[start : start + 1000000]
            x = local[fa[sel]]
            y = local[fb[sel]]
            lo = np.minimum(x, y)
            hi = np.maximum(x, y)
            pos = lo * n - lo * (lo - 1) // 2 + hi - lo
            value = (
                np.ones(len(sel), np.int32)
                if multiplier is None
                else multiplier[sel].astype(float)
            )
            M = (
                M
                + sparse.coo_matrix(
                    (value, (pos, tb.graph[sel])), shape=M.shape
                ).tocsr()
            )
        i, j = np.triu_indices(n)
        M = sparse.diags(np.where(i == j, 1, 1 / np.sqrt(2)) / tb.orderings) @ M
        out.append(normalize_block(M, n))
    return out


class Family:
    """Selected rooted hereditary and stochastic switching rows."""

    def __init__(self, tb: Table, k: int) -> None:
        """Store the profile endpoints and selected rooted flag classes."""
        self.tb = tb
        self.k = k
        self.cells = 4 << k
        u, v = k, k + 1
        full_flag, full_codes = tb.flag(tuple(range(k)) + tuple(range(k + 2, tb.n)), k)
        if tb.n >= 6:
            if k:
                rt, rc = tb.flag(tuple(range(k)), k)
                take = np.isin(rc[rt], representatives(k))
            else:
                canonical = permute(full_codes, tb.n - 2).min(axis=1)
                take = (canonical == full_codes)[full_flag]
            ix = np.flatnonzero(take)
        else:
            ix = np.arange(tb.tuples)
        self.graph = tb.graph[ix]
        encoded = tb.codes[ix]
        self.cu = tb.colours[ix, u].copy()
        self.cv = tb.colours[ix, v].copy()
        for j in range(k):
            self.cu += (
                ((encoded >> tb.index[tuple(sorted((j, u)))]) & 1) << (j + 2)
            ).astype(np.uint8)
            self.cv += (
                ((encoded >> tb.index[tuple(sorted((j, v)))]) & 1) << (j + 2)
            ).astype(np.uint8)
        selected = full_codes[full_flag[ix]]
        self.codes, mapping = np.unique(selected, return_inverse=True)
        self.flag = mapping.astype(np.int32)
        self.nf = len(self.codes)
        self.root_cells = np.empty((self.nf, k), np.int16)
        for f, code in enumerate(self.codes):
            adjacency, colours = decode(int(code), tb.n - 2)
            for root in range(k):
                self.root_cells[f, root] = int(colours[root]) + 4 * sum(
                    int(adjacency[root, j]) << j for j in range(k)
                )
        edge = ((encoded >> tb.index[(u, v)]) & 1).astype(np.int8)
        same = (tb.colours[ix, u] & 1) == (tb.colours[ix, v] & 1)
        self.J = edge * np.where(same, -1, 1).astype(np.int8)
        self.C = (edge * ~same).astype(np.uint8)
        self.pair = (
            (self.flag.astype(np.int64) * self.cells + self.cu) * self.cells + self.cv
        ).astype(np.int32)
        self.order = np.argsort(self.flag, kind='stable').astype(np.int32)
        self.starts = np.searchsorted(self.flag[self.order], np.arange(self.nf + 1))
        log(
            f'paired profile family roots {k}: {self.nf} flags, '
            f'{self.cells} cells, {len(self.graph)} retained tuples'
        )

    def proper_exclusions(self, anchor: int, mode: str) -> np.ndarray:
        """Cells whose omission certifies a proper support in the declared model."""
        if not 0 <= anchor < self.k:
            raise ValueError('A proper-subset anchor must be one of the roots')
        if mode == 'root':
            excluded = np.zeros((self.nf, self.cells), bool)
            excluded[np.arange(self.nf), self.root_cells[:, anchor]] = True
            return excluded
        if mode not in {'cross0', 'cross1'}:
            raise ValueError('Unknown proper-support exclusion mode')
        bit = int(mode[-1])
        cells = np.arange(self.cells)[None, :]
        colours = self.root_cells[:, anchor, None] & 3
        adjacent = (cells & (4 << anchor)) != 0
        opposite = ((cells ^ colours) & (1 << bit)) != 0
        return adjacent & opposite

    def price(
        self,
        y: np.ndarray,
        lower: np.ndarray | None = None,
        limit: int = 200,
        fractional: bool = True,
        proper_anchor: int | None = None,
        proper_mode: str = 'root',
    ) -> list[tuple[np.ndarray, np.ndarray, tuple]]:
        """Price hereditary rows, optionally omitting a root of a minimal support.

        The proper-anchor option uses b only under the least-support
        counterexample hypothesis in the sketch. Its whole profile cell
        has selection zero, so at least that positive-weight support
        vertex is absent, even for fractional selections elsewhere.
        """
        m = self.cells
        nf = self.nf
        bound = B0 if proper_anchor is None else b
        excluded = (
            None if proper_anchor is None
            else self.proper_exclusions(proper_anchor, proper_mode)
        )
        w = y[self.graph] / self.tb.orderings
        Q = np.bincount(
            self.pair, weights=w * (bound - self.C), minlength=nf * m * m
        ).reshape(nf, m, m)
        if lower is not None and proper_anchor is None:
            Q -= np.bincount(
                self.pair,
                weights=(B0 - b) * lower[self.graph] / self.tb.orderings,
                minlength=nf * m * m,
            ).reshape(nf, m, m)
        Q = (Q + Q.transpose(0, 2, 1)) / 2
        L = np.bincount(
            self.flag * m + self.cu, weights=0.5 * w * self.J, minlength=nf * m
        ).reshape(nf, m)
        L += np.bincount(
            self.flag * m + self.cv, weights=0.5 * w * self.J, minlength=nf * m
        ).reshape(nf, m)
        diag = np.diagonal(Q, axis1=1, axis2=2)
        best = np.zeros(nf)
        bestS = np.zeros((nf, m))
        rng = np.random.default_rng(100 + self.k)
        for attempt in range(20):
            S = rng.integers(0, 2, (nf, m)).astype(float)
            if attempt == 0:
                S[:] = 1
            if excluded is not None:
                S[excluded] = 0
            for _ in range(3 * m):
                grad = L + 2 * np.einsum('fij,fj->fi', Q, S, optimize=True)
                opt = np.where(grad + diag * (1 - 2 * S) >= 0, 0.0, 1.0)
                good = diag > 1e-15
                if fractional:
                    opt[good] = np.clip(S[good] - grad[good] / (2 * diag[good]), 0, 1)
                if excluded is not None:
                    opt[excluded] = 0
                change = opt - S
                cost = grad * change + diag * change**2
                a = cost.argmin(axis=1)
                take = cost[np.arange(nf), a] < -1e-13
                if not take.any():
                    break
                use = np.flatnonzero(take)
                S[use, a[use]] = opt[use, a[use]]
            vals = np.einsum('fi,fi->f', S, L) + np.einsum(
                'fi,fij,fj->f', S, Q, S, optimize=True
            )
            good = vals < best
            best[good] = vals[good]
            bestS[good] = S[good]
        out = []
        for f in np.argsort(best)[:limit]:
            if best[f] >= -1e-11:
                continue
            s = bestS[f]
            ix = self.order[self.starts[f] : self.starts[f + 1]]
            x = s[self.cu[ix]]
            z = s[self.cv[ix]]
            value = 0.5 * self.J[ix] * (x + z) + (bound - self.C[ix]) * x * z
            row = (
                np.bincount(self.graph[ix], weights=value, minlength=self.tb.count)
                / self.tb.orderings
            )
            der = (
                np.bincount(self.graph[ix], weights=x * z, minlength=self.tb.count)
                / self.tb.orderings
            )
            if proper_anchor is not None:
                der[:] = 0
            recipe = ('hereditary', self.k, int(self.codes[f]), s.tolist())
            if proper_anchor is not None:
                recipe = (
                    'proper_hereditary', proper_anchor, proper_mode, *recipe[1:]
                )
            out.append(
                (row, der, recipe)
            )
        log(
            f'paired fractional hereditary roots {self.k}, '
            f'proper anchor {proper_anchor}/{proper_mode}, '
            f'least {best.min():.6g}, added {len(out)}'
        )
        return out

    def switches(
        self, y: np.ndarray, limit: int = 200
    ) -> list[tuple[np.ndarray, None, tuple]]:
        """Locally search stochastic profile switchings at a floating state."""
        m = self.cells
        nf = self.nf
        Q = np.bincount(
            self.pair,
            weights=y[self.graph] * self.J / self.tb.orderings,
            minlength=nf * m * m,
        ).reshape(nf, m, m)
        Q += Q.transpose(0, 2, 1).copy()
        diag = np.diagonal(Q, axis1=1, axis2=2)
        L = Q.sum(axis=2)
        best = np.zeros(nf)
        bestS = np.zeros((nf, m))
        rng = np.random.default_rng(600 + self.k)
        for attempt in range(16):
            S = rng.integers(0, 2, (nf, m)).astype(float)
            if attempt == 0:
                S[:] = (np.arange(m) & 1) ^ ((np.arange(m) >> 1) & 1)
            for _ in range(3 * m):
                grad = L - 2 * np.einsum('fij,fj->fi', Q, S, optimize=True)
                curv = -diag
                opt = np.where(grad + curv * (1 - 2 * S) >= 0, 0.0, 1.0)
                good = curv > 1e-15
                opt[good] = np.clip(S[good] - grad[good] / (2 * curv[good]), 0, 1)
                change = opt - S
                cost = grad * change + curv * change**2
                a = cost.argmin(axis=1)
                take = cost[np.arange(nf), a] < -1e-13
                if not take.any():
                    break
                use = np.flatnonzero(take)
                S[use, a[use]] = opt[use, a[use]]
            vals = np.einsum('fi,fi->f', S, L) - np.einsum(
                'fi,fij,fj->f', S, Q, S, optimize=True
            )
            good = vals < best
            best[good] = vals[good]
            bestS[good] = S[good]
        out = []
        for f in np.argsort(best)[:limit]:
            if best[f] >= -1e-11:
                continue
            s = bestS[f]
            ix = self.order[self.starts[f] : self.starts[f + 1]]
            x = s[self.cu[ix]]
            z = s[self.cv[ix]]
            val = self.J[ix] * (x + z - 2 * x * z)
            row = (
                np.bincount(self.graph[ix], weights=val, minlength=self.tb.count)
                / self.tb.orderings
            )
            out.append(
                (
                    row,
                    None,
                    ('fractional_switch', self.k, int(self.codes[f]), s.tolist()),
                )
            )
        log(
            f'paired stochastic switching roots {self.k}, '
            f'least {best.min():.6g}, added {len(out)}'
        )
        return out

    def recursive(
        self,
        y: np.ndarray,
        lower: np.ndarray | None = None,
        limit: int = 200,
        proper_anchor: int | None = None,
        proper_mode: str = 'root',
    ) -> list[tuple[np.ndarray, np.ndarray, tuple]]:
        """Price cuts with a fixed outside colouring and an optimally recut remainder.

        Each profile cell is fixed on side zero, fixed on side one, or left
        in one recursive part. The latter uses m(G[U]) <= B |U|^2 and a
        random global orientation. Every returned assignment is valid; the
        coordinate search is not exhaustive.
        """
        m = self.cells
        nf = self.nf
        bound = B0 if proper_anchor is None else b
        excluded = (
            None if proper_anchor is None
            else self.proper_exclusions(proper_anchor, proper_mode)
        )
        w = y[self.graph] / self.tb.orderings
        edge = abs(self.J)
        mass = np.bincount(self.pair, weights=w, minlength=nf * m * m).reshape(nf, m, m)
        adj = np.bincount(self.pair, weights=w * edge, minlength=nf * m * m).reshape(
            nf, m, m
        )
        mass = (mass + mass.transpose(0, 2, 1)) / 2
        adj = (adj + adj.transpose(0, 2, 1)) / 2
        Qz = adj / 2
        Qu = bound * mass - Qz
        if lower is not None and proper_anchor is None:
            low = np.bincount(
                self.pair,
                weights=lower[self.graph] / self.tb.orderings,
                minlength=nf * m * m,
            ).reshape(nf, m, m)
            Qu -= (B0 - b) * (low + low.transpose(0, 2, 1)) / 2
        constant = np.bincount(self.flag, weights=0.5 * w * self.J, minlength=nf)
        dz = np.diagonal(Qz, axis1=1, axis2=2)
        du = np.diagonal(Qu, axis1=1, axis2=2)
        best = np.zeros(nf)
        bestside = np.zeros((nf, m), np.int8)
        rng = np.random.default_rng(1100 + self.k)
        for attempt in range(24):
            side = rng.integers(-1, 2, (nf, m), dtype=np.int8)
            if attempt == 0:
                side[:] = 0
            if attempt == 1:
                side[:] = 2 * (np.arange(m) & 1) - 1
            if attempt == 2:
                side[:] = 2 * ((np.arange(m) >> 1) & 1) - 1
            if excluded is not None:
                side[excluded] = 1
            for _ in range(3 * m):
                z = side.astype(float)
                u = (side == 0).astype(float)
                lz = 2 * (np.einsum('fij,fj->fi', Qz, z, optimize=True) - dz * z)
                lu = 2 * (np.einsum('fij,fj->fi', Qu, u, optimize=True) - du * u)
                choices = np.stack((dz - lz, du + lu, dz + lz), axis=2)
                if excluded is not None:
                    choices[:, :, 1][excluded] = np.inf
                choice = choices.argmin(axis=2)
                current = dz * z * z + lz * z + du * u + lu * u
                change = choices.min(axis=2) - current
                a = change.argmin(axis=1)
                use = np.flatnonzero(change[np.arange(nf), a] < -1e-13)
                if not len(use):
                    break
                side[use, a[use]] = choice[use, a[use]] - 1
            z = side.astype(float)
            u = (side == 0).astype(float)
            values = (
                constant
                + np.einsum('fi,fij,fj->f', z, Qz, z, optimize=True)
                + np.einsum('fi,fij,fj->f', u, Qu, u, optimize=True)
            )
            take = values < best
            best[take] = values[take]
            bestside[take] = side[take]
        out = []
        for f in np.argsort(best)[:limit]:
            if best[f] >= -1e-11:
                continue
            side = bestside[f]
            ix = self.order[self.starts[f] : self.starts[f + 1]]
            zx = side[self.cu[ix]].astype(float)
            zy = side[self.cv[ix]].astype(float)
            uu = ((zx == 0) & (zy == 0)).astype(float)
            value = (
                0.5 * self.J[ix] + 0.5 * edge[ix] * zx * zy
                + (bound - 0.5 * edge[ix]) * uu
            )
            row = (
                np.bincount(self.graph[ix], weights=value, minlength=self.tb.count)
                / self.tb.orderings
            )
            derivative = (
                np.bincount(self.graph[ix], weights=uu, minlength=self.tb.count)
                / self.tb.orderings
            )
            if proper_anchor is not None:
                derivative[:] = 0
            recipe = ('recursive_cut', self.k, int(self.codes[f]), side.tolist())
            if proper_anchor is not None:
                recipe = (
                    'proper_recursive_cut', proper_anchor, proper_mode, *recipe[1:]
                )
            out.append(
                (
                    row,
                    derivative,
                    recipe,
                )
            )
        log(
            f'paired recursive cuts roots {self.k}, '
            f'proper anchor {proper_anchor}/{proper_mode}, '
            f'least {best.min():.6g}, added {len(out)}'
        )
        return out


class System:
    """The declared paired-cut relaxation on five or six sampled vertices."""

    def __init__(self, order: int = 5) -> None:
        """Build base equalities, scalar rows, and B-independent PSD blocks."""
        if order not in (5, 6):
            raise ValueError('The model supports order five or six')
        self.tb = tb = Table(order)
        self.rows = []
        self.derivatives = []
        self.recipes = []
        self.equalities = []
        self.eqder = []
        self.c = tb.row(tb.adj(0, 1) * tb.same(0, 1))
        self.p = tb.row(tb.adj(0, 1))

        def addmat(
            R: sparse.csr_matrix,
            D: sparse.csr_matrix | None,
            label: str,
            equality: bool = False,
        ) -> None:
            """Store rows and both signs of an asserted equality."""
            for i in range(R.shape[0]):
                r = R.getrow(i)
                d = None if D is None else D.getrow(i)
                self.rows.append(r)
                self.derivatives.append(d)
                self.recipes.append((label, i))
                if equality:
                    self.equalities.append(r)
                    self.eqder.append(d)
                    self.rows.append(-r)
                    self.derivatives.append(-d)
                    self.recipes.append((label + '_negative', i))

        flag, codes = tb.flag((0, *range(2, order)), 1)
        nf = len(codes)
        F = aggregate(tb, flag, nf, 1)
        J = tb.adj(0, 1) * np.where(tb.same(0, 1), -1, 1)
        addmat(aggregate(tb, flag, nf, J), None, 'vertex')
        addmat(aggregate(tb, flag, nf, tb.adj(0, 1)) - 2 * B0 * F, -2 * F, 'degree')
        flag, codes = tb.flag((0, *range(2, order)), 1, 'second')
        nf = len(codes)
        F = aggregate(tb, flag, nf, 1)
        L = aggregate(tb, flag, nf, tb.adj(0, 1) * tb.same(0, 1))
        addmat(L - B0 * F, -F, 'balanced_other_cut', True)
        flag, codes = tb.flag(tuple(range(2, order)), 0)
        nf = len(codes)
        F = aggregate(tb, flag, nf, 1)
        L = aggregate(tb, flag, nf, tb.adj(0, 1) * tb.same(0, 1))
        addmat(L - B0 * F, -F, 'm_equals_B', True)
        self.band_start = len(self.rows)
        edge = aggregate(tb, flag, nf, tb.adj(0, 1))
        addmat(edge - (1243 / 5000) * F, None, 'band_lower')
        addmat((3197 / 10000) * F - edge, None, 'band_upper')
        self.blocks = []
        for k in range(order - 1):
            m = (order + k) // 2
            first = tuple(range(m))
            second = tuple(range(k)) + tuple(range(m, 2 * m - k))
            self.blocks.extend(moment(tb, k, first, second))
        self.ordinary_count = len(self.blocks)
        self.blocks.extend(moment(tb, 1, (0, 2), (0, 3), J))
        self.blocks.extend(moment(tb, 1, (0, 1), (0, 2), tb.adj(3, 4) - 1243 / 5000))
        self.blocks.extend(moment(tb, 1, (0, 1), (0, 2), 3197 / 10000 - tb.adj(3, 4)))
        self.families = [Family(tb, k) for k in range(order - 1)]
        if order == 6:
            # These one-root blocks use five points, so exact deletion
            # projection avoids expanding their extra dummy point.
            small = System(5)
            lookup = np.full(1 << 20, -1, np.int16)
            lookup[small.tb.codes] = small.tb.graph
            rr = []
            cc = []
            for h, code in enumerate(tb.reps):
                adj, col = decode(int(code), 6)
                for deleted in range(6):
                    ix = [i for i in range(6) if i != deleted]
                    mapped = int(lookup[encode(adj[np.ix_(ix, ix)], col[ix])])
                    if mapped < 0:
                        raise RuntimeError('five-point projection missing')
                    rr.append(mapped)
                    cc.append(h)
            P = sparse.coo_matrix(
                (np.full(len(rr), 1 / 6), (rr, cc)), shape=(small.tb.count, tb.count)
            ).tocsr()
            if max(abs(np.asarray(P.T @ small.c).ravel() - self.c)) > 1e-13:
                raise RuntimeError('paired projection objective mismatch')
            self.blocks.extend(
                (M @ P, n) for M, n in small.blocks[small.ordinary_count + 3 :]
            )
            del small, lookup, P
        else:
            # All one-root gain-weighted profile squares for deterministic switches.
            root = tb.colours[:, 0] == 0
            cells = np.array(
                [tb.colours[:, i] + 4 * tb.adj(0, i) for i in (1, 2, 3, 4)]
            )
            signed = tb.adj(1, 2) * np.where(tb.same(1, 2), -1, 1)
            n = 8
            i, j = np.triu_indices(n)
            for mask in range(1, 128):
                side = (mask >> np.arange(8)) & 1
                take = np.flatnonzero(
                    root & (signed != 0) & (side[cells[0]] != side[cells[1]])
                )
                if len(take) == 0:
                    continue
                lo = np.minimum(cells[2, take], cells[3, take]).astype(np.int64)
                hi = np.maximum(cells[2, take], cells[3, take]).astype(np.int64)
                pos = lo * n - lo * (lo - 1) // 2 + hi - lo
                M = sparse.coo_matrix(
                    (signed[take].astype(float), (pos, tb.graph[take])),
                    shape=(n * (n + 1) // 2, tb.count),
                ).tocsr()
                M = sparse.diags(np.where(i == j, 1, 1 / np.sqrt(2)) / tb.orderings) @ M
                self.blocks.append(normalize_block(M, n))
        log(
            f'paired system: {len(self.rows)} scalar rows, '
            f'{len(self.blocks)} PSD blocks, {len(self.equalities)} equalities'
        )


def affine_hereditary_blocks(
    system: System,
) -> list[tuple[sparse.csr_matrix, sparse.csr_matrix, int, int]]:
    """All Boolean one-root hereditary gain-square blocks, affine in B."""
    tb = system.tb
    n = 8
    i, j = np.triu_indices(n)
    root = tb.colours[:, 0] == 0
    take = np.flatnonzero(root)
    cells = np.array(
        [tb.colours[take, k] + 4 * tb.adj(0, k)[take] for k in (1, 2, 3, 4)]
    )
    signed = tb.adj(1, 2)[take] * np.where(tb.same(1, 2)[take], -1, 1)
    cross = tb.adj(1, 2)[take] * ~tb.same(1, 2)[take]
    lo = np.minimum(cells[2], cells[3]).astype(np.int64)
    hi = np.maximum(cells[2], cells[3]).astype(np.int64)
    pos = lo * n - lo * (lo - 1) // 2 + hi - lo
    svec = sparse.diags(np.where(i == j, 1, 1 / np.sqrt(2)) / tb.orderings)
    out = []
    for mask in range(1, 256):
        side = (mask >> np.arange(8)) & 1
        x = side[cells[0]]
        z = side[cells[1]]
        value = 0.5 * signed * (x + z) + (B0 - cross) * x * z
        M = (
            svec
            @ sparse.coo_matrix(
                (value, (pos, tb.graph[take])), shape=(n * (n + 1) // 2, tb.count)
            ).tocsr()
        )
        D = (
            svec
            @ sparse.coo_matrix((x * z, (pos, tb.graph[take])), shape=M.shape).tocsr()
        )
        low = M - (B0 - b) * D
        diag = np.maximum(
            np.asarray(abs(M[i == j]).max(axis=1).toarray()).ravel(),
            np.asarray(abs(low[i == j]).max(axis=1).toarray()).ravel(),
        )
        d = 1 / np.sqrt(np.maximum(diag, 1e-10))
        T = sparse.diags(d[i] * d[j])
        M = T @ M
        D = T @ D
        scale = max(
            np.sqrt(float(M.multiply(M).sum()) / M.shape[0]),
            np.sqrt(
                float((M - (B0 - b) * D).multiply(M - (B0 - b) * D).sum()) / M.shape[0]
            ),
        )
        if scale > 1e-15:
            out.append((M / scale, D / scale, n, mask))
    log(f'paired affine hereditary-square blocks {len(out)}')
    return out


def cut_pattern_blocks(
    system: System,
) -> list[tuple[sparse.csr_matrix, int, int, float]]:
    """PSD of joint patterns of independent cuts at the same sample vertices.

    Conditional on a vertex tuple, the two normalized colour patterns are
    independent with a common probability vector q. Every block is therefore
    an average of q q^T with a nonnegative uncoloured type indicator.
    This positivity samples cuts, unlike the ordinary vertex-flag matrices.
    """
    tb = system.tb
    order = tb.n
    edges = order * (order - 1) // 2
    graph = tb.codes & ((1 << edges) - 1)
    codes = np.unique(graph)
    canonical = permute(codes, order, colour_group=False).min(axis=1)
    selected_codes = codes[codes == canonical]
    out = []
    n = 1 << (order - 1)
    # Complement-equivalent patterns are merged; the underlying active-cut
    # distribution was independently symmetrized by global complementation.
    first = np.zeros(tb.tuples, np.uint16)
    second = np.zeros(tb.tuples, np.uint16)
    for i in range(order):
        first |= (tb.colours[:, i].astype(np.uint16) & 1) << i
        second |= (tb.colours[:, i].astype(np.uint16) >> 1) << i
    np.minimum(first, ((1 << order) - 1) ^ first, out=first)
    np.minimum(second, ((1 << order) - 1) ^ second, out=second)
    i, j = np.triu_indices(n)
    diag = sparse.diags(np.where(i == j, 1, 1 / np.sqrt(2)) / tb.orderings)
    for code in selected_codes:
        ix = np.flatnonzero(graph == code)
        M = sparse.csr_matrix((n * (n + 1) // 2, tb.count))
        for start in range(0, len(ix), 1000000):
            take = ix[start : start + 1000000]
            lo = np.minimum(first[take], second[take]).astype(np.int32)
            hi = np.maximum(first[take], second[take]).astype(np.int32)
            pos = lo * n - lo * (lo - 1) // 2 + hi - lo
            M = (
                M
                + sparse.coo_matrix(
                    (np.ones(len(take), np.int32), (pos, tb.graph[take])), shape=M.shape
                ).tocsr()
            )
        M = diag @ M
        # Retain one common scalar scale, so basis entries still correspond
        # directly to q coordinates for optional copositive pricing.
        scale = float(abs(M).max())
        if scale > 0:
            out.append((M / scale, n, int(code), scale))
    log(f'cut-pattern independence blocks: {len(out)}, dimension {n}')
    return out


def cut_horn_rows(
    blocks: list[tuple[sparse.csr_matrix, int, int, float]],
    y: np.ndarray,
    limit: int = 100,
    starts: int = 48,
) -> list[tuple[float, np.ndarray, tuple]]:
    """Price grouped five-cycle Horn rows by local partition search.

    H=J-2 A(C5-blow-up) is copositive by the weighted triangle-free
    edge bound. Each returned grouping proves its own validity; the local
    search is not an exhaustive lower bound over all copositive matrices.
    """
    out = []
    rng = np.random.default_rng(25017)
    for bi, (M, n, code, scale0) in enumerate(blocks):
        i, j = np.triu_indices(n)
        factor = np.where(i == j, 1, np.sqrt(2))
        matrix = np.zeros((n, n))
        matrix[i, j] = (M @ y) / factor
        matrix[j, i] = matrix[i, j]
        best = 0.0
        bestside = None
        for _attempt in range(starts):
            side = rng.integers(0, 5, n)
            for _ in range(4 * n):
                mass = np.zeros((n, 5))
                for c in range(5):
                    mass[:, c] = matrix[
                        :, (side == (c + 1) % 5) | (side == (c - 1) % 5)
                    ].sum(axis=1)
                # Remove the diagonal if moving a vertex would turn its own
                # old group into a neighbouring group; self loops never count.
                for c in range(5):
                    mass[:, c] -= np.diag(matrix) * (
                        ((side - c) % 5 == 1) | ((side - c) % 5 == 4)
                    )
                delta = mass - mass[np.arange(n), side][:, None]
                a, c = np.unravel_index(delta.argmax(), delta.shape)
                if delta[a, c] <= 1e-13:
                    break
                side[a] = c
            adjacent = ((side[:, None] - side[None, :]) % 5 == 1) | (
                (side[:, None] - side[None, :]) % 5 == 4
            )
            H = 1 - 2 * adjacent.astype(np.int8)
            value = float((H * matrix).sum())
            if value < best:
                best = value
                bestside = side.copy()
        if bestside is not None and best < -1e-10:
            adjacent = ((bestside[i] - bestside[j]) % 5 == 1) | (
                (bestside[i] - bestside[j]) % 5 == 4
            )
            weights = (1 - 2 * adjacent.astype(np.int8)) * factor
            row = np.asarray(M.T @ weights).ravel()
            scale = float(abs(row).max())
            if scale > 0:
                out.append(
                    (
                        best / scale,
                        row / scale,
                        ('cut_horn', bi, int(code), bestside.tolist(), scale, scale0),
                    )
                )
    out.sort(key=lambda x: x[0])
    log(
        f'cut-pattern grouped Horn rows: {len(out)} violations, '
        f'least {out[0][0] if out else 0}'
    )
    return out[:limit]


def cut_triangle_rows(
    blocks: list[tuple[sparse.csr_matrix, int, int, float]],
    y: np.ndarray,
    seconds: float = 2,
) -> list[tuple[float, np.ndarray, tuple]]:
    """Price J-2A rows with a bounded search over triangle-free pattern graphs.

    Every returned integer graph is checked directly for triangles. Weighted
    Mantel proves its copositivity, regardless of solver status or optimality.
    A missing incumbent or a nonnegative row gives no pricing certificate.
    """
    if not np.isfinite(seconds) or seconds <= 0:
        raise ValueError('The pricing time limit must be finite and positive')
    out = []
    for bi, (M, n, code, scale0) in enumerate(blocks):
        i, j = np.triu_indices(n)
        factor = np.where(i == j, 1, np.sqrt(2))
        matrix = np.zeros((n, n))
        matrix[i, j] = (M @ y) / factor
        matrix[j, i] = matrix[i, j]
        pi, pj = np.triu_indices(n, 1)
        count = len(pi)
        lookup = np.zeros((n, n), np.int64)
        lookup[pi, pj] = np.arange(count)
        triples = np.array(list(itertools.combinations(range(n), 3)), np.int64)
        positions = lookup[triples[:, (0, 0, 1)], triples[:, (1, 2, 2)]].ravel()
        constraints = sparse.coo_matrix(
            (
                np.ones(len(positions)),
                (np.repeat(np.arange(len(triples)), 3), positions),
            ),
            shape=(len(triples), count),
        ).tocsc()
        with warnings.catch_warnings():
            warnings.filterwarnings('ignore', message='Unrecognized options detected')
            result = milp(
                -matrix[pi, pj],
                integrality=np.ones(count),
                bounds=Bounds(0, 1),
                constraints=LinearConstraint(constraints, -np.inf, 2),
                options={'time_limit': seconds, 'threads': 1, 'parallel': False},
            )
        if result.x is None:
            log(
                f'cut-pattern triangle pricing block {bi}: status {result.status}, no incumbent'
            )
            continue
        selected = result.x > 0.5
        adj = np.zeros((n, n), np.int64)
        adj[pi, pj] = adj[pj, pi] = selected
        if np.any((adj @ adj) * adj):
            log(f'cut-pattern triangle pricing block {bi}: rounded incumbent rejected')
            continue
        H = 1 - 2 * adj
        value = float((H * matrix).sum())
        if value < -1e-10:
            row = np.asarray(M.T @ (H[i, j] * factor)).ravel()
            scale = float(abs(row).max())
            if scale > 0:
                edges = np.stack((pi[selected], pj[selected]), axis=1).tolist()
                out.append(
                    (
                        value / scale,
                        row / scale,
                        ('cut_triangle', bi, int(code), n, edges, scale, scale0),
                    )
                )
    out.sort(key=lambda x: x[0])
    log(
        f'cut-pattern triangle rows: {len(out)} violations, '
        f'least {out[0][0] if out else 0}; pricing incomplete'
    )
    return out


def cut_scaled_horn_rows(
    blocks: list[tuple[sparse.csr_matrix, int, int, float]],
    y: np.ndarray,
    starts: int = 24,
) -> list[tuple[float, np.ndarray, tuple]]:
    """Price nonnegative diagonal congruences of grouped five-cycle Horn rows.

    Every proposed vector is nonnegative, so weighted Mantel proves each
    returned row independently of the local grouping and vector searches.
    Neither search is exhaustive over the declared copositive family.
    """
    out = []
    rng = np.random.default_rng(25018)
    for bi, (M, n, code, scale0) in enumerate(blocks):
        i, j = np.triu_indices(n)
        factor = np.where(i == j, 1, np.sqrt(2))
        matrix = np.zeros((n, n))
        matrix[i, j] = (M @ y) / factor
        matrix[j, i] = matrix[i, j]
        best = 0.0
        witness = None
        for _attempt in range(starts):
            side = rng.integers(0, 5, n)
            a = np.ones(n) / np.sqrt(n)
            for _outer in range(3):
                weighted = matrix * a[:, None] * a[None, :]
                for _ in range(4 * n):
                    mass = np.zeros((n, 5))
                    for c in range(5):
                        mass[:, c] = weighted[
                            :, (side == (c + 1) % 5) | (side == (c - 1) % 5)
                        ].sum(axis=1)
                        mass[:, c] -= np.diag(weighted) * (
                            ((side - c) % 5 == 1) | ((side - c) % 5 == 4)
                        )
                    change = mass - mass[np.arange(n), side][:, None]
                    v, c = np.unravel_index(change.argmax(), change.shape)
                    if change[v, c] <= 1e-14:
                        break
                    side[v] = c
                adjacent = ((side[:, None] - side[None, :]) % 5 == 1) | (
                    (side[:, None] - side[None, :]) % 5 == 4
                )
                H = 1 - 2 * adjacent.astype(np.int8)
                Q = H * matrix
                eig, vectors = np.linalg.eigh(Q)
                if eig[0] >= -1e-12:
                    break
                shift = max(float(eig[-1]), 1e-12)
                P = shift * np.eye(n) - Q
                candidates = [
                    a,
                    np.maximum(vectors[:, 0], 0),
                    np.maximum(-vectors[:, 0], 0),
                ]
                for initial in candidates:
                    v = initial.copy()
                    if np.linalg.norm(v) == 0:
                        continue
                    v /= np.linalg.norm(v)
                    for _ in range(60):
                        next_v = np.maximum(P @ v, 0)
                        norm = np.linalg.norm(next_v)
                        if norm == 0:
                            break
                        v = next_v / norm
                    if float(v @ Q @ v) < float(a @ Q @ a):
                        a = v
                value = float(a @ Q @ a)
                if value < best:
                    best = value
                    witness = side.copy(), a.copy()
        if witness is not None and best < -1e-10:
            side, a = witness
            adjacent = ((side[i] - side[j]) % 5 == 1) | ((side[i] - side[j]) % 5 == 4)
            weights = (1 - 2 * adjacent.astype(np.int8)) * a[i] * a[j] * factor
            row = np.asarray(M.T @ weights).ravel()
            scale = float(abs(row).max())
            if scale > 0:
                out.append(
                    (
                        best / scale,
                        row / scale,
                        (
                            'cut_horn_scaled',
                            bi,
                            int(code),
                            side.tolist(),
                            a.tolist(),
                            scale,
                            scale0,
                        ),
                    )
                )
    out.sort(key=lambda x: x[0])
    log(
        f'cut-pattern scaled Horn rows: {len(out)} violations, least {out[0][0] if out else 0}'
    )
    return out

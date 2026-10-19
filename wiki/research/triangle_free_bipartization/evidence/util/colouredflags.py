"""Order-six flag relaxation of a triangle-free graphon coloured by a maximum cut.

A state is the distribution of the vertex-2-coloured triangle-free graph
induced by six independent uniform points of a step graphon W_G whose parts
are coloured by a maximum cut of G. Every functional below is the average,
over all 720 orderings of a sampled six-set, of a function of the ordered
tuple; on a state it equals the expectation over six independent points.

- objective: the monochromatic edge density, 2 D_2(G) / N^2 on W_G;
- band rows: p - a, b - p, (p - a)(b - p), and their products with flags;
- vertex rows: sigma(x) F(x) for every one-rooted flag F on four further
  points, where sigma(x) is the density of opposite-coloured minus
  same-coloured neighbours of x; sigma >= 0 at every point of an optimal cut;
- switching rows: for k roots (k = 1, ..., 4), a cell of a point is its colour
  and its adjacencies to the roots; flipping the colours of every point whose
  cell lies in a set S changes the monochromatic density by Delta_S(roots) >= 0
  at an optimal cut. Rows are Delta_S times a k-rooted flag on the remaining
  points; they enter by pricing, exhaustive over S for k <= 3 and by local
  search for k = 4;
- optional products: sigma of the first root times switching rows on one to
  three roots, and sigma(r1) sigma(r2) times two-rooted flags;
- positive semidefinite blocks: flag moment matrices for root types of sizes
  0 to 3 (4 optional), and localizing blocks weighted by sigma, p - a, b - p.

All arithmetic is floating point. Nothing computed here is a proof.
"""

from __future__ import annotations

import itertools
import time
import warnings
from functools import cache

import numpy as np

ORDER = 6


def pairs(n: int) -> list[tuple[int, int]]:
    """Pairs i < j of n positions in lexicographic order."""
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


@cache
def destinations(n: int) -> np.ndarray:
    """For every permutation of n points, the destination of every code bit.

    Bit k < C(n, 2) of a code is the k-th pair; bit C(n, 2) + i is the colour
    of point i.
    """
    index = {p: k for k, p in enumerate(pairs(n))}
    perms = list(itertools.permutations(range(n)))
    edges = len(index)
    dest = np.zeros((len(perms), edges + n), dtype=np.int64)
    for a, pi in enumerate(perms):
        for k, (i, j) in enumerate(pairs(n)):
            u, v = sorted((pi[i], pi[j]))
            dest[a, k] = index[(u, v)]
        for i in range(n):
            dest[a, edges + i] = edges + pi[i]
    return dest


def permuted_codes(codes: np.ndarray, n: int) -> np.ndarray:
    """Codes of every relabelling: shape (len(codes), n!)."""
    dest = destinations(n)
    codes = np.asarray(codes, dtype=np.int64)
    out = np.zeros((len(codes), dest.shape[0]), dtype=np.int64)
    weights = np.int64(1) << dest
    for b in range(dest.shape[1]):
        out += ((codes[:, None] >> b) & 1) * weights[None, :, b]
    return out


def decode(code: int, n: int) -> tuple[np.ndarray, np.ndarray]:
    """Adjacency matrix and colour vector of a code."""
    adj = np.zeros((n, n), dtype=np.int64)
    for k, (i, j) in enumerate(pairs(n)):
        if code >> k & 1:
            adj[i, j] = adj[j, i] = 1
    edges = n * (n - 1) // 2
    colours = np.array([(code >> (edges + i)) & 1 for i in range(n)], dtype=np.int64)
    return adj, colours


def encode(adj: np.ndarray, colours: np.ndarray) -> int:
    """Code of a coloured graph."""
    n = len(colours)
    code = 0
    for k, (i, j) in enumerate(pairs(n)):
        if adj[i, j]:
            code |= 1 << k
    edges = n * (n - 1) // 2
    for i in range(n):
        if colours[i]:
            code |= 1 << (edges + i)
    return code


def coloured_graphs(order: int) -> list[int]:
    """Canonical codes of the vertex-2-coloured triangle-free graphs of an order.

    Each graph on n + 1 points extends one on n points by a point whose
    neighbourhood is an independent set; the canonical code is the least
    code over all relabellings.
    """
    reps = [0, 1]
    for n in range(1, order):
        candidates = set()
        for code in reps:
            adj, colours = decode(code, n)
            for mask in range(1 << n):
                nbrs = [i for i in range(n) if mask >> i & 1]
                if any(adj[u, v] for u, v in itertools.combinations(nbrs, 2)):
                    continue
                for colour in (0, 1):
                    new = np.zeros((n + 1, n + 1), dtype=np.int64)
                    new[:n, :n] = adj
                    new[nbrs, n] = new[n, nbrs] = 1
                    candidates.add(encode(new, np.append(colours, colour)))
        cand = np.array(sorted(candidates), dtype=np.int64)
        out = set()
        for s in range(0, len(cand), 2000):
            out.update(permuted_codes(cand[s:s + 2000], n + 1).min(axis=1).tolist())
        reps = sorted(out)
    return reps


class Table:
    """Every ordering of every coloured triangle-free graph of order six."""

    def __init__(self) -> None:
        """Enumerate the finite sample space and all its orderings."""
        self.reps = coloured_graphs(ORDER)
        perm = permuted_codes(np.array(self.reps, dtype=np.int64), ORDER)
        self.count, self.orderings = perm.shape
        codes = perm.reshape(-1)
        self.index = {p: k for k, p in enumerate(pairs(ORDER))}
        edges = len(self.index)
        self.edge_bits = ((codes[:, None] >> np.arange(edges)[None, :]) & 1).astype(np.uint8)
        self.colours = ((codes[:, None] >> (edges + np.arange(ORDER))[None, :]) & 1).astype(np.uint8)
        self.graph = np.repeat(np.arange(self.count), self.orderings)
        self.tuples = len(self.graph)
        self.lookup = -np.ones(1 << (edges + ORDER), dtype=np.int64)
        self.lookup[perm] = np.arange(self.count)[:, None]

    def adj(self, i: int, j: int) -> np.ndarray:
        """Adjacency of positions i and j in every tuple."""
        return self.edge_bits[:, self.index[tuple(sorted((i, j)))]]

    def same(self, i: int, j: int) -> np.ndarray:
        """Whether positions i and j have the same colour, as floats."""
        return (self.colours[:, i] == self.colours[:, j]).astype(np.float64)

    def average(self, weight: np.ndarray) -> np.ndarray:
        """Average of a per-tuple weight over the orderings of each graph."""
        return np.bincount(self.graph, weights=weight, minlength=self.count) / self.orderings

    def flag_ids(self, positions: tuple[int, ...], roots: int) -> tuple[np.ndarray, np.ndarray]:
        """Flag of the substructure on ordered positions, roots kept in order.

        Returns a flag index per tuple and the canonical codes of the flags,
        the least code under permutations of the non-root positions.
        """
        q = len(positions)
        sub = pairs(q)
        code = np.zeros(self.tuples, dtype=np.int64)
        for k, (a, c) in enumerate(sub):
            code |= self.adj(positions[a], positions[c]).astype(np.int64) << k
        for a in range(q):
            code |= self.colours[:, positions[a]].astype(np.int64) << (len(sub) + a)
        uniq, inverse = np.unique(code, return_inverse=True)
        pid = {p: k for k, p in enumerate(sub)}
        best = None
        for tail in itertools.permutations(range(roots, q)):
            pi = list(range(roots)) + list(tail)
            new = np.zeros_like(uniq)
            for k, (a, c) in enumerate(sub):
                new |= ((uniq >> k) & 1) << pid[tuple(sorted((pi[a], pi[c])))]
            for a in range(q):
                new |= ((uniq >> (len(sub) + a)) & 1) << (len(sub) + pi[a])
            best = new if best is None else np.minimum(best, new)
        canon, flag = np.unique(best, return_inverse=True)
        return flag[inverse], canon


class Switching:
    """Switching rows on k roots: positions 0..k-1 roots, k and k+1 the edge.

    With weighted set, the row is also multiplied by sigma of the first root,
    sampled at position k + 2; both factors are nonnegative pointwise.
    """

    def __init__(self, table: Table, k: int, weighted: bool = False) -> None:
        """Prepare cell and flag indices for this switching family."""
        self.table = table
        self.cells = 2 << k
        u, v = k, k + 1
        cell = []
        for i in (u, v):
            c = table.colours[:, i].astype(np.int64)
            for j in range(k):
                c = c + (table.adj(i, j).astype(np.int64) << (j + 1))
            cell.append(c)
        self.cu, self.cv = cell
        # signed edge: +1 bichromatic, -1 monochromatic; a toggle changes mono by it
        self.weight = table.adj(u, v).astype(np.float64) * (1 - 2 * table.same(u, v))
        rest = tuple(range(k + 2, ORDER))
        if weighted:
            w = k + 2
            self.weight = self.weight * table.adj(0, w) * (1 - 2 * table.same(0, w))
            rest = tuple(range(k + 3, ORDER))
        self.flag, codes = table.flag_ids(tuple(range(k)) + rest, k)
        self.flags = len(codes)
        self.pair = (self.flag * self.cells + self.cu) * self.cells + self.cv
        self.order = np.argsort(self.flag, kind='stable')
        self.start = np.searchsorted(self.flag[self.order], np.arange(self.flags + 1))

    def row(self, f: int, side: np.ndarray) -> np.ndarray:
        """Delta_S times flag f, where S is the set of cells with side 1."""
        ix = self.order[self.start[f]:self.start[f + 1]]
        cross = side[self.cu[ix]] != side[self.cv[ix]]
        return np.bincount(self.table.graph[ix], weights=np.where(cross, self.weight[ix], 0.0),
                           minlength=self.table.count) / self.table.orderings

    def price(self, y: np.ndarray, limit: int, tol: float = 1e-10,
              rng: np.random.Generator | None = None) -> list[tuple[float, int, np.ndarray]]:
        """Most negative rows at the state y: exhaustive over S for at most 16 cells."""
        tb = self.table
        mass = np.bincount(self.pair, weights=y[tb.graph] / tb.orderings * self.weight,
                           minlength=self.flags * self.cells ** 2)
        Q = mass.reshape(self.flags, self.cells, self.cells)
        Q = Q + Q.transpose(0, 2, 1)
        Q[:, np.arange(self.cells), np.arange(self.cells)] = 0.0
        out = []
        if self.cells <= 16:
            sides = ((np.arange(1 << (self.cells - 1))[:, None] >> np.arange(self.cells)[None, :]) & 1)
            S = sides.astype(np.float64)
            for f in range(self.flags):
                q = Q[f]
                if not q.any():
                    continue
                value = S @ q.sum(axis=1) - ((S @ q) * S).sum(axis=1)
                k = int(value.argmin())
                if value[k] < -tol:
                    out.append((float(value[k]), f, sides[k]))
        else:
            rng = rng if rng is not None else np.random.default_rng(0)
            for f in range(self.flags):
                q = Q[f]
                if not q.any():
                    continue
                best = (0.0, None)
                for _ in range(20):
                    s = rng.integers(0, 2, self.cells)
                    for _ in range(60):
                        same = s[None, :] == s[:, None]
                        gain = (q * same).sum(axis=1) - (q * ~same).sum(axis=1)
                        a = int(gain.argmin())
                        if gain[a] >= -1e-15:
                            break
                        s[a] ^= 1
                    value = 0.5 * q[s[:, None] != s[None, :]].sum()
                    if value < best[0]:
                        best = (value, s.copy())
                if best[0] < -tol:
                    out.append((best[0], f, best[1]))
        out.sort(key=lambda t: t[0])
        return out[:limit]


class System:
    """Rows and blocks of the relaxation on the density interval [a, b]."""

    def __init__(self, low: float, high: float, t4: bool = False, products: bool = False) -> None:
        """Build the declared rows and moment blocks on the density interval."""
        tb = self.table = Table()
        self.low, self.high = low, high
        e01 = tb.adj(0, 1).astype(np.float64)
        e23 = tb.adj(2, 3).astype(np.float64)
        self.objective = tb.average(e01 * tb.same(0, 1))
        self.density = tb.average(e01)
        self.rows: list[np.ndarray] = []
        self.add(self.density - low)
        self.add(high - self.density)
        quad = (e01 - low) * (high - e23)
        self.add(tb.average(quad))
        flag, codes = tb.flag_ids((2, 3, 4, 5), 0)
        for weight in (e01 - low, high - e01):
            for f in range(len(codes)):
                self.add(tb.average(np.where(flag == f, weight, 0.0)))
        flag, codes = tb.flag_ids((4, 5), 0)
        for f in range(len(codes)):
            self.add(tb.average(np.where(flag == f, quad, 0.0)))
        sigma = e01 * (1 - 2 * tb.same(0, 1))
        flag, codes = tb.flag_ids((0, 2, 3, 4, 5), 1)
        for f in range(len(codes)):
            self.add(tb.average(np.where(flag == f, sigma, 0.0)))
        self.switching = {str(k): Switching(tb, k) for k in (1, 2, 3, 4)}
        if products:
            # sigma(r1) Delta_S(r) F(r) and sigma(r1) sigma(r2) F(r1, r2)
            for k in (1, 2, 3):
                self.switching[f'{k}s'] = Switching(tb, k, weighted=True)
            sigma2 = tb.adj(0, 2) * (1 - 2 * tb.same(0, 2)) * tb.adj(1, 3) * (1 - 2 * tb.same(1, 3))
            flag, codes = tb.flag_ids((0, 1, 4, 5), 2)
            for f in range(len(codes)):
                self.add(tb.average(np.where(flag == f, sigma2, 0.0)))
        one = self.switching['1']
        for f in range(one.flags):
            for side in itertools.product((0, 1), repeat=one.cells - 1):
                self.add(one.row(f, np.array((0, *side))))
        specs = [
            ((0, 1, 2), (3, 4, 5), 0, None),
            ((0, 1, 2), (0, 3, 4), 1, None),
            ((0, 1, 2, 3), (0, 1, 4, 5), 2, None),
            ((0, 1, 2, 3), (0, 1, 2, 4), 3, None),
            ((0, 2, 3), (0, 4, 5), 1, sigma),
            ((2, 3), (4, 5), 0, e01 - low),
            ((2, 3), (4, 5), 0, high - e01),
        ]
        if t4:
            specs.append(((0, 1, 2, 3, 4), (0, 1, 2, 3, 5), 4, None))
        self.blocks = []
        self.block_scales: list[float] = []
        for first, second, roots, weight in specs:
            self.blocks.extend(self.moment_blocks(first, second, roots, weight))

    def add(self, row: np.ndarray) -> None:
        """Add a row scaled to unit maximum."""
        scale = np.abs(row).max()
        if scale > 1e-12:
            self.rows.append(row / scale)

    def moment_blocks(self, first: tuple[int, ...], second: tuple[int, ...], roots: int,
                      weight: np.ndarray | None) -> list[tuple[np.ndarray, np.ndarray]]:
        """Per root type, the graphs meeting it and their matrices (graphs x n x n)."""
        tb = self.table
        f1, c1 = tb.flag_ids(first, roots)
        f2, c2 = tb.flag_ids(second, roots)
        codes = np.unique(np.concatenate([c1, c2]))
        g1 = np.searchsorted(codes, c1[f1])
        g2 = np.searchsorted(codes, c2[f2])
        if roots:
            rtype, rcodes = tb.flag_ids(first[:roots], roots)
        else:
            rtype, rcodes = np.zeros(tb.tuples, dtype=np.int64), np.zeros(1)
        ftype = -np.ones(len(codes), dtype=np.int64)
        ftype[g1] = rtype
        local = np.zeros(len(codes), dtype=np.int64)
        w = np.ones(tb.tuples) if weight is None else weight
        out = []
        for t in range(len(rcodes)):
            members = np.flatnonzero(ftype == t)
            if len(members) == 0:
                continue
            local[members] = np.arange(len(members))
            sel = np.flatnonzero(rtype == t)
            n = len(members)
            graphs, inverse = np.unique(tb.graph[sel], return_inverse=True)
            F = np.zeros(len(graphs) * n * n)
            np.add.at(F, (inverse * n + local[g1[sel]]) * n + local[g2[sel]], w[sel] / tb.orderings)
            F = F.reshape(len(graphs), n, n)
            F = (F + F.transpose(0, 2, 1)) / 2
            scale = np.abs(np.diagonal(F, axis1=1, axis2=2)).mean() + 1e-30
            self.block_scales.append(float(scale))
            out.append((graphs, F / scale))
        return out

    def state(self, adj: np.ndarray, colours: np.ndarray) -> np.ndarray:
        """Enumerate order-six sample counts and return probabilities as floats."""
        tb = self.table
        n = len(colours)
        y = np.zeros(tb.count)
        tail = np.array(list(itertools.product(range(n), repeat=ORDER - 2)), dtype=np.int64)
        for head in itertools.product(range(n), repeat=2):
            T = np.hstack([np.tile(np.array(head), (len(tail), 1)), tail])
            code = np.zeros(len(T), dtype=np.int64)
            for k, (i, j) in enumerate(pairs(ORDER)):
                code |= adj[T[:, i], T[:, j]].astype(np.int64) << k
            for i in range(ORDER):
                code |= colours[T[:, i]].astype(np.int64) << (len(tb.index) + i)
            graph = tb.lookup[code]
            if (graph < 0).any():
                raise ValueError('sampled a graph with a triangle')
            y += np.bincount(graph, minlength=tb.count)
        return y / n ** ORDER

    def barrier(self, y: np.ndarray, tau: float, R: np.ndarray,
                hessian: bool) -> tuple[float, np.ndarray, np.ndarray | None] | None:
        """Value, gradient and Hessian of the log barrier in (y, tau)."""
        K = self.table.count
        value = 0.0
        g = np.zeros(K + 1)
        H = np.zeros((K + 1, K + 1)) if hessian else None
        for graphs, F in self.blocks:
            M = np.tensordot(y[graphs], F, axes=1) + tau * np.eye(F.shape[1])
            try:
                L = np.linalg.cholesky(M)
            except np.linalg.LinAlgError:
                return None
            value -= 2 * np.log(np.diag(L)).sum()
            if not hessian:
                continue
            S = np.linalg.inv(M)
            g[graphs] -= np.einsum('ij,kji->k', S, F)
            g[K] -= np.trace(S)
            G = S @ F @ S
            H[np.ix_(graphs, graphs)] += F.reshape(len(graphs), -1) @ G.reshape(len(graphs), -1).T
            cross = np.trace(G, axis1=1, axis2=2)
            H[graphs, K] += cross
            H[K, graphs] += cross
            H[K, K] += (S * S).sum()
        s = R @ y + tau
        if np.any(s <= 0) or np.any(y <= 0) or tau <= 0:
            return None
        value -= np.log(s).sum() + np.log(y).sum() + np.log(tau)
        if hessian:
            g[:K] -= R.T @ (1 / s) + 1 / y
            g[K] -= (1 / s).sum() + 1 / tau
            D = 1 / s ** 2
            H[:K, :K] += (R.T * D) @ R + np.diag(1 / y ** 2)
            cross = R.T @ D
            H[:K, K] += cross
            H[K, :K] += cross
            H[K, K] += D.sum() + 1 / tau ** 2
        return value, g, H

    def solve(self, penalty: float = 1e4, final: float = 1e10,
              dual: bool = False, seconds: float = 180,
              lp_seconds: float = 120) -> tuple[np.ndarray, float, float, float]:
        """Maximize the objective minus penalty * tau on the barrier path.

        tau > 0 relaxes every row and block; a converged run ends with tau
        near zero. Returns the state, tau, the objective value and, when dual
        is set, the bound of dual_bound at the last barrier parameter (nan
        otherwise). Positive time limits bound the barrier iterations and the
        optional LP separately. A stopped iterate need not be feasible without
        its positive relaxation tau and is never an optimality certificate.
        """
        if not np.isfinite([seconds, lp_seconds]).all() or seconds <= 0 or lp_seconds <= 0:
            raise ValueError('positive solver time limits are required')
        deadline = time.monotonic() + seconds
        K = self.table.count
        R = np.array(self.rows)
        z = np.concatenate([np.full(K, 1.0 / K), [1e-3]])
        while self.barrier(z[:K], z[K], R, False) is None:
            z[K] *= 2
        c = np.concatenate([self.objective, [-penalty]])
        e = np.concatenate([np.ones(K), [0.0]])
        t = 1.0
        last_t = t
        while t <= final:
            last_t = t
            for _ in range(80):
                if time.monotonic() >= deadline:
                    break
                v, g, H = self.barrier(z[:K], z[K], R, True)
                g = g - t * c
                d = np.concatenate([z[:K], [1.0]])
                kkt = np.zeros((K + 2, K + 2))
                kkt[:K + 1, :K + 1] = H * d[:, None] * d[None, :] + 1e-12 * np.eye(K + 1)
                kkt[:K + 1, K + 1] = e * d
                kkt[K + 1, :K + 1] = e * d
                dz = np.linalg.solve(kkt, np.concatenate([-g * d, [0.0]]))[:K + 1] * d
                decrement = -g @ dz
                if decrement < 2e-7:
                    break
                f0 = v - t * c @ z
                step = 1.0
                while step > 1e-12:
                    zn = z + step * dz
                    r = self.barrier(zn[:K], zn[K], R, False)
                    if r is not None and r[0] - t * c @ zn <= f0 - 0.25 * step * decrement:
                        break
                    step *= 0.5
                z = zn
            if time.monotonic() >= deadline:
                print('positive barrier time limit reached; last iterate is not an optimum', flush=True)
                break
            t *= 10
        y, tau = z[:K], z[K]
        bound = self.dual_bound(y, tau, last_t, R, seconds=lp_seconds) if dual else float('nan')
        return y, float(tau), float(self.objective @ y), bound

    def dual_bound(self, y: np.ndarray, tau: float, t: float, R: np.ndarray,
                   pairs: int = 5, seconds: float = 120) -> float:
        """A dual bound from the state, polished by a linear program.

        Candidate positive semidefinite matrices for each block are the
        barrier's Z_b = (M_b + tau I)^{-1}/t, projected to PSD, and v v^T for
        every eigenvector v of M_b(y) and for (v_i +- v_j)/sqrt(2) over the
        eigenvectors of the pairs smallest eigenvalues. A linear program
        chooses lambda >= 0 on the rows and a weight >= 0 on each candidate to
        minimize max_H (c_H + sum_i lambda_i row_i(H) + sum <Z, F_b(H)>), which
        bounds the objective of every state satisfying the rows and blocks,
        including rows not yet priced. The barrier's own multipliers are one
        feasible choice.
        """
        from scipy.optimize import OptimizeWarning, linprog

        if not np.isfinite(seconds) or seconds <= 0:
            raise ValueError('a positive LP time limit is required')
        K = self.table.count
        cert = self.objective + R.T @ (1 / (t * (R @ y + tau)))
        columns = []
        for graphs, F in self.blocks:
            n = F.shape[1]
            M = np.tensordot(y[graphs], F, axes=1)
            Z = np.linalg.inv(M + tau * np.eye(n)) / t
            lam, V = np.linalg.eigh((Z + Z.T) / 2)
            Z = (V * np.clip(lam, 0, None)) @ V.T
            col = np.zeros(K)
            col[graphs] = np.einsum('ij,kij->k', Z, F)
            cert += col
            columns.append(col)
            _, W = np.linalg.eigh(M)
            vecs = [W[:, k] for k in range(n)]
            for i, j in itertools.combinations(range(min(pairs, n)), 2):
                vecs.append((W[:, i] + W[:, j]) / np.sqrt(2))
                vecs.append((W[:, i] - W[:, j]) / np.sqrt(2))
            U = np.array(vecs)
            values = np.einsum('ci,kij,cj->ck', U, F, U)
            for c in range(len(U)):
                col = np.zeros(K)
                col[graphs] = values[c]
                columns.append(col)
        raw = float(cert.max())
        B = np.array(columns).T
        m, nb = len(R), B.shape[1]
        A_ub = np.hstack([R.T, B, -np.ones((K, 1))])
        with warnings.catch_warnings():
            warnings.filterwarnings('ignore', category=OptimizeWarning,
                                    message='Unrecognized options detected')
            res = linprog(np.concatenate([np.zeros(m + nb), [1.0]]),
                          A_ub=A_ub, b_ub=-self.objective,
                          bounds=[(0, None)] * (m + nb) + [(None, None)], method='highs',
                          options={'time_limit': seconds, 'threads': 1, 'parallel': False})
        if res.status != 0 or res.x is None:
            print(f'LP incomplete (status {res.status}): {res.message}; using raw floating bound',
                  flush=True)
            return raw
        weights = np.clip(res.x[:m + nb], 0, None)
        polished = float((self.objective + A_ub[:, :m + nb] @ weights).max())
        return min(raw, polished)

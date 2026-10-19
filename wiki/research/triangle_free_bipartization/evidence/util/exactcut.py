"""Rigorous weighted-cut lower bounds from branching and integer Gram matrices.

The floating-point log-determinant routine only suggests a factor. Every bound
used for pruning is reconstructed from integers: if Q = K K^T / D^2 and
R = B - Q, set z_i = -R_ii + sum_{j != i} |R_ij|. Then B + diag(z) is PSD,
because its difference from Q is diagonally dominant with nonnegative diagonal.
Consequently s^T B s >= -sum(z) for every sign vector s. No optimizer status,
floating-point eigenvalue, or claimed optimum is used as evidence.
"""

from __future__ import annotations

import math
from collections import Counter
from fractions import Fraction
from numbers import Integral

import numpy as np
from scipy.linalg import cho_factor, cho_solve, solve


def gram_bound(matrix: np.ndarray) -> tuple[Fraction, np.ndarray]:
    """Return an exact lower bound for s^T matrix s and a branching suggestion.

    The symmetric integer matrix has order at most 128. The caller bounds the
    sum of absolute input coefficients. All integer matrix operations below
    have explicit int64 overflow guards. The returned correlation matrix is
    only a heuristic for selecting the next variable to branch on.
    """
    n = len(matrix)
    if (not 1 <= n <= 128 or matrix.shape != (n, n)
            or matrix.dtype != np.dtype(np.int64) or not np.array_equal(matrix, matrix.T)):
        raise ValueError('expected a symmetric matrix of order 1..128')
    maximum = max(abs(int(v)) for v in matrix.flat)
    if maximum > 2 ** 51:
        raise OverflowError('input matrix is outside the coefficient bound')
    scale = max(float(np.abs(matrix).sum(axis=1).max()), 1.0)
    normalized = matrix / scale
    diagonal = np.full(n, max(1.0, -float(np.linalg.eigvalsh(normalized)[0]) + 1.0))
    identity = np.eye(n)
    inverse = identity
    mu = 1.0
    for mu in (1.0, 0.1, 0.01, 0.001, 0.0001, 0.00001):
        for _ in range(60):
            factor = cho_factor(normalized + np.diag(diagonal), lower=True)
            inverse = cho_solve(factor, identity)
            gradient = 1.0 - mu * np.diag(inverse)
            hessian = mu * inverse * inverse
            step = solve(hessian, -gradient, assume_a='pos')
            if -float(gradient @ step) < 1e-9:
                break
            value = diagonal.sum() - 2 * mu * np.log(np.diag(factor[0])).sum()
            length = 1.0
            for _ in range(50):
                candidate = diagonal + length * step
                try:
                    trial = cho_factor(normalized + np.diag(candidate), lower=True)
                    objective = candidate.sum() - 2 * mu * np.log(np.diag(trial[0])).sum()
                    if objective <= value + 0.01 * length * float(gradient @ step):
                        break
                except np.linalg.LinAlgError:
                    pass
                length *= 0.5
            else:
                raise RuntimeError('numeric proposal failed; no bound accepted')
            diagonal = candidate

    # Any finite factor works; proximity to a dual optimum only affects strength.
    factor = np.linalg.cholesky(matrix + np.diag(diagonal * scale))
    if not np.isfinite(factor).all():
        raise RuntimeError('nonfinite proposal')
    largest = max(float(np.abs(factor).max()), 1e-100)
    denominator = 2 ** min(30, max(0, math.floor(math.log2(2 ** 25 / largest))))
    rounded = np.rint(factor * denominator)
    if float(np.abs(rounded).max()) > 2 ** 26:
        raise OverflowError('rounded factor exceeds its exact-product bound')
    integral = rounded.astype(np.int64)
    # n <= 128 and |K_ij| <= 2^26 imply |(K K^T)_ij| <= 2^59.
    gram = integral @ integral.T
    square = denominator * denominator
    if maximum * square > 2 ** 60:
        raise OverflowError('scaled input exceeds its exact-product bound')
    residual = matrix * square - gram
    largest_residual = max(abs(int(v)) for v in residual.flat)
    if n * largest_residual > 2 ** 62:
        raise OverflowError('residual row sum exceeds its exact-sum bound')
    correction = (np.abs(residual).sum(axis=1) - np.abs(np.diag(residual))
                  - np.diag(residual))
    # The formula gives a diagonally dominant residual for every integer K.
    # Python's unbounded sum and Fraction finish the exact bound.
    lower = -Fraction(sum(map(int, correction)), square)
    return lower, mu * inverse


def certify_lower_bound(table: Counter, target: Fraction | int,
                        max_nodes: int = 2000) -> tuple[bool, int]:
    """Prove every Boolean profile rule has uncut weight at least target.

    Return (proved, visited_nodes). A false return has an exactly enumerated
    counterexample within a branch. A resource cap or failed numeric proposal
    raises an exception, never a successful result. Loops are always uncut.
    The partition branches on both values of every chosen sign; global colour
    reversal permits fixing the first sign to +1.
    """
    if not table or any(not isinstance(w, Integral) or w < 0 for w in table.values()):
        raise ValueError('expected nonempty nonnegative integer weights')
    nodes = sorted({x for pair in table for x in pair})
    n = len(nodes)
    if not 1 <= n <= 128 or sum(map(int, table.values())) > 2 ** 50:
        raise ValueError('profile count or total weight exceeds the exact arithmetic domain')
    position = {v: i for i, v in enumerate(nodes)}
    divisor = math.gcd(*map(int, table.values()))
    if not divisor:
        return Fraction(target) <= 0, 1
    adjacency = np.zeros((n, n), dtype=np.int64)
    loops = 0
    off_diagonal = 0
    for (a, b), weight in table.items():
        if a > b:
            raise ValueError('profile pairs must be sorted')
        weight = int(weight) // divisor
        if a == b:
            loops += weight
        else:
            adjacency[position[a], position[b]] = weight
            adjacency[position[b], position[a]] = weight
            off_diagonal += weight
    wanted = math.ceil(Fraction(target) / divisor)
    first = int(np.argmax(adjacency.sum(axis=1)))
    visits = 0

    def visit(fixed: list[int], signs: list[int]) -> bool:
        nonlocal visits
        visits += 1
        if visits > max_nodes:
            raise RuntimeError(f'exact cut certificate exhausted {max_nodes} branch nodes')
        remaining = [i for i in range(n) if i not in fixed]
        values = np.array(signs, dtype=np.int64)
        # Absolute sums in these products are <= twice the original total weight.
        constant = int(values @ adjacency[np.ix_(fixed, fixed)] @ values)
        if not remaining:
            value = Fraction(loops) + Fraction(off_diagonal, 2) + Fraction(constant, 4)
            return value >= wanted
        field = values @ adjacency[np.ix_(fixed, remaining)]
        block = np.zeros((len(remaining) + 1, len(remaining) + 1), dtype=np.int64)
        block[0, 1:] = block[1:, 0] = field
        block[1:, 1:] = adjacency[np.ix_(remaining, remaining)]
        energy_lower, correlation = gram_bound(block)
        lower = (Fraction(loops) + Fraction(off_diagonal, 2)
                 + (constant + energy_lower) / 4)
        if math.ceil(lower) >= wanted:
            return True
        # A correlation affects coverage order only: both children are checked.
        relative = np.abs(correlation[0, 1:]) / np.sqrt(
            np.maximum(correlation[0, 0] * np.diag(correlation)[1:], 1e-30))
        scores = ((1 - np.minimum(relative, 1))
                  * np.sqrt(np.maximum(np.abs(adjacency[remaining]).sum(axis=1), 1)))
        vertex = remaining[int(np.argmax(scores))]
        return (visit(fixed + [vertex], signs + [1])
                and visit(fixed + [vertex], signs + [-1]))

    return visit([first], [1]), visits

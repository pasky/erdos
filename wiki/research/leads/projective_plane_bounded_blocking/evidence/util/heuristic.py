"""First-moment heuristic for constant-cap blocking sets.

For a cap C and a mean load K, the rate D(K, C) is the least relative
entropy D(nu || Pois(K)) over distributions nu on {1, ..., C} with mean K and
variance K, the load mean and variance that every point set of size Kq has
up to lower-order terms. The minimizer is an exponential tilt
nu(x) proportional to Pois(K)(x) exp(a x + b x^2); its parameters solve a
convex dual problem, here by damped Newton steps in floating point. The
crossover order q*(K, C) is the largest q with K q log(e q / K) >= D q^2,
the point beyond which the entropy of Kq-point sets no longer pays for the
constraints on about q^2 lines. The heuristic order is the maximum of
q*(K, C) over the grid K = 1.05, 1.10, ... below C with (K - 1)(C - K) > K.
These numbers are heuristic outputs, not bounds.

The symmetric estimate applies the same count to unions of K classes
modulo M of a Singer cycle (see ``singer.py``): the base distribution is the
load of one line orbit under a uniformly random K-element set of classes,
the forced moments are mean k(p + 1)/M and second moment (k p + k^2 N/M)/M,
and the estimated number of solutions containing class 0 is
binom(M - 1, k - 1) exp(-M D), maximized over k.
"""

from __future__ import annotations

import math

__all__ = [
    'crossover',
    'heuristic_order',
    'rate',
    'symmetric_estimate',
]


def _dual(theta: tuple[float, float], logp: list[float], m1: float, m2: float) -> tuple[float, list[float], list[list[float]]]:
    """Return the dual value, its gradient and its Hessian at theta."""
    xs = range(1, len(logp) + 1)
    vals = [lp + theta[0] * x + theta[1] * x * x for lp, x in zip(logp, xs, strict=True)]
    top = max(vals)
    w = [math.exp(v - top) for v in vals]
    z = sum(w)
    pr = [u / z for u in w]
    e1 = sum(p * x for p, x in zip(pr, xs, strict=True))
    e2 = sum(p * x * x for p, x in zip(pr, xs, strict=True))
    e3 = sum(p * x**3 for p, x in zip(pr, xs, strict=True))
    e4 = sum(p * x**4 for p, x in zip(pr, xs, strict=True))
    value = top + math.log(z) - theta[0] * m1 - theta[1] * m2
    grad = [e1 - m1, e2 - m2]
    hess = [[e2 - e1 * e1, e3 - e1 * e2], [e3 - e1 * e2, e4 - e2 * e2]]
    return value, grad, hess


def rate(k: float, cap: int) -> float:
    """Return D(K, C), the least relative entropy to Pois(K) under the moment constraints."""
    logp = [-k + x * math.log(k) - math.lgamma(x + 1) for x in range(1, cap + 1)]
    return _tilted_rate(logp, k, k * k + k)


def _tilted_rate(logp: list[float], m1: float, m2: float) -> float:
    """Return the least relative entropy to the base masses exp(logp) on 1, ..., C with moments m1, m2."""
    theta = (0.0, 0.0)
    value, grad, hess = _dual(theta, logp, m1, m2)
    for _ in range(500):
        if math.hypot(*grad) < 1e-11:
            break
        det = hess[0][0] * hess[1][1] - hess[0][1] * hess[1][0]
        d0 = -(hess[1][1] * grad[0] - hess[0][1] * grad[1]) / det
        d1 = -(-hess[1][0] * grad[0] + hess[0][0] * grad[1]) / det
        slope = grad[0] * d0 + grad[1] * d1
        # backtrack far from the optimum; near it, rounding makes the Armijo test unreliable
        t = 1.0
        while True:
            trial = (theta[0] + t * d0, theta[1] + t * d1)
            tv, tg, th = _dual(trial, logp, m1, m2)
            if math.hypot(*grad) < 1e-6 or tv <= value + 1e-4 * t * slope or t < 1e-12:
                break
            t /= 2
        theta, value, grad, hess = trial, tv, tg, th
    else:
        raise ArithmeticError('Newton iteration did not converge')
    if math.hypot(*grad) >= 1e-8:
        raise ArithmeticError('moment constraints not met')
    return -value


def crossover(k: float, d: float) -> float:
    """Return the largest q with K q log(e q / K) >= d q^2, or 0 when no such q >= K exists."""
    q = 1e6
    for _ in range(10000):
        # the iteration decreases monotonically to the largest fixed point, if there is one above K
        if q <= k:
            return 0.0
        nxt = k * math.log(math.e * q / k) / d
        if abs(nxt - q) < 1e-10:
            return nxt
        q = nxt
    raise ArithmeticError('fixed-point iteration did not converge')


def heuristic_order(cap: int) -> tuple[float, float, float]:
    """Return (K, D(K, C), q*) maximizing the crossover order over the K grid."""
    best = None
    for j in range(21, 20 * cap - 1):
        k = j / 20
        if (k - 1) * (cap - k) <= k:
            continue
        d = rate(k, cap)
        q = crossover(k, d)
        if best is None or q > best[2]:
            best = (k, d, q)
    if best is None:
        raise ValueError('no admissible mean load')
    return best


def _subset_sums(mu: list[int], k: int) -> list[float]:
    """Return the distribution of sum_{r in K} mu(r) over uniformly random k-element sets K."""
    total = sum(mu)
    dp = [[0.0] * (total + 1) for _ in range(k + 1)]
    dp[0][0] = 1.0
    for v in mu:
        for j in range(k, 0, -1):
            row, prev = dp[j], dp[j - 1]
            for s in range(total - v, -1, -1):
                if prev[s]:
                    row[s + v] += prev[s]
    count = math.comb(len(mu), k)
    return [x / count for x in dp[k]]


def symmetric_estimate(mu: list[int], p: int, cap: int) -> tuple[int, float]:
    """Return (k, log10 of the estimated solution count) maximizing over admissible k."""
    m = len(mu)
    n = p * p + p + 1
    best = None
    for k in range(1, m):
        m1 = k * (p + 1) / m
        m2 = (k * p + k * k * n / m) / m
        var = m2 - m1 * m1
        # the forced moments must lie strictly inside those of distributions on 1, ..., C
        if not (1 < m1 < cap) or not (0 < var < (m1 - 1) * (cap - m1)):
            continue
        dist = _subset_sums(mu, k)
        if any(x >= len(dist) or dist[x] <= 0 for x in range(1, cap + 1)):
            continue
        d = _tilted_rate([math.log(dist[x]) for x in range(1, cap + 1)], m1, m2)
        value = (math.log(math.comb(m - 1, k - 1)) - m * d) / math.log(10)
        if best is None or value > best[1]:
            best = (k, value)
    if best is None:
        raise ValueError('no admissible number of classes')
    return best

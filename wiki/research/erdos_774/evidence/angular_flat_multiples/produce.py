"""Search for low-degree flat multiples of a cyclotomic polynomial (discovery only).

For an integer N and a list of degrees D, decide with the HiGHS mixed-integer
solver in SciPy whether some integer polynomial Q with Q(0) = 1 and degree at
most D - phi(N) makes every coefficient of Phi_N Q lie in {-1, 0, 1}. Every
nonzero flat multiple of Phi_N can be divided by a power of x and negated to
satisfy Q(0) = 1 without raising its degree, so an infeasible degree D means
that no flat multiple of degree at most D exists, and a solution of degree D
remains feasible at every larger degree. The unknowns are bounded by the
partial sums of the absolute coefficients of the power series 1/Phi_N, which
every solution satisfies because Q = P / Phi_N. The solver is limited to one
thread. A reported infeasibility is the solver's verdict, not a retained
certificate, and a time-limit stop decides nothing; a reported solution is
checked here by exact multiplication before it is written.

Run from the repository root, for example:
    uv run --no-sync python wiki/research/erdos_774/evidence/angular_flat_multiples/produce.py 1155 501,502

Dependencies are NumPy, SciPy and SymPy from the repository's evidence group.
Results are printed and appended to the ignored ``output/runs.txt`` beside
this script; they are not evidence. The runs recorded on the evidence page
took from under a second to fifteen minutes each.
"""

from __future__ import annotations

import pathlib
import sys
import time
import warnings

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from sympy import Poly, cyclotomic_poly, symbols

__all__ = [
    'main',
]

_HERE = pathlib.Path(__file__).resolve().parent


def _phi_coefficients(n: int) -> list[int]:
    """Return the coefficients of Phi_n, low degree first."""
    x = symbols('x')
    return [int(c) for c in Poly(cyclotomic_poly(n, x), x).all_coeffs()[::-1]]


def _inverse_series(a: list[int], length: int) -> list[int]:
    """Return the first coefficients of the power series 1 / a, with a[0] == 1."""
    b = [0] * length
    b[0] = 1
    for j in range(1, length):
        b[j] = -sum(a[i] * b[j - i] for i in range(1, min(j, len(a) - 1) + 1))
    return b


def _search(n: int, degree: int, time_limit: float) -> tuple[int, list[int] | None]:
    """Return the solver status and a verified multiplier, if one was found."""
    a = _phi_coefficients(n)
    f = len(a) - 1
    m = degree - f
    if m < 0:
        return 2, None
    beta = _inverse_series(a, m + 1)
    bound = [sum(abs(t) for t in beta[: j + 1]) for j in range(m + 1)]
    matrix = np.zeros((degree + 1, m + 1))
    for j in range(m + 1):
        matrix[j : j + f + 1, j] = a
    lower = [-b for b in bound]
    upper = list(bound)
    lower[0] = upper[0] = 1
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        result = milp(
            c=np.zeros(m + 1),
            constraints=[LinearConstraint(matrix, -1, 1)],
            integrality=np.ones(m + 1),
            bounds=Bounds(lower, upper),
            options={'time_limit': time_limit, 'disp': False, 'threads': 1},
        )
    if result.x is None:
        return result.status, None
    q = [int(round(t)) for t in result.x]
    product = [0] * (len(a) + len(q) - 1)
    for i, s in enumerate(a):
        for j, t in enumerate(q):
            product[i + j] += s * t
    if any(c not in (-1, 0, 1) for c in product) or product[0] != 1:
        raise ValueError('solver point is not a flat multiple')
    return result.status, q


def main() -> int:
    """Run the requested searches and record them in the ignored output folder."""
    n = int(sys.argv[1])
    degrees = [int(t) for t in sys.argv[2].split(',')]
    time_limit = float(sys.argv[3]) if len(sys.argv) > 3 else 600.0
    out = _HERE / 'output'
    out.mkdir(exist_ok=True)
    with open(out / 'runs.txt', 'a', encoding='utf-8') as log:
        for degree in degrees:
            start = time.time()
            status, q = _search(n, degree, time_limit)
            verdict = {0: 'feasible', 1: 'time limit', 2: 'infeasible'}.get(status, f'status {status}')
            line = f'N={n} D={degree} {verdict} time={time.time() - start:.1f}s'
            if q is not None:
                line += f' Q={q}'
            print(line, flush=True)
            log.write(line + '\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())

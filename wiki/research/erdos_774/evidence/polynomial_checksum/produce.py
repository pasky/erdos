"""Search for monochromatic ternary relations against the binary checksum palette.

Finite range: characteristic 2, stages m = 0, 1, 2, both checksum colors.
For each stage and color the script forms the 0/1 incidence matrix of that
color's cosets and asks a mixed-integer solver for a nonzero coefficient
vector in {-1, 0, 1} with zero row sums, minimizing the support size under a
20-second cap. A returned witness is accepted only after exact integer
reconstruction; solver infeasibility and optimality reports are not
mathematical certificates. Proposed witnesses are written to the ignored
``output/`` folder beside this script; the retained witnesses in ``assets/``
are checked independently by ``main.py``.

Run from the repository root:
    uv run --no-sync python wiki/research/erdos_774/evidence/polynomial_checksum/produce.py

Dependencies beyond the standard library are NumPy and SciPy (HiGHS through
``scipy.optimize.milp``), which the repository does not declare; install
them separately before running. The original run used Python 3.13, NumPy
2.5 and SciPy 1.18 with single-threaded BLAS. Solver choices need not
reproduce the same witnesses; the question and bounds are exact.
"""

from __future__ import annotations

import json
import math
import pathlib
import time

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import csc_matrix, eye, hstack, vstack

__all__ = [
    'main',
]

# write disposable products beside this script under the ignored output folder
_OUTPUT = pathlib.Path(__file__).with_name('output') / 'checksum_results.json'


def _mul(a: int, b: int) -> int:
    """Multiply two binary polynomials encoded as integers."""
    z = 0
    while b:
        if b & 1:
            z ^= a
        b >>= 1
        a <<= 1
    return z


def _checksum(a: int) -> int:
    """Return the Catalan-parity checksum of a binary polynomial."""
    z = 0
    j = 0
    while a:
        if a & 1:
            z ^= (math.comb(2 * j, j) // (j + 1)) & 1
        a >>= 1
        j += 1
    return z


def main() -> int:
    """Run the bounded search and write every returned result to output."""
    out = []
    for m in range(3):
        nx = 1 << (m + 1)
        ny = 1 << (2 * m + 1)
        nr = nx * ny
        directions = [('vertical', None, 0)] + [('slope', r, max(0, r.bit_length() - 1)) for r in range(nx)]
        cols = []
        for _, r, j in directions:
            subgroup = [(0, a) for a in range(2)] if r is None else [(a, _mul(r, a)) for a in range(1 << (j + 1))]
            used: set[int] = set()
            for row in range(nr):
                if row in used:
                    continue
                u, v = row % nx, row // nx
                support = sorted((u ^ a) + nx * (v ^ b) for a, b in subgroup)
                used.update(support)
                color = _checksum(u) if r is None else _checksum(v ^ _mul(r, u))
                # every point of a coset must carry the same checksum color
                if not all((_checksum(z % nx) if r is None else _checksum((z // nx) ^ _mul(r, z % nx))) == color for z in support):
                    raise ValueError('checksum is not constant on a coset')
                cols.append({'r': r, 'j': j, 'rep': [u, v], 'support': support, 'color': color})
        for color in range(2):
            chosen = [c for c in cols if c['color'] == color]
            nc = len(chosen)
            matrix = np.zeros((nr, nc), dtype=np.int64)
            for j, col in enumerate(chosen):
                matrix[col['support'], j] = 1
            sparse = csc_matrix(matrix)
            constraints = vstack(
                [hstack([sparse, -sparse]), hstack([eye(nc), eye(nc)]), csc_matrix(np.ones((1, 2 * nc)))],
                format='csc',
            )
            low = np.r_[np.zeros(nr), np.zeros(nc), 1.0]
            high = np.r_[np.zeros(nr), np.ones(nc), 2 * nc]
            started = time.monotonic()
            result = milp(
                np.ones(2 * nc),
                integrality=np.ones(2 * nc),
                bounds=Bounds(np.zeros(2 * nc), np.ones(2 * nc)),
                constraints=LinearConstraint(constraints, low, high),
                options={'time_limit': 20.0, 'mip_rel_gap': 0.0},
            )
            record = {
                'm': m, 'p': 2, 'color': color, 'row_count': nr, 'total_columns': len(cols),
                'class_columns': nc, 'time_cap_seconds': 20, 'status': int(result.status),
                'message': result.message, 'elapsed_seconds': time.monotonic() - started,
            }
            if result.x is not None:
                bits = np.rint(result.x).astype(np.int64)
                coefficients = bits[:nc] - bits[nc:]
                # accept a witness only after exact integer reconstruction
                exact = (
                    np.max(np.abs(result.x - bits)) < 1e-6
                    and np.all(bits[:nc] + bits[nc:] <= 1)
                    and np.any(coefficients)
                    and np.all(np.abs(coefficients) <= 1)
                    and np.all(matrix @ coefficients == 0)
                )
                if not exact:
                    raise ValueError('solver returned a vector that is not an exact ternary relation')
                record['verified_witness'] = [dict(chosen[i], coefficient=int(a)) for i, a in enumerate(coefficients) if a]
                record['witness_size'] = int(np.count_nonzero(coefficients))
            out.append(record)
            print(json.dumps({k: v for k, v in record.items() if k != 'verified_witness'}), flush=True)
            _OUTPUT.parent.mkdir(exist_ok=True)
            _OUTPUT.write_text(json.dumps(out, indent=2) + '\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

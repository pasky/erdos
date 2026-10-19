"""Explore capped floating-point basis reduction for projected moment lattices.

This is a retained exploratory diagnostic in float64, not an exact
certificate, and it produces no evidence. The range is d = 4, ..., 7 and k in
{1, 2} with 2k < d. For each pair the monomials x_A with |A| > k are
projected orthogonally off the Walsh functions of degree at most k, and a
cursor scan applies integer size reductions and Lovasz-parameter 0.75
adjacent swaps, allowing a swap only when the updated Gram--Schmidt
coordinate cap stays at most 0.25 + 1e-9 (inequality tolerance 1e-10). Each
run stops after a complete cursor scan, 20,000 cursor steps or 1,000
accepted swaps, whichever comes first. There is no randomness. The printed
summary (rank, initial and final energy T/n, maximal coordinate, swaps,
steps, complete scan) is written to the ignored ``output/`` folder.

Run from the repository root:
    uv run --no-sync python wiki/research/erdos_774/evidence/moment_basis_float/produce.py

Dependencies beyond the standard library are NumPy, which the repository
does not declare; install it separately before running. The original run
set OPENBLAS_NUM_THREADS=1. Floating-point results are observations only;
neither extraction nor coloring conclusions depend on them.
"""

from __future__ import annotations

import json
import pathlib
from itertools import combinations

import numpy as np

__all__ = [
    'main',
]

# write disposable products beside this script under the ignored output folder
_OUTPUT = pathlib.Path(__file__).with_name('output') / 'basis_reduction.json'


def main() -> int:
    """Run the capped reduction for every pair and record the summary."""
    summaries = []
    for d in range(4, 8):
        for k in (1, 2):
            if 2 * k >= d:
                continue
            n = 1 << d
            x = (np.arange(n)[:, None] >> np.arange(d)) & 1
            chis, monos = [], []
            for size in range(d + 1):
                for subset in combinations(range(d), size):
                    if size <= k:
                        chis.append(np.prod(1 - 2 * x[:, subset], axis=1))
                    else:
                        monos.append(np.prod(x[:, subset], axis=1))
            walsh = np.array(chis, dtype=float)
            basis = np.array(monos, dtype=float)
            basis -= ((basis @ walsh.T) / n) @ walsh
            q, r = np.linalg.qr(basis.T, mode='reduced')
            initial = float(np.sum(np.diag(r) ** 2)) / n
            j = 1
            steps = swaps = blocked = 0
            while j < len(basis) and steps < 20000 and swaps < 1000:
                steps += 1
                for i in range(j - 1, -1, -1):
                    z = int(np.rint(r[i, j] / r[i, i]))
                    if z:
                        basis[j] -= z * basis[i]
                        r[:, j] -= z * r[:, i]
                i = j - 1
                a, c, mu = r[i, i] ** 2, r[j, j] ** 2, r[i, j] / r[i, i]
                a_prime = c + mu * mu * a
                if a_prime < 0.75 * a - 1e-10:
                    u, v = q[:, i] * r[i, i], q[:, j] * r[j, j]
                    w, z = mu * u + v, (c * u - mu * a * v) / a_prime
                    if max(np.max(np.abs(w)), np.max(np.abs(z))) <= 0.25 + 1e-9:
                        basis[[i, j]] = basis[[j, i]]
                        q, r = np.linalg.qr(basis.T, mode='reduced')
                        swaps += 1
                        j = max(1, j - 1)
                        continue
                    blocked += 1
                j += 1
            coordinates = q * np.diag(r)
            summary = dict(
                d=d, k=k, rank=len(basis),
                initial_T_over_n=round(initial, 8),
                final_T_over_n=round(float(np.sum(np.diag(r) ** 2)) / n, 8),
                max_coordinate=round(float(np.max(np.abs(coordinates))), 8),
                swaps=swaps, blocked=blocked, steps=steps, complete_scan=bool(j == len(basis)),
            )
            print(summary, flush=True)
            summaries.append(summary)
    _OUTPUT.parent.mkdir(exist_ok=True)
    _OUTPUT.write_text(json.dumps(summaries, indent=2) + '\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

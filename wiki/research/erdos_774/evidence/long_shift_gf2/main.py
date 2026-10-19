"""Check the binary ranks of increasing-path relations on pair labels.

The full domain is 2 <= k <= 7 and k + 1 <= n <= min(12, 2k + 4), 39 cases.
For each case the pairs {i, j} of [n] are the coordinates, every increasing
(k+1)-tuple gives the binary vector of its k consecutive pairs, and the
active-column nullity is the number of pair coordinates minus the GF(2) rank
of these vectors minus the number of inactive pairs with j - i > n - k. The
check is that the 39 nullities equal the recorded table on the owning page:
for k = 2 they are all 1, and for k >= 3 they decrease from k - 1 to zero or
one as n grows. Arithmetic is exact GF(2) elimination on bit vectors; no
search runs.

Run from the repository root:
    uv run --no-sync python wiki/research/erdos_774/evidence/long_shift_gf2/main.py

Dependencies are the standard library and the installed root ``tools``
package. There are no file inputs, output files, random choices or reduced
modes. Expected runtime is under a second. Failed obligations exit nonzero,
including under ``python -O``. The general binary rank theorem on the owning
lemma page does not use this table.
"""

from __future__ import annotations

import itertools
import sys

import tools

__all__ = [
    'active_nullity',
    'main',
]

# retain the recorded nullities by k, listed for consecutive n from k + 1
_TABLE = {
    2: [1, 1, 1, 1, 1, 1],
    3: [2, 2, 1, 0, 0, 0, 0],
    4: [3, 3, 2, 1, 1, 1, 1, 1],
    5: [4, 4, 3, 2, 1, 0, 0],
    6: [5, 5, 4, 3, 2, 1],
    7: [6, 6, 5, 4, 3],
}


def active_nullity(k: int, n: int) -> int:
    """Return the active-column GF(2) nullity of the increasing-path relations."""
    edges = list(itertools.combinations(range(n), 2))
    index = {e: i for i, e in enumerate(edges)}
    rows: dict[int, int] = {}
    for path in itertools.combinations(range(n), k + 1):
        vector = sum(1 << index[e] for e in zip(path, path[1:]))
        while vector:
            bit = vector.bit_length() - 1
            if bit in rows:
                vector ^= rows[bit]
            else:
                rows[bit] = vector
                break
    inactive = sum(j - i > n - k for i, j in edges)
    return len(edges) - len(rows) - inactive


def main() -> int:
    """Run every finite obligation and return the shared checker's exit code."""
    # parse the fixed-domain interface and recompute every case
    parser = tools.evidence_parser('Check the 39 long-shift binary nullities.', quick=False)
    parser.parse_args()
    checker = tools.Checker()
    total = 0
    for k in range(2, 8):
        values = [active_nullity(k, n) for n in range(k + 1, min(13, 2 * k + 5))]
        total += len(values)
        checker.check(f'k = {k}: nullities {values} match the recorded table', values == _TABLE[k], f'expected {_TABLE[k]}')
    checker.check('39 cases in total', total == 39, f'observed {total}')
    print(f'{total} exact GF(2) nullities recomputed')
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

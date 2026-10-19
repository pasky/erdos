"""Discover the two retained colorings (discovery only).

Mode `bohr m s seed` draws theta_1, ..., theta_m uniformly, puts x in the
sum-free set B_i = {x : {theta_i x} in (1/3, 2/3)}, and gives each x in
[1, s] a uniformly random available color, as in Lemma B of the refutation
of claim L260. Floating arithmetic serves discovery only. The retained input
assets/bohr_psi_m20.json was produced by `bohr 20 800 4`.

Mode `schur n k` runs a depth-first search for a coloring of [1, n] by k
colors with no monochromatic x + y = z (x = y allowed), trying the colors in
order and introducing a new color only after the used ones. The retained
input assets/schur_44.json was produced by `schur 44 4`, in a few seconds.

Outputs go to the ignored output/ folder; main.py re-verifies the retained
inputs exactly and does not rely on either search. Commands, from the
repository root:
    uv run --no-sync python wiki/research/schur_number_growth/evidence/produce.py bohr 20 800 4
    uv run --no-sync python wiki/research/schur_number_growth/evidence/produce.py schur 44 4
"""

from __future__ import annotations

import json
import random
import sys
from pathlib import Path

OUTPUT = Path(__file__).parent / 'output'


def bohr(m: int, s: int, seed: int) -> tuple[list, list] | None:
    """Return a Bohr coloring and exact rational frequencies, or None."""
    rng = random.Random(seed)
    for _ in range(10000):
        # draw the frequencies and the available colors of each x
        thetas = [rng.random() for _ in range(m)]
        avail = []
        for x in range(1, s + 1):
            colors = [
                i for i, th in enumerate(thetas) if 1 / 3 < (th * x) % 1.0 < 2 / 3
            ]
            if not colors:
                break
            avail.append(colors)
        if len(avail) < s:
            continue
        # assign the colors and keep the coloring when it uses all m
        coloring = [rng.choice(colors) for colors in avail]
        if len(set(coloring)) == m:
            return coloring, [list(th.as_integer_ratio()) for th in thetas]
    return None


def schur(n: int, k: int) -> list | None:
    """Return a Schur-free coloring of [1, n] by k colors found by search, or None."""
    col: list[int | None] = [None] * (n + 1)

    def free(x: int, c: int) -> bool:
        # no a + (x - a) = x with both summands of color c
        return all(not (col[a] == c and col[x - a] == c) for a in range(1, x // 2 + 1))

    def extend(x: int, used: int) -> bool:
        if x > n:
            return True
        for c in range(min(used + 1, k)):
            if free(x, c):
                col[x] = c
                if extend(x + 1, max(used, c + 1)):
                    return True
                col[x] = None
        return False

    sys.setrecursionlimit(max(1000, 4 * n))
    return col[1:] if extend(1, 0) else None


def main() -> int:
    """Write a proposed coloring to ignored output for separate checking."""
    mode, args = sys.argv[1], [int(a) for a in sys.argv[2:]]
    if mode == 'bohr':
        m, s, seed = args
        result = bohr(m, s, seed)
        if result is None:
            print('no coloring found')
            return 1
        coloring, frequencies = result
        name, data = f'bohr_psi_m{m}.json', {'m': m, 's': s, 'frequencies': frequencies}
    else:
        n, k = args
        coloring, name, data = schur(n, k), f'schur_{n}.json', {'n': n, 'k': k}
    if coloring is None:
        print('no coloring found')
        return 1
    OUTPUT.mkdir(exist_ok=True)
    (OUTPUT / name).write_text(json.dumps({**data, 'colors': coloring}))
    print(f'wrote {OUTPUT / name}')
    return 0


if __name__ == '__main__':
    sys.exit(main())

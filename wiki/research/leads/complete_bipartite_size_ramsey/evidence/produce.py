"""Write the SAT instances behind the lead's finite diagnostics, and optionally solve them.

A variable is one host edge, true for red. For K_{a,b} (columns 1..a, rows
1..b) every pair of an n-set of columns and an n-set of rows gives two clauses,
not all red and not all blue, and the rows are kept in nonincreasing
lexicographic order to break their symmetry. For K_N every unordered pair of
disjoint n-sets gives the same two clauses. A satisfying assignment is a
colouring without a monochromatic K_{n,n}; ``main.py`` checks any colouring
retained in ``assets/``. An unsatisfiable verdict here is a solver verdict
only: no proof certificate is produced or checked.

Usage, from the repository root:
    uv run --no-sync python wiki/research/leads/complete_bipartite_size_ramsey/evidence/produce.py kab A B N [--solve SECONDS]
    uv run --no-sync python wiki/research/leads/complete_bipartite_size_ramsey/evidence/produce.py kn NV N [--solve SECONDS]

The instance is written to ``output/``, which Git ignores. ``--solve`` runs
``kissat`` from the PATH with that time limit and writes a found colouring to
``output/`` in the format of ``assets/witnesses.json``. This is a discovery
tool, not evidence: nothing it writes is trusted until ``main.py`` checks it.
"""

from __future__ import annotations

import argparse
import itertools
import json
import shutil
import subprocess
from pathlib import Path

_OUT = Path(__file__).resolve().parent / 'output'


def kab_clauses(a: int, b: int, n: int) -> tuple[int, list[list[int]]]:
    """Return the variable count and clauses for K_{a,b}, with row symmetry breaking."""

    def var(j: int, i: int) -> int:
        return j * a + i + 1

    clauses = []
    for cols in itertools.combinations(range(a), n):
        for rows in itertools.combinations(range(b), n):
            lits = [var(j, i) for j in rows for i in cols]
            clauses.append(lits)
            clauses.append([-x for x in lits])
    nv = a * b
    for j in range(b - 1):
        prev = None
        for k in range(a):
            x, y = var(j, k), var(j + 1, k)
            # while rows j and j+1 agree on columns before k, row j is not below row j+1 at k
            clauses.append([x, -y] if prev is None else [-prev, x, -y])
            if k < a - 1:
                nv += 1
                e = nv
                if prev is None:
                    clauses += [[-e, x, -y], [-e, -x, y], [e, x, y], [e, -x, -y]]
                else:
                    clauses += [
                        [-e, prev],
                        [-e, x, -y],
                        [-e, -x, y],
                        [e, -prev, x, y],
                        [e, -prev, -x, -y],
                    ]
                prev = e
    return nv, clauses


def kn_clauses(
    nv: int, n: int
) -> tuple[int, list[list[int]], dict[int, tuple[int, int]]]:
    """Return the variable count, clauses and edge of each variable for K_nv."""
    edge = {}
    index = {}
    for u, v in itertools.combinations(range(nv), 2):
        index[(u, v)] = len(index) + 1
        edge[index[(u, v)]] = (u, v)
    clauses = []
    for s in itertools.combinations(range(nv), n):
        rest = [x for x in range(nv) if x not in s]
        for t in itertools.combinations(rest, n):
            if s < t:
                lits = [index[(min(x, y), max(x, y))] for x in s for y in t]
                clauses.append(lits)
                clauses.append([-x for x in lits])
    return len(index), clauses, edge


def write(path: Path, nv: int, clauses: list[list[int]]) -> None:
    """Write a DIMACS file."""
    with path.open('w') as f:
        f.write(f'p cnf {nv} {len(clauses)}\n')
        for c in clauses:
            f.write(' '.join(map(str, c)) + ' 0\n')


def solve(path: Path, seconds: int) -> set[int] | None:
    """Return the true variables of a kissat model, or None without a model."""
    exe = shutil.which('kissat')
    if exe is None:
        raise SystemExit('kissat is not on the PATH')
    run = subprocess.run(  # noqa: S603
        [exe, '-q', f'--time={seconds}', str(path)],
        capture_output=True,
        text=True,
        check=False,
    )
    if 's SATISFIABLE' not in run.stdout:
        print(
            'kissat:',
            's UNSATISFIABLE' if 's UNSATISFIABLE' in run.stdout else 'no verdict',
        )
        return None
    true = set()
    for line in run.stdout.splitlines():
        if line.startswith('v '):
            true |= {int(t) for t in line[2:].split() if int(t) > 0}
    return true


def main() -> int:
    """Parse the arguments, write the instance and optionally solve it."""
    parser = argparse.ArgumentParser(
        description='Write the SAT instances of the lead diagnostics.'
    )
    parser.add_argument('host', choices=['kab', 'kn'])
    parser.add_argument('sizes', type=int, nargs='+')
    parser.add_argument('--solve', type=int, default=0, metavar='SECONDS')
    args = parser.parse_args()
    _OUT.mkdir(exist_ok=True)
    if args.host == 'kab':
        a, b, n = args.sizes
        nv, clauses = kab_clauses(a, b, n)
        path = _OUT / f'kab_{a}_{b}_n{n}.cnf'

        def decode(true: set[int]) -> dict:
            rows = [
                ''.join('1' if j * a + i + 1 in true else '0' for i in range(a))
                for j in range(b)
            ]
            return {'n': n, 'a': a, 'b': b, 'rows': rows}

    else:
        size, n = args.sizes
        nv, clauses, edge = kn_clauses(size, n)
        path = _OUT / f'k{size}_n{n}.cnf'

        def decode(true: set[int]) -> dict:
            return {
                'n': n,
                'N': size,
                'red_edges': [list(edge[k]) for k in sorted(edge) if k in true],
            }

    write(path, nv, clauses)
    print(f'wrote {path.name}: {nv} variables, {len(clauses)} clauses')
    if args.solve:
        true = solve(path, args.solve)
        if true is not None:
            out = path.with_suffix('.json')
            out.write_text(json.dumps(decode(true), indent=1) + '\n')
            print(f'kissat: s SATISFIABLE; colouring written to {out.name}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

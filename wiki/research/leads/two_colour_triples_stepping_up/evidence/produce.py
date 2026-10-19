"""Optional finite synthesis of a two-colour prefix-selected one-bit lift.

Domain: all 2**M binary words; phi colours unordered coordinate pairs.
For p=max(delta(x,y),delta(y,z)), q=min(...), P=x>>(p+1),
colour = phi[p,q] XOR (delta(x,y)<delta(y,z)) XOR outsider[h(P,p,q)].
Queries h are in range(p). Search only the given finite M, target k.
An UNSAT result is solver-dependent and limited to that finite instance;
this program does not export or independently check an UNSAT certificate.
A SAT result is rechecked by integer evaluation and exhaustive clique search.
No outcome proves the uniform routing lemma. Timeout/unknown exits nonzero.

Uses the repository's z3-solver dependency, exact finite arithmetic, fixed
solver seed, and one thread. Dense mode adds every forbidden-set constraint;
--lazy adds constraints returned by exact clique searches. --bitvectors uses
a pure Boolean/bit-vector encoding instead of bounded integers. The dimension
is deliberately restricted to 2..6. Encoding time is outside --seconds;
the tested cases range from a second for M=3 to a few minutes for M=6.
Other cases may exhaust the cap. Dense constraint lists are size-limited.

From the repository root, a small discovery command is:
uv run --no-sync python <this-file> 4 5 --lazy --bitvectors --seconds 60
    --output <scratch-file.json>
The output must be ignored working storage, never the retained witness asset.
Only main.py verifies the separately retained sixteen-point witness.
"""

from __future__ import annotations

import argparse
import itertools
import json
import sys
import time
from math import comb
from pathlib import Path

import z3


def main() -> int:
    """Run one finite search; write diagnostic output, not a certificate."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('dimension', type=int)
    parser.add_argument('target', type=int)
    parser.add_argument('--seconds', type=int, default=60)
    parser.add_argument('--lazy', action='store_true')
    parser.add_argument('--bitvectors', action='store_true')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    m, k = args.dimension, args.target
    if not 2 <= m <= 6 or not 3 <= k <= (1 << m) or args.seconds <= 0:
        parser.error(
            'require 2 <= dimension <= 6, 3 <= target <= 2**dimension, seconds > 0'
        )
    if not args.lazy and comb(1 << m, k) > 100_000:
        parser.error('dense mode exceeds 100000 subsets; use --lazy')
    z3.set_param('parallel.enable', False)
    solver = z3.SolverFor('QF_BV') if args.bitvectors else z3.Solver()
    solver.set(timeout=args.seconds * 1000, random_seed=0)
    phi = {(p, q): z3.Bool(f'e_{p}_{q}') for p in range(m) for q in range(p)}
    selectors = {
        (p, prefix, q): (
            z3.BitVec(f'h_{p}_{prefix}_{q}', max(1, (p - 1).bit_length()))
            if args.bitvectors
            else z3.Int(f'h_{p}_{prefix}_{q}')
        )
        for p in range(1, m)
        for prefix in range(1 << (m - p - 1))
        for q in range(p)
    }
    for (p, _, _), h in selectors.items():
        if args.bitvectors:
            if p < (1 << h.size()):
                solver.add(z3.ULT(h, p))
        else:
            solver.add(h >= 0, h < p)
    triples = {}
    for x, y, z in itertools.combinations(range(1 << m), 3):
        a, b = (x ^ y).bit_length() - 1, (y ^ z).bit_length() - 1
        p, q = max(a, b), min(a, b)
        outsider = z if a < b else x
        h = selectors[(p, x >> (p + 1), q)]
        bit = z3.Or([h == j for j in range(p) if (outsider >> j) & 1])
        colour = z3.Bool(f'c_{x}_{y}_{z}')
        solver.add(colour == z3.Xor(phi[(p, q)], z3.Xor(a < b, bit)))
        triples[(x, y, z)] = colour

    def add_forbidden(vertices: tuple[int, ...]) -> None:
        colours = [triples[xyz] for xyz in itertools.combinations(vertices, 3)]
        solver.add(z3.Or(colours), z3.Or([z3.Not(c) for c in colours]))

    def find_cliques(
        colours: dict[tuple[int, int, int], int], target: int, limit: int = 64
    ) -> list[tuple[int, ...]]:
        """Exact extension search, retaining at most limit forbidden sets."""
        n = 1 << m
        links = {}
        for (x, y, z), c in colours.items():
            if c == target:
                links[(x, y)] = links.get((x, y), 0) | (1 << z)
        found = []

        def extend(current: list[int], candidates: int) -> None:
            if len(current) == k:
                found.append(tuple(current))
                return
            while candidates and len(found) < limit:
                if len(current) + candidates.bit_count() < k:
                    return
                bit = candidates & -candidates
                candidates ^= bit
                v = bit.bit_length() - 1
                after = candidates
                for u in current:
                    after &= links.get((u, v), 0)
                extend([*current, v], after)

        extend([], (1 << n) - 1)
        return found

    count = 0
    if not args.lazy:
        for vertices in itertools.combinations(range(1 << m), k):
            add_forbidden(vertices)
            count += 1
    started = time.monotonic()
    rounds = 0
    while True:
        left = args.seconds - (time.monotonic() - started)
        if left <= 0:
            status = z3.unknown
            break
        solver.set(timeout=max(1, int(left * 1000)))
        status = solver.check()
        rounds += 1
        if status != z3.sat or not args.lazy:
            break
        model = solver.model()
        actual = {xyz: int(z3.is_true(model.eval(c))) for xyz, c in triples.items()}
        forbidden = find_cliques(actual, 0) + find_cliques(actual, 1)
        if not forbidden:
            break
        for vertices in forbidden:
            add_forbidden(vertices)
            count += 1
    report = {
        'dimension': m,
        'target': k,
        'subsets': count,
        'rounds': rounds,
        'status': str(status),
        'seconds': time.monotonic() - started,
    }
    if status == z3.sat:
        model = solver.model()
        edge_values = {key: int(z3.is_true(model.eval(e))) for key, e in phi.items()}
        query_values = {key: model.eval(h).as_long() for key, h in selectors.items()}

        def colour(x: int, y: int, z: int) -> int:
            a, b = (x ^ y).bit_length() - 1, (y ^ z).bit_length() - 1
            p, q = max(a, b), min(a, b)
            outsider = z if a < b else x
            h = query_values[(p, x >> (p + 1), q)]
            return edge_values[(p, q)] ^ int(a < b) ^ ((outsider >> h) & 1)

        actual = {xyz: colour(*xyz) for xyz in triples}
        if find_cliques(actual, 0, 1) or find_cliques(actual, 1, 1):
            raise RuntimeError('invalid witness')
        maxima = []
        for target in (0, 1):
            best = []
            for size in range(k - 1, 1, -1):
                original_k, k = k, size
                best = find_cliques(actual, target, 1)
                k = original_k
                if best:
                    best = list(best[0])
                    break
            maxima.append(best)
        report.update(
            phi=[[*key, value] for key, value in edge_values.items()],
            selectors=[[*key, value] for key, value in query_values.items()],
            largest_monochromatic_witnesses=maxima,
        )
    elif status == z3.unknown:
        report['reason'] = solver.reason_unknown() or 'search time limit'
    report['solver_version'] = z3.get_version_string()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))
    return 2 if status == z3.unknown else 0


if __name__ == '__main__':
    sys.exit(main())

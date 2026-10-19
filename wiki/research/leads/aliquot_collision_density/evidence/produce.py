"""Write the census findings that ``main.py`` checks, as a proposed asset.

The program builds the census, runs it in the chosen flag modes through
``10^top`` and writes the findings to the output directory (default
``evidence/output/``). With the defaults (``--top 9``, both modes) the file
is ``census.json``; with ``--top 10 --modes 0`` it is ``census_1e10.json``.
The file is a proposal: it becomes the recorded asset of the same name only
when copied to ``assets/`` deliberately, and ``main.py`` then reproduces
every value it holds.

Run from the repository root:
    uv run --no-sync python wiki/research/leads/aliquot_collision_density/evidence/produce.py
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / 'util'))
import report

__all__ = [
    'main',
]

_HERE = Path(__file__).resolve().parent
_PREFIXES = ('D', 'DF', 'DN')


def main() -> int:
    """Run the census in the chosen modes and write the proposed findings file."""
    parser = argparse.ArgumentParser(description='Write the proposed census findings.')
    parser.add_argument(
        '--top', type=int, default=9, help='top exponent of the checkpoints'
    )
    parser.add_argument(
        '--modes', type=int, nargs='+', default=[0, 1], help='flag modes to run'
    )
    parser.add_argument(
        '--workdir', type=Path, default=_HERE / 'output', help='scratch directory'
    )
    args = parser.parse_args()
    exe = report.build(args.workdir / 'build')
    xs = report.checkpoints(args.top)
    hist_js = list(range(0, len(xs), 4))
    out: dict[str, object] = {}
    for mode in args.modes:
        rep = report.parse(
            report.run(exe, args.workdir / 'large', 22, xs, hist_js, mode)
        )
        classes = [f'{p}{k}' for p in _PREFIXES for k in range(16)]
        hist: dict[str, dict[str, list[list[int]]]] = {}
        for (j, c, t), v in sorted(rep['H'].items()):
            hist.setdefault(str(j), {c: [] for c in classes})[c].append([t, v])
        out[f'mode{mode}'] = {
            'checkpoints': xs,
            'R': {c: [rep['R'][c, j] for j in range(len(xs))] for c in classes},
            'C': {c: [rep['C'][c, j] for j in range(len(xs))] for c in classes},
            'H': hist,
            'primes': [rep['PRIMES'][j] for j in range(len(xs))],
            'omega2': [rep['OMEGA2'][j] for j in range(len(xs))],
        }
    target = args.workdir / (
        'census.json' if args.top == 9 else f'census_1e{args.top}.json'
    )
    target.write_text(json.dumps(out, separators=(',', ':')) + '\n')
    print(f'wrote {target}')
    return 0


if __name__ == '__main__':
    sys.exit(main())

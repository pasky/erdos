"""Check twenty stored flat targets and their bounded integer line preimages.

The input is ``assets/axis_flat_preimage_samples.json``: twenty records on
the boxes [3]^3 and [3]^4, each with a nonzero target vector b on the points
and a preimage vector a on the full axis lines. The checks are that every
record has entries in {-1, 0, 1} of the right lengths, that b is nonzero,
that the line combination with coefficients a equals b at every point, and
that b is annihilated by every quotient functional prod_i (1[x_i = r_i] -
1[x_i = d_i - 1]), so b lies in the line image. Arithmetic is exact
integer arithmetic; no solver or search runs, and the records are checked
exactly as stored.

Run from the repository root:
    uv run --no-sync python wiki/research/erdos_774/evidence/axis_flat_preimages/main.py

Dependencies are the standard library and the installed root ``tools``
package. The only input is the asset beside this script; no output file is
written and there is no reduced mode. Expected runtime is under a second.
Failed obligations exit nonzero, including under ``python -O``. Twenty
finite examples prove no four-direction preimage theorem.
"""

from __future__ import annotations

import json
import pathlib
import sys
from itertools import product
from math import prod

import tools

__all__ = [
    'main',
]

# locate the retained samples relative to this script
_ASSET = pathlib.Path(__file__).with_name('assets') / 'axis_flat_preimage_samples.json'


def main() -> int:
    """Run every finite obligation and return the shared checker's exit code."""
    # parse the fixed-domain interface and load the twenty records
    parser = tools.evidence_parser('Check the twenty stored flat preimages.', quick=False)
    parser.parse_args()
    checker = tools.Checker()
    records = json.loads(_ASSET.read_text())
    checker.check('exactly twenty records', len(records) == 20, f'observed {len(records)}')
    shape_failures = preimage_failures = quotient_failures = 0
    for record in records:
        dims = record['dimensions']
        if dims not in ([3, 3, 3], [3, 3, 3, 3]):
            shape_failures += 1
            continue
        points = list(product(*(range(d) for d in dims)))
        lines = [
            (i, fixed)
            for i in range(len(dims))
            for fixed in product(*(range(d) for j, d in enumerate(dims) if j != i))
        ]
        b, a = record['target'], record['preimage']
        if len(b) != len(points) or len(a) != len(lines):
            shape_failures += 1
            continue
        if not all(type(x) is int and abs(x) <= 1 for x in b + a) or not any(b):
            shape_failures += 1
            continue
        # check the line combination against the target at every point
        for x, target in zip(points, b):
            value = sum(
                coefficient
                for (i, fixed), coefficient in zip(lines, a)
                if tuple(x[j] for j in range(len(dims)) if j != i) == fixed
            )
            if value != target:
                preimage_failures += 1
                break
        # check that every quotient functional annihilates the target
        for r in product(*(range(d - 1) for d in dims)):
            value = sum(
                target * prod(int(x[i] == r[i]) - int(x[i] == dims[i] - 1) for i in range(len(dims)))
                for x, target in zip(points, b)
            )
            if value != 0:
                quotient_failures += 1
                break
    checker.check('every record has bounded integer entries of the right shape and a nonzero target', shape_failures == 0)
    checker.check('every preimage reproduces its target exactly', preimage_failures == 0, f'{preimage_failures} failures')
    checker.check('every target lies in the line image', quotient_failures == 0, f'{quotient_failures} failures')
    print('twenty fixed integer targets and bounded integer preimages verified exactly')
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

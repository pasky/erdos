"""Exercise the actual certificate consumer with corrupted small certificates.

The positive controls replay k=3,4. Each negative control changes one declared
constraint and must fail for the expected reason, both normally and under -O.
This is a failure-protocol check, not extra finite mathematical coverage.
"""

from __future__ import annotations

import argparse
import copy
import gzip
import json
import subprocess
import sys
import tempfile
from pathlib import Path

from tools import Checker

ROOT = Path(__file__).resolve().parent


def main() -> int:
    """Replay positive and discriminating negative controls in temporary output."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--assets', type=Path, default=ROOT / 'assets')
    args = parser.parse_args()
    checker = Checker()
    originals = {}
    for k in (3, 4):
        with gzip.open(args.assets / f'k{k:03d}.json.gz', 'rt') as stream:
            originals[k] = json.load(stream)
    cases = (
        ('right_inverse', 'right inverse identity fails'),
        ('zero_annihilator', 'zero modular annihilator'),
        ('wrong_predecessor', 'not at the required endpoint'),
        ('factor_two', 'inhomogeneous target fails'),
        ('wrong_cost', 'wrong recomputed solution cost'),
        ('support_boundary', 'invalid support'),
        ('wrong_shifts', 'wrong ordered shifts'),
        ('invalid_modulus', 'modulus must be at least two'),
        ('nonintegral_inverse', 'right inverse entry'),
        ('support_cap', 'solution endpoint outside domain'),
        ('endpoint_cap', 'endpoint violates dimension or cap'),
        ('missing_order', 'No such file'),
    )
    (ROOT / 'output').mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='controls_', dir=ROOT / 'output') as tmp:
        directory = Path(tmp)
        for optimized in (False, True):
            command = [sys.executable] + (['-O'] if optimized else [])
            command += [str(ROOT / 'main.py'), '--quick', '--assets', str(directory)]
            for name, expected in (
                ('positive', ''),
                ('composite_annihilator', ''),
                *cases,
            ):
                data = copy.deepcopy(originals)
                target = data[3]
                if name == 'composite_annihilator':
                    target['predecessor']['modulus'] *= 2
                    target['predecessor']['row'] = [
                        2 * value for value in target['predecessor']['row']
                    ]
                elif name == 'right_inverse':
                    target['right_inverse'][0][0] += 1
                elif name == 'zero_annihilator':
                    target['predecessor']['row'] = [0] * 6
                elif name == 'wrong_predecessor':
                    target['predecessor']['R'] += 1
                elif name == 'factor_two':
                    for pair in target['solutions'][0]['coefficients']:
                        pair[1] *= 2
                elif name == 'wrong_cost':
                    target['solutions'][0]['cost'] += 1
                elif name == 'support_boundary':
                    target['solutions'][0]['coefficients'][0][0] = target['B'] - 1
                elif name == 'wrong_shifts':
                    target['shifts'][-1] -= 1
                elif name == 'invalid_modulus':
                    target['predecessor']['modulus'] = 1
                elif name == 'nonintegral_inverse':
                    target['right_inverse'][0][0] = True
                elif name == 'support_cap':
                    target['solutions'][0]['R'] = 4097
                elif name == 'endpoint_cap':
                    target['minimal_R'] = 4097
                for k, certificate in data.items():
                    path = directory / f'k{k:03d}.json.gz'
                    path.write_bytes(
                        gzip.compress(json.dumps(certificate).encode(), mtime=0)
                    )
                if name == 'missing_order':
                    (directory / 'k004.json.gz').unlink()
                result = subprocess.run(
                    command, capture_output=True, text=True, check=False
                )
                if name in ('positive', 'composite_annihilator'):
                    passed = (
                        result.returncode == 0 and 'ALL CHECKS PASS' in result.stdout
                    )
                else:
                    passed = result.returncode != 0 and expected in result.stdout
                checker.check(
                    f'{name}, optimized={optimized}',
                    passed,
                    result.stdout + result.stderr,
                )
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

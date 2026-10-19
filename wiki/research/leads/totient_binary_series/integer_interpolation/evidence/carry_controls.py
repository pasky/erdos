"""Exercise the carry-criterion consumer with corrupted witness files.

The positive control replays the retained witnesses with --quick. Each
negative control changes one declared constraint and must fail for the
expected reason, both normally and under -O. This is a failure-protocol
check, not extra finite mathematical coverage.
"""

from __future__ import annotations

import argparse
import copy
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
    parser.add_argument(
        '--assets', type=Path, default=ROOT / 'assets' / 'carry_witnesses.json'
    )
    args = parser.parse_args()
    checker = Checker()
    with open(args.assets, encoding='utf-8') as stream:
        original = json.load(stream)
    cases = (
        ('shift_coefficient', 'aggregated tail integer'),
        ('drop_term', 'not divisible by 2^k'),
        ('wrong_cost', 'wrong recomputed witness cost'),
        ('support_below_k', 'invalid support'),
        ('zero_coefficient', 'contains zero'),
        ('zero_leading', 'leading coefficient must be nonzero'),
        ('boolean_entry', 'coefficient'),
        ('outside_box', 'wrong declared box specification'),
        ('duplicate_label', 'duplicate witness label'),
        ('duplicate_specification', 'duplicate witness specification'),
        ('missing_witness', 'missing witness specification'),
        ('missing_box', 'missing enumeration box'),
        ('changed_order', 'unexpected witness specification'),
        ('missing_file', 'No such file'),
    )
    (ROOT / 'output').mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(
        prefix='carry_controls_', dir=ROOT / 'output'
    ) as tmp:
        directory = Path(tmp)
        for optimized in (False, True):
            command = [sys.executable] + (['-O'] if optimized else [])
            command += [str(ROOT / 'carry.py'), '--quick', '--assets']
            for name, expected in (('positive', ''), *cases):
                data = copy.deepcopy(original)
                target = data['witnesses'][0]
                if name == 'shift_coefficient':
                    # Adding 2^k keeps v = 0 (mod 2^k) and breaks only W.
                    target['coefficients'][0][1] += 1 << target['k']
                elif name == 'drop_term':
                    # Remove the last term but keep cost consistent with W only.
                    target['coefficients'].pop()
                elif name == 'wrong_cost':
                    target['cost'] += 1
                elif name == 'support_below_k':
                    target['coefficients'][0][0] = target['k'] - 1
                elif name == 'zero_coefficient':
                    target['coefficients'][0][1] = 0
                elif name == 'zero_leading':
                    target['c'] = 0
                elif name == 'boolean_entry':
                    target['coefficients'][0][1] = True
                elif name == 'outside_box':
                    target['box'] = {'M': 1, 'h': 1}
                elif name == 'duplicate_label':
                    target['label'] = data['witnesses'][1]['label']
                elif name == 'duplicate_specification':
                    data['witnesses'].append(copy.deepcopy(target))
                elif name == 'missing_witness':
                    # Remove a high-order witness: --quick still checks the roster.
                    data['witnesses'].pop()
                elif name == 'missing_box':
                    target.pop('box')
                elif name == 'changed_order':
                    target['k'] = 7
                path = directory / f'{name}.json'
                if name != 'missing_file':
                    path.write_text(json.dumps(data))
                result = subprocess.run(  # noqa: S603
                    [*command, str(path)], capture_output=True, text=True, check=False
                )
                if name == 'positive':
                    passed = (
                        result.returncode == 0 and 'ALL CHECKS PASS' in result.stdout
                    )
                else:
                    passed = result.returncode != 0 and expected in result.stdout
                mode = 'optimized' if optimized else 'normal'
                checker.check(f'{mode} control {name}', passed, result.stdout[-400:])
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

"""Exercise the frozen order-26 checker's success and failure exits.

This is a runtime verification leg, not an independent calculation of the
weighted table. It copies only the retained main.py, util/certificate.py and
three JSON inputs into temporary directories, changes one specified input at a
time, and runs the unchanged checker in normal and optimized Python. The
baseline must succeed; each negative case must exit 1 for its intended reason.
A value-equivalent floating-point split is expected to be accepted, recording
the limit of the frozen metadata validator rather than claiming strict types.
No discovery program is read or executed. No cached result is read.

From the repository root after filing:
    nice -n 10 uv run --no-sync python wiki/theory/combinatorics/L78_bipartite_order_26_four_choosable/evidence/verify/check_failure_exits.py --subject wiki/theory/combinatorics/L78_bipartite_order_26_four_choosable/evidence/assets/review_subject --work-dir tmp/l78_failure_exit_review

Dependencies: the installed root tools package and the frozen checker's numpy.
Inputs: --subject/evidence/{main.py,util/certificate.py,assets/*.json}, with
the three asset names enumerated in FILES. Outputs are temporary files below
--work-dir, removed on completion. Runtime is normally several seconds. Every
failed obligation exits nonzero, including when this driver runs under -O.
All subprocesses run sequentially and inherit this driver's scheduling priority;
array-library thread counts are forced to one. No subprocess invokes uv, a
solver, or a repository gate.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import tools


FILES = (
    'main.py',
    'util/certificate.py',
    'assets/compact_certificate.json',
    'assets/certificates.json',
    'assets/controls.json',
)

CASES = (
    ('baseline', 0, 'ALL CHECKS PASS'),
    ('compact_arithmetic', 1,
     '[FAIL] total weight from profiles and subsets is 83424'),
    ('compact_domain', 1,
     '[FAIL] compact certificate domain and fixed lists'),
    ('auxiliary_zero', 1, '[FAIL] split (13,13):'),
    ('auxiliary_missing_split', 1,
     '[FAIL] one weighting for every split left = 2..24'),
    ('auxiliary_float_split', 0, 'ALL CHECKS PASS'),
    ('colourable_bad_control', 1,
     '[FAIL] control k3_nine: bad by exhaustion'),
    ('negative_weight', 1, 'ValueError: negative weight'),
    ('overflow_weight', 1,
     'ValueError: total weight too large for exact int64 sums'),
    ('noninteger_weight', 1, 'ValueError: malformed row'),
    ('malformed_assignment', 1,
     'ValueError: colour outside the palette or not an integer'),
)


def change_input(directory: Path, case: str) -> None:
    """Construct the exact negative input from the retained baseline assets."""
    if case == 'baseline':
        return
    if case.startswith('auxiliary_'):
        path = directory / 'assets/certificates.json'
    elif case in ('colourable_bad_control', 'malformed_assignment'):
        path = directory / 'assets/controls.json'
    else:
        path = directory / 'assets/compact_certificate.json'
    data = json.loads(path.read_text())
    if case == 'compact_arithmetic':
        data['weights'][0][3] = 6
    elif case == 'compact_domain':
        data['order'] = 25
    elif case == 'auxiliary_zero':
        next(s for s in data['splits'] if s['left'] == 13)['weights'] = []
    elif case == 'auxiliary_missing_split':
        data['splits'] = [s for s in data['splits'] if s['left'] != 24]
    elif case == 'auxiliary_float_split':
        split = next(s for s in data['splits'] if s['left'] == 13)
        split['left'] = 13.0
        split['right'] = 13.0
    elif case == 'colourable_bad_control':
        data['k3_nine']['right'] = data['k3_nine']['right'][1:]
    elif case == 'negative_weight':
        data['weights'][0][3] = -1
    elif case == 'overflow_weight':
        data['weights'][0][3] = 2**62
    elif case == 'noninteger_weight':
        data['weights'][0][3] = 0.5
    elif case == 'malformed_assignment':
        data['k2_k24']['left'][0][1] = True
    else:
        raise ValueError(f'unknown case {case}')
    path.write_text(json.dumps(data, indent=2) + '\n')


def main() -> int:
    parser = tools.evidence_parser(__doc__, quick=False)
    parser.add_argument('--subject', type=Path, required=True)
    parser.add_argument('--work-dir', type=Path, required=True)
    args = parser.parse_args()
    sources = {
        name: (args.subject / 'evidence' / name).read_bytes()
        for name in FILES
    }
    args.work_dir.mkdir(parents=True, exist_ok=True)
    environment = os.environ.copy()
    for name in (
        'OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
        'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS',
    ):
        environment[name] = '1'
    environment['PYTHONDONTWRITEBYTECODE'] = '1'
    environment['PYTHONPATH'] = str(Path(tools.__file__).resolve().parent.parent)
    checker = tools.Checker()
    for optimized in (False, True):
        mode = 'optimized' if optimized else 'normal'
        for case, expected_exit, expected_text in CASES:
            with tempfile.TemporaryDirectory(
                prefix='l78_failure_exit_', dir=args.work_dir,
            ) as temporary:
                directory = Path(temporary).resolve()
                for name, source in sources.items():
                    destination = directory / name
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    destination.write_bytes(source)
                change_input(directory, case)
                for name in ('main.py', 'util/certificate.py'):
                    if (directory / name).read_bytes() != sources[name]:
                        raise RuntimeError(f'checker source changed: {name}')
                command = [sys.executable, '-B']
                if optimized:
                    command.append('-O')
                command.append(str(directory / 'main.py'))
                result = subprocess.run(
                    command, env=environment, capture_output=True, text=True,
                    check=False,
                )
                output = result.stdout + result.stderr
                checker.check(
                    f'{mode}: {case} exits {expected_exit} for its intended reason',
                    result.returncode == expected_exit and expected_text in output,
                    f'exit={result.returncode}\n{output}',
                )
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

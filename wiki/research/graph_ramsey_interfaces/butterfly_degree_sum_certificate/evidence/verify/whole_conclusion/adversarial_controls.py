"""Replay explicit controls against the frozen and integer checkers.

Each case supplies its full JSON input and expected exit behavior. The frozen
program is copied byte-exact into --scratch and is never edited. Both ordinary
and optimized Python runs must show the named failed obligation when a failure
is expected. The sign-reversed case records an input-domain limitation of the
frozen checker; it is not a counterexample to the fixed mathematical subject.

Run from the repository root with uv run --no-sync python and --scratch set to
disposable storage. The scratch argument is mandatory so the retained evidence
is never used as an output directory. Runtime is a few seconds. Execution is
sequential; all result output comes from fresh subprocesses, never a cache.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess

from tools import Checker, evidence_parser


def main() -> int:
    parser = evidence_parser(__doc__, quick=False)
    parser.add_argument('--scratch', type=Path, required=True)
    parser.add_argument(
        '--controls',
        type=Path,
        default=Path(__file__).resolve().parent / 'assets/controls.json',
    )
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    evidence = here.parents[1]
    subject = evidence / 'assets/review_subject/evidence'
    frozen_code = (subject / 'main.py').read_bytes()
    controls = json.loads(args.controls.read_text())['cases']
    supplied = json.loads((subject / 'assets/parameters.json').read_text())
    check = Checker()
    if not check.check(
        'control baseline equals the retained supplied input',
        bool(controls)
        and controls[0]['name'] == 'supplied_parameters'
        and controls[0]['parameters'] == supplied,
    ):
        return check.finish()
    scratch = args.scratch.resolve()
    if scratch == evidence or evidence in scratch.parents:
        check.check('scratch lies outside retained evidence', False)
        return check.finish()
    scratch.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ)
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    env['PYTHONPATH'] = str(Path.cwd())
    for name in (
        'OMP_NUM_THREADS',
        'OPENBLAS_NUM_THREADS',
        'MKL_NUM_THREADS',
        'VECLIB_MAXIMUM_THREADS',
        'NUMEXPR_NUM_THREADS',
    ):
        env[name] = '1'
    for case in controls:
        name = case['name']
        if not name or any(c not in 'abcdefghijklmnopqrstuvwxyz_0123456789' for c in name):
            check.check('safe control name', False, repr(name))
            return check.finish()
        case_dir = scratch / name
        (case_dir / 'assets').mkdir(parents=True, exist_ok=True)
        program = case_dir / 'main.py'
        parameters = case_dir / 'assets/parameters.json'
        program.write_bytes(frozen_code)
        parameters.write_text(json.dumps(case['parameters'], indent=2) + '\n')
        if program.read_bytes() != frozen_code:
            check.check('byte-exact frozen control program', False, name)
            return check.finish()
        for optimize in (False, True):
            mode = 'optimized' if optimize else 'ordinary'
            prefix = ['uv', 'run', '--no-sync', 'python']
            if optimize:
                prefix.append('-O')
            commands = {
                'author': prefix + [str(program)],
                'recount': prefix
                + [str(here / 'integer_recount.py'), '--parameters', str(parameters)],
            }
            for kind, command in commands.items():
                result = subprocess.run(
                    command, env=env, text=True, capture_output=True, timeout=30
                )
                (case_dir / f'{kind}_{mode}.stdout.txt').write_text(result.stdout)
                (case_dir / f'{kind}_{mode}.stderr.txt').write_text(result.stderr)
                expected = case[f'{kind}_exit']
                failure = case[f'{kind}_failure']
                ok = result.returncode == expected and (
                    failure is None or f'[FAIL] {failure}' in result.stdout
                )
                check.check(
                    f'{name}: {kind} {mode} exit {expected}',
                    ok,
                    f'exit={result.returncode}; required failure={failure!r}',
                )
                if not ok:
                    print(result.stdout, end='')
                    print(result.stderr, end='')
    return check.finish()


if __name__ == '__main__':
    raise SystemExit(main())

"""Replay the unchanged examination with a bounded infrastructure import.

This adapter copies the retained grade_harness.py byte-for-byte into a temporary
tools/__init__.py. That source is the repository's evidence harness, containing
only Checker, evidence_parser, and a standard-library argparse import. It does
not import the root tools package's CLI or other initialization modules. This
is an explicitly adapted replay, not a verbatim canonical-source invocation.

The unchanged frozen main.py runs in normal and optimized modes; the unchanged
original check_failure_exits.py runs under optimization and tests both modes.
Exact commands, output and status are written below --work-dir for private
inspection. Temporary tools and mutation directories are removed afterwards.
No source or subject input is edited. Runs are sequential. Python, numpy and
the existing project environment must already be installed; no setup runs.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--subject', type=Path, required=True)
    parser.add_argument('--keeper', type=Path, required=True)
    parser.add_argument('--work-dir', type=Path, required=True)
    args = parser.parse_args()
    subject = args.subject.resolve()
    keeper = args.keeper.resolve()
    work = args.work_dir.resolve()
    work.mkdir(parents=True, exist_ok=True)
    source = Path(__file__).with_name('grade_harness.py').read_bytes()
    environment = os.environ.copy()
    environment['PYTHONDONTWRITEBYTECODE'] = '1'
    for name in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
                 'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
        environment[name] = '1'
    records = []
    failures = []
    with tempfile.TemporaryDirectory(prefix='adapted_replay_', dir=work) as directory:
        runtime = Path(directory)
        package = runtime / 'tools'
        package.mkdir()
        (package / '__init__.py').write_bytes(source)
        environment['PYTHONPATH'] = str(runtime)
        probe = [sys.executable, '-B', '-c',
                 'import tools,numpy,sys; print(tools.__file__); '
                 'print(sys.version); print(numpy.__version__)']
        commands = [
            ('environment', probe, None),
            ('checker_normal', [sys.executable, '-B', str(subject / 'evidence/main.py')],
             'ALL CHECKS PASS (65 checks)'),
            ('checker_optimized', [sys.executable, '-B', '-O', str(subject / 'evidence/main.py')],
             'ALL CHECKS PASS (65 checks)'),
            ('keeper_optimized', [sys.executable, '-B', '-O', str(keeper),
                                  '--subject', str(subject), '--work-dir', str(runtime / 'mutations')],
             'ALL CHECKS PASS (22 checks)'),
        ]
        for label, command, expected in commands:
            result = subprocess.run(command, cwd=runtime, env=environment,
                                    text=True, capture_output=True, check=False)
            output = result.stdout + result.stderr
            (work / (label + '.log')).write_text(output)
            valid = result.returncode == 0 and (expected is None or expected in output)
            if label == 'environment':
                valid = valid and result.stdout.splitlines()[0] == str(package / '__init__.py')
                valid = valid and (package / '__init__.py').read_bytes() == source
            records.append({'label': label, 'argv': command, 'cwd': str(runtime),
                            'PYTHONPATH': environment['PYTHONPATH'],
                            'exit': result.returncode, 'expected_summary': expected,
                            'accepted': valid})
            print(f"[{'ok' if valid else 'FAIL'}] {label}: exit {result.returncode}")
            if not valid:
                failures.append(label)
                print(output)
                if label == 'environment':
                    break
    (work / 'commands.private.json').write_text(json.dumps(records, indent=2)+'\n')
    return int(bool(failures))


if __name__ == '__main__':
    sys.exit(main())

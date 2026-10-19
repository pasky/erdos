"""Rerun both finite routes and their retained negative controls.

Use the repository's prepared interpreter through uv run --no-sync; launch this
file under nice -n 10. --output is mandatory and names disposable scratch.
All child computations use this same interpreter, one-thread settings, and no
bytecode writes. No repository command, Lean invocation, network access, or
corpus scan is performed. The author checker runs as an unchanged script file.

Each invocation re-executes both computations before comparison. Retained JSON
contains concrete count/witness/certificate data; cached success is never read.
The required finite domain is 28 rows representing 17,421 sign tuples. Negative
controls have three deliberately false minima and must exit 1 under Python -O.
Typical runtime is under one minute. Dependencies: Python standard library and
the supplied subject/tools_runtime closure for the author route alone.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def execute(command: list[str], environment: dict[str, str], out: Path, name: str) -> subprocess.CompletedProcess:
    result = subprocess.run(command, env=environment, capture_output=True, text=True, check=False)
    (out / (name + '_stdout.txt')).write_text(result.stdout)
    (out / (name + '_stderr.txt')).write_text(result.stderr)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    subject = root / 'subject'
    finite = root / 'finite'
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    environment = dict(os.environ)
    for key in ('PYTHONPATH', 'VIRTUAL_ENV', 'UV_PROJECT', 'UV_PROJECT_ENVIRONMENT',
                'UV_WORKING_DIR', 'UV_NO_PROJECT'):
        environment.pop(key, None)
    environment.update(PYTHONDONTWRITEBYTECODE='1', PYTHONHASHSEED='0')
    for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
                'NUMEXPR_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'BLIS_NUM_THREADS'):
        environment[key] = '1'
    author_environment = dict(environment)
    author_environment['PYTHONPATH'] = str(subject / 'tools_runtime')
    author = execute(
        [sys.executable, '-B', '-v', str(subject / 'finite/small_cases.py.txt'),
         '--output', str(out / 'author_results.json')],
        author_environment, out, 'author')
    require(author.returncode == 0, f'author checker exited {author.returncode}')
    manifest = json.loads((subject / 'manifest.json').read_text())
    expected = {
        (subject / item['path']).resolve()
        for item in manifest['allowed_files']
        if item['path'].startswith('tools_runtime/')
    }
    loaded = {
        Path(match.group(1)).resolve()
        for match in re.finditer(r'^# code object from (.*?/tools/.*\.py)$', author.stderr, re.M)
    }
    require(len(expected) == 17 and loaded == expected,
            'actual script invocation did not load exactly the supplied tools closure')
    independent = execute(
        [sys.executable, '-B', str(finite / 'independent.py'),
         '--input', str(finite / 'claims.json'),
         '--output', str(out / 'independent_results.json')],
        environment, out, 'independent')
    require(independent.returncode == 0, f'independent checker exited {independent.returncode}')
    negative = execute(
        [sys.executable, '-B', '-O', str(finite / 'independent.py'),
         '--input', str(finite / 'negative_claims.json'),
         '--output', str(out / 'negative_results.json')],
        environment, out, 'negative')
    require(negative.returncode == 1, f'negative controls exited {negative.returncode}, expected 1')
    author_data = json.loads((out / 'author_results.json').read_text())
    independent_data = json.loads((out / 'independent_results.json').read_text())
    negative_data = json.loads((out / 'negative_results.json').read_text())
    require(author_data == json.loads((subject / 'finite/small_cases_results.json').read_text()),
            'fresh author data differ from the original concrete fixture')
    require(author_data == json.loads((finite / 'author_results.json').read_text()),
            'fresh author data differ from retained rerun data')
    require(independent_data == json.loads((finite / 'results.json').read_text()),
            'fresh independent data differ from retained count/certificate data')
    require(negative_data == json.loads((finite / 'negative_results.json').read_text()),
            'fresh negative-control data differ from retained witnesses')
    require(author_data['records'] == independent_data['records'],
            'independent rows disagree with author rows')
    row_count = sum(len(record['rows']) for record in independent_data['records'])
    require(row_count == 28, 'finite domain does not contain the required 28 rows')
    require(author_data['total_colorings'] == independent_data['total_colorings_represented'] == 17421,
            'finite coloring-domain size differs')
    require(len(negative_data['failures']) == 3,
            'one of the three false minima was not rejected')
    result = {
        'fresh_rows': row_count,
        'colorings_represented': independent_data['total_colorings_represented'],
        'actual_script_tools_origins': sorted(str(path.relative_to(subject)) for path in loaded),
        'author_exit': author.returncode,
        'independent_exit': independent.returncode,
        'negative_control_exit': negative.returncode,
        'negative_control_failures': negative_data['failures'],
    }
    (out / 'verification.json').write_text(json.dumps(result, indent=2) + '\n')
    print('Fresh author and independent routes agree on all 28 count/witness rows.')
    print('All 17 tools origins belong to the supplied runtime closure.')
    print('All three false minima rejected under Python -O with exit 1.')
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, KeyError, TypeError, OSError) as error:
        print('ERROR: ' + str(error), file=sys.stderr)
        raise SystemExit(2) from error

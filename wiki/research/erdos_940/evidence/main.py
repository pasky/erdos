"""Run the retained exact certificates of the powerful-sum research on 940.

Each certificate is a standalone script under ``util/`` that exits nonzero
when one of its exact obligations fails. This entry point runs every
certificate in its own interpreter and records a nonzero exit as a failed
check. The certificates are:

- ``cubic_matrix_composition.py``: every coefficient of the cubic matrix
  identities, reduced modulo ``z^2 + z + 1`` in SymPy;
- ``quartic_residue_obstruction.py``: the exact lower bound above ``27/25``
  for the restricted 32-prescription objective, in integer and rational
  arithmetic;
- ``quintic_four_unit_extension.py``: the 70 four-unit coefficient profiles
  modulo 25 and the strengthened uniform unordered mean, in rational
  arithmetic;
- ``r5_first_moment.py``: the quintic progression first-moment bound, with
  integer convolutions in NumPy and rational comparisons in SymPy;
- ``representation_count_congruences.py``: the exact count of unordered
  exactly-five-part fifth-powerful representations through 100000 in NumPy,
  which finds a witness in every tested residue class.

Run from the repository root:
    uv run --no-sync --with numpy --with sympy python wiki/research/erdos_940/evidence/main.py

Dependencies are the standard library and the installed root ``tools``
package; the first, fourth and fifth certificates additionally need SymPy or
NumPy as stated and fail when the package is not installed, and neither is
declared by the repository, so the command above supplies both. There are no
file inputs, output files, random choices or reduced modes. Expected
runtime is a few minutes, dominated by the representation count. Failed
obligations exit nonzero, including under ``python -O``, because each
certificate runs in its own unoptimized interpreter. No certificate resolves
a density or infinitude case of Problem 940.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import tools

__all__ = [
    'run_probe',
    'main',
]

# locate the certificates
_UTIL = Path(__file__).resolve().parent / 'util'

# list every certificate with the packages beyond the standard library it needs
_PROBES = [
    ('cubic_matrix_composition.py', ('sympy',)),
    ('quartic_residue_obstruction.py', ()),
    ('quintic_four_unit_extension.py', ()),
    ('r5_first_moment.py', ('numpy', 'sympy')),
    ('representation_count_congruences.py', ('numpy',)),
]


def run_probe(script: str, dependencies: tuple[str, ...]) -> tuple[bool, str]:
    """Run one certificate in a fresh unoptimized interpreter and report."""
    # refuse to run a certificate whose declared dependency is missing
    for dependency in dependencies:
        probe = subprocess.run(
            [sys.executable, '-c', f'import {dependency}'],
            capture_output=True,
            text=True,
            check=False,
        )
        if probe.returncode != 0:
            return False, f'{dependency} is not installed'
    # run the certificate itself without inheriting an optimize flag
    env = {key: value for key, value in os.environ.items() if key != 'PYTHONOPTIMIZE'}
    result = subprocess.run(
        [sys.executable, str(_UTIL / script)],
        capture_output=True,
        text=True,
        check=False,
        env=env,
    )
    if result.stdout:
        print(result.stdout.rstrip())
    if result.returncode != 0:
        return False, f'exit {result.returncode}: {result.stderr.strip()[-300:]}'
    return True, ''


def main() -> int:
    """Run every certificate and return the shared checker's exit code."""
    # parse the fixed interface and run each certificate in order
    parser = tools.evidence_parser(
        'Run the retained exact certificates for Problem 940.', quick=False
    )
    parser.parse_args()
    checker = tools.Checker()
    for script, dependencies in _PROBES:
        ok, detail = run_probe(script, dependencies)
        checker.check(f'certificate {script} exits zero', ok, detail)
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

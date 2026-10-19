"""Check the exact 40-vector certificate excluding one candidate family.

The retained certificate ``assets/cube4.json`` partitions the 40 nonzero
antipodal representatives of the ternary four-dimensional cube into three
blocks and lists, for each block, dissociated six-subsets whose pairwise
unions cover every pair of the block. The probe ``util/check_cube4.py``
recomputes the representative set, checks every listed six-subset for
dissociation by enumerating its 64 signed sums, and checks the pair cover
of each block; the conclusion is that every 32-subset of the 40 vectors
contains a dissociated six-subset. This entry point runs the probe in its
own interpreter and records a nonzero exit as a failed check.

Run from the repository root:
    uv run --no-sync python wiki/research/erdos_963/evidence/main.py

Dependencies are the standard library and the installed root ``tools``
package. The only input is the retained JSON certificate; there are no
output files, random choices or reduced modes. Expected runtime is a few
seconds. Failed obligations exit nonzero, including under ``python -O``,
because the probe runs in its own unoptimized interpreter. The certificate
excludes this specific candidate family only and proves nothing about the
target of Problem 963.
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

# locate the probe and the certificate it reads
_EVIDENCE = Path(__file__).resolve().parent
_PROBE = _EVIDENCE / 'util' / 'check_cube4.py'
_CERTIFICATE = _EVIDENCE / 'assets' / 'cube4.json'


def run_probe() -> tuple[bool, str]:
    """Run the probe in a fresh unoptimized interpreter and report its exit."""
    # run the probe without inheriting an optimize flag
    env = {key: value for key, value in os.environ.items() if key != 'PYTHONOPTIMIZE'}
    result = subprocess.run(
        [sys.executable, str(_PROBE)],
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
    """Check the certificate's presence and the probe; return the exit code."""
    # parse the fixed interface and check the certificate is present
    parser = tools.evidence_parser(
        'Check the 40-vector dissociation certificate for Problem 963.',
        quick=False,
    )
    parser.parse_args()
    checker = tools.Checker()
    checker.check('certificate present', _CERTIFICATE.is_file(), str(_CERTIFICATE))

    # run the probe against the certificate
    ok, detail = run_probe()
    checker.check('probe check_cube4.py exits zero', ok, detail)
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

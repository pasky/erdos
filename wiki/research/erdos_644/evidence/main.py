"""Check the exact three-point constant-composition certificate for 644.

The retained certificate ``assets/couplings.json`` lists one representative
of each of the 16 orbits of vertices of the seven-dimensional probability
polytope ``Q_3`` under permutations of the three seed points, each written
as a convex combination of vectors ``(4 delta_I + 2 delta_J + delta_K)/7``
with ``I, J, K`` pairwise disjoint. The probe ``util/verify.py`` enumerates
all 6435 active-constraint choices with exact rational arithmetic, finds
exactly 52 vertices, checks every listed decomposition, and checks that the
orbits of the representatives are exactly those vertices. This entry point
runs the probe in its own interpreter and records a nonzero exit as a
failed check.

Run from the repository root:
    uv run --no-sync python wiki/research/erdos_644/evidence/main.py

Dependencies are the standard library and the installed root ``tools``
package. The only input is the retained JSON certificate; there are no
output files, random choices or reduced modes. Expected runtime is under a
minute. Failed obligations exit nonzero, including under ``python -O``,
because the probe runs in its own unoptimized interpreter. The certificate
checks only the finite three-point polytope inclusion and certifies neither
unrestricted assertion of Problem 644.
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
_PROBE = _EVIDENCE / 'util' / 'verify.py'
_CERTIFICATE = _EVIDENCE / 'assets' / 'couplings.json'


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
        'Check the three-point constant-composition certificate for 644.',
        quick=False,
    )
    parser.parse_args()
    checker = tools.Checker()
    checker.check('certificate present', _CERTIFICATE.is_file(), str(_CERTIFICATE))

    # run the probe against the certificate
    ok, detail = run_probe()
    checker.check('probe verify.py exits zero', ok, detail)
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

"""Run the retained finite probes of the rare-distance research on Problem 132.

Each probe is a standalone script under ``util/`` that exits nonzero when one
of its exact obligations fails. This entry point runs every probe in its own
interpreter, records a nonzero exit as a failed check, and then checks the
Eisenstein-grid enumeration's written results against the table recorded on
the motif page. The probes are:

- ``continuation_checks.py``: the thirteen-point hexagram spectrum and degree
  profile, a six-point invariant-shell spectrum, and the deletion-critical
  meanders at ``K = 3, 5, 9``, in exact integer and rational arithmetic;
- ``valuation_counterexample.py``: the six-, nine- and five-point examples
  refuting a valuation-maximum lemma, in exact arithmetic;
- ``mixed_valuation_selector.py``: the six-point mixed-valuation obstruction,
  in exact rational arithmetic;
- ``eisenstein_grid.py``: the exhaustive enumeration of all nonempty subsets
  of the 4-by-4 Eisenstein grid, whose results it writes under ``output/``;
- ``c3_hex_candidates_exact.py``: the finite quadratic table of the
  unreviewed thirteen-point rotational report, which needs SymPy;
- ``split_class_example.py``: the rigid split-class example of the
  split-class note for ``m = 2..7``, in exact arithmetic over
  ``Q(sqrt2, sqrt3)``.

Run from the repository root:
    uv run --no-sync python wiki/research/erdos_132/evidence/main.py

Dependencies are the standard library and the installed root ``tools``
package; the rotational probe additionally needs SymPy and fails when it is not
installed. There are no file inputs, random choices or reduced modes; the
only file written is the grid enumeration's JSON under ignored ``output/``.
Expected runtime is under two minutes, dominated by the grid enumeration.
Failed obligations exit nonzero, including under ``python -O``, because each
probe runs in its own unoptimized interpreter. No probe proves either
unrestricted assertion of Problem 132.
"""

from __future__ import annotations

import json
import math
import os
import subprocess
import sys
from pathlib import Path

import tools

__all__ = [
    'run_probe',
    'main',
]

# locate the probes and the enumeration's written results
_EVIDENCE = Path(__file__).resolve().parent
_UTIL = _EVIDENCE / 'util'
_GRID_RESULTS = _EVIDENCE / 'output' / 'eisenstein_grid_results.json'

# list every probe with the dependency beyond the standard library it needs
_PROBES = [
    ('continuation_checks.py', None),
    ('valuation_counterexample.py', None),
    ('mixed_valuation_selector.py', None),
    ('eisenstein_grid.py', None),
    ('c3_hex_candidates_exact.py', 'sympy'),
    ('split_class_example.py', None),
]

# retain the motif page's table: order -> (minimum R in the grid, minimizers)
_GRID_TABLE = {
    5: (2, 72),
    6: (2, 32),
    7: (2, 4),
    8: (3, 105),
    9: (3, 56),
    10: (3, 59),
    11: (2, 6),
    12: (3, 6),
    13: (3, 12),
    14: (3, 1),
    15: (4, 2),
    16: (5, 1),
}

# count the subsets the enumeration examines: all nonempty, then all of size >= 5
_NONEMPTY_SUBSETS = (1 << 16) - 1
_LARGE_SUBSETS = _NONEMPTY_SUBSETS - sum(
    math.comb(16, size) for size in range(1, 5)
)


def run_probe(script: str, dependency: str | None) -> tuple[bool, str]:
    """Run one probe in a fresh unoptimized interpreter and report its exit."""
    # refuse to run a probe whose declared dependency is missing
    if dependency is not None:
        probe = subprocess.run(
            [sys.executable, '-c', f'import {dependency}'],
            capture_output=True,
            text=True,
            check=False,
        )
        if probe.returncode != 0:
            return False, f'{dependency} is not installed'
    # run the probe itself without inheriting an optimize flag
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
    """Run every probe and the grid-table comparison; return the exit code."""
    # parse the fixed interface and run each probe in order
    parser = tools.evidence_parser(
        'Run the retained finite probes for Problem 132.', quick=False
    )
    parser.parse_args()
    checker = tools.Checker()
    for script, dependency in _PROBES:
        ok, detail = run_probe(script, dependency)
        checker.check(f'probe {script} exits zero', ok, detail)

    # compare the enumeration's written results with the recorded table
    if not _GRID_RESULTS.is_file():
        checker.check('grid results written', False, f'missing {_GRID_RESULTS}')
        return checker.finish()
    results = json.loads(_GRID_RESULTS.read_text())
    checker.check(
        'grid enumeration covers every nonempty subset',
        results['examined_nonempty'] == _NONEMPTY_SUBSETS
        and results['examined_n_ge_5'] == _LARGE_SUBSETS,
        f"observed {results['examined_nonempty']}, {results['examined_n_ge_5']}",
    )
    checker.check(
        'grid enumeration finds no subset with R <= 1',
        not results['counterexamples'],
        f"observed {len(results['counterexamples'])} counterexamples",
    )
    observed = {
        int(order): (entry['R'], entry['count'])
        for order, entry in results['minimum_R_by_n'].items()
    }
    checker.check(
        'grid minima and minimizer counts match the motif table',
        observed == _GRID_TABLE,
        f'observed {observed}',
    )
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())

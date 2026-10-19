"""Behavior test for the suite's refusal of a temporary folder inside a checkout."""

from __future__ import annotations

import os
import pathlib
import subprocess
import sys

import pytest

from ._helpers import run_git

__all__ = ['test_a_temporary_folder_inside_a_checkout_stops_the_run']

_ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_a_temporary_folder_inside_a_checkout_stops_the_run(
    tmp_path: pathlib.Path,
) -> None:
    """A run with TMPDIR inside a Git checkout stops before any test, naming both."""
    checkout = tmp_path / 'checkout'
    temporary = checkout / 'tmp'
    temporary.mkdir(parents=True)
    run_git(checkout, 'init', '-q')
    env = {**os.environ, 'TMPDIR': str(temporary)}
    env.pop('PYTEST_DEBUG_TEMPROOT', None)
    result = subprocess.run(
        [
            sys.executable,
            '-m',
            'pytest',
            '-p',
            'no:cacheprovider',
            'tests/test_import.py',
        ],
        cwd=_ROOT,
        env=env,
        capture_output=True,
        text=True,
    )
    assert result.returncode == pytest.ExitCode.USAGE_ERROR, result.stdout
    message = ' '.join(result.stderr.split())
    assert (
        f"pytest's temporary folder {temporary.resolve()} is inside the Git "
        f'checkout {checkout.resolve()}'
    ) in message
    assert 'unset TMPDIR' in message

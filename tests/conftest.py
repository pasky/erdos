"""Keep the test suite from writing bytecode under the corpus or running inside a checkout."""

from __future__ import annotations

import os
import pathlib
import sys
import tempfile

import pytest

# Tests load corpus evidence by path, in process and in subprocesses that build
# their environment from ``os.environ``; a rename would otherwise leave an
# orphaned parent folder holding only ignored bytecode. The package ``__init__``
# imports this module first, before any test module is imported.
sys.dont_write_bytecode = True
os.environ.setdefault('PYTHONDONTWRITEBYTECODE', '1')


def pytest_configure(config: pytest.Config) -> None:
    """Refuse a run whose temporary folder lies inside a Git checkout."""
    # the fixtures under such a folder find the enclosing repository, and the
    # ops tests attribute their processes to its worktree; the folder is the
    # one pytest resolves: --basetemp, else its debug root, else the system's
    temporary = pathlib.Path(
        config.option.basetemp
        or os.environ.get('PYTEST_DEBUG_TEMPROOT')
        or tempfile.gettempdir()
    ).resolve()
    for folder in (temporary, *temporary.parents):
        if (folder / '.git').exists():
            raise pytest.UsageError(
                f"pytest's temporary folder {temporary} is inside the Git "
                f'checkout {folder}, where test fixtures find that repository; '
                'unset TMPDIR (and drop --basetemp) so the run uses the '
                "system's temporary folder"
            )

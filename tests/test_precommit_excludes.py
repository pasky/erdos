"""Behavior tests for the pre-commit exclude that keeps hooks off what they must not rewrite."""

from __future__ import annotations

import pathlib
import re
import subprocess

import pytest
import yaml

from tools.core.files import precommit_coverage

__all__ = [
    'test_hooks_skip_every_canonical_slot_and_convert_tree_but_not_result_pages',
    'test_hooks_skip_the_evidence_records_and_lean_apart_from_its_gate_surfaces',
    'test_only_the_repository_layout_passes_the_layout_hook',
]

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_CONFIG = _ROOT / '.pre-commit-config.yaml'
# real pages beside a canonical that the hooks must keep checking
_THEOREM = (
    'library/irrationality/bell_2026_mahler_series_multiplicative_coefficients'
    '/theorem_1_3.md'
)
_CARD = (
    'library/irrationality/bell_2026_mahler_series_multiplicative_coefficients'
    '/_index.md'
)
# real evidence records and Lean files, each with whether the hooks skip it
_RECORDS = [
    # an evidence folder's assets, Markdown included, however deep the folder
    (
        'library/discrete_geometry/cambie_kalviainen_2026_small_step_walk'
        '/evidence/assets/reviewed_problem.md',
        True,
    ),
    (
        'wiki/research/erdos_809/evidence/assets/publication/comparator.json',
        True,
    ),
    # the verify tree apart from its Markdown report pages
    (
        'library/set_systems/li_2025_erdos_lovasz_problem_3_critical'
        '/evidence/verify/bitmask_result.json',
        True,
    ),
    (
        'library/distance_problems/sallerk_2026_convex_nonagon_relations'
        '/evidence/verify/verify_quartic.py',
        True,
    ),
    ('wiki/research/erdos_416/evidence/verify/grade.md', False),
    # the Lean project apart from its README and the three gate scripts
    ('lean/README.md', False),
    ('lean/scripts/audit_selftest.sh', False),
    ('lean/scripts/gate.sh', False),
    ('lean/scripts/selftest_digest.sh', False),
    ('lean/scripts/selftest.stamp', True),
    ('lean/lakefile.toml', True),
    ('lean/Erdos/Core.lean', True),
]


def test_hooks_skip_every_canonical_slot_and_convert_tree_but_not_result_pages() -> (
    None
):
    """The hooks skip each PDF's slot and .convert/, and nothing beside."""
    # the configuration's top-level files and exclude patterns decide what reaches
    # the hooks
    covers = precommit_coverage(_ROOT)

    # the slot is the PDF's path with .md, as the wiki exclude builder derives it
    pdfs = sorted(_ROOT.glob('library/*/*/*.pdf'))
    assert len(pdfs) > 0
    slots = [pdf.with_suffix('.md').relative_to(_ROOT).as_posix() for pdf in pdfs]
    assert [slot for slot in slots if covers(slot)] == []

    # the converter's working directory beside the PDF is skipped as a whole
    convert = (
        f'{pathlib.PurePosixPath(slots[0]).parent}/.convert/{pdfs[0].stem}/page_1.md'
    )
    assert not covers(convert)

    # result pages and the card stay under the hooks
    for page in (_THEOREM, _CARD):
        assert (_ROOT / page).is_file(), page
        assert covers(page), page


@pytest.mark.parametrize(('page', 'skipped'), _RECORDS)
def test_hooks_skip_the_evidence_records_and_lean_apart_from_its_gate_surfaces(
    page: str, skipped: bool
) -> None:
    """The hooks skip the records and keep the pages."""
    assert (_ROOT / page).is_file(), page
    assert precommit_coverage(_ROOT)(page) is not skipped


def test_only_the_repository_layout_passes_the_layout_hook() -> None:
    """Every tracked path passes the layout hook, and a node's records at the root fail it."""
    # pre-commit hands a path to a hook when the configuration's top-level
    # filters cover it and the hook's own exclude leaves it, and the fail hook
    # rejects every path
    config = yaml.safe_load(_CONFIG.read_text(encoding='utf-8'))
    hook = next(
        hook
        for repo in config['repos']
        for hook in repo['hooks']
        if hook['id'] == 'reject-paths-outside-the-layout'
    )
    assert hook['language'] == 'fail'
    covers = precommit_coverage(_ROOT)
    allowed = re.compile(hook['exclude']).search

    def rejected(path: str) -> bool:
        return covers(path) and not allowed(path)

    tracked = subprocess.run(
        ['git', 'ls-files', '-z'],
        cwd=_ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.split('\0')
    assert [path for path in filter(None, tracked) if rejected(path)] == []
    for stray in ('memory/frontier.md', 'plans/grading.md', 'frontier.md'):
        assert rejected(stray), stray

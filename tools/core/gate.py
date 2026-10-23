"""Functions for the repository's non-mathematical gate battery.

The battery checks generated repository structure, every wiki root, page
references, repository tests and package doctests, and working files.
Mathematical evidence is never discovered or executed. Native Lean validation is
expensive and therefore opt-in, with an explicit visible skip otherwise:
``--lean`` runs it, ``--lean-if-changed`` runs it unless the validated-tree
receipt (``lean/.lake/validated.json``) already names the prospective ``lean/``
tree, ``--intake`` skips the repository tests for a merge whose later full
battery runs them, and ``--strict`` fails a leg whose required tool is
unavailable instead of skipping it.
"""

from __future__ import annotations

import dataclasses
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import time
from typing import Optional

import tools.core.audits
import tools.core.claim_refs
import tools.core.files
import tools.core.ledger
import tools.core.problem_claims
import tools.core.problem_layout
import tools.core.reflint
from tools.constants import (
    LIBRARY_DIR,
    MATH_DIR,
    PROBLEM_LINKS_BEGIN,
    PROBLEM_LINKS_END,
    WIKI_ROOTS,
)

__all__ = [
    'LegResult',
    'run_gate',
]

# select the index page of each four-digit catalog folder one subject below the problem root
_PROBLEM_GLOB = '*/E[0-9][0-9][0-9][0-9]/_index.md'
# keep each pre-commit run's arguments and inherited environment within a
# quarter of the smallest host argument limit (ARG_MAX, 1 MiB on macOS):
# pre-commit diffs the whole tree around every hook of every run, so a few large
# runs cost far less than many small ones
_PRECOMMIT_ARGUMENT_BYTES = 256 * 1024
# the words of each pre-commit run ahead of its files
_PRECOMMIT_COMMAND = ('pre-commit', 'run', '--color=never', '--files')
# keep each failed command's diagnostic tail within the gate summary
_OUTPUT_TAIL_LIMIT = 400
# keep each failed hook's own output within the gate summary, by the same budget
_HOOK_OUTPUT_LIMIT = _OUTPUT_TAIL_LIMIT
# match a hook's status line in pre-commit's report: its name, the dot leader,
# then the outcome
_HOOK_STATUS = re.compile(
    r'\.{3}(?:\(no files to check\))?(?P<outcome>Passed|Failed|Skipped)$'
)
# pre-commit's line naming a reported hook, directly under its status line
_HOOK_ID = '- hook id: '
# pre-commit's note on a hook during which the whole tree's diff changed
_HOOK_MODIFIED = 'files were modified by this hook'
# keep a failed batch's first written files within the gate summary, as the
# reference lint keeps its first findings
_WRITTEN_FILE_LIMIT = 10
# keep the first findings of the reference lint, library licenses and problem
# claims legs within the gate summary; each leg's command lists them all
_REFLINT_FINDING_LIMIT = 10
# validated-tree receipt the conditional Lean leg honors, relative to the root
_LEAN_RECEIPT = 'lean/.lake/validated.json'
# schema version the receipt carries
_LEAN_RECEIPT_VERSION = 2
# runtime content kept out of the lean/ fingerprint
_LEAN_RUNTIME = ('lean/.lake',)


@dataclasses.dataclass(frozen=True)
class LegResult:
    """Outcome of one gate leg."""

    name: str
    state: str
    detail: str = ''
    # the outcome came from a missing required tool or script; strict mode fails
    # a SKIPPED leg carrying this mark and leaves deliberate skips alone
    unavailable: bool = False

    @property
    def failed(self: LegResult) -> bool:
        """Return whether the leg blocks the battery."""
        return self.state == 'FAIL'


def run_gate(
    root: pathlib.Path,
    *,
    problems: tuple[str, ...] = (),
    lean: bool = False,
    lean_if_changed: bool = False,
    precommit: bool = True,
    intake: bool = False,
    strict: bool = False,
    settled: bool = False,
) -> list[LegResult]:
    """Run the repository battery at ``root`` and return per-leg outcomes.

    ``lean`` runs the Lean leg unconditionally and refreshes its validated-tree
    receipt; ``lean_if_changed`` runs it only when the prospective ``lean/``
    tree differs from the receipt's; ``intake`` skips the repository tests, a
    deliberate skip, for a merge whose later full battery runs them; ``strict``
    fails a leg whose required tool is unavailable instead of skipping it;
    ``settled`` makes a problem whose provisional standing rests on no claim
    page a failure of the problem claims leg instead of a count in the leg's
    detail (the release mode).
    """
    # check generated corpus structure
    root = root.resolve()
    legs = [
        _problem_layout_leg(root),
        _problem_claims_leg(root, settled=settled),
        _problem_links_leg(root, problems),
        _builder_leg(
            root,
            name='library subjects',
            script='scripts/build_library_subjects.py',
            arguments=(
                '--wiki',
                MATH_DIR,
                '--library',
                LIBRARY_DIR,
                '--taxonomy',
                'scripts/taxonomy.json',
            ),
        ),
        _builder_leg(
            root,
            name='wiki excludes',
            script='scripts/build_wiki_excludes.py',
            arguments=('--library', LIBRARY_DIR),
        ),
    ]
    legs.append(_library_licenses_leg(root))
    legs.extend(_claim_legs(root))

    # check navigation and lint for each wiki root
    for wiki_root in WIKI_ROOTS:
        legs.append(_wiki_leg(root, wiki_root))

    # check the repository's page references
    legs.append(_reflint_leg(root))

    # run tests and the remaining repository checks
    if intake:
        legs.append(LegResult('pytest', 'SKIPPED', 'disabled by --intake'))
    elif not (root / 'pyproject.toml').is_file():
        legs.append(LegResult('pytest', 'FAIL', 'missing pyproject.toml'))
    else:
        pytest = _run_binary(
            'python',
            '-m',
            'pytest',
            '-c',
            'pyproject.toml',
            '-q',
            cwd=root,
        )
        legs.append(_command_leg('pytest', pytest))
    legs.append(_precommit_leg(root, enabled=precommit))
    legs.append(_lean_leg(root, lean=lean, lean_if_changed=lean_if_changed))
    # fail, instead of skipping, any leg whose required tool was missing
    if strict:
        legs = [_strict(leg) for leg in legs]
    return legs


# ------ helper functions


def _problem_layout_leg(root: pathlib.Path) -> LegResult:
    """Check problem-page structure without awarding assessment credit."""
    # require the mathematics root
    if not (root / MATH_DIR).is_dir():
        return LegResult('problem layout', 'FAIL', f'missing required {MATH_DIR}/ root')
    try:
        findings, notes = tools.core.problem_layout.lint_problem_layout(root)
    except (OSError, ValueError) as error:
        return LegResult('problem layout', 'FAIL', str(error))
    return LegResult(
        'problem layout',
        'FAIL' if findings else 'PASS',
        '; '.join([*findings, *notes]),
    )


def _problem_claims_leg(root: pathlib.Path, *, settled: bool) -> LegResult:
    """Check the problem and claim pages against the claims schema."""
    # require the mathematics root
    if not (root / MATH_DIR).is_dir():
        return LegResult('problem claims', 'FAIL', f'missing required {MATH_DIR}/ root')
    try:
        findings, notes = tools.core.problem_claims.lint_problem_claims(
            root, settled=settled
        )
    except (OSError, ValueError) as error:
        return LegResult('problem claims', 'FAIL', str(error))
    # keep the first findings in the summary and point at the command, in the
    # same mode, that lists them all
    command = 'erdos problem-claims --settled' if settled else 'erdos problem-claims'
    shown = findings[:_REFLINT_FINDING_LIMIT]
    if len(findings) > len(shown):
        more = len(findings) - len(shown)
        shown.append(f'... {more} more (run `{command}` for the full list)')
    # count the library dependences the command lists, ahead of the counts and
    # the disclaimer that end the notes
    *dependencies, counts, disclaimer = notes
    if dependencies:
        shown.append(
            f'{len(dependencies)} library dependence(s) (run `{command}` to list them)'
        )
    return LegResult(
        'problem claims',
        'FAIL' if findings else 'PASS',
        '; '.join([*shown, counts, disclaimer]),
    )


def _library_licenses_leg(root: pathlib.Path) -> LegResult:
    """Check every card's license terms against the files it holds and the holding policy."""
    # require the mathematics root
    if not (root / MATH_DIR).is_dir():
        return LegResult(
            'library licenses', 'FAIL', f'missing required {MATH_DIR}/ root'
        )
    try:
        findings, notes = tools.core.audits.audit_library_licenses(root)
    except (OSError, RuntimeError, ValueError) as error:
        return LegResult('library licenses', 'FAIL', str(error))
    # keep the first findings in the summary and point at the full list
    shown = findings[:_REFLINT_FINDING_LIMIT]
    if len(findings) > len(shown):
        more = len(findings) - len(shown)
        shown.append(f'... {more} more (run `erdos license-audit` for the full list)')
    return LegResult(
        'library licenses',
        'FAIL' if findings else 'PASS',
        '; '.join([*shown, *notes]),
    )


def _claim_legs(root: pathlib.Path) -> list[LegResult]:
    """Check native metadata once before the generated view and manifest join."""
    # require the mathematics root
    if not (root / MATH_DIR).is_dir():
        missing = f'missing required {MATH_DIR}/ root'
        return [
            LegResult('native claim ledger', 'FAIL', missing),
            LegResult('native claim references', 'FAIL', missing),
        ]
    # invalid metadata cannot become a successful empty reference scan
    try:
        claims = tools.core.ledger.scan_claims(root)
    except (OSError, ValueError) as error:
        return [
            LegResult('native claim ledger', 'FAIL', '; '.join(str(error).split('\n'))),
            LegResult('native claim references', 'FAIL', 'blocked by invalid metadata'),
        ]

    # check the derived views without rewriting them
    try:
        findings = tools.core.ledger.lint_views(root, claims=claims)
    except OSError as error:
        findings = [str(error)]
    ledger = LegResult(
        'native claim ledger',
        'FAIL' if findings else 'PASS',
        '; '.join(findings) if findings else f'{len(claims)} native claim(s)',
    )

    # the available manifest is a reference surface, not a fresh kernel check
    try:
        findings, notes = tools.core.claim_refs.lint_claim_refs(root, claims=claims)
    except OSError as error:
        findings, notes = [str(error)], []
    references = LegResult(
        'native claim references',
        'FAIL' if findings else 'PASS',
        '; '.join([*findings, *notes, 'manifest freshness not checked']),
    )
    return [ledger, references]


def _problem_links_leg(
    root: pathlib.Path,
    requested: tuple[str, ...],
) -> LegResult:
    """Check the selected incoming-link blocks and count the pages without one."""
    # require the mathematics root
    if not (root / MATH_DIR).is_dir():
        return LegResult(
            'problem library links', 'FAIL', f'missing required {MATH_DIR}/ root'
        )
    # find managed pages without adding blocks to unmanaged pages
    pages = sorted((root / MATH_DIR / 'problems').glob(_PROBLEM_GLOB))
    selected = set(requested)
    marker_bearing = set()
    missing = 0
    for page in pages:
        text = page.read_text(encoding='utf-8')
        has_begin = PROBLEM_LINKS_BEGIN in text
        has_end = PROBLEM_LINKS_END in text
        if has_begin or has_end:
            marker_bearing.add(page.parent.name)
        else:
            missing += 1
    # merge explicitly requested pages into the checked scope
    selected.update(marker_bearing)
    chosen = sorted(selected)
    scope = _problem_scope_detail(len(chosen), missing)
    if not chosen:
        return LegResult('problem library links', 'SKIPPED', scope)

    # check only the selected pages
    arguments = [
        '--wiki',
        MATH_DIR,
        '--library',
        LIBRARY_DIR,
        '--taxonomy',
        'scripts/taxonomy.json',
    ]
    for problem in chosen:
        arguments.extend(('--problem', problem))
    result = _run_script(
        root,
        'scripts/build_problem_library_links.py',
        *arguments,
        '--check',
    )
    if result.returncode == 0:
        return LegResult('problem library links', 'PASS', scope)
    return LegResult(
        name='problem library links',
        state='FAIL',
        detail=f'{scope}; {_tail(result)}',
        unavailable=result.returncode == 127,
    )


def _builder_leg(
    root: pathlib.Path,
    *,
    name: str,
    script: str,
    arguments: tuple[str, ...],
) -> LegResult:
    """Run one Python builder in check mode over its wiki root."""
    # require the mathematics root
    if not (root / MATH_DIR).is_dir():
        return LegResult(name, 'FAIL', f'missing required {MATH_DIR}/ root')
    result = _run_script(root, script, *arguments, '--check')
    return _command_leg(name, result)


def _wiki_leg(root: pathlib.Path, wiki_root: str) -> LegResult:
    """Check generated navigation and lint one required wiki root.

    The lint reads ``wiki lint --json``: an issue fails the leg, and so does a
    stale wikilink, which the wiki tool reports as a ``link_stale`` note; every
    other note stays advisory.
    """
    # require the wiki root
    name = f'wiki {wiki_root}'
    if not (root / wiki_root).is_dir():
        return LegResult(name, 'FAIL', f'missing required {wiki_root}/ root')
    # check generated navigation, skipping visibly when the tool is missing
    update = _run_binary('wiki', 'update', '--path', wiki_root, '--check', cwd=root)
    if update.returncode == 127:
        return LegResult(name, 'SKIPPED', 'wiki unavailable', unavailable=True)
    if update.returncode:
        return LegResult(name, 'FAIL', f'update: {_tail(update)}')
    # lint authored wiki content: an issue or a stale wikilink fails the leg
    lint = _run_binary('wiki', 'lint', '--path', wiki_root, '--json', cwd=root)
    try:
        report = json.loads(lint.stdout)
        findings = [row['text'] for row in report['issues']]
        findings.extend(
            row['text'] for row in report['notes'] if row['kind'] == 'link_stale'
        )
    except (ValueError, KeyError, TypeError):
        return LegResult(name, 'FAIL', f'lint: {_tail(lint)}')
    if findings:
        return LegResult(name, 'FAIL', f'lint: {_lint_detail(findings)}')
    if lint.returncode:
        return LegResult(name, 'FAIL', f'lint: {_tail(lint)}')
    return LegResult(name, 'PASS')


def _reflint_leg(root: pathlib.Path) -> LegResult:
    """Check retired page names and inline links over the repository Markdown."""
    # a listing Git cannot give fails the leg, as it fails the pre-commit leg,
    # and so does a root or page the lint cannot read
    try:
        findings, notes = tools.core.reflint.lint_references(root)
    except RuntimeError as error:
        return LegResult('reflint', 'FAIL', f'working-file enumeration: {error}')
    except (OSError, ValueError) as error:
        return LegResult('reflint', 'FAIL', str(error))
    # keep the first findings in the summary and point at the full list
    shown = findings[:_REFLINT_FINDING_LIMIT]
    if len(findings) > len(shown):
        more = len(findings) - len(shown)
        shown.append(f'... {more} more (run `erdos reflint` for the full list)')
    return LegResult(
        'reflint',
        'FAIL' if findings else 'PASS',
        '; '.join([*shown, *notes]),
    )


def _precommit_leg(root: pathlib.Path, *, enabled: bool) -> LegResult:
    """Run pre-commit on every existing working file in bounded batches."""
    # check whether the leg can run
    if not enabled:
        return LegResult('pre-commit', 'SKIPPED', 'disabled by --no-precommit')
    if not (root / '.pre-commit-config.yaml').is_file():
        return LegResult('pre-commit', 'FAIL', 'missing .pre-commit-config.yaml')
    # enumerate authoritative working-file coverage under the configuration's
    # own top-level filters
    covers = tools.core.files.precommit_coverage(root)
    try:
        covered = [
            name
            for name in (
                path.relative_to(root).as_posix()
                for path in tools.core.files.repository_files(root)
            )
            if covers(name)
        ]
    except RuntimeError as error:
        return LegResult('pre-commit', 'FAIL', f'working-file enumeration: {error}')

    # run hooks in batches within the argument budget, timing each run, and
    # collect failures
    failures = []
    for batch in _precommit_batches(covered):
        began = time.time_ns()
        result = _run_binary(*_PRECOMMIT_COMMAND, *batch, cwd=root)
        ended = time.time_ns()
        if result.returncode == 127:
            return LegResult(
                'pre-commit', 'SKIPPED', 'pre-commit unavailable', unavailable=True
            )
        if result.returncode:
            failures.append(_precommit_failure(root, result, batch, began, ended))
    if failures:
        return LegResult('pre-commit', 'FAIL', '; '.join(failures))
    return LegResult('pre-commit', 'PASS', f'{len(covered)} file(s)')


def _precommit_batches(names: list[str]) -> list[list[str]]:
    """Split the covered files into pre-commit runs within the argument budget."""
    # every run carries the environment and the command words, then its files
    fixed = sum(
        _argument_bytes(f'{key}={value}') for key, value in os.environ.items()
    ) + sum(_argument_bytes(word) for word in _PRECOMMIT_COMMAND)
    batches: list[list[str]] = []
    size = fixed
    for name in names:
        if batches and size + _argument_bytes(name) <= _PRECOMMIT_ARGUMENT_BYTES:
            batches[-1].append(name)
            size += _argument_bytes(name)
        else:
            batches.append([name])
            size = fixed + _argument_bytes(name)
    return batches


def _argument_bytes(text: str) -> int:
    """Return what one argument or environment entry costs against ARG_MAX."""
    # its bytes, its terminating NUL and its pointer, as pre-commit counts them
    return len(os.fsencode(text)) + 1 + 8


def _precommit_failure(
    root: pathlib.Path,
    result: subprocess.CompletedProcess,
    batch: list[str],
    began: int,
    ended: int,
) -> str:
    """Describe a failed batch by its failed hooks and the files written meanwhile.

    pre-commit reports that a hook modified files when the whole tree's
    ``git diff`` changed while it ran, so another process writing a tracked
    file or changing the index fails whichever hook is running. The hooks see
    only the batch's files: a batch file written during the run is most likely
    a fixing hook's rewrite, and any other file was written by another process.
    """
    # report each failed hook; output naming no hook, such as an error before
    # any hook ran, keeps its tail
    hooks = _failed_hooks(result.stdout)
    parts = [
        f'hook {hook} failed ({"; ".join(notes)})' + (f': {output}' if output else '')
        for hook, notes, output in hooks
    ] or [_tail(result)]
    # name the files written while the batch ran, in and outside the batch
    written = _written_files(root, batch, began, ended)
    members = set(batch)
    rewrites = [name for name in written if name in members]
    others = [name for name in written if name not in members]
    if rewrites:
        parts.append(
            'written in the batch during the run (a fixing hook rewrites in '
            f'place; review and commit): {_file_list(rewrites)}'
        )
    if others:
        parts.append(
            'written outside the batch during the run (another writer; leave '
            f'the tree alone while the gate runs): {_file_list(others)}'
        )
    if not written and any(_HOOK_MODIFIED in notes for _, notes, _ in hooks):
        parts.append(
            'nothing written during the run (another process changed the index '
            'or deleted a file)'
        )
    return '; '.join(parts)


def _failed_hooks(report: str) -> list[tuple[str, list[str], str]]:
    """Return each failed hook's id, notes and bounded output from pre-commit."""
    lines = report.splitlines()
    hooks = []
    for index, line in enumerate(lines):
        # a failed hook's status line is followed by its id, its notes (exit
        # code, modified files) and, after a blank line, its own output
        status = _HOOK_STATUS.search(line)
        if status is None or status['outcome'] != 'Failed':
            continue
        if index + 1 == len(lines) or not lines[index + 1].startswith(_HOOK_ID):
            continue
        body = []
        for line in lines[index + 2 :]:
            if _HOOK_STATUS.search(line):
                break
            body.append(line)
        notes = []
        while body and body[0].startswith('- '):
            notes.append(body.pop(0).removeprefix('- '))
        output = ' '.join(' '.join(body).split())
        if len(output) > _HOOK_OUTPUT_LIMIT:
            output = output[:_HOOK_OUTPUT_LIMIT] + ' ...'
        hooks.append((lines[index + 1].removeprefix(_HOOK_ID), notes, output))
    return hooks


def _written_files(
    root: pathlib.Path,
    batch: list[str],
    began: int,
    ended: int,
) -> list[str]:
    """Return the batch and tracked files whose status changed during a run."""
    # pre-commit's modification check sees the tracked files; the hooks see
    # the batch, untracked files included
    listing = subprocess.run(
        ['git', 'ls-files', '-z'],
        cwd=root,
        capture_output=True,
        text=True,
    )
    names = {*batch, *filter(None, listing.stdout.split('\0'))}
    # every write sets a file's change time, which no writer can set back
    written = []
    for name in sorted(names):
        try:
            changed = (root / name).lstat().st_ctime_ns
        except OSError:
            continue
        if began <= changed <= ended:
            written.append(name)
    return written


def _file_list(names: list[str]) -> str:
    """Name the first written files and count the rest."""
    shown = names[:_WRITTEN_FILE_LIMIT]
    more = len(names) - len(shown)
    return ', '.join(shown) + (f' ... {more} more' if more else '')


def _lean_leg(
    root: pathlib.Path,
    *,
    lean: bool,
    lean_if_changed: bool,
) -> LegResult:
    """Run the opt-in Lean launcher, keeping the validated-tree receipt.

    The launcher owns the build, audit, and stamp checks. The prospective
    ``lean/`` tree is fingerprinted first; when there is none (no Git checkout,
    or Git cannot produce the tree) the launcher simply runs and the detail says
    why. When only ``lean_if_changed`` is requested and the receipt already
    names that tree, the leg skips. After the launcher passes, the receipt is
    written only when the fingerprint recomputed afterwards still matches:
    inputs that changed during validation fail the leg, since the validated
    bytes are not the bytes a commit would record, and leave no receipt behind.
    """
    # disclose the opt-in boundary
    name = 'lean build+audit+stamp'
    if not (lean or lean_if_changed):
        return LegResult(
            name=name,
            state='SKIPPED',
            detail=(
                'heavy leg; run with --lean or --lean-if-changed'
                ' (skipped is never certified)'
            ),
        )
    # fingerprint the prospective lean/ tree, runtime content excluded
    before, reason = _fingerprint(root)
    # honor a receipt naming exactly this tree
    conditional = lean_if_changed and not lean
    if conditional and before is not None and before == _read_receipt(root):
        return LegResult(
            name=name,
            state='SKIPPED',
            detail=f'unchanged inputs previously validated (receipt {_LEAN_RECEIPT})',
        )

    # run the authoritative Lean launcher
    launcher = root / 'lean' / 'scripts' / 'gate.sh'
    if not launcher.is_file():
        return LegResult(name, 'FAIL', 'missing lean/scripts/gate.sh')
    result = _run_binary('bash', 'scripts/gate.sh', cwd=root / 'lean')
    if result.returncode:
        return LegResult(
            name=name,
            state='FAIL',
            detail=_tail(result),
            unavailable=result.returncode == 127,
        )
    checked = 'build, audit, and self-test stamp checked'

    # record the validated tree only when there is one and the inputs held still
    if before is None:
        return LegResult(name, 'PASS', f'{checked}; {reason}; no receipt written')
    after, _ = _fingerprint(root)
    if after != before:
        return LegResult(
            name=name,
            state='FAIL',
            detail=(
                'inputs under lean/ changed during validation; rerun the gate'
                ' (no receipt written)'
            ),
        )
    _write_receipt(root, before)
    return LegResult(name, 'PASS', f'{checked}; receipt written ({_LEAN_RECEIPT})')


def _fingerprint(root: pathlib.Path) -> tuple[Optional[str], str]:
    """Return the prospective ``lean/`` tree id and, when there is none, why.

    Outside a Git checkout the reason is fixed; when Git cannot produce the tree
    inside one (a ``lean/`` holding no trackable content, an index Git refuses
    to read) the reason carries Git's message, so the leg never mislabels a
    checkout as absent.
    """
    # fingerprint the prospective lean/ tree, runtime content excluded
    try:
        tree = tools.core.files.prospective_tree(root, 'lean', exclude=_LEAN_RUNTIME)
    except RuntimeError as error:
        return None, f'no prospective lean/ tree ({error})'
    # outside a checkout there is no tree to record
    if tree is None:
        return None, 'not a git checkout'
    return tree, ''


def _read_receipt(root: pathlib.Path) -> Optional[str]:
    """Return the tree id the validated-tree receipt names, else ``None``.

    A missing, unreadable, malformed, or other-version receipt reads as
    ``None``, so the full launcher runs again before its result is trusted.
    """
    # a missing receipt certifies nothing
    path = root / _LEAN_RECEIPT
    if not path.is_file():
        return None
    # parse the record, treating any defect as absence
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except (OSError, ValueError):
        return None
    if not isinstance(data, dict):
        return None
    if data.get('version') != _LEAN_RECEIPT_VERSION:
        return None
    tree = data.get('tree')
    if not isinstance(tree, str):
        return None
    return tree


def _write_receipt(root: pathlib.Path, tree: str) -> None:
    """Record ``tree`` as the validated ``lean/`` tree in the receipt file."""
    # write the record under the ignored Lake cache directory
    path = root / _LEAN_RECEIPT
    path.parent.mkdir(parents=True, exist_ok=True)
    data = {'version': _LEAN_RECEIPT_VERSION, 'tree': tree}
    path.write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')


def _strict(leg: LegResult) -> LegResult:
    """Return ``leg`` failed when it skipped for a missing required tool."""
    if leg.state == 'SKIPPED' and leg.unavailable:
        return dataclasses.replace(
            leg, state='FAIL', detail=f'{leg.detail} (required under --strict)'
        )
    return leg


def _run_script(
    root: pathlib.Path,
    script: str,
    *arguments: str,
) -> subprocess.CompletedProcess:
    """Run a required repository Python script, returning 127 when absent."""
    if not (root / script).is_file():
        return subprocess.CompletedProcess(
            args=(script, *arguments),
            returncode=127,
            stdout=f'missing {script}',
            stderr='',
        )
    return _run_binary('python', script, *arguments, cwd=root)


def _run_binary(
    name: str,
    *arguments: str,
    cwd: pathlib.Path,
) -> subprocess.CompletedProcess:
    """Run a console script venv-first, then on ``PATH``; return 127 if absent."""
    # resolve the binary from the invoking environment first
    if name == 'python':
        binary = sys.executable
    else:
        executable = pathlib.Path(sys.executable)
        binary = shutil.which(name, path=f'{executable.parent}') or shutil.which(name)
    # report missing dependencies without silently skipping their legs
    if binary is None:
        return subprocess.CompletedProcess(
            args=(name, *arguments),
            returncode=127,
            stdout=f'{name} unavailable',
            stderr='',
        )
    return subprocess.run(
        [binary, *arguments],
        cwd=cwd,
        capture_output=True,
        text=True,
    )


def _command_leg(name: str, result: subprocess.CompletedProcess) -> LegResult:
    """Convert one subprocess result to a blocking gate outcome."""
    if result.returncode == 0:
        return LegResult(name, 'PASS')
    return LegResult(
        name=name,
        state='FAIL',
        detail=_tail(result),
        unavailable=result.returncode == 127,
    )


def _lint_detail(findings: list[str], limit: int = 500) -> str:
    """Keep wiki lint's failing findings, issues first, within the summary budget."""
    text = ' '.join('; '.join(findings).split())
    return text[:limit] + (' ...' if len(text) > limit else '')


def _problem_scope_detail(checked: int, missing: int) -> str:
    """Render the incoming-link scope without implying mathematical review."""
    return (
        f'checked {checked} problem(s); {missing} canonical problem page(s) '
        'have no managed block (no library page links them, or a new link '
        'awaits its block; markers are structural, not mathematical acceptance)'
    )


def _tail(
    result: subprocess.CompletedProcess,
    limit: int = _OUTPUT_TAIL_LIMIT,
) -> str:
    """Return a subprocess's final output characters folded to one line."""
    text = (result.stdout + result.stderr).strip()
    return ' '.join(text[-limit:].split()) or f'exit {result.returncode}'

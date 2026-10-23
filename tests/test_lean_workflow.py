"""Test Lean workflow scripts with real scratch projects and an external Lake stub."""

from __future__ import annotations

import json
import os
import pathlib
import shutil
import subprocess

import pytest

__all__ = [
    'test_in_place_gate_requires_compiled_dependencies',
    'test_gate_rejects_invalid_arguments_before_lake',
    'test_clean_gate_validates_the_selected_archive',
    'test_clean_gate_rejects_a_fetch_without_compiled_dependencies',
    'test_gate_rejects_failed_digest_with_empty_stamp',
    'test_gate_rejects_a_build_that_uses_sorry',
    'test_gate_refuses_sources_the_audit_cannot_see',
    'test_selftest_preserves_existing_probe_paths',
    'test_cold_selftest_creates_no_probe_or_stamp',
    'test_selftest_rejects_missing_expect',
    'test_selftest_admit_fixture_needs_pass_and_report',
    'test_selftest_runs_check_fixtures_under_check',
    'test_selftest_failures_print_output_and_keep_the_stamp',
    'test_selftest_requires_every_expected_fragment',
    'test_selftest_places_compiler_records_by_structure',
    'test_selftest_rejects_a_print_fixture_without_records',
    'test_digest_is_independent_of_locale',
    'test_digest_tracks_only_refusal_inputs',
    'test_lake_calls_receive_the_thread_cap',
    'test_invalid_thread_caps_fail_before_lake',
]

#: the axiom name a native_decide proof of `Erdos.L9995.claim` mints
_MINTED = 'Erdos.L9995.claim._native.native_decide.ax_1'

#: the launcher's refusal of a source that could hide the sorry warning
_SILENCED = "could silence the build's sorry warning"

#: the launcher's refusal of an example's compiler-evaluated decision
_COMPILED = 'compiler-evaluated decision'


# ------ fixtures


@pytest.fixture
def shell_environment(tmp_path: pathlib.Path) -> dict[str, str]:
    """Confine fake Lake calls, Git configuration, and shell temp files to pytest."""
    binary = tmp_path / 'bin' / 'lake'
    _write(
        binary,
        '#!/bin/sh\n'
        'set -eu\n'
        'printf "%s|%s|%s|%s\\n" "$*" "$PWD" '
        '"$(cat Erdos/Basic.lean)" "${LEAN_NUM_THREADS:-unset}" '
        '>> "$LEAN_TEST_CALLS"\n'
        'case "$*" in\n'
        '  "exe cache get")\n'
        '    if [ "$LEAN_TEST_FETCH" = warm ]; then\n'
        '      mkdir -p .lake/packages/mathlib/.lake/build/lib/lean\n'
        '      printf "compiled fixture\\n" > '
        '.lake/packages/mathlib/.lake/build/lib/lean/Mathlib.olean\n'
        '    fi ;;\n'
        '  build)\n'
        '    if [ "$LEAN_TEST_BUILD" = edit ]; then\n'
        '      printf "%s\\n" "-- edited during the run" >> Audit/alpha.lean\n'
        '    elif [ "$LEAN_TEST_BUILD" = sorry ]; then\n'
        "      echo 'warning: Erdos/Basic.lean:1:8: declaration uses `sorry`'\n"
        '    elif [ "$LEAN_TEST_BUILD" = probe-error ] &&\n'
        '        [ -f Erdos/AuditSelfTestProbe.lean ]; then\n'
        '      echo "fixture build error"; exit 1\n'
        '    fi ;;\n'
        '  "exe audit"|"exe audit --check"|"exe audit --print")\n'
        '    if [ -f Erdos/AuditSelfTestProbe.lean ]; then\n'
        '      if grep -q "^-- MODE: admit$" Erdos/AuditSelfTestProbe.lean; then\n'
        '        if [ "$LEAN_TEST_ADMIT" != silent ]; then\n'
        '          echo "NOTE fixture admitted"\n'
        '        fi\n'
        '        if [ "$LEAN_TEST_ADMIT" = refuse ]; then exit 1; fi\n'
        '      elif grep -q "^-- MODE: print$" Erdos/AuditSelfTestProbe.lean; then\n'
        '        echo "NOTE fixture admitted"\n'
        '        if [ -f "$LEAN_TEST_MANIFEST" ]; then cat "$LEAN_TEST_MANIFEST"; fi\n'
        '        echo "AUDIT PASS"\n'
        '      elif grep -q "^-- MODE: check$" Erdos/AuditSelfTestProbe.lean; then\n'
        '        if [ "$*" = "exe audit --check" ]; then\n'
        '          echo "FAIL fixture stale"; exit 1\n'
        '        fi\n'
        '      elif [ "$LEAN_TEST_REFUSAL" = pass ]; then\n'
        '        echo "fixture audit passed"\n'
        '      elif [ "$LEAN_TEST_REFUSAL" = mismatch ]; then\n'
        '        echo "FAIL another refusal"; exit 1\n'
        '      else\n'
        '        echo "FAIL fixture refusal"; exit 1\n'
        '      fi\n'
        '    elif [ "$LEAN_TEST_CONTROL" = fail ] && [ "$*" = "exe audit --check" ]; then\n'
        '      echo "FAIL control audit error"; exit 1\n'
        '    fi ;;\n'
        '  *) echo "unexpected lake command: $*" >&2; exit 2 ;;\n'
        'esac\n',
    )
    binary.chmod(0o755)
    temporary = tmp_path / 'runtime'
    temporary.mkdir()
    return {
        'PATH': f'{binary.parent}{os.pathsep}{os.defpath}',
        'LC_ALL': 'C',
        'TMPDIR': str(temporary),
        'GIT_CONFIG_GLOBAL': os.devnull,
        'GIT_CONFIG_SYSTEM': os.devnull,
        'GIT_TERMINAL_PROMPT': '0',
        'LEAN_TEST_CALLS': str(tmp_path / 'lake-calls.log'),
        'LEAN_TEST_FETCH': 'warm',
        'LEAN_TEST_BUILD': 'clean',
        'LEAN_TEST_ADMIT': 'report',
        'LEAN_TEST_REFUSAL': 'report',
        'LEAN_TEST_CONTROL': 'pass',
        'LEAN_TEST_MANIFEST': str(tmp_path / 'printed-manifest.json'),
    }


@pytest.fixture
def lean_project(
    tmp_path: pathlib.Path,
    shell_environment: dict[str, str],
) -> pathlib.Path:
    """Copy the working scripts and create a stamp only for this synthetic project."""
    lean = tmp_path / 'repository' / 'lean'
    source = pathlib.Path(__file__).resolve().parents[1] / 'lean' / 'scripts'
    shutil.copytree(
        source,
        lean / 'scripts',
        ignore=shutil.ignore_patterns('selftest.stamp', 'selftest'),
    )
    for relative, content in {
        '.gitignore': '.lake/\n',
        'lean-toolchain': 'fixture-toolchain\n',
        'lakefile.toml': 'name = "fixture"\n',
        'lake-manifest.json': '{}\n',
        'Audit/Zeta.lean': '-- upper-case audit source\n',
        'Audit/alpha.lean': '-- lower-case audit source\n',
        'Erdos/Basic.lean': '-- first revision\n',
        'scripts/selftest/refusal.lean': '-- EXPECT: fixture refusal\n',
    }.items():
        _write(lean / relative, content)
    _stamp(lean, shell_environment)
    return lean


# ------ gate lifecycle


@pytest.mark.parametrize(
    argnames='cache',
    argvalues=['missing', 'lib/Mathlib.olean', 'lib/lean/Mathlib.olean'],
)
def test_in_place_gate_requires_compiled_dependencies(
    lean_project: pathlib.Path,
    shell_environment: dict[str, str],
    cache: str,
) -> None:
    """Build and audit warm projects, but refuse a source-only Mathlib checkout."""
    _write(lean_project / '.lake/packages/mathlib/Mathlib.lean', '-- source only\n')
    if cache != 'missing':
        _write(lean_project / '.lake/packages/mathlib/.lake/build' / cache, 'object\n')
    result = _run(lean_project, shell_environment)
    calls = _calls(shell_environment)
    if cache == 'missing':
        assert result.returncode != 0
        assert 'binary cache is missing' in result.stdout + result.stderr
        assert calls == []
    else:
        assert result.returncode == 0, result.stdout + result.stderr
        assert calls == [
            f'build|{lean_project.resolve()}|-- first revision|4',
            f'exe audit --check|{lean_project.resolve()}|-- first revision|4',
        ]


@pytest.mark.parametrize(
    argnames='arguments',
    argvalues=[
        ['--unknown'],
        ['HEAD'],
        ['--clean', '--help'],
        ['--clean', 'HEAD', 'extra'],
        ['--clean', 'missing-revision'],
        ['--clean', 'HEAD^{tree}'],
    ],
    ids=[
        'unknown-option',
        'bare-revision',
        'option-revision',
        'extra',
        'missing',
        'tree',
    ],
)
def test_gate_rejects_invalid_arguments_before_lake(
    lean_project: pathlib.Path,
    shell_environment: dict[str, str],
    arguments: list[str],
) -> None:
    """Invalid syntax and non-commit revisions must fail before any Lake command."""
    _git(lean_project.parent, shell_environment, 'init', '-b', 'main')
    _git(lean_project.parent, shell_environment, 'add', 'lean')
    _git(lean_project.parent, shell_environment, 'commit', '-m', 'Fixture')
    result = _run(lean_project, shell_environment, *arguments)
    assert result.returncode != 0, result.stdout + result.stderr
    assert _calls(shell_environment) == []


@pytest.mark.parametrize('revision', ['default', 'HEAD^'])
def test_clean_gate_validates_the_selected_archive(
    lean_project: pathlib.Path,
    shell_environment: dict[str, str],
    revision: str,
) -> None:
    """Run the selected commit's launcher, harness, digest, and stamp on its sources."""
    root = lean_project.parent
    _git(root, shell_environment, 'init', '-b', 'main')
    _git(root, shell_environment, 'add', 'lean')
    _git(root, shell_environment, 'commit', '-m', 'First fixture revision')
    _write(lean_project / 'Erdos/Basic.lean', '-- second revision\n')
    _write(lean_project / 'Audit/alpha.lean', '-- changed audit source\n')
    _stamp(lean_project, shell_environment)
    _git(root, shell_environment, 'add', 'lean')
    _git(root, shell_environment, 'commit', '-m', 'Second fixture revision')

    # A working-tree launcher, harness, or digest would fail, and its stamp
    # cannot validate either archive.
    _write(lean_project / 'Erdos/Basic.lean', '-- uncommitted source\n')
    _write(lean_project / 'scripts/selftest.stamp', 'uncommitted stamp\n')
    for script in ('gate.sh', 'audit_selftest.sh', 'selftest_digest.sh'):
        path = lean_project / 'scripts' / script
        _write(path, path.read_text(encoding='utf-8') + '\nexit 97\n')
    arguments = ['--clean'] if revision == 'default' else ['--clean', revision]
    result = _run(lean_project, shell_environment, *arguments)
    assert result.returncode == 0, result.stdout + result.stderr
    calls = [line.split('|') for line in _calls(shell_environment)]
    expected = '-- second revision' if revision == 'default' else '-- first revision'
    assert [command for command, _, _, _ in calls] == [
        'exe cache get',
        'build',
        'exe audit --check',
        'build',
        'exe audit',
        'build',
        'exe audit --check',
    ]
    assert {source for _, _, source, _ in calls} == {expected}
    assert {cap for _, _, _, cap in calls} == {'4'}
    directories = {pathlib.Path(cwd).resolve() for _, cwd, _, _ in calls}
    assert len(directories) == 1
    archive = directories.pop()
    assert archive != lean_project.resolve()
    assert not archive.exists()
    assert (lean_project / 'Erdos/Basic.lean').read_text(encoding='utf-8') == (
        '-- uncommitted source\n'
    )
    assert (lean_project / 'scripts/selftest.stamp').read_text(encoding='utf-8') == (
        'uncommitted stamp\n'
    )


def test_clean_gate_rejects_a_fetch_without_compiled_dependencies(
    lean_project: pathlib.Path,
    shell_environment: dict[str, str],
) -> None:
    """A successful cache command alone must not authorize a Mathlib source build."""
    _git(lean_project.parent, shell_environment, 'init', '-b', 'main')
    _git(lean_project.parent, shell_environment, 'add', 'lean')
    _git(lean_project.parent, shell_environment, 'commit', '-m', 'Fixture')
    shell_environment['LEAN_TEST_FETCH'] = 'empty'
    result = _run(lean_project, shell_environment, '--clean')
    assert result.returncode != 0
    assert 'binary cache is missing' in result.stdout + result.stderr
    calls = [line.split('|') for line in _calls(shell_environment)]
    assert [(command, cap) for command, _, _, cap in calls] == [('exe cache get', '4')]
    assert not pathlib.Path(calls[0][1]).exists()


def test_gate_rejects_failed_digest_with_empty_stamp(
    lean_project: pathlib.Path,
    shell_environment: dict[str, str],
) -> None:
    """A silent digest failure must not match an empty stamp and pass validation."""
    _write(
        lean_project / '.lake/packages/mathlib/.lake/build/lib/lean/Mathlib.olean',
        'object\n',
    )
    stamp = lean_project / 'scripts/selftest.stamp'
    _write(stamp, '')
    _write(lean_project / 'scripts/selftest_digest.sh', '#!/bin/sh\nexit 1\n')
    result = _run(lean_project, shell_environment)
    assert result.returncode != 0, result.stdout + result.stderr
    assert 'Lean gate passed.' not in result.stdout
    assert stamp.read_bytes() == b''


@pytest.mark.parametrize('mode', ['in-place', 'clean'])
def test_gate_rejects_a_build_that_uses_sorry(
    lean_project: pathlib.Path,
    shell_environment: dict[str, str],
    mode: str,
) -> None:
    """Fail on a sorry warning, the only trace an example's sorry leaves, before auditing."""
    _write(
        lean_project / '.lake/packages/mathlib/.lake/build/lib/lean/Mathlib.olean',
        'object\n',
    )
    if mode == 'clean':
        _git(lean_project.parent, shell_environment, 'init', '-b', 'main')
        _git(lean_project.parent, shell_environment, 'add', 'lean')
        _git(lean_project.parent, shell_environment, 'commit', '-m', 'Fixture')
    shell_environment['LEAN_TEST_BUILD'] = 'sorry'
    arguments = ['--clean'] if mode == 'clean' else []
    result = _run(lean_project, shell_environment, *arguments)
    assert result.returncode != 0, result.stdout + result.stderr
    assert 'declaration uses `sorry`' in result.stderr
    assert 'Lean gate passed.' not in result.stdout
    commands = [line.split('|')[0] for line in _calls(shell_environment)]
    assert commands[-1] == 'build'
    assert 'exe audit --check' not in commands


@pytest.mark.parametrize(
    argnames=('path', 'source', 'refusal'),
    argvalues=[
        ('Erdos/Probe.lean', 'set_option warn.sorry false\n', _SILENCED),
        ('Erdos/Probe.lean', 'set_option warn.«sorry» false\n', _SILENCED),
        ('Erdos/Probe.lean', 'set_option «warn».sorry false in\n', _SILENCED),
        ('Erdos/Probe.lean', '#guard_msgs in\nexample : True := sorry\n', _SILENCED),
        (
            'lakefile.toml',
            'name = "fixture"\nleanOptions = { "warn.sorry" = false }\n',
            _SILENCED,
        ),
        (
            'lakefile.toml',
            'name = "fixture"\n\n[leanOptions.warn]\nsorry = false\n',
            _SILENCED,
        ),
        (
            'lakefile.toml',
            'name = "fixture"\nleanOptions = { warn = { sorry = false } }\n',
            _SILENCED,
        ),
        (
            'Erdos/Probe.lean',
            'example : 1 + 1 = 2 := by native_decide\n',
            _COMPILED,
        ),
        (
            'Erdos/Probe.lean',
            'set_option maxRecDepth 100 in\nexample : 1 + 1 = 2 := by\n  decide +native\n',
            _COMPILED,
        ),
        (
            'Erdos/Probe.lean',
            '@[simp]example : 1 + 1 = 2 := by native_decide\n',
            _COMPILED,
        ),
        (
            'Erdos/Probe.lean',
            'example : (match 1 with\n| 0 => false\n| _ => true) = true := by native_decide\n',
            _COMPILED,
        ),
        (
            'Erdos/Probe.lean',
            'example : 1 + 1 = 2 := by\n/- compiled below -/\n  native_decide\n',
            _COMPILED,
        ),
        (
            'Erdos/Probe.lean',
            'example : 1 + 1 = 2 := by\n  decide (config := { native := true })\n',
            _COMPILED,
        ),
        ('Erdos/Probe.lean', 'theorem t : 1 + 1 = 2 := by native_decide\n', None),
        (
            'Erdos/Probe.lean',
            'example : True := trivial -- not native_decide\n',
            None,
        ),
        (
            'Erdos/Probe.lean',
            '/-- For example, native_decide is avoided. -/\ntheorem t : True := trivial\n',
            None,
        ),
        (
            'Erdos/Probe.lean',
            '/-- An example where\nnative_decide is avoided. -/\ntheorem t : True := trivial\n',
            None,
        ),
        (
            'Erdos/Probe.lean',
            'example : True := trivial\ntheorem t : 1 + 1 = 2 := by\n  native_decide\n',
            None,
        ),
        (
            'Erdos/Probe.lean',
            'example (h : True) : True := by\n  have hnative := h\n  exact hnative\n',
            None,
        ),
    ],
    ids=[
        'warn-sorry',
        'warn-quoted-sorry',
        'quoted-warn-sorry',
        'guard-msgs',
        'lakefile-warn-sorry',
        'lakefile-nested-table',
        'lakefile-inline-table',
        'example-native-decide',
        'example-decide-native',
        'attribute-example',
        'example-match-arms',
        'example-block-comment',
        'example-native-option',
        'theorem-native-decide',
        'commented',
        'docstring',
        'docstring-lines',
        'example-then-theorem',
        'example-native-suffix',
    ],
)
def test_gate_refuses_sources_the_audit_cannot_see(
    lean_project: pathlib.Path,
    shell_environment: dict[str, str],
    path: str,
    source: str,
    refusal: str | None,
) -> None:
    """Refuse a hidden sorry warning or an example's compiled decision before building."""
    _write(
        lean_project / '.lake/packages/mathlib/.lake/build/lib/lean/Mathlib.olean',
        'object\n',
    )
    _write(lean_project / path, source)
    result = _run(lean_project, shell_environment)
    commands = [line.split('|')[0] for line in _calls(shell_environment)]
    if refusal is None:
        assert result.returncode == 0, result.stdout + result.stderr
        assert commands == ['build', 'exe audit --check']
    else:
        assert result.returncode != 0, result.stdout + result.stderr
        assert refusal in result.stderr
        assert commands == []


# ------ self-test safety and freshness


@pytest.mark.parametrize('kind', ['regular', 'symlink', 'dangling'])
def test_selftest_preserves_existing_probe_paths(
    lean_project: pathlib.Path,
    shell_environment: dict[str, str],
    kind: str,
) -> None:
    """Refuse owned probe paths without touching their bytes, targets, or stamp."""
    _write(
        lean_project / '.lake/packages/mathlib/.lake/build/lib/lean/Mathlib.olean',
        'object\n',
    )
    probe = lean_project / 'Erdos/AuditSelfTestProbe.lean'
    target = lean_project.parent / 'owned-source.lean'
    content = b'owned probe\x00\n'
    if kind == 'regular':
        probe.write_bytes(content)
    else:
        if kind == 'symlink':
            target.write_bytes(content)
        probe.symlink_to(target)
    stamp = lean_project / 'scripts/selftest.stamp'
    original_stamp = stamp.read_bytes()
    result = _run(lean_project, shell_environment, script='audit_selftest.sh')
    assert result.returncode != 0
    assert 'refusing to replace existing probe path' in result.stdout + result.stderr
    assert _calls(shell_environment) == []
    assert stamp.read_bytes() == original_stamp
    if kind == 'regular':
        assert not probe.is_symlink()
        assert probe.read_bytes() == content
    else:
        assert probe.is_symlink()
        assert probe.readlink() == target
        if kind == 'symlink':
            assert target.read_bytes() == content
        else:
            assert not target.exists()


def test_cold_selftest_creates_no_probe_or_stamp(
    lean_project: pathlib.Path,
    shell_environment: dict[str, str],
) -> None:
    """Refuse a cold self-test before creating a probe or claiming a fresh stamp."""
    stamp = lean_project / 'scripts/selftest.stamp'
    stamp.unlink()
    _write(lean_project / '.lake/packages/mathlib/Mathlib.lean', '-- source only\n')
    result = _run(lean_project, shell_environment, script='audit_selftest.sh')
    assert result.returncode != 0
    assert 'binary cache is missing' in result.stdout + result.stderr
    assert _calls(shell_environment) == []
    assert not (lean_project / 'Erdos/AuditSelfTestProbe.lean').exists()
    assert not stamp.exists()


@pytest.mark.parametrize(
    argnames='header',
    argvalues=[
        '',
        '-- EXEPCT: fixture refusal\n',
        '-- EXPECT: \n',
        '-- EXPECT: fixture refusal\n-- EXPECT: \n',
    ],
    ids=['missing', 'mistyped', 'empty', 'empty-second'],
)
def test_selftest_rejects_missing_expect(
    lean_project: pathlib.Path,
    shell_environment: dict[str, str],
    header: str,
) -> None:
    """Reject malformed fixture expectations before building a probe or stamping."""
    _write(
        lean_project / '.lake/packages/mathlib/.lake/build/lib/lean/Mathlib.olean',
        'object\n',
    )
    _write(lean_project / 'scripts/selftest/refusal.lean', header + '-- fixture\n')
    stamp = lean_project / 'scripts/selftest.stamp'
    original_stamp = stamp.read_bytes()
    result = _run(lean_project, shell_environment, script='audit_selftest.sh')
    assert result.returncode != 0, result.stdout + result.stderr
    assert 'selftest FAIL refusal: missing EXPECT' in result.stdout
    assert 'SELFTEST PASS' not in result.stdout
    assert _calls(shell_environment) == [
        f'build|{lean_project.resolve()}|-- first revision|4',
        f'exe audit --check|{lean_project.resolve()}|-- first revision|4',
    ]
    assert not (lean_project / 'Erdos/AuditSelfTestProbe.lean').exists()
    assert stamp.read_bytes() == original_stamp


@pytest.mark.parametrize(
    argnames=('audit', 'diagnostic'),
    argvalues=[
        ('report', None),
        ('refuse', 'audit refused an admitted corpus'),
        ('silent', "audit passed without expected report 'fixture admitted'"),
    ],
    ids=['admitted', 'refused', 'unreported'],
)
def test_selftest_admit_fixture_needs_pass_and_report(
    lean_project: pathlib.Path,
    shell_environment: dict[str, str],
    audit: str,
    diagnostic: str | None,
) -> None:
    """Pass an admit fixture only when the audit exits zero and prints its report."""
    _write(
        lean_project / '.lake/packages/mathlib/.lake/build/lib/lean/Mathlib.olean',
        'object\n',
    )
    _write(
        lean_project / 'scripts/selftest/admit.lean',
        '-- EXPECT: fixture admitted\n-- MODE: admit\n',
    )
    shell_environment['LEAN_TEST_ADMIT'] = audit
    stamp = lean_project / 'scripts/selftest.stamp'
    original_stamp = stamp.read_bytes()
    result = _run(lean_project, shell_environment, script='audit_selftest.sh')
    if diagnostic is None:
        assert result.returncode == 0, result.stdout + result.stderr
        assert 'selftest ok   admit' in result.stdout
        assert 'selftest ok   refusal' in result.stdout
        assert 'SELFTEST PASS (stamp written)' in result.stdout
        assert stamp.read_bytes() != original_stamp
    else:
        assert result.returncode != 0, result.stdout + result.stderr
        assert f'selftest FAIL admit: {diagnostic}' in result.stdout
        assert 'SELFTEST PASS' not in result.stdout
        assert stamp.read_bytes() == original_stamp
    assert [line.split('|')[0] for line in _calls(shell_environment)] == [
        'build',
        'exe audit',
        'build',
        'exe audit',
        'build',
        'exe audit --check',
    ]
    assert not (lean_project / 'Erdos/AuditSelfTestProbe.lean').exists()


def test_selftest_runs_check_fixtures_under_check(
    lean_project: pathlib.Path,
    shell_environment: dict[str, str],
) -> None:
    """Route a check fixture to `audit --check`, the only mode that refuses it."""
    _write(
        lean_project / '.lake/packages/mathlib/.lake/build/lib/lean/Mathlib.olean',
        'object\n',
    )
    _write(
        lean_project / 'scripts/selftest/stale.lean',
        '-- EXPECT: fixture stale\n-- MODE: check\n',
    )
    stamp = lean_project / 'scripts/selftest.stamp'
    original_stamp = stamp.read_bytes()
    result = _run(lean_project, shell_environment, script='audit_selftest.sh')
    assert result.returncode == 0, result.stdout + result.stderr
    assert 'selftest ok   stale' in result.stdout
    assert 'SELFTEST PASS (stamp written)' in result.stdout
    assert stamp.read_bytes() != original_stamp
    assert [line.split('|')[0] for line in _calls(shell_environment)] == [
        'build',
        'exe audit',
        'build',
        'exe audit --check',
        'build',
        'exe audit --check',
    ]
    assert not (lean_project / 'Erdos/AuditSelfTestProbe.lean').exists()


@pytest.mark.parametrize(
    argnames=('setting', 'value', 'diagnostic', 'output'),
    argvalues=[
        (
            'LEAN_TEST_BUILD',
            'probe-error',
            'refusal: fixture does not build',
            'fixture build error',
        ),
        (
            'LEAN_TEST_REFUSAL',
            'pass',
            'refusal: audit passed on a violating corpus',
            'fixture audit passed',
        ),
        (
            'LEAN_TEST_REFUSAL',
            'mismatch',
            "refusal: audit failed without expected message 'fixture refusal'",
            'FAIL another refusal',
        ),
        (
            'LEAN_TEST_CONTROL',
            'fail',
            'control: clean corpus does not pass',
            'FAIL control audit error',
        ),
        (
            'LEAN_TEST_BUILD',
            'edit',
            "inputs: the stamp's inputs changed during the run",
            None,
        ),
    ],
    ids=['unbuilt', 'passed', 'mismatched', 'control', 'edited'],
)
def test_selftest_failures_print_output_and_keep_the_stamp(
    lean_project: pathlib.Path,
    shell_environment: dict[str, str],
    setting: str,
    value: str,
    diagnostic: str,
    output: str | None,
) -> None:
    """Fail each broken verdict with its diagnostic, never stamping or leaving a probe."""
    _write(
        lean_project / '.lake/packages/mathlib/.lake/build/lib/lean/Mathlib.olean',
        'object\n',
    )
    shell_environment[setting] = value
    stamp = lean_project / 'scripts/selftest.stamp'
    original_stamp = stamp.read_bytes()
    result = _run(lean_project, shell_environment, script='audit_selftest.sh')
    assert result.returncode != 0, result.stdout + result.stderr
    assert f'selftest FAIL {diagnostic}' in result.stdout
    if output is not None:
        assert output in result.stdout
    assert 'SELFTEST PASS' not in result.stdout
    assert stamp.read_bytes() == original_stamp
    assert not (lean_project / 'Erdos/AuditSelfTestProbe.lean').exists()


@pytest.mark.parametrize(
    argnames=('fragments', 'missing'),
    argvalues=[
        (['fixture refusal', 'FAIL fixture'], None),
        (['fixture refusal', 'absent fragment'], 'absent fragment'),
        (['absent fragment', 'fixture refusal'], 'absent fragment'),
    ],
    ids=['all', 'second-missing', 'first-missing'],
)
def test_selftest_requires_every_expected_fragment(
    lean_project: pathlib.Path,
    shell_environment: dict[str, str],
    fragments: list[str],
    missing: str | None,
) -> None:
    """Pass a fixture only when the audit output holds every one of its fragments."""
    _write(
        lean_project / '.lake/packages/mathlib/.lake/build/lib/lean/Mathlib.olean',
        'object\n',
    )
    _write(
        lean_project / 'scripts/selftest/refusal.lean',
        ''.join(f'-- EXPECT: {fragment}\n' for fragment in fragments),
    )
    stamp = lean_project / 'scripts/selftest.stamp'
    original_stamp = stamp.read_bytes()
    result = _run(lean_project, shell_environment, script='audit_selftest.sh')
    if missing is None:
        assert result.returncode == 0, result.stdout + result.stderr
        assert 'selftest ok   refusal' in result.stdout
        assert stamp.read_bytes() != original_stamp
    else:
        assert result.returncode != 0, result.stdout + result.stderr
        assert (
            f"selftest FAIL refusal: audit failed without expected message '{missing}'"
            in result.stdout
        )
        assert stamp.read_bytes() == original_stamp


@pytest.mark.parametrize(
    argnames=('placement', 'diagnostic'),
    argvalues=[
        ('placed', None),
        ('unlisted', "L9994 records [], not ['Erdos.L9995.claim']"),
        (
            'extra',
            "top records ['Erdos.L9994.claim', 'Erdos.L9995.claim'],"
            " not ['Erdos.L9995.claim']",
        ),
        ('foreign', 'L9995 records a declaration of Erdos.Elsewhere'),
        ('unlisted-axiom', f'L9995 records {_MINTED} outside its axioms'),
        ('detached', 'L9995 records a record the top-level array lacks'),
        ('leaked', 'L1 records a probe declaration that no RECORD line places'),
        ('unprinted', 'no manifest in the audit output'),
    ],
)
def test_selftest_places_compiler_records_by_structure(
    lean_project: pathlib.Path,
    shell_environment: dict[str, str],
    placement: str,
    diagnostic: str | None,
) -> None:
    """Read a print fixture's manifest and find each compiler record where its rows say."""
    _write(
        lean_project / '.lake/packages/mathlib/.lake/build/lib/lean/Mathlib.olean',
        'object\n',
    )
    _write(
        lean_project / 'scripts/selftest/record.lean',
        '-- EXPECT: fixture admitted\n'
        '-- MODE: print\n'
        '-- RECORD: L9995 Erdos.L9995.claim\n'
        '-- RECORD: L9994 Erdos.L9995.claim\n'
        '-- RECORD: top Erdos.L9995.claim\n',
    )
    record = {
        'axiom': _MINTED,
        'declaration': 'Erdos.L9995.claim',
        'module': 'Erdos.AuditSelfTestProbe',
    }
    manifest = {
        'compiler': [record],
        'claims': [
            {'id': 'L9994', 'axioms': [_MINTED], 'compiler': [record]},
            {'id': 'L9995', 'axioms': [_MINTED], 'compiler': [record]},
        ],
    }
    if placement == 'unlisted':
        manifest['claims'][0]['compiler'] = []
    elif placement == 'extra':
        manifest['compiler'] = [
            record,
            {**record, 'declaration': 'Erdos.L9994.claim'},
        ]
    elif placement == 'foreign':
        record['module'] = 'Erdos.Elsewhere'
    elif placement == 'unlisted-axiom':
        manifest['claims'][1]['axioms'] = []
    elif placement == 'detached':
        manifest['compiler'] = [{**record, 'axiom': 'Erdos.other_axiom'}]
    elif placement == 'leaked':
        manifest['claims'].append({'id': 'L1', 'axioms': [], 'compiler': [record]})
    if placement != 'unprinted':
        _write(
            pathlib.Path(shell_environment['LEAN_TEST_MANIFEST']),
            json.dumps(manifest, indent=1) + '\n',
        )
    stamp = lean_project / 'scripts/selftest.stamp'
    original_stamp = stamp.read_bytes()
    result = _run(lean_project, shell_environment, script='audit_selftest.sh')
    if diagnostic is None:
        assert result.returncode == 0, result.stdout + result.stderr
        assert 'selftest ok   record' in result.stdout
        assert stamp.read_bytes() != original_stamp
    else:
        assert result.returncode != 0, result.stdout + result.stderr
        assert (
            f'selftest FAIL record: record check failed: {diagnostic}' in result.stdout
        )
        assert stamp.read_bytes() == original_stamp
    assert [line.split('|')[0] for line in _calls(shell_environment)] == [
        'build',
        'exe audit --print',
        'build',
        'exe audit',
        'build',
        'exe audit --check',
    ]
    assert not (lean_project / 'Erdos/AuditSelfTestProbe.lean').exists()


def test_selftest_rejects_a_print_fixture_without_records(
    lean_project: pathlib.Path,
    shell_environment: dict[str, str],
) -> None:
    """Refuse a print fixture that places no record before building its probe."""
    _write(
        lean_project / '.lake/packages/mathlib/.lake/build/lib/lean/Mathlib.olean',
        'object\n',
    )
    _write(
        lean_project / 'scripts/selftest/record.lean',
        '-- EXPECT: fixture admitted\n-- MODE: print\n',
    )
    stamp = lean_project / 'scripts/selftest.stamp'
    original_stamp = stamp.read_bytes()
    result = _run(lean_project, shell_environment, script='audit_selftest.sh')
    assert result.returncode != 0, result.stdout + result.stderr
    assert 'selftest FAIL record: missing RECORD' in result.stdout
    assert [line.split('|')[0] for line in _calls(shell_environment)] == [
        'build',
        'exe audit',
        'build',
        'exe audit --check',
    ]
    assert stamp.read_bytes() == original_stamp


def test_digest_is_independent_of_locale(
    lean_project: pathlib.Path,
    shell_environment: dict[str, str],
) -> None:
    """Hash the same mixed-case source paths identically in C and US UTF-8 locales."""
    locales = subprocess.run(
        ['locale', '-a'],
        env=shell_environment,
        capture_output=True,
        text=True,
        check=True,
        timeout=120,
    ).stdout.splitlines()
    english = next(
        (name for name in locales if name.lower().replace('-', '') == 'en_us.utf8'),
        None,
    )
    if english is None:
        pytest.skip('en_US UTF-8 locale is not installed')
    baseline = _run(lean_project, shell_environment, script='selftest_digest.sh')
    shell_environment['LC_ALL'] = english
    localized = _run(lean_project, shell_environment, script='selftest_digest.sh')
    assert baseline.returncode == 0, baseline.stdout + baseline.stderr
    assert localized.returncode == 0, localized.stdout + localized.stderr
    assert baseline.stdout == localized.stdout


@pytest.mark.parametrize(
    argnames=('source', 'invalidates'),
    argvalues=[
        ('Audit/alpha.lean', True),
        ('lean-toolchain', True),
        ('lakefile.toml', True),
        ('lake-manifest.json', True),
        ('scripts/audit_selftest.sh', True),
        ('scripts/selftest/refusal.lean', True),
        ('scripts/gate.sh', False),
        ('scripts/selftest_digest.sh', False),
    ],
)
def test_digest_tracks_only_refusal_inputs(
    lean_project: pathlib.Path,
    shell_environment: dict[str, str],
    source: str,
    invalidates: bool,
) -> None:
    """Hash refusal inputs; gate or helper edits alone need no new self-test stamp."""
    stamp = (lean_project / 'scripts/selftest.stamp').read_text(encoding='utf-8')
    path = lean_project / source
    _write(path, path.read_text(encoding='utf-8') + '\n')
    result = _run(lean_project, shell_environment, script='selftest_digest.sh')
    assert result.returncode == 0, result.stdout + result.stderr
    if invalidates:
        assert result.stdout != stamp
    else:
        assert result.stdout == stamp


# ------ thread cap


@pytest.mark.parametrize(
    argnames=('caller', 'threads'),
    argvalues=[('2', '2'), ('', '4')],
    ids=['caller-value', 'empty'],
)
@pytest.mark.parametrize('run', ['in-place', 'clean', 'self-test'])
def test_lake_calls_receive_the_thread_cap(
    lean_project: pathlib.Path,
    shell_environment: dict[str, str],
    run: str,
    caller: str,
    threads: str,
) -> None:
    """Keep a caller's thread cap for every Lake call, and default an empty one to 4."""
    _write(
        lean_project / '.lake/packages/mathlib/.lake/build/lib/lean/Mathlib.olean',
        'object\n',
    )
    if run == 'clean':
        _git(lean_project.parent, shell_environment, 'init', '-b', 'main')
        _git(lean_project.parent, shell_environment, 'add', 'lean')
        _git(lean_project.parent, shell_environment, 'commit', '-m', 'Fixture')
    shell_environment['LEAN_NUM_THREADS'] = caller
    arguments = ['--clean'] if run == 'clean' else []
    script = 'audit_selftest.sh' if run == 'self-test' else 'gate.sh'
    result = _run(lean_project, shell_environment, *arguments, script=script)
    assert result.returncode == 0, result.stdout + result.stderr
    calls = [line.split('|') for line in _calls(shell_environment)]
    assert calls
    assert {cap for _, _, _, cap in calls} == {threads}


@pytest.mark.parametrize('threads', ['0', '-1', 'four'])
@pytest.mark.parametrize('run', ['in-place', 'clean', 'self-test'])
def test_invalid_thread_caps_fail_before_lake(
    lean_project: pathlib.Path,
    shell_environment: dict[str, str],
    run: str,
    threads: str,
) -> None:
    """Refuse a thread cap that is not a positive whole number before any Lake call."""
    _write(
        lean_project / '.lake/packages/mathlib/.lake/build/lib/lean/Mathlib.olean',
        'object\n',
    )
    if run == 'clean':
        _git(lean_project.parent, shell_environment, 'init', '-b', 'main')
        _git(lean_project.parent, shell_environment, 'add', 'lean')
        _git(lean_project.parent, shell_environment, 'commit', '-m', 'Fixture')
    shell_environment['LEAN_NUM_THREADS'] = threads
    arguments = ['--clean'] if run == 'clean' else []
    script = 'audit_selftest.sh' if run == 'self-test' else 'gate.sh'
    result = _run(lean_project, shell_environment, *arguments, script=script)
    assert result.returncode == 2, result.stdout + result.stderr
    assert (
        f"Error: LEAN_NUM_THREADS must be a positive whole number, not '{threads}'."
        in result.stderr
    )
    assert _calls(shell_environment) == []


# ------ helpers


def _write(path: pathlib.Path, content: str) -> None:
    """Write a UTF-8 fixture file and create its parents."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')


def _run(
    lean: pathlib.Path,
    environment: dict[str, str],
    *arguments: str,
    script: str = 'gate.sh',
) -> subprocess.CompletedProcess[str]:
    """Invoke a copied real script from outside the Lean project."""
    return subprocess.run(
        ['bash', str(lean / 'scripts' / script), *arguments],
        cwd=lean.parent,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
        timeout=120,
    )


def _stamp(lean: pathlib.Path, environment: dict[str, str]) -> None:
    """Stamp only a pytest fixture's copied audit surface."""
    result = _run(lean, environment, script='selftest_digest.sh')
    assert result.returncode == 0, result.stdout + result.stderr
    _write(lean / 'scripts/selftest.stamp', result.stdout)


def _calls(environment: dict[str, str]) -> list[str]:
    """Read the fake Lake boundary log, or no calls when the script refused early."""
    path = pathlib.Path(environment['LEAN_TEST_CALLS'])
    return path.read_text(encoding='utf-8').splitlines() if path.exists() else []


def _git(
    root: pathlib.Path,
    environment: dict[str, str],
    *arguments: str,
) -> None:
    """Run real Git only in a pytest repository with an isolated author and hooks."""
    subprocess.run(
        [
            'git',
            '-c',
            'user.name=Lean workflow tests',
            '-c',
            'user.email=lean@example.test',
            '-c',
            'core.hooksPath=/dev/null',
            '-c',
            'commit.gpgsign=false',
            *arguments,
        ],
        cwd=root,
        env=environment,
        capture_output=True,
        text=True,
        check=True,
        timeout=120,
    )

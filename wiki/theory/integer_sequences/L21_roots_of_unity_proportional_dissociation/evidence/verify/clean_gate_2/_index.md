---
name: theory/integer_sequences/L21_roots_of_unity_proportional_dissociation/evidence/verify/clean_gate_2
title: The 2026-10-13 non-author clean gate of L21 on Lean v4.34.1
desc: |
  The non-author clean gate of 2026-10-13 for L21 on Lean v4.34.1, one run
  serving L20, L21 and L22: the committed Lean gate in clean mode over a fresh
  archive of the whole lean/ tree of the change that ported their Lean modules
  to Lean v4.34.1, as committed at 2026-10-13T19:38:30Z, exit 0, AUDIT PASS
  over 4 claims with 0 compiler axioms and the committed self-test stamp
  matched; the receipt, the captured log and the wrapper.
tags: []
sources: []
created: 2026-10-13T20:10:07Z
updated: 2026-10-13T20:10:07Z
---

# The 2026-10-13 non-author clean gate of L21 on Lean v4.34.1

[[theory/integer_sequences/L21_roots_of_unity_proportional_dissociation/evidence/verify/_index|..]]

***

This record is the non-author clean gate of L21 on the whole `lean/` tree of
the change that ported the Lean modules of L20, L21 and L22 to Lean v4.34.1,
as committed at 2026-10-13T19:38:30Z: the declarations `Erdos.L21.statement`
and `Erdos.L21.claim` in `lean/Erdos/L21.lean`, the 278 modules that
`lean/Manifest.json` lists with its four claim rows, L17, L20, L21 and L22,
and the toolchain files `lean/lean-toolchain` (`leanprover/lean4:v4.34.1`),
`lean/lakefile.toml` and `lean/lake-manifest.json`, which pins Mathlib at its
`v4.34.1` tag. One run serves L20, L21 and L22; each of their record folders
files the same log and wrapper with its own receipt. The files filed here:
[clean_gate.json](clean_gate.json), the non-author runner's clean-gate
receipt; [clean_gate_log.txt](clean_gate_log.txt), the gate's captured streams
with the runner's header and trailer; and
[run_clean_gate_sh.txt](run_clean_gate_sh.txt), the runner's wrapper, filed
under a name the wiki tooling admits.

## Native validation

The receipt and the log record `/bin/bash lean/scripts/gate.sh --clean`, run
under `LEAN_NUM_THREADS=4` and `nice -n 10` on a fresh `git archive` of the
checked source's `lean/` tree, from 2026-10-13T19:54:37Z to 19:59:38Z (301 s;
no memory sampler ran): whole-shell exit 0; the dependency fetch and the
Mathlib cache passed; "Build completed successfully (3998 jobs)." (log line
649), every one of the 278 modules built and `Erdos.L21` as job 3997 (line
648); "audited 3771 constants in 278 modules, 4 claims, 0 compiler axioms:
AUDIT PASS" (line 650); and "Lean gate passed." (line 651), after the
committed self-test stamp matched. Per-leg exit codes are inferred from the
gate's `set -euo pipefail` source and the located markers.

The streams carry 54 warning diagnostics from 32 modules: 20 deprecated
Mathlib imports (`Mathlib.Data.Real.Basic`, `Mathlib.Data.Complex.Basic` and
`Mathlib.Data.Set.Lattice`), 8 deprecated lemma names, 25 linter suggestions
to write `have` for `haveI` or `let` for `letI` where the goal is a
proposition, and one linter note that `tac1 <;> tac2` could be
`(tac1; tac2)`; three `info:` lines suggest `ring_nf` where `ring` was
written. None is an error, and none fails the build, the audit or the gate.
The two other lines a search for "warning" finds and the one a search for
"error" finds are build lines of modules whose names contain the word.

The run was serialized by the host's Lean build lock, which full Lean builds
on the host take before they start: the wrapper took it before launch and
held it until exit. No preflight reading was retained and no process watch
ran. The runner's worktree was checked out at another revision with the same
`lean/` tree, with 83 tracked changes outside `lean/` before and after the
run; the gate archives the checked source's `lean/` tree from the
repository's object store, so no file of that worktree entered the archive.

The proof is kernel-only on this tree: the L21 row of `lean/Manifest.json`
lists the axioms `propext`, `Classical.choice` and `Quot.sound` and an empty
`compiler` list, the manifest's top-level `compiler` array is empty, and the
audit line reports 0 compiler axioms.

## What the gate supports

The card's tier-2 standing rests on the statement-fidelity audit and distinct
grade of the source of 2026-09-28, filed in the folder `statement_fidelity/`
beside this one, on a grade decision that applied that grade to this tree, and
on this gate. The grade decision found that the claim's surface differs only
by Mathlib's rename of `setOf` to `Set.ofPred`, a deprecated alias with the
same type and body; the statement declaration, every definition it reaches,
the statement fingerprints in `lean/Manifest.json` and the statement field are
unchanged. A clean gate checks the committed environment independently; it
does not replace the statement-fidelity review and awards no standing by
itself. The receipt asserts no tier.

Roles. Clean gate: a non-author clean-gate runner in a fresh context, who did
not author the port to Lean v4.34.1, as the receipt's role block states.

## Filing

The receipt, the log and the wrapper are filed in this folder, and the same
log and wrapper in the `clean_gate_2/` folders of L20 and L22. The log is
filed as captured apart from four values in its header and trailer: the
checked source's label, which named the branch and an abbreviated revision, is
replaced by the time of its commit; the checked source's revision in the
command line, and the runner worktree's head before and after the run, which
were the same, are replaced by bracketed descriptions. Every stream line is
verbatim. The wrapper `run_clean_gate.sh` is filed under the name
`run_clean_gate_sh.txt` (the wiki tooling admits no `.sh` name), so the name
`run_clean_gate.sh` in the receipt resolves to that file; three of its values
(the revision, the worktree and the lock's directory) are replaced by
bracketed descriptions, its source label as in the log, and its opening
comment, which named the runner's seat and the abbreviated revision of the
earlier change that moved the project to Lean v4.34.1, reworded to name no
person, seat, branch or revision. The record names no commit, tree or blob id
and no per-file hash; the receipt quotes the Mathlib and dependency revisions
as the gate printed them, under the external-version case.

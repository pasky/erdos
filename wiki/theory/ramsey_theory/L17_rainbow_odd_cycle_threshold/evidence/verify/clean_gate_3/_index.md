---
name: theory/ramsey_theory/L17_rainbow_odd_cycle_threshold/evidence/verify/clean_gate_3
title: The 2026-10-13 non-author clean gate of L17 with L20 to L22
desc: |
  The non-author clean gate of 2026-10-13 for L17, one run serving L17, L20, L21
  and L22: the committed Lean gate in clean mode over a fresh archive of the whole
  lean/ tree as it stood on 2026-10-13T04:56:43Z, exit 0, AUDIT PASS over 4 claims
  with 0 compiler axioms and the committed self-test stamp matched; the receipt,
  the captured log and the wrapper.
tags: []
sources: []
created: 2026-10-13T05:40:00Z
updated: 2026-10-13T05:40:00Z
---

# The 2026-10-13 non-author clean gate of L17 with L20 to L22

[[theory/ramsey_theory/L17_rainbow_odd_cycle_threshold/evidence/verify/_index|..]]

***

This record is the non-author clean gate of L17 on the whole `lean/` tree as it
stood on 2026-10-13T04:56:43Z, after the restore of the claims L20, L21 and L22,
before it landed on the default branch: the
declarations `Erdos.L17.statement` and `Erdos.L17.claim` in
`lean/Erdos/L17.lean`, the 278 modules that `lean/Manifest.json` lists with its
four claim rows, L17, L20, L21 and L22, and the toolchain files
`lean/lean-toolchain` (`leanprover/lean4:v4.32.0-rc1` on the date),
`lean/lakefile.toml` and `lean/lake-manifest.json`. One run serves the four
claims; each of their record folders files the same log and wrapper with its own
receipt. The files filed here: [clean_gate.json](clean_gate.json), the
clean-gate receipt; [clean_gate_log.txt](clean_gate_log.txt), the gate's
captured streams with the runner's header and trailer; and
[run_clean_gate_sh.txt](run_clean_gate_sh.txt), the runner's wrapper, filed
under a name the wiki tooling admits.

## Native validation

The receipt and the log record `/bin/bash lean/scripts/gate.sh --clean`, run
under `LEAN_NUM_THREADS=4` and `nice -n 10` on a fresh `git archive` of that
state's `lean/` tree, from 2026-10-13T05:05:07Z to 05:09:06Z (239 s):
whole-shell exit 0; the dependency fetch and the Mathlib cache passed; "Build
completed successfully (3889 jobs)." (log line 361), every one of the 278
modules built and `Erdos.L17` as job 3857 (log line 320); "audited 3788
constants in 278 modules, 4 claims, 0 compiler axioms: AUDIT PASS" (line 362);
and "Lean gate passed." (line 363), after the committed self-test stamp matched.
One stream line is a warning: a linter note at
`Erdos/RootsOfUnitySidon/FiniteRieszMomentBound.lean:186:25` (line 351) that
`tac1 <;> tac2` could be written `(tac1; tac2)`, a style suggestion that does
not stop the build. The other lines a search for "warning" or "error" finds are
build lines of modules whose names contain the word. The worktree named the
checked source with no tracked change before and after the run (log lines 5, 6,
365 and 366). Per-leg exit codes are inferred from the gate's `set -euo
pipefail` source and the located markers. The runner recorded no host reading or
memory sample.

The proof is kernel-only on this tree: the L17 row of `lean/Manifest.json` lists
the axioms `propext`, `Classical.choice` and `Quot.sound` and an empty
`compiler` list, the manifest's top-level `compiler` array is empty, and the
audit line reports 0 compiler axioms.

## What the gate supports

This gate supports the card's tier-2 standing for the tree it checked, with the
second-cycle statement-fidelity review and distinct grade of 2026-10-02, filed
in the folder `statement_fidelity_2/` beside this one; the standing on the Lean
v4.34.1 tree rests on the clean gate filed in `clean_gate_2/`.
`scripts/claim_carry_forward.py`, run on 2026-10-13 from the tree the review and
the grade examined, the default branch as it stood on 2026-10-02 at 19:45:19Z,
to the tree this gate checked, in two legs: to the first tree whose row carries
a surface, comparing the row, the card field, the pins, the Lake configuration
and the import closure, and from there to the checked tree, comparing the row
with its surface, the card field and the pins, found clause (b) of the
carry-forward rule (`docs/verification.md` "Exact subjects and durable
evidence") holding on every leg, so the statement is unchanged in meaning from
the reviewed source to the tree this gate checked. The non-author clean gate of
2026-10-08 is filed in the folder `clean_gate/` beside this one. A clean gate
checks the committed environment independently; it does not replace the
statement-fidelity review and awards no standing by itself. The receipt asserts
no tier.

Roles. Clean gate: a non-author runner, distinct from the restorer of L20, L21
and L22 and from their authors. Filing: the restorer filed the runner's log and
wrapper as stated below and wrote the receipt from them.

## Filing

The log is filed byte for byte as captured, except that the commit id its two
`worktree_head` lines printed is replaced by the words "the checked source
(commit id removed at filing)". The wrapper `run_clean_gate.sh` is filed as
`run_clean_gate_sh.txt` (the wiki tooling admits no `.sh` name), so the name
`run_clean_gate.sh` in the receipt resolves to that file. It is filed as run
apart from its comments and two assignments: its `REV` line, which named the
checked source's commit, became the script's one argument, and its `REPO` line,
which named a local path, became `git -C "$HERE" rev-parse --show-toplevel`, as
in the wrapper of L17's gate of 2026-10-08; its comments lost the commit and the
runner's role name and gained a note on the log's redaction. The record names no
commit, tree or blob id of this repository and no per-file hash; the receipt
quotes the Mathlib and dependency revisions as the gate printed them, under the
external-version case.

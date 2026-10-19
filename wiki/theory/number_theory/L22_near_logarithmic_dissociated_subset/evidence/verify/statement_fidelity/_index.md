---
name: theory/number_theory/L22_near_logarithmic_dissociated_subset/evidence/verify/statement_fidelity
title: Whole-statement fidelity audit of L22 on 2026-09-28
desc: |
  The independent statement-fidelity audit of Erdos.L22.statement against the
  L22 card's prose statement as it stood on 2026-09-28, verdict PASS, its
  distinct grade, pass with tier 2 asserted, and the non-author clean-gate
  receipt, log and wrapper that put the tier in force.
tags: []
sources: []
created: 2026-09-28T18:02:14Z
updated: 2026-10-13T13:08:56Z
---

# Whole-statement fidelity audit of L22 on 2026-09-28

[[theory/number_theory/L22_near_logarithmic_dissociated_subset/evidence/verify/_index|..]]

[[theory/number_theory/L22_near_logarithmic_dissociated_subset/evidence/verify/statement_fidelity/grade|grade]]: A distinct grader's check of the L22 statement-fidelity audit of
2026-09-28: the audit is graded pass, and tier 2 is asserted for L22 with no
compiler assumption.

[[theory/number_theory/L22_near_logarithmic_dissociated_subset/evidence/verify/statement_fidelity/report|report]]: The independent whole-statement fidelity audit comparing the L22 card's
prose statement with Erdos.L22.statement as they stood on 2026-09-28;
verdict PASS, and no tier is assigned.

***

This record assesses the exact source as it stood on the default branch at
2026-09-28T13:50:48Z (the checked source, called "the commit" below; its
repository, `lean/`, `lean/Erdos` and `lean/Erdos/Problem963` tree
identities were taken by `git rev-parse` at the commit and are restated
here by that date): the declarations `Erdos.L22.statement` and
`Erdos.L22.claim` in
`lean/Erdos/L22.lean` with the claim's import closure of eight handwritten
modules under `lean/Erdos/` (`Erdos.L22` and the seven modules under
`lean/Erdos/Problem963/`), among the 2,977 modules `lean/Manifest.json` lists
at the commit, under toolchain `leanprover/lean4:v4.32.0-rc1` and Mathlib
`79aee35d…`; and the prose statement of
[[theory/number_theory/L22_near_logarithmic_dissociated_subset/_index|the L22 card]]
(its `statement` field with its convention and Scope sentences, and its
"Statement" and "Argument and formal surface" sections) together with the
sentences of
[[theory/number_theory/L22_near_logarithmic_dissociated_subset/_proof|the proof page]]
that characterize the Lean modules.

The two examination files filed here are
[[theory/number_theory/L22_near_logarithmic_dissociated_subset/evidence/verify/statement_fidelity/report|the audit report]],
the independent whole-statement fidelity audit: its subject and independence
facts (paths, revisions, reading depth per module and exposures), the
clause-by-clause comparison, the definitions unfolded with their Lean sources,
the discrepancies found (none) and the verdict **PASS**: the Lean statement is
the prose statement, and `claim` proves exactly `statement`; and
[[theory/number_theory/L22_near_logarithmic_dissociated_subset/evidence/verify/statement_fidelity/grade|the grade]],
the distinct grader's check of that audit, dated 2026-09-28: the audit
passes the fidelity contract and the independence rules, the grader's own
comparison agrees on every clause, each of the disclosed exposures E1-E8 is
ruled immaterial by the content test, and **tier 2 is asserted for L22**,
kernel-only, with no `assumes: compiler`; the card takes tier 2 when a
non-author's `lean/scripts/gate.sh --clean` passes on the source of
2026-09-28 and the acceptance cites the grade and that gate's report. That
gate is filed here
as three files: [clean_gate.json](clean_gate.json), the runner's receipt,
dated 2026-09-29; [clean_gate_log.txt](clean_gate_log.txt), the gate's
captured streams with the runner's header and trailer; and
[run_clean_gate_sh.txt](run_clean_gate_sh.txt), the runner's wrapper
`run_clean_gate.sh`, filed under a name the wiki tooling admits, with its
revision lines restated by date.

Roles. Auditor: the statement-fidelity auditor for L22, in a fresh context,
who took no part in writing the claim, its Lean development or its card, and
who read the Lean sources without building them; the auditor filed the report
under this folder as written. Grader: a distinct grader in a fresh context,
neither the author of L22 nor its auditor, given only its assignment, who
built nothing and ran no gate; the grader filed the grade as written. Clean
gate: a non-author clean-gate runner, in a fresh context, who received only
its commission naming the commit and the five record folders, read the gate
script, the Lean README's clean-checkout paragraph, the tier law, the
committed manifest's claim rows, the L18 grade's clean-gate condition and the
precedent receipts for their shape, filed the receipt, the log and the
wrapper, and asserts no tier. Filing: the integrator of the promotion
maintains this card, adds paths and dates and asserts no tier. No
native binding or acceptance warrant is filed; these records use neither,
and the grade's assertion is in force from the promotion that cites it
together with the receipt. The card's tier field and standing text were
outside the audit's subject.

The audit did not build the Lean sources, run the gate or the axiom audit,
review the mathematics of the `Erdos.Problem963` proofs, or read the research
pages the card cites. It asserts nothing about novelty, community acceptance
or the literature status of Problem 963.

## Native validation

The runner's receipt, [clean_gate.json](clean_gate.json), and the captured
[gate log](clean_gate_log.txt) record
`/bin/bash lean/scripts/gate.sh --clean`, run on the repository as it stood
on 2026-09-28, under `LEAN_NUM_THREADS=4` on a fresh `git archive` of the
commit's `lean/` subtree, launched from the repository root of a worktree
whose `lean/` subtree is the commit's: whole-shell exit 0, "Build completed
successfully (7501 jobs).", "audited 42230 constants in 2977 modules, 7
claims, 0 compiler axioms: AUDIT PASS", "Lean gate passed.", the committed
self-test stamp matched, from 2026-09-29T20:10:11Z to 21:30:54Z (4,843 s; no
memory sampler ran). The stream holds 104 linter warning lines (unused simp
arguments, deprecations and similar hints) in 43 files, none of them in
this claim's eight-module closure, and no line beginning `error:`; the
receipt's counts of 106 and 2 are case-insensitive matches that include
Lake progress lines for modules whose names contain the words. The
serialization rule was met: the observation-only watcher saw no `lean` or
`lake` process outside the gate's process tree in any of its 903
five-second samples, and the gate's own processes in that class peaked at
5. The watcher started 72 s after launch, during the Mathlib clone and
before any Lean process existed; in that unwatched window the runner ran
one `lake --version` query, with no build and no workspace load, to record
the Lake version, as the receipt discloses. The pre-launch host readings
were taken once, 27 s before launch. Per-leg exit codes are inferred from
the gate's `set -euo pipefail` source and the located markers.

One run of the gate serves the five claims whose statement-fidelity records
name that source, L18, L19, L20, L21 and L22: the wrapper ran once from the
L18 record folder, and each of the five record folders files the receipt
with its own owner and manifest row, a byte-identical copy of the captured
log and a byte-identical copy of the wrapper. The filed log was the captured
stream with trailing whitespace removed by the repository's pre-commit hook
at filing, 341,290 bytes against the receipt's 341,326, its 3,547 lines
being the 3,536 stream lines with the runner's header and trailer; the
hook changed nothing else. The header's three identity lines now name the
checked source by date, the stream lines are verbatim, the bytes as filed
are not retained, and the five copies remain byte-identical. The wrapper
`run_clean_gate.sh` is filed as `run_clean_gate_sh.txt` (the wiki tooling
admits no `.sh` name); its revision lines are likewise restated by date, and
that name in the receipt resolves to this file. The receipt records a mechanical validation of the
committed revision and confers no tier; the grade's assertion is in force
from the promotion that cites both.

The claims L14, L18 and L19 and their folders were removed from this
repository on 2026-10-08. The names this record gives them are history and
do not resolve: L14, L18 and L19 in the receipt's owners and manifest lists,
in the wrapper's comments and in the log; and the L18 grade and the L18
record folder, from which the wrapper ran, on this page. Their removal
changes no statement, check or verdict of this record.

---
name: theory/integer_sequences/L20_roots_of_unity_analytic_sidon/evidence/verify/statement_fidelity
title: Whole-statement fidelity audit of L20 on 2026-09-28
desc: |
  The independent clause-by-clause audit of the L20 prose statement against
  `Erdos.L20.statement` as it stood on 2026-09-28, verdict PASS, its distinct
  grade, pass with tier 2 asserted, and the non-author clean-gate receipt,
  log and wrapper that put the tier in force.
tags: []
sources: []
created: 2026-09-28T18:01:09Z
updated: 2026-10-13T13:08:56Z
---

# Whole-statement fidelity audit of L20 on 2026-09-28

[[theory/integer_sequences/L20_roots_of_unity_analytic_sidon/evidence/verify/_index|..]]

[[theory/integer_sequences/L20_roots_of_unity_analytic_sidon/evidence/verify/statement_fidelity/grade|grade]]: A distinct fresh-context grader re-checks the L20 statement-fidelity audit
of 2026-09-28 clause by clause, grades it pass, and asserts tier 2 for
L20 under the tier law, kernel-only, in force at the promotion that cites a
non-author clean gate of that source.

[[theory/integer_sequences/L20_roots_of_unity_analytic_sidon/evidence/verify/statement_fidelity/report|report]]: Independent clause-by-clause comparison of the L20 card's prose statement
with `Erdos.L20.statement` as they stood on 2026-09-28, with every
definition the statement uses unfolded to its Lean source; verdict PASS, no
tier assigned.

***

This record assesses the exact source as it stood on the default branch at
2026-09-28T13:50:48Z (the checked source, called "the commit" below; its
repository, `lean/` and `lean/Erdos` tree identities were taken by
`git rev-parse` at the commit and are restated here by that date): the
declarations `Erdos.L20.statement` and `Erdos.L20.claim` in
`lean/Erdos/L20.lean`, read with the three modules of
`lean/Erdos/RootsOfUnitySidon/` that hold the definitions they unfold to,
under toolchain `leanprover/lean4:v4.32.0-rc1` and Mathlib `79aee35d…`,
against the card's prose statement with its Conventions and Scope text. The
two examination files filed here:
[[theory/integer_sequences/L20_roots_of_unity_analytic_sidon/evidence/verify/statement_fidelity/report|report]],
the auditor's whole-statement fidelity report: subject and independence
with reading depth and exposures, the clause-by-clause comparison, the
definitions unfolded with their Lean sources, the discrepancies found
(none), and the verdict **PASS**; and
[[theory/integer_sequences/L20_roots_of_unity_analytic_sidon/evidence/verify/statement_fidelity/grade|grade]],
the distinct grade of that report, dated 2026-09-28: the audit passes the
fidelity contract, the grader reproduces every row with no discrepancy,
each of the audit's six disclosed exposures is ruled immaterial by the
content test, and **tier 2 is asserted for L20** at the commit,
kernel-only, with no `assumes: compiler`, in force at the promotion whose
acceptance cites a non-author run of `lean/scripts/gate.sh --clean` on the
repository as it stood on 2026-09-28, with its compiler-axiom count.

The non-author clean gate is filed in this folder as three files:
[clean_gate.json](clean_gate.json), the runner's receipt, dated 2026-09-29;
[clean_gate_log.txt](clean_gate_log.txt), the gate's captured streams with
the runner's header and trailer; and
[run_clean_gate_sh.txt](run_clean_gate_sh.txt), the runner's wrapper
`run_clean_gate.sh`, filed under a name the wiki tooling admits, with its
revision lines restated by date. The auditor and the grader built nothing
and ran no generator or
gate; the grade's assertion is in force from the promotion that cites it
together with the receipt. No probe, native binding or acceptance warrant
is filed; these records use none. This is the first statement-fidelity
record for L20. The commissioning text placed the claim under
`wiki/theory/number_theory/`; the records are filed under the actual
folder. The record confers no review or grade on the research notes or the
proof route and asserts no novelty or public acceptance.

Roles. Auditor: the independent statement-fidelity auditor for L20, in a
fresh context, given only its assignment, who took no part in the claim,
its Lean development or its card, built nothing and ran no gate. Grader: a
distinct grader in a fresh context, given only its assignment, not the
author of any module, page or record under review, not the auditor, and not
the runner of any gate. Clean gate: a non-author clean-gate runner, in a
fresh context, who received only its commission naming the commit and the
five record folders, read the gate script, the Lean README's clean-checkout
paragraph, the tier law, the committed manifest's claim rows, the L18 grade's
clean-gate condition and the precedent receipts for their shape, and
asserts no tier. Filing: the auditor filed the report and the grader the
grade, each as written; the runner filed the receipt, the log and the
wrapper; the integrator of the promotion maintains this card, adds paths
and dates and asserts no tier.

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
arguments, deprecations and similar hints) in 43 files, one of them,
`Erdos/RootsOfUnitySidon/FiniteRieszMomentBound.lean`, in this claim's
closure, and no line beginning `error:`; the receipt's counts of 106 and 2
are case-insensitive matches that include Lake progress lines for modules
whose names contain the words. The serialization rule was met: the
observation-only watcher saw no `lean` or `lake` process outside the gate's
process tree in any of its 903 five-second samples, and the gate's own
processes in that class peaked at 5. The watcher started 72 s after launch,
during the Mathlib clone and before any Lean process existed; in that
unwatched window the runner ran one `lake --version` query, with no build
and no workspace load, to record the Lake version, as the receipt
discloses. The pre-launch host readings were taken once, 27 s before
launch. Per-leg exit codes are inferred from the gate's `set -euo pipefail`
source and the located markers.

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

The claims L14, L15, L18 and L19 and their folders were removed from this
repository on 2026-10-08. The names this record gives them are history and
do not resolve: L14, L18 and L19 in the receipt's owners and manifest lists,
in the wrapper's comments and in the log; the L14 record and a path under the
L15 folder in the report; and the L18 grade and the L18 record folder, from
which the wrapper ran, on this page. Their removal changes no statement,
check or verdict of this record.

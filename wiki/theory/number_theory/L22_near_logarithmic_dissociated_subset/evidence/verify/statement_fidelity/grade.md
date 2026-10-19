---
name: theory/number_theory/L22_near_logarithmic_dissociated_subset/evidence/verify/statement_fidelity/grade
title: Distinct grade of the L22 statement-fidelity audit
desc: |
  A distinct grader's check of the L22 statement-fidelity audit of
  2026-09-28: the audit is graded pass, and tier 2 is asserted for L22 with no
  compiler assumption.
created: 2026-09-28T19:13:00Z
updated: 2026-09-28T20:42:32Z
---

***

Grade of the audit: **pass**. Tier asserted for L22: **2**, with no
`assumes: compiler`. This record grades
[[theory/number_theory/L22_near_logarithmic_dissociated_subset/evidence/verify/statement_fidelity/report|the statement-fidelity audit]]
of native claim L22 at the checked source of 2026-09-28.

## Subject

**Source and paths.** The subject is the repository as it stood on the
default branch at 2026-09-28T13:50:48Z (the checked source, called "the
commit" below; its repository, `lean/`, `lean/Erdos`,
`lean/Erdos/Problem963` and claim folder tree identities, each re-derived
here by `git rev-parse` at the commit, are restated by date in both
records), under toolchain `leanprover/lean4:v4.32.0-rc1`
(`lean/lean-toolchain`) and Mathlib revision
`79aee35d9696d759b73eed71d7dde666750bc35e` (`lean/lakefile.toml` line 11,
`lean/lake-manifest.json` lines 8 and 11). The audit graded is the report
filed as `report.md` in the folder `statement_fidelity/` under the
claim's `evidence/verify/`, linked above.

**What was re-checked.**

- The card's `statement` field at the commit (`_index.md` lines 12-21)
  against `Erdos.L22.statement` (`lean/Erdos/L22.lean` lines 23-27) and
  `Erdos.L22.claim` (lines 29-30), clause by clause: the dissociation
  convention with the empty subset included, the nonempty finite real set
  $A$ with $n=|A|$, the base-two logarithm, the existence of a dissociated
  $B\subseteq A$, the inequality with its constants, the restatement
  $f(n)\ge\log_2 n-\log_2(\log_2 n+1)$ for every integer $n\ge1$, and the
  Scope sentence.
- The definitions the audit unfolded (its U1-U11), read again from a
  Mathlib package checkout at the pinned revision with a clean status:
  `MulDissociated` and its `to_additive` twin `AddDissociated`
  (`Mathlib/Combinatorics/Additive/Dissociation.lean` line 45, under the
  `CommGroup` variable of line 31, with `mulDissociated_empty` at line 55),
  `Set.InjOn` (`Mathlib/Data/Set/Operations.lean` lines 299-300),
  `Finset.Nonempty` (`Mathlib/Data/Finset/Empty.lean` line 47),
  `Finset.card` (`Mathlib/Data/Finset/Card.lean` lines 47-48), the
  `SetLike` coercion, `mem_coe`, `coe_injective`, `subset_iff` and
  `coe_subset` (`Mathlib/Data/Finset/Defs.lean` lines 101-103, 126-127,
  153, 224-225 and 231-232), `Finset.prod` with its additive twin and
  `prod_empty` (`Mathlib/Algebra/BigOperators/Group/Finset/Defs.lean` lines
  68-69 and 359), `Real.logb`, `logb_zero`, `logb_neg_eq_logb` and
  `logb_nonneg` (`Mathlib/Analysis/SpecialFunctions/Log/Base.lean` lines
  43-44, 50, 81 and 236), `Real.log`, `exp_log`, `log_zero` and
  `log_neg_eq_log` (`Mathlib/Analysis/SpecialFunctions/Log/Basic.lean`
  lines 44-45, 58, 102 and 120), and `Nat.log` (`Mathlib/Data/Nat/Log.lean`
  lines 59-63). Every citation is where the audit places it and says what
  the audit says.
- The import closure of `Erdos.L22` under `lean/Erdos/`: the three import
  lines of `L22.lean` (two Mathlib modules and `Erdos.Problem963.CardBound`),
  the import lines of the seven `Erdos.Problem963` modules, which reach only
  one another and Mathlib, and a search at the commit showing that no other
  module under `lean/Erdos/` imports `Erdos.L22` or any of the seven. The
  entry theorem `Erdos.Problem963.exists_real_dissociated_large`
  (`lean/Erdos/Problem963/CardBound.lean` lines 155-159) has the closed type
  `statement` once `statement` is unfolded, the only textual difference
  being the coercion spelling `(B : Set ℝ)` for `(↑B : Set ℝ)`. The bridge
  theorems `integer_card_le_pow` (lines 142-145), `integer_card_bound`
  (lines 148-151), `real_card_bound_of_integer_card_bound`
  (`IntegerModel.lean` lines 131-137) and `log_bound_of_card_le`
  (`LogBound.lean` lines 15-17, case split at line 31) read as the audit's
  S6, A1, A7 and A8 describe them, and `pivot_dissociated`
  (`Valuation.lean` lines 371-378) and `exists_int_valuation_companions`
  (`ResidueTree.lean` lines 72-75) as A5 and A4 describe them.
- A sweep of the eight modules for `sorry`, `axiom`, `native_decide`,
  `admit`, `opaque`, `unsafe`, `partial`, `implemented_by`, `extern`,
  `csimp`, `macro`, `notation`, `syntax` and `elab`: no hit (the word
  "relabeling" in a docstring at `IntegerModel.lean` line 94 is the only
  false match).
- The axiom-audit standing in `lean/Manifest.json` at the commit: 3,092
  lines; 2,977 modules, 14 claim declarations and 7 claims; `Erdos.L22` in
  the module list (line 16) and its two declarations (lines 2999-3000); the
  L22 claim row (lines 3080-3092) with `depends` `[]`, `decls` `statement`
  and `claim`, `compiler` `[]`, `axioms` `propext`, `Classical.choice` and
  `Quot.sound`, equal `sha256` and `sha256Unfolded` fields and the
  pretty-printed statement the audit quotes; and the empty top-level
  `compiler` array. The other six claim rows also list the three standard
  axioms and no compiler axiom.
- `lean/README.md` at the commit: it lists L22 among the native claims over
  `Erdos/Problem963/`, states the toolchain and Mathlib pin above, describes
  the audit (the three standard axioms plus admitted compiler axioms, the
  NOTE and FAIL lines and the summary line), the manifest and the gate, and
  says a non-author runs `scripts/gate.sh --clean [rev]` at every native
  tier-2 promotion. It records no dated audit run; the committed manifest is
  the audit's record in the tree.
- The Problem 963 page's Statement block
  (`wiki/problems/number_theory/E0963/_index.md` lines 16-24) for the definition
  of $f(n)$ that the audit's P6 uses, and the proof page `_proof.md` at the
  commit for the sentences the audit's A1-A8 characterize.
- The audit's own line references for the card (statement field 12-21,
  `tier` 23, Statement section 41-64, formal-surface section 66-77) and for
  `L22.lean` (32 lines), and the record's three index pages, which file no
  grade and assign no tier.

**Independence facts, by role.**

- The claim's author, who wrote the formalization and the card, took no
  part in the audit or in this grade.
- The auditor: a statement-fidelity auditor in a fresh context, not the
  author of the claim, its Lean development or its card, given only the
  assignment (subject, reading list, exclusions); read the Lean sources
  without building them, with read-only git; disclosed exposures E1-E8 in
  the report.
- The grader: the author of this record is a distinct grader in a fresh
  context, neither the author of L22 nor its auditor, given only the
  assignment naming the subject, the read set and the rules; built nothing,
  ran no gate, generator or wiki command, and used git read-only; read the
  Mathlib sources from a package checkout at the pinned revision with a
  clean status. The card's `tier` field and standing sections were printed
  with its statement field and did not shape this grade; the environment
  listed untracked review pages of other research folders and recent commit
  subjects, none of which was opened.
- Materiality rulings on the audit's exposures, by the content test: E1 and
  E2 (the card's standing text and the proof page's tier mention) are
  immaterial, since the report's axiom facts cite the manifest rows the
  auditor read and the clause comparison uses no standing text; E3, E5, E6
  and E8 (branch and commit subjects, block headers, manifest names,
  untracked file names) are names and headers only, immaterial; E4 (an L17
  record read for its shape) carries no L22 content, immaterial; E7
  (Mathlib read from another worktree's package checkout at the pinned
  revision) is immaterial, the cited lines having been re-read here at the
  same revision from a clean checkout. Nothing in the report could only have
  come from excluded material, and no comparison followed it.

## Audit graded

**Pass.** The audit meets the contract of `docs/lean_authoring.md`
"Statement fidelity and validation" and the independence rules of
`docs/verification.md`:

- It identified the exact source and Lean revisions: the commit, the tree
  and subtree identities (since restated by date), the toolchain and the
  Mathlib pin, all re-derived above, and a path with line numbers for every
  Lean and Mathlib citation,
  each found where cited.
- It unfolds the necessary definitions (U1-U11) with their sources,
  including the junk values of `Real.log` at zero and at negative arguments
  and the proof that the statement never reaches them (U9), and the closed
  type of the entry theorem (U10).
- It compares every clause: the seven clauses of the statement field
  (P1-P7) for objects, quantifiers, hypotheses, conventions, constants,
  exceptional cases and conclusion; the Statement section (S1-S6); the
  formal-surface sentences (G1-G4); and the proof page's module map (A1-A8).
  The exact specialization to Problem 963's notation (P6, S3) is argued,
  not assumed: $f(n)$ is the largest admissible $k$, the admissible $k$ form
  a downward-closed set of integers containing $0$ and bounded by $n$, so
  $f(n)\ge\beta(n)$ holds exactly when every $n$-element real set has a
  dissociated subset of size at least $\beta(n)$, and the union of these
  cases over $n\ge1$ is the Lean statement. This grader's own comparison
  agrees on every clause, on the equivalence for P6, on the remark S4 (for
  $n\ge2$, $x=\log_2 n\ge1$ gives $\log_2(x+1)\ge1$ and
  $\beta(n)\le x-1<\lfloor x\rfloor$) and on the vacuity analysis: under
  `A.Nonempty` both logarithms take arguments at least $1$, and at $n=1$ the
  bound reads $0\le|B|$, met by the empty set.
- It records the independence facts (role, fresh context, exclusions,
  reading depth per module, exposures) and states its limitations (no build,
  no gate, no review of the `Erdos.Problem963` proofs).
- Its verdict, PASS for the whole statement with `claim` at the type
  `statement` itself, is the verdict this grader reaches: the Lean statement
  is neither weaker nor stronger than the prose, and no prose clause lacks a
  counterpart.

## Tier assertion

**Tier 2 is asserted for L22.** `assumes: compiler` does not apply: no
compiler axiom appears in the claim's row or in the corpus. The conditions
of the tier law (`docs/anatomy.md` "Tiers") and the basis for each:

1. The named Lean declaration exists in the accepted closure: `theorem
   Erdos.L22.claim : statement` with `def Erdos.L22.statement : Prop` in
   `lean/Erdos/L22.lean` at the commit, and the card's `lean` field names
   `Erdos.L22.claim`. Basis: the file and the card at the commit.
2. The declaration passes the axiom audit: the L22 row of
   `lean/Manifest.json` at the commit records the axioms `propext`,
   `Classical.choice` and `Quot.sound` and no compiler axiom, and no
   `sorry`, custom axiom, unsafe or opaque constant, partial definition,
   `implemented_by`, `extern`, `csimp` or metaprogramming command occurs in
   the eight modules of the closure. Basis: the committed manifest, which is
   the `lake exe audit --emit` output that the gate's `--check` re-derives,
   and the sweep above; this grader ran no audit.
3. No compiler axiom: the row's `compiler` list and the top-level `compiler`
   array are empty, so the card carries no `assumes: compiler` and the
   compiler sentence is not owed. Basis: the manifest at the commit.
4. The declaration faithfully renders the whole statement, confirmed by an
   independent whole-statement fidelity audit: the audit graded pass above,
   whose PASS verdict holds under this grader's own comparison. Basis: the
   report and the re-check in "Subject".
5. A fresh-context review graded by a separate fresh-context grader, each
   given only its assignment: the auditor's facts in the report's "Subject
   and independence" and the grader's facts above; author, auditor and
   grader are three distinct roles. Basis: the independence facts above.
6. The clean-checkout Lean gate run by a non-author at promotion, its report
   of any compiler axioms cited in the acceptance: not part of this record
   and not run by this grader, whose assignment forbids running the gate.
   The tier law places it at promotion: the card takes tier 2 when a
   non-author's `lean/scripts/gate.sh --clean` passes on the source of
   2026-09-28 and the acceptance cites this grade and that gate's report,
   which the manifest predicts as `0 compiler axioms`.
7. Dependencies: the claim declares none (`depends_on: []` on the card,
   `depends: []` in the manifest); its closure inside `lean/Erdos/` is the
   seven `Erdos.Problem963` modules, source-local development covered by the
   universal audit and not native claims; no other L-claim is consumed, so
   no dependency needs a tier of its own. Basis: the import closure and the
   manifest at the commit.

## Corrections

None. The audit's one observation, that the proof page words the case split
of `log_bound_of_card_le` as $d\ge\log_2 n$ and $d<\log_2 n$ where the Lean
splits on $d\le\log_2 n$ and its negation, concerns the proof account, not
the statement, and both texts cover the boundary case; no card wording is
required.

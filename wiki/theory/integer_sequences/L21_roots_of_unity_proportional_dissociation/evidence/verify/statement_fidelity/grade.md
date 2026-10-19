---
name: theory/integer_sequences/L21_roots_of_unity_proportional_dissociation/evidence/verify/statement_fidelity/grade
title: Distinct grade of the L21 statement-fidelity audit
desc: |
  A distinct grader's check of the L21 fidelity audit of 2026-09-28: the
  audit is graded pass, its PASS verdict holds under the grader's own
  comparison, and tier 2 is asserted for L21 with no compiler assumption, in
  the batch order L20 before L21.
created: 2026-09-28T19:10:33Z
updated: 2026-09-28T19:10:33Z
---

***

## Subject

The repository as it stood on the default branch at 2026-09-28T13:50:48Z,
the tip of `main` when this grade was written (the checked source, called
"the commit" below); its repository, `lean/`, `lean/Erdos` and
`lean/Erdos/RootsOfUnitySidon` tree identities, each by `git rev-parse` at
the commit, are restated here by that date. The record graded is the
[[theory/integer_sequences/L21_roots_of_unity_proportional_dissociation/evidence/verify/statement_fidelity/report|audit report]]
at
`wiki/theory/integer_sequences/L21_roots_of_unity_proportional_dissociation/evidence/verify/statement_fidelity/report.md`,
the whole-statement fidelity audit of `Erdos.L21.statement` against the
`statement` field of
[[theory/integer_sequences/L21_roots_of_unity_proportional_dissociation/_index|L21]]
at that commit, verdict PASS. The commissioning text placed the claim under
`wiki/theory/number_theory/`; no such folder exists at the commit, and the
card, the audit and this grade live under `wiki/theory/integer_sequences/`.

**Re-checked.** Everything below was read in a linked worktree at the
commit with read-only git; nothing was built, no probe was compiled, and no
`lake`, generator or gate was run. The worktree's tracked tree equals the
commit (`git diff` against the commit on `lean` and the diff of both cards
printed nothing; `git status --short` listed only untracked evidence folders
and review pages of other roles, none opened except as named here).

- The identities: the commit and its four subtree objects (restated by date
  in both records), `lean/lean-toolchain` (`leanprover/lean4:v4.32.0-rc1`),
  the Mathlib revision
  `79aee35d9696d759b73eed71d7dde666750bc35e` at `lean/lakefile.toml` line
  11 and `lean/lake-manifest.json` line 11, and the `lean/Manifest.json`
  lines the report cites (module list line 15, declarations lines
  2,997-2,998, the L21 row lines 3,067-3,079 with its pretty statement at
  line 3,071); all equal the report's.
- The card at the commit through `git show`: the `statement` field (lines
  12-19), the Statement section (lines 39-53, its Scope paragraph at 48-53)
  and the line ranges the report puts outside its subject (72-97); and the
  proof page `_proof.md` in full.
- `lean/Erdos/L21.lean` (36 lines) in full with its three imports;
  `RootsOfUnitySidon.lean` lines 1-70 (`rootsOfUnity` line 33,
  `UniformExtraction` lines 44-46, `statement` line 49, `AnalyticSidon`
  lines 54-58) and the declaration names of lines 996-1068;
  `RootsOfUnitySidonComplete.lean`, `RootsOfUnitySidonPisier.lean`,
  `PisierForwardComplete.lean` and `RootsOfUnitySidonAnalytic.lean` in full;
  `SidonExtraction.lean` lines 1-5, 20-30, 85-95 and 200-240; all under
  `lean/Erdos/RootsOfUnitySidon/` at the commit.
- Mathlib at the pinned revision, read from the main checkout's package
  tree `lean/.lake/packages/mathlib` (its `HEAD` equals the pin, status
  clean; the worktree has no `lean/.lake/`):
  `Mathlib/GroupTheory/OrderOfElement.lean` lines 40-80,
  `Mathlib/Combinatorics/Additive/Dissociation.lean` lines 20-60,
  `Mathlib/Data/Set/Operations.lean` lines 295-302,
  `Mathlib/Dynamics/PeriodicPts/Defs.lean` lines 60-66 and 197-202,
  `Mathlib/Data/Finset/Defs.lean` lines 124-128 and 222-233,
  `Mathlib/Data/Finset/Card.lean` lines 45-49, and
  `Mathlib/Data/Complex/Basic.lean` lines 116-119, 141-144, 163-166,
  205-208, 323-328 and 375-382; core `Init/Prelude.lean` lines 1889-1904
  from the elan toolchain directory for `v4.32.0-rc1`.
- The manifest's L20 and L21 rows and its top-level `compiler` array by
  script, and `lean/README.md` lines 1-136 and 195-235.
- The L20 card at the commit, and the L20 audit report at
  `wiki/theory/integer_sequences/L20_roots_of_unity_analytic_sidon/evidence/verify/statement_fidelity/report.md`
  for its subject and verdict, since L21 declares L20 as a dependency; no
  grade of it was in its folder when this grade was written.
- The contract: `docs/anatomy.md` "Tiers"; `docs/lean_authoring.md`
  "Statement fidelity and data discipline" and "Statement fidelity and
  validation"; `docs/verification.md` "Independence and the assignment",
  "Exact subjects and durable evidence", "Grading and claim standing",
  "Whole-claim report" and "Durable reports and current standing"; and
  `docs/compiler_trust.md` in full.
- For shape only: the folder listing of the L17 record
  `wiki/theory/ramsey_theory/L17_rainbow_odd_cycle_threshold/evidence/verify/statement_fidelity/`,
  its `grade.txt` lines 1-120 and the L17 card's Current standing section.

**Not read.** Any research page, library card or PDF; the audit program and
the refusal suite; the proof modules of `lean/Erdos/RootsOfUnitySidon/`
beyond the ranges above; any other claim's records beyond the L20 report
and the L17 shapes named; anything among the private working files.

**Grader's own exposures.** The generated views' L20 and L21 rows
(standing words), the subject lines of the five most recent commits
touching `lean/` and the body of the last one (the L22 delivery, which
says the manifest was regenerated there), the L17 card's standing text,
which discloses a model name, the L19 tail and L22 head of the manifest
range read, and the untracked paths of other roles in `git status`. None
concerns the fidelity of L21; nothing in this grade comes from them.

**Independence facts by role.**

- Author: the formalization author and integrating author of the delivery
  commit of 2026-09-25T23:49:11Z, who recorded the claim at tier 0 on its
  card.
- Auditor: the independent fidelity auditor for L21, in a fresh context,
  who took no part in writing the claim, its Lean development or its card,
  audited by reading alone, and disclosed exposures E1-E7 in the report.
- Grader: the author of this record, a distinct grader in a fresh context,
  separately assigned and given only its assignment; not the author of the
  claim, its Lean modules, its card or its proof page, not the auditor, and
  not the runner of any gate.

**Rulings on the disclosed exposures.** By the content test, each of E1-E7
is immaterial: nothing in the report could only have come from it, and a
fidelity comparison has no attack direction to follow. E1 and E2 expose
standing text (the views' rows and the card's `tier` field and standing
sections), which carries no verdict on fidelity and which the report keeps
outside its subject; the comparison's content is derived from the
`statement` field, `lean/Erdos/L21.lean` and the unfolded sources. E3 and
E5 are other claims' records read for shape, with no L21 content; E5 is
disclosed as a reading the assignment excluded, and its frontmatter lines
carry nothing about L21. E4 and E7 are history metadata, folder names and
untracked paths. E6 is a read of pinned upstream sources at the pinned
revision from a clean checkout, which this grade repeated.

## Audit graded

**Pass.** The report meets the contract for a whole-statement fidelity
audit, and its PASS verdict holds under the grader's own comparison.

- Complete comparison. The report splits the `statement` field into its
  eight clauses P1-P8, gives each its Lean counterpart after the unfolding
  steps U1-U10, and closes the converse direction: the five atoms of the
  unfolded `Erdos.L21.statement` are P4-P7, and no hypothesis, parameter,
  instance argument or side condition beyond them is present. It examines
  binder domains, the empty set, the exponent $0$, $0 \notin R$ and every
  coercion, and it checks that `Erdos.L21.claim` is declared at exactly
  `statement` with no binders and that the proof path to its two
  argument-free inputs leaves no hypothesis open. The one wording
  difference between the `statement` field and the Statement section is
  named and resolved (P1 and P2).
- Resolving revisions. The commit, its trees, the toolchain, the Mathlib
  revision and the manifest lines were stated by git identity when written
  (the commit and trees since restated by date), and each re-derived value
  above equaled the report's. The reading depth per module
  and page is tabulated.
- Independence. The auditor's role and its fresh-context, reading-only
  facts are stated, exposures are disclosed rather than omitted, and none
  is material (rulings above).
- The grader's own check confirms every finding. `IsOfFinOrder z` is
  `(1 : ℂ) ∈ periodicPts (z * ·)` under `[Monoid ℂ]`, the multiplicative
  monoid of `Complex.commRing` (the additive predicate would be
  `IsOfFinAddOrder`, and no `Multiplicative` wrapper appears), and it is
  `∃ n : ℕ, 0 < n ∧ z ^ n = 1` by `isOfFinOrder_iff_pow_eq_one`: the
  prose's $z^n = 1$ for an integer $n \ge 1$. `AddDissociated (↑B)` is
  `{t : Finset ℂ | ↑t ⊆ ↑B}.InjOn (∑ x ∈ ·, x)` under `[AddCommGroup ℂ]`,
  which by `Set.InjOn` reads: two finsets contained in `B` with equal sums
  are equal, the contrapositive of "distinct finite subsets of $B$ have
  distinct sums", the empty subset included on both sides. `0 < k` is
  `Nat.le 1 k`; `Finset.card` is `Multiset.card s.1`; `↑A ⊆ rootsOfUnity`
  is `∀ a, a ∈ A → IsOfFinOrder a` by `coe_subset`, `subset_iff` and
  `mem_coe`, each `Iff.rfl`; `A.card ≤ k * B.card` is in `ℕ` with no cast.
  Delta-unfolding `Problem774.statement`, `Problem774.UniformExtraction`,
  `Problem774.rootsOfUnity` and `L21.rootsOfUnity` gives the body of
  `Erdos.L21.statement` symbol for symbol, and
  `rootsOfUnity_proportionalDissociation` applies
  `statement_of_analyticSidon_of_pisier` to `pisierForward` and
  `rootsOfUnity_analyticSidon`, both without arguments, through
  `statement_iff_pisier_interface`, which is `rfl` against
  `SidonExtraction.UniformExtraction` and `FiniteExtraction`. The two
  lemmas the report names in passing are where it says: the additive form
  of `mulDissociated_empty` at Dissociation.lean line 55, and
  `zero_not_mem_rootsOfUnity` at `RootsOfUnitySidonPisier.lean` lines
  14-18.
- Limits stated honestly. The report asserts nothing about the value of
  $k$, Problem 774's question, the library proof's correctness, novelty or
  acceptance, and says it built nothing; the build is the gate's leg, not
  a defect of the audit.

## Tier assertion

**Tier 2 is asserted for L21** for the checked source of 2026-09-28 (the
commit above), under the tier law of
`docs/anatomy.md` "Tiers", for the `statement` field of the card at that
commit, kernel-only. The conditions and their bases:

1. The named Lean declaration exists here. `Erdos.L21.claim : statement`
   at `lean/Erdos/L21.lean` lines 33-34, with `Erdos.L21.statement` at
   lines 24-27; the L21 row of `lean/Manifest.json` lists both, roles
   statement and claim, module `Erdos.L21`.
2. The proof passes the axiom audit. The L21 row records the axioms
   `propext`, `Classical.choice` and `Quot.sound` and `compiler: []`; the
   top-level `compiler` array is empty; no `sorryAx` and no custom axiom
   appears. The manifest is what `lake exe audit --emit` wrote and
   `--check` re-derives byte for byte; it was regenerated in the last
   `lean/` change before the commit (2026-09-28T02:53:51Z), and the card's
   author-recorded standing states that the full gate passes on the
   delivery tree. `lean/README.md` records the audit's rule and names L21
   among the claims; it records no dated run, and a retained manifest does
   not by itself establish a fresh build.
3. `assumes: compiler` does not apply. No compiler axiom appears in the
   row or in the top-level array, so the card carries no `assumes` key and
   no compiler sentence, and the standing says kernel-only.
4. The declaration faithfully renders the whole statement, confirmed by an
   independent whole-statement fidelity audit graded pass by a distinct
   grader, each in a fresh context and given only its assignment (this
   record and the report it grades).
5. Dependencies inside the accepted closure. The kernel proof reaches only
   source modules of `lean/Erdos/RootsOfUnitySidon/` and no other L-claim
   (`depends: []`). The card's declared dependency L20 is the analytic
   input: `rootsOfUnity_analyticSidon : AnalyticSidon`, and the L20 audit
   records `Erdos.L20.statement` as that proposition after unfolding. L20
   is at tier 0 at the commit, and its own fidelity audit at the same
   commit, in this batch, has verdict PASS. Batch order: L20 before L21.
   This assertion takes effect in that order and falls if the L20 audit is
   graded void.
6. The clean-checkout gate. The tier law places a non-author run of
   `lean/scripts/gate.sh --clean` on the source of 2026-09-28 at promotion,
   cited in the acceptance with its report of compiler axioms (zero
   expected). No such
   record is in this folder, and this grade does not supply it; whoever
   files the promotion cites it and asserts no tier of their own.

The acceptance is of this commit only: a later commit that changes `lean/`
or the `statement` field needs the legs again.

## Corrections

None. The `statement` field needs no repair, and the card carries no
`assumes: compiler` key, since its row records no compiler axiom.

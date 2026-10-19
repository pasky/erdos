---
name: theory/number_theory/L22_near_logarithmic_dissociated_subset/evidence/verify/statement_fidelity/report
title: Statement-fidelity audit of L22 on 2026-09-28
desc: |
  The independent whole-statement fidelity audit comparing the L22 card's
  prose statement with Erdos.L22.statement as they stood on 2026-09-28;
  verdict PASS, and no tier is assigned.
created: 2026-09-28T18:01:07Z
updated: 2026-09-28T20:42:32Z
---

***

Verdict for the whole statement: **PASS**. At the checked source of
2026-09-28 (below), `Erdos.L22.statement` states
exactly the prose statement of
[[theory/number_theory/L22_near_logarithmic_dissociated_subset/_index|the L22 card]],
and `Erdos.L22.claim` proves exactly `statement`. This audit assigns no tier
itself.

## Subject and independence

### Role

This record is an independent statement-fidelity audit of the native claim
L22, written in a fresh context by an auditor who took no part in writing the
claim, its Lean development or its card, and who received only the assignment
naming the subject, the reading list and the exclusions. The auditor read the
Lean sources and did not build them: no `lake` command, no generator, no wiki
command and no gate was run, and every git command was read-only
(`git rev-parse`, `git show`, `git status`). The card's `tier` field and its
"Current standing", "Verification" and "Remaining obligations" sections are
outside the subject and did not shape the verdict. Everything among the private
working files, the audits of other claims and any standing or acceptance text
were excluded from the reading.

### Subject, by path and date

| Object | Identity |
|---|---|
| checked source | the default branch as it stood at 2026-09-28T13:50:48Z |
| repository, `lean/`, `lean/Erdos`, `lean/Erdos/Problem963` and claim folder trees | taken by `git rev-parse` at the checked source; restated by its date |
| toolchain | `leanprover/lean4:v4.32.0-rc1` |
| Mathlib pin | `79aee35d9696d759b73eed71d7dde666750bc35e` |

The checked source is called "the commit" below; the claim folder is
`wiki/theory/number_theory/L22_near_logarithmic_dissociated_subset`. The
toolchain is `lean/lean-toolchain`; the Mathlib pin is the `rev` of
`lean/lakefile.toml` (line 11) and of `lean/lake-manifest.json` (lines 8 and
11). The worktree read was checked out at the commit with a clean tracked
tree, so its files equal the committed blobs; the card and the proof page were
read through `git show` at the commit.

**Prose subject.** The `statement` field of the card (lines 12-21 at the
commit), with its convention sentence (the definition of dissociation and the
base of the logarithm) and its Scope sentence (the closing "Nothing is asserted
about ..."); the card's "Statement" section (lines 41-64) and "Argument and
formal surface" section (lines 66-77) for the same clauses and for the
sentences that characterize the Lean; and the body of the proof page
`_proof.md` (lines 16-68) for its sentences that characterize the Lean
modules. The Problem 963 page's Statement block
(`wiki/problems/number_theory/E0963/_index.md` lines 16-24) was read only for the
definition of $f(n)$ that the statement's consequence sentence uses.

**Lean subject.** `Erdos.L22.statement` (a `def` of type `Prop`, lines 23-27)
and `Erdos.L22.claim` (a `theorem`, lines 29-30) in `lean/Erdos/L22.lean`; the
claim's import closure under `lean/Erdos/`, which is `Erdos.L22` together with
the seven modules under `lean/Erdos/Problem963/` (`BinaryWords`,
`BitValuation`, `CardBound`, `IntegerModel`, `LogBound`, `ResidueTree` and
`Valuation`; their import lines reach only one another and Mathlib, and no
other module under `lean/Erdos/` imports any of them or `Erdos.L22`); the L22
rows of `lean/Manifest.json` (module list line 16, declarations lines
2999-3000, claim row lines 3080-3092; the manifest lists 2,977 modules, 14
claim declarations and 7 claims); `lean/lean-toolchain`; and Mathlib at the
pin.

### Reading depth

Modules of the closure, at the commit:

- `lean/Erdos/L22.lean`: in full (32 lines).
- `lean/Erdos/Problem963/CardBound.lean`: in full (175 lines).
- `lean/Erdos/Problem963/LogBound.lean`: in full (40 lines).
- `lean/Erdos/Problem963/IntegerModel.lean`: import lines 1-7, the docstrings
  and declaration headers at lines 20-35, 55-66, 93-105 and 129-145, and
  lines 37 and 63 by a search for the Mathlib lemma names the proof page
  cites; the proofs were not read.
- `lean/Erdos/Problem963/Valuation.lean`: import lines 1-4 and the
  declaration headers at lines 23-30, 39-45, 73-80, 93-100 and 371-386.
- `lean/Erdos/Problem963/ResidueTree.lean`: import lines 1-4 and the
  declaration headers at lines 24-31 and 72-80.
- `lean/Erdos/Problem963/BinaryWords.lean`: import lines 1-3 and lines
  15-17, 57-60, 128-131, 168-171, 287-292 and 328-336.
- `lean/Erdos/Problem963/BitValuation.lean`: import lines 1-2 and lines
  48-55.
- All eight modules: every declaration header line (a search for `theorem`,
  `lemma`, `def`, `abbrev`, `structure`, `instance` and `inductive`), the
  `namespace` and `end` lines, and a sweep for `sorry`, `axiom`,
  `native_decide`, `admit`, `opaque`, `unsafe`, `implemented_by`, `extern`,
  `set_option`, `open`, `notation`, `macro`, `instance`, `variable` and
  `section`. The sweep's only hits are `set_option autoImplicit false` in
  `L22.lean` and the `namespace` and `end` pairs (`Erdos.L22` once,
  `Erdos.Problem963` in each of the seven modules).
- `lean/Manifest.json`: lines 10-20, 2990-3002 and 3080-3092, and the sizes
  of its `modules`, `declarations` and `claims` arrays by loading the file.
- `lean/lean-toolchain` in full; `lean/lakefile.toml` lines 9-13;
  `lean/lake-manifest.json` lines 7-13.

Mathlib at revision `79aee35d9696d759b73eed71d7dde666750bc35e`, read from
the package checkout `lean/.lake/packages/mathlib` of another worktree of
this repository (the audited worktree holds no `.lake/`), whose git HEAD is
that revision with a clean status:

- `Mathlib/Combinatorics/Additive/Dissociation.lean` lines 1-70.
- `Mathlib/Analysis/SpecialFunctions/Log/Base.lean` lines 39-53 and the
  statements at lines 74, 81 and 236.
- `Mathlib/Analysis/SpecialFunctions/Log/Basic.lean` lines 38-61, 102-104
  and 114-121.
- `Mathlib/Data/Set/Operations.lean` lines 298-300.
- `Mathlib/Data/Finset/Defs.lean` lines 96-128, 152-154, 176-196 and
  222-233.
- `Mathlib/Data/Finset/Empty.lean` line 47.
- `Mathlib/Data/Finset/Card.lean` lines 45-48.
- `Mathlib/Algebra/BigOperators/Group/Finset/Defs.lean` lines 65-70 and 359.
- `Mathlib/Data/Nat/Log.lean` lines 59-68.

Prose and contract pages, at the commit: the card in full (exposure E1
below); the proof page in full; the Problem 963 page's block header lines and
its Statement block (lines 16-24); `docs/lean_authoring.md` "Statement
fidelity and data discipline" (lines 286-349) and "Statement fidelity and
validation" (lines 478-546); `docs/anatomy.md` "Tiers" (lines 298-344);
`docs/verification.md` "Exact subjects and durable evidence" (lines 163-211)
and "Whole-claim report" (lines 573-603); and, for the shape of this record,
the precedent folder
`wiki/theory/ramsey_theory/L17_rainbow_odd_cycle_threshold/evidence/verify/statement_fidelity/`
(a listing, its `_index.md`, the two index pages above it, and sections 1-3,
5, 10, 14 and 15 of its `review.txt`).

### Exposures

- E1. The card was printed in full to read its statement field and sections.
  This exposed its `tier` field (line 23) and its "Current standing",
  "Verification" and "Remaining obligations" sections (lines 79-104), which
  say that the claim is author-recorded, that the gate passed on the
  author's tree and that no fidelity audit has been run. None of that text
  is a verdict on fidelity, and none of it was used in the comparison or
  the verdict.
- E2. The proof page's opening sentence names the claim's tier; standing
  text, not used.
- E3. The operating environment displayed the branch name and the subject
  lines of five recent commits, about a library re-render and proof
  reconstructions; none names L22, and no diff was read.
- E4. The precedent record's pages were read for their shape; they concern
  L17 and carry no L22 content.
- E5. Locating the Problem 963 page's Statement block displayed its block
  header lines, among them the "Status." line and the first line of the
  "Formalization." paragraph; only the Statement block was read.
- E6. The manifest's module and declaration lists show the names of the
  other claims' modules and declarations; names only.
- E7. The Mathlib sources were read outside the audited worktree, from
  another worktree's package checkout at the pinned revision; the bytes are
  Mathlib's at that revision, not this repository's, and their git status
  was clean.
- E8. A final `git status` of the worktree listed untracked evidence
  folders of other claims and untracked research review pages being
  written concurrently by other roles; their names were seen, and none was
  opened. The tracked tree stayed clean throughout.

Nothing else outside the assignment was read.

## Lean statement and definitions unfolded

### The Lean text at the commit

`lean/Erdos/L22.lean` lines 17-32, verbatim (lines 1-15 are the three import
lines, `Mathlib.Analysis.SpecialFunctions.Log.Base`,
`Mathlib.Combinatorics.Additive.Dissociation` and
`Erdos.Problem963.CardBound`, and the module docstring):

```lean
set_option autoImplicit false

namespace Erdos.L22

/-- Every nonempty finite real set `A` has a dissociated subset of size at
least `log₂ |A| - log₂ (log₂ |A| + 1)`. -/
def statement : Prop :=
  ∀ A : Finset ℝ, A.Nonempty →
    ∃ B : Finset ℝ, B ⊆ A ∧ AddDissociated (↑B : Set ℝ) ∧
      Real.logb 2 (A.card : ℝ) -
        Real.logb 2 (Real.logb 2 (A.card : ℝ) + 1) ≤ (B.card : ℝ)

theorem claim : statement :=
  Erdos.Problem963.exists_real_dissociated_large

end Erdos.L22
```

The file has no `variable`, `open`, `notation`, `macro`, `instance`, `axiom`
or attribute command. The manifest's claim row (`lean/Manifest.json` lines
3080-3092) records module `Erdos.L22`, id `L22`, `depends` `[]`, `decls`
`statement` (role statement) and `claim` (role claim), `compiler` `[]`,
`axioms` `["propext", "Classical.choice", "Quot.sound"]`, and prints the
statement as

```
∀ (A : Finset ℝ),
  A.Nonempty →
    ∃ B ⊆ A,
      AddDissociated ↑B ∧ Real.logb 2 ↑A.card - Real.logb 2 (Real.logb 2 ↑A.card + 1) ≤ ↑B.card
```

which is the source text with `∃ B ⊆ A, P` as the printer's sugar for
`∃ B, B ⊆ A ∧ P`. Its `sha256Unfolded` equals its `sha256`, as it must for a
statement with no named parts in the claim's own namespace.

### Definitions unfolded

- U1. `Finset ℝ` is Mathlib's type of finite sets of reals (a multiset with
  no duplicate). `Finset.Nonempty s := ∃ x : α, x ∈ s`
  (`Mathlib/Data/Finset/Empty.lean` line 47). So the binder
  `∀ A : Finset ℝ, A.Nonempty →` ranges over every nonempty finite set of
  real numbers and nothing else; sets containing 0 or negative numbers are
  included.
- U2. `Finset.card s := Multiset.card s.1` (`Mathlib/Data/Finset/Card.lean`
  lines 47-48), the number of elements; `(A.card : ℝ)` and `(B.card : ℝ)`
  are its `Nat.cast` into ℝ, and `≤` is the order of ℝ.
- U3. `B ⊆ A` on finsets: `Finset.subset_iff`, which states
  `s₁ ⊆ s₂ ↔ ∀ ⦃x⦄, x ∈ s₁ → x ∈ s₂`, is `Iff.rfl`
  (`Mathlib/Data/Finset/Defs.lean` lines 224-225).
- U4. `(↑B : Set ℝ)` is the `SetLike` coercion `coe s := {a | a ∈ s.1}`
  (`Defs.lean` lines 100-103); `Finset.mem_coe` is `Iff.rfl` (lines
  126-127), `Finset.coe_subset`, which states `(s₁ : Set α) ⊆ s₂ ↔ s₁ ⊆ s₂`,
  is `Iff.rfl` (lines 231-232), and `Finset.coe_injective` (line 153) makes
  finsets and their underlying sets correspond one to one.
- U5. `AddDissociated` is the `to_additive` twin of `MulDissociated`
  (`Mathlib/Combinatorics/Additive/Dissociation.lean` lines 41-45, under
  `variable {α : Type*} [CommGroup α]` at line 31), defined by

  ```lean
  def MulDissociated (s : Set α) : Prop :=
    {t : Finset α | ↑t ⊆ s}.InjOn (∏ x ∈ ·, x)
  ```

  so that for `[AddCommGroup α]` it reads
  `AddDissociated s := {t : Finset α | ↑t ⊆ s}.InjOn (∑ x ∈ ·, x)`. Its
  docstring: "A set is dissociated iff all its finite subsets have
  different sums."

- U6. `Set.InjOn f s := ∀ ⦃x₁⦄, x₁ ∈ s → ∀ ⦃x₂⦄, x₂ ∈ s → f x₁ = f x₂ → x₁ = x₂`
  (`Mathlib/Data/Set/Operations.lean` lines 299-300). With U4 and U5,
  `AddDissociated (↑B : Set ℝ)` unfolds to: for all `t u : Finset ℝ` with
  `t ⊆ B` and `u ⊆ B`, if `∑ x ∈ t, x = ∑ x ∈ u, x` then `t = u`.
- U7. `∑ x ∈ t, x` is `Finset.sum t (fun x => x)`, the additive twin of
  `Finset.prod s f := (s.1.map f).prod`
  (`Mathlib/Algebra/BigOperators/Group/Finset/Defs.lean` lines 68-69);
  `Finset.sum_empty`, which states `∑ x ∈ ∅, f x = 0`, is the additive twin
  of line 359. The empty finset is in the domain of U6 (`∅ ⊆ B`) and its
  sum is 0.
- U8. `Real.logb (b x : ℝ) : ℝ := log x / log b`
  (`Mathlib/Analysis/SpecialFunctions/Log/Base.lean` lines 43-44), with
  `Real.log x := if x = 0 then 0 else expOrderIso.symm ⟨|x|, _⟩`
  (`Mathlib/Analysis/SpecialFunctions/Log/Basic.lean` lines 44-45): for
  `x > 0` it is the inverse of `exp` (`exp_log`, line 58), `log 0 = 0`
  (line 102) and `log (-x) = log x` (line 120); hence `logb b 0 = 0`
  (`Base.lean` line 50) and `logb b (-x) = logb b x` (line 81). With
  `b = 2`, `log 2 > 0`, so for `x > 0` the value `Real.logb 2 x` is the
  real logarithm of `x` to base two. The literal `2` is `(2 : ℝ)`.
- U9. Junk values and vacuity. Under `A.Nonempty`, `1 ≤ A.card`, so
  `(1 : ℝ) ≤ ↑A.card`, `0 ≤ Real.logb 2 ↑A.card` (`Real.logb_nonneg`,
  `Base.lean` line 236) and `1 ≤ Real.logb 2 ↑A.card + 1`: both logarithms
  in the statement are applied to arguments at least 1, and the junk values
  of `Real.log` at 0 and at negative arguments are never reached. At
  `A.card = 1` both logarithms are 0, the bound reads `0 ≤ ↑B.card`, and
  `B = ∅` satisfies it (`addDissociated_empty`, `Dissociation.lean` lines
  55-56), as the prose's bound at $n = 1$ also reads. Without the
  nonemptiness hypothesis the case `A = ∅` would be decided by the junk
  value `logb 2 0 = 0`; both texts exclude that case, and neither depends
  on the junk value. No other binder could make a clause vacuous: `B` is
  existential, and the universal binders `t`, `u` of U6 range over all
  subfinsets of `B`.
- U10. `Erdos.Problem963.exists_real_dissociated_large`
  (`lean/Erdos/Problem963/CardBound.lean` lines 155-159) has the binders
  `(A : Finset ℝ) (hA : A.Nonempty)` before the colon and the type

  ```lean
  ∃ B : Finset ℝ, B ⊆ A ∧ AddDissociated (B : Set ℝ) ∧
    Real.logb 2 (A.card : ℝ) -
      Real.logb 2 (Real.logb 2 (A.card : ℝ) + 1) ≤ (B.card : ℝ)
  ```

  after it, so its closed type is `statement` after unfolding the one
  definition `statement`; the only textual difference, `(B : Set ℝ)`
  against `(↑B : Set ℝ)`, is two spellings of the same coercion (U4).
  `theorem claim : statement := ...` declares `claim` at the type
  `statement` itself, and the manifest lists it in the claim role with the
  three standard axioms and no compiler axiom. So `claim` proves exactly
  `statement`, not a fragment, a specialization or a variant.

- U11. `Nat.log b n`, used only by the interior theorem
  `integer_card_le_pow` that the card's Statement section names, is the
  largest `k` with `b ^ k ≤ n` (`Mathlib/Data/Nat/Log.lean` lines 59-63),
  that is $\lfloor\log_2(d+1)\rfloor$ at `b = 2` and `n = d + 1`.

## Clause-by-clause comparison

Read as one sentence, the Lean says: for every nonempty finite set $A$ of
real numbers there is a finite set $B\subseteq A$ such that any two subsets
of $B$ with the same sum are equal (the empty subset, with sum 0, included),
and the real number $\log_2|A|-\log_2(\log_2|A|+1)$ is at most $|B|$. The
clauses of the prose subject are numbered P (the card's `statement` field,
lines 13-21), S (the card's "Statement" section, lines 43-64), G (the card's
"Argument and formal surface" section, lines 68-77) and A (the proof page's
body, lines 18-68). "Faithful" means the Lean counterpart has exactly the
clause's strength; "matches" means a sentence that characterizes the Lean is
true of the Lean at the cited lines; "remark" means a sentence about the
mathematics that is not a clause of the claim, checked for truth and not
asserted by the Lean.

| Clause | Prose | Lean counterpart | Verdict |
|---|---|---|---|
| P1 | dissociation convention | `AddDissociated ↑B` (U5-U7) | faithful |
| P2 | nonempty finite A of reals | `A.Nonempty`, `A.card` (U1-U2) | faithful |
| P3 | log_2 is the base-two logarithm | `Real.logb 2` (U8-U9) | faithful |
| P4 | A contains a dissociated B | `∃ B, B ⊆ A ∧ ...` (U3, U5) | faithful |
| P5 | size of B at least the bound | the `≤` clause (U2, U8) | faithful |
| P6 | f(n) ≥ the bound, all n ≥ 1 | consequence of the statement | faithful |
| P7 | scope: nothing more asserted | one conclusion, nothing more | faithful |
| S1-S2 | convention and theorem | as P1-P5 | faithful |
| S3 | the bound as f(n) ≥ ... | as P6 | faithful |
| S4 | weaker than floor(log_2 n) | not a clause; true | remark |
| S5 | no upper bound, no answer | as P7 | faithful |
| S6 | interior theorem and transfer | three theorems, cited below | matches |
| G1-G4 | formal surface | L22.lean, closure, manifest | matches |
| A1-A8 | proof page module map | the named declarations | matches |

### Clause detail

- P1. "A set B of real numbers is additively dissociated if distinct finite
  subsets of B have distinct sums, the empty subset with sum 0 included."
  Lean: `AddDissociated (↑B : Set ℝ)`, which by U5-U7 says that any two
  finsets `t, u ⊆ B` with equal sums are equal; the finsets `t ⊆ B` are
  exactly the subsets of the finite set `B`, all of them finite (U4), the
  empty finset is among them and its sum is 0 (U7). Same objects, same
  quantifier (all pairs of subsets), same conclusion (distinct sums).
  Faithful.
- P2. "Let A be a nonempty finite set of real numbers with n = |A|
  elements". Lean: `∀ A : Finset ℝ, A.Nonempty →` (U1); `n` is `A.card`
  (U2). Every nonempty finite set of reals, and only those. Faithful.
- P3. "write log_2 for the logarithm to base two". Lean: `Real.logb 2`,
  which on the arguments the statement applies it to, all at least 1 (U9),
  is the real logarithm to base two (U8). Faithful.
- P4. "Then A contains an additively dissociated subset B". Lean:
  `∃ B : Finset ℝ, B ⊆ A ∧ AddDissociated (↑B : Set ℝ)` (U3, P1).
  Faithful.
- P5. "with |B| >= log_2 n - log_2(log_2 n + 1)". Lean:
  `Real.logb 2 ↑A.card - Real.logb 2 (Real.logb 2 ↑A.card + 1) ≤ ↑B.card`,
  an inequality in ℝ between the real bound and the cast size of `B` (U2,
  U8); the parse is the outer logarithm minus the logarithm of the outer
  logarithm plus one, at most the size, as the manifest's printed form
  confirms. Same constants (base 2, the added 1), same direction. Faithful.
- P6. "In the notation of Problem 963 this gives f(n) >= log_2 n -
  log_2(log_2 n + 1) for every integer n >= 1." The Problem 963 page
  defines $f(n)$ as the maximal $k$ such that every set $A\subset\mathbb R$
  of size $n$ has a dissociated $B\subseteq A$ with $|B|\ge k$, dissociated
  meaning that the sums over all $S\subseteq B$ are distinct, the same
  convention as P1. Write $\beta(n)$ for the bound. Since $f(n)$ is an
  integer and every $k\le f(n)$ is admissible, $f(n)\ge\beta(n)$ holds if
  and only if $\lceil\beta(n)\rceil$ is admissible, if and only if every
  $A$ of size $n$ has a dissociated $B\subseteq A$ with $|B|\ge\beta(n)$,
  as $|B|$ is an integer. That is the Lean statement restricted to finsets
  of size $n$, and the union over $n\ge1$ of these restrictions is the Lean
  statement, since every nonempty finset has some size $n\ge1$. The Lean
  names no $f$; the sentence is a restatement in the problem's notation
  with exactly the statement's strength. Faithful.
- P7. "Nothing is asserted about whether f(n) >= floor(log_2 n), about any
  upper bound on f(n), or about the sharpness of this bound." The Lean
  statement has the single conclusion of P4-P5; it states no floor bound
  (and implies none, since $\beta(n)<\lfloor\log_2 n\rfloor$ for $n\ge2$,
  S4), no upper bound on any quantity and no sharpness. The Lean asserts
  nothing the Scope sentence excludes. Faithful.
- S1-S2. The "Statement" section restates P1, P2, P4 and P5 with
  $B\subset\mathbb R$, $A\subset\mathbb R$ and the bound in display form;
  the words and the constants are the same. Faithful.
- S3. "In the notation of Problem 963 this is the near-logarithmic lower
  bound f(n) ≥ log_2 n − log_2(log_2 n + 1) for every n ≥ 1, the bound
  proved in prose by the section ... of the proof sketch." As P6. The
  attribution to the research page is outside the subject and was not
  checked. Faithful.
- S4. "It is weaker than the asked ⌊log_2 n⌋ by the log_2(log_2 n + 1)
  term: the two agree only at n = 1, and the bound lies strictly below
  ⌊log_2 n⌋ for every n ≥ 2." A remark about the bound, not a clause of the
  claim. Checked: at $n=1$ both sides are 0; for $n\ge2$ put
  $x=\log_2 n\ge1$, so $\log_2(x+1)\ge1$ and $\beta(n)\le x-1<\lfloor x\rfloor$.
  True. The Lean asserts nothing about $\lfloor\log_2 n\rfloor$, correctly.
  Remark.
- S5. "The claim gives no upper bound on f(n) and does not answer the
  problem." As P7. Faithful.
- S6. "The interior theorem `integer_card_le_pow` proves the sharper
  estimate |S| ≤ 2^(d + ⌊log_2(d+1)⌋), with d the largest size of a
  dissociated subset, for finite integer sets only; the development
  transfers only the product form (d+1)2^d to real sets, and the claim's
  bound follows from that form." `integer_card_le_pow` (`CardBound.lean`
  lines 142-145) takes `S : Finset ℤ`, `d : ℕ` and
  `hbound : ∀ B : Finset ℤ, B ⊆ S → AddDissociated (B : Set ℤ) → B.card ≤ d`
  and concludes `S.card ≤ 2 ^ (d + Nat.log 2 (d + 1))` (U11); it takes any
  upper bound `d` on the sizes of dissociated subsets, of which the largest
  size is an instance, and is stated for integer finsets only.
  `real_card_bound_of_integer_card_bound` (`IntegerModel.lean` lines
  131-137) transfers only a hypothesis of the form
  `S.card ≤ (d + 1) * 2 ^ d` to `Finset ℝ`; `log_bound_of_card_le`
  (`LogBound.lean` lines 15-17) derives the statement's bound from
  `n ≤ (d + 1) * 2 ^ d` with `0 < n`. Matches.
- G1. "states the bound in `Erdos.L22.statement` over Mathlib's
  `AddDissociated` and `Real.logb`, so no project definition is restated
  and no bridge lemma is needed". `L22.lean` declares only `statement` and
  `claim`, and `statement` names only Mathlib constants (U1-U8). Matches.
- G2. "derives `Erdos.L22.claim` from
  `Erdos.Problem963.exists_real_dissociated_large` in
  `lean/Erdos/Problem963/CardBound.lean`". `L22.lean` lines 29-30 and
  `CardBound.lean` lines 155-159 (U10). Matches.
- G3. "The development under `lean/Erdos/Problem963/` (seven modules in the
  namespace `Erdos.Problem963`) is the checked form of the binary
  residue-tree argument of the proof sketch." Seven modules, each opening
  `namespace Erdos.Problem963`. Matches; the comparison with the research
  page is outside the subject.
- G4. "No other native L-claim is used as a premise." The closure's import
  lines reach only the seven `Erdos.Problem963` modules and Mathlib, and
  the manifest row's `depends` is `[]`. Matches.
- A1. The entry point "takes a dissociated subset B of A of maximum size
  (`Finset.exists_max_image`), applies
  `real_card_bound_of_integer_card_bound` to `integer_card_bound` to get
  |A| ≤ (|B|+1)2^|B|, and finishes with `log_bound_of_card_le`":
  `CardBound.lean` lines 160-173, the three calls at lines 164, 171 and
  173. "This proves the entire statement of L22": the entry theorem's
  closed type is `statement` (U10). Matches.
- A2. `BinaryWords.lean`: "a set of more than 2^h words contains a word with
  h+1 companions at pairwise distinct first-difference levels".
  `card_le_pow_of_branchRank_le` lines 57-59, `exists_large_levels` lines
  287-289, `exists_firstDiff_companions` lines 328-331, whose conclusion
  `h < T.card ∧ a ∉ T ∧ Set.InjOn (firstDiff n a) T` is "h+1 companions";
  `encodeNat` line 128, `codeSet` line 168. Matches.
- A3. `BitValuation.lean`: `firstDiff_encodeNat_eq_padicValInt` lines 48-51
  identifies the first differing bit with `padicValInt 2 ((x : ℤ) - y)`.
  Matches.
- A4. `ResidueTree.lean`: `exists_nat_valuation_companions` lines 24-27 and
  `exists_int_valuation_companions` lines 72-75 give `a ∈ S`, `T ⊆ S`,
  `h < T.card`, `a ∉ T` and injectivity of `padicValInt 2 (b - a)` on `T`.
  Matches.
- A5. `Valuation.lean`: `sum_ne_zero_of_distinct_valuation` lines 39-44,
  `signed_sum_ne_zero_of_distinct_valuation` lines 73-79,
  `zero_pivot_dissociated` lines 93-96, `pivot_coefficient_valuation_bound`
  lines 23-27 (with `c.natAbs ≤ d + 1`) and `pivot_dissociated` lines
  371-378, whose `havoid` excludes the values from `padicValInt 2 a` to
  `padicValInt 2 a + Nat.log 2 (B.card + 1)`, that is
  $\lfloor\log_2(d+1)\rfloor+1$ values starting at the pivot's valuation
  with $d$ the number of companions. Matches.
- A6. `CardBound.lean`: `integer_card_le_pow` lines 142-145 and
  `integer_card_bound` lines 148-151. Matches.
- A7. `IntegerModel.lean`: `exists_rational_subset_sum_model` lines 27-30
  (a `ℝ →ₗ[ℚ] ℚ` with the subset-sum equivalence, using
  `Module.exists_dual_forall_apply_ne_zero` at line 37),
  `exists_integer_subset_sum_model` lines 57-60 (an injective `A → ℤ` with
  the same equivalence, using `IsLocalization.exist_integer_multiples` at
  line 63), `addDissociated_image_of_subset_sum_reflection` lines 95-102
  and `real_card_bound_of_integer_card_bound` lines 131-137. Matches.
- A8. `LogBound.lean`: `log_bound_of_card_le` lines 15-17 converts
  `n ≤ (d + 1) * 2 ^ d` with `0 < n` into the statement's bound. The
  page's two cases are written "d ≥ log_2 n and d < log_2 n"; the proof
  splits at line 31 on `(d : ℝ) ≤ Real.logb 2 ↑n` and its negation, so the
  boundary case $d=\log_2 n$ sits in the other branch from the page's
  wording, and both branches close it. Matches, up to that wording (see
  Discrepancies).

## Discrepancies

None. No prose clause lacks a Lean counterpart, no counterpart is weaker or
stronger than its clause, and the Lean statement asserts nothing the prose
does not say.

One observation on the proof account, outside the statement and not a
discrepancy: the proof page describes the case split of
`log_bound_of_card_le` as "d ≥ log_2 n and d < log_2 n", while the Lean
splits on `d ≤ log_2 n` and `d > log_2 n` (A8). Both treatments cover the
boundary case, so the account is accurate up to which branch takes it.

## Verdict

**PASS.** At the checked source of 2026-09-28, under
toolchain `leanprover/lean4:v4.32.0-rc1` and Mathlib `79aee35d…`,
`Erdos.L22.statement` states exactly the prose statement of the L22 card:
for every nonempty finite set $A$ of real numbers there is a subset
$B\subseteq A$ whose distinct finite subsets have distinct sums (the empty
subset with sum 0 included) and whose size is at least
$\log_2|A|-\log_2(\log_2|A|+1)$, with the real logarithm to base two; the
consequence sentence about $f(n)$ and the Scope sentence are respected; and
`Erdos.L22.claim` has the type `statement` itself, supplied by
`Erdos.Problem963.exists_real_dissociated_large`, whose closed type is
`statement` after unfolding, with the manifest recording the axioms
`propext`, `Classical.choice` and `Quot.sound` and no compiler axiom.

Limitations: this is a statement-fidelity audit. It did not build the Lean
sources, run the gate or the axiom audit, review the mathematics of the
`Erdos.Problem963` proofs beyond their declaration headers, or read the
research pages the card cites; the manifest's axiom footprint is reported as
the manifest records it, not re-derived. This audit assigns no tier itself.

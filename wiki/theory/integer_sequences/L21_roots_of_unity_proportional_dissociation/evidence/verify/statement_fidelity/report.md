---
name: theory/integer_sequences/L21_roots_of_unity_proportional_dissociation/evidence/verify/statement_fidelity/report
title: Fidelity audit report for L21 on 2026-09-28
desc: |
  Independent clause-by-clause comparison of the L21 card's prose statement
  with `Erdos.L21.statement` after unfolding every definition it reaches, as
  they stood on 2026-09-28: verdict PASS, no discrepancy, no tier assigned.
created: 2026-09-28T17:52:11Z
updated: 2026-09-28T20:42:55Z
---

***

## Subject and independence

**Verdict: PASS.** At the checked source of 2026-09-28 (below) the
Lean proposition `Erdos.L21.statement` is the prose statement of L21 clause
for clause, it asserts nothing the prose does not say, and `Erdos.L21.claim`
proves exactly that proposition. Audited 2026-09-28 (UTC). This audit
assigns no tier itself.

**Role.** The independent fidelity auditor for L21, in a fresh context, who
took no part in writing the claim, its Lean development or its card. The
audit is a reading: no Lean was built, no probe compiled, no `lake`,
generator or gate run. Every git command was read-only (`rev-parse`,
`ls-tree`, `show`, `status`, `diff --quiet`, `log --oneline`). No network
command was run.

**Frozen subject, by path and date.** The repository as it stood on the
default branch at 2026-09-28T13:50:48Z (the tip of `main`; the checked
source, called "the commit" below); its repository, `lean/`, `lean/Erdos`
and `lean/Erdos/RootsOfUnitySidon` tree identities, all by `git rev-parse`
at the commit, are restated here by that date. Toolchain
`lean/lean-toolchain`: `leanprover/lean4:v4.32.0-rc1`.
Mathlib `79aee35d9696d759b73eed71d7dde666750bc35e` per `lean/lakefile.toml`
line 11 and `lean/lake-manifest.json` line 11. Declarations, from
`lean/Manifest.json` (3,092 lines; module list line 15, declaration list
lines 2,997-2,998, claim row lines 3,067-3,079): `Erdos.L21.statement` (role
statement) and `Erdos.L21.claim` (role claim), module `Erdos.L21`, `depends`
empty, `compiler` empty, `axioms` `propext`, `Classical.choice`,
`Quot.sound`. The checkout was a linked worktree at the commit:
`git status --porcelain --untracked-files=no` printed nothing and
`git diff --quiet` against the commit on
`lean wiki/theory/integer_sequences wiki` exited 0 before the record folder
was created, so every worktree file named below equals its blob at the
commit. The card and the proof page were read through `git show` at the
commit.

**Prose subject.** The card
`wiki/theory/integer_sequences/L21_roots_of_unity_proportional_dissociation/_index.md`
at the commit: the `statement` field (lines 12-19) and the Statement section
(lines 39-53), whose second paragraph (lines 48-53) is the Scope text. The
two texts state the same clauses; the comparison below quotes the
`statement` field and notes where the section's wording differs. The card's
`tier` field and its Current standing, Verification and Remaining
obligations sections (lines 72-97) are outside the subject and did not shape
the verdict. The assignment located the card under
`wiki/theory/number_theory/`; no such folder exists at the commit
(`git ls-tree -r --name-only` at the commit), the card lives under
`wiki/theory/integer_sequences/`, and this record is filed beside it.

**Lean subject.** `lean/Erdos/L21.lean` (36 lines): imports lines 1-3,
`rootsOfUnity` line 20, `statement` lines 24-27, `rootsOfUnity_eq` lines
30-31, `claim` lines 33-34. The statement's meaning reaches
`Erdos.L21.rootsOfUnity`, Mathlib's `IsOfFinOrder`, `AddDissociated`,
`Set.InjOn`, `Finset`, its set coercion, subset and `card`, and core's `Nat`
order; the claim's term reaches
`Erdos.Research.Problem774.rootsOfUnity_proportionalDissociation` and the
project definitions `Erdos.Research.Problem774.rootsOfUnity`,
`UniformExtraction` and `statement`. All are unfolded in the section
"Definitions unfolded" below.

**Reading depth per module and page.** Depth "full" means every line read;
"definitions" means the named declarations read in full with their
docstrings and the rest of the file passed over; "names" means only a
listing of declaration names. Bare file names in the table are under
`lean/Erdos/RootsOfUnitySidon/`; the card pages are under the claim folder
named above.

| Path (at the commit) | Lines | Depth |
| --- | --- | --- |
| `lean/Erdos/L21.lean` | 1-36 | full |
| `RootsOfUnitySidonComplete.lean` | 1-22 | full |
| `RootsOfUnitySidonPisier.lean` | 1-48 | full |
| `RootsOfUnitySidonAnalytic.lean` | 1-39 | full |
| `PisierForwardComplete.lean` | 1-28 | full |
| `RootsOfUnitySidon.lean` | 1-70 | definitions |
| the same file | 996-1068 | names |
| `SidonExtraction.lean` | 1-5, 26, 85-95, 200-240 | definitions |
| `lean/Manifest.json` | 1-20, 2990-3000, 3060-3085 | full in range |
| `lean/lean-toolchain` | 1 | full |
| `lean/lakefile.toml` | 9-11 | full in range |
| `lean/lake-manifest.json` | 9-12 | full in range |
| card `_index.md` (`git show`) | 1-97 | full |
| card `_proof.md` (`git show`) | 1-36 | full |
| `docs/lean_authoring.md` | 286-349, 478-546 | full in range |
| `docs/anatomy.md` | 298-344 | full in range |
| `docs/verification.md` | 163-211, 573-603 | full in range |

Mathlib sources at revision `79aee35d…`, read from the pinned package
checkout (see exposure E6): `Mathlib/GroupTheory/OrderOfElement.lean` lines
40-80; `Mathlib/Combinatorics/Additive/Dissociation.lean` lines 20-50 and a
name listing of the rest; `Mathlib/Data/Set/Operations.lean` lines 299-300;
`Mathlib/Dynamics/PeriodicPts/Defs.lean` lines 60-66 and 197-202;
`Mathlib/Data/Finset/Defs.lean` lines 126-127 and 224-232;
`Mathlib/Data/Finset/Card.lean` lines 47-48; `Mathlib/Data/Complex/Basic.lean`
lines 118, 143, 165, 207 (instance heads), 325-327 and 377-380. Core at the
pinned toolchain: `src/lean/Init/Prelude.lean` lines 1891-1903.

**Excluded and not read.** Nothing among the private working files; no other claim's
audit beyond the shapes named in E3 and E5; no research page, library card
or PDF; the audit program and refusal suite; the module bodies of the
`RootsOfUnitySidon/` development beyond the ranges above (the claim's
correctness is the kernel's business, outside a fidelity audit); no commit
diff.

**Exposures.**

- E1. The assignment's card path did not exist at the commit. Locating the
  card printed the L21 rows of the generated views `wiki/lemmas.md` and
  `wiki/standing.md` (line 39 of each), which carry the standing words
  "proved" and "0" and the folder name. Standing text, outside the subject;
  the rows repeat the card's `statement` field and add nothing to the
  comparison.
- E2. The card was printed in full, exposing its `tier` field and its
  Current standing, Verification and Remaining obligations sections (lines
  72-97: author-recorded standing, gate commands, the open audit item).
  None of that text is a verdict on the statement's fidelity; nothing in
  the comparison or the verdict comes from it.
- E3. The precedent record under
  `wiki/theory/ramsey_theory/L17_rainbow_odd_cycle_threshold/evidence/verify/statement_fidelity/`
  was read for its shape, as assigned: the folder listing, the three index
  pages of its evidence tree in full, `review.txt` lines 1-420 and
  `review_reads.json` lines 1-45. L17 content only; no L21 content.
- E4. The environment displayed the branch name and the subject lines of
  five recent commits (library re-render, proof reconstructions), and
  `git log --oneline -5 -- lean/Erdos/L21.lean` displayed one commit subject
  naming Problems 940 and 774. History metadata only. Listing
  `wiki/theory/` showed other claims' folder names, and the `Manifest.json`
  range read for the L21 row also showed the tail of the L20 row and the
  head of the L22 row, including L22's pretty-printed statement. Not read
  further; no bearing on L21.
- E5. The first 30 lines of
  `wiki/theory/extremal_graph_theory/L15_universal_bipartite_extremal_asymptotic/evidence/verify/k2_disproof_review_fresh.md`
  were read for the frontmatter shape of a filed `.md` record. That file is
  another claim's audit, which the assignment excludes; the reading was of
  its frontmatter and opening paragraphs only, carries no L21 content and
  did not enter this audit's reasoning. Disclosed for the grader.
- E6. The worktree has no `lean/.lake/`, so Mathlib was read from the
  package checkout `lean/.lake/packages/mathlib` of the repository's main
  checkout on the same host, whose `git rev-parse HEAD` printed
  `79aee35d9696d759b73eed71d7dde666750bc35e`, the revision
  `lean/lakefile.toml` pins, with an empty `git status`. Core was read from
  the elan toolchain directory for `v4.32.0-rc1`. Both are reads of pinned
  upstream sources outside the assigned worktree.
- E7. `git status --short` runs after the record folder was created listed
  untracked paths this audit did not create: a review page under
  `wiki/research/erdos_15/evidence/verify/` and an evidence folder under
  `wiki/theory/diophantine_problems/L19_four_powerful_complement_density/`,
  evidently other roles' concurrent output in the same worktree. Neither
  was opened, and the worktree's tracked tree stayed clean throughout.

## Restatement

There is one positive integer $k$ such that, for every finite set $A$ of
complex numbers each of which satisfies $z^n = 1$ for some positive integer
$n$, some subset $B \subseteq A$ is additively dissociated (any two distinct
subsets of $B$ have distinct sums in $\mathbb C$) and has at least $|A|/k$
elements, that is $|A| \le k\,|B|$. Nothing is asserted about the size of
$k$, about subsets of $\mathbb N$, or about the question of Problem 774.

## Clause-by-clause comparison

The prose is the card's `statement` field (lines 13-19), split into its
clauses P1-P8; the Statement section (lines 41-53) states the same clauses
in symbols, and the one wording difference is noted at P1. The Lean column
gives `Erdos.L21.statement` (lines 25-27) after the unfolding steps U1-U10
of the next section, which the bullets below the table cite. "Faithful"
means the Lean clause has exactly the prose clause's strength.

| # | Prose clause | Lean counterpart | Finding |
| --- | --- | --- | --- |
| P1 | $R$: $z^n = 1$, integer $n \ge 1$ | `IsOfFinOrder z` | faithful |
| P2 | inside $(\mathbb C, +)$ | `AddDissociated` on `ℂ` | faithful |
| P3 | distinct subsets, distinct sums | `InjOn` of finset sums | faithful |
| P4 | integer $k \ge 1$ | `∃ k : ℕ, 0 < k` | faithful |
| P5 | $A\subseteq R$ finite | `A : Finset ℂ`, `↑A ⊆ rootsOfUnity` | faithful |
| P6 | $B\subseteq A$ dissociated | `B ⊆ A ∧ AddDissociated ↑B` | faithful |
| P7 | $\lvert A\rvert\le k\lvert B\rvert$ | `A.card ≤ k * B.card` | faithful |
| P8 | Scope exclusions | nothing further asserted | faithful |
| — | every Lean conjunct | one of P4-P7 | nothing extra |

- P1. "Let R be the set of complex roots of unity, the complex z with
  z^n = 1 for some integer n >= 1." Lean: `rootsOfUnity := {z | IsOfFinOrder z}`
  (U1); `IsOfFinOrder z` unfolds to `∃ n > 0, IsPeriodicPt (z * ·) n 1`
  (U2, U3), and Mathlib's `isOfFinOrder_iff_pow_eq_one` reads it as
  `∃ n : ℕ, 0 < n ∧ z ^ n = 1`, the power and the `1` being those of the
  multiplicative monoid of `ℂ` (U4). The exponents are the natural numbers
  $n \ge 1$, the same set as the prose's integers $n \ge 1$; the exponent
  $0$ is excluded on both sides. The Statement section writes the same
  clause as "$z^n = 1$ for some integer $n \ge 1$" and adds "regarded inside
  $(\mathbb C, +)$", which is P2. Faithful.
- P2. "viewed inside the additive group of the complex numbers." The only
  group operation in the conclusion is the sum in `AddDissociated`, taken
  at the instance `AddCommGroup ℂ` (U6): complex addition. Multiplication
  enters only to define $R$ (P1), as in the prose. Faithful.
- P3. "A set B of complex numbers is additively dissociated if distinct
  finite subsets of B have distinct sums." Lean: `AddDissociated (↑B : Set ℂ)`
  is `{t : Finset ℂ | ↑t ⊆ ↑B}.InjOn (∑ x ∈ ·, x)` (U6), that is, for all
  finsets `t₁`, `t₂` contained in `B`, `∑ t₁ = ∑ t₂ → t₁ = t₂` (U7): the
  contrapositive of the prose. Both sides quantify over all finite subsets
  including the empty one (sum $0$); as `B` is finite, "finite subsets of
  B" are all its subsets, and `↑t ⊆ ↑B ↔ t ⊆ B` (U5). Faithful.
- P4. "There is an integer k >= 1." Lean: `∃ k : ℕ, 0 < k ∧ …`. In core,
  `0 < k` is by definition `Nat.le 1 k` (U8), and the natural numbers with
  $k \ge 1$ are the integers with $k \ge 1$. Faithful.
- P5. "every finite set A contained in R." Lean: `∀ A : Finset ℂ`, a finite
  set of complex numbers without repetition, with `(↑A : Set ℂ) ⊆ rootsOfUnity`,
  that is `∀ a, a ∈ A → IsOfFinOrder a` (U5, U1). The empty set is admitted
  on both sides. Faithful.
- P6. "contains an additively dissociated subset B." Lean:
  `∃ B : Finset ℂ, B ⊆ A ∧ AddDissociated (↑B : Set ℂ)`; `B ⊆ A` is
  `∀ x, x ∈ B → x ∈ A` (U5). Faithful.
- P7. "with |A| <= k*|B|." Lean: `A.card ≤ k * B.card`, with `Finset.card`
  the number of elements (U5) and `*`, `≤` on `ℕ` (U8): no cast, no
  truncated subtraction, no division. Faithful.
- P8. "Nothing is asserted about the value of k, about subsets of the
  natural numbers, or about Problem 774's question." The Lean binds `k`
  existentially with the single constraint `0 < k`, mentions no subset of
  `ℕ` and no union of dissociated sets; it asserts exactly the conjunction
  P4-P7 and nothing more (U9). The Statement section's second paragraph
  says the same in more words. Faithful.
- Converse direction. `Erdos.L21.statement` with `rootsOfUnity` unfolded
  (U9) is

  ```lean
  ∃ k : ℕ, 0 < k ∧
    ∀ A : Finset ℂ, (↑A : Set ℂ) ⊆ {z | IsOfFinOrder z} →
      ∃ B : Finset ℂ, B ⊆ A ∧ AddDissociated (↑B : Set ℂ) ∧
        A.card ≤ k * B.card
  ```

  Its five atoms are P4 (`0 < k`), P5 (the hypothesis on `A`), P6 (`B ⊆ A`
  and `AddDissociated ↑B`) and P7 (the cardinality bound). No hypothesis,
  parameter, instance argument or side condition beyond these is present:
  `statement : Prop` has no binders, and `claim : statement` has none (U10).

## Definitions unfolded

Each item names the Lean source read, at the commit for project files and
at Mathlib `79aee35d…` or toolchain `v4.32.0-rc1` for upstream files.

- U1. `Erdos.L21.rootsOfUnity : Set ℂ := {z | IsOfFinOrder z}`
  (`lean/Erdos/L21.lean` line 20). `Erdos.L21.rootsOfUnity_eq` (lines
  30-31) states it equal to `Erdos.Research.Problem774.rootsOfUnity` by
  `rfl`; that definition (`RootsOfUnitySidon.lean` line 33) has the same
  body verbatim.
- U2. `IsOfFinOrder (x : G) : Prop := (1 : G) ∈ periodicPts (x * ·)` under
  `[Monoid G]` (`Mathlib/GroupTheory/OrderOfElement.lean` lines 51-64), with
  `isOfFinOrder_iff_pow_eq_one : IsOfFinOrder x ↔ ∃ n, 0 < n ∧ x ^ n = 1`
  (lines 72-74, `n : ℕ`) proved there by `simp` from `mem_periodicPts` and
  `isPeriodicPt_mul_iff_pow_eq_one` (lines 55-57).
- U3. `periodicPts (f : α → α) : Set α := {x | ∃ n > 0, IsPeriodicPt f n x}`
  and `IsPeriodicPt f n x := IsFixedPt f^[n] x`
  (`Mathlib/Dynamics/PeriodicPts/Defs.lean` lines 199-200 and 62-63); so
  `IsOfFinOrder z` is literally "some `n > 0` with the `n`-fold left
  multiplication by `z` fixing `1`", the `n > 0` written into the set.
- U4. The instance `Monoid ℂ` that `IsOfFinOrder` uses on `ℂ` is the
  multiplicative structure of `Complex.commRing`
  (`Mathlib/Data/Complex/Basic.lean` lines 377-380, `npow := npowRec` on
  `(1 : ℂ)` and `(· * ·)`), with `One ℂ` and `Mul ℂ` at lines 143 and 207.
  Every `Monoid ℂ` instance Mathlib provides is a projection of that ring
  structure or of the field and normed structures built on it; the
  additive structure is the class `AddCommGroup` (`Complex.addCommGroup`,
  line 325), which is not a `Monoid`, and an additive reading would need
  the type `Multiplicative ℂ`, which does not appear. Hence `z ^ n = 1` is
  the ordinary complex power equal to the complex unit.
- U5. `Finset ℂ` is a finite set of complex numbers without repetition; its
  coercion to `Set ℂ` satisfies `a ∈ (s : Set α) ↔ a ∈ s` by `Iff.rfl`
  (`Mathlib/Data/Finset/Defs.lean` lines 126-127, `mem_coe`); `s₁ ⊆ s₂ ↔
  ∀ ⦃x⦄, x ∈ s₁ → x ∈ s₂` by `Iff.rfl` (lines 224-225, `subset_iff`);
  `(s₁ : Set α) ⊆ s₂ ↔ s₁ ⊆ s₂` by `Iff.rfl` (lines 231-232,
  `coe_subset`); `Finset.card s := Multiset.card s.1`
  (`Mathlib/Data/Finset/Card.lean` lines 47-48), the number of elements.
- U6. `AddDissociated`, the additive form that `to_additive` generates from
  `MulDissociated` (`Mathlib/Combinatorics/Additive/Dissociation.lean` lines
  31-45, under `[CommGroup α]`, so `[AddCommGroup α]` additively; docstring
  "A set is dissociated iff all its finite subsets have different sums"):

  ```lean
  def AddDissociated (s : Set α) : Prop :=
    {t : Finset α | ↑t ⊆ s}.InjOn (∑ x ∈ ·, x)
  ```

  At `α = ℂ` the instance is `Complex.addCommGroup` (U4).

- U7. `Set.InjOn` (`Mathlib/Data/Set/Operations.lean` lines 299-300):

  ```lean
  def InjOn (f : α → β) (s : Set α) : Prop :=
    ∀ ⦃x₁ : α⦄, x₁ ∈ s → ∀ ⦃x₂ : α⦄, x₂ ∈ s → f x₁ = f x₂ → x₁ = x₂
  ```

- U8. `Nat.lt (n m : Nat) : Prop := Nat.le (succ n) m` and the instances
  `instLENat`, `instLTNat` (`Init/Prelude.lean` lines 1891-1903), so
  `0 < k` is `1 ≤ k`; `k * B.card` and `≤` are the natural-number
  operations, with no coercion in the statement.
- U9. `Erdos.L21.statement` (`lean/Erdos/L21.lean` lines 24-27, verbatim),
  under `set_option autoImplicit false` (line 15) in `namespace Erdos.L21`
  (line 17); the file has no `variable`, `open`, notation, macro, instance,
  axiom or attribute command:

  ```lean
  def statement : Prop :=
    ∃ k : ℕ, 0 < k ∧
      ∀ A : Finset ℂ, (↑A : Set ℂ) ⊆ rootsOfUnity →
        ∃ B : Finset ℂ, B ⊆ A ∧ AddDissociated (↑B : Set ℂ) ∧ A.card ≤ k * B.card
  ```

  The manifest's pretty statement (`lean/Manifest.json` line 3,071) prints
  the same proposition with `rootsOfUnity` unexpanded and `∃ B ⊆ A` for
  the bounded existential; its `sha256Unfolded` differs from its legacy
  `sha256`, as expected when the statement names a constant of the claim's
  own namespace.

- U10. `Erdos.L21.claim` (`lean/Erdos/L21.lean` lines 33-34, verbatim):

  ```lean
  theorem claim : statement :=
    Erdos.Research.Problem774.rootsOfUnity_proportionalDissociation
  ```

  The declared type is `statement` with no binders. The term's type is
  `Erdos.Research.Problem774.statement`, defined with `UniformExtraction`
  in `RootsOfUnitySidon.lean` lines 44-49, verbatim:

  ```lean
  def UniformExtraction (s : Set ℂ) (k : ℕ) : Prop :=
    ∀ A : Finset ℂ, (↑A : Set ℂ) ⊆ s →
      ∃ B : Finset ℂ, B ⊆ A ∧ AddDissociated (↑B : Set ℂ) ∧ A.card ≤ k * B.card

  def statement : Prop := ∃ k : ℕ, 0 < k ∧ UniformExtraction rootsOfUnity k
  ```

  Delta-unfolding `Problem774.statement`, `Problem774.UniformExtraction`,
  `Problem774.rootsOfUnity` and `L21.rootsOfUnity` gives the same term as
  U9 symbol for symbol, which is the definitional equality the elaborator
  and kernel check. The library theorem
  (`RootsOfUnitySidonComplete.lean` lines 17-20) takes no arguments and is
  `statement_of_analyticSidon_of_pisier` (`RootsOfUnitySidonPisier.lean`
  lines 32-37) applied to two argument-free theorems, `pisierForward`
  (`PisierForwardComplete.lean` lines 20-26) and
  `rootsOfUnity_analyticSidon` (`RootsOfUnitySidonAnalytic.lean` lines
  23-37); `statement_iff_pisier_interface` (`RootsOfUnitySidonPisier.lean`
  lines 25-28) is `rfl` against `SidonExtraction.UniformExtraction`
  (`SidonExtraction.lean` lines 220-222 with `FiniteExtraction` lines
  88-90), whose body is again the same proposition. No hypothesis is left
  open anywhere on the path from `claim` to its two inputs; the manifest
  row records no compiler axiom and the three standard axioms. Whether the
  tree compiles is the gate's business and was not re-established here.

## Vacuous conventions, binder domains and junk values

- Empty `A`: `↑∅ ⊆ rootsOfUnity` holds, `B = ∅` is dissociated
  (`addDissociated_empty`, Dissociation.lean line 55) and `0 ≤ k * 0`; the
  prose is equally trivial there. Nonempty `A` forces `B.card ≥ 1` on both
  sides, since `A.card ≤ k * 0` fails.
- Exponent `0`: excluded by `n > 0` in U3 and by "$n \ge 1$" in the prose;
  without it every complex number would be a root of unity on either side.
- `0 ∉ R` and `{0}` not dissociated: consequences that agree on both sides;
  the statement needs neither (the proof uses `zero_not_mem_rootsOfUnity`).
- Binder domains: `k : ℕ`, `A B : Finset ℂ`; the prose's integer $k \ge 1$
  and finite sets of complex numbers are the same objects.
- No junk value: the statement has no division, subtraction, logarithm,
  supremum, real cast or `sSup`; the only coercions are the two
  `Finset ℂ → Set ℂ` coercions of U5.

## Discrepancies

None.

## Verdict

**PASS.** The Lean statement `Erdos.L21.statement` at the checked source of
2026-09-28 is the prose statement of L21:
every prose clause, including the conventions on $R$ and on dissociation and
the Scope paragraph's exclusions, has its Lean counterpart at exactly its
strength, the Lean statement asserts nothing the prose does not say, and
`Erdos.L21.claim` proves exactly `statement` with no additional hypothesis.
The audit covers the whole statement and nothing beyond it: it asserts
nothing about the value of $k$, about Problem 774's question, about the
correctness of the library proof (the kernel's business), about novelty or
about community acceptance, and it did not rerun the build, the axiom audit
or the gate.

This audit assigns no tier itself. A distinct grade of this report, the
non-author clean gate at the commit and the tier assertion are separate
records under the verification contract and are not part of this record.

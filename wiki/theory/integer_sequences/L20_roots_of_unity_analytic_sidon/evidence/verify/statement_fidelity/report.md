---
name: theory/integer_sequences/L20_roots_of_unity_analytic_sidon/evidence/verify/statement_fidelity/report
title: Statement-fidelity report for L20 on 2026-09-28
desc: |
  Independent clause-by-clause comparison of the L20 card's prose statement
  with `Erdos.L20.statement` as they stood on 2026-09-28, with every
  definition the statement uses unfolded to its Lean source; verdict PASS, no
  tier assigned.
created: 2026-09-28T18:01:09Z
updated: 2026-09-28T18:01:09Z
---

***

## Subject and independence

Role. The auditor is an independent statement-fidelity auditor working in a
fresh context. The auditor took no part in writing the claim, its Lean
development or its card, built nothing, ran no generator and no gate, and
read only the sources listed below, at the commit dated here. The audit
compares the card's prose statement with the Lean statement; it does not
review the proof route and it assigns no tier.

Commit. The repository as it stood on the default branch at
2026-09-28T13:50:48Z, equal to `main` at the time of the audit (the checked
source, called "the commit" below); its repository, `lean/`, `lean/Erdos`
and `lean/Erdos/RootsOfUnitySidon` tree identities and the tree of the claim
folder `wiki/theory/integer_sequences/L20_roots_of_unity_analytic_sidon`
were taken by `git rev-parse` at the commit and are restated here by that
date. Toolchain `leanprover/lean4:v4.32.0-rc1` (`lean/lean-toolchain`,
one line). Mathlib `79aee35d9696d759b73eed71d7dde666750bc35e`
(`lean/lake-manifest.json`, packages block).

Manifest. `lean/Manifest.json` at the commit lists 2,977 modules and seven
claims. Its L20 row names module `Erdos.L20`, the declarations
`Erdos.L20.statement` (role statement) and `Erdos.L20.claim` (role claim),
`depends: []`, `compiler: []`, and the axioms `propext`, `Classical.choice`
and `Quot.sound`; it renders the statement under `pp.fullNames` as

```text
∃ (K : ℝ),
  0 < K ∧
    ∀ (A : Finset ℂ),
      ↑A ⊆ Erdos.L20.rootsOfUnity →
        ∀ (c : ℂ → ℂ), ∃ (χ : AddChar ℂ Circle), ∑ z ∈ A, ‖c z‖ ≤ K * ‖∑ z ∈ A, c z * ↑(χ z)‖
```

which agrees with the source text of `lean/Erdos/L20.lean` and resolves the
bare name `rootsOfUnity` to the claim's own definition. The axiom row is
cited for identification only; standing and tier are outside the subject.

The English subject. The `statement:` field of the card
`wiki/theory/integer_sequences/L20_roots_of_unity_analytic_sidon/_index.md`
at the commit (lines 13–22), read together with its Statement section
(lines 41–60), whose last paragraph carries the Scope exclusions; the two
texts agree with each other. The proof page `_proof.md` (body, lines 17–31)
was read for the names of the modules it maps to. The card's Argument and
formal surface, Current standing, Verification and Remaining obligations
sections (lines 62–97) and its `tier` field (line 24) are outside the
subject and did not shape the verdict.

Reading depth, by path at the commit.

| Path | Lines read | Depth |
|---|---|---|
| `wiki/theory/integer_sequences/L20_roots_of_unity_analytic_sidon/_index.md` | 1–97 | full; subject lines 13–22 and 41–60 |
| `wiki/theory/integer_sequences/L20_roots_of_unity_analytic_sidon/_proof.md` | 1–31 | full |
| `lean/Erdos/L20.lean` | 1–38 | full |
| `lean/Erdos/RootsOfUnitySidon/RootsOfUnitySidonComplete.lean` | 1–22 | full; imports and one theorem the statement does not use |
| `lean/Erdos/RootsOfUnitySidon/RootsOfUnitySidonAnalytic.lean` | 1–39 | full; the type of `rootsOfUnity_analyticSidon` |
| `lean/Erdos/RootsOfUnitySidon/RootsOfUnitySidon.lean` | 1–80, 955–1010, and the declaration lines of all 1,068 | definitions unfolded; the finite-order lemmas read for the reading of `IsOfFinOrder` |
| `lean/Manifest.json` | the L20 claim row, `ppWidth`, `ppOptions`, `compiler`, `declarations`, module list | partial |
| `lean/lean-toolchain` | 1 | full |
| `lean/lake-manifest.json` | packages block | partial |
| `Mathlib/GroupTheory/OrderOfElement.lean` | 41–80 | `IsOfFinOrder` and its power characterization |
| `Mathlib/Dynamics/PeriodicPts/Defs.lean` | 62–63, 199–206 | `IsPeriodicPt`, `periodicPts` |
| `Mathlib/Algebra/Group/AddChar.lean` | 55–120, 153–157, 372–388 | `AddChar`, its coercion, `map_neg_eq_inv` |
| `Mathlib/Analysis/Complex/Circle.lean` | 48–73 | `Circle`, its coercion, group and norm |
| `Mathlib/Analysis/Normed/Field/UnitBall.lean` | 183–191 | `Submonoid.unitSphere` |
| `Mathlib/Analysis/Normed/Group/Basic.lean` | 296–304 | sphere membership |
| `Mathlib/Analysis/Complex/Norm.lean` | 18–40 | the norm of `ℂ` |
| `Mathlib/Analysis/Complex/Basic.lean` | 40–80 | the normed-field instance of `ℂ` |
| `Mathlib/Analysis/SpecialFunctions/Complex/CircleAddChar.lean` | 1–45 | the imported module's header |

Guidance read: `docs/lean_authoring.md` "Statement fidelity and data
discipline", "Native claim surface" and "Statement fidelity and
validation"; `docs/anatomy.md` "Tiers" and its evidence-home rules;
`docs/verification.md` "Exact subjects and durable evidence", "Whole-claim
report" and "Durable reports and current standing"; and the shape of the
L17 record
`wiki/theory/ramsey_theory/L17_rainbow_odd_cycle_threshold/evidence/verify/statement_fidelity/`.

Excluded. Everything among the private working files; other claims' audits, except the
precedent pages read for their shape; all standing and acceptance text; the
68 other modules under `lean/Erdos/RootsOfUnitySidon/`, which carry the
proof route and no definition the statement uses; every other Mathlib file.

Exposures.

1. `git show` printed the card and the proof page in full, so the card's
   standing sections, its `tier` field and the proof page's opening
   sentence, which names a tier, were seen. None was used.
2. The L17 precedent's three folder pages and the file listing of the L14
   record `statement_fidelity_3/` were read for shape, and the first
   22–40 lines of the two Markdown records under
   `wiki/theory/extremal_graph_theory/L15_universal_bipartite_extremal_asymptotic/evidence/verify/`
   for the shape of a filed record. Each concerns another claim's
   acceptance; none concerns L20.
3. The Mathlib sources were read from a checkout outside the audit's
   worktree, the main checkout's `lean/.lake/packages/mathlib`, whose
   `HEAD` was checked to equal the pinned revision `79aee35d…`; reads only.
4. The environment showed the worktree's branch name, its git status and
   the subject lines of the five most recent commits; the manifest's
   administrative fields (`ppWidth`, `ppOptions`, the digest fields) were
   seen.
5. The commissioning text placed the claim folder under
   `wiki/theory/number_theory/`; at the commit the folder is
   `wiki/theory/integer_sequences/L20_roots_of_unity_analytic_sidon/` and
   no L20 folder exists under `number_theory/`. This record is filed under
   the actual folder.
6. Lines 955–1010 of `RootsOfUnitySidon.lean` are proof-side text; they
   were read only to confirm how the development reads `IsOfFinOrder`. The
   verdict rests on the Mathlib definition.

## Clause-by-clause comparison

Restated in the auditor's words: for the set $R$ of complex numbers of
finite multiplicative order, one real constant $K>0$ serves every finite
$A\subseteq R$ and every coefficient function $c:\mathbb C\to\mathbb C$, in
that some additive character $\chi$ of the discrete group $(\mathbb C,+)$
into the unit circle satisfies
$\sum_{z\in A}|c(z)|\le K\,|\sum_{z\in A}c(z)\chi(z)|$; nothing is said
about the size of $K$, about continuous characters, or about Problem 774.

| # | Prose clause (card) | Lean counterpart (`Erdos.L20.statement`) | Finding |
|---|---|---|---|
| 1 | $R$ is the set of complex roots of unity, the $z$ with $z^n=1$ for some integer $n\ge1$ | `rootsOfUnity`, the `z : ℂ` with `IsOfFinOrder z`, which unfolds to `∃ n : ℕ, 0 < n ∧ z ^ n = 1` | Match |
| 2 | $R$ viewed inside $(\mathbb C,+)$ with the discrete topology | `Set ℂ`; the characters are `AddChar ℂ Circle` on the additive monoid of `ℂ`, with no topology anywhere | Match |
| 3 | there is a real $K>0$ | `∃ K : ℝ, 0 < K ∧ …`, outermost | Match |
| 4 | for every finite $A\subseteq R$ | `∀ A : Finset ℂ, (↑A : Set ℂ) ⊆ rootsOfUnity → …` | Match |
| 5 | and every $c:\mathbb C\to\mathbb C$ | `∀ c : ℂ → ℂ, …` | Match |
| 6 | there is an additive character $\chi:(\mathbb C,+)\to S^1$, a group homomorphism into the multiplicative circle group, no continuity required | `∃ χ : AddChar ℂ Circle, …` | Match |
| 7 | $\sum_{z\in A}\lvert c(z)\rvert\le K\,\lvert\sum_{z\in A}c(z)\chi(z)\rvert$ | `(∑ z ∈ A, ‖c z‖) ≤ K * ‖∑ z ∈ A, c z * (χ z : ℂ)‖` | Match |
| 8 | nothing is asserted about the size of $K$ | no bound on `K` appears | Match |
| 9 | nothing is asserted about continuity of $\chi$ | no topology or continuity appears | Match |
| 10 | nothing is asserted about Problem 774's question | no constant of the Problem 774 conclusion appears; `depends: []` | Match |

Clause notes.

1. Membership. `IsOfFinOrder` is Mathlib's predicate on an element of a
   monoid (`variable [Monoid G]`), here the multiplicative monoid of `ℂ`;
   the additive predicate is the separate `IsOfFinAddOrder`. It unfolds to
   `(1 : ℂ) ∈ periodicPts (z * ·)`, that is
   `∃ n > 0, IsPeriodicPt (z * ·) n 1`, and
   `isPeriodicPt_mul_iff_pow_eq_one` turns the periodicity into
   `z ^ n = 1`, so `isOfFinOrder_iff_pow_eq_one` gives
   `∃ n : ℕ, 0 < n ∧ z ^ n = 1`, with `z ^ n` the monoid power of `ℂ` and a
   natural exponent. The naturals $n\ge1$ are the integers $n\ge1$. Both
   sets contain $1$ (take $n=1$) and exclude $0$ (since $0^n=0$ for
   $n\ge1$). The development's own `uniformExtraction_iff_finiteOrders` and
   `analyticSidon_iff_finiteOrders` use this reading through `nthRoots n`,
   the set of `z` with `z ^ n = 1`. Inside `namespace Erdos.L20` the bare
   name `rootsOfUnity` resolves to the local definition of line 22, not to
   Mathlib's `rootsOfUnity` (a subgroup of units, of another type); the
   manifest's full-name render confirms it.
2. Ambient group and topology. The Lean statement puts no topology on `ℂ`
   and no continuity condition on `χ`; it quantifies over every additive
   character, which is what the prose's discrete topology means. The
   phrase has no separate Lean token; its counterpart is the absence of any
   continuity hypothesis.
3. Constant. Outermost existential, `K : ℝ` with `0 < K`, uniform over `A`
   and `c`. The quantifier order is the prose's: there is $K$, for all $A$,
   for all $c$, there is $\chi$.
4. Finite sets. `Finset ℂ` is the type of finite sets of complex numbers,
   `(↑A : Set ℂ)` its coercion to a set, `⊆` set inclusion. The empty set
   is admitted in both.
5. Coefficients. `c : ℂ → ℂ` is defined on all of `ℂ`, as in the prose;
   only its values on `A` enter the sums in both.
6. Characters. `AddChar ℂ Circle` (`variable (A : Type*) [AddMonoid A]`,
   `variable (M : Type*) [Monoid M]`) is a structure with
   `toFun : ℂ → Circle`, `toFun 0 = 1` and
   `toFun (a + b) = toFun a * toFun b`, applied through its `FunLike`
   coercion. `Circle` is `Submonoid.unitSphere ℂ`, the complex numbers of
   norm one under multiplication, with its `CommGroup` instance. Since `ℂ`
   is an additive group and `Circle` a group, such a map is a group
   homomorphism from $(\mathbb C,+)$ to the multiplicative circle group
   (`AddChar.map_neg_eq_inv`). No field of the structure and no hypothesis
   of the statement imposes continuity.
7. Inequality. `‖c z‖` is the complex norm `√(normSq (c z))`, the modulus
   $|c(z)|$, so the left side is a finite sum of real numbers in `ℝ`.
   `(χ z : ℂ)` is the coercion `Circle → ℂ` (`Subtype.val`), the underlying
   complex number of modulus one; `c z * (χ z : ℂ)` is complex
   multiplication; the inner sum is in `ℂ`, and `‖·‖` of it is its modulus.
   `K * ‖…‖` and `≤` are in `ℝ`. This is the prose inequality, term for
   term.
8. Size of $K$. No bound, growth rate or numerical value of `K` appears in
   the statement.
9. Continuity. No topology, metric or continuity appears in the statement.
10. Problem 774. `Erdos.L20.statement` mentions no constant of the Problem
    774 development. `Erdos.Research.Problem774.statement`, the
    proportional-dissociation conclusion, is a different constant, and the
    manifest row has `depends: []`. The Lean statement asserts nothing the
    prose does not say.

Binder domains. `K : ℝ`; `A : Finset ℂ`; `c : ℂ → ℂ`;
`χ : AddChar ℂ Circle`; `z : ℂ` ranging over `A` in both sums; and `n : ℕ`
in the unfolded membership.

Vacuous conventions and coercions. For `A = ∅` both sums are `0` and
`0 ≤ K * 0` holds; the prose's "every finite set" includes the empty set,
so the two agree there. `0 ∉ R` and `1 ∈ R` in both. No division,
logarithm, supremum or other junk-valued operation occurs. The only
coercions are `Finset ℂ → Set ℂ` in the hypothesis and `Circle → ℂ` inside
the second sum; no cast between `ℕ`, `ℤ`, `ℝ` and `ℂ` occurs, and `K` is
used only in `ℝ`. The power `z ^ n` is `Monoid.npow` in `ℂ`.

Claim against statement. `theorem claim : statement :=` followed by
`Erdos.Research.Problem774.rootsOfUnity_analyticSidon` (lines 35–36 of
`lean/Erdos/L20.lean`). Its declared type is the constant
`Erdos.L20.statement`, as the native claim surface requires, and the
manifest lists it under role `claim`. The proof term has type
`Erdos.Research.Problem774.AnalyticSidon`, whose body
(`RootsOfUnitySidon.lean` lines 54–58) is character for character the body
of `Erdos.L20.statement` with `Erdos.Research.Problem774.rootsOfUnity` in
place of `Erdos.L20.rootsOfUnity`; both constants are the set of `z` with
`IsOfFinOrder z` (lines 33 and 22), and `rootsOfUnity_eq` (lines 32–33)
records the equality by `rfl`. After delta-unfolding these four constants
the two propositions are identical, so `claim` proves exactly `statement`,
not a weaker or conditional proposition. The audit read the declarations
and did not build; whether the module elaborates on the pinned toolchain is
a matter for the Lean gate. The statement uses no constant of the bare
`Erdos` namespace, so the digest blind spot for shared constants recorded in
`docs/lean_authoring.md` "Statement fidelity and data discipline" does not
touch it.

## Definitions unfolded

Project sources at the commit.

```lean
-- lean/Erdos/L20.lean, lines 22 and 25-29
def rootsOfUnity : Set ℂ := {z | IsOfFinOrder z}

def statement : Prop :=
  ∃ K : ℝ, 0 < K ∧
    ∀ A : Finset ℂ, (↑A : Set ℂ) ⊆ rootsOfUnity → ∀ c : ℂ → ℂ,
      ∃ χ : AddChar ℂ Circle,
        (∑ z ∈ A, ‖c z‖) ≤ K * ‖∑ z ∈ A, c z * (χ z : ℂ)‖
```

```lean
-- lean/Erdos/RootsOfUnitySidon/RootsOfUnitySidon.lean, lines 33 and 54-58
def rootsOfUnity : Set ℂ := {z | IsOfFinOrder z}

def AnalyticSidon : Prop :=
  ∃ K : ℝ, 0 < K ∧
    ∀ A : Finset ℂ, (↑A : Set ℂ) ⊆ rootsOfUnity → ∀ c : ℂ → ℂ,
      ∃ χ : AddChar ℂ Circle,
        (∑ z ∈ A, ‖c z‖) ≤ K * ‖∑ z ∈ A, c z * (χ z : ℂ)‖
```

```lean
-- lean/Erdos/RootsOfUnitySidon/RootsOfUnitySidonAnalytic.lean, line 23
theorem rootsOfUnity_analyticSidon : AnalyticSidon := by
```

Mathlib sources at `79aee35d9696d759b73eed71d7dde666750bc35e`.

```lean
-- Mathlib/GroupTheory/OrderOfElement.lean, lines 51, 56, 63-64 and 73
variable [Monoid G] {a b x y : G} {n m : ℕ}
theorem isPeriodicPt_mul_iff_pow_eq_one (x : G) : IsPeriodicPt (x * ·) n 1 ↔ x ^ n = 1 := by
def IsOfFinOrder (x : G) : Prop :=
  (1 : G) ∈ periodicPts (x * ·)
theorem isOfFinOrder_iff_pow_eq_one : IsOfFinOrder x ↔ ∃ n, 0 < n ∧ x ^ n = 1 := by
```

```lean
-- Mathlib/Dynamics/PeriodicPts/Defs.lean, lines 62-63 and 199-200
def IsPeriodicPt (f : α → α) (n : ℕ) (x : α) :=
  IsFixedPt f^[n] x
def periodicPts (f : α → α) : Set α :=
  { x : α | ∃ n > 0, IsPeriodicPt f n x }
```

```lean
-- Mathlib/Algebra/Group/AddChar.lean, lines 59, 62, 70-83 (docstrings
-- omitted), 95-96, 383 and 386
variable (A : Type*) [AddMonoid A]
variable (M : Type*) [Monoid M]
structure AddChar where
  toFun : A → M
  map_zero_eq_one' : toFun 0 = 1
  map_add_eq_mul' : ∀ a b : A, toFun (a + b) = toFun a * toFun b
instance instFunLike : FunLike (AddChar A M) A M where
  coe := AddChar.toFun
variable {A M : Type*} [AddGroup A] [DivisionMonoid M]
lemma map_neg_eq_inv (ψ : AddChar A M) (a : A) : ψ (-a) = (ψ a)⁻¹ := by
```

```lean
-- Mathlib/Analysis/Complex/Circle.lean, lines 50, 56, 58 and 70
def Circle : Type := Submonoid.unitSphere ℂ
instance instCoeOut : CoeOut Circle ℂ := subtypeCoe
instance instCommGroup : CommGroup Circle := inferInstanceAs <| CommGroup (sphere _ _)
lemma norm_coe (z : Circle) : ‖(z : ℂ)‖ = 1 := mem_sphere_zero_iff_norm.1 z.2
```

```lean
-- Mathlib/Analysis/Normed/Field/UnitBall.lean, lines 185-187;
-- Mathlib/Analysis/Normed/Group/Basic.lean, line 303, whose additive form
-- `mem_sphere_zero_iff_norm` comes from `to_additive`
def Submonoid.unitSphere (𝕜 : Type*) [SeminormedRing 𝕜] [NormMulClass 𝕜] [NormOneClass 𝕜] :
    Submonoid 𝕜 where
  carrier := sphere (0 : 𝕜) 1
theorem mem_sphere_one_iff_norm : a ∈ sphere (1 : E) r ↔ ‖a‖ = r := by simp
```

```lean
-- Mathlib/Analysis/Complex/Norm.lean, lines 26-27 and 29
instance instNorm : Norm ℂ where
  norm z := √(normSq z)
theorem norm_def (z : ℂ) : ‖z‖ = √(normSq z) := (rfl)
```

So `‖c z‖` is $\sqrt{\operatorname{Re}(c(z))^2+\operatorname{Im}(c(z))^2}$,
the modulus, and `Circle` is the set of complex numbers of modulus one. The
notation `∑ z ∈ A, f z` is `Finset.sum A f`, zero on the empty set.
`Mathlib.Analysis.SpecialFunctions.Complex.CircleAddChar`, one of the
imports through which `AddChar` and `Circle` reach `L20.lean`, defines
circle-valued characters of `ZMod N` and of the additive circle; nothing in
it enters the statement.

## Discrepancies

None.

## Verdict

**PASS.** The Lean statement `Erdos.L20.statement` at the checked source of
2026-09-28 is the prose statement of the
L20 card, clause for clause and at the same strength, its Scope exclusions
included, and `Erdos.L20.claim` is declared at exactly that statement. This
audit assigns no tier itself; it built nothing, ran no gate, and leaves
grading, the clean gate and any acceptance to their own records.

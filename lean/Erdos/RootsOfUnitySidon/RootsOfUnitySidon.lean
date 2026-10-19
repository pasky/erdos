import Mathlib.Combinatorics.Additive.Dissociation
import Mathlib.GroupTheory.OrderOfElement
import Mathlib.Data.Complex.Basic
import Mathlib.Data.Nat.Squarefree
import Mathlib.Data.Nat.Totient
import Mathlib.Analysis.SpecialFunctions.Complex.CircleAddChar
import Mathlib.Algebra.Category.Grp.Injective
import Mathlib.FieldTheory.Relrank
import Mathlib.NumberTheory.Cyclotomic.PrimitiveRoots
import Mathlib.RingTheory.RootsOfUnity.Complex
import Mathlib.RingTheory.Polynomial.Cyclotomic.Roots

/-!
# Roots of unity and proportional dissociation

Definitions and structural reductions for the roots-of-unity Sidon theorem.

`statement` is the proportional-dissociation conclusion and `AnalyticSidon`
is the harmonic-analytic assertion. The cyclotomic coset decomposition and
character gluing are proved for all positive orders. Proportional dissociation
of all roots is reduced to uniform extraction on odd squarefree orders, with a
factor-two loss for the prime-two coordinate. A positive-real bound on odd
squarefree orders transfers to all odd-order roots. The remaining analytic
argument and the uniform extraction theorem are proved in other modules in
this folder.
-/

namespace Erdos.Research.Problem774

open scoped ComplexConjugate

/-- The complex roots of unity, viewed in the additive group of `ℂ`. -/
def rootsOfUnity : Set ℂ := {z | IsOfFinOrder z}

/-- Roots whose multiplicative order is odd. -/
def oddRootsOfUnity : Set ℂ :=
  {z | ∃ n : ℕ, 0 < n ∧ Odd n ∧ z ^ n = 1}

/-- The roots of `X ^ n - 1`. The order-zero case is deliberately excluded
from the uniform finite-order hypothesis. -/
def nthRoots (n : ℕ) : Set ℂ := {z | z ^ n = 1}

/-- A single denominator `k` works for every finite subset of `s`. -/
def UniformExtraction (s : Set ℂ) (k : ℕ) : Prop :=
  ∀ A : Finset ℂ, (↑A : Set ℂ) ⊆ s →
    ∃ B : Finset ℂ, B ⊆ A ∧ AddDissociated (↑B : Set ℂ) ∧ A.card ≤ k * B.card

/-- The precise proportional-dissociation statement for all roots of unity. -/
def statement : Prop := ∃ k : ℕ, 0 < k ∧ UniformExtraction rootsOfUnity k

/-- Sidonicity in the discrete additive group of complex numbers. `AddChar`
imposes no continuity on the character. The finite set `A` is the support of
the trigonometric polynomial; coefficient values outside it are irrelevant. -/
def AnalyticSidon : Prop :=
  ∃ K : ℝ, 0 < K ∧
    ∀ A : Finset ℂ, (↑A : Set ℂ) ⊆ rootsOfUnity → ∀ c : ℂ → ℂ,
      ∃ χ : AddChar ℂ Circle,
        (∑ z ∈ A, ‖c z‖) ≤ K * ‖∑ z ∈ A, c z * (χ z : ℂ)‖

/-- The positive-real form of the Sidon inequality, convenient for gluing
linearly independent frequency components. -/
def PositiveRealBound (s : Set ℂ) (K : ℝ) : Prop :=
  ∀ A : Finset ℂ, (↑A : Set ℂ) ⊆ s → ∀ c : ℂ → ℂ,
    ∃ χ : AddChar ℂ Circle,
      (∑ z ∈ A, ‖c z‖) ≤
        K * (∑ z ∈ A, c z * (χ z : ℂ)).re

theorem analyticSidon_of_positiveRealBound (K : ℝ) (hK : 0 < K)
    (h : PositiveRealBound rootsOfUnity K) : AnalyticSidon := by
  refine ⟨K, hK, ?_⟩
  intro A hA c
  obtain ⟨χ, hχ⟩ := h A hA c
  refine ⟨χ, hχ.trans ?_⟩
  exact mul_le_mul_of_nonneg_left (Complex.re_le_norm _) hK.le

/-- Antipodal pairs rule out a positive-real Sidon bound on all even-order
roots; the analytic proof must treat them separately. -/
theorem not_positiveRealBound_nthRoots_two (K : ℝ) :
    ¬ PositiveRealBound (nthRoots 2) K := by
  intro h
  let A : Finset ℂ := {1, -1}
  let c : ℂ → ℂ := fun z => if z = 1 then 1 else -1
  have hA : (↑A : Set ℂ) ⊆ nthRoots 2 := by
    intro z hz
    simp only [A, Finset.mem_coe, Finset.mem_insert, Finset.mem_singleton] at hz
    rcases hz with rfl | rfl <;> norm_num [nthRoots]
  obtain ⟨χ, hχ⟩ := h A hA c
  have hnorm : (∑ z ∈ A, ‖c z‖) = 2 := by
    norm_num [A, c]
  have hpoly : (∑ z ∈ A, c z * (χ z : ℂ)).re = 0 := by
    have hneg : χ (-1 : ℂ) = (χ (1 : ℂ))⁻¹ := by
      simpa using χ.map_neg_eq_inv (1 : ℂ)
    have hnot : (1 : ℂ) ∉ ({-1} : Finset ℂ) := by norm_num
    dsimp [A]
    rw [Finset.sum_insert hnot, Finset.sum_singleton]
    have hinv : ((χ (1 : ℂ) : Circle) : ℂ)⁻¹ =
        conj (χ (1 : ℂ) : ℂ) := Circle.coe_inv_eq_conj (χ (1 : ℂ))
    have hminus : (-1 : ℂ) ≠ 1 := by norm_num
    simp [c, hneg, hinv, hminus]
  rw [hnorm, hpoly, mul_zero] at hχ
  norm_num at hχ

/-- A character on an additive subgroup of `ℂ`, valued in the additive circle,
extends to all of `ℂ`. This is the algebraic extension needed when a finite
cyclotomic lattice is used to construct a character. -/
theorem extend_addCircle_character (H : AddSubgroup ℂ)
    (χ : H →+ AddCircle (1 : ℝ)) :
    ∃ χ' : ℂ →+ AddCircle (1 : ℝ), χ'.comp H.subtype = χ :=
  (Module.Baer.of_divisible (AddCircle (1 : ℝ))).extension_property_addMonoidHom
    H.subtype H.subtype_injective χ

/-- A circle-valued character extends along any injective additive map into
the discrete additive group `ℂ`. -/
theorem extend_circle_character_along {A : Type*} [AddCommGroup A]
    (f : A →+ ℂ) (hf : Function.Injective f) (χ : AddChar A Circle) :
    ∃ χ' : AddChar ℂ Circle, ∀ z : A, χ' (f z) = χ z := by
  let e := AddCircle.homeomorphCircle (T := (1 : ℝ)) one_ne_zero
  have hto (z : Circle) : AddCircle.toCircle (e.symm z) = z := by
    calc
      AddCircle.toCircle (e.symm z) = e (e.symm z) :=
        (AddCircle.homeomorphCircle_apply one_ne_zero (e.symm z)).symm
      _ = z := e.apply_symm_apply z
  let g : A →+ AddCircle (1 : ℝ) := {
    toFun := fun z => e.symm (χ z)
    map_zero' := by
      apply AddCircle.injective_toCircle one_ne_zero
      change AddCircle.toCircle (e.symm (χ 0)) = AddCircle.toCircle 0
      rw [χ.map_zero_eq_one, hto]
      simp
    map_add' := by
      intro x y
      apply AddCircle.injective_toCircle one_ne_zero
      change AddCircle.toCircle (e.symm (χ (x + y))) =
        AddCircle.toCircle (e.symm (χ x) + e.symm (χ y))
      rw [AddCircle.toCircle_add, hto, hto, hto, χ.map_add_eq_mul]
  }
  obtain ⟨g', hg'⟩ :=
    (Module.Baer.of_divisible (AddCircle (1 : ℝ))).extension_property_addMonoidHom f hf g
  refine ⟨AddCircle.toCircle_addChar.compAddMonoidHom g', ?_⟩
  intro z
  have hz := congrArg (fun h : A →+ AddCircle (1 : ℝ) => h z) hg'
  change g' (f z) = g z at hz
  change AddCircle.toCircle (g' (f z)) = χ z
  rw [hz]
  change AddCircle.toCircle (e.symm (χ z)) = χ z
  exact hto (χ z)

/-- Circle-valued additive characters on a subgroup of `ℂ` extend to the
discrete additive group `ℂ`. -/
theorem extend_circle_character (H : AddSubgroup ℂ)
    (χ : AddChar H Circle) :
    ∃ χ' : AddChar ℂ Circle, ∀ z : H, χ' (z : ℂ) = χ z :=
  extend_circle_character_along H.subtype H.subtype_injective χ

/-- Characters chosen separately on linearly independent scalar copies can
be realized by one character of the discrete additive group `ℂ`. -/
theorem glue_characters_over_field (K : IntermediateField ℚ ℂ) (m : ℕ)
    (v : Fin m → ℂ)
    (hli : LinearIndependent K v)
    (χ : Fin m → AddChar ℂ Circle) :
    ∃ χ' : AddChar ℂ Circle,
      ∀ (i : Fin m) (c : K), χ' ((c : ℂ) * v i) = χ i (c : ℂ) := by
  classical
  let ψ : AddChar (Fin m → K) Circle := {
    toFun := fun a => ∏ i : Fin m, χ i (a i : ℂ)
    map_zero_eq_one' := by simp
    map_add_eq_mul' := by
      intro a b
      simp [Finset.prod_mul_distrib, AddChar.map_add_eq_mul]
  }
  let T : (Fin m → K) →ₗ[K] ℂ := Fintype.linearCombination K v
  have hT : Function.Injective T := hli.fintypeLinearCombination_injective
  obtain ⟨χ', hχ'⟩ := extend_circle_character_along T.toAddMonoidHom hT ψ
  refine ⟨χ', ?_⟩
  intro i c
  have hi := hχ' (Pi.single i c)
  change χ' (T (Pi.single i c)) = ψ (Pi.single i c) at hi
  rw [Fintype.linearCombination_apply_single] at hi
  let a : Fin m → K := Pi.single i c
  have hprod : ψ (Pi.single i c) = χ i (c : ℂ) := by
    change (∏ x : Fin m, χ x (a x : ℂ)) = χ i (c : ℂ)
    rw [Finset.prod_eq_single_of_mem i (Finset.mem_univ _)]
    · simp [a]
    · intro j _ hji
      simp [a, hji]
  rw [hprod] at hi
  simpa [Algebra.smul_def] using hi

/-- The extraction denominator is unchanged by an additive equivalence. This
is the formal version of passing to a nonzero scalar copy of a root grid. -/
theorem uniformExtraction_image (e : ℂ ≃+ ℂ) (s : Set ℂ) (k : ℕ)
    (h : UniformExtraction s k) : UniformExtraction (e '' s) k := by
  classical
  intro A hA
  let A' : Finset ℂ := A.map e.symm.toEmbedding
  have hA' : (↑A' : Set ℂ) ⊆ s := by
    intro z hz
    obtain ⟨x, hx, rfl⟩ := Finset.mem_map.mp hz
    obtain ⟨y, hy, rfl⟩ := hA hx
    simpa using hy
  obtain ⟨B, hBA, hB, hcard⟩ := h A' hA'
  let B' : Finset ℂ := B.map e.toEmbedding
  refine ⟨B', ?_, ?_, ?_⟩
  · intro x hx
    obtain ⟨y, hy, rfl⟩ := Finset.mem_map.mp hx
    have hyA := hBA hy
    obtain ⟨z, hz, rfl⟩ := Finset.mem_map.mp hyA
    simpa using hz
  · apply (e.addDissociated_preimage).mp
    simpa [B', Set.preimage] using hB
  · simpa [A', B'] using hcard

private def scalarAddEquiv (u : ℂˣ) : ℂ ≃+ ℂ where
  toFun z := (u : ℂ) * z
  invFun z := ((u⁻¹ : ℂˣ) : ℂ) * z
  left_inv z := by simp
  right_inv z := by simp
  map_add' x y := mul_add _ _ _

theorem uniformExtraction_scalar (u : ℂˣ) (s : Set ℂ) (k : ℕ)
    (h : UniformExtraction s k) :
    UniformExtraction ((fun z : ℂ => (u : ℂ) * z) '' s) k := by
  exact uniformExtraction_image (scalarAddEquiv u) s k h

/-- Extraction from a union costs at most the sum of the two denominators.
The extracted set comes from whichever side yields the larger witness. -/
theorem uniformExtraction_union (s t : Set ℂ) (k l : ℕ)
    (hs : UniformExtraction s k) (ht : UniformExtraction t l) :
    UniformExtraction (s ∪ t) (k + l) := by
  classical
  intro A hA
  let As := A.filter (fun z => z ∈ s)
  let At := A.filter (fun z => z ∉ s)
  have hAs : (↑As : Set ℂ) ⊆ s := by
    intro z hz
    exact (Finset.mem_filter.mp hz).2
  have hAt : (↑At : Set ℂ) ⊆ t := by
    intro z hz
    have hz' := Finset.mem_filter.mp hz
    rcases hA hz'.1 with hzS | hzT
    · exact False.elim (hz'.2 hzS)
    · exact hzT
  obtain ⟨Bs, hBs, hDs, hcs⟩ := hs As hAs
  obtain ⟨Bt, hBt, hDt, hct⟩ := ht At hAt
  have hcard : As.card + At.card = A.card := by
    simpa [As, At] using
      (Finset.card_filter_add_card_filter_not (s := A) (fun z : ℂ => z ∈ s))
  by_cases hle : Bs.card ≤ Bt.card
  · refine ⟨Bt, hBt.trans (Finset.filter_subset _ _), hDt, ?_⟩
    have hmul : k * Bs.card ≤ k * Bt.card := Nat.mul_le_mul_left k hle
    calc
      A.card = As.card + At.card := hcard.symm
      _ ≤ k * Bs.card + l * Bt.card := Nat.add_le_add hcs hct
      _ ≤ k * Bt.card + l * Bt.card := Nat.add_le_add_right hmul _
      _ = (k + l) * Bt.card := (Nat.add_mul ..).symm
  · have hle' : Bt.card ≤ Bs.card := Nat.le_of_not_ge hle
    refine ⟨Bs, hBs.trans (Finset.filter_subset _ _), hDs, ?_⟩
    have hmul : l * Bt.card ≤ l * Bs.card := Nat.mul_le_mul_left l hle'
    calc
      A.card = As.card + At.card := hcard.symm
      _ ≤ k * Bs.card + l * Bt.card := Nat.add_le_add hcs hct
      _ ≤ k * Bs.card + l * Bs.card := Nat.add_le_add_left hmul _
      _ = (k + l) * Bs.card := (Nat.add_mul ..).symm

theorem uniformExtraction_of_le (s : Set ℂ) {k l : ℕ} (hkl : k ≤ l)
    (h : UniformExtraction s k) : UniformExtraction s l := by
  intro A hA
  obtain ⟨B, hB, hD, hcard⟩ := h A hA
  refine ⟨B, hB, hD, hcard.trans ?_⟩
  exact Nat.mul_le_mul_right B.card hkl

theorem positiveRealBound_image (e : ℂ ≃+ ℂ) (s : Set ℂ) (K : ℝ)
    (h : PositiveRealBound s K) : PositiveRealBound (e '' s) K := by
  classical
  intro A hA c
  let A' : Finset ℂ := A.map e.symm.toEmbedding
  have hA' : (↑A' : Set ℂ) ⊆ s := by
    intro z hz
    obtain ⟨x, hx, rfl⟩ := Finset.mem_map.mp hz
    obtain ⟨y, hy, rfl⟩ := hA hx
    simpa using hy
  obtain ⟨χ, hχ⟩ := h A' hA' (fun z => c (e z))
  let χ' : AddChar ℂ Circle := χ.compAddMonoidHom e.symm.toAddMonoidHom
  refine ⟨χ', ?_⟩
  simpa [A', χ', Finset.sum_map] using hχ

theorem positiveRealBound_scalar (u : ℂˣ) (s : Set ℂ) (K : ℝ)
    (h : PositiveRealBound s K) :
    PositiveRealBound ((fun z : ℂ => (u : ℂ) * z) '' s) K := by
  exact positiveRealBound_image (scalarAddEquiv u) s K h

/-- A relation among elements of `s` separates over the fibers of `f`.
For root-order cosets this is supplied by the rational direct-sum theorem. -/
def FiberSeparates {ι : Type*} [DecidableEq ι] (s : Set ℂ) (f : ℂ → ι) : Prop :=
  ∀ U V : Finset ℂ, (↑U : Set ℂ) ⊆ s → (↑V : Set ℂ) ⊆ s →
    (∑ z ∈ U, z) = (∑ z ∈ V, z) →
    ∀ i : ι, (∑ z ∈ U.filter (fun z => f z = i), z) =
      (∑ z ∈ V.filter (fun z => f z = i), z)

/-- Characters selected independently on the fibers can be combined into a
single character on their union. -/
def FiberCharactersGlue {ι : Type*} (s : Set ℂ) (f : ℂ → ι) : Prop :=
  ∀ χ : ι → AddChar ℂ Circle,
    ∃ χ' : AddChar ℂ Circle, ∀ z ∈ s, χ' z = χ (f z) z

theorem positiveRealBound_of_fibers {ι : Type*} [Fintype ι] [DecidableEq ι]
    (s : Set ℂ) (f : ℂ → ι) (K : ℝ)
    (hfiber : ∀ i : ι, PositiveRealBound {z | z ∈ s ∧ f z = i} K)
    (hglue : FiberCharactersGlue s f) :
    PositiveRealBound s K := by
  classical
  intro A hA c
  let Ai (i : ι) : Finset ℂ := A.filter (fun z => f z = i)
  have hAi (i : ι) : (↑(Ai i) : Set ℂ) ⊆ {z | z ∈ s ∧ f z = i} := by
    intro z hz
    exact ⟨hA (Finset.mem_filter.mp hz).1, (Finset.mem_filter.mp hz).2⟩
  let χi (i : ι) : AddChar ℂ Circle := (hfiber i (Ai i) (hAi i) c).choose
  have hχi (i : ι) :
      (∑ z ∈ Ai i, ‖c z‖) ≤
        K * (∑ z ∈ Ai i, c z * (χi i z : ℂ)).re :=
    (hfiber i (Ai i) (hAi i) c).choose_spec
  obtain ⟨χ, hχ⟩ := hglue χi
  refine ⟨χ, ?_⟩
  have hnorm : (∑ z ∈ A, ‖c z‖) = ∑ i : ι, ∑ z ∈ Ai i, ‖c z‖ := by
    simpa [Ai] using
      (Finset.sum_fiberwise_eq_sum_filter A Finset.univ f (fun z => ‖c z‖)).symm
  have hpoly : (∑ z ∈ A, c z * (χ z : ℂ)) =
      ∑ i : ι, ∑ z ∈ Ai i, c z * (χi i z : ℂ) := by
    calc
      (∑ z ∈ A, c z * (χ z : ℂ)) =
          ∑ i : ι, ∑ z ∈ Ai i, c z * (χ z : ℂ) := by
        simpa [Ai] using
          (Finset.sum_fiberwise_eq_sum_filter A Finset.univ f
            (fun z => c z * (χ z : ℂ))).symm
      _ = ∑ i : ι, ∑ z ∈ Ai i, c z * (χi i z : ℂ) := by
        apply Finset.sum_congr rfl
        intro i _
        apply Finset.sum_congr rfl
        intro z hz
        rw [hχ z (hA (Finset.mem_filter.mp hz).1)]
        rw [(Finset.mem_filter.mp hz).2]
  calc
    (∑ z ∈ A, ‖c z‖) = ∑ i : ι, ∑ z ∈ Ai i, ‖c z‖ := hnorm
    _ ≤ ∑ i : ι, K * (∑ z ∈ Ai i, c z * (χi i z : ℂ)).re := by
      apply Finset.sum_le_sum
      intro i _
      exact hχi i
    _ = K * (∑ i : ι, ∑ z ∈ Ai i, c z * (χi i z : ℂ)).re := by
      rw [← Finset.mul_sum, Complex.re_sum]
    _ = K * (∑ z ∈ A, c z * (χ z : ℂ)).re := by rw [hpoly]

/-- Uniform extraction in every fiber gives uniform extraction in their
union when all additive relations separate by fibers. -/
theorem uniformExtraction_of_fibers {ι : Type*} [Fintype ι] [DecidableEq ι]
    (s : Set ℂ) (f : ℂ → ι) (k : ℕ)
    (hsep : FiberSeparates s f)
    (hfiber : ∀ i : ι, UniformExtraction {z | z ∈ s ∧ f z = i} k) :
    UniformExtraction s k := by
  classical
  intro A hA
  let Ai (i : ι) : Finset ℂ := A.filter (fun z => f z = i)
  have hAi (i : ι) : (↑(Ai i) : Set ℂ) ⊆ {z | z ∈ s ∧ f z = i} := by
    intro z hz
    exact ⟨hA (Finset.mem_filter.mp hz).1, (Finset.mem_filter.mp hz).2⟩
  let Bi (i : ι) : Finset ℂ := (hfiber i (Ai i) (hAi i)).choose
  have hBi (i : ι) :
      Bi i ⊆ Ai i ∧ AddDissociated (↑(Bi i) : Set ℂ) ∧
        (Ai i).card ≤ k * (Bi i).card :=
    (hfiber i (Ai i) (hAi i)).choose_spec
  let B : Finset ℂ := A.filter (fun z => z ∈ Bi (f z))
  have hBA : B ⊆ A := Finset.filter_subset _ _
  have hBfiber (i : ι) : B.filter (fun z => f z = i) = Bi i := by
    ext z
    constructor
    · intro hz
      have hz' := Finset.mem_filter.mp hz
      have hzBi := (Finset.mem_filter.mp hz'.1).2
      simpa [hz'.2] using hzBi
    · intro hz
      have hzAi := (hBi i).1 hz
      have hzA := (Finset.mem_filter.mp hzAi).1
      have hzi := (Finset.mem_filter.mp hzAi).2
      exact Finset.mem_filter.mpr ⟨Finset.mem_filter.mpr ⟨hzA, by simpa [hzi] using hz⟩, hzi⟩
  refine ⟨B, hBA, ?_, ?_⟩
  · intro U hU V hV hsum
    have hUS : (↑U : Set ℂ) ⊆ s := by
      intro z hz
      exact hA (hBA (hU hz))
    have hVS : (↑V : Set ℂ) ⊆ s := by
      intro z hz
      exact hA (hBA (hV hz))
    have hEq (i : ι) : U.filter (fun z => f z = i) =
        V.filter (fun z => f z = i) := by
      apply (hBi i).2.1
      · intro z hz
        have hzB := hU (Finset.mem_filter.mp hz).1
        have hzBi := (Finset.mem_filter.mp hzB).2
        simpa [(Finset.mem_filter.mp hz).2] using hzBi
      · intro z hz
        have hzB := hV (Finset.mem_filter.mp hz).1
        have hzBi := (Finset.mem_filter.mp hzB).2
        simpa [(Finset.mem_filter.mp hz).2] using hzBi
      · exact hsep U V hUS hVS hsum i
    ext z
    have hz := congrArg (fun T : Finset ℂ => z ∈ T) (hEq (f z))
    simpa using hz
  · have hcountA : A.card = ∑ i : ι, (Ai i).card := by
      simpa [Ai] using
        (Finset.card_eq_sum_card_fiberwise (s := A) (t := Finset.univ)
          (f := f) (by simp))
    have hcountB : B.card = ∑ i : ι, (Bi i).card := by
      calc
        B.card = ∑ i : ι, (B.filter (fun z => f z = i)).card := by
          simpa using
            (Finset.card_eq_sum_card_fiberwise (s := B) (t := Finset.univ)
              (f := f) (by simp))
        _ = ∑ i : ι, (Bi i).card := by simp [hBfiber]
    calc
      A.card = ∑ i : ι, (Ai i).card := hcountA
      _ ≤ ∑ i : ι, k * (Bi i).card := by
        apply Finset.sum_le_sum
        intro i _
        exact (hBi i).2.2
      _ = k * ∑ i : ι, (Bi i).card := by rw [Finset.mul_sum]
      _ = k * B.card := by rw [← hcountB]

/-- The product of the distinct prime factors of `n`. -/
def radical (n : ℕ) : ℕ := ∏ p ∈ n.primeFactors, p

theorem radical_pos (n : ℕ) : 0 < radical n := by
  unfold radical
  exact Finset.prod_pos fun p hp => Nat.pos_of_mem_primeFactors hp

theorem radical_dvd (n : ℕ) : radical n ∣ n :=
  Nat.prod_primeFactors_dvd n

theorem radical_squarefree (n : ℕ) : Squarefree (radical n) := by
  unfold radical
  refine Finset.squarefree_prod_of_pairwise_isCoprime (fun p hp q hq hpq => ?_)
    (fun p hp => (Nat.prime_of_mem_primeFactors hp).squarefree)
  simpa only [← Nat.coprime_iff_isRelPrime] using
    (Nat.coprime_primes (Nat.prime_of_mem_primeFactors hp)
      (Nat.prime_of_mem_primeFactors hq)).mpr hpq

theorem radical_mul_quotient (n : ℕ) : radical n * (n / radical n) = n :=
  Nat.mul_div_cancel' (radical_dvd n)

/-- The degree identity behind the direct-sum count in the cyclotomic step. -/
theorem totient_eq_div_radical_mul_totient (n : ℕ) :
    n.totient = (n / radical n) * (radical n).totient := by
  have hrpos := radical_pos n
  rw [Nat.totient_eq_div_primeFactors_mul n,
    Nat.totient_eq_div_primeFactors_mul (radical n)]
  rw [show (radical n).primeFactors = n.primeFactors from
    Nat.primeFactors_prod_primeFactors n]
  rw [show (∏ p ∈ n.primeFactors, p) = radical n from rfl,
    Nat.div_self hrpos, one_mul]

/-- The standard complex primitive `n`-th root used for coset coordinates. -/
noncomputable def zeta (n : ℕ) : ℂ :=
  Complex.exp (2 * (Real.pi : ℂ) * Complex.I / (n : ℂ))

theorem zeta_isPrimitiveRoot (n : ℕ) (hn : 0 < n) :
    IsPrimitiveRoot (zeta n) n := by
  exact Complex.isPrimitiveRoot_exp n hn.ne'

theorem cyclotomic_finrank (n : ℕ) (hn : 0 < n) :
    Module.finrank ℚ (Algebra.adjoin ℚ ({zeta n} : Set ℂ)) = n.totient := by
  letI : NeZero n := ⟨hn.ne'⟩
  letI : IsCyclotomicExtension {n} ℚ (Algebra.adjoin ℚ ({zeta n} : Set ℂ)) :=
    (zeta_isPrimitiveRoot n hn).adjoin_isCyclotomicExtension ℚ
  exact IsCyclotomicExtension.finrank _ (Polynomial.cyclotomic.irreducible_rat hn)

theorem primitiveRoot_field_finrank {z : ℂ} {n : ℕ} (hn : 0 < n)
    (hz : IsPrimitiveRoot z n) :
    Module.finrank ℚ (IntermediateField.adjoin ℚ ({z} : Set ℂ)) = n.totient := by
  have hζ : IsAlgebraic ℚ z := (((hz.isIntegral hn).tower_top).isAlgebraic)
  have hdegree : Module.finrank ℚ (Algebra.adjoin ℚ ({z} : Set ℂ)) = n.totient := by
    letI : NeZero n := ⟨hn.ne'⟩
    letI : IsCyclotomicExtension {n} ℚ (Algebra.adjoin ℚ ({z} : Set ℂ)) :=
      hz.adjoin_isCyclotomicExtension ℚ
    exact IsCyclotomicExtension.finrank _ (Polynomial.cyclotomic.irreducible_rat hn)
  calc
    Module.finrank ℚ (IntermediateField.adjoin ℚ ({z} : Set ℂ)) =
        Module.finrank ℚ (IntermediateField.adjoin ℚ ({z} : Set ℂ)).toSubalgebra :=
      (IntermediateField.finrank_eq_finrank_subalgebra _).symm
    _ = Module.finrank ℚ (Algebra.adjoin ℚ ({z} : Set ℂ)) := by
      rw [IntermediateField.adjoin_toSubalgebra_of_isAlgebraic]
      simpa using hζ
    _ = n.totient := hdegree

theorem cyclotomic_field_finrank (n : ℕ) (hn : 0 < n) :
    Module.finrank ℚ (IntermediateField.adjoin ℚ ({zeta n} : Set ℂ)) = n.totient :=
  primitiveRoot_field_finrank hn (zeta_isPrimitiveRoot n hn)

/-- The root obtained by collapsing repeated prime factors has exactly the
radical order. -/
theorem zeta_pow_quotient_isPrimitiveRoot (n : ℕ) (hn : 0 < n) :
    IsPrimitiveRoot (zeta n ^ (n / radical n)) (radical n) := by
  apply IsPrimitiveRoot.pow hn (zeta_isPrimitiveRoot n hn)
  exact (radical_mul_quotient n).symm.trans (mul_comm _ _)

/-- The two cyclotomic fields in the prime-power decomposition form a tower. -/
theorem radical_cyclotomic_le (n : ℕ) :
    IntermediateField.adjoin ℚ ({zeta n ^ (n / radical n)} : Set ℂ) ≤
      IntermediateField.adjoin ℚ ({zeta n} : Set ℂ) := by
  rw [IntermediateField.adjoin_le_iff]
  intro z hz
  obtain rfl := Set.mem_singleton_iff.mp hz
  exact pow_mem (IntermediateField.mem_adjoin_simple_self ℚ (zeta n)) _

/-- The relative degree is exactly the number of radical-order cosets. -/
theorem radical_cyclotomic_relfinrank (n : ℕ) (hn : 0 < n) :
    IntermediateField.relfinrank
      (IntermediateField.adjoin ℚ ({zeta n ^ (n / radical n)} : Set ℂ))
      (IntermediateField.adjoin ℚ ({zeta n} : Set ℂ)) =
      n / radical n := by
  have hrpos := radical_pos n
  have heta := zeta_pow_quotient_isPrimitiveRoot n hn
  have hK : Module.finrank ℚ
      (IntermediateField.adjoin ℚ ({zeta n ^ (n / radical n)} : Set ℂ)) =
      (radical n).totient := primitiveRoot_field_finrank hrpos heta
  have hL := cyclotomic_field_finrank n hn
  have htower := IntermediateField.finrank_bot_mul_relfinrank (radical_cyclotomic_le n)
  rw [hK, hL, totient_eq_div_radical_mul_totient n] at htower
  exact Nat.eq_of_mul_eq_mul_left (Nat.totient_pos.mpr hrpos) (by simpa [mul_comm] using htower)

/-- The relative cyclotomic field is generated by the original root. -/
private theorem radical_adjoin_zeta (n : ℕ) :
    let K := IntermediateField.adjoin ℚ ({zeta n ^ (n / radical n)} : Set ℂ)
    let L := IntermediateField.adjoin ℚ ({zeta n} : Set ℂ)
    IntermediateField.adjoin K ({zeta n} : Set ℂ) =
      IntermediateField.extendScalars (radical_cyclotomic_le n : K ≤ L) := by
  dsimp
  apply le_antisymm
  · rw [IntermediateField.adjoin_le_iff]
    intro z hz
    obtain rfl := Set.mem_singleton_iff.mp hz
    change zeta n ∈ IntermediateField.adjoin ℚ ({zeta n} : Set ℂ)
    exact IntermediateField.mem_adjoin_simple_self ℚ (zeta n)
  · rw [IntermediateField.extendScalars_le_iff]
    rw [IntermediateField.adjoin_le_iff]
    intro z hz
    obtain rfl := Set.mem_singleton_iff.mp hz
    exact IntermediateField.mem_adjoin_simple_self _ (zeta n)

/-- Powers indexing the radical-order cosets are independent over the smaller
cyclotomic field. -/
theorem radical_cyclotomic_powers_linearIndependent (n : ℕ) (hn : 0 < n) :
    let K := IntermediateField.adjoin ℚ ({zeta n ^ (n / radical n)} : Set ℂ)
    LinearIndependent K (fun i : Fin (n / radical n) => zeta n ^ (i : ℕ)) := by
  dsimp
  let K := IntermediateField.adjoin ℚ ({zeta n ^ (n / radical n)} : Set ℂ)
  let L := IntermediateField.adjoin ℚ ({zeta n} : Set ℂ)
  have hKL : K ≤ L := radical_cyclotomic_le n
  have hζint : IsIntegral K (zeta n) :=
    IsIntegral.tower_top (A := K)
      (((zeta_isPrimitiveRoot n hn).isIntegral hn).tower_top : IsIntegral ℚ (zeta n))
  have hfin : Module.finrank K (IntermediateField.adjoin K ({zeta n} : Set ℂ)) =
      n / radical n := by
    rw [radical_adjoin_zeta n]
    exact (IntermediateField.relfinrank_eq_finrank_of_le hKL).symm.trans
      (radical_cyclotomic_relfinrank n hn)
  have hdeg : (minpoly K (zeta n)).natDegree = n / radical n :=
    (IntermediateField.adjoin.finrank hζint).symm.trans hfin
  have hli := linearIndependent_pow (K := K) (zeta n)
  rw [hdeg] at hli
  exact hli

/-- Every radical-order root is a coefficient in the smaller field. -/
theorem nthRoots_subset_radical_cyclotomic (n : ℕ) (hn : 0 < n) :
    nthRoots (radical n) ⊆
      (IntermediateField.adjoin ℚ
        ({zeta n ^ (n / radical n)} : Set ℂ) : Set ℂ) := by
  letI : NeZero (radical n) := ⟨(radical_pos n).ne'⟩
  intro z hz
  obtain ⟨i, _, rfl⟩ :=
    (zeta_pow_quotient_isPrimitiveRoot n hn).eq_pow_of_pow_eq_one hz
  exact pow_mem (IntermediateField.mem_adjoin_simple_self ℚ
    (zeta n ^ (n / radical n))) i

/-- Linear independence of the coset representatives separates additive
relations whenever each point has a coefficient in the base field. -/
theorem fiberSeparates_of_power_linearIndependent
    (K : IntermediateField ℚ ℂ) (α : ℂ) (m : ℕ)
    (s : Set ℂ) (f : ℂ → Fin m)
    (hli : LinearIndependent K (fun i : Fin m => α ^ (i : ℕ)))
    (hdecomp : ∀ z ∈ s, ∃ c : K, z = (c : ℂ) * α ^ (f z : ℕ)) :
    FiberSeparates s f := by
  classical
  let c (z : ℂ) : K := if hz : z ∈ s then (hdecomp z hz).choose else 0
  have hc (z : ℂ) (hz : z ∈ s) : z = (c z : ℂ) * α ^ (f z : ℕ) := by
    simp only [c, dif_pos hz]
    exact (hdecomp z hz).choose_spec
  intro U V hUs hVs hsum i
  let gU (j : Fin m) : K := ∑ z ∈ U.filter (fun z => f z = j), c z
  let gV (j : Fin m) : K := ∑ z ∈ V.filter (fun z => f z = j), c z
  have hU (j : Fin m) :
      (∑ z ∈ U.filter (fun z => f z = j), z) = (gU j : ℂ) * α ^ (j : ℕ) := by
    calc
      (∑ z ∈ U.filter (fun z => f z = j), z) =
          ∑ z ∈ U.filter (fun z => f z = j), (c z : ℂ) * α ^ (j : ℕ) := by
        apply Finset.sum_congr rfl
        intro z hz
        rw [← (Finset.mem_filter.mp hz).2]
        exact hc z (hUs (Finset.mem_filter.mp hz).1)
      _ = (gU j : ℂ) * α ^ (j : ℕ) := by simp [gU, Finset.sum_mul]
  have hV (j : Fin m) :
      (∑ z ∈ V.filter (fun z => f z = j), z) = (gV j : ℂ) * α ^ (j : ℕ) := by
    calc
      (∑ z ∈ V.filter (fun z => f z = j), z) =
          ∑ z ∈ V.filter (fun z => f z = j), (c z : ℂ) * α ^ (j : ℕ) := by
        apply Finset.sum_congr rfl
        intro z hz
        rw [← (Finset.mem_filter.mp hz).2]
        exact hc z (hVs (Finset.mem_filter.mp hz).1)
      _ = (gV j : ℂ) * α ^ (j : ℕ) := by simp [gV, Finset.sum_mul]
  have hsumU : (∑ z ∈ U, z) = ∑ j : Fin m, (∑ z ∈ U.filter (fun z => f z = j), z) := by
    simpa using (Finset.sum_fiberwise_eq_sum_filter U Finset.univ f id).symm
  have hsumV : (∑ z ∈ V, z) = ∑ j : Fin m, (∑ z ∈ V.filter (fun z => f z = j), z) := by
    simpa using (Finset.sum_fiberwise_eq_sum_filter V Finset.univ f id).symm
  have hcoeff : gU i = gV i := by
    have hzero : (∑ j : Fin m, (gU j - gV j) • α ^ (j : ℕ)) = 0 := by
      calc
        (∑ j : Fin m, (gU j - gV j) • α ^ (j : ℕ)) =
            (∑ j : Fin m, (gU j : ℂ) * α ^ (j : ℕ)) -
              (∑ j : Fin m, (gV j : ℂ) * α ^ (j : ℕ)) := by
          simp [Algebra.smul_def, sub_mul, Finset.sum_sub_distrib]
        _ = (∑ z ∈ U, z) - (∑ z ∈ V, z) := by
          rw [hsumU, hsumV]
          simp_rw [hU, hV]
        _ = 0 := sub_eq_zero.mpr hsum
    have hi := (Fintype.linearIndependent_iff.mp hli) (fun j => gU j - gV j) hzero i
    exact sub_eq_zero.mp hi
  rw [hU i, hV i, hcoeff]

private theorem quotient_pos (n : ℕ) (hn : 0 < n) : 0 < n / radical n := by
  have h := radical_mul_quotient n
  by_contra hz
  have hz' : n / radical n = 0 := Nat.eq_zero_of_not_pos hz
  simp [hz'] at h
  omega

/-- Each `n`-th root lies in one of the displayed radical-order cosets. -/
theorem nthRoot_exists_radical_coset (n : ℕ) (hn : 0 < n)
    (z : ℂ) (hz : z ∈ nthRoots n) :
    ∃ i : Fin (n / radical n), ∃ w ∈ nthRoots (radical n),
      z = zeta n ^ (i : ℕ) * w := by
  letI : NeZero n := ⟨hn.ne'⟩
  obtain ⟨j, hj, rfl⟩ := (zeta_isPrimitiveRoot n hn).eq_pow_of_pow_eq_one hz
  let m := n / radical n
  have hm : 0 < m := quotient_pos n hn
  let i : Fin m := ⟨j % m, Nat.mod_lt _ hm⟩
  let w : ℂ := (zeta n ^ m) ^ (j / m)
  refine ⟨i, w, ?_, ?_⟩
  · change w ^ radical n = 1
    dsimp [w]
    rw [← pow_mul, mul_comm (j / m) (radical n), pow_mul]
    have hζ : (zeta n ^ m) ^ radical n = 1 := by
      rw [← pow_mul, show m * radical n = n from by
        simpa [m, mul_comm] using radical_mul_quotient n]
      exact (zeta_isPrimitiveRoot n hn).pow_eq_one
    rw [hζ, one_pow]
  · change zeta n ^ j = zeta n ^ (j % m) * (zeta n ^ m) ^ (j / m)
    rw [← pow_mul, ← pow_add, Nat.mod_add_div]

/-- Distinct representatives give disjoint radical-order cosets. -/
theorem radical_coset_unique (n : ℕ) (hn : 0 < n)
    {i j : Fin (n / radical n)} {w v : ℂ}
    (hw : w ∈ nthRoots (radical n)) (hv : v ∈ nthRoots (radical n))
    (h : zeta n ^ (i : ℕ) * w = zeta n ^ (j : ℕ) * v) : i = j := by
  have hroot : IsPrimitiveRoot (zeta n ^ radical n) (n / radical n) :=
    IsPrimitiveRoot.pow hn (zeta_isPrimitiveRoot n hn)
      (radical_mul_quotient n).symm
  have hp := congrArg (fun z : ℂ => z ^ radical n) h
  change w ^ radical n = 1 at hw
  change v ^ radical n = 1 at hv
  simp only [mul_pow, hw, hv, mul_one, ← pow_mul] at hp
  apply Fin.ext
  apply hroot.pow_inj i.isLt j.isLt
  calc
    (zeta n ^ radical n) ^ (i : ℕ) = (zeta n ^ (i : ℕ)) ^ radical n := by
      rw [← pow_mul, ← pow_mul, mul_comm]
    _ = (zeta n ^ (j : ℕ)) ^ radical n := by simpa only [pow_mul] using hp
    _ = (zeta n ^ radical n) ^ (j : ℕ) := by
      rw [← pow_mul, ← pow_mul, mul_comm]

/-- Index of the radical-order coset containing an `n`-th root. Outside the
root grid its value is arbitrary. -/
noncomputable def rootCosetIndex (n : ℕ) (hn : 0 < n) (z : ℂ) :
    Fin (n / radical n) := by
  classical
  exact if hz : z ∈ nthRoots n then (nthRoot_exists_radical_coset n hn z hz).choose
    else ⟨0, quotient_pos n hn⟩

theorem rootCosetIndex_spec (n : ℕ) (hn : 0 < n)
    (z : ℂ) (hz : z ∈ nthRoots n) :
    ∃ w ∈ nthRoots (radical n),
      z = zeta n ^ (rootCosetIndex n hn z : ℕ) * w := by
  simpa [rootCosetIndex, hz] using
    (nthRoot_exists_radical_coset n hn z hz).choose_spec

theorem rootCosetIndex_eq (n : ℕ) (hn : 0 < n)
    (z : ℂ) (i : Fin (n / radical n)) (w : ℂ)
    (hw : w ∈ nthRoots (radical n))
    (hz : z ∈ nthRoots n)
    (h : z = zeta n ^ (i : ℕ) * w) : rootCosetIndex n hn z = i := by
  obtain ⟨v, hv, hspec⟩ := rootCosetIndex_spec n hn z hz
  exact radical_coset_unique n hn hv hw (hspec.symm.trans h)

theorem radical_coset_mem_nthRoots (n : ℕ) (hn : 0 < n)
    (i : Fin (n / radical n)) (w : ℂ)
    (hw : w ∈ nthRoots (radical n)) :
    zeta n ^ (i : ℕ) * w ∈ nthRoots n := by
  change (zeta n ^ (i : ℕ) * w) ^ n = 1
  change w ^ radical n = 1 at hw
  have hζ : (zeta n ^ (i : ℕ)) ^ n = 1 := by
    rw [← pow_mul, mul_comm]
    rw [pow_mul, (zeta_isPrimitiveRoot n hn).pow_eq_one, one_pow]
  have hw' : w ^ n = 1 := by
    rw [← radical_mul_quotient n, pow_mul, hw, one_pow]
  rw [mul_pow, hζ, hw', one_mul]

/-- This is the exact cyclotomic input needed for the prime-power step: the
`n`-th roots split into scalar copies of the `radical n`-th roots, and signed
relations separate across the copies. -/
def HasCyclotomicCosetDecomposition (n : ℕ) : Prop :=
  ∃ m : ℕ, ∃ f : ℂ → Fin m, ∃ u : Fin m → ℂˣ,
    FiberSeparates (nthRoots n) f ∧
      ∀ i : Fin m, {z | z ∈ nthRoots n ∧ f z = i} =
        ((fun z : ℂ => (u i : ℂ) * z) '' nthRoots (radical n))

/-- The cyclotomic coset decomposition, including separation of signed
relations, for every positive order. -/
theorem hasCyclotomicCosetDecomposition (n : ℕ) (hn : 0 < n) :
    HasCyclotomicCosetDecomposition n := by
  classical
  let m := n / radical n
  let f : ℂ → Fin m := rootCosetIndex n hn
  let u : Fin m → ℂˣ := fun i =>
    Units.mk0 (zeta n ^ (i : ℕ)) (pow_ne_zero _ (Complex.exp_ne_zero _))
  refine ⟨m, f, u, ?_, ?_⟩
  · have hli : LinearIndependent
        (IntermediateField.adjoin ℚ ({zeta n ^ m} : Set ℂ))
        (fun i : Fin m => zeta n ^ (i : ℕ)) :=
      radical_cyclotomic_powers_linearIndependent n hn
    apply fiberSeparates_of_power_linearIndependent
      (IntermediateField.adjoin ℚ ({zeta n ^ m} : Set ℂ))
      (zeta n) m (nthRoots n) f hli
    intro z hz
    obtain ⟨w, hw, hzw⟩ := rootCosetIndex_spec n hn z hz
    refine ⟨⟨w, nthRoots_subset_radical_cyclotomic n hn hw⟩, ?_⟩
    simpa only [f, mul_comm] using hzw
  · intro i
    ext z
    constructor
    · rintro ⟨hz, hfi⟩
      obtain ⟨w, hw, hzw⟩ := rootCosetIndex_spec n hn z hz
      refine ⟨w, hw, ?_⟩
      simpa only [u, Units.val_mk0, f, hfi] using hzw.symm
    · rintro ⟨w, hw, rfl⟩
      change (u i : ℂ) * w ∈ nthRoots n ∧ f ((u i : ℂ) * w) = i
      have hz : zeta n ^ (i : ℕ) * w ∈ nthRoots n :=
        radical_coset_mem_nthRoots n hn i w hw
      constructor
      · simpa only [u, Units.val_mk0] using hz
      · have heq : (u i : ℂ) * w = zeta n ^ (i : ℕ) * w := rfl
        exact rootCosetIndex_eq n hn _ i w hw hz heq

/-- The stronger character-gluing form of cyclotomic coset separation. -/
theorem rootCoset_characters_glue (n : ℕ) (hn : 0 < n) :
    FiberCharactersGlue (nthRoots n) (rootCosetIndex n hn) := by
  let K := IntermediateField.adjoin ℚ
    ({zeta n ^ (n / radical n)} : Set ℂ)
  let m := n / radical n
  intro χi
  have hli : LinearIndependent K (fun i : Fin m => zeta n ^ (i : ℕ)) :=
    radical_cyclotomic_powers_linearIndependent n hn
  let σ (i : Fin m) : ℂ →+ ℂ := {
    toFun := fun w => zeta n ^ (i : ℕ) * w
    map_zero' := by simp
    map_add' := by intros; simp [mul_add]
  }
  let ψ (i : Fin m) : AddChar ℂ Circle :=
    (χi i).compAddMonoidHom (σ i)
  obtain ⟨χ, hχ⟩ :=
    glue_characters_over_field K m (fun i => zeta n ^ (i : ℕ)) hli ψ
  refine ⟨χ, ?_⟩
  intro z hz
  obtain ⟨w, hw, hzw⟩ := rootCosetIndex_spec n hn z hz
  let c : K := ⟨w, nthRoots_subset_radical_cyclotomic n hn hw⟩
  have h := hχ (rootCosetIndex n hn z) c
  change χ ((c : ℂ) * zeta n ^ (rootCosetIndex n hn z : ℕ)) =
    χi (rootCosetIndex n hn z)
      (zeta n ^ (rootCosetIndex n hn z : ℕ) * (c : ℂ)) at h
  have hzw' : z = w * zeta n ^ (rootCosetIndex n hn z : ℕ) := by
    simpa only [mul_comm] using hzw
  simpa only [c, mul_comm, ← hzw'] using h

theorem rootCoset_fiber_eq (n : ℕ) (hn : 0 < n)
    (i : Fin (n / radical n)) :
    {z | z ∈ nthRoots n ∧ rootCosetIndex n hn z = i} =
      ((fun w : ℂ => zeta n ^ (i : ℕ) * w) '' nthRoots (radical n)) := by
  ext z
  constructor
  · rintro ⟨hz, hindex⟩
    obtain ⟨w, hw, hzw⟩ := rootCosetIndex_spec n hn z hz
    refine ⟨w, hw, ?_⟩
    simpa only [hindex] using hzw.symm
  · rintro ⟨w, hw, rfl⟩
    have hz := radical_coset_mem_nthRoots n hn i w hw
    exact ⟨hz, rootCosetIndex_eq n hn _ i w hw hz rfl⟩

/-- The positive-real Sidon bound extends from radical order to arbitrary
order with no loss of constant. -/
theorem positiveRealBound_of_radical (n : ℕ) (hn : 0 < n) (K : ℝ)
    (h : PositiveRealBound (nthRoots (radical n)) K) :
    PositiveRealBound (nthRoots n) K := by
  apply positiveRealBound_of_fibers (nthRoots n) (rootCosetIndex n hn) K
  · intro i
    rw [rootCoset_fiber_eq n hn i]
    let u : ℂˣ := Units.mk0 (zeta n ^ (i : ℕ))
      (pow_ne_zero _ (Complex.exp_ne_zero _))
    exact positiveRealBound_scalar u (nthRoots (radical n)) K h
  · exact rootCoset_characters_glue n hn

theorem hasCyclotomicCosetDecomposition_squarefree {n : ℕ}
    (hn : Squarefree n) : HasCyclotomicCosetDecomposition n := by
  refine ⟨1, fun _ => 0, fun _ => 1, ?_, ?_⟩
  · intro U V _ _ hsum i
    have : i = 0 := Subsingleton.elim _ _
    subst i
    simpa using hsum
  · intro i
    have : i = 0 := Subsingleton.elim _ _
    subst i
    ext z
    simp [nthRoots, radical, Nat.prod_primeFactors_of_squarefree hn]

private theorem commonOrder (A : Finset ℂ) :
    (↑A : Set ℂ) ⊆ rootsOfUnity →
    ∃ n : ℕ, 0 < n ∧ ∀ z ∈ A, z ^ n = 1 := by
  classical
  induction A using Finset.induction_on with
  | empty =>
      intro _
      exact ⟨1, by omega, by simp⟩
  | @insert a S ha ih =>
      intro hA
      have haRoot : IsOfFinOrder a := hA (by simp)
      obtain ⟨m, hmpos, hm⟩ := haRoot.exists_pow_eq_one
      have hS : (↑S : Set ℂ) ⊆ rootsOfUnity := by
        intro z hz
        exact hA (by simp [hz])
      obtain ⟨n, hnpos, hn⟩ := ih hS
      refine ⟨m * n, mul_pos hmpos hnpos, ?_⟩
      intro z hz
      rcases Finset.mem_insert.mp hz with rfl | hz
      · rw [pow_mul, hm, one_pow]
      · rw [mul_comm m n, pow_mul, hn z hz, one_pow]

private theorem commonOddOrder (A : Finset ℂ) :
    (↑A : Set ℂ) ⊆ oddRootsOfUnity →
    ∃ n : ℕ, 0 < n ∧ Odd n ∧ ∀ z ∈ A, z ^ n = 1 := by
  classical
  induction A using Finset.induction_on with
  | empty =>
      intro _
      exact ⟨1, by omega, by norm_num, by simp⟩
  | @insert a S ha ih =>
      intro hA
      have haRoot : a ∈ oddRootsOfUnity := hA (by simp)
      obtain ⟨m, hmpos, hmodd, hm⟩ := haRoot
      have hS : (↑S : Set ℂ) ⊆ oddRootsOfUnity := by
        intro z hz
        exact hA (by simp [hz])
      obtain ⟨n, hnpos, hnodd, hn⟩ := ih hS
      refine ⟨m * n, mul_pos hmpos hnpos, hmodd.mul hnodd, ?_⟩
      intro z hz
      rcases Finset.mem_insert.mp hz with rfl | hz
      · rw [pow_mul, hm, one_pow]
      · rw [mul_comm m n, pow_mul, hn z hz, one_pow]

/-- The positive-real bound transfers from odd squarefree orders to every
odd-order root of unity. -/
theorem positiveRealBound_oddRoots_of_squarefree (K : ℝ)
    (h : ∀ r : ℕ, 0 < r → Odd r → Squarefree r →
      PositiveRealBound (nthRoots r) K) :
    PositiveRealBound oddRootsOfUnity K := by
  intro A hA c
  obtain ⟨n, hn, hnodd, hAn⟩ := commonOddOrder A hA
  have hrOdd : Odd (radical n) := hnodd.of_dvd_nat (radical_dvd n)
  apply positiveRealBound_of_radical n hn K
    (h (radical n) (radical_pos n) hrOdd (radical_squarefree n)) A
  intro z hz
  exact hAn z hz

/-- For odd `m`, the `(2*m)`-th roots are two antipodal copies of the
`m`-th roots. -/
theorem nthRoots_two_mul_odd (m : ℕ) (hm : Odd m) :
    nthRoots (2 * m) = nthRoots m ∪
      ((fun z : ℂ => -z) '' nthRoots m) := by
  ext z
  constructor
  · intro hz
    have hz2 : (z ^ m) ^ 2 = 1 := by
      simpa only [nthRoots, Set.mem_setOf_eq, ← pow_mul, mul_comm] using hz
    rcases sq_eq_one_iff.mp hz2 with hz1 | hzNeg
    · exact Or.inl hz1
    · right
      refine ⟨-z, ?_, by simp⟩
      change (-z) ^ m = 1
      rw [hm.neg_pow, hzNeg]
      simp
  · rintro (hz | ⟨w, hw, rfl⟩)
    · change z ^ (2 * m) = 1
      rw [mul_comm, pow_mul, hz, one_pow]
    · change (-w) ^ (2 * m) = 1
      rw [mul_comm, pow_mul, hm.neg_pow, hw]
      norm_num

theorem squarefree_even_half_odd {r : ℕ}
    (hr : Squarefree r) (he : Even r) : Odd (r / 2) := by
  by_contra hodd
  have hhalf : Even (r / 2) := Nat.not_odd_iff_even.mp hodd
  obtain ⟨j, hj⟩ := hhalf
  have hrEq : 2 * (r / 2) = r := Nat.mul_div_cancel' (even_iff_two_dvd.mp he)
  have hfour : 2 * 2 ∣ r := by
    refine ⟨j, ?_⟩
    omega
  exact (Nat.squarefree_iff_prime_squarefree.mp hr 2 Nat.prime_two) hfour

/-- A uniform extraction constant on odd squarefree orders gives one on all
squarefree orders, with at most a factor of two. -/
theorem squarefree_extraction_of_odd_squarefree (k : ℕ)
    (h : ∀ m : ℕ, 0 < m → Odd m → Squarefree m →
      UniformExtraction (nthRoots m) k) :
    ∀ r : ℕ, 0 < r → Squarefree r →
      UniformExtraction (nthRoots r) (2 * k) := by
  intro r hrpos hr
  by_cases hodd : Odd r
  · exact uniformExtraction_of_le (nthRoots r) (by omega) (h r hrpos hodd hr)
  · have he : Even r := Nat.not_odd_iff_even.mp hodd
    let m := r / 2
    have hmOdd : Odd m := squarefree_even_half_odd hr he
    have hrEq : 2 * m = r := Nat.mul_div_cancel' (even_iff_two_dvd.mp he)
    have hmPos : 0 < m := by omega
    have hmSq : Squarefree m := hr.squarefree_of_dvd (by
      refine ⟨2, ?_⟩
      simpa [m, mul_comm] using hrEq.symm)
    have hmExtract := h m hmPos hmOdd hmSq
    have hneg : UniformExtraction ((fun z : ℂ => -z) '' nthRoots m) k := by
      simpa using uniformExtraction_image (AddEquiv.neg ℂ) (nthRoots m) k hmExtract
    rw [← hrEq, nthRoots_two_mul_odd m hmOdd]
    simpa [two_mul] using uniformExtraction_union (nthRoots m)
      ((fun z : ℂ => -z) '' nthRoots m) k k hmExtract hneg

theorem uniformExtraction_iff_finiteOrders (k : ℕ) :
    UniformExtraction rootsOfUnity k ↔
      ∀ n : ℕ, 0 < n → UniformExtraction (nthRoots n) k := by
  constructor
  · intro h n hn A hA
    apply h A
    intro z hz
    exact isOfFinOrder_iff_pow_eq_one.mpr ⟨n, hn, hA hz⟩
  · intro h A hA
    obtain ⟨n, hnpos, hn⟩ := commonOrder A hA
    apply h n hnpos A
    intro z hz
    exact hn z hz

/-- The analytic formulation on all roots is equivalent to one constant that
works for every positive root order. -/
theorem analyticSidon_iff_finiteOrders :
    AnalyticSidon ↔
      ∃ K : ℝ, 0 < K ∧
        ∀ n : ℕ, 0 < n → ∀ A : Finset ℂ,
          (↑A : Set ℂ) ⊆ nthRoots n → ∀ c : ℂ → ℂ,
            ∃ χ : AddChar ℂ Circle,
              (∑ z ∈ A, ‖c z‖) ≤ K * ‖∑ z ∈ A, c z * (χ z : ℂ)‖ := by
  constructor
  · rintro ⟨K, hK, h⟩
    refine ⟨K, hK, ?_⟩
    intro n hn A hA c
    apply h A
    intro z hz
    exact isOfFinOrder_iff_pow_eq_one.mpr ⟨n, hn, hA hz⟩
  · rintro ⟨K, hK, h⟩
    refine ⟨K, hK, ?_⟩
    intro A hA c
    obtain ⟨n, hn, hAn⟩ := commonOrder A hA
    apply h n hn A
    intro z hz
    exact hAn z hz

theorem statement_of_finiteOrders
    (h : ∃ k : ℕ, 0 < k ∧
      ∀ n : ℕ, 0 < n → UniformExtraction (nthRoots n) k) : statement := by
  obtain ⟨k, hk, horders⟩ := h
  exact ⟨k, hk, (uniformExtraction_iff_finiteOrders k).mpr horders⟩

theorem statement_iff_finiteOrders :
    statement ↔ ∃ k : ℕ, 0 < k ∧
      ∀ n : ℕ, 0 < n → UniformExtraction (nthRoots n) k := by
  constructor
  · rintro ⟨k, hk, h⟩
    exact ⟨k, hk, (uniformExtraction_iff_finiteOrders k).mp h⟩
  · exact statement_of_finiteOrders

theorem statement_of_radical_extraction_and_cosets
    (hExtract : ∃ k : ℕ, 0 < k ∧
      ∀ n : ℕ, 0 < n → UniformExtraction (nthRoots (radical n)) k)
    (hCosets : ∀ n : ℕ, 0 < n → HasCyclotomicCosetDecomposition n) :
    statement := by
  obtain ⟨k, hk, hSquarefree⟩ := hExtract
  apply statement_of_finiteOrders
  refine ⟨k, hk, ?_⟩
  intro n hn
  obtain ⟨m, f, u, hsep, hfiber⟩ := hCosets n hn
  apply uniformExtraction_of_fibers (nthRoots n) f k hsep
  intro i
  rw [hfiber i]
  exact uniformExtraction_scalar (u i) (nthRoots (radical n)) k (hSquarefree n hn)

/-- Once a uniform extraction bound is known for squarefree root orders, it
extends to roots of every order with the same denominator. -/
theorem statement_of_radical_extraction
    (hExtract : ∃ k : ℕ, 0 < k ∧
      ∀ n : ℕ, 0 < n → UniformExtraction (nthRoots (radical n)) k) :
    statement :=
  statement_of_radical_extraction_and_cosets hExtract hasCyclotomicCosetDecomposition

/-- The remaining combinatorial premise can be stated directly for positive
squarefree orders. -/
theorem statement_of_squarefree_extraction
    (hExtract : ∃ k : ℕ, 0 < k ∧
      ∀ r : ℕ, 0 < r → Squarefree r → UniformExtraction (nthRoots r) k) :
    statement := by
  obtain ⟨k, hk, h⟩ := hExtract
  apply statement_of_radical_extraction
  exact ⟨k, hk, fun n _ => h (radical n) (radical_pos n) (radical_squarefree n)⟩

/-- Proportional dissociation of all roots of unity is equivalent to one
uniform extraction bound on the squarefree-order grids. -/
theorem statement_iff_squarefree_extraction :
    statement ↔ ∃ k : ℕ, 0 < k ∧
      ∀ r : ℕ, 0 < r → Squarefree r → UniformExtraction (nthRoots r) k := by
  constructor
  · rintro ⟨k, hk, h⟩
    exact ⟨k, hk, fun r hr _ => (uniformExtraction_iff_finiteOrders k).mp h r hr⟩
  · exact statement_of_squarefree_extraction

/-- The full proportional-dissociation assertion is reduced to uniform
extraction on odd squarefree root grids. The factor-two loss absorbs the
antipodal prime-two coordinate. -/
theorem statement_iff_odd_squarefree_extraction :
    statement ↔ ∃ k : ℕ, 0 < k ∧
      ∀ m : ℕ, 0 < m → Odd m → Squarefree m →
        UniformExtraction (nthRoots m) k := by
  constructor
  · intro h
    obtain ⟨k, hk, hsq⟩ := statement_iff_squarefree_extraction.mp h
    exact ⟨k, hk, fun m hm _ hmsq => hsq m hm hmsq⟩
  · rintro ⟨k, hk, hodd⟩
    apply statement_of_squarefree_extraction
    exact ⟨2 * k, by omega, squarefree_extraction_of_odd_squarefree k hodd⟩

end Erdos.Research.Problem774

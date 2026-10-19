import Erdos.RootsOfUnitySidon.TensorPhaseLattice
import Erdos.RootsOfUnitySidon.FiniteCharacterAverage

/-!
# Separating small-prime tensor columns

Distinct columns in a finite tensor of simplex factors have distinct coordinate
supports when every simplex has at least three columns. A two-coordinate
determinant consequently gives a linear functional vanishing on one complete
column slice but not on a point of another slice. Composing this functional
with a circle-valued character supplies the pointwise character separator
needed by finite character averaging. The
`ComplexTensor` construction is an abstract additive model; it cannot embed
as an ℂ-linear space into ℂ. For actual root frequencies, the relevant
coefficient space is `FieldTensor K` for the tail cyclotomic field `K`.
Constructing its injective additive embedding into ℂ requires a separate
linear-disjointness argument.
-/

namespace Erdos.Research.Problem774.SmallPrimeAnalytic

open Erdos.Research.Problem774.SimplexTorus
open Erdos.Research.Problem774.TensorPhaseLattice

private theorem lastColumn_apply (n : ℕ) (a : Fin n) :
    lastColumn n a = -1 := by
  classical
  simp [lastColumn, basis, Pi.single_apply]

private theorem basis_apply_same (n : ℕ) (i : Fin n) : basis n i i = 1 := by
  simp [basis]

private theorem basis_apply_ne (n : ℕ) {i a : Fin n} (hia : i ≠ a) :
    basis n i a = 0 := by
  simp [basis, hia]

private theorem column_nonzero (n : ℕ) (hn : 0 < n)
    (j : Fin (n + 1)) : ∃ a : Fin n, column n j a ≠ 0 := by
  induction j using Fin.lastCases with
  | last =>
      refine ⟨⟨0, hn⟩, ?_⟩
      simp [lastColumn_apply]
  | cast i =>
      exact ⟨i, by simp [basis_apply_same]⟩

/-- Two different simplex columns have different coordinate supports. -/
theorem column_support_mismatch (n : ℕ) (hn : 2 ≤ n)
    {j k : Fin (n + 1)} (hjk : j ≠ k) :
    ∃ a : Fin n,
      (column n j a = 0 ∧ column n k a ≠ 0) ∨
      (column n j a ≠ 0 ∧ column n k a = 0) := by
  haveI : Nontrivial (Fin n) := Fin.nontrivial_iff_two_le.mpr hn
  induction j using Fin.lastCases with
  | last =>
      induction k using Fin.lastCases with
      | last => exact False.elim (hjk rfl)
      | cast i =>
          obtain ⟨a, hai⟩ : ∃ a : Fin n, a ≠ i := exists_ne i
          refine ⟨a, Or.inr ⟨?_, ?_⟩⟩
          · simp [lastColumn_apply]
          · simp [basis_apply_ne n hai.symm]
  | cast i =>
      induction k using Fin.lastCases with
      | last =>
          obtain ⟨a, hai⟩ : ∃ a : Fin n, a ≠ i := exists_ne i
          refine ⟨a, Or.inl ⟨?_, ?_⟩⟩
          · simp [basis_apply_ne n hai.symm]
          · simp [lastColumn_apply]
      | cast k =>
          have hik : i ≠ k := by
            intro h
            exact hjk (congrArg Fin.castSucc h)
          refine ⟨i, Or.inr ⟨?_, ?_⟩⟩
          · simp [basis_apply_same]
          · simp [basis_apply_ne n hik.symm]

theorem tensorColumn_nonzero {ι : Type*} [Fintype ι]
    (n : ι → ℕ) (hn : ∀ i, 0 < n i)
    (j : TensorIndex ι n) :
    ∃ a : TensorBasis ι n, tensorColumn n j a ≠ 0 := by
  classical
  let a : TensorBasis ι n := fun i => (column_nonzero (n i) (hn i) (j i)).choose
  refine ⟨a, ?_⟩
  unfold tensorColumn
  apply Finset.prod_ne_zero_iff.mpr
  intro i _
  exact (column_nonzero (n i) (hn i) (j i)).choose_spec

/-- Product-simplex columns have different coordinate supports. This includes
the empty product, where the premise `j ≠ k` is impossible. -/
theorem tensorColumn_support_mismatch {ι : Type*} [Fintype ι]
    (n : ι → ℕ) (hn : ∀ i, 2 ≤ n i)
    {j k : TensorIndex ι n} (hjk : j ≠ k) :
    ∃ a : TensorBasis ι n,
      (tensorColumn n j a = 0 ∧ tensorColumn n k a ≠ 0) ∨
      (tensorColumn n j a ≠ 0 ∧ tensorColumn n k a = 0) := by
  classical
  have hnPos (h : ι) : 0 < n h := lt_of_lt_of_le (by omega : 0 < 2) (hn h)
  obtain ⟨i, hi⟩ : ∃ i : ι, j i ≠ k i := by
    by_contra h
    push Not at h
    exact hjk (funext h)
  obtain ⟨ai, hlocal⟩ := column_support_mismatch (n i) (hn i) hi
  rcases hlocal with hlocal | hlocal
  · let a0 : TensorBasis ι n :=
      fun h => (column_nonzero (n h) (hnPos h) (k h)).choose
    let a : TensorBasis ι n := Function.update a0 i ai
    refine ⟨a, Or.inl ⟨?_, ?_⟩⟩
    · unfold tensorColumn
      apply Finset.prod_eq_zero (Finset.mem_univ i)
      simpa [a] using hlocal.1
    · unfold tensorColumn
      apply Finset.prod_ne_zero_iff.mpr
      intro h _
      by_cases hhi : h = i
      · subst h
        simpa [a] using hlocal.2
      · simpa [a, hhi] using
          (column_nonzero (n h) (hnPos h) (k h)).choose_spec
  · let a0 : TensorBasis ι n :=
      fun h => (column_nonzero (n h) (hnPos h) (j h)).choose
    let a : TensorBasis ι n := Function.update a0 i ai
    refine ⟨a, Or.inr ⟨?_, ?_⟩⟩
    · unfold tensorColumn
      apply Finset.prod_ne_zero_iff.mpr
      intro h _
      by_cases hhi : h = i
      · subst h
        simpa [a] using hlocal.1
      · simpa [a, hhi] using
          (column_nonzero (n h) (hnPos h) (j h)).choose_spec
    · unfold tensorColumn
      apply Finset.prod_eq_zero (Finset.mem_univ i)
      simpa [a] using hlocal.2

/-- Two distinct tensor columns admit a nonzero two-coordinate determinant. -/
theorem tensorColumn_det_witness {ι : Type*} [Fintype ι]
    (n : ι → ℕ) (hn : ∀ i, 2 ≤ n i)
    {j k : TensorIndex ι n} (hjk : j ≠ k) :
    ∃ a b : TensorBasis ι n,
      tensorColumn n j a * tensorColumn n k b -
        tensorColumn n j b * tensorColumn n k a ≠ 0 := by
  have hnPos (i : ι) : 0 < n i := lt_of_lt_of_le (by omega : 0 < 2) (hn i)
  obtain ⟨a, ha | ha⟩ := tensorColumn_support_mismatch n hn hjk
  · obtain ⟨b, hb⟩ := tensorColumn_nonzero n hnPos j
    refine ⟨b, a, ?_⟩
    simp [ha.1, hb, ha.2]
  · obtain ⟨b, hb⟩ := tensorColumn_nonzero n hnPos k
    refine ⟨a, b, ?_⟩
    simp [ha.2, ha.1, hb]

/-- Complex coordinate space for a free tensor frequency group. -/
abbrev ComplexTensor (ι : Type*) (n : ι → ℕ) := TensorBasis ι n → ℂ

/-- A tensor simplex column multiplied by a complex tail frequency. -/
def tensorFrequency {ι : Type*} [Fintype ι] (n : ι → ℕ)
    (j : TensorIndex ι n) (z : ℂ) : ComplexTensor ι n :=
  fun a => (tensorColumn n j a : ℂ) * z

/-- A two-coordinate functional on the tensor coordinate space. -/
def determinantFunctional {ι : Type*} (n : ι → ℕ)
    (u : TensorLattice ι n) (a b : TensorBasis ι n) :
    ComplexTensor ι n →+ ℂ where
  toFun x := (u a : ℂ) * x b - (u b : ℂ) * x a
  map_zero' := by simp
  map_add' x y := by
    simp only [Pi.add_apply]
    ring

theorem determinantFunctional_own_slice {ι : Type*} [Fintype ι]
    (n : ι → ℕ) (j : TensorIndex ι n)
    (a b : TensorBasis ι n) (z : ℂ) :
    determinantFunctional n (tensorColumn n j) a b (tensorFrequency n j z) = 0 := by
  simp [determinantFunctional, tensorFrequency]
  ring

theorem determinantFunctional_other_slice {ι : Type*} [Fintype ι]
    (n : ι → ℕ) (hn : ∀ i, 2 ≤ n i)
    {j k : TensorIndex ι n} (hjk : j ≠ k) (z : ℂ) (hz : z ≠ 0) :
    ∃ a b : TensorBasis ι n,
      determinantFunctional n (tensorColumn n j) a b (tensorFrequency n k z) ≠ 0 := by
  obtain ⟨a, b, hab⟩ := tensorColumn_det_witness n hn hjk
  refine ⟨a, b, ?_⟩
  have hcast : ((tensorColumn n j a * tensorColumn n k b -
      tensorColumn n j b * tensorColumn n k a : ℤ) : ℂ) ≠ 0 := by
    exact_mod_cast hab
  change (tensorColumn n j a : ℂ) * ((tensorColumn n k b : ℂ) * z) -
    (tensorColumn n j b : ℂ) * ((tensorColumn n k a : ℂ) * z) ≠ 0
  calc
    (tensorColumn n j a : ℂ) * ((tensorColumn n k b : ℂ) * z) -
        (tensorColumn n j b : ℂ) * ((tensorColumn n k a : ℂ) * z) =
        ((tensorColumn n j a * tensorColumn n k b -
          tensorColumn n j b * tensorColumn n k a : ℤ) : ℂ) * z := by
            push_cast
            ring
    _ ≠ 0 := mul_ne_zero hcast hz

/-- A circle-valued character trivial on one complete simplex-tensor slice
can flip any chosen nonzero frequency in another slice. -/
theorem exists_separator_character {ι : Type*} [Fintype ι]
    (n : ι → ℕ) (hn : ∀ i, 2 ≤ n i)
    {j k : TensorIndex ι n} (hjk : j ≠ k) (z : ℂ) (hz : z ≠ 0) :
    ∃ ψ : AddChar (ComplexTensor ι n) Circle,
      (∀ w : ℂ, ψ (tensorFrequency n j w) = 1) ∧
      ψ (tensorFrequency n k z) = -1 := by
  obtain ⟨a, b, hab⟩ := determinantFunctional_other_slice n hn hjk z hz
  obtain ⟨φ, hφ⟩ := exists_character_eq_neg_one hab
  refine ⟨φ.compAddMonoidHom (determinantFunctional n (tensorColumn n j) a b), ?_, ?_⟩
  · intro w
    simp [determinantFunctional_own_slice]
  · simpa using hφ

/-- Tensor coordinates with coefficients in the tail cyclotomic field. This
is the coefficient space that can be mapped injectively to actual roots after
the needed cyclotomic linear-disjointness proof. -/
abbrev FieldTensor (K : IntermediateField ℚ ℂ) (ι : Type*) (n : ι → ℕ) :=
  TensorBasis ι n → K

/-- Coordinatewise inclusion of a tail-field tensor into the abstract complex
tensor space. -/
def fieldTensorInclusion (K : IntermediateField ℚ ℂ) (ι : Type*) (n : ι → ℕ) :
    FieldTensor K ι n →+ ComplexTensor ι n where
  toFun x := fun a => (x a : ℂ)
  map_zero' := by ext a; simp
  map_add' x y := by ext a; simp

/-- A small-prime tensor column multiplied by a tail-field frequency. -/
noncomputable def fieldTensorFrequency {ι : Type*} [Fintype ι]
    (K : IntermediateField ℚ ℂ) (n : ι → ℕ)
    (j : TensorIndex ι n) (z : K) : FieldTensor K ι n :=
  fun a => (tensorColumn n j a : K) * z

theorem fieldTensorInclusion_frequency {ι : Type*} [Fintype ι]
    (K : IntermediateField ℚ ℂ) (n : ι → ℕ)
    (j : TensorIndex ι n) (z : K) :
    fieldTensorInclusion K ι n (fieldTensorFrequency K n j z) =
      tensorFrequency n j (z : ℂ) := by
  ext a
  simp [fieldTensorInclusion, fieldTensorFrequency, tensorFrequency]

/-- The separator also lives on the correctly restricted tail-field tensor
space, by restriction from the abstract complex tensor. -/
theorem exists_separator_character_field {ι : Type*} [Fintype ι]
    (K : IntermediateField ℚ ℂ) (n : ι → ℕ) (hn : ∀ i, 2 ≤ n i)
    {j k : TensorIndex ι n} (hjk : j ≠ k) (z : K) (hz : z ≠ 0) :
    ∃ ψ : AddChar (FieldTensor K ι n) Circle,
      (∀ w : K, ψ (fieldTensorFrequency K n j w) = 1) ∧
      ψ (fieldTensorFrequency K n k z) = -1 := by
  have hz' : (z : ℂ) ≠ 0 := by exact_mod_cast hz
  obtain ⟨φ, hφj, hφk⟩ :=
    exists_separator_character n hn hjk (z : ℂ) hz'
  refine ⟨φ.compAddMonoidHom (fieldTensorInclusion K ι n), ?_, ?_⟩
  · intro w
    rw [AddChar.compAddMonoidHom_apply, fieldTensorInclusion_frequency]
    exact hφj w
  · rw [AddChar.compAddMonoidHom_apply, fieldTensorInclusion_frequency]
    exact hφk

private theorem character_list_twist_sum {G : Type*} [AddCommGroup G]
    (L : List (AddChar G Circle)) (ψ : AddChar G Circle) (w : G) :
    ((L.map fun χ => χ * ψ).map fun χ => (χ w : ℂ)).sum =
      (L.map fun χ => (χ w : ℂ)).sum * (ψ w : ℂ) := by
  simpa only [List.map_map, Function.comp_def, AddChar.mul_apply, Circle.coe_mul] using
    (List.sum_map_mul_right L (fun χ : AddChar G Circle => (χ w : ℂ)) (ψ w : ℂ))

/-- A finite equal-weight character list remains trivial on a selected entire
tail-field slice while its average annihilates a prescribed finite collection
of nonzero points in all other slices. -/
theorem exists_relative_character_list_field {ι : Type*} [Fintype ι]
    (K : IntermediateField ℚ ℂ) (n : ι → ℕ) (hn : ∀ i, 2 ≤ n i)
    (j : TensorIndex ι n) (F : Finset (TensorIndex ι n × K))
    (hF : ∀ p ∈ F, p.1 ≠ j ∧ p.2 ≠ 0) :
    ∃ L : List (AddChar (FieldTensor K ι n) Circle),
      L ≠ [] ∧
      (∀ ψ ∈ L, ∀ w : K, ψ (fieldTensorFrequency K n j w) = 1) ∧
      (∀ p ∈ F,
        (L.map fun ψ => (ψ (fieldTensorFrequency K n p.1 p.2) : ℂ)).sum = 0) := by
  classical
  induction F using Finset.induction_on with
  | empty =>
      refine ⟨[1], by simp, ?_, ?_⟩
      · simp
      · simp
  | @insert p F hp ih =>
      have hp' : p.1 ≠ j ∧ p.2 ≠ 0 := hF p (Finset.mem_insert_self _ _)
      have hF' : ∀ q ∈ F, q.1 ≠ j ∧ q.2 ≠ 0 := by
        intro q hq
        exact hF q (Finset.mem_insert_of_mem hq)
      obtain ⟨L, hL, htrivial, hvanish⟩ := ih hF'
      obtain ⟨ψ, hψtrivial, hψp⟩ :=
        exists_separator_character_field K n hn hp'.1.symm p.2 hp'.2
      let L' := L ++ L.map (fun χ => χ * ψ)
      have hsum (w : FieldTensor K ι n) :
          (L'.map fun χ => (χ w : ℂ)).sum =
            (L.map fun χ => (χ w : ℂ)).sum * (1 + (ψ w : ℂ)) := by
        simp only [L', List.map_append, List.sum_append, character_list_twist_sum]
        ring
      refine ⟨L', ?_, ?_, ?_⟩
      · intro hnil
        exact hL (List.append_eq_nil_iff.mp hnil).1
      · intro χ hχ w
        rcases List.mem_append.mp hχ with hχL | hχL
        · exact htrivial χ hχL w
        · obtain ⟨χ₀, hχ₀, rfl⟩ := List.mem_map.mp hχL
          simp [AddChar.mul_apply, htrivial χ₀ hχ₀ w, hψtrivial w]
      · intro q hq
        rcases Finset.mem_insert.mp hq with rfl | hqF
        · rw [hsum, hψp]
          simp
        · rw [hsum, hvanish q hqF]
          simp


end Erdos.Research.Problem774.SmallPrimeAnalytic

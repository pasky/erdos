import Erdos.RootsOfUnitySidon.SimplexGramSchmidt
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic

/-!
# Gram trace of finite tensor products of anchored simplices

The Euclidean vector associated to a tensor index is the pointwise product
of the one-factor orthogonalized anchored vectors. Dot products factor over
coordinates, so distinct tensor vectors are orthogonal. Summing their
squared lengths factors as the product of the one-factor harmonic totals.

This finite identity is the Gram trace needed when averaging a tensor
rounding construction over permutations of its simplex coordinates.
-/

namespace Erdos.Research.Problem774.TensorGramTrace

open Finset Erdos.Research.Problem774.SimplexGramSchmidt

/-- Indices of the non-last columns in each simplex factor. -/
abbrev TensorBasis (ι : Type*) (n : ι → ℕ) := ∀ i : ι, Fin (n i)

/-- Indices of the full columns in each simplex factor. -/
abbrev TensorVertex (ι : Type*) (n : ι → ℕ) := ∀ i : ι, Fin (n i + 1)

/-- The anchored basis column `e_a - e_last` in one factor. -/
def anchoredBasis (n : ℕ) (a : Fin n) (u : Fin (n + 1)) : ℝ :=
  if u = a.castSucc then 1 else if u = Fin.last n then -1 else 0

/-- Expansion of any anchored vector in the anchored basis columns. -/
theorem anchoredVector_eq_sum_basis (n : ℕ) (x : Fin n → ℝ)
    (u : Fin (n + 1)) :
    anchoredVector n x u = ∑ a : Fin n, x a * anchoredBasis n a u := by
  induction u using Fin.lastCases with
  | last =>
      have hne (a : Fin n) : Fin.last n ≠ a.castSucc :=
        ne_of_gt a.castSucc_lt_last
      simp [anchoredVector, anchoredBasis, hne, ← Finset.sum_neg_distrib]
  | cast v =>
      simp [anchoredVector, anchoredBasis]

/-- The pure tensor of the explicit orthogonalized anchored vectors. -/
noncomputable def orthogonalTensor {ι : Type*} [Fintype ι]
    (n : ι → ℕ) (j : TensorBasis ι n) (u : TensorVertex ι n) : ℝ :=
  ∏ i : ι, anchoredVector (n i) (orthogonalCoeff (n i) (j i)) (u i)

/-- The integer anchored tensor basis, viewed in the real vertex grid. -/
def tensorAnchoredBasis {ι : Type*} [Fintype ι]
    (n : ι → ℕ) (a : TensorBasis ι n) (u : TensorVertex ι n) : ℝ :=
  ∏ i : ι, anchoredBasis (n i) (a i) (u i)

/-- Matrix coefficient of the tensor orthogonalization in the anchored basis. -/
noncomputable def tensorTransform {ι : Type*} [Fintype ι]
    (n : ι → ℕ) (j a : TensorBasis ι n) : ℝ :=
  ∏ i : ι, orthogonalCoeff (n i) (j i) (a i)

/-- Every diagonal entry of the tensor basis change is one. -/
theorem tensorTransform_diag {ι : Type*} [Fintype ι]
    (n : ι → ℕ) (j : TensorBasis ι n) :
    tensorTransform n j j = 1 := by
  simp [tensorTransform, coeff_at]

/-- The tensor basis change is triangular for the componentwise order. -/
theorem tensorTransform_zero_of_not_le {ι : Type*}
    [Fintype ι] (n : ι → ℕ) (j a : TensorBasis ι n)
    (h : ¬ ∀ i : ι, a i ≤ j i) : tensorTransform n j a = 0 := by
  classical
  obtain ⟨i, hi⟩ := not_forall.mp h
  have hlt : j i < a i := lt_of_not_ge hi
  exact prod_eq_zero (mem_univ i) (coeff_after (n i) hlt)

/-- Each orthogonal tensor vector is a unitriangular linear combination
of the anchored tensor basis. -/
theorem orthogonalTensor_eq_sum_anchoredBasis {ι : Type*}
    [Fintype ι] [DecidableEq ι] (n : ι → ℕ)
    (j : TensorBasis ι n) (u : TensorVertex ι n) :
    orthogonalTensor n j u =
      ∑ a : TensorBasis ι n,
        tensorTransform n j a * tensorAnchoredBasis n a u := by
  classical
  let f : ∀ i : ι, Fin (n i) → ℝ := fun i a =>
    orthogonalCoeff (n i) (j i) a * anchoredBasis (n i) a (u i)
  calc
    orthogonalTensor n j u = ∏ i : ι, ∑ a : Fin (n i), f i a := by
      unfold orthogonalTensor
      apply prod_congr rfl
      intro i _
      exact anchoredVector_eq_sum_basis (n i) (orthogonalCoeff (n i) (j i)) (u i)
    _ = ∑ a : TensorBasis ι n, ∏ i : ι, f i (a i) := Fintype.prod_sum f
    _ = ∑ a : TensorBasis ι n,
          tensorTransform n j a * tensorAnchoredBasis n a u := by
      apply sum_congr rfl
      intro a _
      simp only [f, tensorTransform, tensorAnchoredBasis, prod_mul_distrib]

/-- The dot product of two tensor vectors is the product of the one-factor
anchored Gram forms. -/
theorem tensor_dot_factor {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) (j k : TensorBasis ι n) :
    (∑ u : TensorVertex ι n, orthogonalTensor n j u * orthogonalTensor n k u) =
      ∏ i : ι,
        anchoredGram (orthogonalCoeff (n i) (j i))
          (orthogonalCoeff (n i) (k i)) := by
  classical
  let f : ∀ i : ι, Fin (n i + 1) → ℝ := fun i v =>
    anchoredVector (n i) (orthogonalCoeff (n i) (j i)) v *
      anchoredVector (n i) (orthogonalCoeff (n i) (k i)) v
  calc
    (∑ u : TensorVertex ι n, orthogonalTensor n j u * orthogonalTensor n k u) =
        ∑ u : TensorVertex ι n, ∏ i : ι, f i (u i) := by
          apply sum_congr rfl
          intro u _
          simp only [orthogonalTensor, f, prod_mul_distrib]
    _ = ∏ i : ι, ∑ v : Fin (n i + 1), f i v := (Fintype.prod_sum f).symm
    _ = ∏ i : ι,
          anchoredGram (orthogonalCoeff (n i) (j i))
            (orthogonalCoeff (n i) (k i)) := by
          apply prod_congr rfl
          intro i _
          exact (anchoredGram_eq_dot _ _).symm

/-- Distinct tensor indices give Euclidean-orthogonal vectors. -/
theorem tensor_orthogonal {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) {j k : TensorBasis ι n} (hjk : j ≠ k) :
    (∑ u : TensorVertex ι n, orthogonalTensor n j u * orthogonalTensor n k u) = 0 := by
  rw [tensor_dot_factor]
  have ⟨i, hi⟩ : ∃ i : ι, j i ≠ k i := by
    by_contra h
    apply hjk
    funext i
    by_contra hi
    exact h ⟨i, hi⟩
  exact prod_eq_zero (mem_univ i) (coeff_pairwise_orthogonal (n i) hi)

/-- Every tensor vector's squared Euclidean length is a product of the
one-factor squared lengths. -/
theorem tensor_squared_length {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) (j : TensorBasis ι n) :
    (∑ u : TensorVertex ι n, (orthogonalTensor n j u) ^ 2) =
      ∏ i : ι, (1 + 1 / ((j i).val + 1 : ℝ)) := by
  simpa only [← pow_two, coeff_gram_self] using tensor_dot_factor n j j

/-- The total squared length factors over the simplex coordinates. -/
theorem tensor_total_squared_length {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) :
    (∑ j : TensorBasis ι n,
      ∑ u : TensorVertex ι n, (orthogonalTensor n j u) ^ 2) =
      ∏ i : ι, ((n i : ℝ) +
        ∑ j : Fin (n i), (1 : ℝ) / (j.val + 1 : ℝ)) := by
  simp_rw [tensor_squared_length]
  let f : ∀ i : ι, Fin (n i) → ℝ :=
    fun i j => 1 + 1 / (j.val + 1 : ℝ)
  change (∑ j : TensorBasis ι n, ∏ i : ι, f i (j i)) =
    ∏ i : ι, ((n i : ℝ) +
      ∑ j : Fin (n i), (1 : ℝ) / (j.val + 1 : ℝ))
  rw [← Fintype.prod_sum f]
  apply prod_congr rfl
  intro i _
  simpa only [f, coeff_gram_self] using total_squared_length (n i)

end Erdos.Research.Problem774.TensorGramTrace

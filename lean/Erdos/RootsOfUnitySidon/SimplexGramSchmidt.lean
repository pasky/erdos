import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Fin.Tuple.Basic
import Mathlib.Order.Interval.Finset.Fin
import Mathlib.Tactic

/-!
# The anchored simplex and its orthogonal coordinates

The vectors `e_j - e_last` for `j : Fin n` have Gram matrix `I + J`.
The functions `orthogonalCoeff` give their explicit ordered orthogonalization:
the `j`-th vector has coefficient `1` at `j`, coefficient `-1/(j+1)`
at earlier indices, and zero at later indices. Their squared lengths are
`1 + 1/(j+1)`.

The ambient quadratic form `anchoredGram` is the ordinary Euclidean form
after sending a coefficient vector `x` to
`∑ j, x j • (e_j - e_last)` in `ℝ^(n+1)`.
-/

namespace Erdos.Research.Problem774.SimplexGramSchmidt

open Finset

/-- The Gram form of the anchored columns `e_j - e_last`. -/
def anchoredGram {n : ℕ} (x y : Fin n → ℝ) : ℝ :=
  (∑ i, x i * y i) + (∑ i, x i) * (∑ i, y i)

theorem anchoredGram_comm {n : ℕ} (x y : Fin n → ℝ) :
    anchoredGram x y = anchoredGram y x := by
  unfold anchoredGram
  have hsum : (∑ i, x i * y i) = ∑ i, y i * x i := by
    apply sum_congr rfl
    intro i _
    ring
  rw [hsum]
  ring

/-- Coordinates in `ℝ^(n+1)` of a linear combination of the columns
`e_j - e_last` with coefficients `x j`. -/
def anchoredVector (n : ℕ) (x : Fin n → ℝ) : Fin (n + 1) → ℝ :=
  Fin.snoc x (-(∑ i, x i))

/-- The coefficient Gram form is exactly the Euclidean dot product of the
corresponding anchored vectors. -/
theorem anchoredGram_eq_dot {n : ℕ} (x y : Fin n → ℝ) :
    anchoredGram x y =
      ∑ i : Fin (n + 1), anchoredVector n x i * anchoredVector n y i := by
  rw [Fin.sum_univ_castSucc]
  simp [anchoredGram, anchoredVector]

/-- Explicit coefficients of the `j`-th ordered orthogonalized column. -/
noncomputable def orthogonalCoeff (n : ℕ) (j i : Fin n) : ℝ :=
  if i = j then 1 else if i < j then -1 / (j.val + 1 : ℝ) else 0

theorem coeff_at (n : ℕ) (j : Fin n) :
    orthogonalCoeff n j j = 1 := by simp [orthogonalCoeff]

theorem coeff_before (n : ℕ) {i j : Fin n} (h : i < j) :
    orthogonalCoeff n j i = -1 / (j.val + 1 : ℝ) := by
  simp [orthogonalCoeff, h, ne_of_lt h]

theorem coeff_after (n : ℕ) {i j : Fin n} (h : j < i) :
    orthogonalCoeff n j i = 0 := by
  simp [orthogonalCoeff, (ne_of_gt h), not_lt_of_ge h.le]

private theorem coeff_indicator (n : ℕ) (j i : Fin n) :
    orthogonalCoeff n j i =
      (if i = j then 1 else 0) -
        (if i ∈ Iio j then (1 : ℝ) / (j.val + 1 : ℝ) else 0) := by
  by_cases hij : i = j
  · simp [orthogonalCoeff, hij]
  · by_cases hlt : i < j
    · simp [orthogonalCoeff, hij, hlt, div_eq_mul_inv]
    · simp [orthogonalCoeff, hij, hlt]

/-- The coordinate sum of the `j`-th orthogonalized column. -/
theorem coeff_sum (n : ℕ) (j : Fin n) :
    (∑ i : Fin n, orthogonalCoeff n j i) = 1 / (j.val + 1 : ℝ) := by
  simp_rw [coeff_indicator]
  rw [sum_sub_distrib]
  have hfirst : (∑ i : Fin n, if i = j then (1 : ℝ) else 0) = 1 := by simp
  have hsecond :
      (∑ i : Fin n, if i ∈ Iio j then (1 : ℝ) / (j.val + 1 : ℝ) else 0) =
        (j.val : ℝ) / (j.val + 1 : ℝ) := by
    simp only [Fintype.sum_ite_mem]
    simp [Fin.card_Iio, nsmul_eq_mul, div_eq_mul_inv]
  rw [hfirst, hsecond]
  have hpos : (j.val + 1 : ℝ) ≠ 0 := by positivity
  field_simp [hpos]
  ring

private theorem coeff_mul_before (n : ℕ) {k j : Fin n} (h : k < j) (i : Fin n) :
    orthogonalCoeff n j i * orthogonalCoeff n k i =
      (-1 / (j.val + 1 : ℝ)) * orthogonalCoeff n k i := by
  by_cases hij : i < j
  · exact congrArg (· * orthogonalCoeff n k i) (coeff_before n hij)
  · have hki : k < i := lt_of_lt_of_le h (le_of_not_gt hij)
    simp [coeff_after n hki]

/-- Distinct explicit columns are orthogonal for the anchored Gram form. -/
theorem coeff_orthogonal (n : ℕ) {k j : Fin n} (h : k < j) :
    anchoredGram (orthogonalCoeff n j) (orthogonalCoeff n k) = 0 := by
  simp only [anchoredGram]
  simp_rw [coeff_mul_before n h]
  rw [← mul_sum]
  simp only [coeff_sum]
  ring

theorem coeff_pairwise_orthogonal (n : ℕ) {j k : Fin n} (h : j ≠ k) :
    anchoredGram (orthogonalCoeff n j) (orthogonalCoeff n k) = 0 := by
  rcases lt_or_gt_of_ne h with hlt | hgt
  · rw [anchoredGram_comm]
    exact coeff_orthogonal n hlt
  · exact coeff_orthogonal n hgt

private theorem coeff_sq_indicator (n : ℕ) (j i : Fin n) :
    (orthogonalCoeff n j i) ^ 2 =
      (if i = j then (1 : ℝ) else 0) +
        (if i ∈ Iio j then (1 / (j.val + 1 : ℝ)) ^ 2 else 0) := by
  by_cases hij : i = j
  · simp [orthogonalCoeff, hij]
  · by_cases hlt : i < j
    · simp [orthogonalCoeff, hij, hlt]
      have hpos : (j.val + 1 : ℝ) ≠ 0 := by positivity
      field_simp [hpos]
    · simp [orthogonalCoeff, hij, hlt]

private theorem coeff_sq_sum (n : ℕ) (j : Fin n) :
    (∑ i : Fin n, (orthogonalCoeff n j i) ^ 2) =
      1 + (j.val : ℝ) * (1 / (j.val + 1 : ℝ)) ^ 2 := by
  simp_rw [coeff_sq_indicator]
  rw [sum_add_distrib]
  have hfirst : (∑ i : Fin n, if i = j then (1 : ℝ) else 0) = 1 := by simp
  have hsecond :
      (∑ i : Fin n,
          if i ∈ Iio j then (1 / (j.val + 1 : ℝ)) ^ 2 else 0) =
        (j.val : ℝ) * (1 / (j.val + 1 : ℝ)) ^ 2 := by
    simp only [Fintype.sum_ite_mem]
    simp [Fin.card_Iio, nsmul_eq_mul, div_eq_mul_inv]
  rw [hfirst, hsecond]

/-- The squared length of the `j`-th orthogonalized simplex column. -/
theorem coeff_gram_self (n : ℕ) (j : Fin n) :
    anchoredGram (orthogonalCoeff n j) (orthogonalCoeff n j) =
      1 + 1 / (j.val + 1 : ℝ) := by
  simp only [anchoredGram, ← pow_two]
  rw [coeff_sq_sum, coeff_sum]
  have hpos : (j.val + 1 : ℝ) ≠ 0 := by positivity
  field_simp [hpos]
  ring

/-- The sum of the squared Gram–Schmidt lengths for the `n + 1` vertex
simplex, expressed using the finite harmonic sum. -/
theorem total_squared_length (n : ℕ) :
    (∑ j : Fin n, anchoredGram (orthogonalCoeff n j) (orthogonalCoeff n j)) =
      (n : ℝ) + ∑ j : Fin n, (1 : ℝ) / (j.val + 1 : ℝ) := by
  simp_rw [coeff_gram_self]
  rw [sum_add_distrib]
  simp

end Erdos.Research.Problem774.SimplexGramSchmidt

import Erdos.RootsOfUnitySidon.TensorGramTrace

/-!
# Inverse anchored simplex coordinates

The ordered orthogonalization of the anchored simplex has a particularly
simple inverse: the coefficient of every earlier orthogonal column depends
only on that earlier index.
-/

namespace Erdos.Research.Problem774.SimplexGramSchmidtInverse

open Finset Erdos.Research.Problem774.SimplexGramSchmidt
  Erdos.Research.Problem774.TensorGramTrace

private theorem weighted_prefix (n : ℕ) (m : ℕ) (hm : m ≤ n)
    (i : Fin n) :
    (∑ k ∈ (Finset.univ.filter fun k : Fin n => k.val < m),
        (1 / (k.val + 2 : ℝ)) * orthogonalCoeff n k i) =
      if i.val < m then 1 / (m + 1 : ℝ) else 0 := by
  induction m with
  | zero => simp
  | succ m ih =>
      have hm' : m ≤ n := by omega
      have hmn : m < n := by omega
      let k₀ : Fin n := ⟨m, hmn⟩
      have hset :
          (Finset.univ.filter fun k : Fin n => k.val < m + 1) =
            insert k₀ (Finset.univ.filter fun k : Fin n => k.val < m) := by
        ext k
        simp only [mem_filter, mem_univ, true_and, mem_insert]
        constructor
        · intro h
          by_cases hk : k.val = m
          · left
            exact Fin.ext hk
          · right
            omega
        · rintro (rfl | h)
          · simp [k₀]
          · omega
      have hnot : k₀ ∉ (Finset.univ.filter fun k : Fin n => k.val < m) := by
        simp [k₀]
      rw [hset, sum_insert hnot, ih hm']
      by_cases him : i.val < m
      · have hki : i < k₀ := by exact him
        rw [coeff_before n hki]
        simp [him, show i.val < m + 1 by omega, k₀]
        have h₁ : (m + 1 : ℝ) ≠ 0 := by positivity
        have h₂ : (m + 2 : ℝ) ≠ 0 := by positivity
        field_simp [h₁, h₂]
        ring
      · by_cases hieq : i.val = m
        · have hi : i = k₀ := Fin.ext hieq
          rw [hi, coeff_at]
          simp [k₀]
          ring
        · have hki : k₀ < i := by exact_mod_cast (show m < i.val by omega)
          rw [coeff_after n hki]
          simp [him, show ¬ i.val < m + 1 by omega]

/-- The coefficient identity inverse to the ordered simplex
orthogonalization. -/
theorem anchoredCoeff_inverse (n : ℕ) (j i : Fin n) :
    (if i = j then (1 : ℝ) else 0) =
      orthogonalCoeff n j i +
        ∑ k ∈ Finset.Iio j,
          (1 / (k.val + 2 : ℝ)) * orthogonalCoeff n k i := by
  have hset : (Finset.univ.filter fun k : Fin n => k.val < j.val) =
      Finset.Iio j := by
    ext k
    simp
  have hs := weighted_prefix n j.val j.isLt.le i
  rw [hset] at hs
  rw [hs]
  by_cases hij : i = j
  · subst i
    simp [coeff_at]
  · by_cases hlt : i < j
    · rw [coeff_before n hlt]
      simp [hij, hlt]
      ring
    · have hgt : j < i := lt_of_le_of_ne (le_of_not_gt hlt) (Ne.symm hij)
      rw [coeff_after n hgt]
      simp [hij, hlt]

/-- Explicit inverse of the one-factor anchored simplex
orthogonalization. -/
theorem anchoredBasis_inverse (n : ℕ) (j : Fin n)
    (u : Fin (n + 1)) :
    anchoredBasis n j u =
      anchoredVector n (orthogonalCoeff n j) u +
        ∑ k ∈ Finset.Iio j,
          (1 / (k.val + 2 : ℝ)) *
            anchoredVector n (orthogonalCoeff n k) u := by
  rw [anchoredVector_eq_sum_basis]
  simp_rw [anchoredVector_eq_sum_basis]
  -- Rearrange the finite double sum into anchored basis coordinates.
  simp_rw [mul_sum]
  rw [Finset.sum_comm]
  simp_rw [← mul_assoc]
  simp_rw [← Finset.sum_mul]
  rw [← Finset.sum_add_distrib]
  simp_rw [← add_mul]
  simp_rw [← anchoredCoeff_inverse n j]
  simp

end Erdos.Research.Problem774.SimplexGramSchmidtInverse

import Erdos.RootsOfUnitySidon.FiniteSidonInterpolation
import Mathlib.Analysis.Convex.Jensen
import Mathlib.Analysis.Convex.Mul

/-!
# Weighted finite moment contraction

This is the Jensen step in the interpolation-to-moment argument. The total
variation of the interpolation weights, rather than the number of support
points, controls the loss.
-/

namespace Erdos.Research.SidonExtraction

open scoped BigOperators

/-- A weighted form of the power triangle inequality. The normalized weights
sum to one, so the bound depends only on their total variation. -/
theorem norm_weighted_sum_pow_le {κ : Type*} (s : Finset κ)
    (w x : κ → ℂ) (n : ℕ)
    (hW : 0 < ∑ k ∈ s, ‖w k‖) :
    ‖∑ k ∈ s, w k * x k‖ ^ n ≤
      (∑ k ∈ s, ‖w k‖) ^ n *
        ∑ k ∈ s, ((∑ j ∈ s, ‖w j‖)⁻¹ * ‖w k‖) * ‖x k‖ ^ n := by
  classical
  let W : ℝ := ∑ k ∈ s, ‖w k‖
  let q : κ → ℝ := fun k => W⁻¹ * ‖w k‖
  have hW0 : W ≠ 0 := ne_of_gt hW
  have hq0 : ∀ k ∈ s, 0 ≤ q k := by
    intro k _
    exact mul_nonneg (inv_nonneg.mpr hW.le) (norm_nonneg _)
  have hqsum : ∑ k ∈ s, q k = 1 := by
    simp [q, ← Finset.mul_sum, W, inv_mul_cancel₀ hW0]
  have hqmem : ∀ k ∈ s, ‖x k‖ ∈ Set.Ici (0 : ℝ) := by
    intro k _
    exact norm_nonneg _
  have hJ : (∑ k ∈ s, q k * ‖x k‖) ^ n ≤
      ∑ k ∈ s, q k * ‖x k‖ ^ n := by
    simpa [smul_eq_mul] using
      (convexOn_pow n).map_sum_le (t := s) (w := q)
        (p := fun k => ‖x k‖) hq0 hqsum hqmem
  have hnorm : ‖∑ k ∈ s, w k * x k‖ ≤
      W * ∑ k ∈ s, q k * ‖x k‖ := by
    calc
      _ ≤ ∑ k ∈ s, ‖w k * x k‖ := norm_sum_le _ _
      _ = ∑ k ∈ s, ‖w k‖ * ‖x k‖ := by simp
      _ = W * ∑ k ∈ s, q k * ‖x k‖ := by
        rw [Finset.mul_sum]
        apply Finset.sum_congr rfl
        intro k _
        dsimp [q]
        calc
          ‖w k‖ * ‖x k‖ = (W * W⁻¹) * (‖w k‖ * ‖x k‖) := by simp [hW0]
          _ = W * (W⁻¹ * ‖w k‖) * ‖x k‖ := by ring
          _ = W * (W⁻¹ * ‖w k‖ * ‖x k‖) := by ring
  have hright : 0 ≤ W * ∑ k ∈ s, q k * ‖x k‖ := by
    exact mul_nonneg hW.le (Finset.sum_nonneg fun k hk =>
      mul_nonneg (hq0 k hk) (norm_nonneg _))
  calc
    _ ≤ (W * ∑ k ∈ s, q k * ‖x k‖) ^ n :=
      pow_le_pow_left₀ (norm_nonneg _) hnorm n
    _ = W ^ n * (∑ k ∈ s, q k * ‖x k‖) ^ n := mul_pow _ _ _
    _ ≤ W ^ n * ∑ k ∈ s, q k * ‖x k‖ ^ n :=
      mul_le_mul_of_nonneg_left hJ (pow_nonneg hW.le _)
    _ = _ := rfl

/-- A finite weighted combination has at most the total-weight loss in an
`n`th moment, provided each summand has the same (or smaller) moment bound. -/
theorem norm_weighted_moment_sum_le {κ σ : Type*}
    (s : Finset κ) (t : Finset σ) (w : κ → ℂ) (P : κ → σ → ℂ)
    (n : ℕ) (hn : 0 < n) (K M : ℝ) (hK : 0 ≤ K) (hM : 0 ≤ M)
    (hW : (∑ k ∈ s, ‖w k‖) ≤ K)
    (hP : ∀ k ∈ s, (∑ u ∈ t, ‖P k u‖ ^ n) ≤ M) :
    (∑ u ∈ t, ‖∑ k ∈ s, w k * P k u‖ ^ n) ≤ K ^ n * M := by
  classical
  let W : ℝ := ∑ k ∈ s, ‖w k‖
  have hWnonneg : 0 ≤ W := Finset.sum_nonneg fun _ _ => norm_nonneg _
  by_cases hW0 : W = 0
  · have hw0 : ∀ k ∈ s, w k = 0 := by
      intro k hk
      have hle : ‖w k‖ ≤ W :=
        Finset.single_le_sum (fun j _ => norm_nonneg (w j)) hk
      rw [hW0] at hle
      exact norm_eq_zero.mp (le_antisymm hle (norm_nonneg _))
    have hpoly0 (u : σ) : (∑ k ∈ s, w k * P k u) = 0 := by
      apply Finset.sum_eq_zero
      intro k hk
      simp [hw0 k hk]
    simp [hpoly0, hn.ne', mul_nonneg (pow_nonneg hK _) hM]
  · have hWpos : 0 < W := lt_of_le_of_ne hWnonneg (Ne.symm hW0)
    let q : κ → ℝ := fun k => W⁻¹ * ‖w k‖
    have hq0 : ∀ k ∈ s, 0 ≤ q k := by
      intro k _
      exact mul_nonneg (inv_nonneg.mpr hWnonneg) (norm_nonneg _)
    have hqsum : ∑ k ∈ s, q k = 1 := by
      simp [q, ← Finset.mul_sum, W, inv_mul_cancel₀ hW0]
    calc
      (∑ u ∈ t, ‖∑ k ∈ s, w k * P k u‖ ^ n)
          ≤ ∑ u ∈ t, W ^ n * ∑ k ∈ s, q k * ‖P k u‖ ^ n := by
              apply Finset.sum_le_sum
              intro u _
              simpa [W, q] using norm_weighted_sum_pow_le s w (fun k => P k u) n hWpos
      _ = W ^ n * ∑ k ∈ s, q k * (∑ u ∈ t, ‖P k u‖ ^ n) := by
          rw [← Finset.mul_sum, Finset.sum_comm]
          apply congrArg
          apply Finset.sum_congr rfl
          intro k _
          rw [← Finset.mul_sum]
      _ ≤ W ^ n * ∑ k ∈ s, q k * M := by
          apply mul_le_mul_of_nonneg_left _ (pow_nonneg hWnonneg _)
          apply Finset.sum_le_sum
          intro k hk
          exact mul_le_mul_of_nonneg_left (hP k hk) (hq0 k hk)
      _ = W ^ n * M := by rw [← Finset.sum_mul, hqsum, one_mul]
      _ ≤ K ^ n * M := by
          exact mul_le_mul_of_nonneg_right
            (pow_le_pow_left₀ hWnonneg hW n) hM

end Erdos.Research.SidonExtraction

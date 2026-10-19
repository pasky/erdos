import Mathlib.Analysis.SpecialFunctions.Log.Base
import Mathlib.Tactic

/-!
# The logarithmic form of the Problem 963 cardinal bound

This elementary implication converts a cardinal estimate for a dissociated
subset into the real logarithmic lower bound.
-/

namespace Erdos.Problem963

/-- The cardinal estimate `n ≤ (d + 1) 2 ^ d` implies the stated logarithmic
lower bound for `d`. -/
theorem log_bound_of_card_le (n d : ℕ) (hn : 0 < n)
    (hbound : n ≤ (d + 1) * 2 ^ d) :
    Real.logb 2 (n : ℝ) - Real.logb 2 (Real.logb 2 (n : ℝ) + 1) ≤ (d : ℝ) := by
  have hb : (1 : ℝ) < 2 := by norm_num
  have hnR : (0 : ℝ) < n := by exact_mod_cast hn
  have hnOne : (1 : ℝ) ≤ n := by
    exact_mod_cast (show 1 ≤ n by omega)
  have hlogn : 0 ≤ Real.logb 2 (n : ℝ) :=
    Real.logb_nonneg hb hnOne
  have hcast : (n : ℝ) ≤ ((d : ℝ) + 1) * (2 : ℝ) ^ d := by
    exact_mod_cast hbound
  have hraw : Real.logb 2 (n : ℝ) ≤ (d : ℝ) + Real.logb 2 ((d : ℝ) + 1) := by
    have h := Real.logb_le_logb_of_le hb hnR hcast
    rw [Real.logb_mul (by positivity) (by positivity), Real.logb_pow,
      Real.logb_self_eq_one hb] at h
    linarith
  by_cases hd : (d : ℝ) ≤ Real.logb 2 (n : ℝ)
  · have hmono : Real.logb 2 ((d : ℝ) + 1) ≤
        Real.logb 2 (Real.logb 2 (n : ℝ) + 1) :=
      Real.logb_le_logb_of_le hb (by positivity) (by linarith)
    linarith
  · have hmono : 0 ≤ Real.logb 2 (Real.logb 2 (n : ℝ) + 1) :=
      Real.logb_nonneg hb (by linarith)
    linarith

end Erdos.Problem963

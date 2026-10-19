import Mathlib.Analysis.SpecialFunctions.Trigonometric.Series
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic

/-!
# Finite moment-to-exponential bounds

All expectations are finite weighted sums.  The central bound needs only
even moments and can be applied to a real part of a character polynomial.
-/

namespace Erdos.Research.FiniteMomentExponential

open scoped BigOperators
open NormedSpace

/-- The factorial comparison used to sum Rudin-type even moments. -/
theorem factorial_mul_pow_le_even_factorial (m : ℕ) :
    m.factorial * m ^ m ≤ (2 * m).factorial := by
  calc
    m.factorial * m ^ m ≤ m.factorial * (m + 1) ^ m := by gcongr; omega
    _ ≤ (m + m).factorial := Nat.factorial_mul_pow_le_factorial
    _ = (2 * m).factorial := by ring

/-- A finite even-moment bound with factorial normalization controls the
finite average of `cosh`.  The `m = 0` moment is supplied by normalization. -/
theorem weighted_cosh_le_exp
    {Ω : Type*} (s : Finset Ω) (w X : Ω → ℝ)
    (C t : ℝ)
    (hw : ∀ ω ∈ s, 0 ≤ w ω)
    (hsum : ∑ ω ∈ s, w ω = 1)
    (hmoment : ∀ m : ℕ, 0 < m →
      ∑ ω ∈ s, w ω * X ω ^ (2 * m) ≤
        C ^ m * ((2 * m).factorial : ℝ) / (m.factorial : ℝ)) :
    (∑ ω ∈ s, w ω * Real.cosh (t * X ω)) ≤ Real.exp (C * t ^ 2) := by
  classical
  let F : ℕ → ℝ := fun m => ∑ ω ∈ s,
    w ω * (t * X ω) ^ (2 * m) / ((2 * m).factorial : ℝ)
  have hFle (m : ℕ) : F m ≤ (C * t ^ 2) ^ m / (m.factorial : ℝ) := by
    by_cases hm : m = 0
    · subst m
      simp [F, hsum]
    · have hmpos : 0 < m := Nat.pos_of_ne_zero hm
      have hrewrite : F m =
          t ^ (2 * m) / ((2 * m).factorial : ℝ) *
            (∑ ω ∈ s, w ω * X ω ^ (2 * m)) := by
        rw [Finset.mul_sum]
        apply Finset.sum_congr rfl
        intro ω _
        rw [mul_pow]
        ring
      rw [hrewrite]
      have htPow : 0 ≤ t ^ (2 * m) := by
        rw [show 2 * m = m * 2 by omega, pow_mul]
        positivity
      have hfacpos : (0 : ℝ) < ((2 * m).factorial : ℝ) := by positivity
      have hmp : (0 : ℝ) < (m.factorial : ℝ) := by positivity
      calc
        _ ≤ t ^ (2 * m) / ((2 * m).factorial : ℝ) *
              (C ^ m * ((2 * m).factorial : ℝ) / (m.factorial : ℝ)) := by
                exact mul_le_mul_of_nonneg_left (hmoment m hmpos)
                  (div_nonneg htPow hfacpos.le)
        _ = (C * t ^ 2) ^ m / (m.factorial : ℝ) := by
              field_simp
              ring
  have hseries : Summable (fun m : ℕ =>
      (C * t ^ 2) ^ m / (m.factorial : ℝ)) := by
    have h := NormedSpace.expSeries_summable' (𝕂 := ℝ) (C * t ^ 2)
    simpa [smul_eq_mul, div_eq_mul_inv, mul_comm] using h
  have hFsummable : Summable F := by
    apply Summable.of_nonneg_of_le
      (fun m => Finset.sum_nonneg fun ω hω => by
        apply div_nonneg
        apply mul_nonneg (hw ω hω)
        rw [show 2 * m = m * 2 by omega, pow_mul]
        positivity
        positivity)
      hFle
    exact hseries
  have hswap :
      (∑ ω ∈ s, w ω * Real.cosh (t * X ω)) = ∑' m, F m := by
    simp_rw [Real.cosh_eq_tsum, ← tsum_mul_left]
    rw [← Summable.tsum_finsetSum]
    · congr 1
      ext m
      simp only [F]
      apply Finset.sum_congr rfl
      intro ω _
      ring
    · intro ω hω
      exact ((Real.hasSum_cosh (t * X ω)).summable.mul_left (w ω))
  rw [hswap, Real.exp_eq_exp_ℝ, NormedSpace.exp_eq_tsum_div]
  exact hFsummable.tsum_le_tsum hFle hseries

/-- The elementary comparison that turns an even-moment bound into a bound
for an unsymmetrized exponential. -/
theorem exp_le_two_cosh_add_sub_one (x : ℝ) :
    Real.exp x ≤ 2 * Real.cosh x + x - 1 := by
  rw [Real.cosh_eq]
  have h := Real.add_one_le_exp (-x)
  linarith

/-- Centering removes the linear term in the preceding comparison. -/
theorem weighted_exp_le_exp_of_even_moments
    {Ω : Type*} (s : Finset Ω) (w X : Ω → ℝ)
    (C t : ℝ)
    (hw : ∀ ω ∈ s, 0 ≤ w ω)
    (hsum : ∑ ω ∈ s, w ω = 1)
    (hmean : ∑ ω ∈ s, w ω * X ω = 0)
    (hmoment : ∀ m : ℕ, 0 < m →
      ∑ ω ∈ s, w ω * X ω ^ (2 * m) ≤
        C ^ m * ((2 * m).factorial : ℝ) / (m.factorial : ℝ)) :
    (∑ ω ∈ s, w ω * Real.exp (t * X ω)) ≤ Real.exp (2 * C * t ^ 2) := by
  classical
  have hterm (ω : Ω) (hω : ω ∈ s) :
      w ω * Real.exp (t * X ω) ≤
        w ω * (2 * Real.cosh (t * X ω) + t * X ω - 1) :=
    mul_le_mul_of_nonneg_left
      (exp_le_two_cosh_add_sub_one (t * X ω)) (hw ω hω)
  have hcosh := weighted_cosh_le_exp s w X C t hw hsum hmoment
  have hsum' :
      ∑ ω ∈ s, w ω * (2 * Real.cosh (t * X ω) + t * X ω - 1) =
        2 * (∑ ω ∈ s, w ω * Real.cosh (t * X ω)) - 1 := by
    calc
      _ = ∑ ω ∈ s,
          (2 * (w ω * Real.cosh (t * X ω)) + t * (w ω * X ω) - w ω) := by
            apply Finset.sum_congr rfl
            intro ω _
            ring
      _ = _ := by
        rw [Finset.sum_sub_distrib, Finset.sum_add_distrib,
          ← Finset.mul_sum, ← Finset.mul_sum, hmean, hsum]
        ring
  have hfirst :
      (∑ ω ∈ s, w ω * Real.exp (t * X ω)) ≤
        2 * Real.exp (C * t ^ 2) - 1 := by
    calc
      _ ≤ ∑ ω ∈ s, w ω * (2 * Real.cosh (t * X ω) + t * X ω - 1) :=
          Finset.sum_le_sum hterm
      _ = 2 * (∑ ω ∈ s, w ω * Real.cosh (t * X ω)) - 1 := hsum'
      _ ≤ 2 * Real.exp (C * t ^ 2) - 1 := by linarith
  have hlast : 2 * Real.exp (C * t ^ 2) - 1 ≤
      Real.exp (2 * C * t ^ 2) := by
    have heq : Real.exp (2 * C * t ^ 2) =
        Real.exp (C * t ^ 2) ^ 2 := by
      rw [show 2 * C * t ^ 2 = C * t ^ 2 + C * t ^ 2 by ring,
        Real.exp_add]
      ring
    rw [heq]
    nlinarith [sq_nonneg (Real.exp (C * t ^ 2) - 1)]
  exact hfirst.trans hlast

/-- A finite Rudin even-moment inequality yields a Gaussian exponential
bound, with explicit factor two in the exponent. -/
theorem weighted_exp_le_exp_of_rudin_moments
    {Ω : Type*} (s : Finset Ω) (w X : Ω → ℝ)
    (D N t : ℝ) (hD : 0 ≤ D) (hN : 0 ≤ N)
    (hw : ∀ ω ∈ s, 0 ≤ w ω)
    (hsum : ∑ ω ∈ s, w ω = 1)
    (hmean : ∑ ω ∈ s, w ω * X ω = 0)
    (hmoment : ∀ m : ℕ, 0 < m →
      ∑ ω ∈ s, w ω * X ω ^ (2 * m) ≤
        (D * (m : ℝ)) ^ m * N ^ m) :
    (∑ ω ∈ s, w ω * Real.exp (t * X ω)) ≤
      Real.exp (2 * D * N * t ^ 2) := by
  have hfac (m : ℕ) :
      (m : ℝ) ^ m ≤ ((2 * m).factorial : ℝ) / (m.factorial : ℝ) := by
    apply (le_div_iff₀ (by positivity : (0 : ℝ) < (m.factorial : ℝ))).2
    have hf : (m.factorial : ℝ) * (m : ℝ) ^ m ≤
        ((2 * m).factorial : ℝ) := by
      exact_mod_cast factorial_mul_pow_le_even_factorial m
    simpa only [mul_comm] using hf
  have hm' (m : ℕ) (hm : 0 < m) :
      ∑ ω ∈ s, w ω * X ω ^ (2 * m) ≤
        (D * N) ^ m * ((2 * m).factorial : ℝ) / (m.factorial : ℝ) := by
    calc
      _ ≤ (D * (m : ℝ)) ^ m * N ^ m := hmoment m hm
      _ = (D * N) ^ m * (m : ℝ) ^ m := by
          simp only [mul_pow]
          ring
      _ ≤ (D * N) ^ m * (((2 * m).factorial : ℝ) / (m.factorial : ℝ)) :=
          mul_le_mul_of_nonneg_left (hfac m) (pow_nonneg (mul_nonneg hD hN) m)
      _ = _ := by ring
  simpa [mul_assoc] using
    weighted_exp_le_exp_of_even_moments s w X (D * N) t hw hsum hmean hm'

/-- Only finitely many Rudin moments need analytic control. Above the cutoff,
a pointwise bound on `X²` supplies all remaining moments. -/
theorem weighted_rudin_moments_of_truncated
    {Ω : Type*} (s : Finset Ω) (w X : Ω → ℝ)
    (D N : ℝ) (M : ℕ) (hD : 0 ≤ D) (hN : 0 ≤ N)
    (hw : ∀ ω ∈ s, 0 ≤ w ω)
    (hsum : ∑ ω ∈ s, w ω = 1)
    (hpoint : ∀ ω ∈ s,
      X ω ^ 2 ≤ D * ((M + 1 : ℕ) : ℝ) * N)
    (hmoment : ∀ m : ℕ, 0 < m → m ≤ M →
      ∑ ω ∈ s, w ω * X ω ^ (2 * m) ≤
        (D * (m : ℝ)) ^ m * N ^ m) :
    ∀ m : ℕ, 0 < m →
      ∑ ω ∈ s, w ω * X ω ^ (2 * m) ≤
        (D * (m : ℝ)) ^ m * N ^ m := by
  intro m hm
  by_cases hmM : m ≤ M
  · exact hmoment m hm hmM
  · have hMm : M + 1 ≤ m := by omega
    have hbase (ω : Ω) (hω : ω ∈ s) :
        X ω ^ 2 ≤ D * (m : ℝ) * N := by
      calc
        _ ≤ D * ((M + 1 : ℕ) : ℝ) * N := hpoint ω hω
        _ ≤ D * (m : ℝ) * N := by
          gcongr
    calc
      ∑ ω ∈ s, w ω * X ω ^ (2 * m) ≤
          ∑ ω ∈ s, w ω * (D * (m : ℝ) * N) ^ m := by
            apply Finset.sum_le_sum
            intro ω hω
            apply mul_le_mul_of_nonneg_left _ (hw ω hω)
            rw [pow_mul]
            exact pow_le_pow_left₀ (sq_nonneg (X ω)) (hbase ω hω) m
      _ = (D * (m : ℝ) * N) ^ m := by
            rw [← Finset.sum_mul, hsum, one_mul]
      _ = (D * (m : ℝ)) ^ m * N ^ m := mul_pow _ _ _

/-- The finite-moment completion followed by the Gaussian bound. -/
theorem weighted_exp_le_exp_of_truncated_rudin_moments
    {Ω : Type*} (s : Finset Ω) (w X : Ω → ℝ)
    (D N t : ℝ) (M : ℕ) (hD : 0 ≤ D) (hN : 0 ≤ N)
    (hw : ∀ ω ∈ s, 0 ≤ w ω)
    (hsum : ∑ ω ∈ s, w ω = 1)
    (hmean : ∑ ω ∈ s, w ω * X ω = 0)
    (hpoint : ∀ ω ∈ s,
      X ω ^ 2 ≤ D * ((M + 1 : ℕ) : ℝ) * N)
    (hmoment : ∀ m : ℕ, 0 < m → m ≤ M →
      ∑ ω ∈ s, w ω * X ω ^ (2 * m) ≤
        (D * (m : ℝ)) ^ m * N ^ m) :
    (∑ ω ∈ s, w ω * Real.exp (t * X ω)) ≤
      Real.exp (2 * D * N * t ^ 2) := by
  exact weighted_exp_le_exp_of_rudin_moments s w X D N t hD hN hw hsum hmean
    (weighted_rudin_moments_of_truncated s w X D N M hD hN hw hsum hpoint hmoment)

end Erdos.Research.FiniteMomentExponential

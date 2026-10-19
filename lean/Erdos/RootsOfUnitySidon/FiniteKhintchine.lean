import Mathlib.Analysis.SpecialFunctions.Trigonometric.Series
import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Analysis.Complex.Basic
import Mathlib.Tactic

/-!
# Finite Rademacher moments

All averages here are finite sums over `Fin n → Bool`. In particular no
measure-theoretic independence or infinite probability space is needed.
-/

namespace Erdos.Research.FiniteKhintchine

open scoped BigOperators

def sign (b : Bool) : ℝ := if b then 1 else -1

def realSum {n : ℕ} (a : Fin n → ℝ) (ω : Fin n → Bool) : ℝ :=
  ∑ i, a i * sign (ω i)

private theorem exp_realSum {n : ℕ} (a : Fin n → ℝ) (ω : Fin n → Bool) (t : ℝ) :
    Real.exp (t * realSum a ω) =
      ∏ i, Real.exp (t * (a i * sign (ω i))) := by
  rw [realSum, Finset.mul_sum, Real.exp_sum]

private theorem sum_exp_realSum {n : ℕ} (a : Fin n → ℝ) (t : ℝ) :
    (∑ ω : Fin n → Bool, Real.exp (t * realSum a ω)) =
      ∏ i : Fin n, (Real.exp (t * a i) + Real.exp (-(t * a i))) := by
  classical
  calc
    _ = ∑ ω : Fin n → Bool, ∏ i, Real.exp (t * (a i * sign (ω i))) := by
      congr 1
      funext ω
      exact exp_realSum a ω t
    _ = ∏ i : Fin n, ∑ b : Bool, Real.exp (t * (a i * sign b)) := by
      rw [Fintype.prod_sum]
    _ = ∏ i : Fin n, (Real.exp (t * a i) + Real.exp (-(t * a i))) := by
      congr 1
      funext i
      simp [sign]

/-- The elementary finite subgaussian estimate for Rademacher sums. -/
theorem sum_exp_realSum_le {n : ℕ} (a : Fin n → ℝ) (t : ℝ) :
    (∑ ω : Fin n → Bool, Real.exp (t * realSum a ω)) ≤
      (2 : ℝ) ^ n * Real.exp (t ^ 2 * (∑ i, a i ^ 2) / 2) := by
  classical
  have hterm (i : Fin n) :
      Real.exp (t * a i) + Real.exp (-(t * a i)) ≤
        2 * Real.exp ((t * a i) ^ 2 / 2) := by
    have h := Real.cosh_le_exp_half_sq (t * a i)
    rw [Real.cosh_eq] at h
    nlinarith
  calc
    _ = ∏ i : Fin n, (Real.exp (t * a i) + Real.exp (-(t * a i))) :=
      sum_exp_realSum a t
    _ ≤ ∏ i : Fin n, (2 * Real.exp ((t * a i) ^ 2 / 2)) := by
      apply Finset.prod_le_prod₀
      · intro i hi
        positivity
      · intro i hi
        exact hterm i
    _ = (2 : ℝ) ^ n * Real.exp (t ^ 2 * (∑ i, a i ^ 2) / 2) := by
      rw [Finset.prod_mul_distrib, ← Real.exp_sum]
      simp only [Finset.prod_const, Finset.card_univ, Fintype.card_fin]
      congr 1
      simp only [mul_pow, div_eq_mul_inv, ← Finset.sum_mul, ← Finset.mul_sum]

private theorem exp_abs_le_sum (x : ℝ) :
    Real.exp |x| ≤ Real.exp x + Real.exp (-x) := by
  rcases le_total 0 x with hx | hx
  · rw [abs_of_nonneg hx]
    exact le_add_of_nonneg_right (Real.exp_nonneg _)
  · rw [abs_of_nonpos hx]
    exact le_add_of_nonneg_left (Real.exp_nonneg _)

private theorem even_pow_le_factorial_exp (x : ℝ) (m : ℕ) :
    x ^ (2 * m) ≤ ((2 * m).factorial : ℝ) *
      (Real.exp x + Real.exp (-x)) := by
  have h := Real.pow_div_factorial_le_exp |x| (abs_nonneg x) (2 * m)
  have hf : (0 : ℝ) < (2 * m).factorial := by positivity
  have hpow : x ^ (2 * m) = |x| ^ (2 * m) := by
    rw [← abs_pow, abs_of_nonneg (Even.pow_nonneg (even_two_mul m) x)]
  rw [hpow]
  calc
    _ ≤ ((2 * m).factorial : ℝ) * Real.exp |x| := by
      apply (div_le_iff₀ hf).mp at h
      simpa [mul_comm] using h
    _ ≤ ((2 * m).factorial : ℝ) *
        (Real.exp x + Real.exp (-x)) := by
      gcongr
      exact exp_abs_le_sum x

/-- An even-moment estimate with a free exponential parameter. -/
theorem sum_even_pow_mul_le {n : ℕ} (a : Fin n → ℝ) (t : ℝ) (m : ℕ) :
    (∑ ω : Fin n → Bool, (t * realSum a ω) ^ (2 * m)) ≤
      ((2 * m).factorial : ℝ) *
        (2 * (2 : ℝ) ^ n * Real.exp (t ^ 2 * (∑ i, a i ^ 2) / 2)) := by
  classical
  have hpos : 0 ≤ ((2 * m).factorial : ℝ) := by positivity
  calc
    _ ≤ ∑ ω : Fin n → Bool,
        ((2 * m).factorial : ℝ) *
          (Real.exp (t * realSum a ω) + Real.exp (-(t * realSum a ω))) := by
      apply Finset.sum_le_sum
      intro ω _
      exact even_pow_le_factorial_exp _ _
    _ = ((2 * m).factorial : ℝ) *
        ((∑ ω : Fin n → Bool, Real.exp (t * realSum a ω)) +
          (∑ ω : Fin n → Bool, Real.exp ((-t) * realSum a ω))) := by
      simp_rw [neg_mul]
      rw [← Finset.mul_sum, Finset.sum_add_distrib, mul_add]
    _ ≤ ((2 * m).factorial : ℝ) *
        (2 * (2 : ℝ) ^ n * Real.exp (t ^ 2 * (∑ i, a i ^ 2) / 2)) := by
      apply mul_le_mul_of_nonneg_left _ hpos
      have hplus := sum_exp_realSum_le a t
      have hminus := sum_exp_realSum_le a (-t)
      simp only [neg_sq] at hminus
      linarith

private theorem factorial_exp_bound (m : ℕ) (hm : 0 < m) :
    ((2 * m).factorial : ℝ) * (2 * Real.exp m) ≤
      ((2 * m : ℕ) : ℝ) ^ m * ((12 * m : ℕ) : ℝ) ^ m := by
  have hfactorial : ((2 * m).factorial : ℝ) ≤ ((2 * m : ℕ) : ℝ) ^ (2 * m) := by
    exact_mod_cast Nat.factorial_le_pow (2 * m)
  have hexp : Real.exp (m : ℝ) ≤ (3 : ℝ) ^ m := by
    rw [← Real.exp_one_pow]
    gcongr
    exact Real.exp_one_lt_three.le
  have htwo : (2 : ℝ) ≤ 2 ^ m := by
    simpa using pow_le_pow_right₀ (by norm_num : (1 : ℝ) ≤ 2) hm
  calc
    _ ≤ ((2 * m : ℕ) : ℝ) ^ (2 * m) * (2 * (3 : ℝ) ^ m) := by
      gcongr
    _ ≤ ((2 * m : ℕ) : ℝ) ^ (2 * m) * ((2 : ℝ) ^ m * 3 ^ m) := by
      gcongr
    _ = ((2 * m : ℕ) : ℝ) ^ m * ((12 * m : ℕ) : ℝ) ^ m := by
      push_cast
      calc
        (2 * (m : ℝ)) ^ (2 * m) * (2 ^ m * 3 ^ m) =
            (2 * (m : ℝ)) ^ m * ((2 * (m : ℝ) * 2 * 3) ^ m) := by
          rw [show 2 * m = m + m by omega, pow_add]
          have hprod : (2 * (m : ℝ) * 2 * 3) ^ m =
              (2 * (m : ℝ)) ^ m * 2 ^ m * 3 ^ m := by
            rw [mul_pow, mul_pow]
          rw [hprod]
          ring
        _ = (2 * (m : ℝ)) ^ m * (12 * (m : ℝ)) ^ m := by
          congr 1
          ring

/-- Finite real Khintchine inequality, with a deliberately loose universal
constant. The cardinal factor is the number of sign vectors. -/
theorem real_even_moment_le {n : ℕ} (a : Fin n → ℝ) (m : ℕ) (hm : 0 < m) :
    (∑ ω : Fin n → Bool, (realSum a ω) ^ (2 * m)) ≤
      (2 : ℝ) ^ n * ((12 * m : ℕ) : ℝ) ^ m * (∑ i, a i ^ 2) ^ m := by
  classical
  let V : ℝ := ∑ i, a i ^ 2
  have hVnonneg : 0 ≤ V := Finset.sum_nonneg fun i _ => sq_nonneg (a i)
  by_cases hVzero : V = 0
  · have ha (i : Fin n) : a i = 0 := by
      have hsq : a i ^ 2 ≤ V :=
        Finset.single_le_sum (fun j _ => sq_nonneg (a j)) (Finset.mem_univ i)
      have : a i ^ 2 = 0 := by nlinarith [sq_nonneg (a i)]
      nlinarith
    simp [realSum, ha, hm.ne']
  have hVpos : 0 < V := lt_of_le_of_ne hVnonneg (Ne.symm hVzero)
  let t : ℝ := Real.sqrt (((2 * m : ℕ) : ℝ) / V)
  have htnonneg : 0 ≤ t := Real.sqrt_nonneg _
  have ht2 : t ^ 2 = (((2 * m : ℕ) : ℝ) / V) := by
    exact Real.sq_sqrt (div_nonneg (by positivity) hVnonneg)
  have htV : t ^ 2 * V / 2 = (m : ℝ) := by
    rw [ht2]
    field_simp
    norm_cast
  have hbase := sum_even_pow_mul_le a t m
  rw [htV] at hbase
  have hleft :
      (∑ ω : Fin n → Bool, (t * realSum a ω) ^ (2 * m)) =
        ((((2 * m : ℕ) : ℝ) / V) ^ m) *
          (∑ ω : Fin n → Bool, (realSum a ω) ^ (2 * m)) := by
    simp_rw [mul_pow]
    rw [← Finset.mul_sum, pow_mul, ht2]
  rw [hleft] at hbase
  have hfactor :
      ((((2 * m : ℕ) : ℝ) / V) ^ m) * V ^ m =
        (((2 * m : ℕ) : ℝ) ^ m) := by
    rw [div_pow, div_mul_cancel₀]
    exact pow_ne_zero _ hVzero
  have hscaled := mul_le_mul_of_nonneg_right hbase (pow_nonneg hVnonneg m)
  have hnum := factorial_exp_bound m hm
  have htarget :
      (((2 * m : ℕ) : ℝ) ^ m) *
        (∑ ω : Fin n → Bool, (realSum a ω) ^ (2 * m)) ≤
      (((2 * m : ℕ) : ℝ) ^ m) *
        ((2 : ℝ) ^ n * ((12 * m : ℕ) : ℝ) ^ m * V ^ m) := by
    calc
      _ = (((2 * m : ℕ) : ℝ) / V) ^ m *
          (∑ ω : Fin n → Bool, (realSum a ω) ^ (2 * m)) * V ^ m := by
        rw [mul_right_comm, hfactor]
      _ ≤ ((2 * m).factorial : ℝ) *
          (2 * (2 : ℝ) ^ n * Real.exp (m : ℝ)) * V ^ m := hscaled
      _ = (((2 * m).factorial : ℝ) * (2 * Real.exp (m : ℝ))) *
          ((2 : ℝ) ^ n * V ^ m) := by ring
      _ ≤ ((((2 * m : ℕ) : ℝ) ^ m) * (((12 * m : ℕ) : ℝ) ^ m)) *
          ((2 : ℝ) ^ n * V ^ m) := by
        exact mul_le_mul_of_nonneg_right hnum (by positivity)
      _ = (((2 * m : ℕ) : ℝ) ^ m) *
          ((2 : ℝ) ^ n * ((12 * m : ℕ) : ℝ) ^ m * V ^ m) := by ring
  have hp : 0 < (((2 * m : ℕ) : ℝ) ^ m) := by positivity
  exact (mul_le_mul_iff_right₀ hp).mp htarget

end Erdos.Research.FiniteKhintchine

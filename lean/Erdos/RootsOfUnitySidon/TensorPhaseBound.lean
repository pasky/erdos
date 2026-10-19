import Mathlib.Analysis.Complex.Exponential
import Mathlib.Analysis.Complex.Trigonometric
import Mathlib.Analysis.Complex.Norm
import Mathlib.Tactic

/-!
A global quadratic remainder bound for purely imaginary exponential phases.  This is
the pointwise estimate used when a tensor character is perturbed by a small phase.
-/

namespace Erdos.Research.TensorPhaseBound

private lemma norm_imaginary (t : ℝ) : ‖Complex.I * (t : ℂ)‖ = |t| := by
  simp [Complex.norm_I, Complex.norm_real]

/-- A global quadratic error bound for a purely imaginary exponential phase. -/
theorem norm_exp_I_mul_sub_one_sub_le (t : ℝ) :
    ‖Complex.exp (Complex.I * (t : ℂ)) - 1 - Complex.I * (t : ℂ)‖ ≤
      3 * t ^ 2 := by
  by_cases ht : |t| ≤ 1
  · have hx : ‖Complex.I * (t : ℂ)‖ ≤ 1 := by simpa [norm_imaginary] using ht
    have h := Complex.norm_exp_sub_one_sub_id_le hx
    rw [norm_imaginary] at h
    have hsq : |t| ^ 2 = t ^ 2 := sq_abs t
    rw [hsq] at h
    nlinarith [sq_nonneg t]
  · have ht₁ : 1 ≤ |t| := le_of_lt (lt_of_not_ge ht)
    have he : ‖Complex.exp (Complex.I * (t : ℂ))‖ = 1 :=
      Complex.norm_exp_I_mul_ofReal t
    have htri :
        ‖Complex.exp (Complex.I * (t : ℂ)) - 1 - Complex.I * (t : ℂ)‖ ≤
          ‖Complex.exp (Complex.I * (t : ℂ))‖ + ‖(1 : ℂ)‖ +
            ‖Complex.I * (t : ℂ)‖ := by
      calc
        _ ≤ ‖Complex.exp (Complex.I * (t : ℂ)) - 1‖ +
              ‖Complex.I * (t : ℂ)‖ := norm_sub_le _ _
        _ ≤ (‖Complex.exp (Complex.I * (t : ℂ))‖ + ‖(1 : ℂ)‖) +
              ‖Complex.I * (t : ℂ)‖ := by gcongr; exact norm_sub_le _ _
        _ = _ := by ring
    rw [he, norm_one, norm_imaginary] at htri
    have ht₂ : 1 ≤ t ^ 2 := by nlinarith [sq_abs t]
    have ht₃ : |t| ≤ t ^ 2 := by nlinarith [sq_abs t]
    nlinarith

/-- A pointwise lower bound for the real part after a phase perturbation. -/
theorem re_mul_exp_I_mul_lower (z : ℂ) (t : ℝ) :
    z.re - t * z.im - 3 * ‖z‖ * t ^ 2 ≤
      (z * Complex.exp (Complex.I * (t : ℂ))).re := by
  let r : ℂ := Complex.exp (Complex.I * (t : ℂ)) - 1 - Complex.I * (t : ℂ)
  have hr : ‖r‖ ≤ 3 * t ^ 2 := norm_exp_I_mul_sub_one_sub_le t
  have hmul : -(‖z‖ * ‖r‖) ≤ (z * r).re := by
    have h := Complex.re_le_norm (-(z * r))
    rw [Complex.neg_re, norm_neg, norm_mul] at h
    linarith
  have hznorm : 0 ≤ ‖z‖ := norm_nonneg _
  have hmul' : -(3 * ‖z‖ * t ^ 2) ≤ (z * r).re := by
    nlinarith [mul_le_mul_of_nonneg_left hr hznorm]
  have hid : z * Complex.exp (Complex.I * (t : ℂ)) =
      z + z * (Complex.I * (t : ℂ)) + z * r := by
    dsimp [r]
    ring
  have hlinear : (z * (Complex.I * (t : ℂ))).re = -z.im * t := by
    rw [← mul_assoc, Complex.re_mul_ofReal, Complex.mul_I_re]
  rw [hid, Complex.add_re, Complex.add_re, hlinear]
  nlinarith

/-- A zero-mean random phase loses at most three times its second moment in
the real part.  The weights are represented by a finite sum. -/
theorem weighted_phase_lower {α : Type*} (s : Finset α)
    (w t : α → ℝ) (z : ℂ) (Q : ℝ)
    (hw : ∀ i ∈ s, 0 ≤ w i)
    (hweight : (∑ i ∈ s, w i) = 1)
    (hmean : (∑ i ∈ s, w i * t i) = 0)
    (hmoment : (∑ i ∈ s, w i * t i ^ 2) ≤ Q) :
    z.re - 3 * ‖z‖ * Q ≤
      ∑ i ∈ s, w i * (z * Complex.exp (Complex.I * (t i : ℂ))).re := by
  have herror :
      z.re - 3 * ‖z‖ * Q ≤
        z.re - 3 * ‖z‖ * (∑ i ∈ s, w i * t i ^ 2) := by
    nlinarith [mul_le_mul_of_nonneg_left hmoment (by positivity : 0 ≤ 3 * ‖z‖)]
  have hlinear :
      z.re - 3 * ‖z‖ * (∑ i ∈ s, w i * t i ^ 2) =
        ∑ i ∈ s, w i * (z.re - t i * z.im - 3 * ‖z‖ * t i ^ 2) := by
    calc
      _ = z.re * (∑ i ∈ s, w i) - z.im * (∑ i ∈ s, w i * t i) -
          (3 * ‖z‖) * (∑ i ∈ s, w i * t i ^ 2) := by rw [hweight, hmean]; ring
      _ = _ := by
        simp only [Finset.mul_sum, ← Finset.sum_sub_distrib]
        apply Finset.sum_congr rfl
        intro i hi
        ring
  calc
    _ ≤ z.re - 3 * ‖z‖ * (∑ i ∈ s, w i * t i ^ 2) := herror
    _ = ∑ i ∈ s, w i * (z.re - t i * z.im - 3 * ‖z‖ * t i ^ 2) := hlinear
    _ ≤ _ := by
      apply Finset.sum_le_sum
      intro i hi
      exact mul_le_mul_of_nonneg_left (re_mul_exp_I_mul_lower z (t i)) (hw i hi)

/-- The weighted phase bound after scaling all phases by a positive `q`. -/
theorem weighted_phase_div_lower {α : Type*} (s : Finset α)
    (w t : α → ℝ) (z : ℂ) (Q q : ℝ)
    (hw : ∀ i ∈ s, 0 ≤ w i)
    (hweight : (∑ i ∈ s, w i) = 1)
    (hmean : (∑ i ∈ s, w i * t i) = 0)
    (hmoment : (∑ i ∈ s, w i * t i ^ 2) ≤ Q)
    (hq : 0 < q) :
    z.re - 3 * ‖z‖ * Q / q ^ 2 ≤
      ∑ i ∈ s, w i *
        (z * Complex.exp (Complex.I * ((t i / q : ℝ) : ℂ))).re := by
  have hmean' : (∑ i ∈ s, w i * (t i / q)) = 0 := by
    calc
      _ = (∑ i ∈ s, w i * t i) / q := by
        rw [Finset.sum_div]
        apply Finset.sum_congr rfl
        intro i hi
        ring
      _ = 0 := by rw [hmean]; simp
  have hmoment' : (∑ i ∈ s, w i * (t i / q) ^ 2) ≤ Q / q ^ 2 := by
    have heq : (∑ i ∈ s, w i * (t i / q) ^ 2) =
        (∑ i ∈ s, w i * t i ^ 2) / q ^ 2 := by
      rw [Finset.sum_div]
      apply Finset.sum_congr rfl
      intro i hi
      ring
    rw [heq]
    exact div_le_div_of_nonneg_right hmoment (by positivity)
  simpa [div_eq_mul_inv, mul_assoc] using
    weighted_phase_lower s w (fun i => t i / q) z (Q / q ^ 2)
      hw hweight hmean' hmoment'

end Erdos.Research.TensorPhaseBound

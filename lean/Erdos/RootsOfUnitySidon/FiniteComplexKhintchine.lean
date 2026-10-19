import Erdos.RootsOfUnitySidon.FiniteKhintchine

/-!
# Finite complex Khintchine inequality

The real Rademacher moment bound is applied separately to the real and
imaginary parts. A loose factor keeps the final constant simple.
-/

namespace Erdos.Research.FiniteComplexKhintchine

open scoped BigOperators
open Erdos.Research.FiniteKhintchine

def complexSum {n : ℕ} (a : Fin n → ℂ) (ω : Fin n → Bool) : ℂ :=
  ∑ i, a i * (sign (ω i) : ℂ)

private theorem complexSum_re {n : ℕ} (a : Fin n → ℂ)
    (ω : Fin n → Bool) :
    (complexSum a ω).re = realSum (fun i => (a i).re) ω := by
  simp [complexSum, realSum, Complex.re_sum, Complex.mul_re]

private theorem complexSum_im {n : ℕ} (a : Fin n → ℂ)
    (ω : Fin n → Bool) :
    (complexSum a ω).im = realSum (fun i => (a i).im) ω := by
  simp [complexSum, realSum, Complex.im_sum, Complex.mul_im]

private theorem complex_norm_even_pow_le_parts (z : ℂ) (m : ℕ) :
    ‖z‖ ^ (2 * m) ≤ (2 : ℝ) ^ m *
      (z.re ^ (2 * m) + z.im ^ (2 * m)) := by
  have hre : 0 ≤ z.re ^ 2 := sq_nonneg _
  have him : 0 ≤ z.im ^ 2 := sq_nonneg _
  have hbase := add_pow_le hre him m
  have htwo : (2 : ℝ) ^ (m - 1) ≤ 2 ^ m :=
    pow_le_pow_right₀ (by norm_num) (Nat.sub_le m 1)
  calc
    ‖z‖ ^ (2 * m) = (z.re ^ 2 + z.im ^ 2) ^ m := by
      rw [pow_mul, Complex.sq_norm, Complex.normSq_apply]
      ring
    _ ≤ 2 ^ (m - 1) * ((z.re ^ 2) ^ m + (z.im ^ 2) ^ m) := hbase
    _ ≤ 2 ^ m * ((z.re ^ 2) ^ m + (z.im ^ 2) ^ m) := by
      gcongr
    _ = 2 ^ m * (z.re ^ (2 * m) + z.im ^ (2 * m)) := by
      rw [pow_mul, pow_mul]

private theorem re_sq_le_norm_sq (z : ℂ) : z.re ^ 2 ≤ ‖z‖ ^ 2 := by
  nlinarith [Complex.sq_norm_sub_sq_re z, sq_nonneg z.im]

private theorem im_sq_le_norm_sq (z : ℂ) : z.im ^ 2 ≤ ‖z‖ ^ 2 := by
  nlinarith [Complex.sq_norm_sub_sq_im z, sq_nonneg z.re]

/-- Complex Rademacher moment bound with one universal constant. -/
theorem complex_even_moment_le {n : ℕ} (a : Fin n → ℂ)
    (m : ℕ) (hm : 0 < m) :
    (∑ ω : Fin n → Bool, ‖complexSum a ω‖ ^ (2 * m)) ≤
      (2 : ℝ) ^ n * ((48 * m : ℕ) : ℝ) ^ m *
        (∑ i, ‖a i‖ ^ 2) ^ m := by
  classical
  let V : ℝ := ∑ i, ‖a i‖ ^ 2
  let Vr : ℝ := ∑ i, (a i).re ^ 2
  let Vi : ℝ := ∑ i, (a i).im ^ 2
  have hV : 0 ≤ V := Finset.sum_nonneg fun _ _ => sq_nonneg _
  have hVr : 0 ≤ Vr := Finset.sum_nonneg fun _ _ => sq_nonneg _
  have hVi : 0 ≤ Vi := Finset.sum_nonneg fun _ _ => sq_nonneg _
  have hVrV : Vr ≤ V :=
    Finset.sum_le_sum fun i _ => re_sq_le_norm_sq (a i)
  have hViV : Vi ≤ V :=
    Finset.sum_le_sum fun i _ => im_sq_le_norm_sq (a i)
  have hReal := real_even_moment_le (fun i => (a i).re) m hm
  have hImag := real_even_moment_le (fun i => (a i).im) m hm
  have hparts :
      (∑ ω : Fin n → Bool, ‖complexSum a ω‖ ^ (2 * m)) ≤
      (2 : ℝ) ^ m *
        ((∑ ω : Fin n → Bool, (realSum (fun i => (a i).re) ω) ^ (2 * m)) +
         (∑ ω : Fin n → Bool, (realSum (fun i => (a i).im) ω) ^ (2 * m))) := by
    calc
      _ ≤ ∑ ω : Fin n → Bool,
          (2 : ℝ) ^ m *
            ((complexSum a ω).re ^ (2 * m) +
             (complexSum a ω).im ^ (2 * m)) := by
          apply Finset.sum_le_sum
          intro ω _
          exact complex_norm_even_pow_le_parts _ _
      _ = _ := by
        simp_rw [complexSum_re, complexSum_im, mul_add]
        rw [Finset.sum_add_distrib, ← Finset.mul_sum, ← Finset.mul_sum]
  have hbase :
      (∑ ω : Fin n → Bool, ‖complexSum a ω‖ ^ (2 * m)) ≤
      (2 : ℝ) ^ (m + 1) * (2 : ℝ) ^ n *
        ((12 * m : ℕ) : ℝ) ^ m * V ^ m := by
    calc
      _ ≤ _ := hparts
      _ ≤ (2 : ℝ) ^ m *
          ((2 : ℝ) ^ n * ((12 * m : ℕ) : ℝ) ^ m * Vr ^ m +
           (2 : ℝ) ^ n * ((12 * m : ℕ) : ℝ) ^ m * Vi ^ m) := by
          gcongr
      _ ≤ (2 : ℝ) ^ m *
          ((2 : ℝ) ^ n * ((12 * m : ℕ) : ℝ) ^ m * V ^ m +
           (2 : ℝ) ^ n * ((12 * m : ℕ) : ℝ) ^ m * V ^ m) := by
          gcongr
      _ = _ := by ring
  have h2m : (2 : ℝ) ≤ 2 ^ m := by
    simpa using pow_le_pow_right₀ (by norm_num : (1 : ℝ) ≤ 2) hm
  have hpow : (2 : ℝ) ^ (m + 1) ≤ 4 ^ m := by
    rw [pow_add, pow_one, show (4 : ℝ) ^ m = 2 ^ m * 2 ^ m by rw [← mul_pow]; norm_num]
    exact mul_le_mul_of_nonneg_left h2m (pow_nonneg (by norm_num) _)
  calc
    _ ≤ (2 : ℝ) ^ (m + 1) * 2 ^ n * ((12 * m : ℕ) : ℝ) ^ m * V ^ m := hbase
    _ ≤ (4 : ℝ) ^ m * 2 ^ n * ((12 * m : ℕ) : ℝ) ^ m * V ^ m := by gcongr
    _ = 2 ^ n * ((48 * m : ℕ) : ℝ) ^ m * (∑ i, ‖a i‖ ^ 2) ^ m := by
      dsimp [V]
      push_cast
      have hpoweq : (4 : ℝ) ^ m * (12 * (m : ℝ)) ^ m = (48 * (m : ℝ)) ^ m := by
        rw [← mul_pow]
        congr 1
        ring
      rw [show (4 : ℝ) ^ m * 2 ^ n * (12 * (m : ℝ)) ^ m =
          2 ^ n * ((4 : ℝ) ^ m * (12 * (m : ℝ)) ^ m) by ring, hpoweq]

/-- The same finite Rademacher bound for any finite coefficient index. -/
theorem complex_even_moment_le_fintype {ι : Type*} [Fintype ι] [DecidableEq ι]
    (a : ι → ℂ) (m : ℕ) (hm : 0 < m) :
    (∑ ω : ι → Bool, ‖∑ i, a i * (sign (ω i) : ℂ)‖ ^ (2 * m)) ≤
      (Fintype.card (ι → Bool) : ℝ) * ((48 * m : ℕ) : ℝ) ^ m *
        (∑ i, ‖a i‖ ^ 2) ^ m := by
  classical
  let e := Fintype.equivFin ι
  let b : Fin (Fintype.card ι) → ℂ := fun j => a (e.symm j)
  have hcoeff : (∑ j, ‖b j‖ ^ 2) = ∑ i, ‖a i‖ ^ 2 := by
    simpa [b, e] using (Equiv.sum_comp (Fintype.equivFin ι) (fun j => ‖a ((Fintype.equivFin ι).symm j)‖ ^ 2)).symm
  have hsum :
      (∑ ω : ι → Bool, ‖∑ i, a i * (sign (ω i) : ℂ)‖ ^ (2 * m)) =
      ∑ ω : Fin (Fintype.card ι) → Bool, ‖complexSum b ω‖ ^ (2 * m) := by
    apply Fintype.sum_equiv (Equiv.arrowCongr e (Equiv.refl Bool))
    intro ω
    unfold complexSum
    apply congrArg (fun z : ℂ => ‖z‖ ^ (2 * m))
    apply Fintype.sum_equiv e
    intro i
    simp [b, e, Equiv.arrowCongr]
  rw [hsum, ← hcoeff]
  convert complex_even_moment_le b m hm using 1
  simp

end Erdos.Research.FiniteComplexKhintchine

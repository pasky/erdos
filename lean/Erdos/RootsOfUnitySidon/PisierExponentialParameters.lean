import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.Algebra.Order.Floor.Semiring
import Mathlib.Tactic

/-!
# Explicit parameters for a finite Pisier thinning step

The thinning construction uses `m = 32 * (n / M)` selected frequencies and
`q = 2m/n`. For a fixed nonnegative exponential-moment constant `C`, one can
choose `M` once so the moment bound is at most `3 ^ (n/M)`, while that integer
still fits under the relation-count threshold `(4/3)^m`.
-/

namespace Erdos.Research.PisierExponentialParameters

private theorem three_pow_thirty_three_le_four_pow_thirty_two :
    3 ^ 33 ≤ 4 ^ 32 := by norm_num

theorem exists_parameters (C : ℝ) (hC : 0 ≤ C) :
    ∃ M : ℕ, 64 ≤ M ∧
      ∀ n : ℕ, M ≤ n →
        let m : ℕ := 32 * (n / M)
        let q : ℝ := (2 * m : ℝ) / n
        q ≤ 1 / 2 ∧
          ∃ K : ℕ, Real.exp (C * n * q ^ 2) ≤ K ∧
            K * 3 ^ m ≤ 4 ^ m := by
  let M : ℕ := 128 + ⌈4096 * C⌉₊
  have hM128 : 128 ≤ M := by dsimp [M]; omega
  have hMC : 4096 * C ≤ (M : ℝ) := by
    have hcnonneg : 0 ≤ 4096 * C := mul_nonneg (by norm_num) hC
    have hc := Nat.le_ceil (4096 * C)
    dsimp [M]
    push_cast
    linarith [hcnonneg]
  refine ⟨M, by omega, ?_⟩
  intro n hn
  let t : ℕ := n / M
  let m : ℕ := 32 * t
  let q : ℝ := (2 * m : ℝ) / n
  have ht : 0 < t := by
    dsimp [t]
    exact Nat.div_pos hn (by omega)
  have hfloor : M * t ≤ n := by
    simpa [t, mul_comm] using Nat.div_mul_le_self n M
  have hnpos : 0 < n := by omega
  have hnreal : (0 : ℝ) < n := by exact_mod_cast hnpos
  have ht_nonneg : (0 : ℝ) ≤ t := Nat.cast_nonneg _
  have hfloorR : (M : ℝ) * t ≤ n := by exact_mod_cast hfloor
  have hmain : 4096 * C * t ≤ (n : ℝ) := by
    have := mul_le_mul_of_nonneg_right hMC ht_nonneg
    nlinarith
  have hq : q = 64 * (t : ℝ) / n := by
    dsimp [q, m]
    push_cast
    ring
  have hqhalf : q ≤ (1 / 2 : ℝ) := by
    rw [hq]
    apply (div_le_iff₀ hnreal).mpr
    have hM128R : (128 : ℝ) ≤ M := by exact_mod_cast hM128
    nlinarith [hfloorR]
  have hexponent : C * (n : ℝ) * q ^ 2 ≤ (t : ℝ) := by
    rw [hq]
    have heq : C * (n : ℝ) * (64 * (t : ℝ) / n) ^ 2 =
        (4096 * C * (t : ℝ) ^ 2) / n := by
      field_simp
      ring
    rw [heq]
    apply (div_le_iff₀ hnreal).mpr
    nlinarith [mul_le_mul_of_nonneg_right hmain ht_nonneg]
  let K : ℕ := 3 ^ t
  have hexpK : Real.exp (C * n * q ^ 2) ≤ (K : ℝ) := by
    calc
      Real.exp (C * n * q ^ 2) ≤ Real.exp (t : ℝ) := Real.exp_le_exp.mpr hexponent
      _ = (Real.exp 1) ^ t := by
        simp [← Real.exp_nat_mul]
      _ ≤ (3 : ℝ) ^ t := by gcongr; exact Real.exp_one_lt_three.le
      _ = (K : ℝ) := by simp [K]
  have hKcard : K * 3 ^ m ≤ 4 ^ m := by
    dsimp [K, m]
    calc
      3 ^ t * 3 ^ (32 * t) = (3 ^ 33) ^ t := by
        rw [← pow_add, ← pow_mul]
        congr 1
        omega
      _ ≤ (4 ^ 32) ^ t :=
        Nat.pow_le_pow_left three_pow_thirty_three_le_four_pow_thirty_two t
      _ = 4 ^ (32 * t) := by rw [pow_mul]
  exact ⟨hqhalf, K, hexpK, hKcard⟩

end Erdos.Research.PisierExponentialParameters

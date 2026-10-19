import Mathlib.Tactic

/-!
# Uniform integer parameters for proportional thinning

The analytic argument chooses one large denominator `M`. For a set of size
`n ≥ M`, take `d = n / M` and a thinning size `m = 32d`. The elementary
inequalities below give room for the fixed-size first-moment and relation
counting steps, and a final extraction denominator `2M`.
-/

namespace Erdos.Research.PisierDensityParameters

theorem density_parameters (M n : ℕ) (hM : 64 ≤ M) (hn : M ≤ n) :
    let d := n / M
    let m := 32 * d
    0 < d ∧ 0 < m ∧ 2 * m ≤ n ∧ 16 * d ≤ m ∧ n ≤ 2 * M * d := by
  dsimp
  have hMpos : 0 < M := by omega
  have hdpos : 0 < n / M := Nat.div_pos hn hMpos
  have hlow : M * (n / M) ≤ n := Nat.mul_div_le n M
  have hhigh : n < M * (n / M + 1) := by
    simpa [mul_comm] using
      (Nat.div_lt_iff_lt_mul hMpos).mp (Nat.lt_succ_self (n / M))
  constructor
  · exact hdpos
  constructor
  · omega
  constructor
  · calc
      2 * (32 * (n / M)) = 64 * (n / M) := by ring
      _ ≤ M * (n / M) := Nat.mul_le_mul_right _ hM
      _ ≤ n := hlow
  constructor
  · omega
  · have htwo : n / M + 1 ≤ 2 * (n / M) := by omega
    have hmul : M * (n / M + 1) ≤ M * (2 * (n / M)) :=
      Nat.mul_le_mul_left _ htwo
    calc
      n ≤ M * (n / M + 1) := hhigh.le
      _ ≤ M * (2 * (n / M)) := hmul
      _ = 2 * M * (n / M) := by ring

end Erdos.Research.PisierDensityParameters

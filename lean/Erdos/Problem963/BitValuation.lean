import Erdos.Problem963.BinaryWords
import Mathlib.NumberTheory.Padics.PadicVal.Basic

/-!
# First binary difference and 2-adic valuation

For bounded natural numbers, the first position where their binary words differ
is the 2-adic valuation of their integer difference.
-/

namespace Erdos.Problem963

private theorem div2_lt_two_pow {n x : ℕ} (hx : x < 2 ^ (n + 1)) :
    Nat.div2 x < 2 ^ n := by
  have hxb : x < 2 * 2 ^ n := by simpa [pow_succ, mul_comm] using hx
  have hd := Nat.bodd_add_div2 x
  omega

private theorem div2_ne_of_bodd_eq {x y : ℕ} (hb : Nat.bodd x = Nat.bodd y)
    (hne : x ≠ y) : Nat.div2 x ≠ Nat.div2 y := by
  intro hd
  apply hne
  calc
    x = Nat.bit (Nat.bodd x) (Nat.div2 x) := (Nat.bit_bodd_div2 x).symm
    _ = Nat.bit (Nat.bodd y) (Nat.div2 y) := by rw [hb, hd]
    _ = y := Nat.bit_bodd_div2 y

private theorem diff_eq_two_mul_div2_diff {x y : ℕ}
    (hb : Nat.bodd x = Nat.bodd y) :
    (x : ℤ) - y = 2 * (((Nat.div2 x : ℕ) : ℤ) - Nat.div2 y) := by
  have hx := Nat.bodd_add_div2 x
  have hy := Nat.bodd_add_div2 y
  cases hbx : Nat.bodd x <;> cases hby : Nat.bodd y <;>
    simp [hbx, hby] at hb hx hy <;> omega

private theorem two_not_dvd_diff_of_bodd_ne {x y : ℕ}
    (hb : Nat.bodd x ≠ Nat.bodd y) :
    ¬(2 : ℤ) ∣ (x : ℤ) - y := by
  intro h
  obtain ⟨k, hk⟩ := h
  have hx := Nat.bodd_add_div2 x
  have hy := Nat.bodd_add_div2 y
  cases hbx : Nat.bodd x <;> cases hby : Nat.bodd y <;>
    simp [hbx, hby] at hb hx hy <;> omega

/-- The first differing binary digit of distinct bounded naturals is the
2-adic valuation of their integer difference. -/
theorem firstDiff_encodeNat_eq_padicValInt :
    ∀ (n x y : ℕ), x < 2 ^ n → y < 2 ^ n → x ≠ y →
      firstDiff n (encodeNat n x) (encodeNat n y) =
        some (padicValInt 2 ((x : ℤ) - y)) := by
  intro n
  induction n with
  | zero =>
      intro x y hx hy _
      simp at hx hy
      omega
  | succ n ih =>
      intro x y hx hy hne
      by_cases hb : Nat.bodd x = Nat.bodd y
      · have hdx := div2_lt_two_pow hx
        have hdy := div2_lt_two_pow hy
        have hdn := div2_ne_of_bodd_eq hb hne
        have htail : (((Nat.div2 x : ℕ) : ℤ) - Nat.div2 y) ≠ 0 := by
          exact sub_ne_zero.mpr (by exact_mod_cast hdn)
        have hval : padicValInt 2 ((x : ℤ) - y) =
            padicValInt 2 (((Nat.div2 x : ℕ) : ℤ) - Nat.div2 y) + 1 := by
          rw [diff_eq_two_mul_div2_diff hb, padicValInt.mul (by norm_num) htail]
          have htwo : padicValInt 2 (2 : ℤ) = 1 :=
            padicValInt.self (by norm_num)
          rw [htwo]
          omega
        rw [firstDiff_encodeNat_of_bodd_eq hb, ih _ _ hdx hdy hdn, hval]
        rfl
      · have hval : padicValInt 2 ((x : ℤ) - y) = 0 :=
          padicValInt.eq_zero_of_not_dvd (two_not_dvd_diff_of_bodd_ne hb)
        rw [firstDiff_encodeNat_of_bodd_ne hb, hval]

end Erdos.Problem963

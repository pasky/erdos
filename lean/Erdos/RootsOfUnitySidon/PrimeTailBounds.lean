import Mathlib.NumberTheory.Chebyshev
import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.NumberTheory.Harmonic.EulerMascheroni
import Mathlib.NumberTheory.Harmonic.Bounds
import Mathlib.Analysis.SpecialFunctions.Stirling
import Mathlib.Analysis.PSeries
import Mathlib.Tactic

/-!
# Elementary bounds for prime-tail tensor factors

This module develops the prime sum and tensor-factor estimates
used by the prime-tail argument for roots of unity.
-/

namespace Erdos.Research.PrimeTailBounds

/-- The primes in the half-open dyadic interval `(N, 2N]`. -/
def dyadicPrimes (N : ℕ) : Finset ℕ :=
  (Finset.Ioc N (2 * N)).filter Nat.Prime

/-- Chebyshev's elementary bound controls each dyadic block of prime reciprocals.
The constant is explicit and independent of `N`. -/
theorem sum_inv_dyadicPrimes_le (N : ℕ) (hN : 2 ≤ N) :
    (∑ p ∈ dyadicPrimes N, (1 / (p : ℝ))) ≤
      2 * Real.log 4 / Real.log (N : ℝ) := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast (by omega : 0 < N)
  have hNgt : (1 : ℝ) < N := by exact_mod_cast (by omega : 1 < N)
  have hlogN : 0 < Real.log (N : ℝ) := Real.log_pos hNgt
  have hdenom : 0 < (N : ℝ) * Real.log N := mul_pos hNpos hlogN
  have hpoint : ∀ p ∈ dyadicPrimes N,
      (1 / (p : ℝ)) ≤ Real.log p / ((N : ℝ) * Real.log N) := by
    intro p hp
    have hpI : N < p ∧ p ≤ 2 * N :=
      (Finset.mem_Ioc.mp (Finset.mem_filter.mp hp).1)
    have hNp : (N : ℝ) ≤ p := by exact_mod_cast hpI.1.le
    have hlog : Real.log (N : ℝ) ≤ Real.log (p : ℝ) :=
      Real.log_le_log hNpos hNp
    have hle : (1 : ℝ) / p ≤ 1 / N :=
      one_div_le_one_div_of_le hNpos hNp
    have hle' : (1 : ℝ) / N ≤ Real.log p / (N * Real.log N) := by
      apply (div_le_div_iff₀ hNpos hdenom).2
      nlinarith
    exact hle.trans hle'
  have hsub : dyadicPrimes N ⊆ Nat.primesLE (2 * N) := by
    intro p hp
    rcases Finset.mem_filter.mp hp with ⟨hpI, hprime⟩
    exact Nat.mem_primesLE.mpr ⟨(Finset.mem_Ioc.mp hpI).2, hprime⟩
  have hlogs : (∑ p ∈ dyadicPrimes N, Real.log (p : ℝ)) ≤
      (∑ p ∈ Nat.primesLE (2 * N), Real.log (p : ℝ)) := by
    apply Finset.sum_le_sum_of_subset_of_nonneg hsub
    intro p hp _
    exact Real.log_nonneg (by exact_mod_cast (show 1 ≤ p by
      have := Nat.two_le_of_mem_primesLE hp
      omega))
  calc
    (∑ p ∈ dyadicPrimes N, (1 / (p : ℝ))) ≤
        ∑ p ∈ dyadicPrimes N, Real.log p / ((N : ℝ) * Real.log N) :=
      Finset.sum_le_sum hpoint
    _ = (∑ p ∈ dyadicPrimes N, Real.log (p : ℝ)) /
        ((N : ℝ) * Real.log N) := by rw [Finset.sum_div]
    _ ≤ (∑ p ∈ Nat.primesLE (2 * N), Real.log (p : ℝ)) /
        ((N : ℝ) * Real.log N) :=
      div_le_div_of_nonneg_right hlogs hdenom.le
    _ = Chebyshev.theta (2 * N : ℕ) / ((N : ℝ) * Real.log N) := by
      rw [Chebyshev.theta_eq_sum_primesLE_log]
    _ ≤ (Real.log 4 * (2 * N : ℕ)) / ((N : ℝ) * Real.log N) := by
      exact div_le_div_of_nonneg_right
        (Chebyshev.theta_le_log4_mul_x (by positivity)) hdenom.le
    _ = 2 * Real.log 4 / Real.log (N : ℝ) := by
      push_cast
      field_simp

/-- The same dyadic estimate with an arbitrary nonnegative logarithmic weight.
For positive `β`, these block bounds are summable along dyadic scales. -/
theorem sum_inv_log_rpow_dyadicPrimes_le (N : ℕ) (hN : 2 ≤ N)
    (β : ℝ) (hβ : 0 ≤ β) :
    (∑ p ∈ dyadicPrimes N,
      (1 / (p : ℝ)) / (Real.log (p : ℝ)) ^ β) ≤
      (2 * Real.log 4 / Real.log (N : ℝ)) /
        (Real.log (N : ℝ)) ^ β := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast (by omega : 0 < N)
  have hNgt : (1 : ℝ) < N := by exact_mod_cast (by omega : 1 < N)
  have hlogN : 0 < Real.log (N : ℝ) := Real.log_pos hNgt
  have hrpowN : 0 < (Real.log (N : ℝ)) ^ β := Real.rpow_pos_of_pos hlogN _
  have hpoint : ∀ p ∈ dyadicPrimes N,
      (1 / (p : ℝ)) / (Real.log (p : ℝ)) ^ β ≤
        (1 / (p : ℝ)) / (Real.log (N : ℝ)) ^ β := by
    intro p hp
    have hpI : N < p ∧ p ≤ 2 * N :=
      Finset.mem_Ioc.mp (Finset.mem_filter.mp hp).1
    have hNp : (N : ℝ) ≤ p := by exact_mod_cast hpI.1.le
    have hlog : Real.log (N : ℝ) ≤ Real.log (p : ℝ) :=
      Real.log_le_log hNpos hNp
    have hpower : (Real.log (N : ℝ)) ^ β ≤
        (Real.log (p : ℝ)) ^ β :=
      Real.rpow_le_rpow hlogN.le hlog hβ
    exact div_le_div_of_nonneg_left (by positivity) hrpowN hpower
  calc
    (∑ p ∈ dyadicPrimes N,
        (1 / (p : ℝ)) / (Real.log (p : ℝ)) ^ β) ≤
        ∑ p ∈ dyadicPrimes N,
          (1 / (p : ℝ)) / (Real.log (N : ℝ)) ^ β :=
      Finset.sum_le_sum hpoint
    _ = (∑ p ∈ dyadicPrimes N, (1 / (p : ℝ))) /
        (Real.log (N : ℝ)) ^ β := by rw [Finset.sum_div]
    _ ≤ (2 * Real.log 4 / Real.log (N : ℝ)) /
        (Real.log (N : ℝ)) ^ β :=
      div_le_div_of_nonneg_right (sum_inv_dyadicPrimes_le N hN) hrpowN.le

/-- The factorial form of the von Mangoldt divisor identity. This is the
starting point for the sharp estimate `∑_{p≤x} log p / p = log x + O(1)`. -/
theorem log_factorial_eq_sum_vonMangoldt_div (N : ℕ) :
    Real.log (N.factorial : ℝ) =
      ∑ n ∈ Finset.Ioc 0 N,
        ArithmeticFunction.vonMangoldt n * (N / n : ℕ) := by
  have hset : Finset.Ioc 0 N = Finset.Ico 1 (N + 1) := by
    ext n
    simp only [Finset.mem_Ioc, Finset.mem_Ico]
    omega
  have hprod : (∏ n ∈ Finset.Ioc 0 N, (n : ℝ)) = (N.factorial : ℝ) := by
    calc
      (∏ n ∈ Finset.Ioc 0 N, (n : ℝ)) =
          ((∏ n ∈ Finset.Ioc 0 N, n : ℕ) : ℝ) :=
        (Finset.prod_natCast (Finset.Ioc 0 N) id).symm
      _ = (N.factorial : ℝ) := by rw [hset, Finset.prod_Ico_id_eq_factorial]
  have hlog : Real.log (N.factorial : ℝ) =
      ∑ n ∈ Finset.Ioc 0 N, Real.log (n : ℝ) := by
    rw [← hprod]
    exact Real.log_prod (fun n hn => by
      exact_mod_cast (Finset.mem_Ioc.mp hn).1.ne')
  calc
    Real.log (N.factorial : ℝ) =
        ∑ n ∈ Finset.Ioc 0 N, Real.log (n : ℝ) := hlog
    _ = ∑ n ∈ Finset.Ioc 0 N,
        ArithmeticFunction.vonMangoldt n * (N / n : ℕ) := by
      simpa only [ArithmeticFunction.vonMangoldt_mul_zeta,
        ArithmeticFunction.log_apply] using
          (ArithmeticFunction.sum_Ioc_mul_zeta_eq_sum
            ArithmeticFunction.vonMangoldt N)

/-- The real quotient lies within one of the natural-number quotient. -/
theorem real_div_lt_nat_div_add_one (N n : ℕ) (hn : 0 < n) :
    (N : ℝ) / n < ((N / n : ℕ) : ℝ) + 1 := by
  apply (div_lt_iff₀ (by exact_mod_cast hn)).2
  have h : N < (N / n + 1) * n := by
    simpa [add_mul] using (Nat.lt_div_mul_add hn : N < N / n * n + n)
  exact_mod_cast h

/-- The rounded factorial sum differs from the von Mangoldt harmonic sum
by at most the Chebyshev `ψ` function. -/
theorem mangoldt_harmonic_factorial_sandwich (N : ℕ) :
    Real.log (N.factorial : ℝ) ≤
      (N : ℝ) *
        (∑ n ∈ Finset.Ioc 0 N, ArithmeticFunction.vonMangoldt n / (n : ℝ)) ∧
    (N : ℝ) *
        (∑ n ∈ Finset.Ioc 0 N, ArithmeticFunction.vonMangoldt n / (n : ℝ)) ≤
      Real.log (N.factorial : ℝ) + Chebyshev.psi N := by
  have hlow :
      (∑ n ∈ Finset.Ioc 0 N,
        ArithmeticFunction.vonMangoldt n * (N / n : ℕ)) ≤
      (N : ℝ) *
        (∑ n ∈ Finset.Ioc 0 N,
          ArithmeticFunction.vonMangoldt n / (n : ℝ)) := by
    rw [Finset.mul_sum]
    apply Finset.sum_le_sum
    intro n hn
    have hfloor : ((N / n : ℕ) : ℝ) ≤ (N : ℝ) / n := Nat.cast_div_le
    have hΛ : 0 ≤ ArithmeticFunction.vonMangoldt n :=
      ArithmeticFunction.vonMangoldt_nonneg
    calc
      ArithmeticFunction.vonMangoldt n * (N / n : ℕ) ≤
          ArithmeticFunction.vonMangoldt n * ((N : ℝ) / n) :=
        mul_le_mul_of_nonneg_left hfloor hΛ
      _ = (N : ℝ) * (ArithmeticFunction.vonMangoldt n / (n : ℝ)) := by ring
  have hupp :
      (N : ℝ) *
        (∑ n ∈ Finset.Ioc 0 N,
          ArithmeticFunction.vonMangoldt n / (n : ℝ)) ≤
      (∑ n ∈ Finset.Ioc 0 N,
        ArithmeticFunction.vonMangoldt n * (N / n : ℕ)) + Chebyshev.psi N := by
    rw [Finset.mul_sum, Chebyshev.psi, Nat.floor_natCast,
      ← Finset.sum_add_distrib]
    apply Finset.sum_le_sum
    intro n hn
    have hnpos : 0 < n := (Finset.mem_Ioc.mp hn).1
    have hquot := (real_div_lt_nat_div_add_one N n hnpos).le
    have hΛ : 0 ≤ ArithmeticFunction.vonMangoldt n :=
      ArithmeticFunction.vonMangoldt_nonneg
    calc
      (N : ℝ) * (ArithmeticFunction.vonMangoldt n / (n : ℝ)) =
          ArithmeticFunction.vonMangoldt n * ((N : ℝ) / n) := by ring
      _ ≤ ArithmeticFunction.vonMangoldt n * (((N / n : ℕ) : ℝ) + 1) :=
        mul_le_mul_of_nonneg_left hquot hΛ
      _ = ArithmeticFunction.vonMangoldt n * (N / n : ℕ) +
          ArithmeticFunction.vonMangoldt n := by ring
  rw [log_factorial_eq_sum_vonMangoldt_div]
  exact ⟨hlow, hupp⟩

/-- Coarse factorial bounds with the sharp coefficient on `N log N`. -/
theorem log_factorial_bounds (N : ℕ) (hN : 2 ≤ N) :
    (N : ℝ) * Real.log N - N ≤ Real.log (N.factorial : ℝ) ∧
    Real.log (N.factorial : ℝ) ≤ (N : ℝ) * Real.log N := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast (by omega : 0 < N)
  have hlogN : 0 ≤ Real.log (N : ℝ) :=
    Real.log_nonneg (by exact_mod_cast (by omega : 1 ≤ N))
  have hlogpi : 0 ≤ Real.log (2 * Real.pi) := by
    apply Real.log_nonneg
    have := Real.two_le_pi
    linarith
  have hstirling := Stirling.le_log_factorial_stirling
    (n := N) (by omega : N ≠ 0)
  constructor
  · nlinarith
  · calc
      Real.log (N.factorial : ℝ) ≤ Real.log ((N : ℝ) ^ N) :=
        Real.log_le_log (by positivity) (by exact_mod_cast Nat.factorial_le_pow N)
      _ = (N : ℝ) * Real.log N := by rw [Real.log_pow]

/-- The weighted von Mangoldt sum has the correct main term up to an
absolute elementary constant. The non-prime prime-power correction is handled
separately below. -/
theorem mangoldt_harmonic_log_bounds (N : ℕ) (hN : 2 ≤ N) :
    Real.log (N : ℝ) - 1 ≤
      (∑ n ∈ Finset.Ioc 0 N,
        ArithmeticFunction.vonMangoldt n / (n : ℝ)) ∧
    (∑ n ∈ Finset.Ioc 0 N,
        ArithmeticFunction.vonMangoldt n / (n : ℝ)) ≤
      Real.log (N : ℝ) + Real.log 4 + 4 := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast (by omega : 0 < N)
  obtain ⟨hfactlow, hfactupp⟩ := log_factorial_bounds N hN
  obtain ⟨hlow, hupp⟩ := mangoldt_harmonic_factorial_sandwich N
  have hpsi : Chebyshev.psi (N : ℝ) ≤ (Real.log 4 + 4) * N :=
    Chebyshev.psi_le_const_mul_self hNpos.le
  constructor
  · apply le_of_mul_le_mul_left _ hNpos
    nlinarith
  · apply le_of_mul_le_mul_left _ hNpos
    nlinarith

/-- A finite prime-logarithm sum, equal to `∑_{p≤N} log p / p`. -/
noncomputable def primeLogHarmonic (N : ℕ) : ℝ :=
  ∑ n ∈ Finset.Ioc 0 N,
    if n.Prime then Real.log (n : ℝ) / n else 0

/-- The omitted higher-prime-power contribution. -/
noncomputable def nonprimeVonMangoldtMass (N : ℕ) : ℝ :=
  ∑ n ∈ Finset.Ioc 0 N,
    (if n.Prime then 0 else ArithmeticFunction.vonMangoldt n) / (n : ℝ)

theorem nonprimeVonMangoldtMass_nonneg (N : ℕ) :
    0 ≤ nonprimeVonMangoldtMass N := by
  unfold nonprimeVonMangoldtMass
  apply Finset.sum_nonneg
  intro n hn
  by_cases hp : n.Prime
  · simp [hp]
  · simp only [hp, ↓reduceIte]
    exact div_nonneg ArithmeticFunction.vonMangoldt_nonneg (Nat.cast_nonneg _)

/-- The von Mangoldt harmonic sum separates into primes and higher prime
powers. -/
theorem mangoldt_harmonic_eq_primeLogHarmonic_add (N : ℕ) :
    (∑ n ∈ Finset.Ioc 0 N,
        ArithmeticFunction.vonMangoldt n / (n : ℝ)) =
      primeLogHarmonic N + nonprimeVonMangoldtMass N := by
  unfold primeLogHarmonic nonprimeVonMangoldtMass
  rw [← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro n hn
  by_cases hp : n.Prime
  · simp [hp, ArithmeticFunction.vonMangoldt_apply_prime hp]
  · simp [hp]

/-- On an interval above `a`, the reciprocal-weighted contribution of higher
prime powers is bounded by the global Chebyshev `ψ-θ` mass divided by `a`. -/
theorem nonprime_vonMangoldt_Ioc_le_psi_sub_theta_div (a b : ℕ)
    (ha : 0 < a) (_hab : a ≤ b) :
    (∑ n ∈ Finset.Ioc a b,
      (if n.Prime then 0 else ArithmeticFunction.vonMangoldt n) / (n : ℝ)) ≤
      (Chebyshev.psi b - Chebyshev.theta b) / (a : ℝ) := by
  let f : ℕ → ℝ := fun n => if n.Prime then 0 else ArithmeticFunction.vonMangoldt n
  have haR : (0 : ℝ) < a := by exact_mod_cast ha
  have hf_nonneg (n : ℕ) : 0 ≤ f n := by
    dsimp [f]
    by_cases hp : n.Prime
    · simp [hp]
    · simp [hp, ArithmeticFunction.vonMangoldt_nonneg (n := n)]
  have hpoint : ∀ n ∈ Finset.Ioc a b, f n / (n : ℝ) ≤ f n / (a : ℝ) := by
    intro n hn
    have han : (a : ℝ) ≤ n := by exact_mod_cast (Finset.mem_Ioc.mp hn).1.le
    exact div_le_div_of_nonneg_left (hf_nonneg n) haR han
  have hsub : Finset.Ioc a b ⊆ Finset.Ioc 0 b := by
    intro n hn
    exact Finset.mem_Ioc.mpr ⟨ha.trans (Finset.mem_Ioc.mp hn).1,
      (Finset.mem_Ioc.mp hn).2⟩
  have hfull : (∑ n ∈ Finset.Ioc 0 b, f n) =
      Chebyshev.psi b - Chebyshev.theta b := by
    rw [Chebyshev.psi_sub_theta_eq_sum_not_prime, Nat.floor_natCast,
      Finset.sum_filter]
    apply Finset.sum_congr rfl
    intro n hn
    by_cases hp : n.Prime <;> simp [f, hp]
  calc
    (∑ n ∈ Finset.Ioc a b,
        (if n.Prime then 0 else ArithmeticFunction.vonMangoldt n) / (n : ℝ)) =
        ∑ n ∈ Finset.Ioc a b, f n / (n : ℝ) := rfl
    _ ≤ ∑ n ∈ Finset.Ioc a b, f n / (a : ℝ) := Finset.sum_le_sum hpoint
    _ = (∑ n ∈ Finset.Ioc a b, f n) / (a : ℝ) := by rw [Finset.sum_div]
    _ ≤ (∑ n ∈ Finset.Ioc 0 b, f n) / (a : ℝ) := by
      apply div_le_div_of_nonneg_right _ haR.le
      exact Finset.sum_le_sum_of_subset_of_nonneg hsub (fun n _ _ => hf_nonneg n)
    _ = (Chebyshev.psi b - Chebyshev.theta b) / (a : ℝ) := by rw [hfull]

/-- The preceding interval estimate with Mathlib's explicit bound for
`ψ-θ`. -/
theorem nonprime_vonMangoldt_Ioc_le_sqrt_log (a b : ℕ)
    (ha : 0 < a) (hb : 1 ≤ b) (hab : a ≤ b) :
    (∑ n ∈ Finset.Ioc a b,
      (if n.Prime then 0 else ArithmeticFunction.vonMangoldt n) / (n : ℝ)) ≤
      2 * Real.sqrt (b : ℝ) * Real.log (b : ℝ) / (a : ℝ) := by
  calc
    _ ≤ (Chebyshev.psi b - Chebyshev.theta b) / (a : ℝ) :=
      nonprime_vonMangoldt_Ioc_le_psi_sub_theta_div a b ha hab
    _ ≤ 2 * Real.sqrt (b : ℝ) * Real.log (b : ℝ) / (a : ℝ) := by
      apply div_le_div_of_nonneg_right _ (by exact_mod_cast ha.le)
      exact Chebyshev.psi_sub_theta_le (by exact_mod_cast hb)

/-- The fourth-power blocks used below have square endpoints. -/
private theorem four_pow_eq_two_pow_sq (k : ℕ) :
    (4 ^ k : ℕ) = (2 ^ k) ^ 2 := by
  calc
    4 ^ k = (2 * 2) ^ k := by norm_num
    _ = 2 ^ k * 2 ^ k := by rw [mul_pow]
    _ = (2 ^ k) ^ 2 := by ring

/-- A square root of a power of four is a power of two. -/
private theorem sqrt_four_pow (k : ℕ) :
    Real.sqrt ((4 ^ k : ℕ) : ℝ) = (2 : ℝ) ^ k := by
  have hpow := four_pow_eq_two_pow_sq k
  rw [hpow]
  push_cast
  exact Real.sqrt_sq (by positivity)

/-- Let `C` bound `ψ(x)-θ(x)` by `C√x`. Then the non-prime von Mangoldt
reciprocal sum in the fourth-power block `(4^k,4^(k+1)]` decays geometrically. -/
theorem nonprime_vonMangoldt_four_block_le (C : ℝ)
    (hC : ∀ x : ℝ,
      Chebyshev.psi x - Chebyshev.theta x ≤ C * Real.sqrt x)
    (k : ℕ) :
    (∑ n ∈ Finset.Ioc (4 ^ k : ℕ) (4 ^ (k + 1) : ℕ),
      (if n.Prime then 0 else ArithmeticFunction.vonMangoldt n) / (n : ℝ)) ≤
      2 * C * (1 / 2 : ℝ) ^ k := by
  have ha : 0 < 4 ^ k := by positivity
  have hab : 4 ^ k ≤ 4 ^ (k + 1) := by
    rw [pow_succ]
    omega
  have haR : (0 : ℝ) < (4 ^ k : ℕ) := by exact_mod_cast ha
  have hpowR : (((4 ^ k : ℕ) : ℝ)) = ((2 : ℝ) ^ k) ^ 2 := by
    rw [four_pow_eq_two_pow_sq]
    push_cast
    rfl
  calc
    (∑ n ∈ Finset.Ioc (4 ^ k : ℕ) (4 ^ (k + 1) : ℕ),
        (if n.Prime then 0 else ArithmeticFunction.vonMangoldt n) / (n : ℝ)) ≤
        (Chebyshev.psi (4 ^ (k + 1) : ℕ) -
          Chebyshev.theta (4 ^ (k + 1) : ℕ)) / (4 ^ k : ℕ) :=
      nonprime_vonMangoldt_Ioc_le_psi_sub_theta_div _ _ ha hab
    _ ≤ C * Real.sqrt ((4 ^ (k + 1) : ℕ) : ℝ) / (4 ^ k : ℕ) :=
      div_le_div_of_nonneg_right (hC _) haR.le
    _ = C * (2 : ℝ) ^ (k + 1) / (4 ^ k : ℕ) := by
      rw [sqrt_four_pow]
    _ = 2 * C * (1 / 2 : ℝ) ^ k := by
      rw [hpowR, pow_succ]
      have htwo : (2 : ℝ) ^ k ≠ 0 := by positivity
      rw [one_div_pow]
      field_simp

/-- The higher-prime-power correction to Mertens' first estimate is uniformly
bounded. The proof splits the natural numbers into fourth-power blocks and
sums their geometric Chebyshev bounds. -/
theorem exists_uniform_nonprimeVonMangoldtMass_bound :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ N : ℕ, nonprimeVonMangoldtMass N ≤ C := by
  obtain ⟨C, hC⟩ := Chebyshev.psi_sub_theta_le_mul_sqrt
  let C₀ : ℝ := max C 0
  have hC₀_nonneg : 0 ≤ C₀ := le_max_right C 0
  have hC₀ (x : ℝ) :
      Chebyshev.psi x - Chebyshev.theta x ≤ C₀ * Real.sqrt x := by
    exact (hC x).trans
      (mul_le_mul_of_nonneg_right (le_max_left C 0) (Real.sqrt_nonneg x))
  let f : ℕ → ℝ := fun n =>
    (if n.Prime then 0 else ArithmeticFunction.vonMangoldt n) / (n : ℝ)
  have hf_nonneg (n : ℕ) : 0 ≤ f n := by
    dsimp [f]
    by_cases hp : n.Prime
    · simp [hp]
    · simp only [hp, ↓reduceIte]
      exact div_nonneg ArithmeticFunction.vonMangoldt_nonneg (Nat.cast_nonneg _)
  have hbound (k : ℕ) :
      (∑ n ∈ Finset.Ioc 0 (4 ^ k), f n) ≤
        2 * C₀ * ∑ j ∈ Finset.range k, (1 / 2 : ℝ) ^ j := by
    induction k with
    | zero =>
        have hIoc : Finset.Ioc 0 1 = ({1} : Finset ℕ) := by
          ext n
          simp only [Finset.mem_Ioc, Finset.mem_singleton]
          omega
        simp [hIoc, f, ArithmeticFunction.vonMangoldt_apply_one]
    | succ k ih =>
        have hpow : 4 ^ k ≤ 4 ^ (k + 1) := by
          rw [pow_succ]
          omega
        calc
          (∑ n ∈ Finset.Ioc 0 (4 ^ (k + 1)), f n) =
              (∑ n ∈ Finset.Ioc 0 (4 ^ k), f n) +
                (∑ n ∈ Finset.Ioc (4 ^ k) (4 ^ (k + 1)), f n) :=
            (Finset.sum_Ioc_consecutive f (Nat.zero_le _) hpow).symm
          _ ≤ 2 * C₀ * (∑ j ∈ Finset.range k, (1 / 2 : ℝ) ^ j) +
                2 * C₀ * (1 / 2 : ℝ) ^ k :=
            add_le_add ih (nonprime_vonMangoldt_four_block_le C₀ hC₀ k)
          _ = 2 * C₀ * ∑ j ∈ Finset.range (k + 1), (1 / 2 : ℝ) ^ j := by
            rw [Finset.sum_range_succ]
            ring
  refine ⟨4 * C₀, mul_nonneg (by norm_num) hC₀_nonneg, ?_⟩
  intro N
  have hk : N < 4 ^ N := Nat.lt_pow_self (by norm_num : 1 < 4)
  have hsub : Finset.Ioc 0 N ⊆ Finset.Ioc 0 (4 ^ N) := by
    intro n hn
    exact Finset.mem_Ioc.mpr ⟨(Finset.mem_Ioc.mp hn).1,
      (Finset.mem_Ioc.mp hn).2.trans hk.le⟩
  have hmono : (∑ n ∈ Finset.Ioc 0 N, f n) ≤
      (∑ n ∈ Finset.Ioc 0 (4 ^ N), f n) :=
    Finset.sum_le_sum_of_subset_of_nonneg hsub (fun n _ _ => hf_nonneg n)
  change (∑ n ∈ Finset.Ioc 0 N, f n) ≤ 4 * C₀
  calc
    _ ≤ (∑ n ∈ Finset.Ioc 0 (4 ^ N), f n) := hmono
    _ ≤ 2 * C₀ * ∑ j ∈ Finset.range N, (1 / 2 : ℝ) ^ j := hbound N
    _ ≤ 2 * C₀ * 2 := by
      exact mul_le_mul_of_nonneg_left (sum_geometric_two_le N) (by positivity)
    _ = 4 * C₀ := by ring

/-- Mertens' first estimate: the prime sum `∑_{p≤N} log p/p` differs from
`log N` by a uniform additive constant. The constant is obtained from the
elementary Chebyshev bound and a geometric series, with no prime number theorem
or unproved prime-tail hypothesis. -/
theorem exists_primeLogHarmonic_log_bound :
    ∃ K : ℝ, 0 ≤ K ∧ ∀ N : ℕ, 2 ≤ N →
      |primeLogHarmonic N - Real.log (N : ℝ)| ≤ K := by
  obtain ⟨C, hC_nonneg, hC⟩ := exists_uniform_nonprimeVonMangoldtMass_bound
  have hlog4 : 0 ≤ Real.log 4 := Real.log_nonneg (by norm_num)
  refine ⟨C + Real.log 4 + 5, by linarith, ?_⟩
  intro N hN
  obtain ⟨hlow, hupp⟩ := mangoldt_harmonic_log_bounds N hN
  rw [mangoldt_harmonic_eq_primeLogHarmonic_add] at hlow hupp
  have hDle := hC N
  have hDnonneg := nonprimeVonMangoldtMass_nonneg N
  apply abs_le.mpr
  constructor <;> linarith

/-- The finite reciprocal-prime sum `∑_{p≤N} 1/p`. -/
noncomputable def primeReciprocalSum (N : ℕ) : ℝ :=
  ∑ n ∈ Finset.Ioc 0 N, if n.Prime then 1 / (n : ℝ) else 0

/-- The logarithm-weighted sum on an interval is at most its largest logarithm
times the reciprocal-prime sum. Combined with the sharp bound for
`primeLogHarmonic`, this supplies a positive reciprocal-prime mass on sufficiently
wide multiplicative intervals. -/
theorem primeLogHarmonic_sub_le_log_mul_primeReciprocalSum_sub
    (a b : ℕ) (hab : a ≤ b) :
    primeLogHarmonic b - primeLogHarmonic a ≤
      Real.log (b : ℝ) * (primeReciprocalSum b - primeReciprocalSum a) := by
  have hlogdiff : primeLogHarmonic b - primeLogHarmonic a =
      ∑ n ∈ Finset.Ioc a b,
        if n.Prime then Real.log (n : ℝ) / n else 0 := by
    have hsplit := Finset.sum_Ioc_consecutive
      (fun n : ℕ => if n.Prime then Real.log (n : ℝ) / n else 0)
      (Nat.zero_le a) hab
    dsimp [primeLogHarmonic]
    linarith
  have hrecipdiff : primeReciprocalSum b - primeReciprocalSum a =
      ∑ n ∈ Finset.Ioc a b, if n.Prime then 1 / (n : ℝ) else 0 := by
    have hsplit := Finset.sum_Ioc_consecutive
      (fun n : ℕ => if n.Prime then 1 / (n : ℝ) else 0)
      (Nat.zero_le a) hab
    dsimp [primeReciprocalSum]
    linarith
  rw [hlogdiff, hrecipdiff, Finset.mul_sum]
  apply Finset.sum_le_sum
  intro n hn
  by_cases hp : n.Prime
  · have hnpos : (0 : ℝ) < n := by
      exact_mod_cast hp.pos
    have hnb : (n : ℝ) ≤ b := by
      exact_mod_cast (Finset.mem_Ioc.mp hn).2
    have hlog : Real.log (n : ℝ) ≤ Real.log (b : ℝ) :=
      Real.log_le_log hnpos hnb
    simp only [hp, ↓reduceIte]
    rw [div_eq_mul_inv, div_eq_mul_inv]
    simpa only [one_mul] using
      mul_le_mul_of_nonneg_right hlog (inv_nonneg.mpr hnpos.le)
  · simp [hp]

/-- A uniform additive bound for the prime logarithm sum gives a quantitative
lower bound for reciprocal-prime mass on every interval. -/
theorem primeReciprocalSum_sub_lower_of_primeLogHarmonic_bound
    (K : ℝ)
    (hK : ∀ N : ℕ, 2 ≤ N →
      |primeLogHarmonic N - Real.log (N : ℝ)| ≤ K)
    (a b : ℕ) (ha : 2 ≤ a) (hab : a ≤ b) :
    (Real.log (b : ℝ) - Real.log (a : ℝ) - 2 * K) /
        Real.log (b : ℝ) ≤
      primeReciprocalSum b - primeReciprocalSum a := by
  have hb : 2 ≤ b := ha.trans hab
  have hlogbpos : 0 < Real.log (b : ℝ) :=
    Real.log_pos (by exact_mod_cast (by omega : 1 < b))
  have hAupper := (abs_le.mp (hK a ha)).2
  have hAlower := (abs_le.mp (hK b hb)).1
  have hrelation :=
    primeLogHarmonic_sub_le_log_mul_primeReciprocalSum_sub a b hab
  apply (div_le_iff₀ hlogbpos).2
  linarith

/-- A fixed multiplicative interval carries at least one reciprocal-logarithm
unit of prime mass once its ratio is large enough for the `A`-error constant. -/
theorem primeReciprocalSum_wide_block_lower
    (K : ℝ)
    (hK : ∀ N : ℕ, 2 ≤ N →
      |primeLogHarmonic N - Real.log (N : ℝ)| ≤ K)
    (R a : ℕ) (hR : 2 ≤ R)
    (hlogR : 2 * K + 1 ≤ Real.log (R : ℝ)) (ha : 2 ≤ a) :
    1 / Real.log (R * a : ℕ) ≤
      primeReciprocalSum (R * a) - primeReciprocalSum a := by
  have hab : a ≤ R * a := by
    calc
      a = 1 * a := by simp
      _ ≤ R * a := Nat.mul_le_mul_right a (by omega)
  have hb : 2 ≤ R * a := ha.trans hab
  have hlogbpos : 0 < Real.log (R * a : ℕ) :=
    Real.log_pos (by exact_mod_cast (by omega : 1 < R * a))
  have hlogmul : Real.log (R * a : ℕ) =
      Real.log (R : ℝ) + Real.log (a : ℝ) := by
    rw [Nat.cast_mul, Real.log_mul]
    · exact_mod_cast (by omega : R ≠ 0)
    · exact_mod_cast (by omega : a ≠ 0)
  have hnum : 1 ≤ Real.log (R * a : ℕ) - Real.log (a : ℝ) - 2 * K := by
    rw [hlogmul]
    linarith
  calc
    1 / Real.log (R * a : ℕ) ≤
        (Real.log (R * a : ℕ) - Real.log (a : ℝ) - 2 * K) /
          Real.log (R * a : ℕ) :=
      div_le_div_of_nonneg_right hnum hlogbpos.le
    _ ≤ primeReciprocalSum (R * a) - primeReciprocalSum a :=
      primeReciprocalSum_sub_lower_of_primeLogHarmonic_bound K hK a (R * a) ha hab

/-- A uniform strict improvement on the harmonic-number bound. It is enough to
create the logarithmic saving in the tensor-factor product. -/
theorem harmonic_pred_sub_one_le_log_sub_third (p : ℕ) (hp : 7 ≤ p) :
    ((harmonic (p - 1) : ℚ) : ℝ) - 1 ≤
      Real.log (p : ℝ) - 1 / 3 := by
  have hn : 6 ≤ p - 1 := by omega
  have hn0 : p - 1 ≠ 0 := by omega
  have hanti := Real.strictAnti_eulerMascheroniSeq'.antitone hn
  have hgamma : ((harmonic (p - 1) : ℚ) : ℝ) -
      Real.log (p - 1 : ℕ) < 2 / 3 := by
    have h := hanti.trans_lt Real.eulerMascheroniSeq'_six_lt_two_thirds
    simpa [Real.eulerMascheroniSeq', hn0] using h
  have hpredpos : (0 : ℝ) < (p - 1 : ℕ) := by
    exact_mod_cast (by omega : 0 < p - 1)
  have hlog : Real.log (p - 1 : ℕ) ≤ Real.log (p : ℝ) :=
    Real.log_le_log hpredpos (by exact_mod_cast (Nat.sub_le p 1))
  linarith

/-- The loss multiplier contributed by an odd prime tensor side. -/
noncomputable def tensorFactor (p : ℕ) : ℝ :=
  ((p : ℝ) - 1 + ((harmonic (p - 1) : ℚ) : ℝ)) / p

/-- The prime-side loss multipliers are strictly positive. -/
theorem tensorFactor_pos (p : ℕ) (hp : 7 ≤ p) : 0 < tensorFactor p := by
  have hpR : (0 : ℝ) < p := by exact_mod_cast (by omega : 0 < p)
  have hH : (0 : ℝ) ≤ ((harmonic (p - 1) : ℚ) : ℝ) := by
    unfold harmonic
    positivity
  unfold tensorFactor
  apply div_pos _ hpR
  have hpR' : (7 : ℝ) ≤ p := by exact_mod_cast hp
  linarith

/-- Every sufficiently large tensor factor is at least one. -/
theorem tensorFactor_ge_one (p : ℕ) (hp : 7 ≤ p) :
    1 ≤ tensorFactor p := by
  have hH : (1 : ℚ) ≤ harmonic (p - 1) := by
    unfold harmonic
    calc
      (1 : ℚ) = ∑ i ∈ ({0} : Finset ℕ), ((i + 1 : ℕ) : ℚ)⁻¹ := by simp
      _ ≤ ∑ i ∈ Finset.range (p - 1), ((i + 1 : ℕ) : ℚ)⁻¹ := by
        apply Finset.sum_le_sum_of_subset_of_nonneg
        · intro i hi
          have hi0 : i = 0 := Finset.mem_singleton.mp hi
          subst i
          simp only [Finset.mem_range]
          omega
        · intro i _ _
          positivity
  have hHr : (1 : ℝ) ≤ ((harmonic (p - 1) : ℚ) : ℝ) := by
    exact_mod_cast hH
  have hpR : (0 : ℝ) < p := by exact_mod_cast (by omega : 0 < p)
  unfold tensorFactor
  apply (le_div_iff₀ hpR).2
  linarith

/-- The logarithm of each large-prime factor has a fixed saving of
`1/(3p)` beyond `log p/p`. -/
theorem log_tensorFactor_le (p : ℕ) (hp : 7 ≤ p) :
    Real.log (tensorFactor p) ≤
      (Real.log (p : ℝ) - 1 / 3) / p := by
  have hpR : (0 : ℝ) < p := by exact_mod_cast (by omega : 0 < p)
  calc
    Real.log (tensorFactor p) ≤ tensorFactor p - 1 :=
      Real.log_le_sub_one_of_pos (tensorFactor_pos p hp)
    _ = (((harmonic (p - 1) : ℚ) : ℝ) - 1) / p := by
      unfold tensorFactor
      field_simp
      ring
    _ ≤ (Real.log (p : ℝ) - 1 / 3) / p :=
      div_le_div_of_nonneg_right
        (harmonic_pred_sub_one_le_log_sub_third p hp) hpR.le

/-- The primes strictly above a cutoff and at most a finite endpoint. -/
def primeInterval (P x : ℕ) : Finset ℕ :=
  (Finset.Ioc P x).filter Nat.Prime

/-- Product of the tensor-side loss multipliers in a finite prime tail. -/
noncomputable def tailFactorProd (P x : ℕ) : ℝ :=
  ∏ p ∈ primeInterval P x, tensorFactor p

theorem tailFactorProd_pos (P x : ℕ) (hP : 7 ≤ P) :
    0 < tailFactorProd P x := by
  unfold tailFactorProd
  apply Finset.prod_pos
  intro p hp
  have hpP : P < p :=
    (Finset.mem_Ioc.mp (Finset.mem_filter.mp hp).1).1
  exact tensorFactor_pos p (hP.trans hpP.le)

/-- Moving the cutoff upward only removes factors, each at least one. -/
theorem tailFactorProd_le_of_le_cutoff (R P x : ℕ)
    (hR : 7 ≤ R) (hRP : R ≤ P) :
    tailFactorProd P x ≤ tailFactorProd R x := by
  unfold tailFactorProd
  apply Finset.prod_le_prod_of_subset_of_one_le₀
  · intro p hp
    rcases Finset.mem_filter.mp hp with ⟨hpI, hprime⟩
    apply Finset.mem_filter.mpr
    exact ⟨Finset.mem_Ioc.mpr ⟨lt_of_le_of_lt hRP (Finset.mem_Ioc.mp hpI).1,
      (Finset.mem_Ioc.mp hpI).2⟩, hprime⟩
  · intro p hp
    have hpP := (Finset.mem_Ioc.mp (Finset.mem_filter.mp hp).1).1
    exact (tensorFactor_pos p (hR.trans (hRP.trans hpP.le))).le
  · intro p hp _
    have hpR := (Finset.mem_Ioc.mp (Finset.mem_filter.mp hp).1).1
    exact tensorFactor_ge_one p (hR.trans hpR.le)

/-- Any product over a subset of tail primes is bounded by the complete
product through the same endpoint. -/
theorem prod_tensorFactor_subset_le (R p : ℕ) (hR : 7 ≤ R)
    (s : Finset ℕ) (hs : s ⊆ primeInterval R p) :
    (∏ q ∈ s, tensorFactor q) ≤ tailFactorProd R p := by
  unfold tailFactorProd
  apply Finset.prod_le_prod_of_subset_of_one_le₀ hs
  · intro q hq
    have hqR := (Finset.mem_Ioc.mp (Finset.mem_filter.mp (hs hq)).1).1
    exact (tensorFactor_pos q (hR.trans hqR.le)).le
  · intro q hq _
    have hqR := (Finset.mem_Ioc.mp (Finset.mem_filter.mp hq).1).1
    exact tensorFactor_ge_one q (hR.trans hqR.le)

/-- Product of the factors preceding `p` in a finite prime selection. -/
noncomputable def priorTensorProd (s : Finset ℕ) (p : ℕ) : ℝ :=
  ∏ q ∈ s.filter (fun q => q < p), tensorFactor q

theorem priorTensorProd_le_tailFactorProd
    (R x p : ℕ) (hR : 7 ≤ R) (s : Finset ℕ)
    (hs : s ⊆ primeInterval R x) :
    priorTensorProd s p ≤ tailFactorProd R p := by
  unfold priorTensorProd
  apply prod_tensorFactor_subset_le R p hR
  intro q hq
  obtain ⟨hqs, hqp⟩ := Finset.mem_filter.mp hq
  have hqprime := (Finset.mem_filter.mp (hs hqs)).2
  have hqR := (Finset.mem_Ioc.mp (Finset.mem_filter.mp (hs hqs)).1).1
  exact Finset.mem_filter.mpr
    ⟨Finset.mem_Ioc.mpr ⟨hqR, hqp.le⟩, hqprime⟩

/-- Every cumulative loss from a selected set of tail primes is dominated by
the corresponding finite complete-prime loss sum. -/
theorem sum_priorTensorLoss_le_complete
    (R x : ℕ) (hR : 7 ≤ R) (s : Finset ℕ)
    (hs : s ⊆ primeInterval R x) :
    (∑ p ∈ s, priorTensorProd s p / (p : ℝ) ^ 2) ≤
      ∑ p ∈ primeInterval R x, tailFactorProd R p / (p : ℝ) ^ 2 := by
  calc
    (∑ p ∈ s, priorTensorProd s p / (p : ℝ) ^ 2) ≤
        ∑ p ∈ s, tailFactorProd R p / (p : ℝ) ^ 2 := by
      apply Finset.sum_le_sum
      intro p _
      exact div_le_div_of_nonneg_right
        (priorTensorProd_le_tailFactorProd R x p hR s hs) (sq_nonneg _)
    _ ≤ ∑ p ∈ primeInterval R x,
          tailFactorProd R p / (p : ℝ) ^ 2 := by
      apply Finset.sum_le_sum_of_subset_of_nonneg hs
      intro p _ _
      exact div_nonneg (tailFactorProd_pos R p hR).le (sq_nonneg _)

theorem log_tailFactorProd_eq_sum (P x : ℕ) (hP : 7 ≤ P) :
    Real.log (tailFactorProd P x) =
      ∑ p ∈ primeInterval P x, Real.log (tensorFactor p) := by
  unfold tailFactorProd
  apply Real.log_prod
  intro p hp
  have hpP : P < p :=
    (Finset.mem_Ioc.mp (Finset.mem_filter.mp hp).1).1
  exact (tensorFactor_pos p (hP.trans hpP.le)).ne'

theorem primeLogHarmonic_sub_eq_primeInterval_sum (P x : ℕ) (hPx : P ≤ x) :
    primeLogHarmonic x - primeLogHarmonic P =
      ∑ p ∈ primeInterval P x, Real.log (p : ℝ) / p := by
  have hsplit := Finset.sum_Ioc_consecutive
    (fun p : ℕ => if p.Prime then Real.log (p : ℝ) / p else 0)
    (Nat.zero_le P) hPx
  unfold primeLogHarmonic primeInterval
  rw [Finset.sum_filter]
  linarith

theorem primeReciprocalSum_sub_eq_primeInterval_sum (P x : ℕ) (hPx : P ≤ x) :
    primeReciprocalSum x - primeReciprocalSum P =
      ∑ p ∈ primeInterval P x, 1 / (p : ℝ) := by
  have hsplit := Finset.sum_Ioc_consecutive
    (fun p : ℕ => if p.Prime then 1 / (p : ℝ) else 0)
    (Nat.zero_le P) hPx
  unfold primeReciprocalSum primeInterval
  rw [Finset.sum_filter]
  linarith

/-- The product-growth estimate before inserting bounds for its two prime
sums. The positive `B` term is the crucial logarithmic saving. -/
theorem log_tailFactorProd_le_prime_sums (P x : ℕ)
    (hP : 7 ≤ P) (hPx : P ≤ x) :
    Real.log (tailFactorProd P x) ≤
      (primeLogHarmonic x - primeLogHarmonic P) -
        (primeReciprocalSum x - primeReciprocalSum P) / 3 := by
  rw [log_tailFactorProd_eq_sum P x hP]
  have hterm (p : ℕ) :
      (Real.log (p : ℝ) - 1 / 3) / p =
        Real.log (p : ℝ) / p - (1 / (p : ℝ)) / 3 := by ring
  calc
    (∑ p ∈ primeInterval P x, Real.log (tensorFactor p)) ≤
        ∑ p ∈ primeInterval P x,
          (Real.log (p : ℝ) - 1 / 3) / p := by
      apply Finset.sum_le_sum
      intro p hp
      have hpP : P < p :=
        (Finset.mem_Ioc.mp (Finset.mem_filter.mp hp).1).1
      exact log_tensorFactor_le p (hP.trans hpP.le)
    _ = (∑ p ∈ primeInterval P x, Real.log (p : ℝ) / p) -
          (∑ p ∈ primeInterval P x, 1 / (p : ℝ)) / 3 := by
      simp_rw [hterm]
      rw [Finset.sum_sub_distrib, Finset.sum_div]
    _ = (primeLogHarmonic x - primeLogHarmonic P) -
          (primeReciprocalSum x - primeReciprocalSum P) / 3 := by
      rw [primeLogHarmonic_sub_eq_primeInterval_sum P x hPx,
        primeReciprocalSum_sub_eq_primeInterval_sum P x hPx]

/-- Summing the wide-block estimate over consecutive powers of `R` gives a
harmonic lower bound for prime reciprocals. -/
theorem primeReciprocalSum_pow_lower
    (K : ℝ)
    (hK : ∀ N : ℕ, 2 ≤ N →
      |primeLogHarmonic N - Real.log (N : ℝ)| ≤ K)
    (R : ℕ) (hR : 2 ≤ R)
    (hlogR : 2 * K + 1 ≤ Real.log (R : ℝ))
    (m : ℕ) :
    (∑ j ∈ Finset.range m,
      1 / Real.log ((R ^ (j + 2) : ℕ) : ℝ)) ≤
      primeReciprocalSum (R ^ (m + 1)) - primeReciprocalSum R := by
  induction m with
  | zero => simp
  | succ m ih =>
      have ha : 2 ≤ R ^ (m + 1) := by
        rw [pow_succ]
        have hpowpos : 0 < R ^ m := pow_pos (by omega) m
        calc
          2 ≤ R := hR
          _ = 1 * R := by simp
          _ ≤ R ^ m * R := Nat.mul_le_mul_right R (by omega)
      have hpow : R ^ (m + 2) = R * R ^ (m + 1) := by
        rw [show m + 2 = (m + 1) + 1 by omega, pow_succ]
        ring
      have hstep :=
        primeReciprocalSum_wide_block_lower K hK R (R ^ (m + 1)) hR hlogR ha
      rw [← hpow] at hstep
      rw [Finset.sum_range_succ]
      linarith

private theorem sum_one_div_add_two_eq_harmonic_sub_one (m : ℕ) :
    (∑ j ∈ Finset.range m, 1 / ((j + 2 : ℕ) : ℝ)) =
      ((harmonic (m + 1) : ℚ) : ℝ) - 1 := by
  induction m with
  | zero => simp [harmonic_succ, harmonic_zero]
  | succ m ih =>
      rw [Finset.sum_range_succ, harmonic_succ]
      simp only [Rat.cast_add, Rat.cast_inv, Rat.cast_natCast]
      rw [ih]
      push_cast
      ring

/-- In particular the reciprocal-prime sum grows at least logarithmically
along powers of a sufficiently wide fixed ratio. -/
theorem primeReciprocalSum_pow_log_lower
    (K : ℝ)
    (hK : ∀ N : ℕ, 2 ≤ N →
      |primeLogHarmonic N - Real.log (N : ℝ)| ≤ K)
    (R : ℕ) (hR : 2 ≤ R)
    (hlogR : 2 * K + 1 ≤ Real.log (R : ℝ))
    (m : ℕ) :
    (Real.log (m + 2 : ℕ) - 1) / Real.log (R : ℝ) ≤
      primeReciprocalSum (R ^ (m + 1)) - primeReciprocalSum R := by
  have hlogRpos : 0 < Real.log (R : ℝ) :=
    Real.log_pos (by exact_mod_cast (by omega : 1 < R))
  have hlogsum :
      (∑ j ∈ Finset.range m,
        1 / Real.log ((R ^ (j + 2) : ℕ) : ℝ)) =
        (((harmonic (m + 1) : ℚ) : ℝ) - 1) / Real.log (R : ℝ) := by
    have hterm (j : ℕ) :
        1 / Real.log ((R ^ (j + 2) : ℕ) : ℝ) =
          (1 / ((j + 2 : ℕ) : ℝ)) / Real.log (R : ℝ) := by
      rw [Nat.cast_pow, Real.log_pow]
      ring
    simp_rw [hterm]
    rw [← Finset.sum_div, sum_one_div_add_two_eq_harmonic_sub_one]
  calc
    (Real.log (m + 2 : ℕ) - 1) / Real.log (R : ℝ) ≤
        (((harmonic (m + 1) : ℚ) : ℝ) - 1) / Real.log (R : ℝ) := by
      apply div_le_div_of_nonneg_right _ hlogRpos.le
      have hh := log_add_one_le_harmonic (m + 1)
      convert sub_le_sub_right hh 1 using 1
    _ = ∑ j ∈ Finset.range m,
          1 / Real.log ((R ^ (j + 2) : ℕ) : ℝ) := hlogsum.symm
    _ ≤ primeReciprocalSum (R ^ (m + 1)) - primeReciprocalSum R :=
      primeReciprocalSum_pow_lower K hK R hR hlogR m

/-- At the endpoints of the wide prime blocks, the tensor product gains a
negative logarithm of the block index beyond its linear logarithmic growth. -/
theorem log_tailFactorProd_pow_le
    (K : ℝ)
    (hK : ∀ N : ℕ, 2 ≤ N →
      |primeLogHarmonic N - Real.log (N : ℝ)| ≤ K)
    (R : ℕ) (hR : 7 ≤ R)
    (hlogR : 2 * K + 1 ≤ Real.log (R : ℝ))
    (m : ℕ) :
    Real.log (tailFactorProd R (R ^ (m + 1))) ≤
      Real.log ((R ^ m : ℕ) : ℝ) + 2 * K -
        (Real.log (m + 2 : ℕ) - 1) / (3 * Real.log (R : ℝ)) := by
  have hpow : R ≤ R ^ (m + 1) := by
    rw [pow_succ]
    have hpowpos : 0 < R ^ m := pow_pos (by omega) m
    calc
      R = 1 * R := by simp
      _ ≤ R ^ m * R := Nat.mul_le_mul_right R (by omega)
  have hlogpow : Real.log ((R ^ (m + 1) : ℕ) : ℝ) =
      Real.log ((R ^ m : ℕ) : ℝ) + Real.log (R : ℝ) := by
    rw [Nat.cast_pow, Nat.cast_pow, Real.log_pow, Real.log_pow]
    push_cast
    ring
  have hAupper := (abs_le.mp (hK (R ^ (m + 1)) (by omega))).2
  have hAlower := (abs_le.mp (hK R (by omega))).1
  have hB := primeReciprocalSum_pow_log_lower K hK R (by omega) hlogR m
  have hprod := log_tailFactorProd_le_prime_sums R (R ^ (m + 1)) hR hpow
  rw [hlogpow] at hAupper
  have hlogRpos : 0 < Real.log (R : ℝ) :=
    Real.log_pos (by exact_mod_cast (by omega : 1 < R))
  have hdiv : (Real.log (m + 2 : ℕ) - 1) / Real.log (R : ℝ) / 3 =
      (Real.log (m + 2 : ℕ) - 1) / (3 * Real.log (R : ℝ)) := by ring
  rw [← hdiv]
  linarith

/-- A Chebyshev upper bound for reciprocal primes in any interval. This is
useful for converting the product decay into a summable block bound. -/
theorem sum_inv_primeInterval_le (a b : ℕ) (ha : 2 ≤ a) (_hab : a ≤ b) :
    (∑ p ∈ primeInterval a b, (1 / (p : ℝ))) ≤
      Real.log 4 * (b : ℝ) / ((a : ℝ) * Real.log (a : ℝ)) := by
  have hapos : (0 : ℝ) < a := by exact_mod_cast (by omega : 0 < a)
  have halog : 0 < Real.log (a : ℝ) :=
    Real.log_pos (by exact_mod_cast (by omega : 1 < a))
  have hdenom : 0 < (a : ℝ) * Real.log (a : ℝ) := mul_pos hapos halog
  have hpoint : ∀ p ∈ primeInterval a b,
      (1 / (p : ℝ)) ≤ Real.log p / ((a : ℝ) * Real.log a) := by
    intro p hp
    have hpI : a < p ∧ p ≤ b :=
      Finset.mem_Ioc.mp (Finset.mem_filter.mp hp).1
    have hap : (a : ℝ) ≤ p := by exact_mod_cast hpI.1.le
    have hlog : Real.log (a : ℝ) ≤ Real.log (p : ℝ) :=
      Real.log_le_log hapos hap
    have hle : (1 : ℝ) / p ≤ 1 / a :=
      one_div_le_one_div_of_le hapos hap
    have hle' : (1 : ℝ) / a ≤ Real.log p / (a * Real.log a) := by
      apply (div_le_div_iff₀ hapos hdenom).2
      nlinarith
    exact hle.trans hle'
  have hsub : primeInterval a b ⊆ Nat.primesLE b := by
    intro p hp
    rcases Finset.mem_filter.mp hp with ⟨hpI, hprime⟩
    exact Nat.mem_primesLE.mpr ⟨(Finset.mem_Ioc.mp hpI).2, hprime⟩
  have hlogs : (∑ p ∈ primeInterval a b, Real.log (p : ℝ)) ≤
      (∑ p ∈ Nat.primesLE b, Real.log (p : ℝ)) := by
    apply Finset.sum_le_sum_of_subset_of_nonneg hsub
    intro p hp _
    exact Real.log_nonneg (by exact_mod_cast (show 1 ≤ p by
      have := Nat.two_le_of_mem_primesLE hp
      omega))
  calc
    (∑ p ∈ primeInterval a b, (1 / (p : ℝ))) ≤
        ∑ p ∈ primeInterval a b, Real.log p / ((a : ℝ) * Real.log a) :=
      Finset.sum_le_sum hpoint
    _ = (∑ p ∈ primeInterval a b, Real.log (p : ℝ)) /
        ((a : ℝ) * Real.log a) := by rw [Finset.sum_div]
    _ ≤ (∑ p ∈ Nat.primesLE b, Real.log (p : ℝ)) /
        ((a : ℝ) * Real.log a) :=
      div_le_div_of_nonneg_right hlogs hdenom.le
    _ = Chebyshev.theta b / ((a : ℝ) * Real.log a) := by
      rw [Chebyshev.theta_eq_sum_primesLE_log]
    _ ≤ (Real.log 4 * (b : ℝ)) / ((a : ℝ) * Real.log a) := by
      exact div_le_div_of_nonneg_right
        (Chebyshev.theta_le_log4_mul_x (by positivity)) hdenom.le

/-- Reciprocal-prime sums increase with their endpoint. -/
theorem primeReciprocalSum_mono {a b : ℕ} (hab : a ≤ b) :
    primeReciprocalSum a ≤ primeReciprocalSum b := by
  have hsplit := Finset.sum_Ioc_consecutive
    (fun n : ℕ => if n.Prime then 1 / (n : ℝ) else 0)
    (Nat.zero_le a) hab
  unfold primeReciprocalSum
  rw [← hsplit]
  have hnonneg : 0 ≤ ∑ n ∈ Finset.Ioc a b,
      if n.Prime then 1 / (n : ℝ) else 0 := by
    apply Finset.sum_nonneg
    intro n hn
    split_ifs
    · have hnpos : (0 : ℝ) < n := by
        exact_mod_cast (lt_of_le_of_lt (Nat.zero_le a) (Finset.mem_Ioc.mp hn).1)
      positivity
    · rfl
  linarith

/-- The logarithmic saving holds at every point past a wide-block endpoint,
not only at the endpoints themselves. -/
theorem log_tailFactorProd_le_of_pow_le
    (K : ℝ)
    (hK : ∀ N : ℕ, 2 ≤ N →
      |primeLogHarmonic N - Real.log (N : ℝ)| ≤ K)
    (R : ℕ) (hR : 7 ≤ R)
    (hlogR : 2 * K + 1 ≤ Real.log (R : ℝ))
    (m x : ℕ) (hmx : R ^ (m + 1) ≤ x) :
    Real.log (tailFactorProd R x) ≤
      Real.log (x : ℝ) - Real.log (R : ℝ) + 2 * K -
        (Real.log (m + 2 : ℕ) - 1) / (3 * Real.log (R : ℝ)) := by
  have hRpow : R ≤ R ^ (m + 1) := by
    rw [pow_succ]
    have hpowpos : 0 < R ^ m := pow_pos (by omega) m
    calc
      R = 1 * R := by simp
      _ ≤ R ^ m * R := Nat.mul_le_mul_right R (by omega)
  have hAx := (abs_le.mp (hK x (by omega))).2
  have hAR := (abs_le.mp (hK R (by omega))).1
  have hBpow := primeReciprocalSum_pow_log_lower K hK R (by omega) hlogR m
  have hBmono := primeReciprocalSum_mono hmx
  have hprod := log_tailFactorProd_le_prime_sums R x hR (hRpow.trans hmx)
  have hdiv : (Real.log (m + 2 : ℕ) - 1) / Real.log (R : ℝ) / 3 =
      (Real.log (m + 2 : ℕ) - 1) / (3 * Real.log (R : ℝ)) := by ring
  rw [← hdiv]
  linarith

/-- The model sequence for the prime loss on wide blocks is summable for
every positive logarithmic saving exponent. -/
theorem summable_wide_block_majorant (β : ℝ) (hβ : 0 < β) :
    Summable (fun m : ℕ =>
      1 / (((m + 1 : ℕ) : ℝ) ^ (1 + β))) := by
  have hs := (Real.summable_one_div_nat_add_rpow 1 (1 + β)).2 (by linarith)
  convert hs using 1
  ext m
  simp only [Nat.cast_add, Nat.cast_one]
  rw [abs_of_pos (show (0 : ℝ) < (m : ℝ) + 1 by positivity)]

/-- An integer block ratio can be chosen wider than any fixed error in the
first Mertens estimate. -/
theorem exists_wide_ratio (K : ℝ) :
    ∃ R : ℕ, 7 ≤ R ∧ 2 * K + 1 ≤ Real.log (R : ℝ) := by
  obtain ⟨R, hR⟩ := exists_nat_gt (max (7 : ℝ) (Real.exp (2 * K + 1)))
  refine ⟨R, ?_, ?_⟩
  · have h7 : (7 : ℝ) ≤ (R : ℝ) := by
      linarith [le_max_left (7 : ℝ) (Real.exp (2 * K + 1))]
    exact_mod_cast h7
  · have he : Real.exp (2 * K + 1) ≤ (R : ℝ) := by
      linarith [le_max_right (7 : ℝ) (Real.exp (2 * K + 1))]
    have hlog := Real.log_le_log (Real.exp_pos _) he
    rwa [Real.log_exp] at hlog

/-- The product divided by its endpoint gains a positive power of the block
index. This is the pointwise estimate used in each prime-loss block. -/
theorem tailFactorProd_div_le_of_pow_le
    (K : ℝ)
    (hK : ∀ N : ℕ, 2 ≤ N →
      |primeLogHarmonic N - Real.log (N : ℝ)| ≤ K)
    (R : ℕ) (hR : 7 ≤ R)
    (hlogR : 2 * K + 1 ≤ Real.log (R : ℝ))
    (m x : ℕ) (hmx : R ^ (m + 1) ≤ x) :
    tailFactorProd R x / (x : ℝ) ≤
      Real.exp (2 * K - Real.log (R : ℝ) +
        1 / (3 * Real.log (R : ℝ))) /
        ((m + 2 : ℕ) : ℝ) ^ (1 / (3 * Real.log (R : ℝ))) := by
  let β : ℝ := 1 / (3 * Real.log (R : ℝ))
  have hlogRpos : 0 < Real.log (R : ℝ) :=
    Real.log_pos (by exact_mod_cast (by omega : 1 < R))
  have hRpow : R ≤ R ^ (m + 1) := by
    rw [pow_succ]
    have hpowpos : 0 < R ^ m := pow_pos (by omega) m
    calc
      R = 1 * R := by simp
      _ ≤ R ^ m * R := Nat.mul_le_mul_right R (by omega)
  have hxpos : (0 : ℝ) < x := by
    exact_mod_cast (lt_of_lt_of_le (by omega : 0 < R) (hRpow.trans hmx))
  have hprodpos := tailFactorProd_pos R x hR
  have hnpos : (0 : ℝ) < (m + 2 : ℕ) := by positivity
  have hlogprod := log_tailFactorProd_le_of_pow_le K hK R hR hlogR m x hmx
  have hlogquot : Real.log (tailFactorProd R x / (x : ℝ)) ≤
      2 * K - Real.log (R : ℝ) + β -
        β * Real.log (m + 2 : ℕ) := by
    rw [Real.log_div hprodpos.ne' hxpos.ne']
    have hrearr : (Real.log (m + 2 : ℕ) - 1) /
        (3 * Real.log (R : ℝ)) =
        (1 / (3 * Real.log (R : ℝ))) * Real.log (m + 2 : ℕ) -
          1 / (3 * Real.log (R : ℝ)) := by ring
    rw [hrearr] at hlogprod
    dsimp [β]
    linarith [hlogprod]
  have hexp := Real.exp_le_exp.mpr hlogquot
  rw [Real.exp_log (div_pos hprodpos hxpos), Real.exp_sub] at hexp
  have hpow : Real.exp (β * Real.log (m + 2 : ℕ)) =
      ((m + 2 : ℕ) : ℝ) ^ β := by
    rw [Real.rpow_def_of_pos hnpos]
    congr 1
    ring
  rw [hpow] at hexp
  exact hexp

/-- A finite wide block of prime losses is controlled by the pointwise
product estimate and Chebyshev's reciprocal-prime bound. -/
theorem sum_tailLoss_wide_block_le
    (K : ℝ)
    (hK : ∀ N : ℕ, 2 ≤ N →
      |primeLogHarmonic N - Real.log (N : ℝ)| ≤ K)
    (R : ℕ) (hR : 7 ≤ R)
    (hlogR : 2 * K + 1 ≤ Real.log (R : ℝ))
    (m : ℕ) :
    (∑ p ∈ primeInterval (R ^ (m + 1)) (R ^ (m + 2)),
        tailFactorProd R p / (p : ℝ) ^ 2) ≤
      (Real.exp (2 * K - Real.log (R : ℝ) +
          1 / (3 * Real.log (R : ℝ))) /
          ((m + 2 : ℕ) : ℝ) ^ (1 / (3 * Real.log (R : ℝ)))) *
        (Real.log 4 * ((R ^ (m + 2) : ℕ) : ℝ) /
          (((R ^ (m + 1) : ℕ) : ℝ) *
            Real.log ((R ^ (m + 1) : ℕ) : ℝ))) := by
  let a : ℕ := R ^ (m + 1)
  let b : ℕ := R ^ (m + 2)
  let C : ℝ := Real.exp (2 * K - Real.log (R : ℝ) +
      1 / (3 * Real.log (R : ℝ))) /
      ((m + 2 : ℕ) : ℝ) ^ (1 / (3 * Real.log (R : ℝ)))
  have ha : 2 ≤ a := by
    dsimp [a]
    rw [pow_succ]
    have hp : 0 < R ^ m := pow_pos (by omega) m
    nlinarith
  have hab : a ≤ b := by
    calc
      a = 1 * a := by simp
      _ ≤ R * a := Nat.mul_le_mul_right a (by omega)
      _ = b := by
        dsimp [a, b]
        rw [show m + 2 = (m + 1) + 1 by omega, pow_succ]
        ring
  have hCnonneg : 0 ≤ C := by
    dsimp [C]
    positivity
  have hpoint (p : ℕ) (hp : p ∈ primeInterval a b) :
      tailFactorProd R p / (p : ℝ) ^ 2 ≤ C * (1 / (p : ℝ)) := by
    have hap : a ≤ p := (Finset.mem_Ioc.mp (Finset.mem_filter.mp hp).1).1.le
    have hppos : (0 : ℝ) < p := by
      exact_mod_cast (lt_of_lt_of_le (by omega : 0 < a) hap)
    have hmain := tailFactorProd_div_le_of_pow_le K hK R hR hlogR m p hap
    change tailFactorProd R p / (p : ℝ) ≤ C at hmain
    have hdiv : tailFactorProd R p / (p : ℝ) ^ 2 =
        (tailFactorProd R p / (p : ℝ)) * (1 / (p : ℝ)) := by ring
    rw [hdiv]
    exact mul_le_mul_of_nonneg_right hmain (by positivity)
  calc
    (∑ p ∈ primeInterval a b, tailFactorProd R p / (p : ℝ) ^ 2) ≤
        ∑ p ∈ primeInterval a b, C * (1 / (p : ℝ)) :=
      Finset.sum_le_sum hpoint
    _ = C * ∑ p ∈ primeInterval a b, (1 / (p : ℝ)) := by
      rw [Finset.mul_sum]
    _ ≤ C * (Real.log 4 * (b : ℝ) /
          ((a : ℝ) * Real.log (a : ℝ))) :=
      mul_le_mul_of_nonneg_left (sum_inv_primeInterval_le a b ha hab) hCnonneg
    _ = _ := rfl

/-- The preceding bound has the summable p-series shape
`constant / ((m+1) * (m+2)^β)` with `β > 0`. -/
theorem sum_tailLoss_wide_block_le_model
    (K : ℝ)
    (hK : ∀ N : ℕ, 2 ≤ N →
      |primeLogHarmonic N - Real.log (N : ℝ)| ≤ K)
    (R : ℕ) (hR : 7 ≤ R)
    (hlogR : 2 * K + 1 ≤ Real.log (R : ℝ))
    (m : ℕ) :
    (∑ p ∈ primeInterval (R ^ (m + 1)) (R ^ (m + 2)),
        tailFactorProd R p / (p : ℝ) ^ 2) ≤
      (Real.exp (2 * K - Real.log (R : ℝ) +
          1 / (3 * Real.log (R : ℝ))) *
          (R : ℝ) * Real.log 4 / Real.log (R : ℝ)) /
        (((m + 1 : ℕ) : ℝ) *
          ((m + 2 : ℕ) : ℝ) ^ (1 / (3 * Real.log (R : ℝ)))) := by
  have hlogRpos : 0 < Real.log (R : ℝ) :=
    Real.log_pos (by exact_mod_cast (by omega : 1 < R))
  have hRpos : (0 : ℝ) < R := by exact_mod_cast (by omega : 0 < R)
  have hapos : (0 : ℝ) < (R ^ (m + 1) : ℕ) := by positivity
  have hmp : (0 : ℝ) < ((m + 1 : ℕ) : ℝ) := by positivity
  have hpowpos : (0 : ℝ) < ((m + 2 : ℕ) : ℝ) ^
      (1 / (3 * Real.log (R : ℝ))) := by positivity
  have hb : ((R ^ (m + 2) : ℕ) : ℝ) =
      ((R ^ (m + 1) : ℕ) : ℝ) * (R : ℝ) := by
    rw [show m + 2 = (m + 1) + 1 by omega, pow_succ, Nat.cast_mul]
  have hloga : Real.log ((R ^ (m + 1) : ℕ) : ℝ) =
      ((m + 1 : ℕ) : ℝ) * Real.log (R : ℝ) := by
    rw [Nat.cast_pow, Real.log_pow]
  calc
    (∑ p ∈ primeInterval (R ^ (m + 1)) (R ^ (m + 2)),
        tailFactorProd R p / (p : ℝ) ^ 2) ≤
      (Real.exp (2 * K - Real.log (R : ℝ) +
          1 / (3 * Real.log (R : ℝ))) /
          ((m + 2 : ℕ) : ℝ) ^ (1 / (3 * Real.log (R : ℝ)))) *
        (Real.log 4 * ((R ^ (m + 2) : ℕ) : ℝ) /
          (((R ^ (m + 1) : ℕ) : ℝ) *
            Real.log ((R ^ (m + 1) : ℕ) : ℝ))) :=
      sum_tailLoss_wide_block_le K hK R hR hlogR m
    _ = _ := by
      rw [hb, hloga]
      field_simp

/-- The exact model sequence in the wide-block estimate is summable. -/
theorem summable_wide_block_loss_shape (β : ℝ) (hβ : 0 < β) :
    Summable (fun m : ℕ =>
      1 / (((m + 1 : ℕ) : ℝ) * ((m + 2 : ℕ) : ℝ) ^ β)) := by
  apply Summable.of_nonneg_of_le (fun m => by positivity) ?_
    (summable_wide_block_majorant β hβ)
  intro m
  have hmpos : (0 : ℝ) < ((m + 1 : ℕ) : ℝ) := by positivity
  have hle : (((m + 1 : ℕ) : ℝ)) ≤ (((m + 2 : ℕ) : ℝ)) := by
    exact_mod_cast (by omega : m + 1 ≤ m + 2)
  have hpow := Real.rpow_le_rpow hmpos.le hle hβ.le
  have hdenom := mul_le_mul_of_nonneg_left hpow hmpos.le
  have hbound := one_div_le_one_div_of_le
    (mul_pos hmpos (Real.rpow_pos_of_pos hmpos β)) hdenom
  have hid : (((m + 1 : ℕ) : ℝ)) * (((m + 1 : ℕ) : ℝ) ^ β) =
      (((m + 1 : ℕ) : ℝ)) ^ (1 + β) := by
    rw [Real.rpow_add hmpos]
    simp
  rw [hid] at hbound
  exact hbound

/-- The losses of consecutive wide prime blocks have a convergent total. -/
theorem summable_wide_block_losses
    (K : ℝ)
    (hK : ∀ N : ℕ, 2 ≤ N →
      |primeLogHarmonic N - Real.log (N : ℝ)| ≤ K)
    (R : ℕ) (hR : 7 ≤ R)
    (hlogR : 2 * K + 1 ≤ Real.log (R : ℝ)) :
    Summable (fun m : ℕ =>
      ∑ p ∈ primeInterval (R ^ (m + 1)) (R ^ (m + 2)),
        tailFactorProd R p / (p : ℝ) ^ 2) := by
  let β : ℝ := 1 / (3 * Real.log (R : ℝ))
  let D : ℝ := Real.exp (2 * K - Real.log (R : ℝ) + β) *
    (R : ℝ) * Real.log 4 / Real.log (R : ℝ)
  have hlogRpos : 0 < Real.log (R : ℝ) :=
    Real.log_pos (by exact_mod_cast (by omega : 1 < R))
  have hβ : 0 < β := by dsimp [β]; positivity
  have hmodel : Summable (fun m : ℕ =>
      D * (1 / (((m + 1 : ℕ) : ℝ) * ((m + 2 : ℕ) : ℝ) ^ β))) :=
    (summable_wide_block_loss_shape β hβ).mul_left D
  apply Summable.of_nonneg_of_le ?_ ?_ hmodel
  · intro m
    apply Finset.sum_nonneg
    intro p _hp
    exact div_nonneg (tailFactorProd_pos R p hR).le (sq_nonneg _)
  · intro m
    calc
      (∑ p ∈ primeInterval (R ^ (m + 1)) (R ^ (m + 2)),
          tailFactorProd R p / (p : ℝ) ^ 2) ≤
        D / (((m + 1 : ℕ) : ℝ) * ((m + 2 : ℕ) : ℝ) ^ β) :=
        sum_tailLoss_wide_block_le_model K hK R hR hlogR m
      _ = D * (1 / (((m + 1 : ℕ) : ℝ) *
          ((m + 2 : ℕ) : ℝ) ^ β)) := by ring

/-- The individual large-prime loss, extended by zero at composite indices. -/
noncomputable def primeLoss (R p : ℕ) : ℝ :=
  if p.Prime then tailFactorProd R p / (p : ℝ) ^ 2 else 0

theorem primeLoss_nonneg (R p : ℕ) (hR : 7 ≤ R) :
    0 ≤ primeLoss R p := by
  unfold primeLoss
  split_ifs
  · exact div_nonneg (tailFactorProd_pos R p hR).le (sq_nonneg _)
  · rfl

theorem sum_primeLoss_interval_eq (R a b : ℕ) :
    (∑ p ∈ Finset.Ioc a b, primeLoss R p) =
      ∑ p ∈ primeInterval a b, tailFactorProd R p / (p : ℝ) ^ 2 := by
  simp only [primeLoss, primeInterval, Finset.sum_filter]

/-- Adjacent wide blocks partition the finite prime tail exactly. -/
theorem sum_wideBlocks_eq_primeLoss_interval
    (R M : ℕ) (hR : 7 ≤ R) :
    (∑ m ∈ Finset.range M,
      ∑ p ∈ primeInterval (R ^ (m + 1)) (R ^ (m + 2)),
        tailFactorProd R p / (p : ℝ) ^ 2) =
      ∑ p ∈ Finset.Ioc R (R ^ (M + 1)), primeLoss R p := by
  induction M with
  | zero => simp
  | succ M ih =>
      have hRpow : R ≤ R ^ (M + 1) := by
        rw [pow_succ]
        have hpowpos : 0 < R ^ M := pow_pos (by omega) M
        calc
          R = 1 * R := by simp
          _ ≤ R ^ M * R := Nat.mul_le_mul_right R (by omega)
      have hpow : R ^ (M + 1) ≤ R ^ (M + 2) := by
        calc
          R ^ (M + 1) = 1 * R ^ (M + 1) := by simp
          _ ≤ R * R ^ (M + 1) := Nat.mul_le_mul_right _ (by omega)
          _ = R ^ (M + 2) := by
            rw [show M + 2 = (M + 1) + 1 by omega, pow_succ]
            ring
      calc
        (∑ m ∈ Finset.range (M + 1),
          ∑ p ∈ primeInterval (R ^ (m + 1)) (R ^ (m + 2)),
            tailFactorProd R p / (p : ℝ) ^ 2) =
          (∑ m ∈ Finset.range M,
            ∑ p ∈ primeInterval (R ^ (m + 1)) (R ^ (m + 2)),
              tailFactorProd R p / (p : ℝ) ^ 2) +
            (∑ p ∈ primeInterval (R ^ (M + 1)) (R ^ (M + 2)),
              tailFactorProd R p / (p : ℝ) ^ 2) := by
          rw [Finset.sum_range_succ]
        _ = (∑ p ∈ Finset.Ioc R (R ^ (M + 1)), primeLoss R p) +
              (∑ p ∈ Finset.Ioc (R ^ (M + 1)) (R ^ (M + 2)),
                primeLoss R p) := by
          rw [ih, ← sum_primeLoss_interval_eq R (R ^ (M + 1)) (R ^ (M + 2))]
        _ = ∑ p ∈ Finset.Ioc R (R ^ ((M + 1) + 1)), primeLoss R p := by
          rw [show (M + 1) + 1 = M + 2 by omega]
          exact Finset.sum_Ioc_consecutive (primeLoss R) hRpow hpow

/-- The loss series over primes above a fixed wide ratio converges. -/
theorem summable_primeLoss_tail
    (K : ℝ)
    (hK : ∀ N : ℕ, 2 ≤ N →
      |primeLogHarmonic N - Real.log (N : ℝ)| ≤ K)
    (R : ℕ) (hR : 7 ≤ R)
    (hlogR : 2 * K + 1 ≤ Real.log (R : ℝ)) :
    Summable (fun p : ℕ => if R < p then primeLoss R p else 0) := by
  let blockLoss : ℕ → ℝ := fun m =>
    ∑ p ∈ primeInterval (R ^ (m + 1)) (R ^ (m + 2)),
      tailFactorProd R p / (p : ℝ) ^ 2
  have hs : Summable blockLoss :=
    summable_wide_block_losses K hK R hR hlogR
  have hblocknonneg (m : ℕ) : 0 ≤ blockLoss m := by
    dsimp [blockLoss]
    apply Finset.sum_nonneg
    intro p _
    exact div_nonneg (tailFactorProd_pos R p hR).le (sq_nonneg _)
  apply summable_of_sum_le (fun p => by
    split_ifs
    · exact primeLoss_nonneg R p hR
    · rfl) (c := ∑' m, blockLoss m)
  intro u
  obtain ⟨M, hM⟩ := pow_unbounded_of_one_lt (u.sup id) (by omega : 1 < R)
  have hpow : R ^ M ≤ R ^ (M + 1) := by
    calc
      R ^ M = 1 * R ^ M := by simp
      _ ≤ R * R ^ M := Nat.mul_le_mul_right _ (by omega)
      _ = R ^ (M + 1) := by rw [pow_succ]; ring
  have hsub : u.filter (fun p => R < p) ⊆ Finset.Ioc R (R ^ (M + 1)) := by
    intro p hp
    obtain ⟨hpu, hpR⟩ := Finset.mem_filter.mp hp
    have hpsup : p ≤ u.sup id := by simpa using Finset.le_sup (f := id) hpu
    exact Finset.mem_Ioc.mpr ⟨hpR, (hpsup.trans hM.le).trans hpow⟩
  have hsumle : (∑ p ∈ u.filter (fun p => R < p), primeLoss R p) ≤
      ∑ p ∈ Finset.Ioc R (R ^ (M + 1)), primeLoss R p :=
    Finset.sum_le_sum_of_subset_of_nonneg hsub
      (fun p _ _ => primeLoss_nonneg R p hR)
  calc
    (∑ p ∈ u, if R < p then primeLoss R p else 0) =
        ∑ p ∈ u.filter (fun p => R < p), primeLoss R p := by
      rw [Finset.sum_filter]
    _ ≤ ∑ p ∈ Finset.Ioc R (R ^ (M + 1)), primeLoss R p := hsumle
    _ = ∑ m ∈ Finset.range M, blockLoss m := by
      exact (sum_wideBlocks_eq_primeLoss_interval R M hR).symm
    _ ≤ ∑' m, blockLoss m :=
      hs.sum_le_tsum (Finset.range M) (fun m _ => hblocknonneg m)

private theorem sum_range_succ_eq_sum_Ioc_zero
    (f : ℕ → ℝ) (hf0 : f 0 = 0) (n : ℕ) :
    (∑ p ∈ Finset.range (n + 1), f p) =
      ∑ p ∈ Finset.Ioc 0 n, f p := by
  have hset : Finset.range (n + 1) = insert 0 (Finset.Ioc 0 n) := by
    ext p
    simp only [Finset.mem_range, Finset.mem_insert, Finset.mem_Ioc]
    omega
  have hzero : (0 : ℕ) ∉ Finset.Ioc 0 n := by simp
  rw [hset, Finset.sum_insert hzero, hf0, zero_add]

private theorem sum_Ioc_le_tsum_sub
    (f : ℕ → ℝ) (hs : Summable f)
    (hf0 : f 0 = 0) (hfn : ∀ p, 0 ≤ f p)
    (P x : ℕ) (hPx : P ≤ x) :
    (∑ p ∈ Finset.Ioc P x, f p) ≤
      (∑' p, f p) - ∑ p ∈ Finset.range (P + 1), f p := by
  have hsplit := Finset.sum_Ioc_consecutive f (Nat.zero_le P) hPx
  have hsumx := hs.sum_le_tsum (Finset.range (x + 1))
    (fun p _ => hfn p)
  rw [sum_range_succ_eq_sum_Ioc_zero f hf0 x] at hsumx
  rw [sum_range_succ_eq_sum_Ioc_zero f hf0 P]
  linarith

/-- Every convergent nonnegative series has uniformly small finite tails. -/
theorem exists_uniform_small_finite_tail
    (f : ℕ → ℝ) (hs : Summable f)
    (hf0 : f 0 = 0) (hfn : ∀ p, 0 ≤ f p)
    (R : ℕ) (ε : ℝ) (hε : 0 < ε) :
    ∃ P : ℕ, R ≤ P ∧ ∀ x : ℕ,
      (∑ p ∈ Finset.Ioc P x, f p) < ε := by
  have ht : Filter.Tendsto
      (fun n : ℕ => (∑' p, f p) - ∑ p ∈ Finset.range (n + 1), f p)
      Filter.atTop (nhds 0) := by
    have hsum := hs.hasSum.tendsto_sum_nat.comp (Filter.tendsto_add_atTop_nat 1)
    simpa using (tendsto_const_nhds.sub hsum :
      Filter.Tendsto
        (fun n : ℕ => (∑' p, f p) - ∑ p ∈ Finset.range (n + 1), f p)
        Filter.atTop (nhds ((∑' p, f p) - ∑' p, f p)))
  have hev : ∀ᶠ n : ℕ in Filter.atTop,
      (∑' p, f p) - ∑ p ∈ Finset.range (n + 1), f p < ε :=
    ht.eventually (isOpen_Iio.mem_nhds hε)
  obtain ⟨P₀, hP₀⟩ := Filter.eventually_atTop.1 hev
  let P := max R P₀
  refine ⟨P, le_max_left R P₀, ?_⟩
  intro x
  by_cases hPx : P ≤ x
  · have hsmall := hP₀ P (le_max_right R P₀)
    have hbound := sum_Ioc_le_tsum_sub f hs hf0 hfn P x hPx
    linarith
  · have hxP : x ≤ P := by omega
    rw [Finset.Ioc_eq_empty_of_le hxP]
    simpa using hε

/-- An existential large-prime cutoff makes the total finite tensor loss
smaller than one, uniformly in the final prime endpoint. -/
theorem exists_cutoff_uniform_primeLoss_lt_one
    (C : ℝ) (hC : 0 < C) :
    ∃ P : ℕ, 7 ≤ P ∧ ∀ x : ℕ,
      (∑ p ∈ primeInterval P x,
        C * tailFactorProd P p / (p : ℝ) ^ 2) < 1 := by
  obtain ⟨K, _hKnonneg, hK⟩ := exists_primeLogHarmonic_log_bound
  obtain ⟨R, hR, hlogR⟩ := exists_wide_ratio K
  let f : ℕ → ℝ := fun p => if R < p then primeLoss R p else 0
  have hs : Summable f := summable_primeLoss_tail K hK R hR hlogR
  have hf0 : f 0 = 0 := by simp [f]
  have hfn (p : ℕ) : 0 ≤ f p := by
    dsimp [f]
    split_ifs
    · exact primeLoss_nonneg R p hR
    · rfl
  have hε : 0 < 1 / C := by positivity
  obtain ⟨P, hRP, hsmall⟩ :=
    exists_uniform_small_finite_tail f hs hf0 hfn R (1 / C) hε
  refine ⟨P, hR.trans hRP, ?_⟩
  intro x
  have hrewrite : (∑ p ∈ Finset.Ioc P x, f p) =
      ∑ p ∈ primeInterval P x, tailFactorProd R p / (p : ℝ) ^ 2 := by
    unfold primeInterval
    rw [Finset.sum_filter]
    apply Finset.sum_congr rfl
    intro p hp
    have hpR : R < p :=
      lt_of_le_of_lt hRP (Finset.mem_Ioc.mp hp).1
    simp [f, primeLoss, hpR]
  have hpoint (p : ℕ) (_hp : p ∈ primeInterval P x) :
      C * tailFactorProd P p / (p : ℝ) ^ 2 ≤
        C * (tailFactorProd R p / (p : ℝ) ^ 2) := by
    have hprod := tailFactorProd_le_of_le_cutoff R P p hR hRP
    have hmul := mul_le_mul_of_nonneg_left hprod hC.le
    calc
      _ ≤ C * tailFactorProd R p / (p : ℝ) ^ 2 :=
        div_le_div_of_nonneg_right hmul (sq_nonneg _)
      _ = C * (tailFactorProd R p / (p : ℝ) ^ 2) := by ring
  calc
    (∑ p ∈ primeInterval P x,
        C * tailFactorProd P p / (p : ℝ) ^ 2) ≤
      C * (∑ p ∈ primeInterval P x,
        tailFactorProd R p / (p : ℝ) ^ 2) := by
      rw [Finset.mul_sum]
      exact Finset.sum_le_sum hpoint
    _ = C * (∑ p ∈ Finset.Ioc P x, f p) := by rw [hrewrite]
    _ < C * (1 / C) := mul_lt_mul_of_pos_left (hsmall x) hC
    _ = 1 := by field_simp

/-- One cutoff works for every finite selection of later primes, with the
factor at each selected prime taken only over earlier selected primes. -/
theorem exists_cutoff_uniform_selectedLoss_lt_one
    (C : ℝ) (hC : 0 < C) :
    ∃ P : ℕ, 7 ≤ P ∧ ∀ (x : ℕ) (s : Finset ℕ),
      s ⊆ primeInterval P x →
      (∑ p ∈ s, C * priorTensorProd s p / (p : ℝ) ^ 2) < 1 := by
  obtain ⟨P, hP, hfull⟩ := exists_cutoff_uniform_primeLoss_lt_one C hC
  refine ⟨P, hP, ?_⟩
  intro x s hs
  have hsum := sum_priorTensorLoss_le_complete P x hP s hs
  have hscaled := mul_le_mul_of_nonneg_left hsum hC.le
  calc
    (∑ p ∈ s, C * priorTensorProd s p / (p : ℝ) ^ 2) =
        C * (∑ p ∈ s, priorTensorProd s p / (p : ℝ) ^ 2) := by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro p _
      ring
    _ ≤ C * (∑ p ∈ primeInterval P x,
          tailFactorProd P p / (p : ℝ) ^ 2) := hscaled
    _ = (∑ p ∈ primeInterval P x,
          C * tailFactorProd P p / (p : ℝ) ^ 2) := by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro p _
      ring
    _ < 1 := hfull x

/-- A single cutoff controls every finite prime list. The numerical product
uses the earlier entries of the list when the list is increasing; the result
is stated using their finite set, so it also tolerates repeated entries. -/
theorem exists_cutoff_uniform_primeListLoss_lt_one :
    ∃ P : ℕ, 7 ≤ P ∧ ∀ ps : List ℕ,
      (∀ p ∈ ps, p.Prime ∧ P < p) →
      (∑ p ∈ ps.toFinset,
        (6 * Real.pi ^ 2) * priorTensorProd ps.toFinset p /
          (p : ℝ) ^ 2) < 1 := by
  have hC : (0 : ℝ) < 6 * Real.pi ^ 2 := by positivity
  obtain ⟨P, hP, hall⟩ :=
    exists_cutoff_uniform_selectedLoss_lt_one (6 * Real.pi ^ 2) hC
  refine ⟨P, hP, ?_⟩
  intro ps hps
  let s : Finset ℕ := ps.toFinset
  let x : ℕ := s.sup id
  have hs : s ⊆ primeInterval P x := by
    intro p hp
    have hmem : p ∈ ps := by simpa [s] using hp
    obtain ⟨hprime, hpP⟩ := hps p hmem
    have hpx : p ≤ x := by
      dsimp [x]
      simpa using Finset.le_sup (f := id) hp
    exact Finset.mem_filter.mpr
      ⟨Finset.mem_Ioc.mpr ⟨hpP, hpx⟩, hprime⟩
  exact hall x s hs

end Erdos.Research.PrimeTailBounds

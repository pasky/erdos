import Mathlib.Analysis.Complex.Circle
import Mathlib.Analysis.SpecialFunctions.Complex.CircleAddChar
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic

/-!
# Finite orthogonal sampling of algebraic characters

For any prescribed finite list of nonzero elements of the discrete additive
group `ℂ`, a finite average of algebraic circle-valued characters annihilates
every element on the list exactly. The same average is one at zero. This
replaces a Haar integral for finite Fourier calculations.
-/

namespace Erdos.Research.FiniteOrthogonalCharacters

private noncomputable def phaseMap (s : ℂ) : ℂ →+ ℝ where
  toFun z := Real.pi * (z / s).re
  map_zero' := by simp
  map_add' x y := by simp [add_div, mul_add]

noncomputable def signChar (s : ℂ) : AddChar ℂ Circle :=
  Real.probChar.compAddMonoidHom (phaseMap s)

theorem signChar_self {s : ℂ} (hs : s ≠ 0) :
    ((signChar s s : Circle) : ℂ) = -1 := by
  simp [signChar, phaseMap, hs, Real.probChar_apply', Circle.coe_exp,
    Complex.exp_pi_mul_I]

noncomputable def sampleChar (T : Finset ℂ) : AddChar ℂ Circle :=
  ∏ s ∈ T, signChar s

theorem sampleChar_apply (T : Finset ℂ) (z : ℂ) :
    ((sampleChar T z : Circle) : ℂ) =
      ∏ s ∈ T, ((signChar s z : Circle) : ℂ) := by
  classical
  induction T using Finset.induction_on with
  | empty => simp [sampleChar]
  | @insert s T hs ih =>
      simp only [sampleChar] at ih ⊢
      simpa [hs] using congrArg
        (fun x : ℂ => ((signChar s z : Circle) : ℂ) * x) ih

/-- The sum is indexed by subsets, so duplicate characters retain their
intended multiplicity. -/
theorem sum_sampleChar_eq_zero (S : Finset ℂ) {z : ℂ}
    (hzS : z ∈ S) (hz : z ≠ 0) :
    (∑ T ∈ S.powerset, ((sampleChar T z : Circle) : ℂ)) = 0 := by
  classical
  simp_rw [sampleChar_apply]
  rw [← Finset.prod_one_add]
  exact Finset.prod_eq_zero hzS (by rw [signChar_self hz]; ring)

theorem sum_sampleChar_zero (S : Finset ℂ) :
    (∑ T ∈ S.powerset, ((sampleChar T 0 : Circle) : ℂ)) =
      (2 : ℂ) ^ S.card := by
  simp [Finset.card_powerset]

theorem sum_sampleChar_eq_ite (S : Finset ℂ) {z : ℂ}
    (hz : z = 0 ∨ z ∈ S) :
    (∑ T ∈ S.powerset, ((sampleChar T z : Circle) : ℂ)) =
      if z = 0 then (2 : ℂ) ^ S.card else 0 := by
  by_cases hzero : z = 0
  · subst z
    simp
  · have hzS : z ∈ S := hz.resolve_left hzero
    simp [hzero, sum_sampleChar_eq_zero S hzS hzero]

/-- A single finite character sample extracts the zero-frequency coefficient
of any finitely supported polynomial whose other frequencies lie in `S`.
There is no normalization or measure-theoretic hypothesis. -/
theorem sum_sampleChar_polynomial (S : Finset ℂ)
    {ι : Type*} (F : Finset ι) (freq : ι → ℂ) (a : ι → ℂ)
    (hfreq : ∀ i ∈ F, freq i = 0 ∨ freq i ∈ S) :
    (∑ T ∈ S.powerset,
      ∑ i ∈ F, a i * ((sampleChar T (freq i) : Circle) : ℂ)) =
        (2 : ℂ) ^ S.card * ∑ i ∈ F.filter (fun i => freq i = 0), a i := by
  classical
  rw [Finset.sum_comm]
  calc
    (∑ i ∈ F, ∑ T ∈ S.powerset,
        a i * ((sampleChar T (freq i) : Circle) : ℂ)) =
      ∑ i ∈ F, a i * (if freq i = 0 then (2 : ℂ) ^ S.card else 0) := by
        apply Finset.sum_congr rfl
        intro i hi
        rw [← Finset.mul_sum, sum_sampleChar_eq_ite S (hfreq i hi)]
    _ = (2 : ℂ) ^ S.card * ∑ i ∈ F.filter (fun i => freq i = 0), a i := by
      simp [Finset.mul_sum, Finset.sum_filter, mul_comm]

end Erdos.Research.FiniteOrthogonalCharacters

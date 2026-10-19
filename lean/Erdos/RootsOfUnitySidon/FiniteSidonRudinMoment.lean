import Erdos.RootsOfUnitySidon.FiniteSidonSampleMoment
import Erdos.RootsOfUnitySidon.FiniteComplexKhintchine

/-!
# Rudin's finite even-moment bound from a Sidon inequality

The same finite character sample works whenever its even moment is invariant
under twisting by an algebraic character. The orthogonal sample construction
supplies this hypothesis for any prescribed finite range of exponents.
-/

namespace Erdos.Research.SidonExtraction

open scoped BigOperators
open Erdos.Research.FiniteKhintchine
open Erdos.Research.FiniteComplexKhintchine
open Erdos.Research.FiniteOrthogonalCharacters
open Erdos.Research.FiniteMomentOrthogonality

private theorem rademacher_eq_sign {A : Finset ℂ} (ω : A → Bool) (a : A) :
    rademacherSign ω a = (sign (ω a) : ℂ) := by
  cases h : ω a <;> simp [rademacherSign, sign, h]

/-- The exact finite-sample form of Rudin's even-moment inequality. -/
theorem finiteSidonBound_rudin_moment_on_sample
    (A : Finset ℂ) (K : ℝ) (hK : 0 < K)
    (hA : FiniteSidonBound A K)
    {σ : Type*} (t : Finset σ) (eval : σ → A → ℂ)
    (heval : ∀ u a, ‖eval u a‖ = 1)
    (m : ℕ) (hm : 0 < m)
    (hInv : ∀ (d : A → ℂ) (ψ : AddChar ℂ Circle),
      (∑ u ∈ t, ‖∑ a : A, d a * eval u a * (ψ a.1 : ℂ)‖ ^ (2 * m)) =
      (∑ u ∈ t, ‖∑ a : A, d a * eval u a‖ ^ (2 * m)))
    (c : A → ℂ) :
    (∑ u ∈ t, ‖∑ a : A, c a * eval u a‖ ^ (2 * m)) ≤
      (t.card : ℝ) * (2 * K) ^ (2 * m) *
        ((48 * m : ℕ) : ℝ) ^ m * (∑ a : A, ‖c a‖ ^ 2) ^ m := by
  classical
  let V : ℝ := ∑ a : A, ‖c a‖ ^ 2
  have hpoint (u : σ) :
      (∑ ω : A → Bool,
        ‖∑ a : A, c a * rademacherSign ω a * eval u a‖ ^ (2 * m)) ≤
      (Fintype.card (A → Bool) : ℝ) * ((48 * m : ℕ) : ℝ) ^ m * V ^ m := by
    let b : A → ℂ := fun a => c a * eval u a
    have h := complex_even_moment_le_fintype b m hm
    have hpoly (ω : A → Bool) :
        (∑ a : A, c a * rademacherSign ω a * eval u a) =
        ∑ a : A, b a * (sign (ω a) : ℂ) := by
      apply Finset.sum_congr rfl
      intro a _
      rw [rademacher_eq_sign]
      ring
    have hb : (∑ a : A, ‖b a‖ ^ 2) = V := by
      apply Finset.sum_congr rfl
      intro a _
      simp [b, heval]
    simpa only [← hpoly, hb] using h
  have hComp := finiteSidonBound_rademacher_moment_comparison A K hK hA
    t eval (2 * m) (by omega) hInv c
  have hrandom :
      (∑ ω : A → Bool, ∑ u ∈ t,
        ‖∑ a : A, c a * rademacherSign ω a * eval u a‖ ^ (2 * m)) ≤
      (t.card : ℝ) *
        ((Fintype.card (A → Bool) : ℝ) *
          ((48 * m : ℕ) : ℝ) ^ m * V ^ m) := by
    rw [Finset.sum_comm]
    calc
      _ ≤ ∑ u ∈ t,
          ((Fintype.card (A → Bool) : ℝ) *
            ((48 * m : ℕ) : ℝ) ^ m * V ^ m) :=
              Finset.sum_le_sum fun u _ => hpoint u
      _ = _ := by simp
  have hcard : (0 : ℝ) < Fintype.card (A → Bool) := by
    exact_mod_cast Fintype.card_pos
  have hnonneg : 0 ≤ (2 * K) ^ (2 * m) := by positivity
  have h := hComp.trans (mul_le_mul_of_nonneg_left hrandom hnonneg)
  have h' :
      (Fintype.card (A → Bool) : ℝ) *
        (∑ u ∈ t, ‖∑ a : A, c a * eval u a‖ ^ (2 * m)) ≤
      (Fintype.card (A → Bool) : ℝ) *
        ((t.card : ℝ) * (2 * K) ^ (2 * m) *
          ((48 * m : ℕ) : ℝ) ^ m * V ^ m) := by
    nlinarith only [h]
  exact le_of_mul_le_mul_left h' hcard

/-- A fixed finite orthogonal sample supports Rudin's bound at every exponent
whose nonzero moment frequencies it contains. -/
theorem finiteSidonBound_rudin_moment_superset
    (A S : Finset ℂ) (K : ℝ) (hK : 0 < K)
    (hA : FiniteSidonBound A K)
    (m : ℕ) (hm : 0 < m)
    (hS : momentFrequencies A m ⊆ S)
    (c : A → ℂ) :
    (∑ T ∈ S.powerset,
      ‖∑ a : A, c a * ((sampleChar T a.1 : Circle) : ℂ)‖ ^ (2 * m)) ≤
      (2 : ℝ) ^ S.card * (2 * K) ^ (2 * m) *
        ((48 * m : ℕ) : ℝ) ^ m * (∑ a : A, ‖c a‖ ^ 2) ^ m := by
  classical
  let eval : Finset ℂ → A → ℂ :=
    fun T a => ((sampleChar T a.1 : Circle) : ℂ)
  have heval (T : Finset ℂ) (a : A) : ‖eval T a‖ = 1 :=
    Circle.norm_coe (sampleChar T a.1)
  have hInv (d : A → ℂ) (ψ : AddChar ℂ Circle) :
      (∑ T ∈ S.powerset,
        ‖∑ a : A, d a * eval T a * (ψ a.1 : ℂ)‖ ^ (2 * m)) =
      (∑ T ∈ S.powerset,
        ‖∑ a : A, d a * eval T a‖ ^ (2 * m)) := by
    let d' : ℂ → ℂ := fun z => if hz : z ∈ A then d ⟨z, hz⟩ else 0
    have h := sampled_even_moment_invariant_superset A d' ψ m S hS
    simp_rw [← A.sum_attach] at h
    simpa [d', eval] using h
  have h := finiteSidonBound_rudin_moment_on_sample A K hK hA
    S.powerset eval heval m hm hInv c
  simpa [eval, Finset.card_powerset] using h

end Erdos.Research.SidonExtraction

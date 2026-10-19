import Erdos.RootsOfUnitySidon.TensorExtension
import Erdos.RootsOfUnitySidon.AnalyticSliceSelection
import Erdos.RootsOfUnitySidon.SmallPrimeFiberBound

/-!
# Turning a finite tensor parameter into a Sidon bound

The tensor extension argument produces a positive-real parameter `ρ` for a
finite frequency set. This module converts it to the reciprocal Sidon constant
and transfers it through an injective additive evaluation map.
-/

namespace Erdos.Research.Problem774

open Erdos.Research.TensorExtension
open Erdos.Research.Problem774.SmallPrimeAnalytic

/-- A positive tensor parameter gives a positive-real bound on the same finite
frequency set. -/
theorem positiveRealBoundOn_of_parameter {G : Type*} [AddCommGroup G]
    (E : Finset G) (ρ : ℝ) (hρ : 0 < ρ)
    (h : PositiveRealParameter E ρ) :
    PositiveRealBoundOn (E : Set G) ρ⁻¹ := by
  classical
  intro A hA c
  let c' : G → ℂ := fun x => if x ∈ A then c x else 0
  obtain ⟨χ, hχ⟩ := h c'
  refine ⟨χ, ?_⟩
  have hsub : A ⊆ E := by
    intro x hx
    exact hA hx
  have hnorm : (∑ x ∈ E, ‖c' x‖) = ∑ x ∈ A, ‖c x‖ := by
    calc
      _ = ∑ x ∈ A, ‖c' x‖ := by
        apply (Finset.sum_subset hsub ?_).symm
        intro x _ hx
        simp [c', hx]
      _ = ∑ x ∈ A, ‖c x‖ := by
        apply Finset.sum_congr rfl
        intro x hx
        simp [c', hx]
  have hsum : (∑ x ∈ E, c' x * (χ x : ℂ)).re =
      (∑ x ∈ A, c x * (χ x : ℂ)).re := by
    congr 1
    calc
      _ = ∑ x ∈ A, c' x * (χ x : ℂ) := by
        apply (Finset.sum_subset hsub ?_).symm
        intro x _ hx
        simp [c', hx]
      _ = ∑ x ∈ A, c x * (χ x : ℂ) := by
        apply Finset.sum_congr rfl
        intro x hx
        simp [c', hx]
  rw [hnorm, hsum] at hχ
  calc
    (∑ x ∈ A, ‖c x‖) = ρ⁻¹ * (ρ * ∑ x ∈ A, ‖c x‖) := by
      rw [← mul_assoc, inv_mul_cancel₀ hρ.ne', one_mul]
    _ ≤ ρ⁻¹ * (∑ x ∈ A, c x * (χ x : ℂ)).re :=
      mul_le_mul_of_nonneg_left hχ (inv_nonneg.mpr hρ.le)

/-- Evaluate a finite free-tensor grid injectively in another additive group.
The positive-real constant is unchanged apart from inverting the parameter. -/
theorem positiveRealBoundOn_image_of_parameter {G H : Type*}
    [AddCommGroup G] [AddCommGroup H]
    (f : G →+ H) (hf : Function.Injective f)
    (E : Finset G) (ρ : ℝ) (hρ : 0 < ρ)
    (h : PositiveRealParameter E ρ) :
    PositiveRealBoundOn (f '' (E : Set G)) ρ⁻¹ :=
  positiveRealBoundOn_image_injective f hf (E : Set G) ρ⁻¹
    (positiveRealBoundOn_of_parameter E ρ hρ h)

end Erdos.Research.Problem774

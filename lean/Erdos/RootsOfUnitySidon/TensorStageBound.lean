import Erdos.RootsOfUnitySidon.TensorExtension
import Erdos.RootsOfUnitySidon.TensorPhaseLattice
import Mathlib.Analysis.SpecialFunctions.Complex.Arg
import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.Tactic

/-!
# Finite-stage positive-real tensor parameters

The one-frequency tensor has positive-real parameter one. If each new
simplex side supplies the one-step character estimate with loss
`3 Q / q²`, the losses telescope across any finite number of sides. The
one-step estimate is an explicit hypothesis here; no random-lift estimate is
asserted by this file.
-/

namespace Erdos.Research.Problem774.TensorStageBound

open Erdos.Research.Problem774.TensorPhaseLattice
open Erdos.Research.TensorExtension

/-- The first `k` simplex ranks for a sequence of side sizes `q`. -/
def stageRanks (q : ℕ → ℕ) (k : ℕ) : Fin k → ℕ :=
  fun i => q i.val - 1

/-- The finite family of free tensor frequencies at stage `k`. -/
noncomputable def stageFrequencies (q : ℕ → ℕ) (k : ℕ) :
    Finset (TensorLattice (Fin k) (stageRanks q k)) := by
  classical
  exact Finset.univ.image (tensorColumn (stageRanks q k))

/-- A positive-real parameter for the first `k` simplex sides. -/
def StageBound (q : ℕ → ℕ) (k : ℕ) (ρ : ℝ) : Prop :=
  PositiveRealParameter (stageFrequencies q k) ρ

/-- Align an arbitrary complex coefficient by a unit phase. -/
private theorem coefficient_phase_alignment (z : ℂ) :
    ∃ t : Circle, (z * (t : ℂ)).re = ‖z‖ := by
  let t : Circle := Circle.exp (-Complex.arg z)
  refine ⟨t, ?_⟩
  have ht : (t : ℂ) = Complex.exp (-(Complex.arg z * Complex.I)) := by
    simp [t, Circle.coe_exp, Complex.exp_neg, mul_comm]
  have hz : z * (t : ℂ) = (‖z‖ : ℂ) := by
    calc
      z * (t : ℂ) =
          ((‖z‖ : ℂ) * Complex.exp (Complex.arg z * Complex.I)) *
            Complex.exp (-(Complex.arg z * Complex.I)) := by
        calc
          z * (t : ℂ) =
              ((‖z‖ : ℂ) * Complex.exp (Complex.arg z * Complex.I)) *
                (t : ℂ) :=
            congrArg (fun w : ℂ => w * (t : ℂ))
              (Complex.norm_mul_exp_arg_mul_I z).symm
          _ = _ := by rw [ht]
      _ = (‖z‖ : ℂ) := by
        rw [mul_assoc, ← Complex.exp_add]
        simp
  rw [hz]
  simp

/-- Before adjoining any simplex side, the tensor index has one frequency
and its character phase can be chosen arbitrarily. -/
theorem stage_zero_parameter_one (q : ℕ → ℕ) : StageBound q 0 1 := by
  let n := stageRanks q 0
  let a₀ : TensorBasis (Fin 0) n := fun i => i.elim0
  let g := tensorColumn n (baseIndex n a₀)
  have hfreq : stageFrequencies q 0 = {g} := by
    ext x
    simp only [stageFrequencies, Finset.mem_image, Finset.mem_univ,
      true_and, Finset.mem_singleton]
    constructor
    · rintro ⟨j, rfl⟩
      have hj : j = baseIndex n a₀ := by
        funext i
        exact i.elim0
      rw [hj]
    · intro hx
      subst x
      exact ⟨baseIndex n a₀, rfl⟩
  intro c
  obtain ⟨t, ht⟩ := coefficient_phase_alignment (c g)
  let χ : AddChar (TensorLattice (Fin 0) n) Circle :=
    basisPhaseCharacter n (fun _ => t)
  refine ⟨χ, ?_⟩
  change (1 : ℝ) * (∑ x ∈ stageFrequencies q 0, ‖c x‖) ≤
    (∑ x ∈ stageFrequencies q 0, c x * (χ x : ℂ)).re
  rw [hfreq]
  simp only [Finset.sum_singleton, one_mul]
  rw [show g = tensorColumn n (baseIndex n a₀) by rfl,
    basisPhaseCharacter_baseIndex]
  exact le_of_eq ht.symm

/-- The loss incurred when adjoining a simplex side of size `q k`. -/
noncomputable def stageLoss (q : ℕ → ℕ) (Q : ℕ → ℝ) (k : ℕ) : ℝ :=
  3 * Q k / (q k : ℝ) ^ 2

/-- The parameter obtained by subtracting the losses of the first `k`
extension steps from the singleton parameter. -/
noncomputable def stageParameter (q : ℕ → ℕ) (Q : ℕ → ℝ) (k : ℕ) : ℝ :=
  1 - ∑ i ∈ Finset.range k, stageLoss q Q i

theorem stageParameter_zero (q : ℕ → ℕ) (Q : ℕ → ℝ) :
    stageParameter q Q 0 = 1 := by simp [stageParameter]

theorem stageParameter_succ (q : ℕ → ℕ) (Q : ℕ → ℝ) (k : ℕ) :
    stageParameter q Q (k + 1) =
      stageParameter q Q k - stageLoss q Q k := by
  simp [stageParameter, Finset.sum_range_succ]
  ring

/-- Any sequence satisfying the one-step lower recurrence stays above the
telescoped parameter. -/
theorem stageParameter_le_of_recurrence
    (q : ℕ → ℕ) (Q ρ : ℕ → ℝ)
    (hzero : 1 ≤ ρ 0)
    (hstep : ∀ k, ρ k - stageLoss q Q k ≤ ρ (k + 1)) :
    ∀ k, stageParameter q Q k ≤ ρ k := by
  intro k
  induction k with
  | zero => simpa [stageParameter_zero] using hzero
  | succ k ih =>
      rw [stageParameter_succ]
      linarith [hstep k]

/-- Conditional finite-stage iteration: any proved one-step tensor estimate
at each stage gives the explicitly telescoped positive-real parameter. -/
theorem stageBound_of_steps (q : ℕ → ℕ) (Q : ℕ → ℝ)
    (hstep : ∀ k,
      StageBound q k (stageParameter q Q k) →
        StageBound q (k + 1) (stageParameter q Q (k + 1))) :
    ∀ k, StageBound q k (stageParameter q Q k) := by
  intro k
  induction k with
  | zero => simpa [stageParameter_zero] using stage_zero_parameter_one q
  | succ k ih => exact hstep k ih

/-- A one-step bound stated directly with the analytic loss telescopes through
all finite stages. -/
theorem stageBound_of_step_loss (q : ℕ → ℕ) (Q : ℕ → ℝ)
    (hstep : ∀ k ρ,
      StageBound q k ρ →
        StageBound q (k + 1) (ρ - stageLoss q Q k)) :
    ∀ k, StageBound q k (stageParameter q Q k) := by
  apply stageBound_of_steps q Q
  intro k hk
  rw [stageParameter_succ]
  exact hstep k _ hk

/-- If the total finite loss is at most `C`, the same one-step hypotheses
give parameter at least `1 - C` at that stage. -/
theorem stageBound_of_loss_sum_le (q : ℕ → ℕ) (Q : ℕ → ℝ)
    (hstep : ∀ k,
      StageBound q k (stageParameter q Q k) →
        StageBound q (k + 1) (stageParameter q Q (k + 1)))
    (k : ℕ) (C : ℝ)
    (hloss : (∑ i ∈ Finset.range k, stageLoss q Q i) ≤ C) :
    StageBound q k (1 - C) := by
  have hstage := stageBound_of_steps q Q hstep k
  have hparameter : 1 - C ≤ stageParameter q Q k := by
    unfold stageParameter
    linarith
  intro a
  obtain ⟨χ, hχ⟩ := hstage a
  refine ⟨χ, ?_⟩
  have hnonneg : 0 ≤ ∑ g ∈ stageFrequencies q k, ‖a g‖ := by
    positivity
  nlinarith

end Erdos.Research.Problem774.TensorStageBound

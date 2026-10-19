import Erdos.RootsOfUnitySidon.TensorUniformStageMoment
import Erdos.RootsOfUnitySidon.TensorStageMoment
import Erdos.RootsOfUnitySidon.TailPrimeFieldBound
import Erdos.RootsOfUnitySidon.PrimeTailBounds
import Erdos.RootsOfUnitySidon.TensorUniformPrimeFactor
import Mathlib.Tactic

/-!
# Uniform positive-real parameter on finite prime-tail tensors

The concrete uniform rounding law feeds the finite-stage tensor theorem.
The remaining arithmetic input is a bound on the accumulated tensor-factor
loss for a finite increasing list of tail primes.
-/

namespace Erdos.Research.Problem774.TensorUniformPrimeTail

open Erdos.Research.Problem774.TensorPhaseLattice
open Erdos.Research.Problem774.TensorStageBound
open Erdos.Research.Problem774.TensorStageMoment
open Erdos.Research.Problem774.TensorUniformStageMoment
open Erdos.Research.Problem774.TailPrimeFieldBound
open Erdos.Research.Problem774.TensorUniformPrimeFactor
open Erdos.Research.TensorExtension

/-- A smaller positive-real parameter follows from a larger one on the same
finite frequency set. -/
theorem positiveRealParameter_mono {G : Type*} [AddCommGroup G]
    (E : Finset G) {ρ σ : ℝ} (hρσ : ρ ≤ σ)
    (hσ : PositiveRealParameter E σ) :
    PositiveRealParameter E ρ := by
  intro a
  obtain ⟨χ, hχ⟩ := hσ a
  refine ⟨χ, ?_⟩
  calc
    ρ * (∑ g ∈ E, ‖a g‖) ≤ σ * (∑ g ∈ E, ‖a g‖) :=
      mul_le_mul_of_nonneg_right hρσ
        (Finset.sum_nonneg fun g _ => norm_nonneg _)
    _ ≤ _ := hχ

/-- Every finite list of simplex sides at least three has the concrete
stage parameter supplied by uniformly symmetrized rounding. -/
theorem finite_list_uniform_stage_parameter (ps : List ℕ)
    (hside : ∀ p ∈ ps, 3 ≤ p) :
    StageBound (listSides ps) ps.length
      (stageParameter (listSides ps)
        (uniformStageQ (listSides ps)) ps.length) := by
  exact finite_side_list_parameter ps
    (uniformStageQ (listSides ps)) hside
    (fun k _ => uniform_stage_moment_law (listSides ps) k)

/-- A bound of one half on the finite loss yields a fixed parameter one
half, independent of the number of selected tail-prime factors. -/
theorem finite_list_uniform_half_parameter (ps : List ℕ)
    (hside : ∀ p ∈ ps, 3 ≤ p)
    (hloss : (∑ i ∈ Finset.range ps.length,
      stageLoss (listSides ps) (uniformStageQ (listSides ps)) i) ≤
        (1 / 2 : ℝ)) :
    StageBound (listSides ps) ps.length (1 / 2 : ℝ) := by
  have hparam : (1 / 2 : ℝ) ≤
      stageParameter (listSides ps)
        (uniformStageQ (listSides ps)) ps.length := by
    unfold stageParameter
    linarith
  exact positiveRealParameter_mono
    (stageFrequencies (listSides ps) ps.length) hparam
    (finite_list_uniform_stage_parameter ps hside)

/-- Reindex the total stage loss of an increasing list by its finite set of
prime entries. -/
theorem total_stageLoss_eq_selectedLoss (ps : List ℕ)
    (hsort : ps.SortedLT) (hside : ∀ p ∈ ps, 3 ≤ p) :
    (∑ i ∈ Finset.range ps.length,
      stageLoss (listSides ps) (uniformStageQ (listSides ps)) i) =
      ∑ p ∈ ps.toFinset,
        3 * Real.pi ^ 2 * PrimeTailBounds.priorTensorProd ps.toFinset p /
          (p : ℝ) ^ 2 := by
  classical
  let f : ℕ → ℝ := fun p =>
    3 * Real.pi ^ 2 * PrimeTailBounds.priorTensorProd ps.toFinset p /
      (p : ℝ) ^ 2
  have hinj : ∀ i ∈ Finset.range ps.length, ∀ j ∈ Finset.range ps.length,
      listSides ps i = listSides ps j → i = j := by
    intro i hi j hj hij
    have hii : i < ps.length := Finset.mem_range.mp hi
    have hjj : j < ps.length := Finset.mem_range.mp hj
    rw [listSides_getElem ps i hii, listSides_getElem ps j hjj] at hij
    exact (hsort.nodup.getElem_inj_iff (hi := hii) (hj := hjj)).mp hij
  have himage : (Finset.range ps.length).image (listSides ps) = ps.toFinset := by
    ext p
    constructor
    · intro hp
      obtain ⟨i, hi, hip⟩ := Finset.mem_image.mp hp
      have hii : i < ps.length := Finset.mem_range.mp hi
      rw [listSides_getElem ps i hii] at hip
      exact List.mem_toFinset.mpr (hip ▸ List.getElem_mem hii)
    · intro hp
      have hpList : p ∈ ps := List.mem_toFinset.mp hp
      obtain ⟨i, hi, hpi⟩ := List.mem_iff_getElem.mp hpList
      apply Finset.mem_image.mpr
      refine ⟨i, Finset.mem_range.mpr hi, ?_⟩
      simpa [listSides_getElem ps i hi] using hpi
  calc
    (∑ i ∈ Finset.range ps.length,
      stageLoss (listSides ps) (uniformStageQ (listSides ps)) i) =
        ∑ i ∈ Finset.range ps.length, f (listSides ps i) := by
      apply Finset.sum_congr rfl
      intro i hi
      have hii : i < ps.length := Finset.mem_range.mp hi
      rw [stageLoss_listSides_eq_priorTensorProd hsort hside i hii,
        listSides_getElem ps i hii]
    _ = ∑ p ∈ (Finset.range ps.length).image (listSides ps), f p := by
      rw [Finset.sum_image]
      exact hinj
    _ = _ := by rw [himage]

/-- One cutoff gives parameter one half for every finite increasing list of
prime tensor sides above that cutoff. -/
theorem exists_cutoff_uniform_stage_half_parameter :
    ∃ R : ℕ, 7 ≤ R ∧ ∀ ps : List ℕ, ps.SortedLT →
      (∀ p ∈ ps, p.Prime ∧ R < p) →
      StageBound (listSides ps) ps.length (1 / 2 : ℝ) := by
  obtain ⟨R, hR, hloss⟩ :=
    PrimeTailBounds.exists_cutoff_uniform_primeListLoss_lt_one
  refine ⟨R, hR, ?_⟩
  intro ps hsort hps
  have hside : ∀ p ∈ ps, 3 ≤ p := by
    intro p hp
    have hpR := (hps p hp).2
    omega
  have hbig := hloss ps hps
  have hsum := total_stageLoss_eq_selectedLoss ps hsort hside
  have hhalf :
      (∑ i ∈ Finset.range ps.length,
        stageLoss (listSides ps) (uniformStageQ (listSides ps)) i) ≤
          (1 / 2 : ℝ) := by
    rw [hsum]
    have hscale :
        (∑ p ∈ ps.toFinset,
          3 * Real.pi ^ 2 * PrimeTailBounds.priorTensorProd ps.toFinset p /
            (p : ℝ) ^ 2) =
          (1 / 2 : ℝ) *
            (∑ p ∈ ps.toFinset,
              (6 * Real.pi ^ 2) *
                PrimeTailBounds.priorTensorProd ps.toFinset p /
                  (p : ℝ) ^ 2) := by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro p _
      ring
    rw [hscale]
    linarith
  exact finite_list_uniform_half_parameter ps hside hhalf

end Erdos.Research.Problem774.TensorUniformPrimeTail

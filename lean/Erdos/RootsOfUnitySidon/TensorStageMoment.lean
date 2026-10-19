import Erdos.RootsOfUnitySidon.TensorStageEquiv
import Erdos.RootsOfUnitySidon.SmallPrimeAnalytic
import Mathlib.Tactic

/-!
# Finite-stage tensor parameter from explicit rounding moments

At every stage, the hypothesis is a finite probability law on integer
additive phases with exact coordinate means and a uniform second-moment
bound. The tensor-extension theorem, an algebraic reindexing of adjacent
stages, and numerical telescoping then give the finite-stage positive-real
parameter. This file does not assert the existence of the rounding laws.
-/

namespace Erdos.Research.Problem774.TensorStageMoment

open Erdos.Research.Problem774.TensorPhaseLattice
open Erdos.Research.Problem774.TensorStageBound
open Erdos.Research.Problem774.TensorStageEquiv
open Erdos.Research.Problem774.TensorStageAssembly
open Erdos.Research.TensorExtension

/-- The exact finite rounding law needed at stage `k`. -/
def StageMomentLaw (q : ℕ → ℕ) (Q : ℕ → ℝ) (k : ℕ) : Prop :=
  ∀ θ : AddChar (TensorLattice (Fin k) (stageRanks q k)) Circle,
    ∃ (s : Finset (TensorLattice (Fin k) (stageRanks q k) →+ ℤ))
      (w : (TensorLattice (Fin k) (stageRanks q k) →+ ℤ) → ℝ),
      (∀ FZ ∈ s, 0 ≤ w FZ) ∧
      (∑ FZ ∈ s, w FZ) = 1 ∧
      (∀ g ∈ stageFrequencies q k,
        (∑ FZ ∈ s, w FZ *
          (TensorRealCharacter.globalRealLiftHom (stageRanks q k) θ g -
            (2 * Real.pi) * (FZ g : ℝ))) = 0) ∧
      (∀ g ∈ stageFrequencies q k,
        (∑ FZ ∈ s, w FZ *
          (TensorRealCharacter.globalRealLiftHom (stageRanks q k) θ g -
            (2 * Real.pi) * (FZ g : ℝ)) ^ 2) ≤ Q k)

private theorem stage_frequency_nonzero (q : ℕ → ℕ)
    (k : ℕ) (hq : ∀ i < k, 3 ≤ q i)
    (g : TensorLattice (Fin k) (stageRanks q k))
    (hg : g ∈ stageFrequencies q k) : g ≠ 0 := by
  classical
  unfold stageFrequencies at hg
  obtain ⟨j, _, rfl⟩ := Finset.mem_image.mp hg
  have hn (i : Fin k) : 0 < stageRanks q k i := by
    dsimp [stageRanks]
    have hi := hq i.val i.isLt
    omega
  obtain ⟨a, ha⟩ := SmallPrimeAnalytic.tensorColumn_nonzero
    (stageRanks q k) hn j
  intro hz
  exact ha (congrArg (fun x : TensorLattice (Fin k) (stageRanks q k) => x a) hz)

/-- A concrete stage rounding law gives the next positive-real parameter
after one simplex extension. -/
theorem stage_step_of_moment_law (q : ℕ → ℕ) (Q : ℕ → ℝ)
    (k : ℕ) (hq : ∀ i < k + 1, 3 ≤ q i) (ρ : ℝ)
    (hbase : StageBound q k ρ)
    (hround : StageMomentLaw q Q k) :
    StageBound q (k + 1) (ρ - stageLoss q Q k) := by
  let n := stageRanks q k
  let r := q k - 1
  have hr : 2 ≤ r := by
    dsimp [r]
    have hk := hq k (by omega)
    omega
  have hE : ∀ g ∈ stageFrequencies q k, g ≠ 0 :=
    fun g hg => stage_frequency_nonzero q k
      (fun i hi => hq i (by omega)) g hg
  have hnext := next_parameter_of_rounding_nonzero n r hr
    (stageFrequencies q k) (Q k) ρ hbase hE hround
  have htransport := positiveRealParameter_image
    (stageTensorEquiv q k) (nextFrequencies (stageFrequencies q k) r)
    (ρ - 3 * Q k / ((r + 1 : ℕ) : ℝ) ^ 2) hnext
  change PositiveRealParameter (stageFrequencies q (k + 1))
    (ρ - stageLoss q Q k)
  rw [stageFrequencies_succ]
  have hrq : r + 1 = q k := by
    dsimp [r]
    have hk := hq k
    omega
  simpa [stageLoss, r, hrq] using htransport

/-- Iterating the explicit finite moment laws gives the parameter at every
finite tensor stage. -/
theorem finite_stage_parameter_of_moment_laws
    (q : ℕ → ℕ) (Q : ℕ → ℝ)
    (hq : ∀ k, 3 ≤ q k)
    (hround : ∀ k, StageMomentLaw q Q k) :
    ∀ k, StageBound q k (stageParameter q Q k) := by
  apply stageBound_of_steps q Q
  intro k hk
  have hstep := stage_step_of_moment_law q Q k
    (fun i _ => hq i)
    (stageParameter q Q k) hk (hround k)
  simpa [stageParameter_succ] using hstep

/-- The finite-prefix form applies directly to a list of side sizes, after
extending that list to a function `q : ℕ → ℕ` in any way. Only the first `k`
side sizes and moment laws enter the conclusion. -/
theorem finite_stage_parameter_of_moment_laws_prefix
    (q : ℕ → ℕ) (Q : ℕ → ℝ) (k : ℕ)
    (hq : ∀ i < k, 3 ≤ q i)
    (hround : ∀ i < k, StageMomentLaw q Q i) :
    StageBound q k (stageParameter q Q k) := by
  have aux : ∀ m : ℕ,
      (∀ i < m, 3 ≤ q i) →
      (∀ i < m, StageMomentLaw q Q i) →
      StageBound q m (stageParameter q Q m) := by
    intro m
    induction m with
    | zero =>
        intro _ _
        simpa [stageParameter_zero] using stage_zero_parameter_one q
    | succ m ih =>
        intro hqm hrm
        have hprior : StageBound q m (stageParameter q Q m) :=
          ih (fun i hi => hqm i (by omega))
            (fun i hi => hrm i (by omega))
        have hstep := stage_step_of_moment_law q Q m hqm
          (stageParameter q Q m) hprior (hrm m (by omega))
        simpa [stageParameter_succ] using hstep
  exact aux k hq hround

/-- Extend a finite ordered list of simplex side sizes by the harmless
default side size three. All statements at the list length use only entries
of the list. -/
def listSides (qs : List ℕ) (i : ℕ) : ℕ := (qs[i]?).getD 3

theorem listSides_getElem (qs : List ℕ) (i : ℕ) (hi : i < qs.length) :
    listSides qs i = qs[i] := by
  simp [listSides, List.getElem?_eq_getElem hi]

/-- The finite-list form of the moment-law theorem. This applies in
particular to any increasing list of odd primes. -/
theorem finite_side_list_parameter (qs : List ℕ) (Q : ℕ → ℝ)
    (hside : ∀ p ∈ qs, 3 ≤ p)
    (hround : ∀ i < qs.length, StageMomentLaw (listSides qs) Q i) :
    StageBound (listSides qs) qs.length
      (stageParameter (listSides qs) Q qs.length) := by
  apply finite_stage_parameter_of_moment_laws_prefix
  · intro i hi
    rw [listSides_getElem qs i hi]
    exact hside qs[i] (List.getElem_mem hi)
  · exact hround

/-- The loss expression in the finite-list theorem, written directly in
terms of its entries. -/
theorem stageParameter_listSides (qs : List ℕ) (Q : ℕ → ℝ) :
    stageParameter (listSides qs) Q qs.length =
      1 - ∑ i ∈ Finset.range qs.length,
        3 * Q i / (qs[i]?.getD 3 : ℝ) ^ 2 := by
  rfl

end Erdos.Research.Problem774.TensorStageMoment

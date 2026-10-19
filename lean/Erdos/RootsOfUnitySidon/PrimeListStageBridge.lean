import Erdos.RootsOfUnitySidon.TailPrimeFieldBound
import Erdos.RootsOfUnitySidon.TensorStageBound

/-!
# Finite prime lists as tensor stages

A sequence of simplex side sizes that agrees with a finite prime list on its
initial segment has exactly the same rank function and free frequency grid at
that stage. This lets finite-stage parameter theorems feed the tail-prime
cyclotomic-field transfer without changing the frequencies being bounded.
-/

namespace Erdos.Research.Problem774.PrimeListStageBridge

open Erdos.Research.Problem774.TensorStageBound
open Erdos.Research.Problem774.TailPrimeFieldBound
open Erdos.Research.Problem774.TensorPhaseLattice
open Erdos.Research.TensorExtension

private noncomputable def tensorGrid {I : Type*} [Fintype I]
    (r : I → ℕ) : Finset (TensorLattice I r) := by
  classical
  exact Finset.univ.image (tensorColumn r)

private theorem stageFrequencies_eq_tensorGrid (q : ℕ → ℕ) (k : ℕ) :
    stageFrequencies q k = tensorGrid (stageRanks q k) := by
  classical
  ext x
  simp [stageFrequencies, tensorGrid]

private theorem tailFreeGrid_eq_tensorGrid (ps : List ℕ) :
    tailFreeGrid ps = tensorGrid (tailRanks ps) := by
  classical
  ext x
  simp [tailFreeGrid, tensorGrid]

private theorem tensorGrid_cast {I : Type*} [Fintype I]
    (r s : I → ℕ) (h : r = s) :
    h ▸ tensorGrid r = tensorGrid s := by
  cases h
  rfl

private theorem tensorParameter_of_ranks_eq {I : Type*} [Fintype I]
    (r s : I → ℕ) (h : r = s) (ρ : ℝ)
    (hp : PositiveRealParameter (tensorGrid r) ρ) :
    PositiveRealParameter (tensorGrid s) ρ := by
  cases h
  exact hp

/-- Extend a finite prime list to an infinite side-size sequence, using `3`
after the list ends. -/
def primeListSides (ps : List ℕ) (k : ℕ) : ℕ :=
  if h : k < ps.length then ps[k] else 3

theorem primeListSides_get (ps : List ℕ) (i : Fin ps.length) :
    primeListSides ps i.val = ps.get i := by
  simp [primeListSides, i.isLt]

/-- The stage ranks agree with the prime-list ranks whenever the side sizes
agree on the relevant prefix. -/
theorem stageRanks_eq_tailRanks (ps : List ℕ) (q : ℕ → ℕ)
    (hq : ∀ i : Fin ps.length, q i.val = ps.get i) :
    stageRanks q ps.length = tailRanks ps := by
  funext i
  simp [stageRanks, tailRanks, hq i]

/-- Transport the finite stage frequency set across equality of its rank
function. The transported set is exactly the free tail-prime grid. -/
theorem stageFrequencies_cast_eq_tailFreeGrid (ps : List ℕ) (q : ℕ → ℕ)
    (hq : ∀ i : Fin ps.length, q i.val = ps.get i) :
    (stageRanks_eq_tailRanks ps q hq) ▸ stageFrequencies q ps.length =
      tailFreeGrid ps := by
  rw [stageFrequencies_eq_tensorGrid, tailFreeGrid_eq_tensorGrid]
  exact tensorGrid_cast (stageRanks q ps.length) (tailRanks ps)
    (stageRanks_eq_tailRanks ps q hq)

/-- A stage parameter on a matching sequence is a parameter on the exact
finite prime-list grid used by the cyclotomic evaluation. -/
theorem tailFreeGrid_parameter_of_stage (ps : List ℕ) (q : ℕ → ℕ)
    (hq : ∀ i : Fin ps.length, q i.val = ps.get i)
    (ρ : ℝ) (h : StageBound q ps.length ρ) :
    PositiveRealParameter (tailFreeGrid ps) ρ := by
  rw [tailFreeGrid_eq_tensorGrid]
  apply tensorParameter_of_ranks_eq
    (stageRanks q ps.length) (tailRanks ps)
    (stageRanks_eq_tailRanks ps q hq) ρ
  simpa only [StageBound, stageFrequencies_eq_tensorGrid] using h

/-- The canonical extension agrees with the finite list and so specializes
the generic stage-to-grid transport. -/
theorem primeListSides_stageFrequencies_eq (ps : List ℕ) :
    (stageRanks_eq_tailRanks ps (primeListSides ps)
      (primeListSides_get ps)) ▸
        stageFrequencies (primeListSides ps) ps.length = tailFreeGrid ps :=
  stageFrequencies_cast_eq_tailFreeGrid ps (primeListSides ps)
    (primeListSides_get ps)

end Erdos.Research.Problem774.PrimeListStageBridge

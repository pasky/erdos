import Erdos.RootsOfUnitySidon.PrimeSimplexGrid
import Erdos.RootsOfUnitySidon.FieldTensorEvaluation

/-!
# Evaluation of prime tensor columns with tail-field coefficients

This module connects the squarefree prime-grid coordinates to the
field-tensor evaluation map used in the analytic slice argument.
-/

namespace Erdos.Research.Problem774.PrimeSimplexGrid

open scoped Classical
open Erdos.Research.Problem774.PrimeSimplex
open Erdos.Research.Problem774.TensorCRT
open Erdos.Research.Problem774.TensorPhaseLattice
open Erdos.Research.Problem774.FieldTensorEvaluation
open Erdos.Research.Problem774.SmallPrimeAnalytic

/-- Tail-field coefficients multiply the evaluated small-prime tensor
column frequency exactly as complex scalars. -/
theorem fieldTensorFrequency_evaluation_eq_prod (small tail : List ℕ)
    (hsmall : ∀ p ∈ small, p.Prime)
    (j : TensorIndex (Fin small.length) (fun i => small.get i - 1))
    (z : primeField tail.prod) :
    evaluation (primeField tail.prod)
      (fun i : Fin small.length => small.get i - 1)
      (primeBasisValue small)
      (fieldTensorFrequency (primeField tail.prod)
        (fun i : Fin small.length => small.get i - 1) j z) =
      (z : ℂ) * ∏ i : Fin small.length,
        PrimeSimplex.zeta (small.get i) ^ (j i : ℕ) := by
  letI : DecidableEq (Fin small.length) := Classical.decEq _
  rw [evaluation_fieldTensorFrequency]
  have hsum :
      (∑ a : TensorBasis (Fin small.length) (fun i => small.get i - 1),
        (tensorColumn (fun i : Fin small.length => small.get i - 1) j a : ℂ) *
          primeBasisValue small a) =
        ∏ i : Fin small.length,
          PrimeSimplex.zeta (small.get i) ^ (j i : ℕ) := by
    convert prime_tensorColumn_evaluation small hsmall j using 1
    apply Finset.sum_congr
    · ext a
      simp
    · intro a _
      rfl
  exact congrArg (fun w : ℂ => (z : ℂ) * w) hsum

/-- A tail-root scalar times a small-prime tensor column evaluates to the
product of that scalar with the small squarefree root selected by the grid
equivalence. -/
theorem fieldTensorFrequency_evaluation_eq_root (small tail : List ℕ)
    (hsmall : ∀ p ∈ small, p.Prime) (hsmall_nodup : small.Nodup)
    (j : TensorIndex (Fin small.length) (fun i => small.get i - 1))
    (z : primeField tail.prod) :
    evaluation (primeField tail.prod)
      (fun i : Fin small.length => small.get i - 1)
      (primeBasisValue small)
      (fieldTensorFrequency (primeField tail.prod)
        (fun i : Fin small.length => small.get i - 1) j z) =
      (z : ℂ) *
        ((primeGridEquiv small hsmall hsmall_nodup
          ((primeIndexColumnEquiv small hsmall).symm j) : RootGrid small.prod) : ℂ) := by
  rw [fieldTensorFrequency_evaluation_eq_prod small tail hsmall j z]
  rw [primeGridEquiv_val_eq_prod]
  congr 1

end Erdos.Research.Problem774.PrimeSimplexGrid

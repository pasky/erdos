import Erdos.RootsOfUnitySidon.PrimeSimplexGrid
import Erdos.RootsOfUnitySidon.TensorParameterTransfer

/-!
# Tail-prime tensor bounds in a cyclotomic field

The free simplex tensor grid for a finite list of distinct tail primes
evaluates injectively in the corresponding cyclotomic field. A positive-real
parameter on that free grid therefore gives a positive-real bound on its
evaluated finite set, with the same reciprocal constant.
-/

namespace Erdos.Research.Problem774.TailPrimeFieldBound

open Erdos.Research.Problem774.PrimeSimplex
open Erdos.Research.Problem774.PrimeSimplexGrid
open Erdos.Research.Problem774.TensorCRT
open Erdos.Research.Problem774.TensorPhaseLattice
open Erdos.Research.TensorExtension

/-- The rank of each prime simplex side. -/
def tailRanks (ps : List ℕ) : Fin ps.length → ℕ :=
  fun i => ps.get i - 1

/-- The free additive tensor frequency grid for the given tail primes. -/
noncomputable def tailFreeGrid (ps : List ℕ) :
    Finset (TensorLattice (Fin ps.length) (tailRanks ps)) := by
  classical
  exact Finset.univ.image (tensorColumn (tailRanks ps))

/-- A free simplex basis value, viewed in the cyclotomic field of the product
order. -/
noncomputable def primeBasisFieldValue (ps : List ℕ)
    (hprime : ∀ p ∈ ps, p.Prime) (a : PrimeBasis ps) :
    primeField ps.prod :=
  ⟨primeBasisValue ps a,
    simplexValue_mem_primeField ps hprime ((recursiveBasisEquiv ps).symm a)⟩

theorem primeBasisFieldValue_linearIndependent (ps : List ℕ)
    (hprime : ∀ p ∈ ps, p.Prime) (hnodup : ps.Nodup) :
    LinearIndependent ℚ (primeBasisFieldValue ps hprime) := by
  have hli : LinearIndependent ℚ (primeBasisValue ps) :=
    LinearIndependent.comp (simplex_linearIndependent ps hprime hnodup)
      (recursiveBasisEquiv ps).symm (recursiveBasisEquiv ps).symm.injective
  apply LinearIndependent.of_comp
    (primeField ps.prod).toSubalgebra.toSubmodule.subtype
  exact hli

/-- Evaluate integer tensor coordinates against their cyclotomic basis
values. -/
noncomputable def tailGridEvaluation (ps : List ℕ)
    (hprime : ∀ p ∈ ps, p.Prime) :
    TensorLattice (Fin ps.length) (tailRanks ps) →+ primeField ps.prod := by
  classical
  exact (Fintype.linearCombination ℤ (primeBasisFieldValue ps hprime)).toAddMonoidHom

theorem tailGridEvaluation_injective (ps : List ℕ)
    (hprime : ∀ p ∈ ps, p.Prime) (hnodup : ps.Nodup) :
    Function.Injective (tailGridEvaluation ps hprime) := by
  classical
  have hli : LinearIndependent ℤ (primeBasisFieldValue ps hprime) :=
    (primeBasisFieldValue_linearIndependent ps hprime hnodup).restrict_scalars' ℤ
  exact hli.fintypeLinearCombination_injective

/-- The field-valued evaluation agrees with the complex evaluation of the
same free tensor coordinates. -/
theorem tailGridEvaluation_coe (ps : List ℕ)
    (hprime : ∀ p ∈ ps, p.Prime)
    (x : TensorLattice (Fin ps.length) (tailRanks ps)) :
    ((tailGridEvaluation ps hprime x : primeField ps.prod) : ℂ) =
      primeLatticeEvaluation ps x := by
  classical
  have key : ∀ y : PrimeBasis ps → ℤ,
      (((Fintype.linearCombination ℤ (primeBasisFieldValue ps hprime)) y :
        primeField ps.prod) : ℂ) =
      (Fintype.linearCombination ℤ (primeBasisValue ps)) y := by
    intro y
    simp [Fintype.linearCombination_apply, zsmul_eq_mul, primeBasisFieldValue]
  exact key x

/-- An evaluated free tensor column is the root selected by the squarefree
prime-grid equivalence. -/
theorem tailGridEvaluation_tensorColumn_coe (ps : List ℕ)
    (hprime : ∀ p ∈ ps, p.Prime) (hnodup : ps.Nodup)
    (j : TensorIndex (Fin ps.length) (tailRanks ps)) :
    ((tailGridEvaluation ps hprime (tensorColumn (tailRanks ps) j) :
      primeField ps.prod) : ℂ) =
      ((primeGridEquiv ps hprime hnodup
        ((primeIndexColumnEquiv ps hprime).symm j) : RootGrid ps.prod) : ℂ) := by
  calc
    ((tailGridEvaluation ps hprime (tensorColumn (tailRanks ps) j) :
        primeField ps.prod) : ℂ) =
        ∏ i : Fin ps.length, zeta (ps.get i) ^ (j i : ℕ) := by
          rw [tailGridEvaluation_coe]
          exact primeLatticeEvaluation_tensorColumn ps hprime j
    _ = ((primeGridEquiv ps hprime hnodup
          ((primeIndexColumnEquiv ps hprime).symm j) : RootGrid ps.prod) : ℂ) := by
      rw [primeGridEquiv_val_eq_prod]
      apply Finset.prod_congr rfl
      intro i _
      rfl

/-- The represented free tensor grid is exactly the set of roots of product
order in its cyclotomic field. -/
theorem tailGridEvaluation_image_eq_roots (ps : List ℕ)
    (hprime : ∀ p ∈ ps, p.Prime) (hnodup : ps.Nodup) :
    ((tailGridEvaluation ps hprime) '' (tailFreeGrid ps : Set _)) =
      {w : primeField ps.prod | (w : ℂ) ^ ps.prod = 1} := by
  classical
  ext w
  constructor
  · rintro ⟨x, hx, rfl⟩
    obtain ⟨j, _, rfl⟩ := Finset.mem_image.mp (Finset.mem_coe.mp hx)
    change (((tailGridEvaluation ps hprime (tensorColumn (tailRanks ps) j) :
      primeField ps.prod) : ℂ) ^ ps.prod) = 1
    rw [tailGridEvaluation_tensorColumn_coe ps hprime hnodup j]
    exact (primeGridEquiv ps hprime hnodup
      ((primeIndexColumnEquiv ps hprime).symm j)).property
  · intro hw
    let r : RootGrid ps.prod := ⟨(w : ℂ), hw⟩
    let j0 : PrimeIndex ps := (primeGridEquiv ps hprime hnodup).symm r
    let j : TensorIndex (Fin ps.length) (tailRanks ps) :=
      primeIndexColumnEquiv ps hprime j0
    refine ⟨tensorColumn (tailRanks ps) j, ?_, ?_⟩
    · exact Finset.mem_coe.mpr
        (Finset.mem_image.mpr ⟨j, Finset.mem_univ _, rfl⟩)
    · apply Subtype.ext
      simpa [j, j0, r] using
        (tailGridEvaluation_tensorColumn_coe ps hprime hnodup j)

/-- Any positive-real parameter on the free tail-prime grid transfers to
its represented frequencies inside the product cyclotomic field. -/
theorem positiveRealBoundOn_tailFieldGrid_of_parameter (ps : List ℕ)
    (hprime : ∀ p ∈ ps, p.Prime) (hnodup : ps.Nodup)
    (ρ : ℝ) (hρ : 0 < ρ)
    (hparam : PositiveRealParameter (tailFreeGrid ps) ρ) :
    PositiveRealBoundOn
      ((tailGridEvaluation ps hprime) '' (tailFreeGrid ps : Set _)) ρ⁻¹ :=
  positiveRealBoundOn_image_of_parameter
    (tailGridEvaluation ps hprime)
    (tailGridEvaluation_injective ps hprime hnodup)
    (tailFreeGrid ps) ρ hρ hparam

/-- The same bound stated on the actual finite root grid inside the product
cyclotomic field. -/
theorem positiveRealBoundOn_tailFieldRoots_of_parameter (ps : List ℕ)
    (hprime : ∀ p ∈ ps, p.Prime) (hnodup : ps.Nodup)
    (ρ : ℝ) (hρ : 0 < ρ)
    (hparam : PositiveRealParameter (tailFreeGrid ps) ρ) :
    PositiveRealBoundOn
      {w : primeField ps.prod | (w : ℂ) ^ ps.prod = 1} ρ⁻¹ := by
  rw [← tailGridEvaluation_image_eq_roots ps hprime hnodup]
  exact positiveRealBoundOn_tailFieldGrid_of_parameter ps hprime hnodup ρ hρ hparam

end Erdos.Research.Problem774.TailPrimeFieldBound

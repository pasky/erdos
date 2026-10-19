import Erdos.RootsOfUnitySidon.TensorLiftAssembly
import Erdos.RootsOfUnitySidon.TensorStageBound
import Mathlib.Tactic

/-!
# Passing the finite rounding estimate to a set-level tensor stage

The one-step theorem in `TensorLiftAssembly` is indexed by an old frequency
and a new simplex column. Under the algebraic injectivity of that indexing,
it becomes a positive-real parameter for the finite set of new tensor
frequencies. The only analytic input is the explicit finite rounding law and
its coordinate moment bound.
-/

namespace Erdos.Research.Problem774.TensorStageAssembly

open Erdos.Research.Problem774.TensorPhaseLattice
open Erdos.Research.Problem774.TensorLiftAssembly
open Erdos.Research.TensorExtension

private theorem nextFrequency_last_apply {G : Type*} [AddCommGroup G]
    (r : ℕ) (g : G) (a : Fin r) :
    nextFrequency r g (Fin.last r) a = -g := by
  classical
  simp [nextFrequency, SimplexTorus.column_last, SimplexTorus.lastColumn,
    SimplexTorus.basis, Pi.single_apply]

/-- A nonzero old frequency, tensored with one of at least three simplex
columns, has a unique old-frequency and column index. -/
theorem nextFrequency_injective_nonzero {G : Type*} [AddCommGroup G]
    (r : ℕ) (hr : 2 ≤ r) {g h : G} (hg : g ≠ 0) (hh : h ≠ 0)
    {j k : Fin (r + 1)}
    (heq : nextFrequency r g j = nextFrequency r h k) :
    g = h ∧ j = k := by
  haveI : Nontrivial (Fin r) := Fin.nontrivial_iff_two_le.mpr hr
  induction j using Fin.lastCases with
  | cast i =>
      induction k using Fin.lastCases with
      | cast l =>
          have hil : i = l := by
            by_contra hne
            have ha := congrArg (fun f : NextTensor G r => f i) heq
            simp [nextFrequency_castSucc, hne] at ha
            exact hg ha
          subst l
          have ha := congrArg (fun f : NextTensor G r => f i) heq
          simp [nextFrequency_castSucc] at ha
          exact ⟨ha, rfl⟩
      | last =>
          obtain ⟨a, hai⟩ : ∃ a : Fin r, a ≠ i := exists_ne i
          have ha := congrArg (fun f : NextTensor G r => f a) heq
          simp [nextFrequency_castSucc, hai,
            nextFrequency_last_apply] at ha
          exact False.elim (hh ha)
  | last =>
      induction k using Fin.lastCases with
      | cast i =>
          obtain ⟨a, hai⟩ : ∃ a : Fin r, a ≠ i := exists_ne i
          have ha := congrArg (fun f : NextTensor G r => f a) heq
          simp [nextFrequency_castSucc, hai,
            nextFrequency_last_apply] at ha
          exact False.elim (hg ha)
      | last =>
          let a : Fin r := ⟨0, by omega⟩
          have ha := congrArg (fun f : NextTensor G r => f a) heq
          simp only [nextFrequency_last_apply] at ha
          exact ⟨neg_injective ha, rfl⟩

/-- The set of frequencies after adjoining a simplex side of size `r+1`. -/
noncomputable def nextFrequencies {G : Type*} [AddCommGroup G]
    (E : Finset G) (r : ℕ) : Finset (NextTensor G r) := by
  classical
  exact (E.product (Finset.univ : Finset (Fin (r + 1)))).image
    (fun gj => nextFrequency r gj.1 gj.2)

/-- Reindex the coefficient norm from a finite image to its old-frequency
and new-column coordinates. -/
private theorem nextFrequencies_sum {G : Type*} [AddCommGroup G]
    (E : Finset G) (r : ℕ)
    (hinj : ∀ g ∈ E, ∀ j : Fin (r + 1), ∀ h ∈ E, ∀ k : Fin (r + 1),
      nextFrequency r g j = nextFrequency r h k → g = h ∧ j = k)
    (f : NextTensor G r → ℝ) :
    (∑ x ∈ nextFrequencies E r, f x) =
      ∑ j : Fin (r + 1), ∑ g ∈ E, f (nextFrequency r g j) := by
  classical
  unfold nextFrequencies
  rw [Finset.sum_image]
  · calc
      _ = ∑ g ∈ E, ∑ j : Fin (r + 1), f (nextFrequency r g j) :=
        Finset.sum_product E Finset.univ
          (fun gj => f (nextFrequency r gj.1 gj.2))
      _ = _ := Finset.sum_comm
  · intro x hx y hy hxy
    obtain ⟨hg, hj⟩ := Finset.mem_product.mp hx
    obtain ⟨hh, hk⟩ := Finset.mem_product.mp hy
    obtain ⟨hgh, hjk⟩ := hinj x.1 hg x.2 y.1 hh y.2 hxy
    exact Prod.ext hgh hjk

/-- Reindex a complex character polynomial over the same finite image. -/
private theorem nextFrequencies_complex_sum {G : Type*} [AddCommGroup G]
    (E : Finset G) (r : ℕ)
    (hinj : ∀ g ∈ E, ∀ j : Fin (r + 1), ∀ h ∈ E, ∀ k : Fin (r + 1),
      nextFrequency r g j = nextFrequency r h k → g = h ∧ j = k)
    (f : NextTensor G r → ℂ) :
    (∑ x ∈ nextFrequencies E r, f x) =
      ∑ j : Fin (r + 1), ∑ g ∈ E, f (nextFrequency r g j) := by
  classical
  unfold nextFrequencies
  rw [Finset.sum_image]
  · calc
      _ = ∑ g ∈ E, ∑ j : Fin (r + 1), f (nextFrequency r g j) :=
        Finset.sum_product E Finset.univ
          (fun gj => f (nextFrequency r gj.1 gj.2))
      _ = _ := Finset.sum_comm
  · intro x hx y hy hxy
    obtain ⟨hg, hj⟩ := Finset.mem_product.mp hx
    obtain ⟨hh, hk⟩ := Finset.mem_product.mp hy
    obtain ⟨hgh, hjk⟩ := hinj x.1 hg x.2 y.1 hh y.2 hxy
    exact Prod.ext hgh hjk

/-- Explicit finite rounding laws give the set-level one-step positive-real
parameter. Injectivity is the algebraic condition that no tensor column is
counted twice. -/
theorem next_parameter_of_finite_hom_rounding {ι : Type*}
    [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) (r : ℕ)
    (E : Finset (TensorLattice ι n)) (Q ρ : ℝ)
    (hbase : PositiveRealParameter E ρ)
    (hinj : ∀ g ∈ E, ∀ j : Fin (r + 1),
      ∀ h ∈ E, ∀ k : Fin (r + 1),
        nextFrequency r g j = nextFrequency r h k → g = h ∧ j = k)
    (hround : ∀ θ : AddChar (TensorLattice ι n) Circle,
      ∃ (s : Finset (TensorLattice ι n →+ ℤ))
        (w : (TensorLattice ι n →+ ℤ) → ℝ),
        (∀ FZ ∈ s, 0 ≤ w FZ) ∧
        (∑ FZ ∈ s, w FZ) = 1 ∧
        (∀ g ∈ E,
          (∑ FZ ∈ s, w FZ *
            (TensorRealCharacter.globalRealLiftHom n θ g -
              (2 * Real.pi) * (FZ g : ℝ))) = 0) ∧
        (∀ g ∈ E,
          (∑ FZ ∈ s, w FZ *
            (TensorRealCharacter.globalRealLiftHom n θ g -
              (2 * Real.pi) * (FZ g : ℝ)) ^ 2) ≤ Q)) :
    PositiveRealParameter (nextFrequencies E r)
      (ρ - 3 * Q / ((r + 1 : ℕ) : ℝ) ^ 2) := by
  intro a
  let c : TensorLattice ι n → Fin (r + 1) → ℂ :=
    fun g j => a (nextFrequency r g j)
  obtain ⟨η, hη⟩ := tensor_step_of_finite_hom_rounding n r E Q ρ hbase hround c
  refine ⟨η, ?_⟩
  have hnorm := nextFrequencies_sum E r hinj (fun x => ‖a x‖)
  have hpoly := nextFrequencies_complex_sum E r hinj
    (fun x => a x * (η x : ℂ))
  rw [hnorm, hpoly]
  exact hη

/-- At a tensor stage with nonzero old frequencies, the moment law is the
only new analytic hypothesis for the positive-real one-step estimate. -/
theorem next_parameter_of_rounding_nonzero {ι : Type*}
    [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) (r : ℕ) (hr : 2 ≤ r)
    (E : Finset (TensorLattice ι n)) (Q ρ : ℝ)
    (hbase : PositiveRealParameter E ρ)
    (hE : ∀ g ∈ E, g ≠ 0)
    (hround : ∀ θ : AddChar (TensorLattice ι n) Circle,
      ∃ (s : Finset (TensorLattice ι n →+ ℤ))
        (w : (TensorLattice ι n →+ ℤ) → ℝ),
        (∀ FZ ∈ s, 0 ≤ w FZ) ∧
        (∑ FZ ∈ s, w FZ) = 1 ∧
        (∀ g ∈ E,
          (∑ FZ ∈ s, w FZ *
            (TensorRealCharacter.globalRealLiftHom n θ g -
              (2 * Real.pi) * (FZ g : ℝ))) = 0) ∧
        (∀ g ∈ E,
          (∑ FZ ∈ s, w FZ *
            (TensorRealCharacter.globalRealLiftHom n θ g -
              (2 * Real.pi) * (FZ g : ℝ)) ^ 2) ≤ Q)) :
    PositiveRealParameter (nextFrequencies E r)
      (ρ - 3 * Q / ((r + 1 : ℕ) : ℝ) ^ 2) := by
  apply next_parameter_of_finite_hom_rounding n r E Q ρ hbase
  · intro g hg j h hh k heq
    exact nextFrequency_injective_nonzero r hr (hE g hg) (hE h hh) heq
  · exact hround

end Erdos.Research.Problem774.TensorStageAssembly

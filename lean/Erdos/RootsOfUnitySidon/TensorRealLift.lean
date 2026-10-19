import Erdos.RootsOfUnitySidon.TensorPhaseLattice
import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.Algebra.BigOperators.Pi
import Mathlib.Tactic

/-!
# Real lifts of tensor-simplex phase arrays

The phase array of any additive character of the free tensor lattice has an
exact real lift with zero sum along every coordinate line. This supplies the
surjective real-lift interface needed before randomized lattice rounding.
-/

namespace Erdos.Research.Problem774.TensorRealLift

open Erdos.Research.Problem774.TensorPhaseLattice

/-- The real vector space of arrays with zero sum on each coordinate line. -/
def LineZero {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) (X : TensorIndex ι n → ℝ) : Prop :=
  ∀ (j : TensorIndex ι n) (i : ι),
    ∑ k : Fin (n i + 1), X (Function.update j i k) = 0

private theorem circle_exp_sum {α : Type*} (s : Finset α) (f : α → ℝ) :
    Circle.exp (∑ a ∈ s, f a) = ∏ a ∈ s, Circle.exp (f a) := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | @insert a s ha ih => simp [ha, Circle.exp_add, ih]

private theorem character_sum {G α : Type*} [AddCommGroup G]
    (s : Finset α) (χ : AddChar G Circle) (f : α → G) :
    χ (∑ a ∈ s, f a) = ∏ a ∈ s, χ (f a) := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | @insert a s ha ih => simp [ha, χ.map_add_eq_mul, ih]

private theorem character_coordinate_product {ι : Type*}
    [Fintype ι] [DecidableEq ι] (n : ι → ℕ)
    [Fintype (TensorBasis ι n)]
    (χ : AddChar (TensorLattice ι n) Circle)
    (x : TensorLattice ι n) :
    χ x = ∏ a : TensorBasis ι n,
      χ (Pi.single a (1 : ℤ)) ^ x a := by
  have hdecomp : x = ∑ a : TensorBasis ι n,
      (x a) • Pi.single a (1 : ℤ) := pi_eq_sum_univ' x
  calc
    χ x = χ (∑ a : TensorBasis ι n,
        (x a) • Pi.single a (1 : ℤ)) := congrArg χ hdecomp
    _ = ∏ a : TensorBasis ι n,
        χ ((x a) • Pi.single a (1 : ℤ)) := by
      exact character_sum (Finset.univ : Finset (TensorBasis ι n)) χ
        (fun a => (x a) • Pi.single a (1 : ℤ))
    _ = _ := by
      apply Finset.prod_congr rfl
      intro a ha
      exact AddChar.map_zsmul_eq_zpow χ (x a) (Pi.single a (1 : ℤ))

/-- Take arguments on the free tensor basis, then extend linearly to all
tensor columns. -/
noncomputable def realLift {ι : Type*} [Fintype ι]
    (n : ι → ℕ) [Fintype (TensorBasis ι n)]
    (χ : AddChar (TensorLattice ι n) Circle) :
    TensorIndex ι n → ℝ := by
  classical
  exact fun j => ∑ a : TensorBasis ι n,
    (tensorColumn n j a : ℝ) * Complex.arg (χ (Pi.single a (1 : ℤ)) : ℂ)

/-- Exponentiating the lift recovers the character's phases. -/
theorem exp_realLift {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) [Fintype (TensorBasis ι n)]
    (χ : AddChar (TensorLattice ι n) Circle)
    (j : TensorIndex ι n) :
    Circle.exp (realLift n χ j) = χ (tensorColumn n j) := by
  classical
  rw [character_coordinate_product n χ (tensorColumn n j)]
  unfold realLift
  rw [circle_exp_sum]
  apply Fintype.prod_congr
  intro a
  have hsmul :
      ((tensorColumn n j a : ℤ) • Complex.arg (χ (Pi.single a (1 : ℤ)) : ℂ)) =
        (tensorColumn n j a : ℝ) * Complex.arg (χ (Pi.single a (1 : ℤ)) : ℂ) := by
    simp [zsmul_eq_mul]
  rw [← hsmul, Circle.exp_zsmul, Circle.exp_arg]

/-- The real lift obeys exact zero-sum equations along every coordinate line. -/
theorem realLift_lineZero {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) [Fintype (TensorBasis ι n)]
    (χ : AddChar (TensorLattice ι n) Circle) :
    LineZero n (realLift n χ) := by
  classical
  intro j i
  have hcoords (a : TensorBasis ι n) :
      ∑ k : Fin (n i + 1),
        (tensorColumn n (Function.update j i k) a : ℝ) = 0 := by
    have hz : ∑ k : Fin (n i + 1),
        tensorColumn n (Function.update j i k) a = 0 := by
      simpa only [Finset.sum_apply, Pi.zero_apply] using
        congrArg (fun x : TensorLattice ι n => x a)
          (sum_tensorColumn_line n j i)
    exact_mod_cast hz
  simp only [realLift]
  rw [Finset.sum_comm]
  simp_rw [← Finset.sum_mul]
  simp [hcoords]

/-- Every tensor-lattice character has a real zero-line-sum lift, with its
complex exponential equal to the character value on every tensor column. -/
theorem exists_real_lift {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) [Fintype (TensorBasis ι n)]
    (χ : AddChar (TensorLattice ι n) Circle) :
    ∃ X : TensorIndex ι n → ℝ,
      LineZero n X ∧
      ∀ j : TensorIndex ι n,
        Complex.exp (Complex.I * (X j : ℂ)) = (χ (tensorColumn n j) : ℂ) := by
  refine ⟨realLift n χ, realLift_lineZero n χ, ?_⟩
  intro j
  have h := congrArg (fun z : Circle => (z : ℂ)) (exp_realLift n χ j)
  simpa only [Circle.coe_exp, mul_comm] using h

end Erdos.Research.Problem774.TensorRealLift

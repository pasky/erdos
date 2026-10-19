import Erdos.RootsOfUnitySidon.TensorPhaseLattice
import Mathlib.Algebra.BigOperators.Pi
import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.Tactic

/-!
# Exact real linearization of tensor-simplex arrays

A real array whose sum vanishes on every coordinate line is exactly the
evaluation of an additive homomorphism on the corresponding tensor columns.
This real version retains exact equality, before exponentiating to Circle.
-/

namespace Erdos.Research.Problem774.TensorRealCharacter

open Erdos.Research.Problem774.TensorPhaseLattice

/-- Arbitrary real values on the free tensor basis define an additive hom. -/
noncomputable def basisRealHom {ι : Type*} [Fintype ι] (n : ι → ℕ)
    (t : TensorBasis ι n → ℝ) : TensorLattice ι n →+ ℝ := by
  classical
  exact {
    toFun x := ∑ a : TensorBasis ι n, (x a : ℝ) * t a
    map_zero' := by simp
    map_add' x y := by
      simp only [Pi.add_apply, Int.cast_add, add_mul, Finset.sum_add_distrib] }

/-- The additive hom constructed from basis values recovers each such value. -/
theorem basisRealHom_baseIndex {ι : Type*} [Fintype ι]
    (n : ι → ℕ) (t : TensorBasis ι n → ℝ)
    (a : TensorBasis ι n) :
    basisRealHom n t (tensorColumn n (baseIndex n a)) = t a := by
  classical
  rw [tensorColumn_baseIndex]
  simp [basisRealHom, Pi.single_apply]

/-- Every additive hom evaluated on tensor columns has zero sum on each
coordinate line. -/
theorem additiveHom_line_sum {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) (φ : TensorLattice ι n →+ ℝ)
    (j : TensorIndex ι n) (i : ι) :
    ∑ k : Fin (n i + 1), φ (tensorColumn n (Function.update j i k)) = 0 := by
  have h := congrArg φ (sum_tensorColumn_line n j i)
  simpa only [map_sum, map_zero] using h

/-- Values on all-basis tensor columns uniquely determine an additive array
with zero sum on each coordinate line. -/
theorem additive_array_unique {ι A : Type*} [Fintype ι] [DecidableEq ι]
    [AddCommGroup A] (n : ι → ℕ) (v w : TensorIndex ι n → A)
    (hv : ∀ j i, ∑ k : Fin (n i + 1),
      v (Function.update j i k) = 0)
    (hw : ∀ j i, ∑ k : Fin (n i + 1),
      w (Function.update j i k) = 0)
    (hbase : ∀ a : TensorBasis ι n, v (baseIndex n a) = w (baseIndex n a)) :
    v = w := by
  classical
  have aux : ∀ m : ℕ, ∀ j : TensorIndex ι n,
      (lastPositions n j).card = m → v j = w j := by
    intro m
    induction m using Nat.strong_induction_on with
    | h m ih =>
      intro j hm
      by_cases hzero : m = 0
      · have hnot : ∀ i : ι, j i ≠ Fin.last (n i) := by
          intro i hi
          have hmem : i ∈ lastPositions n j := by
            simp [lastPositions, hi]
          have hpos : 0 < (lastPositions n j).card :=
            Finset.card_pos.mpr ⟨i, hmem⟩
          omega
        let a : TensorBasis ι n := fun i => (j i).castPred (hnot i)
        have hj : baseIndex n a = j := by
          funext i
          exact Fin.castSucc_castPred (j i) (hnot i)
        rw [← hj]
        exact hbase a
      · have hsome : ∃ i : ι, j i = Fin.last (n i) := by
          by_contra h
          push Not at h
          have hempty : lastPositions n j = ∅ := by
            ext i
            simp [lastPositions, h i]
          have : m = 0 := by simpa [hempty] using hm.symm
          exact hzero this
        obtain ⟨i, hi⟩ := hsome
        have hmem : i ∈ lastPositions n j := by
          simp [lastPositions, hi]
        have hup : Function.update j i (Fin.last (n i)) = j := by
          funext h
          by_cases hhi : h = i
          · subst h
            simp [hi]
          · simp [hhi]
        have hpositions (k : Fin (n i)) :
            lastPositions n (Function.update j i k.castSucc) =
              (lastPositions n j).erase i := by
          ext h
          by_cases hhi : h = i
          · subst h
            simp [lastPositions]
          · simp [lastPositions, hhi]
        have hprefix :
            (∑ k : Fin (n i), v (Function.update j i k.castSucc)) =
            ∑ k : Fin (n i), w (Function.update j i k.castSucc) := by
          apply Finset.sum_congr rfl
          intro k _
          apply ih (lastPositions n (Function.update j i k.castSucc)).card
          · rw [hpositions]
            rw [← hm]
            exact Finset.card_erase_lt_of_mem hmem
          · rfl
        have hvj := hv j i
        have hwj := hw j i
        rw [Fin.sum_univ_castSucc, hup] at hvj hwj
        have heq :
            (∑ k : Fin (n i), v (Function.update j i k.castSucc)) + v j =
              (∑ k : Fin (n i), v (Function.update j i k.castSucc)) + w j := by
          rw [hvj, hprefix, hwj]
        exact add_left_cancel heq
  funext j
  exact aux _ j rfl

/-- Real-valued specialization of coordinate-line uniqueness. -/
theorem real_array_unique {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) (v w : TensorIndex ι n → ℝ)
    (hv : ∀ j i, ∑ k : Fin (n i + 1),
      v (Function.update j i k) = 0)
    (hw : ∀ j i, ∑ k : Fin (n i + 1),
      w (Function.update j i k) = 0)
    (hbase : ∀ a : TensorBasis ι n, v (baseIndex n a) = w (baseIndex n a)) :
    v = w :=
  additive_array_unique n v w hv hw hbase

/-- Any real line-zero array is exactly evaluation on tensor columns of an
additive homomorphism out of the free tensor lattice. -/
theorem realize_real_array {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) (X : TensorIndex ι n → ℝ)
    (hX : ∀ j i, ∑ k : Fin (n i + 1),
      X (Function.update j i k) = 0) :
    ∃ φ : TensorLattice ι n →+ ℝ,
      ∀ j, φ (tensorColumn n j) = X j := by
  let t : TensorBasis ι n → ℝ := fun a => X (baseIndex n a)
  let φ := basisRealHom n t
  have heq : (fun j => φ (tensorColumn n j)) = X := by
    apply real_array_unique n _ _
    · exact additiveHom_line_sum n φ
    · exact hX
    · intro a
      exact basisRealHom_baseIndex n t a
  exact ⟨φ, congrFun heq⟩

/-- Arbitrary integer values on the tensor basis define an integer additive
homomorphism. -/
noncomputable def basisIntegerHom {ι : Type*} [Fintype ι] (n : ι → ℕ)
    (t : TensorBasis ι n → ℤ) : TensorLattice ι n →+ ℤ := by
  classical
  exact {
    toFun x := ∑ a : TensorBasis ι n, x a * t a
    map_zero' := by simp
    map_add' x y := by
      simp only [Pi.add_apply, add_mul, Finset.sum_add_distrib] }

theorem basisIntegerHom_baseIndex {ι : Type*} [Fintype ι]
    (n : ι → ℕ) (t : TensorBasis ι n → ℤ)
    (a : TensorBasis ι n) :
    basisIntegerHom n t (tensorColumn n (baseIndex n a)) = t a := by
  classical
  rw [tensorColumn_baseIndex]
  simp [basisIntegerHom, Pi.single_apply]

theorem integerHom_line_sum {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) (φ : TensorLattice ι n →+ ℤ)
    (j : TensorIndex ι n) (i : ι) :
    ∑ k : Fin (n i + 1), φ (tensorColumn n (Function.update j i k)) = 0 := by
  have h := congrArg φ (sum_tensorColumn_line n j i)
  simpa only [map_sum, map_zero] using h

/-- Every integer array with zero sum on each coordinate line is exactly the
evaluation of an integer additive homomorphism on the tensor columns. -/
theorem realize_integer_array {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) (Z : TensorIndex ι n → ℤ)
    (hZ : ∀ j i, ∑ k : Fin (n i + 1),
      Z (Function.update j i k) = 0) :
    ∃ φ : TensorLattice ι n →+ ℤ,
      ∀ j, φ (tensorColumn n j) = Z j := by
  let t : TensorBasis ι n → ℤ := fun a => Z (baseIndex n a)
  let φ := basisIntegerHom n t
  have heq : (fun j => φ (tensorColumn n j)) = Z := by
    apply additive_array_unique n _ _
    · exact integerHom_line_sum n φ
    · exact hZ
    · intro a
      exact basisIntegerHom_baseIndex n t a
  exact ⟨φ, congrFun heq⟩

/-- Take arguments of a tensor-lattice character on the free integer basis,
then extend those arguments to a real additive homomorphism. -/
noncomputable def globalRealLiftHom {ι : Type*} [Fintype ι]
    (n : ι → ℕ) (χ : AddChar (TensorLattice ι n) Circle) :
    TensorLattice ι n →+ ℝ :=
  basisRealHom n (fun a => Complex.arg (χ (Pi.single a (1 : ℤ)) : ℂ))

/-- The global additive lift restricts to the familiar finite-sum real lift
on every tensor column. -/
theorem globalRealLiftHom_column {ι : Type*} [Fintype ι]
    (n : ι → ℕ) [Fintype (TensorBasis ι n)]
    (χ : AddChar (TensorLattice ι n) Circle)
    (j : TensorIndex ι n) :
    globalRealLiftHom n χ (tensorColumn n j) =
      ∑ a : TensorBasis ι n,
        (tensorColumn n j a : ℝ) *
          Complex.arg (χ (Pi.single a (1 : ℤ)) : ℂ) := by
  classical
  simp only [globalRealLiftHom, basisRealHom]
  apply Finset.sum_congr
  · ext a
    simp
  · intro a _
    rfl

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

/-- Exponentiating the global lift recovers the original character at every
lattice element, not only on the tensor columns. -/
theorem exp_globalRealLiftHom {ι : Type*} [Fintype ι]
    (n : ι → ℕ) (χ : AddChar (TensorLattice ι n) Circle)
    (g : TensorLattice ι n) :
    Circle.exp (globalRealLiftHom n χ g) = χ g := by
  classical
  have hdecomp : g = ∑ a : TensorBasis ι n,
      (g a) • Pi.single a (1 : ℤ) := pi_eq_sum_univ' g
  have hχ : χ g = ∏ a : TensorBasis ι n,
      χ (Pi.single a (1 : ℤ)) ^ g a := by
    calc
      χ g = χ (∑ a : TensorBasis ι n,
          (g a) • Pi.single a (1 : ℤ)) := congrArg χ hdecomp
      _ = ∏ a : TensorBasis ι n,
          χ ((g a) • Pi.single a (1 : ℤ)) := by
        exact character_sum (Finset.univ : Finset (TensorBasis ι n)) χ
          (fun a => (g a) • Pi.single a (1 : ℤ))
      _ = _ := by
        apply Finset.prod_congr rfl
        intro a _
        exact AddChar.map_zsmul_eq_zpow χ (g a) (Pi.single a (1 : ℤ))
  rw [hχ]
  change Circle.exp (∑ a : TensorBasis ι n,
    (g a : ℝ) * Complex.arg (χ (Pi.single a (1 : ℤ)) : ℂ)) = _
  rw [circle_exp_sum]
  apply Finset.prod_congr rfl
  intro a _
  have hsmul :
      ((g a : ℤ) • Complex.arg (χ (Pi.single a (1 : ℤ)) : ℂ)) =
        (g a : ℝ) * Complex.arg (χ (Pi.single a (1 : ℤ)) : ℂ) := by
    simp [zsmul_eq_mul]
  rw [← hsmul, Circle.exp_zsmul, Circle.exp_arg]

end Erdos.Research.Problem774.TensorRealCharacter

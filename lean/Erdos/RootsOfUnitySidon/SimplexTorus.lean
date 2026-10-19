import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Algebra.Group.AddChar
import Mathlib.Analysis.Complex.Circle
import Mathlib.Data.Fin.Tuple.Basic
import Mathlib.Tactic

/-!
# The simplex frequency configuration and its torus of phases

This module describes one prime-size simplex in the free additive
group `Fin n → ℤ`. Its `n + 1` columns are the coordinate vectors and their
negative sum. A character evaluated on these columns has product one, and
every Circle-valued phase tuple with that product relation comes from a
character.
-/

namespace Erdos.Research.Problem774.SimplexTorus

/-- The free additive group of rank `n`, written in coordinates. -/
abbrev Lattice (n : ℕ) := Fin n → ℤ

/-- A standard basis vector in the integer lattice. -/
def basis (n : ℕ) (i : Fin n) : Lattice n := Pi.single i 1

/-- The last simplex column is the negative sum of all basis vectors. -/
def lastColumn (n : ℕ) : Lattice n := -∑ i : Fin n, basis n i

/-- The `n + 1` columns of a rank-`n` simplex. -/
def column (n : ℕ) : Fin (n + 1) → Lattice n :=
  Fin.snoc (basis n) (lastColumn n)

@[simp] theorem column_castSucc (n : ℕ) (i : Fin n) :
    column n i.castSucc = basis n i := by simp [column]

@[simp] theorem column_last (n : ℕ) :
    column n (Fin.last n) = lastColumn n := by simp [column]

/-- The only universal relation needed to characterize simplex phases. -/
theorem sum_columns (n : ℕ) : ∑ j : Fin (n + 1), column n j = 0 := by
  rw [Fin.sum_univ_castSucc]
  simp [lastColumn]

private theorem character_sum {n : ℕ} {ι : Type*} (s : Finset ι)
    (χ : AddChar (Lattice n) Circle) (f : ι → Lattice n) :
    χ (∑ i ∈ s, f i) = ∏ i ∈ s, χ (f i) := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | @insert a s ha ih => simp [ha, χ.map_add_eq_mul, ih]

/-- A character's phases on the simplex columns have product one. -/
theorem character_phase_product (n : ℕ) (χ : AddChar (Lattice n) Circle) :
    ∏ j : Fin (n + 1), χ (column n j) = 1 := by
  rw [← character_sum Finset.univ χ (column n), sum_columns]
  simp

/-- Arbitrary phases assigned to the basis coordinates define a character. -/
noncomputable def phaseCharacter (n : ℕ) (t : Fin n → Circle) :
    AddChar (Lattice n) Circle where
  toFun x := ∏ i : Fin n, t i ^ x i
  map_zero_eq_one' := by simp
  map_add_eq_mul' x y := by
    simp only [Pi.add_apply, zpow_add]
    exact Finset.prod_mul_distrib

@[simp] theorem phaseCharacter_basis (n : ℕ) (t : Fin n → Circle) (i : Fin n) :
    phaseCharacter n t (basis n i) = t i := by
  classical
  simp [phaseCharacter, basis, Pi.single_apply]

theorem phaseCharacter_last (n : ℕ) (t : Fin n → Circle) :
    phaseCharacter n t (lastColumn n) = (∏ i : Fin n, t i)⁻¹ := by
  rw [lastColumn, AddChar.map_neg_eq_inv, character_sum]
  simp

/-- Every Circle-valued tuple satisfying the one simplex relation extends to
an additive character of the lattice. -/
theorem realize_phases (n : ℕ) (v : Fin (n + 1) → Circle)
    (hv : ∏ j : Fin (n + 1), v j = 1) :
    ∃ χ : AddChar (Lattice n) Circle,
      ∀ j : Fin (n + 1), χ (column n j) = v j := by
  let t : Fin n → Circle := fun i => v i.castSucc
  refine ⟨phaseCharacter n t, ?_⟩
  intro j
  induction j using Fin.lastCases with
  | last =>
      have hprod : (∏ i : Fin n, t i) * v (Fin.last n) = 1 := by
        simpa [t, Fin.prod_univ_castSucc] using hv
      have hlast : v (Fin.last n) = (∏ i : Fin n, t i)⁻¹ :=
        (mul_eq_one_iff_eq_inv').mp hprod
      simp [phaseCharacter_last, hlast]
  | cast i =>
      simp [t]

end Erdos.Research.Problem774.SimplexTorus

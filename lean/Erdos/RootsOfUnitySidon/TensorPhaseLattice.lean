import Erdos.RootsOfUnitySidon.SimplexTorus
import Mathlib.Algebra.BigOperators.Pi
import Mathlib.Algebra.Group.AddChar
import Mathlib.Analysis.Complex.Circle
import Mathlib.Tactic

/-!
# Phase characters on finite products of simplices

The frequency attached to a product of simplex columns is its pure tensor in
the free integer group on tuples of basis coordinates. A character of that
free group is specified by arbitrary phases on those basis tuples. Its phases
on the product columns obey the simplex product relation along every
coordinate line.
-/

namespace Erdos.Research.Problem774.TensorPhaseLattice

open Erdos.Research.Problem774.SimplexTorus

/-- Tuples of basis coordinates of a finite family of simplices. -/
abbrev TensorBasis (ι : Type*) (n : ι → ℕ) := ∀ i : ι, Fin (n i)

/-- Tuples of column coordinates of a finite family of simplices. -/
abbrev TensorIndex (ι : Type*) (n : ι → ℕ) := ∀ i : ι, Fin (n i + 1)

/-- The free integer group on tensor basis tuples. -/
abbrev TensorLattice (ι : Type*) (n : ι → ℕ) := TensorBasis ι n → ℤ

/-- The pure tensor of the selected simplex columns. -/
def tensorColumn {ι : Type*} [Fintype ι] (n : ι → ℕ)
    (j : TensorIndex ι n) : TensorLattice ι n :=
  fun a => ∏ i : ι, (column (n i) (j i)) (a i)

/-- Arbitrary phases on tensor basis coordinates define a character of the
free tensor lattice. -/
noncomputable def basisPhaseCharacter {ι : Type*} [Fintype ι] (n : ι → ℕ)
    (t : TensorBasis ι n → Circle) : AddChar (TensorLattice ι n) Circle := by
  classical
  exact {
    toFun x := ∏ a : TensorBasis ι n, t a ^ x a
    map_zero_eq_one' := by simp
    map_add_eq_mul' x y := by
      simp only [Pi.add_apply, zpow_add]
      exact Finset.prod_mul_distrib }

private theorem character_sum {G : Type*} [AddCommGroup G] {α : Type*}
    (s : Finset α) (χ : AddChar G Circle) (f : α → G) :
    χ (∑ a ∈ s, f a) = ∏ a ∈ s, χ (f a) := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | @insert a s ha ih => simp [ha, χ.map_add_eq_mul, ih]

/-- Varying one column coordinate while fixing all others sums to zero in
the tensor lattice. -/
theorem sum_tensorColumn_line {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) (j : TensorIndex ι n) (i : ι) :
    ∑ k : Fin (n i + 1), tensorColumn n (Function.update j i k) = 0 := by
  ext a
  simp only [Finset.sum_apply, Pi.zero_apply]
  have hfactor (k : Fin (n i + 1)) :
      tensorColumn n (Function.update j i k) a =
        (column (n i) k) (a i) *
          ∏ h ∈ (Finset.univ : Finset ι) \ {i},
            (column (n h) (j h)) (a h) := by
    unfold tensorColumn
    calc
      (∏ h : ι, (column (n h) (Function.update j i k h)) (a h)) =
          ∏ h : ι,
            Function.update (fun h : ι => (column (n h) (j h)) (a h)) i
              ((column (n i) k) (a i)) h := by
            apply Finset.prod_congr rfl
            intro h _
            by_cases hhi : h = i
            · subst h
              simp
            · simp [hhi]
      _ = _ := Finset.prod_update_of_mem (Finset.mem_univ i) _ _
  simp_rw [hfactor]
  rw [← Finset.sum_mul]
  have hsum : (∑ k : Fin (n i + 1), (column (n i) k) (a i)) = 0 := by
    simpa only [Finset.sum_apply, Pi.zero_apply] using
      congrArg (fun x : Lattice (n i) => x (a i)) (sum_columns (n i))
  simp [hsum]

/-- A character of the tensor lattice has product-one phases along every
coordinate line of the product simplex grid. -/
theorem character_phase_line_product {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) (χ : AddChar (TensorLattice ι n) Circle)
    (j : TensorIndex ι n) (i : ι) :
    ∏ k : Fin (n i + 1), χ (tensorColumn n (Function.update j i k)) = 1 := by
  rw [← character_sum Finset.univ χ
    (fun k => tensorColumn n (Function.update j i k)), sum_tensorColumn_line]
  simp

/-- A character built from arbitrary tensor-basis phases satisfies every
coordinate-line simplex relation. -/
theorem basisPhaseCharacter_line_product {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) (t : TensorBasis ι n → Circle)
    (j : TensorIndex ι n) (i : ι) :
    ∏ k : Fin (n i + 1),
      basisPhaseCharacter n t (tensorColumn n (Function.update j i k)) = 1 :=
  character_phase_line_product n (basisPhaseCharacter n t) j i

/-- The column indexed by an all-basis tuple. -/
def baseIndex {ι : Type*} (n : ι → ℕ)
    (a : TensorBasis ι n) : TensorIndex ι n :=
  fun i => (a i).castSucc

theorem tensorColumn_baseIndex {ι : Type*} [Fintype ι]
    (n : ι → ℕ) (a : TensorBasis ι n) :
    tensorColumn n (baseIndex n a) = Pi.single a (1 : ℤ) := by
  classical
  ext b
  by_cases hab : a = b
  · subst b
    simp [tensorColumn, baseIndex, basis]
  · have hdiff : ∃ i : ι, a i ≠ b i := by
      by_contra h
      push Not at h
      exact hab (funext h)
    obtain ⟨i, hi⟩ := hdiff
    have hz :
        (∏ h : ι, (column (n h) ((baseIndex n a) h)) (b h)) = 0 := by
      apply Finset.prod_eq_zero (Finset.mem_univ i)
      simp [baseIndex, basis, hi]
    simpa [tensorColumn, Pi.single_apply, hab] using hz

/-- Basis phases are recovered exactly on all-basis tensor columns. -/
theorem basisPhaseCharacter_baseIndex {ι : Type*} [Fintype ι]
    (n : ι → ℕ) (t : TensorBasis ι n → Circle)
    (a : TensorBasis ι n) :
    basisPhaseCharacter n t (tensorColumn n (baseIndex n a)) = t a := by
  classical
  rw [tensorColumn_baseIndex]
  simp [basisPhaseCharacter, Pi.single_apply]

/-- The coordinates at which a tensor index uses the last simplex column. -/
def lastPositions {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) (j : TensorIndex ι n) : Finset ι :=
  Finset.univ.filter (fun i => j i = Fin.last (n i))

private theorem lastPositions_update_castSucc {ι : Type*}
    [Fintype ι] [DecidableEq ι] (n : ι → ℕ)
    (j : TensorIndex ι n) (i : ι) (k : Fin (n i)) :
    lastPositions n (Function.update j i k.castSucc) =
      (lastPositions n j).erase i := by
  ext h
  by_cases hhi : h = i
  · subst h
    simp [lastPositions]
  · simp [lastPositions, hhi]

/-- Coordinate-line product relations and values on all-basis tuples
uniquely determine a phase array. -/
theorem phase_array_unique {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) (v w : TensorIndex ι n → Circle)
    (hv : ∀ j i, ∏ k : Fin (n i + 1),
      v (Function.update j i k) = 1)
    (hw : ∀ j i, ∏ k : Fin (n i + 1),
      w (Function.update j i k) = 1)
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
        have hprefix :
            (∏ k : Fin (n i), v (Function.update j i k.castSucc)) =
            ∏ k : Fin (n i), w (Function.update j i k.castSucc) := by
          apply Finset.prod_congr rfl
          intro k _
          apply ih (lastPositions n (Function.update j i k.castSucc)).card
          · rw [lastPositions_update_castSucc]
            rw [← hm]
            exact Finset.card_erase_lt_of_mem hmem
          · rfl
        have hvj := hv j i
        have hwj := hw j i
        rw [Fin.prod_univ_castSucc, hup] at hvj hwj
        have heq :
            (∏ k : Fin (n i), v (Function.update j i k.castSucc)) * v j =
              (∏ k : Fin (n i), v (Function.update j i k.castSucc)) * w j := by
          rw [hvj, hprefix, hwj]
        exact mul_left_cancel heq
  funext j
  exact aux _ j rfl

/-- Every product-simplex phase array whose coordinate-line products are one
is realized by an additive character of the free tensor lattice. -/
theorem realize_phase_array {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) (v : TensorIndex ι n → Circle)
    (hv : ∀ j i, ∏ k : Fin (n i + 1),
      v (Function.update j i k) = 1) :
    ∃ χ : AddChar (TensorLattice ι n) Circle,
      ∀ j, χ (tensorColumn n j) = v j := by
  let t : TensorBasis ι n → Circle := fun a => v (baseIndex n a)
  let χ := basisPhaseCharacter n t
  have heq : (fun j => χ (tensorColumn n j)) = v := by
    apply phase_array_unique n _ _
    · exact character_phase_line_product n χ
    · exact hv
    · intro a
      exact basisPhaseCharacter_baseIndex n t a
  exact ⟨χ, congrFun heq⟩

end Erdos.Research.Problem774.TensorPhaseLattice

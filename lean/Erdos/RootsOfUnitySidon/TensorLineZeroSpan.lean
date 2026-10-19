import Erdos.RootsOfUnitySidon.TensorPhaseLattice

/-!
# Reconstruction of product-simplex arrays from their basis coordinates

An array on a product of simplex column sets with zero sum on each coordinate
line is the linear combination of the pure tensor columns whose coefficients
are its values on the all-basis tuples.
-/

namespace Erdos.Research.Problem774.TensorLineZeroSpan

open Erdos.Research.Problem774.TensorPhaseLattice

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

/-- Coordinate-line zero sums and values on the all-basis tuples uniquely
determine a real array on a product-simplex grid. -/
theorem lineZero_unique {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) (v w : TensorIndex ι n → ℝ)
    (hv : ∀ j i, ∑ k : Fin (n i + 1), v (Function.update j i k) = 0)
    (hw : ∀ j i, ∑ k : Fin (n i + 1), w (Function.update j i k) = 0)
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
            (∑ k : Fin (n i), v (Function.update j i k.castSucc)) =
            ∑ k : Fin (n i), w (Function.update j i k.castSucc) := by
          apply Finset.sum_congr rfl
          intro k _
          apply ih (lastPositions n (Function.update j i k.castSucc)).card
          · rw [lastPositions_update_castSucc]
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

/-- A real array with zero sum on every coordinate line is recovered from its
all-basis values using the pure tensor simplex columns. -/
theorem reconstruct {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) (X : TensorIndex ι n → ℝ)
    (hX : ∀ j i, ∑ k : Fin (n i + 1), X (Function.update j i k) = 0)
    (u : TensorIndex ι n) :
    X u = ∑ a : TensorBasis ι n,
      X (baseIndex n a) * ((tensorColumn n u a : ℤ) : ℝ) := by
  classical
  let Y : TensorIndex ι n → ℝ := fun u =>
    ∑ a : TensorBasis ι n,
      X (baseIndex n a) * ((tensorColumn n u a : ℤ) : ℝ)
  have hYbase (a : TensorBasis ι n) : Y (baseIndex n a) = X (baseIndex n a) := by
    simp [Y, tensorColumn_baseIndex, Pi.single_apply]
  have hYline (j : TensorIndex ι n) (i : ι) :
      ∑ k : Fin (n i + 1), Y (Function.update j i k) = 0 := by
    simp only [Y]
    rw [Finset.sum_comm]
    apply Finset.sum_eq_zero
    intro a _
    rw [← Finset.mul_sum]
    have hcol := congrArg (fun z : TensorLattice ι n => z a)
      (sum_tensorColumn_line n j i)
    simp only [Finset.sum_apply, Pi.zero_apply] at hcol
    have hcast :
        (∑ k : Fin (n i + 1),
          ((tensorColumn n (Function.update j i k) a : ℤ) : ℝ)) = 0 := by
      exact_mod_cast hcol
    simp [hcast]
  have hEq : X = Y := lineZero_unique n X Y hX hYline
    (fun a => (hYbase a).symm)
  exact congrFun hEq u

end Erdos.Research.Problem774.TensorLineZeroSpan

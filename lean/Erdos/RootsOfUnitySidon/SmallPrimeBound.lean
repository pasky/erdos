import Erdos.RootsOfUnitySidon.FieldTensorSliceAverage
import Erdos.RootsOfUnitySidon.SmallPrimeFiberBound

/-!
# Small-prime simplex grid bound

The positive-real bound for one tail-field slice, the relative character
average, and the finite-slice selection lemma combine with a factor equal to
the number of simplex tensor columns.
-/

namespace Erdos.Research.Problem774

open SmallPrimeAnalytic TensorPhaseLattice

/-- Nonzero tail-field frequencies placed on every small-prime simplex tensor
column. -/
def nonzeroFieldTensorGrid {ι : Type*} [Fintype ι]
    (K : IntermediateField ℚ ℂ) (n : ι → ℕ) (t : Set K) :
    Set (FieldTensor K ι n) :=
  {x | ∃ (j : TensorIndex ι n) (z : K), z ∈ t ∧ z ≠ 0 ∧
    x = fieldTensorFrequency K n j z}

private theorem positiveRealBoundOn_mono {G : Type*} [AddCommGroup G]
    (s t : Set G) (C : ℝ) (hst : s ⊆ t)
    (ht : PositiveRealBoundOn t C) : PositiveRealBoundOn s C := by
  intro A hA c
  exact ht A (hA.trans hst) c

/-- A given slice-index map assembles the tail bound into a bound for the
entire nonzero grid. The representation hypothesis asks that the map return
the column of each grid point; uniqueness is proved separately below. -/
theorem positiveRealBoundOn_nonzeroFieldTensorGrid_of_index
    {ι : Type*} [Fintype ι]
    (K : IntermediateField ℚ ℂ) (n : ι → ℕ)
    [Fintype (TensorIndex ι n)] (hn : ∀ i, 2 ≤ n i)
    (t : Set K) (C : ℝ) (hC : 0 ≤ C)
    (ht : PositiveRealBoundOn t C)
    (f : FieldTensor K ι n → TensorIndex ι n)
    (hrepr : ∀ x ∈ nonzeroFieldTensorGrid K n t,
      ∃ z : K, z ∈ t ∧ z ≠ 0 ∧
        x = fieldTensorFrequency K n (f x) z) :
    PositiveRealBoundOn (nonzeroFieldTensorGrid K n t)
      ((Fintype.card (TensorIndex ι n) : ℝ) * C) := by
  have hnPos (i : ι) : 0 < n i :=
    lt_of_lt_of_le (by decide : 0 < 2) (hn i)
  have hfiber (j : TensorIndex ι n) :
      PositiveRealBoundOn
        {x | x ∈ nonzeroFieldTensorGrid K n t ∧ f x = j} C := by
    apply positiveRealBoundOn_mono
      {x | x ∈ nonzeroFieldTensorGrid K n t ∧ f x = j}
      ((fun z : K => fieldTensorFrequency K n j z) '' t) C
    · intro x hx
      obtain ⟨z, hzt, _, hxz⟩ := hrepr x hx.1
      refine ⟨z, hzt, ?_⟩
      simpa [hx.2] using hxz.symm
    · exact positiveRealBoundOn_fieldTensor_slice K n hnPos j t C ht
  have haverage :
      SliceAnnihilationOn (nonzeroFieldTensorGrid K n t) f := by
    apply sliceAnnihilationOn_fieldTensor_of_representation K n hn
    intro x hx
    obtain ⟨z, _, hz0, hxz⟩ := hrepr x hx
    exact ⟨z, hz0, hxz⟩
  exact positiveRealBoundOn_of_averaged_slices
    (nonzeroFieldTensorGrid K n t) f C hC hfiber haverage

/-- Choose one tensor-column representation for each point of the grid.
Outside the grid, the index is arbitrary. -/
noncomputable def nonzeroFieldTensorGridIndex
    {ι : Type*} [Fintype ι]
    (K : IntermediateField ℚ ℂ) (n : ι → ℕ) (t : Set K)
    (x : FieldTensor K ι n) : TensorIndex ι n := by
  classical
  exact if hx : x ∈ nonzeroFieldTensorGrid K n t then
    Classical.choose hx
  else
    fun i => 0

theorem nonzeroFieldTensorGridIndex_spec
    {ι : Type*} [Fintype ι]
    (K : IntermediateField ℚ ℂ) (n : ι → ℕ) (t : Set K)
    (x : FieldTensor K ι n) (hx : x ∈ nonzeroFieldTensorGrid K n t) :
    ∃ z : K, z ∈ t ∧ z ≠ 0 ∧
      x = fieldTensorFrequency K n (nonzeroFieldTensorGridIndex K n t x) z := by
  classical
  simpa [nonzeroFieldTensorGridIndex, hx] using (Classical.choose_spec hx)

/-- A positive-real bound on the tail-field frequencies gives a bound for
their whole nonzero small-prime tensor grid, with the number of columns as
the only loss in the constant. -/
theorem positiveRealBoundOn_nonzeroFieldTensorGrid
    {ι : Type*} [Fintype ι]
    (K : IntermediateField ℚ ℂ) (n : ι → ℕ)
    [Fintype (TensorIndex ι n)] (hn : ∀ i, 2 ≤ n i)
    (t : Set K) (C : ℝ) (hC : 0 ≤ C)
    (ht : PositiveRealBoundOn t C) :
    PositiveRealBoundOn (nonzeroFieldTensorGrid K n t)
      ((Fintype.card (TensorIndex ι n) : ℝ) * C) := by
  apply positiveRealBoundOn_nonzeroFieldTensorGrid_of_index
    K n hn t C hC ht (nonzeroFieldTensorGridIndex K n t)
  intro x hx
  exact nonzeroFieldTensorGridIndex_spec K n t x hx

end Erdos.Research.Problem774

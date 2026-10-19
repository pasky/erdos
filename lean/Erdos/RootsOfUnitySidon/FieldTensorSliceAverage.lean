import Erdos.RootsOfUnitySidon.AnalyticSliceSelection
import Erdos.RootsOfUnitySidon.SmallPrimeAnalytic

/-!
# Relative character averages for tail-field tensor slices

The checked relative character list for simplex-tensor columns is converted
to the finite family required by the generic analytic slice-selection lemma.
-/

namespace Erdos.Research.Problem774

open SmallPrimeAnalytic TensorPhaseLattice in
/-- The relative character list on a tail-field tensor supplies the finite
average required by `positiveRealBoundOn_of_averaged_slices`. The
representation hypothesis records the slice index of every frequency in `s`.
Its construction from an actual cyclotomic frequency set is separate. -/
theorem sliceAnnihilationOn_fieldTensor_of_representation
    {ι : Type*} [Fintype ι]
    (K : IntermediateField ℚ ℂ) (n : ι → ℕ)
    [Fintype (TensorIndex ι n)] (hn : ∀ i, 2 ≤ n i)
    (s : Set (FieldTensor K ι n))
    (f : FieldTensor K ι n → TensorIndex ι n)
    (hrepr : ∀ x ∈ s, ∃ z : K,
      z ≠ 0 ∧ x = fieldTensorFrequency K n (f x) z) :
    SliceAnnihilationOn s f := by
  classical
  intro A hA i
  let coeff (x : {x // x ∈ A}) : K :=
    (hrepr x.1 (hA x.2)).choose
  have hcoeff (x : {x // x ∈ A}) :
      coeff x ≠ 0 ∧
        x.1 = fieldTensorFrequency K n (f x.1) (coeff x) :=
    (hrepr x.1 (hA x.2)).choose_spec
  let outside : Finset {x // x ∈ A} :=
    A.attach.filter (fun x => f x.1 ≠ i)
  let F : Finset (TensorIndex ι n × K) :=
    outside.image (fun x => (f x.1, coeff x))
  have hF : ∀ p ∈ F, p.1 ≠ i ∧ p.2 ≠ 0 := by
    intro p hp
    obtain ⟨x, hx, rfl⟩ := Finset.mem_image.mp hp
    exact ⟨(Finset.mem_filter.mp hx).2, (hcoeff x).1⟩
  obtain ⟨L, hL, htrivial, hvanish⟩ :=
    SmallPrimeAnalytic.exists_relative_character_list_field K n hn i F hF
  have hbridge (x : FieldTensor K ι n) :
      (∑ j : Fin L.length, (L[j] x : ℂ)) =
        (L.map fun ψ => (ψ x : ℂ)).sum := by
    rw [← Fin.sum_univ_fun_getElem]
    simp
  refine ⟨L.length, List.length_pos_iff_ne_nil.mpr hL,
    (fun j => L[j]), ?_, ?_⟩
  · intro j x hx hxi
    let sx : {x // x ∈ A} := ⟨x, hx⟩
    have hreprx : x = fieldTensorFrequency K n i (coeff sx) := by
      simpa [sx, hxi] using (hcoeff sx).2
    rw [hreprx]
    exact htrivial L[j] (List.getElem_mem _) (coeff sx)
  · intro x hx hxi
    let sx : {x // x ∈ A} := ⟨x, hx⟩
    have hsx : sx ∈ outside := by
      simp [outside, sx, hxi]
    have hp : (f x, coeff sx) ∈ F :=
      Finset.mem_image.mpr ⟨sx, hsx, rfl⟩
    have hreprx : x = fieldTensorFrequency K n (f x) (coeff sx) :=
      (hcoeff sx).2
    have hzero := hvanish (f x, coeff sx) hp
    rw [← hreprx] at hzero
    rw [hbridge]
    exact hzero

end Erdos.Research.Problem774

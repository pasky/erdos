import Erdos.RootsOfUnitySidon.SidonExtraction
import Mathlib.Analysis.Normed.Module.FiniteDimension

/-!
# Finite norming families for a finite Sidon inequality

For a fixed finite frequency set, a Sidon inequality quantified over all
characters can be witnessed by a finite family of characters after doubling
the constant. This compactness step lets later arguments work with finite
sampling spaces.
-/

namespace Erdos.Research.SidonExtraction

open scoped BigOperators

noncomputable def finiteL1Norm {ι : Type*} [Fintype ι] (c : ι → ℂ) : ℝ :=
  ∑ i, ‖c i‖

def finiteEvalPoly {ι X : Type*} [Fintype ι] (v : X → ι → ℂ)
    (x : X) (c : ι → ℂ) : ℂ :=
  ∑ i, c i * v x i

private theorem continuous_finiteL1Norm {ι : Type*} [Fintype ι] :
    Continuous (finiteL1Norm : (ι → ℂ) → ℝ) := by
  unfold finiteL1Norm
  fun_prop

private theorem continuous_finiteEvalPoly {ι X : Type*} [Fintype ι]
    (v : X → ι → ℂ) (x : X) :
    Continuous (finiteEvalPoly v x : (ι → ℂ) → ℂ) := by
  unfold finiteEvalPoly
  fun_prop

/-- A uniform Sidon inequality on a finite coefficient space has a finite
norming family, at a cost of a factor of two in the constant. -/
theorem exists_finite_norming_family {ι X : Type*} [Fintype ι]
    (v : X → ι → ℂ) (K : ℝ) (hK : 0 < K)
    (h : ∀ c : ι → ℂ, ∃ x : X,
      finiteL1Norm c ≤ K * ‖finiteEvalPoly v x c‖) :
    ∃ F : Finset X, ∀ c : ι → ℂ, ∃ x ∈ F,
      finiteL1Norm c ≤ (2 * K) * ‖finiteEvalPoly v x c‖ := by
  classical
  let U : X → Set (ι → ℂ) := fun x =>
    {c | finiteL1Norm c < (2 * K) * ‖finiteEvalPoly v x c‖}
  have hUopen (x : X) : IsOpen (U x) := by
    exact isOpen_lt continuous_finiteL1Norm
      (continuous_const.mul ((continuous_finiteEvalPoly v x).norm))
  have hcover : Metric.sphere (0 : ι → ℂ) 1 ⊆ ⋃ x : X, U x := by
    intro c hc
    have hcne : c ≠ 0 := by
      intro hzero
      simp [hzero] at hc
    have hLpos : 0 < finiteL1Norm c := by
      rw [finiteL1Norm]
      by_contra hn
      have hsum : (∑ i, ‖c i‖) = 0 := le_antisymm (le_of_not_gt hn) (Finset.sum_nonneg fun _ _ => norm_nonneg _)
      have hz : ∀ i, c i = 0 := by
        intro i
        have hle : ‖c i‖ ≤ ∑ j, ‖c j‖ :=
          Finset.single_le_sum (fun j _ => norm_nonneg (c j)) (Finset.mem_univ i)
        have hni : ‖c i‖ = 0 := by rw [hsum] at hle; exact le_antisymm hle (norm_nonneg _)
        simpa using hni
      exact hcne (funext hz)
    obtain ⟨x, hx⟩ := h c
    have hpolypos : 0 < ‖finiteEvalPoly v x c‖ := by
      nlinarith
    have hstrict : finiteL1Norm c < (2 * K) * ‖finiteEvalPoly v x c‖ := by
      nlinarith
    exact Set.mem_iUnion.mpr ⟨x, hstrict⟩
  obtain ⟨F, hF⟩ :=
    (isCompact_sphere (0 : ι → ℂ) 1).elim_finite_subcover U
      hUopen hcover
  obtain ⟨x₀, -⟩ := h (0 : ι → ℂ)
  refine ⟨insert x₀ F, fun c => ?_⟩
  by_cases hc : c = 0
  · exact ⟨x₀, Finset.mem_insert_self _ _, by simp [hc, finiteL1Norm, finiteEvalPoly]⟩
  · let d : ι → ℂ := (‖c‖⁻¹ : ℝ) • c
    have hcnorm : 0 < ‖c‖ := norm_pos_iff.mpr hc
    have hd : d ∈ Metric.sphere (0 : ι → ℂ) 1 := by
      simp [d, mem_sphere_iff_norm, norm_smul,
        inv_mul_cancel₀ hcnorm.ne']
    obtain ⟨x, hx⟩ := Set.mem_iUnion.mp (hF hd)
    obtain ⟨hxF, hxU⟩ := Set.mem_iUnion.mp hx
    refine ⟨x, Finset.mem_insert_of_mem hxF, ?_⟩
    have hL : finiteL1Norm d = ‖c‖⁻¹ * finiteL1Norm c := by
      simp [finiteL1Norm, d, Finset.mul_sum]
    have hP : finiteEvalPoly v x d = (‖c‖⁻¹ : ℂ) * finiteEvalPoly v x c := by
      simp [finiteEvalPoly, d, Finset.mul_sum, mul_assoc]
    have hPinv : ‖finiteEvalPoly v x d‖ = ‖c‖⁻¹ * ‖finiteEvalPoly v x c‖ := by
      rw [hP, norm_mul, norm_inv, Complex.norm_real, Real.norm_eq_abs,
        abs_of_pos hcnorm]
    dsimp [U] at hxU
    rw [hL, hPinv] at hxU
    exact le_of_lt (by nlinarith [inv_pos.mpr hcnorm, inv_mul_cancel₀ hcnorm.ne'])

/-- The finite norming family for the repository's `FiniteSidonBound` on
complex frequencies. -/
theorem finiteSidonBound_finite_norming_family (A : Finset ℂ) (K : ℝ)
    (hK : 0 < K) (hA : FiniteSidonBound A K) :
    ∃ F : Finset (AddChar ℂ Circle), ∀ c : ℂ → ℂ,
      ∃ χ ∈ F, (∑ z ∈ A, ‖c z‖) ≤
        (2 * K) * ‖∑ z ∈ A, c z * (χ z : ℂ)‖ := by
  classical
  let v : AddChar ℂ Circle → A → ℂ := fun χ z => (χ z.1 : ℂ)
  have h : ∀ d : A → ℂ, ∃ χ : AddChar ℂ Circle,
      finiteL1Norm d ≤ K * ‖finiteEvalPoly v χ d‖ := by
    intro d
    let c : ℂ → ℂ := fun z => if hz : z ∈ A then d ⟨z, hz⟩ else 0
    obtain ⟨χ, hχ⟩ := hA c
    refine ⟨χ, ?_⟩
    have hL : (∑ z ∈ A, ‖c z‖) = finiteL1Norm d := by
      rw [← A.sum_attach]
      simp [c, finiteL1Norm]
    have hP : (∑ z ∈ A, c z * (χ z : ℂ)) = finiteEvalPoly v χ d := by
      rw [← A.sum_attach]
      simp [c, finiteEvalPoly, v]
    simpa [hL, hP] using hχ
  obtain ⟨F, hF⟩ := exists_finite_norming_family v K hK h
  refine ⟨F, fun c => ?_⟩
  let d : A → ℂ := fun z => c z.1
  obtain ⟨χ, hχF, hχ⟩ := hF d
  refine ⟨χ, hχF, ?_⟩
  have hL : finiteL1Norm d = ∑ z ∈ A, ‖c z‖ := by
    rw [← A.sum_attach]
    simp [finiteL1Norm, d]
  have hP : finiteEvalPoly v χ d = ∑ z ∈ A, c z * (χ z : ℂ) := by
    rw [← A.sum_attach]
    simp [finiteEvalPoly, v, d]
  simpa [hL, hP] using hχ

end Erdos.Research.SidonExtraction

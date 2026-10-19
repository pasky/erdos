import Erdos.RootsOfUnitySidon.SmallPrimeAnalytic
import Erdos.RootsOfUnitySidon.AnalyticSliceSelection

/-!
# Transfer of positive-real bounds to small-prime tensor slices

A positive-real Sidon bound on tail-field frequencies transfers through a fixed
small-prime tensor column. The character on the column image extends to the
whole additive tensor group because Circle is divisible.
-/

namespace Erdos.Research.Problem774.SmallPrimeAnalytic

open Erdos.Research.Problem774.TensorPhaseLattice

/-- Circle-valued characters extend along any injective homomorphism of
discrete additive commutative groups. -/
theorem extend_circle_character_along_addCommGroup {G H : Type*}
    [AddCommGroup G] [AddCommGroup H]
    (f : G →+ H) (hf : Function.Injective f) (χ : AddChar G Circle) :
    ∃ χ' : AddChar H Circle, ∀ z : G, χ' (f z) = χ z := by
  let e := AddCircle.homeomorphCircle (T := (1 : ℝ)) one_ne_zero
  have hto (z : Circle) : AddCircle.toCircle (e.symm z) = z := by
    calc
      AddCircle.toCircle (e.symm z) = e (e.symm z) :=
        (AddCircle.homeomorphCircle_apply one_ne_zero (e.symm z)).symm
      _ = z := e.apply_symm_apply z
  let g : G →+ AddCircle (1 : ℝ) := {
    toFun := fun z => e.symm (χ z)
    map_zero' := by
      apply AddCircle.injective_toCircle one_ne_zero
      change AddCircle.toCircle (e.symm (χ 0)) = AddCircle.toCircle 0
      rw [χ.map_zero_eq_one, hto]
      simp
    map_add' := by
      intro x y
      apply AddCircle.injective_toCircle one_ne_zero
      change AddCircle.toCircle (e.symm (χ (x + y))) =
        AddCircle.toCircle (e.symm (χ x) + e.symm (χ y))
      rw [AddCircle.toCircle_add, hto, hto, hto, χ.map_add_eq_mul]
  }
  obtain ⟨g', hg'⟩ :=
    (Module.Baer.of_divisible (AddCircle (1 : ℝ))).extension_property_addMonoidHom f hf g
  refine ⟨AddCircle.toCircle_addChar.compAddMonoidHom g', ?_⟩
  intro z
  have hz := congrArg (fun h : G →+ AddCircle (1 : ℝ) => h z) hg'
  change g' (f z) = g z at hz
  change AddCircle.toCircle (g' (f z)) = χ z
  rw [hz]
  change AddCircle.toCircle (e.symm (χ z)) = χ z
  exact hto (χ z)

/-- A positive-real bound transfers through an injective additive map. The
character on the image is extended to the entire target group. -/
theorem positiveRealBoundOn_image_injective {G H : Type*}
    [AddCommGroup G] [AddCommGroup H]
    (f : G →+ H) (hf : Function.Injective f)
    (s : Set G) (K : ℝ) (h : PositiveRealBoundOn s K) :
    PositiveRealBoundOn (f '' s) K := by
  classical
  intro A hA c
  let r : H → G := Function.invFun f
  let B : Finset G := A.image r
  have hr (x : H) (hx : x ∈ A) : f (r x) = x := by
    obtain ⟨z, _, hzx⟩ := hA (Finset.mem_coe.mpr hx)
    exact Function.invFun_eq ⟨z, hzx⟩
  have hB : (↑B : Set G) ⊆ s := by
    intro z hz
    obtain ⟨x, hx, rfl⟩ := Finset.mem_image.mp hz
    obtain ⟨w, hw, hxw⟩ := hA (Finset.mem_coe.mpr hx)
    have hrew : r x = w := hf (by rw [hr x hx, hxw])
    simpa [hrew] using hw
  have hmap : B.map ⟨f, hf⟩ = A := by
    ext x
    constructor
    · intro hx
      obtain ⟨z, hz, hzx⟩ := Finset.mem_map.mp hx
      obtain ⟨y, hy, rfl⟩ := Finset.mem_image.mp hz
      have hyx : y = x := (hr y hy).symm.trans hzx
      simpa [hyx] using hy
    · intro hx
      apply Finset.mem_map.mpr
      exact ⟨r x, Finset.mem_image.mpr ⟨x, hx, rfl⟩, hr x hx⟩
  obtain ⟨χ, hχ⟩ := h B hB (fun z => c (f z))
  obtain ⟨χ', hχ'⟩ := extend_circle_character_along_addCommGroup f hf χ
  refine ⟨χ', ?_⟩
  have hnorm : (∑ x ∈ A, ‖c x‖) = ∑ z ∈ B, ‖c (f z)‖ := by
    rw [← hmap]
    simp only [Finset.sum_map]
    rfl
  have hpoly : (∑ x ∈ A, c x * (χ' x : ℂ)) =
      ∑ z ∈ B, c (f z) * (χ z : ℂ) := by
    rw [← hmap]
    simp only [Finset.sum_map]
    change (∑ z ∈ B, c (f z) * (χ' (f z) : ℂ)) =
      ∑ z ∈ B, c (f z) * (χ z : ℂ)
    apply Finset.sum_congr rfl
    intro z _
    rw [hχ' z]
  rw [hnorm, hpoly]
  exact hχ

/-- Pull back a positive-real bound along an injective additive map. -/
theorem positiveRealBoundOn_pullback_injective {G H : Type*}
    [AddCommGroup G] [AddCommGroup H]
    (f : G →+ H) (hf : Function.Injective f)
    (s : Set G) (K : ℝ)
    (h : PositiveRealBoundOn (f '' s) K) :
    PositiveRealBoundOn s K := by
  classical
  intro A hA c
  let B : Finset H := A.map ⟨f, hf⟩
  have hB : (↑B : Set H) ⊆ f '' s := by
    intro z hz
    obtain ⟨x, hx, rfl⟩ := Finset.mem_map.mp hz
    exact ⟨x, hA (Finset.mem_coe.mpr hx), rfl⟩
  let r : H → G := Function.invFun f
  obtain ⟨χ, hχ⟩ := h B hB (fun z => c (r z))
  refine ⟨χ.compAddMonoidHom f, ?_⟩
  have hleft : (∑ x ∈ B, ‖c (r x)‖) = ∑ z ∈ A, ‖c z‖ := by
    simp only [B, Finset.sum_map]
    change (∑ z ∈ A, ‖c (r (f z))‖) = ∑ z ∈ A, ‖c z‖
    apply Finset.sum_congr rfl
    intro z _
    rw [show r (f z) = z from Function.leftInverse_invFun hf z]
  have hright : (∑ x ∈ B, c (r x) * (χ x : ℂ)) =
      ∑ z ∈ A, c z * ((χ.compAddMonoidHom f) z : ℂ) := by
    simp only [B, Finset.sum_map]
    change (∑ z ∈ A, c (r (f z)) * (χ (f z) : ℂ)) =
      ∑ z ∈ A, c z * ((χ.compAddMonoidHom f) z : ℂ)
    apply Finset.sum_congr rfl
    intro z _
    rw [show r (f z) = z from Function.leftInverse_invFun hf z]
    rfl
  rw [hleft, hright] at hχ
  exact hχ

/-- The additive map from one tail-field coordinate to its fixed small-prime
tensor column. -/
noncomputable def fieldTensorColumnHom {ι : Type*} [Fintype ι]
    (K : IntermediateField ℚ ℂ) (n : ι → ℕ) (j : TensorIndex ι n) :
    K →+ FieldTensor K ι n where
  toFun z := fieldTensorFrequency K n j z
  map_zero' := by
    ext a
    simp [fieldTensorFrequency]
  map_add' x y := by
    ext a
    simp [fieldTensorFrequency, mul_add]

theorem fieldTensorColumnHom_injective {ι : Type*} [Fintype ι]
    (K : IntermediateField ℚ ℂ) (n : ι → ℕ) (hn : ∀ i, 0 < n i)
    (j : TensorIndex ι n) :
    Function.Injective (fieldTensorColumnHom K n j) := by
  obtain ⟨a, ha⟩ := tensorColumn_nonzero n hn j
  have haK : (tensorColumn n j a : K) ≠ 0 := by exact_mod_cast ha
  intro z w hzw
  have hcoord := congrArg (fun x : FieldTensor K ι n => x a) hzw
  change (tensorColumn n j a : K) * z =
    (tensorColumn n j a : K) * w at hcoord
  exact (mul_right_inj' haK).mp hcoord

/-- One fixed simplex-tensor slice inherits its tail-field positive-real
constant unchanged. -/
theorem positiveRealBoundOn_fieldTensor_slice {ι : Type*} [Fintype ι]
    (K : IntermediateField ℚ ℂ) (n : ι → ℕ) (hn : ∀ i, 0 < n i)
    (j : TensorIndex ι n) (s : Set K) (C : ℝ)
    (h : PositiveRealBoundOn s C) :
    PositiveRealBoundOn
      ((fun z : K => fieldTensorFrequency K n j z) '' s) C := by
  exact positiveRealBoundOn_image_injective
    (fieldTensorColumnHom K n j) (fieldTensorColumnHom_injective K n hn j) s C h

end Erdos.Research.Problem774.SmallPrimeAnalytic

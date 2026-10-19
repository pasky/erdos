import Erdos.RootsOfUnitySidon.FiniteSidonNorming
import Mathlib.Analysis.Normed.Module.HahnBanach

/-!
# Finite-dimensional interpolation from a Sidon inequality

The analytic Sidon inequality controls the inverse of the polynomial
evaluation map. Hahn–Banach then supplies a bounded functional realizing
arbitrary coefficient data. This is the finite-dimensional interpolation
step used in Pisier's moment argument.
-/

namespace Erdos.Research.SidonExtraction

open scoped BigOperators

private def evaluationMap {ι κ : Type*} [Fintype ι] [Fintype κ]
    (v : κ → ι → ℂ) : (ι → ℂ) →ₗ[ℂ] (κ → ℂ) where
  toFun c k := finiteEvalPoly v k c
  map_add' c d := by
    ext k
    simp [finiteEvalPoly, add_mul, Finset.sum_add_distrib]
  map_smul' r c := by
    ext k
    simp [finiteEvalPoly, smul_eq_mul, Finset.mul_sum, mul_assoc]

private def coefficientFunctional {ι : Type*} [Fintype ι]
    (φ : ι → ℂ) : (ι → ℂ) →ₗ[ℂ] ℂ where
  toFun c := ∑ i, c i * φ i
  map_add' c d := by simp [add_mul, Finset.sum_add_distrib]
  map_smul' r c := by simp [smul_eq_mul, Finset.mul_sum, mul_assoc]

private theorem finiteL1Norm_eq_zero_iff {ι : Type*} [Fintype ι]
    (c : ι → ℂ) : finiteL1Norm c = 0 ↔ c = 0 := by
  classical
  constructor
  · intro h
    funext i
    have hi : ‖c i‖ ≤ finiteL1Norm c := by
      exact Finset.single_le_sum (fun j _ => norm_nonneg (c j)) (Finset.mem_univ i)
    rw [h] at hi
    exact norm_eq_zero.mp (le_antisymm hi (norm_nonneg _))
  · rintro rfl
    simp [finiteL1Norm]

private theorem coefficientFunctional_bound {ι : Type*} [Fintype ι]
    (φ c : ι → ℂ) :
    ‖coefficientFunctional φ c‖ ≤ ‖φ‖ * finiteL1Norm c := by
  classical
  calc
    ‖coefficientFunctional φ c‖ ≤ ∑ i, ‖c i * φ i‖ := by
      change ‖∑ i, c i * φ i‖ ≤ _
      exact norm_sum_le _ _
    _ = ∑ i, ‖φ i‖ * ‖c i‖ := by simp [mul_comm]
    _ ≤ ∑ i, ‖φ‖ * ‖c i‖ := by
      apply Finset.sum_le_sum
      intro i _
      exact mul_le_mul_of_nonneg_right (norm_le_pi_norm φ i) (norm_nonneg _)
    _ = ‖φ‖ * finiteL1Norm c := by simp [finiteL1Norm, Finset.mul_sum]

/-- A finite Sidon inequality gives a bounded complex-linear interpolation
functional. The domain of this functional is the finite vector of evaluation
points. -/
theorem exists_interpolating_functional {ι κ : Type*} [Fintype ι] [Fintype κ]
    (v : κ → ι → ℂ) (K : ℝ) (hK : 0 ≤ K)
    (hSidon : ∀ c : ι → ℂ,
      finiteL1Norm c ≤ K * ‖evaluationMap v c‖)
    (φ : ι → ℂ) :
    ∃ g : (κ → ℂ) →L[ℂ] ℂ,
      ‖g‖ ≤ K * ‖φ‖ ∧
      ∀ i : ι, g (fun k => v k i) = φ i := by
  classical
  let S := evaluationMap v
  have hSinj : Function.Injective S := by
    intro c d hcd
    have hz : S (c - d) = 0 := by rw [map_sub, hcd, sub_self]
    have hL := hSidon (c - d)
    rw [hz, norm_zero, mul_zero] at hL
    have hcd0 : c - d = 0 :=
      (finiteL1Norm_eq_zero_iff (c - d)).mp
        (le_antisymm hL (Finset.sum_nonneg fun _ _ => norm_nonneg _))
    exact sub_eq_zero.mp hcd0
  let e : (ι → ℂ) ≃ₗ[ℂ] LinearMap.range S :=
    LinearEquiv.ofInjective S hSinj
  let L : LinearMap.range S →ₗ[ℂ] ℂ :=
    (coefficientFunctional φ).comp e.symm.toLinearMap
  have hLbound : ∀ y : LinearMap.range S,
      ‖L y‖ ≤ (K * ‖φ‖) * ‖y‖ := by
    intro y
    obtain ⟨c, rfl⟩ := e.surjective y
    have heval : L (e c) = coefficientFunctional φ c := by simp [L]
    have henorm : ‖e c‖ = ‖S c‖ := rfl
    rw [heval, henorm]
    calc
      _ ≤ ‖φ‖ * finiteL1Norm c := coefficientFunctional_bound φ c
      _ ≤ ‖φ‖ * (K * ‖S c‖) :=
        mul_le_mul_of_nonneg_left (hSidon c) (norm_nonneg _)
      _ = (K * ‖φ‖) * ‖S c‖ := by ring
  let Lc : LinearMap.range S →L[ℂ] ℂ :=
    L.mkContinuous (K * ‖φ‖) hLbound
  obtain ⟨g, hg, hgnorm⟩ :=
    exists_extension_norm_eq (LinearMap.range S) Lc
  refine ⟨g, ?_, ?_⟩
  · calc
      ‖g‖ = ‖Lc‖ := hgnorm
      _ ≤ K * ‖φ‖ := L.mkContinuous_norm_le (mul_nonneg hK (norm_nonneg _)) hLbound
  · intro i
    let ei : ι → ℂ := fun j => if j = i then 1 else 0
    have hei : S ei = fun k => v k i := by
      funext k
      simp [S, evaluationMap, finiteEvalPoly, ei]
    have hgi : g (S ei) = coefficientFunctional φ ei := by
      have h := hg ⟨S ei, LinearMap.mem_range_self S ei⟩
      have he : e ei = (⟨S ei, LinearMap.mem_range_self S ei⟩ : LinearMap.range S) := rfl
      rw [← he] at h
      have hecoe : ((e ei : LinearMap.range S) : κ → ℂ) = S ei := rfl
      simpa [Lc, L, hecoe] using h
    simpa [hei, coefficientFunctional, ei] using hgi

private noncomputable def coordinate {κ : Type*} (k : κ) : κ → ℂ := by
  classical
  exact fun j => if j = k then 1 else 0

private theorem functional_eq_coordinate_sum {κ : Type*} [Fintype κ]
    (g : (κ → ℂ) →L[ℂ] ℂ) (x : κ → ℂ) :
    g x = ∑ k, g (coordinate k) * x k := by
  classical
  have hx : x = ∑ k, x k • coordinate k := by
    funext j
    simp [coordinate, Finset.sum_apply, smul_eq_mul]
  conv_lhs => rw [hx]
  simp [map_sum, map_smul, smul_eq_mul, mul_comm]

private noncomputable def alignPhase (z : ℂ) : ℂ :=
  if z = 0 then 0 else star z / (‖z‖ : ℂ)

private theorem norm_alignPhase_le_one (z : ℂ) : ‖alignPhase z‖ ≤ 1 := by
  by_cases hz : z = 0
  · simp [alignPhase, hz]
  · have hn : 0 < ‖z‖ := norm_pos_iff.mpr hz
    simp [alignPhase, hz, Complex.norm_real]

private theorem mul_alignPhase (z : ℂ) : z * alignPhase z = (‖z‖ : ℂ) := by
  by_cases hz : z = 0
  · simp [alignPhase, hz]
  · have hn : (‖z‖ : ℂ) ≠ 0 := by exact_mod_cast (norm_pos_iff.mpr hz).ne'
    simp only [alignPhase, hz, ↓reduceIte]
    rw [← mul_div_assoc]
    rw [Complex.star_def, Complex.mul_conj, Complex.normSq_eq_norm_sq]
    push_cast
    field_simp

/-- Finite-dimensional Sidon interpolation as an actual finitely supported
complex measure on the chosen character evaluations. -/
theorem exists_interpolating_weights {ι κ : Type*} [Fintype ι] [Fintype κ]
    (v : κ → ι → ℂ) (K : ℝ) (hK : 0 ≤ K)
    (hSidon : ∀ c : ι → ℂ,
      finiteL1Norm c ≤ K * ‖evaluationMap v c‖)
    (φ : ι → ℂ) :
    ∃ w : κ → ℂ,
      (∑ k, ‖w k‖) ≤ K * ‖φ‖ ∧
      ∀ i : ι, (∑ k, w k * v k i) = φ i := by
  classical
  obtain ⟨g, hgBound, hgInterp⟩ :=
    exists_interpolating_functional v K hK hSidon φ
  let w : κ → ℂ := fun k => g (coordinate k)
  let u : κ → ℂ := fun k => alignPhase (w k)
  have huNorm : ‖u‖ ≤ 1 :=
    (pi_norm_le_iff_of_nonneg zero_le_one).mpr
      (fun k => norm_alignPhase_le_one (w k))
  have hgu : g u = ((∑ k, ‖w k‖ : ℝ) : ℂ) := by
    rw [functional_eq_coordinate_sum]
    simp [u, w, mul_alignPhase]
  have hWBound : (∑ k, ‖w k‖) ≤ ‖g‖ := by
    have hsum : 0 ≤ ∑ k, ‖w k‖ := Finset.sum_nonneg fun _ _ => norm_nonneg _
    have hnorm : ‖g u‖ = ∑ k, ‖w k‖ := by
      rw [hgu, Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg hsum]
    calc
      _ = ‖g u‖ := hnorm.symm
      _ ≤ ‖g‖ * ‖u‖ := g.le_opNorm u
      _ ≤ ‖g‖ := by nlinarith [norm_nonneg g]
  refine ⟨w, hWBound.trans hgBound, ?_⟩
  intro i
  simpa [w] using (functional_eq_coordinate_sum g (fun k => v k i)).symm.trans (hgInterp i)

/-- Interpolation of arbitrary bounded data on a finite Sidon set by a finite
complex combination of algebraic additive characters. The total variation
bound depends only on the Sidon constant, not on the finite set. -/
theorem finiteSidonBound_interpolation (A : Finset ℂ) (K : ℝ)
    (hK : 0 < K) (hA : FiniteSidonBound A K) :
    ∃ F : Finset (AddChar ℂ Circle),
      ∀ φ : A → ℂ, ∃ w : F → ℂ,
        (∑ χ, ‖w χ‖) ≤ (2 * K) * ‖φ‖ ∧
        ∀ a : A, (∑ χ, w χ * ((χ.1 a.1 : Circle) : ℂ)) = φ a := by
  classical
  obtain ⟨F, hF⟩ := finiteSidonBound_finite_norming_family A K hK hA
  let v : F → A → ℂ := fun χ a => (χ.1 a.1 : ℂ)
  have hnorm : ∀ d : A → ℂ,
      finiteL1Norm d ≤ (2 * K) * ‖evaluationMap v d‖ := by
    intro d
    let c : ℂ → ℂ := fun z => if hz : z ∈ A then d ⟨z, hz⟩ else 0
    obtain ⟨χ, hχF, hχ⟩ := hF c
    have hL : (∑ z ∈ A, ‖c z‖) = finiteL1Norm d := by
      rw [← A.sum_attach]
      simp [c, finiteL1Norm]
    have hP : (∑ z ∈ A, c z * (χ z : ℂ)) =
        (evaluationMap v d) ⟨χ, hχF⟩ := by
      rw [← A.sum_attach]
      simp [c, evaluationMap, finiteEvalPoly, v]
    rw [hL, hP] at hχ
    exact hχ.trans (mul_le_mul_of_nonneg_left
      (norm_le_pi_norm (evaluationMap v d) ⟨χ, hχF⟩)
      (by positivity))
  refine ⟨F, fun φ => ?_⟩
  obtain ⟨w, hw, hwi⟩ :=
    exists_interpolating_weights v (2 * K) (by positivity) hnorm φ
  exact ⟨w, hw, fun a => hwi a⟩

/-- Interpolation of a sign vector rewrites an unrandomized polynomial as a
weighted sum of sign-randomized polynomials. This identity is the algebraic
step before the moment contraction. -/
theorem polynomial_interpolation_identity {ι κ : Type*}
    [Fintype ι] [Fintype κ]
    (c ε χ : ι → ℂ) (v : κ → ι → ℂ) (w : κ → ℂ)
    (hε : ∀ i, ε i * ε i = 1)
    (hw : ∀ i, (∑ k, w k * v k i) = ε i) :
    (∑ i, c i * χ i) =
      ∑ k, w k * (∑ i, c i * ε i * χ i * v k i) := by
  classical
  calc
    (∑ i, c i * χ i)
        = ∑ i, c i * ε i * χ i * ε i := by
            apply Finset.sum_congr rfl
            intro i _
            calc
              c i * χ i = (c i * χ i) * (ε i * ε i) := by rw [hε i]; ring
              _ = c i * ε i * χ i * ε i := by ring
    _ = ∑ i, c i * ε i * χ i * (∑ k, w k * v k i) := by
          apply Finset.sum_congr rfl
          intro i _
          rw [hw i]
    _ = ∑ k, w k * (∑ i, c i * ε i * χ i * v k i) := by
          simp_rw [Finset.mul_sum]
          rw [Finset.sum_comm]
          apply Finset.sum_congr rfl
          intro i _
          apply Finset.sum_congr rfl
          intro j _
          ring

end Erdos.Research.SidonExtraction

import Erdos.RootsOfUnitySidon.FiniteMomentExponential
import Erdos.RootsOfUnitySidon.FiniteRieszRelation
import Erdos.RootsOfUnitySidon.FiniteSidonRealMoment

/-!
# Moment bound for a finite Riesz product

This connects the real Riesz product to a Rudin even-moment hypothesis for
the real part of the sampled character polynomial.  The hypothesis is kept
explicit so the interpolation-to-moment argument can supply it separately.
-/

namespace Erdos.Research.FiniteRieszMomentBound

open scoped BigOperators
open Erdos.Research.FiniteMomentExponential
open Erdos.Research.FiniteOrthogonalCharacters
open Erdos.Research.FiniteRieszRelation
open Erdos.Research.PisierRelationCounting
open Erdos.Research.FiniteMomentOrthogonality

noncomputable def sampleRealSum (A : Finset ℂ) (T : Finset ℂ) : ℝ :=
  ∑ a ∈ A, (((sampleChar T a : Circle) : ℂ).re)

private theorem sample_re_ge_neg_one (T : Finset ℂ) (a : ℂ) :
    -1 ≤ (((sampleChar T a : Circle) : ℂ).re) := by
  have hn : ‖((sampleChar T a : Circle) : ℂ)‖ = 1 :=
    Circle.norm_coe (sampleChar T a)
  have hr := Complex.abs_re_le_norm ((sampleChar T a : Circle) : ℂ)
  rw [hn] at hr
  exact (abs_le.mp hr).1

private theorem riesz_factor_nonneg (T : Finset ℂ) (a : ℂ)
    (q : ℝ) (hq : 0 ≤ q) (hqhalf : q ≤ 1 / 2) :
    0 ≤ 1 + 2 * q * (((sampleChar T a : Circle) : ℂ).re) := by
  have hre := sample_re_ge_neg_one T a
  have hq2 : 2 * q ≤ 1 := by linarith
  have hmul := mul_le_mul_of_nonneg_left hre (by positivity : 0 ≤ 2 * q)
  nlinarith

/-- The sampled real character polynomial is centered whenever the sample
annihilates each of its nonzero frequencies. -/
theorem sampleRealSum_mean_zero (A S : Finset ℂ)
    (hAS : A ⊆ S) (hzero : 0 ∉ A) :
    ∑ T ∈ S.powerset,
      ((2 : ℝ) ^ S.card)⁻¹ * sampleRealSum A T = 0 := by
  classical
  have ha (a : ℂ) (haA : a ∈ A) :
      ∑ T ∈ S.powerset,
        (((sampleChar T a : Circle) : ℂ).re) = 0 := by
    have h := sum_sampleChar_eq_zero S (hAS haA) (by
      intro heq
      exact hzero (heq ▸ haA))
    have hr := congrArg Complex.re h
    simpa [Complex.re_sum] using hr
  calc
    ∑ T ∈ S.powerset,
        ((2 : ℝ) ^ S.card)⁻¹ * sampleRealSum A T =
      ((2 : ℝ) ^ S.card)⁻¹ *
        ∑ T ∈ S.powerset, sampleRealSum A T := by
          rw [Finset.mul_sum]
    _ = ((2 : ℝ) ^ S.card)⁻¹ *
        ∑ a ∈ A, ∑ T ∈ S.powerset,
          (((sampleChar T a : Circle) : ℂ).re) := by
            congr 1
            simp_rw [sampleRealSum]
            rw [Finset.sum_comm]
    _ = 0 := by
          rw [Finset.mul_sum]
          apply Finset.sum_eq_zero
          intro a haA
          rw [ha a haA]
          ring

/-- The real part of an `A`-term circle-character polynomial is bounded by
the number of terms. -/
theorem sampleRealSum_abs_le_card (A : Finset ℂ) (T : Finset ℂ) :
    |sampleRealSum A T| ≤ (A.card : ℝ) := by
  classical
  have hterm (a : ℂ) (ha : a ∈ A) :
      |(((sampleChar T a : Circle) : ℂ).re)| ≤ (1 : ℝ) := by
    simpa [Circle.norm_coe] using
      (Complex.abs_re_le_norm ((sampleChar T a : Circle) : ℂ))
  calc
    |sampleRealSum A T| =
        |∑ a ∈ A, (((sampleChar T a : Circle) : ℂ).re)| := rfl
    _ ≤ ∑ a ∈ A, |(((sampleChar T a : Circle) : ℂ).re)| :=
        Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ a ∈ A, (1 : ℝ) := Finset.sum_le_sum hterm
    _ = (A.card : ℝ) := by simp

private theorem sampleRealSum_sq_le_threshold (A : Finset ℂ)
    (T : Finset ℂ) (D : ℝ) (hD : 1 ≤ D) :
    (sampleRealSum A T) ^ 2 ≤
      D * ((A.card + 1 : ℕ) : ℝ) * (A.card : ℝ) := by
  let n : ℝ := A.card
  have hn : 0 ≤ n := by positivity
  have hnorm : (sampleRealSum A T) ^ 2 ≤ n ^ 2 := by
    have h := pow_le_pow_left₀ (abs_nonneg _) (sampleRealSum_abs_le_card A T) 2
    simpa [n, sq_abs] using h
  have hmn : n ≤ D * ((A.card + 1 : ℕ) : ℝ) := by
    calc
      n ≤ ((A.card + 1 : ℕ) : ℝ) := by
        dsimp [n]
        norm_cast
        omega
      _ = 1 * ((A.card + 1 : ℕ) : ℝ) := by ring
      _ ≤ D * ((A.card + 1 : ℕ) : ℝ) :=
        mul_le_mul_of_nonneg_right hD (by positivity)
  calc
    _ ≤ n ^ 2 := hnorm
    _ = n * n := pow_two n
    _ ≤ (D * ((A.card + 1 : ℕ) : ℝ)) * n :=
      mul_le_mul_of_nonneg_right hmn hn
    _ = _ := by rfl

/-- The normalized Riesz-product sample is bounded by the centered Rudin
even moments of its real character sum. -/
theorem riesz_average_le_exp_of_rudin_moments
    (A S : Finset ℂ) (q D : ℝ)
    (hq : 0 ≤ q) (hqhalf : q ≤ 1 / 2) (hD : 0 ≤ D)
    (hmean :
      ∑ T ∈ S.powerset,
        ((2 : ℝ) ^ S.card)⁻¹ * sampleRealSum A T = 0)
    (hmoment : ∀ m : ℕ, 0 < m →
      (∑ T ∈ S.powerset,
        ((2 : ℝ) ^ S.card)⁻¹ * (sampleRealSum A T) ^ (2 * m)) ≤
          (D * (m : ℝ)) ^ m * (A.card : ℝ) ^ m) :
    ((2 : ℝ) ^ S.card)⁻¹ *
      (∑ T ∈ S.powerset,
        ∏ a ∈ A,
          (1 + 2 * q * (((sampleChar T a : Circle) : ℂ).re))) ≤
      Real.exp (8 * D * (A.card : ℝ) * q ^ 2) := by
  classical
  let w : Finset ℂ → ℝ := fun _ => ((2 : ℝ) ^ S.card)⁻¹
  have hw : ∀ T ∈ S.powerset, 0 ≤ w T := by
    intro T hT
    dsimp [w]
    positivity
  have hwsum : ∑ T ∈ S.powerset, w T = 1 := by
    simp [w, Finset.card_powerset]
  have hprod (T : Finset ℂ) :
      (∏ a ∈ A, (1 + 2 * q * (((sampleChar T a : Circle) : ℂ).re))) ≤
        Real.exp (2 * q * sampleRealSum A T) := by
    calc
      _ ≤ ∏ a ∈ A,
          Real.exp (2 * q * (((sampleChar T a : Circle) : ℂ).re)) := by
            apply Finset.prod_le_prod₀
            · intro a ha
              exact riesz_factor_nonneg T a q hq hqhalf
            · intro a ha
              simpa [add_comm] using
                (Real.add_one_le_exp
                  (2 * q * (((sampleChar T a : Circle) : ℂ).re)))
      _ = Real.exp (∑ a ∈ A,
          2 * q * (((sampleChar T a : Circle) : ℂ).re)) :=
            (Real.exp_sum A _).symm
      _ = Real.exp (2 * q * sampleRealSum A T) := by
            rw [sampleRealSum, Finset.mul_sum]
  have hExp := weighted_exp_le_exp_of_rudin_moments
    S.powerset w (sampleRealSum A) D (A.card : ℝ) (2 * q)
      hD (by positivity) hw hwsum (by simpa [w] using hmean)
      (by intro m hm; simpa [w] using hmoment m hm)
  have hbound :
      (∑ T ∈ S.powerset,
        w T * ∏ a ∈ A,
          (1 + 2 * q * (((sampleChar T a : Circle) : ℂ).re))) ≤
        Real.exp (2 * D * (A.card : ℝ) * (2 * q) ^ 2) := by
    calc
      _ ≤ ∑ T ∈ S.powerset,
          w T * Real.exp (2 * q * sampleRealSum A T) := by
            apply Finset.sum_le_sum
            intro T hT
            exact mul_le_mul_of_nonneg_left (hprod T) (hw T hT)
      _ ≤ _ := hExp
  have hnorm :
      ((2 : ℝ) ^ S.card)⁻¹ *
        (∑ T ∈ S.powerset,
          ∏ a ∈ A,
            (1 + 2 * q * (((sampleChar T a : Circle) : ℂ).re))) =
        ∑ T ∈ S.powerset,
          w T * ∏ a ∈ A,
            (1 + 2 * q * (((sampleChar T a : Circle) : ℂ).re)) := by
    rw [Finset.mul_sum]
  rw [hnorm]
  convert hbound using 1 <;> ring

/-- Combined with exact finite Fourier orthogonality, the same estimate
bounds the weighted signed-relation enumerator. -/
theorem signed_relation_sum_le_exp_of_rudin_moments
    (A S : Finset ℂ) (q D : ℝ)
    (hS : relationFrequencies A \ {0} ⊆ S)
    (hq : 0 ≤ q) (hqhalf : q ≤ 1 / 2) (hD : 0 ≤ D)
    (hmean :
      ∑ T ∈ S.powerset,
        ((2 : ℝ) ^ S.card)⁻¹ * sampleRealSum A T = 0)
    (hmoment : ∀ m : ℕ, 0 < m →
      (∑ T ∈ S.powerset,
        ((2 : ℝ) ^ S.card)⁻¹ * (sampleRealSum A T) ^ (2 * m)) ≤
          (D * (m : ℝ)) ^ m * (A.card : ℝ) ^ m) :
    (∑ p ∈ signedRelations A, q ^ (p.1.card + p.2.card)) ≤
      Real.exp (8 * D * (A.card : ℝ) * q ^ 2) := by
  rw [← riesz_sample_average A S q hS]
  exact riesz_average_le_exp_of_rudin_moments A S q D hq hqhalf hD hmean hmoment

/-- The same relation estimate with centering discharged by finite
character orthogonality. -/
theorem signed_relation_sum_le_exp_of_rudin_moments_nonzero
    (A S : Finset ℂ) (q D : ℝ)
    (hS : relationFrequencies A \ {0} ⊆ S)
    (hAS : A ⊆ S) (hzero : 0 ∉ A)
    (hq : 0 ≤ q) (hqhalf : q ≤ 1 / 2) (hD : 0 ≤ D)
    (hmoment : ∀ m : ℕ, 0 < m →
      (∑ T ∈ S.powerset,
        ((2 : ℝ) ^ S.card)⁻¹ * (sampleRealSum A T) ^ (2 * m)) ≤
          (D * (m : ℝ)) ^ m * (A.card : ℝ) ^ m) :
    (∑ p ∈ signedRelations A, q ^ (p.1.card + p.2.card)) ≤
      Real.exp (8 * D * (A.card : ℝ) * q ^ 2) := by
  exact signed_relation_sum_le_exp_of_rudin_moments A S q D hS hq hqhalf hD
    (sampleRealSum_mean_zero A S hAS hzero) hmoment

/-- One finite sample contains every frequency needed by the Riesz identity
and by all moments up to `|A|`. -/
noncomputable def fixedSample (A : Finset ℂ) : Finset ℂ :=
  A ∪ (relationFrequencies A \ {0}) ∪
    (Finset.range (A.card + 1)).biUnion (momentFrequencies A)

theorem subset_fixedSample (A : Finset ℂ) : A ⊆ fixedSample A := by
  intro a ha
  exact Finset.mem_union.mpr (Or.inl (Finset.mem_union.mpr (Or.inl ha)))

theorem relationFrequencies_subset_fixedSample (A : Finset ℂ) :
    relationFrequencies A \ {0} ⊆ fixedSample A := by
  intro z hz
  exact Finset.mem_union.mpr (Or.inl (Finset.mem_union.mpr (Or.inr hz)))

theorem momentFrequencies_subset_fixedSample (A : Finset ℂ) (m : ℕ)
    (hm : m ≤ A.card) : momentFrequencies A m ⊆ fixedSample A := by
  intro z hz
  apply Finset.mem_union.mpr
  right
  exact Finset.mem_biUnion.mpr
    ⟨m, Finset.mem_range.mpr (by omega), hz⟩

/-- A finite Sidon inequality bounds the weighted count of all signed
relations by a Gaussian exponential.  The sample is finite and depends only
on `A`, even though the proof uses all even moments. -/
theorem finiteSidonBound_signed_relation_sum_le_exp
    (A : Finset ℂ) (K q : ℝ)
    (hK : 0 < K)
    (hA : Erdos.Research.SidonExtraction.FiniteSidonBound A K)
    (hzero : 0 ∉ A)
    (hq : 0 ≤ q) (hqhalf : q ≤ 1 / 2) :
    (∑ p ∈ signedRelations A, q ^ (p.1.card + p.2.card)) ≤
      Real.exp (8 * (1 + 48 * (2 * K) ^ 2) * (A.card : ℝ) * q ^ 2) := by
  classical
  let S := fixedSample A
  let D : ℝ := 1 + 48 * (2 * K) ^ 2
  have hD : 1 ≤ D := by
    dsimp [D]
    nlinarith [sq_nonneg (2 * K)]
  have hmoment (m : ℕ) (hm : 0 < m) (hmA : m ≤ A.card) :
      (∑ T ∈ S.powerset,
        ((2 : ℝ) ^ S.card)⁻¹ * (sampleRealSum A T) ^ (2 * m)) ≤
          (D * (m : ℝ)) ^ m * (A.card : ℝ) ^ m := by
    have hR := Erdos.Research.SidonExtraction.finiteSidonBound_sample_real_moment_superset
      A S K hK hA m hm (momentFrequencies_subset_fixedSample A m hmA)
    have hR' :
        (∑ T ∈ S.powerset,
          ((2 : ℝ) ^ S.card)⁻¹ * (sampleRealSum A T) ^ (2 * m)) ≤
          (2 * K) ^ (2 * m) * ((48 * m : ℕ) : ℝ) ^ m *
            (A.card : ℝ) ^ m := by
      simpa [S, Erdos.Research.SidonExtraction.sidonSampleRealSum,
        sampleRealSum, Finset.mul_sum] using hR
    have hbase : 48 * (2 * K) ^ 2 * (m : ℝ) ≤ D * (m : ℝ) := by
      dsimp [D]
      nlinarith [show (0 : ℝ) ≤ (m : ℝ) by positivity]
    have hpow :
        (48 * (2 * K) ^ 2 * (m : ℝ)) ^ m ≤ (D * (m : ℝ)) ^ m :=
      pow_le_pow_left₀ (by positivity) hbase m
    calc
      _ ≤ (2 * K) ^ (2 * m) * ((48 * m : ℕ) : ℝ) ^ m *
            (A.card : ℝ) ^ m := hR'
      _ = (48 * (2 * K) ^ 2 * (m : ℝ)) ^ m *
            (A.card : ℝ) ^ m := by
              have hb : (2 * K) ^ 2 * ((48 * m : ℕ) : ℝ) =
                  48 * (2 * K) ^ 2 * (m : ℝ) := by
                push_cast
                ring
              calc
                (2 * K) ^ (2 * m) * ((48 * m : ℕ) : ℝ) ^ m *
                    (A.card : ℝ) ^ m =
                  ((2 * K) ^ 2) ^ m * ((48 * m : ℕ) : ℝ) ^ m *
                    (A.card : ℝ) ^ m := by rw [pow_mul]
                _ = ((2 * K) ^ 2 * ((48 * m : ℕ) : ℝ)) ^ m *
                    (A.card : ℝ) ^ m := by simp only [mul_pow]
                _ = _ := by rw [hb]
      _ ≤ (D * (m : ℝ)) ^ m * (A.card : ℝ) ^ m :=
            mul_le_mul_of_nonneg_right hpow (by positivity)
  have hall := weighted_rudin_moments_of_truncated
    S.powerset (fun _ : Finset ℂ => ((2 : ℝ) ^ S.card)⁻¹)
      (sampleRealSum A) D (A.card : ℝ) A.card
      (le_trans (by norm_num : (0 : ℝ) ≤ 1) hD) (by positivity)
      (by intro T hT; positivity)
      (by simp [Finset.card_powerset])
      (by intro T hT; exact sampleRealSum_sq_le_threshold A T D hD)
      hmoment
  have hfinal := signed_relation_sum_le_exp_of_rudin_moments_nonzero
    A S q D (relationFrequencies_subset_fixedSample A)
      (subset_fixedSample A) hzero hq hqhalf
        (le_trans (by norm_num : (0 : ℝ) ≤ 1) hD) hall
  simpa [D, S] using hfinal

end Erdos.Research.FiniteRieszMomentBound

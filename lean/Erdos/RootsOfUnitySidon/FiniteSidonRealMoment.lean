import Erdos.RootsOfUnitySidon.FiniteSidonRudinMoment

/-!
# Real moments of a finite Sidon character sample

The real part of the sampled character sum has the same even-moment upper
bound as the complex sum. This is the form used by the Riesz-product estimate.
-/

namespace Erdos.Research.SidonExtraction

open scoped BigOperators
open Erdos.Research.FiniteOrthogonalCharacters
open Erdos.Research.FiniteMomentOrthogonality

noncomputable def sidonSampleRealSum (A : Finset ℂ) (T : Finset ℂ) : ℝ :=
  ∑ a ∈ A, (((sampleChar T a : Circle) : ℂ).re)

private theorem sidonSampleRealSum_eq_re (A : Finset ℂ) (T : Finset ℂ) :
    sidonSampleRealSum A T =
      (∑ a : A, ((sampleChar T a.1 : Circle) : ℂ)).re := by
  simp [sidonSampleRealSum, Complex.re_sum, ← A.sum_attach]

private theorem re_even_pow_le_norm (z : ℂ) (m : ℕ) :
    z.re ^ (2 * m) ≤ ‖z‖ ^ (2 * m) := by
  rw [← pow_abs_two_mul]
  exact pow_le_pow_left₀ (abs_nonneg _) (Complex.abs_re_le_norm z) _

/-- The normalized real even-moment bound on any sample containing the
nonzero frequencies of this exponent. -/
theorem finiteSidonBound_sample_real_moment_superset
    (A S : Finset ℂ) (K : ℝ) (hK : 0 < K)
    (hA : FiniteSidonBound A K)
    (m : ℕ) (hm : 0 < m)
    (hS : momentFrequencies A m ⊆ S) :
    ((2 : ℝ) ^ S.card)⁻¹ *
      (∑ T ∈ S.powerset, (sidonSampleRealSum A T) ^ (2 * m)) ≤
      (2 * K) ^ (2 * m) * ((48 * m : ℕ) : ℝ) ^ m *
        (A.card : ℝ) ^ m := by
  classical
  have hreal (T : Finset ℂ) :
      (sidonSampleRealSum A T) ^ (2 * m) ≤
        ‖∑ a : A, ((sampleChar T a.1 : Circle) : ℂ)‖ ^ (2 * m) := by
    rw [sidonSampleRealSum_eq_re]
    exact re_even_pow_le_norm _ _
  have hRudin := finiteSidonBound_rudin_moment_superset A S K hK hA m hm hS
    (fun _ => 1)
  have hcoeff : (∑ a : A, ‖(1 : ℂ)‖ ^ 2) = (A.card : ℝ) := by simp
  simp only [one_mul, hcoeff] at hRudin
  have hsum :
      (∑ T ∈ S.powerset, (sidonSampleRealSum A T) ^ (2 * m)) ≤
      (∑ T ∈ S.powerset,
        ‖∑ a : A, ((sampleChar T a.1 : Circle) : ℂ)‖ ^ (2 * m)) :=
    Finset.sum_le_sum fun T _ => hreal T
  have hnorm : 0 ≤ ((2 : ℝ) ^ S.card)⁻¹ := by positivity
  have h := (mul_le_mul_of_nonneg_left hsum hnorm).trans
    (mul_le_mul_of_nonneg_left hRudin hnorm)
  have htwo : (2 : ℝ) ^ S.card ≠ 0 := by positivity
  simpa only [← mul_assoc, inv_mul_cancel₀ htwo, one_mul] using h

/-- The usual Gaussian-parameter form of the same bound. -/
theorem finiteSidonBound_sample_real_moment_gaussian
    (A S : Finset ℂ) (K : ℝ) (hK : 0 < K)
    (hA : FiniteSidonBound A K)
    (m : ℕ) (hm : 0 < m)
    (hS : momentFrequencies A m ⊆ S) :
    ((2 : ℝ) ^ S.card)⁻¹ *
      (∑ T ∈ S.powerset, (sidonSampleRealSum A T) ^ (2 * m)) ≤
      ((192 * K ^ 2) * (m : ℝ)) ^ m * (A.card : ℝ) ^ m := by
  have h := finiteSidonBound_sample_real_moment_superset A S K hK hA m hm hS
  have hfactor :
      (2 * K) ^ (2 * m) * ((48 * m : ℕ) : ℝ) ^ m =
        ((192 * K ^ 2) * (m : ℝ)) ^ m := by
    push_cast
    rw [pow_mul, ← mul_pow]
    congr 1
    ring
  rwa [hfactor] at h

end Erdos.Research.SidonExtraction

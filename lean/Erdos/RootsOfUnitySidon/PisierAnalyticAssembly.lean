import Erdos.RootsOfUnitySidon.PisierExponentialParameters
import Erdos.RootsOfUnitySidon.PisierWeightedRelationBridge
import Erdos.RootsOfUnitySidon.PisierUniformBridge

/-!
# Assembly from an exponential signed-relation estimate

The analytic step has a convenient finite output: the generating function for
signed relations is bounded by a Gaussian exponential with one constant. The
remaining numeric and combinatorial steps are all explicit here.
-/

namespace Erdos.Research.PisierAnalyticAssembly

open Erdos.Research.PisierRelationCounting
open Erdos.Research.PisierExponentialParameters
open Erdos.Research.PisierWeightedRelationBridge
open Erdos.Research.PisierUniformBridge
open Erdos.Research.SidonExtraction

/-- A uniform Gaussian bound for signed relations implies the exact weighted
support estimate needed for proportional thinning. -/
theorem uniformWeightedRelationBound_of_signed_exp
    (s : Set ℂ) (C : ℝ) (hC : 0 ≤ C)
    (hrel : ∀ A : Finset ℂ, (↑A : Set ℂ) ⊆ s →
      ∀ q : ℝ, 0 ≤ q → q ≤ 1 / 2 →
        (∑ p ∈ signedRelations A,
          q ^ (p.1.card + p.2.card)) ≤
          Real.exp (C * (A.card : ℝ) * q ^ 2)) :
    ∃ M : ℕ, 64 ≤ M ∧ UniformWeightedRelationBound s M := by
  obtain ⟨M, hM, hpar⟩ := exists_parameters C hC
  refine ⟨M, hM, ?_⟩
  intro A hA hn
  let m : ℕ := 32 * (A.card / M)
  let q : ℝ := (2 * m : ℝ) / A.card
  obtain ⟨hqhalf, K, hExpK, hKcard⟩ := hpar A.card hn
  have hnpos : 0 < A.card := by omega
  have hq : 0 ≤ q := div_nonneg (by positivity) (by positivity)
  have hbound :
      (∑ p ∈ signedRelations A,
        q ^ (p.1.card + p.2.card)) ≤ K :=
    (hrel A hA q hq (by simpa [q, m] using hqhalf)).trans
      (by simpa [q, m] using hExpK)
  refine ⟨K, by simpa [m] using hKcard, ?_⟩
  exact weighted_relation_bound_of_signed_bound A m K hnpos
    (by simpa [q, m] using hbound)

/-- The Gaussian relation estimate gives one extraction denominator for the
whole set of nonzero frequencies. -/
theorem uniformExtraction_of_signed_exp
    (s : Set ℂ) (hzero : 0 ∉ s) (C : ℝ) (hC : 0 ≤ C)
    (hrel : ∀ A : Finset ℂ, (↑A : Set ℂ) ⊆ s →
      ∀ q : ℝ, 0 ≤ q → q ≤ 1 / 2 →
        (∑ p ∈ signedRelations A,
          q ^ (p.1.card + p.2.card)) ≤
          Real.exp (C * (A.card : ℝ) * q ^ 2)) :
    UniformExtraction s := by
  obtain ⟨M, hM, hweighted⟩ :=
    uniformWeightedRelationBound_of_signed_exp s C hC hrel
  exact uniformExtraction_of_uniformWeightedRelationBound hzero M hM hweighted

/-- This packages the finite analytic input in the form needed for Pisier's
forward implication. The Gaussian constant is fixed by the Sidon constant,
before any finite frequency set is chosen. -/
theorem pisierForward_of_finiteSignedRelationBound
    (hGaussian : ∀ K : ℝ, 0 < K →
      ∃ C : ℝ, 0 ≤ C ∧
        ∀ A : Finset ℂ, 0 ∉ A → FiniteSidonBound A K →
          ∀ q : ℝ, 0 ≤ q → q ≤ 1 / 2 →
            (∑ p ∈ signedRelations A,
              q ^ (p.1.card + p.2.card)) ≤
              Real.exp (C * (A.card : ℝ) * q ^ 2)) :
    PisierForward := by
  intro s hzero hSidon
  obtain ⟨K, hK, hFinite⟩ := hSidon
  obtain ⟨C, hC, hRel⟩ := hGaussian K hK
  apply uniformExtraction_of_signed_exp s hzero C hC
  intro A hA q hq hqhalf
  have hzeroA : 0 ∉ A := by
    intro hz
    exact hzero (hA hz)
  exact hRel A hzeroA (hFinite A hA) q hq hqhalf

end Erdos.Research.PisierAnalyticAssembly

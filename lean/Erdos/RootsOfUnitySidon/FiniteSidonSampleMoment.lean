import Erdos.RootsOfUnitySidon.FiniteSidonMomentComparison
import Erdos.RootsOfUnitySidon.FiniteMomentOrthogonality

/-!
# Sidon moment comparison on the exact finite orthogonal sample

This specializes finite-dimensional interpolation to the sample of characters
which annihilates every nonzero frequency in the even-moment expansion.
-/

namespace Erdos.Research.SidonExtraction

open scoped BigOperators
open Erdos.Research.FiniteOrthogonalCharacters
open Erdos.Research.FiniteMomentOrthogonality

/-- The finite sample, chosen from `A` and the even exponent alone, compares
the original polynomial moment with all of its Rademacher randomizations. -/
theorem finiteSidonBound_sampled_moment_comparison
    (A : Finset ℂ) (K : ℝ) (hK : 0 < K)
    (hA : FiniteSidonBound A K) (m : ℕ) (hm : 0 < m)
    (c : A → ℂ) :
    (Fintype.card (A → Bool) : ℝ) *
      (∑ T ∈ (momentFrequencies A m).powerset,
        ‖∑ a : A, c a * ((sampleChar T a.1 : Circle) : ℂ)‖ ^ (2 * m)) ≤
      (2 * K) ^ (2 * m) *
        ∑ ω : A → Bool,
          ∑ T ∈ (momentFrequencies A m).powerset,
            ‖∑ a : A,
                c a * rademacherSign ω a *
                  ((sampleChar T a.1 : Circle) : ℂ)‖ ^ (2 * m) := by
  classical
  let eval : Finset ℂ → A → ℂ :=
    fun T a => ((sampleChar T a.1 : Circle) : ℂ)
  have hInv (d : A → ℂ) (ψ : AddChar ℂ Circle) :
      (∑ T ∈ (momentFrequencies A m).powerset,
        ‖∑ a : A, d a * eval T a * (ψ a.1 : ℂ)‖ ^ (2 * m)) =
      (∑ T ∈ (momentFrequencies A m).powerset,
        ‖∑ a : A, d a * eval T a‖ ^ (2 * m)) := by
    let d' : ℂ → ℂ := fun z => if hz : z ∈ A then d ⟨z, hz⟩ else 0
    have h := sampled_even_moment_invariant A d' ψ m
    simp_rw [← A.sum_attach] at h
    simpa [d', eval] using h
  simpa [eval] using
    finiteSidonBound_rademacher_moment_comparison A K hK hA
      (momentFrequencies A m).powerset eval (2 * m)
      (by omega) hInv c

end Erdos.Research.SidonExtraction

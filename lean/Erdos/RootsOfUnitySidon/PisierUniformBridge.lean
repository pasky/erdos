import Erdos.RootsOfUnitySidon.PisierDensityParameters
import Erdos.RootsOfUnitySidon.PisierThinningAssembly
import Erdos.RootsOfUnitySidon.SidonExtraction

/-!
# Uniform extraction from a uniform weighted relation estimate

The theorem below states the exact finite estimate still needed from the
harmonic-analytic side. Its denominator is fixed before the finite set. Small
sets are covered by one nonzero frequency; larger sets use the checked
fixed-size thinning and relation-counting argument.
-/

namespace Erdos.Research.PisierUniformBridge

open Classical
open Erdos.Research.PisierDensityParameters
open Erdos.Research.PisierThinningAssembly
open Erdos.Research.PisierRelationCounting
open Erdos.Research.SidonExtraction

/-- The remaining analytic estimate, phrased in integer arithmetic. For
`m = 32·⌊|A|/M⌋`, a weighted count of signed relation supports must fit under
a number `K` that is exponentially smaller than `2^m`. -/
def UniformWeightedRelationBound (s : Set ℂ) (M : ℕ) : Prop :=
  ∀ A : Finset ℂ, (↑A : Set ℂ) ⊆ s → M ≤ A.card →
    let m := 32 * (A.card / M)
    ∃ K : ℕ,
      K * 3 ^ m ≤ 4 ^ m ∧
      (∑ R ∈ A.powerset.filter AddRelationSupport,
        (2 * m) ^ R.card * A.card ^ (A.card - R.card)) ≤
          K * A.card ^ A.card

/-- Once the uniform weighted relation estimate is supplied, the
proportional-dissociation conclusion follows with denominator `2M`. -/
theorem uniformExtraction_of_uniformWeightedRelationBound
    {s : Set ℂ} (hzero : 0 ∉ s)
    (M : ℕ) (hM : 64 ≤ M)
    (hweighted : UniformWeightedRelationBound s M) :
    UniformExtraction s := by
  classical
  refine ⟨2 * M, by omega, ?_⟩
  intro A hA
  by_cases hn : M ≤ A.card
  · let d := A.card / M
    let m := 32 * d
    have hp : 0 < d ∧ 0 < m ∧ 2 * m ≤ A.card ∧
        16 * d ≤ m ∧ A.card ≤ 2 * M * d := by
      simpa [d, m] using density_parameters M A.card hM hn
    obtain ⟨K, hK, hw⟩ := hweighted A hA hn
    obtain ⟨B, hBA, hdB, hB⟩ :=
      exists_dissociated_of_weighted_relation_bound
        A m d K hp.2.1 hp.2.2.1 hp.1 hp.2.2.2.1
        (by simpa [m, d] using hK)
        (by simpa [m, d] using hw)
    exact ⟨B, hBA, hB,
      hp.2.2.2.2.trans (Nat.mul_le_mul_left (2 * M) hdB)⟩
  · by_cases hAempty : A = ∅
    · subst A
      exact ⟨∅, by simp, by simp, by simp⟩
    · obtain ⟨a, ha⟩ := Finset.nonempty_iff_ne_empty.mpr hAempty
      have ha0 : a ≠ 0 := by
        intro heq
        exact hzero (hA (heq ▸ (Finset.mem_coe.mpr ha)))
      refine ⟨{a}, by simpa using (Finset.singleton_subset_iff.mpr ha), ?_, ?_⟩
      · simpa using (addDissociated_singleton (a := a)).mpr ha0
      · simp
        omega

end Erdos.Research.PisierUniformBridge

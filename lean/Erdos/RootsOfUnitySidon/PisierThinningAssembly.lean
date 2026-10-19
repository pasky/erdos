import Erdos.RootsOfUnitySidon.PisierFixedSizeThinning
import Erdos.RootsOfUnitySidon.PisierRelationCounting

/-!
# From a weighted relation moment to dissociated extraction

This combines the exact fixed-size first moment with the finite relation
counting theorem. The remaining analytic input is the stated bound on the
weighted relation moment, with constants uniform over finite root sets.
-/

namespace Erdos.Research.PisierThinningAssembly

open Erdos.Research.PisierFixedSizeThinning
open Erdos.Research.PisierRelationCounting
open Classical

/-- A quantitative moment criterion for extracting a large dissociated
subset. `m` is the thinning size, `d` the resulting dissociated size, and
`K` the allowed number of signed relation supports after thinning. -/
theorem exists_dissociated_of_weighted_relation_bound
    (A : Finset ℂ) (m d K : ℕ)
    (hmpos : 0 < m) (hmA : 2 * m ≤ A.card)
    (hdpos : 0 < d) (hdm : 16 * d ≤ m)
    (hK : K * 3 ^ m ≤ 4 ^ m)
    (hweighted :
      (∑ M ∈ A.powerset.filter AddRelationSupport,
        (2 * m) ^ M.card * A.card ^ (A.card - M.card)) ≤
        K * A.card ^ A.card) :
    ∃ B : Finset ℂ, B ⊆ A ∧ d ≤ B.card ∧
      AddDissociated (↑B : Set ℂ) := by
  obtain ⟨H, hHA, hHm, hHrel⟩ :=
    exists_fixed_size_of_weighted_relation_bound
      A AddRelationSupport m K hmpos hmA hweighted
  obtain ⟨B, hBH, hdB, hB⟩ :=
    exists_dissociated_of_exponential_relation_count H d
      hdpos (hHm ▸ hdm) (by
        rw [hHm]
        exact (Nat.mul_le_mul_right _ hHrel).trans hK)
  exact ⟨B, hBH.trans hHA, hdB, hB⟩

end Erdos.Research.PisierThinningAssembly

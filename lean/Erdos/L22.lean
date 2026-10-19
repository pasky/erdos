import Mathlib.Analysis.SpecialFunctions.Log.Base
import Mathlib.Combinatorics.Additive.Dissociation
import Erdos.Problem963.CardBound

/-!
# Finite real sets have near-logarithmically large dissociated subsets

Every nonempty finite set `A` of real numbers contains an additively
dissociated subset `B` (all subset sums of `B` distinct) with
`log₂ |A| - log₂ (log₂ |A| + 1) ≤ |B|`, the logarithm being the real
logarithm to base two. The statement uses Mathlib's `AddDissociated` and
`Real.logb` directly, so it restates no project definition; the proof
belongs to `Erdos.Problem963`, whose final theorem has this type by
unfolding.
-/

set_option autoImplicit false

namespace Erdos.L22

/-- Every nonempty finite real set `A` has a dissociated subset of size at
least `log₂ |A| - log₂ (log₂ |A| + 1)`. -/
def statement : Prop :=
  ∀ A : Finset ℝ, A.Nonempty →
    ∃ B : Finset ℝ, B ⊆ A ∧ AddDissociated (↑B : Set ℝ) ∧
      Real.logb 2 (A.card : ℝ) -
        Real.logb 2 (Real.logb 2 (A.card : ℝ) + 1) ≤ (B.card : ℝ)

theorem claim : statement :=
  Erdos.Problem963.exists_real_dissociated_large

end Erdos.L22

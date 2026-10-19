import Mathlib.GroupTheory.OrderOfElement
import Mathlib.Combinatorics.Additive.Dissociation
import Erdos.RootsOfUnitySidon.RootsOfUnitySidonComplete

/-!
# The complex roots of unity are proportionately dissociated

One integer denominator `k` works for every finite set `A` of complex roots
of unity: `A` contains an additively dissociated subset `B` (all subset sums
of `B` distinct in `ℂ`) with `|A| ≤ k · |B|`. The statement's semantic parts
are local to this claim; the proof belongs to `Erdos.Research.Problem774`,
whose definitions coincide with these by unfolding.
-/

set_option autoImplicit false

namespace Erdos.L21

/-- The complex roots of unity, as a subset of the additive group of `ℂ`. -/
def rootsOfUnity : Set ℂ := {z | IsOfFinOrder z}

/-- Some positive `k` bounds the extraction ratio of every finite set of
roots of unity. -/
def statement : Prop :=
  ∃ k : ℕ, 0 < k ∧
    ∀ A : Finset ℂ, (↑A : Set ℂ) ⊆ rootsOfUnity →
      ∃ B : Finset ℂ, B ⊆ A ∧ AddDissociated (↑B : Set ℂ) ∧ A.card ≤ k * B.card

/-- The local set of roots is the project's, by unfolding. -/
theorem rootsOfUnity_eq :
    rootsOfUnity = Erdos.Research.Problem774.rootsOfUnity := rfl

theorem claim : statement :=
  Erdos.Research.Problem774.rootsOfUnity_proportionalDissociation

end Erdos.L21

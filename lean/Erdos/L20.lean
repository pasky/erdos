import Mathlib.GroupTheory.OrderOfElement
import Mathlib.Analysis.SpecialFunctions.Complex.CircleAddChar
import Erdos.RootsOfUnitySidon.RootsOfUnitySidonComplete

/-!
# The complex roots of unity form an analytic Sidon set

In the discrete additive group of `ℂ`, some constant `K` bounds every
trigonometric polynomial supported on roots of unity: for every finite set
`A` of roots of unity and every coefficient function `c`, some additive
character `χ : ℂ → Circle` gives `∑_{z ∈ A} ‖c z‖ ≤ K · ‖∑_{z ∈ A} c z χ(z)‖`.
No continuity is imposed on `χ`. The statement's semantic parts are local to
this claim; the proof belongs to `Erdos.Research.Problem774`, whose
definitions coincide with these by unfolding.
-/

set_option autoImplicit false

namespace Erdos.L20

/-- The complex roots of unity, as a subset of the additive group of `ℂ`. -/
def rootsOfUnity : Set ℂ := {z | IsOfFinOrder z}

/-- One analytic Sidon constant serves every finite set of roots of unity. -/
def statement : Prop :=
  ∃ K : ℝ, 0 < K ∧
    ∀ A : Finset ℂ, (↑A : Set ℂ) ⊆ rootsOfUnity → ∀ c : ℂ → ℂ,
      ∃ χ : AddChar ℂ Circle,
        (∑ z ∈ A, ‖c z‖) ≤ K * ‖∑ z ∈ A, c z * (χ z : ℂ)‖

/-- The local set of roots is the project's, by unfolding. -/
theorem rootsOfUnity_eq :
    rootsOfUnity = Erdos.Research.Problem774.rootsOfUnity := rfl

theorem claim : statement :=
  Erdos.Research.Problem774.rootsOfUnity_analyticSidon

end Erdos.L20

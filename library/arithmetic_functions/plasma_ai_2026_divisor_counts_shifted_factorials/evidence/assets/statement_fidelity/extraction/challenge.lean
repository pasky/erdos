module

public import Mathlib.Analysis.SpecialFunctions.Log.Basic
public import Mathlib.NumberTheory.Divisors



@[expose] public section

open Filter

namespace Erdos420


noncomputable def F (f : ℕ → ℝ) (n : ℕ) : ℝ :=
  ((n + ⌊f n⌋₊).factorial.divisors.card : ℝ) / (n.factorial.divisors.card : ℝ)


theorem erdos_420.parts.iii (f : ℕ → ℝ) (hf : Monotone f)
    (hf_top : Tendsto f atTop atTop) (hf_log : ∀ᶠ n in atTop, f n ≤ Real.log n)
    (N : ℕ) : Set.Ioi 1 ⊆ closure (F f '' Set.Ici N) := by
  sorry


theorem erdos_420.parts.ii :
    Set.Ioi 1 ⊆ closure (Set.range (F fun n ↦ Real.log n)) := by
  sorry

end Erdos420

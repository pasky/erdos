module

public import Mathlib.Analysis.SpecialFunctions.Log.Basic
public import Mathlib.NumberTheory.Divisors



@[expose] public section

namespace Erdos420


noncomputable def F (f : ℕ → ℝ) (n : ℕ) : ℝ :=
  ((n + ⌊f n⌋₊).factorial.divisors.card : ℝ) / (n.factorial.divisors.card : ℝ)

end Erdos420

import Erdos420.FinalAssembly



open Filter

namespace Erdos420


theorem erdos_420.parts.iii (f : ℕ → ℝ) (hf : Monotone f)
    (hf_top : Tendsto f atTop atTop) (hf_log : ∀ᶠ n in atTop, f n ≤ Real.log n)
    (N : ℕ) : Set.Ioi 1 ⊆ closure (F f '' Set.Ici N) :=
  parts_iii_proved f hf hf_top hf_log N


theorem erdos_420.parts.ii :
    Set.Ioi 1 ⊆ closure (Set.range (F fun n ↦ Real.log n)) :=
  parts_ii_proved

end Erdos420

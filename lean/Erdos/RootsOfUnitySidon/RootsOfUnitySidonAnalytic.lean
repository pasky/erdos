import Erdos.RootsOfUnitySidon.TensorUniformPrimeTail
import Erdos.RootsOfUnitySidon.PrimeListStageBridge
import Erdos.RootsOfUnitySidon.SmallPrimeAssembly

/-!
# Analytic Sidonicity of all complex roots of unity

The uniform finite tensor estimate is transferred through the prime-list
grid, small-prime absorption, and the odd/even root-order reductions. The
characters are characters of the discrete additive group of `ℂ`.
-/

namespace Erdos.Research.Problem774

open Erdos.Research.Problem774.TensorStageMoment
open Erdos.Research.Problem774.TensorUniformPrimeTail
open Erdos.Research.Problem774.PrimeListStageBridge
open Erdos.Research.Problem774.SmallPrimeAssembly
open Erdos.Research.TensorExtension

/-- All complex roots of unity form an analytic Sidon set in the discrete
additive group of `ℂ`. -/
theorem rootsOfUnity_analyticSidon : AnalyticSidon := by
  obtain ⟨R, _, hstage⟩ := exists_cutoff_uniform_stage_half_parameter
  apply analyticSidon_of_uniform_tail_parameter R (1 / 2 : ℝ) (by norm_num)
  intro ps hsorted hps
  have htail : ∀ p ∈ ps, p.Prime ∧ R < p := by
    intro p hp
    exact ⟨(hps p hp).1, (hps p hp).2.2⟩
  have hfree := hstage ps hsorted htail
  have hprefix : ∀ i : Fin ps.length,
      listSides ps i.val = ps.get i := by
    intro i
    rw [listSides_getElem ps i.val i.isLt]
    rfl
  exact tailFreeGrid_parameter_of_stage ps (listSides ps) hprefix
    (1 / 2 : ℝ) hfree

end Erdos.Research.Problem774

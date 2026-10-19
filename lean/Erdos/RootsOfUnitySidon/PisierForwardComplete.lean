import Erdos.RootsOfUnitySidon.FiniteRieszMomentBound
import Erdos.RootsOfUnitySidon.PisierAnalyticAssembly

/-!
# Analytic Sidonicity implies proportional dissociation

The finite Rudin moment estimate controls a Riesz product; its zero-frequency
coefficient counts signed additive relations. The counting and thinning
modules then give one extraction denominator for every finite subset.
-/

namespace Erdos.Research.PisierForwardComplete

open Erdos.Research.SidonExtraction
open Erdos.Research.PisierAnalyticAssembly
open Erdos.Research.FiniteRieszMomentBound

/-- Pisier's forward implication for subsets of the discrete additive group
`ℂ` that avoid the zero frequency. -/
theorem pisierForward : PisierForward := by
  apply pisierForward_of_finiteSignedRelationBound
  intro K hK
  let C : ℝ := 8 * (1 + 48 * (2 * K) ^ 2)
  refine ⟨C, by dsimp [C]; positivity, ?_⟩
  intro A hzero hA q hq hqhalf
  exact finiteSidonBound_signed_relation_sum_le_exp A K q hK hA hzero hq hqhalf

end Erdos.Research.PisierForwardComplete

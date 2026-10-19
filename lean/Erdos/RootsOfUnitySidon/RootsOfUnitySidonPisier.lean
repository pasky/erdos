import Erdos.RootsOfUnitySidon.RootsOfUnitySidon
import Erdos.RootsOfUnitySidon.SidonExtraction

/-!
# Pisier interface for roots of unity

This module identifies the root-of-unity propositions with the general
finite-set Pisier interface. The implications below are conditional on the
Pisier principles; they do not prove those principles.
-/

namespace Erdos.Research.Problem774

theorem zero_not_mem_rootsOfUnity : (0 : ℂ) ∉ rootsOfUnity := by
  intro h
  change IsOfFinOrder (0 : ℂ) at h
  obtain ⟨n, hn, hpow⟩ := h.exists_pow_eq_one
  simp [zero_pow hn.ne'] at hpow

theorem analyticSidon_iff_pisier_interface :
    AnalyticSidon ↔
      Erdos.Research.SidonExtraction.AnalyticSidon rootsOfUnity := by
  rfl

theorem statement_iff_pisier_interface :
    statement ↔
      Erdos.Research.SidonExtraction.UniformExtraction rootsOfUnity := by
  rfl

/-- The forward Pisier principle turns an analytic proof of root Sidonicity
into proportional dissociation. -/
theorem statement_of_analyticSidon_of_pisier
    (hPisier : Erdos.Research.SidonExtraction.PisierForward)
    (hSidon : AnalyticSidon) : statement := by
  apply statement_iff_pisier_interface.mpr
  exact hPisier rootsOfUnity zero_not_mem_rootsOfUnity
    (analyticSidon_iff_pisier_interface.mp hSidon)

/-- The reverse Pisier principle turns proportional dissociation into the
ordinary analytic Sidon inequality on the discrete additive group. -/
theorem analyticSidon_of_statement_of_pisier
    (hPisier : Erdos.Research.SidonExtraction.PisierReverse)
    (hExtract : statement) : AnalyticSidon := by
  apply analyticSidon_iff_pisier_interface.mpr
  exact hPisier rootsOfUnity zero_not_mem_rootsOfUnity
    (statement_iff_pisier_interface.mp hExtract)

end Erdos.Research.Problem774

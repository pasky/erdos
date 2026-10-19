import Erdos.RootsOfUnitySidon.RootsOfUnitySidonAnalytic
import Erdos.RootsOfUnitySidon.RootsOfUnitySidonPisier
import Erdos.RootsOfUnitySidon.PisierForwardComplete

/-!
# Analytic Sidonicity and proportional dissociation of roots of unity

Both conclusions are unconditional. The analytic result is proved by the
prime tensor argument; the proportional dissociation result applies the
finite Pisier implication proved in this development.
-/

namespace Erdos.Research.Problem774

/-- One denominator works for dissociated subsets of every finite set of
complex roots of unity. -/
theorem rootsOfUnity_proportionalDissociation : statement :=
  statement_of_analyticSidon_of_pisier
    Erdos.Research.PisierForwardComplete.pisierForward
    rootsOfUnity_analyticSidon

end Erdos.Research.Problem774

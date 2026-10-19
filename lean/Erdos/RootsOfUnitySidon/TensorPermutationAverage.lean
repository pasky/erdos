import Erdos.RootsOfUnitySidon.PermutationAverage
import Erdos.RootsOfUnitySidon.TensorGramTrace
import Mathlib.Algebra.Group.Action.Pi
import Mathlib.Algebra.Group.Action.End

/-!
# Symmetry averaging on the tensor vertex grid

The product of the full symmetric groups on the simplex coordinates acts
transitively on the full tensor vertex grid. Averaging the tensor Gram trace
over that action therefore spreads its total squared length uniformly among
the vertices.
-/

namespace Erdos.Research.Problem774.TensorPermutationAverage

open Finset
open Erdos.Research.Problem774.PermutationAverage
open Erdos.Research.Problem774.TensorGramTrace

/-- Independent permutations of the vertices in each simplex factor. -/
abbrev TensorPermutation (ι : Type*) (n : ι → ℕ) :=
  ∀ i : ι, Equiv.Perm (Fin (n i + 1))

/-- Independent coordinate permutations act transitively on the tensor
vertex grid. -/
theorem tensorPermutation_transitive {ι : Type*} (n : ι → ℕ)
    (u v : TensorVertex ι n) :
    ∃ g : TensorPermutation ι n, g • u = v := by
  classical
  refine ⟨fun i => Equiv.swap (u i) (v i), ?_⟩
  funext i
  simp [Pi.smul_apply']

/-- The sum of squared orthogonal tensor values at one vertex. -/
noncomputable def vertexGram {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) (u : TensorVertex ι n) : ℝ :=
  ∑ j : TensorBasis ι n, (orthogonalTensor n j u) ^ 2

/-- The vertexwise Gram trace sums to the total squared tensor length. -/
theorem sum_vertexGram {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) :
    (∑ u : TensorVertex ι n, vertexGram n u) =
      ∏ i : ι, ((n i : ℝ) +
        ∑ j : Fin (n i), (1 : ℝ) / (j.val + 1 : ℝ)) := by
  classical
  unfold vertexGram
  rw [Finset.sum_comm]
  exact tensor_total_squared_length n

/-- At any fixed vertex, uniformly permuting the simplex coordinates makes
the average Gram trace equal to the total tensor squared length divided by
the number of tensor vertices. -/
theorem average_vertexGram {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) (u : TensorVertex ι n) :
    (∑ g : TensorPermutation ι n, vertexGram n (g⁻¹ • u)) /
        (Fintype.card (TensorPermutation ι n) : ℝ) =
      (∏ i : ι, ((n i : ℝ) +
        ∑ j : Fin (n i), (1 : ℝ) / (j.val + 1 : ℝ))) /
        (Fintype.card (TensorVertex ι n) : ℝ) := by
  classical
  haveI : Nonempty (TensorVertex ι n) :=
    ⟨fun i => ⟨0, Nat.succ_pos _⟩⟩
  rw [average_inv_smul_of_transitive
    (G := TensorPermutation ι n) (I := TensorVertex ι n)
    (fun a b => tensorPermutation_transitive n a b) (vertexGram n) u]
  rw [sum_vertexGram n]

end Erdos.Research.Problem774.TensorPermutationAverage

import Erdos.RootsOfUnitySidon.SmallPrimeFiberBound
import Mathlib.LinearAlgebra.Finsupp.LinearCombination

/-!
# Evaluation of tail-field tensor coordinates in the complex plane

Given a finite family of complex basis elements linearly independent over an
intermediate field `K`, finite `K`-coordinate tensors evaluate injectively in
the additive group of `ℂ`. The formula on a simplex tensor slice separates the
generic analytic argument from the remaining cyclotomic linear-independence
proof.
-/

namespace Erdos.Research.Problem774.FieldTensorEvaluation

open scoped Classical
open Erdos.Research.Problem774.SmallPrimeAnalytic
open Erdos.Research.Problem774.TensorPhaseLattice

/-- Evaluate a finite vector of tail-field coordinates against complex basis
elements. The map is additive even before linear independence is assumed. -/
noncomputable def evaluation {ι : Type*} [Fintype ι]
    (K : IntermediateField ℚ ℂ) (n : ι → ℕ)
    (b : TensorBasis ι n → ℂ) : FieldTensor K ι n →+ ℂ :=
  (Fintype.linearCombination K b).toAddMonoidHom

theorem evaluation_apply {ι : Type*} [Fintype ι]
    (K : IntermediateField ℚ ℂ) (n : ι → ℕ)
    (b : TensorBasis ι n → ℂ) (x : FieldTensor K ι n) :
    evaluation K n b x = ∑ a : TensorBasis ι n, (x a : ℂ) * b a := by
  simp [evaluation, Fintype.linearCombination_apply, Algebra.smul_def]

/-- Linear independence over the tail field makes evaluation injective. -/
theorem evaluation_injective {ι : Type*} [Fintype ι]
    (K : IntermediateField ℚ ℂ) (n : ι → ℕ)
    (b : TensorBasis ι n → ℂ) (hli : LinearIndependent K b) :
    Function.Injective (evaluation K n b) :=
  hli.fintypeLinearCombination_injective

/-- A fixed simplex column and a tail-field scalar evaluate as the scalar
times the corresponding complex tensor-column frequency. -/
theorem evaluation_fieldTensorFrequency {ι : Type*} [Fintype ι]
    (K : IntermediateField ℚ ℂ) (n : ι → ℕ)
    (b : TensorBasis ι n → ℂ)
    (j : TensorIndex ι n) (z : K) :
    evaluation K n b (fieldTensorFrequency K n j z) =
      (z : ℂ) * ∑ a : TensorBasis ι n,
        (tensorColumn n j a : ℂ) * b a := by
  rw [evaluation_apply]
  calc
    (∑ a : TensorBasis ι n,
        ((fieldTensorFrequency K n j z) a : ℂ) * b a) =
        ∑ a : TensorBasis ι n,
          (z : ℂ) * ((tensorColumn n j a : ℂ) * b a) := by
            apply Finset.sum_congr rfl
            intro a _
            simp only [fieldTensorFrequency]
            push_cast
            ring
    _ = (z : ℂ) * ∑ a : TensorBasis ι n,
          (tensorColumn n j a : ℂ) * b a := by
            rw [Finset.mul_sum]

/-- Any positive-real bound on a field-tensor grid transfers through an
injective cyclotomic evaluation without changing its constant. -/
theorem positiveRealBoundOn_evaluation_image {ι : Type*} [Fintype ι]
    (K : IntermediateField ℚ ℂ) (n : ι → ℕ)
    (b : TensorBasis ι n → ℂ) (hli : LinearIndependent K b)
    (s : Set (FieldTensor K ι n)) (C : ℝ)
    (h : Erdos.Research.Problem774.PositiveRealBoundOn s C) :
    Erdos.Research.Problem774.PositiveRealBoundOn
      ((evaluation K n b) '' s) C :=
  positiveRealBoundOn_image_injective
    (evaluation K n b) (evaluation_injective K n b hli) s C h

end Erdos.Research.Problem774.FieldTensorEvaluation

import Erdos.RootsOfUnitySidon.TensorRealLift
import Erdos.RootsOfUnitySidon.TensorPhaseLattice
import Erdos.RootsOfUnitySidon.TensorRealCharacter
import Erdos.RootsOfUnitySidon.TensorExtension
import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.Tactic

/-!
# Deterministic assembly of a tensor character after phase correction

The next tensor lattice is represented in coordinates as one copy of the old
free lattice for each basis vector of a new simplex. A tuple of old-lattice
characters whose product is one therefore determines a character of the next
tensor lattice. This module also records the algebra that makes a common
phase correction cancel the product-inverse character. The random variance
estimate is supplied separately by the rounding argument.
-/

namespace Erdos.Research.Problem774.TensorLiftAssembly

open Erdos.Research.Problem774.SimplexTorus
open Erdos.Research.Problem774.TensorPhaseLattice

/-- The coordinate realization of the tensor product of `G` with a simplex
side of size `n+1`. -/
abbrev NextTensor (G : Type*) (n : ℕ) := Fin n → G

/-- The pure tensor of `g` and the `j`th simplex column. -/
def nextFrequency {G : Type*} [AddCommGroup G]
    (n : ℕ) (g : G) (j : Fin (n + 1)) : NextTensor G n :=
  fun a => (column n j a) • g

/-- A tuple of characters defines a character on the next tensor lattice by
its values on the `q-1` basis copies of `G`. -/
noncomputable def basisTupleCharacter {G : Type*} [AddCommGroup G]
    (n : ℕ) (χ : Fin n → AddChar G Circle) :
    AddChar (NextTensor G n) Circle := by
  classical
  exact {
    toFun x := ∏ a : Fin n, χ a (x a)
    map_zero_eq_one' := by simp
    map_add_eq_mul' := by
      intro x y
      simp only [Pi.add_apply, AddChar.map_add_eq_mul]
      exact Finset.prod_mul_distrib }

private theorem character_sum {G α : Type*} [AddCommGroup G]
    (s : Finset α) (χ : AddChar G Circle) (f : α → G) :
    χ (∑ a ∈ s, f a) = ∏ a ∈ s, χ (f a) := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | @insert a s ha ih => simp [ha, χ.map_add_eq_mul, ih]

theorem nextFrequency_castSucc {G : Type*} [AddCommGroup G]
    (n : ℕ) (g : G) (i : Fin n) :
    nextFrequency n g i.castSucc = Pi.single i g := by
  classical
  funext a
  simp [nextFrequency, basis, Pi.single_apply]

theorem nextFrequency_sum {G : Type*} [AddCommGroup G]
    (n : ℕ) (g : G) :
    ∑ j : Fin (n + 1), nextFrequency n g j = 0 := by
  classical
  funext a
  simp only [Finset.sum_apply, Pi.zero_apply, nextFrequency]
  have hsum : ∑ j : Fin (n + 1), (column n j) a = 0 := by
    simpa only [Finset.sum_apply, Pi.zero_apply] using
      congrArg (fun f : Lattice n => f a) (sum_columns n)
  calc
    (∑ j : Fin (n + 1), (column n j a) • g) =
        (zmultiplesHom G g) (∑ j : Fin (n + 1), (column n j) a) := by
      rw [map_sum]
      rfl
    _ = 0 := by rw [hsum]; simp

theorem basisTupleCharacter_castSucc {G : Type*} [AddCommGroup G]
    (n : ℕ) (χ : Fin n → AddChar G Circle) (g : G) (i : Fin n) :
    basisTupleCharacter n χ (nextFrequency n g i.castSucc) = χ i g := by
  classical
  rw [nextFrequency_castSucc]
  change (∏ a : Fin n, χ a ((Pi.single i g : Fin n → G) a)) = χ i g
  calc
    _ = ∏ a : Fin n, if a = i then χ a g else 1 := by
      apply Fintype.prod_congr
      intro a
      by_cases hai : a = i <;> simp [hai]
    _ = χ i g := by simp

theorem basisTupleCharacter_last {G : Type*} [AddCommGroup G]
    (n : ℕ) (χ : Fin n → AddChar G Circle) (g : G) :
    basisTupleCharacter n χ (nextFrequency n g (Fin.last n)) =
      (∏ i : Fin n, χ i g)⁻¹ := by
  let η := basisTupleCharacter n χ
  have hsum := nextFrequency_sum n g
  rw [Fin.sum_univ_castSucc] at hsum
  have hη := congrArg η hsum
  rw [η.map_add_eq_mul, η.map_zero_eq_one, character_sum] at hη
  have hprefix :
      (∏ i : Fin n, η (nextFrequency n g i.castSucc)) =
        ∏ i : Fin n, χ i g := by
    apply Fintype.prod_congr
    intro i
    exact basisTupleCharacter_castSucc n χ g i
  rw [hprefix] at hη
  exact (mul_eq_one_iff_eq_inv').mp hη

/-- A tuple of old-lattice characters with product one at every lattice
element is realized by a single character of the next tensor lattice. -/
theorem realize_product_one_tuple {G : Type*} [AddCommGroup G]
    (n : ℕ) (φ : Fin (n + 1) → AddChar G Circle)
    (hφ : ∀ g : G, ∏ j : Fin (n + 1), φ j g = 1) :
    ∃ η : AddChar (NextTensor G n) Circle,
      ∀ (g : G) (j : Fin (n + 1)),
        η (nextFrequency n g j) = φ j g := by
  let η := basisTupleCharacter n (fun i => φ i.castSucc)
  refine ⟨η, ?_⟩
  intro g j
  induction j using Fin.lastCases with
  | cast i =>
      exact basisTupleCharacter_castSucc n (fun i => φ i.castSucc) g i
  | last =>
      have hp := hφ g
      rw [Fin.prod_univ_castSucc] at hp
      have hlast : φ (Fin.last n) g =
          (∏ i : Fin n, φ i.castSucc g)⁻¹ :=
        (mul_eq_one_iff_eq_inv').mp hp
      rw [basisTupleCharacter_last]
      exact hlast.symm

/-- An additive real phase produces a circle-valued additive character. -/
noncomputable def phaseAddChar {G : Type*} [AddCommGroup G]
    (q : ℕ) (F : G →+ ℝ) : AddChar G Circle where
  toFun g := Circle.exp (F g / (q : ℝ))
  map_zero_eq_one' := by simp
  map_add_eq_mul' x y := by
    simp only [map_add, add_div, Circle.exp_add]

/-- The product of `q=n+1` copies of the common correction phase is the
unscaled exponential phase. -/
private theorem phase_pow_succ {G : Type*} [AddCommGroup G]
    (n : ℕ) (F : G →+ ℝ) (g : G) :
    (phaseAddChar (n + 1) F g) ^ (n + 1) = Circle.exp (F g) := by
  change Circle.exp (F g / ((n + 1 : ℕ) : ℝ)) ^ (n + 1) = Circle.exp (F g)
  rw [← Circle.exp_natCast_mul]
  congr 1
  have hq : (((n + 1 : ℕ) : ℝ)) ≠ 0 := by positivity
  field_simp

/-- Dividing a real lift of the inverse product character among the `q`
columns makes their corrected character tuple have product one. -/
theorem corrected_tuple_product_one {G : Type*} [AddCommGroup G]
    (n : ℕ) (χ : Fin (n + 1) → AddChar G Circle)
    (F : G →+ ℝ)
    (hF : ∀ g : G, Circle.exp (F g) =
      ((∏ j : Fin (n + 1), χ j)⁻¹) g) :
    ∀ g : G,
      ∏ j : Fin (n + 1), (χ j * phaseAddChar (n + 1) F) g = 1 := by
  intro g
  simp only [AddChar.mul_apply, Finset.prod_mul_distrib]
  have hprod : (∏ j : Fin (n + 1), χ j g) =
      (∏ j : Fin (n + 1), χ j) g :=
    (AddChar.prod_apply Finset.univ χ g).symm
  rw [hprod]
  have hphase : (∏ _j : Fin (n + 1), phaseAddChar (n + 1) F g) =
      (phaseAddChar (n + 1) F g) ^ (n + 1) := by simp
  rw [hphase, phase_pow_succ, hF, AddChar.inv_apply']
  exact mul_inv_cancel _

/-- Periodic integer shifts preserve the exponential of a real phase. -/
private theorem exp_sub_integer_period {G : Type*} [AddCommGroup G]
    (FX : G →+ ℝ) (FZ : G →+ ℤ) (g : G) :
    Circle.exp (FX g - (2 * Real.pi) * (FZ g : ℝ)) =
      Circle.exp (FX g) := by
  rw [Circle.exp_sub, Circle.exp_two_pi_mul_int]
  simp

/-- The exact residual after subtracting an integer lattice point is still
an additive real phase. -/
noncomputable def residualHom {G : Type*} [AddCommGroup G]
    (FX : G →+ ℝ) (FZ : G →+ ℤ) : G →+ ℝ where
  toFun g := FX g - (2 * Real.pi) * (FZ g : ℝ)
  map_zero' := by simp
  map_add' x y := by
    simp only [map_add, Int.cast_add]
    ring

/-- A real lift of the inverse product character, shifted by any integer
additive phase, yields a realizable corrected tensor character. -/
theorem realize_corrected_tuple {G : Type*} [AddCommGroup G]
    (n : ℕ) (χ : Fin (n + 1) → AddChar G Circle)
    (FX : G →+ ℝ) (FZ : G →+ ℤ)
    (hFX : ∀ g : G, Circle.exp (FX g) =
      ((∏ j : Fin (n + 1), χ j)⁻¹) g) :
    ∃ η : AddChar (NextTensor G n) Circle,
      ∀ (g : G) (j : Fin (n + 1)),
        (η (nextFrequency n g j) : ℂ) =
          (χ j g : ℂ) *
            Complex.exp (Complex.I *
              (((FX g - (2 * Real.pi) * (FZ g : ℝ)) / ((n + 1 : ℕ) : ℝ) : ℝ) : ℂ)) := by
  let F := residualHom FX FZ
  have hF (g : G) : Circle.exp (F g) =
      ((∏ j : Fin (n + 1), χ j)⁻¹) g := by
    change Circle.exp (FX g - (2 * Real.pi) * (FZ g : ℝ)) = _
    rw [exp_sub_integer_period, hFX]
  let φ : Fin (n + 1) → AddChar G Circle :=
    fun j => χ j * phaseAddChar (n + 1) F
  obtain ⟨η, hη⟩ := realize_product_one_tuple n φ
    (corrected_tuple_product_one n χ F hF)
  refine ⟨η, ?_⟩
  intro g j
  rw [hη g j]
  have hphase : (phaseAddChar (n + 1) F g : ℂ) =
      Complex.exp (Complex.I * (((F g / ((n + 1 : ℕ) : ℝ) : ℝ) : ℂ))) := by
    change (Circle.exp (F g / ((n + 1 : ℕ) : ℝ)) : ℂ) = _
    rw [Circle.coe_exp]
    congr 1
    ring
  change ((χ j * phaseAddChar (n + 1) F) g : ℂ) = _
  rw [AddChar.mul_apply, Circle.coe_mul, hphase]
  dsimp [F, residualHom]

/-- Tensor-lattice form of the deterministic correction. The real phase is a
global lift of the inverse product character. An integer array with zero sums
on all old coordinate lines is converted to an integer additive hom, so its
`2π` shift is periodic at every old lattice element. -/
theorem realize_corrected_tensor_array {ι : Type*}
    [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) (r : ℕ)
    (χ : Fin (r + 1) → AddChar (TensorLattice ι n) Circle)
    (Z : TensorIndex ι n → ℤ)
    (hZ : ∀ (j : TensorIndex ι n) (i : ι),
      ∑ k : Fin (n i + 1), Z (Function.update j i k) = 0) :
    ∃ η : AddChar (NextTensor (TensorLattice ι n) r) Circle,
      ∀ (j : TensorIndex ι n) (k : Fin (r + 1)),
        (η (nextFrequency r (tensorColumn n j) k) : ℂ) =
          (χ k (tensorColumn n j) : ℂ) *
            Complex.exp (Complex.I *
              (((TensorRealCharacter.globalRealLiftHom n
                    ((∏ k : Fin (r + 1), χ k)⁻¹) (tensorColumn n j) -
                  (2 * Real.pi) * (Z j : ℝ)) /
                ((r + 1 : ℕ) : ℝ) : ℝ) : ℂ)) := by
  let θ : AddChar (TensorLattice ι n) Circle :=
    (∏ k : Fin (r + 1), χ k)⁻¹
  let FX := TensorRealCharacter.globalRealLiftHom n θ
  obtain ⟨FZ, hFZ⟩ := TensorRealCharacter.realize_integer_array n Z hZ
  have hFX (g : TensorLattice ι n) :
      Circle.exp (FX g) = ((∏ k : Fin (r + 1), χ k)⁻¹) g := by
    exact TensorRealCharacter.exp_globalRealLiftHom n θ g
  obtain ⟨η, hη⟩ := realize_corrected_tuple r χ FX FZ hFX
  refine ⟨η, ?_⟩
  intro j k
  have h := hη (tensorColumn n j) k
  rw [hFZ j] at h
  exact h

/-- The one-step positive-real estimate from an explicit finite rounding law
on integer additive phases. The law may depend on the inverse-product
character. Its coordinate moments are required only on the selected old
frequencies `E`. The deterministic realization is supplied by
`realize_corrected_tuple`, so every sample is a genuine target character. -/
theorem tensor_step_of_finite_hom_rounding {ι : Type*}
    [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) (r : ℕ)
    (E : Finset (TensorLattice ι n)) (Q ρ : ℝ)
    (hbase : TensorExtension.PositiveRealParameter E ρ)
    (hround : ∀ θ : AddChar (TensorLattice ι n) Circle,
      ∃ (s : Finset (TensorLattice ι n →+ ℤ))
        (w : (TensorLattice ι n →+ ℤ) → ℝ),
        (∀ FZ ∈ s, 0 ≤ w FZ) ∧
        (∑ FZ ∈ s, w FZ) = 1 ∧
        (∀ g ∈ E,
          (∑ FZ ∈ s, w FZ *
            (TensorRealCharacter.globalRealLiftHom n θ g -
              (2 * Real.pi) * (FZ g : ℝ))) = 0) ∧
        (∀ g ∈ E,
          (∑ FZ ∈ s, w FZ *
            (TensorRealCharacter.globalRealLiftHom n θ g -
              (2 * Real.pi) * (FZ g : ℝ)) ^ 2) ≤ Q)) :
    ∀ c : TensorLattice ι n → Fin (r + 1) → ℂ,
      ∃ η : AddChar (NextTensor (TensorLattice ι n) r) Circle,
        (ρ - 3 * Q / ((r + 1 : ℕ) : ℝ) ^ 2) *
          (∑ j : Fin (r + 1), ∑ g ∈ E, ‖c g j‖) ≤
          (∑ j : Fin (r + 1), ∑ g ∈ E,
            c g j * (η (nextFrequency r g j) : ℂ)).re := by
  classical
  apply TensorExtension.positiveRealParameter_tensor_step
    E (r + 1) (by omega) Q ρ (nextFrequency r) hbase
  intro χ
  let θ : AddChar (TensorLattice ι n) Circle :=
    (∏ j : Fin (r + 1), χ j)⁻¹
  let FX := TensorRealCharacter.globalRealLiftHom n θ
  obtain ⟨s, w, hw, hweight, hmean, hmoment⟩ := hround θ
  refine ⟨s, w, (fun FZ g => FX g - (2 * Real.pi) * (FZ g : ℝ)),
    hw, hweight, hmean, hmoment, ?_⟩
  intro FZ hFZ
  have hFX (g : TensorLattice ι n) :
      Circle.exp (FX g) = ((∏ j : Fin (r + 1), χ j)⁻¹) g :=
    TensorRealCharacter.exp_globalRealLiftHom n θ g
  obtain ⟨η, hη⟩ := realize_corrected_tuple r χ FX FZ hFX
  refine ⟨η, ?_⟩
  intro g hg j
  exact hη g j

end Erdos.Research.Problem774.TensorLiftAssembly

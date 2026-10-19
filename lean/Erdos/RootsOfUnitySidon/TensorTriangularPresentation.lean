import Erdos.RootsOfUnitySidon.TensorLatticeRounding
import Erdos.RootsOfUnitySidon.SimplexGramSchmidtInverse
import Mathlib.Data.Fintype.Sort
import Mathlib.Order.Extension.Linear
import Mathlib.Tactic

/-!
# The explicit triangular presentation of the anchored tensor lattice

The one-factor inverse simplex identity tensors to a unitriangular change
from the integer anchored basis to the orthogonal tensor vectors. A linear
extension of the componentwise order provides the `Fin` ordering required by
the finite rounding law.
-/

namespace Erdos.Research.Problem774.TensorTriangularPresentation

open Finset Erdos.Research


/-- Coefficient of one orthogonal simplex column in an anchored basis
column. -/
noncomputable def inverseCoeff (n : ℕ) (a j : Fin n) : ℝ :=
  if j = a then 1 else if j < a then 1 / (j.val + 2 : ℝ) else 0

theorem inverseCoeff_diag (n : ℕ) (a : Fin n) : inverseCoeff n a a = 1 := by
  simp [inverseCoeff]

theorem inverseCoeff_zero_of_gt (n : ℕ) {a j : Fin n} (h : a < j) :
    inverseCoeff n a j = 0 := by
  simp [inverseCoeff, h.ne', not_lt_of_ge h.le]

private theorem anchoredBasis_inverse_sum (n : ℕ) (a : Fin n)
    (v : Fin (n + 1)) :
    TensorGramTrace.anchoredBasis n a v =
      ∑ j : Fin n, inverseCoeff n a j *
        Erdos.Research.Problem774.SimplexGramSchmidt.anchoredVector n
          (Erdos.Research.Problem774.SimplexGramSchmidt.orthogonalCoeff n j) v := by
  rw [SimplexGramSchmidtInverse.anchoredBasis_inverse]
  symm
  calc
    (∑ j : Fin n, inverseCoeff n a j *
      Erdos.Research.Problem774.SimplexGramSchmidt.anchoredVector n
        (Erdos.Research.Problem774.SimplexGramSchmidt.orthogonalCoeff n j) v) =
        (∑ j : Fin n,
          if j = a then
            Erdos.Research.Problem774.SimplexGramSchmidt.anchoredVector n
              (Erdos.Research.Problem774.SimplexGramSchmidt.orthogonalCoeff n j) v
          else 0) +
        (∑ j : Fin n,
          if j ∈ Finset.Iio a then
            (1 / (j.val + 2 : ℝ)) *
              Erdos.Research.Problem774.SimplexGramSchmidt.anchoredVector n
                (Erdos.Research.Problem774.SimplexGramSchmidt.orthogonalCoeff n j) v
          else 0) := by
      rw [← Finset.sum_add_distrib]
      apply Finset.sum_congr rfl
      intro j _
      by_cases hja : j = a
      · subst j
        simp [inverseCoeff]
      · by_cases hlt : j < a
        · simp [inverseCoeff, hja, hlt]
        · simp [inverseCoeff, hja, hlt]
    _ = _ := by
      simp only [Fintype.sum_ite_mem]
      simp

/-- Product of the explicit inverse coefficients. -/
noncomputable def inverseTensorCoeff {ι : Type*} [Fintype ι]
    (n : ι → ℕ) (a j : TensorGramTrace.TensorBasis ι n) : ℝ :=
  ∏ i : ι, inverseCoeff (n i) (a i) (j i)

theorem inverseTensorCoeff_diag {ι : Type*} [Fintype ι]
    (n : ι → ℕ) (a : TensorGramTrace.TensorBasis ι n) :
    inverseTensorCoeff n a a = 1 := by
  simp [inverseTensorCoeff, inverseCoeff_diag]

theorem inverseTensorCoeff_zero_of_not_le {ι : Type*}
    [Fintype ι] (n : ι → ℕ) (a j : TensorGramTrace.TensorBasis ι n)
    (h : ¬ ∀ i : ι, j i ≤ a i) : inverseTensorCoeff n a j = 0 := by
  classical
  obtain ⟨i, hi⟩ := not_forall.mp h
  have hlt : a i < j i := lt_of_not_ge hi
  exact Finset.prod_eq_zero (Finset.mem_univ i)
    (inverseCoeff_zero_of_gt (n i) hlt)

/-- The anchored tensor basis expands in the orthogonal tensor vectors
with product inverse coefficients. -/
theorem tensorAnchoredBasis_inverse {ι : Type*}
    [Fintype ι] [DecidableEq ι] (n : ι → ℕ)
    (a : TensorGramTrace.TensorBasis ι n) (p : TensorGramTrace.TensorVertex ι n) :
    TensorGramTrace.tensorAnchoredBasis n a p =
      ∑ j : TensorGramTrace.TensorBasis ι n,
        inverseTensorCoeff n a j * TensorGramTrace.orthogonalTensor n j p := by
  classical
  let f : ∀ i : ι, Fin (n i) → ℝ := fun i j =>
    inverseCoeff (n i) (a i) j *
      Erdos.Research.Problem774.SimplexGramSchmidt.anchoredVector (n i)
        (Erdos.Research.Problem774.SimplexGramSchmidt.orthogonalCoeff (n i) j) (p i)
  calc
    TensorGramTrace.tensorAnchoredBasis n a p =
        ∏ i : ι, ∑ j : Fin (n i), f i j := by
      unfold TensorGramTrace.tensorAnchoredBasis
      apply Finset.prod_congr rfl
      intro i _
      exact anchoredBasis_inverse_sum (n i) (a i) (p i)
    _ = ∑ j : TensorGramTrace.TensorBasis ι n, ∏ i : ι, f i (j i) :=
      Fintype.prod_sum f
    _ = ∑ j : TensorGramTrace.TensorBasis ι n,
          inverseTensorCoeff n a j * TensorGramTrace.orthogonalTensor n j p := by
      apply Finset.sum_congr rfl
      intro j _
      simp only [f, inverseTensorCoeff, TensorGramTrace.orthogonalTensor,
        Finset.prod_mul_distrib]

/-- The product basis, with its componentwise partial order. -/
abbrev Basis (ι : Type*) (n : ι → ℕ) := TensorGramTrace.TensorBasis ι n

/-- Choose a linear extension of the componentwise order, then enumerate
its finite elements increasingly. -/
noncomputable def orderedOrderIso {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) :
    Fin (Fintype.card (Basis ι n)) ≃o LinearExtension (Basis ι n) := by
  letI : Fintype (LinearExtension (Basis ι n)) :=
    inferInstanceAs (Fintype (Basis ι n))
  exact monoEquivOfFin (LinearExtension (Basis ι n)) rfl

noncomputable def orderedEquiv {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) :
    Fin (Fintype.card (Basis ι n)) ≃ Basis ι n :=
  (orderedOrderIso n).toEquiv

/-- Componentwise order is respected by the chosen enumeration. -/
theorem orderedEquiv_mono {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ)
    {r s : Fin (Fintype.card (Basis ι n))}
    (h : ∀ i : ι, (orderedEquiv n r) i ≤ (orderedEquiv n s) i) :
    r ≤ s := by
  have hpoint : (orderedEquiv n r : Basis ι n) ≤
      (orderedEquiv n s : Basis ι n) := h
  have hlin : (toLinearExtension (orderedEquiv n r)) ≤
      (toLinearExtension (orderedEquiv n s)) :=
    (toLinearExtension : Basis ι n →o LinearExtension (Basis ι n)).monotone hpoint
  change orderedOrderIso n r ≤ orderedOrderIso n s at hlin
  exact (orderedOrderIso n).le_iff_le.mp hlin

/-- The off-order inverse coefficients vanish in this linear extension. -/
theorem inverseTensorCoeff_ordered_zero {ι : Type*}
    [Fintype ι] [DecidableEq ι] (n : ι → ℕ)
    {r s : Fin (Fintype.card (Basis ι n))} (h : r < s) :
    inverseTensorCoeff n (orderedEquiv n r) (orderedEquiv n s) = 0 := by
  classical
  apply inverseTensorCoeff_zero_of_not_le
  intro hpoint
  have hle : s ≤ r := orderedEquiv_mono n hpoint
  exact (not_le_of_gt h) hle

/-- The integer anchored tensor basis is triangular in the orthogonal
tensor vectors. This supplies the concrete presentation required by the
finite rounding law. -/
noncomputable def concretePresentation {ι : Type*}
    [Fintype ι] [DecidableEq ι] (n : ι → ℕ) :
    TensorLatticeRounding.TriangularPresentation n := by
  classical
  let e := orderedEquiv n
  refine {
    N := Fintype.card (Basis ι n)
    enumeration := e
    μ := fun r s => inverseTensorCoeff n (e r) (e s)
    basis_expansion := ?_ }
  intro r p
  rw [← TensorLatticeRounding.tensorAnchoredBasis_eq_intColumn,
    tensorAnchoredBasis_inverse]
  have hreindex :
      (∑ a : Basis ι n,
          inverseTensorCoeff n (e r) a * TensorGramTrace.orthogonalTensor n a p) =
        ∑ s : Fin (Fintype.card (Basis ι n)),
          inverseTensorCoeff n (e r) (e s) *
            TensorGramTrace.orthogonalTensor n (e s) p := by
    symm
    exact Fintype.sum_equiv e
      (fun s : Fin (Fintype.card (Basis ι n)) =>
        inverseTensorCoeff n (e r) (e s) *
          TensorGramTrace.orthogonalTensor n (e s) p)
      (fun a : Basis ι n =>
        inverseTensorCoeff n (e r) a *
          TensorGramTrace.orthogonalTensor n a p)
      (fun s => rfl)
  rw [hreindex]
  let u : Fin (Fintype.card (Basis ι n)) → ℝ := fun s =>
    TensorGramTrace.orthogonalTensor n (e s) p
  let D : Fin (Fintype.card (Basis ι n)) → ℝ := fun s =>
    inverseTensorCoeff n (e r) (e s)
  change (∑ s, D s * u s) =
    LatticeRounding.triangularBasis (fun i j => inverseTensorCoeff n (e i) (e j))
      (fun s => TensorGramTrace.orthogonalTensor n (e s)) r p
  have hterm (s : Fin (Fintype.card (Basis ι n))) :
      D s * u s =
        (if s = r then u s else 0) +
          (if s ∈ Finset.Iio r then D s * u s else 0) := by
    by_cases hsr : s = r
    · subst s
      simp [D, inverseTensorCoeff_diag]
    · by_cases hlt : s < r
      · simp [hsr, hlt]
      · have hrs : r < s := lt_of_le_of_ne (le_of_not_gt hlt) (Ne.symm hsr)
        have hz : D s = 0 := inverseTensorCoeff_ordered_zero n hrs
        simp [hsr, hlt, hz]
  have hsum : (∑ s, D s * u s) =
      ∑ s : Fin (Fintype.card (Basis ι n)),
        ((if s = r then u s else 0) +
          (if s ∈ Finset.Iio r then D s * u s else 0)) := by
    apply Finset.sum_congr rfl
    intro s _
    exact hterm s
  rw [hsum]
  rw [Finset.sum_add_distrib]
  have hsingle : (∑ s : Fin (Fintype.card (Basis ι n)),
      if s = r then u s else 0) = u r := by simp
  rw [hsingle]
  simp only [Fintype.sum_ite_mem]
  rfl

/-- Every real coordinate-line-zero array admits a finite law supported on
integer coordinate-line-zero arrays, with unbiased pointwise error and the
explicit tensor Gram variance bound. -/
theorem finite_lineZero_rounding {ι : Type*}
    [Fintype ι] [DecidableEq ι] (n : ι → ℕ)
    (X : TensorGramTrace.TensorVertex ι n → ℝ)
    (hX : TensorLatticeRounding.LineZero n X) :
    ∃ L : LatticeRounding.Law (TensorGramTrace.TensorVertex ι n → ℤ),
      LatticeRounding.Law.All (TensorLatticeRounding.LineZero n) L ∧
      ∀ p : TensorGramTrace.TensorVertex ι n,
        L.expect (fun Z => X p - (Z p : ℝ)) = 0 ∧
        L.expect (fun Z => (X p - (Z p : ℝ)) ^ 2) ≤
          (1 / 4 : ℝ) *
            ∑ j : TensorGramTrace.TensorBasis ι n,
              (TensorGramTrace.orthogonalTensor n j p) ^ 2 := by
  let P := concretePresentation n
  let α := TensorLatticeRounding.representCoeff P X
  refine ⟨TensorLatticeRounding.roundedLaw P α,
    TensorLatticeRounding.roundedLaw_lineZero P α, ?_⟩
  intro p
  exact TensorLatticeRounding.roundedLaw_moments P X α
    (TensorLatticeRounding.lineZero_represent P X hX) p

end Erdos.Research.Problem774.TensorTriangularPresentation

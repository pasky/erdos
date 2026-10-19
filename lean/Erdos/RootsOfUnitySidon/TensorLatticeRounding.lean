import Erdos.RootsOfUnitySidon.LatticeRounding
import Erdos.RootsOfUnitySidon.TensorGramTrace
import Erdos.RootsOfUnitySidon.TensorPhaseLattice
import Erdos.RootsOfUnitySidon.TensorLineZeroSpan
import Mathlib.Tactic

/-!
# Finite unbiased rounding in the anchored tensor lattice

This module turns the generic triangular lattice rounding law into finite
random integer arrays on a product simplex grid. Every sample has zero sum
along each coordinate line. The mean error is zero, and the pointwise
second moment is bounded by one quarter of the squared trace of the
orthogonal tensor vectors.

`TriangularPresentation` records the remaining basis-change identity: a
linear enumeration of the anchored tensor basis and the coefficients of
that integer basis in the orthogonal tensor basis. The companion module
`TensorGramTrace` proves the reverse unitriangular basis change.
-/

namespace Erdos.Research.Problem774.TensorLatticeRounding

open Finset

open Erdos.Research

/-- A real or integer array has zero sum along every coordinate line. -/
def LineZero {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) {R : Type*} [AddCommGroup R]
    (X : TensorGramTrace.TensorVertex ι n → R) : Prop :=
  ∀ p : TensorGramTrace.TensorVertex ι n, ∀ i : ι,
    ∑ k : Fin (n i + 1), X (Function.update p i k) = 0

/-- The real anchored basis column is the integer simplex column after
casting to the reals. -/
theorem anchoredBasis_eq_intColumn (n : ℕ) (a : Fin n)
    (v : Fin (n + 1)) :
    TensorGramTrace.anchoredBasis n a v =
      (SimplexTorus.column n v a : ℝ) := by
  classical
  induction v using Fin.lastCases with
  | last =>
      have hsum :
          (∑ i : Fin n, SimplexTorus.basis n i) a = (1 : ℤ) := by
        simp [SimplexTorus.basis]
      have hne : Fin.last n ≠ a.castSucc := ne_of_gt a.castSucc_lt_last
      simp [TensorGramTrace.anchoredBasis, SimplexTorus.column_last,
        SimplexTorus.lastColumn, hsum, hne]
  | cast j =>
      by_cases h : j = a
      · subst j
        simp [TensorGramTrace.anchoredBasis, SimplexTorus.column_castSucc,
          SimplexTorus.basis]
      · simp [TensorGramTrace.anchoredBasis, SimplexTorus.column_castSucc,
          SimplexTorus.basis, h]

/-- The real tensor anchored basis is the cast of the integer tensor
column coefficient. -/
theorem tensorAnchoredBasis_eq_intColumn {ι : Type*}
    [Fintype ι] (n : ι → ℕ)
    (a : TensorGramTrace.TensorBasis ι n)
    (p : TensorGramTrace.TensorVertex ι n) :
    TensorGramTrace.tensorAnchoredBasis n a p =
      (TensorPhaseLattice.tensorColumn n p a : ℝ) := by
  classical
  simp only [TensorGramTrace.tensorAnchoredBasis,
    TensorPhaseLattice.tensorColumn, Int.cast_prod]
  apply Finset.prod_congr rfl
  intro i _
  exact anchoredBasis_eq_intColumn (n i) (a i) (p i)

/-- Data identifying the integer anchored tensor lattice with the generic
triangular presentation used by the finite rounding theorem. -/
structure TriangularPresentation {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) where
  N : ℕ
  enumeration : Fin N ≃ TensorGramTrace.TensorBasis ι n
  μ : Fin N → Fin N → ℝ
  basis_expansion : ∀ (j : Fin N) (p : TensorGramTrace.TensorVertex ι n),
    (TensorPhaseLattice.tensorColumn n p (enumeration j) : ℝ) =
      LatticeRounding.triangularBasis μ
        (fun k => TensorGramTrace.orthogonalTensor n (enumeration k)) j p

/-- Integer synthesis follows from the one-vector triangular presentation. -/
theorem TriangularPresentation.synthesis {ι : Type*}
    [Fintype ι] [DecidableEq ι] {n : ι → ℕ}
    (P : TriangularPresentation n) (z : Fin P.N → ℤ)
    (p : TensorGramTrace.TensorVertex ι n) :
    LatticeRounding.latticePoint P.μ
      (fun j => TensorGramTrace.orthogonalTensor n (P.enumeration j)) z p =
        ∑ j : Fin P.N, (z j : ℝ) *
          (TensorPhaseLattice.tensorColumn n p (P.enumeration j) : ℝ) := by
  rw [LatticeRounding.latticePoint_eq_sum_basis]
  apply Finset.sum_congr rfl
  intro j _
  rw [P.basis_expansion j p]

/-- Coefficient matrix of the generic triangular basis change. -/
def triangularCoeff {ι : Type*} [Fintype ι] [DecidableEq ι]
    {n : ι → ℕ} (P : TriangularPresentation n)
    (j k : Fin P.N) : ℝ :=
  if k = j then 1 else if k < j then P.μ j k else 0

private theorem triangularBasis_eq_sum {ι : Type*}
    [Fintype ι] [DecidableEq ι] {n : ι → ℕ}
    (P : TriangularPresentation n) (j : Fin P.N)
    (p : TensorGramTrace.TensorVertex ι n) :
    LatticeRounding.triangularBasis P.μ
      (fun k => TensorGramTrace.orthogonalTensor n (P.enumeration k)) j p =
    ∑ k : Fin P.N, triangularCoeff P j k *
      TensorGramTrace.orthogonalTensor n (P.enumeration k) p := by
  let u : Fin P.N → ℝ := fun k =>
    TensorGramTrace.orthogonalTensor n (P.enumeration k) p
  change u j + ∑ k ∈ Finset.Iio j, P.μ j k * u k =
    ∑ k : Fin P.N, triangularCoeff P j k * u k
  symm
  calc
    (∑ k : Fin P.N, triangularCoeff P j k * u k) =
        (∑ k : Fin P.N, if k = j then u k else 0) +
          (∑ k : Fin P.N,
            if k ∈ Finset.Iio j then P.μ j k * u k else 0) := by
      rw [← Finset.sum_add_distrib]
      apply Finset.sum_congr rfl
      intro k _
      by_cases hkj : k = j
      · subst k
        simp [triangularCoeff]
      · by_cases hlt : k < j
        · simp [triangularCoeff, hkj, hlt]
        · simp [triangularCoeff, hkj, hlt]
    _ = u j + ∑ k ∈ Finset.Iio j, P.μ j k * u k := by
      simp only [Fintype.sum_ite_mem]
      simp

/-- Orthogonal coordinates obtained by expanding the anchored coordinates
through the triangular basis change. -/
noncomputable def representCoeff {ι : Type*}
    [Fintype ι] [DecidableEq ι] {n : ι → ℕ}
    (P : TriangularPresentation n)
    (X : TensorGramTrace.TensorVertex ι n → ℝ)
    (k : Fin P.N) : ℝ :=
  ∑ j : Fin P.N,
    X (TensorPhaseLattice.baseIndex n (P.enumeration j)) *
      triangularCoeff P j k

/-- Once a triangular presentation is supplied, the line-zero relations
themselves provide the orthogonal-coordinate representation of `X`. -/
theorem lineZero_represent {ι : Type*}
    [Fintype ι] [DecidableEq ι] {n : ι → ℕ}
    (P : TriangularPresentation n)
    (X : TensorGramTrace.TensorVertex ι n → ℝ)
    (hX : LineZero n X) (p : TensorGramTrace.TensorVertex ι n) :
    X p = LatticeRounding.targetPoint (representCoeff P X)
      (fun k => TensorGramTrace.orthogonalTensor n (P.enumeration k)) p := by
  classical
  let c : Fin P.N → ℝ := fun j =>
    X (TensorPhaseLattice.baseIndex n (P.enumeration j))
  let u : Fin P.N → ℝ := fun k =>
    TensorGramTrace.orthogonalTensor n (P.enumeration k) p
  calc
    X p = ∑ a : TensorGramTrace.TensorBasis ι n,
        X (TensorPhaseLattice.baseIndex n a) *
          (TensorPhaseLattice.tensorColumn n p a : ℝ) :=
      TensorLineZeroSpan.reconstruct n X hX p
    _ = ∑ j : Fin P.N,
        c j * (TensorPhaseLattice.tensorColumn n p (P.enumeration j) : ℝ) := by
      symm
      exact Fintype.sum_equiv P.enumeration
        (fun j : Fin P.N =>
          c j * (TensorPhaseLattice.tensorColumn n p (P.enumeration j) : ℝ))
        (fun a : TensorGramTrace.TensorBasis ι n =>
          X (TensorPhaseLattice.baseIndex n a) *
            (TensorPhaseLattice.tensorColumn n p a : ℝ))
        (fun j => rfl)
    _ = ∑ j : Fin P.N, c j *
          (∑ k : Fin P.N, triangularCoeff P j k * u k) := by
      apply Finset.sum_congr rfl
      intro j _
      rw [P.basis_expansion j p, triangularBasis_eq_sum]
    _ = ∑ k : Fin P.N, (∑ j : Fin P.N, c j * triangularCoeff P j k) * u k := by
      simp_rw [Finset.mul_sum, Finset.sum_mul]
      rw [Finset.sum_comm]
      apply Finset.sum_congr rfl
      intro k _
      apply Finset.sum_congr rfl
      intro j _
      ring
    _ = LatticeRounding.targetPoint (representCoeff P X)
          (fun k => TensorGramTrace.orthogonalTensor n (P.enumeration k)) p := by
      rfl

/-- The integer array obtained from coefficients in the anchored tensor
basis. -/
def sampleArray {ι : Type*} [Fintype ι] [DecidableEq ι]
    {n : ι → ℕ} (P : TriangularPresentation n)
    (z : Fin P.N → ℤ) (p : TensorGramTrace.TensorVertex ι n) : ℤ :=
  ∑ j : Fin P.N, z j * TensorPhaseLattice.tensorColumn n p (P.enumeration j)

theorem sampleArray_lineZero {ι : Type*} [Fintype ι] [DecidableEq ι]
    {n : ι → ℕ} (P : TriangularPresentation n) (z : Fin P.N → ℤ) :
    LineZero n (sampleArray P z) := by
  classical
  intro p i
  simp only [sampleArray]
  rw [Finset.sum_comm]
  apply Finset.sum_eq_zero
  intro j _
  rw [← Finset.mul_sum]
  have h := congrArg
    (fun f : TensorPhaseLattice.TensorLattice ι n => f (P.enumeration j))
    (TensorPhaseLattice.sum_tensorColumn_line n p i)
  simp only [Finset.sum_apply, Pi.zero_apply] at h
  simp [h]

theorem sampleArray_cast {ι : Type*} [Fintype ι] [DecidableEq ι]
    {n : ι → ℕ} (P : TriangularPresentation n)
    (z : Fin P.N → ℤ) (p : TensorGramTrace.TensorVertex ι n) :
    (sampleArray P z p : ℝ) =
      ∑ j : Fin P.N, (z j : ℝ) *
        (TensorPhaseLattice.tensorColumn n p (P.enumeration j) : ℝ) := by
  simp [sampleArray]

/-- The finite binary-tree law of integer arrays obtained by triangular
rounding. -/
noncomputable def roundedLaw {ι : Type*} [Fintype ι] [DecidableEq ι]
    {n : ι → ℕ} (P : TriangularPresentation n)
    (α : Fin P.N → ℝ) :
    LatticeRounding.Law (TensorGramTrace.TensorVertex ι n → ℤ) :=
  (LatticeRounding.roundLaw P.N α P.μ).map (fun out => sampleArray P out.1)

theorem roundedLaw_lineZero {ι : Type*} [Fintype ι] [DecidableEq ι]
    {n : ι → ℕ} (P : TriangularPresentation n)
    (α : Fin P.N → ℝ) :
    LatticeRounding.Law.All (LineZero n) (roundedLaw P α) := by
  unfold roundedLaw
  apply LatticeRounding.Law.all_map
  induction LatticeRounding.roundLaw P.N α P.μ with
  | pure out => exact sampleArray_lineZero P out.1
  | mix p hp hp1 lo hi ihlo ihhi => exact ⟨ihlo, ihhi⟩

/-- A real tensor array represented in orthogonal coordinates rounds to
actual integer line-zero arrays, with an unbiased pointwise error. -/
theorem law_mean_zero {ι : Type*} [Fintype ι] [DecidableEq ι]
    {n : ι → ℕ} (P : TriangularPresentation n)
    (X : TensorGramTrace.TensorVertex ι n → ℝ) (α : Fin P.N → ℝ)
    (hX : ∀ p, X p = LatticeRounding.targetPoint α
      (fun j => TensorGramTrace.orthogonalTensor n (P.enumeration j)) p)
    (p : TensorGramTrace.TensorVertex ι n) :
    (LatticeRounding.roundLaw P.N α P.μ).expect
      (fun out => X p - (sampleArray P out.1 p : ℝ)) = 0 := by
  have hpoint (out : LatticeRounding.Outcome P.N) :
      X p - (sampleArray P out.1 p : ℝ) =
        LatticeRounding.targetPoint α
            (fun j => TensorGramTrace.orthogonalTensor n (P.enumeration j)) p -
          LatticeRounding.latticePoint P.μ
            (fun j => TensorGramTrace.orthogonalTensor n (P.enumeration j)) out.1 p := by
    rw [hX p, sampleArray_cast, P.synthesis]
  calc
    _ = (LatticeRounding.roundLaw P.N α P.μ).expect
        (fun out => LatticeRounding.targetPoint α
          (fun j => TensorGramTrace.orthogonalTensor n (P.enumeration j)) p -
          LatticeRounding.latticePoint P.μ
            (fun j => TensorGramTrace.orthogonalTensor n (P.enumeration j)) out.1 p) := by
          apply LatticeRounding.Law.expect_congr
          exact hpoint
    _ = 0 := LatticeRounding.roundLaw_point_mean_zero P.N α P.μ _ p

/-- The pointwise second moment is bounded by the tensor Gram trace. -/
theorem law_second_moment_le {ι : Type*} [Fintype ι] [DecidableEq ι]
    {n : ι → ℕ} (P : TriangularPresentation n)
    (X : TensorGramTrace.TensorVertex ι n → ℝ) (α : Fin P.N → ℝ)
    (hX : ∀ p, X p = LatticeRounding.targetPoint α
      (fun j => TensorGramTrace.orthogonalTensor n (P.enumeration j)) p)
    (p : TensorGramTrace.TensorVertex ι n) :
    (LatticeRounding.roundLaw P.N α P.μ).expect
      (fun out => (X p - (sampleArray P out.1 p : ℝ)) ^ 2) ≤
        (1 / 4 : ℝ) *
          ∑ j : TensorGramTrace.TensorBasis ι n, (TensorGramTrace.orthogonalTensor n j p) ^ 2 := by
  have hpoint (out : LatticeRounding.Outcome P.N) :
      X p - (sampleArray P out.1 p : ℝ) =
        LatticeRounding.targetPoint α
            (fun j => TensorGramTrace.orthogonalTensor n (P.enumeration j)) p -
          LatticeRounding.latticePoint P.μ
            (fun j => TensorGramTrace.orthogonalTensor n (P.enumeration j)) out.1 p := by
    rw [hX p, sampleArray_cast, P.synthesis]
  calc
    _ = (LatticeRounding.roundLaw P.N α P.μ).expect
        (fun out => (LatticeRounding.targetPoint α
          (fun j => TensorGramTrace.orthogonalTensor n (P.enumeration j)) p -
          LatticeRounding.latticePoint P.μ
            (fun j => TensorGramTrace.orthogonalTensor n (P.enumeration j)) out.1 p) ^ 2) := by
          apply LatticeRounding.Law.expect_congr
          intro out
          rw [hpoint]
    _ ≤ (1 / 4 : ℝ) *
          ∑ j : Fin P.N, (TensorGramTrace.orthogonalTensor n (P.enumeration j) p) ^ 2 :=
            LatticeRounding.roundLaw_point_sq_le P.N α P.μ _ p
    _ = _ := by
          congr 1
          exact Fintype.sum_equiv P.enumeration
            (fun j : Fin P.N => (TensorGramTrace.orthogonalTensor n (P.enumeration j) p) ^ 2)
            (fun j : TensorGramTrace.TensorBasis ι n =>
              (TensorGramTrace.orthogonalTensor n j p) ^ 2)
            (fun j => rfl)

/-- The finite law is supported on integer line-zero arrays, is unbiased
at each vertex, and has the Gram-trace second-moment bound. -/
theorem roundedLaw_moments {ι : Type*} [Fintype ι] [DecidableEq ι]
    {n : ι → ℕ} (P : TriangularPresentation n)
    (X : TensorGramTrace.TensorVertex ι n → ℝ) (α : Fin P.N → ℝ)
    (hX : ∀ p, X p = LatticeRounding.targetPoint α
      (fun j => TensorGramTrace.orthogonalTensor n (P.enumeration j)) p)
    (p : TensorGramTrace.TensorVertex ι n) :
    (roundedLaw P α).expect (fun Z => X p - (Z p : ℝ)) = 0 ∧
    (roundedLaw P α).expect (fun Z => (X p - (Z p : ℝ)) ^ 2) ≤
      (1 / 4 : ℝ) *
        ∑ j : TensorGramTrace.TensorBasis ι n, (TensorGramTrace.orthogonalTensor n j p) ^ 2 := by
  constructor
  · rw [roundedLaw, LatticeRounding.Law.expect_map]
    exact law_mean_zero P X α hX p
  · rw [roundedLaw, LatticeRounding.Law.expect_map]
    exact law_second_moment_le P X α hX p

/-- Explicit finite samples of integer line-zero arrays, with nonnegative
weights summing to one and the pointwise moment bounds. -/
theorem finite_rounded_samples {ι : Type*} [Fintype ι] [DecidableEq ι]
    {n : ι → ℕ} (P : TriangularPresentation n)
    (X : TensorGramTrace.TensorVertex ι n → ℝ) (α : Fin P.N → ℝ)
    (hX : ∀ p, X p = LatticeRounding.targetPoint α
      (fun j => TensorGramTrace.orthogonalTensor n (P.enumeration j)) p) :
    let L := roundedLaw P α
    (∀ ω : LatticeRounding.Law.Sample L,
      LineZero n (LatticeRounding.Law.sampleValue L ω)) ∧
    (∀ ω : LatticeRounding.Law.Sample L,
      0 ≤ LatticeRounding.Law.sampleWeight L ω) ∧
    (∑ ω : LatticeRounding.Law.Sample L,
      LatticeRounding.Law.sampleWeight L ω) = 1 ∧
    (∀ p : TensorGramTrace.TensorVertex ι n,
      (∑ ω : LatticeRounding.Law.Sample L,
        LatticeRounding.Law.sampleWeight L ω *
          (X p - (LatticeRounding.Law.sampleValue L ω p : ℝ))) = 0 ∧
      (∑ ω : LatticeRounding.Law.Sample L,
        LatticeRounding.Law.sampleWeight L ω *
          (X p - (LatticeRounding.Law.sampleValue L ω p : ℝ)) ^ 2) ≤
        (1 / 4 : ℝ) *
          ∑ j : TensorGramTrace.TensorBasis ι n,
            (TensorGramTrace.orthogonalTensor n j p) ^ 2) := by
  dsimp
  refine ⟨?_, ?_, ?_, ?_⟩
  · intro ω
    exact LatticeRounding.Law.sample_all (roundedLaw P α) (LineZero n)
      (roundedLaw_lineZero P α) ω
  · exact LatticeRounding.Law.sampleWeight_nonneg _
  · exact LatticeRounding.Law.sampleWeight_sum_one _
  · intro p
    obtain ⟨hmean, hsq⟩ := roundedLaw_moments P X α hX p
    constructor
    · calc
        _ = (roundedLaw P α).expect (fun Z => X p - (Z p : ℝ)) :=
          LatticeRounding.Law.sample_expect (roundedLaw P α) _
        _ = 0 := hmean
    · calc
        _ = (roundedLaw P α).expect (fun Z => (X p - (Z p : ℝ)) ^ 2) :=
          LatticeRounding.Law.sample_expect (roundedLaw P α) _
        _ ≤ _ := hsq

/-- Every real line-zero array has a finite unbiased integer rounding once
the tensor basis is given in triangular orthogonal coordinates. -/
theorem finite_rounding_of_lineZero {ι : Type*}
    [Fintype ι] [DecidableEq ι] {n : ι → ℕ}
    (P : TriangularPresentation n)
    (X : TensorGramTrace.TensorVertex ι n → ℝ)
    (hX : LineZero n X) :
    let α := representCoeff P X
    let L := roundedLaw P α
    (∀ ω : LatticeRounding.Law.Sample L,
      LineZero n (LatticeRounding.Law.sampleValue L ω)) ∧
    (∀ ω : LatticeRounding.Law.Sample L,
      0 ≤ LatticeRounding.Law.sampleWeight L ω) ∧
    (∑ ω : LatticeRounding.Law.Sample L,
      LatticeRounding.Law.sampleWeight L ω) = 1 ∧
    (∀ p : TensorGramTrace.TensorVertex ι n,
      (∑ ω : LatticeRounding.Law.Sample L,
        LatticeRounding.Law.sampleWeight L ω *
          (X p - (LatticeRounding.Law.sampleValue L ω p : ℝ))) = 0 ∧
      (∑ ω : LatticeRounding.Law.Sample L,
        LatticeRounding.Law.sampleWeight L ω *
          (X p - (LatticeRounding.Law.sampleValue L ω p : ℝ)) ^ 2) ≤
        (1 / 4 : ℝ) *
          ∑ j : TensorGramTrace.TensorBasis ι n,
            (TensorGramTrace.orthogonalTensor n j p) ^ 2) := by
  dsimp
  exact finite_rounded_samples P X (representCoeff P X)
    (lineZero_represent P X hX)

end Erdos.Research.Problem774.TensorLatticeRounding

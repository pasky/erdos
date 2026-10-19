import Erdos.RootsOfUnitySidon.PrimeSimplexEmbedding
import Erdos.RootsOfUnitySidon.RootsOfUnityTensorCRT
import Erdos.RootsOfUnitySidon.TensorPhaseLattice

/-!
# Squarefree prime grids and simplex lattice coordinates

This module transports the recursive cyclotomic simplex basis to
the dependent-function indexing used by `TensorPhaseLattice`. It then identifies
the complex frequencies of its columns with the squarefree root grid.
-/

namespace Erdos.Research.Problem774.PrimeSimplexGrid

open scoped Classical
open Erdos.Research.Problem774.PrimeSimplex
open Erdos.Research.Problem774.TensorCRT
open Erdos.Research.Problem774.TensorPhaseLattice
open Erdos.Research.Problem774.SimplexTorus

/-- The dependent-function indexing of the free simplex tensor basis. -/
abbrev PrimeBasis (ps : List ℕ) :=
  TensorBasis (Fin ps.length) (fun i => ps.get i - 1)

/-- The dependent-function indexing of all root columns. -/
abbrev PrimeIndex (ps : List ℕ) :=
  (i : Fin ps.length) → Fin (ps.get i)

/-- Reassociate the recursive simplex basis as a dependent function on the
positions in the prime list. -/
def recursiveBasisEquiv : (ps : List ℕ) →
    SimplexTensor ps ≃ PrimeBasis ps
  | [] => {
      toFun := fun _ i => Fin.elim0 i
      invFun := fun _ => PUnit.unit
      left_inv := by intro x; cases x; rfl
      right_inv := by intro f; funext i; exact Fin.elim0 i }
  | p :: ps =>
      ((Equiv.refl (Fin (p - 1))).prodCongr (recursiveBasisEquiv ps)).trans
        (Fin.consEquiv
          (fun i : Fin (p :: ps).length => Fin ((p :: ps).get i - 1)))

/-- The complex frequency assigned to a dependent-function basis tuple. -/
noncomputable def primeBasisValue (ps : List ℕ) (a : PrimeBasis ps) : ℂ :=
  simplexValue ps ((recursiveBasisEquiv ps).symm a)

theorem primeBasisValue_eq_prod (ps : List ℕ) (a : PrimeBasis ps) :
    primeBasisValue ps a =
      ∏ i : Fin ps.length, PrimeSimplex.zeta (ps.get i) ^ ((a i : Fin (ps.get i - 1)) : ℕ) := by
  induction ps with
  | nil =>
      simp [primeBasisValue, simplexValue]
  | cons p ps ih =>
      change primeBasisValue (p :: ps) a =
        ∏ i : Fin (ps.length + 1), PrimeSimplex.zeta ((p :: ps).get i) ^ (a i : ℕ)
      rw [Fin.prod_univ_succ]
      change PrimeSimplex.zeta p ^ (a 0 : ℕ) * primeBasisValue ps (Fin.tail a) =
        PrimeSimplex.zeta p ^ (a 0 : ℕ) *
          ∏ i : Fin ps.length, PrimeSimplex.zeta (ps.get i) ^ ((Fin.tail a i : Fin (ps.get i - 1)) : ℕ)
      exact congrArg (fun w : ℂ => PrimeSimplex.zeta p ^ (a 0 : ℕ) * w) (ih (Fin.tail a))

/-- A small-prime tensor basis stays independent over the field of disjoint
tail primes, in the exact index type used by the phase-lattice modules. -/
theorem primeBasis_linearIndependent_over_tail (small tail : List ℕ)
    (hsmall : ∀ p ∈ small, p.Prime)
    (htail : ∀ q ∈ tail, q.Prime)
    (hsmall_nodup : small.Nodup)
    (hsep : ∀ p ∈ small, ∀ q ∈ tail, p ≠ q) :
    LinearIndependent (primeField tail.prod) (primeBasisValue small) := by
  exact LinearIndependent.comp
    (simplex_linearIndependent_over_tail small tail hsmall htail hsmall_nodup hsep)
    (recursiveBasisEquiv small).symm (recursiveBasisEquiv small).symm.injective

/-- Rational independence in the dependent-function indexing. -/
theorem primeBasis_linearIndependent (ps : List ℕ)
    (hprime : ∀ p ∈ ps, p.Prime) (hnodup : ps.Nodup) :
    LinearIndependent ℚ (primeBasisValue ps) :=
  (simplex_linearIndependent ps hprime hnodup).comp
    (recursiveBasisEquiv ps).symm (recursiveBasisEquiv ps).symm.injective

/-- Powers of the standard primitive root enumerate all roots of prime order. -/
noncomputable def primeRootPower (p : ℕ) (hp : p.Prime) (j : Fin p) : RootGrid p :=
  ⟨PrimeSimplex.zeta p ^ (j : ℕ), by
    calc
      (PrimeSimplex.zeta p ^ (j : ℕ)) ^ p = (PrimeSimplex.zeta p ^ p) ^ (j : ℕ) := by
        rw [← pow_mul, ← pow_mul, Nat.mul_comm]
      _ = 1 := by rw [(zeta_primitive p hp.pos).pow_eq_one, one_pow]⟩

/-- A prime root grid is indexed without duplication by its exponents. -/
noncomputable def primeRootEquiv (p : ℕ) (hp : p.Prime) : Fin p ≃ RootGrid p := by
  apply Equiv.ofBijective (primeRootPower p hp)
  constructor
  · intro i j hij
    apply Fin.ext
    exact (zeta_primitive p hp.pos).pow_inj i.isLt j.isLt
      (congrArg Subtype.val hij)
  · intro z
    letI : NeZero p := ⟨hp.pos.ne'⟩
    obtain ⟨i, hi, hz⟩ :=
      (zeta_primitive p hp.pos).eq_pow_of_pow_eq_one z.property
    exact ⟨⟨i, hi⟩, Subtype.ext hz⟩

/-- Prime-exponent tuples are equivalent to the corresponding tensor of
individual root grids. -/
noncomputable def primeIndexTensorEquiv (ps : List ℕ)
    (hprime : ∀ p ∈ ps, p.Prime) : PrimeIndex ps ≃ TensorGrid ps := by
  induction ps with
  | nil =>
      refine {
        toFun := fun _ => ⟨1, by simp⟩
        invFun := fun _ i => Fin.elim0 i
        left_inv := by intro f; funext i; exact Fin.elim0 i
        right_inv := ?_ }
      intro z
      apply Subtype.ext
      simpa using z.property.symm
  | cons p ps ih =>
      have hp : p.Prime := hprime p (by simp)
      have hprime' : ∀ q ∈ ps, q.Prime := by
        intro q hq
        exact hprime q (by simp [hq])
      exact
        ((Fin.consEquiv
          (fun i : Fin (p :: ps).length => Fin ((p :: ps).get i))).symm).trans
          ((primeRootEquiv p hp).prodCongr (ih hprime'))

/-- A finite tuple of exponents indexes the root grid of the squarefree
product exactly once. -/
noncomputable def primeGridEquiv (ps : List ℕ)
    (hprime : ∀ p ∈ ps, p.Prime) (hnodup : ps.Nodup) :
    PrimeIndex ps ≃ RootGrid ps.prod :=
  (primeIndexTensorEquiv ps hprime).trans (primeTensorGridEquiv ps hprime hnodup)

theorem primeIndexTensorValue_eq_prod (ps : List ℕ)
    (hprime : ∀ p ∈ ps, p.Prime) (j : PrimeIndex ps) :
    (tensorMultiply ps (primeIndexTensorEquiv ps hprime j) : ℂ) =
      ∏ i : Fin ps.length, PrimeSimplex.zeta (ps.get i) ^ (j i : ℕ) := by
  induction ps with
  | nil =>
      simp [primeIndexTensorEquiv, tensorMultiply]
      rfl
  | cons p ps ih =>
      have hp : p.Prime := hprime p (by simp)
      have hprime' : ∀ q ∈ ps, q.Prime := by
        intro q hq
        exact hprime q (by simp [hq])
      change (tensorMultiply (p :: ps) (primeIndexTensorEquiv (p :: ps) hprime j) : ℂ) =
        ∏ i : Fin (ps.length + 1), PrimeSimplex.zeta ((p :: ps).get i) ^ (j i : ℕ)
      rw [Fin.prod_univ_succ]
      change PrimeSimplex.zeta p ^ (j 0 : ℕ) *
        (tensorMultiply ps (primeIndexTensorEquiv ps hprime' (Fin.tail j)) : ℂ) =
          PrimeSimplex.zeta p ^ (j 0 : ℕ) *
            ∏ i : Fin ps.length, PrimeSimplex.zeta (ps.get i) ^ (Fin.tail j i : ℕ)
      exact congrArg (fun w : ℂ => PrimeSimplex.zeta p ^ (j 0 : ℕ) * w)
        (ih hprime' (Fin.tail j))

/-- The squarefree grid equivalence multiplies the local root powers. -/
theorem primeGridEquiv_val_eq_prod (ps : List ℕ)
    (hprime : ∀ p ∈ ps, p.Prime) (hnodup : ps.Nodup)
    (j : PrimeIndex ps) :
    ((primeGridEquiv ps hprime hnodup j : RootGrid ps.prod) : ℂ) =
      ∏ i : Fin ps.length, PrimeSimplex.zeta (ps.get i) ^ (j i : ℕ) := by
  calc
    ((primeGridEquiv ps hprime hnodup j : RootGrid ps.prod) : ℂ) =
        (tensorMultiply ps (primeIndexTensorEquiv ps hprime j) : ℂ) := by
          exact congrArg Subtype.val
            (tensorGridEquiv_apply ps
              (fun p hp => (hprime p hp).pos)
              (hnodup.pairwise_of_forall_ne fun p hp q hq hpq =>
                (Nat.coprime_primes (hprime p hp) (hprime q hq)).2 hpq)
              (primeIndexTensorEquiv ps hprime j))
    _ = _ := primeIndexTensorValue_eq_prod ps hprime j

/-- A simplex column evaluates at the prime-power basis as the corresponding
root of unity, including the last column. -/
theorem prime_column_evaluation (p : ℕ) (hp : p.Prime)
    (j : Fin (p - 1 + 1)) :
    (∑ a : Fin (p - 1), (column (p - 1) j a : ℂ) * PrimeSimplex.zeta p ^ (a : ℕ)) =
      PrimeSimplex.zeta p ^ (j : ℕ) := by
  classical
  induction j using Fin.lastCases with
  | cast i =>
      simp [basis, Pi.single_apply]
  | last =>
      have hlast (a : Fin (p - 1)) :
          (column (p - 1) (Fin.last (p - 1)) a : ℂ) = -1 := by
        simp [lastColumn, basis, Pi.single_apply]
      simp_rw [hlast]
      simp only [neg_one_mul]
      rw [Finset.sum_neg_distrib]
      change -(∑ a : Fin (p - 1), PrimeSimplex.zeta p ^ (a : ℕ)) = PrimeSimplex.zeta p ^ (p - 1)
      rw [Fin.sum_univ_eq_sum_range]
      exact (prime_last_column hp).symm

/-- The `p` exponents and the `p - 1 + 1` simplex columns have the same
indices for each prime factor. -/
def primeIndexColumnEquiv (ps : List ℕ)
    (hprime : ∀ p ∈ ps, p.Prime) :
    PrimeIndex ps ≃ TensorIndex (Fin ps.length) (fun i => ps.get i - 1) where
  toFun j i := (j i).cast (Nat.sub_add_cancel
    (hprime (ps.get i) (List.get_mem ps i)).one_le).symm
  invFun j i := (j i).cast (Nat.sub_add_cancel
    (hprime (ps.get i) (List.get_mem ps i)).one_le)
  left_inv := by
    intro j
    funext i
    apply Fin.ext
    rfl
  right_inv := by
    intro j
    funext i
    apply Fin.ext
    rfl

/-- Evaluating a pure integer tensor column against the prime-power basis
produces the product of the corresponding complex roots. -/
theorem prime_tensorColumn_evaluation (ps : List ℕ)
    (hprime : ∀ p ∈ ps, p.Prime)
    (j : TensorIndex (Fin ps.length) (fun i => ps.get i - 1)) :
    (∑ a : PrimeBasis ps,
      (tensorColumn (fun i : Fin ps.length => ps.get i - 1) j a : ℂ) *
        primeBasisValue ps a) =
      ∏ i : Fin ps.length, PrimeSimplex.zeta (ps.get i) ^ (j i : ℕ) := by
  classical
  calc
    (∑ a : PrimeBasis ps,
        (tensorColumn (fun i : Fin ps.length => ps.get i - 1) j a : ℂ) *
          primeBasisValue ps a) =
        ∑ a : PrimeBasis ps,
          ∏ i : Fin ps.length,
            (column (ps.get i - 1) (j i) (a i) : ℂ) *
              PrimeSimplex.zeta (ps.get i) ^ (a i : ℕ) := by
          apply Finset.sum_congr rfl
          intro a _
          rw [primeBasisValue_eq_prod]
          change ((∏ i : Fin ps.length,
            column (ps.get i - 1) (j i) (a i) : ℤ) : ℂ) *
              (∏ i : Fin ps.length, PrimeSimplex.zeta (ps.get i) ^ (a i : ℕ)) = _
          push_cast
          rw [← Finset.prod_mul_distrib]
    _ = ∏ i : Fin ps.length,
          ∑ b : Fin (ps.get i - 1),
            (column (ps.get i - 1) (j i) b : ℂ) * PrimeSimplex.zeta (ps.get i) ^ (b : ℕ) := by
          exact (Fintype.prod_sum
            (fun i (b : Fin (ps.get i - 1)) =>
              (column (ps.get i - 1) (j i) b : ℂ) * PrimeSimplex.zeta (ps.get i) ^ (b : ℕ))).symm
    _ = ∏ i : Fin ps.length, PrimeSimplex.zeta (ps.get i) ^ (j i : ℕ) := by
          apply Finset.prod_congr rfl
          intro i _
          exact prime_column_evaluation (ps.get i)
            (hprime (ps.get i) (List.get_mem ps i)) (j i)

/-- Evaluate an integer tensor-lattice vector by its complex prime-power
frequencies. -/
noncomputable def primeLatticeEvaluation (ps : List ℕ) :
    TensorLattice (Fin ps.length) (fun i => ps.get i - 1) →+ ℂ :=
  (Fintype.linearCombination ℤ (primeBasisValue ps)).toAddMonoidHom

theorem primeLatticeEvaluation_injective (ps : List ℕ)
    (hprime : ∀ p ∈ ps, p.Prime) (hnodup : ps.Nodup) :
    Function.Injective (primeLatticeEvaluation ps) := by
  exact ((primeBasis_linearIndependent ps hprime hnodup).restrict_scalars' ℤ).fintypeLinearCombination_injective

theorem primeLatticeEvaluation_tensorColumn (ps : List ℕ)
    (hprime : ∀ p ∈ ps, p.Prime)
    (j : TensorIndex (Fin ps.length) (fun i => ps.get i - 1)) :
    primeLatticeEvaluation ps
      (tensorColumn (fun i : Fin ps.length => ps.get i - 1) j) =
      ∏ i : Fin ps.length, PrimeSimplex.zeta (ps.get i) ^ (j i : ℕ) := by
  simpa [primeLatticeEvaluation, Fintype.linearCombination_apply, zsmul_eq_mul]
    using prime_tensorColumn_evaluation ps hprime j

/-- The integer tensor columns have exactly the same finite additive
relations as their complex prime-root frequencies. -/
theorem prime_tensorColumn_relation_iff (ps : List ℕ)
    (hprime : ∀ p ∈ ps, p.Prime) (hnodup : ps.Nodup)
    (s : Finset (TensorIndex (Fin ps.length) (fun i => ps.get i - 1)))
    (c : TensorIndex (Fin ps.length) (fun i => ps.get i - 1) → ℤ) :
    (∑ j ∈ s, c j • tensorColumn (fun i : Fin ps.length => ps.get i - 1) j = 0) ↔
      (∑ j ∈ s, (c j : ℂ) *
        ∏ i : Fin ps.length, PrimeSimplex.zeta (ps.get i) ^ (j i : ℕ)) = 0 := by
  have hmap : primeLatticeEvaluation ps
      (∑ j ∈ s, c j • tensorColumn (fun i : Fin ps.length => ps.get i - 1) j) =
      ∑ j ∈ s, (c j : ℂ) *
        ∏ i : Fin ps.length, PrimeSimplex.zeta (ps.get i) ^ (j i : ℕ) := by
    rw [map_sum]
    apply Finset.sum_congr rfl
    intro j _
    rw [map_zsmul, primeLatticeEvaluation_tensorColumn ps hprime j, zsmul_eq_mul]
  constructor
  · intro h
    rw [← hmap, h]
    exact map_zero (primeLatticeEvaluation ps)
  · intro h
    apply primeLatticeEvaluation_injective ps hprime hnodup
    rw [hmap, h]
    exact (map_zero (primeLatticeEvaluation ps)).symm

end Erdos.Research.Problem774.PrimeSimplexGrid

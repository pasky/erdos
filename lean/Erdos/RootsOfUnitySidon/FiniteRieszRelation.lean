import Erdos.RootsOfUnitySidon.PisierRelationCounting
import Erdos.RootsOfUnitySidon.FiniteOrthogonalCharacters
import Mathlib.Algebra.BigOperators.Ring.Finset

/-!
# Finite Riesz products and signed additive relations

This is a finite algebraic Fourier identity. The character average is the
finite sample from `FiniteOrthogonalCharacters`; no Haar measure is involved.
-/

namespace Erdos.Research.FiniteRieszRelation

open scoped BigOperators
open scoped ComplexConjugate
open Classical
open Erdos.Research.PisierRelationCounting
open Erdos.Research.FiniteOrthogonalCharacters

private noncomputable def disjointPairs (A : Finset ℂ) :
    Finset (Finset ℂ × Finset ℂ) :=
  (A.powerset.product A.powerset).filter fun p => Disjoint p.1 p.2

private theorem sum_disjointPairs (A : Finset ℂ)
    (f : Finset ℂ → Finset ℂ → ℂ) :
    (∑ p ∈ disjointPairs A, f p.1 p.2) =
      ∑ t ∈ A.powerset, ∑ u ∈ (A \ t).powerset, f t u := by
  classical
  apply Finset.sum_finset_product'
  intro p
  simp only [disjointPairs, Finset.mem_filter]
  constructor
  · rintro ⟨hp, htu⟩
    obtain ⟨ht, hu⟩ := Finset.mem_product.mp hp
    exact ⟨ht, Finset.mem_powerset.mpr
      (Finset.subset_sdiff.mpr
        ⟨Finset.mem_powerset.mp hu, htu.symm⟩)⟩
  · rintro ⟨ht, hu⟩
    have hu' : p.2 ⊆ A \ p.1 := Finset.mem_powerset.mp hu
    refine ⟨Finset.mem_product.mpr
      ⟨ht, Finset.mem_powerset.mpr (hu'.trans Finset.sdiff_subset)⟩, ?_⟩
    exact (Finset.disjoint_sdiff (s := p.1) (t := A)).mono_right hu'

/-- The three choices at each point (unused, positive, negative) expand as
disjoint positive and negative supports. -/
theorem prod_one_add_add (A : Finset ℂ) (f g : ℂ → ℂ) :
    (∏ a ∈ A, (1 + f a + g a)) =
      ∑ p ∈ disjointPairs A,
        (∏ a ∈ p.1, f a) * ∏ a ∈ p.2, g a := by
  classical
  suffices h :
      (∏ a ∈ A, (1 + f a + g a)) =
        ∑ t ∈ A.powerset, ∑ u ∈ (A \ t).powerset,
          (∏ a ∈ t, f a) * ∏ a ∈ u, g a by
    exact h.trans (sum_disjointPairs A (fun t u =>
      (∏ a ∈ t, f a) * ∏ a ∈ u, g a)).symm
  conv_lhs =>
    enter [2, a]
    rw [show (1 : ℂ) + f a + g a = f a + (1 + g a) by ring]
  rw [Finset.prod_add]
  apply Finset.sum_congr rfl
  intro t ht
  rw [Finset.prod_one_add]
  rw [Finset.mul_sum]

private theorem char_signed_sum (χ : AddChar ℂ Circle)
    (t u : Finset ℂ) :
    ((χ ((∑ a ∈ t, a) - ∑ a ∈ u, a) : Circle) : ℂ) =
      (∏ a ∈ t, ((χ a : Circle) : ℂ)) *
        ∏ a ∈ u, ((χ (-a) : Circle) : ℂ) := by
  have hsum (s : Finset ℂ) :
      ((χ (∑ a ∈ s, a) : Circle) : ℂ) =
        ∏ a ∈ s, ((χ a : Circle) : ℂ) := by
    induction s using Finset.induction_on with
    | empty => simp
    | @insert a s ha ih =>
        simp only [Finset.sum_insert ha, Finset.prod_insert ha]
        rw [χ.map_add_eq_mul]
        exact congrArg (fun z : ℂ => ((χ a : Circle) : ℂ) * z) ih
  have hneg (s : Finset ℂ) :
      ((χ (-(∑ a ∈ s, a)) : Circle) : ℂ) =
        ∏ a ∈ s, ((χ (-a) : Circle) : ℂ) := by
    induction s using Finset.induction_on with
    | empty => simp
    | @insert a s ha ih =>
        simp only [Finset.sum_insert ha, neg_add_rev, Finset.prod_insert ha]
        rw [add_comm (-∑ a ∈ s, a) (-a), χ.map_add_eq_mul]
        exact congrArg (fun z : ℂ => ((χ (-a) : Circle) : ℂ) * z) ih
  rw [sub_eq_add_neg, χ.map_add_eq_mul]
  exact congrArg₂ (· * ·) (hsum t) (hneg u)

/-- All possibly nonzero frequencies in the Riesz expansion. -/
noncomputable def relationFrequencies (A : Finset ℂ) : Finset ℂ :=
  (disjointPairs A).image fun p =>
    (∑ a ∈ p.1, a) - ∑ a ∈ p.2, a

/-- Exact finite Fourier bridge, before extracting the zero frequency. -/
theorem riesz_product_expansion (A : Finset ℂ) (q : ℂ)
    (χ : AddChar ℂ Circle) :
    (∏ a ∈ A,
      (1 + q * ((χ a : Circle) : ℂ) +
        q * ((χ (-a) : Circle) : ℂ))) =
      ∑ p ∈ disjointPairs A,
        q ^ (p.1.card + p.2.card) *
          ((χ ((∑ a ∈ p.1, a) - ∑ a ∈ p.2, a) : Circle) : ℂ) := by
  rw [prod_one_add_add]
  apply Finset.sum_congr rfl
  intro p hp
  rw [char_signed_sum]
  simp only [Finset.prod_mul_distrib, Finset.prod_const]
  ring

/-- The finite sample annihilates every nonzero signed-relation frequency.
The relation weight is exactly `q` to the support cardinality. -/
theorem riesz_sample_eq_signedRelations (A S : Finset ℂ) (q : ℂ)
    (hS : relationFrequencies A \ {0} ⊆ S) :
    (∑ T ∈ S.powerset,
      ∏ a ∈ A,
        (1 + q * ((sampleChar T a : Circle) : ℂ) +
          q * ((sampleChar T (-a) : Circle) : ℂ))) =
      (2 : ℂ) ^ S.card *
        ∑ p ∈ signedRelations A, q ^ (p.1.card + p.2.card) := by
  classical
  simp_rw [riesz_product_expansion]
  rw [sum_sampleChar_polynomial S (disjointPairs A)
    (fun p => (∑ a ∈ p.1, a) - ∑ a ∈ p.2, a)
    (fun p => q ^ (p.1.card + p.2.card))]
  · congr 1
    have heq :
        (disjointPairs A).filter (fun p =>
          (∑ a ∈ p.1, a) - ∑ a ∈ p.2, a = 0) = signedRelations A := by
      ext p
      simp only [disjointPairs, signedRelations, Finset.mem_filter, sub_eq_zero]
      tauto
    rw [heq]
  · intro p hp
    by_cases hz : (∑ a ∈ p.1, a) - ∑ a ∈ p.2, a = 0
    · exact Or.inl hz
    · right
      apply hS
      simp only [Finset.mem_sdiff, Finset.mem_singleton]
      exact ⟨Finset.mem_image.mpr ⟨p, hp, rfl⟩, hz⟩

/-- Real-variable form of the same finite identity. The factors of the
Riesz product are real, although the finite sum is written in `ℂ`. -/
theorem riesz_sample_real_eq_signedRelations (A S : Finset ℂ) (q : ℝ)
    (hS : relationFrequencies A \ {0} ⊆ S) :
    (∑ T ∈ S.powerset,
      ∏ a ∈ A,
        (1 + ((2 * q * (((sampleChar T a : Circle) : ℂ).re) : ℝ) : ℂ))) =
      (2 : ℂ) ^ S.card *
        ∑ p ∈ signedRelations A, (q : ℂ) ^ (p.1.card + p.2.card) := by
  calc
    _ = ∑ T ∈ S.powerset,
      ∏ a ∈ A,
        (1 + (q : ℂ) * ((sampleChar T a : Circle) : ℂ) +
          (q : ℂ) * ((sampleChar T (-a) : Circle) : ℂ)) := by
      apply Finset.sum_congr rfl
      intro T hT
      apply Finset.prod_congr rfl
      intro a ha
      have hneg : ((sampleChar T (-a) : Circle) : ℂ) =
          conj ((sampleChar T a : Circle) : ℂ) := by
        rw [(sampleChar T).map_neg_eq_inv, Circle.coe_inv_eq_conj]
      rw [hneg]
      have hreal := Complex.add_conj ((sampleChar T a : Circle) : ℂ)
      calc
        _ = 1 + (q : ℂ) *
            (((sampleChar T a : Circle) : ℂ) +
              conj ((sampleChar T a : Circle) : ℂ)) := by
                rw [hreal]
                push_cast
                ring
        _ = _ := by ring
    _ = _ := riesz_sample_eq_signedRelations A S (q : ℂ) hS

/-- The same identity entirely in `ℝ`, ready for upper bounds on a
nonnegative finite Riesz product. -/
theorem riesz_sample_real (A S : Finset ℂ) (q : ℝ)
    (hS : relationFrequencies A \ {0} ⊆ S) :
    (∑ T ∈ S.powerset,
      ∏ a ∈ A,
        (1 + 2 * q * (((sampleChar T a : Circle) : ℂ).re))) =
      (2 : ℝ) ^ S.card *
        ∑ p ∈ signedRelations A, q ^ (p.1.card + p.2.card) := by
  have h := riesz_sample_real_eq_signedRelations A S q hS
  exact_mod_cast h

/-- The normalized finite average of the Riesz product is precisely the
weighted signed-relation enumerator. -/
theorem riesz_sample_average (A S : Finset ℂ) (q : ℝ)
    (hS : relationFrequencies A \ {0} ⊆ S) :
    ((2 : ℝ) ^ S.card)⁻¹ *
      (∑ T ∈ S.powerset,
        ∏ a ∈ A,
          (1 + 2 * q * (((sampleChar T a : Circle) : ℂ).re))) =
      ∑ p ∈ signedRelations A, q ^ (p.1.card + p.2.card) := by
  rw [riesz_sample_real A S q hS]
  have htwo : (2 : ℝ) ^ S.card ≠ 0 := pow_ne_zero _ (by norm_num)
  simp [htwo]

end Erdos.Research.FiniteRieszRelation

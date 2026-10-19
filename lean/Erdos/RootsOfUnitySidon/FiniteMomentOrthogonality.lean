import Erdos.RootsOfUnitySidon.FiniteOrthogonalCharacters

/-!
# Exact finite sampling of even moments

Finite character samples reproduce the zero-frequency terms in every even
moment of a finite trigonometric polynomial. In particular, multiplying the
frequencies by any algebraic character leaves the sampled moment unchanged.
-/

namespace Erdos.Research.FiniteMomentOrthogonality

open Erdos.Research.FiniteOrthogonalCharacters
open Complex
open scoped ComplexConjugate

noncomputable def tupleSet (A : Finset ℂ) (m : ℕ) : Finset (Fin m → ℂ) :=
  Fintype.piFinset (fun _ : Fin m => A)

noncomputable def signedFrequency {m : ℕ} (p q : Fin m → ℂ) : ℂ :=
  (∑ i, p i) - ∑ i, q i

noncomputable def momentFrequencies (A : Finset ℂ) (m : ℕ) : Finset ℂ :=
  ((tupleSet A m ×ˢ tupleSet A m).image
    (fun pq => signedFrequency pq.1 pq.2)) \ {0}

theorem signedFrequency_mem_or_zero (A : Finset ℂ) (m : ℕ)
    {p q : Fin m → ℂ} (hp : p ∈ tupleSet A m) (hq : q ∈ tupleSet A m) :
    signedFrequency p q = 0 ∨ signedFrequency p q ∈ momentFrequencies A m := by
  classical
  by_cases hzero : signedFrequency p q = 0
  · exact Or.inl hzero
  · right
    simp only [momentFrequencies, Finset.mem_sdiff, Finset.mem_singleton]
    exact ⟨Finset.mem_image.mpr ⟨(p, q), Finset.mem_product.mpr ⟨hp, hq⟩, rfl⟩, hzero⟩

private theorem circleChar_prod (χ : AddChar ℂ Circle) {m : ℕ} (p : Fin m → ℂ) :
    (∏ i, ((χ (p i) : Circle) : ℂ)) = ((χ (∑ i, p i) : Circle) : ℂ) := by
  have h := map_sum χ.toAddMonoidHom p (Finset.univ : Finset (Fin m))
  have h' : (∏ i, χ (p i)) = χ (∑ i, p i) := by
    exact congrArg Additive.toMul h.symm
  change (∏ i, Circle.coeHom (χ (p i))) = Circle.coeHom (χ (∑ i, p i))
  rw [← map_prod]
  exact congrArg Circle.coeHom h'

private theorem circleChar_conj (χ : AddChar ℂ Circle) (z : ℂ) :
    star ((χ z : Circle) : ℂ) = ((χ (-z) : Circle) : ℂ) := by
  change conj ((χ z : Circle) : ℂ) = ((χ (-z) : Circle) : ℂ)
  rw [χ.map_neg_eq_inv]
  exact (Circle.coe_inv_eq_conj (χ z)).symm

noncomputable def trigPoly (A : Finset ℂ) (c : ℂ → ℂ)
    (χ : AddChar ℂ Circle) : ℂ :=
  ∑ a ∈ A, c a * ((χ a : Circle) : ℂ)

noncomputable def tupleCoeff {m : ℕ} (c : ℂ → ℂ) (p : Fin m → ℂ) : ℂ :=
  ∏ i, c (p i)

private theorem trigPoly_pow (A : Finset ℂ) (c : ℂ → ℂ)
    (χ : AddChar ℂ Circle) (m : ℕ) :
    (trigPoly A c χ) ^ m =
      ∑ p ∈ tupleSet A m,
        tupleCoeff c p * ((χ (∑ i, p i) : Circle) : ℂ) := by
  classical
  rw [trigPoly, Finset.sum_pow']
  unfold tupleSet
  apply Finset.sum_congr rfl
  intro p hp
  change (∏ i, c (p i) * Circle.coeHom (χ (p i))) =
    tupleCoeff c p * Circle.coeHom (χ (∑ i, p i))
  rw [Finset.prod_mul_distrib]
  change (∏ i, c (p i)) * (∏ i, ((χ (p i) : Circle) : ℂ)) =
    tupleCoeff c p * ((χ (∑ i, p i) : Circle) : ℂ)
  rw [circleChar_prod]
  rfl

private theorem trigPoly_star_pow (A : Finset ℂ) (c : ℂ → ℂ)
    (χ : AddChar ℂ Circle) (m : ℕ) :
    star ((trigPoly A c χ) ^ m) =
      ∑ p ∈ tupleSet A m,
        (star (tupleCoeff c p)) * ((χ (-(∑ i, p i)) : Circle) : ℂ) := by
  rw [trigPoly_pow]
  simp only [star_sum, star_mul, circleChar_conj]
  congr 1
  funext p
  ring

noncomputable def momentCoeff {m : ℕ} (c : ℂ → ℂ)
    (p q : Fin m → ℂ) : ℂ := tupleCoeff c p * star (tupleCoeff c q)

private theorem circleChar_signed (χ : AddChar ℂ Circle) {m : ℕ}
    (p q : Fin m → ℂ) :
    ((χ (∑ i, p i) : Circle) : ℂ) *
      ((χ (-(∑ i, q i)) : Circle) : ℂ) =
        ((χ (signedFrequency p q) : Circle) : ℂ) := by
  change Circle.coeHom (χ (∑ i, p i)) *
      Circle.coeHom (χ (-(∑ i, q i))) =
    Circle.coeHom (χ (signedFrequency p q))
  rw [← map_mul, ← χ.map_add_eq_mul]
  rfl

theorem trigPoly_moment_expansion (A : Finset ℂ) (c : ℂ → ℂ)
    (χ : AddChar ℂ Circle) (m : ℕ) :
    (trigPoly A c χ)^m * star ((trigPoly A c χ)^m) =
      ∑ pq ∈ tupleSet A m ×ˢ tupleSet A m,
        momentCoeff c pq.1 pq.2 *
          ((χ (signedFrequency pq.1 pq.2) : Circle) : ℂ) := by
  classical
  rw [trigPoly_star_pow, trigPoly_pow, Finset.sum_mul_sum]
  rw [Finset.sum_product]
  apply Finset.sum_congr rfl
  intro p hp
  apply Finset.sum_congr rfl
  intro q hq
  change (tupleCoeff c p * ((χ (∑ i, p i) : Circle) : ℂ)) *
      (star (tupleCoeff c q) * ((χ (-(∑ i, q i)) : Circle) : ℂ)) =
    momentCoeff c p q * ((χ (signedFrequency p q) : Circle) : ℂ)
  rw [momentCoeff, ← circleChar_signed]
  ring

/-- Every nonzero signed frequency in a degree-`2m` moment is annihilated by
the finite sample. The remaining terms are independent of the extra character
`ψ`. -/
theorem sampled_moment_eq_zero_frequency_superset (A : Finset ℂ) (c : ℂ → ℂ)
    (ψ : AddChar ℂ Circle) (m : ℕ) (S : Finset ℂ)
    (hS : momentFrequencies A m ⊆ S) :
    (∑ T ∈ S.powerset,
      (trigPoly A c (sampleChar T * ψ))^m *
        star ((trigPoly A c (sampleChar T * ψ))^m)) =
      (2 : ℂ) ^ S.card *
        ∑ pq ∈ (tupleSet A m ×ˢ tupleSet A m).filter
            (fun pq => signedFrequency pq.1 pq.2 = 0),
          momentCoeff c pq.1 pq.2 := by
  classical
  let F := tupleSet A m ×ˢ tupleSet A m
  have hfreq : ∀ pq ∈ F,
      signedFrequency pq.1 pq.2 = 0 ∨ signedFrequency pq.1 pq.2 ∈ S := by
    intro pq hpq
    rcases Finset.mem_product.mp hpq with ⟨hp, hq⟩
    exact (signedFrequency_mem_or_zero A m hp hq).imp_right (fun h => hS h)
  calc
    (∑ T ∈ S.powerset,
      (trigPoly A c (sampleChar T * ψ))^m *
        star ((trigPoly A c (sampleChar T * ψ))^m)) =
      ∑ T ∈ S.powerset,
        ∑ pq ∈ F,
          (momentCoeff c pq.1 pq.2 *
            ((ψ (signedFrequency pq.1 pq.2) : Circle) : ℂ)) *
            ((sampleChar T (signedFrequency pq.1 pq.2) : Circle) : ℂ) := by
          apply Finset.sum_congr rfl
          intro T hT
          rw [trigPoly_moment_expansion]
          apply Finset.sum_congr rfl
          intro pq hpq
          change momentCoeff c pq.1 pq.2 *
              Circle.coeHom ((sampleChar T * ψ) (signedFrequency pq.1 pq.2)) =
            (momentCoeff c pq.1 pq.2 *
              Circle.coeHom (ψ (signedFrequency pq.1 pq.2))) *
              Circle.coeHom (sampleChar T (signedFrequency pq.1 pq.2))
          rw [AddChar.mul_apply, map_mul]
          ring
    _ = (2 : ℂ) ^ S.card *
        ∑ pq ∈ F.filter (fun pq => signedFrequency pq.1 pq.2 = 0),
          momentCoeff c pq.1 pq.2 *
            ((ψ (signedFrequency pq.1 pq.2) : Circle) : ℂ) :=
          sum_sampleChar_polynomial S F
            (fun pq => signedFrequency pq.1 pq.2)
            (fun pq => momentCoeff c pq.1 pq.2 *
              ((ψ (signedFrequency pq.1 pq.2) : Circle) : ℂ)) hfreq
    _ = (2 : ℂ) ^ S.card *
        ∑ pq ∈ F.filter (fun pq => signedFrequency pq.1 pq.2 = 0),
          momentCoeff c pq.1 pq.2 := by
          congr 1
          apply Finset.sum_congr rfl
          intro pq hpq
          have hzero : signedFrequency pq.1 pq.2 = 0 :=
            (Finset.mem_filter.mp hpq).2
          simp [hzero]

theorem sampled_moment_eq_zero_frequency (A : Finset ℂ) (c : ℂ → ℂ)
    (ψ : AddChar ℂ Circle) (m : ℕ) :
    (∑ T ∈ (momentFrequencies A m).powerset,
      (trigPoly A c (sampleChar T * ψ))^m *
        star ((trigPoly A c (sampleChar T * ψ))^m)) =
      (2 : ℂ) ^ (momentFrequencies A m).card *
        ∑ pq ∈ (tupleSet A m ×ˢ tupleSet A m).filter
            (fun pq => signedFrequency pq.1 pq.2 = 0),
          momentCoeff c pq.1 pq.2 :=
  sampled_moment_eq_zero_frequency_superset A c ψ m
    (momentFrequencies A m) (Finset.Subset.rfl)

theorem sampled_complex_moment_invariant_superset (A : Finset ℂ) (c : ℂ → ℂ)
    (ψ : AddChar ℂ Circle) (m : ℕ) (S : Finset ℂ)
    (hS : momentFrequencies A m ⊆ S) :
    (∑ T ∈ S.powerset,
      (trigPoly A c (sampleChar T * ψ))^m *
        star ((trigPoly A c (sampleChar T * ψ))^m)) =
    ∑ T ∈ S.powerset,
      (trigPoly A c (sampleChar T))^m *
        star ((trigPoly A c (sampleChar T))^m) := by
  rw [sampled_moment_eq_zero_frequency_superset A c ψ m S hS,
      ← sampled_moment_eq_zero_frequency_superset A c
        (1 : AddChar ℂ Circle) m S hS]
  simp

theorem sampled_complex_moment_invariant (A : Finset ℂ) (c : ℂ → ℂ)
    (ψ : AddChar ℂ Circle) (m : ℕ) :
    (∑ T ∈ (momentFrequencies A m).powerset,
      (trigPoly A c (sampleChar T * ψ))^m *
        star ((trigPoly A c (sampleChar T * ψ))^m)) =
    ∑ T ∈ (momentFrequencies A m).powerset,
      (trigPoly A c (sampleChar T))^m *
        star ((trigPoly A c (sampleChar T))^m) :=
  sampled_complex_moment_invariant_superset A c ψ m
    (momentFrequencies A m) (Finset.Subset.rfl)

private theorem norm_even_pow_eq_complex_moment (z : ℂ) (m : ℕ) :
    ((‖z‖ ^ (2 * m) : ℝ) : ℂ) = z^m * star (z^m) := by
  rw [pow_mul, ← Complex.normSq_eq_norm_sq]
  push_cast
  change ((Complex.normSq z : ℝ) : ℂ) ^ m = z^m * conj (z^m)
  rw [← Complex.mul_conj, mul_pow, map_pow]

private theorem norm_even_pow_cast (z : ℂ) (m : ℕ) :
    (((‖z‖ : ℝ) : ℂ) ^ (2 * m)) = z^m * star (z^m) := by
  rw [← Complex.ofReal_pow]
  exact norm_even_pow_eq_complex_moment z m

/-- Twisting any finite trigonometric polynomial by an algebraic character
preserves its exactly sampled even moment. The finite sample depends only on
the frequency set `A` and exponent `m`, not on coefficients or the twist. -/
theorem sampled_even_moment_invariant_superset (A : Finset ℂ) (c : ℂ → ℂ)
    (ψ : AddChar ℂ Circle) (m : ℕ) (S : Finset ℂ)
    (hS : momentFrequencies A m ⊆ S) :
    (∑ T ∈ S.powerset,
      ‖∑ a ∈ A,
          c a * ((sampleChar T a : Circle) : ℂ) * ((ψ a : Circle) : ℂ)‖ ^ (2 * m)) =
    ∑ T ∈ S.powerset,
      ‖∑ a ∈ A, c a * ((sampleChar T a : Circle) : ℂ)‖ ^ (2 * m) := by
  classical
  have htwist (T : Finset ℂ) :
      trigPoly A c (sampleChar T * ψ) =
        ∑ a ∈ A,
          c a * ((sampleChar T a : Circle) : ℂ) * ((ψ a : Circle) : ℂ) := by
    unfold trigPoly
    apply Finset.sum_congr rfl
    intro a ha
    change c a * Circle.coeHom ((sampleChar T * ψ) a) =
      c a * Circle.coeHom (sampleChar T a) * Circle.coeHom (ψ a)
    rw [AddChar.mul_apply, map_mul]
    ring
  apply Complex.ofReal_injective
  push_cast
  calc
    _ = ∑ T ∈ S.powerset,
        (trigPoly A c (sampleChar T * ψ))^m *
          star ((trigPoly A c (sampleChar T * ψ))^m) := by
            apply Finset.sum_congr rfl
            intro T hT
            exact (norm_even_pow_cast _ m).trans
              (congrArg (fun z : ℂ => z^m * star (z^m)) (htwist T).symm)
    _ = ∑ T ∈ S.powerset,
        (trigPoly A c (sampleChar T))^m *
          star ((trigPoly A c (sampleChar T))^m) :=
            sampled_complex_moment_invariant_superset A c ψ m S hS
    _ = _ := by
      apply Finset.sum_congr rfl
      intro T hT
      exact (norm_even_pow_cast _ m).symm

theorem sampled_even_moment_invariant (A : Finset ℂ) (c : ℂ → ℂ)
    (ψ : AddChar ℂ Circle) (m : ℕ) :
    (∑ T ∈ (momentFrequencies A m).powerset,
      ‖∑ a ∈ A,
          c a * ((sampleChar T a : Circle) : ℂ) * ((ψ a : Circle) : ℂ)‖ ^ (2 * m)) =
    ∑ T ∈ (momentFrequencies A m).powerset,
      ‖∑ a ∈ A, c a * ((sampleChar T a : Circle) : ℂ)‖ ^ (2 * m) :=
  sampled_even_moment_invariant_superset A c ψ m
    (momentFrequencies A m) (Finset.Subset.rfl)

end Erdos.Research.FiniteMomentOrthogonality

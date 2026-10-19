import Erdos.RootsOfUnitySidon.PisierRelationCounting
import Mathlib.Tactic

/-!
# Weighted relation supports and signed relations

The Riesz expansion counts signed relations. The thinning argument counts
their supports. Choosing one signed relation for each support compares the
two weighted sums without a loss in the constant.
-/

namespace Erdos.Research.PisierWeightedRelationBridge

open scoped BigOperators
open Classical
open Erdos.Research.PisierRelationCounting

theorem weighted_supports_le_signed (A : Finset ℂ) (q : ℝ) (hq : 0 ≤ q) :
    (∑ R ∈ A.powerset.filter AddRelationSupport, q ^ R.card) ≤
      ∑ p ∈ signedRelations A, q ^ (p.1.card + p.2.card) := by
  classical
  let supports := A.powerset.filter AddRelationSupport
  have hchoose (R : supports) :
      ∃ p : Finset ℂ × Finset ℂ,
        p ∈ signedRelations A ∧ p.1 ∪ p.2 = R.1 := by
    have hR := R.2
    simp only [supports, Finset.mem_filter, Finset.mem_powerset] at hR
    obtain ⟨t, u, htu, htuR, hsum⟩ := hR.2
    have htA : t ⊆ A :=
      ((Finset.subset_union_left.trans_eq htuR).trans hR.1)
    have huA : u ⊆ A :=
      ((Finset.subset_union_right.trans_eq htuR).trans hR.1)
    exact ⟨(t,u), Finset.mem_filter.mpr
      ⟨Finset.mem_product.mpr
        ⟨Finset.mem_powerset.mpr htA, Finset.mem_powerset.mpr huA⟩,
        ⟨htu, hsum⟩⟩, htuR⟩
  let f (R : supports) : Finset ℂ × Finset ℂ := (hchoose R).choose
  have hf (R : supports) := (hchoose R).choose_spec
  have hinj : Function.Injective f := by
    intro R T h
    apply Subtype.ext
    calc
      R.1 = (f R).1 ∪ (f R).2 := (hf R).2.symm
      _ = (f T).1 ∪ (f T).2 := by rw [h]
      _ = T.1 := (hf T).2
  have hcard (R : supports) : (f R).1.card + (f R).2.card = R.1.card := by
    have hdisj := (Finset.mem_filter.mp (hf R).1).2.1
    rw [← (hf R).2, Finset.card_union_of_disjoint hdisj]
  have hsum :
      (∑ R : supports, q ^ R.1.card) =
        ∑ p ∈ supports.attach.image f, q ^ (p.1.card + p.2.card) := by
    rw [Finset.sum_image]
    · apply Finset.sum_congr rfl
      intro R hR
      exact congrArg (q ^ ·) (hcard R).symm
    · intro R hR T hT heq
      exact hinj heq
  have hsum' :
      (∑ R ∈ supports, q ^ R.card) =
        ∑ p ∈ supports.attach.image f, q ^ (p.1.card + p.2.card) := by
    calc
      _ = ∑ R ∈ supports.attach, q ^ R.1.card :=
        (Finset.sum_attach supports (fun R => q ^ R.card)).symm
      _ = _ := by simpa only [Finset.attach_eq_univ] using hsum
  change (∑ R ∈ supports, q ^ R.card) ≤ _
  rw [hsum']
  apply Finset.sum_le_sum_of_subset_of_nonneg
  · intro p hp
    obtain ⟨R, _, rfl⟩ := Finset.mem_image.mp hp
    exact (hf R).1
  · intro p hp hnot
    exact pow_nonneg hq _

private theorem nat_weight_eq (n m r : ℕ) (hn : 0 < n) (hr : r ≤ n) :
    ((2 * m) ^ r * n ^ (n - r) : ℕ) =
      (n : ℝ) ^ n * (((2 * m : ℕ) : ℝ) / n) ^ r := by
  have hnR : (n : ℝ) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt hn)
  have hsplit : n - r + r = n := Nat.sub_add_cancel hr
  norm_num only [Nat.cast_mul, Nat.cast_pow]
  rw [div_pow]
  field_simp
  calc
    (2 * (m : ℝ)) ^ r * (n : ℝ) ^ (n - r) * (n : ℝ) ^ r =
        (2 * (m : ℝ)) ^ r * ((n : ℝ) ^ (n - r) * (n : ℝ) ^ r) := by ring
    _ = (2 * (m : ℝ)) ^ r * (n : ℝ) ^ n := by rw [← pow_add, hsplit]

/-- A normalized signed-relation estimate gives the exact integer-weighted
estimate used by the fixed-cardinality thinning theorem. -/
theorem weighted_relation_bound_of_signed_bound
    (A : Finset ℂ) (m K : ℕ) (hn : 0 < A.card)
    (hbound :
      (∑ p ∈ signedRelations A,
        (((2 * m : ℕ) : ℝ) / A.card) ^ (p.1.card + p.2.card)) ≤ K) :
    (∑ R ∈ A.powerset.filter AddRelationSupport,
        (2 * m) ^ R.card * A.card ^ (A.card - R.card)) ≤
      K * A.card ^ A.card := by
  classical
  let q : ℝ := ((2 * m : ℕ) : ℝ) / A.card
  have hq : 0 ≤ q := div_nonneg (by positivity) (by positivity)
  have hsupport := weighted_supports_le_signed A q hq
  have hsum :
      ((∑ R ∈ A.powerset.filter AddRelationSupport,
        (2 * m) ^ R.card * A.card ^ (A.card - R.card) : ℕ) : ℝ) =
      (A.card : ℝ) ^ A.card *
        ∑ R ∈ A.powerset.filter AddRelationSupport, q ^ R.card := by
    push_cast
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro R hR
    have hr : R.card ≤ A.card := Finset.card_le_card
      (Finset.mem_powerset.mp (Finset.mem_filter.mp hR).1)
    simpa [q, Nat.cast_mul, Nat.cast_pow] using
      nat_weight_eq A.card m R.card hn hr
  have hnnonneg : 0 ≤ (A.card : ℝ) ^ A.card := by positivity
  have hreal :
      ((∑ R ∈ A.powerset.filter AddRelationSupport,
        (2 * m) ^ R.card * A.card ^ (A.card - R.card) : ℕ) : ℝ) ≤
        ((K * A.card ^ A.card : ℕ) : ℝ) := by
    rw [hsum]
    push_cast
    calc
      (A.card : ℝ) ^ A.card *
        ∑ R ∈ A.powerset.filter AddRelationSupport, q ^ R.card ≤
        (A.card : ℝ) ^ A.card *
        ∑ p ∈ signedRelations A, q ^ (p.1.card + p.2.card) :=
          mul_le_mul_of_nonneg_left hsupport hnnonneg
      _ ≤ (A.card : ℝ) ^ A.card * K :=
        mul_le_mul_of_nonneg_left (by simpa only [q] using hbound) hnnonneg
      _ = K * (A.card : ℝ) ^ A.card := by ring
  exact_mod_cast hreal

end Erdos.Research.PisierWeightedRelationBridge

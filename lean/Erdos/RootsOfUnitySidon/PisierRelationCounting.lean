import Mathlib.Combinatorics.Additive.Dissociation
import Mathlib.Data.Finset.Card
import Mathlib.Analysis.SpecialFunctions.Complex.CircleAddChar
import Mathlib.Data.Nat.Choose.Sum

/-!
# A finite relation-count extraction lemma

The combinatorial part of Pisier's proportional quasi-independence argument can
be separated from its harmonic analysis. A relation support is a subset carrying
a nontrivial relation. Its support predicate is closed under disjoint union.
If the total number of relation supports times the number of small subsets is
less than the total number of subsets, some subset has a large relation-free
complement.

The proof counts **all** subsets rather than only half-sized subsets: assign
to each subset a maximal relation support and its complement. This gives an
injection into relation supports times small subsets if every complement is
small.
-/

namespace Erdos.Research.PisierRelationCounting

variable {α : Type*} [DecidableEq α]

/-- A counting criterion for extracting a large subset with no nonempty
relation support. The only algebraic property used is closure of relation
supports under disjoint union. -/
theorem exists_large_relation_free (A : Finset α) (Rel : Finset α → Prop)
    [DecidablePred Rel]
    (h_empty : Rel ∅)
    (h_union : ∀ {M N : Finset α}, Disjoint M N → Rel M → Rel N → Rel (M ∪ N))
    (d : ℕ)
    (h_count :
      (A.powerset.filter Rel).card *
        (A.powerset.filter fun B => B.card < d).card < 2 ^ A.card) :
    ∃ B : Finset α, B ⊆ A ∧ d ≤ B.card ∧
      ∀ C : Finset α, C ⊆ B → C.Nonempty → ¬ Rel C := by
  classical
  have hmax (H : Finset α) :
      ∃ M : Finset α, M ⊆ H ∧ Rel M ∧
        ∀ N : Finset α, M ⊂ N → N ⊆ H → ¬ Rel N := by
    obtain ⟨M, hM⟩ :=
      (H.powerset.filter Rel).exists_maximal
        ⟨∅, Finset.mem_filter.mpr ⟨Finset.empty_mem_powerset _, h_empty⟩⟩
    simp only [Finset.mem_filter, Finset.mem_powerset] at hM
    exact ⟨M, hM.1.1, hM.1.2, fun N hMN hNH hRN =>
      hM.not_gt ⟨hNH, hRN⟩ hMN⟩
  let M (H : Finset α) : Finset α := (hmax H).choose
  have hM (H : Finset α) := (hmax H).choose_spec
  let B (H : Finset α) : Finset α := H \ M H
  have hBfree (H : Finset α) :
      ∀ C : Finset α, C ⊆ B H → C.Nonempty → ¬ Rel C := by
    intro C hCB hC hRC
    have hdisj : Disjoint (M H) C :=
      Finset.disjoint_sdiff.mono_right hCB
    have hproper : M H ⊂ M H ∪ C := by
      apply Finset.ssubset_iff_subset_ne.mpr
      refine ⟨Finset.subset_union_left, ?_⟩
      intro heq
      obtain ⟨c, hc⟩ := hC
      have hcM : c ∈ M H := heq ▸ Finset.mem_union_right _ hc
      exact (Finset.disjoint_left.mp hdisj hcM) hc
    exact (hM H).2.2 (M H ∪ C) hproper
      (Finset.union_subset (hM H).1 (hCB.trans Finset.sdiff_subset))
      (h_union hdisj (hM H).2.1 hRC)
  by_contra hnone
  have hsmall (H : Finset α) (hHA : H ⊆ A) : (B H).card < d := by
    by_contra hnot
    exact hnone ⟨B H, Finset.sdiff_subset.trans hHA,
      Nat.le_of_not_gt hnot, hBfree H⟩
  have hmap : Set.MapsTo
      (fun H : Finset α => (M H, B H))
      (↑A.powerset : Set (Finset α))
      (↑((A.powerset.filter Rel).product
        (A.powerset.filter fun B => B.card < d)) :
        Set (Finset α × Finset α)) := by
    intro H hHA
    have hHA' : H ⊆ A := Finset.mem_powerset.mp hHA
    exact Finset.mem_product.mpr
      ⟨Finset.mem_filter.mpr
          ⟨Finset.mem_powerset.mpr ((hM H).1.trans hHA'), (hM H).2.1⟩,
       Finset.mem_filter.mpr
          ⟨Finset.mem_powerset.mpr (Finset.sdiff_subset.trans hHA'),
            hsmall H hHA'⟩⟩
  have hinj :
      (↑A.powerset : Set (Finset α)).InjOn
        (fun H : Finset α => (M H, B H)) := by
    intro H _ J _ hpair
    have hMJ : M H = M J := congrArg Prod.fst hpair
    have hBJ : B H = B J := congrArg Prod.snd hpair
    calc
      H = M H ∪ B H := (Finset.union_sdiff_of_subset (hM H).1).symm
      _ = M J ∪ B J := by rw [hMJ, hBJ]
      _ = J := Finset.union_sdiff_of_subset (hM J).1
  have hcard := Finset.card_le_card_of_injOn
    (fun H : Finset α => (M H, B H)) hmap hinj
  rw [Finset.card_powerset, Finset.product_eq_sprod, Finset.card_product] at hcard
  exact (Nat.not_le.mpr h_count) hcard

end Erdos.Research.PisierRelationCounting

namespace Erdos.Research.PisierRelationCounting

open scoped BigOperators
open Classical

/-- The exact support of a signed {-1,0,1} additive relation. The empty
support is allowed and represents the trivial relation. -/
def AddRelationSupport (M : Finset ℂ) : Prop :=
  ∃ t u : Finset ℂ, Disjoint t u ∧ t ∪ u = M ∧
    (∑ z ∈ t, z) = ∑ z ∈ u, z

/-- Signed {-1,0,1} relations on `A`, represented by disjoint positive
and negative supports. This is the quantity counted by the Riesz-product
expansion. -/
noncomputable def signedRelations (A : Finset ℂ) : Finset (Finset ℂ × Finset ℂ) :=
  (A.powerset.product A.powerset).filter fun p =>
    Disjoint p.1 p.2 ∧ (∑ z ∈ p.1, z) = ∑ z ∈ p.2, z

/-- Every relation support has a signed relation witness, so support count
is bounded by the signed relation count. -/
theorem card_relation_supports_le_signedRelations (A : Finset ℂ) :
    (A.powerset.filter AddRelationSupport).card ≤
      (signedRelations A).card := by
  classical
  have himage : A.powerset.filter AddRelationSupport ⊆
      (signedRelations A).image (fun p => p.1 ∪ p.2) := by
    intro M hM
    obtain ⟨t, u, htu, htuM, hsum⟩ :=
      (Finset.mem_filter.mp hM).2
    have hMA : M ⊆ A := Finset.mem_powerset.mp (Finset.mem_filter.mp hM).1
    have htA : t ⊆ A :=
      ((Finset.subset_union_left.trans_eq htuM).trans hMA)
    have huA : u ⊆ A :=
      ((Finset.subset_union_right.trans_eq htuM).trans hMA)
    exact Finset.mem_image.mpr
      ⟨(t, u), Finset.mem_filter.mpr
        ⟨Finset.mem_product.mpr
          ⟨Finset.mem_powerset.mpr htA, Finset.mem_powerset.mpr huA⟩,
         ⟨htu, hsum⟩⟩, htuM⟩
  exact (Finset.card_le_card himage).trans Finset.card_image_le

theorem addRelationSupport_empty : AddRelationSupport (∅ : Finset ℂ) := by
  refine ⟨∅, ∅, ?_, ?_, ?_⟩ <;> simp

theorem addRelationSupport_union {M N : Finset ℂ}
    (hMN : Disjoint M N)
    (hM : AddRelationSupport M) (hN : AddRelationSupport N) :
    AddRelationSupport (M ∪ N) := by
  classical
  obtain ⟨t₁, u₁, h₁, h₁eq, h₁sum⟩ := hM
  obtain ⟨t₂, u₂, h₂, h₂eq, h₂sum⟩ := hN
  have ht₁M : t₁ ⊆ M := by rw [← h₁eq]; exact Finset.subset_union_left
  have hu₁M : u₁ ⊆ M := by rw [← h₁eq]; exact Finset.subset_union_right
  have ht₂N : t₂ ⊆ N := by rw [← h₂eq]; exact Finset.subset_union_left
  have hu₂N : u₂ ⊆ N := by rw [← h₂eq]; exact Finset.subset_union_right
  have htt : Disjoint t₁ t₂ := hMN.mono ht₁M ht₂N
  have htu : Disjoint t₁ u₂ := hMN.mono ht₁M hu₂N
  have hut : Disjoint u₁ t₂ := hMN.mono hu₁M ht₂N
  have huu : Disjoint u₁ u₂ := hMN.mono hu₁M hu₂N
  refine ⟨t₁ ∪ t₂, u₁ ∪ u₂, ?_, ?_, ?_⟩
  · exact Finset.disjoint_union_right.mpr
      ⟨Finset.disjoint_union_left.mpr ⟨h₁, hut.symm⟩,
       Finset.disjoint_union_left.mpr ⟨htu, h₂⟩⟩
  · calc
      (t₁ ∪ t₂) ∪ (u₁ ∪ u₂) = (t₁ ∪ u₁) ∪ (t₂ ∪ u₂) := by ext z; simp [or_left_comm]
      _ = M ∪ N := by rw [h₁eq, h₂eq]
  · simp only [Finset.sum_union htt, Finset.sum_union huu]
    rw [h₁sum, h₂sum]

/-- A finset is dissociated exactly when it has no nonempty relation
support. -/
theorem addDissociated_iff_no_nonempty_relation (B : Finset ℂ) :
    AddDissociated (↑B : Set ℂ) ↔
      ∀ C : Finset ℂ, C ⊆ B → C.Nonempty → ¬ AddRelationSupport C := by
  classical
  constructor
  · intro hB C hCB hC ⟨t, u, htu, htuC, hsum⟩
    have htB : (↑t : Set ℂ) ⊆ (↑B : Set ℂ) := by
      exact Finset.coe_subset.mpr ((Finset.subset_union_left.trans_eq htuC).trans hCB)
    have huB : (↑u : Set ℂ) ⊆ (↑B : Set ℂ) := by
      exact Finset.coe_subset.mpr ((Finset.subset_union_right.trans_eq htuC).trans hCB)
    have htne : t ≠ u := by
      intro heq
      have hte : t = ∅ := by simpa [heq] using htu
      have hCe : C = ∅ := by simpa [hte, ← heq] using htuC.symm
      exact (Finset.nonempty_iff_ne_empty.mp hC) hCe
    exact (not_addDissociated_iff_exists_disjoint.mpr
      ⟨t, u, htB, huB, htu, htne, hsum⟩) hB
  · intro hfree
    by_contra hB
    obtain ⟨t, u, htB, huB, htu, htne, hsum⟩ :=
      not_addDissociated_iff_exists_disjoint.mp hB
    have htB' : t ⊆ B := Finset.coe_subset.mp htB
    have huB' : u ⊆ B := Finset.coe_subset.mp huB
    have hC : (t ∪ u).Nonempty := by
      apply Finset.nonempty_iff_ne_empty.mpr
      intro hEmpty
      have htEmpty : t = ∅ := Finset.subset_empty.mp
        (Finset.subset_union_left.trans_eq hEmpty)
      have huEmpty : u = ∅ := Finset.subset_empty.mp
        (Finset.subset_union_right.trans_eq hEmpty)
      exact htne (htEmpty.trans huEmpty.symm)
    exact hfree (t ∪ u) (Finset.union_subset htB' huB') hC
      ⟨t, u, htu, rfl, hsum⟩

/-- The exact finite relation-count criterion specialized to additive
dissociation. It does not assume a Sidon inequality; that inequality is used
only upstream to bound the number of relation supports. -/
theorem exists_dissociated_of_relation_count (A : Finset ℂ) (d : ℕ)
    (h_count :
      (A.powerset.filter AddRelationSupport).card *
        (A.powerset.filter fun B => B.card < d).card < 2 ^ A.card) :
    ∃ B : Finset ℂ, B ⊆ A ∧ d ≤ B.card ∧
      AddDissociated (↑B : Set ℂ) := by
  obtain ⟨B, hBA, hcard, hfree⟩ :=
    exists_large_relation_free A AddRelationSupport
      addRelationSupport_empty
      (fun hMN hM hN => addRelationSupport_union hMN hM hN)
      d h_count
  exact ⟨B, hBA, hcard,
    (addDissociated_iff_no_nonempty_relation B).2 hfree⟩

/-- A binomial identity tailored to counting subsets with small cardinality. -/
theorem sum_powerset_four_pow_compl {α : Type*} [DecidableEq α]
    (A : Finset α) :
    (∑ B ∈ A.powerset, 4 ^ (A.card - B.card)) = 5 ^ A.card := by
  rw [Finset.sum_powerset_apply_card (f := fun k : ℕ => 4 ^ (A.card - k))]
  conv_rhs => rw [← show (1 + 4 : ℕ) = 5 by norm_num, add_pow]
  apply Finset.sum_congr rfl
  intro k hk
  simp only [nsmul_eq_mul, one_pow, one_mul]
  ac_rfl

/-- The number of subsets of size below `d`, multiplied by a simple
weight, is bounded by the binomial sum. This is the elementary counting
input for turning an exponential relation bound into proportional
dissociation. -/
theorem small_subset_count_weighted {α : Type*} [DecidableEq α]
    (A : Finset α) (d : ℕ) :
    (A.powerset.filter fun B => B.card < d).card * 4 ^ (A.card - d) ≤
      5 ^ A.card := by
  classical
  have hterm : ∀ B ∈ A.powerset.filter (fun B => B.card < d),
      4 ^ (A.card - d) ≤ 4 ^ (A.card - B.card) := by
    intro B hB
    have hBd : B.card ≤ d := Nat.le_of_lt (Finset.mem_filter.mp hB).2
    exact pow_le_pow_right₀ (by omega : (1 : ℕ) ≤ 4)
      (Nat.sub_le_sub_left hBd A.card)
  calc
    _ = ∑ B ∈ A.powerset.filter (fun B => B.card < d),
          4 ^ (A.card - d) := by simp
    _ ≤ ∑ B ∈ A.powerset.filter (fun B => B.card < d),
          4 ^ (A.card - B.card) := Finset.sum_le_sum hterm
    _ ≤ ∑ B ∈ A.powerset, 4 ^ (A.card - B.card) :=
      Finset.sum_le_sum_of_subset_of_nonneg (Finset.filter_subset _ _)
        (by intro B hBA hnot; positivity)
    _ = 5 ^ A.card := sum_powerset_four_pow_compl A

private theorem four_mul_five_pow_lt_six_pow (n d : ℕ)
    (hd : 0 < d) (hdn : 16 * d ≤ n) :
    4 ^ d * 5 ^ n < 6 ^ n := by
  have hblock : 4 * 5 ^ 16 < 6 ^ 16 := by norm_num
  have hpow : (4 * 5 ^ 16) ^ d < (6 ^ 16) ^ d :=
    Nat.pow_lt_pow_left hblock (Nat.ne_of_gt hd)
  have hrem : 5 ^ (n - 16 * d) ≤ 6 ^ (n - 16 * d) := by
    gcongr
    norm_num
  calc
    4 ^ d * 5 ^ n = 4 ^ d * 5 ^ (16 * d + (n - 16 * d)) := by
      rw [Nat.add_sub_of_le hdn]
    _ = (4 * 5 ^ 16) ^ d * 5 ^ (n - 16 * d) := by
      rw [pow_add, pow_mul, mul_pow]
      ring
    _ ≤ (4 * 5 ^ 16) ^ d * 6 ^ (n - 16 * d) :=
      Nat.mul_le_mul_left _ hrem
    _ < (6 ^ 16) ^ d * 6 ^ (n - 16 * d) :=
      Nat.mul_lt_mul_of_pos_right hpow (pow_pos (by norm_num) _)
    _ = 6 ^ n := by
      rw [← pow_mul, ← pow_add, Nat.add_sub_of_le hdn]

/-- A fixed quantitative relation-count criterion. A bound of `(4/3)^N`
on relation supports yields a dissociated subset of size at least `d`
whenever `d > 0` and `16d ≤ N`. -/
theorem exists_dissociated_of_exponential_relation_count
    (A : Finset ℂ) (d : ℕ)
    (hd : 0 < d) (hdA : 16 * d ≤ A.card)
    (hrel : (A.powerset.filter AddRelationSupport).card * 3 ^ A.card ≤
      4 ^ A.card) :
    ∃ B : Finset ℂ, B ⊆ A ∧ d ≤ B.card ∧
      AddDissociated (↑B : Set ℂ) := by
  let R := (A.powerset.filter AddRelationSupport).card
  let S := (A.powerset.filter fun B => B.card < d).card
  have hdle : d ≤ A.card := by omega
  have hsmall : S * 4 ^ (A.card - d) ≤ 5 ^ A.card :=
    small_subset_count_weighted A d
  have hnum : 4 ^ d * 5 ^ A.card < 6 ^ A.card :=
    four_mul_five_pow_lt_six_pow A.card d hd hdA
  have hbound : (R * S) * (3 ^ A.card * 4 ^ (A.card - d)) ≤
      4 ^ A.card * 5 ^ A.card := by
    calc
      _ = (R * 3 ^ A.card) * (S * 4 ^ (A.card - d)) := by ring
      _ ≤ 4 ^ A.card * 5 ^ A.card := Nat.mul_le_mul hrel hsmall
  have hstrict : 4 ^ A.card * 5 ^ A.card <
      2 ^ A.card * (3 ^ A.card * 4 ^ (A.card - d)) := by
    have hfour : 4 ^ A.card = 4 ^ d * 4 ^ (A.card - d) := by
      rw [← pow_add, Nat.add_sub_of_le hdle]
    have hsix : 6 ^ A.card = 2 ^ A.card * 3 ^ A.card := by
      calc
        6 ^ A.card = (2 * 3) ^ A.card := by norm_num
        _ = _ := mul_pow 2 3 A.card
    calc
      _ = (4 ^ d * 5 ^ A.card) * 4 ^ (A.card - d) := by
        rw [hfour]
        ring
      _ < 6 ^ A.card * 4 ^ (A.card - d) :=
        Nat.mul_lt_mul_of_pos_right hnum (pow_pos (by norm_num) _)
      _ = _ := by rw [hsix]; ring
  have hRS : R * S < 2 ^ A.card :=
    lt_of_mul_lt_mul_right (lt_of_le_of_lt hbound hstrict) (Nat.zero_le _)
  exact exists_dissociated_of_relation_count A d hRS

/-- The ready-to-use counting bridge when harmonic analysis bounds the
number of signed relations rather than just their supports. -/
theorem exists_dissociated_of_signed_relation_bound
    (A : Finset ℂ) (d : ℕ)
    (hd : 0 < d) (hdA : 16 * d ≤ A.card)
    (hrel : (signedRelations A).card * 3 ^ A.card ≤ 4 ^ A.card) :
    ∃ B : Finset ℂ, B ⊆ A ∧ d ≤ B.card ∧
      AddDissociated (↑B : Set ℂ) := by
  apply exists_dissociated_of_exponential_relation_count A d hd hdA
  exact (Nat.mul_le_mul_right _ (card_relation_supports_le_signedRelations A)).trans hrel

end Erdos.Research.PisierRelationCounting

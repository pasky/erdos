import Mathlib.Data.Finset.Card
import Mathlib.Data.Finset.Lattice.Fold
import Mathlib.Tactic

/-!
# Branching levels in finite binary word sets

A finite set of binary words has at most `2 ^ h` elements when every word
encounters at most `h` branching levels. The extracted first-difference levels
are represented by distinct companion words.
-/

namespace Erdos.Problem963

def Word : ℕ → Type
  | 0 => PUnit
  | n + 1 => Bool × Word n

noncomputable def child {n : ℕ} (S : Finset (Word (n + 1))) (b : Bool) :
    Finset (Word n) := by
  classical
  exact (S.filter (fun a => a.1 = b)).image Prod.snd

theorem mem_child_iff {n : ℕ} {S : Finset (Word (n + 1))} {b : Bool}
    {a : Word n} : a ∈ child S b ↔ (b, a) ∈ S := by
  classical
  simp only [child]
  constructor
  · intro ha
    obtain ⟨⟨c, t⟩, h, rfl⟩ := Finset.mem_image.mp ha
    obtain ⟨ht, hc⟩ := Finset.mem_filter.mp h
    change c = b at hc
    cases hc
    exact ht
  · intro h
    exact Finset.mem_image.mpr ⟨(b, a), Finset.mem_filter.mpr ⟨h, rfl⟩, rfl⟩

theorem card_child {n : ℕ} (S : Finset (Word (n + 1))) (b : Bool) :
    (child S b).card = (S.filter (fun a => a.1 = b)).card := by
  classical
  apply Finset.card_image_of_injOn
  intro x hx y hy hxy
  exact Prod.ext ((Finset.mem_filter.mp hx).2.trans (Finset.mem_filter.mp hy).2.symm) hxy

theorem card_eq_card_children {n : ℕ} (S : Finset (Word (n + 1))) :
    S.card = (child S false).card + (child S true).card := by
  classical
  rw [card_child, card_child]
  have h := Finset.card_filter_add_card_filter_not (s := S) (fun a => a.1 = false)
  simpa only [Bool.not_eq_false] using h.symm

noncomputable def branchRank : (n : ℕ) → Finset (Word n) → Word n → ℕ
  | 0, _, _ => 0
  | n + 1, S, a =>
      branchRank n (child S a.1) a.2 +
        if (child S (!a.1)).Nonempty then 1 else 0

theorem card_le_pow_of_branchRank_le :
    ∀ (n : ℕ) (S : Finset (Word n)) (h : ℕ),
      (∀ a ∈ S, branchRank n S a ≤ h) → S.card ≤ 2 ^ h := by
  intro n
  induction n with
  | zero =>
      intro S h _
      have hcard : S.card ≤ 1 := Finset.card_le_one.mpr (by
        intro a _ b _
        cases a
        cases b
        rfl)
      exact hcard.trans (by
        have hp : 0 < 2 ^ h := pow_pos (by omega : 0 < (2 : ℕ)) _
        omega)
  | succ n ih =>
      intro S h hr
      classical
      let S0 := child S false
      let S1 := child S true
      have hcard : S.card = S0.card + S1.card := card_eq_card_children S
      by_cases h0 : S0.Nonempty
      · by_cases h1 : S1.Nonempty
        · cases h with
          | zero =>
              obtain ⟨a, ha⟩ := h0
              have hm : (false, a) ∈ S := mem_child_iff.mp ha
              have hv := hr (false, a) hm
              simp [branchRank, S1, h1] at hv
          | succ h =>
              have hr0 : ∀ a ∈ S0, branchRank n S0 a ≤ h := by
                intro a ha
                have hv := hr (false, a) (mem_child_iff.mp ha)
                have hv' : branchRank n S0 a + 1 ≤ h + 1 := by
                  simpa [branchRank, S0, S1, h1] using hv
                omega
              have hr1 : ∀ a ∈ S1, branchRank n S1 a ≤ h := by
                intro a ha
                have hv := hr (true, a) (mem_child_iff.mp ha)
                have hv' : branchRank n S1 a + 1 ≤ h + 1 := by
                  simpa [branchRank, S0, S1, h0] using hv
                omega
              have hb0 := ih S0 h hr0
              have hb1 := ih S1 h hr1
              rw [hcard, pow_succ]
              omega
        · have hr0 : ∀ a ∈ S0, branchRank n S0 a ≤ h := by
            intro a ha
            have hv := hr (false, a) (mem_child_iff.mp ha)
            simpa [branchRank, S0, S1, h1] using hv
          have hb0 := ih S0 h hr0
          simp only [Finset.not_nonempty_iff_eq_empty] at h1
          simp [hcard, h1, hb0]
      · by_cases h1 : S1.Nonempty
        · have hr1 : ∀ a ∈ S1, branchRank n S1 a ≤ h := by
            intro a ha
            have hv := hr (true, a) (mem_child_iff.mp ha)
            simpa [branchRank, S0, S1, h0] using hv
          have hb1 := ih S1 h hr1
          simp only [Finset.not_nonempty_iff_eq_empty] at h0
          simp [hcard, h0, hb1]
        · simp only [Finset.not_nonempty_iff_eq_empty] at h0 h1
          simp [hcard, h0, h1]

theorem exists_large_branchRank {n h : ℕ} (S : Finset (Word n))
    (hcard : 2 ^ h < S.card) :
    ∃ a ∈ S, h < branchRank n S a := by
  by_contra hn
  push Not at hn
  exact (not_le.mpr hcard) (card_le_pow_of_branchRank_le n S h hn)

def encodeNat : (n : ℕ) → ℕ → Word n
  | 0, _ => PUnit.unit
  | n + 1, x => (Nat.bodd x, encodeNat n (Nat.div2 x))

theorem encodeNat_injective_of_lt :
    ∀ (n x y : ℕ), x < 2 ^ n → y < 2 ^ n →
      encodeNat n x = encodeNat n y → x = y := by
  intro n
  induction n with
  | zero =>
      intro x y hx hy _
      simp at hx hy
      omega
  | succ n ih =>
      intro x y hx hy he
      have hb : Nat.bodd x = Nat.bodd y := congrArg Prod.fst he
      have ht : encodeNat n (Nat.div2 x) = encodeNat n (Nat.div2 y) :=
        congrArg Prod.snd he
      have hdx : Nat.div2 x < 2 ^ n := by
        have hxb : x < 2 * 2 ^ n := by simpa [pow_succ, mul_comm] using hx
        have hd := Nat.bodd_add_div2 x
        omega
      have hdy : Nat.div2 y < 2 ^ n := by
        have hyb : y < 2 * 2 ^ n := by simpa [pow_succ, mul_comm] using hy
        have hd := Nat.bodd_add_div2 y
        omega
      have hd := ih _ _ hdx hdy ht
      calc
        x = Nat.bit (Nat.bodd x) (Nat.div2 x) := (Nat.bit_bodd_div2 x).symm
        _ = Nat.bit (Nat.bodd y) (Nat.div2 y) := by rw [hb, hd]
        _ = y := Nat.bit_bodd_div2 y

theorem encodeNat_injOn (S : Finset ℕ) :
    Set.InjOn (encodeNat (S.sup id)) S := by
  intro x hx y hy he
  apply encodeNat_injective_of_lt (S.sup id) x y
  · exact (Finset.le_sup hx).trans_lt (S.sup id).lt_two_pow_self
  · exact (Finset.le_sup hy).trans_lt (S.sup id).lt_two_pow_self
  · exact he

noncomputable def codeSet (S : Finset ℕ) : Finset (Word (S.sup id)) := by
  classical
  exact S.image (encodeNat (S.sup id))

theorem card_codeSet (S : Finset ℕ) :
    (codeSet S).card = S.card := by
  classical
  unfold codeSet
  exact Finset.card_image_of_injOn (encodeNat_injOn S)

/-- The level of the first branch at which two binary words differ. -/
def firstDiff : (n : ℕ) → Word n → Word n → Option ℕ
  | 0, _, _ => none
  | n + 1, a, b =>
      if a.1 = b.1 then (firstDiff n a.2 b.2).map Nat.succ else some 0

theorem firstDiff_eq_none_iff_eq :
    ∀ (n : ℕ) (a b : Word n), firstDiff n a b = none ↔ a = b := by
  intro n
  induction n with
  | zero =>
      intro a b
      constructor
      · intro _
        cases a
        cases b
        rfl
      · intro _
        rfl
  | succ n ih =>
      intro a b
      by_cases h : a.1 = b.1
      · simp only [firstDiff, h, ↓reduceIte, Option.map_eq_none_iff, ih]
        constructor
        · intro ht
          exact Prod.ext h ht
        · intro he
          exact congrArg Prod.snd he
      · simp only [firstDiff, h, ↓reduceIte, reduceCtorEq, false_iff]
        intro he
        exact h (congrArg Prod.fst he)

theorem firstDiff_encodeNat_of_bodd_ne {n x y : ℕ}
    (h : Nat.bodd x ≠ Nat.bodd y) :
    firstDiff (n + 1) (encodeNat (n + 1) x) (encodeNat (n + 1) y) = some 0 := by
  simp [firstDiff, encodeNat, h]

theorem firstDiff_encodeNat_of_bodd_eq {n x y : ℕ}
    (h : Nat.bodd x = Nat.bodd y) :
    firstDiff (n + 1) (encodeNat (n + 1) x) (encodeNat (n + 1) y) =
      (firstDiff n (encodeNat n (Nat.div2 x)) (encodeNat n (Nat.div2 y))).map Nat.succ := by
  simp [firstDiff, encodeNat, h]

noncomputable def levels {n : ℕ} (S : Finset (Word n)) (a : Word n) :
    Finset (Option ℕ) := by
  classical
  exact (S.image (firstDiff n a)).erase none

theorem mem_levels_iff {n : ℕ} {S : Finset (Word n)} {a : Word n}
    {j : Option ℕ} :
    j ∈ levels S a ↔ j ≠ none ∧ ∃ b ∈ S, firstDiff n a b = j := by
  classical
  simp only [levels, Finset.mem_erase, Finset.mem_image]

theorem shift_injective : Function.Injective (Option.map Nat.succ) := by
  intro x y h
  cases x <;> cases y <;> simp_all

theorem rank_le_levels_card :
    ∀ (n : ℕ) (S : Finset (Word n)) (a : Word n),
      branchRank n S a ≤ (levels S a).card := by
  intro n
  induction n with
  | zero =>
      intro S a
      simp [branchRank]
  | succ n ih =>
      intro S a
      classical
      let C := child S a.1
      let D := levels C a.2
      let E := levels S a
      let shifted := D.image (Option.map Nat.succ)
      have hshift : shifted.card = D.card :=
        Finset.card_image_of_injective D shift_injective
      have hsubset : shifted ⊆ E := by
        intro j hj
        obtain ⟨k, hk, rfl⟩ := Finset.mem_image.mp hj
        obtain ⟨hk0, b, hb, hdiff⟩ := mem_levels_iff.mp hk
        apply mem_levels_iff.mpr
        constructor
        · cases k <;> simp_all
        · refine ⟨(a.1, b), mem_child_iff.mp hb, ?_⟩
          simp [firstDiff, hdiff]
      have hbase := ih C a.2
      by_cases hother : (child S (!a.1)).Nonempty
      · obtain ⟨b, hb⟩ := hother
        have hother' : (child S (!a.1)).Nonempty := ⟨b, hb⟩
        have hzero : some 0 ∈ E := by
          apply mem_levels_iff.mpr
          refine ⟨by simp, ( !a.1, b), mem_child_iff.mp hb, ?_⟩
          simp [firstDiff]
        have hnot : some 0 ∉ shifted := by
          intro hz
          obtain ⟨k, _, hk⟩ := Finset.mem_image.mp hz
          cases k <;> simp at hk
        have hsubinsert : insert (some 0) shifted ⊆ E := by
          intro j hj
          rcases Finset.mem_insert.mp hj with rfl | hj
          · exact hzero
          · exact hsubset hj
        have hcard := Finset.card_le_card hsubinsert
        rw [Finset.card_insert_of_notMem hnot, hshift] at hcard
        simpa [branchRank, C, E, hother'] using
          (Nat.add_le_add_right hbase 1).trans hcard
      · have hcard := Finset.card_le_card hsubset
        rw [hshift] at hcard
        simpa [branchRank, C, hother] using hbase.trans hcard

theorem exists_large_levels {n h : ℕ} (S : Finset (Word n))
    (hcard : 2 ^ h < S.card) :
    ∃ a ∈ S, h < (levels S a).card := by
  obtain ⟨a, ha, hrank⟩ := exists_large_branchRank S hcard
  exact ⟨a, ha, hrank.trans_le (rank_le_levels_card n S a)⟩

theorem choose_distinct_preimages {α β : Type*} (A : Finset α) (D : Finset β)
    (f : α → β) (hD : ∀ b ∈ D, ∃ a ∈ A, f a = b) :
    ∃ T : Finset α, T ⊆ A ∧ T.card = D.card ∧ Set.InjOn f T ∧
      ∀ a ∈ T, f a ∈ D := by
  classical
  let g : {b // b ∈ D} → α := fun b => Classical.choose (hD b.1 b.2)
  have hg (b : {b // b ∈ D}) : g b ∈ A ∧ f (g b) = b.1 :=
    Classical.choose_spec (hD b.1 b.2)
  have hinj : Function.Injective g := by
    intro b c he
    apply Subtype.ext
    calc
      b.1 = f (g b) := (hg b).2.symm
      _ = f (g c) := congrArg f he
      _ = c.1 := (hg c).2
  let T := D.attach.image g
  refine ⟨T, ?_, ?_, ?_, ?_⟩
  · intro a ha
    obtain ⟨b, _, rfl⟩ := Finset.mem_image.mp ha
    exact (hg b).1
  · simpa [T] using (Finset.card_image_of_injective D.attach hinj)
  · intro a ha c hc he
    obtain ⟨b, _, rfl⟩ := Finset.mem_image.mp ha
    obtain ⟨d, _, rfl⟩ := Finset.mem_image.mp hc
    congr 1
    apply Subtype.ext
    calc
      b.1 = f (g b) := (hg b).2.symm
      _ = f (g d) := he
      _ = d.1 := (hg d).2
  · intro a ha
    obtain ⟨b, _, rfl⟩ := Finset.mem_image.mp ha
    rw [(hg b).2]
    exact b.2

theorem exists_firstDiff_companions {n h : ℕ} (S : Finset (Word n))
    (hcard : 2 ^ h < S.card) :
    ∃ a ∈ S, ∃ T : Finset (Word n), T ⊆ S ∧ h < T.card ∧
      a ∉ T ∧ Set.InjOn (firstDiff n a) T := by
  obtain ⟨a, ha, hlevels⟩ := exists_large_levels S hcard
  have hD : ∀ j ∈ levels S a, ∃ b ∈ S, firstDiff n a b = j := by
    intro j hj
    exact (mem_levels_iff.mp hj).2
  obtain ⟨T, hTS, hTcard, hinj, hTlevels⟩ :=
    choose_distinct_preimages S (levels S a) (firstDiff n a) hD
  refine ⟨a, ha, T, hTS, by simpa [hTcard] using hlevels, ?_, hinj⟩
  intro hat
  have hmem : (firstDiff n a a) ∈ levels S a := hTlevels a hat
  have hnone : firstDiff n a a = none := (firstDiff_eq_none_iff_eq n a a).2 rfl
  exact (mem_levels_iff.mp hmem).1 hnone

end Erdos.Problem963

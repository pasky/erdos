import Mathlib.NumberTheory.Padics.PadicVal.Basic
import Mathlib.Combinatorics.Additive.Dissociation
import Mathlib.Data.Finset.Max
import Mathlib.Data.Int.Lemmas

/-!
# Distinct 2-adic valuations and dissociation

A signed sum of nonzero integers with pairwise distinct 2-adic valuations cannot
vanish. For Problem 963, this observation turns points selected from distinct
branches of the binary residue tree into a dissociated set after removing the
short interval of valuations that can meet a bounded pivot coefficient.
-/

namespace Erdos.Problem963

private theorem two_pow_dvd_iff (n : ℕ) (z : ℤ) :
    (2 : ℤ) ^ n ∣ z ↔ z = 0 ∨ n ≤ padicValInt 2 z := by
  exact padicValInt_dvd_iff_of_ne_one (by decide) n z

/-- The valuation of a nonzero coefficient of magnitude at most `d+1`
lies in the interval excluded around the pivot valuation. -/
theorem pivot_coefficient_valuation_bound
    (a c : ℤ) (d : ℕ) (ha : a ≠ 0) (hc : c ≠ 0)
    (hsize : c.natAbs ≤ d + 1) :
    padicValInt 2 a ≤ padicValInt 2 (c * a) ∧
      padicValInt 2 (c * a) ≤ padicValInt 2 a + Nat.log 2 (d + 1) := by
  haveI : Fact (Nat.Prime 2) := ⟨Nat.prime_two⟩
  rw [padicValInt.mul hc ha]
  constructor
  · omega
  · have hval : padicValInt 2 c ≤ Nat.log 2 c.natAbs :=
      padicValNat_le_nat_log c.natAbs
    have hlog : Nat.log 2 c.natAbs ≤ Nat.log 2 (d + 1) :=
      Nat.log_mono_right hsize
    omega

/-- Distinct valuations of nonzero integer summands prevent cancellation. -/
theorem sum_ne_zero_of_distinct_valuation
    {α : Type*} [DecidableEq α] (s : Finset α) (f : α → ℤ)
    (hs : s.Nonempty)
    (hf : ∀ x ∈ s, f x ≠ 0)
    (hv : (s : Set α).InjOn (fun x => padicValInt 2 (f x))) :
    ∑ x ∈ s, f x ≠ 0 := by
  obtain ⟨x, hx, hmin⟩ := s.exists_min_image (fun x => padicValInt 2 (f x)) hs
  let n := padicValInt 2 (f x) + 1
  have hx_notdvd : ¬ (2 : ℤ) ^ n ∣ f x := by
    rw [two_pow_dvd_iff]
    push Not
    exact ⟨hf x hx, Nat.lt_succ_self _⟩
  have hrest : (2 : ℤ) ^ n ∣ ∑ y ∈ s.erase x, f y := by
    apply Finset.dvd_sum
    intro y hy
    have hys : y ∈ s := Finset.mem_of_mem_erase hy
    have hyx : y ≠ x := (Finset.mem_erase.mp hy).1
    have hlt : padicValInt 2 (f x) < padicValInt 2 (f y) := by
      apply lt_of_le_of_ne (hmin y hys)
      intro heq
      exact hyx (hv hx hys heq).symm
    rw [two_pow_dvd_iff]
    exact Or.inr hlt
  intro hsum
  have hx_dvd : (2 : ℤ) ^ n ∣ f x := by
    have heq : f x + ∑ y ∈ s.erase x, f y = 0 := by
      simpa only [Finset.add_sum_erase _ _ hx] using hsum
    have : f x = -(∑ y ∈ s.erase x, f y) := eq_neg_of_add_eq_zero_left heq
    rw [this]
    exact dvd_neg.mpr hrest
  exact hx_notdvd hx_dvd

/-- A finite sum with independent plus/minus choices cannot vanish when the
underlying nonzero terms have distinct 2-adic valuations. -/
theorem signed_sum_ne_zero_of_distinct_valuation
    {α : Type*} [DecidableEq α] (s : Finset α) (f ε : α → ℤ)
    (hs : s.Nonempty)
    (hf : ∀ x ∈ s, f x ≠ 0)
    (hv : (s : Set α).InjOn (fun x => padicValInt 2 (f x)))
    (hε : ∀ x ∈ s, ε x = 1 ∨ ε x = -1) :
    ∑ x ∈ s, ε x * f x ≠ 0 := by
  have hval (x : α) (hx : x ∈ s) :
      padicValInt 2 (ε x * f x) = padicValInt 2 (f x) := by
    rcases hε x hx with h | h <;> simp [h, padicValInt]
  apply sum_ne_zero_of_distinct_valuation s (fun x => ε x * f x) hs
  · intro x hx
    rcases hε x hx with h | h <;> simp [h, hf x hx]
  · intro x hx y hy h
    apply hv hx hy
    change padicValInt 2 (f x) = padicValInt 2 (f y)
    simpa only [hval x hx, hval y hy] using h

/-- A nonzero set of integers with distinct 2-adic valuations is
dissociated. This handles the zero pivot in the binary residue tree. -/
theorem zero_pivot_dissociated (B : Finset ℤ)
    (hzero : 0 ∉ B)
    (hv : (B : Set ℤ).InjOn (fun b => padicValInt 2 b)) :
    AddDissociated (B : Set ℤ) := by
  by_contra hnot
  obtain ⟨T, U, hT, hU, hdisj, hne, hsum⟩ :=
    not_addDissociated_iff_exists_disjoint.mp hnot
  let C : Finset ℤ := T ∪ U
  let ε : ℤ → ℤ := fun b => if b ∈ T then 1 else -1
  have hC : C ⊆ B := by
    intro b hb
    rcases Finset.mem_union.mp hb with hbT | hbU
    · exact hT hbT
    · exact hU hbU
  have hCne : C.Nonempty := by
    by_contra hn
    have hC0 : C = ∅ := Finset.not_nonempty_iff_eq_empty.mp hn
    have hT0 : T = ∅ := by
      have hsub : T ⊆ C := Finset.subset_union_left
      rw [hC0] at hsub
      exact Finset.subset_empty.mp hsub
    have hU0 : U = ∅ := by
      have hsub : U ⊆ C := Finset.subset_union_right
      rw [hC0] at hsub
      exact Finset.subset_empty.mp hsub
    exact hne (hT0.trans hU0.symm)
  have hnonzero : ∀ b ∈ C, b ≠ 0 := by
    intro b hb hb0
    exact hzero (hb0 ▸ hC hb)
  have hε : ∀ b ∈ C, ε b = 1 ∨ ε b = -1 := by
    intro b hb
    by_cases hbT : b ∈ T
    · exact Or.inl (by simp [ε, hbT])
    · exact Or.inr (by simp [ε, hbT])
  have hsig : ∑ b ∈ C, ε b * b =
      (∑ b ∈ T, b) - (∑ b ∈ U, b) := by
    dsimp [C]
    rw [Finset.sum_union hdisj]
    have hplus : ∑ b ∈ T, ε b * b = ∑ b ∈ T, b := by
      apply Finset.sum_congr rfl
      intro b hb
      simp [ε, hb]
    have hminus : ∑ b ∈ U, ε b * b = -(∑ b ∈ U, b) := by
      calc
        ∑ b ∈ U, ε b * b = ∑ b ∈ U, -b := by
          apply Finset.sum_congr rfl
          intro b hb
          have hbnotT : b ∉ T := by
            intro hbT
            exact (Finset.disjoint_left.mp hdisj hbT) hb
          simp [ε, hbnotT]
        _ = -(∑ b ∈ U, b) := by rw [Finset.sum_neg_distrib]
    rw [hplus, hminus]
    ring
  have hfree := signed_sum_ne_zero_of_distinct_valuation C (fun b => b) ε
    hCne hnonzero (hv.mono (by simpa using hC)) hε
  apply hfree
  rw [hsig]
  exact sub_eq_zero.mpr hsum

/-- Adding one more nonzero summand at a fresh valuation still prevents
cancellation. The proof indexes the new term by `none` and the existing terms
by `some x`. -/
private theorem add_sum_ne_zero_of_distinct_valuation
    {α : Type*} [DecidableEq α] (s : Finset α) (f : α → ℤ) (z : ℤ)
    (hz : z ≠ 0)
    (hf : ∀ x ∈ s, f x ≠ 0)
    (hv : (s : Set α).InjOn (fun x => padicValInt 2 (f x)))
    (hzv : ∀ x ∈ s, padicValInt 2 z ≠ padicValInt 2 (f x)) :
    z + ∑ x ∈ s, f x ≠ 0 := by
  let r : Finset (Option α) := insert none (s.image some)
  let g : Option α → ℤ := fun o => match o with
    | none => z
    | some x => f x
  have hr : r.Nonempty := ⟨none, by simp [r]⟩
  have hmem (o : Option α) (ho : o ∈ r) :
      o = none ∨ ∃ x ∈ s, o = some x := by
    rcases Finset.mem_insert.mp ho with hnone | himage
    · exact Or.inl hnone
    · obtain ⟨x, hx, hxo⟩ := Finset.mem_image.mp himage
      exact Or.inr ⟨x, hx, hxo.symm⟩
  have hg : ∀ o ∈ r, g o ≠ 0 := by
    intro o ho
    rcases hmem o ho with rfl | ⟨x, hx, rfl⟩
    · exact hz
    · exact hf x hx
  have hginj : (r : Set (Option α)).InjOn
      (fun o => padicValInt 2 (g o)) := by
    intro o ho p hp heq
    rcases hmem o ho with rfl | ⟨x, hx, rfl⟩
    · rcases hmem p hp with rfl | ⟨y, hy, rfl⟩
      · rfl
      · exact (hzv y hy heq).elim
    · rcases hmem p hp with rfl | ⟨y, hy, rfl⟩
      · exact (hzv x hx heq.symm).elim
      · exact congrArg some (hv hx hy heq)
  have hsum : ∑ o ∈ r, g o = z + ∑ x ∈ s, f x := by
    rw [Finset.sum_insert (by simp)]
    rw [Finset.sum_image (by intro x hx y hy h; exact Option.some.inj h)]
  rw [← hsum]
  exact sum_ne_zero_of_distinct_valuation r g hr hg hginj

/-- No short signed relation can involve a nonzero pivot after all differences
whose valuations lie in the coefficient range have been removed. -/
private theorem no_short_pivot_relation
    (a : ℤ) (B C : Finset ℤ) (ε : ℤ → ℤ) (c : ℤ)
    (ha : a ≠ 0) (haB : a ∉ B)
    (hC : C ⊆ B)
    (hactive : c ≠ 0 ∨ C.Nonempty)
    (hε : ∀ b ∈ C, ε b = 1 ∨ ε b = -1)
    (hc : c.natAbs ≤ B.card + 1)
    (hv : (B : Set ℤ).InjOn (fun b => padicValInt 2 (b - a)))
    (havoid : ∀ b ∈ B,
      padicValInt 2 (b - a) < padicValInt 2 a ∨
        padicValInt 2 a + Nat.log 2 (B.card + 1) < padicValInt 2 (b - a)) :
    c * a + ∑ b ∈ C, ε b * (b - a) ≠ 0 := by
  have hdelta : ∀ b ∈ C, b - a ≠ 0 := by
    intro b hb hzero
    have hba : b = a := sub_eq_zero.mp hzero
    exact haB (hba ▸ hC hb)
  have hterm : ∀ b ∈ C, ε b * (b - a) ≠ 0 := by
    intro b hb
    rcases hε b hb with h | h
    · simpa [h] using hdelta b hb
    · simpa only [h, neg_one_mul, ne_eq, neg_eq_zero] using hdelta b hb
  have hval (b : ℤ) (hb : b ∈ C) :
      padicValInt 2 (ε b * (b - a)) = padicValInt 2 (b - a) := by
    rcases hε b hb with h | h
    · simp [h]
    · rw [h, neg_one_mul]
      simp only [padicValInt, Int.natAbs_neg]
  have hterm_val : (C : Set ℤ).InjOn
      (fun b => padicValInt 2 (ε b * (b - a))) := by
    intro b hb b' hb' heq
    apply hv (hC hb) (hC hb')
    change padicValInt 2 (b - a) = padicValInt 2 (b' - a)
    simpa only [hval b hb, hval b' hb'] using heq
  by_cases hc0 : c = 0
  · have hCne : C.Nonempty := by
      rcases hactive with hc' | hCne
      · exact (hc' hc0).elim
      · exact hCne
    simpa [hc0] using
      signed_sum_ne_zero_of_distinct_valuation C (fun b => b - a) ε hCne
        hdelta (hv.mono (by simpa using hC)) hε
  · have hca : c * a ≠ 0 := mul_ne_zero hc0 ha
    have hcoef := pivot_coefficient_valuation_bound a c B.card ha hc0 hc
    have hdist : ∀ b ∈ C,
        padicValInt 2 (c * a) ≠ padicValInt 2 (ε b * (b - a)) := by
      intro b hb heq
      have houtside := havoid b (hC hb)
      rw [hval b hb] at heq
      rcases houtside with hlo | hhi <;> omega
    exact add_sum_ne_zero_of_distinct_valuation C
      (fun b => ε b * (b - a)) (c * a) hca hterm hterm_val hdist

/-- Algebraic expansion of an equality between two subset sums about the
pivot. For disjoint `T,U`, take `C=(T.erase a) ∪ (U.erase a)`, give it signs
`+1` on the first side and `-1` on the second, and take
`c=(T.card:ℤ)-(U.card:ℤ)`. Disjointness and containment give
`|c| ≤ B.card+1`; `T ≠ U` gives the active-relation condition. -/
private theorem signed_relation_of_equal_subset_sums
    (a : ℤ) (B T U : Finset ℤ)
    (haB : a ∉ B)
    (hT : (T : Set ℤ) ⊆ (↑(insert a B) : Set ℤ))
    (hU : (U : Set ℤ) ⊆ (↑(insert a B) : Set ℤ))
    (hdisj : Disjoint T U) (hne : T ≠ U)
    (hsum : ∑ t ∈ T, t = ∑ u ∈ U, u) :
    ∃ (c : ℤ) (C : Finset ℤ) (ε : ℤ → ℤ),
      C ⊆ B ∧ (c ≠ 0 ∨ C.Nonempty) ∧
        (∀ b ∈ C, ε b = 1 ∨ ε b = -1) ∧
        c.natAbs ≤ B.card + 1 ∧
        c * a + ∑ b ∈ C, ε b * (b - a) = 0 := by
  let c : ℤ := (T.card : ℤ) - U.card
  let C : Finset ℤ := (T.erase a) ∪ (U.erase a)
  let ε : ℤ → ℤ := fun b => if b ∈ T then 1 else -1
  refine ⟨c, C, ε, ?_, ?_, ?_, ?_, ?_⟩
  · intro b hb
    rcases Finset.mem_union.mp hb with hbT | hbU
    · have hbne : b ≠ a := (Finset.mem_erase.mp hbT).1
      have hbmem : b ∈ insert a B := hT (Finset.mem_of_mem_erase hbT)
      exact (Finset.mem_insert.mp hbmem).resolve_left hbne
    · have hbne : b ≠ a := (Finset.mem_erase.mp hbU).1
      have hbmem : b ∈ insert a B := hU (Finset.mem_of_mem_erase hbU)
      exact (Finset.mem_insert.mp hbmem).resolve_left hbne
  · by_contra h
    have hc0 : c = 0 := not_not.mp (fun hc => h (Or.inl hc))
    have hC0 : C = ∅ := Finset.not_nonempty_iff_eq_empty.mp
      (fun hC => h (Or.inr hC))
    have hT0 : T.erase a = ∅ := by
      have hsub : T.erase a ⊆ C := Finset.subset_union_left
      rw [hC0] at hsub
      exact Finset.subset_empty.mp hsub
    have hU0 : U.erase a = ∅ := by
      have hsub : U.erase a ⊆ C := Finset.subset_union_right
      rw [hC0] at hsub
      exact Finset.subset_empty.mp hsub
    rcases (Finset.erase_eq_empty_iff T a).mp hT0 with hTe | hTs <;>
      rcases (Finset.erase_eq_empty_iff U a).mp hU0 with hUe | hUs
    · exact hne (hTe.trans hUe.symm)
    · simp [c, hTe, hUs] at hc0
    · simp [c, hTs, hUe] at hc0
    · exact hne (hTs.trans hUs.symm)
  · intro b hb
    by_cases hbT : b ∈ T
    · exact Or.inl (by simp [ε, hbT])
    · exact Or.inr (by simp [ε, hbT])
  · have hTfin : T ⊆ insert a B := by
      intro b hb
      exact hT hb
    have hUfin : U ⊆ insert a B := by
      intro b hb
      exact hU hb
    have hcard : T.card + U.card ≤ B.card + 1 := by
      calc
        T.card + U.card = (T ∪ U).card := (Finset.card_union_of_disjoint hdisj).symm
        _ ≤ (insert a B).card := Finset.card_le_card (Finset.union_subset hTfin hUfin)
        _ = B.card + 1 := by simp [haB]
    have hTc : T.card ≤ B.card + 1 := by omega
    have hUc : U.card ≤ B.card + 1 := by omega
    exact Int.natAbs_coe_sub_coe_le_of_le hTc hUc
  · let δ : ℤ → ℤ := fun b => b - a
    have hdisjC : Disjoint (T.erase a) (U.erase a) := by
      apply Finset.disjoint_left.mpr
      intro b hbT hbU
      exact (Finset.disjoint_left.mp hdisj)
        (Finset.mem_of_mem_erase hbT) (Finset.mem_of_mem_erase hbU)
    have hsumErase (S : Finset ℤ) :
        ∑ b ∈ S.erase a, δ b = ∑ b ∈ S, δ b := by
      by_cases haS : a ∈ S
      · have hh := Finset.add_sum_erase S δ haS
        simpa [δ] using hh
      · simp [Finset.erase_eq_of_notMem haS]
    have hCsum :
        ∑ b ∈ C, ε b * δ b =
          (∑ b ∈ T, δ b) - (∑ b ∈ U, δ b) := by
      dsimp [C]
      rw [Finset.sum_union hdisjC]
      have hplus : ∑ b ∈ T.erase a, ε b * δ b = ∑ b ∈ T.erase a, δ b := by
        apply Finset.sum_congr rfl
        intro b hb
        simp [ε, Finset.mem_of_mem_erase hb]
      have hminus : ∑ b ∈ U.erase a, ε b * δ b = -(∑ b ∈ U.erase a, δ b) := by
        calc
          ∑ b ∈ U.erase a, ε b * δ b = ∑ b ∈ U.erase a, -(δ b) := by
            apply Finset.sum_congr rfl
            intro b hb
            have hbnotT : b ∉ T := by
              intro hbT
              exact (Finset.disjoint_left.mp hdisj hbT) (Finset.mem_of_mem_erase hb)
            simp [ε, hbnotT]
          _ = -(∑ b ∈ U.erase a, δ b) := by rw [Finset.sum_neg_distrib]
      rw [hplus, hminus, hsumErase T, hsumErase U]
      ring
    have hsumAbout (S : Finset ℤ) :
        ∑ b ∈ S, b = (S.card : ℤ) * a + ∑ b ∈ S, δ b := by
      calc
        ∑ b ∈ S, b = ∑ b ∈ S, (a + δ b) := by
          apply Finset.sum_congr rfl
          intro b hb
          simp [δ]
        _ = (S.card : ℤ) * a + ∑ b ∈ S, δ b := by
          rw [Finset.sum_add_distrib]
          simp
    calc
      c * a + ∑ b ∈ C, ε b * (b - a)
          = ((T.card : ℤ) * a + ∑ b ∈ T, δ b) -
              ((U.card : ℤ) * a + ∑ b ∈ U, δ b) := by
                rw [show (∑ b ∈ C, ε b * (b - a)) =
                  ∑ b ∈ C, ε b * δ b from rfl, hCsum]
                dsimp [c]
                ring
      _ = (∑ b ∈ T, b) - (∑ b ∈ U, b) := by rw [hsumAbout T, hsumAbout U]
      _ = 0 := sub_eq_zero.mpr hsum

/-- If the pivot is nonzero and the selected differences have distinct
2-adic valuations outside the short coefficient interval, adjoining the pivot
produces a dissociated set. -/
theorem pivot_dissociated
    (a : ℤ) (B : Finset ℤ)
    (ha : a ≠ 0) (haB : a ∉ B)
    (hv : (B : Set ℤ).InjOn (fun b => padicValInt 2 (b - a)))
    (havoid : ∀ b ∈ B,
      padicValInt 2 (b - a) < padicValInt 2 a ∨
        padicValInt 2 a + Nat.log 2 (B.card + 1) < padicValInt 2 (b - a)) :
    AddDissociated (↑(insert a B) : Set ℤ) := by
  by_contra hnot
  obtain ⟨T, U, hT, hU, hdisj, hne, hsum⟩ :=
    not_addDissociated_iff_exists_disjoint.mp hnot
  obtain ⟨c, C, ε, hC, hactive, hε, hc, hrel⟩ :=
    signed_relation_of_equal_subset_sums a B T U haB hT hU hdisj hne hsum
  exact no_short_pivot_relation a B C ε c ha haB hC hactive hε hc hv havoid hrel

end Erdos.Problem963

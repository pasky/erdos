import Erdos.Problem963.Valuation
import Erdos.Problem963.ResidueTree
import Erdos.Problem963.IntegerModel
import Erdos.Problem963.LogBound
import Mathlib.Data.Finset.Card
import Mathlib.Data.Finset.Max
import Mathlib.Order.Interval.Finset.Nat
import Mathlib.Data.Nat.Log
import Mathlib.Tactic

/-!
# The near-logarithmic dissociation bound for finite real sets

The binary residue tree supplies integer points with distinct 2-adic
valuations of their differences from a pivot. The valuation argument gives a
dissociated subset, and an integer model transfers the cardinal estimate to
finite real sets.
-/

namespace Erdos.Problem963

/-- A finite integer set with more than `2^h` points has a pivot and at least
`h+1` other points whose differences from it have distinct 2-adic valuations.
This is supplied by the binary residue-tree argument. -/
private def BranchExtraction (S : Finset ℤ) : Prop :=
  ∀ h : ℕ, 2 ^ h < S.card →
    ∃ a ∈ S, ∃ T : Finset ℤ,
      T ⊆ S.erase a ∧ h + 1 ≤ T.card ∧
        (T : Set ℤ).InjOn (fun b => padicValInt 2 (b - a))

/-- The branch-extraction statement and the valuation argument imply the
sharper integer cardinal estimate. -/
private theorem card_le_pow_of_branch_extraction
    (S : Finset ℤ) (d : ℕ)
    (hextract : BranchExtraction S)
    (hbound : ∀ B : Finset ℤ, B ⊆ S → AddDissociated (B : Set ℤ) → B.card ≤ d) :
    S.card ≤ 2 ^ (d + Nat.log 2 (d + 1)) := by
  classical
  let L := Nat.log 2 (d + 1)
  by_contra hcard
  have hlarge : 2 ^ (d + L) < S.card := Nat.lt_of_not_ge hcard
  obtain ⟨a, ha, T, hT, hTcard, hv⟩ := hextract (d + L) hlarge
  have haT : a ∉ T := by
    intro hmem
    exact (Finset.mem_erase.mp (hT hmem)).1 rfl
  have hTS : T ⊆ S := by
    intro b hb
    exact Finset.mem_of_mem_erase (hT hb)
  by_cases ha0 : a = 0
  · have hsize : d + 1 ≤ T.card := by omega
    obtain ⟨B, hB, hBcard⟩ := Finset.exists_subset_card_eq hsize
    have hBS : B ⊆ S := hB.trans hTS
    have hB0 : 0 ∉ B := by
      intro hb
      exact haT (ha0 ▸ hB hb)
    have hvalB : (B : Set ℤ).InjOn (fun b => padicValInt 2 b) := by
      intro b hb c hc heq
      apply hv (hB hb) (hB hc)
      simpa [ha0] using heq
    have hD := zero_pivot_dissociated B hB0 hvalB
    have hsmall := hbound B hBS hD
    omega
  · let u := padicValInt 2 a
    let bad : Finset ℤ := T.filter
      (fun b => u ≤ padicValInt 2 (b - a) ∧ padicValInt 2 (b - a) ≤ u + L)
    let good : Finset ℤ := T.filter
      (fun b => ¬ (u ≤ padicValInt 2 (b - a) ∧ padicValInt 2 (b - a) ≤ u + L))
    have hbadmap : Set.MapsTo (fun b => padicValInt 2 (b - a))
        (bad : Set ℤ) (Finset.Icc u (u + L) : Set ℕ) := by
      intro b hb
      exact Finset.mem_Icc.mpr (Finset.mem_filter.mp hb).2
    have hbadinj : (bad : Set ℤ).InjOn
        (fun b => padicValInt 2 (b - a)) := by
      intro b hb c hc heq
      exact hv (Finset.mem_filter.mp hb).1 (Finset.mem_filter.mp hc).1 heq
    have hbadcard : bad.card ≤ L + 1 := by
      have h := Finset.card_le_card_of_injOn
        (fun b => padicValInt 2 (b - a)) hbadmap hbadinj
      simp only [Nat.card_Icc] at h
      change bad.card ≤ u + L + 1 - u at h
      omega
    have hparts : T.card = bad.card + good.card := by
      have h := Finset.card_filter_add_card_filter_not (s := T)
        (fun b => u ≤ padicValInt 2 (b - a) ∧
          padicValInt 2 (b - a) ≤ u + L)
      simpa only [bad, good] using h.symm
    have hgoodcard : d ≤ good.card := by omega
    obtain ⟨B, hB, hBcard⟩ := Finset.exists_subset_card_eq hgoodcard
    have hBT : B ⊆ T := by
      intro b hb
      exact (Finset.mem_filter.mp (hB hb)).1
    have haB : a ∉ B := by
      intro hb
      exact haT (hBT hb)
    have hBS : insert a B ⊆ S := by
      intro b hb
      rcases Finset.mem_insert.mp hb with rfl | hb
      · exact ha
      · exact hTS (hBT hb)
    have hvalB : (B : Set ℤ).InjOn
        (fun b => padicValInt 2 (b - a)) := by
      intro b hb c hc heq
      exact hv (hBT hb) (hBT hc) heq
    have hgood : ∀ b ∈ B,
        padicValInt 2 (b - a) < padicValInt 2 a ∨
          padicValInt 2 a + Nat.log 2 (B.card + 1) < padicValInt 2 (b - a) := by
      intro b hb
      have hnot := (Finset.mem_filter.mp (hB hb)).2
      have hcases : padicValInt 2 (b - a) < u ∨
          u + L < padicValInt 2 (b - a) := by omega
      simpa [u, L, hBcard] using hcases
    have hD := pivot_dissociated a B ha0 haB hvalB hgood
    have hsmall := hbound (insert a B) hBS hD
    simp [haB, hBcard] at hsmall

/-- The estimate in the usual product form. -/
private theorem card_le_mul_pow_of_branch_extraction
    (S : Finset ℤ) (d : ℕ)
    (hextract : BranchExtraction S)
    (hbound : ∀ B : Finset ℤ, B ⊆ S → AddDissociated (B : Set ℤ) → B.card ≤ d) :
    S.card ≤ (d + 1) * 2 ^ d := by
  calc
    S.card ≤ 2 ^ (d + Nat.log 2 (d + 1)) :=
      card_le_pow_of_branch_extraction S d hextract hbound
    _ = 2 ^ d * 2 ^ Nat.log 2 (d + 1) := by rw [pow_add]
    _ ≤ 2 ^ d * (d + 1) :=
      Nat.mul_le_mul_left _ (Nat.pow_log_le_self 2 (by omega))
    _ = (d + 1) * 2 ^ d := Nat.mul_comm _ _

private theorem branchExtraction (S : Finset ℤ) : BranchExtraction S := by
  intro h hlarge
  obtain ⟨a, ha, T, hTS, hTcard, haT, hv⟩ :=
    exists_int_valuation_companions S h hlarge
  refine ⟨a, ha, T, ?_, by omega, hv⟩
  intro b hb
  exact Finset.mem_erase.mpr ⟨by
    intro hba
    exact haT (hba ▸ hb), hTS hb⟩

/-- If every dissociated subset of an integer set has size at most `d`, then
the set has at most `2^(d+⌊log₂(d+1)⌋)` points. -/
theorem integer_card_le_pow (S : Finset ℤ) (d : ℕ)
    (hbound : ∀ B : Finset ℤ, B ⊆ S → AddDissociated (B : Set ℤ) → B.card ≤ d) :
    S.card ≤ 2 ^ (d + Nat.log 2 (d + 1)) :=
  card_le_pow_of_branch_extraction S d (branchExtraction S) hbound

/-- The cardinal bound in product form. -/
theorem integer_card_bound (S : Finset ℤ) (d : ℕ)
    (hbound : ∀ B : Finset ℤ, B ⊆ S → AddDissociated (B : Set ℤ) → B.card ≤ d) :
    S.card ≤ (d + 1) * 2 ^ d :=
  card_le_mul_pow_of_branch_extraction S d (branchExtraction S) hbound

/-- Every nonempty finite real set has a dissociated subset achieving the
near-logarithmic lower bound. -/
theorem exists_real_dissociated_large
    (A : Finset ℝ) (hA : A.Nonempty) :
    ∃ B : Finset ℝ, B ⊆ A ∧ AddDissociated (B : Set ℝ) ∧
      Real.logb 2 (A.card : ℝ) -
        Real.logb 2 (Real.logb 2 (A.card : ℝ) + 1) ≤ (B.card : ℝ) := by
  classical
  let F : Finset (Finset ℝ) := A.powerset.filter
    (fun B => AddDissociated (B : Set ℝ))
  have hF : F.Nonempty := ⟨∅, by simp [F]⟩
  obtain ⟨B, hBF, hmax⟩ := Finset.exists_max_image F Finset.card hF
  have hBA : B ⊆ A := Finset.mem_powerset.mp (Finset.mem_filter.mp hBF).1
  have hBD : AddDissociated (B : Set ℝ) := (Finset.mem_filter.mp hBF).2
  have hbound : ∀ C : Finset ℝ, C ⊆ A →
      AddDissociated (C : Set ℝ) → C.card ≤ B.card := by
    intro C hCA hCD
    exact hmax C (Finset.mem_filter.mpr ⟨Finset.mem_powerset.mpr hCA, hCD⟩)
  have hcard := real_card_bound_of_integer_card_bound integer_card_bound A B.card hbound
  exact ⟨B, hBA, hBD,
    log_bound_of_card_le A.card B.card (Finset.card_pos.mpr hA) hcard⟩

end Erdos.Problem963

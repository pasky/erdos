import Erdos.Problem963.BinaryWords
import Erdos.Problem963.BitValuation
import Mathlib.NumberTheory.Padics.PadicVal.Basic
import Mathlib.Data.Finset.Max

/-!
# Binary residue-tree extraction for Erdős Problem 963

Binary words encode a finite integer set after translation. Distinct first
branching levels then give companions whose differences from one pivot have
pairwise distinct 2-adic valuations.
-/

namespace Erdos.Problem963

private theorem padicValInt_sub_comm (a b : ℤ) :
    padicValInt 2 (a - b) = padicValInt 2 (b - a) := by
  unfold padicValInt
  congr 1
  calc
    (a - b).natAbs = (-(a - b)).natAbs := (Int.natAbs_neg _).symm
    _ = (b - a).natAbs := by congr 1; ring

theorem exists_nat_valuation_companions (A : Finset ℕ) (h : ℕ)
    (hcard : 2 ^ h < A.card) :
    ∃ a ∈ A, ∃ T : Finset ℕ, T ⊆ A ∧ h < T.card ∧ a ∉ T ∧
      Set.InjOn (fun b : ℕ => padicValInt 2 ((a : ℤ) - b)) T := by
  classical
  let n := A.sup id
  have hcode : 2 ^ h < (codeSet A).card := by simpa [card_codeSet] using hcard
  obtain ⟨w, hw, U, hU, hUcard, hwU, hUinj⟩ :=
    exists_firstDiff_companions (codeSet A) hcode
  have hwA : ∃ a ∈ A, encodeNat n a = w := by
    change w ∈ A.image (encodeNat n) at hw
    exact Finset.mem_image.mp hw
  obtain ⟨a, ha, haCode⟩ := hwA
  have hUpre : ∀ u ∈ U, ∃ b ∈ A, encodeNat n b = u := by
    intro u hu
    have huCode := hU hu
    change u ∈ A.image (encodeNat n) at huCode
    exact Finset.mem_image.mp huCode
  obtain ⟨T, hTA, hTcard, hCodeInj, hCodeT⟩ :=
    choose_distinct_preimages A U (encodeNat n) hUpre
  have haT : a ∉ T := by
    intro hat
    exact hwU (haCode ▸ hCodeT a hat)
  have hbound (b : ℕ) (hb : b ∈ A) : b < 2 ^ n :=
    (Finset.le_sup hb).trans_lt (A.sup id).lt_two_pow_self
  have hvalInj : Set.InjOn
      (fun b : ℕ => padicValInt 2 ((a : ℤ) - b)) T := by
    intro b hb c hc hval
    have hab : a ≠ b := by intro he; exact haT (he ▸ hb)
    have hac : a ≠ c := by intro he; exact haT (he ▸ hc)
    have hfb : firstDiff n w (encodeNat n b) =
        some (padicValInt 2 ((a : ℤ) - b)) := by
      rw [← haCode]
      exact firstDiff_encodeNat_eq_padicValInt n a b
        (hbound a ha) (hbound b (hTA hb)) hab
    have hfc : firstDiff n w (encodeNat n c) =
        some (padicValInt 2 ((a : ℤ) - c)) := by
      rw [← haCode]
      exact firstDiff_encodeNat_eq_padicValInt n a c
        (hbound a ha) (hbound c (hTA hc)) hac
    change padicValInt 2 ((a : ℤ) - b) =
      padicValInt 2 ((a : ℤ) - c) at hval
    have hbc : encodeNat n b = encodeNat n c :=
      hUinj (hCodeT b hb) (hCodeT c hc)
        (hfb.trans ((congrArg some hval).trans hfc.symm))
    exact hCodeInj hb hc hbc
  exact ⟨a, ha, T, hTA, by simpa [hTcard] using hUcard, haT, hvalInj⟩

theorem exists_int_valuation_companions (S : Finset ℤ) (h : ℕ)
    (hcard : 2 ^ h < S.card) :
    ∃ a ∈ S, ∃ T : Finset ℤ, T ⊆ S ∧ h < T.card ∧ a ∉ T ∧
      Set.InjOn (fun b : ℤ => padicValInt 2 (b - a)) T := by
  classical
  have hS : S.Nonempty := Finset.card_pos.mp (by
    have hp : 0 < 2 ^ h := pow_pos (by omega : 0 < (2 : ℕ)) _
    omega)
  let m := S.min' hS
  let q : ℤ → ℕ := fun x => (x - m).toNat
  have hcast (x : ℤ) (hx : x ∈ S) : (q x : ℤ) = x - m := by
    have hm : m ≤ x := S.min'_le x hx
    exact Int.toNat_of_nonneg (sub_nonneg.mpr hm)
  have hqInj : Set.InjOn q S := by
    intro x hx y hy he
    have h := congrArg (fun z : ℕ => (z : ℤ)) he
    rw [hcast x hx, hcast y hy] at h
    omega
  let A := S.image q
  have hAcard : A.card = S.card := Finset.card_image_of_injOn hqInj
  have hA : 2 ^ h < A.card := by simpa [hAcard] using hcard
  obtain ⟨an, han, V, hVA, hVcard, hanV, hVinj⟩ :=
    exists_nat_valuation_companions A h hA
  have hanpre : ∃ a ∈ S, q a = an := Finset.mem_image.mp han
  obtain ⟨a, ha, haq⟩ := hanpre
  have hVpre : ∀ v ∈ V, ∃ b ∈ S, q b = v := by
    intro v hv
    exact Finset.mem_image.mp (hVA hv)
  obtain ⟨T, hTS, hTcard, hqTinj, hqT⟩ :=
    choose_distinct_preimages S V q hVpre
  have haT : a ∉ T := by
    intro hat
    exact hanV (haq ▸ hqT a hat)
  have hdiff (x y : ℤ) (hx : x ∈ S) (hy : y ∈ S) :
      ((q x : ℕ) : ℤ) - q y = x - y := by
    rw [hcast x hx, hcast y hy]
    ring
  have hvalInj : Set.InjOn (fun b : ℤ => padicValInt 2 (a - b)) T := by
    intro b hb c hc hval
    have hnat : padicValInt 2 (((an : ℕ) : ℤ) - q b) =
        padicValInt 2 (((an : ℕ) : ℤ) - q c) := by
      rw [← haq, hdiff a b ha (hTS hb), hdiff a c ha (hTS hc)]
      exact hval
    have hqeq : q b = q c :=
      hVinj (hqT b hb) (hqT c hc) hnat
    exact hqTinj hb hc hqeq
  have hvalInj' : Set.InjOn (fun b : ℤ => padicValInt 2 (b - a)) T := by
    intro b hb c hc hval
    apply hvalInj hb hc
    change padicValInt 2 (b - a) = padicValInt 2 (c - a) at hval
    change padicValInt 2 (a - b) = padicValInt 2 (a - c)
    rwa [padicValInt_sub_comm a b, padicValInt_sub_comm a c]
  exact ⟨a, ha, T, hTS, by simpa [hTcard] using hVcard, haT, hvalInj'⟩

end Erdos.Problem963

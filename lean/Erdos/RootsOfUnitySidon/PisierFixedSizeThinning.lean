import Mathlib.Data.Finset.Powerset
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic

/-!
# First moment for fixed-size thinning

The relation-count extraction route can choose an `m`-element subset directly.
The exact double count below avoids a separate concentration estimate for the
size of a Bernoulli sample.
-/

namespace Erdos.Research.PisierFixedSizeThinning

variable {α : Type*} [DecidableEq α]

/-- The total number of relation supports seen across all `m`-element
subsets is an exact weighted sum over supports. -/
theorem sum_relation_count_powersetCard (A : Finset α)
    (Rel : Finset α → Prop) [DecidablePred Rel] (m : ℕ) :
    (∑ H ∈ A.powersetCard m, (H.powerset.filter Rel).card) =
      ∑ M ∈ A.powerset.filter Rel,
        ((A.powersetCard m).filter (fun H => M ⊆ H)).card := by
  classical
  have hcount (H : Finset α) (hH : H ∈ A.powersetCard m) :
      (H.powerset.filter Rel).card =
        ∑ M ∈ A.powerset.filter Rel, if M ⊆ H then 1 else 0 := by
    have hHA : H ⊆ A := (Finset.mem_powersetCard.mp hH).1
    have heq : H.powerset.filter Rel =
        (A.powerset.filter Rel).filter (fun M => M ⊆ H) := by
      ext M
      simp only [Finset.mem_filter, Finset.mem_powerset]
      constructor
      · rintro ⟨hMH, hRel⟩
        exact ⟨⟨hMH.trans hHA, hRel⟩, hMH⟩
      · rintro ⟨⟨_, hRel⟩, hMH⟩
        exact ⟨hMH, hRel⟩
    rw [heq]
    simp
  calc
    (∑ H ∈ A.powersetCard m, (H.powerset.filter Rel).card) =
        ∑ H ∈ A.powersetCard m,
          ∑ M ∈ A.powerset.filter Rel, if M ⊆ H then 1 else 0 := by
      apply Finset.sum_congr rfl
      exact hcount
    _ = ∑ M ∈ A.powerset.filter Rel,
          ∑ H ∈ A.powersetCard m, if M ⊆ H then 1 else 0 := Finset.sum_comm
    _ = ∑ M ∈ A.powerset.filter Rel,
          ((A.powersetCard m).filter (fun H => M ⊆ H)).card := by
      simp

/-- Each relation support of size at most `m` is contained in exactly a
binomial number of `m`-element subsets. Larger supports occur in none. -/
theorem sum_relation_count_choose (A : Finset α)
    (Rel : Finset α → Prop) [DecidablePred Rel] (m : ℕ) :
    (∑ H ∈ A.powersetCard m, (H.powerset.filter Rel).card) =
      ∑ M ∈ A.powerset.filter Rel,
        if M.card ≤ m then Nat.choose (A.card - M.card) (m - M.card)
        else 0 := by
  classical
  rw [sum_relation_count_powersetCard]
  apply Finset.sum_congr rfl
  intro M hMA
  have hMA' : M ⊆ A := (Finset.mem_powerset.mp (Finset.mem_filter.mp hMA).1)
  by_cases hMm : M.card ≤ m
  · simp only [hMm, ↓reduceIte]
    exact Finset.card_filter_powersetCard_subset M A m hMA' hMm
  · simp only [hMm, ↓reduceIte]
    have hempty : (A.powersetCard m).filter (fun H => M ⊆ H) = ∅ := by
      apply Finset.eq_empty_iff_forall_notMem.mpr
      intro H hH
      obtain ⟨hHp, hMH⟩ := Finset.mem_filter.mp hH
      have hHcard := (Finset.mem_powersetCard.mp hHp).2
      exact hMm (hHcard ▸ Finset.card_le_card hMH)
    simp [hempty]

/-- A binomial incidence identity, expressed using falling factorials. -/
theorem choose_mul_descFactorial (n m r : ℕ) (hrm : r ≤ m) :
    Nat.choose n m * m.descFactorial r =
      Nat.choose (n - r) (m - r) * n.descFactorial r := by
  have h := Nat.choose_mul (n := n) (k := m) (s := r) hrm
  rw [Nat.descFactorial_eq_factorial_mul_choose,
    Nat.descFactorial_eq_factorial_mul_choose]
  calc
    Nat.choose n m * (r.factorial * Nat.choose m r) =
        r.factorial * (Nat.choose n m * Nat.choose m r) := by ring
    _ = r.factorial * (Nat.choose n r * Nat.choose (n - r) (m - r)) := by rw [h]
    _ = Nat.choose (n - r) (m - r) * (r.factorial * Nat.choose n r) := by ring

/-- A convenient, slightly loose incidence bound when the sampled subset
has at most half the original size. This is enough for fixed-density thinning. -/
theorem choose_incidence_pow_bound (n m r : ℕ)
    (hrm : r ≤ m) (hmn : 2 * m ≤ n) :
    n ^ r * Nat.choose (n - r) (m - r) ≤
      (2 * m) ^ r * Nat.choose n m := by
  have hrn : r ≤ n := by omega
  have hlin : n ≤ 2 * (n + 1 - r) := by omega
  have hpow : n ^ r ≤ 2 ^ r * n.descFactorial r := by
    calc
      n ^ r ≤ (2 * (n + 1 - r)) ^ r := Nat.pow_le_pow_left hlin r
      _ = 2 ^ r * (n + 1 - r) ^ r := mul_pow _ _ _
      _ ≤ 2 ^ r * n.descFactorial r := by
        exact Nat.mul_le_mul_left _ (Nat.pow_sub_le_descFactorial n r)
  calc
    n ^ r * Nat.choose (n - r) (m - r) ≤
        (2 ^ r * n.descFactorial r) * Nat.choose (n - r) (m - r) :=
      Nat.mul_le_mul_right _ hpow
    _ = 2 ^ r * (Nat.choose n m * m.descFactorial r) := by
      rw [choose_mul_descFactorial n m r hrm]
      ring
    _ ≤ 2 ^ r * (Nat.choose n m * m ^ r) := by
      gcongr
      exact Nat.descFactorial_le_pow m r
    _ = (2 * m) ^ r * Nat.choose n m := by rw [mul_pow]; ring

/-- A first-moment bound yields a single sample of exactly the prescribed
size. The right side is the number of samples times the allowed relation
count. -/
theorem exists_fixed_size_relation_count_le (A : Finset α)
    (Rel : Finset α → Prop) [DecidablePred Rel]
    (m K : ℕ) (hm : m ≤ A.card)
    (hbound :
      (∑ M ∈ A.powerset.filter Rel,
        if M.card ≤ m then Nat.choose (A.card - M.card) (m - M.card)
        else 0) ≤ K * Nat.choose A.card m) :
    ∃ H : Finset α, H ⊆ A ∧ H.card = m ∧
      (H.powerset.filter Rel).card ≤ K := by
  classical
  let P := A.powersetCard m
  have hP : P.Nonempty := by
    exact Finset.powersetCard_nonempty.mpr hm
  by_contra hnone
  have hgt : ∀ H ∈ P, K < (H.powerset.filter Rel).card := by
    intro H hH
    by_contra hnot
    exact hnone ⟨H, (Finset.mem_powersetCard.mp hH).1,
      (Finset.mem_powersetCard.mp hH).2, Nat.le_of_not_gt hnot⟩
  have hsum :
      ∑ H ∈ P, K < ∑ H ∈ P, (H.powerset.filter Rel).card :=
    Finset.sum_lt_sum_of_nonempty hP hgt
  have hleft : (∑ H ∈ P, K) = K * Nat.choose A.card m := by
    simp [P, mul_comm]
  have hbound' :
      (∑ H ∈ P, (H.powerset.filter Rel).card) ≤ ∑ H ∈ P, K := by
    calc
      _ = ∑ M ∈ A.powerset.filter Rel,
          if M.card ≤ m then Nat.choose (A.card - M.card) (m - M.card)
          else 0 := sum_relation_count_choose A Rel m
      _ ≤ K * Nat.choose A.card m := hbound
      _ = ∑ H ∈ P, K := hleft.symm
  exact (Nat.not_lt.mpr hbound') hsum

/-- A weighted relation moment at density `2m/n` controls a fixed-size
sample. The integer formulation avoids divisions in later applications. -/
theorem exists_fixed_size_of_weighted_relation_bound (A : Finset α)
    (Rel : Finset α → Prop) [DecidablePred Rel]
    (m K : ℕ) (hmpos : 0 < m) (hmn : 2 * m ≤ A.card)
    (hweighted :
      (∑ M ∈ A.powerset.filter Rel,
        (2 * m) ^ M.card * A.card ^ (A.card - M.card)) ≤
        K * A.card ^ A.card) :
    ∃ H : Finset α, H ⊆ A ∧ H.card = m ∧
      (H.powerset.filter Rel).card ≤ K := by
  classical
  let n := A.card
  have hnpos : 0 < n := by dsimp [n]; omega
  have hterm (M : Finset α) (hMA : M ∈ A.powerset.filter Rel) :
      n ^ n * (if M.card ≤ m then
        Nat.choose (n - M.card) (m - M.card) else 0) ≤
        Nat.choose n m * ((2 * m) ^ M.card * n ^ (n - M.card)) := by
    have hMn : M.card ≤ n :=
      Finset.card_le_card (Finset.mem_powerset.mp (Finset.mem_filter.mp hMA).1)
    by_cases hMm : M.card ≤ m
    · have hnexp : n = M.card + (n - M.card) := by omega
      have hpow : n ^ n = n ^ M.card * n ^ (n - M.card) := by
        calc
          n ^ n = n ^ (M.card + (n - M.card)) := congrArg (n ^ ·) hnexp
          _ = n ^ M.card * n ^ (n - M.card) := pow_add _ _ _
      have hinc := choose_incidence_pow_bound n m M.card hMm (by simpa [n] using hmn)
      calc
        n ^ n * (if M.card ≤ m then
            Nat.choose (n - M.card) (m - M.card) else 0) =
          (n ^ M.card * Nat.choose (n - M.card) (m - M.card)) *
            n ^ (n - M.card) := by rw [if_pos hMm, hpow]; ring
        _ ≤ ((2 * m) ^ M.card * Nat.choose n m) * n ^ (n - M.card) :=
          Nat.mul_le_mul_right _ hinc
        _ = Nat.choose n m * ((2 * m) ^ M.card * n ^ (n - M.card)) := by ring
    · simp [hMm]
  have hmul :
      n ^ n * (∑ M ∈ A.powerset.filter Rel,
        if M.card ≤ m then Nat.choose (n - M.card) (m - M.card)
        else 0) ≤
        n ^ n * (K * Nat.choose n m) := by
    calc
      _ = ∑ M ∈ A.powerset.filter Rel,
          n ^ n * (if M.card ≤ m then
            Nat.choose (n - M.card) (m - M.card) else 0) := by
          rw [Finset.mul_sum]
      _ ≤ ∑ M ∈ A.powerset.filter Rel,
          Nat.choose n m * ((2 * m) ^ M.card * n ^ (n - M.card)) :=
        Finset.sum_le_sum hterm
      _ = Nat.choose n m * (∑ M ∈ A.powerset.filter Rel,
          (2 * m) ^ M.card * n ^ (n - M.card)) := by rw [Finset.mul_sum]
      _ ≤ Nat.choose n m * (K * n ^ n) := by
        exact Nat.mul_le_mul_left _ (by simpa [n] using hweighted)
      _ = n ^ n * (K * Nat.choose n m) := by ring
  have hbound :
      (∑ M ∈ A.powerset.filter Rel,
        if M.card ≤ m then Nat.choose (A.card - M.card) (m - M.card)
        else 0) ≤ K * Nat.choose A.card m := by
    exact Nat.le_of_mul_le_mul_left (by simpa [n] using hmul)
      (pow_pos hnpos _)
  exact exists_fixed_size_relation_count_le A Rel m K (by omega) hbound

end Erdos.Research.PisierFixedSizeThinning

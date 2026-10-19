import Mathlib.Algebra.Order.Floor.Ring
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Tactic

/-!
# Finite conditional laws for lattice rounding

A `Law α` is a finite binary probability tree with outcomes in `α`. Its
weighted expectation is defined by recursion, so dependent choices in a
descending Gram--Schmidt rounding algorithm can be represented without an
ambient measure space. The moment lemmas below are the algebraic core needed
for that algorithm. The triangular rounding construction and its finite
sample law are proved here. Identifying a concrete integer basis and its
Gram--Schmidt vectors with the triangular input data is a separate adapter.
-/

namespace Erdos.Research.LatticeRounding

universe u v

/-- A finitely supported probability law, represented as a binary tree. -/
inductive Law (α : Type u) : Type u where
  | pure : α → Law α
  | mix (p : ℝ) (hp : 0 ≤ p) (hp1 : p ≤ 1) : Law α → Law α → Law α

namespace Law

/-- Weighted expectation of a real-valued function on the leaves. -/
def expect {α : Type u} : Law α → (α → ℝ) → ℝ
  | .pure a, f => f a
  | .mix p _ _ lo hi, f => (1 - p) * expect lo f + p * expect hi f

@[simp] theorem expect_pure {α : Type u} (f : α → ℝ) (a : α) :
    expect (.pure a) f = f a := rfl

@[simp] theorem expect_mix {α : Type u} (f : α → ℝ)
    (p : ℝ) (hp : 0 ≤ p) (hp1 : p ≤ 1) (lo hi : Law α) :
    expect (.mix p hp hp1 lo hi) f = (1 - p) * expect lo f + p * expect hi f := rfl

/-- Every finite tree has total mass one. -/
theorem expect_one {α : Type u} (L : Law α) : expect L (fun _ => 1) = 1 := by
  induction L with
  | pure a => rfl
  | mix p hp hp1 lo hi ihlo ihhi =>
      simp [expect, ihlo, ihhi]

theorem expect_nonneg {α : Type u} (L : Law α) (f : α → ℝ)
    (hf : ∀ a, 0 ≤ f a) : 0 ≤ expect L f := by
  induction L with
  | pure a => exact hf a
  | mix p hp hp1 lo hi ihlo ihhi =>
      exact add_nonneg (mul_nonneg (sub_nonneg.mpr hp1) ihlo)
        (mul_nonneg hp ihhi)

theorem expect_mono {α : Type u} (L : Law α) (f g : α → ℝ)
    (hfg : ∀ a, f a ≤ g a) : expect L f ≤ expect L g := by
  induction L with
  | pure a => exact hfg a
  | mix p hp hp1 lo hi ihlo ihhi =>
      simp only [expect_mix]
      exact add_le_add
        (mul_le_mul_of_nonneg_left ihlo (sub_nonneg.mpr hp1))
        (mul_le_mul_of_nonneg_left ihhi hp)

theorem expect_const {α : Type u} (L : Law α) (c : ℝ) :
    expect L (fun _ => c) = c := by
  induction L with
  | pure a => rfl
  | mix p hp hp1 lo hi ihlo ihhi =>
      simp only [expect_mix, ihlo, ihhi]
      ring

theorem expect_add {α : Type u} (L : Law α) (f g : α → ℝ) :
    expect L (fun a => f a + g a) = expect L f + expect L g := by
  induction L with
  | pure a => rfl
  | mix p hp hp1 lo hi ihlo ihhi =>
      simp only [expect_mix, ihlo, ihhi]
      ring

theorem expect_const_mul {α : Type u} (L : Law α) (c : ℝ) (f : α → ℝ) :
    expect L (fun a => c * f a) = c * expect L f := by
  induction L with
  | pure a => rfl
  | mix p hp hp1 lo hi ihlo ihhi =>
      simp only [expect_mix, ihlo, ihhi]
      ring

theorem expect_congr {α : Type u} (L : Law α) (f g : α → ℝ)
    (h : ∀ a, f a = g a) : expect L f = expect L g := by
  induction L with
  | pure a => exact h a
  | mix p hp hp1 lo hi ihlo ihhi =>
      simp only [expect_mix, ihlo, ihhi]

theorem expect_sum {α : Type u} {ι : Type v} (L : Law α)
    (s : Finset ι) (f : ι → α → ℝ) :
    expect L (fun a => ∑ i ∈ s, f i a) = ∑ i ∈ s, expect L (f i) := by
  classical
  induction s using Finset.induction_on with
  | empty =>
      simpa using expect_const L 0
  | @insert i s hi ih =>
      simp only [Finset.sum_insert hi]
      rw [expect_add, ih]

/-- Map every leaf of a finite law. -/
def map {α : Type u} {β : Type v} (g : α → β) : Law α → Law β
  | .pure a => .pure (g a)
  | .mix p hp hp1 lo hi => .mix p hp hp1 (map g lo) (map g hi)

theorem expect_map {α : Type u} {β : Type v} (L : Law α)
    (g : α → β) (f : β → ℝ) :
    expect (map g L) f = expect L (fun a => f (g a)) := by
  induction L with
  | pure a => rfl
  | mix p hp hp1 lo hi ihlo ihhi =>
      simp only [map, expect_mix, ihlo, ihhi]

/-- Substitute a finite law at each leaf; this models conditional rounding. -/
def bind {α : Type u} {β : Type v} (L : Law α) (g : α → Law β) : Law β :=
  match L with
  | .pure a => g a
  | .mix p hp hp1 lo hi => .mix p hp hp1 (bind lo g) (bind hi g)

theorem expect_bind {α : Type u} {β : Type v} (L : Law α)
    (g : α → Law β) (f : β → ℝ) :
    expect (bind L g) f = expect L (fun a => expect (g a) f) := by
  induction L with
  | pure a => rfl
  | mix p hp hp1 lo hi ihlo ihhi =>
      simp only [bind, expect_mix, ihlo, ihhi]

/-- A proposition holds at every leaf of a finite law. -/
def All {α : Type u} (P : α → Prop) : Law α → Prop
  | .pure a => P a
  | .mix _ _ _ lo hi => All P lo ∧ All P hi

theorem all_map {α : Type u} {β : Type v} (L : Law α)
    (g : α → β) (P : β → Prop) (h : All (fun a => P (g a)) L) :
    All P (map g L) := by
  induction L with
  | pure a => exact h
  | mix p hp hp1 lo hi ihlo ihhi =>
      exact ⟨ihlo h.1, ihhi h.2⟩

theorem all_bind {α : Type u} {β : Type v} (L : Law α)
    (g : α → Law β) (P : β → Prop)
    (h : ∀ a, All P (g a)) : All P (bind L g) := by
  induction L with
  | pure a => exact h a
  | mix p hp hp1 lo hi ihlo ihhi =>
      exact ⟨ihlo, ihhi⟩

theorem all_mono {α : Type u} (L : Law α) (P Q : α → Prop)
    (hPQ : ∀ a, P a → Q a) (h : All P L) : All Q L := by
  induction L with
  | pure a => exact hPQ a h
  | mix p hp hp1 lo hi ihlo ihhi =>
      exact ⟨ihlo h.1, ihhi h.2⟩

theorem expect_congr_of_all {α : Type u} (L : Law α) (f g : α → ℝ)
    (h : All (fun a => f a = g a) L) : expect L f = expect L g := by
  induction L with
  | pure a => exact h
  | mix p hp hp1 lo hi ihlo ihhi =>
      simp only [expect_mix, ihlo h.1, ihhi h.2]

/-- The leaf list makes the finiteness of a tree law explicit. Duplicate
outcomes remain distinct samples, as they should for conditional choices. -/
def atoms {α : Type u} : Law α → List (α × ℝ)
  | .pure a => [(a, 1)]
  | .mix p _ _ lo hi =>
      (atoms lo).map (fun aw => (aw.1, (1 - p) * aw.2)) ++
        (atoms hi).map (fun aw => (aw.1, p * aw.2))

private theorem sum_map_scaled {α : Type u} (xs : List (α × ℝ))
    (p : ℝ) (f : α → ℝ) :
    ((xs.map (fun aw => (aw.1, p * aw.2))).map
      (fun aw => aw.2 * f aw.1)).sum =
      p * (xs.map (fun aw => aw.2 * f aw.1)).sum := by
  induction xs with
  | nil => simp
  | cons aw xs ih =>
      simp only [List.map_cons, List.sum_cons, ih]
      ring

theorem atoms_expect {α : Type u} (L : Law α) (f : α → ℝ) :
    (L.atoms.map (fun aw => aw.2 * f aw.1)).sum = L.expect f := by
  induction L with
  | pure a => simp [atoms, expect]
  | mix p hp hp1 lo hi ihlo ihhi =>
      simp only [atoms, List.map_append, List.sum_append,
        sum_map_scaled, ihlo, ihhi, expect_mix]

theorem atoms_nonneg {α : Type u} (L : Law α) :
    ∀ aw ∈ L.atoms, 0 ≤ aw.2 := by
  induction L with
  | pure a =>
      intro aw haw
      simp only [atoms, List.mem_singleton] at haw
      simp [haw]
  | mix p hp hp1 lo hi ihlo ihhi =>
      intro aw haw
      simp only [atoms, List.mem_append] at haw
      rcases haw with hlow | hhigh
      · obtain ⟨aw', haw', rfl⟩ := List.mem_map.mp hlow
        exact mul_nonneg (sub_nonneg.mpr hp1) (ihlo aw' haw')
      · obtain ⟨aw', haw', rfl⟩ := List.mem_map.mp hhigh
        exact mul_nonneg hp (ihhi aw' haw')

theorem atoms_all {α : Type u} (L : Law α) (P : α → Prop)
    (h : All P L) : ∀ aw ∈ L.atoms, P aw.1 := by
  induction L with
  | pure a =>
      intro aw haw
      simp only [atoms, List.mem_singleton] at haw
      change P a at h
      simpa only [haw] using h
  | mix p hp hp1 lo hi ihlo ihhi =>
      intro aw haw
      simp only [atoms, List.mem_append] at haw
      rcases haw with hlow | hhigh
      · obtain ⟨aw', haw', rfl⟩ := List.mem_map.mp hlow
        exact ihlo h.1 aw' haw'
      · obtain ⟨aw', haw', rfl⟩ := List.mem_map.mp hhigh
        exact ihhi h.2 aw' haw'

/-- A concrete finite sample index for a tree law. -/
abbrev Sample {α : Type u} (L : Law α) := Fin L.atoms.length

def sampleValue {α : Type u} (L : Law α) (i : Sample L) : α :=
  (L.atoms.get i).1

def sampleWeight {α : Type u} (L : Law α) (i : Sample L) : ℝ :=
  (L.atoms.get i).2

theorem sampleWeight_nonneg {α : Type u} (L : Law α) (i : Sample L) :
    0 ≤ sampleWeight L i :=
  atoms_nonneg L _ (List.get_mem L.atoms i)

theorem sample_all {α : Type u} (L : Law α) (P : α → Prop)
    (h : All P L) (i : Sample L) : P (sampleValue L i) :=
  atoms_all L P h _ (List.get_mem L.atoms i)

/-- Flattening preserves every real-valued weighted expectation. -/
theorem sample_expect {α : Type u} (L : Law α) (f : α → ℝ) :
    (∑ i : Sample L, sampleWeight L i * f (sampleValue L i)) = L.expect f := by
  change (∑ i : Fin L.atoms.length, (L.atoms.get i).2 * f (L.atoms.get i).1) = _
  rw [← List.sum_ofFn]
  change (List.ofFn (fun i : Fin L.atoms.length =>
    (fun aw : α × ℝ => aw.2 * f aw.1) (L.atoms.get i))).sum = _
  calc
    _ = ((List.ofFn (L.atoms.get)).map
        (fun aw : α × ℝ => aw.2 * f aw.1)).sum := by
          exact congrArg List.sum
            (List.ofFn_comp' (L.atoms.get) (fun aw : α × ℝ => aw.2 * f aw.1))
    _ = (L.atoms.map (fun aw : α × ℝ => aw.2 * f aw.1)).sum := by
          rw [List.ofFn_get]
    _ = L.expect f := atoms_expect L f

theorem sampleWeight_sum_one {α : Type u} (L : Law α) :
    (∑ i : Sample L, sampleWeight L i) = 1 := by
  have h := sample_expect L (fun _ => 1)
  simpa only [mul_one, expect_one] using h

end Law

/-- Round a real scalar by choosing its floor or successor. -/
noncomputable def scalarLaw (x : ℝ) : Law ℤ :=
  .mix (Int.fract x) (Int.fract_nonneg x) (Int.fract_lt_one x).le
    (.pure ⌊x⌋) (.pure (⌊x⌋ + 1))

theorem scalarLaw_mean (x : ℝ) :
    (scalarLaw x).expect (fun k => (k : ℝ)) = x := by
  simp only [scalarLaw, Law.expect_mix, Law.expect_pure]
  push_cast
  calc
    _ = Int.fract x + (⌊x⌋ : ℝ) := by ring
    _ = x := Int.fract_add_floor x

theorem scalarLaw_error_mean (x : ℝ) :
    (scalarLaw x).expect (fun k => x - (k : ℝ)) = 0 := by
  simp only [scalarLaw, Law.expect_mix, Law.expect_pure]
  push_cast
  have h := Int.fract_add_floor x
  linarith

theorem scalarLaw_error_sq (x : ℝ) :
    (scalarLaw x).expect (fun k => (x - (k : ℝ)) ^ 2) =
      Int.fract x * (1 - Int.fract x) := by
  simp only [scalarLaw, Law.expect_mix, Law.expect_pure]
  push_cast
  have hlow : x - (⌊x⌋ : ℝ) = Int.fract x := by
    linarith [Int.fract_add_floor x]
  have hhigh : x - ((⌊x⌋ : ℝ) + 1) = Int.fract x - 1 := by
    linarith [Int.fract_add_floor x]
  rw [hlow, hhigh]
  ring

theorem scalarLaw_error_sq_le (x : ℝ) :
    (scalarLaw x).expect (fun k => (x - (k : ℝ)) ^ 2) ≤ 1 / 4 := by
  rw [scalarLaw_error_sq]
  nlinarith [sq_nonneg (Int.fract x - 1 / 2)]

/-- Pairwise uncorrelated centered errors have an additive second moment. -/
theorem expect_sum_sq_of_cross_zero {α : Type u} {ι : Type v}
    (L : Law α) (s : Finset ι) (e : ι → α → ℝ)
    (hcross : ∀ i ∈ s, ∀ j ∈ s, i ≠ j →
      L.expect (fun z => e i z * e j z) = 0) :
    L.expect (fun z => (∑ i ∈ s, e i z) ^ 2) =
      ∑ i ∈ s, L.expect (fun z => (e i z) ^ 2) := by
  calc
    L.expect (fun z => (∑ i ∈ s, e i z) ^ 2) =
        L.expect (fun z => ∑ i ∈ s, ∑ j ∈ s, e i z * e j z) := by
          apply L.expect_congr
          intro z
          rw [← Finset.sum_mul_sum]
          ring
    _ = ∑ i ∈ s, ∑ j ∈ s, L.expect (fun z => e i z * e j z) := by
          rw [Law.expect_sum]
          apply Finset.sum_congr rfl
          intro i hi
          rw [Law.expect_sum]
    _ = ∑ i ∈ s, L.expect (fun z => (e i z) ^ 2) := by
          apply Finset.sum_congr rfl
          intro i hi
          rw [Finset.sum_eq_single_of_mem i hi]
          · apply L.expect_congr
            intro z
            ring
          · intro j hj hji
            exact hcross i hi j hj (Ne.symm hji)

/-- The diagonal part of the Gram--Schmidt rounding estimate. This formulation
only requires the two conditional-moment consequences of the rounding process. -/
theorem coordinate_second_moment_le {α : Type u} {ι : Type v} {A : Type*}
    (L : Law α) (s : Finset ι) (η : α → ι → ℝ) (u : ι → A → ℝ) (a : A)
    (hcross : ∀ i ∈ s, ∀ j ∈ s, i ≠ j →
      L.expect (fun z => η z i * η z j) = 0)
    (hdiag : ∀ i ∈ s, L.expect (fun z => (η z i) ^ 2) ≤ 1 / 4) :
    L.expect (fun z => (∑ i ∈ s, η z i * u i a) ^ 2) ≤
      (1 / 4 : ℝ) * ∑ i ∈ s, (u i a) ^ 2 := by
  have hcross' : ∀ i ∈ s, ∀ j ∈ s, i ≠ j →
      L.expect (fun z => (η z i * u i a) * (η z j * u j a)) = 0 := by
    intro i hi j hj hij
    calc
      _ = (u i a * u j a) * L.expect (fun z => η z i * η z j) := by
        rw [← L.expect_const_mul]
        apply L.expect_congr
        intro z
        ring
      _ = 0 := by rw [hcross i hi j hj hij]; ring
  rw [expect_sum_sq_of_cross_zero L s (fun i z => η z i * u i a) hcross']
  calc
    (∑ i ∈ s, L.expect (fun z => (η z i * u i a) ^ 2)) =
        ∑ i ∈ s, (u i a) ^ 2 * L.expect (fun z => (η z i) ^ 2) := by
          apply Finset.sum_congr rfl
          intro i hi
          rw [← L.expect_const_mul]
          apply L.expect_congr
          intro z
          ring
    _ ≤ ∑ i ∈ s, (u i a) ^ 2 * (1 / 4 : ℝ) := by
          apply Finset.sum_le_sum
          intro i hi
          exact mul_le_mul_of_nonneg_left (hdiag i hi) (sq_nonneg _)
    _ = (1 / 4 : ℝ) * ∑ i ∈ s, (u i a) ^ 2 := by
          rw [Finset.mul_sum]
          apply Finset.sum_congr rfl
          intro i hi
          ring

/-- The same orthogonal-error hypotheses give an unbiased coordinate. -/
theorem coordinate_mean_zero {α : Type u} {ι : Type v} {A : Type*}
    (L : Law α) (s : Finset ι) (η : α → ι → ℝ) (u : ι → A → ℝ) (a : A)
    (hmean : ∀ i ∈ s, L.expect (fun z => η z i) = 0) :
    L.expect (fun z => ∑ i ∈ s, η z i * u i a) = 0 := by
  rw [Law.expect_sum]
  apply Finset.sum_eq_zero
  intro i hi
  calc
    _ = u i a * L.expect (fun z => η z i) := by
      rw [← L.expect_const_mul]
      apply L.expect_congr
      intro z
      ring
    _ = 0 := by rw [hmean i hi]; ring

/-- A leaf records both the integer coefficients and the centered errors in
the orthogonal coordinates. -/
abbrev Outcome (n : ℕ) := (Fin n → ℤ) × (Fin n → ℝ)

private def lowerCoefficients (n : ℕ) (α : Fin (n + 1) → ℝ)
    (μ : Fin (n + 1) → Fin (n + 1) → ℝ) (k : ℤ) : Fin n → ℝ :=
  fun j => α j.castSucc - (k : ℝ) * μ (Fin.last n) j.castSucc

private def lowerMatrix (n : ℕ)
    (μ : Fin (n + 1) → Fin (n + 1) → ℝ) : Fin n → Fin n → ℝ :=
  fun i j => μ i.castSucc j.castSucc

private def appendOutcome (n : ℕ) (α : Fin (n + 1) → ℝ)
    (k : ℤ) (out : Outcome n) : Outcome (n + 1) :=
  (Fin.snoc out.1 k, Fin.snoc out.2 (α (Fin.last n) - (k : ℝ)))

/-- Descending, conditionally unbiased rounding for an upper triangular
integer basis. `μ i j` is the coefficient of `u j` in `b i` for `j < i`.
Only those lower-triangular entries are used. -/
noncomputable def roundLaw : (n : ℕ) → (Fin n → ℝ) →
    (Fin n → Fin n → ℝ) → Law (Outcome n)
  | 0, _, _ => .pure (Fin.elim0, Fin.elim0)
  | n + 1, α, μ =>
      let top := Fin.last n
      let t := α top
      (scalarLaw t).bind fun k =>
        (roundLaw n (lowerCoefficients n α μ k) (lowerMatrix n μ)).map
          (appendOutcome n α k)

theorem roundLaw_succ (n : ℕ) (α : Fin (n + 1) → ℝ)
    (μ : Fin (n + 1) → Fin (n + 1) → ℝ) :
    roundLaw (n + 1) α μ =
      (scalarLaw (α (Fin.last n))).bind fun k =>
        (roundLaw n (lowerCoefficients n α μ k) (lowerMatrix n μ)).map
          (appendOutcome n α k) := rfl

/-- Every orthogonal-coordinate rounding error has mean zero. -/
theorem roundLaw_error_mean : ∀ (n : ℕ) (α : Fin n → ℝ)
    (μ : Fin n → Fin n → ℝ) (i : Fin n),
    (roundLaw n α μ).expect (fun out => out.2 i) = 0 := by
  intro n
  induction n with
  | zero =>
      intro α μ i
      exact i.elim0
  | succ n ih =>
      intro α μ i
      cases i using Fin.lastCases with
      | last =>
          rw [roundLaw_succ, Law.expect_bind]
          have hinner (k : ℤ) :
              ((roundLaw n (lowerCoefficients n α μ k) (lowerMatrix n μ)).map
                (appendOutcome n α k)).expect
                (fun out => out.2 (Fin.last n)) = α (Fin.last n) - (k : ℝ) := by
            rw [Law.expect_map]
            simp only [appendOutcome, Fin.snoc_last]
            exact Law.expect_const _ _
          simp only [hinner]
          exact scalarLaw_error_mean _
      | cast i =>
          rw [roundLaw_succ, Law.expect_bind]
          have hinner (k : ℤ) :
              ((roundLaw n (lowerCoefficients n α μ k) (lowerMatrix n μ)).map
                (appendOutcome n α k)).expect
                (fun out => out.2 i.castSucc) = 0 := by
            rw [Law.expect_map]
            simp only [appendOutcome, Fin.snoc_castSucc]
            exact ih (lowerCoefficients n α μ k) (lowerMatrix n μ) i
          simp only [hinner]
          exact Law.expect_const _ _

/-- Each centered orthogonal-coordinate error has second moment at most `1/4`. -/
theorem roundLaw_error_sq_le : ∀ (n : ℕ) (α : Fin n → ℝ)
    (μ : Fin n → Fin n → ℝ) (i : Fin n),
    (roundLaw n α μ).expect (fun out => (out.2 i) ^ 2) ≤ 1 / 4 := by
  intro n
  induction n with
  | zero =>
      intro α μ i
      exact i.elim0
  | succ n ih =>
      intro α μ i
      cases i using Fin.lastCases with
      | last =>
          rw [roundLaw_succ, Law.expect_bind]
          have hinner (k : ℤ) :
              ((roundLaw n (lowerCoefficients n α μ k) (lowerMatrix n μ)).map
                (appendOutcome n α k)).expect
                (fun out => (out.2 (Fin.last n)) ^ 2) =
                  (α (Fin.last n) - (k : ℝ)) ^ 2 := by
            rw [Law.expect_map]
            simp only [appendOutcome, Fin.snoc_last]
            exact Law.expect_const _ _
          simp only [hinner]
          exact scalarLaw_error_sq_le _
      | cast i =>
          rw [roundLaw_succ, Law.expect_bind]
          calc
            _ ≤ (scalarLaw (α (Fin.last n))).expect (fun _ => (1 / 4 : ℝ)) := by
              apply Law.expect_mono
              intro k
              rw [Law.expect_map]
              simp only [appendOutcome, Fin.snoc_castSucc]
              exact ih (lowerCoefficients n α μ k) (lowerMatrix n μ) i
            _ = 1 / 4 := Law.expect_const _ _

/-- Errors from different stages have zero cross moment. -/
theorem roundLaw_cross_zero : ∀ (n : ℕ) (α : Fin n → ℝ)
    (μ : Fin n → Fin n → ℝ) (i j : Fin n), i ≠ j →
    (roundLaw n α μ).expect (fun out => out.2 i * out.2 j) = 0 := by
  intro n
  induction n with
  | zero =>
      intro α μ i j hij
      exact i.elim0
  | succ n ih =>
      intro α μ i j hij
      cases i using Fin.lastCases with
      | last =>
          cases j using Fin.lastCases with
          | last => exact False.elim (hij rfl)
          | cast j =>
              rw [roundLaw_succ, Law.expect_bind]
              have hinner (k : ℤ) :
                  ((roundLaw n (lowerCoefficients n α μ k) (lowerMatrix n μ)).map
                    (appendOutcome n α k)).expect
                    (fun out => out.2 (Fin.last n) * out.2 j.castSucc) = 0 := by
                rw [Law.expect_map]
                simp only [appendOutcome, Fin.snoc_last, Fin.snoc_castSucc]
                calc
                  _ = (α (Fin.last n) - (k : ℝ)) *
                      (roundLaw n (lowerCoefficients n α μ k) (lowerMatrix n μ)).expect
                        (fun out => out.2 j) := by
                      rw [← Law.expect_const_mul]
                  _ = 0 := by rw [roundLaw_error_mean]; ring
              simp only [hinner]
              exact Law.expect_const _ _
      | cast i =>
          cases j using Fin.lastCases with
          | last =>
              rw [roundLaw_succ, Law.expect_bind]
              have hinner (k : ℤ) :
                  ((roundLaw n (lowerCoefficients n α μ k) (lowerMatrix n μ)).map
                    (appendOutcome n α k)).expect
                    (fun out => out.2 i.castSucc * out.2 (Fin.last n)) = 0 := by
                rw [Law.expect_map]
                simp only [appendOutcome, Fin.snoc_castSucc, Fin.snoc_last]
                calc
                  _ = (α (Fin.last n) - (k : ℝ)) *
                      (roundLaw n (lowerCoefficients n α μ k) (lowerMatrix n μ)).expect
                        (fun out => out.2 i) := by
                      rw [← Law.expect_const_mul]
                      apply Law.expect_congr
                      intro out
                      ring
                  _ = 0 := by rw [roundLaw_error_mean]; ring
              simp only [hinner]
              exact Law.expect_const _ _
          | cast j =>
              rw [roundLaw_succ, Law.expect_bind]
              have hij' : i ≠ j := by
                intro h
                exact hij (congrArg Fin.castSucc h)
              have hinner (k : ℤ) :
                  ((roundLaw n (lowerCoefficients n α μ k) (lowerMatrix n μ)).map
                    (appendOutcome n α k)).expect
                    (fun out => out.2 i.castSucc * out.2 j.castSucc) = 0 := by
                rw [Law.expect_map]
                simp only [appendOutcome, Fin.snoc_castSucc]
                exact ih (lowerCoefficients n α μ k) (lowerMatrix n μ) i j hij'
              simp only [hinner]
              exact Law.expect_const _ _

/-- Coordinates of the lattice vector with integer coefficients `z`, written
in the orthogonal `u`-coordinates. The recursive formula is the triangular
change of basis `b_i = u_i + ∑_{j<i} μ_ij u_j`. -/
def latticeCoordinates : (n : ℕ) → (Fin n → Fin n → ℝ) →
    (Fin n → ℤ) → Fin n → ℝ
  | 0, _, _ => Fin.elim0
  | n + 1, μ, z =>
      Fin.snoc
        (fun j => latticeCoordinates n (lowerMatrix n μ) (Fin.init z) j +
          (z (Fin.last n) : ℝ) * μ (Fin.last n) j.castSucc)
        (z (Fin.last n) : ℝ)

theorem latticeCoordinates_succ_cast (n : ℕ)
    (μ : Fin (n + 1) → Fin (n + 1) → ℝ) (z : Fin (n + 1) → ℤ)
    (j : Fin n) :
    latticeCoordinates (n + 1) μ z j.castSucc =
      latticeCoordinates n (lowerMatrix n μ) (Fin.init z) j +
        (z (Fin.last n) : ℝ) * μ (Fin.last n) j.castSucc := by
  simp [latticeCoordinates]

theorem latticeCoordinates_succ_last (n : ℕ)
    (μ : Fin (n + 1) → Fin (n + 1) → ℝ) (z : Fin (n + 1) → ℤ) :
    latticeCoordinates (n + 1) μ z (Fin.last n) = (z (Fin.last n) : ℝ) := by
  simp [latticeCoordinates]

/-- The point of the triangular integer lattice with coefficient tuple `z`. -/
def latticePoint {A : Type*} {n : ℕ} (μ : Fin n → Fin n → ℝ)
    (u : Fin n → A → ℝ) (z : Fin n → ℤ) (a : A) : ℝ :=
  ∑ i : Fin n, latticeCoordinates n μ z i * u i a

/-- Closed form of the recursive triangular change of coordinates. -/
theorem latticeCoordinates_eq_sum_upper : ∀ (n : ℕ)
    (μ : Fin n → Fin n → ℝ) (z : Fin n → ℤ) (j : Fin n),
    latticeCoordinates n μ z j = (z j : ℝ) +
      ∑ i : Fin n, if j < i then (z i : ℝ) * μ i j else 0 := by
  intro n
  induction n with
  | zero =>
      intro μ z j
      exact j.elim0
  | succ n ih =>
      intro μ z j
      cases j using Fin.lastCases with
      | last =>
          rw [latticeCoordinates_succ_last, Fin.sum_univ_castSucc]
          have hlast (i : Fin n) : ¬ Fin.last n < i.castSucc :=
            not_lt.mpr (Fin.le_last _)
          simp [hlast]
      | cast j =>
          rw [latticeCoordinates_succ_cast,
            ih (lowerMatrix n μ) (Fin.init z) j,
            Fin.sum_univ_castSucc]
          simp only [Fin.init, Fin.castSucc_lt_castSucc_iff,
            Fin.castSucc_lt_last, ↓reduceIte]
          simp only [lowerMatrix]
          ring

/-- The explicit triangular basis vector represented by one integer
coefficient. -/
def triangularBasis {A : Type*} {n : ℕ} (μ : Fin n → Fin n → ℝ)
    (u : Fin n → A → ℝ) (i : Fin n) (a : A) : ℝ :=
  u i a + ∑ j ∈ Finset.Iio i, μ i j * u j a

/-- Triangular synthesis has integer coefficients in the explicit basis. -/
theorem latticePoint_eq_sum_basis {A : Type*} (n : ℕ)
    (μ : Fin n → Fin n → ℝ) (u : Fin n → A → ℝ)
    (z : Fin n → ℤ) (a : A) :
    latticePoint μ u z a =
      ∑ i : Fin n, (z i : ℝ) * triangularBasis μ u i a := by
  unfold latticePoint triangularBasis
  simp_rw [latticeCoordinates_eq_sum_upper]
  calc
    (∑ j : Fin n, ((z j : ℝ) + ∑ i : Fin n,
        if j < i then (z i : ℝ) * μ i j else 0) * u j a) =
        (∑ j : Fin n, (z j : ℝ) * u j a) +
          ∑ j : Fin n, (∑ i : Fin n,
            if j < i then (z i : ℝ) * μ i j else 0) * u j a := by
          simp only [add_mul, Finset.sum_add_distrib]
    _ = (∑ i : Fin n, (z i : ℝ) * u i a) +
        ∑ i : Fin n, (z i : ℝ) *
          (∑ j ∈ Finset.Iio i, μ i j * u j a) := by
      congr 1
      calc
        (∑ j : Fin n, (∑ i : Fin n,
        if j < i then (z i : ℝ) * μ i j else 0) * u j a) =
        ∑ i : Fin n, (z i : ℝ) *
          (∑ j : Fin n, if j < i then μ i j * u j a else 0) := by
          simp only [Finset.sum_mul, Finset.mul_sum]
          rw [Finset.sum_comm]
          apply Finset.sum_congr rfl
          intro i hi
          apply Finset.sum_congr rfl
          intro j hj
          split_ifs <;> ring
        _ = ∑ i : Fin n, (z i : ℝ) *
              (∑ j ∈ Finset.Iio i, μ i j * u j a) := by
          apply Finset.sum_congr rfl
          intro i hi
          congr 1
          classical
          rw [← Finset.sum_filter]
          congr 1
          ext j
          simp
    _ = ∑ i : Fin n, (z i : ℝ) *
          (u i a + ∑ j ∈ Finset.Iio i, μ i j * u j a) := by
          simp only [mul_add, Finset.sum_add_distrib]

/-- Every leaf of the recursive law has the advertised integer/error
decomposition in orthogonal coordinates. -/
theorem roundLaw_coordinates : ∀ (n : ℕ) (α : Fin n → ℝ)
    (μ : Fin n → Fin n → ℝ),
    Law.All (fun out => ∀ i : Fin n,
      α i = latticeCoordinates n μ out.1 i + out.2 i) (roundLaw n α μ) := by
  intro n
  induction n with
  | zero =>
      intro α μ
      simp only [roundLaw, Law.All]
      intro i
      exact i.elim0
  | succ n ih =>
      intro α μ
      rw [roundLaw_succ]
      apply Law.all_bind
      intro k
      apply Law.all_map
      change Law.All
        (fun out : Outcome n => ∀ i : Fin (n + 1),
          α i = latticeCoordinates (n + 1) μ (appendOutcome n α k out).1 i +
            (appendOutcome n α k out).2 i)
        (roundLaw n (lowerCoefficients n α μ k) (lowerMatrix n μ))
      apply Law.all_mono
        (roundLaw n (lowerCoefficients n α μ k) (lowerMatrix n μ))
        (fun (out : Outcome n) => ∀ j : Fin n,
          lowerCoefficients n α μ k j =
            latticeCoordinates n (lowerMatrix n μ) out.1 j + out.2 j)
        (fun (out : Outcome n) => ∀ i : Fin (n + 1),
          α i = latticeCoordinates (n + 1) μ (appendOutcome n α k out).1 i +
            (appendOutcome n α k out).2 i)
      · intro out hout i
        cases i using Fin.lastCases with
        | last =>
            simp [appendOutcome, latticeCoordinates_succ_last]
        | cast j =>
            have hj := hout j
            simp only [lowerCoefficients] at hj
            simp only [appendOutcome, latticeCoordinates_succ_cast, Fin.init_snoc,
              Fin.snoc_last, Fin.snoc_castSucc]
            linarith
      · exact ih (lowerCoefficients n α μ k) (lowerMatrix n μ)

/-- The target point expressed in the orthogonal coordinates. -/
def targetPoint {A : Type*} {n : ℕ} (α : Fin n → ℝ)
    (u : Fin n → A → ℝ) (a : A) : ℝ :=
  ∑ i : Fin n, α i * u i a

theorem roundLaw_pointwise_error {A : Type*} (n : ℕ) (α : Fin n → ℝ)
    (μ : Fin n → Fin n → ℝ) (u : Fin n → A → ℝ) (a : A) :
    Law.All (fun out => targetPoint α u a - latticePoint μ u out.1 a =
      ∑ i : Fin n, out.2 i * u i a) (roundLaw n α μ) := by
  apply Law.all_mono (roundLaw n α μ)
    (fun out => ∀ i : Fin n,
      α i = latticeCoordinates n μ out.1 i + out.2 i)
  · intro out h
    unfold targetPoint latticePoint
    rw [← Finset.sum_sub_distrib]
    apply Finset.sum_congr rfl
    intro i hi
    rw [h i]
    ring
  · exact roundLaw_coordinates n α μ

/-- Exact error identity for any concrete triangular presentation. Each leaf
has integer coefficients `out.1`, and the same `out.2` is the centered error
whose moments are bounded below. -/
theorem roundLaw_exact_synthesis {A : Type*} (n : ℕ) (α : Fin n → ℝ)
    (μ : Fin n → Fin n → ℝ) (u b : Fin n → A → ℝ) (x : A → ℝ)
    (hx : ∀ a, x a = targetPoint α u a)
    (hb : ∀ i a, b i a = triangularBasis μ u i a) (a : A) :
    Law.All (fun out => x a - ∑ i : Fin n, (out.1 i : ℝ) * b i a =
      ∑ i : Fin n, out.2 i * u i a) (roundLaw n α μ) := by
  apply Law.all_mono (roundLaw n α μ)
    (fun out => targetPoint α u a - latticePoint μ u out.1 a =
      ∑ i : Fin n, out.2 i * u i a)
  · intro out h
    calc
      x a - ∑ i : Fin n, (out.1 i : ℝ) * b i a =
          targetPoint α u a - latticePoint μ u out.1 a := by
            rw [hx a, latticePoint_eq_sum_basis]
            congr 1
            apply Finset.sum_congr rfl
            intro i hi
            rw [hb i a]
      _ = ∑ i : Fin n, out.2 i * u i a := h
  · exact roundLaw_pointwise_error n α μ u a

/-- The expected pointwise rounding error is zero. -/
theorem roundLaw_point_mean_zero {A : Type*} (n : ℕ) (α : Fin n → ℝ)
    (μ : Fin n → Fin n → ℝ) (u : Fin n → A → ℝ) (a : A) :
    (roundLaw n α μ).expect
      (fun out => targetPoint α u a - latticePoint μ u out.1 a) = 0 := by
  calc
    _ = (roundLaw n α μ).expect (fun out => ∑ i : Fin n, out.2 i * u i a) := by
      apply Law.expect_congr_of_all
      exact roundLaw_pointwise_error n α μ u a
    _ = 0 := by
      apply coordinate_mean_zero
      intro i hi
      exact roundLaw_error_mean n α μ i

/-- Every coordinate of the rounded point obeys the Gram--Schmidt variance
bound; orthogonality is used only when identifying `u` as the Gram--Schmidt
vectors of a concrete lattice basis. -/
theorem roundLaw_point_sq_le {A : Type*} (n : ℕ) (α : Fin n → ℝ)
    (μ : Fin n → Fin n → ℝ) (u : Fin n → A → ℝ) (a : A) :
    (roundLaw n α μ).expect
      (fun out => (targetPoint α u a - latticePoint μ u out.1 a) ^ 2) ≤
        (1 / 4 : ℝ) * ∑ i : Fin n, (u i a) ^ 2 := by
  calc
    _ = (roundLaw n α μ).expect
          (fun out => (∑ i : Fin n, out.2 i * u i a) ^ 2) := by
        apply Law.expect_congr_of_all
        apply Law.all_mono (roundLaw n α μ)
          (fun out => targetPoint α u a - latticePoint μ u out.1 a =
            ∑ i : Fin n, out.2 i * u i a)
        · intro out h
          rw [h]
        · exact roundLaw_pointwise_error n α μ u a
    _ ≤ _ := by
      apply coordinate_second_moment_le
      · intro i hi j hj hij
        exact roundLaw_cross_zero n α μ i j hij
      · intro i hi
        exact roundLaw_error_sq_le n α μ i

/-- Explicit finite-sample form of the lattice-coordinate rounding theorem.
The sample space is `Fin` indexed by the leaves of `roundLaw`; its samples are
integer coefficient tuples, and the real point is their triangular synthesis. -/
theorem finite_lattice_rounding {A : Type*} (n : ℕ) (α : Fin n → ℝ)
    (μ : Fin n → Fin n → ℝ) (u : Fin n → A → ℝ) (a : A) :
    let L := roundLaw n α μ
    (∀ ω : Law.Sample L, 0 ≤ Law.sampleWeight L ω) ∧
      (∑ ω : Law.Sample L, Law.sampleWeight L ω) = 1 ∧
      (∑ ω : Law.Sample L, Law.sampleWeight L ω *
        (targetPoint α u a - latticePoint μ u (Law.sampleValue L ω).1 a)) = 0 ∧
      (∑ ω : Law.Sample L, Law.sampleWeight L ω *
        (targetPoint α u a - latticePoint μ u (Law.sampleValue L ω).1 a) ^ 2) ≤
        (1 / 4 : ℝ) * ∑ i : Fin n, (u i a) ^ 2 := by
  dsimp
  refine ⟨Law.sampleWeight_nonneg _, Law.sampleWeight_sum_one _, ?_, ?_⟩
  · exact (Law.sample_expect (roundLaw n α μ)
      (fun out : Outcome n => targetPoint α u a - latticePoint μ u out.1 a)).trans
        (roundLaw_point_mean_zero n α μ u a)
  · calc
      _ = (roundLaw n α μ).expect
          (fun out => (targetPoint α u a - latticePoint μ u out.1 a) ^ 2) :=
            Law.sample_expect (roundLaw n α μ) _
      _ ≤ _ := roundLaw_point_sq_le n α μ u a

end Erdos.Research.LatticeRounding

import Mathlib.Data.Complex.Basic
import Mathlib.Data.Int.GCD
import Mathlib.Data.Nat.GCD.BigOperators
import Mathlib.Tactic

/-!
# Coprime tensor coordinates for complex root grids

For coprime positive orders, multiplication identifies the product of two
root grids with the root grid of the product order. This module
isolates the algebraic coordinate change needed by an inductive tensor
argument.
-/

namespace Erdos.Research.Problem774.TensorCRT

/-- The complex roots of `X ^ n - 1`, with their exponent equation attached. -/
abbrev RootGrid (n : ℕ) := {z : ℂ // z ^ n = 1}

private theorem root_ne_zero {n : ℕ} (hn : 0 < n) (z : RootGrid n) : (z : ℂ) ≠ 0 := by
  intro hz
  have h := z.property
  simp [hz, hn.ne'] at h

/-- Multiplication takes coprime root coordinates to a root of product order. -/
def multiply (m n : ℕ) : RootGrid m × RootGrid n → RootGrid (m * n) := fun xy =>
  ⟨xy.1.1 * xy.2.1, by
    rw [mul_pow]
    have hx : xy.1.1 ^ (m * n) = 1 := by rw [pow_mul, xy.1.property, one_pow]
    have hy : xy.2.1 ^ (m * n) = 1 := by rw [mul_comm m n, pow_mul, xy.2.property, one_pow]
    rw [hx, hy, one_mul]⟩

private theorem coprime_bezout (m n : ℕ) (h : m.Coprime n) :
    (n : ℤ) * Nat.gcdB m n + (m : ℤ) * Nat.gcdA m n = 1 := by
  have hgcd : m.gcd n = 1 := h
  simpa [hgcd, add_comm] using (Nat.gcd_eq_gcd_ab m n).symm

/-- Explicit CRT inverse using the two Bézout coefficients. -/
noncomputable def split (m n : ℕ) (_h : m.Coprime n) (hm : 0 < m) (hn : 0 < n)
    (z : RootGrid (m * n)) : RootGrid m × RootGrid n :=
  (⟨(z : ℂ) ^ ((n : ℤ) * Nat.gcdB m n), by
      have hz : (z : ℂ) ≠ 0 := root_ne_zero (mul_pos hm hn) z
      rw [← zpow_natCast, ← zpow_mul]
      have hmn : (z : ℂ) ^ (m * n) = 1 := z.property
      rw [show ((n : ℤ) * Nat.gcdB m n) * (m : ℤ) =
        ((m * n : ℕ) : ℤ) * Nat.gcdB m n by push_cast; ring]
      rw [zpow_mul, zpow_natCast, hmn, one_zpow]⟩,
   ⟨(z : ℂ) ^ ((m : ℤ) * Nat.gcdA m n), by
      have hz : (z : ℂ) ≠ 0 := root_ne_zero (mul_pos hm hn) z
      rw [← zpow_natCast, ← zpow_mul]
      have hmn : (z : ℂ) ^ (m * n) = 1 := z.property
      rw [show ((m : ℤ) * Nat.gcdA m n) * (n : ℤ) =
        ((m * n : ℕ) : ℤ) * Nat.gcdA m n by push_cast; ring]
      rw [zpow_mul, zpow_natCast, hmn, one_zpow]⟩)

theorem multiply_split (m n : ℕ) (h : m.Coprime n) (hm : 0 < m) (hn : 0 < n)
    (z : RootGrid (m * n)) : multiply m n (split m n h hm hn z) = z := by
  apply Subtype.ext
  change (z : ℂ) ^ ((n : ℤ) * Nat.gcdB m n) *
    (z : ℂ) ^ ((m : ℤ) * Nat.gcdA m n) = z
  rw [← zpow_add₀ (root_ne_zero (mul_pos hm hn) z), coprime_bezout m n h, zpow_one]

theorem multiply_injective (m n : ℕ) (h : m.Coprime n) (hm : 0 < m) (hn : 0 < n) :
    Function.Injective (multiply m n) := by
  rintro ⟨x₁, y₁⟩ ⟨x₂, y₂⟩ hxy
  have heq : (x₁ : ℂ) * y₁ = (x₂ : ℂ) * y₂ := congrArg Subtype.val hxy
  have hxm : (x₁ : ℂ) ^ m = (x₂ : ℂ) ^ m := by rw [x₁.property, x₂.property]
  have hyn : (y₁ : ℂ) ^ n = (y₂ : ℂ) ^ n := by rw [y₁.property, y₂.property]
  have hxn : (x₁ : ℂ) ^ n = (x₂ : ℂ) ^ n := by
    have hp := congrArg (fun z : ℂ => z ^ n) heq
    simpa [mul_pow, y₁.property, y₂.property] using hp
  have hym : (y₁ : ℂ) ^ m = (y₂ : ℂ) ^ m := by
    have hp := congrArg (fun z : ℂ => z ^ m) heq
    simpa [mul_pow, x₁.property, x₂.property] using hp
  have hxdiv : (x₁ : ℂ) / x₂ = 1 :=
    (pow_eq_one_iff_of_coprime h).mp ⟨by
      rw [div_pow, hxm, div_self (pow_ne_zero m (root_ne_zero hm x₂))], by
      rw [div_pow, hxn, div_self (pow_ne_zero n (root_ne_zero hm x₂))]⟩
  have hydiv : (y₁ : ℂ) / y₂ = 1 :=
    (pow_eq_one_iff_of_coprime h).mp ⟨by
      rw [div_pow, hym, div_self (pow_ne_zero m (root_ne_zero hn y₂))], by
      rw [div_pow, hyn, div_self (pow_ne_zero n (root_ne_zero hn y₂))]⟩
  have hx : x₁ = x₂ := Subtype.ext (by
    exact (div_eq_one_iff_eq (root_ne_zero hm x₂)).mp hxdiv)
  have hy : y₁ = y₂ := Subtype.ext (by
    exact (div_eq_one_iff_eq (root_ne_zero hn y₂)).mp hydiv)
  simp [hx, hy]

/-- Multiplication is a bijection from coprime root grids to their product grid. -/
noncomputable def rootGridEquiv (m n : ℕ) (h : m.Coprime n)
    (hm : 0 < m) (hn : 0 < n) : RootGrid m × RootGrid n ≃ RootGrid (m * n) where
  toFun := multiply m n
  invFun := split m n h hm hn
  left_inv := by
    intro xy
    apply multiply_injective m n h hm hn
    exact multiply_split m n h hm hn (multiply m n xy)
  right_inv := multiply_split m n h hm hn

/-- Set-level form of the coprime tensor coordinate decomposition. -/
theorem rootGrid_product_set (m n : ℕ) (h : m.Coprime n)
    (hm : 0 < m) (hn : 0 < n) :
    {z : ℂ | z ^ (m * n) = 1} =
      {z : ℂ | ∃ x y : ℂ, x ^ m = 1 ∧ y ^ n = 1 ∧ x * y = z} := by
  ext z
  constructor
  · intro hz
    let xy := split m n h hm hn (⟨z, hz⟩ : RootGrid (m * n))
    refine ⟨xy.1, xy.2, xy.1.property, xy.2.property, ?_⟩
    exact congrArg Subtype.val (multiply_split m n h hm hn ⟨z, hz⟩)
  · rintro ⟨x, y, hx, hy, rfl⟩
    change (x * y) ^ (m * n) = 1
    rw [mul_pow]
    have hxm : x ^ (m * n) = 1 := by rw [pow_mul, hx, one_pow]
    have hyn : y ^ (m * n) = 1 := by rw [mul_comm m n, pow_mul, hy, one_pow]
    rw [hxm, hyn, one_mul]

/-- A right-associated tensor product of complex root grids. The empty tensor
factor is the trivial first-root grid. -/
def TensorGrid : List ℕ → Type
  | [] => RootGrid 1
  | m :: ms => RootGrid m × TensorGrid ms

/-- Multiply all tensor coordinates. This map is defined even when the orders
are not coprime; coprimality is needed for bijectivity. -/
def tensorMultiply : (ms : List ℕ) → TensorGrid ms → RootGrid ms.prod
  | [], z => z
  | m :: ms, xy => multiply m ms.prod (xy.1, tensorMultiply ms xy.2)

private theorem list_prod_pos {ms : List ℕ} (hp : ∀ m ∈ ms, 0 < m) : 0 < ms.prod := by
  induction ms with
  | nil => simp
  | cons m ms ih =>
      rw [List.prod_cons]
      apply mul_pos (hp m (by simp))
      apply ih
      intro k hk
      exact hp k (by simp [hk])

/-- Iterating the two-factor CRT equivalence identifies a tensor product of
pairwise coprime root grids with the grid of their product order. In particular,
the coordinate multiplication is injective and surjective. -/
noncomputable def tensorGridEquiv (ms : List ℕ)
    (hp : ∀ m ∈ ms, 0 < m) (hc : ms.Pairwise Nat.Coprime) :
    TensorGrid ms ≃ RootGrid ms.prod := by
  induction ms with
  | nil =>
      exact Equiv.refl (RootGrid 1)
  | cons m ms ih =>
      have hm : 0 < m := hp m (by simp)
      have hp' : ∀ k ∈ ms, 0 < k := by
        intro k hk
        exact hp k (by simp [hk])
      have hc' : ms.Pairwise Nat.Coprime := (List.pairwise_cons.mp hc).2
      have hmc : m.Coprime ms.prod :=
        Nat.coprime_list_prod_right_iff.mpr (List.pairwise_cons.mp hc).1
      exact ((Equiv.refl (RootGrid m)).prodCongr (ih hp' hc')).trans
        (rootGridEquiv m ms.prod hmc hm (list_prod_pos hp'))

theorem tensorGridEquiv_bijective (ms : List ℕ)
    (hp : ∀ m ∈ ms, 0 < m) (hc : ms.Pairwise Nat.Coprime) :
    Function.Bijective (tensorGridEquiv ms hp hc) :=
  (tensorGridEquiv ms hp hc).bijective

theorem tensorGridEquiv_apply (ms : List ℕ)
    (hp : ∀ m ∈ ms, 0 < m) (hc : ms.Pairwise Nat.Coprime)
    (x : TensorGrid ms) : tensorGridEquiv ms hp hc x = tensorMultiply ms x := by
  induction ms with
  | nil => rfl
  | cons m ms ih =>
      rcases x with ⟨xm, xs⟩
      change multiply m ms.prod (xm, tensorGridEquiv ms _ _ xs) =
        multiply m ms.prod (xm, tensorMultiply ms xs)
      rw [ih]

/-- The explicit coordinate multiplication is bijective for pairwise coprime
positive orders. -/
theorem tensorMultiply_bijective (ms : List ℕ)
    (hp : ∀ m ∈ ms, 0 < m) (hc : ms.Pairwise Nat.Coprime) :
    Function.Bijective (tensorMultiply ms) := by
  have heq : tensorMultiply ms = tensorGridEquiv ms hp hc := by
    funext x
    exact (tensorGridEquiv_apply ms hp hc x).symm
  rw [heq]
  exact tensorGridEquiv_bijective ms hp hc

/-- Distinct prime orders supply the coprimality hypotheses for the tensor
equivalence. This is the squarefree prime-grid case. -/
noncomputable def primeTensorGridEquiv (ps : List ℕ)
    (hprime : ∀ p ∈ ps, p.Prime) (hnodup : ps.Nodup) :
    TensorGrid ps ≃ RootGrid ps.prod :=
  tensorGridEquiv ps
    (fun p hp => (hprime p hp).pos)
    (hnodup.pairwise_of_forall_ne fun p hp q hq hpq =>
      (Nat.coprime_primes (hprime p hp) (hprime q hq)).2 hpq)

theorem primeTensorMultiply_bijective (ps : List ℕ)
    (hprime : ∀ p ∈ ps, p.Prime) (hnodup : ps.Nodup) :
    Function.Bijective (tensorMultiply ps) := by
  apply tensorMultiply_bijective ps
  · intro p hp
    exact (hprime p hp).pos
  · exact hnodup.pairwise_of_forall_ne fun p hp q hq hpq =>
      (Nat.coprime_primes (hprime p hp) (hprime q hq)).2 hpq

/-- Finite additive relations can be reindexed exactly through the tensor CRT
coordinates. The coefficient function is pulled back along the inverse
equivalence, so this applies in particular to coefficients in `{0, ±1}`. -/
theorem tensor_additive_sum_reindex (ms : List ℕ)
    (hp : ∀ m ∈ ms, 0 < m) (hc : ms.Pairwise Nat.Coprime)
    (s : Finset (TensorGrid ms)) (a : TensorGrid ms → ℂ) :
    (∑ x ∈ s, a x * (tensorMultiply ms x : ℂ)) =
      ∑ z ∈ s.image (tensorMultiply ms),
        a ((tensorGridEquiv ms hp hc).symm z) * (z : ℂ) := by
  classical
  rw [Finset.sum_image]
  · apply Finset.sum_congr rfl
    intro x _
    have hx : (tensorGridEquiv ms hp hc).symm (tensorMultiply ms x) = x := by
      rw [← tensorGridEquiv_apply ms hp hc x]
      exact Equiv.symm_apply_apply _ _
    rw [hx]
  · intro x _ y _ hxy
    exact (tensorMultiply_bijective ms hp hc).1 hxy

theorem tensor_signed_relation_iff (ms : List ℕ)
    (hp : ∀ m ∈ ms, 0 < m) (hc : ms.Pairwise Nat.Coprime)
    (s : Finset (TensorGrid ms)) (ε : TensorGrid ms → ℤ) :
    (∑ x ∈ s, (ε x : ℂ) * (tensorMultiply ms x : ℂ) = 0) ↔
      (∑ z ∈ s.image (tensorMultiply ms),
        (ε ((tensorGridEquiv ms hp hc).symm z) : ℂ) * (z : ℂ) = 0) := by
  rw [tensor_additive_sum_reindex ms hp hc s (fun x => (ε x : ℂ))]

end Erdos.Research.Problem774.TensorCRT

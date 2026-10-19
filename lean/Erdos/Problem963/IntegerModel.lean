import Mathlib.Algebra.Module.Submodule.Union
import Mathlib.Algebra.Algebra.Rat
import Mathlib.Combinatorics.Additive.Dissociation
import Mathlib.Data.Real.Basic
import Mathlib.Data.Rat.Denumerable
import Mathlib.RingTheory.Localization.FractionRing
import Mathlib.RingTheory.Localization.Integer

/-!
# Integer models of finite real configurations

A rational linear functional separates every distinct pair of subset sums of a
finite real configuration. Clearing its finitely many denominators gives an
injective integer model with exactly the same subset-sum equalities. Thus
dissociation and cardinal estimates can be transferred to real configurations.
-/

namespace Erdos.Problem963

/-- The sum of a subset of a finite real configuration, indexed by the
configuration's subtype. -/
def subsetSum (A : Finset ℝ) (B : Finset A) : ℝ :=
  ∑ a ∈ B, (a.1 : ℝ)

/-- One rational linear functional separates all distinct subset sums of a
finite real configuration. -/
theorem exists_rational_subset_sum_model (A : Finset ℝ) :
    ∃ f : ℝ →ₗ[ℚ] ℚ, ∀ B C : Finset A,
      subsetSum A B = subsetSum A C ↔
        (∑ a ∈ B, f a.1) = ∑ a ∈ C, f a.1 := by
  classical
  let I := {p : Finset A × Finset A // subsetSum A p.1 ≠ subsetSum A p.2}
  let v : I → ℝ := fun p => subsetSum A p.1.1 - subsetSum A p.1.2
  have hv : ∀ p : I, v p ≠ 0 := by
    intro p
    exact sub_ne_zero.mpr p.property
  obtain ⟨f, hf⟩ := Module.exists_dual_forall_apply_ne_zero (K := ℚ) v hv
  refine ⟨f, fun B C => ?_⟩
  have hsum (D : Finset A) : f (subsetSum A D) = ∑ a ∈ D, f a.1 := by
    simp [subsetSum, map_sum]
  constructor
  · intro h
    calc
      (∑ a ∈ B, f a.1) = f (subsetSum A B) := (hsum B).symm
      _ = f (subsetSum A C) := congrArg f h
      _ = ∑ a ∈ C, f a.1 := hsum C
  · intro h
    by_contra hne
    have hbad := hf (⟨(B, C), hne⟩ : I)
    have hmap : f (v (⟨(B, C), hne⟩ : I)) = 0 := by
      change f (subsetSum A B - subsetSum A C) = 0
      rw [map_sub, hsum B, hsum C, h, sub_self]
    exact hbad hmap

/-- Every finite real configuration has an injective integer model preserving
and reflecting all subset-sum equalities. -/
theorem exists_integer_subset_sum_model (A : Finset ℝ) :
    ∃ g : A → ℤ, Function.Injective g ∧ ∀ B C : Finset A,
      subsetSum A B = subsetSum A C ↔
        (∑ a ∈ B, g a) = ∑ a ∈ C, g a := by
  classical
  obtain ⟨f, hf⟩ := exists_rational_subset_sum_model A
  obtain ⟨b, hb⟩ := IsLocalization.exist_integer_multiples
    (nonZeroDivisors ℤ) (Finset.univ : Finset A) (fun a : A => f a.1)
  let g : A → ℤ := fun a => (hb a (Finset.mem_univ a)).choose
  have hg (a : A) : (g a : ℚ) = ((b : ℤ) : ℚ) * f a.1 := by
    simpa [g, Algebra.smul_def] using (hb a (Finset.mem_univ a)).choose_spec
  have hb0 : (((b : ℤ) : ℚ)) ≠ 0 := by
    exact_mod_cast (nonZeroDivisors.coe_ne_zero b)
  have hsum (B : Finset A) :
      ((∑ a ∈ B, g a : ℤ) : ℚ) = ((b : ℤ) : ℚ) * ∑ a ∈ B, f a.1 := by
    simp only [Int.cast_sum, hg, Finset.mul_sum]
  refine ⟨g, ?_, ?_⟩
  · intro a c h
    have h' : (g a : ℚ) = (g c : ℚ) := congrArg (fun z : ℤ => (z : ℚ)) h
    rw [hg, hg] at h'
    have hf' : f a.1 = f c.1 := mul_left_cancel₀ hb0 h'
    have heq := (hf {a} {c}).mpr (by simpa using hf')
    have : a.1 = c.1 := by simpa [subsetSum] using heq
    exact Subtype.ext this
  · intro B C
    rw [hf B C]
    constructor
    · intro h
      apply (Int.cast_inj (α := ℚ)).mp
      rw [hsum B, hsum C]
      exact congrArg (fun q : ℚ => ((b : ℤ) : ℚ) * q) h
    · intro h
      apply mul_left_cancel₀ hb0
      rw [← hsum B, ← hsum C]
      exact congrArg (fun z : ℤ => (z : ℚ)) h

/-- A finite configuration's dissociated subsets are preserved by an injective
relabeling that reflects equality of all subset sums. -/
theorem addDissociated_image_of_subset_sum_reflection
    {ι α β : Type*} [AddCommGroup α] [AddCommGroup β]
    [DecidableEq α] [DecidableEq β]
    (f : ι → α) (g : ι → β) (hf : Function.Injective f) (hg : Function.Injective g)
    (hrel : ∀ B C : Finset ι,
      (∑ x ∈ B, f x) = ∑ x ∈ C, f x ↔ (∑ x ∈ B, g x) = ∑ x ∈ C, g x)
    (S : Finset ι) (hS : AddDissociated (↑(S.image f) : Set α)) :
    AddDissociated (↑(S.image g) : Set β) := by
  classical
  intro T hT U hU hsum
  have hT' : T ⊆ S.image g := by exact_mod_cast hT
  have hU' : U ⊆ S.image g := by exact_mod_cast hU
  obtain ⟨T', hTS, hTeq⟩ := Finset.subset_image_iff.mp hT'
  obtain ⟨U', hUS, hUeq⟩ := Finset.subset_image_iff.mp hU'
  have hsumG : (∑ x ∈ T', g x) = ∑ x ∈ U', g x := by
    calc
      (∑ x ∈ T', g x) = ∑ y ∈ T'.image g, y := by
        rw [Finset.sum_image (fun x _ y _ h => hg h)]
      _ = ∑ y ∈ U'.image g, y := by simpa [hTeq, hUeq] using hsum
      _ = ∑ x ∈ U', g x := by
        rw [Finset.sum_image (fun x _ y _ h => hg h)]
  have hsumF : (∑ x ∈ T', f x) = ∑ x ∈ U', f x := (hrel T' U').mpr hsumG
  have hTF : (↑(T'.image f) : Set α) ⊆ ↑(S.image f) := by
    exact_mod_cast Finset.image_subset_image hTS
  have hUF : (↑(U'.image f) : Set α) ⊆ ↑(S.image f) := by
    exact_mod_cast Finset.image_subset_image hUS
  have hsumF' : (∑ y ∈ T'.image f, y) = ∑ y ∈ U'.image f, y := by
    simpa only [Finset.sum_image (fun x _ y _ h => hf h)] using hsumF
  have hEq := hS hTF hUF hsumF'
  calc
    T = T'.image g := hTeq.symm
    _ = U'.image g := congrArg (Finset.image g) ((Finset.image_inj hf).mp hEq)
    _ = U := hUeq

/-- A cardinal bound expressed in terms of the largest dissociated subset of
an integer set also holds for every finite real set. -/
theorem real_card_bound_of_integer_card_bound
    (hInt : ∀ (S : Finset ℤ) (d : ℕ),
      (∀ B : Finset ℤ, B ⊆ S → AddDissociated (↑B : Set ℤ) → B.card ≤ d) →
        S.card ≤ (d + 1) * 2 ^ d)
    (A : Finset ℝ) (d : ℕ)
    (hA : ∀ B : Finset ℝ, B ⊆ A → AddDissociated (↑B : Set ℝ) → B.card ≤ d) :
    A.card ≤ (d + 1) * 2 ^ d := by
  classical
  obtain ⟨g, hg, hrel⟩ := exists_integer_subset_sum_model A
  let M : Finset ℤ := (Finset.univ : Finset A).image g
  have hMcard : M.card = A.card := by
    dsimp [M]
    rw [Finset.card_image_of_injective _ hg]
    simp
  have hMbound : ∀ B : Finset ℤ, B ⊆ M →
      AddDissociated (↑B : Set ℤ) → B.card ≤ d := by
    intro B hB hDB
    have hB' : B ⊆ (Finset.univ : Finset A).image g := hB
    obtain ⟨T, _, hTeq⟩ := Finset.subset_image_iff.mp hB'
    have hDT : AddDissociated (↑(T.image Subtype.val) : Set ℝ) :=
      addDissociated_image_of_subset_sum_reflection
        g (fun a : A => (a.1 : ℝ)) hg Subtype.val_injective
        (fun X Y => (hrel X Y).symm) T (by simpa only [hTeq] using hDB)
    have hTA : T.image Subtype.val ⊆ A := by
      intro x hx
      obtain ⟨a, _, rfl⟩ := Finset.mem_image.mp hx
      exact a.property
    have hTcard : T.card ≤ d := by
      simpa only [Finset.card_image_of_injective T Subtype.val_injective] using
        hA (T.image Subtype.val) hTA hDT
    simpa only [← hTeq, Finset.card_image_of_injective T hg] using hTcard
  calc
    A.card = M.card := hMcard.symm
    _ ≤ (d + 1) * 2 ^ d := hInt M d hMbound

end Erdos.Problem963

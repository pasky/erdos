import Mathlib.Algebra.Group.Action.Basic
import Mathlib.Algebra.Group.Units.Equiv
import Mathlib.Tactic

/-!
# Averaging over a uniformly distributed family of coordinate permutations

For a fixed coordinate, suppose every other coordinate occurs equally often as
its inverse image under a finite family of permutations. Then the average of
any function of that inverse image is its coordinate average. The proof only
uses the uniform-fiber property, so it also applies to any finite transitive
group action once its equal-size orbit fibers have been established.
-/

namespace Erdos.Research.Problem774.PermutationAverage

open Finset

/-- A finite map with uniformly sized fibers sends a sum to a fixed multiple
of the sum over its codomain. -/
theorem sum_of_uniform_fibers {Ω I : Type*} [Fintype Ω] [Fintype I] [DecidableEq I]
    (f : Ω → I) (r : ℕ)
    (hfiber : ∀ b : I, (Finset.univ.filter fun ω => f ω = b).card = r)
    (V : I → ℝ) :
    (∑ ω : Ω, V (f ω)) = (r : ℝ) * ∑ b : I, V b := by
  classical
  have hpartition :
      (∑ ω : Ω, V (f ω)) =
        ∑ b : I, ∑ ω ∈ (Finset.univ.filter fun ω => f ω = b), V (f ω) := by
    simpa using
      (Finset.sum_fiberwise_eq_sum_filter (Finset.univ : Finset Ω)
        (Finset.univ : Finset I) f (fun ω => V (f ω))).symm
  have hfiberSum (b : I) :
      (∑ ω ∈ (Finset.univ.filter fun ω => f ω = b), V (f ω)) =
        (r : ℝ) * V b := by
    calc
      (∑ ω ∈ (Finset.univ.filter fun ω => f ω = b), V (f ω)) =
          ∑ ω ∈ (Finset.univ.filter fun ω => f ω = b), V b := by
            apply Finset.sum_congr rfl
            intro ω hω
            rw [(Finset.mem_filter.mp hω).2]
      _ = (r : ℝ) * V b := by
        rw [Finset.sum_const, hfiber b]
        simp
  calc
    (∑ ω : Ω, V (f ω)) =
        ∑ b : I, ∑ ω ∈ (Finset.univ.filter fun ω => f ω = b), V (f ω) :=
      hpartition
    _ = ∑ b : I, (r : ℝ) * V b := by
      apply Finset.sum_congr rfl
      intro b _
      exact hfiberSum b
    _ = (r : ℝ) * ∑ b : I, V b := by rw [Finset.mul_sum]

/-- Uniform fibers force the size of the source to be the fiber size times
the size of the target. -/
theorem card_of_uniform_fibers {Ω I : Type*} [Fintype Ω] [Fintype I] [DecidableEq I]
    (f : Ω → I) (r : ℕ)
    (hfiber : ∀ b : I, (Finset.univ.filter fun ω => f ω = b).card = r) :
    Fintype.card Ω = Fintype.card I * r := by
  classical
  have h := Finset.sum_card_fiberwise_eq_card_filter
    (Finset.univ : Finset Ω) (Finset.univ : Finset I) f
  calc
    Fintype.card Ω = ∑ b : I, (Finset.univ.filter fun ω => f ω = b).card := by
      simpa using h.symm
    _ = ∑ _b : I, r := by
      apply Finset.sum_congr rfl
      intro b _
      exact hfiber b
    _ = Fintype.card I * r := by simp

/-- The normalized averaging identity. The explicit positive-fiber premise
avoids division by zero if both finite types are empty. -/
theorem average_of_uniform_fibers {Ω I : Type*} [Fintype Ω] [Fintype I] [DecidableEq I]
    [Nonempty I] (f : Ω → I) (r : ℕ) (hr : 0 < r)
    (hfiber : ∀ b : I, (Finset.univ.filter fun ω => f ω = b).card = r)
    (V : I → ℝ) :
    (∑ ω : Ω, V (f ω)) / (Fintype.card Ω : ℝ) =
      (∑ b : I, V b) / (Fintype.card I : ℝ) := by
  have hcard := card_of_uniform_fibers f r hfiber
  have hI : (Fintype.card I : ℝ) ≠ 0 := by exact_mod_cast Fintype.card_ne_zero
  have hr' : (r : ℝ) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt hr)
  have hcard' : (Fintype.card Ω : ℝ) = (Fintype.card I : ℝ) * r := by
    exact_mod_cast hcard
  rw [sum_of_uniform_fibers f r hfiber V, hcard']
  field_simp

/-- Apply the averaging identity to inverse images under a finite family of
coordinate permutations. -/
theorem average_invPerm {Ω I : Type*} [Fintype Ω] [Fintype I] [DecidableEq I]
    [Nonempty I] (σ : Ω → Equiv.Perm I) (r : ℕ) (hr : 0 < r)
    (hfiber : ∀ a b : I,
      (Finset.univ.filter fun ω => (σ ω).symm a = b).card = r)
    (V : I → ℝ) (a : I) :
    (∑ ω : Ω, V ((σ ω).symm a)) / (Fintype.card Ω : ℝ) =
      (∑ b : I, V b) / (Fintype.card I : ℝ) :=
  average_of_uniform_fibers (fun ω => (σ ω).symm a) r hr (hfiber a) V

/-- Averaging a function over the inverse images of one coordinate under a
finite transitive group action is the same as averaging over all coordinates.
No positivity condition on `V` is needed. -/
theorem average_inv_smul_of_transitive {G I : Type*} [Group G] [Fintype G]
    [MulAction G I] [Fintype I] [Nonempty I]
    (htrans : ∀ a b : I, ∃ g : G, g • a = b)
    (V : I → ℝ) (a : I) :
    (∑ g : G, V (g⁻¹ • a)) / (Fintype.card G : ℝ) =
      (∑ b : I, V b) / (Fintype.card I : ℝ) := by
  let F : I → ℝ := fun b => ∑ g : G, V (g⁻¹ • b)
  have hconst (b : I) : F b = F a := by
    obtain ⟨h, rfl⟩ := htrans a b
    dsimp [F]
    symm
    apply Fintype.sum_equiv (Equiv.mulLeft h)
    intro g
    simp [Equiv.mulLeft, mul_inv_rev, smul_smul]
  have hpermuted (g : G) :
      (∑ b : I, V (g⁻¹ • b)) = ∑ b : I, V b := by
    apply Fintype.sum_equiv (MulAction.toPerm g⁻¹)
    intro b
    rfl
  have hcross :
      (Fintype.card I : ℝ) * F a =
        (Fintype.card G : ℝ) * ∑ b : I, V b := by
    calc
      (Fintype.card I : ℝ) * F a = ∑ b : I, F a := by simp
      _ = ∑ b : I, F b := by
        apply Finset.sum_congr rfl
        intro b _
        exact (hconst b).symm
      _ = ∑ b : I, ∑ g : G, V (g⁻¹ • b) := rfl
      _ = ∑ g : G, ∑ b : I, V (g⁻¹ • b) := Finset.sum_comm
      _ = ∑ g : G, ∑ b : I, V b := by
        apply Finset.sum_congr rfl
        intro g _
        exact hpermuted g
      _ = (Fintype.card G : ℝ) * ∑ b : I, V b := by simp
  have hI : (Fintype.card I : ℝ) ≠ 0 := by
    exact_mod_cast Fintype.card_ne_zero
  have hG : (Fintype.card G : ℝ) ≠ 0 := by
    have : Nonempty G := ⟨1⟩
    exact_mod_cast Fintype.card_ne_zero
  change F a / (Fintype.card G : ℝ) =
    (∑ b : I, V b) / (Fintype.card I : ℝ)
  field_simp [hI, hG]
  nlinarith [hcross]

end Erdos.Research.Problem774.PermutationAverage

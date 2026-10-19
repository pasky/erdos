import Erdos.RootsOfUnitySidon.RootsOfUnitySidon
import Mathlib.Algebra.BigOperators.Ring.List

/-!
# Finite character annihilation on the discrete complex additive group

Every finite set of nonzero complex frequencies is annihilated by a finite,
nonempty list of circle-valued additive characters. Repetitions in the list
encode equal weights, so division by its length gives a finitely supported
probability distribution whose Fourier transform vanishes on the set.
-/

namespace Erdos.Research.Problem774

private noncomputable def parityCharacter : AddChar ℤ Circle where
  toFun n := (-1 : Circle) ^ n
  map_zero_eq_one' := by simp
  map_add_eq_mul' m n := zpow_add _ _ _

/-- For each nonzero frequency there is a character taking value `-1` there. -/
theorem exists_character_eq_neg_one {z : ℂ} (hz : z ≠ 0) :
    ∃ ψ : AddChar ℂ Circle, ψ z = -1 := by
  let f : ℤ →+ ℂ := zmultiplesHom ℂ z
  have hf : Function.Injective f := by
    intro m n h
    have h' : (m : ℂ) * z = (n : ℂ) * z := by
      simpa [f, zsmul_eq_mul] using h
    have hcast : (m : ℂ) = (n : ℂ) := (mul_left_inj' hz).mp h'
    exact_mod_cast hcast
  obtain ⟨ψ, hψ⟩ := extend_circle_character_along f hf parityCharacter
  refine ⟨ψ, ?_⟩
  have hone := hψ 1
  have hfone : f 1 = z := by simp [f]
  simpa [hfone, parityCharacter] using hone

private theorem character_list_twist_sum
    (L : List (AddChar ℂ Circle)) (ψ : AddChar ℂ Circle) (w : ℂ) :
    ((L.map fun χ => χ * ψ).map fun χ => (χ w : ℂ)).sum =
      (L.map fun χ => (χ w : ℂ)).sum * (ψ w : ℂ) := by
  simpa only [List.map_map, Function.comp_def, AddChar.mul_apply, Circle.coe_mul] using
    (List.sum_map_mul_right L (fun χ : AddChar ℂ Circle => (χ w : ℂ)) (ψ w : ℂ))

/-- Equal-weight finite character averaging kills any prescribed finite set
of nonzero frequencies. The list may contain repetitions. -/
theorem exists_character_list_annihilating (A : Finset ℂ) (hzero : 0 ∉ A) :
    ∃ L : List (AddChar ℂ Circle), L ≠ [] ∧
      ∀ z ∈ A, (L.map fun χ => (χ z : ℂ)).sum = 0 := by
  classical
  induction A using Finset.induction_on with
  | empty =>
      refine ⟨[1], by simp, ?_⟩
      simp
  | @insert z A hz ih =>
      have hz0 : z ≠ 0 := by
        intro h
        subst z
        exact hzero (Finset.mem_insert_self _ _)
      have hA0 : 0 ∉ A := by
        intro h
        exact hzero (Finset.mem_insert_of_mem h)
      obtain ⟨L, hL, hvanish⟩ := ih hA0
      obtain ⟨ψ, hψ⟩ := exists_character_eq_neg_one hz0
      refine ⟨L ++ L.map (fun χ => χ * ψ), ?_, ?_⟩
      · intro h
        apply hL
        exact (List.append_eq_nil_iff.mp h).1
      · intro w hw
        have hsum (u : ℂ) :
            ((L ++ L.map fun χ => χ * ψ).map fun χ => (χ u : ℂ)).sum =
              (L.map fun χ => (χ u : ℂ)).sum * (1 + (ψ u : ℂ)) := by
          rw [List.map_append, List.sum_append, character_list_twist_sum]
          ring
        rcases Finset.mem_insert.mp hw with rfl | hwA
        · rw [hsum, hψ]
          simp
        · rw [hsum, hvanish w hwA]
          simp

end Erdos.Research.Problem774

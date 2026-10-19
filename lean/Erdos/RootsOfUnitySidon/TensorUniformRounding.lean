import Erdos.RootsOfUnitySidon.TensorTriangularPresentation
import Erdos.RootsOfUnitySidon.TensorPermutationAverage
import Mathlib.Algebra.Group.Action.Pi
import Mathlib.Tactic

/-!
# Uniformly symmetrized rounding of tensor phase arrays

Randomize the coordinate labels before applying the finite triangular
rounding law, then undo that relabeling on the sampled integer array. The
product permutation action makes the Gram trace bound independent of the
chosen vertex.
-/

namespace Erdos.Research.Problem774.TensorUniformRounding

open Finset
open Erdos.Research
open Erdos.Research.Problem774.TensorGramTrace
open Erdos.Research.Problem774.TensorLatticeRounding
open Erdos.Research.Problem774.TensorTriangularPresentation
open Erdos.Research.Problem774.TensorPermutationAverage

/-- A finite tree law with equal weight on each entry of a list. The default
value only matters for the empty list. -/
noncomputable def uniformList {α : Type*} (default : α) : List α → LatticeRounding.Law α
  | [] => .pure default
  | a :: xs =>
      .mix (1 / ((xs.length + 1 : ℕ) : ℝ))
        (by positivity)
        (by
          have h : (1 : ℝ) ≤ ((xs.length + 1 : ℕ) : ℝ) := by
            exact_mod_cast Nat.succ_le_succ (Nat.zero_le xs.length)
          exact (div_le_iff₀ (by positivity)).2 (by linarith))
        (uniformList default xs) (.pure a)

theorem uniformList_weighted_expect {α : Type*} (default : α)
    (xs : List α) (f : α → ℝ) :
    (xs.length : ℝ) * (uniformList default xs).expect f =
      (xs.map f).sum := by
  induction xs with
  | nil => simp [uniformList]
  | cons a xs ih =>
      have hd : (((xs.length + 1 : ℕ) : ℝ)) ≠ 0 := by positivity
      simp only [List.length_cons, uniformList,
        LatticeRounding.Law.expect_mix, LatticeRounding.Law.expect_pure,
        List.map_cons, List.sum_cons]
      push_cast
      field_simp
      nlinarith [ih]

/-- The uniform finite law on a nonempty finite type. -/
noncomputable def uniformFinite {α : Type*} [Fintype α] [Nonempty α] :
    LatticeRounding.Law α :=
  uniformList (Classical.choice ‹Nonempty α›) (Finset.univ.toList)

theorem uniformFinite_expect {α : Type*} [Fintype α] [Nonempty α]
    (f : α → ℝ) :
    (uniformFinite : LatticeRounding.Law α).expect f =
      (∑ a : α, f a) / (Fintype.card α : ℝ) := by
  classical
  have h := uniformList_weighted_expect
    (Classical.choice ‹Nonempty α›) (Finset.univ.toList) f
  have hlength : (((Finset.univ : Finset α).toList.length : ℕ) : ℝ) =
      (Fintype.card α : ℝ) := by simp
  have hsum : (((Finset.univ : Finset α).toList.map f).sum) = ∑ a : α, f a := by
    change ((((Finset.univ : Finset α).val.toList).map f).sum) =
      (((Finset.univ : Finset α).val.map f).sum)
    exact Multiset.sum_map_toList (Finset.univ.val) f
  have hcard : (Fintype.card α : ℝ) ≠ 0 := by
    exact_mod_cast Fintype.card_ne_zero
  change ((Finset.univ.toList.length : ℝ) *
    (uniformFinite : LatticeRounding.Law α).expect f) = _ at h
  rw [hlength, hsum] at h
  apply (eq_div_iff hcard).2
  calc
    (uniformFinite : LatticeRounding.Law α).expect f * (Fintype.card α : ℝ) =
        (Fintype.card α : ℝ) * (uniformFinite : LatticeRounding.Law α).expect f :=
      mul_comm _ _
    _ = ∑ a : α, f a := h

/-- Pull an array back along a coordinate permutation. -/
def permuteArray {ι : Type*} (n : ι → ℕ)
    (g : TensorPermutation ι n) {R : Type*}
    (X : TensorVertex ι n → R) (p : TensorVertex ι n) : R :=
  X (g • p)

private theorem permute_update {ι : Type*} [DecidableEq ι] (n : ι → ℕ)
    (g : TensorPermutation ι n) (p : TensorVertex ι n)
    (i : ι) (k : Fin (n i + 1)) :
    g • Function.update p i k =
      Function.update (g • p) i ((g i) k) := by
  classical
  funext j
  by_cases h : j = i
  · subst j
    simp [Pi.smul_apply']
  · simp [Pi.smul_apply', h]

/-- Zero sum on coordinate lines is preserved by independent coordinate
permutations. -/
theorem lineZero_permute {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) {R : Type*} [AddCommGroup R]
    (g : TensorPermutation ι n) (X : TensorVertex ι n → R)
    (hX : LineZero n X) : LineZero n (permuteArray n g X) := by
  intro p i
  change (∑ k : Fin (n i + 1), X (g • Function.update p i k)) = 0
  conv_lhs =>
    arg 2
    ext k
    rw [permute_update n g p i k]
  have hsum :
      (∑ k : Fin (n i + 1),
        X (Function.update (g • p) i ((g i) k))) =
        ∑ k : Fin (n i + 1), X (Function.update (g • p) i k) := by
    apply Fintype.sum_equiv (g i)
    intro k
    rfl
  rw [hsum]
  exact hX (g • p) i

/-- A uniform finite mixture of the permuted rounding laws has the same
variance budget at every vertex. -/
theorem finite_uniform_lineZero_rounding {ι : Type*}
    [Fintype ι] [DecidableEq ι] (n : ι → ℕ)
    (X : TensorVertex ι n → ℝ) (hX : LineZero n X) :
    ∃ L : LatticeRounding.Law (TensorVertex ι n → ℤ),
      LatticeRounding.Law.All (LineZero n) L ∧
      ∀ p : TensorVertex ι n,
        L.expect (fun Z => X p - (Z p : ℝ)) = 0 ∧
        L.expect (fun Z => (X p - (Z p : ℝ)) ^ 2) ≤
          (1 / 4 : ℝ) *
            ((∏ i : ι, ((n i : ℝ) +
              ∑ j : Fin (n i), (1 : ℝ) / (j.val + 1 : ℝ))) /
              (Fintype.card (TensorVertex ι n) : ℝ)) := by
  classical
  let Γ := TensorPermutation ι n
  let U : LatticeRounding.Law Γ := uniformFinite
  let Xg (g : Γ) : TensorVertex ι n → ℝ := permuteArray n g X
  let Lg (g : Γ) : LatticeRounding.Law (TensorVertex ι n → ℤ) :=
    (finite_lineZero_rounding n (Xg g)
      (lineZero_permute n g X hX)).choose
  have hLg (g : Γ) :
      LatticeRounding.Law.All (LineZero n) (Lg g) ∧
      ∀ p : TensorVertex ι n,
        (Lg g).expect (fun Z => Xg g p - (Z p : ℝ)) = 0 ∧
        (Lg g).expect (fun Z => (Xg g p - (Z p : ℝ)) ^ 2) ≤
          (1 / 4 : ℝ) * vertexGram n p := by
    exact (finite_lineZero_rounding n (Xg g)
      (lineZero_permute n g X hX)).choose_spec
  let body (g : Γ) : LatticeRounding.Law (TensorVertex ι n → ℤ) :=
    (Lg g).map (permuteArray n g⁻¹)
  let L : LatticeRounding.Law (TensorVertex ι n → ℤ) := U.bind body
  have hback (g : Γ) (p : TensorVertex ι n) :
      g • (g⁻¹ • p) = p := by
    rw [smul_smul, mul_inv_cancel, one_smul]
  have hbodyAll (g : Γ) : LatticeRounding.Law.All (LineZero n) (body g) := by
    exact LatticeRounding.Law.all_map (Lg g) (permuteArray n g⁻¹)
      (LineZero n) (LatticeRounding.Law.all_mono (Lg g)
        (LineZero n)
        (fun Z => LineZero n (permuteArray n g⁻¹ Z))
        (fun Z hZ => lineZero_permute n g⁻¹ Z hZ) (hLg g).1)
  have hbodyMean (g : Γ) (p : TensorVertex ι n) :
      (body g).expect (fun Z => X p - (Z p : ℝ)) = 0 := by
    rw [show body g = (Lg g).map (permuteArray n g⁻¹) from rfl,
      LatticeRounding.Law.expect_map]
    have h := (hLg g).2 (g⁻¹ • p) |>.1
    simpa [Xg, permuteArray, hback] using h
  have hbodyMoment (g : Γ) (p : TensorVertex ι n) :
      (body g).expect (fun Z => (X p - (Z p : ℝ)) ^ 2) ≤
        (1 / 4 : ℝ) * vertexGram n (g⁻¹ • p) := by
    rw [show body g = (Lg g).map (permuteArray n g⁻¹) from rfl,
      LatticeRounding.Law.expect_map]
    have h := (hLg g).2 (g⁻¹ • p) |>.2
    simpa [Xg, permuteArray, hback] using h
  refine ⟨L, ?_, ?_⟩
  · exact LatticeRounding.Law.all_bind U body (LineZero n) hbodyAll
  · intro p
    constructor
    · change (U.bind body).expect (fun Z => X p - (Z p : ℝ)) = 0
      rw [LatticeRounding.Law.expect_bind]
      have hzero : (fun g : Γ =>
          (body g).expect (fun Z => X p - (Z p : ℝ))) = fun _ => 0 := by
        funext g
        exact hbodyMean g p
      rw [hzero]
      exact LatticeRounding.Law.expect_const U 0
    · change (U.bind body).expect (fun Z => (X p - (Z p : ℝ)) ^ 2) ≤ _
      rw [LatticeRounding.Law.expect_bind]
      calc
        U.expect (fun g => (body g).expect
            (fun Z => (X p - (Z p : ℝ)) ^ 2)) ≤
          U.expect (fun g => (1 / 4 : ℝ) * vertexGram n (g⁻¹ • p)) :=
            LatticeRounding.Law.expect_mono U _ _ (fun g => hbodyMoment g p)
        _ = (1 / 4 : ℝ) * U.expect
            (fun g => vertexGram n (g⁻¹ • p)) :=
              LatticeRounding.Law.expect_const_mul U _ _
        _ = (1 / 4 : ℝ) *
            ((∏ i : ι, ((n i : ℝ) +
              ∑ j : Fin (n i), (1 : ℝ) / (j.val + 1 : ℝ))) /
              (Fintype.card (TensorVertex ι n) : ℝ)) := by
                rw [show U = (uniformFinite : LatticeRounding.Law Γ) from rfl,
                  uniformFinite_expect, average_vertexGram]

/-- The phase error `2π(X-Z)` has the uniform variance budget used in the
character extension step. -/
theorem finite_uniform_phase_rounding {ι : Type*}
    [Fintype ι] [DecidableEq ι] (n : ι → ℕ)
    (X : TensorVertex ι n → ℝ) (hX : LineZero n X) :
    ∃ L : LatticeRounding.Law (TensorVertex ι n → ℤ),
      LatticeRounding.Law.All (LineZero n) L ∧
      ∀ p : TensorVertex ι n,
        L.expect (fun Z => (2 * Real.pi) * (X p - (Z p : ℝ))) = 0 ∧
        L.expect (fun Z => ((2 * Real.pi) * (X p - (Z p : ℝ))) ^ 2) ≤
          Real.pi ^ 2 *
            ((∏ i : ι, ((n i : ℝ) +
              ∑ j : Fin (n i), (1 : ℝ) / (j.val + 1 : ℝ))) /
              (Fintype.card (TensorVertex ι n) : ℝ)) := by
  obtain ⟨L, hL, hmom⟩ := finite_uniform_lineZero_rounding n X hX
  refine ⟨L, hL, ?_⟩
  intro p
  obtain ⟨hmean, hsq⟩ := hmom p
  constructor
  · rw [LatticeRounding.Law.expect_const_mul, hmean, mul_zero]
  · have heq :
        L.expect (fun Z => ((2 * Real.pi) * (X p - (Z p : ℝ))) ^ 2) =
          (2 * Real.pi) ^ 2 *
            L.expect (fun Z => (X p - (Z p : ℝ)) ^ 2) := by
      rw [← LatticeRounding.Law.expect_const_mul]
      apply LatticeRounding.Law.expect_congr
      intro Z
      ring
    rw [heq]
    have hpi : 0 ≤ (2 * Real.pi) ^ 2 := sq_nonneg _
    nlinarith [mul_le_mul_of_nonneg_left hsq hpi]

/-- Directly round a real line-zero phase lift, with errors written as the
phase lift minus an integral multiple of `2π`. -/
theorem finite_uniform_phase_lift_rounding {ι : Type*}
    [Fintype ι] [DecidableEq ι] (n : ι → ℕ)
    (FX : TensorVertex ι n → ℝ) (hFX : LineZero n FX) :
    ∃ L : LatticeRounding.Law (TensorVertex ι n → ℤ),
      LatticeRounding.Law.All (LineZero n) L ∧
      ∀ p : TensorVertex ι n,
        L.expect (fun Z => FX p - (2 * Real.pi) * (Z p : ℝ)) = 0 ∧
        L.expect (fun Z => (FX p - (2 * Real.pi) * (Z p : ℝ)) ^ 2) ≤
          Real.pi ^ 2 *
            ((∏ i : ι, ((n i : ℝ) +
              ∑ j : Fin (n i), (1 : ℝ) / (j.val + 1 : ℝ))) /
              (Fintype.card (TensorVertex ι n) : ℝ)) := by
  classical
  let X : TensorVertex ι n → ℝ := fun p => FX p / (2 * Real.pi)
  have hX : LineZero n X := by
    intro p i
    simpa [X, ← Finset.sum_div] using
      congrArg (fun x : ℝ => x / (2 * Real.pi)) (hFX p i)
  obtain ⟨L, hL, hmom⟩ := finite_uniform_phase_rounding n X hX
  refine ⟨L, hL, ?_⟩
  intro p
  have hpi : (2 * Real.pi : ℝ) ≠ 0 := by positivity
  have herr (Z : TensorVertex ι n → ℤ) :
      (2 * Real.pi) * (X p - (Z p : ℝ)) =
        FX p - (2 * Real.pi) * (Z p : ℝ) := by
    dsimp [X]
    field_simp
  simpa only [← herr] using hmom p

end Erdos.Research.Problem774.TensorUniformRounding

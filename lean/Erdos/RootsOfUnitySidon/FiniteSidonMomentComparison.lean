import Erdos.RootsOfUnitySidon.FiniteWeightedMoment

/-!
# Finite Sidon moment comparison

The Sidon interpolation weights compare a polynomial moment with the average
of its randomized-sign moments. The only sampling hypothesis is exact
translation invariance for the finite moment in question; it will be
supplied by the finite orthogonal-character construction.
-/

namespace Erdos.Research.SidonExtraction

open scoped BigOperators

/-- If a finite sample has translation-invariant `n`th polynomial moments,
the Sidon inequality compares the original moment to the average of its
sign-randomized moments. The signs may come from any finite nonempty space. -/
theorem finiteSidonBound_moment_comparison
    (A : Finset ℂ) (K : ℝ) (hK : 0 < K)
    (hA : FiniteSidonBound A K)
    {σ E : Type*} [Fintype E] [Nonempty E]
    (t : Finset σ) (eval : σ → A → ℂ)
    (sign : E → A → ℂ)
    (hsign_sq : ∀ e a, sign e a * sign e a = 1)
    (hsign_norm : ∀ e, ‖sign e‖ ≤ 1)
    (n : ℕ) (hn : 0 < n)
    (hInv : ∀ (d : A → ℂ) (ψ : AddChar ℂ Circle),
      (∑ u ∈ t, ‖∑ a : A, d a * eval u a * (ψ a.1 : ℂ)‖ ^ n) =
      (∑ u ∈ t, ‖∑ a : A, d a * eval u a‖ ^ n))
    (c : A → ℂ) :
    (Fintype.card E : ℝ) *
      (∑ u ∈ t, ‖∑ a : A, c a * eval u a‖ ^ n) ≤
      (2 * K) ^ n *
        ∑ e : E, ∑ u ∈ t,
          ‖∑ a : A, c a * sign e a * eval u a‖ ^ n := by
  classical
  obtain ⟨F, hInterp⟩ := finiteSidonBound_interpolation A K hK hA
  let v : F → A → ℂ := fun ψ a => (ψ.1 a.1 : ℂ)
  let M : E → ℝ := fun e =>
    ∑ u ∈ t, ‖∑ a : A, c a * sign e a * eval u a‖ ^ n
  have hMnonneg (e : E) : 0 ≤ M e :=
    Finset.sum_nonneg fun _ _ => pow_nonneg (norm_nonneg _) _
  have hPoint (e : E) :
      (∑ u ∈ t, ‖∑ a : A, c a * eval u a‖ ^ n) ≤
        (2 * K) ^ n * M e := by
    obtain ⟨w, hw, hwi⟩ := hInterp (sign e)
    have hwK : (∑ ψ : F, ‖w ψ‖) ≤ 2 * K :=
      hw.trans (by
        simpa using mul_le_mul_of_nonneg_left
          (hsign_norm e) (show 0 ≤ 2 * K by positivity))
    let P : F → σ → ℂ := fun ψ u =>
      ∑ a : A, c a * sign e a * eval u a * v ψ a
    have hP (ψ : F) : (∑ u ∈ t, ‖P ψ u‖ ^ n) ≤ M e := by
      have h := hInv (fun a => c a * sign e a) ψ.1
      convert le_of_eq h using 1
    have hWeighted := norm_weighted_moment_sum_le
      (Finset.univ : Finset F) t w P n hn (2 * K) (M e)
      (by positivity) (hMnonneg e) hwK
      (fun ψ _ => hP ψ)
    have hPoly (u : σ) :
        (∑ a : A, c a * eval u a) = ∑ ψ : F, w ψ * P ψ u := by
      simpa [P, v] using
        (polynomial_interpolation_identity c (sign e) (eval u) v w
          (hsign_sq e) hwi)
    simpa only [hPoly] using hWeighted
  calc
    (Fintype.card E : ℝ) *
      (∑ u ∈ t, ‖∑ a : A, c a * eval u a‖ ^ n)
        = ∑ e : E, (∑ u ∈ t, ‖∑ a : A, c a * eval u a‖ ^ n) := by simp
    _ ≤ ∑ e : E, (2 * K) ^ n * M e :=
      Finset.sum_le_sum fun e _ => hPoint e
    _ = (2 * K) ^ n * ∑ e : E, M e := by rw [Finset.mul_sum]
    _ = _ := rfl

/-- The complex-valued Rademacher signs indexed by a finite frequency set. -/
def rademacherSign {A : Finset ℂ} (ω : A → Bool) (a : A) : ℂ :=
  if ω a then 1 else -1

private theorem rademacherSign_sq {A : Finset ℂ}
    (ω : A → Bool) (a : A) :
    rademacherSign ω a * rademacherSign ω a = 1 := by
  cases h : ω a <;> simp [rademacherSign, h]

private theorem rademacherSign_norm_le_one {A : Finset ℂ}
    (ω : A → Bool) : ‖rademacherSign ω‖ ≤ 1 := by
  apply (pi_norm_le_iff_of_nonneg zero_le_one).mpr
  intro a
  cases h : ω a <;> simp [rademacherSign, h]

/-- The concrete sign-family version of `finiteSidonBound_moment_comparison`.
Its sample translation-invariance hypothesis is supplied by
`FiniteMomentOrthogonality.sampled_even_moment_invariant`. -/
theorem finiteSidonBound_rademacher_moment_comparison
    (A : Finset ℂ) (K : ℝ) (hK : 0 < K)
    (hA : FiniteSidonBound A K)
    {σ : Type*} (t : Finset σ) (eval : σ → A → ℂ)
    (n : ℕ) (hn : 0 < n)
    (hInv : ∀ (d : A → ℂ) (ψ : AddChar ℂ Circle),
      (∑ u ∈ t, ‖∑ a : A, d a * eval u a * (ψ a.1 : ℂ)‖ ^ n) =
      (∑ u ∈ t, ‖∑ a : A, d a * eval u a‖ ^ n))
    (c : A → ℂ) :
    (Fintype.card (A → Bool) : ℝ) *
      (∑ u ∈ t, ‖∑ a : A, c a * eval u a‖ ^ n) ≤
      (2 * K) ^ n *
        ∑ ω : A → Bool, ∑ u ∈ t,
          ‖∑ a : A, c a * rademacherSign ω a * eval u a‖ ^ n := by
  classical
  exact finiteSidonBound_moment_comparison A K hK hA t eval
    rademacherSign
    (fun ω a => rademacherSign_sq ω a)
    rademacherSign_norm_le_one n hn hInv c

end Erdos.Research.SidonExtraction

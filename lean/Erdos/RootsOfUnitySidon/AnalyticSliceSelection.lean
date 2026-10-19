import Erdos.RootsOfUnitySidon.RootsOfUnitySidon

/-!
# Analytic selection of a finite frequency slice

Suppose a finite-valued map partitions frequencies into slices, each of which
has a positive-real Sidon bound. A finite character average that is trivial on
one chosen slice and annihilates all other frequencies lets us retain just the
largest slice, losing at most the number of slices in the constant.
-/

namespace Erdos.Research.Problem774

/-- Positive-real Sidon bound on a subset of an arbitrary discrete additive
group. The coefficients remain complex and characters are circle-valued. -/
def PositiveRealBoundOn {G : Type*} [AddCommGroup G] (s : Set G) (K : ℝ) : Prop :=
  ∀ A : Finset G, (↑A : Set G) ⊆ s → ∀ c : G → ℂ,
    ∃ χ : AddChar G Circle,
      (∑ z ∈ A, ‖c z‖) ≤
        K * (∑ z ∈ A, c z * (χ z : ℂ)).re

/-- Finite character averages separating a selected slice from the other
frequencies of any finite set. Repeated characters are allowed through the
index type `Fin n`. -/
def SliceAnnihilationOn {G ι : Type*} [AddCommGroup G] [Fintype ι]
    (s : Set G) (f : G → ι) : Prop :=
  ∀ A : Finset G, (↑A : Set G) ⊆ s → ∀ i : ι,
    ∃ n : ℕ, 0 < n ∧ ∃ η : Fin n → AddChar G Circle,
      (∀ j : Fin n, ∀ z ∈ A, f z = i → η j z = 1) ∧
      (∀ z ∈ A, f z ≠ i → (∑ j : Fin n, (η j z : ℂ)) = 0)

/-- Retain one large slice using character averaging. A positive-real bound on
each slice can be obtained from a tail bound through a character-preserving
scalar or direct-summand embedding. -/
theorem positiveRealBoundOn_of_averaged_slices {G ι : Type*}
    [AddCommGroup G] [Fintype ι]
    (s : Set G) (f : G → ι) (K : ℝ) (hK : 0 ≤ K)
    (hfiber : ∀ i : ι, PositiveRealBoundOn {z | z ∈ s ∧ f z = i} K)
    (haverage : SliceAnnihilationOn s f) :
    PositiveRealBoundOn s ((Fintype.card ι : ℝ) * K) := by
  classical
  intro A hA c
  by_cases hA0 : A = ∅
  · subst A
    refine ⟨1, ?_⟩
    simp
  obtain ⟨z, hz⟩ := Finset.nonempty_iff_ne_empty.mpr hA0
  let Ai (i : ι) : Finset G := A.filter (fun w => f w = i)
  let mass (i : ι) : ℝ := ∑ w ∈ Ai i, ‖c w‖
  let total : ℝ := ∑ w ∈ A, ‖c w‖
  have hcount : total = ∑ i : ι, mass i := by
    simpa [total, mass, Ai] using
      (Finset.sum_fiberwise_eq_sum_filter A Finset.univ f (fun w => ‖c w‖)).symm
  have hnonempty : (Finset.univ : Finset ι).Nonempty :=
    ⟨f z, Finset.mem_univ _⟩
  have hsum : (∑ _i : ι, total) ≤
      ∑ i : ι, (Fintype.card ι : ℝ) * mass i := by
    calc
      (∑ _i : ι, total) = (Fintype.card ι : ℝ) * total := by simp
      _ = (Fintype.card ι : ℝ) * (∑ i : ι, mass i) := by rw [← hcount]
      _ ≤ ∑ i : ι, (Fintype.card ι : ℝ) * mass i := by
        rw [Finset.mul_sum]
  obtain ⟨i, _, hlarge⟩ := Finset.exists_le_of_sum_le hnonempty hsum
  have hAi : (↑(Ai i) : Set G) ⊆ {w | w ∈ s ∧ f w = i} := by
    intro w hw
    exact ⟨hA (Finset.mem_filter.mp hw).1, (Finset.mem_filter.mp hw).2⟩
  obtain ⟨χ, hχ⟩ := hfiber i (Ai i) hAi c
  obtain ⟨n, hn, η, htrivial, hkill⟩ := haverage A hA i
  let sliceSum : ℂ := ∑ w ∈ Ai i, c w * (χ w : ℂ)
  let fullSum (j : Fin n) : ℂ :=
    ∑ w ∈ A, c w * (((χ * η j) w : Circle) : ℂ)
  have htwist (j : Fin n) (w : G) :
      (((χ * η j) w : Circle) : ℂ) = (χ w : ℂ) * (η j w : ℂ) := by
    rw [AddChar.mul_apply, Circle.coe_mul]
  have haverage_complex :
      (∑ j : Fin n, fullSum j) = (n : ℂ) * sliceSum := by
    calc
      (∑ j : Fin n, fullSum j) =
          ∑ w ∈ A, ∑ j : Fin n, c w * (((χ * η j) w : Circle) : ℂ) := by
        simp only [fullSum]
        rw [Finset.sum_comm]
      _ = ∑ w ∈ A, (c w * (χ w : ℂ)) * ∑ j : Fin n, (η j w : ℂ) := by
        apply Finset.sum_congr rfl
        intro w hw
        calc
          (∑ j : Fin n, c w * (((χ * η j) w : Circle) : ℂ)) =
              ∑ j : Fin n, (c w * (χ w : ℂ)) * (η j w : ℂ) := by
            apply Finset.sum_congr rfl
            intro j _
            rw [htwist]
            ring
          _ = (c w * (χ w : ℂ)) * ∑ j : Fin n, (η j w : ℂ) := by
            rw [Finset.mul_sum]
      _ = ∑ w ∈ A, if f w = i then (n : ℂ) * (c w * (χ w : ℂ)) else 0 := by
        apply Finset.sum_congr rfl
        intro w hw
        by_cases hwi : f w = i
        · have hη : (∑ j : Fin n, (η j w : ℂ)) = (n : ℂ) := by
            calc
              (∑ j : Fin n, (η j w : ℂ)) = ∑ _j : Fin n, (1 : ℂ) := by
                apply Finset.sum_congr rfl
                intro j _
                simp [htrivial j w hw hwi]
              _ = (n : ℂ) := by simp
          simp [hwi, hη, mul_comm]
        · simp [hwi, hkill w hw hwi]
      _ = ∑ w ∈ Ai i, (n : ℂ) * (c w * (χ w : ℂ)) := by
        simp [Ai, Finset.sum_ite]
      _ = (n : ℂ) * sliceSum := by
        rw [Finset.mul_sum]
  have haverage_real :
      (∑ j : Fin n, (fullSum j).re) = (n : ℝ) * sliceSum.re := by
    have h := congrArg Complex.re haverage_complex
    simpa [Complex.re_sum, Complex.mul_re] using h
  have hnonempty_n : (Finset.univ : Finset (Fin n)).Nonempty :=
    ⟨⟨0, hn⟩, Finset.mem_univ _⟩
  have hsum_real : (∑ _j : Fin n, sliceSum.re) ≤
      ∑ j : Fin n, (fullSum j).re := by
    rw [haverage_real]
    simp
  obtain ⟨j, _, hj⟩ := Finset.exists_le_of_sum_le hnonempty_n hsum_real
  refine ⟨χ * η j, ?_⟩
  have hnonneg : 0 ≤ (Fintype.card ι : ℝ) * K :=
    mul_nonneg (Nat.cast_nonneg _) hK
  calc
    (∑ w ∈ A, ‖c w‖) = total := rfl
    _ ≤ (Fintype.card ι : ℝ) * mass i := hlarge
    _ ≤ (Fintype.card ι : ℝ) * (K * sliceSum.re) :=
      mul_le_mul_of_nonneg_left hχ (Nat.cast_nonneg _)
    _ = ((Fintype.card ι : ℝ) * K) * sliceSum.re := by ring
    _ ≤ ((Fintype.card ι : ℝ) * K) * (fullSum j).re :=
      mul_le_mul_of_nonneg_left hj hnonneg
    _ = ((Fintype.card ι : ℝ) * K) *
        (∑ w ∈ A, c w * (((χ * η j) w : Circle) : ℂ)).re := rfl

/-- The complex-frequency specialization, definitionally agreeing with the
root-of-unity project's `PositiveRealBound`. -/
def SliceAnnihilation {ι : Type*} [Fintype ι] (s : Set ℂ) (f : ℂ → ι) : Prop :=
  SliceAnnihilationOn s f

theorem positiveRealBound_of_averaged_slices {ι : Type*} [Fintype ι]
    (s : Set ℂ) (f : ℂ → ι) (K : ℝ) (hK : 0 ≤ K)
    (hfiber : ∀ i : ι, PositiveRealBound {z | z ∈ s ∧ f z = i} K)
    (haverage : SliceAnnihilation s f) :
    PositiveRealBound s ((Fintype.card ι : ℝ) * K) := by
  exact positiveRealBoundOn_of_averaged_slices s f K hK hfiber haverage

end Erdos.Research.Problem774

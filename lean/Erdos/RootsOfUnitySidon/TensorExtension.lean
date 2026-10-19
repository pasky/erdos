import Erdos.RootsOfUnitySidon.TensorPhaseBound
import Erdos.RootsOfUnitySidon.SimplexTorus
import Mathlib.Algebra.Group.AddChar
import Mathlib.Data.Finset.Max
import Mathlib.Tactic

/-!
# A one-step positive-real tensor estimate

The random-lift input is deliberately explicit: for a prescribed tuple of
base characters, finitely many corrected phase tuples are realizable in the
new tensor torus, with nonnegative probabilities, zero coordinate means, and
a uniform coordinate second-moment bound. The theorem below turns this input
and a positive-real bound for the base frequencies into the bound after
adjoining a simplex side. The simplex torus realization is supplied by
`SimplexTorus.realize_phases` in the concrete prime-grid application.
-/

namespace Erdos.Research.TensorExtension

open Erdos.Research.TensorPhaseBound

/-- A positive-real Sidon parameter for a finite set of base frequencies. -/
def PositiveRealParameter {G : Type*} [AddCommGroup G]
    (E : Finset G) (ρ : ℝ) : Prop :=
  ∀ a : G → ℂ, ∃ χ : AddChar G Circle,
    ρ * (∑ g ∈ E, ‖a g‖) ≤
      (∑ g ∈ E, a g * (χ g : ℂ)).re

/-- Averaging the phase estimate over finitely many coefficients. -/
theorem weighted_phase_div_sum_lower {β Ω : Type*}
    (A : Finset β) (s : Finset Ω) (w : Ω → ℝ)
    (z : β → ℂ) (t : Ω → β → ℝ) (Q q : ℝ)
    (hw : ∀ ω ∈ s, 0 ≤ w ω)
    (hweight : (∑ ω ∈ s, w ω) = 1)
    (hmean : ∀ b ∈ A, (∑ ω ∈ s, w ω * t ω b) = 0)
    (hmoment : ∀ b ∈ A, (∑ ω ∈ s, w ω * (t ω b) ^ 2) ≤ Q)
    (hq : 0 < q) :
    (∑ b ∈ A, (z b).re) - 3 * Q / q ^ 2 * (∑ b ∈ A, ‖z b‖) ≤
      ∑ ω ∈ s, w ω *
        (∑ b ∈ A, (z b * Complex.exp
          (Complex.I * (((t ω b) / q : ℝ) : ℂ))).re) := by
  have hpoint (b : β) (hb : b ∈ A) :=
    weighted_phase_div_lower s w (fun ω => t ω b) (z b) Q q
      hw hweight (hmean b hb) (hmoment b hb) hq
  have hsum :
      (∑ b ∈ A, ((z b).re - 3 * ‖z b‖ * Q / q ^ 2)) ≤
        ∑ b ∈ A, ∑ ω ∈ s, w ω *
          (z b * Complex.exp (Complex.I * (((t ω b) / q : ℝ) : ℂ))).re := by
    apply Finset.sum_le_sum
    intro b hb
    exact hpoint b hb
  calc
    _ = ∑ b ∈ A, ((z b).re - 3 * ‖z b‖ * Q / q ^ 2) := by
      rw [Finset.sum_sub_distrib]
      simp only [Finset.mul_sum]
      congr 1
      apply Finset.sum_congr rfl
      intro b hb
      ring
    _ ≤ ∑ b ∈ A, ∑ ω ∈ s, w ω *
          (z b * Complex.exp (Complex.I * (((t ω b) / q : ℝ) : ℂ))).re := hsum
    _ = _ := by
      rw [Finset.sum_comm]
      apply Finset.sum_congr rfl
      intro ω hω
      rw [Finset.mul_sum]

/-- A finite weighted average never exceeds every sampled value. -/
theorem exists_sample_ge_average {Ω : Type*} (s : Finset Ω)
    (w f : Ω → ℝ) (hw : ∀ ω ∈ s, 0 ≤ w ω)
    (hweight : (∑ ω ∈ s, w ω) = 1) :
    ∃ ω ∈ s, (∑ i ∈ s, w i * f i) ≤ f ω := by
  classical
  have hs : s.Nonempty := by
    by_contra h
    have : s = ∅ := Finset.not_nonempty_iff_eq_empty.mp h
    simp [this] at hweight
  obtain ⟨ω, hω, hmax⟩ := Finset.exists_max_image s f hs
  refine ⟨ω, hω, ?_⟩
  calc
    _ ≤ ∑ i ∈ s, w i * f ω := by
      apply Finset.sum_le_sum
      intro i hi
      exact mul_le_mul_of_nonneg_left (hmax i hi) (hw i hi)
    _ = f ω := by rw [← Finset.sum_mul, hweight, one_mul]

/-- The analytic one-step tensor extension. `freq g j` is the tensor frequency
indexed by `(g,j)`, and `η` is an additive character of its ambient group.

The lift hypothesis says that an independently optimized tuple of base
characters can be corrected by one common random phase in each old frequency
coordinate. Every sampled corrected tuple must be realizable by an admissible
target character. The coordinate variance bound `Q` is uniform in the tuple. -/
theorem positiveRealParameter_tensor_step
    {G Ω H : Type*} [AddCommGroup G] [AddCommGroup H]
    (E : Finset G) (q : ℕ) (hq : 0 < q) (Q ρ : ℝ)
    (freq : G → Fin q → H)
    (hbase : PositiveRealParameter E ρ)
    (hlift : ∀ χ : Fin q → AddChar G Circle,
      ∃ (s : Finset Ω) (w : Ω → ℝ) (t : Ω → G → ℝ),
        (∀ ω ∈ s, 0 ≤ w ω) ∧
        (∑ ω ∈ s, w ω) = 1 ∧
        (∀ g ∈ E, (∑ ω ∈ s, w ω * t ω g) = 0) ∧
        (∀ g ∈ E, (∑ ω ∈ s, w ω * (t ω g) ^ 2) ≤ Q) ∧
        (∀ ω ∈ s, ∃ η : AddChar H Circle, ∀ g ∈ E, ∀ j : Fin q,
          (η (freq g j) : ℂ) = (χ j g : ℂ) * Complex.exp
            (Complex.I * (((t ω g) / (q : ℝ) : ℝ) : ℂ)))) :
    ∀ c : G → Fin q → ℂ,
      ∃ η : AddChar H Circle,
        (ρ - 3 * Q / (q : ℝ) ^ 2) *
          (∑ j : Fin q, ∑ g ∈ E, ‖c g j‖) ≤
          (∑ j : Fin q, ∑ g ∈ E, c g j * (η (freq g j) : ℂ)).re := by
  classical
  intro c
  have hqreal : (0 : ℝ) < q := by exact_mod_cast hq
  have hχ (j : Fin q) := hbase (fun g => c g j)
  let χ : Fin q → AddChar G Circle := fun j => Classical.choose (hχ j)
  have hχbound (j : Fin q) :
      ρ * (∑ g ∈ E, ‖c g j‖) ≤
        (∑ g ∈ E, c g j * (χ j g : ℂ)).re := Classical.choose_spec (hχ j)
  obtain ⟨s, w, t, hw, hweight, hmean, hmoment, hrealize⟩ := hlift χ
  let A : Finset (G × Fin q) := E.product Finset.univ
  let z : G × Fin q → ℂ := fun b => c b.1 b.2 * (χ b.2 b.1 : ℂ)
  let phase : Ω → G × Fin q → ℝ := fun ω b => t ω b.1
  have hmeanA (b : G × Fin q) (hb : b ∈ A) :
      (∑ ω ∈ s, w ω * phase ω b) = 0 := by
    exact hmean b.1 (Finset.mem_product.mp hb).1
  have hmomentA (b : G × Fin q) (hb : b ∈ A) :
      (∑ ω ∈ s, w ω * (phase ω b) ^ 2) ≤ Q := by
    exact hmoment b.1 (Finset.mem_product.mp hb).1
  have hphase := weighted_phase_div_sum_lower A s w z phase Q (q : ℝ)
    hw hweight hmeanA hmomentA hqreal
  let f : Ω → ℝ := fun ω => ∑ b ∈ A,
    (z b * Complex.exp (Complex.I * (((phase ω b) / (q : ℝ) : ℝ) : ℂ))).re
  obtain ⟨ω, hω, hsample⟩ := exists_sample_ge_average s w f hw hweight
  obtain ⟨η, hη⟩ := hrealize ω hω
  refine ⟨η, ?_⟩
  have hnorm : (∑ b ∈ A, ‖z b‖) =
      ∑ j : Fin q, ∑ g ∈ E, ‖c g j‖ := by
    calc
      _ = ∑ g ∈ E, ∑ j : Fin q, ‖z (g, j)‖ :=
        Finset.sum_product E Finset.univ (fun b => ‖z b‖)
      _ = ∑ g ∈ E, ∑ j : Fin q, ‖c g j‖ := by
        simp only [z, norm_mul, Circle.norm_coe, mul_one]
      _ = _ := Finset.sum_comm
  have hbase_sum :
      ρ * (∑ j : Fin q, ∑ g ∈ E, ‖c g j‖) ≤
        ∑ b ∈ A, (z b).re := by
    calc
      _ = ∑ j : Fin q, ρ * (∑ g ∈ E, ‖c g j‖) := by rw [Finset.mul_sum]
      _ ≤ ∑ j : Fin q, (∑ g ∈ E, c g j * (χ j g : ℂ)).re := by
        apply Finset.sum_le_sum
        intro j hj
        exact hχbound j
      _ = ∑ j : Fin q, ∑ g ∈ E, (z (g, j)).re := by
        simp only [Complex.re_sum]
        rfl
      _ = ∑ g ∈ E, ∑ j : Fin q, (z (g, j)).re := Finset.sum_comm
      _ = _ := (Finset.sum_product E Finset.univ (fun b => (z b).re)).symm
  have htarget : f ω =
      (∑ j : Fin q, ∑ g ∈ E, c g j * (η (freq g j) : ℂ)).re := by
    calc
      f ω = ∑ g ∈ E, ∑ j : Fin q,
          (z (g, j) * Complex.exp
            (Complex.I * (((phase ω (g, j)) / (q : ℝ) : ℝ) : ℂ))).re :=
        Finset.sum_product E Finset.univ (fun b =>
          (z b * Complex.exp
            (Complex.I * (((phase ω b) / (q : ℝ) : ℝ) : ℂ))).re)
      _ = ∑ j : Fin q, ∑ g ∈ E, (c g j * (η (freq g j) : ℂ)).re := by
        rw [Finset.sum_comm]
        apply Finset.sum_congr rfl
        intro j hj
        apply Finset.sum_congr rfl
        intro g hg
        rw [hη g hg j]
        simp only [z, phase]
        ring
      _ = _ := by simp only [Complex.re_sum]
  have hphase' :
      (∑ b ∈ A, (z b).re) - 3 * Q / (q : ℝ) ^ 2 * (∑ b ∈ A, ‖z b‖) ≤
        ∑ i ∈ s, w i * f i := hphase
  calc
    (ρ - 3 * Q / (q : ℝ) ^ 2) *
        (∑ j : Fin q, ∑ g ∈ E, ‖c g j‖) =
      ρ * (∑ j : Fin q, ∑ g ∈ E, ‖c g j‖) -
        3 * Q / (q : ℝ) ^ 2 * (∑ j : Fin q, ∑ g ∈ E, ‖c g j‖) := by ring
    _ ≤ (∑ b ∈ A, (z b).re) -
        3 * Q / (q : ℝ) ^ 2 * (∑ b ∈ A, ‖z b‖) := by
      rw [hnorm]
      linarith [hbase_sum]
    _ ≤ ∑ i ∈ s, w i * f i := hphase'
    _ ≤ f ω := hsample
    _ = _ := htarget

end Erdos.Research.TensorExtension

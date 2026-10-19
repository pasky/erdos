import Erdos.RootsOfUnitySidon.TensorUniformRounding
import Erdos.RootsOfUnitySidon.TensorStageMoment
import Erdos.RootsOfUnitySidon.TensorRealCharacter
import Mathlib.Tactic

/-!
# Concrete finite moment laws for tensor stages

The uniformly symmetrized rounding law gives integer arrays. Coordinate-line
zero sums turn each such array into an integer additive homomorphism on the
free tensor lattice. Pushing the finite tree law forward gives exactly the
finite weighted law required by the stage extension theorem.
-/

namespace Erdos.Research.Problem774.TensorUniformStageMoment

open Finset
open Erdos.Research
open Erdos.Research.Problem774.TensorPhaseLattice
open Erdos.Research.Problem774.TensorGramTrace
open Erdos.Research.Problem774.TensorLatticeRounding
open Erdos.Research.Problem774.TensorUniformRounding
open Erdos.Research.Problem774.TensorStageMoment

/-- Push a finite tree law through a map, collecting repeated outputs into
one finite support point with the sum of their weights. -/
private theorem finite_pushforward {α β : Type*} [DecidableEq β]
    (L : LatticeRounding.Law α) (φ : α → β) :
    ∃ (s : Finset β) (w : β → ℝ),
      (∀ b ∈ s, 0 ≤ w b) ∧
      (∑ b ∈ s, w b) = 1 ∧
      (∀ f : β → ℝ,
        (∑ b ∈ s, w b * f b) = L.expect (fun a => f (φ a))) := by
  classical
  let ψ : LatticeRounding.Law.Sample L → β :=
    fun ω => φ (LatticeRounding.Law.sampleValue L ω)
  let s : Finset β := (Finset.univ : Finset (LatticeRounding.Law.Sample L)).image ψ
  let w : β → ℝ := fun b =>
    ∑ ω ∈ (Finset.univ.filter fun ω : LatticeRounding.Law.Sample L => ψ ω = b),
      LatticeRounding.Law.sampleWeight L ω
  have hcover (ω : LatticeRounding.Law.Sample L) : ψ ω ∈ s :=
    Finset.mem_image.mpr ⟨ω, Finset.mem_univ _, rfl⟩
  have hpartition (h : LatticeRounding.Law.Sample L → ℝ) :
      (∑ b ∈ s,
        ∑ ω ∈ (Finset.univ.filter fun ω : LatticeRounding.Law.Sample L => ψ ω = b),
          h ω) = ∑ ω : LatticeRounding.Law.Sample L, h ω := by
    have h0 := Finset.sum_fiberwise_eq_sum_filter
      (Finset.univ : Finset (LatticeRounding.Law.Sample L)) s ψ h
    have hfilter :
        (Finset.univ.filter fun ω : LatticeRounding.Law.Sample L => ψ ω ∈ s) =
          Finset.univ := by
      ext ω
      simp [hcover ω]
    simpa only [hfilter] using h0
  refine ⟨s, w, ?_, ?_, ?_⟩
  · intro b _
    exact Finset.sum_nonneg (fun ω _ => LatticeRounding.Law.sampleWeight_nonneg L ω)
  · change (∑ b ∈ s,
        ∑ ω ∈ (Finset.univ.filter fun ω : LatticeRounding.Law.Sample L => ψ ω = b),
          LatticeRounding.Law.sampleWeight L ω) = 1
    rw [hpartition]
    exact LatticeRounding.Law.sampleWeight_sum_one L
  · intro f
    calc
      (∑ b ∈ s, w b * f b) =
          ∑ b ∈ s,
            ∑ ω ∈ (Finset.univ.filter fun ω : LatticeRounding.Law.Sample L => ψ ω = b),
              LatticeRounding.Law.sampleWeight L ω * f (ψ ω) := by
        apply Finset.sum_congr rfl
        intro b _
        rw [show w b = ∑ ω ∈ (Finset.univ.filter
          fun ω : LatticeRounding.Law.Sample L => ψ ω = b),
            LatticeRounding.Law.sampleWeight L ω from rfl, Finset.sum_mul]
        apply Finset.sum_congr rfl
        intro ω hω
        rw [(Finset.mem_filter.mp hω).2]
      _ = ∑ ω : LatticeRounding.Law.Sample L,
            LatticeRounding.Law.sampleWeight L ω * f (ψ ω) := hpartition _
      _ = L.expect (fun a => f (φ a)) := by
        simpa only [ψ] using
          (LatticeRounding.Law.sample_expect L (fun a => f (φ a)))

/-- An integer array gives an integer additive homomorphism whenever its
coordinate-line sums vanish. Outside that subspace, choose the zero hom. -/
noncomputable def arrayHom {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) (Z : TensorVertex ι n → ℤ) :
    TensorLattice ι n →+ ℤ := by
  classical
  exact if hZ : LineZero n Z then
    (TensorRealCharacter.realize_integer_array n Z hZ).choose
  else 0

theorem arrayHom_column {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) (Z : TensorVertex ι n → ℤ)
    (hZ : LineZero n Z) (p : TensorVertex ι n) :
    arrayHom n Z (tensorColumn n p) = Z p := by
  classical
  simp only [arrayHom, dif_pos hZ]
  exact (TensorRealCharacter.realize_integer_array n Z hZ).choose_spec p

/-- The tensor Gram trace, after the `2π` phase scale, gives the explicit
uniform variance budget of a finite tensor stage. -/
noncomputable def uniformStageQ (q : ℕ → ℕ) (k : ℕ) : ℝ :=
  let n := TensorStageBound.stageRanks q k
  Real.pi ^ 2 *
    ((∏ i : Fin k, ((n i : ℝ) +
      ∑ j : Fin (n i), (1 : ℝ) / (j.val + 1 : ℝ))) /
      (Fintype.card (TensorVertex (Fin k) n) : ℝ))

/-- A concrete finite weighted law of integer additive homomorphisms with
unbiased `2π` phase error and uniform second moment on every tensor column. -/
theorem finite_hom_moment_law {ι : Type*} [Fintype ι] [DecidableEq ι]
    (n : ι → ℕ) (θ : AddChar (TensorLattice ι n) Circle) :
    ∃ (s : Finset (TensorLattice ι n →+ ℤ))
      (w : (TensorLattice ι n →+ ℤ) → ℝ),
      (∀ FZ ∈ s, 0 ≤ w FZ) ∧
      (∑ FZ ∈ s, w FZ) = 1 ∧
      (∀ p : TensorVertex ι n,
        (∑ FZ ∈ s, w FZ *
          (TensorRealCharacter.globalRealLiftHom n θ (tensorColumn n p) -
            (2 * Real.pi) * (FZ (tensorColumn n p) : ℝ))) = 0) ∧
      (∀ p : TensorVertex ι n,
        (∑ FZ ∈ s, w FZ *
          (TensorRealCharacter.globalRealLiftHom n θ (tensorColumn n p) -
            (2 * Real.pi) * (FZ (tensorColumn n p) : ℝ)) ^ 2) ≤
            Real.pi ^ 2 *
              ((∏ i : ι, ((n i : ℝ) +
                ∑ j : Fin (n i), (1 : ℝ) / (j.val + 1 : ℝ))) /
                (Fintype.card (TensorVertex ι n) : ℝ))) := by
  classical
  let FX : TensorVertex ι n → ℝ :=
    fun p => TensorRealCharacter.globalRealLiftHom n θ (tensorColumn n p)
  have hFX : LineZero n FX := by
    intro p i
    exact TensorRealCharacter.additiveHom_line_sum n
      (TensorRealCharacter.globalRealLiftHom n θ) p i
  obtain ⟨L, hL, hmom⟩ := finite_uniform_phase_lift_rounding n FX hFX
  obtain ⟨s, w, hw, hweight, hexpect⟩ := finite_pushforward L (arrayHom n)
  refine ⟨s, w, hw, hweight, ?_, ?_⟩
  · intro p
    have hall : LatticeRounding.Law.All
        (fun Z =>
          FX p - (2 * Real.pi) * (arrayHom n Z (tensorColumn n p) : ℝ) =
            FX p - (2 * Real.pi) * (Z p : ℝ)) L :=
      LatticeRounding.Law.all_mono L (LineZero n) _
        (fun Z hZ => by rw [arrayHom_column n Z hZ p]) hL
    calc
      (∑ FZ ∈ s, w FZ *
          (TensorRealCharacter.globalRealLiftHom n θ (tensorColumn n p) -
            (2 * Real.pi) * (FZ (tensorColumn n p) : ℝ))) =
          L.expect (fun Z => FX p -
            (2 * Real.pi) * (arrayHom n Z (tensorColumn n p) : ℝ)) :=
        hexpect _
      _ = L.expect (fun Z => FX p - (2 * Real.pi) * (Z p : ℝ)) :=
        LatticeRounding.Law.expect_congr_of_all L _ _ hall
      _ = 0 := (hmom p).1
  · intro p
    have hall : LatticeRounding.Law.All
        (fun Z =>
          (FX p - (2 * Real.pi) * (arrayHom n Z (tensorColumn n p) : ℝ)) ^ 2 =
            (FX p - (2 * Real.pi) * (Z p : ℝ)) ^ 2) L :=
      LatticeRounding.Law.all_mono L (LineZero n) _
        (fun Z hZ => by rw [arrayHom_column n Z hZ p]) hL
    calc
      (∑ FZ ∈ s, w FZ *
          (TensorRealCharacter.globalRealLiftHom n θ (tensorColumn n p) -
            (2 * Real.pi) * (FZ (tensorColumn n p) : ℝ)) ^ 2) =
          L.expect (fun Z =>
            (FX p - (2 * Real.pi) * (arrayHom n Z (tensorColumn n p) : ℝ)) ^ 2) :=
        hexpect _
      _ = L.expect (fun Z => (FX p - (2 * Real.pi) * (Z p : ℝ)) ^ 2) :=
        LatticeRounding.Law.expect_congr_of_all L _ _ hall
      _ ≤ _ := (hmom p).2

/-- The symmetrized concrete rounding law discharges the moment hypothesis
at every finite tensor stage. -/
theorem uniform_stage_moment_law (q : ℕ → ℕ) (k : ℕ) :
    StageMomentLaw q (uniformStageQ q) k := by
  classical
  intro θ
  let n := TensorStageBound.stageRanks q k
  obtain ⟨s, w, hw, hweight, hmean, hmoment⟩ := finite_hom_moment_law n θ
  refine ⟨s, w, hw, hweight, ?_, ?_⟩
  · intro g hg
    obtain ⟨p, _, rfl⟩ := Finset.mem_image.mp hg
    exact hmean p
  · intro g hg
    obtain ⟨p, _, rfl⟩ := Finset.mem_image.mp hg
    exact hmoment p

end Erdos.Research.Problem774.TensorUniformStageMoment

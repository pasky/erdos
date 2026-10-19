import Mathlib.Combinatorics.Additive.Dissociation
import Mathlib.Combinatorics.Additive.Randomisation
import Mathlib.Analysis.SpecialFunctions.Complex.CircleAddChar
import Mathlib.Data.Finset.Card
import Mathlib.Algebra.Order.BigOperators.Expect

/-!
# The finite Pisier interface for Sidon extraction

The hard implication in Pisier's arithmetic characterization of Sidon sets is
isolated in two forms. `PisierForward` is the exact set-level statement needed
in the roots-of-unity argument. `FinitePisierForward` is a quantitative finite
form: a uniform analytic inequality on a finite set yields a dissociated
subset occupying a uniform proportion. The reverse implications have the
corresponding names.

None of these principles is asserted or proved here. The theorems below show
how the finite principles imply the set-level forms. In particular, their
constants are chosen before the finite set, not separately for each finite
set. This is stronger than merely knowing the set-level equivalence for each
individual frequency set. The forward principle excludes
the zero frequency: `{0}` satisfies an analytic Sidon bound but has no
nonempty dissociated subset.
-/

namespace Erdos.Research.SidonExtraction

open scoped BigOperators

section FiniteRiesz

variable {G : Type*} [Fintype G] [AddCommGroup G]

/-- A finite-group consequence of Mathlib's dissociated-support Riesz product
identity: some sample point attains at least the normalized mean. This is a
usable finite analogue of the analytic estimate, though the full Pisier
argument also needs quantitative relation-count and extraction steps. -/
theorem exists_riesz_product_ge_one (d : AddChar G ℂ → ℂ)
    (hd : AddDissociated {ψ | d ψ ≠ 0}) :
    ∃ x : G, (1 : ℝ) ≤
      ∏ ψ : AddChar G ℂ, (1 + (d ψ * ψ x).re) := by
  have hmean :
      (𝔼 x ∈ (Finset.univ : Finset G),
        ∏ ψ : AddChar G ℂ, (1 + (d ψ * ψ x).re)) = (1 : ℝ) := by
    simpa using
      (AddDissociated.randomisation (G := G)
        (fun _ : AddChar G ℂ => (1 : ℝ)) d hd)
  obtain ⟨x, _, hx⟩ := Finset.exists_le_of_le_expect
    (s := Finset.univ)
    (f := fun x : G => ∏ ψ : AddChar G ℂ, (1 + (d ψ * ψ x).re))
    Finset.univ_nonempty (by simpa using hmean.ge)
  exact ⟨x, hx⟩

end FiniteRiesz

/-- The analytic inequality on one finite set of frequencies in the discrete
additive group `ℂ`. `AddChar` is algebraic and imposes no continuity. -/
def FiniteSidonBound (A : Finset ℂ) (K : ℝ) : Prop :=
  ∀ c : ℂ → ℂ, ∃ χ : AddChar ℂ Circle,
    (∑ z ∈ A, ‖c z‖) ≤ K * ‖∑ z ∈ A, c z * (χ z : ℂ)‖

/-- A finite Sidon inequality is hereditary: coefficients outside the
smaller set are set to zero before applying the inequality. -/
theorem finiteSidonBound_subset {A B : Finset ℂ} {K : ℝ}
    (hBA : B ⊆ A) (hA : FiniteSidonBound A K) :
    FiniteSidonBound B K := by
  classical
  intro c
  let c' : ℂ → ℂ := fun z => if z ∈ B then c z else 0
  obtain ⟨χ, hχ⟩ := hA c'
  have hnorm : (∑ z ∈ A, ‖c' z‖) = ∑ z ∈ B, ‖c z‖ := by
    calc
      _ = ∑ z ∈ B, ‖c' z‖ :=
        (Finset.sum_subset hBA (by intro z hzA hzB; simp [c', hzB])).symm
      _ = ∑ z ∈ B, ‖c z‖ := by
        apply Finset.sum_congr rfl
        intro z hz
        simp [c', hz]
  have hpoly : (∑ z ∈ A, c' z * (χ z : ℂ)) =
      ∑ z ∈ B, c z * (χ z : ℂ) := by
    calc
      _ = ∑ z ∈ B, c' z * (χ z : ℂ) :=
        (Finset.sum_subset hBA (by intro z hzA hzB; simp [c', hzB])).symm
      _ = ∑ z ∈ B, c z * (χ z : ℂ) := by simp [c']
  exact ⟨χ, by simpa [hnorm, hpoly] using hχ⟩

/-- A dissociated subset occupying at least the reciprocal of `k` of `A`. -/
def FiniteExtraction (A : Finset ℂ) (k : ℕ) : Prop :=
  ∃ B : Finset ℂ, B ⊆ A ∧ AddDissociated (↑B : Set ℂ) ∧
    A.card ≤ k * B.card

/-- The two-color case of the elementary finite-union implication: one
dissociated color contains at least half the frequencies. This implication
does not use the analytic Sidon inequality. -/
theorem finiteExtraction_of_two_dissociated (D E : Set ℂ)
    (hD : AddDissociated D) (hE : AddDissociated E)
    (A : Finset ℂ) (hA : (↑A : Set ℂ) ⊆ D ∪ E) :
    FiniteExtraction A 2 := by
  classical
  let B : Finset ℂ := A.filter (· ∈ D)
  let C : Finset ℂ := A.filter (· ∉ D)
  have hBA : B ⊆ A := Finset.filter_subset _ _
  have hCA : C ⊆ A := Finset.filter_subset _ _
  have hBD : (↑B : Set ℂ) ⊆ D := by
    intro z hz
    exact (Finset.mem_filter.mp hz).2
  have hCE : (↑C : Set ℂ) ⊆ E := by
    intro z hz
    obtain ⟨hzA, hzND⟩ := Finset.mem_filter.mp hz
    rcases hA hzA with hzD | hzE
    · exact False.elim (hzND hzD)
    · exact hzE
  have hcard : B.card + C.card = A.card := by
    exact Finset.card_filter_add_card_filter_not
      (s := A) (p := fun z : ℂ => z ∈ D)
  by_cases hBC : C.card ≤ B.card
  · exact ⟨B, hBA, hD.subset hBD, by omega⟩
  · exact ⟨C, hCA, hE.subset hCE, by omega⟩

/-- All differences of two subset sums from `B`. This finite superset is
deliberately simpler than the sharp ternary span. -/
noncomputable def differenceSpan (B : Finset ℂ) : Finset ℂ :=
  (B.powerset.product B.powerset).image fun p =>
    (∑ z ∈ p.1, z) - ∑ z ∈ p.2, z

private theorem mem_differenceSpan {B t u : Finset ℂ}
    (ht : t ⊆ B) (hu : u ⊆ B) :
    (∑ z ∈ t, z) - ∑ z ∈ u, z ∈ differenceSpan B := by
  classical
  apply Finset.mem_image.mpr
  exact ⟨(t, u), Finset.mem_product.mpr
    ⟨Finset.mem_powerset.mpr ht, Finset.mem_powerset.mpr hu⟩, rfl⟩

/-- A maximal dissociated subset spans every element of the original finite
set by a difference of two subset sums. This greedy fact alone gives only a
logarithmic lower bound on the extracted size. -/
theorem exists_dissociated_subset_differenceSpan (A : Finset ℂ) :
    ∃ B : Finset ℂ, B ⊆ A ∧ AddDissociated (↑B : Set ℂ) ∧
      A ⊆ differenceSpan B := by
  classical
  obtain ⟨B, hB⟩ :=
    (A.powerset.filter fun B : Finset ℂ => AddDissociated (↑B : Set ℂ)).exists_maximal
      ⟨∅, Finset.mem_filter.mpr ⟨Finset.empty_mem_powerset _, by simp⟩⟩
  simp only [Finset.mem_filter, Finset.mem_powerset] at hB
  refine ⟨B, hB.1.1, hB.1.2, fun a ha => ?_⟩
  by_cases haB : a ∈ B
  · simpa using (mem_differenceSpan (B := B)
      (t := {a}) (u := ∅) (by simpa using haB) (Finset.empty_subset B))
  obtain ⟨t, u, ht, hu, htu⟩ :=
    not_addDissociated_iff_exists_disjoint.mp (by
      intro h
      exact hB.not_gt
        ⟨Finset.insert_subset_iff.mpr ⟨ha, hB.1.1⟩, h⟩
        (Finset.ssubset_insert haB))
  have ht' : t ⊆ insert a B := Finset.coe_subset.mp ht
  have hu' : u ⊆ insert a B := Finset.coe_subset.mp hu
  by_cases hat : a ∈ t
  · have haeq : a = (∑ z ∈ u, z) - ∑ z ∈ t.erase a, z := by
      rw [Finset.sum_erase_eq_sub hat, htu.2.2]
      abel
    rw [haeq]
    exact mem_differenceSpan
      ((Finset.subset_insert_iff_of_notMem
        (Finset.disjoint_left.mp htu.1 hat)).mp hu')
      (Finset.subset_insert_iff.mp ht')
  have htB : t ⊆ B :=
    (Finset.subset_insert_iff_of_notMem hat).mp ht'
  by_cases hau : a ∈ u
  · have haeq : a = (∑ z ∈ t, z) - ∑ z ∈ u.erase a, z := by
      rw [Finset.sum_erase_eq_sub hau, ← htu.2.2]
      abel
    rw [haeq]
    exact mem_differenceSpan htB (Finset.subset_insert_iff.mp hu')
  have huB : u ⊆ B :=
    (Finset.subset_insert_iff_of_notMem hau).mp hu'
  have hnotB : ¬ AddDissociated (↑B : Set ℂ) :=
    not_addDissociated_iff_exists_disjoint.mpr
      ⟨t, u, Finset.coe_subset.mpr htB,
        Finset.coe_subset.mpr huB, htu⟩
  exact False.elim (hnotB hB.1.2)

/-- The maximal-subset argument gives at most an exponential span bound.
The missing Pisier step must use analytic information to improve this to a
linear extraction bound. -/
theorem exists_dissociated_subset_card_exponential (A : Finset ℂ) :
    ∃ B : Finset ℂ, B ⊆ A ∧ AddDissociated (↑B : Set ℂ) ∧
      A.card ≤ 4 ^ B.card := by
  classical
  obtain ⟨B, hBA, hB, hspan⟩ := exists_dissociated_subset_differenceSpan A
  refine ⟨B, hBA, hB, ?_⟩
  calc
    A.card ≤ (differenceSpan B).card := Finset.card_le_card hspan
    _ ≤ (B.powerset.product B.powerset).card := Finset.card_image_le
    _ = 4 ^ B.card := by
      calc
        _ = B.powerset.card * B.powerset.card := Finset.card_product _ _
        _ = 2 ^ B.card * 2 ^ B.card := by simp
        _ = 4 ^ B.card := by rw [← mul_pow]; norm_num

/-- The set-level Sidon property with one analytic constant for all finite
subsets. -/
def AnalyticSidon (s : Set ℂ) : Prop :=
  ∃ K : ℝ, 0 < K ∧
    ∀ A : Finset ℂ, (↑A : Set ℂ) ⊆ s → FiniteSidonBound A K

/-- The one-set finite inequality is equivalent to the set-level Sidon
property of that finite set; the reverse implication uses zero extension. -/
theorem analyticSidon_coe_iff (A : Finset ℂ) :
    AnalyticSidon (↑A : Set ℂ) ↔
      ∃ K : ℝ, 0 < K ∧ FiniteSidonBound A K := by
  constructor
  · rintro ⟨K, hK, h⟩
    exact ⟨K, hK, h A (Set.Subset.refl _)⟩
  · rintro ⟨K, hK, hA⟩
    exact ⟨K, hK, fun B hBA =>
      finiteSidonBound_subset (Finset.coe_subset.mp hBA) hA⟩

/-- The set-level extraction property with one integer denominator for all
finite subsets. -/
def UniformExtraction (s : Set ℂ) : Prop :=
  ∃ k : ℕ, 0 < k ∧
    ∀ A : Finset ℂ, (↑A : Set ℂ) ⊆ s → FiniteExtraction A k

theorem uniformExtraction_union_two_dissociated (D E : Set ℂ)
    (hD : AddDissociated D) (hE : AddDissociated E) :
    UniformExtraction (D ∪ E) :=
  ⟨2, by omega, fun A hA => finiteExtraction_of_two_dissociated D E hD hE A hA⟩

/-- Pisier's difficult direction, restricted to frequency sets excluding the
trivial character. This set-level form suffices for the roots-of-unity proof. -/
def PisierForward : Prop :=
  ∀ s : Set ℂ, 0 ∉ s → AnalyticSidon s → UniformExtraction s

/-- The reverse direction of Pisier's characterization at the set level. -/
def PisierReverse : Prop :=
  ∀ s : Set ℂ, 0 ∉ s → UniformExtraction s → AnalyticSidon s

/-- The finite, quantitative form of Pisier's difficult direction at a fixed
analytic constant. The outer quantifier over `k` precedes the finite set. -/
def FinitePisierForward (K : ℝ) : Prop :=
  ∃ k : ℕ, 0 < k ∧
    ∀ A : Finset ℂ, 0 ∉ A →
      FiniteSidonBound A K → FiniteExtraction A k

/-- The finite form of Pisier's reverse direction at a fixed extraction
denominator. The hypothesis is hereditary over every subset of `A`. -/
def FinitePisierReverse (k : ℕ) : Prop :=
  ∃ K : ℝ, 0 < K ∧
    ∀ A : Finset ℂ, 0 ∉ A →
      (∀ B : Finset ℂ, B ⊆ A → FiniteExtraction B k) →
        FiniteSidonBound A K

theorem uniformExtraction_of_analyticSidon
    (hPisier : ∀ K : ℝ, 0 < K → FinitePisierForward K)
    {s : Set ℂ} (hzero : 0 ∉ s)
    (hs : AnalyticSidon s) : UniformExtraction s := by
  obtain ⟨K, hK, hSidon⟩ := hs
  obtain ⟨k, hk, hFinite⟩ := hPisier K hK
  refine ⟨k, hk, fun A hA => hFinite A ?_ (hSidon A hA)⟩
  exact fun hz => hzero (hA (Finset.mem_coe.mpr hz))

theorem pisierForward_of_finite
    (hPisier : ∀ K : ℝ, 0 < K → FinitePisierForward K) :
    PisierForward := by
  intro s hzero hs
  exact uniformExtraction_of_analyticSidon hPisier hzero hs

theorem analyticSidon_of_uniformExtraction
    (hPisier : ∀ k : ℕ, 0 < k → FinitePisierReverse k)
    {s : Set ℂ} (hzero : 0 ∉ s)
    (hs : UniformExtraction s) : AnalyticSidon s := by
  obtain ⟨k, hk, hExtract⟩ := hs
  obtain ⟨K, hK, hFinite⟩ := hPisier k hk
  refine ⟨K, hK, fun A hA => hFinite A ?_ ?_⟩
  · exact fun hz => hzero (hA (Finset.mem_coe.mpr hz))
  · intro B hBA
    exact hExtract B ((Finset.coe_subset.mpr hBA).trans hA)

theorem pisierReverse_of_finite
    (hPisier : ∀ k : ℕ, 0 < k → FinitePisierReverse k) :
    PisierReverse := by
  intro s hzero hs
  exact analyticSidon_of_uniformExtraction hPisier hzero hs

theorem analyticSidon_iff_uniformExtraction_of_pisier
    (hForward : PisierForward) (hReverse : PisierReverse)
    (s : Set ℂ) (hzero : 0 ∉ s) :
    AnalyticSidon s ↔ UniformExtraction s :=
  ⟨hForward s hzero, hReverse s hzero⟩

theorem analyticSidon_iff_uniformExtraction
    (hForward : ∀ K : ℝ, 0 < K → FinitePisierForward K)
    (hReverse : ∀ k : ℕ, 0 < k → FinitePisierReverse k)
    (s : Set ℂ) (hzero : 0 ∉ s) :
    AnalyticSidon s ↔ UniformExtraction s :=
  analyticSidon_iff_uniformExtraction_of_pisier
    (pisierForward_of_finite hForward) (pisierReverse_of_finite hReverse) s hzero

end Erdos.Research.SidonExtraction

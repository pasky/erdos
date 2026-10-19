import Erdos.RootsOfUnitySidon.TensorUniformStageMoment
import Erdos.RootsOfUnitySidon.PrimeTailBounds

/-!
# Numerical tensor moment factors

The explicit second moment of a finite simplex tensor stage is the product
of the prime-side factors used in the tail estimate. For an increasing list,
the product before an entry is exactly the `priorTensorProd` over that list.
-/

namespace Erdos.Research.Problem774.TensorUniformPrimeFactor

open Finset
open Erdos.Research.Problem774.TensorStageBound
open Erdos.Research.Problem774.TensorStageMoment
open Erdos.Research.Problem774.TensorUniformStageMoment
open Erdos.Research.Problem774.TensorGramTrace
open Erdos.Research.PrimeTailBounds

private theorem side_harmonic_sum (n : ℕ) :
    (∑ j : Fin n, (1 : ℝ) / (j.val + 1 : ℝ)) =
      ((harmonic n : ℚ) : ℝ) := by
  calc
    _ = ∑ j ∈ Finset.range n, (1 : ℝ) / (j + 1 : ℝ) :=
      Fin.sum_univ_eq_sum_range _ _
    _ = _ := by simp [harmonic]

private theorem side_moment_factor (p : ℕ) (hp : 3 ≤ p) :
    (((p - 1 : ℕ) : ℝ) +
      ∑ j : Fin (p - 1), (1 : ℝ) / (j.val + 1 : ℝ)) /
        (p : ℝ) = tensorFactor p := by
  rw [side_harmonic_sum]
  have hsub : ((p - 1 : ℕ) : ℝ) = (p : ℝ) - 1 := by
    rw [Nat.cast_sub (by omega : 1 ≤ p)]
    norm_num
  rw [hsub]
  rfl

/-- The uniform second-moment budget is `π²` times the product of the
individual side factors. -/
theorem uniformStageQ_eq_tensorFactor_prod (q : ℕ → ℕ) (k : ℕ)
    (hq : ∀ i < k, 3 ≤ q i) :
    uniformStageQ q k =
      Real.pi ^ 2 * ∏ i : Fin k, tensorFactor (q i) := by
  classical
  let n := stageRanks q k
  have hcard : (Fintype.card (TensorVertex (Fin k) n) : ℝ) =
      ∏ i : Fin k, (q i : ℝ) := by
    simp only [TensorVertex, Fintype.card_pi, Fintype.card_fin, Nat.cast_prod]
    apply Finset.prod_congr rfl
    intro i _
    change (((q i - 1 + 1 : ℕ) : ℝ)) = (q i : ℝ)
    have hqi := hq i i.isLt
    rw [Nat.sub_add_cancel (by omega : 1 ≤ q i)]
  unfold uniformStageQ
  dsimp only
  rw [hcard, ← Finset.prod_div_distrib]
  congr 1
  apply Finset.prod_congr rfl
  intro i _
  exact side_moment_factor (q i) (hq i i.isLt)

/-- Earlier entries of a strictly increasing list are exactly the entries
smaller than its `i`th entry. -/
private theorem prior_filter_eq_prefix_image
    {ps : List ℕ} (hsort : ps.SortedLT) (i : ℕ) (hi : i < ps.length) :
    ps.toFinset.filter (fun p => p < ps[i]) =
      (Finset.range i).image (listSides ps) := by
  classical
  ext p
  constructor
  · intro hp
    obtain ⟨hmem, hlt⟩ := Finset.mem_filter.mp hp
    obtain ⟨j, hj, rfl⟩ := List.mem_iff_getElem.mp (List.mem_toFinset.mp hmem)
    have hji : j < i := (hsort.getElem_lt_getElem_iff).mp hlt
    refine Finset.mem_image.mpr ⟨j, Finset.mem_range.mpr hji, ?_⟩
    exact listSides_getElem ps j hj
  · intro hp
    obtain ⟨j, hj, rfl⟩ := Finset.mem_image.mp hp
    have hji : j < i := Finset.mem_range.mp hj
    have hjlen : j < ps.length := hji.trans hi
    rw [listSides_getElem ps j hjlen]
    exact Finset.mem_filter.mpr
      ⟨List.mem_toFinset.mpr (List.getElem_mem hjlen),
        hsort.getElem_lt_getElem_of_lt hji⟩

/-- The product of the first `i` side factors is the prior-factor product
for the `i`th entry of a strictly increasing list. -/
theorem priorTensorProd_eq_prefix_prod
    {ps : List ℕ} (hsort : ps.SortedLT) (i : ℕ) (hi : i < ps.length) :
    priorTensorProd ps.toFinset ps[i] =
      ∏ j ∈ Finset.range i, tensorFactor (listSides ps j) := by
  classical
  have hinj : Set.InjOn (listSides ps) (Finset.range i) := by
    intro a ha b hb hab
    have ha' : a < ps.length := (Finset.mem_range.mp ha).trans hi
    have hb' : b < ps.length := (Finset.mem_range.mp hb).trans hi
    rw [listSides_getElem ps a ha', listSides_getElem ps b hb'] at hab
    exact (hsort.nodup.getElem_inj_iff).mp hab
  unfold priorTensorProd
  rw [prior_filter_eq_prefix_image hsort i hi]
  exact Finset.prod_image hinj

/-- At each entry of an increasing side list, the stage loss is the term
bounded by the prime-tail series. -/
theorem stageLoss_listSides_eq_priorTensorProd
    {ps : List ℕ} (hsort : ps.SortedLT)
    (hside : ∀ p ∈ ps, 3 ≤ p)
    (i : ℕ) (hi : i < ps.length) :
    stageLoss (listSides ps) (uniformStageQ (listSides ps)) i =
      3 * Real.pi ^ 2 * priorTensorProd ps.toFinset ps[i] /
        (ps[i] : ℝ) ^ 2 := by
  have hprefix : ∀ j < i, 3 ≤ listSides ps j := by
    intro j hj
    have hjlen : j < ps.length := hj.trans hi
    rw [listSides_getElem ps j hjlen]
    exact hside ps[j] (List.getElem_mem hjlen)
  rw [stageLoss, uniformStageQ_eq_tensorFactor_prod (listSides ps) i hprefix,
    priorTensorProd_eq_prefix_prod hsort i hi,
    listSides_getElem ps i hi]
  rw [Fin.prod_univ_eq_prod_range (fun j => tensorFactor (listSides ps j)) i]
  ring

end Erdos.Research.Problem774.TensorUniformPrimeFactor

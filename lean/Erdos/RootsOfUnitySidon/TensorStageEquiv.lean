import Erdos.RootsOfUnitySidon.TensorStageBound
import Erdos.RootsOfUnitySidon.TensorLiftAssembly
import Erdos.RootsOfUnitySidon.TensorStageAssembly
import Mathlib.Tactic

/-!
# Reindexing adjacent free tensor stages

The fresh `Fin (k+1)` product presentation of a tensor lattice is additively
equivalent to one copy of the old stage lattice for each basis vector of the
new simplex. This is the algebraic change of coordinates between
`TensorStageBound` and `TensorLiftAssembly`.
-/

namespace Erdos.Research.Problem774.TensorStageEquiv

open Erdos.Research.Problem774.TensorPhaseLattice
open Erdos.Research.Problem774.TensorStageBound
open Erdos.Research.Problem774.TensorLiftAssembly
open Erdos.Research.Problem774.TensorStageAssembly

/-- Split a product-index tuple into the new last coordinate and its old
coordinate tuple. -/
def splitStageIndex (q : ℕ → ℕ) (k : ℕ) :
    TensorIndex (Fin (k + 1)) (stageRanks q (k + 1)) →
      TensorIndex (Fin k) (stageRanks q k) × Fin (q k - 1 + 1) :=
  fun j => (fun i => j i.castSucc, j (Fin.last k))

/-- Assemble the old coordinate tuple and the new last coordinate. -/
def joinStageIndex (q : ℕ → ℕ) (k : ℕ) :
    TensorIndex (Fin k) (stageRanks q k) × Fin (q k - 1 + 1) →
      TensorIndex (Fin (k + 1)) (stageRanks q (k + 1)) :=
  fun jl => Fin.snoc jl.1 jl.2

/-- Exact bijection of the product column indices at adjacent stages. -/
def stageIndexEquiv (q : ℕ → ℕ) (k : ℕ) :
    TensorIndex (Fin k) (stageRanks q k) × Fin (q k - 1 + 1) ≃
      TensorIndex (Fin (k + 1)) (stageRanks q (k + 1)) where
  toFun := joinStageIndex q k
  invFun := splitStageIndex q k
  left_inv := by
    intro jl
    rcases jl with ⟨j, l⟩
    simp [splitStageIndex, joinStageIndex]
    exact Prod.ext
      (funext fun i => Fin.snoc_castSucc (α := fun i => Fin (stageRanks q (k + 1) i + 1)) ..)
      (Fin.snoc_last (α := fun i => Fin (stageRanks q (k + 1) i + 1)) ..)
  right_inv := by
    intro j
    funext i
    induction i using Fin.lastCases with
    | last => simp [splitStageIndex, joinStageIndex]
    | cast i => simp [splitStageIndex, joinStageIndex]

/-- Reassociate integer coordinates of a tensor stage. -/
def stageTensorEquiv (q : ℕ → ℕ) (k : ℕ) :
    NextTensor (TensorLattice (Fin k) (stageRanks q k)) (q k - 1) ≃+
      TensorLattice (Fin (k + 1)) (stageRanks q (k + 1)) where
  toFun x := fun b => x (b (Fin.last k)) (fun i => b i.castSucc)
  invFun y := fun l a => y (Fin.snoc a l)
  left_inv := by
    intro x
    funext l a
    simp
    exact congrArg₂ x (Fin.snoc_last (α := fun i => Fin (stageRanks q (k + 1) i)) ..)
      (funext fun i => Fin.snoc_castSucc (α := fun i => Fin (stageRanks q (k + 1) i)) ..)
  right_inv := by
    intro y
    funext b
    have hb : Fin.snoc (fun i : Fin k => b i.castSucc) (b (Fin.last k)) = b := by
      funext i
      induction i using Fin.lastCases with
      | last => simp
      | cast i => simp
    change y (Fin.snoc (fun i : Fin k => b i.castSucc) (b (Fin.last k))) = y b
    rw [hb]
  map_add' := by
    intro x y
    funext b
    rfl

/-- Reassociation carries a pure tensor from the one-step presentation to
the corresponding product-index tensor column. -/
theorem stageTensorEquiv_nextFrequency (q : ℕ → ℕ) (k : ℕ)
    (j : TensorIndex (Fin k) (stageRanks q k))
    (l : Fin (q k - 1 + 1)) :
    stageTensorEquiv q k
      (nextFrequency (q k - 1) (tensorColumn (stageRanks q k) j) l) =
        tensorColumn (stageRanks q (k + 1))
          (stageIndexEquiv q k (j, l)) := by
  ext b
  simp only [stageTensorEquiv, AddEquiv.coe_mk, Equiv.coe_fn_mk,
    nextFrequency, tensorColumn, stageIndexEquiv, joinStageIndex]
  rw [Fin.prod_univ_castSucc]
  have hcast (i : Fin k) :
      Fin.snoc (α := fun i => Fin (stageRanks q (k + 1) i + 1)) j l i.castSucc = j i :=
    Fin.snoc_castSucc ..
  have hlast :
      Fin.snoc (α := fun i => Fin (stageRanks q (k + 1) i + 1)) j l (Fin.last k) = l :=
    Fin.snoc_last ..
  simp only [hcast, hlast]
  change SimplexTorus.column (q k - 1) l (b (Fin.last k)) •
      tensorColumn (stageRanks q k) j (fun i => b i.castSucc) = _
  simp [tensorColumn, stageRanks]
  ring

/-- The stage-frequency set is exactly the image of the one-step tensor
frequency set under coordinate reassociation. -/
theorem stageFrequencies_succ (q : ℕ → ℕ) (k : ℕ) :
    stageFrequencies q (k + 1) =
      (nextFrequencies (stageFrequencies q k) (q k - 1)).image
        (stageTensorEquiv q k) := by
  classical
  ext x
  constructor
  · intro hx
    obtain ⟨j, _, hj⟩ := Finset.mem_image.mp hx
    let jl := (stageIndexEquiv q k).symm j
    have hjl : (stageIndexEquiv q k) jl = j :=
      Equiv.apply_symm_apply _ _
    have hold : tensorColumn (stageRanks q k) jl.1 ∈ stageFrequencies q k := by
      unfold stageFrequencies
      exact Finset.mem_image.mpr ⟨jl.1, Finset.mem_univ _, rfl⟩
    have hnext :
        nextFrequency (q k - 1) (tensorColumn (stageRanks q k) jl.1) jl.2 ∈
          nextFrequencies (stageFrequencies q k) (q k - 1) := by
      simp only [nextFrequencies, Finset.mem_image]
      exact ⟨(tensorColumn (stageRanks q k) jl.1, jl.2),
        Finset.mem_product.mpr ⟨hold, Finset.mem_univ _⟩, rfl⟩
    apply Finset.mem_image.mpr
    refine ⟨_, hnext, ?_⟩
    rw [stageTensorEquiv_nextFrequency, hjl]
    exact hj
  · intro hx
    obtain ⟨y, hy, hxy⟩ := Finset.mem_image.mp hx
    simp only [nextFrequencies, Finset.mem_image] at hy
    obtain ⟨gj, hgj, hgjy⟩ := hy
    obtain ⟨hg, _⟩ := Finset.mem_product.mp hgj
    unfold stageFrequencies at hg
    obtain ⟨j, _, hj⟩ := Finset.mem_image.mp hg
    apply Finset.mem_image.mpr
    refine ⟨stageIndexEquiv q k (j, gj.2), Finset.mem_univ _, ?_⟩
    rw [← stageTensorEquiv_nextFrequency]
    rw [hj, hgjy]
    exact hxy

/-- An additive equivalence transports a positive-real parameter to the
image finite set without changing the parameter. -/
theorem positiveRealParameter_image {G H : Type*}
    [AddCommGroup G] [AddCommGroup H] [DecidableEq H]
    (e : G ≃+ H) (E : Finset G) (ρ : ℝ)
    (hE : Erdos.Research.TensorExtension.PositiveRealParameter E ρ) :
    Erdos.Research.TensorExtension.PositiveRealParameter (E.image e) ρ := by
  classical
  intro a
  obtain ⟨χ, hχ⟩ := hE (fun g => a (e g))
  let η : AddChar H Circle := {
    toFun h := χ (e.symm h)
    map_zero_eq_one' := by simp
    map_add_eq_mul' := by
      intro x y
      simp [map_add, χ.map_add_eq_mul] }
  refine ⟨η, ?_⟩
  have hnorm :
      (∑ h ∈ E.image e, ‖a h‖) = ∑ g ∈ E, ‖a (e g)‖ := by
    rw [Finset.sum_image]
    intro g _ h _ hgh
    exact e.injective hgh
  have hpoly :
      (∑ h ∈ E.image e, a h * (η h : ℂ)) =
        ∑ g ∈ E, a (e g) * (χ g : ℂ) := by
    rw [Finset.sum_image]
    · apply Finset.sum_congr rfl
      intro g _
      simp [η]
    · intro g _ h _ hgh
      exact e.injective hgh
  rw [hnorm, hpoly]
  exact hχ

end Erdos.Research.Problem774.TensorStageEquiv

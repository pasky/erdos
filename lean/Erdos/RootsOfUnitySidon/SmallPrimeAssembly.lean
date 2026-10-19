import Erdos.RootsOfUnitySidon.SmallPrimeBound
import Erdos.RootsOfUnitySidon.FieldTensorEvaluation
import Erdos.RootsOfUnitySidon.PrimeListSplit
import Erdos.RootsOfUnitySidon.PrimeSimplexGrid
import Erdos.RootsOfUnitySidon.PrimeSimplexFieldEvaluation
import Erdos.RootsOfUnitySidon.TailPrimeFieldBound
import Erdos.RootsOfUnitySidon.RootsOfUnitySidon
import Erdos.RootsOfUnitySidon.OddSquarefreeReduction

/-!
# Assembly of small and tail prime grids

The number of small-prime simplex columns is uniformly bounded by the
factorial of a fixed cutoff. This module also collects the generic transfer
from a tail-field positive-real bound through the small-prime tensor grid.
-/

namespace Erdos.Research.Problem774.SmallPrimeAssembly

open Erdos.Research.Problem774
open Erdos.Research.Problem774.PrimeSimplex
open Erdos.Research.Problem774.PrimeSimplexGrid
open Erdos.Research.Problem774.PrimeListSplit
open Erdos.Research.Problem774.TensorPhaseLattice
open Erdos.Research.Problem774.SmallPrimeAnalytic
open Erdos.Research.Problem774.FieldTensorEvaluation
open Erdos.Research.Problem774.TensorCRT
open Erdos.Research.Problem774.TailPrimeFieldBound
open Erdos.Research.TensorExtension

/-- The number of small-prime tensor columns is their product. -/
theorem smallTensorIndex_card (small : List ℕ)
    (hprime : ∀ p ∈ small, p.Prime) :
    Fintype.card
      (TensorIndex (Fin small.length) (fun i => small.get i - 1)) =
      small.prod := by
  calc
    Fintype.card
        (TensorIndex (Fin small.length) (fun i => small.get i - 1)) =
        Fintype.card (PrimeIndex small) :=
      (Fintype.card_congr (primeIndexColumnEquiv small hprime)).symm
    _ = small.prod := by
      simp [PrimeIndex, Fintype.card_pi, List.get_eq_getElem]

/-- The product of any distinct primes below the cutoff is bounded by the
factorial of the cutoff. -/
theorem smallPrimeProd_le_factorial (R : ℕ) (ps : List ℕ)
    (hprime : ∀ p ∈ ps, p.Prime) (hnodup : ps.Nodup) :
    (small R ps).prod ≤ R.factorial := by
  classical
  let s := small R ps
  have hsNodup : s.Nodup := small_nodup R hnodup
  have hsSubset : s.toFinset ⊆ Finset.Ico 1 (R + 1) := by
    intro p hp
    have hpS : p ∈ s := List.mem_toFinset.mp hp
    have hpPrime : p.Prime := small_prime R hprime p hpS
    have hpLe : p ≤ R := of_decide_eq_true (List.mem_filter.mp hpS).2
    exact Finset.mem_Ico.mpr ⟨hpPrime.one_le, by omega⟩
  calc
    (small R ps).prod = ∏ p ∈ s.toFinset, p := by
      simpa [s] using (List.prod_toFinset id hsNodup).symm
    _ ≤ ∏ p ∈ Finset.Ico 1 (R + 1), p :=
      Finset.prod_le_prod_of_subset_of_one_le' hsSubset
        (by intro p hp _; exact (Finset.mem_Ico.mp hp).1)
    _ = R.factorial := Finset.prod_Ico_id_eq_factorial R

/-- Increasing a positive constant preserves a positive-real bound. -/
theorem positiveRealBoundOn_mono_constant {G : Type*} [AddCommGroup G]
    (s : Set G) (C D : ℝ) (hC : 0 < C) (hCD : C ≤ D)
    (h : PositiveRealBoundOn s C) : PositiveRealBoundOn s D := by
  intro A hA c
  obtain ⟨χ, hχ⟩ := h A hA c
  refine ⟨χ, hχ.trans ?_⟩
  let P : ℂ := ∑ z ∈ A, c z * (χ z : ℂ)
  have hnorm : 0 ≤ ∑ z ∈ A, ‖c z‖ := by
    apply Finset.sum_nonneg
    intro z _
    exact norm_nonneg _
  have hRe : 0 ≤ P.re := by
    by_contra hnot
    have hneg : P.re < 0 := lt_of_not_ge hnot
    have := mul_neg_of_pos_of_neg hC hneg
    change 0 > C * P.re at this
    linarith
  exact mul_le_mul_of_nonneg_right hCD hRe

private theorem root_mem_primeField (n : ℕ) (hn : 0 < n)
    (z : ℂ) (hz : z ^ n = 1) : z ∈ primeField n := by
  letI : NeZero n := ⟨hn.ne'⟩
  obtain ⟨i, _, hi⟩ := (zeta_primitive n hn).eq_pow_of_pow_eq_one hz
  rw [← hi]
  exact pow_mem (IntermediateField.mem_adjoin_simple_self ℚ (PrimeSimplex.zeta n)) i

private theorem primeList_prod_pos (ps : List ℕ)
    (hprime : ∀ p ∈ ps, p.Prime) : 0 < ps.prod := by
  induction ps with
  | nil => simp
  | cons p qs ih =>
      have hp : p.Prime := hprime p (by simp)
      have hqs : ∀ q ∈ qs, q.Prime := by
        intro q hq
        exact hprime q (by simp [hq])
      simpa using mul_pos hp.pos (ih hqs)

/-- Evaluating all nonzero small-prime tensor columns against tail-field
roots gives exactly the roots of the product order. -/
theorem evaluated_nonzeroFieldTensorGrid_eq_nthRoots
    (small tail : List ℕ)
    (hsmall : ∀ p ∈ small, p.Prime)
    (htail : ∀ q ∈ tail, q.Prime)
    (hsmallNodup : small.Nodup)
    (hsep : ∀ p ∈ small, ∀ q ∈ tail, p ≠ q) :
    ((evaluation (primeField tail.prod)
      (fun i : Fin small.length => small.get i - 1)
      (primeBasisValue small)) ''
      (nonzeroFieldTensorGrid (primeField tail.prod)
        (fun i : Fin small.length => small.get i - 1)
        {w : primeField tail.prod | (w : ℂ) ^ tail.prod = 1})) =
      nthRoots (small.prod * tail.prod) := by
  classical
  let K := primeField tail.prod
  let n : Fin small.length → ℕ := fun i => small.get i - 1
  let b := primeBasisValue small
  have hsmallPos : 0 < small.prod := primeList_prod_pos small hsmall
  have htailPos : 0 < tail.prod := primeList_prod_pos tail htail
  have hcoprime : small.prod.Coprime tail.prod :=
    coprime_prime_list_products small tail hsmall htail hsep
  ext z
  constructor
  · rintro ⟨x, ⟨j, w, hw, _, hx⟩, rfl⟩
    rw [hx]
    have hval := fieldTensorFrequency_evaluation_eq_root
      small tail hsmall hsmallNodup j w
    change evaluation K n b (fieldTensorFrequency K n j w) ∈
      nthRoots (small.prod * tail.prod)
    rw [hval]
    have hprod : (w : ℂ) *
        ((primeGridEquiv small hsmall hsmallNodup
          ((primeIndexColumnEquiv small hsmall).symm j) : RootGrid small.prod) : ℂ) ∈
        {u : ℂ | ∃ x y : ℂ, x ^ small.prod = 1 ∧
          y ^ tail.prod = 1 ∧ x * y = u} := by
      refine ⟨((primeGridEquiv small hsmall hsmallNodup
      ((primeIndexColumnEquiv small hsmall).symm j) : RootGrid small.prod) : ℂ),
        (w : ℂ), ?_, hw, by ring⟩
      exact (primeGridEquiv small hsmall hsmallNodup
        ((primeIndexColumnEquiv small hsmall).symm j)).property
    rw [← rootGrid_product_set small.prod tail.prod hcoprime hsmallPos htailPos]
      at hprod
    exact hprod
  · intro hz
    have hz' : z ∈
        {u : ℂ | ∃ x y : ℂ, x ^ small.prod = 1 ∧
          y ^ tail.prod = 1 ∧ x * y = u} := by
      rw [← rootGrid_product_set small.prod tail.prod hcoprime hsmallPos htailPos]
      exact hz
    obtain ⟨x, y, hx, hy, hxy⟩ := hz'
    let w : K := ⟨y, root_mem_primeField tail.prod htailPos y hy⟩
    let r : RootGrid small.prod := ⟨x, hx⟩
    let j0 : PrimeIndex small :=
      (primeGridEquiv small hsmall hsmallNodup).symm r
    let j : TensorIndex (Fin small.length) n :=
      primeIndexColumnEquiv small hsmall j0
    have hw0 : w ≠ 0 := by
      intro hwz
      have hyz : y = 0 := congrArg Subtype.val hwz
      rw [hyz] at hy
      simp [htailPos.ne'] at hy
    refine ⟨fieldTensorFrequency K n j w,
      ⟨j, w, hy, hw0, rfl⟩, ?_⟩
    have hj :
        ((primeGridEquiv small hsmall hsmallNodup
          ((primeIndexColumnEquiv small hsmall).symm j) : RootGrid small.prod) : ℂ) =
        x := by
      change ((primeGridEquiv small hsmall hsmallNodup
        ((primeIndexColumnEquiv small hsmall).symm j) : RootGrid small.prod) : ℂ) =
          (r : ℂ)
      simp [j, j0]
    rw [fieldTensorFrequency_evaluation_eq_root small tail hsmall hsmallNodup j w,
      hj]
    simpa [w, mul_comm] using hxy

/-- A positive-real bound on tail roots extends to their product with any
finite family of distinct odd small primes. The only loss is the number of
small-prime simplex columns. -/
theorem positiveRealBound_product_of_tail
    (small tail : List ℕ)
    (hsmall : ∀ p ∈ small, p.Prime)
    (hsmallOdd : ∀ p ∈ small, Odd p)
    (htail : ∀ q ∈ tail, q.Prime)
    (hsmallNodup : small.Nodup)
    (hsep : ∀ p ∈ small, ∀ q ∈ tail, p ≠ q)
    (C : ℝ) (hC : 0 < C)
    (hTail : PositiveRealBoundOn
      {w : primeField tail.prod | (w : ℂ) ^ tail.prod = 1} C) :
    PositiveRealBound (nthRoots (small.prod * tail.prod))
      ((small.prod : ℝ) * C) := by
  let K := primeField tail.prod
  let n : Fin small.length → ℕ := fun i => small.get i - 1
  let t : Set K := {w | (w : ℂ) ^ tail.prod = 1}
  have hn : ∀ i : Fin small.length, 2 ≤ n i := by
    intro i
    have hp : (small.get i).Prime := hsmall (small.get i) (List.get_mem small i)
    have hodd : Odd (small.get i) := hsmallOdd (small.get i) (List.get_mem small i)
    have hp3 : 3 ≤ small.get i := by
      have hp2 := hp.two_le
      obtain ⟨k, hk⟩ := hodd
      omega
    have hp3' : 2 ≤ small.get i - 1 := by omega
    simpa [n, List.get_eq_getElem] using hp3'
  have hli : LinearIndependent K (primeBasisValue small) :=
    primeBasis_linearIndependent_over_tail small tail hsmall htail hsmallNodup hsep
  have hTensor : PositiveRealBoundOn (nonzeroFieldTensorGrid K n t)
      ((Fintype.card (TensorIndex (Fin small.length) n) : ℝ) * C) :=
    positiveRealBoundOn_nonzeroFieldTensorGrid K n hn t C hC.le hTail
  have hEval := positiveRealBoundOn_evaluation_image K n
    (primeBasisValue small) hli (nonzeroFieldTensorGrid K n t)
    ((Fintype.card (TensorIndex (Fin small.length) n) : ℝ) * C) hTensor
  rw [evaluated_nonzeroFieldTensorGrid_eq_nthRoots
    small tail hsmall htail hsmallNodup hsep] at hEval
  change PositiveRealBound (nthRoots (small.prod * tail.prod))
    ((Fintype.card (TensorIndex (Fin small.length) n) : ℝ) * C) at hEval
  simpa only [n, smallTensorIndex_card small hsmall] using hEval

/-- A cutoff makes the small-prime factor uniform over all finite odd-prime
lists, provided the tail root bound is uniform. -/
theorem positiveRealBound_primeList_of_uniform_tail
    (R : ℕ) (C : ℝ) (hC : 0 < C)
    (ps : List ℕ) (hpsNodup : ps.Nodup)
    (hps : ∀ p ∈ ps, p.Prime ∧ Odd p)
    (hTail : PositiveRealBoundOn
      {w : primeField (tail R ps).prod |
        (w : ℂ) ^ (tail R ps).prod = 1} C) :
    PositiveRealBound (nthRoots ps.prod) ((R.factorial : ℝ) * C) := by
  let s := small R ps
  let t := tail R ps
  have hsPrime : ∀ p ∈ s, p.Prime := small_prime R (fun p hp => (hps p hp).1)
  have hsOdd : ∀ p ∈ s, Odd p := by
    intro p hp
    exact (hps p (List.mem_of_mem_filter hp)).2
  have htPrime : ∀ q ∈ t, q.Prime := tail_prime R (fun p hp => (hps p hp).1)
  have hsNodup : s.Nodup := small_nodup R hpsNodup
  have hsep : ∀ p ∈ s, ∀ q ∈ t, p ≠ q := small_tail_disjoint R ps
  have hBound := positiveRealBound_product_of_tail s t hsPrime hsOdd
    htPrime hsNodup hsep C hC hTail
  have hsPos : 0 < s.prod := primeList_prod_pos s hsPrime
  have hprod : s.prod ≤ R.factorial :=
    smallPrimeProd_le_factorial R ps (fun p hp => (hps p hp).1) hpsNodup
  have hfactor : (s.prod : ℝ) * C ≤ (R.factorial : ℝ) * C :=
    mul_le_mul_of_nonneg_right (by exact_mod_cast hprod) hC.le
  have hbase : 0 < (s.prod : ℝ) * C :=
    mul_pos (Nat.cast_pos.mpr hsPos) hC
  rw [← small_mul_tail_prod R ps]
  exact positiveRealBoundOn_mono_constant
    (nthRoots (s.prod * t.prod)) ((s.prod : ℝ) * C)
    ((R.factorial : ℝ) * C) hbase hfactor hBound

/-- The parameter form used by the finite prime-tail tensor argument. -/
theorem positiveRealBound_primeList_of_uniform_tail_parameter
    (R : ℕ) (ρ : ℝ) (hρ : 0 < ρ)
    (hTail : ∀ qs : List ℕ, qs.SortedLT →
      (∀ q ∈ qs, q.Prime ∧ Odd q ∧ R < q) →
      PositiveRealParameter (tailFreeGrid qs) ρ)
    (ps : List ℕ) (hpsSorted : ps.SortedLT)
    (hps : ∀ p ∈ ps, p.Prime ∧ Odd p) :
    PositiveRealBound (nthRoots ps.prod)
      ((R.factorial : ℝ) * ρ⁻¹) := by
  let t := tail R ps
  have htSorted : t.SortedLT := (hpsSorted.pairwise.filter _).sortedLT
  have htPred : ∀ q ∈ t, q.Prime ∧ Odd q ∧ R < q := by
    intro q hq
    have hqPs : q ∈ ps := List.mem_of_mem_filter hq
    exact ⟨(hps q hqPs).1, (hps q hqPs).2,
      of_decide_eq_true (List.mem_filter.mp hq).2⟩
  have htRoot : PositiveRealBoundOn
      {w : primeField t.prod | (w : ℂ) ^ t.prod = 1} ρ⁻¹ :=
    positiveRealBoundOn_tailFieldRoots_of_parameter t
      (fun q hmem => (htPred q hmem).1) htSorted.nodup ρ hρ
      (hTail t htSorted htPred)
  exact positiveRealBound_primeList_of_uniform_tail R ρ⁻¹
    (inv_pos.mpr hρ) ps hpsSorted.nodup hps htRoot

/-- A uniform finite-tail tensor parameter at one cutoff implies the analytic
Sidon assertion for all roots of unity. -/
theorem analyticSidon_of_uniform_tail_parameter
    (R : ℕ) (ρ : ℝ) (hρ : 0 < ρ)
    (hTail : ∀ qs : List ℕ, qs.SortedLT →
      (∀ q ∈ qs, q.Prime ∧ Odd q ∧ R < q) →
      PositiveRealParameter (tailFreeGrid qs) ρ) :
    AnalyticSidon := by
  apply analyticSidon_of_sorted_odd_primeList_bound
    ((R.factorial : ℝ) * ρ⁻¹)
    (mul_pos (Nat.cast_pos.mpr (Nat.factorial_pos R)) (inv_pos.mpr hρ))
  intro ps hsorted hps
  exact positiveRealBound_primeList_of_uniform_tail_parameter
    R ρ hρ hTail ps hsorted hps

end Erdos.Research.Problem774.SmallPrimeAssembly

import Erdos.RootsOfUnitySidon.AntipodalSidon

/-!
# From prime lists to all root orders

A uniform positive-real estimate on finite grids of distinct odd prime orders
implies analytic Sidonicity of all roots of unity. The analytic estimate on the
prime grids is an explicit hypothesis here; this module only removes the
number-theoretic indexing and order reductions.
-/

namespace Erdos.Research.Problem774

/-- Every positive squarefree order is the product of the distinct primes in
its prime-factor finset. -/
theorem squarefree_eq_primeList_prod {r : ℕ} (hr : Squarefree r) :
    r.primeFactors.toList.prod = r := by
  rw [Finset.prod_toList]
  exact Nat.prod_primeFactors_of_squarefree hr

/-- A bound indexed by lists of distinct odd primes covers all odd squarefree
root grids. -/
theorem positiveRealBound_odd_squarefree_of_primeLists (K : ℝ)
    (h : ∀ ps : List ℕ, ps.Nodup →
      (∀ p ∈ ps, p.Prime ∧ Odd p) →
      PositiveRealBound (nthRoots ps.prod) K) :
    ∀ r : ℕ, 0 < r → Odd r → Squarefree r →
      PositiveRealBound (nthRoots r) K := by
  intro r _ hodd hsq
  let ps := r.primeFactors.toList
  have hnodup : ps.Nodup := Finset.nodup_toList _
  have hprime : ∀ p ∈ ps, p.Prime ∧ Odd p := by
    intro p hp
    have hpf : p ∈ r.primeFactors := Finset.mem_toList.mp hp
    have hpprime : p.Prime := Nat.prime_of_mem_primeFactors hpf
    have hpdvd : p ∣ r := Nat.dvd_of_mem_primeFactors hpf
    exact ⟨hpprime, hodd.of_dvd_nat hpdvd⟩
  simpa only [ps, squarefree_eq_primeList_prod hsq] using h ps hnodup hprime

/-- The prime-list positive-real estimate implies analytic Sidonicity of all
complex roots of unity. -/
theorem analyticSidon_of_odd_primeList_bound (K : ℝ) (hK : 0 < K)
    (h : ∀ ps : List ℕ, ps.Nodup →
      (∀ p ∈ ps, p.Prime ∧ Odd p) →
      PositiveRealBound (nthRoots ps.prod) K) : AnalyticSidon := by
  exact analyticSidon_of_odd_squarefree_positiveRealBound K hK
    (positiveRealBound_odd_squarefree_of_primeLists K h)

/-- A prime-grid estimate only for increasing prime lists also suffices. The
prime factors of each squarefree order are sorted before applying it. -/
theorem analyticSidon_of_sorted_odd_primeList_bound (K : ℝ) (hK : 0 < K)
    (h : ∀ ps : List ℕ, ps.SortedLT →
      (∀ p ∈ ps, p.Prime ∧ Odd p) →
      PositiveRealBound (nthRoots ps.prod) K) : AnalyticSidon := by
  apply analyticSidon_of_odd_squarefree_positiveRealBound K hK
  intro r _ hodd hsq
  let ps := r.primeFactors.sort
  have hsorted : ps.SortedLT := Finset.sortedLT_sort _
  have hprime : ∀ p ∈ ps, p.Prime ∧ Odd p := by
    intro p hp
    have hpf : p ∈ r.primeFactors := by simpa [ps] using hp
    have hpprime : p.Prime := Nat.prime_of_mem_primeFactors hpf
    have hpdvd : p ∣ r := Nat.dvd_of_mem_primeFactors hpf
    exact ⟨hpprime, hodd.of_dvd_nat hpdvd⟩
  have hprod : ps.prod = r := by
    calc
      ps.prod = r.primeFactors.toList.prod :=
        (Finset.sort_perm_toList r.primeFactors (· ≤ ·)).prod_eq
      _ = r := squarefree_eq_primeList_prod hsq
  simpa only [hprod] using h ps hsorted hprime

end Erdos.Research.Problem774

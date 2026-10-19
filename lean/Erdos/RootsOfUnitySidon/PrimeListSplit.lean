import Erdos.RootsOfUnitySidon.PrimeSimplexEmbedding

/-!
# Splitting a prime tensor at a fixed cutoff

For a finite list of distinct odd primes, the small and tail sublists have
the expected products, primality, and disjointness properties. These are the
list hypotheses needed by the cyclotomic linear independence theorem.
-/

namespace Erdos.Research.Problem774.PrimeListSplit

/-- Prime factors no larger than a fixed cutoff. -/
def small (R : ℕ) (ps : List ℕ) : List ℕ :=
  ps.filter (· ≤ R)

/-- Prime factors above the cutoff. -/
def tail (R : ℕ) (ps : List ℕ) : List ℕ :=
  ps.filter (R < ·)

theorem small_nodup (R : ℕ) {ps : List ℕ} (h : ps.Nodup) :
    (small R ps).Nodup := h.filter _

theorem tail_nodup (R : ℕ) {ps : List ℕ} (h : ps.Nodup) :
    (tail R ps).Nodup := h.filter _

theorem small_prime (R : ℕ) {ps : List ℕ}
    (h : ∀ p ∈ ps, p.Prime) : ∀ p ∈ small R ps, p.Prime := by
  intro p hp
  exact h p (List.mem_of_mem_filter hp)

theorem tail_prime (R : ℕ) {ps : List ℕ}
    (h : ∀ p ∈ ps, p.Prime) : ∀ p ∈ tail R ps, p.Prime := by
  intro p hp
  exact h p (List.mem_of_mem_filter hp)

theorem small_tail_disjoint (R : ℕ) (ps : List ℕ) :
    ∀ p ∈ small R ps, ∀ q ∈ tail R ps, p ≠ q := by
  intro p hp q hq hpq
  have hple : p ≤ R := of_decide_eq_true (List.mem_filter.mp hp).2
  have hqgt : R < q := of_decide_eq_true (List.mem_filter.mp hq).2
  omega

theorem small_tail_coprime (R : ℕ) {ps : List ℕ}
    (h : ∀ p ∈ ps, p.Prime) :
    (small R ps).prod.Coprime (tail R ps).prod :=
  PrimeSimplex.coprime_prime_list_products (small R ps) (tail R ps)
    (small_prime R h) (tail_prime R h) (small_tail_disjoint R ps)

/-- The small and tail products multiply to the original prime product. -/
theorem small_mul_tail_prod (R : ℕ) (ps : List ℕ) :
    (small R ps).prod * (tail R ps).prod = ps.prod := by
  classical
  simpa [small, tail, List.map_id, not_le] using
    (List.prod_map_filter_mul_prod_map_filter_not (p := fun p : ℕ => p ≤ R)
      (f := id) ps)

end Erdos.Research.Problem774.PrimeListSplit

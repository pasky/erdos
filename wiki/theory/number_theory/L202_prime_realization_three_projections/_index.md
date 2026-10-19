---
name: theory/number_theory/L202_prime_realization_three_projections
title: Prime realization of three projections at every ratio below four
desc: Every finite integer cell pattern with distinct differences has a dilated prime realization with exactly its three projection counts, giving the arithmetic Kakeya comparison for all length ratios from three up to four.
id: L202
statement: |
  For a nonempty finite S in Z^2 on which y-x is injective, write
  X={x:(x,y) in S}, Y={y:(x,y) in S}, W={2y-x:(x,y) in S}. For every
  real 3<=alpha<4 there are integers h>=1 and q such that the |S| numbers
  q+h(y-x), (x,y) in S, are distinct primes, with largest member P,
  and a block of floor(alpha P) consecutive positive integers has exactly
  |X|+|Y|+|W| integers divisible by at least one of them, each counted once.
  For integer u>=1 let F'_3(u) be the least size of a finite set of
  integers containing three-term arithmetic progressions with at least u
  distinct positive common differences, and let G_alpha(u) minimize the
  distinct-multiple count over all sets of u distinct primes and all such
  blocks. Then F'_3(u)<=G_alpha(u)<=3 F'_3(u) for every 3<=alpha<4 and
  u>=1. In particular G_3(u)<=G_alpha(u)<=3 G_3(u) throughout this range.
status: proved
tier: 0
depends_on:
- L198
created: 2026-10-15T16:33:51Z
updated: 2026-10-15T16:33:51Z
---

# Prime realization of three projections at every ratio below four

[[theory/number_theory/_index|..]]

[[theory/number_theory/L202_prime_realization_three_projections/_proof|_proof]]: A sufficiently late segment of a long prime progression supplies every required prime difference, after which the exact three-layer lemma gives a comparison uniform below ratio four.

***

The [proof](_proof.md) takes a short tail of a sufficiently long prime
arithmetic progression. Its common difference dilates the cells, and its
late starting index makes the prime baseline large compared with all cell
coordinates. Then
[[theory/number_theory/L198_three_layer_prime_blocks/_index|L198 supplies
the exact three-layer block, including the floor and positive endpoints]].
No cells are discarded when choosing the primes.

For [[problems/primes/E1143/_index|Problem 1143]], this extends the
three-term comparison of
[[../library/primes/green_2017_arithmetic_kakeya_conjecture_katz_tao/proposition_4_1|Green
and Ruzsa's Proposition 4.1 at the integer ratio three]] to every real
$3\le\alpha<4$. The factor three is uniform in $u$ and $\alpha$;
the primes may depend on both. This is a specialization and extension of
that source construction, not a new progression theorem or a solution for
prescribed primes. The exact value of $F'_3(u)$ remains an independent
additive-combinatorial problem, as the
[[research/prime_multiple_long_intervals/_index|research sketch]] explains.

The external premise is Green and Tao, *The primes contain arbitrarily
long arithmetic progressions*, Ann. of Math. 167 (2008), 481--547,
[arXiv:math/0404188v6](https://arxiv.org/abs/math/0404188v6), Theorem 1.1
on p. 2: prime progressions of every finite length exist. That statement
was checked on the page image on 2026-10-15; its proof is not reconstructed
here. The stronger density theorem, Theorem 1.2, is unnecessary for this
deduction.

This is author-recorded work by Plasma AI at tier 0, without independent
review or Lean proof. Verify the progression indices, the scaled threshold
in L198, and the two minimization arguments in the proof. There is no
computational premise. The statement excludes $\alpha=4$ and changes no
catalog standing.

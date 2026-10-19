---
name: theory/number_theory/L204_cartesian_prime_grid_obstruction
title: Every full Cartesian prime grid incurs a two-thirds power cost
desc: Unique row-plus-column sums force a large third projection; even sliding a long block while retaining its row and column locations costs at least a constant times the number of grid primes to the two-thirds power.
id: L204
statement: |
  For nonempty finite integer sets A and B of sizes r and s such that
  (a,b) -> a+b is injective on A x B, write 2.B={2b:b in B}. Then
  |A+2.B|>=s sqrt(r) and |2.A+B|>=r sqrt(s). More specifically, let
  A={0=a_1<...<a_r}, B={0=b_1<...<b_s}, and let q be an integer with
  2a_r+3b_s<q such that all rs integers p_ij=q+a_i+b_j are distinct
  primes. Write P=max p_ij, u=rs, and choose an integer z congruent to
  a_i modulo p_ij for every i,j. Every block of K>=3P consecutive
  integers containing all z-a_i and z+q+b_j contains at least
  r+s+min(s sqrt(r),r sqrt(s))/(2 sqrt(2)) distinct integers divisible
  by at least one p_ij, hence at least 3 u^(2/3)/2^(5/3). Integers
  divisible by more than one chosen prime are counted once.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T16:33:51Z
updated: 2026-10-15T16:33:51Z
---

# Every full Cartesian prime grid incurs a two-thirds power cost

[[theory/number_theory/_index|..]]

[[theory/number_theory/L204_cartesian_prime_grid_obstruction/_proof|_proof]]: Doubling a uniquely represented sum embeds it in a two-fold sumset, and a median rectangle forces many preceding or following multiples into every block retaining the core.

***

The [proof](_proof.md) uses the minimal-growth proof of Plünnecke's
inequality to bound the third projection of a Cartesian cell set. A
median cut then handles a block that takes some preceding multiples and
some following multiples. No separation between adjacent rows is
assumed. The result therefore goes beyond the separated-row hypothesis
of
[[theory/number_theory/L199_separated_grid_third_layer/_index|L199, whose
stronger linear bound applies to the original repeated-pattern grids]].

For [[problems/primes/E1143/_index|Problem 1143]], full rectangles with
this placement cannot reach the exponent $0.56213$ supplied by the
nonrectangular construction of
[[theory/number_theory/L203_rational_entropy_prime_block_bound/_index|L203]].
This is an obstruction to a specified construction, not a universal lower
bound for $G_\alpha$. The block must retain every row and column
location of this CRT placement. Substantial deletions from the rectangle,
other residue patterns and distant blocks are outside its conclusion.
The exponent $2/3$ is a lower bound for this family; its sharpness is not
claimed.

The sumset ingredient is the additive specialization of G. Petridis,
*New Proofs of Plünnecke-type Estimates for Product Sets in Groups*,
Combinatorica 32 (2012), 721--733,
[arXiv:1101.3507v3](https://arxiv.org/abs/1101.3507v3), Proposition 2.1,
pp. 5--6. Its statement and proof were read on 2026-10-15, and the needed
argument is included. The application to direct row-plus-column sums and
the median cut are author-recorded deductions by Plasma AI at tier 0, without
independent review or Lean proof.

Verify the minimal-growth lemma, the injectivity of the doubled sums,
and the exchange of each excluded following multiple for a preceding
one. There is no computational premise. The
[[research/prime_multiple_long_intervals/_index|research sketch]] places
this obstruction beside the sharp separated-grid count and the
three-projection construction.

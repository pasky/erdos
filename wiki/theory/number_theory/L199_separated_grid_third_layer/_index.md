---
name: theory/number_theory/L199_separated_grid_third_layer
title: The third layer of a separated prime grid
desc: Extending a rectangular prime-grid block with separated rows past three times its largest prime adds at least half as many new locations as primes, so this construction costs at least linearly.
id: L199
statement: |
  Let q, 0=a_1<...<a_r and 0=b_1<...<b_s be integers with
  a_(i+1)-a_i>b_s for 1<=i<r and 2a_r+3b_s<q, such that the numbers
  p_ij=q+a_i+b_j are distinct primes. Let S be a set of u>=1 index pairs
  (i,j), meeting r_S rows and s_S columns, let z be an integer with
  z congruent to a_i modulo p_ij for every (i,j) in S, let P be the
  largest p_ij with (i,j) in S, let alpha>=3 with K=floor(alpha P)<4q,
  and let T_S be the set of values a_i+2b_j with (i,j) in S. Count the
  integers divisible by at least one p_ij with (i,j) in S, each once.
  Then |T_S|>=ceil(u/2). Every block of K consecutive integers containing
  z-a_i and z+q+b_j for every (i,j) in S has count at least
  r_S+s_S+|T_S|, with equality for the block from z-q+1 to z-q+K. Every
  block of K consecutive integers contained in the interval from z-2q+1
  to z+4q-1 has count at least ceil(u/2). For the full grid S one has
  |T_S|>=rs-(r-1)floor(s/2). For every r,s>=1 and every real 3<=alpha<4,
  there exist grids satisfying these hypotheses and attaining this last
  bound, with a positive canonical block and exact core-retaining minimum
  r+s+rs-(r-1)floor(s/2).
status: proved
tier: 0
depends_on:
- L202
created: 2026-10-15T15:58:15Z
updated: 2026-10-15T15:58:15Z
---

# The third layer of a separated prime grid

[[theory/number_theory/_index|..]]

[[theory/number_theory/L199_separated_grid_third_layer/_proof|_proof]]: Outer-layer locations coincide only between adjacent rows, at most twice, and each missing following location forces a distinct preceding one into the block.

[[theory/number_theory/L199_separated_grid_third_layer/evidence/_index|evidence/]]: Brute-force the counts of all core-containing blocks and all blocks near the Chinese-remainder point for small separated prime grids.

***

The two-position construction of
[[theory/number_theory/L37_prime_multiple_block_extremum/_index|L37, the
exact extremum for 2<alpha<3]], uses a grid of primes $q+a_i+b_j$ and
Chinese remaindering, so that each prime's two multiples sit at a row
location $z-a_i$ and a column location $z+q+b_j$. The repeated prime
patterns found in its proof have separated rows: consecutive row offsets
differ by more than the largest column offset. This claim shows what
happens to that construction when the block is lengthened to
$\lfloor\alpha P\rfloor\ge3P$. Each prime gains a third multiple in the
block. In the canonical extension it is the layer $z+2q+a_i+2b_j$, and
separation forces that layer to have at least $\lceil u/2\rceil$
distinct locations. No block retaining the row and column locations does
better, and no block in the window around $z$ has fewer than
$\lceil u/2\rceil$ multiples. The [proof](_proof.md) counts the layers.

For [[problems/primes/E1143/_index|Problem 1143]] this is an exact
obstruction to one construction, not a bound on the problem. The cost
is linear in $u$, while Ruzsa's construction already has
$O((u\log u)^{2/3})$ multiples and
[[theory/number_theory/L201_type_class_long_block_bound/_index|L201 has
exponent log(27/4)/log 27]]. So the separated grids of L37, with their
Chinese-remainder placement, give nothing better than a linear count
past $3P$. The statement fixes the Chinese-remainder solution $z$, and
blocks far from $z$ realize other residue patterns, so it says nothing
about the least count for the same primes over all blocks. The
[[research/prime_multiple_long_intervals/_index|research account of long
blocks]] explains the cell sets that avoid the obstruction. The full-grid
bound $rs-(r-1)\lfloor s/2\rfloor$ is sharp for every $r,s$ and every
$3\le\alpha<4$, including prime realization. Its proof uses
[[theory/number_theory/L202_prime_realization_three_projections/_index|L202
to realize the equality pattern by primes using the Green--Tao theorem]].
The lower bounds and the exact minimum for any given grid are elementary
and do not use that theorem. Without separated rows,
[[theory/number_theory/L204_cartesian_prime_grid_obstruction/_index|L204
still gives a two-thirds-power obstruction for full Cartesian grids]].

This is author-recorded work by Plasma AI at tier 0, with no independent
review or Lean proof. Verify it by checking the multiplicity bounds, the
cluster disjointness and the exchange of each missing following location
for a distinct preceding one in the proof. The
[[theory/number_theory/L199_separated_grid_third_layer/evidence/_index|executable
evidence]] brute-forces every block position in both families for small
prime grids; it illustrates the statement and proves nothing beyond its
instances.

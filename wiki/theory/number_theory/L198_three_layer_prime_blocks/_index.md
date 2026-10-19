---
name: theory/number_theory/L198_three_layer_prime_blocks
title: Three-layer Chinese-remainder blocks of prime multiples
desc: Primes indexed by integer cells and placed by Chinese remaindering give a block of floor(alpha P) integers, 3<=alpha<4, whose multiples are exactly three layers counted by three projections of the cells.
id: L198
statement: |
  Let 3<=alpha<4 and let S be a nonempty finite set of pairs (x,y) of
  integers on which y-x takes distinct values. Let omega>=1 be an integer
  with |x|<=omega and |y|<=omega on S, and let q be an integer with
  (4-alpha)q>=16 omega+1 such that q+y-x is prime for every (x,y) in S.
  Let P be the largest of these |S| distinct primes. Then some block of
  floor(alpha P) consecutive positive integers contains exactly |X|+|Y|+|W|
  integers divisible by at least one of these primes, each integer counted
  once, where X, Y and W are the sets of values of x, of y and of 2y-x on S.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T15:58:15Z
updated: 2026-10-15T15:58:15Z
---

# Three-layer Chinese-remainder blocks of prime multiples

[[theory/number_theory/_index|..]]

[[theory/number_theory/L198_three_layer_prime_blocks/_proof|_proof]]: The multiples of every cell prime fall in layers near multiples of q, and a block of floor(alpha P) integers fits strictly between the layers t=-1 and t=3.

[[theory/number_theory/L198_three_layer_prime_blocks/evidence/_index|evidence/]]: Build type-class cell sets, keep the cells with prime differences, place the block of the proof and count its prime multiples directly.

***

Each cell $(x,y)$ names the prime $p=q+y-x$. A Chinese-remainder
choice of $z$ puts the multiples of $p$ at $z+tq+(1-t)x+ty$ for all
integers $t$, so the multiples at $t=0,1,2$ are $z+x$, $z+q+y$ and
$z+2q+2y-x$. The [proof](_proof.md) places a block of
$\lfloor\alpha P\rfloor$ integers that holds exactly these three layers.
The layers are disjoint, and within a layer two primes share a location
exactly when their cells share the value of $x$, of $y$ or of $2y-x$.
So the count is the sum of the three projection sizes, while the number
of primes is $|S|$.

This is the three-position form of the rectangular prime-grid
construction of
[[theory/number_theory/L37_prime_multiple_block_extremum/_index|L37,
whose two-position block has only the row and column layers]]. With
$x=-a_i$ and $y=b_j$ on a grid of primes $q+a_i+b_j$, layers $0$ and
$1$ are its row and column locations, and layer $2$ is the new set of
locations $z+2q+a_i+2b_j$. The lemma needs no rectangle, so any cell set
can be used; the
[[research/prime_multiple_long_intervals/_index|research account of long
blocks]] explains why the general shape matters. The lemma is the
construction step of
[[theory/number_theory/L200_long_block_sums_differences_exponent/_index|L200,
which identifies the growth exponent for 3<=alpha<4]], and of
[[theory/number_theory/L201_type_class_long_block_bound/_index|L201, an
explicit bound with exponent log(27/4)/log 27]].
[[theory/number_theory/L202_prime_realization_three_projections/_index|L202
supplies the missing simultaneous primes after dilating any cell set]].
It makes no claim about
blocks or prime sets of any other form.

This is author-recorded work by Plasma AI at tier 0, with no independent
review or Lean proof. It uses only the Chinese remainder theorem and
integer bookkeeping. It assumes the primes: finding cells and $q$ for
which every $q+y-x$ is prime is left to its consumers. Verify it by
checking the layer formula, the four endpoint inequalities and the
disjointness of the layers in the proof. The
[[theory/number_theory/L198_three_layer_prime_blocks/evidence/_index|executable
evidence]] counts actual blocks for explicit instances; it illustrates
the conventions and proves nothing beyond its instances.

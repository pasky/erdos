---
name: theory/number_theory/L200_long_block_sums_differences_exponent
title: The long-block exponent is a sums–differences exponent
desc: For 3<=alpha<4 the least number of distinct prime multiples in a block of floor(alpha P) integers grows like u^(1/beta+o(1)), where beta is the best ratio log|S|/log of the largest of three projections of an integer cell set.
id: L200
statement: |
  For a finite set S of pairs (x,y) of integers on which y-x takes
  distinct values, let N(S) be the largest of the numbers of distinct
  values taken on S by x, by y and by 2y-x, and let beta be the supremum
  of log|S|/log N(S) over such sets S with |S|>=2. For real alpha>=1 and
  integer u>=1 let G_alpha(u) be the minimum, over all sets of u distinct
  primes with largest member P and all blocks of floor(alpha P)
  consecutive positive integers, of the number of integers in the block
  divisible by at least one of the primes, each counted once. Then
  1<beta<=2, G_alpha(u)>=u^(1/beta) for every real alpha>=3 and integer
  u>=2, and log G_alpha(u)/log u tends to 1/beta as u tends to infinity
  for every real alpha with 3<=alpha<4.
status: proved
tier: 0
depends_on:
- L198
created: 2026-10-15T15:58:15Z
updated: 2026-10-15T15:58:15Z
---

# The long-block exponent is a sums–differences exponent

[[theory/number_theory/_index|..]]

[[theory/number_theory/L200_long_block_sums_differences_exponent/_proof|_proof]]: Every long block yields a cell set whose projections are counted multiples, and tensor powers of a near-extremal cell set with primes chosen by averaging give the matching upper bound.

***

For [[problems/primes/E1143/_index|Problem 1143]] at length ratios
$3\le\alpha<4$, this determines the growth exponent of the least count
$G_\alpha(u)$ up to one constant $\beta$ of additive combinatorics. The
[proof](_proof.md) gives the lower bound from the three consecutive
multiples that every prime has in a block of at least $3P$ integers.
The upper bound applies tensor powers of near-extremal cell sets, a
prime-number-theorem choice of $q$ and
[[theory/number_theory/L198_three_layer_prime_blocks/_index|L198, which
turns any cell set with prime differences into a block counted by its
three projections]]. The two bounds meet in the exponent, so three-layer
Chinese-remainder blocks are extremal up to a factor $u^{o(1)}$ among all
prime sets and blocks. This is the exponent form of the three-term case
of
[[../library/primes/green_2017_arithmetic_kakeya_conjecture_katz_tao/proposition_4_1|Proposition
4.1 of Green and Ruzsa, which places G_3 between F'_3 and 3F'_3]],
extended from $\alpha=3$ to $3\le\alpha<4$ and proved here without the
Green–Tao theorem.

**Dependency roles.** L198 supplies the exact three-layer block for each
selected cell set; this proof chooses the cells and $q$ that make its
hypotheses hold.

The constant $\beta$ is the sums–differences exponent of Katz and Tao
for the slopes $0$, $1$ and $\infty$: the change of variables
$(a,b)=((2y-x)/2,\,x/2)$ turns $y-x$ into $a-b$ and the three
projections into $a$, $b$ and $a+b$. Integer cells lose nothing here: a
real configuration can be replaced by a rational one with the same
coincidences, since these are given by linear equations with integer
coefficients; rational points can avoid the finitely many additional
equality hyperplanes that would create new coincidences. A rational
configuration can then be scaled to integers. The value of $\beta$ is
not determined here. Combining the lower bound with
[[theory/number_theory/L203_rational_entropy_prime_block_bound/_index|the
explicit upper bound of L203]] gives $1/\beta\le0.56213$.
Bounds on $\beta$ from the literature,
with their reading depth here, are on the
[[research/prime_multiple_long_intervals/_index|research account of long
blocks]]. They are not used in this claim.

This is author-recorded work by Plasma AI at tier 0, with no independent
review or Lean proof and no novelty claim. The upper bound uses the prime
number theorem. Verify it by checking the lower-bound projection argument,
the injectivity of the tensor-power differences and the averaging over
$q$ in the proof. It determines no value of $G_\alpha(u)$, no exponent
for $\alpha\ge4$, and no exact minimum for a prescribed set of primes.
The lower bound does apply to every prescribed prime set. The stronger
finite comparison
[[theory/number_theory/L202_prime_realization_three_projections/_index|L202]]
realizes whole cell sets using the Green--Tao theorem; the proof here
retains the alternative using only prime-number-theorem averaging.

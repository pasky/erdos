---
name: theory/number_theory/L201_type_class_long_block_bound
title: A type-class bound for long prime-multiple blocks
desc: Three-cell type classes give an explicit exponent theta=log(27/4)/log 27 for long prime-multiple blocks, with a small logarithmic factor under Green--Tao realization and an elementary alternative using the prime number theorem.
id: L201
statement: |
  Let theta=log(27/4)/log 27, so 0.5793<theta<0.5794. There is an
  absolute constant C such that for every real alpha with 3<=alpha<4
  and every integer u>=2 there are u distinct primes, with largest
  member P, and a block of floor(alpha P) consecutive positive integers
  containing at most C u^theta (log u)^(theta-1/2) integers divisible
  by at least one of the primes, each integer counted once.
status: proved
tier: 0
depends_on:
- L198
- L202
created: 2026-10-15T15:58:15Z
updated: 2026-10-15T16:33:51Z
---

# A type-class bound for long prime-multiple blocks

[[theory/number_theory/_index|..]]

[[theory/number_theory/L201_type_class_long_block_bound/_proof|_proof]]: Balanced three-cell words give exact multinomial and projection counts; prime averaging gives an elementary bound, while full prime realization and Stirling's formula give a smaller logarithmic factor.

***

For [[problems/primes/E1143/_index|Problem 1143]] this bounds the least
count over prime sets for every length ratio $3\le\alpha<4$ by
$C u^\theta(\log u)^{\theta-1/2}$, where
$\theta-1/2\approx0.0794$. The constant is uniform in $\alpha$.
In this range
[[../library/primes/ruzsa_1995_few_multiples_many_primes/theorem|Ruzsa's
theorem gives the exponent 2/3]], and the Green–Ruzsa bound recorded on
the problem page is proved for large integer ratios. Erdős's lower bound
for longer intervals is untouched.

The [proof](_proof.md) starts from three cells, $(0,1)$, $(2,1)$ and
$(2,2)$, whose three projections each take two values. It keeps the
sequences of $3m$ cells that use each cell exactly $m$ times (a type
class). Then $(3m)!/(m!)^3$ cells share only $\binom{3m}{m}$ values in
each projection, which gives the exponent $\theta$. A
prime-number-theorem choice of $q$ makes enough of the differences
prime to prove the alternative bound $O_\alpha(u^\theta(\log u)^2)$;
then
[[theory/number_theory/L198_three_layer_prime_blocks/_index|L198, the
exact three-layer block count]], places the block.

**Dependency roles.** L198 supplies the block counted by the three
projections for the proof using the prime number theorem.
[[theory/number_theory/L202_prime_realization_three_projections/_index|L202
realizes every cell in a type class by primes]], using the Green--Tao
theorem, and gives the stronger displayed bound by Stirling's formula.

The three cells are, after the change of variables
$(a,b)=((2y-x)/2,\,x/2)$, the classical sums–differences example
$\{(0,1),(1,0),(1,1)\}$ that
[[../library/additive_combinatorics/lemm_2015_new_counterexamples_sums_differences/_index|Lemm attributes to Ruzsa]].
The type classes follow the
[[../library/additive_combinatorics/lemm_2015_new_counterexamples_sums_differences/proposition_1_1|limiting entropy-to-set construction of Proposition 1.1]];
the proof here supplies the exact counts and logarithmic factor for this
example. The exponent is $1/\beta_0$ for that example's ratio
$\beta_0=\log27/\log(27/4)$, which is a lower bound for the constant
$\beta$ of
[[theory/number_theory/L200_long_block_sums_differences_exponent/_index|L200,
the exact growth exponent 1/beta]]. Better sums–differences examples
lower the exponent further, as the
[[research/prime_multiple_long_intervals/_index|research account of long
blocks]] records. The complete type classes themselves retain the factor
$(\log u)^{\theta-1/2}$; removing the loss in selecting primes does not
remove this factor. No bound $O(u^\theta)$ is proved here. The source
example and its entropy method retain Ruzsa's and Lemm's credit, and no
novelty is claimed for their use.

This is author-recorded work by Plasma AI at tier 0, with no independent
review or Lean proof. Its stronger bound uses the Green--Tao theorem and
its elementary alternative uses the prime number theorem; both use
Chinese remaindering. Verify the type-class counts, injectivity of
base-three differences, and the two parameter choices in the proof. The
[[theory/number_theory/L198_three_layer_prime_blocks/evidence/_index|L198
evidence]] counts actual blocks for these type classes with $m\le3$; for
$m=3$, $\alpha=3$ it finds 302 primes with only 220 multiples in one
block. A finite instance proves no exponent. The claim gives no lower
bound and says nothing about $\alpha\ge4$ or a prescribed set of primes.

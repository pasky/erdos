---
name: theory/number_theory/L203_rational_entropy_prime_block_bound
title: A rational seven-point bound for long prime-multiple blocks
desc: A rational measure on Lemm's seven-point sums–differences configuration gives an absolute bound C u^0.56213 for the minimum distinct-multiple count, uniformly over all length ratios from three up to four.
id: L203
statement: |
  There is an absolute constant C such that for every real alpha with
  3<=alpha<4 and every integer u>=2 there are u distinct primes with
  largest member P and a block of floor(alpha P) consecutive positive
  integers containing at most C u^(56213/100000) integers divisible by
  at least one chosen prime, each integer counted once.
status: proved
tier: 0
depends_on:
- L202
created: 2026-10-15T16:33:51Z
updated: 2026-10-15T16:33:51Z
---

# A rational seven-point bound for long prime-multiple blocks

[[theory/number_theory/_index|..]]

[[theory/number_theory/L203_rational_entropy_prime_block_bound/_proof|_proof]]: A fixed rational measure has projection entropy below 0.56213 times its joint entropy; exact type classes turn this strict margin into an all-size prime-block bound.

[[theory/number_theory/L203_rational_entropy_prime_block_bound/evidence/_index|evidence/]]: Recompute the seven-point measure's marginals and use rational logarithm enclosures to certify that its largest projection entropy is less than 0.56213 times its joint entropy.

***

For [[problems/primes/E1143/_index|Problem 1143]], this is an upper
bound on the minimum over prime sets. It follows from type classes of a
seven-point configuration of Marius Lemm, with an explicit rational
probability measure. The [proof](_proof.md) derives the asymptotic
construction from exact multinomial counts, and the
[[theory/number_theory/L203_rational_entropy_prime_block_bound/evidence/_index|rational
logarithm certificate]] checks the one numerical entropy inequality used.
The constant $C$ is independent of $\alpha$; the primes and the block
are allowed to depend on $\alpha$ and $u$.

**Dependency role.**
[[theory/number_theory/L202_prime_realization_three_projections/_index|L202
realizes each whole type class by primes without a loss in cardinality]].
Its external premise is the Green--Tao theorem. The construction improves
the simpler
[[theory/number_theory/L201_type_class_long_block_bound/_index|three-cell
bound of L201]], but is not a new sums--differences example or a claim of
improvement over the published sums--differences record.

The source is M. Lemm, *New counterexamples for sums-differences*,
Proc. Amer. Math. Soc. 143 (2015), 3863--3868, read in the
[[../library/additive_combinatorics/lemm_2015_new_counterexamples_sums_differences/_index|held arXiv:1404.3745v2 edition]].
Its
[[../library/additive_combinatorics/lemm_2015_new_counterexamples_sums_differences/theorem_2_1|Theorem 2.1 supplies the seven-point configuration]].
The seven points and rounded probabilities were checked on pp. 4--5
on 2026-10-15; the canonical library records were read on the same date.
The library result page distinguishes the claimed optimized ratio above
$1.77898$ from the ratio of the printed rounded weights, which falls
slightly below it. The measure here is stated exactly and has its own
rational certificate; it does not rely on either numerical claim.

The library's
[[../library/additive_combinatorics/lemm_2015_new_counterexamples_sums_differences/proposition_1_1|Proposition 1.1 record qualifies the entropy-to-set implication as a limiting statement]].
The proof here constructs integer cells directly and uses a strict
entropy margin below $0.56213$ to pass to every $u$. It does not infer
attainment at a limiting exponent. The source pages retain their
claims-checked reading coverage; that coverage is not independent
acceptance of this prime-block deduction.

This is an author-recorded deduction by Plasma AI at tier 0, with no
independent review or Lean proof. Verify the seven distinct differences,
the marginal masses and logarithm enclosures, the type-class encoding,
and the passage from its sizes to every $u$. The
[[research/prime_multiple_long_intervals/_index|research sketch]] records
the remaining gap in the exponent. This result does not compute a
prescribed-prime-set minimum and does not resolve the catalog problem.

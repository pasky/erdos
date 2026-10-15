---
name: research/methods/shifted_prime_moments
title: Moments of an additive function over primes through the factors of p - 1
desc: |
  Turns equidistribution of the prime factors of p - 1 into the first two
  moments over primes of the additive function behind the totient iteration
  count, the route by which its normal order was made unconditional.
problems: [408, 417]
review_status: unreviewed
created: 2026-10-14T20:25:44Z
updated: 2026-10-14T20:25:44Z
---

# Moments of an additive function over primes through the factors of p - 1

***

This method page is author-recorded. It summarizes a method from two sources:
the 1990 paper of Erdős, Granville, Pomerance and Spiro
([[../library/arithmetic_functions/erdos_1990_normal_behavior_iterates_arithmetic_functions/_index|its card]]) and Plasma AI's 2026 preprint on
[[problems/arithmetic_functions/E0408/_index|Problem 408]]
([[../library/arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/_index|its card]]). It states the method's inputs and limits. It
verifies nothing. The preprint's claim is accepted on its formalization, as
[[problems/arithmetic_functions/E0408/claims/2026_10_14_plasma_ai|its claim page]]
records: this corpus rebuilt and replayed the formalization and reviewed its
statements on 2026-10-14. The paper's proof itself is unreviewed.

## The method

Let $F$ be the completely additive function with $F(2)=1$ and
$F(p)=F(p-1)$ for odd primes $p$. It counts the even terms among
$n,\varphi(n),\varphi_2(n),\dots$, and it differs from the number $f(n)$ of
totient iterations needed to reach $1$ by at most $1$. Two facts about $F$
drive the method:

- $\log n/\log3\le F(n)\le\log n/\log2$.
- Since $F(p)=F(p-1)$, an average of $F$ or $F^2$ over primes $p\in(x,2x]$ is
  an average over the prime factors $q$ of $p-1$ of the values $F(q)$ and
  $F(q)F(r)$.

If the prime factors of $p-1$ are distributed like the harmonic weight
$1/(q_1\cdots q_k)$, with an error summable over the scales, these averages
become harmonic sums of the prime values of $F$. That gives relations between
the first two moments of $F$ over primes, a renewal-type recursion across the
scales. Solving them gives a constant $\alpha\in[1/\log3,1/\log2]$ with
$F(n)$, and hence $f(n)$, of normal order $\alpha\log n$, with an explicit
variance bound.

## Inputs

- **The equidistribution input.** In the 1990 paper it is a strong form of
  the Elliott--Halberstam conjecture
  ([[../library/arithmetic_functions/erdos_1990_normal_behavior_iterates_arithmetic_functions/theorem_2_2|Theorem 2.2]]), which is unproven. The 2026 preprint
  replaces it by its quantitative rectangle estimate (Theorem 2.1, recorded
  on its card): for $1\le k\le3$ prime factors in ranges
  $(x^{u_i},x^{v_i}]$ kept a distance $c(\log\log x)^{-20}$ from the
  boundary, with bounded weights that do not depend on the last factor, the
  average over primes matches the harmonic sum up to $O((\log\log x)^{-300})$.
  It extends
  [[../library/arithmetic_functions/openai_2026_poisson_dirichlet_law_prime_predecessors/theorem_7_1|Theorem 7.1 of the Poisson--Dirichlet manuscript]]
  and rests on
  [[../library/primes/openai_2026_quasi_riemann_hypothesis_zero_free_half_plane_7_8/theorem_1_1|the zero-free half-plane]]
  and the
  [[../library/arithmetic_functions/openai_2026_weighted_dilation_graphs_smooth_shifted_primes_totient_fibers/_index|weighted-dilation-graph]]
  estimates.
- **Weights on one or two factors.** The rectangle estimate allows weights
  that depend on all but one prime factor. Summing over an auxiliary prime
  factor (Section 3 of the preprint) extends this to arbitrary bounded weights
  on one or two factors, at a small cost.

## Where it applies

- [[problems/arithmetic_functions/E0408/_index|Problem 408]]: the first two
  questions, as the preprint's claim, which is accepted on its formalization;
  the paper's proof is unreviewed.
- **The average order.** The average order $\alpha\log n$ of $f$, Theorem 2.1
  of the 1990 paper, follows from the variance bound by Cauchy--Schwarz
  without that paper's hypothesis. The deduction is drawn on the preprint's
  card.
- [[problems/arithmetic_functions/E0417/_index|Problem 417]]: background only.
  The rectangle estimate is the kind of control on the factors of $p-1$ that
  counts of totient values use, but no deduction is recorded.

## Limits

- At most three prime factors at a time, and weights independent of the last
  one.
- Ranges bounded away from the edges of the region. The preprint bounds the
  contribution of the omitted prime factors separately, in its Section 4.
- The constant $\alpha$ is not determined.
- The method gives nothing on the largest prime factor of $\varphi_k(n)$,
  Problem 408's third question.
- It does not reach the 1990 paper's statements on iterates of $\sigma$ and
  its Conjecture 4
  ([[problems/arithmetic_functions/E0410/_index|Problem 410]],
  [[problems/arithmetic_functions/E0412/_index|Problem 412]],
  [[problems/arithmetic_functions/E0955/_index|Problem 955]]). That paper does
  not derive them from its hypotheses.

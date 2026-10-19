---
name: problems/irrationality/E0269
title: Problem 269
desc: |
  Asks whether $\sum_n 1/\operatorname{lcm}(a_1,\ldots,a_n)$ is irrational,
  where $a_1<a_2<\cdots$ are the integers whose prime factors lie in a fixed
  finite set of at least two primes.
tags:
- Irrationality
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-18T03:06:13Z
---

# Problem 269

[[problems/irrationality/_index|..]]

[[problems/irrationality/E0269/claims/_index|claims/]]: The 2 claim pages of Problem 269, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $P$ be a finite set of primes with $\lvert P\rvert \geq 2$
and let $\{a_1<a_2<\cdots\}=\{ n\in \mathbb{N} : \textrm{if }p\mid n\textrm{
then }p\in P\}$. Is the sum

$$
\sum_{n=1}^\infty \frac{1}{[a_1,\ldots,a_n]},
$$

where $[a_1,\ldots,a_n]$ is the lowest common multiple of $a_1,\ldots,a_n$,
irrational?

**Status.** Open.

**Source.** [erdosproblems.com/269](https://www.erdosproblems.com/269), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #269,
https://www.erdosproblems.com/269.

**References.**

- [Er88c] Erdős, P., On the irrationality of certain series: problems and
  results. New advances in transcendence theory (Durham, 1986) (1988), 102-109.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/269.lean).

## Current assessment

Steve Fan posted a proof in the problem's thread on 26 June 2026 that the sum
is transcendental for every two-prime set $P=\{p,q\}$; it is a pending
partial claim on
[[problems/irrationality/E0269/claims/2026_06_26_fan|its claim page]]. The
[[research/smooth_lcm_series/_index|two-prime factorization]] gives a
complete author-recorded deduction of the same conclusion, using
Bugeaud–Laurent, arXiv:2203.12901v1, Theorem 1.1. The
numbered theorem's normalization and hypotheses have been checked in the primary
TeX; its proof has not been independently examined. Repeated running-lcm values
are retained in the sum. This answers only the two-prime case and does not
determine the question for larger finite prime sets.

For three distinct primes, the
[[research/smooth_lcm_three_prime/_index|three-prime analysis]] retains every
smooth-number contribution and gives exact carry, event and integer-block
identities. The author-recorded tier-0 claims
[[theory/irrationality/L189_lcm_series_cone_no_product/_index|L189]] and
[[theory/irrationality/L190_three_prime_no_finite_planar_partition/_index|L190]]
exclude, respectively, a unimodular product decomposition of the expanded
lattice set and a finite signed decomposition into halfspace regions whose
normal coefficients have rational rank at most two. The separate termwise
rank obstruction is credited to Cook at the research page. These results do
not exclude identities that hold only after weighted summation. The actual
normalized tails grow quadratically; no irrationality contradiction or
applicable value theorem for the coupled sum is supplied. This work by Plasma
AI has no independent review and leaves the three-prime case open.

For infinite $P$ the sum is always irrational; erdosproblems.com records that
Erdős calls this a simple exercise in [Er88c]. The Statement excludes that
case, and this page sets it aside as a variant. Steve Fan's proof of it, posted
in the problem's thread on 11 October 2025, is recorded as rejected on
[[problems/irrationality/E0269/claims/2025_10_11_fan|its claim page]], as
answering that variant.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/irrationality/bugeaud_2022_transcendence_continued_fraction_hecke_mahler/_index|bugeaud_2022_transcendence_continued_fraction_hecke_mahler]]
- [[../library/irrationality/cook_2026_running_least_common_multiples/_index|cook_2026_running_least_common_multiples]]
- [[../library/irrationality/erdos_1988_irrationality_certain_series_problems_results/_index|erdos_1988_irrationality_certain_series_problems_results]]

<!-- END problem library links -->

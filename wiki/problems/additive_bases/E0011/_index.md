---
name: problems/additive_bases/E0011
title: Problem 11
desc: |
  Asks whether every large odd integer is the sum of a squarefree number and a
  power of 2.
tags:
- Number theory
- Additive bases
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 11

[[problems/additive_bases/_index|..]]

***

**Statement.** Is every large odd integer $n$ the sum of a squarefree number and
a power of 2?

**Status.** Open.

**Source.** [erdosproblems.com/11](https://www.erdosproblems.com/11), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #11,
https://www.erdosproblems.com/11.

**References.**

- [GrSo98] Granville, A. and Soundararajan, K., [[../library/additive_bases/granville_1998_binary_additive_problem_erdos_order_2_mod_p_2/_index|A Binary Additive Problem of Erdős and the Order of $2$ mod $p^2$]].
  The Ramanujan Journal (1998), 283-298.
- [Gu04] Guy, Richard K., Unsolved problems in number theory. Third edition,
  Problem Books in Mathematics, Springer, New York (2004), xviii+437 pp.;
  section A19 "Values of $n$ making $n-2^k$ prime. Odd numbers not of the
  form $\pm p^a\pm2^b$.", printed p. 67: the question whether some odd
  integer is not of the form $2^k+s$ with $s$ squarefree, with no example
  found below $1.4\cdot10^9$.
  Library home:
  [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]].
- [He24b] C. Hercher, On the Sum of Squarefree Integers and a Power of Two.
  arXiv:2411.01964 (2024).

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/11.lean).

## Current assessment

A bounded exponent search cannot resolve the eventual assertion. In the held
[[../library/additive_bases/hercher_2024_sum_squarefree_integers_power_two/_index|Hercher account]],
Theorem 5 covers odd $1<n<2^{50}$ using exponents $1\le k\le13$; its
computation has not been replayed here. Remark 4 gives the Chinese remainder
obstruction for any fixed positive-exponent cap. The argument below also
covers exponent zero.

Fix $K\ge1$ and choose distinct odd primes $q_1,\ldots,q_K$. The congruences

$$
n\equiv1\pmod4,\qquad n\equiv2^k\pmod{q_k^2}\quad(1\le k\le K)
$$

have infinitely many positive solutions by the Chinese remainder theorem.
For sufficiently large solutions all differences are positive: $n-1$ is
divisible by $4$, and $n-2^k$ is divisible by $q_k^2$. None is squarefree.
Thus infinitely many odd integers defeat every fixed cap $0\le k\le K$.
This author-recorded observation by Plasma AI does not defeat exponents that grow with $n$.

The held Granville–Soundararajan conditional exceptional-set estimate still
allows an infinite exceptional set. Neither it nor a larger fixed search
window removes the all-exponents gap. The source statements were inspected;
no independent proof review or comprehensive new status search is asserted.
A useful new estimate must treat all admissible exponents up to $\log_2 n$.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/additive_bases/granville_1998_binary_additive_problem_erdos_order_2_mod_p_2/_index|granville_1998_binary_additive_problem_erdos_order_2_mod_p_2]]
- [[../library/additive_bases/hercher_2024_sum_squarefree_integers_power_two/_index|hercher_2024_sum_squarefree_integers_power_two]]
- [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]]

<!-- END problem library links -->

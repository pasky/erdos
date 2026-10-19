---
name: problems/integer_sequences/E1101
title: Problem 1101
desc: |
  Asks whether a good sequence of pairwise coprime integers with convergent
  reciprocal sum can have $u_n<n^{O(1)}$, or at least $u_n\le e^{o(n)}$.
tags:
- Number theory
status: open
claim: none
parts: [polynomial, subexponential]
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 1101

[[problems/integer_sequences/_index|..]]

[[problems/integer_sequences/E1101/claims/_index|claims/]]: The 1 claim page of Problem 1101, one per claimant's result; the problem's standing derives from them.

***

**Statement.** If $u=\{u_1<u_2<\cdots\}$ is a sequence of integers such that
$(u_i,u_j)=1$ for all $i\neq j$ and $\sum \frac{1}{u_i}<\infty$ then let
$\{a_1<a_2<\cdots\}$ be the sequence of integers which are not divisible by any
of the $u_i$. For any $x$ define $t_x$ by

$$
u_1\cdots u_{t_x}\leq x< u_1\cdots u_{t_x}u_{t_x+1}.
$$

We call such a sequence $u_i$ good if, for all $\epsilon>0$, if $x$ is
sufficiently large then

$$
\max_{a_k<x} (a_{k+1}-a_k) < (1+\epsilon)t_x \prod_{i}\left(1-\frac{1}{u_i}\right)^{-1}.
$$

Is there a good sequence such that $u_n< n^{O(1)}$? Is there a good sequence
such that $u_n\leq e^{o(n)}$?

**Status.** Open. Bloom's catalog labeled the problem OPEN (page last edited 19
October 2025). Its two questions are the problem's two parts. Erdős expected the
first to have a negative answer and the second a positive one. The second asks
whether some good sequence has $u_n\leq e^{o(n)}$. It has one pending partial
claim,
[[problems/integer_sequences/E1101/claims/2026_04_27_li|Li's subexponential good sequence of 2026]],
which constructs a good sequence of primes with $u_n=\exp((1+o(1))\sqrt n)$. The
first asks whether some good sequence has $u_n<n^{O(1)}$. It has no claim.

**Source.** [erdosproblems.com/1101](https://www.erdosproblems.com/1101),
accessed 2026-09-04. Cite as: T. F. Bloom, Erdős Problem #1101,
https://www.erdosproblems.com/1101.

**References.**

- [Er81h] Erdős, P., Some problems and results on additive and multiplicative
  number theory. Analytic number theory (Philadelphia, Pa., 1980) (1981),
  171-182.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/1101.lean).

## Current assessment

These deductions leave the full question unresolved. They have author-recorded
standing; this assessment is limited to the arguments and source interfaces
stated below. No comprehensive search for recent proof claims is recorded here.

In the nondegenerate setting $u_i>1$, pairwise coprime, $\sum1/u_i<\infty$, put
$\delta=\prod_i(1-1/u_i)>0$, $Q_t=\prod_{i\le t}u_i$, and
$G(x)=\max_{a_k<x}(a_{k+1}-a_k)$ for the free integers. Goodness requires for
every $\epsilon>0$ the uniform eventual bound $G(x)<(1+\epsilon)t_x/\delta$, not
merely a most-$x$ assertion.

CRT gives $y\in[0,Q_t)$ with $y+i\equiv0\pmod{u_i}$,
$1\le i\le t$. It cannot be 0, since the first congruence would
give $u_1\mid1$. Thus $y+1,\ldots,y+t$ are all excluded.
There are infinitely many free integers: the first $s$ divisors give
density $\prod_{i\le s}(1-1/u_i)$ by CRT, and the tail removes
a proportion at most $\sum_{i>s}1/u_i$, tending to zero.
Since 1 is free, the nearest free integers on either side satisfy
$a\le y<Q_t$, $b\ge y+t+1$. They are consecutive, so
$$
 G(Q_t)\ge t+1,\qquad t_{Q_t}=t.
$$
Its leading constant 1 is below $\delta^{-1}$. This neither
disproves polynomial goodness nor certifies any construction.

The Li claim card describes a 2026 construction with $\log u_n=\sqrt
n+O(n^{-1/2})$ and a probabilistic exclusion argument. The [primary
manuscript](https://drive.google.com/file/d/1rRfKzo0JMjUYlzgJ0kGvj_HUVXiit9-M/view)
was not inspected as proof. Its excluding-certificates lemma and uniform-in-$x$
conclusion are the relevant uninspected proof sites. The Erdős display (3.5)
account was also read; its original formulation ambiguity is not substituted for
the exact erdosproblems.com quantifiers.

The unresolved obligation is, for the pending part, to validate the
probability/covering estimate uniformly in x. For polynomial growth: beat the
allowed delta^(-1) factor, not just obtain a CRT gap of order t_x. A useful test
is to inspect, if the primary proof becomes available, Li's exact certificate
count and Borel-Cantelli quantifiers; for a polynomial obstruction, first prove
a gap larger than (1+epsilon)delta^(-1)t_x. Stop at a claim-page summary, a gap
at only the t_x scale, or nonuniform-in-x estimates.

Source interfaces:
[[../library/additive_bases/erdos_1981_problems_results_additive_multiplicative_number_theory/display_3_5|Displays
(3.3')-(3.5), question and proof pointer]].

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/additive_bases/erdos_1981_problems_results_additive_multiplicative_number_theory/_index|erdos_1981_problems_results_additive_multiplicative_number_theory]]
- [[../library/additive_bases/erdos_1981_problems_results_additive_multiplicative_number_theory/display_3_5|erdos_1981_problems_results_additive_multiplicative_number_theory / display_3_5]]
- [[../library/integer_sequences/li_2026_subexponential_good_sequence/_index|li_2026_subexponential_good_sequence]]
- [[../library/integer_sequences/li_2026_subexponential_good_sequence/lemma_1|li_2026_subexponential_good_sequence / lemma_1]]
- [[../library/integer_sequences/li_2026_subexponential_good_sequence/theorem_1|li_2026_subexponential_good_sequence / theorem_1]]

<!-- END problem library links -->

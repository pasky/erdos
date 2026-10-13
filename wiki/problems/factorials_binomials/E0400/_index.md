---
name: problems/factorials_binomials/E0400
title: Problem 400
desc: |
  Asks, for each $k\ge2$, whether $\sum_{n\le x}g_k(n)\sim c_kx\log x$ and
  whether $g_k(n)=c_k\log x+o(\log x)$ for almost all $n<x$, where $g_k(n)$ is
  the largest value of $a_1+\cdots+a_k-n$ with $a_1!\cdots a_k!\mid n!$.
tags:
- Number theory
- Factorials
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-07T02:07:29Z
---

# Problem 400

[[problems/factorials_binomials/_index|..]]

***

**Statement.** For any $k\geq 2$ let $g_k(n)$ denote the maximum value of

$$
(a_1+\cdots+a_k)-n
$$

where $a_1,\ldots,a_k$ are integers such that $a_1!\cdots a_k! \mid n!$. Can one
show that

$$
\sum_{n\leq x}g_k(n) \sim c_k x\log x
$$

for some constant $c_k$? Is it true that there is a constant $c_k$ such that for
almost all $n<x$ we have

$$
g_k(n)=c_k\log x+o(\log x)?
$$

**Status.** Open.

**Source.** [erdosproblems.com/400](https://www.erdosproblems.com/400), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #400,
https://www.erdosproblems.com/400.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/400.lean).

## Current assessment

**Open; a constant $c_k$ would lie between $3(k-1)/\log12$ and
$(k-1)/\log2$, but no constant is shown to exist.** The site's commentary
(read 2026-09-05) reports Erdős and Graham's remark [ErGr80, p. 77] that
$g_k(n)\ll_k\log n$ is easy to show while the best possible constant is
unknown, and points to
[[problems/factorials_binomials/E0401/_index|Problem 401]]. Eric Li's
preprint [[../library/factorials_binomials/li_2026_prime_power_rarefaction_density_one_lower/_index|Li 2026]]
(arXiv:2606.23661v2, with no journal reference) names the problem and
proves three bounds for every fixed $k\ge2$:

- [[../library/factorials_binomials/li_2026_prime_power_rarefaction_density_one_lower/theorem_1_1|Theorem 1.1]]:
  for every $\varepsilon>0$,
  $g_k(n)\ge(3(k-1)/\log12-\varepsilon)\log n$ for all but $o(x)$ integers
  $n\le x$;
- [[../library/factorials_binomials/li_2026_prime_power_rarefaction_density_one_lower/theorem_1_2|Theorem 1.2]]:
  $g_k(n)\le(k-1)\log_2n+\log_2\log n+O_k(1)$ for every large $n$;
- [[../library/factorials_binomials/li_2026_prime_power_rarefaction_density_one_lower/corollary_1_3|Corollary 1.3]]:
  the lower and upper limits of $\frac1{x\log x}\sum_{n\le x}g_k(n)$ lie in
  $[3(k-1)/\log12,(k-1)/\log2]$.

A constant $c_k$ as in either question would therefore lie in that interval,
which for $k=2$ is $[1.2072\ldots,1.4426\ldots]$ (p. 2). Neither question is
answered: the bounds show neither that $\frac1{x\log x}\sum_{n\le x}g_k(n)$
converges nor that $g_k(n)/\log x$ concentrates for almost all $n<x$, and Li
asks whether $(k-1)/\log2$ is the true constant (Question 9.3, p. 26). As
they settle no instance of either question, the results get no claim page,
and the problem stays open. The card records Theorem 1.2 and Corollary 1.3
as read through, and Theorem 1.1 and the digit-sum Theorem 1.4 it rests on
as read for structure only; no proof is reviewed here.

In the problem's forum thread Samuel Korsky (account SamKorsky) derived on
16 June 2026 a weaker lower bound from Theorem 1 of Carl Pomerance's note
[[../library/factorials_binomials/pomerance_2026_remarks_middle_binomial_coefficient/_index|Pomerance 2026]]
(Integers 26 (2026), #A47), which does not mention the problem: for fixed
$\eta<1/\log4$ and a density-one set of $m$, $(m+r)!/m!$ divides
$\binom{2m}{m}$ for every positive $r\le\eta\log m$, so $a_1=m+r$, $a_2=m$
and the remaining $a_i=1$ give $g_k(2m)\ge\lfloor\eta\log m\rfloor$, and the
lower limit of $\frac1{x\log x}\sum_{n\le x}g_k(n)$ is at least
$1/(2\log4)$. On 20 June 2026 Korsky announced a manuscript proving the
coefficient $3(k-1)/\log12$, without posting a proof; Li's preprint appeared
on 22 June, and its second version credits that announcement (the
[[../library/factorials_binomials/li_2026_prime_power_rarefaction_density_one_lower/_index|card]]).
The announcement gets no claim page: it gives no argument, and its bound,
like Li's, settles neither question. Nat Sothanaphan replied that the
appendix of the write-up
[[../library/factorials_binomials/sothanaphan_2026_resolution_erdos_problem_728_writeup_aristotle/_index|Sothanaphan 2026]]
has results parallel to Pomerance's; they are context here. A thread comment
of 24 July 2026 reports exact values of $g_2(n)$ for $n\le10^5$, finite data
that decide nothing about the limit.

**Search scope.** The site's problem page, its discussion thread (eleven
comments) and its proof-claims tab (no claims); the arXiv record of
2606.23661 (two versions, no journal reference) and an arXiv title and
abstract query for "Problem 400" (Li's preprint only); the library cards of
the three sources above. [ErGr80] p. 77 was not read; its remark is cited as
the site gives it. Not searched: MathSciNet, zbMATH, Google Scholar, X.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/factorials_binomials/li_2026_prime_power_rarefaction_density_one_lower/_index|li_2026_prime_power_rarefaction_density_one_lower]]
- [[../library/factorials_binomials/li_2026_prime_power_rarefaction_density_one_lower/corollary_1_3|li_2026_prime_power_rarefaction_density_one_lower / corollary_1_3]]
- [[../library/factorials_binomials/li_2026_prime_power_rarefaction_density_one_lower/theorem_1_1|li_2026_prime_power_rarefaction_density_one_lower / theorem_1_1]]
- [[../library/factorials_binomials/li_2026_prime_power_rarefaction_density_one_lower/theorem_1_2|li_2026_prime_power_rarefaction_density_one_lower / theorem_1_2]]
- [[../library/factorials_binomials/li_2026_prime_power_rarefaction_density_one_lower/theorem_1_4|li_2026_prime_power_rarefaction_density_one_lower / theorem_1_4]]
- [[../library/factorials_binomials/pomerance_2026_remarks_middle_binomial_coefficient/_index|pomerance_2026_remarks_middle_binomial_coefficient]]
- [[../library/factorials_binomials/sothanaphan_2026_resolution_erdos_problem_728_writeup_aristotle/_index|sothanaphan_2026_resolution_erdos_problem_728_writeup_aristotle]]

<!-- END problem library links -->

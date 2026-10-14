---
name: problems/arithmetic_functions/E0824
title: Problem 824
desc: |
  Asks whether the number $h(x)$ of coprime pairs $a<b<x$ with
  $\sigma(a)=\sigma(b)$ satisfies $h(x)>x^{2-o(1)}$. An AI-assisted write-up of
  August 2026 claims $h(x)>x^{\gamma}$ for every $\gamma<13/8$, and a draft of
  October 2026 claims the answer yes under a hypothesis on primes $p$ with
  $p+1$ free of large prime factors.
tags:
- Number theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-13T12:25:21Z
---

# Problem 824

[[problems/arithmetic_functions/_index|..]]

[[problems/arithmetic_functions/E0824/claims/_index|claims/]]: The 1 claim page of Problem 824, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $h(x)$ count the number of integers $1\leq a<b<x$ such that
$(a,b)=1$ and $\sigma(a)=\sigma(b)$, where $\sigma$ is the sum of divisors
function.

Is it true that $h(x)>x^{2-o(1)}$?

**Status.** Open. Bloom's catalog labeled the problem OPEN (page last edited 28
September 2025). Pollack and Pomerance [PoPo16] proved $h(x)>x^{1.4}$ for all
large $x$, which gives $h(x)/x\to\infty$. Erdős [Er74b, p. 202] had sketched
only $\limsup h(x)/x=\infty$. He wrote that the proof of $h(x)/x\to\infty$ "can
be produced with a little more trouble".

A partial result is claimed on erdosproblems.com's [proof-claims
tab](https://www.erdosproblems.com/forum/thread/824/proof-claims#proof-claim-232).
The claim is by Cam, using GPT 5.6 high, and was submitted 2026-08-28. The
[write-up](https://github.com/LeanMeanBean/Erdos-824/blob/fbf066d640a1/erdos_824_partial_proof_13_8.pdf)
claims $h(x)>x^{\gamma}$ for every fixed $\gamma<13/8$ and all large $x$, with
squarefree pairs. It follows the scheme of [PoPo16], with Pascadi's level $5/8$
of distribution for primes in place of Baker and Harman's count of smooth
shifted primes. A bound below exponent $2$ settles no instance of the question,
so the claim has no claim page. The proof-claims thread had no comments when
erdosproblems.com froze it on 6 October 2026.

A conditional answer yes is claimed by Shisheng Li and Zhong Zhuang in a draft
first posted on 7 October 2026 and registered, in its version of 11 October,
with the Palomar registry, on
[[problems/arithmetic_functions/E0824/claims/2026_10_07_li_zhuang|Li and Zhuang 2026]].
Its Hypothesis $\mathrm{A}^+$ asks, for every fixed $0<\delta<1/4$, for
$y^{1-o(1)}$ primes $p\le5y$ with $P^+(p+1)\le y^\delta$, where $P^+$ is the
largest prime factor. Its Theorem 1.3, proved in Lean for natural $x$, derives
$h(x)>x^{2-\varepsilon}$ for every $\varepsilon>0$ and all large $x$ from
$\mathrm{A}^+$ by the argument of [PoPo16, §6] with the smoothness exponent
sent to zero. Its Theorem 1.4 says that the method of OpenAI's manuscript
[[problems/arithmetic_functions/E0821/claims/2026_09_24_openai|claimed for Problem 821]],
which counts primes $p$ with $P^+(p-1)\le x^\delta$, proves $\mathrm{A}^+$
when rerun for primes $2u-1$ in place of $2u+1$. That manuscript has no outside
review, and its theorem as stated concerns $p-1$, not $p+1$, so the problem
stays open: $\mathrm{A}^+$ is unproved.

**Source.** [erdosproblems.com/824](https://www.erdosproblems.com/824), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #824,
https://www.erdosproblems.com/824.

**References.**

- [Er74b] Erdős, P., Remarks on some problems in number theory. Math. Balkanica
  (1974), 197-202.
- [PoPo16] Pollack, Paul and Pomerance, Carl, Some problems of Erdős on the
  sum-of-divisors function. Trans. Amer. Math. Soc. Ser. B (2016), 1-26.

**Formalization.** None recorded.

## Progress

Not yet compiled.

## Known Results

Not yet compiled.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/arithmetic_functions/openai_2026_weighted_dilation_graphs_smooth_shifted_primes_totient_fibers/_index|openai_2026_weighted_dilation_graphs_smooth_shifted_primes_totient_fibers]]
- [[../library/arithmetic_functions/pollack_2016_problems_erdos_sum_divisors_function/_index|pollack_2016_problems_erdos_sum_divisors_function]]
- [[../library/arithmetic_functions/pollack_2016_problems_erdos_sum_divisors_function/theorem_p24|pollack_2016_problems_erdos_sum_divisors_function / theorem_p24]]
- [[../library/number_theory/erdos_1974_remarks_problems_number_theory/_index|erdos_1974_remarks_problems_number_theory]]

<!-- END problem library links -->

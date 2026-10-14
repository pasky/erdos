---
name: problems/factorials_binomials/E0731
title: Problem 731
desc: |
  Asks for a reasonable $f(n)$ such that, for almost all $n$, the least $m$ with
  $m\nmid\binom{2n}{n}$ satisfies $m\sim f(n)$.
tags:
- Number theory
- Binomial coefficients
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-08T17:47:46Z
---

# Problem 731

[[problems/factorials_binomials/_index|..]]

[[problems/factorials_binomials/E0731/claims/_index|claims/]]: The 1 claim page of Problem 731, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Find some reasonable function $f(n)$ such that, for almost all
integers $n$, the least integer $m$ such that $m\nmid \binom{2n}{n}$ satisfies

$$
m\sim f(n).
$$

**Formulation.** erdosproblems.com does not define "reasonable", and without
some such restriction the request would be met trivially by taking $f(n)$ to be
the least non-divisor itself. The page reads the question as its source does.
[EGRS75] (p. 91) state without proof that, for every fixed $\epsilon>0$ and
outside a set of density $0$, the least non-divisor $A(n)$ of $\binom{2n}{n}$
satisfies $\exp((\log n)^{1/2-\epsilon})<A(n)<\exp((\log n)^{1/2+\epsilon})$.
They add that improving this would be easy but that an asymptotic formula looks
hard. The question asks for such a formula: an explicit $f$ with $A(n)/f(n)\to1$
outside a set of density $0$. Li's claim reads "reasonable" as dyadic
regularity, a class that contains the usual explicit formulas, and asserts that
no such $f$ exists. That reading is a variant, which this page sets aside: a no
to it leaves open an explicit $f$ outside the class.

**Status.** OPEN: the erdosproblems.com label, on a page last edited 19 October
2025, before the one claim. The derived standing is open as well. One claim, by
Eric Li, is recorded on the
[[problems/factorials_binomials/E0731/claims/2026_06_27_li|Li claim page]]. The
claim asserts that no dyadically regular $f$ has the least non-divisor
asymptotic to $f(n)$ for almost all $n$. This is a negative answer under Li's
reading of "reasonable" as dyadic regularity, a variant the Formulation sets
aside, so the claim page is rejected (Current assessment). Li posted the claim
as an arXiv preprint on 2026-06-27 and submitted it to the erdosproblems.com
proof-claims tab on 2026-07-17. It comes with a Lean development produced by
Aristotle (Harmonic).

**Source.** [erdosproblems.com/731](https://www.erdosproblems.com/731), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #731,
https://www.erdosproblems.com/731.

**References.**

- [EGRS75] Erdős, P. and Graham, R. L. and Ruzsa, I. Z. and Straus, E. G., On
  the prime factors of $(\sp{2n}\sb{n})$. Math. Comp. (1975), 83-92.

**Formalization.** None recorded.

## Current assessment

**The question.** The Statement asks for a reasonable $f$ with $A(n)\sim f(n)$
for almost all $n$, where $A(n)$ is the least $m$ with $m\nmid\binom{2n}n$.
The erdosproblems.com statement and commentary do not define "reasonable";
[EGRS75] (p. 91), the source, does not use the word and says only that an
asymptotic formula seems hard; and the erdosproblems.com discussion thread,
frozen on 6 October 2026, holds no reply of the curator on the word. The
commentary records [EGRS75]'s remark that $A(n)=\exp((\log n)^{1/2+o(1)})$ for
almost all $n$ is not hard to show.

**Readings and answers.** The answer depends on the reading of "reasonable". The
page reads the question as asking for an explicit asymptotic formula, as its
source does, and sets aside the first two readings below; under its reading the
problem is open.

- With no restriction, $f=A$ meets the request trivially, a yes that the
  Formulation sets aside as not what is asked.
- With "reasonable" read as dyadically regular, a positive $f$ whose $\log f$
  varies by an amount tending to $0$ over the dyadic block $X\le n<2X$ (Li's
  Definition 1.8), Li's
  [[../library/factorials_binomials/li_2026_resolution_erdos_problem_731_under_dyadic/theorem_1_10|Theorem 1.10]]
  states that no such $f$ has $A(n)/f(n)\to1$ in natural density, a no. This
  reading is a variant, so the
  [[problems/factorials_binomials/E0731/claims/2026_06_27_li|Li claim page]]
  is rejected: its mathematics answers the variant and does not settle this
  problem.
- With "reasonable" read as this page reads it, as an explicit formula not
  required to be dyadically regular, nothing is settled. Li's theorems rule out
  every dyadically regular $f$ and say nothing about functions outside that
  class; his Corollary 1.6 states only that any $f$ with $A(n)/f(n)\to1$ in
  density takes values at least a fixed factor apart on positive proportions of
  every large dyadic block.

**Progress.** [EGRS75] (p. 91) state without proof that
$\exp((\log n)^{1/2-\epsilon})<A(n)<\exp((\log n)^{1/2+\epsilon})$ outside a set
of density $0$
([[../library/factorials_binomials/erdos_1975_prime_factors/inequality_8|inequality (8)]]).
Li's
[[../library/factorials_binomials/li_2026_resolution_erdos_problem_731_under_dyadic/corollary_1_7|Corollary 1.7]],
unreviewed like the rest of the preprint, states that
$\log A(n)-\sqrt{(\log2)\log n}-\frac14\log\log n$ is bounded outside a set
of upper density tending to $0$ as the bound grows, so that
$\sqrt2(\log2)^{1/4}(\log n)^{1/4}\exp\sqrt{(\log2)\log n}$ is the
density-tight scale of $A(n)$.

**Search scope and coverage.** The erdosproblems.com problem page, discussion
thread and proof-claims tab, and the library cards of [EGRS75] and of Li's
preprint; no wider literature search was made. Li's preprint is unrefereed and
unreviewed, its Lean development is not built or audited here, and nothing on
this page is independently reviewed.

**Remaining gaps.** (1) The reading of "reasonable", which no source or ruling
fixes. (2) Review of Li's preprint and its Lean development, which would
settle the dyadically regular variant only. (3) An asymptotic formula, or its
impossibility, for any reading broader than dyadic regularity.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/factorials_binomials/erdos_1975_prime_factors/_index|erdos_1975_prime_factors]]
- [[../library/factorials_binomials/erdos_1975_prime_factors/inequality_8|erdos_1975_prime_factors / inequality_8]]
- [[../library/factorials_binomials/erdos_1975_prime_factors/theorem_4|erdos_1975_prime_factors / theorem_4]]
- [[../library/factorials_binomials/erdos_1975_prime_factors/theorem_5|erdos_1975_prime_factors / theorem_5]]
- [[../library/factorials_binomials/li_2026_resolution_erdos_problem_731_under_dyadic/_index|li_2026_resolution_erdos_problem_731_under_dyadic]]
- [[../library/factorials_binomials/li_2026_resolution_erdos_problem_731_under_dyadic/corollary_1_7|li_2026_resolution_erdos_problem_731_under_dyadic / corollary_1_7]]
- [[../library/factorials_binomials/li_2026_resolution_erdos_problem_731_under_dyadic/lemma_2_1|li_2026_resolution_erdos_problem_731_under_dyadic / lemma_2_1]]
- [[../library/factorials_binomials/li_2026_resolution_erdos_problem_731_under_dyadic/theorem_1_10|li_2026_resolution_erdos_problem_731_under_dyadic / theorem_1_10]]
- [[../library/factorials_binomials/li_2026_resolution_erdos_problem_731_under_dyadic/theorem_1_3|li_2026_resolution_erdos_problem_731_under_dyadic / theorem_1_3]]
- [[../library/factorials_binomials/li_2026_resolution_erdos_problem_731_under_dyadic/theorem_1_4|li_2026_resolution_erdos_problem_731_under_dyadic / theorem_1_4]]
- [[../library/factorials_binomials/li_2026_resolution_erdos_problem_731_under_dyadic/theorem_5_2|li_2026_resolution_erdos_problem_731_under_dyadic / theorem_5_2]]

<!-- END problem library links -->

---
name: problems/additive_bases/E1192
title: Problem 1192
desc: |
  Asks whether, for every $r\ge2$, some basis $A$ of order $r$ has
  $\sum_{n\le x}f_r(n)^2\ll x$, where $f_r(n)$ counts the representations of $n$
  as a sum of $r$ elements of $A$.
tags:
- Additive combinatorics
- Additive bases
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 1192

[[problems/additive_bases/_index|..]]

[[problems/additive_bases/E1192/claims/_index|claims/]]: The 1 claim page of Problem 1192, one per claimant's result; the problem's standing derives from them.

***

**Statement.** For $A\subset \mathbb{N}$ let $f_r(n)$ count the number of
solutions to $n=a_1+\cdots+a_r$ with $a_i\in A$.

Does there exist, for all $r\geq 2$, a basis $A$ of order $r$ (so that
$f_r(n)>0$ for all large $n$) such that

$$
\sum_{n\leq x}f_r(n)^2 \ll x
$$

for all $x$?

**Status.** Open. Ruzsa [Ru90] answers the case $r=2$. This is the accepted
partial claim [[problems/additive_bases/E1192/claims/1990_06_01_ruzsa|Ruzsa]].
The cases $r\ge3$ are open.

**Source.** [erdosproblems.com/1192](https://www.erdosproblems.com/1192),
accessed 2026-09-04. Cite as: T. F. Bloom, Erdős Problem #1192,
https://www.erdosproblems.com/1192.

**References.**

- [Ru90] Ruzsa, Imre Z., A just basis. Monatsh. Math. (1990), 145-151.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/1192.lean).

## Current assessment

The held
[[../library/additive_bases/ruzsa_1990_just_basis/theorem_2|Ruzsa second-moment theorem]]
supplies the order-two case at its recorded source standing. Its statement was
inspected; its complete source proof is not independently audited here.
The higher-order question needs a different density scale, as the following
author-recorded argument by Plasma AI shows.

Let $A(y)=|A\cap[0,y]|$ and count ordered $r$-tuples. If
$\sum_{n\le x}f_r(n)^2\le Cx$ for large $x$, Cauchy–Schwarz gives
$\sum_{n\le x}f_r(n)=O(x)$. Every tuple from $A\cap[0,y]$ has sum at
most $ry$, so $A(y)^r=O(y)$. Conversely, eventual $r$-fold coverage gives
$A(y)^r\ge y-O(1)$. Thus the desired basis must satisfy
$A(y)\asymp y^{1/r}$.

An asymptotic order-two basis has $A(y)\gg\sqrt y$. Reusing the same set
for any fixed $r\ge3$ therefore gives, with $y=\lfloor x/r\rfloor$,

$$
\sum_{n\le x}f_r(n)^2
\ge\frac{\bigl(\sum_{n\le x}f_r(n)\bigr)^2}{\lfloor x\rfloor+1}
\ge\frac{A(\lfloor x/r\rfloor)^{2r}}{\lfloor x\rfloor+1}
\gg x^{r-1}.
$$

This rules out direct higher convolution of Ruzsa's same basis. It does not
rule out a new basis at scale $y^{1/r}$. The required construction would need
$r$-fold coverage and an energy bound at that scale, with control of mixed
sums across its blocks. Two-summand cyclic representation bounds do not supply
that interface. This is a scoped obstruction, not a new status search or a
negative answer for $r\ge3$.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/additive_bases/ding_2026_improved_upper_bound_ruzsa_number/_index|ding_2026_improved_upper_bound_ruzsa_number]]
- [[../library/additive_bases/ding_2026_improved_upper_bound_ruzsa_number/lemma_2_2|ding_2026_improved_upper_bound_ruzsa_number / lemma_2_2]]
- [[../library/additive_bases/ding_2026_improved_upper_bound_ruzsa_number/theorem_1_1|ding_2026_improved_upper_bound_ruzsa_number / theorem_1_1]]
- [[../library/additive_bases/ding_2026_improved_upper_bound_ruzsa_number/theorem_1_3|ding_2026_improved_upper_bound_ruzsa_number / theorem_1_3]]
- [[../library/additive_bases/erdos_1960_additive_properties_random_sequences_positive_integers/_index|erdos_1960_additive_properties_random_sequences_positive_integers]]
- [[../library/additive_bases/erdos_1990_representations_integers_as_sum_k_terms/_index|erdos_1990_representations_integers_as_sum_k_terms]]
- [[../library/additive_bases/erdos_1990_representations_integers_as_sum_k_terms/theorem_1|erdos_1990_representations_integers_as_sum_k_terms / theorem_1]]
- [[../library/additive_bases/erdos_1990_representations_integers_as_sum_k_terms/theorem_2|erdos_1990_representations_integers_as_sum_k_terms / theorem_2]]
- [[../library/additive_bases/erdos_1990_representations_integers_as_sum_k_terms/theorem_3|erdos_1990_representations_integers_as_sum_k_terms / theorem_3]]
- [[../library/additive_bases/green_2026_100_open_problems/_index|green_2026_100_open_problems]]
- [[../library/additive_bases/konyagin_2009_erdos_turan_problem_infinite_groups/_index|konyagin_2009_erdos_turan_problem_infinite_groups]]
- [[../library/additive_bases/konyagin_2009_erdos_turan_problem_infinite_groups/corollary_1|konyagin_2009_erdos_turan_problem_infinite_groups / corollary_1]]
- [[../library/additive_bases/konyagin_2009_erdos_turan_problem_infinite_groups/theorem_1|konyagin_2009_erdos_turan_problem_infinite_groups / theorem_1]]
- [[../library/additive_bases/konyagin_2009_erdos_turan_problem_infinite_groups/theorem_2|konyagin_2009_erdos_turan_problem_infinite_groups / theorem_2]]
- [[../library/additive_bases/nathanson_2014_paul_erdos_additive_bases/_index|nathanson_2014_paul_erdos_additive_bases]]
- [[../library/additive_bases/ruzsa_1990_just_basis/_index|ruzsa_1990_just_basis]]
- [[../library/additive_bases/ruzsa_1990_just_basis/theorem_1|ruzsa_1990_just_basis / theorem_1]]
- [[../library/additive_bases/ruzsa_1990_just_basis/theorem_2|ruzsa_1990_just_basis / theorem_2]]

<!-- END problem library links -->

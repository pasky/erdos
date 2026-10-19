---
name: problems/diophantine_problems/E1081
title: Problem 1081
desc: |
  Asks whether the number of $n\leq x$ that are sums of two squarefull numbers
  is asymptotic to $cx/\sqrt{\log x}$ for some $c>0$.
tags:
- Number theory
- Powerful numbers
status: solved
claim: disproved
created: 2026-09-04T09:17:27Z
updated: 2026-10-18T22:19:33Z
---

# Problem 1081

[[problems/diophantine_problems/_index|..]]

[[problems/diophantine_problems/E1081/claims/_index|claims/]]: The 3 claim pages of Problem 1081, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $A(x)$ count the number of $n\leq x$ which are the sum of two
squarefull numbers (a number $m$ is squarefull if $p\mid m$ implies $p^2\mid
m$). Is it true that

$$
A(x) \sim c \frac{x}{\sqrt{\log x}}
$$

for some $c>0$?

**Status.** Disproved. Odoni proves that $A(x)\sqrt{\log x}/x\to\infty$, so
$A(x)$ is not asymptotic to $c\,x/\sqrt{\log x}$ for any $c>0$ (Acta Arith.
1981, refereed), and erdosproblems.com credits his paper for the disproof. Two
later refereed lower bounds each refute the asymptotic independently: Blomer's
$A(x)\gg x(\log x)^{-0.253}$ (J. Reine Angew. Math. 2004), and Blomer and
Granville's, which with their upper bound fixes the order of $A(x)$ as
$x/(\log x)^{1-2^{-1/3}}$ up to powers of $\log\log x$ (Duke Math. J. 2006). The
accepted full claims are
[[problems/diophantine_problems/E1081/claims/1981_01_01_odoni|Odoni 1981]],
[[problems/diophantine_problems/E1081/claims/2004_01_30_blomer|Blomer 2004]]
and
[[problems/diophantine_problems/E1081/claims/2006_11_01_blomer_granville|Blomer and Granville 2006]].

**Source.** [erdosproblems.com/1081](https://www.erdosproblems.com/1081),
accessed 2026-09-04. Cite as: T. F. Bloom, Erdős Problem #1081,
https://www.erdosproblems.com/1081.

**References.**

- [BaBr94] Baker, R. C. and Brüdern, J., On sums of two squarefull numbers.
  Math. Proc. Cambridge Philos. Soc. 116 (1994), no. 1, 1-5.
- [Bl04] Blomer, Valentin, Binary quadratic forms with large discriminants and
  sums of two squareful numbers. J. Reine Angew. Math. 569 (2004), 213-234.
- [BlGr06] Blomer, Valentin and Granville, Andrew,
  [[../library/diophantine_problems/blomer_2006_estimates_representation_numbers_quadratic_forms/_index|Estimates for representation numbers of quadratic forms]].
  Duke Math. J. 135 (2006), no. 2, 261-302.
- [Er76e] Erdős, P., Problems and results on consecutive integers. Publ. Math.
  Debrecen (1976), 271-282.
- [Od81] Odoni, R. W. K., A problem of Erdős on sums of two squarefull numbers.
  Acta Arith. 39 (1981), no. 2, 145-162.

**Formalization.** None recorded.

## Progress

Not yet compiled.

## Known Results

Not yet compiled.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/diophantine_problems/blomer_2006_estimates_representation_numbers_quadratic_forms/_index|blomer_2006_estimates_representation_numbers_quadratic_forms]]
- [[../library/diophantine_problems/blomer_2006_estimates_representation_numbers_quadratic_forms/corollary_2|blomer_2006_estimates_representation_numbers_quadratic_forms / corollary_2]]
- [[../library/diophantine_problems/blomer_2006_estimates_representation_numbers_quadratic_forms/theorem_5|blomer_2006_estimates_representation_numbers_quadratic_forms / theorem_5]]
- [[../library/diophantine_problems/blomer_2006_estimates_representation_numbers_quadratic_forms/theorem_6|blomer_2006_estimates_representation_numbers_quadratic_forms / theorem_6]]
- [[../library/diophantine_problems/odoni_1981_problem_erdos_sums_two_squarefull_numbers/_index|odoni_1981_problem_erdos_sums_two_squarefull_numbers]]

<!-- END problem library links -->

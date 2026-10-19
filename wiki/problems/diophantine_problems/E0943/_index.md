---
name: problems/diophantine_problems/E0943
title: Problem 943
desc: |
  Asks whether the number of ways to write $n$ as a sum of two powerful numbers
  is $n^{o(1)}$.
tags:
- Number theory
- Powerful numbers
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-18T22:19:33Z
---

# Problem 943

[[problems/diophantine_problems/_index|..]]

[[problems/diophantine_problems/E0943/claims/_index|claims/]]: The 2 claim pages of Problem 943, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $A$ be the set of powerful numbers (if $p\mid n$ then
$p^2\mid n$). Is it true that

$$
1_A\ast 1_A(n)=n^{o(1)}
$$

for every $n$?

**Status.** Open.

**Source.** [erdosproblems.com/943](https://www.erdosproblems.com/943), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #943,
https://www.erdosproblems.com/943.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/943.lean).

## Current assessment

Przemyslaw Chojecki's unrefereed write-up of 18 March 2026, posted on the
erdosproblems.com forum thread, claims
$1_A*1_A(n)\ll_\varepsilon n^{2/5+\varepsilon}$ (its Theorem 1.2), a pending
claim on
[[problems/diophantine_problems/E0943/claims/2026_03_18_chojecki|its claim page]].
The later author-recorded bound of Plasma AI in
[[theory/number_theory/L24_powerful_sum_bound/_index|L24]], a pending partial
claim on
[[problems/diophantine_problems/E0943/claims/2026_10_19_plasma_ai|its claim page]],
is the same, $1_A*1_A(N)\le N^{2/5+o(1)}$ for positive powerful summands,
including 1.
It uses a field-uniform quadratic-norm count for each pair of squarefree
cube factors and three complementary dyadic bounds. The
[[research/powerful_numbers_and_products/_index|research account]]
locates the remaining loss when the cube factors vary. Neither bound
reaches $N^{o(1)}$. L24's proof is tier 0, without independent review, and
no review of Chojecki's proof is on record. This is a
scoped mathematical assessment, not a wider standing search.

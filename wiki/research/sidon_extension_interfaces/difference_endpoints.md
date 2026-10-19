---
name: research/sidon_extension_interfaces/difference_endpoints
title: "Unique differences and endpoint growth"
desc: "Processing the least missing difference bounds its eventual endpoints; a counting-function estimate alone does not control that processing order."
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

***

The deductions and obstructions here are author-recorded by Plasma AI.
Source-dependent conclusions retain the named premises and reading limits. No
independent review, novelty claim or complete solution of the linked problems
follows from this account.

The relevant questions are [[problems/additive_bases/E1194/_index|E1194]].

## E1194: the missing-difference order yields a bound on endpoints

The subscript n labels the difference n, not the nth element. In Lev's
single-set greedy construction, start with one positive integer (equivalently,
process the initial missing difference zero). At each subsequent stage take the
least positive unrepresented difference d and adjoin z,z+d, preserving
uniqueness of positive differences.

With k existing marks, d<=binom(k,2)+1. The forbidden choices of z are O(k^3): a
collision between one new mark and three old marks determines z, and the
remaining collisions with two occurrences of new marks also determine z, unless
they reduce to an old representation of d or a trivial identity. The former is
excluded by the choice of d. Coincidences with an old element exclude only O(k)
more choices. Thus a positive z=O(k^3) exists, and z+d=O(k^3). After j stages
k<=2j+1, giving endpoints O(j^3).

The sequence of processed missing positive differences is strictly increasing.
After at most n such stages, each difference <=n has appeared, perhaps earlier
as a byproduct. Its two endpoints were introduced by then, so the uniquely
representing endpoint a_n is O(n^3). This completes the endpoint specialization
of the inspected source construction. A density statement A(x)>>x^(1/3) alone
would not imply it without the processing order.

Cilleruelo–Nathanson's Theorem 1 preserves a lower counting function from a
Sidon input, up to its stated losses. It does not control the processing time of
each difference. If R_A(X)=max_{1<=n<=X}a_n<=Y, then binom(A(Y),2)>=X is
necessary. Its converse is false: many distinct differences can omit a
prescribed initial interval. Next test: bound the covered initial interval [1,X]
directly rather than substitute a counting-function estimate. The stronger lower
claims on the problem page retain their stated unexamined status here.

## Source interfaces

These source locators identify the uses in this account. Statement and account
reading do not certify a source proof; proof reading here is author inspection
and confers no independent standing.

- [[../library/additive_bases/cilleruelo_2008_perfect_difference_sets_constructed_sidon_sets/_index|cilleruelo
  2008 perfect difference sets constructed sidon sets]]: Introduction,
  definitions and Theorems 1-3 (statement reading).
- [[../library/additive_bases/lev_2004_reconstructing_integer_sets_representation_functions/_index|lev
  2004 reconstructing integer sets representation functions]]: Theorem 3 proof;
  Section 3, construction preceding Problem 1 (proof reading).

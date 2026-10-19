---
name: research/diophantine_representation_interfaces/rational_coefficients
title: "A rational coefficient would remove a floor"
desc: "Restricting a floored fifth-power sequence to a denominator progression would give an integer Sidon polynomial, conditional on a rational good coefficient."
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

***

The deductions and obstructions here are author-recorded by Plasma AI.
Source-dependent conclusions retain the named premises and reading limits. No
independent review, novelty claim or complete solution of the linked problems
follows from this account.

The relevant questions are [[problems/diophantine_problems/E0324/_index|E0324]].

## E0324: rationality would remove the floor

The target is one polynomial in Z[X] with globally distinct pair sums for
0<=a<b; diagonal pairs are excluded. Dubickas--Novikas's four-distinct-index
collisions cover this weaker convention and exclude every degree<=3 tail. An
eventual positive construction suffices after an integer input shift.

Precisely, if a rational c=A/B with B>0 made Ruzsa's sequence n^5+floor(cn^4),
n>=n_0, Sidon, choose an integer T with BT>=n_0. Restrict to n=B(t+T); the floor
disappears and

$$
F(t)=B^5(t+T)^5+AB^3(t+T)^4\in\mathbb Z[t]
$$

would solve E0324 for all t>=0. One rational good coefficient is therefore
decisive. The held account supplies only a real one. Uncountability or positive
measure would not force a rational member, and rational approximation on a
finite input range does not preserve all infinitely many pair-sum inequalities.
The Ruzsa construction itself remains uninspected: this is a source gap, not a
proof that no rational coefficient works. Stop unless the source supplies one or
a uniform transfer to one.

## Source interfaces

These source locators identify the uses in this account. Statement and account
reading do not certify a source proof; proof reading here is author inspection
and confers no independent standing.

- [[../library/diophantine_problems/dubickas_2021_no_cubic_integer_polynomial_generates_sidon/_index|dubickas
  2021 no cubic integer polynomial generates sidon]]: Linear/quadratic collision
  families (account reading). Theorem 1.1 and four-distinct-index qualification,
  pp.1859-1865 (account reading).

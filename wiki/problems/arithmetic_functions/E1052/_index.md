---
name: problems/arithmetic_functions/E1052
title: Problem 1052
desc: |
  Asks whether there are only finitely many unitary perfect numbers, the
  integers $n$ equal to the sum of their proper divisors $d$ with $(d,n/d)=1$.
tags:
- Number theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 1052

[[problems/arithmetic_functions/_index|..]]

***

**Statement.** A unitary divisor of $n$ is $d\mid n$ such that $(d,n/d)=1$. A
number $n\geq 1$ is a unitary perfect number if it is the sum of its unitary
divisors (aside from $n$ itself).

Are there only finitely many unitary perfect numbers?

**Status.** Open.

**Source.** [erdosproblems.com/1052](https://www.erdosproblems.com/1052),
accessed 2026-09-04. Cite as: T. F. Bloom, Erdős Problem #1052,
https://www.erdosproblems.com/1052.

**References.**

- [Gu04] Guy, Richard K., Unsolved problems in number theory. Third edition,
  Problem Books in Mathematics, Springer, New York (2004), xviii+437 pp.;
  doi:10.1007/978-0-387-26677-0. Section B3 "Unitary perfect numbers", p. 84,
  records Subbarao's conjecture of finitely many even unitary perfect numbers,
  the prize offers of Subbarao, Carlitz and Erdős, and the four small examples.
  Library home:
  [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]].

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/1052.lean).

## Current assessment

Every unitary perfect positive integer is even. For odd $n>1$, the equation
$\sigma^*(n)=\prod_{p^e\parallel n}(p^e+1)=2n$ forces at most one prime-power
factor by its $2$-adic valuation. But one factor would give $p^e+1=2p^e$,
impossible for $p^e>1$; $n=1$ also fails. For

$$
n=2^a\prod_i p_i^{e_i},\qquad p_i\text{ odd},
$$

comparison of $2$-adic valuations yields $\sum_i v_2(p_i^{e_i}+1)=a+1$. The
number of odd prime factors is therefore at most $a+1$, which is not a uniform
bound because $a$ is unbounded.

The finite box in
[[../library/arithmetic_functions/maciejewski_2026_bounded_box_reductions_subbarao_warren_problem/_index|Maciejewski's
source]] does not cover all parameters. Its already-recorded Proposition 1 gap
is substantive: an odd prime dividing $p-1$ need not divide $p^e+1$ for odd
$e$, as $p=7,e=1,q=3$ shows. This defeats that proof step, not the finiteness
assertion. The parity argument above is author-recorded; the source's suspect
site and finite scope were inspected, without replaying its computation. A
global parameter bound remains necessary.

## Known Results

Not yet compiled.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/arithmetic_functions/maciejewski_2026_bounded_box_reductions_subbarao_warren_problem/_index|maciejewski_2026_bounded_box_reductions_subbarao_warren_problem]]
- [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]]

<!-- END problem library links -->

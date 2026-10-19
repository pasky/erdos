---
name: problems/primes/E0461
title: Problem 461
desc: |
  Asks whether, uniformly for all $t$ and $n$, the $t$-smooth parts of the $t$
  integers in $[n+1,n+t]$ take $\gg t$ distinct values, where the $t$-smooth
  part of $m$ is the product of its prime factors below $t$, counted with
  multiplicity.
tags:
- Number theory
- Primes
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 461

[[problems/primes/_index|..]]

***

**Statement.** Let $s_t(n)$ be the $t$-smooth component of $n$ - that is, the
product of all primes $p$ (with multiplicity) dividing $n$ such that $p<t$. Let
$f(n,t)$ count the number of distinct possible values for $s_t(m)$ for $m\in
[n+1,n+t]$. Is it true that

$$
f(n,t)\gg t
$$

(uniformly, for all $t$ and $n$)?

**Status.** Open.

**Source.** [erdosproblems.com/461](https://www.erdosproblems.com/461), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #461,
https://www.erdosproblems.com/461.

**Formalization.** None recorded.

## Current assessment

There is an exact finite-period reduction for every fixed integer $t\ge2$. For
each prime $p<t$, choose the least positive $e_p$ with $p^{e_p}\ge t$, and put
$M_t=\prod_{p<t}p^{e_p}$. In any block of $t$ positive integers the number of
distinct smooth parts equals the number of distinct values of
$g_t(m)=\gcd(m,M_t)$.

If $g_t(m)<t$, no prime valuation is truncated, since a saturated prime-power
factor would already be at least $t$; hence $g_t(m)=s_t(m)$. A gcd value at
least $t$ cannot occur twice in the block, since it would divide a positive
difference below $t$. The same is true of a smooth part at least $t$, and
truncation cannot merge it with a smaller value. This proves the equality of
counts and periodicity of $f(n,t)$ modulo $M_t$.

Thus its minimum over all shifts is a finite gcd-profile calculation. The cases
$t=2$ and $3$ have minima one and two, using $M_2=1$ and the cycle $1,2,1,4$
modulo $M_3=4$. No larger sweep was run. The
[[../library/number_theory/erdos_1980_old_new_problems_results_combinatorial_number_theory/_index|held
$t/\log t$ lower bound]] was inspected at statement depth. This complete author
reduction does not control the minima uniformly for unbounded $t$.

## Known Results

Not yet compiled.

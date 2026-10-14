---
name: problems/primes/E0459
title: Problem 459
desc: |
  Asks to estimate $f(u)$, the largest $v$ such that no integer strictly between
  $u$ and $v$ is composed only of primes dividing $uv$.
tags:
- Number theory
- Primes
status: solved
claim: answered
created: 2026-09-04T09:17:27Z
updated: 2026-10-08T02:16:54Z
---

# Problem 459

[[problems/primes/_index|..]]

[[problems/primes/E0459/claims/_index|claims/]]: The 1 claim page of Problem 459, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $f(u)$ be the largest $v$ such that no $m\in (u,v)$ is
composed entirely of primes dividing $uv$. Estimate $f(u)$.

**Status.** SOLVED (LEAN), the erdosproblems.com label. The curator credits
Stijn Cambie's observations as settling the natural readings of an estimate
question whose intended precision erdosproblems.com calls unclear. The
observations are that $f$ attains each of its trivial bounds $u+2$ and $u^2$
infinitely often, while $f(n)=(1+o(1))n$ for almost all $n$. The curator also
records Lean proofs of these statements outside this corpus. All of this is on
the [[problems/primes/E0459/claims/2025_09_13_cambie|claim page]]. The Lean
proofs are not built here.

**Source.** [erdosproblems.com/459](https://www.erdosproblems.com/459), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #459,
https://www.erdosproblems.com/459.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/6fbb54f24ccc2e64dcfaffc28c58950e377110d2/FormalConjectures/ErdosProblems/459.lean),
pinned at its commit of 18 September 2026, whose `formal_proof` attribute
points to the Lean file in van Doorn's repository linked from the claim page,
beside Alexeev's earlier file it extends; neither is built or audited here.

## Progress

Not yet compiled.

## Known Results

Not yet compiled.

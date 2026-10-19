---
name: problems/integer_sequences/E0695
title: Problem 695
desc: |
  Asks whether primes $p_1<p_2<\cdots$ with $p_{i+1}\equiv1\pmod{p_i}$ must have
  $p_k^{1/k}\to\infty$, and whether such a sequence exists with
  $p_k\le\exp(k(\log k)^{1+o(1)})$.
tags:
- Number theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 695

[[problems/integer_sequences/_index|..]]

***

**Statement.** Let $p_1<p_2<\cdots$ be a sequence of primes such that
$p_{i+1}\equiv 1\pmod{p_i}$. Is it true that

$$
\lim_k p_k^{1/k}=\infty?
$$

Does there exist such a sequence with

$$
p_k \leq \exp(k(\log k)^{1+o(1)})?
$$

**Status.** Open.

**Source.** [erdosproblems.com/695](https://www.erdosproblems.com/695), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #695,
https://www.erdosproblems.com/695.

**References.**

- [FKL10] Ford, Kevin and Konyagin, Sergei V. and Luca, Florian, Prime chains
  and Pratt trees. Geom. Funct. Anal. (2010), 1231-1258.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/695.lean).

## Current assessment

These deductions leave the full question unresolved. They have author-recorded
standing; this assessment is limited to the arguments and source interfaces
stated below. No comprehensive search for recent proof claims is recorded here.

Write
$p_{i+1}=m_i p_i+1$. Except possibly at the first prime 2,
$m_i$ is even and at least 2, so $p_i$ grows geometrically and
$$
 \log p_k=\sum_{i<k}\log m_i+O(1).
$$
The correction is bounded because
$\sum_i\log(1+1/(m_i p_i))<\infty$.
Thus the first question is exactly whether the averages of
$\log m_i$ tend to infinity, not just whether the multipliers
are unbounded.

An eventually periodic multiplier word is impossible. If $M$ is its period
product, sampling a fixed phase gives $Q_{t+1}=M Q_t+B$ with fixed positive
integer $B$. Start at a sufficiently late prime $q$ so $q\nmid M$. Modulo $q$,
this affine map is a permutation. The orbit from $Q_0\equiv0$ returns to 0
within at most $q$ steps. The corresponding integer term is larger than $q$ and
divisible by $q$, a contradiction. Aperiodic bounded-alphabet words remain
outside the argument.

Ford–Konyagin–Luca's §1.3 remark and Theorem 4 held account were read. A
hypothetical least-prime bound $p_{i+1}\le p_i(\log p_i)^C$ would give $\log
p_k=O(k\log k)$, sufficient for the existence question. Indeed $x_i=\log p_i$
satisfies $x_{i+1}\le x_i+C\log x_i+O(1)$; induction gives $x_i\le D i\log(i+2)$
for sufficiently large $D$. A fixed-power least-prime estimate gives only $\log
p_k=O(C_1^k)$, much weaker. Theorem 4's almost-all-prime height bound cannot be
imposed on a particular chain, which may lie in the exceptional set.

The missing step is uniform control of every prime chain for part
one, or a sufficiently short least-prime-in-progression bound for part two. A
proposed finite-alphabet obstruction must rule out all
aperiodic paths, not just cycles; a proposed upper construction must supply the
least-prime bound it consumes. Stop at almost-all prime statements, periodic
multiplier exclusions, or Linnik's double-exponential-scale iteration.

Source interfaces:
[[../library/integer_sequences/ford_2010_prime_chains_pratt_trees/remark_p4|Section
1.3 least-prime chain and its conditional growth consequence]];
[[../library/integer_sequences/ford_2010_prime_chains_pratt_trees/theorem_4|Theorem
4 and exceptional-set limitation]].

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/integer_sequences/ford_2010_prime_chains_pratt_trees/_index|ford_2010_prime_chains_pratt_trees]]
- [[../library/integer_sequences/ford_2010_prime_chains_pratt_trees/remark_p4|ford_2010_prime_chains_pratt_trees / remark_p4]]
- [[../library/integer_sequences/ford_2010_prime_chains_pratt_trees/theorem_1|ford_2010_prime_chains_pratt_trees / theorem_1]]
- [[../library/integer_sequences/ford_2010_prime_chains_pratt_trees/theorem_3|ford_2010_prime_chains_pratt_trees / theorem_3]]
- [[../library/integer_sequences/ford_2010_prime_chains_pratt_trees/theorem_4|ford_2010_prime_chains_pratt_trees / theorem_4]]

<!-- END problem library links -->

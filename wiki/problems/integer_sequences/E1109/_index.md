---
name: problems/integer_sequences/E1109
title: Problem 1109
desc: |
  Asks for an estimate of the size $f(N)$ of the largest subset of
  $\{1,\ldots,N\}$ whose pairwise sums are all squarefree, and whether
  $f(N)\le N^{o(1)}$.
tags:
- Number theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 1109

[[problems/integer_sequences/_index|..]]

[[problems/integer_sequences/E1109/claims/_index|claims/]]: The 2 claim pages of Problem 1109, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $f(N)$ be the size of the largest subset $A\subseteq
\{1,\ldots,N\}$ such that every $n\in A+A$ is squarefree. Estimate $f(N)$. In
particular, is it true that $f(N)\leq N^{o(1)}$, or even $f(N) \leq (\log
N)^{O(1)}$?

**Status.** Open. Bloom's catalog labeled the problem OPEN (page last edited 3
December 2025). Its commentary credits three sets of bounds: Erdős and Sárközy's
$\log N\ll f(N)\ll N^{3/4}\log N$,
[[problems/integer_sequences/E1109/claims/1987_03_01_erdos_sarkozy|Erdős and Sárközy 1987]];
Gyarmati's second proof of $f(N)\gg\log N$, by graph theory [Gy01], which does
not improve that bound and so has no claim page; and Konyagin's
$\log^2N\log\log N\ll f(N)\ll N^{11/15+o(1)}$, the best known,
[[problems/integer_sequences/E1109/claims/2004_06_30_konyagin|Konyagin 2004]].
None answers either question. G. N. Sárközy [Sa92c] extends the problem to sums
$A+B$ and to $k$-power-free sums. As Konyagin records (p. 494), Sárközy also
improves the upper bound to $f(N)\ll N^{3/4}$. That bound is superseded by
Konyagin's, and erdosproblems.com does not credit it, so it has no claim page.

**Source.** [erdosproblems.com/1109](https://www.erdosproblems.com/1109),
accessed 2026-09-04. Cite as: T. F. Bloom, Erdős Problem #1109,
https://www.erdosproblems.com/1109.

**References.**

- [ErSa87] Erdős, P. and Sárközy, A., On divisibility properties of integers of
  the form $a+a'$. Acta Math. Hungar. (1987), 117-122.
- [Gy01] Gyarmati, Katalin, On divisibility properties of integers of the form
  $ab+1$. Period. Math. Hungar. (2001), 71-79.
- [Ko04] [[../library/integer_sequences/konyagin_2004_problems_set_square_free_numbers/_index|Konyagin, S. V., Problems of the set of square-free numbers]].
  Izv. Ross. Akad. Nauk Ser. Mat. (2004), 63-90.
- [Sa92c] Sárközy, G. N., On a problem of P. Erdős. Acta Math. Hungar. (1992),
  271-282.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/1109.lean).

## Current assessment

These deductions leave the full question unresolved. They have author-recorded
standing; this assessment is limited to the arguments and source interfaces
stated below. No comprehensive search for recent proof claims is recorded here.

For fixed $N$, use vertices $a\in[1,N]$ with $2a$ squarefree, and an edge
between distinct $a,b$ exactly when $a+b$ is squarefree. Then $f(N)$ is exactly
the maximum clique size. All sums are at most $2N$, so only primes $p^2\le2N$
need be tested. The vertex condition handles doubles; omitting it changes the
problem. No clique computation was run.

This is finite for each specified $N$, not a fixed finite state space for the
extremal function. E1103's countermodel rules out a fixed prime list as
$N\to\infty$.

The elementary CRT bound explains its own quantitative limit. For $k$ tested odd
primes, its density factor is comparable to $2^{-k}$, since $\prod(1-1/p^2)$ is
bounded away from zero. Making the main term at most $N^\epsilon$,
$0<\epsilon<1$, requires $k$ of order $\log N$. But $M_F\ge4(k!)^2$, whose
logarithm is then of order at least $\log N\log\log N$; the error overwhelms the
target. This obstructs that naive complete-period count, not every sieve.

Konyagin's introduction, Proposition 1, Theorems 1–3 and discussion of the
quadratic large sieve were read as statements. Their proofs were not audited.
Existing bounds do not settle the subpolynomial or stronger polylogarithmic
question.

The missing step is uniform structural information beyond finite
clique data and the independent half-residue exclusions. A useful test is to use
a clique computation only for a concrete conjectured finite structural lemma;
its vertex and edge tests must include doubles and every prime square <=2N. Stop
at any finite N table or at ignoring the growing CRT-period error in an
asymptotic bound.

Source interfaces:
[[../library/integer_sequences/konyagin_2004_problems_set_square_free_numbers/_index|Section
1 definitions, Proposition 1, Theorems 1-3 and discussion of the quadratic large
sieve]].

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/integer_sequences/doorn_2025_growth_rates_sequences_governed_squarefree_properties/_index|doorn_2025_growth_rates_sequences_governed_squarefree_properties]]
- [[../library/integer_sequences/doorn_2025_growth_rates_sequences_governed_squarefree_properties/squarefree_sums_bound_p4|doorn_2025_growth_rates_sequences_governed_squarefree_properties / squarefree_sums_bound_p4]]
- [[../library/integer_sequences/erdos_1987_divisibility_properties_integers_form/_index|erdos_1987_divisibility_properties_integers_form]]
- [[../library/integer_sequences/erdos_1987_divisibility_properties_integers_form/conjecture_p117|erdos_1987_divisibility_properties_integers_form / conjecture_p117]]
- [[../library/integer_sequences/erdos_1987_divisibility_properties_integers_form/remark_p117|erdos_1987_divisibility_properties_integers_form / remark_p117]]
- [[../library/integer_sequences/erdos_1987_divisibility_properties_integers_form/theorem_1|erdos_1987_divisibility_properties_integers_form / theorem_1]]
- [[../library/integer_sequences/erdos_1987_divisibility_properties_integers_form/theorem_2|erdos_1987_divisibility_properties_integers_form / theorem_2]]
- [[../library/integer_sequences/konyagin_2004_problems_set_square_free_numbers/_index|konyagin_2004_problems_set_square_free_numbers]]

<!-- END problem library links -->

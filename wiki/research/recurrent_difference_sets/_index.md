---
name: research/recurrent_difference_sets
title: Recurrent difference sets
desc: |
  Positive upper Banach density gives syndetic recurrent differences; divergent reciprocal sums and periodic examples delimit the conclusion.
tags: []
sources: []
problems: [332]
created: 2026-10-14T20:10:13Z
updated: 2026-10-14T20:10:13Z
---

# Recurrent difference sets

[[research/_index|..]]

***

This note concerns [[problems/integer_sequences/E0332/_index|Problem 332]] and
preserves the exact scope of its remaining question.

These author-recorded arguments and source-fit limitations are by Plasma AI.
They do not confer independent verification or resolve the remaining
erdosproblems.com question.

Let
$$
 D^+(A)=\{d\ge1:\#\{(a,b)\in A^2:a-b=d\}=\infty\}.
$$
These are recurrent differences, not all differences.

Suppose the upper Banach density of $A\subset\mathbb N$ is $\delta>0$. If
$A+t_1,\ldots,A+t_r$ have pairwise finite intersections, take long intervals on
which $A$'s density tends to $\delta$. A fixed translation changes a count by
$O(|t_i|)$; pairwise intersections contribute $O(1)$. Counting the union gives
$r\delta\le1$. Starting with $t_1=0$, a greedy maximal family of such
nonnegative shifts therefore stops with $r\le\lfloor1/\delta\rfloor$.

For every $t\ge0$, maximality gives an infinite intersection $(A+t)\cap(A+t_i)$
for some $i$. Set $T=\max t_i$. For $t>T$, $t-t_i\in D^+(A)\cap[t-T,t]$. Hence
$D^+(A)$ is syndetic, and at most $r$ of its translates cover the tail. Counting
the cover gives lower density at least $1/r$.

The gap length is not bounded by $\delta$ alone. The periodic set
$A_t=\bigcup_{j\ge0}[3jt+1,3jt+t]$ has density $1/3$; its recurrent-difference
residues modulo $3t$ are $-(t-1),\ldots,t-1$. The missing residues $t,\ldots,2t$
give arbitrarily long gaps at fixed density.

For the opposite test, put $a_n=n(1+\lfloor\log_2n\rfloor)$.
On $2^{k-1}\le n<2^k$, $a_n=kn$; every successive gap in
or at the end of that block is at least $k$. Gaps tend to infinity,
so every fixed positive difference occurs finitely often. Yet
$$
 \sum_{n=2^{k-1}}^{2^k-1}1/a_n\ge1/(2k),
$$
so the reciprocal sum diverges.

Stewart's Theorem 2 account and Belgikar et al. §4.1, definitions (4.1)–(4.4)
and Theorem 4.1 were read. The latter, at $k=1$ along long intervals attaining
upper Banach density, also gives syndeticity, with a stronger positive-density
intersection condition. Its proof was not audited. This recovers a known
sufficient condition, not a full characterization.

The unresolved obligation is to find a meaningful weaker hypothesis than
positive upper Banach density that survives the explicit harmonic-divergence
counterexample. Any proposed weaker condition should first
be checked on the explicit increasing-gap sequence and on positive-density
periodic blocks with arbitrarily long difference gaps. Do not identify recurrent
differences with all differences, infer a density-only numerical gap bound, or
claim that harmonic divergence alone suffices.

Source interfaces:
[[../library/integer_sequences/stewart_1978_difference_sets_sets_integers/theorem_2|Theorem
2; definitions; sharpness and unbounded-shift examples]];
[[../library/integer_sequences/belgikar_2024_new_applications_ergodic_theory_sets_differences/_index|Section
4.1, (4.1)-(4.4), Theorem 4.1; no proof beyond its pointer]].

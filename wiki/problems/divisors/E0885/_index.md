---
name: problems/divisors/E0885
title: Problem 885
desc: |
  Asks whether, for every $k\ge1$, there are integers $N_1<\cdots<N_k$ whose
  factor difference sets $D(N)=\{\lvert a-b\rvert : N=ab\}$ share at least $k$
  common values.
tags:
- Number theory
- Divisors
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 885

[[problems/divisors/_index|..]]

[[problems/divisors/E0885/claims/_index|claims/]]: The 4 claim pages of Problem 885, one per claimant's result; the problem's standing derives from them.

***

**Statement.** For integer $n\geq 1$ we define the factor difference set of $n$
by

$$
D(n) = \{\lvert a-b\rvert : n=ab\}.
$$

Is it true that, for every $k\geq 1$, there exist integers $N_1<\cdots<N_k$ such
that

$$
\lvert \cap_i D(N_i)\rvert \geq k?
$$

**Status.** Bloom's catalog labeled the problem OPEN, and the general question
is open. The instances $k=2$ and $k=3$ are settled by
[[problems/divisors/E0885/claims/1997_01_01_erdos_rosenfeld|Erdős and Rosenfeld's two shared values and Guiduli's triples]]
and
[[problems/divisors/E0885/claims/1999_09_01_jimenez_urroz|Jiménez-Urroz's three shared values]].
The instance $k=4$ is settled by
[[problems/divisors/E0885/claims/2019_05_28_bremner|Bremner's four integers]].
There is also a pending page,
[[problems/divisors/E0885/claims/2026_09_23_sanexxxx777|a Lean proof of the case k = 4]].

**Source.** [erdosproblems.com/885](https://www.erdosproblems.com/885), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #885,
https://www.erdosproblems.com/885.

**References.**

- [Br19] Bremner, Andrew, On a problem of Erdős related to common factor
  differences. Int. J. Number Theory (2019), 1059-1068.
- [ErRo97] Erdős, Paul and Rosenfeld, Moshe, The factor-difference set of
  integers. Acta Arith. (1997), 353-359.
- [Ji99] Jiménez-Urroz, Jorge, A note on a conjecture of Erdős and Rosenfeld. J.
  Number Theory (1999), 140-143.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/70b0d55f6bf429102b019349fcfb6c4e3aafe197/FormalConjectures/ErdosProblems/885.lean).
The file proves `erdos_885.variants.k_eq_4` by an explicit witness, while
`erdos_885`, `erdos_885.variants.k_eq_2` and `erdos_885.variants.k_eq_3` are
stated with proof `sorry`.

## Current assessment

Bloom's catalog labeled the problem OPEN: the answer is yes for $k\le4$ and
unknown for every $k\ge5$. Erdős and Rosenfeld show that any number of integers
can share two factor differences, and their paper prints two triples, found by
Barry Guiduli, that share four values, which settles $k=2$ and $k=3$
([[problems/divisors/E0885/claims/1997_01_01_erdos_rosenfeld|claim page]]).
Jiménez-Urroz raises the two shared values to three for every $k$
([[problems/divisors/E0885/claims/1999_09_01_jimenez_urroz|claim page]]), and
Bremner gives infinitely many sets of four integers sharing four values
([[problems/divisors/E0885/claims/2019_05_28_bremner|claim page]]). A Lean proof
merged into formal-conjectures on 23 September 2026 settles $k=4$ again by an
explicit witness
([[problems/divisors/E0885/claims/2026_09_23_sanexxxx777|claim page]]); this
corpus has not built it.

Three further items in the erdosproblems.com discussion thread settle only
instances already settled by the refereed papers, so they have no claim pages.
Mausberg's note of 19 April 2026, with a Lean repository produced with
Aristotle, gives the $k=3$ witness
$D(79200)\cap D(227205)\cap D(1258560)=\{36,468,692,1028\}$. A post by
Aleksanndr_NFA of 23 September 2026, with no manuscript, gives the $k=4$ example
$515504$, $3542528$, $6010004$ and $19523504$, sharing $872$, $4328$, $5003$ and
$11672$. Two notes posted by zoahdev on 29 September 2026 give three integers
sharing five values and do not reach $k=5$. Every membership in these examples
checks by computation.

## Finite reductions and uniformity requirements

For $N>0$ and $r\ge0$, the exact factor-difference test is

$$
r\in D(N)\quad\Longleftrightarrow\quad
4N+r^2=s^2,\quad s>r,\quad s\equiv r\pmod2.
$$

The maps are $s=a+b$ and $a,b=(s\mp r)/2$. Fix $0\le r_0<r_1$ and write
$\Delta=r_1^2-r_0^2$. Every $N$ admitting both differences comes from a
positive factorization $uv=\Delta$ with $u<v$ and $u\equiv v\pmod2$: set
$s_0=(v-u)/2$, $s_1=(u+v)/2$, and retain $N=(s_0^2-r_0^2)/4$ only when
positive, integral, and satisfying both parity conditions. In particular
$N\le(\Delta-1)^2/16$.

Thus a fixed pair of seed differences gives a complete finite search, while
every additional common difference imposes another square condition. This
author reduction was compared with the inspected constructions in
[[../library/divisors/erdos_1997_factor_difference_set_integers/_index|Erdős–Rosenfeld]].
No bound on the seed pair is proved for the unrestricted problem, and no
numerical search was run. Increasing the number of integers sharing only two
differences does not produce a five-by-five array.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/divisors/erdos_1997_factor_difference_set_integers/_index|erdos_1997_factor_difference_set_integers]]

<!-- END problem library links -->

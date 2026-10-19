---
name: theory/additive_bases/L33_dyadic_root_floor_completeness/_proof
title: Regrouping exponents into two dyadic rays
desc: A sufficiently late tail has distinct positive values and contains two disjoint indexed rays to which the accepted theorem applies.
created: 2026-10-14T18:42:37Z
updated: 2026-10-14T18:42:37Z
---

***

The imported
[[../library/additive_bases/jenw1n_2026_erdos_354_part_i_lean_proof/target|dyadic theorem]]
says that for $u,v>0$ with $u/v$ irrational, every sufficiently large
integer can be written as

$$
\sum_{r\in R}\lfloor u2^r\rfloor+
\sum_{s\in S}\lfloor v2^s\rfloor,
$$

where $R,S$ are finite subsets of the nonnegative integers. An index is
used once in each ray; equal values at different indices are permitted by
that theorem. Its recorded acceptance is on
[[problems/additive_bases/E0354/claims/2026_09_11_jenw1n|the dyadic claim page]].

Fix $m,t,L,F$ as in L33 and put $\gamma=2^{1/m}$. A rational $m$th root
of an integer is an integer, and no integer has $m$th power $2$ for
$m\ge2$. Thus $\gamma$ is irrational and $1<\gamma<2$.

Choose an integer $j\ge L$ so large that

$$
t\gamma^n(\gamma-1)>1\quad(n\ge j),
\qquad \lfloor t\gamma^j\rfloor>\max(F\cup\{0\}).
$$

These inequalities are possible because $t>0$ and $\gamma>1$.
The floor values with indices at least $j$ are positive, strictly
increasing, and outside $F$.

Set $u=t\gamma^j$ and $v=t\gamma^{j+1}$. Both are positive and
$u/v=\gamma^{-1}$ is irrational. Since $\gamma^m=2$,

$$
\lfloor u2^r\rfloor=\lfloor t\gamma^{j+mr}\rfloor,
\qquad
\lfloor v2^s\rfloor=\lfloor t\gamma^{j+1+ms}\rfloor.
$$

The classes $j+mr$ and $j+1+ms$ are disjoint for $m\ge2$.
Consequently each representation given by the dyadic theorem uses
distinct indices of the original tail. Strict increase on that tail
makes their integer values distinct as well. All those values are
positive and avoid $F$, which proves L33.

For Problem 354(ii), choose $m=2$ and $t=\alpha$. Completeness of this
single ray implies completeness after adjoining the $\beta$ ray for
every $\beta>0$, whether or not $\alpha/\beta$ is irrational. The
argument works with first index $0$ or $1$ and with either indexed or
distinct-value sums. The threshold is allowed to depend on every fixed
parameter and the finite deletion. No assertion for arbitrary
$\gamma\in(1,2)$ follows.

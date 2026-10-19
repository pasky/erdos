---
name: research/totient_binary_new_attack/perturbation_barrier
title: Sparse Perturbations of the Totient Reach Every Value
desc: |
  Sparse changes bounded by the square root except at one place, preserving
  growing powers of two, give the binary series any real value. The
  construction preserves empirical distributions of o(log N) windows up to
  o(1), delimiting arguments that use only these shared properties.
tags: []
sources: []
problems:
- 249
created: 2026-10-15T19:52:41Z
updated: 2026-10-15T19:52:41Z
---

# Sparse Perturbations of the Totient Reach Every Value

[[research/totient_binary_new_attack/_index|..]]

***

This page's result is Plasma AI's, author-recorded and without independent
review. It concerns [[problems/irrationality/E0249/_index|Problem 249]], the
irrationality of $S=\sum_{n\ge1}\varphi(n)2^{-n}$. Proposition 1 shows that a
sparse and small change of the totient can give the binary series any
prescribed value, rational or not. Corollary 2 turns this into a precise
limit on distributional arguments: no property that the totient shares with
all such perturbations can decide whether $S$ is rational. In particular, a
proof using only empirical window distributions up to $o(1)$ error,
the preserved residues, and the stated additive size bounds cannot
distinguish these sequences. Quantitative rates, exceptional windows and
arithmetic laws not preserved by the construction remain available. The
[[research/totient_binary_new_attack/proof_sketch|proof sketch]] carries
this precise limitation into the comparison with phase routes.

## The construction

**Proposition 1 (L218).** Let $g,s$ be nondecreasing functions from the
positive integers to the nonnegative integers, and $n_0\ge1$, such that
$s(n)+g(n)\le\frac12\log_2n$ for $n\ge n_0$. Let
$E=\{e_1<e_2<\cdots\}\subset[n_0,\infty)$ be an infinite set of integers with
$e_{k+1}-e_k\le g(e_k)$ for every $k\ge1$. Then for every real number $r$
there is an integer sequence $\psi$ such that

1. $\sum_{n\ge1}\psi(n)2^{-n}=r$, the series converging absolutely;
2. $\psi(n)=\varphi(n)$ for every $n\notin E$;
3. $\psi(e_1)-\varphi(e_1)\in2^{s(e_1)}\mathbb Z$, and for every $k\ge2$,
   $\psi(e_k)-\varphi(e_k)\in2^{s(e_k)}\mathbb Z$ and
   $|\psi(e_k)-\varphi(e_k)|\le e_k^{1/2}$.

This is the claim
[[theory/irrationality/L218_sparse_perturbation_any_value/_index|L218]], and
its [[theory/irrationality/L218_sparse_perturbation_any_value/_proof|canonical
proof]] is a greedy rounding: the change at $e_k$ is the multiple of
$2^{s(e_k)}$ nearest to the remaining error times $2^{e_k}$, which keeps that
error below $2^{s(e_k)-e_k-1}$ and so bounds the next change by
$2^{s+g}\le e^{1/2}$. Check 6 of the [evidence](evidence/main.py) runs this
construction on a finite prefix for four rational targets and verifies each
inequality of the proof there; the proposition itself rests on the proof.

Write $\delta_k=\psi(e_k)-\varphi(e_k)$. Only the first change $\delta_1$ can
be large; it is a single finite modification at $e_1$, of size about
$|r-S|2^{e_1}$. Every later change is at most $e_k^{1/2}$. The elementary
bound $\varphi(n)\ge n/(1+\log_2n)$, obtained by bounding the product over
its ordered prime divisors by $1/(\omega(n)+1)$, gives
$\psi(e_k)=\varphi(e_k)(1+O(e_k^{-1/2}\log e_k))$ and eventual positivity.
This is an additive square-root bound, not a relative $n^{-1/2}$ bound.

## What the perturbed sequences share with the totient

Fix $0<c\le\frac14$ and take

$$
s(n)=\lfloor c\log_2n\rfloor,\qquad
g(n)=\max\bigl(1,\lfloor c\log_2n\rfloor\bigr),\qquad
e_{k+1}=e_k+g(e_k).
$$

Then $s(n)+g(n)\le\frac12\log_2n$ for $n\ge4$, so Proposition 1 applies with
$n_0=4$ and any $e_1\ge4$. Consecutive elements of $E$ differ by exactly
$g(e_k)$, and $g(e)\ge\lfloor\frac c2\log_2X\rfloor$ for $e\ge X^{1/2}$, so
$|E\cap[1,X]|=O(X/\log X)$.

**Corollary 2.** For these choices and every real $r$, the sequence $\psi$
of Proposition 1 has $\sum_n\psi(n)2^{-n}=r$ and moreover:

1. $\psi(n)\equiv\varphi(n)\pmod{2^{\lfloor c\log_2n\rfloor}}$ for every
   $n$; in particular $\psi(n)\equiv\varphi(n)\pmod4$ once
   $c\log_2n\ge2$, so $\psi(n)/2$ is odd exactly where $\varphi(n)/2$ is;
2. $|\psi(n)-\varphi(n)|\le n^{1/2}$ for every $n\ne e_1$;
3. $\psi(n)=\varphi(n)$ outside a set of upper density $0$, and for every
   function $L(N)\ge1$ with $L(N)=o(\log N)$ the proportion of $N\le X$
   whose window $\{N+1,\dots,N+L(N)\}$ meets $E$ tends to $0$ as
   $X\to\infty$.

*Proof.* Items 1 and 2 restate Proposition 1. For item 3, put
$L^*(X)=\max_{N\le X}L(N)$, which is again $o(\log X)$. A window
$\{N+1,\dots,N+L(N)\}$ with $N\le X$ meets $E$ only if $e-L^*(X)\le N<e$ for
some $e\in E\cap[1,X+L^*(X)]$, so at most
$L^*(X)\,|E\cap[1,X+L^*(X)]|=o(\log X)\cdot O(X/\log X)=o(X)$ such $N$
exist. Density zero of $E$ follows from the same count. $\square$

Item 3 says that every statistic of windows of length $o(\log N)$, for
instance the joint distribution of
$(\varphi(N+1),\dots,\varphi(N+L))$ modulo any modulus or as real vectors,
is the same for $\psi$ and $\varphi$ up to $o(1)$ in total variation, along
every sequence $X\to\infty$. Since $r$ is arbitrary, it may be any rational
number, with any denominator. Consequently no argument that uses only
properties shared by $\varphi$ and all such $\psi$ can prove $S$
irrational: such properties are compatible with a rational value. The
shared properties include bounded empirical window statistics up to
$o(1)$ error, the exact congruences modulo
$2^{\lfloor\log_2n/4\rfloor}$, and eventual parity modulo four. The
additive error is at most $n^{1/2}$ away from $e_1$. No assertion is made
about convergence rates or unbounded statistics sensitive to the changed
positions. Eventual parity is relevant to the
[[research/leads/totient_binary_series/integer_interpolation/two_depth_carries|two-depth
page]] uses for odd kernel vectors.

## Scope

The construction does not impose multiplicativity: changing a value at
$e\in E$ need not preserve the relations between $e$ and its multiples.
The set $E$ can, however, be chosen to keep any fixed finite family of them.

**Remark 3 (fixed identities can be kept).** Let $A$ be a finite set of
integers at least two and $Q$ their least common multiple. The integers
$n\equiv1\pmod Q$ are divisible by no element of $A$. Once $g(n)\ge Q$ one
may choose $E$ among them, taking $e_{k+1}=e_k+Q\lfloor g(e_k)/Q\rfloor$, so
that every gap lies in $(g(e_k)/2,g(e_k)]$; Proposition 1 then applies, and
so does the counting of Corollary 2, since $E$ again has $O(X/\log X)$
elements up to $X$. The
resulting $\psi$ agrees with $\varphi$ at every multiple of every element
of $A$, so it satisfies every identity among totient values at such
multiples. For $A=\{2,3\}$ this includes $\psi(3k)=2\psi(2k)$ for all odd
$k$ prime to three, the identity that the
[[research/leads/totient_binary_series/integer_interpolation/phase_localization|arithmetic
localization]] uses.

So that identity, together with the information listed in Corollary 2,
cannot decide the problem; this matches its role there, where it yields an
equivalence rather than a proof. The remark does not reach identities that
relate a value at an arbitrary integer $m$ to a value at a multiple of $m$,
such as $\varphi(pm)=(p-1)\varphi(m)$ for $p\nmid m$, because $E$ cannot avoid
every $m$. The
[[research/leads/totient_binary_series/dilation_cube|prime dilation cubes]]
rest on identities of that kind with growing primes, and the proposition says
nothing about them. The stronger
[[research/totient_binary_new_attack/partial_multiplicativity|partially
multiplicative comparison]] does preserve those laws for any fixed finite
set of primes, together with every prime-power value. Neither construction
imposes full multiplicativity. Nor does this comparison obstruct statistics of
windows of length at least a constant multiple of $\log N$, such as the
one-window phase average with window length $\log_2N+O(1)$ on the
[[research/leads/totient_binary_series/_index|lead page]]: with the choices
above, a window of length $\log_2N$ meets $E$ about $1/c$ times. What it
does show is that $o(1)$-accurate empirical distributions of shorter
windows, combined only with the preserved data, do not supply a phase
saving. A proof may instead use more accurate errors, selected exceptional
windows, further exact identities, or a global argument.

A multiplicative analogue is open. One would ask for an integer-valued
multiplicative $\psi$ with $|\psi(p^a)-\varphi(p^a)|\le p^{a/2}$ at every
prime power and a rational binary series. The construction above does not
supply one. A multiplicative function can be changed independently at
prime powers, but each change also affects other coefficients. Even if
one kept only the leading prime contributions, a nearest-integer scheme
would have an error bound amplified by $2^{p'-p}$ between successive
primes; this does not bound the required corrections by $p^{1/2}$.
A successful construction must control all the affected multiples as well.
A positive answer would show that exact multiplicativity together with
these approximate prime values cannot decide the problem. A negative
answer would imply the target, since $\psi=\varphi$ is admissible. Neither
answer is established here.

Counting shows that small changes at primes alone have too little freedom
to reach a typical target. For $0\le\theta<1$ let $V_\theta$ be the set of
values $\sum_n\psi(n)2^{-n}$ over multiplicative integer-valued $\psi$
with $\psi(p^a)=\varphi(p^a)$ for $a\ge2$ and
$|\psi(p)-(p-1)|\le p^\theta$ at every prime $p$.

**Remark 4.** The upper box-counting dimension of $V_\theta$ is at most
$\theta/\ln2$. In particular $V_\theta$ is Lebesgue-null for
$\theta<\ln2$.

*Proof.* Such $\psi$ satisfy
$|\psi(n)|\le\prod_{p^a\|n}p^{a-1}(p-1+p^\theta)\le n\,3^{\omega(n)}$, so
the terms with $n>M$ contribute at most $\varepsilon_M=\sum_{n>M}n3^{\omega(n)}2^{-n}
=2^{-M(1+o(1))}$. The terms with $n\le M$ depend only on the values
$\psi(p)$, $p\le M$, which take at most
$\prod_{p\le M}(2p^\theta+1)\le3^{\pi(M)}e^{\theta\vartheta(M)}=e^{\theta M+o(M)}$
values by the prime number theorem, $\vartheta$ being Chebyshev's function.
This uses its ordinary fixed-modulus specialization $q=1$, at the
external standing disclosed on the
[[research/leads/totient_binary_series/integer_interpolation/phase_localization|arithmetic
localization page]]; no analytic proof is reconstructed here.
So $V_\theta$ is covered by $e^{\theta M+o(M)}$ intervals of length
$2\varepsilon_M$, and the dimension is at most
$\lim_M(\theta M+o(M))/(M\ln2)=\theta/\ln2$. $\square$

The counting bound limits coverage of an interval, not membership of a
particular value. Whether $V_\theta$ contains a rational number is not
settled by its dimension, even when $\theta<\ln2$.

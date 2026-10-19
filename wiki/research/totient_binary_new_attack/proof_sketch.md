---
name: research/totient_binary_new_attack/proof_sketch
title: Proof Sketch for a Fresh Attack on the Binary Totient Series
desc: |
  Exact base-two target and complete-tail criterion, quantitative kernel
  shadows, rational comparisons preserving all prime-power values and fixed
  prime laws, scoped construction obstructions, and the remaining estimates.
tags: []
sources: []
problems:
- 249
created: 2026-10-15T19:52:41Z
updated: 2026-10-15T19:52:41Z
---

# Proof Sketch for a Fresh Attack on the Binary Totient Series

[[research/totient_binary_new_attack/_index|..]]

***

## Target and standing

The target is [[problems/irrationality/E0249/_index|Problem 249]] in its
exact form: is

$$
S=\sum_{n\ge1}\frac{\varphi(n)}{2^n}=1.3676308019850\ldots
$$

irrational? Other bases and modified coefficient sequences are different
questions. The problem page records the target as open. This sketch
contains no proof or disproof. Its original arguments are Plasma AI's,
author-recorded and without independent review. The claims L218, L219 and
L220 are at tier 0. The
[[research/leads/totient_binary_series/_index|existing lead]] and its
subordinate results retain their recorded standing; a review of that lead
does not cover the arguments here or its later dilation construction.

## Complete tails and the sufficient kernel criterion

For $n\ge0$ and $J\ge1$ put

$$
\Phi_n=\sum_{m=1}^n\varphi(m)2^{n-m},\qquad
T_n=2^nS-\Phi_n=\sum_{j\ge1}\frac{\varphi(n+j)}{2^j},\qquad
U_J(n)=\sum_{j=1}^J\varphi(n+j)2^{J-j}.
$$

Then $0<T_n\le n+2$ and $2^JT_n=U_J(n)+T_{n+J}$. If $S=a/b$ with
integers $a$ and $b\ge1$, every $bT_n$ is an integer. For a finitely
supported integer vector $z$ on $n\ge B\ge4$, define

$$
u=\sum_nz_n2^n,\qquad v=\sum_nz_n\Phi_n,\qquad
C_J(z)=\sum_n|z_n|(n+J+2).
$$

If $\sum_nz_nU_J(n)=0$, the complete identity is

$$
uS-v=2^{-J}\sum_nz_nT_{n+J},\qquad
|uS-v|\le 2^{-J}C_J(z),\qquad 2^B\mid u.
\tag{1}
$$

Call $z$ *odd* when $v\equiv2\pmod4$. Write a proposed denominator as
$b=2^s q$, with $q$ odd. If $s+1<B$, rationality would give
$v_2(au-bv)=s+1$, hence $|uS-v|\ge2/q$. Thus

$$
s+1<B,\qquad qC_J(z)<2^{J+1}
\tag{2}
$$

exclude that denominator. This is the valuation-gap argument of
[[research/leads/totient_binary_series/integer_interpolation/two_depth_carries|Proposition
6 and Corollary 7 of the two-depth page]], with the full tail retained.
Consequently an odd family with $B\to\infty$ and $C_J(z)=o(2^J)$ proves
irrationality. On $[J,2J]$, $J\ge4$, the simpler condition
$bC_J(z)<2^{J+1}$ suffices: oddness implies $C_J(z)\ge2J+2$, which
ensures the cutoff condition in (2).

The author-recorded
[[research/leads/totient_binary_series/integer_interpolation/phase_localization|arithmetic
localization theorem]] proves a converse on a subsequence of powers of
two: irrationality is equivalent to the existence of such cheap odd
vectors on $[J,2J]$. That inherited argument uses the fixed-modulus prime
number theorem at its disclosed external standing. The equivalence does
not supply the vectors.

## What the short-support construction establishes

The [[research/totient_binary_new_attack/kernel_rigidity|kernel page]]
proves the following statements, with its hypotheses explicit.

For $J=2^m$ sufficiently large, the shadows $(u,v)$ of integer kernel
vectors on $[J,2J]$ fill $2^J\mathbb Z\times2\mathbb Z$. At an individual
$J$, the sufficient column-generation condition can be checked directly.
Put

$$
\gamma_J=\min_{1\le k<2^{J-1}}
 \left\|k2^{J-2}S-\tfrac12\right\|,
\qquad
\kappa_J=\min_{\substack{z\text{ odd}\\\sum z_nU_J(n)=0}}C_J(z),
$$

where $\|\cdot\|$ is distance to the nearest integer and the minimum for
$\kappa_J$ uses $[J,2J]$. Under the auxiliary-prime hypotheses of its
Lemma 4, Corollary 6 gives

$$
\kappa_J\le160J^6(1+2^J\gamma_J).
\tag{3}
$$

Conversely, an odd vector of cost $C<2^{J+1}$ yields a nonzero integer $k$
with

$$
|k|\le\frac{2^JC}{2J+2},\qquad
\left\|k2^{J-2}S-\tfrac12\right\|\le2^{-J-2}C.
\tag{4}
$$

These are two implications with different multiplier ranges; they are
not an equivalence at the same approximation threshold. In particular,
$\gamma_J=o(J^{-6})$ on an unbounded subsequence of powers of two would
make (3) satisfy the criterion (2). No such estimate is proved.

The complementary-pair identity on the same page shows that vectors
whose cancellation is robust under multiplication laws at any fixed
finite set of primes have $u=0$ for sufficiently large even $J$.
Fixing every prime-power value does not remove this eventual obstruction.
The precise robustness class and sufficient thresholds are in that page.
Its finite LLL computations find bases containing cheap odd vectors for
$J\in\{16,32,64,128\}$. They do not compute minima or establish an
asymptotic construction.

## Fixed-prime laws on supports of any length

The claim
[[theory/irrationality/L220_partial_multiplicativity_interval/_index|L220]]
constructs positive integer functions $f$ whose binary sums fill an open
interval about $S$. For every fixed $y\ge2$, modulus $M$ and
$0<\varepsilon<1$, these functions preserve all prime-power values,
congruence to $\varphi$ modulo $M$, relative error at most $\varepsilon$,
and both exact totient multiplication laws at every prime $p\le y$.
Only $O(X/\log X)$ values up to $X$ change. Complete contributions from
all smooth multiples of a changed rough integer are included in the
rounding weights. This is partial multiplicativity, not full
multiplicativity.

The interval contains a dyadic rational. Applying the kernel identity to
that comparison gives the
[[research/totient_binary_new_attack/partial_multiplicativity|support-independent
cost bound]]: for each fixed $y$ and $\varepsilon$, there is $B_0$ such
that every odd kernel vector supported on $n\ge B_0$, whose cancellation
holds for all functions with those fixed-prime laws and prime-power
values, satisfies

$$
C_J(z)\ge\frac{2^{J+1}}{1+\varepsilon}.
\tag{5}
$$

There is no upper restriction on support length. Along any such family
with lower cutoff tending to infinity,
$\liminf C_J(z)/2^J\ge2$. Thus simply widening the support does not turn
fixed-prime robust relations into the required $o(2^J)$ family.

When $y$ grows, choose distinct primes $r_0,t_0>y$ and let
$Q=r_0t_0\prod_{p\le y}p$. The same page gives the explicit weaker bound
$C_J(z)\ge2^{J-Q-3}$, with no cutoff requirement. If $Q=o(J)$, it excludes
cost $2^{o(J)}$, but it does not exclude every $o(2^J)$ cost. No uniform
version of (5) as $y\to\infty$ is established.

## Other comparisons and their limits

The sparse rounding claim
[[theory/irrationality/L218_sparse_perturbation_any_value/_index|L218]]
gives any prescribed real binary sum while changing $\varphi$ only
sparsely, by multiples of $2^{\lfloor\log_2n/4\rfloor}$, with additive
error at most $\sqrt n$ except at one place. The
[[research/totient_binary_new_attack/perturbation_barrier|comparison note]]
proves that empirical distributions of windows of length $o(\log N)$
agree up to $o(1)$ in total variation. Arguments using only these shared
properties cannot distinguish rational sums. This does not exclude
quantitative error rates, selected exceptional windows, arithmetic laws
not preserved, or global arguments. In particular it proves no universal
requirement that every irrationality proof use logarithmic windows.

The dilation claim
[[theory/irrationality/L219_dilation_design_prime_count/_index|L219]]
shows that nonempty signed prime designs cancelling levels $1,\ldots,K$
for every function, with primes greater than $K$ and compatible shifts,
need at least $K+1$ distinct primes. If their modulus is at most $x$, this
forces $K\le(1+o(1))\ln x/\ln\ln x$. The
[[research/totient_binary_new_attack/dilation_designs|design note]]
records the resulting limit on formal cancellation when the tail cutoff
is of order $\log x$, as in the retained averaged-error method. A
six-prime example improves the three-level cube's vertex count, without
supplying the missing phase estimate.

The [[research/totient_binary_new_attack/residue_lifting|residue-lifting
obstruction]] explains a separate failed transfer. With
$R_m=\sum_n(\varphi(n)\bmod m)2^{-n}$ one has
$0<S-R_m\le(m+2)2^{-m}$, but whenever a nonempty zero block starts at
$N+1$, $2^N(S-R_m)\ge m/2$. Thus the positive difference cannot be
ignored in a small-tail contradiction at the zero block. Irrationality
of bounded residue series alone does not handle the full series.

The [[research/leads/totient_binary_series/window_cost|termwise window
bounds]] concern whole-progression divisibility constructions. They do
not bound selected representatives or every possible tail method.
For a square-divisible prime cube with primes greater than $K$ and
pairwise distinct positive tail indices, the normalized weights give a
kernel vector at depth $K$ with $2^K$ nonzero integer coefficients. Its
cost is at least $2^K(K+3)$, so this direct cost bound is insufficient.
This observation requires distinct indices; it is not a prohibition on
all cube constructions or signed phase estimates.

The coprime-pair identity

$$
S-\tfrac12=Z(\tfrac12,\tfrac12),\qquad
Z(x,y)=\sum_{\substack{a,c\ge1\\\gcd(a,c)=1}}x^ay^c
      =xy+Z(xy,y)+Z(x,xy)
$$

is another exact representation. Splitting coprime pairs into $a=c=1$,
$a<c$ and $a>c$ proves the functional equation. No theorem establishing
irrationality of this specialization from that equation is supplied.
The Möbius and cross-base representations likewise provide identities
without a denominator-cleared error estimate that reaches the target.

## Open interfaces and conditions for reopening

One way to finish is a family in (2) with $B\to\infty$ and
$C_J(z)=o(2^J)$. On the short support, (3) offers the sufficient target
$\gamma_J=o(J^{-6})$ along powers of two. Both remain open.

An alternative is a phase saving: for each fixed positive integer $q$,
find $\delta_q>0$ and arbitrarily large $X$ such that

$$
\left|\frac1X\sum_{N=1}^X e(qT_N)\right|\le1-\delta_q,
\qquad e(t)=\exp(2\pi i t).
$$

Rationality with denominator $q$ makes every summand one. A family of
multipliers containing a multiple of each candidate denominator also
suffices. The normalized
[[research/leads/totient_binary_series/dilation_cube|dilation construction]]
provides a different sufficient phase target with a complete averaged
error bound; its required saving on the same progression and scales is
still unproved.

The fixed-prime cost obstruction can be escaped by a genuinely growing
prime set, by further relations among rough composite arguments, or by
cancellation that is not robust in its comparison class. None of these
has supplied a cheap odd family here. A fully multiplicative comparison
with approximate prime-power values is also unresolved; the fixed-prime
comparison is not such a construction. New work on that question must
control the contributions from all affected multiples.

The [finite evidence](evidence/_index.md) tests the stated examples and
bounds. No finite computation, author check or change of coordinates here
closes the irrationality gap.

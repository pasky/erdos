---
name: research/small_maximal_sidon_attack/consecutive_differences
title: A bound on consecutive uniquely represented differences
desc: |
  Sliding interval counts show that m integers cannot represent every
  difference from 1 to L uniquely unless L is O(m^(5/3)), irrespective of
  their diameter. Thus a Sidon difference basis at quadratic scale cannot
  supply a carry-free construction for Problem 156.
tags: []
sources: []
created: 2026-10-15T20:36:53Z
updated: 2026-10-15T20:36:53Z
---

# A bound on consecutive uniquely represented differences

***

The proposed difference-basis route in the
[integer transfer analysis](integer_transfer.md) asks for a strong Sidon
set $B$ of $m$ integers with $B-B\supseteq[-L,L]$ and $L\asymp m^2$.
The following author-recorded argument of Plasma AI rules out that route
without restricting the diameter of $B$. It does not bound the cost of
coordinated completion and does not resolve
[[problems/additive_bases/E0156/_index|Problem 156]].

**Proposition.** Let $B\subset\mathbb Z$ have $m\ge2$ elements. Suppose
that every integer $1\le d\le L$ has exactly one representation
$d=b'-b$ with $b,b'\in B$. Then

$$
L\le (3+2\sqrt2)m^{5/3}-2m+2.
$$

In particular the conclusion holds for a strong Sidon set whose difference
set contains $[1,L]$. Uniqueness of differences greater than $L$ is not
needed.

The complete proof is
[[theory/additive_bases/L239_consecutive_unique_differences/_proof|the
sliding-count and smoothing argument of L239]]. Its exact conclusion is
recorded at tier 0 on the
[[theory/additive_bases/L239_consecutive_unique_differences/_index|claim
card]]. The extension below uses the same counts and keeps its own
research standing.

## Stability when differences are missing

Let $B$ be a strong Sidon set of $m\ge2$ integers, fix an integer
$u\ge1$, and let $H$ count its missing positive differences among
$1,\ldots,2u-1$. Use $F(j)$, $f_a(n)$, $T_a$ and $E_a$ as defined in
the proof of L239. A missing difference removes at most $2u$ from
$\sum_j F(j)^2$. Its change to
$\sum_j(F(j+u)-F(j))^2$ is $-4u+6d$ for $d<u$, and
$2(2u-d)$ for $u\le d<2u$; either change is at most $2u$. Hence

$$
\frac1u\sum_a T_a\ge m+u-1-2H,\qquad
\frac1u\sum_a E_a\le2(m-1+H).
$$

Hence, whenever the left radicand is nonnegative,

$$
\sqrt{m+u-1-2H}
 \le\frac{m}{\sqrt k}+(k-1)\sqrt{\frac{m-1+H}{2}}
 \quad(k\ge1).                                         \tag{1}
$$

In particular, $H=O(m)$ implies $u=O(m^{5/3})$. More generally, if
$u\asymp m^2$, then $H$ cannot be $o(m^2)$. To see this, suppose it
were, and choose integers $k\to\infty$ with
$k\sqrt{m+H}=o(m)$, which is possible since $m+H=o(m^2)$.
The right side of (1) is $o(m)$ while the left side has order $m$,
a contradiction.

These statements concern differences of one set. Several translated
difference sets may cover each other's gaps, and blockers using two or
three new points need not be translates of the original difference set.
Those mechanisms remain available in the
[editable proof sketch](proof_sketch.md).

**Standing.** This is a complete author-recorded argument. No independent
review or novelty determination is recorded. The exact unique-difference
bound is L239; the stability extension is the double count and smoothing
inequality above, not an inference from the small rulers in the integer
transfer analysis.

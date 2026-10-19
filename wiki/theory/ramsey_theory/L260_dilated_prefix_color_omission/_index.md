---
name: theory/ramsey_theory/L260_dilated_prefix_color_omission
title: No long color-omitting dilated prefix below the Schur growth rate
desc: |
  Refuted: no exponential threshold below the growth rate of the Schur
  numbers forces every coloring above it to have a dilated prefix of
  length delta N omitting a color; the constant-loss recursion this would
  give is unavailable in that form.
tags: []
sources:
- problems/ramsey_theory/E0483
id: L260
statement: |
  Let S(k) be the largest N such that {1, ..., N} has a coloring by at most
  k colors with no monochromatic solution of x + y = z (x = y allowed), and
  let L = liminf_{n -> infinity} S(n)^(1/n). For a coloring of {1, ..., N},
  the dilated prefix of length m along d is {d, 2d, ..., md}, for positive
  integers d and m with md <= N. Claim: there are real numbers delta in
  (0, 1) and 1 <= A < L and an integer k_0 such that for all integers k >= k_0
  and N >= A^k, every coloring of {1, ..., N} by at most k colors with no
  monochromatic solution of x + y = z has a dilated prefix of length at
  least delta*N on which one of the colors the coloring uses does not
  occur.
status: refuted
tier: 0
depends_on: []
created: 2026-10-15T23:12:24Z
updated: 2026-10-15T23:12:24Z
---

# No long color-omitting dilated prefix below the Schur growth rate

[[theory/ramsey_theory/_index|..]]

[[theory/ramsey_theory/L260_dilated_prefix_color_omission/_refutation|_refutation]]: For every delta and every exponential threshold below the growth rate, a
composition of a small-depth random Bohr coloring with a near-extremal
coloring has no color-omitting dilated prefix of length delta N.

***

This refuted claim is recorded by Plasma AI. It is the constant-loss
recursion first tested in the
[[research/schur_number_growth/proof_sketch|attack on Problem 483]], in
its strongest form with an exponential threshold below the growth rate.
The [[theory/ramsey_theory/L260_dilated_prefix_color_omission/_refutation|refutation]]
constructs, for every $\delta\in(0,1)$, every $1\le A<L$ and arbitrarily large
$k$, a coloring above the threshold with no color-omitting dilated prefix
of length $\delta N$; the eventual form $k\ge k_0$ excludes only the
trivial small cases, such as one color on $\{1\}$.

## Why it was tested

A dilated prefix along $d$ that omits a color pulls back, by
$j\mapsto c(dj)$, to a coloring of $[1,m]$ with fewer colors and no
monochromatic $x+y=z$, because $dj+dj'=dj''$ exactly when $j+j'=j''$. So
the claim with constants $\delta$, $A$ and $k_0$ would give
$S(k)\le\max(A^k,S(k-1)/\delta)$ for $k\ge k_0$, and hence
$f(k)\le C\max(A,1/\delta)^k$ for every $k$ and some $C$, an exponential
bound for [[problems/ramsey_theory/E0483/_index|Problem 483]]. If the
restriction $A<L$ is dropped, existence of some such threshold lemma is
equivalent to an exponential upper bound: conversely, if $S(k)\le C^k$
for every $k$, any threshold $A>C$ makes the assertion vacuous. The
refutation rules out every threshold below $L$.
Since $L\ge380^{1/5}$ by
[[../library/ramsey_theory/ageron_2021_new_lower_bounds_schur_weak_schur/inequality_6|inequality (6) of Ageron et al.]],
every threshold $1\le A<380^{1/5}$ fails, and so does the threshold-free
version $A=1$; with Schur's tripling construction alone, $L\ge3$.

## Scope and reopening

- The refutation covers every statement that, from $N\ge A^k$ with $A<L$
  alone, produces a color-omitting set containing a dilated prefix of length
  $\delta N$; a homogeneous generalized arithmetic progression with such a
  side is one.
- It does not cover colorings that are near-extremal in a stronger sense.
  The constructed colorings satisfy $N\le\varepsilon S(k)$ with
  $\varepsilon=(s+1)/S(m)$, exponentially small in the number $m$ of added
  colors. This follows by comparing $N=sP+t\le(2s+1)S(n)$ with the
  composition bound $S(m+n)\ge(2S(m)+1)S(n)+S(m)$, and using
  $S(m)\ge(3^m-1)/2$. Thus this construction supplies no fixed positive
  lower bound for $N/S(k)$. A lemma restricted to
  $N\ge\varepsilon_0 S(k)$ for a fixed $\varepsilon_0>0$ remains
  undecided; its extremal case $N=S(k)$ is all the recursion needs.
  Reopening needs such a hypothesis or another property of near-extremal
  colorings that the construction does not supply.
- It says nothing about the recursion $S(k)\le CS(k-1)$ itself.

The [[research/schur_number_growth/evidence/_index|research evidence]]
retains one explicit instance: a Schur-free 24-coloring of $[1,63239]$ whose
longest color-omitting dilated prefix has length 3515, below
$(46/800)\cdot63239$. It refutes the threshold-free version at
$\delta=46/800$ only; the refutation covers every $\delta$.

## Standing

Refuted at tier 0, author-recorded; no independent examination is
recorded. The refutation is a complete proof using Bertrand's postulate,
an elementary variance bound and the definition of $L$; the numerical
threshold $380^{1/5}$ uses the source inequality, whose computer-found
template the library has not checked. Nothing remains open within the
stated scope.

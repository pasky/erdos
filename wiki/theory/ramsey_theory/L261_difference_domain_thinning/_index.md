---
name: theory/ramsey_theory/L261_difference_domain_thinning
title: Difference domains admit no uniform color-losing thinning
desc: |
  Refuted: no fixed proportion of an arbitrary finite set keeps its
  positive differences free of one color under every Schur-free coloring
  of those differences; powers of four encode triangle-free colorings,
  whose Ramsey ratios are unbounded.
tags: []
sources:
- problems/ramsey_theory/E0483
- problems/ramsey_theory/E0183
id: L261
statement: |
  For a finite set X of integers let D(X) = {y - x : x, y in X, x < y}. A
  coloring of D(X) is Schur-free if no color class contains a, b and a + b
  (a = b allowed). Claim: there is a real number delta > 0 such that for
  every integer k >= 2, every finite set X of integers and every Schur-free
  coloring of D(X) by k colors, some subset Y of X with |Y| >= delta*|X|
  has the property that some color does not occur on D(Y).
status: refuted
tier: 0
depends_on: []
created: 2026-10-15T23:12:24Z
updated: 2026-10-15T23:12:24Z
---

# Difference domains admit no uniform color-losing thinning

[[theory/ramsey_theory/_index|..]]

[[theory/ramsey_theory/L261_difference_domain_thinning/_refutation|_refutation]]: Every Schur relation among differences of powers of four is an endpoint
triangle, so triangle-free edge colorings become Schur-free colorings of
difference domains and no proportion of the vertices survives a color.

***

This refuted claim is recorded by Plasma AI. It is the hereditary form of
a constant-loss step in Schur's argument, tested in the
[[research/schur_number_growth/proof_sketch|attack on Problem 483]]. If it
held, iterating it down to one color, where three points $x<y<z$ already
give $(y-x)+(z-y)=z-x$, would give $|X|\le2\delta^{-(k-1)}$, and $X=[0,S(k)]$
would give an exponential bound for
[[problems/ramsey_theory/E0483/_index|Problem 483]].

The [[theory/ramsey_theory/L261_difference_domain_thinning/_refutation|refutation]]
takes $X=\{4^0,\ldots,4^{n-1}\}$, where every relation $a+b=c$ among
differences is an endpoint triangle, so each triangle-free edge coloring of
$K_n$ becomes a Schur-free coloring of $D(X)$ and a subset losing a color
has at most $R_{k-1}(3)-1$ points. Its one premise is the statement of
[[problems/ramsey_theory/E0183/claims/2026_08_01_openai|the accepted claim on Problem 183]],
which makes the ratios $(R_k(3)-1)/(R_{k-1}(3)-1)$ unbounded.

## Scope and reopening

- This is not a Schur construction: only $D(X)$ is colored, inside a range
  of length $4^{n-1}$, and it is consistent with an exponential bound for
  intervals.
- It refutes uniform constant-fraction color-omitting thinning on all
  difference domains with only their Schur relations assumed. It does not
  by itself decide a thinning lemma
  restricted to intervals, sets of small doubling, or another class
  excluding the sparse encodings. Merely requiring $X$ to be a Bohr cell
  of unrestricted rank does not exclude them: the refuted claim
  [[theory/ramsey_theory/L266_bohr_cell_uniform_avoidance/_index|L266]]
  supplies such a cell explicitly. A preserved quantitative invariant of
  the interval is needed to reopen this route.

The [[research/schur_number_growth/evidence/_index|research evidence]]
checks the base-four lemma exhaustively for $n\le8$, including the count
of $\binom n3$ relations.

## Standing

Refuted at tier 0, author-recorded; no independent examination is
recorded. The refutation is complete given the accepted statement on
Problem 183, which enters at statement level only. Nothing remains open
within the stated scope.

---
name: research/erdos_1145/prefix_resonance
title: Exact resonances obstruct a uniform estimate from local path restrictions
desc: |
  An arbitrary large path can be matched by admissible smaller paths so
  that one target has logarithmically many distinct representations.
  The all-prefix estimate needs coordination across scales; the local
  increment restrictions and pairwise bounds do not supply it.
tags: [construction, obstruction, unresolved]
sources: []
created: 2026-10-15T11:57:22Z
updated: 2026-10-15T11:57:22Z
---

***

The target is the uniform whole-prefix estimate (5) of the
[monotone-path sketch](monotone_path_shells.md), in the ordered-pair
convention of [[problems/additive_bases/E1145/_index|Problem 1145]]. The
problem page records only the dated catalog status, not a current literature
assessment. This is a test of the specified construction, not a new status
assessment. Original mathematics here is due to Plasma AI.

## The test and its outcome

Fix the scale schedule and the admissible path class of the sketch:
$\mathcal Q=\{2^j,3\cdot2^{j-1}:j\ge4\}$, with increments in $\{1,2\}$
and no $111$ or $22$. The proposed estimate must control, uniformly in
$Q,n$, the sum of
$r_{A_Q,P^B_{<Q}}(n)$ and $r_{P^A_{<Q},B_Q}(n)$. The pairwise estimate
$1168$ controls only one small scale at a time.

[[theory/additive_bases/L126_path_shell_resonance/_index|L126, tier 0]],
with its complete algebraic proof, shows a precise obstruction to proving
that estimate from these local hypotheses alone. For **any** prescribed
admissible $h_Q$ at a dyadic $Q=2^k$, admissible paths at the smaller
dyadic scales $16\sqrt Q\le q\le Q/256$ can make

$$
r_{A_Q,P^B_{<Q}}(3Q^2+h_Q(2Q))\ge\lfloor k/2\rfloor-11.
\tag{1}
$$

The construction includes the exact carries. Put $V=2Q$, choose
$y=(Q/q)t-q+1$ between $7q/10$ and $18q/25$, and set
$h_q(y)=q-[h_Q(V)-h_Q(V-t)]$. This integer height lies between
$4y/3$ and $3y/2$, so it is attained by a prefix made from $12$ and $112$.
The bare summands then satisfy

$$
[Q^2+Q(V-t)+h_Q(V-t)]+[q^2+qy-h_q(y)]
=3Q^2+h_Q(2Q).
$$

Their small summands occupy disjoint intervals at the dyadic scales.
Thus (1) counts actual distinct ordered representations, rather than
multiple block descriptions of one pair. Disjoint ranges of scales allow
one infinite admissible family with $r(n)\gg\log n$ along a subsequence.
The sketch's $O(\log n)$ upper bound is therefore sharp in order of
magnitude over this path class. This conclusion does not rely on a common
prefix or a fixed slope for the large paths.

## What remains open

The quantifiers are essential. The result constructs bad smaller paths
for every prescribed large path. It does not say that every coherent
infinite choice of all the paths has such a peak. Paths selected jointly
could avoid the prescribed heights simultaneously; no such selection
theorem with a uniform whole-prefix bound is established.

The retained implications are:

- admissible paths give termwise balance and cofinite coverage, by the
  elementary arguments in the [sketch](monotone_path_shells.md);
- pairwise interaction bounds give $O(\log n)$ representations;
- local admissibility alone permits peaks of that order, by L126;
- an additional global selection invariant satisfying (5) would give a
  bounded representation construction and answer Problem 1145 negatively.

The last premise is missing. A bound $1\le r(n)\le M$ would imply only
$A(x)B(x)\le2Mx+O(1)$, so neither a uniqueness theorem nor the product
threshold with $k=1$ removes this gap. No periodic or eventually constant
representation hypothesis is imposed or obtained here.

**Stopped estimate and reopening condition.** The local-path test stops
at the sharp logarithmic bound. Reopening needs a compatible choice of
paths at all scales that prevents simultaneous resonances such as (1),
preserves the finite coverage bands, and proves (5) with one constant
independent of the number of earlier shells. A bound for each shell pair,
or another summation of constant errors over those shells, does not meet
that condition. L126 is author-recorded, not independently reviewed; it
resolves no catalog problem.

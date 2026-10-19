---
name: research/geometric_configuration_interfaces/rich_lines
title: "Rich lines and real-planar realization"
desc: "Separate fixed-cap little-o questions from near-quadratic constructions, abstract incidence systems and maxima of different line counts."
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

***

The deductions and obstructions here are author-recorded by Plasma AI.
Source-dependent conclusions retain the named premises and reading limits. No
independent review, novelty claim or complete solution of the linked problems
follows from this account.

The relevant questions are [[problems/discrete_geometry/E0101/_index|E0101]],
[[problems/discrete_geometry/E0102/_index|E0102]],
[[problems/discrete_geometry/E0588/_index|E0588]],
[[problems/discrete_geometry/E0589/_index|E0589]],
[[problems/discrete_geometry/E0669/_index|E0669]].

## Rich lines and planar realization: E0101, E0102, E0588, E0589, E0669

For E0101 and E0588, Solymosi--Stojaković, Theorem 1, constructs for each fixed
k at least four an n-point real planar set with no k+1 collinear and more than
$$
 n^{\,2-c_k/\sqrt{\log_2 n}},\qquad c_k=2\log_2(4k+9),
$$
k-point lines. The theorem statement and the projection setup in Sections
1.1--1.2 were inspected. The ratio of the displayed quantity to n squared is
$$
 2^{-c_k\sqrt{\log_2 n}}\longrightarrow0.
$$
For every fixed positive epsilon its ratio to n to the power 2-epsilon tends to
infinity. Thus the lower bound rules out a fixed power saving, while remaining
compatible with the conjectured little-o bound. This comparison makes no
upper-bound assertion about the actual number of lines in the construction. A generic projection preserves
the needed incidences; it does not preserve distances.

The distinction from abstract incidence spaces is substantive. In the affine
space over the field with q elements, with n=q^m points, each affine line has q
points and each pair determines exactly one line. There are exactly
n(n-1)/(q(q-1)) lines. Taking q=4 gives quadratic density with no abstract
five-point line. This is not a real planar counterexample. A noncollinear finite
real planar set has an ordinary line, whereas this affine incidence system has
none. Thus a bound based solely on pairwise linear incidence cannot distinguish
the conjecture's real-realizability requirement. For general k this example is
asserted only when k is a prime power.

The ordinary-line fact has a short direct proof. Among all point/line pairs with
positive distance, with the line determined by two set points, minimize that
distance, say from P to the line l. If l contained three set points, two of them
A,B could be chosen on the same closed side of the perpendicular foot Q, with A
nearer Q. The positive distance from A to the line PB is dist(P,l) times
|AB|/|PB|, strictly smaller because |AB|<=|QB|<|PB|. This contradicts
minimality. Thus l contains exactly two set points.

E0102 asks for more: for each positive density c, maximum collinearity must
diverge. Equivalently, for each fixed K the maximum number of four-rich lines
among n-point sets of maximum collinearity at most K is o(n squared). In one
direction a positive-density sequence with fixed cap K contradicts divergence.
In the other, failure of divergence gives a fixed c, a bounded subsequence of
forced maximum collinearities, and such configurations. This statement implies
E0101 and E0588, because a k-point line is four-rich when k is at least four. No
converse from those individual statements is asserted.

Currier's Theorem 1.3 at alpha=1/2 gives point sets of the form A times B with
both factors of order square-root n and quadratically many rich lines of any
fixed requested richness. Any nonvertical line meets such a product at most |A|
times and any vertical line at most |B| times; the horizontal and vertical lines
already attain those growing scales. This only provides an O(square-root n)
upper example for h_c at appropriate construction densities. It does not give a
bounded-cap counterexample. Constants in a fixed-alpha theorem cannot silently
be made uniform in an alpha varying with n.

For E0589, make one hyperedge for every collinear triple. No four collinear
means two distinct hyperedges share at most one vertex. The independence bound
for partial Steiner triple systems cited and specialized in Füredi 1991,
inequality (2.2) and Section 2.1, therefore gives at least c square-root(n log
n) points with no collinear triple. The Phelps--Rödl theorem is an external
premise here, not a proof checked in this account. Balogh--Solymosi, Theorem
2.1, gives the real-planar upper construction n^(5/6+o(1)); only its statement
was inspected. An abstract Steiner extremizer cannot simply be substituted for
that real construction.

For E0669 take k at least two, so the line counts are finite. The cap on
collinearity is absent. Pair counting gives
$$
 F_k(n)\leq \frac{\binom n2}{\binom k2},
$$
and the inspected rich-line incidence theorem gives the scale O(n squared/k
cubed+n/k). Neither determines the requested normalized limits. Within a single
configuration the exactly-k count is the difference between its at-least-k and
at-least-(k+1) counts; the maxima of those counts may occur in different
configurations, so subtracting their separate extremal values is invalid.

Next discriminating tests: E0101/E0588 need positive quadratic density with a
fixed real collinearity cap, or a theorem excluding it; E0102 needs that
exclusion for every fixed cap; E0589 needs coordinates realizing the proposed
hypergraph without four collinear; E0669 needs an extension inequality for the
extremal counts themselves that controls accidental lines. Stop abstract-design,
growing-cap and subtraction-of-maxima shortcuts.

## Source interfaces

These source locators identify the uses in this account. Statement and account
reading do not certify a source proof; proof reading here is author inspection
and confers no independent standing.

- [[../library/discrete_geometry/balogh_2018_number_points_general_position_plane/_index|balogh
  2018 number points general position plane]]: Section 2.1, Theorem 2.1
  (statement reading).
- [[../library/discrete_geometry/currier_2025_more_pointsets_many_rich_lines/_index|currier
  2025 more pointsets many rich lines]]: Section 1, Theorem 1.1 rich-line bound;
  Theorem 1.3 examples (statement reading). Section 1, Theorems 1.1-1.3 and
  definition of nice basis (statement reading).
- [[../library/discrete_geometry/furedi_1991_maximal_independent_subsets_steiner_systems_planar_sets/_index|furedi
  1991 maximal independent subsets steiner systems planar sets]]: Theorem 1.1;
  inequality (2.2); Section 2.1 proof of the planar lower bound; Section 3
  realization discussion (proof reading).
- [[../library/discrete_geometry/solymosi_2013_many_collinear_k_tuples/_index|solymosi
  2013 many collinear k tuples]]: Section 1.1, Theorem 1; Section 1.2 projection
  construction (statement reading). Section 1.1, Theorem 1; Section 1.2
  projection mechanism (statement reading). Statement and scope (account
  reading).

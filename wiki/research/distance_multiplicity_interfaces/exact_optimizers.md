---
name: research/distance_multiplicity_interfaces/exact_optimizers
title: "Exact optimizers and local geometric obstructions"
desc: "Near-optimal perturbations do not control exact minimizers; local rigidity and finite classifications have precisely limited domains."
created: 2026-10-14T15:30:27Z
updated: 2026-10-17T22:11:11Z
---

***

The deductions and obstructions here are author-recorded by Plasma AI.
Source-dependent conclusions retain the named premises and reading limits. No
independent review, novelty claim or complete solution of the linked problems
follows from this account.

The relevant questions are [[problems/distance_problems/E0091/_index|E0091]],
[[problems/distance_problems/E0099/_index|E0099]],
[[problems/distance_problems/E0103/_index|E0103]],
[[problems/distance_problems/E0217/_index|E0217]],
[[problems/distance_problems/E0982/_index|E0982]],
[[problems/distance_problems/E1082/_index|E1082]].

## Exact optimizers and finite geometric obstructions

## E0091: one finite nonuniqueness example is not eventual nonuniqueness

A regular hexagon has three lengths. A regular pentagon together with its center
also has three: its side, diagonal and circumradius. The inspected few-distance
statement $g(2)=5$ excludes a two-distance set of six points. Both examples
therefore minimize the global count at six points. Their convex hulls have six
and five vertices, so they are not similar. Kovács's inspected six-point theorem
concerns sets in which every triangle is isosceles; a regular hexagon has
scalene triples. Thus its uniqueness classification does not classify every
distance minimizer. A construction extending this pair to all sufficiently large
orders while preserving minimality is still missing. The $g(2)$ source statement
was inspected in Shinohara's introduction; its classification proof was not
rechecked.

## E0099: there is no positive gap to triangle-free near-optimizers

Fix $n\ge3$, and let an optimal normalized packing have minimum distance one and
diameter $D_n$. In the space of labeled planar coordinates, pair coincidences
and equality between two different unordered pair lengths are proper polynomial
zero sets. Their finite union has empty interior. Hence configurations with all
pair lengths distinct approximate the optimizer arbitrarily closely. Minimum
distance and diameter are continuous. Rescale each approximation by its positive
minimum distance; the resulting minimum is exactly one, its diameter converges
to $D_n$, and exactly one pair has length one. In particular there is no unit
equilateral triangle. Therefore
$$
 \inf\{\operatorname{diam}P:\min|p-q|=1,
                 \ P\text{ has no unit triangle}\}=D_n.
$$
This does not produce a triangle-free exact optimizer. It rules out a uniform
positive diameter gap or an asymptotic density argument as a sufficient
substitute for an exact contact argument.

One possible exact sufficient condition is more than $2n-4$ contacts in every
optimizer. The straight-line contact graph of a minimum-one packing is planar:
two crossing unit segments would have two endpoints at distance less than one,
by the triangle inequality applied through their crossing (equality would force
collinearity). A triangle-free planar graph has at most $2n-4$ edges. No lower
bound of this strength for every diameter optimizer was obtained. The
[Bezdek--Fodor publisher
abstract](https://www.sciencedirect.com/science/article/pii/S0097316598928898)
was inspected for its exact order-eight result, not a general theorem or its
full proof.

## E0103: a sufficient flex criterion has two active constraints

Suppose an exact minimum-diameter packing contains a point $p$ with
$1<|p-q|<D_n$ for every other point $q$. Its finitely many strict inequalities
persist under small motions of $p$. Both the minimum one and maximum $D_n$ are
realized by pairs among the fixed other points. Therefore a small open disk of
positions of $p$ consists of exact optimizers. There are continuum many
congruence classes: an isometry taking one of these finite sets to another has
only finitely many choices on two fixed distinct points and on their images, and
hence only finitely many choices in each class. The strict-slack hypothesis is
not known for an optimizer. A flexible contact graph by itself is insufficient,
because moving along the flex may increase an active diameter. The concrete next
test is a simultaneous contact-and-diameter constraint calculation on an exact
optimizer.

## E0217: a local obstruction for one nine-point partition

The exact point list, distance spectrum and Jacobian computation are retained in
[[theory/discrete_geometry/L30_nine_point_distance_rigidity/_index|L30]]. The
determinant $-1102248$ isolates this realization modulo similarities. Separated
neighborhoods of its eight lengths then show that every sufficiently close
eight-distance configuration preserves the same partition. Its forbidden
collinearity and circles cannot be removed by a small perturbation. A different
partition or a remote component of the realization space remains possible; no
global order-nine exclusion or enumeration is claimed.

## E0982 and E1082: global and pinned targets separate at order eight

For E0982, Dumitrescu's explicit bound at eight vertices is
$\lceil(13\cdot8-6)/36\rceil=3$, below the requested four. Altman's planar bound
forces at least four global distances. If there are exactly four, Shinohara's
inspected Lemma 2.2(a)(ii), specialized to $k=4$, says the convex eight-point
set is a regular octagon or a regular nonagon with one vertex removed. In the
octagon every pin sees four lengths. In the nonagon each length occurs twice
about each pin; deleting one point leaves at least one occurrence of every
length. Thus a counterexample with all pinned counts at most three would have at
least five global lengths. This narrows a finite realization test; it does not
carry out that test. The convex classification is an external statement premise,
not a newly checked proof.

For E1082, the inspected facts $g(2)=5,g(3)=7,g(4)=9$, together with the
elementary maximum of three equidistant planar points, prove $D\ge\lfloor
n/2\rfloor$ for every $n\le11$, without even using no-three-collinearity. They
supply no all-order conclusion.

The pinned counterexample $H_8$ can be checked directly. Put $h=1+\sqrt3$, take
square vertices $(\pm1,\pm1)$ and apexes $(0,\pm h),(\pm h,0)$. Its four global
lengths are
$$
 2,\quad2\sqrt2,\quad\sqrt2h=\sqrt2+\sqrt6,\quad2h.
$$
A square vertex sees the first three; an apex sees the first, third and fourth.
There are no three collinear: a line through two square vertices is one of
$x=\pm1,y=\pm1,y=\pm x$, containing no apex; a line through two apexes is one of
$x=0,y=0,x\pm y=\pm h$, containing no square vertex. Each set of four alone has
no collinear triple. The square vertices satisfy $|x|+|y|=2<h$, so all lie
strictly inside the apex diamond. Hence $H_8$ refutes the pinned version, meets
the global lower bound, and is not a convex-polygon example for E0982.

The [[research/leads/concentric_polygon_census/_index|exact concentric and
affine polygon census]] uses $H_8$ as a convexity-filter control. It finds no
strictly convex counterexample among half-step concentric regular $m$-gons for
$3\le m\le32$, over all positive radii, or the specified diagonal stretches
of regular $n$-gons for $8\le n\le24$, over all positive stretch parameters.
Every critical parameter is enumerated in exact cyclotomic arithmetic, and
the generic complement is covered symbolically. The exclusion is
author-recorded and bounded to those families and order ranges.

## Source interfaces

These source locators identify the uses in this account. Statement and account
reading do not certify a source proof; proof reading here is author inspection
and confers no independent standing.

- [[../library/distance_problems/dumitrescu_2006_distinct_distances_vertex_convex_polygon/_index|dumitrescu
  2006 distinct distances vertex convex polygon]]: Theorem 2 statement (account
  reading).
- [[../library/distance_problems/kovacs_2024_note_erdos_s_mysterious_remark/_index|kovacs
  2024 note erdos s mysterious remark]]: Abstract; Sections 1-2 (statement
  reading).
- [[../library/distance_problems/shinohara_2008_uniqueness_maximum_planar_five_distance_sets/_index|Shinohara:
  Uniqueness of maximum planar five-distance sets]]: Section 1, g(2), g(3),
  Theorem 1.1(a) (statement reading). Section 1, g(2)=5 and similarity
  convention (statement reading). Section 2, Lemma 2.2(a)(ii), M_(2k)(k) for
  k>=4 (statement reading).

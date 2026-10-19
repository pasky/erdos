---
name: research/distance_multiplicity_interfaces/integral_realizations
title: "Finite integral blocks and infinite distance graphs"
desc: "Generic placement composes finite integral blocks, while rational density and height bounds leave distinct uniformity obligations."
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

***

The deductions and obstructions here are author-recorded by Plasma AI.
Source-dependent conclusions retain the named premises and reading limits. No
independent review, novelty claim or complete solution of the linked problems
follows from this account.

The relevant questions are [[problems/distance_problems/E0130/_index|E0130]],
[[problems/distance_problems/E0212/_index|E0212]],
[[problems/distance_problems/E0213/_index|E0213]].

## Rational and integral realizations

## E0130 and E0213: finite blocks and one infinite graph

The following equivalence needs no compactness assumption about coordinate
height:

1. There are arbitrarily large finite integral-distance sets with no three
   collinear and no four cocircular.
2. One countable planar set in that general position has an integer-distance
   graph with unbounded finite clique sizes.

The reverse implication takes finite cliques and their subsets. For the forward
implication, choose integral blocks of sizes tending to infinity and place them
one at a time by rigid motions. At each finite stage first rotate the next block
so none of its segment directions is parallel to an old segment. Choose its
translation outside the following bad sets: point coincidences, mixed collinear
triples, mixed cocircular quadruples, and cross-block distances equal to any
nonnegative integer.

The first, second and fourth types are points, lines or circles. Every mixed
circle condition is a proper polynomial condition in translation. For three old
points and one new point, or the reverse, it is a translated circle condition.
For two old and two new points, translate the new segment onto a line through
one old endpoint, with three distinct points on that line; the other old
endpoint is off it by the chosen nonparallel directions. Those four points are
not concyclic, proving the polynomial is not identically zero. The mixed
collinearity polynomials are likewise proper. The countable union of these
closed nowhere-dense algebraic sets cannot fill the plane (or any open region),
so a permitted translation exists. This completes the induction.

The resulting integer-distance graph is a disjoint union of finite cliques with
unbounded sizes, and contains no infinite complete subgraph. This distinction
matters: unbounded clique number is the supremum of finite clique sizes, not the
existence of an infinite clique. The held pending infinite-chromatic
constructions do not supply these finite integral blocks. The equivalence is a
completed author argument; neither side has been established unconditionally.
Separately, every planar integer-distance graph has a countable proper coloring:
partition the plane into half-open squares of side one half and give each square
its own color. Its diameter is less than one, so no two points of the square are
at a positive integer distance. This upper bound does not give a finite bound on
the chromatic number.

## E0212: density implies finite blocks, not a common denominator

If an everywhere dense rational-distance set exists, choose any finite number of
points greedily. At each stage avoid the finitely many lines through two earlier
points and circles through three earlier noncollinear points. Their complement
contains a nonempty open set, so density supplies the next point. The chosen set
is in general position. Clear its finitely many distance denominators to get an
integral-distance set of the same size. This proves E0212 positive would imply
E0213 positive.

The common denominator is finite-set dependent. Applying this procedure to an
infinite set and asserting one finite scaling would be invalid; even rational
numbers on a line need not have bounded denominators. Solymosi--de Zeeuw Theorem
2.1 permits infinitely many rational-set points on an algebraic curve only if
there is a line or circle component. Theorem 2.2 makes all but at most four or
three points lie on such a line or circle if its intersection is infinite. A
dense set cannot have that form. Decomposing a curve into finitely many
components therefore shows that a hypothetical dense rational set meets every
real algebraic curve only finitely often. Topological density does not imply an
infinite intersection with a closed curve, so there is no contradiction. The
primary statements were read; the Faltings-based proof was not rechecked.

## E0213: the held bound is a height obstruction

Greenfeld--Iliopoulou--Peluse Corollary 1.3 gives, for an integral
general-position set in $[-N,N]^2$, a bound $n\le C(\log N)^A$ with fixed
constants. Hence
$$
 N\ge\exp\bigl((n/C)^{1/A}\bigr).
$$
It does not bound $n$ when the diameter is unrestricted. Translation can put a
finite configuration inside such a box, but cannot make $N$ uniform in its
cardinality. The next discriminating construction remains an eight-point
general-position rational or integral set, or a genuine size-only obstruction.
The seven-point example is inherited from the exact problem account and was not
rerun. The source introduction, Theorem 1.1, Remark 1.2 and Corollary 1.3 were
inspected; not the complete number-theoretic proof.

## Source interfaces

These source locators identify the uses in this account. Statement and account
reading do not certify a source proof; proof reading here is author inspection
and confers no independent standing.

- [[../library/distance_problems/greenfeld_2024_integer_distance_sets/_index|greenfeld
  2024 integer distance sets]]: Introduction; Theorem 1.1; Corollary 1.3
  (statement reading). Theorem 1.1; Remark 1.2, bounded-height qualification
  (statement reading).
- [[../library/distance_problems/solymosi_2010_question_erdos_ulam/_index|solymosi
  2010 question erdos ulam]]: Section 2, Theorems 2.1 and 2.2 (statement
  reading).

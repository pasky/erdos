---
name: research/erdos_836
title: Vertex counts and intersections in 3-chromatic hypergraphs
desc: |
  Independently reviewed arguments give exponentially many incident
  vertices and a linear maximum edge intersection under the exact
  chromatic-number condition, with separate grades and exact subjects.
created: 2026-10-14T15:03:48Z
updated: 2026-10-18T10:11:03Z
---

# Vertex counts and intersections in 3-chromatic hypergraphs

[[research/_index|..]]

[[research/erdos_836/evidence/_index|evidence/]]: Exact mathematical extracts, independent reports and separate grades
for the vertex-count and linear-intersection arguments. Both warrants
are noncomputational.

***

For every integer $r\ge2$, an intersecting $r$-uniform hypergraph with no
proper $2$-coloring has two distinct edges meeting in at least
$\lfloor r/2\rfloor$ vertices. The result includes infinite hypergraphs
in ordinary classical set theory with choice, and implies the uniform
bound $r/3$. It answers the second question of
[[problems/graph_coloring/E0836/_index|Problem 836]] with chromatic number
exactly $3$.

The
[[research/erdos_836/evidence/verify/linear_intersection/_index|independently examined argument and separate grade]]
retain the complete compactness, recoloring and counting derivations.
They also retain a two-edge family showing that mere proper
$3$-colorability does not imply a uniform linear intersection bound.
The mathematical result is credited on
[[problems/graph_coloring/E0836/claims/2026_04_27_price|Price's claim page]];
the reconstruction and independent examination are Plasma AI's work.

The first question has a separate
[[research/erdos_836/evidence/verify/vertex_count/_index|independent examination and passing grade]].
For every integer $r\ge2$, the Erdős–Lovász construction is finite,
intersecting, $r$-uniform and exactly $3$-chromatic, has no isolated
vertices, and has $2r-2+\tfrac12\binom{2r-2}{r-1}$ vertices. Dividing
by $r^2$ tends to infinity, so no uniform quadratic bound holds. Its
[[problems/graph_coloring/E0836/claims/1975_01_01_erdos_lovasz|pending source claim]]
retains the historical attribution and review scope.

The first construction supplies finite counterexamples, sufficient for the
negative answer even when arbitrary hypergraphs are allowed. The second
argument applies to arbitrary non-2-colorable hypergraphs using classical
choice. Thus the two reviewed statements cover both modified questions
with the same nonmonochromatic-edge coloring convention. The stronger
second statement needs no exact-3 upper bound. Each review retains its own
independence limits and excludes fidelity to an external source document
and all external Lean artifacts.

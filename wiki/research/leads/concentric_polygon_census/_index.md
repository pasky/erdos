---
name: research/leads/concentric_polygon_census
title: Exact census of symmetric convex polygons
desc: |
  Closed (refuted): No counterexample to Problem 982 occurs among half-step
  concentric regular polygons for 3 <= m <= 32 or the specified diagonal
  stretches of regular polygons for 8 <= n <= 24, by an author-recorded
  exact critical-parameter census over each full positive parameter domain.
problems: [982]
research_state: closed
review_status: unreviewed
created: 2026-10-16T13:41:30Z
updated: 2026-10-16T13:41:30Z
---

# Exact census of symmetric convex polygons

[[research/leads/_index|..]]

[[research/leads/concentric_polygon_census/census|census]]: Complete positive critical-parameter counts for half-step concentric
polygons of orders 3 through 32 and diagonal stretches of regular polygons
of orders 8 through 24, with strict convexity and every vertex checked.

[[research/leads/concentric_polygon_census/evidence/_index|evidence/]]: Re-runnable cyclotomic enumeration of all critical parameters in two
bounded symmetric polygon families, with exact event data, every-vertex
distance checks and strict convexity controls.

[[research/leads/concentric_polygon_census/sketch|sketch]]: Exact definitions, complete exceptional-parameter equations, convexity
tests and remaining obligations for two bounded symmetric-family searches
for a counterexample to Problem 982.

***

The bounded counterexample search is exhausted without a witness. The target
was a strictly convex counterexample to
[[problems/distance_problems/E0982/_index|Problem 982]]: every vertex of an
$n$-gon would have fewer than $\lfloor n/2\rfloor$ distances to the other
vertices. The [canonical sketch](sketch.md) gives the two families, continuous
parameter domains, finite order ranges, and completeness argument. The
[exact census](census.md) records the result at every order, and the
[evidence instructions](evidence/_index.md) describe its re-runnable checker
and exact event data. These are author-recorded by Plasma AI, without
independent review.

There are 4,438 distinct positive critical radii across $3\le m\le32$ and
5,682 distinct positive critical stretch parameters across $8\le n\le24$.
Every concentric order has precisely two strictly convex critical radii,
giving orbit counts $(m-1,m)$ and $(m,m-1)$. No admissible parameter makes
every vertex fall below the required threshold. The closure concerns exactly
these bounded families. Unbounded orders, other offsets, further radial
orbits and other affine maps remain outside the result.

The
[[research/distance_multiplicity_interfaces/exact_optimizers|local geometric
obstructions account]] supplies the nonconvex eight-point example used to
check the convexity filter. Its source-dependent convex classifications are
not premises of this enumeration. The problem page carries the status and
literature assessment; the census does not resolve the unrestricted problem.

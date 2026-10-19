---
name: research/dissociated_covering_attack
title: Dissociated covering attack
desc: "A sustained attack on Problem 774: uniform extraction for repeated power-of-two simplexes at their critical scale, an exact finite fractional covering gap, and the remaining arbitrary-color and odd-root rigidity questions."
tags: [E0774]
sources: []
created: 2026-10-15T17:59:57Z
updated: 2026-10-15T23:24:37Z
---

# Dissociated covering attack

[[research/_index|..]]

[[research/dissociated_covering_attack/evidence/_index|evidence/]]: Exact arithmetic checks the relations and proper 2-colorings of the 15th roots of unity, a nine-layer two-color certificate, the root spans of arc classes below the rank threshold, signed-pair and signed-triple survival under coordinate twists, the failure of two arcs at 165 and 195, the diverging first moment, and exhaustive survival sets at 105 for arc and layered classes.

[[research/dissociated_covering_attack/fractional_covering|fractional_covering]]: Bourgain's weighted extraction theorem bounds fractional dissociated covering by an absolute multiple of the reciprocal hereditary extraction constant, without symmetry; the remaining problem is an integral covering gap.

[[research/dissociated_covering_attack/layer_race|layer_race]]: Coordinate-permutation twists of a proper coloring give layered colorings of the next odd-root grid; robust layering preserves the root-span fraction exactly and three colors win the layer-count race of the roots, but the exact first moment of common values diverges along the odd-prime grids, so deciding the odd-root grids this way needs a rigidity argument for common values of large complexity.

[[research/dissociated_covering_attack/proof_sketch|proof_sketch]]: Editable argument for Problem 774: repeated power-of-two simplexes have uniform hereditary extraction at a precise critical scale, fractional covering is uniformly bounded for every candidate family, and a thirteen-point example crosses the fractional threshold two; arbitrary-color growth remains open, alongside the odd-root rigidity route.

[[research/dissociated_covering_attack/repeated_simplex|repeated_simplex]]: Boolean compression proves semistability and uniform hereditary extraction for repeated power-of-two simplexes at k = q(log log q + log log log q + O(1)); entropy excludes larger scales, and flat trades defeat scalar linear fibers, bounded Boolean linear palettes, and every quadratic two-coloring.

***

This folder holds a sustained attack on
[[problems/integer_sequences/E0774/_index|Problem 774, which asks whether every proportionately dissociated set of positive integers is a finite union of dissociated sets]].
It builds on the inherited research in
[the E0774 research folder](../erdos_774/_index.md), whose main argument
reduces a negative answer to unbounded dissociated coloring of uniformly
extracting finite configurations, in particular of the odd-prime grids
$S_3\otimes S_5\otimes\cdots$.

The [proof sketch](proof_sketch.md) states the finite target, exact
interfaces, and remaining gaps. The
[repeated-simplex argument](repeated_simplex.md) proves semistability and
one hereditary extraction constant in
[[theory/integer_sequences/L271_repeated_simplex_extraction/_index|L271, tier 0]],
for a new family with common side
$q=2^b$ and about $q(\log\log q+\log\log\log q+c)$ factors, for one
fixed $c$. It also excludes larger parameter scales by entropy and
constructs flat relations in every scalar linear fiber once the number
of factors reaches $q$
([[theory/integer_sequences/L269_simplex_affine_fiber_threshold/_index|L269, tier 0]]).
Boolean linear fibers of bounded codimension and quadratic two-colorings
also fail in their stated ranges. Unbounded coloring under arbitrary
palettes remains open.

The [fractional-covering formulation](fractional_covering.md) shows that
every counterexample family must have an integral covering gap, even
without symmetry. The exact finite claim
[[theory/integer_sequences/L211_fractional_half_cover_obstruction/_index|L211]]
has fractional covering number $37/19<2$ and needs three dissociated
classes. It is a finite obstruction, not an amplification.

[The twisted-layer note](layer_race.md) retains the odd-root alternative:
robust layering preserves the root-span fraction, but a first moment over
all common values diverges, leaving a rigidity problem. Its
[evidence](evidence/_index.md) checks the finite cases. None of these
arguments resolves Problem 774 or asserts an independent tier for the
new work.

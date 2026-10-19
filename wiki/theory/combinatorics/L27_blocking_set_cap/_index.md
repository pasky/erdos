---
name: theory/combinatorics/L27_blocking_set_cap
title: A lower bound on a universal blocking-set cap
desc: Incidence moments exclude blocking sets with at most three points per line in every projective plane of order at least five.
id: L27
statement: |
  If a projective plane of order q has a set of s points meeting every line
  in between 1 and C points, where C is a positive integer, then
  s^2-(C(q+1)+1)s+C(q^2+q+1)<=0. For q>=5 no such set exists with C<=3.
  Consequently any real constant bounding all line intersections of a
  blocking set in every finite projective plane must be at least 4.
status: proved
tier: 0
depends_on: []
created: 2026-10-14T12:38:34Z
updated: 2026-10-14T12:38:34Z
---

# A lower bound on a universal blocking-set cap

[[theory/combinatorics/_index|..]]

[[theory/combinatorics/L27_blocking_set_cap/_proof|_proof]]: Counting incidences and ordered pairs gives a quadratic obstruction to a blocking set with a prescribed maximum line intersection.

***

The [proof](_proof.md) counts point-line incidences and ordered point pairs.
It is a complete author-recorded argument by Plasma AI, at tier 0, without
independent review or Lean proof. No computation or other native claim is
used, and no novelty claim is made.

This is a necessary condition for
[[problems/set_systems/E1159/_index|Problem 1159]], not an upper bound or
a construction at cap four. At that cap it only confines the size to

$$
\frac{4q+5-\sqrt{24q+9}}2\le s\le
\frac{4q+5+\sqrt{24q+9}}2.
$$

The stated claim has no remaining mathematical gap. The catalog question
still asks whether some absolute cap suffices in all finite planes.

---
name: problems/distance_problems/E0605
title: Problem 605
desc: |
  Asks whether $n$ points on a sphere can have at least $f(n)n$ pairs at the
  same distance, for some $f(n)\to\infty$.
tags:
- Geometry
- Distances
status: solved
claim: proved
created: 2026-09-04T09:17:27Z
updated: 2026-10-18T22:19:33Z
---

# Problem 605

[[problems/distance_problems/_index|..]]

[[problems/distance_problems/E0605/claims/_index|claims/]]: The 2 claim pages of Problem 605, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Is there some function $f(n)\to \infty$ as $n\to\infty$ such that
there exist $n$ distinct points on the surface of a two-dimensional sphere with
at least $f(n)n$ many pairs of points whose distances are the same?

**Status.** Proved. Erdős, Hickerson and Pach [EHP89] show that for every $n$
and every distance strictly between $0$ and $2$, some $n$ points on the unit
sphere have at least $c\,n\log^* n$ pairs at that distance, so $f(n)=c\log^* n$
answers the question; this is the accepted full claim on
[[problems/distance_problems/E0605/claims/1989_08_01_erdos_hickerson_pach|its
claim page]]. Swanepoel and Valtr [SwVa04] give more than $c\,n\sqrt{\log n}$
unit distances among $n$ points on every sphere of diameter above $1$, a second
proof with a stronger bound, recorded as an accepted full claim on
[[problems/distance_problems/E0605/claims/2004_01_01_swanepoel_valtr|its claim
page]].

**Source.** [erdosproblems.com/605](https://www.erdosproblems.com/605), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #605,
https://www.erdosproblems.com/605.

**References.**

- [EHP89] Erdős, Paul and Hickerson, Dean and Pach, János, A problem of Leo
  Moser about repeated distances on the sphere. Amer. Math. Monthly (1989),
  569-575.
- [SwVa04] Swanepoel, Konrad J. and Valtr, Pavel, The unit distance problem on
  spheres. (2004), 273-279.

**Formalization.** None recorded.

## Progress

Not yet compiled.

## Known Results

Not yet compiled.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/distance_problems/erdos_1989_problem_leo_moser_about_repeated_distances/_index|erdos_1989_problem_leo_moser_about_repeated_distances]]
- [[../library/distance_problems/erdos_1989_problem_leo_moser_about_repeated_distances/theorem_2|erdos_1989_problem_leo_moser_about_repeated_distances / theorem_2]]
- [[../library/distance_problems/swanepoel_2004_unit_distance_problem_spheres/_index|swanepoel_2004_unit_distance_problem_spheres]]
- [[../library/distance_problems/swanepoel_2004_unit_distance_problem_spheres/theorem_1|swanepoel_2004_unit_distance_problem_spheres / theorem_1]]

<!-- END problem library links -->

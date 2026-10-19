---
name: discrete_geometry/plasma_ai_2026_monochromatic_triangles_two_colorings_plane/main_theorem
title: "Main theorem: every two-coloring of the plane misses at most one triangle"
desc: |
  In every two-coloring of the plane every non-equilateral triangle, degenerate
  or not, has a monochromatic congruent copy and at most one equilateral side
  length is missed, so any two triangles without a monochromatic copy are
  congruent; its Lean formalization is rebuilt and kernel-replayed here.
created: 2026-10-18T02:18:16Z
updated: 2026-10-18T02:18:16Z
---

***

## Statement

Let $c:\mathbb R^2\to\{0,1\}$ be any function, with no measurability or other
regularity assumed. A *triangle* is a triple of distinct points, nondegenerate
when they are affinely independent and degenerate when they are collinear, and
a *monochromatic copy* of a triangle $T$ is a triple congruent to $T$,
reflections and relabellings allowed, whose three points have one color.

**Main theorem.**

1. If $r,s>0$ and $c$ has no monochromatic equilateral triangle of side $r$
   and none of side $s$, then $r=s$.
2. Every triangle without a monochromatic copy is equilateral; in particular
   every degenerate triangle has a monochromatic copy.
3. Hence any two triangles without a monochromatic copy are congruent: for all
   but at most one triangle $T$, up to congruence, there is a monochromatic
   copy of $T$, which answers
   [[../wiki/problems/discrete_geometry/E0173/_index|Problem 173]] whether or
   not degenerate triangles count.
4. Every right triangle has a monochromatic copy, the theorem of
   [[discrete_geometry/shader_1976_all_right_triangles_are_ramsey_e2/_index|Shader]].
5. The exception occurs: coloring by the parity of $\lfloor y/(\sqrt3/2)\rfloor$
   gives no monochromatic equilateral triangle of side $1$.

Comparator checks parts 2 to 5, as the statements of the repository's
`Challenge.lean`. Parts 3, 4 and 5 are the formal-conjectures statements
`Erdos173.erdos_173`, `Erdos173.erdos_173.variants.right_triangle` and
`Erdos173.erdos_173.variants.equilateral_exception`, whose triangles are
nondegenerate. Part 2 is `Erdos173.erdos_173.variants.non_equilateral` for
nondegenerate triangles and `Erdos173.erdos_173.variants.three_distinct_points`
for every triangle, degenerate ones included; with it, part 3 extends to
degenerate triangles, since a degenerate triangle is never equilateral. Part 1
follows from part 3, since equilateral triangles of different sides are not
congruent; it is the development's `two_scale`, on colorings of $\mathbb C$,
which the proofs of parts 2 and 3 use.

## Proof

The blueprint `blueprint/proof.md` of the
[[discrete_geometry/plasma_ai_2026_monochromatic_triangles_two_colorings_plane/_index|source card]]
proves the theorem in prose, following the Lean development; the card's digest
outlines the route. Part 2 follows from part 1 by Lemma 1.3 of
[[discrete_geometry/jelinek_2009_monochromatic_triangles_two_colored_plane/corollary_1_4|Jelínek, Kynčl, Stolař and Valla]]:
a triangle without a monochromatic copy, degenerate or not, has each of its
side lengths avoided as an equilateral side, so its three sides are equal. Part
1 is the two-scale theorem, proved by rescaling to sides $1$ and $x\ne1$ and
then excluding $x$ outside $(2/3,3/2)$ by a Bessel bound on a radial spectral
measure, and inside by the binary transfer to a measurable coloring and a
circle argument.

**Depends on.** OpenAI's spectral rigidity theorem, from
[[discrete_geometry/openai_2026_euclidean_plane_not_five_colorable/_index|*The Euclidean plane is not five-colorable*]],
in its Lean form, generalized over the carrier field and proved there for each
carrier the theorem uses; Lemma 1.3 of Jelínek et al. is formalized in
coordinates.

**Read depth.** Claims checked: the statements of `Challenge.lean` were read
clause by clause, its three formal-conjectures statements against
formal-conjectures' `FormalConjectures/ErdosProblems/173.lean` at its commit of
2026-10-14, and parts 1 and 2 in the development's `TwoScale.lean` and
`FinalAssembly.lean`. The proofs were not read here; the formalization was
rebuilt, checked with Comparator and replayed in the kernel, as the card's
`evidence/` records.

## Bears on

- [[../wiki/problems/discrete_geometry/E0173/_index|Problem 173]]: settles the
  Statement whether or not three distinct collinear points count as a
  triangle, with the one equilateral exception, on
  [[../wiki/problems/discrete_geometry/E0173/claims/2026_10_19_plasma_ai|its claim page]].

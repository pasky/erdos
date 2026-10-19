---
name: discrete_geometry/plasma_ai_2026_monochromatic_triangles_two_colorings_plane
desc: |
  Plasma AI's 2026 blueprint and Lean formalization proving that every
  two-coloring of the plane has a monochromatic congruent copy of every
  triangle, collinear triples of distinct points included, except at most one,
  which is then equilateral, answering Problem 173; the step from arbitrary to
  measurable colorings extends the spectral rigidity theorem of OpenAI's
  plane-coloring manuscript from the algebraic numbers to the algebraic closure
  of $\mathbb Q(x)$ for every real $x$.
license: Apache-2.0
created: 2026-10-18T02:18:16Z
updated: 2026-10-19T03:51:30Z
---

# discrete_geometry/plasma_ai_2026_monochromatic_triangles_two_colorings_plane

[[discrete_geometry/_index|..]]

[[discrete_geometry/plasma_ai_2026_monochromatic_triangles_two_colorings_plane/evidence/_index|evidence/]]: The held repository of Plasma AI's Problem 173 blueprint and Lean
formalization at its pinned commit, and this corpus's verification records
of the formalization.

[[discrete_geometry/plasma_ai_2026_monochromatic_triangles_two_colorings_plane/main_theorem|main_theorem]]: In every two-coloring of the plane every non-equilateral triangle, degenerate
or not, has a monochromatic congruent copy and at most one equilateral side
length is missed, so any two triangles without a monochromatic copy are
congruent; its Lean formalization is rebuilt and kernel-replayed here.

***

Plasma AI, *Monochromatic triangles in two-colorings of the plane*,
blueprint with Lean formalization, October 2026, in the repository
[plasma-ai/erdos-173](https://github.com/plasma-ai/erdos-173) at commit
[4a368a6](https://github.com/plasma-ai/erdos-173/tree/4a368a652753fab53272f7a747755876f04bc2cc)
(2026-10-19 UTC). The blueprint is `blueprint/proof.md` there. The repository
is released under the Apache License 2.0, read in its root `LICENSE` at that
commit on 2026-10-19, whose copyright line is left as the license's template
placeholder; the blueprint carries no license or copyright statement of its
own and is held under the repository's license. The whole repository,
blueprint included, is held as
[evidence/assets/erdos_173_formalization.tar.gz](evidence/assets/erdos_173_formalization.tar.gz),
made by `git archive 4a368a6 | gzip -n`.

```bibtex
@misc{PlasmaAI:Erdos173,
  author = {{Plasma AI}},
  title = {{Monochromatic triangles in two-colorings of the plane}},
  howpublished = {Blueprint with Lean formalization,
                  \url{https://github.com/plasma-ai/erdos-173}},
  year = {2026}
}
```

The result is credited to Plasma AI, as the README and the blueprint state.
The repository's `formalization.yaml` names Jacob Parish as the
formalization's author, Jacob Parish and Andrew Turner as its responsible
maintainers, and records that it was written with Claude Code (model
`claude-opus-5-5`), its components developed by parallel agents against fixed
intermediate statements.

**The result.**
[[discrete_geometry/plasma_ai_2026_monochromatic_triangles_two_colorings_plane/main_theorem|The main theorem]]:
in every two-coloring of the plane, with no measurability or other regularity
assumed, every non-equilateral triangle, collinear triples of distinct points
included, has a monochromatic congruent copy, and the coloring misses the
monochromatic equilateral triangles of at most one side length. Hence any two
triangles without a monochromatic copy, degenerate or not, are congruent,
which answers
[[../wiki/problems/discrete_geometry/E0173/_index|Problem 173]], and the
exceptional triangle, when there is one, is equilateral. The alternating
half-open strips of width $\sqrt3/2$ show that the exception occurs.

**The argument.** The blueprint follows the Lean development module by module.

- **Reduction.** The eight-point configuration of Lemma 1.3 of
  [[discrete_geometry/jelinek_2009_monochromatic_triangles_two_colored_plane/corollary_1_4|Jelínek, Kynčl, Stolař and Valla]],
  which they take from Erdős, Graham, Montgomery, Rothschild, Spencer and
  Straus, turns a monochromatic equilateral triangle of side $a$ into a
  monochromatic copy of every triangle with a side $a$, collinear triples of
  distinct points included. It remains to show that
  no coloring avoids the equilateral triangles of sides $1$ and $x\ne1$.
- **The carrier.** The coloring is restricted to a countable dense subfield of
  $\mathbb C$ containing $x$: the algebraic numbers for algebraic $x$, the
  algebraic closure of $\mathbb Q(x)$ otherwise. Its labelings without a
  monochromatic equilateral triangle of side $1$ or $x$ carry a probability
  measure invariant under the field's translations and unit rotations.
- **Rigidity.** The spectral rigidity theorem of
  [[discrete_geometry/openai_2026_euclidean_plane_not_five_colorable/_index|OpenAI's plane-coloring manuscript]],
  that a wild rotation-invariant character law is Haar measure, is used in the
  manuscript's own Lean form, generalized from the algebraic numbers to any
  countable, relatively algebraically closed subfield of $\mathbb C$ whose
  unit circle has a *template property*: for every finite set $Q$ of units
  there is a finite set $S$ of units such that, for every choice of $q_s\in Q$
  at each $s\in S$, the products $q_s s$ span $1$ and $i$ over $\mathbb Q$.
  The manuscript's number-field selection gives it for the algebraic numbers.
  For transcendental $x$ the formalization proves it: a finite cover of the
  unit group by translated kernels of a functional linear over the algebraic
  numbers would force rational Cauchy transforms in a finite extension of
  $\overline{\mathbb Q}(T)$, $T=(x+i)/(x-i)$, and then a finite-dimensional
  quotient algebra in which Cayley transforms rule the cover out.
- **Far ratios.** Avoidance makes the sign correlation $-1/3$ at distances $1$
  and $x$, so the radial spectral measure $\nu$ of mass at most one has
  $\int J_0(t)\,d\nu=\int J_0(xt)\,d\nu=-1/3$. For $x\ge3/2$ or $x\le2/3$ this
  contradicts $J_0(t)+J_0(xt)\ge-83/125$.
- **Binary transfer and ratios near one.** The quadratic $1+ab+ac+bc$ involves
  only pair correlations, which the projection onto continuous vectors
  preserves, so thresholding the projected field gives a measurable coloring
  weakly avoiding both sides. For $2/3<x<3/2$ a circle argument excludes it:
  one apex angle of the isosceles triangles with sides in $\{1,x\}$ is an
  irrational multiple of $\pi$, which makes the null boundary of the color
  classes support itself on circles and so empty, while nested squares of red
  proportion one half give it a point.

**The formalization.** Lean 4 at `v4.35.0-rc3` with Mathlib `v4.35.0-rc3`.
`Challenge.lean` states five theorems with deliberate `sorry` bodies.
`HasMonochromaticCopy` and the theorems `Erdos173.erdos_173`,
`Erdos173.erdos_173.variants.right_triangle` and
`Erdos173.erdos_173.variants.equilateral_exception` are copied verbatim, apart
from their attribute lists, from formal-conjectures'
`FormalConjectures/ErdosProblems/173.lean` at its commit of 2026-10-14, with
its `ℝ²` notation declared locally. The other two are the repository's own:
`Erdos173.erdos_173.variants.non_equilateral`, that every non-equilateral
triangle has a monochromatic copy, and
`Erdos173.erdos_173.variants.three_distinct_points`, the same for any three
distinct points that are not the vertices of an equilateral triangle. The
triangles of the first four are Mathlib's `Affine.Triangle`, whose vertices are
affinely independent; `three_distinct_points` takes any three distinct points,
collinear ones included. `Solution.lean` proves the five through the
development `Erdos173/` (34 files) and 36 modules under `OAI/`: 34 from the
`lean/` directory of `openai/math` at revision adc7f1241, under the Apache
License 2.0, ported to Lean `v4.35.0-rc3` and generalized over a carrier
field, and two new modules defining the carrier class and its two instances;
`OAI/README.md` records every change, and each changed file begins with a
comment saying so. `comparator.json` permits only the axioms `propext`,
`Quot.sound` and `Classical.choice`.

Attestation, recorded as the source's own statements and not as this corpus's
review: `formalization.yaml` gives a `sorry` count of zero and the three
standard axioms; it records that Comparator accepts the five theorems, that the
project lead checked the three formal-conjectures statements against the
problem and the other two have not had that check, and that no independent
review of the formalization has been recorded. This corpus's own checks are
under
[[discrete_geometry/plasma_ai_2026_monochromatic_triangles_two_colorings_plane/evidence/_index|evidence/]].

Read status: claims checked for the main theorem, read clause by clause in
`Challenge.lean`, its three formal-conjectures statements against
formal-conjectures' statement at its commit of 2026-10-14, and in the
blueprint's Sections 1 and 2; the proofs were not read here.

## Bears on

- [[../wiki/problems/discrete_geometry/E0173/_index|Problem 173]]: settles the
  Statement whether or not three distinct collinear points count as a
  triangle, with the one equilateral exception, on
  [[../wiki/problems/discrete_geometry/E0173/claims/2026_10_19_plasma_ai|its claim page]].
- [[discrete_geometry/erdos_1975_euclidean_ramsey_theorems_iii/conjecture_3|Conjecture 3 of Euclidean Ramsey Theorems III]]
  and
  [[discrete_geometry/graham_2017_euclidean_ramsey_theory/conjecture_11_1_1|Conjecture 11.1.1 of Graham's survey]]:
  every non-equilateral triangle has a monochromatic copy in every two-coloring
  of the plane. The main theorem proves it, collinear triples of distinct
  points included. The stronger
  [[discrete_geometry/graham_2017_euclidean_ramsey_theory/conjecture_11_1_2|Conjecture 11.1.2]],
  that one color class contains every triangle with at most one equilateral
  exception, is not addressed. This row is an inference drawn on this card.

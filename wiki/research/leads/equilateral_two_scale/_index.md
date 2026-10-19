---
name: research/leads/equilateral_two_scale
title: Two Equilateral Scales in Two-Colorings of the Plane
desc: |
  Closed (resolved): a reviewed proof that every plane two-coloring misses
  at most one triangle congruence class. A function-field unit template
  extends the wild-character rigidity argument to each real scale ratio;
  binary transfer then composes with the measurable two-scale circle
  exclusion. A separate grade accepts the whole-conclusion review, and the
  Plasma AI claim on Problem 173 is accepted on its Lean formalization.
problems:
- 173
research_state: closed
review_status: reviewed
last_reviewed: 2026-10-17
created: 2026-10-16T14:00:00Z
updated: 2026-10-17T08:30:38Z
---

# Two Equilateral Scales in Two-Colorings of the Plane

[[research/leads/_index|..]]

[[research/leads/equilateral_two_scale/binary_transfer|binary_transfer]]: For two colors and three-point configurations the monochromatic indicator
is quadratic, so OpenAI's projection onto continuous vectors preserves
avoidance after thresholding. The algebraic-family version uses the
release's rigidity premise; the two-scale version uses the one-parameter
rigidity extension and applies to every real scale ratio.

[[research/leads/equilateral_two_scale/circle_exclusion|circle_exclusion]]: At a boundary point of a measurable coloring that weakly misses equilateral
sides 1 and x, the density points on a suitable circle must be invariant
under a dense group of rotations while a sixty-degree turn swaps the
colors, unless that circle meets the boundary in positive length, which a
null boundary cannot sustain. With the Bessel bound this excludes every
ratio x != 1 for measurable colorings.

[[research/leads/equilateral_two_scale/evidence/_index|evidence/]]: The whole-conclusion review and separate grade, their exact native
subjects, independent derivations, and rational Bessel check.

[[research/leads/equilateral_two_scale/rigidity_extension|rigidity_extension]]: The function-field unit template replaces the number-field selection in
the wild-character rigidity proof. The other steps use countability,
real closedness and divisibility of the rotation group. This gives the
residual-correlation vanishing required for two-scale binary transfer.

[[research/leads/equilateral_two_scale/spectral_exclusion|spectral_exclusion]]: Avoiding equilateral triangles of side r forces the rotation-averaged pair
correlation -1/3 at distance r. A Bessel bound then excludes sides 1 and x
for x >= 3/2 or x <= 2/3: for measurable colorings outright, and for every
coloring when x is algebraic, granting the Lean rigidity theorem of
OpenAI's plane-coloring release.

[[research/leads/equilateral_two_scale/transcendental_scales|transcendental_scales]]: The algebraic closure of Q(x) is an exact carrier for the two-scale
problem. The smaller algebraic span of 1 and x admits an XOR avoider.
Unit-vector templates, finite witnesses and algebraic-line continuity
describe the transfer interfaces; the function-field finite-cover proof
supplies the template used in the rigidity extension.

[[research/leads/equilateral_two_scale/unit_templates|unit_templates]]: A finite cover of the unit group by translated kernels of a functional
linear over the algebraic numbers would force a finite-dimensional
quotient, where Cayley transforms rule out the cover. This supplies the
unit-vector template for the transcendental rigidity argument.

***

The project mathematics is credited to Plasma AI. The
[[research/leads/equilateral_two_scale/evidence/verify/whole_conclusion/_index|whole-conclusion record]]
retains an independent review and a separate PASS grade accepting
**refutation-failed** for the complete seven-step argument below. The
unused alternative routes retain their stated author standing. The result
is the accepted
[[problems/discrete_geometry/E0173/claims/2026_10_19_plasma_ai|Plasma AI claim]]
on Problem 173, accepted on this corpus's rebuild, Comparator check and kernel
replay of its external Lean formalization and a graded review of the formal
statements, which
[[../library/discrete_geometry/plasma_ai_2026_monochromatic_triangles_two_colorings_plane/_index|its source card]]
records.

## Target

[[problems/discrete_geometry/E0173/_index|Problem 173]] asks whether, in every
two-coloring of the plane, every triangle with at most one exception has a
monochromatic congruent copy. Its problem assessment records the status open,
with three partial claim pages, none bearing on whether one coloring can miss
two triangles. By Lemma 1.3 and Corollary 1.4 of
[[../library/discrete_geometry/jelinek_2009_monochromatic_triangles_two_colored_plane/corollary_1_4|Jelínek, Kynčl, Stolař and Valla]],
which they take from Erdős, Graham, Montgomery, Rothschild, Spencer and
Straus, a coloring that contains a monochromatic equilateral triangle of
side $a$ contains every triangle with a side $a$, and a coloring that
contains a monochromatic triangle with sides $a,b,c$ contains a monochromatic
equilateral triangle of one of those sides. Hence the problem is equivalent
to this two-scale question, the target of the lead: for which $x>0$, $x\ne1$,
does every two-coloring of the plane contain a monochromatic equilateral
triangle of side $1$ or of side $x$? A full solution answers it for every
such $x$, or exhibits a coloring missing two sides. The question is symmetric
under $x\mapsto1/x$, and copies may be taken by translations and rotations
alone, since equilateral triangles are symmetric under reflection.

The compactness argument and the nonuniform witness sizes near $x=1$
([[theory/discrete_geometry/L32_equilateral_witness_size/_index|L32, finite
witnesses must grow as x tends to 1]]) are recorded on
[[research/geometric_configuration_interfaces/colorings|the coloring
certificates account]].

## Proof sketch

**Candidate conclusion.** Every two-coloring of the whole plane contains a
monochromatic congruent copy of every non-equilateral triangle, including
every collinear triple of distinct points, and misses at most one
equilateral side length. Thus it misses at most one triangle congruence
class, which, if present, is equilateral.

The independent whole review and separate grade cover this exact
conclusion, formulation and consumed source extensions. The examined
mathematical argument is unchanged; its frozen excerpts and independent
derivations are retained in the whole-conclusion record. The formal
statements that the Lean formalization proves include collinear triples of
distinct points and allow reflected copies; the claim page states what its
acceptance covers.

1. **Finite forcing.** Lemma 1.3 and Corollary 1.4 of Jelínek et al. reduce
   the question to simultaneous avoidance of equilateral sides $1$ and
   $x\ne1$. The eight-point configuration is reconstructed in coordinates
   on the [[research/leads/equilateral_two_scale/circle_exclusion|circle
   account]], including its orientation-preserving maps and its
   positive-measure version. No picture is needed for this interface.
2. **Carrier.** Given $x>0$, use $L=F_x(i)$, where $F_x$ is the real
   closure of $\mathbb Q(x)$ inside $\mathbb R$, and its unit group $K_x$.
   This is a countable dense carrier containing both equilateral
   triangles. Proposition 3 of the
   [[research/leads/equilateral_two_scale/transcendental_scales|carrier
   account]] also proves its exact equivalence to the whole-plane
   avoidance question by finite compactness and real-closed transfer.
3. **Unit template.** At transcendental $x$, Theorem 1 of the
   [[research/leads/equilateral_two_scale/unit_templates|finite-cover
   account]] rules out a finite cover of $K_x$ by the kernels
   $u\mapsto\lambda(q_j u)$ of an $E$-linear functional with
   $\lambda(1)=1$, where $E$ is the algebraic numbers. It reduces such a
   cover to a finite function field, forces rational Cauchy transforms,
   and factors the functional through a finite-dimensional algebra where
   Cayley transforms contradict the cover. Propositions 6--8 of the
   carrier account turn this into the rational unit-vector template
   required by the rigidity proof. At algebraic $x$, the original
   number-field selection has its stated hypotheses.
4. **Haar rigidity.** Theorem 2 of the
   [[research/leads/equilateral_two_scale/rigidity_extension|rigidity
   extension]] applies the template to the wild-character proof in
   Sections 2 and 3 of the OpenAI plane-coloring manuscript. Its other
   field inputs are countability, density, real closedness and divisibility
   of $K_x$, all discharged there. The source's relative-singularity,
   compact-tower and multiple-average arguments supply the radial
   identities; the template replaces the number-field step. Every wild
   invariant character law on $L$ is therefore Haar, by the reviewed
   argument. This is a prose proof of the needed
   extension, not a promotion of the separate Lean interface (R0).
5. **Binary transfer.** In an invariant law on an avoiding coloring,
   projection of the origin sign onto continuous vectors is conditional
   expectation. Corollary 3 of the rigidity extension preserves every
   nonzero pair correlation. The identity
   $Q(a,b,c)=1+ab+ac+bc\ge0$ on $[-1,1]^3$, with equality only when both
   endpoint signs occur, gives a Borel weakly avoiding coloring by joint
   sampling and thresholding. The
   [[research/leads/equilateral_two_scale/binary_transfer|binary account]]
   supplies this argument; it applies on $L$ to both scales for every
   real $x>0$.
6. **Measurable exclusion.** Theorem 4 of the circle account excludes
   weak measurable avoidance at two unequal scales. A Bessel bound treats
   $x\ge3/2$ and $x\le2/3$. Inside that window a boundary point would
   force alternation under a sixty-degree rotation and invariance under
   an irrational rotation on one of its two circles, unless the circle
   contains a positive-length part of the null boundary. The two-step
   circle map rules out a nonempty null set with that property. Empty
   measure-theoretic boundary makes a color null or conull, contradicting
   avoidance. This argument needs no classification of measurable
   single-scale avoiders.
7. **Whole conclusion.** If an arbitrary coloring missed equilateral
   sides $a<b$, rescale to $1,x=b/a$. Step 5 would give a weak measurable
   avoider, contradicting step 6. Thus at most one equilateral side is
   missed. Step 1 gives every non-equilateral triangle, and hence the
   stated at-most-one-congruence-class conclusion.

The source inputs and project deductions retain their individual reading
and review standing. In particular the source's accepted five-color bounds
do not independently verify any part of this new conclusion.

The following unused alternative concerns the zebra-like class. It would
give the measurable exclusion from a classification of measurable avoiders
as zebra-like colorings, which remains unknown. The candidate proof does
not assume that classification.

**Proposition (two zebra scales).** No measurable coloring agrees almost
everywhere both with a zebra-like coloring at scale $1$ and with one at scale
$x\ne1$. This uses Definition 3.2 of Jelínek et al., including its condition
(d), without assuming polygonality.

*Proof.* Use coordinates in the two unit directions of a zebra-like
coloring at scale $1$, and put $h=\sqrt3/2$. For two points of one boundary
curve with horizontal displacement $s$, $|s|\le1/2$, and vertical
displacement $t$, take the lower point as $A$. Translate the higher point
to the next curve by one of $(1/2,h)$ and $(-1/2,h)$, choosing the sign so
that its horizontal distance from $A$ is $1/2-|s|$. Its vertical distance
from $A$ is $h+|t|$, so the angle with the horizontal is at least $\pi/3$.
Condition (d) makes the distance at most $1$. Therefore

$$
(1/2-|s|)^2+(h+|t|)^2\le1,
\qquad \sqrt3|t|+t^2\le |s|-s^2\le|s|.
$$

In particular no two distinct points on the curve have the same horizontal
coordinate. Its horizontal projection is connected and invariant under
integer translation, hence is all of $\mathbb R$. The displayed bound and
subdivision into horizontal increments at most $1/2$ make the curve the
graph of a $1$-periodic $1/\sqrt3$-Lipschitz function. The neighboring
graphs have vertical separation at least
$h-1/(2\sqrt3)=1/\sqrt3$, and the curves form a locally finite family.
They are null sets. Each point of a curve has both adjacent colors in
positive area in every disk, whereas off the curves there is a
monochromatic neighborhood. Thus their union is the essential boundary,
determined by the coloring up to null sets.

Two zebra-like colorings agreeing almost everywhere consequently have the
same boundary, and its connected components are the same individual
curves. The graph of a bounded periodic function has no translation period
with nonzero vertical component. A common curve, periodic in both zebra directions,
therefore forces those directions to be parallel. Choose common horizontal
and upward directions. A consecutive pair of common curves is obtained by
translation through $(1/2,h)$ in the first description and through
$(x/2,xh)$ in the second; reversing a horizontal direction does not change
the curve, by its horizontal period. The difference of these two
translations is a period of one curve. Its vertical component is
$(x-1)h$, so $x=1$. $\square$

This is an author-recorded implication about the defined zebra-like class,
not a classification of measurable avoiding colorings.

## Limits of the alternative routes

The smallest carrier $E+Ex$ at a transcendental ratio supports an XOR
avoider and violates Haar rigidity. It is a proper carrier and supplies no
whole-plane counterexample. The exact carrier $L$ and its full unit group
are essential to the candidate proof.

The source's number-field selection cannot simply be applied to
transcendental cover rotations. The function-field finite-cover theorem
supplies a replacement; it does not place those rotations in a number
field. The two-element template and the separate algebraic-line mass bound
of Proposition 9 in the carrier account remain valid weaker deductions,
but neither alone gives the required vanishing.

Two Bessel moments are feasible near $x=1$. They do not by themselves
exclude measurable avoidance there; the circle argument supplies that
exclusion. Parallel straight-strip classification is false, and a
classification by the more general zebra-like colorings remains unknown.
Neither classification is a premise of the candidate.

## Verification scope

The [[research/leads/equilateral_two_scale/evidence/verify/whole_conclusion/grade|whole-conclusion grade]]
accepts the finite-branch argument, uniform rational Cauchy space and
finite-dimensional quotient, the field hypotheses of the retained source
lemmas, the circle proof and Bessel bounds, and finite forcing of the
exact triangle formulation. It covers arbitrary colorings and every real
positive unequal ratio, including collinear triples of distinct points.
The rigidity input is discharged in the examined prose chain.

The separate Lean interface, source PDF fidelity, novelty and outside
acceptance are outside that grade. The external Lean formalization of the
result is checked separately, on its source card; it follows this route with
the departures its blueprint lists, among them an elementary nested-squares
argument in place of Federer's criterion. The
[[research/leads/equilateral_two_scale/evidence/verify/whole_conclusion/source_access|source-access account]]
identifies the editions and external theorem boundaries. A stronger or
repaired mathematical statement would require its own examination;
repository checks add no mathematical coverage.

## Sources and reading

- [[../library/discrete_geometry/openai_2026_euclidean_plane_not_five_colorable/_index|OpenAI 2026]]:
  manuscript Definition 2.1 through Lemma 2.7, Section 3 and Section 4 read
  at proof depth in the transcription; the opening of Section 5 through
  Definition 5.1 and the proof of Lemma 5.5 read; the remaining portions of
  Sections 5 to 8 are not used here. The Lean
  files `Ergodicity.lean`, `Basic.lean` and `Representations.lean` under
  `lean/OAI/Analysis/PlaneSpectrum/` and `BorelTransfer.lean` and `Five.lean`
  under `lean/OAI/Geometry/PlaneColoring/` were read for the statements and
  the dependency chain named on the spectral account; the proofs of the
  rigidity files were not read.
- [[../library/discrete_geometry/jelinek_2009_monochromatic_triangles_two_colored_plane/_index|Jelínek et al. 2009]]:
  Sections 1 and 2, Definitions 3.1 and 3.2, Theorem 3.3 and Lemmas 3.4 to
  3.12 with Claim 3.11 read in the transcription; Theorems 3.19 and 3.20 at
  statement and proof level. Definition 3.2 was also read on the page image
  of p. 7; no transcription repair was needed.
- [[../library/discrete_geometry/shkredov_2015_problems_euclidean_ramsey_theory/_index|Shkredov 2015]]:
  the source card and Theorem 1 at statement level, for the comparison on
  the spectral account.
- Jelínek et al. 2009, Lemma 1.3: proof read in the transcription; the
  eight-point configuration and all six orientation-preserving target maps
  are independently derived in the circle account for the measure form.
- [[theory/discrete_geometry/L32_equilateral_witness_size/_index|L32]]:
  statement and proof.
- Federer's criterion for finite perimeter (H. Federer, *Geometric Measure
  Theory*, 1969, 4.5.11): statement, boundary definition and perimeter
  formula read in P. Lahti,
  [arXiv:1804.11216v1](https://arxiv.org/abs/1804.11216v1), Introduction
  and Section 2, pp. 1--2 and 5--6; the original proof was not read.
- Tarski's transfer principle for real closed fields and Ramanujan sums:
  cited at statement level as
  standard facts, not read here.
- [NIST DLMF, Bessel definitions](https://dlmf.nist.gov/10.2): equations
  10.2.1 and 10.2.2, and
  [the large-argument asymptotic](https://dlmf.nist.gov/10.17.E3), at formula
  level. The rational enclosures and zero-spacing argument in Lemma 1 are
  derived in the spectral account.

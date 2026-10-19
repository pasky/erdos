---
name: analysis/lahti_2018_federer_characterization_finite_perimeter/theorem_1_1
title: "Theorem 1.1: finite perimeter from measure-theoretic boundary"
desc: |
  Finite codimension-one boundary measure implies finite perimeter in the
  stated metric setting. In the Euclidean plane the criterion and the
  perimeter representation imply that a measurable set with empty
  measure-theoretic boundary is null or conull.
created: 2026-10-17T04:03:50Z
updated: 2026-10-17T04:03:50Z
---

***

**Source.** P. Lahti, *Federer's characterization of sets of finite
perimeter in metric spaces*, arXiv:1804.11216v1, Theorem 1.1 (p. 2), with
(2.2) and (2.3) on p. 5 and (2.4) on p. 6, under the standing
hypotheses in Section 2 (p. 3). The Euclidean criterion recalled
on p. 1 is attributed to H. Federer, *Geometric Measure Theory* (1969),
Section 4.5.11. The [[analysis/lahti_2018_federer_characterization_finite_perimeter/_index|source card]]
identifies the version and reading limits.

**Read depth.** Claims checked: the stated hypotheses, boundary definition
and three formulas were read in the v1 TeX and on the PDF page images.
The original proofs of the criterion and representation were not read.
The application below is a direct author-recorded deduction by Plasma AI.

## Statement and convention

Let $(X,d)$ be a complete metric space with at least two points and let
$\mu$ be a Borel regular outer measure, positive and finite on balls and
satisfying the doubling condition. Suppose that $(X,d,\mu)$ supports a
$(1,1)$-Poincare inequality.
Write $P(A,\Omega)$ for the variation of the indicator of a measurable
set $A$ in the open set $\Omega$, and $\mathcal H$ for the
codimension-one Hausdorff measure formed from ball weights $\mu(B(x,r))/r$.
The measure-theoretic boundary is

$$
\partial^* A=
\left\{x:
\limsup_{r\downarrow0}\frac{\mu(A\cap B(x,r))}{\mu(B(x,r))}>0,
\quad
\limsup_{r\downarrow0}\frac{\mu(B(x,r)\setminus A)}{\mu(B(x,r))}>0
\right\}.
$$

**Theorem 1.1.** If $\mathcal H(\partial^*A\cap\Omega)<\infty$, then
$P(A,\Omega)<\infty$.

For finite-perimeter sets the accompanying representation (2.4) gives

$$
P(A,U)=\int_{\partial^*A\cap U}\theta_A\,d\mathcal H
$$

for Borel $U\subset\Omega$, with $\theta_A$ bounded above and below by
positive constants depending on the metric-space constants. The relative
isoperimetric inequality (2.2) gives

$$
\min\{\mu(A\cap B(x,r)),\mu(B(x,r)\setminus A)\}
\le 2C_P r\,P(A,B(x,\lambda r)),
$$

where $C_P$ and $\lambda$ are Poincare constants. These formulas retain
the source's normalization; no exact normalization of $\mathcal H$ is
needed when the boundary is empty.

## Euclidean application

Let $A\subset\mathbb R^2$ be Lebesgue measurable and suppose that
$\partial^*A=\varnothing$. Then $A$ is null or conull.

Indeed, in every open ball $\Omega$ the criterion gives finite perimeter,
and (2.4) gives $P(A,\Omega)=0$. Apply (2.2) to any ball, taking a larger
open ball for its dilate if necessary. At least one of $A$ and its
complement has zero measure in that ball. For the nested balls
$B(0,n)$, $n\ge1$, the same choice must hold for every $n$: two different
choices would contradict the positive measure of the smaller ball. Their
union is the plane, proving the assertion.

For a measurable red-blue coloring let $A^*$ be the red density-one
points and $B^*$ the red density-zero points. Then
$\mathbb R^2\setminus(A^*\cup B^*)=\partial^*A$, exactly with the
limsup convention above. Indeed, failure of both density limits $0$ and
$1$ is equivalent to positive upper density of each class. Thus proving
this complement empty suffices for the application; proving only that
it has area zero does not.

The criterion is used locally. No finite area, boundedness, smoothness or
polygonality of $A$ is required. The measure-theoretic boundary is not
the topological boundary or a boundary defined only at density $1/2$.

## Bears on

- [[../wiki/problems/discrete_geometry/E0173/_index|Problem 173]]: supplies
  the last measure-theoretic implication for an approach that first forces
  the boundary of a measurable avoiding coloring to be empty. The geometric
  premise remains the responsibility of the
  [[../wiki/research/leads/equilateral_two_scale/_index|two-scale argument]].

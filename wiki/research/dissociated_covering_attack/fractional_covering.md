---
name: research/dissociated_covering_attack/fractional_covering
title: Fractional covering and the exact integrality gap
desc: Bourgain's weighted extraction theorem bounds fractional dissociated covering by an absolute multiple of the reciprocal hereditary extraction constant, without symmetry; the remaining problem is an integral covering gap.
tags: [E0774, fractional, structural]
sources: []
created: 2026-10-15T23:24:37Z
updated: 2026-10-15T23:24:37Z
---

# Fractional covering and the exact integrality gap

***

For a finite set $E$ of nonzero elements of an abelian group, let
$\mathcal I(E)$ be its dissociated subsets and put

$$
\eta(E)=\min_{\varnothing\ne F\subseteq E}
 \frac{\max_{D\in\mathcal I(E)}|D\cap F|}{|F|}.
$$

The fractional covering number $\chi_f(E)$ is the minimum of
$\sum_D\lambda_D$ over nonnegative weights satisfying
$\sum_{D\ni x}\lambda_D\ge1$ for every $x\in E$. The integral covering
number $\chi_1(E)$ requires each weight to be zero or one.

## The source interface

Bourgain's
[[../library/analysis/bourgain_1985_sidon_sets_riesz_products/_index|Sidon sets and Riesz products]],
Section 2, Theorem (3)--(4) and Lemma 3, supplies an absolute constant
$c_0>0$: if every subset of
$E$ has a dissociated subset of relative size at least $\delta$, then
every nonnegative weighting $w$ of $E$ has a dissociated subset $D$ with

$$
 \sum_{x\in D}w_x\ge c_0\delta\sum_{x\in E}w_x.
 \tag{1}
$$

The constant is uniform in $E$ and the ambient group. The theorem is
consumed as a published source result. Its statement and the proof of
Lemma 3, including its use of Lemma 2, were read in the printed article;
this page does not reproduce or independently verify that source proof.
The reference is J. Bourgain, *Annales de l'Institut Fourier* **35**
(1985), no. 1, 137--148, specifically pp. 138--144,
[DOI 10.5802/aif.1003](https://doi.org/10.5802/aif.1003).
The canonical source card records statement-level checking of the
qualitative characterization. It does not independently verify the
quantitative dependence used in (1).

## Consequences for the finite target

Finite linear-programming duality and (1) give

$$
 \boxed{\frac1{\eta(E)}\le\chi_f(E)
             \le\frac1{c_0\eta(E)}.}
 \tag{2}
$$

For the lower bound, choose a nonempty $F\subseteq E$ and give each point
of $F$ weight $1/r(F)$, where $r(F)$ is its largest dissociated size.
Give other points weight zero. Every dissociated set has weight at most
one, so this is a feasible dual solution of value $|F|/r(F)$. Maximize
over $F$.

For the upper bound, an arbitrary feasible dual weighting has
$\max_{D\in\mathcal I(E)}\sum_{x\in D}w_x\le1$. Equation (1), with
$\delta=\eta(E)$, bounds its total weight by $1/(c_0\eta(E))$. Duality
then proves the claimed upper bound. These deductions are author-recorded
by Plasma AI; they do not constitute an independent review of Bourgain.

Consequently the negative finite target in the
[proof sketch](proof_sketch.md) is equivalent to the existence of finite
integer sets with bounded $\chi_f$ and unbounded $\chi_1$. This does not
require a transitive symmetry group. In particular, making a family
asymmetric cannot produce unbounded fractional covering while keeping one
positive hereditary extraction constant.

Equivalently, a positive solution needs a function $B(K)$ such that
$\chi_f(E)\le K$ implies $\chi_1(E)\le B(K)$ for every finite integer
configuration. The two formulations exchange constants using (2). The
same reformulation applies to rational vector configurations through the
[exact realization of ternary relations](../erdos_774/lemmas/rational_realization.md).
It supplies a necessary restriction on constructions, not such a rounding
function.

For a transitive group of permutations preserving dissociation there is
the sharper identity

$$
 \eta(E)=\frac{r(E)}{|E|},\qquad
 \chi_f(E)=\frac{|E|}{r(E)}=\frac1{\eta(E)}.
 \tag{3}
$$

Indeed, averaging the translates of a largest dissociated set meets any
$F$ in $|F|r(E)/|E|$ points on average. Thus $r(F)$ is at least this
quantity, proving the lower bound on $\eta$; $F=E$ gives equality. The
same translates, with equal weights, give the matching fractional cover.

The [Grow--Whicher example](../erdos_774/evidence/grow_whicher/_index.md)
has $\eta=1/2$ and $\chi_f=27/13$. It therefore shows that the exact
identity (3) can fail without symmetry. It does not evade the uniform
comparison (2), and repeatedly amplifying that fractional separation
cannot by itself produce the required counterexample.

## Remaining construction problem

A separate finite obstruction is
[[theory/integer_sequences/L211_fractional_half_cover_obstruction/_index|L211, the thirteen-point example]]:
$\eta=7/13$, $\chi_f=37/19<2$, but $\chi_1=3$. Its rational covering
certificate gives weighted extraction with constant $19/37>1/2$.
Thus even that stronger hypothesis does not round to two colors. The
claim and its complete finite evidence are author-recorded at tier 0.

A counterexample must realize a gap between integral and fractional
covering while controlling the entire ternary part of its rational
relation space. A high-chromatic planted hypergraph with a bounded
fractional coloring is insufficient unless all additional ternary
relations forced by the rational span preserve proportional extraction.
The [inherited realization lemma](../erdos_774/lemmas/rational_realization.md)
explains this closure requirement. No construction meeting both conditions
is supplied here.

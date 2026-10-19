---
name: set_systems/asgarli_2025_blocking_sets_union_plane_curves/theorem_3_2
title: "Theorem 3.2: counting Frobenius classes of line sections"
desc: |
  For a reflexive plane curve with geometrically irreducible components
  defined over an odd finite field, each product conjugacy class occurs
  among line sections with its group-theoretic density and an error
  uniform at fixed total degree.
created: 2026-10-16T23:57:33Z
updated: 2026-10-16T23:57:33Z
---

***

## Statement

Use the odd-characteristic setting of Section 3 in
[[set_systems/asgarli_2025_blocking_sets_union_plane_curves/_index|Asgarli, Ghioca and Yip, v2]].
Let a reduced reflexive plane curve over $\mathbb F_q$ have distinct
geometrically irreducible components $C_i$, each defined over
$\mathbb F_q$, with degrees $d_i$ and total degree $D=\sum_i d_i$.
Let $U$ be the open set of nontangent lines used in the theorem, on
which the Frobenius permutation of a transverse line section is defined.
For a conjugacy class $\mathcal C$ of
$G=\prod_i S_{d_i}$, Theorem 3.2 gives

$$
\#\{\ell\in U(\mathbb F_q):
       \operatorname{Frob}(C\cap\ell)=\mathcal C\}
=\frac{|\mathcal C|}{|G|}q^2
  \bigl(1+O_D(q^{-1/2})\bigr).
$$

The implied constant depends only on the total degree. Thus the estimate
is uniform over curves of bounded degree, even when the curve varies
with the field. In the applications here $d_i\ge2$. A rational point of
a transverse section corresponds to a fixed point of Frobenius, so any
class with no fixed point in any factor counts lines missing the curve.

The choice of a full $d_i$-cycle in every factor has relative size
$\prod_i 1/d_i$. Equation (3.1) on printed p. 7 therefore gives that
coefficient for a subfamily of the missing lines. It is not asserted to
count every missing line.

## Source and reading scope

Theorem 3.2 and equation (3.1), printed p. 7 of the
[v2 PDF](asgarli_2025_blocking_sets_union_plane_curves.pdf), with the
odd-characteristic and reflexivity conventions on pp. 6–7. Claims
checked: the theorem and formula were read clause by clause in the TeX
sidecar and on the page image. The application in equations (3.1)–(3.2)
was followed. No independent proof verification is claimed.

The paper imports this theorem from Alexei Entin, *Monodromy of
hyperplane sections of curves and decomposition statistics over finite
fields*, IMRN 2021(14), 10409–10441, Theorem 1. Entin's original proof
is not read here. The preceding paragraph on p. 6 imports from Hefez the
fact that a geometrically irreducible plane curve of degree $d$ is
reflexive if the characteristic is greater than $d$; that original
result is also unchecked. These are the external interfaces used when
specializing to prime fields with $p>D$.

## Bears on

- [[../wiki/problems/set_systems/E1159/_index|Problem 1159]]: supplies
  uniformly many lines missing a fixed-degree nonlinear curve. The
  [[../wiki/research/leads/projective_plane_bounded_blocking/curve_reduction|approximation route]]
  still has to put an arbitrary minimal bounded-cap blocking set close
  enough to such a curve; the theorem alone does not do that.

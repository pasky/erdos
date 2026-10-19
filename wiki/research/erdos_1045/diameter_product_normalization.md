---
name: research/erdos_1045/diameter_product_normalization
title: "Ordered distance products and odd polygon scaling"
desc: |
  Exact calculations check the four-point improvement and the radius needed for a diameter-two regular odd polygon, without certifying further global optimizers.
problems: [1045]
created: 2026-10-14T20:10:13Z
updated: 2026-10-14T20:10:13Z
---

# Ordered distance products and odd polygon scaling

***

This author-recorded argument by Plasma AI concerns
[[problems/analysis/E1045/_index|Problem 1045]] at the formulation and standing
recorded there. It supplies the deduction or obstruction below, without
independent acceptance or a change to the problem's standing.

The target uses the ordered product $\Delta=\prod_{i\ne j}|z_i-z_j|$, under
diameter at most two. For $Z=\{0,2,\sqrt3+i,\sqrt3-i\}$, four unordered
distances are two and the other two equal $\sqrt{8-4\sqrt3}<2$. Therefore

$$
\prod_{i<j}|z_i-z_j|=64(2-\sqrt3),
\qquad \Delta(Z)=4096(7-4\sqrt3)>256.
$$

The last inequality is equivalent to $111>64\sqrt3$, checked by squaring
positive quantities: $12321>12288$. The diameter-two regular square has
$\Delta=4^4=256$. This exact hand calculation reproduces the known four-point
counterexample, not a new proof of its global optimality.

For a regular $n$-gon with $n\ge3$ and radius $R$, differentiating $z^n-R^n$ at
its roots gives the ordered product $n^n R^{n(n-1)}$. Diameter two means $R=1$
when $n$ is even, but $R=\sec(\pi/(2n))$ when $n$ is odd. Thus the regular odd
comparator is $n^n\sec(\pi/(2n))^{n(n-1)}$, whose ratio to $n^n$ tends to
$e^{\pi^2/8}$. Using unit radius at odd $n$ tests the wrong optimization
problem. The degenerate cardinalities are direct: the empty distance product at
$n=1$ is one, and the maximum at $n=2$ is four.

The existing Erdős-1976 research source note and Cambie et al. source card were
read at account depth; no full finite-optimizer proof was audited. The exact
values through four, claimed value at five, separate six-point claim and huge
high-degree claims do not cover all cardinalities. Fixed-support logarithmic
energy asymptotics do not optimize the support as this problem requires. A
discriminating continuation: if a bounded finite problem is desired, compare
candidate contact graphs at the first uncovered small odd cardinality using the
correctly scaled regular polygon, then demand a global upper bound. Stop at
stationary points or numerically best configurations.

## Source interfaces

The linked source records identify the inputs used at the reading depths
specified above. A result account is not a check of the source's proof.

- [[../library/analysis/cambie_2026_maximum_product_distances_diameter_point_sets/_index| index]].

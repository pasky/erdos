---
name: research/erdos_774/lemmas/coefficient_two_factor_products
title: Two-factor products of coefficient-two circuits have two colors
desc: For d,e at least four, the product of two coefficient-two circuits C_d and C_e has two rationally independent color classes, so full-product flattening of two staircase factors forces no relation.
tags: [E0774, proved, obstruction]
sources: []
created: 2026-09-24T23:30:00Z
updated: 2026-09-24T23:30:00Z
---

# Two-factor products of coefficient-two circuits have two colors

***

After the [prime staircase](prime_staircase_obstruction.md) retired
density-only descent, a further actual-color attempt examined the **full**
products of its coefficient-two circuits, not just their mandatory subsets.
Up to rational basis changes and column signs these factors are

$$
C_d=\{e_1,\ldots,e_d,w\},\qquad w=\tfrac12\sum_a e_a.
$$

The fixed ratio two would flatten two factors by the
[coefficient-growth criterion](../routes/coefficient_growth_flattening.md)
if the requisite full dependent supports had one product color, but no
mechanism forces that condition. Proper subalphabets of a factor are
independent, so arbitrary subalphabet focusing does not preserve its
circuit.

## The two-factor check

An exact two-factor check gives a useful small-case boundary without a
computation. For $d,e\ge4$, the product $C_d\otimes C_e$ has two
rationally independent color classes. Color the leaf grid by surjective row
and column types in $\mathbb Z/4$, red when column type minus row type is
in $\{0,1\}$, and blue otherwise. Each color's spanning bipartite graph is a
blowup of a connected eight-cycle. Color each of the two wildcard wings with
both colors and color the center arbitrarily. A rational relation has
coordinate equations

$$
4k_{ab}+2y_a+2z_b+t=0.
$$

For a monochromatic relation, the opposite-color grid is connected and has
$k_{ab}=0$, forcing constant row coefficients $y_a=\alpha$ and column
coefficients $z_b=\beta$. An opposite-color vertex in each wing gives
$\alpha=\beta=0$, hence $t=0$ and all $k_{ab}=0$. The disjoint-wing
ternary relation $\sum_a e_a\otimes w-\sum_b w\otimes e_b=0$ gives the
matching lower bound two. Thus all finite-height coloring numbers equal two
in this two-factor case. This algebraic check makes no assertion for three
or arbitrarily many factors.

## Consequence

The full-product attempt therefore still needs actual-color control of all
leaves or a coefficient-safe substitute. It is not an amplification
theorem. The required negative solution still needs either unbounded
$\chi_h(G)$ at one fixed finite height or a valid actual-color substitute;
the coefficient-growth inequality supplies a broader sufficient flattening
target, and the staircase shows why raw short-relation rank cannot force
it. This page is author-recorded; a separate reviewer checked the
two-factor algebra.

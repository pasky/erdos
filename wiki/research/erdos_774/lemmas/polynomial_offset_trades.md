---
name: research/erdos_774/lemmas/polynomial_offset_trades
title: Binary affine-offset palettes fail at polynomial stage two
desc: A full-graph lifting lemma and an adaptive four-direction character identity defeat every common-linear-intercept binary palette with arbitrary direction offsets by stage two; arbitrary colorings remain open.
tags: [E0774, lines, coloring, proved, restricted-palette]
sources: []
created: 2026-09-19T01:00:00Z
updated: 2026-09-19T01:00:00Z
---


# Binary affine-offset palettes fail at polynomial stage two

***

## The proved statement and its scope

Use the binary [polynomial line model](../routes/field_tower_lines.md).
Write $V_j=\{f\in\mathbb F_2[t]:\deg f\leq j\}$, with zero included,
and $X_m=V_m\times V_{2m}$. The actual slope-$r$ columns are all
cosets of

$$
H_r=\{(a,ra):a\in V_j\},\qquad j=\deg r,
$$

where zero is assigned $j=0$. The vertical direction is
$H_\infty=\{(0,a):a\in\mathbb F_2\}$.

**Theorem.** Let $L:\mathbb F_2[t]\to\mathbb F_2$ be linear, and choose
arbitrary offsets $h_r,h_\infty\in\mathbb F_2$, independently in every
direction. Color a slope-$r$ coset represented by $(u,v)$ by

$$
c_r(u,v)=L(v-ru)+h_r,
\qquad c_\infty(u,v)=L(u)+h_\infty.                 \tag{1}
$$

This well-defined coloring has a monochromatic nonzero ternary relation
already in $X_2$. If $L(1)=1$, each of its two color classes has such
a relation, using at most four slope directions and no vertical column.

In particular, the proper offset two-coloring of the **entire stage one**
in the [previous diagnostic](../evidence/polynomial_checksum/_index.md) has no
stage-two extension of form (1), even if the higher values of $L$ and
all new direction offsets may be chosen afresh. This does **not** prove
that stage two needs three colors: general colorings need not have form
(1). It does not establish unbounded actual coloring.

## 1. An exact full-graph lifting device

For $r\in V_m$, $b\in V_{2m}$, define the auxiliary full graph

$$
G_{r,b}=\{(x,rx+b):x\in V_m\}.
$$

It is not necessarily an actual column. For representatives $a$ of
$V_m/V_j$, however, it has the disjoint partition

$$
G_{r,b}=\bigsqcup_a\bigl((a,ra+b)+H_r\bigr).       \tag{2}
$$

All constituent columns have color $L(b)+h_r$. Different intercepts
give disjoint sets of columns, and columns from different slopes cannot
coincide. Indeed equal nonempty cosets imply equal direction subgroups;
then $(1,r)\in H_{r'}$ forces $r=r'$.

Consequently, if ternary-valued functions $f_r:V_{2m}\to\{0,\pm1\}$
are supported on $L(b)=\gamma+h_r$, and

$$
\sum_r f_r(y-rx)=0\qquad((x,y)\in X_m),            \tag{3}
$$

assigning coefficient $f_r(b)$ to every component of (2) gives an
actual color-$\gamma$ ternary relation. If some $f_r\ne0$, the relation
is nonzero: there are no column collisions in the lift. Stage-one
relations embed into stage two by zero extension, by genuine nesting.

The lifting observation also applies to other colorings whenever the
chosen full graphs have monochromatic constituent partitions. It does
not assert that arbitrary colorings have such graphs.

## 2. The degenerate case and singular Hankel matrices

If $L(1)=0$, each of the three parallel classes of the initial constant
four-point plane is monochromatic, with its direction's offset. Two
classes share a color. Their equal total indicators give a nonzero
four-column trade. This handles arbitrary vertical offset as well.

Assume henceforth $L(1)=1$, and put

$$
M_m=(L(t^{i+j}))_{0\leq i,j\leq m}.
$$

If $M_m$ is singular, choose $0\ne d\in V_m$ with $L(dx)=0$ for
every $x\in V_m$. For either fixed color $\gamma$, its full graphs
in direction $r$ partition the nonempty affine hyperplane

$$
W_r=\{(x,y):L(y-rx)=\gamma+h_r\}.
$$

The underlying linear functionals for $W_r,W_{r+d}$ are equal. If any
such pair has equal offsets, the hyperplanes coincide and subtracting
their monochromatic partitions gives a two-direction trade. Otherwise
every pair has opposite offsets, hence

$$
1_{W_r}+1_{W_{r+d}}=1_{X_m}.
$$

For $m\geq1$, choose two distinct cosets of the subgroup $\{0,d\}$
in $V_m$ and subtract these identities. This gives a four-direction
trade. Every constituent is in color $\gamma$, and the distinct
directions make it nontrivial. Thus singularity of either $M_1$ or
$M_2$ proves the theorem in both colors.

## 3. Consecutive nonsingular matrices give an adaptive trade

It remains to assume $M_1,M_2$ are both nonsingular over $\mathbb F_2$.
Let $\lambda:V_4\to\mathbb F_2$ extract the coefficient of $t^4$,
and let the coefficient vector of $w\in V_2$ be $M_2^{-1}e_2$.
The cofactor identity gives

$$
w_2=(M_2^{-1})_{22}=\frac{\det M_1}{\det M_2}=1.
$$

For $x=x_0+x_1t+x_2t^2\in V_2$, therefore,

$$
L(wx)=x_2=\lambda(wx),\qquad (\lambda+L)(wx)=0.    \tag{4}
$$

Also $\lambda(ux)=0$ for every $u\in V_1$. The four pairs
$\{u,u+w\}$, $u\in V_1$, partition $V_2$. Put

$$
s_u=(-1)^{h_u+h_{u+w}}.
$$

Choose distinct $u,u'\in V_1$ with the same value $s=s_u=s_{u'}$.
This choice depends on the actual direction offsets, not on a prescribed
four-direction support. For either color $\gamma$, define

$$
f_r(b)=(-1)^{\lambda(b)}1_{L(b)=\gamma+h_r}
=\tfrac12\left((-1)^{\lambda(b)}
 +(-1)^{\gamma+h_r}(-1)^{(\lambda+L)(b)}\right).    \tag{5}
$$

Using (4), the second character terms cancel in

$$
P_u(x,y)=f_u(y-ux)-s_u f_{u+w}(y-(u+w)x).
$$

The first character terms give exactly

$$
P_u(x,y)=\tfrac12(-1)^{\lambda(y)}
                  (1-s_u(-1)^{x_2}).             \tag{6}
$$

Hence $P_u-P_{u'}=0$, an identity of form (3) on the four distinct
directions $u,u+w,u',u'+w$. The old directions have degree at most one
and the new directions degree two. Each $f_r$ is ternary, is nonzero
on exactly half of $V_4$, and is supported on color $\gamma$.
Section 1 gives the required nonzero actual ternary relation.

## Review and next obligation

The proof is author-recorded; a separate reviewer independently checked
the degenerate case, both Hankel cases, exact character cancellation,
and the collision-free lift. These are internal checks, not external
review. No search, numerical calculation, or new external theorem is
used. The surviving task is a mechanism for **arbitrary finite palettes**;
failure of all palettes in (1) is not that theorem.

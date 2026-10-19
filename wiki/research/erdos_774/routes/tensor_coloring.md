---
name: research/erdos_774/routes/tensor_coloring
title: The exact tensor coloring obligation
desc: Signed-span intersections characterize coloring after adding a simplex factor, isolating the missing ingredient in the uniform-extraction construction.
tags: [E0774, proved, reduction, open]
sources: []
created: 2026-09-18T00:04:10Z
updated: 2026-09-18T00:04:10Z
---


# The exact tensor coloring obligation

***

The [tensor extraction theorem](tensor_extraction.md) supplies one uniform
full-dissociation constant. This page isolates what is needed to turn it into
a counterexample. All statements below are elementary; the chromatic-growth
obligation remains unproved.

## Layer criterion — proved

Throughout, $B$ is a nonempty finite set of nonzero vectors in a rational
vector space, and simplex side sizes $p,m$ are integers at least three.
The colorings may have empty color classes. For $C\subseteq B$, define

$$
\Sigma(C)=\left\{\sum_{x\in C}\epsilon_xx:
\epsilon_x\in\{-1,0,1\}\right\}.
$$

A subset of $B\otimes S_p$ has layers $C_1,\ldots,C_p\subseteq B$.
It is dissociated if and only if

1. each $C_j$ is dissociated; and
2. $\bigcap_{j=1}^p\Sigma(C_j)=\{0\}$.

Indeed a relation has one signed sum $u_j$ from each layer, and
$\sum_j u_j\otimes s_j=0$ is equivalent to
$u_1=\cdots=u_p$, because the sole rational relation of the simplex is
$s_1+\cdots+s_p=0$. Common nonzero sums give a relation, while a common
zero sum is trivial exactly when every layer is dissociated.

## A finite separation parameter

Suppose $B$ has a proper dissociated $q$-coloring. Let $\tau_q(B)$
be the least positive integer $p$ for which there are proper
$q$-colorings $f_1,\ldots,f_p$ of $B$ satisfying

$$
\bigcap_{j=1}^p\Sigma(f_j^{-1}(c))=\{0\}
\quad\text{for every }c\in[q]. \tag{1}
$$

Set $\tau_q(B)=\infty$ if there are no such colorings. Repeating layers
shows that if (1) holds for $p$, it holds for every larger $p$. The
layer criterion gives the exact equivalence

$$
\chi(B\otimes S_p)\leq q
\quad\Longleftrightarrow\quad p\geq\tau_q(B). \tag{2}
$$

Define the universal signed-span set

$$
U_q(B)=\bigcap_{f\text{ proper }q\text{-coloring}}
\ \bigcap_{c\in[q]}\Sigma(f^{-1}(c)).
$$

Then $\tau_q(B)=\infty$ if and only if $U_q(B)\ne\{0\}$.
To prove the nontrivial direction, take all finitely many proper colorings as
layers; by permuting color names, the intersection for any one fixed color is
exactly $U_q(B)$.

If $\chi(B)=q$ and $p\geq q+1$, then
$q\leq\chi(B\otimes S_p)\leq q+1$. For the upper bound, use a fixed
proper $q$-partition in every layer but choose its palette from $q+1$
colors so that each color is absent from at least one layer. Its signed-span
intersection is then zero. Thus (2) tells precisely when a single factor
raises the coloring number.

## A concrete but unproved route to completion

### Two elementary constraints on the threshold

Always $\tau_q(B)\geq3$ when $\chi(B)=q$. If two colorings witnessed
zero intersections, their corresponding color classes would be disjoint and
their unions dissociated. These $q$ unions cover every point twice, so
discarding any one union still covers $B$, contradicting $\chi(B)=q$.

There is also a reset after a sufficiently large chromatic jump. If
$\chi(B)=q$, $Y=B\otimes S_m$, $m\geq2q+1$, and
$\chi(Y)=q+1$, then

$$
\tau_{q+1}(Y)\leq2(q+1). \tag{3}
$$

Use palette colorings putting the new color on a chosen $q$-set of blocks,
and another coloring putting it on a disjoint $q$-set. Their signed spans
intersect only at zero, since the union uses at most $m-1$ independent
simplex directions. Repeat these two colorings with each of the $q+1$
cyclic permutations of the color names. For every color the intersection of
all resulting signed spans is zero, proving (3). Thus immediate repetition
of very large factors cannot by itself force successive chromatic jumps.

A finite benchmark is
$8\leq\tau_2(S_3\otimes S_5)\leq10$, with exact proofs and bounded
certificates in [the tensor-layer test](../evidence/tensor_layers/_index.md).

Critical cores give another restriction. If $\chi(B)=q$ and deleting
either of two distinct non-antipodal elements $x,y$ lowers the coloring
number, then $\tau_q(B)\leq2q$. Use a proper coloring having singleton
class $\{x\}$, another having singleton class $\{y\}$, and all cyclic
permutations of their color names. For each color the intersection is contained
in $\{0,\pm x\}\cap\{0,\pm y\}=\{0\}$. Thus reducing to critical cores
does not produce arbitrarily large thresholds cheaply.

### The remaining quantitative obligation

The analytic extension loss for a tensor base $B$ and side size $p$ is
at most $Q(B)/(2p^2)$, with $Q$ explicitly defined in the extraction
theorem. To force a chromatic jump while keeping the analytic losses summable,
one would like to choose

$$
p<\tau_q(B),\qquad Q(B)/(2p^2)\leq\varepsilon_q,
\qquad\sum_q\varepsilon_q<\rho(B_0).
$$

No family providing these inequalities at all stages is known in these notes.
In particular, neither $\tau_q(B)\gg\sqrt{Q(B)}$ nor unbounded coloring
for the explicit side sizes in the extraction theorem has been proved.

Universal anchors allow arbitrarily large $p$ for one jump, but the
[anchor-gluing obstruction](anchor_gluing.md) explains why they do not
automatically propagate after that jump.

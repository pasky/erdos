---
name: theory/number_theory/L270_recentered_pivot_obstruction/_proof
title: A split leaf and two clusters obstruct recentered certificates
desc: A split perfect binary tree forces the cluster counts in every longest star. The centered cost stays positive, and binary codes realize the construction by odd integers; the 65-element instance has exact defect 892.
created: 2026-10-15T23:06:00Z
updated: 2026-10-15T23:06:00Z
---

# A split leaf and two clusters obstruct recentered certificates

***

This proves
[[theory/number_theory/L270_recentered_pivot_obstruction/_index|L270]].
All valuations below are $2$-adic valuations of nonzero integers.

## Why the certificate implies dissociation

Let $a,b_j$ be positive odd integers, with
$v_2(b_j-a)=j$ pairwise distinct, and suppose (RC) holds. Consider a
ternary relation

$$
\varepsilon_0a+\sum_j\varepsilon_jb_j
=sa+\sum_j\varepsilon_j(b_j-a)=0,
\qquad s=\varepsilon_0+\sum_j\varepsilon_j.
$$

If all companion coefficients vanish, the relation is trivial.
Otherwise let $j_0$ be the least used companion level. The sum of the
difference terms has valuation $j_0$, since exactly one of them has
that valuation. Consequently $s\ne0$ and $v_2(s)=j_0$, because $a$
is odd. Thus $2^{j_0}\le|s|\le k+1$, and all used elements lie in
$D_{j_0}$. Recenter the original relation around $c_{j_0}$ to obtain

$$
2^{j_0}c_{j_0}\le |s|c_{j_0}
\le\sum_{x\in D_{j_0}}|x-c_{j_0}|<2^{j_0}c_{j_0},
$$

a contradiction.

## A tree with forced cluster counts

Fix $R>1$. Choose $1<R_0<R$ and positive integers $h,l$ such that

$$
h(R_0-1)>2,\qquad l(R_0-1)>2R_0.
\tag{1}
$$

In particular $l\ge3$. Put $k=h+l-1\ge3$. Begin with a perfect
binary tree of height $k-1$ and split one leaf into two children.
There are $2^{k-1}+1$ leaves. Only the two new leaves have depth $k$;
all other leaves have depth $k-1$.

For a given leaf, the possible depths of its lowest common ancestor
with another leaf are exactly the depths of the internal vertices on
its path. A star with $k$ distinct levels must therefore use one of
the two new leaves as pivot, and one leaf from each of the $k$ sibling
subtrees along its path.

Give the two new leaves location $1$. Of the other $k-1=h+l-2$
sibling subtrees along their common path, give all leaves in $h$ of
them location $R_0$, and all leaves in the remaining $l-2$ location
$1$. Every star with $k$ companions then contains exactly $h$ high
leaves and $l$ low leaves. Its centered cost defect is

$$
F(c)=l|1-c|+h|R_0-c|-2c.
$$

On $[1,R_0]$ this function is linear, with

$$
F(1)=h(R_0-1)-2>0,\qquad
F(R_0)=l(R_0-1)-2R_0>0.
$$

Below $1$ it decreases toward $F(1)$; above $R_0$ its slope is
$h+l-2>0$. Hence $F(c)\ge\delta>0$ for every $c>0$, where
$\delta=\min(F(1),F(R_0))$.

Replacing each location by a number within $\eta$ changes the defect
of any selected star, at any center, by at most $(k+1)\eta$.
Choose $\eta>0$ so small that

$$
(k+1)\eta<\delta,\qquad
0<1-\eta,\qquad R_0+\eta<R(1-\eta).
\tag{2}
$$

Thus the obstruction and the required ratio survive these changes.

## Realization by odd integers

Encode each leaf $\lambda$ by
$e(\lambda)=\sum_{r\ge0}b_r(\lambda)2^r$, where $b_r$ records its
choice of child at depth $r$; missing terminal bits are zero. Choose
an integer $H>k$. Two distinct leaves have different codes, and if
their lowest common ancestor has depth $r$, then
$v_2(e(\lambda)-e(\mu))=r<H$.

Write $\xi(\lambda)\in\{1,R_0\}$ for its assigned location. For a
positive integer $M$, define

$$
x(\lambda)=e(\lambda)+2^H
\left\lfloor M\xi(\lambda)+\tfrac12\right\rfloor,
\qquad y(\lambda)=2x(\lambda)+1.
$$

The $y(\lambda)$ are distinct positive odd integers, and

$$
v_2(y(\lambda)-y(\mu))=r+1.
$$

With $S=2^{H+1}M$, each $y(\lambda)/S$ tends to
$\xi(\lambda)$ as $M\to\infty$. Take $M$ large enough that all
these errors are below $\eta$. The set
$O=\{y(\lambda):\lambda\text{ a leaf}\}$ has the required size and
ratio by (2).

Only the two deepest leaves can be pivots of a star with $k$
companions. Every such star has all levels $1,\ldots,k$, so its
level-$1$ tail is the whole star. For any center $c>0$, its level-$1$
defect, divided by $S$, equals the defect of its scaled points at
center $c/S$. This is at least $\delta-(k+1)\eta>0$.
Condition (RC) at level $1$ is therefore impossible. This proves the
universal construction.

## The exact 65-element instance

Put

$$
x_t=2049+2t+1792\boldsymbol 1_{8\nmid t},\qquad 0\le t\le64.
$$

Since $256\mid1792$ and $v_2(2(t-t'))\le7$ for distinct indices,

$$
v_2(x_t-x_{t'})=1+v_2(t-t').
\tag{3}
$$

The indices $0$ and $64$ have all difference valuations $0,\ldots,6$;
every other index has exactly $0,\ldots,5$. For the latter assertion,
toggling any of the six lowest bits supplies those six valuations
within $\{0,\ldots,63\}$, and a difference of magnitude $64$ is
unavailable. Thus only $x_0,x_{64}$ can be pivots of a seven-companion
star. Also $\min O=2049$ and $\max O=3967<2\cdot2049$.

For either eligible pivot, the three levels $1,2,3$ supply high
elements, with indices respectively odd, congruent to $2$ modulo $4$,
and congruent to $4$ modulo $8$. Levels $4,5,6$ supply low elements
with indices congruent to $8$ modulo $16$, $16$ modulo $32$, and $32$
modulo $64$. The remaining level supplies the other endpoint, $0$ or
$64$. Every star therefore has three high and five low elements.

For ordered values $z_1<\cdots<z_8$, the minimum over $c>0$ of
$\sum_i|z_i-c|-2c$ occurs on $[z_5,z_6]$ and equals

$$
z_6+z_7+z_8-(z_1+\cdots+z_5).
$$

All high elements exceed all low elements. Their least possible sum
uses indices $1,2,4$, while the greatest possible low sum uses
$0,64,56,48,32$. These choices occupy distinct required levels and
can be made simultaneously. Hence the minimum over all stars and
centers is exactly

$$
(3843+3845+3849)-(2049+2177+2161+2145+2113)=892>0.
$$

This disproves (RC) at level $1$ for every such star.

## Eight dissociated elements still exist

Let

$$
D=\{2049,3843,3845,3847,3851,3859,3875,3907\}\subset O.
$$

Its seven high elements are $3841+2t$ for
$t\in C=\{1,2,3,5,9,17,33\}$. This code set is affinely
dissociated: in a balanced ternary relation on $C$, subtracting
pivot $1$ leaves coefficients of $1,2,4,8,16,32$; the least nonzero
power of two cannot cancel.

For a ternary relation on $D$, write $s$ for the sum of the seven
high coefficients and $\varepsilon$ for the coefficient on $2049$.
The code contribution has absolute value at most
$2(1+2+3+5+9+17+33)=140$. If $\varepsilon\ne0$, then
$|3841s+2049\varepsilon|\ge1792$ for every integer $s$; if
$\varepsilon=0$ and $s\ne0$, this absolute value is at least $3841$.
Both are impossible. Thus $s=\varepsilon=0$, and affine dissociation
of $C$ makes the relation trivial.

The seven high elements themselves have pivot $3843$ and differences
$2,4,8,16,32,64$, whose sum is $126<3843$. They satisfy (RC) with
every center equal to the pivot. Thus this instance has a
seven-element certificate and an eight-element dissociated subset,
despite having no eight-element certificate.

The
[[research/sharp_dissociated_subset/evidence/_index|retained exact entry point]]
also verifies (3)'s depth profile, the minimum $892$, the $256$ subset
sums of $D$, the seven-element certificate and a comparison progression.
The displayed arithmetic and argument establish the finite statements
without an exhaustive search over dissociated subsets of $O$.

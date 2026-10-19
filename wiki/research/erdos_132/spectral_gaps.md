---
name: research/erdos_132/spectral_gaps
title: A sharp multiplicative-gap criterion for rare distances
desc: |
  Any occurring r with no distance in (r,2r) is rare, including when 2r
  occurs; a seven-point family proves the factor two cannot be lowered.
sources: []
research_state: closed
created: 2026-09-23T01:43:51Z
updated: 2026-09-24T22:12:56Z
---


# A sharp multiplicative-gap criterion for rare distances

***

All multiplicities below count unordered pairs in the full planar set. This is
an unrestricted sufficient condition for a particular class to be rare, not a
solution of [Problem 132](../../problems/distance_problems/E0132/_index.md).

## The gap lemma

**Lemma.** Let $A$ be a finite planar set of $n\ge2$ distinct points.
If $r>0$ occurs and no distance in $(r,2r)$ occurs, then

$$m_A(r)\le n.$$

Consider one connected component of the distance-$r$ graph. If its
vertices are collinear, its graph is a finite path, including the
possible one-vertex path, and has fewer edges than vertices.

Otherwise there is a noncollinear two-edge path. Indeed, if every
two-edge path were collinear, connectedness would put the whole
component on one line. The third side of this noncollinear triangle
is strictly shorter than $2r$, hence at most $r$ by the gap hypothesis.
Its three vertices form a connected noncollinear set $S$ with
$\operatorname{diam}S\le r$.

Grow $S$ along edges of the component. Suppose a new vertex $z$ is
at distance $r$ from $w\in S$. If $|z-u|>r$ for some $u\in S$, then

$$r<|z-u|\le |z-w|+|w-u|\le2r.$$

The gap forces equality throughout the upper bounds. Thus $u,w,z$
are collinear, $|w-u|=r$, and $w$ is the midpoint of $u,z$.
Because $S$ is noncollinear, it has a point $p$ off this line.
Strict triangle inequality gives

$$|z-p|<|z-w|+|w-p|\le2r,$$

so $|z-p|\le r$. Also $|u-p|\le r$. But the two closed radius-$r$
disks centered at $u,z$, whose centers are $2r$ apart, meet only at
$w$. This contradicts the choice of $p$.

Consequently adjoining $z$ preserves diameter at most $r$. Every
noncollinear component therefore has diameter exactly $r$. Its
distance-$r$ edges are diameter pairs, so their number is at most
its vertex count by the planar diameter theorem. Sum over the
components to prove the lemma.

The open interval in the hypothesis is essential to the statement:
the proof explicitly permits the distance $2r$ to occur.

## Counting gaps

List the occurring distances as $r_1<\cdots<r_q$. The lemma and
the ordinary diameter bound give

$$R(A)\ge1+\#\{i<q:r_{i+1}\ge2r_i\}. \tag{1}$$

The classes counted on the right are distinct; none of the
gap-preceding classes is the diameter. In particular, an unbounded
number of such gaps forces rarity growth without any convexity or
arithmetic assumption.

## Sharpness of the factor two

Let $0<\theta<\pi/6$, $c=\cos\theta$, $s=\sin\theta$, and set

$$A=\{(0,0),(c,s),(c,-s),(2c,0),(-c,s),(-c,-s),(-2c,0)\}.$$

These seven distinct points have the following complete spectrum,
in strictly increasing order:

| Distance | Unordered multiplicity |
| --- | ---: |
| $2s$ | 2 |
| $1$ | 8 |
| $2c$ | 4 |
| $2$ | 2 |
| $\sqrt{1+8c^2}$ | 4 |
| $4c$ | 1 |

Here is a direct partition of the 21 pairs. Put $o=(0,0)$,
$t_\pm=(\pm2c,0)$, $a_\pm=(c,\pm s)$, and
$b_\pm=(-c,\pm s)$. The pairs $a_+a_-$ and $b_+b_-$ have
length $2s$. The four pairs from $o$ to the $a$'s and $b$'s,
the two $t_+a_\pm$ pairs, and the two $t_-b_\pm$ pairs have
length one. The pairs $ot_\pm,a_+b_+,a_-b_-$ have length $2c$;
$a_+b_-,a_-b_+$ have length two. The four pairs from each $t$
to the two opposite-side points have squared length
$9c^2+s^2=1+8c^2$. Finally $|t_+-t_-|=4c$.

The inequalities in the table follow from $0<s<1/2$ and
$\sqrt3/2<c<1$. Thus $m_A(1)=8>7$, but the next distance
after one is $2c\to2$ as $\theta\to0$. For any constant
$\lambda<2$, choosing $\theta$ sufficiently small gives a rich
class at one with no distance in $(1,\lambda)$. No factor below
two can replace two in the lemma.

## Scope and checks

The proof and the exact spectrum were checked by the author and are
author-recorded. No numerical enumeration is used.
The result also explains why sufficiently lacunary versions of the
[scalar-Bessel test spectra](unrestricted_frontier.md) cannot be
realized as planar distance spectra, despite satisfying that scalar
positivity condition.

Formula (1) gives no additional rare class when all consecutive
ratios are below two. No argument forces enough multiplicative gaps
in a hypothetical bounded-$R$ family. The seven-point example refutes
a smaller universal gap threshold, not either Erdős assertion.

## Cycle surplus is supported by the immediate shell

There is a quantitative version of the gap mechanism. Let $H$ be the
2-core of $G_r(A)$, with vertex set $B$. Let $J$ consist of pairs in
$B$ whose lengths belong to $(r,2r)$, let $X$ be their endpoint set,
and put $t=|X|$, $M=|J|$. Then

$$e(H)-|B|\le t+e(H[X]),\qquad
m_A(r)\le |A|+t+e(H[X])\le |A|+2M^2. \tag{S1}$$

If $\Delta(H)\le D$, then also

$$e(H)-|B|\le(D+2)M. \tag{S2}$$

**Geometric step.** Every vertex of $H$ has at most two neighbors in
$Y=B\setminus X$. Otherwise choose three or more such neighbors on
$C(p,r)$. Every mutual separation is at most $r$ or exactly $2r$.
An antipodal pair $u,v$ is impossible: a third neighbor would be within
$r$ of both, forcing it to be their midpoint $p$. Thus all these
neighbors are pairwise within $r$. They lie on an arc of angle at most
$\pi/3$. For clarity, relative to one neighbor their angles lie in
$[-\pi/3,\pi/3]$; the extremes differ by at most $2\pi/3<\pi$, so
their own chord bound reduces the difference to at most $\pi/3$.

Choose the extreme neighbors $u,v$ and an intermediate one $q$.
If $z$ is another $r$-neighbor of $q$ in $B$, then
$|z-u|\le r+|q-u|<2r$ and likewise for $v$. Since $u,v\in Y$,
these lengths are at most $r$. Normalize $p=0,r=1$. On the short
circular arc, $q=a u+b v$ with $a,b>0$ and $a+b>1$; the latter
follows also from strict convexity of the unit disk. The three distance
conditions imply

$$z\cdot q=|z|^2/2,\qquad z\cdot u,z\cdot v\ge |z|^2/2.$$

It follows that $|z|^2/2\ge(a+b)|z|^2/2$, so $z=p$.
Then $q$ has degree one in $H$, a contradiction.

**Counting.** The geometric step gives $e(H[Y])\le|Y|$ and
$e_H(X,Y)\le2t$, proving the first bound. Peeling removes at most
$|A|-|B|$ edges. Moreover $t\le2M$, and the $r$-pairs and the
intermediate-shell pairs on $X$ are disjoint, so

$$e(H[X])+M\le\binom t2,\qquad
 t+e(H[X])\le t+\binom t2-M\le2M^2.$$

This proves (S1), including $M=0$. Finally
$e(H[X])\le Dt/2$ proves (S2).

For a fixed largest rank $k$, the established core-degree bound
$D=4k-2$ gives $M\ge(e(H)-|B|)/(4k)$. Hence linear core surplus
forces linearly many pairs in the immediate interval $(r,2r)$, not just
somewhere above $r$. The author checked the antipodal and
intermediate-arc cases and the pair factors; the argument is
author-recorded. This controls pairs, not distinct successor
lengths: all the charged pairs could use very few lengths. No branching
argument giving additional rare classes has been established.

---
name: research/erdos_132/quantitative_rank_inverse
title: A polynomial quantitative rank inverse lemma
desc: |
  Two ordered anchors replace van der Waerden in the constant-width
  inverse argument, giving an explicit polynomial dependence on the error.
sources: []
research_state: closed
created: 2026-09-23T02:02:46Z
updated: 2026-09-24T22:12:56Z
---


# A polynomial quantitative rank inverse lemma

***

This strengthens the quantitative dependence in
[constant_width_inverse](constant_width_inverse.md). It does not resolve either
unrestricted question in
[Problem 132](../../problems/distance_problems/E0132/_index.md).

## Rank lemma

Let $p_0,\ldots,p_{m-1}$ be the vertices of a strictly convex polygon,
in counterclockwise order, with indices modulo $m$. Suppose that an
increasing list $d_1<\cdots<d_q$ and integers $e_i(j)$ satisfy

$$|p_i-p_{i+j}|=d_{j+e_i(j)},\qquad
1\le j\le F:=\lfloor m/3\rfloor,$$

where each $e_i$ is nondecreasing and takes values in $\{0,\ldots,E\}$.
Put $H=E+1$. If $m\ge1000H^3$, some circle contains at least

$$\frac{m}{360H^3} \tag{1}$$

of the vertices.

Partition $[1,F]\cap\mathbb Z$ into $12H$ consecutive intervals of
nearly equal length. A row $e_i$ is nonconstant on at most $E$ of
these intervals. Consequently one interval $J=[u,v]$ has fewer than
$m/12$ nonconstant rows, and

$$|J|\ge\frac{m}{36H}-2.$$

Call the other rows good and denote their constant values on $J$ by
$b_i$. More than $5m/6$ indices $i$ have both $i$ and $i+1$ good.
Color each such index by

$$(e_i(1),\ b_i-b_{i+1}).$$

There are at most $P=H(2E+1)\le2H^2$ colors. Averaging over cyclic
windows of length $2P$ gives one window containing more than $P$
good adjacent starts. Thus two equally colored starts have the form
$a$ and $a+k$, with $1\le k<2P\le4H^2$.

The two directed sides starting there have the same length. Let $T$
be the direct isometry taking $(p_a,p_{a+1})$ to
$(p_{a+k},p_{a+k+1})$. Directed sides of a strictly convex polygon
have pairwise distinct directions, so $T$ is not a translation.
It is a nontrivial rotation.

Set

$$t=b_a-b_{a+k},\qquad \delta=k+t.$$

Equal colors imply also $t=b_{a+1}-b_{a+k+1}$. For

$$j\in I:=[u+E+1,v-E]\cap\mathbb Z,$$

all four integers $j,j-1,j+t,j-1+t$ lie in $J$. Hence the rank
formulas give

$$
|p_{a+j}-p_a|=|p_{a+j+\delta}-p_{a+k}|,
\qquad
|p_{a+j}-p_{a+1}|=|p_{a+j+\delta}-p_{a+k+1}|.
$$

Both $T p_{a+j}$ and $p_{a+j+\delta}$ lie strictly to the left of
the target directed side. A point in a specified open half-plane
is uniquely determined by its distances to that half-plane's two
distinct boundary anchors. Thus

$$T p_{a+j}=p_{a+j+\delta}\qquad(j\in I). \tag{2}$$

Here the source offset is at least two and the target offset relative
to $a+k$ is $j+t\ge2$. Both offsets are at most $F$. In particular,
the strict half-plane assertions do not accidentally include side
endpoints. Also $F+4H^2<m$, so all relevant indices may be unwrapped
in one turn of the polygon.

The assumed lower bound on $m$ gives

$$|I|\ge\frac{m}{72H},\qquad |\delta|\le5H^2.$$

If $\delta=0$, (2) makes $T$ fix at least two distinct points,
which is impossible. Otherwise partition $I$ by index modulo
$|\delta|$. In each resulting progression, (2), used forward or
backward according to the sign of $\delta$, places all corresponding
points in a single orbit of $T$. One progression has at least the
number of points in (1). This number exceeds two under the stated
size assumption, so its orbit is not the rotation center and lies
on a positive-radius circle. This proves the lemma.

## Consequence for constant-width boundaries

The rank derivation in [constant_width_inverse](constant_width_inverse.md)
shows that an $m$-point subset of a constant-width boundary with
$q\le m/2+L$, $L\ge0$, satisfies the hypotheses above with
$E=\lceil4L+4\rceil$ once $m$ exceeds an absolute linear function
of $E$. Therefore the explicit hypothesis

$$m\ge1000(\lceil4L+4\rceil+1)^3$$

ensures a circle containing at least

$$\frac{m}{360(\lceil4L+4\rceil+1)^3}$$

points. In particular, the dependence on $L$ is polynomial rather
than an unspecified van der Waerden bound.

The proof was developed by a separate author, strengthened by the
author using the shifted index $\delta$, and is author-recorded. The
rank hypotheses remain essential: bounded
rarity alone has not supplied them with bounded $E$ for an arbitrary
large convex layer. Even a circle of size $m/(L+1)^3$ need not be a
positive fraction when $L$ grows; the existing positive-circle
theorem cannot then be invoked with a fixed constant.

---
name: research/erdos_132/line_covers
title: Rare distances in sets covered by few lines
desc: |
  A complete distance-rank count gives linear growth for a fixed number
  of covering lines, without arithmetic assumptions.
sources: []
research_state: closed
created: 2026-09-22T21:20:00Z
updated: 2026-10-13T05:28:09Z
---


# Rare distances in sets covered by few lines

***

This is a restricted result, not a resolution of
[Problem 132](../../problems/distance_problems/E0132/_index.md). It uses no source
theorem. Write $r_k$ for the $k$-th largest distinct distance and count
unordered pairs.

## Rank bound

Suppose $A$ is covered by $m$ lines, and partition its points into disjoint
nonempty sets $A_i$, each on one covering line. Then

$$m_A(r_k)\le k(2m^2-m). \tag{1}$$

If the covering lines are parallel, the stronger bound is

$$m_A(r_k)\le km^2. \tag{2}$$

For one assigned line, orient its coordinate and write its $r_k$-pairs
as $(x_j,x_j+r_k)$, with $x_1<\cdots<x_s$. The distances from
$x_s+r_k$ to $x_1,\ldots,x_{s-1}$ give $s-1$ distinct values larger
than $r_k$, so $s\le k$.

For a cross-pair $p\in A_i,q\in A_j$ at distance $r_k$, the point $p$
must be among the first $k$ or last $k$ points of $A_i$. Otherwise,
choose the direction on its line pointing away from the orthogonal
projection of $q$. In that direction there are at least $k$ other
points, whose distances from $q$ are distinct and larger than $r_k$.
This is impossible. Each of the at most $2k$ eligible points on line
$i$ has at most two radius-$r_k$ neighbors on line $j$. There are
therefore at most $4k$ such cross-pairs. Summing yields

$$km+4k\binom m2=k(2m^2-m).$$

For parallel lines at separation $h$, the cross-pairs have one of the
two signed coordinate differences $\pm t$, where
$t=\sqrt{r_k^2-h^2}$. For a fixed sign, suppose there are $s$ pairs.
Ordering their coordinates and fixing the endpoint at the extreme
which increases the signed gap gives $s-1$ distinct gaps larger in
absolute value than $t$. They give $s-1$ distinct cross-distances
larger than $r_k$, so $s\le k$. Thus there are at most $2k$ cross-pairs
per line pair (and only $k$ if $t=0$), proving (2).

## Consequence

For $m\ge2$,

$$R(A)\ge\left\lfloor\frac{n}{2m^2-m}\right\rfloor,$$

and for parallel lines,

$$R(A)\ge\left\lfloor\frac{n}{m^2}\right\rfloor.$$

Let $C$ be the relevant denominator and $K=\lfloor n/C\rfloor$.
When $K\ge1$, we have $n\ge C\ge2m$. A largest assigned line gives
at least $\lceil n/m\rceil-1\ge K$ distinct distances; indeed
$n/m-1\ge n/C$ follows from $n\ge C$ and $C/m\ge2$.
All top $K$ distances are rare by (1) or (2). For $m=1$, every
distance has at most $n-1$ pairs, and there are at least $n-1$
distinct distances.

In particular $R(A_n)\to\infty$ if the number of covering lines is
$o(\sqrt n)$. The argument does not give a useful uniform result
when every line cover needs order $\sqrt n$ or more lines.

## Improvement using convex layers

The [rank--layer bound](layers_and_obstructions.md) strengthens the
growth criterion to **any $o(n)$ covering lines**. Each line
contains at most two vertices of a convex hull, so if $m$ lines
cover $A$, the first $k$ layers contain at most $2km$ points.
Thus

$$m_A(r_k)\le 4k^2m,$$

using the later angular bound $m_A(r_k)\le2k|B_k|$. Since every
layer has at most $2m$ vertices, it also gives
$R(A)\ge\lfloor\sqrt{n/(4m)}\rfloor$. The direct rank bounds
(1)--(2) can still be stronger for very small $m$.

For every fixed $k$ this is at most $n$ once $m=o(n)$ and $n$ is
sufficiently large. The required fixed ranks exist eventually by
the general two-anchor bound $n\le2q(A)^2+2$.
The same conclusion holds if $o(n)$ exceptional points are not
on the covering lines: their contribution to the first $k$
layers is at most the total number of exceptions.

The [hyperbola-incidence theorem](algebraic_concentration.md) gives
a different strengthening: a fixed positive fraction of points
on just one line already forces linear rarity, without assuming
a line cover in advance.

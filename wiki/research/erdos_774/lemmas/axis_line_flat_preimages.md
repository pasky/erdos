---
name: research/erdos_774/lemmas/axis_line_flat_preimages
title: Integer height-preserving line preimages in at most three directions
desc: Every bounded integer point vector in the line image of a box with at most three directions has an equally bounded integer line preimage; no actual-color support is controlled, and four-direction samples are not a theorem.
tags: [E0774, proved, lifting, incomplete]
sources: []
created: 2026-09-18T19:39:00Z
updated: 2026-10-13T05:28:09Z
---


# Integer height-preserving line preimages in at most three directions

***

## Theorem and exact scope

Let $A$ be the full axis-line incidence matrix of a box with at most
three directions. For every integer $h\ge0$, every
$b\in\operatorname{span}_{\mathbb R}A\cap\mathbb Z^X$ with
$\|b\|_\infty\le h$ has an integer preimage
$$
Aa=b,\qquad \|a\|_\infty\le h. \tag{1}
$$
This theorem has **no color-support assertion**. In particular it does
not provide the same-color preimages required by the
[quotient coloring route](../routes/axis_line_quotient.md).
It is not established for four or more nonbinary directions.

## 1. One and two directions

One direction is immediate. For two directions, write
$b(x,y)=u(x)+v(y)$ with integer $u,v$, using a reference row
and column. The change $u'=u-s$, $v'=v+s$ bounds both functions
by $h$ precisely when
$$
s\in[\max u-h,\min u+h]\cap[-\min v-h,-\max v+h].
$$
The individual intervals are nonempty because each width is at most
$\max b-\min b\le2h$. The cross-endpoint inequalities follow from
$\max u+\max v=\max b\le h$ and
$\min u+\min v=\min b\ge-h$. Integer endpoints therefore permit
an integer $s$, proving (1).

## 2. Three directions: a bounded integral graph gauge

Write the box as $X\times Y\times Z$. An integer decomposition
$$
b(x,y,z)=A(y,z)+B(x,z)+C(x,y)
\tag{2}
$$
exists. Explicitly, with reference coordinates $x_0,y_0,z_0$, take
$$
\begin{aligned}
A(y,z)&=b(x_0,y,z),\\
B(x,z)&=b(x,y_0,z)-b(x_0,y_0,z),\\
C(x,y)&=b(x,y,z_0)-b(x_0,y,z_0)
       -b(x,y_0,z_0)+b(x_0,y_0,z_0).
\end{aligned}
$$
The missing third mixed difference vanishes because $b$ belongs to
the real line image, so these integer functions satisfy (2).

Regard them as an integer antisymmetric edge cochain $a$ on the
complete tripartite graph, oriented cyclically $Y\to Z\to X\to Y$.
Its circulation on every oriented tripartite triangle is the corresponding
value of $b$, of magnitude at most $h$.

Every simple graph cycle of length $m$ has a triangle filling with
total absolute coefficient mass at most $m$. If the cyclic part-label
sequence uses all three parts, some three consecutive vertices lie in
distinct parts: otherwise the labels would alternate between two parts.
Remove the middle vertex and fill the resulting triangle. This costs one
triangle and reduces the cycle length by one. Continue until a triangle
remains, or until a bichromatic cycle remains. The former costs one final
triangle; the latter cones to any vertex of the third part, using exactly
its length many triangles. Orientations give cancellation of interior
edges, and total filling mass is at most the original length.

Consequently every directed cycle $D$ satisfies
$$
\left|\sum_{e\in D}a(e)\right|\le h|D|. \tag{3}
$$
The same is true of closed walks by decomposition into simple cycles.
Now impose, for both orientations of each edge, the difference constraints
$$
\phi(v)-\phi(u)\le h-a(u,v).
$$
Equation (3) says that every directed cycle has nonnegative total
constraint weight. Add a source with zero-weight arcs to every vertex.
Shortest-path distances exist and are integers; a shortest walk can have
its nonnegative cycles removed. They provide feasible integer $\phi$.
The gauged cochain
$$
a'(u,v)=a(u,v)+\phi(v)-\phi(u)
$$
lies in $[-h,h]$ on every edge, using both orientations. Gauge
changes preserve all triangle circulations. Interpreting $a'$ as
line coefficients proves (1).

The explicit consecutive-three-parts deletion is needed for the stated
filling bound; arbitrary chord splitting alone would double-count chords.
This argument is author-recorded; a separate reviewer checked it.

## 3. Real preimages survive adjoining a binary side

If an old box has the real analog of (1) for every $h\ge0$,
adjoining a binary side preserves that real property. Write a new target
as $b=(b_0,b_1)$. Membership in the new line image means
$b_0-b_1$ belongs to the old line image. Obtain real coefficients
$d$ for that difference with $\|d\|_\infty\le2h$. Use
$d/2$ and $-d/2$ in the two old layers, and put
$(b_0+b_1)/2$ on the new-axis columns. These represent $b$ and
are bounded by $h$. Halving can destroy integrality, so no integral
extension is claimed. The three-direction argument also works over the
reals; hence this proves the real property with at most three nonbinary
directions and any number of binary ones.

## 4. Finite evidence, not higher-dimensional proof

Twenty stored targets on $[3]^3$ and $[3]^4$ have explicit
bounded integer preimages. The
[fixed verification probe](../evidence/axis_flat_preimages/_index.md)
checks exactly these targets and preimages with integer arithmetic;
it performs no search. Exact generation bounds, solver distinctions,
and an additional noncertified duplicate probe are recorded on that
page. These examples neither prove the four-direction preimage property
nor control any actual colors.

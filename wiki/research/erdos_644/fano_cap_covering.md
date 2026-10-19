---
name: research/erdos_644/fano_cap_covering
desc: An exact seven-dimensional fractional-cover formula and its elementary polyhedral proof.
tags: [proved, auxiliary-lemma]
sources: []
created: 2026-09-22T21:16:40Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/fano_cap_covering

***

Let $\mathcal C$ be the seven complements of lines of the Fano plane on $[7]$.
For nonnegative demands $q_1,\ldots,q_7$, let

$$
\phi(q)=\min\left\{\sum_{C\in\mathcal C}w_C:
w_C\ge0,\quad \sum_{C\ni i}w_C\ge q_i\ (i\in[7])\right\}.
$$

Then

$$
\boxed{\phi(q)=
\max\left\{\max_iq_i,\ \frac12\max_{\text{line }L}\sum_{i\in L}q_i,\
\frac14\sum_iq_i\right\}.}
\tag{1}
$$

Excess incidences in a covering solution can be deleted. Thus (1) is also the
minimum total mass of points realizing the exact row demands, when each point's
spectrum must be a subset of a Fano cap.

This lemma assists the block-profile constructions. It does not turn arbitrary
edges with the given profiles into members of an unsymmetrized family.

## Dual polytope

By finite linear-programming duality, it suffices to show that

$$
D=\{z\ge0:\sum_{i\in C}z_i\le1\ \text{for every cap }C\}
$$

is the convex hull of zero, the seven coordinate unit vectors, the seven
half-line vectors $\frac12\mathbf1_L$, and $\frac14\mathbf1$.

All the listed vectors are feasible. For the converse, put $u=\min_i z_i$. Then
$u\le1/4$. If $u=1/4$, all coordinates equal $1/4$: every coordinate belongs to
a cap whose sum is at most one. Otherwise

$$
z=4u\left(\frac14\mathbf1\right)+(1-4u)z',
\qquad
z'=\frac{z-u\mathbf1}{1-4u}\in D,
$$

and $z'$ has a zero coordinate. It remains to analyze this face.

## The six-coordinate face

Delete the zero-coordinate Fano point. Identify the other six points with the
edges of $K_4$, so that the four Fano lines not containing the deleted point
become the four stars of $K_4$. The remaining cap inequalities are exactly

$$
\sum_{e\in T}z_e\le1 \quad(T\text{ a triangle}),\qquad
\sum_{e\in Q}z_e\le1 \quad(Q\text{ a four-cycle}).
\tag{2}
$$


We show that this polytope is the convex hull of zero, the six edge unit
vectors, and the four half-star vectors. Consider

$$
B=\max\left\{\sum_v\beta_v:
\beta_v\ge0,\quad \beta_u+\beta_v\le2z_{uv}\right\}.
$$

Its dual is the minimum-cost fractional edge-cover problem on $K_4$, with edge
costs $2z_e$.

For nonnegative costs this problem has an integral optimum. Here is a short
justification specific to $K_4$. Restrict edge-cover variables to $[0,1]$ and
take an optimum extreme point. Every tight vertex incident with a fractional
edge has at least two fractional incident edges: it cannot also have an incident
edge of weight one. Independence of the fractional columns on the tight vertex
constraints, together with the degree count, forces every fractional component
to be a cycle, all its vertices tight. An even cycle admits an alternating
perturbation, so such a component must be an odd cycle. On four vertices the
only possibility is a triangle, but the fourth vertex could not then be covered
without meeting a tight triangle vertex. Thus no fractional edges occur.

An inclusion-minimal integral edge cover of $K_4$ is either a perfect matching
or a three-edge star. Consequently

$$
B=2\min\left\{\sum_{e\in M}z_e,\ \sum_{e\in S}z_e:
M\text{ a perfect matching},\ S\text{ a star}\right\}.
$$

Choose an optimal $\beta$ and set $\alpha_{uv}=z_{uv}-(\beta_u+\beta_v)/2\ge0$.
Then

$$
z=\sum_e\alpha_e\mathbf e_e+\sum_v\beta_v\left(\frac12\mathbf1_{\operatorname{star}(v)}\right).
$$

The coefficient sum is

$$
\sum_e\alpha_e+\sum_v\beta_v
=\sum_ez_e-\frac B2
=\max\left\{\sum_{e\notin M}z_e,\ \sum_{e\notin S}z_e\right\}\le1,
$$

because the complements of perfect matchings and stars are four-cycles and
triangles. This proves the asserted convex-hull description on the face, and
hence on $D$. Evaluating its listed vertices gives (1).

The initial bounded enumeration of active constraints suggested this formula,
but the proof above does not depend on that computation.

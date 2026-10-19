---
name: research/erdos_940/primitive_cubic_fibers
title: Primitive cubic multiplicity and low-degree geometry
desc: Common dilations have bounded entropy, low-height collision planes and three target cube classes are negligible, and the special cubic's output surfaces have no rational lines or conics.
tags: []
sources: []
created: 2026-09-22T17:29:14Z
updated: 2026-09-22T21:53:34Z
---


# Primitive cubic multiplicity and low-degree geometry

***

## Status

The statements below are proved. They isolate, but do not estimate, the
primitive large fibers in the
[cubic multiplicity problem](energy_and_multiplicity.md). No bounded logarithmic
moment or positive-density conclusion was obtained.

## Removing common dilations costs bounded entropy

Fix positive integral coefficients and $F(\mathbf x)=\sum_{i=1}^3a_ix_i^3$.
Let $r(n)$ count all positive representations and $r_*(n)$ those with
$\gcd(x_1,x_2,x_3)=1$. Define, with $0\log0=0$,

$$
A(X)=\sum_{n\le X}r(n)\log r(n),\qquad
A_*(X)=\sum_{n\le X}r_*(n)\log r_*(n).
$$

Then uniformly for sufficiently large $X$,

$$
0\le A(X)-\sum_{g\ge1}A_*(X/g^3)\ll_F X.                 \tag{1}
$$


To prove this, choose an input uniformly from the finite region
$\{\mathbf x\in\mathbb N^3:F(\mathbf x)\le X\}$, of size $T(X)\asymp_F X$.
Put $G=\gcd(\mathbf x)$ and $Y=F(\mathbf x)$. The representations of a fixed
$n$ split into gcd classes of sizes $r_*(n/g^3)$, where $g^3\mid n$.
The definition of conditional Shannon entropy therefore gives exactly

$$
A(X)-\sum_g A_*(X/g^3)=T(X)H(G\mid Y).
$$

Also $\Pr(G=g)\ll_F g^{-3}$, by the box bound for inputs of gcd $g$.
Consequently $\mathbb E\log G$ is bounded. Comparing this probability law
with $q_g=g^{-2}/\zeta(2)$ gives
$H(G)\le\log\zeta(2)+2\mathbb E\log G\ll_F1$; this is the elementary
nonnegativity of relative entropy. Since $0\le H(G\mid Y)\le H(G)$,
(1) follows.

In particular, the **uniform** bounds $A(X)\ll_F X$ and $A_*(X)\ll_F X$
are equivalent. One implication uses $r_*(n)\le r(n)$; the other uses (1)
and $\sum_g g^{-3}<\infty$. Bounds at small $X$ can be absorbed into the
constant. This is not a statement about transferring a bound given only
along one unspecified sparse sequence of scales.

For every fixed $1<p<3$, there is also the equivalence

$$
\sum_{n\le X}r(n)^p\ll_{F,p} X
\quad\Longleftrightarrow\quad
\sum_{n\le X}r_*(n)^p\ll_{F,p} X.                        \tag{2}
$$

Indeed $r(n)=\sum_{g^3\mid n}r_*(n/g^3)$, so Minkowski's inequality bounds
the $\ell^p$ norm of $r$ by a constant times
$X^{1/p}\sum_g g^{-3/p}$. The converse is immediate.
Thus common dilations do not account for the missing logarithmic or
fractional-moment estimate.

## Low-height projected collision planes have negligible input mass

Let $E_H(N)$ be the triples in $[1,N]^3$ lying on a rational plane through
the origin whose primitive integral normal has maximum norm at most $H$.
Then

$$
|E_H(N)|\ll N^2H^2+NH^3.                                \tag{3}
$$

For a primitive normal $\mathbf b$ of height $B$, relabel coordinates so
$|b_1|=B$. Set $g=\gcd(b_2,B)$. The congruence
$b_2x_2+b_3x_3\equiv0\pmod B$ forces $g\mid x_3$, since
$\gcd(g,b_3)=1$. For each such $x_3$, there is one residue class for $x_2$
modulo $B/g$. Thus there are at most
$N^2/B+N/g\le N^2/B+N$ possible pairs $(x_2,x_3)$, and the equation then
determines $x_1$. There are $O(B^2)$ normals of height $B$; summing proves
(3).

The fixed-box representation count satisfies $R_N(n)\le N^2$. For any
fixed $0<\eta<1/2$, (3) consequently gives

$$
\sum_{\mathbf x\in E_{N^{1/2-\eta}}(N)}
\log R_N(F(\mathbf x))
\ll N^{3-2\eta}\log N=o(N^3).                           \tag{4}
$$

Every fixed two-parameter homogeneous linear collision identity projects
to a fixed rational plane (or a subspace of one) in the input coordinates.
Equation (4) removes such identities, and all projected planes in the
stated height range, from the logarithmic-moment problem.

This range cannot simply be increased to cover all inputs. Every triple
of height at most $N$ has a nonzero integral orthogonal vector of size
$O(\sqrt N)$: pigeonhole the dot products of vectors in
$\{0,\ldots,L\}^3$, with $L$ a sufficiently large constant times $\sqrt N$,
into their $O(NL)$ possible values, and subtract two equal ones. Dividing
by the coordinate gcd makes the normal primitive. High-height planes
therefore contain the entire remaining problem, not an automatically
negligible exceptional set.

## Degrees of curves on the special output surfaces

For $n\in\mathbb Q_{>0}$ put

$$
S_n:\quad x^3+2y^3+4z^3=nw^3\subset\mathbb P^3_{\mathbb Q},
\qquad C=S_n\cap\{w=0\}.
$$

**Proposition.** Every curve defined over $\mathbb Q$ on $S_n$ has degree
divisible by $3$. In particular, $S_n$ contains no rational line or
rational conic. No cube-freeness hypothesis on $n$ is required.

First every closed point of $C$ has degree divisible by $3$. If $C$ has a
point over a finite extension $K/\mathbb Q_2$, let $e=v_K(2)$ with the
valuation normalized integrally. Unless $3\mid e$, the nonzero terms in

$$
x^3+2y^3+4z^3=0
$$

have valuations in distinct classes $0,e,2e\pmod3$. Their minimum would
occur uniquely, which is impossible. Hence $3\mid e$.
For a closed point with residue number field $L$, apply this at every
place $v$ above $2$. Each local degree $[L_v:\mathbb Q_2]=e_vf_v$ is
divisible by $3$, and their sum is $[L:\mathbb Q]$.

If a curve $D$ on $S_n$ is not contained in $w=0$, its hyperplane
intersection with $w=0$ is an effective zero-cycle over $\mathbb Q$ of
degree $\deg D$, supported on $C$. The preceding result makes this degree
a multiple of $3$. The smooth plane cubic $C$ itself has degree $3$;
this also handles curves contained in the boundary and arbitrary curve
cycles by additivity.

This excludes degree-one and degree-two curves on individual output
surfaces. It does **not** exclude the split planes on the six-variable
collision variety, whose outputs vary along the plane. Nor does it bound
the number of higher-degree curves or integral points uniformly as $n$
varies. Primitive high multiplicity remains uncontrolled.

## Three special target cube classes have negligible input mass

For $F=x^3+2y^3+4z^3$, let $E(N)$ be the positive triples in
$[1,N]^3$ with $F(\mathbf x)=2^e m^3$ for some
$e\in\{0,1,2\}$ and positive integer $m$. Then

$$
|E(N)|\ll N^{\sqrt3}(1+\log N)^4=o(N^3).              \tag{5}
$$

This uses the same checked statement of
[Salberger's Corollary 0.7](cubic_collision_ranges.md#coordinate-zero-differences-have-a-power-saving-for-distinct-cube-classes)
as the coordinate-sharing estimate, not a new uniform surface theorem. For fixed
$e$, consider the nonsingular diagonal cubic surface

$$
x^3+2y^3+4z^3-2^e m^3=0.
$$

A positive solution has no vanishing two-term subsum: a subsum
involving only positive terms cannot vanish, and cancellation with
the negative term would leave two strictly positive terms summing
to zero. Also $m\le7^{1/3}N$, so the projective height is $O(N)$.
The quoted bound gives $O(N^{\sqrt3}(1+\log N)^4)$ primitive
points. Summing common dilations gives the same order, since
$\sum_{g\ge1}g^{-\sqrt3}<\infty$; the additive constant in each
primitive bound contributes only $O(N)$. Summing over the three
values of $e$ proves (5).

As $R_N(n)\le N^2$, deleting these inputs costs at most
$2|E(N)|\log N=o(N^3)$ in the logarithmic-multiplicity sum.
This removes only three fixed rational cube classes of targets.
It supplies no bound for the remaining integer fibers and no
positive-density conclusion.

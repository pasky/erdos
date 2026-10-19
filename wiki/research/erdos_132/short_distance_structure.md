---
name: research/erdos_132/short_distance_structure
title: Short-distance spectra under bounded rarity
desc: |
  Local spectra constrain convex matchings and zigzags; deleting a large
  convex subset gives only a cutoff-dependent residual-rarity bound.
sources: []
research_state: closed
created: 2026-09-22T23:15:00Z
updated: 2026-09-24T22:12:56Z
---


# Short-distance spectra under bounded rarity

***

This is a local necessary condition, not a solution of
[Problem 132](../../problems/distance_problems/E0132/_index.md). Write $r_s$ for the
$s$-th smallest positive distance, and assume $R(A)\le K$.

## A bounded local spectrum

For an absolute constant $C$,

$$\#\{r\in D(A):r\le2r_s\}\le K+C s^2. \tag{1}$$

To prove this, fix $p\in A$ and cover its radius-$2r_s$ disk by
64 squares of side $r_s/2$. Each square has diameter less than
$r_s$, so its points determine at most $s$ distances. If it has
at least two points, use two as anchors. Every remaining point
is an intersection of one circle about each anchor, with radii
chosen among at most $s$ values. There are at most $2s^2+2$
points in the square. Hence $p$ has at most $128(s^2+1)$ points
of $A$ within distance $2r_s$.

Consequently distances at most $2r_s$ account for at most
$64(s^2+1)n\le128s^2n$ unordered pairs. Fewer than $128s^2$
of these distance classes can be rich, since each rich class has
more than $n$ pairs. There are at most $K$ rare classes, proving
(1), for example with $C=128$.

## Equilateral zigzags between two convex chains

Suppose $p_0,\ldots,p_t$ is an $x$-monotone path with all edges
of length $r_s$. Assume its even vertices follow the lower
boundary chain of a strictly convex polygon, its odd vertices
follow the upper chain, and successive edges alternate upward
and downward. Then

$$t\le 2K+2Cs^2+1. \tag{2}$$

Let the successive edge directions be
$\theta_i\in(-\pi/2,\pi/2)$, indexed by $0\le i<t$, and set

$$\beta_i=(-1)^i(\theta_i-\theta_{i+1})\in(0,\pi),
\qquad \phi_i=\theta_i+\theta_{i+1}.$$

The two-step chord is

$$p_{i+2}-p_i=2r_s\cos(\beta_i/2)e^{i\phi_i/2}.$$

Strict convexity of the two chains makes $\phi_{2j}$ strictly
increasing and $\phi_{2j+1}$ strictly decreasing. The identity

$$
\phi_i-\phi_{i+2}
=(-1)^i(\beta_i-2\beta_{i+1}+\beta_{i+2})
$$

therefore says that $(\beta_i)$ is strictly concave. Each value
occurs at most twice: three equal values would contradict strict
concavity at the middle index. The map
$\beta\mapsto2r_s\cos(\beta/2)$ is injective on $(0,\pi)$, so the
$t-1$ two-step chords determine at least $(t-1)/2$ distances.
All are at most $2r_s$. Apply (1) to obtain (2).

The hypotheses on the zigzag are essential. This does not control
all cross-chain edges, numerous small components, or branching
in a fixed-rank distance graph. In particular no almost-spanning
boundary chain or circle has been deduced from richness. The
bound supplies a local restriction for that missing step rather
than asserting it.

The author checked the disk count, unordered-pair factor, angle
identity, and strict-concavity inference; the argument is
author-recorded.

## Linear local spectrum for convex sets

If $A$ is in strictly convex position, the stronger estimate

$$
Q_\lambda:=\#\{r\in D(A):r\le\lambda r_s\}
\le K+C_0\lambda s\qquad(\lambda\ge1) \tag{3}
$$

holds for an absolute constant $C_0$. Here is a perimeter proof.
For fixed $p$, the subset $S=A\cap\overline B(p,\lambda r_s)$
is in convex position. Its hull perimeter is at most
$2\pi\lambda r_s$, by monotonicity of convex perimeter under
inclusion. Partition that boundary into at most
$\lceil4\pi\lambda\rceil$ arcs of length at most $r_s/2$,
assigning shared endpoints to just one arc. Each part has
diameter at most $r_s$ and thus at most $s$ distinct distances.
Altman's convex distance bound gives at most $2s+1$ points
per part. The cases $|S|\le2$ are immediate. Therefore $p$
has $O(\lambda s)$ neighbors within distance $\lambda r_s$.
Counting unordered pairs as above proves (3).

Altman's bound is recorded as Theorem 1 in the supplied
[Fishburn source](../../../library/distance_problems/fishburn_1995_convex_polygons_few_intervertex_distances/_index.md).
For $s=1$, one can omit it: after normalizing the minimum distance to one, any
convex subset in a radius-$\lambda$ disk has at most $2\pi\lambda$ points,
because every hull side has length at least one. This gives
$Q_\lambda\le K+\pi\lambda$ for $\lambda\ge1$, with the sets of at most two
points handled directly.

## Densely spaced, order-preserving cross matchings

Let $p_1,\ldots,p_m$ be points of an upper convex chain in
left-to-right order and $q_1,\ldots,q_m$ points of a disjoint
lower convex chain in left-to-right order. Assume their directed
successive-chord angles lie in one interval of width less than
$\pi/2$, and that

$$|p_i-q_i|\le r_s,\qquad |p_{i+1}-p_i|\le Lr_s,$$

where $L\ge1$. For strictly convex $A$ with $R(A)\le K$,

$$m\le2Q_{L+2}^{\,6}+1
\le2\bigl(K+C_0(L+2)s\bigr)^6+1. \tag{4}$$

All six distances in the ordered quadruple
$(p_i,p_{i+1},q_i,q_{i+1})$ are at most $(L+2)r_s$, by the
triangle inequality. Their ordered list determines the cosine
of the relative angle of its two directed chain chords, using

$$
2(b-a)\cdot(d-c)
=|a-d|^2+|b-c|^2-|a-c|^2-|b-d|^2.
$$

There are at most $Q_{L+2}^6$ lists, and each cosine gives at
most two relative angles in the stipulated nonwrapping interval.
But the upper chord angles strictly decrease while the lower
ones strictly increase, so all $m-1$ relative angles are distinct.
This proves (4). Cross-pair lengths need not be equal.

The author checked the six-distance bound, the polarization identity, and angle
monotonicity; the argument is author-recorded. These estimates still do not
control numerous isolated or widely separated cross components. Richness has not
been converted into the almost-spanning boundary successor structure needed for
circular rigidity.

## What can be inherited after removing a large convex subset

Let $C\subseteq A$ be strictly convex, with $m=|C|\ge cn$, and put
$I=A\setminus C$. The rest of $A$ need not be convex. Let $r_s$
remain the $s$-th smallest **global** distance. For any set $B$, let
$R_B(\le t)$ count its occurring distances at most $t$ whose
multiplicities are at most $|B|$.

The local perimeter proof above works for $C$ in a disk centered at
any point of $A$. A disk of radius $\lambda r_s$ contains
$O(\lambda s)$ points of $C$: partition its convex-hull perimeter
into $O(\lambda)$ arcs of length at most $r_s/2$ and use Altman's
bound to put at most $2s+1$ vertices on each. Thus there are at most
$C_1\lambda s n$ unordered pairs of length at most $\lambda r_s$
touching $C$, for an absolute $C_1$.

A class rare in $I$ but rich in $A$ must gain at least
$n+1-|I|=m+1$ such pairs. Therefore

$$R_I(\le\lambda r_s)
 \le R_A(\le\lambda r_s)+\frac{C_1\lambda s n}{m+1}
 \le K+O_c(\lambda s). \tag{5}$$

This is a checked local inheritance inequality with the correct
threshold $|I|$ on the residual set. It gives no uniform bound for
the total $R(I)$: allowing the cutoff to reach the full diameter
can make the error grow with $n$. Iterating deletion of large
convex layers therefore does not currently yield an induction for
the unrestricted problem.

Another attempted step was to turn few short chord lengths on an
equilateral convex chain into a periodic sequence of turning angles.
No such rigidity lemma was proved. Chord length does not encode
the turn word injectively: already the three-step square length
$3+2\cos\alpha+2\cos\beta+2\cos(\alpha+\beta)$ is unchanged by
reversing the two turns. No adequate bound on the fibers of the
longer-word map was established. Moreover, richness has not supplied
a long chain with the required boundary order. Neither missing
statement should be assumed when using (1)--(5).

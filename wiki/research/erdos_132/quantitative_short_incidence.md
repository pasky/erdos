---
name: research/erdos_132/quantitative_short_incidence
title: Quantitative short incidences and polynomial convex-cover bounds
desc: |
  Counting anchor multiplicities sharpens short incidences to n^(55/56)
  up to logarithms and gives polynomial rarity growth for convex covers.
sources: []
research_state: closed
created: 2026-09-23T07:03:23Z
updated: 2026-09-24T22:12:56Z
---


# Quantitative short incidences and polynomial convex-cover bounds

***

All multiplicities count unordered pairs. Write $n=|A|$, $q=q(A)$,
$R=R(A)$, and $\lambda=\log(2n)$. Constants in $\ll$ below are
absolute unless dependencies are indicated.

The improvement over [moving frames](moving_frames.md) is to count how
often each motion is induced by an anchor pair: its multiplicity is at
most $6j$ times its overlap with the convex chain, rather than merely
the total number of anchors. This gives the following conclusions.

**Short incidences.** If $R(A)\le K$ and $r$ has fixed smallest-distance
rank $j$, the number of $r$-edges touching any strictly convex subset is

$$O_{K,j}\bigl(n^{55/56}\lambda^{1/7}\bigr). \tag{1}$$

**Convex covers.** If $A$ is covered by $L\ge1$ strictly convex subsets,
then for an absolute $c>0$,

$$R(A)+1\ge
 c\frac{n^{1/64}}{L^{7/8}\lambda^{1/8}}. \tag{2}$$

In particular a fixed convex cover gives polynomial rarity growth.
More generally $L=o(n^{1/56}/\lambda^{1/7})$ forces $R(A)\to\infty$.
Neither conclusion supplies such a cover for arbitrary planar sets.

## Rich motions without a restriction on their number

Let $C$ be strictly convex, $|C|=m$, and suppose every circle contains
at most $h$ points of $C$. For a finite family $S$ of $s$ direct motions
having overlap $\nu_C(g)=|C\cap gC|\ge t\ge2$, we have

$$t^5s^2\ll
m^3\bigl(m^3\log(2m)+s^2\bigr)(\sqrt{s}+h). \tag{3}$$

Here is the extension of the calculation in [moving frames](moving_frames.md).
The affine-group energy bound and the vertical/nonvertical fiber bounds
$V\le3m^2/t^2$, $H\ll mh/t$ give

$$E(S)\ll(m/t)s^2(\sqrt{s}+h).$$

On the other hand, two applications of Cauchy--Schwarz give

$$\frac{t^4s^4}{m^2}
\le E(S)\sum_{u\in SS^{-1}}\nu_C(u)^2.$$

The rich-motion estimate $\#\{u:\nu_C(u)\ge v\}\ll m^3/v^2$
for $v\ge2$ bounds the sum by $O(m^3\log(2m)+s^2)$; the last term
accounts for one-point overlaps. Combining proves (3). No upper bound
on $s$ was used.

The two external inputs are equation (1) and Theorem 4.1 of Mansfield--Passant,
[*A Structural Theorem for Sets with Few
Triangles*](https://link.springer.com/article/10.1007/s00493-023-00066-z). Their
full statements were rechecked for this application. The remaining fiber
estimates and the energy calculation are proved in the linked note.

## An explicit narrow-chain estimate

Assume $q(A)\le n$, and let $r$ have smallest-distance rank $j$ in $A$.
Let $C\subset A$ be an ordered strictly convex chain of $m$ vertices
whose consecutive edge directions lie in an interval of width $\pi/3$.
Suppose $F$ is a collection of $E\le n$ distinct ordered anchors
$(p,q_0)$ with $p\in C$, $q_0\in A$, and $|p-q_0|=r$.
Then

$$E\ll
j^{17/12}n^{11/12}
+j^{19/15}n^{14/15}\lambda^{2/15}
+j^{8/7}n^{6/7}(h\lambda)^{1/7}, \tag{4}$$

where $h$ is the largest circular subset of $C$.

The case $E=0$ is immediate. The short-rank degree bound gives
$E\le6jm$. Use the
[narrow-chain bin argument](short_incident_inverse.md), now keeping
the dependence on $j$ explicit. A radius interval of length $r$ has
at most $20j$ pinned endpoints on the chain. Taking the bin overload
threshold $\lceil240jn/m\rceil+1$ leaves, for $m\ge8$,
at least $m/2$ noncollinear apices per anchor and at most
$1452jn^2/m$ oriented triangle types. For $m\le7$, (4) follows
directly from $E\le42j$; assume otherwise.

Thus the number of ordered pairs of retained congruent triangles is
at least

$$P_0=c\frac{E^2m^3}{jn^2},\qquad c=1/6000. \tag{5}$$

Every ordered pair of anchors determines one direct motion. Let
$f(g)$ count the anchor pairs inducing $g$, so $\sum_g f(g)=E^2$.
Their number of matching apex pairs is at most $\nu_C(g)$ each.
Discard motions with overlap less than

$$k=\frac{P_0}{2E^2}=\frac{cm^3}{2jn^2};$$

they account for at most $P_0/2$ matches. If $k<2$, then
$m^3\ll jn^2$ and
$E\le6jm\ll j^{4/3}n^{2/3}$, absorbed by the first term of (4).

The additional observation is

$$f(g)\le6j\nu_C(g). \tag{6}$$

Indeed, a source anchor root must lie in $C\cap g^{-1}C$, and
there are at most $6j$ choices of its distance-$r$ neighbor. Once
the source anchor is fixed, its image is fixed. This argument also
applies to the identity motion.

Group the remaining generated motions into dyadic overlap intervals
$[t,2t)$, starting at $k$, and write $s_t$ for the number in a level.
There are at most $E^2\le n^2$ generated motions altogether. By (6),

$$P_0/2\le24j\sum_t t^2s_t. \tag{7}$$

Apply (3) to each level. If $k^5$ is not larger than a sufficiently
large absolute constant times $m^3n$, then
$m^{12}\ll j^5n^{11}$ and $E\le6jm$ give the first term of (4).
Otherwise, since $\sqrt{s_t}+h\le2n$, the $s_t^2$ term on the right
of (3) can be absorbed into the left for every $t\ge k$. We obtain

$$t^5s_t^2\ll m^6\lambda(\sqrt{s_t}+h),$$

and hence

$$s_t\ll m^4\lambda^{2/3}t^{-10/3}
+m^3(h\lambda)^{1/2}t^{-5/2}. \tag{8}$$

Substituting (8) into (7) gives convergent geometric sums, not an
additional logarithmic loss:

$$P_0\ll
jm^4\lambda^{2/3}k^{-4/3}
+jm^3(h\lambda)^{1/2}k^{-1/2}.$$

Insert (5) and the value of $k$. At least one of

$$E^6m^9\ll j^{10}n^{14}\lambda^2,
\qquad E^4m^3\ll j^5n^6h\lambda$$

holds. Using $m\ge E/(6j)$ yields respectively the second and
third terms of (4). This proves the estimate, including its rounding
and low-overlap cases; real thresholds can equivalently be rounded
after changing absolute constants.

## Consequences for bounded rarity and convex covers

The [weighted-circle theorem](weighted_circle_energy.md) implies, when
$q(A)\le n$,

$$M(A):=\max_\gamma|A\cap\gamma|
\ll n^{7/8}+R(A). \tag{9}$$

Indeed, above its absolute $C(q+1)^{7/8}$ threshold a circular subset
of size $h$ forces $R(A)\ge h/4$.

Under $R(A)\le K$, pair counting gives $q(A)\le n$ for large $n$.
Partition any convex subset into at most twelve narrow chains and
orient incident edges from that subset. Apply (4) and (9) to each
chain. If there are more than $n$ anchors on a chain, first take $n$
of them; (4) excludes this for large $n$. Thus every chain has
$O_{K,j}(n^{55/56}\lambda^{1/7})$ anchors, proving (1).

For (2), cases $R\ge\min(n/4,n^{7/8})$ already satisfy the result,
after reducing the absolute constant. If every distance is rare,
the two-anchor bound $n\le2q^2+2$ gives the result as well.
In the remaining cases pair counting gives $q(A)\le n$.
The first rich distance has rank $j\le R+1$. Select
exactly $n$ of its unordered edges. Assign each edge to one endpoint,
one of the $L$ covering convex subsets containing that endpoint,
and one of its at most twelve narrow chains. Some chain has
$n/(12L)$ assigned ordered anchors. Formula (4), with (9) and
$R\le n^{7/8}$, gives at least one of

$$n\ll L^{12}j^{17},\qquad
n\ll L^{15}j^{19}\lambda^2,\qquad
n\ll L^{56}j^{64}\lambda^8.$$

The last right side dominates the first two because $L,j,\lambda\ge1$.
Replacing $j$ by $R+1$ proves (2). One- and two-point covering sets
cause no difficulty; they enter the bounded-chain-size case of (4).

If $b$ points are uncovered, the same argument gives

$$R(A)+1\gg\min\left\{\frac{n}{b+1},
\frac{n^{1/64}}{L^{7/8}\lambda^{1/8}}\right\}. \tag{10}$$

Indeed, either $6jb>n/2$, giving the first lower bound, or at least
$n/2$ selected edges have a covered endpoint, and the same chain
argument applies. Consequently the growing-cover divergence criterion
also permits $o(n)$ exceptional points.

Finally, the patch argument in [moving frames](moving_frames.md)
uses a bad-vertex count bounded by the short incidences. Replacing its
older estimate by (1) gives complete triangular patches of radius

$$\left\lfloor c n^{1/112}\lambda^{-1/14}\right\rfloor$$

at linearly many centers in any hypothetical unbounded $R=1$ sequence.
This still does not align the different lattices or close the unrestricted
palette obstruction.

The author checked the motion multiplicity, generalized energy
estimate, absorption, geometric sums, and all displayed exponents; the
argument is author-recorded. No unrestricted conclusion follows.

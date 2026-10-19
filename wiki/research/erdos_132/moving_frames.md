---
name: research/erdos_132/moving_frames
title: Quantitative short incidences and moving triangle frames
desc: |
  Bounded rarity forces linearly many congruent rooted triangles and a
  superlinear inverse-image union; quantitative short incidences give growing lattice patches.
sources: []
research_state: closed
created: 2026-09-23T06:20:00Z
updated: 2026-10-14T00:26:52Z
---


# Quantitative short incidences and moving triangle frames

***

These are necessary conditions for hypothetical bounded-rarity sequences, not a
proof of either assertion of
[Problem 132](../../problems/distance_problems/E0132/_index.md). Constants may depend
on a fixed rarity bound $K$ or fixed distance rank. The later
[anchor-multiplicity estimate](quantitative_short_incidence.md) improves the
short-incidence exponent to $55/56$ and gives a polynomial convex-cover bound.
The earlier calculation is retained below for comparison; the patch radius uses
the improved estimate. The new
[weighted circle theorem](weighted_circle_energy.md) gives

$$M(A):=\max_{\gamma\text{ circle}}|A\cap\gamma|=O_K(n^{7/8})
\quad\text{when }R(A)\le K.$$

## Two external estimates

Write $\nu_C(g)=|C\cap gC|$ for a direct rigid motion. The estimates used are

$$
\#\{g:\nu_C(g)\ge k\}\ll |C|^3/k^2\quad(2\le k\le |C|),
\tag{1}
$$

and, for a finite $S\subset\operatorname{Aff}(\mathbb C)$,

$$
E(S)\ll V^{1/2}|S|^{5/2}+H|S|^2.
\tag{2}
$$

Here $E(S)$ counts $g_1g_2^{-1}=g_3g_4^{-1}$, and $V,H$ are the largest
intersections of $S$ with vertical and nonvertical complex lines in the
coordinates $g(z)=az+b$. These are equation (1) and Theorem 4.1 of
Mansfield--Passant, *A Structural Theorem for Sets with Few Triangles*,
[full primary paper](https://link.springer.com/article/10.1007/s00493-023-00066-z).
The author checked both full statements; (2) is their stated theorem of
Petridis--Roche-Newton--Rudnev--Warren. The use of (1) always separates
one-point overlaps, since the family of such motions can be infinite.

Strict convexity also gives

$$r_C(v)\le2\ (v\ne0),\qquad E_+(C)\le3|C|^2-2|C|,$$

as proved in [motion_incidence](motion_incidence.md).

## Quantitative rich motions on a convex set

Let $C$ be strictly convex, $|C|=m$, with at most $h$ points on any circle.
Let $S$ consist of $s=O(m)$ distinct direct motions, each having at least
$k\ge2$ overlaps with $C$. Then

$$
k^5s^2\ll m^6\log(2m)(\sqrt s+h).
\tag{3}
$$

For a fixed rotation coefficient $a$, the corresponding overlaps are
representation counts in $C-aC$. Their squared sum is
$E_+(C,aC)\le E_+(C)\le3m^2$, by Cauchy--Schwarz. Thus $V\le3m^2/k^2$.
A nonvertical line is a coset $g(x)=y$. For each $p\in C\setminus\{x\}$,
its images under the distinct motions in this coset are distinct points
of a circle centered at $y$. Hence $H(k-1)\le mh$, giving $H\ll mh/k$.
Estimate (2) now gives

$$E(S)\ll (m/k)s^2(\sqrt s+h).$$

For the reverse estimate, count pairs $(g,x)$ with $x,gx\in C$.
There are at least $ks$ such pairs. Cauchy--Schwarz over the $m$ possible
sources gives at least $k^2s^2/m$ pairs of these actions sharing a source.
For fixed $g,g'$, their number is at most $\nu_C(g'g^{-1})$.
A second Cauchy--Schwarz, grouped by this quotient, gives

$$
(k^2s^2/m)^2
\le E(S)\sum_{u\in SS^{-1}}\nu_C(u)^2.
$$

By (1) and dyadic summation, the contribution with $\nu_C(u)\ge2$ is
$O(m^3\log(2m))$; the contribution with $\nu_C(u)=1$ is at most
$s^2=O(m^2)$. Consequently
$E(S)\gg k^4s^4/(m^5\log(2m))$, proving (3).

## Quantitative short incidences

Suppose $q(A)=O(n)$, a length $r$ has fixed smallest-distance rank $\ell$, and
$E$ unordered $r$-edges touch a strictly convex subset. Partition that
subset into the bounded number of narrow chains used in
[short_incident_inverse](short_incident_inverse.md). One chain supports
$\gg E$ oriented anchors; call its size $m$. The fixed-rank degree
bound gives $m\gg E$.

In the narrow-chain proof, choose bin overload threshold $\asymp n/m$,
rather than suppressing this dependence in a constant. Each anchor
retains $\gg m$ apices, and there are $O(n^2/m)$ retained oriented
triangle types. The same two Cauchy--Schwarz counts then supply

$$
k\asymp m^3/n^2,\qquad s\asymp E m^2/n^2
\tag{4}
$$

distinct $k$-rich motions, after taking a subset of them if needed.
Here $s=O(m)$ since $E=O(m)$ by the fixed-rank degree bound.
If either expression in (4) is too small to round to the required
positive integers, then $E=O(n^{2/3})$, already below the bound below.

Substitution into (3) gives

$$
E^2m^{13}\ll\log(2n)
\left(n^{13}\sqrt E\,m+n^{14}h\right).
\tag{5}
$$

The first term, with $m\gg E$, gives
$E\ll n^{26/27}(\log(2n))^{2/27}$. The second gives
$E^{15}\ll n^{14}h\log(2n)$. Under $R(A)\le K$ the circle bound
$h\ll_K n^{7/8}$ therefore yields

$$
E\ll_{K,\ell} n^{119/120}(\log(2n))^{1/15}.
\tag{6}
$$

The constants are uniform over the convex subset and any fixed finite
set of smallest-distance ranks.

Counting the multiplicity of each motion more carefully, rather than
retaining just $O(m)$ motions, now gives the stronger bound

$$E\ll_{K,\ell}n^{55/56}(\log(2n))^{1/7}. \tag{6a}$$

The complete proof, including the rank dependence and one-point quotient
overlaps, is in
[quantitative short incidences](quantitative_short_incidence.md).

## Growing patches when there is only one rare distance

Use the established [one-rare reduction](one_rare_asymptotics.md), with
minimum separation normalized to one and
$I=A\setminus(L_1\cup L_2)$. Let $b$ be the number of vertices of $I$
having fewer than six unit neighbors in $I$. Since $|I|<n/3$ and

$$e_1(I)\le3|I|-b/2,$$

richness of the minimum distance implies
$b<2e_1(L_1\cup L_2,A)$. Formula (6a) bounds $b$ by its right-hand side.

Eventually every whole minimum-distance component lies in a triangular
lattice, by the previously proved exact spectrum through length two.
A radius-$L$ graph ball in such a lattice has $O(L^2)$ vertices. Thus
only $O(bL^2)$ interior vertices lie within graph distance $L$ of a bad
vertex. The others have complete radius-$L$ triangular patches.
For sufficiently small fixed $c>0$, take

$$
L=\left\lfloor c n^{1/112}(\log(2n))^{-1/14}\right\rfloor.
\tag{7}
$$

There are then $\gg n$ complete-patch centers. This improves the earlier
fixed-radius statement to a polynomially growing radius. It still does
not align the different patches.

For completeness, in any point-stabilizer coset of these canonically
oriented patch frames there are $O(n/L^2)$ frames. Such a coset contains
at most one frame of each orientation. Two radius-$\lfloor L/2\rfloor$
subpatches with different orientations cannot intersect: a shared point
has a complete unit hexagon in both larger patches, whose directions
must agree since the global minimum distance is one. These subpatches
are therefore disjoint, each containing $\gg L^2$ points.

## Many congruent triangles for every bounded rarity

Assume now only $R(A)\le K$ along an unbounded sequence. There are
$\alpha_K,\beta_K>0$, a strictly convex $C\subset A$ with
$|C|\ge\alpha_Kn$, a noncollinear rooted triangle $T_n$, and at least
$\beta_Kn$ direct isometries $g$ such that

$$gT_n\subset A\setminus C,$$

with all roots $g(0)$ distinct.

Indeed the [rank-layer bound](layers_and_obstructions.md) gives a convex
layer of size at least $\alpha_Kn$, where
$\alpha_K=1/((K+1)(2K+1))$. Choose a rich length among the first
$K+1$ smallest lengths. Its graph has maximum degree
$D_K=6(K+1)$, and only $o(n)$ edges touch $C$, by (6), or already by
the qualitative short-incidence theorem. Its induced graph on
$A\setminus C$ therefore has at least $n-o(n)$ edges. At least
$\alpha_Kn/(D_K-2)$ vertices have degree at least three, since otherwise
the degree sum is less than
$2(n-|C|)+(D_K-2)\alpha_Kn/(D_K-2)$.

There are $O_K(1)$ lengths at most $2r$. A radius-$2r$ disk is covered
by $196$ squares of side $r/3$; each square has diameter less than $r$,
hence at most $K$ internal lengths, and at most $2(K+1)^2$ points by
the two-anchor bound. Thus the total number of pairs of length at most
$2r$ is at most $196(K+1)^2n$. Since all but at most $K$ such lengths
are rich, there are at most
$J_K=K+196(K+1)^2$ occurring lengths in this interval.

Choose at each degree-three root two noncollinear $r$-neighbors.
Pigeonhole their base length among these $J_K$ possibilities, then
order the neighbors counterclockwise. This supplies
$\beta_Kn$ directly congruent triangles with distinct roots.
The triangle $T_n$ may vary with $n$ and may approach degeneracy;
no contrary uniformity claim is made.

## Expansion of the inverse-image union

More generally, let $|C|\ge\alpha n$ be strictly convex and let $G$
contain at least $\beta n$ direct motions with distinct roots $g(0)\in A$.
Put

$$
U=\bigcup_{g\in G}g^{-1}C,\qquad N=|U|,\qquad M=M(A).
$$

Then

$$
N^2(\sqrt N+M)\gg_{\alpha,\beta}\frac{n^3}{\log(2n)}.
\tag{8}
$$

To prove this, put $m=|C|$, $p=|G|\le n$. A same-orientation fiber with
$v$ roots $B$ contributes a rotated copy of $C-B$ to $U$. Convex
difference multiplicities and Cauchy--Schwarz give

$$
N\ge |C-B|\ge\frac{m^2v}{m+2v-2};
$$

hence $V\ll_\alpha N/n$. A nonvertical line $b=\lambda a+\mu$ in
motion coordinates puts its distinct roots on
$|b-\mu|=|\lambda|$ if $\lambda\ne0$; if $\lambda=0$ it contains at
most one root. Thus $H\le M$. Applying (2) gives

$$E(G)\ll_\alpha n^2(\sqrt N+M).$$

On the other hand, if $r(z)=|\{g:z\in g^{-1}C\}|$, then

$$
I:=\sum_zr(z)^2
=\sum_u r_{GG^{-1}}(u)\nu_C(u)
\ge\frac{m^2p^2}{N}.
$$

Cauchy--Schwarz and (1), again including at most $p^2$
one-point quotient overlaps, give

$$E(G)\gg_{\alpha,\beta}\frac{n^5}{N^2\log(2n)}.$$

This proves (8). Under bounded rarity $M\ll_K n^{7/8}$, so

$$
N\gg_K
\min\left\{
\frac{n^{6/5}}{(\log(2n))^{2/5}},
\frac{n^{17/16}}{\sqrt{\log(2n)}}
\right\}
\gg_K\frac{n^{17/16}}{\sqrt{\log(2n)}}.
\tag{9}
$$

Apply this to the triangle frames above. Every $z\in U$ has all three
distances to $T_n$ in $D(A)\cup\{0\}$. The checked uniform three-anchor
theorem in [translated_triangles](translated_triangles.md) gives only
$N=O_K(n^{12/7})$, using the updated Solymosi--Zahl input there.
The two exponents are compatible. No stronger
many-anchor estimate sufficient to contradict (9) was proved.

Collinear anchors alone cannot provide one: for fixed $L$, take
$z_{x,k}=(x,\sqrt{R^2+k-x^2})$, $1\le x\le M_0$, $0\le k\le M_0$,
and $R>(2L+2)M_0$. The squared distances to $(j,0)$,
$0\le j\le L$, are $R^2+k-2jx+j^2$. They occupy only $O_L(M_0)$
values for $\Theta(M_0^2)$ distinct points.

There is a restricted many-anchor improvement: if the squared
palette is covered by $r$ progressions of at most $Q$ terms, the
[uniform ellipse argument](arithmetic_palettes.md) gives
$N\ll_\varepsilon(q+1)r^2Q^\varepsilon$ and
$M(A)\ll_\varepsilon r^2Q^\varepsilon$. Combined with (8), it forces
$r\ge n^{1/10-o(1)}$ when $Q$ is polynomial in $n$. This does not
control an arbitrary palette.

The author checked the displayed derivations, the external statements,
the fixed-rank uniformity, the growing-patch argument, the circle
improvement, and the two quantitative energy calculations; the
arguments are author-recorded. These results do not close the
unrestricted gap.

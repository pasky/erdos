---
name: research/erdos_132/independent/layer_bound_and_circular_majority
title: Independent notes on Erdős Problem 132
desc: |
  Archived unverified input; the elementary additive and circle bounds
  were checked, while its layer, finite, and convex scopes are superseded.
sources: []
created: 2026-09-23T06:48:25Z
updated: 2026-09-24T22:12:56Z
---


# Independent notes on Erdős Problem 132

***

## Status and provenance

Neither assertion has been proved or disproved here for arbitrary planar point
sets. In particular, the results below are not a resolution of the problem. They
give finite-order cases, extensions of the convex case, quantitative asymptotic
results for several families, and explicit restrictions on a hypothetical
counterexample.

Only the supplied problem page and papers were consulted. No web search was
made, and no earlier research notes were used. The proofs developed during this
investigation are recorded in the files linked below.

Throughout, $A\subset\mathbb R^2$ consists of $n\ge5$ distinct points,


$$
m_A(r)=\#\{\{x,y\}\subset A:|x-y|=r\},\qquad
R(A)=\#\{r:1\le m_A(r)\le n\}.
$$


All multiplicities count unordered pairs. Write $d(A)$ for the number of
distinct positive distances and list them in decreasing order as


$$
d_1>d_2>\cdots>d_{d(A)}.
$$


## 1. Summary of established results

1. **Small orders:** $R(A)\ge2$ for every $5\le n\le10$. The proof uses
   the supplied few-distance classifications, with explicit coordinates and
   checked multiplicity tables for all four nine-point four-distance types.
   The complete finite-order proof is not retained.

2. **Almost convex sets:** $R(A)\ge2$ if the convex hull has $n-1$
   vertices. Together with the supplied convex-set theorem, this covers hull
   size at least $n-1$. Also, $R(A)\ge2$ if the hull is cocircular and has
   $n-2$ vertices. The separate proofs are not retained. The latter
   statement needs cocircularity; it has not been extended to all hulls with
   $n-2$ vertices.

3. **Convex layers:** Let $L_i$ be the successive convex layers, removing
   only hull vertices at each step, and put $s_k=|L_1\cup\cdots\cup L_k|$.
   Then

   $$
   \boxed{m_A(d_k)\le(6k-5)s_k.}
   \tag{1}
   $$

   Thus, if every layer has size at most $H$,

   $$
   \boxed{R(A)\ge
   \max\left\{1,\left\lfloor\sqrt{\frac n{6H}}\right\rfloor\right\}.}
   \tag{2}
   $$

   In particular, maximal layer size $o(n)$ implies $R(A)\to\infty$.
   These statements have elementary proofs, given below; the separate
   layer write-up is not retained.

4. **Diameter and separation:** If $\Delta$ is the diameter and
   $\delta$ is the minimum separation, then

   $$
   \boxed{R(A)\ge
   \max\left\{1,\left\lfloor
   \sqrt{\frac{\delta n}{6\pi\Delta}}
   \right\rfloor\right\}.}
   \tag{3}
   $$

   Hence $\Delta/\delta=o(n)$ implies divergence. In particular,
   $\Delta/\delta=O(\sqrt n)$ gives $R(A)=\Omega(n^{1/4})$.

5. **Regular-polygon subsets:** If $m$ points of $A$ belong to the
   vertices of a regular $M$-gon, then

   $$
   \boxed{R(A)\ge m-\frac n2-27M^{2/3}-18.}
   \tag{4}
   $$

   Thus a fixed majority lying in a regular polygon of order $O(n)$
   forces linearly many rare distances, even when all remaining points are
   arbitrary. The proof uses an elementary bound for lattice points on a
   strictly convex graph, not a genericity assumption. The full
   incidence and transfer proof is not retained.

The circular-set write-up, linked in Section 5 below, strengthens the last
conclusion to a fixed majority on an arbitrary circle.

## 2. Counting and the finite-order argument

The diameter theorem gives $R(A)\ge1$. A general pair count gives


$$
\binom n2\ge (d(A)-R(A))(n+1)+R(A),
$$

and therefore

$$
R(A)\ge
\left\lceil\frac{(n+1)d(A)-\binom n2}{n}\right\rceil.
\tag{5}
$$


In particular, if $R(A)=1$, every distance except the diameter has
multiplicity at least $n+1$, so


$$
(d(A)-1)(n+1)+1\le\binom n2,
\qquad d(A)\le\lfloor n/2\rfloor.
\tag{6}
$$


For $n=2k$, the case $d(A)=k$ forces equality:


$$
m_A(d_1)=1,\qquad m_A(r)=2k+1\quad(r\ne d_1).
\tag{7}
$$


Erdős--Fishburn (1996), Theorem 1, supplies
$g(2)=5$, $g(3)=7$, and $g(4)=9$, together with the relevant
maximum-set classifications. Under (6), for $5\le n\le10$ there must be
exactly $\lfloor n/2\rfloor$ distances. The odd orders reduce to:

| Number of points | Classified types | Unordered multiplicities |
|---|---|---|
| 5 | Regular pentagon | $5,5$ |
| 7 | Regular heptagon; regular hexagon and center | $7,7,7$; $12,6,3$ |
| 9 | Four types | $9,9,9,9$; $16,9,7,4$; $15,9,6,6$; $18,6,6,6$ |

Every row has at least two multiplicities at most its number of points.

For even $n=6,8,10$, delete either endpoint of the unique diameter in
(7). Each deletion is an odd-order set in the preceding table. Every
nonregular candidate has a multiplicity exceeding $n+1$, so both deletion
sets must be regular polygons. They share at least three vertices. These
vertices identify their common circumcircle, and one common vertex then
identifies the entire regular polygon of the specified order. Thus the two
deletion sets coincide, contrary to the endpoints being distinct.

The coordinate and displacement tables that made the nine-point check
independent of missing source figures are not retained. In particular,
the exceptional representative is


$$
\{a\omega^j:a\in\{1,1+\sqrt3,-2-\sqrt3\},\ j=0,1,2\},
\qquad \omega=e^{2\pi i/3}.
$$


Its squared distances $3,6+3\sqrt3,12+6\sqrt3,21+12\sqrt3$
have multiplicities $6,18,6,6$, respectively.

This finite argument stops at $n=10$. A hypothetical eleven-point
counterexample would have exactly five distances and diameter multiplicity
at most seven. The supplied uniqueness theorem for twelve-point five-distance
sets does not classify eleven-point five-distance sets.

## 3. A proof of the layer bound

### 3.1. Distance rank controls layer depth

If $p\in L_i$, $q\in L_j$, and $|p-q|=d_k$, then


$$
i+j\le k+1.
\tag{8}
$$


Indeed, if $i>1$, express $p$ as a nontrivial convex combination of
vertices of $L_{i-1}$. Strict convexity of $x\mapsto|x-q|^2$
gives a vertex $p'\in L_{i-1}$ with $|p'-q|>|p-q|$.
Repeat through all preceding layers, then move $q$ outward in the same
way. This creates $i+j-2$ strict increases among distances of $A$.
At most $k-1$ distinct distances exceed $d_k$, proving (8).

In particular, every $d_k$-edge lies in the first $k$ layers. This
argument also handles nonvertices on hull edges and collinear layers.

### 3.2. A rank-$k$ distance has only linearly many pairs

We prove for every $N$-point planar set $B$, and its $k$-th largest
distance $r$, that


$$
m_B(r)\le(6k-5)N.
\tag{9}
$$


Let

$$
C=\{x\in B:|x-p|\le r\text{ for every }p\in B\},
\qquad E=B\setminus C.
$$


Fix $q\in B$, and put $S=\{x\in B:|x-q|=r\}$. For each
$p\ne q$, the radius-$r$ disk centered at $p$ cuts the radius-$r$
circle centered at $q$ in a closed arc $I_p$ of angular length strictly
less than $\pi$, a point, or the empty set. At most $2(k-1)$ points
of $S$ lie outside $I_p$: their distances to $p$ exceed $r$, and
each of the $k-1$ possible larger-distance circles centered at $p$
meets the circle centered at $q$ in at most two points.

A family of closed arcs of length less than $\pi$ has these elementary
properties:

* A nonempty intersection is determined by at most two arcs. Cut at the
  antipode of a common point and use the largest left endpoint and smallest
  right endpoint of the resulting intervals.
* An empty intersection is witnessed by at most three arcs. Fix one arc
  $I_0$. Its intersection with each other short arc is an interval in
  $I_0$, possibly empty. If none is empty, two of these intervals are
  already disjoint by the interval intersection property.

Consequently, with $J=\bigcap_{p\ne q}I_p$, either at most
$4(k-1)$ points of $S$ lie outside $J$, or $J$ is empty and
$|S|\le6(k-1)$. Since $S\cap J=S\cap C$, in both cases


$$
\#\{x\in E:|x-q|=r\}\le6(k-1).
$$


Sum over $q$. Every $r$-edge not entirely in $C$ is counted at
least once, so there are at most $6(k-1)N$ such edges. Edges entirely
in $C$, if any, are diameter edges of $C$, hence number at most
$|C|\le N$. This proves (9).

### 3.3. Localization and consequences

By (8), the first $k$ distances and every occurrence of $d_k$ are
present in $L_1\cup\cdots\cup L_k$. Applying (9) there proves (1).
If


$$
(6k-5)s_k\le n,
\tag{10}
$$


all the first $k$ distances are rare. For $k\ge2$, (10) implies
$s_k<n$; a point in a deeper layer and (8) guarantee that these
distances exist. For $k=1$, the diameter suffices.

If each layer has at most $H$ points, take
$k=\lfloor\sqrt{n/(6H)}\rfloor$. Then
$(6k-5)s_k\le6k^2H\le n$, proving (2).

For a nondegenerate layer with $h$ vertices and perimeter $P$,
$h\delta\le P\le\pi\Delta$. The last inequality follows by integrating
the widths of a convex polygon; a proof was included in the layer
write-up, which is not retained.
A degenerate layer has at most two vertices, also at most
$\pi\Delta/\delta$. Thus $H\le\pi\Delta/\delta$, proving (3).

An exact remaining restriction is worth recording. If $R(A)\le K$,
then


$$
s_{K+1}>\frac{n}{6K+1}.
\tag{11}
$$


Otherwise (10) would give $K+1$ rare distances. Therefore some one of
the first $K+1$ convex layers has more than


$$
\frac{n}{(K+1)(6K+1)}
$$


vertices. This is a necessary condition, not a contradiction.

## 4. Why a regular-polygon subset survives arbitrary added points

Here is the mechanism behind (4); the complete calculations are not
retained.

On a circle containing a regular $M$-gon, every chord-distance graph has
degree at most two. For a subset $B$ of $m$ vertices, consequently
$m_B(r)\le m$ and $B$ determines at least $\lfloor m/2\rfloor$
distances.

For a point $q$ not among the ambient polygon's vertices and not its
center, at most


$$
J(M)=27M^{2/3}+17
$$


vertices $v$ can have $|q-v|$ equal to any chord length of that
polygon. To see this, normalize the circumradius to one and write
$q=\rho(\cos\phi,\sin\phi)$. For $\rho\notin\{0,1\}$, the
incidence equation is


$$
\cos(2\pi k/M)=\frac{1-\rho^2}{2}
 +\rho\cos(2\pi j/M-\phi).
$$


Its inverse-cosine graph, with integer coordinates ((j,k)), splits into
at most nine strictly convex or concave pieces after at most eight exceptional
points are removed. The second derivative has a nonzero quadratic numerator
in $\cos(2\pi j/M-\phi)$, so this splitting is uniform in $q$.
Each piece lies in a rectangle of width $M$, height $M/2$.
Successive lattice-point differences have distinct slopes and total
$\ell^1$-length at most $2M$; counting integer vectors of length at
most $M^{1/3}$ gives at most $3M^{2/3}+1$ points per piece.
If $\rho=1$, equality would make $q$ an ambient polygon vertex,
which was excluded. The center affects only the circumradius class.

Take $B=A\cap P_M$, where $P_M$ is the ambient vertex set, and put
$t=n-m$. Discard at most the one center-related distance. All other
chord classes together receive at most


$$
tJ(M)+\binom t2
$$


new pairs. A chord class that becomes rich must receive at least $t+1$
new pairs, since its old multiplicity was at most $m$. Hence


$$
R(A)\ge\left\lfloor\frac m2\right\rfloor-1
-\frac{tJ(M)+\binom t2}{t+1},
\tag{12}
$$


which implies (4). This calculation addresses the subset-to-whole-set
transfer explicitly; merely finding a rare distance inside $B$ would not
suffice.

## 5. Circular sets and the additive argument

The regular-polygon method extends to a majority on an arbitrary circle.
The self-contained proof and its additive lemma were written in companion
files that are not retained; the mechanism is given in Section 8 below. It
establishes


$$
\boxed{R(A)\ge h-\frac n2-10n^{6/7}}
\tag{13}
$$


whenever a circle contains $h$ points of $A$. In particular,
$h\ge(1/2+\varepsilon)n$ gives
$R(A)\ge\varepsilon n-10n^{6/7}$.

The argument is structural, not a deformation of the points. If the angular
set $S\subset\mathbb R/\mathbb Z$ has too many differences, (5) already
forces many rare distances. Otherwise an elementary minimal-expansion-set
argument produces a finite subgroup of order $M\ge2|S|-|S-S|$.
Both $S$ and (S-S) lie in boundedly many cosets when the circular
majority is fixed. Each coset is a shifted regular angular grid, so the same
convex-graph incidence bound and pair-budget transfer apply. Keeping track
of the coset counts yields the error $O(n^{6/7})$ in (13).

No theorem on small sumsets is being imported without proof: the
minimal-expansion-set argument, including the finite-group boundary case,
is proved in the linked files.

## 6. Source use and exact unresolved gaps

The following supplied passages were read before their results were used:

* Erdős (1946), Section 4 and Theorem 3: the diameter multiplicity bound.
* Erdős--Fishburn (1995), Theorem 2 and Section 5/Theorem 5: the original
  five- and six-point cases and the exact unordered-pair convention.
* Erdős--Fishburn (1996), Theorem 1 and the accompanying few-distance
  classifications: the finite-order proof.
* Fishburn (1995), Theorems 1--3: the convex minimum-distance count and
  equality classifications used for hull size $n-1$.
* Shinohara (2008), Theorems 1.1 and 1.2$b$: confirmation of the nine-point
  classification and uniqueness of the twelve-point five-distance set.
* Clemen--Dumitrescu--Liu (2025), Sections 1.1 and 2: the convex and
  first-two-layer conclusions and their proofs. Its Theorem 1.3 in the
  supplied **source**, rather than the inconsistent digest transcription,
  uses

  $$
  \min\{\tfrac32(h_1+h_2),\tfrac43h_1+2h_2,2h_1+h_2\}\le n.
  $$

* Bhowmick (2024), Section 2: rich-distance constructions. These do not
  give configurations with only one, or only boundedly many, rare distances.

The two unrestricted questions remain beyond the arguments above. The
specific obstacles are:

* A sequence with bounded $R(A)$ can still have a linear-sized convex
  layer, as required by (11), without having a majority on any circle.
  No reduction established here forces that layer to be regular or
  cocircular.
* Fishburn's exact equality classifications cannot be extended, without a
  proof, to all convex sets whose distance count is a bounded amount above
  the minimum. Even the asymptotic assertion for arbitrary convex sets is
  not proved here.
* Rare distances in a selected subset can gain many pairs involving the
  remaining points. The transfer estimate (12) controls this only for its
  stated circular structures; it is not valid for an arbitrary convex
  subset.
* The second-largest distance need not itself be rare. Its source bounds,
  or the much weaker general rank bound (9), cannot replace a search for
  another distance at the exact threshold $n$.

Thus there is neither a general counterexample nor a complete general proof
in this write-up. The proved partial results and their assumptions are the
claims to retain.

## 7. Additional calculations and the almost-convex proofs

### 7.1. Exact small examples

The restriction $n\ge5$ is essential. The four points

$$
(0,0),\quad(1,0),\quad(1/2,\sqrt3/2),\quad(1/2,-\sqrt3/2)
$$

have five unit pairs and one pair at distance $\sqrt3$. Thus $R=1$
at $n=4$, not in the requested range.

There is an eight-point example with $R=2$. Put $a=1+\sqrt3$ and take

$$
\{(\pm1,\pm1)\}\cup\{(0,\pm a),(\pm a,0)\}.
$$

Its squared distances and multiplicities are

$$
\begin{array}{c|rrrr}
r^2&4&8&8+4\sqrt3&16+8\sqrt3\\\hline
m(r)&12&2&12&2.
\end{array}
$$

The first class comprises four square sides and eight pairs to nearer outer
points; the second comprises two square diagonals; the third comprises four
adjacent outer pairs and eight pairs to farther square corners; the last
comprises two opposite outer pairs. The counts sum to 28.

The unique twelve-point five-distance type has squared-distance multiplicities

$$
\begin{array}{c|rrrrr}
r^2&1&3&4&7&9\\\hline
m(r)&24&15&12&12&3.
\end{array}
$$

An explicit triangular-lattice representative and complete displacement counts
were recorded in a companion file that is not retained. Removing its point
((0,-2)), in the axial coordinates used there, subtracts degrees
((6,3,2,0,0)). The resulting eleven-point set has multiplicities
((18,12,10,12,3)), hence $R=2$. This is an example, not a proof of the
universal assertion for eleven points.

The triangular-lattice nine-point representatives used in Section 2 are,
with squared norm $i^2+ij+j^2$,

$$
\begin{aligned}
P={}&\{(0,0),(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1),(1,1),(2,-1)\},\\
Q={}&\{(0,1),(0,2),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(3,0)\}.
\end{aligned}
$$

At squared lengths $1,3,4,7$, their multiplicities are respectively
((16,9,7,4)) and ((15,9,6,6)). These counts, together with the explicit
three-triangle configuration in Section 2, establish four nonsimilar
nine-point four-distance sets including $R_9$. The supplied classification
allows at most four types, so no identification from absent pictures is needed.

### 7.2. Why one nonvertex can be handled

Let $H$ now denote the hull vertex set, $h=|H|$, and suppose $h=n-1$.
A nonvertex cannot be a diameter endpoint: its expression as a nontrivial
convex combination of hull vertices, and strict convexity of squared distance,
would give a strictly longer pair.

If $H$ is cocircular with center $O$, and its one remaining point $p$
is not $O$, every distance from $p$ is attained by at most two hull
vertices. None is the diameter. Consequently

$$
d(A)\ge\left\lceil\frac h2\right\rceil+1
>\lfloor n/2\rfloor,
$$

contradicting (6) under $R=1$. If $p=O$, adding $p$ changes just the
circumradius class. For $n\ge7$, the hull has at least three distance
classes, each of multiplicity at most $h$, so at least two stay rare.

It remains to justify cocircularity, rather than assume it. For odd
$n=2k+1\ge9$, (6) and the convex distinct-distance lower bound force
$H$, a convex $2k$-gon, to have exactly $k$ distances. Fishburn's
even equality classification makes $H$ cocircular.

For even $n=2k\ge10$, a convex $H$ of size $2k-1$ has either
$k-1$ or $k$ distances. In the former case it is regular by the odd
equality classification. In the latter case $A$ has $k$ distances,
so (7) gives a unique diameter pair $a,b\in H$. Each of
$H\setminus\{a\}$ and $H\setminus\{b\}$ is a convex
$(2k-2)$-gon with exactly $k-1$ distances. Both are cocircular by
Fishburn's even equality classification. They share at least three
noncollinear points, so their circles coincide and $H$ is cocircular.
For $n=8$, Fishburn's classification of convex heptagons with four
distances supplies the same conclusion. Smaller cases follow from the
finite-order proof.

### 7.3. Two nonvertices require a separate argument

Suppose the hull is cocircular and has $h=n-2$ vertices, with remaining
points $p,q$. At least one is not the circle center. For odd $n$, its
distances to the hull already give
$d(A)\ge\lceil h/2\rceil+1>\lfloor n/2\rfloor$, excluding $R=1$.

For even $n=2k\ge8$, assuming $R=1$ instead forces $d(A)=k$, a
unique diameter, and exactly $k-1$ nonmaximal classes of multiplicity
$n+1$. If one of $p,q$ is the center, a nonmaximal class different from
the circumradius and (|p-q|) receives at most $h+2=n$ pairs, a
contradiction. There are at least three nonmaximal classes, so such a choice
exists.

If neither point is the center, each sees every nonmaximal distance exactly
twice among the $h=2k-2$ hull vertices. Reflection in the line joining the
center to $p$ therefore preserves the hull and fixes no hull vertex;
likewise for $q$. Both reflections must swap the endpoints of the unique
diameter, so their axes coincide. In coordinates with this axis horizontal,
write $p=(t,0)$, $q=(s,0)$, and the hull as
$(x_i,\pm y_i)$, where $x_i^2+y_i^2=\rho^2$. The numbers $x_i$
are distinct. Equality of the two sets of squared distances says that
$X=\{x_i\}$ is preserved by

$$
x\longmapsto \frac tsx+\frac{s^2-t^2}{2s}.
$$

The diameter of a finite real set with at least two elements is preserved
only if $|t/s|=1$. Since $p\ne q$, $s=-t$, and this map is
$x\mapsto-x$. Thus the hull is centrally symmetric and has several
antipodal diameter pairs, contradicting uniqueness.

Without cocircularity, this two-nonvertex argument is unavailable. The
unhandled convex hulls have one more distance than the classified minimum;
no classification of that regime for all orders was proved here.

## 8. Detailed mechanism of the circular-majority theorem

The following records the delicate steps of (13), so the result is not merely
a reference to a proposed structural lemma.

### 8.1. The additive lemma and its finite-group issue

Let $S\subset\mathbb R/\mathbb Z$ be finite, $a=|S|$,
$b=|S-S|<2a-1$. Translate $S$ to contain zero and work in
$G=\langle S\rangle$. If $S-S=G$, the group is finite and can itself
be used below. Otherwise, for nonempty finite $X$ with $X+S\ne G$,
minimize

$$
f(X)=|X+S|-|X|.
$$

Its minimum $\kappa$ exists and satisfies
$\kappa\le b-a<a-1$, by taking $X=-S$. Choose a minimizer $U$
of least size and translate it to contain zero.

The inequality

$$
f(X\cap Y)+f(X\cup Y)\le f(X)+f(Y)
$$

follows directly from intersections and unions of sumsets. To apply it to
two intersecting translates of $U$, their union must still be admissible.
This is automatic when $G$ is infinite. When $G$ is finite, the
exterior $G\setminus(U+S)$ is a minimizer for expansion by (-S),
and reflection makes it a minimizer for expansion by $S$. This follows
from the inclusions

$$
\bigl(G\setminus(X+S)\bigr)-S\subseteq G\setminus X
$$

and equality of the two minimum expansion values. Minimality of (|U|)
then gives $|G|\ge2|U|+\kappa$.

If the neighborhoods of intersecting translates $U,V$ covered $G$,
their intersection would have at most $\kappa$ elements. But it
contains a translate of $S$, of size $a>\kappa$, a contradiction.
Thus the union is admissible. Submodularity now makes $U\cap V$ a
minimizer, so minimal cardinality forces $U=V$. In particular
$U+u=U$ for each $u\in U$; hence $U$ is a finite subgroup $H$.

Put $M=|H|$, and let $k$ be the number of $H$-cosets met by $S$.
Then $\kappa=(k-1)M$, and

$$
M\ge2a-b.
$$

The total number $u=kM-a$ of missing elements in these cosets satisfies
$u<M$. Two different occupied fibers have sizes summing to more than
$M$, so their differences fill the corresponding entire $H$-coset.
At least one fiber has more than $M/2$ elements, so its self-difference
fills $H$. Therefore (S-S) is a union of complete $H$-cosets.
Since

$$
b\ge a+\kappa=(2k-1)M-u>(2k-2)M,
\qquad b<2a\le2kM,
$$

divisibility by $M$ forces

$$
b=(2k-1)M,\qquad u<M/2.
\tag{14}
$$

The case $S-S=G$ satisfies the same conclusion with $k=1$.

This proves the needed small-difference structure without invoking an
unprovided additive-combinatorics theorem. A finite subgroup of
$\mathbb R/\mathbb Z$ of order $M$ is the regular angular grid
$\{j/M:0\le j<M\}$.

### 8.2. Shifted angular grids and the incidence constant

Let $B=A\cap C$, $|B|=h$, and normalize $C$ to the unit circle.
Suppose the angular set $S$ lies in $k$ cosets of an order-$M$
subgroup and (S-S) lies in $l$ cosets of that subgroup. An off-circle,
noncentral point $q$ has at most

$$
F=kl(27M^{2/3}+17)
\tag{15}
$$

incidences into $B$ whose lengths occur within $B$.

For a source coset $\alpha+H$ and a target difference coset
$\beta+H$, choose principal angular differences in ([0,1/2]).
This is valid because (S-S) is symmetric under negation. The incidence
equation has the integer-coordinate graph

$$
v=\frac{M}{2\pi}\arccos\!\left(
\frac{1-\rho^2}{2}+\rho\cos(2\pi(\alpha+j/M)-\phi)
\right)-M\beta.
$$

The horizontal interval has length less than $M$; the vertical interval
has length at most $M/2$. Thus the proof of $J(M)$ in Section 4
applies to each pair of cosets. Using principal angles is important: it
avoids an unnecessary extra factor for the branches of cosine.

Since $B$ includes every point of $A$ on $C$, no off-circle point
falls into the degenerate case $\rho=1$. The center, if present,
affects only one distance class, which is discarded. The old chord classes
then receive at most $tF+\binom t2$ new unordered pairs, where $t=n-h$.
Consequently, exactly as in (12),

$$
R(A)\ge h-\frac n2-F-1.
\tag{16}
$$


### 8.3. The exponent (6/7)

Write $s=R(A)$ and $y=h-n/2-s$. The pair count (5) implies

$$
|S-S|\le2d(A)+1\le n+2s.
$$

If $y>1/2$, the additive lemma applies and gives

$$
M\ge2y,\qquad l=|S-S|/M=2k-1,\qquad k\le l.
$$

Also $|S-S|<2n$. Thus (15) gives

$$
F\le44\left(\frac{|S-S|}{M}\right)^2M^{2/3}
\le \frac{176n^2}{(2y)^{4/3}}.
$$

By (16), $y\le F+1$. For $y\ge2$, therefore,

$$
y^{7/3}\le\frac{352}{2^{4/3}}n^2
<10^{7/3}n^2,
$$

which gives $y<10n^{6/7}$. The cases $y<2$ are immediate. This is
the claimed bound (13). No asymptotic estimate is used to disguise a missing
transfer inequality.

## 9. Other approaches tried, and what failed

### Counting alone

The inequality (5) is useful when the number of distances exceeds roughly
$n/2$. It does not prove the problem for arbitrary sets: the supplied
lattice constructions have far fewer than $n/2$ distinct distances for
large orders. A lower bound tending to infinity on the total number of
distances does not force the number of rare ones to tend to infinity.

### Taking the next-largest distance

The supplied second-largest-distance bound is $3n/2$, not $n$, and
examples can exceed $n$. Clemen--Dumitrescu--Liu, Proposition 1.5 and its
proof, were read: the minimum distance and the second-largest distance can
both have multiplicity $9n/8+o(n)$. Selecting just those two candidates
therefore cannot yield a universal proof. The rank estimate (9) succeeds
only after sufficiently strong support localization; on a convex set it
gives $(6k-5)n$, which is too large as soon as $k\ge2$.

### An earlier, weaker support bound

Before the disk-core argument, the two-circle intersection property gave
a fully elementary bound for a distance graph on $s$ vertices:

$$
\sum_v\binom{\deg(v)}2\le2\binom s2.
$$

If it has $e$ edges, Cauchy--Schwarz gives

$$
\frac{2e^2}{s}-e\le s(s-1),
\quad
e\le U(s):=\frac{s}{4}\bigl(1+\sqrt{8s-7}\bigr)\le s^{3/2}.
$$

Combined with layer localization, $s_k\le n^{2/3}$ makes the first
$k$ distances rare. If all layers have at most $H$ vertices, this gives
$R(A)\ge\lfloor n^{2/3}/H\rfloor$. It remains useful for very small
$H$, but only proves divergence when $H=o(n^{2/3})$.

The source-quoted unit-distance bound $O(s^{4/3})$, explicitly stated in
Clemen--Dumitrescu--Liu Section 1.4, similarly gives
$R(A)\ge\lfloor c n^{3/4}/H\rfloor$ for an absolute $c>0$.
Its proof was not supplied there and was not independently recreated.
The stronger qualitative conclusion $H=o(n)\Rightarrow R(A)\to\infty$
instead follows from the self-contained disk-core proof, without this quoted
incidence theorem.

### A much less efficient fixed-rank proof

An independent alternative was developed before the disk-core proof:
pairwise disjoint equal-length segments force a longer endpoint distance.
Color each pair of such segments by an endpoint choice and one of the
$k-1$ larger lengths. A monochromatic five-segment configuration would
give three common points of two distinct circles, so a finite Ramsey bound
limits the number of disjoint segments. A vertical-line decomposition then
bounds the edges by a constant depending on $k$ times the vertex count.

This gives a valid but very inefficient constant, for example

$$
C_k=3\big((4(k-1))^{16(k-1)+2}-1\big)^4\quad(k\ge2).
$$

The proof is not retained.
It is superseded for the present application by $C_k=6k-5$, not used as
an unproved intermediate step.

### Subsets and deleting diameter endpoints

Deleting endpoints of a unique diameter works at $n=6,8,10$ because
the resulting odd-order few-distance sets are classified and their
multiplicities can be compared with the original threshold. It does not
give an induction for arbitrary $n$. At twelve points, the corresponding
deletions have eleven points and five distances, a class not classified by
the supplied sources. Similarly, a diameter-independent subset may have
rare distances that gain many pairs when the deleted points are restored.
No unrestricted transfer bound was established.

### Near-minimal convex distance counts

The convex theorem and the one-nonvertex extension use exact minimum
distance counts. For hull size $n-2$, the remaining case is generally one
above that minimum. Assuming these hulls are automatically cocircular would
be a gap. Fishburn's introduction explicitly distinguishes exact equality
from the broader near-minimum classification problem. A stability theorem
strong enough to deal with bounded excess was considered as a possible
route, but no such theorem was proved here.

### Algebraic and deformation considerations

Equal-distance constraints can be written as equations between squared
lengths; merely noting their algebraic form supplied no useful inequality
at the exact threshold $n$. An affine or generic perturbation can split
one rich distance into many rare distances, so proving a statement after
such a perturbation would not prove it for the original configuration.
No generic-deformation extension, field-embedding argument, or unseen
number-field note was used in any claim of this record.

## 10. Proof status and checks

The layer-rank lemma, short-arc argument, exact pair budgets, circle-grid
incidence estimate, and additive-atom lemma all have proofs in this record
or the linked detailed files. Particular checks were made of the following
delicate points:

* A layer step uses strict convexity even when a point is on a hull edge,
  and strictly increasing lengths cannot introduce coincident endpoints.
* The disk-center $p=q$ is omitted from the circle-intersection count;
  for every other center the circles really are distinct.
* Short arcs have length strictly less than a semicircle; empty and
  singleton arcs are allowed. The finite-group union-admissibility step
  in the additive lemma was proved rather than assumed.
* All new-pair budgets use $t+1$, because richness means at least
  $n+1$ unordered pairs, not at least $n$.
* The circumcenter is an explicit exception in the incidence bound. All
  same-circle points are included in $B$ in the arbitrary-circle theorem.
* The exceptional nine-point model was counted using signed radii;
  its three noncorresponding cross-orbits contribute $6+6+6=18$ pairs.
* The finite-order classifications are invoked only within their stated
  orders and number-of-distances hypotheses. Source figures absent from
  the supplied files were not treated as though they had been inspected.

The important remaining uncertainty is mathematical, not numerical: no
argument excludes all configurations with a linear-sized convex layer but
without a large circular subset. The proofs do not establish either universal
assertion, and do not construct a counterexample in the requested range.

The detailed companion records (small orders, near-convex sets, layers,
regular polygons, circular majorities, and the additive atom lemma) and the
alternate rank proofs are not retained. No general resolution is claimed.

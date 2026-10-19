---
name: research/erdos_132/independent/large_distance_graph_and_convex_extension
title: Independent investigation of Erdős Problem 132
desc: |
  Archived unverified input; the 2-core improvement and circular-hull
  extension were checked, while its convex and twelve-point gaps are superseded.
sources: []
created: 2026-09-23T03:42:39Z
updated: 2026-09-24T22:12:56Z
---


# Independent investigation of Erdős Problem 132

***

The companion file small_sets.md that Section 4 names for its expanded
vertex-degree checks was not retained with this record.

## 1. Status and scope

For a set $A$ of $n\geq5$ distinct planar points, write

$$
m_A(r)=\#\{\{x,y\}\subset A:|x-y|=r\},\qquad
R(A)=\#\{r:1\leq m_A(r)\leq n\}.
$$

Every multiplicity in this record counts **unordered** pairs.

**Neither unrestricted assertion was proved or disproved in this
investigation.** The results established here are:

1. If $d_1>\cdots>d_D$ are the distinct distances and $s_k$ is the
   number of points in the first $k$ convex layers, then

   $$
   m_A(d_k)\leq(2k-1)s_k.
   $$

   Consequently, with $H$ the largest convex-layer cardinality,

   $$
   \boxed{R(A)\geq
   \left\lfloor\frac{1+\sqrt{1+8n/H}}4\right\rfloor.}
   $$

   In particular, $H=o(n)$ implies $R(A)\to\infty$.
2. Writing $\Delta,\delta$ for the largest and smallest distances,
   $\Delta/\delta=o(n)$ also implies $R(A)\to\infty$.
3. $R(A)\geq2$ for every $5\leq n\leq10$.
4. $R(A)\geq2$ whenever at least $n-1$ points are vertices of the
   convex hull.
5. $R(A)\geq2$ when there are exactly two nonvertices and all the hull
   vertices are cocircular.
6. Every twelve-point five-distance set has exactly three rare
   distances. This does not settle arbitrary twelve-point sets.

Items 1–2 have self-contained elementary proofs below. Items 3–6 use
specified classification statements from the supplied papers, together
with additional arguments given below. No claim of historical novelty
is made.

Only the supplied problem page and papers were used; there was no
browsing. No earlier research notes were accessed or used. Source
statements were read in the full supplied source files before use.
Expanded versions of the proofs were written in companion files that are
not retained.

## 2. A large-distance graph bound

### 2.1. A balanced point on a circle

**Lemma.** Among $N\geq2$ distinct points on a circle, some point $q$
has at least $\lfloor(N-1)/2\rfloor$ other points in each of the two
closed semicircles from $q$ to its antipode. An antipodal point, if
present, is counted in both semicircles.

**Proof.** First exclude antipodal pairs. In circular order
$q_1,\ldots,q_N$, let $c_i$ count the points strictly clockwise
between $q_i$ and its antipode. Each unordered pair contributes once,
so

$$
\sum_i c_i=\binom N2.
$$

Moreover $c_{i+1}\geq c_i-1$: shifting the initial endpoint to the next
point removes at most that point, while the final endpoint advances.
Set $t=\lfloor(N-1)/2\rfloor$. The average of the $c_i$'s is
$(N-1)/2$, so some value is at most $t$ and some is at least $t$.
A cyclic transition downward cannot skip $t$. Thus some $c_i=t$;
the other semicircle contains $N-1-t\geq t$ points.

For antipodal configurations, perturb the angular positions to remove
antipodal pairs and take a sequence of perturbations tending to zero.
The same selected label occurs on a subsequence. The limiting closed
semicircles retain the required counts. This is why closed, rather than
open, semicircles are used. $\square$

### 2.2. The 2-core argument

**Proposition.** Suppose an occurring distance $r$ has at most $k-1$
distinct distances larger than it. Its distance graph has a 2-core of
maximum degree at most $4k-2$. Consequently, on any $s$-point set,

$$
m(r)\leq(2k-1)s.
\tag{2.1}
$$


**Proof.** Delete vertices of current degree at most one until the
2-core remains. At a core vertex $p$, let $N$ be its degree; its
neighbors lie on $C(p,r)$. Choose a balanced neighbor $q$ by the
lemma. Since $q$ belongs to the core, it has an $r$-neighbor
$w\ne p$.

The intersection of $C(p,r)$ with the closed disk $B(w,r)$ is an
arc of angular length strictly less than $\pi$, with $q$ as an
endpoint, or is the singleton $q$. Indeed, with
$\rho=|p-w|>0$, its polar description about $p$, with direction
toward $w$ as angle zero, is

$$
\cos\theta\geq\frac{\rho}{2r}>0.
$$

One of the two closed semicircles based at $q$, apart from $q$,
therefore lies strictly outside this disk. At least
$\lfloor(N-1)/2\rfloor$ neighbors $x$ of $p$ satisfy
$|x-w|>r$.

There are at most $k-1$ possible larger lengths $|x-w|$.
For each, its circle about $w$ intersects $C(p,r)$ in at most two
points, since $w\ne p$. Hence

$$
\left\lfloor\frac{N-1}{2}\right\rfloor\leq2(k-1),
\qquad N\leq4k-2.
$$

If the core has $v$ vertices, it has at most $(2k-1)v$ edges.
Deleting the other $s-v$ vertices discarded at most $s-v$ edges.
Thus

$$
m(r)\leq s-v+(2k-1)v\leq(2k-1)s.
$$

This also handles an empty core. $\square$

For $k=1$, this proves the diameter bound $1\leq m_A(d_1)\leq n$
without importing a separate theorem.

## 3. Localization by convex depth

Define $L_1,L_2,\ldots$ by repeatedly removing the **vertices** of the
convex hull of the residual set. Nonvertex points on hull edges are not
removed until a later layer. For a collinear residual set, the vertices
are its two endpoints, or its sole remaining point. Put

$$
\lambda(x)=i\quad(x\in L_i),\qquad
S_k=\bigcup_{i\leq k}L_i,\quad s_k=|S_k|,\quad H=\max_i|L_i|.
$$

Empty later layers contribute zero.

**Depth lemma.** If $|x-y|=d_k$, then

$$
\lambda(x)+\lambda(y)\leq k+1.
\tag{3.1}
$$


**Proof.** If $x\in L_a$, $a>1$, then $x$ is a nonvertex in
$\operatorname{conv}L_{a-1}$. Write it as a nontrivial convex
combination $x=\sum_j\alpha_j z_j$ of vertices of $L_{a-1}$.
For fixed $y$,

$$
\sum_j\alpha_j|z_j-y|^2
=|x-y|^2+\sum_j\alpha_j|z_j-x|^2>|x-y|^2.
$$

Some $z_j$ is strictly farther from $y$. Move the first endpoint
outward one layer at a time, then move the second endpoint outward
while keeping the new first endpoint fixed. For depths $a,b$, this
produces $a+b-2$ successive strict increases in distance.
There are only $k-1$ larger distinct distances, proving (3.1).
Strict increases also ensure that the chosen endpoints never coincide.
$\square$

All occurrences of $d_k$ are thus supported on $S_k$. Applying
(2.1) to $S_k$, which still has at most $k-1$ lengths larger than
$d_k$, gives

$$
\boxed{m_A(d_k)\leq(2k-1)s_k.}
\tag{3.2}
$$

Therefore

$$
(2K-1)s_K\leq n\quad\Longrightarrow\quad R(A)\geq K.
\tag{3.3}
$$

The required distances exist: if $K\geq2$, the premise gives
$s_K<n$, so a point deeper than $K$, paired with a first-layer
point, has distance rank greater than $K$ by (3.1). For $K=1$,
existence follows from $n\geq2$.

Since $s_K\leq KH$, any integer satisfying

$$
K(2K-1)H\leq n
$$

is a lower bound for $R(A)$. Solving this quadratic gives the bound
in Section 1. In particular, $H=o(n)$ implies divergence.

### 3.1. Aspect ratio

Let $\Lambda=\Delta/\delta$. Each layer has at most $\pi\Lambda$
points. For a layer of $h\geq3$ vertices and perimeter $P$,
$h\delta\leq P\leq\pi\Delta$. The second inequality follows by
integrating widths: the sum of absolute projections of the polygon's
edges in direction $u_\theta$ is twice its width $w(\theta)$, and

$$
\int_0^\pi|e\cdot u_\theta|\,d\theta=2|e|.
$$

Consequently $P=\int_0^\pi w(\theta)\,d\theta\leq\pi\Delta$.
Layers of size at most two also satisfy the bound.
Thus

$$
R(A)\geq
\max\left\{1,\left\lfloor
\frac{1+\sqrt{1+8n/(\pi\Lambda)}}4
\right\rfloor\right\}.
\tag{3.4}
$$

This proves divergence whenever $\Lambda=o(n)$. For a $q\times q$
integer grid, $n=q^2$, $\delta=1$, and
$\Delta=\sqrt2(q-1)$, giving $R(A)=\Omega(n^{1/4})$.
This is a lower bound, not an assertion of the optimal grid order.

### 3.2. Necessary structure of bounded-$R$ sequences

The contrapositive of (3.3) is particularly useful. If $R(A)\leq M$,
then

$$
\sum_{i=1}^{M+1}|L_i|>\frac{n}{2M+1}.
\tag{3.5}
$$

Some one of these layers therefore contains more than

$$
\frac{n}{(M+1)(2M+1)}
$$

points. Thus a sequence violating the asymptotic conjecture must have
a positive-density convex layer among a bounded number of its outer
layers. The argument does not control that remaining situation.

## 4. Pair counting and the small-order result

Write $D=D(A)$ for the number of distances. For arbitrary $R=R(A)$,

$$
\binom n2\geq(D-R)(n+1)+R=(n+1)D-nR.
\tag{4.1}
$$

In particular, if $R=1$, the unique rare distance is the diameter,
and

$$
D\leq\lfloor n/2\rfloor.
\tag{4.2}
$$

For even $n=2t$, if $D=t$, equality holds because

$$
(t-1)(2t+1)+1=\binom{2t}{2}.
$$

Thus

$$
m_A(\Delta)=1,\qquad m_A(r)=n+1\quad(r<\Delta).
\tag{4.3}
$$

For odd $n=2t+1$ and $D=t$, the analogous calculation gives only
$m_A(\Delta)\leq t+2$; it does not give a unique diameter.

### 4.1. Classification inputs actually used

The supplied
[Erdős–Fishburn 1996 source](../../../../library/distance_problems/erdos_fishburn_1996_maximum_planar_sets_that_determine_k_distances/_index.md),
Theorem 1 and Sections 2–4, states:

* $g(1)=3,\ g(2)=5,\ g(3)=7,\ g(4)=9,\ g(5)=12$, where $g(k)$
  is the maximum cardinality of a planar $k$-distance set.
* The only five-point two-distance set is the regular pentagon.
* The seven-point three-distance sets are the regular heptagon and
  the regular hexagon together with its center.
* There are at most four similarity types of nine-point four-distance
  sets: the regular nonagon and three displayed configurations.

The last classification is also stated in the supplied
[Shinohara 2008 source](../../../../library/distance_problems/shinohara_2008_uniqueness_maximum_planar_five_distance_sets/_index.md),
Theorem 1.1(a). The classification proofs are imported results, not
independently reconstructed here.

The figures are not needed for the nine-point multiplicity check:
four mutually nonsimilar examples below realize the four possible
types, and hence exhaust the classification.

### 4.2. Exact nine-point calculations

In triangular-lattice coordinates $(a,b)\mapsto(a+b/2,\sqrt3b/2)$,
the squared norm is $a^2+ab+b^2$. Take

$$
\begin{aligned}
T_1={}&\{(0,0),(1,0),(0,1),(-1,1),(-1,0),(0,-1),
                  (1,-1),(1,1),(-1,2)\},\\
T_2={}&\{(0,0),(1,0),(0,1),(-1,1),(1,-1),(1,1),
                  (-1,0),(2,-1),(0,2)\}.
\end{aligned}
$$

Direct substitution for all unordered pairs gives

$$
\begin{array}{c|rrrr}
\text{squared distance}&1&3&4&7\\ \hline
T_1&16&9&7&4\\
T_2&15&9&6&6
\end{array}
\tag{4.4}
$$

The rows sum to $36=\binom92$. Expanded vertex-degree checks appear
in small_sets.md; these integer calculations were also independently
checked by a short exact enumeration.

For the third nonregular example, identify the plane with
$\mathbb C$, put $\omega=e^{2\pi i/3}$, and set

$$
T_3=\{a\omega^j:
 a\in\{1,1+\sqrt3,-2-\sqrt3\},\ j=0,1,2\}.
$$

For two signed radii $a,b$, corresponding vertices have squared
distance $(a-b)^2$, three times; noncorresponding vertices have
squared distance $a^2+ab+b^2$, six times. The internal squared
side length is $3a^2$, three times. Hence

$$
\begin{array}{c|rrrr}
\text{squared distance}&3&6+3\sqrt3&12+6\sqrt3&21+12\sqrt3\\ \hline
T_3&6&18&6&6 .
\end{array}
\tag{4.5}
$$

The regular nonagon has spectrum $(9,9,9,9)$. All four
multiplicity multisets differ, so these examples are nonsimilar and
exhaust the classification. Each has at least two rare distances;
each nonregular example has a multiplicity at least fifteen.

### 4.3. A regular-polygon extension obstruction

**Lemma.** For a regular $(2t+1)$-gon $P$, $t\geq2$, no added
point has distances to $P$ consisting of each of the $t$ polygon
distances twice, and one additional distance once.

Normalize its circumcircle to the unit circle. The added point
$p$ is not the center. Each equal-distance pair of vertices is
interchanged by reflection in the line $0p$. The sum of all vertices
is zero, so the remaining unpaired vertex also lies on $0p$.
Rotate it to $(1,0)$, and write $p=(x,0)$. With
$c_j=\cos(2\pi j/(2t+1))$, the two sets of squared distances are

$$
\{x^2+1-2xc_j:1\leq j\leq t\}
=\{2-2c_j:1\leq j\leq t\}.
$$

Their ranges imply $|x|=1$. Their sums, using
$\sum_jc_j=-1/2$, imply

$$
t(x^2+1)+x=2t+1.
$$

Thus $x=1$, making $p$ the unpaired vertex itself, a contradiction.

### 4.4. Proof for $5\leq n\leq10$

Assume $R(A)=1$.
For $n=5,7,9$, (4.2) and the $g(k)$ bounds reduce to the maximum
configurations above. Their spectra are, respectively,

$$
(5,5);\qquad (7,7,7),\ (12,6,3);
$$

and the four nine-point spectra (4.4)–(4.5) and $(9,9,9,9)$.
Every one has at least two rare distances.

For $n=6,8,10$, the same bounds force $D=n/2$, so (4.3) applies.
Delete one endpoint of the unique diameter. Every other distance
survives, since its $n+1$ pairs cannot all be among the $n-1$
deleted pairs. The resulting $n-1$-point set has exactly $n/2-1$
distances and is classified above.

If it is nonregular, it has a multiplicity $12>9$ when $n=8$,
or at least $15>11$ when $n=10$, contradicting (4.3).
Otherwise it is the regular $(n-1)$-gon. Each old multiplicity
must rise from $n-1$ to $n+1$, and exactly one new diameter pair
is added. This is precisely the impossible extension in the lemma.
Therefore $R(A)\geq2$ throughout $5\leq n\leq10$.

### 4.5. Twelve points with five distances

Shinohara 2008, Theorem 1.2(b), states uniqueness up to similarity.
An explicit representative is

$$
U=\{(a,b)\in\mathbb Z_{\geq0}^2:a+b\leq4\}
\setminus\{(0,0),(4,0),(0,4)\}
$$

in triangular-lattice coordinates. At squared distances $1,3,4,7,9$,
its multiplicities are

$$
(24,15,12,12,3).
\tag{4.6}
$$

These sum to $66$, and give $R(U)=3$.
At squared distance four every vertex has degree two. Deleting one
point leaves ten pairs at that distance. The three diameter pairs
are the disjoint pairs

$$
\{(0,1),(3,1)\},\quad\{(1,0),(1,3)\},\quad\{(0,3),(3,0)\}.
$$

At least two survive, so every eleven-point subset of $U$ also
has two rare distances.

This does not classify arbitrary eleven-point five-distance sets.
Nor does it settle twelve-point six-distance sets; see Section 7.

## 5. A proved extension beyond convex sets

The supplied
[Fishburn 1995 source](../../../../library/distance_problems/fishburn_1995_convex_polygons_few_intervertex_distances/_index.md),
Section 1, Theorems 1–2, gives the following inputs: a convex $h$-gon has at
least $\lfloor h/2\rfloor$ distances; for odd $h$, equality forces
regularity; for even $h\geq8$, equality forces a regular $h$-gon or a
regular $(h+1)$-gon with one vertex deleted. In particular, both even equality
cases are cocircular.

### 5.1. One extra point inside a cocircular hull

Let $B$ be $h=n-1$ points on a circle and
$p\in\operatorname{conv}B\setminus B$. For every $b\in B$,

$$
|p-b|<\operatorname{diam}B.
\tag{5.1}
$$

This follows from the same strict convexity identity as in Section 3
by expressing $p$ as a nontrivial convex combination of points of
$B$. It includes points in the relative interior of a hull edge.

If $p$ is not the circumcenter, circles centered at $p$ meet the
circumcircle in at most two points. Thus $p$ sees at least
$\lceil h/2\rceil$ distances, none the diameter. Consequently

$$
D(A)\geq\lceil(n-1)/2\rceil+1>\lfloor n/2\rfloor,
$$

excluding $R=1$.

If $p$ is the circumcenter, each distance graph on $B$ has maximum
degree two, hence at most $h$ edges. Adding $p$ changes just the
circumradius class. For $h\geq6$, there are at least three old
classes, leaving two rare ones. For $h=5$, either there are at least
three old classes, or $B$ is a regular pentagon; its circumradius
is a new distance and is rare. The case $n=5$ is already settled.
Thus a cocircular hull plus one nonvertex always satisfies $R\geq2$.

### 5.2. At most one nonvertex, without the circle assumption

**Theorem.** If at least $n-1$ points are hull vertices, then
$R(A)\geq2$.

The fully convex case is the supplied Clemen–Dumitrescu–Liu
Theorem 1.2, whose proof in Section 2.1 was read. Suppose instead
that $B$ is the set of $n-1$ hull vertices and $p$ is the single
nonvertex. Small orders through eight are settled above. Assume
$n\geq9$ and $R(A)=1$.

If $n$ is odd, the bounds

$$
(n-1)/2\leq D(B)\leq D(A)\leq(n-1)/2
$$

force equality for the even polygon $B$. Fishburn's classification
makes $B$ cocircular, contradicting Section 5.1.

If $n=2t$ is even, $t-1\leq D(B)\leq D(A)\leq t$.
If $D(B)=t-1$, the odd equality theorem makes $B$ regular.
Otherwise $D(B)=D(A)=t$, and (4.3) gives a unique diameter $uv$.
Its endpoints lie in $B$, by (5.1).

Both $B\setminus\{u\}$ and $B\setminus\{v\}$ are convex
$(n-2)$-point sets from which the diameter has disappeared. Thus
each has exactly $(n-2)/2=t-1$ distances. Since $n-2\geq8$,
both are cocircular by the even equality classification. Their
circles share $n-3$ hull vertices, including three noncollinear
points, and hence coincide. Therefore all of $B$ is cocircular,
again contradicting Section 5.1.

This endpoint-deletion step closed an initially unresolved even-order
branch. It avoids needing a classification of odd polygons with one
more than the minimum number of distances.

### 5.3. Two nonvertices with a cocircular hull

Let $C$ be $h=n-2$ hull vertices on a circle and let $p,q$
be the two nonvertices. For $n\leq10$ the result is already known;
the following argument in fact needs only the small cases $n\leq6$.
Assume $R=1$.

At least one of $p,q$ is not the center. If $n=2t+1$ is odd, that
point sees at least $\lceil h/2\rceil=t$ non-diameter lengths on
$C$. Together with the diameter this contradicts (4.2).

Let $n=2t\geq8$, so $h=2t-2$. An off-center point sees at least
$t-1$ non-diameter lengths; hence $D=t$, and (4.3) applies.
Each off-center added point therefore sees every one of the $t-1$
non-diameter lengths exactly twice on $C$.

Normalize the circle to radius one and center zero. If one added
point, say $q$, is the center, then for any non-diameter
$r\notin\{1,|p|\}$,

$$
m_A(r)=m_C(r)+2\leq h+2=n,
$$

a contradiction. There are $t-1\geq3$ distinct non-diameter
lengths, so such an $r$ exists.

Otherwise both are off-center. The equal-distance pairs show that
reflection in each of $0p$ and $0q$ permutes $C$, with no fixed
vertex. Both reflections must exchange the endpoints of the unique
diameter, so their axes coincide with its perpendicular bisector.
Take this common axis to be the $x$-axis, and write
$p=(a,0),q=(b,0)$, with $a,b\ne0$. Write the hull vertices in
reflected pairs

$$
(x_j,\pm\sqrt{1-x_j^2}),\qquad 1\leq j\leq h/2.
$$

The two sets of squared distances to these pairs are identical:

$$
\{1+a^2-2ax_j\}_j=\{1+b^2-2bx_j\}_j.
$$

The $x_j$'s are not all equal, so comparing ranges gives
$|a|=|b|$. Since $p\ne q$, $b=-a$. The same equality of sets
then gives $\{x_j\}_j=\{-x_j\}_j$. Together with reflection in the
$x$-axis, this makes $C$ centrally symmetric. It has $h/2\geq3$
antipodal diameter pairs, contradicting uniqueness. Thus $R\geq2$.

## 6. Other bounds retained, and source cautions

Two weaker elementary approaches preceded the 2-core bound.
They remain valid, but are superseded for the main asymptotic purpose.

* On $s$ points a fixed-distance graph has at most two common
  neighbors for each pair of vertices. Thus

  $$
  \sum_v\binom{\deg(v)}2\leq s(s-1),\qquad
  m\leq\left\lfloor\frac{s(1+\sqrt{8s-7})}{4}\right\rfloor.
  $$

  Combining this with support in $S_k$ would prove divergence under
  the stronger restriction $H=o(n^{2/3})$.

* From (3.1), if $h_i=|L_i|$, a $d_k$-edge can only join layers
  with indices summing to at most $k+1$. Hence

  $$
  m_A(d_k)\leq
  \sum_{\substack{i<j\\i+j\leq k+1}}h_i h_j+
  \sum_{2i\leq k+1}\binom{h_i}{2}.
  $$

  This direct count gives weaker layer-width conditions than (3.2).

The supplied
[Clemen–Dumitrescu–Liu source](../../../../library/distance_problems/clemen_2025_multiplicities_interpoint_distances/_index.md),
Theorem 1.3 and Section 2.2, states

$$
m_A(d_2)\leq
\min\left\{\frac32(h_1+h_2),\ \frac43h_1+2h_2,\ 2h_1+h_2\right\}.
\tag{6.1}
$$

The digest miscopies the second and third expressions; the full
source is the authority here. There is also an intermediate arithmetic
typo in the source proof:

$$
2|L'_1|-\tfrac12e(L'_1,L'_2)
=2|L'_1|-|L'_2|
$$

when $e(L'_1,L'_2)=2|L'_2|$, not
$2|L'_1|-2|L'_2|$. The next display uses the correct expression.
No stronger theorem is inferred from the typo.

Equation (6.1) implies that any counterexample to $R\geq2$ must,
in particular, have $h_1+h_2>2n/3$. This sharper two-distance
source bound is separate from the elementary all-rank estimate (3.2).
The detailed inherited geometric degree assertions in the source's
proof were not independently reproved here; the source theorem is
being used as a stated result. The new proof of (3.2) does not depend
on them.

## 7. Failed extensions and precise remaining gaps

### Counting alone

Equation (4.1) is useful only when the total number of distinct
distances is sufficiently close to or above $n/2$. It does not
force two rare classes for arbitrary sets. Bounds on the total number
of distances that grow more slowly than $n/2$ cannot repair this
argument. A putative $R=1$ multiplicity sequence is not ruled out
merely because the total number of distances grows.

### The second-largest distance is not always rare

The supplied
[Vesztergombi 1987 source](../../../../library/distance_problems/vesztergombi_1987_large_distances_planar_sets/_index.md),
main theorem and final construction, gives the sharp upper bound
$m_A(d_2)\leq3n/2$, with examples exceeding $n$. Therefore one cannot
universally select the two largest lengths. Those examples are not
counterexamples to this problem: their other distance multiplicities would also
need to be checked.

### Passing from a subset to the original set

A rare distance in a convex subset or a diameter-free subset need not
be rare in $A$. Restoring the removed points can add many pairs of
that same length. In particular, the supplied diameter-graph
independent-set methods do not on their own transfer a rare-distance
bound back to $A$. The one-nonvertex result above avoids this gap
through equality classifications and the two endpoint deletions,
not through a general monotonicity assertion.

### Large convex layers

The main asymptotic estimate becomes ineffective when an early convex
layer contains a positive proportion of all points. This is a real
unresolved branch, not a technicality. Even an arbitrary number of
layers does not help if an early one is sufficiently large.
Equation (3.5) precisely states what a bounded-$R$ sequence would
have to satisfy; no contradiction has been obtained from it.

For convex sets, pair counting implies that a bounded-$R$ sequence
would have only a bounded additive excess of distinct distances over
$n/2$. The supplied Fishburn paper classifies the exact minimum
and discusses a conjectural wider stability phenomenon. The necessary
general near-minimum classification is not established in the supplied
material and was not proved here. It cannot be assumed to conclude
divergence, even for all convex sets.

### The first unhandled small-order branch

For $n=11$, a putative counterexample has exactly five distances:
four classes of size at least twelve and a diameter class of size at
most seven. The supplied results do not classify all eleven-point
five-distance sets, and there is no justification for assuming they
extend to the unique twelve-point example $U$.

For $n=12$, the five-distance case is settled by (4.6). The remaining
counterexample pattern has six distances, with multiplicities

$$
1,13,13,13,13,13,
$$

where the singleton is the diameter. Deleting one diameter endpoint
leaves an eleven-point five-distance set, bringing back the same
unresolved classification branch.

### Scope of the near-convex results

The theorem with at most one nonvertex is proved for every $n\geq5$.
The two-nonvertex theorem still assumes a cocircular hull. There is
no proved extension here to an arbitrary hull with two or more
nonvertices. Neither theorem supplies a uniform unbounded lower
bound for $R$ in near-convex sets.

## 8. Checks and status

The main geometric argument was checked independently for antipodal
neighbors, tangent circle intersections, empty 2-cores, collinear
layers, nonvertex hull-edge points, and existence of all distance
ranks used. The small lattice spectra were checked by exact integer
arithmetic; the exceptional nine-point spectrum follows from the
displayed symbolic triangle formulas. These computations verify
explicit configurations only; exhaustiveness comes from the stated
source classifications.

The restriction $n\geq5$ has been retained. For comparison, the four
points

$$
(0,0),\ (1,0),\ (1/2,\sqrt3/2),\ (1/2,-\sqrt3/2)
$$

have five unit pairs and one pair of length $\sqrt3$, so $R=1$.
This is not a counterexample in the requested range.

The established
results above are retained as proofs and source-dependent deductions;
the large-layer branch and the unrestricted conjectures remain open
within this record.

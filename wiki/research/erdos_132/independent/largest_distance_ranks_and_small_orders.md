---
name: research/erdos_132/independent/largest_distance_ranks_and_small_orders
title: Independent record of Erdős Problem 132
desc: |
  Archived independent input, not a canonical proof record; selected
  claims were checked and incorporated into the linked topical notes.
sources: []
created: 2026-09-23T00:27:00Z
updated: 2026-10-13T05:28:09Z
---


# Independent record of Erdős Problem 132

***

## Status and scope

The targets are (i) $R(A)\ge2$ for every set of $n\ge5$ distinct planar
points, and (ii) $\min_{|A|=n}R(A)\to\infty$. The threshold in both questions
is the size of the full set, not the size of a selected subset.

Neither assertion for **all** finite planar sets is resolved in this
investigation. No planar counterexample is constructed. The results below are
proved for the indicated hypotheses; no passage from a restricted family to
arbitrary configurations is assumed.

All multiplicities count unordered pairs, and

$$
 m_A(r)=\#\{\{p,q\}\subset A:|p-q|=r\},\qquad
 R(A)=\#\{r:1\le m_A(r)\le |A|\}.
$$

Only the supplied problem page and source files were used. No browsing was
performed. The mention of unavailable earlier notes in the problem page was not
used as mathematical evidence.

The principal conclusions are:

1. **Arbitrary sets, finite orders:** $R(A)\ge2$ for every $5\le |A|\le10$,
   by exact counting and the supplied few-distance classifications.
2. **Arbitrary sets, a quantitative layer bound:** if $h$ is the largest
   number of vertices in any convex layer, then

   $$
   \boxed{R(A)\ge\max\left\{1,\left\lfloor\sqrt{\frac{n}{2h}}\right\rfloor\right\}.}\tag{1}
   $$

   More precisely, writing $s_k$ for the number of points in the first $k$
   layers, $2ks_k\le n$ implies that the $k$ largest distances are rare.
3. **A restricted asymptotic theorem:** $R(A_n)\to\infty$ if every fixed
   number of outer convex layers contains $o(|A_n|)$ points. In particular
   this holds if the largest layer is $o(n)$, or if diameter divided by
   minimum separation is $o(n)$.
4. **An independently proved affine restriction:** if a nonsimilarity invertible
   affine map preserves all equal-distance relations of $A$, then

   $$
   R(A)\ge\left\lceil\frac{n-1}{4}\right\rceil,
   $$

   and $R(A)\ge2$ throughout the required range $n\ge5$.

This record contains the principal proofs, exact coordinate calculations, failed
approaches, and explicit uncertainties. Sections 1–5 give the main results and
the unresolved general gap; Appendix A gives finite configurations and remaining
small-order cases; Appendix B records the affine obstruction; Appendix C gives
the abstract countermodel’s Euclidean obstruction and the component argument;
Appendix D records superseded and unsuccessful approaches; Appendix E states the
final limits. The investigation's scratch files are not retained; this record is
intended to be readable without them, and the supplied published classifications
remain explicit external inputs.

## 1. Largest-distance ranks and convex depth

Delete the vertices of the convex hull repeatedly to obtain layers
$L_1,L_2,\ldots$. For a collinear remaining set, its hull vertices are its two
endpoints, or its sole point. Write $\ell(p)=i$ when $p\in L_i$, and

$$
 H_k=L_1\cup\cdots\cup L_k,\quad s_k=|H_k|,
 \qquad d_1>d_2>\cdots>d_q>0
$$

for the distinct distances in decreasing order.

### Lemma 1: depth restricts distance rank

If $|p-q|=d_j$, then

$$
 \ell(p)+\ell(q)\le j+1.\tag{2}
$$


**Proof.** Suppose $p$ has depth $i>1$. It is a convex combination of at
least two distinct vertices of $L_{i-1}$. Strict convexity of
$x\mapsto|x-q|^2$ implies that at least one of those vertices $p'$ satisfies
$|p'-q|>|p-q|$. Repeat until the first endpoint is on $L_1$, obtaining
$i-1$ strict increases. Keep the resulting endpoint fixed and move the other
endpoint outward in the same way, obtaining $\ell(q)-1$ further strict
increases. These yield $i+\ell(q)-2$ distinct distances larger than $|p-q|$,
so there can be at most $j-1$ of them. A replacement never coincides with the
fixed endpoint, since the new distance strictly increases. This proves (2),
including degenerate layers. $\square$

In particular, all pairs at one of the first $j$ distances have both endpoints
in $H_j$. Thus

$$
 m_A(d_j)=m_{H_j}(d_j),\tag{3}
$$

and $d_j$ retains its rank in $H_j$.

### Lemma 2: a rank-dependent linear bound

If a distance $r$ has at most $k-1$ distinct larger distances in a planar
set $B$, its distance graph is $2k$-degenerate. In particular,

$$
 m_B(r)\le2k|B|.\tag{4}
$$


**Proof.** Consider any nonempty subset $T\subseteq B$, and translate a
leftmost point $p$ to the origin. All points of $T$ lie in the closed right
halfplane. If $p$ has at most $2k$ neighbors at distance $r$, it is the
required low-degree vertex.

Otherwise its $t\ge2k+1$ neighbors can be written

$$
 q_j=r(\cos\theta_j,\sin\theta_j),\qquad
 -\pi/2\le\theta_1<\cdots<\theta_t\le\pi/2.
$$

Choose $q_i$ with at least $k$ of these neighbors on each angular side. We
claim that $q_i$ has no distance-$r$ neighbor in $T$ other than $p$.

Suppose such a neighbor $x\ne p$ exists. Write

$$
 x=\rho(\cos\phi,\sin\phi),\quad \rho>0,
 \quad -\pi/2\le\phi\le\pi/2.
$$

The equality $|x-q_i|=r$ gives

$$
 \cos(\theta_i-\phi)=\frac{\rho}{2r}>0.
$$

If $\theta_i\ge\phi$, use $k$ indices with $\theta_j>\theta_i$. The angles
$\theta_j-\phi$ are distinct and lie in $(\theta_i-\phi,\pi]$. Since cosine
is strictly decreasing on $[0,\pi]$, the quantities

$$
 |x-q_j|^2=\rho^2+r^2-2\rho r\cos(\theta_j-\phi)
$$

are distinct and strictly greater than $r^2$. This gives $k$ distinct larger
distances, a contradiction. If $\theta_i\le\phi$, use the $k$ neighbors
below $\theta_i$ instead, with angles $\phi-\theta_j$. Hence $q_i$ has
degree one.

Every induced subgraph therefore contains a vertex of degree at most $2k$.
Removing such vertices successively counts every unordered edge once and proves
(4). Ties in the leftmost coordinate cause no problem: the angles still lie in a
closed semicircle. $\square$

### Theorem 3: the layer bound

If $A$ has at least $k$ distances and $2ks_k\le n$, then $R(A)\ge k$;
specifically, its $k$ largest distances are rare.

**Proof.** For every $j\le k$, equations (3) and (4) give

$$
 m_A(d_j)=m_{H_j}(d_j)\le2js_j\le2ks_k\le n.
$$

These classes are nonempty by definition. $\square$

Let $h=\max_i|L_i|$. Since $s_k\le kh$, this proves (1), apart from checking
that the required distances exist. If there are $t$ layers, then $t\ge n/h$.
Applying Lemma 1 to a deepest point and any other point shows that there are at
least $t$ distances. Consequently $\lfloor\sqrt{n/(2h)}\rfloor\le t\le q$.
The additional lower bound one is the diameter theorem: the diameter occurs on
at most $n$ unordered pairs. Its statement and proof were read in Erdős
(1946), Section 4.

For a sequence with $s_k=o(n)$ for each fixed $k$, Theorem 3 proves
$R(A_n)\to\infty$. There are eventually at least $k$ distances: if there are
only $q$, two fixed distinct centers and intersections of their distance
circles give $n\le2q^2+2$.

### A geometric consequence in terms of separation

Let $\delta$ be the least distance and $\Delta$ the diameter. A layer with
at least three vertices has perimeter at least $|L_i|\delta$ and at most
$\pi\Delta$, so

$$
 h\le\frac{\pi\Delta}{\delta}.
$$

The same inequality holds for one- or two-point layers. For completeness, the
perimeter upper bound follows by integrating projections: for a convex polygon,
the sum of absolute projections of its edges on a line is twice its width in
that direction. Integrating over directions $0\le\theta\le\pi$, each edge of
length $a$ contributes $2a$, while every width is at most $\Delta$. Hence
its perimeter is at most $\pi\Delta$.

Thus

$$
 \boxed{R(A)\ge\max\left\{1,
 \left\lfloor\sqrt{\frac{n\delta}{2\pi\Delta}}\right\rfloor\right\}.}\tag{5}
$$

In particular, uniformly separated sets of diameter $O(\sqrt n)$ have
$R(A)=\Omega(n^{1/4})$, by this elementary argument.

There is also a complementary elementary estimate. Two vertices of a
fixed-distance graph have at most two common neighbors. If that graph has $s$
vertices and $e$ edges, counting pairs of neighbors and using Cauchy–Schwarz
gives

$$
 \sum_v\binom{\deg v}{2}\le2\binom{s}{2},
 \qquad e\le U(s):=\frac{s}{4}\bigl(1+\sqrt{8s-7}\bigr).
$$

Hence $U(s_k)\le n$ is another sufficient condition for the first $k$
distances to be rare. For instance $s_k\le n^{2/3}$ suffices, since
$U(s)\le s/4+s^{3/2}/\sqrt2$ and $1/4+1/\sqrt2<1$. This also gives
$R(A)\ge\lfloor n^{2/3}/h\rfloor$. If one invokes the general unit-distance
bound $m_B(r)\le C|B|^{4/3}$ stated in the supplied Clemen–Dumitrescu–Liu
Section 1.4, the same support argument improves this supplementary bound to
$R(A)\ge\lfloor c n^{3/4}/h\rfloor$ for an absolute $c>0$. The
rank-dependent bound (1) and its consequences do not need that incidence
theorem.

## 2. Exact consequences for small orders

Let $q$ be the number of distinct distances and $N=\binom n2$. If
$R(A)=1$, its sole rare distance is the diameter, and

$$
 N\ge1+(q-1)(n+1),\qquad q\le\lfloor n/2\rfloor.\tag{6}
$$

If $n=2t$ and $q=t$, equality holds: the diameter occurs once and every
other distance occurs exactly $n+1$ times. Deleting either endpoint of the
diameter leaves exactly $t-1$ distances, each with multiplicity at most
$n+1$.

Let $g(k)$ denote the maximum cardinality of a planar set determining exactly
$k$ distances. Theorem 1 of the supplied Erdős–Fishburn (1996) paper gives

$$
 g(2)=5,\quad g(3)=7,\quad g(4)=9,
$$

and classifies the sets attaining these bounds. Its statement and relevant proof
passages were read. The classifications, with exact multiplicities, are:

| Points | Distances | All possible multiplicity multisets |
|---:|---:|---|
| 5 | 2 | $(5,5)$ |
| 7 | 3 | $(7,7,7)$, $(12,6,3)$ |
| 9 | 4 | $(9,9,9,9)$, $(16,9,7,4)$, $(15,9,6,6)$, $(18,6,6,6)$ |

The seven-point types are a regular heptagon and a regular hexagon with its
center. For nine points the source lists exactly four similarity types. Because
its figures are only textually reproduced, Appendix A.1 below constructs four
pairwise nonsimilar coordinate models and computes all their distances exactly.
This exhausts the classification without guessing missing figure coordinates.

For $n=5,7,9$, (6) and the bounds on $g$ force respectively two, three, and
four distances. The table excludes $R=1$.

For $n=6,8,10$, (6) forces respectively three, four, and five distances, so
the even-order equality case applies. Delete either endpoint of the unique
diameter. For $n=6$, both resulting sets are regular pentagons. For $n=8$,
both are regular heptagons, since the alternative seven-point type has
multiplicity twelve, greater than $n+1=9$. For $n=10$, both are regular
nonagons, since every nonregular nine-point type has a multiplicity at least
fifteen, greater than eleven.

In each case two regular $(n-1)$-gons share $n-2\ge4$ vertices. Three shared
vertices determine their circumcircle, and one vertex on that circle determines
the regular polygon of a specified order. Thus the two sets coincide,
contradicting deletion of distinct endpoints. This proves $R(A)\ge2$ for every
$5\le n\le10$.

The exact calculations in Appendix A.2 establish:

* Every twelve-point five-distance set has multiplicities $(24,15,12,12,3)$ in
  increasing distance order, using Shinohara (2008), Theorem 1.2(b), and an
  explicit lattice model. Thus it has three rare distances.
* Deleting one specified point of that model gives eleven points with
  multiplicities $(18,12,10,12,3)$, and exactly two rare distances.
* A possible counterexample at $n=11$ must be a five-distance set. A possible
  counterexample at $n=12$ must have six distances with multiplicities
  $(13,13,13,13,13,1)$, the last class being the diameter. Neither possibility
  is excluded by the classifications used here.

## 3. A linear bound under a precise affine hypothesis

Suppose an orthonormal coordinate system has the property

$$
 |p-q|=|p'-q'|\quad\Longrightarrow\quad
 |x(p)-x(q)|=|x(p')-x(q')|.\tag{7}
$$

Then equality of absolute vertical displacements follows as well. Thus each
distance has a fixed displacement pair $(a,b)$, up to signs.

Every vertical distance class is a disjoint union of finite paths on the
vertical fibers, so it has at most $n-1$ edges. Write $m=\min x$,
$M=\max x$, and $W=M-m>0$; the case $W=0$ is collinear and immediate. A
class with $a>W/2$ has maximum degree at most two: a point cannot have
neighbors on both lines $x-a$ and $x+a$, and the one possible neighbor line
allows at most two ordinates. Such a class is therefore rare.

Let $c$ points lie on $x=(M+m)/2$. Of the remaining points, at least
$(n-c)/2$ lie strictly on one side of that line. Join these to an anchor on
the opposite extreme line. Every resulting distance is rare by the preceding
paragraph, and at most two anchor edges have the same distance by (7). We obtain
at least $\lceil(n-c)/4\rceil$ rare classes. If $c\ge1$, the middle fiber
gives another $c-1$ distinct vertical distances; by (7), these are globally
rare and distinct from the previous classes. Therefore

$$
 R(A)\ge\left\lceil\frac{n-1}{4}\right\rceil.\tag{8}
$$

For $c=0$, the anchor argument gives the stronger $\lceil n/4\rceil$.

For $n\ge6$, (8) gives at least two. At $n=5$, every class is rare: a
non-axis class has edge vectors $\pm(a,b),\pm(a,-b)$, so each connected
component is a square-grid subgraph. If a component has $u$ vertices in $r$
rows and $s$ columns, it has at most

$$
 2u-r-s\le2u-2\sqrt u
$$

edges. Summing gives at most $2n-2\sqrt n$, whose floor is five at $n=5$.
Axis classes are unions of paths. Five planar points cannot all be mutually
equidistant, so at least two classes occur.

Condition (7), in some orthonormal coordinates, is equivalent to the existence
of an invertible nonsimilarity affine map preserving every original
equal-distance relation. Indeed, write its positive definite matrix
$T^{\mathsf T}T$ in an orthonormal eigenbasis with distinct eigenvalues
$\lambda,\mu$. For equal-length vectors $d,e$, the two equalities

$$
 d_x^2+d_y^2=e_x^2+e_y^2,
 \qquad \lambda d_x^2+\mu d_y^2=\lambda e_x^2+\mu e_y^2
$$

force $d_x^2=e_x^2$. Conversely, (7) permits any positive diagonal stretching
in those coordinates.

This hypothesis is a real restriction. An equilateral triangle, or a square,
forces every equality-preserving affine map to be a similarity; the matrix
obstruction is detailed in Appendix B. A generic perturbation cannot be
substituted, because it splits old distance classes and can turn a rich original
class into many rare new ones.

## 4. A concrete obstruction to diameter-only arguments

Even imposing the diameter edge bound, absence of even cycles, and at most one
cycle on **every induced maximum-color graph** does not force two rare colors in
an ordered edge-coloring of a complete graph.

For $n=4s$, $s\ge2$, label vertices $0,\ldots,n-1$ and color a pair
according to which of these intervals contains $|a-b|$:

$$
 \{1\},\quad[2,3],\quad[4,5],\quad\ldots,\quad
 [2s-2,2s-1],\quad[2s,4s-1].
$$

Order the colors as displayed, with $\{1\}$ highest. Its multiplicity is
$n-1$. A middle color $[2j,2j+1]$ has

$$
 (n-2j)+(n-2j-1)=2n-4j-1\ge n+3
$$

edges, and the last color has $s(2s+1)>n$. There is exactly one rare color and
$n/4+1$ colors in total.

In any subset whose highest occurring color is $[L,U]$, all consecutive label
gaps are at least $L$. Nonconsecutive labels differ by at least $2L$,
whereas every displayed interval satisfies $U<2L$. Thus the highest-color
graph is a subgraph of the path through consecutive labels. Every induced
maximum-color graph is a linear forest, yet only one global color is rare.

These are **not Euclidean counterexamples**. Their restriction to five
consecutive vertices is already unrealizable, as proved by the explicit
circle-intersection equations in Appendix C.1. The construction shows precisely
that inter-color Euclidean constraints, beyond hereditary diameter edge counts
or abstract diameter graph structure, are indispensable.

## 5. Remaining gap

The layer theorem gives a precise necessary condition for a sequence with
bounded $R$. If $R(A)\le M$, $n>2M^2+2$, and $K=M+1$, then $A$ has at
least $K$ distances. Theorem 3 forces

$$
 s_K>\frac{n}{2K}.
$$

At least one of its first $K$ convex layers consequently has more than
$n/(2K^2)$ vertices. Thus any bounded-$R$ sequence must have a macroscopic
convex layer at bounded depth.

The supplied Clemen–Dumitrescu–Liu paper proves $R\ge2$ for convex sets and
proves

$$
 m_A(d_2)\le\min\left\{
 \tfrac32(|L_1|+|L_2|),\
 \tfrac43|L_1|+2|L_2|,\
 2|L_1|+|L_2|\right\}.
$$

Its statements and proofs in Sections 1.1 and 2 were read. These yield
additional sufficient conditions, but do not fill the macroscopic-layer gap. In
the displayed derivation of the last bound, the supplied transcription has an
arithmetic typo: after $e(L'_1,L'_2)=2|L'_2|$, the bound on $e(L'_1)$ is
$2|L'_1|-|L'_2|$, not $2|L'_1|-2|L'_2|$. Its following display uses the
correct coefficient.

Nor does the convex theorem alone establish divergence for arbitrary convex
sets. In any configuration with $q$ distances,

$$
 \binom n2\ge(q-R)(n+1)+R,
 \quad\text{so}\quad
 q\le\frac{\binom n2+nR}{n+1}.
$$

For convex sets, the supplied distinct-distance lower bound is
$q\ge\lfloor n/2\rfloor$. Hence bounded $R$ forces $q=n/2+O(1)$, but no
classification or stability theorem for this entire bounded-excess regime is
established here.

The unresolved tasks are therefore substantive: control rare classes in
configurations with large outer layers, or find another inter-color Euclidean
mechanism. Passing to a convex subset does not preserve the required
multiplicity upper bound after the other points are restored. Passing to a
generic deformation does not preserve rare classes when equalities split.
Neither transfer is used in the proved results above.

## Source passages used

* Erdős (1946), *On sets of distances of n points*, Section 4: the diameter
  bound.
* Erdős–Fishburn (1996), *Maximum planar sets that determine k distances*,
  Theorem 1 and Sections 2–3: extremal sizes and the classifications used for
  $5\le n\le10$.
* Shinohara (2008), *Uniqueness of maximum planar five-distance sets*, Theorems
  1.1–1.2 and Section 3: uniqueness at twelve points and the stated
  diameter-graph restrictions.
* Clemen–Dumitrescu–Liu (2025), *On multiplicities of interpoint distances*,
  Sections 1.1 and 2: the convex and two-layer results. Their Section 1.4 was
  also read, but its reported unit-distance incidence bound is not needed for
  the elementary main results here.
* Vesztergombi (1987), *On large distances in planar sets*: the
  second-largest-distance bound and its proof were read while examining
  extensions.
* Bhowmick, *A problem of Erdős about rich distances*, Section 2: the
  common-vertex rotation and common-edge reflection constructions, recorded as
  an unsuccessful route to controlling the number of rare classes.

All these refer to the cited papers. No assertion above depends on an
unavailable figure, an external web source, or an assumed earlier investigation.

## Appendix A. Exact configurations and unresolved finite cases

### A.1. Four nine-point four-distance models

Let $P_m$ denote a regular $m$-gon. Its $(m-1)/2$ distances each occur $m$ times
when $m$ is odd. Thus $P_9$ has the multiplicity vector

$$
(9,9,9,9).
$$


For the next two models use axial triangular-lattice coordinates. A pair
$(x,y)\in\mathbb Z^2$ represents the Euclidean point

$$
\phi(x,y)=\left(x+\frac y2,\frac{\sqrt3\,y}{2}\right).
$$

For coordinate difference $(u,v)$, the squared Euclidean distance is

$$
Q(u,v)=u^2+uv+v^2. \tag{A1}
$$

Put

$$
H=\{(0,0),(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)\},
$$

and define the coordinate sets

$$
\begin{aligned}
T_1={}&H\cup\{(1,1),(-1,2)\},\\
T_2={}&\{(0,0),(1,0),(0,1),(-1,1),(-1,2),\\
 &\hspace{31mm}(1,1),(2,0),(1,-1),(0,-1)\}.
\end{aligned}
$$

Both $\phi(T_i)$ have squared-distance set $\{1,3,4,7\}$. Their multiplicities
in this order are

$$
\begin{array}{c|rrrr}
 &1&3&4&7\\ \hline
\phi(T_1)&16&9&7&4\\
\phi(T_2)&15&9&6&6
\end{array} \tag{A2}
$$


For an explicit integer check of (A2), the distance-degree vectors of vertices,
in squared-distance order $(1,3,4,7)$, have the following distributions. Summing
each coordinate and dividing by two gives the unordered pair counts.

| Model | Distance-degree vector | Number of vertices |
|---|---:|---:|
| $T_1$ | $(6,2,0,0)$ | 1 |
| $T_1$ | $(4,2,2,0)$ | 2 |
| $T_1$ | $(5,2,1,0)$ | 1 |
| $T_1$ | $(3,2,2,1)$ | 2 |
| $T_1$ | $(3,2,1,2)$ | 1 |
| $T_1$ | $(2,2,2,2)$ | 2 |
| $T_2$ | $(5,2,1,0)$ | 3 |
| $T_2$ | $(3,2,2,1)$ | 3 |
| $T_2$ | $(2,2,1,3)$ | 3 |

For the final model identify the plane with $\mathbb C$, put $s=\sqrt3$, and let
$\omega=e^{2\pi i/3}$. Set

$$
C=\{a\omega^j:a\in\{1,1+s,-(2+s)\},\ j=0,1,2\}.
$$

The three signed radii have distinct absolute values, so these are nine distinct
points. For real $a,b$, pairs with the same exponent have squared distance
$(a-b)^2$, while pairs with distinct exponents have squared distance
$a^2+ab+b^2$. There are three pairs of the first kind and six of the second
between two distinct three-point orbits. Within the orbit of radius $a$, there
are three pairs of squared distance $3a^2$.

Writing $a=1$, $b=1+s$, $c=-(2+s)$, the exact table is

$$
\begin{array}{c|c|c}
\text{pairs}&\text{squared distance}&\text{number}\\ \hline
\text{within }a&3&3\\
\text{within }b&12+6s&3\\
\text{within }c&21+12s&3\\
a,b\text{; same exponent}&3&3\\
a,b\text{; distinct exponents}&6+3s&6\\
a,c\text{; same exponent}&12+6s&3\\
a,c\text{; distinct exponents}&6+3s&6\\
b,c\text{; same exponent}&21+12s&3\\
b,c\text{; distinct exponents}&6+3s&6
\end{array}
$$

Hence $C$ has four squared distances, in increasing order,

$$
3,\quad6+3\sqrt3,\quad12+6\sqrt3,\quad21+12\sqrt3,
$$

with corresponding multiplicities

$$
(6,18,6,6). \tag{A3}
$$


The four models have distinct sorted multiplicity multisets:

$$
(9,9,9,9),\ (16,9,7,4),\ (15,9,6,6),\ (18,6,6,6).
$$

They are therefore pairwise nonsimilar. The nine-point classification implies
that they exhaust all nine-point four-distance sets. In particular, every such
set has at least three distance classes of multiplicity at most nine. Also, each
nonregular type contains a distance of multiplicity at least fifteen.


### A.2. The twelve-point model and an eleven-point example

In the same axial coordinates, define

$$
\begin{aligned}
U=\{&(0,1),(0,2),(0,3),\\
 &(1,0),(1,1),(1,2),(1,3),\\
 &(2,0),(2,1),(2,2),(3,0),(3,1)\}.
\end{aligned}
$$

Using (A1), its squared-distance set and multiplicities are

$$
\begin{array}{c|rrrrr}
\text{squared distance}&1&3&4&7&9\\ \hline
\text{multiplicity in }\phi(U)&24&15&12&12&3.
\end{array} \tag{A4}
$$

Here is a grouped exact check. The distance-degree vectors in the order
$(1,3,4,7,9)$ are:

| Vertices | Distance-degree vector | Number |
|---|---:|---:|
| $(1,1),(1,2),(2,1)$ | $(6,3,2,0,0)$ | 3 |
| $(0,2),(2,0),(2,2)$ | $(4,3,2,2,0)$ | 3 |
| The other vertices | $(3,2,2,3,1)$ | 6 |

Their sum is $(48,30,24,24,6)$, proving (A4). Shinohara's uniqueness theorem
implies that every twelve-point five-distance set is similar to this one. Thus
each has exactly three rare distances at threshold twelve.

Deleting $(1,1)$ from $U$ gives an eleven-point set with multiplicity vector

$$
(24,15,12,12,3)-(6,3,2,0,0)
=(18,12,10,12,3).
$$

It has exactly two rare distances at threshold eleven.

Every eleven-point subset of $\phi(U)$ has at least two distances occurring at
most eleven times: squared distance four has multiplicity ten because all
vertices have degree two in that class; squared distance nine has multiplicity
two or three. Also, every such subset retains at least $24-6=18$ pairs at the
shortest distance.


### A.3. Remaining cases at eleven, twelve, and thirteen points

The use of thirteen points below also invokes the source value $g(5)=12$, from
Erdős–Fishburn (1996), Theorem 1.


For $n=11$, a hypothetical counterexample must have exactly five distances. The
four nondiameter distances have multiplicity at least twelve and the diameter
has multiplicity at most seven. The diameter graph cannot have a one-vertex
cover: deleting that vertex would leave ten points with at most four distances,
contradicting $g(4)=9$. The unique twelve-point classification does not classify
all eleven-point five-distance sets, so Appendix A.2 does not exclude this case.

For $n=12$, a hypothetical counterexample has either five or six distances by
the counting bound (6) and $g(4)=9$. The five-distance case is excluded by (A4).
In the six-distance case the even-order equality argument forces five
multiplicities thirteen and a unique diameter. Deleting either endpoint gives an
eleven-point five-distance set with every multiplicity at most thirteen. Such a
set cannot be contained in a twelve-point five-distance set, because every
eleven-point subset of the unique twelve-point model retains a multiplicity at
least eighteen. If both endpoint deletions were regular hendecagons, their ten
shared vertices would force them to coincide. Therefore at least one is a
nonregular eleven-point five-distance set with maximum multiplicity at most
thirteen, not extendible to any twelve-point five-distance set. The supplied
classification results do not exclude such an eleven-point set.

For $n=13$, a hypothetical counterexample has exactly six distances, with five
nondiameter multiplicities at least fourteen and diameter multiplicity at most
eight. Its diameter graph cannot have a one-vertex cover. Otherwise deleting
that vertex leaves a twelve-point five-distance set and hence a class of
multiplicity at least twenty-four. Then the original thirteen-point set has at
least

$$
24+4\cdot14+1=81>\binom{13}{2}=78
$$

pairs, a contradiction. This is only a necessary condition, not a resolution for
thirteen points.

The uncontrolled cases involve arbitrary eleven-point five-distance sets or
larger few-distance sets, and no classification or extension principle for them
has been proved here.

## Appendix B. Affine obstruction and failed deformation transfer

### B.1. A finite linear-algebra test

There is also a finite-dimensional test. For every pair of equal-length
difference vectors $d,e$, form the traceless symmetric matrix
$dd^{\mathsf T}-ee^{\mathsf T}$. Let $V$ be their span in the
two-dimensional space of traceless symmetric $2\times2$ matrices. The
equivalent conditions hold exactly when $\dim V\le1$. Indeed, a nonzero
traceless symmetric $S$ orthogonal to $V$ gives a positive definite
nonscalar $Q=tI+S$ for sufficiently large $t$; conversely, the traceless
part of any admissible nonscalar $Q$ is a nonzero vector orthogonal to $V$.

### B.2. Explicit obstruction and safe direction of transfer

An equilateral triangle prevents the nonsimilarity affine condition of Section
3. In coordinates with unit edge vectors
$(1,0),(1/2,\sqrt3/2),(-1/2,\sqrt3/2)$, preserving equality of their
transformed squared lengths forces the off-diagonal entry of $Q$ to vanish and
its two diagonal entries to agree. A square also prevents the nonsimilarity
affine condition of Section 3: equality of horizontal and vertical side lengths
forces $q_{11}=q_{22}$, and equality of its two diagonal lengths forces
$q_{12}=0$. Thus even these elementary configurations force $Q$ to be
scalar.

Arbitrary perturbation does not repair this obstruction. It usually splits an
original distance class into smaller classes; these new classes can be rare even
when the original class was rich. Hence a lower bound for $R$ after a generic
perturbation does not transfer back. For example, six vertices of a regular unit
hexagon together with its center give seven points with multiplicities
$12,6,3$, and thus $R=2$. A generic sufficiently small perturbation gives 21
distinct distances, all rare.

In contrast, if an injective deformation preserves every original equal-distance
relation, each new class is a union of original classes. Every original class
inside a rare new class is itself rare, so
$R(\text{original})\ge R(\text{deformed})$. This is the safe direction of
transfer, but existence of such a useful deformation for arbitrary sets remains
unproved. The affine examples above show that it cannot always be achieved by a
nonsimilarity affine map.


## Appendix C. Failed abstract and component arguments

### C.1. Five-point nonrealizability of the ordered coloring

These are not planar counterexamples. Their restriction to the five
vertices $0,1,2,3,4$ already cannot be realized by planar points respecting
the color order.

Suppose it could be realized by $p_0,\ldots,p_4$, with distances $a>b>c>0$
for colors $0,1,2$. Then adjacent labels are at distance $a$, labels whose
difference is two or three are at distance $b$, and
$|p_0p_4|=c$.

Put $p_1=(0,0)$ and $p_2=(a,0)$. The conditions on $p_0$ and $p_3$ give

$$
p_0=\left(a-\frac{b^2}{2a},y\right),
\qquad
p_3=\left(\frac{b^2}{2a},z\right),
\qquad
y^2=z^2=b^2-\frac{b^4}{4a^2}>0.
$$

If $z=-y$, then

$$
|p_0p_3|^2=
\left(a-\frac{b^2}{a}\right)^2+4y^2
=a^2+2b^2>b^2,
$$

contrary to $|p_0p_3|=b$. Hence $z=y$, and $p_0,p_3$ are reflections of
each other across the perpendicular bisector of $p_1p_2$. Since
$|p_1p_4|=|p_2p_4|=b$, the point $p_4$ lies on this perpendicular
bisector. Therefore

$$
|p_0p_4|=|p_3p_4|=a,
$$

contradicting $|p_0p_4|=c<a$.

The obstruction is thus an exact relation between different distance
colors, not the numerical or abstract graph structure of diameter classes.


### C.2. A component criterion without a counting conclusion

For an actual planar point set $A$ and a distance $r$, form the graph
$G_r$ with vertex set $A$ and edges at distance $r$. If every nontrivial
connected component of $G_r$ has geometric diameter at most $r$, then
$m_A(r)\leq|A|$: within each such component, every $r$-edge is a diameter
edge, so the planar diameter bound applies separately; summing the vertex
counts gives the claim.

Equivalently, every rich distance $r$ has a connected component containing
two points at some distance greater than $r$. One can strengthen the
statement slightly by taking a component with positive graph excess
$e-v$: its geometric diameter must be greater than $r$.

This yields an upward dependency from each rich distance to a larger
distance. It does not give an injection into rare distances, a branching
bound, or any useful restriction on how many rich distances can depend on
the same larger distance. No such missing assertion is established here.

## Appendix D. Superseded and unsuccessful approaches

This section records work already undertaken. It does not propose additional
assertions as established results.

### D.1. A valid but superseded sampling bound for the largest distances

Before the direct angular proof, an independent-set sampling argument gave an
exponential-in-rank bound. It is retained because it isolates what can be
obtained using only hereditary diameter counting.

Let $F_k(B)$ be the graph consisting of pairs at the $k$ largest distances
of $B$, or all its pairs if it has fewer than $k$ distances. One can prove

$$
 |E(F_k(B))|\le C_k|B|,\qquad
 C_1=1,\qquad C_k=(1+4\mathrm e)C_{k-1}+\mathrm e,
$$

where $\mathrm e$ denotes Euler's number. Equivalently,

$$
 C_k=\frac{5(1+4\mathrm e)^{k-1}-1}{4}.
$$


For the inductive step, let $r$ be the $k$-th largest distance and let $G$
consist of all pairs longer than $r$. The inductive bound holds on every
induced subset, since its edges lie among at most the $k-1$ largest distances
of that subset. Hence every induced subgraph of $G$ has a vertex of degree at
most $2C_{k-1}$. Orient its edges according to a successive low-degree
deletion order; every outdegree is at most $2C_{k-1}$.

Independently mark vertices with probability $p$, and retain a marked vertex
only if all its outneighbors are unmarked. The retained set $S$ is independent
in $G$, so all its distances are at most $r$, and its distance-$r$ graph
has at most $|S|$ edges by the diameter theorem. For an original
distance-$r$ edge, its endpoints are not adjacent in $G$, so both are
retained with probability at least

$$
 p^2(1-p)^{4C_{k-1}}.
$$

Also $\mathbb E|S|\le p|B|$. Therefore

$$
 m_B(r)\le\frac{|B|}{p(1-p)^{4C_{k-1}}}.
$$

Choosing $p=1/(4C_{k-1}+1)$ gives

$$
 m_B(r)\le\mathrm e(4C_{k-1}+1)|B|,
$$

which proves the recurrence. If fewer than $k$ distances exist, the
preceding-rank bound suffices instead.

Combined with layer support, this already proved divergence when every fixed
layer prefix is $o(n)$, but yielded only a logarithmic quantitative bound in
$n/h$. It is not a failed proof: it is a weaker valid argument. Lemma 2
supersedes it by proving $m_B(r)\le2k|B|$, and consequently a quadratic rather
than exponential bound on the total number of pairs at the first $k$
distances.

### D.2. Convex-subset and point-deletion transfers

Applying a rare-distance theorem to a convex subset $B\subset A$ controls
$m_B(r)$, not $m_A(r)$. Restoring the other points may add both cross-pairs
and pairs among the restored points. No bound was established that keeps enough
of these distances below the full threshold $n$.

The small even-order argument does not justify a general deletion principle. It
works because pair counting forces a **unique** diameter and exactly $n+1$
occurrences of every other class. Deleting one endpoint removes the diameter and
cannot eliminate any other class: at most $n-1$ incident pairs disappear,
leaving at least two occurrences. Outside this equality case, the needed
residual classification and multiplicity control are missing.

### D.3. Generic deformation and the strict half-width condition

Generic perturbation typically destroys equalities. The regular hexagon with its
center has multiplicities $(12,6,3)$, hence $R=2$ at $n=7$; a generic
small perturbation has 21 distinct distances, all rare. Thus a lower bound after
perturbation gives no lower bound before perturbation. The usable affine
hypothesis in Section 3 is preservation of every original equal-distance
relation, not merely injectivity or preservation of inequalities between
previously distinct lengths.

In the coordinate-splitting proof, the long-horizontal condition must be
$a>W/2$, not $a\ge W/2$. The proof excludes neighbors on both abscissae
$x-a$ and $x+a$ only in the strict case. Points on the middle fiber are
therefore handled separately by globally rare vertical distances. The
distinctness of these two collections uses the splitting hypothesis; it is not a
conclusion of their being represented by different pairs.

### D.4. Translation directions and graph excess

A fixed nonzero displacement vector gives a graph made of finite translation
chains, so its unordered edge count is at most $n-1$. This suggested
extracting rare distances from extremal displacement vectors. The missing step
is that a Euclidean distance can combine many different directions of the same
norm. Rarity of a direction class is not rarity of the full distance class. The
affine hypothesis solves this only by restricting a distance to at most two
unoriented directions of the form $(a,b)$ and $(a,-b)$.

Likewise, a rich distance graph has more edges than vertices and therefore a
component of positive graph excess. Appendix C.2 forces a larger distance within
such a component. This does not count distinct larger classes: many rich classes
might lead to the same larger one. No injection or bound on this multiplicity of
dependence was found. The abstract construction in Section 4 shows that even
strong hereditary restrictions on maximum-color graphs cannot substitute for
relations between different Euclidean lengths.

### D.5. Selecting only the smallest and second-largest distances

The second-largest distance is not always rare. The supplied Vesztergombi paper
states and constructs examples attaining $m_A(d_2)=3n/2$. Its original passage
was read; the direct rank bound here does not assume the contrary.

Nor does selecting the smaller-multiplicity class among the shortest and
second-largest distances suffice. The supplied Clemen–Dumitrescu–Liu Proposition
1.5 gives constructions with

$$
 m_A(d_2)\ge3m,\qquad m_A(\delta)\ge3n-5m+o(m).
$$

Taking $m$ asymptotic to $3n/8$ gives both multiplicities at least
$9n/8+o(n)$. The statement and construction passage were read during the
investigation. This source construction was not independently reconstructed in
full; it is recorded as a sourced obstruction and is not needed for any
independently proved bound above.

### D.6. Many rich distances do not give few rare distances

The supplied Bhowmick construction was read. In its odd-order case, two rotated
regular $(m+1)$-gons sharing one vertex give $n=2m+1$ points. Each of
$\lfloor m/2\rfloor$ selected polygon chord lengths has at least

$$
 2(m+1)=n+1
$$

unordered occurrences, because the two polygons share no pair of vertices. This
establishes many rich classes. It does not control the additional distances
between the two polygons and does not bound the number of rare classes. The
analogous reflection construction has the same logical limitation for the
present problem. These constructions were not treated as counterexamples to
either requested assertion.

## Appendix E. Exact endpoint, verification status, and unresolved uncertainties

**The range $n\ge5$ is retained.** At four points, the coordinates

$$
 (0,0),\quad(1,0),\quad(1/2,\sqrt3/2),\quad(1/2,-\sqrt3/2)
$$

give five unit pairs and one pair of length $\sqrt3$, hence $R=1$. This does
not bear on the intended first question and does not obstruct the asymptotic
question.

**What is proved here.** The depth-sum restriction, angular degeneracy lemma,
layer and separation bounds, coordinate-splitting theorem, affine criterion,
exact model counts, and abstract countermodel/nonrealizability calculation have
explicit arguments in this record. The finite-order conclusion through ten
points uses the stated published classifications as inputs. In particular, the
nine-point models are identified by exhibiting four pairwise nonsimilar examples
when the classification permits only four types, not by guessing figures that
were not reproduced.

**What is imported.** The diameter theorem and the few-distance classifications
are source theorems, not discoveries or exhaustive classifications independently
reproved in this investigation. The twelve-point uniqueness input is Shinohara's
Theorem 1.2(b). The optional $O(s^{4/3})$ incidence estimate is used only as
stated in the supplied Clemen–Dumitrescu–Liu Section 1.4; the independent
elementary bounds do not depend on it. A transcription coefficient in their
two-layer proof is corrected explicitly in Section 5. No claimed error in the
final source theorem follows from that correction.

**Checks performed.** Exact coordinate calculations were checked by
squared-distance formulas, integer distance-degree tables, and the symbolic
three-orbit table in Appendix A; their pair totals are respectively 36, 66, and
55 for nine, twelve, and eleven points. The checks are reproducible from the
tables without floating-point tests. The delicate geometric checks include
nonvertex convex combinations on degenerate layers, strict increases of
distance, leftmost-coordinate ties in the closed semicircle, cosine monotonicity
through the endpoint $\pi$, existence of enough ranked distances, and survival
of nondiameter classes after endpoint deletion.

**Unresolved finite cases.** No argument excludes every eleven-point
five-distance set with only one rare class. Nor does the twelve-point uniqueness
theorem classify arbitrary eleven-point five-distance sets. At twelve points the
only remaining one-rare pattern identified here is five multiplicities 13 and a
unique diameter. Appendix A.3 gives further necessary conditions, not a proof of
nonexistence. The thirteen-point restrictions are likewise only necessary
conditions.

**Unresolved asymptotic case.** A bounded-$R$ sequence must have a macroscopic
convex layer at bounded depth. No argument controls this regime. For convex
sets, the available distinct-distance and multiplicity counts reduce bounded
$R$ to $q=n/2+O(1)$, but no general bounded-excess classification or
stability theorem was proved or supplied. Even divergence restricted to
arbitrary convex sets is not established by this record.

**Scope of the conclusion.** Neither universal assertion has been proved or
disproved here. The abstract colorings are explicitly non-Euclidean and are not
planar counterexamples. There is no claimed extension from convex sets,
affine-deformable sets, or sparse-layer sequences to all planar sets. No
statement about novelty or the complete later literature was verified. No
unavailable earlier research notes, external web material, or later papers were
consulted. This record does not assert that the remaining gaps have been
resolved.

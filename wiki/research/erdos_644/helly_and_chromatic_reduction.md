---
name: research/erdos_644/helly_and_chromatic_reduction
desc: An exact chromatic reformulation, a shortest-edge half-rank bound at Helly number three, logarithmic bounds for Helly families, and the sharp six-edge theorem for linear families.
tags: [proved, restricted-upper-bounds, reductions]
sources: []
created: 2026-09-23T00:23:41Z
updated: 2026-10-13T05:28:09Z
---


# research/erdos_644/helly_and_chromatic_reduction

***

This route replaces transversals by colorings of the minimal empty-intersection
obstructions. In the Helly case these obstructions form a graph, and counting
its maximal independent sets gives a logarithmic bound, much smaller than a
positive linear coefficient. The exact reformulation also applies to arbitrary
families, but the counting argument does not yet extend beyond graphs. Neither
assertion of Problem 644 is resolved.

All hypergraphs below are finite and have nonempty edges. Write $P_r$ for the
condition on **at most** $r$ edges. For the exactly-$r$ convention, the same
conclusions apply when there are at least $r$ distinct edges; otherwise use the
trivial transversal bound $r-1$.

## An exact chromatic reformulation

Index the edges of $\mathcal H$ by a set $I$. Form a clutter $\mathcal F$ on $I$
whose edges are the inclusion-minimal subfamilies with empty common
intersection. Singletons are not edges of $\mathcal F$. A subset $J\subseteq I$
is independent in $\mathcal F$ exactly when the corresponding hyperedges have a
common point.

Consequently

$$
\tau(\mathcal H)=\chi(\mathcal F),
\tag{1}
$$

where a proper coloring of a hypergraph means that no edge is monochromatic. A
color class can be covered by its common point; conversely a transversal
assigns each original edge to one of its selected points. Also

$$
P_r\quad\Longleftrightarrow\quad
\mathcal F[J]\text{ is 2-colorable for every }|J|\le r.
\tag{2}
$$


Every maximal independent set of $\mathcal F$ is the complete incidence star of
some original point. Indeed, choose a point common to its indexed edges; its
full star contains that independent set and so equals it by maximality. Distinct
maximal independent sets require distinct points. Thus, writing
$m_i(\mathcal F)$ for the number of maximal independent sets containing $i$,

$$
m_i(\mathcal F)\le |E_i|\le k.
\tag{3}
$$


Conversely, for a finite clutter $\mathcal F$ without singleton edges, take its
maximal independent sets as ground points and put

$$
E_i=\{J:J\text{ is maximal independent in }\mathcal F,\ i\in J\}.
$$

This recovers (1) and (2), with rank $\max_i m_i(\mathcal F)$. Repeated rows can
be identified without changing transversal numbers or the at-most-$r$ condition.
Private padding then makes the family uniform without changing any subfamily's
transversal number.

Hence the unrestricted problem can equivalently be phrased as bounding the
chromatic number of a clutter satisfying (2), in terms of the largest number of
its maximal independent sets through a vertex. This is a reformulation, not an
upper bound.

## The Helly case is logarithmic

A family is **Helly** here if every pairwise-intersecting subfamily has a common
point. Its minimal empty-intersection obstructions are exactly pairs of disjoint
edges. Thus $\mathcal F$ is the disjointness graph $G$ of $\mathcal H$, and

$$
\tau(\mathcal H)=\chi(G).
$$

Property $P_3$ makes $G$ triangle-free. For a Helly family, $P_7$ is exactly the
condition that $G$ has no odd cycle of length at most seven.

**Theorem.** If a Helly rank-$k$ family satisfies $P_3$, then

$$
\boxed{\tau(\mathcal H)\le\lfloor\log_2 k\rfloor+2.}
\tag{4}
$$

More precisely, if $t=\tau(\mathcal H)\ge3$, then

$$
k\ge2^{t-1}-t+1.
\tag{5}
$$

In particular, every fixed-$r$ Helly subclass with $r\ge3$ has zero linear
coefficient. Compactness, as recorded in
[Structural reductions](structural_reductions.md), extends the bound to infinite
families of finite rank under the at-most-$r$ convention.

This excludes the graph construction in §6.5 of
[second independent record](independent/fractional_reductions_and_good_triples.md),
rather than merely leaving its ratio unknown. For a graph with no odd cycle of
length at most seven, let $E_v$ consist of the maximal independent sets
containing $v$, as proposed there. Pairwise-intersecting rows correspond to
pairwise nonadjacent graph vertices, which form an independent set and extend to
a maximal one. Thus the row family is Helly. Its rank is $k=\max_v m_v(G)$, and
(4) gives $\chi(G)=\tau\le\lfloor\log_2k\rfloor+2$. Private padding preserves
these transversal numbers and cannot improve the ratio.

### Counting maximal independent sets

For a graph $G$, let $M(G)$ be its number of maximal independent sets, including
the empty independent set when $G$ is empty, and let $m_v(G)$ count those
containing $v$. We prove

$$
G\text{ triangle-free}\quad\Longrightarrow\quad
M(G)\ge2^{\chi(G)}-\chi(G).
\tag{6}
$$


First, for any graph with an edge, put $M=M(G)$ and $s=\min_v m_v(G)$. Represent
$v$ by the set $S_v\subseteq[M]$ of maximal independent sets containing it.
These supports have size at least $s$, and adjacent vertices have disjoint
supports. In particular $M\ge2s$.

There is a coloring with $M-2s+2$ colors. If $S_v$ contains one of the first
$M-2s+1$ coordinates, color $v$ by its first such coordinate. All remaining
supports lie in the same $2s-1$ coordinates; as each has size at least $s$, they
intersect pairwise, so the remaining vertices form an independent final color
class. Hence

$$
M(G)\ge 2\min_v m_v(G)+\chi(G)-2.
\tag{7}
$$


Now assume $G$ is triangle-free and $t=\chi(G)\ge3$. Its open neighborhood
$N(v)$ is independent. The graph $G-N[v]$ is nonempty, and coloring it, giving
$N(v)$ one new color, and reusing an old color at $v$ proves

$$
\chi(G-N[v])\ge t-1.
\tag{8}
$$

There is a bijection between maximal independent sets containing $v$ and maximal
independent sets of $G-N[v]$, obtained by deleting or adjoining $v$. Therefore

$$
m_v(G)=M(G-N[v]).
\tag{9}
$$


Induct on the number of vertices. Formula (6) is immediate for chromatic number
zero, one, or two. For $t\ge3$, (8), (9), and the induction hypothesis give

$$
m_v(G)\ge2^{t-1}-(t-1).
$$

Substitution in (7) proves (6). Applying the same estimate to each vertex of the
disjointness graph and then using (3) proves (5). Since $2^{t-1}-t+1\ge2^{t-2}$
for $t\ge3$, it also proves (4).

## A sharper finite check using all seven local edges

For Helly $P_7$ families,

$$
k\le4\quad\Longrightarrow\quad\tau\le2,
\tag{10}
$$

and, when $t=\tau\ge4$,

$$
k\ge15\cdot2^{t-4}-t+1.
\tag{11}
$$


Here are elementary counts establishing these refinements. The number $Q_j$ of
maximal independent sets in a $j$-vertex path satisfies

$$
Q_0=Q_1=1,\quad Q_2=2,\qquad
Q_j=Q_{j-2}+Q_{j-3}\quad(j\ge3).
$$

Separate independent sets containing the first endpoint from those instead
containing its neighbor. In particular $Q_6=5$ and $Q_9=12$.

The cycle $C_9$ has twelve maximal independent sets: three of size three, with
all cyclic gaps equal to three, and nine of size four, with gaps $3,2,2,2$.
Maximal-independent-set counts cannot decrease on passing from an induced
subgraph to the full graph: extend each maximal independent set, noting that its
intersection with the original vertex set cannot change. The same holds for
counts through a fixed vertex.

A nonbipartite graph of odd girth at least nine contains an induced odd cycle of
length $g\ge9$. At a vertex of this cycle there are $Q_{g-3}\ge Q_6=5$ maximal
independent sets containing it, proving (10). The graph has at least twelve
maximal independent sets: use the count for $C_9$, or an induced nine-vertex
path in a longer odd cycle.

The induction proving (6), now starting at $M(G)\ge12$ for chromatic number
three, gives

$$
M(G)\ge15\cdot2^{t-3}-t\qquad(t\ge3)
$$

for graphs of odd girth at least nine. Applying this to $G-N[v]$ proves (11).
These improvements change only the additive constant in the logarithmic bound.

The threshold in (10) is sharp. Apply the canonical construction above to
$G=C_9$. Its twelve maximal independent sets are the ground points. Cyclic
symmetry and the preceding size counts show that each graph vertex belongs to
$(3\cdot3+9\cdot4)/9=5$ of them. The resulting family is 5-uniform and Helly,
has transversal number three, and even satisfies $P_8$, since every proper
induced subgraph of $C_9$ is bipartite.

## Why this does not reduce the arbitrary case

Without Helly, the disjointness graph loses the obstruction. Complete-family
examples with $n=\lceil7k/4\rceil-1$ are pairwise intersecting and have $P_7$
and $\tau=\lceil3k/4\rceil$, although their disjointness graph is empty. Their
minimal empty-intersection clutter, not just its pair edges, must be retained.

Nor can deleting a subfamily with small transversal number generally make a
$P_7$ family Helly. If $\mathcal H$ satisfies $P_3$ (in particular, if it
satisfies $P_7$), $\mathcal D\subseteq\mathcal H$, and
$\mathcal H\setminus\mathcal D$ is Helly, then

$$
\tau(\mathcal D)\ge
\tau(\mathcal H)-\lfloor\log_2 k\rfloor-2,
$$

by covering the two parts separately and applying (4). Thus a family with linear
transversal number requires a linear-transversal deletion cost. Adding common
points to enforce Helly can instead collapse the transversal number; no
small-loss completion is available.

Checking intersections only up to a fixed number of edges is also insufficient.
For fixed $h\ge3$, the complete $k$-uniform family on
$n=\lceil hk/(h-1)\rceil-1$ points has every at-most-$h$ edges intersecting,
since $h(n-k)<n$. It has $P_7$ because $n<7k/4$, but its transversal number is
$\lceil k/(h-1)\rceil$, still linear. This finite-order intersection condition
must not be confused with a bounded Helly number, which asserts the existence of
a small witness whenever an intersection is empty.

## A shortest-edge bound for bounded Helly number

There is a direct linear improvement for Helly number three, even though the
sublinear counting question below remains open in these notes.

**Theorem.** Suppose a family $\mathcal H$ of nonempty finite sets has Helly
number at most $h$: every finite subfamily with empty intersection contains at
most $h$ members with empty intersection. If $\mathcal H$ has $P_{2h+1}$, then,
for every $A\in\mathcal H$,

$$
\boxed{\tau(\mathcal H)\le\left\lceil\frac{|A|}{2}\right\rceil+1.}
\tag{BH}
$$

In particular, a rank-$k$, Helly-number-three $P_7$ family has
$\tau\le\lceil k/2\rceil+1$.

**Proof.** Partition $A=B\sqcup C$ as evenly as possible and put

$$
\mathcal F_B=\{E\in\mathcal H:E\cap A\subseteq B\},\qquad
\mathcal F_C=\{E\in\mathcal H:E\cap A\subseteq C\}.
$$

If both residuals have transversal number greater than one, each has empty total
intersection. This has a finite witness even if the family is infinite: fix one
finite edge and, for each of its points, choose an edge missing that point. The
Helly hypothesis therefore supplies at most $h$ rows of each residual with empty
intersection.

Apply $P_{2h+1}$ to these rows and $A$. A two-cover has a point $x\in A$. If
$x\in B$, it misses all chosen $\mathcal F_C$ rows, forcing the other point into
their empty intersection. If $x\in C$, use the $\mathcal F_B$ rows instead. This
is impossible. Hence, say, $\tau(\mathcal F_B)\le1$. Its transversal, together
with $C$, covers $\mathcal H$ and proves (BH). An empty residual uses an empty
transversal. $\square$

Equivalently, for fixed $A$, the subsets $B\subseteq A$ for which
$\tau(\mathcal F_B)>1$ form an intersecting upward-closed family. If
$\mathcal L_A$ is the family of its minimal members, then

$$
\tau(\mathcal H)\le\tau(\mathcal L_A)+1:
$$

a transversal $D\subseteq A$ of $\mathcal L_A$ makes $A\setminus D$ nonbad. This
reformulation alone gives no sublinear bound, since arbitrary intersecting
families on $A$ can have transversal number of order $|A|/2$.

Under the exactly-$(2h+1)$ convention, apply the theorem when there are at least
$2h+1$ edges; otherwise use the vacuous-case bound $2h$. In particular, a
fixed-excess three-quarter counterexample must have Helly number at least four.
No reduction to bounded Helly number has been established.

## The counting question at Helly number three

If every empty intersection has a witness of size at most three, the clutter
$\mathcal F$ in (1) has rank at most three. Bound (BH) applies. The following
additional constraint survives, but no corresponding global counting theorem
giving a sublinear bound was obtained.

**Contraction-clique lemma.** Suppose $\mathcal F$ has edge sizes two or three
and every induced subclutter on at most seven vertices is 2-colorable. Fix a
vertex $v$, exclude its 2-edge neighbors, and on the other vertices form the
graph

$$
xy\in E(J_v)\quad\Longleftrightarrow\quad
\{x,y\}\in\mathcal F\ \text{or}\ \{v,x,y\}\in\mathcal F.
$$

For every clique $S$ of $J_v$, either $\mathcal F[S]$ has no edges or its edges
have a common vertex. In particular $\chi(\mathcal F[S])\le2$.

To prove this, take $X\subseteq S$ with $|X|\le6$ and color
$\mathcal F[X\cup\{v\}]$ with two colors. At most one vertex of $X$ has the
color of $v$, by the definition of $J_v$. That at-most-one vertex therefore
meets every edge of $\mathcal F[X]$.

Any family of nonempty sets of size at most three with empty total intersection
has such a witness whose union has size at most six. Choose an inclusion-minimal
witness $B_1,\ldots,B_q$, and points $x_i$ in all its members except $B_i$.
These points are distinct, so $q\le4$. For $q=2,3,4$, the union has size at most
$6,6,4$, respectively: each $B_i$ already contains the other $q-1$ distinguished
points. A failure of the common-vertex assertion for $\mathcal F[S]$ would
therefore contradict the preceding paragraph on a set $X$ of at most six
vertices. This proves the lemma.

The graph induction itself does not survive contraction. For an arbitrarily
large set $S$, the clutter

$$
\mathcal F=\{\{v,x,y\}:x,y\in S,\ x\ne y\}
$$

is globally 2-colorable, but contraction at $v$ produces the complete graph on
$S$. Thus it preserves neither triangle-freeness nor the seven-vertex local
condition. The contraction-clique lemma controls these cliques in the original
clutter, but a way to turn that control into a bound on maximal independent sets
is still missing.

### A support-count inequality, but no contraction recurrence

There is a generalization of (7). Let $\mathcal F$ be a finite clutter with at
least one edge, no singleton edges, and rank at most $h\ge2$. Let $M$ be its
number of maximal independent sets and $s=\min_v m_v(\mathcal F)$. Then

$$
M\ge\chi(\mathcal F)+\left\lceil\frac{hs}{h-1}\right\rceil-2.
\tag{H}
$$

Represent each vertex by its support among the $M$ maximal independent sets.
Each support has size at least $s$, while the supports on any edge have empty
common intersection. In particular $M\ge\lceil hs/(h-1)\rceil$. Put
$L=\lceil hs/(h-1)\rceil-1$, and color every vertex whose support meets the
first $M-L$ coordinates by the first such coordinate. All remaining supports lie
in the same $L$ coordinates. Any at most $h$ of them intersect, since

$$
hs-(h-1)L>0.
$$

Their vertices therefore form one independent color class. This gives
$\chi\le M-L+1$ and proves (H).

For $h=3$ this is $M\ge\chi+\lceil3s/2\rceil-2$. It does not give the needed
recurrence for the number of maximal independent sets through a vertex:
contraction still creates new constraints and may destroy locality. No sublinear
transversal bound for all fixed-Helly-number-three $P_7$ families was proved.

The tempting stronger claim without $P_7$, that every pairwise-intersecting
Helly-number-three family has $\tau\le k/2+O(1)$, is false. All lines of a
projective plane of prime-power order $q$ form a pairwise-intersecting family
with Helly number three and

$$
k=\tau=q+1.
$$

Two lines meet in one point; if a line collection is not concurrent, two lines
together with a third avoiding their intersection witness its empty
intersection. A line is a transversal of size $q+1$, while $q$ points meet at
most $q(q+1)<q^2+q+1$ lines. This example lacks $P_7$; it rules out discarding
the local hypothesis in that proposed rank-three shortcut.

## Linear families: six local edges suffice exactly

A family is linear if every two distinct edges intersect in at most one point.
There is a stronger conclusion than the earlier bound $\tau\le3$ from bounded
pair intersections:

$$
\boxed{\mathcal H\text{ linear and }P_6\quad\Longrightarrow\quad\tau(\mathcal H)\le2.}
\tag{L}
$$

No rank bound is needed. The threshold six is sharp.

To prove (L), take a finite inclusion-minimal subfamily $\mathcal C$ with no
two-cover, if one exists. Deleting any edge admits a two-cover. Every point
occurs in at most three edges of $\mathcal C$. Indeed, if $v$ occurs in at least
four, delete one incident edge $E$. A two-cover of the remainder has a point in
at least two of the other edges containing $v$. By linearity that point must be
$v$ itself, so the cover also meets $E$, a contradiction. Since two points cover
$\mathcal C\setminus\{E\}$, it follows that $|\mathcal C|-1\le6$, so
$|\mathcal C|\le7$.

The case $|\mathcal C|=7$ is impossible. Deleting a row $r$ requires two points
whose incidence stars $A,B$ are disjoint three-subsets of the other six row
indices. Distinct points have stars intersecting in at most one row, again by
linearity. Any other three-element star must consequently contain $r$ and one
index from each of $A,B$. It meets both $A,B$, and any two such other stars meet
at $r$. Thus $A,B$ are the only disjoint pair of three-element stars. They
cannot cover the six rows left after deleting a row other than $r$. This
contradicts minimality and proves $|\mathcal C|\le6$.

For sharpness, take the seven lines of the Fano plane. Every five lines have a
two-cover: their fifteen incidences on seven points force a point on three of
the selected lines, and the other at most two lines have a common point. But any
two points meet at most five of the seven lines, so any six lines have no
two-cover. This linear family therefore has $P_5$ but transversal number three.

The same minimality argument gives a separate bounded-multiplicity statement. If
every two distinct ground points occur together in at most $\lambda$ edges, a
minimal family without a two-cover has maximum point degree at most $2\lambda+1$
and at most $4\lambda+3$ edges. Otherwise deleting an edge at a higher-degree
point forces that point into every two-cover of the remainder. Hence
$P_{4\lambda+3}$ implies a global two-cover under this hypothesis. For
$\lambda=1$, the preceding argument sharpens seven to the exact threshold six.
This bounds co-occurrence of pairs of points, not just the sizes of pairwise
edge intersections when $\lambda>1$.

The linear theorem addresses a restricted incidence class. The remaining
Helly-number-three problem permits nonlinear incidence and is not resolved by
(L).

## Connected disjointness references without Helly

One part of the graph viewpoint does apply to arbitrary $P_7$ families. Let $q$
reference edges, $2\le q\le6$, have connected bipartite disjointness graph, with
bipartition $L,R$. Put

$$
P=\bigcap_{i\in L}A_i,\qquad Q=\bigcap_{j\in R}A_j.
$$

Their two-point transversals are exactly the pairs in $P\times Q$. Each
reference edge must contain exactly one point of any two-cover, since it has a
disjoint neighbor. The resulting proper 2-coloring is unique up to
interchange, proving the assertion. In particular $P,Q$ are nonempty and
disjoint.

For positive integers $u,v$ with $uv\le7-q$, partition $P$ into $u$ balanced
parts and $Q$ into $v$ balanced parts, allowing empty parts. The unions of one
part from each side contain every possible pair. Choosing an edge avoiding each
union, if their sizes were all smaller than $\tau$, would contradict $P_7$.
Hence

$$
\tau(\mathcal H)\le
\left\lceil\frac{|P|}{u}\right\rceil+
\left\lceil\frac{|Q|}{v}\right\rceil.
\tag{12}
$$


For three distinct edges $A,B,C$ with $A\cap B=B\cap C=\varnothing$, set
$a=|A\cap C|$. In a $k$-uniform family, (12) gives

$$
\tau(\mathcal H)\le
\min\{a+\lceil k/4\rceil,\ \lceil a/2\rceil+\lceil k/2\rceil\}.
$$

Thus a hypothetical excess $\tau>(3/4+\varepsilon)k$ forces distinct neighbors
of any vertex in the disjointness graph to intersect in more than
$(1/2+2\varepsilon)k-O(1)$ points. This is a conditional restriction, not a
proof that disjoint edges are impossible in a counterexample. No general
three-quarter bound follows yet.

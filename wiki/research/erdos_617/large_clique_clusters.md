---
name: research/erdos_617/large_clique_clusters
desc: Near-full clique clusters have only order r excess incidences; joint deficit and variance accounting bounds their number by r plus one for large r.
tags: [graph-theory, proved, stability]
sources: []
created: 2026-09-22T00:27:20Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/large_clique_clusters

***

**Status.** The following is a proved structural consequence of the hereditary
density inequalities and the localized independence inequality recorded in
[Packing tools](packing_tools.md). It does not resolve Problem 617 or produce a
packing of full $K_r$'s.

Let $r$ be an integer at least three, and put

$$
N=r^2+1,\qquad
p_r(rq+b)=r\binom q2+qb\quad(0\le b<r),
\qquad
D_r(n)=\binom n2-(r-1)p_r(n).
$$

Suppose that a graph $G$ on $N$ vertices satisfies

$$
\alpha(G)\le r,\qquad 2e(G)\le rN,
\qquad e(G[W])\le D_r(|W|)\quad(W\subseteq V(G)).
\tag{1}
$$

In particular, a least color in a hypothetical counterexample satisfies (1).

Write $c(v)$ for the largest order of a clique containing $v$. The
$(r+1)$-vertex case of (1) gives $c(v)\le r$ for $r\ge3$. The localized
independence inequality, in the uniform-vector form already checked in the
research notes, gives

$$
2e(G)+N+\sum_v c(v)\ge\frac{2N^2}{r}.
\tag{2}
$$

Consequently, putting $D=\sum_v(r-c(v))$, we have

$$
D\le N\left(1-\frac2r\right),
\qquad
\sum_v\bigl(d(v)-c(v)+1\bigr)
\le \left(2-\frac2r\right)N.
\tag{3}
$$

The second inequality follows by combining (2) with $4e(G)\le2rN$. Each summand
in that inequality is nonnegative.

## 1. The clustering lemma

Fix an integer $k\ge1$ such that

$$
r>(k+1)^2+1,\qquad r-3k\ge2,\qquad
r-1>\frac32k(k+1).
\tag{4}
$$

Let $\mathcal Q$ consist of all cliques of order at least $r-k$. Join two such
cliques when their intersection has at least two vertices, and let
$C_1,\ldots,C_q$ be the unions of the connected components of this
clique-intersection graph. Then

1. $|C_j|\le r$ for every $j$;
2. cliques belonging to distinct components intersect in at most one vertex;
3. if $q_v=|\{j:v\in C_j\}|$ and

$$
   L=\sum_v\max(q_v-1,0),
$$

   then

   $$
   L\le\frac{(2-2/r)N}{r-k-1};
   \tag{5}
   $$

4. the uncovered set $U=V(G)\setminus\bigcup_j C_j$ satisfies

$$
   |U|\le\frac{D}{k+1}.
   \tag{6}
$$


### Pairwise intersection and transitivity

Take cliques $Q,R$ of orders $r-t,r-u$, where $0\le t,u\le k$, and put
$h=|Q\cap R|$. Suppose that $h\ge2$ and $|Q\cup R|\ge r+1$. Its order is

$$
n=2r-t-u-h\in[r+1,2r].
$$

All nonedges of $G[Q\cup R]$ are between $Q\setminus R$ and $R\setminus Q$.
Therefore the inherited density inequality requires

$$
(r-t-h)(r-u-h)\ge(r-1)(r-t-u-h).
$$

Equivalently,

$$
f(h):=h^2+h(t+u-r-1)+tu-t-u+r\ge0.
\tag{7}
$$

The allowed interval is $2\le h\le r-t-u-1$. At both endpoints,

$$
f(2)=f(r-t-u-1)=tu+t+u+2-r
\le(k+1)^2+1-r<0.
$$

Since $f$ is convex, (7) is impossible throughout the interval. Thus

$$
|Q\cap R|\ge2\quad\Longrightarrow\quad |Q\cup R|\le r.
\tag{8}
$$


If $Q,R,S\in\mathcal Q$ and both $|Q\cap R|$ and $|R\cap S|$ are at least two,
then (8) gives

$$
\begin{aligned}
|Q\cap S|
&\ge |Q\cap R|+|R\cap S|-|R|\\
&\ge |Q|+|R|+|S|-2r\ge r-3k\ge2.
\end{aligned}
$$

Consequently the intersection-at-least-two relation is transitive (with its
evident reflexive interpretation). Every two cliques in one connected component
intersect in at least two vertices, and (8) applies to them.

### Each cluster union has at most $r$ vertices

Fix an anchor clique $Q$ in one component, with $|Q|=r-t$, $0\le t\le k$. For
any vertex $x$ of its cluster union outside $Q$, choose a clique $R$ of that
component containing $x$. The preceding transitivity argument and (8) give

$$
|Q\cap R|\ge |Q|+|R|-r\ge |Q|-k.
$$

The vertex $x$ is adjacent to every vertex of $Q\cap R$, so it has at most $k$
nonneighbors in $Q$.

If the cluster union had at least $r+1$ vertices, choose $t+1$ of these outside
vertices. Their union with the *entire* anchor $Q$ has exactly $r+1$ vertices.
Its number of nonedges is at most

$$
k(t+1)+\binom{t+1}{2}
\le\frac32k(k+1)<r-1.
$$

This contradicts $D_r(r+1)=\binom{r+1}{2}-(r-1)$, proving $|C_j|\le r$. Notice
that this argument follows the transitivity proof; no bound on a cluster union
was used in proving transitivity.

### Overlaps and uncovered vertices

For a covered vertex $v$, a maximum clique through $v$ belongs to one of its
$q_v$ clusters. Choose that clique, and choose one clique through $v$ from each
of its other clusters. Any two chosen cliques intersect only in $v$: an
intersection of size at least two would put them in the same cluster. Hence
their sets of neighbors of $v$ are disjoint and

$$
d(v)\ge c(v)-1+(q_v-1)(r-k-1).
$$

For an uncovered vertex, $d(v)\ge c(v)-1$ still holds. Summing and using (3)
proves (5). An uncovered vertex has $c(v)\le r-k-1$, hence $r-c(v)\ge k+1$;
summing proves (6).

## 2. Number and total deficits of maximum anchors

In each cluster choose a clique $Q_j$ of maximum order *among all cliques in
that cluster*, and write

$$
|Q_j|=r-t_j,\qquad 0\le t_j\le k,
\qquad T=\sum_{j=1}^q t_j.
$$

Then

$$
\sum_j(r-t_j)t_j\le D+kL,
\qquad
(r-k)T\le D+kL.
\tag{9}
$$


Here is a vertexwise check of the first inequality, which avoids assuming that a
globally maximum clique through a vertex is its fixed anchor. Put
$\delta_v=r-c(v)$. If $v$ belongs to at least one anchor, choose a maximum
clique through $v$, and call its cluster $j_0$.

If $v\in Q_{j_0}$, then $|Q_{j_0}|=c(v)$: maximum order within its cluster gives
$|Q_{j_0}|\ge c(v)$, and containment of $v$ gives the reverse inequality. Thus
$t_{j_0}=\delta_v$, and all other anchors through $v$ contribute at most $k$
each.

If $v\notin Q_{j_0}$, at most $q_v-1$ anchors contain $v$, and their total
contribution is at most $k(q_v-1)$. In either case,

$$
\sum_{j:v\in Q_j}t_j\le \delta_v+k\max(q_v-1,0).
$$

For a vertex belonging to no anchor, the same inequality is immediate. Summing
proves (9).

The maximum anchors from different clusters have edge-disjoint edge sets, so

$$
\sum_j\binom{r-t_j}{2}\le e(G).
$$

Expanding gives the useful bound

$$
q r(r-1)
\le rN+(2r-1)T-\sum_j t_j^2
\le rN+(2r-1)T.
\tag{10}
$$


## 3. Explicit square-root-scale form

Assume $r\ge25$ and take

$$
k=\left\lfloor\frac{\sqrt r}{2}\right\rfloor.
$$

All three inequalities in (4) hold. Then

$$
|U|<2r^{3/2},\qquad
L\le2r+2k+3,\qquad
T\le r+3k,
\tag{11}
$$

and

$$
r-2\sqrt r<q\le r+3.
\tag{12}
$$


For the uncovered bound, use $D<r^2$ and $k+1>\sqrt r/2$. For the overlap bound,
(5) equals

$$
L\le 2r+\frac{2rk+2-2/r}{r-k-1}.
$$

The final fraction is at most $2k+3$, because

$$
2k^2+5k+5\le3r
$$

for $r\ge25$ and $k\le\sqrt r/2$.

Also $D\le r^2-2r+1$. Applying (9) and the overlap bound,

$$
\begin{aligned}
D+kL
&\le r^2-2r+1+2kr+2k^2+3k\\
&\le (r-k)(r+3k),
\end{aligned}
$$

where the second inequality is $5k^2+3k+1\le2r$, valid in the stated range. This
proves the bound on $T$.

The lower bound in (12) follows from $qr\ge N-|U|$. For the upper bound, (10)
gives

$$
q\le r+3+
\frac{3r+(6r-3)k}{r(r-1)}<r+4.
$$

The strict final inequality follows from $r>6k+4$, valid for $r\ge25$. Since $q$
is an integer, $q\le r+3$.

## 4. A disjoint packing of near-full cliques

Assign every vertex lying in several anchors to just one of those anchors and
delete it from the others. The total number of deletions, counted with
multiplicity, is at most $L$. Delete completely every resulting anchor that lost
more than $k$ vertices. At most $L/(k+1)$ anchors are discarded, and every
retained anchor is a clique of order at least $r-2k\ge r-\sqrt r$.

For $r\ge25$ one can use

$$
L\le2r+\sqrt r+2.
\tag{13}
$$

Indeed, the preceding exact bound for $L$ and $k\le\sqrt r/2$ show that (13)
follows from

$$
\frac{r\sqrt r+2}{r-\sqrt r/2-1}\le\sqrt r+2,
$$

which reduces to $\tfrac32r-2\sqrt r-4\ge0$.
Therefore

$$
\frac{L}{k+1}<4\sqrt r+2+\frac4{\sqrt r}
\le4\sqrt r+3.
$$

Combining this with (12), the number of retained pairwise disjoint cliques is
greater than

$$
r-6\sqrt r-3.
$$

Thus, in particular, there are at least

$$
\max\{0,\lfloor r-6\sqrt r-3\rfloor\}
$$

pairwise disjoint cliques of order at least $r-\sqrt r$. They cover all but
$O(r^{3/2})$ vertices.

## Limitation

This gives actual large cliques and exact upper capacity $r$ for every overlap
cluster, with only $O(r)$ excess incidences. It does not say that the clusters
themselves are complete, or that all vertices are covered. In particular, the
packing consists of cliques of order $r-O(\sqrt r)$, not full $K_r$'s. The
[inherited span theorem](hereditary_span_bound.md) does not presently apply to
the remaining square-root-scale independence range.

## 5. Balanced disjointification

All $q$ maximum anchors can be retained, instead of discarding some of
them. Put $\ell=\lceil\sqrt{L/2}\rceil$. There are pairwise disjoint
subcliques $Q'_j\subseteq Q_j$ with

$$
|Q'_j|\ge |Q_j|-\ell.
$$

For a family of $s$ anchors its overlap loss is at most
$\min\{L,\binom s2\}\le s\sqrt{L/2}$. The first bound uses global
excess incidences; the second uses the fact that two distinct anchors
meet in at most one point. Thus every family has enough distinct
vertices to meet the demands $|Q_j|-\ell$, and the capacitated form of
Hall's theorem applies. Negative demands, if any, are replaced by zero.
For the square-root choice of $k$, every retained block has order
$r-(3/2+o(1))\sqrt r$, and their number remains greater than
$r-2\sqrt r$. They are still not full cliques.

## 6. A sharper cluster-deficit tradeoff

Write $|C_j|=r-b_j$, so $0\le b_j\le t_j$, and put $a=r-q$.
Then

$$
\boxed{T+(k+1)(r-q)\le r-3.} \tag{14}
$$

For a covered vertex $v$, choose the cluster of a maximum clique
through $v$. Its anchor deficit is at most $\delta_v=r-c(v)$; hence

$$
\sum_{j:v\in C_j}t_j\le\delta_v+k(q_v-1).
$$

The uncovered set has order $ar+\sum_jb_j+L+1$, and every one of
its vertices has deficit at least $k+1$. Summing gives

$$
D\ge r[T+(k+1)a]+\sum_j b_j(k+1-t_j)+L+k+1.
$$

Use $D\le r^2-2r+1-2/r$ and integrality to obtain (14).
When $q\le r$, the number of full anchors is therefore at least

$$
q-T\ge k(r-q)+3.
$$

This is a dichotomy between missing clusters and full anchors, not a
proof that the near-full anchors complete.

## 7. The upper cluster count is $r+2$ for large $r$

For $r\ge625$, one can sharpen (12) to $q\le r+2$. If $q=r+3$,
the edge budget outside all anchor cliques is at most

$$
B\le\frac{3r+(6r-3)k}{2}
\le\frac32r(1+\sqrt r).
$$

Let $h_j$ count vertices of $Q_j$ shared with another anchor. The
three largest $h_j$ have sum at most $L+3$: the excess over their
contribution to $L$ consists only of vertices shared entirely within
those three anchors, and there are at most three such vertices.
Discard the two anchors of largest $h_j$. In each of the remaining
$r+1$ anchors, the vertices private to the full anchor family number
at least $r-k-(L+3)/3\ge r/4$ for $r\ge144$.

All edges between these private parts lie outside the anchor cliques.
Independent uniform representatives have expected conflict count at
most $16B/r^2\le24(1+\sqrt r)/r<1$ for $r\ge625$.
An independent transversal contradicts $\alpha(G)\le r$.

## 8. Joint deficit and degree-variance accounting

**Proved.** For $r\ge16384$, the cluster count in Section 3 satisfies

$$
\boxed{q\le r+1.} \tag{15}
$$

This improves the upper cluster count, not the unrestricted coloring
assertion. The case $q=r+1$ and the completion of clusters remain open.

Put $A_v=d(v)+c(v)+1$, $\mu=2N/r$, and

$$
V=\sum_v\frac{(A_v-\mu)^2}{A_v}.
$$

The localized independence inequality gives $\sum_v2/A_v\le r$.
Sum the exact identity

$$
\frac1A=\frac1\mu-\frac{A-\mu}{\mu^2}
 +\frac{(A-\mu)^2}{\mu^2 A}
$$

and use $N/\mu=r/2$. It follows that $V\le\sum_v A_v-N\mu$.
Since $\sum_v A_v=2e+(r+1)N-D$, the edge budget gives

$$
\boxed{D+V\le(1-2/r)N<r^2.} \tag{16}
$$


Let $h_v=\max(q_v-1,0)$ and keep
$k=\lfloor\sqrt r/2\rfloor$. Clique geometry gives, when $h_v\ge1$,

$$
A_v\ge2(r-k)+h_v(r-k-1)
\ge\mu+h_v z,\qquad z=r-3k-2>0.
$$

The function $(A-\mu)^2/A$ increases for $A\ge\mu$. Hence

$$
\frac{(A_v-\mu)^2}{A_v}
\ge\frac{h_v^2z^2}{\mu+h_vz}
\ge\frac{h_vz^2}{\mu+z}
\ge h_v(r/3-2k-2).
$$

Here $\mu+z\le3r$, and expanding $z^2/(3r)$ gives the last
inequality. Combining this with (9) and (16) yields

$$
(r-k)T+\gamma L<r^2,
\qquad \gamma=r/3-3k-2. \tag{17}
$$


Section 7 already gives $q\le r+2$, so assume $q=r+2$.
Counting anchor incidences gives $L\ge2r-T-1$, while (10) gives
$T\ge(r-3)/2$. Substitute the first in (17) to obtain

$$
(2r/3+2k+2)T
\le r^2/3+6kr+(13/3)r-3k-2.
$$

Consequently

$$
T\le r/2+(15/2)k+5.
$$

Also $\gamma\ge r/4$ for $r\ge625$. Substituting
$T\ge(r-3)/2$ into (17) gives

$$
L\le\frac32r+\frac{(5k+9/2)r-3k/2}{\gamma}
\le\frac32r+20k+18. \tag{18}
$$


Let $B$ count edges outside the union of the anchor edge sets.
Those edge sets are disjoint. The edge budget and the bound on $T$
give

$$
2B\le-r^2+3r+(2r-1)T-\sum_jt_j^2
\le15rk+(25/2)r,
\qquad B\le8r(k+1). \tag{19}
$$

Let $h_j$ count vertices of $Q_j$ that belong to another anchor.
For any two anchors $h_i+h_j\le L+1$. Indeed each shared vertex
contributes at most its cluster multiplicity minus one, except a vertex
lying in both chosen anchors and in no other cluster; there is at most
one such vertex. Drop an anchor with largest $h_j$. In each of the
remaining $r+1$ anchors, retain only vertices private to the entire
anchor family. Each retained part has order at least

$$
r-k-(L+1)/2\ge r/4-11k-10\ge r/5
$$

for $r\ge16384$. Their cross edges are all among the $B$ edges
in (19). Uniform independent representatives have expected conflict
count at most

$$
25B/r^2\le200(k+1)/r
\le100/\sqrt r+200/r<1.
$$

They therefore have an independent transversal, contrary to
$\alpha(G)\le r$. This proves (15).

The private-vertex restriction is essential here. Balanced
disjointification alone does not ensure that all cross edges lie
outside the original anchors: an edge of a third anchor may join
vertices assigned to two different retained anchors.

## 9. Two thresholds in a minimal-ratio core

**Proved refinement, with an unresolved extension step.** Here work in
the [minimal-ratio core](minimal_ratio_potential.md), not the original
$N$-vertex graph. Write

$$
|H|=ar+1,\quad h=r-a,\quad
S=\sum_v(d_H(v)-r)\le rh,\quad
D=\sum_v(r-c_H(v))\le r^2-2r+1-2/a.
$$

Choose $1\le k<K$, where $K$ satisfies the three clustering hypotheses
(4), and assume $r>2K+2$. Form clusters from all cliques of size at
least $r-K$, but retain only clusters whose largest clique has size
at least $r-k$. For their maximum anchors and cluster sizes put

$$
|Q_j|=r-t_j,\quad |C_j|=r-b_j,\quad
1\le t_j\le k,\quad0\le b_j\le t_j.
$$

Let $q$ count retained clusters, $T=\sum_jt_j$, and let $L$ be their
excess vertex incidences. Then

$$
\boxed{L\le L_0:=\frac{rh}{r-2K-2},} \tag{20}
$$


$$
\boxed{T+(k+1)(a-q)\le r-3,\qquad
a-q\le\frac{h-3}{k},} \tag{21}
$$


$$
\boxed{(r-k)T\le D+kL,\qquad q(r-k)\le ar+1+L.} \tag{22}
$$


A vertex in $m\ge2$ retained clusters has $m$ cliques through it,
each of size at least $r-K$, intersecting pairwise only at that
vertex. Thus

$$
d_H(v)-r\ge m(r-K-1)-r\ge(m-1)(r-2K-2).
$$

Summing proves (20). Every uncovered vertex has clique deficit at
least $k+1$. At a covered vertex the smallest retained anchor deficit
is at most its local clique deficit: if its maximum clique belongs
to a retained cluster this is immediate; otherwise its deficit is
at least $k+1$. The same vertexwise counting as before therefore gives

$$
D\ge r[T+(k+1)(a-q)]
 +\sum_jb_j(k+1-t_j)+L+k+1.
$$

The bound on $D$ and integrality prove the first inequality in (21).
Since $T\ge q$, the second follows. The anchor-incidence arguments
from Section 2 give (22).

Let $P_j$ be the vertices of $Q_j$ belonging to no other retained
cluster. Then these parts are disjoint and

$$
|P_j|\ge r-k-L_0.
$$

For a vertex $x\notin C_j$, the broader cluster threshold gives

$$
\boxed{d_H(x,Q_j)\le r-K-2,\qquad
|Q_j\setminus N(x)|\ge K+2-t_j.} \tag{23}
$$

Otherwise $x$ and its anchor neighbors form a clique of order at
least $r-K$ meeting $Q_j$ in at least two vertices, putting $x$
in $C_j$.

If $F$ counts edges between distinct $P_j$, then

$$
\boxed{2F\le r(T+q)+S.} \tag{24}
$$

A private-part vertex in $Q_j$ has $t_j+1+s(v)$ neighbors outside
that anchor, where $s(v)=d_H(v)-r\ge0$. Summing over the disjoint
private parts proves (24). For fixed $k,K$ these formulas imply
$T\le r+O(k)$, $q\le a+O(k)$, and $F\le r^2+O(kr)$.

There is an exact way to discard large overlap losses. If $h_j$ is
the number of nonprivate vertices in $Q_j$, then $\sum_jh_j\le2L$:
a vertex of cluster multiplicity $m\ge2$ contributes at most
$m\le2(m-1)$. Discarding the at most $2L/(\eta r)$ anchors with
$h_j>\eta r$ leaves parts of size at least $(1-\eta)r-k$.
For fixed small $\eta>0$, their normalized cross-edge weight is at
most $1+O(\eta+k/r)$. This is near the independent-transversal
union-bound threshold, not strictly below it.

### Why this does not justify suppression

The linear independent-outsider bound in
[Saturated-row suppression](saturated_row_suppression.md) requires
a nearly complete set of **order $r$**. For a mere clique $Q$ of
order $r-t$ and an independent outside set $J$ of order
$t\le s\le r+t$, the inherited cap only gives

$$
e(Q,J)\le t(r-s-1)+\binom{s+1}{2}. \tag{25}
$$

This follows by subtracting $\binom{r-t}{2}$ from
$D_r(r-t+s)=\binom r2+\binom{s-t+1}{2}$.
The term of order $tr$ cannot be discarded.

In particular, when $t\ge2$, two independent outsiders can partition
and cover $Q$ by their neighborhoods on a graph of order at most
$r$. Every hereditary cap is then vacuous, even if each outsider
misses a linear number of clique vertices. Also the missing-neighbor
margin in (23) concerns the full anchor, not its private part;
removing shared vertices can remove all those missing neighbors.

No argument here proves $q\le a$, or proves that an independent
$(a-q+1)$-set in a residual extends across the retained clusters.
The refinement separates useful counting and adjacency thresholds,
but a quantitative transversal stability or a valid completion and
extension argument remains missing.

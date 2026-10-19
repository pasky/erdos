---
name: research/erdos_644/online_avoidance_barrier
desc: A sharp 15k/8 ground-size threshold for bad seven-tuples covered by two reference edges, ruling out pure seven-response avoidance strategies below 7k/8.
tags: [proved, method-obstruction, fractional-covers]
sources: []
created: 2026-09-23T04:10:00Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/online_avoidance_barrier

***

This investigates an online selection approach, not a new lower-bound
construction for Problem 644. The basic oracle consequence of
$\tau(\mathcal H)>t$ is that every query of at most $t$ points has an avoiding
edge. Could seven adaptive queries alone force seven edges with no two-cover?
The answer is **no for every integer $t<7k/8$**. A sharp anchored-pair theorem
supplies the obstruction.

The argument does not restrict strategies using global structural information,
selecting a seven-edge subfamily after more than seven queries, or imposing
additional requirements on the replies. Neither original assertion is resolved.

## A seven-coordinate fractional certificate

**Lemma.** Let $\mathcal F$ be an intersecting family of nonempty subsets of
$\{p,q,a,b,c,d,e\}$, no member of which contains both $p,q$. Then

$$
\tau^*(\mathcal F)=\nu^*(\mathcal F)\le\frac{15}{7}.
\tag{1}
$$

Only the fractional-cover upper bound is needed below.

If a member has size at most two, it itself is a transversal and gives a cover
of weight at most two. Otherwise every member has size at least three. Put
$X=\{a,b,c,d,e\}$, and define graphs on $X$ by

$$
uv\in G_p\iff\{p,u,v\}\in\mathcal F,
\qquad uv\in G_q\iff\{q,u,v\}\in\mathcal F.
$$

Every edge of $G_p$ intersects every edge of $G_q$.

Three elementary cases have covers of weight two. If $G_p$ is empty, give weight
$1/3$ to each coordinate except $p$: a member containing $p$ has size at least
four, and every other member has size at least three. The case $G_q=\varnothing$
is symmetric. If $uv$ belongs to both graphs, $\{u,v\}$ is a transversal: a
member missing both would have to contain both $p,q$ to meet the two
corresponding triples. Finally, if some vertex of $X$ is isolated in
$G_p\cup G_q$, give weight $1/2$ to the other four vertices of $X$. Every
special triple uses two of them, every triple inside $X$ uses at least two, and
every allowed larger set also uses at least two.

We may therefore assume that the graphs are nonempty, edge-disjoint, and their
union spans all five vertices of $X$. After swapping $p,q$, suppose
$|G_p|\le|G_q|$. We claim $|G_p|\le2$.

Otherwise both graphs have at least three edges. If $G_p$ contains disjoint
edges $ab,cd$, all $G_q$-edges lie in the $K_{2,2}$ between these pairs. Any
three distinct edges of that $K_{2,2}$ have empty common intersection.
Consequently no $G_p$-edge can use the fifth vertex $e$, since its other
endpoint would have to meet every $G_q$-edge. This contradicts spanning. Thus
$G_p$ is a pairwise-intersecting graph, hence a star or a triangle. A triangle
forces every $G_q$-edge to be an edge of the same triangle, contradicting
edge-disjointness. A star with at least three edges forces all $G_q$-edges to
contain its center. Two disjoint edge sets of size at least three cannot fit in
a four-edge star. This proves the claim.

There are now two cases, with explicit vertex weights:

$$
\begin{array}{c|c|c}
G_p&\text{restriction on }G_q&7(w_p,w_q,w_a,w_b,w_c,w_d,w_e)\\ \hline
\{ab\}&\text{every edge meets }ab&(1,2,3,3,2,2,2)\\
\{ab,ac\}&G_q\subseteq\{ad,ae,bc\}&(0,1,4,3,3,2,2).
\end{array}
$$

In the second case the two $G_p$-edges must intersect: disjoint ones would
confine both graphs to four vertices. Cross-intersection and edge-disjointness
then give exactly the indicated restriction.

Both weight vectors have total $15/7$. In the first case all special triples
have weight at least one. The only triple inside $X$ of weight below one is
$cde$, which is absent because it misses $pab$. Every allowed set of size at
least four has weight at least one. In the second case the listed special
triples have weight one, every triple inside $X$ has weight at least
$(3+2+2)/7=1$, and every allowed four-set has weight at least one: it contains
at most one of $p,q$ and at least three central vertices. Larger sets inherit
the bound. This proves (1).

## The sharp anchored-pair threshold

**Theorem.** Suppose $E_1,\ldots,E_7\subseteq U$ all have size $k$, have no
transversal of size at most two, and satisfy $E_1\cup E_2=U$. Then

$$
\boxed{|U|\ge\frac{15k}{8}.}
\tag{2}
$$


For every $v\in U$, let $S_v=\{i:v\notin E_i\}$. These spectra are nonempty and
pairwise intersecting; otherwise one or two points would cover the rows. The
union condition excludes spectra containing both $1,2$. Apply (1), with these
two coordinates playing $p,q$, to obtain weights $w_i$ of total at most $15/7$
satisfying $\sum_{i\in S_v}w_i\ge1$ for every $v$. Uniform counting on $U$ gives
every coordinate absence load

$$
\lambda=\frac{|U|-k}{|U|}.
$$

Hence

$$
1\le\mathbb E_v\sum_{i\in S_v}w_i
=\lambda\sum_iw_i\le\frac{15}{7}\lambda,
$$

which rearranges to (2). Repeated rows cause no difficulty.

The constant is attained. Take fifteen points with the following complement
spectra and multiplicities:

$$
1345:4,\quad236:3,\quad456:1,\quad247:2,\quad257:2,\quad167:3.
\tag{3}
$$

The six spectra intersect pairwise, none contains $1,2$, and each coordinate
occurs seven times. Their complementary rows are therefore seven distinct
$8$-sets with no two-cover and $E_1\cup E_2=U$. Replacing every point by the
same positive number of copies gives equality for every $8\mid k$. This also
certifies sharpness of (1): weights $1/7$ per occurrence in (3) form a
fractional matching of total $15/7$.

## An adversary against seven avoidance queries

Fix integers $k\ge1$ and $0\le t<7k/8$. In each round a procedure queries a set
$T_i$ of at most $t$ points and receives a $k$-set $E_i$ disjoint from it.
Queries may depend arbitrarily on preceding replies; the ground universe is
unrestricted.

Answer the first query by any disjoint $k$-set $E_1$. After the second query
choose

$$
C\subseteq E_1\setminus T_2,\quad |C|=k-t,
\qquad |D|=t,
$$

where $D$ is fresh and disjoint from $E_1\cup T_2$, and answer $E_2=C\cup D$.
Put $U=E_1\cup E_2$, so $|U|=k+t$. Every later query leaves at least $k$ points
in $U$, so answer with any $k$-subset of $U\setminus T_i$.

The seven replies satisfy the union condition in (2), but

$$
|U|=k+t<15k/8.
$$

They consequently have a two-cover. Shorter lists inherit this conclusion by
completing them to seven replies. All replies are consistent with the single
complete $k$-uniform family on $U$, whose transversal number is $t+1$.

That complete family need not have $P_7$: the obstruction concerns what follows
from the avoiding-edge oracle and its seven replies **alone**. It shows that a
proof below the $7/8$ coefficient must use more than this pure seven-response
strategy. The existing $7/8$ upper proof uses global intersection choices, and
is not contradicted. Neither an unrestricted lower bound nor an optimal online
strategy at the endpoint is asserted.

## Why ordinary decision-tree rank did not help

For a family of subsets, the Littlestone dimension is the maximum depth of a
complete binary tree of point queries such that every root-to-leaf membership
sequence is realized by a member. Rank $k$ bounds this dimension by $k$, by the
all-positive branch. But $P_7$ cannot improve that bound: the nonroot vertex
sets of root-to-leaf paths in a full binary tree of depth $k$ have Littlestone
dimension $k$, while its two root children form a transversal. Querying the left
child at each current node realizes every binary path.

Nor does a positive branch preserve locality. For $m\ge2$, all $4m$-sets on
$7m-1$ points have $P_7$ and transversal number $3m$. Conditioning on
containment of a fixed four-set and contracting those four points leaves all
$4(m-1)$-sets on $7m-5$ points. This contains a Fano-cap blowup on $7(m-1)$
points and fails $P_7$. Thus a standard rank-decreasing positive-branch
induction cannot reuse the local hypothesis. These examples do not exclude a
different tree invariant incorporating residual transversal number and
controlled contractions.

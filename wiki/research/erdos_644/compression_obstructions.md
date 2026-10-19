---
name: research/erdos_644/compression_obstructions
desc: Ordinary shifting can destroy the local property at every uniformity or lose linearly in transversal number; a seven-anchor obstruction is explicit.
tags: [proved, limitations, compression]
sources: []
created: 2026-09-22T21:37:17Z
updated: 2026-10-13T05:28:09Z
---


# research/erdos_644/compression_obstructions

***

Neither assertion of Problem 644 is resolved here. These examples rule out
several unqualified shifting arguments, not every possible symmetrization or a
carefully selected sequence with small loss.

Write $P_r$ for the condition that every at-most-$r$ edges have a transversal of
size at most two. For distinct points $i,j$, the ordinary shift $S_{ij}$
replaces an edge $E$ containing $j$ but not $i$ by

$$
E-j+i
$$

if that replacement is not already in the family; otherwise it retains $E$. The
examples use notation such as $1247$ for $\{1,2,4,7\}$.

## A shift can destroy the local property while preserving the transversal number

Consider the $3$-uniform family on $[6]$

$$
\mathcal H=\{123,124,125,134,235,346,356,456\}.
$$

For the edges in this order, the following pairs miss the designated edge and
meet all the other edges:

$$
45,\quad35,\quad34,\quad26,\quad16,\quad15,\quad24,\quad13.
$$

Every subfamily with at most seven edges omits some designated edge and
therefore has a two-point transversal. Thus $\mathcal H$ has $P_7$.

The shift $S_{4,5}$ changes only $235$ to $234$. Its image contains the seven
edges

$$
123,124,125,134,234,356,456.
\tag{1}
$$

Their complements in $[6]$ are

$$
456,356,346,256,156,124,123.
$$

Every pair of $[6]$ is contained in at least one of these complements, so no
pair covers (1). Hence the shifted family fails $P_7$.

For completeness, the original family also has no two-point transversal. Its
eight complementary triples are

$$
456,356,346,256,146,125,124,123,
$$

which again contain every pair of $[6]$. The triple $134$ covers both the
original family and its shifted image. Both transversal numbers are therefore
three.

If $\sigma$ exchanges $4$ and $5$, then
$S_{4,5}\mathcal H\subseteq\mathcal H\cup\sigma\mathcal H$. Consequently even
completing a family under a single transposition can destroy $P_7$.

### The same failure at every uniformity

Section 6 of
[third independent record](independent/complete_family_limit_and_seven_edge_obstruction.md)
gives a relabeling of the preceding example and a valid padding extension. For
every $k\ge3$, append $k-3$ fresh points to each edge of $\mathcal H$, sharing
the padding exactly within the pairs

$$
(346,356),\qquad(124,125),
$$

and using disjoint padding otherwise. The original deletion covers
still prove $P_7$.

Under $S_{4,5}$, the shared padding retains the two mirror collisions
$356\mapsto346$ and $125\mapsto124$. Thus only the padded edge $235$
changes, to padded $234$. The seven padded edges corresponding to (1)
still have no two-cover: two original points fail by the preceding
certificate, while every original point meets at most four of these
seven edges and every padding point meets at most two.

Both entire eight-edge families have transversal number three. The
original triple $134$ covers both. Two original points fail to cover
either entire family; any padding point together with an original
point meets at most $2+5<8$ edges, and two padding points meet at most
four. Consequently a single ordinary shift can destroy $P_7$ at every
uniformity $k\ge3$, while retaining $\tau=3$. This strengthens the
finite-rank scope of the obstruction, not its asymptotic ratio.

## Seven star-forcing anchors can be necessary

Call a subfamily *star-forcing at $j$* if every transversal of size at most two
contains $j$. In applications below the subfamily has a two-point transversal;
the assertion is not based on absence of all two-point transversals.

**Short-anchor bound.** Suppose a rank-at-most-$k$ family $\mathcal H$ has $P_7$
and contains $q\le6$ star-forcing reference edges at $j$, at least one of which
avoids $j$. Put

$$
X=\bigcap_{\substack{A\text{ a reference edge}\\j\notin A}}A.
$$

The reference edges have precisely the two-point covers $\{j,x\}$ with $x\in X$,
and $|X|\le k$. Then

$$
\tau(\mathcal H)\le1+\left\lceil\frac{|X|}{7-q}\right\rceil.
$$

To prove this, partition $X$ into $7-q$ parts of size at most
$\lceil|X|/(7-q)\rceil$. If the bound failed, for each part choose an edge
avoiding that part together with $j$. Adjoin these edges to the references. Any
two-cover must contain $j$ and some $x\in X$, but the edge queried for the part
containing $x$ avoids both points. This contradicts $P_7$. Repeated query edges
can simply be removed, since the total number of distinct edges is at most
seven. In particular, $q\le5$ gives $\tau(\mathcal H)\le1+\lceil k/2\rceil$.

The following $4$-uniform example strengthens the obstruction to extracting a
short star-forcing subfamily:

$$
\mathcal F=\{1247,1256,1346,1357,1456,2345,2367,2567,3467\}
\quad\text{on }[7].
\tag{2}
$$

For its edges in this order, deletion leaves the two-point covers

$$
35,\quad47,\quad57,\quad24,\quad23,\quad16,\quad45,\quad13,\quad12.
\tag{3}
$$

Thus every proper subfamily has a two-point transversal, proving $P_8$ and hence
$P_7$. The complements of the nine edges are

$$
356,347,257,246,237,167,145,134,125.
$$

They contain every pair of $[7]$, so $\tau(\mathcal F)\ge3$. Adjoining one point
of a deleted edge to its cover in (3) gives a three-point transversal. Thus
$\tau(\mathcal F)=3$, and deletion of every edge reduces the transversal number
to two.

The shift $S_{3,5}$ changes only $1256$ to $1236$: the potential replacements of
$1456$ and $2567$ are already $1346$ and $2367$. Its image contains the bad
seven-tuple

$$
3467,1236,1247,1357,1456,2345,2567.
\tag{4}
$$

The complementary triples are

$$
125,457,356,246,237,167,134.
\tag{5}
$$

Each pair of $[7]$ appears in exactly one triple of (5). These are the lines of
a Fano plane, and (4) consists of its complementary caps. In particular, (4) has
no two-point transversal.

Undo the changed row, obtaining

$$
\mathcal G=\{3467,1256,1247,1357,1456,2345,2567\}\subseteq\mathcal F.
$$

Any two-cover of $\mathcal G$ avoiding $5$ would still cover (4): if such a pair
meets $1256$, it meets it at $1$, $2$, or $6$, all of which remain in $1236$.
Hence $\mathcal G$ is star-forcing at $5$. It does have the two-cover $\{4,5\}$.

Moreover, no subfamily of $\mathcal F$ with six or fewer edges is star-forcing
at $5$. For the seven displayed rows of $\mathcal G$, respectively, the pairs

$$
12,\quad47,\quad36,\quad24,\quad23,\quad16,\quad13
\tag{6}
$$

avoid $5$, miss the designated row, and meet every other row of $\mathcal F$.
Any star-forcing subfamily must therefore contain all seven designated rows.
This is an exact obstruction to replacing an unsafe-shift witness by at most six
star-forcing anchors, even though the original family has $P_8$.

## Linear cumulative loss along shifts that all preserve $P_7$

The following construction starts with a uniform family that is both
transversal-critical and domination-reduced. Here a vertex $x$ is dominated by a
different vertex $y$ if every edge containing $x$ also contains $y$.

Fix an integer $q\ge1$ and put

$$
a=4q,\qquad n=7q-1,\qquad t=n-a+1=3q.
$$

Let $V=\mathbb Z/n\mathbb Z$ and partition the complete family $\binom Va$ into
its orbits under cyclic rotation. For each orbit $O$, introduce a distinct
padding vertex $p_O$. Set

$$
\mathcal K=\{E\cup\{p_O\}:O\text{ is an orbit and }E\in O\}.
\tag{7}
$$

Every core edge $E\in\binom Va$ occurs exactly once in (7). The family is
$K$-uniform with $K=a+1$.

### The local property

The complete core has $P_7$. Indeed, seven $a$-subsets have total degree
$7a>4n$, so some core point lies in at least five of them. The at most two
remaining sets intersect because $n<2a$. These one or two core points cover all
seven sets. There are more than seven core edges, so the at-most-seven version
follows as well.

Every corresponding padded family, including each intermediate family below, is
covered by the same core points. Thus (7) has $P_7$.

### The transversal number

Any $t$ core points cover all core $a$-sets, giving $\tau(\mathcal K)\le t$.
Suppose conversely that a cover uses $r$ core points and $s$ padding points,
with

$$
r+s\le t-1.
$$

At least

$$
\binom{n-r}{a}\ge\binom{a+s}{a}
\tag{8}
$$

core edges avoid the selected core points. Every orbit has at most $n$ edges.

If $s=0$, (8) already contradicts coverage. If $s\ge2$, note that
$\binom{a+s}{a}/s$ is increasing for integral $s\ge1$, since the ratio of its
successive values is

$$
\frac{s(a+s+1)}{(s+1)^2}>1\qquad(a\ge4).
$$

Consequently

$$
\frac1s\binom{a+s}{a}\ge\frac{(a+1)(a+2)}4
>\frac{7a}4-1=n.
$$

The selected padding vertices cover at most $ns$ core edges, fewer than the
number in (8), again a contradiction.

It remains to exclude $s=1$. Choose an $(a+1)$-subset $R$ of the core points
outside the selected $r$ points. Its $a+1$ subsets of size $a$ must all belong
to the one selected orbit $O$. Write $M=|O|\le n$. Rotation invariance makes
every core point have degree $Ma/n$ within $O$. Every point of $R$ lies in $a$
of those $a+1$ edges, so $Ma/n\ge a$, forcing $M=n$ and degree exactly $a$ at
every core point. The incidences of each point of $R$ are already exhausted by
the $a+1$ edges inside $R$. The remaining $n-a-1>0$ edges of $O$ must therefore
lie wholly in $V\setminus R$. But

$$
|V\setminus R|=n-a-1<a,
$$

which is impossible for an $a$-edge. Thus no cover of size at most $t-1$ exists,
and

$$
\tau(\mathcal K)=t=3q.
\tag{9}
$$


### Criticality and absence of dominated vertices

For an edge based on $E$, the core complement $V\setminus E$ has size $t-1$,
misses that edge, and meets every other edge because distinct core edges have
the same size $a$. Deleting any edge therefore reduces the transversal number to
at most $t-1$. It cannot reduce it further, since one point from the deleted
edge could then be added to give a cover of $\mathcal K$ smaller than $t$. Thus
$\mathcal K$ is transversal-critical.

Each cyclic orbit has empty common core intersection. Its intersection is
rotation-invariant, hence is either empty or all of $V$, and the latter is
impossible because $a<n$. Thus no padding vertex is dominated by a core vertex.
Different padding vertices have disjoint nonempty incidence sets, so do not
dominate each other.

No core vertex is dominated by another core vertex, since the complete core
separates them. A core vertex belongs to

$$
\binom{n-1}{a-1}\ge\binom{n-1}{2}>n
$$

edges; here $n\ge6$ and $2\le a-1\le n-3$. A padding vertex belongs to at most
$n$ edges. Hence no core vertex is dominated by a padding vertex. This proves
that the entire uniform family (7) is domination-reduced.

### The shifts

Choose one padding vertex $p$ and successively apply ordinary shifts replacing
every other padding label $p_O$ by $p$. These can be ordinary left-shifts in a
fixed order with $p$ first. When an edge based on $E$ still has label $p_O$, the
edge $E\cup\{p\}$ is absent: every core edge has exactly one padding label
throughout. Therefore the shift replaces every edge with label $p_O$, with no
mirror collision.

At every stage, the same complete core certifies $P_7$. At the end the family is

$$
\{E\cup\{p\}:E\in\tbinom Va\},
$$

which has transversal number one. The cumulative loss is

$$
3q-1=\frac34K-\frac74.
$$

Thus even a sequence consisting entirely of $P_7$-preserving shifts can lose a
positive linear fraction of the rank.

This construction does not show that every shifting order suffers linear loss.
Also, although its initial family has no dominated vertices, deleting all
padding vertices preserves $P_7$ and $\tau$, and reduces the rank by one. It
does not obstruct a more substantial preliminary reduction that removes such
dispensable incidences.

## What full shifting would require

Suppose a $k$-uniform family on an ordered ground set is fully shifted and has
transversal number $t$. The initial segment $[t-1]$ fails to cover it, so there
is an edge disjoint from $[t-1]$. Shiftedness then gives
$\{t,t+1,\ldots,t+k-1\}$, and subsequently every $k$-subset of $[t+k-1]$.
Therefore

$$
\binom{[t+k-1]}k\subseteq\mathcal H,
\qquad
|\mathcal H|\ge\binom{t+k-1}{k}.
$$

Together with the [complete-family bound](complete_families.md), this would give
the desired $3k/4$-scale conclusion for fully shifted $P_7$ families.

Ordinary shifts preserve the number of edges. The first example has eight edges,
fewer than $\binom53=10$; the second has nine, fewer than $\binom64=15$. Neither
can become fully shifted through any ordinary shifting sequence while retaining
its transversal number three. These finite examples do not disprove a theorem
restricted to hypothetical families above $3k/4+o(k)$, nor do they exclude
adding edges by a more selective operation that retains $P_7$.

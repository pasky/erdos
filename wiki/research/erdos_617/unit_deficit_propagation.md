---
name: research/erdos_617/unit_deficit_propagation
desc: Private-set expansion, rigid near-extremal unit blocks, a matching unit support graph, and the bound nine a at most seven r minus five.
tags: [graph-theory, proved, private-cliques, reductions]
sources: []
created: 2026-09-22T05:15:00Z
updated: 2026-10-14T00:26:52Z
---


# research/erdos_617/unit_deficit_propagation

***

**Proved partial results; no uniform exclusion of the core.** Let
$r\ge12$ and use the minimum-anchor normalized two-supported core from
[Two-support normalization](two_support_normalization.md). Thus

$$
|H|=ar+1,\quad \alpha(H)=a,\quad \omega(H)\le r-1,
\quad |P_i|=r-d_i,\quad d_i\ge1,
$$


$$
b=|B|=1+\sum_i d_i\le r.
$$

The $a$ anchors are independent. Every private vertex has exactly its
own anchor as an anchor neighbor, and every exception has exactly two.
Every private vertex has degree at least $r$. The support multigraph
therefore has degree at least $d_i+1$ at anchor $i$.

These results do not impose a least-color edge budget on $H$.

## 1. Expansion for all-private independent sets

For every nonempty independent set $I\subseteq\bigcup_iP_i$,

$$
\boxed{|N_H[I]|\ge r|I|+1.} \tag{1}
$$


Write $t=|I|$ and let $A$ be its $t$ touched rows. The set $I$ together
with the untouched anchors is an independent $a$-set. Thus an exception
whose two support anchors lie in $A$ cannot survive outside $N[I]$:
it would augment that independent set. Also $N[I]$ contains every
touched row and contains no untouched anchor.

Suppose $t<a$ and $|N[I]|\le rt$. The residual has at least
$(a-t)r+1$ vertices, independence at most $a-t$, and every vertex has
one or two retained anchor neighbors. Trim it to $(a-t)r+1$ vertices,
keeping all retained anchors. Its singleton-support classes are
cliques, by the usual independent-set augmentation. Its two-supported
exceptions form a subset of $B$, so their number is still at most $r$.
This contradicts minimum-anchor normalization. If $t=a$, maximality
of $I$ gives $N[I]=V(H)$ directly. This proves (1).

Let $L$ consist of private vertices of degree exactly $r$. For any
nonempty $W\subseteq L$ and independent $I\subseteq W$, (1) implies

$$
\sum_{v\in I}d_{H[W]}(v)\le |W|-1.
$$

Indeed the repeated neighborhood-incidence count for $I$ in $H$ is
at most $|I|-1$, and restricting to $W$ cannot increase it.
The checked maximum-independent-cover characterization in
[Minimal-core structure, Section 2](minimal_core_structure.md) now
shows that **$H[L]$ is a Gallai forest**. This applies only to the
degree-$r$ private vertices, not to degree-$r$ exceptions.

### Extension to independent sets with tight anchor support

The expansion argument also applies to any nonempty independent $I$
whose union of original anchor supports has size $|I|$. Here an anchor
has its own singleton support. If that union is $S$, then
$I\cup(Q\setminus S)$ is a maximum independent set. Every surviving
vertex outside $N[I]$ must therefore retain an anchor neighbor outside
$S$; otherwise it augments that maximum set. All anchors of $S$ lie in
$N[I]$, and all others survive. If $|N[I]|\le r|I|$, trimming the
residual while retaining its $a-|I|$ anchors gives a smaller
one/two-supported core, a contradiction. Thus

$$
|N[I]|\ge r|I|+1. \tag{1a}
$$

For $|I|=a$ this follows directly from maximality.

In particular, take an exception $x$ supported on $\{i,j\}$ and a
private nonneighbor $v\in P_i$. Their support union has size two, so

$$
d(x)+d(v)-|N(x)\cap N(v)|\ge2r-1.
$$

They share the neighbor $q_i$. Hence if $d(v)=r$, then $d(x)\ge r$.
Every private nonneighbor, in either supporting row, of an exception
of degree below $r$ must consequently have degree at least $r+1$.
This does not establish minimum degree $r$ at all exceptions.

## 2. Active unit-deficit rows

Put $q=r-1$. A unit-deficit row $P_i$, of order $q$, is called active
if an incident exception $x_i$ misses at most two vertices of $P_i$.
Write $h_i=|P_i\setminus N(x_i)|\le2$.

For any $z\notin P_i\cup\{x_i\}$, the $(r+1)$-set
$P_i\cup\{x_i,z\}$ must have at least $r-1=q$ nonedges. Hence

$$
d_H(z,P_i)+\mathbf1_{\{zx_i\in E(H)\}}
\le h_i+1\le3. \tag{2}
$$

In particular $x_i$ is the unique incident exception missing at most
two row vertices, since every other incident exception misses at least
$q-h_i-1\ge r-4>2$.

**Propagation.** Every other incident exception $y$ is complete to its
other supporting row, say $P_j$. If $z\in P_j$ were nonadjacent to
$y$, two-support augmentation would make $z$ adjacent to all of
$P_i\setminus N(y)$, a set of order at least $q-h_i-1$. This
contradicts (2), since $q-h_i-1>h_i+1$ for $r\ge8$.
Moreover $d_j\ge2$: otherwise $P_j\cup\{y\}$ would be a $K_r$.

Thus all support edges from an active unit row except its designated
edge $x_i$ go to higher-deficit rows and give complete adjacency there.

## 3. Clique-safe propagated groups

For each higher-deficit row $j$, let $C_j$ be the exceptions propagated
to $j$ from active unit rows. Then

$$
\boxed{P_j\cup C_j\text{ is a clique},\qquad |C_j|\le d_j-1.} \tag{3}
$$


Completeness to $P_j$ is already proved. Suppose two such exceptions
$y,z$ are nonadjacent. If they come from the same active row $i$, (2)
leaves at least $q-6=r-7>0$ common nonneighbors there. One of these,
together with $y,z$ and the anchors outside $\{i,j\}$, is an
independent $(a+1)$-set.

If their active rows are distinct $i,k$, both common-nonneighbor lists
in $P_i,P_k$ have at least $r-7$ vertices. Two-support augmentation
using $y,z$ and the anchors outside $\{i,j,k\}$ forces these lists
to be completely joined. But each private vertex of $P_i$ has at
most three neighbors in $P_k$, by (2). Since $r-7>3$ for $r\ge11$,
this is impossible. Thus $C_j$ is a clique, and $K_r$-freeness gives
the capacity in (3).

An exception in these groups has exactly one unit support endpoint,
so it is counted in exactly one group and from exactly one active row.

## 4. The unit support graph

Every unit--unit support edge has an active endpoint. Indeed its two
missing counts satisfy

$$
(m_i-1)(m_k-1)\le1,
$$

so they cannot both be at least three. Each active unit vertex has
at most one unit support edge, by propagation. Consequently the unit
support graph is a union of stars with inactive centers and active
leaves, isolated active--active edges, and isolated vertices.
Parallel unit edges are also impossible; equivalently use the strict
pair capacity $|B_{ik}|\le d_i+d_k-1=1$.

In particular no simple unit-deficit support path has three edges.
This does not justify deleting a unit row together
with its designated exception.

## 5. A fixed linear gap in the anchor parameter

Put

$$
E=\sum_i(d_i-1)=b-a-1,
\quad U=\#\{i:d_i=1\},\quad h=a-U,
$$

and let $A$ denote the number of active unit rows. By (3),

$$
C:=\sum_{i\text{ active}}(\deg_{\rm supp}(i)-1)
=\sum_{j:d_j\ge2}|C_j|\le E.
$$

Since every active support degree is at least two, $A\le C\le E$;
also $h\le E$. Let $e_U$ count unit--unit support edges. Section 4
gives $e_U\le A$. Every unit support degree is at least two, whence

$$
b\ge2U-e_U\ge2U-A.
$$

Using $b=a+E+1$ and $U=a-h$ yields

$$
a\le E+2h+A+1\le4E+1.
$$

Finally $E\le r-a-1$, so

$$
\boxed{5a\le4r-3.} \tag{4}
$$

The stronger intermediate form $a\le E+2h+A+1$ is useful when
the higher deficits are concentrated. If $t$ is the number of
active--active unit edges and $e_H$ the number of high--high support
edges, the same counting retains
$a\le E+2h+A-t-e_H+1$.

The propagation, clique argument, expansion, and bound (4) were checked by the
author and are author-recorded. No $7/9$ bound follows by keeping the minimum
support degree at inactive units after deleting active--inactive edges, since
that deletion can lower it. The direct count above does not make that deletion.

## 6. Near-extremal blocks at an inactive or active unit row

The following results use $r\ge12$ and the normalized core, but do
not require the unit row to be active. Put $q=r-1$.

### An exception missing one vertex in its other row

Suppose $x$ has support $\{i,j\}$, $|P_i|=q$, and
$P_j\setminus N(x)=\{z\}$. Write

$$
A=P_i\setminus N(x),\quad m=|A|,\quad t=d(z,P_i).
$$

The two-support augmentation forces $A\subseteq N(z)$, so
$t\ge m$. The set $Z=P_i\cup\{x,z\}$ has exactly
$m+(q-t)+1$ nonedges. Its hereditary cap therefore gives
$t\le m+1$. Consequently

$$
\lambda=m+1-t\in\{0,1\},\qquad
e(H[Z])=D_r(r+1)-\lambda. \tag{5}
$$

Since $D_r(r+2)-D_r(r+1)=2$, every $v\notin Z$ satisfies

$$
\boxed{d(v,Z)\le2+\lambda\le3.} \tag{6}
$$


Let $y\ne x$ be any other exception supported on $\{i,k\}$.
It has at least $q-3=r-4$ nonneighbors in $P_i$. If it misses
$w\in P_k$, the two-support augmentation makes $w$ adjacent to
all those nonneighbors. Unless $w=z$, this contradicts (6),
because $r-4>3$. Thus $y$ is complete to $P_k$ when $k\ne j$,
and misses at most $z$ when $k=j$. In particular, all exceptions
on a fixed pair incident to a unit row that miss exactly one
vertex in the other row have the **same** missing vertex.

This also controls all edges between the two private rows.
Put $Y=P_j\setminus\{z\}$ and $c=e(P_i,Y)$. The set
$S=P_i\cup P_j\cup\{x\}$ has $2r-d_j$ vertices and precisely

$$
(r-1)|P_j|+\lambda-c
$$

nonedges. Its hereditary cap requires at least $(r-1)|P_j|$,
so

$$
\boxed{e(P_i,P_j\setminus\{z\})\le\lambda.} \tag{7}
$$

When $\lambda=0$, both $Z$ and $S$ attain their hereditary caps.

In an actual coloring, this last equality determines every other
color on $S$. Write $p=|P_j|=r-d_j$. Each other color has at
least $p$ edges on $S$, and all $(r-1)p$ non-target edges are
accounted for. Each of these color graphs has independence at
most $r$ and $2r-d_j$ vertices. A graph with $p$ edges has an
independent set of size at least $(2r-d_j)-p=r$; equality here
forces its edges to be a matching. Indeed two incident edges
could be covered by one vertex, and the remaining edges by at
most one vertex each, leaving an independent $(r+1)$-set.
Thus every other color induces

$$
pK_2\ \sqcup\ d_jK_1 \quad\text{on }S. \tag{8}
$$

For an outsider $v$ and any such color, $v$ must meet one of
these isolated vertices or both ends of one matching edge in
that color. Otherwise one can choose a nonneighbor from every
matching edge together with all isolated vertices and $v$,
obtaining an independent $(r+1)$-set.

### A nonadjacent parallel pair

Suppose $x,y\in B_{ij}$ are nonadjacent and $P_i$ is a unit row.
Their nonneighbor sets $A_x,A_y$ in $P_i$ are disjoint: a common
nonneighbor, together with $x,y$ and the unused anchors, would
augment the anchor set. They both omit $q_i$, so
$|A_x|+|A_y|\le q-1$. The cap on $Z=P_i\cup\{x,y\}$ gives
the reverse inequality, since its nonedges number
$|A_x|+|A_y|+1$. Hence

$$
A_x\sqcup A_y=P_i\setminus\{q_i\},\quad
e(H[Z])=D_r(r+1),\quad d(v,Z)\le2\ (v\notin Z). \tag{9}
$$

Both sets $A_x,A_y$ are nonempty, since otherwise there would
be a $K_r$.

There is no third exception $w\in B_{ij}$. The bound
$\alpha(H[B_{ij}])\le2$ forces $w$ to see $x$ or $y$.
It already sees $q_i$, so (9) permits exactly one of $x,y$ and
no other vertex of $P_i$. Its nonneighbor set in $P_i$ then
meets the nonempty nonneighbor set of the other exception,
again giving an augmenting independent triple. Consequently

$$
\boxed{B_{ij}\text{ is a clique or consists of two
nonadjacent vertices whenever }d_i=1.} \tag{10}
$$


Every other exception $w$ supported on $\{i,k\}$ is complete
to $P_k$. It misses at least $q-2$ private vertices in $P_i$;
any missed vertex of $P_k$ would lie outside $Z$ and be adjacent
to all of them, contrary to (9). If the unit row is inactive,
$x$ and $y$ themselves each miss at least three vertices in
$P_i$, so the same argument makes them complete to $P_j$.
In that case $P_j$ is anticomplete to $P_i$: each of its vertices
already has its two allowed neighbors $x,y$ in $Z$.

These block and routing statements do not imply safe deletion of
$r$ vertices. An independent set outside a proposed deleted row
can still contain its exceptional hole. No unconditional
independence drop, or iteration eliminating all unit rows, has
been proved.

## 7. Independent support sets and exact wedge accounting

For an independent exception set $J\subseteq B$, let $S$ be its
supporting anchors and put

$$
C_J=\bigcup_{i\in S}(P_i\setminus N(J)).
$$

Adjoining the unused anchors to $J$ and an independent subset of
$C_J$ proves

$$
\alpha(H[C_J])\le |S|-|J|. \tag{11}
$$

In particular, if the support edges of $J$ form a tree, $C_J$ is
a clique of order at most $r-1$; if $|S|=|J|$, it is empty.

For each row, let $B_i$ be its incident exceptions,
$s_i=|B_i|$, and $W_i$ the number of nonedges of $H[B_i]$.
For $x$ supported on $i,j$, set

$$
m_i(x)=|P_i\setminus N(x)|,\qquad
\delta_x=r-1-m_i(x)-m_j(x)\ge0.
$$

Nonnegativity holds because the two nonneighbor cliques are
completely joined and $H$ is $K_r$-free. Since $s_i\ge d_i+1$
and $r+1\le |P_i\cup B_i|\le2r$, its hereditary cap gives

$$
\lambda_i=\sum_{x\in B_i}m_i(x)+W_i
-(r-1)(s_i-d_i)\ge0.
$$

Sum this expression, using $\sum_i s_i=2b$ and
$\sum_i d_i=b-1$, to obtain the exact identity

$$
\boxed{\sum_i W_i=r-1+\sum_{x\in B}\delta_x+\sum_i\lambda_i.}
\tag{12}
$$

Thus there are at least $r-1$ nonadjacent incident exception
pairs, counting a parallel pair twice. Turning these pairs into
an independent support set with more edges than vertices, or
using (11) to force a contradiction, remains unproved.

Zero slack in an individual exception is rigid. If $\delta_x=0$
for support $ij$, put $u=m_i-d_j$, $v=m_j-d_i$. The row-size
bounds and $m_i+m_j=r-1$ give $u,v\ge0$ and
$u+v=r-1-d_i-d_j\ge a-2\ge2$. The two-support inequality is

$$
u(d_i-1)+v(d_j-1)+uv\le1.
$$

Thus the two deficits cannot both be at least two. If
$d_i=1<d_j$, it forces $v=0$; if both deficits are one,
$uv\le1$ and $u+v=r-3\ge9$ force one of $u,v$ to vanish.
After exchanging endpoints, in every case

$$
d_i=1,\qquad m_i=r-2,\qquad m_j=1.
$$

The exception sees only $q_i$ in $P_i$, and its unique missed
vertex in $P_j$ is complete to $P_i\setminus\{q_i\}$.
Every high--high support edge therefore has $\delta_x\ge1$.

## 8. The unit support graph is a matching

The one-hole lemma strengthens Section 4: its inactive-centered
stars with more than one edge are impossible. For a unit--unit
exception $x$ on $i,j$, both missing counts are positive, and

$$
(m_i-1)(m_j-1)\le1.
$$

If both counts are at most two, both endpoints are active, so
Section 2 already excludes another unit edge at either endpoint.
Otherwise, say $m_i\ge3$, one has $m_j=1$. The one-hole block
lemma routes every other exception at $i$ completely to its other
row. That row cannot be a unit row, since adjoining the exception
would create a $K_r$. The active endpoint $j$ also has no other
unit edge. Parallel unit edges were already excluded. Thus the
unit support graph is a matching, say of $t$ edges.

Promote each inactive endpoint of this matching to a routing
source, in addition to all active unit rows. At a promoted source,
designate its unit--unit exception $x_i$ and use the one-hole
block $Z_i=P_i\cup\{x_i,z_i\}$. At an active source retain the
earlier designated block $P_i\cup\{x_i\}$. All nondesignated
incident exceptions are complete to their other, higher-deficit
rows, and each has only one unit endpoint. All such routed
exceptions lie outside every source block: a designated exception
cannot be routed from another unit row, and a private hole is not
an exception. Each has at most three neighbors in every source row.

For a higher row $P_j$, its routed group is a clique. If two
members from the same source were nonadjacent, a common private
nonneighbor at that source would augment them and the unused
anchors. For different sources $i,k$, each common-nonneighbor
list has at least $r-7$ vertices. Independence augmentation
forces the two lists to be completely joined. At most one vertex
of $P_k$ lies in $Z_i$ (its private hole), so choose a listed
vertex outside $Z_i$. Its degree into $P_i$ is at most three,
contradicting the other list's size $r-7>3$. This proves clique
safety for the enlarged groups. Since each is complete to its
owner row, its order is at most $d_j-1$.

Retain $E=\sum(d_i-1)$, let $U$ be the number of unit rows,
and put $h=a-U\le E$. Every promoted source routes at least
one exception, by its support degree at least two. These routed
exceptions are counted once and their owner capacities sum to
$E$. The $2t$ endpoints of the unit matching are all promoted,
so $2t\le E$. Also the total number of support edges satisfies
$b\ge2U-t$. Using $b=a+E+1$ gives

$$
a\le E+2h+t+1\le\tfrac72E+1.
$$

Since $E\le r-a-1$, this proves the strengthened bound

$$
\boxed{9a\le7r-5.} \tag{13}
$$

It supersedes (4), not the independence-deletion requirements in
[Saturated-row suppression](saturated_row_suppression.md).

There is a related conditional completion for larger deficits.
If $|P_i|=r-d$, an exception $x$ sees only $q_i$ in $P_i$,
and its other row has exactly $d$ nonneighbors of $x$, call that
set $T$. Two-support augmentation makes $T$ complete to
$P_i\setminus\{q_i\}$; private support makes it anticomplete to
$q_i$. Thus $P_i\cup T$ is an $r$-set with exactly $d$
missing edges, and every outsider has at most $d+1$ neighbors
there, by the $(r+1)$-set cap. The linear outsider bound would
be useful for suppression, but these hypotheses have not been
forced for general higher-deficit rows.

**Correction of scope.** In the normalized core with $a\ge4$, this
particular proposed completion is actually impossible for $d\ge2$.
Its two-support product inequality would give

$$
(d-1)(r-d-d_j-1)\le1,
$$

whereas the total-deficit bound gives
$r-d-d_j-1\ge a-2\ge2$. Thus this configuration is confined to
unit rows; it cannot serve as the suggested higher-deficit reduction.
The [common-hole inequalities](two_support_normalization.md) record
a valid restriction on parallel exceptions without making that assumption.

## Remaining gap

The groups $C_j$ are clique-safe but not private relative to the
unchanged anchors: each member still has its unit anchor as a
second neighbor. Removing $P_i\cup\{x_i\}$ would remove $r$ vertices,
but this set is not necessarily a clique. The required drop in
independence has not been proved. The local suppression counterexample
in [Local-cap obstruction](local_cap_obstruction.md) prevents silently
assuming it.

Inactive units with higher-deficit neighbors and higher-deficit
support circuits remain. The upper bound (13) and the hereditary
restriction $r<64a^2$ leave
an unbounded range; they prove no new unrestricted infinite family
of positive cases of Problem 617.

### The balanced residual from a pendant parallel pair

Suppose a unit anchor $i$ has exactly two incident exceptions
$x,y$, both supported on $\{i,j\}$, and $xy$ is a nonedge.
Then $N[q_i]=Z=P_i\cup\{x,y\}$, so

$$
|H-Z|=(a-1)r,\qquad \alpha(H-Z)=a-1.
$$

The upper bound on independence follows by adjoining $q_i$;
the other $a-1$ anchors give equality. This is a balanced
residual, not an overloaded core of order $(a-1)r+1$.

If deletion of only $P_i\cup\{x\}$ fails to lower independence,
every resulting independent $a$-set must contain $y$: otherwise
it could be augmented by $q_i$. If the unit row is inactive,
Section 6 makes $y$ complete to $P_j$, so that witness also
avoids the entire owner row. No argument rules out this witness
or proves the balanced residual contains a $K_r$.

### Tight local blocks really occur

The matching extremizers in (8) alone cannot be contradictory.
Here is a local realization for every $r\ge4$, not a coloring
counterexample at order $r^2+1$. Put $q=r-1$. Properly edge-color
$K_{q,q}$ with $q$ colors (for example label both parts by
$\mathbb Z/q\mathbb Z$ and color $uv$ by $u+v$).
Write its parts as $P$ and $Y\cup\{u\}$, and fix $p_0\in P$.
Split $u$ into vertices $x,z$. Partition the $q-1$ edges from
$u$ to $P\setminus\{p_0\}$ into two nonempty sets and attach
them to $x,z$, retaining their colors. Remove $up_0$ and give
$xz$ its former color. Call the resulting colored graph $F$;
color every remaining pair with the distinguished color $H$.

Each of the $q$ other colors is a matching of $q$ edges on
$2q+1=2r-1$ vertices, hence has independence number $r$.
The graph $F$ is triangle-free: its only edge not between
$P$ and $Y\cup\{x,z\}$ is $xz$, whose endpoints have disjoint
neighborhoods in $P$. Thus $\alpha(H)=2$.
Also $\alpha(F)=q$, so $\omega(H)=r-1$. To check the upper
bound, an independent set meeting $Y$ avoids all of $P$ and
contains at most one of $x,z$, giving at most $q$ vertices.
One avoiding $Y$ contains at most one of $x,z$; either has a
nonempty neighborhood in $P$, again giving at most $q$.
The set $P$ attains this bound.

Choose $q_i\in N_F(z)\cap P$ and $q_j\in Y$. Relative to these
two independent $H$-anchors, the private rows are $P$ and
$Y\cup\{z\}$, each of order $r-1$, and $x$ is the sole
two-supported exception. It misses exactly $z$ in the second
row. This realizes the tight case $\lambda=0$ in (5)--(8).
Every vertex of $(P\setminus\{p_0\})\cup Y$ has $H$-degree
$r-1$, while $p_0$ has degree $r$.
Thus the example lacks both the overload and the private
minimum-degree condition of the normalized core; it does not
refute any core exclusion. It explains why the external
conditions, rather than the tight block alone, must enter a
successful suppression argument.

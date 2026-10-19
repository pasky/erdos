---
name: research/erdos_617/two_support_normalization
desc: A K_r-free two-supported core with minimum degree r on private vertices, stricter pair capacities, and an excluded support family.
tags: [graph-theory, proved, private-cliques, reductions]
sources: []
created: 2026-09-22T04:49:07Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/two_support_normalization

***

**Proved reductions and a construction exclusion, not a resolution.**
The [full-row deletion theorem](full_row_deletion.md) supplies,
for $r\ge12$, a two-supported induced core with $a<r$ anchors,

$$
|H|=ar+1,\quad \alpha(H)=a,\quad
|P_i|=r-d_i,\quad b=|B|\le r,\quad
\sum_i d_i=b-1.
\tag{1}
$$

Here the anchors $q_1,\ldots,q_a$ are independent, $P_i$ is
the anchor together with its singleton-support private neighbors,
and every exception in $B$ has exactly two anchor neighbors.
Every row is a clique and the hereditary density caps remain valid.
An outside vertex has at most one neighbor in any target $K_r$.

Among induced two-supported cores satisfying (1), choose one with
the fewest anchors. The following additional properties can be
imposed simultaneously:

$$
\boxed{\omega(H)\le r-1,\qquad
d_H(v)\ge r\quad\text{for every }v\in\bigcup_iP_i.}
\tag{2}
$$

The exception vertices are not asserted to have degree at least
$r$. No least-color edge budget is asserted for this selected color.

## 1. Every full clique can be deleted safely

First suppose a $K_r$ contains no anchor. Each of its vertices
has one or two neighbors among the anchors, giving at least $r$
incidences. Each of the $a<r$ outside anchors has at most one
neighbor in the clique, a contradiction.

Thus a $K_r$ contains exactly one anchor, say $q_i$.
Every clique vertex outside $P_i$ is an exception supported on
$i$, and their other support endpoints are distinct, by the same
outside-neighbor bound. There are at most $a-1$ such exceptions.
The clique therefore contains at least $r-a+1\ge2$ vertices of
$P_i$. Any omitted vertex of $P_i$ would have at least two
neighbors in the clique. Hence every $K_r$ has the form

$$
P_i\cup X,\qquad |X|=d_i,\quad X\subseteq B.
\tag{3}
$$


Delete this full clique. The remaining independence number is at
most $a-1$: an independent $a$-set outside it would forbid at
most $a<r$ vertices in the clique and could be augmented.
The other $a-1$ anchors survive. Every remaining vertex has one
or two neighbors among them: row $i$ has disappeared, and each
surviving exception has lost at most one support endpoint.
Singleton-support classes must again be cliques, since two
nonadjacent private neighbors would augment the retained anchors.
The new exceptional set is a subset of the old one.

The residual has order $(a-1)r+1$ and satisfies (1), contradicting
minimality. This proves the clique assertion in (2), including
the exclusion of full cliques that were not originally private rows.

## 2. Closed-neighborhood deletion at a private vertex

Suppose $v\in P_i$ has degree at most $r-1$. Its closed
neighborhood contains all of $P_i$ and the anchor $q_i$, but
contains no other anchor. Deleting it leaves at least
$(a-1)r+1$ vertices and independence number at most $a-1$.
Every surviving vertex has one or two remaining anchor neighbors,
for exactly the reason in Section 1.

Trim to $(a-1)r+1$ vertices while keeping all $a-1$ anchors.
The new singleton-support classes are cliques and the new
exceptional set is a subset of $B$. Counting gives
$\sum_i d'_i=b'-1\le r-1$. Thus the trimmed graph is another
smaller core of type (1), a contradiction. This proves the
degree assertion in (2).

The known span bounds exclude $a\le3$, so the normalized core
still has $a\ge4$. Since it is $K_r$-free, all deficits are
positive and

$$
d_i\le r-a,\qquad |P_i|\ge a\ge4.
\tag{4}
$$

The support degree at anchor $i$ is at least $d_i+1$, since
$d_H(q_i)=r-d_i-1+\deg_{\mathrm{supp}}(i)\ge r$.

For every proper nonempty anchor set $A$, write $B_A$ for
exceptions supported entirely in $A$. Then

$$
|B_A|\le\sum_{i\in A}d_i.
\tag{5}
$$

Otherwise the rows in $A$ and $B_A$ have more than $r|A|$
vertices and independence at most $|A|$, by adjoining the
unused anchors. Trimming while preserving $A$ again gives a
smaller two-supported core. Globally $b=\sum_i d_i+1$, so
the support multigraph is a minimal overloaded capacitated
system. This minimality is only within the two-supported class;
full induced minimal-ratio expansion has not been proved here.
The later [private-set expansion theorem](unit_deficit_propagation.md)
does establish $|N[I]|\ge r|I|+1$ for independent sets consisting
entirely of private vertices, and a Gallai forest on degree-$r$
private vertices.

## 3. Pair capacities and additional two-row caps

Let $B_{ij}$ be the exceptions supported on $\{i,j\}$. Then,
in the normalized core,

$$
\boxed{|B_{ij}|\le d_i+d_j-1.}
\tag{6}
$$

Indeed, the set $P_i\cup P_j\cup B_{ij}$ has independence
number at most two. If its order is at least $2r$, restrict
to $2r$ vertices and apply the
[two-row structure theorem](two_row_structure.md), valid for
$r\ge6$. It would contain a $K_r$, contradicting (2).
This proves (6).

More generally, before normalization, with positive deficits and
row sizes at least three, $|B_{ij}|\le d_i+d_j$, and equality forces
$d_i=d_j=1$. At equality the two-row theorem partitions the
$2r$-set into two $K_r$'s with matching cross edges.
Each private row of size at least three lies wholly in one
clique, and the independent anchors lie in different cliques.
The opposite anchor sees every exception absorbed into the
other clique, so at most one exception can be absorbed per row.

For a single exception $x$ supported on $i,j$, put
$m_i=|P_i\setminus N(x)|$, $m_j=|P_j\setminus N(x)|$.
In addition to the previously proved product inequality, one has

$$
m_j(m_i+d_i-1)\le(r-1)d_i,\qquad
m_i(m_j+d_j-1)\le(r-1)d_j.
\tag{7}
$$

The two nonneighbor sets are completely joined. In
$P_i\cup(P_j\setminus N(x))$, there are therefore at most
$(r-d_i-m_i)m_j$ nonedges. If $m_j\ge d_i$, its hereditary
cap requires at least $(r-1)(m_j-d_i)$, yielding (7).
If $m_j<d_i$, use $m_i\le r-d_i-1$ to obtain the inequality
directly. The other estimate is symmetric. These are necessary
conditions, not a completed capacity theorem.

## 4. A double-edge star support system is impossible

**Proposition.** Suppose $r\ge15$, the support multigraph is a
star with $L\ge3$ leaves and exactly two parallel edges to
each leaf, and every leaf row has deficit one. Then (1) is
impossible.

Counting gives $b=2L\le r$ and center deficit $d=L-1$.
Put $q=r-1$. In a leaf row, at most one of its two exceptions
can miss at most two private vertices: otherwise its private
$K_{r-1}$ and those exceptions form an $(r+1)$-set with at
most five nonedges, violating the local cap.

Call a leaf active if such an exception exists, and let $h$ be
the number of active leaves. Discard the designated exception
at each active leaf and call the remaining exception set $Y$.
Write

$$
u=L-h,\qquad s=|Y|=2L-h=L+u.
$$

Every member of $Y$ misses at least three vertices in its leaf
row. The two-support inequality with leaf deficit one is

$$
(m_{\rm leaf}-1)(m_{\rm center}-1)\le1.
$$

Thus every member of $Y$ misses at most one center-row vertex.

The $h$ members of $Y$ from active leaves form a target clique.
The designated exception at an active leaf has at least $r-3$
neighbors in its private row. Applying the local cap to that
row and this exception and any other outside vertex bounds
the latter vertex's row degree by three. If two of the $h$
remaining active-leaf exceptions were nonadjacent, their common
nonneighbor lists in their two leaf rows would each have at
least $r-7$ vertices. Independence augmentation forces those
lists to be completely joined. As each list is itself a
clique, their union would be a clique of order at least
$2r-14>r$, a contradiction.

The other $2u$ exceptions are supported on the center and $u$
leaves, so have independence number at most $u+1$. They span
at least $u-1$ target edges: deleting one endpoint per edge
always leaves an independent set. This bound remains valid,
though weak, when $u=0$. Consequently

$$
e_H(Y)\ge\binom h2+u-1.
\tag{8}
$$

The center-row subset cap, with each member of $Y$ missing
at most one center vertex, gives

$$
e_H(Y)\le\binom{s+1}{2}-(s-d)q.
$$

Here $s-d=u+1$ and $q\ge2L-1$, so the right side is at most

$$
\frac{(h-1)(h-2)}2.
\tag{9}
$$

The lower bound (8) minus (9) is $h+u-2=L-2>0$.
This proves the proposition.

## Remaining gaps

The later [unit-row theorem](unit_deficit_propagation.md) strengthens
the propagation here: every nondesignated exception at an active
unit row is complete to its other row, and same-owner propagated
groups are cliques. Its further one-hole block analysis makes
the unit support graph a matching and proves $9a\le7r-5$.
Inactive units attached to higher-deficit rows and higher-deficit
circuits are still not excluded.

[Saturated-row suppression](saturated_row_suppression.md) gives
safe deletion under explicit bounds on the unsaturated remainder.
It does not justify arbitrary row suppression. The
[local deficit-one example](local_cap_obstruction.md) still
invalidates the unrestricted one-row rule.

The star argument above does not cover larger leaf multiplicities
or general support circuits. No clique-safe owner assignment
with capacities $d_i$ has been proved for all exceptions.
The exception-edge penalties in the row subset caps remain.

Finally, (2) does not permit combining this core with the
least-budget core's surplus or its Gallai-forest statement on
all degree-$r$ vertices.
Its exception vertices may have degree below $r$, it has
only the restricted minimality (5), and its selected color
need not be a least color.


## Critical pruning does not by itself give a line graph

One may delete target edges while preserving independence $a$, and
assign them to another color on the core. This preserves all other
independence upper bounds. Relative to the retained anchors, no vertex
can lose its last support; new singleton-support classes must be
cliques. Thus one/two-support structure and $|B|\le r$ survive, and
minimum-anchor normalization can be repeated if necessary.

It would nevertheless be unjustified to infer claw-freeness merely
from independence-criticality and one/two-support structure. Here is
a counterexample to that weaker inference, **not** to the normalized
core hypotheses. Replace each edge of $K_4$ by a path of length three.
The resulting graph has 16 vertices and independence number seven.
If an independent set uses $k$ original branch vertices, it uses at
most $6-\binom k2$ subdivision vertices, so its size is at most
$k+6-\binom k2\le7$; equality is attained.

Every edge is independence-critical. On deleting an end edge of the
path between $u,v$, choose $u,v$ and one subdivision vertex on all
six paths, obtaining eight independent vertices. On deleting a middle
edge of that path, choose both its subdivision vertices, one branch
vertex outside $\{u,v\}$, and one subdivision vertex on each other
path, again obtaining eight.

Choose anchors consisting of branch vertex 0, the subdivision vertex
farther from 0 on each of its three incident paths, and the first
subdivision vertex on each of the cyclically oriented paths
$1\to2\to3\to1$. These seven vertices are independent. Each
outsider has one or two anchor neighbors: the other three branch
vertices have two, the three nearer-to-0 subdivision vertices have
two, and the three remaining subdivision vertices have one. Yet
branch vertex 0 is the center of an induced claw.

The example has neither the overloaded order nor the private row
sizes/deficit budget of the core. A theorem using those extra
hypotheses remains conceivable, but was not proved. In particular the
complete [multigraph line-graph exclusion](line_graph_obstruction.md)
cannot presently be applied to arbitrary two-supported cores.

## Exact critical witnesses on the support multigraph

The following holds for any independence-critical graph with a maximum
independent anchor set $I$ of order $a$ and one/two-support structure.
It uses no edge budget. Represent a private vertex by a singleton list
at its anchor, and an exception by its two-element support list.

For every independent set $J$ and every $X\subseteq J$,

$$
|X|\le\left|\bigcup_{x\in X}\operatorname{supp}(x)\right|. \tag{10}
$$

Otherwise adjoining the unused anchors augments $I$. Equivalently,
viewing singleton lists as loops, the support edges of every independent
set form a pseudoforest.

For a critical edge $uv$, take an independent $(a+1)$-set in $H-uv$.
Its support lists have an inclusion-minimal Hall-deficient subfamily
$C$. Every such subfamily contains both $u,v$, since any set not
containing both is independent in $H$ and satisfies (10). Write $V_C$
for its support union. Minimality gives $|C|=|V_C|+1$, every index
occurs in at least two lists, and the support incidence graph is
connected. Thus $C$ is a connected bicircular-matroid circuit, and
$uv$ is its unique target edge.

In particular, for $u\in P_i$, $v\in P_j$, $i\ne j$,

$$
\boxed{uv\in E(H)\ \Longleftrightarrow\
\text{there is a simple support path from $i$ to $j$ whose exceptions
are independent and anticomplete to $\{u,v\}$.}} \tag{11}
$$

For the forward implication, $u,v$ give two singleton lists in $C$.
If $h$ counts all singleton lists, the incidence bounds are

$$
2|V_C|\le2|C|-h=2|V_C|+2-h.
$$

Hence $h=2$ and every support index has exactly two incidences.
Connectedness leaves precisely an exception path joining the two
singleton lists. For the converse, a path of $k$ exceptions uses
$k+1$ anchors. If $uv$ were absent, its exceptions, $u,v$, and the
unused anchors would give $a+1$ independent vertices.

Consequently, for $u,v$ in the same private row,

$$
N_B(u)\subseteq N_B(v)
\ \Longrightarrow\
N(u)\cap\!\bigcup_{j\ne i}P_j
\supseteq N(v)\cap\!\bigcup_{j\ne i}P_j.
$$

Equal $B$-neighborhoods make $u,v$ true twins. Also the connected
components of the support multigraph correspond exactly to the graph
components of $H$: any critical edge has its two support lists in the
same connected circuit, while support incidences themselves are graph
edges to the anchors.

These statements characterize critical cross-row adjacencies; they do
not exclude long independent support paths or imply claw-freeness.

The [new component reduction](critical_component_reduction.md) supplies
a least-budget two-supported residue in one color. Its exception count
is not bounded by $r$, and full induced minimal-ratio minimality has not
been transferred. It therefore does not justify combining all of the
normalized hypotheses on this page with a least-color budget.

## Common holes of parallel exceptions

Here the bounded-exception normalized hypotheses (1)--(4) are in force.
Let row $P_i$ have deficit $d$, and let $X\subseteq B_{ij}$ have
$t>d$ vertices. Suppose some $T\subseteq P_j$ of order $d$ is
anticomplete to $X$. Put

$$
c=\min_{x\in X}d(x,P_i),\qquad
\mu=\overline e(P_i,T).
$$

Then

$$
\boxed{\mu\le dc,\qquad (t-d)c\le t.} \tag{12}
$$


The set $X$ is a clique: two nonadjacent members, one vertex of $T$,
and the anchors outside $\{i,j\}$ would be an independent
$(a+1)$-set. For a member $x$ attaining $c$, two-support augmentation
makes $P_i\setminus N(x)$ complete to $T$, giving $\mu\le dc$.
The set $P_i\cup T\cup X$ has order $r+t\le2r$ and exactly

$$
\mu+tr-\sum_{x\in X}d(x,P_i)
$$

nonedges. Its hereditary cap requires at least $(r-1)t$ nonedges.
Thus $\mu\ge t(c-1)$, proving (12).

For $d\ge2$, the two-support product inequality, with at least $d$
nonneighbors in row $j$, also gives

$$
c\ge r-d-d_j-\varepsilon_d,
\qquad \varepsilon_2=1,\quad \varepsilon_d=0\ (d\ge3).
$$

Indeed, if the nonneighbor count in $P_i$ is positive, substitute
it and the lower bound $d$ into that product inequality; if it is
zero, the displayed conclusion is immediate. Since
$d+d_j\le r-a+1$, (12) implies

$$
\boxed{(t-d)(a-1-\varepsilon_d)\le t.} \tag{13}
$$

In particular, for $d\ge3$ and $a\ge d+3$, no $d+1$ parallel
exceptions can have $d$ common private nonneighbors in their other
row. For $d=2$ and $a\ge6$, no three parallel exceptions have two
such common nonneighbors.

For a unit row, (12) with $t=2$ gives a different conclusion:
$P_i$ together with a common private hole is an $r$-set with between
one and two missing edges. If three parallel exceptions share that
hole, there is exactly one missing edge. The existence of enough such
blocks, and a general simultaneous suppression theorem for them, are
not established here.

## Maximum independent sets avoiding a private row

**Proved.** Minimum-anchor normalization gives

$$
\boxed{\alpha(H-P_i)=a\quad\text{for every private row }P_i.} \tag{14}
$$

If instead this independence number were at most $a-1$, the
remaining order would be $(a-1)r+d_i+1$. Every surviving vertex
has one or two neighbors among the retained $a-1$ anchors:
exceptions incident with $i$ simply become singly supported.
Trim to $(a-1)r+1$ vertices while retaining those anchors. Its
singleton-support classes are cliques, because a nonadjacent
pair in one class would augment the anchors. Its two-supported
exception set is a subset of $B$, so its order is at most $r$.
This is a smaller normalized-type core, a contradiction.

There is an exact form of a witness to (14). Represent private
vertices by loops and exceptions by edges on their support anchors.
An independent $a$-set $J\subseteq H-P_i$ satisfies Hall's
inequalities (10). Its support therefore uses all $a$ anchors,
and each connected component of the resulting support multigraph
has as many edges as vertices: every component is unicyclic.

In the component through $i$, retain the simple path from $i$
to its unique cycle, together with that cycle. A loop is allowed
as the cycle. This produces an independent subfamily $C$ whose
support $A$ contains $i$, with

$$
|C|=|A|,\qquad C\cap P_i=\varnothing.
$$

Thus $C$ has one of two shapes: an exception path ending at one
private vertex of another row, or an exception cycle with a path
attached from $i$. A two-edge cycle of parallel exceptions is
allowed. There are no extra branches.

The set $C$ dominates every vertex whose anchor support is
contained in $A$, in particular every private row indexed by
$A$. Otherwise that vertex, $C$, and the untouched anchors
would form an independent $(a+1)$-set. This is domination in
the original graph, not just a property of the support graph.

One conditional consequence isolates the complete-owner difficulty.
Suppose every exception has a chosen supporting row to which it
is complete. A unit row $i$ owns none, since an exception complete
to its $K_{r-1}$ would create $K_r$. Assign every member of its
witness $C$ to its owner, assigning a terminal private vertex to
its own row. These $|A|$ assignments omit $i$, so two collide.
A collision involving the private vertex contradicts independence.
Hence two independent exceptions have the same complete owner.
Individual completeness does not therefore justify treating owner
groups as cliques.

The reduction does not bound the path or cycle length, the
number of private vertices dominated by each member of $C$,
or the overlap of owner conflicts from different starting rows.
Consequently it does not give the missing capacity charge or
an unconditional row-suppression theorem. The row deletion,
unicyclic support count, and domination assertion were checked
independently.

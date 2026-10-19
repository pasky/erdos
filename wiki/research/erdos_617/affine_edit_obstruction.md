---
name: research/erdos_617/affine_edit_obstruction
desc: Affine extensions require order r^(5/2) old-edge recolorings and edit-graph vertex-cover number at least 2r minus order sqrt(r).
tags: [graph-theory, proved, constructions]
sources:
  - erdos_gyarfas_1999_split_balanced_colorings_complete_graphs
created: 2026-09-22T04:18:35Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/affine_edit_obstruction

***

**Proved construction obstruction, not a solution of Problem 617.** Section 5 of
the
[independent input](independent/small_independence_and_packing_obstructions.md)
states the quadratic bounds below but refers to an unavailable equality proof.
That proof is reconstructed here. The second independent input's defective-row
idea, combined with the established hereditary span theorem, gives the stronger
bound proved first.

Suppose an affine plane of order $r\ge3$ exists. Start from its standard
coloring: $r-1$ parallel classes get separate colors and the remaining two
classes share the last color. The construction was checked in the
[Erdős--Gyárfás source](../../../library/extremal_graph_theory/erdos_gyarfas_1999_split_balanced_colorings_complete_graphs/_index.md),
the paragraph immediately following Conjecture 1.

Add one vertex and recolor some old edges. If the resulting coloring
were a counterexample, the number $M$ of old edges whose final color
differs from their original color would satisfy

$$
\boxed{M>\frac{(r-1)r^2}{16\sqrt r+1}
=\left(\frac1{16}-o(1)\right)r^{5/2}.}
$$

The earlier bounds remain useful at smaller parameters:

$$
M\ge2(r-1)^2;
\qquad M\ge(r-1)(2r-1)\quad\text{if }r\ge5.
$$

The newly added star edges are not counted.

## Defective rows and the hereditary span theorem

Here is a one-graph statement with no affine-plane or edge-budget
hypothesis. Let $G$ have independence at most $r$ on $X\cup\{v\}$,
where $X$ is partitioned into $r$ sets $L_j$ of order $r$.
Assume every inherited cap $e(G[W])\le D_r(|W|)$ from
[Reductions](reductions.md). Let $t$ count edges of $G[X]$
between different $L_j$. Then, for $r\ge3$,

$$
\boxed{t>\frac{r^2}{16\sqrt r+1}.} \tag{1}
$$


Let $d(x)$ count neighbors of $x$ in the other old parts.
If $x,y$ are nonadjacent in one part, choose independently one
uniform vertex from each other part. The resulting $(r+1)$-set
must contain an edge. Its expected edge count is at most
$(d(x)+d(y))/r+t/r^2$, so

$$
d(x)+d(y)\ge r-t/r. \tag{2}
$$

Call an old part defective if it is not a clique, and let $s$
count such parts. Choose one nonedge in each defective part.
Their endpoints are all distinct, and $\sum_{x\in X}d(x)=2t$.
For $t<r^2$, summing (2) gives

$$
s\le\frac{2rt}{r^2-t}. \tag{3}
$$


Suppose contrary to (1) that $t\le r^2/(16\sqrt r+1)$.
Then $s\le\sqrt r/8$. The $k=r-s$ intact original parts are
disjoint $K_r$'s, leaving a residue $R$ of order $sr+1$.
If it contains an independent $(s+1)$-set, avoiding its neighbors
in the intact parts leaves lists of size at least $k-1$.
The local cap makes every pair's cross graph a matching.
[Matching-transversal rigidity](packing_tools.md) therefore forces

$$
t\ge(k-1)\binom k2.
$$

All these edges join different original parts and are counted in
$t$. But $s\le r/8$, so $k\ge7r/8$, and for $r\ge3$ both
$k$ and $k-1$ are at least $r/2$. Thus

$$
t\ge r^3/16>\frac{r^2}{16\sqrt r+1},
$$

a contradiction.

Hence $\alpha(G[R])\le s$. For $s=0$ this contradicts nonemptiness;
for $s=1$ it gives a forbidden $K_{r+1}$. For $s\ge2$, the
[hereditary span theorem](hereditary_span_bound.md) applies because
$r\ge64s^2$, again a contradiction. This proves (1).

Apply (1) to each original singleton-direction affine color. Every counted edge
is an old edge newly assigned that color, and each recolored old edge is counted
at most once, in its final color. Summing proves the displayed $r^{5/2}$ repair
bound. Both the defective-row count and its combination with the span theorem
were checked by the author and are author-recorded. No claim places an arbitrary
counterexample close to an affine coloring.

## With only the local cap: the sharp exponent is four thirds

Section 5 of the
[second independent input](independent/clique_residue_and_affine_repair.md)
proves a different-scope statement: retain $\alpha(G)\le r$ and only the
$(r+1)$-set cap, with the same old partition and $t$. Then

$$
t\ge\frac14r^{4/3}-\frac12r,\qquad
t\ge(4^{-2/3}-o(1))r^{4/3}. \tag{4}
$$

Here is the checked argument. If $t<r^2$, (2) shows that every
within-part nonedge meets

$$
H=\{x:d(x)\ge(r-t/r)/2\},\qquad
h=|H|\le\frac{4rt}{r^2-t}.
$$

Thus $C_j=L_j\setminus H$ are cliques. Suppose $h<r$, so none
is empty, and put $q=\lfloor\sqrt t\rfloor$. Every
$b\in H\cup\{v\}$ has at most $q$ nonneighbors in some $C_j$:
otherwise independent uniform choices from its nonneighbor lists
have expected cross-edge count at most $t/(q+1)^2<1$,
contradicting $\alpha(G)\le r$.

Assign $b$ to such a core. If $h_j=|H\cap L_j|$, some core
receives at least $h_j+1$ assignments. The core and this many
assignees have $r+1$ vertices and at most
$(h+1)(\sqrt t+h/2)$ nonedges. Therefore

$$
r-1\le(h+1)(\sqrt t+h/2). \tag{5}
$$

For $t=O(r^{4/3})$, this gives
$r-1\le(4+o(1))t^{3/2}/r+o(r)$, proving the asymptotic
bound. Any sequence violating the asserted asymptotic lower
bound has a subsequence with bounded $t/r^{4/3}$, to which
the preceding argument applies.

For the explicit bound, $t<r^2/16$ ensures $h<r$ and
$h\le9t/(2r)$. In (5) use
$\sqrt t+h/2\le25\sqrt t/16$ and
$h+1\le9(t+r/4)/(2r)$ to obtain

$$
r-1\le\frac8r(t+r/4)^{3/2}.
$$

Consequently
$t\ge[r(r-1)]^{2/3}/4-r/4\ge r^{4/3}/4-r/2$.
The last inequality follows from $(1-1/r)^{2/3}\ge1-1/r$.
For $r\le8$ the claimed bound is nonpositive; for $r\ge8$
the complementary case follows from
$r^2/16\ge r^{4/3}/4-r/2$. To verify the latter for all
$r$, set $z=r^{1/3}$ and use $z^3-4z+8>0$ for $z\ge0$.

The [sharp local-cap example](local_cap_obstruction.md) has
$t=O(r^{4/3})$, even with distinguished degree $r-1$.
It violates the full hereditary caps, so it does not contradict
(1). The input's $r^{7/3}$ multicolor consequence is valid but
superseded by the $r^{5/2}$ bound here; no optimal exponent for
actual affine repairs is established.

## A deleted pair must cover a second line

Fix one original singleton-direction color, called the target color.
Its original lines $L_1,\ldots,L_r$ are disjoint $K_r$'s. Let $A$
be the set of old edges added to this color. Every edge of $A$
joins different original lines. The
[full-resolution obstruction](packing_tools.md) forces at least
one old target edge $xy$ to be deleted from a line $L$.

Suppose $|A|\le2r-2$. We claim that every deleted pair $xy$
jointly covers another entire original line with target neighbors.
Otherwise, on each of the other $r-1$ lines its common target
nonneighbors form a nonempty list. Let $t_1\le t_2$ be the two
smallest list sizes. An independent transversal of these lists,
together with $x,y$, would have size $r+1$.

Uniform independent representatives therefore have expected cross-edge
count at least one. Each cross edge occurs with probability at most
$1/(t_1t_2)$, so there are at least $t_1t_2$ edges of $A$
between the lists. Removing vertices from the two smallest lists
requires at least $2r-t_1-t_2$ additional edges incident with $x,y$.
These are disjoint edge counts. Hence

$$
|A|\ge 2r-t_1-t_2+t_1t_2
=2r-1+(t_1-1)(t_2-1),
$$

a contradiction.

Let $B$ be a line covered by $xy$. It must itself contain a deleted
edge $uv$: otherwise it is a target $K_r$, and each external
vertex has at most one neighbor there, whereas $r>2$.
Apply the claim to $uv$. Its covered line is necessarily $L$;
covering a third line would use at least $r+r$ distinct additions.
Mutual coverage of $L,B$ uses at least $r-2$ additions from
$x,y$ to $B\setminus\{u,v\}$, at least $r-2$ from $u,v$
to $L\setminus\{x,y\}$, and at least two among the four centers.
Thus

$$
|A|\ge2r-2.
$$

This proves the first per-color lower bound.

## Equality classification

Suppose $|A|=2r-2$. All the preceding counts are exact, so every
addition lies between $L,B$. The center edges form a matching;
relabel to make them $xu,yv$. Each noncenter has exactly one
cross-neighbor among the opposite centers. Write

$$
L\setminus\{x,y\}=L_u\sqcup L_v,\qquad
B\setminus\{u,v\}=B_x\sqcup B_y
$$

according to that neighbor.

Every other original line is intact: a deleted pair there would
have to cover another line, but has no incident additions.
There are also no target edges from these other lines to $L\cup B$
or to each other. Therefore

$$
\alpha(G[L\cup B])\le2,
$$

since an independent triple could be supplemented by one vertex
from each of the other $r-2$ lines.

Both sets of noncenters are cliques: two nonadjacent noncenters
in one line could be joined by any noncenter of the other.
Also $x$ is complete to $L_u$, $y$ to $L_v$, $u$ to $B_x$,
and $v$ to $B_y$. For example, a missing $xz$ with
$z\in L_u$ would make $x,z,v$ independent.
The only further possible deletions obey

$$
\begin{array}{c|c}
\text{deleted pair type}&\text{necessary empty part}\\ \hline
x\text{--}L_v&B_y=\varnothing\\
y\text{--}L_u&B_x=\varnothing\\
u\text{--}B_y&L_v=\varnothing\\
v\text{--}B_x&L_u=\varnothing .
\end{array}
$$

For instance, a missing $xz$ with $z\in L_v$ could otherwise
be supplemented by a vertex of $B_y$ to give an independent triple.
The other assertions are symmetric.

If all four parts are nonempty, the only old deletions in these
two lines are $xy,uv$. Their union consequently has

$$
2\binom r2-2+(2r-2)=r^2+r-4
$$

target edges. For $r\ge5$, this exceeds the inherited cap
$D_r(2r)=r^2$.

If a part is empty, exchange the two lines and relabel their
centers to assume $B_y=\varnothing$. Then

$$
Q=(B\setminus\{v\})\cup\{x\}
$$

is a $K_r$. Every vertex of $L_u$ would have two neighbors
$x,u$ in $Q$, so $L_u=\varnothing$. Now

$$
Q'=(L\setminus\{x\})\cup\{v\}
$$

is another $K_r$. They are disjoint and, with the untouched
lines, give the forbidden full resolution.

Thus equality is impossible for $r\ge5$, proving $|A|\ge2r-1$
in that range. Sum the per-color bounds over the $r-1$
singleton-direction colors. Each recolored old edge is counted
only in its final color, so their sum is at most $M$.
This proves both claimed edit-distance bounds.

The argument does not put an arbitrary counterexample near an affine
plane, and it does not exclude modifications above the stated budget.

## A vertex-cover obstruction for changed old edges

Section 6 of the
[third independent input](independent/uniform_capacity_and_clique_packings.md)
gives a distinct restriction on the concentration of edits. Define

$$
q=\min\{d\ge1:\tbinom{d+1}{2}\ge r-1\}.
$$

If $k$ old points are deleted, the old coloring is unchanged on the
remaining points, and $k+1$ new vertices have arbitrary incident edges,
a hypothetical counterexample must satisfy

$$
\boxed{k\ge
\left\lceil\frac{(r-1)q^2}{r+q-2}\right\rceil
=2r-O(\sqrt r).} \tag{6}
$$

This holds for every $r\ge3$ and $0\le k\le r^2$.

Fix a singleton direction and write $d_L$ for the number of deleted
points on its line $L$. Suppose all $d_L<q$. Since $q\le r$, every
residual line is nonempty. Each new vertex must be complete in this
color to one residual line: otherwise one nonneighbor from each of
the $r$ lines extends it to an independent $(r+1)$-set.

A line $L$ can be complete in this color to at most $d_L$ new vertices.
Otherwise its $r-d_L$ surviving points and $d_L+1$ such new vertices
form an $(r+1)$-set seeing at most

$$
1+\binom{d_L+1}{2}\le1+\binom q2<r
$$

colors. Assigning each new vertex to an available line gives capacity
only $\sum_Ld_L=k$, less than $k+1$. Thus each singleton direction
has a line containing at least $q$ deleted points. Empty residual lines
already satisfy this conclusion, rather than forming an exception.

Choose one such line in each of the $r-1$ singleton directions and
exactly $q$ deleted points on each. If $c_p$ counts selected incidences
at deleted point $p$, distinct selected lines meet at most once, so

$$
\sum_pc_p=(r-1)q,\qquad
\sum_pc_p(c_p-1)\le(r-1)(r-2).
$$

Cauchy--Schwarz gives

$$
(r-1)^2q^2\le k\sum_pc_p^2
\le k(r-1)(r+q-2),
$$

proving (6). The asymptotic form uses $q=\sqrt{2r}+O(1)$.

For a one-vertex repair, let $S$ be a vertex cover of the graph whose
edges are the changed old pairs. Removing $S$ leaves exactly the old
induced coloring. Regard $S$ and the added vertex as the new vertices
in (6); hence (6) bounds the minimum vertex-cover size of the edit graph.
The edge-count lower bound alone allows a cover to support up to
$k(r^2-k)+\binom k2$ edits and yields only an order-$\sqrt r$ cover
bound. Thus (6) is not superseded by the stronger numerical edit count.
The proof, including the empty-line case, was checked by the author and
is author-recorded.

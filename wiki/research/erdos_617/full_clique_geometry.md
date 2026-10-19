---
name: research/erdos_617/full_clique_geometry
desc: Matching-valued reciprocity, exact transversal structure of same-color clique fans, and pointwise degree capacities.
tags: [graph-theory, proved, color-coupling]
sources: []
created: 2026-09-22T05:15:00Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/full_clique_geometry

***

**Proved necessary conditions, not a solution.** Throughout, an
$r$-coloring of $K_{r^2+1}$ satisfies $\alpha(G_j)\le r$ in every
color. A full clique means a monochromatic $K_r$. Recall that an
outside vertex has at most one neighbor in a full clique in its color.

## 1. Matching-valued reciprocity

Let full cliques $Q,R$ of distinct colors $i,j$ meet at $u$, and put
$A=Q\setminus\{u\}$, $C=R\setminus\{u\}$. In each row and column
of the cross array $A\times C$, every color $k\ne i,j$ appears once
or twice, while colors $i,j$ together appear at most once. Indeed,
the edges from a vertex of $A$ to $R$ must contain every color
other than $j$, and the edge to $u$ already has color $i$.
The analogous statement holds for a vertex of $C$.

For every $k\ne i,j$, the bipartite color-$k$ graph on $A,C$ has
a perfect matching. Otherwise a Hall-deficient $S\subseteq A$
would give the color-$k$ independent set

$$
\{u\}\cup S\cup(C\setminus N_k(S))
$$

of order greater than $r$. Choose a perfect matching for each of
these $r-2$ colors. Their deletion from $K_{A,C}$ leaves a single
perfect matching. It contains all color-$i$ and color-$j$ edges;
its color-$k$ edges form a matching between exactly the vertices
whose original color-$k$ degree in the cross array was two.

Using the exception-set notation relative to an anchor clique,
these two vertex sets are

$$
\boxed{B_k(R)\cap Q\quad\text{and}\quad B_k(Q)\cap R.}
$$

Thus they admit a color-$k$ perfect matching. This strengthens the
cardinality reciprocity in [Cross-color cores](cross_color_cores.md),
and applies to any intersecting full cliques, not only a private-row
incidence. It does not supply a simultaneous clique-safe assignment.

## 2. Exact structure of a same-color fan

Suppose $s\ge2$ distinct full color-$i$ cliques meet at $u$.
Their petals $A_1,\ldots,A_s$, each of order $r-1$, are disjoint.
There are no color-$i$ edges between petals: a vertex's unique
color-$i$ neighbor in another full clique is already $u$.
For every $j\ne i$, each pair of petals is therefore joined by
a color-$j$ perfect matching.

On $X=\bigcup_t A_t$, color $j$ has exactly
$(r-1)\binom s2$ edges and independence at most $r-1$, because
$u$ is isolated in this color on $X\cup\{u\}$. This is equality
in complementary Turán. Consequently

$$
\boxed{G_j[X]=(r-1)K_s,}
\tag{1}
$$

with each component meeting every petal exactly once. In particular
$s\le r$. The cross arrays form a resolvable transversal design.

One necessary multiplicity bound is

$$
\binom{r-s+1}{2}\ge r-1. \tag{2}
$$

Indeed, put $Y=V\setminus(X\cup\{u\})$, so
$|Y|=r^2-s(r-1)$. If $y\in Y$ is not joined to $u$ in color $j$,
it must be complete in color $j$ to one of the $K_s$ blocks in (1).
Otherwise one nonneighbor from each block, together with $u,y$,
would be an independent $(r+1)$-set.

If (2) failed, at most $r-s$ such vertices could be complete to any
one block: the block and $r-s+1$ complete outsiders form an
$(r+1)$-set with at most $\binom{r-s+1}{2}<r-1$ nonedges.
Hence at most $(r-1)(r-s)$ vertices of $Y$ are nonneighbors of
$u$ in color $j$, giving $d_j(u)\ge r$. Summing over $j\ne i$
and using $d_i(u)\ge s(r-1)$ gives total degree at least
$(r-1)(r+s)>r^2$, a contradiction.

Both this fan argument and the matching-valued reciprocity were
checked by the author and are author-recorded.

## 3. A stronger pointwise capacity bound

Let $Q$ be any full color-$i$ clique and $u\in Q$. In the private
systems relative to $Q$, write $d_{j,u}=r-|P_{j,u}|$ and

$$
h(u)=\sum_{j\ne i}|\{x\in B_j(Q):u\in K_j(x)\}|,
\quad z_i(Q)=e_i(Q,V\setminus Q).
$$

Anchor degrees give

$$
d_i(u)=2r-1+\sum_{j\ne i}d_{j,u}-h(u).
$$

Each $d_{j,u}\le b_j-1$, since the private deficits are nonnegative
and sum to $b_j-1$. Also
$\sum_{j\ne i}b_j=r^2-r+1-z_i(Q)$. Therefore

$$
\boxed{d_i(u)+z_i(Q)+h(u)\le r^2+1.} \tag{3}
$$

Since $z_i(Q)\ge d_i(u)-(r-1)$, this gives
$2d_i(u)+h(u)\le r^2+r$. A same-color full-clique fan through
$u$ consequently has

$$
\boxed{s\le\left\lfloor\frac{r(r+1)}{2(r-1)}\right\rfloor.} \tag{4}
$$

For large $r$, (4) is stronger than (2); the exact structure (1)
remains useful independently of these numerical bounds.

None of these results forces the existence of a fan violating (4),
or closes the core exclusions in the research index.


## 4. Private-row directions inside a same-point fan

For full cliques $Q,R$ of different colors meeting at $u$, write
$Q\to R$ if $R$ is the full private row at $u$ relative to $Q$.
Equivalently, if $R$ has color $j$, there are no color-$j$ edges
between $Q\setminus\{u\}$ and $R\setminus\{u\}$. Each $Q$ has
at most one outgoing arc to cliques of a fixed other color at $u$.

**Propagation rule.** If $Q\to R$ and $R'$ is another full clique
of $R$'s color through $u$, then $R'\to Q$. Moreover the cross
array between $R'\setminus\{u\}$ and $Q\setminus\{u\}$ has a
perfect matching in $R$'s color and no edges in $Q$'s color.

Indeed, a vertex $x\in R'\setminus\{u\}$ already has its edge
to $u$ in color $j$. It must have another color-$j$ neighbor in
$Q$: otherwise it would lie in the private row $R$. These further
edges form a matching, because any vertex outside the full clique
$R'$ has at most one color-$j$ neighbor there. Both parts have size
$r-1$, so the matching is perfect. A vertex $y\in Q\setminus\{u\}$
now has one color-$j$ edge to $R'$, as well as its edge to $u$ in
$Q$'s color $i$. Its edges to $R'$ must contain every color other
than $j$, so every color appears exactly once. No cross edge has
color $i$, and $Q$ is the reverse private row.

Let $s_i(u)$ count full color-$i$ cliques through $u$. If
$s_i(u),s_j(u)\ge2$ and there is any private arc between these two
color groups, then

$$
\boxed{s_i(u)=s_j(u)=2.}
$$

To see this, start from $Q\to R$. Every other $R'$ points to $Q$,
and every other $Q'$ then points to $R'$. Uniqueness of the outgoing
row at $Q'$ forces exactly two cliques in the $j$ group; reversing
the argument forces exactly two in the $i$ group. Their four forced
arcs form a directed four-cycle, and uniqueness excludes all reverse
arcs. In particular a group of multiplicity at least three has no
private arcs to or from any other repeated color group.

There is a corresponding aggregate restriction. At $u$ let $p,d,h$
count color groups of sizes one, two, and at least three, and set
$t=\sum_i s_i(u)\le r+1$. If $A(u)$ counts private arcs there, then

$$
A(u)\le p(t+d+h-1)+2d(d-1). \tag{5}
$$

Singleton pairs contribute at most $p(p-1)$; a singleton and a
group of size $s\ge2$ contribute at most $s+1$; double pairs
contribute at most four; all other repeated pairs contribute zero.
These contributions give (5).

Let $F$ count all full cliques, and put
$c=r-2+(r-1)e(r)$, with $e(r)$ as in
[Cross-color cores](cross_color_cores.md), for $r\ge7$. The full-row
count there implies

$$
\sum_u A(u)\ge cF+\sum_Q z_{\operatorname{col}(Q)}(Q).
$$

Exact double counting and $d_i(u)\ge(r-1)s_i(u)$ give

$$
\sum_Q z_{\operatorname{col}(Q)}(Q)
=\sum_{u,i}s_i(u)(d_i(u)-r+1)
\ge(r-1)\sum_{u,i}s_i(u)(s_i(u)-1).
$$

Consequently

$$
\sum_u\left[p(t+d+h-1)+2d(d-1)
-(r-1)\sum_i s_i(u)(s_i(u)-1)\right]\ge cF. \tag{6}
$$

The propagation, group classification, and count were separately
checked. The inequality does not contradict the configurations with
many singleton color groups at each point, and is not a completion
of the clique geometry into an affine net.

## 5. Disjoint full cliques of distinct colors

Suppose $Q_1,\ldots,Q_t$, $t\ge2$, are disjoint full cliques of
distinct colors. Between any two blocks, every color forms exactly one
perfect matching. This holds even in the critical partial coloring:
every color requires at least $r$ cross edges, by domination of a
foreign independent $r$-set and the full-clique outsider bound. These
$r$ lower bounds exhaust all $r^2$ cross pairs.

In a selected color $j$, the other $t-1$ blocks therefore have
$r\binom{t-1}{2}$ edges and independence at most $r$. Complementary
Turán equality makes their graph $rK_{t-1}$. Every vertex of $Q_j$
must be complete to one of these $r$ cliques, or it augments an
independent transversal. Its cross degree is exactly $t-1$, and the
perfect matchings make these attachments bijective.

Thus on the selected union the color-$j$ graph consists of $r$ disjoint
$K_t$'s plus the edges of $Q_j$, which joins one distinguished vertex
from each $K_t$. Relative to any foreign selected block, all its private
rows consequently have size at least $t$.

Put $d=r-t$. For $r\ge7$, the
[two-support owner argument](two_supported_private_cliques.md) gives

$$
d(d+1)\ge\frac{2(r-1)}3,
\qquad
\boxed{t\le r-
\left\lceil\frac{\sqrt{1+8(r-1)/3}-1}{2}\right\rceil.} \tag{7}
$$

Here is why the old argument applies without an exception-count bound.
All row deficits are at most $d$. If $2d\le r-1$, every supporting
pair meets the size condition of the two-support product inequality.
The full-row absorption rule handles zero deficits, so every exception
can be assigned a positive-deficit owner with at most $\max(d_i,2)$
missing row neighbors. There are one more exceptions than total deficit,
hence some row owns at least $d_i+1$. The local cap excludes $d_i=1$
for $r\ge7$ and gives $3d_i(d_i+1)\ge2(r-1)$ otherwise. If
$2d>r-1$, the displayed bound is automatic.

## 6. Nearly dominating full cliques are disjoint

For a full color-$i$ clique $Q_i$, write

$$
Y_i=\{x\notin Q_i:N_i(x)\cap Q_i=\varnothing\},\qquad m_i=|Y_i|.
$$

If full cliques $Q_i,Q_j$ of different colors intersect, then

$$
\boxed{m_i+m_j\ge r-1.} \tag{8}
$$

Indeed their two own colors together form a matching in the petal
cross array, as in Section 1. The two edge counts there are
$r-1-|Y_i\cap Q_j|$ and $r-1-|Y_j\cap Q_i|$. Their sum is at most
$r-1$, proving (8).

Consequently full cliques chosen in distinct colors with
$m_i\le\lfloor(r-2)/2\rfloor$ are pairwise disjoint and obey (7).
However, the subsequent [private-fiber count](critical_component_reduction.md)
gives $m_i\ge r-1$ for every full clique in an actual coloring or a
spanning partial witness coloring. Thus the displayed small-$m_i$
hypothesis cannot occur in the present problem. Equation (8) remains
valid, but this criterion does not provide a useful division of the
actual nongood colors into cases. All nongood critical colors containing
a full clique instead incur the saturated noncomponent-clique charge;
the $K_r$-free nongood colors remain uncontrolled by that charge.

## 7. A fully saturated pencil in the critical partial coloring

**Proved conditional structure, not a forced configuration.** Work in
the [critical partial coloring](critical_component_reduction.md).
Suppose a vertex $u$ lies in a full component $Q_i$ in every color $i$.
Put $A_i=Q_i\setminus\{u\}$ and
$Y=V\setminus\bigcup_iQ_i$. Distinct $Q_i$ meet only at $u$, so $|Y|=r$.

Every pair $uy$, $y\in Y$, is uncolored, because all colored
neighborhoods of $u$ lie in their respective components. For $i\ne j$,
every $y\in Y$ must have a color-$i$ neighbor in $Q_j$: otherwise it
augments the independent $r$-set $Q_j$ in color $i$. That neighbor
lies in $A_j$. Color $j$ is absent from $yA_j$, and its $r-1$ vertices
are exhausted by the $r-1$ required foreign colors. Thus every such
neighbor is unique and every $Y$--$A_j$ pair is colored.
Consequently $\{u\}\cup Y$ is a whole connected component of the
uncolored graph, with all the edges $uY$ and possibly further edges
inside $Y$.

For $i\ne j$, let $f_{ij}:Y\longrightarrow A_j$ give this unique
color-$i$ neighbor. Each fiber is a color-$i$ clique. If $y,z$ in
one fiber were nonadjacent in that color, then

$$
\{y,z\}\cup(A_j\setminus\{f_{ij}(y)\})
$$

would be an independent $r$-set outside the color-$i$ component $Q_i$.
The latter complement has independence $r-1$, a contradiction.

### The neighbor maps alone do not contradict one another

There is a finite auxiliary model at $r=6$, not a coloring of $K_{37}$.
Take $Y$ to be a cycle of length six, with its six edges in distinct
colors. For one omitted color, order the vertices along the remaining
five-edge path. The following permutations of five symbols have
consecutive rows agreeing only in their corresponding path-edge
coordinate, and nonconsecutive rows agreeing nowhere:

$$
\begin{pmatrix}
0&3&4&2&1\\
0&1&3&4&2\\
4&1&2&0&3\\
1&4&2&3&0\\
2&0&1&3&4\\
3&2&0&1&4
\end{pmatrix}.
$$

Use the symbols as the vertices of the omitted color's petal, and
the coordinates as the other colors. Each row being a permutation
gives the required unique neighbor of every foreign color; each fiber
is a singleton or the corresponding colored cycle edge. Relabeling
does the same for each omitted color.

This verifies only the neighbor-map and clique-fiber conditions.
Edges between petals and the other global independence constraints
are unspecified. The attempted contradiction using these conditions
alone therefore fails, and no argument forces a fully saturated
vertex to exist in the first place.

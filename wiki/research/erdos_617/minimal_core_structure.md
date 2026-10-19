---
name: research/erdos_617/minimal_core_structure
desc: A square-root upper gap for the least-budget core, Gallai structure on its degree-r vertices, and a conditional low-clique obstruction.
tags: [graph-theory, proved, reductions, stability]
sources: []
created: 2026-09-22T04:49:07Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/minimal_core_structure

***

**Proved partial results; the problem remains unresolved.** These
statements concern the same least-budget minimal-ratio core as in
[Minimal-ratio potential](minimal_ratio_potential.md), not the
possibly different two-supported color.
The later [greedy block charge](greedy_block_charge.md) adds the
uniform upper bound $a\le\lfloor3r/4\rfloor$ to the restrictions here.

Throughout, $r\ge12$, $n=ar+1$, $4\le a\le r-3$, and $H$ satisfies

$$
\alpha(H)=a,\quad \delta(H)\ge r,\quad \omega(H)\le r-1,\quad
2e(H)\le ar(r-1)+r(r+1).
$$

Every proper induced set has order at most $r$ times its
independence number, and all inherited caps hold. Write

$$
s(v)=d_H(v)-r,\quad S=\sum_v s(v),\quad
\mathcal D=\sum_v(r-c_H(v)),\quad h=r-a.
$$

The established consequences needed below are

$$
S\le rh,\qquad
\mathcal D-n\le r(h-2)-2/a, \tag{1}
$$


$$
|N_H[I]|\ge r|I|+1
\quad(I\ne\varnothing\text{ independent}), \tag{2}
$$

and, for nonadjacent $x,z$ with $c$ common neighbors,

$$
s(x)+s(z)\ge c-1. \tag{3}
$$


## 1. A square-root gap below the original independence parameter

**Theorem.**

$$
\boxed{r<8(r-a)^2,\qquad a<r-\sqrt{r/8}.} \tag{4}
$$


Suppose instead that $r\ge8h^2$, and set $k=h-1$. The three
numerical hypotheses of the
[clustering lemma](large_clique_clusters.md) hold:

$$
r>(k+1)^2+1,\quad r-3k\ge2,\quad
r-1>\tfrac32k(k+1).
$$

Use all cliques of order at least $r-k$ to form its clusters
$C_1,\ldots,C_q$. The clustering and capacity arguments use only
the inherited caps, so apply to $H$ despite its smaller order.
Each cluster has at most $r$ vertices. Let $Q_j$ be a maximum
clique in its cluster and write

$$
|Q_j|=r-t_j,\quad |C_j|=r-b_j,\quad
1\le t_j\le k,\quad 0\le b_j\le t_j.
$$

Let $U$ be the uncovered set, $T=\sum_jt_j$, and let $L$ count
total excess cluster incidences.

Every vertex has clique deficit at least one. An uncovered vertex
has deficit at least $k+1$, so (1) gives

$$
k|U|\le\mathcal D-n\le r(h-2)-2/a<rk.
$$

Thus $|U|<r$, and cluster capacity implies $q\ge a$.

### Independent representatives after removing high-surplus vertices

Put

$$
B=\{v:s(v)\ge r/4\},\qquad |B|\le4h.
$$

A vertex in two anchors has degree at least $2(r-k-1)=2(r-h)$,
since distinct clusters' cliques intersect in at most one vertex.
Its surplus is at least $r-2h>r/4$. Therefore
$Q'_j=Q_j\setminus B$ are pairwise disjoint and have orders

$$
|Q'_j|\ge r-5h+1\ge3r/4.
$$


The number of edges between $Q'_j$ and the other reduced anchors
is at most

$$
\begin{aligned}
e_H(Q_j,V(H)\setminus Q_j)
&=(r-t_j)(t_j+1)+\sum_{v\in Q_j}s(v)\\
&\le2rh. \tag{5}
\end{aligned}
$$

Choose independent uniform representatives of the reduced anchors.
For each cross edge, the event of selecting both its endpoints has
probability at most $16/(9r^2)$. Events involving disjoint pairs
of parts are jointly independent. By (5), a dependency graph has
maximum degree at most $4rh-1$.

We use the elementary symmetric local lemma in the form
$e p D\le1$ for event probabilities at most $p$ and dependency
degree at most $D-1$. One proof sets $x=1/D$ and uses
$(1-1/D)^{D-1}\ge e^{-1}$; induction on conditioning sets gives
conditional probabilities at most $x$ and hence positive
probability of avoiding every event. Here $D=4rh>1$ and

$$
e\,\frac{16}{9r^2}\,(4rh)
<\frac{192h}{9r}\le\frac89<1.
$$

Thus there is an independent transversal, so $q\le a$.
Consequently $q=a$.

### Accounting for vertices outside the maximum anchors

The cluster-deficit argument can now be written at this exact
order. At a covered vertex $v$, choose a cluster of a maximum
clique through $v$. Its anchor deficit is at most $r-c_H(v)$;
each other cluster through $v$ contributes at most $k$.
Summing, and using
$|U|=\sum_j b_j+L+1$, gives

$$
\mathcal D\ge
rT+\sum_j b_j(k+1-t_j)+L+k+1.
$$

Together with $\mathcal D\le r^2-2r+1-2/a$, this implies

$$
T\le r-3,\qquad T-a\le h-3. \tag{6}
$$


If $x\in C_j\setminus Q_j$, maximality of $Q_j$ supplies a
nonneighbor $z\in Q_j$. Some clique in this cluster contains
$x$ and intersects $Q_j$ in at least $|Q_j|-k\ge r-2k$
vertices. These are common neighbors of $x,z$, so (3) gives

$$
s(x)+s(z)\ge r-2h+1>r/2.
$$

Hence every cluster larger than its anchor meets $B$.

For a covered vertex contained in $q_v$ clusters, selecting one
clique through it from each cluster gives
$d_H(v)\ge q_v(r-h)$. Thus the total number of incidences
between $B$ and clusters is at most

$$
|B|+\frac{S+h|B|}{r-h}
\le4h+\frac{rh+4h^2}{r-h}\le6h.
$$

Let $E=\sum_j(|C_j|-|Q_j|)$. Only these at most $6h$ clusters
contribute to $E$, and each contributes at most $t_j$.
Since all $t_j\ge1$, (6) yields

$$
E\le6h+(T-a)\le7h-3.
$$

Therefore

$$
|U|=T-E+L+1\ge a-E+1\ge r-8h+4.
$$

Substitute this into $k|U|\le\mathcal D-n$ and use (1):

$$
(h-1)(r-8h+4)\le r(h-2)-2/a.
$$

This rearranges to
$r\le8h^2-12h+4-2/a<8h^2$, contradicting the assumption.
This proves (4).

The theorem does not exclude the remaining intermediate range
between the hereditary small-independence bound and (4).

## 2. Degree-r vertices form a Gallai forest

For every nonempty $W\subseteq V(H)$ and every nonempty independent
$I\subseteq W$, expansion (2) implies

$$
\boxed{\sum_{v\in I}\bigl(d_{H[W]}(v)-s(v)\bigr)
\le |W|-1.} \tag{7}
$$

Indeed, the number of repeated incidences in the neighborhoods of
$I$ is

$$
\sum_{v\in I}d_H(v)-|N_H(I)|
\le\sum_{v\in I}s(v)+|I|-1.
$$

Restricting the incidences to $W$ cannot increase that repetition
count. Now use $|N_{H[W]}(I)|\le |W|-|I|$ to obtain (7).

Let $L_0=\{v:d_H(v)=r\}$. For every component $J$ of $H[L_0]$,
(7) gives

$$
\operatorname{mic}(J):=
\max_{I\text{ independent in }J}\sum_{v\in I}d_J(v)
\le |J|-1.
$$

Theorem 6.4 of Kierstead--Rabern,
[*Extracting list colorings from large independent sets*,
printed p. 12](https://landon.github.io/graphdata/Papers/KernelMagic3.pdf),
characterizes this equality case: a connected graph has
$\operatorname{mic}(J)=|J|-1$ exactly when all its blocks are
cliques or odd cycles; otherwise $\operatorname{mic}(J)\ge|J|$.
The theorem statement and proof were checked in the primary paper.
Consequently $H[L_0]$ is a Gallai forest.

This deduction uses minimal-ratio expansion, not chromatic
criticality or even independence-critical pruning. It does not
establish that all of $H$ is a chromatic-critical graph.

## 3. A maximal-low-clique configuration is impossible

**Proposition.** There cannot be $a$ pairwise disjoint maximal
cliques $P_1,\ldots,P_a$ of $H$, all of whose vertices have
degree $r$, such that

$$
|P_i|=r-d_i,\quad d_i\ge1,\quad
D:=\sum_i d_i\le r-1. \tag{8}
$$


We first need a transversal fact. If pairwise disjoint clique
blocks of a Gallai forest have nonempty lists, at most one of
which is a singleton, the lists admit an independent transversal.
In each connected component, root the minimal block-cut subtree
connecting the specified block nodes at the singleton row, if
there is one, and otherwise at any row. A leaf row other than the
root connects toward the remaining rows through one cutvertex.
Choose a listed vertex different from that cutvertex; this is
possible because its list has size at least two. It has no
neighbor in any remaining row. Remove the row from consideration
and repeat; choose the root representative last.

It would be incorrect to claim that contracting the row cliques
always gives a forest. An additional triangle block can join three
rows through three different port vertices. The block-cut argument,
not a contraction assertion, is what proves the transversal fact.

Now put $E=D-a\ge0$ and
$B=V(H)\setminus\bigcup_iP_i$, so $|B|=a+E+1$.
Since $d_i\le r-a$, every $P_i$ has at least $a\ge4$
vertices. Section 2 and maximality make each $P_i$ a clique
block of $H[L_0]$.

For any $x\in B$, its nonneighbor lists in the rows are nonempty,
by maximality, and have no independent transversal, by $\alpha(H)=a$.
The transversal fact forces at least two singleton lists. Since
any two deficits sum to at most $E+2$, this gives

$$
e_H\!\left(B,\bigcup_iP_i\right)
\ge(a+E+1)(2r-E-4). \tag{9}
$$

On the other hand every vertex of row $i$ has exactly $d_i+1$
neighbors outside its row. Interrow edges only weaken the bound

$$
\begin{aligned}
e_H\!\left(B,\bigcup_iP_i\right)
&\le\sum_i(r-d_i)(d_i+1)\\
&\le r(2a+E)-2a-4E, \tag{10}
\end{aligned}
$$

where the last step uses $d_i^2\ge3d_i-2$.
The lower bound (9) minus the upper bound (10) is

$$
(E+2)(r-a)-E(E+1)-4.
$$

For $E=0,1$ this is positive because $r-a\ge3$.
For $E\ge2$, (8) gives $r-a\ge E+1$, so it is at least
$2E-2>0$. This proves the proposition.

## 4. High-degree vertices and critical-edge witnesses

Let $X=\{v:d_H(v)>r\}$ and $L=V(H)\setminus X$. Every maximum
independent set $I$ satisfies

$$
\sum_{v\in I}s(v)\ge2. \tag{11}
$$

To see this, take its private cliques. Each has order at most
$r-1$, so at least $a+1$ vertices lie outside their union.
These exceptional vertices have at least two neighbors in $I$.
Counting edges incident with $I$ gives

$$
\sum_{v\in I}d_H(v)\ge |H|-a+(a+1)=ar+2.
$$

Thus $\alpha(H[L])\le a-1$. Since $H[L]$ is a $K_r$-free
Gallai forest and $r\ge12$, it is $(r-1)$-colorable. Therefore

$$
\boxed{|X|\ge ar+1-(r-1)(a-1)=r+a.} \tag{12}
$$

This is stronger than the bound $a+1$ obtained without (11), but
does not contradict the surplus allowance $\sum_v s(v)\le r(r-a)$.

In fact $\sum_{v\in I}s(v)\ge3$ for every maximum independent
set here. Equality two would force all its private rows to have
order $r-1$, exactly $a+1$ exceptions, and exactly two anchor
neighbors per exception. The two-support product inequality gives
each exception an owner row in which it misses at most two vertices.
Two exceptions share an owner, producing an $(r+1)$-set with at
most five nonedges, contrary to the cap for $r\ge7$.

More generally, every maximal independent set $J$ in $H[X]$ satisfies

$$
\sum_{v\in J}(s(v)+2)\ge a+1. \tag{13}
$$

Indeed, $J$ dominates $X$, and the low vertices outside $N(J)$
have independence at most $a-|J|$ and are $(r-1)$-colorable.
Consequently

$$
|N(J)\cap L|\ge a+1-|X|+(r-1)|J|.
$$

On the other hand this quantity is at most
$r|J|+\sum_Js-(|X|-|J|)$, proving (13).

If the optional independence-critical pruning is performed, two
additional elementary restrictions hold. First, for adjacent $u,v$,

$$
N[u]\subseteq N[v]\quad\Longrightarrow\quad N[u]=N[v]. \tag{14}
$$

Otherwise take $x\in N(v)\setminus N[u]$. A critical-edge witness
for $vx$ is an independent $(a+1)$-set in $H-vx$ containing
$v,x$. Replacing $v$ by $u$ makes it independent in $H$, a
contradiction. In particular, if an exception $x$ is complete to
a private row $P_i$ and has another anchor neighbor, some other
exception supported on $i$ must be nonadjacent to $x$. Otherwise
$N[q_i]\subsetneq N[x]$.

Second, every critical edge $uv$ lies in a clique
$V(H)\setminus N[S]$ for an independent $(a-1)$-set $S$.
Take $S$ from a critical-edge witness by omitting $u,v$; two
nonadjacent vertices outside $N[S]$ would augment it. In this
core that clique has order at most $r-1$.

In any independence-critical graph with independence strictly less than $r$
and the outside-neighbor cap for full $K_r$'s, a full $K_r$ is
an isolated component. Deleting it lowers independence by exactly
one: an independent set of the original maximum size outside it
could be extended. Any cross edge is consequently noncritical,
since after its deletion an independent set still uses at most
one clique vertex and at most $\alpha-1$ outside vertices.
The assertion at independence exactly $r$ is not established by
this argument; the extension lemma stops at that boundary.

Under the same outside-neighbor cap, there is a precise componentwise
version from Section 7.3 of the
[second independent input](independent/clique_residue_and_affine_repair.md).
If an independence-critical edge $bx$ leaves $B=K_r$ within
a connected component $C$, take its independent witness of size
$\alpha(C)+1$ after deletion. It contains $b,x$. Every
$b'\in B\setminus\{b\}$ must meet the witness minus $b$:
otherwise replacing $b$ by $b'$ gives the same larger independent
set in the original graph. The vertex $x$ already uses its
unique neighbor $b$ in $B$. Each of the other $\alpha(C)-1$
witness vertices covers at most one $b'$, so $\alpha(C)\ge r$.
Thus in a **disconnected** independence-critical graph with total
independence at most $r$ and this cap, every $K_r$ is a whole component.
This still says nothing about the connected boundary case
$\alpha(C)=r$, nor about simultaneous components in every color.

No chromatic-criticality conclusion follows from these facts.

## What the attempted completion still lacks

No argument forces the configuration (8). In particular, high-degree
vertices inside candidate rows cannot simply be moved into the
outside set: such a vertex may be complete to the remaining low
part of its own row, giving an empty nonneighbor list. Both the
nonempty-list assertion and the exact external-degree budget in
(10) would then be lost.

Extracting a smaller chromatic-critical subgraph also does not
repair this gap: no sufficiently large order for that subgraph
has been established. Chromatic-critical density must not be
applied to all of an independence-critical core.

The later [chromatic-support bridge](chromatic_support_bridge.md)
does control independence in an induced vertex-critical support:
with $h=r-a$, it is at most $h+1$. This support need not be overloaded,
so that new bound does not justify applying the existing span theorem.

The weighted-inequality approach was not completed either.
For a common probability vector $x$, summing the quadratic
inequalities over all colors cancels their edge matrices exactly.
Writing $c_i(v)$ for local clique orders, it leaves only

$$
\sum_v\left(r-1+\sum_i c_i(v)\right)x_v^2\ge1.
$$

Optimizing this expression gives precisely the already recorded
harmonic bound. Distinct vectors in distinct colors destroy this
edge cancellation. No quantitative strictness estimate sufficient
for a contradiction was proved.

The arguments on this page received targeted checks of the stated
hypotheses, the local-lemma event count, and the surplus and
block-cut calculations. No computational certificate is used.

## Ore compositions cannot supply a small critical support

There is a precise structural exclusion beyond the scalar
chromatic-critical density bound. A $k$-Ore graph is obtained from
$K_k$ by repeated Ore compositions: delete an edge $xy$ of an
edge-side graph, split a vertex of a disjoint split-side graph into
two nonadjacent vertices with nonempty neighborhoods partitioning
its former neighborhood, and identify them with $x,y$.

**Proved.** Every $(r+1)$-Ore graph satisfying the cap
$e(W)\le\binom r2+1$ on its $(r+1)$-vertex sets has at least
$r^2+1$ vertices.

Follow edge-sides recursively through an Ore decomposition until
the initial $K_{r+1}$ is reached. This expresses the final graph
as successive compositions with the current graph always on the
edge-side. The original $r+1$ vertices survive. Each composition
removes at most one edge between them, adds no edge between
them, and adds at least $r$ vertices. Their induced graph must
miss at least $r-1$ of its original edges by the cap. Hence at
least $r-1$ compositions occurred, giving

$$
|G|\ge(r+1)+r(r-1)=r^2+1.
$$


Consequently any $(r+1)$-critical subgraph of an $ar+1$ core
with $a<r$ is non-Ore. This does not classify such critical
subgraphs or give the order lower bound needed for arbitrary
ones. In particular, the supplied Kostochka--Yancey density
theorem cannot be reversed to infer that a sparse critical graph
is Ore; its supplied equality examples are not an equality
classification.

### Even small Ore completions are excluded

There is a stronger two-level statement. Suppose $G$ satisfies
the inherited caps on $(r+1)$- and $(r+2)$-sets, and adding at
most $h\le r-2$ edges produces an $(r+1)$-Ore subgraph $O$.
Then

$$
\boxed{|O|\ge r+1+r(r-1-h)(r-2)\ge r^2-r+1.} \tag{15}
$$


An Ore graph has a useful root representation. Start with an
original $K_{r+1}$; some root edges remain intact, and each other
root edge is replaced by a split Ore graph attached at its two
endpoints. Branch interiors are disjoint, and branch edge sets
are disjoint from one another and from intact root edges. To
prove this by induction, a subsequent composition at an intact
root edge creates a new branch. A composition inside a branch
lifts to the corresponding edge of its unsplit Ore graph and
enlarges that graph by an Ore composition. Preserve the original
split, assigning any new edges at a split endpoint to the copy
where the replaced edge lay. Both copies keep positive degree:
if the last edge at a copy was replaced, the new composition
supplies an incident edge there. This proves the representation.

Every Ore graph has order $rt+1$ with $t\ge1$. If its root
has $\ell$ branches, each contributes at least $r$ internal
vertices, so $t\ge\ell+1$.

Let $F=E(O)\setminus E(G)$, so $|F|\le h$. Consider an
outer branch that is obtained by splitting a vertex $z$ of an
Ore graph $C$, where $|C|=rt+1$. Let $h_C$ count the edges
of $F$ in this branch, and choose a root of $C$ having
$\ell_C$ replaced edges. Its original root spans
$\binom{r+1}{2}-\ell_C$ edges before splitting. If $z$ is
outside the root, the cap on its $r+1$ vertices gives
$\ell_C+h_C\ge r-1$. If $z$ is in the root, take both
copies after splitting: its $r+2$ vertices still span that
many root edges before deletion. The cap
$D_r(r+2)=\binom r2+3$ gives $\ell_C+h_C\ge r-3$.
In either case,

$$
t\ge\max\{1,r-2-h_C\}.
$$


For the outer root, let $\ell$ be its number of branches,
$h_0$ the number of deleted intact root edges, and $h_j$ the
number in branch $j$. Then

$$
\ell+h_0\ge r-1,\qquad h_0+\sum_jh_j\le h,
\qquad |O|=r+1+r\sum_jt_j.
$$

Therefore, for $r\ge3$,

$$
\begin{aligned}
\sum_jt_j
&\ge\ell(r-2)-\sum_jh_j\\
&\ge(r-1-h_0)(r-2)-h+h_0\\
&\ge(r-1-h)(r-2).
\end{aligned}
$$

This proves (15). All caps apply because $O-F$ is a subgraph
of $G$; it need not be induced.

Since the least-budget core has at most $r^2-3r+1$ vertices,
even adding $r-2$ edges anywhere in it cannot produce an Ore
subgraph. No theorem has been proved forcing a non-Ore critical
subgraph to admit such a completion; that remains a substantive
gap rather than a consequence of its edge budget.

## A failed degree-balancing bridge

Independence-criticality does not guarantee a maximum independent set
$I$ with $\sum_I d\le a\overline d$: the
[explicit counterfamily](light_independent_set_obstruction.md) disproves
that assertion even for connected graphs of independence number four.
This does not disprove its specialization to the full core hypotheses.

Here is the exact bookkeeping that motivated the attempted bridge.
Choose a degree-sum-minimal maximum independent set $I=\{q_i\}$,
write $\sigma=\sum_i s(q_i)$, and let its private cliques have orders
$r-d_i$. Put

$$
E=\sum_i(d_i-1),\quad b=|B|,\quad
u=\sum_{x\in B}(|N(x)\cap I|-2).
$$

Vertex and anchor-degree counting give

$$
b=a+E+1,\qquad
|\{x\in B:q_i\in N(x)\}|=d_i+1+s(q_i),\qquad
\boxed{\sigma=E+u+2.}
$$

Also $s(v)\ge s(q_i)$ on each private row, by the choice of $I$.
Thus the least-color surplus budget gives the proved inequality

$$
\sum_i\sum_{v\in P_i}(s(v)-s(q_i))+\sum_{x\in B}s(x)
\le r(r-a-\sigma)+\sum_i d_i s(q_i).
$$

If the unproved core-specific bound $\sigma<r-a$ held, it would
imply $E+u\le r-a-3$ and a support complexity
$b+u=a+\sigma-1\le r-2$. No such light-set bound or subsequent
exclusion is asserted here.


## Original-degree greedy selection reaches a maximum independent set

In the least-budget core, repeatedly choose a vertex of minimum
**original** degree among the remaining vertices, and delete its closed
neighborhood in the remaining graph. Let the selected set have size $k$
and the removed blocks be $C_1,\ldots,C_k$. Each vertex of $C_i$ has
original degree at least the chosen vertex's original degree, itself
at least $|C_i|-1$. Thus

$$
2e(H)+n\ge\sum_i|C_i|^2\ge n^2/k.
$$

But the core budget gives

$$
n^2-(a-1)(2e(H)+n)
\ge r^2+(a+1)r+2-a>0.
$$

Therefore $k\ge a$, and of course $k\le\alpha(H)=a$.
In particular every independent set consisting of global
minimum-degree vertices extends to a maximum independent set: choose
its members first using the allowed ties.

This does not bound the unweighted degree sum of that maximum set.
The block sizes weight the low-degree choices unevenly, and the last
selected vertex may have high original degree. No light-maximum-set
conclusion is asserted.


## Deleting a degree-$r$ closed neighborhood

If $d_H(v)=r$, put $R=H-N[v]$ and $b=a-1$. Then

$$
|R|=br,\qquad \alpha(R)=b,\qquad \delta(R)\ge r-1,
\qquad e(R)\le b\binom r2+\binom{r-1}{2}. \tag{24}
$$

The upper independence bound follows by adjoining $v$; minimal-ratio
minimality gives equality. For $w\in R$, pair expansion gives
$|N(v)\cap N(w)|\le s(w)+1$, so
$d_R(w)\ge d_H(w)-s(w)-1=r-1$.

Since $e(H[N[v]])\le\binom r2+1$, minimum degree in $H$ shows
that deleting $N[v]$ removes at least

$$
r(r+1)-\left(\binom r2+1\right)
=\frac{r(r+3)}2-1
$$

edges. Subtraction from the core budget gives (24). Finally, deleting
any at most $r-1$ vertices from $R$ leaves more than $r(b-1)$
vertices, so the original induced-set minimality preserves independence
$b$ there.

This residual is balanced, not overloaded. No theorem has been proved
forcing its $K_r$-resolution or otherwise excluding it in the full
surviving parameter range.

## Sharper neighborhood charges and the bound a at most r minus five

**Proved for $r\ge12$.** The least-budget core satisfies

$$
\boxed{a\le r-5.} \tag{25}
$$

This strengthens the earlier $a\le r-3$; it does not replace the
square-root gap or exclude the remaining core range.

### A matching charge in a closed neighborhood

Let $d_H(v)=r$, $A=N_H[v]$, and $F=\overline{H[A]}$. Write
$M=e(F)$, $T=\sum_{x\in A}s(x)$, and let $F$ have a matching of
size $m$. Then

$$
T+M\ge m(r-m). \tag{26}
$$

For a matched pair $xy$, pair expansion and the common neighbors
inside $A$ give

$$
s(x)+s(y)\ge r-d_F(x)-d_F(y)+c_F(x,y).
$$

If $U$ consists of the $2m$ matching endpoints, then
$\sum_{x\in U}d_F(x)\le M+e_F(U)$. Also

$$
e_F(U)-\sum_{xy\text{ matched}}c_F(x,y)\le m^2.
$$

To check the latter, the matched edges contribute $m$. Between two
matched pairs, the four possible cross edges minus their contributions
to the two common-neighbor counts contribute at most two: with
$0,1,2,3,4$ cross edges the maximum is respectively $0,1,2,1,0$.
Common neighbors outside $U$ only decrease the expression. Summing
proves (26).

The inherited cap gives $M\ge r-1$. Moreover $F$ has a matching of
size at least two. Otherwise its edges form a star or a triangle.
A star leaves a $K_r$ in $H[A]$, while a triangle has fewer than
$r-1$ edges. Deleting $A$ removes exactly
$\binom r2+r+T+M$ edges. Thus, with $R=H-A$ and $b=a-1$,

$$
e(R)\le b\binom r2+\binom r2-m(r-m)
\le b\binom r2+\binom r2-2r+4. \tag{27}
$$

The localized independence bound, using $|R|=br$, $\alpha(R)=b$,
and $\omega(R)\le r-1$, gives $e(R)\ge br^2/2$. Hence

$$
r-a\ge2m(1-m/r).
$$

Taking a matching of size two forces $r-a\ge4$.

### Balanced low-degree deletion

Any induced balanced residual $Q$ of order $br$ and independence
$b$ inherits $|W|\le r\alpha(Q[W])$, and therefore
$|N_Q[I]|\ge r|I|$ for every independent $I$. If $d_Q(u)=r-1$,
deleting $N_Q[u]$ leaves order $(b-1)r$, independence $b-1$, and
minimum degree at least $r-1$ when that minimum bound held in $Q$.
Indeed, for $w$ outside the neighborhood, pair expansion gives
$|N(u)\cap N(w)|\le d_Q(w)+1-r$.

There is also a strengthened edge cost. On $N_Q[u]$, use deficits
$s'(x)=d_Q(x)-(r-1)$ and its complementary graph $F$. This graph
has at least one edge because $Q$ is $K_r$-free. The same matching
calculation, now with $|N_Q[u]|=r$ and the non-strict expansion,
gives $\sum s'(x)+e(F)\ge r-1$ using one matching edge. Thus this
deletion removes at least

$$
\binom r2+r-1 \tag{28}
$$

edges. The residual remains balanced, not overloaded.

Two nonadjacent vertices of degree $r-1$ in a balanced graph have
disjoint closed neighborhoods, directly from pair expansion. Thus
this degree layer induces disjoint cliques, and no outside vertex
meets two of those cliques.

### All-low maximum independent sets force surplus

Suppose a balanced $K_r$-free graph $Q$ has $|Q|=br$,
$\alpha(Q)=b$, $\delta(Q)\ge r$, and a maximum independent set
of degree-$r$ vertices. Put $S_Q=\sum_x(d_Q(x)-r)$. Then

$$
2S_Q\ge b(r-6). \tag{29}
$$

For the private cliques of this independent set write $|P_i|=r-d_i$.
Here $d_i\ge1$, and the number of exceptions is $D=\sum d_i$.
Anchor-degree counting gives $\sum_x k_x=D+b$, while $k_x\ge2$.
Thus $D\le b$, forcing $D=b$, all $d_i=1$, and all exceptions
exactly two-supported. Each row has exactly two incident exceptions.

For an exception $x$, its two nonneighbor lists in its supporting
rows are nonempty (otherwise it creates $K_r$) and completely joined
by the independent-set augmentation argument. Let their sizes be
$p,q$. The exception and these two lists have total degree surplus
at least

$$
(r-2-p-q)_++p(q-2)_++q(p-2)_+\ge r-6.
$$

For positive integers $p,q$, the last two terms are at least
$p+q-4$, which proves the inequality. Each private vertex is charged
at most twice, because its row has exactly two incident exceptions;
each exception is charged once. Summing proves (29). In particular,
an $r$-regular balanced $K_r$-free graph of this kind is impossible
for $r\ge7$.

### Excluding the last two constant gaps

Write $h=r-a$. If $h=3$ or $4$, the budget $\sum s\le rh<|H|$
forces a degree-$r$ vertex. Equation (27) already excludes $h=3$.
If $h=4$, it gives

$$
b=r-5,\qquad 2e(R)\le br^2+8.
$$

A degree-$(r-1)$ vertex in $R$, by (28) and the localized lower bound
on its balanced residual, would give $2e(R)\ge br^2+r-2$, impossible
for $r\ge12$. Hence $\delta(R)\ge r$ and $S_R\le8$.
Deleting these at most eight higher-degree vertices preserves
independence, since deletion of at most $r-1$ vertices does so in
$R$. An all-degree-$r$ maximum independent set therefore exists.
Equation (29) gives $16\ge(r-5)(r-6)$, again impossible. This proves
(25). The matching and surplus charges received a separate check.

## No 1-join in a minimal-ratio core

This uses neither the budget nor claw-freeness. A 1-join partitions
vertices into $A_1,B_1,A_2,B_2$, with two nonempty sides,
$A_1\cup A_2$ a clique, and all cross-side edges precisely the
$A_1$--$A_2$ edges. Put

$$
\alpha_i=\alpha(H[A_i\cup B_i]),\qquad
\beta_i=\alpha(H[B_i])\in\{\alpha_i-1,\alpha_i\}.
$$

If either $\beta_i=\alpha_i$, then $\alpha(H)=\alpha_1+\alpha_2$,
and proper-subset minimality on both sides contradicts
$|H|=r\alpha(H)+1$. Otherwise
$\alpha(H)=\alpha_1+\alpha_2-1$ and

$$
|B_1|+|B_2|\le r(\alpha(H)-1),\qquad
|A_1\cup A_2|\le r-1,
$$

again a contradiction. This removes one structural decomposition,
not all non-line-graph possibilities.

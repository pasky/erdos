---
name: research/erdos_617/local_cap_obstruction
desc: Complementary counterfamilies showing why both the full hereditary caps and the least-color budget matter.
tags: [graph-theory, obstruction]
sources: []
created: 2026-09-21T23:52:12Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/local_cap_obstruction

***

**Proved.** Independence number, the least-color edge budget, and the cap on
$(r+1)$-sets alone do not imply Problem 617. This is an obstruction to a
proposed proof, **not** a counterexample to the problem.

The later [growing-independence barrier](growing_independence_barrier.md)
additionally combines criticality, proper-induced minimality, all smaller
capacity statements, and two-support with fewer than $r$ exceptions.
Its failure of a three-bag hereditary cap is explicit. It does not
contradict the full-cap core reductions.

Let $t\ge3$ be odd and $r=(5t-1)/2$. Replace every vertex of a five-cycle
by a clique of size $t$, and join successive cliques completely. Call the
result $H=C_5[K_t]$. Put

$$
G=(r-2)K_r\ \dot\cup\ H.
$$

Then

$$
|G|=r^2+1,\qquad \alpha(G)=r,\qquad
\omega(H)=2t<r,
$$

and $e(H)=(15t^2-5t)/2$. Direct substitution gives

$$
\frac{r(r^2+1)}2-e(G)=\frac{5(3t-1)(t-1)}8>0.
$$


## Every local cap holds

The complement of $H$, after cyclic relabeling, is the independent-set
blow-up of $C_5$. For $0\le y_i\le1$, with indices modulo five,

$$
\sum_i y_i y_{i+1}\ge\sum_i y_i-2.
$$

Indeed, the difference is affine in each coordinate separately, so its
minimum on the cube is attained at a cube vertex. There it asserts
$e(C_5[S])\ge|S|-2$, which follows from $\alpha(C_5)=2$ by deleting
one endpoint per edge.

Thus a set of $m$ vertices in $H$, with bag occupancies $x_i\le t$,
has at least

$$
\sum_i x_i x_{i+1}\ge t(m-2t)
$$

nonedges. At $m=r+1=(5t+1)/2$, this is

$$
\frac{t(t+1)}2\ge r-1,
$$

because the difference is $(t-1)(t-3)/2\ge0$.
An $(r+1)$-set meeting two or more components of $G$ has at least $r$
cross-component nonedges: for positive component occupancies summing to
$r+1$, their number is minimized by occupancies $r,1$.
No $(r+1)$-set lies in one of the $K_r$ components. Therefore every such
set spans at most $\binom r2+1$ edges.

## Why it is not a coloring counterexample

The [full inherited cap](reductions.md) on $V(H)$ requires

$$
e(H)\le D_r(2r+1)=r^2+2.
$$

Instead

$$
e(H)-(r^2+2)=\frac{5t^2-9}{4}>0.
$$

Hence its complement cannot be partitioned into $r-1$ color graphs each
having independence number at most $r$.

## The scalar packing barrier

In the minimum-degree row $d=r-1$ of the usual packing reduction, a
residual of independence cap $a$ has $ar+1$ vertices and edge budget

$$
E_r(a)=a\binom r2+\frac{r(r+1)}2.
$$

For $1\le a\le r-1$, direct evaluation gives

$$
D_r(ar+1)=\frac{ar^2+a^2r-2ar+2a}{2},
$$

and consequently

$$
2(D_r(ar+1)-E_r(a))=r(a^2-a-r-1)+2a.
$$

Whenever this is nonpositive, any realizable residual automatically has
at most the outer budget. A lower-bound contradiction in this range is
therefore an **emptiness theorem**, not an ordinary edge-count improvement.
The range grows approximately as $a\le\sqrt r$.
This does not prove that the packing framework cannot work; it identifies
the unbounded structural input a uniform version needs.

## A different obstruction: local deficit-one suppression

**Proved; not an overloaded core.** For every $r\ge5$, the clique
blow-up

$$
H=C_5[2,2,r-3,1,r-3]
$$

has order $2r-1$, independence number two, clique number $r-1$, and
satisfies **every** inherited cap $e(H[W])\le D_r(|W|)$.
Nevertheless, a deficit-one private row with exactly two supported
exceptions cannot necessarily be suppressed by deleting the row and
one exception with an independence drop.

Choose anchors in bags 1 and 3. Their private cliques are bags $1\cup5$
of order $r-1$ and bags $3\cup4$ of order $r-2$. The two vertices
of bag 2 are exactly the exceptions, both supported on both anchors.
Deleting the first private row and either exception leaves the other
exception nonadjacent to the vertex in bag 4. Independence remains two.
No anchor pivot can reveal a $K_r$, since the graph contains none.

Here is a verification of all inherited caps. Put $L=r-3\ge2$.
The complement is an independent-bag $C_5$ with cyclic capacities
$(2,L,L,2,1)$. For occupancies $(u,x,y,w,z)$ in those ranges,
its edge count is

$$
ux+xy+yw+wz+zu.
$$

Since the graph has fewer than $2r$ vertices, the only nontrivial cap
requires this to be at least $(r-1)(u+x+y+w+z-r)$.
Let $\Psi$ denote the difference. It is affine in each of $x,y$
separately, so it suffices to check $x,y\in\{0,L\}$, retaining all
allowed $u,w,z$.

At $(0,0)$ the total occupancy is at most $5\le r$, so $\Psi\ge0$.
At $(L,0)$,

$$
\Psi=3(L+2)-2u-(L+2)w+z(u+w-L-2).
$$

Its coefficients of $u,w$ are nonpositive. Setting $u=w=2$ minimizes
it and gives $(L-2)(1-z)\ge0$. The corner $(0,L)$ is symmetric.
At $(L,L)$,

$$
\Psi=L+6-2(u+w)+z(u+w-L-2),
$$

again minimized at $u=w=2$, with the same nonnegative value.
This proves the cap for every occupancy.

The example has order $2r-1$, not $2r+1$. It rules out a purely local
suppression inference, not the globally overloaded two-support core.

## All hereditary caps without the least-color budget

**Proved for every prime power $r\ge3$.** The construction in Appendix C of the
[independent input](independent/small_independence_and_packing_obstructions.md)
has $r^2+1$ vertices, independence and clique numbers both $r$, and satisfies
every hereditary upper cap, but exceeds the least-color edge budget. This
complements, rather than contradicts, the first counterfamily on this page. The
input states the construction for primes; its finite-field proof works unchanged
for prime powers.

On an $r\times r$ grid make every row a clique and every column
except a distinguished column $C$ a clique. Add a vertex $v$
adjacent precisely to the $r$ points of $C$, which is independent.
Call the resulting graph $G$. Without $v$, an independent set
has at most one point per row. With $v$, it avoids $C$ and has
at most one point in each of the other $r-1$ columns. Thus
$\alpha(G)=r$, attained by $C$. Every old clique lies in a row
or a nondistinguished column, and a clique through $v$ has order
at most two. Hence $\omega(G)=r$.

Let $R$ be the full rook graph on the grid. Identify its points
with $\mathbb F_r^2$. For each of the $r-1$ nonzero finite slopes,
take the union of the cliques on that direction's lines. These
graphs partition the complement of $R$ and each has independence
number at most $r$. Complementary Turán therefore gives

$$
e(R[W])\le D_r(|W|)
$$

for every old point set $W$.

Sets not containing $v$ induce subgraphs of $R$. If
$U=W\cup\{v\}$ and $h=|W\cap C|$, then

$$
e(G[U])=e(R[W])+h-\binom h2\le D_r(|W|)+1.
$$

For $t=qr+s\ge1$, $0\le s<r$, direct subtraction gives

$$
D_r(t+1)-D_r(t)=q+s\ge1.
$$

The singleton case $W=\varnothing$ is immediate. This proves
every hereditary cap, including sets containing $v$.

Finally,

$$
\begin{aligned}
e(G)&=(2r-1)\binom r2+r\\
&=\frac{r(r^2+1)}2+\frac{r(r-1)(r-2)}2
>\frac{r(r^2+1)}2.
\end{aligned}
$$

The rows are $r$ disjoint $K_r$'s, and this edge count attains the
target-color lower bound in [Packing tools](packing_tools.md).
It does not contradict that note's exclusion in an actual coloring:
the other-color nonpartite gaps, not the one-color hereditary caps
alone, finish the exclusion. The independent input's reference to
“the lower bound of Section 1” should refer instead to its
Section 4, equation (13).

This graph is not a line graph of a simple graph or a loopless multigraph: $v$
and any three points of $C$ induce a claw, whereas three mutually disjoint edges
cannot all meet a fourth edge. Thus it also does not conflict with
[Line-graph restrictions](line_graph_obstruction.md). No extension to all
integer orders $r$ is claimed here.

## Unsaturated private rows can have minimum degree r

This is another obstruction to a weaker completion lemma, **not** to
the normalized overloaded core. For a fixed $a\ge3$, take the rook
graph on an $a\times(r-1)$ rectangle, with $r>2a+1$ and
$r\ge a(a-1)$. Choose diagonal anchors $(i,i)$, $1\le i\le a$.
The private row at $i$ consists of its anchor and the cells in row
$i$ whose columns lie outside $[a]$. It has order $r-a$, hence
deficit $a$. The $a(a-1)$ off-diagonal cells in the first $a$ columns
are the two-supported exceptions.

Each exception is complete to its row-owner private clique and sees
only the opposite anchor in its other supporting row. Thus each row
has exactly $a-1$ strongly incident exceptions under the missing-count
threshold $a$, fewer than its deficit. Yet every vertex has degree
$r+a-3\ge r$, the graph is $K_r$-free, and its independence is $a$.
For prime-power $r$, it inherits every cap from the full $r\times r$
rook graph, whose cap verification is given above via the affine-plane
complement decomposition.

Here the order is $ar-a$, and exceptions minus total deficit equals
$-a$, rather than $+1$. It also lacks the normalized core's strict
private-set expansion. For $a=3$, two independent private cells in
different rows and different columns have degree $r$ and exactly two
common neighbors, giving $|N[I]|=2r$, not $2r+1$. Thus completion
cannot follow from private minimum degree and the caps alone; the
global overload and strict expansion remain essential hypotheses.

## The near-equal pentagon works for every r at least eleven

Section 7.1 of the
[second independent input](independent/clique_residue_and_affine_repair.md)
extends the first family on this page to every $r\ge11$. Take five nonempty bags
as equal as possible, totaling $2r+1$, and adjoin $r-2$ disjoint $K_r$'s. Put
$q=\lfloor(2r+1)/5\rfloor$, $c=\lceil(2r+1)/5\rceil$. The resulting graph has
order $r^2+1$, independence $r$, and minimum degree $r-1$, since the blow-up's
degrees lie between $3q-1\ge r-1$ and $3c-1$. Its clique number inside the
blow-up is at most $2c<r$.

The degree upper bound gives the minority budget whenever
$3r^2-31r-10\ge0$, which holds throughout the stated range.
The cube inequality proved earlier gives at least
$c(r+1-2c)$ nonedges in a local set inside the blow-up.
Writing $r=5h+j$, the difference of this expression from
$r-1$ is

$$
\begin{array}{c|ccccc}
j&0&1&2&3&4\\ \hline
&2h(h-3)&2h(h-2)&2h(h-1)&(2h+1)(h-2)&(2h+1)(h-1).
\end{array}
$$

Every entry is nonnegative in its applicable $r\ge11$ range.
Cross-component sets are handled as before. Criticality follows
from the witness argument in the next section, which applies to
any positive-bag pentagon blow-up.

This is not a new mechanism: it is the existing equal-bag
obstruction with all integer parameters covered. The complementary
maximum degree is at most $2c$, so its exceptional component
$J$ satisfies

$$
e(J)-D_r(2r+1)\ge(r^2-7r-15)/5>0.
$$

Thus the full cap fails already for every stated parameter, not
only in the large-parameter range of the independent coupled theorem.

## Local-only stability can lose a square-root number of full cliques

**Proved weak-hypothesis counterfamily.** Section 7.2 of the
[second independent input](independent/clique_residue_and_affine_repair.md)
strengthens the first obstruction on this page. Put

$$
r=2k^2,\quad k\ge4,\quad m=\lfloor k/2\rfloor,\quad
L=r-3k,\quad b=2k.
$$

Let $H$ be the cyclic clique blow-up $C_5[L,b,L,b,b]$, let
$H^+$ add one vertex to a large bag, and set

$$
G=(r-2m)K_r\ \dot\cup\ (m-1)H\ \dot\cup\ H^+.
$$

Then

$$
|G|=r^2+1,\quad \alpha(G)=r,\quad \delta(G)=r-1,
\quad e(G)\le r(r^2+1)/2,
$$

every $(r+1)$-set has at least $r-1$ nonedges, and every
edge is independence-critical. Yet $G$ has exactly $r-2m$
copies of $K_r$, all whole components. Thus the deficit is
$2m=\Theta(\sqrt r)$, not bounded.

The orders of $H,H^+$ are $2r,2r+1$, their independence
numbers are two, and their maximum clique orders are
$r-k,r-k+1<r$. Degrees in $H$ are $r+k-1$ or
$2r-4k-1$, both at least $r-1$; adding the extra vertex
does not decrease degrees. The intact cliques give equality
$\delta(G)=r-1$. Every edge in a positive-bag clique blow-up
of $C_5$ is independence-critical: for an internal bag edge,
its endpoints after deletion extend with a nonadjacent bag;
for a consecutive-bag edge on $i,i+1$, use bag $i+3$.
These witnesses extend over all the other components.

Direct expansion gives

$$
e(H)=r(r-1)+k^2(4k-5),\qquad e(H^+)=e(H)+r+k.
$$

Hence

$$
\frac{r(r^2+1)}2-e(G)
=2k^4-mk^2(4k-5)-k^2-k
\ge\tfrac52k^3-k^2-k>0.
$$


### Checking every local cap

For any graph $F$, a minimum of
$Q(x)=\sum_{ij\in E(F)}x_ix_j$ on
$0\le x_i\le c_i$, $\sum_i x_i=u$ has at most one coordinate
strictly between its bounds. Transfer mass between two interior
coordinates. With their sum fixed, $Q$ is linear when the
coordinates are nonadjacent and concave when adjacent. Moving
to an endpoint does not increase $Q$ and reduces the number of
interior coordinates; iterate. Integer capacities and total
give an integer minimizer as well.

The complement of $H^+$ is an independent-bag cycle with cyclic
capacities $(L+1,L,b,b,b)$. Take total occupancy $u=r+1$.
We show $Q\ge r$, stronger than required. At a minimizer with
at most one interior coordinate, use

$$
2L+1>u,\qquad u>3b,\qquad u-3b\ge b.
$$

The two large coordinates cannot both be full or both zero.

If neither is full, exactly one is positive and partial.
At least two small coordinates are full, and the large
occupancy is at least $u-3b\ge b$. If its small cycle neighbor
is full, their edge contributes at least $b^2$; otherwise
the other two small coordinates are full and adjacent,
again contributing $b^2>r$.

If one large coordinate is full, of size $C\in\{L,L+1\}$,
the remaining occupancy is $d=u-C\in\{3k,3k+1\}$.
If the other large coordinate is positive, it is partial,
and at most one small coordinate is full. Its size is
therefore at least $d-b\ge k$, giving contribution
$Lk=k^2(2k-3)\ge r$ on the large--large edge.
If the other large coordinate is zero, exactly one small
coordinate is full and another has size $d-b\ge k$.
An occupied small neighbor of the large coordinate contributes
at least $Lk\ge r$. If that neighbor is zero, the two occupied
small coordinates are adjacent and contribute at least $bk=r$.
This exhausts the minimizers.

The graph $H$ inherits this bound from $H^+$. Sets meeting
multiple components have at least $r$ cross-component nonedges,
as earlier on this page. Thus every local cap holds.

The full hereditary caps nevertheless fail explicitly:

$$
e(H)-D_r(2r)=k^2(4k-7)>0,\qquad
e(H^+)-D_r(2r+1)=k^2(4k-5)+k-2>0.
$$

The family therefore refutes bounded-defect stability from
the local cap, budget, minimum degree, and independence-criticality,
not from the full core hypotheses.

## Sharpness of the local perturbation exponent

The local-only $r^{4/3}$ perturbation bound in
[Affine edit obstruction](affine_edit_obstruction.md) has the correct
exponent. The second independent input supplies the following
checked example. Put $r=k^3$, $k\ge10$, and take cyclic clique
bags

$$
(A,B,C,D,E)=(r-k^2,\ 4k+1,\ r-k^2,\ k^2-2k,\ k^2-2k).
$$

Let $J$ be their blow-up and $G=J\dot\cup(r-2)K_r$.
Its order is $r^2+1$ and its independence number is $r$.
Choose a distinguished vertex $v$ in bag $B$, split $B-\{v\}$
into $B_1,B_2$ of size $2k$, and use old parts

$$
A\cup E\cup B_1,\qquad C\cup D\cup B_2
$$

together with the intact cliques. Each part has size $r$.
The crossing-edge and missing-within-part counts are respectively

$$
t=5k^4-8k^3+8k^2,\qquad 4k^3-8k^2,
$$

so the total old edit distance from disjoint complete parts is
$5k^4-4k^3=O(r^{4/3})$.

For a set of $r+1$ vertices in $J$, use lower-case bag
occupancies $a,b,c,d,e$. Its nonedge count is

$$
F=ac+ad+bd+be+ce.
$$

Since $b+d+e\le2k^2+1$, we have $a+c\ge r-2k^2$.
Reflect to assume $c\le a$. If $c\ge2$, then
$F\ge ac\ge2(a+c)-4\ge r-1$. If $c\le1$ but
$c+d\ge2$, then $F\ge2a\ge2(r-2k^2-1)\ge r-1$.
All these numerical comparisons hold for $k\ge10$.

The remaining cases are $(c,d)=(1,0),(0,1),(0,0)$.
In the first case $F=r+b(e-1)\ge r$, because the capacities
force $e\ge1$. In the second $F=r+e(b-1)\ge r$, because
they force $b\ge1$. In the last, $b+e\ge k^2+1$, so
$b\ge2k+1$, $e\ge k^2-4k$, and
$F=be\ge(2k+1)(k^2-4k)\ge r-1$. Cross-component sets
again have at least $r$ nonedges. This verifies every local cap.

The distinguished vertex can instead be chosen in an intact
$K_r$: insert the original $v$ into its vacated old part.
The crossing count increases by $2(r-k^2)+4k=O(r)$,
while the new distinguished vertex has degree $r-1$.
Thus bounding that individual degree does not improve the
local-only exponent.

This example violates the full cap on $J$ by

$$
e(J)-D_r(2r+1)=5k^4-11k^3+14k^2+4k-2>0.
$$

It does not contradict the stronger full-hereditary perturbation
bound, nor prove sharpness of any multicolor repair exponent.

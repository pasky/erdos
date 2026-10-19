---
name: research/erdos_617/parallel_unit_row_fold
title: Parallel unit-row folding and the remaining cap gap
desc: Exact fold slacks and normalized expansion bounds, a near-clique exclusion, and a checked local obstruction that fails the full normalized hypotheses.
problems: [617]
created: 2026-10-15T17:09:48Z
updated: 2026-10-15T17:09:48Z
---

# Parallel unit-row folding and the remaining cap gap

[[research/erdos_617/_index|..]]

[[research/erdos_617/parallel_unit_row_fold/evidence/_index|evidence/]]: Exact finite local obstruction and an all-subset dynamic-programming cap check.

***

These are author-recorded deductions and finite evidence by Plasma AI.
They refine the [unit-row folding argument](../saturated_row_suppression.md)
for [[problems/extremal_graph_theory/E0617/_index|Problem 617]]. Preservation
of every hereditary cap under the full normalized hypotheses is unresolved.
The local example below disproves a weaker implication; it is not a
normalized counterexample. No independent tier is asserted.

## Exact setting

Use the [minimum-anchor two-supported core](../two_support_normalization.md)
with $r\ge12$, $4\le a<r$, $|H|=ar+1$, $\alpha(H)=a$, independent anchors
$Q$, private clique rows $P_l$ of order $r-d_l$, and $b\le r$ exceptions
having exactly two anchor neighbors. The deficits satisfy
$\sum d_l=b-1$. Every induced subgraph obeys

$$
e_H(U)\le D_r(|U|),\qquad
D_r(rq+c)=\binom{rq+c}{2}-(r-1)\left(r\binom q2+qc\right),
\quad 0\le c<r.
$$

The core has the fewest anchors among induced cores of that type.
Every private vertex has degree at least $r$, every row has size at least
$a$, and $\omega(H)\le r-1$. These are the simultaneous hypotheses of the
linked reduction. A minimum exception degree, independence-criticality
and a least-color budget are not assumed.

Let $P=P_i$ have order $r-1$, with exactly two incident exceptions $x,y$,
both supported on $\{i,j\}$ and nonadjacent. Put
$Z=P\cup\{x,y\}$, $R=H-Z$, and $k=a-1$. Delete $P$ and replace $x,y$
by one vertex $z$ adjacent to their union neighborhood in $R$; call this
simple graph $F$.

Sections 10--11 of the linked folding argument give
$|F|=kr+1$, $\alpha(F)=k$, $|R|=kr$, $\alpha(R)=k$,
$e_H(Z)=D_r(r+1)$ and $d_H(v,Z)\le2$ for every outsider.
The holes of $x,y$ partition $P\setminus\{q_i\}$. They also give

$$
d_H(v,P)+\mathbf1_{\{vx,vy\in E(H)\}}=1\quad(v\in P_j),
\qquad d_H(v)\ge r+1\quad(v\in P_j),\qquad r\le4a-4.
$$

These supplied reductions retain their own standing; they are not an
independent verification here. The folded enlarged receiving row is a clique.

## Three lifts of a proposed violating set

For $T\subseteq R$, let $t=|T|$, $s=t+1$, and

$$
A=e_H(P,T),\quad C=|T\cap N_H(x)\cap N_H(y)|,\quad
\sigma_Z=D_r(t+r+1)-e_H(Z\cup T),\quad
\delta=e_F(T\cup\{z\})-D_r(s).
$$

Folding removes exactly $e_H(Z)+A+C$ edges from $Z\cup T$.
Since $D_r(s+r)-D_r(s)=\binom r2+s$,

$$
\delta=t-A-C-\sigma_Z. \tag{A}
$$

The slack $\sigma_Z$ is nonnegative. Receiving-row contributions to
$t-A-C$ vanish pointwise, but positive charge elsewhere is not by itself
a cap violation.

Let $X=T\cap(N_H(x)\setminus N_H(y))$ and
$Y=T\cap(N_H(y)\setminus N_H(x))$, and put
$\sigma_x=D_r(s)-e_H(T\cup\{x\})$, with $\sigma_y$ defined symmetrically.
The two ordinary lifts give

$$
\delta=|Y|-\sigma_x=|X|-\sigma_y. \tag{B}
$$

Thus both exclusive classes must have size at least $\delta$ for a violation.
The double lift has $e_H(T\cup\{x,y\})=e_F(T\cup\{z\})+C$, so, writing
$g_r(n)=D_r(n+1)-D_r(n)=\lfloor n/r\rfloor+(n\bmod r)$,

$$
\delta+C\le g_r(s),\qquad
D_r(s+1)-e_H(T\cup\{x,y\})=g_r(s)-\delta-C. \tag{C}
$$

If a violating set has minimum cardinality, deleting any vertex $v$ gives

$$
d_F(v,T\cup\{z\})\ge D_r(s)-D_r(s-1)+\delta. \tag{D}
$$

Sets without $z$ inherit their caps, and sets of size at most $r$ have the
complete-graph cap automatically. Equations (A)--(D) do not imply that a
violating set exists.

## Consequences of minimum-anchor normalization

Set $N_x=N_H(x)\cap R$ and $N_y=N_H(y)\cap R$. Then

$$
\alpha(R-N_x)=\alpha(R-N_y)=k,
\qquad \alpha(R-(N_x\cup N_y))\le k-1. \tag{E}
$$

Indeed, deleting $P\cup\{y\}$ leaves an induced graph of order $kr+1$
with the $k$ other anchors. If its independence number were $k$, it would
be a smaller induced core: $x$ has singleton support at $j$, other surviving
vertices keep one or two anchor neighbors, singleton classes are cliques by
augmentation, the exception set shrinks, and every cap is inherited.
Minimum-anchor choice excludes this. An independent $(k+1)$-set in that
graph must contain $x$, since $\alpha(R)=k$. Removing $x$ proves the first
equality; interchange $x,y$ for the second. Adjoining the independent pair
$x,y$ proves the final inequality.

For any nonempty independent $I\subseteq H$ whose union of original anchor
supports $S$ has size $|I|$, one has

$$
|N_H[I]|\ge r|I|+1. \tag{F}
$$

Here an anchor has its own singleton support. The independent set
$I\cup(Q-S)$ is maximum. Every vertex outside $N_H[I]$ has a retained
anchor neighbor, or it would augment that set. If $|I|<a$ and
$|N_H[I]|\le r|I|$, trim the residual to $(a-|I|)r+1$ vertices retaining
the anchors. Its independence number is $a-|I|$, its one/two-support
structure and exception bound survive, and it contradicts minimum-anchor
choice. If $|I|=a$, maximality gives $N_H[I]=V(H)$.
This is the tight-support expansion also used in
[unit-deficit propagation](../unit_deficit_propagation.md).

Apply (F) to $\{x,y\}$. It dominates $P$, and therefore

$$
d_F(z)=|N_x\cup N_y|\ge r. \tag{G}
$$

For an independent set $J$ of original private vertices retained in $R$,
let $\epsilon(J)$ be one if $J$ has a neighbor of $z$, and zero otherwise.
The independent set $\{q_i\}\cup J$ has tight support, and
$|N_H[\{q_i\}\cup J]|=r+1+|N_F[J]|-\epsilon(J)$. Hence

$$
|N_F[J]|\ge r|J|+\epsilon(J). \tag{H}
$$

If $\{z\}\cup J$ is independent in $F$, then $J$ avoids $P_j$ and the
lift $\{x,y\}\cup J$ has tight support. Its closed neighborhood has
exactly $r$ more vertices than $N_F[\{z\}\cup J]$, so

$$
|N_F[\{z\}\cup J]|\ge r(|J|+1)+1. \tag{I}
$$

In particular a retained private neighbor of $z$ has degree at least $r$
in $F$; other retained private vertices have degree at least $r-1$.
These statements do not grant minimum degree $r$ to all exceptions or
strengthen (H) by one when $\epsilon=0$.

## Near-clique restriction

[[theory/combinatorics/L238_normalized_core_near_clique_bound/_index|L238]]
proves that an $r$-set with $h\le a-2$ missing edges satisfies
$r\le a(h+1)$ and contains at most one original anchor. The pair capacity
it assumes is supplied by the same normalized core. Since $r\le4a-4$
here, every $r$-set has at least $\lceil r/a\rceil-1$ missing edges.

For the first nontrivial folded cap, $|T|=r$, write $u$ for its number
of union neighbors of $x,y$. Then

$$
\delta=u-h-1,\qquad \delta+C\le2.
$$

A violation has excess one or two and needs
$u\ge h+2\ge\lceil r/a\rceil+1$. In particular the one-hole,
three-union-neighbor shape is impossible when $r>2a$.
This does not exclude all violating sets.

## The local implication fails

The [finite evidence](evidence/_index.md) specifies a graph with 29 vertices
at $r=12$ and checks every hereditary $D_{12}$ cap. It has independent
anchors, one/two-support structure, exactly twelve exceptions, a parallel
nonadjacent pair at an eleven-vertex private row of degree twelve,
clique number eleven, and the pointwise receiving-row charge above.
Its set $T$ is $K_{12}-e$; $x$ sees two of its vertices, $y$ a third,
and no vertex of $T$ sees both. Thus

$$
e_F(T\cup\{z\})=65+3=68>D_{12}(13)=67,
\qquad (A,C,\sigma_Z,\delta)=(10,0,1,1).
$$

The ordinary lift slacks are $\sigma_x=0$, $\sigma_y=1$, and the double
lift has slack one. This is an actual cap violation, not just positive
charge in (A).

The graph is underloaded: its order is $29$, not $4\cdot12+1=49$.
Its row sizes are $11,4,1,1$, its receiving-row degrees are five, and
$d_F(z)=7$. Its deficit sum is $31$, not $b-1=11$. It fails the normalized
row-size and degree requirements as well as (G). Its two anchors in $T$
are excluded by L238's pair-capacity argument, and at $r=12,a=4$ the
one-hole pattern itself is excluded. This exact support pattern has no
normalized completion. The example refutes only the local implication
from the stated weaker properties.

The exact integer checker covers all $2^{29}$ subsets by a component
dynamic program, after comparison with all 2,048 subsets of an eleven-vertex
restriction. It recounts all retained extremizers and rejects an edge-addition
negative control. Run from the repository root:

```sh
nice -n 10 uv run --no-sync python wiki/research/erdos_617/parallel_unit_row_fold/evidence/main.py
```

The finite check does not verify the universal normalization arguments.

## Remaining mathematical gap

To justify the fold one still needs
$\sigma_Z(T)\ge |T|-A(T)-C(T)$ whenever (B)--(D) permit a violation.
The available expansion and maximum-independent-set constraints (E)--(I)
do not yet imply this dense-set slack bound. A least-color transfer would
instead require a simultaneous bounded-exception and least-budget
normalization, which is not supplied here.

A narrower question remains for $r\le2a$: can a normalized core contain
$T=K_r-e$ outside both supporting rows, with at most one original anchor,
three union neighbors and no common neighbor? That shape would force
excess one. A completion must satisfy all degree, overload, support-capacity,
balanced-residual and minimum-anchor requirements. Excluding it would
settle only this shape; proving full cap preservation still requires all
other shapes and larger sets. No further graph search or normalization
claim is implied by the local example.

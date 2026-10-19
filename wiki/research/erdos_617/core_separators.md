---
name: research/erdos_617/core_separators
desc: Minimal-ratio cores have no clique cutset or long clique-path strip; two-vertex separators have a rigid independence-loss pattern and a large surplus cost.
tags: [graph-theory, proved, critical-graphs, reductions]
sources: []
created: 2026-09-22T10:40:00Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/core_separators

***

**Proved structural restrictions, not a resolution.** These concern the
[least-budget minimal-ratio core](minimal_ratio_potential.md), not the
possibly different budgeted two-supported residue. Thus

$$
|H|=ra+1,\quad \alpha(H)=a,\quad \omega(H)\le r-1,
\quad |W|\le r\alpha(H[W])\quad(W\subsetneq V(H)). \tag{1}
$$

When needed, use its optional independence-critical pruning. Write
$s(v)=d_H(v)-r\ge0$ and $S=\sum_v s(v)\le r(r-a)$.

Deleting any at most $r$ vertices preserves independence $a$: the
remaining order is greater than $r(a-1)$, so (1) gives the lower bound.

## No clique cutset

Suppose a clique $C$ separates components $B_1,\ldots,B_k$, $k\ge2$.
Since $|C|\le r$, deleting it preserves independence. Put
$b_i=\alpha(H[B_i])$, so $\sum_i b_i=a$.

For every $c\in C$, at least one component $B_i$ satisfies
$\alpha(H[B_i\setminus N(c)])\le b_i-1$: otherwise $c$ augments
maximum independent sets in all components. Assign each $c$ to one
such component and let $C_i$ be its assigned subset. Since $C_i$ is
a clique, $\alpha(H[B_i\cup C_i])=b_i$.
These sets partition $V(H)$ and are all proper. Summing (1) gives
$ra+1\le r\sum_i b_i=ra$, a contradiction.

This argument actually needs only $\omega(H)\le r$, not $r-1$.

## Proper modules in a critical core

A module $M$ has each outside vertex complete or anticomplete to it.
In a connected independence-critical graph, every proper nonempty
module is a clique.

Indeed, if $M$ contains two nonadjacent vertices, take a crossing edge
$ux$, $u\in M$, $x\notin M$. A critical witness in $H-ux$ is an
independent $(a+1)$-set containing $u,x$. It contains no other vertex
of $M$, since $x$ is complete to $M$. Its other vertices are outside
$M$ and anticomplete to $M$, since they avoid $u$. Replace $u,x$ by
two nonadjacent vertices of $M$ to obtain an independent $(a+1)$-set
in $H$, a contradiction.

Thus contracting the true-twin clique modules does not leave arbitrary
nonclique substitution modules. It still need not give a line graph or
one of the [clique-path networks](clique_path_networks.md).

## Complete classification of a two-vertex separator

Assume now that $H$ is independence-critical. If $\{x,y\}$ is a
cutset, then $x,y$ are nonadjacent and there are exactly two components
$A,B$ of $H-\{x,y\}$. After possibly interchanging them, for some
$p+q=a$,

$$
\boxed{|A|=rp-1,\quad |B|=rq,\quad
\alpha(A)=p,\quad \alpha(B)=q.} \tag{2}
$$

Their losses in independence under deleting the neighbors of $x$, of
$y$, and of both are respectively

$$
\boxed{(1,1,1)\text{ on }A,\qquad(0,0,1)\text{ on }B.} \tag{3}
$$


Here and below $A-N(x)$ means the induced subgraph on
$A\setminus N_H(x)$, and similarly for the other expressions.

To prove this, let the components initially be $C_0,\ldots,C_{k-1}$,
put $b_i=\alpha(C_i)$ and $t_i=rb_i-|C_i|$. Deletion stability
gives $\sum_i b_i=a$. Proper-set minimality gives $t_i\ge0$, and
their sum is one. Relabel so that $t_0=1$ and the other slacks vanish.
The vertices $x,y$ are nonadjacent by the clique-cutset exclusion.

For $z\in\{x,y\}$ put

$$
d_i^z=b_i-\alpha(C_i-N(z)),\qquad
d_i=b_i-\alpha(C_i-N(\{x,y\})).
$$

At least one $d_i^z$ is positive, or $z$ extends an independent
$a$-set. If $d_i^z\ge1$, then $\alpha(C_i+z)=b_i$, and applying
(1) to this proper induced set forces $t_i\ge1$. Thus the only
positive singleton loss is on $C_0$.

If $d_0\ge2$, then independent sets in $C_0+\{x,y\}$ using zero,
one, or two cut vertices all have size at most $b_0$. Applying (1)
would force $t_0\ge2$. Consequently

$$
d_0=d_0^x=d_0^y=1.
$$

Since $x,y$ are independent, $\Delta:=\sum_i d_i\ge2$.

Every component meets both $N(x)$ and $N(y)$; otherwise one cut
vertex alone would be a clique cutset. For $i\ne0$, choose an edge
$xu$ with $u\in C_i$ and take its critical independent witness $J$
of size $a+1$. If $y\notin J$, the component $C_0$ contributes at
most $b_0-1$, while all other components contribute at most $b_j$.
Including $x$ still gives at most $a$ vertices, impossible.

Thus $y\in J$. In $C_i$, deleting $xu$ makes at most the one vertex
$u$ newly available outside $N(x)\cup N(y)$. Therefore

$$
|J|\le2+\sum_j(b_j-d_j)+1=a+3-\Delta.
$$

This forces $\Delta=2$. Also $J\cap C_i$ is independent in the
unchanged graph $C_i$, so it has size at most $b_i$. Hence

$$
|J|\le2+\sum_j(b_j-d_j)+d_i=a+d_i,
$$

forcing $d_i\ge1$. Every $i\ne0$ has this property, and $d_0=1$.
It follows that there is just one other component, with joint loss
one. This proves (2)--(3).

## Endpoint degrees and balanced rigidity

The same witness for $xu$, $u\in B$, contains $y$. Thus $u$ cannot
be adjacent to $y$, and

$$
N_B(x)\cap N_B(y)=\varnothing. \tag{4}
$$

Apply (1) to $A-N(x)$ and $A-N(y)$, of independence $p-1$, and
to $B-N(\{x,y\})$, of independence $q-1$. This gives

$$
d_A(x),d_A(y)\ge r-1,\qquad
|N_B(x)\cup N_B(y)|\ge r.
$$

Together with (4),

$$
\boxed{d_H(x)+d_H(y)\ge3r-2,
\qquad s(x)+s(y)\ge r-2.} \tag{5}
$$

In particular a family of $k$ pairwise disjoint two-vertex cutsets
satisfies $k(r-2)\le r(r-a)$.

Both $H[A+x]$ and $H[B]$ are induced $K_r$-free balanced graphs,
with orders $rp,rq$ and independence numbers $p,q$. The established
[two-row](two_row_structure.md), [three-row](three_row_structure.md),
and [hereditary balanced rigidity](hereditary_span_bound.md) results
therefore give, for $r\ge12$,

$$
p,q\ge4,\qquad p,q>\sqrt r/8.
$$

Consequently a core with $a\le7$ is 3-connected, and any two-cut
requires $a>\sqrt r/4$. These are restrictions, not a proof that the
surviving core is 3-connected in general.

## The exact cap-closure obstruction to splitting

The separator produces two smaller overloaded graphs:

$$
H_A=H[A+x+y]+xy,
$$

and $H_B$, obtained from $H[B+x+y]$ by identifying $x,y$ to one
vertex. Their orders and independence numbers are respectively
$(rp+1,p)$ and $(rq+1,q)$, by (3). Both have minimum degree at
least $r$: use the endpoint estimates for $H_A$, and disjointness
(4) for the degrees in $H_B$.

Their edge counts satisfy

$$
e(H_A)+e(H_B)=e(H)+1.
$$

For the potential $\Phi(J,b)=2e(J)-(2r-1)|J|+r^2b$,

$$
\Phi(H_A,p)+\Phi(H_B,q)=\Phi(H,a)+3-2r.
$$

Each potential is nonnegative by complementary Turán. Thus each
factor individually retains the old potential upper bound and hence
the least-color budget.

What is missing is preservation of the hereditary caps. Adding $xy$
in $H_A$, or merging its neighborhoods in $H_B$, can increase an
induced density relative to its new order. New $K_r$'s are not excluded
either. The factors cannot be substituted into the inherited-cap
induction without a further argument. Their simultaneous budgets do
not repair this specific closure gap.

## Long clique-path strips can be removed without adding edges

**Proved.** A core satisfying (1) and the hereditary caps contains no
clique-path strip of length at least four. Here a strip consists of
pairwise disjoint nonempty clique bags $Q_0,\ldots,Q_L$, consecutive
bags are completely joined, and an internal bag has no other neighbors.
The two endpoint bags may have arbitrary outside neighbors and arbitrary
edges between themselves. In particular, this conclusion does not
assume that the entire graph is a clique-path network.

First note the following deletion criterion. There cannot be a nonempty
set $D$ and positive integer $t$ such that

$$
|D|\le rt,\qquad \alpha(H-D)\le a-t. \tag{6}
$$

If $H-D$ is nonempty, its order is at least $r(a-t)+1$, contrary
to proper-induced minimality. If it is empty and $t\le a$, the
size bound contradicts $|H|=ra+1$ directly. In the applications below
there is an independent $t$-set in $D$, so $t\le a$.

Write $u=|Q_0|$, $v=|Q_L|$, and let $S$ be the total internal
bag order. The [clique-path inequalities](clique_path_networks.md)
depend only on consecutive triples and adjacent internal pairs.
They therefore still hold with the permitted extra endpoint edges.

For odd length $L=2k+1\ge5$ they give

$$
S+\min(u,v)\le kr-k+2\le kr.
$$

Delete all internal bags and a smaller endpoint bag. Every independent
set outside this deletion extends by $k$ internal representatives:
even if it uses the surviving endpoint, omitting its adjacent internal
bag leaves a path on $2k-1$ bags, from which alternating bags supply
$k$ representatives. This is (6) with $t=k$.

For even length $L=2k\ge4$, put $T=S+u+v$. The path inequality is

$$
T\le kr+(u+v-r)_+.
$$

If $u+v\le r$, delete all the bags. Alternating internal bags
extend every remaining independent set by $k$ vertices, and
$|D|=T\le kr$. If $u+v>r$, delete only the internal bags. Then
$S\le(k-1)r$. Even if both endpoints are used by an outside
independent set, the middle $2k-3$ internal bags supply $k-1$
alternating representatives. This is (6) with $t=k-1$.

These are induced deletions, so no cap-preservation issue arises.
They do not remove strips of length three: its two internal bags
need not supply a vertex when both endpoints are selected. Thus
the edge-addition and identification gaps for two-separators remain.

## A clique-module deficit bound

If a proper clique module $C$ has order $c$, put $d=r-c$. Every
outside vertex is complete or anticomplete to $C$. Since $\delta(H)\ge r$,
there are at least $d+1$ vertices complete to $C$. On $C$ and any
$d+1$ such vertices, all nonedges lie among the latter vertices.
The $(r+1)$-vertex cap therefore gives

$$
\boxed{d(d+1)\ge2(r-1).} \tag{7}
$$

In particular, a clique substantially closer to order $r$ cannot
be a single true-twin class. This restriction does not bound the
number of true-twin classes within a large private clique.

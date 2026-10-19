---
name: research/erdos_617/critical_semidefinite_gap
desc: Critical edges force a Schrijver-theta gap; copositive equality rigidity gives spectral radius strictly less than r minus one for uncolored pairs.
tags: [graph-theory, proved, semidefinite, critical-graphs]
sources: []
created: 2026-09-22T08:59:28Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/critical_semidefinite_gap

***

**A new approach within this investigation, not a resolution of E617.**
Instead of trying to complete near-full cliques, consider the quadratic
forms encoding independence. Critical-edge witnesses give a uniform
gap between exact copositivity and a standard semidefinite certificate.
The resulting obstruction is to that certificate, not to the coloring.

## The certificate parameter

Define

$$
\sigma(G)=\min\{t:\ P\succeq0,\ P_{vv}=t-1,\
P_{uv}\le-1\text{ for distinct nonadjacent }u,v\}.
\tag{1}
$$

This is Schrijver's $\vartheta'(G)$, or the vector chromatic number of
$\overline G$. The definition and identification were checked in
[Godsil--Roberson--Rooney--Šámal--Varvitsiotis, pp.
1--2](https://arxiv.org/pdf/1801.08243). The argument below uses only (1), not
any further theorem from that paper.

The minimum exists: $t=n=|G|$, $P=nI-J$, is feasible, and
bounded $t$ bounds every entry of a positive semidefinite feasible
matrix. Thus a minimizing sequence has a feasible limit. If
$P_{uv}=p_u\cdot p_v$ is a Gram representation and $I$ is an
independent $a$-set, then

$$
0\le\left\|\sum_{v\in I}p_v\right\|^2\le a(t-a).
$$

In particular $\sigma(G)\ge\alpha(G)$.

For comparison, put $B_t(G)=t(I+A_G)-J$. Then

$$
B_t(G)\text{ is copositive}\quad\Longleftrightarrow\quad
t\ge\alpha(G). \tag{2}
$$

To prove this, minimize $x^\top(I+A_G)x$ over the probability
simplex. If adjacent vertices have positive coordinates, transfer
all their combined weight to one of them without increasing the
value: on that segment the expression is affine. Repetition gives
an independent support. Cauchy--Schwarz then gives minimum
$1/\alpha(G)$, attained by uniform weight on a maximum independent
set. This proves (2).

There is also the exact equivalence

$$
B_t(G)=P+Z,\quad P\succeq0,\ Z\ge0\text{ entrywise}
\quad\Longleftrightarrow\quad \sigma(G)\le t. \tag{3}
$$

For the forward implication, transfer the diagonal of $Z$ into
$P$; this preserves positive semidefiniteness and gives (1).
Conversely a feasible matrix in (1) has $P_{uv}\le t-1$
on every edge by Cauchy--Schwarz, so $B_t(G)-P$ is entrywise
nonnegative. If the optimum is below $t$, increase its diagonal
to obtain a feasible matrix at $t$.

## A quantified gap from two critical edges

An edge is independence-critical if deleting it increases the
independence number.

**Theorem.** Suppose $\alpha(G)=a\ge2$ and $u,v,w$ induce a
path with both $uv,vw$ independence-critical. Let $\varepsilon_a$
be the unique root in $(3-2\sqrt2,\sqrt5-2]$ of

$$
(a-1+\varepsilon)(1+\varepsilon)^2=8(a-1)\varepsilon.
\tag{4}
$$

Then

$$
\boxed{\sigma(G)\ge a+\varepsilon_a>a+3-2\sqrt2.} \tag{5}
$$


Let $t=a+\varepsilon$ be feasible, put $d=a-1$,
$T=t-1=d+\varepsilon$, and take its Gram vectors.
For a critical edge $xy$, a witness after deletion supplies an
independent $d$-set $S$ anticomplete to both endpoints.
Writing $q=\sum_{s\in S}p_s$ gives

$$
\|q\|^2\le d(1+\varepsilon),\qquad
(p_x+p_y)\cdot q\le-2d.
$$

Thus Cauchy--Schwarz and the parallelogram identity yield

$$
\|p_x-p_y\|^2
\le4\left(T-\frac d{1+\varepsilon}\right)
=\frac{4\varepsilon t}{1+\varepsilon}=:D. \tag{6}
$$


Suppose $\varepsilon<\varepsilon_a$. The root analysis below
gives $\varepsilon_a\le\sqrt5-2<1/4$, and

$$
(1+\varepsilon)T-2\varepsilon t
=d-(d+1)\varepsilon-\varepsilon^2
\ge1-2\varepsilon-\varepsilon^2>0.
$$

Hence $D<2T$. Apply (6) to the two path edges:

$$
(p_u+p_w)\cdot p_v\ge2T-D>0.
$$

Another Cauchy--Schwarz inequality gives

$$
\|p_u-p_w\|^2
=4T-\|p_u+p_w\|^2
\le4D-D^2/T.
$$

Since $uw$ is a nonedge, its squared distance is at least $2t$.
Substituting $D$ and simplifying therefore gives

$$
(d+\varepsilon)(1+\varepsilon)^2-8d\varepsilon\le0. \tag{7}
$$


The polynomial on the left is strictly decreasing on
$[0,\sqrt5-2]$ for every $d\ge1$. At $c=3-2\sqrt2$ its
value is $c(1+c)^2>0$, while at $\gamma=\sqrt5-2$ its
value is $(1-d)\gamma(1+\gamma)^2\le0$.
This proves existence and uniqueness of the specified root and
contradicts (7) below it, proving the theorem.

For $a=2$, the gap is exactly $\sqrt5-2$. This is attained by
$C_5$: the matrix

$$
P=\sqrt5\,I-J+\frac{5-\sqrt5}{2}A_{C_5}
$$

has the required entries and eigenvalues zero (multiplicity three)
and $5(\sqrt5-1)/2$ (multiplicity two). Thus
$\sigma(C_5)=\sqrt5$. As $a$ grows, the roots in (4)
decrease to $3-2\sqrt2$.

In particular an independence-critical graph with
$\sigma(G)=\alpha(G)$ must be a disjoint union of cliques:
every noncomplete connected component contains an induced
three-vertex path, to which (5) applies. The converse follows
directly by assigning the same regular-simplex vector to every
vertex in a clique component.

## Safe normalization of an actual coloring

Suppose a counterexample exists on $n=r^2+1$ vertices.
Choose one color as a sink. In each other color, repeatedly
recolor into the sink any edge whose deletion preserves
independence at most $r$. Every other color's independence
bound remains valid: only the source loses an edge and the
sink gains one. The process terminates because the total
number of nonsink edges decreases.

Every final nonsink graph has independence exactly $r$ and
every edge critical. Indeed deletion of a single edge raises
independence by at most one, so a nonempty graph with
independence below $r$ would allow another deletion.
The edgeless case is impossible on $n>r$ vertices.

No nonsink graph has $K_{r+1}$. If all its components were
cliques, their number would be $r$, giving order at most
$r^2$, a contradiction. Hence it has a noncomplete component
and an induced critical path. Consequently all $r-1$ nonsink
colors satisfy

$$
\boxed{\vartheta'(G_i)\ge r+\varepsilon_r
>r+3-2\sqrt2.} \tag{8}
$$

If the sink is initially a largest color, at least one nonsink
starts within the minority budget and retains that budget after
pruning. All hereditary upper caps still follow from the resulting
actual complete coloring.

## What the approach has and has not established

The exact matrices $B_r(G_i)$ are copositive and satisfy

$$
\sum_i B_r(G_i)=r(r-1)I. \tag{9}
$$

Nevertheless (8) and (3) show that all but one can be forced
outside the cone of positive-semidefinite-plus-nonnegative matrices,
with the uniform gap (5). Thus replacing copositivity by that
stronger certificate is not a justified route to excluding
counterexamples.

There is no contradiction between nonmembership of individual
matrices and their diagonal sum. The exceptional two-color
pentagon already demonstrates this: its two matrices are copositive,
neither has the decomposition (3) at $t=2$, and their sum is $2I$.
No inequality coupling the exceptional parts of all $r$ matrices
has been proved here.

An initially considered ordinary-theta product argument was also
insufficient. The pairwise bound for edge-disjoint graphs concerns
$\vartheta$, not $\vartheta'$, and cannot justify (3).
The critical-witness argument above is what supplies the actual
$\vartheta'$ conclusion.

The cone equivalence, Gram inequalities, root interval, and coloring
normalization were checked by the author and are author-recorded. No
numerical SDP or
computational evidence is used. The main unresolved requirement is
a simultaneous constraint on these copositive matrices, not another
single-color semidefinite lower bound.

## A strict spectral bound for uncolored pairs

**Proved, for $r\ge3$.** In any partial $r$-coloring on $N=r^2+1$ vertices
whose color graphs are edge-disjoint and have independence at most
$r$, let $U$ be the graph of uncolored pairs. Then

$$
\boxed{\rho(U)<r-1.} \tag{10}
$$

This is a coupled necessary condition, not a coloring contradiction.

Write $M_i=I+A_i-J/r$. The Motzkin--Straus argument in (2) makes
every $M_i$ copositive, and

$$
\sum_iM_i=(r-1)I-A_U.
$$

Apply this sum to a nonnegative Perron vector of $A_U$ to get
$\rho(U)\le r-1$.

Suppose equality holds. Choose a Perron vector $x$ positive on one
component $S$ attaining this spectral radius, zero elsewhere, and
normalize $\sum_vx_v=1$. Each $x^{\mathsf T}M_ix$ is nonnegative
and their sum is zero, so each is zero. Perturbing $x$ in either
direction on $S$ preserves nonnegativity for a sufficiently small
perturbation. Thus

$$
M_i[S]x_S=0,\qquad M_i[S]\succeq0.
$$

If $uv$ is a color-$i$ edge within $S$, then
$(e_u-e_v)^{\mathsf T}M_i[S](e_u-e_v)=0$. Positive semidefiniteness
makes the two columns equal, so $u,v$ have identical closed
neighborhoods within $S$. Every connected component of $G_i[S]$
is consequently a clique. The kernel equation says that each such
clique has $x$-weight $1/r$; hence there are exactly $r$ of them.

For a vertex $y\notin S$, copositivity applied to $x+\varepsilon e_y$
gives $(M_ix)_y\ge0$. Its color-$i$ neighbors in $S$ therefore
have $x$-weight at least $1/r$. Summing over colors forces equality
in every color, since color edge sets are disjoint and $x(S)=1$.
In color $i$, the vertex $y$ must be complete to one of the $r$
cliques in $S$; otherwise one nonneighbor from each clique, together
with $y$, exceeds the independence bound. Weight equality, and
positivity of $x$ on $S$, make it anticomplete to the other cliques.

Assign every outside vertex to that unique clique. Two vertices
assigned to the same clique must be adjacent in color $i$: if not,
one representative from each of the other $r-1$ cliques augments
them to an independent $(r+1)$-set. This partitions the whole vertex
set into $r$ color-$i$ cliques. Each has order at most $r$, since
a larger clique is independent in any other color. This contradicts
$N=r^2+1$, proving strictness.

No lower bound forcing $\rho(U)\ge r-1$ is known. In particular,
(10) does not justify a completion preserving all full components;
the endpoint-coverage condition in
[Critical components](critical_component_reduction.md) remains open.

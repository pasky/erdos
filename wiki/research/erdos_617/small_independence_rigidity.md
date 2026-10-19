---
name: research/erdos_617/small_independence_rigidity
desc: A uniform core theorem when r is at least 20000 times the eighth power of the target independence bound.
tags: [graph-theory, proved, stability]
sources: []
created: 2026-09-21T23:52:12Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/small_independence_rigidity

***

This earlier proof is superseded by the stronger
[hereditary span and equality theorem](hereditary_span_bound.md).
It is retained to document the initial AES-deletion approach.

**Proved, but not a solution of Problem 617.** Suppose an $r$-coloring of a
complete graph has $\alpha(G_j)\le r$ for every color. Let $a\ge2$ and

$$
r\ge20000a^8.
$$

Every induced target graph $H$ with $\alpha(H)\le a$ has at most $ar$
vertices. If it has exactly $ar$ vertices, it partitions into $a$ target
$K_r$'s, with a matching of target edges between each pair.

Only the [full density inequalities](reductions.md), the local cap, and
Andrásfai--Erdős--Sós are used. The latter theorem was checked in [the supplied
full source, Theorem
1.1](../../../library/extremal_graph_theory/andrasfai_et_al_1974_connection_between_chromatic_number_maximal_clique_minimal_degree_graph/_index.md):
a $K_{a+1}$-free graph of order $m$ and minimum degree greater than
$(3a-4)m/(3a-1)$ is $a$-partite.

It suffices to analyze $n=ar+\eta$, $\eta\in\{0,1\}$.

## Removing a bounded exceptional set

Put $F=\overline H$, $\gamma=(a-1)/a$, and $M=6a^3$.
The graph $F$ is $K_{a+1}$-free, so its continuous Turán deficit

$$
\mathcal D(F)=\frac{\gamma n^2}{2}-e(F)
$$

is nonnegative. The inherited lower bound
$e(F)\ge(r-1)p_r(n)$ gives

$$
\mathcal D(F)\le \frac{a(a-1)r}{2}.
$$

For $\eta=1$, its exact upper expression is
$[a(a-1)/2-1]r+a+(a-1)/(2a)$, at most the stated bound.

While $F$ is not $a$-partite, delete a vertex supplied by
Andrásfai--Erdős--Sós. At current order $m$ its degree is at most
$(3a-4)m/(3a-1)$. Deleting it decreases the deficit by at least

$$
\frac{m}{a(3a-1)}-\frac12
\ge\frac{r}{4(3a-1)}
$$

through the first $M$ deletions: our bound on $r$ ensures both
$m\ge ar/2$ and $r\ge2(3a-1)$. But

$$
\frac{Mr}{4(3a-1)}>\frac{a(a-1)r}{2}.
$$

Thus fewer than $M$ deletions are possible.

Write $X$ for the deleted set, $t=|X|<M$. Its complement in $H$ partitions
into $a$ cliques $C_i$, of orders $r-d_i$, where

$$
d_i\ge0,\qquad \sum_i d_i=t-\eta.
$$

Here every clique has order at most $r$ by the local cap. There must be
exactly $a$ nonempty parts because $t<r$.

## Sparse interactions between core cliques

Since $d_i+d_j<r$, the inherited cap on $C_i\cup C_j$ gives the exact bound

$$
e_H(C_i,C_j)
\le(r-d_i)(r-d_j)-(r-1)(r-d_i-d_j)
=r+d_id_j-d_i-d_j\le2r.
$$

The last inequality uses $M^2\le r$. Thus the total number of target edges
between core cliques is less than $a^2r$.

Set $L=\lceil2a\sqrt r\rceil$. For every $x\in X$, there is some $i$ such
that $x$ has fewer than $L$ nonneighbors in $C_i$. Otherwise choose
independently one nonneighbor in each core. The expected number of target
edges among the choices is less than $a^2r/L^2\le1/4$, so an independent
choice exists. Adjoining $x$ contradicts $\alpha(H)\le a$.
Call every such index $i$ an available assignment for $x$.

For a set $S$ of $d_i+1$ outsiders to $C_i$, the local cap on
$C_i\cup S$, of order $r+1$, gives

$$
\sum_{x\in S}d_F(x,C_i)
\ge r-1-\binom{d_i+1}{2}.
$$

Our numerical hypothesis ensures

$$
(M+1)L+\binom{M+1}{2}<r-1.
\tag{1}
$$

Consequently, at most $d_i$ exceptional vertices can have $i$ as an
available assignment.

If $\eta=1$, there are $t$ exceptions and total capacity
$\sum_i d_i=t-1$. Every exception has an available assignment, which is
impossible. This proves the order bound.

## Completing the equality structure

Suppose $\eta=0$. Available assignments have total capacity $t$, so each
exception has exactly one available assignment, and exactly $d_i$
exceptions are assigned to $C_i$. Denote this set by $Z_i$ and put
$P_i=C_i\cup Z_i$, so $|P_i|=r$.

For $x\notin P_i$, apply the same local cap to $C_i\cup Z_i\cup\{x\}$.
Since every member of $Z_i$ has fewer than $L$ nonneighbors in $C_i$,

$$
d_H(x,C_i)\le K:=ML+\binom{M+1}{2}+1.
$$

The hypothesis also ensures

$$
M+2K\le r/2.
\tag{2}
$$

If $x,y\in P_i$ were nonadjacent in $H$, then in every other core $C_j$
they would have at least $r-M-2K\ge r/2$ common nonneighbors.
Choose one independently from each such core. Their expected number of
target edges is less than $4a^2/r<1$. Together with $x,y$, an
independent choice would give $a+1$ vertices, a contradiction.
Every $P_i$ is therefore a target $K_r$.
The local cap makes target edges between distinct $P_i$'s a matching.

## Constant check

The stated assumption implies

$$
r\ge256a^2(M+1)^2.
$$

Indeed $M+1\le(49/8)a^3$ for $a\ge2$, and
$256(49/8)^2=9604<20000$.
In particular,

$$
(M+1)L\le r/8+r/256,\qquad
\binom{M+1}{2}\le r/512,\qquad M\le r/256.
$$

Hence the left side of (1) is at most $67r/512<r-1$.
Also $K\le67r/512+1$, so
$M+2K\le17r/64+2\le r/2$.
All weaker size assumptions used above follow at once.

## Remaining gap

This theorem handles independence bounds up to a constant multiple of
$r^{1/8}$, not $a=r$. Even the scalar packing framework requires
structural emptiness through a range approximately $a\le\sqrt r$.
It must not be described as proving the original assertion for an infinite
set of values of $r$.

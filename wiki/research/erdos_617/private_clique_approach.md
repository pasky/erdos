---
name: research/erdos_617/private_clique_approach
desc: An elementary obstruction to complete coverage by target cliques, and private-neighborhood formulations of the remaining problem.
tags: [graph-theory, proved, draft]
sources: []
created: 2026-09-22T00:02:05Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/private_clique_approach

***

The complete-coverage lemma and the two reductions below are proved. The
final section records an unaudited extension and is not part of the established
results. None of these statements resolves Problem 617.

Throughout, put $N=r^2+1$. A target graph $G$ satisfies


$$
\alpha(G)\le r,\qquad e(G)\le \frac{r(r^2+1)}2,
\tag{1}
$$


and the inherited local cap


$$
e(G[W])\le \binom r2+1\qquad (|W|=r+1).
\tag{2}
$$


When stated explicitly, we also use the full induced-density bound
$e(G[W])\le D_r(|W|)$ from [Parameterized reductions](reductions.md).

## Complete coverage by target cliques is impossible

**Theorem.** For $r\ge4$, a graph satisfying (1)--(2) has a vertex contained
in no $K_r$.

First note three consequences of (2). Every vertex outside a $K_r$ has at
most one neighbor in that clique. Consequently distinct $K_r$'s intersect
in at most one vertex, and their edge sets are disjoint. They also have no
*Berge triangle*: three cliques cannot have distinct vertices in their three
pairwise intersections. Indeed, one intersection vertex would lie outside
the opposite clique and have two neighbors in it.

Suppose every vertex is covered, and list all target cliques as
$Q_1,\ldots,Q_t$. Edge disjointness and (1) give


$$
t\le\frac{r^2+1}{r-1}=r+1+\frac2{r-1}<r+2.
$$


Coverage gives $tr\ge r^2+1$, so $t=r+1$. If $m(x)$ is the number of these
cliques containing $x$, then


$$
\sum_x(m(x)-1)=r-1.
\tag{3}
$$


Call a vertex shared when $m(x)\ge2$. The total number of shared incidences
is at most $2r-2$, because $m\le2(m-1)$ for $m\ge2$.

Let $P_i$ be the private vertices of $Q_i$, those lying in no other $Q_j$,
and put $p_i=|P_i|$. Each $P_i$ is nonempty: every shared vertex of $Q_i$
uses at least one unit of (3), so $Q_i$ has at most $r-1$ shared vertices.
Edges between two private parts form a matching. If their parent cliques
intersect, there are no such edges: a private vertex of one already has the
intersection vertex as its sole possible neighbor in the other clique.

All edges between private parts lie outside the listed $K_r$'s. Their total
number is therefore at most


$$
\frac{r(r^2+1)}2-(r+1)\binom r2=r.
\tag{4}
$$


An independent transversal of the $r+1$ private parts contradicts (1).
Suppose no such transversal exists, and take an inclusion-minimal
subcollection without one. Let its number of parts be $k$.

Every private vertex in an active part has a neighbor in another active
part. Otherwise that vertex could be combined with a transversal of the
remaining parts. Consequently, by (4),


$$
\sum_{i\text{ active}}p_i\le2r.
\tag{5}
$$


Also $p_i\le k-1$ for every active part: a transversal of the other parts
forbids at most one vertex per chosen representative, since conflicts between
parts are matchings. Finally, the shared-incidence bound gives


$$
\sum_{i\text{ active}}p_i\ge kr-(2r-2)=(k-2)r+2.
\tag{6}
$$


Equations (5)--(6) imply $k\le3$. The case $k=1$ is impossible because
the parts are nonempty. If $k=2$, both private parts have order one. The
two parent cliques therefore contain at least $2r-3$ distinct shared
vertices, using their intersection bound. Each uses at least one unit of
(3), contradicting $2r-3>r-1$.

If $k=3$, then (6) and $p_i\le2$ give $r+2\le6$. Thus only $r=4$
remains. Equality now forces all three private parts to have order two,
all six shared incidences to lie in their three parent cliques, and every
shared vertex to have multiplicity two. Each parent clique has two shared
vertices. Linearity then makes the three intersections distinct, producing
the forbidden Berge triangle. This final contradiction proves the theorem.

This proof uses only the one-color edge budget and local cap. It does not
assume the full induced-density inequalities.

## Minimal Hall-ratio cores

Here assume the full inherited density bounds as well. Choose an
inclusion-minimal induced subgraph $H$ with


$$
|H|>r\alpha(H),
$$


and write $a=\alpha(H)$. Such an $H$ exists if $G$ is a counterexample.
Deleting one vertex shows that $|H|=ra+1$. It is connected, since otherwise
one component would itself violate the same inequality. Moreover,


$$
\delta(H)\ge r.
$$


For if $d_H(v)\le r-1$, deleting $N_H[v]$ leaves at least
$r(a-1)+1$ vertices and independence number at most $a-1$, contrary to
minimality. Equality $2e(H)=r|H|$ would make $H$ $r$-regular. Brooks's
theorem would then make it $r$-colorable: (2) forbids $K_{r+1}$, and the
odd-cycle exception has degree two. Thus


$$
\frac{r|H|}{2}<e(H)\le D_r(|H|).
$$


For $r\ge4$, necessarily $a\ge3$. Here is a self-contained proof of the
independence-two obstruction used for this assertion. If an induced target
graph $J$ on $2r+1$ vertices had $\alpha(J)\le2$, its complement $F$
would be triangle-free and nonbipartite. A bipartition would otherwise
give a clique of order at least $r+1$ in $J$.

Take a shortest odd cycle in $F$, of length $2k+1\ge5$. It is induced,
every vertex outside it has at most $k$ neighbors on it, and Mantel's
theorem applies to the remaining vertices. Writing $n=2r+1$ gives


$$
\begin{aligned}
e(F)&\le(2k+1)+k(n-2k-1)+\frac{(n-2k-1)^2}{4}\\
&=\frac{(n-1)^2}{4}+1-k(k-2)\le r^2+1.
\end{aligned}
$$


Hence $e(J)\ge r^2+r-1$, whereas full inherited density gives
$e(J)\le D_r(2r+1)=r^2+2$. These contradict each other for $r\ge4$.
See also [Two-row structure](two_row_structure.md).

## Private neighborhoods of a maximum independent set

Choose a maximum independent set $S$ minimizing $\sum_{s\in S}d(s)$.
Under (1), $|S|=r$: the elementary Caro--Wei average-degree bound gives
$\alpha(G)\ge N/(r+1)>r-1$.

For $s\in S$, define


$$
C_s=\{s\}\cup\{x\notin S:N(x)\cap S=\{s\}\}.
$$


The set $C_s$ is a clique, because two nonadjacent private neighbors could
replace $s$ in $S$. Furthermore $d(x)\ge d(s)$ for every $x\in C_s$,
by the degree-sum minimality of $S$.

Every vertex outside the disjoint union of the $C_s$'s has at least two
neighbors in $S$. Counting edges incident to $S$ therefore gives


$$
2N\le\sum_{s\in S}\bigl(d(s)+|C_s|+1\bigr).
\tag{7}
$$


Since $N=r^2+1$, some private clique $C_s$ has
$d(s)+|C_s|\ge2r$. Every vertex of this clique consequently has degree at
least $2r-|C_s|$.

This argument is the mechanism of Theorem 1 in
[Henning--Löwenstein--Southey--Yeo
(2014)](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v21i1p38/pdf/),
whose statement and proof on printed pages 3--4 were checked. It is a necessary
high-degree-clique certificate, not an edge-budget contradiction.

Put $B=V(G)\setminus\bigcup_{s\in S}C_s$, and $K_b=N(b)\cap S$ for
$b\in B$. For every $T\subseteq S$, define


$$
W_T=\bigcup_{s\in T}C_s\;\cup\;\{b\in B:K_b\subseteq T\}.
$$


This set is anticomplete to $S\setminus T$, so
$\alpha(G[W_T])\le|T|$. In particular, when $T\ne\varnothing$,


$$
p_{|T|}(|W_T|)\le e(G[W_T])\le D_r(|W_T|).
$$


The capacities $r-|C_s|$ satisfy


$$
|B|=1+\sum_{s\in S}(r-|C_s|).
$$


Thus the full set $S$ is overloaded: it contains more vertices $b$ with
$K_b\subseteq S$ than its total capacity. An inclusion-minimal overloaded
$T$ gives $|W_T|>r|T|$ and $\alpha(G[W_T])\le|T|$. This organizes
potential applications of the full induced-density constraints to a smaller
core, but does not by itself exclude that core.

## Draft extension: bounding the total number of target cliques

**Not independently checked and not included among the proved results.**
An extension of the private-part argument was developed claiming that the
total number of $K_r$'s is at most $r-2$ for $r\ge12$. This extension
has not been independently audited.
The complete-coverage theorem above does not imply this stronger claim.

The proposed argument keeps $u$ uncovered vertices and $t=r-j$ target
cliques. Their incidence excess and the budget for edges outside them are


$$
L=u-jr-1,\qquad
M=\frac{(j+1)r^2+(1-j)r}{2}.
$$


Its first dependency is the recent localized independence inequality
recorded in [Packing tools](packing_tools.md). A tangent-line calculation
was proposed to give, when $u\ge2M/r$,


$$
\alpha(G)\ge
\frac{r^2+jr+2-2u}{r}
+\frac{2(u-jr-1)}{3r-1}
+\frac{2u^2}{ru+2M}.
\tag{8}
$$


For $j=0$ this would imply $u\le2r-3$, and for $j=1$ it would imply
$u\le4r-12$ in the stated range.

The second dependency is an independent-transversal analysis. Let $D$ join
pairs of disjoint target cliques. After avoiding an independent
$(j+1)$-set of uncovered vertices, each private list has order at least its
degree in $D$. A connected matching-conflict cover with one list larger
than its degree has a transversal by greedy coloring along a rooted
spanning tree. An uncolorable component must consequently have all lists
degree-sized. Fixing a color at a noncut vertex also shows that every
such color must be matched into each adjacent list. These facts were used
to claim that the available edge budget excludes a connected obstruction,
and that a proper obstructing component forces a complete-bipartite
clique-intersection pattern with one side of size at most two.

The remaining proposed checks are the quantitative bounds in (8), the
connected-obstruction edge counts, and the final two complete-bipartite
patterns. For $j=1$, the one-block pattern was reduced to an induced
$(2r+1)$-vertex graph of independence at most two; the two-block pattern
was reduced to $\alpha(G[U])\le3$ on $3r-5$ vertices, whose Turán lower
bound exceeds $M=r^2$ for $r\ge12$. These reductions should be audited
together with their hypotheses before the stronger clique-count bound is
promoted to an established result. No general clique-count descent or
solution of the original quantified problem has been established.

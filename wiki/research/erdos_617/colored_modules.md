---
name: research/erdos_617/colored_modules
desc: A counterexample has no nontrivial colored module, and every pair of vertices has color neighborhoods differing in at least ceiling r over three positions.
tags: [graph-theory, proved, constructions, color-coupling]
sources: []
created: 2026-09-22T13:00:00Z
updated: 2026-10-14T00:26:52Z
---


# research/erdos_617/colored_modules

***

**Proved necessary conditions, not a resolution.** Let an $r$-coloring
of $K_{r^2+1}$, $r\ge3$, have color graphs $G_i$ with
$\alpha(G_i)\le r$. A *colored module* is a vertex set $S$ such
that, for every $x\notin S$, all edges from $x$ to $S$ have the
same color; that color may depend on $x$.

There is no colored module with $2\le |S|\le r^2$. In particular,
no ordinary nontrivial substitution or blowup of an edge-colored
complete graph can be a counterexample. This does not exclude
constructions that color edges between fibers nonuniformly.

## A coupled inequality for common nonneighbors

Let $O$ be a vertex set of order $m$, and for each color choose
$W_i\subseteq O$ with $\alpha(G_i[W_i])\le b_i$. Omit terms for
which $b_i=0$; those sets must be empty. Put

$$
L=\sum_i|W_i|,\qquad B=\sum_i b_i.
$$

When $L>0$, also $B>0$, and

$$
\boxed{\frac{2L^2}{B}-(r+1)L\le m(m-1).} \tag{1}
$$

Indeed, the [localized independence inequality](packing_tools.md)
and $\omega(G_i)\le r$ give

$$
2e(G_i[W_i])\ge\frac{2|W_i|^2}{b_i}-(r+1)|W_i|.
$$

Sum, use Cauchy--Schwarz, and note that the counted edges of
different colors are disjoint subsets of $\binom O2$. The input
inequality is Theorem 2.2 of
[Abiad--Kumar--Pragada](https://arxiv.org/html/2609.00210v1#S2),
evaluated at the uniform vector. Its relevant statement and proof were checked,
as the linked note records.

## Quantitative separation of two color neighborhoods

For distinct $u,v$, define

$$
k(u,v)=|\{x\notin\{u,v\}:c(ux)\ne c(vx)\}|.
$$

Then

$$
\boxed{\frac{2k(u,v)^2}{(r-1)^2}
-3(r+1)k(u,v)+r^2-1\le0,} \tag{2}
$$

and therefore

$$
\boxed{k(u,v)\ge\lceil r/3\rceil.} \tag{3}
$$

To prove this, take $O=V\setminus\{u,v\}$ and let $W_i$
consist of vertices sending neither incident edge to $u,v$ in
color $i$. If $c(uv)=j$, the independence capacities are
$b_j=r-1$ and $b_i=r-2$ for $i\ne j$: append one or both of
$u,v$ to an independent set in $W_i$, as appropriate. Thus

$$
m=r^2-1,\quad B=(r-1)^2,\quad L=(r-1)m-k(u,v).
$$

An agreeing outside vertex belongs to $r-1$ sets $W_i$ and a
disagreeing one belongs to $r-2$. Substituting in (1) gives (2).
For $0\le k\le(r-1)/3$, the constant minus the linear term in
(2) is nonnegative and its quadratic term is positive unless
$k=0$, when the constant is positive. This proves (3).

This argument does not require the full-palette conclusion.
In particular, it directly excludes two-vertex colored modules.

## Excluding every proper nontrivial module

Suppose $S$ is a colored module. Write

$$
t=|S|,\quad m=r^2+1-t,\quad
a_i=\alpha(G_i[S]),\quad b_i=r-a_i.
$$

Let $W_i$ consist of vertices outside $S$ whose common color
to $S$ is not $i$. Independent sets in $S$ and $W_i$ combine
in color $i$, so $b_i$ is a valid capacity. Here
$L=(r-1)m$, and (1) implies

$$
B\ge\frac{2(r-1)^2m}{m+r^2-2}. \tag{4}
$$


Complementary Turan on $S$ gives

$$
2e(G_i[S])\ge t^2/a_i-t.
$$

Summing over colors and applying Cauchy--Schwarz gives

$$
\sum_i\frac1{a_i}\le\frac{t+r-1}{t},\qquad
\sum_i a_i\ge\frac{r^2t}{t+r-1},\qquad
B\le\frac{r^2(r-1)}{t+r-1}. \tag{5}
$$

For $t=2$ the preceding separation theorem is enough. Suppose
$t\ge3$. Every vertex sees every color, by the established
[critical-component reduction](critical_component_reduction.md).
An outside vertex sees only one color on $S$ and at most $m-1$
colors on the other outside vertices, so $m\ge r$. Also
$m\le r^2-2$.

Combining (4)--(5) requires $F(m)\le0$, where

$$
F(m)=2(r-1)m(r^2+r-m)-r^2(m+r^2-2).
$$

This polynomial is concave, but its two endpoint values are

$$
F(r)=r^2(r-1)(r-2)>0,\qquad
F(r^2-2)=2(r-2)(r^2-2)>0.
$$

It is therefore positive throughout the required interval, a
contradiction. The known cases $3\le r\le11$ may simply be
treated as inputs; the full-palette reduction supplies the
nonvacuous conditional argument for the remaining range.

## A shorter structural proof for the remaining range

For $r\ge4$, two disjoint full cliques of one color already
exclude all nontrivial proper modules. Such cliques are supplied
by the [least-color packing reduction](packing_tools.md).

First, a module $S$ with at least two vertices cannot be disjoint
from a full color-$i$ clique $Q$. Partition $Q$ into sets $Q_j$
according to their common color to $S$. For $j\ne i$, the
independent-set bound gives $|Q_j|\ge\alpha(G_j[S])$. Any two
vertices of $S$ consequently give

$$
r\ge\sum_{j\ne i}|Q_j|
\ge\sum_{j\ne i}\alpha(G_j[S])\ge2r-3>r.
$$


Thus $S$ meets two disjoint full color-$i$ cliques $Q,R$.
If $q\in Q\setminus S$, the module condition makes $q$
complete to $S$ in color $i$. The full-clique outsider cap
then gives $|R\cap S|=1$. Every vertex of $R\setminus S$
is likewise complete to $S$ in color $i$. A vertex of
$Q\cap S$ now has $r-1\ge2$ color-$i$ neighbors in $R$,
again contradicting that cap. Hence $Q\subseteq S$.
For an outside vertex $x$, the $(r+1)$-set $Q\cup\{x\}$
uses at most two colors, the final contradiction.

The general inequality, endpoint arithmetic, and structural proof were checked
by the author and are author-recorded. None forces a module to exist in an
arbitrary coloring, so none proves the quantified assertion.

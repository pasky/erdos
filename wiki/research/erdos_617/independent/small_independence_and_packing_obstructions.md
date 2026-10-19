---
name: research/erdos_617/independent/small_independence_and_packing_obstructions
title: Independent investigation of Erdős Problem 617
desc: Unverified isolated investigation retained verbatim below the metadata; audited claims are recorded in independent-comparison.
tags: []
sources: []
created: 2026-09-22T04:17:41Z
updated: 2026-10-13T05:28:09Z
---


# Independent investigation of Erdős Problem 617

***

## Status

The late pair-density improvement and concrete failed approaches are included in
the appendices below.

**The problem is not resolved here.** No counterexample has been constructed,
and the arguments below do not prove the assertion for all $r$.

This investigation used only
[problem page](../../../problems/extremal_graph_theory/E0617/_index.md) and the
supplied Erdős–Gyárfás paper. In particular, it did not use the later fixed-case
proofs mentioned on the problem page. All results below are parameter-uniform;
no additional isolated case of the original problem is claimed.

The main completed line is a quantitative structural obstruction: in a
hypothetical counterexample, a vertex set of size $ar+1$ with independence
number at most $a$ in one color must satisfy


$$
 r<256a^6,\qquad r<4096a^5.                                  \tag{1}
$$


Thus every minimal induced subgraph violating the inequality
$|U|\le r\alpha(G_i[U])$ has independence number greater than
$\max\{(r/256)^{1/6},(r/4096)^{1/5}\}$. The first bound is proved in Section 3
and the second in Appendix A. This excludes bounded-independence defects without
assuming any particular construction or component structure. The proof uses an
elementary quantitative Turán argument, an independent-transversal estimate, and
the requirement that every $r+1$ vertices see all colors.

Other completed results are:

* Every $2r+1$-set has an independent triple in every color. For $r\ge7$,
  every $3r+1$-set has an independent four-set in every color.
* No color contains $r$ vertex-disjoint monochromatic $K_r$'s, even when
  arbitrary extra edges join those cliques.
* Starting from the paper's affine-plane coloring, any hypothetical
  extension by one vertex requires at least $2(r-1)^2$ old-edge
  recolorings. For $r\ge5$, at least $(r-1)(2r-1)$ are required.

The proofs and the remaining obstruction follow. Additional construction
obstructions are indexed at the end.

## 1. Necessary conditions and notation

Suppose a counterexample exists, and let $G_1,\ldots,G_r$ be its color
graphs on $r^2+1$ vertices. Then


$$
 \alpha(G_i)\le r,\qquad \omega(G_i)\le r.                    \tag{2}
$$


For positive integers $k,m$, write


$$
 T_k(m)=k\binom q2+sq,
 \qquad m=kq+s,\quad 0\le s<k.
$$


This is the minimum number of edges in an $m$-vertex graph with
independence number at most $k$, by Turán's theorem. Every vertex subset

$U$ therefore satisfies the **hereditary edge bound**


$$
 e(G_i[U])\le f_r(|U|),\qquad
 f_r(m)=\binom m2-(r-1)T_r(m).                               \tag{3}
$$


Indeed, each of the other $r-1$ colors contributes at least $T_r(|U|)$
edges on $U$. In particular, every $r+1$-set has at least $r-1$
nonedges in each color, and


$$
 e(G_i[U])\le r^2\quad\text{when }|U|=2r.                   \tag{4}
$$


An additional useful consequence is that, for any color-$i$ clique $Q$
of order $r$ and any $v\notin Q$,


$$
 |N_{G_i}(v)\cap Q|\le1.                                    \tag{5}
$$


All $r-1$ other colors must occur among the $r$ edges from $v$ to

$Q$.

## 2. Small-independence subsets

We use the following refinement of Turán's theorem, proved from scratch
in a companion note that is not retained: if $\alpha(H)\le k$, but the vertices
of $H$ cannot be partitioned into $k$ cliques, then


$$
 e(H)\ge T_k(|H|)+\left\lfloor\frac{|H|}{k}\right\rfloor-1.
                                                               \tag{6}
$$


The proof first uses nondecreasing vertex cloning in the complement until
the first $k$-partite graph appears. Immediately before that step,
deleting one vertex leaves a $k$-partite graph. Counting the missing
edges necessary to block every transversal of that vertex's neighborhood
gives $6$. The linked note includes the complete cloning argument and
count, not an invocation of an external refinement.

Suppose $2\le a\le r$ and a set $U$ of size $ar+1$ has

$\alpha(G_i[U])\le a$. Since $\omega(G_i[U])\le r$, this graph
cannot be partitioned into $a$ cliques, so


$$
 e(G_i[U])\ge T_a(ar+1)+r-1.
$$


For $j\ne i$, every color-$j$ clique in $U$ is independent in

$G_i[U]$, so it has at most $a$ vertices. Thus $G_j[U]$ cannot
be partitioned into $r$ cliques, and


$$
 e(G_j[U])\ge T_r(ar+1)+a-1.
$$


The resulting lower bound for the total number of edges exceeds

$\binom{ar+1}{2}$ by


$$
 \frac{-a^2+3a+2}{2}\,r-2a.                                \tag{7}
$$


For $a=2$, this is $2r-4>0$; for $a=3$, it is $r-6>0$ when

$r\ge7$. This proves the two local independence assertions in the
summary. The same calculation does **not** exclude $a=4$: its value
there is $-r-8$.

## 3. A quantitative obstruction for arbitrary independence parameter

**Theorem.** Let $a\ge2$ and $r\ge256a^6$ be integers. There is no
graph $H$ on $ar+1$ vertices satisfying


$$
 \alpha(H)\le a,\qquad e(H)\le f_r(ar+1),
$$


and having at least $r-1$ nonedges on every $r+1$ vertices.

### Quantitative Turán lemma

Let $t_a(n)=\binom n2-T_a(n)$. A $K_{a+1}$-free graph $F$ has
a partition into $a$ parts with at most $t_a(n)-e(F)$ edges inside
the parts.

To prove this, induct on $a$, the case $a=1$ being immediate. Take a
maximum-degree vertex $v$, put $A=N_F(v)$, $d=|A|$, and

$B=V(F)\setminus A$. Partition $F[A]$ into $a-1$ parts by
induction and take $B$ as the last part. The number of internal edges
is at most


$$
 t_{a-1}(d)-e(F[A])+e(F[B]).
$$


Since


$$
 e_F(A,B)+2e(F[B])\le d(n-d),\qquad
 t_{a-1}(d)+d(n-d)\le t_a(n),
$$


this is at most $t_a(n)-e(F)$, as required. The first inequality uses
maximum degree; the second uses an $a$-partite graph with one part of
size $n-d$.

### Almost complete parts

Set (n=ar+1) and $D=e(H)-T_a(n)\ge0$. The full-set edge bound gives


$$
 D\le\frac{a^2-a-2}{2}r+a\le\frac{a^2r}{2}.                \tag{8}
$$


Apply the quantitative lemma to the complement of $H$. It gives a
partition $P_1,\ldots,P_a$ with at most $D$ internal nonedges in

$H$. Write $p_i=|P_i|$, and let $X$ count the edges of $H$
between different parts. Comparing the internal edge count with

$T_a(n)$ gives


$$
 X\le2D\le a^2r,\qquad
 \sum_i(p_i-r)^2\le1+4D\le1+2a^2r.                        \tag{9}
$$


In particular $p_i\ge3r/4$, since $r\ge256a^6\ge64a^2$.

Call a vertex bad if it has more than $r/4$ neighbors outside its own
part. If $B$ is the bad set and $b=|B|$, then


$$
 b\le8a^2.                                                  \tag{10}
$$


Each $C_i=P_i\setminus B$ is a clique. Otherwise, take nonadjacent

$u,v\in C_i$. In every other original part $P_j$, at least $r/4$
vertices avoid both $u,v$. Choose one uniformly and independently
from each such set. The expected number of edges among the choices is
at most


$$
 \frac{X}{(r/4)^2}\le\frac{16a^2}{r}<1.
$$


Some choice is therefore independent, and together with $u,v$ gives
an independent $(a+1)$-set, a contradiction.

### Assigning the exceptional vertices

The local nonedge condition implies $\omega(H)\le r$. Hence, putting

$d_i=r-|C_i|\ge0$, we have the exact identity


$$
 \sum_i d_i=b-1.                                           \tag{11}
$$


For each bad vertex $z$, some $C_i$ contains at most

$\sqrt X\le a\sqrt r$ nonneighbors of $z$. If not, a random
choice of one nonneighbor in every $C_i$ would again have expected
number of edges less than one, giving an independent $(a+1)$-set
with $z$. When $X=0$, this statement follows directly.

Assign every bad vertex to one such clique. By $11$, some $C_i$
receives at least $d_i+1$ vertices. Choose exactly $k=d_i+1$ of
them. Together with $C_i$ they form an $r+1$-set having at most


$$
 ka\sqrt r+\binom k2
 \le8a^3\sqrt r+32a^4
 \le\frac r2+\frac{r}{8a^2}
 \le\frac{17r}{32}<r-1
$$


nonedges. This is the required contradiction. $\square$

The proof was checked independently during this investigation. It needs
neither a fixed graph template nor a bounded number of components.

### Consequence for minimal induced subgraphs

Every color graph has $|G_i|>r\alpha(G_i)$. Choose an induced subgraph

$H$ minimal subject to $|H|>r\alpha(H)$, and put

$a=\alpha(H)$. Deleting one vertex shows $|H|=ar+1$: minimality
gives $|H|-1\le r\alpha(H-v)\le ra$. The case $a=1$ is impossible
by the local nonedge condition. The theorem proves $1$, and hence


$$
 \alpha(H)>\left(\frac r{256}\right)^{1/6}.                 \tag{12}
$$


This leaves a substantial gap: the argument does not control such
subgraphs when their independence number grows with $r$.

## 4. No nearly spanning packing of large monochromatic cliques

The following elementary transversal fact is useful. Suppose $m$ disjoint
parts each have at least $m-1$ vertices, with a matching between each
pair of parts. If there is no independent transversal, every part has
exactly $m-1$ vertices, and the cross edges are $m-1$ disjoint
transversal $K_m$'s.

Indeed, a part of size at least $m$ can be selected last in a greedy
transversal. For the remaining assertion, fix a vertex $x$, delete its
neighbors in the other parts, and induct on $m$. Each resulting part
must have size $m-2$, so all original matchings are perfect. Deleting
the two neighbors of $x$ from any one of these perfect matchings must
leave it perfect, so those neighbors are matched to each other. This
makes all matchings consistent and proves the assertion.

Suppose a color graph contains $r$ disjoint $K_r$'s, leaving one vertex

$v$. By $5$, their cross graphs are matchings. Remove the neighbors of

$v$ from each clique. The resulting parts have size at least $r-1$
and cannot have an independent transversal. The preceding fact therefore
forces at least


$$
 (2r-1)\binom r2+r                                         \tag{13}
$$


edges in this color.

Every other color has at least


$$
 T_r(r^2+1)+r-1=r\binom r2+2r-1
$$


edges by $6$, because $r$ cliques of size at most $r$ cannot cover

$r^2+1$ vertices. Summing these bounds exceeds the total number of
edges by


$$
 \frac{(r-1)(r-2)}2>0.
$$


This proves the claimed packing obstruction. Further propagation and
absorption lemmas around a single monochromatic $K_r$, with the precise
remaining gap, were recorded in a companion note that is not retained.

## 5. How far an affine construction must be changed

Use the paper's affine plane of order $r$: $r-1$ parallel classes have
separate colors, and the remaining two classes share a color. Add a vertex,
and suppose some old edges are recolored to produce a counterexample.

Let $A_i$ be the old edges changed **into** a single-class color $i$.
The packing theorem forces at least one old color-$i$ edge to be deleted;
otherwise the $r$ original lines remain disjoint color-$i$ $K_r$'s.

Here is the main local counting mechanism. If a deleted edge (xy) lies on
an old line $L$, and $|A_i|\le2r-2$, some other old line $B$ must
be completely covered by the new color-$i$ neighborhoods of $x,y$.
Otherwise take one common nonneighbor on each other line. If $t_1,t_2$
are the two smallest residual sizes, the required added edges number at
least


$$
 2r-t_1-t_2+t_1t_2\ge2r-1.
$$


The line $B$ must itself lose an old edge, by $5$. Applying the same
argument to a deleted pair on $B$ forces mutual coverage of $L,B$,
requiring at least $2r-2$ added edges.

At equality, the additions form two pairs of stars between $L$ and $B$,
with a matching between their centers. For $r\ge5$, either the two lines
span $r^2+r-4>r^2$ edges in this color, contradicting $4$, or swapping
two centers produces two new $K_r$'s. In the latter case, all other old
lines are intact, contradicting the packing theorem again. The full
equality classification was written out in a companion note that is not
retained.

Thus every single-class color receives at least $2r-2$ old edges, and
at least $2r-1$ when $r\ge5$. Every recolored old edge is counted only
in its new color, proving


$$
 M\ge2(r-1)^2\quad(r\ge3),\qquad
 M\ge(r-1)(2r-1)\quad(r\ge5).                               \tag{14}
$$


These are edit-distance obstructions, not a reduction of an arbitrary
counterexample to affine geometry.

## 6. Remaining obstruction and preserved records

A sufficient, still unproved, one-color statement would be that no graph
can satisfy all of


$$
 |G|=r^2+1,\quad \alpha(G)\le r,\quad
 e(G)\le\frac{r(r^2+1)}2,\quad
 e(G[U])\le f_r(|U|)\quad\text{for every }U.                 \tag{15}
$$


A minority color of a counterexample would satisfy $15$. The work here
does not establish this implication, nor is it known here whether $15$
itself is feasible. Its hypotheses cannot simply be dropped:

* A companion note (not retained) gives an infinite family satisfying
  the minority edge bound, independence bound, and all $r+1$-vertex
  density bounds, but failing larger hereditary bounds.
* Another companion note (not retained)
  gives graphs satisfying all hereditary bounds and the independence
  bound, but exceeding the minority edge budget.

The following additional rigorous construction obstructions were preserved:

* Not retained: no $r$ edge-disjoint spanning
  witnesses each consisting of $r-2$ cliques and an independence-two
  component. This permits leftover uncolored edges.
* Not retained: if each actual
  color graph consists of $r-a$ components $K_r$ and one component on
  $ar+1$ vertices of independence at most $a$, then necessarily

  $$
  r^2-(a^2-3a+1)r-4a+2\le0.
  $$

* Not retained: further odd-cycle and
  bounded-template witness-packing obstructions.

The unresolved task is to exclude structures whose independence budget and
complexity grow with $r$, or to construct and verify a coloring using such
structures. None of the completed arguments supplies that last step.

## Supplied sources

* T. F. Bloom, *Erdős Problem #617*, recorded on the
  [problem page](../../../problems/extremal_graph_theory/E0617/_index.md).
* P. Erdős and A. Gyárfás, *Split and balanced colorings of complete graphs*,
  Discrete Mathematics **200** $1999$, 79–86, supplied in
  [source.md](../../../../library/extremal_graph_theory/erdos_gyarfas_1999_split_balanced_colorings_complete_graphs/_index.md).

No other research source was consulted.

## Addendum: sharper claims, failed approaches, and uncertainties

The pair-density improvement below has had its cap calculation, dependency
condition, conditional-probability argument, and constants checked. It improves
the asymptotic exponent in the main report from 1/6 to 1/5, without resolving
the growing-independence regime.

### Appendix A. Improving the exponent using the two-clique caps

**Theorem.** If $|H|=ar+1$, $\alpha(H)\le a$, $a\ge2$, and $e(H[U])\le f_r(|U|)$
for every subset $U$, then


$$
 r<4096a^5.                                             \tag{12}
$$


This improves the asymptotic exponent in the main record from $1/6$ to $1/5$.
Unlike the first quantitative theorem, it uses the hereditary caps on unions of
two of the large cliques produced by stability.

### A finite probability lemma

Suppose events $E_1,\ldots,E_m$ have a dependency graph of maximum
degree at most $D-1$, with $D\ge1$; specifically, each event
is independent of every joint collection of events not adjacent to
it. If $\Pr(E_i)\le1/(4D)$ for every $i$, then
$\Pr(\bigcap_i\overline E_i)>0$.

Here is the usual elementary proof, included so no external result
is needed. Put $x=1/(2D)$. Bernoulli's inequality gives
$(1-x)^{D-1}\ge1/2$, and therefore
$\Pr(E_i)\le x(1-x)^{D-1}$. Induct on the size of a set $S$
not containing $i$ to prove


$$
 \Pr(E_i\mid\text{no event in }S\text{ occurs})\le x.
$$


Separate $S$ into the neighbors of $i$ and its nonneighbors.
Conditional on avoidance of the nonneighbors, the numerator is at
most $\Pr(E_i)$, by independence; the denominator for additionally
avoiding the neighbors is at least $(1-x)^{D-1}$, by the induction
hypothesis and the chain rule. This proves the conditional bound.
The chain rule then gives a strictly positive lower bound
$(1-x)^m$ for avoiding all events.

### Proof of (12)

Suppose instead that $r\ge4096a^5$. Repeat the stability argument of Section 3
through the clique decomposition and capacity identity; those steps require only
$r\ge64a^2$, not $r\ge256a^6$. Thus there are $a$ disjoint cliques $C_i$
of order $r-d_i$, together with a set $B$ of $b\le8a^2$ other vertices,
and


$$
 d_i\ge0,\qquad \sum_i d_i=b-1.
$$


Let $X_{ij}$ be the number of edges between $C_i$ and $C_j$.
The order $2r-d_i-d_j$ of their union lies between $r$ and
$2r$. Its cap says that it has at least
$(r-1)(r-d_i-d_j)$ nonedges. All nonedges are between the two
cliques, so


$$
 \begin{aligned}
 X_{ij}
 &\le (r-d_i)(r-d_j)-(r-1)(r-d_i-d_j)\\
 &=r+d_id_j-d_i-d_j\\
 &\le r+16a^4\le2r.                                    \tag{13}
 \end{aligned}
$$


For a fixed $z\in B$, let $M_i$ be its nonneighbors in
$C_i$. If every $|M_i|>4\sqrt{ar}$, choose one vertex
uniformly and independently from each $M_i$. For each pair
$i,j$, let $E_{ij}$ be the event that the two chosen vertices
are adjacent. By (13),


$$
 \Pr(E_{ij})\le\frac{2r}{|M_i||M_j|}<\frac1{8a}.
$$


The event $E_{ij}$ depends only on the choices in parts $i,j$,
and hence is independent of every joint collection of events whose
pairs avoid $i,j$. Its dependency degree is at most $2a-4$.
Take $D=2a-3$. Since $1/(8a)\le1/(4D)$, the probability
lemma supplies a choice with no edges. Adding $z$ gives an
independent $(a+1)$-set, a contradiction.

Consequently every $z\in B$ has at most $4\sqrt{ar}$
nonneighbors in some $C_i$. Assign it to one such clique.
Because $b=1+\sum_i d_i$, some $C_i$ receives at least
$d_i+1$ assignments. Choose $k=d_i+1$ of them. Their union
with $C_i$ is an $(r+1)$-set with at most


$$
 4k\sqrt{ar}+\binom k2
 \le32a^{5/2}\sqrt r+32a^4
 \le\frac r2+\frac{r}{128a}
 <r-1
$$


nonedges, because $k\le8a^2$, $r\ge4096a^5$, and
$a\ge2$. This contradicts the cap and proves (12).
$\square$

Thus every minimal ratio-violating induced core in a hypothetical
coloring satisfies both


$$
 a>\left(\frac r{256}\right)^{1/6},\qquad
 \boxed{\quad a>\left(\frac r{4096}\right)^{1/5}.\quad}   \tag{14}
$$



The central verified restrictions therefore give both lower bounds on the
independence number of a minimal core. The proof of the 1/5 bound uses all
hereditary caps, specifically those on unions of two of the extracted cliques;
the 1/6 proof only needs the full-set and (r+1)-set caps. Neither proof uses the
global minority edge budget.

### Appendix B. Explicit failure of the first minority-only approach



For every integer $k\ge3$, put $r=5k$. There is a graph $G$ such that


$$
 |V(G)|=r^2+1,\qquad \alpha(G)=r,
 \qquad |E(G)|\le \frac{r(r^2+1)}2,
$$


and every set of $r+1$ vertices has at least $r-1$ nonedges.
Thus these conditions by themselves cannot prove Problem 617.

Construct $G$ as the disjoint union of $r-2$ copies of $K_r$ and a
clique blow-up $H$ of the cycle $C_5$, whose five clique classes have
sizes $2k+1,2k,2k,2k,2k$. Consecutive cycle classes are complete to one
another and other pairs of classes are anticomplete. Clearly
$\alpha(H)=2$, $|V(H)|=2r+1$, and


$$
 |E(H)|=30k^2+k,\qquad
 |E(G)|=\frac{125k^3-15k^2+12k}{2}.
$$


The difference between the allowed edge bound and the displayed edge count
is $(15k^2-7k)/2\ge0$.

Here is a full verification of the local nonedge condition. If a set of
$r+1$ vertices is not contained in $H$, all its intersections with
components have at most $r$ vertices. The complete multipartite graph
between those intersections has at least $r$ edges: among partitions of
$r+1$ with every part at most $r$, the sum of squares is maximized by
$(r,1)$. All these pairs are nonedges of $G$.

It remains to minimize the number of nonedges in $H$ on $5k+1$
vertices. Let $x_i$ be the number chosen in the $i$-th class. The
objective is


$$
 F(x)=\sum_{i\pmod5}x_ix_{i+2},
 \qquad 0\le x_i\le a_i,\quad \sum_i x_i=5k+1,
$$


where $(a_0,\ldots,a_4)=(2k+1,2k,2k,2k,2k)$.
A minimum occurs with all but at most one coordinate at an endpoint.
Indeed, if two coordinates are interior, move equal amounts from one to
the other. The resulting function is linear when that pair is not a
nonedge-class pair, and concave quadratic when it is. One endpoint of the
allowed interval does not increase the objective and puts another
coordinate at an endpoint. Iterate. Since
$2(2k+1)<5k+1<3(2k)$ for $k\ge3$, the resulting vector has exactly
two full classes and one partial class. If the full classes are
nonconsecutive, their product alone is at least $4k^2$. If they are
consecutive, the third class is nonconsecutive to at least one of them.
The partial class has at least $k$ vertices and the full class at least
$2k$; hence $F\ge2k^2$. Equality is attained by choosing the large
class, a consecutive small class, and $k$ vertices of the next small
class. Finally $2k^2\ge5k-1=r-1$ for $k\ge3$.

This is not a coloring counterexample. The next stronger necessary
condition rules out its proposed minority graph immediately.


### Appendix C. Explicit failure when the minority budget is omitted



For every prime $r\ge3$ there is a graph with $r^2+1$ vertices,
independence number $r$, clique number $r$, and every hereditary
cap, but with too many edges to be a minority color.

Take an $r\times r$ grid, make every row a clique and every column
except one distinguished column a clique, and add a vertex $v$
adjacent precisely to the $r$ vertices of the distinguished column.
Call this graph $G$, and let $R$ be the full rook graph on the old
grid (all rows and all columns complete).

An independent set not using $v$ has at most one vertex in each row.
An independent set using $v$ avoids the distinguished column and
has at most one vertex in each of the other $r-1$ columns. Thus
$\alpha(G)\le r$; the distinguished column itself shows equality.
The clique number is $r$, as follows directly from the row-column
description (and $v$ has an independent neighborhood).

To verify all caps, identify the grid with $\mathbb F_r^2$. Its
nonhorizontal, nonvertical affine directions give $r-1$ pairwise
edge-disjoint graphs, each a union of $r$ cliques of order $r$,
which partition the complement of $R$. Each such graph has
independence number at most $r$, so on a $t$-set each contributes
at least $T_r(t)$ edges. It follows that


$$
 e(R[W])\le f_r(|W|)\quad\text{for every grid subset }W.
$$


For a set $U$ containing $v$, put $W=U\setminus\{v\}$, and
let $h$ count its distinguished-column vertices. Then


$$
 e(G[U])=e(R[W])+h-\binom h2\le f_r(|W|)+1.
$$


If $|W|=qr+s\ge1$, $0\le s<r$, then


$$
 f_r(|W|+1)-f_r(|W|)=q+s\ge1.
$$


The single-vertex set is immediate, and sets not containing $v$
are subgraphs of the rook graph. Thus every hereditary cap holds.
The edge count is


$$
 e(G)=r\binom r2+(r-1)\binom r2+r
      =\frac{r(r^2+1)}2+\frac{r(r-1)(r-2)}2.
$$


This graph meets equality in the lower bound of Section 1. Its excess
above the minority threshold explains exactly why it is not a
solution to the full one-color feasibility problem.


### Appendix D. The unfinished absorption mechanism

This extract retains local equation numbers from multicolor_structure.md. In
particular, its reference to (2) is the external-neighbor bound, equation (5) in
the main record.



The following local structure may provide a route beyond Theorem 3.
Fix a color-$i$ clique $C$ of size $r$. For each
$j\neq i$ and $c\in C$, define

$$
A_{j,c}=\{v\notin C:N_{G_j}(v)\cap C=\{c\}\},
\qquad Q_{j,c}=\{c\}\cup A_{j,c}.
$$

Every $Q_{j,c}$ is a color-$j$ clique: if $x,y\in A_{j,c}$
were nonadjacent in that color, then
$(C\setminus\{c\})\cup\{x,y\}$ would be a color-$j$
independent set of size $r+1$.

For each outside vertex, its neighborhoods into $C$ in colors
$j\neq i$ are nonempty. At most one such neighborhood has size
two, and all others have size one; alternatively all have size one and
the remaining edge has color $i$. Let

$$
D_j=\{v\notin C:|N_{G_j}(v)\cap C|=2\},\qquad t_j=|D_j|.
$$

The sets $D_j$ are pairwise disjoint. The $r$ disjoint cliques
$Q_{j,c}$ cover all vertices except $D_j$. Since each has size
at most $r$,

$$
\delta_{j,c}:=r-|Q_{j,c}|\geq0,
\qquad \sum_{c\in C}\delta_{j,c}=t_j-1.
\tag{4}
$$

In particular $t_j\geq1$. There is some $j\neq i$ with
$t_j\leq r$, because

$$
\sum_{j\neq i}t_j\leq r^2-r+1<(r-1)(r+1).
$$


**Lemma 4.** The existence of a monochromatic $K_r$ forces a
monochromatic $K_r$ in a different color.

*Proof.* If every $Q_{j,c}$ had size at most $r-1$, then
$\sum_c\delta_{j,c}\geq r$, so (4) would give $t_j\geq r+1$
for all $j\neq i$, contradicting the last displayed inequality.
$\square$

**Lemma 5 (absorption at a full clique).** Fix $j\neq i$, and let
$v\in D_j$ have its two color-$j$ neighbors in $C$ at
$a,b$. If $|Q_{j,a}|=r$, then $v$ is color-$j$
adjacent to every vertex of $Q_{j,b}$.

*Proof.* By (2), the only color-$j$ neighbor of $v$ in
$Q_{j,a}$ is $a$. Suppose $y\in Q_{j,b}$ is nonadjacent
to $v$ in color $j$. For any $x\in Q_{j,a}\setminus\{a\}$,
if $xy$ also lacked color $j$, then

$$
\{v,x,y\}\cup(C\setminus\{a,b\})
$$

would be a color-$j$ independent $(r+1)$-set. Consequently
$y$ is adjacent in color $j$ to all $r-1$ such vertices
$x$. They form a color-$j$ clique of order $r$ together
with $y$. But the external vertex $a$ has $r-1\geq2$
color-$j$ neighbors in this clique, contradicting (2).
$\square$

One can encode $D_j$ as a multigraph on $C$, with an edge
$ab$ for each exception whose two neighbors are $a,b$.
Formula (4) gives total available clique capacity $t_j-1$ for
$t_j$ exceptions. Lemma 5 forces an exception incident with a full
clique toward its other endpoint.

For $r\geq4$, the first round of such absorptions can be made
simultaneously. Fix $b$, and let $v,w$ be exceptions supported on
$\{a,b\}$, $\{c,b\}$, respectively, with both $Q_{j,a}$
and $Q_{j,c}$ full. They are both complete to $Q_{j,b}$ by
Lemma 5. If they were nonadjacent, then for $a=c$ one could choose
$x\in Q_{j,a}\setminus\{a\}$ and obtain the independent set
$\{v,w,x\}\cup(C\setminus\{a,b\})$. For $a\neq c$,
choose $x\in Q_{j,a}$ avoiding both $v,w$, and then
$y\in Q_{j,c}$ avoiding $v,w,x$. The first choice has at least
$r-2$ possibilities. Before avoiding $x$, the second has at
least $r-2\geq2$, and (2) says $x$ forbids at most one of them.
Then
$\{v,w,x,y\}\cup(C\setminus\{a,b,c\})$ is an independent
$(r+1)$-set. Thus all first-round exceptions targeted at the same
block are pairwise adjacent and can be absorbed there together.

This does not yet yield a complete absorption argument. A support
multigraph can have components supported entirely on deficient cliques.
Also, after the first round, newly enlarged blocks contain vertices
adjacent to previously processed anchors, so repeating the preceding
independent-set arguments requires additional justification.

There is a useful exact reduction that does not depend on successful
absorption. For a component $B\subseteq C$ of the support
multigraph, let $W_B$ consist of its core blocks $Q_{j,c}$,
$c\in B$, and all exceptions whose support is in $B$. Then

$$
\alpha(G_j[W_B])\leq |B|.
\tag{5}
$$

Every vertex of $W_B$ is color-$j$ nonadjacent to
$C\setminus B$, so a violation of (5) would extend to an independent
$(r+1)$-set. The sets $W_B$ partition the entire vertex set.
Consequently deleting all color-$j$ edges between distinct support
components preserves the bound $\alpha\leq r$. An isolated
support vertex produces a clique component, and a two-vertex support
component produces a graph with independence number at most two. The
unresolved general case permits support components with independence
budget at least three, or several nontrivial components.


### Appendix E. Remaining global-stability attempt

This extract retains its own local equation and section numbering. The exact
equality classification is proved; its extension to near equality is explicitly
unresolved.

## Global stability and independent-transversal covers

This note records the deductions obtained on global stability.
It does not establish the proposed one-color infeasibility theorem.

Write

$$
 T_r(t)=r\binom q2+sq\quad(t=qr+s, 0\le s<r),\qquad
 f_r(t)=\binom t2-(r-1)T_r(t).
$$

The remaining system is a graph $G$ on $r^2+1$ vertices with
$\alpha(G)\le r$, $e(G)\le r(r^2+1)/2$, and
$e(G[U])\le f_r(|U|)$ for every vertex set $U$.

## 1. Minimum degree in a minimal ratio obstruction

**Lemma.** Suppose every proper induced subgraph $J$ of a graph $H$
satisfies $|J|\le r\alpha(J)$, whereas $|H|>r\alpha(H)$.
Put $a=\alpha(H)$. Then

$$
 |H|=ar+1,\qquad \delta(H)\ge r.
$$


Deleting a vertex gives $|H|-1\le ra$, proving the order identity.
For any vertex $v$, the induced graph
$J=H-N_H[v]$ has independence number at most $a-1$, since an
independent set in $J$ can be joined to $v$. Minimality therefore
gives

$$
 ar-d_H(v)=|J|\le r\alpha(J)\le r(a-1),
$$

and hence $d_H(v)\ge r$.

Consequently, if this core also satisfies the hereditary caps, then

$$
 e(H)\ge \frac{r(ar+1)}2.
$$

When $a=2$, the upper cap is $e(H)\le f_r(2r+1)=r^2+2$, so
$r\le4$. Thus for every $r\ge5$, a minimal ratio obstruction
has independence number at least three. This is a small core exclusion,
not a proof of another fixed value of the coloring conjecture. For
$a\ge3$, comparison with the total cap alone gives no contradiction.

## 2. Exact equality in the transversal union bound

Let $B_1,\ldots,B_k$ be pairwise disjoint nonempty vertex sets, with
$b_i=|B_i|$, and let $Q$ be a graph whose edges join different
sets. Suppose there is no independent transversal: every choice of one
vertex from each $B_i$ contains an edge of $Q$. If $m_{ij}$
counts the edges between $B_i$ and $B_j$, then

$$
 \sum_{i<j}\frac{m_{ij}}{b_i b_j}\ge1.                 \tag{1}
$$

This follows by choosing a uniformly random transversal and bounding the
probability that it contains an edge by the expected number of its
edges.

The equality case has a complete elementary description.

**Lemma.** Equality holds in (1) if and only if there is a central part
$B_c$, and a map
$j:B_c\longrightarrow [k]\setminus\{c\}$, such that the entire
edge set of $Q$ consists, for each $x\in B_c$, of all edges
from $x$ to $B_{j(x)}$.

**Proof.** Under equality, the random transversal has at least one edge
always and expected edge count one. It therefore has exactly one edge
always. Thus the events of containing two distinct specified edges are
disjoint.

Consider the graph on the part indices whose pairs support edges of
$Q$. Any two of its edges intersect: edges on four different parts
would occur together in some transversal. A pairwise intersecting family
of two-element sets is either a star or is contained in a triangle.
If all three pairs of a triangle occur, then, at each of its parts, the
vertices incident to edges to the two other parts must form disjoint
sets; otherwise two such edges occur together in a transversal. Label
the three parts $A,B,C$. Choose a vertex of $A$ used on an
$AB$-edge, a vertex of $B$ used on a $BC$-edge, and a vertex
of $C$ used on a $CA$-edge. These three vertices have no edges
between them, by the disjointness just proved. There are no supported
pairs outside this triangle, so arbitrary choices in the other parts
give an independent transversal, a contradiction. Hence all supported
pairs share a central part $B_c$.

For a fixed $x\in B_c$, neighbors can lie in at most one other
part: neighbors in two other parts again give a transversal with two
edges. Moreover $x$ must be adjacent to every vertex of that other
part; otherwise select a nonneighbor there, and arbitrary vertices in
the remaining parts, to obtain an independent transversal. Every
$x$ needs such a part. This proves necessity. Conversely, every
transversal in the asserted construction has precisely its unique edge
joining its selected central vertex $x$ to its selected vertex in
$B_{j(x)}$. This proves equality. $\square$

For equal part sizes $b$, a transversal obstruction therefore needs
at least $b^2$ edges, and the constructions just described are
exactly those attaining $b^2$.

## 3. Application to a stability partition, and the unresolved step

Suppose a stability partition $P_1,\ldots,P_r$ of $G$ has been
chosen, and $u,v\in P_i$ are nonadjacent. For each $j\ne i$,
put

$$
 B_j=P_j\setminus(N_G(u)\cup N_G(v)).
$$

If all these sets are nonempty, the graph of edges between them has
no independent transversal: such a transversal together with $u,v$
would be an independent $(r+1)$-set. Thus (1) applies to these
specific available sets. Likewise, fixing any vertex and taking its
nonneighbors in all parts yields a transversal obstruction whenever
adjoining the fixed vertex would exceed the independence bound.

The global stability estimates available in the investigation are

$$
 D=e(G)-T_r(r^2+1)\le\frac{r(r-1)}2,
$$

with a partition for which the number $I$ of internal nonedges is
at most $D$, the number $M$ of crossing edges is at most
$2D$, and

$$
 \sum_i(|P_i|-r)^2\le 2r^2-2r+1.
$$

They place the relevant transversal weights near, but not necessarily
at, the threshold one. Unequal part sizes and the neighborhoods removed
in defining the $B_j$'s can produce nonnegligible variation in their
sizes. The exact equality classification above does not control this
near-equality regime. No quantitative conclusion was proved that
absorbs its star systems into clique parts, or forces an induced
ratio-violating core of bounded independence number.

In particular, the minimum-degree observation does not transfer the
global minority edge bound to a minimal core: the vertices outside the
core can have average degree below $r$. It is not valid to infer
that such a core is $r$-regular merely from the global edge bound.
This is a specific obstruction to combining the core lemma with
regular-graph coloring arguments.


### Appendix F. Unproved ideas that are not used

The averaged independence inequality
$\alpha(G)\ge 2|G|/(\overline d(G)+\omega(G)+1)$ was considered. It was neither
proved nor disproved here, and is not used in any claimed result. Small checks
do not justify this inequality. A maximum-degree analog, even if available,
would not justify replacing maximum degree by average degree.

An additive edge-charge argument for the exceptions in a maximum-independent-set
decomposition also failed: the same cross edge can block the transversals
associated with several different exceptions. No injective charging rule was
established.

A possible further refinement, not developed or claimed, is to choose the
stability partition minimizing internal complement edges. Local optimality
compares a vertex's nonneighbors in its own part with its nonneighbors in other
parts. No argument turning this observation into a stronger final conclusion was
completed.

The longer bounded-template witness arguments (not retained) are not
prerequisites for the central theorem and were not re-audited. Actual
color-component decompositions and edge-disjoint witness subgraphs with leftover
edges must not be interchanged.

## Final status

The quantified Erdős problem remains unresolved in this independent
investigation. All conclusions above are necessary conditions, construction
obstructions, or explicitly labeled incomplete approaches. There is no verified
coloring counterexample, and no proof excluding cores whose independence number
and complexity grow with r.

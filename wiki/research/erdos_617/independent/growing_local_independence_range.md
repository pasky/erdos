---
name: research/erdos_617/independent/growing_local_independence_range
title: 'Independent research record: Erdős Problem 617'
desc: Fourth unverified isolated investigation, preserved below the metadata; checked conclusions are in independent-comparison.
tags: [unverified, archive]
sources: []
created: 2026-09-22T15:19:31Z
updated: 2026-09-22T15:21:22Z
---


# Independent research record: Erdős Problem 617

***

This record collects the investigation and the specific failed approaches
below. It records partial results, not a solution.

## Status and scope

**The problem is not resolved here.** No counterexample coloring has been
constructed, and the argument below does not prove the assertion for every
$r$. It gives parameter-uniform restrictions on a hypothetical
counterexample, including a growing range of local independence bounds.

The only external material used was the supplied
[problem page](../../../problems/extremal_graph_theory/E0617/_index.md) and
[Erdős--Gyárfás paper](../../../../library/extremal_graph_theory/erdos_gyarfas_1999_split_balanced_colorings_complete_graphs/_index.md).
No web searches or other research notes were consulted. The proofs below are
developed from the problem; the complement form of Turán's theorem is the
standard extremal result also used in the supplied paper. No additional isolated
value of $r$ was investigated.

Here are the main established conclusions. In any hypothetical
counterexample:

1. Every $2r+1$-vertex set has an independent triple in each color graph.
2. For $r\ge6$, every $3r+1$-vertex set has an independent four-set in
   each color graph. The exact boundary at $2r$ vertices is rigid:
   independence number at most two forces two monochromatic $K_r$'s.
3. More generally, every $kr+1$-vertex set has independence number at
   least $k+1$ in every color whenever

   $$
   r\ge256k^6(1+\log k)^3.
   \tag{A}
   $$

   Thus the excluded local independence numbers grow on the scale
   $r^{1/6}/\sqrt{\log r}$.
4. No color contains $r$ vertex-disjoint monochromatic $K_r$'s, even
   when arbitrary additional edges of that color are allowed.
5. Around any monochromatic $K_r$, each other color must have an
   unbounded number of double-neighbor exceptions: at least
   $(r/4)^{1/4}$.

The first three statements form the main line of attack. The exact
unproved endpoint is identified in Section 6.

## 1. Basic consequences of a counterexample

Fix $r\ge3$, put $N=r^2+1$, and suppose that an edge coloring of
$K_N$ with colors $1,\ldots,r$ has every color on every
$(r+1)$-vertex set. Let $G_i$ be its color-$i$ graph. Then

$$
\alpha(G_i)\le r.
\tag{1}
$$

There is no monochromatic $K_{r+1}$. Moreover, for every
$(r+1)$-set $S$,

$$
e(G_i[S])\le\binom{r+1}{2}-(r-1)=\binom r2+1.
\tag{2}
$$

The reason is that the other $r-1$ colors must each occupy an edge.

If $A$ is a color-$i$ $K_r$ and $x\notin A$, all other colors
must occur on the $r$ edges from $x$ to $A$. Consequently

$$
|N_i(x)\cap A|\le1.
\tag{3}
$$

In particular, edges of color $i$ between two disjoint color-$i$
$K_r$'s form a matching.

For a set $W$ of order $kr+1$, where $1\le k\le r$, (1) and
Turán's theorem imply that each color has at least

$$
r\binom k2+k
$$

edges on $W$. The minimizing graph is a union of $r-1$ cliques of
order $k$ and one of order $k+1$. Subtracting the contributions of
the other colors gives

$$
e(G_i[W])\le E_k:=
\frac{k}{2}\bigl(r^2+(k-2)r+2\bigr).
\tag{4}
$$

Similarly,

$$
|W|=2r\quad\Longrightarrow\quad e(G_i[W])\le r^2.
\tag{5}
$$

These are simultaneous-color constraints, not estimates for an arbitrary
single graph of small independence number.

Write $P_k$ for the assertion that every set of $kr+1$ vertices has
independence number at least $k+1$ in every specified color. Thus $P_1$
follows from the exclusion of a monochromatic $K_{r+1}$, and $P_r$
would contradict (1) and solve the problem.

## 2. Two exact local steps

### Proposition 1: $P_2$ holds for every $r\ge3$

Suppose $H=G_i[W]$, $|W|=2r+1$, has independence number at most two.
The nonneighbors of any vertex form a clique, so there are at most $r$
of them. Hence $\delta(H)\ge r$.

If $d_H(v)=r$, its nonneighbors form a clique $A$ of order $r$.
If two vertices $x,y\in N_H(v)$ were nonadjacent, (3) would leave a
vertex of $A$ nonadjacent to both, since $r\ge3$. This gives an
independent triple. Thus $N_H(v)$ is a clique and, together with $v$,
forms a forbidden $K_{r+1}$.

It follows that $\delta(H)\ge r+1$. But (4) gives

$$
\frac{(2r+1)(r+1)}2\le e(H)\le r^2+2,
$$

which is impossible for $r\ge3$. This proves $P_2$.

### Lemma 2: rigidity at $2r$ vertices

For $r\ge6$, if $|W|=2r$ and $\alpha(G_i[W])\le2$, then $W$
partitions into two color-$i$ $K_r$'s, with matching cross edges.

**Proof.** Put $H=G_i[W]$, and first suppose $H$ contains no $K_r$.
Its complement $F$ is triangle-free. Every neighborhood in $F$ is a
clique in $H$, so $\Delta(F)\le r-1$. On the other hand, (5) gives

$$
e(F)\ge\binom{2r}{2}-r^2=r(r-1).
$$

Thus $F$ is $(r-1)$-regular.

It is not bipartite: one side of a bipartition would have at least $r$
vertices and give a $K_r$ in $H$. Take a shortest odd cycle $C$ in
$F$, of length $\ell\ge5$. It has no chord, and every vertex outside
it has at most two neighbors on it. Indeed, with three or more neighbors,
the cyclic gaps between consecutive neighbors all have length at least
two, and some gap is odd. That odd gap and the two edges to the outside
vertex give a shorter odd cycle; the other gaps have total length at
least four.

Counting incidences with $C$ now gives

$$
\ell(r-1)=\sum_{v\in C}d_F(v)\le2|W|=4r.
$$

Since $\ell\ge5$, this implies $r\le5$, a contradiction.

Therefore $H$ contains a clique $A$ of order $r$. If two vertices
of $W\setminus A$ were nonadjacent, (3) would give an independent
triple with a vertex of $A$. Thus $W\setminus A$ is also a clique.
The cross edges form a matching by (3). $\square$

### Proposition 3: $P_3$ holds for every $r\ge6$

Suppose $H=G_i[W]$, $|W|=3r+1$, has independence number at most
three. By $P_2$, a vertex cannot have at least $2r+1$ nonneighbors,
so $\delta(H)\ge r$. From (4),

$$
\frac{2e(H)}{3r+1}
\le\frac{3r^2+3r+6}{3r+1}<r+1.
$$

Hence some vertex $v$ has degree exactly $r$.

Its $2r$ nonneighbors have independence number at most two. By Lemma 2
they form two cliques $A,B$, each of order $r$. Put $C=N_H[v]$;
then $|C|=r+1$.

If $x,y\in C$ were nonadjacent, choose $a\in A$ nonadjacent to both,
using (3). At most three vertices of $B$ are adjacent to $x,y,a$,
so choose $b\in B$ nonadjacent to all three. The set
$\{x,y,a,b\}$ is independent, a contradiction. Thus $C$ is a
forbidden $K_{r+1}$, proving the proposition.

## 3. A growing range of local independence bounds

### Theorem 4

For every integer $k\ge2$, condition (A) implies $P_k$.
The logarithm is natural.

**Proof.** Induct on $k$; $P_1$ is already established. The threshold
in (A) is increasing, so it also supplies all preceding induction
hypotheses.

Suppose $W$ has order $n=kr+1$, and $G=G_i[W]$ has
$\alpha(G)\le k$. If a vertex had degree at most $r-1$, its
nonneighbors would contain $(k-1)r+1$ vertices and therefore, by
$P_{k-1}$, an independent $k$-set. Adding the vertex contradicts
$\alpha(G)\le k$. Consequently

$$
\delta(G)\ge r.
\tag{6}
$$


Let $H=\overline G$. It is $K_{k+1}$-free and has
$\Delta(H)\le(k-1)r$. Define nonnegative deficits

$$
\delta_x=(k-1)r-d_H(x),\qquad L=\sum_{x\in W}\delta_x.
$$

By (4),

$$
L=2e(G)-rn
\le(k^2-2k-1)r+2k\le k^2r.
\tag{7}
$$


We first find a $K_k$ in $H$ whose vertices have small total deficit.
Let

$$
H_k=\sum_{j=1}^k\frac1j,\qquad h=1+\log k.
$$

After choosing a clique of $t<k$ vertices with total deficit $S$,
their common neighborhood has size at least

$$
(k-t)r+1-t-S.
\tag{8}
$$

This follows by subtracting the union of their nonneighbor sets;
the nonneighbor set here includes the chosen vertex itself.

The assumed bound on $r$ implies

$$
r\ge4k^2H_k+2k.
$$

If $S\le2k^2H_k$, (8) is at least $(k-t)r/2$. By (7), some
vertex in the common neighborhood then has deficit at most

$$
\frac{2k^2}{k-t}.
$$

Greedy selection thus constructs a clique
$C=\{c_1,\ldots,c_k\}$ with

$$
\sum_{j=1}^k\delta_{c_j}\le2k^2H_k.
\tag{9}
$$

The bound assumed during the construction follows at every intermediate
step by summing the same reciprocal bounds.

For $x\in W$, let

$$
I(x)=\{j:x\text{ is not adjacent to }c_j\text{ in }H\},
$$

again treating a vertex as nonadjacent to itself. Every $I(x)$ is
nonempty, since $H$ is $K_{k+1}$-free. Set

$$
A_j=\{x:I(x)=\{j\}\},\qquad
Z=\{x:|I(x)|\ge2\},\qquad z=|Z|.
$$

Each $A_j$ is independent in $H$: an edge between two of its
vertices, together with $C\setminus\{c_j\}$, would form a
$K_{k+1}$. Thus $A_j$ is a clique in $G$, and

$$
|A_j|\le r.
\tag{10}
$$

By (9),

$$
\sum_x|I(x)|
=kn-\sum_jd_H(c_j)
\le kr+k+2k^2H_k.
$$

Each vertex contributes at least one, and each vertex in $Z$ contributes
at least two. Therefore

$$
1\le z\le2k^2H_k+k-1\le3k^2h.
\tag{11}
$$

The lower bound also follows from (10) and $n=kr+1$.

Let $M$ count nonedges of $H$ between distinct $A_j$'s. They are
edges of $G$. Writing $a_j=|A_j|$, we have
$\sum_j(r-a_j)=z-1$, and hence

$$
\sum_j\binom{a_j}{2}
\ge k\binom r2-(r-1)(z-1).
$$

Subtracting these within-class edges from (4) gives

$$
M\le\frac{rk(k-1)}2+k+(r-1)(z-1)
\le4k^2hr.
\tag{12}
$$


Every $x\in Z$ has at most $\sqrt M$ neighbors in some $A_j$.
Otherwise choose independently a uniformly random neighbor of $x$
from each $A_j$. If $M>0$, each cross-class nonedge has probability
strictly less than $1/M$ of being selected. The union bound gives
positive probability that all selected pairs are edges. This creates a
$K_k$ in $N_H(x)$, a contradiction. When $M=0$, the same conclusion
is immediate if all these neighbor sets are nonempty.

Assign each vertex of $Z$ to such a class. The resulting $k$ enlarged
classes partition $kr+1$ vertices, so one class $B$ has at least
$r+1$ vertices. Equations (11) and (12) give

$$
\begin{aligned}
e(H[B])
&\le z\sqrt M+\binom z2\\
&\le6k^3h^{3/2}\sqrt r+\frac92k^4h^2\\
&\le\frac r2<r-1.
\end{aligned}
$$

For the last estimate, the first term is at most $3r/8$ under (A).
The second is at most $r/8$, since (A) implies
$r\ge36k^4h^2$.

But every $(r+1)$-subset of $W$ has at least $r-1$ edges in $H$
by (2). Taking such a subset of $B$ is a contradiction. This proves
the induction. $\square$

### Consequence for connected components

For each color, some connected component $Q$ satisfies

$$
|Q|>r\alpha(Q).
\tag{13}
$$

Otherwise summing over components would contradict
$r^2+1>r\alpha(G_i)$.

If $P_1,\ldots,P_K$ have been proved, any component satisfying (13)
has $\alpha(Q)>K$: if $\alpha(Q)=k\le K$, take $kr+1$ of its
vertices and apply $P_k$. In particular, for $r\ge6$ such a
component has independence number at least four. Theorem 4 makes this
necessary independence number unbounded as $r$ grows.

## 4. A separate clique-factor obstruction

### Theorem 5

No color in a hypothetical counterexample contains $r$ vertex-disjoint
$K_r$'s.

Two elementary rigidity facts are useful.

**Matching-transversal fact.** Suppose a graph has $s$ disjoint vertex
parts, each of size at least $s-1$, and the edges between each pair of
parts form a matching. If there is no independent transversal, all parts
have size $s-1$, and the cross-part edges are $s-1$ disjoint
transversal $K_s$'s.

To prove this, a part of size at least $s$ can be left last in a greedy
selection. If a pair matching misses a vertex, choose that vertex first
and leave the opposite part last; again greedy selection succeeds.
Thus all pair matchings are perfect. If three pair matchings are
inconsistent, there are $a,b,c$ in three parts with $ab,bc$ edges
and $ac$ a nonedge. Choose $a,c$ first and leave $b$'s part last:
the first two choices forbid only one vertex there. This again succeeds.
Hence all matchings are consistent, proving the assertion.

**Maximum-degree equality fact.** A graph on $t(d+1)$ vertices with
maximum degree at most $d$ and independence number at most $t$ is a
disjoint union of $t$ copies of $K_{d+1}$.

The greedy independence bound is $n/(d+1)$. A vertex of smaller
degree, chosen first, makes this bound strictly greater than $t$.
Similarly, if a vertex has two nonadjacent neighbors, choose those
neighbors first: their closed neighborhoods overlap, again improving
the bound strictly. Thus the graph is regular with every neighborhood
a clique, which gives the assertion.

**Proof of the theorem.** Let $B_1,\ldots,B_r$ be the disjoint
color-$i$ cliques, and let $v$ be the remaining vertex. By (3),
each $B_j\setminus N_i(v)$ has at least $r-1$ vertices and the
cross edges form matchings. An independent transversal, together with
$v$, would contradict (1).

The matching-transversal fact therefore gives

$$
X=N_i(v),\quad |X|=r,
$$

with one vertex of $X$ in each $B_j$. The remaining set $A$
partitions into $r-1$ transversal color-$i$ $K_r$'s
$C_1,\ldots,C_{r-1}$.

Fix $j\ne i$. A vertex $y\in A$ has exactly one color-$i$ neighbor
in each $C_a$ not containing it: the vertex in its original $B$
block. By (3) and the requirement to see all colors, it has exactly
one neighbor of each other color there. Thus $G_j[A]$ is
$(r-2)$-regular on $r(r-1)$ vertices. The maximum-degree equality
fact and (1) partition it into $r$ cliques
$D_1,\ldots,D_r$, each of order $r-1$.

Likewise each $x\in X$ has exactly $r-1$ color-$j$ neighbors in
$A$. To prevent an independent transversal of the $D_b$'s together
with $x$, these neighbors must be exactly one whole $D_b$.
Two points of $X$ cannot be assigned the same $D_b$: if their
mutual edge has color $j$, they form a $K_{r+1}$ with $D_b$;
otherwise they and one vertex from every other $D_b$ are independent.
Thus the assignment is bijective.

The vertex $v$ must be color-$j$ complete to at least two $D_b$'s.
If it is complete to none, its nonneighbors give an independent
transversal. If it is complete to exactly one, let $x\in X$ be
assigned that component. The edge $vx$ has color $i$, and
$v,x$ together with suitable nonneighbors of $v$ from the other
components form an independent $(r+1)$-set in color $j$.

Consequently

$$
r^2=d(v)=\sum_jd_j(v)
\ge r+2(r-1)^2>r^2
$$

for $r\ge3$, a contradiction. $\square$

In particular, retaining even one complete parallel class of the
affine-plane construction prevents an extension to $r^2+1$ vertices,
regardless of how edges outside those line-cliques are changed.

## 5. Limits of single-color reductions

The conditions

$$
|V(G)|=r^2+1,\qquad
\alpha(G)\le r,\qquad
e(G)\le\frac{r(r^2+1)}2,
\qquad
e(G[S])\le\binom r2+1\quad(|S|=r+1)
\tag{14}
$$

are mutually compatible for every $r\ge11$.

For an explicit construction, take $r-2$ disjoint $K_r$'s and,
on the remaining $2r+1$ vertices, the complement of an independent
blow-up of $C_5$ with five parts as equal as possible. Its
independence number is $r$. The edge and induced-density calculations
were given in a companion note that is not retained. A more nearly
extremal infinite family was recorded in another companion note that is
not retained.

These graphs are **not counterexample colorings**. Proposition 1 excludes
their $2r+1$-vertex cores immediately. They establish that the
simultaneous-color argument genuinely adds information: the minority
budget and all the $(r+1)$-vertex density inequalities alone do not
suffice.

There is also a quantitative restriction around a monochromatic $K_r$.
Fix such a clique $A$ in color $i$, and another color $j$. Every
vertex outside $A$ has one or two color-$j$ neighbors in $A$.
Let $D_j$ be the double-neighbor vertices, $d=|D_j|$, and let

$$
C_a=\{a\}\cup\{x\notin A:N_j(x)\cap A=\{a\}\},\qquad
t_a=r-|C_a|.
$$

Each $C_a$ is a color-$j$ clique, and counting gives

$$
\sum_{a\in A}t_a=d-1.
\tag{15}
$$

The sets $D_j$, as $j\ne i$ varies, are pairwise disjoint.

A simultaneous packing calculation, proved in detail in
a companion note that is not retained, yields

$$
r-1\le
d\sqrt{\frac{r d(d-1)}2+d-1}+\binom d2.
\tag{16}
$$

For completeness, the mechanism is as follows. Retain the deficient
cliques $C_a$, those with $t_a>0$, and all $d$ doubles. If there
are $s$ deficient cliques, this set has order $sr+1$. Applying (4)
and subtracting the internal clique edges bounds the remaining
color-$j$ edges by $M_0=rd(d-1)/2+d-1$.

A double with two deficient anchors has nonneighbor sets in their
cliques that must be completely joined in color $j$; otherwise
these two nonneighbors and the double could replace its two anchors
in $A$. Their product is therefore at most $M_0$. If one anchor
is full, (3) and the same exchange argument force the double to be
complete to the deficient clique. Assign each double to a deficient
clique in which it has at most $\sqrt{M_0}$ nonneighbors.

By (15), some $C_a$ receives $t_a+1$ doubles. Together they give an
$(r+1)$-set with at most
$d\sqrt{M_0}+\binom d2$ nonedges in color $j$. Inequality (2)
proves (16). Since $M_0\le rd^2$,

$$
d\ge
\sqrt{\frac{r-1}{\sqrt r+1/2}}
\ge (r/4)^{1/4}.
\tag{17}
$$

This tends to infinity but does not contradict the available
$r^2-r+1$ vertices outside $A$.

## 6. The unresolved endpoint

The local induction has a precise target: prove $P_r$. Theorem 4 only
reaches $k$ of order $r^{1/6}/\sqrt{\log r}$, not $k=r$.
Its loss is structural, not a matter of constants: after finding a
high-degree $K_k$ in the complement, the proof bounds the exceptional
set by $O(k^2\log k)$ and absorbs its vertices separately using a
square-root estimate. Those estimates do not remain useful at $k=r$.

The short proof of $P_3$ also has a specific obstruction to direct
iteration. At $k=3$, (4) and the preceding local exclusion force a
degree-$r$ vertex. At $k\ge4$, (4) permits average degree above
$r+1$; the same step no longer follows. No general boundary rigidity
theorem at $kr$ vertices has been proved here.

The clique-factor theorem does not fill this gap: no argument here
forces a color, or even the minority color, to contain the requisite
factor. Conversely, the explicit single-graph constructions are not
packings of $r$ color graphs, so they do not provide a counterexample.

Further derivations and failed approaches, with their assumptions
identified, are preserved in:

- Local independence and fiber exchanges (not retained).
- Packing, defects, and explicit single-graph obstructions (not retained).
- Growing-range proof and stability calculations (not retained).
- Independent check of the growing-range proof (not retained).
- Clique factors and affine-extension investigations (not retained).
- An unproved average-degree inequality investigated along the way (not
  retained).

The established results therefore narrow the possible structure of a
counterexample, but neither alternative requested in the problem has
been completed.


## 7. Concrete failure ledger and auxiliary calculations

This section incorporates the relevant working calculations directly into
this record, rather than leaving the failed approaches only as links.
No unproved assertion in this section is used in the established theorems.

The first construction proves that the minority budget, independence bound,
and every required $(r+1)$-vertex density inequality are compatible for
an infinite tail of parameters. The second investigation concerns an
auxiliary average-degree inequality that remains unproved. The later
calculations separate a proved packing upper bound from the missing
existence of any large clique packing.

### A uniform obstruction to a minority-graph proof

This note uses only the supplied problem statement and Erdős--Gyárfás paper.
It does **not** construct an edge coloring counterexample. It proves that a
natural single-color reduction loses essential information, for every
parameter in an infinite tail.

Let $r\geq 3$, $n=r^2+1$, and suppose hypothetically that every
$(r+1)$-vertex set in an $r$-coloring of $K_n$ contains every color.
Every color graph $G_i$ then satisfies


$$
\alpha(G_i)\leq r,\qquad
e(G_i[S])\leq \binom{r+1}{2}-(r-1)=\binom r2+1
\quad (|S|=r+1).
$$


A minority graph additionally satisfies $e(G_i)\leq rn/2$. The three
conditions do not contradict one another, even when imposed for every
$(r+1)$-set, rather than merely forbidding $K_{r+1}$.

#### Proposition

For every $r\geq 11$ there is a graph $G$ on $r^2+1$ vertices such that


$$
\alpha(G)=r,\qquad e(G)\leq \frac{r(r^2+1)}2,
\qquad
e(G[S])\leq\binom r2+1\quad (|S|=r+1).
$$


##### Construction

Set $N=2r+1$, and partition an $N$-element set into five nonempty parts
$A_0,\ldots,A_4$, with sizes $a_i$ differing by at most one. Let $F$
be the independent blowup of the five-cycle: its edges are all pairs between
$A_i$ and $A_{i+1}$, with subscripts modulo five, and no others. Put
$H=\overline F$, and take


$$
G=(r-2)K_r\ \dot\cup\ H.
$$


The graph has $(r-2)r+(2r+1)=r^2+1$ vertices. As $F$ is triangle-free
and has an edge, $\alpha(H)=\omega(F)=2$, and hence
$\alpha(G)=(r-2)+2=r$.

##### Edge count

Write $N=5q+s$, $0\leq s\leq4$, and let $a_i=q+\epsilon_i$, where
$\epsilon_i\in\{0,1\}$ and $\sum_i\epsilon_i=s$. Then


$$
e(F)=\sum_i a_i a_{i+1}
=5q^2+2qs+\sum_i\epsilon_i\epsilon_{i+1}
\geq \frac{N^2-s^2}{5}\geq\frac{N^2-16}{5}.
$$


It follows that


$$
e(H)\leq\binom N2-\frac{N^2-16}{5}
=\frac{6r^2+r+15}{5}.
$$


For $r\geq5$,


$$
\frac{6r^2+r+15}{5}\leq\frac{3r^2-r}{2},
$$


because this is equivalent to $3r^2-7r-30\geq0$. Therefore


$$
e(G)\leq (r-2)\binom r2+\frac{3r^2-r}{2}
=\frac{r(r^2+1)}2.
$$


##### Every small set has enough missing edges

We first record an elementary optimization fact. If $a>0$,
$2a\leq t\leq3a$, and $0\leq b_i\leq a$ with $\sum_{i=0}^4b_i=t$,
then


$$
\sum_i b_i b_{i+1}\geq a(t-2a).
\tag{1}
$$


Indeed, minimize the left-hand side on this compact polytope, choosing a
minimizer with as few coordinates strictly between $0$ and $a$ as
possible. If $b_i,b_j$ are two such coordinates, replace them by
$b_i+x,b_j-x$ throughout the allowed closed interval for $x$. The
objective is affine in $x$ when $i,j$ are nonadjacent in the five-cycle,
and has quadratic coefficient $-1$ when they are adjacent. It is therefore
concave, so at least one endpoint is no worse. That endpoint has fewer
strictly intermediate coordinates, a contradiction. Thus at most one
coordinate is intermediate. The minimum consequently has two coordinates
equal to $a$, one coordinate $t-2a$, and the others zero, including
the evident interpretations when $t=2a$ or $3a$. If the two full
coordinates are adjacent, their product alone is $a^2\geq a(t-2a)$.
Otherwise the third occupied coordinate is adjacent to at least one of
them, since the five-cycle has independence number two. This proves (1).

Now let $a=\lceil(2r+1)/5\rceil$. For an $(r+1)$-set $S\subseteq V(H)$,
put $b_i=|S\cap A_i|$. The number of missing edges of $H[S]$ is
$\sum_i b_i b_{i+1}$. Here $2a\leq r+1\leq3a$, so (1) gives at least


$$
a(r+1-2a)
$$


missing edges. This is at least $r-1$ for every $r\geq11$. For an
explicit residue check, write $r=5k+j$, $0\leq j\leq4$. The difference
$a(r+1-2a)-(r-1)$ is, respectively,


$$
\begin{array}{c|ccccc}
j&0&1&2&3&4\\ \hline
\text{difference}
&2k(k-3)&2k(k-2)&2k^2-2k&(2k+1)(k-2)&(2k+1)(k-1).
\end{array}
$$


All entries are nonnegative in their corresponding ranges $r\geq11$:
for $j=0$, $k\geq3$; for $j=1,2,3,4$, $k\geq2$.

Finally, if an $(r+1)$-set $S$ is not wholly contained in $H$, it
meets at least two components, and no one component contains more than
$r$ of its vertices. The number of cross-component pairs is at least
$r$: among nonnegative integers summing to $r+1$ with each at most
$r$, the maximum of the sum of squares is $r^2+1$. These pairs are
all missing edges of $G[S]$. Thus every $S$ has at least $r-1$
missing edges, as claimed.

#### Consequence for the proof strategy

No theorem involving only the order, the minority edge budget, the
independence bound, and the displayed induced-density exclusion can prove
Problem 617 for all $r$. A successful continuation must use more of the
simultaneous edge partition into color classes. The construction above
does have many $K_r$ components; it leaves open the useful possibility
that these same numerical hypotheses force a $K_r$ somewhere. That
stronger structural question is distinct from the false assertion that
the three conditions already give a contradiction.

### An unresolved average-degree strengthening

This investigation uses no outside sources. The following proposed inequality
has **not** been proved or disproved here:


$$
\alpha(G)\geq \frac{2|V(G)|}{\overline d(G)+\omega(G)+1}. \tag{A}
$$


Writing $n=|V(G)|$, $a=\alpha(G)$, $w=\omega(G)$, it is equivalent to


$$
e(G)\geq \frac{n^2}{a}-\frac{(w+1)n}{2}. \tag{B}
$$


In the complement $F$, this becomes the Ramsey--Turán-type assertion


$$
e(F)\leq \frac{a-2}{2a}n^2+\frac{\alpha(F)n}{2},
\qquad \omega(F)=a.
$$


#### Established special cases and obstacles

For $a=1$, (A) is equality. For $a=2$, the complement is triangle-free,
so each neighborhood is independent and has size at most $w$. Thus
$e(F)\leq nw/2$, proving (A).

Equality holds for a balanced clique blow-up of $C_5$: with five clusters
of size $t$, the parameters are $n=5t,a=2,w=2t,\bar d=3t-1$.
Disjoint unions of equal such blow-ups also give equality, for every positive
even independence number. Disjoint unions of equal cliques give further
equality cases.

A standard maximum-independent-set argument proves only the maximum-degree
version. If $I$ is a maximum independent set, each vertex outside $I$
has at least one neighbor in $I$. For each $u\in I$, the vertices whose
unique neighbor in $I$ is $u$ form a clique of size at most $w-1$.
Consequently


$$
\sum_{u\in I}d(u)\geq 2n-a(w+1).
$$


The replacement of the left side by $a\bar d$ is unjustified: maximum
independent sets can have larger mean degree than the whole graph. For
example, join an independent set of size three to the disjoint union of two
triangles. Its unique maximum independent set has degree six at each vertex,
whereas the graph's average degree is $16/3$.

#### A minimum-degree reduction

If (A) is false, a counterexample of minimum order must have
$\delta(G)\geq\omega(G)$. Here is the exact induction calculation.
Assume smaller graphs satisfy (A), and let $v$ have minimum degree
$\delta$. Put $s=\delta+1$, $a=\alpha(G)$, $w=\omega(G)$, with
$a,w\geq2$. The graph on $V\setminus N[v]$ has independence number
at most $a-1$, and its clique number is at most $w$. Thus deleting
$N[v]$ proves (B) whenever the number $q$ of edges deleted satisfies


$$
q\geq s^2-\frac{(w+1)s}{2}
       -\frac{(n-as)^2}{a(a-1)}. \tag{C}
$$


This follows by subtracting the lower bound
$(n-s)^2/(a-1)-(w+1)(n-s)/2$ for the surviving edges from the target
in (B). An empty surviving graph causes no problem: its required lower
bound is zero.

All vertices have degree at least $\delta$. The neighborhood of $v$
is $K_w$-free. Turán's bound inside that neighborhood therefore gives


$$
q=\sum_{u\in N[v]}d(u)-e(G[N[v]])
 \geq \frac{w\delta^2}{2(w-1)}.
$$


The difference between this last bound and the first two terms on the
right side of (C) is


$$
\frac{(w-1-\delta)((w-2)\delta+w-1)}{2(w-1)}.
$$


It is nonnegative if $\delta\leq w-1$, establishing the reduction.
It does not handle $\delta\geq w$, which includes the delicate regime
needed for the main problem.

#### Status

(A) remains an unproved auxiliary assertion and must not be invoked in a
proof of Problem 617. The calculations above give a genuine reduction, not
a resolution of the average-degree difficulty.

### Conditional clique-packing lower bound

More generally, suppose a color contains `k` disjoint `K_r`'s and its
remaining points contain an independent set `S` of size
`s=r-k+1`. Assume `k>=2`. Each core vertex list after removing the
neighbors of `S` has size at least `r-s=k-1`; an independent transversal
would extend `S` to an independent `(r+1)`-set. Lemma 1 therefore says
that every point of `S` has a color-`i` neighbor in every core, these
neighbors are distinct within each core, and the cross matchings on the
remaining `k-1` points of each core form `k-1` transversal `K_k`'s.
Counting only the resulting forced edges gives

`e(G_i) >= k binom(r,2) + (k-1) binom(k,2) + sk`

`= k[r^2+r+k^2-4k+3]/2`.

For a minority color the latter quantity must not exceed
`r(r^2+1)/2`. If the local assertion that every `(s-1)r+1`-set has
color-`i` independence number at least `s` has been proved, it guarantees
the required set `S` in the complement of the core cliques. This is one
way to translate the growing local independence bounds from the other
agents into restrictions on near-affine clique packings.

For an explicit consequence, write `P_h` for the assertion that every
`hr+1`-set in a counterexample has independence number at least `h+1`
in every color. Suppose `P_h` is established, `h>=1`, and `r>=4h+3`.
If a minority color had `k=r-h` disjoint `K_r`'s, its residue would
contain the required independent set of size `h+1`. Twice the difference
between the forced edge lower bound and the minority edge budget is

`D(r,h) = r^3-(4h+3)r^2+(3h^2+7h+2)r-h(h+1)(h+3)`.

The first two terms together are nonnegative at `r>=4h+3`, and the
remaining terms are at least

`(3h^2+7h+2)(4h+3)-h(h+1)(h+3)`

`=11h^3+33h^2+26h+6>0`.

Thus a minority color contains at most `r-h-1` disjoint `K_r`'s under
these hypotheses. For `h=2`, the exact polynomial is

`D(r,2)=r^3-11r^2+28r-30`,

which is positive for `r>=8`: at `r=8` it equals `2`, and on writing
`r=8+t` it becomes `t^3+13t^2+44t+2`. Since `P_2` is proved separately,
this yields the unconditional necessary condition that every minority
color of a hypothetical counterexample with `r>=8` has at most `r-3`
disjoint `K_r`'s.

More generally, any checked growing range for `P_h` immediately gives
a growing number of clique blocks which a minority color must fail to
retain. This deduction does not assert that most vertices are covered by
monochromatic `K_r`'s; establishing such a covering remains a separate,
unresolved issue.

### Near-boundary rigidity cannot simply be assumed

The exact `2r`-point rigidity proved by a separate author does not
extend to `2r-1` points using only the one-color local constraints and
the multicolor edge cap. For example, let `F` be a blowup of a five-cycle
with weights `(r-2,r-2,1,1,1)` around the cycle, and put `H=F^c`.
The two large parts are adjacent in `F`. For `r>=3`, this graph has

`|H|=2r-1`, `alpha(H)=2`, `omega(H)=r-1`,

and

`e(H)=r^2-r-1`.

The induced edge cap from the other `r-1` colors at this order is
`r^2-r`, so this example lies one edge below it. In particular it has
no `K_r` at all, so the local restriction on external neighbors of
monochromatic `K_r`'s is vacuous. This is not a full multicolor
counterexample; it shows that a boundary `3r` argument cannot simply
assume a `2r-1` residue contains a `K_r`.

### Exact disconnected templates versus spanning subgraphs

One construction route considered packing, for each color $i$, a graph

$$
(r-2)K_r\;\dot\cup\;H_i,\qquad |H_i|=2r+1,\quad\alpha(H_i)\le2,
$$

and then assigning colors to the unused pairs.

Some preliminary incidence arguments treated the displayed cliques as
components and used the absence of edges between components. That absence
cannot be assumed when the displayed graph is merely a spanning subgraph
of a color class: assigning unused pairs may introduce cross-component
edges. Therefore an obstruction for exact disconnected templates alone
does not exclude a packing followed by completion.

The final obstruction to this particular template route is stronger and
does not make that assumption: Proposition 1 forbids the
$2r+1$-vertex independence-two subgraph itself. It therefore rules out
both exact templates and spanning-template packings. The older affine
two-line repair arguments in the working notes are superseded by this
result; they are not additional steps in the main proof.

An unchanged affine extension fails even more directly. If one color on
the old $r^2$ vertices is exactly $r$ disjoint $K_r$'s, a new vertex
must be complete in that color to one of those cliques. Otherwise one
nonneighbor from each clique, together with the new vertex, is independent.
Being complete instead gives a monochromatic $K_{r+1}$.
Theorem 5 strengthens this by allowing arbitrary additional edges among
the old cliques.

## 8. Verification status and exact outstanding uncertainties

The growing-range theorem was checked independently within this
investigation. The edge-budget algebra, greedy clique construction,
exceptional partition, strict union bound, and constants were recorded in
an audit note that is not retained. The proofs of $P_2$, the exact
$2r$-vertex boundary lemma, and $P_3$ were also checked independently.
The established conclusions are mathematical deductions, not conclusions
from finite searches. No additional isolated value of $r$ was classified.

The remaining uncertainties are specific:

- The local independence hierarchy has not been continued to $P_r$.
  Its proved growing range is much smaller than that endpoint.
- There is no collective control of the exceptional vertices strong enough
  to replace the $O(k^2\log k)$ exceptional-set bound and separate
  square-root assignments at $k=r$.
- No useful large monochromatic clique packing has been forced in a
  minority color. Upper bounds on such packings do not supply an existence
  theorem.
- The average-degree inequality recorded above is unproved and unused.
  Even if proved, its immediate consequence would be a $K_r$ in a
  minority color, not a solution of the simultaneous packing problem.
- The explicit single-color graphs do not supply compatible edge-disjoint
  graphs for all $r$ colors. Conversely, excluding those examples does
  not classify the possible color graphs.

No proof for every $r$, no uniform infinite family of positive cases of
the original assertion, and no counterexample coloring were obtained.
The completed work consists of the conditional structural theorems,
explicit obstructions to certain reductions, and the gaps stated above.

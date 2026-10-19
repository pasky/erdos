---
name: research/erdos_617/independent/clique_residue_and_affine_repair
title: Independent investigation of Erdős Problem 617
desc: Second unverified isolated investigation, preserved below the metadata; checked conclusions are in independent-comparison.
tags: []
sources: []
created: 2026-09-22T08:27:34Z
updated: 2026-09-22T08:27:34Z
---


# Independent investigation of Erdős Problem 617

***

## Status and sources

**The problem was not resolved.** No coloring contradicting the assertion was
constructed, and no proof for all $r$ was obtained. The results below are
parameter-dependent structural restrictions on a hypothetical counterexample,
not additional isolated cases of the conjecture.

Only [problem page](../../../problems/extremal_graph_theory/E0617/_index.md) and the
supplied Erdős–Gyárfás paper and its local digest were used as external
mathematical material. No web search or later research notes were consulted. The
supplied statement that the cases through $r=11$ are known was not used to infer
any mechanism behind those proofs.

This is the retained independent record; longer supporting calculations were
in companion files that are not retained:

- `multicolor_constraints.md`: clique components, leakage, and the stronger
  clique–residue obstruction;
- `affine_extension.md`: affine repairs and sharp one-color perturbation bounds;
- `clique_packing.md`: the independent-transversal argument;
- `sparse_structure.md`: explicit obstructions to one-color methods;
- `constructive_algebra.md`: local palettes, cuts, and construction
  obstructions;
- `audit.md`: independent checks and the edge-coverage caveat.

## 1. Reformulation and elementary constraints

Put $N=r^2+1$. A counterexample is precisely an edge partition


$$
E(K_N)=E(G_1)\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}E(G_r)
$$


with


$$
\alpha(G_i)\le r\qquad(1\le i\le r).                 \tag{1}
$$


Every $(r+1)$-set must also have at least $r-1$ nonedges in each
individual $G_i$, because the other $r-1$ colors each need an edge.
Equivalently,


$$
e(G_i[S])\le\binom r2+1\quad\text{if }|S|=r+1.     \tag{2}
$$


A minority graph has


$$
e(G_i)\le\frac{r(r^2+1)}2.                          \tag{3}
$$


The ordinary independence version of Turán gives the individual lower bound


$$
e(G_i)\ge(r-1)\binom r2+\binom{r+1}2
=\frac{r^3-r^2+2r}{2}.
$$


Thus the allowance above the minimum, for a minority graph, is
$(r^2-r)/2$. This is small relative to its roughly $r^3/2$ edges, but
it is not small enough by itself to force a union of cliques.

If $L$ is a color-$i$ $K_r$, every outside vertex has at most one
color-$i$ neighbor in $L$: its $r$ edges into $L$ must include
all other $r-1$ colors. Any two monochromatic $K_r$'s of distinct colors
intersect in at most one vertex. If they are disjoint, their cross edges
are one perfect matching in every color. To see the last assertion, every
color is forced to have at least $r$ cross edges, and there are exactly
$r^2$ cross edges; the degree conditions at the two ends then give the
perfect matchings.

## 2. Strongest coupled result: a clique and a small-independence residue

**Theorem.** Suppose $s\ge2$ and $r\ge10000s^{10}$. In a hypothetical
counterexample there are no disjoint sets $L,H$ such that


$$
L\text{ is a color-}i\ K_r,\qquad |H|=sr+1,
\qquad\alpha(G_i[H])\le s.                          \tag{4}
$$


This is not a conjectural reduction: the stated theorem is proved below.
The unresolved issue is obtaining its hypotheses from an arbitrary coloring.
In particular, the existence of the large monochromatic clique is **not**
being assumed without proof in any claimed solution of the original problem.

### 2.1. Singleton neighbors give a near-extremal complement

Let $F=\overline{G_i[H]}$, $m=sr+1$, and $a=1-1/s$. Then $F$ is
$K_{s+1}$-free. By (2), every $(r+1)$-set in $H$ spans at least
$r-1$ edges of $F$.

For $j\ne i$ and $x\in L$, set


$$
C_{j,x}=\{v\in H:N_j(v)\cap L=\{x\}\}.
$$


Each $C_{j,x}$ is a color-$j$ clique: otherwise two nonadjacent vertices
of this set, together with $L\setminus\{x\}$, give a color-$j$
independent $(r+1)$-set. It is therefore a clique in $F$, so
$|C_{j,x}|\le s$.

Every $v\in H$ has at least one edge to $L$ in each color $j\ne i$.
At most one such color occurs twice; all other foreign colors occur once.
Consequently


$$
\sum_{j\ne i}\sum_{x\in L}|C_{j,x}|\ge(r-2)m.
$$


Edges inside these sets are distinct across all $j,x$. Using
$\binom u2\ge(s-1)u-\binom s2$ for $0\le u\le s$, we obtain


$$
\begin{aligned}
e(F)&\ge(s-1)(r-2)m-r(r-1)\binom s2\\
&=\frac{s(s-1)}2r^2
 -(s-1)\left(\frac{3s}{2}-1\right)r-2(s-1).
\end{aligned}                                                    \tag{5}
$$


In particular the Turán potential satisfies


$$
0\le\Phi(F):=\frac a2m^2-e(F)\le2sm.                \tag{6}
$$


No component assumption on $L$ is needed. If color $i$ occurs once in
the star from $v$ to $L$, then no foreign color is doubled, which only
improves the singleton count.

### 2.2. Elementary high-minimum-degree partiteness

The following sufficient condition is proved here, rather than imported
from a separate stability theorem:

> A $K_{s+1}$-free graph $J$ of order $n$ with
> $\delta(J)\ge(1-1/s-1/(6s^3))n$ is $s$-partite.

Put $D=n-\delta(J)$, $p=sD-n$, and $A=n-(s-1)D$. Turán implies
$p\ge0$, and the degree hypothesis gives


$$
A-(3s-2)p
\ge n\left[\frac1s-\frac{3s^2-s-1}{6s^3}\right]>0.  \tag{7}
$$


Since $A>0$, greedy common-neighborhood selection finds a $K_s$, say
$q_1,\ldots,q_s$. Let $A_i$ be the common neighborhood of the
$q_j$ with $j\ne i$. These sets are pairwise disjoint and independent,
since an overlap or an internal edge would produce a $K_{s+1}$.
Furthermore $|A_i|\ge A$. A vertex in $A_i$ has at most
$D-|A_i|\le p$ nonneighbors outside $A_i$.

A vertex $v$ outside their union must have at most $(s-1)p$ neighbors
in some $A_i$. Otherwise one can greedily select a $K_s$ in $N(v)$,
one vertex from each $A_i$. Assign $v$ to such a class. It has at most
$D-[A-(s-1)p]=sp$ nonneighbors outside that original class.

If two adjacent vertices are assigned to the same class $i$, choose
common neighbors in all the other original $A_j$'s. The pair excludes
at most $2sp$ vertices of a class, and previous choices exclude at most
$(s-2)p$ more. Inequality (7) permits every choice. This gives a
$K_{s+1}$, a contradiction. Thus the expanded classes are independent.

### 2.3. Delete a bounded exceptional set, then find a sparse large set

Starting from $F$, repeatedly delete a vertex of degree at most
$(a-\varepsilon)n$ in the current graph, where
$\varepsilon=1/(6s^3)$. One deletion changes the potential by at most


$$
\Phi_{\rm new}-\Phi_{\rm old}\le-\varepsilon n+a/2.
$$


As long as $n\ge m/2$ and $m\ge2/\varepsilon$, this is at most
$-\varepsilon m/4$. Equation (6) therefore permits at most


$$
b=48s^4                                                     \tag{8}
$$


deletions. The theorem's range ensures $m>2(b+1)$, so the process stops
before half the graph disappears. The remaining graph $F'=F-B$ is
$s$-partite by the preceding lemma; write its independent classes as
$A_1,\ldots,A_s$.

Let $M$ count nonedges of $F'$ between distinct classes. The potential
never increased, and the total number of cross-class pairs is at most
$a|F'|^2/2$, so


$$
M\le\Phi(F')\le2sm\le4s^2r.                         \tag{9}
$$


For every deleted vertex $v$, some $A_i$ contains at most $\sqrt M$
neighbors of $v$. Otherwise choose a random neighbor of $v$ in each
class. The expected number of nonadjacent chosen pairs is strictly below
$M/(\min_i|N(v)\cap A_i|)^2<1$, giving a $K_s$ in $N(v)$,
impossible. This also works when $M=0$.

Assign each deleted vertex to a class with at most $\sqrt M$ neighbors.
The expanded classes partition $sr+1$ vertices, so one contains an
$(r+1)$-set $S$. Its edges satisfy


$$
e_F(S)\le b\sqrt M+\binom b2
\le96s^5\sqrt r+1152s^8.                              \tag{10}
$$


For $r\ge10000s^{10}$, $s\ge2$, the two terms are at most
$0.96r$ and $0.0288r$, respectively. Their sum is less than $r-1$,
contradicting (2). This proves the theorem.

## 3. Independent transversals and clique packings

A useful exact lemma is the following. Suppose there are $t\ge2$ disjoint
parts $A_1,\ldots,A_t$, each of size at least $t-1$, and edges between
any two parts form a matching. If there is no independent transversal, then
all parts have size $t-1$, and the cross-edge graph is the union of
$t-1$ transversal $K_t$'s.

Here is the proof mechanism. A part with at least $t$ vertices can be
left until last in a greedy transversal. A vertex missing the matching
into another part can be chosen first and that other part last. Thus all
parts have size $t-1$ and all cross matchings are perfect. If two
nonadjacent vertices in different parts have the same neighbor in a third
part, choose them first; the third part has one extra available vertex and
can be left until last. This again gives a transversal. The perfect matching
maps must therefore be consistent, which is exactly the asserted union of
transversal cliques.

Suppose a color graph $G$ has $t$ disjoint $K_r$'s and the uncovered
vertices have an independent set $X$ of size $r-t+1$. Removing neighbors
of $X$ from each clique leaves at least $t-1$ vertices. The local
$K_r$ neighborhood cap makes all cross edges matchings. A transversal
would combine with $X$ to give $r+1$ independent vertices. The lemma
therefore forces


$$
\boxed{
 e(G)\ge t\binom r2+(t-1)\binom t2+t(r-t+1)
 =\frac t2[r^2+r+t^2-4t+3].}                          \tag{11}
$$


The last summand counts edges from $X$ into the original cliques: equality
of all remaining part sizes forces every vertex of $X$ to have one
neighbor in each clique, all distinct there.

For $t=r-1$, the residue has $r+1$ vertices and cannot itself be a
clique, so it supplies an independent pair. Twice the bound in (11) exceeds
the minority budget by


$$
r^3-7r^2+12r-8>0\qquad(r\ge5).
$$


Hence a minority graph has at most $r-2$ disjoint $K_r$'s for every
$r\ge5$.

More generally, if $t=r-s$ and the explicit right side of (11) exceeds
$r(r^2+1)/2$, the uncovered residue of a minority graph must have
independence at most $s$. If also $r\ge10000s^{10}$, Section 2 excludes
this clique packing. For every fixed $s$, these two conditions hold once
$r$ is sufficiently large. This is a uniform restriction on clique-rich
minority graphs, not a proof that arbitrary minority graphs are clique-rich.

## 4. Simultaneous component counting and leakage

There is a stronger quantitative result under a stronger structural
hypothesis. Suppose every color has at least $r-s$ components $K_r$,
where $1\le s<r$. Choose $r-s$ in each color, and call the uncovered
core $H_i$, of size $sr+1$.

Selected blocks of different colors intersect exactly once: if disjoint,
the perfect-matching observation in Section 1 would force an edge leaving
a monochromatic component. Each selected block of color $i\ne j$
therefore meets $H_j$ in exactly $s$ vertices, contributing
$\binom s2$ distinct non-$j$ edges to that core. Thus


$$
\sum_j e(\overline{G_j[H_j]})
\ge r(r-1)(r-s)\binom s2.                            \tag{12}
$$


The complete edge partition gives the exact count


$$
\begin{aligned}
\sum_j e(\overline{G_j[H_j]})
&=r\binom{sr+1}2-\binom{r^2+1}2+r(r-s)\binom r2\\
&=\frac12[(s^2-s-1)r^3+(2s-1)r^2].
\end{aligned}                                                     \tag{13}
$$


Subtracting (12) from (13) proves impossibility whenever


$$
\boxed{r^2-(s^3+s-1)r+s^2(s-1)>0.}                   \tag{14}
$$


In particular fixed $s\ge2$ is excluded for $r\ge s^3+s-1$.

For arbitrary selected disjoint $K_r$'s, let $B$ be the number of
own-color edges between selected blocks or from a selected block into its
core. For a block $L$ of color $i$, let $d_j(L)$ count selected
color-$j$ blocks disjoint from it. Then $|L\cap H_j|=s+d_j(L)$.
Writing


$$
D=\sum_{j}\sum_{i\ne j}\sum_L d_j(L),\qquad
Q=\sum_{j}\sum_{i\ne j}\sum_L\binom{d_j(L)}2,
$$


the same count gives the exact necessary inequality


$$
\boxed{
B\ge\frac r2[r^2-(s^3+s-1)r+s^2(s-1)]+sD+Q.}        \tag{15}
$$


For fixed $s$, this requires at least $(1/2+o(1))r^3$ such edges.
No sufficiently small upper bound for $B$ was established.

**Coverage caveat.** If the graphs are only edge-disjoint spanning subgraphs
and leave $U$ pairs uncolored, (13) acquires $+U$; (15) becomes the
same lower bound for $B+U$. Passing to independence-critical subgraphs
therefore does not preserve the contradiction. This was checked explicitly.

## 5. Affine-plane extension and a superquadratic repair bound

In the paper's construction on $r^2$ affine points, $r-1$ colors each
consist of one parallel class of $r$ cliques $K_r$; the last color merges
two directions.

An unchanged extension by one vertex $v$ is impossible. For any pure
color, unless its star neighborhood at $v$ contains a whole old line,
choose a nonneighbor of $v$ from each parallel line. These points and
$v$ are an independent $(r+1)$-set in that color. Two pure colors
would therefore require whole nonparallel lines in their disjoint star
neighborhoods, but the lines meet.

A quantitative strengthening does not assume intact old lines.

**Perturbation theorem.** Partition $X$, $|X|=r^2$, into $r$ parts
$L_j$ of size $r$, and let $G$ be a graph on $X\cup\{v\}$
satisfying (1) and (2). If $t$ counts edges of $G[X]$ between different
parts, then


$$
t\ge\frac14r^{4/3}-\frac12r,
\qquad
t\ge(4^{-2/3}-o(1))r^{4/3}.                         \tag{16}
$$


For the main argument, let $d(x)$ count neighbors outside the part of
$x\in X$. If $x,y$ are nonadjacent in one part, append random uniform
vertices from every other part. The resulting $(r+1)$-set is never
independent, so the union bound gives


$$
d(x)+d(y)\ge r-t/r.
$$


If $t<r^2$, all within-part nonedges therefore meet


$$
H=\{x:d(x)\ge(r-t/r)/2\},\qquad
h=|H|\le\frac{4rt}{r^2-t}.                           \tag{17}
$$


The sets $C_j=L_j\setminus H$ are cliques. Assume $h<r$, as holds
in the regime relevant to the asymptotic bound. Put $q=\lfloor\sqrt t\rfloor$.
Every $b\in H\cup\{v\}$ has at most $q$ nonneighbors in some $C_j$:
otherwise choose a nonneighbor of $b$ from each core, and the expected
number of cross edges is at most $t/(q+1)^2<1$, producing an independent
set with $b$.

Assign each $b$ to such a core. If $h_j=|H\cap L_j|$, some core
receives at least $h_j+1$ assignments, since there are $h+1$ vertices
to assign and $\sum h_j=h$. Together with that core they give $r+1$
vertices with at most


$$
(h+1)(\sqrt t+h/2)
$$


nonedges. Consequently


$$
r-1\le(h+1)(\sqrt t+h/2).                            \tag{18}
$$


If $t=O(r^{4/3})$, (17) and (18) yield
$r-1\le(4+o(1))t^{3/2}/r+o(r)$, proving the asymptotic assertion.
For the explicit version, $t<r^2/16$ gives $h\le9t/(2r)$ and


$$
r-1\le\frac8r(t+r/4)^{3/2}.
$$


Hence $t\ge[r(r-1)]^{2/3}/4-r/4\ge r^{4/3}/4-r/2$.
The complementary case follows from
$r^2/16\ge r^{4/3}/4-r/2$.

Apply this to every one of the $r-1$ pure affine colors. Its cross edges
are old edges newly given that color. Thus any repair into a counterexample
requires a number $m$ of changed old edges satisfying


$$
\boxed{m\ge(4^{-2/3}-o(1))r^{7/3}.}                  \tag{19}
$$


There is also a separate finite bound $m\ge(r-1)(r-2)+1$, obtained by
random independent transversals for the pure colors and random permutation
matrices for the merged color; the equality case forces an unhit old line.
Its full calculation is in `affine_extension.md`.

The exponent $4/3$ of the **single-graph** theorem is sharp. For
$r=k^3$, $k\ge10$, take a clique blow-up of $C_5$ with cyclic bag
sizes


$$
(r-k^2,\;4k+1,\;r-k^2,\;k^2-2k,\;k^2-2k)
$$


and adjoin $r-2$ disjoint $K_r$'s. It has independence number $r$
and satisfies (2). A suitable old partition into $r$ parts of size $r$
has exactly $5k^4-8k^3+8k^2$ crossing edges and total edit distance
$5k^4-4k^3$. The full local nonedge check is preserved in the affine note.
Moving the distinguished vertex into an intact $K_r$ also gives degree
$r-1$ at that vertex with only $O(r)$ extra crossings. Therefore a bound
on the new vertex's individual degree does not improve this one-color
exponent. This does **not** show the multicolor exponent $7/3$ is optimal.

## 6. A uniform lower bound on the incident palette

The following elementary decomposition gives another unconditional necessary
condition. Greedily choose a minimum-degree vertex of the current residual
graph and remove its closed neighborhood $A_j$. The chosen vertices are
independent, so if $\alpha(G)\le k$ there are at most $k$ blocks.
Writing $s_j=|A_j|$ and $h_j$ for the nonedges in that block, the edges
removed at its step number at least


$$
s_j(s_j-1)-e(G[A_j])=\binom{s_j}2+h_j.
$$


Thus $e(G)\ge\sum_j[\binom{s_j}2+h_j]$.

Apply this on $r^2$ vertices with independence at most $r-1$, still
assuming the local condition (2). Pad the block sizes to $r-1$ entries
and set $a_j=s_j-r$. Then $\sum a_j=r$. If $m$ of these are positive,
$\sum a_j^2\ge r^2/m$, and each positive block has $h_j\ge r-1$.
Using the exact Turán minimum $T(r^2,r-1)=(r^3+r+2)/2$, one obtains


$$
\begin{aligned}
e(G)-T(r^2,r-1)
&\ge\frac{r^2}{2m}+(r-1)m-\frac{r+2}{2}\\
&\ge r\sqrt{2(r-1)}-\frac{r+2}{2}.
\end{aligned}                                                     \tag{20}
$$


Set


$$
b_r=\left\lceil r\sqrt{2(r-1)}-\frac{r+2}{2}\right\rceil,
\qquad D_r=(r^2+r+2)/2.
$$


If a vertex $v$ sees only $k$ colors, each missing color has independence
at most $r-1$ on $V\setminus\{v\}$, while the other colors still have
independence at most $r$. Summing their edge lower bounds gives


$$
(r-k)b_r\le(k-2)D_r+2,
\qquad
\boxed{k\ge\frac{rb_r+r^2+r}{D_r+b_r}
=(2\sqrt2+o(1))\sqrt r.}                            \tag{21}
$$


This rules out constructions having a bounded incident palette at some
vertex. It falls well short of forcing all $r$ colors there.

A related cut inequality was also proved. If $a$ colors are absent between
disjoint sets of sizes $x,y>0$, then


$$
a\le\frac{r(r-1)}2\left(\frac1x+\frac1y\right).      \tag{22}
$$


For an absent color, its two independence numbers sum to at most $r$;
for another color each is at most $r$. Apply the continuous Turán bound
$e\ge(m^2/\alpha-m)/2$ on both sides, use Cauchy–Schwarz, and sum over
the colors to obtain (22). Every balanced cut therefore uses at least
$r-1$ colors. For two sets of size $r+t$, $1\le2t\le r$, exact
Turán rounding improves the corresponding palette bound to


$$
k(r+2t)\ge r(2t+1)+t-t^2
$$


if at most $k$ colors occur between them. These exclude fixed-template
blowups with macroscopic parts and a positive proportion of colors forbidden
across a pair of parts, but not templates whose complexity grows with $r$.

## 7. Explicit failures of tempting one-color approaches

### 7.1. Minority count plus local density does not suffice

For every $r\ge11$, let $H_r$ be a clique blow-up of $C_5$ with five
as-equal-as-possible nonempty bags totaling $2r+1$ vertices, and put


$$
G_r=(r-2)K_r\mathbin{\dot\cup}H_r.
$$


Then


$$
|G_r|=r^2+1,\quad\alpha(G_r)=r,\quad
\delta(G_r)=r-1,\quad e(G_r)\le r(r^2+1)/2,
$$


and every $(r+1)$-set has at least $r-1$ nonedges. Moreover every edge
is independence-critical.

For the local check, if $a=\lceil(2r+1)/5\rceil$ and $2a\le u\le3a$,
then


$$
\sum_{i\bmod5}x_ix_{i+1}\ge a(u-2a)
\quad(0\le x_i\le a,\ \sum x_i=u).
$$


Indeed, shifting mass between two interior coordinates makes the objective
linear or concave, so a minimum has all but at most one coordinate at a
bound. The nonzero sizes are then $a,a,u-2a$; the independence number of
$C_5$ is two, giving the displayed inequality. The complement of $C_5$
is another $C_5$, so it counts nonedges of the clique blow-up. At $u=r+1$
the resulting bound is at least $r-1$ for $r\ge11$. Sets meeting
multiple components have at least $r$ nonedges automatically.

The edge estimate follows from maximum degree $3a-1$ in $H_r$; the
sufficient arithmetic inequality is $3r^2-31r-10\ge0$. Deleting an edge
inside or between adjacent bags creates an independent triple using a
suitable third bag, proving criticality. Detailed residue-class arithmetic
and a version saturating the edge budget are in `sparse_structure.md`.

These are individual graphs, **not** colorings of the complete graph.
Section 2 supplies additional coupled constraints that prohibit these
particular clique-plus-small-core configurations for sufficiently large $r$.

### 7.2. Bounded-defect clique stability is also false for one graph

There are one-color examples with $r-\Theta(\sqrt r)$, not
$r-O(1)$, copies of $K_r$. For $r=2k^2$, $k\ge4$, set
$m=\lfloor k/2\rfloor$. Let $H$ have cyclic clique-bag sizes


$$
(r-3k,\ 2k,\ r-3k,\ 2k,\ 2k),
$$


and let $H^+$ add one vertex to a large bag. Then


$$
G=(r-2m)K_r\mathbin{\dot\cup}(m-1)H\mathbin{\dot\cup}H^+
$$


has $r^2+1$ vertices, independence number $r$, minimum degree $r-1$,
and is independence-critical. It meets the minority edge budget and the
local nonedge condition, but has exactly $r-2m$ copies of $K_r$.
The cost of replacing two $K_r$'s by $H$ is $k^2(4k-5)$ edges.
The complete edge and capped-simplex checks are preserved in the sparse note.
Thus bounded-defect stability cannot be asserted from those single-graph
hypotheses, even after imposing criticality.

### 7.3. A useful but incomplete criticality observation

Suppose a graph is edge-independence-critical and every outside vertex has
at most one neighbor in a clique $B=K_r$. If an edge $bx$ leaves $B$
inside its connected component $C$, then $\alpha(C)\ge r$.

Delete $bx$. A critical independent witness of size $\alpha(C)+1$
contains $b,x$. Each $b'\in B\setminus\{b\}$ must meet the witness
minus $b$, or replacing $b$ by $b'$ would give that larger independent
set in the original graph. The vertex $x$ already uses its unique
neighbor $b$ in $B$; the other $\alpha(C)-1$ witness vertices can
cover at most one $b'$ apiece. Hence $\alpha(C)-1\ge r-1$.

Therefore in a disconnected critical graph with independence $r$, every
$K_r$ is a whole component. The connected case is not settled. In
particular, no proof was found that a connected critical graph of order
$r^2+1$, independence $r$, and the local density condition must exceed
the minority edge budget.

## 8. Construction attempts and remaining uncertainties

- Color-preserving vertex-transitive constructions cannot work. All color
  graphs would be regular; one has degree at most $r$, and the same
  Brooks argument used in the supplied paper gives either an independent
  $(r+1)$-set or a monochromatic $K_{r+1}$. This excludes ordinary
  color-preserving Cayley constructions, not arbitrary actions that permute
  colors.
- The unchanged affine extension fails, and (19) rules out small repairs.
  There is no proof that an arbitrary counterexample is close to an affine
  coloring. Nor is there a construction achieving the required simultaneous
  repairs.
- A direct tensor amplification of the exceptional two-color pentagon,
  assigning fixed colors to equality coordinates, has independent coordinate
  fibers of size $5^{k-1}>2^k$ for $k\ge2$. This defeats that full
  product, but does not rule out carefully restricted products or different
  equality-coordinate rules.
- The central obstacle in the strongest line is structural: no argument
  forces an arbitrary counterexample to contain the pair (4) with
  $s\le(r/10000)^{1/10}$. Even the existence of a monochromatic $K_r$
  in a suitable minority graph has not been proved here.
- The leakage lower bound (15) has no matching contradiction-producing
  upper bound. Removing leakage by passing to critical subgraphs creates
  uncolored pairs, which invalidate the uncorrected edge identity.
- The single-color counterfamilies are rigorous obstructions to proposed
  lemmas, not evidence of a complete coloring. Their simultaneous packing
  with the independence bounds in all other colors is unestablished, and
  the coupled results explain why several natural packings cannot work.

All theorems above are
partial results with explicit hypotheses; no unproved structural reduction
has been promoted to a proof of Erdős Problem 617.

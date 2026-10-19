---
name: research/erdos_617/cross_color_cores
desc: Cross-color core constraints and common clique-feasible balancing weights with an exact energy budget; no universal contradiction.
tags: [graph-theory, proved, color-coupling]
sources: []
created: 2026-09-22T01:40:00Z
updated: 2026-10-14T00:26:52Z
---


# research/erdos_617/cross_color_cores

***

## Near-full-clique stars

**Proved coupled restriction.** Suppose the color graphs on
$N=r^2+1$ vertices are edge-disjoint and each has independence at
most $r$; uncolored pairs are allowed. Let $Q$ be a color-$i$
clique of order $r-t$, where either $t=1$, or $t\ge2$ and
$r\ge64t^2$. For $j\ne i$, put

$$
Z_j=\{x\notin Q:N_j(x)\cap Q=\varnothing\}.
$$

Then $\alpha(G_j[Z_j])\le t$, since a larger independent set
could be united with $Q$. Consequently $|Z_j|\le rt$: for
$t=1$ this is the clique cap; otherwise restrict to $rt+1$
vertices if necessary and apply [Hereditary span](hereditary_span_bound.md).

For $x\notin Q$, let $u(x,Q)$ count its uncolored pairs into
$Q$, and define the nonnegative integer

$$
f(x)=d_i(x,Q)+u(x,Q)+
\sum_{j\ne i}(d_j(x,Q)-1)_+.
$$

Counting the $r-t$ star slots gives

$$
|\{j\ne i:x\in Z_j\}|=t-1+f(x).
$$

Summing, and using the bounds on $Z_j$, proves

$$
\boxed{\sum_{x\notin Q}f(x)
\le r(r-1)-t^2+1
=|V\setminus Q|-t(t+1).} \tag{S1}
$$

At least $t(t+1)$ outsiders therefore have $f(x)=0$.
Their stars into $Q$ are fully colored, omit color $i$, and
have no repeated foreign color. In particular **every monochromatic
$K_{r-1}$ has at least two such rainbow stars**, each using all
other colors.

The same calculation bounds the own-color degree sum:

$$
\boxed{\sum_{q\in Q}d_i(q)
\le2(r-1)(r-t)-t+1.} \tag{S2}
$$

Indeed its internal contribution is $(r-t)(r-t-1)$, and its
external contribution is at most the left side of (S1).
For $t=1$, the $Z_j$ are foreign monochromatic cliques, and
$|Z_j\cap Z_k|\le1$ for distinct $j,k$.

No useful mutual-edge pattern between the guaranteed rainbow-star
vertices has been forced. These star counts do not supply an
independence augmentation or settle the growing-parameter core.

**Status: proved reductions, not a resolution.** These use the actual
coloring, not merely the one-color hereditary upper bound. Throughout,
the $r$ color graphs on $r^2+1$ vertices all have independence number
at most $r$.

## An asymmetric local-clique deficit

Let $W$ have $n=ar+1$ vertices, where $2\le a<r$, and suppose
$H=G_j[W]$ has independence number at most $a$. Let $c_k(v)$ be the
largest color-$k$ clique through $v$ **within $W$**. We have
$c_j(v)\le r$ and $c_k(v)\le a$ for $k\ne j$: a clique in any other
color is independent in $H$.

Define the nonnegative integer

$$
\delta(v)=r-c_j(v)+\sum_{k\ne j}(a-c_k(v)).
$$

Then

$$
\boxed{\sum_{v\in W}\delta(v)
\le n\left(a-2-\frac2a+\frac2r\right).} \tag{1}
$$


For each color apply the uniform-vector form of the localized
independence inequality from [Packing tools](packing_tools.md):

$$
2e(G_k[W])+n+\sum_{v\in W}c_k(v)
\ge\frac{2n^2}{\alpha(G_k[W])}.
$$

Sum over all colors, using their edge partition and the respective
independence upper bounds $a,r,\ldots,r$. This gives

$$
n(n-1)+rn+\sum_{v,k}c_k(v)
\ge2n^2\left(\frac1a+\frac{r-1}{r}\right).
$$

Substitute $\sum_k c_k(v)=r+(r-1)a-\delta(v)$ and $n=ar+1$
to obtain (1). The relevant quadratic inequality is Theorem 2.2 in
[Abiad--Kumar--Pragada](https://arxiv.org/html/2609.00210v1#S2);
its statement and the inequality proof were checked in the primary text.

Since $a<r$, the average in (1) is strictly less than $a-2$.
Thus some vertex has $\delta(v)\le a-3$. At that vertex choose a
maximum monochromatic clique in each color. Distinct chosen cliques
meet only at $v$, since otherwise their common edge has two colors.
Their union leaves exactly

$$
\boxed{a+\delta(v)\le2a-3} \tag{2}
$$

vertices of $W$ uncovered. This is a nearly exhaustive monochromatic
fan with a number of uncovered vertices linear in $a$.

For $a=2$, (1) has a negative right side, which is impossible.
For $a=3$, (1) implies that $H$ contains a $K_r$: otherwise every
$\delta(v)\ge1$. Deleting that clique lowers its independence bound
to two, because an independent triple outside it excludes at most
three vertices of the clique, and $r>3$. Its remaining $2r+1$
vertices contradict the $a=2$ conclusion. These are consequences of
the parameterized inequality, not new fixed-$r$ results.

## A minimal-ratio core

### An elementary alternative for the small-independence span bounds

Section 2 of the
[independent input](independent/small_independence_and_packing_obstructions.md)
gives a shorter alternative that does not use the localized independence
theorem. Its Turán-gap step, which the input does not prove, is proved in
[Packing tools](packing_tools.md).

Suppose $|W|=ar+1$, $2\le a\le r$, and $\alpha(G_j[W])\le a$.
The target graph cannot partition into $a$ cliques, since every
target clique has order at most $r$. Every other color has clique
number at most $a$, and so cannot partition into $r$ cliques.
The nonpartite gap therefore gives

$$
e(G_j[W])\ge p_a(ar+1)+r-1,\qquad
e(G_k[W])\ge p_r(ar+1)+a-1\quad(k\ne j).
$$

Their sum exceeds $\binom{ar+1}{2}$ by

$$
\frac{-a^2+3a+2}{2}\,r-2a.
$$

This excludes $a=2$ for $r\ge3$ and $a=3$ for $r\ge7$.
It is not stronger than the localized argument above, but uses
only elementary nonpartite density. This counting argument requires
actual color coupling; the one-color hereditary caps alone do not
justify its other-color gap estimates.
It also gives no equality structure at order $ar$, and therefore
does not replace the [three-row structure theorem](three_row_structure.md).

### Minimality and expansion

Choose an inclusion-minimal induced color graph $H$ such that
$|H|>r\alpha(H)$, and put $a=\alpha(H)$. Then

$$
|H|=ar+1,
\qquad |J|\le r\alpha(J)\quad
\text{for every proper induced }J\subset H.
\tag{3}
$$

The first assertion follows by deleting one vertex and using minimality.
For every nonempty independent $S\subset H$ with $|S|<a$,

$$
|N_H[S]|\ge r|S|+1. \tag{4}
$$

Otherwise the induced nonneighborhood has order greater than
$r(a-|S|)$ and independence at most $a-|S|$, contradicting (3).
In particular $\delta(H)\ge r$ when $a\ge2$.

If $a<r$, the core contains no $K_r$. Indeed, an independent $a$-set
outside such a clique could be augmented by a clique vertex, since
every outside vertex has at most one neighbor in the clique. Thus
deleting it leaves order $(a-1)r+1$ and independence at most $a-1$,
again contradicting (3).

At the fan vertex in (2), write $t=r-c_j(v)$. All target neighbors
outside its target clique belong to the uncovered set $U$, because
every other petal is anticomplete to $v$ in the target color. Hence

$$
d_H(v,U)\ge t+1.
$$

Also at least $r-|U|$ colors have no edge from $v$ to $U$; in each
such color $v$ is simplicial and its closed neighborhood is precisely
the corresponding petal. When $a$ is close to $r$, this count need
not be positive. No rectangular induction closing this gap is proved.

## Overloaded support cores meet the other exception classes

Use the notation of
[Two-supported private cliques](two_supported_private_cliques.md): $Q$ is a
color-$i$ $K_r$, and for every $j\ne i$ the private cliques are $P_{j,u}$, with
exception set $B_j$ and two-element supports. The sets $B_j$ are pairwise
disjoint.

For $A\subseteq Q$, put

$$
C_A=\bigcup_{u\in A}P_{j,u},\quad
X_A=\{x\in B_j:K_j(x)\subseteq A\},\quad
\varepsilon_A=|X_A|-\sum_{u\in A}(r-|P_{j,u}|).
$$

The induced set $W_A=C_A\cup X_A$ has order
$|A|r+\varepsilon_A$ and target independence number at most $|A|$,
by adjoining the anchors in $Q\setminus A$.
For every $k\ne i,j$, each private color-$k$ clique meets $W_A$ in
at most $|A|$ vertices. Its $r$ private cliques therefore cover at
most $r|A|$ vertices of $W_A$. Since $B_j\cap B_k=\varnothing$,

$$
\boxed{|B_k\cap C_A|\ge\varepsilon_A.} \tag{5}
$$

Thus any excess-one support core contains in its private rows an
exception of every other non-$i$ color. Summing (5) supplies at least
$(r-2)\varepsilon_A$ such vertices, but does not itself bound $|A|$.

## Pairwise Hall assignments

Fix distinct $j,k\ne i$. The $r\times r$ array of intersections
$P_{j,u}\cap P_{k,v}$ has at most one vertex per cell and exactly
$b_j+b_k-1$ empty cells, where $b_l=|B_l|$. Indeed its occupied cells
represent the $r^2+1-b_j-b_k$ vertices outside $B_j\cup B_k$.

In column $v$, the set $P_{k,v}\setminus\{v\}$ is independent in
color $j$. Its color-$j$ neighbor lists in $Q\setminus\{v\}$ satisfy
Hall's condition: a subfamily with fewer neighbors than members,
together with all unused anchors, would be independent of order
greater than $r$. Singleton lists occupy the already occupied cells.
Consequently the vertices of $B_j\cap P_{k,v}$ can be assigned
injectively to empty cells $(u,v)$ with $u\in K_j(x)$.

Across all columns this selects $b_j$ empty cells. Reversing $j,k$
selects $b_k$ empty cells, so the two selections overlap. At a shared
cell $(u,v)$ there are distinct vertices

$$
x\in B_j\cap P_{k,v},\qquad y\in B_k\cap P_{j,u},
\qquad u\in K_j(x),\quad v\in K_k(y).
$$

Both assignments cannot be clique-safe: completeness of $x$ to
$P_{j,u}$ and of $y$ to $P_{k,v}$ would give the edge $xy$ both colors.
This identifies an obstruction to simultaneous clique completion;
it does not establish that any Hall assignment is clique-safe.

## Many colors contain full cliques

The excess-deficit estimate in Section 8 of
[Two-supported private cliques](two_supported_private_cliques.md)
extends to every color $j\ne i$, not just the selected color with
$b_j\le r$. Write $f_j$ for its number of full private rows and

$$
E_j=\sum_{u:|P_{j,u}|<r}(r-|P_{j,u}|-1),\qquad
e(r)=\left\lceil\frac{\sqrt{8r-7}-5}{2}\right\rceil.
$$

For $r\ge7$,

$$
E_j\ge e(r). \tag{6}
$$

If $E_j\ge r-2$, this is immediate. Otherwise, any positive supporting
pair has deficit sum at most $E_j+2\le r-1$, which is the only size
hypothesis needed for the two-support inequality. The same owner proof
therefore gives $r-1\le\binom{E_j+3}{2}$; its separate exclusion of
$E_j=0$ is also unchanged. No upper bound on $b_j$ is needed to choose
the $d_i+1$ exceptions used in that proof.

Let $z_i(Q)=e_i(Q,V\setminus Q)$. Since
$f_j=r-b_j+1+E_j$ and
$\sum_{j\ne i}b_j=r^2-r+1-z_i(Q)$, exact counting gives

$$
\sum_{j\ne i}f_j
=z_i(Q)+r-2+\sum_{j\ne i}E_j
\ge z_i(Q)+r-2+(r-1)e(r). \tag{7}
$$

No color has $r$ disjoint $K_r$'s, by
[Packing tools](packing_tools.md), so $f_j\le r-1$. Consequently at
least $e(r)+1$ colors other than $i$ contain a full $K_r$, or at least

$$
\boxed{e(r)+2}
$$

colors in total. The $\Omega(r^{3/2})$ full-row incidences in (7) do
not imply a near-complete packing in a single color.

## Reciprocity of a full private row

The following identity was checked in the subsequent attempt at a
global contradiction. Let $Q$ be a color-$i$ $K_r$, and let
$R=P_{j,u}(Q)$ be a full private color-$j$ row, with $j\ne i$.
Their intersection is $\{u\}$. In the cross array between
$Q\setminus\{u\}$ and $R\setminus\{u\}$, color $j$ is absent,
by the private-row definition.

Color $i$ forms a matching in this array. Each vertex of
$R\setminus\{u\}$ has at most one color-$i$ neighbor in $Q$.
For a vertex of $Q\setminus\{u\}$, its edge to $u$ already
has color $i$; its edges to the full color-$j$ clique $R$
must contain every color other than $j$. Only one further edge
can therefore have color $i$. Write $m$ for this matching size.

Every color $k\ne i,j$ occurs once or twice in each row and
column of the array. Counting its edges in both ways gives

$$
\boxed{|B_k(Q)\cap R|=|B_k(R)\cap Q|.}
\tag{8}
$$

Indeed, an extra occurrence records exactly an exceptional
vertex for that anchor clique.

The reverse private row in color $i$ satisfies, when $m\le r-2$,

$$
\boxed{P_{i,u}(R)=Q\setminus B_i(R),\qquad
|P_{i,u}(R)|=r-m.}
\tag{9}
$$

The indicated subset of $Q$ belongs to the reverse private row
and has at least two vertices. Any additional private vertex
would be adjacent in color $i$ to both, since private rows are
cliques, contradicting the outside-neighbor bound for $Q$.
When $m=r-1$, only $u$ is guaranteed and this argument gives
no such equality.

These identities do not force a contradiction. The attempted
charge from asymmetric full-row incidences to edges leaving
$Q$ is not injective: one color-$i$ edge can be used in up
to $r-1$ outgoing private-row systems. Nor does reciprocity
make the pairwise Hall assignments clique-safe. No simultaneous
completion theorem was proved.


## Exact intersections of residual cores behind full-clique packings

Suppose color $i$ has $k_i=r-a_i$ disjoint full cliques
$B_{i,1},\ldots,B_{i,k_i}$ whose complement $S_i$ satisfies
$\alpha_i(S_i)\le a_i$. Then every full clique $Q$ of any other
color meets each $B_{i,t}$ exactly once and meets $S_i$ in exactly
$a_i$ vertices. Indeed $Q$ is color-$i$ independent, so these
intersections have upper bounds $1,\ldots,1,a_i$, whose sum is
$r=|Q|$. Every bound must be attained.

If color $j$ has another such packing with parameter $a_j$, its
$r-a_j$ full cliques account for $a_i(r-a_j)$ points of $S_i$.
Consequently

$$
\boxed{|S_i\cap S_j|=a_i a_j+1,\qquad
\alpha_i(S_i\cap S_j)\le a_i,\quad
\alpha_j(S_i\cap S_j)\le a_j.}
$$

All chosen blocks from different such color classes intersect once.
These assertions require the stated independence bounds on the
residuals; they are not claimed for arbitrary full-clique packings.

For a maximum disjoint packing with $k=r-a$, there is a useful
edge-count dichotomy. If its residual contains an independent
$(a+1)$-set, matching-transversal rigidity gives

$$
e(G_i)\ge k\binom r2+(k-1)\binom k2+k(a+1)+p_r(ar+1).
$$

For $k\ge2$ the second term counts the forced matching obstruction;
equality of the remaining list sizes also forces $k(a+1)$ edges
from the chosen independent set to the blocks. For $k=1$, the
independent $(a+1)$-set has size $r$ and must cover the entire
clique by its neighbors, giving the same last charge directly.
All these edges are disjoint from the residual's own edges.
If instead the residual has independence at
most $a$, it is $K_r$-free by maximum packing, and the localized
independence bound gives

$$
e(G_i)\ge\frac{r^3-r^2+ar+3r}{2}+\frac1a.
$$

Thus near-resolutions whose residual independence is too large are
expensive, but the second branch still leaves a substantial global
edge budget. These estimates do not exclude its growing residual cores.

The intersection identities alone cannot force a small $a_i$. In an
affine plane of order $r$, retain $r-a_i$ lines in direction $i$ and
let $S_i$ consist of its other $a_i$ lines together with one new point.
For arbitrary $1\le a_i\le r-1$, these sets have all the displayed
sizes and cross-intersections. This is only an incidence model, not
a coloring counterexample: it supplies no color-$i$ independence
bound on $S_i$. In particular no conclusion on the unrestricted
problem follows from this model or the pairwise identities.

## Simultaneous component counts and the coverage issue

These arguments audit Section 4 of the
[second independent input](independent/clique_residue_and_affine_repair.md).
Fix $1\le s<r$, and in every color choose $r-s$ disjoint
$K_r$'s. Let $H_j$ be their uncovered set in color $j$, of
order $sr+1$. Let $B$ count own-color edges between distinct
selected blocks or between a selected block and its core,
summed over colors, each edge once.

Put

$$
A_{r,s}=\tfrac12[(s^2-s-1)r^3+(2s-1)r^2].
$$

The exact edge partition gives

$$
\sum_j e(\overline{G_j[H_j]})=A_{r,s}+B. \tag{10}
$$

Indeed $\sum_j e(G_j[H_j])$ is the total edge count minus
$r(r-s)\binom r2$ selected internal edges and minus $B$.
Subtract it from $r\binom{sr+1}{2}$ to obtain (10).

### Arbitrary selected packings require leakage

For a selected color-$i$ block $L$ and $j\ne i$, let
$d_j(L)$ count selected color-$j$ blocks disjoint from $L$.
Blocks of different colors meet in at most one point, so
$|L\cap H_j|=s+d_j(L)$. Put

$$
D=\sum_{j,i\ne j,L}d_j(L),\qquad
Q=\sum_{j,i\ne j,L}\binom{d_j(L)}2.
$$

The edges within all the sets $L\cap H_j$ are distinct
within each complement: same-color selected blocks are disjoint,
and different colors have disjoint edge sets. Hence (10) yields

$$
\boxed{
B\ge\frac r2\bigl[r^2-(s^3+s-1)r+s^2(s-1)\bigr]+sD+Q.
} \tag{11}
$$

This verifies the input's leakage formula. No upper bound for
$B$ yielding a general contradiction is known.

If the selected blocks are whole color components, then $B=0$.
They must meet every differently colored selected block: a disjoint
pair of differently colored full cliques has a perfect matching
in every color between them, contradicting the component condition.
For completeness, color $i$ on such a pair has degree at least one
at every vertex of the color-$i$ clique (by the other clique's
independence property) and at most one at every opposite vertex
(by its own clique's outside-neighbor cap). Thus it is a perfect
matching; the same holds for color $j$. Every remaining color
has degree at least one on both sides. The $r^2$ cross edges
force exactly one perfect matching in each of the $r$ colors.
Thus in the component case $D=Q=0$ as well.

### A stronger component inequality, now proved

If the chosen blocks are components, component additivity gives
$\alpha(G_j[H_j])\le s$. In each foreign color $k\ne j$,
every clique in $G_k[H_j]$ has order at most $s$. Consequently
this graph cannot partition its $sr+1$ vertices into $r$ cliques.
The [nonpartite Turán gap](packing_tools.md) gives

$$
e(G_k[H_j])\ge p_r(sr+1)+s-1
=r\binom s2+2s-1.
$$

Sum over $k\ne j$ and then over $j$, and compare with (10)
at $B=0$. It follows that

$$
\boxed{r^2-(s^2-3s+1)r-4s+2\le0.} \tag{12}
$$

This is exactly the component formula left unverified in the
first [independent comparison](independent_comparison.md).
It is stronger than the second input's component exclusion
derived from (11). Neither proves that the required component
decomposition exists in a counterexample.

### Uncolored pairs cannot be silently discarded

If the graphs are only edge-disjoint spanning witnesses and
$U$ pairs are left uncolored, (10) has $B+U$ in place of $B$.
Equation (11) is then a lower bound on $B+U$, not $B$.
For true components, the same nonpartite argument proves only

$$
U\ge\frac r2\bigl[r^2-(s^2-3s+1)r-4s+2\bigr],
$$

not the contradiction (12).

More generally the latter is a lower bound for $B+U$ if all
the selected-packing residues have independence at most $s$.
Those additional independence bounds must not be assumed for
arbitrary packings. Independence-critical pruning can create
uncolored pairs; recoloring them to restore coverage can destroy
other colors' component decompositions. The local pruning in
[Minimal-ratio potential](minimal_ratio_potential.md) makes no
simultaneous component assertion.

## Positive balancing weights for simultaneous components

**Proved limitation of an incidence-only approach.** Consider the good
colors of the [critical partial coloring](critical_component_reduction.md).
Let their number be $g$, let color $i$ have $c_i$ full components,
and put $a_i=r-c_i>0$. Write $R_i$ for the complement of those
components. Every full component of a foreign color is an independent
$r$-set in color $i$, so it meets each of its full components once.
It therefore meets $R_i$ in exactly $a_i$ vertices.

In particular, for distinct good colors,

$$
|R_i|=ra_i+1,\qquad |R_i\cap R_j|=a_i a_j+1.
$$

Indeed their component unions have orders $rc_i,rc_j$ and intersect
in $c_ic_j$ vertices, one for each pair of components.

These incidences always admit the following strictly positive balancing
weight. Put

$$
A=\sum_{i\text{ good}}\frac1{a_i},\qquad
x(v)=1-\frac{\sum_{i:v\in R_i}1/a_i}{r+A},\qquad
t=r-\frac{g-1}{r+A}.
$$

One has $x(v)\ge r/(r+A)>0$. For a full component $Q$ of a good
color $j$, its own residue contributes zero to the sum on $Q$, and
every other residue contributes $a_i/a_i=1$. Consequently

$$
x(Q)=t.
$$

Summing over the entire vertex set gives

$$
x(V)=r^2+1-\frac{rg+A}{r+A}=rt,
\qquad x(R_i)=x(V)-c_i t=a_i t.
$$


Thus the simultaneous incidence constraints cannot rule out a positive
weight assigning the same mass to every full component and the matching
mass to each residue. This does not say that $x$ is a stable-set marginal
vector in a residue, or that the incidence system extends to an actual
coloring. No contradiction using the additional residue edges was
obtained. A proposed stronger edge-cost claim for nongood colors was
discarded: excluding a disjoint union of $r$ cliques does not exclude
a partition into $r$ cliques with cross edges, as needed to invoke the
nonpartite Tur\'an gap.

## Normalized common weights and their exact energy budget

**Proved refinement; no contradiction.** The preceding balancing
weights have an exact squared norm. Retain the good colors, their
component counts $c_i$, and $a_i=r-c_i>0$, and put $N=r^2+1$.
Let $T(v)$ be the good colors whose full components contain $v$, and set

$$
s(v)=\sum_{i\in T(v)}\frac1{a_i},\qquad
S=\sum_{i\text{ good}}\frac{c_i}{a_i},\qquad
D=N+S,\qquad w(v)=\frac{r+s(v)}D.
$$

This is the preceding weight $x/t$ in a more convenient form. Same-color
components are disjoint, while differently colored components meet once.
Consequently

$$
\sum_vs(v)=rS,
$$


$$
\begin{aligned}
\sum_vs(v)^2
&=\sum_i\frac{rc_i}{a_i^2}
 +2\sum_{i<j}\frac{c_ic_j}{a_i a_j}\\
&=S^2+\sum_i\frac{c_i(r-c_i)}{a_i^2}=S^2+S.
\end{aligned}
$$

It follows that

$$
\boxed{w(V)=r,\qquad \|w\|_2^2=1-\frac1D<1.} \tag{13}
$$

Indeed the numerator of the squared norm is
$r^2N+2r^2S+S^2+S=D(D-1)$.
For a full component $Q$ of color $j$,

$$
s(Q)=\frac r{a_j}+\sum_{i\ne j}\frac{c_i}{a_i}=S+1,
$$

so $w(Q)=1$ and $w(R_i)=r-c_i=a_i$.

These weights are **clique-feasible in every color**: every monochromatic
clique has weight at most one. A full clique of a nongood color meets
each good component exactly once and therefore has weight
$(r^2+S)/D=1-1/D$. A full clique of a good color is a component, by
criticality. For a clique $K$ of order at most $r-1$, put
$A=\sum_{i\text{ good}}1/a_i$. Since $s(v)\le A$,

$$
w(K)\le\frac{(r-1)(r+A)}D<1,
$$

where $D=r(r+A)-g+1$ and
$D-(r-1)(r+A)=r+A-g+1>0$.

Let $A_i$ and $A_U$ be the adjacency matrices of the critical color
graphs and of their uncolored pairs. Motzkin--Straus copositivity,
proved in [Critical semidefinite gap](critical_semidefinite_gap.md), gives

$$
\varepsilon_i:=w^{\mathsf T}(I+A_i)w-r\ge0.
$$

The disjoint edge sets give $\sum_i A_i=J-I-A_U$. Thus

$$
\boxed{\sum_i\varepsilon_i
=(r-1)\left(1-\frac1D\right)-w^{\mathsf T}A_Uw<r-1.} \tag{14}
$$

For a good color $i$, each full component contributes its squared
weight, namely one, so this is exactly the residual excess

$$
\varepsilon_i
=w_{R_i}^{\mathsf T}(I+A_{G_i[R_i]})w_{R_i}-a_i.
$$

In particular some color has excess below one, while every good
residue has its exact independence mass $a_i$.

The missing condition is **rank feasibility**: $w(W)\le\alpha(G_i[W])$ for
arbitrary induced sets is not proved. Clique feasibility is only its
independence-one case. Thus these weights do not establish the
[low-energy rounding candidate](light_independent_set_obstruction.md), a light
foreign-clique anchor, or a coloring contradiction. The incidence normalization
and the additional actual-edge accounting above are valid without those unproved
conclusions.

### A degree bound using the actual component incidences

The same incidence vector also bounds degrees in the simultaneous
critical witnesses. For a vertex $v$ outside the full components of
color $i$, there are no color-$i$ edges into those components. Into
a foreign full component not containing $v$, it has at most two
color-$i$ neighbors; into one containing $v$, it has none. Therefore

$$
(A_i s)(v)\le2S.
$$

Put $\mu=rS/N$. The preceding moment calculation gives

$$
V_s:=\sum_v(s(v)-\mu)^2=S+S^2/N.
$$

For $d=d_i(v)$, Cauchy--Schwarz now implies

$$
\mu d\le2S+\sqrt{dV_s}.
$$

Using $\sqrt{dV_s}\le(\mu d+V_s/\mu)/2$ yields

$$
\boxed{d_i(v)\le\frac{4N}{r}
 +\frac{N^2}{r^2S}+\frac N{r^2}.} \tag{15}
$$

Full-component vertices instead have color degree exactly $r-1$.
The established component count gives $S\ge C/r=\Omega(\sqrt r)$,
so every simultaneous critical witness has maximum degree
$O(r^{3/2})$. If $S=\Omega(r)$, (15) improves to $O(r)$, but that
stronger lower bound on $S$ is not established. Neither degree bound
forces an independent $(r+1)$-set or supplies the missing rank
feasibility.

## Rank deficits of the common weights

The common weights have two additional exact properties. For a good
color $i$ use its residue $R_i$ and $a_i=r-c_i$ as above; for a nongood
color set $c_i=0$, $a_i=r$, and $R_i=V$.
For $W\subseteq R_i$, put $b=\alpha_i(W)$ and

$$
\Delta_i(W)=\sum_{\substack{j\ne i\\j\text{ good}}}\frac1{a_j}
\sum_{Q\text{ full component of }j}(b-|W\cap Q|)\ge0.
$$

Nonnegativity holds because each such $Q$ is independent in color $i$.
Since $s(W)=b(S-c_i/a_i)-\Delta_i(W)$, direct substitution gives

$$
\boxed{D(w(W)-b)=r\left(|W|-rb-\frac b{a_i}\right)-\Delta_i(W).} \tag{16}
$$

Thus every nonoverloaded subset ($|W|\le rb$) satisfies its rank
inequality. The case $b=a_i$ also satisfies it because $w(R_i)=a_i$.
A rank violation must therefore contain an overloaded induced subgraph
of independence strictly below $a_i$.

If all residues satisfied the proper-induced minimal-ratio condition,
then $w$ would be rank-feasible in every color. To verify the statement
for a general set, split off its intersections with that color's full
components, each contributing at most one to both its weight bound and
the componentwise independence number, then apply (16) to its residual
part. Simultaneous minimal-ratio normalization has not been established.
For a minimal overloaded set of order $rb+1$, the exact needed charge is

$$
\Delta_i(W)\ge r(1-b/a_i),
$$

which the incidence identities alone do not prove.

Moreover, $w$ uniquely minimizes squared norm among all real vectors
$y$ satisfying $y(V)=r$ and $y(Q)=1$ on every good full component.
Indeed, $s\cdot y=S$, so

$$
w\cdot y=\frac{r^2+S}{D}=\|w\|_2^2,
\qquad
\boxed{\|y\|_2^2=1-\frac1D+\|y-w\|_2^2.} \tag{17}
$$

A rank repair preserving these component masses retains squared norm
less than one exactly when its squared displacement is less than $1/D$.
No such simultaneous repair is supplied here.

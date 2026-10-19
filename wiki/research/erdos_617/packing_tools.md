---
name: research/erdos_617/packing_tools
desc: Localized independence and clique-packing tools, plus an elementary total-edge independent-transversal bound with controlled local degree.
tags: [graph-theory, packing]
sources: []
created: 2026-09-21T23:52:12Z
updated: 2026-10-13T18:04:28Z
---


# research/erdos_617/packing_tools

***

## A transversal criterion from topological density

**Proved consequence of specified external theorems.** Let a graph
$J$ be partitioned into independent parts of order at least $m$.
Let $E=e(J)$, suppose each pair of parts has at most $\kappa>0$
cross edges, and assume

$$
\Delta(J)\le(1-\epsilon)m,\qquad0<\epsilon\le1/2.
$$

Writing $c=\epsilon(1-\epsilon)$, one has

$$
\boxed{E\kappa<2c^2m^4\quad\Longrightarrow\quad
J\text{ has an independent transversal}.} \tag{TD}
$$


Use Theorems 7, 8, and 14 of
[Haxell--Wdowinski, *Degree criteria and stability for independent
transversals*](https://arxiv.org/html/2305.10595), checked in the
primary text. They respectively give topological Hall, the bound
$e(F)\ge d|F|-d^2k$ when $\eta(F)\le k$ and
$d=\Delta(F)$, and $\eta(F)\ge |F|/(2d)$.

If no transversal exists, topological Hall gives a subfamily of
$s$ parts whose cross graph $F$ has $\eta(F)\le s-1$.
The connectivity bound implies $d>m/2$. Thus

$$
e(F)\ge dms-d^2(s-1)
=d(m-d)s+d^2>cm^2s.
$$

Combining with $e(F)\le\kappa s(s-1)/2$ gives
$s-1>2cm^2/\kappa$, hence
$E>cm^2+2c^2m^4/\kappa$, contradicting (TD).

For disjoint capped cliques of orders between $r-k$ and $r$,
with $2k\le r$, the two-clique cap gives $\kappa\le r+k^2$.
Consequently, when $k=O(\sqrt r)$, total cross edges are
$O(r^2)$, and all surviving lists have linear order, a fixed
positive margin between their order and the maximum cross degree
forces a transversal for sufficiently large $r$. Arbitrary list
trimming preserves the pair-edge bound. The required maximum-degree
margin has not been established for arbitrary residual extensions.

These are necessary conditions on a hypothetical counterexample, not a
resolution. Use the notation of [the reductions](reductions.md).

## An elementary total-edge independent-transversal bound

**Proved.** Let a graph $J$ be partitioned into parts of order at least
$m\ge8$. Ignore edges within parts, let $E$ be the number of cross
edges, and assume that a vertex has at most $d\ge1$ neighbors in
any other individual part. If

$$
\boxed{E<\frac{m^3}{128d},} \tag{T}
$$

then the parts have an independent transversal. The number of parts
is arbitrary. This is a sufficient bound, not a sharp constant claim.

Call a part heavy if at least $T=m^2/32$ cross edges are incident
with it. If there are $h$ heavy parts, then
$hT\le2E$, so $hd<m/2$. Greedily choose independent representatives
in the heavy parts: earlier choices exclude at most $(h-1)d<m$
vertices in any later heavy part. Their deletion of neighbors from
each light part leaves a list of size greater than $m/2$.

Choose independent uniform representatives from the light lists.
For each remaining cross edge, the event of choosing both endpoints
has probability at most $4/m^2$. Events on disjoint pairs of parts
are jointly independent. The number of events sharing either part
with a given event, including the event itself, is less than
$2T=m^2/16$, because each light part had fewer than $T$ incident
edges before any deletion. The symmetric local lemma applies:

$$
e\,\frac4{m^2}\,\frac{m^2}{16}=\frac e4<1.
$$

There is a conflict-free choice, completing the transversal.
The edge-free case is immediate. Real-valued $m,T$ cause no rounding
problem: the dependency count is an integer strictly below $2T$.

The proof and event dependencies were checked by the author and are
author-recorded. It requires a local-degree bound, which has **not** been
established for arbitrary near-full anchors in the surviving cores. It does
exclude the new two-reserved-direction affine candidate described in
[Construction attempts](construction_attempts.md).

## The localized Caro--Wei bound

Abiad, Kumar, and Pragada, *Localization of the Caro--Wei bound and its
applications to bipartiteness*, arXiv:2609.00210v1 (31 August 2026),
[Theorems 2.2 and 3.1](https://arxiv.org/html/2609.00210v1), prove

$$
\alpha(H)\ge\sum_{v\in V(H)}\frac{2}{d_H(v)+c_H(v)+1},
$$

where $c_H(v)$ is the largest clique order through $v$.
The inequality portion of their quadratic minimization/private-neighbor
proof was read and checked by the author. The equality
classification is not needed here. Jensen's inequality gives

$$
e(H)\ge\frac{|H|^2}{\alpha(H)}
-\frac{(\omega(H)+1)|H|}{2}. \tag{1}
$$

This input is a 2026 preprint result, not a classical theorem, so its
provenance is stated explicitly.

The
[independent input](independent/small_independence_and_packing_obstructions.md),
Appendix F, leaves the averaged inequality unproved. That uncertainty is
resolved by this checked input, not by replacing maximum degree with average
degree in Fajtlowicz's bound. Explicitly, Jensen and $c(v)\le\omega(H)$ give

$$
\alpha(H)\ge\frac{2|H|}{\overline d(H)+\omega(H)+1}.
$$

The primary paper's Theorem 2.2 inequality proof and Theorem 3.1
statement were rechecked during the comparison.

## What (1) forces in the least-color nonneighborhood

Let $d$ be the least-color minimum degree, put $t=r-d\ge1$, and suppose
$j$ disjoint target $K_r$'s have been removed from its nonneighborhood.
If the residual contains no further $K_r$, set $s=r-1-j$. It has
$n=rs+t$ vertices and independence number at most $s$.
Its edge budget and the lower bound (1) are

$$
E=r^2+s\binom r2-\binom{d+1}{2},\qquad
L=\frac{(rs+t)^2}{s}-\frac{r(rs+t)}2.
$$

Straight subtraction gives

$$
E-L=\frac{r(j-t)}2-\frac{t(t-1)}2-\frac{t^2}{s}.
$$

Thus whenever $s\ge1$ and $j\le t$, another $K_r$ is forced.
In particular two blocks are forced universally.
If the process reaches $s=0$ with a nonempty residual, the independence
bound itself is a contradiction.

For the difficult row $d=r-1$, the estimate ceases to contradict the budget
after the second block. This gap is not repaired by simply invoking the
new theorem again.

## Rigidity of a failed independent transversal

Let $Q_1,\ldots,Q_k$ be disjoint target $K_r$'s and let $I$ be an
independent set outside them of size $r+1-k$, where $2\le k\le r$.
Delete the neighbors of $I$ from each block, obtaining lists $L_i$.
Every list has at least $k-1$ vertices, and edges between lists form
matchings.

If there is no independent transversal, every list has exactly $k-1$
vertices and every pair of lists is joined by a perfect matching.
Indeed, a list of order at least $k$ can be left to the last greedy choice.
If $x\in L_i$ has no neighbor in $L_j$, select $x$ first.
The other $k-2$ lists each retain at least $k-2$ choices, and $L_j$
retains at least $k-1$; greedy choice with $L_j$ last succeeds.
Thus failure costs at least

$$
(k-1)\binom k2
$$

target edges between the blocks. No assertion about the colors of
unselected edges is needed.

In fact the matching obstruction is completely rigid: its cross graph
is the disjoint union of $k-1$ transversal $K_k$'s. This strengthening
from Section 4 of the independent input is correct. For an abstract
system of $k\ge2$ parts of order at least $k-1$, argue by induction.
The case $k=2$ is immediate. Fix a vertex $x$ in one part and remove
its neighbors from all other parts. The resulting $k-1$ parts have
order at least $k-2$ and still have no independent transversal.
Induction makes every remaining part have exactly $k-2$ vertices.
Repeating for every $x$ shows that all original parts have order
$k-1$ and all pairwise matchings are perfect. For any two other
parts, deleting the two neighbors of $x$ leaves their matching
perfect. Those neighbors must therefore be matched to one another.
Labeling vertices by their matching partners in one fixed part now
gives precisely $k-1$ disjoint transversal cliques.

This rigidity is distinct from the arbitrary-cross-graph
[transversal union-bound equality theorem](transversal_equality.md).
For equal lists of size $k-1$, the matching obstruction has normalized
edge weight $k/2$, not one (unless $k=2$).

The [second independent input](independent/clique_residue_and_affine_repair.md)
also retains a useful edge charge: since each list has exactly
$k-1$ vertices, the $r+1-k$ vertices of $I$ each have one
neighbor in each full clique, and these neighbors are distinct
within that clique. Thus, for $2\le k\le r$,

$$
\boxed{
e(G)\ge k\binom r2+(k-1)\binom k2+k(r+1-k)
       +p_r((r-k)r+1).
} \tag{P}
$$

The last term counts the residual's own edges and is disjoint
from the first three charges. The independent input omitted
this optional last term, while the earlier packing branch in
[Cross-color cores](cross_color_cores.md) omitted the third.
Both can be retained simultaneously.

In particular a minority graph cannot contain $r-1$ disjoint
$K_r$'s for $r\ge5$. Its $r+1$ uncovered vertices have an
independent pair because $K_{r+1}$ is forbidden. Even without
the last term in (P), twice its lower bound minus the doubled
minority budget is

$$
r^3-7r^2+12r-8=r(r-3)(r-4)-8>0.
$$

For $k=r-s$, whenever (P) exceeds the minority budget, the
residue must instead have independence at most $s$.
It is then excluded for $s=1$ by the clique cap, or for
$s\ge2$ and $r\ge64s^2$ by
[Hereditary span](hereditary_span_bound.md). For each fixed $s$
these conditions eventually hold, but no near-resolution with
fixed $s$ is forced by the existing arguments.

## A self-contained nonpartite Turán gap

The following supplies the gap used below. It also repairs the missing
proof link for equation (6) in the independent input. Write
$\tau_k(n)=\binom n2-p_k(n)$. If $k\ge2$ and a $K_{k+1}$-free
graph $F$ is not $k$-partite, then

$$
e(F)\le\tau_k(n)-\lfloor n/k\rfloor+1. \tag{2}
$$

Equivalently, $\alpha(J)\le k$ and failure of a partition of $J$
into $k$ cliques imply $e(J)\ge p_k(n)+\lfloor n/k\rfloor-1$.

First transform $F$, by single-vertex cloning operations that never
decrease its edge count, into a complete multipartite graph with at
most $k$ parts. For completeness, choose a maximum-degree vertex
$v$, put $A=N(v)$, $B=V(F)\setminus A$, and replace each other
vertex of $B$ by a nonadjacent twin of $v$. An unprocessed vertex of
$B$ only loses neighbors as this proceeds, so each operation is
nondecreasing in edge count; clique-freeness is preserved. The set
$B$ becomes independent and complete to $A$. Repeat recursively in
the $K_k$-free graph on $A$. The complete adjacency to the previous
parts adds a constant to all degrees, so the same edge monotonicity
holds globally.

Let $F'$ be the graph immediately before the first $k$-partite
graph in this sequence, and let $x$ be the vertex cloned at that
step. Then $e(F')\ge e(F)$ and $F'-x$ has a partition into exactly
$k$ nonempty independent sets, of sizes $n_i$. Fewer parts would
make $F'$ itself $k$-partite. Put $m_i=|N_{F'}(x)\cap V_i|$.
Every $m_i\ge1$, for the same reason.

Order the $m_i$ increasingly. A choice of one neighbor of $x$ in
each part must contain a missing cross-edge. Uniform independent
choices and the union bound show that there are at least $m_1m_2$
missing cross-edges, since each such edge occurs with probability
at most $1/(m_1m_2)$. If $s\le t$ are the two smallest part sizes,
then

$$
\begin{aligned}
e(F')&\le\sum_{i<j}n_in_j+\sum_i m_i-m_1m_2\\
&\le\sum_{i<j}n_in_j+n-s-t.
\end{aligned}
$$

Here $m_1+m_2-m_1m_2\le1$, and the two corresponding part sizes
sum to at least $s+t$.

Add one vertex to an $s$-part of the complete $k$-partite graph
with sizes $n_i$, obtaining a graph $K$ on $n$ vertices. The last
bound becomes $e(F')\le e(K)-t+1$. Put $q=\lfloor n/k\rfloor$.
If $t\ge q$, this proves (2). If $t<q$, some part of $K$ has size
$c\ge q+1$. Moving a vertex from it to the unchanged $t$-part
gains $c-t-1\ge q-t$ edges. Hence
$\tau_k(n)-e(K)\ge q-t$, again proving (2).

This agrees with the relevant branch of
[Kang--Pikhurko Theorem 1](../../../library/extremal_graph_theory/kang_pikhurko_2005_maximum_k_r_1_free_graphs_which_are_not_r_partite/_index.md),
whose digest and theorem passage were checked. The proof here needs neither that
theorem's equality classification nor its sharper small-order branch.

## No full $r$-block resolution in any color, for $r\ge3$

Suppose a color contains $r$ disjoint $K_r$'s, leaving a vertex $v$.
Apply the preceding result with $I=\{v\}$. Since an independent transversal
would augment $v$ to $r+1$, failure forces each list to have $r-1$
vertices and all its pairwise matching edges. There is also exactly one
target edge from $v$ to each block. Hence that color has at least

$$
(2r-1)\binom r2+r
$$

edges.

Each other color $G_j$ has $\alpha(G_j)\le r$, and its complement cannot be
$r$-partite: otherwise some part of its $r$-partition has $r+1$ vertices,
a forbidden color-$j$ clique. The preceding nonpartite gap gives

$$
e(G_j)\ge p_r(r^2+1)+r-1
=r\binom r2+2r-1.
$$

Summing exceeds $\binom{r^2+1}{2}$ by

$$
\frac{(r-1)(r-2)}2>0\qquad(r\ge3).
$$

Thus no color of a counterexample can contain $r$ disjoint $K_r$'s.
In particular, extending an affine-plane example must alter edges in
every original singleton-direction class; retaining even one complete
resolution is impossible. The margin vanishes at the exceptional parameter
$r=2$.

## A summed local-clique restriction

The quadratic form version of the new independence theorem, evaluated
on the uniform probability vector, gives for each color

$$
2e(G_i)+N+\sum_v c_i(v)\ge \frac{2N^2}{r},
\qquad N=r^2+1.
$$

Let $m(v)$ be the number of colors in which $v$ lies in a $K_r$.
Since $c_i(v)\le r-1+\mathbf1_{\{c_i(v)=r\}}$, summing the preceding
inequalities over colors gives

$$
\sum_v m(v)\ge2N.
$$

More generally, applying the same common weight vector to every color gives

$$
\sum_v\frac{1}{r-1+\sum_i c_i(v)}\le1.
$$

These inequalities do not force a large packing in any one color.
That missing link, rather than an arithmetic evaluation of the inequalities,
is the present obstacle.

### Joint deficit and irregularity budget

There is an exact refinement retaining the slack in the reciprocal
inequality. Put

$$
A_i(v)=d_i(v)+c_i(v)+1,\quad
D_i=\sum_v(r-c_i(v)),\quad
E_i=e(G_i)-rN/2,\quad \mu=2N/r.
$$

Then

$$
\boxed{D_i+\sum_v\frac{(A_i(v)-\mu)^2}{A_i(v)}
\le(1-2/r)N+2E_i.} \tag{15}
$$

Indeed, the localized bound gives $\sum_v2/A_i(v)\le r$.
Sum the exact identity

$$
\frac1A=\frac1\mu-\frac{A-\mu}{\mu^2}
+\frac{(A-\mu)^2}{\mu^2A}
$$

and use $2N/\mu=r$. It gives
$\sum_v(A_i(v)-\mu)\ge\sum_v(A_i(v)-\mu)^2/A_i(v)$;
expanding its left side proves (15). Summing over colors yields

$$
\boxed{\sum_iD_i+
\sum_{i,v}\frac{(A_i(v)-\mu)^2}{A_i(v)}\le(r-2)N.} \tag{16}
$$

Thus degree irregularity and clique deficits consume the same budget.
This has not forced a clique resolution or excluded either core.

There is also a small integrality improvement. The integer left side
of $2e(G_i)+N+\sum_v c_i(v)\ge2N^2/r$ is at least
$2r^3+4r+1$. Summing separately rounded inequalities gives

$$
\sum_iD_i\le(r-2)r^2,\qquad
\sum_v m(v)\ge2r^2+r.
$$

The resulting minimum number of full cliques remains $2r+1$;
no stronger packing conclusion is implicit.

## Full-clique deletion with overlaps

**Proved.** Disjointness is unnecessary for the extension lemma in the
least-color nonneighborhood. Let $Q_1,\ldots,Q_F$ be distinct target
$K_r$'s, and let $I$ be independent outside their union. If
$|I|+F\le r$, then $I$ extends by one representative from each clique.

Use only vertices private to a clique within this family. If $Q_j$
meets $s_j$ other cliques, it has at least $r-s_j$ private vertices.
A private representative of a clique meeting $Q_j$ is anticomplete to
its private vertices: its unique possible neighbor in $Q_j$ is their
intersection point. Thus, in any sequential choice, the previously
chosen representatives and $I$ forbid at most
$F-1-s_j+|I|$ private vertices of $Q_j$. At least one choice remains.

Apply this to a family in $U$, the nonneighborhood of the least-color
minimum-degree vertex. Put

$$
t=r-d,\qquad s=r-1-F,\qquad
M=Fr-\left|\bigcup_{j=1}^FQ_j\right|.
$$

For $s\ge1$, the residual has order $rs+t+M$ and independence at
most $s$. Clique edge sets are disjoint even when their vertices
overlap, so the usual edge budget still subtracts $F\binom r2$.
If the residual is $K_r$-free, subtraction of the localized lower
bound gives exactly

$$
E-L=\frac r2(F-t-3M)-\frac{t(t-1)}2
-\frac{(t+M)^2}{s}.
$$

In particular, stopping requires

$$
\boxed{F\ge t+3M+1.}
$$

For $t=1$, every unit of overlap therefore costs at least three
additional full cliques: $F\ge3M+2$. This removes the need to find a
disjoint subfamily, but still does not force indefinite continuation.

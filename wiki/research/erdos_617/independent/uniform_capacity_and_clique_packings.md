---
name: research/erdos_617/independent/uniform_capacity_and_clique_packings
title: Independent investigation of Erdős Problem 617
desc: Third unverified isolated investigation, preserved below the metadata; checked conclusions are in independent-comparison.
tags: [unverified, archive]
sources: []
created: 2026-09-22T12:10:32Z
updated: 2026-09-22T12:10:32Z
---


# Independent investigation of Erdős Problem 617

***

## Status, sources, and conventions

**Unresolved.** This investigation neither proves the assertion for every
$r\ge3$ nor constructs a counterexample. It establishes parameterized
structural restrictions and records concrete failed approaches. It does not
claim another isolated fixed case.

The only supplied mathematical sources used were:

- **[Problem 617](../../../problems/extremal_graph_theory/E0617/_index.md)**, the
  canonical problem page.
- **[source record](../../../../library/extremal_graph_theory/erdos_gyarfas_1999_split_balanced_colorings_complete_graphs/_index.md)**,
  Erdős and Gyárfás, *Split and balanced colorings of complete graphs* (1999).

There was no web browsing and no consultation of later research notes. The notes
linked below were generated during this investigation. Turán's theorem and, for
the homogeneous-coloring observation, Brooks' theorem are used as in the
supplied paper. The stability and other structural lemmas are proved here rather
than attributed to outside sources.

“Hypothetical counterexample” means an $r$-edge-coloring of $K_{r^2+1}$ in
which every $(r+1)$-set sees every color. Write $G_i$ for its color-$i$
graph. Thus

$$
\alpha(G_i)\le r\qquad(1\le i\le r).
\tag{C}
$$

For every $(r+1)$-set $X$,

$$
e(G_i[X])\le \binom{r+1}{2}-(r-1)=\binom r2+1.
\tag{L}
$$

In particular, $\omega(G_i)\le r$. If $A$ is a monochromatic $K_r$ of
color $i$, then

$$
d_i(x,A)\le1\qquad(x\notin A).
\tag{K}
$$

Indeed, the $r$ edges from $x$ to $A$ must supply every other color.

## 1. The hereditary edge budget

Let $T_r(m)$ be the minimum edge count of an $m$-vertex graph with
independence number at most $r$. By Turán's theorem it is the sum of
$\binom{b_j}{2}$ for an equitable partition into $r$ parts. In particular,

$$
T_r(ar+1)=r\binom a2+a.
$$

A necessary condition on each individual color graph is

$$
e(G_i[S])\le \binom{|S|}{2}-(r-1)T_r(|S|)
\quad\text{for every }S\subseteq V.
\tag{H}
$$

This follows by counting the edges required by the other $r-1$ colors on
$S$.

Condition (H) is essential. An individual graph can pass the minority-edge
bound, (L), and several small-independence tests while failing (H). Such a graph
is not a counterexample coloring.

For the whole graph set

$$
T=T_r(r^2+1)=r\binom r2+r
=\frac{r(r^2-r+2)}2.
$$

The total edge surplus over $rT$ is

$$
\binom{r^2+1}{2}-rT=\frac{r^2(r-1)}2.
\tag{B}
$$


## 2. Main checked result: uniform capacity for small independence number

The following complete argument was also preserved, with an independent
proof audit including the numerical constants and empty-set cases, in
companion notes that are not retained.

### Theorem

Let $a\ge2$ be an integer. If

$$
 r\ge256a^6,
$$

then, for every color $i$ and every vertex subset $H$,

$$
 \alpha(G_i[H])\le a\quad\Longrightarrow\quad |H|\le ar. \tag{P_a}
$$

In particular, this gives $(P_a)$ simultaneously for all integers
$2\le a\le\lfloor(r/256)^{1/6}\rfloor$.

We first prove the elementary stability fact needed in the argument.

### Lemma: a near-Turán partition

Let $s\ge1$, and let $F$ be a $K_{s+1}$-free graph on $n$ vertices. Define

$$
 Q_s(n)=\frac{s-1}{2s}n^2,\qquad D=Q_s(n)-e(F)\ge0.
$$

There is a partition $V(F)=V_1\dot\cup\cdots\dot\cup V_s$ such that the total
number $I$ of edges internal to the parts is at most $D$. For this partition,
writing $n_i=|V_i|$ and $W$ for the number of missing cross-part pairs, one has

$$
 W\le2D,
 \qquad
 |n_i-n/s|\le2\sqrt D\quad(1\le i\le s). \tag{7}
$$


**Proof.** Induct on $s$. For $s=1$, the graph is edgeless and the result is
immediate. For $s\ge2$, choose a maximum-degree vertex $v$, with degree $d$, and
put $U=N_F(v)$ and $B=V(F)\setminus U$. The graph $F[U]$ is $K_s$-free. Set

$$
 D_U=Q_{s-1}(d)-e(F[U])\ge0.
$$

The maximum-degree condition gives

$$
 e(U,B)+2e(B)\le d|B|,
$$

so

$$
 e(F)\le e(F[U])+d(n-d)-e(B).
$$

The identity

$$
 Q_s(n)-Q_{s-1}(d)-d(n-d)
 =\frac{s}{2(s-1)}\left(d-\frac{s-1}{s}n\right)^2
$$

therefore implies $D\ge D_U+e(B)$. By induction, partition $U$ into $s-1$ parts
with at most $D_U$ internal edges and take $B$ as the last part. The resulting
partition has $I\le D$.

The number of all possible cross-part pairs is

$$
 \frac{n^2-\sum_i n_i^2}{2}
 =Q_s(n)-\frac12\sum_i(n_i-n/s)^2.
$$

Subtracting the actual number $e(F)-I$ of cross-part edges gives

$$
 W=D+I-\frac12\sum_i(n_i-n/s)^2. \tag{8}
$$

Since $0\le W$ and $I\le D$, this proves (7). $\square$

### Proof of the theorem

If $(P_a)$ fails, restrict to a subset $H$ of exactly

$$
 n=ar+1
$$

vertices with $\alpha(G_i[H])\le a$. Let $F$ be the graph on $H$ formed by edges
of all colors other than $i$. Then $F$ is $K_{a+1}$-free.

For each other color $j$, the graph $G_j[H]$ has independence number at most
$r$. The complement form of Turán's theorem gives

$$
 e(G_j[H])\ge(r-1)\binom a2+\binom{a+1}{2}
 =r\binom a2+a.
$$

Summing over the $r-1$ colors different from $i$ yields

$$
 e(F)\ge(r-1)\left(r\binom a2+a\right).
$$

Consequently its deficit from the real Turán bound satisfies

$$
 \begin{aligned}
 D&=Q_a(ar+1)-e(F)\\
 &\le\left(\binom a2-1\right)r+a+\frac{a-1}{2a}\\
 &\le a^2r. \tag{9}
 \end{aligned}
$$

The last inequality holds for all $a\ge2,r\ge1$.

Apply the lemma with $s=a$. Its partition has at most $D$ internal edges, at
most

$$
 W\le2D\le2a^2r \tag{10}
$$

missing cross-part pairs, and each part has size at least

$$
 n/a-2\sqrt D\ge r-2a\sqrt r\ge\frac{9r}{10}. \tag{11}
$$

For the final inequality it suffices that $r\ge400a^2$, which follows from
$r\ge256a^6$ and $a\ge2$.

For a vertex $x$, let $b(x)$ be the number of its nonneighbors in parts
different from its own. Define

$$
 X=\{x:b(x)\ge2r/5\},\qquad k=|X|.
$$

Since $\sum_xb(x)=2W$, we have

$$
 k\le\frac{2W}{2r/5}\le10a^2. \tag{12}
$$


We claim that every set $C_i=V_i\setminus X$ is independent in $F$. Suppose that
$xy$ is an edge with $x,y\in C_i$. In every other **full part** $V_j$, the
common-neighbor set

$$
 S_j=N_F(x)\cap N_F(y)\cap V_j
$$

has size strictly greater than

$$
 \frac{9r}{10}-\frac{2r}{5}-\frac{2r}{5}=\frac r{10}.
$$

Choose independently and uniformly one vertex from each of these $a-1$ sets. The
probability that some chosen pair is a nonedge is at most

$$
 \sum_{j<\ell,\,j,\ell\ne i}
 \frac{e_{\overline F}(S_j,S_\ell)}{|S_j||S_\ell|}
 \le\frac{100W}{r^2}
 \le\frac{200a^2}{r}<1. \tag{13}
$$

For $a=2$ the sum is empty, which is harmless. Thus there is an $(a-1)$-clique
of common neighbors of $x,y$, giving a forbidden $K_{a+1}$. This proves the
claim. Notice that (13) uses the full parts $V_j$, not the smaller cores $C_j$;
no subtraction of marked vertices is required here.

Next consider any $x\in X$. It has at most $\sqrt W$ neighbors in at least one
of the cores $C_1,\ldots,C_a$. Otherwise choose uniformly one neighbor of $x$ in
each core. The same union bound, now with all $a$ cores, gives failure
probability at most

$$
 \frac{W}{\min_j |N_F(x)\cap C_j|^2}<1.
$$

This would produce a $K_a$ inside $N_F(x)$, hence a forbidden $K_{a+1}$. The
argument also covers $W=0$: if every core contained a neighbor of $x$, all cross
pairs would be edges. If a core is empty, its zero neighbor count already proves
the assertion.

Assign every $x\in X$ to a core in which it has at most $\sqrt W$ neighbors.
Since the cores are independent, the total number of internal edges of this new
$a$-partition is at most

$$
 \begin{aligned}
 k\sqrt W+\binom k2
 &\le10\sqrt2\,a^3\sqrt r+50a^4. \tag{14}
 \end{aligned}
$$

Under $r\ge256a^6$, one has $\sqrt r\ge16a^3$ and $a\ge2$, so

$$
 10\sqrt2\,a^3\sqrt r
 \le\frac{5\sqrt2}{8}r
 \le\frac{15}{16}r,
 \qquad
 50a^4\le\frac{25}{128a^2}r\le\frac{25}{512}r.
$$

Thus (14) is at most $505r/512<r-1$; indeed $r\ge256\cdot2^6=16384>512/7$.

Since $|H|=ar+1$, one part of this new $a$-partition has at least $r+1$
vertices. Any $(r+1)$-subset of that part spans fewer than $r-1$ edges of $F$.
Yet every such set must have at least one edge in each of the $r-1$ colors other
than $i$, requiring at least $r-1$ edges of $F$. This contradiction proves
$(P_a)$. $\square$


## 3. Stronger capacity statements at independence two and three

These arguments hold uniformly in $r$; they do not reprove a single isolated
value. Their full provenance and an independent check were recorded in companion
notes that are not retained.

### Independence two

The preceding template analysis is superseded by the following general theorem.

**Theorem (two-slot capacity).** In a hypothetical counterexample, every vertex
set $S$ satisfying $\alpha(G_i[S])\le2$ has $|S|\le2r$, for every color $i$.

**Proof.** Put $H=G_i[S]$ and $m=|S|$, and suppose $m>2r$. The earlier local
$K_r$ lemma shows that $H$ cannot contain $K_r$: otherwise its complement
outside that clique would itself be a clique and $m\le2r$. Thus
$\omega(H)\le r-1$. Since $\alpha(H)\le2$, the nonneighbors in $H$ of any vertex
form a clique of $H$, of size at most $r-1$. Consequently


$$
e(\overline H)\le \frac{m(r-1)}2.
$$


Every other color $j$ induces a graph on $S$ with independence number at most
$r$. Every graph on $m$ vertices and $e$ edges has an independent set of size at
least $m-e$: choose at most one endpoint from each edge to obtain a vertex
cover. Hence $e(G_j[S])\ge m-r$. Summing the $r-1$ other colors gives


$$
e(\overline H)\ge(r-1)(m-r)>\frac{m(r-1)}2,
$$


because $m>2r$, a contradiction. $\square$

The proof only requires pairwise edge-disjoint spanning graphs $G_1,\ldots,G_r$
with $\alpha(G_i)\le r$: one may first color any uncovered pairs arbitrarily,
which preserves all these independence bounds. It therefore applies to proposed
packings as well as complete edge partitions.

**Corollary.** In a hypothetical counterexample, every color graph has a
connected component of independence number at least three. Indeed, if all its
components had independence number at most two, a clique component has at most
$r$ vertices and a component of independence number two has at most $2r$
vertices. Summing would give $|V|\le r\alpha(G_i)\le r^2$.

This eliminates every construction assembled in each color from cliques and
pentagon-type independence-two pieces, irrespective of their sizes, balance,
overlap supports, or edge densities.

### Equality in the independence-two bound

Here $r\ge6$.

**Theorem.** If $S$ has $2r$ vertices and $\alpha(G_i[S])\le2$ in a hypothetical
counterexample, then $S$ is the disjoint union of two monochromatic $K_r$'s in
color $i$, and all color-$i$ edges between them form a matching.

**Proof.** Again write $H=G_i[S]$. If $H$ contains a $K_r=A$, the local $K_r$
lemma makes $S\setminus A$ a clique, hence another $K_r$. Every vertex of either
clique has at most one neighbor in the other by the local $K_r$ restriction, so
the edges between them form a matching.

Suppose instead that $H$ has no $K_r$. Its complement $F$ is triangle-free and
has maximum degree at most $r-1$. The proof of the capacity theorem gives


$$
r(r-1)\le e(F)\le r(r-1),
$$


so $F$ is $(r-1)$-regular. (Each other color restricted to $S$ has exactly $r$
edges and independence number at most $r$, and is therefore a perfect matching:
if two of these edges met, a vertex cover with at most $r-1$ vertices could be
selected.)

We use the elementary fact that a nonbipartite triangle-free graph on $N$
vertices has minimum degree at most $2N/5$. To prove it, take a shortest odd
cycle $C$ of length $q\ge5$. It has no chord, and any vertex outside $C$ has at
most two neighbors on $C$. For if it had at least three, the cyclic gaps between
consecutive neighbors are at least two, and one is odd; that odd gap has length
at most $q-4$, producing an odd cycle of length at most $q-2$ through the
outside vertex. This contradicts minimality. Counting incidences into $C$ gives


$$
q\delta\le\sum_{v\in C}d(v)\le2N,
$$


and $q\ge5$ proves the fact. Applied to $F$, it shows that $F$ is bipartite,
since


$$
r-1>\frac{4r}{5}\qquad(r\ge6).
$$


One side of a bipartition of $F$ has at least $r$ vertices, giving a $K_r$ in
$H$, a contradiction. $\square$

### Independence three

For $r\ge6$, the equality theorem yields another capacity statement: every $S$
with $\alpha(G_i[S])\le3$ has $|S|\le3r$.

Indeed, suppose $H=G_i[S]$ has $m>3r$. It cannot contain an independence-two
induced subgraph on $2r$ vertices. Such a set would, by the equality theorem,
split into two color-$i$ $K_r$'s $A,B$, with a matching between them. If two
vertices $x,y$ outside $A\cup B$ were nonadjacent in color $i$, at most two
vertices in each of $A,B$ could be adjacent to either $x$ or $y$. Since $r\ge4$,
there are at least two candidates in each clique, and the matching between $A$
and $B$ permits a nonadjacent choice $a,b$. Then $\{a,b,x,y\}$ is independent in
$H$, impossible. Thus $H\setminus(A\cup B)$ is a clique, so it has at most $r$
vertices and $m\le3r$, again impossible.

Every nonneighborhood in $H$ has independence number at most two, and therefore
has size at most $2r-1$ (the size $2r$ case was just ruled out). Thus
$\Delta(\overline H)\le2r-1$. The complement form of Turán's theorem supplies
the universal supporting-line bound


$$
e(G_j[S])\ge3m-6r\qquad(j\ne i).
$$


One way to see the supporting line is to write the Turán minimum as
$\sum_{a=1}^r\binom{n_a}{2}$ with $\sum_a n_a=m$ and use
$\binom{n_a}{2}\ge3n_a-6$ for every nonnegative integer $n_a$; this last
difference is $(n_a-3)(n_a-4)/2\ge0$.

Consequently


$$
0\ge (r-1)(3m-6r)-\frac{m(2r-1)}2.
$$


The right side is increasing in $m$ and at $m=3r+1$ equals $(r-5)/2>0$, a
contradiction.


## 4. Minimal unresolved subgraphs

For $r\ge6$, put

$$
A_r=\max\left\{3,\left\lfloor(r/256)^{1/6}\right\rfloor\right\}.
$$

Every color of a hypothetical counterexample has a connected induced subgraph
$H$ with

$$
|H|=ar+1,\qquad \alpha(H)=a>A_r,\qquad \delta(H)\ge r.
\tag{M}
$$


To prove this, choose an inclusion-minimal induced set with $|H|>r\alpha(H)$;
the whole color graph is such a set. Write $a=\alpha(H)$. Deleting one vertex
and applying minimality gives

$$
|H|-1\le r\alpha(H-v)\le ra,
$$

so $|H|=ar+1$. If a vertex had degree at most $r-1$, deleting its closed
neighborhood would leave at least $(a-1)r+1$ vertices of independence number
at most $a-1$, a smaller violation. Disconnectedness would also contradict
minimality by adding the capacity inequalities for the components. The proved
capacity statements force $a>A_r$.

This is a precise remaining obstruction, not a contradiction. No argument
establishes $a\le A_r$. Applying the main theorem with $a=r$ is invalid,
since its hypothesis would be $r\ge256r^6$.

## 5. Clique packings and interaction between colors

### 5.1 A strengthened lower bound for every color

Every graph satisfying (C) and (L) has

$$
e(G_i)\ge T+r-1.
\tag{E}
$$

Repeatedly choose a minimum-degree vertex of the remaining graph and delete its
closed neighborhood $B_j$, of size $b_j$. The chosen vertices are
independent, so there are at most $r$ batches. If $q_j$ is the number of
missing edges inside $B_j$, the number of edges removed at that step is at
least

$$
b_j(b_j-1)-e(G_i[B_j])=\binom{b_j}{2}+q_j.
$$

Thus

$$
e(G_i)\ge\sum_j\binom{b_j}{2}+\sum_jq_j.
$$

Convexity gives the first sum at least $T$. Some batch has at least $r+1$
vertices, so (L) supplies $q_j\ge r-1$. More information can be retained:

$$
e(G_i)\ge
\sum_j\binom{b_j}{2}+
\sum_{b_j\ge r+1}
\left\lceil\frac{(r-1)b_j(b_j-1)}{r(r+1)}\right\rceil.
$$


### 5.2 Matching transversals

Suppose $k$ disjoint parts each have at least $k-1$ vertices, and the
forbidden pairs between every two parts form a matching. If there is no
independent transversal, all parts have size exactly $k-1$, and the cross
edges form $k-1$ disjoint transversal $K_k$'s.

A part of size at least $k$ could be left last in a greedy choice. A missing
edge from a pairwise perfect matching can similarly be exploited by starting
with an unmatched vertex and leaving its opposite part last. Hence all pairwise
matchings are perfect. If two nonadjacent vertices in different parts share a
matched neighbor in a third part, choose those two first and the third part
last; the last part loses at most $k-2$ choices. This proves coherence. When
applying the lemma to monochromatic clique rows, discard within-row edges: they
do not affect transversals.

If a color had $r$ disjoint $K_r$'s, its remaining vertex would need one
neighbor in each row. Avoiding those neighbors and applying this lemma forces
$r-1$ crossing $K_r$'s. That color has at least

$$
(2r-1)\binom r2+r
$$

edges. Together with (E) for the other colors, this exceeds $\binom{r^2+1}{2}$
by $(r-1)(r-2)/2$. Thus no color has such a packing.

### 5.3 Cross-color fibers

Let $p$ be the largest number of disjoint monochromatic $K_r$'s in any one
color. Fix a color-$i$ clique $A=K_r$. The star of an outside vertex into
$A$ is either rainbow or omits $i$ and repeats exactly one other color.

For $j\ne i$, let $E_j(A)$ consist of the vertices whose repeated color is
$j$, and let $e_j=|E_j(A)|$. Every remaining outside vertex has a unique
color-$j$ neighbor in $A$. For each $a\in A$, its fiber together with
$a$ is a color-$j$ clique: otherwise $(A\setminus\{a\})\cup\{x,y\}$ would
omit $j$. These $r$ disjoint cliques have total size $r^2+1-e_j$, so their
total deficit from size $r$ is $e_j-1$. At least $r-e_j+1$ are full
$K_r$'s. Consequently

$$
e_j\ge r-p+1,
$$

and, writing $t_i(A)$ for the outgoing color-$i$ edges of $A$,

$$
t_i(A)\le (r-1)(p-1)+1.
\tag{F}
$$


### 5.4 Excluding a packing of $r-1$ full cliques

The result is

$$
p\le r-2.
\tag{P}
$$

Here are the main calculations; all steps were recorded and independently
audited in companion notes that are not retained.

Suppose $p=r-1$, with rows $A_1,\ldots,A_{r-1}$ and residue $R$ of size
$r+1$. Let $F=\overline{G_i[R]}$, and let $s$ count its nonisolated
vertices. Since $e(F)\ge r-1$, $s\ge2$. Any edge $xy$ of $F$ must have
distinct color-$i$ neighbors in every row. The transversal lemma, after
deleting those two neighbors, forces at least $r-2$ color-$i$ edges between
every pair of rows. Each of the $s$ residue vertices has a color-$i$
neighbor in every row. Thus

$$
t_i(A_a)\ge(r-2)^2+s.
$$

Comparing with (F) gives $s\le r-1$.

Each $e_j(A_a)\ge2$, while

$$
\sum_{j\ne i}e_j(A_a)\le3r-3-s.
$$

Therefore at least $s$ other colors have $e_j=2$, and hence also have
$r-1$ disjoint full cliques. This is the crucial propagation to other colors.

For $r\ge5$, $e(F)\ge4$ implies $s\ge4$. Any propagated color has at least

$$
(r-1)\binom r2+(r-2)\binom{r-1}{2}+4(r-1)
$$

edges. Its surplus over $T$ is

$$
A=\frac{r^3-6r^2+15r-12}{2}.
$$

There are at least three such colors. Their surpluses and (E) for the rest
exceed the budget (B), because

$$
3A+(r-3)(r-1)-\frac{r^2(r-1)}2
=\frac{(r-3)(r-2)(2r-5)}2>0.
$$

The same structural statement at the lower parameters follows from the canonical
residue calculation in the linked proof; no separate new fixed case is claimed
here. Substituting (P) into (F) gives

$$
t_i(A)\le(r-2)^2.
$$


### 5.5 Last derived extension: $p\le r-3$ for $r\ge8$

The complete derivation was preserved in a companion note that is not retained.
Unlike the preceding packing theorem, this extension did not complete a separate
independent audit. Its proof was checked locally, including the following
support lemma and budget calculation; it is kept distinct from the independently
audited results.

A graph $F$ on $2r+1$ vertices containing a triangle, with all triangle
vertices lying in a set $S$ of size $s\le r$, satisfies

$$
e(F)\le r^2+s-1.
\tag{TS}
$$

To see this, symmetrize $Y=V(F)\setminus S$ without creating a triangle
meeting $Y$. Choose a maximum-degree $y\in Y$, put $A=N_Y(y)$,
$B=Y\setminus A$, and replace every vertex of $B$ by a twin of $y$. The
edge gain is

$$
\sum_{b\in B}(d(y)-d(b))+e(F[B])\ge0.
$$

Then make the independent set $A$ twins of a vertex with maximum number of
neighbors in $S$. The resulting $Y$ is complete bipartite. Its two
neighborhoods $C,D$ in $S$ are disjoint independent sets. With
$t=|S\setminus(C\cup D)|\ge1$, counting yields

$$
e(F)\le\left\lfloor\frac{(2r+1-t)^2}{4}\right\rfloor
+ts-\frac{t(t+1)}2
\le r^2+s-1.
$$


Now suppose $p=r-2$. The residue has $2r+1$ vertices, so the two-slot
capacity theorem forces an independent triple in its color-$i$ graph. Let
$s$ be the number of vertices participating in such triples. The other colors
require

$$
e(\overline{G_i[R]})\ge(r-1)(r+2)=r^2+r-2.
$$

Applying (TS), if necessary, gives $s\ge r-1$. Each independent triple and the
matching-transversal lemma force $r-3$ cross edges between every pair of rows
and attachments from all $s$ supported vertices. The duplicate-color budget
then propagates the same packing to at least three other colors.

Each of these at least four colors has surplus at least

$$
A_2=\frac{r^3-8r^2+15r-14}{2}
$$

over $T$. The budget excess is

$$
4A_2+(r-4)(r-1)-\frac{r^2(r-1)}2
=\frac{3r^3-29r^2+50r-48}{2}
=\frac{(r-8)(3r^2-5r+10)}2+16>0
$$

for $r\ge8$. This yields the stated extension. No argument yet forces any
color to have a packing of size $r-2$.

## 6. The affine-plane extension: exact and quantitative obstructions

Assume an affine plane of order $r$ exists. Start with the paper's coloring of
its $r^2$ points: $r-1$ parallel classes get separate colors, and the last
two classes share the remaining color.

### Unchanged extension fails

For a singleton-class color $i$, the independent $r$-sets are all
transversals of its $r$ lines. The new vertex's color-$i$ neighbors must
meet every such transversal, and therefore must contain an entire old line. Two
singleton colors force two intersecting lines, assigning two colors to the edge
from the new vertex to their intersection. Thus the unchanged affine coloring
cannot be extended.

### Recolored-edge count

Let $A_i$ be the old points joined to the new vertex in color $i$,
$a_i=|A_i|$, and let $t_i,d_i$ count old edges recolored into and out of
color $i$. Put $t=\sum_i t_i=\sum_i d_i$.

For a singleton color with no entire line in $A_i$, let
$b_1\le b_2\le\cdots\le b_r$ be the positive residual line sizes. Every
transversal must contain an added color-$i$ edge. A random transversal gives

$$
t_i\ge b_1b_2\ge b_1+b_2-1\ge2r-a_i-1.
$$

Thus $a_i+t_i\ge2r-1$.

If $A_i$ contains a whole old line, that line together with the new vertex
needs at least $r-1$ recolored edges to supply other colors. Turán's bound
gives

$$
a_i+t_i\ge r+d_i\ge2r-1.
$$

Equality would force a forbidden $K_{r+1}$, so this case is strict.

For the merged color, independent $r$-sets are permutation transversals of an
$r\times r$ grid. The union bound gives

$$
a_r+\frac{t_r}{r-1}\ge r.
$$

Summing proves

$$
t\ge(r-1)^2+\frac{r-2}{r-1}t_r.
$$

Equality $t=(r-1)^2$ is impossible. In that equality case the merged star is
an entire line; the nearly-full singleton star lines must all meet at one point
on it. The remaining points force $a_i=r,t_i=r-1$ and a specific added-edge
star in every singleton color. Some added edge must have been removed from
another singleton color. But deleting an edge from a singleton line requires at
least $r$ additions to that color: take the two endpoints and one random point
from every other old line, and apply the union bound. This contradicts
$t_i=r-1$. Hence

$$
t\ge(r-1)^2+1.
\tag{AR}
$$


### Vertex-cover bound for the changed edges

Delete $k$ old points and keep the old coloring on the remainder; allow
$k+1$ new vertices with arbitrary incident edges. Define

$$
q=\min\{d\ge1:\binom{d+1}{2}\ge r-1\}.
$$

A hypothetical counterexample obtained this way must satisfy

$$
k\ge
\left\lceil\frac{(r-1)q^2}{r+q-2}\right\rceil
=2r-O(\sqrt r).
\tag{AV}
$$


For every singleton direction, some old line must lose at least $q$ points.
Otherwise every new vertex must send that color to an entire residual line. If
line $L$ loses $d_L<q$ points, it can be chosen by at most $d_L$ new
vertices: $d_L+1$ such vertices and its $r-d_L$ surviving points form an
$(r+1)$-set seeing at most $1+\binom{d_L+1}{2}<r$ colors. There are $k+1$
new vertices but $\sum_Ld_L=k$, a contradiction.

Choose $q$ deleted points on one heavy line in each of the $r-1$ directions.
If $c_p$ counts their incidences at a deleted point, then

$$
\sum_pc_p=(r-1)q,\qquad
\sum_pc_p(c_p-1)\le(r-1)(r-2).
$$

Cauchy–Schwarz proves (AV). Deleting a vertex cover of the recolored-old-edge
graph puts any one-vertex affine repair in this situation, proving the
advertised vertex-cover restriction.

Full equality arguments and a separate exact small-replacement obstruction were
recorded in a companion note that is not retained. These are necessary
conditions on affine repairs, not a closeness theorem for arbitrary colorings.

## 7. Failed approaches and explicit one-color constructions

### 7.1 Why a minority graph alone is insufficient

For every $r=5u$, $u\ge3$, consider

$$
G=(r-2)K_r\ \dot\cup\ J,
$$

where $\overline J$ is the independent-bag blow-up of $C_5$ with bag sizes

$$
(2u+1,2u,2u,2u,2u).
$$

Then

$$
|G|=r^2+1,\quad \alpha(G)=\omega(G)=r,\quad
e(J)=30u^2+u,
$$

and

$$
\frac{r(r^2+1)}2-e(G)=\frac{15u^2-7u}{2}>0.
$$

It satisfies (L). An $(r+1)$-set meeting an ordinary component has at least
$r$ cross-component nonedges. Within $J$, minimize

$$
\sum_{\ell=0}^4x_\ell x_{\ell+1},\qquad \sum_\ell x_\ell=5u+1
$$

under the bag capacities. Moving two non-boundary coordinates while keeping
their sum makes the objective affine or concave, so a minimum has at most one
non-boundary coordinate. Two full bags and a third partial bag then yield at
least $2u^2\ge5u-1$ nonedges.

Thus a hypothetical lemma saying “minority edge count plus (L) forces an
independent $(r+1)$-set” is false. This graph cannot actually be a color graph
of a counterexample: its exceptional $J$ violates the proved two-slot
capacity.

A sharper family, recorded in a companion note that is not retained, works for
every $r\ge27$. Put

$$
L=\lceil r^{1/3}\rceil,\quad
b=\left\lceil\frac{r-1}{L}\right\rceil,\quad
c=2L-1,\quad a=r+1-b-L,
$$

take $\overline J=C_5[a,a,b,c,b]$, and again set $G=(r-2)K_r\dot\cup J$. A
weighted five-bag minimization shows every $(r+1)$-set in $J$ has at least
$bL\ge r-1$ nonedges. Writing $q=L-1$,

$$
e(G)=T+D,\qquad
D=r+2rq-q^2+b^2-2b(2q+1)=O(r^{4/3})<\binom r2.
$$

An elementary complementary lower bound in the same note shows the $r^{4/3}$
order is sharp for this particular independence-two exceptional-block model.
This still does not produce compatible color graphs.

### 7.2 Growing independence and alpha-criticality do not rescue that shortcut

A more elaborate individual graph also passes all capacity tests below a growing
parameter. For every integer $a\ge2$, let

$$
r=16a^3,\qquad g=4a,\qquad t=ag+1,\qquad
B=r-t-g.
$$

Let $H$ be the clique blow-up of $C_{2a+1}$ with $a$ alternating heavy
bags of size $B$ and $a+1$ light bags of size $t$; the two extra
consecutive bags are light. Set

$$
G=(r-a)K_r\ \dot\cup\ H.
$$

Then

$$
|H|=ar+1,\quad \alpha(H)=a,\quad
\alpha(G)=r.
$$

Every edge is alpha-critical: deleting an intra-bag edge permits two selected
vertices there and an independent set of size $a-1$ on the remaining path;
deleting an inter-bag edge permits its two endpoints and an independent set of
size $a-1$ on the complementary path.

All adjacent bag sums are at most $r$. Any set whose support omits a cycle bag
has path components; pairing adjacent bags proves $|S|\le r\alpha(G[S])$.
Hence all capacity statements with independence number less than $a$ hold. In
fact the overcapacity sets are exactly the whole $H$ together with zero or
more complete ordinary $K_r$ components.

The minimum number of nonedges on an $(r+1)$-set in $H$ is

$$
t(g+1)=(4a^2+1)(4a+1)>r.
$$

The proof again pushes coordinates to bag boundaries. At most one heavy bag can
be full; if one is full, the remaining selected vertices force at least
$t(g+1)$ nonedges. If no heavy bag is full, a partial heavy bag and at least
two full light bags force the same bound. Equality is attained by a heavy bag
and portions of its two neighboring light bags.

Its edge surplus is

$$
e(G)-T
=(a-1)\bigl(64a^5-16a^4+8a^3-8a^2-1\bigr)
<64a^6=\frac{r^2}{4}<\binom r2.
$$

Full proofs and an independent audit were recorded in companion notes that
are not retained.

**Important limitation:** this example obstructs only an inference from minority
sparsity, (L), alpha-criticality, and the smaller capacity statements. It does
**not** satisfy all necessary conditions for a color graph. In particular its
surplus inside $H$ is of order $r^2$, while (H), applied to $|H|=ar+1$,
permits only order $a^2r$, which here is order $r^{5/3}$. The hereditary
edge budget already rejects it. It is therefore not evidence of a counterexample
to the original problem.

### 7.3 Other construction attempts

- If every color graph is regular, one has degree at most $r$; Brooks' theorem
  then yields an independent $(r+1)$-set or a forbidden $K_{r+1}$. This
  rules out color-preserving vertex-transitive/difference colorings, but not
  actions that also permute colors.
- The asymmetric $C_5$ clique blow-up with bags $(r-1,1,r-1,1,1)$, attached
  to $r-2$ ordinary $K_r$'s, has attractive edge and independence counts. It
  fails (K): an outside singleton has $r-1$ neighbors in a full $K_r$.
- Putting every color's independence-two defect on two affine lines plus one
  common added vertex fails the two-slot capacity theorem. Merely rearranging
  those two-line supports is not enough.
- Lexicographic and strong-product constructions did not give a valid
  independence bound with the required number of colors. No product construction
  was promoted to a theorem.
- A stronger geometric statement forcing all color graphs to be near affine
  clique factors was not proved.
- The proposed shortcut “small total edge surplus forces a minimal overcapacity
  component of bounded independence” was not proved. The preceding
  individual-graph examples show why sparsity and local density alone are
  insufficient; (H) must also be retained.

## 8. Uncertainties and exact endpoint

The following are established in the record:

1. The universal capacity theorem for $r\ge256a^6$, and the sharper $a=2,3$
   statements.
2. The minimal-obstruction description (M).
3. The checked clique-packing restriction $p\le r-2$, with a separately
   recorded, locally checked extension $p\le r-3$ for $r\ge8$.
4. Quantitative obstructions to affine repairs.
5. Explicit individual graphs refuting weaker one-color proof strategies.

What is **not** established:

- A bound $a\le A_r$ for a minimal obstruction in (M).
- Capacity for all $a\le r$.
- A sufficiently large clique packing in any color.
- A theorem placing every hypothetical coloring close to an affine construction.
- An edge-disjoint packing of the proposed individual graphs.
- A counterexample coloring.

A further proposed improvement concerning arbitrary odd-cycle clique blow-ups
and a weighted-cycle inequality is not recorded in full. It is not needed for
any proved result above and is a provisional calculation until its precise
lemma and proof are checked. No conclusion of this investigation relies on it.

No substantial computation or numerical search was used as proof. The
mathematical claims above rest on the displayed counting, extremal, and
transversal arguments; the independent checks were proof audits, not
certificates of the original conjecture.

**The quantified assertion of Erdős Problem 617 remains unresolved in this
independent record.**

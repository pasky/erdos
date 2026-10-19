---
name: research/erdos_644/degree_bounded_selections
desc: A small-overlap triple and six-set certificate reduce any hypothetical three-quarter counterexample to a minimum bad subfamily of eight or nine edges.
tags: [proved, reductions, limitations]
sources: []
created: 2026-09-23T01:39:00Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/degree_bounded_selections

***

These are unrestricted selection lemmas, but they do not resolve either
assertion of Problem 644. Throughout, edges are nonempty and have size at most
$k$, and $P_r$ denotes the at-most-$r$ two-cover property. Repetitions are
allowed in tuples; $P_r$ applies to such tuples by passing to their underlying
subfamilies.

[Incidence-moment rounding](incidence_moment_rounding.md) gives a different
adaptive selection method: if every small vertex-deletion residual has large
fractional transversal number, successive edge choices can keep all degrees at
most three across seven rows. Its contrapositive yields low-fractional-cover
residuals and a sublinear transversal bound for sublinear VC dimension, but not
the unrestricted three-quarter coefficient.

## A balanced exclusion lemma

**Theorem.** For integers $p>b\ge1$, if

$$
\tau(\mathcal H)>\left\lceil\frac{(p-b)k}{b}\right\rceil,
$$

there is a $p$-tuple of edges, allowing repetitions, in which every point occurs
at most $b$ times.

**Proof.** Induct on $p$, putting $a=p-b$. If $a\le b$, repeat any edge $a$
times. Otherwise apply the induction hypothesis to obtain an $a$-tuple of
maximum point degree at most $b$. Its required bound is exactly $k$ smaller than
the displayed bound.

Let $d(x)\le b$ be a point's degree in this reference tuple. Distribute $x$ into
$d(x)$ consecutive bins cyclically among $b$ bins, continuing the cyclic counter
between points. A point never repeats within a bin, and the bin loads differ by
at most one. Thus the resulting sets $S_1,\ldots,S_b$ satisfy

$$
|S_j|\le\left\lceil\frac{\sum_xd(x)}b\right\rceil
\le\left\lceil\frac{ak}b\right\rceil<\tau(\mathcal H).
$$

Choose an edge missing each $S_j$. Every reference point misses at least $d(x)$
of these new edges, and hence has final degree at most $b$. Every other point
occurs only among the $b$ new edges. This proves the induction. $\square$

For a nonempty family, write $\nu_b^{\rm mult}$ for the largest size of an edge
multiset of maximum degree at most $b$. The theorem equivalently gives, when
this number is finite,

$$
\tau(\mathcal H)\le
\left\lceil\frac{(\nu_b^{\rm mult}-b+1)k}{b}\right\rceil.
$$


In particular, $\tau>\lceil3k/4\rceil$ gives seven rows of maximum point degree
four. In a $P_7$ family these rows still have a two-point cover. Its two spectra
therefore have sizes $4,3$ and are disjoint, or have sizes $4,4$ and intersect
in one row. Eliminating these covers, not merely eliminating degrees five and
above, is the missing step.

For the distinct-member $(p,q)$-intersection condition, where $p\ge q\ge2$, the
repeated version must not be applied directly. A distinct-edge version follows
with an additive $p-1$: before each new selection, add one point from each
previously selected distinct edge to the exclusion set. In the induction's
initial branch choose $a$ distinct reference edges instead of repeating one; the
assumed transversal bound ensures that sufficiently many edges exist. The same
induction then proves

$$
\tau(\mathcal H)\le
\left\lceil\frac{(p-q+1)k}{q-1}\right\rceil+p-1
$$

whenever every $p$ distinct edges contain $q$ with a common point. Families with
fewer than $p$ edges already have a $(p-1)$-point cover.

## A good triple with controlled pair intersections

Here a good triple has empty common intersection, and repetitions are allowed.

**Selection lemma.** Let $\mathcal H$ be nonempty and $k$-uniform, and let
$0\le a\le k$ be an integer. If every good triple has a pair intersection larger
than $a$, then

$$
\tau(\mathcal H)\le\max\{a,2(k-a)\}.
\tag{1}
$$


If every pair of edges intersects in more than $a$ points, any $(k-a)$-subset of
a fixed edge covers the family. Otherwise choose $A,B$ with $I=A\cap B$ of size
$r\le a$. Every edge $E$ avoiding $I$ forms a good triple with $A,B$, and hence
meets $A\setminus I$ or $B\setminus I$ in more than $a$ points. If $k-r\le a$,
no such $E$ exists, so $I$ is a transversal. Otherwise choose arbitrary subsets
$X\subseteq A\setminus I$ and $Y\subseteq B\setminus I$, each of size $k-r-a$.
Every $E$ avoiding $I$ meets $X$ or $Y$. Thus $I\cup X\cup Y$ is a transversal
of size $2k-r-2a\le2(k-a)$, proving (1).

In particular, with

$$
a=\lfloor5k/8\rfloor,
\qquad T=\lceil3k/4\rceil,
$$

one has

$$
\max\{a,2(k-a)\}=2\lceil3k/8\rceil\le T+1.
$$

Therefore $\tau>T+1$ forces a good triple whose pair intersections are all at
most $\lfloor5k/8\rfloor$. Since this is smaller than $k$, its edges are
distinct.

## Six sets covering the candidate pairs

**Certificate.** Let $A_1,A_2,A_3$ be a good triple of $k$-sets. Define its
disjoint atoms by

$$
P_i=A_j\cap A_\ell,\qquad
Q_i=A_i\setminus(A_j\cup A_\ell),\qquad
\{i,j,\ell\}=[3].
$$

Write $p_i=|P_i|$, $q_i=|Q_i|$, $s=\sum_i p_i$, and reorder so that
$p_1\ge p_2\ge p_3$. Suppose $p_1\le\lfloor5k/8\rfloor$, and put
$T=\lceil3k/4\rceil$. Then all two-point covers of the triple are contained in a
union of six induced vertex sets, each of size at most $T+1$.

The candidate pairs are exactly $P_i\times P_j$ for $i\ne j$, and
$P_i\times Q_i$. Also

$$
q_i=k-s+p_i,\qquad d_i:=p_i+q_i=k-s+2p_i,
\qquad d_1\ge d_2\ge d_3.
$$


Use at most two auxiliary sets, each containing all of $P_i$ for every portion
of $Q_i$ placed in it. These sets cover the associated $P_iQ_i$ pairs. Let $R_i$
denote the portion of $Q_i$ not placed in these sets. Four further sets cover
all remaining candidate pairs as follows. Index them by the vertices of $K_4$,
and index its three perfect matchings cyclically by $i\in[3]$. Split
$P_i\cup R_{i-1}$ into two balanced parts and give them the two matching edges
as supports. Distinct perfect matchings have every pair of their edges
intersecting. Consequently every $P_iP_j$ pair and every $P_iR_i$ pair has
intersecting supports and is contained in a covering set. With

$$
M=s+\sum_i|R_i|,
$$

each of these four sets has size at most

$$
\sum_{i=1}^3\left\lceil\frac{p_i+|R_{i-1}|}{2}\right\rceil
\le\left\lceil\frac M2\right\rceil+1.
\tag{2}
$$

It remains to choose the two auxiliary sets with size at most $T$ and $M\le2T$.

**Case 1: $p_1\le k/2$ and $d_2\le T$.** Use $P_2\cup Q_2$ and $P_3\cup Q_3$.
They fit because $d_3\le d_2$. The remaining mass is
$M=s+q_1=k+p_1\le3k/2\le2T$.

**Case 2: $p_1\le k/2$ and $d_2>T$.** Start one auxiliary set with $P_2$, the
other with $P_1\cup P_3$, and fill both to size $T$ from their corresponding
$Q$-atoms. The second initial size satisfies

$$
p_1+p_3=k+p_2-d_2\le3k/2-T\le T.
$$

The first can be filled because $d_2\ge T$; the second because
$d_1+d_3=2k-2p_2\ge k\ge T$. The total removed $Q$-mass is $2T-s$, so
$M=3k-2T\le2T$.

**Case 3: $p_1>k/2$ and $p_2+p_3\le3k/4$.** Start the auxiliary sets with $P_1$
and $P_2\cup P_3$, respectively, and again fill both to $T$ from their own
$Q$-atoms. Both initial sizes are at most $T$. The available totals satisfy

$$
d_1=k+p_1-(p_2+p_3)>3k/4,
\qquad d_2+d_3=2k-2p_1\ge3k/4.
$$

They are integers, hence at least $T$. Again $M=3k-2T\le2T$.

**Case 4: $p_1>k/2$ and $p_2+p_3>3k/4$.** Use just one auxiliary set: $P_1$
together with $\min(q_1,T-p_1)$ points of $Q_1$. If $d_1\le T$, all of $Q_1$ is
removed and $M=2k-p_1<3k/2\le2T$. Otherwise

$$
M=3k-(p_2+p_3)-T\le2T.
$$


These cases exhaust the possibilities. All choices are integral. Formula (2) now
proves the certificate.

## A nine-edge witness at the three-quarter threshold

**Theorem.** Every family of nonempty edges of rank at most $k$ with

$$
\boxed{\tau(\mathcal H)>\lceil3k/4\rceil+1}
$$

contains a subfamily of at most **nine** edges with no two-point transversal.

First suppose the family is $k$-uniform. The selection lemma supplies the good
triple used above. For each of its at most six covering sets, choose an edge
avoiding it; this is possible because its size is smaller than $\tau$. A
two-cover of the resulting at-most-nine edges would cover the reference triple,
hence be contained in one of the six sets, and would miss the edge chosen to
avoid that set. This is a contradiction.

For rank at most $k$, pad each edge with its own private points. The transversal
number of every subfamily is unchanged: replace any selected private point by an
original point of its unique nonempty edge. Apply the uniform result and project
the bad witness back to the original edges. The finite-witness argument in
[Structural reductions](structural_reductions.md) also permits infinite
families.

In particular,

$$
P_9\quad\Longrightarrow\quad
\tau(\mathcal H)\le\lceil3k/4\rceil+1.
\tag{3}
$$

For the exactly-nine convention without a lower bound on the number of edges,
take the maximum of this right side with eight.

A hypothetical fixed-excess $P_7$ family therefore has, for large $k$, a
minimum-cardinality subfamily requiring more than two points of size **eight or
nine**. This improves the earlier eight-through-eleven reduction, but does not
force a bad seven-subfamily.

### Why five static covering sets do not suffice

For even $k$, take

$$
(p_1,p_2,p_3)=(k/2,k/2,0),\qquad
(q_1,q_2,q_3)=(k/2,k/2,0).
$$

The candidate graph is the bipartite path blowup $Q_1-P_1-P_2-Q_2$, with
$3k^2/4$ edges. A set of $L$ vertices induces at most $L^2/4$ edges in any
bipartite graph. Five covering sets of size at most $L$ would therefore require

$$
\frac{5L^2}{4}\ge\frac{3k^2}{4},
\qquad L\ge\sqrt{3/5}\,k>3k/4.
$$

This profile satisfies the selection lemma's pair bound. Thus reducing the new
nine-edge witness to eight cannot follow from a universal five-set static
certificate for every selected triple. This does not exclude another choice of
triple, adaptive additional edges, or stronger information from the ambient
high-transversal family.

## The earlier eleven-edge cube certificate

**Theorem.** A $k$-uniform family satisfying

$$
\tau(\mathcal H)>\left\lceil\frac{3k}{4}\right\rceil+3
$$

contains a subfamily of at most eleven edges with no two-point transversal.

**Proof.** There is a triple $A_1,A_2,A_3$ with empty common intersection.
Otherwise partitioning one edge into two balanced parts and choosing an edge
avoiding each part proves $\tau\le\lceil k/2\rceil$.

Put

$$
P_i=A_j\cap A_\ell,\qquad
Q_i=A_i\setminus(A_j\cup A_\ell),\qquad
\{i,j,\ell\}=[3].
$$

All six atoms are disjoint. Every two-cover of the reference triple lies in
their union and is of type $P_iP_j$, $i\ne j$, or $P_iQ_i$.

Index eight exclusion sets by $x\in\mathbb F_2^3$. Split $P_i$ into two balanced
pieces, giving their points the respective supports $\{x:x_i=0\}$ and
$\{x:x_i=1\}$. Split $Q_i$ into four balanced pieces and give their points
supports equal to the four lines parallel to coordinate $i$. Let $S_x$ consist
of the points whose supports contain $x$.

The supports of every candidate pair intersect: coordinate planes with different
normals intersect, and a coordinate-$i$ plane meets every coordinate-$i$ line.
Consequently every candidate pair is contained in some $S_x$. Writing
$p_i=|P_i|$ and $q_i=|Q_i|$, we have $2\sum p_i+\sum q_i=3k$, and

$$
|S_x|\le\sum_i\left\lceil p_i/2\right\rceil+
\sum_i\left\lceil q_i/4\right\rceil
\le\left\lfloor\frac{3k+15}{4}\right\rfloor
=\left\lceil\frac{3k}{4}\right\rceil+3
$$

where the rounding losses are at most $3/2+9/4=15/4$, and the loads are
integers. Choose eight edges, one avoiding each $S_x$. A two-cover of these and
the three references would lie in some $S_x$ and miss the corresponding selected
edge. $\square$

This earlier construction is retained for its explicit critical example below.
Its witness-size conclusion is superseded by the nine-edge theorem. Both
arguments use global high transversal number; neither reduces the original
problem to arbitrary small critical families on their own.

## Eleven is possible for a critical local obstruction

For every positive integer $b$, take disjoint atoms $P_i,Q_i$ of sizes $10b,4b$,
respectively. Perform the preceding cube assignment with equal pieces. Its
ground set $U$ has size $42b$, and every $S_x$ has size $18b$. Define

$$
A_i=P_j\cup P_\ell\cup Q_i,
\qquad E_x=U\setminus S_x.
$$

These eleven distinct edges all have size $24b$, and the cube argument excludes
a two-cover.

Deleting $A_i$ admits a pair from opposite halves of $P_i$. The pair covers the
other two reference edges, and its two disjoint cube supports ensure that it
meets every $E_x$. Deleting $E_x$ admits a $P_iQ_i$ pair whose plane and line
supports intersect exactly at $x$. It covers all references and every other
$E_y$. Consequently the family is transversal-critical with transversal number
three, and every ten of its edges have a two-cover.

Its global transversal number is only three. It is not an asymptotic
counterexample, but shows why the bounded-witness reduction still requires
information from the surrounding high-transversal family.

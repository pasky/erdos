---
name: research/erdos_644/nonuniform_guard_fibres
desc: Arbitrary rank-s guard fibers of transversal number greater than 2s can be projected away while preserving P7.
tags: [proved, reductions, boolean-functions, limitations]
sources: []
created: 2026-09-23T06:00:00Z
updated: 2026-10-13T05:28:09Z
---


# research/erdos_644/nonuniform_guard_fibres

***

Here $P_7$ means that every subfamily of at most seven edges has a
transversal of size at most two.

The safe projection in
[Prime guard families](prime_guard_families.md#safe-removal-of-a-sparse-partial-product)
assumes that omitted guard fibers have small transversal number, or that every
seven allowed fibers have three disjoint edges in their common intersection.
Neither condition is needed for the following $P_7$-specific projection. Its
hypothesis concerns each fiber separately. It does not provide an extraction
theorem for arbitrary families, and does not settle Problem 644.

## A graph on the seven row indices

**Lemma.** Let $\mathcal M$ be a nonempty intersecting family of
subsets of $[7]$, each of size at least two. There exists a
nonbipartite, 2-degenerate graph $G$ on $[7]$ such that every member
of $\mathcal M$ contains an edge of $G$.

A graph is 2-degenerate if its vertices can be ordered so that each
vertex has at most two earlier neighbors.

**Proof.** If $\{a,b\}\in\mathcal M$, take the edge $ab$ and join
both $a$ and $b$ to all five other vertices. Every member of
$\mathcal M$ meets $\{a,b\}$ and has at least two points, so it
contains an edge. The graph contains a triangle, and deleting the
five degree-two vertices leaves just $ab$.

If every member has at least four points, take the disjoint union
$K_3\sqcup K_2\sqcup K_2$. Its independence number is three.

In the remaining case choose $A\in\mathcal M$ of size three and
put $B=[7]\setminus A$. There exist $a\in A$ and a pair
$P\subseteq B$ for which $\{a\}\cup P\notin\mathcal M$.
Otherwise, choosing different $a,b\in A$ and complementary pairs
$P,Q\subseteq B$ would give two disjoint members $aP,bQ$.

Make $A$ a triangle. Give the two vertices of $P$ label $a$, and
give the other two vertices of $B$ the two different remaining
labels in $A$. Join each vertex of $B$ to the two vertices of $A$
different from its label. This graph is nonbipartite and 2-degenerate:
delete the four degree-two vertices in $B$, followed by the triangle.

If a member $M\in\mathcal M$ were independent, it would meet $A$
in exactly one point: it must meet $A$ by intersection, and cannot
meet it twice because $A$ is a triangle. Every other point of $M$
would have the same label as that point. Since $|M|\ge3$, the
only possibility is $M=\{a\}\cup P$, which was excluded. $\square$

## Projection of arbitrary guard fibers

Let $U,W$ be disjoint finite sets. Let $\mathcal A$ be a family of
nonempty subsets of $U$, and for each $A\in\mathcal A$ let
$\mathcal G_A$ be a nonempty family of subsets of $W$, all of size
at most $s$. Define

$$
\mathcal Q=\{A\cup B:A\in\mathcal A,\ B\in\mathcal G_A\}.
\tag{1}
$$

Assume the following avoidance condition in every fiber:

$$
\text{for each }X\subseteq W\text{ with }|X|\le2s,
\quad \text{some }B\in\mathcal G_A\text{ is disjoint from }X.
\tag{2}
$$

For fibers of nonempty sets, this is exactly
$\tau(\mathcal G_A)>2s$. Condition (2) also permits an empty guard
edge, without needing a convention for its transversal number.

**Theorem.** Under (2),

$$
\boxed{\mathcal Q\text{ has }P_7
\quad\Longleftrightarrow\quad
\mathcal A\text{ has }P_7,\qquad
\tau(\mathcal A)\ge\tau(\mathcal Q).}
\tag{3}
$$


**Proof.** A two-cover of any core subfamily covers its chosen lifts,
and a global core transversal covers $\mathcal Q$. Thus only
reflection of $P_7$ needs proof.

Suppose $\mathcal A$ fails $P_7$. Repeat edges, if necessary, to
obtain a bad tuple $A_1,\ldots,A_7$. For each point $x$ in their
union, let $M_x=\{i:x\notin A_i\}$. These missing sets are pairwise
intersecting, since two disjoint ones would give a two-cover. Each
has at least two elements: if it had just one, a point of that
remaining nonempty row would complete a two-cover; an empty missing
set would give a one-cover.

Apply the graph lemma to the $M_x$, and order the rows so that every
vertex of $G$ has at most two earlier neighbors. Choose
$B_i\in\mathcal G_{A_i}$ successively, avoiding the union of the
guards at those earlier neighbors. This union has size at most
$2s$, so (2) allows the choice. Thus

$$
ij\in E(G)\quad\Longrightarrow\quad B_i\cap B_j=\varnothing.
$$

The row spectrum of each guard point is an independent set of $G$.

The lifted tuple $A_i\cup B_i$ has no two-cover. Two core points
already fail on the original tuple. A core point $x$ and a guard
point fail because $M_x$ contains a graph edge, while the guard
spectrum is independent. Two guard points cannot cover all rows,
since that would cover $V(G)$ by two independent sets and make $G$
bipartite. Points outside the tuple's union cannot help. Thus
$\mathcal Q$ fails $P_7$, proving (3). $\square$

The coefficient two cannot be uniformly replaced by a smaller
coefficient for all $s$. At $s=1$, take three disjoint singleton
core edges, and let every fiber consist of the singleton guards
$\{u\},\{v\}$. Each fiber has transversal number two. The lifted
family has a global two-cover, whereas the core fails $P_3$.
This observation does not assert asymptotic sharpness as $s\to\infty$.

## Limitation

The fibers need not coincide or have any common allowed edge, and
their ground supports may overlap arbitrarily. However, the theorem
only applies when **every** fiber satisfies (2). It does not show
that a high-transversal family has a useful core--guard partition,
or that the fibers failing (2) can be discarded with $o(k)$ loss.
Controlling the aggregate cost of such low-transversal fibers is
still missing. Thus (3) is a safe projection criterion, not a
rank-sensitive normalization or an unrestricted amplifier.

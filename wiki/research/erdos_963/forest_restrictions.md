---
name: research/erdos_963/forest_restrictions
title: 'Restrictions on a deficient color family'
desc: Proved support and small-graphic-rank bounds for the conditional rainbow-forest approach; no general augmentation theorem.
tags: []
sources: []
created: 2026-09-18T23:48:02Z
updated: 2026-09-19T04:11:13Z
---


# Restrictions on a deficient color family

***

Let $P$ be positive, $D\subseteq P$ maximum dissociated,
$d=|D|$, $S=\Sigma(D)$, and $T=\sum D$. Color every edge
$\{s,s+a\}\subset S$ by $a\in P$. For $C\subseteq P$, let
$H=(S,E(C))$ and let $r(H)$ be its graphic rank, including
isolated vertices in the component count.

The [[research/erdos_963/continuation_routes|forest criterion]] asks whether
some maximum $D$ always satisfies $r(H)\ge|C|$. The results below restrict
deficient families; they do not establish that criterion.

## Distinct unsigned supports contribute independent edges

Let $\mathcal U(C)$ be the family of distinct unsigned supports of
all ternary representations on $D$ of colors in $C$. Then

$$
r(H)\ge|\mathcal U(C)|. \tag{1}
$$


For each support $I\in\mathcal U(C)$, choose one representation.
Its possible upper endpoints form a face $F_I$ of the subset cube:
coordinates in the positive support are fixed to one, coordinates
in the negative support to zero, and all remaining coordinates are free.

Any family of cube faces with distinct fixed-coordinate sets has a
system of distinct vertex representatives. To check Hall's condition,
take any subfamily and downward-compress its union successively in
every coordinate. The compressed union contains the downward-compressed
image of each individual face: fixed one coordinates become zero,
fixed zero coordinates remain zero, and free coordinates remain free.
Compression preserves the cardinality of the union. The final union
contains, for each $I$, the distinct vertex
$\mathbf1_{[d]\setminus I}$. Its original cardinality is therefore
at least the number of faces. This applies to every subfamily.

Choose the corresponding difference edge at each selected upper
endpoint. These edges form a forest, since an undirected cycle would
have two edges entering its greatest vertex. Their colors can repeat,
which does not affect graphic rank. This proves (1).

Thus every graphic-rank-deficient family is also deficient for
unsigned-support matching. The converse does not follow, as the
existing full-support matching counterexamples demonstrate.

### The whole upward closure contributes independent edges

Let $\mathcal U^\uparrow(C)$ be the family of all $J\subseteq D$
containing at least one member of $\mathcal U(C)$. The same argument
in fact proves

$$
r(H)\ge|\mathcal U^\uparrow(C)|.                            \tag{1a}
$$

For each such $J$, choose a representation with support $I(J)\subseteq J$.
Its upper-endpoint face, after downward compression, contains
$\mathbf1_{D\setminus J}$. These vertices are distinct as $J$ varies,
even if several chosen faces coincide. Applying compression to each
subfamily verifies Hall. The distinct upper endpoints again give a
forest.

If $\tau$ is the minimum size of a set of coordinates meeting every
representation support, the largest support-free coordinate set has
size $d-\tau$. Every coordinate set of larger size therefore belongs
to $\mathcal U^\uparrow(C)$, so

$$
r(H)\ge\sum_{j=0}^{\tau-1}\binom dj\ge2^\tau-1.             \tag{1b}
$$

Deleting such a hitting set leaves a dissociated set which each color
can extend individually. This does not justify simultaneous extension:
combinations of different colors can have new representations on the
remaining coordinates. No augmentation from deficiency has been proved.

## Every deficient family has rank at least six

For a maximum $D$, one has

$$
r(H)<|C|\quad\Longrightarrow\quad r(H)\ge6,\quad |C|\ge7. \tag{2}
$$


Reflection $J(s)=T-s$ is a fixed-point-free automorphism of $H$
preserving each edge color. In cube coordinates it is complementation.
A representation with unsigned support $I$ supplies
$2^{d-|I|}$ pairwise vertex-disjoint edges, by translating the
endpoint subsets in the zero coordinates.

Suppose $r(H)\le5$ and $|C|>r(H)$. A component not fixed by $J$
is paired with another component of the same size and the same color
set. A pair of $k$-vertex components contributes rank $2(k-1)$;
hence $k\le3$. A paired pair of triangles has at most three colors
and rank four, and any remaining rank is at most one. Such components
cannot give a deficiency. Two-vertex components have at most one
color each. A component fixed by $J$ has even order. It follows that
a deficient graph of rank at most five must contain a
reflection-invariant component of order four or six.

### Four vertices

There is only one such component $K$; all remaining nontrivial
components are $t\le2$ isolated edges. After centering at $T/2$,
write

$$
K=\{-x,-y,y,x\},\qquad x>y>0.
$$

Its lengths belong to $\{2x,2y,x+y,x-y\}$. Since the total rank is
$3+t$, deficiency forces all four lengths to be distinct and present,
and each other edge to have a new color distinct from all the others.

Write the corresponding cube vertices as
$\{p,p^c,q,q^c\}$. The two cross-pair length classes have complementary
supports $I=p\triangle q$ and $I^c$. Each of these colors has
exactly two edges in the entire graph. The translated-edge count gives

$$
2^{d-|I|}\le2,\qquad 2^{|I|}\le2,
$$

so $d\le2$. If $t>0$, there are more than four nonisolated vertices,
impossible. If $t=0$, $P$ has four distinct positive elements, hence
a dissociated triple, contradicting $d\le2$.
For the last elementary fact, take $a<b<c<e$: either $\{b,c,e\}$
is dissociated, or $e=b+c$, when $\{a,c,e\}$ is dissociated.

### Six vertices

Here $r(H)=5$, and the six-vertex component $K$ is the only
nontrivial component. Every representation of a color in $C$ has
support at least $d-1$: two zero coordinates would give four disjoint
edges and require eight nonisolated vertices.

There are three complementary pairs in $K$. Full-support edges join
members of one such pair and give at most three colors. Any other
edge has support $d-1$. It therefore joins two complementary pairs
that are adjacent in the folded cube, the quotient of the $d$-cube
by complementation.

For $d\ge4$, the folded cube is triangle-free. A triangle would imply
$e_i+e_j+e_k\in\{0,\mathbf1\}$ over $\mathbb F_2$, which is
impossible for $d\ge4$. Thus the three pairs have at most two
adjacencies. Each adjacency supplies at most one permissible color:
the other cross-pair length is the basis color $d_i$, whose
$2^{d-1}$ disjoint canonical edges require more than six vertices.
Consequently $|C|\le3+2=5$, a contradiction.

For $d=3$, a basis color has four disjoint canonical edges and
therefore cannot belong to $C$. Hence

$$
|P|\ge|D|+|C|\ge3+6=9,
$$

contrary to the already-proved positive bound $|P|\le7$ in
dimension three. Finally, $d\le2$ cannot supply six vertices.
This proves (2).

## Excluding rank six

In fact every deficient family has rank at least seven. Suppose
$r(H)=6<|C|$. If $d\le3$, the proved positive bound gives $|P|\le7$,
so $C=P$ has seven colors; its basis colors connect $S$, forcing rank
seven. Thus $d\ge4$.

A reflection-paired pair of components of order $k$ has rank $2(k-1)$
and at most $\binom{k}{2}$ colors. Under the rank-six budget, such
pairs alone cannot be deficient. The remaining possibilities are:
a four-vertex invariant component plus three isolated edges; a
six-vertex invariant component plus one fixed complement edge; or
two invariant four-vertex components.

In the first case deficiency forces four distinct colors in the
four-vertex component and three new outside colors. Its two cross colors
each have exactly two edges globally. Their complementary supports force
$d\le2$, as above. In the second case a nonfull representation must have
support at least $d-1$: four disjoint non-complement edges cannot use the
fixed complement edge and cannot fit into six vertices. The earlier
folded-cube argument gives at most five colors inside and one outside.

In the third case every support has size at least $d-2$, since only
eight vertices are nonisolated. Deficiency forces one component to have
all four of its possible colors. Its complementary cross supports both
have size at least $d-2$, giving $d\le4$. At $d=4$, both have size two
and each supplies four disjoint edges. Its two edges in the first
component force two in the second. Thus both cross colors are shared,
and there are at most $4+4-2=6$ colors. This excludes rank six.

## Excluding rank seven for the maximum-sum choice

If $D$ maximizes $\sum D$ among maximum dissociated subsets, every
deficient family has rank at least eight.

Call a color *exclusively full-support* when every representation of it
has full support. Replacing any coordinate of $D$ by such a color
preserves dissociation. Maximum sum therefore forces its value to be
smaller than $\min D$. The complement orbits carrying these colors are
independent in the folded cube: adjacent orbits with absolute full
signed sums $a,b$ satisfy $2d_i=|\pm a\pm b|$ for some $i$, contrary to
$a+b<2\min D\le2d_i$.

The word **exclusively** is essential. A color with both full and
nonfull representations need not allow these exchanges.

Suppose $r(H)=7<|C|$. Again $d\ge4$. Reflection-paired components alone
cannot be deficient. The cases with an invariant component smaller
than eight vertices are excluded as follows:

* A four-vertex component plus four isolated edges is handled by the
  complementary-support argument. A four-vertex component plus paired
  triangles has at most $4+3=7$ colors.
* Two invariant four-vertex components plus a fixed edge have at most
  seven colors. If either component has all four colors, the rank-six
  argument forces $d=4$ and both cross colors are shared.
* A six-vertex component plus two fixed edges gives at most $5+2=7$
  colors, since nonfull supports have size at least $d-1$.
* If the two outside edges instead form a reflection pair, they carry
  one color $b$. Every other color has all its edges inside the
  six-vertex component, so its nonfull supports have size at least
  $d-1$. The folded-cube argument bounds these colors and the full
  colors there by five; adding $b$ cannot cause deficiency.

It remains to treat one invariant eight-vertex component, consisting
of four complement orbits. All supports have size at least $d-2$.
Basis colors are absent, since their canonical edges cover at least
sixteen vertices.

If all nonfull representations have support $d-1$, they give at most
one color per adjacency among the four folded-cube vertices.
Triangle-freeness bounds these colors by four. Deficiency then forces
four exclusively full-support colors on the four vertices. There must
also be an adjacency, contradicting their independence.

Otherwise a representation omits exactly two coordinates $i,j$.
Its four translated edges exhaust the component, and its four
complement orbits form an affine plane with directions $e_i,e_j$ in
$\mathbb F_2^d/\langle\mathbf1\rangle$. For $d\ge4$, these are the only
coordinate directions in that plane. Hence support-$d-1$ colors give
at most its four square edges, and any support-$d-2$ representation
omits the same two coordinates. The fixed sign pattern is determined
by the component up to reversal, giving at most one latter color.
Thus at most five colors admit any nonfull representation.
Deficiency forces at least three exclusively full-support colors on
the four vertices of a square, contradicting independence. Rank seven
is excluded.

## Minimal deficient families have rainbow alternate paths

Let $C$ be inclusion-minimal with $r(E(C))<|C|$. Then, for every
$a\in C$,

$$
r(E(C))=|C|-1=r(E(C\setminus\{a\})).
$$

Indeed, minimality gives the lower bound $|C|-1$ for the last
rank, monotonicity bounds it by $r(E(C))$, and deficiency gives
the opposite upper bound. Inclusion and equal graphic ranks show
that deleting any color preserves every connected component.

There is in fact a rainbow alternate path for each edge of color
$a$, after a suitable forest is chosen. Every subfamily of
$C\setminus\{a\}$ satisfies the forest rank criterion proved in
[[research/erdos_963/continuation_routes|the forest note]]. Hence one may choose a
forest $F$ containing one edge of each of its $|C|-1$ colors.
Its rank equals $r(E(C))$, so it spans the full component
partition of $E(C)$. The endpoints of any $a$-edge are joined
by a path in $F$, and that path has distinct colors, none equal
to $a$.

This gives a ternary relation among the color values on that
cycle, but not the needed exchange with $D$. Substitution of
representations on $D$ may have coefficients of absolute value
greater than one. No argument turns these cycles into a larger
dissociated set or an equally large one of larger sum. Thus this
elementary reduction does not establish the maximum-sum forest
assertion.

## Exact gap

Families of graphic rank at least eight remain untreated for the maximum-sum
choice. In particular, the support count (1) does not control multiple colors
with the same support. There is no proved exchange or augmentation from a
deficient family to a dissociated $(d+1)$-subset. The minimum-sum endpoint
counterexample in [[research/erdos_963/minimum_sum_matching|the matching note]]
still has graphic rank equal to its three colors and does not refute this route.

---
name: research/erdos_617/global_clique_packing
desc: Cross-color fibers and transversal rigidity give a square-root gap in every color's full-clique packing; the independent triangle-support lemma also checks.
tags: [graph-theory, proved, color-coupling]
sources: []
created: 2026-09-22T12:10:32Z
updated: 2026-10-14T00:26:52Z
---


# research/erdos_617/global_clique_packing

***

**Proved necessary conditions, not a resolution.** Let $p$ be the maximum number
of vertex-disjoint monochromatic $K_r$'s in one color of a hypothetical
counterexample. Section 5 of the
[third independent input](independent/uniform_capacity_and_clique_packings.md)
correctly proves $p\le r-2$ for $r\ge3$ and, in its extension, $p\le r-3$ for
$r\ge8$. The missing boundary arguments and the
triangle-support lemma are supplied below.

Combining the argument with the established private-row excess bound
gives the stronger conclusion

$$
\boxed{p\le r-\max\{3,\lfloor\sqrt r/8\rfloor\}-1
\qquad(r\ge8).} \tag{1}
$$

Unlike the older minority-color packing bound, these restrictions apply
to every color. They do not force a packing large enough to contradict
them, and they are not bounds on the total number of full cliques.

## Fibers and independent-set attachments

An outsider has at most one own-color neighbor in a full clique. Fix
a full color-$i$ clique $A$. For $j\ne i$, let $b_j(A)$ count outsiders
whose star into $A$ repeats color $j$. Every such star contains each
foreign color; it is either rainbow or omits $i$ and repeats exactly
one foreign color.

For each $u\in A$, its private color-$j$ fiber consists of $u$ and
the outsiders with unique color-$j$ neighbor $u$ in $A$. It is a clique:
otherwise two private nonneighbors, together with $A\setminus\{u\}$,
would be a color-$j$ independent $(r+1)$-set. The $r$ fibers cover
$r^2+1-b_j(A)$ vertices and their deficits from order $r$ sum to
$b_j(A)-1$. At least $r-b_j(A)+1$ are full, giving

$$
b_j(A)\ge r-p+1.
$$

If $t_i(A)$ counts color-$i$ edges leaving $A$, star counting yields

$$
t_i(A)=r^2-r+1-\sum_{j\ne i}b_j(A)
\le(r-1)(p-1)+1. \tag{2}
$$


Suppose a color has $k\ge2$ disjoint full rows and its residue contains
an independent set $I$ of order $r+1-k$. Avoid the neighbors of $I$
in every row. The resulting lists have order at least $k-1$ and matching
cross graphs. An independent transversal would augment $I$ to order
$r+1$, so [matching-transversal rigidity](packing_tools.md) makes all
lists have order exactly $k-1$, with a perfect matching between each
pair. In particular each member of $I$ has a neighbor in every row,
and these neighbors are distinct within each row.

Let $S$ be the residue vertices belonging to at least one such $I$,
and write $s=|S|$. Every pair of rows has at least $k-1$ cross edges,
and each vertex of $S$ attaches to every row. Thus

$$
\boxed{t_i(A)\ge(k-1)^2+s.} \tag{3}
$$

This does not assume simultaneous choices of the different independent
sets: the forced attachments are individual edges.

## Excluding a packing of r minus one full cliques

The [full-resolution obstruction](packing_tools.md) already gives
$p\le r-1$. Suppose equality holds, and take $r-1$ rows in color $i$.
The residue $R$ has order $r+1$. Set $F=\overline{G_i[R]}$ and let $s$
count its nonisolated vertices. We have $e(F)\ge r-1$. Applying (3)
to independent pairs and comparing with (2) gives $s\le r-1$.
Also

$$
\sum_{j\ne i}b_j(A)\le3r-3-s.
$$

Since every $b_j(A)\ge2$, at least $s$ foreign colors have $b_j(A)=2$.
Each therefore has $r-1$ full private rows. This is the propagation
step missing from a one-color edge argument.

Put $T=r\binom r2+r$. Every color has at least $T+r-1$ edges, by
the [nonpartite gap](packing_tools.md), or the coupled block count in
[Palette and cut bounds](palette_and_cut_bounds.md). The total surplus
available above $rT$ is $r^2(r-1)/2$.

For $r\ge5$, the inequality $e(F)\ge r-1\ge4$ forces $s\ge4$.
Every packing color therefore has at least

$$
(r-1)\binom r2+(r-2)\binom{r-1}{2}+4(r-1)
$$

edges, with surplus $A=(r^3-6r^2+15r-12)/2$ above $T$.
There are at least three such colors, and

$$
3A+(r-3)(r-1)-\frac{r^2(r-1)}2
=\frac{(r-3)(r-2)(2r-5)}2>0,
$$

a contradiction.

The input's separate proof for the smaller parameters is not retained,
but these cases are direct. For $r=3$, $s\le2$ contradicts $e(F)\ge2$.
For $r=4$, necessarily $s=3$ and $F=K_3\sqcup2K_1$, so the target
residue has seven edges. Propagation gives all four colors three-row
packings. Each has at least

$$
3\binom42+2\binom32+3\cdot3+7=40
$$

edges, exceeding the total $\binom{17}{2}=136$ when summed. Hence
$p\le r-2$ for all $r\ge3$.

## A triangle-support lemma

**Lemma.** Suppose a graph $F$ on $2r+1$ vertices contains a triangle,
and every vertex belonging to a triangle lies in a set $S$ with
$s=|S|\le r$. Then

$$
e(F)\le r^2+s-1. \tag{4}
$$


Put $Y=V(F)\setminus S$. Each vertex of $Y$ has an independent
neighborhood. Choose $y\in Y$ of maximum total degree among vertices
of $Y$, and put $A=N(y)\cap Y$, $B=Y\setminus A$, $C=N(y)\cap S$.
Replace all vertices of $B$ by independent twins of $y$. The edge gain is

$$
\sum_{b\in B}(d(y)-d(b))+e(F[B])\ge0.
$$

No triangle meeting $Y$ is created: the new neighborhood of every
vertex in $B$ is the independent set $A\cup C$. If $A$ is nonempty,
make all its vertices twins of a member with the most neighbors in $S$.
This also does not decrease the edge count. Their common neighborhood
$D\subseteq S$ is independent and disjoint from $C$. If $A$ is empty,
take $D=\varnothing$ and omit this operation.

Now $Y$ is complete bipartite on $A,B$, its edges to $S$ are exactly
those from $A$ to $D$ and $B$ to $C$, and $F[S]$ is unchanged. Because
$F[S]$ still contains a triangle, $t=|S\setminus(C\cup D)|\ge1$.
Writing $a,b,c,d$ for the respective sizes gives

$$
\begin{aligned}
e(F)&\le ab+ad+bc+cd+t(s-t)+\binom t2\\
&\le\left\lfloor\frac{(2r+1-t)^2}{4}\right\rfloor
 +ts-\frac{t(t+1)}2.
\end{aligned}
$$

After dropping the floor, the difference of the final expression
from $r^2+s-1$ is

$$
(t-1)\left(s-r-1-\frac{t+1}{4}\right)\le0.
$$

This proves (4), including the empty-$A$ case. It is sharp: add to
$K_{r,r}$ an apex adjacent to nonempty subsets of opposite sides whose
total order is $s-1$. Exactly $s$ vertices lie in triangles, and the
edge count is $r^2+s-1$.

## Checking the independent extension

Let $r\ge8$ and suppose $p=r-2$. The residue has order $2r+1$, so
[two-row capacity](two_row_structure.md) forces an independent triple.
Let $s$ count the vertices participating in such triples. The complement
$F$ of the residue has

$$
e(F)\ge(r-1)(r+2)=r^2+r-2.
$$

If $s\le r$, apply (4); otherwise no lemma is needed. In both cases
$s\ge r-1$. Equations (2)--(3) give

$$
t_i(A)\ge(r-3)^2+s,\qquad
\sum_{j\ne i}b_j(A)\le5r-8-s.
$$

Every $b_j(A)\ge3$, so at least $s-r+4\ge3$ foreign colors have
$b_j(A)=3$, and therefore have $r-2$ full rows. Each of these at least
four packing colors has surplus above $T$ at least

$$
A_2=\frac{r^3-8r^2+15r-14}{2},
$$

by counting row edges, $(r-3)$ cross edges per row pair, and $r-1$
supported residue attachments per row. Residual edges are omitted.
The budget excess is

$$
4A_2+(r-4)(r-1)-\frac{r^2(r-1)}2
=\frac{(r-8)(3r^2-5r+10)}2+16>0
$$

for $r\ge8$. Thus the archived extension is valid without assuming
any of its unretained proofs.

## Stronger comparison using established private-row excess

For $r\ge7$, [Cross-color cores](cross_color_cores.md) proves that every
foreign private system has excess deficit

$$
E_j\ge e(r):=\left\lceil\frac{\sqrt{8r-7}-5}{2}\right\rceil.
$$

Its exact number of full rows is $f_j=r-b_j+1+E_j$. Since $f_j\le p$,
the fiber bound strengthens to

$$
b_j\ge r-p+1+e(r),\qquad
t_i(A)\le(r-1)(p-1-e(r))+1. \tag{5}
$$

This established excess bound applies without $b_j\le r$; its owner
proof and the required supporting-pair size conditions are recorded
in the linked note.

Suppose $p=r-a\ge2$ and the residue has an independent $(a+1)$-set.
Equation (3), even using only these $a+1$ supported vertices, gives
$t_i(A)\ge(p-1)^2+a+1$. The upper bound (5) minus this lower bound is
exactly

$$
a(p-2)-(r-1)e(r). \tag{6}
$$

It is negative whenever $a\le e(r)$.

For $a=1$, the clique cap supplies the required independent pair.
For $a=2,3$, the [small-independence span bounds](three_row_structure.md)
supply it when $r\ge8$. We have $e(r)\ge2$ for $r\ge8$ and $e(r)\ge3$
for $r\ge12$. When $8\le r\le11$, $e(r)=2$ and (6) for $a=3$ is
$r-13<0$. Thus $p=r-1,r-2,r-3$ are all excluded for $r\ge8$.

Put $m=\max\{3,\lfloor\sqrt r/8\rfloor\}$. For $4\le a\le m$,
$r\ge64a^2$ and $e(r)\ge a$. The
[hereditary span theorem](hereditary_span_bound.md) forces an independent
$(a+1)$-set in the $ar+1$ residue, so (6) again contradicts (5).
Together with $p\ne r$, this proves (1). All these cases have $p\ge2$;
if $p\le1$, (1) is immediate.

At $r=7$, assuming $p=r-2$, (3) and (5) instead give $s\le3$, while
(4) gives $s\ge6$. Thus $p\le r-3$ also holds at that parameter.
This is not a new fixed case of the coloring problem, whose status is
unchanged. The essential unresolved issue is a lower bound forcing a
near-complete packing, not the validity of these upper bounds.

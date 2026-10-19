---
name: research/erdos_617/three_row_structure
desc: Cap-only independence-three span for r at least six; near-Mantel and row-column arguments give three-clique equality for r at least twelve.
tags: [graph-theory, proved, stability]
sources:
  - kang_pikhurko_2005_maximum_k_r_1_free_graphs_which_are_not_r_partite
  - sneiderman_2026_nine_color_case_balanced_coloring
created: 2026-09-21T23:52:12Z
updated: 2026-10-13T05:28:09Z
---


# research/erdos_617/three_row_structure

***

**Status: proved, author-recorded.** This is an auxiliary
parameterized theorem, not a solution of Problem 617. The main conclusion
holds for every $r\ge12$, without a fixed-order catalog or computation.

## Statement and inherited hypotheses

Fix a hypothetical coloring in which every color graph has independence
number at most $r$. For a target color write $H$ for an induced target
graph. If $n=rq+b$, $0\le b<r$, put

$$
p_r(n)=r\binom q2+qb,\qquad
D_r(n)=\binom n2-(r-1)p_r(n).
$$

Every induced target subgraph satisfies

$$
e(H[Z])\le D_r(|Z|).
\tag{1}
$$

Indeed, the other $r-1$ color graphs on $Z$ each have at least $p_r(|Z|)$
edges by complementary Turán, and their edge sets partition the complement of
the target graph. This argument is also the parameterized version of Lemma 2 in
the
[nine-color source](../../../library/extremal_graph_theory/sneiderman_2026_nine_color_case_balanced_coloring/_index.md);
its statement and proof were checked.

We use the following consequence of the
[two-layer theorem](two_row_structure.md): for $r\ge6$, a target
$K_r$-free inherited graph of independence number at most two has at most
$2r-1$ vertices.

**Theorem.** If $r\ge12$, an inherited target graph $H$ on $3r$
vertices with $\alpha(H)\le3$ contains $K_r$.

All the arguments below use only (1), the stated independence and clique
bounds, and the two-layer theorem. The full hereditary hypothesis is
needed, not merely the cap on $(r+1)$-sets.

## Checked external triangle-free bounds

The digest was read first. The statements of Theorems 1 and 2, together with the
monotonicity paragraph following Theorem 2, were then checked in the
[Kang--Pikhurko full source](../../../library/extremal_graph_theory/kang_pikhurko_2005_maximum_k_r_1_free_graphs_which_are_not_r_partite/_index.md),
printed page 13.

Theorem 1, specialized to the triangle-free nonbipartite case, says that
for $n\ge5$,

$$
e(L)\le
\left\lfloor\frac{n^2}{4}\right\rfloor
-\left\lfloor\frac n2\right\rfloor+1.
\tag{2}
$$

Theorem 2 and its following monotonicity observation say that a
nonbipartite graph with no odd cycle shorter than seven has

$$
e(L)\le
\left\lfloor\frac{(n-3)^2}{4}\right\rfloor+3.
\tag{3}
$$

The source's equality classification is not needed: the relevant
near-extremal structures are derived below. Mantel's theorem is also used.

## Symbolic classification at loss at most one

A blow-up $C_5(w_0,w_1,w_2,w_3,w_4)$ replaces the five cycle vertices,
in cyclic order, by independent sets of the displayed positive sizes,
and puts in all edges between consecutive parts. There are no other
edges.

We need two consequences of one classification argument.

**Odd-core lemma.** Let $m\ge7$. If $L$ is triangle-free and

$$
|V(L)|=2m+1,\qquad \alpha(L)\le m,\qquad e(L)\ge m^2,
$$

then there is $z\in V(L)$ such that $L-z$ is bipartite with sides
$X,Y$ of size $m$. Define

$$
p=|N_L(z)\cap X|,\qquad q=|N_L(z)\cap Y|,\qquad
h=m^2-e_L(X,Y).
$$

After exchanging $X,Y$, one of the following holds:

$$
q=1,\qquad 1\le p\le\lfloor m/2\rfloor,\qquad h\le p+1;
\tag{4}
$$

or

$$
p=q=2,\qquad h=4.
\tag{5}
$$


**Even-core lemma.** Let $m\ge9$. A triangle-free graph $L$ satisfying

$$
|V(L)|=2m,\qquad e(L)\ge m^2-m,\qquad \delta(L)\ge m-3
\tag{6}
$$

is bipartite.

### Finding the five-cycle and isolating the loss

For the odd-core lemma, $L$ is nonbipartite: a bipartite graph on
$2m+1$ vertices has an independent set of size at least $m+1$.
For the even-core lemma, suppose for contradiction that $L$ is
nonbipartite.

In the odd case, (3) would give

$$
e(L)\le m^2-2m+4<m^2
$$

if there were no five-cycle. In the even case it would give

$$
e(L)\le m^2-3m+5<m^2-m.
$$

Thus choose a five-cycle $C$ in $L$. It is induced, since $L$ is
triangle-free. Every vertex outside $C$ has at most two neighbors on
$C$, because its cycle neighbors are an independent subset of $C_5$.

Put $W=V(L)\setminus C$, and write $L[W]$ simply as the outside
graph. Mantel's theorem gives

$$
e(L)\le 5+2|W|+\left\lfloor |W|^2/4\right\rfloor.
$$

The right side is $m^2+1$ at order $2m+1$, and $m^2-m+1$ at order
$2m$. Let

$$
\epsilon_W=\left\lfloor |W|^2/4\right\rfloor-e(L[W]),\qquad
\epsilon_C=\sum_{w\in W}(2-d_L(w,C)).
$$

These are nonnegative integers, and

$$
\epsilon_W+\epsilon_C\le1.
\tag{7}
$$

In particular, the outside graph has at least its Mantel number minus
one edges. It is bipartite by (2): in our ranges
$\lfloor |W|/2\rfloor\ge3$, so the upper bound for a nonbipartite
outside graph is strictly smaller than its Mantel number minus one.

Choose a bipartition $P,Q$ of the outside graph.

In the odd case, put $s=m-2$, so $|W|=2s$. Its possible side sizes
are

$$
(|P|,|Q|)=(s,s)\quad\text{or}\quad(s-1,s+1),
$$

up to exchange. In the balanced case at most one cross-edge is missing.
In the unbalanced case the outside graph is complete bipartite, since
the product of its part sizes is already $s^2-1$. Greater imbalance
loses at least four edges from $s^2$.

In the even case, $|W|=2m-5$. The only possible side sizes are
$m-3,m-2$, up to exchange, with at most one missing cross-edge.
Changing these sizes to $m-4,m-1$ already loses two edges from the
maximum.

Equation (7) has an additional consequence: all outside vertices have
two cycle neighbors, except possibly one vertex with exactly one cycle
neighbor. In that exceptional situation $\epsilon_C=1$, so
$\epsilon_W=0$: the outside graph is complete bipartite with balanced,
or as nearly balanced as possible, sides.

### The clone types and their compatibility

Index $C$ by $\mathbb Z/5\mathbb Z$. Every pair of nonadjacent cycle
vertices has a unique common cycle neighbor. Thus an outside vertex
having two cycle neighbors has a unique type $i$, meaning that its
cycle neighborhood is

$$
\{i-1,i+1\}.
$$

It has exactly the neighborhood on $C$ of a clone of cycle vertex
$i$.

If two typed outside vertices are adjacent in $L$, their two cycle
neighborhoods must be disjoint, to avoid a triangle. Directly in $C_5$,
the sets $\{i-1,i+1\}$ and $\{j-1,j+1\}$ are disjoint if and only if
$i,j$ are adjacent cycle vertices. Hence adjacent outside vertices
must have adjacent types in the type cycle $C_5$.

The following three cases are exhaustive by (7).

### Case I: complete outside graph and all vertices typed

Let $\mathcal P,\mathcal Q$ be the type supports on $P,Q$.
Every type in $\mathcal P$ is adjacent to every type in
$\mathcal Q$. Both supports cannot have at least two elements:
that would give a $K_{2,2}$ in $C_5$, which has no four-cycle.
Therefore one support is a singleton.

Say all vertices of $Q$ have type $i$. Vertices of $P$ then have
only types $i-1,i+1$. If their multiplicities are $a,b$, the entire
graph $L$ is the $C_5$ blow-up whose central part has size
$|Q|+1$, whose two neighboring parts have sizes $a+1,b+1$, and whose
remaining two parts are singletons. The two neighboring parts have
total size $|P|+2$.

In the odd case, unbalanced outside sides are impossible. If the
singleton-support side has size $m-1$, its central blow-up part has
size $m$, and adjoining either nonneighboring singleton gives an
independent $(m+1)$-set. If that side has size $m-3$, the two
neighboring blow-up parts have total size $m+1$, again an independent
set. Thus the outside sides both have size $m-2$, and

$$
L=C_5(a,m-1,m-a,1,1)
\quad\text{for some }1\le a\le m-1,
\tag{8}
$$

after cyclic relabeling.

In the even case, the singleton-support side has size $m-3$ or
$m-2$. The two other nonsingleton parts have total size $m$ or
$m-1$, respectively. The degrees of the two singleton vertices
therefore have sum at most $m+2$. In particular,

$$
\delta(L)\le \left\lfloor m/2\right\rfloor+1.
\tag{9}
$$


### Case II: one missing outside edge and all vertices typed

Let the missing edge be $uv$, with $u\in P,v\in Q$. The remaining
sets $P'=P\setminus\{u\}$, $Q'=Q\setminus\{v\}$ are nonempty in the
ranges under consideration.

If the types of $u,v$ are adjacent, adding $uv$ is triangle-free:
their cycle neighborhoods are disjoint, and adding a cross-edge to a
bipartite outside graph creates no triangle within that outside graph.
The resulting graph is Case I. Thus $L$ is a graph of Case I with one
edge deleted. In the odd case the added-edge graph still has independence
number at most $m$, because adding edges cannot increase independence.

Suppose instead that the types of $u,v$ are not adjacent. We show that
each ordinary side $P',Q'$ has just one type. If $P'$ had two distinct
types, every type in $Q'$ would be a common neighbor of those two
types. Such a common neighbor, if it exists in $C_5$, is unique.
Call it $b$. The type of $v$, being adjacent to all types on $P'$,
must also be $b$. But the type of $u$ is adjacent to $b$, because
$u$ is adjacent to every vertex of $Q'$. This contradicts the
assumed incompatibility of $u,v$. The argument with $P',Q'$
interchanged gives the other assertion.

Let the ordinary types be adjacent cycle vertices $a,b$. The type
of $u$ must be the neighbor of $b$ other than $a$, and the type
of $v$ the neighbor of $a$ other than $b$; otherwise $u,v$
would have compatible types. In cyclic order the five types are
$a,b,c,e,d$, where $c,d$ are these two exceptional types. The
resulting blow-up is exactly

$$
C_5(|P|,|Q|,2,1,2).
\tag{10}
$$

For odd order its weights are $(m-2,m-2,2,1,2)$. For even order they
are $(m-3,m-2,2,1,2)$, up to reflection. The singleton vertex in
(10) has degree four.

### Case III: one outside vertex has only one cycle neighbor

Call this vertex $u\in P$. The outside graph is complete bipartite,
and every other outside vertex is typed. We show explicitly that a
second cycle neighbor can be added to $u$, preserving triangle-freeness.

Choose any typed vertex of $P\setminus\{u\}$. Every type on $Q$
is adjacent to its type, so $Q$ uses at most two types.

If $Q$ uses two types, they are $i-1,i+1$ for some $i$. Their
cycle neighborhoods have union

$$
\{i-2,i,i+2\}.
$$

The sole cycle neighbor of $u$ cannot lie in this union, since $u$
is adjacent to all of $Q$. It is therefore $i-1$ or $i+1$.
Add the other of these two cycle neighbors to $u$. They are
nonadjacent in $C$, and neither is adjacent in $L$ to any vertex of
$Q$, so no triangle is created.

If $Q$ uses just one type $b$, the sole cycle neighbor of $u$
lies in $\{b,b-2,b+2\}$. If it is $b-2$ or $b+2$, add $b$;
if it is $b$, add $b+2$. In each case the resulting pair is the
cycle neighborhood of type $b-1$ or $b+1$, compatible with type
$b$. Again no triangle is created.

The augmented graph is now Case I, and $L$ is obtained from it by
deleting the added edge.

### Completing the two core lemmas

In the odd case, Cases I--III prove that $L$ is either a graph
$J$ of form (8), possibly with one edge deleted, or the graph

$$
C_5(m-2,m-2,2,1,2).
$$


Label the two singleton vertices of $J$ as $x,y$ so that $x$ is
adjacent to the part of size $a$. Deleting $x$ leaves a bipartite graph with
sides of size $m,m$, and $x$ has $a$ neighbors on one side and
one on the other. Deleting $y$ gives the corresponding counts
$m-a,1$. Choose the singleton for which the first count is smaller.

If an edge was deleted from $J$ to obtain $L$, it cannot have been
the edge $xy$: removing that unique edge turns the underlying
five-cycle into a path and makes the entire graph bipartite, contradicting
$\alpha(L)\le m$. Thus the chosen vertex still has one neighbor on
the singleton side, and its other side count is at most
$\lfloor m/2\rfloor$. This other count is positive, since otherwise
the chosen vertex would be pendant on a bipartite graph, making $L$
bipartite. Finally

$$
e(L)=m^2-h+p+q\ge m^2
$$

gives $h\le p+q=p+1$. This proves (4).

For the exceptional odd blow-up, delete its singleton. The two
remaining sides have sizes $(m-2)+2=m$. The deleted vertex has two
neighbors on each side; the four edges between the two parts of size
two are the missing cross-edges. This is (5).

In the even case, Cases I and III, and the compatible subcase of
Case II, give (9), since deleting an edge cannot raise the minimum
degree. The incompatible subcase has a degree-four vertex. For
$m\ge9$,

$$
m-3>\left\lfloor m/2\right\rfloor+1,\qquad m-3>4.
$$

Both possibilities contradict (6), proving the even-core lemma.

## The degree-$r$ branch

Suppose $H$ has $3r$ vertices, $\alpha(H)\le3$, and no $K_r$.
Set $m=r-1$. Suppose there is a vertex $v$ of target degree $r$.
Put

$$
A=N_H(v),\qquad B=V(H)\setminus N_H[v],\qquad
F=\overline{H[A]},\qquad L=\overline{H[B]}.
$$

Then

$$
|A|=m+1,\qquad |B|=2m+1.
$$

Since $v$ has no target neighbor in $B$, one has
$\alpha(H[B])\le2$, so $L$ is triangle-free. The absence of
$K_r$ gives $\alpha(L)\le m$. Inherited density gives

$$
e(L)\ge (r-1)p_r(2r-1)=(r-1)^2=m^2.
$$

For $m\ge7$, apply the odd-core lemma.

There is an edge $cu\in E(F)$, since otherwise $H[A]$ itself would
be a $K_r$. Define

$$
S=(N_H(c)\cap B)\cup(N_H(u)\cap B).
$$

This is a vertex cover of $L$: an uncovered edge $bb'$ of $L$,
together with $c,u$, would be a target-independent four-set.

We have

$$
D_r(r+2)=\binom r2+3.
$$

Apply this inherited cap to $\{c,u\}\cup X\cup\{z\}$. The target
edges inside $X$ number $\binom m2$, and there are $m-p$ target
edges from $z$ to $X$. If $t_X$ counts the target incidences from
$c,u$ to $X$, and $t_z$ those from $c,u$ to $z$, the cap gives

$$
\binom m2+m-p+t_X+t_z
\le\binom{m+1}{2}+3.
$$

Since $t_X\ge|S\cap X|$ and $t_z\ge\mathbf1_{z\in S}$,

$$
|S\cap X|+\mathbf1_{z\in S}\le p+3.
$$

The same argument on $Y$ yields

$$
|S\cap Y|+\mathbf1_{z\in S}\le q+3.
\tag{11}
$$


If $z\in S$, the uncovered subsets of $X,Y$ have sizes at least
$m-p-2,m-q-2$. There are no $L$-edges between them, since $S$
covers $L$. Therefore

$$
h\ge(m-p-2)(m-q-2).
\tag{12}
$$


If $z\notin S$, all $L$-neighbors of $z$ belong to $S$.
Triangle-freeness makes the rectangle
$(N_L(z)\cap X)\times(N_L(z)\cap Y)$ missing. The uncovered rectangle
$(X\setminus S)\times(Y\setminus S)$ is also missing, and the two
rectangles are disjoint. Thus

$$
h\ge pq+(m-p-3)(m-q-3).
\tag{13}
$$


For (4), $q=1$ and $p\le\lfloor m/2\rfloor$. When $m\ge7$,
$m-p-2\ge2$, and (12) gives

$$
h\ge2(m-3)>p+1.
$$

Also $m-p-3\ge1$, so (13) gives

$$
h\ge p+(m-4)\ge p+3>p+1.
$$

Both contradict (4).

For (5), (12) gives $h\ge(m-4)^2>4$, and (13) gives
$h\ge4+(m-5)^2>4$. Both contradict $h=4$.

This excludes the degree-$r$ branch for every $r\ge8$.

## The regular branch: reduction to an incidence system

Now suppose $H$ is $(r+1)$-regular and has no $K_r$. Again set
$m=r-1$, choose $v$, and use the same definitions of $A,B,F,L$.
This time

$$
|A|=m+2,\qquad |B|=2m.
$$

The graph $L$ is triangle-free and inherited density gives

$$
e(L)\ge(r-1)p_r(2r-2)=(r-1)(r-2)=m^2-m.
$$

For $b\in B$, regularity gives

$$
|N_H(b)\cap A|
=(m+2)-(2m-1-d_L(b))=d_L(b)-m+3\ge0.
$$

Hence $\delta(L)\ge m-3$. The even-core lemma makes $L$ bipartite
when $m\ge9$. Since $\alpha(L)\le m$, both sides $X,Y$ have size
exactly $m$.

Let $M$ be the missing bipartite graph between $X,Y$, and put

$$
h=e(M),\qquad \operatorname{def}(b)=d_M(b).
$$

The preceding edge bound gives $h\le m$.

Define columns and rows by

$$
C_b=N_H(b)\cap A\quad(b\in B),\qquad
D_a=N_H(a)\cap B\quad(a\in A).
$$

Regularity gives the exact identities

$$
|C_b|=3-\operatorname{def}(b),\qquad
|D_a|=d_F(a).
\tag{14}
$$

For the row identity, $a$ has one target neighbor $v$, exactly
$m+1-d_F(a)$ target neighbors within $A$, and $|D_a|$ in $B$.
In particular $\Delta(M)\le3$. Summing (14) gives

$$
2e(F)=\sum_b|C_b|=6m-2h,\qquad e(F)=3m-h\ge2m.
\tag{15}
$$


We also have the following properties.

- $F$ is $K_4$-free, because $\alpha(H)\le3$.
- Every row $D_a$ omits a point of $X$ and a point of $Y$.
  Otherwise $a$, together with a whole side, would form a target
  $K_{m+1}=K_r$.
- If $aa'\in E(F)$, then $D_a\cup D_{a'}$ covers $L$, since an
  uncovered edge would produce a target-independent four-set.
- If $xy\in E(L)$, then $C_x\cup C_y$ covers $F$, by the same
  four-set argument with the roles interchanged.

The next argument excludes this incidence system whenever $m\ge11$.

## A uniform incidence contradiction for $m\ge11$

### Covers, orientations, and their cost

Suppose $S\subseteq A$ is a vertex cover of $F$, with $|S|=k$.
Put $T=A\setminus S$. Then $T$ is independent in $F$, so

$$
d_F(t)\le k\qquad(t\in T).
\tag{16}
$$


Write $\Delta=\Delta(M)$. A vertex cover $Q$ of $L$ which contains
neither all of $X$ nor all of $Y$ has

$$
|Q|\ge2m-2\Delta.
\tag{17}
$$

Indeed, if $x\in X\setminus Q$, every point of $Y\setminus Q$ is a
missing neighbor of $x$, so $|Y\setminus Q|\le\Delta$. The symmetric
argument gives $|X\setminus Q|\le\Delta$.

For $st\in E(F)$, where $s\in S,t\in T$,

$$
|D_s\cup D_t|\le d_F(s)+d_F(t)\le m+1+k.
\tag{18}
$$

Whenever $m+1+k<2m-2\Delta$, (17) forces this cover of $L$ to
contain a whole side. In the case $M=\varnothing$, the same conclusion
holds without a numerical condition, since every cover of $K_{m,m}$
contains a whole side.

Call the resulting choice of a full side the orientation of the edge
$st$. In all applications below $m+1+k<2m$, so both sides cannot
be contained in $D_s\cup D_t$.

For a fixed $s$, at most three of its $T$-neighbors can have
orientation $X$. To see this, choose $x\in X\setminus D_s$, which
exists because rows omit a point of each side. Every such neighbor's
row must contain $x$, and $|C_x|\le3$. The same statement holds
for orientation $Y$.

If both orientations occur at $s$, then (16) gives

$$
|D_s\cap X|\ge m-k,\qquad |D_s\cap Y|\ge m-k,
$$

while the preceding capacity bound gives at most six neighbors in
$T$ and at most $k-1$ neighbors in $S$. Consequently

$$
2(m-k)\le |D_s|=d_F(s)\le k+5.
\tag{19}
$$

For $m\ge11$ and $k\le5$, this is impossible. Therefore all
$T$-neighbors of a given $s$ have the same orientation, and there
are at most three of them. It follows that

$$
e(F)\le\binom k2+3k.
\tag{20}
$$


### Nonempty missing graph

Suppose $h>0$. We obtain a cover $S=C_x\cup C_y$ from a suitable
edge $xy\in E(L)$.

If $\Delta=3$, choose $x$ with missing degree three and any
$L$-neighbor $y$. Equation (14) gives $C_x=\varnothing$, so
$k\le3$.

If $\Delta=2$, the same choice at a missing-degree-two vertex gives
$k\le1+3=4$.

If $\Delta=1$, the missing graph is a matching. When $h\ge2$,
choose $x\in X,y\in Y$ incident to different missing matching edges.
Then $xy\in E(L)$ and $|C_x|=|C_y|=2$, so $k\le4$.
When $h=1$, choose an endpoint of the unique missing edge and any
of its $L$-neighbors, giving $k\le2+3=5$.

These choices satisfy

$$
m>k+2\Delta+1
$$

for all $m\ge11$. Thus (18) forces a full side, and (19)--(20)
apply.

For $k\le4$,

$$
e(F)\le18<2m,
$$

contrary to (15). The only remaining possibility has $h=1,k\le5$,
when

$$
e(F)\le25<3m-1=e(F).
$$

Therefore $h>0$ is impossible.

### No missing edges

Suppose $h=0$, so $L=K_{m,m}$ and every column has size three.

If a row $D_a$ meets both sides, choose $x\in D_a\cap X$ and
$y\in D_a\cap Y$. The cover $S=C_x\cup C_y$ has size at most five,
because the columns share $a$. Every cover of $L$ contains a full
side, so (19)--(20) give

$$
e(F)\le25<3m=e(F).
$$

Thus every nonempty row lies entirely in one side.

Let $A_X,A_Y$ be the vertices with nonempty rows lying in $X,Y$,
respectively. Vertices with empty rows have degree zero by (14).
There are no $F$-edges between $A_X,A_Y$: two proper rows on
different sides cannot cover $K_{m,m}$. Both classes contain an
edge, since the total column incidence on each side is $3m>0$.

For any edge $aa'$ within $A_X$, the two rows must cover $X$;
hence

$$
d_F(a)+d_F(a')\ge m.
$$

Both endpoint degrees are at most $|A_X|-1$, so

$$
|A_X|\ge m/2+1.
$$

Likewise $|A_Y|\ge m/2+1$. But

$$
|A_X|+|A_Y|\le m+2.
$$

If $m$ is odd, integrality already contradicts this.

If $m$ is even, equality is forced: both classes have size
$m/2+1$, and every edge endpoint has degree exactly $m/2$ within
its class. Since each class contains an edge, its endpoints are
universal there; every vertex is consequently incident with an edge
and is itself universal. Each class is therefore a clique of order
$m/2+1\ge4$, contradicting that $F$ is $K_4$-free.

This completes the incidence contradiction for every $m\ge11$,
and therefore excludes the regular branch for every $r\ge12$.

## A shorter span bound from hereditary caps alone

The
[third independent input](independent/uniform_capacity_and_clique_packings.md),
Section 3, gives a separate improvement for the overloaded case:

$$
\boxed{r\ge6,\quad \alpha(H)\le3
\quad\Longrightarrow\quad |H|\le3r}
$$

under the inherited caps on $H$. This does not prove equality rigidity
at order $3r$ below the threshold $r\ge12$ of the theorem above.

Here is a shorter version of its checked argument. Restrict a putative
violation to $m=3r+1$ vertices. If it contained a $K_r$, an independent
triple outside that clique could extend into it, since each outsider
has at most one neighbor there and $r>3$. The remaining $2r+1$ vertices
would therefore have independence at most two, contradicting
[two-row capacity](two_row_structure.md). Thus $H$ is $K_r$-free.

Every nonneighborhood has independence at most two. Two-row capacity
and its $2r$ equality theorem bound its order by $2r-1$. Consequently
the complement $F$ satisfies $\Delta(F)\le2r-1$. But the inherited cap
at order $3r+1$ gives

$$
e(F)\ge(r-1)p_r(3r+1)=3(r-1)(r+1),
$$

whereas $e(F)\le(3r+1)(2r-1)/2$. The former exceeds the latter by
$(r-5)/2>0$. This contradiction proves the claim without other-color
clique information or the localized independence theorem. It improves
the cap-only span threshold, not any unsettled case of E617.

## Proof of the three-layer theorem

Suppose $H$ were $K_r$-free. If a vertex had target degree at most
$r-1$, its target nonneighborhood would have at least $2r$ vertices
and target independence number at most two. An induced $2r$-vertex
subset would contradict the two-layer theorem. Thus

$$
\delta(H)\ge r.
$$


On the other hand,

$$
e(H)\le D_r(3r)
=\binom{3r}{2}-(r-1)(3r)
=\frac{3r(r+1)}2.
$$

Hence the minimum degree is at most $r+1$. If it equals $r$, the
degree-$r$ branch above is impossible. If it equals $r+1$, the
average-degree bound forces $H$ to be $(r+1)$-regular, and the
regular branch is impossible for $r\ge12$.

Both alternatives are excluded, proving the theorem.

**Corollary.** For $r\ge12$, every inherited target graph of independence
number at most three has at most $3r$ vertices. At order $3r$, it
partitions into three target $K_r$'s, with matching cross edges.

Indeed, restrict to $3r$ or $3r+1$ vertices and find a target $K_r$
using the theorem. Its deletion leaves independence number at most two:
an independent triple in the remainder could be extended by a vertex of
the clique, since the triple forbids at most three clique vertices.
At remainder order $2r+1$ this contradicts the two-row span bound; at
order $2r$ the two-row structure theorem supplies two further $K_r$'s.
The local cap makes all cross edges matchings.

## Scope and checks

The theorem improves the $K_r$-free three-layer emptiness threshold
from order $3r+1$ to order $3r$ for an unbounded parameter range.
It does not by itself close the outer clique-packing inequalities or
settle Problem 617.

The author checked the clone-type classification at loss at most one, the two
missing-rectangle bounds (12)--(13), the even-core boundary $m=9$, the
cover-size/orientation argument leading to (20), the final no-missing-edges
case, and the cited source hypotheses, and read the complete argument; it is
author-recorded. All cases and parameter inequalities are explicit above. No
computer enumeration, fixed-$r$ terminal catalog, or SAT certificate is
used.

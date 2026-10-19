---
name: research/erdos_617/two_supported_private_cliques
desc: A color-coupling reduction to private cliques with total deficit at most r minus one, and rigorous constraints on its exceptional vertices.
tags: [graph-theory, proved, private-cliques, reductions]
sources: []
created: 2026-09-22T00:18:43Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/two_supported_private_cliques

***

**Proved reductions, not a resolution.** A hypothetical balanced coloring
has a color with a maximum independent set of order $r$, disjoint private
cliques of total deficit at most $r-1$, and at most $r$ exceptional vertices,
each adjacent to exactly two members of that independent set. The selected
color need not be a least color. The reductions below force a private
deficit of order at least $\sqrt r$, but do not exclude this concentration.

After full-row deletion, the
[minimum-anchor normalization](two_support_normalization.md) also
removes hidden $K_r$'s while retaining two-support structure, and
ensures degree at least $r$ at every private vertex. It does not
give the least-color budget or minimum degree on the exceptions.

Throughout, $r\ge4$, $N=r^2+1$, and the color graphs $G_1,\ldots,G_r$
partition $E(K_N)$ and satisfy $\alpha(G_j)\le r$. We use the
[inherited density bound](reductions.md)

$$
e(G_j[W])\le D_r(|W|),\qquad
D_r(n)=\binom n2-(r-1)p_r(n),
$$

where $p_r(rq+b)=r\binom q2+qb$ for $0\le b<r$. In particular, every
$(r+1)$-set spans at most $\binom r2+1$ edges of one color. There is no
monochromatic $K_{r+1}$, and an outside vertex has at most one neighbor in
a monochromatic $K_r$ in its color.

## 1. Selecting a two-supported private-clique system

Choose a color-$i$ clique $Q$ of order $r$. Such a clique exists by the
[localized independence inequality](packing_tools.md): a least color graph
has average degree at most $r$, and clique number at most $r-1$ would give

$$
\alpha(G_i)\ge
\frac{2N}{\overline d(G_i)+\omega(G_i)+1}
\ge\frac Nr>r.
$$

This checked independence inequality is the only non-elementary input in
the selection of $Q$.

For every $j\ne i$, the set $Q$ is a maximum independent set in $G_j$.
Every outside vertex has at least one color-$j$ neighbor in $Q$; otherwise
it augments $Q$. Consequently, among its $r$ edges to $Q$, either color
$i$ occurs once and all other colors occur once, or color $i$ is absent
and exactly one other color occurs twice.

Let $B_j$ be the outside vertices having two color-$j$ neighbors in $Q$,
and write $b_j=|B_j|$. Then

$$
\sum_{j\ne i}b_j=N-r-e_i(Q,V\setminus Q)\le r^2-r+1.
\tag{1}
$$

For $q\in Q$, put

$$
P_{j,q}=\{q\}\cup
\{x\notin Q:N_j(x)\cap Q=\{q\}\}.
$$

Each $P_{j,q}$ is a clique: two nonadjacent private vertices could replace
$q$ in $Q$. The private cliques are disjoint and have order at most $r$.
Writing $t_{j,q}=r-|P_{j,q}|$, vertex counting gives

$$
\sum_{q\in Q}t_{j,q}=b_j-1.
\tag{2}
$$

In particular $b_j\ge1$. Since $r\ge3$, (1) ensures that some $j\ne i$
has $b_j\le r$: otherwise the left side is at least
$(r-1)(r+1)>r^2-r+1$.

Fix such a color and suppress $j$. We obtain $r$ private cliques $P_q$,
with

$$
|P_q|=r-t_q,\qquad
T:=\sum_qt_q=b-1\le r-1,
\qquad B:=V\setminus\bigcup_qP_q,\quad |B|=b.
\tag{3}
$$

Each $x\in B$ has a two-element *support* $K_x=N(x)\cap Q$. Thus the
supports form a multigraph on $Q$, with one edge for each exception.

## 2. The exact two-support inequality

Fix an exception $x$ supported on $\{u,v\}$, and put

$$
A_u=P_u\setminus N(x),\qquad A_v=P_v\setminus N(x),
\qquad m_u=|A_u|,\quad m_v=|A_v|.
$$

The sets $A_u,A_v$ are complete to each other. Otherwise $x$, two
nonadjacent representatives, and $Q\setminus\{u,v\}$ are an independent
$(r+1)$-set. Therefore, with $c_{uv}=e(P_u,P_v)$,

$$
c_{uv}\ge m_um_v.
\tag{4}
$$

If $t_u+t_v\ge1$, then $P_u\cup P_v\cup\{x\}$ has between $r+2$
and $2r$ vertices. Substituting its order in $D_r$ and subtracting its
internal clique edges and the edges incident with $x$ yields

$$
c_{uv}\le m_u+m_v+(t_u-1)(t_v-1).
$$

Together with (4), this gives

$$
(m_u-1)(m_v-1)\le(t_u-1)(t_v-1)+1.
\tag{5}
$$


Suppose $t_u,t_v\ge1$ and $t_u+t_v\ge3$. If both $m_u>t_u$ and
$m_v>t_v$, the left side of (5) is at least $t_ut_v$, while its right
side is at most $t_ut_v-1$. Thus $x$ misses at most $t_q$ vertices in at
least one supporting private clique. When $t_u=t_v=1$, either some
$m_q\le1$, or $m_u=m_v=2$.

If one supporting deficit is zero, Section 4 proves that $x$ is complete
to its other supporting private clique, whose deficit is positive.
Consequently every exception has an owner $q\in K_x$ such that

$$
t_q\ge1,
\qquad |P_q\setminus N(x)|\le\max(t_q,2).
\tag{6}
$$


## 3. A necessary large private deficit

Assign each exception one owner satisfying (6). There are $T+1$
exceptions and total capacity $\sum_qt_q=T$, so some $q$ owns at least
$t_q+1$ exceptions. Adjoin any $t_q+1$ of them to the entire clique
$P_q$. The resulting $(r+1)$-set has at most

$$
(t_q+1)\max(t_q,2)+\binom{t_q+1}{2}
$$

missing target edges. The local cap requires at least $r-1$ missing edges,
so

$$
r-1\le(t_q+1)\max(t_q,2)+\binom{t_q+1}{2}.
\tag{7}
$$

For $r\ge7$, one cannot have $t_q=1$, since the right side would be $5$.
Hence $t_q\ge2$ and

$$
t_q(t_q+1)\ge\frac{2(r-1)}3.
\tag{8}
$$

Thus the near-full hypothesis $|P_q|\in\{r-1,r\}$ cannot hold for this
two-supported system when $r\ge7$. The reduction instead forces a
concentrated deficit of order at least $\sqrt r$. There is no established
upper bound excluding that concentration.

## 4. Exact clique absorption at full private rows

Suppose an exception $x$ has support $\{u,v\}$ and $t_v=0$. Its sole
neighbor in the full clique $P_v$ is $v$. If some $y\in P_u$ were
nonadjacent to $x$, (4) would make $y$ adjacent to all $r-1$ vertices of
$P_v\setminus\{v\}$, contradicting the outside-neighbor bound for $P_v$.
Thus $x$ is complete to $P_u$. Necessarily $t_u>0$, since $x$ cannot be
complete to another $K_r$. In particular no support edge joins two
zero-deficit anchors.

For each positive-deficit anchor $u$, let $H_u$ consist of exceptions
whose support is $\{u,v\}$ for some zero-deficit anchor $v$. The set
$H_u$ is a clique. Indeed, suppose $x,y\in H_u$ are nonadjacent, with
other supporting anchors $v,w$. If $v=w$, choose any
$z\in P_v\setminus\{v\}$. Then

$$
\{x,y,z\}\cup(Q\setminus\{u,v\})
$$

is an independent $(r+1)$-set. If $v\ne w$, each list

$$
P_v\setminus(N(x)\cup N(y)),\qquad
P_w\setminus(N(x)\cup N(y))
$$

has at least $r-2\ge2$ vertices. The edges between the two full cliques
form a matching, so there are nonadjacent representatives $z_v,z_w$ from
these lists. They, $x,y$, and $Q\setminus\{u,v,w\}$ again give an
independent $(r+1)$-set. The representatives are private vertices, so they
are anticomplete to the remaining anchors.

Every member of $H_u$ is complete to $P_u$. Consequently

$$
P_u\cup H_u\text{ is a clique},\qquad |H_u|\le t_u.
\tag{9}
$$

These enlarged cliques are disjoint. Delete the original full rows and
absorb each $H_u$ into its owner row. The absorbed vertices are private
relative to the remaining anchors, and each unabsorbed exception still
has a two-element support among those anchors.

Ordinary greedy extension does not alone prove that deleting $k$ full
rows reduces independence to $r-k$: it only extends a set $I$ when
$|I|+k\le r$. Absorbed exceptions also retain neighbors among the deleted
original anchors. The two-support structure nevertheless resolves this
boundary case when there are at least three full original rows, by the
separate [exact full-row deletion theorem](full_row_deletion.md).

For the selected system and $r\ge12$, (8) forces a deficit at least
three. If $z$ is the number of zero-deficit anchors, then

$$
T\ge\max_qt_q+(r-z-1),\qquad T\le r-1,
$$

so $z\ge\max_qt_q\ge3$. Thus exact deletion applies. After the first
drop the anchor count is less than $r$, and subsequent full-row deletions
and absorptions preserve the required independence bound by greedy
extension; see the linked theorem. This still does not bring the core
into the known small-independence range of the
[hereditary span bound](hereditary_span_bound.md).

## 5. Transfer to degree-sum-minimal independent sets

The original anchor set $Q$ has degree sum

$$
\sum_{q\in Q}d(q)
=\sum_q(|P_q|-1)+2b
=N-r+b
=r^2-r+T+2\le r^2+1.
\tag{10}
$$

Choose a maximum independent set $I$ minimizing its degree sum in the
same color. Let $P'_u$ be its private cliques, let $B'$ be the remaining
vertices, and put $k_x=|N(x)\cap I|\ge2$ for $x\in B'$. Exact counting
of the edges incident to $I$ gives

$$
\sum_{u\in I}d(u)
=N-r+|B'|+\sum_{x\in B'}(k_x-2).
$$

Comparison with (10) yields the joint budget

$$
|B'|+\sum_{x\in B'}(k_x-2)\le b\le r.
\tag{11}
$$

In particular, the new total private deficit satisfies

$$
T':=\sum_{u\in I}(r-|P'_u|)=|B'|-1\le T\le r-1,
\qquad
\sum_{x\in B'}(k_x-2)\le r-T'-1.
\tag{12}
$$

Also $d(x)\ge d(u)$ for $x\in P'_u$, since exchanging $u$ for $x$
preserves a maximum independent set. Thus degree-sum minimality and total
private deficit at most $r-1$ can be imposed simultaneously. The new
exceptions need not be two-supported, and the selected color still need
not be a least color.

## 6. A sufficient condition for absorption to lower independence

The elementary criterion below remains valid. The
[exact full-row deletion theorem](full_row_deletion.md) is stronger when
there are at least three full rows and applies to the selected system
for $r\ge12$, irrespective of this matching criterion.

Return to the original two-supported system. Let $Z$ be its zero-deficit
anchors and $k=|Z|$. Perform the deletion and absorption of Section 4,
obtaining an induced residual $R$. If the bipartite support graph between
$Z$ and $Q\setminus Z$ has no matching covering $Z$, then

$$
\alpha(R)\le r-k.
\tag{13}
$$

In particular, (13) holds when $k>r/2$.

To prove this, suppose $J\subseteq R$ is independent of order $r-k+1$.
For each $v\in Z$, the list $L_v=P_v\setminus N(J)$ has at least $k-1$
vertices. Unless $J$ contains an absorbed exception whose original
support includes $v$, the original anchor $v$ lies in $L_v$. It is
anticomplete to every other deleted private row. Choose it first and
greedily choose representatives from the remaining $k-1$ lists, each of
size at least $k-1$. This augments $J$ to an independent $(r+1)$-set.

If $J$ contains at least two absorbed exceptions supported on $v$, those
exceptions have the same sole neighbor $v$ in $P_v$. Hence
$|L_v|\ge k$. Leave that larger list to last in a greedy transversal,
again obtaining a contradiction.

Therefore failure requires exactly one absorbed exception from $J$ for
each $v\in Z$. Their positive-deficit owners are distinct: two
exceptions with the same owner lie in the clique $H_u$. Their original
support edges give a matching covering $Z$, proving (13).

This argument alone does not exclude a matching covering $Z$. The exact
deletion theorem handles that case using a minimal Hall-deficient family
of support lists, whose one- and two-element lists have at most two
boundary incidences.

## 7. Structural closure of full rows and a proper overloaded core

For $r\ge12$, every original private clique $P_u$ in the selected system
has order at least four. Indeed, if $|P_u|\le3$, then
$t_u\ge r-3$. Since $T\le r-1$, at most three anchors have positive
deficit. Write their number as $a\le3$. There are $r-a>r/2$ full rows,
so Section 6 gives an induced residual of order $ar+1$ and independence
number at most $a$. For $a=1$ the local cap is a contradiction; for
$a=2,3$, the [two-row](two_row_structure.md) and
[three-row](three_row_structure.md) span bounds give a contradiction.

Assume now that every original $|P_u|\ge4$. The full-row absorption can
be iterated as a statement about cliques, without claiming that a reduced
anchor set remains maximum independent. Keep the **original** independent
set $Q$ and its original private cliques throughout the proof. Grow
pairwise disjoint cliques $C_u$, initially $C_u=P_u$, by assigning
exceptional vertices to their supporting anchors. A row is called full
when $|C_u|=r$.

Suppose $C_u$ is full and an unassigned exception $x$ has support
$\{u,v\}$. Its only neighbor in $C_u$ is $u$. If some original private
vertex $y\in P_v$ were nonadjacent to $x$, the original two-support
augmentation in Section 2 would make $y$ adjacent to every vertex of
$P_u\setminus\{u\}$. Since $|P_u|-1\ge3$, this contradicts the
outside-neighbor bound for the full clique $C_u$. Thus $x$ is complete
to the original $P_v$.

All exceptions assigned to a fixed row $v$ by this rule are pairwise
adjacent. To verify this, let $x,y$ be two such exceptions, with other
supporting anchors $u,w$ whose growing rows are full. If $u=w$, the
original private set $P_u\setminus\{u\}$ is nonempty and anticomplete to
$x,y$. If $x,y$ were nonadjacent, one of its vertices would augment
$Q\setminus\{u,v\}$ with $x,y$. If $u\ne w$, use the original private
lists

$$
P_u\setminus(N(x)\cup N(y)),\qquad
P_w\setminus(N(x)\cup N(y)).
$$

Each has at least $|P_u|-2\ge2$ or $|P_w|-2\ge2$ vertices, respectively.
Edges between the disjoint full cliques $C_u,C_w$ form a matching, so
nonadjacent representatives exist. With $x,y$ and
$Q\setminus\{u,v,w\}$ they would again augment the original independent
set. This proves the assertion.

Consequently $C_v=P_v$ together with the exceptions assigned to $v$ is
always a clique. Assign $x$ to $v$, and mark $v$ full if its row reaches
order $r$. An unassigned exception cannot have both endpoints full:
the preceding argument would make it complete to the original $P_v$,
giving it more than one neighbor in the full $C_v$. Thus the process
cannot overfill any row, and terminates with no unassigned exception
incident to a full row.

This closure gives a purely structural restriction on the support
multigraph. For a support component $A\subseteq Q$, write $b_A$ for its
number of exceptional edges and put

$$
\delta_A=b_A-\sum_{u\in A}t_u.
$$

If $\delta_A>0$, that component is not a pseudoforest. To prove this,
run the closure within the component. Each assignment removes one
unassigned edge and consumes one unit of the receiving row's capacity,
so edges minus remaining capacity stays equal to $\delta_A$. At
termination all remaining edges lie on nonfull rows, each with positive
remaining capacity. Let $U$ be the anchors of all nonfull rows, including
isolated ones. The number of remaining
edges is therefore at least

$$
|U|+\delta_A\ge |U|+1.
$$

This is impossible if the original component is a pseudoforest, since
every induced subgraph of a pseudoforest has at most as many edges as
vertices. The argument also covers $U=\varnothing$, when positive excess
cannot remain.

The support multigraph has total excess $b-T=1$, so it has a component
with $\delta_A>0$. Being connected and not a pseudoforest, that component
has at least $|A|+1$ exceptional edges. Since $b\le r$, necessarily

$$
a:=|A|\le r-1.
\tag{14}
$$

Take the original private rows anchored in $A$ and all exceptional
vertices supported there. This induced graph is anticomplete to
$Q\setminus A$, so its independence number is at most $a$. Its order is

$$
\sum_{u\in A}(r-t_u)+b_A=ar+\delta_A>ar.
\tag{15}
$$

Thus the reduction yields a **proper** overloaded core, not merely the
original independence-$r$ graph. Restricting further gives a core on
$ar+1$ vertices if desired.

The established span theorems rule out (15) when $a\le3$ (for $r\ge12$)
or when $r\ge64a^2$. They do not exclude its remaining possible range
$4\le a\le r-1$. Structural closure has not supplied a bound reducing
$a$ to the known small-independence range.

## 8. Excess deficit and a stronger full-row count

**Proved, author-recorded.** Let $a$ now denote the number of
positive deficits, put $D=\sum_i d_i=b-1$, and set

$$
E=D-a=\sum_{d_i>0}(d_i-1).
$$

For $r\ge7$, every selected two-supported system satisfies

$$
r-1\le\binom{E+3}{2}. \tag{16}
$$

The statement applies both to the original system and to the core after
full-row deletion.

First, $E=0$ is impossible. All positive deficits would equal one;
Section 2 assigns every exception to a positive row in which it misses
at most two vertices. Since $b=D+1$, one row receives two exceptions.
Their union with its private $K_{r-1}$ misses at most five edges,
contrary to the local cap when $r\ge7$.

For $E\ge1$, give each positive row the threshold

$$
h_i=E-d_i+2.
$$

Every exception has a supporting positive row $i$ in which it misses at
most $h_i$ private vertices. This follows from completeness when its other
supporting row is full. Otherwise, for positive endpoints $i,j$, put
$x=d_i-1$, $y=d_j-1$. We have $x+y\le E$, and

$$
h_ih_j-\bigl((d_i-1)(d_j-1)+1\bigr)
=(E+1)^2-(E+1)(x+y)-1\ge E>0.
$$

Thus missing more than both thresholds contradicts (5).

Assign an owner using these thresholds. Some row of deficit $d$ owns at
least $d+1$ exceptions. Its entire private clique together with these
exceptions is an $(r+1)$-set with at most

$$
(d+1)(E-d+2)+\binom{d+1}{2}
=(d+1)\left(E+2-\frac d2\right)
\le\binom{E+3}{2}
$$

missing edges. The last expression is maximized at $d=E+1$ on
$1\le d\le E+1$. The local cap proves (16).

If the original system has $z$ full rows, then $a=r-z$ and
$E=D-a\le z-1$. Hence the exact deletion theorem can start with at least

$$
\boxed{z\ge\lambda(r):=
\left\lceil\frac{\sqrt{8r-7}-3}{2}\right\rceil}
\tag{17}
$$

full rows. This improves the earlier $\sqrt{2r/3}+O(1)$ bound to
$\sqrt{2r}+O(1)$. In the final all-deficient core, $E=D-a\le r-a-1$
gives the same bound $r-a\ge\lambda(r)$. This is still not a uniform
exclusion of the core.

## 9. All row-plus-exception caps

Let $F=\overline{H[B]}$, where $H$ is the selected color graph (or its
two-supported core). For every row $i$ and every $S\subseteq B$,

$$
\boxed{
\sum_{x\in S}\bigl(d_H(x,P_i)+d_i-1\bigr)-e(F[S])
\le d_i(r-1).}
\tag{18}
$$

For $s=|S|\ge d_i$, the set $P_i\cup S$ has order $r-d_i+s$
between $r$ and $2r$, since $|B|\le r$. On this interval,

$$
D_r(r-d_i+s)=\binom r2+\binom{s-d_i+1}{2}.
$$

Subtract $\binom{r-d_i}{2}$ and use
$e(H[S])=\binom s2-e(F[S])$ to obtain (18). For $s<d_i$, each
summand is at most $r-1$, so the inequality is immediate.

No assignment theorem has been deduced from (18). In particular,
maximizing a functional $w(S)-e(F[S])$ is not the usual capacitated
orientation deficiency problem, which involves incident edges instead.

## 10. Independent exceptional sets and their common nonneighbors

If $X\subseteq B$ is independent and $U$ is the union of its supports,
then

$$
\alpha\!\left(H\!\left[
\bigcup_{i\in U}(P_i\setminus N_H(X))\right]\right)
\le |U|-|X|. \tag{19}
$$

Indeed, a larger independent set there could be combined with $X$ and
all anchors outside $U$ to exceed the full independence bound.
Consequently, when the support edges of $X$ form a tree, the displayed
common-nonneighbor union is a clique; when $|X|=|U|$, it is empty.
These are exact geometric constraints not captured by (18) alone.

## 11. Capacitated Hall constraints on exceptional cliques

Here assume the core is all-deficient, so $d_i\ge1$. Put $q=r-1$ and

$$
w_i(x)=d_H(x,P_i)+d_i-1
=q-|P_i\setminus N_H(x)|\ge0.
$$

For an exception $x$ supported on $\{u,v\}$,

$$
w_u(x)+w_v(x)\ge q. \tag{20}
$$

Its nonneighbors in $P_u\cup P_v$ form a clique, by the two-support
augmentation argument. This clique has order at most $r-1$: if it
contained a $K_r$, each of the outside anchors $u,v$ would have at most
one neighbor there, while every chosen vertex is adjacent to its own
anchor, an impossibility for $r\ge3$. This proves (20).

For a nonempty anchor set $U$, let

$$
B_U=\{x\in B:K_x\subseteq U\},\qquad D_U=\sum_{i\in U}d_i.
$$

Apply (18) with $S=B_U$ and sum over $i\in U$. Nonnegativity permits
retaining just the two support contributions from (20), giving

$$
\boxed{|U|\,e(F[B_U])\ge(r-1)(|B_U|-D_U).} \tag{21}
$$

In particular $e(F[B])\ge\lceil(r-1)/a\rceil$, where $a$ is the
number of core anchors.

If $C\subseteq B$ is a target clique, apply the same argument to
$C_U=\{x\in C:K_x\subseteq U\}$. Now $e(F[C_U])=0$, so

$$
|C_U|\le D_U\qquad(U\subseteq[a]).
$$

These are the capacitated Hall conditions: each exceptional target
clique can be assigned to supporting rows with capacities $d_i$.
In particular $B$ itself is not a target clique, since $|B|=D+1$.

No argument extends these assignments to all exceptions. The missing
exception-edge terms in (21) are a real remaining term, not an established
contradiction. The nonnegativity used above also explains why this
summation is stated only after all full rows have been removed.

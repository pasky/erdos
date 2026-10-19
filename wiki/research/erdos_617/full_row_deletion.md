---
name: research/erdos_617/full_row_deletion
desc: Exact deletion of at least three full private rows in a two-supported system, followed by safe clique absorption and iteration.
tags: [graph-theory, proved, private-cliques, reductions]
sources: []
created: 2026-09-22T00:31:00Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/full_row_deletion

***

**Status: proved, author-recorded.** The first deletion theorem
resolves the independent-transversal boundary in the
[two-supported private-clique reduction](two_supported_private_cliques.md).
For the selected color when $r\ge12$, full rows can be deleted and their
incident exceptions absorbed until every surviving private row is
deficient. The resulting proper core is still not excluded in general.

## 1. Hypotheses and statement

Let $r\ge5$, and let $G$ have an independent set
$Q=\{q_1,\ldots,q_r\}$ with $\alpha(G)\le r$. Suppose every vertex
outside $Q$ has exactly one or two neighbors in $Q$. Define the private
rows

$$
P_i=\{q_i\}\cup\{x\notin Q:N(x)\cap Q=\{q_i\}\},
$$

and let $B$ be the remaining vertices. Thus each exception $x\in B$
has a two-element support $N(x)\cap Q$.

Assume the private rows are cliques of order at most $r$, and that

$$
\text{every vertex outside any }K_r\text{ has at most one neighbor in it.}
\tag{1}
$$

Condition (1) also rules out $K_{r+1}$. All these hypotheses follow from
the inherited density bound in the selected color. In particular, (1)
follows by applying the $(r+1)$-set cap to a full clique and one outside
vertex.

Let $Z$ be the indices of full rows, that is, $|P_i|=r$; put

$$
z=|Z|,\qquad A=[r]\setminus Z,\qquad a=|A|=r-z,
\qquad X=\bigcup_{i\in A}P_i\;\cup B.
$$


**First-deletion theorem.** If $z\ge3$, then

$$
\alpha(G[X])\le a.
\tag{2}
$$


The theorem does not need a bound on $|B|$ or the total private deficit.

## 2. Exceptions incident with full rows

For an exception $x$ supported on $\{i,j\}$, the two lists
$P_i\setminus N(x)$ and $P_j\setminus N(x)$ are completely joined.
Otherwise nonadjacent representatives, together with $x$ and
$Q\setminus\{q_i,q_j\}$, give an independent $(r+1)$-set.

No exception can have both support indices in $Z$. If it did, the two
lists above would each have order $r-1$ by (1), and their union would
be a clique of order $2r-2>r$.

If $x$ has support $\{i,j\}$ with $i\in A$ and $j\in Z$, then
$x$ is complete to $P_i$. Indeed, a vertex of $P_i\setminus N(x)$
would be adjacent to all $r-1$ points of $P_j\setminus N(x)$, contrary
to (1).

For a fixed $i\in A$, all exceptions supported on $i$ and some member
of $Z$ form a clique. Suppose two such exceptions $x,y$ were
nonadjacent, and let $J\subseteq Z$ be their zero-row endpoints, with
$t=|J|\in\{1,2\}$. Start with

$$
\{x,y\}\cup
\bigl(Q\setminus(\{q_i\}\cup\{q_j:j\in J\})\bigr),
$$

an independent set of size $r+1-t$. In each of the $t$ full rows,
successively choose a representative avoiding $x,y$ and previous
representatives. At most $2+(t-1)\le3$ points are forbidden by (1),
so the choices exist. Retained anchors have no neighbors in other
private rows. The resulting independent set has size $r+1$, a
contradiction.

## 3. What failure of extension would force

Suppose, contrary to (2), that $T\subseteq X$ is independent and
$|T|=a+1$. For every full row put

$$
L_j=P_j\setminus N(T),\qquad j\in Z.
$$

By (1),

$$
|L_j|\ge r-|T|=z-1.
\tag{3}
$$


Let $k$ be the number of full-row anchors having a neighbor in $T$.
If $k\le z-1$, keep the other $z-k$ anchors and greedily choose
representatives from the $k$ touched rows. At most $k-1\le z-2$
previous representatives can forbid points of any list in (3).
Untouched anchors have no neighbors in the other private rows.
This extends $T$ to an independent set of size $(a+1)+z=r+1$.
Thus every full-row anchor is touched.

If some list has size at least $z$, choose representatives from the
other $z-1$ lists first and from this larger list last. Equation (3)
and the matching cross edges between full rows make every greedy
choice possible. Again $T$ extends to size $r+1$.

Consequently every list has size exactly $z-1$. In each full row, the
$a+1$ vertices of $T$ therefore have exactly one neighbor each, and
these neighbors are distinct. In particular, exactly one member of
$T$ is adjacent to each full-row anchor. Such a member must be an
exception with a zero-row endpoint. No exception has two zero-row
endpoints, so $T$ contains exactly $z$ zero-supported exceptions.

Their positive endpoints are distinct, by the clique assertion in
Section 2. Let $S\subseteq A$ be those endpoints; then $|S|=z$.
For $s\in S$, denote the corresponding exception by $x_s$ and its
zero-row endpoint by $j(s)$. The map $s\mapsto j(s)$ is a bijection
from $S$ to $Z$, and $x_s$ is complete to $P_s$.

Put

$$
R=A\setminus S,\qquad |R|=r-2z,
\qquad T_0=T\setminus\{x_s:s\in S\}.
$$

Thus

$$
|T_0|=|R|+1.
\tag{4}
$$


## 4. At most two boundary supports

A private vertex in $T_0$ lies in a row indexed by $R$: a vertex of
$P_s$, $s\in S$, would be adjacent to $x_s$.

Every exception $y\in T_0$ has both endpoints in $A$, since all
zero-supported members of $T$ were removed. It cannot have both
endpoints $s,t$ in $S$. Otherwise $x_s,x_t,y$ are independent.
Keep all anchors except those indexed by
$s,t,j(s),j(t)$ and add this triple, obtaining $r-1$ independent
vertices. Choose representatives in the two full rows indexed by
$j(s),j(t)$, avoiding the triple and each other. At most four points
are forbidden in either row, so $r\ge5$ suffices. This gives an
independent $(r+1)$-set.

Assign each member of $T_0$ a nonempty support list in $R$. A private
vertex receives its singleton row index. An exception receives its
anchor endpoints lying in $R$, a set of size one or two. An
exception has an endpoint in $S$ precisely when this list is a
singleton.

By (4), choose an inclusion-minimal subcollection $C\subseteq T_0$
whose number of members exceeds the size of the union $V$ of its
$R$-support lists. Write $v=|V|$. Minimality gives

$$
|C|=v+1.
\tag{5}
$$

Every index in $V$ occurs in at least two lists: deleting the unique
member using an index would leave $v$ objects supported on at most
$v-1$ indices, contrary to minimality.

If $h$ lists are singletons, counting incidences therefore gives

$$
2v\le\sum_{c\in C}|\operatorname{supp}_R(c)|
      =2|C|-h=2v+2-h.
$$

Hence $h\le2$. Let $S_C\subseteq S$ be the endpoints in $S$ of
exceptions belonging to $C$, and put $s=|S_C|$. Then

$$
s\le h\le2.
\tag{6}
$$


## 5. Final augmentation

The set

$$
U=C\cup\{x_t:t\in S_C\}
$$

is independent, being a subset of $T$, and has $v+1+s$ vertices.
All its anchor neighbors lie among the $v+s$ positive anchors indexed
by $V\cup S_C$ and the $s$ distinct zero anchors indexed by
$J_C=\{j(t):t\in S_C\}$.

Keep every other anchor and add $U$. This gives an independent set
of size

$$
(r-v-2s)+(v+1+s)=r+1-s.
$$

Fill the $s$ full rows indexed by $J_C$ successively. In each such
row, $U$ and the earlier representatives forbid at most

$$
|U|+(s-1)=v+2s
\le r-2z+4\le r-2
$$

points. All choices exist by (1), and the retained anchors have no
neighbors in these rows. Adding the $s$ representatives produces an
independent $(r+1)$-set. This proves the first-deletion theorem.

## 6. Absorption and all subsequent deletions

Let $B_0$ be all exceptions with a zero-row endpoint. For every
$i\in A$, Section 2 shows that

$$
C_i=P_i\cup
\{x\in B_0:\text{the positive endpoint of }x\text{ is }i\}
$$

is a clique. Its order is at most $r$. Relative to the retained
anchors $\{q_i:i\in A\}$, the $C_i$ are exactly the private rows in
$G[X]$: every absorbed exception now has just its positive anchor
as a neighbor in the retained anchor set. Every other exception
still has exactly two retained anchor neighbors.

If initially $|V(G)|=r^2+1$, $|P_i|=r-d_i$,
$b=|B|\le r$, and $\sum_i d_i=b-1$, then

$$
|X|=ar+1.
$$

Writing $d'_i=r-|C_i|$ and $b'=|B\setminus B_0|$ gives

$$
\sum_{i\in A}d'_i=b'-1\le r-1.
\tag{7}
$$


Once the number $m$ of anchors is strictly below $r$, no special
first-deletion argument is needed. Suppose a two-supported system
has $m<r$ independent anchors, independence number at most $m$, and
$z'$ full private rows. An independent set of size $m-z'+1$ outside
these rows would leave in each full row a list of size at least

$$
r-(m-z'+1)=r-m+z'-1\ge z'.
$$

Representatives can be chosen greedily from all $z'$ rows, producing
an independent $(m+1)$-set. Thus deleting them lowers the independence
bound to $m-z'$.

The absorption conclusions of Section 2 remain valid with $m$ anchors:
their contradictory independent sets have size $m+1$, while all
avoidance bounds still use the fixed clique size $r\ge5$. Hence
absorption preserves the two-supported structure after each deletion.
If the graph has order $mr+1$ before the deletion, it has order
$(m-z')r+1$ afterward, and (7) is preserved with the remaining
exceptions. Iterate until no full row remains; deletion of all
anchors would itself contradict the positive remaining order.

## 7. Consequence for the selected color when $r\ge12$

In the [selected two-supported system](two_supported_private_cliques.md),
there are $r$ rows and

$$
D:=\sum_i d_i=b-1\le r-1.
$$

If $z$ deficits vanish, every other deficit is positive, so for every
positive deficit

$$
d_i\le D-(r-z-1)\le z.
\tag{8}
$$

The owner-overcapacity argument in that note supplies a deficit
$d_i\ge2$ with

$$
d_i(d_i+1)\ge\frac{2(r-1)}3.
$$

Consequently

$$
z(z+1)\ge\frac{2(r-1)}3.
\tag{9}
$$

For $r\ge12$, (9) excludes $z\le2$. Therefore the first-deletion
theorem applies, after which Section 6 permits every subsequent
full-row deletion and absorption.

The result is an induced core with $a$ independent anchors and

$$
|V|=ar+1,\qquad \alpha\le a,
\qquad |P_i|=r-d_i<r,\qquad
1\le d_i,\qquad
\sum_{i=1}^a d_i=b-1\le r-1.
\tag{10}
$$

It retains the inherited density bound, and every remaining exception
has exactly two anchor neighbors. More precisely, put

$$
\kappa(r)=\left\lceil
\frac{\sqrt{1+8(r-1)/3}-1}{2}
\right\rceil.
$$

At least $\kappa(r)$ full rows were initially deleted, so

$$
a\le r-\kappa(r)\le r-3\qquad(r\ge12).
$$

Thus some color contains at least $\kappa(r)=\Theta(\sqrt r)$ disjoint
$K_r$'s whose deletion has the stated independence drop; this color
need not be a least color. The existing
[two-row](two_row_structure.md) and
[three-row](three_row_structure.md) span bounds exclude $a\le3$;
the [general span bound](hereditary_span_bound.md) also excludes
$r\ge64a^2$.

What remains unresolved is the all-deficient core (10) outside those
proved span ranges. Exact full-row deletion does not itself bound its
number of anchors sufficiently sharply.

The later excess-deficit argument in
[Two-supported private cliques, Section 8](two_supported_private_cliques.md)
improves the initial full-row count from $\kappa(r)$ to

$$
\lambda(r)=\left\lceil\frac{\sqrt{8r-7}-3}{2}\right\rceil
=\sqrt{2r}+O(1).
$$

Consequently the final core satisfies $a\le r-\lambda(r)$. The deletion
proof above is unchanged, and this stronger count still does not exclude
all remaining cores.

## Checks

The author checked the proof in full, including the extraction of the
distinct zero-supported exceptions, the support-list minimality
argument, all augmentation cardinalities, and preservation under
iteration; it is author-recorded. It uses no computation or external
theorem.

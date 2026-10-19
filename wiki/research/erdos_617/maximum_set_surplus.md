---
name: research/erdos_617/maximum_set_surplus
desc: A linear lower bound on the degree surplus of every maximum independent set, allowing arbitrary anchor supports.
tags: [graph-theory, proved, private-cliques, reductions]
sources: []
created: 2026-09-22T13:45:00Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/maximum_set_surplus

***

**Proved necessary inequality, not a resolution of E617.** Let $r\ge12$.
Suppose a graph $Q$ satisfies the hereditary density caps
$e(Q[W])\le D_r(|W|)$ from [Reductions](reductions.md), is $K_r$-free,
and satisfies

$$
|Q|=ar+\varepsilon,\qquad \alpha(Q)=a,\qquad \delta(Q)\ge r,
\qquad \varepsilon\in\{0,1\}.
$$

Then every maximum independent set $I$ satisfies

$$
\boxed{7\sum_{q\in I}(d_Q(q)-r)\ge2a+12\varepsilon.} \tag{1}
$$

No bound on $a$, exception count, or support size is assumed. Neither
criticality, proper-induced minimality, nor an edge budget is used.

In fact, for a specified maximum set $I$, the proof only needs degree
at least $r$ at its **unit-row anchors**. Degrees at its other anchors
and at vertices outside $I$ need not be at least $r$: their individual
surpluses may be negative, but the exact identities remain valid, and
only $\sigma_U,\sigma_M\ge0$ are used at the end. The minimum-degree
hypothesis above is a convenient sufficient condition for the assertion
about every maximum set.

The proof extends the unit-row routing argument in
[Unit-deficit propagation](unit_deficit_propagation.md). Its new point
is to count higher-support exceptions separately, without routing them.
Only caps at orders $r+1,r+2,2r-1$ are needed.

## Private rows and exact accounting

Write $I=\{q_1,\ldots,q_a\}$ and $s_i=d_Q(q_i)-r\ge0$.
Let $P_i$ contain $q_i$ and all outside vertices whose only neighbor
in $I$ is $q_i$. Each $P_i$ is a clique: a nonadjacent pair in it,
together with the other anchors, would exceed $a$.
Put

$$
|P_i|=r-d_i,\quad d_i\ge1,\quad
E=\sum_i(d_i-1),\quad \sigma=\sum_i s_i.
$$

The remaining vertices form an exception set $B$, each with at least
two anchor neighbors. For $x\in B$ write $k_x=|N(x)\cap I|$, and put

$$
b=|B|=a+E+\varepsilon,\quad
v=|\{x\in B:k_x\ge3\}|,\quad
u=\sum_{x\in B}(k_x-2).
$$

Thus $v\le u$. Counting edges incident with $I$ in two ways gives

$$
\boxed{\sigma=E+u+2\varepsilon.} \tag{2}
$$

Indeed the private rows contribute $ar-a-\sum_i d_i$ incidences,
and $B$ contributes $2b+u$.

Call a row unit if $d_i=1$, and let $U$ be the set of its indices.
Then $a-|U|\le E$. A unit anchor has exactly $2+s_i$ incident
exceptions, regardless of their support sizes. An exception with
exactly two anchor neighbors will be called two-supported below.

## Local routing only uses two-supported exceptions

If a two-supported exception $x$ has supports $i,j$, then
$P_i\setminus N(x)$ and $P_j\setminus N(x)$ are completely joined:
a nonadjacent pair from these sets, together with $x$ and the unused
anchors, would be an independent $(a+1)$-set.

Suppose both rows are unit, and let their nonneighbor counts be
$m_i,m_j$. Both are positive, since otherwise $x$ creates a $K_r$.
The cap on $P_i\cup P_j\cup\{x\}$ gives

$$
(m_i-1)(m_j-1)\le1. \tag{3}
$$

For an explicit count, its $2r-1$ vertices have at most
$(r-1)^2-m_im_j+m_i+m_j$ nonedges, and the cap requires
at least $(r-1)^2$.

If $m_i\le2$, then for every $z\notin P_i\cup\{x\}$ the cap on
$P_i\cup\{x,z\}$ gives

$$
d(z,P_i)+\mathbf1_{xz\in E(Q)}\le m_i+1\le3. \tag{4}
$$

Any other two-supported exception $y$ at $i$ therefore misses at
least $r-4$ vertices of $P_i$. If it missed a private vertex in
its other supporting row, that vertex would be complete to all
these nonneighbors, contrary to (4). Consequently $y$ is complete
to its other row, which cannot be unit because $Q$ is $K_r$-free.
In particular there is no parallel unit--unit exception.

If instead $m_i\ge3$, (3) gives $m_j=1$. Let $z$ be the unique
nonneighbor of $x$ in $P_j$, and put $Z_i=P_i\cup\{x,z\}$.
Complete joining of the nonneighbor sets gives $d(z,P_i)\ge m_i$;
the cap on $Z_i$ gives $d(z,P_i)\le m_i+1$. Thus

$$
e(Q[Z_i])=D_r(r+1)-\lambda,\qquad \lambda\in\{0,1\}.
$$

Since $D_r(r+2)-D_r(r+1)=2$, every vertex outside $Z_i$ has
at most three neighbors in $Z_i$. A second two-supported exception
at $i$ cannot have other endpoint $j$, by (4) at the active endpoint
$j$. Its other row therefore lies outside $Z_i$, and the same
augmentation argument makes it complete to that row. Again the
other row is nonunit.

It follows that the support graph of two-supported exceptions between
unit rows is a matching. Let it have $t$ edges, with endpoint set
$M\subseteq U$ of order $2t$.

At each endpoint designate its matching exception. Every other
two-supported exception there is complete to its other, nonunit row.
Route it to that row. These routed exceptions are distinct across
sources: their only unit endpoint is their source.

For a nonunit row $P_j$, let $C_j$ be the routed group. Then

$$
P_j\cup C_j\text{ is a clique},\qquad |C_j|\le d_j-1. \tag{5}
$$

To verify pairwise adjacency in $C_j$, every routed exception lies
outside every source block: designated exceptions are unit--unit,
routed exceptions are unit--nonunit, and private holes are not
exceptions. Hence each routed exception has at most three neighbors
in every source row. Two nonadjacent group members from one source
have a common private nonneighbor there and augment the unused
anchors. If their sources are distinct $i,k$, their common-nonneighbor
lists in those rows have at least $r-7$ vertices. Augmentation forces
the two lists to be completely joined. Choose a listed vertex in
$P_k$ outside the source block at $i$, omitting at most its one private
hole. It has at most three neighbors in $P_i$, contradicting
$r-7>3$. This proves (5). The total routed capacity is therefore $E$.

## Higher-support incidence accounting

Let $K_U$ and $K_M$ count incidences of exceptions with support at
least three at unit anchors and matching endpoints respectively.
Write $\sigma_U=\sum_{i\in U}s_i$ and
$\sigma_M=\sum_{i\in M}s_i$. Then

$$
K_M\le K_U\le u+2v.
$$

The number of routed exceptions from matching endpoints is exactly
$2t+\sigma_M-K_M$: subtract the designated incidence at each
endpoint from its $2+s_i$ incidences and exclude the higher supports.
By (5),

$$
t\le\frac{E+u+2v-\sigma_M}{2}. \tag{6}
$$


The $b-v$ two-supported exceptions have
$2|U|+\sigma_U-K_U$ incidences at unit anchors. Only the $t$ matching
exceptions are counted twice, so

$$
b-v\ge2|U|+\sigma_U-K_U-t.
$$

Using $|U|\ge a-E$ and the identities above gives

$$
a\le3E+\varepsilon+u+v+t-\sigma_U
\le\tfrac72(E+u)+\varepsilon-\sigma_U-\tfrac12\sigma_M.
$$

Substitute (2) to obtain the slightly stronger statement

$$
7\sigma\ge2a+12\varepsilon+2\sigma_U+\sigma_M,
$$

which proves (1).

## Consequences and limitation

For the [least-budget minimal-ratio core](minimal_ratio_potential.md),
every maximum independent set has surplus at least
$\lceil(2a+12)/7\rceil$. In a balanced capped $K_r$-free graph of
order $ar$ and minimum degree at least $r$, an all-degree-$r$
maximum independent set is impossible.

If the unproved [light-set bridge](light_independent_set_obstruction.md)
gave a maximum independent set of degree sum at most
$a(r-1)+r+1$, then $\sigma\le r-a+1$, and (1) would yield

$$
9a\le7r-5.
$$

This conclusion would no longer require transferring that set to a
two-supported anchor system. The light-set bridge is still unproved,
and the displayed linear bound would itself leave an unbounded range.

The local routing hypotheses, higher-support separation, and incidence
algebra were checked by the author and are author-recorded. No
computation is used.

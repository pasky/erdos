---
name: research/erdos_617/two_row_structure
desc: Cap-only independence-two capacity and equality rigidity, with a full-cap sharpness example at two r minus one vertices.
tags: [graph-theory, proved]
sources: []
created: 2026-09-21T23:52:12Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/two_row_structure

***

Throughout, the target graph satisfies all
[inherited density inequalities](reductions.md)
$e(H[W])\le D_r(|W|)$. An actual hypothetical counterexample supplies
these inequalities, but no other-color structure is needed below.
The results hold for a variable parameter but do not resolve the problem.

## An elementary triangle-free bound

A nonbipartite triangle-free graph $L$ of order $n$ has

$$
e(L)\le\frac{(n-1)^2}{4}+1.
$$

Choose a shortest odd cycle of length $\ell\ge5$. It is induced.
Each outside vertex has at most $(\ell-1)/2$ neighbors on the cycle,
since these neighbors are independent on the cycle.
Mantel's theorem on the remaining vertices gives

$$
\begin{aligned}
e(L)&\le \ell+\frac{(n-\ell)(\ell-1)}2+\frac{(n-\ell)^2}{4}\\
&=\frac{n^2}{4}-\frac n2+\frac{6\ell-\ell^2}{4}
\le \frac{(n-1)^2}{4}+1.
\end{aligned}
$$

If $\ell\ge7$, the same calculation improves the final bound by three.
Integrality can strengthen either displayed real bound.

## No $2r+1$ vertices of target independence at most two

**Proposition.** For $r\ge3$, every induced target graph of independence
number at most two has at most $2r$ vertices.

The
[third independent input](independent/uniform_capacity_and_clique_packings.md),
Section 3, supplies the following shorter proof. Suppose $H$ has $m>2r$ vertices
and $\alpha(H)\le2$. The local cap forbids $K_{r+1}$ and allows at most one
neighbor in a $K_r$ to an outsider. If $A$ is a target $K_r$, any nonadjacent
pair outside $A$ extends into $A$ to an independent triple, since $r>2$. Thus
$H-A$ would be a clique of order greater than $r$, impossible. Hence $H$ is
$K_r$-free.

Every nonneighborhood in $H$ is a clique of order at most $r-1$.
Writing $L=\overline H$, the inherited cap and $p_r(m)\ge m-r$ give

$$
(r-1)(m-r)\le e(L)\le\frac{m(r-1)}2,
$$

contrary to $m>2r$. The elementary bound on $p_r$ follows from
$\binom t2\ge t-1$ for every nonnegative integer $t$.

## Exact structure on $2r$ vertices

**Theorem.** Let $r\ge6$. If an induced target graph $H$ has $2r$
vertices and $\alpha(H)\le2$, then $H$ is the union of two disjoint
$K_r$'s, with a possibly empty matching between them.

Here too Section 3 of the third input gives a shorter proof of the
existing theorem. If $H$ contains a $K_r=A$, the preceding independent
triple argument makes $H-A$ another $K_r$. The local cap makes the
cross edges a matching.

Otherwise $L=\overline H$ is triangle-free with maximum degree at most
$r-1$. The cap gives $e(L)\ge(r-1)p_r(2r)=r(r-1)$, forcing $L$ to
be $(r-1)$-regular.

A nonbipartite triangle-free graph on $n$ vertices has minimum degree
at most $2n/5$. Indeed, take a shortest odd cycle $C$, of length
$q\ge5$. It has no chord. An outside vertex has at most two neighbors
on $C$: if there were at least three, their cyclic gaps are at least
two, and an odd gap has length at most $q-4$, giving a shorter odd
cycle through the outside vertex. Thus

$$
q\delta(L)\le\sum_{v\in C}d_L(v)\le2n.
$$

But $r-1>4r/5$ for $r\ge6$. Consequently $L$ is bipartite; one of
its sides has at least $r$ vertices and gives the excluded target
$K_r$. This contradiction proves the theorem. Both shorter proofs
were checked by the author and are author-recorded; no unretained
proof is used.

## Consequence for packing

For $r\ge6$, a target $K_r$-free inherited graph of independence number
at most two has at most $2r-1$ vertices. This replaces a finite terminal
classification by a uniform argument; higher independence layers remain.

## Sharpness below the equality boundary

**Proved; not a coloring counterexample.** For every $r\ge3$, there is
a $K_r$-free graph of order $2r-1$ and independence number two satisfying
every inherited upper cap. Thus the preceding $K_r$-free order bound
is sharp, and a $2r-1$-vertex residue cannot simply be assumed to contain
a full clique.

Section 7 of the
[fourth independent input](independent/growing_local_independence_range.md)
gives the following particularly simple example. Let $F$ be the independent-bag
blowup of $C_5$ with cyclic bag orders $(r-2,r-2,1,1,1)$, and put
$H=\overline F$. Since $F$ is triangle-free and has edges, $\alpha(H)=2$. An
independent set in $F$ meets at most two nonconsecutive bags. The two large bags
are consecutive, so $\omega(H)=\alpha(F)=r-1$.

Direct counting gives

$$
|F|=2r-1,\qquad \Delta(F)=r-1,\qquad e(F)=(r-1)^2+1,
$$

and hence

$$
\delta(H)=r-1,\qquad e(H)=r^2-r-1=D_r(2r-1)-1.
$$

The input checks this last total-edge cap. In fact, for any $W$ of
order $r\le m\le2r-1$, deleting the other vertices removes at most
$(r-1)(2r-1-m)$ edges of $F$. Therefore

$$
e(F[W])\ge(r-1)(m-r)+1\ge(r-1)p_r(m),
$$

which proves $e(H[W])\le D_r(m)$. For $m\le r$ the cap is trivial.
This verifies the full hereditary hypothesis without computation.

This family is also a special case of the odd-core structures in
[Three-row structure](three_row_structure.md). The
[tight local blocks](unit_deficit_propagation.md) give an even stronger
local realization for $r\ge4$: an actual $r$-coloring on $2r-1$ vertices
with target independence two, no target $K_r$, and target edge count
$D_r(2r-1)$. Neither construction is overloaded. Neither conflicts with
the equality theorem at $2r$ or the three-row theorem at $3r$.

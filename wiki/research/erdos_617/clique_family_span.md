---
name: research/erdos_617/clique_family_span
desc: Odd-clique inequalities follow from hereditary caps; a quasi-line branch and small-independence fractional obstructions are excluded.
tags: [graph-theory, proved, fractional-coloring, structure]
sources: []
created: 2026-09-22T07:15:00Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/clique_family_span

***

**Proved restrictions, not a resolution of E617.** Throughout $H$ is
$K_r$-free and satisfies $e(H[W])\le D_r(|W|)$ for every induced set.
No least-color budget is assumed.

## Odd families of cliques

For any $2t+1$ cliques $Q_1,\ldots,Q_{2t+1}$, let $Y$ consist of
vertices belonging to at least two of them. Then

$$
\boxed{|Y|\le rt.} \tag{1}
$$

For each $y\in Y$, choose two distinct clique memberships and make
an edge between those two indices in a loopless multigraph $F$.
This gives one root edge per vertex of $Y$, and
$L(F)\subseteq H[Y]$: two root edges sharing an index represent
adjacent vertices of that clique. The subgraph $L(F)$ remains
$K_r$-free and satisfies all upper caps. The
[budget-free line-graph span theorem](line_graph_obstruction.md) gives

$$
|Y|\le r\alpha(L(F))=r\nu(F)\le rt,
$$

proving (1). This lifting does not require an edge-clique cover of $H$.

## A verified quasi-line consequence

A graph is quasi-line when each neighborhood partitions into two cliques.
Eisenbrand, Oriolo, Stauffer, and Ventura, [*The Stable Set Polytope of
Quasi-Line Graphs*, Theorems 3--4, printed p.
7](https://www.iasi.cnr.it/~ventura/PaoloVenturaFiles/papers/EOSV06.pdf), record
the following structural and polyhedral results: a connected quasi-line graph is
fuzzy circular interval or a composition of fuzzy linear interval strips; the
stable-set polytope in the latter case has, besides the trivial inequalities,
only Edmonds inequalities. These have the form $\sum_{v\in Y}x_v\le t$ for the
odd clique families in (1). The precise statements and the definition of those
inequalities were checked in the primary paper. Its polyhedral theorem is an
invoked input, not reproved here.

The vector $x_v=1/r$ satisfies (1), nonnegativity, and every clique
inequality. Therefore, in the strip-composition branch,

$$
\frac1r\mathbf1\in\operatorname{STAB}(H),\qquad
\chi_f(H)\le r,\qquad |H|\le r\alpha(H).
$$

In particular a connected quasi-line graph that is not fuzzy circular
interval cannot be either overloaded core. No reduction of arbitrary
cores to this graph class, or exclusion of the circular branch, is
claimed.

## A weighted independence-two obstruction

If $C\ne\varnothing$ is a clique and $B$ is disjoint from and
complete to $C$, with $\alpha(H[B])\le2$, then

$$
\boxed{2|C|+|B|\le2r-2.} \tag{2}
$$

Put $c=|C|\le r-1$ and $R=r-c$. If (2) fails, retain $2R-1$
vertices of $B$. When $R=1$, any one extends $C$ to a $K_r$.
For $R\ge2$, complementary Mantel gives $e(H[B])\ge(R-1)^2$.
The difference between the resulting lower edge bound and the cap is

$$
\binom c2+c(2R-1)+(R-1)^2-D_r(r+R-1)
=(c-1)(R-1).
$$

This is positive for $c\ge2$. For $c=1$, equality forces the Mantel
extremizer: $B$ is a disjoint union of cliques of orders $R$ and
$R-1$. The first together with $C$ is a $K_r$, again impossible.

For $r\ge6$, a $K_r$-free inherited-cap graph $J$ with
$\alpha(J)\le2$ consequently satisfies

$$
\boxed{\chi_f(J)\le r-\tfrac12.} \tag{3}
$$

Here is a self-contained explanation of the fractional step. Put
$F=\overline J$. Since stable sets of $J$ have size at most two,
fractional coloring is fractional matching in $F$ plus singleton
coverage: $\chi_f(J)=|J|-\nu_f(F)=|J|-\tau_f(F)$, by linear
programming duality. A minimum fractional vertex cover can be chosen
half-integral. Indeed, on the coordinates strictly between zero and
one, a bipartite component of tight edge constraints admits alternating
perturbations; an odd cycle of tight constraints forces value $1/2$.
An extreme optimum thus has only values $0,1/2,1$.

Its zero set $C$ is independent in $F$, its one set can be taken as
exactly $N_F(C)$, and all other values are $1/2$. Any additional one
could be decreased to $1/2$. Conversely each such $C$ supplies a
feasible cover. Hence, writing
$B_C=\{v\notin C:v\text{ is complete to }C\text{ in }J\}$,

$$
\chi_f(J)=\max_{C\text{ clique in }J}
\left(|C|+\frac{|B_C|}{2}\right),
$$

including $C=\varnothing$. The [two-row theorem](two_row_structure.md)
gives $|J|\le2r-1$, controlling the empty case. Equation (2) bounds
all nonempty cases by $r-1$, proving (3).

In particular any claw-free $H$ under these hypotheses has

$$
\boxed{\Delta(H)\le2r-4,}
$$

because $\alpha(H[N(v)])\le2$ and (2) applies to
$C=\{v\}$, $B=N(v)$.

## Safe removal of mixed homogeneous clique pairs

Let $A,B$ be disjoint cliques, with every outside vertex complete or
anticomplete to each separately. If there are both cross edges and
cross nonedges, erase all $A$--$B$ edges. This preserves independence
number, and preserves claw-freeness or the quasi-line property when
present.

Any new independent set uses at most one vertex of each clique. If
it uses both, replace those two by a fixed old cross nonedge; all
outside adjacencies are identical. A new claw must have its center
outside $A\cup B$ and one leaf in each clique. The same replacement
would give an old claw. For an outside vertex adjacent to both cliques,
the fixed nonadjacent representatives lie in different parts of its
old two-clique neighborhood partition. Put all of $A$ into the first
part and all of $B$ into the second. Homogeneity preserves both
cliques. Neighborhoods centered inside $A\cup B$ only lose vertices.

Repeated removal preserves all hereditary upper caps and any edge
budget. It also preserves minimal-ratio conditions, since the global
independence number is unchanged and induced independence numbers
can only increase. This targeted operation avoids the unjustified
assumption that arbitrary independence-critical pruning preserves
claw-freeness.

## Remaining gaps

Odd-clique lifting handles only a specified quasi-line branch.
General quasi-line graphs have further clique-family inequalities;
the circular interval branch is not excluded. For general claw-free
strip decompositions, true-twin weights and the simultaneous marginal
constraints at attachment cliques remain uncontrolled. Complete and
anticomplete homogeneous pairs survive the pruning above. Local
fractional colorings from (3) do not automatically combine across
those attachments. No general core has been proved claw-free.

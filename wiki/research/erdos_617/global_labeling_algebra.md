---
name: research/erdos_617/global_labeling_algebra
desc: Exact labeling and third-moment identities, an obstruction to unconditional splitting, and affine-span facts that do not establish exchange connectivity.
tags: [graph-theory, proved, unsuccessful-approaches, algebra, topology]
sources:
  - erdos_gyarfas_1999_split_balanced_colorings_complete_graphs
created: 2026-09-22T13:15:22Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/global_labeling_algebra

***

**Status: exact reformulations and elementary lemmas, not a solution.**
This attempt deliberately set aside clique packing and private-row
completion. It investigated vertex labelings, global generating
functions, and reconfiguration of maximum independent sets. No universal
proof, counterexample, or unrestricted infinite family of positive
cases resulted.

## 1. Labeling energy and its limitation

For an edge coloring $c:E(K_n)\to[r]$ and a vertex labeling
$\sigma:V\to[r]$, put

$$
F(\sigma)=|\{uv:\sigma(u)=\sigma(v)=c(uv)\}|.
$$

A zero-energy labeling is exactly a partition into sets $V_i$
independent in their respective color graphs $G_i$. At
$n=r^2+1$, such a labeling would give an independent
$(r+1)$-set in some color by pigeonhole.

However, zero energy cannot be forced from the order alone. The construction in
[Erdos--Gyarfas, Proposition 1](../../../library/extremal_graph_theory/erdos_gyarfas_1999_split_balanced_colorings_complete_graphs/_index.md)
consists of two disjoint four-vertex red cycles, each with blue diagonals, and
all cross edges green. Its digest was read first and the construction in the
source was checked.

Each four-set requires a green-labeled vertex in a zero-energy
labeling. Without green labels, its red-labeled vertices form a
red-independent set of order at most two. If there are two, they
are a diagonal and the two remaining vertices form a blue edge;
if there are at most one, the at least three blue-labeled vertices
contain a blue edge. But green labels in both four-sets conflict
on a cross edge. Hence this coloring of $K_8$ is nonsplittable.
Appending two arbitrarily colored vertices preserves that obstruction
and gives a nonsplittable coloring of $K_{10}$.

This is not an E617 counterexample: its green graph already has
an independent four-set. It rules out a proof of zero energy from
$n=r^2+1$ alone, not a labeling argument that substantively uses
all the assumptions $\alpha(G_i)\le r$.

## 2. Exact partition-function expansions

Define the polynomial

$$
Z(t)=\sum_{\sigma:V\to[r]}t^{F(\sigma)}.
$$

For an edge $e=uv$, let $X_e(\sigma)$ indicate the event
$\sigma(u)=\sigma(v)=c(e)$. Expanding
$t^{F(\sigma)}=\prod_e(1+(t-1)X_e(\sigma))$ gives

$$
\boxed{
Z(t)=r^n\!
\sum_{\substack{A\subseteq E(K_n)\\
\text{each nontrivial component of }(V,A)\text{ is monochromatic}}}
(t-1)^{|A|}r^{-|V(A)|}.} \tag{1}
$$

Here $V(A)$ denotes the endpoints of the selected edges, and
$V(\varnothing)=\varnothing$. Selected events are consistent
precisely when all selected edges incident at a vertex have the
same color, equivalently when each nontrivial connected component
is monochromatic. In that case the labels on $V(A)$ are forced
and the other $n-|V(A)|$ labels are arbitrary. This proves (1).

For the multivariate independence polynomials

$$
I_i(\mathbf x)=\sum_{S\text{ independent in }G_i}\prod_{v\in S}x_v,
$$

one also has

$$
\boxed{Z(0)=\left[\prod_{v\in V}x_v\right]
\prod_{i=1}^r I_i(\mathbf x).} \tag{2}
$$

The coefficient selects exactly one occurrence of each vertex,
so it counts disjoint independent sets covering $V$, with their
colors specified. Under the counterexample assumptions, each
$I_i$ has degree at most $r$ and the product degree is at most
$r^2<n$. Thus the coefficient vanishes tautologically. No separate
positivity, nonvanishing, or cancellation estimate was obtained.

## 3. A conflict-graph formulation

Make a graph on $V\times[r]$. Join all pairs $(v,i),(v,j)$
with $i\ne j$, and join $(u,i),(v,i)$ precisely when $c(uv)=i$.
An independent transversal of the $n$ vertical $K_r$'s is
exactly a zero-energy labeling. Between two different vertical
parts there is exactly one edge.

At $n=r^2+1$ this graph has average degree $2r-1$: vertical
edges contribute $r-1$ and horizontal edges contribute
$(n-1)/r=r$. Under the counterexample assumptions its clique
number is at most $r$. Indeed, a clique meeting two vertical
parts must have one vertex in each and use a common label, so
corresponds to a monochromatic clique of the original coloring.

These facts are exact, but no independent-transversal theorem at
these parameters was proved. The nonsplittable example above
prevents silently assuming that the special one-edge-between-parts
condition alone supplies a transversal.

## 4. Global third-moment identities

Let $d_i(v)$ be the color degrees, let $t(G_i)$ count triangles,
and let $I_3(G_i)$ count independent three-vertex sets. Put

$$
S=\sum_{v,i}d_i(v)^2,\qquad
W=\sum_{v,i}\binom{d_i(v)}2,\qquad
T=\sum_i t(G_i).
$$

Inclusion-exclusion on the three possible edges of a triple gives

$$
I_3(G_i)=\binom n3-(n-2)e(G_i)
 +\sum_v\binom{d_i(v)}2-t(G_i).
$$

Summing over the edge partition yields

$$
\boxed{\sum_i I_3(G_i)=(r-3)\binom n3+W-T.} \tag{3}
$$

Also

$$
W=\frac{S-n(n-1)}2,\qquad
S\ge\frac{n(n-1)^2}{r}. \tag{4}
$$

The second inequality is Cauchy--Schwarz at each vertex.

Under $\omega(G_i)\le r$, each color neighborhood has clique
number at most $r-1$. Turan's theorem there gives

$$
3T=\sum_{v,i}e(G_i[N_i(v)])
\le\frac{r-2}{2(r-1)}S,
\qquad
\boxed{T\le\frac{r-2}{6(r-1)}S.} \tag{5}
$$

These are only degree and triangle estimates. No incompatible
bound on the independent-triple counts, and no contradiction
using the condition that independent $(r+1)$-sets are absent,
was derived from them. They are retained as exact identities,
not as evidence for either answer to E617.

## 5. Maximum-set exchange: affine span is not connectivity

For a graph $G$ with independence number $a$, its maximum-set
exchange graph has the maximum independent sets as vertices;
two are adjacent when one vertex is replaced by another.
Every such swap replaces adjacent vertices of $G$: otherwise
their union would be an independent $(a+1)$-set.

**Affine-span lemma.** If $G$ is connected and every edge is
independence-critical, the incidence vectors of all maximum
independent sets affinely span

$$
\{x\in\mathbb R^{V(G)}:\textstyle\sum_vx_v=a\}. \tag{6}
$$

For every critical edge $uv$, a witness supplies an independent
$(a-1)$-set $R$ anticomplete to both endpoints. The maximum
sets $R\cup\{u\}$ and $R\cup\{v\}$ have incidence-vector
difference $e_u-e_v$. Connectedness makes these differences
span $\mathbf1^\perp$, proving (6).

There is a precise componentwise version. For one component
$C$ of the exchange graph, let $D_C$ be the graph on $V(G)$
whose edges are the swaps used inside $C$, retaining isolated
vertices. Then

$$
\boxed{\dim\operatorname{aff}\{\mathbf1_I:I\in C\}
=|V(G)|-c(D_C),} \tag{7}
$$

where $c(D_C)$ counts components including isolates. Every swap
difference belongs to the affine difference space. Conversely,
an exchange path expresses any difference between members of
$C$ as a sum of swap differences. The span of edge-coordinate
differences of $D_C$ has the dimension in (7).

Exchange connectivity holds for $a\le2$. The case $a=1$ is
immediate. For $a=2$, the complement is maximal triangle-free,
by independence-criticality, and is connected: adding an edge
between distinct components would create no triangle. Maximum
independent sets of $G$ are its complement's edges, and their
exchange graph is the connected line graph of that complement.

For $a\ge3$, no proof of exchange connectivity was obtained.
Although every critical edge occurs in at least one $D_C$,
that does not prove the exchange components merge. A bounded
probe of 1,000 randomly generated saturated complements on at
most 16 vertices found no counterexample. This is not a
certificate or a theorem and is not used in any argument here.

## Precise remaining gaps

A proposed reconfiguration route would first need disjoint
color-$i$ independent sets of size $r$, one per color, leaving
one unassigned vertex. Such a partial cooperative partition was
not proved to exist. Even assuming it, no exchange argument was
found that forces an independent $(r+1)$-set or a zero-energy
labeling. General maximum-set exchange connectivity is also
unproved, and would not by itself settle these other gaps.

Possible further work on labeling cancellations or exchange
connectivity is provisional only. These formulations do not
replace the unresolved core conditions in the research index.

## Further checked obstructions to cooperative packing

Balance alone does not give disjoint maximum sets even at the sharp
order one below E617. On $\mathbb F_3^2$, color vertical pairs 1,
horizontal pairs 2, and both diagonal directions 3. All three
independence numbers equal three. A color-3 independent triple must
be an entire vertical or horizontal line: three pairwise
vertical-or-horizontal differences must share a coordinate.
Removing a vertical line leaves no color-1 independent triple, and
removing a horizontal line leaves no color-2 independent triple.
Thus this balanced $K_9$ has no cooperative partition into three
respective independent triples. Any one-hole packing theorem at
$r^2+1$ must use the extra vertex substantively.

There is also no two-way single-vertex exchange between occupied
maximum blocks. If $A_i,A_j$ are disjoint independent $r$-sets in
their respective colors, and $A_i-a+b$ remains independent for
$a\in A_i$, $b\in A_j$, maximality forces the edge $ab$ to have
color $i$. The reverse replacement forces it to have color $j$,
which is impossible. A hole $x$ can enter $A_i$ precisely when
$N_i(x)\cap A_i$ is a singleton, exchanging the hole with that
unique vertex. This does not prove existence of an initial packing
or a global augmentation mechanism.

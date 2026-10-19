---
name: research/erdos_644/topological_guards
desc: A rank-two path guard makes the nontransversal complex and intersection nerve contractible while the former has arbitrarily large deleted-square indices, even after conjunction-primality.
tags: [proved, limitations, topology, boolean-functions]
sources: []
created: 2026-09-23T02:56:00Z
updated: 2026-10-13T05:28:09Z
---


# research/erdos_644/topological_guards

***

The following construction limits approaches using ordinary homotopy or the
standard deleted-product and deleted-join indices. It does not settle either
assertion of Problem 644. The resulting family is neither transversal-critical
nor incidence-minimal.

Let $\mathcal H$ be a finite clutter of nonempty sets, on its support, with rank
at most $k$, property $P_7$, and transversal number $t\ge2$. Here $P_7$ concerns
subfamilies of at most seven edges. For arbitrarily large $n\equiv1\pmod3$,
there is a clutter $\mathcal Q$ with rank at most $k+2$, property $P_7$, and
transversal number $t$ such that:

- its nontransversal complex and ordinary intersection nerve are contractible;
- the free $\mathbb Z_2$-coindices of the deleted product and deleted join of
  its nontransversal complex are at least $\lfloor n/2\rfloor-2$;
- its monotone edge-containment function is conjunction-prime, and every ground
  vertex belongs to an edge.

If $\mathcal H$ is $k$-uniform, then $\mathcal Q$ is $(k+2)$-uniform.

## The path guard

Take $n\ge7$ with $n\equiv1\pmod3$ and $q=\lfloor n/2\rfloor\ge t$. On a
disjoint support, let $\mathcal G=P_n$ be the edge family of the path
$1,\ldots,n$. Choose $E_0\in\mathcal H$, put $e=\{n-1,n\}$, and define

$$
\mathcal Q=(\mathcal H\otimes\mathcal G)\setminus\{E_0\cup e\},
\qquad
\mathcal H\otimes\mathcal G=\{E\cup F:E\in\mathcal H,F\in\mathcal G\}.
$$

The one-deleted-product-edge lemma in
[Prime guard families](prime_guard_families.md) proves conjunction-primality.
Its hypotheses hold because $\tau(\mathcal H)=t\ge2$ and
$\tau(\mathcal G)=q\ge2$.

For completeness, the transversal calculation is elementary. Either projection
of a transversal of $\mathcal Q$ covers its factor, or its projections leave
exactly $E_0$ and $e$ uncovered. In the latter case its size is at least
$(t-1)+(q-1)\ge t$. A minimum $\mathcal H$-transversal covers $\mathcal Q$, so
$\tau(\mathcal Q)=t$. Local covers in the $\mathcal H$ coordinates give $P_7$.
Both factors have at least two edges, so the single deletion leaves every vertex
supported.

## Contractibility of the ordinary complexes

For a family $\mathcal F$ on $V$, write

$$
K(\mathcal F)=\bigcup_{E\in\mathcal F}2^{V\setminus E},
\qquad
X(\mathcal F)=\bigcup_{E\in\mathcal F}2^E.
$$

The intersection nerve of $\mathcal F$ is homotopy equivalent to
$X(\mathcal F)$: its covering simplices have intersections that are either
simplices or empty. All joins and unions below are simplicial. We use the
standard gluing fact that the union of two contractible subcomplexes with
nonempty intersection $C$ is homotopy equivalent to the suspension $\Sigma C$.

For $n\ge7$, direct decomposition at the last path edge gives

$$
K(P_n)=\bigl(n*K(P_{n-1})\bigr)\cup\Delta([n-2]).
$$

The intersection is

$$
C_n=K(P_{n-1})\big|_{[n-2]}
=\Delta([n-3])\cup\bigl((n-2)*K(P_{n-3})\bigr).
$$

The two pieces defining $C_n$ are contractible and intersect in $K(P_{n-3})$.
Consequently

$$
C_n\simeq\Sigma K(P_{n-3}),
\qquad K(P_n)\simeq\Sigma^2K(P_{n-3}).
$$

The facets of $K(P_4)$ are $34,14,12$, forming a path. Induction therefore
proves that $K(P_n)$ and $C_n$ are contractible for the chosen $n$.

Put $\mathcal H^-=\mathcal H\setminus\{E_0\}$. The deleted product row yields

$$
K(\mathcal Q)=
\bigl(K(\mathcal H)*[n*K(P_{n-1})]\bigr)
\cup\bigl(K(\mathcal H^-)*\Delta([n-2])\bigr).
$$

Both pieces are contractible. Since $K(\mathcal H^-)\subseteq K(\mathcal H)$,
their intersection is $K(\mathcal H^-)*C_n$, also contractible. Thus
$K(\mathcal Q)$ is contractible.

Similarly, viewing paths now as their edge-generated simplicial complexes,

$$
X(\mathcal Q)=
\bigl(X(\mathcal H)*P_{n-1}\bigr)
\cup\bigl(X(\mathcal H^-)*\Delta(\{n-1,n\})\bigr).
$$

Both pieces and their intersection $X(\mathcal H^-)*\{n-1\}$ are contractible.
Hence $X(\mathcal Q)$, and therefore the intersection nerve, is contractible.

## Explicit equivariant spheres

Despite this contractibility,

$$
K(\mathcal Q)[V(P_n)]=K(P_n).
$$

Indeed, every guard edge still occurs paired with an $\mathcal H$-edge different
from $E_0$. If $T$ is a minimum path transversal, then $|T|=q$ and

$$
K(P_n)[T]=\partial\Delta^{q-1}.
$$

Every proper subset of $T$ is a nontransversal, whereas $T$ is a transversal.

The centrally symmetric polyhedral sphere

$$
S=\{z\in\mathbb R^T:\ \sum_vz_v=0,\ \sum_v|z_v|=1\}
\cong S^{q-2}
$$

embeds equivariantly in the deleted join of $K(\mathcal Q)$ by its positive and
negative supports. Both supports are proper subsets of $T$. It also embeds in
the deleted product by

$$
z\longmapsto(2z^+,2z^-).
$$

The two images are barycentric points with disjoint supports, and antipodality
swaps them. Thus both coindices are at least $q-2$, and hence so are the
corresponding sphere-valued equivariant indices.

As $n$ grows, these indices are unbounded at unchanged rank $k+2$ and
transversal number $t$. No rank-dependent upper bound for these standard indices
follows from $P_7$, even with conjunction-primality. Ordinary contractibility
likewise cannot supply the required transversal bound.

## Low Shapley values and the criticality limitation

The construction also preserves vanishing maximum Shapley value along a sequence
of cores with that property, provided $n\to\infty$. For a path vertex $x$,
choose a matching of $m\ge\lfloor n/2\rfloor-3$ edges disjoint from its closed
neighborhood. At Bernoulli bias $p$, pivotality of $x$ requires a selected
neighbor and no completed matching edge. These events use disjoint coordinates,
giving

$$
I_x^{P_n}(p)\le2p(1-p^2)^m,
\qquad \phi_x(P_n)\le\int_0^1 2p(1-p^2)^m\,dp=\frac1{m+1}.
$$

Product-coordinate Shapley values do not exceed the corresponding factor values,
as shown in [Prime guard families](prime_guard_families.md). Deleting
$E_0\cup e$ can change the first pivotal coordinate only if this is the unique
product edge at the first winning prefix. Then $e$ is the first completed path
edge. A maximum matching containing $e$ has $q=\lfloor n/2\rfloor$ disjoint
pairs with exchangeable completion times, so this event has probability at most
$1/q$. Consequently

$$
\max_x\phi_x(\mathcal Q)
\le\max\{\max_x\phi_x(\mathcal H),O(1/n)\}+O(1/n).
$$


The family is not transversal-critical. Choose $E_1\ne E_0$ and $F_1\ne e$.
Deleting $E_1\cup F_1$ also leaves transversal number $t$: if neither projection
of a transversal covers its factor, the nonempty rectangle of uncovered factor
edges is contained in two diagonally opposite pairs, so is a singleton. The same
lower bound $(t-1)+(q-1)\ge t$ applies. Nor is the construction
incidence-minimal: deleting all guard incidences recovers the core, preserving
$P_7$ and $t$. It supplies no obstruction to an argument using an appropriately
normalized, facet-sensitive relative complex after simultaneous edge and
incidence minimization.

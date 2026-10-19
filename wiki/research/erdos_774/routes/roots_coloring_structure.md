---
name: research/erdos_774/routes/roots_coloring_structure
title: Root colorings, transversals, and symmetry
desc: Finite dissociated coloring of all roots is equivalent to one prime-fiber transversal; equivariant partitions have an exact exponential obstruction that does not cover arbitrary colorings.
tags: [E0774, proved, reduction, incomplete]
sources: []
created: 2026-09-18T00:49:00Z
updated: 2026-09-18T01:24:28Z
---


# Root colorings, transversals, and symmetry

***

The [prime-tensor extraction theorem](prime_tensor_extraction.md) proves the
local property for all roots of unity. This page makes the remaining global
coloring problem more concrete. None of the reductions below resolves it.

## Local extraction, fractional coloring, and the precise source gap

Let $\Psi(n)$ be the largest dissociated cardinality in $\mu_n$.
For any $F\subseteq\mu_n$ and a maximum dissociated set $I\subseteq\mu_n$,
rotation preserves dissociation and gives

$$
\frac1n\sum_{g\in\mu_n}|F\cap gI|
=\frac{|F|\Psi(n)}n.
$$

Thus the hereditary dissociation constant of $\mu_n$ is exactly
$\Psi(n)/n$: averaging proves the lower bound and taking
$F=\mu_n$ proves the upper bound. The weighted version is identical,
replacing cardinalities by sums of nonnegative vertex weights. Consequently
the fractional chromatic number of its signed-relation hypergraph is
$n/\Psi(n)$. For a direct proof, give each of the $n$ indexed
rotates of $I$ weight $1/\Psi(n)$, so every vertex is covered with
weight one; conversely summing the fractional covering constraints and using
the maximum class size proves the matching lower bound.

It follows that $\inf_n\Psi(n)/n>0$ is equivalent to proportional
dissociation of all roots. The prime extraction theorem proves this local
condition. The target is still **integral** chromatic growth; bounded
fractional chromatic number is not its substitute.

The primary 2006–2007 working-group contribution of Myriam Déchamps explicitly
separates these issues: Question 36 concerns $n/\Psi(n)$, Question 38
asks finite quasi-independent covering of all roots, and Question 39 asks
Sidonicity. The definitions and statements were checked on pp. 19–20 of
the [full primary document](https://www.renyi.hu/~revesz/OpenProblems.pdf).
This is a historical source check, not a claim about the present literature
status or publication priority of the result. It supplies no proof
of the missing coloring assertion.

### Relation to the odd-prime integer-block candidate

Let $Q=\sup_k\chi(E_k)$ for the odd-prime grids of the main argument.
Restriction gives $Q\leq\chi(\mu_\infty)$. Conversely, if $Q<\infty$,
every odd squarefree root set is a slice of a prefix grid and has a proper
$Q$-coloring. An even squarefree root set is the disjoint union of an
odd root set and its negative, so has a $2Q$-coloring using separate
palettes. The already proved prime-power coset separation extends that bound
to every $\mu_n$. A diagonal subsequence of colorings of $\mu_{j!}$
stabilizes the color of each root, yielding a global proper coloring; every
relation has finite support. Hence

$$
Q\leq\chi(\mu_\infty)\leq2Q\qquad(Q<\infty).
$$

Thus finite colorability of all roots and bounded coloring of the odd-prime
grids are equivalent. Full roots are used only for this reformulation:
their antipodal pairs are not passed directly to positive-integer encoding.

The new [profile-compression theorem](root_profile_compression.md) applies to
arbitrary putative colorings, without symmetry assumptions. It forces a summable
reciprocal loss when symbols having identical **global** color profiles are
merged. This excludes fixed-order bounded-state colorings, but it permits all
coordinate profiles to be distinct and hence does not give a contradiction.

## Equivalence with a dissociated transversal — proved

Write $G=\mu_\infty$ for all roots of unity, with dissociation always
referring to addition in $\mathbb C$. The following are equivalent:

1. $G$ has a finite dissociated partition.
2. For some prime $\ell$, there is a dissociated set containing exactly
   one representative of every multiplicative $\mu_\ell$-coset in $G$.

A proper $q$-coloring gives such a transversal for every prime $\ell>q$.
The cosets have finite size $\ell$; their quotient is infinite.

### Proof

Fix $\ell>q$, let $T$ consist of roots of order coprime to $\ell$,
and put $K=\mathbb Q(T)$. Restrict the coloring to classes
$C_1,\ldots,C_q$ of $T$. Choose distinct $a_c\in\mu_\ell$.
They are linearly independent over $K$: for every finite conductor
$m$ coprime to $\ell$, the cyclotomic degree formula gives
$[\mathbb Q(\zeta_{m\ell}):\mathbb Q(\zeta_m)]=\ell-1$, and
any $\ell-1$ distinct $\ell$-th roots form a rational basis.
Every hypothetical dependence over $K$ lies at such a finite stage.

Therefore $D_0=\bigcup_c a_c C_c$ is dissociated: a signed relation
splits first by these independent coefficients and then by each color class.
It meets each $\mu_\ell$-coset in $\mu_\ell T$ exactly once.

Choose representatives $r_\alpha\in\mu_{\ell^\infty}$ modulo
$\mu_\ell$. The spaces $r_\alpha K(\zeta_\ell)$ have direct sum.
For any finite collection, pass to a common $\ell^j$ level and a
finite coprime conductor $m$. There are $\ell^{j-1}$ cosets, and
the degree over $\mathbb Q(\zeta_{m\ell})$ is exactly
$\ell^{j-1}$; their spanning representatives are consequently a basis.

Thus $D=\bigcup_\alpha r_\alpha D_0$ is dissociated and is the desired
transversal in the entire $G$. This step is necessary: simply choosing an
unused prime does not handle its unbounded prime-power levels.

Conversely, a dissociated transversal gives the partition
$G=\bigsqcup_{a\in\mu_\ell}aD$, whose $\ell$ classes are
dissociated. This proves the equivalence.

**Exact remaining gap:** no argument here excludes dissociated
$\mu_\ell$-transversals for arbitrarily large primes $\ell$.
The checked $r(\mu_{105})=52$ gives only the finite bound
$\chi(\mu_{210})\geq5$: antipodal reorientation proves
$r(\mu_{210})=52$. It is not an unbounded obstruction.

### Exact condition on selector labels

For the coprime-order group $T$ above and any map
$f:T\to\mathbb Z/\ell\mathbb Z$, put
$C_a=f^{-1}(a)$ and $D_f=\{\zeta_\ell^{f(t)}t:t\in T\}$.
Then $D_f$ is dissociated exactly when all $C_a$ are dissociated
and

$$
\bigcap_{a=0}^{\ell-1}\Sigma(C_a)=\{0\}. \tag{*}
$$

Indeed a selector relation is $\sum_a\zeta_\ell^a u_a=0$, where
$u_a\in\Sigma(C_a)\subset K$. The sole $K$-linear relation
among these $\ell$ roots forces all $u_a$ equal. A common nonzero
value gives a nontrivial selector relation; a common zero value is harmless
exactly when every class is dissociated. Every representation has finite
support, so this criterion also applies to the infinite classes. It is the
same coefficient-sensitive intersection condition as the finite tensor
layer lemma, not just a condition excluding monochromatic regular polygons.

Regular-polygon cosets alone cannot force unbounded coloring. Write
$x\in\mathbb Q/\mathbb Z$ in its finite-support primary decomposition
$x=\sum_p x_p$, with $x_p\in[0,1)$, and color by the parity of the
number of coordinates in $[1/p,2/p)$. In every order-$p$ coset
exactly one point has that $p$-flag and the other flags are fixed.
Every nontrivial finite subgroup coset therefore has both colors. This is
not a dissociated coloring: the rest of the signed relations remain relevant.

## Equivariant partitions require exactly one color per divisor

If $n$ is squarefree with $k$ prime factors, the least number of
dissociated classes in a partition of $\mu_n$ **permuted by its Galois
group** is exactly $2^k$.

For the upper bound, partition by multiplicative order. The primitive
$d$-th roots, for squarefree $d$, form the tensor product of the
primitive-prime bases and are rationally independent.

For the lower bound write the Galois group as
$\mathcal G=\prod_{p\mid n}\mathcal G_p$, acting also on the palette.
Fix a transitive palette orbit $O$, and let $a$ be the product of
primes whose coordinate group acts nontrivially on $O$. If primitive
$d$-th roots map to $O$, then $a\mid d$. Indeed the stabilizer
of a primitive $d$-th root includes every coordinate outside $d$.
Those coordinates fix its color and hence all of $O$, since
$\mathcal G$ is abelian and acts transitively on $O$.

Write $d=ab$. All coordinate groups in $b$ act trivially on $O$,
so the color map on primitive $d$-th roots is independent of the
primitive-$b$ coordinate. Its remaining equivariant map on primitive
$a$-th roots is determined by one color in $O$.

If more than $|O|$ orders map to $O$, two distinct orders $ab,ac$
give the same such map. Fix a primitive $a$-th root $u$. The two
disjoint sets $u\operatorname{Prim}(b)$ and
$u\operatorname{Prim}(c)$ are monochromatic in the same color, and
their sums are $\mu(b)u$, $\mu(c)u$, with both Möbius values
equal to $\pm1$. Explicitly, the forbidden signed relation is

$$
\mu(c)\sum_{x\in u\operatorname{Prim}(b)}x
-\mu(b)\sum_{y\in u\operatorname{Prim}(c)}y=0.
$$

Thus at most $|O|$ orders feed this orbit. Summing over palette orbits
shows that at least the $2^k$ divisors' worth of colors are required.

In particular any finite dissociated partition of all roots, **if it exists**,
must have infinite Galois orbit. Otherwise its common refinement with its
finitely many Galois translates would be a finite equivariant dissociated
partition, contradicting the finite theorem for arbitrarily large $k$.

There is no justification for assuming a general coloring is equivariant
or has finite orbit. Compactness or averaging alone does not give that
assumption. Therefore this exponential bound is **not** a lower bound for
unrestricted dissociated coloring.

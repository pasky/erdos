---
name: research/erdos_774/routes/fixed_height_focusing
title: Fixed-height chromatic growth suffices for full dissociation
desc: Profile focusing works at one fixed coefficient height with unbounded chromatic number; the proved palette-dependent height theorem does not supply that quantifier.
tags: [E0774, proved, reduction, incomplete]
sources: []
created: 2026-09-18T02:38:00Z
updated: 2026-09-18T17:37:54Z
---


# Fixed-height chromatic growth suffices for full dissociation

***

## Standing

The
[piecewise-syndetic reformulation](recurrent_high_height_roots.md) is
equivalent to the fixed-height premise below. That page also constructs an
ordinary idempotent containing a dissociated root set, with infinite
rational coloring number in every member. Thus rational dependence in all
members, even with idempotence, does not replace one common finite height.

This is a positive, elementary focusing reduction for the exact gap in the
[main argument](../proof_sketch.md). It does **not** establish its hypothesis.
Unlike a bare monochromatic-rectangle assertion, it explicitly pays for the
whole-profile palette and for every excluded conductor prime.

Let
$$
G=\bigoplus_{p\text{ odd prime}}\mu_p
$$
be the multiplicative group of odd squarefree-order complex roots. Additive
relations always refer to their values in $\mathbb C$. For $h\geq1$, write
$\chi_h(X)$ for the least number of classes with no nonzero integer relation
having every coefficient in $[-h,h]$. Thus $\chi_1$ is the dissociated coloring
number. This is a bound on **coefficient magnitude**, not the fixed-order notion
of $h$-freeness of
[Nešetřil–Rödl–Sales](../../../../library/integer_sequences/nesetril_2024_pisier_type_theorems/_index.md).

## Theorem

If $\chi_h(G)=\infty$ for **one fixed finite** $h$, then
$\chi_1(G)=\infty$. Consequently
$$
\chi_1(G)<\infty
\quad\Longleftrightarrow\quad
\chi_h(G)<\infty\text{ for every finite }h.
\tag{1}
$$

The forward implication is special to this multiplicatively closed root
family and the focusing argument below; it is not asserted for arbitrary
integer sets. In fact, for each fixed finite $h$, finiteness of
$\chi_1(G)$ and of $\chi_h(G)$ are equivalent.

### Finite witnesses and conductor tails

For a finite set $S$ of odd primes, put
$T_S=\bigoplus_{p\notin S,\ p\text{ odd}}\mu_p$. If $T_S$ had
a finite $h$-independent coloring, using separate palettes on its finitely
many multiplicative cosets would color $G$: multiplication by a nonzero
root preserves every integer relation. Therefore
$$
\chi_h(G)=\infty\quad\Longrightarrow\quad
\chi_h(T_S)=\infty\quad\text{for every finite }S.
\tag{2}
$$

An infinite chromatic number has finite witnesses. Indeed, if every finite
subset of a countable set had a proper $q$-coloring, take colorings of
nested finite exhaustions and successively stabilize each vertex color along
infinite subsequences. The resulting coloring avoids every forbidden relation,
because its support is finite. Apply the contrapositive for each $q$.

### Focusing induction with a fixed height

Assume $\chi_h(G)=\infty$. We prove the following statement simultaneously
for every finite $S$, every palette size $q$, and every $r\geq1$:

> Every $q$-coloring of $T_S$ contains finite height-$h$ dependent
> sets $X_1,\ldots,X_r$ in pairwise coprime conductor groups, disjoint
> from $S$, whose full product $X_1\cdots X_r$ is monochromatic.

For $r=1$, use (2). Suppose the statement holds for $r-1$, with **all**
finite palettes. Choose a finite $F\subset T_S$ with $\chi_h(F)>q$,
and let $J$ be its conductor-prime set. Given $f:T_S\to[q]$, color
$T_{S\cup J}$ by the complete finite profiles
$$
y\longmapsto (f(xy))_{x\in F}\in[q]^F.
$$
There are at most $q^{|F|}$ profile colors. The induction hypothesis at
that palette supplies $r-1$ conductor-disjoint height-$h$ dependent
sets whose product $Y$ has one profile $g:F\to[q]$.
Since $\chi_h(F)>q$, one color class of $g$ contains a nonzero
height-$h$ relation. Take its support as $X_1$. Then
$f(xy)$ is one fixed color for every $x\in X_1$, $y\in Y$.
The conductors of $X_1$ and all the other factors are coprime by construction.
This completes the induction without any bound on $|F|$ or the profile
palette: the hypothesis permits every finite palette at the **same** height.

For $h\geq2$, take $r=h$ and apply the proved
[Hall/determinant flattening lemma](bounded_height_flattening.md). It gives a
nonzero monochromatic ternary relation. This holds for every $q$, so
$\chi_1(G)=\infty$. The case $h=1$ is immediate. Finally
$\chi_h\geq\chi_1$, proving the other direction of (1).

## Exact unresolved quantifier

The previously proved bounded-height result has the form
$$
\forall q\ \exists h=h(q)\quad \chi_h(G)>q,
\qquad h(q)=\lceil e^{3q}\rceil\text{ is sufficient}.
\tag{3}
$$
The focusing theorem instead needs
$$
\exists h<\infty\ \forall q\quad\chi_h(G)>q.
\tag{4}
$$
There is no exchange of these quantifiers. Finite numbers $\chi_h(G)$
growing with $h$ satisfy (3) without satisfying (4). In particular,
applying (3) at $q^{|F|}$ changes the height and invalidates the fixed-height
induction.

A proof of (4), even for $h=2$, would be a genuine route to completing
the required counterexample: the theorem gives unbounded ternary
coloring on finite odd-prime grids, and the already proved uniform extraction,
exact integer encoding, and separated-block assembly then apply. No such
fixed height is currently known in this package.

## Finite quantitative formulation

If finite conductor-disjoint factors $F_i$, $n_i=|F_i|$, satisfy
$$
\chi_h(F_i)>q^{\,n_1\cdots n_{i-1}},
\tag{5}
$$
with empty product one, every $q$-coloring of their product has a
monochromatic product of height-$h$ dependent subsets. Start with the
last factor, color it by all prefix profiles, and select a dependent profile
class. The common profile is a coloring of the shorter prefix; repeat.
For $h$ factors, determinant flattening applies.

Conditionally on $\chi_h(G)=\infty$, put
$\kappa_h(t)=\min\{k:\chi_h(E_k)>t\}$, and let $N_k=|E_k|$.
Define $k_0=0$, $N_0=1$, and
$$
k_i=\kappa_h\bigl(N_{k_{i-1}}q^{N_{k_{i-1}}}\bigr).
$$
These indices increase: $\chi_h(E_k)\leq N_k$ excludes earlier ones.
The consecutive prime blocks $F_i$ satisfy (5), since coloring their
$N_{k_{i-1}}$ prefix slices separately gives
$\chi_h(E_{k_i})\leq N_{k_{i-1}}\chi_h(F_i)$.
Thus $\chi_1(E_{k_h})>q$. This is a bound in terms of an **unproved
finite witness function**, not a new numerical chromatic estimate.

## A conditional idempotent formulation

This formulation records a second rigorous focusing mechanism; no existence
or minimality theorem for ultrafilters is used. Let $\mathcal U$ be an
ultrafilter on $G$, with
$R_B=\{x:x^{-1}B\in\mathcal U\}$, and suppose it is idempotent,
meaning $B\in\mathcal U$ if and only if $R_B\in\mathcal U$.

**Proposition.** If one finite $h$ works so that every member of
$\mathcal U$ contains a height-$h$ dependence, every member contains
a ternary dependence. Consequently, if $\mathcal U$ contains a
dissociated set, it contains nested $h$-independent sets for all finite
$h$.

For $A\in\mathcal U$, set $A^*=A\cap R_A$. It belongs to
$\mathcal U$; for $x\in A^*$, both $x^{-1}A$ and
$x^{-1}R_A=R_{x^{-1}A}$ belong to $\mathcal U$, so
$x^{-1}A^*\in\mathcal U$. Every finite-prime tail $T_S$ also
belongs to $\mathcal U$: the ultrafilter selects a coset $aT_S$
in the finite quotient, and $R_{aT_S}=T_S$; apply idempotence.

Construct $h$ factors inductively. If $P$ is the finite set of all
nonempty products taking at most one point from the preceding factors, and
$S$ contains their conductor primes, choose the next dependent support in
$$
T_S\cap A^*\cap\bigcap_{s\in P}s^{-1}A^*\in\mathcal U.
$$
The invariant $P\subset A^*$ persists. All conductors are disjoint,
and the full product lies in $A^*$. Determinant flattening proves the
proposition. Its contrapositive supplies an $h$-independent member for
each $h$; intersect these successively with the dissociated member to
make them nested.

For $h=1$, the proposition is immediate from its hypothesis; the
determinant step is needed only for $h\geq2$.

### Covering information does not supply uniform height

Call $FB$ thick if, for every finite $E\subset G$, some translate
$tE$ is contained in $FB$. If this holds with finite $F$,
$k=|F|$, and $B$ is $h$-independent, assigning each
$x\in E$ an $f\in F$ with $f^{-1}tx\in B$ properly
$h$-colors $E$ with $k$ colors. The existing small-column
inequality, on all odd-prime prefixes and with $P\to\infty$, gives
$$
\log(h+1)\leq2k.
$$
The explicit earlier height $\lceil e^{3k}\rceil$ therefore forces
a dependence in a set with such a $k$-element thick-cover witness.

But these cover sizes cannot be uniformly bounded inside an idempotent
ultrafilter, even after fixing one member $A$. For finite $S$,
$A\cap T_S\in\mathcal U$, and any finite $F$ with
$F(A\cap T_S)$ thick has
$$
|F|\geq[G:T_S]=\prod_{p\in S}p.
$$
A thick set projects onto the entire finite quotient, while the displayed
product projects into the image of $F$. This only disproves a uniform
bound on these covering witnesses; it does not independently prove that
minimal relation heights grow. The missing exchange is still from
member-dependent heights to one height for every member.

The elementary finite focusing theorem and its finite quantitative form
received an independent internal audit. All new proofs here are algebraic or
finite-color compactness arguments, with no numerical experiment.

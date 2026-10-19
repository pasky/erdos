---
name: research/dissociated_covering_attack/layer_race
title: Twisted layers and the layer-count race
desc: "Coordinate-permutation twists of a proper coloring give layered colorings of the next odd-root grid; robust layering preserves the root-span fraction exactly and three colors win the layer-count race of the roots, but the exact first moment of common values diverges along the odd-prime grids, so deciding the odd-root grids this way needs a rigidity argument for common values of large complexity."
tags: [E0774, tensor, coloring, heuristic, incomplete]
sources: []
created: 2026-10-15T17:59:57Z
updated: 2026-10-15T17:59:57Z
---

# Twisted layers and the layer-count race

***

## Standing

This page studies the missing theorem (4) of the
[inherited main argument](../erdos_774/proof_sketch.md), unbounded
dissociated coloring of the odd-prime grids $S_3\otimes S_5\otimes\cdots$,
from the positive side: it builds colorings of each grid from colorings of
the previous one and asks when that can fail. Everything here is
author-recorded, by Plasma AI; nothing is independently reviewed.

- **Proved here.** Lemma 1 (coordinate permutations act on signed spans),
  Lemma 2 (exact root survival under random twists), Lemma 3 (robust layering
  preserves the root-span fraction exactly), Corollary 4 (the root-coverage
  parameter is constant along robust twisted steps), Lemma 5 (localization),
  Proposition 6 (annealed transfer of survival bounds), the exact
  first-moment identity (O) and Lemma 7 (the first moment diverges) of
  Section 6, Lemma 8 (certificates by pairs of layers stay below the rank)
  of Section 9, and Lemma 9 (clustered survival sets are excluded
  together), Lemma 10 (the arc class has exactly two coordinate symmetries)
  and Lemma 11 (layered classes are rigid) of Section 10. Corollary 4 uses
  the inherited nonjump recurrence for one inequality.
- **Exact finite data.** The checks of Section 5, the numerical instances
  of Lemma 7 and the survival sets of Section 10 for arc and layered classes
  at the conductor 105, by
  exact arithmetic in the
  [evidence checker](evidence/_index.md), with the solver-only observations
  of Section 5 labeled as such.
- **Heuristic.** The race model of Section 6 and the far-regime count of
  Section 8 are models with stated assumptions, not arguments. Lemma 7
  proves that the model's first-moment bound fails at all sufficiently
  large odd-prime orders for any fixed palette. At order 15015 the
  expectation already exceeds $2^{2479}$ for the tested palettes
  $q=2,3,4$, carried by twist families of tiny probability. What survives is the race of the roots themselves, which
  three colors win at every prime. Three colors for every odd squarefree
  order, the open claim of Section 7, therefore rests on the root race,
  the rank bound through seven primes and small-order data, not on a valid
  first-moment bound.

No statement here changes the standing of Problem 774, of
[[theory/integer_sequences/L123_odd_root_arc_colorings/_index|L123]] or of
[[theory/integer_sequences/L124_flat_cyclotomic_degree_ratio/_index|L124]].
Nothing here depends on L124: the colorings studied are not arc colorings.

## 1. Setting and the layer criterion

Let $M>1$ be odd and squarefree, $M=p_1\cdots p_k$, and identify
$\mathbb Z/M$ with the grid $\prod_i\mathbb Z/p_i$ by reduction, so that
$\mu_M=\{\zeta_M^e\}$ becomes a grid. For $C\subseteq\mu_M$ write

$$
\Sigma(C)=\Bigl\{\sum_{x\in C}\epsilon_xx:\epsilon_x\in\{-1,0,1\}\Bigr\}
\subseteq\mathbb Z[\zeta_M],
$$

so $C$ is dissociated exactly when no nonzero signed sum vanishes. For a
prime $p\nmid M$ write every element of $\mu_{Mp}$ uniquely as $y\zeta_p^t$
with $y\in\mu_M$ and $t\in\mathbb Z/p$. The
[layer criterion](../erdos_774/routes/tensor_coloring.md) states that
$D=\bigcup_t\zeta_p^tC_t$ is dissociated if and only if every layer $C_t$
is dissociated and $\bigcap_t\Sigma(C_t)=\{0\}$; a common nonzero value is
a nonzero relation of $D$. The same page defines the separation parameter
$\tau_q(\mu_M)$, the least number of proper $q$-colorings of $\mu_M$ whose
color classes have trivial signed-span intersection for every color, and
proves $\chi(\mu_{Mp})\le q$ exactly when $p\ge\tau_q(\mu_M)$.

Two quantities of a set $C\subseteq\mu_M$ organize what follows:

$$
\kappa(C)=\frac{|\Sigma(C)\cap\mu_M|}{M},\qquad
\alpha(C)=1-\kappa(C).
$$

The **root-span fraction** $\kappa(C)$ counts the roots of unity that $C$
represents, its own elements included. The unspanned fraction $\alpha(C)$
is $|R(C)|/M$ for the set $R(C)=\mu_M\setminus\Sigma(C)$ of the
[root-coverage page](../erdos_774/routes/tensor_holes.md), whose parameter
$\alpha_q(\mu_M)$ is the largest average of $\alpha$ over the classes of a
proper $q$-coloring, and which proves $\tau_q\ge\lceil1/\alpha_q\rceil$.

## 2. Coordinate permutations act on signed spans

Let $G_M=\prod_i\mathrm{Sym}(\mathbb Z/p_i)$ act on $\mu_M$ through the grid.
[[../library/analysis/ramsey_graham_2006_permutation_extension_planar_quasi_independent_subsets_roots_unity/theorem_1_2_1|Ramsey and Graham, Theorem 1.2.1]]
prove that these are exactly the permutations of $\mu_M$ preserving the
quasi-independent sets. The twisting below needs slightly more: an action on
signed spans.

**Lemma 1.** Every $g\in G_M$ extends to an additive automorphism $\hat g$
of $\mathbb Z[\zeta_M]$ that agrees with $g$ on $\mu_M$. Consequently
$\hat g(\Sigma(C))=\Sigma(gC)$ for every $C\subseteq\mu_M$, $gC$ is
dissociated exactly when $C$ is, and $\kappa(gC)=\kappa(C)$.

*Proof.* For $f:\mu_M\to\mathbb Z$ the sum $\sum_xf(x)x$ vanishes exactly
when all its Galois conjugates vanish, that is, when the Fourier transform
of $f$ on $\mathbb Z/M$ vanishes at every character of exact order $M$. By
the Chinese remainder theorem these characters are the products of
nontrivial characters of the factors, so the condition says that $f$ has no
component in the tensor product of the mean-zero spaces of the factors:

$$
\prod_{i=1}^k(I-E_i)f=0,
$$

where $E_i$ averages along the $i$-th grid coordinate. Each $E_i$ commutes
with every coordinatewise permutation, so $f\mapsto f\circ g^{-1}$ maps the
integer relation lattice $\Lambda\subset\mathbb Z^{\mu_M}$ onto itself. The
evaluation map identifies $\mathbb Z^{\mu_M}/\Lambda$ with
$\mathbb Z[\zeta_M]$, because the powers of $\zeta_M$ generate it
additively, so the permutation of the coordinates of $\mathbb Z^{\mu_M}$
descends to an automorphism $\hat g$ with $\hat g(x)=g(x)$ for $x\in\mu_M$.
Signed sums over $C$ map to signed sums over $gC$, and
$\hat g(\mu_M)=\mu_M$ gives the last claim. $\square$

The cyclotomic symmetries, multiplication by a root and the Galois
automorphisms, are the coordinatewise affine maps, a small subgroup of
$G_M$.

## 3. Twisted layerings

Fix a proper $q$-coloring $f$ of $\mu_M$, twists $g_t\in G_M$ and color
permutations $\sigma_t$ of $[q]$, for $t\in\mathbb Z/p$. The **twisted
layering** is the coloring of $\mu_{Mp}$ given by

$$
F(y\zeta_p^t)=\sigma_t\bigl(f(g_ty)\bigr).
$$

Its layer $t$ is the proper coloring $\sigma_t\circ f\circ g_t$ of $\mu_M$
(Lemma 1), and its color-$c$ class has layers
$C_{t,c}=g_t^{-1}f^{-1}(\sigma_t^{-1}c)$. By the layer criterion and
Lemma 1, $F$ is proper exactly when, for every color $c$,

$$
\bigcap_{t\in\mathbb Z/p}\hat g_t^{-1}\Bigl(\Sigma\bigl(f^{-1}(\sigma_t^{-1}c)\bigr)\Bigr)
=\{0\}.
$$

A twisted layering is **robust** when this holds after deleting any one
layer. Arc colorings and Bohr-cell colorings are layerings too, but their layers are offset arc or Bohr colorings
rather than coordinate twists of one coloring; twisting replaces the
cyclotomic geometry by the whole group $G_M$.

## 4. Root survival and preservation of the root-span fraction

**Lemma 2 (exact root survival).** Let $g_1,\ldots,g_p$ be independent and
uniform in $G_M$, and let $C_1,\ldots,C_p\subseteq\mu_M$. The expected
number of roots $y\in\mu_M$ with $\hat g_ty\in\Sigma(C_t)$ for every $t$ is
exactly $M\prod_t\kappa(C_t)$, and the same holds for the values $-y$.

*Proof.* $\hat g_ty=g_ty$ is a uniform root, independently in $t$, because
$G_M$ acts transitively on the grid; and $\Sigma(C)=-\Sigma(C)$. $\square$

**Lemma 3 (robust layering preserves the root-span fraction).** Let
$C_0,\ldots,C_{p-1}\subseteq\mu_M$ be dissociated, and suppose
$\bigcap_{i\ne j}\Sigma(C_i)=\{0\}$ for every $j$. Then
$D=\bigcup_t\zeta_p^tC_t$ is dissociated and

$$
\kappa(D)=\frac1p\sum_{t}\kappa(C_t).
$$

*Proof.* $D$ is dissociated by the layer criterion. A root
$y\zeta_p^j\in\mu_{Mp}$ lies in $\Sigma(D)$ exactly when
$\sum_t\zeta_p^tu_t=y\zeta_p^j$ for some $u_t\in\Sigma(C_t)$. Since the only
relation among the $\zeta_p^t$ over $\mathbb Q(\zeta_M)$ is their vanishing
sum, this means $u_t=w$ for $t\ne j$ and $u_j=w+y$ for one common $w$; this
is the exact membership rule (4) of the root-coverage page. Here $w$ lies
in $\bigcap_{i\ne j}\Sigma(C_i)=\{0\}$, so $y\zeta_p^j\in\Sigma(D)$ exactly
when $y\in\Sigma(C_j)$. Counting over $j$ gives
$|\Sigma(D)\cap\mu_{Mp}|=\sum_j|\Sigma(C_j)\cap\mu_M|$. $\square$

**Corollary 4.** Let $f$ attain $\alpha_q(\mu_M)$, and suppose some twisted
layering of $f$ with $p$ layers is robust for every color. Then
$\chi(\mu_{Mp})\le q$ and $\alpha_q(\mu_{Mp})=\alpha_q(\mu_M)$.

*Proof.* Lemma 1 gives $\kappa(gC)=\kappa(C)$, and the color permutations
permute the classes of $f$, so Lemma 3 gives, for the classes $D_c$ of the
layering,
$\sum_c|R(D_c)|=p\sum_c|R(f^{-1}c)|$, whence
$\alpha_q(\mu_{Mp})\ge\alpha_q(\mu_M)$. The reverse inequality is the
inherited nonjump recurrence (3) of the root-coverage page,
$\alpha_q(B\otimes S_m)\le\alpha_q(B)$, which is author-recorded there.
$\square$

The root-coverage page proposed amplifying $\tau_q\ge1/\alpha_q$ by forcing
$\alpha_q$ to decay. Corollary 4 shows where that mechanism cannot act:
$\alpha_q$ cannot decrease across a prime at which some coloring attaining
$\alpha_q$ has a robust twisted layering, so any decay, and with it any
chromatic jump forced through $\tau_q\ge1/\alpha_q$, happens at primes
where every such coloring fails to layer robustly.

Call a twisted layering **$s$-robust** if
$\bigcap_{t\notin T}\Sigma(C_{t,c})=\{0\}$ for every color $c$ and every
set $T$ of at most $s$ layers; robust means 1-robust. The layers outside
such a $T$ are themselves a family of proper $q$-colorings with trivial
intersections, so an $s$-robust layering with $p$ layers has
$p-s\ge\tau_q(\mu_M)$.

**Lemma 5 (localization).** Let $D=\bigcup_t\zeta_p^tC_t$ with dissociated
layers, and let $T\subsetneq\mathbb Z/p$ satisfy
$\bigcap_{t\notin T}\Sigma(C_t)=\{0\}$. Then for all
$Y_t\in\mathbb Z[\zeta_M]$, $t\in T$,

$$
\sum_{t\in T}\zeta_p^tY_t\in\Sigma(D)
\iff Y_t\in\Sigma(C_t)\ \text{for every }t\in T.
$$

*Proof.* A representation $\sum_t\zeta_p^tu_t$ with $u_t\in\Sigma(C_t)$
differs from the given sum by a vanishing combination of the $\zeta_p^t$,
so $u_t=Y_t+w$ on $T$ and $u_t=w$ off $T$ for one common $w$, and
$w\in\bigcap_{t\notin T}\Sigma(C_t)=\{0\}$. $\square$

Every value $Y\in\mathbb Z[\zeta_{Mp}]$ has decompositions
$Y=\sum_t\zeta_p^tY_t$ with a zero component, since subtracting one
component from all of them changes nothing. Write $s(Y)$ for the
complexity of a value, the least support of a signed representation by
roots. Concatenating component representations shows
$s(Y)\le\sum_ts(Y_t)$ for every decomposition, and splitting a shortest
representation by layers gives a decomposition with equality, supported on
at most $s(Y)$ layers.

**Proposition 6 (annealed transfer).** Let $f$ be a proper $q$-coloring of
$\mu_M$ with classes $C^{(j)}$, put
$\Lambda(X)=\max_j\Pr_g[\hat gX\in\Sigma(C^{(j)})]$ for $X\in\mathbb Z[\zeta_M]$
and $g$ uniform in $G_M$, and let the twists $g_t$ of a twisted layering be
independent and uniform. Let $h=(h',\pi)$ be uniform in
$G_{Mp}=G_M\times\mathrm{Sym}(\mathbb Z/p)$ and independent of them, and
let $Y=\sum_{t\in T}\zeta_p^tY_t$ with $|T|\le s$. If $E$ is the event that
the layering is $s$-robust, then for every color $c$ of the layering

$$
\Pr\bigl[\hat hY\in\Sigma(D_c)\ \text{and}\ E\bigr]\le\prod_{t\in T}\Lambda(Y_t).
$$

*Proof.* $\hat hY=\sum_{t\in T}\zeta_p^{\pi(t)}\hat h'Y_t$. On $E$, Lemma 5
reduces membership to
$\hat g_{\pi(t)}\hat h'Y_t\in\Sigma(C^{(j_t)})$ for every $t\in T$, with
$j_t$ fixed by $c$ and the color permutation of layer $\pi(t)$. Given $\pi$
and $h'$, the elements $g_{\pi(t)}h'$, $t\in T$, are independent and
uniform in $G_M$ because the $g_{\pi(t)}$ are. $\square$

So if the twisted copies of one coloring satisfy $\Lambda(X)\le\kappa^{s(X)}$
for every value of complexity at most $s$, the next grid inherits
$\Pr[\hat hY\in\Sigma(D_c)]\le\kappa^{s(Y)}+\Pr[E^c]$ for every value of
complexity at most $s$, on average over the twists. This is the exact form
in which the race model of Section 6 transmits itself from one conductor to
the next; by Lemma 7 the hypothesis can hold only for $s$ up to about
$\log|G_M|/\log(1/\kappa)$. It is annealed: the first-moment count at the following prime
needs the $p'$-th moment of the quenched probability, and two twisted
copies of $Y$ that use two common layers are correlated through the ratio
of their twists.

## 5. Exact small cases

The [evidence checker](evidence/_index.md) verifies the first three items
by exact integer arithmetic.

- **$\mu_{15}$, two colors.** $\mu_{15}$ has 446 nonzero signed relations
  with 127 supports, of which 98 are minimal, of sizes 3, 5, 6, 7, 8 and 9;
  its largest dissociated sets have $8=\varphi(15)$ elements. Its 1440
  proper 2-colorings (as unordered partitions) all have classes of sizes 7
  and 8, and form four orbits of 360 under $G_{15}$, of order 720. Every
  8-element class spans every root, so $\kappa=1$. The 7-element class
  leaves 6 roots outside its signed span in 360 colorings and 4 roots in
  the other 1080.
- **Nine layers suffice.** Nine labeled proper 2-colorings of $\mu_{15}$,
  eight from one $G_{15}$-orbit and one from another, have trivial
  signed-span intersection for both colors. Hence
  $\tau_2(S_3\otimes S_5)\le9$, sharpening the inherited range
  $8\le\tau_2\le10$ of the
  [tensor-layer test](../erdos_774/evidence/tensor_layers/_index.md); the
  primes this decides are unchanged: $\chi(\mu_{15p})=2$ for every prime
  $p\ge11$.
- **Arc classes below the rank threshold span nothing outside.** For
  $M\in\{105,165,195,1155,15015,255255\}$ and $q\in\{3,4\}$, an arc of
  $\lceil M/q\rceil\le\varphi(M)$ consecutive roots is part of a power basis,
  and no root outside it lies in its signed span, so
  $\kappa=\lceil M/q\rceil/M$, equal to $1/3$ when $q=3$.
  This is the smallest root-span fraction possible for an arc of that size. The largest
  power-basis coordinate of a root of unity grows from 2 at 105 to 545 at
  15015 and 116762 at 255255.
- **Signed pairs of roots behave like independent points.** For the arc
  class of $q=3$ at $M=105$ and $M=1155$ we computed, for each agreement
  pattern of a pair of distinct roots and each sign, the probability that a
  uniform coordinate twist sends the signed pair into the class's signed
  span; coordinate twists act transitively on the pairs with a given
  pattern. The only representations other than the obvious one are the
  identities $z+z\omega=-z\omega^2$ on cosets of $\mu_3$, which make such a
  pair a single root in disguise, surviving with probability exactly
  $1/3$. Every other pattern survives with probability between $0$ and
  $0.1333$, against $\kappa^2=0.1111$: assumption 1 of the race model holds
  for complexity two at these conductors, up to a factor $1.2$.
- **Signed triples.** At $M=105$, exactly, and at $M=1155$, by a Monte
  Carlo estimate with 1500 samples per orbit, the orbits of signed triples
  whose values do not visibly reduce through cosets of $\mu_3$ or $\mu_5$
  survive a random twist with probability at most $4/45\approx0.089$ at
  105 and about $0.088$ at 1155, against $\kappa^3=0.037$. The excess sits
  on small orbits of triples confined to a few coordinates: at 105 every
  such orbit needs fewer layers than the roots, as (O) asks
  ($\log|O|/\log(1/\lambda_O)$ at most $3.4$ against $4.2$ for the roots),
  and at 1155 the estimates give at most $5.6$ against $6.4$.
- **Two arcs fail at 165 and 195, two colors do not.** $\Phi_{165}$ and
  $\Phi_{195}$ have height two while $(1-x)\Phi_{165}$ and $(1-x)\Phi_{195}$
  are flat ([inherited table](../erdos_774/evidence/short_arc_root_relations.md)),
  so $D(165)=81$ and $D(195)=97$, and L123 shows that two arcs are not
  proper there. The nine-layer family nevertheless gives
  $\chi(\mu_{165})=\chi(\mu_{195})=2$. Arc colorings are therefore not optimal
  beyond the rank threshold.
- **Solver observations, not certificates.** A direct exact-coefficient
  integer program found no signed relation in either class of the
  resulting colorings of $\mu_{165}$ and $\mu_{195}$, while it found one in
  an arc of $\lceil N/2\rceil$ roots and in the layering with all layers
  equal. In that coloring of $\mu_{165}$ the 82-element class represents at
  least 71 of the 83 roots outside it (each found representation was
  checked), and the solver found none for the other 12; the 83-element
  class represents at least 70 of 82, with none found for 12. Such classes
  are nearly maximal, and twisted layerings of this one coloring need at
  least $\lceil165/12\rceil=14$ layers if these reported representation
  counts hold (the counting bound of the root-coverage page), one more
  than the prime 13 supplies at
  $3\cdot5\cdot11\cdot13$. The reported 12 unrepresented roots
  of each class lie on only 2 of the 11 values of the 11-coordinate,
  suggesting a further obstruction to efficient coverage by twists. A set-cover program
  over 20000 random candidate twists found no 17 that leave every root
  unspanned in some layer for both colors, and over 6000 candidates the
  least such family within that sample has 22 twists. These sampled
  searches give no global obstruction at 17 or 19 layers. The reported
  22-twist family would suffice for root exclusion with 23 layers,
  but its solver output is not retained here as an exact certificate.

These cases fit one pattern: twisted layering struggles where the colors are
**tight**, that is, where $q$ classes can cover $\mu_M$ only by being nearly
maximal dissociated sets, because nearly maximal classes span almost every
root and slow the race below. This is the case for $q=2$ at $M=15$, where
every 8-element class is a largest dissociated set spanning all roots and
the coloring number jumps to 3 at 105, and for the coloring of $\mu_{165}$
above, whose classes leave only 12 roots unspanned.

## 6. The race model and its first moment

This section is a model, not an argument, except for the identity (O) and
Lemma 7, which are proved.

For one color, let the layers come from a class $C$ of a proper $q$-coloring
of $\mu_M$ under independent uniform twists, and write $\kappa=\kappa(C)$.
A nonzero value $F$ is common when $\hat g_tF\in\Sigma(C)$ for every layer.
Since $\hat gF$ is uniform on the $G_M$-orbit $O$ of $F$, it survives one
layer with probability $\lambda_O=|O\cap\Sigma(C)|/|O|$, independently, and
the expected number of nonzero common values is exactly

$$
\sum_{O}|O|\,\lambda_O^{\,p}, \tag{O}
$$

the sum over the $G_M$-orbits of nonzero values. Orbit $O$ is killed in
expectation once $p$ exceeds $p_O=\log|O|/\log(1/\lambda_O)$. The roots
form an orbit of size $M$ with $\lambda=\kappa$ (Lemma 2), so they need
$p>\log M/\log(1/\kappa)$. Classify a value $F$ by its complexity $s(F)$,
the least support of a signed representation by roots of $\mu_M$. The model
assumes:

1. the roots are the binding orbits: a value of complexity $s$ survives
   one random layer with probability at most about $\kappa^s$, or more
   generally its orbit needs no more layers than the roots do (exact for
   $s=1$; for $s\ge2$ it treats the points of a representation as nearly
   independent);
2. at most $\binom Ms2^s$ values have complexity $s$.

Under these assumptions the expected number of common nonzero values would
be at most about

$$
q\sum_{s\ge1}\binom Ms2^s\kappa^{ps}\le q\bigl(e^{2M\kappa^p}-1\bigr),
$$

dominated by single roots and small once

$$
p\log\frac1\kappa>\log(2qM). \tag{R}
$$

The term of the single roots is exact: by Lemma 2 the roots and their
negatives contribute $2M\kappa^p$ per color, so (R) is exactly the condition
that the roots lose the race in expectation. The rest of the bound is
false at large conductors.

**Lemma 7 (the first moment diverges).** Let $C\subseteq\mu_M$ be
dissociated and let $g_1,\ldots,g_p$, with $p\ge2$, be independent and
uniform in $G_M$. Then

$$
\mathbb E\,\#\{F\ne0:\hat g_tF\in\Sigma(C)\ \text{for every}\ t\}
\ \ge\ \frac{2^{|C|}-1}{|G_M|^{\,p-1}}.
$$

*Proof.* By (O) in the form of Section 8, the expectation is
$\sum_{0\ne F\in\Sigma(C)}\lambda(F)^{p-1}$. For $F\in\Sigma(C)$ the orbit
$O$ of $F$ meets $\Sigma(C)$ at least in $F$, so
$\lambda(F)\ge1/|O|\ge1/|G_M|$; and $|\Sigma(C)|\ge2^{|C|}$, because the
subset sums of a dissociated set are distinct. $\square$

One event carries the bound: with probability $|G_M|^{1-p}$ all twists are
equal, and then every element of $\Sigma(C)$ is common. For the odd-prime
grids $|G_{N_k}|=\prod_{i\le k}p_i!$, so $\log|G_{N_k}|$ grows like
$p_k^2/2$, while the largest class of a proper $q$-coloring has at least
$N_k/q=e^{(1+o(1))p_k}/q$ elements. Hence for every fixed $q$ the right
side of Lemma 7 tends to infinity along the grids. Exactly, with
$p=p_{k+1}$: a class of $\lceil M/2\rceil$ elements gives an expectation
above $2^{12}$ at $M=1155$, and classes of $\lceil M/q\rceil$ elements give
expectations above $2^{2479}$ at $M=15015$ for $q=2,3,4$; at $M=1155$ the
bound says nothing for $q=3$. Three consequences:

- Assumption 1 fails for every $F\in\Sigma(C)$ whose complexity exceeds
  $\log|G_M|/\log(1/\kappa)$, since such $F$ have
  $\lambda(F)\ge1/|G_M|>\kappa^{s(F)}$. At most
  $\sum_{j\le s}\binom Mj2^j$ values have complexity at most $s$, so most of
  $\Sigma(C)$ is of this kind once $|C|$ is large.
- For any fixed palette, the unconditioned union bound over individual
  common values cannot certify properness at all sufficiently large
  odd-prime orders. The exact bound already exceeds one at $M=15015$
  for the tested palettes $q=2,3,4$.
- Lemma 7 does not show that twisted layerings fail. The expectation is
  carried by twist families of tiny probability, such as families of equal
  twists; it shows only that the first moment cannot certify properness.

**What survives.** The race of the roots is exact, and so is any first-moment
count restricted to values of complexity at most $s_0$, where the
degenerate events of Lemma 7 contribute at most
$\sum_{j\le s_0}\binom Mj2^j\,|G_M|^{1-p}$, negligible while
$s_0\log(2eM)$ stays well below $(p-1)\log|G_M|$, an allowance of order
$(\log M)^2$ for the odd-prime grids. A proof of properness along this
route therefore splits in two: the first moment over values of complexity
at most $s_0$, which the model's assumptions address, and a **rigidity**
statement, that outside an event of small probability the twists have no
common value of complexity above $s_0$. The second part cannot come from
a union bound over values; Section 7 states it.

**Primes.** For the odd-prime grids take $M=N_k=3\cdot5\cdots p_k$ and
$p=p_{k+1}$, so $\log N_k=\theta(p_k)-\log2$ with Chebyshev's function
$\theta$. Since $\theta(x)\sim x$ and $p_{k+1}>p_k$, (R) holds for every
large $k$ when $\kappa<e^{-1}$, up to a factor $1+o(1)$ in the exponent.
With $\kappa=1/3$ the margin is

$$
p_{k+1}\log3-\log(6N_k)\ge(\log3-1.01624)\,p_k-\log3,
$$

by the explicit bound $\theta(x)<1.01624\,x$ for $x>0$ of Rosser and
Schoenfeld (1962). The right side grows linearly and is positive for
$p_k\ge17$; direct computation shows that the margin itself is positive
for every $p_k\ge3$. So the expected numbers of surviving roots are
summable over $k$; by Lemma 7 the full first moment is not. Three arcs are
proper by the rank bound through the prime 19, with $\kappa=1/3$ exactly
(Section 5, computed through $255255$), and their roots lose the race at
23 and at every later prime; whether twisted layerings of them stay proper
depends on the rigidity statement. Two colors lose even the root race for
every large $k$, since $\log2<1$, consistent with $\chi(\mu_{105})=3$.

**Other side schedules.** For simplex tensors with sides $q_j=Aj\log j$ the
same computation gives $\log M_j\sim j\log j$ and $q_j\sim A\log M_j$, so
(R) holds eventually when $\kappa<e^{-1/A}$. The inherited extraction loss
$Q/(2q_j^2)$ of the [tensor extraction theorem](../erdos_774/routes/tensor_extraction.md)
has $\log Q\sim\sum_{i<j}(\log q_i)/q_i\sim(\log j)/A$, so it is summable
only for $A\ge1$. For every schedule that the inherited extraction method
covers, roughly $e^{1/A}+1$ colors win the root race; the primes sit at
$A=1$. The root race therefore does not distinguish the side schedules,
and Lemma 7 applies to all of them.

**Where the model can fail.**

- *Tightness.* If every proper $q$-coloring of some $\mu_{N_k}$ has nearly
  maximal classes, $\kappa$ is close to 1 and (R) fails; this is how the
  small jumps happen. The model needs $q$ to exceed the fractional
  coloring number $N_k/\Psi(N_k)$ with room to spare. L21 bounds that
  fractional number uniformly, but its constant is not explicit.
- *Values with many short representations.* Inflations of short relations
  of subconductors, and other structured values, can have survival
  probabilities far above $\kappa^s$. For arc classes, the fiber geometry
  removes the most obvious ones: every coset of $\mu_3$ meets an arc of
  length $N/3$ exactly once, and coordinate twists map such cosets to such
  cosets.
- *Correlations* between the classes of the base coloring.

## 7. Consequences for the attack

- **The open claim.** $\chi(\mu_N)\le3$ for every odd squarefree $N$, hence
  $\chi(\mu_\infty)\le6$ by the inherited reduction, a positive answer to
  Déchamps's Question 38, and (4) false. It is recorded as the open claim
  [[theory/integer_sequences/L210_odd_root_three_colorings/_index|L210]],
  which states exactly this bound. Three colors win the root race at every
  prime, but by Lemma 7 that is the only part of the first-moment count
  that holds, so the claim is a conjecture supported by the root race, the
  rank bound through seven primes and small-order data. It is independent
  of L124: two arcs already fail at 165 while two colors succeed.
- **What a proof of (4) must do.** For every palette $q$ it must find a
  prime at which no family of proper $q$-colorings of the previous grid,
  twisted or not, has trivial signed-span intersections; by Corollary 4,
  if the jump is to come from decay of the root coverage, that prime must
  defeat robust twisted layerings of the colorings attaining $\alpha_q$.
  Since the roots lose their race, it needs tightness at infinitely many
  conductors for every fixed palette, or common values of complexity at
  least two that survive typical twist families. Lemma 7 does not supply
  the latter: it exhibits common values only on twist families of tiny
  probability.
- **What a proof of the open claim needs.** Two parts, with a threshold
  $s_0$ inside the allowance of Section 6. First, for values of complexity
  at most $s_0$, a bound of the form
  $\Pr_g[\hat gF\in\Sigma(C)]\le\kappa^{c\,s(F)}$, uniform in the conductor,
  for the classes $C$ produced by robust twisted layerings, together with
  a count of the relevant orbits. With the crude count in assumption 2
  and $p\sim\log M$, the exponent must satisfy
  $c\log(1/\kappa)>1$; an unspecified $c>0$ is insufficient. The error
  probabilities from this estimate and the rigidity estimate must sum to
  less than one over all colors and all required robustness tests.
  Lemma 3 already transfers $\kappa$ itself exactly, and Section 5
  supports the bound for complexity two and three at small conductors. By Lemma 7 no such bound can hold for every $F$: it
  fails for each $F\in\Sigma(C)$ of complexity above
  $\log|G_M|/(c\log(1/\kappa))$. Second, **rigidity**: outside an event of
  small probability, a family of $p$ independent uniform twists has no
  common value of complexity above $s_0$. The exceptional event must
  contain the near-coincident families behind Lemma 7, and the statement
  has to explain how a value can have signed representations inside many
  twisted copies of one class, which no count over values does. Lemma 9 of
  Section 10 reduces it to a property of a single class: the survival sets
  of its values of large complexity, apart from few orbits, must be covered
  by fewer than $p$ translates of a small set of twists (fewer than $p/q$
  if the color permutations distribute the classes over the layers).
- **Tests that can falsify the model.** $\tau_2(\mu_{165})$, which decides
  $\chi(\mu_{3\cdot5\cdot11\cdot13})$; the root-span fraction of other
  proper 2-colorings of $\mu_{165}$; survival of values of complexity three
  and more for arc classes; and $\kappa$ of arc classes at
  $4849845=3\cdot5\cdots19$, the last conductor where three arcs are below
  the rank threshold.

## 8. Shape of the missing estimate

Write $\lambda(F)=\lambda_O$ for the orbit $O$ of $F$. Since
$|O|\lambda_O=|O\cap\Sigma(C)|$, the identity (O) can be rewritten as a
sum over the class's own signed sums,

$$
\mathbb E\,\#\{\text{nonzero common values}\}
=\sum_{0\ne F\in\Sigma(C)}\lambda(F)^{p-1},
$$

and since $\lambda(F)\ge1/|G_M|$ on $\Sigma(C)$ the right side is at least
$(|\Sigma(C)|-1)/|G_M|^{p-1}$, which is Lemma 7. No signed sum of $C$ has
an orbit of which $\Sigma(C)$ occupies a fraction below $1/|G_M|$, so the
estimate can only concern values of small complexity, as Section 7 states.
For those, since $\hat gF\in\Sigma(C)$ exactly when some signed
representation $R$ of $F$ has $g(\operatorname{supp}R)\subseteq C$,

$$
\lambda(F)\le\sum_{R}\pi(\operatorname{supp}R),\qquad
\pi(S)=\Pr_g[gS\subseteq C],
$$

the sum running over all signed representations of $F$. For an arc class
the natural survival $\pi(S)$ trades off against the orbit size of $S$: a
support confined to few coordinate values has a small orbit, and each new
coordinate value placed last in a coordinate of a prime $r$ must land in a
set of about $r/3$ of the $r$ residues. For large complexity the count of
representations is not the obstacle. The far-regime model of the
[angular-coloring page](../erdos_774/routes/angular_colorings.md) gives a
typical value about $A(\alpha)^t$ representations of support $t=\alpha M$,
with $A(\alpha)=2\exp\bigl((H(\alpha)-e^{-\gamma})/\alpha\bigr)\le2.66$ for
the binary entropy $H$ in nats, below the factor $3^t$; but natural
survival does not pay $3^{-t}$ once $3^t$ exceeds $|G_M|$. The
coordinate-permutation group has only $\prod_ip_i!=e^{O((\log M)^2)}$
elements while $|\Sigma(C)|$ is exponential in $M$, so a single
representation inside $C$ already gives $\lambda(F)\ge1/|G_M|$, and the
large-complexity part must come from the rigidity statement of Section 7.

## 9. Certificates by pairs of layers stay below the rank

The layer criterion certifies dissociation recursively. For odd squarefree
$N$ and a prime $p\mid N$, write each $S\subseteq\mu_N$ as
$S=\bigcup_{t\in\mathbb Z/p}\zeta_p^tS_t$ with $S_t\subseteq\mu_{N/p}$. Call
$S$ **pair-certified** if either $N$ is prime and $S\ne\mu_N$, or for some
prime $p\mid N$ every layer $S_t$ is pair-certified and either some layer is
empty or some two layers $S_a,S_b$ with $a\ne b$ are disjoint and
$S_a\cup S_b$ is pair-certified. The prime may change from step to step.

**Lemma 8.** Every pair-certified $S\subseteq\mu_N$ is dissociated and has at
most $\varphi(N)$ elements.

*Proof.* Induction on the number of prime factors of $N$. For $N$ prime the
only nonzero signed relations of $\mu_N$ are the sum of all its elements
and its negative, so $S\ne\mu_N$ is dissociated and $|S|\le N-1=\varphi(N)$.
Otherwise the layers are dissociated by induction. If $S_a$ and $S_b$ are
disjoint with dissociated union, a common value $w=u_a=u_b$ with
$u_a\in\Sigma(S_a)$ and $u_b\in\Sigma(S_b)$ gives the signed relation
$u_a-u_b=0$ of $S_a\cup S_b$, so $w=0$; an empty layer has
$\Sigma(S_t)=\{0\}$. Either way $\bigcap_t\Sigma(S_t)=\{0\}$, and $S$ is
dissociated by the layer criterion. For the size,
$|S|\le(p-2)\varphi(N/p)+|S_a\cup S_b|\le(p-1)\varphi(N/p)=\varphi(N)$, and
an empty layer gives the same bound. $\square$

The two simplest ways of making the common-value intersection trivial, an
empty layer or two layers with dissociated union, never certify a set
beyond the rank, whichever primes are used. A proper $q$-coloring with
$q<N/\varphi(N)$ has a class larger than $\varphi(N)$. Since two dissociated
sets have trivially intersecting signed spans exactly when they are
disjoint with dissociated union, any recursive certification of such a
class must, at some step, show that three or more signed spans intersect
trivially although no two of them do. Coloring beyond the rank is in this
sense a higher-order phenomenon: the nine-layer family of Section 5 shrinks
the intersection only gradually (447 values remain after two layers), and
twisted layerings rely on intersections over many layers. This is also why
the rigidity statement of Section 7 concerns many twisted copies at once.

## 10. Clustered survival sets

Lemma 7 says that a union bound over values fails; the following lemma
shows how values can be excluded together instead. For a class $C$ and a
nonzero value $F$ write

$$
T(F)=\{g\in G_M:\hat gF\in\Sigma(C)\},
$$

the **survival set** of $F$, so that $\lambda(F)=|T(F)|/|G_M|$ and $F$ is
common to the layers of a twisted layering of $C$ exactly when every twist
lies in $T(F)$. Fix a set $\mathcal N\subseteq G_M$ containing the identity
and call $F$ **$m$-clustered** if $T(F)$ is covered by at most $m$ left
translates $h\mathcal N$.

**Lemma 9.** Let $g_1,\ldots,g_p$ be independent and uniform in $G_M$ and
$m<p$. The probability that some $m$-clustered value is common to all $p$
layers is at most $\binom p2|\mathcal N^{-1}\mathcal N|/|G_M|$.

*Proof.* If an $m$-clustered $F$ is common, the $p$ twists lie in $T(F)$,
which is covered by $m<p$ translates of $\mathcal N$, so two of them,
$g_s$ and $g_t$ with $s\ne t$, lie in one translate and
$g_s^{-1}g_t\in\mathcal N^{-1}\mathcal N$. For $s\ne t$ the element
$g_s^{-1}g_t$ is uniform on $G_M$; take the union over the
$\binom p2$ pairs. $\square$

The bound does not sum over values, and it absorbs the degenerate events
of Lemma 7, in which twists coincide. A random twisted layering is
therefore proper with probability at least $1-\varepsilon$ as soon as, for
some $\mathcal N$ with $\binom p2|\mathcal N^{-1}\mathcal N|\le
\varepsilon|G_M|/2$ and some $m<p$, the first moment of the common values
that are not $m$-clustered, summed over the classes, is at most
$\varepsilon/2$. This is the case where every color permutation $\sigma_t$
of Section 3 is the identity, so that each color uses twisted copies of
one class; if the color permutations distribute the $q$ classes evenly
over the layers, the same argument applies with $m<p/q$ clusters per
class. This replaces
the rigidity statement of Section 7 by a property of a single class: its
unclustered values must be few enough for a first moment.

Which values are unclustered depends on their representations, since
$T(F)$ is the union, over the signed representations $R$ of $F$, of the
sets of twists carrying $\operatorname{supp}R$ into $C$ with matching
signs. In the following list the descriptions of $T(F)$ are exact and the
counts are heuristic.

- *Roots and short values.* A root $y$ has $|T(y)|=\kappa|G_M|$, spread over
  the whole group, and values of small complexity are similar; they are the
  first-moment part, exact for the roots by Lemma 2.
- *Thin supports.* If a representation of $F$ lies in a box
  $\prod_iA_i$ with small sides, $T(F)$ is a union of left cosets of the
  large group $\prod_i\mathrm{Sym}(\mathbb Z/p_i\setminus A_i)$, which
  fixes the box pointwise, so $F$ is not clustered for any small
  $\mathcal N$; such values fall into comparatively few orbits, and the
  first moment is the tool for them.
- *A unique representation.* If $F$ has a single signed representation,
  with support $S$, then $T(F)=\{g:gS\subseteq C\}$ up to sign
  compatibility. A maximal family of elements of $T(F)$ with pairwise
  $h_a^{-1}h_b\notin\mathcal N^{-1}\mathcal N$ covers $T(F)$ by its
  translates of $\mathcal N^{-1}\mathcal N$, so $F$ fails to be
  $m$-clustered for $\mathcal N^{-1}\mathcal N$ only if $S$ lies in $m+1$
  twisted copies $h_0^{-1}C,\ldots,h_m^{-1}C$ of the class with such
  pairwise far twists. For
  twisted copies that intersect like independent sets of density $1/q$,
  $m+1$ copies share about $Mq^{-m-1}$ points, fewer than the complexity
  threshold once $m+1$ exceeds about $\log_q M$; that is below $p$ exactly
  in the regime (R) where the roots lose their race.
- *Many representations.* The open case is a value of large complexity
  whose representations land in many pairwise far copies of $C$. Their
  differences are integer relations with coefficients in
  $\{-2,-1,0,1,2\}$, and need not be ternary relations. Suppose that $C$ meets every line of
  direction $p$ in at most $\lceil p/q\rceil$ points, as twisted arc
  classes do, and that $F$ has a representation inside $C$. A twist maps
  lines onto lines, so the twisted representation also meets every line in
  at most $\lceil p/q\rceil$ points, and the only relations supported on one
  line are the multiples of its indicator: changing the representation
  along a single line leaves at least $p-\lceil p/q\rceil>\lceil p/q\rceil$
  points of that line in the new support when $q\ge3$, too many for $C$. So the
  relations that carry a twisted representation back into $C$ involve at
  least two lines; longer relations are not controlled. At the conductor
  105 the relations that carry a twisted image back into the arc class lie
  on two or three grid lines: crosses and stars built from the identities
  $\sum_{x\in\ell\setminus P}x=-\sum_{x\in P}x$ for a line $\ell$ and a
  set $P$ of its points.

The single-class property to prove is therefore: for the classes of the
colorings being layered, a set $\mathcal N$ of twists with
$|\mathcal N^{-1}\mathcal N|\le|G_M|/p^3$, such that every value of
complexity above $s_0$ that is not in a few orbits of thin or short values
has its survival set covered by fewer than $p$ translates of $\mathcal N$.
That threshold is for layerings that keep each color on twisted copies of
one class, with every color permutation $\sigma_t$ the identity; if the
color permutations distribute the classes evenly over the layers, it is
$p/q$.

The set $\mathcal N$ cannot consist only of twists that move few points.
For the arc class $C=\{\zeta^e:0\le e<M/3\}$, every value supported on
the initial arc $\{\zeta^e:0\le e<M/(3m)\}$ survives each Galois
automorphism $\zeta\mapsto\zeta^u$ with $u\le m$ a unit modulo $M$,
because $ue<M/3$ there; these automorphisms move almost every point, and
the values have complexity up to about $M/(3m)$, far above $s_0$ when
$m\approx p$. The cyclotomic symmetries $\zeta^e\mapsto\zeta^{ue+d}$ are
the coordinatewise affine maps, a subgroup of $G_M$ of order $M\varphi(M)$,
so the natural candidate is that subgroup combined with twists that move
few points: a permutation of $\mathbb Z/r$ fixing all but $\eta r$
points is one of at most $\binom r{\eta r}(\eta r)!\le r^{\eta r}$ such
permutations, against $r!$ in all, so both parts are vanishing fractions of
$G_M$. Families of twists whose effects on the arc parameter form an
arithmetic progression keep large common parts of the arc class, and the
Galois automorphisms are the basic example; whether the twists of each
coordinate in such a family must be affine is part of the open question.
This intersection property is open; nothing on this page proves it for any
class beyond the rank.

The arc colorings sit at the clustered extreme. Write
$\zeta_{Mp}=\zeta_M^{\alpha}\zeta_p^{\beta}$ with $\alpha p+\beta M=1$, so
that $\zeta_{Mp}^e=\zeta_M^{\alpha e}\zeta_p^{\beta e}$. The exponents
$e<Mp/q$ with $\beta e\equiv t\pmod p$ form a progression of difference
$p$, and $\alpha p\equiv1\pmod M$, so layer $t$ of the arc coloring of
$\mu_{Mp}$ is an arc of consecutive roots of $\mu_M$, of length about
$M/q$. The arc coloring is therefore the layering of the arc coloring of
$\mu_M$ whose twists are rotations, a subgroup of order $M$, and Lemma 9
says nothing about it; its properness is decided by the cyclotomic
criterion of L123 instead. That two arcs fail at 165 while twisted
layerings with spread-out twists succeed is consistent with this.

At the other extreme, the support of a value is the whole arc class, and
there the clustering holds exactly.

**Lemma 10 (the arc has two coordinate symmetries).** Let $M$ be odd and
squarefree and $A=\{\zeta_M^e:0\le e<L\}$ with $2\le L\le M-2$. For a
prime $p\mid M$ put $K=M/p$ and write $L=aK+b$ with $0\le b<K$. Suppose
that for every prime $p\ge5$ dividing $M$ either $b\ge p$ and
$2\le a+1\le p-2$, or $K-b\ge p$ and $2\le a\le p-2$. Then the
coordinate permutations $g$ with $gA=A$ are exactly the identity and the
reflection $\zeta^e\mapsto\zeta^{L-1-e}$. For $L=\lceil M/3\rceil$ the
hypothesis holds when $M/5\ge7$ if $5\mid M$ and $M/p\ge2p$ for every
prime $p\ge7$ dividing $M$, in particular for $M=3\cdot5\cdots p_k$ with
$k\ge3$.

*Proof.* Identify $\mu_M$ with $\mathbb Z/M$ by exponents. Fix a prime
$p\mid M$ and let $w$ be the inverse of $K$ modulo $p$. A line of direction
$p$ is a coset $c+K\mathbb Z/M$ with $0\le c<K$; its point $c+tK$ has
$p$-coordinate $v\equiv c+tK$, so $t\equiv w(v-c)\pmod p$. In the
rescaled coordinate $v'=wv$ the points of the line inside $A$, those with
$c+tK<L$, therefore form the arc $[wc,wc+n_c)$ of $\mathbb Z/p$, with
$n_c=a+1$ for $c<b$ and $n_c=a$ for $b\le c<K$. Since $p$ consecutive
values of $c$ give every rotation $wc$, the hypothesis supplies a length
$\lambda$ with $2\le\lambda\le p-2$ such that every arc of length
$\lambda$ is the trace of $A$ on some line. A coordinate permutation $g$
maps lines of direction $p$ onto lines of direction $p$, acting on their
$p$-coordinates by one permutation, which in rescaled coordinates is a
permutation $G$ of $\mathbb Z/p$. If $gA=A$, then $G$ maps every arc of
length $\lambda$ onto an arc of length $\lambda$. Passing to complements
if $\lambda>p/2$, two arcs of length $\lambda\le p/2$ share
$\lambda-1\ge1$ points exactly when their starting points differ by
$\pm1$, so the starting points transform by an automorphism
$r\mapsto\pm r+c$ of the $p$-cycle, and the point $r$, the difference of
the arcs starting at $r$ and $r+1$, goes to $\pm r+c'$. Hence $g$ acts on
the $p$-coordinate by $v\mapsto\pm v+d_p$; for $p=3$ every permutation has
this form. So $g$ is $e\mapsto ue+d$ on $\mathbb Z/M$ with $u^2\equiv1$,
and $uA+d=A$. If $L<M/2$, this map sends $A\cap(A+1)$, of size $L-1$, onto
$A\cap(A+u)$, of size $\max(0,L-\min(u,M-u))$ for the representative
$0\le u<M$, so $u\equiv\pm1$; if $L>M/2$ the same argument applies to the
complement of $A$, an interval of length $M-L\ge2$. Finally $d=0$ when
$u=1$ and $d=L-1$ when $u=-1$. For $L=\lceil M/3\rceil$: at $p=5$, $a=1$
and $b=\lceil2K/3\rceil\ge5$ once $K\ge7$; at $p\ge7$, both $a$ and $a+1$
lie in $[2,p-2]$ and $\max(b,K-b)\ge K/2\ge p$. $\square$

So a signed sum over the whole class survives, with its own support,
exactly two twists, both affine. Lemma 10 concerns this natural survival
only; a value can also survive a twist that carries its support off the
class, through another signed representation.

The [evidence checker](evidence/_index.md) computes survival sets at
$M=105$ for the arc class of 35 roots exhaustively over all $3628800$
twists. The sums of the whole class, with all signs $+1$ and with
alternating signs, survive exactly the identity and the reflection, with
no other survivor. Twelve seeded signed sums on 20, 22 and 24 points of the
class have survival sets meeting at most eight of the 720 left cosets of
the affine group, fewer than 11, the next prime, which is what Lemma 9
needs for the step to 1155. Four seeded sums on 10 points meet 29 to 415
cosets, and among ten seeded sums on 17 points one meets 15 cosets and one
survives two twists that move its support off the class, each through a
relation on two grid lines. In these samples a
survival set meeting 11 or more cosets occurs only for sums on at most 17
points, inside the first-moment allowance of Section 6 for $p=11$, about
23 points at this conductor.

The classes that a twisted layering produces are more rigid than arcs. The
checker layers the three arcs of $\mu_{15}$ by seven seeded twists into a
proper and robust 3-coloring of $\mu_{105}$, whose classes are linearly
independent sets of 35 roots. The sum of each whole class survives only the
identity, with neither the reflection nor any other twist; six seeded
signed sums on 20 class points survive at most two twists each, and six on
10 points survive 52 to 165 each. Thus the sampled large-support values
cluster with $\mathcal N=\{1\}$ for classes of the kind the induction
feeds to the next step. This finite sample gives no clustering theorem
for every value in those classes. Whether that pattern persists, with spread survival only
below an allowance of order $(\log M)^2$, is the clustering question at
larger conductors.

The whole-class part of this rigidity propagates through the induction.
Write $\mathrm{Stab}(C)=\{g\in G_M:gC=C\}$.

**Lemma 11 (layered classes are rigid).** Let $C\subseteq\mu_M$, let $p$ be
a prime not dividing $M$, and let $D=\bigcup_{t\in\mathbb Z/p}\zeta_p^t\,g_t^{-1}C$
with twists $g_t\in G_M$. A twist $h=(h',\pi)$ of
$G_{Mp}=G_M\times\mathrm{Sym}(\mathbb Z/p)$ satisfies $hD=D$ exactly when
$h'\in g_{\pi(t)}^{-1}\mathrm{Stab}(C)\,g_t$ for every $t$. Hence
$\mathrm{Stab}(D)=\{1\}$ when the conjugates
$g_t^{-1}\mathrm{Stab}(C)\,g_t$ have trivial common intersection and, for
every permutation $\pi\ne1$ of $\mathbb Z/p$, the sets
$g_{\pi(t)}^{-1}\mathrm{Stab}(C)\,g_t$, $t\in\mathbb Z/p$, have no common
element.

*Proof.* The twist $h$ sends the layer $\zeta_p^t\,g_t^{-1}C$ to
$\zeta_p^{\pi(t)}h'g_t^{-1}C$, so $hD=D$ exactly when
$h'g_t^{-1}C=g_{\pi(t)}^{-1}C$ for every $t$, that is,
$g_{\pi(t)}h'g_t^{-1}\in\mathrm{Stab}(C)$. For $\pi=1$ the conditions put
$h'$ in every conjugate, so $h'=1$; for $\pi\ne1$ they have no common
solution. $\square$

Both hypotheses ask the twists to avoid coincidences: for $\pi\ne1$, that
no single $h'$ satisfies $p$ coset conditions at once, and for $\pi=1$, that
the conjugates of the small group $\mathrm{Stab}(C)$ by different twists
share no nontrivial element. Starting from an arc class, whose stabilizer
has two elements by Lemma 10, and twists that avoid these coincidences at
every step, every layered class has trivial stabilizer, so the sum of a
whole layered class survives, with its own support, only the identity;
the checker confirms this for the seeded layering at 105, whose base arcs
of $\mu_{15}$ lie outside the range of Lemma 10. A quantitative bound for
random twists involves the centralizers of the elements of
$\mathrm{Stab}(C)$ and is not written here. Large proper subsets and other
representations are not covered by this argument.

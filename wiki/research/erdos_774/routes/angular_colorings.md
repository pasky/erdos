---
name: research/erdos_774/routes/angular_colorings
title: Angular colorings and short flat relations
desc: "Coloring the roots of odd squarefree order by arcs of argument bounds every prime grid by the least degree of a flat cyclotomic multiple, so unbounded coloring of the grids needs signed vanishing sums in arbitrarily short arcs."
tags: [E0774, proved, tensor, obstruction, incomplete]
sources: []
created: 2026-10-15T11:14:17Z
updated: 2026-10-15T11:14:17Z
---

# Angular colorings and short flat relations

***

## Standing

This page tests the [distinct-prime tensor route](../proof_sketch.md) against
one explicit coherent coloring: color a root of unity by the arc of the circle
that contains its argument. All results here are author-recorded, by Plasma
AI; none is independently reviewed.

- **Proved.** The arc coloring is proper exactly when no signed vanishing sum
  fits in an arc, which is a statement about flat multiples of cyclotomic
  polynomials, and the governing ratio can only fall as primes are added
  ([[theory/integer_sequences/L123_odd_root_arc_colorings/_index|L123, tier 0, with its proof]]).
  Consequently the missing theorem (4) of the main argument, unbounded
  dissociated coloring of $S_3\otimes S_5\otimes\cdots\otimes S_{p_k}$,
  **implies** that signed vanishing sums of roots of unity of odd squarefree
  order exist inside arcs of every positive length. Shortest relations obey
  the layer, cylinder and minimal-component constraints below.
- **Open.** Whether such short sums exist is the precise open claim
  [[theory/integer_sequences/L124_flat_cyclotomic_degree_ratio/_index|L124, which asserts that they do not; it would bound every prime grid and close this route]].
  Neither direction is proved.
- **Data.** The governing ratio is $8/15$ at $N=15$ and $7/15$ at $N=105$,
  both exact; an explicit flat multiple gives at most $502/1155$ at
  $N=1155$, where an exact-coefficient integer program found nothing
  shorter. The rank bound alone keeps three arcs proper through the prime
  19 and four arcs through the prime 73.

The proved result is a necessary condition for (4), not an obstruction to
the whole prime family: the constant needed to make these arc colorings
uniform is still unproved. The finite examples and restrictions on special
relation types do not supply an all-palette forcing mechanism or a bounded
coloring of every stage.

## Setting

Let $N>1$ be odd and squarefree, $\zeta_N=e^{2\pi i/N}$ and
$\mu_N=\{\zeta_N^e\}$. For $p$ prime map the basis vectors
$e_1,\ldots,e_{p-1}$ of $S_p$ to $1,\zeta_p,\ldots,\zeta_p^{p-2}$; the last
vector $-e_1-\cdots-e_{p-1}$ then maps to $\zeta_p^{p-1}$. Tensor products of
these bases form a rational basis of $\mathbb Q(\zeta_{N_k})$,
$N_k=p_1\cdots p_k$, because the degrees $p_i-1$ multiply. So
$E_k=S_{p_1}\otimes\cdots\otimes S_{p_k}$ maps bijectively and linearly onto
$\mu_{N_k}$, every linear relation is preserved, and $E_k$, $\mu_{N_k}$ and
the integer blocks $F_k$ of the main argument have the same dissociated
coloring number.

For extraction, use
[[theory/integer_sequences/L21_roots_of_unity_proportional_dissociation/_index|L21 at its recorded tier-2 standing]]:
one integer denominator $K$ works for every finite set of roots of unity.
The rational identification therefore gives every subset of every $E_k$
a dissociated subset of relative size at least $1/K$. The
[radix encoding](../lemmas/rational_realization.md), with base $N_k+2$
and absolute values, preserves every ternary relation support because
each signed coordinate sum has magnitude at most $N_k$; odd-order roots
give no zero or antipodal columns. Finally the
[separated-block construction](../lemmas/finite_blocks.md) preserves that
same $1/K$ and has coloring number $\sup_k\chi(E_k)$. These elementary
transfers are author-recorded. No extraction constant depends on a palette
size, and none of these transfers proves the missing chromatic growth.

A **signed relation** of $\mu_N$ is a nonzero $f:\mu_N\to\{-1,0,1\}$ with
$\sum_xf(x)x=0$; a set is dissociated exactly when it carries none. Its
**arc length** $\ell(f)$ is the least $\ell$ such that the support lies in
$\ell$ consecutive powers $\zeta_N^a,\ldots,\zeta_N^{a+\ell-1}$. Write

$$
D(N)=\min_f\ell(f)-1,\qquad \rho(N)=\frac{D(N)}N .
$$

Dividing by $\zeta_N^a$ turns a signed relation in $\ell$ consecutive powers
into a nonzero polynomial with coefficients in $\{-1,0,1\}$ and degree at
most $\ell-1$ that is divisible by $\Phi_N$, and conversely. So $D(N)$ is the
least degree of a flat multiple of $\Phi_N$, and $D(N)\ge\varphi(N)$.

## The angular coloring

Color $\zeta_N^e$, $0\le e<N$, by $\lfloor qe/N\rfloor$. Each class is a run
of at most $\lceil N/q\rceil$ consecutive powers.
[[theory/integer_sequences/L123_odd_root_arc_colorings/_index|L123]] proves:

1. the $q$ classes are dissociated **if and only if** $qD(N)\ge N$, so
   $\chi_{\rm diss}(\mu_N)\le\lceil1/\rho(N)\rceil\le\lceil
   N/\varphi(N)\rceil$, the last being the rational bound, here realized by
   an explicit coloring;
2. $\rho(N)\le\rho(M)$ whenever $M\mid N$, by substituting $x^{N/M}$ in a
   flat multiple of $\Phi_M$;
3. if $c=\inf\rho(M)$ over odd squarefree $M>1$ is positive, coloring every
   root of unity of odd squarefree order by $\lfloor q\theta\rfloor$, where
   $e^{2\pi i\theta}$ is the root and $0\le\theta<1$, gives $q$ dissociated
   classes for every $q\ge1/c$.

Every odd squarefree $M$ divides some $N_k$, so $c=\lim_k\rho(N_k)$, a
nonincreasing limit, and

$$
\chi_{\rm diss}(E_k)\le\lceil1/\rho(N_k)\rceil\le\lceil1/c\rceil
\quad\text{for all }k\text{ when }c>0 .
$$

Thus (4) implies $c=0$:

> **(N)** For every $\varepsilon>0$ some nonempty set of distinct roots of
> unity of odd squarefree order, all with arguments in one closed arc of
> length $2\pi\varepsilon$, has a vanishing signed sum.

(N) is the negation of
[[theory/integer_sequences/L124_flat_cyclotomic_degree_ratio/_index|L124]].
It is a necessary condition only: $c=0$ would defeat the arc colorings but
would not by itself force a monochromatic relation under other colorings.
If instead $c>0$, the set of all roots of unity of odd squarefree order is a
finite union of dissociated sets, and the prime-power coset separation in the
[root-transversal equivalence](roots_coloring_structure.md) then makes all
roots of unity a finite union of dissociated sets, a positive answer to the
covering question (Question 38) of Déchamps recorded there.

## Values of the governing ratio

| $N$ | $\varphi(N)$ | $D(N)$ | $\rho(N)$ | Basis |
|---:|---:|---:|---:|---|
| 15 | 8 | 8 | 0.5333 | $\Phi_{15}$ is flat; no nonzero multiple has degree below 8 |
| 105 | 48 | 49 | 0.4667 | $(1-x)\Phi_{105}$ is flat; degree-48 multiples are $\pm\Phi_{105}$, of height two |
| 1155 | 480 | $\le502$ | $\le0.4347$ | explicit flat multiple of degree 502; no certified matching lower bound |

The polynomial $\Phi_{15}=x^8-x^7+x^5-x^4+x^3-x+1$ is visibly flat. The flat
multiple $(1-x)\Phi_{105}$ is the
[degree-49 relation](../evidence/short_arc_root_relations.md), whose
flatness follows from Bzdęga's jump-one theorem cited there. A multiple of
degree exactly $\varphi(N)$ is an integer multiple of $\Phi_N$ by Gauss's
lemma, so it is flat only when $\Phi_N$ is; $\Phi_{105}$ has the
coefficient $-2$ at $x^7$ and $x^{41}$.

For $N=1155$ the multiplier

$$
Q(x)=(1-x^6)\bigl(1+x+x^2-x^4-2x^5-x^6+x^8-x^{10}-2x^{11}-x^{12}
+x^{14}+x^{15}+x^{16}\bigr),
$$

of degree 22, makes $\Phi_{1155}Q$ a flat polynomial of degree 502 with
128 nonzero coefficients; its second factor has no cyclotomic factor. The [checker](../evidence/angular_flat_multiples/_index.md)
verifies these displayed multiples by exact multiplication. Thus
$\rho(1155)\le502/1155<7/15$: the prime 11 lowers the ratio strictly, below
the value $49\cdot11/1155$ that inflating the 105 relation gives. That no
flat multiple of $\Phi_{1155}$ has degree at most 501 is a solver
observation, not a retained certificate: the exact-coefficient feasibility
problem with $Q(0)=1$ (every flat multiple can be shifted and negated to
satisfy it), its bounded integer unknowns and its $\{-1,0,1\}$ coefficient
constraints was declared infeasible by the HiGHS solver in SciPy at the
degrees 488 and 495 to 501, which covers every degree up to 501 because a
shorter flat multiple stays feasible at a larger degree, and feasible at 502
to 505, 520 and 538; the
[discovery script](../evidence/angular_flat_multiples/_index.md) beside the
checker reproduces these runs. For $N=15015$ the inflation of the 1155
multiple gives $D(15015)\le6526$, ratio $0.4346$; solver runs of 450 and 900
seconds at the degrees 6000 and 6300 stopped at their time limits without a
solution and decide nothing.

The exact ratios at 15 and 105 and the upper bound at 1155 are
$0.5333,0.4667,0.4347$, while the corresponding rank bounds
$\varphi(N)/N$ are $0.5333,0.4572,0.4156$. The excesses at the first two
orders are approximately $0$ and $0.0095$; the third is at most $0.0191$.
Only the uncertified solver lower bound would make the third excess an
observed increase. Three arcs stay
proper while $\lceil N_k/3\rceil\le\varphi(N_k)$, which holds through the
prime 19, where $\varphi/N=0.342$; at 23 the rank bound is $0.327$, so a
three-arc failure there would need an excess below $0.006$. Four arcs stay
proper through the prime 73 ($\varphi/N=0.252$; at 79 it is $0.249$).

## Structure of a short relation

### Layers

Let $N=Mp$ with $p$ prime and write every $x\in\mu_N$ uniquely as
$x=y\zeta_p^t$, $y\in\mu_M$, $t\in\mathbb Z/p$. For $f$ on $\mu_N$ put
$f_t(y)=f(y\zeta_p^t)$ and $F_t=\sum_yf_t(y)y\in\mathbb Z[\zeta_M]$. Since
$[\mathbb Q(\zeta_N):\mathbb Q(\zeta_M)]=p-1$, the powers
$1,\zeta_p,\ldots,\zeta_p^{p-1}$ satisfy only the relation
$\sum_t\zeta_p^t=0$ over $\mathbb Q(\zeta_M)$, so
$\sum_t\zeta_p^tF_t=0$ exactly when all $F_t$ equal one common value $F$.

Suppose the support of a signed relation $f$ lies in a half-open arc of
angular fraction $\alpha$. Then layer $t$ lies in the rotated arc of the same
fraction, which contains at most $\lceil\alpha M\rceil$ consecutive $M$-th
roots of unity.

- If $F=0$, every nonzero layer is a signed relation of $\mu_M$ inside
  $\lceil\alpha M\rceil$ consecutive powers, so
  $D(M)+1\le\lceil\alpha M\rceil$.
- If $\alpha\le1/p$, two points of one coset $y\mu_p$ differ in argument by
  a nonzero multiple of $2\pi/p$ and cannot both lie in the arc. The layers
  then have pairwise disjoint supports, and $F$ has $p$ signed
  representations with pairwise disjoint supports.

For a shortest relation $\alpha M=(D(N)+1)/p$. So **whenever
$D(M)\ge\lceil(D(N)+1)/p\rceil$, every shortest relation of $\mu_N$ has a
nonzero common layer value in the direction of $p$**: a strict improvement
over the subconductor is never a union of subconductor relations. The 1155
relation above has nonzero layer value in each of its four prime directions,
because $\lceil503/11\rceil=46<49=D(105)$ and, for $p=7,5,3$, the
values $72,101,168$ lie below $\varphi(165)=80$, $\varphi(231)=120$ and
$\varphi(385)=240$.

### Cylinders and the large-prime limit

For odd squarefree $M>1$ and $w\ge1$, let $V_w(M)$ be the set of
$F\in\mathbb Z[\zeta_M]$ that have a signed representation on every run of
$w$ consecutive $M$-th roots of unity, and let $w^*(M)$ be the least $w$ with
$V_w(M)\ne\{0\}$.

**Cylinder lemma.** For every prime $p\nmid M$,
$D(Mp)\le p\,w^*(M)-1$; and if moreover $p>M$, then
$D(Mp)\ge p\bigl(\min\{D(M)+1,w^*(M)\}-1\bigr)$.

*Proof.* Take $0\ne F\in V_w(M)$, $w=w^*(M)$. For each $t\in\mathbb Z/p$ the
half-open arc of arguments $2\pi[-t/p,-t/p+w/M)$ contains exactly $w$
consecutive $M$-th roots $\zeta_M^{j_t},\ldots,\zeta_M^{j_t+w-1}$, since its
length is $w$ times their spacing. Choose a signed representation of $F$ on
them and place it on layer $t$. Every layer has value $F$, so the result is
a signed relation of $\mu_{Mp}$, nonzero since $F\ne0$; the argument of
$\zeta_M^{j}\zeta_p^t$ with $j/M\in[-t/p,-t/p+w/M)$ lies in $2\pi[0,w/M)$,
which contains exactly $wp$ consecutive $Mp$-th roots. Hence
$D(Mp)\le wp-1$.

For the lower bound let $f$ be a shortest relation of $\mu_{Mp}$, rotated
into the arc $2\pi[0,\ell/(Mp))$, $\ell=D(Mp)+1$, and put
$w=\lceil\ell/p\rceil$. If its common layer value is zero, the first layer
bullet gives $D(M)+1\le w$. Otherwise, for each $b$ choose $t$ with
$-t/p\in((b-1)/M,b/M]$ modulo one, possible because $p>M$; layer $t$ then
lies in $\zeta_M^b,\ldots,\zeta_M^{b+w-1}$, so $F$ has a signed
representation on every run of $w$ consecutive roots and $w^*(M)\le w$. In
both cases $\min\{D(M)+1,w^*(M)\}\le\lceil\ell/p\rceil$. $\square$

With the inflation bound $D(Mp)\le pD(M)$, a single new prime $p>M$ thus
moves the ratio into the interval of length $1/M$ ending at
$\min\{\rho(M),w^*(M)/M\}$. Comparing the upper bound with
$D(Mp)\ge\varphi(Mp)=(p-1)\varphi(M)$ for a prime $p>\varphi(M)$ gives
$w^*(M)\ge\varphi(M)$. If $\Phi_M$ has a
coefficient of absolute value at least three, then $w^*(M)>\varphi(M)$:
multiplication by $\zeta_M$ shifts power-basis coordinates and subtracts the
top coordinate times the coefficients of $\Phi_M$, so a nonzero top
coordinate creates a coordinate of absolute value at least two, and some
rotation of any nonzero $F$ has a nonzero top coordinate because the
rotations span a lattice of full rank. The cylinder lemma is the one
construction found here that could carry the excess
$\rho(N_k)-\varphi(N_k)/N_k$ to zero along the prime prefixes, through
$\rho(N_{k+1})\le w^*(N_k)/N_k$; it needs $w^*(N_k)-\varphi(N_k)=o(N_k)$.

### Minimal components

The support of a signed relation splits into disjoint parts on each of which
$f$ restricts to a minimal vanishing sum: choose an inclusion-minimal
nonempty vanishing part and repeat on the rest, whose sum also vanishes.
Divide a minimal part $T$ by one of its roots. In the terms of
[[../library/number_theory/conway_jones_1976_trigonometric_diophantine_equations_vanishing_sums_roots_unity/_index|Conway and Jones]]
(their Section 3, printed p. 231), the result is a monic minimal vanishing
sum, whose
exponent equals its reduced exponent $r$; here $r$ divides $N$, so it is odd
and squarefree, and $T$ is a
rotated signed relation of $\mu_r$. Their Theorem 5 (p. 235), consumed as
stated, gives

$$
|T|\ge2+\sum_{p\mid r}(p-2).
$$

The definitions and this statement are checked against the printed
pp. 231 and 235. The source theorem is an external premise; its proof is
not reconstructed here. The coefficient convention is rational formal
sums, so signs remain coefficients and do not introduce an extra factor
of two into the reduced exponent.

The angular span of $f$ is at least that of $T$, which is at least
$2\pi D(r)/r\ge2\pi\varphi(r)/r$. Hence a signed relation inside a closed
arc of length $2\pi\varepsilon$ has every minimal component of reduced
exponent with $\varphi(r)/r\le D(r)/r\le\varepsilon$. Let $P$ be the least
prime with $\prod_{3\le p\le P}(1-1/p)\le\varepsilon$ and $J$ the number of
odd primes up to $P$. If the $j$ prime factors of $r$ are
$q_1<\cdots<q_j$, then $q_i$ is at least the $i$-th odd prime, so
$\prod_i(1-1/q_i)\le\varepsilon$ forces $j\ge J$ and
$\sum_{p\mid r}(p-2)\ge\sum_{3\le p\le P}(p-2)$. For $\varepsilon=1/3$,
$P=23$ and $J=8$: every minimal component has at least $84$ terms and a
reduced exponent with at least eight prime factors.

## What the arc colorings defeat

A monochromatic relation for the $q$-arc coloring of $\mu_M$ lies in at
most $\lceil M/q\rceil$ consecutive powers, an arc of span less than $2\pi/q$.
So the $q$-arc coloring defeats every forcing mechanism all of whose forced
relations have a minimal component of reduced exponent $r$ with
$qD(r)\ge r$. For $q=3$ this includes every relation with a minimal component
of at most 83 terms or with reduced exponent dividing
$3\cdot5\cdots19=4849845$. It therefore includes full fibers, the crosses
and checkerboards of two-prime slices, every relation inside a slice over at
most seven odd primes, every mechanism whose relations have at most 83 terms,
and the tensor products $g\otimes h$ of such a relation $g$ with any signed
function $h$ on a coprime factor, whose support contains a rotated copy of
the support of $g$. For larger $q$ the same holds with larger bounds: any
mechanism whose relations have bounded support is defeated by the $q$-arc
coloring once $q$ is large in terms of the bound.

Two mechanisms are not covered. Determinant flattening multiplies blocks of
height-$h$ factor relations, and its support is a union of sets of sums of
block arguments; nothing above bounds the span of such a union from below by
the spans of the factors. Adaptive nondecomposable constructions are not
covered either. Both remain admissible routes to (N), and to (4).

## Heuristics, and why they do not decide L124

These are models, not arguments. Two regimes behave differently.

**Far beyond the rank bound.** For a uniformly random signed function on an
arc of $L=\varepsilon N$ consecutive $N$-th roots, a local limit model for
its value in $\mathbb Z[\zeta_N]$ gives an expected number of signed
relations

$$
3^{L}\Bigl(\frac{3}{4\pi\varepsilon G(N)}\Bigr)^{\varphi(N)/2}
\det(K)^{-1/2},\qquad G(N)=\prod_{p\mid N}p^{1/(p-1)},
$$

with $K$ the normalized Gram matrix of the unit frequencies of $\Phi_N$ on
the arc. Along the prime prefixes $\varphi/N\sim2e^{-\gamma}/\log p_k$ and
$\log G=\log p_k-\gamma-\log2+o(1)$. If moreover $\log\det K=o(\varphi)$, the
exponent is $N(\varepsilon\log3-e^{-\gamma}+o(1))$, and random-like relations
need arcs of fraction above $e^{-\gamma}/\log3\approx0.511$, which exceeds
$1/3$. The model needs $L/\varphi(N)\to\infty$, that is $\log p_k\to\infty$,
so it describes only astronomically large conductors, and its correlation
hypothesis fails at the sizes computed here: at $N=1155$ and $L=503$ the
uncorrelated value $\det K=1$ would give the lattice below the covolume
$(\varepsilon G)^{\varphi/2}=e^{164.3}$, while its exact covolume is
$e^{51.4}$.

**Near the rank bound.** When $L$ exceeds $\varphi(N)$ by a small rank
$m=L-\varphi(N)$, the relations of the arc form the rank-$m$ lattice
$\Phi_N\cdot\mathbb Z[x]_{<m}$, and the geometry-of-numbers count compares
its covolume, the square root of the Gram determinant of
$\Phi_N,x\Phi_N,\ldots,x^{m-1}\Phi_N$, with the volume of the $m$-dimensional
section of the cube $[-1,1]^L$, at most $2^m(L/m)^{m/2}$ by K. Ball's 1989
bound for central sections of cubes. At $N=1155$ and $L=503$, $m=23$, the
exact covolume is $e^{51.39}$ and the section bound is $e^{51.42}$, and the
Gaussian heuristic length of a shortest
vector is about $10.8$, while the flat multiple above has length
$\sqrt{128}\approx11.3$. So at this size the threshold behaves like that of a
generic lattice of the same covolume, and predicting $D(N_k)$ reduces to
estimating these covolumes. At the prime 23 the rank needed for a three-arc
failure is $\lceil N_8/3\rceil-\varphi(N_8)=686{,}785$, and that covolume was
not computed.

The finite values and upper bounds are compatible with a limit above
$1/3$ and with a limit of zero. The model comparisons are diagnostics;
neither is an estimate uniform in the conductor, and neither settles the
open infimum.

## Limits of the remaining tests

- Decide the sign of the excess trend: $D(15015)$, or any flat multiple of
  $\Phi_{15015}$ of degree below 6526, and the cylinder threshold
  $w^*(1155)$, which bounds every $\rho(1155p)$ from above.
- Estimate the covolume of $\Phi_{N}\cdot\mathbb Z[x]_{<m}$, a Toeplitz Gram
  determinant of the autocorrelation of the coefficients of $\Phi_N$, at
  $N=N_8$ and $m=686{,}785$, against the section volume; a covolume far above
  the section bound would make a three-arc failure at the prime 23
  implausible without special structure, and one far below would make it
  likely.
- A construction for (N) must, at its first conductor below each threshold,
  be cylindrical in every prime direction where it improves, and its
  minimal components must reach the lengths above. The cylinder lemma with
  $w^*(N_k)-\varphi(N_k)=o(N_k)$ is the natural candidate.
- A proof of L124 needs a lower bound $D(M)\ge cM$, growing like $M$ rather
  than like $\varphi(M)$. The height of $\Phi_M$ gives only one extra degree
  in the arguments recorded here, for $D(105)$ and for $w^*$.

These finite calculations would describe the angular invariant at another
stage. None alone would prove $c=0$, prove $c>0$, or control arbitrary
palettes. In particular, a trend in several ratios is not a continuation
theorem for the fixed prime schedule.

**Stopped conclusion and reopening condition.** Neither the fixed family
with unbounded actual chromatic number nor a uniform obstruction to that
conjunction has been obtained. L123 identifies a necessary condition and
the following precise alternatives. A proof of L124 closes the prime
family. A construction of short signed sums with angular fractions tending
to zero refutes L124 but only defeats the arc colorings; it must be coupled
to a mechanism forcing a monochromatic actual ternary relation for every
finite palette before (4) follows. A single sub-third-circle relation,
another finite SAT instance, or a construction for bounded templates does
not meet that obligation. The extraction constant and both integer-transfer
steps remain fixed as in the main argument.

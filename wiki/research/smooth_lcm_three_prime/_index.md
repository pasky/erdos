---
name: research/smooth_lcm_three_prime
title: Three-prime running-lcm series
desc: |
  Exact three-prime running-lcm expansions with every multiplicity, finite
  cone-partition obstructions, and arithmetic tail identities with the
  remaining irrationality and transcendence gaps.
tags: []
sources: []
problems: [269]
created: 2026-10-15T15:50:35Z
updated: 2026-10-15T16:35:43Z
---

# Three-prime running-lcm series

[[research/_index|..]]

[[research/smooth_lcm_three_prime/arithmetic_routes|arithmetic_routes]]: Exact block numerators and quadratic tail bounds for every three-prime
set, with the obstruction to finite tail states and to a direct integral
polynomial-growth fixed-base recoding.

[[research/smooth_lcm_three_prime/evidence/_index|evidence/]]: Exact checks of the three-prime running-lcm expansions, the triangular
witnesses for the face-rank obstruction, and formal relation searches with positive controls;
domains and limitations are stated on the owning research page.

[[research/smooth_lcm_three_prime/finite_separation|finite_separation]]: An elementary derivation of the known finite-separation obstruction,
using dense fractional parts and triangular carry matrices.

***

For [[problems/irrationality/E0269/_index|Problem 269]] with exactly three
primes, $P=\{p,q,r\}$, this page retains every smooth-number contribution
and tests the extension of the
[[research/smooth_lcm_series/_index|two-prime factorization]]. The exact
identities below lead to a coupled lattice sum. Finite termwise separation,
a unimodular product decomposition, and finite signed partitions into
one-slope halfspace regions fail in the precise senses stated below.
A separate [[research/smooth_lcm_three_prime/arithmetic_routes|arithmetic
attack]] gives exact integer block numerators and quadratic tail bounds,
but no irrationality contradiction.

The supplied derivations are author-recorded by Plasma AI, with source-owned
results identified separately. No identity or applicable value theorem here
settles the irrationality of the three-prime series. The current sketch and
conditions for reopening the tested separations appear below.

## Exact expansion

Fix distinct primes $p,q,r$, and include $1$ in the increasing enumeration of
the integers whose prime factors lie in $P$ (the smooth integers). For distinct
primes $x,y$ write $\lambda_{xy}=\log y/\log x$, so that
$\log_x(y^k)=k\lambda_{xy}$. Each $\lambda_{xy}$ is irrational, and
$\log p,\log q,\log r$ are linearly independent over $\mathbb Q$, both by
unique factorization. As on the two-prime page, the running lcm at a smooth
cutoff $m$ is

$$
D(m)=p^{\lfloor\log_p m\rfloor}q^{\lfloor\log_q m\rfloor}
     r^{\lfloor\log_r m\rfloor}:
$$

each factor $u^{\lfloor\log_u m\rfloor}$ is a smooth integer at most $m$, and
every smooth integer at most $m$ has $u$-adic valuation at most
$\lfloor\log_u m\rfloor$. At $m=p^aq^br^c$ this reads

$$
D(m)=p^{a+\lfloor b\lambda_{pq}+c\lambda_{pr}\rfloor}\,
     q^{b+\lfloor a\lambda_{qp}+c\lambda_{qr}\rfloor}\,
     r^{c+\lfloor a\lambda_{rp}+b\lambda_{rq}\rfloor}.
$$

Unique factorization makes $(a,b,c)\mapsto p^aq^br^c$ a bijection onto the
smooth integers, so the series of the problem is exactly

$$
S_P=\sum_{a,b,c\ge0}\frac1{D(p^aq^br^c)}.
$$

Every smooth integer contributes its own term, including the cutoffs at which
the running lcm does not change. Since $D(m)\ge m$, the series is dominated by
$\prod_{u\in P}(1-u^{-1})^{-1}$, which justifies every rearrangement of the
nonnegative terms below.

Each prime's floor depends on the two other exponents:

$$
\frac1{D(p^aq^br^c)}=\frac{K_p(b,c)\,K_q(a,c)\,K_r(a,b)}{p^aq^br^c},
\qquad
K_p(b,c)=p^{-\lfloor\log_p(q^br^c)\rfloor},
$$

and cyclically. For two primes each such factor depends on one exponent, and
the series is the product of two one-variable series. Here
$K_p(b,c)=p^{-\lfloor b\lambda_{pq}\rfloor-\lfloor c\lambda_{pr}\rfloor
-e_p(b,c)}$ with the carry digit
$e_p(b,c)=\lfloor\{b\lambda_{pq}\}+\{c\lambda_{pr}\}\rfloor\in\{0,1\}$, where
$\{t\}$ is the fractional part, and cyclically for $e_q(a,c)$ and $e_r(a,b)$.
Hence

$$
\frac1{D(p^aq^br^c)}
 =W_p(a)W_q(b)W_r(c)\,p^{-e_p(b,c)}q^{-e_q(a,c)}r^{-e_r(a,b)},
\qquad
W_p(a)=\frac1{D(p^a)}=p^{-a}q^{-\lfloor a\lambda_{qp}\rfloor}
       r^{-\lfloor a\lambda_{rp}\rfloor},
$$

and cyclically. Grouping the exponent triples by their carry vector partitions
$S_P$ into at most eight cells. A cell is cut out by conditions on pairs of
fractional parts, not by linear inequalities. For example, at
$(p,q,r)=(2,3,5)$ and $m=30$ the carry vector is $(0,1,1)$ and
$D(30)=2^43^35^2=10800=15\,D(2)D(3)D(5)$. A face is not a two-prime series
either: the cutoff $6$ has $D(6)=60$ for $P=\{2,3,5\}$, but $12$ for
$P=\{2,3\}$, because powers of $5$ have already occurred.

## Prime-power events

List the prime powers $u^j$ with $u\in P$ and $j\ge1$ in increasing order as
$\tau_1<\tau_2<\cdots$, which are distinct by unique factorization, and let
$w_i$ be the prime of $\tau_i$. Then $D(\tau_i)=w_1\cdots w_i$, and
$D(m)=D(\tau_i)$ whenever $\tau_i\le m<\tau_{i+1}$. Telescoping gives, for every
smooth $m$,

$$
\frac1{D(m)}=\sum_{i:\ \tau_i>m}\frac{w_i-1}{D(\tau_i)}.
$$

At $m=1$, grouping the events by their prime, this reads

$$
\sum_{u\in P}(u-1)\bigl(A_u-1\bigr)=1,
\qquad
A_u=\sum_{j\ge0}\frac1{D(u^j)},
$$

for every finite set $P$ of primes. For $P=\{p,q\}$ it is the affine identity
of the two-prime page: there $A_p$ and $A_q$ are its series $A$ and $B$, and
$(p-1)(A-1)+(q-1)(B-1)=1$ is the relation $y(1-x)A+x(1-y)B=x+y-xy$ at
$x=1/p$, $y=1/q$. For three primes each $A_u$ is a series with two floors,
$A_p=\sum_aW_p(a)$, and the identity makes $A_r$ an affine function of $A_p$
and $A_q$. Summing the telescoping identity over all smooth $m$ instead gives

$$
S_P=\sum_{u\in P}(u-1)\sum_{j\ge1}\frac{\Psi(u^j)}{D(u^j)},
\qquad
\Psi(x)=\#\{m\ \text{smooth}:\ m<x\}.
$$

The counting function $\Psi$ carries every multiplicity. For two primes,
$\Psi(p^j)=\sum_{n=1}^{j}(\lfloor n\lambda_{qp}\rfloor+1)$ involves one floor.
For three primes $\Psi(p^j)=\sum_{n=1}^{j}N(p^n)$ with

$$
N(p^n)=\#\{(b,c):\ q^br^c<p^n\}
      =\sum_{c=0}^{\lfloor n\lambda_{rp}\rfloor}
       \bigl(\lfloor n\lambda_{qp}-c\lambda_{qr}\rfloor+1\bigr),
$$

the number of lattice points in a right triangle with two irrational legs.
Discarding the multiplicities would give the different series
$\sum_{i\ge0}1/D(\tau_i)=A_p+A_q+A_r-2$, with $\tau_0=1$; for three primes it
is again a combination of series with two floors.

## Obstructions to separation

Each obstruction below concerns the stated class of identities, not the
irrationality of $S_P$.

*Bipartitions.* Let $P$ be any finite set of primes with $\lvert P\rvert\ge3$
and $P=P_1\sqcup P_2$ with both parts nonempty, and let $S^{(i)}$ be the sum of
$1/D(m)$ over the $P_i$-smooth integers $m$, with $D$ the running lcm of the
full $P$-smooth enumeration. Then $S_P<S^{(1)}S^{(2)}$. Indeed
$\lfloor\log_x(m_1m_2)\rfloor\ge\lfloor\log_xm_1\rfloor+\lfloor\log_xm_2\rfloor$
for every prime $x$, so $D(m_1)D(m_2)$ divides $D(m_1m_2)$, and
$(m_1,m_2)\mapsto m_1m_2$ is a bijection from pairs of $P_1$- and $P_2$-smooth
integers onto the $P$-smooth integers; this gives $S_P\le S^{(1)}S^{(2)}$. One
part, say $P_2$, contains two primes $v\ne x$; take $u\in P_1$. The fractional
parts $\{a\lambda_{xu}\}$ and $\{b\lambda_{xv}\}$ are dense in $[0,1)$, so
some $a,b$ make both exceed $1/2$. Then $m_1=u^a$ and $m_2=v^b$ satisfy
$D(m_1m_2)\ge x\,D(m_1)D(m_2)$, and the inequality is strict. For two primes
equality holds, which is the two-prime factorization.

*No finite termwise separation.* For exactly three primes,
[[research/smooth_lcm_three_prime/finite_separation|the carry-matrix
argument]] shows that $1/D(p^aq^br^c)$ is not a finite sum of products of
functions on complementary groups of exponents, across any fixed split.
This is the known rank
obstruction of Cook's Theorem 7.3, with an elementary derivation retained
at the linked page. On each coordinate face the carry digits of the third
prime can be made to form a triangular pattern, which produces invertible
square submatrices of every size.

*No lattice product decomposition.* Since
$u^{-\lfloor x\rfloor}=(1-u^{-1})\sum_{k\ge\lfloor x\rfloor}u^{-k}$, the series
is a weighted count of the lattice points $(m,k)$ with $m,k\ge0$ and
$\sum_vm_v\log v<(k_u+1)\log u$ for every $u\in P$. For two primes the
unimodular change $k'_u=k_u-m_u$ splits this set into a product of two planar
sets, which is the two-prime factorization.
[[theory/irrationality/L189_lcm_series_cone_no_product/_index|L189 proves that
for three or more primes no unimodular change of variables turns the set into a
product of two lower-dimensional sets]]; each irrational facet involves at
least three logarithms, and no splitting into rational subspaces separates
the facets. Writing this lattice set as $\Omega$, the precise identity is

$$
S_P=\prod_{u\in P}(1-u^{-1})
       \sum_{(m,k)\in\Omega}\prod_{u\in P}u^{-k_u}.
$$

*No finite one-slope cone partition.*
[[theory/irrationality/L190_three_prime_no_finite_planar_partition/_index|L190
excludes a finite signed identity for this lattice set using halfspace regions
whose normals each have rational coefficient rank at most two]]. In
particular, lattice points in finitely many invertible affine rational images
of products of planar Hecke–Mahler regions cannot supply such a partition.
A facet normal of the
actual set has coefficient span generated by $\log p,\log q,\log r$,
which has rational dimension three. The obstruction permits arbitrary
one-slope parameters and intercepts; it does not assume their algebraicity.
It concerns lattice indicators in these six coordinates, not identities
that arise only after weighted summation or after adding coordinates.

*Slices.* Along a line parallel to a coordinate axis, for instance with $b,c$
fixed, the term is a constant times
$p^{-a}q^{-\lfloor a\lambda_{qp}+c\lambda_{qr}\rfloor}
r^{-\lfloor a\lambda_{rp}+b\lambda_{rq}\rfloor}$. It carries two floors whose
slopes have the irrational ratio $\log q/\log r$. Along a nonzero lattice
direction supported on at least two coordinates,
all three raw logarithmic slopes are irrational by the rational independence
of the prime logarithms. A direction with negative components has no
infinite ray inside the nonnegative orthant. There are infinitely many
slices in each direction, so even transcendence of every slice would give no
conclusion about $S_P$.

*Formal relation searches.* The evidence below treats $Y_p,Y_q,Y_r$ as
variables independent of the slopes and replaces each value $1/D$ by the
monomial in $Y$ with the exponents of $D$, so that $S_P$, the $A_u$ and the
two-prime series
$A_{u;v}=\sum_{j\ge0}Y_u^{\,j}Y_v^{\lfloor\log_v u^j\rfloor}$ become formal
power series. It proves, by exact rank computations, that for $(2,3,5)$ there
is no relation $\sum_ic_iM_i=0$ in which the $M_i$ are the products
$S_P^kA^\mu$ of total degree at most $3$ in $S_P$ and the five series $A_p$,
$A_q$, $A_{p;q}$, $A_{p;r}$, $A_{q;r}$, and the $c_i$ are polynomials of degree
at most $4$ with rational coefficients. The partner series $A_{q;p}$,
$A_{r;p}$, $A_{r;q}$ and $A_r$ are affine in these, with rational-function
coefficients, by the two-prime and telescoping identities. The same holds with
coefficients of degree at most $3$ for $(2,3,7)$ and $(3,5,7)$, and for
$(2,3,5)$ when the three face sums of $S_P$ join the five series, at total
degree at most $2$ and coefficients of degree at most $3$. Nor is there such a
relation, with coefficients of degree at most $4$, among the products of total
degree at most $3$ in $S_P$ and the three two-prime series $S_{\{p,q\}}$,
$S_{\{p,r\}}$, $S_{\{q,r\}}$ for $(2,3,5)$; in particular, no relation of that
kind expresses $S_P$ as a polynomial of degree at most $3$ in one two-prime
series. Two positive controls confirm that the computation detects the
two-prime identity $S_{\{p,q\}}=A_{p;q}A_{q;p}$ and the telescoping identity
above. These searches cover only the stated families and the formal setting; a
relation that holds only at the point $Y=(1/p,1/q,1/r)$ would not be detected.

## Fit with Theorem 1.1

Bugeaud and Laurent's Theorem 1.1, in
[[../library/irrationality/bugeaud_2022_transcendence_continued_fraction_hecke_mahler/_index|the
arXiv version 1 of their 2022 Hecke–Mahler paper]] (Section 1, printed page 3),
treats

$$
F_{\theta,\rho}(\beta,\alpha)
 =\sum_{k_1\ge1}\ \sum_{k_2=1}^{\lfloor k_1\theta+\rho\rfloor}
  \beta^{k_1}\alpha^{k_2}
$$

for real $\theta,\rho$ with $0\le\theta,\rho<1$ and $\theta$ irrational, and
nonzero algebraic $\alpha,\beta$ with $\beta\ne1$ and
$\lvert\beta\alpha^\theta\rvert<1$; when also $\lvert\beta\rvert<1$, it states
that $F_{\theta,\rho}(\beta,\alpha)$ is transcendental. The statement and the
series conventions were read in the primary TeX and on the printed pages 2 and
3; the proof was not examined. For $\alpha\ne1$, summing the inner geometric
progression turns
$F_{\theta,\rho}$ into a single-index series of terms
$\beta^{k}\alpha^{\lfloor k\theta+\rho\rfloor}$: one slope and one floor.

For three primes the evaluation points $1/p,1/q,1/r$ are algebraic and every
series above converges, so those hypotheses would be met. The univariate
one-floor form is missing. The coupled formulas involve
multiple floors with incommensurable slopes: the series $A_u$, the triangle
counts $N(p^n)$, the carry cells and every slice. The values that do fit the
theorem are the two-prime series $A_{u;v}$, each an affine function of a
Theorem 1.1 value as on the two-prime page. The formal searches exclude
polynomial expressions of $S_P$ in them of low degree, and Theorem 1.1 asserts
nothing about the algebraic independence of values with different slopes,
so it does not control the algebraic nature of a general sum or product of
those values. A separate argument would be needed for the specific
combination.

A two-slope analogue would bring its own slope hypothesis. If it asked that
$1,\lambda_{qp},\lambda_{rp}$ be linearly independent over $\mathbb Q$, as
equidistribution of the pair of fractional parts does, it would ask that
$1/\log p,1/\log q,1/\log r$ be linearly independent over $\mathbb Q$. That
excludes a homogeneous quadratic relation among $\log p,\log q,\log r$ and does
not follow from their linear independence, the only arithmetic input used on
this page. None of the arguments here needs it: the density statements above
concern one slope at a time.

## Further theorem interfaces

The [[research/smooth_lcm_three_prime/arithmetic_routes|integer-block
expansion]] tests a different interface. Luca–Ouaknine–Worrell,
[arXiv:2412.07908v2](https://arxiv.org/html/2412.07908v2), Definition 4 and
Theorem 5, require a polynomially growing integer coefficient sequence in a
fixed algebraic base, together with sparse shifted differences and a uniform
variation bound. Direct termwise recoding of the block expansion into any
fixed algebraic base cannot satisfy both integrality and polynomial growth;
the linked page proves this for every ordered prime triple. A different
regrouping would need its own proof of all the hypotheses.

Adamczewski–Faverjon's
[Mahler's method in several variables II](https://adamczewski.perso.math.cnrs.fr/RegularSingular2.pdf),
Theorem 1.3 on printed page 5, gives algebraic independence for specified
one-variable Hecke–Mahler values with quadratic irrational slopes. It is not
a theorem for arbitrary irrational logarithmic slopes. Their general
Theorem 1.1 assumes regular singular Mahler systems and admissible evaluation
data. Neither a suitable system nor its admissibility is constructed by the
lattice expansion here. These theorem statements were inspected; their
proofs are not imported.

Kebis, Luca, Ouaknine, Scoones and Worrell,
[On Transcendence of Numbers Related to Sturmian and Arnoux-Rauzy Words](https://d-nb.info/1367519063/34),
ICALP 2024, Theorem 6, treats fixed-base series with a finite algebraic
coefficient alphabet and the stated echoing property. The block radices
form a finite set, but the block numerators grow quadratically. No exact
recoding with the required alphabet and echoing property is supplied. This
is a statement-level comparison, not an application of that theorem.

For the source convention at nonzero intercept, a separate caution is
needed. Bugeaud–Laurent's printed page 2 displays an additional term
$\beta^2\alpha\lfloor\theta+\rho\rfloor$ in the relation between its
$\xi$ and $F$ series. From the printed definitions, put
$T_n=\sum_{j=1}^{\lfloor n\theta+\rho\rfloor}\alpha^j$ and $T_0=0$.
For $0<\theta<1$, $0\le\rho<1$, their difference is
$T_n-T_{n-1}=s_n\alpha^{\lfloor n\theta+\rho\rfloor}$. In the domain
$|\beta|<1$ and $|\beta|\,|\alpha|^\theta<1$, direct telescoping gives

$$
\xi_{\mathbf s_{\theta,\rho}}(\beta,\alpha)
 =(1-\beta)F_{\theta,\rho}(\beta,\alpha).
$$

This is a direct derivation, not a source-issued correction. The additional
printed term is nonzero when $\theta+\rho\ge1$ and $\alpha,\beta\ne0$;
it vanishes at the zero intercept used by the two-prime argument. This
auxiliary display supplies no refutation of the numbered theorem.

## Sketch and standing

The target is the transcendence, or at least the irrationality, of $S_P$
for fixed distinct primes $p,q,r$, with the original multiplicities.

Held links are the exact summand, carry partition, event and telescoping
identities, with their elementary derivations above; the known
[[research/smooth_lcm_three_prime/finite_separation|finite-separation
obstruction]]; the complete author-recorded tier-0 arguments
[[theory/irrationality/L189_lcm_series_cone_no_product/_index|L189]] and
[[theory/irrationality/L190_three_prime_no_finite_planar_partition/_index|L190]];
and the exact finite formal relation searches. The
[[research/smooth_lcm_three_prime/arithmetic_routes|arithmetic argument]]
also holds at author-recorded standing: it identifies the genuine block
numerators, proves quadratic growth of normalized tails, and rules out
one direct fixed-base transfer. No unproved premise is used in these held
links.

The separation route still lacks either an exact relation making $S_P$
a nonconstant algebraic function of one applicable transcendental value,
or a relation to several values with enough joint arithmetic information
to control the resulting expression. The excluded finite indicator
partitions cannot supply it. A value theorem applying directly to the
coupled sum is another possible bridge, but none of the inspected theorem
statements covers it.

The arithmetic route lacks a non-cancelling family of small integer linear
forms in the actual tails, or an applicable theorem for the variable
integer denominator chain. Under a rationality assumption the normalized
tails would be integral after one fixed multiplier, but their quadratic
growth prevents a finite-state pigeonhole argument. A new estimate must
use the actual smooth-count numerators, since other positive quadratic
numerators on the same denominator chain give rational values.

These are precise gaps in the proposed arguments. They neither refute the
irrationality target nor establish a no-go theorem for all representations.
The wider finite-prime question remains outside the scope of the target
here; where an obstruction is stated uniformly for larger sets, its proof
is supplied separately in L189 or above.

## Reopening the tested separations

A new identity can reopen the route if it falls outside the excluded
finite termwise and same-coordinate halfspace classes and reaches a value
theorem at the actual algebraic points and logarithmic slopes. Possible
interfaces include an infinite partition with controlled summation, a
representation with additional coordinates, or an identity holding only
after specialization. None is furnished merely by naming the interface.

A theorem for the two-floor series
$\sum_n\beta^n\alpha_1^{\lfloor n\theta_1\rfloor}
\alpha_2^{\lfloor n\theta_2\rfloor}$ would also require an exact bridge
to the full sum and a check of its actual slope conditions. In particular,
a hypothesis about simultaneous rational independence must not be replaced
by the pairwise irrationality that unique factorization supplies. For the
arithmetic route, reopening the fixed-base transfer requires a different
coefficient construction, or a theorem allowing the demonstrated
coefficient heights and variable denominators.

## Evidence

[evidence/main.py](evidence/main.py) runs, from the repository root, with
`uv run --no-sync python wiki/research/smooth_lcm_three_prime/evidence/main.py`.
It checks in exact arithmetic the running-lcm formula against a brute-force
lcm at every smooth cutoff up to $10^{14}$ for five prime sets, finite forms of
the telescoping identity and of the event formula, the examples at the cutoffs
$30$ and $6$, explicit triangular face-rank witnesses at $(2,3,5)$ with $N\le6$,
and the formal relation searches with their positive controls. The full run
takes about two minutes and about 1 GB of memory; `--quick` takes about
fifteen seconds and keeps only the smallest formal search. The checks cover
finite ranges and families; the identities and obstructions are proved above
and in the claims.

---
name: research/erdos_940/quartic_finite_families
title: Quartic finite families and the remaining tail problem
desc: The finite-family theorem, its resolved tail obstruction, and sharper odd-valuation support bounds for every principal-character exception.
tags: []
sources: []
created: 2026-09-22T02:24:55Z
updated: 2026-09-23T00:37:30Z
---


# Quartic finite families and the remaining tail problem

***

## Status

The finite-family theorem below is proved. By itself it applies only to fixed
canonical truncations. The obstruction at the end of this note was subsequently
overcome by the character distribution and uniform Euler majorant in
[the full quartic proof](quartic_complement.md), which establishes positive
lower density of the complement of $S_4$.

## Theorem

Let $F_1,\ldots,F_J$ be a finite family of forms


$$
F_j(\mathbf x)=\sum_{i=1}^4d_{ji}x_i^4,
$$


whose coefficients are positive 4-powerful integers. For every $\varepsilon>0$,
there is a residue class $a\pmod M$, with $a\equiv8\pmod{16}$, such that


$$
\limsup_{X\to\infty}\frac M X
\sum_{j=1}^J\#\{\mathbf x\in\mathbb N^4:F_j(\mathbf x)\le X, F_j(\mathbf x)\equiv a\pmod M\}
<\varepsilon.
\tag{1}
$$


In particular, the complement of the union of their positive value sets has
positive lower density.

### Elimination of square products of coefficients

Let $P$ be the finite set of odd primes dividing some coefficient in the family.
Put


$$
M_0=16\prod_{p\in P}p^2,
$$


and choose $a_0$ by


$$
a_0\equiv8\pmod{16},\qquad a_0\equiv p\pmod{p^2}\quad(p\in P).
\tag{2}
$$


We claim that (2) excludes every form with $\Delta=\prod_i d_i$ a rational
square.

Associate the positive definite quadratic form $Q(\mathbf y)=\sum_i d_i y_i^2$.
Since its determinant is a square, it is similar over $\mathbb Q$ to


$$
\langle1,u,v,uv\rangle,\qquad u,v>0,
$$


the norm form of the quaternion algebra $(-u,-v)$. This algebra is ramified at
the real place. Hilbert reciprocity implies ramification at at least one finite
place. Here we use the standard reciprocity theorem for Hilbert symbols, and the
equivalence between splitting of a quaternion algebra and isotropy of its norm
form.

If $F(\mathbf x)\equiv8\pmod{16}$, at least one $d_i x_i^4$ is odd: otherwise
every term is divisible by 16, because each even coefficient is 4-powerful. Set
$y_i=x_i^2$. Then $v_2(Q(\mathbf y))=3$, while the derivative in a coordinate
with $d_i,y_i$ odd has valuation 1. The one-variable Hensel criterion
$3>2\cdot1$ proves that $Q$ is isotropic over $\mathbb Q_2$.

Consequently $Q$ is anisotropic at some odd prime $p$. This prime divides a
coefficient: a four-variable nondegenerate quadratic form with unit coefficients
has a nonsingular zero modulo every odd prime and hence is isotropic locally.

At this anisotropic prime, at most two coefficients are units. Three unit
coefficients would already give a nonsingular zero of the corresponding ternary
quadratic form modulo $p$. If exactly two are units, their binary reduction must
be anisotropic. Therefore $F(\mathbf x)\equiv0\pmod p$ forces every variable
belonging to a unit coefficient to be divisible by $p$. Their fourth powers are
divisible by $p^4$, and every nonunit coefficient is itself divisible by $p^4$.
Hence $p^4\mid F(\mathbf x)$, contradicting $F(\mathbf x)\equiv p\pmod{p^2}$.
The cases of at most one unit coefficient give the same contradiction.

This proves the claim.

### Simultaneous savings for nonsquare products

Discard the excluded forms. Let


$$
K=\mathbb Q(\sqrt{\Delta_j}:1\le j\le J),\qquad G=\operatorname{Gal}(K/\mathbb Q).
$$


Every remaining $\Delta_j$ is nonsquare and defines a nontrivial quadratic
character $\chi_j$ of $G$. The field $K$ is totally real, so
$K\cap\mathbb Q(i)=\mathbb Q$.

For each $g\in G\setminus\{1\}$, Chebotarev supplies a positive-density set of
primes $q\equiv3\pmod4$ with Frobenius $g$ in $K$, avoiding the finite
coefficient-prime set. Its reciprocal sum diverges. Given $T>0$, choose finitely
many such primes with


$$
T\le\sum_{q\in\mathcal Q_g}\frac1q\le T+\frac1{|G|}.
\tag{3}
$$


All selected primes can be required to exceed any fixed threshold.

At $q\equiv3\pmod4$, the fourth-power map and the square map on $\mathbb F_q$
have identical fiber cardinalities over each target. The elementary
four-variable quadratic Gauss-sum formula therefore gives


$$
\rho_q(0;F_j):=q^{-3}\#\{\mathbf x\bmod q:F_j(\mathbf x)=0\}
=1+\chi_j(g)\frac{q-1}{q^2}.
\tag{4}
$$


Using $\log(1+t)\le t$, equations (3)–(4), and $\sum_q q^{-2}<\infty$, we obtain


$$
\log\prod_{g\ne1}\prod_{q\in\mathcal Q_g}\rho_q(0;F_j)
\le T\sum_{g\ne1}\chi_j(g)+O(1)
=-T+O(1).
\tag{5}
$$


The error is bounded independently of $T$ and $j$ for this fixed family. The
final equality holds because $\chi_j$ is nontrivial.

Take


$$
M=M_0\prod_g\prod_{q\in\mathcal Q_g}q,
$$


and choose $a\equiv a_0\pmod{M_0}$, $a\equiv0\pmod q$ at every selected prime.
The local factors at $M_0$ are fixed. By (5), every surviving form's normalized
congruence count tends to zero as $T\to\infty$.

### Passage from congruence counts to representations

For each fixed form and modulus, positive lattice-point counting gives


$$
\#\{\mathbf x\in\mathbb N^4:F_j(\mathbf x)\le X, F_j(\mathbf x)\equiv a\pmod M\}
=\frac{\Gamma(5/4)^4X}{M\Delta_j^{1/4}}\rho_M(a;F_j)
+O_{M,F_j}(X^{3/4}),
$$


where $\rho_M=M^{-3}\#\{\mathbf x\bmod M:F_j(\mathbf x)\equiv a\}$ and CRT makes
$\rho_M$ multiplicative. Sum this identity over the finite family, and choose
$T$ sufficiently large. This proves (1).

## Why this is not yet a theorem about $S_4$

Every fixed canonical truncation satisfies (1). However, the number of quadratic
Frobenius classes used is $|G|-1$, and the total reciprocal-prime sum in (3) is
about $(|G|-1)T$. A core tuple outside the controlled family can acquire a
fallback factor of order $\exp((|G|-1)T)$. Enlarging the core to reduce its
weighted tail may enlarge $G$ drastically.

Thus the supplied cubic two-tail proof cannot simply be copied: its fallback
amplification is independent of the size of the controlled core, whereas that
uniformity has not been obtained here. Nor does positive complement density for
every finite truncation imply positive complement density or infinitude for
their infinite union.

This obstruction is resolved in [the full quartic proof](quartic_complement.md).
The distribution $f(g)=1-\sum_m c_m\chi_m(g)$, with fixed positive summable
$c_m$, gives class-dependent savings with a total reciprocal-prime budget
independent of the Galois rank. The remaining majorant requires eliminating
every principal quartic trace character, a larger class than square products
alone.

## Comparison with the independent quartic obstructions

Sections 5–8 of the
[independent record](independent/canonical_decomposition_and_quartic_zero_target.md)
describe genuine failures of more restricted approaches. Its conclusion that no
quartic infinitude theorem was obtained describes that separate investigation,
not the current research state. The checks below do not change the
[quartic complement argument](quartic_complement.md).

### Positive zero-target factors do occur

For the canonical tuple $(1,1,64,64)$, every odd-prime zero-target factor is
strictly greater than one. At $p\equiv3\pmod4$ its coefficient product is
square, giving $1+(p-1)/p^2$. At $p\equiv1\pmod4$, put
$\epsilon=\chi(-1)$ for a quartic character $\chi$, and $J=J(\chi,\chi)$.
The checked Gauss-sum expansion gives

$$
\rho_p(0)=1+\frac{p-1}{p^2}\left(B+2\Re(J^2/p)\right),
\qquad |J^2/p|=1.
$$

Since $\chi(64)=(2/p)$, the finite trace $B$ is $19$ when
$p\equiv1\pmod8$, and $11$ when $p\equiv5\pmod8$. Thus the traces lie
in $[17,21]$ and $[9,13]$, respectively. The pattern calculation agrees with
the [Euler-majorant expansion](quartic_euler_majorant.md).

This example is nevertheless excluded immediately by the successful
target $8\pmod{16}$: its values are only $0,1,2\pmod{16}$. Replacing the
last coefficients by $4,4$ preserves odd-prime local counts but requires
even new root variables. It is not an unrestricted integral or $2$-adic
equivalence. The analogous normalization of $(1,32,64,128)$ also does not
justify a universality claim.

More generally, the independent paired family consists of tuples equivalent,
under permutation, common positive rational scaling and individual rational
fourth-power scaling, to $(1,4,a,4a)$. Its good odd-prime zero-target factors
are all greater than one. For split primes, $\chi(4)=\epsilon$ gives pattern
$(1,\epsilon,z,\epsilon z)$: the finite traces are $19,7,3$ when
$\epsilon=1$, and $11,7$ when $\epsilon=-1$. The remaining Jacobi term has
absolute value at most $2$. At inert primes the coefficient product is
square, giving the positive quadratic trace.

Every paired tuple has square product, so it belongs to the class eliminated
by the reciprocity argument above. That argument uses $8\pmod{16}$ and
valuation-one targets at the coefficient primes, not only homogeneous
conditions at good primes. No reduction of all representations to the paired
family is needed.

### A checked global bound for the paired subfamily

The independent global bound is correct, although unnecessary for the
quartic theorem. For canonical coefficients, paired partners have the same
odd part and dyadic exponents $\{0,6\}$ or $\{5,7\}$. Let $\mathcal P$ be
the values represented by tuples admitting a partition into two such pairs.
Set

$$
L=1/\sqrt2+1/4,\quad
W=\prod_{p\text{ odd}}(1+p^{-5/2}+p^{-3}+p^{-7/2}),\quad
Z=\prod_{p\text{ odd}}(1+p^{-5}+p^{-6}+p^{-7}).
$$

A fixed ordered pair has total coefficient weight $LW$. Two different
pair partitions force all four odd parts to agree; the dyadic exponents
alternate between an allowed pair, giving weight

$$
\left(2\cdot2^{-3}+2\cdot2^{-6}\right)Z=\frac9{32}Z.
$$

All three partitions cannot hold, since three dyadic exponents cannot have
pairwise differences $2\pmod4$. Inclusion–exclusion therefore gives exact
ordered coefficient weight

$$
3L^2W^2-\frac{27}{32}Z.
$$

Lattice counting and the summable coefficient weights give the corresponding
ordered tuple asymptotic with factor $VX$, $V=\Gamma(5/4)^4$. Repeated actual
summands contribute $O(X^{3/4})$; all other permutation orbits have size $24$.
Consequently

$$
\overline d(\mathcal P)
\le\frac V{24}\left(3L^2W^2-\frac{27}{32}Z\right)<\frac14.
$$

For the strict inequality, $V\le1$, $L<1$, and, with
$f(t)=t^{-5/2}+t^{-3}+t^{-7/2}$,

$$
\log W\le f(3)+\tfrac12\int_3^\infty f(t)\,dt
=\frac7{108}+\frac{38}{135\sqrt3}<\frac14.
$$

Thus $W^2<\sqrt e<2$. This global upper density does not remain a relative
density bound after restricting to an arbitrarily sparse progression.
The separate reported bound $<1/200$ inside $15\pmod{16}$ depends on a
finite certificate not supplied with the independent record; its numerical
step has not been adopted here.

### Why the independent tail obstruction is bypassed

For target zero modulo $p$, a tuple with all four coefficients divisible by
$p$ has local factor $p$. A majorant ignoring this common-divisor factor is
indeed invalid. The independent repair involving
$\operatorname{rad}(\gcd(d_1,d_2,d_3,d_4))$ does give a summable majorant
uniformly for a fixed reciprocal-prime budget, but not uniformly as that
budget grows.

The successful proof instead imposes $F\equiv p\pmod{p^2}$. If all
coefficients are divisible by $p$, there are no solutions. Otherwise every
solution has a unit-coefficient unit variable, since canonical nonunit
coefficients and fourth powers of nonunit variables are divisible by $p^4$.
Nonsingular lifting and the one-variable root bound give
$\rho_{p^2}(p;\mathbf d)\le4$ at every coefficient prime. This explains the
smaller summable weight $4^{\omega(d_1d_2d_3d_4)}$ in the current proof.

For the regular tuples, the uniform Euler majorant is independent of the
small-prime cutoff. The later Frobenius distribution
$f(g)=1-\sum_m c_m\chi_m(g)$ has total reciprocal-prime budget at most $T+1$,
independent of the finite coefficient set. One first chooses $T$ using
dominated convergence, then the coefficient-prime cutoff $B$, and finally
the finite core $E$. Thus the fallback factor $e^{T+1}$ is fixed before the
tails are cut off. The independent record did not establish these ingredients.
The proof also eliminates mixed principal-character cases, not just square
products; its treatment of the remaining Jacobi term requires an upper
bound for a Hecke $L$-function, not angular prime equidistribution.

The independent record's more specific $32$-prescription optimization failure
has also been [reconstructed as an exact finite
obstruction](quartic_residue_obstruction.md). It applies only to that
target-$15$ safe objective, not to the construction used in the current proof.
The broader finite-character classification and the exploratory phase
optimizations in the independent record are not needed here and have not been
incorporated as established results.

## Comparison with the later random omission record

[The second independent record](independent/quartic_pattern_elimination_and_random_omission.md)
does obtain the full quartic theorem. Its
[checked random omission construction](quartic_random_omission.md) is an
alternative to the established bounded-budget distribution, not a stronger
conclusion. Its warning about a finite quadratic-character mask concerns the
equal-budget, nonidentity-Frobenius construction above. It is not a failure of
every finite-character method: the distribution $f(g)=1-\sum_m c_m\chi_m(g)$
already resolves that circularity.

Three diagnostic failures from its Section 9 are useful and check directly.

**Square-product elimination alone does not justify the Euler majorant.**
The canonical tuple $(1,1,1,32)$ has nonsquare product, but its mixed
monomial can be $32^2=4\cdot4^4$. It therefore has a principal mixed
quartic character. Its values are only $0,1,2,3\pmod{16}$, so the
successful target $8\pmod{16}$ excludes it. The general mixed-pattern
elimination, not merely square determinants, is necessary in the
[Euler-product proof](quartic_euler_majorant.md).

**Quaternion anisotropy does not imply a missing valuation class modulo
four.** For $F=x_1^4+x_2^4+64x_3^4+64x_4^4$, the positive inputs

$$
(1,2,1,1),\quad(1,1,1,1),\quad(4,4,1,2),\quad(4,4,1,1)
$$

give $145,130,1600,640$, with $2$-adic valuations $0,1,6,7$.
Every class modulo four occurs. This does not contradict exclusion of
the exact valuation three; indeed the values are only $0,1,2\pmod{16}$.
The successful argument forces local isotropy at the specified exact
valuations rather than asserting a general valuation-class gap.

**Making all coefficients fourth powers can remove the useful primes.**
At primes $p\equiv5\pmod8$, the Fermat quartic's finite trace is
$1+6-12=-5$, so its complete trace is at most $-3$. But a coefficient
$2^5$ being a fourth power forces $2$ itself to be a fourth power.
Among split primes this implies $(2/p)=1$, hence $p\equiv1\pmod8$.
Thus the cubic all-coefficients-splitting strategy cannot simply retain
this Fermat deficit in degree four. Neither quartic completion uses
that strategy.

The independent numerical Euler products are explicitly uncertified
diagnostics and are not adopted as proof inputs. The existing
[target-$15$ finite certificate](quartic_residue_obstruction.md)
concerns a different restricted objective and obstructs neither proof.

## Odd-valuation support and a sharper exceptional tail

Appendix B of
[third independent record](independent/quartic_analytic_architecture.md)
correctly strengthens square-product elimination: only odd primes having an
**odd valuation in some coefficient** need be prescribed. Square factors at
arbitrarily large primes do not require new congruences. The same refinement
also holds for the mixed principal-character cases, although the independent
Appendix C states only full-support elimination.

To check this, let $P$ contain all odd primes having an odd coefficient
valuation, and use (2). At primes in $P$ and at $2$, the established
local lifting arguments are unchanged. At an odd prime outside $P$,
all coefficient valuations of $Q=\langle d_1,d_2,d_3,d_4\rangle$ are
even; rescaling its coordinates removes those valuations and gives a
unit form, which is isotropic.

For a mixed case write

$$
d_k=cu^2,\quad d_l=cv^2,\quad
d_i^2d_j^2d_kd_l^3\in4\mathbb Q^{\times4}.
$$

Here $c$ is positive squarefree and $u,v$ are positive integers.
The established identity gives the square-determinant form
$Q'=\langle d_i,d_j,c,2cuv\rangle$ and
$d_i d_j uv=2s^2$ for some rational $s$.
At an odd prime outside $P$, $c$ is a unit and the last identity makes
$v_p(uv)$ even. Thus every coefficient of $Q'$ has even valuation too,
so coordinate rescaling gives a unit form. All finite places are
isotropic, contradicting the same quaternion reciprocity theorem.
This proves the refinement for the entire exceptional family of the
[full quartic proof](quartic_complement.md), not just square products.

There is also a sharper tail for canonical tuples
$\mathbf d\in\mathcal C_4^4$. For fixed $\kappa\ge1$, put

$$
w_\kappa(\mathbf d)=
(d_1d_2d_3d_4)^{-1/4}\kappa^{\sum_i\omega(d_i)}.
$$

Then

$$
\sum_{\substack{\mathbf d\text{ exceptional}\\
\exists p>Y,\ i:\ v_p(d_i)\text{ odd}}}
w_\kappa(\mathbf d)\ll_\kappa Y^{-3/2}\qquad(Y\ge3).
\tag{6}
$$

For square-product tuples an odd local exponent occurs at least twice.
For a mixed tuple, its exponents $e_h\in\{0,5,6,7\}$ at an odd prime
satisfy

$$
2e_i+2e_j+e_k+3e_l\equiv0\pmod4.
$$

A vector having just one nonzero exponent, that exponent odd, cannot
satisfy this congruence. Thus every exceptional tuple in the event at
$p$ has at least two nonzero local exponents, of total at least ten.
Its local weight is $O_\kappa(p^{-5/2})$ even if the exceptional
condition is dropped at all other primes. The unrestricted Euler product
of the other local weights converges. A union bound and
$\sum_{p>Y}p^{-5/2}\ll Y^{-3/2}$ prove (6).

Prescribe all odd primes at most $Y$. Survivors in the exceptional
family must belong to (6), whereas their local factors are at most
$C4^{\omega(d_1d_2d_3d_4)}(\log(2Y))^{21}$ by the checked trace bound.
Their total weighted local mass is consequently
$O(Y^{-3/2}(\log(2Y))^{21})=o(1)$.
This controls the entire exceptional stratum without a Hecke bound;
regular tuples still need the separate suppression argument.

The independent Appendix B uses the weaker elementary logarithmic
exponent $81e$, while its summary writes $81$. Either exponent suffices
for its conclusion; the existing trace and prime-harmonic estimates give
the exponent $21$ used here.

### A negative one-prime average cannot be iterated

Section 6 of the third record averages over four independent coefficient
choices, each with dyadic weights $1,2^{-5/4},2^{-6/4},2^{-7/4}$, at a prime
$q\equiv5\pmod8$, with $\chi_4(2)=i$ and all odd coefficient parts
fourth residues. Its displayed mean formula is the direct average of
the nineteen finite-character terms. It is an average over **tuples**,
not independence of the local factors as the prime varies.

The fixed positive-weight tuple $(1,1,64,64)$ already proves the failure
of such iteration: at every prime with this prescription it has finite
trace $11$, hence total trace at least nine. Its contribution grows
when the reciprocal-prime budget diverges, despite a negative one-prime
mean over all tuples. This tuple is excluded by $8\pmod{16}$ (and also
by $15\pmod{16}$). Conditioning on either dyadic target changes the
weights, so this example obstructs only the unconditioned averaging
argument, not the successful proof or the separate target-$15$
certificate.

The finite-core circularity described in the same independent section
is likewise the old equal-budget obstruction, already resolved by
the bounded-budget distribution. The newly checked
[universal selector](quartic_universal_selector.md) is another resolution,
not evidence that every finite-character construction fails.

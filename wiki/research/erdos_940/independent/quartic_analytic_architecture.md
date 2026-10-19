---
name: research/erdos_940/independent/quartic_analytic_architecture
title: 'Independent record: Erdős Problem 940'
desc: Unverified independent record; the universal selector and local refinements were checked separately in the topical notes.
tags: []
sources: []
created: 2026-09-23T00:35:02Z
updated: 2026-10-13T05:28:09Z
---


# Independent record: Erdős Problem 940

***

The working files this record names (`positive_density_reduction.md`,
`r4_local_elimination.md` and `r4_principal_character_elimination.md`) were
not retained; the names are kept so the citations stay readable, and the
retained re-derivations are the topical notes of this folder.

## Status

This document records an investigation from scratch, using the canonical problem
page and the supplied papers. There was no browsing and no use of earlier
research notes. References in supplied digests to other “current research” were
not treated as available results.

**No complete resolution of an open part is claimed in this record.** The
investigation produced a concrete proposed proof of a positive-lower-density
complement for **$S_4$**. Its local algebraic steps and fixed-modulus transfer
were checked. Analytic supporting lemmas were written by separate authors, but
the complete assembled proof did not receive a final independent verification.
The proposed theorem is therefore distinguished from the established components
below. This is not a density-zero proof.

The different questions retain the following status in this record:

* $r=3$: Beyer de Ryke's positive-lower-density complement theorem is accepted
  background and was not re-audited. Density zero of $S_3$ is unresolved here.
* $r=4$: substantial local elimination, a full treatment of the square-product
  kernel stratum, and an explicit proposed completion for the full sumset.
  Neither an unconditional theorem about the full $S_4$ nor density zero is
  claimed here.
* $r\geq5$: neither requested assertion was established.
* No unconditional positive-density construction for any $S_r$ was
  established.

The appendices reproduce the actual supporting working files. Claims in those
files concern their stated auxiliary lemmas; their conjunction has not been
silently promoted to a completed theorem.

## 1. Established canonical reduction

Write $P_r$ for the positive $r$-powerful integers and

$$
\mathcal C_r=\left\{\prod_p p^{e_p}:e_p\in\{0,r+1,\ldots,2r-1\}\right\}.
$$

Every $m\in P_r$ has a unique expression $m=dx^r$, $d\in\mathcal C_r$,
$x\geq1$. This follows by reducing its prime exponents modulo $r$, retaining
$r+j$ in the kernel when the residue is $j\ne0$.

The convergent weight is

$$
W_r=\sum_{d\in\mathcal C_r}d^{-1/r}
=\prod_p\left(1+\sum_{j=1}^{r-1}p^{-1-j/r}\right)<\infty.
$$

Thus $\#(P_r\cap[1,X])\leq W_rX^{1/r}$. Fewer than $r$ summands contribute
$O_r(X^{(r-1)/r})$ values. If
$U_r(Y)=\sum_{d>Y,\ d\in\mathcal C_r}d^{-1/r}$, ordered $r$-tuples with at
least one kernel exceeding $Y$, and all summands at most $X$, number at most

$$
rW_r^{r-1}U_r(Y)X. \tag{1}
$$


A proved consequence is the equivalence:

$$
d(S_r)=0
\quad\Longleftrightarrow\quad
d\bigl(\{\sum_{i=1}^r c_ix_i^r:x_i\geq1\}\bigr)=0
\quad\hbox{for every fixed }\mathbf c\in\mathbb N_{>0}^r.
$$

For the reverse implication use the finite-kernel truncation and (1). For the
forward implication multiply a fixed coefficient vector by
$L=(c_1\cdots c_r)^r$; every $Lc_i$ is $r$-powerful, so its scaled value
set is a subset of $S_r$.

In particular, positive upper density of $S_r$ would already imply positive
upper density for some fixed positive diagonal degree-$r$ form in $r$
variables. This does not assert existence of natural density. It prevents a
purported positive-density construction from relying essentially on kernels
tending to infinity. Full proof: Appendix A.

## 2. Proved quartic elimination: first square products, then all principal terms

For $r=4$, kernels have prime exponents $0,5,6,7$. For a finite set $P$
of odd primes choose

$$
B_P=16\prod_{p\in P}p^2,\qquad
a_P\equiv8\pmod {16},\qquad a_P\equiv p\pmod {p^2}\quad(p\in P). \tag{2}
$$


### Square-product lemma

If the kernel tuple is supported on $P\cup\{2\}$ and $\prod_i d_i$ is
square, then $F_{\mathbf d}(x)=\sum_i d_ix_i^4\equiv a_P\pmod{B_P}$ is
impossible.

Indeed put $Q(z)=\sum d_iz_i^2$, $z_i=x_i^2$. At an odd $p\in P$, the
target valuation $1$ forces an original summand to be a unit, since every
nonunit summand has valuation at least $4$. There is consequently a unit
derivative of $Q$, and Hensel lifting gives a nonzero $p$-adic zero. At
$2$, target valuation $3$ forces an odd summand, so the derivative valuation
is $1$; strong Hensel applies because $3>2$. At other odd primes $Q$ is
unimodular of dimension four and is isotropic.

A positive definite quaternary form of square determinant is similar to
$\langle1,B,C,BC\rangle$, the norm of the quaternion algebra $(-B,-C)$.
The preceding isotropy makes the quaternion algebra split at every finite
place, while positivity makes it ramified at infinity, contradicting Hilbert
reciprocity. This uses Proposition 14.2.1 and Corollary 14.2.3 of the supplied
Voight chapter, whose full Markdown was read.

### Extension to every principal finite character

Ghidelli's exact quartic count, for $q\equiv1\pmod4$ away from the
coefficients, is

$$
N_q(\mathbf d)=q^3+q(q-1)(K_{\mathbf d}(q)+2\Re H_{\mathbf d}(q)). \tag{3}
$$

The nineteen finite-character terms of $K$, all with coefficient $1$, have
quartic-symbol arguments

$$
A^2;\quad d_id_jd_k^3d_l^3\ (6\text{ terms});\quad
-d_i^2d_j^2d_kd_l^3\ (12\text{ terms}),\qquad A=\prod_i d_i. \tag{4}
$$

The $H$-term is a Gaussian Hecke character of infinity type $2$.
For $q\equiv3\pmod4$,

$$
N_q(\mathbf d)=q^3+(A/q)q(q-1). \tag{5}
$$

The full supplied Ghidelli Markdown, not merely the digest, was read.

Principality in the first seven terms forces $A$ square. The remaining case
has

$$
d_i^2d_j^2d_kd_l^3=4t^4.
$$

Write $d_k=cu^2,d_l=cv^2$, with $c$ positive squarefree. Then
$d_id_j uv=2s^2$, where $s=t/(cv)$, and

$$
d_kx_k^4+d_lx_l^4
=c(ux_k^2-vx_l^2)^2+2cuv(x_kx_l)^2. \tag{6}
$$

Thus $F_{\mathbf d}$ is represented by the positive square-determinant form

$$
Q'=\langle d_i,d_j,c,2cuv\rangle.
$$

The same local contradiction applies. At an odd support prime, an original unit
summand gives a unit coefficient-coordinate of $Q'$: if the unit is in the
last pair, use either $ux_k^2-vx_l^2$ or $x_kx_l$.
At $2$, if neither of the first two summands is odd and both of the last two
are odd, their sum is $2c\pmod8$, contradicting the target. In the remaining
cases $Q'$ has an odd coefficient-coordinate, and strong Hensel again applies.

Therefore (2) eliminates **every supported tuple with any principal term in
(4)**, not just square-product tuples. This distinction is necessary:
$(1,32,1,1)$ has nonsquare determinant but a principal term of the last type.
Detailed proofs, independently checked at the local level: Appendices B and C.

## 3. Exact local factors and summable weights

Every selected odd prime must use modulus $p^2$, with target $p\pmod{p^2}$.
If $t$ coefficients are units at $p$, and $N_{p,t}$ counts zeros of the
active $t$-variable form modulo $p$, its normalized density is

$$
\rho_{p^2}(\mathbf d)=
\frac{N_{p,t}-1}{p^{t-1}}\quad(t\geq1), \tag{7}
$$

and is zero for $t=0$. The nonzero zeros lift nonsingularly, whereas the
origin cannot lift to target valuation $1$. Inactive coefficients vanish
modulo $p^2$. Formula (7) follows by counting the lifts, including the free
inactive coordinates. It is at most $4$, by fixing all but one active
variable.

At a good prime this becomes $(N_p-1)/p^3$. At $2$, the normalized factor
modulo $16$ is at most $16$. Using only modulus $p$ at an all-bad prime
would instead give factor $p$, a real error avoided by (7).

Set

$$
R=\operatorname{rad}(d_1d_2d_3d_4),\qquad
w(\mathbf d)=(d_1d_2d_3d_4)^{-1/4}.
$$

For every fixed $C$ and $\theta<1/4$,

$$
\sum_{\mathbf d\in\mathcal C_4^4}
w(\mathbf d)C^{\sum_i\omega(d_i)}R^\theta<\infty. \tag{8}
$$

The nonconstant local Euler term is $O_C(p^{-5/4+\theta})$. Any completed
analytic argument must respect this exponent margin.

The entire square-product stratum can already be treated. At a prime, let
$a_p=1+C p^{-3/2}$, $b_p=C(p^{-5/4}+p^{-7/4})$.
Its square-product local weight is

$$
a_p^4+6a_p^2b_p^2+b_p^4.
$$

An odd valuation must occur in at least two coordinates, so that event has
weight $O_C(p^{-5/2})$. The weighted tail with an odd-valuation prime $>Y$
is consequently $O_C(Y^{-3/2})$. Such primes are the only support primes
needed in the square-product elimination, because even coefficient valuations
can be removed from the quadratic form by rescaling.

Prescribing (2) at all odd primes up to $Y$, the total local weighted mass of
surviving square-product tuples is therefore at most

$$
O((\log(2Y))^{81}Y^{-3/2})=o(1).
$$

Here a crude Gauss-sum estimate gives $1+81/p$ at good primes, and (7) handles
bad primes. This yields arbitrarily small upper relative density for the
square-product stratum in suitable progressions. It does not yet say this about
the full $S_4$. Appendix B includes the proof.

## 4. Proposed analytic completion of the full $r=4$ argument

This section states the precise assembly that was not finally certified.
The supporting analytic proofs are included in Appendices
D and E so another mathematician can check them rather than reconstruct them.

### 4.1. Baseline bound

The needed estimate for tuples with **no principal term in (4)** is

$$
\prod_{\substack{p\leq Z\\p\text{ odd}}}\rho_{p^2}(\mathbf d)
\ll_\eta C^{\sum_i\omega(d_i)}R^\eta
\quad\text{for every }\eta>0,\text{ uniformly in }Z. \tag{B}
$$

The proposed proof is positive Euler-product factorization, using upper bounds
only. The determinant character occurs at all rational odd primes through
(3) and (5); the other terms pair into Gaussian characters. Inert Gaussian
primes have norm $p^2$, hence bounded contribution. All the relevant
nonprincipal $L$-functions then occur with positive powers.

The baseline working file claims, more precisely, a bound

$$
C[\log(2R)]^{11-m}[\log(2Z)]^m,
$$

where $m\leq10$ counts the principal contributions after conjugate pairing.
The full elimination removes $m>0$ tuples whose support lies below $Z$.

The proposed uniform proof uses a defining modulus $(32R)$. At odd Gaussian
primes, an order-four character is trivial on principal units; at $1+i$, units
$1\pmod{(1+i)^9}$ are fourth powers by Hensel. The fixed Jacobi character has
defining ideal $(16)$. For infinity type $k=0$ or $2$, write
$\psi((z))=\nu(z)(z/|z|)^k$ with periodic finite factor $\nu$.
Residue/lattice cancellation gives a coefficient partial sum bounded by a
constant times $m\sqrt{x}$ for $x\geq m^2$, $m=32R$. Splitting the
Dirichlet series at $m^2$ gives $|L(\sigma,\psi)|\ll\log(2m)$ for
$1<\sigma\leq2$. Prime-sum smoothing then gives (B).

The points requiring final verification are the uniform lattice estimate, the
local conductor reduction, and the precise positive Euler-factor bookkeeping.
Ghidelli's fixed-character prime-number theorem by itself is not enough:
its constants depend on the character.

### 4.2. A single universal selector for all nonsquare determinants

For positive squarefree $E>1$, choose $\lambda_E=c/E^2$ with a fixed small
$c>0$, and for primes $p\equiv3\pmod4$ choose independent selectors of mean

$$
g(p)=\delta\left(1-\sum_E\lambda_E(E/p)\right),\qquad 0<\delta<1/2. \tag{9}
$$

Take $c$ so $\sum\lambda_E<1/2$; also
$\sum\lambda_E\log(2E)<\infty$.
A completed selector lemma must give one realization $\mathcal P$, not a
different realization for each determinant, with:

1. Uniformly in positive squarefree $D>1$ and $2\leq Z<T$,

$$
\prod_{\substack{Z<p\leq T\\p\in\mathcal P}}
(1+(D/p)(p^{-1}-p^{-2}))\ll_\theta D^\theta, \tag{S1}
$$

   where $\theta>0$ is arbitrarily small by choosing $\delta$ small.
2. For every fixed $D>1$, this product tends to zero on the moving interval
   $Z=(\log T)^{A_0}$, for any fixed $A_0>0$. $\tag{S2}$

The mechanism is a negative expectation for each nontrivial determinant:

$$
\sum_{p\leq T,\ p\equiv3(4)} g(p)(D/p)/p
=-\frac{\delta\lambda_D}{2}\log\log T+o_D(\log\log T).
$$

The $E=D$ term is the sole principal correlation. The sum over $E$ must be
justified by truncation or a uniformly summable bound. Removing primes up to
$(\log T)^{A_0}$ costs only $O(\log\log\log T)$.

Uniform upper bounds use

$$
\left|\sum_{p\leq x}\chi(p)/p\right|\ll\log(2q) \tag{Q}
$$

for nonprincipal real Dirichlet characters of modulus $q$, uniformly in $x$.
In the expanded expectation the only principal term has a negative coefficient,
so it can be discarded for an upper bound. Every other term is controlled by
(Q); the weighted conductor losses sum because
$\sum_E\lambda_E\log(2E)<\infty$.

Centered selector sums have squared increment bounds summing to
$\sum_p p^{-2}<\infty$. A maximal Hoeffding/exponential-martingale estimate
should give a tail $O(e^{-ct^2})$ for the supremum over all cutoffs. Set
$t=K+\epsilon\log(2D)$, sum these bounds over $D$, and take $K$ large.
There is then one realization with all-$D$, all-cutoff discrepancy
$O_\epsilon(1)+\epsilon\log(2D)$. Interval errors cost twice a prefix error.
This both preserves fixed-$D$ decay and gives (S1).

Appendix E contains the selector proof, written by a separate author. Its
statement is somewhat stronger than needed here; only the polylogarithmic lower
cutoff is used in this proposed completion.

### 4.3. Avoiding an unprovided Siegel bound in (Q)

The proposed elementary proof of (Q) is retained because mere fixed-character
convergence does not supply a summable uniform bound.

For primitive odd real $\chi$ of conductor $q$, finite Fourier expansion
gives

$$
L(1,\chi)=-\pi q^{-3/2}\sum_{a=1}^{q-1}a\chi(a).
$$

The nonzero integer numerator gives a polynomial lower bound. For even $\chi$,

$$
U=\prod_{a\in(\mathbb Z/q\mathbb Z)^\times}(1-\zeta_q^a)^{\chi(a)}
$$

is intended to be a positive norm-one quadratic unit, with
$L(1,\chi)=-q^{-1/2}\log U$. Since $U\ne1$, its integer trace gives
$|\log U|\geq\log((3+\sqrt5)/2)$. The unit assertion uses cancellation of
the common cyclotomic prime factor at prime-power conductor.
Nonvanishing can be supplied by a fixed-character theorem in the sources,
or by Landau's nonnegative-coefficient argument for $\zeta(s)L(s,\chi)$.

Character partial sums give $L'(\sigma,\chi)\ll\log^2(2q)$ near $1$.
Together with

$$
L(\sigma,\chi)\geq\zeta(2\sigma)/\zeta(\sigma)\gg\sigma-1
$$

this yields a polynomial conductor lower bound uniformly for $1<\sigma\leq2$.
Imprimitive factors cost another polynomial. Upper bounds are elementary.
Finally, at $\sigma=1+1/\log x$, Chebyshev's prime upper bound makes the
difference between the truncated harmonic prime sum and $\log L(\sigma,\chi)$
bounded uniformly. This gives (Q).

These details are written in Appendix E, but were not all independently
verified by the author. No Siegel theorem or unproved GRH
assumption is being silently used.

## 5. Conditional assembly, with the infinite-kernel reduction proved

Assume the uniform statements (B), (S1), and (S2) have been fully verified.
Let $Z=(\log T)^{A_0}$, and prescribe (2) at all odd primes at most $Z$
and at selected primes in $(Z,T]$. Write $M_T,a_T$ for the resulting
modulus and target, and $\rho_T(\mathbf d)$ for the normalized local density.

For a nonexceptional tuple the squarefree determinant part $D$ is nontrivial:
otherwise the first character in (4) is principal. At good selected primes,

$$
\rho_{p^2}(\mathbf d)
=1+(D/p)(p^{-1}-p^{-2})-p^{-3}.
$$

Thus (B) and (S1) give a bound

$$
\rho_T(\mathbf d)\ll C^{\sum\omega(d_i)}R^\theta,\qquad \theta<1/4, \tag{10}
$$

by taking the small exponents appropriately. Deleting coefficient-dividing
primes costs only another exponential in $\omega(R)$, by (7).
For each fixed such tuple, (S2) makes $\rho_T(\mathbf d)\to0$.

For an exceptional tuple, if its support is below $Z$, elimination gives
$\rho_T=0$. A surviving tuple has $R>Z$. The crude bound

$$
\rho_T(\mathbf d)\ll C^{\sum\omega(d_i)}(\log(2T))^{81}
$$

is absorbed in (10) by choosing $A_0$ sufficiently large. Each fixed
exceptional tuple eventually vanishes.

Equation (8) would therefore be a single summable majorant, independent of
$T$. Dominated convergence would give

$$
\sum_{\mathbf d\in\mathcal C_4^4} w(\mathbf d)\rho_T(\mathbf d)\longrightarrow0.
\tag{11}
$$

This is the essential full-sumset statement, not a bound on a narrower equation.

Here is the proved transfer from (11). Fix one modulus $M$ and target $a$.
For a fixed tuple, count residue classes in $1\leq x_i\leq(X/d_i)^{1/4}$. The
positive quartic region is inside that box, so

$$
\limsup_{X\to\infty}\frac M X
\#\{x_i\geq1:F_{\mathbf d}(x)\leq X,\ F_{\mathbf d}(x)\equiv a(M)\}
\leq w(\mathbf d)\rho_M(\mathbf d).
$$

To sum this, first restrict to finitely many kernels. The remaining normalized
count is at most $M$ times the raw summable kernel weight; let the finite
set increase while $M$ stays fixed. Fewer than four summands contribute
$O(X^{3/4})$. There is no need for an estimate uniform in a growing modulus.

If (11) were certified, choose a single finite $T$ with its weighted sum
below $1/2$. Then

$$
\underline d(\mathbb N\setminus S_4)\geq 1/(2M_T)>0.
$$

Order of limits: choose $T$, then $X\to\infty$, then remove a kernel
truncation with $M_T$ fixed. This conclusion would settle infinitude for
$r=4$, but would not prove density zero of $S_4$.

## 6. Calculations and approaches that did not resolve an open part

### Total tuple counts

The natural unordered tuple constant is
$\Gamma(1+1/r)^rW_r^r/r!$, not automatically less than one.
Euler products truncated at primes below $10^6$ gave:

| $r$ | truncated $W_r$ | corresponding constant |
|---|---:|---:|
| 3 | 4.6507 | 11.9379 |
| 4 | 9.5971 | 238.5820 |
| 5 | 19.0925 | 13795.6 |
| 6 | 36.7496 | 2181147.8 |

These were exploratory computations, not rigorous upper bounds. They do not
prove anything about the complement.

### A negative one-prime mean that cannot be multiplied

At $q\equiv5\pmod8$, with all relevant odd coefficients fourth residues and
$\chi_4(2)=i$, the four canonical 2-adic weights are
$1,2^{-5/4},2^{-3/2},2^{-7/4}$. Divide by their sum $B$, and set

$$
z_1=\frac{1-2^{-3/2}+i(2^{-5/4}-2^{-7/4})}{B},\qquad
z_2=\frac{1+2^{-3/2}-2^{-5/4}-2^{-7/4}}{B}.
$$

The mean $K$ is

$$
6|z_1|^4-12|z_1|^2z_2^2+z_2^4\approx-0.044,
$$

whereas the possible $H$-contribution has absolute value at most
$2|z_1|^4\approx0.0204$. This negative one-prime mean is not an iterable
independence statement: the coefficient classes remain fixed, and positive
$K$ strata can dominate repeated products. The tuple $(1,1,64,64)$ is
one obstruction.

Forcing every coefficient to be a fourth residue also fails: the powers of 2 in
a sufficiently rich core force primes $1\pmod8$, where the equal-coefficient
quartic has $K=19$, rather than the $K=-5$ at primes $5\pmod8$.

### Finite-core multiquadratic selection and circular constants

For a finite real multiquadratic field with group $G$, summing any nontrivial
quadratic character over nonidentity elements gives $-1$. Thus primes
$3\pmod4$ with nonidentity Frobenius suppress every nonsquare determinant
in that finite core.

The unresolved issue in that version is the tail: its bounds depend on the
core field, and enlarging the core changes the constants, potentially
exponentially. Square-product tuples also have positive local drift until
eliminated. A naive two-tail argument is circular. The universal selector
(9) was proposed to remove the dependence on a changing finite core.

### Positive-density attempts and the Perazzo mismatch

For cube collisions, let $u_i=x_i-y_i$, $v_i=x_i+y_i$. Then

$$
4\sum_i c_i(x_i^3-y_i^3)
=\sum_i c_i u_i(3v_i^2+u_i^2).
$$

The extra $\sum c_i u_i^3$ cannot be discarded to use the supplied Perazzo
theorem. Moreover the six-variable diagonal cubic is projectively smooth,
whereas the Perazzo hypersurface is singular along a plane, ruling out an
invertible linear identification. No valid nonlinear reduction was found.

An $O(B^3)$ equal-three-cube energy bound would give positive lower density
by Cauchy--Schwarz, hence refute density zero for $S_3$. No unconditional
such bound was established. The conditional Wang theorem was not presented
as an unconditional result.

Norm-form ideas likewise did not produce a fixed critical diagonal form with
known positive-density values. The finite-kernel equivalence prevents avoiding
that difficulty merely by introducing unbounded auxiliary kernels.

### Other scope limitations

Primitive $a+b=c$ estimates where all three entries are powerful do not
bound representations of arbitrary targets. Fixed quadratic-fiber bounds do
not control all targets after summing kernels. Gaps in a perfect-power subset
need not be gaps in the larger powerful-number sumset. No such reduction was
asserted.

For $r\geq5$, the good-prime deviations of fixed critical diagonal forms are
summable at the relevant local scale. No replacement for the cubic/quartic
divergent local saving was found. This is a limitation of a method, not a
negative answer to the problem.

## 7. Precise remaining uncertainty

The algebraic elimination and the fixed-modulus transfer had passed
independent checks. The two analytic component files had just been completed.
The proposed full $r=4$ argument still needed a final check of:

1. All conductor-uniform details of the Gaussian baseline lemma, including
   the positive-character multiplicities and the lattice estimate.
2. The quadratic Fourier/unit/nonvanishing chain, imprimitive Euler factors,
   and its uniformity in the partial Euler cutoff.
3. The maximal probabilistic estimate, a single realization for every
   determinant and cutoff, and summation of the infinite character mixture.
4. The complete assembly of constants in (10), ensuring a coefficient weight
   genuinely summable as in (8), with no hidden dependence on $T$.

The attached proofs make these concrete verification tasks, rather than an
unspecified wish for a stronger counting theorem. However the independent
audit explicitly did not certify their conjunction.
Accordingly (11) and the claimed consequence for the full $S_4$ are retained
as a proposed completion, not announced as a solved case.

## Appendices: complete working proofs and audit

The following files are reproduced verbatim below. Their labels and any claims
of completion apply to their own auxiliary statements only.



---

## Appendix A. Finite-coefficient density reduction

Source working file: positive_density_reduction.md

## A finite-coefficient reduction for the density question

Fix an integer $r\geq 3$, and let $\mathcal P_r$ be the positive
$r$-powerful integers. Put

$$
\mathcal B_r=\left\{\prod_p p^{e_p}:e_p\in\{0,r+1,\ldots,2r-1\}\right\}.
$$

All products here have finite support. For a positive integer vector
$\mathbf c=(c_1,\ldots,c_r)$, define

$$
V_{r,\mathbf c}=\{c_1x_1^r+\cdots+c_rx_r^r:x_1,\ldots,x_r\geq1\}.
$$


**Proposition.** The following assertions are equivalent:

1. $S_r$ has natural density zero.
2. Every $V_{r,\mathbf c}$, with $\mathbf c\in\mathbb N^r$ fixed, has
   natural density zero.
3. Every $V_{r,\mathbf b}$, with $\mathbf b\in\mathcal B_r^r$ fixed,
   has natural density zero.

In particular, $S_r$ has positive upper natural density if and only if
at least one fixed positive diagonal degree-$r$ form in $r$ variables has
a value set of positive upper natural density.

*Proof.* Every $a\in\mathcal P_r$ has a unique decomposition
$a=bx^r$ with $b\in\mathcal B_r$ and $x\geq1$. Indeed, write each
nonzero prime exponent as $e=qr+s$, where $0\leq s<r$. If $s=0$,
put the entire exponent into $x^r$. If $s>0$, then $q\geq1$, and put
the exponent $r+s$ into $b$ and the remaining exponent $(q-1)r$ into
$x^r$. This construction is forced by the permitted exponents of $b$.

The constant

$$
C_r=\sum_{b\in\mathcal B_r}b^{-1/r}
=\prod_p\left(1+\sum_{s=1}^{r-1}p^{-1-s/r}\right)
$$

is finite: the sum over primes of the nonconstant terms is bounded by
$(r-1)\sum_{n\geq2}n^{-1-1/r}<\infty$. Consequently,

$$
\#(\mathcal P_r\cap[1,X])
=\sum_{b\in\mathcal B_r}\left\lfloor (X/b)^{1/r}\right\rfloor
\leq C_rX^{1/r},
$$

where terms with $b>X$ contribute zero. If

$$
T_r(Y)=\sum_{\substack{b\in\mathcal B_r\\b>Y}}b^{-1/r},
$$

then the number of $a\leq X$ whose unique kernel exceeds $Y$ is at most
$X^{1/r}T_r(Y)$, and $T_r(Y)\to0$.

The sums with fewer than $r$ positive summands form a set of size at
most

$$
\sum_{j=1}^{r-1}(C_rX^{1/r})^j=O_r(X^{(r-1)/r}).
$$

For exactly $r$ summands, the number of ordered representations having
at least one kernel exceeding $Y$ is at most

$$
r\big(C_rX^{1/r}\big)^{r-1}X^{1/r}T_r(Y)
=rC_r^{r-1}T_r(Y)X.
$$

All other represented integers belong to the finite union

$$
\bigcup_{\mathbf b\in(\mathcal B_r\cap[1,Y])^r}V_{r,\mathbf b}.
$$

If (3) holds, this finite union has density zero. Dividing the preceding
estimates by $X$, letting $X\to\infty$, and then letting $Y\to\infty$
proves (1).

For (1)$\Rightarrow$(2), fix $\mathbf c$ and set
$L=(c_1\cdots c_r)^r$. Every $Lc_i$ is $r$-powerful: any prime
dividing it already divides $c_1\cdots c_r$ and therefore occurs in $L$
to exponent at least $r$. Hence every $Lc_ix_i^r$ is $r$-powerful, so
$LV_{r,\mathbf c}\subseteq S_r$. Thus

$$
\#(V_{r,\mathbf c}\cap[1,X])
\leq\#(S_r\cap[1,LX])=o(X).
$$

The implication (2)$\Rightarrow$(3) is immediate. Since a subset of
$\mathbb N$ fails to have density zero exactly when its upper density
is positive, the final equivalence follows. $\square$

This proposition does not prove either outcome of the density question.
It prevents a positive-density construction from depending essentially
on kernels tending to infinity: such kernels have arbitrarily small
total first-moment mass. It also shows that the density question is not
reduced merely to the equal-coefficient form. A positive-density theorem
for any fixed positive coefficient vector would suffice to disprove the
density-zero assertion for $S_r$.

### The elementary obstruction to a Perazzo substitution

For three-cube collisions, put $u_i=x_i-y_i$ and $v_i=x_i+y_i$.
Then

$$
4\sum_{i=1}^3c_i(x_i^3-y_i^3)
=\sum_{i=1}^3 c_i u_i(3v_i^2+u_i^2).
$$

The collision equation is therefore

$$
3\sum_{i=1}^3c_i u_i v_i^2+\sum_{i=1}^3c_i u_i^3=0,
$$

not the Perazzo equation $\sum_i u_iv_i^2=0$.
Moreover, the projective hypersurface
$\sum_i c_i(x_i^3-y_i^3)=0$ is smooth in characteristic zero, since all
six partial derivatives vanish only at the zero vector. The Perazzo
hypersurface is singular along the plane $v_1=v_2=v_3=0$.
An invertible linear substitution cannot identify these hypersurfaces,
since it preserves smoothness. This does not exclude nonlinear
reductions, but no such reduction is established here.

No theorem from a supplied paper is invoked in these arguments.


---

## Appendix B. Square-product local elimination and full stratum

Source working file: r4_local_elimination.md

## A local elimination lemma for square-product quartic kernels

Let

$$
\mathcal C_4=\{b_1^5b_2^6b_3^7:b_1b_2b_3\text{ is squarefree}\}.
$$

Every 4-powerful positive integer has a unique expression $dx^4$, with
$d\in\mathcal C_4$ and $x\geq1$. Indeed, a nonzero prime exponent
is uniquely $4u$, $4u+5$, $4u+6$, or $4u+7$, according to its
residue modulo 4. In particular, every nonzero valuation of a kernel
$d\in\mathcal C_4$ is at least 5.

### Lemma

Let $P$ be a finite set of odd primes. Put

$$
B_P=16\prod_{p\in P}p^2,
$$

and choose $a_P\bmod B_P$ by

$$
a_P\equiv8\pmod {16},\qquad a_P\equiv p\pmod {p^2}\quad(p\in P).
$$

Let $d_1,\dots,d_4\in\mathcal C_4$, suppose every odd prime having
odd valuation in at least one $d_i$ belongs to $P$, and suppose
$d_1d_2d_3d_4\in\mathbb Q^{\times2}$. Then the congruence

$$
d_1x_1^4+\cdots+d_4x_4^4\equiv a_P\pmod {B_P}
$$

has no integer solution. The same conclusion holds for any positive integral
coefficients $d_i$ whose nonzero prime valuations are at least 4.

#### Proof

Assume a solution, write $n=\sum_i d_ix_i^4$, and put
$Q(z)=\sum_i d_iz_i^2$. For every $p\in P$, we have $v_p(n)=1$.
There is an index $j$ with $p\nmid d_jx_j$: otherwise each summand
would be divisible by $p^4$, contrary to $v_p(n)=1$. At the vector
$z_i=x_i^2$, the equation $Q(z)\equiv0\pmod p$ therefore has a
nonzero partial derivative $2d_jz_j\pmod p$. Hensel's lemma, varying
only $z_j$, gives a nonzero isotropic vector for $Q$ over
$\mathbb Q_p$.

At 2, $v_2(n)=3$, so again some $d_jx_j$ is odd; otherwise all
summands would be divisible by 16. Fix all coordinates other than $z_j$
and let

$$
f(T)=d_jT^2+\sum_{i\ne j}d_ix_i^4.
$$

Then $v_2(f(x_j^2))=3$ and $v_2(f'(x_j^2))=1$. The usual strong
form of Hensel's lemma, whose hypothesis is
$v_2(f(t))>2v_2(f'(t))$, produces a root congruent to the odd number
$x_j^2\pmod2$. Thus $Q$ is isotropic over $\mathbb Q_2$.
Equivalently, one can solve

$$
T^2=x_j^4-n/d_j;
$$

the right side is a 2-adic unit congruent to 1 modulo 8, hence is a square
in $\mathbb Q_2$.

If $p\notin P$ is odd, all coefficient valuations are even. Rescale
each quadratic coordinate by the corresponding half-valuation; the form is
then equivalent over $\mathbb Q_p$ to a form with unit coefficients. Every
nondegenerate quadratic form in at least three variables over
$\mathbb F_p$ has a nontrivial zero, which then lifts by Hensel's lemma.
For completeness, for any nonzero $a,b,c\in\mathbb F_p$, the sets
$\{au^2:u\in\mathbb F_p\}$ and
$\{-c-bv^2:v\in\mathbb F_p\}$ both have size $(p+1)/2$, hence
intersect; the resulting vector $(u,v,1)$ is a nontrivial zero of
$au^2+bv^2+cw^2$. Therefore $Q$ is isotropic over every finite
completion of $\mathbb Q$.

The square-product assumption now contradicts reciprocity. Set

$$
B=d_2/d_1,\qquad C=d_3/d_1,\qquad D=d_4/d_1.
$$

Since $BCD=(d_1d_2d_3d_4)/d_1^4$ is a square, the ratio
$D/(BC)$ is a square. Hence, after scaling the form and rescaling its
fourth coordinate, $Q$ is isometric up to similarity to

$$
\langle1,B,C,BC\rangle.
$$

This is the reduced norm of the quaternion algebra
$\mathcal B=(-B,-C)_{\mathbb Q}$. A quaternion reduced norm is
isotropic precisely when its algebra is split: in a division algebra every
nonzero element has nonzero reduced norm, while in the matrix algebra the
reduced norm is the determinant. The preceding local argument therefore
shows that $\mathcal B$ splits at every finite place. But $B,C>0$,
so $\mathcal B$ is ramified at the real place. This gives exactly one
ramified place, contradicting Hilbert reciprocity.

The reciprocity input is Proposition 14.2.1 and Corollary 14.2.3 of the
supplied Voight chapter. Its full supplied Markdown has been read. No
Hasse--Minkowski theorem, integral local-global assertion, or density result
is being inferred from it. $\square$

### Scope

For every finite set of allowed odd squarefree-kernel primes, one progression
excludes *all* square-product coefficient tuples whose odd-valuation primes
lie in that set. The square parts of the kernels can have arbitrary prime
support. In particular, $n\equiv8\pmod {16}$ excludes all tuples for
which every $d_i$ is a square, with no truncation. In
particular it excludes Ghidelli's exceptional quartic tuples in that finite
family, because tuples proportional over fourth powers to
$(a,b,4a,4b)$ have square product.

This does not yet exclude every square-product tuple: a kernel with an
odd-valuation prime outside the prescribed set can evade the argument. Nor does
it control the nonsquare-product tuples. A separate uniform summable majorant is
needed to pass from the finite-supported elimination to the full powerful-number
sumset.

### A weighted square-product tail estimate

Fix $\kappa\geq1$, and for a tuple write

$$
w_\kappa(\mathbf d)=
\kappa^{\omega(d_1)+\cdots+\omega(d_4)}(d_1d_2d_3d_4)^{-1/4}.
$$

The total weight of square-product tuples having an odd-valuation prime
greater than $Y$ is $O_\kappa(Y^{-3/2})$. Here and below the
implied constant is independent of $Y$.

To see this, put

$$
u_p=1+\kappa p^{-3/2},\qquad
v_p=\kappa(p^{-5/4}+p^{-7/4}).
$$

The local Euler factor for square-product tuples is

$$
E_p=u_p^4+6u_p^2v_p^2+v_p^4.
$$

Its product over all primes converges, because
$E_p=1+O_\kappa(p^{-3/2})$. If a prime has odd valuation in some
coefficient of a square-product tuple, it has odd valuation in two or four
of the coefficients. Its corresponding local weight is
$6u_p^2v_p^2+v_p^4=O_\kappa(p^{-5/2})$. A union bound inside the
nonnegative Euler product therefore gives the asserted estimate, since
$\sum_{p>Y}p^{-5/2}\leq\sum_{n>Y}n^{-5/2}\ll Y^{-3/2}$.

This sharper estimate separates the genuinely relevant odd-valuation
primes from primes occurring only in square kernel factors; the latter
require no congruence condition in the elimination lemma.

### Consequence for the full square-product stratum

Let $\mathcal T$ consist of the sums
$d_1x_1^4+\cdots+d_4x_4^4$, with $x_i\geq1$,
$d_i\in\mathcal C_4$, and $d_1d_2d_3d_4$ a square. Then
$\mathbb N\setminus\mathcal T$ has positive lower natural density.
This statement is about a stratum, not about $S_4$.

Here are the details of the necessary uniform congruence estimate. If
$p$ is odd, $p\nmid d_1\cdots d_4$, and

$$
N_p=\#\{\mathbf x\bmod p:\sum_i d_ix_i^4=0\},
$$

then

$$
N_p\leq p^3+81p^2.
$$

Indeed, for $s\ne0$, the complete sum
$\sum_xe_p(sd_ix^4)$ is the sum of at most three Gauss sums of
modulus $\sqrt p$, each multiplied by a multiplicative character of
$s$. Expand the product of four such sums and sum over $s\ne0$.
There are at most $3^4=81$ terms, each of modulus at most
$p^2(p-1)/p\leq p^2$ after additive orthogonality. This proves the
bound. The standard Gauss-sum absolute value follows directly by expanding
its squared modulus and using multiplicative-character orthogonality.

If some coefficient vanishes modulo $p$, fixing all variables except
one with nonzero coefficient gives $N_p\leq4p^3$; if all vanish,
the congruence modulo $p^2$ with target $p\pmod {p^2}$ has no
solution. For a solution modulo $p^2$ with this target, at least one
$d_jx_j$ is a unit: otherwise all summands are divisible by $p^4$.
Thus the quartic equation is nonsingular modulo $p$, and each such
root modulo $p$ has exactly $p^3$ lifts to the specified target
modulo $p^2$. Consequently its normalized density satisfies

$$
\frac{\#\{\mathbf x\bmod p^2:F_{\mathbf d}(\mathbf x)
 \equiv p\pmod {p^2}\}}{p^6}
\leq(1+81/p)4^{\sum_i\mathbf1_{p\mid d_i}}.
$$

The factor modulo 16 is at most 16. CRT therefore gives, for
$P=\{p\text{ odd prime}:p\leq Y\}$,

$$
\frac{\#\{\mathbf x\bmod B_P:F_{\mathbf d}(\mathbf x)
 \equiv a_P\pmod {B_P}\}}{B_P^3}
\leq16\,4^{\sum_i\omega(d_i)}\prod_{p\leq Y}(1+81/p).
\tag{1}
$$

No prime-number theorem is needed to bound the last product. For
$Y\geq e$, put $\sigma=1+1/\log Y$; then

$$
\sum_{p\leq Y}p^{-1}
\leq e\sum_p p^{-\sigma}
\leq e\log\zeta(\sigma)
\leq e\log(1+\log Y).
$$

Here the last inequality follows from the integral bound
$\zeta(\sigma)\leq1+1/(\sigma-1)$. Hence

$$
\prod_{p\leq Y}(1+81/p)\leq(1+\log Y)^{81e}.
\tag{2}
$$


For a fixed tuple and a fixed modulus, elementary lattice-point counting
in the dilates of
$\{\mathbf t\geq0:\sum_i d_it_i^4\leq1\}$ gives

$$
R_{\mathbf d}(X;a_P,B_P)
=\frac{V_4X}{B_P}(d_1d_2d_3d_4)^{-1/4}\rho_{B_P}(\mathbf d)
+O_{B_P,\mathbf d}(X^{3/4}),
$$

where $V_4=\Gamma(5/4)^4$, and $\rho_{B_P}$ is the
left side of (1). This estimate can also be obtained by covering the
boundary of a fixed convex body by $O(X^{3/4})$ unit cubes in each
fixed residue lattice; it needs no uniformity in the tuple.

The elimination lemma removes all square-product tuples without an
odd-valuation prime exceeding $Y$. Combining (1), (2), and the
weighted tail estimate with $\kappa=4$, the total main term for all
remaining square-product tuples is at most

$$
\frac X{B_P}\,O\bigl(Y^{-3/2}(1+\log Y)^{81e}\bigr).
\tag{3}
$$

To justify summing despite nonuniform errors, first restrict all kernels
to a finite set $E$, sum the displayed lattice-point formula, and
then let $E$ grow. The omitted tuples have at most

$$
X\sum_{\mathbf d\notin E^4}(d_1d_2d_3d_4)^{-1/4}=o_E(X)
$$

representations, since the full weight series converges. As $B_P$
is fixed during this step, this tail can be made arbitrarily small
relative to $X/B_P$. Thus (3) bounds the upper relative density of
$\mathcal T$ in the chosen progression. Taking $Y$ large makes
that bound smaller than $1/2$, proving the positive-lower-density
complement statement.

The unhandled set consists of tuples with nonsquare product. Its weight
is not a tail, and neither the local elimination lemma nor (3) bounds its
contribution. In particular, this consequence cannot be promoted to a
theorem about $S_4$ without an additional argument.


---

## Appendix C. Principal quartic character elimination

Source working file: r4_principal_character_elimination.md

## Elimination of every principal algebraic quartic character

Let $d_1,d_2,d_3,d_4$ be positive integers such that every nonzero prime
valuation of every $d_i$ is at least $4$. Let $P$ contain all odd
prime divisors of $d_1d_2d_3d_4$. Suppose that

$$
n=\sum_{i=1}^4d_ix_i^4,\qquad
v_2(n)=3,\quad v_p(n)=1\quad(p\in P).
\tag{1}
$$

Then none of the nineteen algebraic characters occurring in Ghidelli's
formula for $K_{F,q}$, viewed as characters over $\mathbb Q(i)$, is
principal.

The formula, in Proposition 4.3 of the supplied Ghidelli Markdown, has
one term with argument $(d_1d_2d_3d_4)^2$, six terms with arguments
$d_id_jd_k^3d_l^3$, and twelve terms with arguments
$-d_i^2d_j^2d_kd_l^3$. Here the latter two lists run through distinct
assignments of their indicated exponent patterns. Every term has
coefficient $1$.

### The first seven characters

A positive rational number is a fourth power in $\mathbb Q(i)$ if and
only if it is a fourth power in $\mathbb Q$. Thus principality of the
first character forces $d_1d_2d_3d_4$ to be a square. Principality of a
character of type $(1,1,3,3)$ also forces the product to be a square,
because all its exponents are odd. Both possibilities are ruled out by
the square-product local elimination lemma proved in
`r4_local_elimination.md`.

### The remaining twelve characters

It remains to rule out

$$
d_i^2d_j^2d_kd_l^3=4t^4\qquad(t\in\mathbb Q_{>0}).
\tag{2}
$$

Indeed, a negative rational is a fourth power in $\mathbb Q(i)$
precisely when it is $-4$ times a rational fourth power: if
$(a+bi)^4<0$ is real, with $a,b\in\mathbb Q$, then $b=\pm a$.

Equation (2) implies that $d_kd_l$ is a square. Therefore write

$$
d_k=cu^2,\qquad d_l=cv^2,
$$

where $c$ is a positive squarefree integer and $u,v$ are positive
integers. Taking the positive square root of (2) gives

$$
d_id_j uv=2s^2,\qquad s=t/(cv)\in\mathbb Q_{>0}.
\tag{3}
$$

Define the positive definite quadratic form

$$
Q(Z_1,Z_2,Z_3,Z_4)
=d_iZ_1^2+d_jZ_2^2+cZ_3^2+2cuvZ_4^2.
$$

Its determinant is $2d_id_jc^2uv=(2cs)^2$, a rational square.
The identity

$$
d_kx_k^4+d_lx_l^4
=c(ux_k^2-vx_l^2)^2+2cuv(x_kx_l)^2
$$

shows that $Q(z)=n$ at the integral vector

$$
z=(x_i^2,x_j^2,ux_k^2-vx_l^2,x_kx_l).
\tag{4}
$$


We prove that $Q$ is isotropic over every finite completion, contradicting
the positive definite square-determinant quaternion reciprocity argument
in `r4_local_elimination.md`.

For an odd prime $p\in P$, (1) and the lower bound on the nonzero
valuations of the original coefficients imply that some original summand
$d_hx_h^4$ is a $p$-adic unit. If one of the terms with $h=i,j$
is a unit, then the corresponding coefficient times coordinate of $Q$
at (4) is a unit. Otherwise at least one of $cu^2x_k^4$,
$cv^2x_l^4$ is a unit, so $c$ is a unit. If just one of
$ux_k^2,vx_l^2$ is a unit, then $z_3$ is a unit. If both are
units, then either $z_3$ is a unit or else $2cuvz_4$ is a unit.
In every case some partial derivative of $Q$ at $z$ is a unit.
Since $Q(z)\equiv0\pmod p$, Hensel's lemma supplies a nonzero
isotropic vector over $\mathbb Q_p$.

At $2$, every even original summand is divisible by $16$, so (1)
again implies that at least one original summand is odd. If an $i$-
or $j$-summand is odd, a corresponding coefficient times coordinate
of $Q$ is odd. If neither is odd, at least one of the $k$- or
$l$-summands is odd, and $c$ is odd. If exactly one is odd,
$z_3$ is odd. The only remaining case would have $c,u,v,x_k,x_l$
all odd and neither $i$- nor $j$-summand odd. But the two latter
summands vanish modulo $16$, whereas

$$
n\equiv c(u^2x_k^4+v^2x_l^4)\equiv2c\not\equiv0\pmod8,
$$

contradicting (1). Thus some coefficient times coordinate of $Q$ at
$z$ is odd. Varying just that coordinate gives a polynomial whose
value has valuation $3$ and whose derivative has valuation $1$.
The strong form of Hensel's lemma applies since $3>2$, yielding a
nonzero isotropic vector over $\mathbb Q_2$.

Every odd prime outside $P$ divides none of $d_i,d_j,c,2cuv$.
The reduction of $Q$ is a nonsingular quadratic form in four
variables over $\mathbb F_p$, hence has a nonzero zero; this zero
lifts. Consequently $Q$ is isotropic at every finite prime and
anisotropic at the real place. Since its determinant is a square,
it is similar to a quaternion reduced norm, whose ramification set
would then consist only of the real place. Hilbert reciprocity rules
this out, and proves the claim.

### Scope

For the kernels $d_i\in\mathcal C_4$, all the valuation assumptions
hold. Hence the single congruence progression from
`r4_local_elimination.md`, imposed at a finite set of kernel-support
primes, eliminates *all* coefficient tuples supported there that have
any principal algebraic character in $K_{F,q}$. This includes the
nonsquare-determinant principal-character tuples as well as all
square-determinant tuples. No estimate for the remaining Euler products
or the infinite coefficient tail is asserted here.


---

## Appendix D. Baseline Euler-product lemma

Source working file: baseline_lemma.md

## Uniform upper bound for the quartic baseline Euler product

This note establishes an auxiliary lemma for the investigation of Erdős 940.
It does not, by itself, assert any density conclusion. The supplied full text
of Ghidelli (2019) has been read. The inputs taken from it are the exact local
formulas in Proposition 4.3 and Lemma 6.4, the Hecke-character interpretation
in Proposition 5.2, and the elementary Kummer identification in Section 6.2.
The conductor and uniform analytic estimates below are proved here.

Let

$$
 F(\mathbf x)=d_1x_1^4+d_2x_2^4+d_3x_3^4+d_4x_4^4,
 \qquad R=\operatorname{rad}(d_1d_2d_3d_4),
$$

where the coefficients are positive integers. Put
$\rho_p(F)=p^{-3}\#\{\mathbf x\bmod p:F(\mathbf x)=0\}$.
Let $K=\mathbb Q(i)$, and write $\vartheta_a$ for the quartic power-residue
Hecke character $(a/\cdot)_4$ of $K$, for rational $a\ne0$. Multiplying
$a$ by a rational fourth power does not change this character.

There are nine finite-order Gaussian characters naturally associated to
$F$. Three of them are obtained by taking one representative from each
complementary pair of two-element subsets $I,I^c$ of $\{1,2,3,4\}$:

$$
 \vartheta_{\prod_{i\in I}d_i/\prod_{i\notin I}d_i}.
$$

The other six are indexed by a two-element set $I=\{i,j\}$, with complementary
indices $k,l$; choose either ordering of $k,l$, and take

$$
 \vartheta_{-d_i^2d_j^2d_k/d_l}.
$$

Changing a choice replaces the character by its inverse and therefore does
not change whether it is principal. Let $b(F)$ be the number of principal
characters in this list, counted with multiplicity. Let $D$ be the positive
squarefree part of $d_1d_2d_3d_4$, and set

$$
 m(F)=b(F)+\mathbf1_{D=1},\qquad 0\le m(F)\le10.
$$


**Lemma.** There is an absolute constant $C$ such that, for every such form
and every $Z\ge3$,

$$
 \prod_{\substack{3\le p\le Z\\p\nmid R}}\rho_p(F)
 \le C\,[\log(2R)]^{11-m(F)}[\log(2Z)]^{m(F)}. \tag{1}
$$

Consequently, for every $\epsilon>0$,

$$
 \prod_{\substack{3\le p\le Z\\p\nmid R}}\rho_p(F)
 \ll_\epsilon R^\epsilon[\log(2Z)]^{m(F)}. \tag{2}
$$

In particular, if $D\ne1$ and none of the nine finite Gaussian characters is
principal, the product is $\ll_\epsilon R^\epsilon$, uniformly in $Z$.

### 1. A uniform defining modulus

Every finite character $\vartheta_a$ appearing here has order dividing four
and, by Ghidelli Proposition 5.2(i), has a defining ideal supported at prime
ideals over $2R$. It has a defining ideal dividing $(32R)$. Here is the
uniform justification, which is not supplied by the unspecified exponent in
that proposition.

Since $\mathbb Z[i]$ has class number one, a finite Hecke character with a
defining ideal $\mathfrak f$ is represented by a character of
$(\mathbb Z[i]/\mathfrak f)^\times$, trivial on the images of units. By the
Chinese remainder theorem, this character is a product of local characters.
At an odd prime ideal $\mathfrak p$, the kernel of reduction from units
modulo $\mathfrak p^e$ to units modulo $\mathfrak p$ is a group of odd
prime-power order. An order-dividing-four character is trivial on it. Its
conductor exponent at $\mathfrak p$ is therefore at most one.

At $\pi=1+i$, every unit congruent to $1\pmod{\pi^9}$ is a fourth power
in $\mathbb Z_2[i]$. Indeed, apply the usual Newton/Hensel argument to
$X^4-u$ at $X=1$: $v_\pi(u-1)\ge9>2v_\pi(4)=8$. The same assertion
modulo every $\pi^e$ follows by reduction. An order-dividing-four local
character is thus trivial on this subgroup, so its conductor exponent is at
most nine. The integer modulus $32R$ contains all these local factors.

The normalized Jacobi symbol $\mathfrak J_4$ of Ghidelli Proposition 5.2(ii)
has defining ideal $(16)$ and infinity type $z\mapsto z/|z|$. Hence

$$
 \Psi=\mathfrak J_4^2\vartheta_{d_1d_2d_3d_4}^{-1}
$$

has defining ideal $(32R)$ and infinity type $(z/|z|)^2$. It is never
principal.

### 2. An elementary uniform upper bound for Gaussian Hecke L-functions

Let $m\ge2$ be an integer, and let $\psi$ be a unitary Gaussian Hecke
character with defining ideal $(m)$ and infinity type
$(z/|z|)^k$, where $k=0$ or $2$. Extend it by zero on ideals not coprime
to $(m)$. Assume that $\psi$ is not principal. There is a periodic
function $\eta$ modulo $m\mathbb Z[i]$, zero on nonunits and a
multiplicative character on units, such that

$$
 \psi((z))=\eta(z)(z/|z|)^k \qquad(z\ne0).
$$

For completeness, periodicity follows from the defining-ideal condition:
if $z_1\equiv z_2\pmod m$ and both are coprime to $m$, multiply them by
an inverse of their common residue modulo $m$, and apply that condition to
the resulting two elements congruent to one.

The mean of $\eta$ on a full residue square is zero. For $k=0$, this is
because $\eta$ is nonprincipal; if it were principal, class number one would
make $\psi$ principal. For $k=2$, the unit $i$ gives
$\eta(i)=i^{-2}=-1$, so $\eta$ is again nonprincipal.

Partition the Gaussian lattice into squares of side $m$. On a complete
square at distance $r\ge2m$ from the origin, subtract the value of
$(z/|z|)^k$ at a fixed point in the square and use the zero mean of
$\eta$. Its derivative is $O(1/r)$, so that square contributes
$O(m^3/r)$. Summing the complete squares in the disk of radius $T$, and
bounding the $O(T/m+1)$ boundary squares trivially, gives

$$
 \left|\sum_{0<|z|\le T}\eta(z)(z/|z|)^k\right|
 \ll mT+m^2.
$$

There are four generators of each nonzero ideal. Consequently, for
$x\ge m^2$,

$$
 A_\psi(x):=\sum_{N\mathfrak a\le x}\psi(\mathfrak a)\ll m\sqrt x, \tag{3}
$$

with an absolute constant. Also $\#\{\mathfrak a:N\mathfrak a\le x\}\ll x$
by the elementary Gaussian lattice count.

For $1<\sigma\le2$, split the Hecke Dirichlet series at $m^2$. Its initial
part is at most $C\log(2m)$ in modulus. Partial summation with (3) shows that
the remaining tail has modulus $O(1)$, uniformly in $m,\sigma$. Therefore

$$
 |L(\sigma,\psi)|\ll\log(2m)\qquad(1<\sigma\le2). \tag{4}
$$

For a principal character with the same defining ideal, the elementary bound
is instead $L(\sigma,\psi)\le\zeta_K(\sigma)\ll(\sigma-1)^{-1}$.

The corresponding rational statement is simpler: a nonprincipal Dirichlet
character modulo $q$ has periodic partial sums bounded by $q$; splitting
at $q$ gives $|L(\sigma,\chi)|\ll\log(2q)$, uniformly for
$1<\sigma\le2$. The principal character is bounded by $\zeta(\sigma)$.

### 3. Uniform smoothing of prime sums

For $Z\ge3$, put $\sigma=1+1/\log Z$. For every character above,

$$
 \sum_{N\mathfrak p\le Z}\frac{\operatorname{Re}\psi(\mathfrak p)}{N\mathfrak p}
 =\log|L(\sigma,\psi)|+O(1), \tag{5}
$$

with an absolute constant independent of its modulus. Indeed, prime-power terms
of order at least two in $\log L$ have an absolutely bounded total. The
difference between the prime terms up to $Z$ with weights $1/N\mathfrak p$
and $(N\mathfrak p)^{-\sigma}$ is bounded by
$(\sigma-1)\sum_{N\mathfrak p\le Z}\log(N\mathfrak p)/N\mathfrak p\ll1$. The
remaining prime tail is also bounded, by partial summation and the Chebyshev
upper bound for rational primes. Gaussian prime ideals of degree one occur at
most twice over a rational prime; degree-two prime ideals have norm the square
of a rational prime. Thus the rational Chebyshev estimate suffices, with an
absolute constant. The rational counterpart of (5) is identical.

Combining (4) and (5), a nonprincipal character contributes at most
$\log\log(2m)+O(1)$ to its prime sum. A principal character contributes at
most $\log\log(2Z)+O(1)$.

### 4. The local expansion and its sum

For odd $p\nmid R$, put $A=d_1d_2d_3d_4$. At $p\equiv3\pmod4$,
Ghidelli Lemma 6.4 gives

$$
 \rho_p(F)=1+\chi_D(p)(p^{-1}-p^{-2}),
$$

where $\chi_D$ is the real quadratic character associated with the positive
squarefree integer $D$. At $p\equiv1\pmod4$, Proposition 4.3 gives the
same quadratic term and, in addition, the eighteen finite quartic terms
listed above together with $2\operatorname{Re}\Psi(\mathfrak p)$, all
multiplied by $p^{-1}-p^{-2}$. The eighteen finite terms form nine conjugate
pairs: complementary subsets give inverse characters in the first family,
and exchanging $k,l$ does so in the second because the product of the two
arguments is $(d_i d_j)^4$.

For rational $a$, $\vartheta_a(\overline{\mathfrak p})
=\overline{\vartheta_a(\mathfrak p)}$; the same conjugation relation holds
for $\Psi$. Consequently the sum over split rational primes of each
conjugate pair is the sum over the corresponding degree-one Gaussian prime
ideals. Completing that sum by the degree-two prime ideals changes it by
$O(1)$, because their norms are $p^2$.

Use $\log(1+u)\le u$ and absorb all $p^{-2}$ terms. We obtain

$$
 \log\prod_{\substack{3\le p\le Z\\p\nmid R}}\rho_p(F)
 \le \sum_{p\le Z}\frac{\chi_{D,R}(p)}p
 +\sum_{j=1}^9\sum_{N\mathfrak p\le Z}
       \frac{\operatorname{Re}\vartheta_j(\mathfrak p)}{N\mathfrak p}
 +\sum_{N\mathfrak p\le Z}
       \frac{\operatorname{Re}\Psi(\mathfrak p)}{N\mathfrak p}+O(1). \tag{6}
$$

Here all Gaussian characters are extended by zero at prime ideals dividing
$(32R)$, and $\chi_{D,R}$ is the character induced from $\chi_D$ modulo
$8R$, also extended by zero at primes dividing $2R$. It is principal
exactly when $D=1$. The modulus $8R$ is divisible by the fundamental
discriminant of $\mathbb Q(\sqrt D)$.

There are eleven characters on the right of (6): one rational quadratic,
nine finite Gaussian, and one infinite-order Gaussian. Exactly $m(F)$ are
principal. Applying Section 3 to each gives (1), and hence (2).

### 5. Bad primes when coefficients are canonical

Suppose now that each $d_j$ is a canonical quartic-powerful coefficient:
$v_p(d_j)\in\{0,5,6,7\}$. For any odd prime $p$, let

$$
 \widetilde\rho_p(F)=p^{-6}
  \#\{\mathbf x\bmod p^2:F(\mathbf x)\equiv p\pmod{p^2}\}.
$$

If $p\nmid R$, smooth lifting gives
$\widetilde\rho_p(F)\le\rho_p(F)$. For $p\mid R$, either there is no
solution or at least one coordinate with coefficient prime to $p$ is a
unit. Otherwise every summand is divisible by $p^4$, contrary to the target
valuation one. Such residue vectors are smooth modulo $p$, and each has
exactly $p^3$ lifts to the target class modulo $p^2$. There are at most
$4p^3$ such residue vectors: choose a coefficient prime to $p$, fix the
other three coordinates, and solve a polynomial of degree four for that
coordinate. Therefore

$$
 \widetilde\rho_p(F)\le4\qquad(p\mid R).
$$

It follows from (2) that

$$
 \prod_{3\le p\le Z}\widetilde\rho_p(F)
 \ll_\epsilon 4^{\omega(R)}R^\epsilon[\log(2Z)]^{m(F)}. \tag{7}
$$

In the absence of principal finite characters, this is uniform in $Z$
without any logarithm of $Z$.


---

## Appendix E. Universal quadratic selector lemma

Source working file: quadratic_selector_lemma.md

## A universal, uniformly controlled quadratic prime selector

This is a self-contained lemma for the quartic-powerful investigation. It does
not by itself prove a statement about powerful sums.

For a positive squarefree integer $D$, write $\chi_D$ for the primitive
quadratic Dirichlet character of $\mathbb Q(\sqrt D)$; $\chi_1=1$. Values at
ramified primes are zero. Let $\mathcal P_3=\{p:p\equiv3\pmod4\}$.

### 1. Uniform quadratic Euler sums

There is an absolute constant $C$ such that every nonprincipal real Dirichlet
character $\chi$ modulo $m$ satisfies

$$
 \sup_{X\ge3}\left|\sum_{p\le X}\frac{\chi(p)}p\right|\le C\log(2m).\tag{1}
$$

Consequently, for $D>1$,

$$
 \sup_{X\ge3}\left|\sum_{p\le X,\ p\in\mathcal P_3}\frac{\chi_D(p)}p\right|
 \le C\log(2D),\tag{2}
$$

and, if $D,E>1$ are distinct squarefree integers,

$$
 \sup_{X\ge3}\left|\sum_{p\le X,\ p\in\mathcal P_3}
 \frac{\chi_D(p)\chi_E(p)}p\right|\le C\log(2DE).\tag{3}
$$

All these bounds hold for sums over an interval, after doubling $C$.

Here is an elementary proof, including the polynomial lower bound that is needed
for (1).

#### Nonvanishing and a lower bound at 1

Let $\chi$ be primitive, real, and nonprincipal, of conductor $q$. Its partial
sums are bounded by $q$, so $L(s,\chi)$ is holomorphic on
$\operatorname{Re} s>0$. Also $L(1,\chi)>0$. For completeness, nonvanishing
follows from the positive coefficients of

$$
 \zeta(s)L(s,\chi)=\sum_{n\ge1}a(n)n^{-s},\qquad
 a(n)=\sum_{d\mid n}\chi(d)\ge0.
$$

Multiplicativity gives $a(k^2)\ge1$, so the abscissa of convergence is at least
$1/2$. If $L(1,\chi)=0$, the product would be holomorphic throughout
$\operatorname{Re} s>0$, contradicting the elementary Landau lemma for a series
with nonnegative coefficients. That lemma follows by expanding at a real point
to the right of the abscissa: the nonnegative Taylor coefficients in the
leftward direction allow Tonelli's theorem to extend convergence leftward past
the abscissa. Positivity at 1 follows by taking the limit from $s>1$, where all
Euler factors are positive.

Let $\zeta=e^{2\pi i/q}$, and let $\tau=\sum_{a=1}^q\chi(a)\zeta^a$. The usual
finite Fourier identity, obtained by the change of variable $a\mapsto an^{-1}$,
and finite Fourier orthogonality give

$$
 \sum_a\chi(a)\zeta^{an}=\chi(n)\tau,\qquad |\tau|=\sqrt q.
$$

The identity remains true when $(n,q)>1$, with both sides zero, by primitivity.
Expanding $-\log(1-r\zeta^a)$ and letting $r\uparrow1$ gives

$$
 -\tau L(1,\chi)=\sum_{a=1}^q\chi(a)\log(1-\zeta^a).\tag{4}
$$

If $\chi$ is odd, the real parts on the right cancel in pairs. Since
$\arg(1-\zeta^a)=\pi a/q-\pi/2$, (4) gives

$$
 |L(1,\chi)|=\frac{\pi}{q^{3/2}}\left|\sum_{a=1}^q a\chi(a)\right|\ge\pi q^{-3/2}.
$$

The sum is a nonzero integer, by nonvanishing.

If $\chi$ is even, put

$$
 P=\prod_{(a,q)=1}(1-\zeta^a)^{\chi(a)}.
$$

This is a positive real algebraic unit. Indeed, $(1-\zeta^a)/(1-\zeta)$ is a
unit: it and its inverse are finite geometric sums, using an inverse of $a$
modulo $q$; and $\sum_a\chi(a)=0$. The automorphism $\zeta\mapsto\zeta^b$ takes
$P$ to $P^{\chi(b)}$. Thus $P$ belongs to the quadratic fixed field of
$\ker\chi$, and its other conjugate is $P^{-1}$. It is not 1 by (4) and
nonvanishing. Hence $P+P^{-1}$ is an integer strictly larger than 2, and

$$
 |\log P|\ge\log((3+\sqrt5)/2).
$$

Equation (4) implies $L(1,\chi)\ge c q^{-1/2}$. In both parity cases,

$$
 L(1,\chi)\ge c q^{-3/2}.\tag{5}
$$

#### Bounds uniformly to the right of 1

Splitting the Dirichlet series at $q$ and applying partial summation to the
tail, using the bound $q$ for the partial sums, gives, for $1\le\sigma\le2$,

$$
 |L(\sigma,\chi)|\le C\log(2q),\qquad |L'(\sigma,\chi)|\le C\log^2(2q).\tag{6}
$$

For example, the tail in the derivative is bounded by
$q\log q/q^\sigma+q\int_q^\infty(1+\sigma\log t)t^{-\sigma-1}\,dt\ll\log(2q)$,
and the initial segment contributes $O(\log^2(2q))$.

Set $h=cq^{-3/2}/(2C\log^2(2q))$, with the constants in (5) and (6). If
$1\le\sigma\le1+h$, (5) and (6) give $L(\sigma,\chi)\ge cq^{-3/2}/2$. If
$1+h<\sigma\le2$, Euler factors give

$$
 L(\sigma,\chi)\ge\prod_p(1+p^{-\sigma})^{-1}
 =\frac{\zeta(2\sigma)}{\zeta(\sigma)}\ge\frac{\sigma-1}{\sigma}\ge h/2.
$$

Since $\log^2(2q)\ll q^{1/2}$, we obtain

$$
 cq^{-2}\le L(\sigma,\chi)\le C\log(2q)\qquad(1\le\sigma\le2).\tag{7}
$$

For $\sigma\ge2$, absolute Euler products give absolute upper and lower bounds.
An imprimitive character modulo $m$ differs from its primitive character by
Euler factors at primes dividing $m$; their product and its inverse are at most
$m$. Thus

$$
 |\log L(\sigma,\chi)|\le C\log(2m)\quad(\sigma>1)\tag{8}
$$

for every nonprincipal real character modulo $m$.

To pass to prime sums, put $\sigma=1+1/\log X$. Chebyshev's bound
$\pi(t)\ll t/\log t$ gives

$$
 \sum_{p\le X}(p^{-1}-p^{-\sigma})\ll1,\qquad
 \sum_{p>X}p^{-\sigma}\ll1.
$$

For the first inequality use $1-e^{-u}\le u$ and
$\sum_{p\le X}\log p/p\ll\log X$; for the second use partial summation and the
substitution $u=\log t/\log X$. Higher prime powers in $\log L$ contribute
$O(1)$. Hence

$$
 \sum_{p\le X}\frac{\chi(p)}p=\log L(1+1/\log X,\chi)+O(1),\tag{9}
$$

uniformly in $\chi$ and $X\ge3$. This proves (1). The same smoothing with the
principal character gives $\sum_{p\le X}1/p=\log\log X+O(1)$. Taking half the
difference between $\chi_D$ and $\chi_D\chi_{-4}$ proves (2); both characters
are nonprincipal when $D>1$. The same argument proves (3), since for distinct
positive squarefree $D,E$ neither $\chi_D\chi_E$ nor its twist by $\chi_{-4}$
is principal. In particular,

$$
 \sum_{p\le X,\ p\in\mathcal P_3}\frac1p=\frac12\log\log X+O(1).\tag{10}
$$

### 2. Universal selector

Fix positive numbers $\lambda_E$, indexed by all positive squarefree $E>1$,
such that

$$
 \Lambda=\sum_E\lambda_E<\frac12,\qquad \sum_E\lambda_E\log(2E)<\infty.\tag{11}
$$

For example one may take $\lambda_E=1/(4E^2)$. For $0<\delta\le1/4$ and
$p\in\mathcal P_3$, set

$$
 f(p)=\delta\left(1-\sum_E\lambda_E\chi_E(p)\right).
$$

Thus $0<f(p)<1$. Choose independent Bernoulli variables $B_p$ with mean $f(p)$.

For every $\eta>0$, there exists a realization and a constant $C_\eta$ such
that simultaneously for every positive squarefree $D\ge1$ and every $X\ge3$,

$$
 \left|\sum_{p\le X,\ p\in\mathcal P_3}\frac{(B_p-f(p))\chi_D(p)}p\right|
 \le C_\eta+\eta\log(2D).\tag{12}
$$

Indeed, the increments are independent, have mean zero, and lie in intervals of
lengths at most $1/p$. Hoeffding's exponential supermartingale and its maximal
inequality yield

$$
 \Pr\left(\sup_X|M_D(X)|>u\right)\le2\exp(-2u^2/V),\qquad
 V=\sum_{p\in\mathcal P_3}p^{-2}<\infty.
$$

The union bound, with $u=C_\eta+\eta\log(2D)$, is less than 1 for sufficiently
large $C_\eta$: the sum over all $D\ge1$ converges and tends to zero as
$C_\eta\to\infty$. Fix such a realization, and put
$\mathcal P=\{p\in\mathcal P_3:B_p=1\}$.

For $3\le Z\le T$, let

$$
 P_D(Z,T)=\prod_{Z<p\le T,\ p\in\mathcal P}
 \left(1+\chi_D(p)(p^{-1}-p^{-2})\right).
$$

Then there is an absolute $C_0$, depending only on the fixed $\lambda_E$, such
that for every nonsquare $D>1$,

$$
 P_D(Z,T)\ll_{\eta,\delta}(2D)^{C_0\delta+2\eta},\tag{13}
$$

uniformly in $Z,T,D$. To see this, use
$\log(1+\chi_D(p)(p^{-1}-p^{-2}))=\chi_D(p)/p+O(p^{-2})$ and (12) at both
endpoints. The expectation is

$$
 \delta\sum_{Z<p\le T,\ p\in\mathcal P_3}\frac{\chi_D(p)}p
 -\delta\sum_E\lambda_E
 \sum_{Z<p\le T,\ p\in\mathcal P_3}\frac{\chi_D(p)\chi_E(p)}p.\tag{14}
$$

The term $E=D$ is nonpositive, so discard it for an upper bound. Bound the other
terms by (2), (3), and (11). This gives $C_0\delta\log(2D)+O(1)$, proving (13).

Moreover, for each fixed $D>1$, retaining $E=D$ and using (10) gives

$$
 \log P_D(Z,T)=-\frac{\delta\lambda_D}{2}
 (\log\log T-\log\log Z)+O_{D,\eta,\delta}(1).\tag{15}
$$

Here all nonprincipal sums in (14), including their infinite weighted sum, are
bounded uniformly in both endpoints by (2), (3), and (11). The finitely many
omitted primes dividing $D$ affect only the constant. Thus if $Z=Z(T)$ satisfies

$$
 \log\log T-\log\log Z(T)\longrightarrow+\infty,
$$

then $P_D(Z(T),T)\to0$ for every fixed nonsquare $D>1$.

For $D=1$, the same proof gives

$$
 P_1(Z,T)\ll_{\eta,\delta}\left(\frac{\log T}{\log Z}\right)^{\delta/2}.\tag{16}
$$

In particular, given any $\theta>0$, choosing $\eta$ and then $\delta$
sufficiently small gives a single set $\mathcal P\subseteq\mathcal P_3$ such
that (13) has exponent $\theta$, every nonsquare $D$ has the decay (15), and the
sole positive principal growth is (16). No prime number theorem in progressions,
Chebotarev theorem, Siegel theorem, or zero-free region is needed for this
selector lemma.


---

## Appendix F. Independent audit

Source working file: r4_independent_audit.md

## Independent audit of the proposed quartic architecture

This records an audit, not a completed proof of an open case. The two local
elimination notes were read, and the full supplied Ghidelli Markdown was
read. The proposed baseline and selector estimates were communicated by
the other researchers but are not available here as a complete,
independently checked proof.

### Checks that passed

The principal-character elimination in
`r4_principal_character_elimination.md` passes the following checks.
The nineteen algebraic terms are exactly those obtained by expanding
Ghidelli's Proposition 4.3: one exponent pattern `(2,2,2,2)`, six terms
with pattern `(1,1,3,3)`, and twelve signed terms with pattern
`(2,2,1,3)`. Their coefficients are positive. The first seven principal
possibilities force square determinant. For the remaining possibilities,
the transformation to the positive definite square-determinant quadratic
form in that note is algebraically correct. In particular, if
`d_k=c u^2`, `d_l=c v^2` and
`d_i^2 d_j^2 d_k d_l^3=4t^4`, then
`d_i d_j u v=2(t/(cv))^2`.

At a prescribed odd prime, valuation one of the represented integer
forces at least one original quartic summand to be a unit; the quadratic
form constructed in the note then has a nonsingular zero modulo that
prime. At 2, the only potential failure of the indicated unit derivative
would leave exactly the two paired terms odd; their sum is `2c mod 8`,
contradicting valuation three. The stated strong Hensel application is
therefore valid. These verifications do not independently reprove the
quaternion reciprocity theorem cited in the local notes.

For a prescribed odd prime, it is essential to impose
`n = p mod p^2`, including at selected primes larger than the cutoff.
Prescribing only `n=0 mod p` would give a factor `p` when every coefficient
is divisible by `p`; it would not give the claimed uniform bad-prime
bound. With the squared modulus, let `t` be the number of coefficients
prime to `p`. For canonical quartic kernels all the other coefficients
vanish modulo `p^2`. If `t>=1`, the normalized local density is exactly

    rho_p(d) = (N_t(0;p)-1)/p^(t-1) <= 4.

Here `N_t` counts zeros of the active diagonal quartic over the finite
field. The subtracted zero vector cannot lift to target `p mod p^2`,
whereas every other zero is nonsingular and has `p^(t-1)` lifts. If
`t=0`, the local density is zero. At good primes `t=4`, this gives
`rho_p=(N_4(0;p)-1)/p^3`.

### Exact final density reduction

Write `w(d)=(d_1 d_2 d_3 d_4)^(-1/4)`, with each `d_i` a canonical
quartic kernel. Their total weight is finite. Suppose finite moduli
`M_T` and residue classes `a_T` have been constructed, and put

    rho_T(d) = # {x mod M_T : sum d_i x_i^4 = a_T mod M_T}/M_T^3.

The sufficient analytic conclusion is

    sum_d w(d) rho_T(d) -> 0.                         (A)

For each fixed modulus `M=M_T`, counting each variable in its residue
class gives, for a fixed coefficient tuple, the upper asymptotic
contribution `w(d) rho_T(d) X/M` from tuples whose sum is at most `X`.
One may interchange this limit and the coefficient sum: before taking
the limit, the normalized contribution of any coefficient tuple is at
most `M w(d)`, because the unrestricted box contains at most
`w(d) X` positive tuples. This is a summable majorant for fixed `M`.
Thus the relative upper density of the exactly-four-summand set in the
progression is at most the sum in (A).

Sums with at most three 4-powerful summands contribute `O(X^(3/4))`
integers globally, hence zero relative density in every fixed progression.
If (A) holds, select one finite `T` for which its left side is below
`1/2`. Then the complement of `S_4` has lower natural density at least
`1/(2M_T)`. The modulus must be fixed before `X` tends to infinity.
This argument would prove positive density of the complement, not
density zero of `S_4`.

### Selector interval and remaining analytic obligations

The growing lower cutoff `Z=(log T)^A` is compatible with the intended
quadratic-character selector. Indeed,

    log log T - log log Z
      = log log T - log log log T - log A -> infinity.

For any fixed nontrivial positive squarefree discriminant, convergence
of its prime harmonic character sums makes the unweighted interval
contribution tend to zero. With selector mean
`delta(1-sum_E lambda_E chi_E(p))` on primes `p=3 mod 4`, the term
`E=D` consequently supplies the proposed negative divergent drift.
To interchange the infinite `E` sum with this limit one still needs a
uniform bound of size `O(log(DE))`, together with
`sum lambda_E log E < infinity`.

The random discrepancy can in principle be bounded simultaneously for
all `D`: its increments are bounded by `1/p`, whose squares are
summable. A maximal exponential inequality and Borel--Cantelli with
threshold `epsilon log D` give a finite random constant after accounting
for finitely many exceptional `D`. The interval discrepancy is bounded
by twice the corresponding initial-segment bound and tends to zero for
each fixed `D`.

The delicate deterministic point is two-sided control of quadratic
prime harmonic sums. Negative coefficients in the selector require
lower bounds for `L(sigma,chi)`, not just upper bounds. The proposed
repair uses the finite Fourier formula at 1: for odd primitive real
characters, a nonzero integer numerator gives a polynomial lower bound;
for even characters, the cyclotomic product is a nontrivial totally
positive quadratic unit of norm 1 and gives another polynomial bound.
A derivative bound `|L'(sigma,chi)| << (log q)^2` near 1, combined with
`L(sigma,chi) >= zeta(2sigma)/zeta(sigma)`, would extend this to a
uniform polynomial lower bound for every `sigma>1`. This outline looks
consistent, but its Fourier normalization, unit assertion, conductor
bookkeeping, and uniform constants were not written and fully audited
in this investigation.

Likewise, the baseline Gaussian Hecke-character bound communicated by
the `large_r` researcher requires a complete proof of its common
conductor bound, periodic lattice cancellation for infinity type 2,
and conversion from `L`-function bounds to truncated prime products.
If these baseline and selector majorants are proved with a sufficiently
small power of the coefficient radical, their product is summable
against `w(d)`. Principal-character tuples not yet locally eliminated
have radical exceeding `Z`, so their crude logarithmic factor can be
absorbed into a small radical power by taking `A` large. These facts
explain how dominated convergence could establish (A), but do not by
themselves establish those missing analytic estimates.


---

## Appendix G. Additional Hecke-bound route, not needed in the simplified selector

Source working file: r4_uniform_hecke_bounds.md

## Elementary bounds for the Hecke characters needed by a small prime tilt

This note supplies a possible analytic ingredient; it does not itself prove
an assertion about the powerful-number sumset.

### 1. A uniform character-sum bound

Let $K=\mathbb Q(i)$, let $\mathfrak m=(\alpha)$ be a nonzero
Gaussian ideal of norm $Q$, and let $a$ be an integer with
$|a|\leq A$, where $A$ is fixed. Suppose a unitary Hecke character
$\psi$, extended by zero on ideals not coprime to $\mathfrak m$,
has the expression

$$
\psi((z))=\eta(z)(z/|z|)^a,
\tag{1}
$$

where $\eta$ is a character modulo $\mathfrak m$, extended by zero
on nonunits. The compatibility condition at Gaussian units is understood.
If $\psi$ is nonprincipal, then

$$
\sum_{N\mathfrak a\leq X}\psi(\mathfrak a)
\ll_A Q+\sqrt{QX}.
\tag{2}
$$


Here is a direct lattice proof. Every ideal has four generators, so the sum
is one quarter of the sum of (1) over nonzero Gaussian integers in the disk
of radius $\sqrt X$. Tile the plane by translates of a fundamental
square for $\mathfrak m$, whose diameter is $O(\sqrt Q)$. The
tiles meeting the disk boundary contribute $O(\sqrt{QX}+Q)$.
The tiles within distance $O(\sqrt Q)$ of the origin contribute
$O(Q)$. On a remaining tile at distance $r$, the angular factor
changes by $O_A(\sqrt Q/r)$; summing this error over its $Q$
Gaussian points and then over all tiles gives $O_A(\sqrt{QX})$.
The tile main term is the complete residue sum
$S=\sum_{z\bmod\mathfrak m}\eta(z)$, times its angular factor.
If $a=0$, nonprincipality gives $S=0$. If $a\ne0$, the
integral of the angular factor over the disk is zero; comparison of its
tile Riemann sum with that integral has the same
$O_A(\sqrt{QX}+Q)$ error. This proves (2).

Partial summation, splitting at $X=\max(Q,2)$, now gives, uniformly
for real $\sigma\geq1$,

$$
|L(\sigma,\psi)|\ll_A \log(3Q),\qquad
|L'(\sigma,\psi)|\ll_A (\log(3Q))^2.
\tag{3}
$$

Indeed the unsigned sum over ideals of norm at most $Q$, weighted by
$1/N\mathfrak a$, is $O(\log(3Q))$, and the logarithmically
weighted version is $O((\log(3Q))^2)$. For the tails use
$\sum_{N\mathfrak a\leq t}\psi(\mathfrak a)\ll_A\sqrt{Qt}$
for $t\geq Q$. The same calculation proves convergence and
continuity at $\sigma=1$.

### 2. Nonreal characters and nonzero infinity types

If $\psi^2$ is nonprincipal, the elementary trigonometric inequality

$$
3+4\cos\theta+\cos(2\theta)=2(1+\cos\theta)^2\geq0
$$

and Euler products imply

$$
\zeta_K(\sigma)^3|L(\sigma,\psi)|^4
 |L(\sigma,\psi^2)|\geq1\qquad(\sigma>1).
\tag{4}
$$

Omitted Euler factors cause no difficulty because the full zeta function
is at least the zeta function with those factors omitted. Put
$H=\log(3Q)$. Equations (3)--(4), applied also to $\psi^2$, give

$$
|L(1+\delta,\psi)|\gg_A\delta^{3/4}H^{-1/4}
\qquad(0<\delta\leq1).
\tag{5}
$$

Choose $\delta_0=c_AH^{-12}$, with a sufficiently small fixed
$c_A>0$. The derivative estimate in (3) gives

$$
|L(1+\delta_0,\psi)-L(1,\psi)|
\ll_A\delta_0H^2,
$$

which is less than one quarter of the lower bound in (5). The same estimate
works for every $0\leq\delta\leq\delta_0$; for larger $\delta$
use (5) directly. Thus, loosening the exponent,

$$
|L(\sigma,\psi)|\gg_A H^{-10}
\qquad(\sigma\geq1)
\tag{6}
$$

whenever $\psi^2$ is nonprincipal. The case $\sigma\geq2$
also follows immediately from the absolutely convergent Euler product.

### 3. Crude quadratic Dirichlet lower bounds without a class-number formula

Let $\chi$ be a primitive nonprincipal real Dirichlet character of
conductor $q$. Then

$$
L(1,\chi)\gg q^{-3/2}.
\tag{7}
$$

Here is a proof of the facts needed for (7).

First $L(1,\chi)\ne0$. The coefficients of
$\zeta(s)L(s,\chi)$ are nonnegative: at a prime the local
coefficients are respectively $k+1$, $1$ for even $k$ and
$0$ for odd $k$, or $1$, according as $\chi(p)=1,-1,0$.
The coefficients at squares are at least $1$, so the abscissa of
convergence is at least $1/2$. If $L(1,\chi)=0$, the product is
holomorphic in $\Re s>0$: for the character factor this follows by
partial summation from bounded periodic partial sums, and for zeta it
follows from its usual alternating-series continuation. This contradicts
Landau's elementary lemma that a Dirichlet series with nonnegative
coefficients has a singularity at its finite abscissa of convergence.
To see the lemma, expand the function in a Taylor series about a real
point to the right of its abscissa. After replacing the argument by a
smaller real number, all terms of the differentiated Dirichlet series
are nonnegative; monotone interchange of sums would extend convergence
to the left of the abscissa if the boundary point were regular.
Moreover $L(1,\chi)>0$, by the positive Euler product for real
$s>1$ and continuity.

Let $\zeta_q=e^{2\pi i/q}$ and let $\tau(\chi)$ be the Gauss
sum, of absolute value $\sqrt q$. Fourier expansion, first for
$\sum \chi(n)r^n/n$ with $r<1$ and then by passage to the limit,
gives

$$
L(1,\chi)=-\tau(\chi)^{-1}
 \sum_{a=1}^q\chi(a)\log(1-\zeta_q^a).
\tag{8}
$$

For odd $\chi$, conjugate pairs cancel the real parts and (8) becomes

$$
L(1,\chi)=-\frac{i\pi}{q\tau(\chi)}
 \sum_{a=1}^q a\chi(a).
$$

The sum is a nonzero integer, by nonvanishing. This proves (7).

For even $\chi$, define

$$
\beta=\prod_{(a,q)=1}(1-\zeta_q^a)^{\chi(a)}>0.
$$

Its conjugate under $\zeta_q\mapsto\zeta_q^b$ is
$\beta^{\chi(b)}$. Therefore $\beta$ belongs to the real
quadratic fixed field of $\ker\chi$, and has norm $1$.
It is a unit: if $q$ is not a prime power then $1-\zeta_q$
is a unit, since $\Phi_q(1)=1$. If $q$ is a prime power, all
$1-\zeta_q^a$ with $(a,q)=1$ are associates, and the total
exponent $\sum_a\chi(a)$ is zero. These statements also follow
directly from the cyclotomic polynomial and the geometric-sum quotient
$(1-\zeta_q^a)/(1-\zeta_q)$.
Nonvanishing in (8) implies $\beta\ne1$. Hence
$u=\max(\beta,\beta^{-1})>1$ has positive conjugate $u^{-1}$,
and its integral trace is at least $3$. Consequently

$$
|\log\beta|\geq\log((3+\sqrt5)/2),
$$

which in fact gives the stronger bound $L(1,\chi)\gg q^{-1/2}$.

### 4. The real Hecke characters occurring here

In the quartic-character expansions under consideration, every finite
character is a quartic residue symbol of a rational number. When such
a character is real, it is a quadratic residue symbol
$(h/\cdot)_2$ over $\mathbb Q(i)$, with rational $h$, which
can be taken squarefree integral. For example, if the rational quartic
argument is $-b^2$, the character equals
$(2b/\cdot)_2$, since $-1$ and $4$ have the same class
modulo fourth powers in $\mathbb Q(i)$.

For its primitive version the Euler factors give

$$
L_K(s,(h/\cdot)_2)
=L_{\mathbb Q}(s,\chi_h)L_{\mathbb Q}(s,\chi_{-h}),
\tag{9}
$$

where the two Dirichlet characters correspond to
$\mathbb Q(\sqrt h)$ and $\mathbb Q(\sqrt{-h})$. Neither is
principal when the Hecke character is nonprincipal. Their conductors and
$|h|$ are bounded by fixed powers of $Q$. Removing any additional
Euler factors costs at most a further factor $Q^{-1}$, because
$1-1/N\mathfrak p\geq1/N\mathfrak p$.
Thus (7) gives $L(1,\psi)\gg Q^{-C}$, for an absolute $C$.

For $\sigma>1$, (4) still gives
$|L(\sigma,\psi)|\geq\zeta_K(\sigma)^{-1}$ when
$\psi^2$ is principal. Combine this with the derivative estimate
(3), taking $\sigma-1$ smaller or larger than a suitable
$Q^{-C}/H^2$, to obtain

$$
|L(\sigma,\psi)|\gg Q^{-C'}\qquad(\sigma\geq1).
\tag{10}
$$


### 5. Uniform partial Euler-product bounds

For $Y\geq3$, put $\sigma=1+1/\log Y$. The elementary
Chebyshev prime-counting bound gives, uniformly in a unitary character,

$$
\Re\sum_{N\mathfrak p\leq Y}
 \frac{\psi(\mathfrak p)}{N\mathfrak p}
=\log|L(\sigma,\psi)|+O(1).
\tag{11}
$$

Indeed the prime-power terms of order at least two are absolutely bounded;
the change from $1/N\mathfrak p$ to
$(N\mathfrak p)^{-\sigma}$ below $Y$ has total size $O(1)$,
and the omitted tail above $Y$ has total size $O(1)$. The inert
Gaussian prime ideals have square norms, so removing them only changes
the sums by $O(1)$.

It follows from (3), (6), and (10) that the partial prime sum of a
nonprincipal character is at most $O_A(\log\log(3Q))$ and at least
$-O_A(\log(3Q))$, uniformly in $Y$. The lower bound can be
improved to $-O_A(\log\log(3Q))$ unless the character is real.
These are enough for a tilted Euler product with an arbitrarily small
negative coefficient to have a majorant $Q^\varepsilon$, after the
tilt is chosen sufficiently small.

### Checks still needed before use in a full proof

The above estimates assume that the exact finite characters in the
application admit (1) with $Q$ bounded by a fixed power of the
radical of the coefficients (times a fixed factor from the finite core).
This follows from explicit quartic reciprocity or local conductor bounds,
but must be established in the final application rather than inferred
from Ghidelli's fixed-character error terms. Also, a finite-core prime
tilt, an infinite coefficient-tail majorant, and the reduction from
representation counts to missing integers still need to be assembled.

---

## Second reading of the baseline and selector lemmas

A reading in full of the baseline Euler-product lemma (Appendix D) and the
universal quadratic selector lemma (Appendix E), by the author of the
principal-character elimination (Appendix C) and not of either lemma, found no
remaining gap in those two lemmas. The points checked were the modulus-$32R$
argument, the Gaussian lattice estimate, the quadratic Fourier and unit lower
bound, and the maximal-probability union bound. This is additional favorable
audit evidence for the two lemmas. The assembled theorem of Sections 4 and 5
did not receive a final line-by-line verification; the status stated at the
beginning of this record is unchanged.

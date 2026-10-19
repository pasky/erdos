---
name: research/leads/totient_binary_series/integer_interpolation/two_depth_carries
title: Separate Depths and Scalar Kernels
desc: |
  Separate-depth carry and homogeneous scalar-kernel criteria control the
  full binary tail; odd pairing is feasible, while its uniform weighted cost
  remains open and does not follow from generic short kernel vectors.
problems:
- 249
research_state: ready
review_status: unreviewed
created: 2026-09-17T12:06:34Z
updated: 2026-10-14T00:26:52Z
---

***

The [[research/leads/totient_binary_series/integer_interpolation/carry_criterion|carry
criterion]] does not require the truncation depth to equal the depth of
the residue congruence. Separating them permits a slowly growing modulus
while a much longer truncation makes the complete remainder small. This
page first proves the corresponding sufficient criterion and qualitative
solvability with leading coefficient one. The homogeneous criterion below
then removes the prescribed nonzero scalar target: one small kernel vector
with an odd normalized-prefix pairing would suffice. A more general
valuation-gap criterion allows a nonzero scalar remainder. The quantitative
construction remains open here; the
[[research/leads/totient_binary_series/integer_interpolation/shadows|shadows
page]] proves a reverse implication on specified wider supports with
a growing lower cutoff. The separate
[[research/leads/totient_binary_series/integer_interpolation/phase_localization|arithmetic
localization]] supplies a subsequence equivalence on $[J,2J]$. All
arguments here are author-recorded and unreviewed;
[[problems/irrationality/E0249/_index|Problem 249]] is unresolved.

## The two depths

Retain
$\Phi_n=\sum_{m\le n}\varphi(m)2^{n-m}$,
$T_n=2^nS-\Phi_n$ and
$U_J(n)=\Phi_{n+J}-2^J\Phi_n$.
In particular $0<T_n\le n+2$ and
$2^JT_n=U_J(n)+T_{n+J}$.

Fix integers $d\ge1$, $J\ge3$, $c\ne0$, and finitely supported integers
$y_n$ with $n\ge d$. Put

$$
u=c+\sum_ny_n2^n,\qquad v=\sum_ny_n\Phi_n,\qquad
\Lambda=uS-v=cS+\sum_ny_nT_n,
$$

$$
W_J=c\Phi_J+\sum_ny_nU_J(n),\qquad
C_J=|c|(J+2)+\sum_n|y_n|(n+J+2).
$$

These definitions use the actual finite support, with no assumption
that $d=J$ or that all $n$ exceed $J$. The exact identity is

$$
\Lambda=2^{-J}\left(W_J+cT_J+\sum_ny_nT_{n+J}\right),
\qquad
|\Lambda|\le2^{-J}(|W_J|+C_J).
\tag{1}
$$

It controls the entire infinite remainder in the same parameters.
Also $u\equiv c\pmod{2^d}$.

**Proposition 1.** Suppose $W_J=0$ and $v\equiv0\pmod{2^d}$.
Then a rational value $S=a/b$, $b\ge1$, is impossible whenever

$$
bC_J<2^J,\qquad 3|c|b\le2^{d+1}.
\tag{2}
$$

*Proof.* Under rationality, $b\Lambda=au-bv$ is an integer.
The first inequality and (1) force it to be zero. The residue
congruence would then give $ca\equiv0\pmod{2^d}$. But
$1<S<3/2$, so
$0<|c|a<3|c|b/2\le2^d$, a contradiction. $\square$

For completeness, the elementary upper bound used here follows without
any numerical approximation: $\Phi_4=18$, while $T_4<6$ by
$\varphi(4+j)\le4+j$ with a strict inequality. Thus
$S=(18+T_4)/16<3/2$. Its first three summands total one, and later
summands are positive.

For a specific certificate, (2) excludes every positive denominator
through

$$
\min\left\{
\left\lfloor\frac{2^J-1}{C_J}\right\rfloor,\
\left\lfloor\frac{2^{d+1}}{3|c|}\right\rfloor
\right\}.
\tag{3}
$$

The second bound describes this sufficient test, not a necessary
restriction on all rational approximations.

**Corollary 2.** Suppose there is a sequence of such certificates with
$J\to\infty$,

$$
\frac{C_J}{2^J}\longrightarrow0,\qquad
\frac{|c|}{2^d}\longrightarrow0.
\tag{4}
$$

Then $S$ is irrational. In particular, with $c=1$, any $d\to\infty$
suffices in the second condition. One may seek
$d=\lceil\log_2(J+1)\rceil$ and $C_J=o(2^J)$.

*Proof.* Every fixed $b$ eventually satisfies both inequalities
in (2). $\square$

Corollary 7 below uses no leading coefficient. In its odd-kernel case,
the sufficient hypotheses are just an increasing support cutoff and
$C_J/2^J\to0$; the condition on $|c|/2^d$ is absent.

This is a genuine separation of the two requirements. A previous
argument inferred that the residue depth had to be close to the tail
depth by trying to exclude every denominator allowed by the tail bound
at the same finite order. Irrationality needs only that every fixed
denominator is eventually excluded; (3) can grow without its two
entries having comparable sizes. No certificate family satisfying (4)
has been constructed here.

There is also a slack version. Let $r$ represent $v$ modulo $2^d$.
Under rationality, the two conditions

$$
b(|W_J|+C_J)<2^J,\qquad
0<|ca-br|<2^d
\tag{5}
$$

give the same contradiction. For $|c|=1$ or $2$, $cS$ is not an
integer, so the second quantity is nonzero for every integer $r$.
The readily checked bound
$b(3|c|/2+|r|)\le2^d$ then suffices for its upper inequality.
For a different $c$, nonvanishing needs its own justification.

## Qualitative feasibility with leading coefficient one

**Proposition 3 (mixed integer image).** Fix $d\ge2$, $J\ge1$, and an
integer cutoff $B\ge d+2$. The vectors

$$
\left(\frac{\Phi_n}{2}\bmod 2^{d-1},\
      \frac{U_J(n)}2\right),\qquad n\ge B,
\tag{6}
$$

generate all of $\mathbb Z/2^{d-1}\mathbb Z\times\mathbb Z$.
Some finite prefix $B\le n\le R$ already generates it, but no endpoint
or coefficient bound is asserted.

*Proof.* Use the [[research/leads/totient_binary_series/integer_interpolation/_index|integer
span theorem]] for the distinct shifts

$$
-d+2,\ldots,-1,0,1,\ldots,J.
$$

The normalized values $\varphi(n+s)/2$ are integral on this domain.
Given integers $a,t$, that theorem supplies finitely supported integers
$y_n$, $n\ge B$, whose normalized shifted sums are $a$ at shift zero,
$t$ at shift $J$, and zero at all other listed shifts. The recurrence
for $\Phi_n/2$ gives

$$
\frac{\Phi_n}{2}
\equiv\sum_{i=0}^{d-2}2^i\frac{\varphi(n-i)}2
\pmod{2^{d-1}},
\qquad
\frac{U_J(n)}2
=\sum_{j=1}^{J}2^{J-j}\frac{\varphi(n+j)}2.
$$

The resulting sums in (6) are $(a\bmod2^{d-1},t)$. Taking finite
representations of the two standard generators proves the prefix
assertion. $\square$

Since $\Phi_J$ is even for $J\ge3$, choosing $a=0$ and
$t=-\Phi_J/2$ gives $v\equiv0\pmod{2^d}$ and $W_J=0$ with $c=1$.
This works beyond any prescribed cutoff $B\ge d+2$. In particular,
leading coefficient one is qualitatively feasible at every equal-depth
order as well, not merely at the orders of the finite witnesses.
Neither the possibly large target $\Phi_J/2$ nor the coefficients
provided by the span theorem have a useful height bound.

For $d\ge2$, $J\ge3$, let $\Gamma_{d,J}^{(1)}$ be the minimum of $C_J$
over these $c=1$ certificates supported on $n\ge d$.
Proposition 3 and well-ordering make this a finite attained minimum.
The open sufficient target is to find $d_\ell\to\infty$ and
$J_\ell\to\infty$ with

$$
\frac{\Gamma_{d_\ell,J_\ell}^{(1)}}{2^{J_\ell}}\longrightarrow0.
\tag{7}
$$

The existing $c=1$ equal-depth witnesses give finite examples only.

## What recurrence corrections preserve

There is a precise limitation on one way of correcting the scalar equation.
For finitely supported integers $z_n$, consider the coefficient change

$$
\delta y=\sum_nz_n(e_n-2e_{n-1}).
$$

Only use indices for which the resulting support is permitted. The
recurrences give the exact changes

$$
\delta u=0,\qquad
\delta v=\sum_nz_n\varphi(n),\qquad
\delta W_J=\sum_nz_n\bigl(\varphi(n+J)-2^J\varphi(n)\bigr).
$$

In particular, corrections with $\sum_nz_n\varphi(n)=0$ preserve
both $u$ and $v$, and hence preserve the actual real linear form
$\Lambda=uS-v$. If they make $W_J=0$ at a larger depth, (1) forces
$C_J\ge2^J|\Lambda|$. Such changes cannot by themselves drive the
normalized cost to zero from a fixed nonzero form.

For $c=1$ there is an unconditional statement even when $\delta v$ is
allowed to change. A family obtained solely by these corrections has
fixed $u$. If its residue depths tend to infinity, $u\equiv1\pmod{2^d}$
forces $u=1$. But $\Phi_4/2^4=9/8\le S<3/2$ implies
$\operatorname{dist}(S,\mathbb Z)\ge1/8$, so
$|\Lambda|=|S-v|\ge1/8$ for every integer $v$.
Every strict member of this family therefore has
$C_J\ge2^{J-3}$.

This rules out the fixed-$u$ correction scheme as a way to obtain (7).
It does not rule out recurrence-based constructions that also change
$u$, or integer-kernel directions that preserve $W_J$ while changing
the linear form. It needs no unproved Diophantine lower bound for
multipliers tending to infinity.

## Condition on the exact tail equation first

The [[research/leads/totient_binary_series/integer_interpolation/carry_criterion|forced-character
obstruction]] explains why uniform mixing in the two original
coordinates is an impossible requirement. A different exact identity
keeps the scalar equation separate.

Fix $d\ge2$, $J\ge3$, $c\ne0$, a finite set
$\mathcal N\subset\{n\ge d+2\}$, and an integer $h\ge1$.
Put $Q=2^{d-1}$, $A_n=\Phi_n/2$, $V_n=U_J(n)/2$, and define the finite
slice

$$
\Omega=\left\{y\in\{-h,\ldots,h\}^{\mathcal N}:
          \sum_ny_nV_n=-c\Phi_J/2\right\}.
$$

For $0\le t<Q$ set

$$
F_t=\sum_{y\in\Omega}
   \exp\left(\frac{2\pi i t}{Q}\sum_ny_nA_n\right).
$$

**Proposition 4 (conditional residue count).** The number of strict
certificates in this slice is exactly

$$
N_0=\frac1Q\sum_{t=0}^{Q-1}F_t
   =\frac1Q\left(|\Omega|+\sum_{t=1}^{Q-1}F_t\right).
\tag{8}
$$

Consequently $\Omega\ne\varnothing$ and
$\sum_{t=1}^{Q-1}|F_t|<|\Omega|$ suffice for a certificate of cost at most

$$
C_{\max}=|c|(J+2)+h\sum_{n\in\mathcal N}(n+J+2).
\tag{9}
$$

*Proof.* For each $y\in\Omega$, the average
$Q^{-1}\sum_{t=0}^{Q-1}\exp(2\pi i t\sum_n y_nA_n/Q)$ is one if
$\sum_ny_nA_n\equiv0\pmod Q$ and zero otherwise, by the finite
geometric sum. Sum over the slice. The triangle inequality gives
positivity under the stated sufficient bound. $\square$

The scalar character that obstructed the unconditioned argument is
constant on $\Omega$; it is part of the imposed equation, not a
nontrivial residue character in (8). There is no product factorization
of $F_t$ into independent coordinate sums, because membership in
$\Omega$ couples the coefficients.

For $d=\lceil\log_2(J+1)\rceil$, there are only $Q=O(J)$ residue
characters. Their phases use $\Phi_n/2$ modulo $Q$, hence only the last
$d-1=O(\log J)$ normalized totients at each $n$. The exact slice still
depends on the full $J$-term weights $U_J(n)$. Low modulus by itself
does not prove cancellation after this conditioning.

With fixed $c,h$ and indices $n=O(J)$, $|\mathcal N|=O(J)$, (9) is
$O(J^2)$. If a family in this range satisfied the hypotheses of
Proposition 4 and $d\to\infty$, Corollary 2 would apply. What remains
unproved is precisely the existence and sufficient residue spread of
these bounded slices. Full mixed integer image permits unbounded
coefficients and supplies neither fact. A direct construction satisfying
(7) need not use (8).

## Repair the residue with one odd kernel vector

There is a constructive alternative to estimating every $F_t$.
Use the notation $A_n,V_n,Q$ above and the weights $w_n=n+J+2$.
For an integer vector $x$ of finite support, write
$\|x\|_w=\sum_nw_n|x_n|$.

**Proposition 5.** Suppose integer vectors $a,z$ on the same permitted
support satisfy

$$
\sum_na_nV_n=-\Phi_J/2,\qquad
\sum_nz_nV_n=0,\qquad
\sum_nz_nA_n\ \hbox{is odd}.
\tag{10}
$$

Then there is a strict $c=1$ certificate with

$$
C_J\le J+2+\|a\|_w+\frac Q2\|z\|_w.
\tag{11}
$$

*Proof.* The odd integer $\sum_nz_nA_n$ is invertible modulo the power
of two $Q$. Choose an integer $t$, $|t|\le Q/2$, such that

$$
t\sum_nz_nA_n\equiv-\sum_na_nA_n\pmod Q.
$$

Then $y=a+tz$ preserves the scalar equation and has the required
zero residue. The triangle inequality gives (11). $\square$

Qualitative existence of both vectors on some finite prefix follows
from Proposition 3, by selecting the mixed targets
$(0,-\Phi_J/2)$ and $(1,0)$. This does not give useful costs, and
the first vector in (10) need not have residue zero in a quantitative
construction.

With $d=\lceil\log_2(J+1)\rceil$, it would suffice to construct
$\|a\|_w=o(2^J)$ and $\|z\|_w=o(2^J/J)$ along unbounded $J$.
Polynomial weighted costs for both would be more than sufficient.
The second task is one exact homogeneous scalar relation with an odd
normalized-prefix pairing. Ordinary homogeneous short-vector bounds
do not ensure that parity. The first task retains the prescribed
nonzero scalar target. This separates two concrete arithmetic
construction tasks without claiming either has been solved.

Proposition 6 and Corollary 7 below make the odd kernel vector itself
the linear form. For that route the vector $a$ is unnecessary, and
the sufficient cost for $z$ is $o(2^J)$ rather than $o(2^J/J)$.
Proposition 5 remains a valid way to construct the specified $c=1$
certificates.

The parity itself is local: for $n\ge4$,
$A_n\equiv\varphi(n)/2\pmod2$, by the recurrence for $\Phi_n$.
Thus the last condition in (10) is
$\sum_nz_n\varphi(n)/2$ odd. Nevertheless a cheap repair vector must
change the coefficient of $S$. If $\sum_nz_n2^n=0$, then
$|\sum_nz_nT_n|=|\sum_nz_n\Phi_n|\ge2$ by this oddness. The scalar
kernel condition also gives
$\sum_nz_nT_n=2^{-J}\sum_nz_nT_{n+J}$, so
$\|z\|_w\ge2^{J+1}$. This excludes only such zero-$u$ repair vectors
from the sufficient small-cost construction.

## Use the scalar kernel without residue repair

Fix integers $J\ge1$, $B\ge4$ and a finitely supported integer vector
$z=(z_n)_{n\ge B}$. No leading coefficient is included. Define

$$
u=\sum_nz_n2^n,\qquad v=\sum_nz_n\Phi_n,\qquad
W=\sum_nz_nU_J(n),\qquad
C=\sum_n|z_n|(n+J+2),\qquad D=|W|+C.
$$

The exact full-tail identity and support congruence are

$$
\Lambda=uS-v
=2^{-J}\left(W+\sum_nz_nT_{n+J}\right),\qquad
|\Lambda|\le 2^{-J}D,\qquad 2^B\mid u.
\tag{12}
$$

For a nonzero integer $m$, write $v_2(m)$ for the exponent of two in
$|m|$.

**Proposition 6 (valuation gap).** Suppose $v\ne0$ and put $t=v_2(v)$.
For a positive integer $b$, write $b=2^s b_{\mathrm{odd}}$ with
$b_{\mathrm{odd}}$ odd. Then $S$ cannot equal any $a/b$, $a\in\mathbb Z$,
if

$$
s+t<B,\qquad b_{\mathrm{odd}}D<2^{J+t}.
\tag{13}
$$

*Proof.* Under rationality, $b\Lambda=au-bv$ is an integer.
The first condition and $2^B\mid au$ imply the exact valuation

$$
v_2(au-bv)=s+t.
$$

This also holds when $u=0$, since $bv\ne0$. Consequently
$|b\Lambda|\ge2^{s+t}$. But (12) and the second inequality in (13)
give $|b\Lambda|\le bD/2^J<2^{s+t}$, a contradiction. $\square$

The weaker conditions $bD<2^J$ and $v_2(b)<B-t$ therefore suffice too.
Using the exact integer valuation in the proof gains the factor $2^t$
and removes the power of two in $b$ from the tail inequality.
Whenever $u\ne0$, $B$ in the valuation condition can be replaced by the
computed value $v_2(u)$, since the proof only uses the divisibility of $u$.

**Corollary 7 (families).** A sequence of vectors as above, indexed by
$\ell$, proves irrationality if $v_\ell\ne0$ and

$$
B_\ell-v_2(v_\ell)\longrightarrow\infty,\qquad
\frac{D_\ell}{2^{J_\ell+v_2(v_\ell)}}\longrightarrow0.
\tag{14}
$$

Indeed every fixed denominator eventually satisfies (13). All parameters
belong to the same sequence; no exchange of infinite sums or uniform
approximation is used beyond (12).

In particular, an **odd scalar-kernel vector** satisfies

$$
\sum_nz_nU_J(n)=0,\qquad
\sum_nz_n\frac{\Phi_n}{2}\ \hbox{odd}.
\tag{15}
$$

Here $t=1$, $D=C$, and it suffices to construct a sequence with
$B\to\infty$ and $C/2^J\to0$. There is no inhomogeneous target,
leading coefficient, or additional $1/J$ saving to supply. Since
$\Phi_n/2\equiv\varphi(n)/2\pmod2$ for $n\ge4$, the parity in (15)
can be tested on the local totient values.

For each fixed $B\ge4$ and $J\ge1$, Proposition 3 with residue depth
two and mixed target $(1\bmod2,0)$ proves qualitative existence.
Thus the minimum $\kappa_{B,J}$ of $C$ over vectors satisfying (15)
is finite and attained. No bound on its endpoint or magnitude follows.
The sufficient target is a sequence $B_\ell\to\infty$, $J_\ell\to\infty$
with $\kappa_{B_\ell,J_\ell}/2^{J_\ell}\to0$. Choosing $B=J$ is
convenient, not required.

**Corollary 8 (equal cutoff).** If $B=J\ge4$ and (15) holds, then every
positive denominator satisfying

$$
bC<2^{J+1}
\tag{16}
$$

is excluded. Equivalently the certificate excludes denominators through
$\lfloor(2^{J+1}-1)/C\rfloor$.

*Proof.* The oddness makes $z$ nonzero, so $C\ge2J+2\ge4$.
Equation (16) implies $b<2^{J-1}$ and hence
$v_2(b)+1<J$. Also $b_{\mathrm{odd}}C\le bC<2^{J+1}$.
Apply Proposition 6 with $t=1$. $\square$

An exact small example is $J=B=4$ and $z=e_4+e_8-e_{12}$.
The prefix values are
$\Phi_4=18$, $\Phi_8=344$, $\Phi_{12}=5592$, $\Phi_{16}=89616$,
so

$$
(U_4(4),U_4(8),U_4(12))=(56,88,144),\quad
W=0,\quad v=-5230,\quad u=-3824,\quad C=42.
$$

Thus $v/2=-2615$ is odd and $v_2(u)=4$. This checks the
kernel and parity interface, but $42>2^5$, so this particular
certificate excludes no positive denominator by (16).

If $u=0$ and $v\ne0$, (12) always gives
$D\ge2^J|v|$. In the exact kernel, this is
$C\ge2^J|v|$, and odd pairing forces $C\ge2^{J+1}$.
The assertion about $C$ needs $W=0$: for $J=B=4$,
$z=2e_4-e_5$ has $u=0$, $v=-4$, $W=58$ and $C=31<64$.
Its combined bound is $D=89\ge64$, as required.
Multiplying a vector by a power of two does not improve
$D/2^{J+v_2(v)}$ and decreases the support-based valuation gap;
it cannot manufacture (14).

## Feasible parity does not imply a small vector

For a nonempty finite permitted support $\mathcal N$, put
$V_n=U_J(n)/2$, $A_n=\Phi_n/2$ and
$g=\gcd_{n\in\mathcal N}V_n$. All $V_n$ are positive.
There is an integer vector with $V\cdot z=0$ and $A\cdot z$ odd
if and only if there are $i,j\in\mathcal N$ for which

$$
A_i(V_j/g)-A_j(V_i/g)\ \hbox{is odd}.
\tag{17}
$$

To prove sufficiency, use
$z_i=V_j/g$, $z_j=-V_i/g$, with other coordinates zero.
Conversely some $V_j/g$ is odd. If every minor in (17) is even,
then $A_i\equiv A_j(V_i/g)\pmod2$ for every $i$.
Every kernel vector therefore has even $A$-pairing. This characterizes
feasibility on a fixed support; the displayed two-coordinate solution
can have exponentially large cost.

**Proposition 9 (a short feasible interval).** For every sufficiently
large integer $J$ with $5\nmid J$, there is an odd scalar-kernel vector
supported on two indices in $[J,2J]$. In particular the interval
contains an odd kernel vector for every sufficiently large $J=2^m$.
This asserts feasibility, not a small weighted cost or full mixed
integer image.

The external input is the prime number theorem in arithmetic progressions for
fixed modulus: for each fixed reduced residue $r\bmod20$, $\pi(x;20,r)\sim
x/(8\log x)$. Its statement was inspected in the closing paragraph of [NIST DLMF
§27.11](https://dlmf.nist.gov/27.11) (version 1.2.8, released 2026-09-15) and in
the introductory fixed-modulus formula of [Tao's 2009
exposition](https://terrytao.wordpress.com/2009/09/24/the-prime-number-theorem-in-arithmetic-progressions-and-dueling-conspiracies/).
Its analytic proof is an external dependency, not reconstructed or independently
reviewed here.

*Proof.* Choose a prime $n_1\in[J,2J]$ with
$n_1\equiv3\pmod4$ and $n_1\equiv-J\pmod5$.
Separately choose a prime $p\in[2J,3J]$ with
$p\equiv3\pmod4$ and $p\equiv J\pmod5$, and put $n_2=p-J$.
Both specified classes are reduced modulo 20 because $5\nmid J$.
The fixed-modulus theorem makes each interval count asymptotic to
$J/(8\log J)$. Only four residue classes occur in either choice,
so a common threshold works as $J$ varies. No pair of numbers is
required to be simultaneously prime.

For $n\ge4$,
$A_n\equiv\varphi(n)/2\pmod2$ and
$V_n\equiv A_{n+J}\equiv\varphi(n+J)/2\pmod2$.
A multiple of 5 has totient divisible by 4. Since $n_1$ and $p$
are primes congruent to 3 modulo 4, the two parity pairs are

$$
(A_{n_1},V_{n_1})\equiv(1,0),\qquad
(A_{n_2},V_{n_2})\equiv(0,1)\pmod2.
$$

The indices are distinct for $J>5$: $n_1$ is a prime greater than
5, whereas $5\mid n_2$. The gcd $g_{12}=\gcd(V_{n_1},V_{n_2})$
is odd. Therefore

$$
z_{n_1}=V_{n_2}/g_{12},\qquad
z_{n_2}=-V_{n_1}/g_{12}
$$

give a scalar relation with odd $A$-pairing. $\square$

The construction has exactly the cost

$$
C=\frac{V_{n_2}(n_1+J+2)+V_{n_1}(n_2+J+2)}{g_{12}}
 <\frac{2^J(2J+2)(3J+2)}{g_{12}},
$$

using $U_J(n)<2^J(n+2)$. No useful lower bound on $g_{12}$ is
proved. Consequently the exhibited vector does not establish
$C=o(2^J)$. The minimum over all odd kernel vectors supported on
$[J,2J]$ is known to be finite along this subsequence; estimating
that minimum is still the open construction.

Even full mixed image and many short kernel vectors do not bound that
cost in a general positive integer row. Here is a precise comparison
family, **not the totient row**. For integers $M\ge3$ and $H\ge1$ set

$$
\widetilde V_i=Hi+1,\qquad \widetilde A_i=i,\qquad 1\le i\le M.
$$

The columns $(\widetilde A_i\bmod2,\widetilde V_i)$ generate
$\mathbb Z/2\mathbb Z\times\mathbb Z$. Indeed the first two scalar
entries are coprime, and the kernel vector
$(2H+1,-H-1,0,\ldots,0)$ has odd $\widetilde A$-pairing.
However, every odd-pairing kernel vector satisfies

$$
0=H\sum_i i z_i+\sum_i z_i,\qquad
\|z\|_1\ge\left|\sum_i z_i\right|
 =H\left|\sum_i i z_i\right|\ge H.
\tag{18}
$$

Meanwhile the $M-2$ independent vectors
$e_i-2e_{i+1}+e_{i+2}$ have norm four and even pairing.
Taking $H=2^J$ permits any polynomially growing dimension while
every odd vector still costs at least $2^J$. Thus qualitative
mixed image, positive entries of size $O(2^JM)$, and many small
homogeneous relations cannot alone prove the desired estimate.
The comparison says nothing against a construction using additional
arithmetic of the actual totient windows.

## A quantitative obstruction and the Fourier interface

On the finite support above let $w_n=n+J+2$. If a real $\theta$,
integers $m_n$ and $\epsilon>0$ satisfy

$$
\left|\theta V_n-\frac{A_n}{2}-m_n\right|
\le\epsilon w_n\qquad(n\in\mathcal N),
\tag{19}
$$

then every odd scalar-kernel vector on that support obeys

$$
C\ge\frac1{2\epsilon}.
\tag{20}
$$

In fact the sum of the errors in (19), weighted by $z_n$, is a
half-integer with odd numerator: the scalar part vanishes and
$A\cdot z$ is odd. Its absolute value is at least $1/2$ and at
most $\epsilon C$. This is a lower bound, not a converse producing
a small vector when such an obstruction is absent. The comparison
family in (18) has the unweighted obstruction
$\theta=1/(2H)$, $\epsilon=1/(2H)$.

Under the hypothetical rationality $S=a/b$ with $b$ odd, this
obstruction has an explicit location. Write

$$
I_n=a2^n-b\Phi_n=bT_n,\qquad
\theta_*=\frac{b}{2^{J+1}}.
$$

For $n\ge4$, $I_n\equiv2A_n\pmod4$ and

$$
\theta_*V_n
=\frac{I_n}{4}-\frac{I_{n+J}}{2^{J+2}}
\equiv\frac{A_n}{2}
       -\frac{bT_{n+J}}{2^{J+2}}\pmod1.
\tag{21}
$$

Taking $\epsilon=b/2^{J+2}$ in (19) recovers
$C\ge2^{J+1}/b$ for every odd kernel vector. This locates the
remaining arithmetic obstruction without assuming a distribution law.

For completeness, let $h\ge1$ be an integer,
$d_h(x)=(2h+1)^{-1}\sum_{m=-h}^h\exp(2\pi i mx)$, and set

$$
P(\theta)=\prod_{n\in\mathcal N}d_h(\theta V_n),\qquad
Q(\theta)=\prod_{n\in\mathcal N}d_h(\theta V_n+A_n/2).
$$

Integer orthogonality and the parity indicator give the exact number
of odd kernel vectors in the coefficient box:

$$
N_{\mathrm{odd}}
=\frac{(2h+1)^{|\mathcal N|}}2
  \int_0^1\bigl(P(\theta)-Q(\theta)\bigr)\,d\theta.
\tag{22}
$$

There is no assertion here that the difference is positive.
The bound
$|d_h'(x)|\le L_h=2\pi h(h+1)/(2h+1)$, together with
$|d_h|\le1$ and a telescoping product, turns (21) into the
uniform estimate

$$
\sup_{\theta\in\mathbb R}
|Q(\theta+\theta_*)-P(\theta)|
\le \frac{L_h b}{2^{J+2}}\sum_{n\in\mathcal N}(n+J+2).
\tag{23}
$$

Thus the shifted signed product is close to the unsigned one when
the displayed aggregate error tends to zero. In particular
$Q(\theta_*)$ is close to one in that regime. A per-coordinate
$O(bR/2^J)$ phase error alone does not justify calling an increasing
product a full-height peak, and no pointwise cancellation of two
major-arc contributions is proved. The exact count, obstruction
and error bound above are what is retained. Constructing cheap odd
vectors still requires quantitative information about the actual
totient scalar row beyond qualitative feasibility.

## Two shadows suffice

The
[[research/leads/totient_binary_series/integer_interpolation/shadows|shadows page]]
gives a conditional way to obtain the parity in (15). Two vectors of
$L=\{z:\sum_nz_nU_J(n)=0\}$ whose shadows $(u,v)=(\sum z_n2^n,\sum z_n\Phi_n)$
are not proportional exclude every denominator $b<2^J/C$ directly,
where $C$ bounds both costs. If any odd kernel vector exists, explicit
rounding against vectors with zero shadow produces one of cost at most
the sum of their costs plus $9(N-3)(R+J+2)^3$.
For $B_J=\max(4,\lfloor\log_2(J+1)\rfloor)$ on $[B_J,3J]$,
irrationality implies a subsequence of powers of two with odd cost
$O(J^4)$; the converse uses $B_J\to\infty$ in Corollary 7 above.
A fixed lower cutoff would leave sufficiently large dyadic denominator
parts untreated. These two-shadow constructions give no all-depth
bound or reverse implication on $[J,2J]$.

The [[research/leads/totient_binary_series/integer_interpolation/phase_transference|phase
comparison]] makes (19) quantitative in the other direction. For the
actual totient row on $[J,2J]$ along sufficiently large powers of two,
the minimum odd cost is $o(2^J)$ if and only if the least weighted
phase error $\epsilon_J$ satisfies $\epsilon_J2^J\to\infty$.
That estimate is open. The comparison family (18), the gcd in
Proposition 9, and the odd-box integral (22)--(23) retain their stated
scope. Arithmetic control of those quantities might still construct a
small odd vector without first producing two independent shadows.

The separate
[[research/leads/totient_binary_series/integer_interpolation/phase_localization|arithmetic
localization]] uses $\varphi(3k)=2\varphi(2k)$ within the short
support. It proves $S\notin\mathbb Q$ if and only if
$\epsilon_J2^J$ is unbounded along powers of two, and hence if and
only if an odd $o(2^J)$ family exists there along a subsequence.
Its finite sufficient test controls the whole tail through (21)'s
underlying exact identity. No growing family passing that test is known.

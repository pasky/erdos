---
name: research/prime_binary_new_attack/phase_transport
title: Phase transport and the dephased prime-tail sum
desc: |
  Composite deletion yields two signed sums with different unconditional
  endpoints. Integer carries make their corresponding root increments
  agree. Removing each root's phase retains the actual carry coefficient.
  A periodic reference and an odd multiple of every denominator give
  the common rationality endpoint 3N/2. The signed cofactor estimate
  needed to improve that endpoint remains unproved.
created: 2026-10-17T14:40:42Z
updated: 2026-10-17T23:52:10Z
---

# Phase transport and the dephased prime-tail sum

***

This is Plasma AI's author-recorded analysis of a proposed route to
[[problems/irrationality/E0251/_index|Problem 251]]. It has not been
independently reviewed. The fixed-saving prime estimate remains unproved,
including for odd denominator part $d=1$. Notation is that of the
[[research/prime_binary_new_attack/proof_sketch|canonical sketch]]:
$g_n=p_{n+1}-p_n$, $h_n=g_n/2$ for $n\ge2$,
$H_n=\sum_{j\ge0}h_{n+j}2^{-j-1}$, $I_X=\{n:X<p_n\le2X\}$ and
$N_X=|I_X|$. Write $e(t)=\exp(2\pi it)$ and $\|t\|$ for the distance
from $t$ to the nearest integer. Set $c_n=dH_n$, without initially
assuming these real numbers are integers.

## The original transport

Fix a positive odd $d$ and an odd prime $q$ with $L=2^{q-1}-1>d$.
Let $W$ be the odd positive integers not divisible by $q$. For $m\in W$, let $w(m)$ be
the half-gap tail of $W$ from $m$. Its half-gaps are periodic, with one
$2$ and $q-2$ ones in each period. Thus $w(m)$ depends on $m$ modulo
$2q$ and takes each value $1+2^u/L$, $0\le u\le q-2$, on one admissible
class. Put

$$
\beta_{d,q}=\frac1{q-1}\sum_{u=0}^{q-2}e\Bigl(\frac{d2^u}{L}\Bigr),
\qquad \delta_{d,q}=1-\operatorname{Re}\beta_{d,q}.
$$

Here $0<\delta_{d,q}<2$: $L$ divides no $d2^u$, and an odd denominator
cannot represent a half-integer modulo one. For $d=1$, $q=3$ one has
$\beta=-1/2$ and $\delta=3/2$; for $d=3$, $q=5$ one has $\beta=-1/4$.

Let $Y=2X+D$ with $D=\lfloor K(\log X)^2\rfloor$ and
$K=\lceil12\log_2\log X\rceil$. Starting from $W$, delete the composites
of $W\cap(X,Y]$ in increasing order. Take $X>q$, so every intermediate
set contains every prime above $X$. The roots are the actual primes
$p_n$, $n\in I_X$. For a set $T$ put
$F(T)=\sum_{n\in I_X}e(dH_T(p_n))$.

The prime number theorem in the fixed classes modulo $2q$ gives
$F(W)=\beta_{d,q}N_X+o(N_X)$. Adding points to a sequence lowers its
tails. At a root whose $K$th successor lies below $Y$, the final tail
therefore differs from $H_n$ by at most $2^{-K}H_{n+K}$. The span sum
is $O(KX)$, so the roots with span above $D$ number $O(N_X/\log X)$.
The canonical sketch's mean-tail bound (T) now gives

$$
F(T_{\rm fin})=\sum_{n\in I_X}e(c_n)+o(N_X).
\tag{P0}
$$

If $S=a/(2^sd)$, Lemma A of that sketch makes $c_n$ a positive integer
for all sufficiently large $n$. The real change of $F$ is then
$(\delta_{d,q}+o(1))N_X$.

## Exact increments and prime endpoints

**Proposition P1 (original increment).** Let $m\in W$ be composite with
$p_r<m<p_{r+1}$, and suppose all composites of $W$ in $(X,m)$ have been
deleted. For a root $p_n$ with $X<p_n\le p_r$, put $j=r-n+1$ and

$$
P_{r,j}=2^{j-1}p_n-\sum_{k=0}^{j-2}2^kp_{r-k}.
$$

Then

$$
H_{\rm before}(p_n)=\frac{m-P_{r,j}}{2^{j+1}}+\frac{w(m)}{2^j},
\qquad
H_{\rm after}(p_n)=\frac{m-P_{r,j}}{2^{j+1}}+\frac{2w(m)}{2^j}.
$$

*Proof.* For an increasing sequence $x_0<x_1<\cdots$, its half-gap tail
at $x_0$ is $\sum_{\ell\ge1}(x_\ell-x_0)2^{-\ell-2}$. Before deletion,
the successors of $p_n$ are $p_{n+1},\ldots,p_r$, followed by $m$ and
the elements of $W$ above $m$. This gives the first formula. If $m^+$
is the next element of $W$, the recurrence for $w$ gives
$m^++2w(m^+)=m+4w(m)$, which gives the second. $\square$

The original complex increment at this root is consequently

$$
e\Bigl(\frac{d(m-P_{r,j})}{2^{j+1}}\Bigr)
\left(e\Bigl(\frac{2dw(m)}{2^j}\Bigr)
-e\Bigl(\frac{dw(m)}{2^j}\Bigr)\right).
\tag{P1}
$$

This expression involves a finite prime prefix and no tail. That fact
concerns the original increment; the dephased increment below is different.

**Proposition P2 (gap endpoints).** Put
$\gamma_j(x)=e(d(x+2w(x))/2^{j+1})$ for $x\in W$. The increment (P1)
is
$e(-dP_{r,j}/2^{j+1})(\gamma_j(m^+)-\gamma_j(m))$.
Its sum over the composites of $W$ in a complete prime gap is

$$
e\Bigl(-\frac{dP_{r,j}}{2^{j+1}}\Bigr)
\bigl(\gamma_j(p_{r+1})-\gamma_j(p_r^+)\bigr),
$$

where $p_r^+$ is the least element of $W$ above $p_r$. Equivalently, put

$$
H_n^{(j)}=\sum_{i<j}\frac{h_{n+i}}{2^{i+1}}+
\frac{w(p_{n+j})}{2^j}.
$$

The complete rank-$j$ contribution is
$\sum_n(e(dH_n^{(j)})-e(dH_n^{(j-1)}))$, with the root and boundary
restrictions of the deletion window.

*Proof.* The identity for $m^+$ in P1 gives the displayed difference of
$\gamma_j$. Consecutive elements of $W$ inside a prime gap are exactly
the sites deleted there, so the sum telescopes. The two endpoint tails
are obtained by revealing respectively $j-1$ and $j$ actual successors.
$\square$

The periodic site weight in P1 has zero mean over a period and partial
sums of absolute value at most $2$ along $W$. These facts do not estimate
the sum of its prime-gap endpoints. A regrouping by least prime factor
still has to control the coefficients supplied by those endpoints.

## The unweighted phase-deficit alternative

By (P0), a fixed saving for the original real change is equivalent to

$$
\operatorname{Re}\sum_{n\in I_X}e(d2^{n-2}S)
\le(1-\varepsilon_d)N_X
\quad\text{on unbounded scales},
\tag{UPD}
$$

because $H_n-2^{n-2}S$ is an integer for $n\ge3$.

**Lemma P3 (digit-change form).** For fixed odd $d$, (UPD) holds for some
$\varepsilon_d>0$ if and only if the binary expansion of $dS$ has, for
some $\kappa_d>0$ and unbounded $X$, at least $\kappa_dN_X$ positions
$n\in I_X$ where its $n$th and $(n+1)$th digits differ.

*Proof.* Use the expansion of $x=dS$ that does not end in ones. A change
between digits $k+1$ and $k+2$ gives $\{2^kx\}\in[1/4,3/4]$, hence
$1-\cos(2\pi2^kx)\ge1$. Conversely, put
$\eta^2=\varepsilon_d/(4\pi^2)$. Since
$1-\cos2\pi t\le2\pi^2\|t\|^2$ and is at most $2$, (UPD) forces at
least $\varepsilon_dN_X/4$ indices with $\|2^{n-2}x\|\ge\eta$.
Choose a fixed integer $\ell$ with $2^{-\ell}<\eta$. At each such index,
the next $\ell$ binary digits cannot all agree, so there is a digit change
among them. Each change is charged at most $\ell$ times. Shifting the
consecutive index interval $I_X$ by a fixed number alters the counts by
$O_\eta(1)$. Both implications follow after reducing the positive
constants if necessary. $\square$

This positive-density condition is stronger than merely saying that $dS$
is not dyadic: an irrational number can have digit changes of density zero.
It would exclude a reduced odd denominator dividing $d$. It is unknown
here, including for $d=1$.

The combined contribution of ranks beyond
$J=\lceil\log_2\log X\rceil+C$ is $O_d(2^{-C}N_X)$. Indeed its endpoint
is $\sum_n(e(c_n)-e(dH_n^{(J)}))$, whose modulus is bounded using
$0\le H_n-H_n^{(J)}\le2^{-J}H_{n+J}$ and (T). The earlier ranks need
control of consecutive prime residues up to this growing length. Already
the rank-one part is

$$
\sum_{n\in I_X}(-1)^{h_n}e\Bigl(\frac{dw(p_{n+1})}{2}\Bigr)
-\sum_{n\in I_X}e(dw(p_n)).
$$

Fixed-modulus PNT estimates the second sum. It does not estimate the first
sum's correlation between the two prime classes modulo $4$ and the next
prime's class modulo $q$. No asymptotic for that correlation is supplied
by the inspected sources. This describes one attempted proof of (UPD),
without asserting that every proof must estimate all of these parts.

## The dephased sum and its separate endpoint

For a composite $m\in W$ in $(p_r,p_{r+1})$, define

$$
z_m=\frac{m-p_r}{2},\qquad B_m=2c_r-dz_m,
$$

and the uniformly absolutely convergent weight

$$
T_{d,q}(B,w)=\sum_{j\ge1}
\left(\cos\frac{2\pi(B-2dw)}{2^j}
-\cos\frac{2\pi(B-dw)}{2^j}\right).
$$

The $j$th term has modulus at most $4\pi d2^{-j}$, so $|T|\le4\pi d$.
Set

$$
Q_{d,q}(X)=\sum_{\substack{X<m\le2X\\m\in W\text{ composite}}}
T_{d,q}(B_m,w(m)).
$$

The recurrence $c_{n+1}=2c_n-dh_n$ gives the exact identities

$$
dH_{\rm before}(p_n)=c_n-\frac{B_m-dw(m)}{2^j},\qquad
dH_{\rm after}(p_n)=c_n-\frac{B_m-2dw(m)}{2^j}.
\tag{P4a}
$$

Thus the real term used in $Q$ is the real part of the original complex
increment multiplied by $e(-c_n)$. Under rationality this factor is one.
Without rationality it depends on the root and must be retained.

**Proposition P4 (dephased endpoint).** For fixed $d,q$, unconditionally,

$$
Q_{d,q}(X)=N_X-
\operatorname{Re}\sum_{n\in I_X}e(dw(p_n)-c_n)
+O_{d,q}(\log X).
\tag{P4}
$$

In particular $-o(N_X)\le Q_{d,q}(X)\le2N_X+o(N_X)$. Under
$S=a/(2^sd)$, fixed-modulus PNT makes
$Q_{d,q}(X)=(\delta_{d,q}+o(1))N_X$.

*Proof.* Define, for real $t$,

$$
\mathcal V(t)=\sum_{j\ge1}(1-\cos(2\pi t/2^j)).
$$

It converges, is $O(1+\log(1+|t|))$, and satisfies
$\mathcal V(2t)=\mathcal V(t)+1-\cos2\pi t$. Put
$u_r=c_r-dw(p_r)$. For successive sites $m,m^+$ of $W$ inside one
prime gap,
$B_{m^+}-dw(m^+)=B_m-2dw(m)$ by the recurrence for $w$.
At the first site the initial argument is $2u_r$; after the last site
it is $u_{r+1}$, using $c_{r+1}=2c_r-dh_r$. If there are no sites,
these two arguments agree. Thus direct telescoping of the site weights
in a complete gap gives, for every $j\ge1$,

$$
\cos(2\pi u_{r+1}/2^j)-\cos(2\pi(2u_r)/2^j).
$$

Absolute convergence permits summing in $j$. The entire gap contributes

$$
\mathcal V(2u_r)-\mathcal V(u_{r+1})
=\mathcal V(u_r)-\mathcal V(u_{r+1})+1-\cos(2\pi u_r).
\tag{P4b}
$$

Sum over the complete prime gaps inside $(X,2X]$. The potential terms
telescope. The PNT bound $p_k\ll k\log(2k)$ gives $H_r=O(X)$ for the
primes adjacent to $X$ or $2X$, so the two remaining potentials are
$O_{d,q}(\log X)$.

The at most two partial boundary gaps also telescope. On any consecutive
segment of sites in one prime gap, the sum of $T$ is the difference of
$\mathcal V$ at the first argument $B_m-dw(m)$ and the last argument
$B_m-2dw(m)$. Both arguments are $O_{d,q}(X)$: the preceding carry is
$O_d(X)$, the site lies in $(X,2X]$, and $w<2$. Thus each partial gap
contributes $O_{d,q}(\log X)$, regardless of its number of sites.
The complete-gap root set differs from $I_X$ by $O(1)$ indices. This
proves (P4), without a short-gap theorem; the sign of the exponent does
not affect its real part. If $c_n$ is
integral eventually, the endpoint sum is $\beta_{d,q}N_X+o(N_X)$ by PNT
in the fixed progressions. $\square$

The sufficient upper target for this observable is

$$
Q_{d,q}(X)\le(\delta_{d,q}-\varepsilon_d)N_X
\quad\text{on unbounded scales},\qquad \varepsilon_d>0.
\tag{FPT}
$$

Its proof may use eventual integer carries. Alternatively, an unconditional
proof would suffice. By (P4), the latter target, with a positive margin
adjusted for $o(N_X)$, is the weighted correlation bound

$$
\operatorname{Re}\sum_{n\in I_X}e(dw(p_n)-c_n)
\ge(\operatorname{Re}\beta_{d,q}+\varepsilon_d)N_X.
\tag{WC}
$$

This is a different unconditional endpoint from (UPD). To see exactly where
they meet, put $A_r=4c_r+dp_r$. For the roots of P1,

$$
A_r=2^{j+1}c_{r-j+1}+dP_{r,j}.
\tag{P5}
$$

Replacing $e(A_r/2^{j+1})$ by $e(dP_{r,j}/2^{j+1})$ is valid under
integer carries. For real carries it discards the factor $e(c_{r-j+1})$
and changes the observable. At each actual root the substituted expression
is the conjugate of (P1). With the original root and deletion-window
restrictions, its real sum therefore has the unweighted endpoint from
(P0), whereas $Q$ has (P4). Under rationality the two totals agree up to
$o(N_X)$; this does not identify their unconditional bounds.
Neither endpoint identity prohibits an upper argument from using integrality.

## The signed cofactor estimate that remains

A direct arithmetic attempt keeps the coefficient in (P5). The complex
expression whose real part is the $j$th term of $T$ can be written

$$
a_{r,j}v_j(m),\qquad
a_{r,j}=e(A_r/2^{j+1}),\qquad
v_j(m)=e(-dm/2^{j+1})b_j(m),
$$

where $b_j(m)=e(-2dw(m)/2^j)-e(-dw(m)/2^j)$ on $W$, and is zero off $W$.
The Fourier coefficient absolute sum of $b_j$ on modulus $2q$ is at most

$$
\sqrt{2q}\min(2,4\pi d2^{-j}).
$$

This follows from Cauchy--Schwarz and Parseval on that finite group. The
sum of these bounds over $j\ge1$ is finite, depending only on $d,q$.
Truncation at $J=\lceil3\log_2\log X\rceil$ costs
$O_d(X2^{-J})=o(N_X)$. The displayed frequencies have denominator at most
$q2^{J+1}=O_q((\log X)^3)$.

Writing each composite uniquely as $m=\ell v$, with $\ell=P^-(m)$,
gives the exact truncated arithmetic target

$$
\operatorname{Re}\sum_{j\le J}\sum_{\substack{\ell\le\sqrt{2X}\\\ell\text{ prime}}}
\ \sum_{\substack{X<\ell v\le2X\\v\ge\ell,\ P^-(v)\ge\ell}}
a_{\pi(\ell v),j}v_j(\ell v).
\tag{P6}
$$

The sum of (P6) and the stated truncation error must be bounded by the
right side of (FPT). A small Fourier coefficient norm alone does not do
this: $a_{\pi(m),j}$ is selected by the entire actual prime gap containing
$m$. Under rationality (P5) expresses it through $j$ preceding primes,
with $j$ growing. No independence from $\ell$ follows.

Two direct estimates fail to supply the saving.

- Partial summation against a progression discrepancy pays the variation of
  $a_{\pi(m),j}$. The available bound is $2N_X+O(1)$, since this coefficient
  can change at every prime. Even granting a global unweighted discrepancy
  $O_A(X/(\log X)^A)$, this argument only yields an error of order
  $XN_X/(\log X)^A$, which is larger than $N_X$ for every fixed $A$.
  This rejects that use of the variation bound, not a weighted
  Bombieri--Vinogradov theorem proved with additional structure.
- The shortcut $T_{1,3}(B,w)\le2$ for positive integer $B$ is false. At
  $B=3$, $w=4/3$, the rank-one term is zero, the next two terms are
  $\sqrt3$ and $1/\sqrt2$, and every remaining term is positive. Thus
  $T_{1,3}(3,4/3)>2$. A count of rough sites cannot be multiplied by $2$
  without a further bound on the carries at those sites. This is a
  counterexample to the proposed pointwise function bound; it asserts
  no occurrence of that carry at an actual prime gap and does not
  refute (FPT).

The inspected statement of
[[../library/primes/gafni_2025_rough_numbers_between_consecutive_primes/_index|Gafni and Tao's rough-number theorem]]
in arXiv:2508.06463v1, Theorem 1.1, places some integer with least prime
factor at least the gap length inside all but $O(X/(\log X)^2)$ gaps
whose initial prime is in $[X,2X]$. It does not select the sites
weighted by (P6), nor raise that least-factor threshold to $X^{1/3}$.
Its Lemma 2.1 on short-interval rough counts uses
$H=(\log X)^\alpha$, $z=\exp((\log X)^\beta)$ with
$0<\beta<\alpha<1$. Neither statement supplies the missing signed,
carry-dependent estimate. Only these statements and their stated parameter
ranges are used in this comparison; they are not new premises of a proof.

## The sign of the dephased target

This section is author-recorded. It shows that the unconditional form of
(FPT) asks for a correlation between the binary digits of $dS$ and the
primes. At $d=7$ the correlation must be positive for the reference family
specified here: $q$ prime and $2^{q-1}-1>d$. Proposition P9 uses a
different reference and multiplier, for which the corresponding target
does not require a positive correlation. The restriction on this family
is not a restriction on every dephased transport.

For $n\ge3$ the number $H_n-2^{n-2}S$ is an integer. Indeed, iterating
$G_{k+1}=2G_k-g_k$ from $G_1=S-2$ gives

$$
H_n=2^{n-2}S-2^{n-1}-\sum_{1\le k<n}2^{n-2-k}g_k,
$$

and each term of the last sum is an integer when $n\ge3$: the term $k=n-1$
is $g_{n-1}/2$ with $g_{n-1}$ even, and the term $k=1$ is $2^{n-3}$.
Consequently $c_n\equiv d2^{n-2}S\pmod1$ for $n\ge3$, without any
hypothesis on $S$.

**Lemma P7 (the dephased target as a digit correlation).** Fix an odd
$d$, an odd prime $q$ with $2^{q-1}-1>d$, and $\varepsilon>0$. Along any
sequence of scales $X\to\infty$,

$$
Q_{d,q}(X)\le(\delta_{d,q}-\varepsilon)N_X+o(N_X)
$$

holds if and only if

$$
\operatorname{Re}\sum_{n\in I_X}e\bigl(dw(p_n)-d2^{n-2}S\bigr)
\ge(\operatorname{Re}\beta_{d,q}+\varepsilon)N_X-o(N_X).
\tag{P7}
$$

*Proof.* Substitute the congruence for $c_n$ into Proposition P4 and use
$\delta_{d,q}=1-\operatorname{Re}\beta_{d,q}$. $\square$

So an unconditional proof of (FPT) at $(d,q)$ is a lower bound for the
correlation between the phase $e(-d2^{n-2}S)$, which records the binary
digits of $dS$ from position $n-1$ on, and the phase $e(dw(p_n))$, which
records the class of $p_n$ modulo $2q$. When
$\operatorname{Re}\beta_{d,q}\ge0$ the required correlation is a positive
proportion of $N_X$.

**Proposition P8 (the denominator $7$).** For every odd prime $q$ with
$2^{q-1}-1>7$, that is $q\ge5$, one has $\operatorname{Re}\beta_{7,q}\ge0$.
Precisely, $\operatorname{Re}\beta_{7,5}=1/8$,
$\operatorname{Re}\beta_{7,7}=0$, and $\operatorname{Re}\beta_{7,q}>0$
for $q\ge11$.

*Proof.* Put $L=2^{q-1}-1$; then
$(q-1)\operatorname{Re}\beta_{7,q}=\sum_{0\le u\le q-2}\cos(2\pi\rho_u/L)$
with $\rho_u\equiv7\cdot2^u\pmod L$, $0\le\rho_u<L$.

For $q=5$, $L=15$ and the residues are $7,14,13,11$. Their negatives are
$8,1,2,4$, so the residues and their negatives are the eight units modulo
$15$. The cosine sum is therefore half the Ramanujan sum
$\sum_{(r,15)=1}e(r/15)=\mu(15)=1$, and
$\operatorname{Re}\beta_{7,5}=(1/2)/4=1/8$.

For $q=7$, $L=63$ and $\rho_u/L\equiv2^u/9\pmod1$. The residues of
$2^u$ modulo $9$
for $0\le u\le5$ are $1,2,4,8,7,5$, the six units modulo $9$. Their sum
of $e(r/9)$ is $\mu(9)=0$, so $\operatorname{Re}\beta_{7,7}=0$.

For $q\ge11$, every $u\le q-7$ has
$\rho_u=7\cdot2^u\le(7/64)2^{q-1}$, hence $\rho_u/L<1/8$ and
$\cos(2\pi\rho_u/L)>1/\sqrt2$. The remaining $5$ terms are at least $-1$
each. For $q\ge17$ this gives a sum at least $(q-6)/\sqrt2-5>0$. For
$q=11$ and $q=13$ the exact residues $\rho_u$ are $7\cdot2^u$ for
$u\le q-4$ and then $7\cdot2^{q-3}-L$, $7\cdot2^{q-2}-3L$. The fractions
$\rho_u/L$ for $u=q-6,\ldots,q-2$ lie respectively in the intervals
$(0.218,0.220)$, $(0.437,0.438)$, $(0.875,0.876)$, $(0.750,0.752)$ and
$(0.500,0.504)$, and those for $u\le q-7$ are below $0.110$. Hence the
first $q-6$ cosines exceed $3/4$: their arguments are less than $7/10$,
and $\cos\theta\ge1-\theta^2/2$. The cosines at $u=q-6$ and $u=q-3$
are positive, the one at $u=q-4$ exceeds $1/\sqrt2$, and the other two
are at least $-1$. The sum is at least
$(3/4)(q-6)+1/\sqrt2-2>0$ for $q\in\{11,13\}$. $\square$

**Consequence for the restricted reference family at $d=7$.** An
unconditional proof of (FPT) at $d=7$, for a prime $q\ge5$, would prove

$$
\operatorname{Re}\sum_{n\in I_X}e\bigl(7w(p_n)-7\cdot2^{n-2}S\bigr)
\ge(\varepsilon-o(1))N_X
$$

on unbounded scales, by (P7) and Proposition P8. The stronger bound in
(P7) requires an excess of $\varepsilon N_X$ above the reference mean
$\operatorname{Re}\beta_{7,q}N_X$. That excess is absent in two situations.
If $S=a/(2^s\cdot7)$,
then $c_n$ is eventually an integer and the sum is
$(\beta_{7,q}+o(1))N_X$ by the prime number theorem in the fixed classes,
so (FPT) fails, as it must under the hypothesis it is meant to refute.
If instead the pairs $(\{7\cdot2^{n-2}S\},p_n\bmod2q)$, $n\in I_X$, are
asymptotically equidistributed on $[0,1)$ times the $q-1$ admissible
classes, as the usual digit heuristics for $S$ predict, the sum is
$o(N_X)$ and (FPT) fails again. Neither hypothesis is proved here; the
statement is that unconditional (FPT) at $d=7$ would assert a correlation
between the digits of $7S$ and the primes modulo $2q$, not that (FPT) is
disproved. The same reasoning applies to every odd $d$ for which no
admissible $q$ has $\operatorname{Re}\beta_{d,q}<0$. For the cases computed
above, $\operatorname{Re}\beta_{1,3}=-1/2$, $\operatorname{Re}\beta_{3,5}=-1/4$
and $\operatorname{Re}\beta_{5,5}=-1/2$, so (FPT) at those pairs is
compatible with that equidistribution.

The original transport carries no such sign restriction. Its sufficient
target (UPD) asks for
$\operatorname{Re}\sum_{n\in I_X}e(d2^{n-2}S)\le(1-\varepsilon_d)N_X$,
which the same equidistribution hypothesis supports for every odd $d$.
Under integer carries the substitution (P5) replaces the coefficient of
(P6) by the prefix phase $e(dP_{r,j}/2^{j+1})$; with that coefficient, at
each actual root, the site terms are the conjugates of the original
increments (P1), and their real sum has the endpoint of (P0). An attack
on (P6) can use this prefix coefficient under rationality. Keeping instead
the real-carry coefficient and the reference restriction $L>d$ leaves
the correlation displayed above. That restriction is unnecessary for
the identities (P4)--(P6). For example, $d=7,q=3$ has $L=3<d$ and
$\beta_{7,3}=-1/2$. The following construction handles every odd $d$.

## A resonant reference for every denominator

This construction is author-recorded. It changes the reference parameters
of the phase sum; it changes none of the parameters of the deletion-sign
or shorter-span counts.

**Proposition P9 (constant real reference).** Let $d\ge1$ be odd. Write
$d=3^\nu d_0$, where $3\nmid d_0$, and put

$$
q=2\cdot3^\nu+1,\qquad L=2^{q-1}-1,\qquad
k=\frac{L}{3^{\nu+1}},\qquad b=kd=\frac{d_0L}{3}.
\tag{P9a}
$$

Then $k$ and $b$ are positive odd integers. The integer $q$ need not be
prime. For the odd integers $W$ not divisible by $q$, its half-gap tail
$w$ satisfies

$$
\operatorname{Re}e(bw(m))=-\frac12\qquad(m\in W).
\tag{P9b}
$$

Define $C_n=bH_n$, and use multiplier $b$ in place of $d$ in the
definitions of $B_m,T_{d,q}$ and $Q_{d,q}$. Thus the new gap argument
is $B_m^{(b)}=2C_r-b(m-p_r)/2$. For these parameters,

$$
Q_{b,q}(X)=N_X-
\operatorname{Re}\sum_{n\in I_X}e(bw(p_n)-C_n)
+O_{b,q}(\log X).
\tag{P9c}
$$

If $S=a/(2^sd)$, then for every sufficiently large $X$,

$$
Q_{b,q}(X)=\frac32N_X+O_{b,q}(\log X).
\tag{P9d}
$$

*Proof.* The elementary valuation identity
$v_3(4^{3^\nu}-1)=\nu+1$ follows by induction. The initial value is
$v_3(4-1)=1$. If $A\equiv1\pmod3$, then
$A^2+A+1\equiv3\pmod9$, and factoring $A^3-1$ raises the valuation
by exactly one. Consequently $k$ is an integer. Both $L$ and its divisor
$3^{\nu+1}$ are odd, so $k$ and $b$ are odd.

The half-gap word of $W$ has period $q-1$, with one $2$ and $q-2$
ones, also when $q$ is composite. Its tails are precisely
$1+2^u/L$, $0\le u\le q-2$. Therefore

$$
bw(m)\equiv \frac{d_0 2^u}{3}\pmod1.
$$

The numerator is not divisible by $3$, proving (P9b). Every prime above
$q$ belongs to $W$. The proof of P4 uses only this containment, the
periodic-tail recurrence and the boundary estimates; it needs neither
primality of $q$ nor $L>b$. It therefore proves (P9c). Under the stated
rationality hypothesis, $C_n=k(dH_n)$ is integral for
$n\ge\max(s+2,3)$. Each real summand in (P9c) is then $-1/2$, proving
(P9d). No progression equidistribution is needed for this real endpoint.
$\square$

All parameters in (P9a) are fixed once $d$ is fixed. In particular,
$d=1$ and $d=7$ both permit $q=3$ and $b=d$; for $d=3$ the construction
gives $q=7,b=21$. Large constants depending on $d$ do not obstruct the
limit $X\to\infty$.

A prime reference can also be kept within the original parameter
restriction, if useful for an arithmetic estimate. Let
$t=\operatorname{ord}_{3d}(2)$, which is even, choose a fixed prime
$q\equiv1\pmod t$ by PNT in a fixed progression, and set
$L=2^{q-1}-1$, $b=L/3$. Then $3d\mid L$, so $b$ is an odd multiple
of $d$ and $L>b$. Again $bw\equiv2^u/3\pmod1$ at every site.
Thus the common endpoint $3N_X/2$ is available even with $q$ prime and
$L$ larger than the multiplier. This choice does not give an estimate
for the signed sum either.

The full sufficient arithmetic target for this reference is

$$
Q_{b,q}(X)\le\left(\frac32-\varepsilon_d\right)N_X
\quad\text{on unbounded scales},\qquad \varepsilon_d>0.
\tag{RFPT}
$$

It may be proved using eventual integrality of $C_n$. An unconditional
proof would also suffice. In particular, the joint decorrelation
$\sum_{n\in I_X}e(bw(p_n)-C_n)=o(N_X)$ would give
$Q_{b,q}(X)=N_X+o(N_X)$ and hence (RFPT). This decorrelation is an
unproved sufficient input, not an estimate obtained from the construction.
Unlike the restricted family in P8, this reference is compatible with
that hypothesis for every odd denominator.

The exact arithmetic sum is still (P6), with $b,C_r$ in place of $d,c_r$.
All cofactors, the condition $P^-(v)\ge\ell$, and the coefficient
$e((4C_r+bp_r)/2^{j+1})$ remain. With
$J=\lceil3\log_2\log X\rceil$, the omitted ranks cost
$O_b(X2^{-J})=o(N_X)$, and the Fourier coefficient norm is bounded by a
constant depending on $b,q$. The required strict upper bound for this
actual-prime sum is unknown. Changing the reference does not estimate it.

### Two attempted ways to estimate the resonant sum

Increasing the frequency does not move a fixed contribution into a small
error. If $B$ is an integer and $bw\equiv\pm1/3\pmod1$, then for every
integer $u\ge0$,

$$
T_{2^ub,q}(2^uB,w)=T_{b,q}(B,w).
\tag{P9e}
$$

Indeed the first $u$ summands on the left vanish: both cosines are
$-1/2$, since their integer parts disappear and multiplication by a
power of two preserves the two nonzero residues modulo three. Reindexing
the remaining summands gives the right side. Under rationality this
applies at every composite site, but the higher-rank weight is exactly
the old weight. In particular, the general truncation bound becomes
$O_b(2^uX2^{-J})$; it cannot be kept at $O_b(X2^{-J})$ while increasing
the multiplier.

The
[[../library/arithmetic_functions/tao_2025_quantitative_correlations_problems_prime_factors_consecutive/_index|Tao--Teräväinen method for the prime-factor series]]
was also examined as a possible replacement. In arXiv:2512.01739v2,
Theorem 3.1 concerns two multiplicative functions; its statement was
inspected, not its proof. The carry coefficient in (P6) has no supplied
representation of that kind. The proof in Sections 5.1--5.4, read at
argument depth, uses the dilation law for $\omega$ to cancel early terms.
No corresponding dilation law for consecutive prime gaps is proved here.
These source results are comparisons, not premises of (RFPT).

The paper's Theorem 3.3 does permit arbitrary bounded functions, but
couples them at shifts given by products of primes. Its statement and
proof reduction were inspected; the imported spectral estimates were
not independently verified. The statement on printed p. 25 and the
iterated-logarithm convention on p. 9 were checked against the PDF.
The direct shift comparison of
$a(m)=e((4C_{\pi(m)}+bp_{\pi(m)})/2^{j+1})$ gives only

$$
\sum_{X<m\le2X}|a(m+u)-a(m)|\ll uN_X
\qquad(1\le u\le X).
\tag{P9f}
$$

To see this, charge each difference to the primes crossed between $m$
and $m+u$; a prime is charged at most $u$ times and each jump is at most
$2$. There are $O(N_X)$ relevant primes. At the small ranks, the
periodic weight has only a constant bound, so this comparison leaves
an error of the same order as the desired prime-count budget even for a
unit shift. The larger shifts do not give an $o(N_X)$ error by this
argument. This rejects the direct absolute-value comparison, not a
signed boundary estimate or another application of the decoupling theorem.

### Signed crossings and the precision of a short-shift application

The crossing terms can be retained exactly. Put
$A_r=bp_r+4C_r$ and $a_j(m)=e(A_{\pi(m)}/2^{j+1})$, with
$\pi(p_r)=r$. For a positive integer $u$,

$$
a_j(m+u)-a_j(m)=\sum_{m<p_r\le m+u}\Delta_{r,j},\qquad
\Delta_{r,j}=e\left(\frac{bp_r}{2^{j+1}}\right)
\left[e\left(\frac{C_r}{2^{j-1}}\right)
-e\left(\frac{C_r}{2^j}\right)\right].
\tag{P9g}
$$

Indeed $C_r=2C_{r-1}-bh_{r-1}$ gives
$A_{r-1}=bp_r+2C_r$, and the first equality telescopes. This is valid
for real carries. Under rationality the same integer $C_r$ controls
every rank, so treating the brackets as independent residues loses a
constraint that an arithmetic estimate is permitted to use.

Let $v_j$ be the periodic weight in (P6), with multiplier $b$, extended
by zero off $W$. For any specified arithmetic weight $\kappa_j(m)$ put
$z_j(m)=v_j(m)\kappa_j(m)$ and $I=(X,2X]\cap\mathbb Z$. Exchanging
finite sums gives

$$
\sum_{m\in I}z_j(m)[a_j(m+u)-a_j(m)]
=\sum_{X<p_r\le2X+u}\Delta_{r,j}
\sum_{m\in I\cap[p_r-u,p_r)}z_j(m).
\tag{P9h}
$$

In an application to a part of (P6), $\kappa_j$ must retain that part's
least-factor and cofactor conditions. Dropping them before estimating
the inner sum changes the problem. For example, $v_j$ has period
$q2^{j+1}$ and mean zero. Fixing a class modulo $2q$, its sum over a
period is a geometric sum with primitive ratio $e(-bq/2^j)$, since
$bq$ is odd. Thus unsifted inner sums vanish when $u$ is a multiple of
that period. This is a periodic identity, not cancellation with
$\kappa_j$ present.

There is a useful but insufficient payment for windows crossing more
than one prime. If $k_m=\pi(m+u)-\pi(m)$, the uniform pair upper bound
with constant $8+\eta$ and the singular-series average used in the
[[research/prime_binary_new_attack/residue_switch_moments|residue moment analysis]]
give

$$
\sum_{m\in I} k_m\mathbf1_{k_m\ge2}
\le\sum_{m\in I}k_m(k_m-1)
\ll\frac{u^2X}{(\log X)^2}=o(N_X)
\quad\text{if }u=o(\sqrt{\log X}).
\tag{P9i}
$$

Each ordered pair of primes at separation $h<u$ is counted in at most
$u-h$ windows. Summing its upper bound over $h$ proves (P9i), using
$\sum_{h\le u}\mathfrak S(h)\ll u$. No constant-$4$ pair estimate or
pair asymptotic is used. Since
$\|v_j\|_\infty\le\min(2,4\pi b2^{-j})$, their norms have sum
$O_b(1)$. If $|\kappa_j|\le1$, (P9i) therefore pays for these windows
after summing all ranks. The outside boundaries cost $O_b(u)$. The
single crossings still have only the unsigned bound $O_b(uN_X)$;
(P9i) does not estimate their signed contribution in (P9h).

At precisely these short shifts, Theorem 3.3's stated interval bound
also lacks the required precision. To distinguish its parameters from
the carries and the rank cutoff, call its shift-scale parameter $U$ and its
number of prime bands $J_s$. For fixed sufficiently small
$\varepsilon_1>0$, it requires

$$
J_s\le\varepsilon_1^2\log\log U,\qquad
\Lambda=\frac{\varepsilon_1\log\log U}{2J_s},\qquad
U_0=\exp((\log U)^{1-\varepsilon_1}).
$$

Every prime in the bands exceeds $U_0$, and each shift is a nonempty
product of band primes, at most $U$. Each band's reciprocal-prime mass
is asymptotic to $\Lambda$.
Taking the theorem's upper-bound parameter $V$ comparable to
$\max(2,\Lambda)$, its centered-divisibility estimate saves
$V^{0.49J'}$ against the interval-norm scale, for $J'\le J_s$.
The length requirement is $N\ge\exp((\log U)^{2.01})$. Here $N$
is the number of integers in the interval, of order $X$, not $N_X$.
The source writes $\log_2 U$ for $\log\log U$.

The available saving is at most a fixed power of $\log U$: writing
$t=\log\log U$, the bound
$J_s\log V\ll_{\varepsilon_1}t$ follows on putting $x=J_s/t$.
For a fixed constant $C_{\varepsilon_1}\ge1$ one has
$V\le C_{\varepsilon_1}\max(2,1/x)$, and the function
$x\log(C_{\varepsilon_1}\max(2,1/x))$ is bounded on
$0<x\le\varepsilon_1^2$, with limit zero as $x\to0$.
Even if $U$ is larger than the shifts actually used, requiring those
shifts to be at most $u_0=o(\sqrt{\log X})$ forces $U_0<u_0$.
Consequently
$\log U<(\log u_0)^{1/(1-\varepsilon_1)}$
and $\log\log U=O_{\varepsilon_1}(\log\log\log X)$.
The resulting error scale is therefore only $X$ divided by a fixed
power of $\log\log X$. That stated bound is too large to be
$o(X/\log X)$. Increasing $V$ artificially does not increase the actual
mass being normalized and cannot improve the bound.

This rejects the direct use of the stated interval bound together with
the small-shift payment (P9i). It proves no lower bound for the actual
correlation. A stronger estimate using sparse support, a signed
arithmetic estimate for (P9h), or a comparison retaining multiple
crossings at larger shifts could change the conclusion. None is proved
here. In particular, the exact endpoint identity (P9d) does not forbid
a strict upper bound derived from rationality and additional prime
arithmetic; those two conclusions would be the desired contradiction.

## Implication for the canonical contradiction

Assume $S=a/(2^sd)$ with any fixed odd $d$. Lemma A gives eventual positive
integer carries. For the original reference family, choose a fixed odd
prime $q$ with $2^{q-1}-1>d$. Proposition P4 and PNT force
$Q_{d,q}(X)=(\delta_{d,q}+o(1))N_X$ for all large $X$. A proof of (FPT)
on unbounded scales contradicts this, after those scales pass the preperiod.
Doing so for every odd $d$ proves irrationality. These steps form the
dephased variant of the canonical sketch. Its upper-bound step is
**unknown**, already at $d=1$.
The unconditional bound $Q\le2N_X+o(N_X)$ is insufficient because
$\delta_{d,q}<2$.

Proposition P9 supplies another complete contradiction sketch: assume
$S=a/(2^sd)$, choose $b,q$ by (P9a), obtain the forced value (P9d), and
prove (RFPT) for this actual-prime sum on unbounded scales beyond the
preperiod. The last step is **unknown**, including at $d=1$. Its constants
need not be uniform in $d$. A fixed saving in (P6), with multiplier $b$
and every cofactor and remainder included, would supply precisely that
step. The sign calculation of P8 does not obstruct this choice of
reference. It remains permissible to use the prime-prefix coefficient
from P5 under integer carries, or another consequence of rationality.
The separate unweighted alternative (UPD) is also unknown. These
identities supply no estimate for the shorter-span
bounded event or the positive-mass target in the
[[research/prime_binary_new_attack/rational_deletion_signs|deletion-sign note]],
and neither of those routes is retired by this calculation.

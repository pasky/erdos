---
name: research/prime_binary_new_attack/short_span_sieve
title: A monotone upper event in a shorter prime window
desc: |
  A rational prime binary series forces at least N_X/24 qualifying blocks
  in a shorter span. Their monotone enlargement is rare in the reference
  model and can be posed for actual sieve survivors. The survivor estimate
  is unproved. Its centered-moment cost is equivalent to a prime-rooted
  short-interval estimate. A damped signed form isolates the remaining
  truncated phase cost, whose required bound is also unproved. The band-loss
  alternative has an exact divisor expansion but no arithmetic estimate.
created: 2026-10-17T01:32:13Z
updated: 2026-10-17T01:32:13Z
---

***

This is Plasma AI's author-recorded alternative to step 5 of the
[[research/prime_binary_new_attack/proof_sketch|canonical contradiction
sketch]] for [[problems/irrationality/E0251/_index|Problem 251]]. It proves
the reductions and the reference calculation below, not the required
estimate for primes or sieve survivors. No independent review is claimed.

The change of span has a specific purpose. At span $16K\log X$, the
[[research/prime_binary_new_attack/consecutive_block_counts|nonnegative
majorant analysis, U13--U14]], shows that almost every reference window
contains some compatible $K$-subset. At the shorter span used here, that
existence event has reference probability tending to zero. It is monotone
under adding sites, unlike the event concerning the first $K$ sites. This
permits an upper bound by an actual sifted set. The arithmetic estimate
for that monotone event remains open. Counting all its certificates with
multiplicity still fails, even at the shorter span.

## The smaller forced count

Use $h_n=(p_{n+1}-p_n)/2$, $H_n=G_n/2$, $I_X=\{n:X<p_n\le2X\}$ and
$N_X=|I_X|$ from the sketch. Fix an odd $d$, including $d=1$, and put

$$
K=\lceil12\log_2\log X\rceil,\quad M=2^K,\quad
R=\lfloor4d\log X\rfloor,\quad
D_*=\left\lfloor\frac65K\log X\right\rfloor,\quad
J=\lfloor D_*/2\rfloor.
\tag{S1}
$$

Let $r_d(u)$ be the least positive residue of $-du$ modulo $M$. Thus an
ordinary zero residue means $r_d(u)=M$, and is excluded when $R<M$.
Write $U_{n,K}=\sum_{j<K}2^{K-1-j}h_{n+j}$, and define

$$
B_d^*(X)=\#\{n\in I_X:p_{n+K}-p_n\le D_*,\ r_d(U_{n,K})\le R\}.
$$

**Proposition S1.** If $S=a/(2^sd)$, then
$B_d^*(X)\ge(1/24-o(1))N_X$ as $X\to\infty$.

*Proof.* Past $n\ge\max(s+2,3)$, the sketch's lattice gives positive
integers $c_n=dH_n$ with
$c_{n+K}+dU_{n,K}=Mc_n$. The uniform mean-tail bound (T) excludes at most
$(1/8+o(1))N_X$ starts with $c_{n+K}>R$. At every other start,
$r_d(U_{n,K})=c_{n+K}\le R$, since $R<M$ for large $X$.
PNT telescoping, exactly as in U3, gives

$$
\sum_{n\in I_X}(p_{n+K}-p_n)=(1+o(1))KX.
$$

Consequently at most $(5/6+o(1))N_X$ starts have span above $D_*$.
The union bound leaves $1-1/8-5/6=1/24$. The scales eventually pass
every fixed preperiod $s$. $\square$

More generally, span $\lambda K\log X$ and cutoff
$\tau d\log X$ give the same lower bound with coefficient
$1-1/\lambda-1/(2\tau)$, when it is positive. In particular this
first-moment argument requires $\lambda>1$. Proposition S1 uses only
PNT and the retained lattice identities, not a local prime model.

## An event preserved when sites are added

For a $K$-set $A=\{a_1<\cdots<a_K\}\subseteq\{1,\ldots,J\}$ put
$a_0=0$ and

$$
U(A)=\sum_{i=1}^K2^{K-i}(a_i-a_{i-1}).
$$

Call $A$ compatible when $r_d(U(A))\le R$. These are half-offsets: at
root $x$, its selected sites are $x+2a_i$.
For a finite set $T$ of odd integers and $x\in T$, let

$$
\begin{aligned}
Y_T(x)&=\{a\in\{1,\ldots,J\}:x+2a\in T\},\\
Z_T(x)&=\#\{A\subseteq Y_T(x):|A|=K,\ A\text{ compatible}\},\\
\mathcal C_d(T)&=\sum_{x\in T\cap(X,2X]}\min(1,Z_T(x)).
\end{aligned}
\tag{S2}
$$

Each root is counted once if it has any compatible subset. Both $Z_T(x)$
and $\mathcal C_d(T)$ are nondecreasing when $T$ is enlarged. For
$\mathbb P_X=\mathbb P\cap(X,2X+D_*]$, every root counted by $B_d^*(X)$
has its first $K$ prime successors as such a subset. Therefore

$$
B_d^*(X)\le\mathcal C_d(\mathbb P_X).
\tag{S3}
$$

Consecutiveness is used in the rationality lower bound S1. The upper event
in (S3) allows other prime subsets explicitly; it does not identify them
with consecutive blocks.

For example, take $z=X^{1/2-1/K^2}$ and

$$
T_z=\{m\in(X,2X+D_*]:P^-(m)>z\}.
$$

For large $X$, $T_z$ consists of odd integers and contains $\mathbb P_X$.
Thus $\mathcal C_d(\mathbb P_X)\le\mathcal C_d(T_z)$. The following
actual-arithmetic estimate would finish the contradiction:

$$
\mathcal C_d(T_z)\le\frac1{48}N_X
\quad\text{along arbitrarily large }X,\quad\text{for every fixed odd }d.
\tag{MS}
$$

Together with S1--S3, (MS) contradicts rationality for each $d$ and every
preperiod. It is unproved, even for $d=1$. The choice of sieve level is
part of this proposed estimate. Lowering it adds survivors and can only
increase the upper event.

The unweighted composite count in U10 implies
$|T_z\cap(X,2X]|=N_X+O(N_X/K^2)$. Its bound of $K+1$ per deletion
does **not** apply to (S2): deleting one site can destroy certificates at
every earlier root within $D_*$, not just its first $K$ predecessors.
The fixed-dimensional sieve in
[[research/prime_binary_new_attack/survivor_moments|Corollary M3 of the
survivor-moment note]] instead counts the surviving neighbors of composite
sites. It gives
$\mathcal C_d(T_z)-\mathcal C_d(\mathbb P_X)=O(N_X/K)$, uniformly in
$d$. This does not bound either event; it permits the bounded upper
estimate to be sought directly on the primes, with an $o(N_X)$ error.

## An exact census of compatible subsets

**Lemma S2.** For integers $J\ge2K$, $K\ge1$, odd $d$, and
$1\le R<M=2^K$, let $L_d(J,K,R)$ count compatible $K$-sets in
$\{1,\ldots,J\}$. Then

$$
R\binom{\lfloor J/2\rfloor}{K}
\le L_d(J,K,R)
\le R\binom{\lfloor(J+K)/2\rfloor}{K}.
\tag{S4}
$$

If $K^2/J\to0$, this gives uniformly in odd $d$ and $1\le R<M$

$$
\frac{L_d(J,K,R)}{\binom JK}
=\frac R{2^K}\bigl(1+O(K^2/J)\bigr).
\tag{S5}
$$

*Proof.* A $K$-set is equivalently a positive gap vector
$v_i=a_i-a_{i-1}$ with $\sum_i v_i\le J$. Write uniquely
$v_i=2w_i+1+b_i$, where $w_i\ge0$ and $b_i\in\{0,1\}$. For fixed
$(w_i)$ the sum $U$ is a fixed integer plus
$\sum_i2^{K-i}b_i$, so the $2^K$ bit vectors run once through all its
residues modulo $M$. Exactly $R$ are compatible, since $d$ is odd.

If $\sum_iw_i\le\lfloor(J-2K)/2\rfloor$, every bit vector meets the
span cutoff. Stars and bars therefore gives the lower bound in (S4).
Conversely a vector meeting the cutoff has
$\sum_iw_i\le\lfloor(J-K)/2\rfloor$, giving the upper bound, even if
some of its $R$ compatible bit vectors fail the cutoff. The numbers of
quotient vectors are the two binomial coefficients displayed in (S4).
Comparing their falling-factorial products with $\binom JK$ proves (S5).
$\square$

This is a census of integer subsets, not a theorem about the primes.
It keeps the positive-residue convention: with $K=1$, $J=4$ and $d=R=1$,
only the two odd singleton offsets qualify. Testing the ordinary residue
as at most $R$ would incorrectly count all four.

## Why the monotone event can be small

**Proposition S3 (reference only).** Include each of the $J$ half-offsets
independently with probability $\rho=2/\log X$, obtaining a set $Y$.
With (S1), the probability that $Y$ contains a compatible $K$-subset tends
to zero, for every fixed odd $d$.

*Proof.* Put $V=|Y|$ and $t=\lfloor5K/4\rfloor$. Conditional on $V=v$,
$Y$ is uniform among all $v$-subsets. Hence, by (S5), the expected number
of compatible $K$-subsets in $Y$ is

$$
\binom vK\frac{L_d(J,K,R)}{\binom JK}
=\binom vK\frac R{2^K}(1+o(1)),
$$

with zero when $v<K$. The error is uniform in $v$. A union bound, used
only after restricting $V$, gives

$$
\Pr(Z_Y>0)
\le\Pr(V>t)+(1+o(1))\frac R{2^K}\binom tK.
\tag{S6}
$$

Here $J\rho=(6/5)K+o(1)$. The exponential Markov inequality gives

$$
\Pr(V>t)\le\exp(-(I+o(1))K),\qquad
I=\frac54\log\frac{25}{24}-\frac1{20}>0.
\tag{S7}
$$

For example use $\mathbb E e^{uV}=(1-\rho+\rho e^u)^J
\le\exp(J\rho(e^u-1))$ with $e^u=25/24$. For the other term,
$\binom tK4^K\le5^t\le5^{5K/4}$, so

$$
\frac R{2^K}\binom tK
\le R\left(\frac{5^{5/4}}8\right)^K
\ll_d(\log X)^{15\log_2 5-35}=o(1).
\tag{S8}
$$

The exponent is negative because $5^{15}<2^{35}$. Both bounds apply at
the growing length in (S1). $\square$

The saturation at one per root is essential. At the same parameters the
unrestricted expected number of certificates is, by S2 and Stirling,

$$
\mathbb E Z_Y
=\rho^K L_d(J,K,R)
\sim\frac R{\sqrt{2\pi K}}\left(\frac{3e}5\right)^K
\longrightarrow\infty.
\tag{S9}
$$

Thus replacing $\min(1,Z_Y)$ by $Z_Y$ loses the desired bound already
in this reference, before any prime-tuple sieve loss. Rare windows with
many sites dominate (S9). This concerns that sum of certificates, not
every nonnegative majorant. U13's monotonicity lemma still applies here;
U14's near-one reference conclusion has a different span and does not.
No part of S3 transfers the reference law to $T_z$ or to primes.

## The arithmetic attempt and its two costs

For the actual set $T_z$ write $V_z(x)=|Y_{T_z}(x)|$ and define

$$
\begin{aligned}
\mathcal D_z&=\#\{x\in T_z\cap(X,2X]:V_z(x)>t\},\\
\mathcal Q_{d,z}&=\sum_{\substack{x\in T_z\cap(X,2X]\\V_z(x)\le t}}Z_{T_z}(x).
\end{aligned}
$$

Exactly as a pointwise inequality, without a probabilistic assumption,

$$
\mathcal C_d(T_z)\le\mathcal D_z+\mathcal Q_{d,z}.
\tag{S10}
$$

An upper bound $N_X/96$ for each term, along the same unbounded scales,
would give (MS). Neither is proved. The reference calculations S7 and S8
identify different obligations: unusually many survivors around a
surviving root, and compatible subsets among the remaining roots.
In particular a cluster bound alone would not prove irrationality.

The first concrete arithmetic test is a centered second moment. Put
$\lambda=6/5$, $\chi=\mathbf1_{T_z}$ and

$$
\mathcal V_z=\sum_{X<x\le2X}\chi(x)(V_z(x)-\lambda K)^2.
$$

Since $t< V_z(x)$ implies $V_z(x)-\lambda K>K/20$,
$\mathcal D_z\le400\mathcal V_z/K^2$. In particular
$\mathcal V_z=o(K^2N_X)$ would handle this first cost. Expanding gives

$$
\begin{aligned}
\mathcal V_z={}&
\sum_{\substack{1\le a,b\le J\\a\ne b}}
 \sum_{X<x\le2X}\chi(x)\chi(x+2a)\chi(x+2b)\\
&+(1-2\lambda K)\sum_{1\le a\le J}
 \sum_{X<x\le2X}\chi(x)\chi(x+2a)
+\lambda^2K^2\sum_{X<x\le2X}\chi(x).
\end{aligned}
\tag{VM}
$$

The negative pair term must be retained. Upper estimates for both the
pair and triple counts do not prove the required cancellation. The
required estimate concerns these averaged survivor sums together, at the
displayed level $z$, with an error $o(K^2N_X)$, or a direct bound
$\mathcal D_z\le N_X/96$. It is an unproved arithmetic task, not an
application of PNT in progressions or Bombieri--Vinogradov to their
stated counting functions; Proposition S4 below shows that it implies a
short-interval law of large numbers of unknown status. Success would leave
$\mathcal Q_{d,z}$ to be bounded with its local-count cutoff intact;
removing that cutoff returns to the loss in (S9).

The inspected prime moment theorem does not settle the first test.
[[../library/primes/kuperberg_2023_sums_singular_series_large_sets_tail/_index|Kuperberg,
arXiv:2210.09775v2]], Theorem 1.8 on printed p. 4, bounds uncentered
moments for intervals of length $h=\Lambda\log X$. Corollary 1.9 on
printed pp. 4--5 requires the threshold $k$ to satisfy
$k/\Lambda\to\infty$. Here $\Lambda\sim6K/5$ and $k\sim5K/4$, so their
ratio tends to $25/24$. Moreover (VM) is rooted at a survivor and concerns
survivors, not all integer roots with a prime count. The displayed
moments and the corollary's hypotheses were checked on the page images;
the proof of Theorem 1.8 and its use of the tuple sieve were read in the
transcription, without an independent audit of the sieve. The available
uncentered upper bounds do not provide the negative pair contribution
or the centered error in (VM).

## What the two costs require

This section proves implications of the two costs in (S10), restates the
second cost in a damped signed form, and compares both with the inspected
source estimates. It refutes neither (VM), (MS) nor the phase bound.
The separate survivor-moment note proves that rough composites change
$\mathcal V_z$ by only $O(N_X)$, without estimating the remaining
prime-rooted moment.

### The moment forces a law of large numbers

**Proposition S4.** Keep the parameters (S1) and $\lambda=6/5$. Suppose
$\mathcal V_z=o(K^2N_X)$ along a set of scales $X$. Then along those
scales, for every fixed $\varepsilon>0$,

$$
\#\{x\in T_z\cap(X,2X]:|V_z(x)-\lambda K|>\varepsilon K\}=o(N_X)
\tag{S11}
$$

and

$$
\#\{n\in I_X:\pi(p_n+2J)-\pi(p_n)>(\lambda+\varepsilon)K\}=o(N_X).
\tag{S12}
$$

Consequently, with $L=\lfloor(\lambda+\varepsilon)K\rfloor+1$, all but
$o(N_X)$ starts $n\in I_X$ have $p_{n+L}-p_n>2J$.

*Proof.* Each root counted in (S11) contributes more than
$\varepsilon^2K^2$ to $\mathcal V_z$, so there are at most
$\mathcal V_z/(\varepsilon^2K^2)$ of them. For large $X$ every prime
$p\in(X,2X]$ lies in $T_z$. Every prime in $(p,p+2J]$ is odd, so it is
$p+2a$ with $1\le a\le J$; it is at most $2X+D_*$, because $2J\le D_*$, and
it exceeds $z$. So it lies in $T_z$, and $\pi(p+2J)-\pi(p)\le V_z(p)$.
Hence (S11) gives (S12). Finally, if
$\pi(p_n+2J)-\pi(p_n)\le(\lambda+\varepsilon)K<L$, then
$p_{n+L}>p_n+2J$. $\square$

Here $2J=(6/5+o(1))K\log X$ and $L=(6/5+\varepsilon+o(1))K$. So (VM)
implies that after almost every prime the next $L\asymp\log\log X$ gaps
sum to at least $(\lambda/(\lambda+\varepsilon)-o(1))L\log X$: near almost
every prime there is no cluster of relative density above
$1+\varepsilon/\lambda$ at this scale. This lower law of large numbers for
sums of about $\log\log X$ consecutive gaps is a consequence of the proposed
first input, not of rationality.

In fact Corollary M3 of the
[[research/prime_binary_new_attack/survivor_moments|survivor-moment note]]
gives the stronger exact interface

$$
\mathcal V_z=
\sum_{X<p\le2X}\bigl(\pi(p+2J)-\pi(p)-\lambda K\bigr)^2+O(N_X).
$$

Thus (VM) is equivalent to the prime-rooted estimate (PVM) there, along
the same scales. The sieve proving this comparison has at most three
linear factors; its upper bounds remove the composite contamination,
but do not evaluate the signed pair/triple combination on the primes.

We know no proof of (S12), unconditionally or under the Riemann
hypothesis. For comparison, Selberg's mean-square bound under the Riemann
hypothesis, $\int_X^{2X}|\psi(x+h)-\psi(x)-h|^2\,dx\ll hX(\log X)^2$, read
here in the Saffari--Vaughan form restated in
[Gorodetsky, Section 1.1](https://link.springer.com/article/10.1007/s00209-024-03601-w),
gives by Chebyshev's
inequality that the set of $x\in[X,2X]$ with
$|\psi(x+h)-\psi(x)-h|>\varepsilon h$ has measure
$\ll X(\log X)^2/(\varepsilon^2h)$. This is $o(X)$ only when
$h/(\log X)^2\to\infty$; here $h\asymp\log X\log\log X$, and (S12) roots
each interval at a prime as well. The pair term of (VM) is the survivor
pair correlation averaged over the shifts $2a\le2J$. Matomäki, Radziwiłł
and Tao, *Correlations of the von Mangoldt and higher divisor functions I.
Long shift ranges*, Proc. London Math. Soc. 118 (2019), arXiv:1707.01315v3,
prove the expected asymptotic for $\sum_{X<n\le2X}\Lambda(n)\Lambda(n+h)$
for almost all $|h|\le H$ when $X^{8/33+\varepsilon}\le H\le
X^{1-\varepsilon}$; only the abstract was read here. Shift ranges of size
$O(K\log X)$ lie far outside that theorem.

The survivor indicator $\mathbf 1[P^-(n)>z]$ is multiplicative, and
[[../library/primes/matomaki_2016_multiplicative_functions_short_intervals/theorem_1|Theorem 1
of Matomäki and Radziwiłł]] compares short and long averages of bounded
multiplicative functions in almost all intervals of any growing length. Its
error is absolute, at least $C'\log\log h/\log h$, while the survivors
have density about $1/\log X$. Relative precision would need
$\delta\ll1/\log X$, and then its exceptional-set bound exceeds $X$. It
does not give (S11).

Gorodetsky's *The variance of integers without small prime factors in short
intervals*, Math. Z. 308, 59 (2024),
[Theorem 1.1](https://link.springer.com/article/10.1007/s00209-024-03601-w),
also misses this range. Its unrooted variance theorem requires, among
other hypotheses,

$$
(1+a)\frac{\log H}{\log\log H}
\le(1-\varepsilon)\frac{\log X}{\log y},
\qquad a=\frac{\log\log H}{\log y}.
$$

At $H=2J$ and $y=z$, the left side tends to infinity and the right
side tends to $2(1-\varepsilon)$. Its centering is also the periodic
density $H\prod_{p\le y}(1-1/p)$. The published statement and these
definitions were inspected; the proof was not used.

Tuple upper bounds do not reach (S12) either. Markov's inequality applied to
the rooted factorial moments $\sum_p\binom{\pi(p+2J)-\pi(p)}k$ bounds the
proportion in (S12) by roughly $B(1+\varepsilon/\lambda)^{-k}$ when those
moments are at most $B$ times their Poisson values. The inspected tuple bound
has $B$ of size $(2+\delta)^kk!$ for fixed $\delta>0$, which defeats every
choice of $k$.

### The Buchstab transport rearranges the moment

For a finite odd set $T$ put
$W(T)=\sum_{x\in T\cap(X,2X]}(V_T(x)-\lambda K)^2$, so that
$\mathcal V_z=W(T_z)$. Deleting one site $m$ from $T$ removes the root $m$
and lowers $V_T$ by one at each earlier root whose window contains $m$, so
$W$ changes by

$$
\Omega_T(m)=-\mathbf 1_{X<m\le2X}(V_T(m)-\lambda K)^2
+\sum_{\substack{x\in T\cap(X,2X]\\m=x+2a,\ 1\le a\le J}}
(1+2\lambda K-2V_T(x)).
$$

Let $y=X^{2/5}$, let $T_y$ be the set of $m\in(X,2X+D_*]$ with $P^-(m)>y$,
and for a prime $\ell\in(y,z]$ let $T_{<\ell}$ be the set of those $m$ with
no prime factor below $\ell$. Since $\ell>D_*$, two multiples of $\ell$ are
more than $D_*$ apart, so no window meets two sites deleted at the same
prime and their changes add. Since $\ell^3>3X$, every site of $T_{<\ell}$
divisible by $\ell$ is $\ell r$ with $r\ge\ell$ prime. Deleting the
multiples of each prime $\ell\in(y,z]$ in increasing order therefore gives
the exact identity

$$
W(T_z)=W(T_y)+\sum_{\substack{y<\ell\le z\\\ell\text{ prime}}}
\sum_{\substack{r\ge\ell\text{ prime}\\\ell r\in(X,2X+D_*]}}
\Omega_{T_{<\ell}}(\ell r).
\tag{S13}
$$

The sum of the two terms is needed with error $o(K^2N_X)$. Their orders
alone do not supply that cancellation.

- *The base.* By the prime number theorem applied to the products
  $\ell r$ with $X^{2/5}<\ell\le r$, the set $T_y\cap(X,2X]$ has
  $(1+\log(3/2)+o(1))N_X$ elements. The pair and triple sums in
  $W(T_y)$ are correlations of $X^{2/5}$-rough numbers at shifts up to
  $D_*$. Proposition M4 of the
  [[research/prime_binary_new_attack/survivor_moments|survivor-moment note]]
  proves that $W(T_y)\gg K^2N_X$ by this census and a telescoping span
  bound, and that $W(T_y)\ll K^2N_X$ by a fixed-dimensional upper
  sieve. More precisely its lower coefficient is
  $\lambda^2\log(3/2)^3/3+o(1)>0$. No concentration hypothesis is used
  for these bounds. The leading constant is unestimated, and the signed
  transport would have to cancel a nonzero term of order $K^2N_X$.
- *The transport.* $\Omega_{T_{<\ell}}(\ell r)$ is a polynomial of degree
  two in the indicators of $T_{<\ell}$ within $D_*$ of $\ell r$. The double
  sum is thus a bilinear sum over $\ell\in(X^{2/5},z]$ and $r\ge\ell$,
  weighted by short-shift correlations of the intermediate sifted sets
  around $\ell r$. Applying a Type II estimate would require a bound
  for this specified coefficient class, including its dependence on
  $\ell$. No such bound is supplied by the inspected estimates; the
  short-shift correlations remain unestimated.

So (S13) is an exact rearrangement and supplies no centered estimate. It
has the same unresolved need for a signed correction as the
[[research/prime_binary_new_attack/consecutive_block_counts|upper-count
note]] records for its consecutive count in Proposition U12. The base
moment's order is known; the matching cancellation over the deleted
semiprimes is not.

### Nonnegative polynomial cutoff bounds

For a finite odd set $T$ write
$\mathcal Q_d(T)=\sum_{x\in T\cap(X,2X],\,V_T(x)\le t}Z_T(x)$, so that
$\mathcal Q_{d,z}=\mathcal Q_d(T_z)$.

**Lemma S5.** Let $P(v)=\sum_{k=0}^{k_0}c_k\binom vk$ with every
$c_k\ge0$, and suppose $P(v)\ge1$ for the integers $0\le v\le t$. Then
$P(v)\ge1$ for every integer $v\ge0$, and for every finite odd set $T$

$$
\sum_{x\in T\cap(X,2X]}Z_T(x)P(V_T(x))
\ \ge\ \sum_{x\in T\cap(X,2X]}Z_T(x)\ \ge\ \mathcal Q_d(T).
$$

The left side is a nonnegative combination of the tuple indicators
$\mathbf 1_T(x)\prod_{a\in A\cup B}\mathbf 1_T(x+2a)$, with $A$ a
compatible $K$-set and $|B|\le k_0$.

*Proof.* Each $\binom vk$ is nondecreasing on the integers $v\ge0$, so $P$
is, and $P(v)\ge P(t)\ge1$ for $v>t$. Moreover $Z_T(x)\binom{V_T(x)}k$
counts the pairs $(A,B)$ of subsets of $Y_T(x)$ with $A$ compatible,
$|A|=K$ and $|B|=k$. $\square$

So a bound for $\mathcal Q_{d,z}$ obtained by majorizing the cutoff with
such a polynomial and then bounding each tuple count from above is never
smaller than the untruncated certificate count $\sum_xZ_{T_z}(x)$. Its
reference expectation diverges, by (S9). Such a bound could succeed only if
the actual untruncated count fell below its reference value by a factor
tending to infinity, a deficit that the Hardy–Littlewood heuristics do
not predict. Within this polynomial cutoff approach, an improvement
therefore requires negative coefficients and estimates retaining their
signs. This conclusion does not exclude a direct arithmetic bound for
the truncated event or every other majorant.

### A damped signed form of the second cost

Put $\eta=1/5$. For a finite odd set $T$ let $A_0(T)=|T\cap(X,2X]|$ and

$$
F_d(T)=\sum_{x\in T\cap(X,2X]}\eta^{V_T(x)-K}Z_T(x),
$$

with summands zero when $V_T(x)<K$. Let $C=2^{\lfloor\log_2R\rfloor}$, so
that $C\le R<2C$ and $C$ divides $M$ once $R<M$. Define

$$
P_{d,C}(u)=\frac CM\#\{1\le a\le R:a\equiv-du\pmod C\},\qquad
\kappa_d(u)=\mathbf 1[r_d(u)\le R]-P_{d,C}(u),
$$

and the signed statistic

$$
E_d(T)=\sum_{x\in T\cap(X,2X]}\eta^{V_T(x)-K}
\sum_{\substack{A\subseteq Y_T(x)\\|A|=K}}\kappa_d(U(A)).
\tag{S14}
$$

**Lemma S6.** For every finite odd set $T$, and $X$ so large that $R<M$,

$$
\mathcal Q_d(T)\le2R\Bigl(\frac{5^{5/4}}8\Bigr)^KA_0(T)+5^{t-K}E_d(T).
\tag{S15}
$$

The function $\kappa_d$ has zero Fourier coefficient modulo $M$ at every
frequency $r$ with $(M/C)\mid r$, that is, at every character whose
conductor divides $C$.

*Proof.* On roots with $V_T(x)\le t$ one has
$\eta^{V_T(x)-K}\ge\eta^{t-K}$, so
$\mathcal Q_d(T)\le5^{t-K}F_d(T)$. As $i$ runs over $0\le i<M/C$, the
residues $-d(u+iC)$ modulo $M$ run once through the class of $-du$ modulo
$C$, because $d$ is odd; their least positive representatives are the
$a\in[1,M]$ in that class. Hence $P_{d,C}(u)$ is the average of
$\mathbf 1[r_d(\cdot)\le R]$ over $u+iC$, and $0\le P_{d,C}(u)\le
(R/C+1)C/M\le2R/M$. Averaging over the subgroup $C\mathbb Z/M\mathbb Z$
keeps exactly the frequencies $r$ with $(M/C)\mid r$, which gives the
Fourier statement. Splitting
$\mathbf 1[r_d\le R]=P_{d,C}+\kappa_d$ in $F_d$ gives
$F_d(T)\le(2R/M)\sum_x\eta^{V_T(x)-K}\binom{V_T(x)}K+E_d(T)$. For every
integer $v\ge K$, $\binom vK(4/5)^K(1/5)^{v-K}\le1$, being one value of a
binomial distribution, so the last sum is at most $(5/4)^KA_0(T)$. Finally
$t-K\le K/4$, so $5^{t-K}(2R/M)(5/4)^K\le2R(5^{5/4}/8)^K$. $\square$

At $T=T_z$, $A_0(T_z)=(1+O(1/K^2))N_X$ by the survivor census of Lemma U10,
and $R(5^{5/4}/8)^K\ll_d(\log X)^{15\log_2 5-35}=o(1)$, as in (S8).
Therefore the one-sided bound

$$
E_d(T_z)\le\frac{N_X}{192\cdot5^{t-K}}
\tag{S16}
$$

on the scales of the first cost would give $\mathcal Q_{d,z}\le N_X/96$.
Since $5^{t-K}=(\log X)^{3\log_25+o(1)}$, the budget is about
$N_X(\log X)^{-6.97}$. The trivial bound is
$|E_d(T_z)|\le(5/4)^KA_0(T_z)=(\log X)^{12\log_2(5/4)+o(1)}N_X$, about
$(\log X)^{3.86}N_X$, so (S16) asks for a saving of about $(\log X)^{10.8}$
in a signed sum. Since

$$
\eta^{V_T(x)-K}\prod_{a\in A}\mathbf 1_T(x+2a)
=\prod_{a\in A}\mathbf 1_T(x+2a)
\prod_{b\in[1,J]\setminus A}\bigl(1-\tfrac45\mathbf 1_T(x+2b)\bigr),
$$

$E_d(T_z)$ expands into survivor correlations of every order from $K+1$ to
$J+1$ with alternating signs. Lemma S6 removes the coarse part of the phase
deterministically; it supplies no estimate for the high-conductor residual.
The survivor-moment note's $O(N_X/K)$ bound for affected roots does not
transfer this signed sum at the required precision: its summand can have
size $(5/4)^K$, and the resulting error is larger than the budget in
(S16). The bounded event $\mathcal C_d$, in contrast, does transfer with
an $o(N_X)$ error.

### Where this leaves the route

The proposed moment and damped estimates ask for correlation information
that the inspected theorems do not supply at this scale. The first would
imply (S12), a law of large numbers for sums of about $\log\log X$
consecutive gaps. The selected approach to the second leaves the signed
sum (S16), whose expansion contains correlations of order exceeding $K$.
Uniform prime-tuple hypotheses, such as those assumed by the conditional
claims on the problem page, concern growing patterns; no implication
from the bounds required here to those hypotheses is asserted. The
shorter span supplies no unconditional substitute for the missing
estimates. This account concerns the proposed estimates for the two
costs of (S10); it does not prove that every bound for either cost must
pass through the same correlation expansion.

## Band deletions below the sieve level

A different attempt on (MS) lowers the sieve level and asks each band of
deleted semiprimes to destroy a fixed share of the counted roots. This
section proves the exact deletion identities and states a sufficient
lower bound for the losses. Such a bound also controls the prime-supported
roots. That implication is a necessary consequence of the proposed route,
not a reason an arithmetic proof of the loss bound cannot work.

Write $I=(X,2X+D_*]\cap\mathbb Z$ and let $T\subseteq I$ be a finite set of
odd integers. For $m\in T$ and a root $x\in T\cap(X,2X]$ with $0<m-x\le2J$
and $m-x$ even, call $m$ decisive at $x$ when $Z_T(x)\ge1$ and every
compatible $K$-subset of $Y_T(x)$ contains $(m-x)/2$. Put

$$
L_T(m)=\mathbf 1[X<m\le2X]\min(1,Z_T(m))
+\#\{x:m\text{ is decisive at }x\}.
$$

**Lemma S17.** For every such $T$ and $m\in T$,

$$
\mathcal C_d(T)-\mathcal C_d(T\setminus\{m\})=L_T(m)\ge0.
\tag{S17}
$$

Summing over the sites, $\sum_{m\in T}L_T(m)$ equals $\mathcal C_d(T)$ plus,
for each root with $Z_T(x)\ge1$, the number of half-offsets common to all
its compatible $K$-subsets; hence it is at most $(K+1)\mathcal C_d(T)$. If
$E\subseteq T$ and any two members of $E$ differ by more than $2J$, then
$\mathcal C_d(T)-\mathcal C_d(T\setminus E)=\sum_{m\in E}L_T(m)$.

*Proof.* Deleting $m$ removes its own summand. Another root $x$ can change
only if $(m-x)/2\in Y_T(x)$, that is, $0<m-x\le2J$ with $m-x$ even. Its
compatible subsets after the deletion are exactly those not containing
$(m-x)/2$, so its summand falls from one to zero exactly when $m$ is
decisive at $x$. This proves (S17). In the sum over $m$, each counted root
is counted once for itself and once for each half-offset common to all its
compatible subsets, each of which has $K$ elements. For separated $E$, the
set $\{x\}\cup(x+2Y_T(x))$ of each root lies in an interval of length $2J$
and so meets at most one member of $E$; the summand of $x$ changes exactly
as in the single deletion of that member from $T$. $\square$

The sum over sites is an upper bound on total influence; it gives no lower
bound for any loss. A root whose compatible subsets have no common
half-offset has no decisive site, and a site can become decisive only after
other sites have been deleted.

Now take $K\ge10^4$ and, for $0\le i\le8$,

$$
\alpha_i=\frac{49}{100}+\frac{8i}K,\qquad
T_i=\{m\in I:P^-(m)>X^{\alpha_i}\},\qquad
\mathcal C_i=\mathcal C_d(T_i).
$$

For $0\le i\le7$, put $L_i=\mathcal C_i-\mathcal C_{i+1}$.
Then $1/3<\alpha_i<1/2-1/K^2$. For large $X$ every member of $T_i$ is a
prime or a product of two primes greater than $X^{\alpha_i}$, and
$\mathbb P_X\subseteq T_z\subseteq T_8\subseteq\cdots\subseteq T_0$.
Sieve by the primes $\ell\in(X^{\alpha_i},X^{\alpha_{i+1}}]$ in increasing
order. At the step of $\ell$ the removed sites are the products $\ell r\in I$
with $r\ge\ell$ prime; since $\ell>2J$, they are separated by more than
$2J$. Lemma S17 therefore writes $L_i$ exactly as the sum of
$L_{T_{<\ell}}(\ell r)$ over these products, where $T_{<\ell}$ is the set
just before the step of $\ell$. The product count in the proof of
Proposition U12 of the
[[research/prime_binary_new_attack/consecutive_block_counts|upper-count
note]], with $a=49/100$ and $b=1/2$, gives
$(\log(51/49)+o(1))N_X$ such products in $(X,2X]$ with $\ell\le\sqrt X$;
those with $\ell>\sqrt X$ number $O(X/(\log X)^2)$. Hence
$\mathcal C_0\le|T_0\cap(X,2X]|<2N_X$.

The bands would suffice if each lost half its counted roots up to a small
error. The inequalities

$$
L_i\ge\frac12\mathcal C_i-\frac{N_X}{1024}\qquad(0\le i\le7),
\tag{PB}
$$

on one unbounded set of scales, give
$\mathcal C_8\le2^{-8}\mathcal C_0+(N_X/1024)\sum_{j<8}2^{-j}<5N_X/512$.
Since $\mathcal C_d(T_z)\le\mathcal C_8$ and $5/512<1/48$, this is (MS).
The following proposition identifies the roots that no band can remove.

**Proposition S18.** For $0\le i\le7$,

$$
L_i\le\mathcal C_i-\mathcal C_d(\mathbb P_X).
\tag{S18}
$$

Consequently (PB) implies $\mathcal C_d(\mathbb P_X)<5N_X/512$ on its
scales. If $S=a/(2^sd)$, then for all large $X$ at least one inequality of
(PB) fails.

*Proof.* Monotonicity and $\mathbb P_X\subseteq T_{i+1}$ give
$\mathcal C_{i+1}\ge\mathcal C_d(\mathbb P_X)$, which is (S18). The bound
$\mathcal C_8<5N_X/512$ obtained from (PB) is at least
$\mathcal C_d(\mathbb P_X)$. Under rationality, (S3) and S1 give
$\mathcal C_d(\mathbb P_X)\ge B_d^*(X)\ge(1/24-o(1))N_X$, which exceeds
$5N_X/512$ for large $X$. $\square$

Deleting composites never removes a compatible subset of primes. Only
composite roots, or prime roots whose compatible subsets all contain a
composite, can be lost. Thus (S18) converts the proposed loss bounds into
upper bounds for prime roots certified by primes alone. The bound supplied
by (PB), together with (S3) and S1, contradicts rationality. The band
identities alone rearrange $\mathcal C_0-\mathcal C_8$ and supply no estimate. This
persistent prime contribution exists for every order or range of
deletions ending at a set containing $\mathbb P_X$, since the total
loss is at most $\mathcal C_d(T)-\mathcal C_d(\mathbb P_X)$. It does not
refute (PB): the conclusion that (PB) must fail under rationality is
precisely what makes an unconditional proof of (PB) sufficient. The
remaining question is an arithmetic lower bound for the actual losses.

## An arithmetic expansion of the band loss

The following calculation attempts that lower bound by exposing the
prime cofactor of each deleted semiprime. It gives an exact sum to
estimate, but the available progression theorem does not estimate its
full coefficient. The failure is in the proposed application of the
theorem, not a disproof of (PB).

Fix the parameters of (S1), and put
$\mathcal B=\{-J,\ldots,-1,1,\ldots,J\}$. For
$v\in\{0,1\}^{\mathcal B}$, translate the deleted site to zero and set
$T(v)=\{0\}\cup\{2b:b\in\mathcal B,\ v_b=1\}$. The even coordinates here
are translations of odd sites. Write $F_T(x)=\min(1,Z_T(x))$ using the
same half-offset convention as (S2), and define the local loss

$$
\mathcal L(v)=F_{T(v)}(0)+
\sum_{a=1}^J v_{-a}
\bigl(F_{T(v)}(-2a)-F_{T(v)\setminus\{0\}}(-2a)\bigr).
$$

Thus $0\le\mathcal L(v)\le J+1$. It vanishes if fewer than $K$ of the
neighbor sites are present: every counted loss needs a root and $K$
successors, one of these $K+1$ distinct sites being the deleted site.
The unique multilinear expansion on the Boolean cube is consequently

$$
\begin{aligned}
\mathcal L(v)&=\sum_{\substack{B\subseteq\mathcal B\\|B|\ge K}}
 a_B\prod_{b\in B}v_b,\\
a_B&=\sum_{E\subseteq B}(-1)^{|B|-|E|}\mathcal L(\mathbf1_E).
\end{aligned}
\tag{S19}
$$

The second identity is finite inclusion--exclusion; it also proves the
first by evaluating at every $\mathbf1_E$. In particular
$|a_B|\le(J+1)2^{|B|}$ and
$\sum_B|a_B|\le(J+1)3^{2J}$. These are crude bounds, not lower bounds for
the loss from any cancellation. Nonnegativity of $\mathcal L$ does not
make its coefficients nonnegative. For example, at $K=1$, $J=3$ and
$d=R=1$, only offsets $1$ and $3$ qualify, and direct evaluation gives

$$
\mathcal L(v)=v_1+v_3-v_1v_3+
v_{-1}(1-v_2)+v_{-3}(1-v_{-2}).
$$

Let $\chi_{<\ell}(n)=\mathbf1[P^-(n)\ge\ell]$. In a band of (PB), the
set immediately before sieving by $\ell$ has this indicator on $I$.
For $m\in(X+2J,2X]$, the coefficient of its deletion in S17 is therefore
$\mathcal L((\chi_{<\ell}(m+2b))_{b\in\mathcal B})$. All earlier roots
and all their forward sites lie in the permitted interval. Sites within
$2J$ of the left boundary, and deleted sites in the upper buffer
$(2X,2X+D_*]$, contribute a total error $O(J^2)$: there are $O(J)$ such
integer sites, each with loss at most $J+1$. This error is bounded before
expanding (S19), so it is not multiplied by $\sum|a_B|$.

It follows that the exact arithmetic sum for a band is

$$
\begin{aligned}
L_i={}&
\sum_{\substack{B\subseteq\mathcal B\\|B|\ge K}}a_B
\sum_{\substack{X^{\alpha_i}<\ell\le X^{\alpha_{i+1}}\\\ell\ {\rm prime}}}
\ \sum_{\substack{X/\ell<r\le2X/\ell\\r\ {\rm prime}}}
\prod_{b\in B}\chi_{<\ell}(\ell r+2b)
+O(J^2).
\end{aligned}
\tag{S20}
$$

Here $r>\ell$, since $\alpha_{i+1}<1/2$; thus $\ell$ is indeed the least
prime factor of each removed site. The separated-deletion part of S17
justifies summing the coefficients computed before removing all multiples
of a fixed $\ell$. Formula (S20) keeps the original rooted count. Its
error is $o(N_X)$, and every nonzero monomial involves at least $K$
neighboring survival conditions. Fixed-dimensional estimates such as
M1 do not evaluate this growing sum.

To try a progression estimate in the variable $r$, expand each factor
exactly as

$$
\chi_{<\ell}(n)=
\sum_{\substack{q\mid n\\q\mid\prod_{p<\ell}p}}\mu(q).
$$

Each argument is at most $3X$ for large $X$, so one may restrict every
$q_b$ to at most $3X$ without changing this exact sum. For a chosen
divisor $q_b$ at each site, let
$Q=\mathop{\rm lcm}_{b\in B}q_b$. The resulting congruences are
$\ell r\equiv-2b\pmod {q_b}$. They are consistent exactly when
$\gcd(q_b,q_c)\mid2(b-c)$ for every pair $b,c$. When consistent they
specify a single class $r\equiv a\pmod Q$, because $\ell$ is coprime to
$Q$. A nonprimitive class contributes no prime $r$: every prime divisor
of $Q$ is below $\ell$, whereas $r>\ell$. Each remaining term is a prime
count in a primitive progression over $(Y,2Y]$, where $Y=X/\ell$.

This last statement is an exact reduction, not a license to replace all
those counts by their main terms. The Bombieri--Vinogradov theorem as
stated in the
[[../library/integer_sequences/polymath_2014_variants_selberg_sieve_bounded_intervals_containing/_index|Polymath source]],
arXiv v4, Section 2, Claim 2.2 and Theorem 2.3, supplies averaged errors
for moduli at most $Y^\theta$ for each fixed $\theta<1/2$. At the
cofactor scale here this is at most $X^{51\theta/100}$, strictly below
$X^{51/200}$. The exact divisor expansion includes larger moduli; even a
single divisor $q_b<\ell$ need not be in that range. There is no proved
truncation or cancellation of the out-of-range terms. Nor does the
pointwise bound $\mathcal L\le J+1$ control the sum of the absolute
divisor coefficients required for a termwise error estimate.

One may instead try to apply a convolution theorem at the product scale
$X$. Claim 2.6 and Theorem 2.8 of the same source give the corresponding
generalized Bombieri--Vinogradov statement for exponents below $1/2$,
with divisor-bounded factor coefficients and a stated
Siegel--Walfisz condition on one factor. A fixed divisor choice in
(S20) can be reorganized into a semiprime progression sum, with a
least-factor cutoff depending on its divisors. To use that theorem one
still has to handle these cutoffs, sum the signed coefficients, and
control the moduli beyond its range. Neither statement is an estimate
for an arbitrary bounded function of the neighboring sifted sites.
The cited statements and hypotheses are inspected; their external proofs
are not independently audited here.

There is an actual arithmetic test for the simplest proposed disposal of
the omitted divisors. At the level $z$ of (MS), U10 and Mertens' product
formula give, respectively,

$$
\begin{aligned}
|T_z\cap(X,2X]|&=(1+o(1))N_X,\\
X\prod_{p\le z}(1-1/p)&=(2e^{-\gamma}+o(1))N_X.
\end{aligned}
\tag{S21}
$$

Here $\gamma$ is Euler's constant and $2e^{-\gamma}>1$. The first
identity counts the actual primes and the $O(N_X/K^2)$ rough composites.
The second uses $\log z=(1/2-1/K^2)\log X$ and $N_X\sim X/\log X$.
Thus replacing the exact one-site divisor sum by its periodic density
has error $(1-2e^{-\gamma}+o(1))N_X$, already of order $N_X$.
An $o(N_X)$ remainder for that replacement is false. This calculation
does not determine the sign or size of the corresponding *weighted*
remainder in (S20), and it does not refute (PB). It shows why the
large-divisor contribution needs an arithmetic treatment even before
addressing the phase condition.

The missing input for this attack is a lower estimate of (S20) by
$\mathcal C_i/2-N_X/1024$, simultaneously for the eight bands on
unbounded scales for each fixed odd $d$. A usable progression or
switching argument must prove both the summed error control, including
the out-of-range divisors, and the comparison of its retained main term
with $\mathcal C_i/2$. Neither is supplied by (S19)--(S21). Obtaining
such an estimate would finish the whole contradiction by (PB), S1 and
S3; no independent-gap distribution would then be needed.

## A bounded target and its aggregate error

The numerical target in (MS) is stronger than the contradiction needs.
Keeping every parameter of (S1), it suffices, for each fixed odd $d$, to
prove on an unbounded set of scales

$$
\mathcal C_d(\mathbb P_X)
\le\left(\frac1{24}-\varepsilon_d\right)N_X,
\qquad \varepsilon_d>0.
\tag{BC}
$$

The scales and the saving may depend on $d$. The estimate may also be
proved under the rationality assumption: a contradiction does not require
an unconditional upper theorem. That assumption must supply a valid
additional argument, rather than the desired upper estimate itself.

**Proposition S22.** Condition (BC) contradicts $S=a/(2^sd)$ for every
fixed $s$. The concrete upper bound $\mathcal C_d(\mathbb P_X)\le N_X/32$
suffices. With the eight bands of (PB), put

$$
e_i=\mathcal C_{i+1}-\frac12\mathcal C_i,
\qquad
E=\sum_{i=0}^7 2^{-(7-i)}e_i.
$$

The single bound $E\le N_X/64$ on unbounded scales also suffices. Under
rationality, in contrast, these same quantities satisfy
$E\ge(13/384-o(1))N_X$.

*Proof.* S1 and S3 force
$\mathcal C_d(\mathbb P_X)\ge(1/24-o(1))N_X$ past every fixed preperiod.
This contradicts (BC), and $1/24-1/32=1/96>0$. Iterating the definition
of $e_i$ gives the exact identity

$$
\mathcal C_8=2^{-8}\mathcal C_0+E.
\tag{S22}
$$

Since $\mathcal C_0<2N_X$ and
$\mathcal C_d(\mathbb P_X)\le\mathcal C_8$, the proposed bound on $E$
gives

$$
\mathcal C_d(\mathbb P_X)
\le\mathcal C_8
<\left(\frac1{128}+\frac1{64}\right)N_X
=\frac3{128}N_X<\frac1{32}N_X.
$$

Conversely, under rationality the forced lower count and (S22) give
$E\ge(1/24-1/128-o(1))N_X=(13/384-o(1))N_X$.
$\square$

Corollary M3 transfers a fixed saving below $1/24$ between the actual
primes and $T_z$, with an $o(N_X)$ change and, if necessary, a smaller
positive saving. Neither the prime bound $N_X/32$ nor the aggregate
bound above is asserted to imply the specific bound $N_X/48$ in (MS).
They contradict S1 directly. No centered moment or unbounded certificate
count is needed if (BC) itself can be estimated.

The individual inequalities (PB) imply $e_i\le N_X/1024$ and hence
$E<N_X/512$, a stronger sufficient bound. The aggregate target permits
errors in different bands to compensate. It does not yet supply a new
arithmetic estimate: $E$ is identically
$\mathcal C_8-2^{-8}\mathcal C_0$. In particular, the rationality lower
bound on $E$ is part of the proposed contradiction, not a refutation of
an unconditional upper bound for it.

The attempted use of fixed-dimensional sieve bounds on (S20) stops at
this aggregate too. Every monomial there has at least $K$ neighboring
survival factors, without a coefficient-positivity guarantee. Upper bounds for
separate correlations provide neither the required signed remainder nor
its comparison with the bounded count. The pointwise size of the local
loss does not give the small absolute coefficient sum required by a
termwise progression estimate. S21
also prevents discarding the full arithmetic correction to periodic
density as $o(N_X)$, already for one site. That test does not determine
the weighted correction. To finish this route one must estimate (BC),
or prove the stated bound for $E$ with its actual coefficients and all
out-of-range divisor contributions included. Both estimates remain
unknown, even for $d=1$.

## Failure account

- The shorter-span rationality lower bound and the monotone upper
  enlargement are proved. (MS) for actual survivors is unknown for every
  odd $d$. It is a stronger sufficient upper target, not an equivalence
  to the original consecutive-block upper bound. Proposition S22 instead
  needs only a fixed saving below $1/24$ for the bounded prime event,
  for example $N_X/32$, or the aggregate band bound $E\le N_X/64$.
  These weaker sufficient estimates are also unproved.
- S3 proves rarity only in the stated independent-site reference. Its
  parameter choice avoids U14's large-span saturation, but gives no
  arithmetic comparison. The underlying sieve level is near $\sqrt X$,
  not the small periodic exclusion of U9.
- Bounding the monotone event by the untruncated sum of compatible
  tuple indicators fails to be small in the reference, by (S9). Lemma
  S5 extends this to every cutoff majorant that is a nonnegative
  combination of binomial coefficients in the local count, followed by
  tuple upper bounds: such a bound is at least the untruncated count.
  No assertion is made about signed or other arithmetic majorants.
- The centered moment (VM) is unknown and does not depend on $d$.
  Corollary M3 of the survivor-moment note identifies it, up to $O(N_X)$,
  with the prime-rooted moment (PVM). Proposition S4 proves that it implies
  (S12), a law of
  large numbers for sums of about $(6/5)K$ consecutive gaps after almost
  every prime. No proof of (S12) is known to this note, even under the
  Riemann hypothesis, whose mean-square bound needs intervals longer than
  $(\log X)^2$. Its pair term is an average over shifts of size
  $O(K\log X)$, far below the shift ranges of the known averaged
  pair-correlation theorem. Tuple upper bounds cannot give it: their loss
  $(2+\delta)^kk!$ defeats the factorial-moment route, and the inspected
  uncentered moment theorem has the wrong threshold range and root
  convention. These inspected bounds do not establish (VM), which
  remains a short-interval distribution statement of unknown status.
- The signed Buchstab transport (S13) is exact. Its base $W(T_y)$ is
  bounded above and below by positive constants times $K^2N_X$ in
  Proposition M4; no leading constant is computed. Its correction is a
  bilinear sum over semiprimes weighted by short-shift correlations, and
  no cancellation to $o(K^2N_X)$ is proved. Reopens with an estimate
  for that signed combination, or directly for (PVM); another bound for
  the number of deleted semiprimes is not enough.
- The truncated phase cost $\mathcal Q_{d,z}$ is unknown for every odd
  $d$. Lemma S6 reduces it to the one-sided bound (S16) for the damped
  high-conductor statistic $E_d(T_z)$, with budget about
  $N_X(\log X)^{-6.97}$ against a trivial size about
  $(\log X)^{3.86}N_X$. That statistic expands into survivor
  correlations of every order from $K+1$ to $J+1$ with alternating
  signs. No required estimate is proved here or supplied by the inspected
  sources. Reopens with a
  cancellation argument for (S16) that does not pass through asymptotics
  for each correlation, or with a direct estimate for the bounded event
  $\min(1,Z_{T_z})$.
- The
  [[research/prime_binary_new_attack/rational_deletion_signs|conditional
  deletion-sign bound]] concerns the consecutive-block count at an
  enlarged span. Its negligible negative mass under rationality
  estimates neither arithmetic cost in (S10); it supplies no transfer
  from the independent reference to the actual survivors here.
- Lowering the sieve level to $X^{49/100}$ and asking each of eight bands
  of deleted semiprimes to destroy half of the counted roots, (PB), would
  finish the contradiction; Lemma S17 gives each band loss exactly.
  The band composition and Proposition S18 prove that (PB) implies (MS)
  and the prime bound $\mathcal C_d(\mathbb P_X)<5N_X/512$, because
  deleting composites never removes a prime root certified by primes alone.
  This necessary consequence does not refute (PB) or prohibit an
  arithmetic proof of it. The exact expansion (S20) attempts such a
  proof through the prime cofactors of removed semiprimes. The
  termwise progression argument fails to control its signed
  coefficients, the moduli outside the available range, and the
  comparison of the remaining contribution with $\mathcal C_i/2$.
  Those weighted estimates are unknown even for $d=1$. The simpler
  replacement of the one-site count by periodic density with an
  $o(N_X)$ remainder is false by (S21). Reopens with an estimate of the
  full weighted arithmetic sum, including that correction, or with
  a direct upper bound for the bounded prime event.

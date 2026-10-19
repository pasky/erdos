---
name: research/leads/totient_binary_series/dilation_cube
title: Prime Dilation and Alternating Cubes for the Binary Totient Series
desc: |
  Exact totient dilation cubes, their common-divisor normalization and
  complete averaged error bound, with a missing phase estimate, a bounded
  coincidence obstruction, and a positive-tail obstruction for cofactors k.
tags: []
sources: []
problems:
- 249
review_status: unreviewed
created: 2026-10-15T00:18:22Z
updated: 2026-10-15T00:18:22Z
---

# Prime Dilation and Alternating Cubes for the Binary Totient Series

[[research/leads/totient_binary_series/_index|..]]

***

This page uses the notation of
[[research/leads/totient_binary_series/_index|the binary totient sketch]]:
$S=\sum_{n\ge1}\varphi(n)2^{-n}$ and
$T_N=\sum_{h\ge1}\varphi(N+h)2^{-h}$, so $T_N=2^NS-\Phi_N$ with
$\Phi_N\in\mathbb Z$. If $S=a/q$ with integers $a,q\ge1$, then
$qT_N\in\mathbb Z$ for every $N\ge0$. The arguments below are Plasma AI's,
author-recorded, and have not received independent review.

The mechanism tested here is the reduction by which Tao and Teräväinen
prove that $\sum_n\omega(n)2^{-n}$ is irrational,
[[../library/arithmetic_functions/tao_2025_quantitative_correlations_problems_prime_factors_consecutive/_index|Section 5
of their correlation paper]] (arXiv:2512.01739v2), the result recorded for
[[problems/irrationality/E0069/_index|Problem 69]]. Their argument has three
moves: a prime dilation of the shift tail, using
$\omega(pm)=\omega(m)+1-1_{p\mid m}$ (their (5.1)--(5.3)); an alternating
sum over a cube of primes that cancels the first $K$ shifts identically
(their (5.4)--(5.8)); and a variance argument that writes the remaining
phase as a sum of small, nearly independent prime contributions (their
(5.12)--(5.21), with their Theorem 3.1 for the very large primes). Only the
shift bookkeeping of the second move is reused below, and it is
elementary; no theorem of the source is consumed. The totient analogues of
the first two moves are exact. A common-divisor normalization improves
their coefficients, but the third move still needs an unproved phase
estimate. The results below delimit specific attempted constructions;
they do not exclude other decompositions or resolve Problem 249. Here
$\log_2$ means logarithm to base two and $\ln$ means natural logarithm;
the source instead uses $\log_j$ for iterated natural logarithms.

## The dilation identity

**Lemma 1.** For a prime $p$ and an integer $N\ge0$,

$$
\sum_{h\ge1}\frac{\varphi(pN+ph)}{2^h}=(p-1)\,T_N+\delta_p(N),
\qquad
\delta_p(N)=\sum_{h\ge1,\ p\mid N+h}\frac{\varphi(N+h)}{2^h}.
$$

If $S=a/q$, then $q\sum_{h\ge1}\varphi(pN+ph)2^{-h}\equiv q\,\delta_p(N)
\pmod 1$.

*Proof.* For every $m\ge1$, $\varphi(pm)=(p-1)\varphi(m)$ when $p\nmid m$
and $\varphi(pm)=p\varphi(m)$ when $p\mid m$; that is,
$\varphi(pm)=(p-1)\varphi(m)+\varphi(m)1_{p\mid m}$. Apply this to
$m=N+h$ and sum with weights $2^{-h}$; both series converge absolutely.
The congruence follows from $q(p-1)T_N\in\mathbb Z$. $\square$

The error is weighted by a totient value, unlike the source's indicator
error. Two bounds make the difference quantitative. First, for $m\ge1$,

$$
\frac{\varphi(m)}{m}=\prod_{\ell\mid m}\Bigl(1-\frac1\ell\Bigr)
\ge\prod_{i=1}^{\omega(m)}\Bigl(1-\frac1{i+1}\Bigr)
=\frac1{\omega(m)+1}\ge\frac1{1+\log_2m},
$$

since the $i$-th prime divisor of $m$ is at least $i+1$ and
$2^{\omega(m)}\le m$. Second, the least $h_0\ge1$ with $p\mid N+h_0$
satisfies $h_0\le p$, so

$$
\delta_p(N)\ \ge\ \frac{\varphi(N+h_0)}{2^{h_0}}
\ \ge\ \frac{N+1}{2^{p}\,(1+\log_2(N+p))}.
$$

Hence $q\,\delta_p(N)<1/4$ forces $2^{p}>4q(N+1)/(1+\log_2(N+p))$; for
$p\le N$ this means $p\ge\log_2N-\log_2\log_2N+\log_2q+O(1)$. When
$p\mid N$ (the case $p^2\mid pN$), the terms are $h=kp$ and
$\delta_p(N)=\sum_{k\ge1}\varphi(N+kp)2^{-kp}\le2(N+2p)2^{-p}$, so this
threshold has the right order. For $\omega$ the source's error $\delta_p$
in (5.3) is at most $2^{1-p}$ in the corresponding case. When $p\nmid N$
the error contains the term $h_0$, which can be as large as
$\varphi(N+1)/2$; the source's averaged treatment of that event is
discussed under the parameter ranges below.

## The alternating cube

**Proposition 2.** Let $K\ge1$ and let $p_0,v_1,\ldots,v_K$ be integers
such that $p_\epsilon=p_0+\sum_k\epsilon_kv_k$ are distinct primes for all
$\epsilon\in\{0,1\}^K$. Put $s_\epsilon=\sum_{k=1}^Kk\epsilon_kv_k$ and
$r_{\epsilon,h}=p_\epsilon h-s_\epsilon$. Let $n>\sum_kk|v_k|$ satisfy
$n\equiv s_\epsilon\pmod{p_\epsilon}$ for every $\epsilon$, and put
$N_\epsilon=(n-s_\epsilon)/p_\epsilon$ and

$$
\Delta_h(n)=\sum_{\epsilon\in\{0,1\}^K}(-1)^{|\epsilon|}
 \varphi(n+r_{\epsilon,h}).
$$

Then $\Delta_h(n)=0$ for $1\le h\le K$, and

$$
\sum_{h>K}\frac{\Delta_h(n)}{2^h}
=\sum_{\epsilon}(-1)^{|\epsilon|}
 \bigl((p_\epsilon-1)T_{N_\epsilon}+\delta_{p_\epsilon}(N_\epsilon)\bigr).
$$

If $S=a/q$, then
$q\sum_{h>K}\Delta_h(n)2^{-h}\equiv
q\sum_\epsilon(-1)^{|\epsilon|}\delta_{p_\epsilon}(N_\epsilon)\pmod1$.

*Proof.* Since $n+r_{\epsilon,h}=p_\epsilon(N_\epsilon+h)$, Lemma 1 at
$(p_\epsilon,N_\epsilon)$, multiplied by $(-1)^{|\epsilon|}$ and summed,
gives the displayed identity once the terms $h\le K$ are removed. For
$h\le K$, $r_{\epsilon,h}=p_0h+\sum_k(h-k)\epsilon_kv_k$ does not involve
$\epsilon_h$; pairing $\epsilon$ with the vector that differs from it only
in coordinate $h$ gives equal arguments and opposite signs, so
$\Delta_h(n)=0$. The congruence follows from
$q(p_\epsilon-1)T_{N_\epsilon}\in\mathbb Z$. $\square$

The cancellation for $h\le K$ holds for every function in place of
$\varphi$; only the right-hand side uses multiplicativity. The
congruences are the source's single-power conditions (5.5). Requiring
$p_\epsilon^2\mid n-s_\epsilon$ instead means $p_\epsilon\mid N_\epsilon$,
the case of the pointwise upper bound after Lemma 1.

The identity is exact, and its phase is also a function of the target.
Since $T_N\equiv\{2^NS\}\pmod1$, the left side is congruent modulo one
to $\sum_\epsilon(-1)^{|\epsilon|}\bigl((p_\epsilon-1)\{2^{N_\epsilon}S\}
+\delta_{p_\epsilon}(N_\epsilon)\bigr)$, unconditionally. An estimate for
its phase is therefore equally a statement about the binary digits of $S$
at the $2^K$ positions $N_\epsilon\approx n/p_\epsilon$. This is the cube
counterpart of the one-window reformulation in the sketch.

## A common-divisor normalization

Let $G$ be any positive common divisor of the $p_\epsilon-1$. Dividing
Proposition 2 by $G$ is compatible with rationality, since every
$(p_\epsilon-1)/G$ is an integer. Thus $S=a/q$ implies

$$
\frac qG\sum_{h>K}\frac{\Delta_h(n)}{2^h}
\equiv\frac qG\sum_\epsilon(-1)^{|\epsilon|}
\delta_{p_\epsilon}(N_\epsilon)\pmod1.
\tag{1}
$$

Also $\varphi(p_\epsilon m)/G$ is an integer for every $m\ge1$.
Indeed, writing $m=p_\epsilon^a u$ with $p_\epsilon\nmid u$ gives
$\varphi(p_\epsilon m)=p_\epsilon^a(p_\epsilon-1)\varphi(u)$.

**Proposition 2a (weights for the prescribed cube pairings).** Suppose
nonzero rational weights $c_\epsilon$ are required to cancel separately at each
of the paired equal arguments used in Proposition 2, for every
$1\le h\le K$. Then $c_\epsilon=C(-1)^{|\epsilon|}$ for one rational
$C$. The corresponding coefficients $c_\epsilon(p_\epsilon-1)$ on
$T_{N_\epsilon}$ are integers exactly when

$$
C\gcd_\epsilon(p_\epsilon-1)\in\mathbb Z.
$$

*Proof.* Each prescribed pairing requires
$c_\epsilon+c_{\epsilon\mathbin\triangle\{h\}}=0$. Connecting vertices
by coordinate flips gives the asserted weights. If all
$C(p_\epsilon-1)$ are integers, a Bezout combination of the
$p_\epsilon-1$ shows that their gcd times $C$ is integral. The converse
follows because that gcd divides each $p_\epsilon-1$. $\square$

Consequently $G=\gcd_\epsilon(p_\epsilon-1)$ gives the largest common
normalization within this class of integer tail coefficients. For example,
$p_0=13$, $(v_1,v_2)=(6,18)$ gives the prime vertices $13,19,31,37$
and $G=6$. The normalized tail weights, in that order, are
$2,-3,-5,6$. This saves a factor six. It does not rule out
other pairings, cancellations between different levels, or using extra
divisibility of the tail integers. For instance $qT_N$ is always even
for $N\ge3$ under rationality, giving a further fixed factor two.

## An averaged estimate and its parameter cost

Put $M=2^K$ and $R=\sum_k k|v_k|$. Suppose $p_\epsilon\in[P/2,P]$,
$x/2>R$, and $Q$ is divisible by every $p_\epsilon$ but by none of their
squares. Let $\mathcal A$ be the nonempty set of integers in $[x/2,x]$
in a single class modulo $Q$ satisfying Proposition 2, and put
$A=|\mathcal A|$ and $Y=2(x+R)/P$. Expectations below are uniform on
$\mathcal A$, and $e(t)=\exp(2\pi i t)$.

**Proposition 2b (complete error bound).** For integers $L\ge1$ and
$H\ge K$, define

$$
\Psi_{G,H}(n)=\frac qG\sum_{K<h\le H}\frac{\Delta_h(n)}{2^h}.
$$

If $S=a/q$, then

$$
\begin{aligned}
\bigl|\mathbf E e(\Psi_{G,H}(\mathbf n))-1\bigr|
\le{}&2ML\left(\frac2P+\frac1A\right)\\
&+\frac{2\pi qM}{G}
\left((Y+L+2)2^{-L}
 +(x+R+P(H+2))2^{-H}\right).
\end{aligned}
\tag{2}
$$

*Proof.* Write the members of $\mathcal A$ as $n_0+tQ$ for $A$
consecutive integers $t$. Then
$N_\epsilon=(n_0-s_\epsilon)/p_\epsilon+tQ/p_\epsilon$ runs through
all residues modulo $p_\epsilon$ in a cycle, since
$p_\epsilon^2\nmid Q$. For each $h$, the event
$p_\epsilon\mid N_\epsilon+h$ has probability at most
$1/p_\epsilon+1/A$. The union of these events for all vertices and
$1\le h\le L$ has probability at most $ML(2/P+1/A)$.

Off this exceptional event, the complete positive error satisfies

$$
\delta_{p_\epsilon}(N_\epsilon)
\le\sum_{h>L}(N_\epsilon+h)2^{-h}
=(N_\epsilon+L+2)2^{-L}\le(Y+L+2)2^{-L}.
$$

The complete signed tail beyond $H$, divided by $G$ and multiplied by
$q$, is bounded absolutely by

$$
\frac{qM}{G}\sum_{h>H}(x+R+Ph)2^{-h}
=\frac{qM}{G}(x+R+P(H+2))2^{-H}.
\tag{3}
$$

Use (1), $|e(t)-1|\le2\pi|t|$ off the exceptional event, and the
bound two for the difference of two unit complex numbers on that event.
This gives (2). No infinite tail has been dropped. $\square$

One sufficient asymptotic regime, with $q$ and $0<\eta<1$ fixed, is

$$
Q\le x^{1-\eta},\qquad
\frac{P}{M\ln x}\longrightarrow\infty,
\tag{4}
$$

with integer $C\to\infty$, $C=o(\ln x)$, and

$$
L=\left\lceil\log_2\frac{qMx}{PG}\right\rceil+C,
\qquad
H=\left\lceil\log_2\frac{qMx}{G}\right\rceil+C.
\tag{5}
$$

Here $Q\ge(P/2)^M$, $M\ge2$, and $G<P$. Thus
$P\le2x^{(1-\eta)/M}$ and $x/(PG)\ge x^\eta/4$; both cutoffs
are positive and of order $\ln x$. The range of the cube's vertices is
$\sum_k|v_k|\le P/2$, so $R\le KP/2$. Also
$A\ge x/(2Q)-1$, $M=O(\ln x)$, and $P\ln x=o(x)$. Substitution
into (2) makes its right side $o(1)$. Cubes satisfying these hypotheses
are required inputs; no existence claim for arbitrary growing $K$ is
implicit in this estimate.

The regime is nonempty already with $K=1$. Take two distinct odd primes
in $[P/2,P]$, put $Q=p_0p_1$, and set $x=P^D$ for a fixed
$D>2/(1-\eta)$. Such pairs exist for all sufficiently large $P$ by the
prime number theorem. The two congruences determine a class modulo $Q$,
and (4) holds. This supplies an unbounded family for the error estimate,
but no saving for its exponential average.

The normalization does not turn this absolute-bound method into a short
window argument. Specifically,

$$
\log_2(x/G)
\ge\left(1-\frac{1-\eta}{M}\right)\log_2x-1
\ge\frac{1+\eta}{2}\log_2x-1.
\tag{6}
$$

The right side of (3) cannot tend to zero unless
$H-\log_2(qMx/G)\to\infty$. This is a necessity for making that
particular upper bound vanish, not a lower bound for the signed tail
itself. Selected representatives with $Q>x^{1-\eta}$ and estimates
using signed cancellation are outside (6). From (4) and
$M\ln(P/2)\le(1-\eta)\ln x$ one also obtains

$$
K\le\log_2\ln x-\log_2\ln\ln x+O(1).
\tag{7}
$$

The condition $P/(M\ln x)\to\infty$ likewise belongs to the
exceptional-event bound in (2); it is not necessary for every use of
(1). The source's choice $P=\exp((\ln\ln\ln x)^3)$ does not meet it.

The remaining sufficient estimate is now exact: construct admissible
parameters with
$|\mathbf E e(\Psi_{G,H}(\mathbf n))|\le1-c$ for some fixed $c>0$
along an unbounded sequence. Equations (2)--(5) would contradict
$S=a/q$. Doing this for a set of $q$ containing a multiple of every
positive integer would prove irrationality. No such saving is proved.

## Where the variance step fails

The source obtains that estimate for $\omega$ from the identity
$\omega(m)=\sum_p1_{p\mid m}$, which writes its phase as
$\sum_p\mathbf X_p$ with each prime piece $\mathbf X_p=o(1)$ on its core
set (its (5.13) and (5.19)). For $\varphi$ the phase has a different
shape.

**Proposition 3.** Let $q\ge1$ and $\eta>0$.

1. If $q$ is odd, then for every integer $h\ge(2+\eta)\ln\ln x$ the
   number $q\varphi(m)2^{-h}$ is not an integer for all but
   $O_\eta(x/\ln\ln x)$ integers $m\le x$.
2. For every integer $h\le(2-\eta)\ln\ln x$ the number
   $q\varphi(m)2^{-h}$ is an integer for all but $O_\eta(x/\ln\ln x)$
   integers $m\le x$.

*Proof.* The valuation is
$v_2(\varphi(m))=\max(a-1,0)+\sum_{\ell\mid m,\ \ell\ \mathrm{odd}}v_2(\ell-1)$
for $2^a\Vert m$. The additive function
$g(m)=\sum_{\ell\mid m,\ \ell\ \mathrm{odd}}v_2(\ell-1)$, the sums here
running over odd primes $\ell$, has mean
$A(x)=\sum_{\ell\le x}v_2(\ell-1)/\ell=(2+o(1))\ln\ln x$. This uses
Mertens' theorem in the classes $1\bmod2^j$ for each fixed $j$, and for
the remaining classes the bound
$\sum_{\ell\le x,\ \ell\equiv1\ (2^j)}1/\ell\ll2^{-j}(j+\ln\ln x)$,
which follows from the trivial count below $2^{2j}$ and the
Brun--Titchmarsh inequality above it. The variance bound is
$B(x)^2=\sum_{\ell\le x}v_2(\ell-1)^2/\ell=O(\ln\ln x)$, by the same
bound. In the prime-power form of Turán--Kubilius the mean and squared
variance parameter differ from these prime sums by $O(1)$, since
$v_2(\ell-1)\le\log_2\ell$ and
$\sum_{\ell}(\log\ell)^2/\ell^2<\infty$. The inequality gives
$\#\{m\le x:|g(m)-A(x)|>\lambda B(x)\}\ll x/\lambda^2$. The
contribution $\max(a-1,0)$ exceeds $t$ for at most $x2^{-t}$ integers.
Taking $\lambda\asymp\eta\sqrt{\ln\ln x}$ proves both parts; when $q$ is
odd a term is an integer exactly when $2^h\mid\varphi(m)$. $\square$

The all-integers estimate does not give an upper valuation bound on the
averaging class. For example, a forced prime divisor congruent to one
modulo a large power of two makes every corresponding totient divisible
by that power. In particular Proposition 3(1) cannot show that the cube's
remaining terms are non-integral, let alone bounded away from integers.

The lower valuation statement does transfer, including after the
normalization by $G$, by a direct argument. Suppose in addition to (4)
that every prime factor of $Q$ other than the $p_\epsilon$ is at most
$w$, where $\ln\ln(w+3)=o(\ln\ln x)$. For each vertex and each level
$h\le H$ separately, and each fixed $0<\varepsilon<1$, all but a
proportion $O_\varepsilon(1/\ln\ln x)$ of the class satisfy

$$
v_2\left(\frac{\varphi(p_\epsilon(N_\epsilon+h))}{G}\right)
\ge(2-\varepsilon)\ln\ln x.
\tag{8}
$$

Here is a proof with its uniformity explicit. Choose a fixed integer $t$
so that $\mu_t=2-2^{1-t}>2-\varepsilon/4$. For odd primes define
$a_t(\ell)=\min\{v_2(\ell-1),t\}$, let $z=\lfloor A^{1/3}\rfloor$,
and set

$$
Z(n)=\sum_{\substack{\ell\le z,\ \ell\text{ odd prime}\\\ell\nmid Q}}
 a_t(\ell)1_{\ell\mid N_\epsilon+h}.
$$

Every prime in this sum is coprime to $Q/p_\epsilon$. The single and
pair divisibility probabilities over $A$ consecutive class members are
$1/\ell+O(1/A)$ and $1/(\ell\ell')+O(1/A)$. Therefore

$$
\mathbf E Z=\sum_{\substack{\ell\le z\\\ell\nmid Q}}
 \frac{a_t(\ell)}\ell+O_t(z/A),\qquad
\operatorname{Var}Z=O_t(\ln\ln z+z^2/A).
$$

Fixed-modulus prime reciprocal sums give
$\sum_{\ell\le z}a_t(\ell)/\ell=(\mu_t+o(1))\ln\ln z$:
write $a_t$ as the sum of the indicators
$\ell\equiv1\pmod{2^j}$, $1\le j\le t$.
The deleted primes contribute at most
$O_t(\ln\ln(w+3)+M/P)=o(\ln\ln x)$. Since
$x^\eta/3\le A\le x$, one has $\ln\ln z=\ln\ln x+O_\eta(1)$.
Chebyshev now gives $Z\ge(2-\varepsilon)\ln\ln x$ with the asserted
exceptional proportion, uniformly in the vertex and shift.

Finally write $N_\epsilon+h=p_\epsilon^a u$ with
$p_\epsilon\nmid u$. Then

$$
\frac{\varphi(p_\epsilon(N_\epsilon+h))}{G}
=\frac{p_\epsilon-1}{G}\,p_\epsilon^a\varphi(u),
$$

whose valuation is at least $Z(n)$, since the primes counted by $Z$
do not divide $Q$ and in particular are different from $p_\epsilon$.
This proves (8).

By (7), the cancelled levels satisfy
$K\le(1/\ln2+o(1))\ln\ln x<(2-\varepsilon)\ln\ln x$ for, say,
$\varepsilon=1/4$. Thus each cancelled coordinate was already integral
for almost all class members. This is a statement for each coordinate,
with a uniform exceptional proportion. It does not assert simultaneous
integrality of all $MK$ coordinates when $K$ grows. Nor does it locate
the remaining phase: non-integrality is weaker than a fixed distance
from $\mathbb Z$, and even many non-integral terms can sum to an integer.

### Two decompositions and their limits

The literal additive-prime identity used for $\omega$ fails for
$\varphi$ even modulo powers of two. For $a\ge1$ and distinct odd
primes $r,s$ with $\gcd(a,rs)=1$,

$$
\varphi(ars)-\varphi(ar)-\varphi(as)+\varphi(a)
=\varphi(a)(r-2)(s-2).
\tag{9}
$$

If $h>v_2(q\varphi(a))$, its product with $q2^{-h}$ is non-integral.
Any expression for $q\varphi(m)2^{-h}\pmod1$ as a constant plus
separate functions of the prime-power divisors of $m$ would have zero
mixed difference on $a,ar,as,ars$, contradicting (9). This excludes
that exact additive identity on the four-point set. It excludes neither
an approximate decomposition on a selected class nor terms involving
several primes together.

The divisor expansion
$\varphi(m)=\sum_{d\mid m}\mu(d)m/d$ is exact, but its raw weighted
pieces have size $q m/(d2^h)$; they do not come with the source's
uniform $o(1)$ bound. Integer pieces can be removed and other pieces
can cancel, so this size calculation is an unmet estimate rather than
an impossibility theorem for a regrouped divisor expansion.

A character expansion exposes a different cost. Already for the
unnormalized case, on the stratum $v_2(\varphi(m))=v$ and for odd $q$,
put $k=h-v\ge3$. The function $u\mapsto e(qu/2^k)$ on odd residues
modulo $2^k$ has $2^{k-2}$ nonzero multiplicative-character
coefficients, each of modulus $2^{1-k/2}$, hence total coefficient mass
$2^{k/2-1}$. To see this, an imprimitive character has zero Gauss sum
by pairing $u$ and $u+2^{k-1}$. For a primitive character the square
of the Gauss sum's modulus is $2^k$: expansion of the square leaves
only the residues $1$ and $1+2^{k-1}$, on which its values are $1$
and $-1$. Divide by the group order $2^{k-1}$.
The odd part of $\varphi(m)$ is multiplicative, so each character
composition is 1-bounded and multiplicative. The valuation stratum,
the growing coefficient mass and the joint shifts still need control.
This calculation is not a lower bound for every possible expansion.

The inspected Theorem 3.1 is a two-point estimate with either its
real-valued equidistribution and prime-value assumptions (3.1)--(3.2),
or its quantified non-pretentiousness assumption (3.3). Its scale
parameter satisfies $\mathcal L\le\ln X$; its progression modulus and
shifts are $O(\mathcal L^c)$ for a sufficiently small absolute $c>0$,
and it omits a quantitatively bounded exceptional set of scales.
A direct application to the full class here is outside that range:
(4) gives $P\gg\ln x$ and $Q\ge(P/2)^M\gg(\ln x)^2$, whereas
$Q=O((\ln x)^c)$ would be required. Removing a forced prime factor
or using a different representation needs a new reduction, with its
hypotheses checked afresh.

More fundamentally, no decomposition and moment comparison yielding a
fixed saving for $\Psi_{G,H}$ has been obtained from these inputs.
The source uses small additive prime pieces before invoking its
correlation theorem. Formula (9) blocks the literal additive identity;
the divisor and character expansions above supply no replacement
estimate. This is the precise remaining gap, not a theorem that all
correlation approaches fail.

## Exact cancellation by dilation designs

A different arrangement of dilations could cancel more levels by equal
arguments. There is a window bound for this particular mechanism.
Arithmetic progressions with different strides need not be disjoint or
meet only once; their intersection period is essential.

**Proposition 4 (bounded coincidence count).** Consider lines
$L_i=\sum_{h\ge1}c_i\varphi(n_i+d_ih)2^{-h}$, $1\le i\le M$,
with nonzero rational $c_i$, positive integer strides $d_i$, and
integer offsets $n_i$ satisfying $n_i+d_i\ge1$. Equal strides are required
to have distinct offsets modulo that stride. On each line select any
$E$ consecutive positive levels. For distinct strides put
$\lambda_{ij}=d_j/\gcd(d_i,d_j)$. Then the number of selected
points on line $i$ that lie on no other line is at least

$$
\left(E-\sum_{\substack{j\ne i\\d_j\ne d_i}}
 \left\lceil\frac E{\lambda_{ij}}\right\rceil\right)^+.
\tag{10}
$$

In particular, if $E\le\lambda_{ij}$ for all pairs of distinct
strides, there are at least $M(E-M+1)^+$ unshared points in total.
Their formal coefficients in $\sum_iL_i$ are nonzero. If $c_i$ is
an integer and a selected level exceeds $v_2(c_i)$, that coefficient
is also non-integral.

*Proof.* Membership of $n_i+d_ih$ in line $j$ requires
$d_ih\equiv n_j-n_i\pmod{d_j}$. This congruence is either
inconsistent or restricts $h$ to one residue modulo $\lambda_{ij}$.
It therefore has at most $\lceil E/\lambda_{ij}\rceil$ solutions
in $E$ consecutive levels. Requiring the corresponding index on line
$j$ to be positive can only remove solutions. Equal strides contribute
none by the offset assumption. A union bound gives (10). Unshared
points on different lines are distinct, and each retains its single
nonzero coefficient. $\square$

The window restriction cannot be omitted. For $n_1=n_2=0$,
$d_1=2$, $d_2=3$, and $E=6$, line 1 has two shared selected points
and line 2 has three. There are only seven unshared pairs, fewer than
$M(E-M+1)=10$. The two progressions share every positive multiple of six.

For the cube's distinct prime strides, $\lambda_{ij}=p_j\ge P/2$.
In regime (4), any block of $E=O(\ln x)$ levels meets the required
window restriction. In particular, the block $K<h\le H$ of (5) has
$E=H-K=\Theta(\ln x)$ while
$M=O(\ln x/\ln\ln x)=o(E)$. It retains at least
$M(E-M+1)$ unshared points. Dividing all weights by $G$ does not change
this count. Thus coincidences of arguments alone do not annihilate the
normalized truncated expression as a formal linear combination.

This does not show that the values of that expression at the totient
are nonzero or far from integers. Divisibility of a totient can turn a
non-integral weight into an integer term, and distinct totient arguments
can satisfy arithmetic relations. Equal-stride lines in one residue
class are also outside the statement; they include the ordinary-tail
combinations of the odd scalar-kernel route. Small strides with repeated
intersections, other level selections and selected representatives
outside (4) remain separate possibilities.

## The favorable-window mechanism

The earlier conditional theorem for $\omega$,
[[../library/irrationality/pratt_2024_irrationality_prime_factor_series_under_prime/theorem_1_3|Pratt's
Theorem 1.3]], uses a different mechanism. Its reduction takes
$N=n_0Q$ with $k^2\mid Q$ for all $k\le K=\lfloor5\log\log\log x\rfloor$
and $n_0Q/k+1$ prime for every such $k$, so that the window values
$\omega(N+k)=\omega(k)+1$ are known exactly; the rest of its tail is
$o(1)$ because $\omega$ is at most $(\log\log x)^2$ on the next
$2\log\log x$ shifts by construction and $O(\log x)$ beyond. The totient
analogue of the exact window is $\varphi(N+k)=\varphi(k)N/k$. Its
discarded positive tail cannot satisfy the analogous smallness bound.

**Proposition 5.** For every $b\ge1$ there is $N_0(b)$ such that no
$N\ge N_0(b)$ and $K\ge1$ satisfy both
$\operatorname{lcm}(1,\ldots,K)\mid N$ and
$b\sum_{k>K}\varphi(N+k)2^{-k}<1$.

*Proof.* By the bound $\varphi(m)\ge m/(1+\log_2m)$ of the dilation
section, and since $m/(1+\log_2m)$ is nondecreasing on the positive
integers, $\sum_{k>K}\varphi(N+k)2^{-k}\ge(N+1)2^{-K}/(1+\log_2(N+1))
\ge N2^{-K}/(2+\log_2N)$. So the second condition forces
$K>\log_2N-\log_2(2+\log_2N)+\log_2b$. The first condition
gives $\psi(K)\le\ln N$ for the Chebyshev function $\psi$, and
$\psi(K)=(1+o(1))K$ by the prime number theorem, so
$K\le(\ln2+o(1))\log_2N$. These bounds are incompatible once $N$ is
large. $\square$

A window with exact values and a discarded positive tail below $1/b$
therefore cannot use the cofactors $k$. At a scale $N=x^{1+o(1)}$,
the positive-tail lower bound also forces $K=\Omega(\ln x)$. An
extension asking for one distinct prime linear form at every position
of such a window would be outside the range of Pratt's
[[../library/irrationality/pratt_2024_irrationality_prime_factor_series_under_prime/conjecture_1_2|quantitative
prime tuples conjecture]], which covers at most $100\log\log\log x$ forms with
coefficients at most $(\log\log x)^{100}$. It does not supply that
longer prescription. This excludes neither a selected arithmetic
subfamily with a different certificate nor weighted cancellation or
another use of a prime-tuples hypothesis.

## Standing and reopening

The retained construction consists of the exact dilation and cube
identities, the common-divisor normalization, and the full averaged
bound (2). The prescribed-pairing weight calculation, the limitation
(6) of its absolute tail bound, the progression valuation estimate (8),
the bounded coincidence count (10), and the positive-tail obstruction
of Proposition 5 have their stated scopes only. These are Plasma AI's
author-recorded arguments, without independent review or a native tier.
The finite examples are exposed in the proofs; no numerical evidence is
needed for their implications.

The construction stops at a specific unproved estimate: a fixed saving
in $|\mathbf E e(\Psi_{G,H}(\mathbf n))|$ for an admissible family.
Neither the literal additive-prime identity nor the raw divisor or
character expansion supplies it. The normalization saves a factor $G$
but does not remove the logarithmic window in this absolute-bound
regime. Coincidences alone leave formal coefficients; they do not settle
the phase at actual totient values. No impossibility claim for all
weighted, correlation or selected-subfamily arguments follows.

A reopening input would be a decomposition with moment bounds yielding
a fixed phase saving, a direct saving for the normalized
phase, or a signed-tail estimate that avoids the bound (3). A new
identity among the actual totient values could also use the surviving
formal coefficients. The independent
[[research/leads/totient_binary_series/integer_interpolation/two_depth_carries|odd
scalar-kernel construction]] remains open: no vector family of cost
$o(2^J)$ is obtained here, and its equivalence with a phase criterion
does not obstruct an arithmetic attack on it.

The external input and reading scope are as follows. Tao--Teräväinen's
arXiv:2512.01739v2 is a preprint; its Theorem 3.1 was checked at statement
depth, and the reduction in Sections 5.1--5.4 through Theorem 5.1 was
followed in the held transcription. The later estimates proving that
technical theorem are not imported. Pratt's arXiv:2409.15185 statement,
Conjecture 1.2, Proposition 2.1 and the deduction of Theorem 1.3 from it
were inspected in the held transcription; its prime-tuples hypothesis
remains an assumption, and no proof of that hypothesis is claimed.

Proposition 3 uses the standard Turán--Kubilius and Brun--Titchmarsh
inequalities. Their exact statements were checked in
[[../library/unit_fractions/elsholtz_2013_counting_number_solutions_erdos_straus/_index|Elsholtz--Tao's
arXiv:1107.1010v6]], Lemma A.2, p. 48, and (A.10), p. 49,
including the page images. Their proofs remain external. The
fixed-modulus reciprocal-prime asymptotic used there and in (8) is
[DLMF (27.11.9)](https://dlmf.nist.gov/27.11.E9), version 1.2.8;
only finitely many
fixed moduli are used for each truncation. The prime number theorem
used in Proposition 5 has the same disclosed external standing as on
[[research/leads/totient_binary_series/integer_interpolation/phase_localization|the
phase-localization page]]. These source statements and the elementary
specializations above confer no independent acceptance on the target.

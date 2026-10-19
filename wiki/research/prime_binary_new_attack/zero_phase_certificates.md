---
name: research/prime_binary_new_attack/zero_phase_certificates
title: Zero-phase certificates for the prime binary series
desc: |
  For Problem 251, one congruence among K+1 consecutive primes would force
  a large following tail under rationality; a two-cutoff count turns this
  into a criterion, the counts that known cluster theorems supply fall short
  of it, and under the Riemann hypothesis a frequency bound for the
  congruence alone would suffice.
tags: []
sources: []
created: 2026-10-16T14:53:50Z
updated: 2026-10-16T14:53:50Z
---

***

This page is Plasma AI's author-recorded analysis, not independently
reviewed, of one construction for
[[problems/irrationality/E0251/_index|Problem 251]]. It uses the notation of
[[research/prime_binary_new_attack/proof_sketch|the parity-prediction sketch]]:
$h_n=(p_{n+1}-p_n)/2$ and $H_n=\sum_{j\ge0}h_{n+j}2^{-j-1}$ for $n\ge2$,
$Q_{n,K}=\sum_{0\le j<K}h_{n+j}2^{-j-1}$, the identities (N), the mean-tail
bound (T), $I_X=\{n:X<p_n\le2X\}$, $N_X=|I_X|$, the phase
$\varphi_{n,K}=\{dQ_{n,K}\}$, and Lemmas A and B. Everything below is
elementary algebra plus (T), except where a published theorem is named. It
proves no new estimate for primes. Its contribution is a construction of
certificates from one congruence and from size bounds, the exact count such a
construction must reach, and the first inequality at which each known
consecutive-prime theorem stops.

## The zero phase is one congruence

For $n\ge2$ and $k\ge0$ write $c_k=(p_{n+k}-p_n)/2$ for the half-offsets of
the primes that follow $p_n$, with $n$ fixed.

**Lemma Z1.** For $n\ge2$ and $K\ge1$,

$$
2^KQ_{n,K}=c_K+\sum_{1\le k<K}2^{K-1-k}c_k .
$$

Hence $Q_{n,K}\in\mathbb Z$ exactly when the right side is divisible by
$2^K$, that is, when

$$
(p_{n+K}-p_n)+\sum_{1\le k<K}2^{K-1-k}(p_{n+k}-p_n)\equiv0\pmod{2^{K+1}} .
$$

*Proof.* Since $h_{n+j}=c_{j+1}-c_j$ and $c_0=0$,

$$
2^KQ_{n,K}=\sum_{0\le j<K}2^{K-1-j}(c_{j+1}-c_j)
=c_K+\sum_{1\le k<K}\bigl(2^{K-k}-2^{K-1-k}\bigr)c_k ,
$$

and $2^{K-k}-2^{K-1-k}=2^{K-1-k}$. $\square$

Call $n$ a *zero-phase start of length $K$* when $Q_{n,K}\in\mathbb Z$; then
$\varphi_{n,K}=0$ for every odd $d$. Three remarks fix what this event is.

- If all $K$ gaps $g_n,\dots,g_{n+K-1}$ are divisible by $2^{K+1}$, the start
  has zero phase; this is the constant residue pattern $r=0$ of
  [[research/prime_binary_new_attack/critical_length_obstructions|the obstruction record]].
  The converse fails. The primes $31,37,41$ are consecutive, with $c_1=3$ and
  $c_2=5$, so $c_2+c_1=8\equiv0\pmod 4$ and the start $p_n=31$ has zero phase
  of length $2$, although neither gap $6$ nor $4$ is divisible by $8$.
- In a model in which $2^KQ_{n,K}$ is uniform modulo $2^K$, a zero-phase start
  of length $K$ has probability $2^{-K}$. The constant pattern asks for $K$
  separate congruences, each of conditional probability $2^{-K}$ for an even
  gap, so its model probability is $2^{-K^2}$. A construction that only
  produces constant patterns gives up this factor.
- The coefficients of the linear form in $p_n,\dots,p_{n+K}$ sum to zero:
  $-2^{K-1}$ for $p_n$, $2^{K-1-k}$ for $p_{n+k}$ with $1\le k<K$, and $1$ for
  $p_{n+K}$. The event is therefore unchanged when all $K+1$ primes are
  translated by one integer: it depends only on their differences. The prime
  number theorem in arithmetic progressions and the Bombieri–Vinogradov
  theorem count primes in residue classes one prime at a time, and they give
  no estimate for the frequency of such an event without further input on
  consecutive differences.

## Rationality forces long tails after a zero phase

**Lemma Z2.** Suppose $S=a/(2^sd)$ with $d$ odd, let $n\ge\max(s+2,3)$, and
let $n$ be a zero-phase start of length $K\ge1$. Then

$$
H_{n+K}=\sum_{\ell\ge1}\frac{p_{n+K+\ell}-p_{n+K}}{2^{\ell+2}}\ge\frac{2^K}{d}.
$$

*Proof.* Lemma B with $\{dQ_{n,K}\}=0$ gives $1\le d2^{-K}H_{n+K}$. For the
displayed form of $H_m$, write $b_\ell=p_{m+\ell}-p_m$ with $b_0=0$; summation
by parts in $H_m=\sum_{j\ge0}(b_{j+1}-b_j)2^{-j-2}$ gives
$\sum_{\ell\ge1}b_\ell(2^{-\ell-1}-2^{-\ell-2})=\sum_{\ell\ge1}b_\ell2^{-\ell-2}$;
both series converge absolutely because $b_\ell$ grows polynomially in
$\ell$. $\square$

This is the structure a rational value would impose. One congruence among the
positions of $K+1$ consecutive primes, past the preperiod, would force the
weighted tail after them to be at least $2^K/d$. By (T), the average of
$H_{n+K}$ over $I_X$ is at most about $(\log X)/2$, so this lower bound is
$2^{K+1}/(d\log X)$ times that average. The contrapositive needs a single
witness.

**Corollary Z2.** Suppose there are starts $n_i\to\infty$, lengths $K_i\ge1$
and numbers $D_i\to\infty$ such that each $n_i$ is a zero-phase start of length
$K_i$ with $D_iH_{n_i+K_i}<2^{K_i}$. Then $S$ is irrational.

*Proof.* Given $a/(2^sd)$, choose $i$ with $n_i\ge\max(s+2,3)$ and $D_i\ge d$.
Then $H_{n_i+K_i}<2^{K_i}/d$, contradicting Lemma Z2. $\square$

The witness must control an infinite tail at a single start. The
consecutive-prime theorems compared below do not provide the required
conditional upper bound after their configurations. The averaged form below
states one way to discharge that obligation.

## Two cutoffs

Fix an odd $d$ and integers $K,J\ge1$, and put $M=K+J$. The continuation of a
start is the next block of $J$ gaps after its prefix of $K$ gaps:

$$
B_{n;K,J}=Q_{n+K,J}=\sum_{0\le\ell<J}\frac{h_{n+K+\ell}}{2^{\ell+1}},\qquad
F_{n;K,J}=\max\bigl(0,\;1-\varphi_{n,K}-d2^{-K}B_{n;K,J}\bigr).
$$

The score $F_{n;K,J}\in[0,1]$ depends only on $M$ consecutive gaps.

**Lemma Z3.** Suppose $S=a/(2^sd)$ with $d$ odd and $n\ge\max(s+2,3)$. Then

$$
F_{n;K,J}\le d2^{-M}H_{n+M}.
$$

If $F_{n;K,J}>0$, then $F_{n;K,J}=1-\varphi_{n,M}$.

*Proof.* By Lemma B, $1-\varphi_{n,K}\le d2^{-K}H_{n+K}$, and by (N) at the
start $n+K$, $H_{n+K}=B_{n;K,J}+2^{-J}H_{n+M}$. Subtracting $d2^{-K}B_{n;K,J}$
gives $1-\varphi_{n,K}-d2^{-K}B_{n;K,J}\le d2^{-M}H_{n+M}$, whose right side is
positive, so the positive part obeys the same bound. For the second claim,
$Q_{n,M}=Q_{n,K}+2^{-K}B_{n;K,J}$. If $F_{n;K,J}>0$, then
$\varphi_{n,K}+d2^{-K}B_{n;K,J}<1$, so this sum is $\{dQ_{n,M}\}$. $\square$

Thus a start with $F_{n;K,J}>1/2$ has $\varphi_{n,M}<1/2$: by the rule (P) of
the sketch it is a mispredicted start at length $M$. The two-cutoff score
describes a subfamily of the starts that Corollary D of the sketch counts at
length $M$; it is not a stronger criterion. Its use is that the subfamily is
described by one congruence and by size bounds.

**Proposition Z4 (counting criterion).** Let $d$ be odd. Suppose that for
arbitrarily large $X$ there are $K,J\ge1$ with $K+J\le X/(\log X)^2$ and a
set $\mathcal F_X\subseteq I_X$ of starts with $F_{n;K,J}\ge1/2$ for every
$n\in\mathcal F_X$ and

$$
|\mathcal F_X|>\frac{2dX}{2^{K+J}} .
\tag{Z4}
$$

Then $S\ne a/(2^sd)$ for every $a$ and $s$. If $|\mathcal F_X|\ge\rho_XN_X$,
a sufficient condition for (Z4) at large $X$ is
$2^{K+J}\ge4d\log X/\rho_X$.

*Proof.* Take $X\ge\max(X_0(1),5)$ with $\pi(X)\ge s+2$. Every $n\in I_X$
has $n\ge\max(s+2,3)$, so Lemma Z3 and (T) with $\varepsilon=1$ give
$|\mathcal F_X|/2\le\sum_{n\in I_X}F_{n;K,J}\le d2^{-M}X$, contradicting
(Z4). For the second claim, $N_X>X/(2\log X)$ for large $X$, so
$\rho_XN_X>2dX/2^{K+J}$ once $2^{K+J}\ge4d\log X/\rho_X$. $\square$

The factor $\log_2(1/\rho_X)$ in the required length cannot be dropped: a rare
family must be certified over correspondingly more gaps.

## Size bounds certify the continuation

Write $P=p_{n+K}$ and $b_\ell=p_{n+K+\ell}-P$. Summation by parts gives

$$
B_{n;K,J}=\sum_{1\le\ell<J}\frac{b_\ell}{2^{\ell+2}}+\frac{b_J}{2^{J+1}} .
\tag{E}
$$

Every coefficient is positive, so upper bounds for the $b_\ell$ bound the
continuation. An upper bound $b_\ell\le W$ says that $(P,P+W]$ contains at
least $\ell$ primes. Additional primes anywhere after $P$ only decrease the
$b_\ell$, so the continuation needs lower counts of primes in intervals, with
no condition on their residues.

**Lemma Z5 (continuation from counts).** Put $A=2^K/d$ and
$W_\ell=\lfloor A2^\ell/(\ell+2)^2\rfloor$ for $1\le\ell\le J$. If
$(P,P+W_\ell]$ contains at least $\ell$ primes for each $1\le\ell\le J$, then
$B_{n;K,J}<A/4$. If moreover $n$ is a zero-phase start of length $K$, then
$F_{n;K,J}>3/4$.

*Proof.* By (E),
$B_{n;K,J}\le\frac A4\sum_{1\le\ell<J}(\ell+2)^{-2}+\frac A2(J+2)^{-2}$.
Since $\sum_{r\ge3}r^{-2}\le\int_2^\infty t^{-2}\,dt=1/2$ and $J\ge1$, this is
at most $A/8+A/18<A/4$; the first sum is empty when $J=1$. Then
$d2^{-K}B_{n;K,J}<1/4$, and with $\varphi_{n,K}=0$ the score exceeds $3/4$.
$\square$

The widths $W_\ell$ are nondecreasing in $\ell$. When $A\ge\lambda\log X$
with a large constant $\lambda$, every width is many times the mean spacing
of $\ell$ consecutive primes, so the hypothesis of Lemma Z5 asks for no
atypically dense configuration. When $A$ is bounded, the levels with $2^\ell$
much smaller than $\log X$ ask for $\ell$ primes within $O(2^\ell/\ell^2)$ of
$P$, a nested cluster far denser than the mean spacing.

The two requirements are not incompatible with admissibility. Take $K=2r$,
$L=2^r$, prefix offsets $a_i=2(iL)^2$ for $0\le i\le K$ and continuation
offsets $a_{K+\ell}=2(KL+\ell)^2$ for $\ell\ge1$. All prefix offsets are
divisible by $2^{K+1}=2L^2$. Every finite set of these offsets lies in
$\{2j^2:j\ge0\}$, which meets one class modulo $2$ and at most $(p+1)/2$
classes modulo an odd prime $p$, so it is admissible. The continuation half
gaps are $2KL+2\ell+1$ for $\ell\ge0$, whose weighted sum is
$\sum_{\ell\ge0}(2KL+2\ell+1)2^{-\ell-1}=2KL+3$; this is below $2^{K-1}/d$
once $K$ is large in terms of $d$. This calculation concerns integers only.
It does not say that any translate of the template consists of consecutive
primes, and prescribing it as a prime pattern is a prime-tuples hypothesis of
the kind used by the conditional claims on the problem page.

## What each mechanism supplies

The certificate needs a family of zero-phase starts whose continuations obey
Lemma Z5 or (E), counted as in (Z4). The known theorems on consecutive primes
produce clusters or strings. The two results below locate where they stop.

**Lemma Z6 (universal zero phase forces one class).** Let $A$ be a set of
at least $K+2$ integers of one parity, with $K\ge1$. Suppose that every subset
$u_0<u_1<\dots<u_K$ of $A$ with $K+1$ elements satisfies
$(u_K-u_0)/2+\sum_{1\le k<K}2^{K-1-k}(u_k-u_0)/2\equiv0\pmod{2^K}$. Then all
elements of $A$ other than its $K-1$ smallest are congruent modulo
$2^{K+1}$.

*Proof.* For $K=1$ the hypothesis directly says that every pair has
difference divisible by $4$. For $K\ge2$, fix the $K-1$ smallest elements
$a_1<\dots<a_{K-1}$, and take any three other elements $v<w<z$.
In a subtuple made of those fixed elements and two of $v,w,z$, the two
variable half-offsets both have coefficient $1$ in Lemma Z1.
Comparing the choices $(v,w)$ and $(v,z)$ gives
$(w-z)/2\equiv0\pmod{2^K}$, and comparing $(v,z)$ and $(w,z)$ gives
$(v-w)/2\equiv0\pmod{2^K}$. Every such triple is therefore in one class
modulo $2^{K+1}$, which proves the assertion. $\square$

Banks, Freiberg and Turnage-Butterbaugh produce, from a sufficiently large
admissible $k$-tuple, an unspecified subtuple of a fixed size $m$ as
consecutive primes infinitely often. Fix $K,J\ge1$, assume
$m\ge K+J+1$ and $k\ge m+K+J$, and suppose that every possible $m$-element
selection is to give a zero-phase prefix of length $K$ and a score
$F_{n;K,J}\ge1/2$, using the first $K+J+1$ selected primes. Any $K+1$
elements of the tuple
other than its $m-K-1$ largest are the first $K+1$ elements of some
selection, so Lemma Z6 applies to the tuple without those largest elements:
all but $K-1$ of the remaining $k-m+K+1$ elements lie in one class modulo
$q=2^{K+1}$. There are at least $K+J+2$ elements in this class. Select its
first $K+1$ elements as the prefix, skip the next element, and select its
next $J$ elements as the continuation. Complete the selection to size $m$
using elements among the omitted $m-K-1$ largest; there are enough, and they
all follow the constructed block.

The first continuation gap is at least $2q$, and the other continuation
gaps are at least $q$. Therefore
$B_{n;K,J}\ge2^K(3/2-2^{-J})\ge2^K$ and $F_{n;K,J}=0$ for every $d\ge1$.
This contradicts the proposed universal score bound, including its boundary
case $d=J=1$. It refutes this particular requirement on every selection,
not the possibility that a prime theorem selects a favorable subtuple, nor
a construction choosing a different root after inspecting its selection.
The theorem does not control a continuation beyond its selected tuple.

**Lemma Z6b (allowing an adaptive root).** Let $m\ge3$, and let $A$ be a
set of $k>(m-1)2^{m-1}$ integers of one parity. Some $m$-element subset
$u_1<\cdots<u_m$ has the following property: at every root and for every
$K,J\ge1$ whose prefix and continuation fit inside this subset, the score
$F$ formed from its successive half-gaps is zero, for every $d\ge1$.

*Proof.* There are $2^{m-1}$ classes of the given parity modulo $2^m$.
One contains at least $m$ elements; choose them as the subset. Every
half-gap is a positive multiple of $2^{m-1}$. Since $K+J\le m-1$,
one has $K\le m-2$, so $Q_{n,K}$ is an integer at any allowed root.
Moreover

$$
B_{n;K,J}\ge2^{m-1}(1-2^{-J})\ge2^{m-2}\ge2^K .
$$

Thus $F=\max(0,1-d2^{-K}B_{n;K,J})=0$. $\square$

Admissibility of a set of shifts for the forms $x+a$ requires all shifts
to have one parity. Consequently this obstruction applies to a construction
which requires every possible selected subtuple to furnish a certificate,
even if the root, $K$ and $J$ are chosen after the selection. For example,
the explicit sufficient threshold quoted in
[[../library/integer_sequences/banks_2014_consecutive_primes_tuples/theorem_1|Banks, Freiberg and Turnage-Butterbaugh's Theorem 1]]
is $k\log k>e^{8m+4}$, which implies $k>(m-1)2^{m-1}$. Indeed, at
$k=(m-1)2^{m-1}$ one has $k\log k<m^2 2^m<e^{8m+4}$.
The comparison concerns this stated sufficient threshold, not the smallest
possible threshold for finding $m$ primes. The theorem could select a
favorable subtuple; Lemma Z6b says that its unspecified selection cannot
be replaced by a guarantee about every selection. Control of the selected
subtuple or of primes outside it remains an additional input.

**Lemma Z6c (unspecified representatives of groups).** Let $m\ge2$, and
let $A_1,\ldots,A_r$ be finite sets of integers of a common parity, with
$r\ge m+1$. Suppose either that $A_1<\cdots<A_r$ and $|A_i|\ge2^m$
for every $i$, or that $|A_i|\ge m2^{m+1}$ for every $i$ with no ordering
assumption. The order means that every element of $A_i$ is smaller than
every element of $A_{i+1}$.
Choose any $m+1$ of the groups. There is a choice of one representative
from each chosen group for which every score $F$ whose prefix and
continuation fit within the chosen representatives is zero, for every
$d\ge1$.

*Proof.* In the ordered case choose the least element of each chosen
group. If $u$ is the
least element of a group of size $L$ and $v$ is the least element of a
later group, then $v-u\ge2L$: the $L$ elements of the earlier group and
$v$ have one parity and are strictly increasing. Every successive
half-gap of the chosen representatives is therefore at least $2^m$.
In the unordered case, pass to integer half-coordinates and choose the
representatives greedily. Each previous choice forbids at most
$2^{m+1}-1$ integers at distance less than $2^m$. At most $m$ previous
choices therefore cannot exhaust a group of size $m2^{m+1}$. The
chosen representatives, sorted in increasing order, again have every
half-gap at least $2^m$.
For any allowed root and $K,J\ge1$, $K+J\le m$ and

$$
B\ge2^m(1-2^{-J})\ge2^{m-1}\ge2^K.
$$

Since $0\le\varphi<1$ and $d\ge1$, one has
$F=\max(0,1-\varphi-d2^{-K}B)=0$. No congruence condition on the
representatives is needed. $\square$

This tests a more structured selection theorem than the arbitrary-subtuple
statement above.
[[../library/primes/banks_2016_limit_points_sequence_normalized_prime_gaps/_index|Banks, Freiberg and Maynard]]
(arXiv:1404.5094v2, Theorem 4.3(ii), p. 10) partition a sufficiently large
admissible $k$-tuple into $r=8m^2+8m$ equal groups. Under hypotheses
(4.15)--(4.19), including smoothness of every pairwise difference and
the prescribed residue class avoiding the sieving primes, at a suitable translate
at least $m+1$ groups each contain exactly one prime, and the intervening
groups contain at most one. Their Section 6 combines this with a covering
of the other shifts to obtain $m+1$ consecutive primes from distinct
groups. The theorem, its deduction from Lemmas 4.5 and 4.6, and this
consecutiveness deduction were read; the analytic estimates in those
lemmas were not checked here. The covering formula (6.1) on p. 23 uses
primes outside $\mathcal Z$; the opposite membership sign in the later
explanatory sentence is a printed misprint. The consecutiveness deduction
uses (6.1), with the excluded primes kept out of the covering.

In a construction from these groups, a proposed certificate which must work
for every permitted selection of $m+1$ groups and every representative
in those groups fails at either size threshold in Lemma Z6c. The proof's parameter
choice $\delta\rho\log k=2m$, with $0<\delta<1/4$ and $0<\rho<1$,
has $k>e^{8m}>r m2^{m+1}$. This comparison concerns that sufficient choice,
not an optimal lower bound for $k$. The lemma does not assert that the
unhelpful representatives actually occur as consecutive primes; it
identifies information absent from an argument that uses the selection
guarantee alone. Selection depending on the phase or on the sizes of the
later gaps, additional primes outside the guaranteed block, or guarantees
with smaller groups are not excluded. The published
theorem also fixes $m$ and $k$ before the prime scale tends to infinity;
it supplies no uniform bound at the growing length in Theorem U8.

**Proposition Z7 (the counts supplied by cluster theorems).** Let a
construction certify $F_{n;K,J_0}\ge1/2$ on a family of proportion at least
$\rho_X$ in $I_X$, using only primes it places, and put $M_0=K+J_0$.

1. Suppose the certificate is extended to a continuation of length $J>J_0$
   by prescribing widths $V_\ell>0$ for the levels $J_0<\ell\le J$ and
   discarding the members with $p_{n+K+\ell}-p_{n+K}>V_\ell$ at some level.
   Assume $K+J\le X/(\log X)^2$ and that the widths are chosen within the
   termwise budget
   $\sum_{J_0<\ell\le J}V_\ell2^{-\ell-1}\le2^K/d$ from (E).
   The unweighted Markov inequality and union bound give the discard
   estimate $(1+o(1))X\sum_\ell\ell/V_\ell$. By Cauchy--Schwarz, this
   available upper estimate is at least
   $(1+o(1))d(J_0+1)X/2^{M_0+2}$ whatever the widths. Subtracting it from
   the supplied lower guarantee $\rho_XN_X$ can prove a positive remainder
   only if $2^{M_0}\rho_X>(1+o(1))(J_0+1)d\log X/4$. This is the condition
   of Proposition Z4 at length $M_0$, up to a factor linear in $J_0$.
   This restriction concerns this termwise budget and discard estimate;
   it is neither a lower bound for the number actually discarded nor a
   necessary condition for every way of controlling the continuation.
2. For the counts proved in
   [[../library/primes/maynard_2014_dense_clusters_primes_subsets/_index|Maynard's dense-clusters paper]]
   (arXiv:1405.2593v2, statements read, proofs not checked), the requirement
   $2^{M_0}\rho_X>(2+o(1))d\log X$, which is (Z4) for a family of proportion
   $\rho_X$, is not established by the stated lower guarantees.
   In this comparison $\rho_X$ means the rate supplied by the quoted
   bound, not the unknown true proportion of configurations. We even grant
   a count of that order in $(X,2X]$; a cumulative count up to $x$ does not
   automatically give this for growing parameters.
   Theorem 3.1 gives at least $C^{-1}\delta\log k$ primes among $k$ linear
   forms on $\gg\#\mathcal A(x)/((\log x)^k\exp(Ck))$ integers, and its
   consecutive clause, for $k\le(\log x)^{1/5}$, replaces $\exp(Ck)$ by
   $\exp(Ck^5)$. Here $M_0\le k-1$, so $2^{M_0}\rho_X\ll2^k(\log X)^{1-k}$,
   which is bounded. Theorem 3.3 gives $m+1$ consecutive primes in one class
   modulo $q$ on $\gg_\epsilon\pi(x)/(2q)^{\exp(Cm)}$ starts, uniformly for
   $m\le c_\epsilon\log\log x$ and $q\le(\log x)^{1-\epsilon}$; here
   $M_0\le m$ and $2^{M_0}\rho_X\ll_\epsilon2^{m-\exp(Cm)}$, which is bounded
   in $m$. Theorem 3.2 gives $\gg\log y$ primes in intervals of length $y$ on
   $\gg x\exp(-\sqrt{\log x})$ starts, and the guaranteed primes give
   $2^{M_0}\rho_X\ll y^{O(1)}\log X\,\exp(-\sqrt{\log X})$, which tends to zero
   for $y\le(\log X)^{O(1)}$, a range containing every $y$ for which the
   theorem exceeds the typical count.

*Proof.* Part 1: use the assumed termwise budget. For
$K+\ell\le X/(\log X)^2$, the prime number theorem gives
$\sum_{n\in I_X}(p_{n+K+\ell}-p_{n+K})\le(1+o(1))\ell X$, so at most
$(1+o(1))\ell X/V_\ell$ starts in $I_X$ violate level $\ell$. By
Cauchy–Schwarz,
$(\sum_\ell\sqrt{\ell2^{-\ell-1}})^2\le(\sum_\ell\ell/V_\ell)(\sum_\ell
V_\ell2^{-\ell-1})$, and keeping only the term $\ell=J_0+1$ on the left gives
$\sum_\ell\ell/V_\ell\ge(J_0+1)2^{-J_0-2}d2^{-K}$. Comparing with
$\rho_XN_X$ and $N_X\sim X/\log X$ gives the stated condition. Part 2:
if a certificate uses only the primes explicitly guaranteed by a theorem,
its length cannot exceed their number minus one. Apply this to the stated
guarantees, allowing the larger bound $k-1$ for Theorem 3.1. The displayed
products follow from the quoted rates and $N_X\sim X/\log X$; each is
$o(\log X)$. None of these comparisons bounds the true count from above.
$\square$

Proposition Z7 limits the use of these stated counts, not the true number of
such configurations: a proof that the configurations are much more frequent
than these lower bounds would reopen the route. Even if every selected
subtuple placed its primes exactly where the prefix and the continuation need
them, the supplied count would not establish (Z4). Each certified gap may cost at
most about one binary digit of rarity, beyond the fixed overhead
$\log_2(4d\log X)$, while each prime that a sieve forces into a short window
costs a factor comparable to $\log X$ in the supplied count.

The other inputs compare as follows, at their exact ranges.

- **Prime number theorem and its forms in progressions.** They supply (T) and
  $N_X\sim X/\log X$. By the third remark after Lemma Z1 they say nothing
  about zero phases by themselves, and they bound the continuation only on
  average over all starts, which is part 1 of Proposition Z7.
- **Bounded gaps.**
  [[../library/primes/maynard_2015_small_gaps_between_primes/proposition_4_2|Maynard's criterion]]
  (arXiv:1311.4600v3) gives, for each admissible $k$-set, at least
  $\lceil\theta M_k/2\rceil$ primes infinitely often. Its stated lower bound
  $M_k>\log k-2\log\log k-2$, with $\theta<1/2$ from Bombieri--Vinogradov,
  yields a guarantee of about $(1/4)\log k$ primes. This is not an upper
  bound for the method. For fixed $k$ the certified length is bounded while (Z4) needs
  $2^{K+J}>2dX/N_X=(2+o(1))d\log X$, the fixed-length obstruction O1 of
  the obstruction record. The same holds for the strings of
  [[../library/integer_sequences/banks_2014_consecutive_primes_tuples/theorem_1|Banks, Freiberg and Turnage-Butterbaugh]]
  (arXiv:1311.7003v3), which also give no count. Shiu's strings in a fixed
  class modulo $q$ have length $m\ll(\log\log x)^{1/\varphi(q)-\epsilon}$, in
  the range reported in Maynard's comparison after Theorem 3.3, so their
  certified length has $2^m=(\log x)^{o(1)}$, below the scale $d\log X$
  that (Z4) needs.
- **Constant residue strings at growing length.** Theorem 3.3 above reaches
  moduli $q\le(\log x)^{1-\epsilon}$. A constant prefix modulo $2^{K+1}$ then
  has $A=2^K/d<(\log X)^{1-\epsilon}$, so Lemma Z5 asks for a dense
  continuation, and Proposition Z7 bounds the count in any case.
- **Large gaps.**
  [[../library/integer_sequences/ford_2018_long_gaps_between_primes/theorem_1|Ford, Green, Konyagin, Maynard and Tao]]
  (arXiv:1412.5029v3) give gaps of size
  $\gg\log X\log\log X\log\log\log\log X/\log\log\log X$ below $X$.
  A long gap is allowed inside a
  zero-phase prefix but its endpoints are not located modulo $2^K$ by the
  theorem, and a long gap in the continuation raises $B_{n;K,J}$. Long gaps
  give lower bounds for tails, which this certificate cannot use.

A single witness for Corollary Z2 needs no count, so the counting comparison
of Proposition Z7 does not settle the pointwise route. The next result
describes witnesses built from one residue class. Lemma Z6 forces such a
class in its specified universal-prefix construction; Lemmas Z6b and Z6c
give separate unhelpful selections. They do not classify every possible
pointwise certificate.

**Proposition Z9 (one-class witnesses).** Let $d$ be odd and $K\ge1$, and let
$p_n,\ldots,p_{n+K}$, with $n\ge3$, be consecutive primes in one class
modulo $2^{K+1}$. Then $n$ is a zero-phase start of length $K$, and every gap
$g_{n+j}$ with $0\le j<K$ is at least $2^{K+1}$. If $n\ge s+2$, the start
contradicts $S=a/(2^sd)$ through Lemma Z2, for every $a$, exactly when
$H_{n+K}<2^K/d$. For such a witness and every $T>0$:

1. if $2^K\ge dT$, the block is a chain of $K\ge\log_2(dT)$ consecutive
   gaps, each at least $2dT$;
2. if $2^K<dT$, then $p_{n+K+\ell}-p_{n+K}<2^{\ell+1}T$ for every $\ell\ge1$.

*Proof.* Every gap of the block is a positive multiple of $2^{K+1}$, so it is
at least $2^{K+1}$, and every half-gap $h_{n+j}$, $j<K$, is a multiple of
$2^K$, so each term $h_{n+j}2^{-j-1}$ of $Q_{n,K}$ is an integer. Lemma Z2
gives $H_{n+K}\ge2^K/d$ under $S=a/(2^sd)$, which is the stated criterion.
In case 1, $2^{K+1}\ge2dT$. In case 2, $H_{n+K}<2^K/d<T$, and for every
$m\ge2$ and $\ell\ge1$,
$H_m>\sum_{j<\ell}h_{m+j}2^{-\ell}=(p_{m+\ell}-p_m)/2^{\ell+1}$, since
$2^{-j-1}\ge2^{-\ell}$ for $j<\ell$ and the later terms are positive.
$\square$

Take $T=\lambda\log p_n$ with a fixed $\lambda>0$. In case 1 the block is a
chain of at least $\log_2(d\lambda\log p_n)$ consecutive gaps, each at least
$2d\lambda\log p_n$. For comparison, Ford, Maynard and Tao, *Chains of large
gaps between primes* (arXiv:1511.04468v1; abstract read, the paper is not
held here), state that for each fixed $k$ there are chains of $k$
consecutive gaps below $X$, each
$\gg k^{-2}\log X\log\log X\log\log\log\log X/\log\log\log X$,
with an effective implied constant
independent of $k$ and $X$ large in terms of $k$. Even if this held uniformly
at $k\asymp\log_2\log X$, the supplied lower guarantee would be
$o(\log X)$, below $2d\lambda\log X$. This is not an upper bound for
the actual gaps. The statement also does not place the primes of a chain in
one class modulo $2^{K+1}$. In case 2 the displacement bounds grow
exponentially with the number of later primes; they do not rule out large
gaps far down the tail. The proof gives the precise bound
$p_{n+K+\ell}-p_{n+K}<2^{K+\ell+1}/d$ for every $\ell$, so each $\ell$ with
$2^{K+\ell+1}<d\ell\log p_n$ puts the $\ell$th prime after the block closer
than $\ell$ mean spacings. That is a cluster immediately after a selected
block, which the cluster theorems do not control (the remark after Lemma
Z6). Since every $\ell$ with $2^{K+\ell+1}<d\log p_n$ qualifies, the block
and this cluster contain at least $\log_2(d\log p_n)-2$ primes when
$2^{K+1}<d\log p_n$. Thus this one-class construction requires size or
residue conditions involving about $\log_2\log p_n$ primes, the critical
length of the sketch. None of the stated theorems supplies their conjunction
with the upper bound for the following infinite tail.
This is a comparison with stated results, not an impossibility theorem.

## The missing theorem

**Zero-phase continuation statement ZPC($d$).** For the odd number $d$ and
arbitrarily large $X$ there are $K,J\ge1$ with $K+J\le X/(\log X)^2$ such that

$$
\#\Bigl\{n\in I_X:Q_{n,K}\in\mathbb Z,\ B_{n;K,J}<\frac{2^{K-1}}d\Bigr\}
>\frac{2dX}{2^{K+J}} .
$$

Each counted start has $F_{n;K,J}>1/2$, so by Lemma Z3 it has
$\varphi_{n,K+J}<1/2$ and is a mispredicted start at length $K+J$. ZPC($d$)
is therefore the count $(C_d)$ of the sketch at length $K+J$, restricted to
this subfamily, and Corollary D of the sketch (or Proposition Z4) shows that
it excludes every rational value with odd denominator part $d$. ZPC($d$) for
every odd $d$ proves that $S$ is irrational. ZPC($1$) alone would show that
the binary expansion of $S$ does not terminate.

In the model of the second remark after Lemma Z1, with the continuation
independent of the prefix, take $K=J=\lceil\log_2(8d\log X)\rceil$. A zero
phase has probability $2^{-K}$. Since $B_{n;K,J}\le H_{n+K}$, (T) and
Markov's inequality show that $B_{n;K,J}\ge2^{K-1}/d$ for at most about
$d\log X/2^K\le1/8$ of all starts. The model count is therefore at least
about $\tfrac78 2^{-K}N_X$, while $2dX/2^{K+J}$ is at most about
$2^{-K}N_X/4$. So ZPC($d$) asks for a proportion of order $1/(d\log X)$ of
starts, with about $2\log_2\log X$ consecutive gaps constrained. The critical
phase statement CPS($d$) of the sketch asks for a positive proportion at about
$\log_2\log X$ gaps. Both are lower bounds for joint statistics of about
$\log\log X$ consecutive gaps, and neither is known. Each implies $(C_d)$ at
its own length; no implication between them is proved. ZPC($d$) separates its
requirement into a congruence on the prefix and size bounds on the
continuation. What it needs is that zero-phase prefixes, at a modulus $2^K$
of order $\log X$, occur with frequency of order $2^{-K}$ and are followed by
unexceptional continuations with positive conditional frequency.

## A second moment removes the continuation

The continuation is needed only because (T) controls the tails on average.
A bound for the second moment of the gaps replaces it by Chebyshev's
inequality, at the price of a longer prefix.

**Proposition Z8.** Suppose there are constants $C_0$ and $B$ with
$\sum_{p_m\le x}g_m^2\le C_0x(\log x)^B$ for all large $x$. Let $d$ be odd and
$c>0$, and suppose that for arbitrarily large $X$ there is
$K\le X/(\log X)^2$ with

$$
2^K>\frac{4C_0d^2(\log X)^{B+1}}c,\qquad
\#\{n\in I_X:Q_{n,K}\in\mathbb Z\}\ge c2^{-K}N_X .
$$

Then $S\ne a/(2^sd)$ for every $a$ and $s$.

*Proof.* Suppose $S=a/(2^sd)$ and take such an $X$ with $\pi(X)\ge s+2$.
By Lemma Z2 every zero-phase start in $I_X$ has $H_{n+K}\ge2^K/d$. By
convexity, $H_{n+K}^2\le\sum_{j\ge0}2^{-j-1}h_{n+K+j}^2$. Summed over
$n\in I_X$, the terms with $K+j\le N_X$ involve only indices $m$ with
$p_m\le4X$ for large $X$, so they contribute at most
$\sum_{p_m\le4X}h_m^2\le C_0X(\log4X)^B$; the terms with $K+j>N_X$
contribute $o(1)$, using $h_m\le p_m\le m^2$ for large $m$. By Chebyshev's
inequality at most $(1+o(1))C_0d^2X(\log X)^B/4^K$ starts in $I_X$ have
$H_{n+K}\ge2^K/d$, while at least $c2^{-K}N_X>c2^{-K}X/(2\log X)$ starts have
zero phase. The first bound is smaller than the second once
$2^K>(2+o(1))C_0d^2(\log X)^{B+1}/c$, a contradiction. $\square$

Under the Riemann hypothesis, Selberg's bound $\ll x(\log x)^3$, recorded on
[[../library/primes/stadlmann_2022_mean_square_gap_between_primes/theorem_1|the mean-square gap page]],
gives $B=3$. The zero-phase event does not involve $d$, so under the Riemann
hypothesis it would suffice that for one $c>0$, one $A>4$ and arbitrarily
large $X$, at least $c2^{-K}N_X$ starts in $I_X$ have zero phase of length
$K=\lceil A\log_2\log X\rceil$; this would exclude every odd $d$ at once. In
the model of the second remark after Lemma Z1 that frequency is $2^{-K}$. No
unconditional lower bound of order $2^{-K}N_X$ for zero-phase starts is known
at any growing length; the constant strings of Theorem 3.3 above are far
rarer. With Stadlmann's unconditional bound $x^{1.23+\varepsilon}$ on the
same page, the condition on $K$ would require $2^K$ to exceed a power of $X$,
a prefix of about $0.23\log_2X$ gaps. Obstruction O4 of the obstruction record
makes the same use of the second moment for mispredicted starts.

**Conditional half-plane comparison.** Suppose that $\zeta(s)$ has no zeros
in $\operatorname{Re}s>\theta$, with $1/2<\theta<1$; the proposed
$\theta=7/8$ case is treated only as an unconfirmed hypothesis. No improvement
on the cited unconditional second-moment bound from this hypothesis and
zero-density estimates is established here, so the bound available for this
comparison remains $\ll_\varepsilon x^{1.23+\varepsilon}$. Repeating Z8's
count comparison gives the sufficient threshold

$$
2^K>C_{\varepsilon,d,c}X^{0.23+\varepsilon}\log X,
\qquad
K>(0.23+\varepsilon)\log_2X+\log_2\log X+
\log_2 C_{\varepsilon,d,c},
$$

for a sufficiently large constant $C_{\varepsilon,d,c}$. The half-plane
hypothesis permits, but does not assert, zeros between $1/2$ and $\theta$;
the power of $X$ here is a limitation of the bound used, not a necessity
theorem for every consequence of that hypothesis. Even under RH, or the
stronger GRH, the zero-phase frequency estimate required above remains
unproved.

## A large-gap count removes the continuation

A tail bound for the number of large gaps can replace the second moment.
The finite cutoff below is necessary: the infinite tail after a prime below
$2X$ includes gaps whose right endpoints exceed $4X$.

**Proposition Z8′.** Put

$$
N(x,H)=\#\{m:p_{m+1}\le x,\ g_m\ge H\}.
$$

Suppose that for fixed $C>0$ and $B'\ge0$, all sufficiently large $x$ and
all $H\ge1$ satisfy

$$
N(x,H)\le \frac{Cx(\log x)^{B'}}{H^2}.
\tag{LG}
$$

Suppose also that for some $c>0$, some $A>B'+1$, and arbitrarily large $X$,
at least $c2^{-K}N_X$ starts in $I_X$ have $Q_{n,K}\in\mathbb Z$, where
$K=\lceil A\log_2\log X\rceil$. Then $S$ is irrational.

*Proof.* Fix a putative representation $S=a/(2^sd)$ with $d$ odd. At all
sufficiently large $X$, Lemma Z2 makes every counted start satisfy
$H_{n+K}\ge T$, where $T=2^K/d$. Take $J=\lceil4\log_2X\rceil$. Since
$K+J=O(\log X)$ and $\pi(4X)-\pi(2X)\gg X/\log X$, the prime number
theorem gives

$$
p_{n+K+J}\le4X\qquad(n\in I_X)
\tag{Z8a}
$$

for all large $X$. The prime number theorem also gives $p_m\le C_1m^2$
for every $m\ge1$, after enlarging $C_1$. Consequently

$$
H_m=\sum_{j\ge0}\frac{g_{m+j}}{2^{j+2}}
\le C_1\sum_{j\ge0}\frac{(m+j+1)^2}{2^{j+2}}
\le C_2(m^2+1).
$$

For $m=n+K+J=O(X)$ this proves, uniformly over $I_X$,

$$
2^{-J}H_{n+K+J}=O(X^{-2})<T/2.
\tag{Z8b}
$$

Thus $H_{n+K}\ge T$ implies
$\sum_{0\le j<J}g_{n+K+j}2^{-j-2}>T/2$. The positive weights
$w_j=1/((j+1)(j+2))$ sum to $1$ over all $j\ge0$, and to less than $1$
over $j<J$. Some $j<J$ therefore satisfies

$$
g_{n+K+j}\ge (T/2)w_j2^{j+2}.
\tag{Z8c}
$$

For a fixed $j$ the map $n\mapsto n+K+j$ is injective, and (Z8a) puts the
right endpoint of every such gap below $4X$. All thresholds in (Z8c) exceed
$1$ for large $X$. Applying (LG) at each threshold and taking the union
bound now gives

$$
\begin{aligned}
\#\{n\in I_X:H_{n+K}\ge T\}
&\le C_3X(\log X)^{B'}T^{-2}
  \sum_{j\ge0}\frac{(j+1)^2(j+2)^2}{4^j}\\
&\le C_4d^2X(\log X)^{B'}4^{-K}.
\end{aligned}
\tag{Z8d}
$$

Only the finite set $j<J$ was counted by (LG); extending the numerical
majorant to an infinite convergent series adds no gaps. Since
$N_X\sim X/\log X$, the ratio of (Z8d) to the assumed zero-phase count is

$$
O_{c,d}\!\left(\frac{(\log X)^{B'+1}}{2^K}\right)
=O_{c,d}\bigl((\log X)^{B'+1-A}\bigr)=o(1).
$$

This contradicts Lemma Z2. The same phase-frequency assumption works for
every fixed $d$, and the unbounded sequence of $X$ passes every preperiod
$s$. $\square$

A second-moment hypothesis as in Z8 implies (LG) with $B'=B$ by Markov's
inequality, so Z8′ includes that specialization at the logarithmic prefix
length used here. A separately proved (LG) with $B'=2$ would instead require
$A>3$, and one with $B'=1$ would require $A>2$. These substitutions are
conditional implications; no source establishing either stronger (LG) is
used here. In every case the zero-phase frequency remains a separate
unproved input.

The elementary bound $N(x,H)\le x/H$ cannot replace (LG) in this proof.
The same finite-cutoff argument then gives $O(X/T)$ exceptional starts.
Against $c2^{-K}N_X$ its upper bound has ratio $O_d(\log X)$, independently
of the choice of $A$. Increasing the prefix length alone does not make that
first-moment estimate small enough.

## The step lemma

With
[[research/prime_binary_new_attack/proof_sketch|the step lemma of the sketch]],
the same construction runs on the $t$-step gaps $p_{n+t}-p_n$ with the
integer lattice and mean bound $t(1+\varepsilon)X/2$. In the lattice
inequalities use multiplier $1$; in the mean-based count include the
factor $t$. One such count excludes every odd part dividing $2^t-1$.
The certificates now involve filtered gaps: their length $K+J$ uses
$K+J+t-1$ original gaps.
[[research/prime_binary_new_attack/critical_length_obstructions|Proposition O9]]
shows that clearing the denominator in this way does not shorten the
required window of original gaps for the same mean-based count.

## Status of the steps

- Lemmas Z1, Z2, Z3, Z5, Z6, Z6b and Z6c, Corollary Z2 and Proposition Z4 are proved
  here from Lemma B and (T); they are author-recorded. Proposition Z8 is
  proved from its stated second-moment hypothesis; with Selberg's bound it is
  conditional on the Riemann hypothesis. Proposition Z8′ is proved from
  (LG) and its separate phase-frequency hypothesis, with the finite and far
  tails both accounted for.
- Proposition Z7 is proved for the stated counts of the named theorems, read
  at statement depth; it is a cost bound for those inputs, not an
  impossibility theorem for the route.
- Proposition Z9 is proved here. Its comparison with the chain theorem of
  Ford, Maynard and Tao rests on that paper's abstract alone. A single
  one-class witness needs a chain of about $\log_2\log p_n$ gaps of size
  at least a constant times $\log p_n$, or a cluster right after its block;
  neither is supplied by the stated theorems. Reopening the pointwise route
  needs a theorem that controls the selected subtuple, or a chain theorem
  uniform at that length with gaps of order $\log X$ in one class modulo
  $2^{K+1}$, together with a suitable bound for the weighted following
  tail. No restriction forbidding large distant gaps is asserted.
- ZPC($d$) is open for every $d$. It is true in the model above and not
  known to be false. Reopening this route needs a lower bound for zero-phase
  starts of order $2^{-K}N_X$ with conditional control of the next
  $\log_2\log X+O_d(1)$ gaps, or any family meeting $(Z4)$ with its own
  certified length.

---
name: research/prime_binary_series/truncation_certificates
title: Truncation certificates for the prime binary series
desc: |
  Certificate arguments for Problem 251: exact lattice and mean-tail tests,
  a congruence block supplied by a consecutive-prime theorem, the remaining
  tail and counting gaps, and the limits of the replacements examined.
created: 2026-10-15T00:04:37Z
updated: 2026-10-17T22:11:11Z
---

***

## Target and standing

[[problems/irrationality/E0251/_index|Problem 251]] asks whether
$S=\sum_{n\ge1}p_n/2^n$, with $p_1=2$, is irrational. The question is open.
The two conditional proofs on its claim pages,
[[problems/irrationality/E0251/claims/2026_09_06_land|Land]] and
[[problems/irrationality/E0251/claims/2026_09_07_ringer|Ringer]], are claimed,
unrefereed and not independently reviewed, and their hypotheses are unproved.

This is Plasma AI's author-recorded certificate argument, without independent
review or a tier. The
[[research/prime_binary_new_attack/proof_sketch|canonical editable sketch]]
composes these identities and bounds with the current counting criteria.
The elementary deductions here use the prime number theorem where stated;
the consecutive-prime construction also uses the cited published theorem.
They give no new prime-distribution estimate. The common starting point is
the rational lattice of weighted tails. The attempted replacements are a
congruence block with a small following tail and an averaged phase test.
Both leave a prime-distribution gap. The stops below concern the particular
estimates used, not all irrationality arguments or all fixed-size blocks.

## The exact interface

Write $g_n=p_{n+1}-p_n$, $d_j(n)=p_{n+j}-p_n$ and

$$
G_n=\sum_{j\ge0}\frac{g_{n+j}}{2^{j+1}},\qquad
P_{n,K}=\sum_{0\le j<K}\frac{g_{n+j}}{2^{j+1}} .
$$

The bound $p_m=O(m\log(2m))$ ensures convergence of these tails. The
following identities are elementary.

1. $S=2+\sum_{m\ge1}g_m2^{-m}=2+G_1$, by summation by parts
   ([[../library/irrationality/bloom_2026_erdos_problem_251_discussion/reformulation_gap_series|the reformulation proves this identity]]).
2. $G_{n+1}=2G_n-g_n$, since $2G_n=g_n+\sum_{j\ge1}g_{n+j}2^{-j}$.
3. $G_n=\sum_{j\ge1}d_j(n)2^{-j-1}$, by exchanging the order of summation,
   and for $K\ge1$
   $P_{n,K}=\sum_{1\le j<K}d_j(n)2^{-j-1}+d_K(n)2^{-K}$.
4. $G_n=P_{n,K}+2^{-K}G_{n+K}$ for every $K\ge0$.
5. $G_m>2$ for $m\ge2$: every gap from $p_2$ on is at least $2$, and not all
   are $2$, since one of three consecutive odd numbers is divisible by $3$.

**Rationality.** If $S=a/b$ with integers $a,b\ge1$, then $bG_1=a-2b$ is an
integer, and by identity 2 so is $bG_n$ for every $n$. Conversely, if $G_n$ is
rational for one $n$, then $G_1$ is rational, by identity 2 run backwards.
Write $b=2^sb'$ with $b'$ odd. Since $G_{n+1}=2G_n-g_n$, the denominator of
$G_n$ divides $b'$ once $n>s$, and then the fractional part of $G_n$, which
equals that of $2^{n-1}G_1$, depends only on $n$ modulo the order of $2$ modulo
$b'$; take period $1$ when $b'=1$. Conversely, repetition of two fractional
parts gives $(2^{v-u}-1)G_u\in\mathbb Z$ for some $v>u$, hence rationality.
An equivalent form of the target, by counting the integers $m$ with
$\pi(m)=k$, is $S=\sum_{m\ge0}2^{-\pi(m)}$.

## The certificate lemma

Write $\{x\}=x-\lfloor x\rfloor$.

**Lemma 1.** Let $b\ge1$, $n\ge1$ and $K\ge0$ be integers and $L<U$ real
numbers with $L<G_{n+K}\le U$. Put $x=bP_{n,K}+b2^{-K}L$ and
$w=b2^{-K}(U-L)$. If $\{x\}<1-w$, then $bG_n$ is not an integer, so
$S\ne a/b$ for every integer $a$.

*Proof.* By identity 4, $bG_n=x+b2^{-K}(G_{n+K}-L)$ lies in $(x,x+w]$. The
least integer greater than $x$ is $x+1-\{x\}$, which exceeds $x+w$. $\square$

The condition $\{x\}<1-w$ says exactly that the interval
$(P_{n,K}+2^{-K}L,\,P_{n,K}+2^{-K}U]$ misses $(1/b)\mathbb Z$, that is,
$\lfloor b(P_{n,K}+2^{-K}U)\rfloor=\lfloor b(P_{n,K}+2^{-K}L)\rfloor$. Width
below $1/b$ ($w<1$) is necessary for it and not sufficient. To refute
rationality one needs, for each fixed $b$, some $(n,K,L,U)$; $K$ and every
constant may depend on $b$, and no growth of $K$ with an auxiliary scale
follows from the quantifiers alone.

In the restricted case $L=0$, $U=\Gamma$, this is
$2^{-K}\Gamma<\Delta_b(P_{n,K})$, where
$\Delta_b(P)=(\lfloor bP\rfloor+1)/b-P$. Since $G_{n+K}>2$ for
$n+K\ge2$, such a certificate needs $2^K>2b$. An informative lower
endpoint instead makes the width depend on $U-L$, so that length
restriction does not apply to every bracket.

The lemma's shape is universal: if $bG_n\notin\mathbb Z$, then $K=0$ with a
sufficiently tight bracket around $G_n$ satisfies it. All the content lies in
how the bracket $(L,U]$ and the phase $\{bP_{n,K}\}$ are certified from
information about primes, and the stops below concern exactly that.

### Two instances

**Land's template.** If $g_{n+j}=4j+2$ for $0\le j<K$, then
$P_{n,K}=6-(4K+6)2^{-K}$ and $G_n-6=2^{-K}(G_{n+K}-4K-6)$. In Land's
configuration no prime follows the template within the stretch Land excludes,
so $g_{n+K}>8K+12$; then every $d_j(n+K)\ge g_{n+K}+2(j-1)$, and identity 3
gives $G_{n+K}\ge g_{n+K}/2+1\ge4K+8$. With $L=4K+6$ one has $x=6b$, and
Lemma 1 asks for

$$
0<G_{n+K}-4K-6<2^K/b ,
$$

the realization that Land's route must supply. With the trivial lower
endpoint $L=2$ instead, and $(4K+4)b<2^K$, one has
$\{x\}=1-(4K+4)b2^{-K}$, and Lemma 1 asks for $G_{n+K}<4K+6$: a template
followed by a tail smaller than its template value. These are two sufficient
windows on opposite sides of $4K+6$; Land's composite stretch selects the
first side.

**A congruence block.** The phase needs only congruences, not exact gaps.

**Lemma 2.** Let $K\ge1$. If $p_{n+j}\equiv p_n\pmod{2^{j+1}}$ for
$1\le j<K$ and
$p_{n+K}\equiv p_n\pmod{2^K}$, then $P_{n,K}$ is an integer. This holds in
particular when $p_n,p_{n+1},\dots,p_{n+K}$ are all congruent modulo $2^K$.

*Proof.* Each term of identity 3's formula for $P_{n,K}$ is an integer.
$\square$

If $S=a/b$ and the block of Lemma 2 occurs at $n$, then
$b2^{-K}G_{n+K}=bG_n-bP_{n,K}$ is a positive integer, so
$G_{n+K}\in(2^K/b)\mathbb Z$ and $G_{n+K}\ge2^K/b$; for $n>s$ the same holds
with $b'$ in place of $b$. Hence such a block followed by $G_{n+K}<2^K/b$
refutes the denominator $b$; this is Lemma 1 with $L=0$ and $\{x\}=0$.

Such blocks exist for every fixed $K\ge1$.
[[../library/integer_sequences/banks_2014_consecutive_primes_tuples/theorem_1|Banks, Freiberg and Turnage-Butterbaugh's Theorem 1]]
applies with $g=1$, $m=K+1$, $k\ge k_{K+1}$ and shifts $b_j=1+2^Kc_j$, where
$c_1,\dots,c_k$ are the first $k$ primes exceeding $k$. The forms $x+b_j$
are admissible: the shifts are odd, no $c_j$ is divisible by an odd prime
$p\le k$, so no $x+b_j$ vanishes at $x\equiv-1\pmod p$, and $k<p$ for the
remaining primes. The consecutive primes it supplies are pairwise
congruent modulo $2^K$, so rationality would force $G_{n+K}\ge2^K/b$ at the
end of infinitely many blocks of bounded diameter. This is no contradiction:
the theorem gives no upper bound for $G_{n+K}$ along those occurrences.
The phase is controlled whichever subtuple the theorem selects. Selecting
one occurrence with $G_{n+K}<2^K/b$ remains an additional obligation.

Finite gap data alone cannot discharge that obligation in the class of
positive even integer sequences. For any prescribed block of $K\ge1$ even
gaps, $A=2^KP$ is an even integer. Choose an even $c\ge2$ with
$c\equiv-A\pmod{2^K}$ and continue with the constant gap $c$. Then
$G=P+2^{-K}c$ is an integer. This completion is not a sequence of primes
and says nothing against a prime-specific argument; it identifies the
uncontrolled continuation in a use of the block alone.

## The averaged tail

**Lemma 3.** With $T_m=p_m+G_m$, identity 2 gives $T_{m+1}-T_m=G_m$, so
$\sum_{m=A}^{B}G_m=T_{B+1}-T_A$ and
$\sum_{m\le M}G_m=p_{M+1}+G_{M+1}-S$. Moreover $G_m=o(p_m)$. Consequently,
for every $\varepsilon>0$ there is $X_0(\varepsilon)$ such that for
$X\ge X_0(\varepsilon)$, $0\le K\le X/(\log X)^2$ and every set $T$ of indices
$n$ with $X<p_n\le2X$,

$$
\sum_{n\in T}G_{n+K}\le(1+\varepsilon)X.
$$

If $T$ is nonempty, some $n\in T$ has
$G_{n+K}\le(1+\varepsilon)X/|T|$.

*Proof.* For $G_m=o(p_m)$, fix $J$ and split identity 3 at $j=J$ and $j=m$.
The terms $j\le J$ contribute at most $d_J(m)=p_{m+J}-p_m=o(p_m)$ by the
prime number theorem. The terms $J<j\le m$ contribute at most
$2^{-J}p_{2m}\le3\cdot2^{-J}p_m$ for large $m$. The terms $j>m$ contribute at
most $\sum_{j>m}p_{2j}2^{-j-1}\le\sum_{j>m}4j^22^{-j-1}$, which tends to $0$.
Since $J$ is arbitrary, $G_m=o(p_m)$. The indices $n+K$ are distinct and lie
in $(\pi(X),\pi(2X)+K]$, so the sum is at most
$T_{\pi(2X)+K+1}-T_{\pi(X)+1}<p_{\pi(2X)+K+1}+G_{\pi(2X)+K+1}-X$. For
$K\le X/(\log X)^2$ the prime number theorem gives
$p_{\pi(2X)+K+1}=2X+o(X)$, and $G_{\pi(2X)+K+1}=o(X)$. $\square$

## Route I: an averaged certificate

Fix $b\ge1$ and $w\in(0,1)$, and put

$$
E=E_{b,w}(K,X)=\bigl\{n:X<p_n\le2X,\ \{bP_{n,K}+b2^{1-K}\}<1-w\bigr\}.
$$

**Proposition 4.** Let $\varepsilon>0$, $X\ge X_0(\varepsilon)$ and
$1\le K\le X/(\log X)^2$. If

$$
|E_{b,w}(K,X)|\ge\frac{(1+\varepsilon)bX}{2^Kw},
$$

then $S\ne a/b$ for every integer $a$.

*Proof.* Lemma 3 gives $n\in E$ with $G_{n+K}\le(1+\varepsilon)X/|E|\le2^Kw/b$.
Apply Lemma 1 with $L=2$, valid by identity 5 since $n+K\ge2$, and
$U=2^Kw/b$: then $b2^{-K}(U-L)<w$ and $\{x\}<1-w$. $\square$

Read in reverse, rationality forces fewer than
$(1+\varepsilon)bX/(2^Kw)$ of these shifted phases to lie in $[0,1-w)$.
This is a test for one denominator, not a demand for equidistribution.

**Length.** Since $|E|\le m_X:=\pi(2X)-\pi(X)=(1+o(1))X/\log X$,
for fixed $\varepsilon,w$ Proposition 4 can apply only when
$2^K\ge((1+\varepsilon)/w+o(1))b\log X$; in particular
$K\ge\log_2\log X+\log_2b-o(1)$. This explains the length of about
$\log\log n$ consecutive gaps in Tao's suggestion recorded on the problem
page, for this sufficient count condition. It is not a restriction on all
certificates or all proofs.

**Loss.** Were the phases equidistributed modulo 1,
$|E|$ would be about $(1-w)m_X$. If instead $|E|\ge\lambda(1-w)m_X$ for some
$\lambda\in(0,1]$, Proposition 4 applies once
$\lambda>(1+2\varepsilon)b\log X/(2^Kw(1-w))$ and $X$ is large. Taking
$\varepsilon=1/10$, $w=1/2$ and
$K=\lceil\log_2\log X+\log_2b\rceil+C$, a retained fraction
$\lambda>5\cdot2^{-C}$ suffices. For fixed $A>1$ and
$K=\lceil A\log_2\log X\rceil$, a fraction
$\lambda>5b(\log X)^{1-A}$ suffices.

**What it still asks.** The phase is determined by $b$ and the residues of
$g_{n+j}$ modulo $2^{j+1}$ for $0\le j<K$, or by the displacement residues
in identity 3. Exact gaps are sufficient information, not necessary
information. At $K=\log_2\log X+O_b(1)$, Proposition 4 asks for a positive
proportion of all starting indices; at $K=A\log_2\log X$, it asks for a
proportion of order $(\log X)^{1-A}$. No prime estimate obtained here
supplies either count. The
[[research/prime_binary_series/single_phase_comparison|single-phase comparison]]
derives the signed correlation test and explains why a direct substitution
of upper bounds for its tuple counts does not prove it.

## Route II: pointwise certificates

**Lemma 5.** If $G_m\le U$, then $p_{m+j}-p_m\le2^jU$, that is,
$\pi(p_m+2^jU)-\pi(p_m)\ge j$, for every $j\ge1$.

*Proof.* By identity 3,
$G_m\ge\sum_{i\ge j}d_i(m)2^{-i-1}\ge d_j(m)\sum_{i\ge j}2^{-i-1}=d_j(m)2^{-j}$.
$\square$

**Proposition 6.** Suppose Lemma 1 applies at $(n,K)$ with $L\le2$, and let
$q=p_{n+K}$ be sufficiently large. Then
$\pi(q+2^j(2+2^K/b))-\pi(q)\ge j$ for every $j\ge1$, and

$$
\max(K,\log_2b)+\pi(q+2\log q)-\pi(q)\ge\log_2(b\log q)-2 .
$$

*Proof.* Since $w<1$, $G_{n+K}\le U<L+2^K/b\le V:=2+2^K/b$, and Lemma 5 gives
the first claim. If $V>\log q$, then $K>\log_2(b(\log q-2))$ and the display
holds for large $q$. Otherwise take $j=\lfloor\log_2(2\log q/V)\rfloor\ge1$.
Then $2^jV\le2\log q$, so the window $(q,q+2\log q]$ holds at least
$j\ge\log_2\log q-\log_2V$ primes. Since
$\log_2V\le1+\max(1,K-\log_2b)\le2+\max(0,K-\log_2b)$, adding
$\max(K,\log_2b)$ to both sides gives the display. $\square$

Thus a certificate with $L\le2$ must satisfy a tradeoff: the window after
the block contains at least
$\log_2(b\log q)-2-\max(K,\log_2b)$ primes, with at least $j$ primes within
$2^jV$ of $q$ at each scale. This is a necessary consequence of a small
absolute tail, not a general lower bound on how much prime information a
certificate must encode. In particular, it does not say that the $K$
preceding primes lie in an interval of length $O(\log q)$.

These nested counts are not sufficient for the tail bound. For example, in
the class of increasing integer sequences take an even $U\ge2$ and set
$d_j=2^jU$ for $1\le j\le R$, then
$d_j=2^RU+2(j-R)$ for $j>R$. Every $d_j\le2^jU$, but
$\sum_{j\ge1}d_j2^{-j-1}=(R+1)U/2+2^{1-R}$ can greatly exceed $U$.
A proposed replacement must bound the weighted sum itself, not just its
individual terms.

A certificate with an informative lower endpoint $L>2$ lies outside
Proposition 6, and that lower bound must itself be certified. The natural
source is a prime-free stretch $(q,q+E)$ with $E\ge2$. The quantities
$e_j=d_j(n+K)-E-2(j-1)$ are nonnegative and nondecreasing. Hence
$R_*=G_{n+K}-E/2-1=\sum_{j\ge1}e_j2^{-j-1}$ satisfies $e_j\le2^jR_*$.
If a certificate uses this lower endpoint and proves $R_*\le V_*$, it
therefore requires

$$
p_{n+K+j}\le q+E+2(j-1)+2^jV_*\qquad(j\ge1).
$$

This residual estimate treats that specific source of a lower bound.
Arbitrary informative brackets, including weighted cancellations, are not
covered by Proposition 6 or by this observation.

## Replacements tried and where they stop

**Land's lower count.**
[[../library/irrationality/land_2026_conditional_proof_irrationality_prime_series/theorem_2|Land's Theorem 2]]
realizes the template through a lower bound for the number of $t\in[X,2X]$
with every $t+2j^2$ ($0\le j\le K$) prime, where
$K=\lceil\log_2\log X+4\log_2\log\log X\rceil$, together with lower
first-moment and upper mixed-moment counts for primes added to the
constellation. The certificate it feeds is the first instance above. The
count-to-tail step needs only one aggregate quantity. In Land's notation, put
$H_0=2K^2+8K+12$ and $H=\lfloor\log X(\log\log X)^3\rfloor$; let $A$ be the
set of such $t$, $Z(t)$ the number of primes $t+u$ with $0\le u\le H_0$
outside the template, and $Y(t)$ the number of primes $t+h$ with
$H_0<h\le H$ and $h\equiv0$ or $2\pmod6$. Take $R\ge1$ integral and put

$$
W=\sum_{t\in A}Y(t)-\sum_{t\in A}Y(t)Z(t)-(R-1)|A| .
$$

If $W>0$, at least $W/H$ roots have $Z=0$ and $Y\ge R$, since spoiled roots
contribute at most $\sum YZ$, roots with $Y<R$ at most $(R-1)|A|$, and each
root at most $H$. Their prescribed primes are consecutive, and their terminal
indices $n+K+R$ are distinct. Since $W>0$ implies $R\le H$ and
$K+H=o(X/(\log X)^2)$, the proof of Lemma 3 applies to this common offset
for sufficiently large $X$ (including $t=X$ changes only an $o(X)$ endpoint
term). It selects a root with

$$
G_{n+K}\le\frac{H-2K^2}{2}
 +2^{-R}\frac{(1+\varepsilon)XH}{W}=:\Gamma.
$$

Indeed, the first $R$ gaps after $p_{n+K}=t+2K^2$ sum to at most
$H-2K^2$, and each has weight at most $1/2$. Together with the strict
lower bound from the empty interval, $\Gamma<4K+6+2^K/b$ supplies the
certificate. This is an extraction of the count-to-tail mechanism, not a
new estimate for $W$.

Under the restricted uniform hypothesis of Sections 4--5, Land obtains
$|A|\ge X\exp(-C\ell^2)$,
$\sum_A Y\ge |A|\mu$ and $\sum_A YZ=o(|A|\mu)$, where
$\ell=\log\log X$ and $\mu=cH/(\log X\log K)$ for a small fixed $c>0$.
The inputs are respectively a lower base count, summed lower
single-extension counts, and summed upper mixed two-extension counts, all
on at most $K+3$ shifts. Taking $R=\lfloor\mu/4\rfloor$ leaves
$W\gg|A|\mu$, and $R\asymp\ell^3/\log\ell$ makes the discounted terminal
remainder tend to zero. Thus $\Gamma=O(H)$ and $H/2^K=O(1/\ell)$.
The common terminal offset is essential to this selection argument;
prime-cluster existence alone does not supply it.

**Stop:** the unbounded-scale lower counts of this route imply infinitely
many twin primes, since $t,t+2$ are in every base pattern. They remain
unproved. Land deduces the required uniform estimates from
[[../library/primes/kuperberg_2023_sums_singular_series_large_sets_tail/conjecture_1_3|Kuperberg's Conjecture 1.3]],
whose single pair of absolute error constants precedes the scale and shift
set. That conjecture asserts error $O(x^{1-\delta})$ uniformly for up to
$(\log\log x)^3$ shifts in $[0,(\log x)^2]$; it is not a proved replacement.

**Ringer's comparison.**
[[../library/irrationality/ringer_2026_local_gap_statistics_telescoping_normality/corollary_1_2|Ringer's Corollary 1.2]]
assumes the positive comparison (19). With $N_X=\pi(2X)-\pi(X)$ and the
stopped transforms $J_C,J_M$ of its Section 5, this says, for one fixed
$c\ge1$,

$$
1-\frac{\sum_{|A|=L}J_C(A)}{N_X}
 +\frac{\sum_{|A|=L}[J_C(A)-cJ_M(A)]_+}{N_X}\longrightarrow0.
$$

It implies upper domination of nonnegative first-$L$ tests within the
physical span $\lfloor(6/5)L\log X\rfloor$, together with vanishing actual
span-failure mass. At $\kappa=1/\log2$, $L$ is near
$\log_2\log X+\sqrt{\log_2\log X}$. The averaged adverse-error assumption
(16) suffices for (19), without pointwise relative errors on individual
tuples. With the model's local laws (Section 4, not reconstructed here) and
the unconditional mean-tail estimate, Section 3 makes limiting phase laws
absolutely continuous. That already excludes a rational finite orbit;
invariance is then used to derive normality. No equivalence between
Land's and Ringer's specialized hypotheses is asserted.

For the present target a single event would suffice. If, for some
$0<w<1$, $0<\eta\le1$ and integer $C$ with $2^C\ge2b/(\eta w)$, at most
a proportion $1-\eta$ of the $n$ with
$X<p_n\le2X$ have $\{bP_{n,K}+b2^{1-K}\}\ge1-w$ for
$K=\lceil\log_2\log X\rceil+C$ and arbitrarily large $X$, then
Proposition 4 with $\varepsilon=1/2$ gives $S\ne a/b$, using
$N_X\sim X/\log X$. This is one non-concentration statement per denominator,
with a fixed positive fraction and along one sequence of scales. It does
not ask for the distribution of every phase or for normality.
The [[research/prime_binary_series/single_phase_comparison|signed comparison]]
goes further by deriving the exact tuple-count functional for one test.
**Stop:** no arithmetic lower estimate for that functional is obtained.
Its positive coefficients prevent a direct substitution of upper sieve
bounds alone. Cancellation between tuple orders remains a possible extra
input; naming it is not a way to prove it.

**Fixed-size cluster theorems.**
[[../library/primes/maynard_2015_small_gaps_between_primes/proposition_4_2|Maynard's Proposition 4.2]],
[[../library/integer_sequences/banks_2014_consecutive_primes_tuples/theorem_1|the consecutive-primes theorem of Banks, Freiberg and Turnage-Butterbaugh]]
and
[[../library/primes/pintz_2016_polignac_numbers_conjectures_erdos_gaps_primes/main_theorem|Pintz's Main Theorem]]
have different counting conclusions. Maynard guarantees a specified number
of primes among a fixed admissible tuple, without prescribing which ones.
Banks, Freiberg and Turnage-Butterbaugh give a fixed consecutive subtuple
infinitely often, but their Theorem 1 states no occurrence rate or following
tail bound. Pintz gives at least two consecutive primes at
$\gg_k\mathfrak S(\mathcal H)X/(\log X)^k$ translations for fixed
$k\ge3.5\times10^6$, an admissible tuple
$\mathcal H\subset[0,\varepsilon\log X]$ with sufficiently small
$\varepsilon>0$ depending on $k$, and onset $X>X_0(\mathcal H)$.
The other tuple entries have all prime factors exceeding $x^{c_1(k)}$
at root $x$, for some $c_1(k)>0$; they need not be prime. This gives
neither a prescribed long prime block nor a complete-tail bound.

**Stop:** the congruence construction above resolves the phase for the
unspecified subtuple, but none of these statements selects an occurrence
with $G_{n+K}<2^K/b$. Averaging a complete tail over a supplied set of
$M_X$ distinct terminal indices gives only $(1+o(1))X/M_X$ by Lemma 3.
A lower count of order $X/(\log X)^k$, after any bounded multiplicities
are accounted for, therefore supplies an upper bound of order
$(\log X)^k$, not the fixed bound needed for fixed $K,b$.
For $L\le2$, Proposition 6 also exposes missing nested counts after the
block, growing with $q$ when $K$ is fixed. It does not forbid those counts
from occurring, and an unquantified infinity of blocks does not select them.
Nor can the fixed-tuple statements be used with $k=k(X)$ without a uniform
onset estimate. This stops the substitutions made here, not every possible
use of these theorems for a fixed denominator.

For a numerical comparison of guarantees only: with Maynard's yield
$\theta M_k/2$ and his bound $M_k>\log k-2\log\log k-2$, the proved
guarantee for a $k$-shift configuration is about $(\theta/2)\log k$ primes,
that is $(1/4+o(1))\log k$ at Bombieri–Vinogradov's $\theta=1/2$. The cluster
alternative of Proposition 6 with $K,b$ fixed needs about
$\log_2\log q=(1/\log2)\log\log q$ primes in $(q,q+2\log q]$, where $k\le2\log q$,
so this lower-bound guarantee is smaller by a factor of about
$4/\log2\approx5.8$, or
$2/\log2\approx2.9$ at $\theta=1$. The held texts give no upper bound for
$M_k$, so this compares the requirement with the proved yield, not with a
limit of the method. Substituting $k$ of size $\log q$ here is a comparison
of formulas, not an application of a fixed-tuple theorem at growing $k$.
An adequate uniform theorem would still have to place the primes at the
required scales after the block and bound the complete weighted tail.

**Growth and short-block statistics.** W. Cook's unreviewed
[sparse-rationalisation construction](https://github.com/wcook04/plectis-erdos/blob/605b2735ee308e1d1c621c81b8a363e1d4e05925/paper/251/erdos-251-prime-gap-dyadic-series.tex)
claims nonnegative corrections to prime gaps, eventually bounded by
$(\log(n+3))^\epsilon$ for any fixed $0<\epsilon<1$, on a support meeting
each index interval $[M,2M)$ in $O_\epsilon(M/\log\log M)$ points. They
make the dyadic sum rational while preserving cumulative growth, every
fixed eventual congruence of gaps and cumulative sums, and empirical
block laws at lengths $o(\log\log M)$. The reconstructed positions are
integers, not asserted primes. Rare certificate occurrences may lie in the
changed blocks. This does not exclude rare fixed blocks, actual primality,
or statistics at length comparable to $\log\log M$.

**Growing denominators.**
[[../library/irrationality/hancl_2004_irrationality_cantor_series/theorem_5_1|Hančl and Tijdeman's Theorem 5.1]]
requires $p_n=o(a_n^2)$, and their
[[../library/irrationality/hancl_2004_irrationality_cantor_series/theorem_6_1|Theorem 6.1]]
requires $a_n/\log n\to\infty$, among other hypotheses. The denominator
products equal $2^n$ for all $n$ only if every $a_n=2$, which violates
both requirements. Their
[[../library/irrationality/hancl_2004_irrationality_cantor_series/example_3_1|Example 3.1]]
uses $2^{p_n}$ instead. This excludes those particular applications only.

## What this page does not cover

Arguments that never certify a bracket for a single tail are not restricted
here, for instance a contradiction drawn from the forced periodicity of the
fractional parts of $G_n$ (see Rationality above) by means other than the
phase counts of Route I. That periodicity is equivalent to rationality, so it
reformulates the question and supplies no input by itself. Lemma 1 is
universal, so every stop above concerns how a bracket or a phase is certified,
not the lemma.

## Remaining input and reopening conditions

The remaining sufficient prime inputs for the routes retained here are:

- Route I: for every $b\ge1$ there are $w\in(0,1)$, an $X\ge X_0(1)$ and
  $1\le K\le X/(\log X)^2$ with $|E_{b,w}(K,X)|\ge2bX/(2^Kw)$; one $X$ per $b$
  suffices.
- Route II: for every $b\ge1$ some $n$, $K$ and a certified bracket satisfying
  Lemma 1, for example a block of Lemma 2 followed by $G_{n+K}<2^K/b$; with
  $L\le2$ every such certificate obeys Proposition 6.

The route reopens on any of the following.

- A proved lower bound for the phase event in Proposition 4, or for the
  signed functional on the linked page, with constants beating the mean-tail
  error. A fixed positive fraction suffices at
  $K=\log_2\log X+\log_2b+O_b(1)$; the displayed loss calculation gives
  the smaller fraction that suffices at a longer truncation.
- A theorem that places a congruence block next to a tail satisfying
  $\sum_{j\ge1}(p_{n+K+j}-p_{n+K})2^{-j-1}<2^K/b$, or supplies another
  bracket satisfying Lemma 1. Nested counting bounds alone do not imply
  this weighted inequality.
- An argument of a different shape, one that certifies no bracket for a
  single tail.

---
name: research/prime_binary_new_attack/proof_sketch
title: Parity prediction for the prime binary series
desc: |
  The canonical sketch for Problem 251, from a rational sum through an
  integer carry lattice to a contradiction conditional on a consecutive
  prime-block estimate. An upper comparison may lose c^K for any c<2.
  Parity prediction, zero-phase alternatives, model computations and an
  exact failure log distinguish the held reductions from the missing
  arithmetic estimate.
created: 2026-10-15T18:43:21Z
updated: 2026-10-17T23:52:10Z
---

***

## Target and standing

[[problems/irrationality/E0251/_index|Problem 251]] asks whether
$S=\sum_{n\ge1}p_n2^{-n}$, with $p_1=2$, is irrational. The question is open;
the problem page records the status search and the two conditional claims.

This is Plasma AI's canonical editable proof sketch. The section "How the
pieces compose, and what is held" gives the complete proposed contradiction
through an upper count for consecutive prime blocks, with its single
arithmetic gap marked. Alternative formulations remain available. This page
proves a sharpened form of the averaged criterion of
[[research/prime_binary_series/truncation_certificates|the truncation-certificate sketch]]
(Theorem C and Corollary D). It recasts that criterion as a dichotomy about
predicting the parity of prime gaps, with no dependence on the denominator
(Theorem F), and it shows that a rational $S$ would make the prediction exact
at every large index once about $0.525\log_2p_m$ gaps are used
(Proposition G). The proofs are complete, author-recorded and not
independently reviewed. They use elementary algebra, the prime number theorem
through the mean-tail bound (T) below, and, for Proposition G only, the
Baker–Harman–Pintz gap bound. They prove no new estimate for primes, and the
problem stays open: no required prime-block estimate is proved. The section
"The named gap" states the corresponding parity-count input. The additional
[[theory/irrationality/L228_sparse_prime_position_interpolation/_index|sparse interpolation theorem]]
preserves the nth prime at a set of indices of density one, while attaining
an interval of binary-series values. Its altered terms need not be prime.
The
[[research/prime_binary_new_attack/critical_length_obstructions|obstruction record]]
explains why the substitutions examined so far do not supply it.

The elementary
[[research/prime_binary_new_attack/matching_gap_windows|matching-window constraint]]
gives another formulation of a possible contradiction: equal finite gap
windows with sufficiently small later tails must start in the same index
class modulo the multiplicative order of two in the odd denominator, and,
for every odd denominator including $1$, their preceding gaps must agree
modulo $4$. Producing late windows that violate either restriction is
unproved. The independently accepted review on the matching-window page
concerns the index-class conditional alone; it supplies no review of the
preceding-gap congruence or of the other results in this sketch.

The
[[research/prime_binary_new_attack/consecutive_block_counts|upper-count note]]
states the lattice as two lower counts that a rational value would force:
one weighted tail value repeated about $N_X/(d\log X)$ times among the starts
in $I_X$, and most starts followed by a block of about $\log_2\log X$
consecutive gaps with a small endpoint carry. Condition (AC) does not depend
on the denominator. Theorem U8 permits an upper comparison with loss $Cc^K$,
for any $c<2$, by using $K=\lceil A\log_2\log X\rceil$ with
$A>1/\log_2(2/c)$. The independent-gap model and a reference incorporating
small odd primes satisfy the required phase estimate. The comparison with
actual consecutive primes is unproved. The tuple upper bounds examined
here have factorial losses and do not keep the primes consecutive; their
failure to give the comparison is not a limitation proved for all sieve
methods.

The section "Binary digits and the lattice" records the first link of every
route: the binary digits of $S$ from the second on are the parities of the
integer parts of the gap tails, and the step lemma turns every rational value
into a dyadic case for the gaps $p_{n+t}-p_n$, with $t$ the order of $2$
modulo the odd part of the denominator.
[[research/prime_binary_new_attack/zero_phase_certificates|The zero-phase analysis]]
builds mispredicted starts from one congruence among consecutive primes and
size bounds on the gaps after them, states the count ZPC($d$) it needs, and
shows that the counts proved by the known cluster theorems fall short of it.
[[research/leads/prime_binary_irrationality/_index|The lead page]] summarizes
the route and its current gap.

## Notation and the retained interface

Write $g_n=p_{n+1}-p_n$ and $G_n=\sum_{j\ge0}g_{n+j}2^{-j-1}$, as on the
truncation sketch. For $n\ge2$ the gap $g_n$ is even; put

$$
h_n=\frac{g_n}{2},\qquad
H_n=\frac{G_n}{2}=\sum_{j\ge0}\frac{h_{n+j}}{2^{j+1}},\qquad
Q_{n,K}=\sum_{0\le j<K}\frac{h_{n+j}}{2^{j+1}}\qquad(n\ge2,\ K\ge0).
$$

Thus $h_n$ is odd exactly when $p_n$ and $p_{n+1}$ lie in different classes
modulo $4$. Identities 2, 4 and 5 of the truncation sketch, halved, give

$$
H_{n+1}=2H_n-h_n,\qquad H_n=Q_{n,K}+2^{-K}H_{n+K},\qquad H_n>1
\qquad(n\ge2,\ K\ge0).
\tag{N}
$$

Let $I_X=\{n:X<p_n\le2X\}$ and $N_X=|I_X|=\pi(2X)-\pi(X)$. The mean-tail
Lemma 3 of the truncation sketch, divided by $2$, reads as follows; it rests on
the prime number theorem and is author-recorded there.

**(T)** For every $\varepsilon>0$ there is $X_0(\varepsilon)$ such that for
$X\ge X_0(\varepsilon)$, $0\le K\le X/(\log X)^2$ and every $T\subseteq I_X$,

$$
\sum_{n\in T}H_{n+K}\le\frac{(1+\varepsilon)X}{2}.
$$

Write $\{x\}=x-\lfloor x\rfloor$. A rational $S$ can be written
$S=a/(2^sd)$ with $a\in\mathbb Z$, $s\ge0$ and $d\ge1$ odd; the results below
hold for every such representation.

## Binary digits and the lattice

The first link of every route is elementary. It is recorded here with its
indexing, because a tail is also often written with its sum starting one gap
later. For $N\ge1$ put $T_N=\sum_{k\ge1}p_{N+k}2^{-k}$; every series below
converges absolutely because $p_n=O(n\log(2n))$.

**Digit lemma.** For $N\ge1$,

$$
T_N=p_{N+1}+G_{N+1}=p_N+2G_N,\qquad \{G_N\}=\{2^{N-1}S\}.
$$

Let $\epsilon_N=\lfloor2^NS\rfloor-2\lfloor2^{N-1}S\rfloor\in\{0,1\}$ be the
$N$th binary digit of $S$, so that the expansion terminates if $S$ is a
dyadic rational. Then

$$
\epsilon_N\equiv p_N+p_{N+1}+\lfloor G_{N+1}\rfloor\pmod2,
\qquad
\epsilon_N\equiv\lfloor G_{N+1}\rfloor\pmod2\quad(N\ge2).
$$

Consequently $S$ is rational exactly when the sequence
$\lfloor G_{N+1}\rfloor\bmod2$, $N\ge2$, is eventually periodic.

*Proof.* Write $p_{N+k}=p_{N+1}+\sum_{1\le i<k}g_{N+i}$ and exchange the
absolutely convergent sums:

$$
T_N=p_{N+1}+\sum_{i\ge1}g_{N+i}\sum_{k>i}2^{-k}
=p_{N+1}+\sum_{i\ge1}g_{N+i}2^{-i}=p_{N+1}+G_{N+1},
$$

and $p_N+2G_N=p_N+g_N+G_{N+1}$ is the same number. Next,
$2^NS=\sum_{n\le N}p_n2^{N-n}+T_N$, and the first sum is an integer congruent
to $p_N$ modulo $2$. Hence
$\lfloor2^NS\rfloor\equiv p_N+p_{N+1}+\lfloor G_{N+1}\rfloor\pmod2$, and
$\epsilon_N\equiv\lfloor2^NS\rfloor\pmod2$. For $N\ge2$ both primes are odd.
The same decomposition gives $\{2^NS\}=\{G_{N+1}\}$, which is the stated
identity at $N+1$; at $N=1$ it reads $\{S\}=\{G_1\}$, true because
$S=p_1/2+T_1/2=2+G_1$. The last statement is the base-two criterion: a real
number is rational exactly when its binary digits are eventually periodic.
$\square$

At $N=1$ the identity reads $\epsilon_1\equiv1+\lfloor G_2\rfloor$, since
$p_1=2$ is even. A tail written as $\sum_{j\ge1}g_{N+j}2^{-j}$ is $G_{N+1}$ in
this indexing.

**Residues do not fix a digit.** For every start $n$ and every $r\ge1$, the
parity of $\lfloor G_n\rfloor$ is not determined by the residues of the gaps
modulo $2^r$. Among sequences of positive even gaps, adding $2^r$ to
$g_{n+r-1}$ and changing nothing else keeps every residue modulo $2^r$,
increases $G_n$ by exactly $2^r\cdot2^{-r}=1$, and so changes the parity of
$\lfloor G_n\rfloor$. The altered sequence is not asserted to consist of
prime gaps; the example shows that a digit depends on the sizes of the gaps
as well as on their residues. In the phase of Lemma B below, the halved gap
$h_{n+j}$ enters only through its residue modulo $2^{j+1}$, so a gap enters
through its actual size once $2^{j+1}$ exceeds it, at about
$j=\log_2\log p_n$ (item O7 of the obstruction record).

**Step lemma.** For $t\ge1$ put $g^{(t)}_m=p_{m+t}-p_m$,

$$
G^{(t)}_n=\sum_{j\ge0}\frac{g^{(t)}_{n+j}}{2^{j+1}}=G_n+G_{n+1}+\dots+G_{n+t-1},
\qquad V_t=G^{(t)}_1=\sum_{m\ge1}\frac{p_{m+t}-p_m}{2^m}.
$$

Then

$$
(2^t-1)S=\sum_{1\le n\le t}p_n2^{t-n}+V_t .
$$

Hence $V_t$ is a dyadic rational exactly when $S=a/(2^sd)$ with $d$ odd and
$d\mid2^t-1$, and $S$ is rational exactly when $V_t$ is a dyadic rational for
some $t\ge1$. If $V_t\in2^{-s}\mathbb Z$, then $G^{(t)}_n\in2\mathbb Z$ for
every $n\ge\max(s+2,3)$; this holds in particular when $S=a/(2^sd)$ and
$t=\operatorname{ord}_d(2)$, with $t=1$ when $d=1$.

*Proof.* The sum formula for $G^{(t)}_n$ follows from
$p_{n+j+t}-p_{n+j}=\sum_{0\le i<t}g_{n+j+i}$. The identity is $2^tS-S$ with the
first $t$ terms of $2^tS$ separated:
$\sum_{n\ge1}p_n2^{t-n}-\sum_{m\ge1}p_m2^{-m}
=\sum_{n\le t}p_n2^{t-n}+\sum_{m\ge1}(p_{m+t}-p_m)2^{-m}$, and the first sum
on the right is an integer. If $S=a/(2^sd)$ with $d\mid2^t-1$, then
$(2^t-1)S\in2^{-s}\mathbb Z$, so $V_t\in2^{-s}\mathbb Z$. Conversely, if $V_t$
is dyadic, then $S$ is an integer plus $V_t$, divided by $2^t-1$, so it is
rational and the odd part of its reduced denominator divides $2^t-1$. Every
odd $d$ divides $2^t-1$ for $t=\operatorname{ord}_d(2)$. Finally
$G^{(t)}_{n+1}=2G^{(t)}_n-g^{(t)}_n$, so
$G^{(t)}_n=2^{n-1}V_t-\sum_{k<n}2^{n-1-k}g^{(t)}_k$ is an integer for
$n\ge s+1$; since $g^{(t)}_n$ is even for $n\ge2$, $G^{(t)}_{n+1}$ is even
for $n\ge\max(s+1,2)$. $\square$

So every rational value is a dyadic case for a coarser gap sequence, and the
odd part $d$ of the denominator is replaced by the step $t$. In the halved
form $H^{(t)}_n=G^{(t)}_n/2$ the lattice is $\mathbb Z$, and (T), applied to
the $t$ shifts, gives $\sum_{n\in T}H^{(t)}_{n+K}\le t(1+\varepsilon)X/2$ for
$T\subseteq I_X$ and $K+t\le X/(\log X)^2$. Lemma B, the rule (P), Theorem C
and Corollary D below therefore hold for the halved $t$-step gaps
$(p_{n+t}-p_n)/2$ with $d$ replaced by $1$ and the right side of Theorem C
multiplied by $t$. A count of mispredicted starts for the $t$-step gaps
exceeding $2tX/2^K$, along arbitrarily large $X$, excludes every odd
denominator part dividing $2^t-1$ at once. Its critical length in
$t$-step gaps is $\log_2(t\log X)+O(1)$, but a block of $K$ such gaps uses
$K+t-1$ original gaps.
[[research/prime_binary_new_attack/critical_length_obstructions|Proposition O9]]
shows that every nonnegative integer filter which clears $d$ obeys the
same lower threshold $\log_2(d\log X)+1-o(1)$ in original gaps for this
mean-based count. The step lemma can help only if the filtered statistic
has an arithmetic estimate unavailable for the original one; it does not
reduce the required original window just by clearing the denominator.
The case $d=1$ is $t=1$. The index classes used by the
[[research/prime_binary_new_attack/matching_gap_windows|matching-window note]]
for $d>1$ are extra structure of the original gap sequence, which this
reformulation does not use.

## The criterion

**Lemma A (odd lattice).** If $S=a/(2^sd)$ with $d$ odd, then
$dH_n\in\mathbb Z$ for every $n\ge\max(s+2,3)$.

*Proof.* By identity 1 of the truncation sketch, $S=2+G_1$, and iterating
$G_{k+1}=2G_k-g_k$ gives $G_n=2^{n-1}G_1-\sum_{k<n}2^{n-1-k}g_k$. Since
$2^sdG_1=a-2^{s+1}d$ is an integer, $dG_n\in\mathbb Z$ for $n\ge s+1$. For
$n\ge\max(s+1,2)$ the number $dG_{n+1}=2dG_n-dg_n$ is even, because $g_n$ is
even. Hence $dH_m=dG_m/2\in\mathbb Z$ for $m\ge\max(s+2,3)$. $\square$

The truncation sketch's Rationality paragraph gives $dG_n\in\mathbb Z$; the
extra factor $2$ is the parity of the gaps, and it is worth one binary digit in
every count below.

**Lemma B (one-sided phase).** If $S=a/(2^sd)$ with $d$ odd,
$n\ge\max(s+2,3)$ and $K\ge0$, then

$$
1-\{dQ_{n,K}\}\le d2^{-K}H_{n+K}.
$$

If moreover $d2^{-K}H_{n+K}<1$, then $\{dQ_{n,K}\}=1-d2^{-K}H_{n+K}$ and
$\lfloor dQ_{n,K}\rfloor=dH_n-1$.

*Proof.* By (N), $dQ_{n,K}=dH_n-x$ with $x=d2^{-K}H_{n+K}>0$, and
$dH_n\in\mathbb Z$ by Lemma A. If $x\notin\mathbb Z$, then
$\{dQ_{n,K}\}=1-\{x\}$, so $1-\{dQ_{n,K}\}=\{x\}\le x$. If $x\in\mathbb Z$,
then $x\ge1\ge1-\{dQ_{n,K}\}$. If $x<1$, then $dQ_{n,K}$ lies strictly
between the integers $dH_n-1$ and $dH_n$, which gives both equalities.
$\square$

**The prediction rule.** Fix an odd $d$. For $K\ge1$ put

$$
\varphi_{n,K}=\{dQ_{n,K}\},\qquad
\psi_{n,K}=\Bigl\{d\sum_{1\le j<K}\frac{h_{n+j}}{2^{j+1}}\Bigr\},\qquad
\beta_{n,K}=\begin{cases}1,&\psi_{n,K}<1/2,\\0,&\psi_{n,K}\ge1/2,\end{cases}
$$

with $\psi_{n,1}=0$. Since $dh/2^{j+1}$ modulo $1$ depends only on $h$ modulo
$2^{j+1}$, the predicted parity $\beta_{n,K}$ is a function of $d$ and of the
residues $h_{n+j}\bmod 2^{j+1}$, $1\le j<K$. Because $d$ is odd,
$dh_n/2\equiv(h_n\bmod2)/2\pmod 1$. If $h_n$ is even, then
$\varphi_{n,K}=\psi_{n,K}$; if $h_n$ is odd, then $\varphi_{n,K}$ equals
$\psi_{n,K}+1/2$ when $\psi_{n,K}<1/2$ and $\psi_{n,K}-1/2$ otherwise. In both
cases

$$
\varphi_{n,K}\ge\tfrac12\iff h_n\equiv\beta_{n,K}\pmod 2 .
\tag{P}
$$

**Theorem C (rationality forces parity prediction).** Suppose $S=a/(2^sd)$
with $d$ odd. Let $\varepsilon>0$, let $X\ge\max(X_0(\varepsilon),5)$ with
$\pi(X)\ge s+2$, and let $1\le K\le X/(\log X)^2$. Then:

1. $\sum_{n\in I_X}(1-\varphi_{n,K})\le(1+\varepsilon)dX/2^{K+1}$;
2. $\#\{n\in I_X:h_n\not\equiv\beta_{n,K}\pmod2\}\le(1+\varepsilon)dX/2^K$;
3. every $n\in I_X$ with $h_n\not\equiv\beta_{n,K}\pmod 2$ has
   $H_{n+K}\ge2^{K-1}/d$.

*Proof.* Every $n\in I_X$ satisfies $n>\pi(X)\ge s+2$ and $n\ge3$, so Lemma B
applies to it. Summing Lemma B over $I_X$ and applying (T) with $T=I_X$ gives
part 1. By (P), the set in part 2 is $\{n\in I_X:\varphi_{n,K}<1/2\}$, and each
of its members contributes more than $1/2$ to the sum in part 1. For part 3,
if $d2^{-K}H_{n+K}<1/2$, Lemma B gives $\varphi_{n,K}=1-d2^{-K}H_{n+K}>1/2$.
$\square$

In words: if the odd part of a denominator of $S$ is $d$, then in every long
dyadic range the parity of $(p_{n+1}-p_n)/2$, that is, whether $p_n$ and
$p_{n+1}$ lie in the same class modulo $4$, is given by the explicit rule
$\beta_{n,K}$ applied to the residues of the next $K-1$ halved gaps, for all
but at most $(1+\varepsilon)dX/2^K$ starting indices. When
$2^K\ge2^Cd\log X$ the exceptions number about $2^{-C}N_X$ at most.

**Remark (past residues fix future sizes).** Applying Lemma B at $n-K$ and at
$n$, whenever $n-K\ge\max(s+2,3)$, $d2^{-K}H_n<1$ and $d2^{-K}H_{n+K}<1$,

$$
\lfloor dQ_{n,K}\rfloor+1=dH_n=2^K\bigl(1-\varphi_{n-K,K}\bigr).
$$

The right side depends only on the residues $h_{n-K+j}\bmod2^{j+1}$ of the
previous $K$ gaps; the left side is $d$ times the weighted size of the next
$K$ gaps, rounded down. By (T), applied with shifts $0$ and $K$, and Markov's
inequality, the two conditions on $H$ fail for at most
$(1+\varepsilon)dX/2^K$ starts in $I_X$. So a rational
$S$ would tie the sizes of the gaps that follow almost every prime, at the
scale of the mean gap, to the binary residues of the gaps that precede it.

**Corollary D (sufficient count).** Let $d$ be odd. Suppose that for
arbitrarily large $X$ there is an integer $1\le K\le X/(\log X)^2$ with

$$
\#\{n\in I_X:h_n\not\equiv\beta_{n,K}\pmod 2\}>\frac{2dX}{2^K}.
\tag{$C_d$}
$$

Then $S\ne a/(2^sd)$ for every $a\in\mathbb Z$ and $s\ge0$. If $(C_d)$ holds
for every odd $d$, then $S$ is irrational.

*Proof.* Given $a$ and $s$, take $X$ with $(C_d)$, $X\ge\max(X_0(1),5)$ and
$\pi(X)\ge s+2$, and apply part 2 of Theorem C with $\varepsilon=1$. $\square$

**Length.** The left side of $(C_d)$ is at most $N_X=(1+o(1))X/\log X$, so
$(C_d)$ requires $2^K>2d\log X\,(1+o(1))$, that is,
$K\ge\log_2\log X+\log_2d+1-o(1)$. At $K=\lceil\log_2(d\log X)\rceil+C$ it
asks for more than about $2^{1-C}N_X$ mispredicted starts; at
$K=\lceil A\log_2\log X\rceil$ with fixed $A>1$, for more than about
$2d(\log X)^{1-A}N_X$. The required block of about $\log_2\log X$ consecutive
gaps is the critical length for this averaged criterion.

**Relation to the earlier criterion.** Proposition 4 of the truncation sketch,
with $b=d$ and $w=1/2$, asks for at least $(1+\varepsilon)dX/2^{K-1}$ starts
with $\{dP_{n,K}+d2^{1-K}\}<1/2$, where $P_{n,K}=2Q_{n,K}$. Corollary D runs
the same averaged mechanism on $H$ instead of $G$, so the count it asks for is
halved, and the phase window becomes the parity rule (P). The two criteria
have the same critical length and differ in strength by one binary digit. The
gain is structural: the event has an exact parity form whose balance under
translations (Lemma E) does not depend on $d$.

## The named gap

**Critical phase statement CPS($d$).** For the odd number $d$ there are a
constant $C\ge3$ and arbitrarily large $X$ such that, with
$K=\lceil\log_2(d\log X)\rceil+C$,

$$
\#\{n\in I_X:h_n\not\equiv\beta_{n,K}\pmod 2\}\ge2^{2-C}N_X .
$$

Since $N_X>X/(2\log X)$ and $2^K\ge2^Cd\log X$ for large $X$, CPS($d$) gives
$2^{2-C}N_X>2^{1-C}X/\log X\ge2dX/2^K$, which is $(C_d)$. So CPS($d$) for one
$d$ excludes every denominator with odd part $d$, and CPS($d$) for every odd
$d$ proves that $S$ is irrational. CPS($1$) alone would show that the binary
expansion of $S$ does not terminate.

CPS($d$) asks only for a fixed positive proportion, which may be small, of
mispredicted starts, along one sequence of scales, at block length
$\log_2\log X+O_d(1)$. A model in which $h_n\bmod 2$ is close to uniform and
nearly independent of the later residues gives a proportion close to $1/2$, by
Lemma E below. The primes below $2\times10^7$ behave that way:
[[research/prime_binary_new_attack/evidence/_index|the finite check]] finds
mispredicted fractions between $0.49$ and $0.51$ for $X\in\{10^6,10^7\}$,
$d\le15$ and $C\le6$, where a rational sum would force them, at large scales,
below about $2^{1-C}$. Such finite observations exclude no denominator. No
proof of CPS($d$) for any $d$ is known to this sketch, and no
unconditional estimate of this kind at growing block length is known to this
sketch. Known positive-proportion theorems for consecutive primes concern
fixed block lengths and constant residue patterns; the obstruction record
compares them with this requirement. A mispredicted start is a start whose
next $K$ gaps form a residue pattern on which the rule fails, so CPS($d$) is a
lower bound for the number of starts in a union of residue patterns of
consecutive gaps. Obstruction O2 bounds the number of exact patterns that
such a certificate would need, conditional on its stated sieve premise (U).

**Residues below the critical length.** Proposition O8 of
[[research/prime_binary_new_attack/critical_length_obstructions|the obstruction record]]
gives a comparison sequence preserving these residues and cumulative growth.
For every sequence of
positive even gaps with $p_n\sim n\log n$, and every block length with
$2^K/\log X\to0$, adding sparse multiples of $2^K$ to the gaps, of size
$o(\log n)$, gives a sequence whose sum is a dyadic rational, whose positions
keep their growth, and whose residue patterns of length $K$ are unchanged at
every start. Conversely, part 1 of Theorem F below, whose proof applies to
every such sequence, shows that when $2^K/\log X\to\infty$, every sequence
with a rational sum has residue laws nearly singular to their translates.
The pointwise residue data below the critical length and the growth of
$p_n$ alone therefore do not force irrationality. CPS($d$) is posed at
$\log_2\log X+O(1)$, and
part 2 of Theorem F at $\log_2\log X+\omega_X$ with $\omega_X\to\infty$.

[[theory/irrationality/L228_sparse_prime_position_interpolation/_index|L228 strengthens the comparison for the actual prime sequence]].
For every nested sequence of integer moduli $q_n=o(\log n)$ and every
prescribed prefix, it constructs one density-zero set $D$ such that an
interval of values, including dyadic rationals, is attained by increasing
integer sequences $(a_n)$ equal to $p_n$ outside $D$. They satisfy
$a_n\equiv p_n\pmod{2q_n}$ at every index and change each gap by
$o(\log n)$. Taking $q_n=2^{K_n}$ preserves the subcritical residue patterns
at every start, including starts in $D$. The argument pairs each positive
gap change with an equal negative change at a later gap; a classical
prime-pair upper bound shows that the intervening position intervals have
density zero. It is author-recorded, not independently reviewed. It does not
preserve primality at every index and does not rule out arguments using
that property or relative counts of rare events.

There is a complementary boundary at the critical modulus.
[[theory/irrationality/L229_critical_modulus_interpolation/_index|L229 bounds the dimension of the corresponding value set]]
when $q_n\ge c\log n$ eventually. Without any bound on the individual
gap changes, the sums over all increasing integer sequences agreeing with
$p_n$ at density one and satisfying the same nested congruences form a
set of Hausdorff dimension zero. The proof counts sparse integer quotients
of gap changes with total variation $O(N)$ up to index $N$, obtaining
arbitrarily small exponential prefix counts on classes with uniform
sparsity bounds, then takes countable unions. Consequently the
interval construction cannot extend to this regime. Dimension zero does
not exclude an individual rational value and gives no new prime-phase
lower bound. Both comparison results concern their stated modulus
regimes; neither settles a sequence of moduli satisfying neither bound.

There is also a limit on further sparsifying an interval construction.
[[theory/irrationality/L230_sparse_interpolation_support/_index|L230 gives dimension zero without congruences]]
if the changed position set has size $o(N/\log\log N)$ up to $N$.
That support bound would suffice to preserve exact blocks of
$O(\log\log N)$ gaps at almost every index start, by counting the
windows touching a changed position. Thus an interval construction
cannot obtain that particular support guarantee. This does not rule out
preserving the distribution of blocks by a different construction, nor
does it exclude an individual rational target. L228 does attain
$|D\cap[1,N]|=O(N/\log\log N)$ whenever the preserved moduli are
$O((\log n)^\alpha)$ for some fixed $\alpha<1$, so its achievable
big-oh support bound cannot be replaced by little-oh for this method.

## A dichotomy that does not depend on the denominator

Fix $K\ge1$ and let $R_K=\prod_{0\le j<K}\mathbb Z/2^{j+1}\mathbb Z$. For
$n\in I_X$ let $r(n)=(h_{n+j}\bmod 2^{j+1})_{0\le j<K}\in R_K$, and let
$\mu_{X,K}$ be the law of $r(n)$ for $n$ uniform in $I_X$. For $0\le j<K$ let
$\tau_j:R_K\to R_K$ add $2^j$ to the coordinate of index $j$; it is an
involution. For a probability measure $\mu$ on $R_K$ put

$$
\delta_j(\mu)=\frac12\sum_{r\in R_K}\bigl|\mu(r)-\mu(\tau_jr)\bigr|,
$$

the total variation distance between $\mu$ and its image under $\tau_j$. For
$j=0$ this is $\delta_0(\mu)=\sum_{r'}|\mu(0,r')-\mu(1,r')|$, summed over the
remaining coordinates $r'$, and the best prediction of the parity of $h_n$
from the residues of the next $K-1$ gaps is correct with frequency
$(1+\delta_0(\mu_{X,K}))/2$. The phase is a function on $R_K$,
$\varphi(r)=\{d\sum_jr_j2^{-j-1}\}$, and $E_d=\{r:\varphi(r)<1/2\}$ is the set
of residue patterns on which the rule (P) fails.

**Lemma E (balance).** For every odd $d$ and every $0\le j<K$,
$\tau_j(E_d)=R_K\setminus E_d$. Consequently
$|2\mu(E_d)-1|\le\delta_j(\mu)$ for every probability measure $\mu$ on $R_K$.

*Proof.* $\varphi(\tau_jr)=\{\varphi(r)+d2^j2^{-j-1}\}=\{\varphi(r)+1/2\}$,
since $d$ is odd; so $\varphi(r)<1/2$ exactly when $\varphi(\tau_jr)\ge1/2$.
Hence $\mu(\tau_jE_d)=\mu(R_K\setminus E_d)=1-\mu(E_d)$, and
$|\mu(A)-\mu(\tau_jA)|\le\delta_j(\mu)$ for every set $A$. $\square$

**Theorem F (prediction dichotomy).**

1. If $S=a/(2^sd)$ with $d$ odd, then for every $\varepsilon>0$, every
   $X\ge\max(X_0(\varepsilon),5)$ with $\pi(X)\ge s+2$, every
   $1\le K\le X/(\log X)^2$ and every $0\le j<K$,
   $\delta_j(\mu_{X,K})\ge1-2(1+\varepsilon)dX/(2^KN_X)$. In particular, for
   fixed $A>1$ and $K=\lceil A\log_2\log X\rceil$,
   $\delta_0(\mu_{X,K})\to1$: the parity of $h_n$ becomes asymptotically a
   function of the residues of the next $K-1$ gaps, and the rule
   $\beta_{n,K}$ is such a function.
2. Conversely, let $\eta>0$, and let $K_X$ be block lengths with
   $2^{K_X}/\log X\to\infty$ and $K_X\le X/(\log X)^2$; for instance
   $K_X=\lceil A\log_2\log X\rceil$ with $A>1$, or
   $K_X=\lceil\log_2\log X+\sqrt{\log_2\log X}\rceil$. If
   $\delta_j(\mu_{X,K_X})\le1-\eta$ for arbitrarily large $X$ and some
   $j<K_X$, which may depend on $X$, then $S$ is irrational.

*Proof.* Part 1: by part 2 of Theorem C and (P),
$\mu_{X,K}(E_d)\le(1+\varepsilon)dX/(2^KN_X)$, and Lemma E gives
$\delta_j\ge1-2\mu_{X,K}(E_d)$. For $K=\lceil A\log_2\log X\rceil$ one has
$2^K\ge(\log X)^A$ and $N_X\sim X/\log X$, so the bound tends to $1$. Part 2:
for each odd $d$ and each such $X$, Lemma E gives
$\mu_{X,K_X}(E_d)\ge\eta/2$, that is, at least $\eta N_X/2$ mispredicted
starts. Since $N_X>X/(2\log X)$ and $2^{K_X}/\log X\to\infty$, this exceeds
$2dX/2^{K_X}$ for large $X$. So $(C_d)$ holds along arbitrarily large $X$ for
every odd $d$, and Corollary D applies. $\square$

The hypothesis of part 2 is a single statement about consecutive prime gaps,
free of $d$: the joint law of the residues $h_{n+j}\bmod2^{j+1}$ is not
nearly singular to its translate in one coordinate. It also implies the
constant-excess version CPS($d$) for every fixed $d$. Here the possibly
varying coordinate needs attention. With $A_j=\{r:r_j<2^j\}$, Markov's
inequality and $h_{n+j}\le2H_{n+j}$ give, for large $X$,

$$
\delta_j\ge1-2\Pr(h_{n+j}\ge2^j),\qquad
\delta_j\le1-\eta\ \Longrightarrow\ 2^j\le8\log X/\eta,
$$

using (T) with $\varepsilon=1$ and $N_X>X/(2\log X)$. Choose a constant
$C\ge3$ with $2^C>16/\eta$. Eventually
$K'=\lceil\log_2(d\log X)\rceil+C\le K_X$ and $j<K'$. Projection to the
first $K'$ coordinates cannot increase $\delta_j$, so Lemma E gives at
least $\eta N_X/2\ge2^{2-C}N_X$ mispredicted starts at length $K'$. This
is CPS($d$). Thus part 2 is a stronger sufficient hypothesis, uniform in
$d$; no converse is proved.

It is not obviously comparable with the hypotheses of the conditional claims.
Ringer's positive comparison, as the truncation sketch records it, bounds the
counts of the first $L$ consecutive offsets above by a fixed multiple $c$ of
model counts, at a length $L$ for which $2^L/\log X\to\infty$. Such upper
domination rules out the concentration of Theorem C directly, because a model
gives the phases just below $1$ little mass. If the model law of residue
patterns is invariant under $\tau_j$ up to $o(1)$, upper domination also gives
$\delta_j\le c/2+o(1)$: for every set $A$ of patterns,
$\mu(A)-\mu(\tau_jA)\le\mu(A\setminus\tau_jA)$, and $A\setminus\tau_jA$ has
model mass at most $1/2$. That bound is informative only when $c<2$, and
non-singularity gives no upper domination, so neither hypothesis visibly
implies the other. Three remarks limit the use of part 2.

- $\delta_j(\mu_{X,K})$ is nondecreasing in $K$, since forgetting the last
  coordinate commutes with $\tau_j$ and cannot increase a total variation
  distance. Thus the overlap bound in part 2 at length $K$ implies the same
  bound at length $j+1$. For $j=0$ this necessary marginal condition is
  $|\Pr(h_n\text{ even})-\Pr(h_n\text{ odd})|\le1-\eta$, which needs a
  positive proportion of $n$ with $p_n\not\equiv p_{n+1}\pmod 4$, a statement
  the obstruction record lists as not known.
- For $2^j$ much larger than $\log X$ the conclusion of part 1 holds for any
  sequence of gaps with mean $\log X$: if $A_j$ is the set of patterns with
  $r_j<2^j$, then $\tau_jA_j$ consists of patterns with $r_j\ge2^j$.
  Such a pattern requires $h_{n+j}\ge2^j$, so
  $\delta_j\ge\mu(A_j)-\mu(\tau_jA_j)\ge1-2\Pr(h_{n+j}\ge2^j)$, which is
  $1-O(\log X/2^j)$ by Markov's inequality. The informative instances are the
  small $j$.
- For $j=0$, $(-1)^{h_n}=\chi_4(p_n)\chi_4(p_{n+1})$, with $\chi_4$ the
  nontrivial character modulo $4$. Part 1 therefore says that a rational $S$
  would make the product $\chi_4(p_n)\chi_4(p_{n+1})$ asymptotically a
  function of the next $\lceil A\log_2\log X\rceil-1$ gap residues.

## The pointwise form

**Proposition G (exact prediction at every large index).** Suppose
$S=a/(2^sd)$ with $d$ odd, and put
$J_m=\lceil0.525\log_2p_m+\log_2d\rceil+3$. There is $m_1(d)$ such that
$h_m\equiv\beta_{m,J_m}\pmod 2$ for every $m\ge\max(s+2,m_1(d))$.
Consequently, if $h_m\not\equiv\beta_{m,J_m}\pmod2$ for infinitely many $m$,
then $S\ne a/(2^sd)$ for every $a$ and $s$.

*Proof.* By
[[../library/primes/baker_2001_difference_between_consecutive_primes/theorem_1|the Baker–Harman–Pintz theorem, in the gap form derived on its library page]],
$g_k\le2p_k^{0.525}$, so $h_k\le p_k^{0.525}$, for all large $k$. Let $m$ be
large and $J\le m$. For $0\le i<m$ the index $m+J+i$ is below $3m$, and
$p_{3m}\le4p_m$ for large $m$ by the prime number theorem, so these terms of
$H_{m+J}=\sum_{i\ge0}h_{m+J+i}2^{-i-1}$ contribute at most
$(4p_m)^{0.525}<2.08p_m^{0.525}$. For $i\ge m$ we use $h_k\le p_k\le k^2$ for
large $k$ and $m+J+i\le3i$, so these terms contribute at most
$\sum_{i\ge m}9i^22^{-i-1}$, which tends to $0$. Hence
$H_{m+J}\le2.1p_m^{0.525}$ for large $m$. With $J=J_m$ (and $J_m\le m$ for
large $m$) one has $2^{J_m}\ge8dp_m^{0.525}$, so
$d2^{-J_m}H_{m+J_m}<1/2$. For $m\ge s+2$, Lemma B gives
$\varphi_{m,J_m}>1/2$, and (P) gives the congruence. $\square$

Without a better pointwise bound for gaps, fewer gaps cannot decide the same
question at one index: obstruction O3 shows that when
$2^J\le p_{m+J}^{0.525}$, the first $J$ gaps after $m$ are consistent, under
the same gap bound, with a continuation whose tails all lie on the lattice.
Under Cramér's conjecture $g_k\ll(\log p_k)^2$ the same proof works with
$J_m=2\log_2\log p_m+O_d(1)$, which is again of critical order.

## How the pieces compose, and what is held

The proposed contradiction uses an upper bound for one event, not a
complete distribution law for the primes. Each step names its support;
step 5 is the open one. Constants in that step may depend on the fixed
odd denominator part $d$.

1. Suppose $S=a/(2^sd)$ in lowest terms, with $d$ odd and $d=1$ allowed.
2. By the digit lemma and Lemma A, $dH_n\in\mathbb Z$ for every
   $n\ge\max(s+2,3)$. For $c_n=dH_n$ the exact recurrence is
   $c_{n+1}=2c_n-dh_n$, with $c_n$ a positive integer.
3. Take $K=\lceil A\log_2\log X\rceil$ for a constant $A>1$ to be
   specified, $M=2^K$, $R=\lfloor4d\log X\rfloor$ and
   $D=\lfloor16K\log X\rfloor$. Put
   $U_{n,K}=\sum_{j<K}2^{K-1-j}h_{n+j}$ and let $r_d(u)$ be the least
   positive residue of $-du$ modulo $M$, so residue zero means $M$.
   Iterating the recurrence gives $c_{n+K}+dU_{n,K}=Mc_n$. Hence
   $c_{n+K}\le R<M$ forces $r_d(U_{n,K})\le R$.
4. By (T), at most $(1/8+o(1))N_X$ starts have $c_{n+K}>R$.
   Telescoping and the prime number theorem give
   $\sum_{n\in I_X}(p_{n+K}-p_n)=(1+o(1))KX$, so at most
   $(1/16+o(1))N_X$ have span above $D$. Therefore the count
   $B_d(X;K)$ of starts with both span at most $D$ and
   $r_d(U_{n,K})\le R$ is at least $(13/16-o(1))N_X$. This is the
   proof of Proposition U3 at the parameters of Theorem U8.
5. **Gap: the prime-block upper estimate.** Prove, for some
   $\varepsilon_d>0$, along arbitrarily large $X$, that
   $B_d(X;K)\le(13/16-\varepsilon_d)N_X$.
   One sufficient stronger estimate, for constants $C>0$, $1\le c<2$
   and $A>1/\log_2(2/c)$, is
   $B_d(X;K)/N_X\le Cc^K R/2^K+o(1)$.
   The right side tends to zero because
   $(c/2)^K\log X\le(\log X)^{1-A\log_2(2/c)}\to0$.
   This bound is unknown for the actual primes, even for $d=1$.
   The independent geometric reference satisfies the phase bound
   $(1+o(1))R/2^K$ by Lemma U6; Lemma U9 gives the same bound after
   excluding small odd prime divisors. Neither calculation transfers
   it to the primes. Condition (GC) is one sufficient transfer statement.
   By Lemma U10 the same count for the integers with no prime factor up
   to $X^{1/2-1/K^2}$ differs from $B_d(X;K)$ by $O(N_X/K)$, so step 5
   may equally be posed for those survivors. Lemma U11 and Proposition
   U12 display its unestimated base term and signed correction at
   lower cutoffs. Proposition U15 instead starts with the periodic set
   of odd integers avoiding one fixed prime $q$, chosen so that
   $2^{q-1}-1>d$. Its count is zero for large $X$. Deleting its
   composites in increasing order gives $B_d(X;K)=\sum\Phi(m)$
   exactly. The weight $\Phi(m)$ is defined there from the preceding
   $K$ actual primes and the unchanged periodic continuation. Bound
   (PD*), $\sum\Phi(m)\le3N_X/4$, is another precise form of this
   open step. For $A>2$, Lemma U16 bounds every weight above by a
   constant $C_{d,q}$, whatever the preceding primes, and Corollary U17
   then bounds the part from composites with two prime factors above
   $X^{\alpha_{d,q}}$ by $(1/4+o(1))N_X$, using the prime number theorem.
   The remaining part (SF), needed with coefficient $9/16-\varepsilon_d$,
   equals $B_d(X;K)$ minus that part; it is a form of this step, not a
   weaker one. No estimate for it is proved.
   Lemma U13 and Proposition U14 obstruct fixed nonnegative tuple
   majorants valid on every finite set at the span in step 3: their
   reference mass is nearly one. This conclusion does not cover all
   upper-bound methods or all arithmetic majorants.
6. Steps 4 and 5 contradict each other. This excludes the fixed $d$ and
   every preperiod $s$, because the scales can be taken past it. Proving
   step 5 for every odd $d$ proves $S\notin\mathbb Q$.

**Shorter-span variant of steps 3--5.** The
[[research/prime_binary_new_attack/short_span_sieve|monotone upper-event
construction]] keeps steps 1--2, takes $K=\lceil12\log_2\log X\rceil$
and the same $M,R$, and changes the span to
$D_*=\lfloor(6/5)K\log X\rfloor$. Rationality then forces
$B_d^*(X)\ge(1/24-o(1))N_X$, by Proposition S1. Enlarge this event to
the existence of any compatible $K$-subset in that shorter interval,
counting each root once. The resulting count $\mathcal C_d$ is monotone
in the set of sites. For the actual survivors
$T_z=\{m\in(X,2X+D_*]:P^-(m)>X^{1/2-1/K^2}\}$, this gives
$B_d^*(X)\le\mathcal C_d(\mathbb P_X)\le\mathcal C_d(T_z)$.
An upper bound $\mathcal C_d(T_z)\le N_X/48$ along arbitrarily large
$X$, for every fixed odd $d$, would contradict the lower bound and
finish step 6. This is the unproved estimate (MS).
More generally, Proposition S22 of the same note needs only
$\mathcal C_d(\mathbb P_X)\le(1/24-\varepsilon_d)N_X$ on unbounded
scales, for some $\varepsilon_d>0$ for each fixed odd $d$. The concrete
target $N_X/32$ leaves a margin $N_X/96$ against the forced lower count.
It is a weaker sufficient target than (MS), not a proof of its numerical
bound $N_X/48$. It may be sought under rationality, provided the upper
argument actually uses that assumption. No estimate of this strength is
proved here.
Consecutiveness is retained in the forced lower count, and the upper
enlargement and changed span are explicit. The model probability of
this monotone event tends to zero, unlike the larger-span event of U14;
the untruncated number of its certificates still has divergent model
expectation. The construction separates (MS) into an excessive local
survivor count and a truncated compatible-subset count, neither proved.
The first cost would follow from the centered survivor moment (VM), but
Proposition S4 shows that (VM) implies a law of large numbers for sums of
about $(6/5)K$ consecutive gaps after almost every prime, (S12), for
which no proof is known here, even under the Riemann hypothesis. The
[[research/prime_binary_new_attack/survivor_moments|survivor-moment
calculation]] removes the rough composites: they change (VM) by only
$O(N_X)$ and change either bounded local event by $O(N_X/K)$.
Thus (VM) is equivalent to the prime-rooted estimate (PVM), without
estimating that signed pair/triple combination. Its stopped-sieve base
has order $K^2N_X$ with a positive lower constant, so the Buchstab
transport (S13) must cancel a nonzero contribution to prove (VM).
Lemma S5 shows that the second cost's specified nonnegative polynomial
cutoff majorants are at least the untruncated certificate count. Lemma S6
reduces this cost to the one-sided bound (S16) for a damped signed
statistic of survivor correlations of every order from $K+1$ upward.
The affected-root estimate does not transfer that statistic at the
required precision. No theorem inspected here supplies either missing
bound. A direct upper estimate for the bounded event could replace both.
There is also a sufficient band-loss route to (MS). For sufficiently
large $K$, put $\alpha_i=49/100+8i/K$ and
$T_i=\{m\in(X,2X+D_*]:P^-(m)>X^{\alpha_i}\}$, $0\le i\le8$.
The unweighted semiprime census gives $\mathcal C_d(T_0)<2N_X$.
If, for every fixed odd $d$, all eight losses satisfy
$\mathcal C_d(T_i)-\mathcal C_d(T_{i+1})
\ge\mathcal C_d(T_i)/2-N_X/1024$ on the same unbounded scales,
then iteration gives
$\mathcal C_d(T_z)\le\mathcal C_d(T_8)<5N_X/512<N_X/48$.
These sufficient inequalities are (PB), unproved even for $d=1$.
Proving them would contradict the lower bound $(1/24-o(1))N_X$.
S17 identifies the actual
deletion coefficients; (S19)--(S20) expand them into prime-cofactor
progression sums. The missing estimate concerns the full signed sum,
including its large divisors, and its comparison with
$\mathcal C_d(T_i)/2$. The inspected Bombieri--Vinogradov statements do
not supply that estimate. Proposition S18 says that prime-supported
roots survive every band. It does not refute (PB) or preclude proving
it arithmetically; (PB) implies the prime upper bound needed for the
contradiction.
Proposition S22 also permits one aggregate estimate in place of the eight
individual losses: with $e_i=\mathcal C_{i+1}-\mathcal C_i/2$, the bound
$\sum_{i=0}^7 2^{-(7-i)}e_i\le N_X/64$ gives
$\mathcal C_d(\mathbb P_X)<3N_X/128< N_X/32$. The same sum is exactly
$\mathcal C_8-2^{-8}\mathcal C_0$, so this identity alone estimates
nothing. Under rationality it is at least $(13/384-o(1))N_X$; proving
the upper bound would supply the contradiction. Its arithmetic control
remains unknown.

**Deletion signs under the rationality assumption.** The
[[research/prime_binary_new_attack/rational_deletion_signs|conditional sign
bound]] uses the same carries, positive-residue convention and
increasing-order deletions, with $A>2$. At the enlarged span
$D=\lfloor K(\log X)^2\rfloor$, rationality forces
$B_d(X)\ge(7/8-o(1))N_X$ and makes the total negative deletion mass
$o(N_X)$. The latter statement follows from the common carry inside
each actual prime gap, the lattice separation and (T); it is not an
unconditional sign bound for arbitrary prefixes. An upper bound
$(7/8-\varepsilon_d)N_X$ for the positive deletion mass on unbounded
scales, for every fixed odd $d$, would therefore suffice for step 6.
This is the unproved estimate (D8), which may itself be sought under
rationality. By (D5) and (D7) the positive mass equals $B_d(X)+o(N_X)$
(equation (D16)), so existence of a fixed saving in (D8) is equivalent
to a fixed saving below $7/8$ for $B_d(X)/N_X$, after reducing the
saving if necessary.
Lemma D17 shows that, in a gap with small carry, whether a root's
residue rises is decided by the carries and periodic data at the two
prime endpoints; a full gain also keeps the span cutoff. Proposition
D18 removes the high ranks, the gaps with
large carry and multiple gains at one site, each at cost $o(N_X)$ or an
arbitrarily small multiple of $N_X$, and bounds the gains at sites with
least prime factor above $X^{1/3}$ by $(\log2+o(1))N_X$.
For $\eta=17/24-\log2>0$, take a fixed $T_0$ with
$C_02^{-T_0}<\eta/2$. The sufficient remaining test is
$P_{\rm SF}^{<T_0}(X)\le N_X/6$ for the number of gains at sites
with least factor at most $X^{1/3}$ and rank below $T_0$.
Then the full count is at most
$(\log2+1/6+\eta/2+o(1))N_X=(7/8-\eta/2+o(1))N_X$,
contradicting the lower bound. This test is unknown for every fixed
odd $d$; proving it for $d=1$ alone would not finish step 6.
The exact identity (D16) supplies no such estimate and does not rule
out estimating its parts. Proposition D19 does rule out one specific
relaxation: for ordinary crossings of the unreduced real prime tails,
the same small-factor, low-rank count is at least
$(7/8-\log2-C_02^{-T_0}-o(1))N_X$, unconditionally, hence exceeds
$N_X/6$. The original residue event keeps the origin $Mc_n$ in
(D20); dropping it without using integrality is invalid.
Proposition D21 gives an exact integer rounding rule for each remaining
site. Equation (D22b) retains the good-gap, root, interior-site and span
conditions in one count along the increasing orbit
$\mathcal A_r=dp_r+4c_r$. Divisibility is a finite-period predicate of
that orbit, not of the prime endpoint alone. The artificial two-period
ensemble (D23) has integral tails and uniform endpoint residues modulo
$30$, but $5/16$ of its rank-two selected sites are divisible by $5$.
This refutes a transfer based only on those local data; its endpoints
are not asserted to be primes. It does not refute the actual-prime test
or supply a prime-distribution estimate.
The enlarged span is essential to the stated negligible span loss:
this argument gives no bound for the shorter-span costs (VM) or
$\mathcal Q_{d,z}$.

**Dephased phase-transport variant.** Keep steps 1--2 and fix an odd prime
$q$ with $2^{q-1}-1>d$. On the
[[research/prime_binary_new_attack/phase_transport|phase-transport page]],
$w$ is the half-gap tail of the odd integers avoiding $q$,
$\beta_{d,q}$ is the mean of $e(dw)$ over their $q-1$ residue classes,
and $0<\delta_{d,q}=1-\operatorname{Re}\beta_{d,q}<2$.
The observable $Q_{d,q}(X)$ sums the specified dephased cosine increment
over composites in those classes, using the actual carries $c_r$.
Proposition P4 proves

$$
Q_{d,q}(X)=N_X-\operatorname{Re}\sum_{n\in I_X}
e(dw(p_n)-c_n)+o(N_X).
$$

Since $c_n$ is eventually integral, PNT in the fixed classes forces
$Q_{d,q}(X)=(\delta_{d,q}+o(1))N_X$. The missing step is (FPT): prove
$Q_{d,q}(X)\le(\delta_{d,q}-\varepsilon_d)N_X$ on unbounded scales,
for some $\varepsilon_d>0$ for each fixed odd $d$. An upper proof may
use rationality. This would contradict the forced value beyond any fixed
preperiod and finish step 6. At $d=1,q=3$ the required saving is below
$3N_X/2$; that case alone does not settle all denominators.
The available unconditional bound $Q\le2N_X+o(N_X)$ does not suffice.
The original, undephased transport has a different unconditional endpoint
and the separate sufficient target (UPD). No saving for either sum has
been proved. Without integrality, (FPT) asks for a correlation between
the binary digits of $dS$ and the prime classes modulo $2q$ (Lemma P7);
at $d=7$ it must be positive in the restricted family with $q$ prime and
$2^{q-1}-1>d$ (Proposition P8). That restriction is not needed by the
phase identities. In particular $d=7,q=3$ has reference mean $-1/2$.
Using the prefix coefficient of (P5) under integrality remains an
alternative, with the endpoint of the original transport.

**Resonant-reference contradiction.** Proposition P9 of the phase-transport
page gives the following complete alternative with one arithmetic gap.

1. Suppose $S=a/(2^sd)$ with fixed odd $d$, including $d=1$, and finite
   $s$. Lemma A gives $dH_n\in\mathbb Z_{>0}$ beyond
   $n=\max(s+2,3)$.
2. Write $d=3^\nu d_0$ with $3\nmid d_0$ and choose the fixed integers
   $q=2\cdot3^\nu+1$, $L=2^{q-1}-1$, and $b=d_0L/3$.
   The valuation $v_3(L)=\nu+1$ makes $b$ an odd multiple of $d$, so
   $C_n=bH_n$ is eventually integral. The odd integers avoiding $q$
   contain every prime above $q$, even if $q$ is composite.
3. Their periodic half-gap tails $w$ satisfy
   $\operatorname{Re}e(bw)=-1/2$ at every site. The endpoint identity
   (P9c), with every actual composite site included, therefore gives
   $Q_{b,q}(X)=(3/2+o(1))N_X$ for all sufficiently large $X$.
4. Prove $Q_{b,q}(X)\le(3/2-\varepsilon_d)N_X$ on unbounded scales
   for some $\varepsilon_d>0$, for these fixed $b,q$. **UNKNOWN.**
   The estimate may use rationality. The forced value in step 3 is the
   other side of the proposed contradiction, not an obstruction to that
   use. An unconditional proof would also suffice: by (P9c), up to an
   $o(N_X)$ error, it asks for
   $\operatorname{Re}\sum_{n\in I_X}e(bw(p_n)-C_n)$ at least
   $(-1/2+\varepsilon_d)N_X$. Its exact signed cofactor sum is
   (P6) with multiplier $b$, coefficient
   $e((4C_r+bp_r)/2^{j+1})$, every least-factor exclusion retained, and
   rank cutoff $J=\lceil3\log_2\log X\rceil$. The discarded ranks cost
   $O_b(X2^{-J})=o(N_X)$. No bound for the retained sum is proved.
5. An unbounded sequence of scales in step 4 passes every finite
   preperiod. Steps 3 and 4 then contradict each other. Proving step 4
   for each fixed odd $d$ proves irrationality; uniform constants in $d$
   are unnecessary.

The reference construction is proved at author standing. It removes the
restricted-family sign issue of P8, not the need for an actual-prime
estimate. Joint decorrelation of $e(bw(p_n)-bH_n)$ would suffice and
remains unproved. No equivalence with (D22b), (BC) or (UPD) is asserted.
The [[research/prime_binary_new_attack/harmonic_phase_ceiling|doubled-phase
comparison]] applies to this reference for each fixed $d$. Its optimal
universal ceiling is $3/2$, even for finite signed normalized mixtures.
For the weights $2/3,1/3$, a strict saving is equivalent to a positive
proportion of the explicit square energy in (H5). Under integrality that
energy vanishes and every doubled site weight agrees. Thus averaging
alone supplies no strict saving; an estimate using the actual primes
remains necessary for this comparison.

**Preceding-gap matching contradiction.** The section "The preceding gap and
the reversed constraint" of the
[[research/prime_binary_new_attack/matching_gap_windows|matching-window note]]
gives a complete alternative with one gap and no index class.

1. Suppose $S=a/(2^sd)$ with fixed odd $d$, including $d=1$, and finite
   $s$; put $n_0=\max(s+2,3)$. Lemma A makes $c_n=dH_n$ a positive integer
   for $n\ge n_0$.
2. The recurrence gives, whenever $n-r\ge n_0$, the congruence
   $c_n\equiv-d\sum_{k=1}^r2^{k-1}h_{n-k}\pmod{2^r}$; at $r=1$ the
   parity of $c_n$ records the class of $g_{n-1}$ modulo $4$.
3. With $K=\lceil A\log_2\log X\rceil$, $A>1$, all but $X^{o(1)}$ of
   at least $(3/4-o(1))N_X$ good starts in $I_X$ share their window of $K$
   gaps with another good start, both later $G$-tails being below $2^K/d$
   (repeated-window lemma). Equal good windows give equal carries, so
   step 2 makes their preceding gaps congruent modulo $4$.
4. Produce, for unbounded $X$, two good starts beyond $n_0$ with equal
   windows and preceding gaps in different classes modulo $4$.
   **UNKNOWN.** Graded congruences in place of equality suffice with the
   explicit integer correction of that note.
5. Steps 3 and 4 contradict each other. Doing this for each fixed odd $d$
   proves irrationality.

The reversed form makes the tail constant on each class of graded
congruences of about $A\log_2\log X$ preceding gaps; its step 4 asks for
two starts in one class whose next half-gaps differ by at least the larger
following $H$-tail minus one. Both forms concern consecutive primes across one
index at the critical length. The reduction is author-recorded and outside
the matching-window review.

The [[research/prime_binary_new_attack/prediction_overlap|prediction-overlap
comparison]] gives a quantitative alternative. Let $M_U(X,K)$ count
minority preceding half-gap parities after grouping starts by
$U_K=\sum_{0\le j<K}h_{n+j}2^{-j-1}\bmod2$. Rationality forces
$M_U\le(1+\varepsilon)dX/2^{K+1}$ by paying for the large following
tails. Thus, at $K=\lceil A\log_2\log X\rceil$, $A>1$, the condition
$\limsup_{X\to\infty}2^KM_U/X=\infty$ would exclude every odd $d$.
This coarser feature can have more overlap than exact windows or their
residue vectors; no converse implication is claimed. The required lower
bound is unknown. The comparison's rational nonprime model shows why
repeated windows, prime-number-theorem growth and balanced parity
marginals alone do not supply it. These deductions are author-recorded
and outside the matching-window review.

The alternative lower-count route uses Lemma B to give
$1-\varphi_{n,K}\le d2^{-K}H_{n+K}$. Summing with (T), Theorem C permits
at most $(1+\varepsilon)dX/2^K$ mispredicted starts. CPS($d$), or the
zero-phase subfamily ZPC($d$) with its continuation bound, would give more
starts and hence the same contradiction by Corollary D.

The alternative chain is

$$
\text{CPS}(d)\ \text{or}\ \text{ZPC}(d)\ \text{for every odd }d
\ \Longrightarrow\ (C_d)\ \text{for every odd }d
\ \Longrightarrow\ S\notin\mathbb Q ,
$$

with the hypothesis of part 2 of Theorem F as a single, stronger sufficient
condition. Condition (AC) and Corollary U4 of the upper-count note give
other upper-count alternatives. None of these comparisons with the
actual primes follows from the model computations. Proposition G gives a
pointwise alternative: infinitely many
exceptions to the rule at length $J_m$, for each odd $d$. Under the Riemann
hypothesis, Proposition Z8 of the zero-phase analysis replaces step 5 by a
lower bound for the frequency of zero-phase starts alone, at length
$A\log_2\log X$ with $A>4$.

- **Held links.** The digit lemma, the step lemma, Lemmas A, B and E, the
  rule (P), Theorems C and F, Corollary D and Proposition G are proved on this
  page, author-recorded and not independently reviewed. They use elementary
  algebra and (T); Proposition G also uses the Baker–Harman–Pintz theorem.
  (T) is author-recorded on the truncation sketch and uses only the prime
  number theorem. Lemmas Z1, Z2, Z3, Z5, Z6, Z6b and Z6c and Propositions Z4, Z7 and
  Z8 are proved on the zero-phase page, Z8 from its stated second-moment
  hypothesis. Proposition Z8′ is proved from its explicit large-gap
  count and phase-frequency hypotheses, and Proposition Z9 describes the
  shape of a one-class witness. The unreviewed graded-congruence
  extension of the matching-window note keeps an integral truncation
  difference and the original tail threshold.
  Proposition O8 and Corollary O8, the subcritical residue comparison, are
  proved on the obstruction record, as are the filter accounting of
  Proposition O9 and the exact finite carry calculation of Lemma O10.
  L228 strengthens that comparison using
  the classical prime-pair upper bound; its proof is on the linked claim.
  L229 proves the dimension-zero boundary at logarithmic moduli by a prefix
  count; L230 gives a support boundary without congruence assumptions.
  Propositions U1, U3, U12, U14 and U15, Theorems U2 and U8, Corollaries
  U4 and U17 and Lemmas U5--U7, U9--U11, U13 and U16 are proved on the
  upper-count note. U7
  proves that bounding its signed error by the sum of adverse termwise
  errors fails; U6 and U9 are reference-model calculations only.
  Propositions S1 and S3 and Lemma S2 of the shorter-span note prove
  its rationality lower bound, exact integer-subset census and reference
  rarity. The monotone sieve enlargement and decomposition (S10) are
  exact; neither (MS) nor its two arithmetic costs is proved.
  Proposition S4 proves that (VM) implies the law of large numbers
  (S12), the transport identity (S13) is exact, Lemma S5 proves that
  its specified nonnegative cutoff majorants cannot beat the untruncated certificate
  count, and Lemma S6 proves the damped reduction (S15) of the second
  cost. Lemma S17 proves the exact band-deletion identities, and
  Proposition S18 proves that their sufficient loss bounds (PB) imply
  (MS). Equations (S19)--(S20) give the local polynomial and exact
  semiprime expansion; (S21) shows an order-$N_X$ discrepancy from
  periodic density already for the one-site survivor census. These
  calculations do not estimate the weighted band losses.
  Proposition S22 gives the sufficient fixed-saving prime bound and
  aggregate band-error budget, not an arithmetic estimate for either.
  Lemma M1 and Proposition M2 of the survivor-moment note prove the
  fixed-dimensional sieve and composite-neighborhood bounds. Corollary
  M3 transfers the bounded events and the second moment to the primes;
  Proposition M4 proves the positive lower and upper bounds for the
  stopped base moment. These estimates prove neither (PVM) nor (S16).
  The conditional sign bound (D12) and its span accounting (D7) are
  proved on the deletion-sign page under the rationality assumption;
  their sufficient positive-mass estimate (D8) remains open. The
  identity (D16), the endpoint criterion of Lemma D17 and the
  finite-rank and single-gain bounds of Proposition D18 are proved
  there under the same assumption, using Lemma M1, (M4) and the
  semiprime count of Corollary U17. Proposition D19 proves an
  unconditional lower bound for the distinct ordinary-crossing
  relaxation, using the same pair bound, semiprime census and (T).
  Equation (D20) identifies the phase omitted by that relaxation.
  Proposition D21 and (D22) give the exact selected-site locator and
  actual-carry count; the artificial ensemble (D23) refutes only the
  stated single-endpoint-marginal shortcut, without prime hypotheses.
  Propositions P1 and P2 and Lemma P3 of the phase-transport note prove
  the original increment, the prime-gap endpoint form and the digit-change
  equivalence for the unweighted phase deficit. Proposition P4 gives the
  distinct endpoint of the dephased sum $Q$. Its partial boundary gaps
  telescope as well, leaving $O_{d,q}(\log X)$ error without a short-gap
  theorem. It proves
  $Q\le2N_X+o(N_X)$, which is insufficient for its fixed-saving target.
  Lemma P7 restates the unconditional form of (FPT) as a correlation of
  the digits of $dS$ with the prime classes, and Proposition P8 computes
  $\operatorname{Re}\beta_{7,q}\ge0$ for primes $q\ge5$. Proposition P9
  chooses an odd multiple of every denominator and a periodic reference
  with constant real phase $-1/2$, giving the common rationality endpoint
  $3N_X/2+o(N_X)$. Its proof and the frequency and shift comparisons
  (P9e)--(P9f) are author-recorded. The strict upper bound (RFPT) is not
  proved.
  Proposition D24 of the deletion-sign note rejects bounded-potential
  certificates with nonnegative pair costs by an exact stationary
  calculation at $d=1$, and the repeated-window lemma of the
  matching-window note proves, by pigeonhole and (T), that equal windows
  with small later tails occur at all but $X^{o(1)}$ good starts. Its
  preceding-gap congruence (8) and reversed constraint (9) prove, for
  every odd $d$ under rationality, that such windows have preceding gaps
  in one class modulo $4$ and that graded congruences of the preceding
  gaps fix the tail.
  None of these identities proves (FPT), (UPD) or a block-count estimate.
  These arguments are all author-recorded.
- **Provisional premises.** The stated sufficient prime-block estimates
  are unproved hypotheses, not held facts. Theorems U2 and U8 prove
  implications from them. Proposition Z8 similarly proves an implication
  from a second-moment bound, which is known under the Riemann hypothesis.
  Z8′ uses its stated large-gap count and the separate, unproved
  zero-phase frequency; neither hypothesis follows from the tail cutoff.
- **Gap.** The prime-block upper estimate in step 5, or one of the stated
  alternatives. It is open for every $d$, including $d=1$; the supporting
  pages state what the examined substitutions supply and where each stops.

## Failure log

Each entry names the failing step, the missing input, its status for the
actual primes, and the condition for reopening. "Unknown" means neither proved
nor disproved; a mechanism shown not to deliver the input is marked as such,
with its scope.

- **Step 5 by a positive proportion (CPS($d$)).** Missing: a lower bound for
  mispredicted starts at length $\log_2(d\log X)+C$. Unknown for every $d$; it
  holds in the independent model by Lemma E, and the finite check finds
  proportions near $1/2$. Reopens with any positive-proportion statement on
  the joint residues of $\log_2\log X+O(1)$ consecutive gaps.
- **Step 5 by zero phases (ZPC($d$)).** Missing: zero-phase starts at moduli
  $2^K$ of order $\log X$, with frequency of order $2^{-K}$ and continuations
  of positive conditional frequency. Unknown. Requiring every selected
  subtuple to work at its first root fails under the size assumptions of
  Lemma Z6. Lemma Z6b also allows an adaptive root, prefix and continuation
  inside the selected block, when $k>(m-1)2^{m-1}$; this includes the
  explicit sufficient tuple size quoted in the consecutive-subtuple
  theorem. Lemma Z6c gives unhelpful representatives of prescribed groups:
  a sufficiently large group allows representatives with every selected
  half-gap at least $2^m$. It also treats interleaved groups, with a
  larger size threshold. This includes the group sizes in the inspected
  proof of Banks--Freiberg--Maynard's Theorem 4.3. These lemmas do not
  exclude a theorem selecting favorable representatives.
  The lower counts proved by the
  dense-cluster, bounded-gap and congruent-string theorems fail its count
  inequality before any question of where the selected primes fall
  (Proposition Z7). Reopens with a lower bound of order $2^{-K}N_X$ for
  zero-phase starts with conditional control of the next
  $\log_2\log X+O_d(1)$ gaps, or with any family meeting (Z4) at its own
  certified length.
- **Step 5 by a prime-block upper estimate (U8).** Missing: the bound
  $B_d(X;K)/N_X\le Cc^K R/2^K+o(1)$ at the stated length, with $c<2$,
  or more generally (GC). Unknown for every $d$, including $d=1$.
  Kuperberg's examined tuple upper bound permits the length but loses
  $(2+\varepsilon)^kk!$, with $k=K+1$, and drops consecutiveness.
  A loss need not stay bounded: every $c<2$ suffices after increasing
  $A$. Reopens with a direct bound for the phase event, or an upper
  comparison meeting $F_X\log X/2^K\to0$. The periodic reference U9
  handles small odd-prime exclusions but supplies no transfer theorem.
  Every nonnegative combination of tuple indicators that majorizes the
  event for all sets has reference mass $1-O(e^{-K/6})$ (Lemma U13 and
  Proposition U14, proved): it counts every root with some compatible
  $K$-set among its later primes. Within this specified class and span,
  a successful bound requires a deficit of prime tuple counts relative
  to the reference in aggregate, which the Hardy–Littlewood heuristics
  do not predict. Signed or arithmetic-specific majorants and other
  spans are not excluded by this result.
- **Step 5 through a sieve on survivors (U10--U12).** The survivor count
  at the level $X^{1/2-1/K^2}$ is equivalent to $B_d(X;K)$ up to
  $O(N_X/K)$, proved; it is not easier. Stopping the sieve at $X^{2/5}$
  or at $X^{1/s}$ gives an exact identity whose base term is the same
  kind of count and whose correction is a signed sum over at least
  $(\log(3/2)+o(1))N_X$, respectively $(\log(s-1)-o(1))N_X$, deletions of
  size up to $K+1$. Each term depends on the survivors within $D$ of a
  semiprime in (BD); the other cutoff also leaves composites with more
  factors. No bilinear estimate for these coefficients is supplied by
  the inspected sources. The correction needs better accounting than
  the bound $K+1$ per deletion; cancellation is one possibility, not
  a proved necessity for every method. Unknown. Rooting the
  block at every integer, through $F(x)\equiv2^{\pi(x)}S\pmod1$, needs
  gap-weighted sums of order $X\log X$ that are not known either.
- **Step 5 through increasing-order deletions (U15).** The periodic
  starting count is zero and (PD) is exact. Missing: (PD*) for the
  weights depending on the preceding $K$ actual primes. Unknown for
  every odd $d$. The least-prime-factor sum (PF) locates the arithmetic
  input; its range with two prime factors is a first concrete test, not
  a reduction of the other ranges. Both positive and negative weights
  occur. The zero base count removes one obligation in (BD), but does
  not supply the upper bound. In the $K$th-successor term, formula
  (PE) gives at most $6d$ classes modulo $2^{K+1}$ whose translations
  depend on the preceding primes. Counting by interval length leaves
  an additive $O_d(N_X)$ term without a constant saving. For $A>2$ the
  weights are bounded above by a constant (Lemma U16), so the
  composites with two prime factors above $X^{\alpha_{d,q}}$ cost at most
  $(1/4+o(1))N_X$ (Corollary U17); both are proved. The remaining sum
  (SF) over composites with a smaller least factor is
  $B_d(X;K)$ minus that part, identically, and summing by parts inside
  the prime gaps restates the identity. Its part at sites divisible by
  a fixed small prime $\ell$ needs the residue of $p_r$ modulo $\ell$
  jointly with the preceding gaps; such estimates for every class would
  estimate $B_d(X;K)$. This decomposition supplies no saving. Unknown.
  Reopens with an estimate for consecutive primes jointly with the
  weighted block sum, or with a starting set or deletion order whose
  remaining weights a known theorem controls.
- **Step 5 from conditional deletion signs (D8).** Under rationality,
  downward residue transitions are negligible by (D12). At the
  enlarged span $K(\log X)^2$, span losses are negligible as well.
  Missing: the upper bound for positive deletion mass in (D8), unknown
  for every odd $d$, including $d=1$. By (D16) this mass is
  $B_d(X)+o(N_X)$, so (D8) is a reformulation of a direct count bound,
  with a smaller positive saving if needed. The gap-by-gap potentials telescope to
  $B_d(X)$ by (D14)--(D15). Proposition D18 proves that gains at ranks
  $t\ge T_0$ cost at most $C_02^{-T_0}N_X+o(N_X)$, that gaps with large
  carry and multiple gains at one site are negligible, and that sites
  with least prime factor above $X^{1/3}$ carry at most
  $(\log2+o(1))N_X$ gains. The remaining small-factor, low-rank target
  $P_{\rm SF}^{<T_0}\le N_X/6$ is unknown. It implies
  $B_d(X)\le(7/8-\eta/2+o(1))N_X$ with $\eta=17/24-\log2$, and is
  stronger than that bound, because the least-factor split counts rough
  sites rather than their gains. Lemma D17 is an endpoint criterion,
  not an independence theorem for those sites and carries. Neither
  it nor the telescoping identity rules out a least-factor estimate.
  The attempted relaxation to unreduced real-tail crossings does fail:
  D19 gives that relaxed low-rank, small-factor count a lower bound
  strictly above $N_X/6$ for the chosen cutoff, without rationality.
  Its missing phase origin is $Mc_n$ in (D20). The exact rounding
  rule (D21) makes divisibility periodic in $\mathcal A_r$, but does
  not estimate its joint distribution with the actual prime gap and
  the flags in (D22b). The attempted replacement by uniform endpoint
  classes fails even for positive integer tails: (D23) has uniform
  endpoint classes modulo $30$ and $5/16$ of its selected sites divisible
  by $5$. This artificial model has no actual-prime or correlation
  warrant. Reopens with a bound
  using the integer carry condition in the actual weighted arithmetic
  sum, or a direct bound for $B_d(X)$; the continuous surrogate cannot
  supply the proposed upper bound. A certificate for the low-rank gains
  by a bounded potential in the carry and a fixed-wheel class, with
  nonnegative prime-pair costs paid by the constant-$8$ pair bound,
  fails already at $d=1$: Proposition D24 builds stationary integer
  transitions on which every such certificate has cost
  $(\kappa_X+o(1))N_X$ with $\liminf\kappa_X\ge1$, above the $7/8$
  budget. This rejects only that pointwise enlargement
  with positive costs; certificates keeping the root and span flags,
  signed costs or further prime correlations are not excluded.
- **Step 5 by phase transport over prime roots (FPT).** For the original
  increments, Propositions P1--P2 of the
  [[research/prime_binary_new_attack/phase_transport|phase-transport note]]
  give a prime-prefix formula and a gap-endpoint telescope. A fixed saving
  for their total is the unweighted phase-deficit bound (UPD), equivalent
  to a positive proportion of binary digit changes of $dS$ by Lemma P3.
  The dephased sum $Q$ instead multiplies each root increment by
  $e(-c_n)$. Its unconditional endpoint is
  $N_X-\operatorname{Re}\sum e(dw(p_n)-c_n)+o(N_X)$, by Proposition P4.
  After the stated boundary errors, the two sums agree under integer carries.
  Replacing the carry coefficient through (P5) without that hypothesis
  changes the observable. Equating
  their unconditional endpoints is invalid. Missing: a fixed saving
  $Q\le(\delta_{d,q}-\varepsilon_d)N_X$, possibly proved under
  rationality, for each fixed odd $d$. Unknown, including $d=1$.
  The displayed Fourier norm is bounded, but the coefficients depend on
  the actual prime gaps; partial summation with the bound $2N_X+O(1)$
  for their variation does not give an error $o(N_X)$. The pointwise
  shortcut $T_{1,3}(B,w)\le2$ is false already at $B=3,w=4/3$.
  The inspected rough-number theorem places some rough site in almost
  every gap, without controlling these signed carry-selected weights.
  Reopens with the signed cofactor estimate (P6) at the needed saving,
  or another proof of (FPT). The endpoint identities do not retire
  rationality-dependent estimates, least-factor methods, or the other
  block-count routes. The unconditional form of (FPT) is a lower bound
  for the correlation between the binary digits of $dS$ and the classes
  of $p_n$ modulo $2q$ (Lemma P7), and at $d=7$ every prime $q$ with
  $2^{q-1}-1>7$ has $\operatorname{Re}\beta_{7,q}\ge0$
  (Proposition P8, proved). An unconditional (FPT) in that restricted
  reference family requires a positive-proportion excess above the
  reference mean $\operatorname{Re}\beta_{7,q}N_X$. This excess is absent
  both under rationality and under joint equidistribution of
  $7\cdot2^nS$ modulo one with the prime classes. That equidistribution
  is a heuristic, not proved; (FPT) is not disproved. This is not an
  obstruction to all dephased references: $d=7,q=3$ gives $-1/2$, and
  P9 constructs a reference with constant real phase $-1/2$ after an
  odd multiplier for every denominator. The proof of P4 does not need
  $L>d$ or primality of $q$; the reference average used in P0 cannot be
  carried to a composite $q$ without justification. P9 uses its constant
  real phase instead, so needs no such progression average.
- **Step 4 of the resonant-reference contradiction (RFPT).** Missing:
  a strict saving below $3N_X/2$ in (P6) with the parameters (P9a), all
  least-factor and rank conditions retained. Unknown for every fixed
  odd denominator, including $1$. The constant reference phase and the
  forced rationality endpoint are proved; they do not give a saving.
  Multiplying the frequency by $2^u$ makes the first $u$ real rank
  increments vanish under integer carries, but leaves exactly the old
  site weight at the shifted ranks (P9e). Keeping the old truncation
  error after this multiplication is invalid: it grows by $2^u$.
  The attempted transfer from the prime-factor-series argument does not
  supply a prime-gap dilation law or a multiplicative representation of
  the carry coefficient. Its more general decoupling inequality permits
  bounded functions, but the direct comparison across its shifts costs
  $O(uN_X)$ by (P9f), with no adequate small-rank saving. These failures
  concern the stated transfers, not every use of those methods.
  The examined signed-boundary exchange gives an identity, not the
  required saving. At each rank $j$ the sites of a complete gap
  telescope, as in the proof of P4, so with
  $A_j=\sum_{r\in I_X}\cos(2\pi(C_r-bw(p_r))/2^j)$ the rank-$j$ part of
  (P6) is $A_j-A_{j-1}$ up to $O(1)$, and (P6) is
  $A_J-A_0+O_b(\log X)$. Unconditionally $A_J=N_X-o(N_X)$ at
  $J=\lceil3\log_2\log X\rceil$, by (T). A split of the sites by least
  prime factor, or an exchange of sums along the prime crossings,
  separates terms whose cancellation is exact over each whole gap. This
  identity gives no estimate for an individual part. Under integer carries
  $C_r$ is congruent
  to $-b\sum_{k\le j}2^{k-1}h_{r-k}$ modulo $2^j$, so each $A_j$ is a
  statistic of the $j$ preceding half-gaps and of $p_r$ modulo $2q$;
  rationality fixes $A_0=-N_X/2$. The missing input is a strict bound for
  the actual signed sum; a proof may use these integer-carry constraints.
  An unconditional proof is equivalently an endpoint-correlation bound
  via (P9c). Neither form is proved.

  The short-shift calculation (P9g)--(P9i) retains all signed crossings
  and pays $O_b(u^2X/(\log X)^2)=o(N_X)$ for multiple crossings when
  $u=o(\sqrt{\log X})$. It leaves the single-crossing arithmetic kernel
  unestimated. At that shift range, the stated interval-norm estimate in
  Tao--Teräväinen v2, Theorem 3.3, supplies at most a fixed power of
  $\log\log X$ as a saving against $X$, insufficient for an $o(N_X)$
  error. Its arbitrary bounded-function hypothesis is not the obstacle.
  This rejects the direct plug-in, not a stronger sparse-support estimate
  or a treatment of larger shifts retaining multiple crossings. Reopens
  with a proved strict upper bound for the actual signed sum, possibly
  using integrality, or with a different complete contradiction.

- **Step 5 in a shorter span (MS).** Missing: the monotone upper count
  $\mathcal C_d(T_z)\le N_X/48$ at the parameters of the
  [[research/prime_binary_new_attack/short_span_sieve|shorter-span note]].
  Unknown for every odd $d$. The weaker bounded-event target (BC) of
  Proposition S22, with any fixed saving below $1/24$, is unknown too;
  $N_X/32$ would suffice without proving the numerical version of (MS).
  The rationality lower bound $N_X/24-o(N_X)$ and
  the monotone enlargement to actual survivors are proved. The reference event
  is rare; this is not an arithmetic comparison. Dropping saturation and
  counting all compatible subsets still fails in the reference, by (S9). The
  first cost was tested through (VM), a centered second moment at survivor
  roots. (VM) is unknown; Proposition S4 proves that it implies (S12), a law of
  large numbers for sums of about $(6/5)K\asymp\log\log X$ consecutive gaps
  after almost every prime, for which no proof is known here, even under the
  Riemann hypothesis: the Selberg mean-square bound needs intervals longer than
  $(\log X)^2$, and the known averaged pair-correlation theorem needs shift
  ranges a power of $X$. Kuperberg's inspected uncentered tail bound requires a
  threshold-to-mean ratio tending to infinity; this test has ratio $25/24$ and
  a different root convention. The survivor-moment calculation proves that
  (VM) differs from the prime-rooted moment (PVM) by $O(N_X)$; composites
  also change the bounded event by only $O(N_X/K)$. These comparisons
  remove that contamination but leave (PVM) unproved. The signed Buchstab
  transport (S13) has a base of order $K^2N_X$, with positive lower
  coefficient $\lambda^2\log(3/2)^3/3+o(1)$, and an unestimated signed
  correction weighted by short-shift correlations. The second cost
  $\mathcal Q_{d,z}$ is unknown. The nonnegative polynomial cutoff
  majorants of Lemma S5 are at least the untruncated count, and the
  damped reduction (S15) leaves the one-sided bound (S16) for
  signed survivor correlations of every order from $K+1$ to $J+1$, with a
  saving of about $(\log X)^{10.8}$ over the trivial bound. An
  $O(N_X/K)$ affected-root bound does not suffice for this weighted sum.
  Both missing inputs remain unknown, rather than refuted or supplied
  by the comparison. Reopens with cancellation for (S16), together with
  (PVM), (S12) or another sufficient bound for $\mathcal D_z$, or with a
  direct estimate for the bounded event. No equivalence to the original
  consecutive-block upper count is claimed.
- **Step 5 by band deletion losses (PB).** Lower the sieve level to
  $X^{49/100}$ and ask each of eight bands of deleted semiprimes to destroy
  half of the counted roots, up to $N_X/1024$. The exact band losses
  (Lemma S17 of the shorter-span note) and the composition are proved;
  (PB) would finish the contradiction. Missing: (PB) itself, unknown for
  every odd $d$, including $d=1$. Deleting composites never removes a
  prime root certified by primes alone, and (PB) implies
  $\mathcal C_d(\mathbb P_X)<5N_X/512$ (Proposition S18, proved).
  This is the desired implication, not a refutation of the route.
  The attempted arithmetic proof expands the bounded loss into (S20).
  It fails at assigning a sufficiently small *summed* progression error:
  there are signed coefficients of growing degree and moduli outside the
  inspected Bombieri--Vinogradov ranges. The proposed shortcut of
  replacing the one-site divisor sum by periodic density with an
  $o(N_X)$ remainder is false by (S21). The corresponding weighted
  remainder is unknown, not refuted. Reopens with a switching or
  progression estimate that controls that remainder and gives the
  lower comparison with $\mathcal C_i/2$, or with a direct upper
  bound for the bounded prime event. Proposition S22 allows the single
  weighted-error bound $E\le N_X/64$ in place of the individual
  comparisons, but the exact identity for $E$ provides no such bound.
- **Step 5 by one zero-phase witness (Z9).** A single start suffices
  (Corollary Z2). A witness built from one residue class is a chain
  of about $\log_2\log p_n$ consecutive gaps each
  at least a constant times $\log p_n$, or is followed at once by a
  cluster of primes denser than the mean. The lower guarantee in the
  stated chain theorem of Ford, Maynard and Tao is $o(\log X)$ at that
  length even if it were uniform; this is not an upper bound on the
  actual gaps. The cluster theorems do not place primes after their
  selection. Unknown. Reopens with control of the selected subtuple, or
  a uniform chain theorem at that length in one class modulo $2^{K+1}$,
  together with an upper bound for the weighted following tail. The
  displacement bounds in case 2 grow exponentially; they do not
  exclude large gaps far down that tail. The classification concerns
  this one-class construction, not all pointwise certificates.
- **A large gap forcing a long binary run.** The replacement contradiction
  would fix an arbitrary odd denominator $d$, choose $L$ with
  $2^{-L}<1/d$, and find a sufficiently late $n$ with
  $1-2^{-L}\le\{G_n\}<1$. This contradicts $dG_n\in\mathbb Z$ and
  would exclude every denominator, including $d=1$. For $m=n+k$ put
  $V=\sum_{j=0}^k2^{k-j}g_{n+j}$. The exact identity
  $2^{k+1}G_n=V+G_{m+1}$ makes the needed prime input

  $$
  0<2^{k+1}a-V-G_{m+1}\le2^{k+1-L}
  \quad\text{for some integer }a.
  $$

  A large value of $g_m$ enters $V$ but supplies neither its position
  modulo $2^{k+1}$ nor the required interval for $G_{m+1}$. Relative
  domination of the other terms does not give the necessary absolute
  precision. The simultaneous interval assertion is unknown here; no
  inspected large-gap theorem supplies it. Reopens with a construction
  controlling both the weighted prefix and the continuation at this
  scale, not a larger isolated gap alone.

- **Upper alternatives at length $\log_2\log X+O(1)$ ((AC) or U4).** Missing:
  control of the local density of weighted block sums at a small fixed
  scale, or the small-carry count at $K=\log_2\log X+O_d(1)$.
  Unknown. A suitable fixed-factor comparison suffices, as proved on
  the upper-count page.
- **Step 5 by the signed majorant (SB).** Unknown. The weighted first
  model layer is $\gg_{d,\theta}(\log X)^4N_X$, proved by an exact
  count, not a phase-uniformity assumption. More decisively, bounding
  the signed error by its termwise adverse part cannot give $O(N_X)$:
  tuples forbidden modulo $3$ already contribute
  $\gg_{d,\theta}(\log X)N_X$ (Lemma U7). That proposed bound is
  false. This excludes the specified error accounting around the
  Bernoulli reference, not every signed estimate or every sieve
  method. Reopens with cancellation, a reference incorporating the
  arithmetic exclusions, or a different majorant. No equivalence
  with a uniform prime-tuples conjecture is proved.
- **Step 2 by clearing the odd denominator (O9).** The step lemma is valid,
  but the apparent reduction in length counts filtered gaps. For every
  nonnegative integer filter, its span and mean cost restore the original
  critical-length threshold. Proved for the same mean-based criterion.
  Reopens if a prime theorem controls the filtered statistic more easily.
- **Step 2 at all cuts of a block (O10).** Missing: an estimate using
  primality, consecutiveness or carry sizes to exclude the rational carry
  path. Unknown. Treating the integrality constraints at overlapping cuts
  as independent is false: a single endpoint congruence is equivalent to
  all of them, including the numerator's index phase when it is prescribed.
  Every finite positive gap block has such positive integer completions.
  A bound or exclusion for the actual following tail remains necessary.
- **Step 5 from bounded-length information (O1).** Fails for every bounded
  length, since the count needs $2^K>2d\log X$. Proved.
- **Step 5 from residues below the critical length (O8, L228).** Fails: the
  comparison sequences keep those residues and the growth of $p_n$ and have
  rational sums; their terms need not be prime. Proved at author standing.
  Reopens only with information that the comparisons do not preserve.
- **Pointwise brackets (O3).** The gap bound alone needs about
  $0.525\log_2p_m$ gaps at one index. Proved limitation of that input.
- **Weighted means (O4).** Bounded weights never ask for less, and sieve
  weights ask for more. A second moment of the strength the Cramér model
  predicts would lower the proportion needed; the known bounds, Selberg's
  under the Riemann hypothesis and Stadlmann's unconditional one, need longer
  blocks. Proved comparison.
- **Bounded tails with infinitely many values.** A lattice has only finitely
  many points in a bounded range, so infinitely many distinct values of
  $G_n$ below a fixed bound $B$ would exclude every rational value; this is
  the mechanism of
  [[problems/irrationality/E0251/claims/2026_09_06_land|Land's conditional claim]].
  Missing: infinitely many distinct values with $G_n\le B$, or a strict
  approach to a finite limit. Even boundedness alone is not obtained by the
  inputs examined here. Since
  $G_n=\sum_{\ell\ge1}(p_{n+\ell}-p_n)2^{-\ell-1}$, it requires
  the $\ell$th prime after $p_n$ within $2^{\ell+1}B$ for every $\ell$, about
  $\log_2\log p_n-O_B(1)$ primes in a nested cluster within $(\log p_n)/2$.
  In the construction that must work from the first selected prime for
  every $m$-element selection from a $k$-tuple of diameter $D$, a selection
  containing both endpoints requires $D\le2^mB$, hence
  $m\ge\log_2D-\log_2B$. The usual Maynard lower guarantee is about
  $(\theta/2)\log k\le(\theta/2)\log(D+1)$ primes, with $\theta<1/2$ from
  Bombieri--Vinogradov, and does not reach that threshold even at
  $\theta=1$. This compares that guarantee, not an upper bound for every
  sieve construction or a construction with an adaptive root. Unknown for
  the actual primes. Land's claim
  derives such tails from a uniform prime-tuple hypothesis; the claim is
  unreviewed and is not a premise here.
- **Matching windows.** Missing: equal windows with small later tails at
  late starts whose preceding gaps lie in different classes modulo $4$,
  or, for $d>1$, in different index classes. The graded congruences
  $h_{n+j}\equiv h_{m+j}\pmod{2^{j+1}}$ also suffice if the preceding
  gaps violate $g_{n-1}-g_{m-1}\equiv2I\pmod4$, where
  $I=Q_{n,K}-Q_{m,K}\in\mathbb Z$, or violate the higher congruence
  (8) of the matching-window note. These occurrences are unproved. That note
  proves both restrictions at author standing. The preceding-gap
  congruence holds for every odd $d$, so a separate dyadic argument is not
  needed; its reversed form makes the tail constant on each class of graded
  congruences of the preceding gaps. The graded variant gives the following
  tails equal and the initial halved tails differing by an integer, with
  an explicit correction to the preceding-gap congruence. Occurrence is
  not the obstacle: by pigeonhole and (T), all but $X^{o(1)}$ of at least
  $(3/4-o(1))N_X$ starts share their window of $\lceil A\log_2\log X\rceil$
  gaps with another start, both later tails being small (proved on the
  matching-window note). A rational value with odd part $d>1$ would make
  the index class modulo $\operatorname{ord}_d(2)$ constant on each such
  window class. One late pair in different classes would refute it; no
  inspected theorem relates a gap window to the index of its first prime.
  By the step lemma each odd part is a dyadic case for coarser gaps, where
  index classes give nothing. Every odd $d$ also makes the class modulo $4$
  of the preceding gap constant on each equal-window class. No inspected
  theorem supplies the required joint pattern of
  $\lceil A\log_2\log X\rceil$ consecutive gaps and the adjacent gap.
  Occurrence of a fixed window alone does not supply the later-tail bound.
  Reopens with such a statement for the actual primes.
- **Zero phases with a large-gap count (Z8′).** The finite-prefix and far-tail
  interface is proved. A bound $N(x,H)\ll x(\log x)^{B'}/H^2$, together
  with zero-phase frequency $\gg2^{-K}N_X$ at
  $K=\lceil A\log_2\log X\rceil$, $A>B'+1$, would finish the proof.
  The frequency is unknown; the stronger proposed gap-count exponents
  need their own source warrants. The elementary first moment gives an
  exceptional upper bound larger than the required count by a factor of
  order $\log X$, which increasing $A$ does not remove.
- **Residue switches through second moments.** The
  [[research/prime_binary_new_attack/residue_switch_moments|moment criterion]]
  needs a same-class pair coefficient below $1-1/\lambda$ in intervals
  of length $\lambda\log x$. For modulus $4$, a pair-sieve constant
  below $2-2/\lambda$ would suffice; the examined constant-$8$ bound
  and even a constant-$4$ input miss it. The fourth moment controls
  concentration but does not lower that pair constant. The inspected
  inputs do give an aggregate positive proportion of switches for fixed
  $q$ with $\varphi(q)>8$. This supplies no growing-block estimate and
  no modulo-$4$ conclusion. Reopens with a sharper averaged pair estimate
  or another mechanism controlling the required parity.
- **Distinct tails as a coordinate.** For $n\ge3$,
  $H_n-2^{n-2}S$ is an integer. Together with U1 this makes irrationality
  equivalent to injectivity of $n\mapsto H_n$ on $n\ge3$. This is a
  valid reformulation, not a prime-input theorem. U1 already makes a
  rational value repeat one tail at least a constant times
  $N_X/(d\log X)$ times on a dyadic prime interval. A bound excluding
  that repetition is missing; none follows from merely changing
  coordinates. Reopens with a quantitative count for actual tails or
  their weighted truncations.
- **Conditional claims.** The two claim pages under Problem 251 assume uniform
  prime-tuple hypotheses. They are not premises here.
- **A fixed-range carry countermodel.** Positive integers
  $c_n\in[\lambda,2\lambda-1]$ give positive half-gaps
  $h_n=2c_n-c_{n+1}$ and $H_n=c_n$, hence a dyadic binary sum.
  The positions are
  $x_n=x_0+2c_0+2\sum_{0\le i<n}c_i-2c_n$. For fixed $\lambda$
  these grow linearly, so the assertion that this seed also has PNT
  growth is false. A construction with growing carries, the required
  roughness, Bombieri--Vinogradov distribution and the named string
  properties is unproved here. Neither this seed nor L228--L230
  supplies such a model or an estimate for the actual primes.

## Next moves

- Attack the bounded actual-prime event (BC) directly at the unchanged
  shorter-span parameters, first at $d=1$ as a diagnostic. An upper
  bound $N_X/32$ on unbounded scales for every fixed odd $d$ closes the
  whole contradiction. Alternatively estimate the weighted band error
  $E$ of S22 by $N_X/64$, with every signed arithmetic error paid.
  Neither a proof at $d=1$ alone nor another exact expansion settles
  the target. A proof may use the rational carry lattice; it need not
  establish a stronger unconditional distribution law. If the arithmetic
  estimate cannot be supplied, replace the mechanism while retaining the
  complete contradiction and its precise gap.
- At the enlarged span $K(\log X)^2$, D18 leaves the concrete test
  $P_{\rm SF}^{<T_0}(X)\le N_X/6$ at a sufficiently large fixed rank
  cutoff. Its proof would finish this variant for each fixed odd $d$.
  A proof through the ordinary-crossing surrogate must use integrality
  or another consequence of rationality: D19 proves a contradictory
  unconditional lower bound for that surrogate. An unconditional
  estimate of the original residue gains may instead retain the full
  phase in (D20). The endpoint identity does not refute a
  least-factor argument, but supplies no estimate for its carry-dependent
  weights. Use (D21)--(D22) to retain the actual selected integer and all
  flags; a finite-period locator and single-prime progression counts do
  not estimate that joint sequence, as the scoped model (D23) shows.
  The direct fixed-saving bound for $B_d(X)$ remains an alternative.
- For the dephased transport, choose the resonant parameters (P9a) for
  each fixed odd $d$ and estimate the signed cofactor sum (P6), with
  multiplier $b$, strictly below $3N_X/2$ on unbounded scales. Its
  coefficient norm is bounded, but its actual prime-gap coefficient
  remains unestimated. The reference phase is $-1/2$ for every $d$;
  the sign issue of P8 concerns only its restricted reference family.
  Preserve the root phase when passing between this sum and the
  original transport; their unconditional endpoints differ. The upper
  bound $2N_X+o(N_X)$ and a telescope do not provide the saving. The
  estimate may use the prefix coefficient permitted by integer carries
  or another proved consequence of rationality. Frequency doubling and
  the direct short-shift comparison in P9 supply no saving. The signed
  crossing identity (P9h) retains the arithmetic weight but does not
  estimate it. Rationality-dependent bounds for that sum remain legitimate;
  an unconditional bound would estimate the endpoint correlation in (P9c).
- For the matching route, the discriminating test is one late pair of
  good starts with equal windows of $\lceil A\log_2\log X\rceil$ gaps
  whose preceding gaps lie in different classes modulo $4$. It would
  refute every rational value with odd part $d$ and earlier preperiod,
  including the dyadic ones, and a family at unbounded indices for every
  $d$ would prove irrationality. The equal windows are already supplied
  by pigeonhole; the adjacent residue is the whole missing input.
- The shorter-span monotone event (MS) needs both costs on common
  unbounded scales, for every fixed odd $d$. Rough composites are
  removable from its bounded event and its second moment by the
  survivor-moment estimates. The next moment test is cancellation in
  the actual prime-rooted pair/triple combination (PVM); fixed-dimensional
  upper sieve bounds alone give only constant-factor errors. A continuation
  also needs the damped signed bound (S16), or another estimate for the
  truncated phase cost. Its coarse Fourier component is controlled, but
  its residual is not. Resolving the moment alone does not finish the
  contradiction; a direct bound for the bounded event can replace both
  tests. Neither missing arithmetic estimate has been disproved.
  The band-loss inequalities (PB) would replace both by implying (MS).
  Their exact sum (S20) gives a concrete alternative test: handle the
  signed divisor remainder and prove the lower comparison with
  $\mathcal C_i/2$ for all eight bands on common scales. The one-site
  calculation (S21) forbids discarding the arithmetic correction to
  periodic density as $o(N_X)$; it does not settle the weighted sum.
- The main discriminating test is a bound for $B_d(X;K)$ itself with
  loss $Cc^K$, $c<2$, at the length of Theorem U8, first for $d=1$.
  A fixed upper bound below $13/16$ is enough. The deletion form (PD)
  pays for its semiprimes with two large factors (Lemma U16,
  Corollary U17), and its remainder (SF) is no weaker than this test.
  A further attempt on (PD) must change the starting set or the
  deletion order so that the remaining weights fall under a known
  theorem, or estimate the residues of $p_r$ modulo small primes
  jointly with the preceding weighted block sum. Replacing the
  preceding primes by a random model or by rough survivors does not
  prove (PD*).
- The adverse-error bound around independent Bernoulli sites is false.
  Lemma U9 gives an arithmetic reference, with no transfer to primes;
  Lemma U13 and Proposition U14 concern only their specified nonnegative majorant
  class and span. A different majorant must state where primality and
  consecutiveness enter and how every error is paid for. Grouped
  selection does not by itself furnish a pointwise certificate: Z6c
  gives unhelpful representatives even with the groups prescribed.
  Reopening that construction needs information about which
  representatives are selected or about the primes following them.
- A lower bound of positive proportion for the mispredicted starts at length
  $\log_2\log X+O(1)$, for a single $d$. Even $d=1$ would be new: it would
  show that the binary expansion of $S$ does not terminate.
- The discriminating test for the zero-phase route: a lower bound of order
  $2^{-K}N_X$ for zero-phase starts at a length $K$ that grows with $X$, even
  without the continuation. Under the Riemann hypothesis this alone would
  suffice at length $A\log_2\log X$ with $A>4$ (Proposition Z8);
  unconditionally it would still need the conditional continuation of
  ZPC($d$). Proposition Z8′ gives the alternative threshold $A>B'+1$
  under its explicit large-gap count; improving that tail input alone
  does not prove the phase frequency. A theorem of this shape is not
  supplied at any growing length.
- An upper bound, within any fixed factor, for the number of starts whose
  weighted sum of the next $\log_2\log X+O(1)$ halved gaps lies in a short
  interval: condition (AC) of the upper-count note. It is free of $d$ and
  asks only for an upper estimate, but for consecutive primes at a growing
  length.
- A smaller step that is itself open: a positive proportion of $n$ with
  $p_n\not\equiv p_{n+1}\pmod 4$. This is one side of the necessary
  marginal condition for the $j=0$ overlap bound in part 2 of Theorem F.
  It would not prove CPS($d$) but would measure the
  distance from the known theorems, which give only constant residue
  patterns. By Corollary O8 it carries no information about rationality by
  itself when used only with the growth and residue information preserved
  by the comparison sequence.
- The finite-window attempts for CPS($d$), (UPD), (AC), (BC) and the
  small-factor test reach roughly $\log_2\log X$ consecutive primes,
  with power-of-two moduli of order a power of $\log X$. The inspected
  fixed-length results and cluster bounds have not supplied the stated
  estimates at that scale. This describes these attempted proofs, not
  necessary inputs to every proof of the sufficient targets. The
  repeated-window lemma already supplies many equal windows with small
  later tails; its remaining condition on the preceding gap modulo $4$,
  or for $d>1$ on the index class, must be kept separate from the
  counting targets.
  L228--L230 restrict particular local and sparse substitutes for primes,
  but give no model satisfying the prime number theorem and
  Bombieri--Vinogradov in progressions together with every cluster and
  gap input used here. No such stronger insufficiency theorem is proved.
- A conditional route could estimate the alternating expansion of
  [[research/prime_binary_series/single_phase_comparison|the single-phase comparison]],
  using quantitative Hardy–Littlewood estimates at growing tuple lengths.
  No new sufficient error budget or weakening of the retained conditional
  hypotheses is proved here. Upper bounds on all tuple counts do not
  supply the signed lower estimate.

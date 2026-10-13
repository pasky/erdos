---
name: arithmetic_functions/openai_2026_prime_predecessors_even_number_prime_factors/theorem_1_1
title: "Theorem 1.1: infinitely many primes p with p-1 squarefree and Omega(p-1) even"
desc: |
  The manuscript's main claim: infinitely many primes p for which p-1 is
  squarefree with an even number of prime factors, that is with mu(p-1)=1.
  Claims checked only.
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

***

## Statement

For a positive integer $n$, $\Omega(n)$ counts the prime factors of $n$ with
multiplicity and $\omega(n)$ counts its distinct prime factors (p. 1). For
squarefree $n$ the two agree and the Möbius function is
$\mu(n)=(-1)^{\omega(n)}$; for $n$ not squarefree, $\mu(n)=0$.

**Theorem 1.1.** The set of primes $p$ for which $p-1$ is squarefree and
$\Omega(p-1)$ is even is infinite. Since $\Omega(p-1)=\omega(p-1)$ for these
primes, the same set gives infinitely many such primes when only distinct
prime factors are counted; it is exactly the set of primes with
$\mu(p-1)=1$, the form the abstract states.

The introduction calls this an affirmative answer to "the parity question for
predecessors of primes" (p. 1), and says the squarefreeness condition is
there to make the two ways of counting prime factors agree. The statement
gives no count, density or explicit threshold. The closing paragraph of the
proof observes that every $u$ in the support of the weights lies in $[x,2x]$,
so the primes $p=2u+1$ it finds exceed $x$, with $x$ arbitrarily large. Every
supported $u$ is odd, so each prime found has $p-1=2u$ with $u$ odd and
$\Omega(u)$ odd, hence $p\equiv3\pmod4$ (the congruence is an observation
made here, not stated in the manuscript).

**Source.** OpenAI, *Prime Predecessors with an Even Number of Prime
Factors*, release folder
`preprints/Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026`;
TeX file `build/main.tex`, label `thm:main` (lines 53--57; the abstract at
lines 40--44), PDF p. 1; the proof closes in
`build/sections/07-extraction.tex` (lines 645--668, PDF pp. 44--45). Provenance
and attestations are on
[[arithmetic_functions/openai_2026_prime_predecessors_even_number_prime_factors/_index|the card]].

**Read depth.** Claims checked: the statement, the abstract's equivalent
form and the definitions of $\Omega$ and $\omega$ were read clause by clause
in the TeX source. The closing proof (lines 645--668) was read in full but not
checked; the lemmas it combines and the argument of Sections 2--8 behind them
were read for their structure only, as summarized below, and no step was
checked. Nothing here is independently reviewed.

## Proof pointer

Write $L=\log x$ and $p=2u+1$. The proof builds nonnegative weights $A(u)$ on
odd $u$ in $[x,2x]$ whose support forces $\Omega(u)$ to be odd, shows that
the weights are well distributed in two senses, and then runs a sieve on
$2u+1$ that keeps a positive proportion of the weighted mass on primes.

The weights (Section 5). Two disjoint families of odd primes are used. The
ordinary bands $Q_j$, $0\le j\le j_x$, take the primes with
$\log p\in[s_j,\tfrac65s_j]$, $s_j=s'2^{-j}L$, down to $s_j$ of order
$\log L$; the weight $a(v)$ counts the ordered ways of writing $v$ with
exactly $r_0$ primes from each band, divided by $(r_0!)^{j_x+1}$, with $r_0$
a fixed even integer, so the ordinary part of a supported $u$ has
$r_0(j_x+1)$ prime factors, an even number. Groups $\mathcal P_g$ of primes
with $\log p$ in
$[L^{1/10},L^{1/5}]$ or $[L^{3/10},L^{2/5}]$ carry a marked weight $W_1$
that asks for a prime divisor from every group and damps each further one by
$1/2$. With $\mathcal E(u)=-1$ raised to the number of group-prime factors of
$u$ counted with multiplicity, $A(u)=W_1(u)a(u_*)(1-\mathcal E(u))/2$, where
$u_*$ is the part of $u$ prime to the groups; the projection keeps an odd
number of group-prime factors, so $A(u)>0$ forces $\Omega(u)$ odd and
$\Omega(2u)$ even ((5.5), p. 23). Lemma 5.2 gives the total mass
$X_A=\sum_uA(u)\Psi(u/x)\gg xL^{-C_A}$, and Lemma 5.3 shows that the $u$ with
$2u$ not squarefree carry only $o(X_A/L)$.

Distribution (Sections 6--7). Theorem 6.1 is a Type II estimate: for
$2u+1=mn$ with $m,n$ in dyadic ranges inside $[x^{b_*},x^{1-b_*}]$, the
bilinear sum against $A(u)\Psi(u/x)$ is $\ll xL^{-D_*}$ whenever the
coefficient on $m$ has small discrepancy against characters and phases of
log-power size, with no condition on the other coefficient. Writing
$A=A_0(1-\mathcal E)/2$, it is proved for $A_0$ and for $A_0\mathcal E$: one
band prime in $[x^\tau,x^\eta]$ is designated as a prime slot, the remaining
band primes are allocated smoothly between two factors $e,h$ of $u$, and after
Fourier separation and Cauchy--Schwarz a change of variables turns the
off-diagonal terms into shifted correlations of the kind Theorem 4.1 bounds,
with the same sign at both ends. Theorem 4.1 is where the parity enters: in
the lifted dilation-graph pairing imported from S, a shared dilation $D_R$
divides both positions, and complete multiplicativity gives
$\varepsilon(D_R)^2=1$ ((4.18), p. 16), so the sign survives the graph
reduction; the comparison terms are bounded through local Fourier energy,
with
[[arithmetic_functions/openai_2026_prime_predecessors_even_number_prime_factors/lemma_3_1|Lemma 3.1]]
on the prime slot at large heights. Theorem 7.1 supplies level of
distribution $x^\vartheta$, $\vartheta<1/2$, for the weights in congruence
classes $2u+1\equiv0\pmod d$.

Extraction (Section 8). The block sieve with Theorem 7.1 gives a presieved
mass at least $(\mathfrak SX_A/L)(e^{-\gamma_E}/b_1)(1-O(e^{-c/b_1})+o(1))$
on $u$ with $P^-(2u+1)>x^{b_1}$ (Lemma 8.6). Composites whose least prime
factor $n$ lies in $(x^{b_1},x^{1/2-\kappa}]$ are bounded by replacing the
rough indicator of the cofactor by its local-density proxy (Lemma 8.5, which
applies Theorem 6.1 to the difference), a sieve conditional on $n$ (Lemma 8.7)
and Buchstab's identity for the rough density; for $b_1$ small this
leaves at least $\mathfrak SX_A/(2L)$ on primes and on products of two
primes both above $x^{1/2-\kappa}$ (Lemma 8.8). Those products are bounded by
$C_{\rm bal}(\kappa+1/L)X_A/L+o(X_A/L)$ (Lemma 8.9) through the prime-proxy
density and a positive pair estimate (Lemma 8.4) whose constant does not
depend on $\kappa$. Choosing $\kappa$ with $C_{\rm bal}\kappa<\mathfrak S/4$
leaves $\gg X_A/L$ of mass on $u$ with $2u+1$ prime; removing the $u$ with
$2u$ not squarefree (Lemma 5.3) leaves a supported $u$ with $2u+1$ prime and
$2u$ squarefree, and then $\Omega(2u)=1+\Omega(u)$ is even. The manuscript
fixes the order of choices: the weight data and $C_{\rm bal}$, then $\kappa$,
$b_1$, the mesh, the distribution savings, the discrepancy exponent $B$, and
last the proxy precision $S_1>2B+3$, before $x$ grows.

## Dependencies

Proved in the manuscript: Lemma 2.4 (in an elementary version), the lemmas
of Section 3, Theorem 4.1 given its imported inputs, Lemma 4.4, the lemmas
of Section 5, Theorems 6.1 and 7.1, and Lemmas 8.3 to 8.9. Imported at
statement level, without proof, from the companion S, *Weighted dilation
graphs, smooth shifted primes and totient fibers*
([[arithmetic_functions/openai_2026_weighted_dilation_graphs_smooth_shifted_primes_totient_fibers/_index|card]]):
the forms of the classical estimates in Propositions 2.1--2.3 (prime number
theorem, Mertens and Siegel--Walfisz; large sieve, divisor moments and
mean values; derivative tests); the transference and residual ideal operator
results of Propositions 4.2--4.3 (S's Theorem 3.5, Corollary 3.11 and
Lemma 3.4; S's Theorem 4.1 and Lemma 4.3) and S's integer bilinear estimate
(its Lemma 4.2); the block sieve of Lemma 8.1 (S's Lemma 2.9) and the proxy
estimates of Lemma 8.2 (S's Lemmas 7.3 and 7.4). Linnik's $p$-adic form of
Vinogradov's mean-value method enters Lemma 3.2, with Wooley (2012,
Section 2) cited for an exposition. None of these was checked here, and the
statements attributed to S were not compared with S.

## Bears on

The manuscript names no Erdős problem, and no problem page is identified as
using this theorem.

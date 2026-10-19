---
name: research/covering_prime_interfaces/prime_pattern_uniformity
title: Uniformity required by prime patterns
desc: Growing parameters, exceptional bases, representation tails and short-interval errors in additive prime-pattern routes.
tags: [primes, uniformity, sieve]
sources: []
created: 2026-10-14T22:17:53Z
updated: 2026-10-14T22:17:53Z
---

# Uniformity required by prime patterns

***

These author-recorded route comparisons retain source dependence explicitly.
Inspected theorem statements are not independent verifications of their proofs.

## Growing families and unproved hypotheses

The conditional convergence theorem for
[[problems/primes/E0015/_index|Problem 15]] uses a quantitative
Hardy--Littlewood hypothesis uniform over tuple sizes up to
$(\log\log x)^5$ and shifts up to $(\log x)^2$, with a power-saving
error. This is Conjecture 1.3 and Theorem 1.4 in
[[../library/primes/tao_2023_convergence_alternating_series_erdos_assuming_hardy/_index|Tao's paper]];
the [[research/erdos_15/_index|existing reconstruction]] records the
argument and its qualified review. Fixed-tuple asymptotics do not supply
that growing uniform range. The relevant convergence is convergence of
partial sums of the alternating series, not absolute summability. The
formalization issue on the problem page does not remove this hypothesis.

Similarly, a cluster prime in
[[problems/primes/E0017/_index|Problem 17]] requires all the specified
even differences up to a bound growing with that prime, with both endpoints
within the prime's range. The sparse upper bound in Theorem 1 of
[[../library/primes/elsholtz_2003_cluster_primes/_index|Elsholtz's paper]]
is compatible with finitely or infinitely many cluster primes. It supplies
no growing family of simultaneous representations. The discriminating
question is uniformity over that entire growing set of differences, not
existence for each fixed difference separately.

Theorem 3 of
[[../library/primes/erdos_1949_applications_brun_s_method/_index|Erdős's
Brun-sieve paper]] gives, for each fixed separation $c_2>0$, some positive
coefficient $c_6(c_2)$ and a run of at least
$\lfloor c_6(c_2)\log x\rfloor$ consecutive primes below $x$ whose adjacent
gaps exceed $c_2$, for all sufficiently large $x$. The exact question in
[[problems/primes/E0238/_index|Problem 238]] requires more than
$c_1\log x$ consecutive primes for every prescribed $c_1,c_2>0$.
Adjacent separation implies pairwise separation within the run, but the
coefficient of the number of primes must become arbitrarily large for fixed
$c_2$. The theorem only gives one positive coefficient depending on $c_2$.
The discriminating test is whether a proposed result supplies every $c_1$,
with the threshold allowed to depend on $c_1,c_2$. Stop at a single small
coefficient; this is a count of consecutive primes, not an interval-length
parameter.

## A second moment controls almost all representations

Let $r(n)=\#\{(p,k):n=p+2^k,\ p\text{ prime},\ k\ge1\}$.
Display (2.11) of
[[../library/primes/chen_2023_conjecture_erdos_p_2_k/_index|Chen's paper]]
imports the classical sieve estimate $\sum_{n\le X}r(n)^2\ll X$.
Its statement and surrounding definition were inspected; the cited
second-moment proof was not rechecked. For any fixed $\varepsilon>0$ it
implies

$$
\#\{X<n\le2X:r(n)>\varepsilon\log n\}
\ll_\varepsilon\frac{X}{(\log X)^2}.
$$

Allowing $k=0$ adds at most one representation and does not change the
limiting issue in [[problems/primes/E0236/_index|Problem 236]]. The
estimate gives a density-zero exceptional set, not the asserted bound
$r(n)=o(\log n)$ for every sufficiently large $n$. To see the logical
gap, the nonnegative sequence $b(2^j)=j$, $b(n)=0$ otherwise, satisfies
$\sum_{n\le X}b(n)^2=O((\log X)^3)=O(X)$ yet
$b(2^j)/\log(2^j)=1/\log2$. This is not a representation-count
counterexample. A route must rule out sparse spikes using arithmetic
information beyond the second moment; stop if Markov's inequality is its
only tail control.

## Exceptional bases and admissible patterns

The held fourth version of
[[../library/primes/ding_2025_two_romanoff_type_problems_erdos/_index|Ding's
Romanoff-type paper]] proves positive lower density for almost every real
base, as recorded for [[problems/primes/E0244/_index|Problem 244]].
An almost-everywhere theorem may exclude every member of a countable
specified family. It therefore does not settle an arbitrary fixed base.
The source card records a golden-ratio result in a later version; that
specific-base result is separate from the held version's theorem, and no
proof from the later version is imported here. The full target remains
every real $C>1$. A useful test names one previously uncovered base and
checks its actual hypotheses; stop treating a measure-zero exception as
empty.

For [[problems/primes/E0855/_index|Problem 855]], the inspected Theorem
1.1 of
[[../library/primes/chahal_et_al_2025_second_hardy_littlewood_conjecture/_index|Chahal
and collaborators]] assumes a positive nondecreasing $R$ with
$|\pi(x)-\operatorname{li}(x)|\le CR(x)$ and
$x^{1/2}\le R(x)\le x/(\log x)^3$ for large $x$. Its conclusion holds
in the range

$$
\frac{3CR(2x)(\log x)^2}{\log\log x}\le y\le x.
$$

This is a lower restriction on the smaller variable $y$ in terms of the
larger variable $x$. It leaves pairs where both grow but $y$ is below that
threshold. The restriction cannot be dropped to obtain the eventual
assertion for all pairs.

In the opposite direction, an admissible tuple of diameter $h$ with more
than $\pi(h)$ members would yield a violation of the prime-count
subadditivity inequality at interval length $h$ if it occurred as a tuple
of primes. Admissibility is only the local congruence condition. An
unproved prime-tuple conjecture is needed for that occurrence argument.
Moreover, one fixed $h$ does not refute a statement restricted to both
variables sufficiently large; the construction must allow unbounded $h$.
The admissible-set extremal information in
[[problems/integer_sequences/E1204/_index|Problem 1204]] supplies neither
of these missing prime-occurrence assertions. The one-step test is to write
the actual two parameter ranges and the occurrence hypothesis. Stop at a
fixed diameter or an unproved tuple hypothesis rather than declare an
unconditional disproof.

## A short-interval prime theorem gives only its own exponent

Suppose a set $A\subseteq\mathbb N$ in
[[problems/primes/E0428/_index|Problem 428]] has arbitrarily large integers
$N$ for which every $a\in A$, $0<a<N$, has $N-a$ prime. Fix $0<\theta<1$
and put $x=N^\theta$. Injecting these $0<a\le x$ into primes of
$[N-x,N)$ gives

$$
A(x)\le\pi(N)-\pi(N-x)+O(1).
$$

If a prime-number-theorem asymptotic is available uniformly at that length,
then the right side is $(1+o(1))x/\log N$, whereas
$\pi(x)\sim x/(\theta\log N)$. Along those $N$ this proves
$\liminf A(x)/\pi(x)\le\theta$. A theorem valid only above a fixed
positive exponent therefore supplies only a positive upper bound.
To answer the existence question negatively by this argument, one needs
zero instead of a positive upper bound. That requires the short-interval
asymptotic for arbitrarily small fixed $\theta$, or an additional idea.

## Local gaps and weighted short intervals

For the midpoint quantity in
[[problems/primes/E0454/_index|Problem 454]], write
$M_n=\min_{1\le i<n}(p_{n+i}+p_{n-i}-2p_n)$. The inner expression is

$$
\sum_{j=0}^{i-1}(d_{n+j}-d_{n-j-1}).
$$

Its first term being large is necessary, not sufficient, for $M_n$ to be
large: every subsequent partial sum must remain large. The data and
midpoint discussion on the
[[../library/primes/mcnew_2018_convex_hull_prime_number_graph/midpoint_convex_primes_p13|McNew
source page]] do not supply the arbitrary-height, all-$i$ conclusion.
The discriminating test is control of the minimum of all these partial
sums at the same center.

Finally, for [[problems/primes/E0950/_index|Problem 950]], set
$A_n(t)=\#\{p<n:n-p\le t\}$ for integers $1\le t\le n-1$. Exact
summation by parts gives

$$
\sum_{p<n}\frac1{n-p}
=\frac{A_n(n-1)}{n-1}
+\sum_{t=1}^{n-2}\frac{A_n(t)}{t(t+1)}.
$$

The largest weights lie on the shortest backward intervals. A global prime
number theorem does not give the needed uniform control of these terms
for every $n$. No primary proof of the requested bound is supplied here.
The next test is a bound for the weighted short-interval sum itself; stop
if only a macroscopic prime-count asymptotic is available.

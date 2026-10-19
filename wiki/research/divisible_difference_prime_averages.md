---
name: research/divisible_difference_prime_averages
title: Finite prime averages for sets with no divisible differences
desc: |
  Reconstructs the known half-density bound for sets with no divisible
  differences above a fixed threshold, using an exact finite-period variance;
  the sharper maximum and error term remain undetermined.
problems:
- 635
created: 2026-10-14T23:20:16Z
updated: 2026-10-14T23:20:16Z
---

For fixed real $t\ge1$, let $F_t(N)$ be the maximum size of a set
$A\subseteq\{1,\ldots,N\}$ such that

$$
a,b\in A,\qquad b-a\ge t
\quad\Longrightarrow\quad b-a\nmid b.
$$

Then

$$
F_t(N)=\left(\frac12+o_t(1)\right)N. \tag{1}
$$

This is the half-density subanswer of
[[problems/integer_sequences/E0635/_index|Problem 635]]. The known
second-moment argument is described on
[[problems/integer_sequences/E0635/claims/2026_01_30_leeham|the Leeham claim page]],
which also records its connection to Elliott's inequality. The proof below
is a self-contained reconstruction by Plasma AI using finite prime averages;
it makes no novelty claim and does not audit the linked manuscript, book
inequality or external formalization. It is author-recorded, with no
independent examination or change to the problem's acceptance standing.

## Counting consecutive multiples

Fix a nonempty finite set $P$ of primes with $p\ge t$ for every $p\in P$.
Write

$$
m=|P|,\qquad Q=\prod_{p\in P}p,\qquad
\mu=\sum_{p\in P}\frac1p,\qquad
w(n)=\sum_{p\in P}1_{p\mid n}.
$$

For a fixed $p\in P$, no two consecutive multiples $jp,(j+1)p$ can
both lie in $A$: their difference is $p\ge t$ and divides the larger.
Among the $\lfloor N/p\rfloor$ multiples of $p$ in $[1,N]$, at most
$\lceil\lfloor N/p\rfloor/2\rceil$ can therefore belong to $A$.
Summing over the primes, with multiplicities counted by $w$, gives

$$
\sum_{n\in A}w(n)
\le\sum_{p\in P}\left(\frac{N}{2p}+\frac12\right)
=\frac{N\mu}{2}+\frac m2. \tag{2}
$$

## The exact variance on a finite period

For a uniformly chosen residue modulo $Q$, the events $p\mid n$, for
$p\in P$, are independent by the Chinese remainder theorem. Their
probabilities are $1/p$, so

$$
\frac1Q\sum_{n=1}^Q(w(n)-\mu)^2
=\sigma^2:=\sum_{p\in P}\frac1p\left(1-\frac1p\right)
\le\mu. \tag{3}
$$

In particular, this uses only a fixed finite set of primes, with no
uniform probabilistic theorem about a growing prime range. Both $w$ and
$(w-\mu)^2$ are $Q$-periodic, and $|w(n)-\mu|\le m$. Splitting
$[1,N]$ into full periods and a remainder gives the explicit estimate

$$
V_N:=\sum_{n=1}^N(w(n)-\mu)^2
\le N\sigma^2+Qm^2. \tag{4}
$$

Cauchy--Schwarz, applied to any admissible $A$, now yields

$$
\sum_{n\in A}w(n)
=\mu|A|+\sum_{n\in A}(w(n)-\mu)
\ge\mu|A|-\sqrt{|A|V_N}
\ge\mu|A|-\sqrt{NV_N}. \tag{5}
$$

Combining (2), (4) and (5) proves, uniformly over every admissible $A$,

$$
\frac{|A|}{N}
\le\frac12+\frac{m}{2N\mu}
  +\frac{\sqrt{\sigma^2+Qm^2/N}}{\mu}. \tag{6}
$$

## The order of limits and the remaining question

Keep $P$ fixed while letting $N$ tend to infinity in (6). The same bound
holds for the maximum $F_t(N)$, since (6) did not depend on $A$. Thus

$$
\limsup_{N\to\infty}\frac{F_t(N)}N
\le\frac12+\frac{\sqrt{\sigma^2}}\mu
\le\frac12+\frac1{\sqrt\mu}. \tag{7}
$$

The sum of prime reciprocals diverges, and deleting the finitely many
primes below $t$ does not change that. For completeness, if that sum
converged, the finite Euler products
$\prod_{p\le x}(1-1/p)^{-1}$ would be bounded: take logarithms and use
$-\log(1-1/p)\le1/p+2/p^2$. But their geometric-series expansions contain
every reciprocal $1/n$ with $1\le n\le\lfloor x\rfloor$, so they
dominate the divergent harmonic sums. This is a contradiction.

Consequently finite sets $P$ of primes above the fixed threshold can
make $\mu$ arbitrarily large. Taking that choice only after the limit
in (7) gives $\limsup F_t(N)/N\le1/2$. The odd integers in $[1,N]$
are admissible: a positive difference of two odd integers is even and
cannot divide the odd larger integer. They supply
$F_t(N)\ge\lceil N/2\rceil$, proving (1).

The estimate is for each fixed $t$; it asserts no uniformity for $t$
growing with $N$. Although (6) is explicit for a chosen $P$, its period
$Q$ can be very large. This argument neither determines the exact
maximum nor closes the gap in its additive error term. No finite census,
claimed formal build or independent proof acceptance is used.

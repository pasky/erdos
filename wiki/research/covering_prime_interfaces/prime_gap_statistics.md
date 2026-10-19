---
name: research/covering_prime_interfaces/prime_gap_statistics
title: What prime-gap statistics would imply
desc: Support, moments, first-occurrence times and adjacent-record conditions required by seven prime-gap questions.
tags: [prime gaps, limiting distribution]
sources: []
created: 2026-10-14T22:17:53Z
updated: 2026-10-14T22:17:53Z
---

# What prime-gap statistics would imply

***

Put $d_n=p_{n+1}-p_n$. These are author-recorded comparisons of the target
statements. They do not establish the conjectured prime-gap laws.

## Support is stronger than existence of a distribution

[[problems/primes/E0234/_index|Problem 234]] asks for a continuous limiting
distribution of $d_n/\log n$. If such a distribution $F$ gives positive
mass to every open interval in $(0,\infty)$ and to every interval $(0,b)$,
then every $c\ge0$ is a limit point, as requested by
[[problems/primes/E0005/_index|Problem 5]]. For $c>0$, take arbitrarily
small intervals about $c$ with positive mass; convergence of their frequencies
gives infinitely many indices in each interval. Choose an increasing sequence
of those indices. For $c=0$, use $(0,1/j)$ instead. Since
$\log p_n/\log n\to1$, the normalizations have the same finite limit points.

Continuity alone does not supply full support. The conditional exponential
distribution reported on Problem 234 has it, but its prime-tuple hypothesis
remains unproved. The unconditional positive measure and bounded-gap
properties of the set of limit points do not give full support either.
For example, $\bigcup_{j\ge0}[j,j+1/2]$ is a proper closed subset of
$[0,\infty)$, has measure at least $T/2$ in $[0,T]$, and meets every
interval of length one. This example tests only those two consequences,
not all the stronger combinatorial assertions in
[[../library/primes/merikoski_2020_limit_points_normalized_prime_gaps/_index|Merikoski's paper]].
Its Theorem 1 and Corollaries 2--3 were inspected at statement depth.
The next test for a proposed route is positive limiting mass in an arbitrary
prescribed interval. Stop if the available conclusion only bounds total
measure or gaps in the set of limit points.

## Two half-density inequalities do not prove infinitely many equalities

For [[problems/primes/E0218/_index|Problem 218]], let $A_N$ count
$n\le N$ with $d_{n+1}\ge d_n$, let $B_N$ count those with
$d_{n+1}\le d_n$, and let $E_N$ count equalities. Then
$A_N+B_N=N+E_N$. Thus $A_N/N\to1/2$ and $B_N/N\to1/2$ together imply
$E_N/N\to0$, not $E_N\to\infty$. The numerical sequence alternating
between $2$ and $4$ has both inequality densities $1/2$ and no equality;
this is a logical example, not a prime-gap construction. Marginal
distributions of individual gaps likewise do not determine adjacent pairs.
[[../library/primes/banks_2023_ratios_consecutive_prime_gaps/_index|Banks's
ratio formula]] is presented as a conjecture motivated by a heuristic, not
an unconditional adjacent-gap theorem. A route must supply both the needed
joint distribution and a separate reason for infinitely many exact equalities.

## A second moment still leaves a power-sized distinct run

Let $M_2(N)=\sum_{n\le N}d_n^2$. Cauchy--Schwarz and the prime number
theorem give $M_2(N)\gg N(\log N)^2$, so
[[problems/primes/E0233/_index|Problem 233]] asks for an upper bound of
the correct order. The inspected Theorem 1 of
[[../library/primes/stadlmann_2022_mean_square_gap_between_primes/_index|Stadlmann]]
is instead $\sum_{p_n\le X}d_n^2\ll_\varepsilon X^{1.23+\varepsilon}$.
Changing from prime value $X$ to index $N$ does not remove its excess power.

Even the desired bound would only give a power estimate for the length $H$
of a run of pairwise distinct gaps starting at index $n<x$, the quantity in
[[problems/primes/E0852/_index|Problem 852]]. Distinct positive integers
have sum at least $H(H+1)/2$. The telescoping sum of these gaps is at most
$p_{n+H}\ll(x+H)\log(x+H)$. For large $x$ this first forces $H<x$,
and then $H\ll\sqrt{x\log x}$. The run therefore ends before $2x$.
Its squared gaps have sum at least $\sum_{j=1}^Hj^2\gg H^3$, while the
hypothetical bound for Problem 233 gives $M_2(2x)\ll x(\log x)^2$.
Consequently

$$
H\ll\bigl(x(\log x)^2\bigr)^{1/3}.
$$

This is far above $o(\log x)$. It is a limitation of this direct moment
argument, not a proof that Problem 233 could never help by another method.
A useful next test must exploit local repetition or dependence beyond a
global second moment; stop the bare sum-of-squares route at the displayed bound.

## First occurrences and Problem 853

For a positive even integer $t$, let
$\tau(t)=\min\{n:d_n=t\}$, with $\tau(t)=\infty$ if no such index
exists. For real $y\ge2$ put
$T(y)=\max_{2\le t\le y,\ 2\mid t}\tau(t)$. In the notation of
[[problems/primes/E0853/_index|Problem 853]], $r(x)$ is the least missing
positive even gap among indices $n\le x$. The positivity convention matters:
including zero among candidate gap sizes would make $r(x)$ identically zero.
Exactly

$$
r(x)>y\quad\Longleftrightarrow\quad T(y)\le x.\tag{1}
$$

It follows that $r(x)\to\infty$ is equivalent to every positive even gap
occurring at least once. Infinitely many occurrences of each gap would be
stronger than needed. The stronger requested conclusion is equivalent to

$$
T(y)<\infty\text{ for every }y,\qquad \log T(y)=o(y).\tag{2}
$$

Indeed, if $r(x)/\log x\to\infty$, take $x=\exp(\varepsilon y)$.
Eventually $r(x)>y$, so $T(y)\le\exp(\varepsilon y)$ for every fixed
$\varepsilon>0$. Conversely, fix $K>0$ and use (2) with
$\varepsilon<1/K$. For $y=K\log x$ and all sufficiently large $x$,
$T(y)\le\exp(\varepsilon y)<x$, so (1) gives $r(x)>K\log x$.
Integer rounding changes neither conclusion. This exact interface exposes
the hard step: a subexponential upper bound for the worst first occurrence,
uniform over all even $t\le y$. A fixed-pattern existence theorem with
uncontrolled constants does not supply (2). Stop a proposed deduction if
its threshold still depends ineffectively on each individual $t$.

## Adjacent near-record gaps and Problem 1137

For integer $N\ge2$, define

$$
D_N=\max_{1\le n\le N}d_n,\quad
M_N=\max_{2\le n\le N}d_nd_{n-1},\quad
B_N=\max_{2\le n\le N}\min(d_n,d_{n-1}).
$$

Both factors in every product are bounded by $D_N$, hence

$$
B_N^2\le M_N\le D_NB_N.
$$

Thus [[problems/primes/E1137/_index|Problem 1137]] is equivalent to
$B_N/D_N\to0$. Equivalently, for every $\varepsilon>0$, all sufficiently
large prefixes contain no adjacent pair both at least $\varepsilon D_N$.
The omitted initial undefined product and changing $n<x$ to an integer
prefix have no asymptotic effect. This is a relative isolation assertion.
A lower bound for one large gap, such as Theorem 1 of
[[../library/primes/maynard_2016_large_gaps_between_primes/_index|Maynard's
large-gap paper]], gives no such upper bound for adjacent products. A route
must control the smaller member of every adjacent pair relative to the
running maximum. Stop before inferring isolation from a single-gap
construction, even if that construction substantially increases $D_N$.

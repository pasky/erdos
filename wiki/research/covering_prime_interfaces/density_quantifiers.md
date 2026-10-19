---
name: research/covering_prime_interfaces/density_quantifiers
title: Density, tails and inverse thresholds
desc: Conditioned density tails, exact Jacobsthal inversion, and the gap between fixed sieve density and uniform interval control.
tags: [density, sieve, Jacobsthal function]
sources: []
created: 2026-10-14T22:17:53Z
updated: 2026-10-14T22:17:53Z
---

# Density, tails and inverse thresholds

***

The elementary comparisons here are author-recorded. The linked problem
pages own the standing of imported bounds; no independent source-proof audit
or new acceptance is claimed.

## Multiples and delayed congruences

For [[problems/integer_sequences/E0025/_index|Problem 25]], normalize
$0\le a_i<n_i$ and exclude only $B_i=\{a_i+n_it:t\ge1\}$. Let
$A_K=\mathbb N\setminus\bigcup_{i\le K}B_i$, $A=\bigcap_KA_K$, and
$\delta_K=d(A_K)\downarrow\delta$. Writing
$H_E(X)=\sum_{n\le X,n\in E}1/n$, the exact residual for the proposed
value $\delta$ is

$$
\lim_{K\to\infty}\limsup_{X\to\infty}
\frac{H_{A_K\setminus A}(X)}{\log X}=0.\tag{1}
$$

This follows from $H_A=H_{A_K}-H_{A_K\setminus A}$ and the logarithmic
density $\delta_K$ of each fixed truncation. The converse follows from the
same identity. The
[[research/erdos_25/basic_reductions|existing reduction and proof]] also
explains why universal existence reduces to this candidate-value question.
The ambient union $\bigcup_{i>K}B_i$ is the wrong residual: with zero
classes for all primes it has density one for every $K$. Conditioning on
survival of the prefix is essential. Summable reciprocal moduli and pairwise
coprime moduli are already covered by the existing reduction; they do not
prove (1) for arbitrary translated classes.

For [[problems/integer_sequences/E0691/_index|Problem 691]], put
$M_D=\bigcup_{d\in D}d\mathbb N$ and
$\beta_N=d(M_{D\cap[1,N]})$. The classical multiples theorem identifies
the logarithmic density with $\beta=\sup_N\beta_N$; the logarithmic-density
proof is also given in the linked reduction. Consequently

$$
d(M_D)=1\quad\Longleftrightarrow\quad\sup_N\beta_N=1.\tag{2}
$$

For the forward direction natural density one implies logarithmic density
one. For the reverse direction $\underline d(M_D)\ge\beta_N$ for every
$N$. Each $\beta_N$ can be computed by finite inclusion-exclusion, using
$d(d_1\mathbb N\cap\cdots\cap d_r\mathbb N)=1/\operatorname{lcm}(d_1,\ldots,d_r)$.
This is a known limiting criterion, not a new structural characterization
of the generators. In particular, divergence of $\sum_{d\in D}1/d$
does not suffice: the even generators have divergent reciprocal sum and
their multiples have density $1/2$. A proposed improvement must give a
new effective or structural condition rather than restate (2).

## Covering functions and exact inversion

Let $P(x)=\prod_{p\le x}p$, and let $j(n)$ be the least length such that
every interval of that many consecutive integers contains an integer coprime
to $n$. The maximal covered run has length $j(n)-1$. A choice of residues
$a_p$ covering $1,\ldots,y$ is, by the Chinese remainder theorem, equivalent
to an interval $N+1,\ldots,N+y$ with every member sharing a prime factor
with $P(x)$: choose $N\equiv-a_p\pmod p$. Conversely any such interval
gives these residues. Thus the function of
[[problems/integer_sequences/E0687/_index|Problem 687]] satisfies

$$
Y(x)=j(P(x))-1\le h(\pi(x))-1,
$$

where $h(r)$ is the maximum Jacobsthal function over integers with at most
$r$ distinct prime factors, as in
[[problems/integer_sequences/E0970/_index|Problem 970]]. For fixed $k,x$,
successful starting points $N$ form a periodic set modulo $P(x)$. Existence
is therefore equivalent to positive natural density. This proves the exact
inverse description from
[[problems/integer_sequences/E0929/_index|Problem 929]]:

$$
S(k)=\min\{x:Y(x)\ge k\}.\tag{3}
$$

The already recorded bound $Y(x)\ll x^2/(\log x)^2$ gives
$S(k)\gg\sqrt{k}\log k$. To see the logarithm without assuming an inverse
asymptotic, first $k\ll S(k)^2$ implies
$\log S(k)\ge\tfrac12\log k-O(1)$; then
$\sqrt{k}\ll S(k)/\log S(k)$. Its exponent remains $1/2$.

The stronger questions $Y(x)\le x^{1+o(1)}$ and
$S(k)\ge k^{1-o(1)}$ are equivalent in the usual quantified-exponent sense.
If $Y(x)\le x^{1+\varepsilon}$ eventually, (3) gives
$S(k)\ge k^{1/(1+\varepsilon)}$ eventually. Conversely, putting
$k=Y(x)$ in $S(k)\ge k^{1-\varepsilon}$ gives
$Y(x)\le x^{1/(1-\varepsilon)}$ once $k$ is large. Constants in either
bound can be absorbed into a slightly larger exponent. No quadratic bound
for $h$ yields these stronger exponent-one conclusions. The next useful
test is an improvement of the exponent in the covering bound, not another
inversion of the existing estimate.

## Fixed sieve density does not locate a first hit

For fixed $k$, the integers $n$ for which no $n+i$, $1\le i\le k$, has a
prime divisor in $(k,2k)$ have the exact positive density

$$
\prod_{k<p<2k}\left(1-\frac{k}{p}\right).
$$

Each prime excludes $k$ distinct residues and the Chinese remainder theorem
multiplies their surviving proportions. This addresses the periodic density
in [[problems/integer_sequences/E0451/_index|Problem 451]], not its least
positive successful $n$. A periodic set of positive density can concentrate
its residues in part of a huge period. A first-hit bound requires control
of incomplete periods uniform in $k$.

Likewise the density of a fixed sifted set in
[[problems/integer_sequences/E0688/_index|Problem 688]] does not guarantee
a survivor in the particular interval $[1,n]$ when the prime cutoff and
excluded residues depend on $n$. The elementary covering count supplies a
necessary condition, not a sufficient construction or uniform survivor theorem.
For both problems the discriminating test is the size and uniformity of the
error in the proposed incomplete-period estimate. Stop using a fixed-parameter
density formula as a first-hit argument if that error dominates the main term.

## Moment and prime-product comparisons

Write $s_i$ for the squarefree integers and $\Delta_i=s_{i+1}-s_i$.
If the moment assertion in
[[problems/integer_sequences/E0145/_index|Problem 145]] held for every
$\alpha>0$ with finite limiting constants, its nonnegative summands would
give $\Delta_i^\alpha\ll_\alpha s_i$. For any $\varepsilon>0$, choose
$\alpha>1/\varepsilon$ to obtain $\Delta_i=o(s_i^\varepsilon)$.
This would answer the subpower part of
[[problems/integer_sequences/E0208/_index|Problem 208]], but not a
logarithmic gap estimate. Moments in a fixed bounded range of $\alpha$
give only fixed powers. A claimed distributional limit must also control
the tails of these unbounded powers before this implication is usable.

For [[problems/integer_sequences/E1181/_index|Problem 1181]], let
$k=\lfloor\log n\rfloor$ and let $q$ be the smallest prime dividing none
of $n+1,\ldots,n+k$. Every prime below $q$ divides their product, hence

$$
\vartheta(q^-)\le\log\prod_{i=1}^k(n+i)\le k\log(n+k).
$$

The prime number theorem gives only $q\le(1+o(1))(\log n)^2$.
Obtaining a fixed coefficient smaller than one requires additional uniform
information beyond this product comparison. The Jacobsthal covering problem
does not supply it: there one asks for a small prime in each integer, whereas
here every small prime must occur somewhere in the block.

An upper bound $q=o((\log n)^2)$ for all sufficiently large $n$ would
suffice, for example by taking the required fixed saving to be $c=1/2$.
This differs from improving the coefficient-one bound by only a subleading
amount: $q\le(\log n)^2-r(n)$ with $r(n)=o((\log n)^2)$ need not
give any fixed positive fractional saving.

For the sums of two squares in
[[problems/integer_sequences/E0222/_index|Problem 222]], an elementary
rounding argument gives only a quarter-power gap. If $a=\lfloor\sqrt X\rfloor$
and $b=\lceil\sqrt{X-a^2}\rceil$, then
$0\le a^2+b^2-X\le2\sqrt{X-a^2}+1=O(X^{1/4})$.
This produces a sum of two squares just above any $X$, but does not close
the gap with the much smaller lower-bound scales on the problem page.

Finally, normalize an admissible $k$-tuple by $a_1=0$. Every initial
$j$-tuple remains admissible, so the diameter function in
[[problems/integer_sequences/E1204/_index|Problem 1204]] gives
$a_j\ge A(j)$. Since that problem defines $B(k)$ as a mean, not a sum,

$$
B(k)\ge\frac1k\sum_{j\le k}A(j).
$$

Thus $A(j)\sim j\log j$ would imply
$B(k)\ge(1/2+o(1))k\log k$, matching the upper asymptotic bound recorded
on the problem page. This is a conditional transfer between the two
questions, not a proof of the diameter asymptotic. The hard step is its
leading constant; fixed-size admissibility tests cannot determine it.

A negative answer has a different sufficient interface: for some fixed
$\eta>0$, admissible $k$-tuples with diameter at most
$(1-\eta)k\log k$ for unbounded $k$ would refute $A(k)\sim k\log k$.
Finite tables and second-order refinements do not supply that family.
The problem page's Siegel-zero obstruction is conditional; refuting its
hypothesis merely disables that route and proves neither asymptotic.
An unconditional counterexample family must remain a possible disproof route.

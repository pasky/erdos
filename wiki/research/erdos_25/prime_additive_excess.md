---
name: research/erdos_25/prime_additive_excess
desc: Unbounded finite harmonic excess already for prime moduli, ruling out every rank-only bounded additive comparison.
tags: [obstructions, primes, harmonic-density]
sources: []
created: 2026-09-22T09:25:34Z
updated: 2026-10-14T00:26:52Z
---


# research/erdos_25/prime_additive_excess

***

## Statement: proved

For every $M>0$ there is a finite singleton family of distinct prime
moduli, with the original activation $n\ge q$, and a cutoff $X$,
such that its delayed union $B$ and full periodic union measure
$\beta$ satisfy
$$
 H_B(X)-\beta H_{\lfloor X\rfloor}>M.
 \tag{1}
$$
Thus no finite constant depending only on $\sup\Omega(q)$ can bound
this additive error: even the rank-one constant would be infinite.
This supersedes the remaining small-exponential-rank-error target in
[rank and moment obstructions](rank_and_moment_obstructions.md).

The proof amplifies the checked prime-template construction in
[finite sharp counterexamples](finite_sharp_counterexamples.md).
It uses that note's finite-complexity prime linear-forms theorem, not
an unproved prime-tuple conjecture. The relevant source passages were checked:
Green--Tao,
[*Linear equations in primes*](https://annals.math.princeton.edu/wp-content/uploads/annals-v171-n3-p08-p.pdf),
Lemma 1.6, printed p. 1761, and Main Theorem, p. 1763; and
Green--Tao--Ziegler, [*An inverse theorem for the Gowers
$U^{s+1}[N]$-norm*](https://annals.math.princeton.edu/wp-content/uploads/annals-v176-n2-p11-p.pdf),
Theorem 1.3 and its following application paragraph, printed p. 1235.
All systems of forms and all auxiliary parameters are fixed before
the scale tends to infinity. No growing-complexity uniformity is used.

This is **not** a counterexample to Problem 25. Infinite prime-modulus
systems have natural density by the pairwise-coprime theorem. The
normalized excess in this construction is not bounded away from zero.

## A uniform rough-number harmonic remainder

For an integer $y\ge2$, let
$$
 R_y=\{n\ge1:p\nmid n\text{ for all primes }p\le y\},\qquad
 F_y(x)=H_{R_y}(x),\qquad
 \delta_y=\prod_{p\le y}(1-1/p).
$$
There is an absolute constant $C_0$ such that, for $x\ge1$,
$$
 0\le F_y(x)-\delta_y H_{\lfloor x\rfloor}\le C_0.
 \tag{2}
$$

The elementary [coprime upper sieve](coprime_entropy.md#a-fourier-upper-sieve-for-coprime-composite-moduli)
gives
$$
 |R_y\cap[1,t]|\le C\delta_y t\qquad(t\ge y).
 \tag{3}
$$
Its theorem applies to every pairwise-coprime modulus set in
$[2,\lfloor t\rfloor]$; there is no requirement that $t$ exceed
a fixed power of $y$. Also $R_y\cap[1,y]=\{1\}$.
Partial summation, splitting at $y$ when necessary, gives for $d\ge1$
and $x\ge y$
$$
 F_y(x)-F_y(x/d)
 \le C\delta_y(1+\log d)+\mathbf1_{d>x}.
 \tag{4}
$$
If $x/d\ge y$, integrate (3) between $x/d$ and $x$.
If $1\le x/d<y$, start at $y$, and use
$\log(x/y)\le\log d$. If $d>x$, include the atom at one.

Let $D$ be a random positive $y$-smooth integer with
$\Pr(D=d)=\delta_y/d$. The finite Euler product normalizes this
law. Unique smooth/rough factorization yields
$$
 \mathbb E F_y(x/D)=\delta_y H_{\lfloor x\rfloor},\qquad
 \mathbb E\log D=\sum_{p\le y}\frac{\log p}{p-1}\ll\log(2y).
$$
The Euler expansion gives $\delta_y\le1/H_y\ll1/\log(2y)$.
Average (4) to obtain the upper bound in (2). Its lower bound follows
from $D\ge1$ and monotonicity of $F_y$. For $1\le x<y$,
$F_y(x)=1$ and $0\le\delta_y H_{\lfloor x\rfloor}\le1$,
so (2) also holds there.

## Prime-template amplification

Fix an arbitrary real $K>1$, put $\varepsilon=1/(4K)$, and choose
a finite admissible set $S\subset\mathbb N$ with
$$
 L:=\sum_{t\in S}\log(1+1/t)\ge8K\log4.
$$
The existence of such $S$ is proved in the
[prime-template note](finite_sharp_counterexamples.md#admissible-sets-with-large-harmonic-weight).
Write $T=\max S$. These parameters are now fixed. Let $N$ tend
to infinity through integers, and set

$$
 X=\lfloor N^K\rfloor.
$$

Install the zero class at every prime at most $N$. For every good
prime $q\in(N,X]$, independently retain it with probability
$\varepsilon$, and then choose its residue uniformly among the
prime-pattern shifts $a\in[0,q)$ for which every $a+tq$,
$t\in S$, is prime. Here “good” has exactly the definition and
moment estimates in the prime-template note. Let $A$ be the final
delayed survivor set and $\delta$ its full Haar survivor measure.

The first and second prime moments proved in that note imply that
the expected harmonic mass of deleted target primes in
$((T+1)N,X]$ is at least
$$
 (1-e^{-\varepsilon L/2})\log K+o(1)
 \ge\tfrac34\log K+o(1).
 \tag{5}
$$
Unlike its earlier application, this estimate allows every fixed
$K>1$, not just $K<2$. The old restriction was used only to say
that *all* old survivors were primes. For (5), it suffices that the
target primes are old survivors, which remains true.

For completeness, the moment argument bounds target-prime survival
by $e^{-\varepsilon J_{\rm good}(p)/2}$, where
$J_{\rm good}\to L$ in prime-average $L^1$ on growing dyadic
intervals. Partial summation then sums the errors to $o(1)$ between
$N$ and $N^K$, with $K,S$ fixed. The boundary interval up to
$(T+1)N$ has prime harmonic mass $o(1)$, and the full target
mass is $\log K+o(1)$. Every used hit has
$p=a+tq$ with $t\ge1$, so $p\ge q$: activation is exact.
Thus
$$
 \mathbb E H_A(X)\le F_N(X)-\tfrac34\log K+o(1).
 \tag{6}
$$

All moduli are distinct primes, so their periodic survivor measure is
the product of their individual survivor fractions, independently of
the chosen residues. Consequently
$$
\begin{aligned}
 0\le\delta_N-\mathbb E\delta
 &=\delta_N\left(1-
       \prod_{\substack{N<q\le X\\q\text{ good}}}(1-\varepsilon/q)\right)\\
 &\le\varepsilon\delta_N\sum_{\substack{N<q\le X\\q\text{ prime}}}1/q.
\end{aligned}
$$
Since $\delta_N H_X\le H_X/H_N=K+o(1)$, prime reciprocal
summation gives
$$
 (\delta_N-\mathbb E\delta)H_X
 \le\tfrac14\log K+o(1).
 \tag{7}
$$
Combine (2), (6), and (7):
$$
\begin{aligned}
 \mathbb E[\delta H_X-H_A(X)]
 &\ge-[F_N(X)-\delta_N H_X]
          +\tfrac12\log K+o(1)\\
 &\ge\tfrac12\log K-C_0+o(1).
\end{aligned}
\tag{8}
$$
Given $M$, first choose $K$ making the last main term greater
than $M+1$; next fix $\varepsilon,S$; only then choose $N$
sufficiently large. Some realization has
$\delta H_X-H_A(X)>M$, which is (1).

The finite moduli are singly assigned and can be ordered increasingly.
There is no assertion that the realizations for different $M$ can
be nested while retaining a positive Haar survivor measure. In fact
their old prime sieves have $\delta_N\to0$. The constant normalized
first-kill entropy bound and a uniform additive $o(\log X)$ bound
are not contradicted by this result.

## A related improvement of the preparatory-period restriction

Suppose a finite preparatory sieve has pairwise-coprime moduli, maximum
modulus $N$, full survivor measure $\delta$, and period $P$.
Append moduli $q>N$ coprime to $P$, all with one normalized integer
center $0\le a<\min q$. The appended prepared-block estimates hold
with an absolute constant even though $q$ need not exceed $P$:
$$
 h(X)^2\le C\tau,\qquad
 \sum_{i\text{ appended}}c_i(X)\log_+\frac{c_i(X)}{e_i}
 \le C\delta\log(C/\delta).
 \tag{9}
$$
Here $h$ is total normalized harmonic appended first-kill mass and
$\tau$ its total incremental Haar measure.

Indeed the same coprime upper sieve bounds the full old survivors
below every $t\ge N$ by $C\delta t$. Every appended hit is beyond
$N$, where all old classes are active. Partial summation gives
$h(X)\le C\delta$. Independence gives
$e_i=\delta e_i^0$ and $\tau=\delta\beta_0$, where the superscript
and subscript refer to the appended zero-center system alone.
Center subtraction and the valuation model used in
[prepared-block entropy](prepared_blocks_entropy.md) give
$c_i(X)\le C e_i^0$ and $h(X)\le C\beta_0$. These inequalities
imply both parts of (9). If $\delta=0$, no appended first kills occur.
This removes a period barrier for coprime preparations, not for
arbitrary overlapping preparatory systems.

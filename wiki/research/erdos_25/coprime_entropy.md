---
name: research/erdos_25/coprime_entropy
desc: An absolute first-kill entropy bound for finite pairwise-coprime singleton systems, proved by an elementary Fourier sieve.
tags: [entropy, pairwise-coprime, sieve, partial-results]
sources: []
created: 2026-09-22T05:00:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/coprime_entropy

***

## A simpler unconditioned finite bound

For pairwise-coprime moduli, arbitrary residues, full union measure
$\beta$, and the original activation rule, the exact progression
bound and the CRT product give
$$
 \frac{H_B(X)}{H_{\lfloor X\rfloor}}
 \le\min\left(1,\sum_q\frac1q\right)
 \le\min(1,-\log(1-\beta))
 \le\frac{e}{e-1}\,\beta.
$$
The case $\beta=1$ is immediate. For $\beta<1$, use
$1-\beta=\prod_q(1-1/q)$. The last scalar inequality follows because
$-\log(1-t)/t$ is increasing on $(0,1)$, and split at
$t=1-e^{-1}$. This is an unconditioned weak-type bound, not a proof
of the first-kill entropy theorem below. No corresponding absolute
constant was established for coherent families with overlapping
prime supports.

## Statement and scope

**Proved.** There is an absolute constant $C$ such that every finite
singleton family with pairwise-coprime moduli satisfies
$$
 \sum_i c_i(X)\log_+\frac{c_i(X)}{e_i}\le C
 \qquad(X\ge2).
 \tag{1}
$$
Here the moduli are ordered increasingly, the residues are normalized as
$0\le a_i<q_i$, and
$$
 B_i=\{a_i+tq_i:t\ge1\},\qquad
 E_i=B_i\setminus\bigcup_{j<i}B_j,\qquad
 c_i(X)=\frac1{H_{\lfloor X\rfloor}}
                \sum_{\substack{n\le X\\n\in E_i}}\frac1n.
$$
The quantity $e_i$ is the Haar measure of the full first-kill cell
$$
 F_i=[a_i]_{q_i}\setminus\bigcup_{j<i}[a_j]_{q_j}.
$$
Terms with $c_i=0$ are zero. A modulus $1$ makes the assertion trivial,
so the proof assumes $q_i\ge2$.

The constant is independent of the residues, moduli, family size, cutoff,
and final survivor density. Composite pairwise-coprime moduli are allowed.
This proves the constant entropy target in
[rank and moment obstructions](rank_and_moment_obstructions.md#entropy-of-the-disjoint-potential-an-unresolved-stronger-target)
under pairwise coprimality. It does **not** extend that target to
overlapping prime supports and does not resolve Problem 25. No general
additive harmonic comparison is asserted here.

The main intermediate result is the uniform estimate
$$
 \frac{H_A(X)}{H_{\lfloor X\rfloor}}
 \ll \delta\left(1+\log\frac1\delta\right),
 \qquad X\ge\max_iq_i,
 \tag{2}
$$
where $A=\mathbb N\setminus\bigcup_iB_i$ and
$\delta=\prod_i(1-1/q_i)$. This is an **upper**, not a lower, bound
for harmonic survivor mass.

## Elementary prime estimates

The proof uses
$$
 \vartheta(y):=\sum_{p\le y}\log p\ll y,\qquad
 \pi(y)\ll\frac{y}{\log(2y)},\qquad
 \sum_{p\le y}\frac{\log p}{p}\ll\log(2y),
 \tag{3}
$$
and, with $Z(y)=\prod_{p\le y}(1-1/p)^{-1}$,
$$
 \log(2y)\ll Z(y)\ll\log(2y)\qquad(y\ge2).
 \tag{4}
$$
Here are elementary derivations to make the argument self-contained.
The primes in $(m,2m]$ divide $\binom{2m}{m}\le4^m$; dyadic summation
gives the first estimate in (3). Splitting the primes at $\sqrt y$
then proves the estimate for $\pi(y)$, and partial summation proves the
last estimate in (3).

The expansion of $Z(y)$ contains $1/n$ for every $n\le y$, giving its
lower bound. For the upper bound, set $s=1+1/\log y$. Absolute convergence
of the Euler product for $\zeta(s)$ and (3) give
$$
 \begin{aligned}
 \log Z(y)-\log\zeta(s)
 &\le\sum_{p\le y}(p^{-1}-p^{-s})
       +\sum_p\sum_{k\ge2}\frac1{kp^k}\\
 &\le(s-1)\sum_{p\le y}\frac{\log p}{p}+O(1)
 \ll1.
 \end{aligned}
$$
The double sum converges by comparison with $\sum_{n\ge2}n^{-2}$.
Finally $\zeta(s)\le1+1/(s-1)$ by the integral test, proving (4).

For a finite pairwise-coprime modulus set, put
$$
 \delta(t)=\prod_{q_i\le t}(1-1/q_i).
$$
Assign each modulus a prime divisor $p(q)$. These assigned primes are
distinct. Since $(\log u)/u$ decreases for $u\ge3$, the possible
assigned prime $2$ contributes only an absolute constant, and (3) gives
$$
 \sum_{q_i\le y}\frac{\log q_i}{q_i}\ll\log(2y).
 \tag{5}
$$
Also $q_i\ge p(q_i)$ and (4) imply
$$
 \delta(t)\ge Z(t)^{-1}\gg\frac1{\log(2t)}.
 \tag{6}
$$

For $2\le y\le T$ there is the useful comparison
$$
 \frac{\delta(y)}{\delta(T)}
 \ll\frac{\log(2T)}{\log(2y)}.
 \tag{7}
$$
To prove it, divide the moduli in $(y,T]$ according as their assigned
prime is at most $y$ or greater than $y$. There are at most $\pi(y)\le y$
in the first group, and
$-\log(1-1/q)\le2/q<2/y$, so their product contributes at most $e^2$.
The remaining product is at most
$$
 \prod_{y<p\le T}(1-1/p)^{-1}=Z(T)/Z(y),
$$
which is bounded as claimed by (4).

## A Fourier upper sieve for coprime composite moduli

Let $\mathcal Q$ be any finite pairwise-coprime set of moduli in $[2,N]$,
and let $S\subseteq\{1,\ldots,N\}$ avoid one prescribed full class
$a_q\pmod q$ for every $q\in\mathcal Q$. Write
$\widehat S(\theta)=\sum_{n\in S}\exp(2\pi i n\theta)$.
We will prove
$$
 |S|\ll N\prod_{q\in\mathcal Q}(1-1/q).
 \tag{8}
$$

For a subset $J\subseteq\mathcal Q$, put
$$
 d_J=\prod_{q\in J}q,
 \qquad w_J=\prod_{q\in J}(q-1)^{-1},
 \qquad
 \mathcal F_J=\left\{\sum_{q\in J}\frac{j_q}{q}\pmod1:
                                    1\le j_q<q\right\}.
$$
Empty products give $d_\varnothing=w_\varnothing=1$ and
$\mathcal F_\varnothing=\{0\}$. Pairwise coprimality implies that the
characters in each $\mathcal F_J$ are distinct, and that the frequency
sets for different $J$ are disjoint: their nonzero CRT coordinate
supports are different. Every frequency in $\mathcal F_J$ has reduced
denominator dividing $d_J$.

For every $n\in S$,
$$
 \prod_{q\in J}\sum_{j=1}^{q-1}
       \exp\bigl(2\pi i j(n-a_q)/q\bigr)=(-1)^{|J|}.
$$
Expand, sum over $n\in S$, and apply Cauchy--Schwarz. All phase
coefficients have modulus one, so
$$
 \sum_{\theta\in\mathcal F_J}|\widehat S(\theta)|^2
 \ge w_J|S|^2.
 \tag{9}
$$

Take $R=N^{1/4}$ and retain $J$ with $d_J\le R$. The resulting frequency
set has circular separation at least $R^{-2}$. For completeness, an
elementary large-sieve estimate sufficient here is
$$
 \sum_\theta\left|\sum_{n=1}^N b_n\exp(2\pi i n\theta)\right|^2
 \ll (N+R^2\log(2R))\sum_{n=1}^N|b_n|^2.
 \tag{10}
$$
Indeed, the Gram matrix on the frequency side has entries
$\sum_{n=1}^N\exp(2\pi i n(\theta-\phi))$, of absolute value at most
$\min(N,1/(2\|\theta-\phi\|))$. Separation bounds each off-diagonal
absolute row sum by $O(R^2\log(2R))$, by summing the reciprocal distances
in order away from the diagonal. The diagonal entry is $N$. The
row-sum bound for the Hermitian matrix, followed by finite-dimensional
duality, proves (10).

Since $R^2\log(2R)\ll N$, summing (9) and applying (10) with
$b_n=\mathbf1_S(n)$ gives
$$
 G(R)|S|^2\ll N|S|,
 \qquad
 G(R)=\sum_{J:d_J\le R}w_J.
 \tag{11}
$$

It remains to lower-bound $G(R)$. Fix a sufficiently small absolute
$\eta>0$ and set $y=N^\eta$. Expanding
$$
 W_y:=\prod_{\substack{q\in\mathcal Q\\q\le y}}
             \left(1+\frac1{q-1}\right)=\delta(y)^{-1}
$$
and normalizing the subset weights makes each $q\le y$ present
independently with probability $1/q$. The associated random product $D$
therefore satisfies, by (5),
$$
 \mathbb E\log D=\sum_{\substack{q\in\mathcal Q\\q\le y}}
                         \frac{\log q}{q}\ll\log(2y).
$$
Choose $\eta$ so small that, for all sufficiently large $N$,
this expectation is at most $\tfrac18\log N=\tfrac12\log R$.
Markov's inequality gives $\Pr(D\le R)\ge1/2$, whence
$$
 G(R)\ge\tfrac12\delta(y)^{-1}\gg\delta(N)^{-1}
$$
by (7), since $\eta$ is fixed. Equations (11) and (6), enlarging the
absolute constant to handle bounded $N$, prove (8).

## Delayed counting and harmonic survivors

For the original delayed family, its survivors up to $N$ are unchanged
if moduli exceeding $N$ are discarded. Compared with the full sieve
using $q_i\le N$, a delayed survivor can only be one of the protected
positive roots $a_i<q_i$. There are at most as many such roots as active
moduli, hence at most $\pi(N)$ by the assignment of distinct prime
divisors. Equations (3), (6), and (8) therefore give
$$
 |A\cap[1,N]|\ll N\delta(N).
 \tag{12}
$$
This bound is uniform in the entire finite family and in $N$; it is not
an asymptotic formula.

Now suppose all moduli are at most $Q$, and put $\delta=\delta(Q)$.
For $2\le t\le Q$, (7) and the trivial bound $\delta(t)\le1$ give
$$
 \delta(t)\ll
 \min\left(1,\frac{\delta\log(2Q)}{\log(2t)}\right).
 \tag{13}
$$
For $t\ge Q$, $\delta(t)=\delta$. By partial summation, (12), and
(13), for $X\ge Q$,
$$
 H_A(X)\ll
 1+\delta\bigl(1+\log(X/Q)\bigr)
 +\delta\log(2Q)\left(1+\log\frac1\delta\right).
 \tag{14}
$$
The integral used here, after setting $u=\log(2t)$, is bounded by
$$
 \int_0^L\min(1,aL/u)\,du
 \ll L a\bigl(1+\log(1/a)\bigr)\qquad(0<a\le1).
$$
If the constant multiple of $\delta$ in (13) exceeds one, the trivial
integral bound $L$ gives the same conclusion after adjusting constants.
The initial constant in (14) is absorbed by
$\delta\log(2Q)\gg1$, from (6). Division by $H_{\lfloor X\rfloor}$
proves (2). An empty family has survivor mass one and satisfies (2)
with $\delta=1$.

## Entropy by integrating the first-kill tail

Discard moduli exceeding $X$: their $c_i(X)$ are zero, and this does not
change the earlier first-kill cells or densities. Thus every remaining
prefix has largest modulus at most $X$. Set
$$
 \delta_j=\prod_{i\le j}(1-1/q_i),\qquad
 \delta_0=1,\qquad t_i=-\log\delta_{i-1}.
$$
CRT independence gives
$$
 e_i=\frac{\delta_{i-1}}{q_i}.
$$
The elementary delayed progression estimate gives
$$
 c_i(X)\le\frac{H_{\lfloor X/q_i\rfloor}}
                    {q_iH_{\lfloor X\rfloor}}\le\frac1{q_i},
 \qquad
 \log_+\frac{c_i(X)}{e_i}\le t_i.
 \tag{15}
$$

For $u\ge0$, if there is an $i$ with $t_i>u$, let $i_0$ be the first
such index. The first kills with $t_i>u$ are disjoint and are all
survivors of the prefix ending at $i_0-1$. Apply (2) to that prefix:
$$
 \sum_{i:t_i>u}c_i(X)
 \ll e^{-t_{i_0}}(1+t_{i_0})
 \le e^{-u}(1+u),
 \tag{16}
$$
where the final inequality uses that $e^{-t}(1+t)$ is decreasing for
$t\ge0$. If there is no such index, the sum is zero. Integrating (16)
and using (15) proves
$$
 \sum_i c_i(X)\log_+\frac{c_i(X)}{e_i}
 \le\sum_i c_i(X)t_i
 =\int_0^\infty\sum_{i:t_i>u}c_i(X)\,du
 \ll\int_0^\infty e^{-u}(1+u)\,du\ll1.
$$
This is (1).

As a consequence, for any selection $J$ of first-kill cells, writing
$\alpha=\sum_{i\in J}c_i(X)$ and $\tau=\sum_{i\in J}e_i$, the log-sum
inequality gives
$$
 \alpha\log(\alpha/\tau)\le C.
$$
Thus their harmonic mass tends to zero uniformly whenever their total
Haar mass tends to zero. This recovers conditioned-tail control in the
pairwise-coprime setting; the existence of natural density in that
setting was already established by the simpler argument in
[basic reductions](basic_reductions.md).

## Why the proof does not cover overlapping moduli

Two uses of pairwise coprimality are essential here. In (9)--(11), it
makes the character blocks for different products disjoint. In (15), it
gives the exact identity $e_i=\delta_{i-1}/q_i$. For general distinct
moduli, a conditional first-kill density can be arbitrarily smaller than
the global previous survivor density divided by $q_i$. Neither step has
been replaced by a valid general argument.

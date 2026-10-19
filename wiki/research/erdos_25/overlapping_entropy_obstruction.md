---
name: research/erdos_25/overlapping_entropy_obstruction
desc: Zero-residue first-kill masses produce overlapping potentials that are not uniformly integrable.
tags: [entropy, obstructions, first-kill-measures]
sources: []
created: 2026-09-22T08:29:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/overlapping_entropy_obstruction

***

The [moment obstructions](rank_and_moment_obstructions.md) rule out
fixed higher-moment bounds for an overlapping potential. The following
strengthening also rules out uniform integrability, including every
superlinear Orlicz bound. It does **not** refute the disjoint first-kill
entropy target and is not a counterexample to Problem 25.

For a finite singleton system, let $F_q$ be its full first-kill cells,
$e_q=\mu(F_q)$, and
$c_q(X)=H_{E_q}(X)/H_{\lfloor X\rfloor}$. Consider on Haar space
$$
 Z_X(z)=\sum_q q c_q(X)\mathbf1_{[a_q]_q}(z).
$$
There are zero-residue systems and cutoffs $X=X_k$ such that, for a
fixed $\gamma>0$,
$$
 \liminf_{k\to\infty}
 \int_{\{Z_{X_k}\ge e^{\gamma k}\}} Z_{X_k}\,d\mu
 \ge\frac12.
 \tag{1}
$$
In particular $\int Z_{X_k}\log_+ Z_{X_k}\,d\mu\gg k$.

## Construction and the first-kill formula

Choose a finite set $P$ of primes exceeding $k^3$, stopping when
$$
 \lambda:=\sum_{p\in P}p^{-1}=2k+O(k^{-3}).
$$
Then $\sum_{p\in P}p^{-2}=O(k^{-2})$. Take every product of $k$
distinct primes from $P$ as a modulus, with residue zero, and order
these products numerically. Put $L=\prod_{p\in P}p$ and $X=L^2$.
These moduli are distinct and primitive. Every positive multiple of
a modulus is active, so $E_q=F_q\cap\mathbb N$ exactly.

Each cell is $L$-periodic with exactly $e_qL$ points in every block
of $L$ consecutive positive integers. In the $j$th such block,
each reciprocal is at least $1/(jL)$. Therefore
$$
 H_{E_q}(L^2)\ge e_qH_L,
 \qquad c_q(L^2)\ge e_q/2,
 \tag{2}
$$
using $H_{L^2}\le2H_L$. The latter inequality follows, for example,
by bounding the $j$th block after the first in $H_{mn}$ by
$1/(j-1)$, which gives $H_{mn}\le H_m+H_n$.

Define
$$
 Y=\frac12\sum_q qe_q\mathbf1_{q\mid z}\le Z_X,
 \qquad \beta=\sum_qe_q.
$$
If $N_P$ counts the dividing primes of $P$ in a Haar integer, then
$\beta=\Pr(N_P\ge k)=1-O(k^{-1})$, by Chebyshev, since
$\mathbb E N_P=2k+O(k^{-3})$ and
$\operatorname{Var}N_P\le\mathbb E N_P$. Thus
$$
 \mathbb EY=\beta/2\longrightarrow1/2.
 \tag{3}
$$

For a modulus $q$, write $u(q)=\max_{p\mid q}p$ and
$T(q)=\sum_{p\in P,\ p\le u(q)}1/p$.
The least numerical $k$-prime product dividing a Haar integer consists
of its $k$ smallest dividing pool primes. Consequently
$$
 qe_q=\prod_{\substack{p\in P,\ p<u(q)\\p\nmid q}}(1-1/p).
 \tag{4}
$$
If $q$ has law $e_q/\beta$, it is that first product conditional on
$N_P\ge k$. Therefore
$$
 \Pr(0.9k\le T(q)\le1.1k)=1-O(k^{-1}).
 \tag{5}
$$
Indeed, a first product before reciprocal time $0.9k$ requires at
least $k$ successes in a prime prefix of mean at most $0.9k$.
A first product after time $1.1k$ requires fewer than $k$ successes
in a prefix of mean $1.1k+O(k^{-3})$ (or one with mean just below
that threshold). Both probabilities are $O(1/k)$ by Chebyshev;
conditioning costs a factor $1/\beta=1+O(1/k)$.

## Size bias and concentration

The size-biased probability $d\nu=Y\,d\mu/\mathbb EY$ can be sampled
by choosing $q$ with probability $e_q/\beta$ and then choosing a
Haar integer conditional only on $q\mid z$, not on $F_q$.
Its density is exactly
$\sum_q(e_q/\beta)q\mathbf1_{q\mid z}=2Y/\beta$.

For the chosen $q$, let $N_q$ count dividing pool primes at most
$u(q)$. Under this conditional Haar law,
$$
 N_q=k+\sum_{\substack{p\in P,\ p\le u(q)\\p\nmid q}}
                    \mathbf1_{p\mid z},
$$
with independent Bernoulli terms. When (5) holds,
$$
 \mathbb E(N_q\mid q)\ge1.9k-k^{-2},
 \qquad \operatorname{Var}(N_q\mid q)\le1.1k.
$$
Another application of Chebyshev gives
$\Pr(N_q\ge1.8k\mid q)=1-O(1/k)$, uniformly over these $q$.

Every $k$-product $r$ of these dividing primes is among our moduli,
and (4) gives
$$
 re_r\ge\prod_{\substack{p\in P\\p\le u(q)}}(1-1/p)
       \ge e^{-T(q)-O(k^{-2})}.
$$
It follows, with $\nu$-probability $1-O(1/k)$, that
$$
 Y\ge\frac12e^{-1.1k-O(k^{-2})}
            {\lfloor1.8k\rfloor\choose k}.
$$
Stirling's formula gives
$$
 \log {\lfloor1.8k\rfloor\choose k}
 =(1.8\log1.8-0.8\log0.8)k+O(\log k),
$$
whose linear coefficient exceeds $1.1$. Hence, with
$\gamma=1/20$, for all sufficiently large $k$,
$$
 \nu(Y\ge e^{\gamma k})=1-O(1/k),
 \qquad
 \int_{\{Y\ge e^{\gamma k}\}}Y\,d\mu\longrightarrow1/2.
$$
Since $Y\le Z_X$, this proves (1).

If $\Phi$ is convex and increasing, $\Phi(0)=0$, and
$\Phi(t)/t\to\infty$, then $\Phi(t)/t$ is nondecreasing and (1)
implies $\int\Phi(Z_{X_k})\,d\mu\to\infty$ as well.

The distinction from the disjoint potential is essential. In these
zero-residue examples, the geometric valuation model gives
$c_q(X)\le (Z_X^{\rm Euler}/H_X)e_q\ll e_q$, where
$Z_X^{\rm Euler}=\prod_{p\le X}(1-1/p)^{-1}$.
Thus $\sum_q(c_q/e_q)\mathbf1_{F_q}$ is uniformly bounded.
Replacing these disjoint cells by the cylinders loses precisely the
information needed by the still-unproved entropy argument.

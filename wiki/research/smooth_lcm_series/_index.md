---
name: research/smooth_lcm_series
title: Two-prime running-lcm series
desc: |
  Factorization of the running-lcm reciprocal series for two primes into
  Hecke–Mahler values, with the exact Bugeaud–Laurent theorem specialization
  and the unresolved case of larger prime sets.
tags: []
sources: []
problems: [269]
created: 2026-10-14T20:10:13Z
updated: 2026-10-18T03:07:19Z
---

# Two-prime running-lcm series

[[research/_index|..]]

***

For [[problems/irrationality/E0269/_index|Problem 269]], the case of two primes
follows from Bugeaud and Laurent's Theorem 1.1 in
[[../library/irrationality/bugeaud_2022_transcendence_continued_fraction_hecke_mahler/_index|their
2022 Hecke–Mahler paper]]. The deduction below is author-recorded and imports
that theorem as a source result. Its exact statement and series normalization
have been inspected in the primary TeX; its proof has not been independently
examined. This is a partial result and supplies no conclusion for three or more
primes.

Let $P$ be a finite set of primes, including the smooth integer $1$ in the
increasing enumeration. At a smooth cutoff $m$, the running lcm equals

$$
D(m)=\prod_{p\in P}p^{\lfloor\log_p m\rfloor}.
$$

Every earlier smooth integer divides this product. Conversely each maximal prime
power in the product occurs by the cutoff, so every displayed factor is
required. In particular, each smooth integer contributes its own term, including
cutoffs at which the lcm does not change.

Now let $P=\{p,q\}$ with $p<q$, and put

$$
\theta=\frac{\log p}{\log q},\qquad x=p^{-1},\qquad y=q^{-1}.
$$

Here $0<\theta<1$ is irrational: a rational slope would equate positive powers
of the two different primes. At $m=p^i q^j$ one has

$$
D(m)=p^{i+\lfloor j/\theta\rfloor}
      q^{j+\lfloor i\theta\rfloor}.
$$

Therefore the full series factors as

$$
S_P=AB,\qquad
A=\sum_{i\ge0}x^i y^{\lfloor i\theta\rfloor},\qquad
B=\sum_{j\ge0}y^j x^{\lfloor j/\theta\rfloor}.
$$

All terms are positive and the two factors are bounded by convergent geometric
series, so the factorization preserves both convergence and multiplicity. Define
the source's Hecke–Mahler series at intercept zero by

$$
F_\theta(x,y)=\sum_{i\ge1}\sum_{j=1}^{\lfloor i\theta\rfloor}x^iy^j.
$$

Summing the inner geometric progression gives

$$
F_\theta(x,y)=\frac{y}{1-y}\left(\frac1{1-x}-A\right).
$$

Because the slope is irrational, the positive lattice points partition into
$j<i\theta$ and $i<j/\theta$. The corresponding double series sum to
$xy/((1-x)(1-y))$. Applying the same geometric identity to the second region and
rearranging yields

$$
y(1-x)A+x(1-y)B=x+y-xy.
$$

Thus $B$ is an affine function of $A$ with nonzero rational slope, and $AB$ is a
nonconstant quadratic polynomial in $A$ with rational coefficients. If $AB$ were
algebraic, this polynomial relation would make $A$ algebraic over the algebraic
numbers, hence algebraic over $\mathbb Q$. Consequently transcendence of
$F_\theta(x,y)$ implies transcendence of $A$ and then of $S_P$. For $p=2,q=3$,
the relation simplifies to $A+2B=4$.

Bugeaud–Laurent, arXiv:2203.12901v1, Section 1, Theorem 1.1, treats
$F_{\theta,\rho}(\beta,\alpha)$ with irrational $\theta\in(0,1)$,
$\rho\in[0,1)$, and nonzero algebraic $\alpha,\beta$. Its hypotheses for this
value are $\beta\ne1$, $|\beta|<1$ and $|\beta\alpha^\theta|<1$. Setting

$$
\rho=0,\qquad\beta=1/p,\qquad\alpha=1/q
$$

meets all of them, since $\beta\alpha^\theta=p^{-2}<1$. The theorem therefore
gives the transcendence needed in the preceding argument. No assumption that
$\theta$ is algebraic, has bounded partial quotients, or has unbounded partial
quotients is required by the numbered theorem.

The [public account of Problem
269](https://wcook04.github.io/plectis/maths/problems/erdos_269.html) credits
Steve Fan with the two-prime factorization and conclusion in a forum post of 26
June 2026. The post is quoted and read on
[[problems/irrationality/E0269/claims/2026_06_26_fan|its claim page]], and no
novelty is asserted here.
The stated Hecke–Mahler source is from 2022, so this is a source-supported
partial deduction identified in a later problem discussion, not a new theorem
for all finite prime sets.

For three or more primes, the prime exponents contain floors of sums of several
logarithmic terms. The displayed separation into two one-variable series no
longer follows. A further application needs an exact higher-dimensional identity
and a transcendence theorem with matching hypotheses; the two-prime result alone
supplies neither. That is the next source-fit question, with failure to obtain
such an identity the stopping point for this route.

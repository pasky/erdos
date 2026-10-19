---
name: research/erdos_940/quartic_universal_selector
title: A single prime selector for the quartic complement
desc: A checked universal selector gives compatible growing progressions and another completion of the quartic theorem.
tags: []
sources: []
created: 2026-09-23T00:35:02Z
updated: 2026-09-23T00:37:30Z
---


# A single prime selector for the quartic complement

***

## Status and comparison

The proposed completion in Sections 4–5 and Appendix E of
[third independent record](independent/quartic_analytic_architecture.md)
is valid. The checks below supply the simultaneous quantifiers and a
single summable majorant. This proves the **already established**
[quartic complement theorem](quartic_complement.md), not a new target case.

Unlike the [finite random omission proof](quartic_random_omission.md),
this construction fixes one infinite prime set that works for every
coefficient tuple and every cutoff interval. Above a deterministic
small-prime cutoff, it uses only selected primes congruent to $3\pmod4$;
it does not retain all split primes up to the upper cutoff. The resulting
progressions can be chosen compatible and nested. Neither nesting nor
their vanishing relative representation means proves global density zero.

## 1. The universal selector

For positive squarefree $D$, let $\chi_D$ be the quadratic character of
$\mathbb Q(\sqrt D)$, with $\chi_1=1$. Choose fixed positive numbers
$\lambda_E$, indexed by squarefree $E>1$, satisfying

$$
\Lambda=\sum_E\lambda_E<\tfrac12,
\qquad \sum_E\lambda_E\log(2E)<\infty;
$$

for example $\lambda_E=1/(4E^2)$. On primes $p\equiv3\pmod4$, choose
independent Bernoulli variables $B_p$ of means

$$
g(p)=\delta\left(1-\sum_E\lambda_E\chi_E(p)\right),
\qquad 0<\delta\le\tfrac14.
\tag{1}
$$

These means lie strictly between zero and one.

**Lemma.** For every $\theta>0$, sufficiently small $\delta>0$ admits a
single realization $\mathcal P=\{p:B_p=1\}$ such that, for every squarefree
$D>1$ and every $3\le Z<T$,

$$
P_D(Z,T):=\prod_{\substack{Z<p\le T\\p\in\mathcal P}}
\left(1+\chi_D(p)(p^{-1}-p^{-2})\right)\ll_\theta D^\theta.
\tag{2}
$$

For each fixed $D>1$, this same product tends to zero whenever
$\log\log T-\log\log Z\to\infty$.

**Proof.** Put

$$
M_D(X)=\sum_{\substack{p\le X\\p\equiv3\ (4)}}
\frac{(B_p-g(p))\chi_D(p)}p,
\qquad V=\sum_{p\equiv3\ (4)}p^{-2}<\infty.
$$

Each independent centered increment lies in an interval of length at
most $1/p$. Hoeffding's exponential bound and the maximal inequality for
the resulting nonnegative supermartingale give

$$
\Pr\{\sup_X|M_D(X)|>u\}\le2\exp(-2u^2/V).
\tag{3}
$$

For clarity, the exponential process with exponent
$tM_D(X)-t^2\sum_{p\le X,\ p\equiv3\ (4)}p^{-2}/8$ is a supermartingale.
At the first crossing of $M_D(X)$ above $u$, its value is at least
$\exp(tu-t^2V/8)$; optimize at
$t=4u/V$ and apply the same argument to $-M_D$.

For any $\eta>0$, the sum over integers $D\ge1$ of the right side of
(3) with $u=K+\eta\log(2D)$ converges and tends to zero as $K\to\infty$.
The union bound therefore supplies one realization satisfying

$$
\sup_X|M_D(X)|\le K_\eta+\eta\log(2D)
\quad\text{for every squarefree }D\ge1.
\tag{4}
$$

Interval discrepancies are at most twice this bound. Convergence of
$M_D(X)$ is not needed.

The [two-sided quadratic harmonic bound](quadratic_prime_harmonics.md)
gives, uniformly over intervals, $O(\log(2D))$ for $\chi_D$ on
$p\equiv3\pmod4$ when $D>1$, and $O(\log(2DE))$ for
$\chi_D\chi_E$ when $E\ne D$. Indeed multiply each character by
$(1-\chi_{-4})/2$; neither constituent is principal. For $E=D$,

$$
\sum_{\substack{Z<p\le T\\p\equiv3\ (4)}}\frac{\chi_D(p)^2}p
=\tfrac12(\log\log T-\log\log Z)+O(\log(2D)).
$$

The error accounts also for primes dividing $D$.

Expand (1) and use
$\log(1+\chi_D(p)(p^{-1}-p^{-2}))=\chi_D(p)/p+O(p^{-2})$.
The infinite mixture of nonprincipal interval sums is absolutely bounded
by $C\sum_E\lambda_E\log(2DE)$. Equations (1) and (4) thus give

$$
\log P_D(Z,T)
=-\frac{\delta\lambda_D}{2}(\log\log T-\log\log Z)
+O\bigl(1+K_\eta+(\delta+\eta)\log(2D)\bigr),
\tag{5}
$$

with an absolute implied constant depending only on the fixed weights.
Alternatively, for an upper bound discard the nonpositive diagonal
correlation before estimating the other terms. This yields
$P_D(Z,T)\ll_{\delta,\eta}(2D)^{C\delta+2\eta}$.
Choose $\eta$, then $\delta$, sufficiently small to prove (2).
For fixed $D$, (5) proves the claimed decay. $\square$

## 2. Uniform assembly over all canonical tuples

Use the notation of the omission proof: $P=\prod_i d_i$,
$R=\operatorname{rad}(P)$, $D=\operatorname{sf}(P)$, $w(\mathbf d)=P^{-1/4}$,
and $d_i\in\mathcal C_4$. Regular and exceptional mean exactly the classes in
the [principal-character elimination
lemma](quartic_complement.md#2-elimination-of-the-principal-character-cases).
Take $Z=(\log T)^{400}$, for sufficiently large $T$ that $3<Z<T$, and prescribe

$$
M_T=16\prod_{p\in\mathcal Q_T}p^2,
\quad a_T\equiv8\pmod{16},\quad a_T\equiv p\pmod{p^2},
\qquad
\mathcal Q_T=\{p\le Z:p\text{ odd prime}\}
\cup\{p\le T:p\in\mathcal P\}.
\tag{6}
$$

Let $\rho_T(\mathbf d)$ be the solution count modulo $M_T$, divided
by $M_T^3$.

For regular tuples, the [radical baseline](quartic_euler_majorant.md)
and the bad-prime bound give

$$
\prod_{2<p\le Z}\rho_{p^2}(p;\mathbf d)
\ll_\epsilon4^{\omega(R)}R^\epsilon.
$$

At a good selected prime above $Z$, the local factor is
$1+\chi_D(p)(p^{-1}-p^{-2})-p^{-3}$, at most the factor in (2).
Deleting coefficient primes from (2) costs at most
$(9/7)^{\omega(R)}$, since each of its factors is at least $7/9$.
Actual bad-prime factors are at most four. Including the dyadic factor,

$$
\rho_T(\mathbf d)\ll C^{\omega(R)}R^{\epsilon+\theta}
\qquad(\mathbf d\text{ regular}),
\tag{7}
$$

using $D\mid R$. Choose $\epsilon+\theta<1/8$. For each fixed regular
tuple, eventually all coefficient primes lie below $Z$, and (5) makes
$\rho_T(\mathbf d)\to0$.

Every fixed exceptional tuple is eventually eliminated. Uniformly in
all tuples, the trace bound $|A_p|\le21$ and the bad-prime estimate give

$$
\rho_T(\mathbf d)\ll4^{\omega(R)}(\log T)^{21}.
$$

A surviving exceptional tuple has a coefficient prime greater than $Z$,
so $R>Z$ and $(\log T)^{21}=Z^{21/400}\le R^{1/8}$.
Thus (7), with exponent $1/8$, is a common majorant for both classes.
The Euler product

$$
\sum_{\mathbf d\in\mathcal C_4^4}w(\mathbf d)C^{\omega(R)}R^{1/8}
<\infty
$$

converges: its nonconstant prime term is $O_C(p^{-9/8})$.
Dominated convergence proves

$$
\sum_{\mathbf d}w(\mathbf d)\rho_T(\mathbf d)\longrightarrow0.
\tag{8}
$$


Now choose one finite $T$, then fix $M_T,a_T$ before sending $X$ to infinity.
The
[established lattice transfer](quartic_complement.md#1-canonical-coefficients-and-summable-weights),
with summable majorant $M_Tw(\mathbf d)$, turns (8) into arbitrarily small
progression representation means. At most three summands contribute $O(X^{3/4})$
values. This proves the quartic theorem again.

Finally, both sets on the right of (6) increase with $T$. Hence the
moduli divide one another and the residues are compatible. Their
progression densities tend to zero, so this additional nesting supplies
no density-zero conclusion for $S_4$ or extension to $r\ge5$.

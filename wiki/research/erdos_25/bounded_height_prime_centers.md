---
name: research/erdos_25/bounded_height_prime_centers
desc: Full arithmetic capped-square tails for moderately many bounded-height smaller-part centers at each prime; conditional digit transfer is still missing.
tags: [prime-filtration, partial-results, divisor-bounds]
sources: []
created: 2026-09-22T16:03:00Z
updated: 2026-10-14T00:26:52Z
---


# research/erdos_25/bounded_height_prime_centers

***

This proves a subclass of the arithmetic square-tail target in
[capped prime fractions](capped_prime_fractions.md), including the middle prime
range that note leaves uncontrolled. It does **not** prove logarithmic density:
the survivor-conditioned digit transfer remains a separate issue. Indeed,
the [full-survivor trace obstruction](full_survivor_trace_obstruction.md)
shows that a transfer using the infinite survivor marginals cannot follow
just from such square bounds and bounded weights.

## A finite interval estimate

For distinct singleton moduli, write $q=p^em$, where
$P^+(m)<p$, and retain the original activated fraction
$$
 \alpha_p(n)=\mu_p\!\left(
  \bigcup_{\substack{q=p^em\le n\\n\equiv a_q\ (m)}}
             [a_q]_{p^e}\right).
$$
Here $P^+(1)=1$. On $I_N=(N,2N]\cap\mathbb N$, suppose that
for each prime $p$ there is a set of integer centers
$\mathcal B_{p,N}$, with
$$
 |\mathcal B_{p,N}|\le R_N,\qquad |b|\le B_N
       \quad(b\in\mathcal B_{p,N}),
 \tag{1}
$$
such that every selected $p^em\le2N$ satisfies
$a_q\equiv b\pmod m$ for some $b\in\mathcal B_{p,N}$.
The choice may depend on $q$, and the forbidden $p$-adic digits
are unrestricted. Centers for different primes need not agree.

Put
$$
 D_N=\max_{1\le t\le 2N+B_N}d(t),
$$
where $d(t)$ is the divisor-counting function. Uniformly in all the
data and in $Y\ge2$,
$$
 \frac1N\sum_{N<n\le2N}\sum_{p>Y}\alpha_p(n)^2
 \ll \frac{R_N^2D_N^2}{Y\log(2Y)}
       +\frac{R_N}{\sqrt N\log(2N)}.
 \tag{2}
$$

**Proof.** If $n\notin\mathcal B_{p,N}$, every matching smaller
part $m$ divides one of the nonzero integers $n-b$. For each
exponent $e$, there are consequently at most $R_ND_N$ matching
smaller parts. Singleton distinctness gives
$$
 \alpha_p(n)\le\sum_{e\ge1}p^{-e}R_ND_N
                 =\frac{R_ND_N}{p-1}.
 \tag{3}
$$
At a center itself, use the cap and activation instead. For fixed
$e$, activation permits at most $\lfloor2N/p^e\rfloor$ smaller
parts, so
$$
 \alpha_p(n)\le
 \min\left(1,\sum_{e\ge1}p^{-e}\lfloor2N/p^e\rfloor\right)
 \le\min\left(1,\frac{2N}{p^2-1}\right).
 \tag{4}
$$
For each prime there are at most $R_N$ exceptional integers.
Chebyshev's prime-counting upper bound and partial summation give
$$
 \sum_{p>Y}\frac1{(p-1)^2}\ll\frac1{Y\log(2Y)},
 \qquad
 \sum_p\min\left(1,\frac{4N^2}{(p^2-1)^2}\right)
                 \ll\frac{\sqrt N}{\log(2N)}.
$$
For the second inequality, split at $2\sqrt N$; above it use
$\sum_{p>Z}p^{-4}\ll1/(Z^3\log(2Z))$.
Summing (3)--(4) proves (2). In particular, repeated powers of the
largest prime cause no additional exception. $\square$

## A full square-tail theorem

For sufficiently large $N$, set
$$
 L_N=\frac{\log N\,\log\log\log N}{\log\log N}.
$$
Suppose (1) holds for every sufficiently large dyadic $N$, with
$$
 B_N\le N^C,\qquad R_N\le\exp(\kappa L_N),
 \qquad C\ge1,\quad 0\le\kappa<\frac14
 \tag{5}
$$
fixed. Then, for $K\ge60$, the full activated fractions satisfy
$$
 \limsup_{X\to\infty}\frac1{H_{\lfloor X\rfloor}}
     \sum_{n\le X}\frac1n\sum_{p>K}\alpha_p(n)^2
 \le T_K,\qquad T_K=\sum_{p>K}U_p\longrightarrow0,
 \tag{6}
$$
where
$$
 U_p=\frac1{(p-1)^2}
       \prod_{\ell<p}\frac{1+1/\ell}{(1-1/\ell)^2}
       \ll\frac{\log^3(2p)}{p^2}.
$$
The product is over primes. Formula (6) concerns harmonic averages,
not logarithmic density of the original survivor set.

For completeness, the needed elementary maximal-divisor bound is
$$
 \log\max_{t\le Z}d(t)\ll\frac{\log Z}{\log\log Z}.
 \tag{7}
$$
To prove it, separate prime factors at $y=\sqrt{\log Z}$. There
are at most $y$ small primes, each exponent is at most
$\log Z/\log2$, and their contribution to $\log d(t)$ is
$O(\sqrt{\log Z}\log\log Z)$. The sum of the exponents at
larger primes is at most $\log Z/\log y$; use
$e+1\le2^e$ for their contribution. This proves (7).

Under (5), (7) gives $\log D_N=o(L_N)$. Choose
$2\kappa<c<1/2$ and use (2) at
$Y=\exp(cL_N)$. Its first term is at most
$\exp(-(c-2\kappa+o(1))L_N)$, and its second tends to zero
because $R_N=N^{o(1)}$. Thus the primes above this cutoff have
vanishing interval mean, and hence vanishing harmonic mass on $I_N$.

For the remaining primes, the optimized small-prime proof in
[capped prime fractions](capped_prime_fractions.md#an-optimized-small-prime-cutoff)
gives, on the same dyadic interval, the bound
$$
 \sum_{N<n\le2N}\frac1n
    \sum_{K<p\le \exp(cL_{2N})}\alpha_p(n)^2
 \le (H_{2N}-H_N)T_K+o_N(1).
$$
Together these ranges cover every prime. Summing over dyadic intervals,
the main terms telescope and the errors have vanishing Cesàro mean.
Enlarging the last partial interval changes its harmonic endpoint by
$O(1)$. This proves (6), with the exact coefficient shown there.

One can replace the polynomial height in (5) by
$$
 \log(2+B_N)=o(\log N\,\log\log\log N).
$$
Indeed (7), applied to $2N+B_N$, still gives
$\log D_N=o(L_N)$; the rest of the proof is unchanged.

## Scope

The center sets may depend on the prime and on the interval, and their
allowed size tends to infinity. This is not a finite-local-color
hypothesis. The result excludes a broad class of moderate-height
translated or polynomial incidence constructions from violating the
square-tail target. Arbitrarily large CRT centers or unrestricted
smaller-part residues are not covered. Even for this subclass, no
survivor-conditioned arithmetic cancellation or general density
conclusion is asserted.

---
name: research/erdos_25/smooth_largest_prime_reduction
desc: A sharp reciprocal-summability cutoff for very smooth smaller parts, and a capped-square obstruction to bounded-degree polynomial CRT coding.
tags: [prime-filtration, smooth-numbers, reductions, obstructions]
sources: []
created: 2026-09-22T15:44:58Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/smooth_largest_prime_reduction

***

These are support reductions and a construction obstruction, not a
logarithmic-density theorem for general residues. They use the optimized
Rankin estimate from [capped prime fractions](capped_prime_fractions.md#an-optimized-small-prime-cutoff).

## A reciprocal-summability threshold

For sufficiently large primes $p$, define
$$
 u_c(p)=c\,\frac{\log\log p}{\log\log\log p}.
$$
Let $\mathcal S_c$ consist of the integers
$$
 q=p^e m,\qquad e\ge1,\quad P^+(m)<p,\quad m>p^{u_c(p)}.
 \tag{1}
$$
Any fixed finite set of smaller primes may be omitted from this
definition. Including all integers supported on those primes would
still add only a reciprocal-summable set.

**Theorem.** For every fixed $c>1$,
$$
 \sum_{q\in\mathcal S_c}\frac1q<\infty.
 \tag{2}
$$
For every fixed $0<c<1$, that sum diverges, already with $e=1$.
No assertion at $c=1$ is needed here. The sharp threshold concerns
reciprocal summability only, not existence of density.

**Convergence.** The optimized reciprocal smooth-tail estimate is
$$
 \sum_{\substack{m>p^u\\P^+(m)<p}}\frac1m
 \ll\log(2p)\exp\!\left(
 -u\log u+2u\log\log u+O(u/\log u)\right).
 \tag{3}
$$
Its hypotheses hold for $u=u_c(p)$ and all sufficiently large $p$.
Since
$$
 u_c(p)\log u_c(p)=c\log\log p+o(\log\log p),\qquad
 u_c(p)\log\log u_c(p)=o(\log\log p),
$$
the left side of (3) is at most
$(\log p)^{1-c+o(1)}$. For $\eta=(c-1)/2>0$, it is therefore
$O_c((\log p)^{-\eta})$. Summing the $p$-power exponent gives
$$
 \sum_{q\in\mathcal S_c}\frac1q
 =\sum_p\frac1{p-1}
       \sum_{\substack{m>p^{u_c(p)}\\P^+(m)<p}}\frac1m<\infty.
$$
The last prime sum converges by Chebyshev's upper bound and partial
summation. Its part with $p>K$ is $O_c((\log K)^{-\eta})$.

**Divergence.** Fix $a$ with $c<a<1$, put
$y=p^a$, and take $k=\lceil u_c(p)/a\rceil$. Consider products
$$
 m=b\,r_1\cdots r_k,
 \qquad P^+(b)\le y,\qquad y<r_1<\cdots<r_k<p.
$$
Their factorization into $b$ and the displayed primes is unique, and
$m>p^{ak}\ge p^{u_c(p)}$. Chebyshev's upper and lower prime-counting
bounds, followed by partial summation, give
$$
 \lambda_p:=\sum_{p^a<r<p}\frac1r\asymp_a1.
$$
For example the integral of the lower bound
$\pi(t)\gg t/\log t$ on $[p^a,p]$ supplies a positive constant,
while the endpoint error is $O_a(1/\log p)$.

Choose $k$ primes independently with probabilities $1/(r\lambda_p)$.
Their collision probability is at most $O_a(k^2/p^a)=o(1)$, so
the elementary symmetric sum obeys
$$
 e_k((1/r)_{p^a<r<p})
 \ge (1-o(1))\frac{\lambda_p^k}{k!}.
$$
Also
$\prod_{\ell\le y}(1-1/\ell)^{-1}\ge H_{\lfloor y\rfloor}
\gg_a\log p$. Consequently
$$
 \begin{aligned}
 \sum_{\substack{m>p^{u_c(p)}\\P^+(m)<p}}\frac1m
 &\ge H_{\lfloor y\rfloor}
          (1-o(1))\frac{\lambda_p^k}{k!}\\
 &\ge(\log p)^{1-c/a+o(1)}.
 \end{aligned}
 \tag{4}
$$
Here $k\log k=(c/a+o(1))\log\log p$. Since $c/a<1$, the
last bound eventually exceeds one. The divergence of $\sum_p1/p$
now proves the assertion for $q=pm$. $\square$

## Reductions retaining original activation

For one normalized residue at each selected $q\in\mathcal S_c$,
$$
 |B_q\cap[1,X]|\le X/q,\qquad
 H_{B_q}(X)\le H_{\lfloor X\rfloor}/q.
$$
Thus the numerical tails of this family are negligible in upper natural
and logarithmic density. Its fixed initial classes may have positive
density and must still be retained when approximating a full system.
Combining (2) with the
[repeated-largest-prime reduction](prime_filtration.md#removing-repeated-largest-prime-factors-from-the-tail)
shows that, for any fixed $c>1$, the remaining general tail problem
can be restricted to
$$
 q=pm,\qquad P^+(m)<p,\qquad m\le p^{u_c(p)}.
 \tag{5}
$$
This is a reduction to a large-prime support, not an estimate for its
remaining congruences.

There is also a uniform reduction for the capped-square target.
Let $\widetilde\alpha_p$ retain only the nonexceptional moduli.
The fraction removed by exceptional moduli is at most their incidence
potential $R_p$, and
$$
 0\le\alpha_p(n)^2-\widetilde\alpha_p(n)^2\le2R_p(n).
$$
For each term $p^{-e}\mathbf1_{n\equiv a_q\ (m)}$ of $R_p$,
activation $n\ge p^em$ implies
$$
 \sum_{\substack{n\le X\\n\ge p^em\\n\equiv a_q\ (m)}}\frac1n
 \le \frac{H_{\lfloor X\rfloor}}m.
$$
Hence the normalized harmonic contribution of the squared-fraction
difference at $p>K$ is at most
$$
 2\sum_{\substack{q\in\mathcal S_c\\P^+(q)>K}}\frac1q=o_K(1),
 \tag{6}
$$
uniformly over the finite family and $X$. The same calculation
handles the reciprocal-summable repeated-largest-prime exception.

## Bounded polynomial CRT templates have vanishing square tails

The quadratic CRT construction in
[Green--Ruzsa, Section 5](https://arxiv.org/html/1712.02108#S5)
suggests assigning a starting point $m^2\bmod Q$ to a progression
of direction $m$. The following obstruction to its direct use here
is independent of any theorem in that paper.

Fix $d\ge1$, $C\ge1$, and $\gamma>0$. For each sufficiently
large prime $p$, let $Q_p$ be an integer with
$\omega(Q_p)\ge\gamma\log p$, and let $f_p\in\mathbb Z[t]$
satisfy
$$
 f_p(0)=0,\qquad 0\le f_p(m)\le C m^d\quad(m\ge1).
 \tag{7}
$$
For selected $m$ with $P^+(m)<p$, prescribe the smaller-coordinate
residue at modulus $pm$ by
$$
 c_{p,m}\equiv (f_p(m)\bmod Q_p)\pmod m,
 \tag{8}
$$
where the inner residue is the least nonnegative representative.
The $p$-digits may be arbitrary, independently at every selected
modulus. All these original moduli are globally distinct.

**Proposition.** The exact fractions for such systems obey
$$
 \lim_{K\to\infty}\sup_{\mathcal F,X\ge2}
 \frac1{H_{\lfloor X\rfloor}}
 \sum_{n\le X}\frac1n\sum_{p>K}\alpha_p(n)^2=0,
 \tag{9}
$$
uniformly over $Q_p,f_p$ subject to the fixed parameters in (7).

**Proof.** Put $M_p=(Q_p/(2C))^{1/d}$. If $m<M_p$, then
$0\le f_p(m)<Q_p$, and $m\mid f_p(m)$ by $f_p(0)=0$.
Thus the smaller-coordinate residue is zero.

Let $r=\omega(Q_p)$. Distinct prime divisors give
$Q_p\ge(r+1)!$, without any squarefreeness assumption. Therefore
$$
 \frac{\log M_p}{\log p}
 \ge\frac{\gamma}{d}\log\log p-O_{C,d,\gamma}(1).
$$
For any fixed $c>1$, all sufficiently large $p$ consequently
satisfy $M_p>p^{u_c(p)}$, uniformly in the choices.

Split the incidence potential as $A_{0,p}+R_p$, with
$$
 A_{0,p}(n)=\frac1p\sum_{\substack{m<M_p\\pm\ {\rm selected}}}
                 \mathbf1_{m\mid n},
$$
and with $R_p$ containing the remaining, activated incidences.
The zero part deliberately omits activation. Then
$\alpha_p^2\le A_{0,p}^2+2R_p$. Every pair in the zero part
intersects in a multiples set, so the exact harmonic multiples bound
gives
$$
 \frac1{H_{\lfloor X\rfloor}}\sum_{n\le X}\frac{A_{0,p}(n)^2}{n}
 \le \frac1{p^2}
       \prod_{\ell<p}\frac{1+1/\ell}{(1-1/\ell)^2}
 \le U_p.
$$
All remaining moduli belong to $\mathcal S_c$. Their contribution
is bounded by (6). Summing $U_p$ and letting $K\to\infty$
proves (9). $\square$

For the literal quadratic template, a proposed image compression
$\prod_{\ell\mid Q_p}\frac{1+1/\ell}{2}\le p^{-2}$ forces
$\omega(Q_p)\ge2\log p/\log2$, so the proposition applies.
It controls the entire installed system, not only a selected finite
progression trace.

Large varying coefficients or constant terms are not covered:
$f_p(m)=B_pm^2+A_p$ need not satisfy (7), and its small smaller-part
residues need not be zero. No obstruction to all arithmetic-Kakeya
constructions, no general capped-square theorem, and no conditioned
arithmetic digit transfer is asserted.

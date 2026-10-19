---
name: theory/number_theory/L104_shifted_prime_totient_fibers/_proof
title: From exceptional totient fibers to exceptional prime basins
desc: |
  Apply the 2005 exceptional-prime theorem and the absence of predecessors
  of 2p to identify almost every prime basin. A supplementary reconstruction
  of a weaker count uses the source's largest-prime splitting mechanism.
created: 2026-10-15T05:22:42Z
updated: 2026-10-15T05:22:42Z
---

***

We prove
[[theory/number_theory/L104_shifted_prime_totient_fibers/_index|L104]].
Natural logarithms are used throughout, $\ell$ and $q$ denote primes,
$P^+(n)$ is the largest prime factor of $n$, and $\mathcal V$ is the set of
values of Euler's function.

## The source theorem and the basin deduction

Banks, Ford, Luca, Pappalardi and Shparlinski, *Values of the Euler Function
in Various Sequences*, Monatshefte für Mathematik 146 (2005), 1–19,
[[../library/arithmetic_functions/banks_et_al_2005_values_euler_function_various_sequences/theorem_4_1|Theorem 4.1]]
([author manuscript, pp. 14–15](https://www.ford126.web.illinois.edu/wwwpapers/philam.pdf),
accessed 2026-10-15),
bound the set

$$
\mathcal L(x)=\{p\le x:p\text{ prime},\ \varphi(n)=p-1
\text{ for some }n\notin\{p,2p\}\}
$$

by $x(\log x)^{-2}\exp((\kappa+o(1))(\log\log\log x)^2)$, with
$\kappa=0.8178\ldots$. The definition on manuscript page 3 and the proof
on pages 14–15 were read. We use this published theorem as an input;
the original totient-counting and sieve results on which it rests have
not been independently audited here. Since
$(\log\log\log x)^2=o(\log\log x)$, this is
$O_\delta(x/(\log x)^{2-\delta})$ for every $\delta>0$.

Let $p$ be odd. If its basin is $\{p,2p\}$, every solution of
$\varphi(n)=p-1$ belongs to this set. Conversely, suppose these are the
only solutions. No positive integer has $T(n)=2p$: $\varphi(n)$ is even
for $n\ge3$, while $T(1)=T(2)=2$. A first arrival at $p$ must therefore
come directly from $2p$. Thus its whole basin is $\{p,2p\}$.

The prime $2$ contributes at most one exception. The source theorem and
$\pi(x)\asymp x/\log x$ prove the claimed relative density among primes.
The union of the two-element basins contains at most
$\pi(x)+\pi(x/2)=O(x/\log x)$ integers up to $x$, proving its natural
density is zero. Every integer reaches a prime: for composite $n>2$,
$T(n)<n$, and $T(1)=2$. Hence the complementary union, over exceptional
terminal primes, has density one. A countable union of zero-density sets
can have density one, so this does not force any fixed basin to be infinite
or to have positive density.

## Supplementary reconstruction of the weaker count

The following argument records the same largest-prime split used in the
source proof, with a weaker totient sparsity estimate. It is an
author-recorded reconstruction, not a new exceptional-prime theorem.

### Inputs

The proof uses the following classical results.

1. **Size of $n/\varphi(n)$.** $n/\varphi(n)\le2\log\log n$ for all large
   $n$, since $\limsup n/(\varphi(n)\log\log n)=e^{\gamma}<2$ (Landau).
2. **Two-prime upper-bound sieve.** There is an absolute constant $C_1$ such
   that for every integer $m\ge2$ and every real $Y\ge2$,

   $$
   \#\{t\le Y:\ t\text{ and }m(t-1)+1\text{ both prime}\}
   \le C_1\frac{Y}{(\log Y)^2}
       \prod_{\ell\mid m(m-1)}\Bigl(1-\frac1\ell\Bigr)^{-1}.
   $$

   This is Brun's or Selberg's upper-bound sieve (Halberstam and Richert,
   *Sieve Methods*, 1974, Chapters 2 and 3) applied to the values of
   $F(t)=t\,(mt-m+1)$ for $t\le Y$, sifted by the primes up to $Y^{1/4}$.
   The number $\rho(\ell)$ of residues $t\bmod\ell$ with
   $F(t)\equiv0$ is $1$ when $\ell\mid m(m-1)$ (for $\ell\mid m$ the second
   factor is $\equiv1$; for $\ell\mid m-1$ it is $\equiv t$, the root of the
   first) and $2$ otherwise, so $\rho(\ell)<\ell$ for every $\ell$, and the
   remainder at a squarefree $d$ is at most $\rho(d)$, independently of $m$.
   The sieve product is
   $\prod_{\ell\le Y^{1/4}}(1-\rho(\ell)/\ell)\ll(\log Y)^{-2}
   \prod_{\ell\mid m(m-1)}(1-1/\ell)^{-1}$, and the $t\le Y^{1/4}$ add at
   most $Y^{1/4}$.
3. **Sparsity of totient values.** For every $\delta>0$ and all large $t$,
   $\#(\mathcal V\cap[1,t])<t/(\log t)^{1-\delta}$ (Erdős 1935, on
   [[../library/arithmetic_functions/erdos_1935_normal_number_prime_factors_related_problems/_index|his paper's card]];
   Ford's Theorem 1 on
   [[../library/arithmetic_functions/ford_1998_distribution_totients/_index|the Ford 1998 card]]
   gives the true order). By partial summation,

   $$
   \sum_{m\in\mathcal V,\ m\le x}\frac1m
   =\frac{\#(\mathcal V\cap[1,x])}x
     +\int_1^x\frac{\#(\mathcal V\cap[1,t])}{t^2}\,dt
   \ll_\delta1+\int_{3}^x\frac{dt}{t(\log t)^{1-\delta}}
   \ll_\delta(\log x)^\delta.                                     \tag{1}
   $$

4. **Rankin's bound.** For $X\ge y\ge2$ and $0<\sigma<1$, the number
   $\Psi(X,y)$ of $y$-smooth integers up to $X$ is at most
   $\sum(X/n)^\sigma$ over all $y$-smooth $n$, that is
   $X^\sigma\prod_{\ell\le y}(1-\ell^{-\sigma})^{-1}$. Take
   $\sigma=1-1/(2\log y)$ with $y\ge e^2$. For $\ell\le y$,
   $\ell^{-\sigma}=\ell^{-1}e^{\log\ell/(2\log y)}\le\ell^{-1}
   (1+\log\ell/\log y)$, so Mertens' theorems give
   $\sum_{\ell\le y}\ell^{-\sigma}=\log\log y+O(1)$; as $2\sigma\ge3/2$, the
   product is $O(\log y)$, and

   $$
   \Psi(X,y)\ll Xe^{-u/2}\log y,\qquad u=\frac{\log X}{\log y}.  \tag{2}
   $$

### The cases

Let $x$ be large, and put

$$
\varepsilon=\frac1{12\log\log x},\qquad
y=x^{2\varepsilon}=\exp\Bigl(\frac{\log x}{6\log\log x}\Bigr).
$$

Call a prime $p\le x$ exceptional if some $n\notin\{p,2p\}$ has
$\varphi(n)=p-1$. Discard $p=2$ at a cost of one, and for each remaining
exceptional prime fix such an $n$. Since $\varphi(n)\ge\sqrt{n/2}$, we
have $n\le2x^2$, and input 1 gives
$n\le X:=3x\log\log x$. Let $q=P^+(n)$.

**A power of two.** If $q=2$, then $n=2^b$ and $p=2^{b-1}+1$; there are at
most $\log_2x+1$ such primes.

Otherwise $q$ is odd; let $q^a$ be the exact power of $q$ dividing $n$.

**Case A: $q\le y$.** Then $n$ is a $y$-smooth integer up to $X$, and $n$
determines $p=\varphi(n)+1$. Here $u=\log X/\log y\ge1/(2\varepsilon)
=6\log\log x$, so (2) gives at most

$$
\ll3x\log\log x\cdot(\log x)^{-3}\cdot\frac{\log x}{6\log\log x}
\ll\frac x{(\log x)^2}
$$

exceptional primes in this case.

**Case B: $q>y$ and $a\ge2$.** Each possible $n\le X$ is divisible by
$q^2$ for some $q>y$. Each $n$ determines $p=\varphi(n)+1$, so their
contribution is at most

$$
\sum_{q>y}\left\lfloor\frac X{q^2}\right\rfloor
\le X\sum_{j>y}\frac1{j^2}
\ll\frac{x\log\log x}{y}
\ll\frac x{(\log x)^{10}}.
$$

Here $y$ exceeds every fixed power of $\log x$ for all sufficiently large
$x$.

**Case C: $q>y$ and $a=1$.** Write $n=qn'$ with $q\nmid n'$. If
$n'\in\{1,2\}$, then $\varphi(n)=q-1=p-1$, so $q=p$ and $n\in\{p,2p\}$,
which is excluded. So $n'\ge3$, and $m=\varphi(n')$ is a totient value with
$m\ge2$ and

$$
p-1=(q-1)m,\qquad q-1\le x/m.
$$

Every exceptional prime of this case is therefore $m(q-1)+1$ for some
$m\in\mathcal V$ with $2\le m\le x$ and some prime $q$ with
$y<q\le x/m+1$ such that $m(q-1)+1$ is prime. Only $m$ with
$Y:=x/m+1\ge y$ contribute. For those $m$,
$\log Y\ge\log x/(6\log\log x)$, and
$Y\le2x/m$. Since $m$ and $m-1$ are coprime,

$$
\prod_{\ell\mid m(m-1)}\Bigl(1-\frac1\ell\Bigr)^{-1}
=\frac m{\varphi(m)}\cdot\frac{m-1}{\varphi(m-1)}\ll(\log\log x)^2
$$

by input 1. Input 2 bounds the number of these $q$ by
$\ll x(\log\log x)^4/(m(\log x)^2)$, uniformly in $m$. Summing over
$m\in\mathcal V$ with (1),

$$
\#\{\text{exceptional }p\le x\text{ in case C}\}
\ll_\delta\frac{x(\log\log x)^4}{(\log x)^{2-\delta}}.
$$

### Conclusion of the reconstruction

Adding the cases, the number of exceptional primes up to $x$ is
$\ll_\delta x(\log\log x)^4/(\log x)^{2-\delta}$ for every $\delta>0$, hence
at most $C_\delta x/(\log x)^{2-2\delta}$; replacing $\delta$ by $\delta/2$
and enlarging $C_\delta$ to cover small $x$ gives the bound in the
statement. As $\pi(x)\gg x/\log x$, the exceptional primes have relative
density zero.

Let $p$ be a prime that is not exceptional. The integers $n$ with
$T(n)=\varphi(n)+1=p$ are those with $\varphi(n)=p-1$, namely $p$ and $2p$.
No $n$ has $T(n)=2p$, because $\varphi(n)$ is even for $n\ge3$ and
$\varphi(1)=\varphi(2)=1$, while $2p-1$ is odd and greater than $1$. If some
iterate of $n$ equals $p$, take the first one, $T^k(n)=p$. For $k\ge1$ the
previous iterate is a $T$-preimage of $p$ other than $p$, so it is $2p$,
and then $k=1$ because $2p$ has no preimage. Hence $n\in\{p,2p\}$, and
both elements reach $p$.

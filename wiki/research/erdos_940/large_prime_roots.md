---
name: research/erdos_940/large_prime_roots
title: Restricting root variables by large prime factors
desc: A positive-mass input restriction gives bilinear cubic sums, but elementary Type-II estimates lose a cofactor power and anchor congruences do not constrain competing roots.
tags: []
sources: []
created: 2026-09-22T18:23:06Z
updated: 2026-09-22T18:23:06Z
---


# Restricting root variables by large prime factors

***

## The new mechanism tested

Instead of changing the cubic's coefficients, or bounding all of its
fibers, restrict the inputs to integers with one large prime factor.
This retains positive input mass and gives a bilinear description of the
exponential sums. The hope was to use the prime factors to control
alternative representations. The elementary estimates below are proved;
the required restricted multiplicity bound is not. This attempt has not
resolved any density or higher-exponent infinitude case.

## A restriction that does retain positive input mass

Fix $0<\delta<1$ and $1/2<\theta<1$. Set

$$
\mathcal A_\theta(N)=
\{x\in(\delta N,N]\cap\mathbb Z:
  p\mid x\text{ for a prime }p>N^\theta\}.
$$

There is at most one such prime, since $N^{2\theta}>N$. Consequently

$$
|\mathcal A_\theta(N)|
=\sum_{N^\theta<p\le N}
 \left(\left\lfloor N/p\right\rfloor
      -\left\lfloor\delta N/p\right\rfloor\right)
=\bigl((1-\delta)\log(1/\theta)+o(1)\bigr)N.             \tag{1}
$$

The total floor error is $O(\pi(N))=o(N)$, and
$\sum_{N^\theta<p\le N}1/p=\log(1/\theta)+o(1)$.
Thus three independently restricted roots still supply $\gg N^3$ inputs
to the fixed form $F=x^3+2y^3+4z^3$. This is not coefficient averaging
with escaping arithmetic height. Multiplication of its values by $8$
puts them in $S_3$.

Writing $x=mp$ gives exactly

$$
W_{\theta,N}(\alpha)=
\sum_{m\le N^{1-\theta}}
\ \sum_{\substack{p>N^\theta\\ \delta N<mp\le N}}
 e(\alpha m^3p^3).
$$

For the resulting representation function $R_{\theta,N}$,

$$
\sum_nR_{\theta,N}(n)^2
=\int_0^1
 |W_{\theta,N}(\alpha)W_{\theta,N}(2\alpha)
                    W_{\theta,N}(4\alpha)|^2\,d\alpha. \tag{2}
$$

An $O(N^3)$ bound in (2), or a bounded logarithmic moment on these inputs,
would give positive density by the existing multiplicity criteria.
Neither was proved.

## Where the elementary Type-II estimate loses the endpoint

On a rectangular block $m\asymp M$, $p\asymp P$, $MP\asymp N$, put

$$
T(\alpha)=\sum_{m\asymp M}\sum_{p\asymp P}e(\alpha m^3p^3).
$$

Cauchy–Schwarz in $m$, followed by a triangle inequality, gives

$$
|T(\alpha)|^2
\ll M^2\#\{p\asymp P\}
+M\sum_{\substack{p,q\asymp P\\p\ne q}}
\left|\sum_{m\asymp M}
 e\bigl(\alpha(p^3-q^3)m^3\bigr)\right|.                \tag{3}
$$

The first term in this upper-bound method is
$\asymp MN/\log P$. It is a factor $M$ above the square-root scale
$N/\log P$ for the block. It persists even if the off-diagonal part of
this particular bound were negligible. Applying such pointwise estimates
and a fourth moment therefore leaves a polynomial cofactor loss when
$M=N^\varepsilon$. This is a limitation of that estimate, not a lower
bound on the actual sum or a refutation of a joint sixth-moment method.

Restricting all cofactors to $m\le M=N^{o(1)}$ sacrifices the positive
input mass:

$$
\#\{mp\in(\delta N,N]:m\le M,\ p\text{ prime}\}
\ll\frac{N(1+\log M)}{\log(N/M)}=o(N).                 \tag{4}
$$

For example, sum the elementary prime-counting upper bound
$\pi(N/m)\ll(N/m)/\log(N/m)$ over $m\le M$.

## The prime factors do not propagate to competing roots

An input prime $p\mid x$ imposes an equation on the competing value, not
divisibility of a competing coordinate. This can be checked without an
asymptotic heuristic. If $p>3$ and $p\equiv2\pmod3$, cubing permutes
$\mathbb F_p$, so for every $n$,

$$
\#\{(u,v,w)\bmod p:u^3+2v^3+4w^3=n\}=p^2.
$$

At most $3p$ of these roots have a zero coordinate. Thus all-unit
solutions exist for every target, and are nonsingular. They lift to
every $p^k$, including when the original input has a coordinate divisible
by $p$. If $p\nmid n$, all roots are nonsingular and the full number
modulo $p^k$ is exactly $p^{2k}$.

The same elementary character estimate gives all-unit nonsingular roots
at every sufficiently large good prime, not just in the displayed
progression. CRT therefore does not make several input-prime conditions
independent of the original output equation. A modulus exceeding the
output range turns their conjunction back into exact equality; its
very incomplete-box count has not become easier.

## Target roughness does not force large root primes

There is also an exact higher-exponent caution. Fix $r\ge3$, put
$A=\operatorname{rad}(r)$, and choose a prime $q\nmid r$. For any $y$
and any $K$, there is $k$ such that

$$
U_k=A^{rk}+(r-1)q^{rk}
$$

has no prime divisor at most $y$ and has at least $K$ distinct prime
divisors. Nevertheless it is the sum of $r$ positive $r$th powers
whose roots use only the fixed primes dividing $Aq$.

First choose $k$ divisible by every $p-1$ with $p\le y$, $p\nmid Aq$.
Then $U_k\equiv r\not\equiv0\pmod p$ for these primes. At $p\mid A$
the second term is a unit, and at $p=q$ the first term is a unit, so
$U_k$ is $y$-rough and is always coprime to $Aq$.

To add prime divisors while retaining all existing ones, let
$e_p=v_p(U_k)$ for the finitely many $p\mid U_k$. Choose $L$ divisible
by the earlier $p-1$ conditions and by the multiplicative orders of
$A^r$ and $q^r$ modulo every $p^{e_p+1}$. Replacing $k$ by $k+Lt$
keeps all these valuations fixed and retains $y$-roughness. Since
$U_{k+Lt}\to\infty$, some sufficiently large $t$ introduces a new
prime divisor. Iterate.

For any fixed $\theta>0$, these roots have no prime factor greater than
$N^\theta$ once $k$ is large, where $N=\max(A,q)^k$. This excludes a
deterministic inference from arbitrarily large *fixed-threshold*
roughness and many target prime factors to a large root-prime factor.
It does not exclude a power-scale roughness condition, an average
argument, or a condition requiring every root to have comparable size.

## A power-scale test with comparable roots

The following stronger, but sparse, construction tests power-scale
roughness. Fix $r\ge5$, $k\ge1$, and $0<\eta<1/2$. For all sufficiently
large $Z$ there are

$$
\gg_{r,k,\eta}\frac{Z^r}{\log Z}
$$

tuples $Z<z_i\le2Z$ such that

$$
P^-\left(\sum_{i=1}^r z_i^{rk}\right)\ge Z^\eta.        \tag{5}
$$

The target is represented by the $r$ positive $r$th powers of the roots
$x_i=z_i^k$. These roots are comparable and all their prime factors are
at most $2Z$.

Here is a proof with the sieve hypotheses explicit. Write
$G(\mathbf z)=\sum_i z_i^{rk}$ and

$$
\rho(d)=\#\{\mathbf z\bmod d:G(\mathbf z)=0\bmod d\},
\qquad g(d)=\rho(d)/d^r
$$

for squarefree $d$. Both functions are multiplicative. At a prime
$p\nmid rk$, expansion in additive characters and the monomial
Gauss-sum bound give

$$
\rho(p)=p^{r-1}+O_{r,k}(p^{r/2}),\qquad
g(p)=p^{-1}+O_{r,k}(p^{-r/2}).
$$

There are only finitely many other primes. Also $g(p)<1$ at every
prime, since $G(1,0,\ldots,0)=1$. Since $r\ge5$, the product comparison
$\sum_p p^{1-r/2}<\infty$ gives the uniform bound
$\rho(d)\ll_{r,k}d^{r-1}$ for squarefree $d$.

Counting the box in residue classes now gives, uniformly for squarefree
$d\le Z$,

$$
\#\{\mathbf z\in(Z,2Z]^r:d\mid G(\mathbf z)\}
=g(d)Z^r+O_{r,k}(Z^{r-1}).                            \tag{6}
$$

For each residue vector the error is
$O_r((Z/d)^{r-1})$, which explains the uniform remainder after summing
over $\rho(d)$ roots.

Choose $2\eta<\gamma<1$ and use sieve level $D=Z^\gamma$ with sifting bound
$z=Z^\eta$. The summed remainders in (6) are $O(Z^{r-1+\gamma})=o(Z^r/\log Z)$.
The dimension-one lower linear sieve has positive lower factor when
$\log D/\log z=\gamma/\eta>2$; the applicable statement, hypotheses, and
positive lower factor were checked in [Tao, *The linear sieve*, Theorem 2,
equations (1)–(3), (11),
(13)](https://terrytao.wordpress.com/2015/01/29/254a-supplement-5-the-linear-sieve-and-chens-theorem-optional/).
Its local product satisfies $\prod_{p<z}(1-g(p))\asymp_{r,k}1/\log z$. It
therefore proves (5).

In terms of root height $N=(2Z)^k$, the targets in (5) have no prime
factor below $\tfrac12N^{\eta/k}$, while every root prime is at most
$N^{1/k}$. In particular, choosing $1/k<\theta$ produces represented
power-rough targets with comparable roots and no prime anchor above
$N^\theta$. The tuples form a sparse input set when $k>1$; (5) is
not a positive-density assertion about distinct targets and does not
exclude a statistical use of roughness.

## Outcome

The restriction (1) avoids the immediate zero-density problem with prime
roots alone. But neither prime divisibility nor the elementary bilinear
estimate controls its fibers. A useful continuation would have to
estimate the six bilinear sums jointly, before the Cauchy step in (3),
or supply a different arithmetic mechanism. No such estimate is
established here; another conditional moment bound is not a resolution.

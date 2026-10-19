---
name: theory/irrationality/L16_totient_kernel_separation/_proof
title: Proof of separation for infinite totient kernels
desc: |
  Divisor counting gives exact progression means; two fresh-prime
  refinements separate an isolated nonzero coefficient from the l1 tail.
tags: []
sources:
- theory/irrationality/L16_totient_kernel_separation/_index
created: 2026-09-17T06:05:14Z
updated: 2026-09-17T06:05:14Z
---

***

This proves the entire statement of
[[theory/irrationality/L16_totient_kernel_separation/_index|L16]] at
author-recorded tier 0. Write $\mu$ for the Möbius function and
$\rho(n)=\varphi(n)/n$. Inclusion-exclusion over the distinct prime
divisors of $n$ gives

$$
\rho(n)=\prod_{p\mid n}(1-p^{-1})
       =\sum_{d\mid n}\frac{\mu(d)}d,
\qquad 0<\rho(n)\le1.
$$

## Exact means of the normalized totient

Fix $Q\ge1$ and first take an integer $r\ge0$. For $g=\gcd(d,Q)$,
the condition $d\mid r+Qt$ is soluble in $t$ exactly when $g\mid r$.
In that case it defines one residue class modulo $d/g$, whose count
among $1\le t\le X$ differs from $Xg/d$ by at most one. Expanding
the divisor identity, with $Y=r+QX$, therefore gives

$$
\frac1X\sum_{t=1}^X\rho(r+Qt)
 =\sum_{\substack{d\le Y\\(d,Q)\mid r}}
   \frac{\mu(d)(d,Q)}{d^2}
  +O\!\left(\frac{1+\log Y}{X}\right).
$$

The sum on the right extends to an absolutely convergent series: its
tail is at most $Q\sum_{d>Y}d^{-2}\le Q/Y$. Both errors tend to zero
for fixed $Q,r$. A fixed shift of $t$ handles negative $r$ and shows
that changing representatives modulo $Q$ does not change the mean.
Thus the mean is

$$
\kappa_Q(r)=\sum_{\substack{d\ge1\\(d,Q)\mid r}}
              \frac{\mu(d)(d,Q)}{d^2}.
$$

Its multiplicative summands admit an absolutely convergent Euler
product. A prime $p\nmid Q$ gives the factor $1-p^{-2}$; a prime
$p\mid Q$ gives $1-p^{-1}$ if $p\mid r$, and $1$ otherwise. Using
$\prod_p(1-p^{-2})=1/\zeta(2)$ gives the formula in the statement.
The infinite product is positive because $\sum_p p^{-2}<\infty$,
and the finitely many replacement factors are positive. Consequently
$\kappa_Q(r)>0$ for every $r$, and $\kappa_Q(r)\le1$ because it is
a limit of averages of numbers in $(0,1]$.

## Refinement at a fresh prime

Let $\ell\nmid Q$ be prime. For each residue $b\pmod\ell$, choose
$a_b$ with $a_b\equiv a\pmod Q$ and $a_b\equiv b\pmod\ell$;
the Chinese remainder theorem supplies it. The product formula shows,
for every integer $s$,

$$
\kappa_{Q\ell}(a_b+s)
 =\frac{\kappa_Q(a+s)}{1-\ell^{-2}}
   \left(1-\frac{\boldsymbol1_{\ell\mid b+s}}\ell\right).
$$

Indeed the factors at primes dividing $Q$ are unchanged. At $\ell$,
the former factor $1-\ell^{-2}$ is replaced by $1-\ell^{-1}$ when
$\ell\mid b+s$, and by $1$ otherwise.

## Passing the infinite kernel through the mean

For any absolutely summable real kernel $c$, the tails of
$F(N)=\sum_sc_s\rho(N+s)$ have absolute value at most
$\sum_{s>H}|c_s|$, uniformly in $N\ge1$. For a finite truncation,
the mean is the sum of the finitely many means already computed.
Letting the cutoff grow proves that every progression mean of $F$
exists and equals

$$
\mathcal M_Q(a)=\sum_{s\ge1}c_s\kappa_Q(a+s).
$$

The error from the omitted kernel is bounded by its absolute tail
in each average and in this limiting expression. This justifies the
interchange without any assumption on pointwise asymptotics for
$\varphi(n)/n$.

## Separating the two refinements

Put $d_s=c_s\kappa_Q(a+s)$. This sequence is absolutely summable,
and it has a nonzero entry since $\kappa_Q(a+s)>0$ and $c$ is
nonzero. Take any $s_*,K,\ell$ satisfying the statement's conditions.
Such a $K$ exists by absolute convergence, and such primes exist by
infinitude of primes. Define

$$
D_r=\sum_{\substack{s\ge1\\s\equiv r\ (\ell)}}d_s.
$$

Because $1\le s_*\le K<\ell$, the initial part with $s\le K$
of $D_{s_*}$ contains only $d_{s_*}$, whereas that of $D_0$ is
empty. The two remaining sums use disjoint subsets of $s>K$, so

$$
|D_{s_*}-D_0|
 \ge |d_{s_*}|-\sum_{s>K}|d_s|
 >\frac34|d_{s_*}|>\frac12|d_{s_*}|.
$$

Summing the refinement identity against $c_s$ now gives

$$
\mathcal M_{Q\ell}(a_{-s_*})-
\mathcal M_{Q\ell}(a_0)
 =-\frac{D_{s_*}-D_0}{\ell(1-\ell^{-2})}.
$$

Its magnitude exceeds $|d_{s_*}|/[2\ell(1-\ell^{-2})]=2\eta$.
Hence at least one of these two means has magnitude greater than
$\eta$. The class denoted $a_{-s_*}$ here is the class denoted
$a_1$ in the statement; it is different from $a_0$ since
$0<s_*<\ell$.

On the refinement whose mean has magnitude greater than $\eta$,
there must be infinitely many $N$ with $|F(N)|>\eta/2$. Otherwise,
all sufficiently late terms would have absolute value at most
$\eta/2$, forcing the mean to have absolute value at most $\eta/2$.
The finitely many earlier terms have no effect on the mean because
$|F(N)|\le\sum_s|c_s|$. These infinitely many witnesses are also
in the original progression, proving its positive absolute limsup.
This proves both the main conclusion and every quantified refinement
assertion. $\square$

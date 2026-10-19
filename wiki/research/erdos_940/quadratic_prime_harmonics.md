---
name: research/erdos_940/quadratic_prime_harmonics
title: A conductor-uniform quadratic prime-harmonic bound
desc: An elementary two-sided logarithmic bound for real-character prime sums, used with a small coefficient in the quartic selection proofs.
tags: []
sources: []
created: 2026-09-22T20:53:41Z
updated: 2026-10-14T00:26:52Z
---


# A conductor-uniform quadratic prime-harmonic bound

***

## Statement and role

The following claim from Section 4 of the
[independent record](independent/quartic_pattern_elimination_and_random_omission.md)
is checked here. For every nonprincipal real Dirichlet character presented
modulo $q$,

$$
\sup_{z\ge2}\left|\sum_{p\le z}\frac{\chi(p)}p\right|
\ll\log(2q),                                             \tag{1}
$$

with an absolute constant. Differences of endpoints give the same bound
on any prime interval. The estimates after fixed-character nonvanishing
at $1$ are elementary; an elementary proof of that nonvanishing is included
below. No prime number theorem, Siegel bound, or zero-free
hypothesis is needed.

The existing [quartic Euler majorant](quartic_euler_majorant.md) needs only
upper bounds for $L$-functions, so (1) is additional input, not a missing
step of that proof. Its two-sided character is needed by the
[random omission construction](quartic_random_omission.md).

## A weak polynomial lower bound at one

First suppose $\chi$ is primitive. We use $L(1,\chi)>0$. This follows, for
example, from the fixed-character case of
[Ghidelli, Lemma 5.4](../../../library/diophantine_problems/ghidelli_2019_arbitrarily_long_gaps_between_values_positive_definite_cubic_biquadratic_diagonal_forms/_index.md),
whose passage has been checked: partial summation gives convergence of
$\sum_p\chi(p)/p$, and the Euler logarithm then has a finite real limit as
$\sigma\downarrow1$. Constants in that fixed-character assertion need not be
uniform and are not used in the estimates below.

Alternatively, Appendix E of
[third independent record](independent/quartic_analytic_architecture.md)
supplies a valid elementary nonvanishing argument. For real nonprincipal
$\chi$, the Dirichlet coefficients

$$
\zeta(s)L(s,\chi)=\sum_{n\ge1}a(n)n^{-s},\qquad
a(n)=\sum_{d\mid n}\chi(d)
$$

are nonnegative, and $a(k^2)\ge1$. Their convergence abscissa is therefore
in $[1/2,1]$. Periodic cancellation continues $L(s,\chi)$ holomorphically
to $\Re s>0$, while

$$
\zeta(s)=\frac{s}{s-1}
-s\int_1^\infty\{t\}\,t^{-s-1}\,dt
$$

continues zeta there with only its pole at one. If $L(1,\chi)=0$,
the product would be holomorphic throughout that half-plane. This
contradicts the elementary Landau lemma: a Dirichlet series with
nonnegative coefficients is singular at its finite convergence abscissa.
Indeed, a Taylor expansion about a real point just to its right, in
the leftward direction, has nonnegative coefficient sums. If it extended
past the abscissa, Tonelli would sum that Taylor series as the original
Dirichlet series at a smaller real argument, forcing convergence there.
Finally the positive Euler product for $s>1$ gives $L(1,\chi)>0$.
Thus this argument removes the fixed-character prime-distribution input
without changing any of the uniform bounds below.

Put $\zeta=e^{2\pi i/q}$ and
$\tau=\sum_{a=1}^q\chi(a)\zeta^a$, so $|\tau|=\sqrt q$ and
$\sum_a\chi(a)\zeta^{an}=\chi(n)\tau$ for every integer $n$.
If $\chi(-1)=-1$, multiply the sine Fourier series

$$
\sum_{n\ge1}\frac{\sin(2\pi na/q)}n
=\pi\left(\frac12-\frac aq\right)\qquad(0<a<q)
$$

by $\chi(a)$ and sum. The Gauss identity gives

$$
|L(1,\chi)|=\pi q^{-3/2}\left|\sum_{a=1}^q a\chi(a)\right|
\ge\pi q^{-3/2}.                                        \tag{2}
$$

The integer sum is nonzero by nonvanishing. The finite Fourier
manipulations can equivalently be made with Abel factors and then passed
to the limit.

If $\chi(-1)=1$, set

$$
U=\prod_{(a,q)=1}(1-\zeta^a)^{\chi(a)}.
$$

This is an algebraic unit. Indeed,
$(1-\zeta^a)/(1-\zeta)$ and its reciprocal are algebraic integers
by geometric sums, using an inverse of $a\bmod q$ for the reciprocal.
The common factors cancel because $\sum_a\chi(a)=0$.
Pairing $a$ and $-a$ shows $U>0$. The automorphism
$\zeta\mapsto\zeta^b$ sends $U$ to $U^{\chi(b)}$, so
$U+U^{-1}$ is a rational algebraic integer.

The cosine series
$\log|1-e^{2\pi it}|=-\sum_{n\ge1}\cos(2\pi nt)/n$
and the Gauss identity yield

$$
|\log U|=\sqrt q\,L(1,\chi).
$$

Thus $U\ne1$, and $U+U^{-1}$ is an integer greater than two.
It is at least three, whence

$$
L(1,\chi)\ge q^{-1/2}\log\frac{3+\sqrt5}{2}.
\tag{3}
$$

Both parities give the absolute effective bound $L(1,\chi)\gg q^{-3/2}$.

## Bounds just to the right of one

Periodicity and zero mean give
$|\sum_{n\le x}\chi(n)|\le q$. Splitting at $q$ and applying
partial summation to the tails, including the differentiated series,
gives uniformly for $1\le\sigma\le2$

$$
|L(\sigma,\chi)|\ll\log(2q),\qquad
|L'(\sigma,\chi)|\ll\log^2(2q).                        \tag{4}
$$

For $0\le\sigma-1\le c q^{-3/2}\log^{-2}(2q)$, (2)–(4)
preserve half the lower bound at one if $c>0$ is sufficiently small.
Outside that interval, the Euler factors give

$$
L(\sigma,\chi)\ge\prod_p(1+p^{-\sigma})^{-1}
=\frac{\zeta(2\sigma)}{\zeta(\sigma)}\gg\sigma-1.
$$

Consequently, throughout $1<\sigma\le2$,

$$
L(\sigma,\chi)\gg q^{-3/2}\log^{-2}(2q).                 \tag{5}
$$


## From the Euler logarithm to sharp cutoffs

For $z\ge3$, put $\sigma=1+1/\log z$. Uniformly for every real
Dirichlet character,

$$
\sum_{p\le z}\frac{\chi(p)}p=\log L(\sigma,\chi)+O(1).
\tag{6}
$$

Prime powers of exponent at least two have bounded total. Chebyshev's
prime bounds give

$$
\sum_{p\le z}\frac{1-p^{-1/\log z}}p
\le\frac1{\log z}\sum_{p\le z}\frac{\log p}p\ll1,
\qquad
\sum_{p>z}p^{-1-1/\log z}\ll1.
$$

For the last estimate, partial summation reduces to a constant multiple
of $\int_1^\infty e^{-u}\,du/u$. This proves (6).
Equations (4)–(6) prove (1) for primitive characters.
Passing to a character presented modulo $q$ removes only Euler factors
at primes dividing $q$; their contribution to a sharp prime sum is at
most $\sum_{p\mid q}1/p\ll\log(2q)$. Thus (1) holds as stated.

The identical smoothing argument for the principal character yields
$\sum_{p\le z}1/p=\log\log z+O(1)$, since
$\zeta(1+1/\log z)=\log z+O(1)$. Applying (1) to $\chi_{-4}$ gives,
uniformly for $3\le Y<Z$,

$$
\sum_{\substack{Y<p\le Z\\p\equiv3\ (4)}}\frac1p
=\frac12\log\frac{\log Z}{\log Y}+O(1).                 \tag{7}
$$


## Why the small multiplier matters

Exponentiating (1) with a fixed large coefficient can cost a polynomial
in the conductor that is not summable against canonical coefficient
weights. In the omission proof it is multiplied only by $O(\delta)$,
where $\delta>0$ can be chosen arbitrarily small. The resulting loss
$R^{C\delta}$ is summable. The complete quartic baseline still uses
only the positive $L$-powers of the established Euler majorant.

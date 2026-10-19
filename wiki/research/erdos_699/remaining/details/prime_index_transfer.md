---
name: research/erdos_699/remaining/details/prime_index_transfer
title: "Erdős 699: what the proved neighbouring indices force"
desc: "Prime-index exclusions impose explicit prime-square congruences on five remaining indices. Exact Lucas alternatives describe the forced common primes, but do not yet transfer complete exclusions across a threshold prime."
created: 2026-09-22T04:53:15Z
updated: 2026-10-13T05:25:33Z
---

# Erdős 699: what the proved neighbouring indices force

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/archive/previous_bounds/cutoff_21|The complete small-index cases]]

***

The proved prime-index cases impose the following necessary conditions on
remaining bad triples:

| Bad index $i$ | Forced common prime $p$ of $\binom np$ and $\binom nj$ | Necessary row condition |
| --- | --- | --- |
| $12$ | $11$ | $n\bmod121\in\{0,\ldots,10\}$ |
| $14,15$ | $13$ | $n\bmod169\in\{0,\ldots,12\}$ |
| $18$ | $17$ | $n\bmod289\in\{0,\ldots,16\}$ |
| $20$ | $19$ | $n\bmod361\in\{0,\ldots,18\}$ |

These are exclusions of entire residue classes, independent of the size of
$n$. They do not supply stopping bounds or exclude the remaining classes.
The exact Lucas alternatives below explain why the common prime cannot
simply be treated as another prime avoiding $\binom nj$.

## Prime-index transfer

**Proposition.** Let $p<q$ be consecutive primes. Suppose the original
Erdős 699 assertion is proved at index $p$. If

$$
p<i<q,\qquad i<j\le n/2
$$

is bad, then

$$p\mid\gcd\!\left(\binom np,\binom nj\right),\qquad
n\bmod p^2<p. \tag{1}$$

**Proof.** For every prime $\ell\ge q$,

$$
\binom ni=\binom np
\frac{(n-p)(n-p-1)\cdots(n-i+1)}{(p+1)(p+2)\cdots i}
$$

has $\ell$-valuation at least that of $\binom np$: every denominator
factor is less than $q$. Badness at $i$ therefore excludes every
$\ell\ge q$ from the gcd of $\binom np$ and $\binom nj$.
The proved assertion at $p$ supplies a common prime at least $p$.
Since $p,q$ are consecutive, that prime must be $p$ itself.

Put $r=n\bmod p$, so $0\le r<p$, and let $a=v_p(n-r)$.
Among the $p$ numerator factors of $\binom np$, the unique multiple of
$p$ is $n-r$. Consequently

$$
v_p\!\left(\binom np\right)=a-1.
$$

The forced common prime gives $a\ge2$, equivalently
$n\bmod p^2=r<p$. This proves (1). $\square$

The table applies this proposition to the complete cases
$p=11,13,17,19$. In the same notation, if $a\ge2$ and $p<i<q$, the
small-prime valuation at the bad index is also explicit:

$$
 v_p\!\left(\binom ni\right)
 =a-1+\mathbf1_{\{r<i-p\}}. \tag{2}
$$

Indeed, Bertrand's inequality gives $i<2p$. There is a second multiple
of $p$ in the numerator exactly when $r+p<i$, and that second multiple
has valuation one. The denominator has valuation one.

## The complete Lucas alternative at the forced prime

Write

$$
n=p^a u+r,\qquad p\nmid u,\qquad 0\le r<p,\qquad a\ge2,
$$

and divide the column by the same power:

$$
j=p^a J+b,\qquad 0\le b<p^a.
$$

Lucas's theorem gives the exact equivalence

$$
\boxed{
 p\mid\binom nj
 \quad\Longleftrightarrow\quad
 b>r\ \text{or}\
 \bigl(b\le r\ \text{and}\ p\mid\binom uJ\bigr).
} \tag{3}
$$

To see this, the first $a$ base-$p$ digits of $n$ are precisely those
of $r$. Lucas factors the reduction of $\binom nj$ as
$\binom uJ\binom rb$ modulo $p$, with $\binom rb=0$ when $b>r$.
When $b\le r<p$, the latter binomial coefficient is nonzero modulo $p$.

In the second branch of (3), admissibility implies

$$
1\le J\le u/2,\qquad u\ge p+1. \tag{4}
$$

The upper bound follows from $2j\le n$, since
$|r-2b|<p^a$. The lower bound follows because $\binom u0=1$.
A common prime $p$ of $\binom uJ$ requires $u\ge p$; equality is
excluded by $p\nmid u$.

In particular, when $u<p$, the forced common prime really does require
$b>r$. In general, the higher digits can be responsible instead. The
second branch cannot be dropped merely because $p^a$ is the full prime
power dividing $n-r$.

There is a useful bound on the actual gcd in that second branch. Put
$G=\gcd(\binom ni,\binom nj)$ and
$\delta=\mathbf1_{\{r<i-p\}}$. Since $b\le r$, subtraction of $j$
from $n$ has no borrow in its first $a$ base-$p$ digits. Kummer therefore
gives the exact identity

$$
v_p\!\left(\binom nj\right)=v_p\!\left(\binom uJ\right).
$$

There are at most $\lfloor\log_pu\rfloor$ carries in the latter
binomial coefficient. Using (2), it follows that

$$
\boxed{
 [G]_{\{p\}}\le\min\{p^{a-1+\delta},u\}
 \le\sqrt{\frac{n-r}{p^{1-\delta}}}\le\sqrt n.
} \tag{5}
$$

This replaces the exponent one for that prime's possible contribution
to $G$ by one half, conditional on the second branch of (3).
It does not apply to the first branch $b>r$.

## A witness supplied by a larger complete index

There is also an exact statement in the other direction. Suppose $i<k<j$
and the assertion is proved at $k$. For a bad triple at $i$, there is a
prime $\ell\ge k$ dividing $\binom nj$ and a position

$$
i\le t<k,\qquad \ell\mid n-t. \tag{6}
$$

If $\ell=k$ is prime, then in fact $\ell^2\mid n-t$.

To prove this, take the common prime supplied by the complete case $k$.
It cannot divide $\binom ni$. Since $\ell\ge k>i$, the denominator
$i!$ has no $\ell$-factor, so none of $n,n-1,\ldots,n-i+1$ is divisible
by $\ell$. Its numerator position in $\binom nk$ must therefore be one
of (6). That position is unique since $\ell\ge k$. At $\ell=k$ the
factor in $k!$ requires numerator valuation at least two.

For $P=\ell^{v_\ell(n-t)}$ and $u=(n-t)/P$, the corresponding column
condition is again exactly

$$
 j\bmod P>t\quad\text{or}\quad
 \left(j\bmod P\le t\ \text{and}\
       \ell\mid\binom{u}{\lfloor j/P\rfloor}\right). \tag{7}
$$

Here $t<k\le\ell$, so the same Lucas argument applies. In particular,
a witness prime $\ell>\sqrt n$ forces the first branch of (7).
The statement only applies when $j>k$, as required by the complete
case being invoked.

## Retaining the valuation in the polynomial argument

The [exact localization lemma](../../methods/details/gcd_localization.md)
proves that a polynomial with multiplicity $m_r$ on row $r$ satisfies

$$
v_p(F(j,n-j))\ge m_r\max\{a-v_p\binom nj,0\}.
$$

This holds without a loss even for prime powers smaller than a row label.
In the weighted divisor inequality, it replaces a selected prime power
$p^a$ by $p^{\min\{a,v_p\binom nj\}}$. The off-maximum and
prime-index denominator constants are unchanged, and coinciding
positions still have total capacity at most one.

For the branch $b\le r$ of (3), this replacement factor is at most
$\min\{p^a,u\}\le\sqrt n$. Thus the square-root bound is usable
in the polynomial argument itself. It still leaves the other Lucas
branch to be handled.

## Why the direct transfer stops

Within an interval containing no new denominator prime, the large-prime
support of $\binom ni$ grows with $i$. Thus a complete lower index
propagates upwards when the prime threshold stays fixed and the
intervening denominator factors are below that threshold.

The unresolved indices in the table occur just after the threshold
changes. The common prime furnished by the preceding complete prime
index can be exactly the prime that has just become too small. The
proposition determines its row congruence and (3) determines its column
condition. Neither condition currently contradicts the badness hypotheses.
Likewise, a witness from a larger complete index belongs to the newly
added numerator factors (6), whose prime divisors were absent from the
original hypothesis. Treating these witnesses as primes with no carries
would reverse their actual Lucas condition.

---
name: research/erdos_699/methods/details/gcd_localization
title: "Erdős 699: polynomial divisibility retaining the actual common-prime valuations"
desc: "An exact Kummer localization lemma replaces each selected small-prime power by its overlap with the column binomial coefficient, without an extra prime-power loss."
created: 2026-09-22T05:00:00Z
updated: 2026-10-13T05:28:09Z
---

# Erdős 699: polynomial divisibility retaining the actual common-prime valuations

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/remaining/details/prime_index_transfer|Forced primes from neighbouring indices]] ·
[[research/erdos_699/methods/details/weighted_ramps|Weighted polynomial certificates]]

***

The weighted polynomial argument can use the actual common-prime
valuations, instead of discarding every contribution from a small prime.
The following localization is exact, including when the prime power is
smaller than the row label.

## Exact localization

Put $c=n-j$ and $B=\binom nj$. Let $0\le r<i\le n$, and suppose an
integer polynomial $F(X,Y)$ has multiplicity at least $m_r$ at every
nonnegative integer point $x+y=r$.

**Lemma.** For every prime $p$ and every $A$ with $p^A\mid n-r$,

$$
v_p(F(j,c))\ge m_r\max\{A-v_p(B),0\}. \tag{1}
$$

The valuation of zero is understood as infinite.

**Proof.** Put $g=v_p(B)$. When $A\le g$ the assertion is immediate.
Otherwise let $d=A-g\ge1$, $M=p^d$, $x=j\bmod M$ and $y=c\bmod M$.
Since $n\equiv r\pmod M$, the sum $x+y$ is either $r\bmod M$ or
$r\bmod M+M$. If $r\ge M$, both possibilities are at most $r$.

Suppose $r<M$ and $x+y>r$. Then $x+y=r+M$, and $y<M$ implies $x>r$.
For every $k=d,\ldots,A$, it follows that

$$
j\bmod p^k\ge x>r=n\bmod p^k.
$$

Kummer's formula

$$
v_p(B)=\sum_{k\ge1}\mathbf1_{\{j\bmod p^k>n\bmod p^k\}}
$$

would give at least $A-d+1=g+1$ carries, a contradiction.
Thus $x+y\le r$ in both cases.

The nonnegative integer point $(r-y,y)$ has coordinate sum $r$ and is
congruent to $(j,c)$ modulo $M$. The Taylor expansion of $F$ around this
integer point has integer coefficients and no nonzero term of degree
less than $m_r$. Both increments are divisible by $M$, proving
$p^{d m_r}\mid F(j,c)$. $\square$

In particular, define the explicit row divisor

$$
d_r=\frac{n-r}{\gcd(n-r,B)}.
$$

Then the lemma gives the unconditional divisibilities

$$\boxed{d_r^{m_r}\mid F(j,c),\qquad
       \operatorname{lcm}_{0\le r<i}d_r^{m_r}\mid F(j,c).} \tag{2}$$

The product of these row divisors need not divide $F$, because different
rows can share small primes. The following bound accounts for that overlap.

## The weighted product under badness

Suppose $(n,i,j)$ is bad for the original threshold $p\ge i$.
For every small prime $p<i$, choose a position $r_p$ maximizing
$A_p=v_p(n-r_p)$, and put

$$P_p=p^{A_p},\qquad
E_p=p^{\min\{A_p,v_p(B)\}}. \tag{3}$$

For nonnegative integer row multiplicities $m_0,\ldots,m_{i-1}$, set

$$
C_* =\prod_{p<i}p^{\displaystyle
 \max_{0\le r<i}\sum_{\substack{0\le t<i\\t\ne r}}
 m_t v_p(|t-r|)},\qquad m_* =\max_t m_t,
$$

and let $H_i=i$ if $i$ is prime and $H_i=1$ otherwise.

**Proposition.** If $F$ has the prescribed multiplicity $m_t$ at every
nonnegative integer point on every row $x+y=t<i$, then

$$
\boxed{
\prod_{t=0}^{i-1}(n-t)^{m_t}
\ \mid\ H_i^{m_*} C_* F(j,c)
          \prod_{p<i}E_p^{m_{r_p}}.
} \tag{4}
$$

Consequently, if $F(j,c)\ne0$, then

$$
\prod_{t=0}^{i-1}(n-t)^{m_t}
\le H_i^{m_*}C_*|F(j,c)|\prod_{p<i}E_p^{m_{r_p}}. \tag{5}
$$

**Proof.** At a small prime $p$, the selected numerator position
contributes $m_{r_p}A_p$. Lemma (1) supplies at least
$m_{r_p}\max\{A_p-v_p(B),0\}$ to $v_p(F(j,c))$.
Their difference is exactly $m_{r_p}\min\{A_p,v_p(B)\}$,
accounted for by $E_p^{m_{r_p}}$.

For $t\ne r_p$, maximality and the ultrametric inequality imply

$$
v_p(n-t)\le v_p(|t-r_p|).
$$

The remaining numerator contribution is therefore bounded by the
$p$-valuation of $C_*$.

For a prime $p\ge i$, at most one of the $i$ consecutive numerator
factors is divisible by $p$. If $p>i$, or if $i$ is composite, a prime
occurring there divides $\binom ni$. Badness then gives $v_p(B)=0$,
and (1) supplies its entire numerator contribution.

The sole possible exception is $p=i$ when $i$ is prime. Write $A$ for
the valuation of its unique divisible numerator factor. If $A\ge2$,
then $p\mid\binom ni$ and again $v_p(B)=0$. If $A=1$, the denominator
$i!$ cancels that prime, but its weighted numerator contribution is at
most $m_*$. The factor $H_i^{m_*}$ covers precisely this possibility.
This proves (4) prime by prime, and (5) follows. $\square$

Thus every existing weighted certificate remains valid after replacing
its selected loss factor $P_p^{m_{r_p}}$ by the smaller
$E_p^{m_{r_p}}$. No additional factor $p^{\lceil\log_p i\rceil}$ is
needed.

For example, with $M=\sum_t m_t$ and $L=\sum_t t m_t$, a positive
polynomial bound $|F(j,c)|\le C_F n^D$ gives, for $n>L$,

$$
n^{M-D}\left(1-\frac Ln\right)
\le H_i^{m_*}C_* C_F\prod_{p<i}E_p^{m_{r_p}}. \tag{6}
$$

This uses the elementary inequality
$\prod_t(1-t/n)^{m_t}\ge1-L/n$.

## Collisions of maximal positions

The previous collision argument is unchanged. If a group of distinct
small primes has selected position $r$, then

$$
\prod_{p:r_p=r}E_p
\mid\gcd(n-r,B),\qquad
\prod_{p:r_p=r}E_p\le n-r\le n. \tag{7}
$$

Indeed each factor contributes exactly the corresponding prime-power
part of that gcd. A group of two or more primes therefore still has
exponent capacity at most one.

At a singleton position, every previous cofactor bound on $P_p$ remains
valid for $E_p\le P_p$. Additional information about $v_p(B)$ can
improve that capacity without changing the other small-prime bounds.

## Application to the forced-prime alternative

The [neighboring-index proposition](../../remaining/details/prime_index_transfer.md)
forces a common prime $p$ with

$$
n=p^a u+r,\qquad a\ge2,\quad p\nmid u,\quad 0\le r<p.
$$

Write $j=p^a J+b$, $0\le b<p^a$. In the branch $b\le r$, the first
$a$ base-$p$ digits produce no carry, so

$$
v_p(B)=v_p\binom uJ\le\lfloor\log_pu\rfloor.
$$

The selected factor at that prime consequently satisfies

$$
\boxed{E_p\le\min\{p^a,u\}\le\sqrt{n-r}\le\sqrt n.} \tag{8}
$$

The selected position is indeed $r$: here $p<i<2p$ and $a\ge2$,
so any second multiple of $p$ in the numerator has valuation one.
Thus a singleton at this prime has capacity at most $1/2$ in (6).
If it shares its position with another small prime, the group bound (7)
continues to apply.

This is a conditional improvement to the polynomial argument. The other
Lucas branch, $b>r$, remains possible and receives no square-root bound
from this reasoning.

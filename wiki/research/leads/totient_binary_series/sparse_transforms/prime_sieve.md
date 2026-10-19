---
name: research/leads/totient_binary_series/sparse_transforms/prime_sieve
title: A Reduced-Denominator Obstruction for Literal Prime Sieves
desc: |
  A cyclotomic factor survives in the reduced denominator for every finite
  prime sieve, and its square outgrows the full positive remainder.
problems:
- 249
review_status: unreviewed
created: 2026-09-17T07:14:44Z
updated: 2026-09-17T07:14:44Z
---

***

Write $A(x)=\sum_{n\ge1}\varphi(n)x^n$, $S=A(1/2)$, and
$B(x)=x/(1-x)^2$. These are the conventions of the
[[research/leads/totient_binary_series/_index|parent sketch]]. All new arguments
here are author-recorded and unreviewed. The obstruction concerns the
literal rational sieve sums defined below, with their reduced denominators.

## The exact family and its entire remainder

For a squarefree positive integer $Q$ define

$$
M_Q(x)=\sum_{d\mid Q}\mu(d)B(x^d).
$$

Then, for $|x|<1$,

$$
M_Q(x)=\sum_{\substack{n\ge1\\(n,Q)=1}}A(x^n).
\tag{1}
$$

Indeed, the coefficient of $x^m$ on the left is
$m\sum_{d\mid(m,Q)}\mu(d)/d$. Write $m=m_0m_1$, where every prime
factor of $m_0$ divides $Q$ and $(m_1,Q)=1$. The coefficient on the right
is $\sum_{n\mid m_1}\varphi(m/n)
=\varphi(m_0)\sum_{n\mid m_1}\varphi(m_1/n)
=\varphi(m_0)m_1$, the same quantity. Absolute convergence follows from
$\varphi(n)\le n$ and justifies the analytic identity.

From now on let $Q$ be squarefree with largest prime factor $P\ge5$,
and let $q$ be the least prime not dividing $Q$. The prime divisors of
$Q$ need not be consecutive. Put

$$
M_Q=M_Q(1/2)
 =\sum_{d\mid Q}\frac{\mu(d)2^d}{(2^d-1)^2},
\qquad R_Q=M_Q-S.
$$

The entire omitted series is positive and obeys

$$
2^{-q}\le R_Q
 =\sum_{\substack{n>1\\(n,Q)=1}} A(2^{-n})
 \le\frac{2^{1-q}}{(1-2^{-q})^2}.
\tag{2}
$$

The least admissible index is $q$, and $A(t)\ge t$ for $0<t<1$.
For the upper bound use $A(t)\le t/(1-t)^2$ and include all $n\ge q$.
Both bounds concern the full infinite remainder in the same parameter
$Q$ as the rational approximant.

## Which denominator factors cannot cancel

Let $\Psi_Q(X)$ denote the $Q$th cyclotomic polynomial and put
$C_Q=\Psi_Q(2)$. Define

$$
G_Q=\frac{C_Q}{\gcd(C_Q,P)}.
$$

**Lemma 1.** Every prime factor $\ell$ of $G_Q$ satisfies
$\operatorname{ord}_{\ell}(2)=Q$. Moreover

$$
G_Q\ge\frac{C_Q}{P}>\frac{2^{\varphi(Q)-2}}P.
\tag{3}
$$

*Proof.* The Möbius formula for the cyclotomic value is

$$
C_Q=\prod_{d\mid Q}(2^d-1)^{\mu(Q/d)}.
\tag{4}
$$

It is an odd positive integer. Fix an odd prime $\ell$ and put
$m=\operatorname{ord}_{\ell}(2)$. If $m\nmid Q$, no factor in (4)
has nonzero $\ell$-adic valuation. If $m\mid Q$, write $Q=mh$.
The squarefreeness of $Q$ makes $(m,h)=1$, and $\ell\nmid m$ since
$m\mid\ell-1$. The elementary valuation formula

$$
v_\ell(2^{me}-1)=v_\ell(2^m-1)+v_\ell(e)
\qquad(e\ge1)
\tag{5}
$$

gives

$$
v_\ell(C_Q)=
\begin{cases}
v_\ell(2^Q-1),&m=Q,\\
1,&h=\ell,\\
0,&\text{otherwise}.
\end{cases}
\tag{6}
$$

For completeness, substitute $d=me$ in (4). The constant term in
(5) sums to zero over $e\mid h$ when $h>1$. Because $h$ is squarefree,
the remaining sum is $\sum_{e\mid h,\,\ell\mid e}\mu(h/e)$,
which equals one exactly for $h=\ell$. Formula (5) follows by the
binomial expansion of $(1+\ell^a u)^\ell$ for odd $\ell$ and
$\ell\nmid u$, followed by induction and the case of an exponent
coprime to $\ell$.

In the nonprimitive case $Q=m\ell$ with $m\mid\ell-1$, every other
prime divisor of $Q$ is smaller than $\ell$. Thus $\ell=P$, and its
exponent in $C_Q$ is exactly one. Removing $\gcd(C_Q,P)$ therefore
removes every possible nonprimitive factor.

Finally (4) and $\sum_{d\mid Q}\mu(Q/d)d=\varphi(Q)$ imply

$$
C_Q=2^{\varphi(Q)}
 \prod_{d\mid Q}(1-2^{-d})^{\mu(Q/d)}
 >\frac14\,2^{\varphi(Q)}.
$$

To see the strict lower bound, omit the reciprocal factors and bound the
remaining product below by the product over all positive integers.
Its first two factors are $1/2$ and $3/4$; its tail is at least
$1-\sum_{d\ge3}2^{-d}=3/4$. Their product is $9/32>1/4$.
This proves (3). $\square$

This proof does not invoke a primitive-divisor existence theorem. It
identifies and removes the possible exceptional cyclotomic prime directly.

**Lemma 2.** If $D_Q$ is the positive reduced denominator of $M_Q$, then

$$
G_Q^2\mid D_Q,
\qquad
D_Q>\frac{2^{2\varphi(Q)-4}}{P^2}.
\tag{7}
$$

*Proof.* Let $\ell\mid G_Q$. Its order is $Q$, so it divides
$2^Q-1$ and divides no $2^d-1$ for a proper divisor $d\mid Q$.
Consequently only the $d=Q$ summand of $M_Q$ has a denominator divisible
by $\ell$. Its numerator $\mu(Q)2^Q$ is an $\ell$-adic unit. Therefore

$$
v_\ell(M_Q)=-2v_\ell(2^Q-1)=-2v_\ell(G_Q).
$$

Adding the other $\ell$-integral summands cannot change that negative
valuation. Multiplying the surviving prime powers proves the divisibility;
(3) gives the inequality. $\square$

The readily available common denominator $(2^Q-1)^2$ is an upper bound.
It plays no role in this reduced-denominator lower bound.

## The obstruction after exact denominator clearing

**Theorem 3.** For every squarefree $Q$ with largest prime factor
$P\ge5$,

$$
D_Q R_Q>
 \frac{2^{2\varphi(Q)-q-4}}{P^2}
 \ge\frac{2^{2P-9}}{P^2}.
\tag{8}
$$

Consequently $D_QR_Q\to\infty$ along every sequence of squarefree
$Q\to\infty$. For primorials the sharper lower bound
$D_QR_Q>2^{2P-8}/P^2$ holds.

*Proof.* Combine (2) and (7). If $3\nmid Q$, then $q\le3$ and
$\varphi(Q)\ge P-1$, whence $2\varphi(Q)-q-4\ge2P-9$.
If $3\mid Q$, then $\varphi(Q)\ge2(P-1)$, since $3$ and $P$ are
distinct prime divisors. Bertrand's postulate gives a prime between $P$
and $2P$, which cannot divide $Q$, so $q<2P$. Therefore
$2\varphi(Q)-q-4>2P-8$. This case includes every primorial with $P\ge5$.
Finally, only finitely many squarefree integers have all prime factors
bounded by a fixed number, so $Q\to\infty$ forces $P\to\infty$.

For that external prime bound, the source states that for every integer
$n\ge1$ there is a prime with $n<p\le2n$; at $n=P\ge5$ the upper
endpoint is composite, so $q<2P$. See
[Erdős, *Beweis eines Satzes von Tschebyschef* (1932), pp. 197-198,
section 5](https://users.renyi.hu/~p_erdos/1932-01.pdf).
Its source statement was inspected; the classical theorem is an external
input, not a new proof claimed here. $\square$

If $S=a/b$ were rational, then

$$
bD_Q(M_Q-S)=bD_QM_Q-aD_Q\in\mathbb Z_{>0}.
$$

For each fixed $b$, (8) shows that these particular integers grow without
bound. They cannot eventually lie strictly between zero and one. The same
holds for any larger integer denominator clearing $M_Q$.

This closes only the use of $M_Q$ itself as an approximation with a small
denominator-cleared error, for every choice of the finite prime set.
It does not compare different $Q$ at a prescribed reduced denominator or
claim that primorials are extremal in such a comparison. It does not exclude
signed combinations of different $M_Q$, subtraction of further rational
terms, other sieve weights, or multiplier approximants with independent
cancellation. Those operations change both the reduced denominator and
the full remainder, and require new estimates.

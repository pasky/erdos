---
name: research/leads/totient_binary_series/arithmetical_windows/classification
title: The Sole Excess Pair Admitting an Eventual Progression Certificate
desc: |
  Exact existence conditions for an eventual whole-progression carry
  assertion, and the unique pair with actual divisibility and dyadic excess.
problems:
- 249
research_state: ready
review_status: unreviewed
created: 2026-09-17T08:40:00Z
updated: 2026-09-17T08:46:27Z
---

***

An assertion on an entire arithmetic progression is much stronger than
divisibility at one of its members. The distinction permits an exact
classification in the setting below. This is a complete author-recorded
argument, without independent review. It uses the author-recorded
prime-square isolation theorem from
[[research/leads/totient_binary_series/arithmetical_windows/_index|the progression
argument]], Theorem 4, and inherits its explicit Dirichlet and quadratic
reciprocity dependencies. It does not resolve
[[problems/irrationality/E0249/_index|Problem 249]].

Put

$$
\Phi_n=\sum_{r=1}^n\varphi(r)2^{n-r},\qquad
W_m(N)=\sum_{i=0}^{m-1}2^i\varphi(N-i)\quad(N\ge m),
$$

with $\varphi(1)=1$. For positive integers $n,m$, say that an
*eventual progression certificate at $(n,m)$* exists if there are
integers $M\ge1$ and $N_0\ge1$ such that

$$
N\ge N_0,\quad N\equiv n\pmod M
 \quad\Longrightarrow\quad 2^m\mid\Phi_N.
\tag{1}
$$

This definition does not require $2^m\mid\Phi_n$: the representative
$n$ might be below $N_0$. Whenever actual divisibility at $n$ is used,
it is a separate hypothesis.

## Exact existence at a fixed representative

**Proposition 1.** If (1) holds, then

$$
m\le i+v_2(\varphi(n-i))+1
\quad\text{for every }0\le i<m\text{ with }n-i>0.
\tag{2}
$$

If $n\ge m$, these inequalities are also sufficient for existence of
some $M,N_0$ satisfying (1).

*Proof.* For all sufficiently large $N$,
$\Phi_N\equiv W_m(N)\pmod{2^m}$. Apply the prime-square isolation
theorem to this fixed sum, with shifts $-i$ and coefficients $2^i$.
For each chosen position with $n-i>0$, it supplies infinitely many
$N\equiv n\pmod M$ for which

$$
v_2(W_m(N))=i+v_2(\varphi(n-i))+1.
$$

Some such indices exceed both $N_0$ and $m$, proving (2). Only the
selected argument at the base needs to be positive; the constructed
indices eventually make all the arguments positive.

Conversely let $n\ge m$ and suppose (2) holds. Choose $M$ divisible by
$2t\operatorname{rad}(t)$ for every $t=n-i$, $0\le i<m$, where
$\operatorname{rad}(t)$ is the product of its distinct prime factors
and $\operatorname{rad}(1)=1$. At $N=n+hM$, $h\ge1$, write

$$
N-i=tq_i,\qquad q_i=1+hM/t.
$$

Then $q_i>1$ is odd and coprime to $t$. Multiplicativity gives
$\varphi(N-i)=\varphi(t)\varphi(q_i)$, divisible by
$2\varphi(t)$. By (2), every $2^i\varphi(N-i)$ is divisible by
$2^m$. Thus (1) holds with $N_0=n+M$. $\square$

The necessity isolates each position separately; it assumes no
independence of the odd parts of several totients. The sufficiency uses
no bound for the size of its modulus or its first large member.

## Classification with actual divisibility and excess

**Theorem 2.** Let $n,m\ge1$. An eventual progression certificate (1),
actual divisibility $2^m\mid\Phi_n$, and the inequality $2^m>n+2$
hold together if and only if

$$
(n,m)=(5,3).
\tag{3}
$$

In particular the modulus and threshold may depend arbitrarily on
$n,m$. There is no assumption that the representative exceeds either.

*Proof.* Put $e=v_2(\varphi(n))$. Position zero in (2) gives
$m\le e+1$, hence $2^m\le2\varphi(n)$. If $n$ is even,
$\varphi(n)\le n/2$, contradicting $2^m>n+2$. At $n=1$,
$\Phi_1=1$ contradicts actual divisibility. Thus $n\ge3$ is odd.
Since

$$
2^m>n+2>\varphi(n)\ge2^e,
$$

we have $m=e+1$. Also $\varphi(n)<2^{e+1}$, so its odd part is one:

$$
\varphi(n)=2^e.
\tag{4}
$$

Here $e\ge1$, so position one in (2) is available. It gives
$2^{e-1}\mid\varphi(n-1)$. Since $n-1$ is even and
$n+2<2^{e+1}$,

$$
0<\varphi(n-1)\le(n-1)/2<2^e.
$$

Consequently

$$
\varphi(n-1)=2^{e-1}.
\tag{5}
$$

The elementary classification of integers $t$ with $\varphi(t)$ a
power of two is

$$
t=2^a\prod_{j\in J}F_j,\qquad F_j=2^{2^j}+1,
\tag{6}
$$

where $a\ge0$ and $J$ is a finite set of indices for which $F_j$ is
prime. Indeed each odd prime factor has exponent one and its predecessor
is a power of two. If $2^h+1$ is prime, writing $h=2^ju$ with $u$ odd
shows $u=1$, since $x+1$ divides $x^u+1$ when $u$ is odd.
Conversely every number in (6) has totient a power of two. This uses
no assertion about how many Fermat primes exist.

Write the odd $n$ as a product of $r\ge1$ distinct Fermat primes.
Expanding $\prod_j(1+2^{2^j})$ gives exactly $2^r$ nonzero binary
digits: the subset sums of the distinct powers $2^j$ are all distinct,
so no carries occur. Subtracting one from the odd number removes only
its final digit. Thus $n-1$ has $2^r-1$ nonzero binary digits.
By (5)-(6), it also has $2^s$ such digits for some $s\ge0$; multiplying
by a power of two does not change their number. Therefore
$2^r-1=2^s$, forcing $r=1,s=0$. We obtain

$$
n=2^e+1\text{ prime},\qquad e=2^a.
\tag{7}
$$

For $e=1$, $n=3,m=2$ fails the excess condition $4>5$.
For $e=2$ we have the proposed pair $(5,3)$. For $e=4$, the pair
$(17,5)$ fails actual divisibility, because
$\Phi_{17}=179248=16\cdot11203$. These small values follow from
$\Phi_j=2\Phi_{j-1}+\varphi(j)$, starting at $\Phi_0=0$.
The exact totients through 17 are

$$
1,1,2,2,4,2,6,4,6,4,10,4,12,6,8,8,16.
$$

It remains to exclude every $e\ge8$ in (7), including any arising
from an unknown Fermat prime. Then $4\mid e$ and position three in
(2) gives $v_2(\varphi(n-3))\ge e-3$. Put $z=2^{e-1}-1$,
so $n-3=2z$ and $\varphi(n-3)=\varphi(z)$. We have
$z\equiv7\pmod8$ and $\gcd(z,15)=1$: the latter follows from
$e-1\equiv3\pmod4$, hence $z\equiv7\pmod{15}$. As
$0<\varphi(z)<2^{e-1}$, the only possibilities are

$$
\varphi(z)\in
\{2^{e-3},\,2^{e-2},\,3\cdot2^{e-3}\}.
\tag{8}
$$

If it is a power of two, (6) makes the odd $z$ a product of
distinct Fermat primes. None is 3 or 5, so every one is $1\pmod8$.
This contradicts $z\equiv7\pmod8$.

Otherwise $\varphi(z)=3\cdot2^{e-3}$. The totient factorization
formula and $3\nmid z$ show that every prime factor of $z$ occurs
once. Exactly one of their predecessors has odd part three; all the
others have odd part one. Thus all but one are Fermat primes at least
17, and the remaining prime is $p=3\cdot2^h+1$ for $h\ge1$.
The residue $z\equiv7\pmod8$ forces $p\equiv7\pmod8$. At $h=1$
this gives $p=7$; at $h=2$ it gives residue 5, and at $h\ge3$
residue 1. Hence $z$ is 7 times a product of distinct Fermat primes
at least 17. It follows that

$$
\frac z{\varphi(z)}
=\frac76\prod_{j\in J}(1+2^{-2^j})
<\frac76\prod_{j\ge2}(1+2^{-2^j})
=\frac76\frac{16}{15}=\frac{56}{45}.
\tag{9}
$$

For the product identity, apply
$\prod_{j=0}^{r}(1+x^{2^j})=(1-x^{2^{r+1}})/(1-x)$ at $x=1/16$
and take the limit. Every finite subset has strictly smaller product,
irrespective of which Fermat numbers are prime. But the assumed value
of $\varphi(z)$ gives

$$
\frac z{\varphi(z)}
=\frac43-\frac{1}{3\cdot2^{e-3}}
\ge\frac{127}{96}>\frac{56}{45},
\tag{10}
$$

a contradiction. This proves the necessity of (3).

Conversely $\Phi_5=40$ is divisible by 8 and $8>5+2$.
For $N=5+200h$, $h\ge1$, write $N=5u$ with $u=1+40h>1$
odd and coprime to 5. Then $\varphi(N)=4\varphi(u)$ is divisible
by 8. Also $N-1=4v$ with $v=1+50h>1$ odd, so
$\varphi(N-1)=2\varphi(v)$ is divisible by 4. Finally
$\varphi(N-2)$ is even. Therefore

$$
\Phi_N\equiv
\varphi(N)+2\varphi(N-1)+4\varphi(N-2)\equiv0\pmod8.
$$

This establishes (1), for example with $M=200,N_0=205$, and
completes the proof. $\square$

## Effect on the binary-tail argument

The [[research/leads/totient_binary_series/_index|dyadic reduction]] would
exclude every dyadic rational value of the target if there were
infinitely many $n$ with $2^{v_2(\Phi_n)}>n+2$. Theorem 2 rules out
obtaining such infinitely many distinct indices with precision that is
also certified eventually on their entire containing progressions,
even with a different progression at each index.

It does not bound the actual excess at selected members of a class.
The larger excess-positive indices in the
[[research/leads/totient_binary_series/evidence/_index|finite evidence]]
simply admit no certificate of type (1) at any excess-producing
precision. A construction using additional factorization or
prime-cofactor conditions on a selected subfamily is outside the
theorem. So are linear combinations of several tails and the
[[research/leads/totient_binary_series/integer_interpolation/_index|integer
interpolation criterion]]. No family beyond the explicitly quantified
whole-progression assertion is ruled out.

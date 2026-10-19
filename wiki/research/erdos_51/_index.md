---
name: research/erdos_51
title: Least totient preimages
desc: The exact all-preimage forcing target, substitution and cross-prime obstructions, and a finite-covering obstruction for shifted divisors. No family with unbounded least-preimage ratio is constructed.
tags: []
sources: []
created: 2026-10-15T11:06:18Z
updated: 2026-10-15T11:06:18Z
---

# Least totient preimages

[[research/_index|..]]

***

This folder's results that are not drawn from a cited source are Plasma AI's,
credited to Plasma AI. They are author-recorded and settle no instance of the
question.

The substitution, explicit witnesses and covering obstruction below have
elementary arguments here. Ford's results and the convenient-integer
construction are imported through the cited connections pages at their stated
scope: statement-level use for Ford, and a partial reconstruction with imported
counting steps for the convenient construction. The cited historical finite
census supplies no universal conclusion.

## Target and quantifiers

[[problems/arithmetic_functions/E0051/_index|Problem 51]] asks for an infinite
set of totients $a$ whose least preimage $n_a$ satisfies $n_a/a\to\infty$.
Write $\ell(v)=\min\{n:\varphi(n)=v\}$. Since
$n/\varphi(n)=\prod_{p\mid n}p/(p-1)$,

$$
\frac{\ell(v)}{v}=\min_{\varphi(n)=v}\ \prod_{p\mid n}\frac{p}{p-1}.
$$

As [[research/erdos_416/connections|the Problem 416 connections page]] records,
a positive answer is equivalent to the unboundedness of this ratio over
totients. If it is unbounded, choose increasing values $v_j$ with
$\ell(v_j)/v_j>j$: the finitely many values below any fixed bound have
bounded ratios. The minimum runs over **every** preimage. A preimage with many
small prime factors does not raise the ratio while another preimage of the
same value has few: $\varphi(105)=\varphi(65)=48$, with ratios $35/16$ and
$65/48$, and $\varphi(6)=\varphi(3)=2$.

A sufficient condition is a family of totients $v_j$ such that every preimage
of $v_j$ has $\prod_{p\mid n}p/(p-1)\ge K_j$, with $K_j\to\infty$. The common
divisor form on the problem page is the special case in which every preimage
of $v_j$ is divisible by one $k_j$ with $k_j/\varphi(k_j)=K_j$.

## Substitution and merging

**Substitution principle.** Let $n=AB$ be a preimage of $v$ with
$\gcd(A,B)=1$. For every $B'$ with $\varphi(B')=\varphi(B)$ and
$\gcd(A,B')=1$, the integer $AB'$ is also a preimage of $v$. This is
multiplicativity of $\varphi$. Both negative controls are instances:
$105=5\cdot21$ and $65=5\cdot13$ with $\varphi(21)=\varphi(13)=12$, and
$6=3\cdot2$ and $3=3\cdot1$ with $\varphi(2)=\varphi(1)=1$.

Consequently, if every preimage of $v$ is divisible by a prime $p$, then for
every preimage $n=AB$ with $p\mid B$ and $\gcd(A,B)=1$, every preimage of
$\varphi(B)$ coprime to $A$ is divisible by $p$. A forcing argument must
control every coprime sub-factor of every preimage in this way.

**Merging.** Let distinct primes $p_1,\ldots,p_s$, $s\ge2$, divide a preimage
$n$ exactly once, and suppose $q=\prod_i(p_i-1)+1$ is a prime not dividing
$n/\prod_ip_i$. Then $n'=nq/\prod_ip_i$ is a preimage of $\varphi(n)$ with a
strictly smaller ratio: since $q-1\ge p_1-1$,

$$
\frac{q}{q-1}\le\frac{p_1}{p_1-1}<\prod_{i=1}^s\frac{p_i}{p_i-1}.
$$

The collision $105\to65$ merges $3$ and $7$ into $13$. Thus a set $F$ of
primes can be forced into every preimage of $v$ only if the following holds
for every preimage $n$: for every set $T$ of at least two primes dividing $n$
exactly once, put $q=\prod_{p\in T}(p-1)+1$. If $q$ is prime and does not
divide $n/\prod_{p\in T}p$, then $F\cap T\subseteq\{q\}$. Indeed the
substitution removes every prime of $T$ other than $q$ itself. The exception
is essential: $T=\{2,p\}$ gives $q=p$, so the substitution removes only $2$.
For example the value $10$ has just the preimages $11,22$ and forces $11$,
although merging $2,11$ in $22$ is allowed. The preimage list follows from
$v_2(10)=1$: an odd part has at most one prime factor, whose prime-power
totient can equal $10$ only at $11$; a factor $4$ would leave the impossible
odd totient $5$. The condition fails for the products
$\prod_{i\le k}(p_i-1)$ of the rejected claim whenever $3$ and $7$ occur once
and $13$ does not.

**Two-adic budget.** Each odd prime divisor of a preimage $n$ of $v$
contributes an even factor $p-1$, so $n$ has at most $s=v_2(v)$ distinct odd
prime factors. If $r_1<r_2<\cdots$ are the odd primes, every preimage satisfies

$$
\frac{n}{\varphi(n)}\le2\prod_{i=1}^s\frac{r_i}{r_i-1}.
$$

Thus forcing a ratio at least $K$ requires this finite product to be at least
$K$. This is a necessary budget, not a construction controlling preimages.

There is also a bound using the number of prime factors of the **value**.
For every preimage $n$ of $v$, distinct primes $p\mid n$ give distinct
divisors $p-1$ of $v$. Hence

$$
\log\frac{n}{\varphi(n)}
\le\sum_{p\mid n}\frac1{p-1}
\le\sum_{d\mid v}\frac1d
\le\prod_{q\mid v}\frac{q}{q-1}.
\tag{1}
$$

If $\omega(v)\le s$, the last product is at most the corresponding product
over the first $s$ primes. Thus bounded $\omega(v)$ bounds the ratio of
every preimage uniformly, not just the least one. Any family answering the
question positively must have unbounded $\omega(v)$.

## Small forcing witnesses

**A power of two.** Every preimage of $2^{32}$ is even. An odd preimage of
$2^m$ is a product of distinct primes $2^j+1$ with exponents $j$ summing to
$m$. For $j\le32$ such primes occur only for $j=1,2,4,8,16$, since $2^j+1$ can
be prime only when $j$ is a power of two and $2^{32}+1=641\cdot6700417$. These
exponents sum to $31$. Thus every preimage has ratio at least $2$; the
preimage $2^{33}$ gives $\ell(2^{32})/2^{32}=2$.

**Forcing the prime three.** For $k\ge1$ the preimages of $2\cdot3^k$ are
$3^{k+1}$ and $2\cdot3^{k+1}$, together with $q$ and $2q$ when
$q=2\cdot3^k+1$ is prime. Indeed $v_2(2\cdot3^k)=1$ allows at most one odd
prime factor. If $4\mid n$, its exact power of two must be $4$, leaving the
impossible odd totient $3^k$ for its odd part. When $2\cdot3^k+1$ is
composite, every preimage is divisible by $3$ and the least-preimage ratio is
exactly $3/2$. The least case is
$v=54$, with preimages $81$ and $162$.

**A high power does not force its prime.** The preimages of
$2500=4\cdot5^4$ are $2761=11\cdot251$, $3125$, $5522$ and $6250$. The least
one is prime to $5$, with ratio about $1.104$: the factor $5^4$ is split
between $11-1=2\cdot5$ and $251-1=2\cdot5^3$. To see that the list is
complete, write $n=2^am$ with $m$ odd. If $a=2$ then $\varphi(m)=2\cdot5^4$
makes $m$ a prime power, impossible since $4\nmid1250$ and
$1251=3^2\cdot139$. The case $a=3$ leaves the impossible odd totient $625$,
and $a\ge4$ contributes too many factors of two.
So $\varphi(m)=2500$, and $m$ has at most two odd prime factors. One factor
gives $m=5^5$, as $2501=41\cdot61$. Two factors each contribute exactly one
factor two, so neither is $5$, both occur once, and they are primes
$2\cdot5^b+1$ with exponents summing to four; among $3,11,51,251,1251$ only
$11\cdot251$ qualifies.

## Combining forced divisors

The value $54$ forces $3$ and $2^{32}$ forces $2$, but their product does not
force $6$. The product $54\cdot2^{32}$ has the preimage $81\cdot2^{33}$, with
ratio $3$, and also

$$
N=5\cdot13\cdot17\cdot19\cdot257\cdot65537,\qquad
\varphi(N)=4\cdot12\cdot16\cdot18\cdot256\cdot65536=54\cdot2^{32},
$$

which is odd and prime to $3$, with ratio about $1.525$. The primes $13$ and
$19$ are **cross primes**: $13-1=2^2\cdot3$ and $19-1=2\cdot3^2$ draw on the
three-part of the first value and the two-part of the second. Primality of
the Fermat factors used here can be checked elementarily: a prime divisor of
$2^{2^t}+1$ has multiplicative order $2^{t+1}$ for $2$, hence is
$1\pmod{2^{t+1}}$. For $17$ and $257$ no such possible prime divisor lies
below the square root. For $65537$ the only candidates below $257$ are $97$
and $193$, and the remainders are $62$ and $110$, respectively. A product lemma
(forced $k_1$ and forced $k_2$ give forced $k_1k_2$) therefore fails in this
direct form. A combination must control preimage factorizations using primes
$q$ with $q-1$ dividing the combined value and drawing on both factors;
excluding every such prime would be one sufficient way to remove this issue.
The convenient multipliers of
Pollack, Pomerance and Treviño's Lemma 4.1, recorded on
[[research/erdos_49/connections|the Problem 49 connections page]], preserve the
preimage set of one fixed seed by multiplying each preimage by the same
integer of bounded totient ratio. Their recorded conclusion therefore
transports a fixed divisor and a bounded ratio.

Even preserving just the forced prime $3$ fails for every nontrivial power of
two multiplying the seed $54$. Put $v_t=54\cdot2^t$ for $t\ge1$.
The value $v_1=108$ has the prime preimage $109$; $v_2$ has the preimage
$247=13\cdot19$; for $t\ge3$, the value $v_t$ has the preimage
$247\cdot2^{t-1}$. In the latter two cases use
$\varphi(247)=12\cdot18=216$. Every listed preimage is prime to $3$.

## A fixed covering cannot control all divisor products

A possible forcing construction would write $v=2^aw$, with $w$ odd, and
certify the compositeness of all unwanted candidates $2^cd+1$, where
$d\mid w$ and $1\le c\le a$. The following obstruction applies to the
stronger proposed certificate that uses one fixed finite set of primes to
cover every $c\ge1$ for all undesignated divisors $d>1$.

Let $Q$ be a nonempty finite set of odd covering primes, put
$M=\prod_{q\in Q}q$, and let $h=\varphi(M)$. Let $r$ be the number of
distinct prime factors of $w$ outside $Q$. There are at least
$\lfloor r/h\rfloor$ distinct divisors $d>1$ of $w$ for which no prime in
$Q$ divides $2^cd+1$ whenever

$$
c\equiv0\pmod{\lambda},\qquad
\lambda=\operatorname{lcm}_{q\in Q}\operatorname{ord}_q(2).
\tag{2}
$$

*Proof.* Partition $h\lfloor r/h\rfloor$ of the distinct prime factors
outside $Q$ into blocks of $h$. In each block, the $h+1$ successive partial
products, starting with $1$, lie in the group
$(\mathbb Z/M\mathbb Z)^\times$ of order $h$. Two coincide, so their
quotient is a nonempty product $d$ of primes in the block with
$d\equiv1\pmod M$. The different blocks give pairwise coprime, hence
distinct, divisors $d>1$. For $c$ in (2), $2^c\equiv1\pmod q$ for every
$q\in Q$, and consequently $2^cd+1\equiv2\pmod q$. $\square$

Therefore, if the designated divisor set has size $b$, such a fixed cover
requires $r<(b+1)\varphi(M)$. For the finite exponent range $c\le a$, the
same obstruction applies when $a\ge\lambda$. Divisors of $w$ are closed
under products only when the product still divides $w$; the disjoint blocks
make every product used in this argument legitimate.

For fixed $Q$ and $b$, the bound on $r$ bounds $\omega(v)$: primes of $v$
are $2$, the $r$ primes of $w$ outside $Q$, and at most $|Q|$ others.
Inequality (1) then bounds every preimage ratio. Consequently a fixed cover
with boundedly many designated divisors cannot produce the required
unbounded-ratio family. This conclusion concerns the specified covering
certificate; an uncovered candidate need not be prime. Covers with growing
$Q$, growing designated sets, or exponent bounds
$a<\lambda$ are outside this obstruction. Even a successful compositeness
certificate must still show that $v$ is a totient and that **every**
factorization giving a preimage includes the proposed divisor $k$.

## Remaining gap

A positive answer by forcing needs totients all of whose preimages share
divisors $k$ with $k/\varphi(k)$ unbounded. Every $k$ with $k/\varphi(k)>2$ is
divisible by $2p$ for an odd prime $p$ or has at least three odd prime
factors; the least are $6$ and $10$, and $105$ among odd moduli. The Problem
416 connections page records that Ford found no totient with all preimages
divisible by $6$ or by $10$, and that a computation found none up to $10^7$
for either. No mechanism here forces even $k=6$. The obstruction is the one
exhibited above: alternative factorizations through primes $q$ with $q-1$
dividing the value, either merging forced primes or crossing between forced
factors.

The fixed-cover test above does not repair this: products of sufficiently many
prime factors produce undesignated divisors outside the cover. Reopening this
construction requires explicit control of the cover as it grows and of every
remaining preimage factorization, while $k/\varphi(k)$ grows. Transport of
one seed, or one unusually large preimage, provides neither condition. No such
family is constructed here.

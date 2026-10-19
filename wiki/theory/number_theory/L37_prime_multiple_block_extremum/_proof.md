---
name: theory/number_theory/L37_prime_multiple_block_extremum/_proof
title: Two halves and a rectangular grid of primes
desc: Distinct translates give the lower bound, and repeated prime patterns with Chinese remaindering attain it in an exact integer block.
created: 2026-10-14T18:42:37Z
updated: 2026-10-14T18:42:37Z
---

***

Fix $2<\alpha<3$ and $u\ge1$. Let $G_\alpha(u)$ be the minimum in
the statement of L37. We prove $G_\alpha(u)=\lceil2\sqrt u\rceil$.

**Lower bound.** First take an open real interval $I=(A,B)$ of length
$>2P$, where $P=p_u$, and split it at $M=(A+B)/2$. Each open half has
length $>P$, so each contains a multiple of each of the $u$ primes.
Let $r$ be the largest number of these primes dividing a single integer
in the two halves, excluding the midpoint. If the maximum occurs at $m$
in the left half, that half contains at least $\lceil u/r\rceil$
distinct multiple locations, by counting prime incidences. For each of the
$r$ primes $p\mid m$, choose the least integer $e\ge0$ for which
$m+2^e p>M$. This point lies in the right half. Indeed, if $p>M-m$,
then $m+p<M+P<B$; otherwise minimality gives
$2^e p\le2(M-m)$ and $m+2^e p\le2M-m<B$.
The points for different primes are distinct: an equality
$2^e p=2^f q$ for primes forces $p=q$, including when one prime is 2.
Thus the right half has at least $r$ multiple locations. Reflect the
argument if the maximum is in the right half. Altogether there are at
least

$$
r+\lceil u/r\rceil\ \ge\ \lceil2\sqrt u\rceil
$$

distinct locations. A block of $K=\lfloor\alpha P\rfloor\ge2P$
consecutive integers is exactly the integer intersection of an open interval
of length $K+1/2>2P$ (extend its endpoints by $3/4$). The same bound
therefore applies to every block in the definition of $G_\alpha(u)$.

**A rectangular prime grid.** For any fixed positive integers $r,s$ and
any $\delta>0$, there are distinct primes

$$
p_{ij}=p_0+a_i+b_j\qquad(1\le i\le r,\ 1\le j\le s)
$$

with $a_1=b_1=0$, both offset lists strictly increasing, and all primes
in $[p_0,(1+\delta)p_0]$. Here is an elementary counting proof using the
prime number theorem. Put $L=\lceil(\log X)^{s+2}\rceil$. Partition
$[X,2X]$ into integer blocks of at most $L$ consecutive integers. The
prime number theorem implies, for arbitrarily large $X$, that some full
block contains $w\ge L/(2\log X)$ primes; the final incomplete block
contributes at most $L=o(X/\log X)$ and can be discarded.
Group the ordered primes of this block into disjoint consecutive groups
of $s$ primes. At most $L/(4s\log X)$ groups have span exceeding
$4s\log X$, because the disjoint spans sum to at most $L$.
Consequently at least $L/(4s\log X)-1$ groups have span at most
$4s\log X$. The number of their normalized offset patterns is at most
$(\lfloor4s\log X\rfloor+1)^{s-1}$ (one pattern if $s=1$).
The ratio tends to infinity, so at least $r$ disjoint groups have the same
pattern. Their first elements give $p_0+a_i$, and the common pattern gives
$b_j$. All $rs$ primes are distinct, and their total span is at most
$L=o(X)$, proving the assertion. No simultaneous-primality conjecture is
used: the tuples are selected from primes that already exist by counting.

**Upper construction.** Choose $r,s$ with $rs\ge u$ and
$r+s=\lceil2\sqrt u\rceil$. For example take
$r=\lfloor\sqrt u\rfloor$, $s=\lceil u/r\rceil$; checking
$u=r^2$, $r^2<u\le r(r+1)$ and $r(r+1)<u<(r+1)^2$ proves the claimed
sum. Obtain the grid above with its relative span arbitrarily small.
The Chinese remainder theorem gives an integer $z$ satisfying

$$
z\equiv a_i\pmod{p_{ij}}\quad\text{for every }i,j.
$$

For each $p_{ij}$, two consecutive multiples are
$R_i=z-a_i$ and $C_j=z+p_0+b_j$, since $C_j-R_i=p_{ij}$.
The preceding multiple is $z-p_0-2a_i-b_j\le z-p_0$, and the following
one is $z+2p_0+a_i+2b_j\ge z+2p_0$. Hence the only multiples in
$(z-p_0,z+2p_0)$ occur at the $r+s$ distinct row and column locations.
Take any $u$ grid primes including the maximum $P$; deleting primes
cannot increase this count. Set $K=\lfloor\alpha P\rfloor$.
For a sufficiently narrow grid, $\alpha P<3p_0$, so $K\le3p_0-1$.
For sufficiently large $p_0$, $K\ge2p_0+\max b_j$ and
$\max a_i<p_0$. The block

$$
[z-p_0+1,\ z-p_0+K]
$$

has exactly $K$ integers, lies in the larger open interval, and contains
all row and column locations. Add a sufficiently large multiple of the
product of the grid primes to $z$ to make the block positive.
Its union count for the selected primes is at most $r+s$; the lower bound
already proved forces equality. This completes the author argument.

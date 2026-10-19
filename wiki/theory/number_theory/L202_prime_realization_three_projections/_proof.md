---
name: theory/number_theory/L202_prime_realization_three_projections/_proof
title: A tail of a long prime progression realizes the whole pattern
desc: A sufficiently late segment of a long prime progression supplies every required prime difference, after which the exact three-layer lemma gives a comparison uniform below ratio four.
created: 2026-10-15T16:33:51Z
updated: 2026-10-15T16:33:51Z
---

***

**Realizing a fixed pattern.** Choose an integer $\Omega\ge1$ bounding
$|x|$ and $|y|$ on $S$. Then every $d=y-x$ satisfies $|d|\le2\Omega$.
Fix $3\le\alpha<4$ and choose an integer $M\ge2\Omega$ such that

$$
(4-\alpha)M\ge16\Omega+1.
$$

By Green and Tao's Theorem 1.1, there are integers $a\ge2$, $h\ge1$
such that $a+jh$ is prime for every $0\le j\le M+2\Omega$. Put
$q=a+Mh$. For every cell of $S$,

$$
q+h(y-x)=a+(M+y-x)h
$$

is one of these primes. The indices lie between $0$ and $M+2\Omega$,
and distinct cells have distinct indices by the injectivity of $y-x$.
On the dilated cell set $hS$, take $\omega=h\Omega$. We have

$$
(4-\alpha)q\ge (4-\alpha)Mh
\ge(16\Omega+1)h\ge16\omega+1.
$$

Thus L198 applies to $hS$ and $q$. Multiplication by the nonzero integer
$h$ preserves the cardinalities of all three projections. L198 therefore
gives precisely the required count in a block of
$\lfloor\alpha P\rfloor$ consecutive positive integers, where $P$ is
the largest chosen prime. This proves the first assertion.

**The progression minimum.** Define $F'_3(u)$ exactly as in the claim,
using distinct positive common differences. The minimum exists because
the attainable cardinalities form a nonempty subset of the positive
integers.

For the lower bound, take any $u$ primes with largest member $P$ and any
block $J$ of $K=\lfloor\alpha P\rfloor$ consecutive integers. Since
$K\ge3P$, for every chosen prime $p$ there are three consecutive
multiples $m,m+p,m+2p$ in $J$. The set of counted integers therefore
contains progressions with $u$ distinct positive differences, so its size
is at least $F'_3(u)$.

For the upper bound, let $A\subset\mathbb Z$ attain $F'_3(u)$.
Select exactly $u$ of its distinct positive differences $d_i$, and choose
$a_i,a_i+d_i,a_i+2d_i\in A$ for each. The cells
$S=\{(a_i,a_i+d_i):1\le i\le u\}$ have injective differences.
Their three projections are subsets of $A$, so their cardinalities sum
to at most $3|A|$. The first assertion realizes this cell set as primes
and a block with that sum as its exact count. Consequently

$$
F'_3(u)\le G_\alpha(u)\le3F'_3(u).
$$

Finally any block of $\lfloor\alpha P\rfloor\ge3P$ integers contains a
subblock of $3P$ integers. Its count is therefore at least $G_3(u)$.
Combining this with $F'_3(u)\le G_3(u)$ gives
$G_3(u)\le G_\alpha(u)\le3G_3(u)$. No limit in $u$ or uniform bound on
the sizes of the realizing primes is needed.

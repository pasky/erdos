---
name: research/erdos_25/binary_colored_private_witnesses
desc: A locally two-colored system with dense moduli and private profinite witnesses, yet natural survivor density one half.
tags: [endpoints, obstructions, local-colors, profinite-witnesses]
sources: []
created: 2026-09-22T10:37:29Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/binary_colored_private_witnesses

***

## Statement and scope

There is an explicitly specified singleton congruence system with the
following properties:

- Its distinct moduli have natural density $1/4$.
- Every residue is idempotent: $a_q^2\equiv a_q\pmod q$. Thus at
  each prime-power coordinate the residue is either $0$ or $1$.
- Every full cylinder has a private **profinite** witness, belonging
  to no other cylinder, even in the entire infinite system.
- The full Haar union has measure $1/2$, and the actual delayed
  union, with activation $n\ge q$, has natural density $1/2$.

This is an obstruction to replacing comparable positive integer
witnesses by profinite witnesses, even with only two local colors.
It is **not** a counterexample to Problem 25: both the delayed union
and its complement have natural, hence logarithmic, density $1/2$.
In particular, profinite privacy and positive survivor measure do not
force the moduli to have logarithmic density zero in this restricted
color setting either.

## A prime partition with sufficiently many groups

For $j\ge1$, let $w(j)$ be its binary gamma code. If the binary
expansion of $j$ has length $\ell$, prepend $\ell-1$ zeroes.
The code length is
$$
 L(j)=2\lfloor\log_2j\rfloor+1.
$$
These words are prefix-free. Indeed the initial zero run determines
$\ell$, and then exactly $\ell$ further bits determine $j$.

Let $p_h$ denote the $h$-th odd prime. Put $p_h$ in group
$\mathcal P_j$ if the successive binary digits of $h$, read
from the least significant digit onward, begin with $w(j)$.
This partitions the positive indices: every positive integer has a
first nonzero binary digit, so gamma parsing always terminates,
using zero digits beyond its usual finite expansion if needed.
The index set of group $j$ is one residue class modulo
$$
 M_j=2^{L(j)},\qquad j^2/2<M_j\le2j^2.
$$

We need the following uniform lower bound. Put $t=\log\log X$.
For sufficiently large $X$ and $1\le j\le C\log(t+2)$, with
any fixed $C$,
$$
 \mu_j(X):=\sum_{\substack{p\le\sqrt X\\p\in\mathcal P_j}}\frac1p
 \gg_C \frac{t}{j^2}.
 \tag{1}
$$
Here and below all prime groups contain only odd primes.

To check (1), the elementary Chebyshev bound gives
$p_h\ll h\log(2h)$. Thus all indices
$h\le H=c\sqrt X/\log X$, with a sufficiently small absolute
$c>0$, give primes at most $\sqrt X$. Each dyadic index interval
$[2^u,2^{u+1})$, for $2^u\ge4M_j$, contains at least
$2^{u-1}/M_j$ indices from the required residue class. Its
reciprocal-prime mass is consequently $\gg1/(M_j(u+1))$.
Summing these intervals up to $H$ gives
$$
 \mu_j(X)\gg \frac1{M_j}
       \bigl(\log\log H-\log\log(8M_j)-O(1)\bigr).
$$
For the indicated range of $j$, the bracket is at least
$t/2$ for large $X$. This proves (1); in particular every
group has a divergent prime reciprocal sum.

## Almost every odd modulus is eligible

Let $D$ consist of odd integers $q>1$ such that, with
$k=\Omega(q)$, the integer $q$ has a prime factor in every group
$\mathcal P_j$ for $1\le j\le L(k)$. Then
$$
 d(D)=\frac12.
 \tag{2}
$$

For a proof sample $n$ uniformly from $[1,X]$, and let $Z_j(n)$
count its prime factors from $\mathcal P_j$ at most $\sqrt X$.
If $s_j$ is the number of those primes, exact floor counts give
$$
 \mathbb EZ_j\ge\mu_j-s_j/X,\qquad
 \mathbb EZ_j^2\le\mu_j+\mu_j^2.
$$
Therefore
$$
 \mathbb E(Z_j-\mu_j)^2\le\mu_j+2\mu_js_j/X,\qquad
 \Pr(Z_j=0)\ll1/\mu_j.
 \tag{3}
$$
Also
$$
 \mathbb E\Omega(n)
 \le\sum_{p^a\le X}p^{-a}\le\log\log X+O(1),
$$
by the elementary Euler-product upper bound. Thus
$\Pr(\Omega(n)>t^2)=O(1/t)$. On the complementary event,
$L(\Omega(n))\le4\log_2t+1$. Taking
$J_X=\lceil5\log_2(t+2)\rceil$, (1), (3), and a union bound give
$$
 \Pr(\exists j\le J_X:Z_j=0)
 \ll\frac1t\sum_{j\le J_X}j^2
 \ll\frac{(\log(t+2))^3}{t}=o(1).
$$
Apart from $o(X)$ exceptions and the integer $1$, all odd integers
at most $X$ are therefore eligible. This proves (2).

## Idempotent residues and private witnesses

Initially use the odd moduli $q\in D$. For $k=\Omega(q)$, define
$b_{k,j}$ to be digit $j$ of $w(k)$ if $j\le L(k)$, and
zero otherwise. For every $p^e\parallel q$ with
$p\in\mathcal P_j$, prescribe
$$
 a_q\equiv b_{k,j}\pmod{p^e}.
 \tag{4}
$$
CRT gives one normalized residue modulo $q$, and it is idempotent.

Its private profinite witness $x^{(q)}$ has, at an odd prime $p$,
the coordinate
$$
 x^{(q)}_p=
 \begin{cases}
 b_{k,j}+p^e,&p^e\parallel q,\ p\in\mathcal P_j,\\
 2,&p\nmid q.
 \end{cases}
 \tag{5}
$$
Choose its 2-adic coordinate to be zero. It belongs to its own
cylinder. If it also belongs to the cylinder of $r\in D$, no
prime outside $q$ can divide $r$, since $2$ is neither $0$
nor $1$ modulo an odd prime. At a prime dividing $q$, a match
requires the same bit and an exponent no greater than $v_p(q)$:
the difference from that bit in (5) has valuation exactly $e$.
Consequently $r\mid q$.

If $r\ne q$, then $\Omega(r)<\Omega(q)$. The distinct prefix-free
codewords differ at some position $j$ not exceeding either length.
Eligibility of $r$ supplies a prime of $\mathcal P_j$ dividing
$r$, hence also $q$. The prescribed bits there differ, a
contradiction. Thus $x^{(q)}$ belongs to no other cylinder.

## A positive survivor measure and exact activation

Now replace the modulus $q\in D$ by $2q$, prescribing simultaneously
the old odd-prime residues (4) and residue zero modulo $2$.
This is a CRT extension, **not** multiplication of the old residue by
two. Idempotency and all private witnesses (5) are preserved.
The new moduli are distinct and, by (2), have natural density $1/4$.
They admit a strictly increasing enumeration.

All full and delayed classes lie in the even fiber. Since
$w(1)=1$, for every prime $p\in\mathcal P_1$ the family includes
the cylinder
$$
 [0]_2\cap[1]_p
$$
at the single modulus $2p$. The reciprocal sum of these primes
diverges. Their finite Haar unions therefore have measures
$$
 \frac12\left(1-\prod_{p\in F}(1-1/p)\right)\longrightarrow\frac12.
$$
Their delayed versions, activated exactly at $n\ge2p$, differ from
each fixed finite periodic union on only finitely many integers.
Hence the full delayed union has lower natural density at least
$1/2$. Its containment in the even integers gives upper natural
density at most $1/2$. Both its natural density and the full Haar
union measure are exactly $1/2$.

Every finite first-kill cell is nonempty, since it contains its private
profinite witness; being clopen, it has positive Haar measure. This
still supplies no positive integer private witnesses of size
$[q,2q)$, or any other uniformly bounded multiple of $q$.
That quantitative arithmetic requirement remains unresolved in the
general endpoint problem.

In fact, any globally private **integer** witness set for this
particular family is naturally null, even without a size restriction.
Outside the finitely many witnesses assigned to a fixed group-1 prime
prefix, it lies in the even fiber and avoids that entire prefix.
The densities of these periodic remainders tend to zero. Thus the
example cannot itself furnish a positive-density private integer family.

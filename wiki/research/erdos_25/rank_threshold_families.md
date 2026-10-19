---
name: research/erdos_25/rank_threshold_families
desc: Uniform small-footprint bounds for complete rank-threshold families of coprime blocks.
tags: [sieve, partial-results, counterexamples]
sources: []
created: 2026-09-22T01:50:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/rank_threshold_families

***

## Theorem: proved

Let $m_1,\ldots,m_s\ge2$ be pairwise coprime integers and fix one
residue $b_i\pmod{m_i}$ for each. Fix an integer $r\ge1$. For every $r$-element subset
$S\subseteq\{1,\ldots,s\}$, install the CRT-induced class modulo
$q_S=\prod_{i\in S}m_i$, activated at $n\ge q_S$. Let $B$ be this
delayed union and $\beta$ its full periodic density. Then
$$
 \sup_{X\ge1}\frac{|B\cap[1,X]|}{X}
 \ll\frac1{\sqrt{\log(e/\beta)}}.
 \tag{1}
$$
The implied constant is absolute, and the same bound holds for
$H_B(X)/H_{\lfloor X\rfloor}$. If $r>s$, both unions are empty.

All product moduli are distinct, since the blocks are pairwise coprime
and greater than one. Thus these are genuine singleton systems. The
blocks need not be prime powers. This theorem excludes another
small-full-footprint construction, but does not control arbitrary
subfamilies of products or incoherent residues.

## Three elementary counting bounds

Put $p_i=1/m_i$, $\lambda=\sum_i p_i$, and let
$Y=\sum_i Y_i$, with independent $Y_i\sim\operatorname{Bernoulli}(p_i)$.
CRT gives $\beta=\Pr(Y\ge r)$. Writing the supremum on the left of
(1) as $\rho$, we have
$$
 \rho\le2^r\beta,\qquad
 \rho\le\lambda/r,\qquad
 \rho\le\frac{\lambda+3}{(r-1-\lambda)^2}\quad(r>\lambda+1).
 \tag{2}
$$

For the first bound, partition the deleted integers below $N$ among
their first covering product classes, and write their normalized counts
as $c_S$. For a block face $J$, activation gives
$$
 \sum_{S\supseteq J}c_S\le\frac1{\prod_{j\in J}m_j}.
$$
On Haar space use $Z=\sum_S q_Sc_S\mathbf1_{C_S}$. Expand intersections
using
$$
 \gcd(q_S,q_T)
 =\sum_{J\subseteq S\cap T}\prod_{j\in J}(m_j-1).
$$
The same calculation as in
[bounded prime rank](bounded_prime_rank.md#a-finite-counting-and-harmonic-estimate)
now yields
$$
 \mathbb EZ^2
 \le\sum_S c_S\prod_{i\in S}(2-1/m_i)
 \le2^r\sum_Sc_S.
$$
Since $Z$ is supported on the full union of measure $\beta$,
Cauchy--Schwarz proves the first assertion of (2).

Every actual deletion has at least $r$ active block hits. Block $i$
has at most $N/m_i$ active hits up to $N$. Summing proves the second.

For the third, average over $1\le n\le N$, and put
$$
 Z_N(n)=\sum_{m_i\le\sqrt N}\mathbf1_{n\equiv b_i\pmod{m_i}},
 \qquad \lambda_N=\sum_{m_i\le\sqrt N}1/m_i.
$$
An active certificate has at most one block larger than $\sqrt N$,
so deletion implies $Z_N(n)\ge r-1$. If $k$ blocks occur in this
sum, their single and pair CRT counts have normalized error at most
$1/N$. Thus
$$
 \mathbb E(Z_N-\lambda_N)^2
 \le\lambda_N+\frac{k^2}{N}+\frac{2\lambda_Nk}{N}
 \le\lambda_N+3,
$$
using $k\le\sqrt N$ and $\lambda_N\le k/2$. Chebyshev's inequality,
with $\lambda_N\le\lambda$, proves (2).

## An elementary independent-tail lower bound

When $\lambda\ge10^4$ and $r\le1.1\lambda$,
$$
 \beta\ge\frac23\exp\left[-150\left(1+
                  \frac{(r-\lambda)_+^2}{\lambda}\right)\right].
 \tag{3}
$$
To prove this, set $a=(r-\lambda)_+$ and
$d=4(a+2\sqrt\lambda)/\lambda\le0.48$. Tilt each Bernoulli odds by
$1+d$; the new probabilities are
$$
 p_i'=\frac{(1+d)p_i}{1+dp_i}.
$$
Their mean $M$ satisfies
$$
 M-\lambda=\sum_i\frac{dp_i(1-p_i)}{1+dp_i}
 \ge\frac{d\lambda}{2+d},\qquad
 M\le(1+d)\lambda\le1.5\lambda.
$$
It follows that $M-r\ge3\sqrt\lambda$. The tilted variance is at
most $1.5\lambda$, so Chebyshev gives tilted probability at least
$2/3$ to $r\le Y\le M+3\sqrt\lambda$. On this event, using
$\log(1+x)\ge x-x^2/2$,
$$
\begin{aligned}
 \log\frac{d\Pr'}{d\Pr}
 &=Y\log(1+d)-\sum_i\log(1+dp_i)\\
 &\le d(Y-\lambda)+\frac{d^2}2\sum_i p_i^2\\
 &\le\frac54d^2\lambda+3d\sqrt\lambda
 \le150(1+a^2/\lambda).
\end{aligned}
$$
For the last inequality, put $u=a/\sqrt\lambda$. Its left side is at
most $20u^2+92u+104\le150(1+u^2)$. Changing measure proves (3).

## Combining the bounds

Let $L=\log(1/\beta)$, with bounded $L$ absorbed in the constant.
If $r\le L/(2\log2)$, (2) gives $\rho\le e^{-L/2}$. Otherwise,
if $\lambda\le\sqrt L$, it gives $\rho\ll L^{-1/2}$. If
$\lambda>\sqrt L$ and $r-1-\lambda\ge\lambda/20$, its last bound
gives $\rho\ll1/\lambda\ll L^{-1/2}$.

In the remaining case, $r\le1.1\lambda$ for sufficiently large $L$,
and (3) implies $(r-\lambda)_+^2/\lambda\gg L$. In particular
$r>\lambda+1$, and the last bound in (2) is $O(1/L)$. This proves
(1). Partial summation of the uniform counting bound proves its harmonic
version.

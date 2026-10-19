---
name: research/erdos_25/one_unbounded_prime_power
desc: Natural density for bounded complementary prime rank, and for arbitrary singleton residues with at most two distinct prime factors per modulus.
tags: [density, prime-rank, partial-results]
sources: []
created: 2026-09-22T09:25:34Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/one_unbounded_prime_power

***

## Theorem: proved

Suppose that for some fixed integer $r\ge0$, every modulus $q>1$
has a distinguished prime $p=p(q)$ for which
$$
 q=p^e m,\qquad (p,m)=1,\qquad \Omega(m)\le r.
 \tag{1}
$$
Then arbitrary residue classes at these moduli, activated at $n\ge q$,
have finite-periodic approximation in upper natural density. In
particular the survivor set has natural density equal to its finite-prefix
candidate, and hence logarithmic density. Multiple residues at a modulus
are allowed in this theorem; duplicate congruence pairs are discarded.

**Corollary.** For the singleton problem, arbitrary residues and
$\omega(q)\le2$ imply natural density. Exponents need not be bounded,
and the residues need not be coherent.

This strengthens [bounded prime rank](bounded_prime_rank.md). The later
[squarefull-kernel truncation](squarefull_kernel_truncation.md) proves
natural density for all bounded-$\omega$ singleton systems and, more
generally, bounded exponent-one prime rank. The finite tree inequalities
here remain useful stronger finite bounds on their stated subclass.
Neither theorem settles the unrestricted problem.

## Finite estimate with one fixed prime

Fix a prime $p$. Consider a finite family

$$
 C_i=[a_i]_{q_i},\qquad q_i=p^{e_i}m_i,\quad
 (p,m_i)=1,\quad \Omega(m_i)\le r,
$$

allowing $e_i=0$. Normalize $0\le a_i<q_i$, put
$B_i=C_i\cap[q_i,\infty)$, and write
$\beta=\mu(\bigcup_i C_i)$. Partition the actual delayed union into
disjoint sets $E_i\subseteq B_i$. At a counting cutoff $X$, set

$$
 c_i=X^{-1}|E_i\cap[1,X]|,\qquad \alpha=\sum_i c_i.
$$

Every divisor face obeys

$$
 \sum_{\substack{i:d\mid q_i\\a_i\equiv b\pmod d}}c_i\le1/d.
 \tag{2}
$$

Indeed all its counted points satisfy $n\ge q_i\ge d$ and
$n\equiv b\pmod d$; the delayed progression contains at most $X/d$
integers up to $X$.

On Haar space let $Z=\sum_iq_ic_i\mathbf1_{C_i}$. Then
$\mathbb EZ=\alpha$. Compatible $p$-adic balls are nested. In the
second moment orient each compatible pair by $e_i\le e_j$, paying
a factor of two, and expand
$\gcd(m_i,m_j)=\sum_{d\mid m_i,m_j}\varphi(d)$. Dropping other
compatibility restrictions only increases the resulting positive sum:

$$
\begin{aligned}
 \mathbb EZ^2
 &\le2\sum_i c_i p^{e_i}\sum_{d\mid m_i}\varphi(d)
  \sum_{\substack{j:d\mid m_j,\ e_j\ge e_i\\
              a_j\equiv a_i\pmod{p^{e_i}d}}}c_j\\
 &\le2\sum_i c_i\sum_{d\mid m_i}\frac{\varphi(d)}d
 \le2^{r+1}\alpha.
\end{aligned}
\tag{3}
$$

The inner capacity in (2) is at most $1/(p^{e_i}d)$. The last
inequality uses $\sum_{d\mid m}\varphi(d)/d\le2^{\Omega(m)}$.
Since $Z$ is supported on a set of Haar measure $\beta$,
Cauchy--Schwarz proves

$$
 |B\cap[1,X]|\le2^{r+1}\beta X.
 \tag{4}
$$

The same proof gives
$H_B(X)\le2^{r+1}\beta H_{\lfloor X\rfloor}$: take
$c_i=H_{E_i}(X)/H_{\lfloor X\rfloor}$. Capacity (2) still holds,
because the harmonic sum of a delayed class modulo $d$ is at most
$H_{\lfloor X/d\rfloor}/d$.

## Finite approximation for a fixed distinguished prime

Induct on $r$. When $r=0$, the cylinders are $p$-adic balls.
Retain the maximal balls under inclusion. They exist because the set
of eligible ancestor exponents has a minimum, and they are disjoint.
A discarded descendant contributes no new delayed points: its modulus
is at least its retained ancestor's modulus. The retained disjoint
balls have summable measures, and (4), or the direct progression bound,
makes their remote tails negligible in upper natural density.

For the induction step write $U$ for the full union, and let $U_N$
be the union of classes whose moduli have no prime factor at most $N$
other than possibly $p$. These sets decrease to $E$. The conditional
prime-coordinate zero--one law implies that $E$, modulo a Haar-null
set, depends only on the $p$-coordinate. One way to check this is to
fix that coordinate: the section of $E$ belongs to the tail
sigma-field of all other independent prime coordinates, and so has
measure zero or one. Fubini then identifies its indicator almost
everywhere with a measurable function of the $p$-coordinate.

Given $\varepsilon>0$, choose a union $V$ of residue classes modulo
$p^F$, with $F\ge1$, such that
$\mu(V\triangle E)<\varepsilon$. Then choose $N\ge p$ such that
$\mu(U_N\setminus E)<\varepsilon$.

Call a class retained if its $p$-exponent is less than $F$, or if
its modulus has a prime divisor $\ell\le N$, $\ell\ne p$.
The first family has bounded $\Omega(q)$, and is covered by the
established [bounded-$\Omega$ theorem](bounded_prime_rank.md).
Partition the second family according to a chosen $\ell$ and its
residue $b\pmod\ell$. The substitution $n=b+\ell t$,
$0\le b<\ell$, identifies delayed activation exactly with
$t\ge q/\ell$. The complementary rank drops by one, so induction
applies. There are finitely many groups; consequently the whole
retained family has finite-periodic natural approximation.

Every remaining class has $p$-exponent at least $F$, hence lies
wholly inside or outside $V$. Those outside $V$ have full union
measure at most $\mu(U_N\setminus V)<2\varepsilon$. Apply (4) to the
finitely many classes active at any cutoff: their delayed union has
upper natural density at most $2^{r+2}\varepsilon$.

Since $E\subseteq U$, $\mu(V\setminus U)<\varepsilon$. By monotone
convergence choose a finite subfamily $F_0$ with
$\mu(V\setminus U_{F_0})<2\varepsilon$. Its delayed union differs
from its periodic union on only finitely many integers. Thus
$V\cap\mathbb N\setminus B_{F_0}$ has natural density less than
$2\varepsilon$. Choose another finite subfamily $F_1$ approximating
the retained family to upper density error less than $\varepsilon$.
The union omitted by $F_0\cup F_1$ has upper density at most
$(3+2^{r+2})\varepsilon$. This proves the fixed-$p$ assertion.

## A finite estimate when the distinguished prime varies

Assign a representation (1) to each class. In $\mathbb EZ^2$, pairs
with equal distinguished prime contribute at most
$2^{r+1}\alpha$, by (3) summed over the distinguished primes.

For a pair with $p_i\ne p_j$, the exponent of $p_i$ in $q_j$ is
at most $r$. Therefore

$$
 \gcd(q_i,q_j)\mid\widetilde q_i
 :=p_i^{\min(e_i,r)}m_i,\qquad \Omega(\widetilde q_i)\le2r.
$$

Expanding the gcd and applying (2), the contribution of these ordered
pairs is at most

$$
 \sum_i c_i\sum_{d\mid\widetilde q_i}\varphi(d)
       \sum_{\substack{j:d\mid q_j\\a_j\equiv a_i\pmod d}}c_j
 \le\sum_i c_i\sum_{d\mid\widetilde q_i}\frac{\varphi(d)}d
 \le2^{2r}\alpha.
$$

Consequently, with $C_r=2^{r+1}+2^{2r}$,

$$
 |B\cap[1,X]|\le C_r\beta X,\qquad
 H_B(X)\le C_r\beta H_{\lfloor X\rfloor}.
 \tag{5}
$$

## Proof of the theorem with varying distinguished prime

Induct on $r$. If $\mu(U)=1$, fixed finite delayed subfamilies
already force natural density one; their omitted upper densities are
at most their survivor densities, tending to zero.

Otherwise let $U_N$ be the full union of classes whose prime factors
all exceed $N$. Its decreasing intersection is a prime-coordinate
tail event of measure at most $\mu(U)<1$. The zero--one law gives
$\mu(U_N)\to0$. Estimate (5) uniformly bounds the corresponding
delayed union by $C_r\mu(U_N)X$.

For every other class choose a prime divisor $\ell\le N$. If
$\ell=p(q)$, it belongs to one of finitely many fixed-prime
families already treated. Otherwise partition further by its residue
modulo $\ell$, and divide out $\ell$. The same exact affine
substitution drops the complementary rank by one while keeping the
distinguished prime. Induction applies. When $r=0$, this second
case is empty. Combining finitely many approximating subfamilies and
then letting $N\to\infty$ proves finite-periodic approximation.

The limit equals the increasing limit of the finite full union
measures, since each finite delayed union has that periodic density.
Complements give the stated survivor density. Partial summation gives
logarithmic density with the same value.

## Deduction for at most two distinct prime factors

Prime powers and numbers $p^a\ell^b$ with $\min(a,b)=1$ satisfy
(1) with $r=1$. The remaining modulus family is reciprocal-summable:

$$
 \sum_{p<\ell}\sum_{a,b\ge2}\frac1{p^a\ell^b}
 =\sum_{p<\ell}\frac1{p(p-1)\ell(\ell-1)}<\infty.
$$

With one residue per modulus, its delayed tail is uniformly bounded
in counting by $X$ times the reciprocal tail. It therefore has
finite-periodic natural approximation, as does its union with the
family covered by (1). This proves the corollary. The singleton
restriction is needed for this last summable-exception step.

Two uncontrolled prime-power exponents together with a third variable
prime are not covered by this particular argument, but are covered by
the later [squarefull-kernel theorem](squarefull_kernel_truncation.md).
The existing
[three-prime divisor-face obstruction](product_capacity_obstruction.md)
also rules out extending (5) to that class solely by the individual
capacities (2). The new natural-density theorem uses additional
arithmetic activation estimates, not only those capacities.

---
name: research/erdos_25/bounded_prime_rank
desc: Natural-density criteria from bounded prime rank and bounded pairwise common rank.
tags: [density, partial-results, sieve]
sources: []
created: 2026-09-21T23:55:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/bounded_prime_rank

***

The later [one-unbounded-prime-power theorem](one_unbounded_prime_power.md)
allows arbitrary exponents at one distinguished prime per modulus and
bounded complementary $\Omega$. In particular it proves natural density
for arbitrary singleton residues with $\omega(q)\le2$, without coherence.
The subsequent [squarefull-kernel theorem](squarefull_kernel_truncation.md)
extends this to all bounded-$\omega$ singleton systems, and more generally
to bounded numbers of prime factors occurring to exponent exactly one.

## Theorem: proved

Write $\Omega(q)$ for the number of prime factors of $q$, counted with
multiplicity. If $\sup_i\Omega(n_i)<\infty$, the delayed survivor set in
Problem 25 has **natural density**, equal to its finite-periodic candidate
$\delta$. More precisely, the delayed excluded union has finite-periodic
approximation in upper natural density.

The proof actually permits several residues at each modulus. It therefore
does not address the distinctive difficulty of unbounded-rank singleton
families. Duplicate congruence pairs can be discarded, so each modulus
has only finitely many distinct normalized residues. No theorem from an
external source is required below.

## A finite counting and harmonic estimate

Let $C_i=[a_i]_{q_i}$ be finitely many full congruence classes, with
$0\le a_i<q_i$, and let
$$
 B_i=C_i\cap[q_i,\infty),\qquad B=\bigcup_iB_i,
 \qquad \beta=\mu\left(\bigcup_iC_i\right),
$$
where $\mu$ is Haar probability on $\widehat{\mathbb Z}$, equivalently
periodic density for this finite family. Define
$$
 \kappa(q)=\sum_{d\mid q}\frac{\varphi(d)}d
 =\prod_{p^e\Vert q}\left(1+e(1-1/p)\right).
$$
Then, for every $X\ge1$,
$$
 |B\cap[1,X]|\le \beta X\max_i\kappa(q_i),
 \qquad
 H_B(X)\le \beta H_{\lfloor X\rfloor}\max_i\kappa(q_i).
 \tag{1}
$$
In particular $\Omega(q_i)\le r$ gives the constant $2^r$, since
$\kappa(q)\le\tau(q)\le2^{\Omega(q)}$.

**Proof.** Partition the actually deleted integers among their first
covering classes, obtaining disjoint sets $E_i\subseteq B_i$. In the
counting version put $c_i=|E_i\cap[1,X]|/X$ and
$\alpha=\sum_i c_i$. For every divisor-face $[b]_d$ put
$$
 S_{d,b}=\sum_{\substack{i:d\mid q_i\\a_i\equiv b\pmod d}}c_i.
$$
All points counted by this sum lie in the delayed class
$\{n\ge d:n\equiv b\pmod d\}$: activation gives $n\ge q_i\ge d$.
Consequently $S_{d,b}\le1/d$.

On Haar space set $Z=\sum_i q_i c_i\mathbf1_{C_i}$. Then
$\mathbb EZ=\alpha$ and $Z$ vanishes off a set of measure $\beta$.
Compatible pairs of classes have intersection measure
$1/\operatorname{lcm}(q_i,q_j)$; incompatible pairs have empty
intersection. Using $\gcd(q_i,q_j)=\sum_{d\mid q_i,q_j}\varphi(d)$,
$$
\begin{aligned}
 \mathbb EZ^2
 &=\sum_{\substack{i,j:\ a_i\equiv a_j\pmod{\gcd(q_i,q_j)}}}
       c_ic_j\gcd(q_i,q_j)\\
 &\le\sum_d\varphi(d)\sum_{b\bmod d}S_{d,b}^2\\
 &\le\sum_d\frac{\varphi(d)}d\sum_{b\bmod d}S_{d,b}
 =\sum_i\kappa(q_i)c_i.
 \tag{2}
\end{aligned}
$$
The first inequality can be strict: an incompatible pair may agree
modulo a proper divisor of its gcd and hence contribute to the right side.
Cauchy--Schwarz now gives
$\alpha^2\le\beta\mathbb EZ^2\le\beta(\max_i\kappa(q_i))\alpha$,
proving the counting statement.

For the harmonic statement instead take
$c_i=H_{E_i}(X)/H_{\lfloor X\rfloor}$. The same argument applies because
$$
 \sum_{\substack{n\le X\,,\ n\ge d\\n\equiv b\pmod d}}\frac1n
 \le\frac1d H_{\lfloor X/d\rfloor}
 \le\frac1d H_{\lfloor X\rfloor}.
$$
Thus (2) and Cauchy--Schwarz remain valid. $\square$

The more informative form of (2) is
$\alpha^2\le\beta\sum_i\kappa(q_i)c_i$; replacing its weighted factor
by a universal constant is not justified.

## Proof of the theorem

We prove by induction on $r$ that every family of congruence pairs with
$\Omega(q)\le r$ has finite-periodic approximation in upper natural
density. Multiple distinct residues per modulus are allowed in the
inductive statement. The case $r=0$ has only modulus $1$ and is immediate.

Let $U$ be the union of the full cylinders and $\beta=\mu(U)$. If
$\beta=1$, finite truncations already force the delayed excluded union
$B$ to have natural density $1$. If $F$ is a finite subfamily, then
$d(B\setminus B_F)=1-d(B_F)$, which tends to zero as finite truncations
exhaust the family. This proves the desired approximation in this case.

Suppose $\beta<1$. For $N\ge2$, let $U_N$ be the union of those full
classes whose moduli have no prime factor at most $N$, and let $B_N$
be their actual delayed union. On the product of independent prime-adic
Haar coordinates, $U_N$ depends only on primes greater than $N$.
The sets $U_N$ decrease, and their intersection is a prime-coordinate
tail event. Kolmogorov's zero--one law and
$\mu(\bigcap_N U_N)\le\beta<1$ give
$$
 \mu_N:=\mu(U_N)\longrightarrow0.
 \tag{3}
$$
Here the zero--one law follows because the tail event is independent of
every finite set of prime coordinates, hence of the whole product
sigma-field and therefore of itself.
For each fixed $X$, only finitely many of these classes can be active:
their moduli are at most $X$, and there are finitely many residues per
modulus. Applying (1) to those classes gives the uniform bound
$$
 |B_N\cap[1,X]|\le2^r\mu_N X.
 \tag{4}
$$

It remains to handle the nonrough moduli, for a fixed $N$. Partition
their classes according to a chosen prime divisor $p\le N$ and the
residue $b=a_i\bmod p$, where $0\le b<p$. There are finitely many such
groups. In one group write
$$
 q_i=pm_i,\qquad a_i=b+pc_i.
$$
The substitution $n=b+pt$ identifies its delayed exclusions exactly with
$$
 t\ge m_i,\qquad t\equiv c_i\pmod{m_i}.
 \tag{5}
$$
Indeed $b+pt\ge pm_i$ is equivalent to $t\ge m_i$, because
$0\le b<p$. Moreover $\Omega(m_i)\le r-1$. By induction the quotient
family has finite-periodic natural approximation. Its image under
$t\mapsto b+pt$ has the same property, with densities divided by $p$.
Finite unions of these groups retain that property: the omitted union
is bounded by the sum of the omitted upper densities.

Given $\varepsilon>0$, first choose $N$ so that $2^r\mu_N<\varepsilon/2$.
Then choose finitely many classes in each nonrough group so that the sum
of their omitted upper densities is less than $\varepsilon/2$. The
union $F$ of these finite selections satisfies
$$
 \overline d(B\setminus B_F)<\varepsilon
$$
by (4). An original finite initial segment can include $F$.
Thus $B$ has natural density $\beta$, and its complement has natural
density $1-\beta=\delta$. Natural density implies logarithmic density
by partial summation. $\square$

## Coherent bounded distinct-prime rank

A further proved case allows unbounded exponents. Suppose the residues
come from one $\alpha\in\widehat{\mathbb Z}$ and
$\omega(q_i)\le r$, where $\omega$ counts distinct prime factors. Then
the same natural-density conclusion holds.

For an integer $E\ge2$, a modulus divisible by $p^E$ has its full class
contained in $\alpha\pmod{p^E}$. Its delayed hits have $n\ge q_i\ge p^E$.
The union over moduli with any exponent at least $E$ therefore has,
uniformly in $X$, at most
$$
 X\sum_p p^{-E}
$$
hits below $X$. This tends to zero after division by $X$ as $E\to\infty$.
All remaining moduli have $\Omega(q_i)\le r(E-1)$ and are covered by
the theorem. Finite-periodic approximation follows by truncating $E$
and then using that theorem. Coherence is essential to this particular
high-power bound: without it, the projected residues modulo $p^E$ need
not be the same.

## Bounded pairwise common rank

Two further natural-density cases follow by a summable-tail reduction.
For any fixed $k\ge0$:

- Arbitrary residues are allowed if
  $\Omega((q_i,q_j))\le k$ whenever $i\ne j$.
- Coherent residues are allowed if
  $\omega((q_i,q_j))\le k$ whenever $i\ne j$.

For the first assertion, retain the moduli with $\Omega(q)\le k+1$;
the established bounded-$\Omega$ theorem applies. For each remaining
$q$, let $d$ be the product of its $k+1$ smallest prime factors,
counting multiplicity, and let $p$ be the largest prime factor of $d$.
No two moduli can have the same $d$, since then their gcd would have
at least $k+1$ prime factors counted with multiplicity. Also $q\ge dp$.
Consequently
$$
 \sum_{\Omega(q)\ge k+2}\frac1q
 \le\sum_{p_1\le\cdots\le p_{k+1}}
        \frac1{p_1\cdots p_k p_{k+1}^2}
 \le\sum_{m\ge2}\frac{H_m^k}{m^2}<\infty.
$$
The removed family is therefore covered by the summable case.

For the second assertion use the $k+1$ smallest **distinct** prime
factors of every modulus with $\omega(q)\ge k+2$. The same injection
and convergent majorant apply. The retained coherent family has bounded
$\omega$ and is covered by the preceding theorem. In both cases the two
subfamilies have finite-periodic natural approximation, so their union
does too.

This reduction does not extend the theorem to arbitrary residues with
bounded $\omega(q)$. Indeed the
[fixed-rank product obstruction](product_capacity_obstruction.md) shows
that even at $\omega(q)\le3$, distinctness and all divisor-face capacities
alone cannot supply the needed uniform bound. Its abstract weights have
not been realized as first-kill masses.

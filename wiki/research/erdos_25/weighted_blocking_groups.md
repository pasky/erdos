---
name: research/erdos_25/weighted_blocking_groups
desc: Weighted blocking-prime groups give uniform coherent trace bounds and control the spanning-tree divisor-cover obstruction.
tags: [coherent-residues, sieve, partial-results, fractional-packing]
sources: []
created: 2026-09-22T09:44:24Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/weighted_blocking_groups

***

The following finite estimate is proved. It extends the
[transversal-prime-group bound](transversal_prime_groups.md) to overlapping
groups with fractional weights. In particular, it controls the coherent
arithmetic traces of the spanning-tree family used in the
[positive divisor-cover obstruction](divisor_cover_obstruction.md).
It does not prove the unrestricted coherent small-footprint bound.

## A weighted blocking-group estimate

Let $P_1,\ldots,P_t$ be finite nonempty sets of primes. Suppose that
every modulus $q$ in a finite family $D$ has a prime factor in every
$P_j$. Choose weights $w_j\ge0$ satisfying
$$
 \sum_{j:p\in P_j}w_j\le1\qquad\text{for every prime }p.
 \tag{1}
$$
Put
$$
 W=\sum_jw_j,\qquad
 u_j=\prod_{p\in P_j}(1-1/p),\qquad
 \mu=\sum_jw_ju_j.
$$
For any coherent center $\alpha\in\widehat{\mathbb Z}$, use the original
activation rule
$$
 B=\{n\ge1:\exists q\in D,\ q\le n,\ n\equiv\alpha\pmod q\}.
$$
There is an absolute constant $C$ such that, for every $X\ge2$,
$$
 \frac{|B\cap[1,X]|}{X}\le\min(1,C/\mu),\qquad
 \frac{H_B(X)}{H_{\lfloor X\rfloor}}\le\min(1,C/\mu).
 \tag{2}
$$
When $\mu=0$, interpret the right side as the trivial bound one.
The constants do not depend on the groups, weights, moduli, center, or
cutoff. The family $D$ need not contain all products meeting the groups.
Repeated prime factors in its moduli are also allowed.

### The sieve input already checked

We use exactly the interval comparison established in
[transversal prime groups](transversal_prime_groups.md#removing-the-bound-on-group-reciprocal-sums).
It follows from the upper and lower weights in Koukoulopoulos,
[*The Distribution of Prime Numbers*, Theorem 19.1](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf#page=206),
printed p. 195, with the dimension-one hypothesis on printed p. 187.
Those passages were checked for the earlier result.

Here is the form needed below. Let $N\ge2$ be an integer, $I=(N,2N]$,
and $\mathcal P$ any finite set of primes at most $z$. Give each prime
one forbidden residue. Write $F$ for their joint avoidance indicator
and $v=\prod_{p\in\mathcal P}(1-1/p)$. With sieve level $D_0=\sqrt N$,
$$
 |\mathbb E_I F-v|\le\varepsilon v+N^{-1/2},\qquad
 \varepsilon\ll s^{-s/2},\qquad
 s=\frac{\log D_0}{\log z},
 \tag{3}
$$
provided $s$ exceeds an absolute constant. The constants are independent
of the prime set and forbidden residues. Indeed the weights have absolute
value at most one and support on squarefree integers at most $D_0$.
Each corresponding CRT class has normalized counting error at most $1/N$,
so their total error is at most $D_0/N$. The Euler-product error is relative,
as displayed in (3).

### Haar variance with fractional weights

On any finite product of independent prime-coordinate spaces, suppose
$F_j$ is an avoidance indicator depending only on primes in $P_j$.
Set $M=\sum_jw_jF_j$ and $m=\mathbb E M$. Then (1) implies
$$
 \operatorname{Var}M
 \le\sum_jw_j\operatorname{Var}F_j\le m.
 \tag{4}
$$

For completeness, expand each centered function in its orthogonal
coordinate decomposition,
$$
 F_j-\mathbb EF_j
 =\sum_{\varnothing\ne S\subseteq P_j}f_{j,S}.
$$
Each component has mean zero in every coordinate of $S$, so components
indexed by different sets $S$ are orthogonal. For every nonempty $S$,
weighted Cauchy--Schwarz and (1) give
$$
 \left\|\sum_{j:S\subseteq P_j}w_jf_{j,S}\right\|_2^2
 \le
 \left(\sum_{j:S\subseteq P_j}w_j\right)
 \sum_{j:S\subseteq P_j}w_j\|f_{j,S}\|_2^2
 \le\sum_{j:S\subseteq P_j}w_j\|f_{j,S}\|_2^2.
$$
To bound the first factor, choose any prime in $S$ and apply (1).
Summing over $S$ proves the first inequality of (4); the second uses
$\operatorname{Var}F_j\le\mathbb EF_j$.

### Proof of the arithmetic estimate

It is enough to treat $\mu$ larger than a sufficiently large absolute
constant. Work on $I=(N,2N]$. If it contains no deleted point, there is
nothing to prove. Otherwise choose an active witness $q\le2N$.
Since $q$ meets every group, (1) implies
$$
 W\le\sum_{p\mid q}\sum_{j:p\in P_j}w_j\le\omega(q).
$$
Consequently
$$
 2N\ge q\ge2^W,\qquad W\ge\mu.
 \tag{5}
$$
In particular $N\ge2$ in the present range.

Set
$$
 z=(2N)^{2/\mu},\qquad
 F_j(n)=\mathbf1_{\{n\not\equiv\alpha\pmod p
                    \text{ for every }p\in P_j,\ p\le z\}},
 \qquad M(n)=\sum_jw_jF_j(n).
$$
Let $m=\mathbb E_{\rm Haar}M$. Removing the larger primes increases
each avoidance probability, so
$$
 \mu\le m\le W.
 \tag{6}
$$
Equation (5) also gives $z\ge4$. With $D_0=\sqrt N$,
$$
 s=\frac{\log D_0}{\log z}
   =\frac{\mu\log N}{4\log(2N)}\ge\mu/8.
$$
Thus (3) applies to each $F_j$ and to each $F_jF_k$: the latter is
avoidance of the union of the two truncated prime groups, with the same
residue at any shared prime. Coherence is used here.

Write $p_j=\mathbb E_{\rm Haar}F_j$ and
$p_{jk}=\mathbb E_{\rm Haar}F_jF_k$. Shared primes mean that
$p_{jk}$ need not equal $p_jp_k$. Summing (3) with the weights gives
$$
 |\mathbb E_I M-m|\le\varepsilon m+W N^{-1/2},
$$
and
$$
 |\mathbb E_I M^2-\mathbb E_{\rm Haar}M^2|
 \le\varepsilon\mathbb E_{\rm Haar}M^2+W^2N^{-1/2}.
$$
Combining these inequalities with (4) and (6) yields
$$
 \mathbb E_I(M-m)^2
 \le(1+\varepsilon)m+3\varepsilon m^2+3W^2N^{-1/2}.
 \tag{7}
$$

Suppose now that $n\in B\cap I$ is witnessed by $q\le n$. Every
group with $F_j(n)=1$ must be met by a prime divisor of $q$ greater
than $z$: a smaller prime divisor in that group would match $\alpha$
and make $F_j(n)=0$. By (1), each such larger prime can account for
groups of total weight at most one. Hence
$$
 M(n)\le\#\{p\mid q:p>z\}.
$$
If $M(n)\ge\mu/2$, this would force
$$
 q>z^{M(n)}\ge z^{\mu/2}=2N\ge n,
$$
contradicting activation. Therefore every deleted point lies in
$\{M<\mu/2\}$. Since $m\ge\mu$, Chebyshev's inequality and (7) show
$$
 \frac{|B\cap I|}{N}
 \ll\frac1\mu+\varepsilon+rac{W^2}{\mu^2\sqrt N}.
 \tag{8}
$$
For large $\mu$, the sieve error is at most
$C(\mu/8)^{-\mu/16}$. By (5), the last term is at most
$$
 \frac{W^2}{\mu^2}\,2^{(1-W)/2}
 \le2^{(1-\mu)/2}
$$
when $\mu$ exceeds an absolute constant: the function
$t^2 2^{-t/2}$ is decreasing for sufficiently large $t$, and $W\ge\mu$.
Thus (8) is $O(1/\mu)$.

Summing over dyadic intervals gives $|B\cap[1,X]|\ll X/\mu$;
enlarging to the next dyadic endpoint costs only an absolute factor.
The point $1$ is not deleted in the range under consideration, by (5)
applied to any generator. Partial summation gives the harmonic estimate.
Increasing the constant handles bounded $\mu$, proving (2).
$\square$

## Bounded overlap and complete clause families

If each prime belongs to at most $R$ of the groups, take $w_j=1/R$.
Equation (2) becomes
$$
 \frac{|B\cap[1,X]|}{X},\quad\frac{H_B(X)}{H_{\lfloor X\rfloor}}
 \ll\min\left(1,\frac{R}{\sum_j u_j}\right).
 \tag{9}
$$

There is a small-footprint consequence when the family is complete in
the following precise sense. Let $P=\bigcup_jP_j$, and take every
inclusion-minimal subset $S\subseteq P$ meeting every $P_j$. Define
$$
 D=\left\{\prod_{p\in S}p:S\text{ is such a minimal subset}\right\}.
$$
These moduli are distinct and primitive: divisibility of two of these
squarefree products is containment of their prime sets, contradicting
minimality unless the sets agree. Give every modulus its residue induced
by the one common center $\alpha$. The full Haar union is exactly
$$
 U=\bigcap_j\bigcup_{p\in P_j}[\alpha]_p.
 \tag{10}
$$
Indeed, a configuration meeting every group contains a minimal meeting
subset among its matching primes. Conversely, each generator meets
every group. Including nonminimal meeting products would change neither
the full union nor its delayed union: a minimal generator divides each
such product and is already active whenever that product is active.
The delayed union in what follows is the one activated at $n\ge q$
for these primitive product moduli; (10) is a statement about the full
Haar union, not a replacement activation rule.

Put $\beta=\mu_{\rm Haar}(U)$ and $L=\log(1/\beta)$. For $L\ge2$,
$$
 \frac{|B\cap[1,X]|}{X},\quad\frac{H_B(X)}{H_{\lfloor X\rfloor}}
 \ll\min\left(1,\frac{R\log L}{L}\right).
 \tag{11}
$$

The prime-hit events form a product of Bernoulli spaces. Positive
correlation of increasing events gives
$$
 \beta\ge\prod_j(1-u_j).
 \tag{12}
$$
This elementary correlation inequality follows by induction on the
number of coordinates: conditional covariance is nonnegative by the
induction hypothesis, and the two conditional means are increasing
functions of the last Bernoulli coordinate. Iterating the two-event
inequality proves (12).

If some $u_j\ge1-1/L$, every actual deletion belongs to the delayed
prime union for that group. In fact its active witness contains a
matching prime $p\in P_j$ with $p\le q\le n$. The individual delayed
progression bounds and
$$
 \sum_{p\in P_j}1/p\le-\log u_j
 \le-\log(1-1/L)\le2/L
$$
give (11) in this case. Otherwise, the increasing function
$-\log(1-u)/u$ is at most $2\log L$ on the possible range of $u_j$.
Equation (12) consequently gives
$$
 L\le\sum_j-\log(1-u_j)\le2\log L\sum_j u_j.
$$
Applying (9) proves (11).

This extends the complete disjoint transversal case to bounded prime
overlap. For a proper subfamily of the minimal products, (9) remains
valid, but (11) need not follow with that smaller family's footprint:
the identity (10), and hence the lower bound (12) for that footprint,
would no longer be available.

## Application to the spanning-tree obstruction

Use the family from
[the divisor-cover obstruction](divisor_cover_obstruction.md#the-spanning-tree-family).
There are $m$ graph vertices, and each edge $e$ has a disjoint prime
pool satisfying
$$
 2/m\le\sum_{p\in P_e}1/p<3/m.
$$
For a vertex $v$, let $P_v$ be the union of the pools on its incident
edges. Every spanning-tree product has a prime factor in $P_v$ for
every vertex $v$. Each prime belongs to exactly two vertex groups,
and
$$
 \sum_{p\in P_v}1/p<3,
 \qquad
 u_v=\prod_{p\in P_v}(1-1/p)\ge e^{-6},
$$
using $\log(1-1/p)\ge-2/p$. With weights $w_v=1/2$,
$\mu\ge me^{-6}/2$. Therefore, uniformly in every coherent center,
$$
 \sup_{X\ge2}\frac{|B\cap[1,X]|}{X}\ll\frac1m,
 \qquad
 \sup_{X\ge2}\frac{H_B(X)}{H_{\lfloor X\rfloor}}\ll\frac1m.
 \tag{13}
$$
The spanning-tree family is only a subfamily of the products meeting
all vertex groups. Connectivity is not being identified with absence
of isolated vertices; the one-sided certificate condition in the
weighted theorem is sufficient.

Thus this family, whose positive divisor-cover cost is exactly one
although its Haar footprint tends to zero, cannot produce a fixed
coherent harmonic anomaly. Equation (13) is an arithmetic conclusion
not supplied by the divisor-cover obstruction itself.

## Limitation: rank thresholds can have no useful blocking weight

The parameter $\mu$ in (2) need not become large when the full footprint
tends to zero, even after optimizing over all finite blocking groups
and all weights satisfying (1).

For a concrete example, let $k\to\infty$ and choose a finite prime pool
$P$ with all primes greater than $M=k^3$ such that
$$
 k\le\lambda:=\sum_{p\in P}1/p<k+1/M.
$$
Divergence of the prime reciprocal sum permits this by stopping at the
first crossing of $k$. Put $s=|P|$, $r=\lceil2\lambda\rceil$, and let
$D$ consist of all products of $r$ distinct pool primes. These moduli
are distinct and primitive. Their full footprint is
$$
 \beta=\Pr\left(\sum_{p\in P}Y_p\ge r\right),
 \qquad Y_p\text{ independent Bernoulli}(1/p).
$$
The sum has mean $\lambda$ and variance at most $\lambda$, so
Chebyshev's inequality gives $\beta\le1/\lambda\to0$.
Also $s>M\lambda$, hence $s\gg r$.

Any prime group meeting every generator must contain at least
$s-r+1$ pool primes: otherwise its complement in $P$ contains an
$r$-element generator. Primes outside $P$ do not help meet any generator.
Consequently, for any collection of such groups and any feasible weights,
summing (1) over the pool gives
$$
 (s-r+1)W\le s.
$$
Each group's avoidance probability is at most
$$
 u_j\le\exp\left(-\lambda+\frac{r-1}{M}\right),
$$
because it omits at most $r-1$ pool primes. Therefore every admissible
weighted blocking parameter satisfies
$$
 \mu\le
 \frac{s}{s-r+1}
 \exp\left(-\lambda+\frac{r-1}{M}\right)
 \longrightarrow0.
 \tag{14}
$$

These rank-threshold families are controlled by the separate
[rank-threshold theorem](rank_threshold_families.md), but not by (2).
Thus no reduction from arbitrary small-footprint coherent families to
large weighted blocking parameter has been established. The general
finite estimate $H_B(X)/H_X\le f(\beta)$ with $f(\beta)\to0$ remains
unresolved.

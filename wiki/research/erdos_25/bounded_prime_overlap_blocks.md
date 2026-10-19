---
name: research/erdos_25/bounded_prime_overlap_blocks
desc: Logarithmic density for bounded prime-overlap blocks, and for coherent systems with reciprocal-summable exceptional overlap primes.
tags: [logarithmic-density, coherent-residues, product-measures]
sources: []
created: 2026-09-22T08:29:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/bounded_prime_overlap_blocks

***

The later [branch-separated centers theorem](branch_separated_centers.md)
allows arbitrarily many blocks at a prime when their centers have bounded
multiplicity in each first-digit branch. It proves logarithmic density
for arbitrary residues satisfying
$\min(a_q,q-a_q)<C P^-(q)$, without coherence, and allows signed centers.

The theorem below extends the disjoint-prime-support result in
[prepared blocks](prepared_blocks_entropy.md). It is a sufficient
condition, not a resolution for arbitrary singleton residues.

## Theorem

Partition a family of globally distinct moduli into nonempty blocks
$D_j$. In block $j$, use a single integer residue
$$
 0\le a_j<\min D_j.
$$
Suppose each prime divides moduli in at most $R$ different blocks,
where $R$ is a fixed positive integer. Then the delayed union $B$ has
logarithmic density equal to the Haar measure of its full periodic
union. Moreover, finite congruence subfamilies approximate $B$ in upper
logarithmic density.

For a finite such family, if its full union has measure $\beta<1$,
then, for every $X\ge1$,
$$
 \frac{H_B(X)}{H_{\lfloor X\rfloor}}
 \le \min\left\{1,R\log\frac1{1-\beta}\right\}.
 \tag{1}
$$
No assertion of natural density is made when the full survivor measure
is positive.

## Product-space inequality

Let $f_1,\ldots,f_m$ be nonnegative functions on a finite product
probability space. Suppose each coordinate occurs in the dependence
sets of at most $R$ functions. Then
$$
 \mathbb E\prod_{j=1}^m f_j
 \le\prod_{j=1}^m(\mathbb E f_j^R)^{1/R}.
 \tag{2}
$$
Here the individual coordinate spaces need not be finite.

For a proof, induct on the number of coordinates. In the last
coordinate, apply Hölder with exponent $R$ to its incident factors,
padding with factors equal to one if fewer than $R$ occur. Replace
each incident $f_j$ by
$g_j=(\mathbb E_{\rm last}f_j^R)^{1/R}$, and leave the other factors
unchanged. The remaining coordinate-dependence bound is still $R$.
The induction hypothesis applies to the $g_j$, and
$\mathbb E g_j^R=\mathbb E f_j^R$. This proves (2).

## Proof of the theorem

Write
$$
 U_j=\bigcup_{q\in D_j}[a_j]_q,
 \qquad \beta_j=\mu(U_j),
 \qquad \delta=1-\mu\left(\bigcup_j U_j\right).
$$
The prime coordinates of $\widehat{\mathbb Z}=\prod_p\mathbb Z_p$
are independent under Haar measure. Apply (2) to the avoidance
indicators of finitely many finite block truncations. Exhausting each
of those blocks gives, for every finite set $J$ of block indices,
$$
 \delta\le\mu\left(\bigcap_{j\in J}U_j^c\right)
 \le\prod_{j\in J}(1-\beta_j)^{1/R}.
 \tag{3}
$$
The passage to infinite blocks is continuity of probability for
decreasing sequences of avoidance events.

If $\delta=0$, fixed finite congruence prefixes already prove natural
density zero for the survivor set, so assume $\delta>0$. Taking
logarithms in (3) and exhausting $J$ yields
$$
 \sum_j\beta_j
 \le\sum_j-\log(1-\beta_j)
 \le R\log(1/\delta)<\infty.
 \tag{4}
$$

Let $B_j$ be the delayed integer union of block $j$. The normalization
of its center gives the exact identity
$$
 B_j=a_j+M(D_j),\qquad
 M(D_j)=\bigcup_{q\in D_j}q\mathbb N.
 \tag{5}
$$
Indeed a congruence hit is active precisely at the points
$a_j+tq$ with $t\ge1$; its root $a_j<q$ is inactive. Consequently,
using the [exact harmonic inequality for multiples](basic_reductions.md),
$$
 H_{B_j}(X)
 \le H_{M(D_j)}(X)
 \le\beta_j H_{\lfloor X\rfloor}.
 \tag{6}
$$
For infinite $D_j$, at a fixed cutoff only the finitely many moduli
$q\le X$ matter, so the finite inequality applies directly.

Equations (4)--(6) give the uniform tail bound
$$
 H_{\bigcup_{j>J}B_j}(X)
 \le H_{\lfloor X\rfloor}\sum_{j>J}\beta_j.
 \tag{7}
$$
Each retained block has finite-congruence approximation in upper
logarithmic density: this is the multiples theorem followed by the
fixed translation in (5). More explicitly, for a finite subfamily
$F\subset D_j$, the multiples difference has logarithmic density
$\beta_j-\mu(M(F))$, which tends to zero as $F$ exhausts $D_j$.
Fixed translations preserve logarithmic density, because their
reciprocal-weight changes are absolutely summable. Finite unions of
retained blocks therefore have the same approximation property.
Combining it with (7) proves the theorem. The limit is the full Haar
measure, since the finite periodic union measures increase to it.

For a finite family, summing (6) and using (4), with
$\delta=1-\beta$, proves (1). Global modulus distinctness is preserved
throughout: blocks are a partition of the given modulus set, not
additional copies of congruences.

## A coherent varying-residue consequence

Suppose $a_q=\alpha\bmod q$, normalized by $0\le a_q<q$, for a fixed
$\alpha\in\widehat{\mathbb Z}$. Omit the trivial modulus-$1$ case.
If, for some fixed $C>0$,
$$
 a_q<C P^-(q)\qquad\text{for every selected }q,
 \tag{8}
$$
where $P^-(q)$ is the least prime factor, then the original delayed
system has logarithmic density and finite-periodic logarithmic
approximation.

To prove this, group the moduli by their exact normalized residue
$a_q=a$. If a prime $p$ occurs in a group, then
$$
 a\equiv\alpha\pmod p,\qquad 0\le a<Cp.
$$
At most $\lceil C\rceil$ integers in this interval have that residue
modulo $p$. Hence the block theorem applies with
$R=\lceil C\rceil$.

Condition (8) may also hold only outside a finite set of moduli:
the exceptional moduli introduce at most finitely many additional
center groups and thus increase $R$ by at most a fixed amount.

For an unrestricted coherent center, a prime can occur in arbitrarily
many normalized-residue groups. Neither (3) nor (4) then supplies the
summable block bound. This is the remaining limitation of this argument.

## Allowing a reciprocal-summable set of exceptional overlap primes

**Theorem.** Suppose the residues are coherent, and partition the moduli
by their exact normalized residues $a_q=a$. Let $\mathcal P$ be a set
of primes with $\sum_{p\in\mathcal P}1/p<\infty$. If each prime
outside $\mathcal P$ occurs in at most $R$ of these groups, then the
delayed union has logarithmic density and finite-congruence approximation
in upper logarithmic density.

There is no bound on how many groups share a prime in $\mathcal P$.
In particular, arbitrary overlap at finitely many primes is harmless.
The proof does not give a uniform finite small-footprint estimate when
the exceptional set and the needed truncations vary.

### Finite exceptional set

First suppose $\mathcal P$ is finite and nonempty. Fix $K\ge1$, and
temporarily discard every modulus divisible by $p^K$ for any
$p\in\mathcal P$. Coherence and activation imply that all discarded
hits lie in the union of the delayed classes $[\alpha]_{p^K}$.
Thus their harmonic mass is at most
$$
 H_{\lfloor X\rfloor}\sum_{p\in\mathcal P}p^{-K}.
 \tag{9}
$$
Their full Haar union has at most the same sum as its measure.

Put $L=\prod_{p\in\mathcal P}p^K$ and consider the retained family.
In a fixed fiber $n=r+Lm$, $0\le r<L$, split each root group $a$
further by $h=(q,L)$. Every retained modulus in this subblock has
the form $q=hd$, where $(d,L)=1$. Write $s=L/h$.
The subblock is incompatible with the fiber unless $a\equiv r\pmod h$.
For a compatible subblock, put $b=(a-r)/h$. For every one of its
moduli, normalization gives
$$
 -s<b<d.
$$
The original active hits, with $m\ge1$, are exactly
$$
 sm-b\in M(D'),\qquad D'=\{q/h:q\text{ is in the subblock}}.
 \tag{10}
$$
Indeed $n-a=h(sm-b)$; being a positive multiple of $q=hd$ is
equivalent to (10). It automatically gives $n\ge a+q\ge q$.
For such a hit, $k=sm-b>0$ and
$$
 k<s(m+1)\le2sm,
 \qquad \frac1m\le\frac{2s}{k}.
$$
Since $m\mapsto k$ is injective, the exact multiples inequality gives
$$
 H_{\text{projected subblock}}(T)
 \le2s\,\beta_{D'} H_{\lfloor s(T+1)\rfloor},
 \qquad \beta_{D'}=\mu(M(D')).
 \tag{11}
$$
The full projected union has measure exactly $\beta_{D'}$:
multiplication by $s$ and translation by $-b$ preserve Haar measure
on all coordinates appearing in $D'$, since $(d,s)=1$.

Outside $\mathcal P$, a prime now occurs in at most $R\tau(L)$
projected subblocks, where $\tau(L)$ is the number of divisors of $L$.
No prime in $\mathcal P$ occurs in $D'$. Let $\delta_r$ be the
full survivor measure of the projected family in the chosen fiber.
If $\delta_r>0$, product-space Hölder, as in (3)--(4), gives
$$
 \sum_{\text{compatible subblocks}}\beta_{D'}
 \le R\tau(L)\log(1/\delta_r)<\infty.
 \tag{12}
$$
Here $L$ is fixed. The ratios
$H_{\lfloor s(T+1)\rfloor}/H_{\lfloor T\rfloor}$ are bounded by
a constant depending only on $L$, uniformly for $T\ge1$.
Consequently (11)--(12) give uniformly negligible harmonic tails of
subblocks.

Each individual subblock also has finite-congruence logarithmic
approximation. Under (10), deleting all but finitely many generators
restricts a difference of two multiples sets to one residue modulo $s$.
The unrestricted multiples difference has logarithmic density tending
to zero as the generators are exhausted; the inequality $1/m\le2s/k$
transfers its upper harmonic bound. This suffices even though no
density for the restricted multiples difference is being assumed.
Thus (12) yields finite-congruence approximation for the entire fiber.

If $\delta_r=0$, finite prefixes of the projected family have survivor
densities tending to zero. Each such prefix is eventually periodic,
so its complement bounds the tail and gives the same approximation
conclusion. The finitely many original integers represented by $m=0$
do not matter. Finally, the affine map $m\mapsto r+Lm$ divides upper
logarithmic density by $L$. Summing over the finitely many fibers
establishes the conclusion for the retained family.

Let $K\to\infty$ in (9). Uniform harmonic approximation and the
corresponding Haar bound transfer finite-congruence approximation and
the Haar value to the original family. If $\mathcal P$ is empty,
the original bounded-overlap theorem applies directly.

### Infinite reciprocal-summable exceptional set

First discard moduli containing any $p\in\mathcal P$ with $p>Y$.
Every discarded active hit is in the delayed class $[\alpha]_p$
for such a prime, so its normalized harmonic mass, and the Haar
measure of the discarded union, are at most
$$
 \sum_{\substack{p\in\mathcal P\\p>Y}}\frac1p.
$$
For the retained family, the only exceptional primes are the finitely
many in $\mathcal P\cap[1,Y]$. Apply the finite-exception argument
and then let $Y\to\infty$.

All subblocks are partitions or restrictions of the original distinct
moduli. Effective moduli may repeat across subblocks, but Hölder is
applied to subblock events, not to a newly asserted singleton system.
Thus no duplicate-modulus construction is introduced. Coherence is
essential for both exceptional-prime deletion bounds. The argument
does not handle unbounded overlap on a set of primes with divergent
reciprocal sum.

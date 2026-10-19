---
name: research/erdos_25/colored_towers
desc: A uniform weighted-antichain bound rules out the zero-base colored-tower construction.
tags: [obstructions, primitive-sets]
sources: []
created: 2026-09-22T01:12:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/colored_towers

***

## The construction that was being tested

Let $M=2^r$. For odd base moduli $g$, choose classes $C_g$ and colors
$c_g\pmod M$. Binary tower precursors can cover
$C_g\setminus[c_g]_M$. The old survivor portion inside the base union is
therefore
$$
 H=\left\{n\in\bigcup_gC_g:
     n\equiv c_g\pmod M\text{ for every }g\text{ with }n\in C_g\right\}.
$$
Its Haar measure is at most $1/M$: after fixing all odd-prime
coordinates, at most one of the $M$ possible $2$-adic residues survives.
This offers a small *incremental* footprint, not a small full footprint.
The unresolved construction was to make the actual trace of $H$ have
positive normalized harmonic mass beyond all precursor activation thresholds.

For zero base classes and the choice $c_g=g\pmod M$, selecting base
endpoints from a set $D$ imposes
$$
 d,e\in D,\quad d\mid e\quad\Longrightarrow\quad e/d\equiv1\pmod M.
 \tag{1}
$$
The following uniform estimate rules out this particular synchronization
mechanism, even for finite epochs with $M$ varying.

## Uniform finite estimate: proved

There is an absolute constant $C$ such that, if $M\ge2$, $X\ge2$, and
$D\subset\mathbb N$ has no two distinct members with divisibility ratio
in $\{2,\ldots,\lfloor M\rfloor\}$, then
$$
 \frac{H_D(X)}{H_{\lfloor X\rfloor}}
 \le\frac{C}{\sqrt{\log\log(3+\min(M,X))}}.
 \tag{2}
$$
Condition (1) has this property. Thus its normalized harmonic mass tends
to zero whenever both $M$ and the cutoff tend to infinity.

### Weighted antichains of smooth integers

For a finite prime set $P$, put
$$
 Z_P=\prod_{p\in P}(1-1/p)^{-1}.
$$
Every divisibility antichain $S$ of $P$-smooth integers satisfies
$$
 \sum_{a\in S}\frac1a\le\theta_P Z_P,
 \qquad
 \theta_P\ll\left(1+\sum_{p\in P}\frac1{p+1}\right)^{-1/2}.
 \tag{3}
$$
For a proof, take independent geometric valuations
$\Pr(V_p=v)=(1-1/p)p^{-v}$. Their product assigns a smooth integer $a$
mass $1/(Z_Pa)$. Decompose independently
$$
 V_p=B_p+2W_p,
 \qquad B_p\sim\operatorname{Bernoulli}(1/(p+1)),
$$
where $W_p$ is geometric with ratio $p^{-2}$. Further represent
$B_p=I_pJ_p$, with $I_p$ Bernoulli of parameter $2/(p+1)$ and $J_p$ fair.
Conditional on the $W_p$ and $I_p$, an antichain is an antichain of a
uniform Boolean cube of dimension $R=\sum_pI_p$. Sperner's bound gives
conditional probability $O((R+1)^{-1/2})$.
Since $\mathbb ER=2\sum_p1/(p+1)$ and
$\operatorname{Var}(R)\le\mathbb ER$, splitting at $R=\mathbb ER/2$
and applying Chebyshev proves (3).

### Smooth-part decomposition

Write $n=ab$ uniquely, with $a$ $P$-smooth and $b$ $P$-rough, and set
$$
 C_P=\sum_{p\in P}\frac{\log p}{p-1}.
$$
The harmonic mass of integers with $a>M$ is at most
$C_PH_{\lfloor X\rfloor}/\log M$, because
$$
 \sum_{n\le X}\frac{v_p(n)}n
 =\sum_{j\ge1}p^{-j}H_{\lfloor X/p^j\rfloor}
 \le\frac{H_{\lfloor X\rfloor}}{p-1}.
$$
For fixed $b$, the selected smooth parts
$\{a\le\min(M,X/b):ab\in D\}$ form an antichain: comparable distinct
members would have a forbidden ratio at most $M$. Hence (3) gives
$$
 H_D(X)\le\frac{C_P}{\log M}H_{\lfloor X\rfloor}
       +\theta_PZ_P H_{\mathrm{rough},P}(X).
 \tag{4}
$$

For a uniform rough harmonic bound, put
$$
 A_P=\prod_{p\in P}(1+1/p),\qquad
 B_P=\sum_{p\in P}\frac{\log p}{p+1}.
$$
Inclusion--exclusion and
$0\le H_{\lfloor X\rfloor}-H_{\lfloor X/d\rfloor}\le1+\log d$
give
$$
 H_{\mathrm{rough},P}(X)
 \le H_{\lfloor X\rfloor}/Z_P+A_P(1+B_P).
$$
Combining with (4),
$$
 \frac{H_D(X)}{H_{\lfloor X\rfloor}}
 \le\theta_P+\frac{C_P}{\log M}
 +\frac{\theta_PZ_PA_P(1+B_P)}{H_{\lfloor X\rfloor}}.
 \tag{5}
$$

Take the odd primes at most $z=\exp((\log Y)^{1/4})$, where
$Y=\min(M,X)$, treating bounded $Y$ by increasing $C$.
The Mertens product bound gives $Z_P,A_P\ll\log z$ and
$C_P,B_P\ll\log z\log\log z$. Also
$\sum_{p\in P}1/(p+1)\ge\log\log z-O(1)$: the Euler product over all
primes at most $z$ dominates $H_{\lfloor z\rfloor}$, and the logarithm
of that product differs from $\sum_{p\le z}1/p$ by $O(1)$.
Thus $\theta_P\ll(\log\log Y)^{-1/2}$, while the two error terms in
(5) are smaller. This proves (2).

The Mertens bound used here is the passage before equation (12) of the
[Davenport--Erdős 1951 full source](../../../library/divisors/davenport_1951_sequences_positive_integers/_index.md),
already checked for the earlier smooth-number arguments and checked again
for this application. The remaining ingredients are elementary product
probability, Sperner's theorem, and inclusion--exclusion.

## Exact infinite bound for the colored condition

For completeness, (1) has the sharper infinite conclusion
$\overline{\operatorname{ld}}(D)\le1/M$. Partition $D$ by odd residues
$c\pmod M$, writing $U_c=M(D_c)$. Then $D$ is contained in
$$
 \bigcup_c\left([c]_M\cap
       \left(U_c\setminus\bigcup_{b\ne c}U_b\right)\right).
$$
Each multiples union has finite-periodic approximation in logarithmic
density. The displayed finite Boolean combination therefore has its Haar
density. The events $U_c\setminus\bigcup_{b\ne c}U_b$ are disjoint and
depend only on odd-prime valuations, independently of the $2$-adic residue.
Its density is at most $1/M$. Equality holds for $D=[1]_M$.
This infinite bound alone would not have ruled out varying finite epochs;
that is the purpose of (2).

No corresponding theorem was obtained for arbitrary nonzero base classes.

## A bounded number of coherent components cannot supply dense early first kills

Suppose a finite singleton system partitions into $h$ coherent
subfamilies, each with its own common profinite residue. A modulus
divisible by a smaller modulus in its own subfamily cannot first-kill
any integer: the smaller class contains it and is already active.
Consequently all global first-kill moduli belong to the primitive
cores of their respective subfamilies.

Apply (2) above to each primitive core with $M=X$. If $T_K(X)$ is the
set of first kills up to $X$ whose witnessing quotient
$t=(n-a_q)/q$ satisfies $1\le t\le K$, then
$$
 \frac{H_{T_K}(X)}{H_{\lfloor X\rfloor}}
 \ll \frac{hH_{\lfloor K\rfloor}}
           {\sqrt{\log\log(3+X)}}.
$$
Indeed the contribution of one witnessing modulus is at most
$H_{\lfloor K\rfloor}/q$, and the harmonic sums of its primitive
core obey (2). This bound is uniform in the component centers, even
if those centers vary between finite epochs.

Thus boundedly many coherent components cannot synchronize a positive
logarithmic mass of bounded-quotient first kills. This does not control
unbounded quotients, and does not settle even the single coherent
infinite-family case.

The later [ordered-run theorem](ordered_coherent_runs.md) permits
$o(\log X)$ coherent components below $X$ when they occupy consecutive
modulus intervals. Its uniform primitive-annulus lemma exploits this
ordering and does not apply to arbitrarily interlaced components.

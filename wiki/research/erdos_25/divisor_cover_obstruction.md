---
name: research/erdos_25/divisor_cover_obstruction
desc: Small-footprint primitive families can have positive divisor-cover cost exactly one.
tags: [coherent-residues, obstructions, fractional-covers]
sources: []
created: 2026-09-22T09:01:09Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/divisor_cover_obstruction

***

This is an obstruction to one proposed finite harmonic upper sieve,
not a counterexample to Problem 25. The construction has zero residues,
so its actual logarithmic density is already understood.

For a finite modulus set $D$, consider nonnegative weights $c_d$ with
$$
 \sum_{d\mid q}c_d\ge1\qquad(q\in D).
 \tag{1}
$$
For a coherent center $\alpha$, a hit of an active modulus $q$
also hits each divisor $d\mid q$, actively, since $n\ge q\ge d$.
Thus (1) gives the pointwise majorant
$$
 \mathbf1_{B_{D,\alpha}}(n)
 \le\sum_d c_d\mathbf1_{\{n\ge d,\ n\equiv\alpha\ (d)\}}.
$$
The exact delayed progression inequality bounds its normalized harmonic
mass by $\sum_d c_d/d$. The question was whether small full footprint
always permits such a cover of small cost.

**Proposition.** There are finite distinct primitive sets $D_m$ with
$\beta_m=\mu(M(D_m))\to0$, but
$$
 \inf_{c_d\ge0\text{ satisfying (1)}}\sum_d\frac{c_d}{d}=1.
 \tag{2}
$$
Only divisors of generators need receive weight, so this is a finite
optimization problem.

## The spanning-tree family

Let $m\ge6$. To each edge $e$ of the complete graph on $m$ vertices
assign a finite prime set $P_e$, with all these sets disjoint and all
primes greater than $m$, such that
$$
 \frac2m\le\lambda_e:=\sum_{p\in P_e}\frac1p<\frac3m.
$$
Successively taking unused primes until their reciprocal sum first
reaches $2/m$ constructs the blocks, by divergence of the prime
reciprocal sum.

For every spanning tree, choose one prime from each of its edges and
include their product in $D_m$. Distinct choices give distinct products,
since each prime identifies its edge. All products are squarefree of
rank $m-1$, so the family is primitive.

For a Haar integer, declare an edge present when at least one of its
assigned primes divides the integer. These are independent edge events,
of probabilities
$$
 t_e=1-\prod_{p\in P_e}(1-1/p)\le\lambda_e<3/m.
$$
The integer belongs to $M(D_m)$ exactly when this random graph is
connected.

Let $I_v$ indicate that vertex $v$ is isolated and let $Z=\sum_v I_v$.
For $m\ge6$,
$$
 \mathbb E I_v\ge(1-3/m)^{m-1}\ge e^{-6}.
$$
For distinct vertices $v,w$, direct cancellation of the shared edge
gives
$$
 \operatorname{Cov}(I_v,I_w)
 =\mathbb E I_v\,\mathbb E I_w
       \frac{t_{vw}}{1-t_{vw}}\le\frac6m.
$$
Hence $\mathbb EZ\gg m$ and $\operatorname{Var}Z=O(m)$.
Chebyshev's inequality gives
$$
 \beta_m\le\Pr(Z=0)=O(1/m).
 \tag{3}
$$

## A probability certificate for the cover cost

Sample a uniform spanning tree $T$. Independently on each of its
edges $e$, choose $p\in P_e$ with probability $(1/p)/\lambda_e$.
Let $Q\in D_m$ be the resulting product. We claim that
$$
 \Pr(d\mid Q)\le1/d\qquad(d\ge1).
 \tag{4}
$$
The probability is zero unless $d$ is squarefree, uses at most one
prime from each edge, and its selected edges form a forest.
For such a forest $F$ with $k$ edges and component sizes $s_1,\ldots,s_c$,
including isolated vertices, the uniform-tree inclusion probability is
$$
 \Pr(F\subseteq T)=m^{-k}\prod_{i=1}^c s_i\le(2/m)^k.
 \tag{5}
$$
For completeness, collapsing the forest components leaves a tree on
$c$ vertices. Each intercomponent edge has $s_i s_j$ choices of endpoints.
The Prüfer-code identity
$\sum_{T'}\prod_i s_i^{\deg_{T'}(i)}
 =(\prod_i s_i)(\sum_i s_i)^{c-2}$
therefore counts $m^{c-2}\prod_i s_i$ extensions of $F$.
Dividing by $m^{m-2}$ gives (5); the case $c=1$ is immediate.
Finally $s_i\le2^{s_i-1}$ and $\sum_i(s_i-1)=k$ prove its inequality.

Multiplying (5) by the probabilities of choosing the prescribed
edge primes, and using $\lambda_e\ge2/m$, yields
$$
 \Pr(d\mid Q)
 \le(2/m)^k\prod_{p\mid d}\frac{m}{2p}=1/d.
$$
This proves (4), including $d=1$.

Averaging (1) against this random $Q$ now gives
$$
 1\le\mathbb E\sum_{d\mid Q}c_d
   =\sum_d c_d\Pr(d\mid Q)\le\sum_d c_d/d.
$$
The choice $c_1=1$ attains equality, proving (2).

## Scope

The obstruction allows arbitrary positive combinations of divisor
subcertificates, not just a fixed-rank or a single-prime sieve. The
missing arithmetic bound cannot be obtained solely by optimizing this
positive majorant and then applying individual progression bounds.
The construction does not estimate the actual shifted harmonic trace
and does not refute a universal finite bound
$H_B(X)/H_X\le f(\beta)$ by a different method.

## A different pointwise majorant is also too restrictive

Allowing arbitrary cylinders contained in the full union, rather
than only divisor subcertificates, does not fix every positive
majorant strategy. Let $U=\bigcup_{p\le X}[0]_p$, using prime
moduli, and attempt to majorize every activated deletion pointwise
by nonnegative multiples of delayed cylinders $[b]_d\subseteq U$,
at cost $\sum w_{d,b}/d$.

Any full cylinder contained in this $U$ must itself be contained in
some $[0]_p$. Otherwise CRT, choosing a nonzero residue at each
selected prime not already fixed by $d$, gives a point of the
cylinder outside $U$. At the active endpoint $n=p$, a contributing
cylinder must have $d\le p$ and contain $p$. Its containing zero
prime class must therefore be $[0]_p$, forcing $d=p$ and $b=0$.
Thus its weight must be at least one for every selected prime.
The total cost is at least $\sum_{p\le X}1/p$, which diverges,
although $\mu(U)\le1$ and the actual zero-residue harmonic bound
has constant one. This particular pointwise, activation-preserving
cover is therefore too strong even in a solved case; a valid dual
may need to transport weights rather than cover every point at
unit height.

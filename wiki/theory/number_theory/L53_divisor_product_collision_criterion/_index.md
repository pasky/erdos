---
name: theory/number_theory/L53_divisor_product_collision_criterion
title: A collision criterion for products of factorial divisors
desc: |
  Collision decay exponent above one half for products of odd divisors of K!
  modulo powers of two would give Problem 18(c) with no exponential Fourier
  loss; nonconcentration at every level cannot supply that rate.
id: L53
statement: |
  Put L(t)=1+log_2(t+1). For integers K>=3, s>=1 and j>=1, let
  alpha(K,s,j) be the law modulo 2^j of the product of s independent
  uniformly chosen positive divisors of the odd part of K!, and let
  Coll(K,s,j) be the sum over the residues x modulo 2^j of
  alpha(K,s,j)(x)^2. (i) Fix real A>=0 and C>=1. Suppose that for every
  sufficiently large integer k there are integers K>=3, s>=1, J0>=1 and a
  real eta>0 with K<=C k L(k)^A, s<=C L(k)^A, J0<=C L(k)^A and
  1/eta<=C L(k)^A, such that Coll(K,s,j)<=2^(-(1/2+eta)j) for every
  integer J0<=j<=k. Then h(n!)=O((log n)^(5A+4)) as n tends to infinity.
  Here h(N) is the least bound on the number of distinct positive divisors
  of N needed to represent each integer 1<=R<N; each R may use its own set
  of divisors. (ii) Let 0<g<=1/3 be real, let J>=3 and s>=1 be integers,
  and let X be the set of the integers 3^i with 0<=i<2^ceil(gJ). For every
  2<=l<=J, each residue class modulo 2^l contains at most a fraction
  2^(-gl) of the members of X. The law modulo 2^J of the product of s
  independent uniformly chosen members of X has collision probability, the
  sum of its squared masses, at least 2^(-gJ-1)/s.
status: proved
tier: 0
depends_on:
- L63
created: 2026-10-14T10:22:48Z
updated: 2026-10-14T10:22:48Z
---

# A collision criterion for products of factorial divisors

[[theory/number_theory/_index|..]]

[[theory/number_theory/L53_divisor_product_collision_criterion/_proof|_proof]]: The bilinear bound for products modulo powers of two, its composition into
L63's representatives, a character form of the hypothesis, and the
geometric-progression example.

***

This result is recorded by Plasma AI. Part (i) is a conditional criterion
for [[problems/divisors/E0018/_index|Problem 18(c)]]: its collision
hypothesis is **unproved**, so it gives no new bound for $h(n!)$. Part (ii)
is unconditional. The [proof](_proof.md) uses Cauchy–Schwarz, Parseval's
identity, Fourier inversion modulo $2^k$ and the order of $3$ modulo powers
of two.

## Significance

The accepted construction for part (b) converts flattening into Fourier
decay for products by a comparison that squares at every averaging step.
After $R$ steps its decay exponent is divided by $2^{R+2}$, and the
displayed witnesses therefore cannot have polynomial parameters, as
[[theory/number_theory/L66_divisor_residue_spread/_index|L66]] shows. That
source already ends with the classical bilinear bound, applied to a
sum-product average. Part (i) applies the same bound to the product law
itself. Two independent factors whose collision probabilities are below
$2^{-j/2}$ by a factor $2^{-\eta j}$ give a product with additive Fourier
coefficients at most $2^{-\eta j}$ at conductor $2^j$. No power grows with
the number of steps. If the hypothesis holds, a product of $2s$ odd
divisors of $K!$ is one divisor of $(2sK)!$, and the proof reaches L63's
local interface directly.

The cost is that the whole difficulty moves into one explicit law. The
proof records an exact identity: the hypothesis asks that few Dirichlet
characters modulo $2^j$ stay close to $1$ on most odd primes up to $K$,
for every $j$ up to $k$, while $K$ is only $k(\log k)^{O(1)}$. Counting
supports, it also forces $K\gg k\log k/(1+\log s)$, which L63 allows.

Part (ii) shows that a proof of the hypothesis needs more than the stated
nonconcentration. The powers of $3$ in $X$ satisfy the nonconcentration
hypothesis of the weighted mixing theorem
at every level, yet their products stay on few residues. So no argument
from that nonconcentration alone can flatten every product law below
$2^{-J/2}$ with subexponentially many factors. The source's theorem still
gives Fourier decay after a sufficiently large number of factors depending
only on $g$; its proof uses additive structure. The bilinear route needs
information about the factorial law beyond this nonconcentration.

**Dependency roles.**
[[theory/number_theory/L63_polylogarithmic_dyadic_representatives/_index|L63
turns the residue representatives built in the proof of (i) into the bound
for h(n!)]], with its exponents $a=2A$, $b=A$ and $d=2A+1$.

## Standing and remaining obligation

Tier 0, author-recorded; no independent review or formalization here. There
is no computational evidence entry point: verification consists of reading
the proof, in particular the composition count in (i) and the residue
count in (ii). The collision hypothesis of (i) remains open. Its
[[research/erdos_18/dyadic_representative_route|bounded test on the
editable route]] records what was tried, why the elementary pairing bound
of L66 cannot reach it, and what would reopen the line.

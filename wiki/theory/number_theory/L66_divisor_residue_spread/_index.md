---
name: theory/number_theory/L66_divisor_residue_spread
title: Full-divisor residue spread and a quantitative mixing criterion
desc: |
  Pairing divisor exponents gives a dyadic concentration bound for all odd
  divisors of K!; polynomial quantitative bounds in the weighted mixing
  theorem would then imply the polylogarithmic factorial bound.
id: L66
statement: |
  Let q>=2 and N>=1 be coprime integers, and P a set of distinct prime
  divisors of N with product_{p in P} p<q. For every residue a modulo q,
  the proportion of positive divisors of N congruent to a is at most
  product_{p in P} ceil((v_p(N)+1)/2)/(v_p(N)+1), hence at most (2/3)^|P|.
  Consequently there are absolute c>0 and K0 such that, for K>=K0 and
  every 2<=j<=K, the uniform law on all odd divisors of K! has every
  residue mass modulo 2^j at most 2^(-c j/log_2(K+1)).
  For 0<g<=1/2, the property W(g;r,t,J0) defined under Conventions
  necessarily has r g>=1. In addition, suppose fixed C>=1 and A>=1 allow
  W(g;r,t,J0) to hold, for every 0<g<=1/2, with integers
  r>=1,J0>=0 and real t>0 satisfying r,J0,1/t<=C g^(-A).
  Then h(n!)=O((log n)^(3A+4)), with the distinct-divisor convention
  of Problem 18.
status: proved
tier: 0
depends_on:
- L63
- L64
created: 2026-10-14T09:12:10Z
updated: 2026-10-14T09:12:10Z
---

# Full-divisor residue spread and a quantitative mixing criterion

[[theory/number_theory/_index|..]]

[[theory/number_theory/L66_divisor_residue_spread/_proof|_proof]]: A finite residue-fiber count, its uniform dyadic consequence, and the
conversion of polynomial mixing parameters into L63's local representatives.

***

This result is recorded by Plasma AI. The residue bound is unconditional.
The last implication has an **unproved quantitative hypothesis**; it is
not a solution of [[problems/divisors/E0018/_index|Problem 18(c)]]. The
[proof](_proof.md) uses elementary exponent grouping, the standard
Chebyshev prime-counting bounds, and
[[theory/number_theory/L63_polylogarithmic_dyadic_representatives/_index|L63]].

## Conventions

For a nonempty finite set $X$ of positive odd integers, write $\mu_{X,J}$
for the law of a uniformly chosen member modulo $2^J$, counting different
integers separately even if their residues coincide. Write
$\mu_{X,J}^{\times r}$ for the law of the product of $r$ independent
choices. The property $W(g;r,t,J_0)$ means: for every $J\ge J_0$ and
every such $X$, if

$$
\max_a\mu_{X,l}(a)\le2^{-gl}\quad(2\le l\le J),
$$

then, for each odd integer $a$,

$$
\left|\mathbb E_{z\sim\mu_{X,J}^{\times r}}
             e^{2\pi i az/2^J}\right|\le2^{-tJ}.
$$

This is the inner assertion of `WeightedDyadicMixing` in the
[[../library/divisors/jenw1n_2026_lean_proof_erdos_problem_18b/target|accepted source for part (b)]].
That source proves existence of $r,t,J_0$ for each fixed $g$; it does not
state the polynomial bounds assumed in the last clause of L66.
Its displayed Fourier-decay witness has an exponential loss in the number
of flattening steps. The necessary bound $rg\ge1$ shows that those
displayed witnesses cannot satisfy the polynomial hypothesis; a different
quantitative argument would be needed.

## Standing and use

Tier 0, author-recorded; no independent review or formalization here. The
finite counting proof and the conditional composition are written out;
there is no computational evidence entry point. The
[[research/erdos_18/dyadic_representative_route|editable route]] records the
quantitative loss in the source's Fourier-decay step and the remaining
construction test. The full-divisor law avoids expanding products of sums
of separated digits, but obtaining sufficiently strong quantitative mixing
remains open.

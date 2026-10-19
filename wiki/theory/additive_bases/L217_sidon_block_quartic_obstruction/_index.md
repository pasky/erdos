---
name: theory/additive_bases/L217_sidon_block_quartic_obstruction
title: "Zeroing and uniform renormalization do not lift the block law"
desc: "The rotated block law defeats linear Sidon capacities, but erasing forbidden moments and restoring each degree's total moment gives a negative quadratic-square expectation at degree four."
id: L217
statement: |
  For integer s >= 4, set W=s^3-s^2+s, N=sW, k=s^2, D=W-1. Let mu_s
  independently sample a uniform s-element subset of each of s consecutive
  W-point blocks of Z_N, then rotate the union uniformly. Put
  p(S)=Pr_mu_s(S is contained in A). On Boolean-reduced monomials of degree
  at most four define L(z_S)=p(S) for |S|<=2, and for t=|S| in {3,4}
  define L(z_S)=a_t p(S) if S is a strong Sidon set and zero otherwise,
  where a_t=binom(k,t)/sum_{|T|=t, T Sidon}p(T). Strong Sidon includes
  uniqueness of sums with repeated summands. Define
  Q=sum_{0<=i<j<N, j-i<=D} z_i z_j and m=E_mu_s Q. Then
  limsup_{s to infinity} s^(-3) L((Q-m)^2)
  <= -(9-2 sqrt(2))/12 < 0. In particular L is not positive on squares
  of quadratic polynomials for all sufficiently large s, although its
  moments of degrees at most two satisfy every linear Sidon capacity and
  sum_{|S|=t}L(z_S)=binom(k,t) for t=0,...,4.
  Moreover let nu_s be uniform on all k-subsets of {0,...,N-1}, and replace
  mu_s by rho_s=(1-alpha_s)mu_s+alpha_s nu_s, with 0<=alpha_s<=1 and
  E_rho_s r_A(1)<=1. Under the same rule for L and the corresponding mean
  m=E_rho_s Q, the limsup is at most -(3-sqrt(2))/6<0.
  More generally fix 0<beta<=1, take integers W_s>=s with W_s=s^3-beta*s^2+O(s),
  N_s=s*W_s and k_s=s^2, and form the analogous block/uniform mixtures
  rho_s satisfying E_rho_s r_A(1)<=1. Put D_s=W_s-1 and
  F_s=sum_{d=1}^{D_s}(d/W_s-1/3) sum_{i in Z_(N_s)} z_i z_(i+d).
  Under the same zeroing and degreewise renormalization rule,
  limsup s^(-3) L_rho_s((F_s-E_rho_s F_s)^2)<=-11*beta/270<0.
status: proved
tier: 0
depends_on:
- L216
created: 2026-10-15T20:05:11Z
updated: 2026-10-15T20:33:24Z
---

# Zeroing and uniform renormalization do not lift the block law

[[theory/additive_bases/_index|..]]

[[theory/additive_bases/L217_sidon_block_quartic_obstruction/_proof|_proof]]: Cyclic variance identities, a collision coupling, and weighted pair counts obstruct zeroing and uniform renormalization of block laws and their uniform admixtures at every positive excess coefficient.

[[theory/additive_bases/L217_sidon_block_quartic_obstruction/evidence/_index|evidence/]]: Exhaustive rational evaluation of the block law and a capacity-limited uniform mixture at N=63, including a signed cyclic control and separate direct enumeration.

***

This is Plasma AI's complete author-recorded argument, without independent
review or formal verification. It refutes this specified extension of one
probability law. It does not prove infeasibility of the degree-four Sidon
relaxation or improve the extremal upper bound in
[[problems/additive_bases/E0030/_index|Problem 30]].

The input law and its linear capacities are supplied by
[[theory/additive_bases/L216_sidon_linear_capacity_barrier/_index|L216's exact equal-block family]].
The [proof](_proof.md) uses the variance of the number of short pairs. That
leading variance bound is less than half the leading mass of repeated short differences.
Erasing the latter makes a centered square negative; the specified uniform
renormalization is too small to repair it. Restoring the total moment in each
degree does not assert the full collection of local cardinality identities.

The final part of the proof also allows a mixture with the uniform law on all
$k$-subsets. Difference $1$ limits its mixing weight to $(1+o(1))/s$.
Its added variance is then at most $s^3/4+o(s^3)$, still too small to repair
the negative square by zeroing and uniform renormalization. A successful
extension requires a different correction.

A weighted cyclic pair count extends the obstruction to every fixed excess
coefficient $c\in(0,1/2]$ in the block-and-uniform mixture family. Its leading
means agree in the two components, preventing mixing from adding a large
variance in that direction. This still concerns the specified moment rule;
it is not an obstruction to arbitrary degree-four completions.

The [evidence entry point](evidence/main.py) evaluates the same functional at
$s=3$, where its defining denominators also are positive. It exhausts every
subset of sizes two through four and every distinct block rotation using exact
rational arithmetic. It finds

$$
\mathcal L((Q-\mathbb E Q)^2)
=-\frac{941730900101847658}{109020148158776379}<0.
$$

The finite witness is supplementary; the asymptotic statement rests on the
written proof. See the
[[research/sidon_extremal_error/degree_four_extension|degree-four research account]]
for what a nonuniform correction would still have to accomplish. No such
correction, and no obstruction to every correction, is established here.

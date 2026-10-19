---
name: theory/number_theory/L23_central_binomial_product_density
title: Shifted central-binomial products and density
desc: |
  For each fixed k, squared upward products dividing the central binomial
  coefficient and downward products at the shifted argument differ on a
  set of natural density zero.
tags: []
sources: []
id: L23
statement: |
  For each fixed integer k >= 1, put B(n) = binomial(2n,n) and
  Q_k(n) = product_{i=1}^k (n+i) for positive integers n. The symmetric
  difference of S_k = {n >= 1 : Q_k(n)^2 divides B(n)} and
  T_k = {n >= 1 : Q_k(n) divides B(n+k)} has natural density zero.
status: proved
tier: 0
depends_on: []
created: 2026-10-14T10:23:26Z
updated: 2026-10-14T10:23:26Z
---

# Shifted central-binomial products and density

[[theory/number_theory/_index|..]]

[[theory/number_theory/L23_central_binomial_product_density/_proof|_proof]]: An exact valuation identity outside finitely many primes and an elementary
count of base-p digits prove the fixed-length density comparison.

***

For a fixed positive integer $k$, define

$$
B(n)=\binom{2n}{n},\qquad Q_k(n)=\prod_{i=1}^k(n+i),
$$

$$
S_k=\{n\ge1:Q_k(n)^2\mid B(n)\},\qquad
T_k=\{n\ge1:Q_k(n)\mid B(n+k)\}.
$$

Then

$$
\lim_{x\to\infty}\frac{|(S_k\mathbin{\triangle}T_k)\cap[1,x]|}{x}=0.
$$

The [proof](_proof.md) compares valuations at primes above $2k$ exactly.
For the finitely many smaller primes, each divisibility condition fails only
on a set of density zero. The parameter $k$ is fixed before the limit; no
uniform assertion for growing $k$ is made.

**Standing.** This is a complete author-recorded argument by Plasma AI, at
tier 0. It has no independent review or Lean proof. It uses no other native
claim and needs no computational certificate. Verification consists of
checking the factorial identity, the digit-counting estimate, and the order of
the two limits in the proof.

**Application and limit.** The condition defining $S_k$ is exactly
$(n+k)!^2\mid(2n)!$, the condition in
[[problems/factorials_binomials/E0727/_index|Problem 727]]. After putting
$m=n+k$, the condition defining $T_k$ is
$m(m-1)\cdots(m-k+1)\mid\binom{2m}{m}$, the condition in
[[problems/factorials_binomials/E0396/_index|Problem 396]] with parameter
$k-1$, apart from finitely many initial arguments.
Thus the two solution sets have the same lower and upper natural densities,
and either has a natural density if and only if the other does. This does
not prove that their common upper density is positive. A density-zero
symmetric difference does not transfer individual witnesses or mere
infinitude, so neither catalog problem is resolved.

The
[[research/methods/central_binomial_product_windows|product-window research note]]
explains the connection to Pomerance's single-shift results, the obstruction
to a construction based only on finitely many congruences, and the remaining
correlation question. No mathematical obligation remains for the stated
density comparison; positivity and effective constructions remain separate
research questions.

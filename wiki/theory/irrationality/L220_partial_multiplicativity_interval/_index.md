---
name: theory/irrationality/L220_partial_multiplicativity_interval
title: Totient comparisons preserving finitely many prime laws fill an interval
desc: |
  Positive integer sequences arbitrarily close to the totient, agreeing at
  every prime power and obeying its multiplication laws at any fixed finite
  set of primes, can have any binary sum in an interval about the totient sum.
tags: []
sources:
- problems/irrationality/E0249
id: L220
statement: |
  Let phi be Euler's totient with phi(1)=1, and put
  S=sum_{n>=1} phi(n)*2^(-n). For every integer y>=2, integer M>=1 and
  real epsilon with 0<epsilon<1, there is d>0 such that every real r with
  |r-S|<d is the absolutely convergent sum sum_{n>=1} f(n)*2^(-n) of a
  positive integer-valued function f satisfying all the following:
  f(1)=1 and f(p^a)=phi(p^a) for every prime p and integer a>=1;
  f(n) is congruent to phi(n) modulo M for every n>=1;
  (1-epsilon)*phi(n)<=f(n)<=(1+epsilon)*phi(n) for every n>=1;
  for every prime p<=y and every n>=1, f(p*n)=(p-1)*f(n) if p does not
  divide n, and f(p*n)=p*f(n) if p divides n;
  and the number of n<=X with f(n) different from phi(n) is O(X/log X)
  as X tends to infinity, with the implied constant allowed to depend
  on y, M and epsilon.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T21:48:35Z
updated: 2026-10-15T21:48:35Z
---

# Totient comparisons preserving finitely many prime laws fill an interval

[[theory/irrationality/_index|..]]

[[theory/irrationality/L220_partial_multiplicativity_interval/_proof|_proof]]: Greedy rounding against complete smooth-orbit weights preserves finitely
many prime multiplication laws; sparse composite rough parts protect every
prime-power value, and a nearby target keeps all coefficients positive.

***

For every fixed $y\ge2$, $M\ge1$ and $0<\varepsilon<1$, the values
$\sum_{n\ge1}f(n)2^{-n}$ fill a nonempty open interval about
$S=\sum_{n\ge1}\varphi(n)2^{-n}$ even when $f$ must satisfy all of:

- $f$ is positive and integer-valued, with $f(1)=1$ and
  $f(p^a)=\varphi(p^a)$ at every prime power;
- $f(n)\equiv\varphi(n)\pmod M$ and
  $(1-\varepsilon)\varphi(n)\le f(n)\le(1+\varepsilon)\varphi(n)$ for all
  $n$;
- for every prime $p\le y$, the exact laws
  $f(pn)=(p-1)f(n)$ when $p\nmid n$ and $f(pn)=pf(n)$ when $p\mid n$;
- $\#\{n\le X:f(n)\ne\varphi(n)\}=O(X/\log X)$.

In particular such a function can have a dyadic rational sum. The interval
and the implied constant may depend on $y,M,\varepsilon$; there is no
uniform assertion as $y$ grows. Full multiplicativity is not asserted.

The [proof](_proof.md) makes changes at selected integers with at least two
prime factors above $y$, then propagates each change through multiplication
by integers supported on primes up to $y$. Rounding uses the complete
contribution of each such orbit, including all its multiples.

The result is Plasma AI's, recorded at tier 0 without independent review
or a novelty claim. Its proof is elementary and consumes no native claim.
It neither proves nor disproves
[[problems/irrationality/E0249/_index|the irrationality asked for in
Problem 249]]. The
[[research/totient_binary_new_attack/partial_multiplicativity|research
application]] proves an exponential cost bound for odd kernel vectors
whose cancellation uses only these fixed-prime laws and prime-power
values, on supports of arbitrary length. The distinction between fixed
and growing sets of primes is essential.

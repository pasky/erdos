---
name: research/methods/central_binomial_product_windows
title: Product windows in the central binomial coefficient
desc: |
  A density comparison connects downward products and squared upward
  products; large-prime obstructions explain the missing step in a fixed
  congruence construction and in a density-one specialization.
tags: []
sources: []
problems: [396, 727]
created: 2026-10-14T10:23:26Z
updated: 2026-10-14T10:23:26Z
---

# Product windows in the central binomial coefficient

***

Write $B(n)=\binom{2n}{n}$. Two questions require simultaneous
divisibility by nearby integers:

- [[problems/factorials_binomials/E0396/_index|Problem 396]] asks whether,
  for each fixed $h\ge0$, some $n>h$ has
  $n(n-1)\cdots(n-h)\mid B(n)$.
- [[problems/factorials_binomials/E0727/_index|Problem 727]] asks whether,
  for each fixed $k\ge2$, infinitely many $n$ satisfy
  $(n+k)!^2\mid(2n)!$. This is equivalent to
  $((n+1)\cdots(n+k))^2\mid B(n)$.

The deductions below are author-recorded by Plasma AI. Neither question is
resolved. No novelty is claimed for the elementary valuation observations.

## What the density results transfer

[[theory/number_theory/L23_central_binomial_product_density/_index|L23]]
proves, at tier 0, that for each fixed $k$ the sets

$$
\{n\ge1:((n+1)\cdots(n+k))^2\mid B(n)\}
$$

and

$$
\{n\ge1:(n+1)\cdots(n+k)\mid B(n+k)\}
$$

differ on a set of natural density zero. The second is the translate of
Problem 396's solution set with parameter $k-1$, apart from finitely many
initial values. Hence positive upper density of either set would imply
infinitely many solutions of both questions at those parameters. Mere
infinitude, or a single witness, does not transfer through this comparison.

The exact part of the proof is

$$
B(n+k)=B(n)\frac{2^k\prod_{i=1}^k(2n+2i-1)}
                       {\prod_{i=1}^k(n+i)}.
$$

A prime above $2k$ cannot divide both the numerator's odd product and the
denominator. The two divisibility tests are therefore identical at those
primes. The small-prime conditions hold with density one, by counting
base-$p$ digit strings with few carries. No unproved literature result is
needed for L23's proof.

This extends the scope of the comparison in
[[../library/factorials_binomials/pomerance_2015_divisors_middle_binomial_coefficient/theorem_4|Pomerance's Theorem 4 and its subsequent squared-shift statement]]
from individual factors to a fixed product. That source defines
$D_0=\{m:m\mid B(m)\}$ and gives density-zero comparisons for individual
shifts. Its theorem and subsequent statement were read in the held
transcription; the source gives a sketch for the theorem and omits the
details of the squared-shift extension. The local proof of L23 supplies its
own argument rather than assuming that extension for products.

By contrast,
[[../library/factorials_binomials/pomerance_2015_divisors_middle_binomial_coefficient/theorem_2|Pomerance's positive-shift theorem and product remark]]
concern $(n+1)\cdots(n+k)\mid B(n)$ with the first power. The statement
and proof account were inspected; the product extension is stated without
details in the source. Its density-one conclusion cannot be substituted for
the squared product required by Problem 727.

## A large-prime obstruction on either side

Suppose $n>2k^2$ and $p>\sqrt{2n}$ is prime. Then $p>2k$ and $p^2>2n$,
so Legendre's formula reduces to

$$
v_p(B(n))=\left\lfloor\frac{2n}{p}\right\rfloor
                   -2\left\lfloor\frac{n}{p}\right\rfloor
\in\{0,1\}.                                                   \tag{1}
$$

If $p\mid n-i$ for some $0\le i\le k$, then $n\bmod p=i<p/2$,
and (1) equals zero. Thus the downward product in Problem 396 cannot
divide $B(n)$. This is the obstruction used for a single downward factor
in
[[../library/factorials_binomials/pomerance_2015_divisors_middle_binomial_coefficient/theorem_3|Pomerance's proof of Theorem 3]].
The held transcription's proof and the printed page 642 were inspected for
this use; no assertion about its full density or infinitude proof is needed
here.

If $p\mid n+i$ for some $1\le i\le k$, then $n\bmod p=p-i>p/2$,
and (1) equals one. This still falls short of the two copies of $p$
required by $((n+1)\cdots(n+k))^2$. Consequently a solution of either
problem beyond $2k^2$ requires every integer in its corresponding window
to have no prime factor above $\sqrt{2n}$. This is a necessary condition,
not a sufficient one: all lower prime-power valuations still matter.

## Why finitely many congruences cannot finish a construction

Every residue class contains arbitrarily large failures of each divisibility
condition. Here is a direct construction requiring no theorem on primes in
progressions.

Fix a modulus $M\ge1$ and a residue $a$. For every sufficiently large
prime $p>M$, choose $t\in\{1,\ldots,M\}$ with $tp\equiv a\pmod M$.
Then $n=tp\equiv a\pmod M$, and for $p>2M$ the two base-$p$ digits
of $n$ are $t,0$, both below $p/2$. Hence $v_p(B(n))=0$, while $p\mid n$.
Thus $n(n-1)\cdots(n-h)$ fails to divide $B(n)$ for every fixed $h$
once $n>h$. Since $n\ge p$, these failures are unbounded.

For the upward squared product, choose instead $t\in\{1,\ldots,M\}$
with $tp\equiv a+1\pmod M$ and put $n=tp-1$. For $p>2M$, one has
$p^2>2n$ and $n\bmod p=p-1$, so $v_p(B(n))=1$.
But $p^2\mid(n+1)^2$, which divides the required squared product for
every $k\ge1$. These failures are again unbounded in the given residue
class.

A nonempty finite system of congruences is periodic, so it cannot ensure
either divisibility condition for all sufficiently large integers satisfying
it. This does not rule out a congruence construction followed by an additional
selection, a modulus growing with the desired witness, or a sparse
parametrized family. Any such route still needs an argument controlling
primes not fixed by its congruences.

## The remaining discriminating question

A source theorem giving positive upper density for every fixed downward
window would, through L23, settle Problem 727 as well as strengthen Problem
396. A theorem controlling one factor, or the marginal density of $D_0$,
does not provide those correlations. Positive density alone need not give
consecutive strings of any specified length.

Before extending this route, test whether a proposed source actually controls
the full product at a fixed window length with positive upper density, or
supplies an explicit unbounded family with all prime-power valuations checked.
Stop a proposed specialization when it provides only first powers on the
upward side, marginal one-factor information, or a density-zero comparison
applied to a sparse witness set. Those outcomes leave the central
simultaneous-divisibility step open.

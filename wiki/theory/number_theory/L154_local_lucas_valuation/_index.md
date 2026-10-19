---
name: theory/number_theory/L154_local_lucas_valuation
title: Sharp local polynomial valuation under Lucas domination
desc: When the first quotient digit is at least a polynomial's local multiplicity, full Lucas domination at one prime still permits a column with exactly the initial valuation gain.
id: L154
statement: |
  Let F in Z[X,Y] be nonzero, let 0<=s<=t be integers, and let mu be
  the least total degree in the Taylor expansion of F at (s,t-s),
  with homogeneous part H of degree mu. Let p>t be prime and not
  divide every coefficient of H, and let e>=1 and N>=1 be integers
  with p not dividing N. Put n=t+p^e*N and d=N mod p. For any
  nonnegative integer J whose base-p digits are each at most the
  corresponding digits of N, put
  j=s+p^e*J. Then 0<=j<=n, p does not divide binom(n,j), and
  v_p(F(j,n-j))>=e*mu, with v_p(0)=infinity. Equality holds exactly
  when H(J mod p,d-(J mod p)) is nonzero modulo p. If d>=mu, at
  least one such J gives equality.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T11:42:54Z
updated: 2026-10-15T11:42:54Z
---

# Sharp local polynomial valuation under Lucas domination

[[theory/number_theory/_index|..]]

[[theory/number_theory/L154_local_lucas_valuation/_proof|_proof]]: The leading form stays nonzero on X+Y=d when d is a unit, and its root count supplies a Lucas-admissible next digit with no extra valuation.

***

The [proof](_proof.md), by Plasma AI, is author-recorded at tier 0.
It has no independent review or formalization. It uses Taylor expansion,
the root bound for a polynomial over a field, and the elementary Lucas
criterion for a binomial coefficient to be a unit modulo a prime.

The [[research/erdos_699/remaining/details/index_5_higher_digits|quintic higher-digit test]]
uses this result to delimit a local polynomial approach to
[[problems/factorials_binomials/E0699/_index|Problem 699]]. At a prime
outside the finite set dividing the Taylor form's content, a next digit
$d\ge\mu$ does not by itself force an extra factor $p$. The witnessing
column is only local: the statement requires neither $5<j\le n/2$ nor
simultaneous domination at other active primes. It supplies no infinite
family of bad triples and no uniform obstruction to such triples.

## Verification and remaining obligations

The complete argument is in the proof page. To check it, reduce the
leading Taylor form on the line $X+Y=d$, verify that this polynomial is
nonzero, and count its roots among the allowed next digits. The remaining
digits can all be zero, so the construction is explicit and needs no
computational evidence entry point. No mathematical gap remains in this
local statement; the simultaneous-prime problem remains open in the
linked research.

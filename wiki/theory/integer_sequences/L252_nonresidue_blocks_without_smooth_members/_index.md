---
name: theory/integer_sequences/L252_nonresidue_blocks_without_smooth_members
title: The least quadratic nonresidue of a prime 3 mod 4 bounds k(p) from below
desc: |
  For a prime p = 3 (mod 4) with least quadratic nonresidue q, each of p-q+1,
  ..., p-1 has a prime factor at least q, so k(p) >= q-1 in Problem 962; an
  exponent below 1/(4 sqrt(e)) for k(n) would improve Burgess's bound for
  these primes.
tags: []
sources:
- problems/integer_sequences/E0962
id: L252
statement: |
  Let p be a prime with p = 3 (mod 4), and let q be the least positive
  integer that is a quadratic nonresidue modulo p. Then each of the q-1
  integers p-q+1, ..., p-1 has a prime factor at least q. Consequently
  k(p) >= q-1, where k(n) is the largest integer k for which some integer m
  with 0 <= m <= n has each of m+1, ..., m+k divisible by a prime greater
  than k (the function of Problem 962); the witness m = p-q is positive, so
  the bound holds equally when m is required to be positive.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T22:27:51Z
updated: 2026-10-15T22:27:51Z
---

# The least quadratic nonresidue of a prime 3 mod 4 bounds k(p) from below

[[theory/integer_sequences/_index|..]]

[[theory/integer_sequences/L252_nonresidue_blocks_without_smooth_members/_proof|_proof]]: A term u of the block with all prime factors below q would be a quadratic
residue, and so would p-u, which is below q; then -1 would be a residue,
which fails for p = 3 (mod 4).

***

This result is recorded by Plasma AI as a specialization of an argument that
[[../library/integer_sequences/granville_2008_smooth_numbers_computational_number_theory/_index|Granville]] gives after his Conjecture 4.4.2 (A. Granville, Smooth numbers:
computational number theory and beyond, in Algorithmic Number Theory, MSRI
Publications 44 (2008), 267--323, section 4.4, printed p. 300), where it is
stated for $k$-th power nonresidues and smooth integers in intervals of
length $x^\varepsilon$. It places
[[problems/integer_sequences/E0962/_index|Problem 962, whose upper bounds for k(n) it shows to be at least as hard as bounds for the least quadratic nonresidue]]
next to a classical open problem.

## Meaning of the statement

The block $p-q+1,\ldots,p-1$ has length $q-1$, and every term has a prime
factor greater than $q-1$; so it is a block of the kind Problem 962 counts,
starting at $m=p-q\le p$. Hence an upper bound $k(n)\le An^\theta$, valid for
all large $n$, gives $q\le Ap^\theta+1$ for the least quadratic nonresidue
$q$ of every large prime $p\equiv3\pmod4$.

The classical unconditional bound for the least quadratic nonresidue is
$q\ll_\varepsilon p^{1/(4\sqrt e)+\varepsilon}$, from Burgess's character
sum estimate (D. A. Burgess, Mathematika 4 (1957), 106--112) with
Vinogradov's device; Granville (2008, section 4.4, with the proof in section
6.4) reports it in this form. So a proof of $k(n)\ll n^\theta$ with any
$\theta<1/(4\sqrt e)=0.1516\ldots$ would improve that bound for the primes
$p\equiv3\pmod4$. The displayed question of Problem 962,
$\log k(n)\le(\log n)^{1/2+o(1)}$, would give
$\log q\le(\log p)^{1/2+o(1)}$ for these primes. Under the generalized
Riemann hypothesis $q=O((\log p)^2)$ (N. C. Ankeny, Ann. of Math. 55 (1952),
65--72), so the implication conflicts with no standard conjecture; it
measures difficulty and is not an obstruction to the truth of either
statement. The inequality $k(p)\ge q-1$ alone gives no improvement to the
uniform lower bound for $k(n)$ on the problem page: such an improvement
would require a sufficiently strong lower bound for $q$, not the upper
bound just cited.

## Standing and verification

Tier 0, author-recorded, with a complete elementary
[[theory/integer_sequences/L252_nonresidue_blocks_without_smooth_members/_proof|proof]];
reading it is the verification procedure. Nothing remains open within the
stated scope. The comparison with Burgess's exponent above cites the
literature for context and is not part of the statement.

## Context

The
[[research/smooth_integer_intervals/proof_sketch|research sketch on smooth integers in every short interval]]
uses this statement to separate the exponent waypoints, where
[[theory/integer_sequences/L253_exponent_pair_smooth_blocks/_index|L253 reaches every exponent above 38/97]],
from the regime below $1/(4\sqrt e)$, where an upper bound would also
strengthen that classical estimate for quadratic nonresidues.

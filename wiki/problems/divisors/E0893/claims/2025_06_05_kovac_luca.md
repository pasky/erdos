---
name: problems/divisors/E0893/claims/2025_06_05_kovac_luca
title: "Kovač and Luca: no finite limit for the doubling ratios"
desc: |
  Kovač and Luca prove that the ratios $f(2n)/f(n)$ are unbounded, so they
  converge to no finite limit: a no to the finite-limit variant. Under the
  problem page's reading, which allows the limit $+\infty$, both answers stay
  possible.
authors:
- Vjekoslav Kovač
- Florian Luca
status: accepted
claim: disproved
scope: partial
evidence:
- refereed
submitted: null
links:
- url: https://doi.org/10.1080/10586458.2026.2636060
  kind: paper
  date: 2026-05-20
- url: https://arxiv.org/abs/2506.04883
  kind: preprint
  date: 2025-06-05
- url: https://www.erdosproblems.com/893
  kind: discussion
created: 2026-10-07T20:00:46Z
updated: 2026-10-07T20:00:46Z
---

***

**Claim.** V. Kovač and F. Luca, *On the number of divisors of Mersenne
numbers*, Experimental Mathematics (online 20 May 2026;
[[../library/divisors/kovac_2025_number_divisors_mersenne_numbers/_index|card]]),
Theorem 1 (numbered as in arXiv v4; Corollary 1 in v1):
$\limsup_{n\to\infty}f(2n)/f(n)=\infty$. The proof goes through Proposition 2:
for $f'(n)=\sum_{k\le n}2^{\tau(k)}$, $f'(2n)/f'(n)\to\infty$, proved with
highly composite numbers. Primitive prime divisors give
$\tau(2^k-1)\ge2^{\tau(k)}/4$, so $f\ge f'/4$. Hence $f(2n)/f(n)$ converges to
no real number, which answers [[problems/divisors/E0893/_index|Problem 893]] no
if a finite limit is meant. The problem page's Formulation reads the question
as allowing the limit $+\infty$, and under that reading unboundedness decides
nothing: it leaves exactly two cases, $f(2n)/f(n)\to\infty$, a yes, and no
limit at all, a no.

**Covers.** The finite-limit variant, answered no: every finite limit is
ruled out. The value `disproved` records that negative answer to the variant,
which lies outside the standing; under the Formulation's reading the theorem
does not settle the question, since a ratio tending to infinity would answer
it yes. Whether $f(2n)/f(n)\to\infty$ stays open; the paper's conditional
Theorem 3 is on
[[problems/divisors/E0893/claims/2025_06_05_kovac_luca_conditional|its own page]].

**Depends on.** No page of this wiki.

**Acceptance.** Refereed: Experimental Mathematics. The site credits the result
but labeled the problem OPEN, so its commentary is not acceptance.

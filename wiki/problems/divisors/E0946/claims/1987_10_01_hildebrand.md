---
name: problems/divisors/E0946/claims/1987_10_01_hildebrand
title: Hildebrand's count of equal divisor counts at consecutive integers
desc: |
  Hildebrand proves that $\tau(n)=\tau(n+1)$ for at least $cx/(\log\log x)^3$
  integers $n\le x$, where $c$ is a constant. This answers the question again
  with a far larger count.
authors:
- Adolf Hildebrand
status: accepted
claim: proved
scope: full
evidence:
- refereed
published: 1987-10-01
submitted: null
links:
- url: https://doi.org/10.2140/pjm.1987.129.307
  kind: paper
  date: 1987-10-01
- url: https://www.erdosproblems.com/946
  kind: discussion
  date: 2026-02-02
created: 2026-10-07T21:33:46Z
updated: 2026-10-07T21:33:46Z
---

***

**Claim.** A. Hildebrand, *The divisor function at consecutive integers*,
Pacific J. Math. 129 (1987), no. 2, 307--319, Theorem 1: for all
sufficiently large $x$,

$$
\#\{n\le x:\tau(n)=\tau(n+1)\}\gg x(\log\log x)^{-3},
$$

so the answer to [[problems/divisors/E0946/_index|Problem 946]] is yes. The
proof combines Heath-Brown's method with an idea of Erdős, Pomerance and
Sárközy and a sieve estimate
([[../library/divisors/hildebrand_1987_divisor_function_at_consecutive_integers/_index|card]]).
The issue is nominally dated June 1987; the publisher records publication on
1 October 1987, the date this page carries.

**Depends on.** No page of this wiki (the key lemma is quoted from
Heath-Brown's paper).

**Acceptance.** Refereed: Pacific Journal of Mathematics. erdosproblems.com's
PROVED label credited Heath-Brown, so the erdosproblems.com credit is not
counted as review of this paper.

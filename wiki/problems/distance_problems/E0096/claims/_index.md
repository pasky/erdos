---
name: problems/distance_problems/E0096/claims
desc: The 3 claim pages of Problem 96, one per claimant's result; the problem's standing derives from them.
tags: []
sources: []
created: 2026-10-07T07:56:38Z
updated: 2026-10-11T22:24:14Z
---

# problems/distance_problems/E0096/claims

[[problems/distance_problems/E0096/_index|..]]

[[problems/distance_problems/E0096/claims/2016_05_24_khopkar|2016_05_24_khopkar]]: Theorem 4 of Khopkar's 2016 preprint asserts that a unit distance graph on $n$
points in convex position has $O(n)$ edges. The preprint was never published,
was found incomplete in the discussion, and is contradicted by Kruer and
Kohlmeyer's disproof.

[[problems/distance_problems/E0096/claims/2026_09_10_kruer_kohlmeyer|2026_09_10_kruer_kohlmeyer]]: For every $d\ge2$, Kruer and Kohlmeyer construct $2d^d\,2^{d^{d+1}}$ points in
strictly convex position with at least $d/4$ times as many unit-distance pairs
as points, so the count is not $O(n)$. The result has a Lean proof, certified
by Conjectures.io.

[[problems/distance_problems/E0096/claims/2026_09_13_kruer_kohlmeyer_price|2026_09_13_kruer_kohlmeyer_price]]: A manuscript by Kruer, Kohlmeyer and Price, with a Lean file, constructs for
every large $n$ a set of $n$ points in strictly convex position with at least
$(1/4-o(1))\,n\log\log n$ unit-distance pairs, so the count is not $O(n)$. It
was posted as a proof claim under Problem 97.

***

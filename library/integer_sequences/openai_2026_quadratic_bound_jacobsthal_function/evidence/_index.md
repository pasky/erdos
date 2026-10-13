---
name: integer_sequences/openai_2026_quadratic_bound_jacobsthal_function/evidence
title: Evidence for the release's Jacobsthal bound
desc: |
  Retains the review of the deduction that carries the release's Lean bound
  on Jacobsthal's function to Problem 687's covering function.
created: 2026-10-13T05:29:01Z
updated: 2026-10-13T05:32:28Z
---

# Evidence for the release's Jacobsthal bound

[[integer_sequences/openai_2026_quadratic_bound_jacobsthal_function/_index|..]]

[[integer_sequences/openai_2026_quadratic_bound_jacobsthal_function/evidence/verify/_index|verify/]]: Links the review of 2026-10-12 that carries the release's Lean bound on
Jacobsthal's function to Problem 687's covering function.

***

The
[[integer_sequences/openai_2026_quadratic_bound_jacobsthal_function/evidence/verify/covering_bound_review|filed review]]
checks that the Lean bound $h(k)\le Ck^2$, accepted on Problem 970's claim
page, gives $Y(x)\ll x^2/(\log x)^2$ for Problem 687's covering function. The
step from $h$ to $Y$ is authored, not formalized; the review covers it and
relies on the formal bound as accepted.

This noncomputational deduction needs no executable check. The small brute
force and the sieve figures in the record are consistency checks, not
evidence for the asymptotic statement. Nothing in this folder reviews the
manuscript's prose proof or its result pages.

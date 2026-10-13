---
name: integer_sequences/openai_2026_quadratic_bound_jacobsthal_function/evidence/verify
title: Review of the covering-function deduction
desc: |
  Links the review of 2026-10-12 that carries the release's Lean bound on
  Jacobsthal's function to Problem 687's covering function.
created: 2026-10-13T05:29:01Z
updated: 2026-10-13T05:32:28Z
---

# Review of the covering-function deduction

[[integer_sequences/openai_2026_quadratic_bound_jacobsthal_function/evidence/_index|..]]

[[integer_sequences/openai_2026_quadratic_bound_jacobsthal_function/evidence/verify/covering_bound_review|covering_bound_review]]: Retains Plasma AI's review of 2026-10-12: the accepted Lean bound
h(k) <= Ck^2, with Y(x) = j(P(x)) - 1 and Chebyshev's bound, gives
Y(x) << x^2/(log x)^2, a yes to Problem 687's first displayed question.

***

The
[[integer_sequences/openai_2026_quadratic_bound_jacobsthal_function/evidence/verify/covering_bound_review|review of Y(x) = o(x^2)]]
retains Plasma AI's check of the deduction from the Lean declaration
`erdos_970_quadratic`, accepted on Problem 970's claim page, through display
(1.3) of Ford, Green, Konyagin, Maynard and Tao, the count
$\omega(P(x))=\pi(x)$ and Chebyshev's bound, to $Y(x)\ll x^2/(\log x)^2$ for
[[../wiki/problems/integer_sequences/E0687/_index|Problem 687]]. It does not
review the manuscript's prose proof, its Theorem 1.2 or the declaration
`erdos_970_iterated_log`, and it confers no numerical tier.

Edits to the filed record: on 2026-10-13 the record was filed with the
report's private working paths replaced by plain descriptions; no repository
path, scope, date or verdict changed.

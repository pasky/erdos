---
name: problems/factorials_binomials/E0684/claims
desc: The 3 claim pages of Problem 684, one per claimant's result; the problem's standing derives from them.
tags: []
sources: []
created: 2026-10-07T07:37:55Z
updated: 2026-10-11T22:24:14Z
---

# problems/factorials_binomials/E0684/claims

[[problems/factorials_binomials/E0684/_index|..]]

[[problems/factorials_binomials/E0684/claims/2026_01_19_tang|2026_01_19_tang]]: Theorem 1.2 of the note by Quanyu Tang and ChatGPT-5.2 Thinking gives
$f(n)\le\lceil n^{12/17+\varepsilon}\rceil$ for large $n$, and the thread
states the exponent $30/43$ through Guth and Maynard. Both are superseded by
the $(\log n)^2$ bound.

[[problems/factorials_binomials/E0684/claims/2026_03_31_alexeev_putterman_sawhney_sellke_valiant|2026_03_31_alexeev_putterman_sawhney_sellke_valiant]]: Theorem 2.1 of Alexeev, Putterman, Sawhney, Sellke and Valiant (arXiv 2026,
unrefereed) gives $f(n)\le(24/(\pi^2-6)+o(1))(\log n)^2$ for large $n$ and
$f(n)\ge(1/2+o(1))\log n$ along a sequence. The order of $f(n)$ stays open.

[[problems/factorials_binomials/E0684/claims/2026_09_03_bae|2026_09_03_bae]]: Ji Ho Bae's arXiv preprint, which comes with a Lean 4 proof, shows that
$f(n)>(1/2-o(1))\log n\,\log\log n/\log\log\log n$ infinitely often, so
$f(n)=O(\log n)$ fails. The order of $f(n)$ stays open between that bound and
$(\log n)^2$.

***

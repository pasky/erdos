---
name: research/arithmetic_construction_interfaces/factorial_divisor_cutoff
title: A finite test for a fixed factorial divisor
desc: The least prime factor bounds the factorial indices for a fixed composite divisor of a factorial plus one, without giving a subpower count of such divisors.
created: 2026-10-14T23:45:12Z
updated: 2026-10-14T23:45:12Z
---

# A finite test for a fixed factorial divisor

***

For a fixed composite $u$, the existential factorial test in
[[problems/integer_sequences/E1073/_index|Problem 1073]] is finite. If
$p$ is its least prime factor and $n\ge p$, then $p\mid n!$ and
$n!+1\equiv1\pmod p$, contradicting $u\mid n!+1$. It therefore suffices
to test $0\le n<p$ for that $u$. This elementary reduction is
author-recorded by Plasma AI and uses no numerical computation.

The reduction does not bound the number of successful moduli $u<x$ by
$x^{o(1)}$: the moduli remain unbounded and a finite decision for each
modulus is not a counting estimate. Hardy and Subbarao's
[[../library/integer_sequences/hardy_2002_modified_problem_pillai_related_questions/problem_f|Problem F]]
states the counting question. A route based on factorial residues still
needs a uniform estimate for their composite divisors; no such estimate is
established by this observation.

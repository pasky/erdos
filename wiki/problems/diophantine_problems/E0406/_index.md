---
name: problems/diophantine_problems/E0406
title: Problem 406
desc: |
  Asks whether only finitely many powers of $2$ use only the digits $0$ and $1$
  in base $3$.
tags:
- Number theory
- Base representations
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 406

[[problems/diophantine_problems/_index|..]]

***

**Statement.** Is it true that there are only finitely many powers of $2$ which
have only the digits $0$ and $1$ when written in base $3$?

**Status.** Open.

**Source.** [erdosproblems.com/406](https://www.erdosproblems.com/406), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #406,
https://www.erdosproblems.com/406.

**References.**

- [AbLa14] Abram, William C. and Lagarias, Jeffrey C., Intersections of
  multiplicative translates of 3-adic Cantor sets. J. Fractal Geom. 1 (2014),
  no. 4, 349-390; doi:10.4171/JFG/11.
- [Gu04] Guy, Richard K., Unsolved problems in number theory. 3rd ed., Problem
  Books in Mathematics, Springer, New York (2004), xviii+437 pp. Section B33
  "Largest divisor of a binomial coefficient", printed p. 135: "Erdős has also
  conjectured that for $k>8$, $2^k$ is not the sum of distinct powers of 3
  [$2^8=3^5+3^2+3+1$]", a stronger form of the page's question (no such power
  beyond $2^8$, where the page asks only for finitely many), stated for its
  consequence that $3\mid\binom{2^{k+1}}{2^k}$ for $k\ge9$. Library home:
  [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]].
- [La09] Lagarias, Jeffrey C., Ternary expansions of powers of 2. J. Lond. Math.
  Soc. (2) (2009), 562-588.
- [Na80] Narkiewicz, W., A note on a paper of H. Gupta concerning powers of two
  and three: ``Powers of $2$\ and sums of distinct powers of $3$''\ [Univ.
  Beograd. Publ. Elektrotehn. Fak. Ser. Mat. Fiz. No. 602-633 (1978), 151-158
  (1979);\ MR 81g:10016]. Univ. Beograd. Publ. Elektrotehn. Fak. Ser. Mat. Fiz.
  (1980), 173-174.
- [Sa22] Saye, Robert I., On two conjectures concerning the ternary digits of
  powers of two. J. Integer Seq. (2022), Art. 22.3.4, 9.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/406.lean).

## Current assessment

The counting bounds and exceptional-set dimension statements in
[[../library/diophantine_problems/lagarias_2009_ternary_expansions_powers_2/_index|Lagarias's
Theorems 1.1–1.4]] do not prove finiteness at multiplier one.
[[../library/diophantine_problems/saye_2022_two_conjectures_concerning_ternary_digits_powers/_index|Saye]]
reports that through exponent $2\cdot3^{45}$ the only examples are $0,2,8$.
That finite computation has not been replayed.

A fixed-depth digit sieve has an exact obstruction. The order of two modulo
$3^k$ is $2\cdot3^{k-1}$: starting with order two modulo three, cubing a number
$1+c3^k$ with $3\nmid c$ raises the exact valuation of its difference from one
by one. Powers of two therefore enumerate all units modulo $3^k$. Exactly
$2^{k-1}$ of these units have only zero and one in their lowest $k$ ternary
digits: the last digit is one and each higher digit has two choices. Thus that
many exponent residue classes survive at every fixed depth, each with
arbitrarily large members.

This author-recorded argument does not obstruct a sieve whose depth grows with
the exponent. Such a growing-depth estimate, or a theorem excluding the
specified multiplier from the exceptional set, remains necessary. The source
statements and order-lifting argument were inspected, not the full source
proofs.

## Known Results

Not yet compiled.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/diophantine_problems/abram_2014_intersections_multiplicative_translates_3_adic_cantor/_index|abram_2014_intersections_multiplicative_translates_3_adic_cantor]]
- [[../library/diophantine_problems/abram_2014_intersections_multiplicative_translates_3_adic_cantor/conjecture_1_2|abram_2014_intersections_multiplicative_translates_3_adic_cantor / conjecture_1_2]]
- [[../library/diophantine_problems/abram_2014_intersections_multiplicative_translates_3_adic_cantor/theorem_1_6|abram_2014_intersections_multiplicative_translates_3_adic_cantor / theorem_1_6]]
- [[../library/diophantine_problems/abram_2014_intersections_multiplicative_translates_3_adic_cantor/theorem_1_8|abram_2014_intersections_multiplicative_translates_3_adic_cantor / theorem_1_8]]
- [[../library/diophantine_problems/abram_2014_intersections_multiplicative_translates_3_adic_cantor/theorem_1_9|abram_2014_intersections_multiplicative_translates_3_adic_cantor / theorem_1_9]]
- [[../library/diophantine_problems/abram_2014_intersections_multiplicative_translates_3_adic_cantor/theorem_5_2|abram_2014_intersections_multiplicative_translates_3_adic_cantor / theorem_5_2]]
- [[../library/diophantine_problems/lagarias_2009_ternary_expansions_powers_2/_index|lagarias_2009_ternary_expansions_powers_2]]
- [[../library/diophantine_problems/lagarias_2009_ternary_expansions_powers_2/theorem_1_1|lagarias_2009_ternary_expansions_powers_2 / theorem_1_1]]
- [[../library/diophantine_problems/lagarias_2009_ternary_expansions_powers_2/theorem_1_2|lagarias_2009_ternary_expansions_powers_2 / theorem_1_2]]
- [[../library/diophantine_problems/lagarias_2009_ternary_expansions_powers_2/theorem_1_3|lagarias_2009_ternary_expansions_powers_2 / theorem_1_3]]
- [[../library/diophantine_problems/lagarias_2009_ternary_expansions_powers_2/theorem_1_4|lagarias_2009_ternary_expansions_powers_2 / theorem_1_4]]
- [[../library/diophantine_problems/lagarias_2009_ternary_expansions_powers_2/theorem_1_5|lagarias_2009_ternary_expansions_powers_2 / theorem_1_5]]
- [[../library/diophantine_problems/lagarias_2009_ternary_expansions_powers_2/theorem_1_6|lagarias_2009_ternary_expansions_powers_2 / theorem_1_6]]
- [[../library/diophantine_problems/lagarias_2009_ternary_expansions_powers_2/theorem_1_7|lagarias_2009_ternary_expansions_powers_2 / theorem_1_7]]
- [[../library/diophantine_problems/saye_2022_two_conjectures_concerning_ternary_digits_powers/_index|saye_2022_two_conjectures_concerning_ternary_digits_powers]]
- [[../library/diophantine_problems/saye_2022_two_conjectures_concerning_ternary_digits_powers/lemma_1|saye_2022_two_conjectures_concerning_ternary_digits_powers / lemma_1]]
- [[../library/diophantine_problems/saye_2022_two_conjectures_concerning_ternary_digits_powers/main_theorem|saye_2022_two_conjectures_concerning_ternary_digits_powers / main_theorem]]
- [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]]

<!-- END problem library links -->

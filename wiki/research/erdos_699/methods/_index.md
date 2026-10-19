---
name: research/erdos_699/methods
title: "Tools used in the P699 proofs"
desc: "A short guide to the divisibility, approximation, nonvanishing, and finite-range arguments used in the current proofs."
created: 2026-09-22T19:09:27Z
updated: 2026-09-22T19:12:28Z
---

# Tools used in the P699 proofs

[[research/erdos_699/_index|..]]

[[research/erdos_699/methods/details/_index|details/]]: The divisibility, approximation, prime estimates, and nonvanishing lemmas behind the P699 arguments.

***

The [proof guide](../proofs/_index.md) explains how these ingredients fit
together. This page is for a reader who wants the general mathematical
statements before the individual index certificates.

1. **Divisibility and the actual column.** The
   [localization lemma](details/gcd_localization.md)
   turns vanishing on the triangular grid into an exact divisor of
   a polynomial evaluated at $(j,n-j)$. It retains the common small-prime
   valuations of the two binomial coefficients. The
   [weighted polynomial argument](details/weighted_ramps.md)
   explains why different multiplicities on different rows help.
2. **Effective cofactor bounds.** The
   [unequal Padé block construction](details/off_diagonal_pade.md)
   and [block adjustment lemma](details/pade_block_adjustment.md)
   provide the approximation inequalities used at seven and nine.
   The [coefficient-gcd lemma](details/prime_power_gcd.md)
   supplies their prime-power divisibility; each construction links the
   explicit analytic estimates needed to make it numerical.
3. **Nonvanishing.** The
   [interpolation lemma](details/jet_nonvanishing.md)
   gives a family of polynomials that cannot all vanish at an admissible
   pair. The [coprime-polynomial argument](details/coprime_kernels.md)
   is another effective way to control common zeros. The smallest
   completed cases also use the arithmetic arguments linked in their proofs.
4. **Covering a bounded range.** The
   [prime-power strip argument](details/prime_power_strips.md)
   bounds cofactors throughout whole regions of exponents and retains the
   exceptional solutions. Those estimates feed the interval proofs.
5. **A possible tool for the remaining cases.** The
   [Runge criterion](details/runge_curve_criterion.md)
   gives effective finiteness on a fixed curve when enough finite fibers
   supply poles. It does not put all bad pairs on finitely many curves.

The [supporting statements](details/_index.md) retain the additional
estimates and exact constants used by these arguments. They are reference
material, rather than a second required reading list.

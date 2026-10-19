---
name: number_theory/bourgain_2017_decoupling_exponential_sums_riemann_zeta/theorem_6
title: Bourgain's exponent pair
desc: Theorem 6 of arXiv 1408.5794v2 gives the exponent pair with coordinates 13/84 plus epsilon and 55/84 plus epsilon, under the usual smooth-phase convention.
created: 2026-10-15T23:41:00Z
updated: 2026-10-15T23:41:00Z
---

# Bourgain's exponent pair

***

**Source.** [[number_theory/bourgain_2017_decoupling_exponential_sums_riemann_zeta/_index|Bourgain]],
*Decoupling, exponential sums and the Riemann zeta function*,
arXiv:1408.5794v2, Section 5, Theorem 6.

For every $\varepsilon>0$,

$$
\left(\frac{13}{84}+\varepsilon,\frac{55}{84}+\varepsilon\right)
$$

is an exponent pair in the standard smooth-phase sense. With the source's
phase scale $T$ and summation scale $M$, the corresponding bound has the form

$$
|S|\ll (T/M)^{13/84+\varepsilon}M^{55/84+\varepsilon}
       =M^{1/2}T^{13/84+\varepsilon}.
$$

This statement is restricted to the phase class required by exponent-pair
theory. Section 5 invokes Graham–Kolesnik, Chapter 3, including Condition
(3.3.3), for that class and its derivative conditions. It treats both
$M>\sqrt T$ and summation over a proper subinterval: the former through the
$B$-process and extreme-range estimates, the latter by a derivative-controlled
extension and a logarithmic completion loss absorbed in $\varepsilon$.
The estimate is not asserted for arbitrary smooth functions of that scale.

**Read status: claims checked.** The statement, preceding bound (5.1),
and the complete Section 5 discussion were read in the v2 TeX source.
The reduction was read for structure; the source's preceding estimates and
the original Graham–Kolesnik and Sargos arguments remain unread proof
premises. No independent verification of Theorem 6 is recorded here.

**Application boundary.** For
[[../wiki/problems/integer_sequences/E0962/_index|Problem 962]], a
smooth-interval argument using this pair must verify its normalized phase
against those conditions, with constants uniform over its starting intervals.

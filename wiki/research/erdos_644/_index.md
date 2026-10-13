---
name: research/erdos_644
title: Seven-edge transversal bounds
desc: "Source notes on seven-edge transversal bounds; both unrestricted assertions remain open."
tags: []
sources: []
created: 2026-09-22T20:01:25Z
updated: 2026-10-08T13:55:35Z
---

# Seven-edge transversal bounds

[[research/_index|..]]

[[research/erdos_644/source_notes/_index|source_notes/]]: Paper summaries and source comparisons used in the research on Problem 644.

***

## Where things stand

**Neither assertion of [Problem 644](../../problems/set_systems/E0644/_index.md) has
been resolved.** In the asymptotic range the bounds are

$$
3\lfloor k/4\rfloor+1\le f(k,7)\le\lceil7k/8\rceil\qquad(k\ge40),
$$

so $f(k,7)\ge(3/4-o(1))k$. The bounds are due to
[Fon-der-Flaass, Kostochka, and Woodall](source_notes/fon_der_flaass_et_al_1999_transversals_uniform_hypergraphs_property_7_2.md):
their Theorem 2 gives the upper bound for every $k\ge8$, and their Theorem 1
gives the lower bound only at multiples of four, $f(4q,7)\ge3q+1$ for
$q\ge10$. It reaches every $k\ge40$ because $f(k,7)$ is nondecreasing in $k$:
adding to each set a new point of its own keeps the seven-set hypothesis and
does not lower the transversal number. At $k\equiv2,3\pmod4$ this gives less
than $\lceil3k/4\rceil$, which is not known to be a lower bound for every $k$.
No fixed-positive-excess counterexample or unrestricted convergence theorem
is known.

## Source caution

The supplied 1997 transcription's floor roundings for both $r=4$ and $r=5$
conflict with nonvacuous examples: all triples on seven points have $P_4$ and
transversal number five, while all triples on six points have $P_5$ and
transversal number four. These bounded discrepancies do not challenge the
reported asymptotic coefficients; no argument here relies on the disputed exact
formulas.

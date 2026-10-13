---
name: problems/arithmetic_functions/E0928
title: Problem 928
desc: |
  Asks whether the integers $n$ with $P(n)<n^{\alpha}$ and
  $P(n+1)<(n+1)^{\beta}$ have a density, where $P$ is the largest prime factor.
  The OpenAI release of September 2026 shows the density is a Dickman product;
  this is accepted because its Lean proof was built.
tags:
- Number theory
status: solved
claim: proved
created: 2026-09-04T09:17:27Z
updated: 2026-10-08T13:36:40Z
---

# Problem 928

[[problems/arithmetic_functions/_index|..]]

[[problems/arithmetic_functions/E0928/claims/_index|claims/]]: The 2 claim pages of Problem 928, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $\alpha,\beta\in (0,1)$ and let $P(n)$ denote the largest
prime divisor of $n$. Does the density of integers $n$ such that
$P(n)<n^{\alpha}$ and $P(n+1)<(n+1)^\beta$ exist?

**Formulation.** The set with $P(n)\le n^{\alpha}$ and $P(n+1)\le n^{\beta}$
in place of the strict inequalities and the threshold $(n+1)^{\beta}$ differs
from the problem's set, up to $X$, by at most
$\pi(X^{\alpha})+\pi((X+1)^{\beta})$ integers, so a density statement for
either set holds for the other; the claim page below states the bridge, which
is elementary and not in Lean.

**Status.** Proved here. The site labeled the problem OPEN (page last edited 3
April 2026). The OpenAI release of September 2026 claims that the density exists
and equals $\rho(1/\alpha)\rho(1/\beta)$, where $\rho$ is Dickman's function.
This is the independence Erdős asked for. The release proves the theorem in
Lean. This corpus built that Lean with only the three standard axioms, and its
fingerprint is identical to the release's comparator challenge. The statement
audit found it exact, and the elementary bridge to the Statement's strict
inequalities is stated on the claim page. So the claim is accepted on
[[problems/arithmetic_functions/E0928/claims/2026_09_24_openai|OpenAI 2026]],
and the problem stands solved. No outside review is known.

Wang [Wa21] proved the density under the Elliott–Halberstam conjecture for
friable integers. This is an accepted conditional claim,
[[problems/arithmetic_functions/E0928/claims/2021_01_20_wang|Wang 2021]], and it
settles no standing. Teräväinen [Te18] proved the product law in logarithmic
density. Tao and Teräväinen (Algebra Number Theory 13 (2019), Remark 3.3) proved
it for ordinary averages outside an exceptional set of scales of logarithmic
density zero. Neither result settles an instance of the natural-density
question, so neither has a claim page. The site's commentary also records
Erdős's further question whether infinitely many such $n$ exist. Meza observed
that this follows from Schinzel's theorem [Sc67b] that
$P(n(n+1))\le n^{O(1/\log\log n)}$ for infinitely many $n$. That answers a side
question and settles no instance of the density question, so it has no claim
page.

**Source.** [erdosproblems.com/928](https://www.erdosproblems.com/928), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #928,
https://www.erdosproblems.com/928.

**References.**

- [Di30] K. Dickman, On the frequency of numbers containing prime factors of a
  certain relative magnitude. Ark. Mat. Astr. Fys. (1930), 1-14.
- [Er76e] Erdős, P., Problems and results on consecutive integers. Publ. Math.
  Debrecen (1976), 271-282.
- [Sc67b] Schinzel, A., On two theorems of Gelfond and some of their
  applications. Acta Arith. (1967/68), 177-236.
- [Te18] Teräväinen, Joni, On binary correlations of multiplicative functions.
  Forum Math. Sigma (2018), Paper No. e10, 41.
- [Wa21] Wang, Zhiwei, Three conjectures on $P^+(n)$ and $P^+(n+1)$ hold under
  the Elliott-Halberstam conjecture for friable integers. J. Number Theory
  (2021), 1-11.

**Formalization.** No statement in formal-conjectures is recorded. The release
proves its theorem in Lean (`OAI.JointDickmanPaper.joint_law`), pinned by its
comparator challenge and linked from the claim page; this corpus built it from
the pinned revision with the axioms `propext`, `Classical.choice` and
`Quot.sound` only. The bridge from the theorem's thresholds to the Statement's
is stated on the claim page, not in Lean.

## Progress

Not yet compiled.

## Known Results

Not yet compiled.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/arithmetic_functions/openai_2026_joint_dickman_law_consecutive_integers/_index|openai_2026_joint_dickman_law_consecutive_integers]]
- [[../library/arithmetic_functions/openai_2026_joint_dickman_law_consecutive_integers/theorem_1_1|openai_2026_joint_dickman_law_consecutive_integers / theorem_1_1]]
- [[../library/arithmetic_functions/schinzel_nd_two_theorems_gelfond_applications/_index|schinzel_nd_two_theorems_gelfond_applications]]
- [[../library/arithmetic_functions/teravainen_2018_binary_correlations_multiplicative_functions/_index|teravainen_2018_binary_correlations_multiplicative_functions]]
- [[../library/arithmetic_functions/teravainen_2018_binary_correlations_multiplicative_functions/theorem_1_11|teravainen_2018_binary_correlations_multiplicative_functions / theorem_1_11]]
- [[../library/arithmetic_functions/teravainen_2018_binary_correlations_multiplicative_functions/theorem_1_14|teravainen_2018_binary_correlations_multiplicative_functions / theorem_1_14]]
- [[../library/arithmetic_functions/teravainen_2018_binary_correlations_multiplicative_functions/theorem_1_19|teravainen_2018_binary_correlations_multiplicative_functions / theorem_1_19]]

<!-- END problem library links -->

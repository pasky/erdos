---
name: problems/arithmetic_functions/E0050
title: Problem 50
desc: |
  Asks whether the density $f(c)$ of the integers $n$ with $\phi(n)<cn$, as a
  function of $c$, ever has a positive derivative.
tags:
- Number theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 50

[[problems/arithmetic_functions/_index|..]]

***

**Statement.** Schoenberg proved that for every $c\in [0,1]$ the density of

$$
\{ n\in \mathbb{N} : \phi(n)<cn\}
$$

exists. Let this density be denoted by $f(c)$. Is it true that there are no $x$
such that $f'(x)$ exists and is positive?

**Status.** Open.

**Source.** [erdosproblems.com/50](https://www.erdosproblems.com/50), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #50,
https://www.erdosproblems.com/50.

**References.**

- [Er95] Erdős, Paul, Some of my favourite problems in number theory,
  combinatorics, and geometry. Resenhas (1995), 165-186.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/50.lean).

## Current assessment

The held
[[../library/arithmetic_functions/erdos_1974_distribution_numbers_form_sigma_n_n/question_p59|singularity account]]
gives derivative zero almost everywhere, which leaves exceptional points.
The same paper's
[[../library/arithmetic_functions/erdos_1974_distribution_numbers_form_sigma_n_n/theorem_p60|logarithmic modulus estimate]]
is proved for $\sigma(n)/n$ and asserted without proof for $\phi(n)/n$.
Even that asserted analogue permits linear increments and hence does not
exclude a positive derivative. This assessment concerns those precise
implications; it is not a complete current-literature or formalization
audit.

The following author-recorded countermodel of Plasma AI shows why
singularity alone is insufficient. For each $j\ge1$, place a continuous
singular measure of total mass $|I_j|/2$ inside
$I_j=(1/(j+1),1/j]$, and reflect it across zero. Such a measure can be
obtained by an affine copy of the usual Cantor probability measure on a
closed subinterval of $I_j$. The resulting measure has total mass one,
no atoms, and is supported on a countable union of null sets. Its
continuous distribution function $G$ is therefore singular.

If $t\in I_j$, the total mass on $(0,1/(j+1)]$ is $1/(2(j+1))$.
The remaining mass before $t$ lies between zero and $|I_j|/2$, so

$$
\left|G(t)-G(0)-\frac t2\right|
\le\frac{|I_j|}{2}=O(t^2).
$$

Reflection gives the same estimate for negative $t$, hence $G'(0)=1/2$.
An affine change of variable places the example inside $[0,1]$, with a
positive derivative at an interior point. This is a countermodel to the
general implication from singularity, not to the assertion about the
totient distribution, and has not been independently reviewed. The
arithmetic problem needs local two-sided control at every exceptional
point of its particular distribution.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/arithmetic_functions/erdos_1974_distribution_numbers_form_sigma_n_n/_index|erdos_1974_distribution_numbers_form_sigma_n_n]]
- [[../library/arithmetic_functions/erdos_1974_distribution_numbers_form_sigma_n_n/question_p59|erdos_1974_distribution_numbers_form_sigma_n_n / question_p59]]
- [[../library/arithmetic_functions/erdos_1974_distribution_numbers_form_sigma_n_n/theorem_p60|erdos_1974_distribution_numbers_form_sigma_n_n / theorem_p60]]
- [[../library/number_theory/erdos_1995_my_favourite_problems_number_theory_combinatorics/_index|erdos_1995_my_favourite_problems_number_theory_combinatorics]]

<!-- END problem library links -->

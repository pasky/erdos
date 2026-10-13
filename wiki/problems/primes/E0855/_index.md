---
name: problems/primes/E0855
title: Problem 855
desc: |
  Asks whether the prime-counting function satisfies $\pi(x+y)\le\pi(x)+\pi(y)$
  for all large $x$ and $y$.
tags:
- Number theory
- Primes
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-13T13:29:21Z
---

# Problem 855

[[problems/primes/_index|..]]

[[problems/primes/E0855/claims/_index|claims/]]: The 5 claim pages of Problem 855, one per claimant's result; the problem's standing derives from them.

***

**Statement.** If $\pi(x)$ counts the number of primes in $[1,x]$ then is it
true that (for large $x$ and $y$)

$$
\pi(x+y) \leq \pi(x)+\pi(y)?
$$

**Status.** Open.

**Source.** [erdosproblems.com/855](https://www.erdosproblems.com/855), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #855,
https://www.erdosproblems.com/855.

**References.**

- [ClJa01] Clark, David A. and Jarvis, Norman C., Dense admissible sequences.
  Math. Comp. (2001), 1713-1718.
- [Er80] Erdős, Paul, A survey of problems in combinatorial number theory. Ann.
  Discrete Math. (1980), 89-115.
- [Er85c] Erdős, P., On some of my problems in number theory I would most like
  to see solved. Number theory (Ootacamund, 1984) (1985), 74-84.
- [Gu04] Guy, Richard K., Unsolved problems in number theory. Third edition,
  Problem Books in Mathematics, Springer (2004), xviii+437 pp. Section A9
  "Patterns of primes", printed p. 40: the prime-pattern conjecture is
  "incompatible with the well-known conjecture (also due to Hardy &
  Littlewood)" that
  $\pi(x+y)\le\pi(x)+\pi(y)$ for all integers $x,y\ge2$, a display Guy sets
  between inverted and upright question marks because it "is very likely to
  be false", with the Montgomery--Vaughan bound. Library home:
  [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]].
- [HeRi73] Hensley, Douglas and Richards, Ian, On the incompatibility of two
  conjectures concerning primes. (1973), 123-127.
- [MoVa73] Montgomery, H. L. and Vaughan, R. C., The large sieve. Mathematika
  (1973), 119-134.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/855.lean).

## Current assessment

The standing above derives from the claim pages below, and the site's label
was also OPEN. The notes below are not independently reviewed. Their scope is
the sources the library holds on the inequality; the page records no
systematic literature search beyond them, and no independent assessment of
proof coverage.

The inequality is proved on every region in which the smaller entry $u$ of
the pair is not too small against the larger entry $v$. Dusart's refereed
Theorem 1 covers $v\le\frac75u\log u\log\log u$
([[problems/primes/E0855/claims/2002_01_01_dusart|accepted partial claim]];
[[../library/primes/dusart_2002_sur_la_conjecture_pi_x_y_pi_x_pi_y/_index|card]]).
Alkan's refereed Theorem 1 gives the strict inequality for $u,v\ge x_0$ and
$u\ge Kv/\log v$, a region inside Dusart's for large pairs
([[problems/primes/E0855/claims/2022_06_03_alkan|accepted partial claim]];
[[../library/primes/alkan_2022_generalization_hardy_littlewood_conjecture/_index|card]]).
Axler's preprint claims $u\ge c_0v/\log^2v$ with $c_0=0.7088\ldots$
([[../library/primes/axler_2019_some_results_conjecture_hardy_littlewood/theorem_1_3|Theorem 1.3]];
[[problems/primes/E0855/claims/2019_09_27_axler|pending partial claim]]).
The widest unconditional range is that of Chahal, Elma, Fellini, Vatwani and
Vo, refereed in Acta Arithmetica: $u\ge3CR(2v)\log^2v/\log\log v$ for large
$v$, where $CR$ bounds the error in the prime number theorem, so that the
lower end is $v$ times a factor tending to zero faster than any power of
$1/\log v$
([[../library/primes/chahal_et_al_2025_second_hardy_littlewood_conjecture/theorem_1_1|Theorem 1.1]];
[[problems/primes/E0855/claims/2025_03_04_chahal_elma_fellini_vatwani_vo|accepted partial claim]]).
Under the Riemann hypothesis their
[[../library/primes/chahal_et_al_2025_second_hardy_littlewood_conjecture/corollary_1_2|Corollary 1.2]]
reaches $u\ge(2+\epsilon)\sqrt v\log^2v/(8\pi)$, and Axler's
[[../library/primes/axler_2019_some_results_conjecture_hardy_littlewood/theorem_1_5|Theorem 1.5]]
a range of the same order. Every one of these ranges has a lower end that
grows with $v$, so none covers, for instance, the pairs with
$u=\lfloor\sqrt v\rfloor$, even under the Riemann hypothesis, and the
problem stays open. The same papers show that failures have density zero
among pairs of entries at most $X$ (Dusart's Proposition 4, Alkan's
Corollary 1,
[[../library/primes/chahal_et_al_2025_second_hardy_littlewood_conjecture/corollary_1_5|Chahal et al.'s Corollary 1.5]]);
a density-zero set may still hold infinitely many large pairs, so this
decides nothing.

Finite checks rule out small counterexamples only. Segal's
[[../library/primes/segal_1962_x_y_x_y/theorem_i|Theorem I]] (Trans. Amer.
Math. Soc. 104 (1962)) shows that the inequality for all $x,y\ge2$ is
equivalent to $p_n\ge p_{n-q}+p_{q+1}-1$ for $n\ge3$ and
$1\le q\le(n-1)/2$; his
[[../library/primes/segal_1962_x_y_x_y/theorem_ii|Theorem II]] places the
least failing sum at the least prime failing that inequality, and his machine
check gives the inequality whenever $x+y\le101{,}081$.
[[../library/primes/segal_1962_x_y_x_y/lemma_iv|Lemma IV]] turns a prime in a
certain window into an explicit violating pair. Axler's
[[../library/primes/axler_2019_some_results_conjecture_hardy_littlewood/proposition_2_4|Proposition 2.4]]
extends the check to $x+y\le39\,708\,229\,123$. A finite check says
nothing about large $x$ and $y$, so these get no claim pages.

Hensley and Richards proved in Acta Arithmetica that the prime $k$-tuples
conjecture is incompatible with the inequality: under that conjecture, for
every large $x$ there are infinitely many $y$ with
$\pi(x+y)>\pi(x)+\pi(y)$. The result is recorded on
[[problems/primes/E0855/claims/1973_01_01_hensley_richards|their conditional claim page]];
it settles nothing unconditionally, since the $k$-tuples conjecture is
unproved.

No claim page records the three manuscripts of the OpenAI mathematics
release that the library links here, the zero-free half-planes
$\operatorname{Re}s>7/8$ and $\operatorname{Re}s>11/12$ for every Dirichlet
$L$-function
([[../library/primes/openai_2026_quasi_riemann_hypothesis_zero_free_half_plane_7_8/_index|card]],
[[../library/primes/openai_2026_quasi_riemann_hypothesis_zero_free_half_plane_11_12/_index|card]])
and the uniform exclusion of Landau--Siegel zeros
([[../library/primes/openai_2026_uniform_exclusion_landau_siegel_zeros/_index|card]]):
none of them names this problem or claims anything about
$\pi(x+y)\le\pi(x)+\pi(y)$. Their only bearing is on the hypothesis of
Granville's conditional interval constructions, recorded on
[[../library/integer_sequences/granville_2020_sieving_intervals_siegel_zeros/_index|the source card]],
which assume infinitely many Siegel zeros; if the release's claims stand,
those constructions have a false hypothesis, and the inequality itself is
untouched either way. The claims are unverified here.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/additive_combinatorics/erdos_1957_unsolved_problems/_index|erdos_1957_unsolved_problems]]
- [[../library/additive_combinatorics/erdos_1957_unsolved_problems/problem_1|erdos_1957_unsolved_problems / problem_1]]
- [[../library/integer_sequences/granville_2020_sieving_intervals_siegel_zeros/_index|granville_2020_sieving_intervals_siegel_zeros]]
- [[../library/integer_sequences/granville_2020_sieving_intervals_siegel_zeros/corollary_3|granville_2020_sieving_intervals_siegel_zeros / corollary_3]]
- [[../library/integer_sequences/konyagin_2022_construction_schinzel_many_numbers_short_interval_without_small_prime_factors/_index|konyagin_2022_construction_schinzel_many_numbers_short_interval_without_small_prime_factors]]
- [[../library/integer_sequences/konyagin_2022_construction_schinzel_many_numbers_short_interval_without_small_prime_factors/corollary_1|konyagin_2022_construction_schinzel_many_numbers_short_interval_without_small_prime_factors / corollary_1]]
- [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]]
- [[../library/primes/alkan_2022_generalization_hardy_littlewood_conjecture/_index|alkan_2022_generalization_hardy_littlewood_conjecture]]
- [[../library/primes/axler_2019_some_results_conjecture_hardy_littlewood/_index|axler_2019_some_results_conjecture_hardy_littlewood]]
- [[../library/primes/axler_2019_some_results_conjecture_hardy_littlewood/proposition_2_4|axler_2019_some_results_conjecture_hardy_littlewood / proposition_2_4]]
- [[../library/primes/axler_2019_some_results_conjecture_hardy_littlewood/proposition_5_1|axler_2019_some_results_conjecture_hardy_littlewood / proposition_5_1]]
- [[../library/primes/axler_2019_some_results_conjecture_hardy_littlewood/theorem_1_1|axler_2019_some_results_conjecture_hardy_littlewood / theorem_1_1]]
- [[../library/primes/axler_2019_some_results_conjecture_hardy_littlewood/theorem_1_2|axler_2019_some_results_conjecture_hardy_littlewood / theorem_1_2]]
- [[../library/primes/axler_2019_some_results_conjecture_hardy_littlewood/theorem_1_3|axler_2019_some_results_conjecture_hardy_littlewood / theorem_1_3]]
- [[../library/primes/axler_2019_some_results_conjecture_hardy_littlewood/theorem_1_4|axler_2019_some_results_conjecture_hardy_littlewood / theorem_1_4]]
- [[../library/primes/axler_2019_some_results_conjecture_hardy_littlewood/theorem_1_5|axler_2019_some_results_conjecture_hardy_littlewood / theorem_1_5]]
- [[../library/primes/chahal_et_al_2025_second_hardy_littlewood_conjecture/_index|chahal_et_al_2025_second_hardy_littlewood_conjecture]]
- [[../library/primes/chahal_et_al_2025_second_hardy_littlewood_conjecture/corollary_1_2|chahal_et_al_2025_second_hardy_littlewood_conjecture / corollary_1_2]]
- [[../library/primes/chahal_et_al_2025_second_hardy_littlewood_conjecture/corollary_1_4|chahal_et_al_2025_second_hardy_littlewood_conjecture / corollary_1_4]]
- [[../library/primes/chahal_et_al_2025_second_hardy_littlewood_conjecture/corollary_1_5|chahal_et_al_2025_second_hardy_littlewood_conjecture / corollary_1_5]]
- [[../library/primes/chahal_et_al_2025_second_hardy_littlewood_conjecture/theorem_1_1|chahal_et_al_2025_second_hardy_littlewood_conjecture / theorem_1_1]]
- [[../library/primes/clark_jarvis_2001_dense_admissible_sequences/_index|clark_jarvis_2001_dense_admissible_sequences]]
- [[../library/primes/clark_jarvis_2001_dense_admissible_sequences/conjecture_b|clark_jarvis_2001_dense_admissible_sequences / conjecture_b]]
- [[../library/primes/clark_jarvis_2001_dense_admissible_sequences/result_p1716|clark_jarvis_2001_dense_admissible_sequences / result_p1716]]
- [[../library/primes/clark_jarvis_2001_dense_admissible_sequences/result_p1717|clark_jarvis_2001_dense_admissible_sequences / result_p1717]]
- [[../library/primes/clark_jarvis_2001_dense_admissible_sequences/table_5|clark_jarvis_2001_dense_admissible_sequences / table_5]]
- [[../library/primes/dusart_2002_sur_la_conjecture_pi_x_y_pi_x_pi_y/_index|dusart_2002_sur_la_conjecture_pi_x_y_pi_x_pi_y]]
- [[../library/primes/hensley_1974_primes_intervals/_index|hensley_1974_primes_intervals]]
- [[../library/primes/hensley_1974_primes_intervals/theorem|hensley_1974_primes_intervals / theorem]]
- [[../library/primes/johnston_yang_2022_some_explicit_estimates_error_term_prime_number_theorem/_index|johnston_yang_2022_some_explicit_estimates_error_term_prime_number_theorem]]
- [[../library/primes/johnston_yang_2022_some_explicit_estimates_error_term_prime_number_theorem/corollary_1_2|johnston_yang_2022_some_explicit_estimates_error_term_prime_number_theorem / corollary_1_2]]
- [[../library/primes/johnston_yang_2022_some_explicit_estimates_error_term_prime_number_theorem/corollary_1_3|johnston_yang_2022_some_explicit_estimates_error_term_prime_number_theorem / corollary_1_3]]
- [[../library/primes/johnston_yang_2022_some_explicit_estimates_error_term_prime_number_theorem/lemma_2_2|johnston_yang_2022_some_explicit_estimates_error_term_prime_number_theorem / lemma_2_2]]
- [[../library/primes/johnston_yang_2022_some_explicit_estimates_error_term_prime_number_theorem/theorem_1_1|johnston_yang_2022_some_explicit_estimates_error_term_prime_number_theorem / theorem_1_1]]
- [[../library/primes/johnston_yang_2022_some_explicit_estimates_error_term_prime_number_theorem/theorem_1_4|johnston_yang_2022_some_explicit_estimates_error_term_prime_number_theorem / theorem_1_4]]
- [[../library/primes/openai_2026_quasi_riemann_hypothesis_zero_free_half_plane_11_12/_index|openai_2026_quasi_riemann_hypothesis_zero_free_half_plane_11_12]]
- [[../library/primes/openai_2026_quasi_riemann_hypothesis_zero_free_half_plane_11_12/theorem_1_1|openai_2026_quasi_riemann_hypothesis_zero_free_half_plane_11_12 / theorem_1_1]]
- [[../library/primes/openai_2026_quasi_riemann_hypothesis_zero_free_half_plane_7_8/_index|openai_2026_quasi_riemann_hypothesis_zero_free_half_plane_7_8]]
- [[../library/primes/openai_2026_quasi_riemann_hypothesis_zero_free_half_plane_7_8/theorem_1_1|openai_2026_quasi_riemann_hypothesis_zero_free_half_plane_7_8 / theorem_1_1]]
- [[../library/primes/openai_2026_uniform_exclusion_landau_siegel_zeros/_index|openai_2026_uniform_exclusion_landau_siegel_zeros]]
- [[../library/primes/openai_2026_uniform_exclusion_landau_siegel_zeros/theorem_1|openai_2026_uniform_exclusion_landau_siegel_zeros / theorem_1]]
- [[../library/primes/richards_1974_incompatibility_two_conjectures_concerning_primes_discussion_use_computers_attacking_theoretical_pro/_index|richards_1974_incompatibility_two_conjectures_concerning_primes_discussion_use_computers_attacking_theoretical_pro]]
- [[../library/primes/richards_1974_incompatibility_two_conjectures_concerning_primes_discussion_use_computers_attacking_theoretical_pro/corollary_1_10|richards_1974_incompatibility_two_conjectures_concerning_primes_discussion_use_computers_attacking_theoretical_pro / corollary_1_10]]
- [[../library/primes/richards_1974_incompatibility_two_conjectures_concerning_primes_discussion_use_computers_attacking_theoretical_pro/definition_1_7|richards_1974_incompatibility_two_conjectures_concerning_primes_discussion_use_computers_attacking_theoretical_pro / definition_1_7]]
- [[../library/primes/richards_1974_incompatibility_two_conjectures_concerning_primes_discussion_use_computers_attacking_theoretical_pro/proposition_1_9|richards_1974_incompatibility_two_conjectures_concerning_primes_discussion_use_computers_attacking_theoretical_pro / proposition_1_9]]
- [[../library/primes/richards_1974_incompatibility_two_conjectures_concerning_primes_discussion_use_computers_attacking_theoretical_pro/theorem_4_1|richards_1974_incompatibility_two_conjectures_concerning_primes_discussion_use_computers_attacking_theoretical_pro / theorem_4_1]]
- [[../library/primes/segal_1962_x_y_x_y/_index|segal_1962_x_y_x_y]]
- [[../library/primes/segal_1962_x_y_x_y/lemma_iv|segal_1962_x_y_x_y / lemma_iv]]
- [[../library/primes/segal_1962_x_y_x_y/theorem_i|segal_1962_x_y_x_y / theorem_i]]
- [[../library/primes/segal_1962_x_y_x_y/theorem_ii|segal_1962_x_y_x_y / theorem_ii]]

<!-- END problem library links -->

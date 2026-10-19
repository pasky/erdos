---
name: problems/arithmetic_functions/E0955
title: Problem 955
desc: |
  Asks whether every set $A$ of density zero has a preimage $s^{-1}(A)$ of
  density zero, where $s(n)=\sigma(n)-n$ is the sum of proper divisors. Known
  results cover the primes, sums of two squares, integers with unusually many
  prime factors, palindromes, and sparse and missing-digit sets.
tags:
- Number theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-17T22:11:11Z
---

# Problem 955

[[problems/arithmetic_functions/_index|..]]

[[problems/arithmetic_functions/E0955/claims/_index|claims/]]: The 8 claim pages of Problem 955, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let

$$
s(n)=\sigma(n)-n=\sum_{\substack{d\mid n\\ d<n}}d
$$

be the sum of proper divisors function.

If $A\subset \mathbb{N}$ has density $0$ then $s^{-1}(A)$ must also have density
$0$.

**Status.** Open. Bloom's catalog labeled the problem OPEN (page last edited 30
September 2025). Its commentary credits proofs for the following choices of $A$:
the primes, the integers with unusually many prime factors, the sums of two
squares, and the sets of size $x^{1/2+o(1)}$. Each is an accepted partial claim.
The general conjecture is open.

**Source.** [erdosproblems.com/955](https://www.erdosproblems.com/955), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #955,
https://www.erdosproblems.com/955.

**References.**

- [EGPS90] Erdős, P. and Granville, A. and Pomerance, C. and Spiro, C., On the
  normal behavior of the iterates of some arithmetic functions. Analytic number
  theory (Allerton Park, IL, 1989) (1990), 165-204.
- [Er73b] Erdős, P.,
  [[../library/arithmetic_functions/erdos_1973_uber_die_zahlen_der_form_und/_index|Über die Zahlen der Form $\sigma (n)-n$ und $n-\phi(n)$]].
  Elem. Math. (1973), 83-86.
- [Gu04] Guy, Richard K., Unsolved problems in number theory. Third edition,
  Problem Books in Mathematics, Springer, New York (2004), xviii+437 pp.;
  doi:10.1007/978-0-387-26677-0. Part B has no passage stating the
  density-zero preimage assertion; the nearest is section B10 "Untouchable
  numbers", p. 100, which records that the untouchable numbers have
  positive lower density. Library home:
  [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]].
- [PPT18] Pollack, Paul and Pomerance, Carl and Thompson, Lola, Divisor-sum
  fibers. Mathematika (2018), 330-342.
- [Po14b] Pollack, Paul,
  [[../library/arithmetic_functions/pollack_2014_arithmetic_properties_sum_proper_divisors_sum/_index|Some arithmetic properties of the sum of proper divisors and the sum of prime divisors]].
  Illinois J. Math. (2014), 125-147.
- [Tr15] Troupe, Lee,
  [[../library/arithmetic_functions/troupe_2015_number_prime_factors_values_sum_proper/_index|On the number of prime factors of values of the sum-of-proper-divisors function]].
  J. Number Theory (2015), 120-135.
- [Tr20] Troupe, Lee,
  [[../library/arithmetic_functions/troupe_2020_divisor_sums_representable_as_sum_two/_index|Divisor sums representable as the sum of two squares]].
  Proc. Amer. Math. Soc. (2020), 4189-4202.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/955.lean).

## Current assessment

**Search scope (2026-09-07 and 2026-09-09 UTC).** A bounded literature check
found no full solution among its sampled sources. It covered the 2023 and 2026
arXiv records, the authors' publication pages, exact-title and EGPS searches,
and indexed recent announcements including X. The July 2026 paper retains the
general assertion as its Conjecture 1.3 and says it remains open; its [arXiv
record](https://arxiv.org/abs/2607.18981) lists v1, and [Thompson's publication
page](https://www.lolathompson.com/research.html) lists the work as submitted.
No status-changing item was found on these routes. This is a bounded assessment,
not an exhaustive literature or announcement search.

**Proof coverage.** The cited statements and source versions below are
taken from the complete cited pages. The truncation, digit-target
interpretation and prime-input split are elementary derivations recorded
here. Full proofs of the cited theorems are not reconstructed here; each
claim page records the evidence its result rests on, and the general
conjecture remains the mathematical gap.

## Progress

The arbitrary density-zero assertion remains open. It is the preimage form of
Erdős--Granville--Pomerance--Spiro's
[[../library/arithmetic_functions/erdos_1990_normal_behavior_iterates_arithmetic_functions/conjecture_4|Conjecture 4]]:
a set of positive upper density has an image under $s$ of positive upper
density. The 1990 paper states that image form on printed p. 169 and
explicitly uses the preimage form on printed p. 200. The equivalence
follows from
$s(s^{-1}(A))\subseteq A$ and $B\subseteq s^{-1}(s(B))$; it does not prove
either formulation.

The strongest structure-free result compiled here requires substantially more
than density zero: a target counting function at most $x^{1/2+o(1)}$.
Missing-digit sets admit separate results, including the 2026 extension to
base two and a sharper bound, stated after prime inputs are excluded, whose
printed proof has a gap for $g\geq3$. None treats an arbitrary density-zero
target.

## Known Results

**Single targets.** Pollack's Theorem 1.11 [Po14b] shows that $s(n)$ is prime
for only $O(x/\log x)$ of the $n\le x$, so the preimage of the primes has
density zero
([[problems/arithmetic_functions/E0955/claims/2015_04_01_pollack|claim page]]).
Troupe's Theorem 1.3 [Tr15] shows that $\omega(s(n))$ and $\Omega(s(n))$ lie
within $\epsilon\log\log s(n)$ of $\log\log s(n)$ for all but $o(x)$ of the
$n\le x$, which settles the targets of integers with abnormally many or few
prime factors
([[problems/arithmetic_functions/E0955/claims/2014_05_14_troupe|claim page]]).
Pollack and Troupe's Erdős--Kac law for $\omega(s(n))$ (Proc. Amer. Math. Soc.
151 (2023), 977--988) refines this to the targets
$\{m:|\omega(m)-\log\log m|>h(m)(\log\log m)^{1/2}\}$ for every
$h(m)\to\infty$
([[problems/arithmetic_functions/E0955/claims/2021_06_20_pollack_troupe|claim page]]).
Troupe's Theorem 1.2 [Tr20] counts the $n\le x$ with $s(n)$ a sum of two
squares as of order $x/(\log x)^{1/2}$
([[problems/arithmetic_functions/E0955/claims/2019_02_28_troupe|claim page]]).
Pollack's Theorem 1 (Integers 15A (2015), A13) shows that $s(n)$ is a base-$g$
palindrome only for a density-zero set of $n$
([[problems/arithmetic_functions/E0955/claims/2015_06_15_pollack|claim page]]).

**Finite sparse targets.** Pollack, Pomerance, and Thompson's
[[../library/arithmetic_functions/pollack_2018_divisor_sum_fibers/theorem_1_2|Theorem 1.2]]
is a proved theorem. In the 11-page 2017 author manuscript, its p. 2, it
fixes a function $\varepsilon(x)\to0$ and assumes that a finite set
$A$ of positive integers has total cardinality

$$
|A|\leq x^{1/2+\varepsilon(x)}.
$$

The number of $n\leq x$ with $s(n)\in A$ is then $o_\varepsilon(x)$,
uniformly over such $A$. Equivalently, there is a function
$\delta_\varepsilon(x)\to0$, independent of $A$, such that this count is at
most $\delta_\varepsilon(x)x$. Density zero alone does not imply the finite
total-cardinality hypothesis.

The infinite-set consequence is a separate truncation argument. If a fixed
set $B$ satisfies $|B\cap[1,y]|\leq y^{1/2+o(1)}$, then for sufficiently
large $x$ every relevant value $s(n)$, $n\leq x$, is below
$2x\log\log x$. Apply the finite theorem to
$A_x=B\cap[1,2x\log\log x]$, whose total cardinality is
$x^{1/2+o(1)}$ or smaller. It follows that $s^{-1}(B)$ has density zero
([[problems/arithmetic_functions/E0955/claims/2017_06_09_pollack_pomerance_thompson|claim page]]).
The manuscript's page numbers are distinct from the published
*Mathematika* 64 (2018), 330--342 pagination.

**Large individual fibers.** The same paper's
[[../library/arithmetic_functions/pollack_2018_divisor_sum_fibers/theorem_1_4|Theorem 1.4]],
also on its p. 2, proves that there is an absolute $c>0$ such that, for
every $\alpha,\eta>0$, infinitely many $m$ have at least
$\exp(c\log m/\log\log m)$ distinct $s$-preimages in
$(\alpha(1-\eta)m,\alpha(1+\eta)m)$. The authors give $c=1/7$.
This disproves the proposed uniform bound on the number of solutions
$n\leq\theta m$ to $s(n)=m$ for fixed $\theta>0$. It does not disprove
the density-zero preimage conjecture: large individual fibers do not supply
a density-zero target whose preimage has positive upper density.

**Missing digits.** Fix a base $g$, a nonempty proper digit set
$D\subsetneq\{0,\ldots,g-1\}$, and $\gamma\in(0,1)$. Benli, Cesana,
Dartyge, Dombrowsky, and Thompson's
[[../library/arithmetic_functions/benli_2023_sums_proper_divisors_missing_digits/theorem_1_8|Theorem 1.8]]
(arXiv:2307.12859v1, p. 2;
[[problems/arithmetic_functions/E0955/claims/2023_07_24_benli_cesana_dartyge_dombrowsky_thompson|claim page]])
gives, for $g\geq3$,

$$
\#\{n\leq x:\text{all base-}g\text{ digits of }s(n)\text{ lie in }D\}
\ll_{g,D,\gamma}x\exp\bigl(- (\log\log x)^\gamma\bigr).
$$

These fixed digit targets have density zero. Benli, Dartyge, Dombrowsky,
Pollack, and Thompson's 2026 preprint records the bound for every $g\geq2$
in
[[../library/arithmetic_functions/benli_2026_digits_sum_proper_divisors/theorem_1_4|Theorem 1.4]]
(arXiv:2607.18981v1, p. 2). Its Appendix A, pp. 16--17,
supplies the binary case omitted from the earlier theorem
([[problems/arithmetic_functions/E0955/claims/2026_07_21_benli_dartyge_dombrowsky_pollack_thompson|claim page]]).

The 2026 paper's
[[../library/arithmetic_functions/benli_2026_digits_sum_proper_divisors/theorem_1_5|Theorem 1.5]]
(same version, p. 2) fixes a nonzero digit $a_0\in\{1,\ldots,g-1\}$ and
states, for some $c=c(g)>0$,

$$
\#\{n\leq x:n\text{ composite and }s(n)\text{ omits }a_0\}
\ll x\exp(-c\sqrt{\log x}).
$$

This sharper estimate is restricted to composite inputs and omission of a
nonzero digit. Since $s(p)=1$, restoring prime inputs adds no primes when
$a_0=1$, and at most $\pi(x)$ otherwise; $n=1$ contributes at most one
exception. The derived all-input bound is therefore still $o(x)$, but the
displayed sharper estimate is not asserted for all inputs. The printed proof
of this rate for $g\geq3$ has a gap in its small-gcd step (pp. 15--16), as the
library card records; the qualitative density-zero conclusion for these
targets already follows from Theorem 1.4.

**Sources without a claim page.** Erdős's [Er73b]
[[../library/arithmetic_functions/erdos_1973_uber_die_zahlen_der_form_und/satz_i|Satz I]]
exhibits a set of positive lower density with empty preimage under $s$ and
concerns no density-zero target. Fan's Theorem 6 (arXiv:2508.06005) with $f=1$
treats a target that moves with $x$ and follows from Pollack and Troupe's
theorem, and its weighted proportions are not the problem's density. Pollack
and Singha Roy (Colloq. Math. 168 (2022), 287--295) prove in Proposition 3.1,
for $k\ge4$, that almost always no $p^k$ above a threshold depending on $x$
divides $s(n)$; with their Lemma 2.2 this bears on the density-zero target of
their Remark 3.4, but the paper states no preimage theorem for a fixed target.
Luca and Pomerance's theorem concerns a target of positive lower density, and
the congruence estimates of Lebowitz-Lockard and coauthors supply no
density-zero target; neither settles an instance.

## Exact scope of the arithmetic reduction

The uniform finite-target theorem in
[[../library/arithmetic_functions/pollack_2018_divisor_sum_fibers/_index|Pollack–Pomerance–Thompson,
Theorem 1.2]] applies when the target cardinality is at most
$x^{1/2+\epsilon(x)}$, with $\epsilon(x)\to0$. Splitting an arbitrary
density-zero target into many such pieces multiplies an uncontrolled $o(x)$
error and does not prove the desired extension.

A complete abstract countermodel shows the missing implication. Let
$A=\{\lfloor j^{3/2}\rfloor:j\ge1\}$, and let $T(n)$ be its largest member at
most $n$. Consecutive members near $x$ are separated by $O(x^{1/3})$, so every
fiber restricted to $[1,x]$ has size at most $Cx^{1/3}$. Uniformly over sets
$B$ of size at most $x^{1/2+\epsilon(x)}$,

$$
\#\{n\le x:T(n)\in B\}\le Cx^{5/6+\epsilon(x)}=o(x).
$$

Nevertheless $A(x)=O(x^{2/3})$, $T(n)\sim n$, and $T^{-1}(A)=\mathbb N$. Thus
even uniform small-target control and linear output size do not imply
preservation of every density-zero set. This countermodel, independently
examined in the
[[research/leads/aliquot_collision_density/evidence/verify/analytic_conclusions/grade|graded analytic review]],
concerns a general inference, not the arithmetic function $s$. The source
theorem and initial proof reduction were inspected, without auditing the whole
proof. Additional arithmetic control on larger sparse target sets remains
necessary.

How much control is needed is recorded in
[[research/leads/aliquot_collision_density/_index|the collision-count lead]].
It proves that the problem is equivalent to the same uniform control for
targets of size $\eta x$, with the bound tending to zero with $\eta$, and to
a linear bound on the collisions $s(n)=s(n')$ after an arbitrarily small
proportion of inputs is removed. It also proves that no density-zero
exclusion of inputs gives a linear collision bound. The independent review
and separate grade accept those exact analytic propositions at the stated
external theorem interfaces. Neither proves that the equivalent conditions
hold; the stronger condition (D) also remains unproved. The review excludes
the numerical census and the sieve route, and does not change the problem
status above. The lead also reduces the problem to collision bounds for
inputs made of a small cofactor and boundedly many large primes. Its
coefficient-uniform two-form sieve estimate is proved. After an arbitrarily
small input deletion, its averaged sieve input reduces to one open estimate
for large common divisors of values of $s$; that estimate and the
smooth-input count remain unproved.
For the full equation with at least three large primes on each side,
the lead proves uniform bounds on the prime-power local densities and
their cofactor average after a negligible removal. These local bounds
do not count the prime solutions in integer boxes. Inputs with
many comparable prime factors make the sum of an error of one over every
pair of short-slice fixed parts too large; an averaged estimate remains
possible. These additions are author-recorded and outside the review,
and do not prove the class collision bounds or the problem.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/arithmetic_functions/benli_2023_sums_proper_divisors_missing_digits/_index|benli_2023_sums_proper_divisors_missing_digits]]
- [[../library/arithmetic_functions/benli_2023_sums_proper_divisors_missing_digits/theorem_1_8|benli_2023_sums_proper_divisors_missing_digits / theorem_1_8]]
- [[../library/arithmetic_functions/benli_2026_digits_sum_proper_divisors/_index|benli_2026_digits_sum_proper_divisors]]
- [[../library/arithmetic_functions/benli_2026_digits_sum_proper_divisors/theorem_1_4|benli_2026_digits_sum_proper_divisors / theorem_1_4]]
- [[../library/arithmetic_functions/benli_2026_digits_sum_proper_divisors/theorem_1_5|benli_2026_digits_sum_proper_divisors / theorem_1_5]]
- [[../library/arithmetic_functions/erdos_1973_uber_die_zahlen_der_form_und/_index|erdos_1973_uber_die_zahlen_der_form_und]]
- [[../library/arithmetic_functions/erdos_1973_uber_die_zahlen_der_form_und/satz_i|erdos_1973_uber_die_zahlen_der_form_und / satz_i]]
- [[../library/arithmetic_functions/erdos_1973_uber_die_zahlen_der_form_und/satz_ii|erdos_1973_uber_die_zahlen_der_form_und / satz_ii]]
- [[../library/arithmetic_functions/erdos_1990_normal_behavior_iterates_arithmetic_functions/_index|erdos_1990_normal_behavior_iterates_arithmetic_functions]]
- [[../library/arithmetic_functions/erdos_1990_normal_behavior_iterates_arithmetic_functions/conjecture_4|erdos_1990_normal_behavior_iterates_arithmetic_functions / conjecture_4]]
- [[../library/arithmetic_functions/erdos_1990_normal_behavior_iterates_arithmetic_functions/theorem_5_2|erdos_1990_normal_behavior_iterates_arithmetic_functions / theorem_5_2]]
- [[../library/arithmetic_functions/fan_2025_hardy_ramanujan_inequality_sifted_sets_its_applications/_index|fan_2025_hardy_ramanujan_inequality_sifted_sets_its_applications]]
- [[../library/arithmetic_functions/fan_2025_hardy_ramanujan_inequality_sifted_sets_its_applications/theorem_1_1|fan_2025_hardy_ramanujan_inequality_sifted_sets_its_applications / theorem_1_1]]
- [[../library/arithmetic_functions/fan_2025_hardy_ramanujan_inequality_sifted_sets_its_applications/theorem_1_6|fan_2025_hardy_ramanujan_inequality_sifted_sets_its_applications / theorem_1_6]]
- [[../library/arithmetic_functions/lebowitz_lockard_et_al_2021_distribution_mod_p_eulers_totient_sum_proper_divisors/_index|lebowitz_lockard_et_al_2021_distribution_mod_p_eulers_totient_sum_proper_divisors]]
- [[../library/arithmetic_functions/lebowitz_lockard_et_al_2021_distribution_mod_p_eulers_totient_sum_proper_divisors/theorem_1_3|lebowitz_lockard_et_al_2021_distribution_mod_p_eulers_totient_sum_proper_divisors / theorem_1_3]]
- [[../library/arithmetic_functions/luca_pomerance_2015_range_sum_of_proper_divisors_function/_index|luca_pomerance_2015_range_sum_of_proper_divisors_function]]
- [[../library/arithmetic_functions/luca_pomerance_2015_range_sum_of_proper_divisors_function/theorem_1|luca_pomerance_2015_range_sum_of_proper_divisors_function / theorem_1]]
- [[../library/arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/_index|plasma_ai_2026_normal_order_number_iterations_euler_s_function]]
- [[../library/arithmetic_functions/pollack_2014_arithmetic_properties_sum_proper_divisors_sum/_index|pollack_2014_arithmetic_properties_sum_proper_divisors_sum]]
- [[../library/arithmetic_functions/pollack_2014_arithmetic_properties_sum_proper_divisors_sum/theorem_1_11|pollack_2014_arithmetic_properties_sum_proper_divisors_sum / theorem_1_11]]
- [[../library/arithmetic_functions/pollack_2015_palindromic_sums_proper_divisors/_index|pollack_2015_palindromic_sums_proper_divisors]]
- [[../library/arithmetic_functions/pollack_2018_divisor_sum_fibers/_index|pollack_2018_divisor_sum_fibers]]
- [[../library/arithmetic_functions/pollack_2018_divisor_sum_fibers/theorem_1_2|pollack_2018_divisor_sum_fibers / theorem_1_2]]
- [[../library/arithmetic_functions/pollack_2018_divisor_sum_fibers/theorem_1_4|pollack_2018_divisor_sum_fibers / theorem_1_4]]
- [[../library/arithmetic_functions/pollack_roy_2021_powerfree_sums_proper_divisors/_index|pollack_roy_2021_powerfree_sums_proper_divisors]]
- [[../library/arithmetic_functions/pollack_roy_2021_powerfree_sums_proper_divisors/proposition_3_1|pollack_roy_2021_powerfree_sums_proper_divisors / proposition_3_1]]
- [[../library/arithmetic_functions/pollack_roy_2021_powerfree_sums_proper_divisors/theorem_1_2|pollack_roy_2021_powerfree_sums_proper_divisors / theorem_1_2]]
- [[../library/arithmetic_functions/pollack_roy_2021_powerfree_sums_proper_divisors/theorem_3_3|pollack_roy_2021_powerfree_sums_proper_divisors / theorem_3_3]]
- [[../library/arithmetic_functions/pollack_troupe_2021_sums_proper_divisors_follow_erdos_kac_law/_index|pollack_troupe_2021_sums_proper_divisors_follow_erdos_kac_law]]
- [[../library/arithmetic_functions/pollack_troupe_2021_sums_proper_divisors_follow_erdos_kac_law/theorem_1|pollack_troupe_2021_sums_proper_divisors_follow_erdos_kac_law / theorem_1]]
- [[../library/arithmetic_functions/pomerance_2018_first_function_iterates/_index|pomerance_2018_first_function_iterates]]
- [[../library/arithmetic_functions/pomerance_2018_first_function_iterates/conjecture_2_3|pomerance_2018_first_function_iterates / conjecture_2_3]]
- [[../library/arithmetic_functions/pomerance_2018_first_function_iterates/theorem_2_4|pomerance_2018_first_function_iterates / theorem_2_4]]
- [[../library/arithmetic_functions/troupe_2015_number_prime_factors_values_sum_proper/_index|troupe_2015_number_prime_factors_values_sum_proper]]
- [[../library/arithmetic_functions/troupe_2015_number_prime_factors_values_sum_proper/theorem_1_3|troupe_2015_number_prime_factors_values_sum_proper / theorem_1_3]]
- [[../library/arithmetic_functions/troupe_2015_number_prime_factors_values_sum_proper/theorem_1_4|troupe_2015_number_prime_factors_values_sum_proper / theorem_1_4]]
- [[../library/arithmetic_functions/troupe_2020_divisor_sums_representable_as_sum_two/_index|troupe_2020_divisor_sums_representable_as_sum_two]]
- [[../library/arithmetic_functions/troupe_2020_divisor_sums_representable_as_sum_two/theorem_1_2|troupe_2020_divisor_sums_representable_as_sum_two / theorem_1_2]]
- [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]]

<!-- END problem library links -->

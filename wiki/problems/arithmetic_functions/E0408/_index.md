---
name: problems/arithmetic_functions/E0408
title: Problem 408
desc: |
  Asks whether the number of iterations of Euler's totient needed to reach 1,
  divided by $\log n$, has a distribution function or is almost always constant.
tags:
- Number theory
- Iterated functions
status: solved
claim: proved
parts: [distribution, constant]
created: 2026-09-04T09:17:27Z
updated: 2026-10-19T06:24:13Z
---

# Problem 408

[[problems/arithmetic_functions/_index|..]]

[[problems/arithmetic_functions/E0408/claims/_index|claims/]]: The 2 claim pages of Problem 408, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $\phi(n)$ be the Euler totient function and $\phi_k(n)$ be
the iterated $\phi$ function, so that $\phi_1(n)=\phi(n)$ and
$\phi_k(n)=\phi(\phi_{k-1}(n))$. Let

$$
f(n) = \min \{ k : \phi_k(n)=1\}.
$$

Does $f(n)/\log n$ have a distribution function? Is $f(n)/\log n$ almost always
constant? What can be said about the largest prime factor of $\phi_k(n)$ when,
say, $k=\log\log n$?

**Formulation.** The second question is read as asking for a normal order:
whether $f(n)/\log n$ tends to a constant on a set of asymptotic density one.
That is how Erdős and Graham pose it on p. 81 of [ErGr80], asking whether
$f(n)/\log n$ is almost always constant, how [EGPS90] states its conjecture on
p. 166, $k(n)\sim\alpha\log n$ on a set of asymptotic density one, and how
erdosproblems.com reads it. Read as Bloom's catalog words it, the question has a
trivial answer no: $f(n)/\log n=c$ determines $n$ from $f(n)$, so each value of
$f$ gives at most one such $n$. The first two questions are the parts
`distribution` and `constant`, in order. The third asks what can be said rather
than a definite question, so it is open-ended: it is not a part, and it never
blocks the standing.

**Status.** Solved: an accepted partial claim settles both parts, and the
open-ended third question does not block the standing.
Bloom's catalog labeled the problem OPEN (page last edited 30 September 2025). Its commentary credits [EGPS90] with a yes to the first two
questions under a form of the Elliott--Halberstam conjecture. That conditional
theorem is the claim on
[[problems/arithmetic_functions/E0408/claims/1990_01_01_erdos_granville_pomerance_spiro|the Erdős–Granville–Pomerance–Spiro page]].
Its scope is conditional, and it derives nothing for the standing. Plasma AI's
2026 preprint and Lean formalization claim the first two questions without
hypothesis; that claim, on
[[problems/arithmetic_functions/E0408/claims/2026_10_14_plasma_ai|the Plasma AI page]],
is accepted on this corpus's rebuild, Comparator check and kernel replay of
the formalization and a graded review of its statements. The third question,
open-ended, is answered in the form
the erdosproblems.com commentary expects by Ford, Konyagin and Luca
[FKL10, Theorem 5], by a deduction that [PAI26, Proposition 7.1] records and
the Standing restates.

**Source.** [erdosproblems.com/408](https://www.erdosproblems.com/408), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #408,
https://www.erdosproblems.com/408.

**References.**

- [EGPS90] Erdős, P. and Granville, A. and Pomerance, C. and Spiro, C., On the
  normal behavior of the iterates of some arithmetic functions. Analytic number
  theory (Allerton Park, IL, 1989) (1990), 165-204.
- [ErGr80] Erdős, P. and Graham, R., Old and new problems and results in
  combinatorial number theory. Monographies de L'Enseignement Mathematique
  (1980).
- [Gu04] Guy, Richard K., Unsolved problems in number theory, third
  edition, Problem Books in Mathematics, Springer (2004), xviii+437 pp.;
  B41 "Iterations of $\phi$ and $\sigma$", printed pp. 147--148: the class
  $k(n)$, the least $k$ with $\phi_k(n)=1$, Pillai's bounds between
  $\ln n/\ln 3$ and $\ln n/\ln 2$, the density of $k(n)/\ln n$ in
  $[1/\ln 3,1/\ln 2]$, the question of its average and normal behavior, and
  the [EGPS90] conjecture of a normal order $\alpha\ln n$, which Guy records
  as proved there under the Elliott--Halberstam conjecture; the hypothesis
  [EGPS90] uses is a strong form of that conjecture, stated on
  [[problems/arithmetic_functions/E0408/claims/1990_01_01_erdos_granville_pomerance_spiro|its claim page]].
  Library home:
  [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]].
- [FKL10] Ford, Kevin and Konyagin, Sergei V. and Luca, Florian, Prime chains
  and Pratt trees. Geom. Funct. Anal. (2010), 1231-1258. Library home:
  [[../library/integer_sequences/ford_2010_prime_chains_pratt_trees/_index|ford_2010_prime_chains_pratt_trees]].
- [PAI26] Plasma AI, The normal order of the number of iterations of Euler's
  function, preprint (2026), with a Lean formalization, at
  https://github.com/plasma-ai/erdos-408. Library home:
  [[../library/arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/_index|plasma_ai_2026_normal_order_number_iterations_euler_s_function]].
- [Pi29] Pillai, S. Sivasankaranarayana, On some functions connected with
  $\phi(n)$. Bull. Amer. Math. Soc. (1929), 832-836.
- [Sh50] Shapiro, Harold N., On the iterates of a certain class of arithmetic
  functions. Comm. Pure Appl. Math. (1950), 259-272.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/7db2ea3b91bfbd0ab620215163e6c488bbb916d5/FormalConjectures/ErdosProblems/408.lean)
at its commit of 2026-10-14, linked, which states the first two questions as
`erdos_408.parts.i` and `erdos_408.parts.ii` with `sorry` bodies, leaves the
third unformalised, and states Pillai's bounds and a theorem of Ford, Konyagin
and Luca as solved variants. Plasma AI's Lean development
([plasma-ai/erdos-408](https://github.com/plasma-ai/erdos-408/tree/4ea44bf911f8668aec10ec25c4b309e8ed476666),
linked) proves both, copying the two statements with formal-conjectures'
density inlined; [[problems/arithmetic_functions/E0408/claims/2026_10_14_plasma_ai|its claim page]]
records it. This corpus rebuilt it at that commit, checked it with Comparator
and replayed its three theorems in the kernel, as
[[../library/arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence/verify/replay_receipt|the replay receipt]] records.

## Current assessment

**The question (erdosproblems.com formulation, 2026-09-04).** Whether
$f(n)/\log n$, the number of totient iterations needed to reach $1$ divided by
$\log n$, has a distribution function; whether it is almost always constant,
read as a normal order (Formulation); and what can be said about the largest
prime factor of $\phi_k(n)$ for $k=\log\log n$. Bloom's catalog labeled the
problem OPEN (page last edited 30 September 2025).

**Standing.** Solved. Plasma AI's 2026 claim, on
[[problems/arithmetic_functions/E0408/claims/2026_10_14_plasma_ai|its page]],
proves the first two questions unconditionally: $f(n)$ has normal order
$\alpha\log n$ for a constant $\alpha\in[1/\log3,1/\log2]$, so $f(n)/\log n$ tends
to $\alpha$ on a set of density one, with the unit step at $\alpha$ as its
distribution function. It is accepted: this corpus rebuilt the Lean
formalization, Comparator accepted it, and the kernel replayed its three
theorems from an empty environment
([[../library/arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence/verify/replay_receipt|the replay receipt]]), and the
[[../library/arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence/verify/statement_fidelity/_index|graded review of the formalization's statements]]
found them faithful, covering the first two questions; the preprint itself is
unrefereed. The claim settles the parts `distribution` and `constant`, so the
problem is solved; the open-ended third question does not block the standing,
and what is known about it is recorded below.
The earlier claim page,
[[problems/arithmetic_functions/E0408/claims/1990_01_01_erdos_granville_pomerance_spiro|the Erdős–Granville–Pomerance–Spiro page]],
records a conditional theorem: for some $\alpha>0$, $f(n)$ has normal and
average order $\alpha\log n$ provided an Elliott--Halberstam-type estimate
holds up to the level $x^{1-(\log\log x)^{-2}}$, a hypothesis stronger than
the usual conjecture and unproven; under it $f(n)/\log n\to\alpha$ on a set
of density one, and the first two questions have the answer yes. The claim
is `claimed`: the chapter is in a proceedings volume with no evidence of
refereeing recorded, and the erdosproblems.com credit is commentary on a problem
it labeled OPEN. Unconditionally, the erdosproblems.com commentary records
Pillai's bounds $\log n/\log3<f(n)<\log n/\log2$ for all large $n$ [Pi29] and
Shapiro's result that $f(n)$ is essentially multiplicative [Sh50]; [EGPS90]
notes on p. 166 that the values of $f(n)/\log n$ are dense in
$[1/\log3,1/\log2]$, by the numbers $2^i3^j$. On the third question, the
erdosproblems.com commentary records the expectation that, whenever
$k\to\infty$ with $n$, the largest prime factor of $\phi_k(n)$ is at most
$n^{o(1)}$ for almost all $n$. Ford, Konyagin and Luca proved it
[FKL10, Theorem 5]: for all $\varepsilon,\delta>0$ some integer $k$ makes
$P^+(\phi_k(n))\le x^\varepsilon$ for at least $(1-\delta)x$ integers
$n\le x$ once $x$ is large. Since $P^+(\phi(m))\le P^+(m)$, the bound holds at
every later iterate, so for every integer-valued $k(n)\to\infty$, among them
$k=\lfloor\log\log n\rfloor$, the largest prime factor of $\phi_{k(n)}(n)$ is
$n^{o(1)}$ on a set of density one; [PAI26, Proposition 7.1] records this
deduction. The credit for that part is theirs. It is
not formalized here; formal-conjectures states their theorem as a solved
variant with a `sorry` body.

**Search scope (2026-10-07).** The erdosproblems.com page and its commentary,
the abstract and introduction of [EGPS90], and B41 of [Gu04]; no other
literature search was made, and no proof was independently assessed.

**Search scope (2026-10-14).** Plasma AI's preprint and the repository
plasma-ai/erdos-408 at its commit of 2026-10-14, formal-conjectures' statement
of the problem at its commit of the same date, and Theorem 5 of [FKL10], which
that statement cites, on its library card. The paper's argument was not
refereed here; the formal proof's check is in
[[../library/arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence/verify/replay_receipt|the replay receipt]].

## Method connection

[[research/methods/shifted_prime_moments|Moments over the prime factors of $p-1$]]
carries Plasma AI's claimed resolution of the first two questions: the
additive function behind $f$ and the equidistribution of the prime factors of
$p-1$.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/arithmetic_functions/erdos_1990_normal_behavior_iterates_arithmetic_functions/_index|erdos_1990_normal_behavior_iterates_arithmetic_functions]]
- [[../library/arithmetic_functions/erdos_1990_normal_behavior_iterates_arithmetic_functions/theorem_2_1|erdos_1990_normal_behavior_iterates_arithmetic_functions / theorem_2_1]]
- [[../library/arithmetic_functions/erdos_1990_normal_behavior_iterates_arithmetic_functions/theorem_2_2|erdos_1990_normal_behavior_iterates_arithmetic_functions / theorem_2_2]]
- [[../library/arithmetic_functions/openai_2026_poisson_dirichlet_law_prime_predecessors/_index|openai_2026_poisson_dirichlet_law_prime_predecessors]]
- [[../library/arithmetic_functions/openai_2026_weighted_dilation_graphs_smooth_shifted_primes_totient_fibers/_index|openai_2026_weighted_dilation_graphs_smooth_shifted_primes_totient_fibers]]
- [[../library/arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/_index|plasma_ai_2026_normal_order_number_iterations_euler_s_function]]
- [[../library/arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence/verify/statement_fidelity/_index|plasma_ai_2026_normal_order_number_iterations_euler_s_function / evidence/verify/statement_fidelity/_index]]
- [[../library/arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/theorem_1_1|plasma_ai_2026_normal_order_number_iterations_euler_s_function / theorem_1_1]]
- [[../library/integer_sequences/ford_2010_prime_chains_pratt_trees/_index|ford_2010_prime_chains_pratt_trees]]
- [[../library/integer_sequences/ford_2010_prime_chains_pratt_trees/theorem_5|ford_2010_prime_chains_pratt_trees / theorem_5]]
- [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]]
- [[../library/primes/openai_2026_quasi_riemann_hypothesis_zero_free_half_plane_7_8/_index|openai_2026_quasi_riemann_hypothesis_zero_free_half_plane_7_8]]

<!-- END problem library links -->

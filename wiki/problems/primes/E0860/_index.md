---
name: problems/primes/E0860
title: Problem 860
desc: |
  Asks to estimate the least $h(n)$ such that every interval $(m,m+h(n))$
  contains distinct integers $a_1,\ldots,a_{\pi(n)}$, with $a_i$ divisible by
  the $i$th prime $p_i$.
tags:
- Number theory
- Primes
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 860

[[problems/primes/_index|..]]

[[problems/primes/E0860/claims/_index|claims/]]: The 6 claim pages of Problem 860, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $h(n)$ be such that, for any $m\geq 1$, in the interval
$(m,m+h(n))$ there exist distinct integers $a_i$ for $1\leq i\leq \pi(n)$ such
that $p_i\mid a_i$, where $p_i$ denotes the $i$th prime.

Estimate $h(n)$.

**Status.** Open. This is the erdosproblems.com label (page last edited 30
September 2025). The proof-claims tab carries two pending partial claims.
Neither would settle the problem, and the Current assessment records them. The
accepted partial claims are on
[[problems/primes/E0860/claims/1980_06_13_erdos_pomerance|the page of Erdős and Pomerance]]
and [[problems/primes/E0860/claims/1995_01_01_ruzsa|Ruzsa's page]]. The
Erdős--Selfridge lower bound and the joint upper bound of Chen and Korsky are
claimed partial results. They are on
[[problems/primes/E0860/claims/1980_06_13_erdos_selfridge|the page of Erdős and Selfridge]]
and
[[problems/primes/E0860/claims/2026_08_13_chen_korsky|the joint page of Chen and Korsky]].

**Source.** [erdosproblems.com/860](https://www.erdosproblems.com/860), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #860,
https://www.erdosproblems.com/860.

**References.**

- [ErPo80] P. Erdős and C. Pomerance, Matching the natural numbers up to $n$
  with distinct multiples in another interval. Indag. Math. (Proc.) 83
  (1980), no. 2, 147--161, DOI 10.1016/1385-7258(80)90018-9. Library home:
  [[../library/primes/erdos_1980_matching_natural_numbers_up_n_distinct/_index|erdos_1980_matching_natural_numbers_up_n_distinct]].
- [Gu04] Guy, Richard K., Unsolved problems in number theory. Third edition,
  Problem Books in Mathematics, Springer (2004), xviii+437 pp. Section B32
  "Grimm's conjecture", printed p. 133: "Erdős & Selfridge asked for an
  estimate of $f(n)$", the page's $h(n)$ less one, with the
  Erdős--Selfridge--Pomerance bounds
  $(3-\epsilon)n\le f(n)\ll n^{3/2}(\ln n)^{-1/2}$ for large $n$. Library
  home:
  [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]].

**Formalization.** None recorded.

## Current assessment

**Known bounds.** The erdosproblems.com commentary records $h(n)>(3-o(1))n$
(Erdős and Selfridge), $h(n)/n\to\infty$ (Ruzsa) and
$h(n)\ll n^{3/2}/(\log n)^{1/2}$ (Erdős and Pomerance [ErPo80]). The last two
are refereed and recorded as accepted partial claims, on
[[problems/primes/E0860/claims/1995_01_01_ruzsa|Ruzsa's page]] and
[[problems/primes/E0860/claims/1980_06_13_erdos_pomerance|the page of Erdős and Pomerance]];
the first is reported by Erdős and Pomerance and by Guy with no printed
proof on record, and stays claimed on
[[problems/primes/E0860/claims/1980_06_13_erdos_selfridge|the page of Erdős and Selfridge]].
The functions of Erdős and Pomerance, of Guy and of the arXiv paper below
count the integers of a closed interval, so each is this page's $h(n)$ less
one; no asymptotic bound feels the shift.

**Pending claims.** On 2026-10-06 the proof-claims tab carries two partial
claims, both made with AI systems and both pending, each on its own page.
Samuel Korsky (with GPT 5.6-Pro, filed 26 July 2026, four comments) claims
the lower bound
$h(n)\ge n\exp((\frac{\log2}2-o(1))\frac{\log n}{\log\log n})$ by adapting a
construction of Green and Ruzsa, on
[[problems/primes/E0860/claims/2026_07_26_korsky|Korsky's claim page]]. Kaizhe
Chen (with ChatGPT 5.6 Sol, filed 29 July 2026, one comment) claims a lower
bound of the same shape with an unspecified constant and the upper bounds
$h(n)\ll n^{1.4}$ and, for the function of Problem 711,
$F(n)\ll n^{1.4031}$, on
[[problems/primes/E0860/claims/2026_07_29_chen|the second claim page]]. Chen's
arXiv paper 2607.26450 carried the tab's bounds in its first version (29
July 2026: $h(n)\ll n^{7/5}/(\log n)^{2/5}$, $F(n)\ll n^{1.4031}$,
lower-bound constant $1/50$); its second version (13 August 2026), joint
with Korsky, sharpens the upper bound to $h(n)\ll n^{4/3}/(\log n)^{1/3}$
and carries Korsky's constant $\frac{\log2}2$. The joint upper bound, which
no tab claim carries, is on
[[problems/primes/E0860/claims/2026_08_13_chen_korsky|the joint page of Chen and Korsky]].
This page records the claims without adopting them; no claim would settle
the problem, which asks for the order of magnitude of $h(n)$.

## Exact local reduction and remaining uniformity

Hall's condition requires the union of available multiples to have size at
least $|S|$ for every subset $S$ of primes up to $n$, not just the full prime
set. For fixed $n$, these incidence graphs are periodic modulo the primorial,
giving finite tests but no asymptotic bound by themselves.

The partial matching in
[[../library/primes/doorn_2026_optimal_bounds_erdos_problem_matching_integers/_index|van
Doorn–Li–Tang's Theorem 2.1]] matches at least $\min(r,\lceil2\sqrt r\rceil)$
of any remaining $r$ primes in an open interval of length $2n$. Apply it in
consecutive disjoint such intervals. While $r>4$, removal of at least $2\sqrt
r$ decreases the square root of the remainder by at least one; one last block
handles $r\le4$. Hence

$$
h(n)\le2n\bigl(\lceil\sqrt{\pi(n)}\rceil+1\bigr)
 \ll n^{3/2}/\sqrt{\log n}.
$$

This checked specialization recovers the known scale only. The source's full
proof and formalization were not audited or run; pending stronger claims are
not adopted. A prime-specific Hall estimate beating this depletion rate must
treat every subset, not merely count all multiples.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/discrete_geometry/erdos_1981_applications_graph_theory_combinatorial_methods_number/_index|erdos_1981_applications_graph_theory_combinatorial_methods_number]]
- [[../library/discrete_geometry/erdos_1981_applications_graph_theory_combinatorial_methods_number/divisor_matchings_p147|erdos_1981_applications_graph_theory_combinatorial_methods_number / divisor_matchings_p147]]
- [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]]
- [[../library/primes/doorn_2026_optimal_bounds_erdos_problem_matching_integers/_index|doorn_2026_optimal_bounds_erdos_problem_matching_integers]]
- [[../library/primes/erdos_1980_matching_natural_numbers_up_n_distinct/_index|erdos_1980_matching_natural_numbers_up_n_distinct]]
- [[../library/primes/ruzsa_1995_few_multiples_many_primes/_index|ruzsa_1995_few_multiples_many_primes]]
- [[../library/primes/ruzsa_1995_few_multiples_many_primes/theorem|ruzsa_1995_few_multiples_many_primes / theorem]]

<!-- END problem library links -->

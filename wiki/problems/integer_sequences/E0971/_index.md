---
name: problems/integer_sequences/E0971
title: Problem 971
desc: |
  Asks whether some $c>0$ makes the least prime $p(a,d)\equiv a\pmod d$ exceed
  $(1+c)\phi(d)\log d$ for $\gg\phi(d)$ residues $a$, for all large $d$. Two
  2026 proof claims answer yes, one with a Lean development; both are pending
  and unreviewed.
tags:
- Number theory
status: claimed
claim: proved
created: 2026-09-04T09:17:27Z
updated: 2026-10-08T17:47:46Z
---

# Problem 971

[[problems/integer_sequences/_index|..]]

[[problems/integer_sequences/E0971/claims/_index|claims/]]: The 3 claim pages of Problem 971, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $p(a,d)$ be the least prime congruent to $a\pmod{d}$. Does
there exist a constant $c>0$ such that, for all large $d$,

$$
p(a,d) > (1+c)\phi(d)\log d
$$

for $\gg \phi(d)$ many values of $a$?

**Status.** OPEN on erdosproblems.com. Two full proof claims are pending. This
page records the claims without adopting them.

The site's proof-claims tab carries one entry, KyungMin Han's candidate proof of
25 July 2026, made with GPT 5.6 Pro
([[problems/integer_sequences/E0971/claims/2026_07_25_han|claim page]]). It
claims that a positive proportion of reduced classes have least prime beyond
$(1+c)\phi(d)\log d$ for all large $d$, using a second- and third-moment count
of primes in classes. Its Lean file covers only the finite reduction. The
claimant, posting as the forum account Dogcake, labeled the entry a partial
proof claim. The manuscript's main theorem is the full statement, and the full
scope recorded here follows the manuscript. A comment under that entry, dated 28
September 2026, announces Shisheng Li's Lean 4 development proving the
formal-conjectures statement of the problem along a related route
([[problems/integer_sequences/E0971/claims/2026_09_28_li|claim page]]). By its
author's account, it was found with GPT-6 and formalized with Claude, and it has
no `sorry` and uses the standard three axioms. This corpus has not built or
audited it. The tab's disclaimer says that a listing does not mean anyone
associated with the site has examined the proof. No review of either proof is
recorded beyond Li's check of one step of Han's argument, which is recorded on
Han's claim page.

The site's commentary credits Erdős [Er49c] with the assertion along an infinite
sequence of moduli
([[problems/integer_sequences/E0971/claims/1949_01_01_erdos|claim page]],
accepted, partial). The discussion thread holds no proof. A comment of 31
January 2026 derives the answer yes from a uniform prime-tuple hypothesis, by a
Poisson count of primes per class. Two other comments give heuristics and a
literature note on the larger quantity $\max_ap(a,d)$.

**Source.** [erdosproblems.com/971](https://www.erdosproblems.com/971), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #971,
https://www.erdosproblems.com/971.

**References.**

- [Er49c] Erdős, P., On some applications of Brun's method. Acta Univ. Szeged.
  Sect. Sci. Math. (1949), 57-63
  ([[problems/integer_sequences/E0971/claims/1949_01_01_erdos|claim page]]).

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/971.lean).

## Progress

Not yet compiled.

## Known Results

Not yet compiled.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/integer_sequences/li_2016_lower_bound_least_prime_arithmetic_progression/_index|li_2016_lower_bound_least_prime_arithmetic_progression]]
- [[../library/integer_sequences/li_2016_lower_bound_least_prime_arithmetic_progression/theorem_1_1|li_2016_lower_bound_least_prime_arithmetic_progression / theorem_1_1]]
- [[../library/primes/erdos_1949_applications_brun_s_method/_index|erdos_1949_applications_brun_s_method]]
- [[../library/primes/erdos_1949_applications_brun_s_method/theorem_1|erdos_1949_applications_brun_s_method / theorem_1]]
- [[../library/primes/erdos_1949_applications_brun_s_method/theorem_2|erdos_1949_applications_brun_s_method / theorem_2]]

<!-- END problem library links -->

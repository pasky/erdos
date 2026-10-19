---
name: problems/arithmetic_functions/E0414
title: Problem 414
desc: |
  Asks whether, under the map $n\mapsto n+\tau(n)$ with $\tau(n)$ the number of
  divisors, the iterates of any two starting integers eventually reach a common
  value.
tags:
- Number theory
- Iterated functions
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 414

[[problems/arithmetic_functions/_index|..]]

***

**Statement.** Let $h_1(n)=h(n)=n+\tau(n)$ (where $\tau(n)$ counts the number of
divisors of $n$) and $h_k(n)=h(h_{k-1}(n))$. Is it true, for any $m,n$, there
exist $i$ and $j$ such that $h_i(m)=h_j(n)$?

**Status.** Open.

**Source.** [erdosproblems.com/414](https://www.erdosproblems.com/414), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #414,
https://www.erdosproblems.com/414.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/414.lean).

## Current assessment

The annular transfer construction in
[[../library/arithmetic_functions/li_2026_square_annular_dynamics_coalescence_frontiers_n/_index|Li's
Theorem 4.4]] converts coalescence into a precise condition: for every starting
square annulus, some later first-hit transfer image is a singleton. The
construction and this proof were inspected. A bound on static annular width
does not by itself give the dynamic width required by Corollary 5.10.

Theorem 12.2 assumes an eventual two-point frontier, opposite parities when two
points remain, and infinitely many frontiers containing zero. Those hypotheses
remain unproved. The necessary gate equation in Proposition 12.3 is
$\tau((k+1)^2-j)=j$; fixing $j=2$ demands primes $(k+1)^2-2$, and even their
infinitude would not prove reachability of the gates. Variable offsets may
follow another mechanism. Thus the source supplies a representation and
conditional criteria, not a coalescence proof. A finite singleton computation
settles only its specified starts; the universal frontier mechanism is still
missing.

## Known Results

Not yet compiled.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/arithmetic_functions/li_2026_square_annular_dynamics_coalescence_frontiers_n/_index|li_2026_square_annular_dynamics_coalescence_frontiers_n]]
- [[../library/arithmetic_functions/li_2026_square_annular_dynamics_coalescence_frontiers_n/corollary_5_10|li_2026_square_annular_dynamics_coalescence_frontiers_n / corollary_5_10]]
- [[../library/arithmetic_functions/li_2026_square_annular_dynamics_coalescence_frontiers_n/proposition_5_1|li_2026_square_annular_dynamics_coalescence_frontiers_n / proposition_5_1]]
- [[../library/arithmetic_functions/li_2026_square_annular_dynamics_coalescence_frontiers_n/proposition_5_4|li_2026_square_annular_dynamics_coalescence_frontiers_n / proposition_5_4]]
- [[../library/arithmetic_functions/li_2026_square_annular_dynamics_coalescence_frontiers_n/proposition_5_8|li_2026_square_annular_dynamics_coalescence_frontiers_n / proposition_5_8]]
- [[../library/arithmetic_functions/li_2026_square_annular_dynamics_coalescence_frontiers_n/proposition_6_1|li_2026_square_annular_dynamics_coalescence_frontiers_n / proposition_6_1]]
- [[../library/arithmetic_functions/li_2026_square_annular_dynamics_coalescence_frontiers_n/proposition_7_1|li_2026_square_annular_dynamics_coalescence_frontiers_n / proposition_7_1]]
- [[../library/arithmetic_functions/li_2026_square_annular_dynamics_coalescence_frontiers_n/proposition_7_5|li_2026_square_annular_dynamics_coalescence_frontiers_n / proposition_7_5]]
- [[../library/arithmetic_functions/li_2026_square_annular_dynamics_coalescence_frontiers_n/theorem_10_3|li_2026_square_annular_dynamics_coalescence_frontiers_n / theorem_10_3]]
- [[../library/arithmetic_functions/li_2026_square_annular_dynamics_coalescence_frontiers_n/theorem_10_6|li_2026_square_annular_dynamics_coalescence_frontiers_n / theorem_10_6]]
- [[../library/arithmetic_functions/li_2026_square_annular_dynamics_coalescence_frontiers_n/theorem_12_2|li_2026_square_annular_dynamics_coalescence_frontiers_n / theorem_12_2]]
- [[../library/arithmetic_functions/li_2026_square_annular_dynamics_coalescence_frontiers_n/theorem_3_4|li_2026_square_annular_dynamics_coalescence_frontiers_n / theorem_3_4]]
- [[../library/arithmetic_functions/li_2026_square_annular_dynamics_coalescence_frontiers_n/theorem_4_4|li_2026_square_annular_dynamics_coalescence_frontiers_n / theorem_4_4]]
- [[../library/arithmetic_functions/li_2026_square_annular_dynamics_coalescence_frontiers_n/theorem_7_2|li_2026_square_annular_dynamics_coalescence_frontiers_n / theorem_7_2]]
- [[../library/arithmetic_functions/li_2026_square_annular_dynamics_coalescence_frontiers_n/theorem_8_14|li_2026_square_annular_dynamics_coalescence_frontiers_n / theorem_8_14]]
- [[../library/arithmetic_functions/li_2026_square_annular_dynamics_coalescence_frontiers_n/theorem_8_23|li_2026_square_annular_dynamics_coalescence_frontiers_n / theorem_8_23]]
- [[../library/arithmetic_functions/li_2026_square_annular_dynamics_coalescence_frontiers_n/theorem_8_3|li_2026_square_annular_dynamics_coalescence_frontiers_n / theorem_8_3]]
- [[../library/arithmetic_functions/li_2026_square_annular_dynamics_coalescence_frontiers_n/theorem_8_7|li_2026_square_annular_dynamics_coalescence_frontiers_n / theorem_8_7]]

<!-- END problem library links -->

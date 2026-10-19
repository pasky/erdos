---
name: research/erdos_699
title: "Erdős 699: current results and remaining questions"
desc: "A reading guide to the common-prime problem: the original argument, the completed cases, and the five indices that remain open."
created: 2026-09-22T19:09:27Z
updated: 2026-10-19T04:19:07Z
---

# Erdős 699: current results and remaining questions

[[research/_index|..]]

[[research/erdos_699/archive/_index|archive/]]: Superseded bounds and approaches that did not finish the remaining cases, preserved separately from the current reading guide.

[[research/erdos_699/computations/_index|computations/]]: Entry points for checking the completed proofs, with their retained certificates and the earlier computations preserved together.

[[research/erdos_699/evidence/_index|evidence/]]: Exact inputs of the Problem 699 computations kept beside their pages: the
pinned dependency list the interpolation computations were run with.

[[research/erdos_699/methods/_index|methods/]]: A short guide to the divisibility, approximation, nonvanishing, and finite-range arguments used in the current proofs.

[[research/erdos_699/proofs/_index|proofs/]]: The mathematical argument and proof dependencies for i=1,2,7 and every i>=9, with a direct route to the retained certificates.

[[research/erdos_699/remaining/_index|remaining/]]: What is known at indices 3, 4, 5, 6, and 8, and the precise gaps in the current arguments.

***

This folder's results that a claim covers are credited on its claim page; its
other notes that cite no source are author-recorded research, not claims. The
[[research/leads/binomial_common_prime_indices/_index|index-exclusion lead]]
records their route, their conditions and what blocks it.

For every $1\le i<j\le n/2$, must a prime $p\ge i$ divide both
$\binom ni$ and $\binom nj$? A *bad triple* is an admissible triple for
which no such prime exists. The threshold is $p\ge i$, including $p=i$
when $i$ is prime.

**The problem remains open.** The current conclusions are:

| Index $i$ | What is known |
| --- | --- |
| $1,2,7$ and every $i\ge9$ | There are no bad triples. |
| $4,5,6,8$ | There are only finitely many bad triples, but this investigation gives no effective upper bound on their rows. |
| $3$ | Unconditional nonexistence and global finiteness remain open. Assuming rational $abc$, there are only finitely many bad triples. Unconditionally, any bad triple has $n>10^{19}$, $v_2(n)\ge49$, and at least three distinct prime factors in $(n-2)/2$. |

Thus every possible counterexample has $i\in\{3,4,5,6,8\}$. The finite
exceptional sets at $4,5,6,8$ have not been determined and may be empty.
The [conditional cubic argument](remaining/details/cubic_abc.md), together
with fixed-index finiteness for $i\ge4$, shows that rational $abc$ implies
only finitely many bad triples in total. A valid constant $K$ for the single
$abc$ exponent $10/9$ gives $n<10^{263}K^{69}$ at $i=3$.

Van Doorn and Rocca's retained, unpublished manuscripts establish the
fixed-index finiteness theorem for $i\ge4$, settle $i=1,2$, and exclude a
uniform range of large indices. The stronger complete range above and
the additional cubic restrictions are subsequent repository deductions.
The completed small-index proofs use exact computational certificates
and directed analytic estimates; a complete Lean formalization is not
claimed. No claim of novelty is made for the repository deductions.

## Reading guide

These are the main entry points. The proof and remaining-case guides link
the individual arguments only where they are needed.

1. **[Problem statement and sources](../../problems/factorials_binomials/E0699/_index.md).**
   The canonical statement, bibliography, and current status.
2. **[Van Doorn and Rocca's argument](../../../library/factorials_binomials/van_doorn_rocca_2026_partial_progress_erdos_problem_699/_index.md).**
   A theorem-by-theorem account of the retained manuscript, with its full
   text: the local congruences, polynomial divisibility, discriminant
   bound, and the ineffective finiteness theorem.
3. **[Why the completed cases are proved](proofs/_index.md).**
   The mathematical structure of the repository refinements, direct
   references for each completed range, and the scope of the certificates.
4. **[The remaining indices $4,5,6,8$](remaining/_index.md).**
   Current reductions, what prevents an effective bound, and which new
   arithmetic restrictions remain useful.
5. **[The case $i=3$](remaining/index_three.md).**
   The rational $abc$ finiteness argument, the strongest unconditional
   restrictions, and the role of higher Lucas digits.
6. **[Earlier investigations](archive/_index.md).**
   Superseded cutoffs, earlier computations, and approaches that did not
   resolve the remaining cases. These are preserved separately from the
   current reading route.

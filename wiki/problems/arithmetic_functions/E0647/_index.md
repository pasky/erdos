---
name: problems/arithmetic_functions/E0647
title: Problem 647
desc: |
  Asks whether some $n>24$ satisfies $m+\tau(m)\le n+2$ for every $m<n$, where
  $\tau(m)$ is the number of divisors of $m$.
tags:
- Number theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 647

[[problems/arithmetic_functions/_index|..]]

[[problems/arithmetic_functions/E0647/claims/_index|claims/]]: The 1 claim page of Problem 647, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $\tau(n)$ count the number of divisors of $n$. Is there some
$n>24$ such that

$$
\max_{m<n}(m+\tau(m))\leq n+2?
$$

**Status.** Verifiable (the erdosproblems.com label, VERIFIABLE; page last
edited 07 April 2026).

**Source.** [erdosproblems.com/647](https://www.erdosproblems.com/647), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #647,
https://www.erdosproblems.com/647.

**References.**

- [Er79] [[../library/number_theory/erdos_1979_unconventional_problems_number_theory_math_mag/_index|Erdős, Paul, Some unconventional problems in number theory]]. Math. Mag.
  (1979), 67-70.
- [Er79d] Erdős, P., Some unconventional problems in number theory. Acta Math.
  Acad. Sci. Hungar. (1979), 71-80.
- [Er92e] Erdős, Pál, Some Unsolved problems in Geometry, Number Theory and
  Combinatorics. Eureka (1992), 44-48.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/647.lean).

## Current assessment

Bloom's catalog labeled the problem verifiable: a positive answer is witnessed
by one integer $n>24$ together with the finite check of $m+\tau(m)\leq n+2$ for
every $m<n$, so a solution could be confirmed by computation, whereas a negative
answer would need a proof. The problem is Erdős and Selfridge's. The
erdosproblems.com remarks (page last edited 07 April 2026) record that the
inequality holds for $n=24$; that $n+2$ cannot be lowered, since
$\max(\tau(n-1)+n-1,\tau(n-2)+n-2)\geq n+2$ for every $n\ge7$; that Erdős [Er79]
found it extremely doubtful that infinitely many such $n$ exist and suggested
that $\max_{m<n}(\tau(m)+m-n)\to\infty$; that Erdős [Er79d] wrote that it seems
certain, though hopeless with the methods of the time, that for every $k$
infinitely many $n$ satisfy $\max_{n-k<m<n}(m+\tau(m))\leq n+2$, a statement
that follows from Schinzel's Hypothesis H; and that Erdős [Er92e] offered a
prize for an example, the prize erdosproblems.com shows. Tao's comment on the
thread (2025-10-02), repeated in the remarks, places the problem among its
neighbors: since $\tau(m)$ behaves like $2^{\omega(m)}$, it is similar to,
though slightly weaker than, the first part of Problem 679 and much stronger
than Problems 413 and 248. The formal-conjectures file, at its revision of
2026-09-18
([pinned](https://github.com/google-deepmind/formal-conjectures/blob/6fbb54f24ccc2e64dcfaffc28c58950e377110d2/FormalConjectures/ErdosProblems/647.lean)),
states the question and Erdős's two variants as open and proves the case $n=24$
by decision as `erdos_647.variants.twenty_four`.

No result settles an instance of the question, so the folder holds no
accepted or pending claim, and one claim is rejected:
[[problems/arithmetic_functions/E0647/claims/2026_01_18_agbanwa|Agbanwa 2026]],
an AI-assisted Zenodo write-up (first version 2026-01-18) asserting that no
$n>24$ exists, with a Lean file. Terence Tao's reply on the thread
(2026-01-28) found its asymptotic step unproven and only assumed in the
Lean, and its April revision has a gap of its own, as the claim page
records.

The thread's partial results, none of which decides the question:

- Reductions. Sayan Dutta (2026-01-18) derived from the values at
  $m=n-1,n-2,\dots$ that any $n>84$ satisfying the inequality is a multiple
  of $2520$; Kenta Kitamura (2026-05-29) re-derived, within Scott Hughes's
  prime-chain families, Dutta's condition that $(n-3)/3=840N-1$ is prime.
  Scott Hughes (2026-05-27 to 2026-06-08;
  [repository](https://github.com/scottdhughes/erdos647-proof-chain))
  refined the modular reduction to $n=2520N$ with $N$ in $41$ residue classes
  modulo $46189$, which the repository states is checked in Lean, and gave a
  prime-chain reduction to two explicit families, from which the Brun sieve
  bounds the number $|C(x)|$ of solutions up to $x$ by $x/(\log x)^7$ up to a
  constant; companion manuscripts described as submitted claim
  $|C(x)|\leq x\exp(-(\log\log x)^{2-o(1)})$. A density bound does not decide
  whether $C$ is empty.
- Searches without a proof certificate. OEIS
  [A087280](https://oeis.org/A087280) records no solution in $(24,10^{10}]$;
  Patrik Idén's report
  ([Zenodo](https://doi.org/10.5281/zenodo.20677388), 2026-06-13, revised
  2026-06-30 and 2026-07-02) extends this to $10^{12}$ (the minimum gap of
  $224$ that it reports, near $n=10^{11}$, is the least of the values its log
  prints at multiples of $10^{10}$, not a minimum over the range: the gap
  $\max_{m<n}(m+\tau(m))-n$ falls to $3$, first at $n=35$); Hughes's frontier
  certificate (2026-06-15) covers $n\leq6.15\times10^{17}$, and the thread
  (2026-09-10) credits Hughes and bentrd with a frontier near
  $9.17\times10^{18}$; veljjanoski's GPU search
  ([repository](https://github.com/veljjanoski/erdos647)) found no solution
  up to $10^{20}$ (2026-09-10) and then up to $10^{22}$ (2026-09-13).
- Kernel-checked exclusions. Ibrahim Mian's Lean development (thread,
  2026-08-17; [repository](https://github.com/ibrahimmian36/decanus)) proves
  from stored factorization witnesses that no solution lies in $(24,10^8]$;
  the preprint of Mian and Siddique,
  [arXiv:2608.17880](https://arxiv.org/abs/2608.17880) (2026-08-18), extends
  the kernel-checked range to $10^9$; eerot's development (2026-10-04;
  [repository](https://github.com/fjordmindlabs/math/tree/main/erdos647-sparse))
  reaches $10^{13}$.

A finite exclusion, however checked, leaves the existence question open, and
the thread records no further proof attempt. Beyond these results the
mathematics of the problem is unassessed in this wiki.

Search scope: the erdosproblems.com problem page and remarks, its discussion
thread (18 comments on 2026-10-07) and its empty proof-claims tab, the community
database entry, the formal-conjectures file, the Zenodo records and repositories
linked from the thread, and the arXiv record of Mian and Siddique. MathSciNet
and zbMATH were not searched and X was not used.

## Prime-factor and interval interface

For any proposed $n$, the exact inequalities are $\tau(n-j)\le j+2$ for $1\le
j<n$. Since $\tau(m)\le2\sqrt m$, all offsets with $j+2\ge2\sqrt n$ are
automatic, including equality. Thus only $j+2<2\sqrt n$ require factorization.
This is a complete finite checking window for a fixed candidate, not a global
bound on $n$.

For $n>84$, the first four offsets force $24\mid n$ and primality of
$n-1,(n-2)/2,(n-3)/3,(n-4)/4$. Indeed $j=1$ forces $n$ even; $j=2$ makes
$n-2=2q$ with $q$ odd prime, hence $4\mid n$. The alternatives
$n\equiv1,2\pmod3$ force respectively $n-1\in\{3,9\}$ or $q=3$, so $3\mid n$.
If $n\equiv4\pmod8$, the bound at $j=4$ makes $n-4$ a power of two at most
$32$, impossible. Thus $24\mid n$. Now $n-1\equiv23\pmod{24}$ cannot be a prime
square; the bound at $j=3$ excludes pure powers of three above $81$ and forces
$(n-3)/3$ prime; the exact valuation $v_2(n-4)=2$ forces $(n-4)/4$ prime.

These author-recorded necessary conditions are weaker than the previously
reported $2520$ and seven-prime reductions. No search or external exclusion
range was replayed. A solution still needs every offset in the checking window,
or a proof that no candidate can pass it.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/number_theory/erdos_1979_unconventional_problems_number_theory_math_mag/_index|erdos_1979_unconventional_problems_number_theory_math_mag]]

<!-- END problem library links -->

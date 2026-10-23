---
name: problems/arithmetic_functions/E0420
title: Problem 420
desc: |
  Asks whether $\tau((n+\lfloor(\log n)^C\rfloor)!)/\tau(n!)$ tends to infinity
  for large $C$, where $\tau$ counts divisors.
tags:
- Number theory
status: open
claim: none
parts: [divergence, logarithmic_density, monotone_density]
created: 2026-09-04T09:17:27Z
updated: 2026-10-23T17:38:29Z
---

# Problem 420

[[problems/arithmetic_functions/_index|..]]

[[problems/arithmetic_functions/E0420/claims/_index|claims/]]: The 1 claim page of Problem 420, one per claimant's result; the problem's standing derives from them.

***

**Statement.** If $\tau(n)$ counts the number of divisors of $n$ then let

$$
F(f,n)=\frac{\tau((n+\lfloor f(n)\rfloor)!)}{\tau(n!)}.
$$

Is it true that

$$
\lim_{n\to \infty}F((\log n)^C,n)=\infty
$$

for large $C$?

Is it true that $F(\log n,n)$ is everywhere dense in $(1,\infty)$?

More generally, if $f(n)\leq \log n$ is a monotonic function such that $f(n)\to
\infty$ as $n\to \infty$, then is $F(f,n)$ everywhere dense?

**Status.** Open.

**Source.** [erdosproblems.com/420](https://www.erdosproblems.com/420), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #420,
https://www.erdosproblems.com/420.

**References.**

- [EGIP96] Erdős, Paul and Graham, S. W. and Ivić, Aleksandar and Pomerance,
  Carl, On the number of divisors of $n!$. (1996), 337-355.

**Formalization.** Plasma AI's
[erdos-420](https://github.com/plasma-ai/erdos-420) supplies Lean proofs of the
two density questions, with every-tail density for a nondecreasing shift
bounded by $\log n$ eventually. The
[[problems/arithmetic_functions/E0420/claims/2026_10_23_plasma_ai|partial claim]]
records their scope and acceptance evidence. The divergence question is not
formalized there.

## Current assessment

The two density questions have an
[[problems/arithmetic_functions/E0420/claims/2026_10_23_plasma_ai|accepted partial claim]].
The first question remains open; the following author-recorded reduction
identifies a sufficient and necessary short-interval estimate for it.

Let $h\ge0$ be an integer with $h=o(\sqrt n)$.
[[../library/factorials_binomials/erdos_1996_number_divisors/_index|Erdős–Graham–Ivić–Pomerance,
Theorem 2]] gives

$$
\frac{\tau(t!)}{\tau((t-1)!)}=1+\frac{P^+(t)}t+O(t^{-1/2}).
$$

Both quantities inside the logarithmic comparison are at least one, where
logarithm is Lipschitz. Multiplication and telescoping therefore give

$$
\log\frac{\tau((n+h)!)}{\tau(n!)}
 =\sum_{i=1}^h\log\left(1+\frac{P^+(n+i)}{n+i}\right)
   +O(h/\sqrt n).
$$

Using $a/2\le\log(1+a)\le a$ for $0\le a\le1$ and $(n+i)/n=1+o(1)$ uniformly,
one obtains the exact divergence equivalence

$$
\frac{\tau((n+h)!)}{\tau(n!)}\longrightarrow\infty
\quad\Longleftrightarrow\quad
\frac1n\sum_{i=1}^hP^+(n+i)\longrightarrow\infty.
$$

Every fixed polylogarithmic $h$ is allowed. The source theorem and its proof
were followed; this deduction is author-recorded, without independent review.
For the open divergence question, the missing input is a lower bound showing
that $n^{-1}\sum_{i\le\lfloor(\log n)^C\rfloor}P^+(n+i)\to\infty$ for some
fixed $C$. The global asymptotic for $\log\tau(n!)$ cannot be differenced at
this scale using its stated fixed-order error.

## Known Results

The estimates of Erdős, S. W. Graham, Ivić and Pomerance give
$\liminf F(c\log n,n)=1$ for each fixed $c>0$, from the averaging estimate
in [[../library/factorials_binomials/erdos_1996_number_divisors/theorem_3|the proof of Theorem 3]],
and $F(n^{4/9},n)\to\infty$, from
[[../library/factorials_binomials/erdos_1996_number_divisors/lemma_3|Lemma 3]].
The linked pages spell out these consequences beyond the stated doubling
bounds, with their reading and review limitations.

**Normal-order correction.** The assertion that $F(f,n)\sim1$ for almost
all $n$ whenever $f=o((\log n)^2)$ is false. It appears in the authors'
manuscript, p. 5, and is repeated in the
[erdosproblems.com remarks](https://www.erdosproblems.com/420) (accessed
2026-10-22). The manuscript's adjacent assertion of a finite constant normal
order at $f(n)\sim c\log n$ is also false. A positive proportion of
logarithmic windows give $F(c\log n,n)\ge2^m$ for each fixed $m$.
The [[../library/factorials_binomials/erdos_1996_number_divisors/_index|source card]]
records the obstruction using Mastrostefano's Theorem 1.1 and an averaging
proof of the valid replacement: $F(f,n)\to1$ on a density-one set for
eventually nonnegative $f=o(\log n)$. These deductions are author-recorded,
without independent review. The first question, divergence for sufficiently
large fixed $C$, remains open; these corrections do not resolve it.

[[problems/arithmetic_functions/E0420/claims/2026_10_23_plasma_ai|Plasma AI's density claim]]
answers the two density questions through the formalization documented on
[[../library/arithmetic_functions/plasma_ai_2026_divisor_counts_shifted_factorials/_index|its source card]].
The claim was accepted on its formalization on 2026-10-20, after independent
rebuilding, complete kernel replay and a graded statement-fidelity review. It
proves density even after any finite initial segment is removed, and assumes
$f(n)\le\log n$ only eventually.
The first question, divergence for sufficiently large fixed $C$, remains
unresolved by this result.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/arithmetic_functions/plasma_ai_2026_divisor_counts_shifted_factorials/_index|plasma_ai_2026_divisor_counts_shifted_factorials]]
- [[../library/arithmetic_functions/plasma_ai_2026_divisor_counts_shifted_factorials/density_theorem|plasma_ai_2026_divisor_counts_shifted_factorials / density_theorem]]
- [[../library/factorials_binomials/erdos_1996_number_divisors/_index|erdos_1996_number_divisors]]
- [[../library/factorials_binomials/erdos_1996_number_divisors/corollary_2|erdos_1996_number_divisors / corollary_2]]
- [[../library/factorials_binomials/erdos_1996_number_divisors/corollary_3|erdos_1996_number_divisors / corollary_3]]
- [[../library/factorials_binomials/erdos_1996_number_divisors/lemma_1|erdos_1996_number_divisors / lemma_1]]
- [[../library/factorials_binomials/erdos_1996_number_divisors/lemma_3|erdos_1996_number_divisors / lemma_3]]
- [[../library/factorials_binomials/erdos_1996_number_divisors/theorem_1|erdos_1996_number_divisors / theorem_1]]
- [[../library/factorials_binomials/erdos_1996_number_divisors/theorem_3|erdos_1996_number_divisors / theorem_3]]
- [[../library/factorials_binomials/erdos_1996_number_divisors/theorem_4|erdos_1996_number_divisors / theorem_4]]

<!-- END problem library links -->

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
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 420

[[problems/arithmetic_functions/_index|..]]

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

**Formalization.** None recorded.

## Current assessment

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
Its missing input is a uniform lower sum in every polylogarithmic interval. For
the density questions one needs the exact logarithmic sum, since the factor-two
comparison does not preserve limit values. The global asymptotic for
$\log\tau(n!)$ cannot be differenced at this scale using its stated fixed-order
error.

## Known Results

Not yet compiled.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/factorials_binomials/erdos_1996_number_divisors/_index|erdos_1996_number_divisors]]
- [[../library/factorials_binomials/erdos_1996_number_divisors/corollary_2|erdos_1996_number_divisors / corollary_2]]
- [[../library/factorials_binomials/erdos_1996_number_divisors/corollary_3|erdos_1996_number_divisors / corollary_3]]
- [[../library/factorials_binomials/erdos_1996_number_divisors/lemma_1|erdos_1996_number_divisors / lemma_1]]
- [[../library/factorials_binomials/erdos_1996_number_divisors/lemma_3|erdos_1996_number_divisors / lemma_3]]
- [[../library/factorials_binomials/erdos_1996_number_divisors/theorem_1|erdos_1996_number_divisors / theorem_1]]
- [[../library/factorials_binomials/erdos_1996_number_divisors/theorem_3|erdos_1996_number_divisors / theorem_3]]
- [[../library/factorials_binomials/erdos_1996_number_divisors/theorem_4|erdos_1996_number_divisors / theorem_4]]

<!-- END problem library links -->

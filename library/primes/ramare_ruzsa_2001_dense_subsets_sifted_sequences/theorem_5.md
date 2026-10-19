---
name: primes/ramare_ruzsa_2001_dense_subsets_sifted_sequences/theorem_5
title: Theorem 5 — improved large sieve for sifted sequences
desc: |
  The two-level Fourier bound with factor G_1(Q_0)/G_1(Q/Q_0) and
  enlarged-level cost N+Q squared, with its exact support hypotheses.
created: 2026-10-17T05:23:58Z
updated: 2026-10-17T05:23:58Z
---

# Theorem 5 — improved large sieve for sifted sequences

***

Assume the [[primes/ramare_ruzsa_2001_dense_subsets_sifted_sequences/g_functions|supporting compact and Johnsen condition]].
Let $N\geq1$ be an integer and let $\varphi_1,\ldots,\varphi_N$ be
complex numbers, extended by zero outside $[1,N]$, supported by
$\mathcal K$ up to level $Q$. For $1\leq Q_0\leq Q$,

$$
\sum_{q\leq Q_0}\ \sum_{\substack{a\bmod q\\(a,q)=1}}
\left|\sum_{n=1}^N\varphi_n e(na/q)\right|^2
\leq
\frac{G_1(Q_0)}{G_1(Q/Q_0)}(N+Q^2)
\sum_{n=1}^N|\varphi_n|^2.
$$

The Fourier sum stops at $Q_0$, but the support condition must hold through
$Q$. The denominator is $G_1(Q/Q_0)$, not $G_1(Q)$, and the quadratic
cost uses $Q$, not $Q_0$.

The proof on p. 571 compares the nonnegative decomposition in
[[primes/ramare_ruzsa_2001_dense_subsets_sifted_sequences/theorem_4|Theorem 4]]
at the two levels. Lemma 1 bounds the coefficient ratio by
$G_1(Q_0)/G_1(Q/Q_0)$; the ordinary large sieve bounds the energy at
level $Q$ by $(N+Q^2)\sum_n|\varphi_n|^2$.

For an application to [[../wiki/problems/integer_sequences/E0012/_index|Problem 12(iii)]],
the residue-support system, its uniform lifting, both G-function estimates
and the enlarged quadratic cost remain separate requirements. The theorem
itself gives no bound for a property-P set's joint divisor exclusions.

**Source and reading.** Theorem 5 and its proof, printed p. 571 of
[[primes/ramare_ruzsa_2001_dense_subsets_sifted_sequences/_index|Ramaré–Ruzsa (2001)]].
The statement and parameter dependence were checked against the scan. The
short proof and its cited interfaces were read; no independent proof audit
of the large-sieve input or the complete paper is asserted.

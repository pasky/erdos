---
name: primes/ramare_ruzsa_2001_dense_subsets_sifted_sequences/theorem_4
title: Theorem 4 — Fourier-energy identity
desc: |
  The exact nonnegative decomposition of reduced-fraction Fourier energy
  for a sequence supported by a compact satisfying uniform lifting.
created: 2026-10-17T05:23:58Z
updated: 2026-10-17T05:23:58Z
---

# Theorem 4 — Fourier-energy identity

***

Use the [[primes/ramare_ruzsa_2001_dense_subsets_sifted_sequences/g_functions|support and G-function conventions]].
Assume the Johnsen uniform-lifting condition. For a finitely supported
complex sequence $(\varphi_n)_{n\geq1}$ supported by $\mathcal K$ up to
level $Q\geq1$, put

$$
T_\ell(b)=\sum_{n\equiv b\pmod\ell}\varphi_n,
\qquad
\Theta(q)=|\mathcal K_q|\sum_{b\in\mathcal K_q}
\left|\sum_{\ell\mid q}\mu(q/\ell)
       \frac{|\mathcal K_\ell|}{|\mathcal K_q|}T_\ell(b)\right|^2.
$$

Then

$$
\sum_{q\leq Q}\ \sum_{\substack{a\bmod q\\(a,q)=1}}
\left|\sum_n\varphi_n e(na/q)\right|^2
=\sum_{q\leq Q}G_q(Q)\Theta(q).
$$

The numerator in the inner divisor sum is $|\mathcal K_\ell|$, and its
denominator is $|\mathcal K_q|$. The sum over $b$ runs over
$\mathcal K_q$, whereas the inner residue condition is modulo $\ell$.
All positive integer moduli up to $Q$ occur, including prime powers; the
sum is not restricted to squarefree moduli. At $q=1$ the reduced residue
sum has its single usual term.

**Source and reading.** Theorem 4, printed p. 569, with proof on p. 570 of
[[primes/ramare_ruzsa_2001_dense_subsets_sifted_sequences/_index|Ramaré–Ruzsa (2001)]].
The statement and its support hypotheses were checked against the scan;
the proof was read for the residue-fiber and nonnegative-energy interfaces,
without an independent proof audit. The theorem assumes uniform lifting,
not just multiplicative splitting.

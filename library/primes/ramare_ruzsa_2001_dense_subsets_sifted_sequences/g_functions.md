---
name: primes/ramare_ruzsa_2001_dense_subsets_sifted_sequences/g_functions
title: Supporting compact and G-functions
desc: |
  Exact residue-support, uniform-lifting and G-function conventions from
  Section 4.1, including the comparison used in the improved large sieve.
created: 2026-10-17T05:23:58Z
updated: 2026-10-17T05:23:58Z
---

# Supporting compact and G-functions

***

The conventions below are from Section 4.1, printed pp. 567–569 of
[[primes/ramare_ruzsa_2001_dense_subsets_sifted_sequences/_index|Ramaré–Ruzsa (2001)]].
Write $e(t)=\exp(2\pi i t)$.

## Residue support and uniform lifting

Let $\mathcal K$ be a nonempty compact subset of $\widehat{\mathbb Z}$
whose images $\mathcal K_d\subseteq\mathbb Z/d\mathbb Z$ split under the
Chinese remainder theorem for coprime moduli. In particular, the nonempty
sets $\mathcal K_{p^\nu}$ are compatible under reduction, and
$\mathcal K_d$ is the product of its prime-power factors. Set
$|\mathcal K_1|=1$.

A complex sequence $(\varphi_n)_{n\geq1}$ is supported by $\mathcal K$
up to level $D$ when

$$
\varphi_n\ne0\quad\Longrightarrow\quad
 n\bmod d\in\mathcal K_d\quad\text{for every integer }1\leq d\leq D.
$$

This is equation (4.1.1). The Johnsen condition (4.1.12) additionally
requires, for every prime $p$ and integer $\nu\geq1$, that

$$
\#\{b\in\mathcal K_{p^{\nu+1}}:b\equiv a\pmod {p^\nu}\}
$$

be independent of $a\in\mathcal K_{p^\nu}$. Compatibility of images alone
is not this uniform-lifting condition.

## The G-functions

For an integer $d\geq1$ and real $z>0$, equation (4.1.3) defines

$$
G_d(z)=\sum_{\substack{q\leq z\\d\mid q}}
       \ \sum_{d\mid f\mid q}\mu(q/f)\frac{f}{|\mathcal K_f|}.
$$

The equivalent nonnegative formulation (4.1.5)–(4.1.6) is

$$
h(1)=1,\qquad
h(\delta)=\prod_{p^\nu\parallel\delta}
\left(\frac{p^\nu}{|\mathcal K_{p^\nu}|}
      -\frac{p^{\nu-1}}{|\mathcal K_{p^{\nu-1}}|}\right)\geq0,
\qquad
G_d(z)=\sum_{\substack{\delta\leq z\\[d,\delta]\leq z}}h(\delta),
$$

where $[d,\delta]$ denotes the least common multiple. Thus
$G_1(z)=\sum_{\delta\leq z}h(\delta)$, and $G_1(z)\geq1$ for $z\geq1$.
Lemma 1 on p. 568 states that, for $\ell\mid d$,

$$
G_\ell(z\ell/d)\leq G_d(z)\leq G_\ell(z).
$$

These are the G-functions used in
[[primes/ramare_ruzsa_2001_dense_subsets_sifted_sequences/theorem_4|Theorem 4]]
and [[primes/ramare_ruzsa_2001_dense_subsets_sifted_sequences/theorem_5|Theorem 5]].
They depend on the entire specified residue-support system. No asymptotic
estimate for them is implied merely by this definition.

**Reading.** Definitions and Lemma 1 checked against printed pp. 567–569;
no independent verification of the full sieve argument is asserted.

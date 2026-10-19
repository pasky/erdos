---
name: primes/goldston_pintz_yildirim_2011_small_prime_gaps
title: Positive proportion of small gaps between consecutive primes
desc: |
  Goldston, Pintz and Yıldırım show that gaps below any fixed positive
  multiple of the average spacing occur with positive lower proportion;
  this is a comparison input for consecutive-prime arguments.
license: reserved
created: 2026-10-15T21:52:47Z
updated: 2026-10-15T21:57:54Z
---

# Positive proportion of small gaps between consecutive primes

[[primes/_index|..]]

***

D. A. Goldston, J. Pintz and C. Y. Yıldırım, *Positive Proportion of Small
Gaps Between Consecutive Primes*. The selected text is
[arXiv:1103.3986v1](https://arxiv.org/abs/1103.3986v1), posted
21 March 2011. The source PDF is available from
[arXiv](https://arxiv.org/pdf/1103.3986v1).

The [arXiv record](https://arxiv.org/abs/1103.3986v1), read 2026-10-15,
specifies arXiv's non-exclusive distribution license. This does not grant
redistribution under an open license. No file of this source is held.

## Scope

Write $p_n$ for the $n$th prime and $\pi(x)$ for the prime-counting function.
Theorem 1 states that, for each fixed $\eta>0$,

$$
\frac{\#\{p_n\leq x:p_{n+1}-p_n\leq\eta\log p_n\}}{\pi(x)}
\gg_\eta 1
$$

as $x\to\infty$. The fixed-$\eta$ condition matters: the theorem does not
assert a positive lower proportion uniform as $\eta\to0$. The introduction
separately labels stronger distribution-dependent results and an
Elliott–Halberstam-dependent result for triples.

**Read status: claims checked.** The introduction, the definition of its
counting function and Theorems 1–4 were read in the arXiv TeX source at statement
depth. Their proofs have not been checked here.

**Bears on.** [[../wiki/problems/irrationality/E0251/_index|Problem 251]]:
this is a comparison for assumptions about short consecutive-prime gaps. The
pair-counting result alone does not specify long residue patterns or prove the
irrationality of the prime-weighted binary series.

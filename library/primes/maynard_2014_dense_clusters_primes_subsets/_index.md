---
name: primes/maynard_2014_dense_clusters_primes_subsets
title: Dense clusters of primes in subsets
desc: |
  Maynard obtains clusters from distribution hypotheses and gives a
  quantitative theorem for consecutive primes in one residue class, with
  explicit growing ranges for the run length and modulus.
license: reserved
created: 2026-10-15T21:52:47Z
updated: 2026-10-15T21:57:54Z
---

# Dense clusters of primes in subsets

[[primes/_index|..]]

***

James Maynard, *Dense clusters of primes in subsets*. The selected text is
[arXiv:1405.2593v2](https://arxiv.org/abs/1405.2593v2), revised
16 December 2014. The source PDF is available from
[arXiv](https://arxiv.org/pdf/1405.2593v2).

The [arXiv record](https://arxiv.org/abs/1405.2593v2), read 2026-10-15,
specifies arXiv's non-exclusive distribution license. This does not grant
redistribution under an open license. No file of this source is held.

## Scope

The general theorem produces several simultaneous primes from suitable
arithmetic-progression estimates for the ambient sets. The application relevant
to consecutive residue patterns is Theorem 3.3. For fixed $\epsilon>0$, it
gives a constant $c_\epsilon>0$ such that, when $x>x_0(\epsilon,q)$,

$$
\#\{p_n\leq x:p_n\equiv\cdots\equiv p_{n+m}\equiv a\pmod q,
\ p_{n+m}-p_n\leq\epsilon\log x\}
\gg_\epsilon\frac{\pi(x)}{(2q)^{\exp(Cm)}}
$$

uniformly for $m\leq c_\epsilon\log\log x$,
$q\leq(\log x)^{1-\epsilon}$ and $(a,q)=1$, with an absolute constant
$C>0$. These are $m+1$ consecutive primes, all in the same residue class.
For fixed $m,q$ the lower bound is a positive proportion of the primes.

**Read status: claims checked.** The abstract, introduction and Theorem 3.3,
including its parameter ranges and counting convention, were read in the arXiv
TeX source. Its proof and the general sieve theorem have not been verified here.

**Bears on.** [[../wiki/problems/irrationality/E0251/_index|Problem 251]]:
Theorem 3.3 supplies a comparison for proposed consecutive-prime pattern inputs.
It concerns constant residue runs and does not itself provide the weighted
parity or prescribed-pattern estimates that a particular irrationality argument
would need.

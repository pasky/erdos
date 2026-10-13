---
name: problems/factorials_binomials/E0683/claims/1973_01_01_jutila_ramachandra_shorey
title: The Jutila-Ramachandra-Shorey bound in binomial form
desc: |
  Jutila, Ramachandra and Shorey's refereed bound on the function of Problem
  961, attested by Erdős's 1976 survey, gives by the 1955 claim's deduction
  $P(\binom nk)\gg\min(n-k+1,k\log k\log\log k/\log\log\log k)$ for
  $k\le n/2$.
authors:
- M. Jutila
- K. Ramachandra
- T. N. Shorey
status: accepted
claim: proved
scope: partial
evidence:
- refereed
submitted: null
links:
- url: https://doi.org/10.4064/aa-24-1-99-111
  kind: paper
- url: https://doi.org/10.4064/aa-25-4-365-373
  kind: paper
- url: https://www.erdosproblems.com/961
  kind: discussion
created: 2026-10-13T13:29:21Z
updated: 2026-10-13T13:29:21Z
---

***

**Claim.** For $1\le k\le n/2$,

$$
P\left(\binom nk\right)\gg\min\left(n-k+1,\frac{k\log k\log\log k}{\log\log\log
k}\right).
$$

This is a consequence, derived here, of the bound

$$
f(m)<c_1\frac{m\log\log\log m}{\log m\log\log m}
$$

of Jutila, Ramachandra and Shorey, where $f(m)$ is the least $L$ such that
every block of $L$ consecutive integers, each greater than $m$, contains a
multiple of a prime greater than $m$, the function of
[[problems/integer_sequences/E0961/_index|Problem 961]] and of Theorem 1 of
[Er55d]. The bound is display (1) on printed p. 271 of Erdős's survey
*Problems and results on consecutive integers*, Publ. Math. Debrecen 23
(1976), 271--282
([[../library/primes/erdos_1976_problems_results_consecutive_integers/inequality_1|result page]]),
which credits it to Jutila, Ramachandra and Shorey: M. Jutila, *On numbers
with a large prime factor. II*, J. Indian Math. Soc. (N.S.) 38 (1974),
125--130; K. Ramachandra and T. N. Shorey, *On gaps between numbers with a
large prime factor*, Acta Arith. 24 (1973), no. 1, 99--111; and T. N.
Shorey, *On gaps between numbers with a large prime factor. II*, Acta Arith.
25 (1974), no. 4, 365--373. None of the three states a binomial form.

The deduction is that of the
[[problems/factorials_binomials/E0683/claims/1955_01_01_erdos|1955 claim page]],
with this bound in place of Erdős's $f(m)\le c_1m/\log m$. For $k\le n/2$ the
$k$ members of the numerator block $n-k+1,\ldots,n$ of $\binom nk$ all exceed
$n-k\ge k$, and a prime greater than $k$ dividing one of them is not canceled
by $k!$, so it divides $\binom nk$. Write $g(m)$ for the right side of the
bound, which increases for large $m$, and $m_k$ for the largest $m$ with
$g(m)\le k$, of order $k\log k\log\log k/\log\log\log k$. If $n-k\le m_k$,
then $f(n-k)<g(n-k)\le k$, so the block contains a multiple of a prime greater
than $n-k$, and $P(\binom nk)\ge n-k+1$. Otherwise every member of the block
exceeds $m_k$ and $f(m_k)<k$, so $P(\binom nk)>m_k$. The finitely many small
$k$ are absorbed in the implied constant.

**Covers.** The instances with $k\le n/2$ and $n-k$ at most a constant
multiple of $k\log k\log\log k/\log\log\log k$, where $P(\binom nk)\ge n-k+1$
and the inequality of the problem, read as its Formulation states, holds for
every $c>0$. This widens the range of the 1955 claim by the factor
$\log\log k/\log\log\log k$. Elsewhere the bound gives only
$P(\binom nk)\gg k\log k\log\log k/\log\log\log k$, no bound of the form
$k^{1+c}$; those instances stay open.

**Depends on.**
[[problems/integer_sequences/E0961/claims/1973_01_01_jutila_ramachandra_shorey|The accepted claim on Problem 961]],
for the bound on $f$; the step to $\binom nk$ above is this page's.

**Acceptance.** Refereed: the bound appeared in Acta Arithmetica and in the
Journal of the Indian Mathematical Society, as Erdős's 1976 survey attests.
The papers are not held, so the bound's exact statements and hypotheses rest
on that attestation and the site's, as on the Problem 961 claim page. The
site's page for Problem 683 does not cite the papers; it calls the problem
essentially equivalent to Problem 961, whose commentary credits the bound.
The step from $f$ to $\binom nk$ is the elementary deduction of the 1955
claim page, made here without separate review. The site labeled the problem
OPEN, so its commentary gives no `reviewed` evidence.

---
name: research/finite_experiments/binomial_gcd_search
title: Binomial GCD Thresholds Through Order Thirty
desc: |
  Exact finite checks of the common-prime threshold for binomial coefficients,
  distinguishing the erdosproblems.com inequality from four strict-variant
  exceptions.
tags: []
sources:
- problems/factorials_binomials/E0699
created: 2026-09-08T18:16:13Z
updated: 2026-10-14T07:06:52Z
---

# Binomial GCD Thresholds Through Order Thirty

[[research/finite_experiments/_index|..]]

[[research/finite_experiments/binomial_gcd_search/evidence/_index|evidence/]]: Exact enumeration of the binomial-gcd thresholds through order thirty,
using the stated finite domain and inline arithmetic witnesses.

***

## Question and finite scope

The [[problems/factorials_binomials/E0699/_index|E0699 problem page]], using the
erdosproblems.com formulation accessed, asks:

Is it true that for every $1\leq i<j\leq n/2$ there exists some
prime $p\geq i$ such that

$$
p\mid \textrm{gcd}\left(\binom{n}{i}, \binom{n}{j}\right)?
$$

This experiment checks every integer triple in the finite domain

$$
4\le n\le30,\qquad 1\le i<j\le\lfloor n/2\rfloor.
$$

It also tests the **strict variant**, which replaces $p\ge i$ with $p>i$.
The exact computation finds different answers on this domain. The
non-strict threshold holds on all 1,015 triples, while the strict
threshold fails exactly at

$$
(10,3,5),\quad(16,2,6),\quad(28,3,14),\quad(28,5,14).
$$

The listed failure set is fixed as the expectation before the checker runs.
Ordinary and optimized runs compute it from the stated integer formulas,
without reading stored outputs. This is author-checked finite coverage, not
independent acceptance.

## Exact enumeration and witnesses

The [native check](evidence/main.py) computes each binomial row with
`math.comb`, then computes every required gcd with `math.gcd`. Trial division
through the integer square root lists the primes through thirty. For each
gcd it checks divisibility by those primes at the two thresholds.

This prime list is complete for the task. If a prime divides $\binom nk$,
then it divides $n!=\binom nk\,k!\,(n-k)!$, so it is at most $n$.
The exhaustive loops include both parity cases for $n$, $i=1$, and the
endpoint $j=\lfloor n/2\rfloor$. Their number of triples is

$$
\sum_{n=4}^{30}\binom{\lfloor n/2\rfloor}{2}
=2\sum_{h=2}^{14}\binom h2+\binom{15}2
=2\binom{15}3+105=1015.
$$

There are no eligible pairs for $n<4$. The count is a coverage check; the
explicit loops, prime-divisor argument, and exact predicates supply the
connection to the finite question.

The following exact witnesses can also be checked directly from the
factorial formula for binomial coefficients:

| $(n,i,j)$ | $\binom ni$ | $\binom nj$ | Their gcd |
| --- | ---: | ---: | --- |
| $(4,1,2)$ | 4 | 6 | $2$ |
| $(10,3,5)$ | 120 | 252 | $12=2^2\cdot3$ |
| $(16,2,6)$ | 120 | 8008 | $8=2^3$ |
| $(28,3,14)$ | 3276 | 40116600 | $36=2^2\cdot3^2$ |
| $(28,5,14)$ | 98280 | 40116600 | $1080=2^3\cdot3^3\cdot5$ |

For the last two rows,

$$
\binom{28}{14}=2^3\cdot3^3\cdot5^2\cdot17\cdot19\cdot23,
$$

whereas $\binom{28}{3}=2^2\cdot3^2\cdot7\cdot13$ and
$\binom{28}{5}=2^3\cdot3^3\cdot5\cdot7\cdot13$.
Minimum prime exponents give the displayed gcds. Each exception has largest
common prime exactly $i$, so it satisfies the erdosproblems.com threshold and
fails the strict one. The first row supplies a strict success. These individual
witnesses alone do not exclude further exceptions.

## Reproduction and standing

From the repository root, with its locked environment installed, run:

```sh
uv run --no-sync python wiki/research/finite_experiments/binomial_gcd_search/evidence/main.py
```

The default is the full declared domain; there is no reduced mode. It uses
Python integers, the standard library and the root `tools` package. All
inputs are the stated bounds and small witness constants in the new
implementation. It reads no input files, depends on no external output or
source manifest, and writes no files. No asset packet is required.

The observed full run finished in about 0.05 seconds, including command
startup, under a 60-second external limit. The optimized run also completed
with the same failure sets and `ALL CHECKS PASS (10 checks)`. The program
prints both observed failure sets, checks the exact witnesses and domain
count, and exits nonzero if any required result fails, including under
`python -O`. A strict exception is an expected observation; an additional
exception or any non-strict failure makes the declared finite classification
fail. Interrupted execution establishes no complete coverage.

The failure protocol was checked with the actual classifier on $(10,3,5)$:
requiring its false strict predicate produced a named failed obligation and
exit code 1 under both ordinary and optimized Python. The prime-list checks
also reject 1 and the composite divisor 6 as prime witnesses.

The arithmetic and exhaustive classification are author-recorded and have no
independent review or formal-verification standing. No all-order result
follows from this finite domain, and the strict exceptions do not disprove
the erdosproblems.com question. This account changes no problem status and
claims no new computational frontier or current literature assessment.

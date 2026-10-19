---
name: research/leads/rational_ratio_dyadic_floor_descent/evidence
title: Evidence
desc: |
  Exact finite completeness certificates for specific two-ray dyadic floor
  sets with rational ratio, recomputed by one entry point: the pinned
  pairs, a sweep over thirty-two rational coefficients, and an incomplete
  control pair.
tags: []
sources: []
created: 2026-09-28T06:40:00Z
updated: 2026-09-28T06:40:00Z
---

# Evidence

[[research/leads/rational_ratio_dyadic_floor_descent/_index|..]]

***

The [entry point](main.py) recomputes the finite certificates that the
[[research/leads/rational_ratio_dyadic_floor_descent/_index|lead]] and the
[[research/erdos_354/connections|connections page]] record. It uses the
root Python environment and the shared `Checker`, reads no files and
writes no output. Run it from the repository root:

```sh
uv run --no-sync python wiki/research/leads/rational_ratio_dyadic_floor_descent/evidence/main.py
```

A certificate for a normalized pair $(\alpha,\beta)$ is a depth $n$ at
which the subset sums of the weights $\lfloor2^i\alpha\rfloor$,
$\lfloor2^i\beta\rfloor$ with $i<n$ contain $b_n=\lfloor2^n\beta\rfloor$
consecutive integers; by the finite-certificate lemma on the connections
page (the mesh lemma with gap one), the set of nonzero values of the two
rays is then complete. The weights are computed exactly, as integer
quotients for rational coefficients and integer square roots for
quadratic ones, the subset sums are held as one integer used as a bit
set, and the longest run of represented integers is found by binary
search. The pinned pairs are checked against their recorded depth and
run start; the sweep certifies every pair $(3\gamma,2\gamma)$ with
$\gamma=2^T/d$ for the thirty-two odd denominators $5\le d\le99$ not
divisible by $3$, normalized by the least $T$; the control checks that
Hegyvári's incomplete multiset $(5/2,5)$ receives no certificate to depth
$16$, which is a check that the search is not vacuous and proves nothing.

A passing run certifies completeness of the listed pairs only. It does
not bear on Hegyvári's conjecture in general, verifies no source
argument and awards no tier.

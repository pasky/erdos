---
name: research/leads/totient_binary_series/sparse_transforms/evidence
title: Exact Checks of Sparse-transform Witnesses
desc: |
  Five retained integer multipliers, exact gap and infinite-tail certificates,
  and finite reduced-denominator checks for eleven prime-sieve sums.
created: 2026-09-17T07:14:44Z
updated: 2026-09-17T07:14:44Z
---

# Exact Checks of Sparse-transform Witnesses

[[research/leads/totient_binary_series/sparse_transforms/_index|..]]

***

The [checker](main.py) and [integer witnesses](assets/witnesses.json)
support the
[[research/leads/totient_binary_series/sparse_transforms/gap_multipliers|multiplier criterion]]
and [[research/leads/totient_binary_series/sparse_transforms/prime_sieve|prime-sieve obstruction]].
They confer finite author-checked evidence only, without independent review.

Run from the repository root with its prepared Python environment:

```sh
nice -n 10 uv run --no-sync python wiki/research/leads/totient_binary_series/sparse_transforms/evidence/main.py
```

The full default checks all five witnesses and all eleven sieve sums. The
optional `--quick` checks the first two witnesses and the first three
sieve sums and labels that reduced scope. Runtime is a few seconds.
Required dependencies are Python's standard library and the repository's
`tools` package. Inputs resolve relative to the checker; no discovery
environment, private checkout, cached success, or optional lattice package
is needed. The checker writes no files. Every failed obligation exits
nonzero, including with `python -O`.

The full run passed all 112 obligations in normal and optimized Python.
As a failure control, increasing one retained constant coefficient by one
in a scratch copy caused the optimized checker to exit 1, identifying the
broken product gaps, central coefficient, and specialization residues.
This checks the failure path; it supplies no independent mathematical review.

The witness parameters and declared values are:

| $N$ | $k$ | Height | $[x^N]PA$ | Denominators excluded through |
| --- | --- | --- | --- | --- |
| 100 | 20 | 11 | -58 | 11433 |
| 160 | 28 | 18 | 230 | 1152083 |
| 300 | 28 | 26 | 192 | 290856 |
| 300 | 32 | 27 | 62 | 3597545 |
| 900 | 32 | 67 | -7726 | 555695 |

Discovery used integer LLL reduction and an embedding with python-flint
0.9.0. These are found vectors, not minimum-height certificates. The
checker independently recomputes totients and convolutions, verifies the
coefficient data and exact degree, top coefficient two, every required
preceding and following zero, height, and central coefficient. A vector
with top coefficient two, together with the parity lemma on the owning
page, establishes that normalization's minimum for its particular pair.
No full-kernel or saturated-basis conclusion is drawn from discovery.

For each vector the checker sums 400 coefficients after its following gap
using rational arithmetic and adds the rigorous bound for every remaining
term from equation (7) of the multiplier page. It compares that bound with
the uniform crude bound and reports the largest integer denominator
excluded by the two strict inequalities in its Proposition 1. Displayed
logarithms are descriptive; all certificate decisions use exact integers
or fractions. These modest exclusions are far weaker than the parent's
continued-fraction result and do not prove an infinite family exists.

For the six primorials $Q=2,6,30,210,2310,30030$ and five nonprimorials
$Q=5,10,15,21,70$, the checker reduces $M_Q$ exactly and checks its
denominator bit lengths against retained observations. For largest prime
factor $P\ge5$, it also computes the cyclotomic value by Möbius inversion,
removes the possible exceptional largest prime, and checks that the square
of the remaining factor divides the actual reduced denominator. The case
$Q=21$ checks an actual exception: $\Psi_{21}(2)=2359=7\cdot337$,
and the primitive part used in the proof is $337$.

The nonprimorial cases include sets containing $3$ and sets omitting it,
the two branches of the uniform bound. The checker tests the corresponding
reduced-denominator lower bounds, including
$D_QP^2>2^{2P+q-9}$ with $q$ the least prime not dividing $Q$.
Together with the proved full-tail lower bound $R_Q\ge2^{-q}$, this
checks the claimed lower scale for $D_QR_Q$ in those instances. It also
checks the sieve coefficient identity through degree 120. These finite
checks supplement the all-parameter proof on the owning page; they do not
substitute for that proof.

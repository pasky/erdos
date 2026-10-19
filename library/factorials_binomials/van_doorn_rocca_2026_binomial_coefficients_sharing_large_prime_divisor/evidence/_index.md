---
name: factorials_binomials/van_doorn_rocca_2026_binomial_coefficients_sharing_large_prime_divisor/evidence
desc: |
  Replays the finite and analytic inequalities that strengthen the manuscript's
  explicit large-index cutoff from i at least 1000 to i at least 906.
tags: []
sources: []
created: 2026-09-21T18:25:51Z
updated: 2026-10-05T05:52:35Z
---

# factorials_binomials/van_doorn_rocca_2026_binomial_coefficients_sharing_large_prime_divisor/evidence

[[factorials_binomials/van_doorn_rocca_2026_binomial_coefficients_sharing_large_prime_divisor/_index|..]]

***

The [entry point](main.py) checks every $906\le i<10^6$ against the retained
counterexample bound and checks the uniform analytic inequality for the tail.
It uses the root Python environment and shared failure harness, reads no input
files, and writes no output files. Run it from the repository root:

```sh
uv run --no-sync python library/factorials_binomials/van_doorn_rocca_2026_binomial_coefficients_sharing_large_prime_divisor/evidence/main.py
```

The [[factorials_binomials/van_doorn_rocca_2026_binomial_coefficients_sharing_large_prime_divisor/_index|owning account]]
states the reduction and the published prime-gap and prime-interval premises.
The program does not independently reverify those external computations or
the manuscript's determinant inequality, and it proves nothing for $i<906$.

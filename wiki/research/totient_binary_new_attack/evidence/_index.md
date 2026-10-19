---
name: research/totient_binary_new_attack/evidence
title: Evidence for the Fresh Attack
desc: |
  Exact finite checks of kernel shadows, retained fixed-prime robust vectors,
  complete smooth-orbit rounding, sparse comparisons, dilation designs and
  residue-lifting inequalities, with explicit limits on their coverage.
tags: []
sources: []
created: 2026-10-15T19:52:41Z
updated: 2026-10-15T19:52:41Z
---

# Evidence for the Fresh Attack

[[research/totient_binary_new_attack/_index|..]]

***

The [entry point](main.py) uses Python integers and rational arithmetic,
with `python-flint` for Hermite forms, ranks and lattice reduction. Run it
from the repository root:

```sh
uv run --no-sync python wiki/research/totient_binary_new_attack/evidence/main.py
```

The full run takes a few seconds and uses well under 1 GiB. The optional
`--quick` reduces the instances exactly as its docstring states. Failed
obligations give a nonzero exit, including under `python -O`. No private
input or cached output is used. The coverage is:

- Generation of $\mathbb Z^2$ by normalized columns for $J=2^m$,
  $3\le m\le13$, including explicit odd minors for $6\le m\le13$.
- The exact shadow image of verified kernel bases at eight stated depths;
  fixed-prime structural ranks on short and longer supports; and LLL basis
  costs at $J\in\{16,32,64,128\}$. The
  [[research/totient_binary_new_attack/kernel_rigidity|kernel page]] gives
  the domains. Returned vectors are not certified minima.
- Sparse nearest-integer rounding through $e_k\le3000$. The implementation
  uses the partial totient sum $S_{3200}$, so its rational target $r$
  corresponds to the exact infinite target $r+(S-S_{3200})$. It checks
  residue, size and error bounds; doubling the gaps supplies a failing
  control. This tests instances of
  [[theory/irrationality/L218_sparse_perturbation_any_value/_index|L218]],
  not arbitrary rational targets for the infinite series.
- The coprime-pair identities in the
  [[research/totient_binary_new_attack/proof_sketch|sketch]], with exact
  coefficients and explicit truncation errors.
- The six- and twelve-point integer configurations in the
  [[research/totient_binary_new_attack/dilation_designs|design note]],
  failure at the next level, and the actual six-prime realization with
  compatible square congruences.
- Five [retained robust vectors](assets/robust_kernel_vectors.json),
  found by weighted LLL and checked directly against every affine
  fixed-prime constraint, the totient kernel, parity and cost. Altering a
  coefficient supplies a failing control.
- Eight or six certified rounding decisions with complete smooth-orbit
  weights, for $(a,Q)=(15,30)$ or $(35,210)$ and target zero. The weights
  and $S$ are enclosed by rational intervals; every rounding decision is
  determined uniquely. The resulting signed sequences obey the fixed
  prime laws, fixed prime-power values and size/congruence bounds through
  $n=10000$. Omitting propagation to multiples fails a prime law.
  This checks a finite prefix underlying the quantitative bound in the
  [[research/totient_binary_new_attack/partial_multiplicativity|fixed-prime
  note]]. It does not instantiate the positive interval of L220 or prove
  the infinite sum from a finite prefix.
- The [[research/totient_binary_new_attack/residue_lifting|residue-lifting
  inequalities]] for $2\le m\le64$ and zero-block starts $0\le N\le128$,
  using exact partial sums with certified positive tail bounds.

The asymptotic conclusions and infinite constructions rest on the
written proofs. These computations check their listed finite instances
and interfaces; they do not prove irrationality or confer an independent
verification tier.

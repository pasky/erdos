---
name: research/erdos_774/evidence/axis_flat_preimages
title: Twenty stored flat targets with bounded integer line preimages
desc: Twenty solver-generated flat point vectors on [3]^3 and [3]^4 have exactly checked bounded integer axis-line preimages; they are finite examples, not a four-direction theorem.
tags: [E0774, computational, finite, incomplete]
sources: []
created: 2026-09-24T23:30:00Z
updated: 2026-09-24T23:30:00Z
---

# Twenty stored flat targets with bounded integer line preimages

[[research/erdos_774/evidence/_index|..]]

***

## Ingredient tested

The [flat-preimage lemma](../../lemmas/axis_line_flat_preimages.md) proves
that in at most three directions every bounded integer vector in the line
image of a box has an equally bounded integer line preimage. Whether every
flat integer vector in the full line image of a four-direction box has a
flat integer line preimage remains unproved. The records here are finite
examples in that direction. No color-lifting assertion was tested.

## What is checked

Run, from the repository root,

```sh
uv run --no-sync python wiki/research/erdos_774/evidence/axis_flat_preimages/main.py
```

The [checker](main.py) reads the twenty stored
[target and preimage pairs](assets/axis_flat_preimage_samples.json) and,
with the standard library, integer arithmetic and the shared root `tools`
checker, verifies for each that the entries lie in $\{-1,0,1\}$, that the
target is nonzero, that the line combination with the stored coefficients
equals the target at every point, and that the target is annihilated by
every quotient functional, so that it lies in the line image. It performs
no search and finishes in under a second; a failed clause exits nonzero.
Points are ordered lexicographically with zero-based coordinates, and line
columns by axis and then by fixed coordinates.

## Generation and its exact range

The targets are optimization-generated, not uniform random flat vectors,
and their generation is not part of the verification. The quotient matrix
used to constrain a target $b$ to the line image is

$$
T_{r,x}=\prod_i(1_{x_i=r_i}-1_{x_i=d_i-1}),
\qquad 0\le r_i<d_i-1.
$$

Targets came from a mixed-integer solver minimizing a fresh Gaussian linear
objective over integer $b\in[-1,1]^X$ with $Tb=0$; preimages came from a
real feasibility solve followed by an integer feasibility solve with the
same equality and bounds.

| Probe | Exact finite scope and recorded conclusion |
|---|---|
| Seed 20260918, continued across both boxes | Eight trials on $[3]^3$, then eight on $[3]^4$. All 16 targets had full $\{\pm1\}$ support. Every real and integer preimage solve returned a feasible status. |
| Seed 20260919 | Four trials on $[3]^4$; choose 41 allowed point indices without replacement, force the other 40 target coordinates to zero, then generate the Gaussian objective. Supports were 35, 29, 35, 30; all four preimage solves succeeded. |
| Separate overlapping probe, seed 774 | Thirty targets on $[3]^3$, then twenty on $[3]^4$, with the same quotient constraints and independent Gaussian objectives. All returned a target and integer preimage with no reported infeasibility. Those preimages were not residual-checked or retained, so these fifty statuses are noncertified solver observations. |

In the first two probes each integer call had an eight-second limit and the
real feasibility solve had none. The matrix sizes were $A:27\times27$,
$T:8\times27$ and $A:81\times108$, $T:16\times81$. The separate probe used
a three-second limit on both integer calls and stopped at its fixed caps.
Only the twenty pairs of the first two probes are retained, and only they
are checked; the fifty noncertified statuses are used in no proof.

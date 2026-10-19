---
name: research/erdos_774/evidence/moment_basis_float
title: Capped floating-point basis reduction for projected moment lattices
desc: A float64 exploration of whether basis exchanges can meet the phase-rounding coordinate cap on small cubes; it is an observation record, not a certificate.
tags: [E0774, computational, Boolean-moments, exploratory]
sources: []
created: 2026-09-24T23:30:00Z
updated: 2026-09-24T23:30:00Z
---

# Capped floating-point basis reduction for projected moment lattices

[[research/erdos_774/evidence/_index|..]]

***

## Question and scope

The [phase-rounding criterion](../../routes/moment_phase_lattice.md)
would give uniform extraction from a rational basis of the projected
lattice whose Gram–Schmidt coordinates are at most $1/4$ in magnitude and
whose total squared length is $O(2^d)$. This exploration asked whether
basis exchanges could satisfy that criterion on small cubes. It is
**float64, not an exact certificate**, and supplies no uniform-energy
theorem. Neither extraction nor coloring conclusions depend on it.

The seven pairs were $d=4,\ldots,7$ and $k\in\{1,2\}$ with $2k<d$. Each run
stopped after a complete cursor scan, 20,000 cursor steps, or 1,000
accepted swaps, whichever came first. There was no randomness. Initial
representatives were the monomials $x_A$ with $|A|>k$, in increasing degree
and combination order; points were ascending integer masks with bit $i$ as
coordinate $i$. Orthogonal projection removed the Walsh rows of degree at
most $k$. Integer size reductions and Lovász-parameter $0.75$ adjacent
swaps were allowed only if the explicitly updated Gram–Schmidt coordinate
cap stayed at most $0.25+10^{-9}$; the inequality test used tolerance
$10^{-10}$, and the QR factorization was recomputed after each accepted
swap.

| $d,k$ | Rank | Initial $T/n$ | Final $T/n$ | Max coordinate | Swaps | Steps | Full scan |
|---|---:|---:|---:|---:|---:|---:|---|
| 4,1 | 11 | .44140625 | .375 | .25 | 15 | 40 | Yes |
| 5,1 | 26 | .80175781 | .625 | .25 | 103 | 231 | Yes |
| 5,2 | 16 | .17675781 | .15625 | .125 | 20 | 55 | Yes |
| 6,1 | 57 | 1.31469727 | .9375 | .25 | 498 | 1052 | Yes |
| 6,2 | 42 | .37719727 | .3125 | .125 | 207 | 455 | Yes |
| 7,1 | 120 | 2.01837158 | 1.54278564 | .25 | 1000 | 2030 | No |
| 7,2 | 99 | .70587158 | .56890869 | .125 | 1000 | 2046 | No |

No swap was blocked by the floating cap test. These values ceased to
discriminate and no further computation was undertaken.

## Script

The [exploration script](produce.py) records the complete algorithm and
writes its summary to the ignored `output/` folder beside it. It needs
NumPy, which the repository does not declare, and the original run set
`OPENBLAS_NUM_THREADS=1`. There is no checker: floating-point observations
are not evidence, and this folder contributes nothing to the aggregate
evidence entry point.

---
name: research/erdos_774/evidence/long_shift_gf2
title: Binary ranks of increasing-path relations on pair labels
desc: An exact GF(2) rank table for 39 small cases of the long-shift path relations; the general binary rank theorem on the lemma page does not use it.
tags: [E0774, computational, finite]
sources: []
created: 2026-09-24T23:30:00Z
updated: 2026-09-24T23:30:00Z
---

# Binary ranks of increasing-path relations on pair labels

[[research/erdos_774/evidence/_index|..]]

***

## Purpose

The [long-shift extraction lemma](../../lemmas/long_shift_extraction.md)
proves an elementary binary rank theorem for the prescribed $k$-edge
increasing-path relations on pair labels. A single finite GF(2) rank
diagnostic preceded that proof and is retained here as an exact record;
the general theorem does not use the table.

## The finite table

The range is

$$
2\le k\le7,\qquad k+1\le n\le\min(12,2k+4),
$$

39 cases. Each case enumerates all increasing $(k+1)$-tuples of $[n]$,
forms their pair-path incidence bit vectors over the $\binom n2$ pair
coordinates, and computes the exact GF(2) row rank. Columns with
$j-i>n-k$ are inactive and are removed when reporting the nullity.

| $k$ | Consecutive $n$ values | Active-column nullities |
|---|---|---|
| 2 | 3--8 | 1, 1, 1, 1, 1, 1 |
| 3 | 4--10 | 2, 2, 1, 0, 0, 0, 0 |
| 4 | 5--12 | 3, 3, 2, 1, 1, 1, 1, 1 |
| 5 | 6--12 | 4, 4, 3, 2, 1, 0, 0 |
| 6 | 7--12 | 5, 5, 4, 3, 2, 1 |
| 7 | 8--12 | 6, 6, 5, 4, 3 |

## What is checked

Run, from the repository root,

```sh
uv run --no-sync python wiki/research/erdos_774/evidence/long_shift_gf2/main.py
```

The [checker](main.py) recomputes all 39 nullities by exact GF(2)
elimination on bit vectors, using the standard library and the shared root
`tools` checker; it performs no search and finishes in under a second. Its
named checks are that each row of the table is reproduced and that 39 cases
are covered. A failed clause exits nonzero.

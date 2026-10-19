---
name: theory/integer_sequences/L211_fractional_half_cover_obstruction/evidence
title: Exact evidence for the thirteen-point fractional obstruction
desc: Exhaustive integer checks of all subsets and ternary relations, together with matching rational covering certificates, establish the fixed thirteen-point claim.
tags: [evidence, finite]
sources: []
created: 2026-10-15T23:24:37Z
updated: 2026-10-15T23:24:37Z
---

# Exact evidence for the thirteen-point fractional obstruction

[[theory/integer_sequences/L211_fractional_half_cover_obstruction/_index|..]]

***

Run from the repository root:

```sh
uv run --no-sync python wiki/theory/integer_sequences/L211_fractional_half_cover_obstruction/evidence/main.py
```

The [entry point](main.py) uses Python integers and rational numbers,
the standard library, and the shared `tools` checker. Its fixed input is
[the thirteen binary vectors and exact covering certificates](assets/configuration.json).
The vectors were located by a finite search; the checker reproduces no
search and uses no optimization solver. It takes a few seconds and less
than 32 MiB. The optional `--quick` performs the same complete check.

It enumerates all $2^{13}$ subset sums and, independently as an author
cross-check, all $3^{13}$ ternary sums through two half-word tables. The
resulting relation-support sets must agree. A separate scalar subset-sum
check tests the base-sixteen encoding. Upward closure of relation supports
gives every dissociated subset, and submask dynamic programming gives the
largest dissociated size in every nonempty subset.

The checker exhausts all two-color partitions, verifies the displayed
three-color partition, and checks the dual inequality on every dissociated
subset and the primal coverage at every point. It also checks that deleting
any point makes the set two-colorable. In particular, the
[[research/erdos_774/routes/tensor_coloring|critical-core separation bound]]
applies to this example: its three-color separation threshold is at most
six. This finite seed alone does not provide successive tensor color jumps.

Any false hereditary bound, proper two-coloring, invalid coloring class,
undercovered point, or overweight dual independent set makes the program
exit nonzero, including under `python -O`. No cached output is read. These
are author checks of the finite claim, not independent verification of it
or evidence for an unbounded family.

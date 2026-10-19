---
name: research/erdos_774/evidence/axis_line_circuit
title: A height-two circuit among four-direction axis lines
desc: A fixed 27-line rational circuit in [3]^4 with one coefficient two shows that four-direction rational dependence need not give a ternary relation; the certificate is checked exactly.
tags: [E0774, computational, proved, lines]
sources: []
created: 2026-09-24T23:30:00Z
updated: 2026-09-24T23:30:00Z
---

# A height-two circuit among four-direction axis lines

[[research/erdos_774/evidence/_index|..]]

***

## Ingredient tested

On three-direction slices of the axis-line family, rational dependence
implies a ternary subrelation, because the slices are cographic; see
[the line coloring page](../../routes/axis_line_coloring.md). The question
tested here is whether that collapse extends to four full axis-line
directions. It does not: the retained certificate is a rational circuit of
27 full axis-parallel lines of $[3]^4$, of rank 26, whose primitive
relation has exactly one coefficient of magnitude two and all other
coefficients $\pm1$. Rank and full support prove that the support is a
rational circuit, and the primitive coefficient two proves that it is
dissociated.

## What is checked

Run, from the repository root,

```sh
uv run --no-sync python wiki/research/erdos_774/evidence/axis_line_circuit/main.py
```

The [checker](main.py) reads the fixed
[certificate](assets/axis_line_circuit.json), which lists every line and
coefficient with zero-based coordinates and axes, the three fixed
coordinates of each line in increasing coordinate order. It constructs
exactly the $81\times27$ incidence matrix and checks, with the standard
library, exact rational elimination and the shared root `tools` checker,
that the 27 lines are distinct, that the coefficients are nonzero with
exactly one of magnitude two and greatest common divisor one, that the
signed combination vanishes at all 81 points, and that the matrix has rank
26. It performs no search and finishes in under a second; a failed clause
exits nonzero.

## Discovery and its exact range

The circuit was found by a bounded discovery run that is not part of the
verification: exact symbolic rational elimination with random seed 8043 and
at most eight random full-column orders for each of the dimensions
$(3,3,3,3)$, $(2,3,3,3)$ and $(3,3,3)$, inspecting a rational basis and
its fundamental circuits for each order and stopping a dimension at the
first primitive circuit of height greater than one. No floating-point
certificate was accepted.

| Exact input | Bounded discovery observation |
|---|---|
| $[3]^4$, 81 point rows and 108 line columns | Trial 0 found the retained 27-column rank-26 circuit of height two, with one coefficient two |
| $[2]\times[3]^3$, 54 rows and 81 columns | Trial 4 found a 32-column height-two circuit; this extra observation is not a durable proof input |
| $[3]^3$, 27 rows and 27 columns | None in eight orders; the algebraic cographic proof, not this search, establishes the exact three-direction statement |

The search stopped after answering the ingredient question and did not test
chromatic growth.

## Extension to larger boxes

The circuit persists when coordinate layers are duplicated. Copy nonparallel
lines in the duplicated layer and extend parallel lines through the new
layer. Restriction of a new relation to the old rows determines its old
coefficients; independence of the copied proper circuit subset determines
the remaining ones. Choose layers away from the heavy line's fixed
coordinate whenever that line is nonparallel. Thus the coefficient two
remains unique, and the example extends to every four-dimensional grid with
side lengths at least three. This is an algebraic scope check, not another
computation.

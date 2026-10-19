---
name: research/erdos_132/evidence
title: Evidence
desc: |
  Exact valuation obstructions, a rigid split-class example, and a bounded
  Eisenstein-grid enumeration; none resolves either unrestricted question.
tags: []
sources: []
created: 2026-09-22T21:34:44Z
updated: 2026-10-16T06:44:50Z
---

# Evidence

[[research/erdos_132/_index|..]]

***

The [entry point](main.py) runs every retained probe under `util/` in its
own interpreter, fails when any probe exits nonzero, and then checks the
Eisenstein-grid enumeration's written results against the table on the
[motif note](../eisenstein_motif.md). It uses the root Python environment
and the shared failure harness, reads no input files, and writes only the
enumeration's JSON under ignored `output/`. Run it from the repository
root:

```sh
uv run --no-sync python wiki/research/erdos_132/evidence/main.py
```

[`util/continuation_checks.py`](util/continuation_checks.py) performs
bounded exact checks of the thirteen-point hexagram spectrum, the six-point
invariant-shell obstruction, and the deletion-critical meanders at
$K=3,5,9$. The general arguments and exact scope are in
[small orders](../small_orders.md), [dyadic distances](../dyadic_distances.md),
and [deletion criticality](../deletion_criticality.md). It is not a search
or an independent reproduction of the published six-distance
classification.

[`util/valuation_counterexample.py`](util/valuation_counterexample.py)
enumerates all 15 unordered pairs of the stated six-point
Eisenstein-coordinate configuration and checks its complete spectrum. Four
distances are rare; the failed claim concerns only the maximum distance
within one valuation level. The same certificate includes the exactly
checked nine-point example with both odd-shell extremes rich, and the
five-point rational Eisenstein example with only three residue classes and
a rich odd-shell maximum. Their spectra and the precise failed claims are
recorded in [dyadic distances](../dyadic_distances.md).

[`util/split_class_example.py`](util/split_class_example.py) checks the
rigid example of the [split-class note](../split_class_deformations.md) for
$m=2,\ldots,7$ in exact arithmetic over $\mathbb Q(\sqrt2,\sqrt3)$: the unit
class is the only class whose pairs have unequal absolute horizontal
displacements, the unit triangle gives two independent equal-length tensors,
and the exact rare count is at least $(m^2-4m-6)/4$. The general bound and the
circle-occupancy estimate are proved in the note and its claim, not computed.
This probe can also be run alone from the repository root:

```sh
uv run --no-sync python wiki/research/erdos_132/evidence/util/split_class_example.py
```

[`util/mixed_valuation_selector.py`](util/mixed_valuation_selector.py)
checks the six-point mixed-valuation obstruction of the
[selector note](../mixed_valuation_selector.md) in exact rational
arithmetic.

[`util/eisenstein_grid.py`](util/eisenstein_grid.py) enumerates all
nonempty subsets of the 4-by-4 Eisenstein grid in integer arithmetic and
writes its results to `output/eisenstein_grid_results.json`; the entry
point compares the minima and minimizer counts with the motif note's
table. The [motif note](../eisenstein_motif.md) states the finite
conclusions and proves the reduction used to rule out one-point
extensions of its eleven-point example.

[`util/c3_hex_candidates_exact.py`](util/c3_hex_candidates_exact.py) belongs to
the [unreviewed rotational report](../independent/c3_13_unreviewed.md) and needs
SymPy. It concerns only one finite algebraic subcase and does not certify that
report's other reductions. It is not evidence of a solution to either
unrestricted question.

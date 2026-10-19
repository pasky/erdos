---
name: research/graph_ramsey_interfaces/butterfly_degree_sum_certificate/evidence
title: Exact butterfly parameter check
desc: Rational arithmetic checks the five-part witness, its only triangle types and the all-order isolated-vertex extension.
created: 2026-10-14T22:08:00Z
updated: 2026-10-15T04:32:53Z
---

# Exact butterfly parameter check

[[research/graph_ramsey_interfaces/butterfly_degree_sum_certificate/_index|..]]

[[research/graph_ramsey_interfaces/butterfly_degree_sum_certificate/evidence/verify/_index|verify/]]: Independent whole-conclusion examination and separate grade of the exact finite graph construction and its asymptotic consequence.

***

From the repository root run:

```sh
uv run --no-sync python wiki/research/graph_ramsey_interfaces/butterfly_degree_sum_certificate/evidence/main.py
```

The [exact input](assets/parameters.json) specifies five part numerators,
the common denominator, all six supported pairs and their density
numerators, the comparison constant and the cutoff. The program uses
integer and rational arithmetic only. It checks all ten triples of part
labels, the handshaking identity, the exact two triangle sums, the positive
edge-density surplus, the rational comparison with $2(\sqrt3-1)$, and the
padding inequality at the cutoff. Monotonicity extends the latter check to
every larger order, as proved on the owning page.

The run takes less than a second in the repository environment. It has no
search parameters, external source input or generated witness. The
construction and the reduction from rational parameters to actual graphs
are proved in
[[theory/combinatorics/L113_butterfly_triangle_degree_sum/_proof|the native proof]].
This program supplies author arithmetic evidence. The independent recount,
adversarial controls, whole-conclusion report and separate grade are retained
in the
[[research/graph_ramsey_interfaces/butterfly_degree_sum_certificate/evidence/verify/whole_conclusion/_index|verification record]].

The handshaking diagnostic is forced by shared pair accumulation and has no
independent checking weight. The program also does not validate arbitrary
construction inputs: simultaneous sign reversal preserves its rational
values while invalidating the finite-set parameters. The retained positive
input and the full analytic proof are the subject of the accepted grade.

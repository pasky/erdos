---
name: research/four_point_sidon_certificates/evidence
title: Exact fourteen-point Sidon certificate
desc: Exhaust all four-subsets and nine-subsets and verify an eight-point witness in Ma–Tang's fixed integer set.
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

# Exact fourteen-point Sidon certificate

[[research/four_point_sidon_certificates/_index|..]]

***

From the repository root run:

```sh
uv run --no-sync python wiki/research/four_point_sidon_certificates/evidence/main.py
```

The exact input [fourteen_points.json](assets/fourteen_points.json) is the
set and eight-point witness in Ma–Tang, arXiv:2602.23282v2, Lemma 5.1.
The [owning account](../_index.md) gives the source link and the distinction
between strong Sidon and the four-point hypothesis.

Using integer arithmetic, the program checks all 1001 four-subsets for at
least five positive differences, all 2002 nine-subsets for a strong Sidon
violation, and the contained eight-point witness for all 36 distinct pair
sums including diagonals. The maximum strong Sidon cardinality of this
one set is therefore exactly eight, since the property is hereditary.
Boundary checks distinguish repeated summands and the weak convention.

Expected runtime is a few seconds or less in the repository environment.
There is no discovery search, assertion of optimality of $4/7$, or
independent review. The checker exits nonzero on any failed obligation,
also under optimized Python.

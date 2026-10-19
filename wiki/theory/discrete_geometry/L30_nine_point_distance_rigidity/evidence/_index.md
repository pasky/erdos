---
name: theory/discrete_geometry/L30_nine_point_distance_rigidity/evidence
title: Exact evidence for one nine-point distance partition
desc: The retained coordinates and full Jacobian minor are recomputed with exact arithmetic; the scope is local rigidity of one configuration.
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

# Exact evidence for one nine-point distance partition

[[theory/discrete_geometry/L30_nine_point_distance_rigidity/_index|..]]

***

From the repository root run:

```sh
uv run --no-sync python wiki/theory/discrete_geometry/L30_nine_point_distance_rigidity/evidence/main.py
```

The program uses the repository's `tools.Checker` and Python integers and
fractions. Its expected runtime is a few seconds or less. It reads
[configuration.json](assets/configuration.json), containing the complete
point list, distance classes, degeneracies, equality labels and square
matrix. This mathematical input is computed from the example stated on
[[problems/distance_problems/E0217/_index|Problem 217]]; the checker
recomputes all its consumed data from the coordinates.

The finite domain consists of all 36 unordered pairs, all 84 triples,
all 126 quadruples and all 28 equality derivatives of this one set.
The determinant $-1102248$ is the computational input to the
[[theory/discrete_geometry/L30_nine_point_distance_rigidity/_proof|local uniqueness proof]].
The program checks neither other distance partitions nor a global
nonexistence statement. Every failed obligation causes a nonzero exit,
including under optimized Python. This is author evidence, not an
independent examination.

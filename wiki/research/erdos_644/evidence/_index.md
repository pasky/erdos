---
name: research/erdos_644/evidence
title: Evidence
desc: Exact rational vertex enumeration and disjoint-triple couplings for the three-point constant-composition theorem, checked by one entry point.
tags: []
sources: []
created: 2026-09-23T05:34:48Z
updated: 2026-09-24T22:12:53Z
---

# Evidence

[[research/erdos_644/_index|..]]

***

The [entry point](main.py) checks that the retained certificate
[`assets/couplings.json`](assets/couplings.json) is present and runs the
probe [`util/verify.py`](util/verify.py) in its own interpreter, failing
when the probe exits nonzero. It uses the root Python environment and the
shared failure harness, reads only the certificate, and writes no output
files. Run it from the repository root:

```sh
uv run --no-sync python wiki/research/erdos_644/evidence/main.py
```

The probe uses only the Python standard library and exact rational
arithmetic. It examines all $\binom{15}{7}=6435$ active-constraint
choices for the seven-dimensional probability polytope $Q_3$, discards
singular and infeasible bases, and finds exactly 52 distinct vertices.
The certificate supplies one representative of each of their 16 orbits
under permutations of the three seed points. Every representative is
expressed as a convex combination of vectors
$(4\delta_I+2\delta_J+\delta_K)/7$, with $I,J,K$ pairwise disjoint.

States are bit masks in the order
$\varnothing,1,2,12,3,13,23,123$, namely integers 0 through 7.
Each coupling entry is `[rational coefficient, [I, J, K]]`.

This is a finite, exhaustive, rational computational certificate, not a
proof-assistant formalization. Its mathematical reduction and the
integral rounding argument are in
[constant-composition families](../constant_composition_families.md). No
numerical linear-programming solver or floating-point calculation is used
by the probe. The certificate checks only the finite three-point polytope
inclusion and does not certify either unrestricted assertion of
Problem 644.

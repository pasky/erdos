---
name: research/erdos_963/evidence
title: Evidence
desc: Exact finite certificate excluding one specific candidate configuration, checked by one entry point.
tags: []
sources: []
created: 2026-09-18T20:40:03Z
updated: 2026-09-24T22:12:58Z
---

# Evidence

[[research/erdos_963/_index|..]]

***

The [entry point](main.py) checks that the retained certificate
[`assets/cube4.json`](assets/cube4.json) is present and runs the probe
[`util/check_cube4.py`](util/check_cube4.py) in its own interpreter,
failing when the probe exits nonzero. It uses the root Python environment
and the shared failure harness, reads only the certificate, and writes no
output files. Run it from the repository root:

```sh
uv run --no-sync python wiki/research/erdos_963/evidence/main.py
```

The certificate proves that every 32-subset of the 40 nonzero antipodal
representatives in the ternary four-dimensional cube contains a
dissociated six-subset: it partitions the representatives into blocks of
sizes 13, 13, and 14 and lists dissociated six-subsets whose pairwise
unions cover every pair of each block. The probe recomputes the
representative set, enumerates the 64 signed sums of every listed
six-subset, and checks the pair covers. The
[proof sketch](../proof_sketch.md) states how this excludes one proposed
counterexample family; the certificate excludes this specific candidate
family only.

---
name: research/erdos_940/evidence
title: Evidence
desc: Preserved exact finite calculations supporting the topical proofs, run by one entry point; current research status is in the main index.
tags: []
sources: []
created: 2026-09-22T02:48:33Z
updated: 2026-09-24T22:13:02Z
---

# Evidence

[[research/erdos_940/_index|..]]

***

The [entry point](main.py) runs every retained certificate under `util/`
in its own interpreter and fails when any certificate exits nonzero. It
uses the root Python environment and the shared failure harness, reads no
input files, and writes no output files; the certificates that need NumPy
or SymPy say so and fail when the package is missing, and neither package
is declared by the repository, so the command supplies both. Run it from
the repository root:

```sh
uv run --no-sync --with numpy --with sympy python wiki/research/erdos_940/evidence/main.py
```

The [quintic first-moment certificate](util/r5_first_moment.py) preserves
the exact integer convolutions and rational inequalities used in
[the quintic barrier theorem](../quintic_first_moment_barrier.md). Its
combined file runs and passes under the entry point above. It requires
NumPy and SymPy.

The [quartic residue certificate](util/quartic_residue_obstruction.py) was
reconstructed during the independent-record comparison. It uses only the Python
standard library and proves the [restricted 32-prescription objective exceeds
1.08](../quartic_residue_obstruction.md). It does not obstruct the quartic
complement argument.

The [four-unit quintic extension](util/quintic_four_unit_extension.py)
uses only the Python standard library. Its 70 integer convolutions modulo
25 give primitive minimum nine, and its rational arithmetic certifies the
strengthened uniform unordered mean $385732347/156250000>2.468$ in
[the quintic note](../quintic_first_moment_barrier.md).

The [cubic matrix certificate](util/cubic_matrix_composition.py) uses
SymPy to verify polynomial identities in a nine-dimensional matrix
algebra, reducing coefficients modulo $z^2+z+1$. It checks every
coefficient, not sampled inputs. The accompanying
[composition note](../cubic_matrix_composition.md) gives the trace
obstructions and the analytic bounds for the remaining scalar repairs.

The [representation-count diagnostic](util/representation_count_congruences.py)
preserves the one exact computation through $100000$ made in the
[count-congruence attempt](../representation_count_congruences.md). It
requires NumPy, finds counterexamples in every residue class for six
specified pairs of target and count moduli, and fails if any tested class
lacks a witness. It excludes only universal congruences of those
particular forms, not eventual congruences.

This directory stores supporting material only. See
[the main research index](../_index.md) for established results and
unresolved questions.

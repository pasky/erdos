---
name: research/erdos_774/evidence
title: Evidence
desc: Exact finite certificates and retained diagnostics for the E0774 research, each with its checker or discovery script, its inputs and its exact scope.
tags: [E0774, computation]
sources: []
created: 2026-09-17T23:53:25Z
updated: 2026-10-15T11:14:17Z
---

# Evidence

[[research/erdos_774/_index|..]]

[[research/erdos_774/evidence/angular_flat_multiples/_index|angular_flat_multiples/]]: Exact arithmetic certifies D(15) = 8, D(105) = 49 and a flat multiple of the 1155th cyclotomic polynomial of degree 502, with the quoted thresholds and covolume; a separate solver script records the searches that suggest 502 is least.

[[research/erdos_774/evidence/axis_flat_preimages/_index|axis_flat_preimages/]]: Twenty solver-generated flat point vectors on [3]^3 and [3]^4 have exactly checked bounded integer axis-line preimages; they are finite examples, not a four-direction theorem.

[[research/erdos_774/evidence/axis_line_circuit/_index|axis_line_circuit/]]: A fixed 27-line rational circuit in [3]^4 with one coefficient two shows that four-direction rational dependence need not give a ternary relation; the certificate is checked exactly.

[[research/erdos_774/evidence/boundary_anchor/_index|boundary_anchor/]]: A checked finite certificate rules out universal three-color anchors at the remaining simplex boundary, including after all exact scalar encodings.

[[research/erdos_774/evidence/grow_whicher/_index|grow_whicher/]]: An exact exhaustive certificate verifies the Grow–Whicher example and its fractional dissociated coloring number 27/13.

[[research/erdos_774/evidence/long_shift_gf2/_index|long_shift_gf2/]]: An exact GF(2) rank table for 39 small cases of the long-shift path relations; the general binary rank theorem on the lemma page does not use it.

[[research/erdos_774/evidence/moment_band_determinants/_index|moment_band_determinants/]]: Exact Smith forms of 53 Walsh degree-band matrices and nine even-parity moment matrices test the semistability of moment lattices on small cubes; they supply no theorem.

[[research/erdos_774/evidence/moment_basis_float/_index|moment_basis_float/]]: A float64 exploration of whether basis exchanges can meet the phase-rounding coordinate cap on small cubes; it is an observation record, not a certificate.

[[research/erdos_774/evidence/moment_scalar_bound/_index|moment_scalar_bound/]]: An exact scan of 16,694 degree patterns on ten pairs finds no violation of a candidate scalar lower bound for moment-lattice covolumes; the expression is a diagnostic, not a theorem.

[[research/erdos_774/evidence/polynomial_checksum/_index|polynomial_checksum/]]: A bounded six-instance test found eight-column ternary witnesses against one explicit binary checksum palette; the retained witnesses are checked by elementary integer sums and are not an arbitrary-color theorem.

[[research/erdos_774/evidence/prime_circuit/_index|prime_circuit/]]: Exact minors and kernel checks certify the displayed seed circuit in S_3 x S_3 x S_3 and its twenty-point dissociated lift in S_3 x S_5 x S_7.

[[research/erdos_774/evidence/prime_reset_span/_index|prime_reset_span/]]: The 96-by-105 common-span matrix of the explicit seven-layer three-coloring of S_3 x S_5 x S_7 has nullity 22, above the enumeration gate, so the test decides nothing.

[[research/erdos_774/evidence/short_arc_root_relations|short_arc_root_relations]]: An explicit degree-49 flat multiple of a cyclotomic polynomial gives a 26-point signed root relation in a short arc; short arcs force angular color variation, not a coloring contradiction, and no o(n)-degree flat family was found.

[[research/erdos_774/evidence/simplicial_7_3/_index|simplicial_7_3/]]: An exact enumeration of the 3-subset boundaries of [6] and inconclusive solver searches for two-colorings of the boundaries of [7]; no coloring or infeasibility certificate was obtained.

[[research/erdos_774/evidence/tensor_boundary/_index|tensor_boundary/]]: A checked twelve-coloring certificate shows the boundary tensor S_3 x S_4 x S_3 has no universal three-color anchor, before or after exact scalar encoding.

[[research/erdos_774/evidence/tensor_layers/_index|tensor_layers/]]: Exact 3-by-5 tensor-layer certificates give a three-color obstruction, a two-color extension, and bounds 8 to 10 on the separation parameter.

[[research/erdos_774/evidence/voltage_parity_checks|voltage_parity_checks]]: An exact witness refutes a proposed nonzero-XOR tensor certificate on K_{3,3}, and eight prescribed cofactor multipliers are recorded; neither is a theorem about arbitrary multipliers or colorings.

***

These computations test finite ingredients; none establishes the missing
unbounded family. Every probe lives in its own folder under the evidence
contract: a `main.py` that states its checked clauses and exits nonzero on
any failed obligation, an `assets/` folder for the exact inputs it reads,
and its own page. The [aggregate entry point](main.py) runs every checker
probe in a fresh interpreter and fails if any fails. From the repository
root:

```sh
uv run --no-sync python wiki/research/erdos_774/evidence/main.py
```

The checkers use only the Python standard library and the shared root
`tools` checker, so they run in the repository's locked environment; the
whole battery finishes in a few seconds. Two folders,
`moment_basis_float/` and `simplicial_7_3/`, hold only a discovery script
(`produce.py`) whose observations are not evidence, and the
`polynomial_checksum/` and `angular_flat_multiples/` folders each hold one
beside a checker. Those four scripts need NumPy and SciPy, and the last also
SymPy, all from the repository's evidence dependency group; each
page states its dependencies and writes disposable products only to an
ignored `output/` folder.

Two further pages, [short-arc root relations](short_arc_root_relations.md)
and [voltage parity checks](voltage_parity_checks.md), record exact finite
observations whose verification is short exposed arithmetic and needs no
checker.

Certificates that a probe checks (the Grow boundary and 3-by-4-by-3 tensor
certificates, the twenty-point prime circuit, the four-direction line
circuit, the twenty flat preimages, the checksum witnesses, and the flat
cyclotomic multiples) are exact inputs whose mathematical reading is on the
owning research pages. The
remaining probes are retained diagnostics: they reproduce recorded finite
tables exactly and prove no general statement, as each page says.

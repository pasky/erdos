---
name: theory/integer_sequences/L271_repeated_simplex_extraction/evidence
title: Exact repeated-simplex lattice diagnostics
desc: Integer Smith forms and monomial Gram determinants check ten full relation lattices, all 254 spectral subfamilies in two small cases, and every downset in four small cases.
tags: [evidence, lattice, tensor]
sources: []
created: 2026-10-15T23:24:37Z
updated: 2026-10-15T23:24:37Z
---

# Exact repeated-simplex lattice diagnostics

[[theory/integer_sequences/L271_repeated_simplex_extraction/_index|..]]

***

The [checker](main.py) supplies finite author diagnostics for
[[theory/integer_sequences/L271_repeated_simplex_extraction/_index|L271]].
Its [proof](../_proof.md), including the inherited analytic interfaces,
is the warrant for the unbounded statement. No numerical Gaussian sum,
independent verification or finite reduction of that statement is claimed.

Run from the repository root:

```sh
uv run --no-sync python wiki/theory/integer_sequences/L271_repeated_simplex_extraction/evidence/main.py
```

Write $q=2^b$, $d=bk$, and let $\mathcal F$ consist of Boolean
frequencies missing at least one whole block. The fixed domain checks:

- Ten full lattices: $(b,k)=(1,1),\ldots,(1,5)$,
  $(2,1),\ldots,(2,3)$, and $(3,1),(3,2)$. The product of the Smith
  invariants of the Walsh rows is their index in the saturated integer
  lattice, giving its exact covolume. Independently, fraction-free
  determinants of the monomial Gram matrix
  $G_{S,T}=2^{d-|S\cup T|}$ give the square covolume. Both are compared
  with $\log_2\det K=bk(q-1)^{k-1}/2$.
- All 254 nonempty spectral subfamilies at $(b,k)=(1,3),(2,2)$.
  Their Smith covolumes are compared exactly, after dividing the logarithm
  by rank, with the full lattice. This domain contains non-downsets.
- All nonempty downsets inside $\mathcal F$ at
  $(b,k)=(1,3),(1,4),(2,2),(3,2)$: respectively 18, 166, 25 and 361
  downsets. Their mean degrees are compared with the full frequency family
  by integer cross-multiplication.

The code uses exact integers and fractions, the standard library,
repository `tools`, and the retained
[Smith-form helper](../../../../research/erdos_774/evidence/moment_band_determinants/main.py).
Inputs are fixed in the code. No private file, cached success result or
external solver is required. The run takes under thirty seconds and less
than 64 MiB; `--quick` has the same coverage. A failed comparison or
nonexact arithmetic step exits nonzero.

---
name: theory/integer_sequences/L269_simplex_affine_fiber_threshold/evidence
title: Exact affine-fiber boundary diagnostics
desc: Exact small tensors certify rational independence below the threshold and check the displayed ternary trades at and above it over both a prime field and a non-prime finite field.
tags: [evidence, finite-field, tensor]
sources: []
created: 2026-10-15T23:24:37Z
updated: 2026-10-15T23:24:37Z
---

# Exact affine-fiber boundary diagnostics

[[theory/integer_sequences/L269_simplex_affine_fiber_threshold/_index|..]]

***

The [checker](main.py) is author evidence for
[[theory/integer_sequences/L269_simplex_affine_fiber_threshold/_index|L269]].
It constructs the original integer simplex tensor columns; no matrix
entry is reduced to the characteristic of the field indexing the points.

Run from the repository root:

```sh
uv run --no-sync python wiki/theory/integer_sequences/L269_simplex_affine_fiber_threshold/evidence/main.py
```

For $q=3,4$, every $1\le k<q$, every affine value and each of two
specified nonzero normals (one when these coincide), the program checks
full column rank modulo 65521. This certifies rational independence of
all 29 tested fibers. The non-prime field is
$\mathbb F_4=\mathbb F_2[X]/(X^2+X+1)$.

At $k=q$ and $k=q+1$, it constructs the proof's difference of two
codimension-two fibers for both normals and every affine value. For all
28 trades it checks the support size $2q^{q-2}$, disjointness of the two
terms, and a zero image under the actual integer tensor matrix. Each
term separately has nonzero image, checking the cancellation at the heart
of the construction. The extra coordinate is fixed in the $k=q+1$ cases.

The input domain is fixed in the code. Arithmetic is exact; only the
standard library and repository `tools` package are needed. The run
takes under ten seconds and less than 32 MiB; `--quick` runs the same
complete fixed domain. Failure gives a nonzero exit code. These checks
are diagnostics, not a finite reduction of the general theorem. Its
[Fourier proof](../_proof.md) supplies the all-parameter argument.

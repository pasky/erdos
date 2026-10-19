---
name: research/leads/totient_binary_series/integer_interpolation/evidence
title: Integer Interpolation Evidence
desc: |
  Exact right inverses, predecessor obstructions, and weighted target
  solutions for nine finite shifted-totient interpolation systems, and
  exact witnesses of the aggregated carry criterion through order 384,
  and an exact exercise of the shadow bridge at four depths.
sources: []
created: 2026-09-17T08:47:10Z
updated: 2026-09-17T08:47:10Z
---

# Integer Interpolation Evidence

[[research/leads/totient_binary_series/integer_interpolation/_index|..]]

***

The [[research/leads/totient_binary_series/integer_interpolation/computation|finite
computation account]] states the contract, results, certificate format, and
rerun commands. [main.py](main.py) checks the retained inputs independently
of discovery, and [controls.py](controls.py) exercises its failure protocol.
[produce.py](produce.py) and [reduce.py](reduce.py) are optional discovery
programs with separate dependencies.

The exact certificates are
[k=3](assets/k003.json.gz), [k=4](assets/k004.json.gz),
[k=8](assets/k008.json.gz), [k=12](assets/k012.json.gz),
[k=16](assets/k016.json.gz), [k=24](assets/k024.json.gz),
[k=32](assets/k032.json.gz), [k=48](assets/k048.json.gz), and
[k=64](assets/k064.json.gz). Each contains a complete right inverse, a
proper-image obstruction at the preceding endpoint, and four exact
inhomogeneous solutions with support and cost data. Disposable discovery
products and control scratch belong in ignored `output/`.

The [[research/leads/totient_binary_series/integer_interpolation/carry_criterion|aggregated
carry criterion]] has its own exact witnesses in
[carry_witnesses.json](assets/carry_witnesses.json): exhaustive box minima
at thirteen specified boxes through order 16 and twenty lattice-reduction
witnesses at ten specified orders from 16 through 384, with leading
coefficients one and two. [carry.py](carry.py)
replays every witness independently of discovery (`--quick` for orders
through 8; `--box-minima` re-derives each declared box minimum by
enumeration in under a minute), [carry_controls.py](carry_controls.py)
exercises its failure protocol, and [carry_reduce.py](carry_reduce.py) is
the optional fpylll discovery program whose outputs are not evidence
until replayed.

The carry consumer uses Python integers, standard-library trial division
and the root reporting helpers. Schema 1 retains the leading coefficient,
the ordered sparse coefficient pairs, the exact box when a minimum is
claimed, and the recomputed support, height, cost, reduced ratio and
denominator exclusion. The required roster contains every displayed box
and both leading coefficients at each displayed lattice order. Missing
witnesses, changed box specifications, duplicate specifications or labels,
noninteger data and false arithmetic cause nonzero exit, including under
optimization. The roster is checked even in quick mode, whose arithmetic
coverage remains only the nine witnesses with order at most eight.

From the ordinary prepared repository environment:

```sh
uv run --no-sync python wiki/research/leads/totient_binary_series/integer_interpolation/evidence/carry.py
uv run --no-sync python -O wiki/research/leads/totient_binary_series/integer_interpolation/evidence/carry.py
uv run --no-sync python wiki/research/leads/totient_binary_series/integer_interpolation/evidence/carry_controls.py
```

Normal and optimized full replay each pass 35 checks in under a second,
covering all 33 witnesses, their roster and direct totient controls.
The failure protocol passes 30 expected outcomes: a positive replay and
fourteen corruptions in each mode. These include omitted high-order data
even when quick mode is selected. The optional enumeration re-derives the
thirteen finite-box minima; it is not required to check a retained
feasible witness. No minimum over unrestricted supports is asserted.
Neither these computations nor the conditional counting formulas prove
the uniform cost bound in the
[[research/leads/totient_binary_series/integer_interpolation/two_depth_carries|two-depth
argument]].

The [[research/leads/totient_binary_series/integer_interpolation/shadows|shadows page]]
has its own exact exercise, [shadows.py](shadows.py). At $B=8$ and
$J\in\{32,64,128,200\}$ it realizes the shadows $2^B(q,p)$ of two
consecutive convergents of $S$ as exact scalar-kernel vectors, builds
the $N-3$ cross vectors of the shadow-zero sublattice, rounds the
two-term odd vector against that family, and checks the kernel
identity, the shadows, the nonzero shadow determinant, the cost bounds,
the parity and the support congruence. It separately checks the
determinant-scaled realization, runs four failure controls, replays the
40000-term continued-fraction enclosure consumed by the finite
non-flatness corollary, and checks all four integer inequalities at every
depth from 33 through 19950. It needs no asset: $S$ enters through exact
truncations with rigorous enclosures. The selected consecutive
convergents share the prefix of both enclosure endpoints; the kernel
identity certifies the resulting full-tail error bound. `--quick` runs only
$J=32$. From the ordinary prepared repository environment:

```sh
uv run --no-sync python wiki/research/leads/totient_binary_series/integer_interpolation/evidence/shadows.py
uv run --no-sync python -O wiki/research/leads/totient_binary_series/integer_interpolation/evidence/shadows.py
```

Normal and optimized full runs each pass 34 checks; quick mode contains
16 checks. The recorded costs are outcomes of one
construction with a crude correction step, not minima, and the
exclusions they imply are weaker than the continued-fraction record.

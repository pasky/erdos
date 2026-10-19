---
name: research/leads/concentric_polygon_census/evidence
title: Exact census evidence
desc: |
  Re-runnable cyclotomic enumeration of all critical parameters in two
  bounded symmetric polygon families, with exact event data, every-vertex
  distance checks and strict convexity controls.
created: 2026-10-16T13:41:30Z
updated: 2026-10-16T13:41:30Z
---

# Exact census evidence

[[research/leads/concentric_polygon_census/_index|..]]

***

This is the author evidence for the [finite census](../census.md) and the
[mathematical reduction](../sketch.md). It confers no independent review and
proves no assertion about orders outside the specified ranges.

From the repository root, using the existing repository environment:

```sh
uv run --no-sync python wiki/research/leads/concentric_polygon_census/evidence/main.py
```

The default run rebuilds every positive critical radius for $3\le m\le32$
in the half-step concentric family and every positive critical parameter for
$8\le n\le24$ in the specified affine family. It takes about half a minute
on one thread; runtime varies by machine. Dependencies are SymPy and
python-flint, exercised with versions 1.14.0 and 0.9.0. No solver or network
access is needed. `--quick` checks only $3\le m\le6$ and $8\le n\le10$;
its reduced coverage is printed. The program also works under `python -O`.

## Retained exact inputs

The 47 JSON files under `assets/` are author-generated mathematical event
data, one per order, recomputed and compared in full by `main.py`. They
carry no success logs or cached acceptance. All records are sorted by exact
parameter order. The first event in a record already specifies its exact
parameter; the remaining events record all coincident equations.

- `assets/concentric_MM.json` records the field order $2m$, threshold $m$,
  generic orbit counts, the number of equations, real-root tallies before
  deduplication, and every distinct positive critical radius. An event
  `["P", i, j, branch]` or `["Q", i, j, branch]` uses the polynomial in
  the sketch, $1\le i\le\lfloor m/2\rfloor$ and
  $0\le j<\lceil m/2\rceil$. After making a quadratic monic, branch
  $-1$ means its smaller real root and $1$ its larger; $0$ means the unique
  root of a linear or double-root equation. The intended cyclotomic
  embedding is always $\zeta_{2m}=e^{\pi i/m}$. `position` is `below`,
  `lower_boundary`, `inside`, `upper_boundary` or `above`, relative to the
  open strict-convexity interval. `counts` lists the $A$ and $B$ orbit counts.
- `assets/affine_NN.json` records the field order $n$, threshold
  $\lfloor n/2\rfloor$, generic counts at all pins, pair-equation tallies,
  and every distinct positive critical $s$. An event `[i, j, k]` means the
  quotient $(X_{ik}-X_{ij})/(Y_{ij}-Y_{ik})$ in the sketch, in the embedding
  $\zeta_n=e^{2\pi i/n}$, with $i$ the pin and $j<k$ its two other
  vertices. `counts` lists all pins in order $0,\ldots,n-1$; `circle`
  records exact equality $s=1$. Persistent equalities are accounted for in
  the generic counts and pair tallies, not as isolated parameter events.

See [the order-three input](assets/concentric_03.json) for the two degenerate
convexity endpoints and [the order-four input](assets/concentric_04.json)
for the nonconvex eight-point control. The complete data can be regenerated
with `produce.py --outdir <working-directory>`; that discovery command writes
only to the explicitly named directory. Its output requires the mathematical
checks in `main.py` before use as evidence.

## Checked obligations and failure behavior

The implementation is [exact.py](util/exact.py) for cyclotomic arithmetic,
real-root identities and certified ordering, and [census.py](util/census.py)
for the complete equality equations and distance partitions.

All equalities are rational polynomial identities modulo a cyclotomic
polynomial. Arb enclosures decide only strict order. An overlap triggers an
exact identity test or precision refinement, and an unresolved comparison
fails at the precision limit. No tolerance decides a coincidence.

The checker verifies input range coverage, every event record, every
recorded count, the absence of a convex every-vertex witness, and the exact
two-event pattern in the concentric convex intervals. It checks the
coordinate formulas for affine squared distances by a second construction;
at every affine event it evaluates every pinned distance and reconstructs
all new equalities. For concentric radii it directly partitions all vertex
labels at every admissible event, every event lowering both orbits, and all
events with $m\le5$. Other concentric counts use the complete event lists
and the injectivity proof in the sketch. Reciprocal events must exchange the
two orbit counts.

Controls distinguish quadratic branches, common roots of different
quadratics, repeated roots, linear equations, zero roots, strict convexity
endpoints, and unequal parameters separated by $2^{-300}$. The eight-point
control must have counts $(3,3)$ and fail convexity. A corrupted retained
count or omitted critical record fails the full-data comparison with a
nonzero exit, including under `python -O`. Every asserted computational
obligation is enforced without bare assertions. The noncomputational
generic-complement and convexity arguments remain visible in the sketch.

The affine octagon at $s=1+2\sqrt2$ must have the complete count vector
$(3,6,4,6,3,6,4,6)$; its exact parameter must occur in the enumeration.
It checks that one favorable pin cannot stand in for every vertex.

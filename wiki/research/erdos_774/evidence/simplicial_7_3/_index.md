---
name: research/erdos_774/evidence/simplicial_7_3
title: Inconclusive two-coloring searches for small simplicial boundaries
desc: An exact enumeration of the 3-subset boundaries of [6] and inconclusive solver searches for two-colorings of the boundaries of [7]; no coloring or infeasibility certificate was obtained.
tags: [E0774, computational, simplicial, exploratory, incomplete]
sources: []
created: 2026-09-24T23:30:00Z
updated: 2026-09-24T23:30:00Z
---

# Inconclusive two-coloring searches for small simplicial boundaries

[[research/erdos_774/evidence/_index|..]]

***

## Question

The [simplicial route](../../routes/simplicial_extraction.md) has uniform
extraction at $n/k\sim C\log n$ but no unbounded actual coloring theorem.
The columns of $E(n,3)$ are the oriented triangle boundaries
$\partial[i,j,k]=[j,k]-[i,k]+[i,j]$ for $0\le i<j<k<n$. The searches below
asked whether the smallest interesting instances admit two fully
dissociated colors. **There is no mathematical conclusion from these
tests.**

## Exact enumeration at n = 6

For $n=6$, all $3^{10}=59049$ assignments on triangles avoiding zero were
enumerated, the other coefficients were solved exactly, and all
$2^{20}=1048576$ subsets were checked. The enumeration reported 1,011
signed supports, 450 minimal supports, maximum dissociated size 11 (with
120 maximizers), and 13,884 ordered two-colorings. No randomness or solver
was used, and no script is retained.

## Inconclusive solver searches at n = 7

For the 35-column $n=7$ input, mixed-integer searches used default solver
settings with no specified seed:

- initial 35 tetrahedron constraints, a cap of 150 rounds, each with at
  most one 10-second coloring call and two 5-second relation calls; the
  round cap was reached without deciding two-colorability;
- 2,870 augmented constraints from six-vertex restrictions, a cap of 300
  rounds with the same call limits, invoked twice; the retained output
  records a timeout without incumbent in the first coloring call;
- one relaxed maximum-size call capped at 20 seconds, followed by at most
  one 5-second relation call; its 17-column incumbent (reported upper
  bound 21) had a verified ten-column relation and was not a dissociated
  witness.

The retained [alternating search](produce.py) is the $(n,k,q)=(7,3,2)$
instance. It constructs the complete triangle-to-edge boundary matrix,
starts with the elementary tetrahedral boundary supports, and alternates a
binary coloring feasibility problem with two ternary relation-separation
problems, adding each monochromatic relation found in a color class as a
new support. Every returned relation is checked by exact integer matrix
multiplication before it is added. The caps are 100 rounds and 10 seconds
per solver call, with at most three calls per round. In the original run
the round cap was reached in under a second with 156 support constraints,
and neither a proper-color certificate nor an infeasibility certificate was
produced. Solver-dependent choices need not reproduce the same intermediate
constraints; the bounds and the question are exact.

## Scripts

The script needs NumPy and SciPy, which the repository does not declare,
and writes its final state to the ignored `output/` folder beside it. There
is no checker: an inconclusive search is not evidence, and this folder
contributes nothing to the aggregate evidence entry point.

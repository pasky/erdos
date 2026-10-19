---
name: research/erdos_592/height_three_evidence
title: Evidence for the height-three attack
desc: |
  Checks explicit selected union trees and their partition-cell endpoints,
  the first-tree synchronization obstruction, fixed-shape schedules through
  height three, and a separately qualified finite global-state adversary
  model. No adaptive-game or ordinal conclusion is certified.
created: 2026-10-14T15:17:47Z
updated: 2026-10-14T15:17:47Z
---

# Evidence for the height-three attack

[[research/erdos_592/_index|..]]

***

The entry point `main.py` checks the finite statements used by
[[research/erdos_592/height_three_attack|the height-three attack]]. It
retains three selected union trees for the first shape $1$-$1$-$3$ and
second shape $1$-$2$-$(1,1)$, and the explicit event schedule. It checks
both projections of each union tree, replays the three games, and
separately derives the actual convex leaf cells to check every nonfinal
maximum. A negative control replaces the first single mark by a double
and must fail the cell check. Exhaustive merging for this fixed pair
also confirms that no schedule keeps the first tree entirely synchronized.
The owning page gives the symbolic obstruction and the expansion proof
for arbitrary infinite sets and finite move thresholds.
The adjacent shape pair $1$-$1$-$4$ / $1$-$3$-$(1,1,1)$ is also checked:
it has a schedule, but none keeping the last tree entirely synchronized.

The full shape census covers height one with degree and leaf bounds $6$,
height two with degree bound $4$ and leaf bound $6$, and height three
with degree bound $3$ and leaf bound $6$: respectively $12$, $1287$ and
$33{,}278$ pairs, including an empty second shape when appropriate.
Every found schedule is checked by both the turn replay and the cell
reconstruction. The quick mode reduces only the height-three range to
degree bound $2$ and leaf bound $4$, or $203$ pairs. Height-one boundary
cases and the other stated witnesses run in both modes.

The separate adversary probe permits counts $1,\ldots,K$ at every
selected node, including the roots, with access to the whole three-game
state. Its lower-total filter ignores bounded upper totals and does not
establish correct completion or game locality. Its reported wins are
outcomes of that artificial finite process, not actual winning Architect
strategies. The program and owning page state all of its cases.

Run from the repository root:

```sh
uv run --no-sync python wiki/research/erdos_592/height_three_evidence/main.py
```

Add `--quick` for the reduced census or `-O` immediately after `python`
to check that optimization cannot remove the obligations. The program
uses exact integer counts, deterministic finite enumeration, the standard
library and the root `tools` package. It needs no external data, writes
no output files, and fails through a nonzero exit. The full run takes
about nine minutes and can use about four gigabytes; the quick run takes
under a minute. These are author checks, not independent review. No
partition relation or strategy reading arbitrary numerical histories is
certified.

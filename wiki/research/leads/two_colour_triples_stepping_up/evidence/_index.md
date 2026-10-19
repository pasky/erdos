---
name: research/leads/two_colour_triples_stepping_up/evidence
desc: |
  Deterministic finite checks of the fixed-query, prefix-selected XOR and
  copy-squaring obstructions, and exhaustive verification of a sixteen-point
  routing table, recomputing every relevant triple colour.
tags: []
sources: []
created: 2026-10-16T14:25:13Z
updated: 2026-10-16T14:25:13Z
---

# research/leads/two_colour_triples_stepping_up/evidence

[[research/leads/two_colour_triples_stepping_up/_index|..]]

***

[main.py](main.py) checks the explicit constructions behind
[[research/leads/two_colour_triples_stepping_up/bounded_query_obstruction|the bounded-query obstruction]]
and
[[research/leads/two_colour_triples_stepping_up/copy_squaring_obstruction|the copy-squaring obstruction]]
on deterministic instances: 40 bounded-query rules on cubes of dimension 14
to 26 (random query sets and windows), 12 rules that also read the common
prefix (built with contexts, with a control showing that the construction
without contexts fails for some of them), all 256 outsider-bit tables over two
seed graphs on 16 labels, and both squaring rules over a 14-point seed with a
planted red 7-set. For each rule it builds the red and blue trees of the
product inequality, with labels repeated where the proof allows, checks that
their sizes multiply to more than the number of labels and that no two
demands on an outsider bit disagree, and realizes them as words; for every
instance it recomputes the colour of every triple of the claimed
monochromatic set from the rule. Two controls per rule check that the rule
takes both colours and that a square on a pair with mixed values is not
monochromatic.

It also checks the table in
[prefix_selector_16.json](assets/prefix_selector_16.json) for the
[[research/leads/two_colour_triples_stepping_up/prefix_routing|prefix-selected XOR family]].
The asset's edge rows are $(p,q,\varphi(p,q))$; query rows are
$(p,P,q,h(P,p,q))$. They cover every admissible key in dimension four,
with no omitted or duplicate keys. The driver directly evaluates all 560
triple colours, checks all 4,368 five-sets, checks a four-set in each
colour, and checks a triple on which prefix-dependent query selection
changes the colour. The asset was found by finite constraint search and
contains only the exact colouring data and its witnesses, not a success
log. Verification needs no solver. It proves nothing about unbounded
dimension or the sufficient routing lemma.

A prefix-independent one-query control, specified on that page,
also passes all 4,368 five-set checks and the two four-set witnesses. The
driver checks it to prevent interpreting the finite example as evidence
that prefix selection is essential to this finite bound.

For the prefix-selected XOR obstruction, the driver constructs sparse
canonical trees in dimensions 64, 512, 4,096 and 32,768, using four query
families and both target colours. It checks that no selected pair queries
a different selected label, that each node's prefix agrees with a separate
calculation using only the higher labels, and that every triple of the
realized words has the target colour. The families query the lower delta,
a nearby position selected by the prefix, the prefix modulo the upper
delta, or a hash-selected position. Label sets are deterministic sparse
samples, with a bounded retry loop that fails explicitly if none is found.
No assertion about all routing tables is inferred from these finite samples.

Run it from the repository root with
`uv run --no-sync python wiki/research/leads/two_colour_triples_stepping_up/evidence/main.py`;
it takes about a second, uses no randomness beyond BLAKE2b of fixed strings,
and exits nonzero if any check fails. It checks finite instances only: the
universal statements rest on the proofs on the three pages, and the
random-deletion bound on the spread label set is not exercised (the driver
chooses spread sets greedily).

[produce.py](produce.py) is an optional synthesis probe, outside the default
check. It uses the pinned `z3-solver` dependency to search every graph seed
and routing table at one specified dimension and forbidden size. A SAT
model is re-evaluated with integer operations and exact clique search;
UNSAT is a solver-dependent finite finding, without an independently
checked proof trace. Unknown or timeout exits nonzero. Neither outcome
supplies a uniform construction; the routing assertion for this family is
refuted by the written obstruction. For example, from the repository root:

```sh
uv run --no-sync python \
  wiki/research/leads/two_colour_triples_stepping_up/evidence/produce.py \
  6 6 --lazy --bitvectors --seconds 180 \
  --output wiki/research/leads/two_colour_triples_stepping_up/evidence/output/selector_6_6.json
```

This finite instance takes about two minutes on the tested environment;
the time cap may produce unknown on another machine. Dimensions 3 and 5
with respective forbidden sizes 4 and 5 take about a second. The dimension
is restricted to 2 through 6 to bound this probe's scope. The synthesis
output is disposable diagnostic data; the checked sixteen-point witness
is retained separately under `assets/` and checked by `main.py`.

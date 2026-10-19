---
name: research/erdos_699/computations
title: "Erdős 699: computations and reproducibility"
desc: "Entry points for checking the completed proofs, with their retained certificates and the earlier computations preserved together."
created: 2026-09-22T19:09:27Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: computations and reproducibility

[[research/erdos_699/_index|..]]

***

Start with the mathematical proofs at
[seven](../proofs/details/index_7_complete.md) and
[nine](../proofs/details/index_9_complete.md). Their combined
checkers join the numerical infinite tails to the finite exclusions:

| Case | Combined checker | Retained proof record |
| --- | --- | --- |
| $i=7$ | [Python](erdos_699_index_7_complete.py) | [JSON](erdos_699_index_7_complete.json) |
| $i=9$ | [Python](erdos_699_index_9_complete.py) | [JSON](erdos_699_index_9_complete.json) |

With the [pinned dependencies](../evidence/assets/erdos_699_interpolation_requirements.txt)
installed in the repository's `.venv/`, run these commands from the
repository root:

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_7_complete.py
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_9_complete.py
```

These commands check the retained proof records without replacing them.
They verify numerical source bounds, all retained initial interval
inequalities, exact polynomial coverage, the joint interval bindings, and
the overlap with the finite range. They reuse the interpolation ranks.
By default each then regenerates every joint witness sequence, 9,811,438
witnesses at seven and 11,599,987 at nine, and compares the count and
sequence digest of every direction with the retained joint record. The
replay builds the directed prime-log cache through $10^{10}$ under the
ignored repository directory `tmp/erdos699/` on first use, about 2.3 GB
in under a minute, and the regeneration takes roughly an hour of processor
time per index, under ten minutes of wall time with the default eight
worker processes (`--workers`) on the machine used here. `--quick` skips
the regeneration, checks only the source and endpoint bindings of the
retained joint record, and says so in its output; `--compact-cache`
relocates the cache.

## Longer replays

The [seven](erdos_699_index_7_height_cover.py) and
[nine](erdos_699_index_9_height_cover.py) joint-source drivers accept
`--check` for their retained source and endpoint checks, and can be run
on their own as the combined checkers run them. They load the compact
prime-log cache that a combined checker builds on first use; build it
separately with `erdos_699_compact_prime_prefix.py --limit 10000000000
--base-limit 100000000 --cache-dir tmp/erdos699/compact-prime-prefix-10000000000`,
and pass another location with `--compact-cache`. Use a separate output
file under the ignored repository `tmp/` when reconstructing sequences:

```sh
mkdir -p tmp/erdos699
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_7_height_cover.py --replay --reuse wiki/research/erdos_699/computations/erdos_699_index_7_height_cover.json --output tmp/erdos699/erdos699-seven-replay.json
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_9_height_cover.py --output tmp/erdos699/erdos699-nine-replay.json
```

At seven, `--replay` compares each reconstructed witness count and sequence
digest with the `--reuse` record. At nine, compare those fields in the
output with the retained record; the driver has no `--replay` option.
Execution times and other diagnostic fields need not match.

The initial-source certificates retain every witness. Their separate
drivers can additionally reconstruct all pointwise coefficient-gcd bounds:
[seven](erdos_699_index_7_initial_height_cover.py) does this by default,
while [nine](erdos_699_index_9_initial_height_cover.py) uses
`--replay-gcd`. Both accept `--cache`. The proof notes distinguish these
replays from the checks performed by the combined drivers.

## How the files are kept

The scripts, source tables, proof records, and older experiments remain
in one directory because they import one another and locate their inputs
as siblings. The relocation preserved every computation file byte for
byte. A retained record names its inputs by basename and carries no digest
of them; a checker validates an input by loading it and checking its domain
and coverage, never by a hash. The digests a record does carry are the
expected digests of recomputed objects listed under "Computed-result
digests" in the verification guide. Follow the links from the relevant
mathematical note to
find its supporting computation; this page is not an inventory of every
intermediate file.

Some older docstrings and three historical JSON records retain the former
`research/finite_experiments/` paths. These are preserved provenance;
the applicable readers resolve the data by sibling basename. For current
commands, use `wiki/research/erdos_699/computations/` as above.
The pinned requirements cover the principal proof checkers; individual
older experiments may state additional dependencies in their docstrings.

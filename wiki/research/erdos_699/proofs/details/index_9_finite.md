---
name: research/erdos_699/proofs/details/index_9_finite
title: "Erdős 699: finite exclusion at index nine through 10^241547629"
desc: "Two finite cofactor cliques and degree-42 weighted ramps reduce index nine to 607,975 intervals and thirteen exact rows. The numerical infinite tail remains separate."
created: 2026-09-22T17:10:03Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: finite exclusion at index nine through 10^241547629

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/proofs/details/index_7_finite|The companion index-seven calculation]]

***

**Theorem.** There is no admissible bad triple with $i=9$ and
$n\le10^{241\,547\,629}$, for the original threshold $p\ge9$.

This is an unconditional finite-range result. A numerical infinite-tail
theorem at or below this exponent would complete index nine; that theorem
is a separate input, not asserted by this file.

The [combination checker](../../computations/erdos_699_index_9_finite.py)
and its [certificate](../../computations/erdos_699_index_9_finite.json)
use two finite cofactor calculations:

| Input range | Complete prime graph | Exponent | Weighted-ramp consequence |
| --- | --- | --- | --- |
| $n\le10^{241\,547\,629}$ | $2,3,5,7$ | $41/100$ | $n<10^{122}$ |
| $n\le10^{122}$ | $2,3,5,7$ | $9/20$ | $n<10^{25}$ above the exceptional pair heights |

Both ramps have $k=6$, degree $42$, and row multiplicities $12-t$ for
$0\le t<9$. Their minimum gains, including every possible collision of
selected prime-power positions, are respectively $3/10$ and $3/2$.
The first pair certificate's exceptional heights are below $10^{122}$.
The second certificate's largest exceptional threshold is below $10^{26}$.
Thus every bad triple in the stated finite range would have to satisfy
$n<10^{26}$.

The [first clique](../../computations/erdos_699_prime_pair_strips_9_extended.json)
was certified by the
[logarithmic strip generator](../../computations/erdos_699_prime_pair_log_strips.py).
It uses 128, 123, 123, 120, 120, and 117 anchors for the six pairs.
The [earlier certificate](../../computations/erdos_699_prime_pair_strips_9_global.json)
through $10^{27\,027\,659}$ is preserved. The extension adds respectively
13, 14, 13, 13, 13, and 14 anchors, with no new exceptions. The generator
verifies that every retained boundary check was untruncated, then continues
from its final exponent orthant. Each continued certificate names its
prefix file and reproduces the prefix's anchors, boundary checks and
height cap, as in the index-seven continuation proof.
The [second clique](../../computations/erdos_699_prime_pair_strips_9_middle.json)
uses the same exact CRT argument at the smaller cap. Both allow every
factor difference through eight.

The final [interval driver](../../computations/erdos_699_index_9_finite_intervals.py)
also uses the older complete $2/5$ clique through $10^{1732}$ as a fallback
where a stronger edge is unavailable. Each edge is disabled on its precise
exceptional row windows.

The terminal-prime lemma covers the prefix below row $113$. The remaining
range is excluded by **607,975 certified intervals** and **thirteen exact
rows**, all at most $5,832$. The exact part checks **6,762 columns** and
finds a common prime at least nine in every case. The smallest directed
logarithmic margin is greater than $0.00000218172979727$.

The [interval output](../../computations/erdos_699_index_9_finite_intervals.json)
records the partition hash, the source file names, every residual row, and
the count of exact column gcd checks. No modular polynomial ranks are recomputed
for this finite argument. Reproduce the interval and combination steps
with the
[pinned dependencies](../../evidence/assets/erdos_699_interpolation_requirements.txt)
installed in the repository's `.venv/`:

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_9_finite_intervals.py
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_9_finite.py
```

**Complete result.** The [combined proof](index_9_complete.md)
excludes every admissible bad triple at nine. The estimates below
are retained as components of that proof.

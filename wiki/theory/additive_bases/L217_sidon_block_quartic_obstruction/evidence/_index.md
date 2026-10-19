---
name: theory/additive_bases/L217_sidon_block_quartic_obstruction/evidence
title: "Exact finite witness"
desc: "Exhaustive rational evaluation of the block law and a capacity-limited uniform mixture at N=63, including a signed cyclic control and separate direct enumeration."
created: 2026-10-15T20:05:11Z
updated: 2026-10-15T20:05:11Z
---

# Exact finite witness

[[theory/additive_bases/L217_sidon_block_quartic_obstruction/_index|..]]

***

The [entry point](main.py) computes the finite witness displayed on
[[theory/additive_bases/L217_sidon_block_quartic_obstruction/_index|L217]].
At $N=63$, $k=9$, block length $21$ and occupancy $3$, it enumerates every
subset of sizes two, three and four and every one of the 21 distinct block
rotations. Falling-factorial inclusion probabilities and all accumulations
are exact. An explicit bound excludes integer overflow.

A separate control enumerates every outcome and rotation of the law with
three blocks of length four and occupancy two, comparing the resulting
short-pair mean, variance and repeated-difference mass with the moment
calculation. The unmodified variance is also checked to be positive, while
both the zeroed and renormalized centered-square expectations are negative
at the retained witness.

The calculation also treats the mixture with weight $33/82$ on the uniform
law on all nine-element sets. It satisfies every difference and sum capacity,
with equality at difference one, yet its zeroed and renormalized short-pair
square is negative. The uniform component's mean and variance are checked
against independent graph intersection counts, and the mixture against the
law of total variance.

For the signed cyclic polynomial $F$ in the final part of the proof, the same
small mixture instead gives the positive value

$$
\mathcal L((F-\mathbb E F)^2)
=\frac{26206418542771452345267619483}{89042295412084245797931582420}.
$$

This is a finite limitation: that part of the theorem asserts negativity
only for sufficiently large parameters. Signed genuine moments have a
separate direct-enumeration control on the small block law. Accumulations
use bounded integer arrays or exact Python integers where needed.

From the repository root, run
`uv run --no-sync python wiki/theory/additive_bases/L217_sidon_block_quartic_obstruction/evidence/main.py`.
The full run and `--quick` have the same finite coverage, take under ten seconds
and use under 300 MB with one thread. Dependencies are NumPy and the root
tools package. No external input or saved output is required. This witness
does not prove the asymptotic statement; that is the scope of the written
argument.

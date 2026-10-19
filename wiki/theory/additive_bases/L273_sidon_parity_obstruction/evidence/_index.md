---
name: theory/additive_bases/L273_sidon_parity_obstruction/evidence
title: "Exact parity controls"
desc: "Exhaustive rational moment checks for the parity identity at N=8,16,54, both block rotation conventions and three mixture weights, with an independent direct sample-space calculation at N=8."
created: 2026-10-16T00:12:37Z
updated: 2026-10-16T00:12:37Z
---

# Exact parity controls

[[theory/additive_bases/L273_sidon_parity_obstruction/_index|..]]

***

The [entry point](main.py) checks the finite controls for
[[theory/additive_bases/L273_sidon_parity_obstruction/_index|L273]]. It
enumerates every two-, three- and four-element support at
$(s,W)=(2,4),(2,8),(3,18)$, and every distinct rotation when averaging the
block law. For both rotation conventions and mixture weights $0,1/2,1$, it
checks the centered parity square, degree totals and positive renormalization
denominators in exact rational arithmetic. The square coefficients are
compared with direct edge pairings; balanced hypergeometric distributions
give a separate calculation of the genuine moments. At $(s,W)=(2,4)$ it
also enumerates every whole-set outcome of both laws and directly evaluates
the original and zeroed square.

The checks do not require a negative square at these small parameters and
do not prove the asymptotic estimate. That conclusion rests on the written
proof. There are no external inputs or output files. From the repository root:

```sh
uv run --no-sync python wiki/theory/additive_bases/L273_sidon_parity_obstruction/evidence/main.py
```

Default and `--quick` have the same exhaustive coverage. Allow thirty seconds
and 300 MB with one thread. The only dependencies are NumPy and the root
`tools` package; all theorem-relevant arithmetic is integer or rational.

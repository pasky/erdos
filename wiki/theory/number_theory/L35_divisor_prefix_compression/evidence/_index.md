---
name: theory/number_theory/L35_divisor_prefix_compression/evidence
title: Complete divisor-prefix minima through 64
desc: Exhaust all distinct-part partitions, check their counts independently, and compare the minima with an exact divisor sieve.
created: 2026-10-14T18:42:37Z
updated: 2026-10-14T18:42:37Z
---

# Complete divisor-prefix minima through 64

[[theory/number_theory/L35_divisor_prefix_compression/_index|..]]

***

From the repository root run:

```sh
uv run --no-sync python wiki/theory/number_theory/L35_divisor_prefix_compression/evidence/main.py
```

The [input](assets/input.json) specifies $2\le N\le64$ and a secondary
divisor-sieve limit of $10000$. The [exact table](assets/values.json)
records the minima, witnesses and partition counts computed by Plasma AI.
Every run recomputes the table using the
[compression formula](../_proof.md); its completeness does not depend
on the sieve limit. All arithmetic is integral and exact.

The checker validates input coverage, counts and uniqueness of partitions,
all witnesses and minima, the independently counted partition domain,
the divisor-sieve comparison, and the stated boundary and extremal
conclusions. It uses the repository's evidence harness and standard Python
library. Expected runtime is less than a minute. Any failed obligation
gives a nonzero exit, also under optimized Python. There is no reduced
quick mode, discovery search beyond the stated finite domain, or
asymptotic inference.

---
name: research/smooth_lcm_three_prime/evidence
desc: |
  Exact checks of the three-prime running-lcm expansions, the triangular
  witnesses for the face-rank obstruction, and formal relation searches with positive controls;
  domains and limitations are stated on the owning research page.
tags: []
sources: []
created: 2026-10-15T15:50:35Z
updated: 2026-10-15T15:50:35Z
---

# research/smooth_lcm_three_prime/evidence

[[research/smooth_lcm_three_prime/_index|..]]

***

The [entry point](main.py) uses the root Python environment, numpy, mpmath
and the shared `Checker`; it reads no files and writes no output. Run it from
the repository root:

```sh
uv run --no-sync python wiki/research/smooth_lcm_three_prime/evidence/main.py
```

Its helpers live in `util/`: exact integer decisions of every floor of a
logarithm, and formal power series with relation counts modulo a prime. The
[[research/smooth_lcm_three_prime/_index|owning research page]] states what
each check covers. A zero relation count proves that no relation of the stated
shape exists; the two positive controls show that the computation detects the
known relations. No check bears on the irrationality of any series.

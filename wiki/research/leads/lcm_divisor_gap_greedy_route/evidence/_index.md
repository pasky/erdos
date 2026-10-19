---
name: research/leads/lcm_divisor_gap_greedy_route/evidence
title: Evidence
desc: |
  One exploratory script profiling the consecutive divisor gaps of
  lcm(1, ..., x); no entry point, no checks, and no evidence for any claim.
tags: []
sources: []
created: 2026-09-28T07:43:12Z
updated: 2026-09-28T07:43:12Z
---

# Evidence

[[research/leads/lcm_divisor_gap_greedy_route/_index|..]]

***

The retained script [`gap_profile.py`](util/gap_profile.py) is an
exploratory computation, not evidence for any claim: it enumerates the
divisors of $L_x=\operatorname{lcm}(1,\ldots,x)$ and prints the gap
profile that [the lead](../_index.md) tabulates. There is no entry point
and nothing is checked, so a run certifies nothing. It uses the root
Python environment and no third-party package. Run it from the repository
root:

```sh
uv run --no-sync python wiki/research/leads/lcm_divisor_gap_greedy_route/evidence/util/gap_profile.py 20 30 40 50 60 64
```

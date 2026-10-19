---
name: research/finite_experiments/binomial_gcd_search/evidence
desc: |
  Exact enumeration of the binomial-gcd thresholds through order thirty,
  using the stated finite domain and inline arithmetic witnesses.
tags: []
sources: []
created: 2026-09-08T18:16:13Z
updated: 2026-09-08T18:16:13Z
---

# research/finite_experiments/binomial_gcd_search/evidence

[[research/finite_experiments/binomial_gcd_search/_index|..]]

***

The [entry point](main.py) recomputes all 1,015 eligible triples and checks
the non-strict threshold, four strict exceptions, and exact witnesses. It
uses the root Python environment and shared failure harness, reads no input
files, and writes no output files. Run it from the repository root:

```sh
uv run --no-sync python wiki/research/finite_experiments/binomial_gcd_search/evidence/main.py
```

The [[research/finite_experiments/binomial_gcd_search/_index|owning account]]
states the mathematical question, exact domain, observed results, runtime,
and verification limits. This finite check supplies no all-order proof.

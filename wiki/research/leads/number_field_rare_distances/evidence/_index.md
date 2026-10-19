---
name: research/leads/number_field_rare_distances/evidence
desc: |
  Exact distance spectra for all nonempty subsets of a four-by-four grid
  after two algebraic maps, and a seven-point example with a rich distance.
created: 2026-09-22T20:37:22Z
updated: 2026-09-22T20:37:22Z
---

# research/leads/number_field_rare_distances/evidence

[[research/leads/number_field_rare_distances/_index|..]]

***

The [finite probe](main.py) belongs to the
[[research/leads/number_field_rare_distances/_index|number-field research
argument]]. It checks all 65,535 nonempty subsets of a four-by-four integer
grid after the two stated algebraic maps, using integer coefficient
representations of squared distances. It also checks the complete retained
seven-point spectrum, including a distance occurring eight times.

Run from the repository root:

```bash
uv run --no-sync python wiki/research/leads/number_field_rare_distances/evidence/main.py
```

The standard library and the root `tools` package are sufficient. There
are no input files or random choices; the full run takes a few seconds.
Every failed obligation produces a nonzero exit, including with Python
assertions disabled. The finite domain does not prove an unrestricted or
asymptotic statement, and these author checks are not independent review.

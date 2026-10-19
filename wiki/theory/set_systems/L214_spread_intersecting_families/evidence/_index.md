---
name: theory/set_systems/L214_spread_intersecting_families/evidence
desc: Exact brute-force checks of the block-family bound, the substitution recursion and two small spread instances behind L214.
tags: []
sources: []
created: 2026-10-15T17:54:12Z
updated: 2026-10-15T17:54:12Z
---

# theory/set_systems/L214_spread_intersecting_families/evidence

[[theory/set_systems/L214_spread_intersecting_families/_index|..]]

***

The entry point `main.py` builds every member of eight small block families
and five small substitutions and checks, in exact rational arithmetic, the
containment bound of Lemma 3, the spread recursion of Lemma 2, and the spread
of $B(2,4)$ and $B(2,2)^2$. It covers finite instances only; the general
statement and the thinning part rest on the written proof. Run it from the
repository root with
`uv run --no-sync python wiki/theory/set_systems/L214_spread_intersecting_families/evidence/main.py`;
it takes a few seconds and exits with status 0 when every check passes.

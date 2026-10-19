---
name: theory/set_systems/L215_spread_large_core_sunflowers/evidence
desc: Exact checks of the triangle powers, the core lemma on two small substitutions and the spread recursion behind L215.
tags: []
sources: []
created: 2026-10-15T18:17:48Z
updated: 2026-10-15T18:17:48Z
---

# theory/set_systems/L215_spread_large_core_sunflowers/evidence

[[theory/set_systems/L215_spread_large_core_sunflowers/_index|..]]

***

The entry point `main.py` builds the triangle powers $D$, $D^2$, $D^3$ and the
substitutions $B(3,3)[D]$ and $B(2,3)[D]$ member by member. It checks that the
triangle powers are intersecting and free of $3$- and $4$-sunflowers, checks the
excess of Lemma A for $D$ and $D^2$, and verifies that the smallest
$3$-sunflower cores of the two substitutions have exactly the sizes Lemma B
predicts. It also checks the spread recursion on $B(3,3)[D]$. These are finite
instances; the statement for
general parameters rests on the written proof. Run it from the repository root
with
`uv run --no-sync python wiki/theory/set_systems/L215_spread_large_core_sunflowers/evidence/main.py`;
it takes a few seconds and exits with status 0 when every check passes.

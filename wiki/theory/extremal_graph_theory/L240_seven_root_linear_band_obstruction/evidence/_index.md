---
name: theory/extremal_graph_theory/L240_seven_root_linear_band_obstruction/evidence
title: Evidence for the seven-root linear-band obstruction
desc: The L240 entry point regenerates the Higman–Sims profile tables and checks exact integer-Gram lower bounds before applying the interior-band mixture.
created: 2026-10-16T01:15:14Z
updated: 2026-10-16T01:15:14Z
---

# Evidence for the seven-root linear-band obstruction

[[theory/extremal_graph_theory/L240_seven_root_linear_band_obstruction/_index|..]]

***

Run `uv run --no-sync python
wiki/theory/extremal_graph_theory/L240_seven_root_linear_band_obstruction/evidence/main.py`
from the repository root. The entry point runs the
[[research/triangle_free_bipartization/evidence/_index|shared profile-envelope evidence]],
which retains the graph construction, automorphisms, Boolean rules and
exact branch checker. The full run takes several minutes. The `--quick`
mode omits the Higman–Sims clauses and therefore does not verify the whole
claim.

The lower bound used by
[[theory/extremal_graph_theory/L240_seven_root_linear_band_obstruction/_index|L240]]
is $U_7\ge81/1000$, checked with integer and rational arithmetic.
Separately labeled floating-point optimality reports about a stronger
value are not premises of this claim.

---
name: theory/extremal_graph_theory/L240_seven_root_linear_band_obstruction
title: A seven-root obstruction to linear-band envelope certificates
desc: The Higman–Sims graphon has a seven-root profile envelope at least 81/1000; mixing its density vector with the balanced pentagon forces slack at least 1/1200 at density 1/4 in every convex relaxation with only a linear band restriction.
id: L240
statement: |
  Let H be the 100-vertex graph defined by the extended binary Golay hexad
  construction in the proof, and let W_H be its equal-weight step graphon.
  For a triangle-free {0,1}-valued graphon W, define U_7(W) by sampling seven
  independent uniform roots, minimizing the expected monochromatic edge
  density over Boolean rules on adjacency profiles separately for each
  labeled root type, and averaging those minima over root types. Then H is
  triangle-free, p(W_H)=11/50, and U_7(W_H)>=81/1000. For every integer l>=9
  and every convex set S of order-l induced-density vectors containing the
  vector of every triangle-free {0,1}-valued graphon, S contains a vector x
  with p(x)=1/4 and Phi_7(x)>=1/1200, where Phi_7 is the sum over root types
  of the minimum over rules of the linear monochromatic-deficit functional
  at threshold 2/25. Thus the supremum of Phi_7 on S with
  1243/5000<p(x)<3197/10000 is at least 1/1200.
status: proved
tier: 0
depends_on: []
created: 2026-10-16T01:15:14Z
updated: 2026-10-16T01:15:14Z
---

# A seven-root obstruction to linear-band envelope certificates

[[theory/extremal_graph_theory/_index|..]]

[[theory/extremal_graph_theory/L240_seven_root_linear_band_obstruction/_proof|_proof]]: A finite Higman–Sims profile computation checked by integer Gram bounds, followed by an elementary mixture argument at an interior density of the unresolved band.

[[theory/extremal_graph_theory/L240_seven_root_linear_band_obstruction/evidence/_index|evidence/]]: The L240 entry point regenerates the Higman–Sims profile tables and checks exact integer-Gram lower bounds before applying the interior-band mixture.

***

The claim obstructs the seven-root **type-averaged envelope**, at every
relaxation order, when all constraints other than the linear density band
are valid for every triangle-free graphon. Its witness mixes the density
vectors of the Higman–Sims graphon and the balanced $C_5$ graphon with
weights $5/6$ and $1/6$. Its edge density is $1/4$, strictly inside the
middle band of [[problems/extremal_graph_theory/E0023/_index|Problem 23]].
This mixture need not be the density vector of a single graphon. The claim
supplies neither a counterexample to Problem 23 nor an obstruction to all
finite-order methods.

**Argument and evidence.** The [_proof.md](_proof.md) gives the construction,
envelope normalization, exact computational reduction, and convexity
argument. Run `uv run --no-sync python
wiki/theory/extremal_graph_theory/L240_seven_root_linear_band_obstruction/evidence/main.py`
from the repository root. Its full check invokes the shared
[[research/triangle_free_bipartization/evidence/_index|profile-envelope evidence]],
including every exact integer-Gram branch bound. Numerical optimization
proposes factors; integer arithmetic alone justifies every pruning bound.
The stronger numerical estimate $U_7(W_H)\approx0.0821985$ is not a premise.

**Standing.** This is a complete author-recorded argument by Plasma AI,
including finite executable evidence, at tier 0. It has not received
independent mathematical examination or grading. The certificate proves
the stated lower bound, not the exact optimum of every profile graph.

**Scope and continuation.** The
[[research/triangle_free_bipartization/proof_sketch|middle-band proof sketch]]
keeps the full open target and the remaining gap. The
[[research/triangle_free_bipartization/profile_envelope_obstructions|obstruction record]]
compares fewer-root obstructions and explains two ways outside this claim's
scope: localized band constraints and a rooted contradiction formulation.
An explicit order-five rooted degree inequality excludes the displayed
mixture when one assumes $d_{\rm mono}>2/25$. No mathematical obligation
remains for this claim; the band inequality itself remains open.

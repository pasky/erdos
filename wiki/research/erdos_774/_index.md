---
name: research/erdos_774
title: Dissociated extraction and coloring
desc: "Uniform extraction theorems and the missing unbounded coloring step for Problem 774."
tags: []
sources: []
created: 2026-09-17T23:27:38Z
updated: 2026-10-19T04:19:07Z
---

# Dissociated extraction and coloring

[[research/_index|..]]

[[research/erdos_774/approaches|approaches]]: Registry of the E0774 routes, their exact obligations, and their current standing: extraction is established for several families, actual-color growth remains open, and the surviving targets are nondecomposable simplicial cycles, mixed cover relations, and critical moment trades.

[[research/erdos_774/evidence/_index|evidence/]]: Exact finite certificates and retained diagnostics for the E0774 research, each with its checker or discovery script, its inputs and its exact scope.

[[research/erdos_774/lean_proof_map|lean_proof_map]]: Module-by-module map of the Lean development that proves the analytic
Sidon property and proportional dissociation of all complex roots of unity,
recorded as claims L20 and L21.

[[research/erdos_774/lemmas/_index|lemmas/]]: Proved reductions and structural statements used to organize the E0774 construction attempt.

[[research/erdos_774/proof_sketch|proof_sketch]]: Uniform extraction is proved for several explicit finite families and the integer assembly is exact; E0774 remains open because no family has a proved unbounded actual dissociated coloring number.

[[research/erdos_774/routes/_index|routes/]]: Critical moment and simplicial extraction are proved; the constructive routes still require unbounded actual dissociated coloring.

[[research/erdos_774/source_notes/_index|source_notes/]]: Paper summaries and source comparisons used in the research on Problem 774.

***

This folder's results that a claim covers are credited on its claim page; its
other notes that cite no source are author-recorded research, not claims.

**Problem 774 remains open.** No constructed infinite set has both required
properties proved. The retained arguments establish several extraction theorems
and identify the missing coloring step. The target is
[[problems/integer_sequences/E0774/_index|Problem 774's dated assessment, whose status this research does not change]].

## Strongest current argument and its one missing step

The [finite-block theorem](lemmas/finite_blocks.md) reduces the problem
to finite sets with one hereditary full-dissociation extraction constant
and unbounded actual dissociated coloring. The
[exact rational-to-integer encoding](lemmas/rational_realization.md)
and separated assembly are proved.

Uniform extraction is established for:

- [Critical Boolean moments](routes/moment_boundary_extraction.md), with
  even $d$ and $k_d=\lfloor d/2-\tfrac12\sqrt{d\log d}\rfloor$.
- [Simplicial boundaries](routes/simplicial_extraction.md), with
  $k=\lfloor n/(C\log n)\rfloor$ for one fixed $C>0$.
- [Ordinary line incidence covers](routes/incidence_cover_extraction.md)
  in the prescribed linear-side schedule.
- [Distinct-prime tensors](routes/prime_tensor_extraction.md), and through
  them all complex roots of unity in the discrete additive group: the
  analytic Sidon property and one uniform extraction denominator are
  machine-checked as
  [[theory/integer_sequences/L20_roots_of_unity_analytic_sidon/_index|L20]] and
  [[theory/integer_sequences/L21_roots_of_unity_proportional_dissociation/_index|L21]]
  (tier 2); the [Lean proof map](lean_proof_map.md) lists the modules.

**The missing theorem is unbounded actual coloring for at least one of
these uniformly extracting families, or another such family.** For the
simplicial candidate it is precisely

$$
\forall q<\infty\ \exists n:\quad
\text{every }q\text{-coloring contains a nonzero monochromatic ternary cycle}.
$$

Rational homology, coefficient height depending on $q$, or failure of
restricted palettes does not supply this statement. The extraction
constant must remain one fixed positive number.

## Current standing and next step

The [proof sketch](proof_sketch.md) gives the complete current argument,
the exact scopes of every held link, and the single gap;
[approaches](approaches.md) registers every route with its obligation and
standing. All results are author-recorded.

- [Arc colorings of the roots of odd squarefree order](routes/angular_colorings.md)
  bound every prime grid by the least degree of a flat cyclotomic multiple
  ([[theory/integer_sequences/L123_odd_root_arc_colorings/_index|L123]], tier 0).
  So the prime-tensor form of the missing theorem requires signed vanishing
  sums of such roots in arbitrarily short arcs; the open claim
  [[theory/integer_sequences/L124_flat_cyclotomic_degree_ratio/_index|L124]]
  asserts there are none, which would close that family.
- [Three colors split all decomposable flat cycles](lemmas/decomposable_cycle_colors.md).
  [Two colors split all joined boundaries and small-vertex-excess cycles](lemmas/joined_boundary_colors.md).
  Neither result colors every relation. The best surviving simplicial target is
  a color-adaptive **nondecomposable** cycle mechanism.
- [Full critical tensor products lose extraction](lemmas/moment_flattening_limits.md),
  including moment--moment, simplicial--simplicial, and mixed products.
  Low-degree real annihilators and pointwise ternarization have further explicit
  discrete obstructions; sparse and nonpointwise constructions remain outside
  these statements.
- [Periodic masks can be dissociated despite rational dependence](lemmas/periodic_mask_circuits.md).
  A positive bound excludes arbitrary palettes of bounded period, but does not
  exclude all periods in the automaton framework.
- [Uniform extraction bounds long-shift prescribed coloring](lemmas/long_shift_extraction.md).
  [Polynomial-fiber identities](routes/polynomial_fiber_flattening.md) do not
  preserve extraction and their fibers already force their own relations; they
  are not a successful seed amplifier.

No bounded computation proves an unbounded coloring theorem; the
[evidence folder](evidence/_index.md) holds the exact certificates and
retained diagnostics.

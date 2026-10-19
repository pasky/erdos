---
name: theory/integer_sequences/L20_roots_of_unity_analytic_sidon/_proof
title: Proof account for the analytic Sidon property of the roots of unity
desc: |
  The prime tensor argument gives a uniform finite estimate, small primes are
  absorbed with a fixed factor, and cyclotomic decomposition transfers the
  bound to all roots of unity; this account maps the Lean modules.
tags: []
sources:
- theory/integer_sequences/L20_roots_of_unity_analytic_sidon/_index
created: 2026-09-25T22:01:44Z
updated: 2026-10-13T13:08:56Z
---

***

This proves the entire statement of
[[theory/integer_sequences/L20_roots_of_unity_analytic_sidon/_index|L20]]
by machine-checked Lean, at tier 2 for the Lean sources of 2026-09-28 that
the card's standing names; the prose route it formalizes is the
[[research/erdos_774/routes/prime_tensor_extraction|prime tensor extraction route]],
and the [[research/erdos_774/lean_proof_map|Lean proof map]] lists the
modules stage by stage. The formal entry point is
`Erdos.Research.Problem774.rootsOfUnity_analyticSidon` in
`lean/Erdos/RootsOfUnitySidon/RootsOfUnitySidonAnalytic.lean`: a cutoff prime
with a uniform half parameter on every finite tail stage
(`exists_cutoff_uniform_stage_half_parameter`) feeds
`analyticSidon_of_uniform_tail_parameter`, which absorbs the finitely many
small primes (`SmallPrimeAssembly.lean`) and passes from odd squarefree
orders to all root orders (`OddSquarefreeReduction.lean`,
`RootsOfUnitySidon.lean`, `AntipodalSidon.lean`). The definitions
`rootsOfUnity` and `AnalyticSidon` live in `RootsOfUnitySidon.lean`.

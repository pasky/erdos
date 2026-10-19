---
name: set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs
desc: |
  Plasma AI's 2026 Lean formalization proving that every graph whose finite
  subgraphs on $m$ vertices can be made bipartite by deleting at most $Cm$
  edges has countable chromatic number, and hence that $h_G(n)/n\to\infty$
  for every graph $G$ that is not countably colorable, answering the second
  question of Problem 111; it carries a prose blueprint of the proof.
license: Apache-2.0
created: 2026-10-18T02:15:08Z
updated: 2026-10-19T06:23:35Z
---

# set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs

[[set_theory/_index|..]]

[[set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/corollary|corollary]]: For every graph $G$ that is not countably colorable, of any cardinality,
and in particular for every graph of chromatic number $\aleph_1$, the
least number $h_G(n)$ of deletions that make every $n$-vertex subgraph
bipartite satisfies $h_G(n)/n\to\infty$; its Lean formalization is rebuilt
and kernel-replayed here.

[[set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/evidence/_index|evidence/]]: The held Lean formalization of Plasma AI's Problem 111 result, as the
repository's tree at its pinned commit, and this corpus's verification
records of it.

[[set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/main_theorem|main_theorem]]: For every $C\ge0$, a graph in which every finite subgraph on $m$ vertices
can be made bipartite by deleting at most $Cm$ edges has countable
chromatic number, at every vertex cardinality; its Lean formalization is
rebuilt and kernel-replayed here.

***

Plasma AI, *Erdős Problem 111: bipartizing finite subgraphs of uncountably
chromatic graphs*, Lean formalization with a prose blueprint, October 2026, in
the repository
[plasma-ai/erdos-111](https://github.com/plasma-ai/erdos-111/tree/de72caf0e388c729697b6813f4ea90bfe1617c7b)
at commit de72caf (2026-10-19 UTC). The blueprint is `blueprint/proof.md` there.
The repository is released under the Apache License 2.0, read in its root
`LICENSE` at that commit on 2026-10-19, which prints no copyright line. The
formalization is held as
[evidence/assets/erdos_111_formalization.tar.gz](evidence/assets/erdos_111_formalization.tar.gz),
the repository's whole tree at that commit, made by
`git archive de72caf | gzip -n`. The repository's README credits the proof to
two models working in alternating steps, GPT-6 Astra in Codex and Claude Opus
5.5 in Claude Code, and the Lean to Claude Opus 5.5 in Claude Code.

```bibtex
@misc{PlasmaAI:Erdos111,
  author = {{Plasma AI}},
  title = {{Erdős Problem 111: bipartizing finite subgraphs of uncountably
            chromatic graphs}},
  howpublished = {Lean formalization with a prose blueprint,
                  \url{https://github.com/plasma-ai/erdos-111}},
  year = {2026}
}
```

The result is credited to Plasma AI; the repository's README says the proof
is Plasma AI's. Its `formalization.yaml` names Jacob Parish as the
formalization's author, Jacob Parish and Andrew Turner as its responsible
maintainers, and records that it was written with
Claude Code (model `claude-opus-5-5`) and parallel subagents.

**The results.** The
[[set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/main_theorem|main theorem]]:
for every $C\ge0$, a graph in which every finite subgraph on $m$ vertices can
be made bipartite by deleting at most $Cm$ edges has countable chromatic
number, at every vertex cardinality. Its
[[set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/corollary|corollary]]:
$h_G(n)/n\to\infty$ for every graph $G$ that is not countably colorable, in
particular for every graph of chromatic number $\aleph_1$, which answers the
second question of
[[../wiki/problems/set_theory/E0111/_index|Problem 111]]. The divergence is of
the whole sequence. The first, open-ended question is not addressed beyond it.

**The formalization.** Lean 4 at `v4.35.0-rc3` with Mathlib `v4.35.0-rc3`, and
no other dependency. `Challenge.lean` defines `bipartizationNumber`, the least
number of edges of a subgraph whose deletion leaves it bipartite (Mathlib's
`IsBipartite`); `h`, its supremum over the subgraphs on $n$ vertices; and
`chromaticCardinal`, the least cardinality of a color type. It states three
theorems with deliberate `sorry` bodies: `Erdos111.countably_colorable_of_linear`,
the main theorem for real $C$; `Erdos111.tendsto_of_not_countably_colorable`,
the corollary for every graph with no coloring by $\mathbb N$; and
`Erdos111.erdos_111`, the corollary for `chromaticCardinal G = ℵ₁`.
`Solution.lean` proves the three through the development `Erdos111/`
(19 files), and `comparator.json` permits only the axioms `propext`,
`Quot.sound` and `Classical.choice`. The blueprint proves the theorems in prose,
module by module, and records how the Lean route reorganizes the argument of the
[[../wiki/research/leads/linear_bipartization_countable_coloring/_index|countable-coloring lead]]:
closure over a set in place of elementary submodels, a chain that starts from
the empty set and has length the initial ordinal of $\#V$, limits of laws along
an ultrafilter with Kolmogorov extension for Boolean coordinates in place of
weak-star compactness, and a finite minimax lemma.

Attestation, recorded as the source's own statements and not as this corpus's
review: `formalization.yaml` gives the review status as self-assessed, a `sorry`
count of zero and the three standard axioms, and records that its Comparator
check ran on macOS without Comparator's sandbox. This corpus rebuilt the
formalization in its own sandbox, checked it with Comparator and replayed its
three theorems in the kernel
([[set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/evidence/verify/replay_receipt|the replay receipt]]),
and its
[[set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/evidence/verify/statement_fidelity/_index|statement-fidelity audit]]
passed, graded, on 2026-10-18.

Read status: claims checked for the three statements of `Challenge.lean`, read
clause by clause against the README's Theorem and Corollary and against
Problem 111's Statement; the blueprint and the Lean proofs were not read.

## Bears on

- [[../wiki/problems/set_theory/E0111/_index|Problem 111]]: the resolution of
  the second question,
  [[../wiki/problems/set_theory/E0111/claims/2026_10_19_plasma_ai|its claim page]],
  accepted on this corpus's replay of the formalization and the graded review
  of its statements. The first question is open-ended and not a part.

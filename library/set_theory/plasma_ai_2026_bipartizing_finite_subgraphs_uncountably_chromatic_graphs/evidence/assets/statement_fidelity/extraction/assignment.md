# Assignment: whole-statement fidelity audit of a Lean challenge file for Erdős Problem 111

You are an independent reviewer under a refutation charge. Your task is to find any defect in the fidelity of three Lean statements to the mathematical statements they claim to formalize. Your task is not to agree with them. The commissioner prepared this extraction and froze it on 2026-10-18. You did not write any of it, and you have no other context.

## Read set (read only these files, all in this folder)

- `assignment.md`: this file.
- `problem_statement.md`: the corpus's Statement of Erdős Problem 111, the erdosproblems.com wording. It is the target for `Erdos111.erdos_111`.
- `claim_statement.md`: the claim the formalization is offered for. Its first paragraph states the limit for graphs of chromatic number ℵ₁; its second states the countable-coloring theorem the proof goes through, the target for `Erdos111.countably_colorable_of_linear`.
- `challenge.lean`: the Lean file under audit. It defines `Erdos111.bipartizationNumber`, `Erdos111.h` and `Erdos111.chromaticCardinal`, and states `Erdos111.countably_colorable_of_linear`, `Erdos111.tendsto_of_not_countably_colorable` and `Erdos111.erdos_111`, each with a deliberate `sorry`. Its module doc comment states the claim in prose; that **Claim.** paragraph is the target for `Erdos111.tendsto_of_not_countably_colorable`.
- `mathlib_definitions.lean`: excerpts of the Mathlib definitions the statements reach (`SimpleGraph.Subgraph`, `Subgraph.coe`, `Subgraph.edgeSet`, `Subgraph.deleteEdges`, `Sym2.fromRel`, `Sym2.ToRel`, `SimpleGraph.Coloring`, `Colorable`, `IsBipartite`, `Set.encard`, `Set.ncard`, `Cardinal.aleph` and the notation `ℵ₁`), at the Mathlib version the formalization pins. Read them as supporting definitions.

Read no other file. Do not search the filesystem, run git, run Lean, use the web, or consult any other source. If you do see anything outside this read set, say what it was and how you saw it, in your report at the point it happened.

## What to decide

For each of the three theorems, decide whether the Lean statement is faithful to its target. Compare objects, quantifiers, hypotheses, conventions, constants, domains, exceptional cases, junk values and the conclusion. Unfold every definition it uses: `bipartizationNumber` (its `sInf`, `Set.ncard` on a possibly infinite set, `Subgraph.deleteEdges` and `.coe`, `IsBipartite`), `h` (its `sSup`, whether the set is nonempty and bounded above, and its value at `n = 0` and when `G` has fewer than `n` vertices), `chromaticCardinal` (its `sInf` over `Cardinal.{u}` and the universe of the color types), the `ℕ`-to-`ℝ` casts and the division by `n` at `n = 0`, `Tendsto … atTop atTop`, and `ℵ₁`.

1. **`erdos_111` against the second question of the Statement** ("Is it true that h_G(n)/n → ∞ for every graph G with chromatic number ℵ₁?"). Does `h` capture "the least h_G(n) such that any subgraph of G on n vertices can be made bipartite after deleting at most h_G(n) edges"? Does `chromaticCardinal G = ℵ₁` capture "chromatic number ℵ₁"? Is the conclusion neither stronger nor weaker than h_G(n)/n → ∞? Are graphs of every vertex cardinality covered, up to the universe the statement quantifies over?
2. **`tendsto_of_not_countably_colorable` against the module doc comment's Claim** that h_G(n)/n → ∞ for every graph that is not countably colorable, of any cardinality. Is `IsEmpty (G.Coloring ℕ)` exactly "not countably colorable"? Does this theorem imply `erdos_111`, given the definitions?
3. **`countably_colorable_of_linear` against the countable-coloring theorem** of `claim_statement.md`. The claim takes a finite C ≥ 0; the Lean statement takes any real C. Is the hypothesis, over subgraphs `H` with finitely many vertices and `bipartizationNumber H ≤ C · ncard H.verts`, the same as the claim's hypothesis on finite subgraphs F? Is `Nonempty (G.Coloring ℕ)` exactly "countable chromatic number"?
4. **Subgraphs.** The Statement says "any subgraph of G on n vertices". The Lean statement ranges over `G.Subgraph` (all subgraphs, not only induced ones) with `H.verts.Finite` and `ncard = n`. Say whether that is the intended reading and whether the induced reading would give the same `h`.
5. **Coverage.** Does `erdos_111` cover the second question whole? Confirm that the first, open-ended question ("What is the behaviour of h_G(n)?") is not covered.

## Report

Return your report as the text of your final reply; do not write any file. Use these sections:

- **Subject:** your role, as an independent fresh-context reviewer, with no names. List the files read, with their names in this folder, the freeze date 2026-10-18, and the exact scope.
- **Independence:** how you were separated from the authorship, what you read, and any exposure.
- **(a) Restatement:** each target and each Lean statement, in your own words.
- **(b) Clause-by-clause comparison:** a verdict for every clause and definition listed above.
- **(c) Checklist:** a verdict for each of these modes, applicable or not, saying which. A quantifier or "every" quietly narrowed (vertex cardinality, universe, finite versus arbitrary subgraphs). A limit replaced by a subsequence or a positive coefficient. Consequence sentences as claim surfaces (each "hence", "so" or "in particular"). Junk values and edge cases (`sInf ∅`, `sSup` of an unbounded or empty set, `ncard` of an infinite set, division by zero). Convention drift (bipartite as 2-colorable, chromatic number as a least cardinal).
- **(d) Strongest attack:** the strongest attempt you made to show unfaithfulness, and why it failed, or the defect with its exact witness.
- **Verdict:** for each theorem, either "faithful" or "not faithful (defect: …)", and a coverage statement (whole or partial, with what is missing). Write verdict words in full.

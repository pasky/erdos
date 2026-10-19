---
name: set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/evidence/verify/statement_fidelity/report
title: Fidelity audit of the Problem 111 challenge statements
desc: |
  Fresh-context refutation-charge audit, on 2026-10-18, of the three
  statements of the Problem 111 formalization's challenge file against the
  problem's Statement, the claim's countable-coloring theorem and the challenge's
  own Claim paragraph: all three faithful; the second question covered whole,
  the open-ended first question not formalized.
created: 2026-10-18T02:15:08Z
updated: 2026-10-19T00:30:14Z
---

***

**Subject.** I am an independent reviewer working from a fresh context under a refutation charge. My task is a whole-statement fidelity audit of three Lean statements against their prose targets. The extraction was frozen on 2026-10-18. Files read, all in the extraction folder: `assignment.md`, `problem_statement.md`, `claim_statement.md`, `challenge.lean`, `mathlib_definitions.lean`. The audit covers:

- `Erdos111.erdos_111` against the second question of the Statement.
- `Erdos111.tendsto_of_not_countably_colorable` against the **Claim.** paragraph of the module doc comment.
- `Erdos111.countably_colorable_of_linear` against the countable-coloring theorem in the second paragraph of `claim_statement.md`.
- The definitions those statements use: `bipartizationNumber`, `h`, `chromaticCardinal`, and the Mathlib excerpts.

The proofs are out of scope. Every theorem ends in `sorry`, as intended.

**Independence.** I did not write any part of the extraction and had no earlier context. I read only the five files listed. I ran no commands and did no search, git, Lean or web access. Exposure:

- The harness put two general instruction files into my context automatically before I started: the organization's and the repository's. They hold general repository and tooling conventions. They say nothing about Problem 111 or this formalization.
- The harness also added a repository status snapshot and an environment date of 2026-10-17. That date is one day earlier than the stated freeze date; I note it but it does not affect anything here.

None of this bears on the verdicts.

**(a) Restatement.**

- **The Statement's h_G(n) and second question.** For each n, h_G(n) is a bound such that every n-vertex subgraph of G can be made bipartite by deleting at most h_G(n) edges. The second question asks whether h_G(n)/n → ∞ for every graph G with chromatic number ℵ₁.
- **`erdos_111`.** For every type V in any universe u and every simple graph G on V whose least proper-coloring cardinal is ℵ₁: n ↦ (h G n : ℝ)/n tends to +∞. Here `h G n` is the largest, over subgraphs H of G with exactly n vertices, of the minimum number of H's edges whose deletion makes H 2-colorable.
- **The module-doc Claim.** Its first sentence (the C-linear bound forces countable chromatic number) is the target of theorem 3. Its "Hence" sentence says that for every graph that is not countably colorable, of any cardinality, h G n/n → ∞. Its "in particular" sentence extends this to every graph of chromatic number ℵ₁.
- **`tendsto_of_not_countably_colorable`.** For every G on V : Type u that has no proper coloring by ℕ, (h G n : ℝ)/n → +∞.
- **The countable-coloring theorem.** Fix a finite C ≥ 0. If every finite subgraph F of G can be made bipartite by deleting at most C·|V(F)| edges, then χ(G) ≤ ℵ₀, at every vertex cardinality.
- **`countably_colorable_of_linear`.** For every real C: if every subgraph H with finite vertex set has bipartizationNumber H ≤ C·|H.verts|, then G has a proper ℕ-coloring.

**(b) Clause-by-clause comparison.**

- **`bipartizationNumber`: faithful on finite H, which is the only case reached.** It is the `sInf` over k of sets D ⊆ H.edgeSet with D.ncard = k and (H.deleteEdges D).coe 2-colorable.
  - If H.verts is finite, then H.edgeSet is finite, because edge_vert puts every edge inside Sym2 of the vertex set. So every D is finite and `ncard` is exact.
  - The set is nonempty: D = H.edgeSet leaves an edgeless graph, which is bipartite. So the `sInf` is a true minimum and never the `sInf ∅ = 0` junk value.
  - `deleteEdges` removes exactly the pairs in D and keeps the vertex set.
  - `.coe` is the graph on H.verts.
  - `IsBipartite` is `Colorable 2`, the standard meaning of "made bipartite".
  - For infinite H, `ncard` would take the junk value 0 on an infinite D, which could give a junk 0. But no statement evaluates `bipartizationNumber` at a subgraph with infinite vertex set: both `h` and `hC` require `H.verts.Finite`.
- **`h`: faithful.** It is the `sSup` in ℕ of {bipartizationNumber H : H finite, ncard H.verts = n}.
  - The set is bounded above by n(n−1)/2, because bipartizationNumber H ≤ |H.edgeSet| via the witness D = edgeSet. So `sSup` is a true maximum and the unbounded-`sSup` junk value 0 never arises.
  - The set is empty only when |V| < n, giving `sSup ∅ = 0`. That case is irrelevant: a graph that is not countably colorable, and in particular one with χ = ℵ₁, has infinite V, since a finite V injects into ℕ.
  - At n = 0 the only subgraph is the empty one, so h = 0, and in ℝ we get 0/0 = 0. A single index does not affect `atTop`.
  - The maximum, over n-vertex subgraphs, of the minimum number of deletions is exactly the least admissible bound. Any admissible bound is ≥ h. So h/n → ∞ for the least bound implies it for every admissible bound, which makes "least" the correct and strongest reading.
- **`chromaticCardinal`: faithful.** It is the `sInf` in Cardinal.{u} of cardinals of types α : Type u that carry a proper coloring.
  - The set is nonempty (α = V with the identity coloring, which is proper because G is loopless), and cardinals are well ordered, so this is the least such cardinal.
  - Restricting α to universe u loses nothing. Any coloring factors through its image, which is a subset of the target of a map from V, so its cardinal is at most #V and is realized in Type u.
  - So `chromaticCardinal G = ℵ₁` is exactly χ(G) = ℵ₁.
  - `ℵ₁ = aleph 1` with aleph 0 = ω, so it is the first uncountable cardinal, in the matching universe.
- **Casts and `Tendsto … atTop atTop`: faithful.** The ℕ → ℝ cast is exact. `Tendsto f atTop atTop` means ∀K ∃N ∀n ≥ N, f n ≥ K. That is the full limit h/n → ∞ (equivalent to the claim's ∀K ∃N ∀n ≥ N, h > Kn), not a subsequence and not a limsup.
- **`IsEmpty (G.Coloring ℕ)`: faithful to "not countably colorable".** Every countable color set, finite ones included, injects into ℕ, and composing a coloring with an injection keeps it proper. So a ℕ-coloring exists iff G has a coloring with at most countably many colors.
- **`Nonempty (G.Coloring ℕ)`: faithful to "countable chromatic number"** (χ ≤ ℵ₀, finite included), for the same reason.
- **Hypothesis `hC`: equivalent to the claim's hypothesis.**
  - "Finite subgraph F" with |V(F)| maps to `H.verts.Finite` with `ncard`, which is exact.
  - If "finite subgraph" were read as finite edge set with possibly infinite vertex set, then C·|V(F)| is infinite and the hypothesis is vacuous there, so nothing changes.
  - Over all subgraphs versus only induced ones: equivalent, as shown under item 4 below.
  - C ∈ ℝ versus a finite C ≥ 0: equivalent. If C < 0 and V is nonempty, a one-vertex subgraph gives 0 ≤ C, which is false, so the hypothesis fails and the theorem is vacuous. If V is empty, the conclusion holds trivially. So the Lean statement is equivalent to its restriction to C ≥ 0, and every real C is finite.
  - The claim's "at every vertex cardinality" is covered by V : Type u with u universe-polymorphic.
- **Item 2: `tendsto_of_not_countably_colorable` implies `erdos_111`.** Suppose `chromaticCardinal G = ℵ₁` but a ℕ-coloring exists. Transfer it to ULift ℕ : Type u, whose cardinal is ℵ₀. Then chromaticCardinal ≤ ℵ₀ < ℵ₁, a contradiction. So hG of `erdos_111` gives hG of `tendsto_of_not_countably_colorable`, with identical conclusions.
- **Item 4, subgraphs: the all-subgraphs reading is the natural reading of "any subgraph of G on n vertices", and the induced reading gives the same h.**
  - Let H be a subgraph on vertex set S, and suppose deleting D from the induced subgraph G[S] makes it bipartite.
  - Then deleting D ∩ H.edgeSet from H leaves a spanning subgraph of a bipartite graph on the same vertices, which is bipartite. So b(H) ≤ b(G[S]).
  - Every induced subgraph is itself a subgraph. So the maximum over all n-vertex subgraphs equals the maximum over induced ones.
  - The same monotonicity makes `hC` over all subgraphs equivalent to `hC` over induced subgraphs.
- **Item 5, coverage.** `erdos_111` covers the second question whole, answered in the affirmative: every G of chromatic number ℵ₁, every vertex cardinality, every universe. The first question, "What is the behaviour of h_G(n)?", is open-ended and is not formalized. No theorem addresses it.

**(c) Checklist.**

- **Quantifier or "every" quietly narrowed: applicable, not triggered.**
  - Vertex cardinality and universe: V : Type u is arbitrary, and the universe restriction in `chromaticCardinal` is harmless, as shown above.
  - Finite versus arbitrary subgraphs: the finite restriction is what "on n vertices" and "finite subgraphs F" say. All-subgraphs versus induced gives the same values.
  - C over all reals widens the claim's C ≥ 0 only by vacuous cases.
- **Limit replaced by a subsequence or a positive coefficient: applicable, not triggered.** `Tendsto … atTop atTop` is the full limit to +∞. There is no limsup and no "h ≥ cn".
- **Consequence sentences as claim surfaces: applicable, each one checked.**
  - The doc comment's "Hence h G n/n → ∞ for every graph … not countably colorable" is stated separately as `tendsto_of_not_countably_colorable`, so it is a formal surface of its own and does not rest on the word "hence".
  - Mathematically, the countable-coloring theorem alone gives only unbounded h(n)/n along some n, which is the limsup. Getting the full limit needs the extra argument sketched in `claim_statement.md`: deleting countably many vertices keeps the graph uncountably chromatic, a type recurs, and its copies are packed. That argument also works for any non-countably-colorable G, not only for χ = ℵ₁.
  - So the "Hence" is a genuine further step, but it is formalized as its own theorem and is not smuggled in.
  - "In particular … ℵ₁" is `erdos_111`, which is implied as shown in (b).
  - "This answers … in the affirmative" is a prose gloss on `erdos_111`.
  - In `claim_statement.md`, "so h_G(n)/n → ∞" follows correctly from ∀K ∃N ∀n ≥ N, h > Kn. "Therefore has a positive answer" is `erdos_111`.
- **Junk values and edge cases: applicable, none reached.**
  - `sInf ∅` in `bipartizationNumber` cannot occur, because the set is nonempty.
  - `sInf` in `chromaticCardinal` is over a nonempty set.
  - `sSup` in `h` is bounded, and empty only when |V| < n, which is excluded under both hypotheses.
  - `ncard` of an infinite set is never reached, because every use carries `H.verts.Finite`.
  - Division by zero at n = 0 is a single index, irrelevant to `atTop`.
  - A negative C makes the theorem vacuous; that is harmless.
- **Convention drift: applicable, none.** "Bipartite" is `Colorable 2`, i.e. 2-colorable, which is standard, and the edgeless and empty graphs count as bipartite. The chromatic number is the least cardinal of a proper coloring set, and ℵ₁ is the first uncountable cardinal.

**(d) Strongest attack.** I tried three routes; none produces a defect.

1. **The `sSup` junk value in `h`.** In ℕ, `sSup` of an unbounded set is 0, and `sSup ∅ = 0`. Such a junk value would make h G n ≡ 0 on a tail, which would make `erdos_111` false for a trivial reason. It fails because the set is bounded by C(n,2), via D = edgeSet, and is nonempty whenever |V| ≥ n, and any G meeting either hypothesis has infinite V.
2. **The infinite-D `ncard` junk inside `bipartizationNumber`.** This could make the hypothesis `hC` hold too cheaply, since it would set bipartizationNumber to 0 for an infinite subgraph. It fails because `hC` only ranges over subgraphs with finite vertex set, where every D is finite.
3. **Letting C range over ℝ.** This could make `countably_colorable_of_linear` stronger than the claim. It fails because C < 0 is unsatisfiable on any nonempty V; one singleton subgraph is enough.

I also checked whether the universe restriction in `chromaticCardinal` could misidentify χ = ℵ₁. It cannot: colorings can always be reduced to their image, which lives in Type u.

**Verdict.**

- **`Erdos111.erdos_111`: faithful.** It covers the second question of the Statement whole, as an affirmative answer, for all graphs of chromatic number ℵ₁ at every vertex cardinality and universe. Coverage of the Statement is partial: the first, open-ended question ("What is the behaviour of h_G(n)?") is not covered.
- **`Erdos111.tendsto_of_not_countably_colorable`: faithful** to the module doc comment's "Hence" sentence, covered whole. Given the definitions, it implies `erdos_111`.
- **`Erdos111.countably_colorable_of_linear`: faithful** to the countable-coloring theorem of `claim_statement.md`, covered whole. Allowing every real C adds only vacuous instances, and the subgraph hypothesis is equivalent to the claim's hypothesis on finite subgraphs.

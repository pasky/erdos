---
name: set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/evidence/verify/statement_fidelity/grade
title: Grade of the Problem 111 fidelity audit
desc: |
  A distinct grader's check, on 2026-10-18, of the Problem 111 fidelity
  audit: PASS, every part of the contract present, each verdict re-derived,
  the exposure immaterial and the refutation charge met.
created: 2026-10-18T02:15:08Z
updated: 2026-10-19T00:30:14Z
---

***

- **Grader:** I am an independent grader working from a fresh context. I did not write the extraction and I did not write the report. Examination date: 2026-10-18. Files read, all relative to the grading folder: `grading_assignment.md`, `report.md`, `extraction/assignment.md`, `extraction/problem_statement.md`, `extraction/claim_statement.md`, `extraction/challenge.lean`, `extraction/mathlib_definitions.lean`. I ran no commands and did no search, git, Lean, build or web access. My own exposure matches the reviewer's. The agent environment automatically put into my context the organization's and the repository's general instruction files, a repository status snapshot and an environment date of 2026-10-17. None of that material concerns Problem 111 or this formalization, and none of it bears on this grade.

- **Contract:** every part is present.
  - Subject block: present. It gives the reviewer's role as an independent fresh-context reviewer under a refutation charge, names no people, lists all five files read, gives the freeze date 2026-10-18, and states the exact scope (three theorems with their targets, plus the definitions; proofs out of scope).
  - Independence section: present. It says what was read, that no commands were run, and what the exposure was: the two instruction files, the status snapshot, and the environment date with its one-day discrepancy from the freeze date.
  - (a) Restatement: present for all three targets and all three Lean statements.
  - (b) Clause-by-clause comparison: present. It covers every listed item: `bipartizationNumber` (its `sInf`, `ncard`, `deleteEdges`, `.coe`, `IsBipartite`), `h` (bounded, empty case, n = 0, fewer than n vertices), `chromaticCardinal` (the `sInf` and the universe of the color types), the casts and division at 0, `Tendsto … atTop atTop`, `ℵ₁`, `IsEmpty`/`Nonempty (G.Coloring ℕ)`, the hypothesis `hC`, all-subgraphs versus induced, the implication between theorems, and coverage.
  - (c) Checklist: present. All five modes are named, each marked applicable, with a finding for each.
  - (d) Strongest attack: present. It tries three routes (the `sSup` junk value, the infinite-D `ncard` junk value, C ranging over ℝ) plus the universe check, and says why each fails.
  - Verdicts: present, in full words, with a coverage statement for each theorem.
  - Minor note, not voiding: the Independence section names the instruction files by their file name, the repository by its local name, and the branch. These are not names of people, but under convention 09 a filed copy should describe them generically ("the organization's and the repository's general instruction files").

- **Soundness:** I checked each point against the extraction and found no error that changes a verdict.
  - **`bipartizationNumber`.**
    - If `H.verts` is finite, then `H.edgeSet` is finite. `edge_vert` together with symmetry puts both ends of every edge in `H.verts`, so every D ⊆ edgeSet is finite and `ncard D` is its true size.
    - The defining set is nonempty. Take D = edgeSet: since `ToRel D x y` holds exactly when s(x,y) ∈ D, every adjacency is removed. The vertex set is unchanged, and the edgeless `.coe` is 2-colorable by a constant coloring.
    - So the `sInf` over ℕ is a true minimum, never `sInf ∅ = 0` and never an infinite-set `ncard` value.
    - Every use of `bipartizationNumber` (in `h` and in `hC`) carries `H.verts.Finite`. Correct.
  - **The set defining `h`.**
    - It is bounded above by |H.edgeSet| ≤ n(n−1)/2, using the witness D = edgeSet.
    - It is nonempty exactly when V has at least n elements: an edgeless subgraph on any n-set is a witness.
    - At n = 0 the only finite vertex set of size 0 is ∅, which forces no edges. So h = 0, and 0/0 = 0 in ℝ, at a single index that `atTop` ignores.
    - Under either hypothesis V is infinite: a finite or countable V injects into ℕ, and an injection is a proper coloring because G is loopless. So the empty case never arises on a tail.
    - None of this can affect either limit theorem. Correct.
  - **`h` is the least bound of the Statement.**
    - The maximum, over n-vertex subgraphs, of the minimum number of deletions is the least admissible bound, and every admissible bound is at least as large. So the least-bound reading is the strongest, as the report says.
    - The report's monotonicity argument is right. If H has vertex set S, then H ≤ G[S] on the same vertex type. Deleting D ∩ H.edgeSet from H leaves a subgraph of G[S] − D on the same vertices, so any 2-coloring of G[S] − D colors it, and ncard(D ∩ H.edgeSet) ≤ ncard D.
    - So the all-subgraphs maximum equals the induced maximum, and `hC` over all subgraphs is equivalent to `hC` over induced subgraphs. Correct.
  - **`chromaticCardinal G = ℵ₁`.**
    - The defining set is nonempty: α = V with the identity coloring, which is proper because G is loopless. Cardinals are well ordered, so the `sInf` is a least element.
    - Restricting color types to Type u loses nothing. Any coloring factors through the quotient of V by its fibers, which lives in Type u, has cardinality at most #V, and is properly colored.
    - `ℵ₁ = aleph 1` and aleph 0 = preAleph ω = ℵ₀, so ℵ₁ is the first uncountable cardinal.
    - The report's image-based argument is slightly loose, since the image lives in α's universe, but the fact it states, "realized in Type u", is true. No error.
  - **`IsEmpty (G.Coloring ℕ)` is "not countably colorable", and the implication holds.**
    - A coloring with countably many colors (finitely many included) composed with an injection into ℕ stays proper, and ℕ is countable. So the two notions agree.
    - Implication: if χ = ℵ₁ and a ℕ-coloring existed, transferring it to `ULift ℕ : Type u` would give chromaticCardinal ≤ ℵ₀ < ℵ₁, a contradiction. The two theorems have identical conclusions, so `tendsto_of_not_countably_colorable` implies `erdos_111`. Correct.
  - **`Tendsto … atTop atTop`.** It means ∀K ∃N ∀n ≥ N, h/n ≥ K. That is the full limit to +∞, not a subsequence and not a limsup. It is equivalent to the claim's strict form ∀K ∃N ∀n ≥ N, h > Kn (apply it with K+1). Correct.
  - **C over all reals in `countably_colorable_of_linear`.**
    - If C < 0 and V is nonempty, a singleton subgraph has bipartizationNumber 0 (D = ∅ works), and 0 ≤ C is false. So the hypothesis fails and the instance is vacuous.
    - If V is empty, the conclusion holds through the empty coloring.
    - The hypothesis `H.verts.Finite` with `ncard` is exactly "finite subgraph F" with |V(F)|, and the all-versus-induced equivalence holds as above. The claim's "every vertex cardinality" is covered by the universe-polymorphic `V : Type u`. Correct.
  - **Coverage.** `erdos_111` covers the second question whole, as an affirmative answer. The first, open-ended question is not formalized. The other two theorems each cover their target whole. Correct.
  - Noted, not an error: the report's side remark on reading "finite subgraph" as finite-edge-set with infinitely many vertices treats C·|V(F)| as infinite. At C = 0 that product is ambiguous. It is offered only as an alternative reading and changes no verdict.

- **Exposure ruling:** immaterial.
  - The material was general repository and tooling conventions, a status snapshot and a date, and none of it mentions Problem 111 or this formalization.
  - Every mathematical fact in the report can be derived from the five extraction files.
  - The directions of attack (the `sSup`/`sInf`/`ncard` junk values, the universe of the color types, the range of C, all subgraphs versus induced) are exactly the ones `extraction/assignment.md` lists, so they did not follow the exposure.
  - Nothing in the report could have come only from that material. The only exposure-derived item, the environment date, is disclosed and plays no role in any finding.

- **Charge:** met. The reviewer tried three concrete routes to unfaithfulness, each of which would have been a real defect had it worked, and checked the universe restriction separately. It also flagged on its own that the module doc comment's "Hence" is a genuine further step, not a consequence of the countable-coloring theorem alone, before concluding that it is harmless because the step is stated as its own theorem. This is a refutation attempt, not agreement.

- **Grade:** PASS. All the required parts are present: the Subject block, the Independence section, (a) through (d), and full-word verdicts with coverage. Each verdict checks out against the extraction:
  - `bipartizationNumber` is a true minimum on every finite-vertex subgraph and never reaches a junk value.
  - The set defining `h` is bounded and is nonempty on the infinite vertex sets both hypotheses force. Its n = 0 value sits at a single index.
  - `h` is the least bound, with the all-subgraphs and induced readings agreeing.
  - `chromaticCardinal = ℵ₁` is χ = ℵ₁, with the universe restriction harmless.
  - `IsEmpty (G.Coloring ℕ)` is non-countable-colorability, and it implies `erdos_111`.
  - The limit is the full limit.
  - Letting C range over ℝ adds only vacuous instances.

  The only flaws are expository: generic naming in the Independence section, a slightly loose universe argument whose conclusion is right, and the C = 0 side remark. None changes a verdict. The exposure is immaterial and the refutation charge was met.

- **Accepted judgment:**
  - `Erdos111.erdos_111`: faithful. It covers the Statement's second question whole, as an affirmative answer for every graph of chromatic number ℵ₁, at every vertex cardinality in any universe. Coverage of the Statement is partial, because the first, open-ended question ("What is the behaviour of h_G(n)?") is not covered.
  - `Erdos111.tendsto_of_not_countably_colorable`: faithful to the "Hence" sentence of the module doc comment's **Claim.** paragraph, covered whole. Given the definitions, it implies `erdos_111`.
  - `Erdos111.countably_colorable_of_linear`: faithful to the countable-coloring theorem in the second paragraph of `claim_statement.md`, covered whole. Letting C range over all reals adds only vacuous instances, and the all-subgraphs finite-vertex hypothesis is equivalent to the claim's hypothesis on finite subgraphs.

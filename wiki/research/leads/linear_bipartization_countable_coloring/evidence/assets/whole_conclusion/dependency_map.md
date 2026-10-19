---
desc: Consumed proof interfaces and source boundaries examined for the arbitrary-cardinality coloring theorem and its E111 implication.
---

# Consumed dependency map

***

Examination date: 2026-10-17 UTC. The subject was frozen on 2026-10-17
at 06:43:02 UTC. Project mathematics is credited to Plasma AI.
[The subject manifest](subject/manifest.json) identifies the exact
mathematical extractions. The examination covers the arbitrary-cardinality
C-linear coloring theorem and its full E111 implication, not the unused
alternative routes or by-products in the shared mathematical pages.

The following is the consumed dependency list derived from the statement
and proof sites. The entries are parts of the argument examined together;
they are not assumed established because they have labels in the subject.
The independent support is [the retained derivation](derivations.md), at
the section numbers indicated.

## Dependency order and checked interfaces

The principal source root is
`wiki/research/leads/linear_bipartization_countable_coloring/`.

| Deduction | Exact source and consumed interface | Independent check |
| --- | --- | --- |
| Finite bipartization budget | `_index.md`, Target and conventions: edge deletion equals minimum monochromatic-edge count; vertex and edge deletion are monotone. | Section 1 proves the equivalence and inheritance, including selected-edge patterns. |
| Small elementary layers | `layered_rooted_measures.md`, Chains, layers, traces and patterns: a continuous chain of length cf(kappa), models of size less than kappa, covering V(G), with each model an element and subset of its successor. | Section 2 checks hull sizes, proper limits at singular cardinals, first-entry successors, and earlier-neighbor traces. |
| Replication | `_index.md`, Lemma F, and the generalized replication paragraph in `layered_rooted_measures.md`: finite diagrams can be copied inside a model, avoiding a finite set and a parameter Q disjoint from their original new vertices. | Section 3 checks all parameters and avoidance of Q=N_xi when copying inside the next model. |
| Arbitrary-product probability | `layered_rooted_measures.md`, Probability on arbitrary products: consistent finite laws, Radon representation, compact fixed-marginal spaces, and countably determined new signs. | Section 4 proves the cylinder-density and marginal interfaces and checks the classical representation/compactness hypotheses. |
| Initial rooted law | `rooted_cut_measures.md`, One measure for all abundant patterns, and `layered_rooted_measures.md`, Lemma 0: one law satisfies every rooted expected-minimum inequality J at N_0. | Section 5 checks replication with shared roots, removal of the root overhead, finite separation, and finite-intersection compactness. |
| Derived signs | `layered_rooted_measures.md`, Lemma D: an infinite trace has a countably determined sign with total mismatch probability at most C, even for an uncountable trace. | Section 6 proves attainment of the expected-minority supremum by a countable union and checks individual zero-probability terms outside it. |
| Fixed-marginal successor | `layered_rooted_measures.md`, Lemma S: retain the whole old law, prescribe the infinite-trace signs, and retain every future rooted inequality. | Section 7 independently computes the copied-pattern minimum, proves finite weighted feasibility, and turns any separating obstruction into a finite violation of old J. |
| Limit law and trace energy | `layered_rooted_measures.md`, Proposition L: consistent laws preserve J at limits and give finite expected energy on every infinite earlier trace. | Section 8 checks finite-root transfer at all limits, preservation of countable-coordinate identities, and the factor two between equality probabilities and Hilbert energy. |
| Hilbert partition | `_index.md`, Proposition C, only the construction of countably many classes with positive same-class energy. | Section 9 proves finite threshold supports, the sign labeling, and the lower bound without separability. The basis index is not a color label. |
| Actual coloring and cardinal induction | `layered_rooted_measures.md`, Lemma T and Proof of the theorem: finite earlier-neighbor coloring between layers combined with proper colors inside smaller layers. | Section 9 treats finite traces separately, covers every edge, and rules out a minimal-cardinality counterexample. |
| Countable deletion | `_index.md`, Step 1: chi(G)=aleph_1 persists after countable vertex deletion. | Section 10 uses disjoint countable palettes to check the contradiction. |
| Packing | `_index.md`, Step 2: infinitely many disjoint copies of a fixed finite witness give an all-large-n lower bound. | Section 10 checks repeated isomorphism type, exact-n padding, disjoint deletion costs, and the ratio inequality. |
| E111 composition and remainder | `_index.md`, Step 3, and the application in `layered_rooted_measures.md`: recurse through omega_1; alternatively use a maximal disjoint family to obtain a linear remainder from a failed limit. The supplied formulation is `wiki/problems/set_theory/E0111/_index.md`. | Section 10 checks both directions for the restricted CC lemma and the full eventual-all-n consequence, without a vertex-cardinality restriction. |

The order is acyclic. The measure construction assumes no infinite
countable coloring. The only induction use of countable colorability is
on strictly smaller layers. The arbitrary-cardinality theorem is
established before it is used to obtain the E111 consequence.

## Native premises and classical inputs

No native L-claim is consumed. This was reconciled against the unchanged
proof sites on 2026-10-17 UTC. No live ledger was read: there was no
consumed row to check, and none is supplied as a warrant. The local
lemmas above are examined as deductions within the whole argument.

The classical inputs are choice and ordinal recursion; elementary hulls
in a countable language and elementary chain unions; compactness of
products of finite spaces; Riesz representation and weak-star compactness
of Radon probability laws; uniqueness of probability laws on countable
products from finite cylinders; monotone convergence and Fatou's lemma;
finite-dimensional convex separation; and orthonormal bases with Bessel's
inequality. Their exact hypotheses and uses are stated in the report and
expanded in the derivation. No specialized literature theorem is needed
by this chain. External proofs of the classical inputs were not read or
claimed reconstructed.

## Boundaries that matter to composition

- The rooted proposition supplies expected **minimum extension costs**,
  not costs of its existing new-vertex coordinates. Lemma S proves the
  required coordinate relation for infinite traces in a new, compatible
  extension. The infinite-star witness in derivations Section 11 shows
  that the unproved stronger replacement would be false.
- The derived-sign claim is a sum of probabilities, not a simultaneous
  statement on one outcome for all vertices. Countable determining
  coordinate sets and finite collections of roots are used at the
  precise measure interfaces.
- The compactness constraint in Lemma S fixes a whole joint Radon law.
  A Borel derived-sign graph is not simply declared closed.
- Proposition C is used only for its Hilbert partition. Its separate
  finite-density compactness conclusion is not applied to trace-star
  energy. Lemma T supplies the actual coloring transfer needed here.
- Finite traces need no uniform energy bound; their earlier-neighbor
  sets are already finite. Within-layer edges use separate proper
  colors, justified by the smaller cardinality.
- The E111 reduction needs repeatable witnesses after every countable
  deletion. The theorem gives precisely that. One isolated finite
  obstruction would not give the required full limit.

## Material read but not consumed

The retained full bodies include Propositions A, B, D, E and U; the
partitioned-vector, finite-root, and transversal alternatives, including
Lemma G; the sparse-ladder and recursive-probe companions; the evidence
index; and historical mathematical extractions. They were read to
identify the real proof boundary. Their specialized source claims,
finite numerical values, sharpness statements, and alternative conjectures
are not independently certified by this examination.

The rooted companion's later formula (5) and its coloring consequence
are not premises of Lemma 0 or the layered proof. The optional finite
checker is likewise not a premise; it and its runtime modules were not
read as source or executed. No external source was followed through a
navigation link. The exact supplied E111 formulation, rather than a live
catalog or current-status survey, is the formulation tested.

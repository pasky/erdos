/-
Excerpts from Mathlib at its tag v4.35.0 (commit 56a005855ea17e0b0958f73ec801ae140b0a1679),
the version the formalization pins: the definitions that the statements of challenge.lean
reach outside Lean core. Mathlib is released under the Apache License 2.0;
Copyright (c) the Mathlib contributors. Each excerpt names its file and lines.
-/

-- Mathlib/Combinatorics/SimpleGraph/Subgraph.lean, lines 55–68

/-- A subgraph of a `SimpleGraph` is a subset of vertices along with a restriction of the adjacency
relation that is symmetric and is supported by the vertex subset.  They also form a bounded lattice.

Thinking of `V → V → Prop` as `Set (V × V)`, a set of darts (i.e., half-edges), then
`Subgraph.adj_sub` is that the darts of a subgraph are a subset of the darts of `G`. -/
@[ext]
structure Subgraph {V : Type u} (G : SimpleGraph V) where
  /-- Vertices of the subgraph -/
  verts : Set V
  /-- Edges of the subgraph -/
  Adj : V → V → Prop
  adj_sub : ∀ {v w : V}, Adj v w → G.Adj v w
  edge_vert : ∀ {v w : V}, Adj v w → v ∈ verts

-- Mathlib/Combinatorics/SimpleGraph/Subgraph.lean, lines 133–138
/-- Coercion from `G' : Subgraph G` to a `SimpleGraph G'.verts`. -/
@[simps]
protected def coe (G' : Subgraph G) : SimpleGraph G'.verts where
  Adj v w := G'.Adj v w
  symm := G'.symm.comap Subtype.val
  loopless.irrefl _ hadj := G.irrefl hadj.adj_sub

-- Mathlib/Combinatorics/SimpleGraph/Subgraph.lean, lines 248–249
/-- The edge set of `G'` consists of a subset of edges of `G`. -/
def edgeSet (G' : Subgraph G) : Set (Sym2 V) := Sym2.fromRel G'.symm

-- Mathlib/Combinatorics/SimpleGraph/Subgraph.lean, lines 1095–1104
/-- Given a subgraph `G'` and a set of vertex pairs, remove all of the corresponding edges
from its edge set, if present.

See also: `SimpleGraph.deleteEdges`. -/
def deleteEdges (G' : G.Subgraph) (s : Set (Sym2 V)) : G.Subgraph where
  verts := G'.verts
  Adj := G'.Adj \ Sym2.ToRel s
  adj_sub h' := G'.adj_sub h'.1
  edge_vert h' := G'.edge_vert h'.1
  symm.symm a b := by simp [G'.adj_comm, Sym2.eq_swap]

-- Mathlib/Combinatorics/SimpleGraph/Coloring/Vertex.lean, lines 68–72
variable {V : Type u} (G : SimpleGraph V) {n : ℕ}
/-- An `α`-coloring of a simple graph `G` is a homomorphism of `G` into the complete graph on `α`.
This is also known as a proper coloring.
-/
abbrev Coloring (α : Type v) := G →g completeGraph α

-- Mathlib/Combinatorics/SimpleGraph/Coloring/Vertex.lean, lines 159–161
variable (G) in
/-- Whether a graph can be colored by at most `n` colors. -/
def Colorable (n : ℕ) : Prop := Nonempty (G.Coloring (Fin n))

-- Mathlib/Combinatorics/SimpleGraph/Bipartite.lean, lines 287–288
/-- The predicate for a simple graph to be bipartite. -/
abbrev IsBipartite (G : SimpleGraph V) : Prop := G.Colorable 2

-- Mathlib/Data/Set/Card.lean, lines 68–68
noncomputable def encard (s : Set α) : ℕ∞ := ENat.card s

-- Mathlib/Data/Set/Card.lean, lines 638–639
/-- The cardinality of `s : Set α` . Has the junk value `0` if `s` is infinite -/
noncomputable def ncard (s : Set α) : ℕ := ENat.toNat s.encard

-- Mathlib/SetTheory/Cardinal/Aleph.lean, lines 400–408
def aleph : Ordinal ↪o Cardinal :=
  (OrderEmbedding.addLeft ω).trans preAleph

@[inherit_doc] scoped notation "ℵ_ " => aleph
recommended_spelling "aleph" for "ℵ_" in [aleph, «termℵ_»]

/-- `ℵ₁` is the first uncountable cardinal. -/
scoped notation "ℵ₁" => ℵ_ 1
recommended_spelling "aleph_one" for "ℵ₁" in [«termℵ₁»]

-- Mathlib/Data/Sym/Sym2.lean, lines 600–603
of elements that are related.
-/
def fromRel (sym : Std.Symm r) : Set (Sym2 α) :=
  Set.ofPred <| lift ⟨r, fun _ _ ↦ propext ⟨symm, symm⟩⟩

-- Mathlib/Data/Sym/Sym2.lean, lines 723–726
/-- The inverse to `Sym2.fromRel`. Given a set on `Sym2 α`, give a symmetric relation on `α`
(see `Sym2.toRel_symm`). -/
def ToRel (s : Set (Sym2 α)) (x y : α) : Prop :=
  s(x, y) ∈ s

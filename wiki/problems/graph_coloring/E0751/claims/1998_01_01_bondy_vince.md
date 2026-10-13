---
name: problems/graph_coloring/E0751/claims/1998_01_01_bondy_vince
title: Bondy and Vince's two close cycle lengths
desc: |
  Bondy and Vince prove that every graph other than $K_1$ and $K_2$ with at most
  two vertices of degree below three has two cycles whose lengths differ by one
  or two. So a $4$-chromatic graph, whatever its girth, has consecutive cycle
  lengths at most two apart.
authors:
- J. A. Bondy
- A. Vince
status: accepted
claim: disproved
scope: full
evidence:
- reviewed
- refereed
submitted: null
links:
- url: "https://doi.org/10.1002/(SICI)1097-0118(199801)27:1<11::AID-JGT3>3.0.CO;2-J"
  kind: paper
  date: 1998-01-01
- url: https://people.clas.ufl.edu/avince/files/Cycles.pdf
  kind: paper
- url: https://github.com/SpringSense-Innovation-Institute/ai-for-math-lean/tree/ae3ead960a494cf81b28541c477e50997cb03999/erdos-problems/erdos751
  kind: formalization
  date: 2026-01-27
- url: https://github.com/plby/lean-proofs/blob/cecc3fc4b7725db36692f0eca3c24712a481cfba/src/latest/ErdosProblems/Erdos751.lean
  kind: formalization
- url: https://github.com/Jayyhk/erdos-lean/blob/cd127968300ea9c594fe869c13e7ed3e2ded18bd/problems/751/Erdos751.lean
  kind: formalization
- url: https://www.erdosproblems.com/751
  kind: discussion
created: 2026-10-07T05:46:59Z
updated: 2026-10-07T19:40:10Z
---

***

**Claim.** Both questions of
[[problems/graph_coloring/E0751/_index|Problem 751]] are answered no. Theorem 1
of Bondy and Vince states that every simple graph other than $K_1$ and $K_2$
with at most two vertices of degree less than three has two cycles whose lengths
differ by one or two
([[../library/graph_coloring/bondy_1998_cycles_graph_lengths_differ_one_two/_index|card]]).
A graph $G$ with $\chi(G)=4$ contains a finite subgraph of minimum degree at
least three: by the de Bruijn–Erdős theorem $G$ has a finite subgraph that is
not $3$-colorable, that subgraph is not $2$-degenerate, since a $2$-degenerate
graph is $3$-colorable, so it contains a finite subgraph of minimum degree at
least three. Theorem 1 is a finite-graph theorem, proved by induction on the
number of vertices; applying it to that finite subgraph gives two cycles of $G$
whose lengths differ by at most two. So $\min(m_{i+1}-m_i)\le 2$ for every graph
of chromatic number four, and large girth does not change this. The paper poses
the minimum-degree form of the question, attributing it to Erdős and colleagues,
and does not mention chromatic number; the reduction from chromatic number four
to minimum degree three is the standard observation the site records, with the
finite subgraph supplied as above. The page is dated by the paper's journal
issue, January 1998; the day is not recorded.

**Acceptance.** Refereed: Bondy, J. A. and Vince, A., Cycles in a graph whose
lengths differ by one or two, J. Graph Theory 27 (1998), no. 1, 11–15. Reviewed:
the site's curator, Thomas Bloom, labeled the problem DISPROVED (LEAN) and
credits the result to Bondy and Vince, independently of its authors.

A Lean 4 development by the SpringSense Innovation Institute was posted on the
site's discussion thread on 2026-01-27 and is linked above at its commit. It
describes itself as following Bondy and Vince's approach. It proves
`erdos_751_strong`: every finite simple graph with chromatic number at least
four has two cycles whose lengths differ by exactly one or two. Its vertex type
is finite, so the Lean does not cover the infinite case, which the de
Bruijn–Erdős theorem reduces to the finite one. The post says that ChatGPT 5.2
Thinking was used for dialogue and GPT-5.2 Codex to complete the Lean
implementation. According to the post, the AI helped to understand the paper and
choose the formalization route, while the poster implemented the basic
definitions in Lean and fine-tuned the code. That development is third-party
Lean, not among the corpus's audited builds, so the page lists no `formalized`
evidence.

The same development is also posted in Boris Alexeev's lean-proofs collection.
Its header there names Bondy, Vince and ChatGPT 5.2 Thinking as informal authors
and links the SpringSense posting. A single-file copy is in the erdos-lean
catalog, which adds `erdos_751`, the negative answer to the first question for
finite graphs. The corpus built neither.

The [statement file of
formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/6fbb54f24ccc2e64dcfaffc28c58950e377110d2/FormalConjectures/ErdosProblems/751.lean)
states both parts with the answer false and leaves their proofs as `sorry`. Its
finite variant also ends in `sorry` and carries a `formal_proof` attribute
pointing at `Main.lean`, lines 40–69, of that development at the linked commit.
Its variant `erdos_751.variants.bondy_vince`, the theorem for a finite graph of
minimum degree at least three alone, ends in `sorry` with no `formal_proof`, so
the Lean does not settle that form.

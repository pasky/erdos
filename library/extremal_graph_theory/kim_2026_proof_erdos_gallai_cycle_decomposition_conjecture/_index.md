---
name: extremal_graph_theory/kim_2026_proof_erdos_gallai_cycle_decomposition_conjecture
title: "Kim: A proof of the Erdős–Gallai cycle decomposition conjecture"
desc: |
  An October 2026 arXiv preprint of Jaehoon Kim proving that every graph on n
  vertices decomposes into O(n) cycles and edges, by a single procedure that
  reduces the problem to light graphs; unrefereed, with a declared extensive
  use of ChatGPT and Claude.
license: CC-BY-NC-SA-4.0
created: 2026-10-14T00:20:00Z
updated: 2026-10-14T00:21:45Z
---

# Kim: A proof of the Erdős–Gallai cycle decomposition conjecture

[[extremal_graph_theory/_index|..]]

[[extremal_graph_theory/kim_2026_proof_erdos_gallai_cycle_decomposition_conjecture/theorem_1_1|theorem_1_1]]: The preprint's main theorem: the edges of every graph on n vertices
decompose into O(n) cycles and single edges; the deduction from Theorems
1.3 and 1.4 followed here; unrefereed.

[[extremal_graph_theory/kim_2026_proof_erdos_gallai_cycle_decomposition_conjecture/theorem_1_3|theorem_1_3]]: The preprint's new ingredient: a light graph of large minimum degree has a
set S inducing minimum degree at least |S|^(1/1000) with at least |S|/12
vertices having at most two neighbors outside S; statement only checked.

[[extremal_graph_theory/kim_2026_proof_erdos_gallai_cycle_decomposition_conjecture/theorem_1_4|theorem_1_4]]: The preprint's extension of Conlon, Fox and Sudakov's linear-minimum-degree
theorem: for every eps > 0, a graph on n vertices with minimum degree at
least n^eps decomposes into at most C_eps n cycles and edges; statement only
checked.

***

Jaehoon Kim, *A proof of the Erdős–Gallai cycle decomposition conjecture*,
arXiv:2610.07840 [math.CO], v1 of 6 October 2026 (32 pages) and v2 of 9
October 2026 (22 pages). A preprint: no journal reference and no refereed
version were found. Kim, of KAIST, is its only author.

**Edition read.** The v2 text, <https://arxiv.org/abs/2610.07840v2>, read in
its TeX source with the page locators of its PDF; v1 is
<https://arxiv.org/abs/2610.07840v1>. The arXiv record of v2
(https://arxiv.org/abs/2610.07840v2, read 2026-10-14) names the Creative
Commons Attribution-NonCommercial-ShareAlike 4.0 license.

**Versions.** Version 2 simplifies version 1, by its "Note added" (p. 21):
heavy cycles are defined by degrees instead of vertex weights, which removes
logarithmic factors from Sections 3--5, and in Section 6 a deterministic
routing lemma replaces a random coloring with $\Theta(\log^3n)$ colors. Version
1 numbers the two ingredients as Theorems 1.4 and 1.5, states the Eulerian
form as Corollary 1.2 and counts $52kn$ cycles and edges where version 2 counts
$14kn$. The result pages use the numbering of version 2.

**Read status.** Claims checked for
[[extremal_graph_theory/kim_2026_proof_erdos_gallai_cycle_decomposition_conjecture/theorem_1_1|Theorem 1.1]],
with its deduction from Theorems 1.3 and 1.4 (Section 2.1, pp. 3--4)
followed; claims checked for the statements of
[[extremal_graph_theory/kim_2026_proof_erdos_gallai_cycle_decomposition_conjecture/theorem_1_3|Theorem 1.3]]
and
[[extremal_graph_theory/kim_2026_proof_erdos_gallai_cycle_decomposition_conjecture/theorem_1_4|Theorem 1.4]],
whose proofs (Sections 3--6) were read only through the paper's outline
(Sections 2.2--2.3) and were not checked. Nothing here is independently
reviewed.

## Contents

- Introduction (pp. 1--2): the conjecture as posed, its Eulerian form (every
  Eulerian graph on $n$ vertices decomposes into $O(n)$ cycles, Hajós's
  conjecture up to a constant factor), the earlier bounds $O(n\log n)$,
  Conlon, Fox and Sudakov's $O(n\log\log n)$ and Bucić and Montgomery's
  $O(n\log^\star n)$, and the lower bound $(3/2-o(1))n$.
- Definition 1.2 (p. 2): a cycle $C$ of $G$ is heavy if, for some real
  $b\ge1$, at least $b^{3/2}$ vertices of $C$ have degree at most $b$ in $G$;
  $G$ is light if it has no heavy cycle.
- Theorem 1.1 (p. 1), the main theorem, deduced in Section 2.1 from Theorem
  1.3 (p. 2), which finds near-closed subgraphs of polynomial minimum degree in
  light graphs and is the paper's new ingredient, and Theorem 1.4 (p. 2),
  which decomposes graphs of polynomial minimum degree into linearly many
  cycles and edges.
- Sections 3--5: counting cycles through vertices of small degree, and the
  proof of Theorem 1.3, which uses no expanders. Section 6: the proof of
  Theorem 1.4 from Bucić and Montgomery's robust sublinear expanders and
  Conlon, Fox and Sudakov's decomposition of sparse graphs, quoted as Theorems
  6.2 and 6.3 (p. 15).
- Section 7: the constant is large and not optimized; the optimal constant,
  Hajós's conjecture and Gallai's path conjecture remain open.
- "Note added" (p. 21): OpenAI announced an independent proof after version 1
  was submitted and before it appeared; the paper contrasts that proof's
  induction on the number of vertices through quotient graphs with its own two
  statements joined by a short procedure.
- "Use of AI tools" (p. 21): the author states extensive use of ChatGPT
  (OpenAI) and Claude (Anthropic) in developing the arguments and preparing the
  text and figures, and that the author verified all results and takes full
  responsibility for the content.

## Compiled scope

Theorem 1.1 and its deduction at claims-checked depth; the statements of the
two ingredients at claims-checked depth, their proofs not checked. The claim
the paper makes on the problem is recorded, with its standing, on
[[../wiki/problems/extremal_graph_theory/E0184/claims/2026_10_06_kim|its claim page]].

**Bears on.** [[../wiki/problems/extremal_graph_theory/E0184/_index|#184]]:
Theorem 1.1 is the problem's statement, $f(n)=O(n)$, a claimed third proof
after the OpenAI release's theorem and Coffey's formalized proof.

No file of this source is held: no license on record permits its redistribution,
and the card cites the edition it names above.

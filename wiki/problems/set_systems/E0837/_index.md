---
name: problems/set_systems/E0837
title: Problem 837
desc: |
  Asks for the set $A_3$ of $\alpha$ such that $3$-uniform hypergraphs of
  limiting density above $\alpha$ must contain growing subgraphs of density
  above some fixed $\beta>\alpha$, while limiting density at least $\alpha$ need
  not.
tags:
- Graph theory
- Hypergraphs
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 837

[[problems/set_systems/_index|..]]

***

**Statement.** Let $k\geq 2$ and $A_k\subseteq [0,1]$ be the set of $\alpha$
such that there exists some $\beta(\alpha)>\alpha$ with the property that, if
$G_1,G_2,\ldots$ is a sequence of $k$-uniform hypergraphs with

$$
\liminf \frac{e(G_n)}{\binom{\lvert G_n\rvert}{k}} >\alpha
$$

then there exist subgraphs $H_n\subseteq G_n$ such that $\lvert H_n\rvert \to
\infty$ and

$$
\liminf \frac{e(H_n)}{\binom{\lvert H_n\rvert}{k}} >\beta,
$$

and further that this property does not necessarily hold if $>\alpha$ is
replaced by $\geq \alpha$.

What is $A_3$?

**Statement (modified).** Let $k\geq 2$ and $A_k\subseteq [0,1]$ be the set
of $\alpha$ such that there exists some $\beta(\alpha)>\alpha$ with the
property that, if $G_1,G_2,\ldots$ is a sequence of $k$-uniform hypergraphs
with $\lvert G_n\rvert\to\infty$ and

$$
\liminf \frac{e(G_n)}{\binom{\lvert G_n\rvert}{k}} >\alpha
$$

then there exist subgraphs $H_n\subseteq G_n$ such that $\lvert H_n\rvert
\to\infty$ and

$$
\liminf \frac{e(H_n)}{\binom{\lvert H_n\rvert}{k}} >\beta,
$$

and further that this property does not necessarily hold if $>\alpha$ is
replaced by $\geq\alpha$.

What is $A_3$?

**Notes.** The growing-host condition is explicit in Erdős's original
Section 6, printed p. 157, as recorded with its definition on the
[[../library/graph_coloring/erdos_1979_problems_results_graph_theory_combinatorial_analysis/conjecture_p158|source page]].
Without it, repeating a fixed complete three-uniform graph defeats the
first implication for every $\alpha<1$: the density is one but no
subgraphs grow. That degeneration does not answer the intended problem.
The modification restores only host growth, retaining the two density
clauses and the displayed range for $\alpha$. With no upper restriction
on $\beta$, the endpoint $\alpha=1$ satisfies them vacuously in the
first clause, while growing complete graphs witness failure of the
equality version. Requiring $\beta\le1$ instead would exclude that
endpoint; no such extra restriction is imposed here.

**Status.** Open.

**Source.** [erdosproblems.com/837](https://www.erdosproblems.com/837), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #837,
https://www.erdosproblems.com/837.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/83397bad317ac2cf180ffd418f791b8613d1a78f/FormalConjectures/ErdosProblems/837.lean),
added on 2026-10-07. The file states `erdos_837` as research open, with the
set $A_3$ left as an `answer(sorry)` and no `formal_proof` pointer, so no claim
follows from it.

## Current assessment

For $0\le\alpha<1$, the first clause with growing hosts is the jump
property in
[[../library/set_systems/komorech_2025_non_jumping_densities_3_uniform_hypergraphs/proposition_1_4|Proposition 1.4's local-density form]].
If its constant is $c>0$, take $\beta=\alpha+c/2$ and let the
guaranteed subgraph order increase slowly enough to meet each finite-size
threshold along the sequence. Conversely, failure of the local property
at $c=\beta-\alpha$ gives some $\varepsilon>0$ and fixed order $m$
with arbitrarily large hosts of density at least $\alpha+\varepsilon$
whose $m$-vertex subgraphs all have density below $\beta$. Averaging
over $m$-subsets gives the same upper bound for every larger subgraph,
contradicting the sequence clause.

The additional failure-at-equality requirement remains a separate clause;
classifying jumps alone does not identify $A_3$. The source definition,
local-density statement and this translation are the scope of the account.
The original page's host-growth condition was also read in the print.
No independent proof review or complete current literature survey is
claimed, and no classification of the modified question follows here.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/graph_coloring/erdos_1979_problems_results_graph_theory_combinatorial_analysis/_index|erdos_1979_problems_results_graph_theory_combinatorial_analysis]]
- [[../library/graph_coloring/erdos_1979_problems_results_graph_theory_combinatorial_analysis/conjecture_p158|erdos_1979_problems_results_graph_theory_combinatorial_analysis / conjecture_p158]]
- [[../library/set_systems/komorech_2025_non_jumping_densities_3_uniform_hypergraphs/_index|komorech_2025_non_jumping_densities_3_uniform_hypergraphs]]
- [[../library/set_systems/komorech_2025_non_jumping_densities_3_uniform_hypergraphs/proposition_1_4|komorech_2025_non_jumping_densities_3_uniform_hypergraphs / proposition_1_4]]
- [[../library/set_systems/komorech_2025_non_jumping_densities_3_uniform_hypergraphs/theorem_1_5|komorech_2025_non_jumping_densities_3_uniform_hypergraphs / theorem_1_5]]
- [[../library/set_systems/komorech_2025_non_jumping_densities_3_uniform_hypergraphs/theorem_1_6|komorech_2025_non_jumping_densities_3_uniform_hypergraphs / theorem_1_6]]
- [[../library/set_systems/komorech_2025_non_jumping_densities_3_uniform_hypergraphs/theorem_4_8|komorech_2025_non_jumping_densities_3_uniform_hypergraphs / theorem_4_8]]
- [[../library/set_systems/liu_2026_number_4_9_is_non_jump/_index|liu_2026_number_4_9_is_non_jump]]

<!-- END problem library links -->

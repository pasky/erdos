---
name: problems/set_theory/E0111
title: Problem 111
desc: |
  Asks how many edge deletions make every $n$-vertex subgraph of a graph $G$
  bipartite, and whether this number grows faster than $n$ when $G$ has
  chromatic number $\aleph_1$.
tags:
- Graph theory
- Chromatic number
- Set theory
status: solved
claim: proved
created: 2026-09-04T09:17:27Z
updated: 2026-10-19T06:23:35Z
---

# Problem 111

[[problems/set_theory/_index|..]]

[[problems/set_theory/E0111/claims/_index|claims/]]: The 1 claim page of Problem 111, one per claimant's result; the problem's standing derives from them.

***

**Statement.** If $G$ is a graph let $h_G(n)$ be defined such that any subgraph
of $G$ on $n$ vertices can be made bipartite after deleting at most $h_G(n)$
edges.

What is the behaviour of $h_G(n)$? Is it true that $h_G(n)/n\to \infty$ for
every graph $G$ with chromatic number $\aleph_1$?

**Status.** Solved: an accepted full claim answers the limit question, and
the open-ended first question does not block the standing. Bloom's catalog
labeled the problem open. Plasma AI's
[[problems/set_theory/E0111/claims/2026_10_19_plasma_ai|full claim]] answers the
limit question yes; it is accepted on this corpus's rebuild, Comparator check
and kernel replay of its Lean formalization and a graded review of its
statements, and Current assessment gives its review.

**Source.** [erdosproblems.com/111](https://www.erdosproblems.com/111), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #111,
https://www.erdosproblems.com/111.

**References.**

- [EHS82] Erdős, P. and Hajnal, A. and Szemerédi, E., On almost bipartite large
  chromatic graphs. Theory and practice of combinatorics (1982), 117-123.
- [Er81] Erdős, P., On the combinatorial problems which I would most like to see
  solved. Combinatorica (1981), 25-42.

**Formalization.** Plasma AI's Lean development
([plasma-ai/erdos-111](https://github.com/plasma-ai/erdos-111), at commit
de72caf, linked) states the second question as `Erdos111.erdos_111`, for every
graph of chromatic number $\aleph_1$, and proves it, together with the
countable-coloring theorem and the limit for every graph that is not countably
colorable; [[problems/set_theory/E0111/claims/2026_10_19_plasma_ai|its claim page]]
records it. This corpus rebuilt it at that commit, checked it with Comparator
and replayed its three theorems in the kernel, as
[[../library/set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/evidence/verify/replay_receipt|the replay receipt]] records.
No formal-conjectures statement of the problem was merged on 2026-10-18.

## Current assessment

The source results below give a positive linear lower bound and examples
with a superlinear upper bound; those bounds alone do not decide the
requested divergence. The separate project examination described below
covers a proof of the full divergence statement. This account is not a
current literature survey or an independent review of the cited source
proofs. Here $h_G(n)$ denotes the least bound in the statement.

If $\chi(G)=\aleph_1$, deleting countably many vertices leaves an
uncountably chromatic graph: a countable coloring of the remainder could
otherwise be extended using countably many fresh colors. Recursion of length
$\omega_1$ therefore produces disjoint finite odd cycles. At each stage
only countably many vertices have been removed, and the remaining graph is
not bipartite. Some fixed odd length $\ell$ occurs uncountably often.
Taking $\lfloor n/\ell\rfloor$ such cycles and padding to $n$ vertices
shows

$$
h_G(n)\ge\lfloor n/\ell\rfloor.
$$

Each cycle needs an edge deletion independently of the others. This gives a
fixed positive coefficient, not a coefficient tending to infinity.
[[../library/graph_coloring/erdos_1982_almost_bipartite_large_chromatic_graphs/theorem_3|Erdős–Hajnal–Szemerédi Theorem 3]]
gives graphs of arbitrarily large chromatic number with
$h_G(n)\le2n^{3/2}$. Its $n^{1+\varepsilon}$ conclusion allows an
$r$-coloring, with $r$ depending on $\varepsilon$; it is not a two-color
bound. Neither conclusion fills the gap in the question.

An [Erdős Problem a Day report](https://www.erdosproblemaday.com/report/111)
dated 2026-07-26 claims that the ordered two-shift graph has
$h_G(n)=\Theta(n^{3/2})$, using a finite five-cycle obstruction for the
lower bound and Erdős–Hajnal–Szemerédi's upper bound. It also reports an
exact finite calculation $\beta(S_{12})=40$, where $\beta$ is the least
number of edge deletions needed for bipartiteness, and $S_t$ has vertices
$(i,j)$ with $0\le i<j<t$ and edges $(i,j)(j,k)$ for $i<j<k$.
Its separate reduction equates the universal limit question with the
assertion that every graph of chromatic number $\aleph_1$ has finite subgraphs
of arbitrarily large edge-bipartization density. That assertion is left
unproved. The report was read on 2026-10-16; its arguments have no
independent review here and its computation was not replayed. The
particular shift-graph result is not a full solution or a premise here.

The remarks on erdosproblems.com (accessed 2026-10-16) add that in [Er81]
Erdős conjectured the $n^{3/2}$ bound can be improved to
$\ll n^{1+\varepsilon}$ for every $\varepsilon>0$.
[[research/leads/linear_bipartization_countable_coloring/_index|The countable-coloring lead]]
records an independently reviewed auxiliary argument, accepted by a
[[research/leads/linear_bipartization_countable_coloring/evidence/verify/analytic_conclusions/grade|separate grade]],
that the construction in Lambie-Hanson's ZFC proof of
[[../library/graph_coloring/lambiehanson_2020_growth_rate_chromatic_numbers_finite_subgraphs/theorem_a|Theorem A]]
gives, for every nondecreasing unbounded $g:\mathbb N\to\mathbb N$, a graph of chromatic number
$\aleph_1$ with $h_G(n)\le(n-1)g(n)$ for all $n\ge1$, confirming that
upper-bound conjecture and showing that no common divergence rate can hold
if the limit question has a positive answer. This is a ZFC graph of size
$2^{\aleph_1}$; the size-$\aleph_1$ version assumes $\diamondsuit$. The
same lead reduces the question to an equivalent countable-coloring lemma for
graphs with $h_G(n)\le Cn$, and shows that such linear budgets do not bound the
chromatic number by any finite number; that latter assertion remains
author-recorded. The review does not cover the repaired nonnegative-budget
consequence or the partitioned vector route.

Plasma AI's
[[research/leads/linear_bipartization_countable_coloring/layered_rooted_measures|layered-measure proof]]
establishes that every set-sized graph with a finite hereditary linear
edge-bipartization budget is countably colorable. The independent
[[research/leads/linear_bipartization_countable_coloring/evidence/verify/whole_conclusion/review|whole-conclusion review]]
and separate
[[research/leads/linear_bipartization_countable_coloring/evidence/verify/whole_conclusion/grade|PASS grade]]
of 2026-10-17 accept **refutation-failed** first for that theorem at every
vertex cardinality, then for its full consequence
$h_G(n)/n\to\infty$ whenever $\chi(G)=\aleph_1$. This means every
sufficiently large order for each threshold, not just a subsequence.
The
[[research/leads/linear_bipartization_countable_coloring/evidence/verify/whole_conclusion/_index|exact verification record]]
retains the subject, independent derivations, exposure rulings and classical
source boundaries. The claim is accepted on its Lean formalization: this corpus
rebuilt it, Comparator accepted it, and the kernel replayed its three theorems
from an empty environment
([[../library/set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/evidence/verify/replay_receipt|the replay receipt]]), and the
[[../library/set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/evidence/verify/statement_fidelity/_index|graded review of the formalization's statements]]
found them faithful, covering the second question whole. The formalization
follows the reorganized route of its blueprint, not the reviewed text line by
line, and it lies outside this repository's Lean closure, so it confers no tier.
The problem is solved; the open-ended first question does not block the
standing, and what is known about it is recorded above.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/graph_coloring/adamczewski_2026_erdos74/_index|adamczewski_2026_erdos74]]
- [[../library/graph_coloring/erdos_1979_problems_results_graph_theory_combinatorial_analysis/_index|erdos_1979_problems_results_graph_theory_combinatorial_analysis]]
- [[../library/graph_coloring/erdos_1979_problems_results_graph_theory_combinatorial_analysis/question_p154|erdos_1979_problems_results_graph_theory_combinatorial_analysis / question_p154]]
- [[../library/graph_coloring/erdos_1982_almost_bipartite_large_chromatic_graphs/_index|erdos_1982_almost_bipartite_large_chromatic_graphs]]
- [[../library/graph_coloring/erdos_1982_almost_bipartite_large_chromatic_graphs/lemma_2_1|erdos_1982_almost_bipartite_large_chromatic_graphs / lemma_2_1]]
- [[../library/graph_coloring/erdos_1982_almost_bipartite_large_chromatic_graphs/remark_p121|erdos_1982_almost_bipartite_large_chromatic_graphs / remark_p121]]
- [[../library/graph_coloring/erdos_1982_almost_bipartite_large_chromatic_graphs/theorem_3|erdos_1982_almost_bipartite_large_chromatic_graphs / theorem_3]]
- [[../library/set_systems/erdos_1981_combinatorial_problems_which_i_would_most/_index|erdos_1981_combinatorial_problems_which_i_would_most]]
- [[../library/set_theory/erdos_1987_problems_finite_infinite_graphs/_index|erdos_1987_problems_finite_infinite_graphs]]
- [[../library/set_theory/erdos_1987_problems_finite_infinite_graphs/problem_7|erdos_1987_problems_finite_infinite_graphs / problem_7]]
- [[../library/set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/_index|plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs]]
- [[../library/set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/corollary|plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs / corollary]]
- [[../library/set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/evidence/verify/statement_fidelity/_index|plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs / evidence/verify/statement_fidelity/_index]]
- [[../library/set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/main_theorem|plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs / main_theorem]]

<!-- END problem library links -->

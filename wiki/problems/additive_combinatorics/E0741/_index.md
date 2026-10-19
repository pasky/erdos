---
name: problems/additive_combinatorics/E0741
title: Problem 741
desc: |
  Asks whether every $A\subseteq\mathbb{N}$ with $A+A$ of positive upper density
  splits into two parts whose sumsets both have positive upper density, and
  whether some basis of order $2$ has no split in which both self-sumsets have
  bounded gaps.
tags:
- Additive combinatorics
status: solved
claim: proved
parts: [splitting, basis]
created: 2026-09-04T09:17:27Z
updated: 2026-10-14T07:12:04Z
---

# Problem 741

[[problems/additive_combinatorics/_index|..]]

[[problems/additive_combinatorics/E0741/claims/_index|claims/]]: The 3 claim pages of Problem 741, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $A\subseteq \mathbb{N}$ be such that $A+A$ has positive
(upper) density. Can one always decompose $A=A_1\sqcup A_2$ such that $A_1+A_1$
and $A_2+A_2$ both have positive (upper) density?

Is there a basis $A$ of order $2$ such that if $A=A_1\sqcup A_2$ then $A_1+A_1$
and $A_2+A_2$ cannot both have bounded gaps?

**Formulation.** Erdős [Er94b] asks the first question with positive
density. The erdosproblems.com wording, positive (upper) density, reads this as
positive upper density, which its commentary calls the reading most likely
to capture the question, and the page's standing targets that reading. If
positive density means that the density exists and is positive, the first
question has the answer no (the counterexample on the
[[problems/additive_combinatorics/E0741/claims/2026_03_31_deepmind|DeepMind claim page]]);
the formal-conjectures file under Formalization lists the lower-density
reading as an open variant (`erdos_741.variants.lower`).

**Status.** Proved. Bloom's catalog labeled the problem SOLVED (LEAN), and the
suffix is an erdosproblems.com label explained under Formalization. Both
questions are answered yes. The first is answered under the upper-density
reading of the Formulation. The second is answered by an explicit basis of order
$2$ that no bipartition splits into two self-sumsets with bounded gaps. There
are three claim pages. The first is
[[problems/additive_combinatorics/E0741/claims/2026_03_31_deepmind|Google DeepMind's three Lean proofs]],
found by its AlphaProof Nexus system, which the thread calls a DeepMind prover
agent, and posted on the erdosproblems.com thread by Moritz Firsching. It is a
full claim, accepted on the erdosproblems.com curator's credit and on the
refereed publication of the paper that proves both answers, [TKS26]. The second
is the
[[problems/additive_combinatorics/E0741/claims/2026_03_31_alexeev_putterman_sawhney_sellke_valiant|Alexeev–Putterman–Sawhney–Sellke–Valiant basis]]
from arXiv:2603.29961, which its authors attribute to an internal OpenAI model.
It is a partial claim, for the second question only, accepted on the
erdosproblems.com curator's credit. The third is a
[[problems/additive_combinatorics/E0741/claims/2026_04_24_chojecki|note of April 2026]]
that reproves all three statements (claimed). [TKS26] is the only refereed
publication of either answer.

**Source.** [erdosproblems.com/741](https://www.erdosproblems.com/741), accessed
2026-10-07 (page last edited 2 May 2026; six thread posts between 2026-03-31
and 2026-04-24); its proof-claim tab was empty. Cite as: T. F. Bloom, Erdős
Problem #741, https://www.erdosproblems.com/741.

**References.**

- [APSSV26] B. Alexeev, M. Putterman, M. Sawhney, M. Sellke, and G. Valiant,
  Short proofs in combinatorics and number theory. arXiv:2603.29961 (2026),
  v1 of 2026-03-31; Theorem 3.1 is the basis. Library home:
  [[../library/number_theory/alexeev_2026_short_proofs_combinatorics_number_theory/_index|alexeev_2026_short_proofs_combinatorics_number_theory]].
- [Er94b] Erdős, Paul, Some problems in number theory, combinatorics and
  combinatorial geometry. Math. Pannon. (1994), 261-269.
- [TKS26] G. Tsoukalas, A. Kovsharov, S. Shirobokov and eighteen further
  authors, Advancing mathematics research with AI-driven formal proof search.
  Science 394 (2026), 234--239; arXiv:2605.22763. Appendix B.4 proves both
  answers. Library home:
  [[../library/additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/_index|tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search]].

**Formalization.** erdosproblems.com's (LEAN) suffix is an erdosproblems.com
label. The statement is in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/9d259649abe0b02d7a25f7589b872db679b35e21/FormalConjectures/ErdosProblems/741.lean),
which at its commit of 2026-10-06 states the first question for upper density
(`parts.i`, tagged solved with answer true and a proof inside the repository at
its commit of 2026-04-16), for lower density (open) and for an existing limit
(`variants.exact_density`, solved with answer false), and the second question
with $A\cup\{0\}$ as the basis of order $2$ (`parts.ii`, solved with answer
true); the last two proofs are in Moritz Firsching's fork at its commit of
2026-03-31. The development `src/latest/ErdosProblems/Erdos741.lean` of Boris
Alexeev's lean-proofs repository (first added 2026-05-13) restates the three
theorems. DeepMind's results repository, at its commit of 2026-05-19, holds a
Lean file for each part; the file that [TKS26] gives for the upper-density
answer proves the exact-density answer instead, and for the second part [TKS26]
links a file of Problem 12. All are pinned on the
[[problems/additive_combinatorics/E0741/claims/2026_03_31_deepmind|DeepMind claim page]],
which records both discrepancies. The community database (teorth/erdosproblems,
file commit of 2026-09-28) lists `status` "solved (Lean)" and `formal_status`
Lean with a last update of 2025-08-31, and `formalized` "yes" with a last update
of 2026-01-06; these are the database's update fields and do not date the
changes of state. This corpus has built none of these developments, so no
`formalized` evidence is listed.

## Progress

Not yet compiled.

## Known Results

Not yet compiled.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/_index|tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search]]
- [[../library/additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_741_i|tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search / erdos_741_i]]
- [[../library/additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_741_ii|tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search / erdos_741_ii]]
- [[../library/number_theory/alexeev_2026_short_proofs_combinatorics_number_theory/_index|alexeev_2026_short_proofs_combinatorics_number_theory]]
- [[../library/number_theory/alexeev_2026_short_proofs_combinatorics_number_theory/theorem_3_1|alexeev_2026_short_proofs_combinatorics_number_theory / theorem_3_1]]

<!-- END problem library links -->

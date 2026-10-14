---
name: additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search
desc: |
  Google DeepMind's refereed AlphaProof Nexus paper: a Lean proof-search agent
  resolved nine Erdős problem statements of the 353 it attempted, and an
  appendix proves all nine informally. Cited; no file held.
license: CC-BY-NC-ND-4.0
created: 2026-10-13T10:06:04Z
updated: 2026-10-13T11:56:24Z
---

# additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search

[[additive_combinatorics/_index|..]]

[[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_125|erdos_125]]: With A and B the integers whose base-3 and base-4 digits are all 0 or 1, the
lower density of A+B is zero, by an inductive thinning along scales where a
power of 3 nearly equals a power of 4.

[[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_12_i|erdos_12_i]]: An infinite set in which no element divides the sum of two distinct larger
elements, whose count up to N over N^(1/2) has positive liminf; built from
progression-free blocks placed by the Chinese remainder theorem.

[[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_12_ii|erdos_12_ii]]: For every epsilon > 0 there is an infinite set in which no element divides
the sum of two distinct larger elements and which has at least
N^(1-epsilon) elements up to N for all large N; built from Behrend spheres.

[[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_138_difference|erdos_138_difference]]: The two-color van der Waerden numbers satisfy W(k+1) >= W(k) + k, so
W(k+1) - W(k) tends to infinity, by extending a coloring greedily; this is
Erdős's difference question of 1981, not the problem's main request.

[[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_152|erdos_152]]: Every Sidon set of size n has at least (n^2 - 100n - 16)/16 elements s of
A+A with s-1 and s+1 outside A+A, so the minimum f(n) tends to infinity;
proved by counting adjacent pairs in the sumset and the difference set.

[[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_26_variant|erdos_26_variant]]: A sequence with divergent reciprocal sum such that for every shift k >= 1
the multiples of A + k have upper density below 3/4, refuting Tenenbaum's
variant; the Lean file states a lower-density bound instead.

[[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_741_i|erdos_741_i]]: If A+A has positive upper density then A splits into two parts whose
sumsets both have positive upper density, by an alternating block
partition. The Lean file the paper links proves another statement.

[[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_741_ii|erdos_741_ii]]: A set A with A together with 0 a basis of order 2 such that in every
partition of A into two parts one part's sumset has unbounded gaps, built
from forbidden zones at scales 100^k, each with one surviving element.

[[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_846|erdos_846]]: An infinite plane set in which every n points contain n/2 with no three on a
line, but which is not a finite union of sets with no three on a line: one
point per edge of the infinite complete graph and the infinite Ramsey
theorem.

***

# additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search

# additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search

# additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search

George Tsoukalas, Anton Kovsharov, Sergey Shirobokov, Anja Surina, Moritz
Firsching, Gergely Bérczi, Francisco J. R. Ruiz, Arun Suggala, Adam Zsolt
Wagner, Eric Wieser, Lei Yu, Aja Huang, Miklós Z. Horváth, Andrew Ferraiuolo,
Henryk Michalewski, Codrut Grosu, Edward Lockhart, Thomas Hubert, Matej Balog,
Pushmeet Kohli, Swarat Chaudhuri, *Advancing mathematics research with
AI-driven formal proof search*. Science 394 (6820), 234--239, published
2026-10-08, DOI
[10.1126/science.aej2213](https://doi.org/10.1126/science.aej2213). It is the
refereed version of the preprint arXiv:2605.22763, *Advancing Mathematics
Research with AI-Driven Formal Proof Search*, by the same twenty-one authors
(cs.AI; v1 2026-05-21, v2 2026-06-08, 60 pages). The author order above is the
published one, as the DOI's Crossref record gives it; the preprint prints Edward
Lockhart before Codrut Grosu.

**Versions read.** The Science article and its supplementary text were not
read: the publisher's site answered with HTTP 403 on 13 October 2026. Checked
against the
published version are the Crossref record's title, author list, volume, issue,
pages 234--239, date 2026-10-08 and abstract; the abstract reports the
preprint's counts (nine of 353 open Erdős problems, 44 of 492 OEIS conjectures)
in reworded sentences. The account on this card follows arXiv v2, and every
locator is a PDF page of v2. Section 3 of v2 (p. 4) refers the reader to "Table
1 and supplementary text" for the nine Erdős results, and its Appendix B.4
(pp. 31--43) proves them; that the published supplement carries the same proofs
is this card's reading of that reference, not a comparison. The published
version's reference list, in the Crossref record, cites the repository's
release `v1.0.0-science-submission`, archived on Zenodo as
[10.5281/zenodo.21477349](https://doi.org/10.5281/zenodo.21477349).

**License.** The arXiv record of arXiv:2605.22763
(<https://arxiv.org/abs/2605.22763>) names the Creative Commons
Attribution-NonCommercial-NoDerivatives 4.0 license, the card's `license` term.
The v2 PDF prints "© 2026 Google DeepMind. All rights reserved" on p. 1. The
Crossref record carries no license, and the publisher's page could not be read.
No file of the paper is held: a NonCommercial-NoDerivatives term is not an open
license under the library's holding policy, and no record read gives the
published version an open license.

## The system and the evaluation

AlphaProof Nexus is a framework of agents that take a Lean file whose target
theorem has a `sorry` proof, with markers (`EVOLVE-BLOCK`, `EVOLVE-VALUE`)
delimiting what the agent may change, and return a proof without `sorry`
(Section 2, pp. 2--4). The basic agent (A) runs independent prover subagents,
loops of Gemini 3.1 Pro inference checked by the Lean compiler after every turn;
agent (B) adds AlphaProof as a proof tool; agent (C) adds an evolutionary
database of proof sketches that rater subagents rank by Elo score; and the
full-featured agent (D) combines both (Fig. 2, p. 5). Agent (D) produced the
Erdős results.

Agent (D) was run on every Erdős statement in the formal-conjectures repository
as of early February 2026, 353 statements, with a cap of 3000 episodes each,
and proved nine (Section 3, p. 4; Appendix B.2, p. 26). The paper says that
after each solve, experts on its team checked that the Lean statement captured
the original question. Table 1 (p. 7) lists the nine with a one-line summary
and the proof technique; it marks 138 and 26 as variants of the problem with
that number, and 26 as a generalization of Erdős's question that Erdős did not
pose. Section 3 (p. 6) reports that for 125 and 741(i) the agent first proved
the readings in which density means an existing limit, and that the formal
statements were then amended to lower density (125) and upper density (741(i)),
which the agent also resolved. In the comparison of Section 5 (pp. 8--10), run
after the search, the basic agent (A) also solved all nine; Codex (GPT-5.5)
solved seven, failing 152 and 125 within 12 hours; Claude Code (Opus 4.7),
AlphaProof alone and agent (A) on smaller Gemini models solved none.

Appendix B.4 (pp. 31--43) gives informal ("deformalized") proofs of the nine,
each with a link to its Lean file and, for all but 152, to the forum thread or
post that the paper calls its original communication of the result. The
results were first posted between February and April 2026, on the threads of
erdosproblems.com and in a fork of formal-conjectures, credited to "a DeepMind
prover agent"; the paper identifies that agent as AlphaProof Nexus.

## Lean and written proofs

The paper's Lean proofs and prose proofs are in the repository
[google-deepmind/alphaproof-nexus-results](https://github.com/google-deepmind/alphaproof-nexus-results/tree/42f344cfa9d57154f36e6b9bef1f71760a438c54),
cited here at its commit `42f344cfa9d57154f36e6b9bef1f71760a438c54` ("Results
for AlphaProof Nexus", authored 2026-05-13, committed 2026-05-19). That commit
added the nine Erdős Lean files under `APNOutputs/ErdosProblems/` and nine
prose PDFs under `NaturalLanguageProofs/ErdosProblems/`, whose texts follow
Appendix B.4. The Erdős files are unchanged at the repository's tag
`science-submission` (2026-07-21); the paper links them at `main`. The
repository's README licenses its software under Apache-2.0 and its other
materials under CC BY 4.0, and the Lean files carry a "Copyright 2025 Google
LLC" header. None of these files is held here.

Each Lean file imports formal-conjectures' utilities and proves a theorem
`target_theorem_0`, the formal-conjectures statement with its answer filled in,
with the agent's work between `EVOLVE-BLOCK` markers. The target statements and
the definitions they use were read in the files; nothing was built or audited
here, so no kernel credit is claimed. The repository's list of the statement
names attempted,
[`erdos_problems_attempted.txt`](https://github.com/google-deepmind/alphaproof-nexus-results/blob/science-submission/erdos_problems_attempted.txt),
is not in the commit cited above: a later commit, `a1912f87` of 2026-05-20,
added it, and it is cited here at the tag `science-submission`.

## Discrepancies in the paper and its repository

These are the source's own errors and inconsistencies. Each result page records
those that concern it.

1. **741(i): the Lean link proves a different statement.** B.4 (p. 37) gives
   `erdos_741.parts.i.lean` as the Lean proof of the upper-density "yes" that
   Table 1 and B.4 state. The file instead proves `answer(False)` for the
   reading in which `HasPosDensity` asks that the natural density exist and be
   positive (formal-conjectures' definition): the exact-density counterexample
   posted on 2026-03-31, under the name formal-conjectures then gave that
   statement, which upstream now calls `erdos_741.variants.exact_density`. The
   repository's prose PDF `erdos741i.pdf` is the upper-density proof, so the
   paper's prose and its Lean file disagree; the upper-density Lean proof is
   the formal-conjectures commit of 2026-04-16 linked from Problem 741's claim
   page.
2. **741(ii): the wrong file is linked.** B.4 (p. 38) links
   `erdos_12.parts.ii.lean` as the Lean proof of 741(ii); the repository's file
   for it is `erdos_741.parts.ii.lean`.
3. **12(i): Table 1 understates the theorem.** Table 1 summarizes 12(i) as
   $|A\cap[1,N]|/\sqrt N>\delta>0$ "infinitely often"; the theorem of B.4 and
   the Lean target give $\liminf_N|A\cap[1,N]|/\sqrt N>0$, which is stronger.
4. **26: prose and Lean state different bounds.** B.4 (p. 38) states the
   theorem with upper density below $3/4=1-\epsilon$ for $\epsilon=1/4$ and
   every shift $k\ge1$, and its union bound gives about $0.334$ (p. 40). The
   Lean target refutes Tenenbaum's variant through lower density: no shift's
   multiples reach lower density $1-\epsilon$ for $\epsilon=1/2$, the file
   bounding the lower density below $1/2$ for every $k\ge0$. Both refute the
   variant.
5. **12(ii): the printed theorem is stronger than its proof.** Theorem (ii)
   (p. 32) is printed with one set for every $\varepsilon>0$, but the
   construction depends on the exponent (p. 33), so the proof gives one set for
   each exponent, which is what the stated consequence needs and what the Lean
   target states.
6. **The attempted list omits five of the solved statements.**
   `erdos_problems_attempted.txt`, at the tag `science-submission`, has 353
   names, matching the count of B.2, but
   omits five of the nine statements proved: `erdos_12.parts.i`,
   `erdos_12.parts.ii`, `erdos_152`, `erdos_26.variants.tenenbaum` and
   `erdos_846`.
7. **The repository's files are not the files first posted.** For 12, 26, 125
   and 138 the lemma names of the repository's files differ from those of the
   fork files posted in February to April 2026 and linked from the claim pages
   (for 26, `seqA` against `elementary_thick_sequence_exists`; for 138,
   `W_diff_ge_k_all` against `W_diff_tendsto`), and B.4 does not always
   describe the repository's proof: for 12(i) the repository's set is cut out
   by congruences on intervals $[M_m,2M_m]$ with no progression-free digit set,
   and for 741(ii) it is built by a recursive extension step without the scales
   $100^k$, where B.4 describes the constructions of the first postings. B.4
   still calls the forum posts its original communication. The files and the
   prose were compared only at these points.

Read status: claims checked. Table 1 (p. 7) and the nine statements of Appendix
B.4 were read clause by clause on the v2 page images (pp. 31--42), with
Sections 2, 3 and 5 and Appendix B.2; the proofs were read for structure only,
and none is independently reviewed here. The Lean target statements were read
statically in the files at the commit cited.

**Bears on.** Each row states what the paper's text gives; standing is recorded
on the problem pages.

- [[../wiki/problems/integer_sequences/E0012/_index|#12]]:
  [[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_12_i|Erdős #12-(i)]]
  answers the first question yes, and
  [[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_12_ii|Erdős #12-(ii)]]
  the second no; the third question, on the reciprocal sum, is left open
  (p. 34).
- [[../wiki/problems/divisors/E0026/_index|#26]]:
  [[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_26_variant|Erdős #26, More General Variant]]
  refutes Tenenbaum's variant with a thick sequence, which also answers the
  question as erdosproblems.com states it no.
- [[../wiki/problems/diophantine_problems/E0125/_index|#125]]:
  [[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_125|Erdős #125]]
  proves that $A+B$ has lower density zero, a no; the upper density is left
  open.
- [[../wiki/problems/additive_combinatorics/E0138/_index|#138]]:
  [[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_138_difference|Erdős #138, Differences Variant]]
  proves $W(k+1)\ge W(k)+k$, the difference question of 1981, not the
  problem's request for bounds on $W(k)$.
- [[../wiki/problems/additive_bases/E0152/_index|#152]]:
  [[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_152|Erdős #152]]
  proves $f(n)\ge(n^2-100n-16)/16$, a yes with a quadratic bound.
- [[../wiki/problems/additive_combinatorics/E0741/_index|#741]]:
  [[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_741_i|Erdős #741-(i)]]
  answers the first question yes for upper density, and
  [[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_741_ii|Erdős #741-(ii)]]
  the second yes.
- [[../wiki/problems/discrete_geometry/E0846/_index|#846]]:
  [[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_846|Erdős #846]]
  gives a set with $\epsilon=1/2$ that is not a finite union of sets with no
  three points on a line, a no.

**Results.**

- [[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_12_i|Erdős #12-(i)]]
  (pp. 31--32): a set with property P whose counting function is at least a
  constant times $\sqrt N$ for all large $N$.
- [[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_12_ii|Erdős #12-(ii)]]
  (pp. 32--34): for each $\varepsilon>0$, a set with property P and at least
  $N^{1-\varepsilon}$ elements up to $N$ for all large $N$.
- [[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_125|Erdős #125]]
  (pp. 34--35): the lower density of $A+B$ is zero.
- [[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_138_difference|Erdős #138, Differences Variant]]
  (pp. 35--36): $W(k+1)\ge W(k)+k$.
- [[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_741_i|Erdős #741-(i)]]
  (pp. 36--37): the upper-density splitting theorem.
- [[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_741_ii|Erdős #741-(ii)]]
  (pp. 37--38): a basis of order 2 that no partition splits into two
  self-sumsets with bounded gaps.
- [[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_26_variant|Erdős #26, More General Variant]]
  (pp. 38--40): a thick sequence whose shifts all have multiples of upper
  density below $3/4$.
- [[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_846|Erdős #846]]
  (pp. 40--42): the edge-point construction from the infinite complete graph.
- [[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_152|Erdős #152]]
  (pp. 42--43): $16\,I(A+A)+100n+16\ge n^2$ for every Sidon set of size $n$.

No file of this source is held: no license on record permits its redistribution,
and the card cites the edition it names above.

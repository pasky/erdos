---
name: graph_coloring/openai_2026_correspondence_coloring_graphs_forbidden_clique
desc: |
  A 29-page manuscript of the OpenAI mathematics release claiming that for
  each fixed r at least 4, every K_r-free graph of sufficiently large maximum
  degree Delta has correspondence chromatic number O_r(Delta/log Delta), so
  also list and ordinary chromatic number, and the same for any fixed
  forbidden subgraph; it names no Erdős problem.
license: Apache-2.0
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

# graph_coloring/openai_2026_correspondence_coloring_graphs_forbidden_clique

[[graph_coloring/_index|..]]

[[graph_coloring/openai_2026_correspondence_coloring_graphs_forbidden_clique/corollary_1_2|corollary_1_2]]: The forbidden-subgraph form of the main claim, whose ordinary-coloring case
is Conjecture 3.1 of Alon, Krivelevich and Sudakov (1999); deduced from
Theorem 1.1 in three lines. Claims checked only.

[[graph_coloring/openai_2026_correspondence_coloring_graphs_forbidden_clique/theorem_1_1|theorem_1_1]]: The manuscript's main claim: for each fixed r at least 4, every K_r-free
graph of maximum degree Delta at least Delta_r has correspondence, hence
list and ordinary, chromatic number O_r(Delta/log Delta). Claims checked
only.

***

OpenAI, *Correspondence coloring graphs with a forbidden clique*, OpenAI Math
Release preprint, October 5, 2026. Released under the Apache License 2.0 at
<https://github.com/openai/math> (revision fd4aeeb2e), folder
`preprints/Correspondence-Coloring-Graphs-with-a-Forbidden-Clique-October-5-2026`;
the held PDF, `correspondence-coloring-forbidden-clique.pdf` in the release, is
retained as
[openai_2026_correspondence_coloring_graphs_forbidden_clique.pdf](openai_2026_correspondence_coloring_graphs_forbidden_clique.pdf),
and the release's TeX bundle in that folder is the TeX source cited on this
card. The license term was read in the release's root `LICENSE` file at that
revision on 2026-10-12.

```bibtex
@misc{OAI:Correspondence-Coloring-Graphs-with-a-Forbidden-Clique-October-5-2026,
  author = {{OpenAI}},
  title = {{Correspondence coloring graphs with a forbidden clique}},
  howpublished = {OpenAI Math Release preprint
                  \href{https://github.com/openai/math/blob/main/preprints/Correspondence-Coloring-Graphs-with-a-Forbidden-Clique-October-5-2026/correspondence-coloring-forbidden-clique.pdf}{OAI:Correspondence-Coloring-Graphs-with-a-Forbidden-Clique-October-5-2026}},
  year = {2026}
}
```

The held PDF has 29 pages with a text layer; its title page is dated October
5, 2026 and its metadata records a creation date of 5 October 2026 (at offset
UTC−7). The TeX source is `build/main.tex` (25 lines) with `build/preamble.tex`
(34 lines), six section files under `build/sections/` (`introduction.tex` 188
lines, `history.tex` 98, `adjustment.tex` 506, `triangles.tex` 524,
`rounds.tex` 562, `completion.tex` 68), the figure file
`build/figures/vertex-splitting.tex` (40 lines) and `build/references.tex`
(173 lines), 2,218 lines in all; `history.tex` is read in through
`introduction.tex`.

**Attestation.** The release README states that the repository's manuscripts
were "produced by an internal OpenAI model", that the collection "includes
results at different stages of verification", that "Not all have
accompanying Lean formalizations" and that "Some of the unformalized results
could have issues". Its account of the method says that "The vast majority
of results were obtained with the same procedure using an unreleased internal
OpenAI model"; the exceptions it names are work on a zero-free region for
the Riemann zeta function and on the Hodge conjecture for CM abelian
varieties, and neither describes this family. The manuscript's own README
carries only the title, the author line "OpenAI", the date October 5, 2026
and the citation block above, and adds no sentence about authorship or
assistance. The title page names OpenAI as
the sole author; the manuscript has no acknowledgment, funding note or
affiliation. These are the source's own statements, recorded as attestations
and not as this corpus's review. No refereed publication, arXiv version or
independent review of the manuscript is recorded here, and nothing on this
card is independently reviewed.

**Formalization.** The release lists no formalization of this manuscript. Its
Lean page for the family, `lean/docs/184.md`, carries the family's title
"Correspondence coloring with a fixed forbidden subgraph" but names only the
companion independence manuscript as its accompanying paper, and its scope
describes only that companion's bound: for every fixed $r\ge4$ a constant
$c_r>0$ such that every finite $K_r$-free simple graph on $n$ vertices with
average degree $d\ge2$ has an independent set of size at least
$c_rn\log d/d$. Its one comparator statement,
`lean/ComparatorChallenges/CliqueFreeLog.lean`, states that bound and nothing
about coloring. The release's catalog `lean/formalization.yaml` has a source
entry for the companion and lists its comparator
`OAI.CliqueFreeLog.logarithmic_independence_bound` under
`status.main_results`; it has no entry for this manuscript and no comparator
for any statement in it. All of this was read statically; nothing was built,
replayed or audited in this repository for this card.

**Companions.** The release's family *Correspondence coloring with a fixed
forbidden subgraph* holds two manuscripts: this one and *A logarithmic
independence bound for clique-free graphs* (September 25, 2026), filed at
[[extremal_graph_theory/openai_2026_logarithmic_independence_bound_clique_free_graphs/_index|the independence card]],
which claims the Ajtai--Erdős--Komlós--Szemerédi bound $\alpha\ge c_rn\log d/d$
for $K_r$-free graphs of average degree $d\ge2$, $r\ge4$, and whose Theorem 1.1
is recorded as accepted, with formalized evidence, on the claim page of
[[../wiki/problems/extremal_graph_theory/E0802/_index|Problem 802]]. This
manuscript cites the companion's Sections 2--5 as the source of the weighted
multipliers, neighborhood walks and vertex splitting that it adapts, and says it
proves every ingredient it needs itself, with the extra bound on how many
entries of one list an operation touches. The release holds no earlier dated
version of this manuscript at this revision. The companion's arguments were not
read for this card.

Read status: claims checked for Theorem 1.1 and Corollary 1.2, read clause by
clause in the release's TeX source (`build/sections/introduction.tex`, labels
`thm:main` at lines 25--34 and `cor:forbidden` at lines 44--52, with the
definitions at lines 3--21 and 41--42 and the conventions at lines 179--188),
together with the statements of Lemma 2.1 (`lem:adjustment`,
`build/sections/adjustment.tex` lines 78--96, with its definitions at lines
10--61), Lemmas 2.2--2.3, Corollary 2.4 and Proposition 2.5 (same file, lines
302--316, 368--386, 453--464 and 486--496), Lemmas 3.1--3.2
(`build/sections/triangles.tex` lines 102--119 and 184--191), and Proposition
4.1 and Lemmas 4.2--4.4 (`build/sections/rounds.tex` lines 85--102, 154--163,
251--262 and 371--382), on 2026-10-12, with the PDF page map taken from the
held PDF's text layer. The three-line proof of Corollary 1.2 was followed; all
other proofs were read for their structure only and no step was checked.
Nothing here is independently reviewed.

## Contents

The held PDF has 29 pages: the title, abstract and table of contents on
p. 1, Sections 1--5 on pp. 2--27 and the references on pp. 27--29.
Theorems, lemmas, corollaries and propositions share one counter per section,
and displays are numbered within sections. Logarithms are natural.

- Section 1, Introduction (`introduction.tex` and `history.tex`, pp. 2--5).
  Defines a correspondence assignment on a finite simple graph $G$: pairwise
  disjoint finite lists $L(v)$ and, for each edge $uv$, a matching
  $M_{uv}\subseteq L(u)\times L(v)$ of forbidden pairs, with no consistency
  required around cycles; a coloring picks $c(v)\in L(v)$ avoiding every
  forbidden pair, and $\chi_{\mathrm{DP}}(G)$, the correspondence (DP)
  chromatic number, is the least $k$ such that lists of size at least $k$
  always admit one. Notes
  $\chi\le\chi_{\mathrm{list}}\le\chi_{\mathrm{DP}}\le\Delta+1$. States
  [[graph_coloring/openai_2026_correspondence_coloring_graphs_forbidden_clique/theorem_1_1|Theorem 1.1]]
  ($\chi_{\mathrm{DP}}(G)\le\lceil C_r\Delta/\log\Delta\rceil$ for
  $K_r$-free $G$, $r\ge4$, $\Delta\ge\Delta_r$) and
  [[graph_coloring/openai_2026_correspondence_coloring_graphs_forbidden_clique/corollary_1_2|Corollary 1.2]]
  (the same for any fixed forbidden subgraph $F$, not necessarily induced),
  whose ordinary-coloring form it identifies with Conjecture 3.1 of Alon,
  Krivelevich and Sudakov (1999); it cites Bollobás (1978) for the order
  $\Delta/\log\Delta$ being best possible when $F$ contains a cycle. Section
  1.1 reviews list coloring (Vizing; Erdős, Rubin and Taylor), correspondence
  coloring (Dvořák and Postle), Kim's girth-five bound, Johansson's bounds
  $O(\Delta/\log\Delta)$ for triangle-free and
  $O_r(\Delta\log\log\Delta/\log\Delta)$ for $K_r$-free graphs (through
  Molloy and Reed, Chapter 13, and Bansal, Gupta and Guruganesh), Molloy
  (2019), Bernshteyn's extensions to correspondence coloring (2016; 2019,
  Theorems 1.3 and 1.5), which it names as the previous general bound
  $O_r(\Delta\log\log\Delta/\log\Delta)$ for $r\ge4$, Davies, Kang, Pirot
  and Sereni (Theorem 30), Przybyło (Theorem 10), the Alon--Krivelevich--Sudakov
  sparse-neighborhood theorem and Vu's list version, Anderson, Bernshteyn and
  Dhawan for bipartite and almost bipartite $F$, and Dhawan, Janzer and
  Methuku (Theorems 1.4--1.5) for $K_{t,t,t}$-free graphs, ordinary coloring
  only. It then places the structural part next to the
  Ajtai--Erdős--Komlós--Szemerédi independence problem, Shearer (1983,
  1995) and the companion manuscript. Section 1.2 outlines the proof: a
  graph $H$ on the list entries whose edges are the forbidden pairs (each
  entry has at most one neighbor in each list, and $H$ is $K_r$-free), a
  potential combining entropy, lost weight and incident edge mass $D_v$,
  local weight adjustments that offset the triangle term $t_i$ up to a
  constant multiple of the incident edge mass, and concentration by bounded
  participation. Section 1.3 fixes conventions,
  among them homomorphisms injective on directed edges.
- Section 2, Local weight adjustment with bounded participation
  (`adjustment.tex`, pp. 6--12). For a $K_r$-free graph $H$ with a vertex
  partition in which each vertex has at most one neighbor per part, and
  positive weights with neighborhood weights $s_i\le\Lambda$, defines the
  incident edge mass $d_i$, the triangle mass $t_i$, multiplier operations
  (supports in a ball of radius $R_0=\lceil4\log(8\Lambda)\rceil+10$ meeting
  each part in at most $P_0=\lceil\exp(40\log^2(8\Lambda))\rceil$ vertices,
  multipliers in $[0,U]$, $U=\exp(A\log^2(8\Lambda))$) and drop operations,
  each with a cost vector. Lemma 2.1 (local weight adjustment, p. 6): for
  $\Lambda\ge\Lambda_r$ there are such operations with rates $a_j\ge0$ such
  that $t_i+\sum_ja_jg^{(j)}_i\le Bd_i$ and the rates of operations whose
  support contains $i$ sum to at most $\Lambda^4$, for every vertex $i$, with
  $A$, $B$, $\Lambda_r$ depending only on $r$. Section 2.1 reduces the lemma
  by cone separation to a priced inequality, disposes of triangles at "bad"
  vertices through the drop operations, and groups the rest into dyadic
  price levels with rescaled weights. Section 2.2 proves Lemma 2.2 (sparse
  multipliers, p. 9: random multipliers of mean one, bounded by
  $D_r\epsilon^{-(r-2)}$, with expected edge mass at most $\epsilon s^2$, by
  the neighborhood recursion the text traces to Section 3 of
  Ajtai--Erdős--Komlós--Szemerédi), Lemma 2.3 (local cross estimate, p. 10),
  Corollary 2.4 (its transfer under maps injective on directed edges,
  p. 11), and states Proposition 2.5 (triangle bound, p. 12):
  $T_0\le O_r(M_x)$, the priced triangle mass against the priced edge mass.
- Section 3, Controlling triangles by splitting vertices (`triangles.tex`,
  pp. 12--19). Section 3.1 deletes low-price vertices and edges of small
  common-neighborhood weight at controlled cost and states Lemma 3.1
  (splitting a level graph, p. 13): neighborhood weights drop from $e^\ell$
  to $e^{\sqrt\ell}$ while a $1-C_2\log\ell/\sqrt\ell$ fraction of the
  triangle mass survives. Section 3.2 defines lazy walks inside
  neighborhoods and proves Lemma 3.2 (p. 14), a bound $O_r(\log\ell)$ on
  their weighted row entropy after $\lceil\ell\rceil$ lazy steps, using
  local sets whose admission threshold also bounds their size in each part.
  Section 3.3 proves Lemma 3.1 by an entropy-increment step, a shared rejection-sampling
  coupling (cited to Angel and Spinka, Theorem 2, and proved in the text)
  and a qualification rule on reverse transitions; Figure 1 (p. 18) shows
  the local splitting. Section 3.4 iterates $\ell\mapsto\sqrt\ell$ to prove
  Proposition 2.5 (pp. 18--19) and completes Lemma 2.1 (p. 19).
- Section 4, Coloring rounds with dependent entry weights (`rounds.tex`,
  pp. 19--26). Fixes $K=16(B+2)$, $\gamma=0.003$, $C=100K/\gamma$, lists cut
  to $k=\lceil C\Delta/\log\Delta\rceil$ entries, weights kept in
  $[\Delta^{-3},\Delta^{-0.99}]$ with $s_i\le\Lambda=20\log\Delta$, and a
  per-vertex potential $F_v$. States Proposition 4.1 (one coloring round,
  p. 20): while each list's total weight lies in $[K/2,2K]$, one round
  extends the coloring so that mass and potential grow by at most
  $\xi=\Delta^{-0.14}$ and normalized degrees shrink by the factor
  $1-\tau$, $\tau=\Delta^{-0.1}$, up to $\xi$. Lemma 4.2 (expected changes,
  p. 21) uses Lemma 2.1 to bound the expected potential increase by
  $\tau(B+1)D_v$; Lemma 4.3 (bounded input participation, p. 22) is a
  read-$k$ style tail bound in the setting of Gavinsky, Lovett, Saks and
  Srinivasan, derived in the text from Finner's generalized Hölder
  inequality and Hoeffding's exponential-moment bound; Lemma 4.4 (collision
  bound, p. 24) controls activations that collide along forbidden pairs.
  Section 4.4 applies the symmetric Lovász local lemma (proved in the text)
  and trims extreme weights; the proof of Proposition 4.1 is on pp. 25--26.
- Section 5, Iteration and completion (`completion.tex`, pp. 26--27). Runs
  $\lceil2\tau^{-1}\log\Delta\rceil$ rounds, after which remaining degrees
  are at most about $\Delta^{0.96}$ while each list keeps at least
  $(K/2)\Delta^{0.99}$ positive-weight entries, and finishes greedily; this
  closes the proof of Theorem 1.1 with $C_r=C$ (p. 27).
- References (pp. 27--29): 27 entries, numbered [1]--[27], among them the
  companion manuscript, Ajtai--Erdős--Komlós--Szemerédi (1981),
  Alon--Krivelevich--Sudakov (1999), Bernshteyn (2016, 2019),
  Molloy (2019), Shearer (1983, 1995), Angel--Spinka (arXiv:1903.00632),
  Davies--Kang--Pirot--Sereni (arXiv:2003.14361) and
  Dhawan--Janzer--Methuku (arXiv:2511.17191v2).

External inputs. The text proves its own adjustment lemma, sparse multipliers,
coupling, concentration lemma and local lemma; the citations to the companion
manuscript, Ajtai--Erdős--Komlós--Szemerédi (1981),
Benjamini--Duminil-Copin--Kozma--Yadin, Angel--Spinka,
Gavinsky--Lovett--Saks--Srinivasan, Finner and Hoeffding are given as
precedents for those arguments. Bollobás (1978) is cited only for the
sharpness remark. The manuscript flags nothing as numerical,
computer-assisted or conditional; $C_r$ and $\Delta_r$ are existence constants
depending only on $r$, not optimized. The release folder holds only the PDF,
the TeX build directory and the README; there is no `verification/` folder.

## Bears on

The manuscript names no Erdős problem. The row below is an input inferred on
this card; it is not stated in the manuscript, it is not verified here, and
the page's status rests on its own acceptance evidence.

- [[../wiki/problems/extremal_graph_theory/E0620/_index|Problem 620]]: input.
  The best lower bound for $f(n)$ that the page records a refereed paper
  printing, Dudek and Mubayi's $c\sqrt{n\log n/\log\log n}$, comes from the
  neighborhood argument written out on
  [[extremal_graph_theory/shearer_1995_independence_number_sparse_graphs/corollary_1|Shearer's Corollary 1 page]]
  (the same argument, with Brooks' theorem as its coloring step, proves
  [[extremal_graph_theory/bollobas_hind_1991_graphs_without_large_triangle_free_subgraphs/theorem_1|Bollobás and Hind's Theorem 1]]):
  a vertex of degree at least $D$ has a triangle-free neighborhood, and
  otherwise a $K_4$-free graph of maximum degree below $D$ has a large
  independent set. Theorem 1.1 at $r=4$, inside its range $r\ge4$ and with
  $C_4$, $\Delta_4$ absolute, would supply that second step without the
  $\log\log$ loss: since $\chi\le\chi_{\mathrm{DP}}$ and $x/\log x$ increases
  for $x\ge e$, maximum degree $\Delta$ with $\Delta_4\le\Delta<D$ gives
  $\chi\le\lceil C_4D/\log D\rceil$, and $\Delta<\Delta_4$ gives
  $\chi\le\Delta_4$, so the largest color class has at least $n/\chi$
  vertices and spans no triangle; with $D=\sqrt{n\log n}$ this gives
  $f(n)\ge c\sqrt{n\log n}$ for large $n$. That is the bound the page already
  derives in one line from Corollary 2 of Joret, Micek, Reed and Smid, and
  the lower half of the pending Morris--Sahasrabudhe--Verstraëte claim; this
  route avoids that theorem and the unexamined gap claim the page records
  through Problem 610, but it rests on an unrefereed manuscript. The
  companion's Theorem 1.1, recorded as accepted on Problem 802's claim page,
  gives the same bound by the same argument (maximum degree below $D$ forces
  average degree below $D$, and Turán's bound covers average degree below
  $2$). Problem 620's page does not record that route; the companion's card
  and its Proposition 6.1 page list Problem 620 for the same neighborhood
  argument without drawing this conclusion. Neither result touches
  the open upper bound $O(\sqrt{n\log n})$, the new part of the pending
  claim, or determines the order of $f(n)$. Unverified.

---
name: problems/graph_coloring/E0836
title: Problem 836
desc: |
  Asks whether an intersecting $r$-uniform hypergraph with chromatic number $3$
  must have $O(r^2)$ vertices, and whether two of its edges must meet in $\gg r$
  vertices. Plasma AI's internal whole-statement reviews with separate passing grades support the negative vertex-count answer and the positive linear-intersection answer under the exact-chromatic formulation; both claims await the sign-off of Jacob Parish at Plasma AI.
tags:
- Graph theory
- Hypergraphs
- Chromatic number
status: claimed
claim: answered
parts:
- vertex_count
- linear_intersection
created: 2026-09-04T09:17:27Z
updated: 2026-10-18T00:09:26Z
---

# Problem 836

[[problems/graph_coloring/_index|..]]

[[problems/graph_coloring/E0836/claims/_index|claims/]]: The 3 claim pages of Problem 836, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $r\geq 2$ and $G$ be a $r$-uniform hypergraph with chromatic
number $3$ (that is, there is a $3$-colouring of the vertices of $G$ such that
no edge is monochromatic).

Suppose any two edges of $G$ have a non-empty intersection. Must $G$ contain
$O(r^2)$ many vertices? Must there be two edges which meet in $\gg r$ many
vertices?

**Statement (modified).** Let $r\geq 2$ and $G$ be a $r$-uniform hypergraph
with chromatic number $3$ (that is, there is a $3$-colouring of the vertices of
$G$ such that no edge is monochromatic, but no such $2$-colouring), every vertex
lying in an edge.

Suppose any two edges of $G$ have a non-empty intersection. Must $G$ contain
$O(r^2)$ many vertices? Must there be two edges which meet in $\gg r$ many
vertices?

**Notes.** The erdosproblems.com parenthetical gloss says only that
$\chi(G)\leq3$; it does not express the preceding exact condition $\chi(G)=3$.
Taken literally, the gloss makes both questions false: arbitrarily large stars
are intersecting and $2$-colorable, and every two of their edges meet in exactly
one vertex. The erdosproblems.com commentary on Alon's counterexample states
that "its chromatic number is 3", and Erdős and Lovász [ErLo75, Theorem 8 p.
613, construction (b) p. 620] work with exact chromatic number $3$ and count
only points lying in edges. The modified Statement adds the missing "no such
$2$-colouring" and the convention that every vertex lies in an edge; if isolated
vertices were allowed, adjoining isolates would trivially falsify the first
question even under the exact chromatic-number hypothesis.

**Status.** Both questions of the modified Statement have claimed answers from arguments Plasma AI's internal review graded sound, no for the quadratic vertex bound and yes for the linear intersection bound; each claim awaits the sign-off of Jacob Parish at Plasma AI. Bloom's catalog labeled the problem
OPEN. erdosproblems.com credits a counterexample to the first question to Alon. The same construction
gives the lower bound of Erdős and Lovász's Theorem 8, recorded on
[[problems/graph_coloring/E0836/claims/1975_01_01_erdos_lovasz|their claim page]].

**Source.** [erdosproblems.com/836](https://www.erdosproblems.com/836), accessed
2026-09-07. Cite as: T. F. Bloom, Erdős Problem #836,
https://www.erdosproblems.com/836, accessed 2026-09-07.

**References.**

- [ErLo75] Erdős, P. and Lovász, L.,
  [[../library/graph_coloring/erdos_1975_problems_results_3_chromatic_hypergraphs_related/_index|Problems and results on $3$-chromatic hypergraphs and some related questions]].
  Infinite and Finite Sets (1975), 609–627.
- [BuGlSu20] Bucić, Matija; Glock, Stefan; and Sudakov, Benny,
  [[../library/graph_coloring/bucic_2020_intersection_spectrum_3_chromatic_intersecting_hypergraphs/_index|The intersection spectrum of $3$-chromatic intersecting hypergraphs]].
  Proc. London Math. Soc. **124** (2022), 680–690. The result locators refer
  to arXiv:2010.00495v2 (26 October 2020), not to the journal version.

**Formalization.** The
[formal-conjectures source](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/836.lean),
read on 14 October 2026, marks both parts research solved and links
Linmiao Xu's external Lean development. Its statements, registry report and
pending local verification are recorded on
[[problems/graph_coloring/E0836/claims/2026_10_14_xu|the formalization claim page]].

## Current assessment

**Status target and outcomes.** For exact $\chi(G)=3$, the
Erdős–Lovász construction below has exponentially many incident vertices and
disproves the $O(r^2)$ proposal; this is the lower bound of their Theorem 8
(printed p. 613), recorded on
[[problems/graph_coloring/E0836/claims/1975_01_01_erdos_lovasz|their claim page]].
The same source proves only the $r/\log r$ maximum-intersection lower bound
below, which it credits to Shelah and the authors jointly. For the requested
linear bound, a note that Liam Price posted in the erdosproblems.com thread on
27 April 2026, produced with GPT-5.5 Pro, claims the answer yes: for exact
$\chi(G)=3$ some two edges meet in at least $\lfloor r/2\rfloor$ vertices.
The recorded intersection argument has a reconstruction reviewed internally by Plasma AI with a separate passing grade; its partial claim stays claimed on [[problems/graph_coloring/E0836/claims/2026_04_27_price|its claim page]] until Jacob Parish at Plasma AI signs off.
An external Lean development by Linmiao Xu claims both answers and includes
the finite bound $r\le2t+1$ when all distinct edges meet in at most $t$
vertices. Its
[[problems/graph_coloring/E0836/claims/2026_10_14_xu|full claim]] retains
claimed standing pending local formal verification. The two prose claims cover both named parts but are pending, so the problem's derived status is claimed, with claim answered. Neither the external registry report nor the
formal-conjectures label supplies the acceptance warrant.

**Evidence and search window.** The source assessment covers the
erdosproblems.com problem, discussion and proof-claim pages, the
Erdős–Lovász paper, and the complete arXiv v2 of Bucić–Glock–Sudakov. The
latter work was published in 2022; its journal version is not held, and the
locators above follow the arXiv version. The external-status search of
14 October 2026 also inspected the formal-conjectures statement, Palomar
entry PALOMAR-2026-10-14-000004 version 1, and the header and exported
statements of its pinned `Solution.lean`. Palomar reports a complete
resolution, crediting the intersection argument to Price. The Overleaf
note remains an editable document with no fixed version.

**Proof and review coverage.** The §3(b) construction, its two complementary
edges per partition, vertex count, intersecting property, and chromatic number
match printed p. 620. The $r/\log r$ statement and the distinct spectrum
invariant are verified at statement level only. For the linear-intersection
bound, Plasma AI's
[[research/erdos_836/evidence/verify/linear_intersection/_index|independent report and separate grade]],
dated 14 October 2026, cover the whole recorded argument, its exact
formulations, and its finite and infinite conclusions. The infinite case
uses classical choice and an expressly permitted compactness
reconstruction. The grade passes independence with the disclosed limit
that no complete historical read or incoming-communication record was
supplied; no excluded exposure was identified. Fidelity to the editable
source document and the external Lean development are outside that review.

The first question has its own
[[research/erdos_836/evidence/verify/vertex_count/_index|independent whole-statement review and separate passing grade]],
also dated 14 October 2026. They cover the explicit finite construction for
every integer $r\ge2$, its exact vertex count and superquadratic growth,
and both supplied readings of the first question. The retained mathematical
extracts match the canonical proof. The grade passes independence with its
disclosed limits: an incomplete historical native read trace and two
unavailable private helper bodies. It supplies no external-source fidelity
or upper-bound certification.

**Formalization and source limits.** The external Lean development has not
been rebuilt and kernel-replayed by this repository. Its formal targets
are finite; the claim page separates the compactness implication for
arbitrary hypergraphs from that formal coverage. The two prose arguments, pending that sign-off, address the modified questions independently of that external formalization. Historical attribution, proceedings refereeing and the
source's upper bound receive no additional warrant from these reviews.
erdosproblems.com credits the vertex construction to Alon; Erdős and Lovász
published the matching construction in 1975 as their construction (b),
giving the lower bound of their Theorem 8.

## Progress

Erdős and Lovász call an intersecting hypergraph a clique. Their §3(b)
construction takes a set $S$ of size $2r-2$. For every unordered equal
partition $P=\{S_1,S_2\}$ of $S$, it introduces a point $x_P$. Its edges are
all $r$-subsets of $S$ and, for each $P$, both

$$
S_1\cup\{x_P\}
\quad\text{and}\quad
S_2\cup\{x_P\}.
$$

The source states that this $r$-uniform hypergraph is intersecting and has
chromatic number $3$. It has no isolated points and has

$$
|V|=2r-2+\frac12\binom{2r-2}{r-1}
  =\Theta\!\left(\frac{4^r}{\sqrt r}\right),
$$

which disproves the first question; it is the lower bound of their Theorem 8
(printed p. 613, proof p. 621), recorded on
[[problems/graph_coloring/E0836/claims/1975_01_01_erdos_lovasz|their claim page]].

For the second question, Erdős and Lovász record an observation they made
with Shelah (printed p. 613), proved by the method of their Theorem 7
(pp. 622–623): every $3$-chromatic intersecting $r$-uniform hypergraph has two
edges $E$ and $F$ such that

$$
|E\cap F|\geq\frac{r}{\log r}.
$$

Their printed p. 613 explicitly asks whether the lower bound can be
strengthened to $c r$ or even $r-c$. Printed p. 623 recapitulates the
$r/\log r$ bound in the proof and sharpness discussion. The printed statement
does not specify a logarithm base.

Bucić–Glock–Sudakov study the different invariant

$$
I(H)=\{|E\cap F|:E,F\in E(H),\ E\ne F\}.
$$

Their
[[../library/graph_coloring/bucic_2020_intersection_spectrum_3_chromatic_intersecting_hypergraphs/theorem_2|Theorem 2]]
gives

$$
|I(H)|=\Omega\!\left(\frac{\sqrt r}{\log r}\right).
$$

This counts distinct intersection sizes. It neither bounds the maximum member
of $I(H)$ linearly nor controls the number of vertices, so it settles neither
question on this page.

## Known Results

- [[problems/graph_coloring/E0836/claims/2026_04_27_price|Price's linear-intersection bound]]:
  the argument, graded sound by Plasma AI's internal review with its sign-off pending, gives distinct edges
  meeting in at least $\lfloor r/2\rfloor\ge r/3$ vertices whenever the
  intersecting $r$-uniform hypergraph is not $2$-colorable. It includes
  infinite hypergraphs in classical set theory with choice.
- [[../library/graph_coloring/erdos_1975_problems_results_3_chromatic_hypergraphs_related/_index|Erdős–Lovász §3(b)]]:
  an exact-$3$-chromatic intersecting construction with
  $2r-2+\frac12\binom{2r-2}{r-1}$ incident vertices, disproving the first
  question.
- [[../library/graph_coloring/erdos_1975_problems_results_3_chromatic_hypergraphs_related/_index|Erdős–Lovász, printed pp. 613 and 623]]:
  the lower bound $|E\cap F|\geq r/\log r$ for some pair of edges and the
  explicit linear-scale questions, with the logarithm base unspecified in the
  printed statement.
- [[../library/graph_coloring/bucic_2020_intersection_spectrum_3_chromatic_intersecting_hypergraphs/theorem_2|Bucić–Glock–Sudakov, Theorem 2]]:
  an adjacent lower bound on the number of distinct intersection sizes, not a
  resolution of the requested maximum-intersection bound.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/graph_coloring/bucic_2020_intersection_spectrum_3_chromatic_intersecting_hypergraphs/_index|bucic_2020_intersection_spectrum_3_chromatic_intersecting_hypergraphs]]
- [[../library/graph_coloring/bucic_2020_intersection_spectrum_3_chromatic_intersecting_hypergraphs/theorem_2|bucic_2020_intersection_spectrum_3_chromatic_intersecting_hypergraphs / theorem_2]]
- [[../library/graph_coloring/erdos_1975_problems_results_3_chromatic_hypergraphs_related/_index|erdos_1975_problems_results_3_chromatic_hypergraphs_related]]
- [[../library/set_systems/lovasz_1973_coverings_colorings_hypergraphs/_index|lovasz_1973_coverings_colorings_hypergraphs]]
- [[../library/set_systems/lovasz_1973_coverings_colorings_hypergraphs/theorem_8|lovasz_1973_coverings_colorings_hypergraphs / theorem_8]]

<!-- END problem library links -->

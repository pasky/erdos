---
name: problems/graph_coloring/E0108/claims/2026_09_15_kohlmeyer_kruer
title: Lean disproof at girth five and seven colors
desc: |
  Kohlmeyer and Kruer's kernel-checked Lean counterexample family, certified by
  Conjectures.io in September 2026, gives finite graphs of arbitrarily large
  chromatic number whose four-cycle-free subgraphs are $6$-colorable. Hence no
  $f(7,5)$ exists.
authors:
- Jensen Kohlmeyer
- Liam Kruer
status: accepted
claim: disproved
scope: full
evidence:
- formalized
submitted: 2026-09-27
links:
- url: https://conjectures.io/results/8c083793-9c3c-4960-8a23-869e54fcb584/solution
  kind: formalization
  date: 2026-09-15
- url: https://conjectures.io/results/8c083793-9c3c-4960-8a23-869e54fcb584/solution/download
  kind: formalization
  date: 2026-09-15
- url: https://jenwin.io/papers/erdos108-arc-graphs.pdf
  kind: preprint
  date: 2026-09-15
- url: https://conjectures.io/results/8c083793-9c3c-4960-8a23-869e54fcb584
  kind: record
  date: 2026-09-17
- url: https://conjectures.io/papers/erdos108.pdf
  kind: preprint
  date: 2026-09-17
- url: https://www.erdosproblems.com/forum/thread/108/proof-claims#proof-claim-364
  kind: discussion
  date: 2026-09-27
created: 2026-10-07T19:40:10Z
updated: 2026-10-08T03:54:20Z
---

***

**Claim.** The answer is no. For every $M$ there is a finite graph $G$ with
$\chi(G)>M$ such that every subgraph of $G$ containing no four-cycle is
$6$-colorable. The graphs are triangle-free, so their subgraphs of girth at
least $5$ are exactly their four-cycle-free subgraphs; hence no finite $f(7,5)$
exists, the universal question fails at $r=5$ and $k=7$, and the same family
refutes every $r\ge5$ with $k\ge7$. The $r=4$ case is Rödl's theorem
([[problems/graph_coloring/E0108/claims/1977_06_01_rodl|its claim page]]),
and the cases $r\ge5$ with $2\le k\le6$ are not decided by this result; a
later expository note sharpens the bound to $3$ (see the
[[problems/graph_coloring/E0108/claims/2026_09_30_nguyen_walczak|Nguyen–Walczak
page]]).

**Submission note.** Posted to erdosproblems.com as a proof claim by
conjectures.io (account TFBloom) on 27 September 2026, giving "Unknown" as the
AI used:

> This formalisation claims a disproof of the main claim for $r=5$ and $k=7$.
> Notes: This was posted on conjectures.io. I have not verified the proof yet,
> and do not claim that the formalisation is correct, nor have I looked into the
> proof at all. I am posting this here so that others are aware that this claim
> has been made, and we can discuss it here. This should also not be read as any
> kind of endorsement of the conjectures.io program - in my view it is using
> these problems, which it does not care about, for its own ends, without making
> any attempts to explain these proofs or engage with the mathematical
> community. It is also not transparent (e.g. of who is running these through
> the AI, how long for, and which AI).

**Construction.** Take an ordered multipartite random base graph $F$: parts
$V_0,\dots,V_{C-1}$ of rapidly decreasing sizes, each at least $C$ times
smaller than every earlier part, each vertex of $V_i$ choosing one uniformly
random neighbor in every later part. Orient each edge of $F$ from its smaller
to its larger endpoint and let $G$ be the arc graph: its vertices are the arcs,
two being adjacent when the head of one is the tail of the other. A proper
$m$-coloring of $G$ gives a proper $2^m$-coloring of $F$ (color a base vertex
by the set of arc colors leaving it), so $\chi(G)$ grows with $\chi(F)$, and
$\chi(F)$ is large because, with probability bounded away from zero, $F$ has
no heavy independent set. In a four-cycle-free subgraph $H$ of $G$, the arcs
with two or more forward neighbors in $H$ form a base subgraph of bounded
maximum degree, which the sparsity of every vertex set of $F$ makes
$4$-colorable; the remaining arcs form a $1$-degenerate graph, colored with two
further colors, so $\chi(H)\le6$.

**Claimant and postings.** The claimants are Jensen Kohlmeyer and Liam Kruer.
Their own manuscript, *A counterexample to Erdős problem 108 via arc graphs*
(dated 15 September 2026, second link, authors printed as Kohlmeyer and
Kruer), states the result as its Theorem 1.1 and Corollary 1.2, says that the
main theorem and the negation of the pinned formal-conjectures statement are
proved in Lean 4 with only the standard axioms, and discloses that the work
was developed with substantial assistance from OpenAI ChatGPT/Codex, in the
mathematical exploration, the estimates, the Lean proofs and the drafting,
with the authors responsible for the mathematical content. The proof was
published on Conjectures.io, a Bittensor subnet that publishes catalog
problems as pinned formal-conjectures statements and pays for kernel-checked
Lean proofs passing its review, under the handle JenW1N, which the record
credits as the solver. The platform's exposition of the proof (fourth link,
dated 17 September 2026) prints Kruer and Kohlmeyer as its authors while
saying that the public account credit is retained without inferring an
unconfirmed author list, and that it was prepared by the platform with Codex
assistance from the accepted Lean file and is neither formally verified nor an
author-approved publication; the Lean file's header states nothing about how
the proof was found. Nguyen and Walczak's note cites both manuscripts and
credits Kohlmeyer and Kruer with the negative solution.

**Formal statement.** The file's final theorem is the negation of the catalog
statement `Erdos108.erdos_108` of formal-conjectures (the
[formal-conjectures
file](https://github.com/google-deepmind/formal-conjectures/blob/6fbb54f24ccc2e64dcfaffc28c58950e377110d2/FormalConjectures/ErdosProblems/108.lean)
at its revision of 18 September 2026; the formal-conjectures commit the
Conjectures.io record names does not resolve in the public repository, and the
record page displays the same statement), whose Lean form matches the wording
clause by clause except that its $r$ ranges over the extended naturals, so
$r=\infty$ is admitted, where a girth of at least $\infty$ means acyclic and the
formal statement is trivially false, so the negation the target states is
trivial and proves nothing about the problem. The proof does not use that
defect: it instantiates $r=5$ and $k=7$, both inside the wording's range, and
its counterexamples are finite graphs lifted to every universe, so the
refutation holds under both a finite-graph and an all-graphs reading of "every
graph".

**Acceptance.** Formalized. This corpus's verification rebuilt the record's
solution file on the repository's pinned toolchain, `leanprover/lean4:v4.34.1`
with Mathlib at the revision `lean/lake-manifest.json` pins, after two lemma
renames that Mathlib made since the site's toolchain; the target's statement is
unchanged. The kernel replayed, from an empty environment, every declaration the
target `Bounty.target` depends on, Lean core, Mathlib and formal-conjectures
included, and accepted them all. The target's axioms are exactly `propext`,
`Classical.choice` and `Quot.sound`, and its type, and every definition its
statement reaches, are identical to the formal-conjectures statement of the
site's task. That target alone is trivial. The refutation is the lemma
`Bounty.counterexample_family`, from which the file derives the target and which
the kernel replayed with it: for every $M$ it gives a graph of chromatic number
at least $M$ all of whose subgraphs of girth at least $5$ are $6$-colorable. A
separate instance check confirmed that its witness graphs are finite, so the
lemma refutes the Statement at $r=5$ and $k=7$. Acceptance rests on the replay
of that lemma and this check.

Conjectures.io's certification is reported, not counted. Conjectures.io records
the proof as verified on 15 September 2026. Its Lean kernel accepted the file
with `propext`, `Quot.sound` and `Classical.choice` as the only axioms, after a
static scan found no imports, axiom declarations, `sorry`, `native_decide` or
unsafe options. The site's second kernel was not run, so the verdict rests on
one kernel implementation. Conjectures.io records its review as approved on 16
September 2026, on two independent agent assessments covering formal semantics
and prior-source eligibility. It marks the record as certified on 17 September
2026, with the bounty paid. The result is not refereed.

On 27 September 2026 the site's curator, Thomas Bloom, posted the claim on the
erdosproblems.com proof-claims forum so that it could be discussed. The curator
stated that they had not verified the proof, did not claim the formalization
correct and did not endorse the platform. The site labeled the problem OPEN.

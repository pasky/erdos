---
name: graph_coloring/rinot_2015_chromatic_numbers_graphs_large_gaps/theorem_3_3
title: "Rinot Theorem 3.3 — (ℵ₀, μ)-chromatic graphs of size λ⁺ for every μ ≤ λ"
desc: |
  Proves that if square_lambda and 2^lambda = lambda^+ hold for an infinite
  cardinal lambda, then for every cardinal mu <= lambda some graph on lambda^+
  vertices has chromatic and coloring number mu while every subgraph on fewer
  than lambda^+ vertices is countably chromatic.
created: 2026-10-14T22:51:38Z
updated: 2026-10-14T22:51:38Z
---

***

**Source.** A. Rinot, *Chromatic numbers of graphs — large gaps*: Theorem 3.3,
p. 15, proof pp. 15–16, in the author's copy dated April 12, 2013, which is
not the journal edition (Combinatorica **35** (2015), 215–233). Labels and pages
are the copy's; the journal edition was not compared. The copy is named on the
[[graph_coloring/rinot_2015_chromatic_numbers_graphs_large_gaps/_index|source card]].

**Definitions.** For a graph $(W,E)$, $\operatorname{Chr}(W,E)$ is the least
$\kappa$ admitting a coloring $\chi:W\to\kappa$ with $\chi(x)\ne\chi(y)$
whenever $x$ and $y$ are joined, and the coloring number
$\operatorname{Col}(W,E)$ is the least $\kappa$ such that some well-ordering of
$W$ gives every vertex fewer than $\kappa$ neighbours preceding it (p. 11);
always $\operatorname{Chr}\le\operatorname{Col}$. A graph $G$ is
$(\aleph_0,\kappa)$-chromatic when $\operatorname{Chr}(G)=\kappa$ and every
subgraph on fewer than $|G|$ vertices is countably chromatic (p. 1). Jensen's
$\square_\lambda$ asserts a sequence $\langle C_\alpha:\alpha<\lambda^+\rangle$
in which each $C_\alpha$, for limit $\alpha$, is a club in $\alpha$ of order
type at most $\lambda$, and which is coherent: $C_\beta=C_\alpha\cap\beta$
whenever $\beta$ is a limit point of $C_\alpha$ (p. 3).
$\mathrm{CH}_\lambda$ is $2^\lambda=\lambda^+$ (p. 3).

**Statement.** Let $\lambda$ be an infinite cardinal such that
$\square_\lambda$ holds and $2^\lambda=\lambda^+$. Then for every cardinal
$\mu\le\lambda$ there is a graph $(G,E)$ with

- $|G|=\lambda^+$;
- $\operatorname{Chr}(G,E)=\operatorname{Col}(G,E)=\mu$;
- $\operatorname{Chr}(G',E')\le\aleph_0$ for every $G'\subseteq G$ with
  $|G'|<\lambda^+$ and every $E'\subseteq E\cap[G']^2$.

For uncountable $\mu$ the graph is $(\aleph_0,\mu)$-chromatic of size
$\lambda^+$: its chromatic number is $\mu$, and every subgraph on fewer than
$\lambda^+$ vertices, whichever of the available edges it keeps, is countably
chromatic.

**Scope.** The hypotheses are $\square_\lambda$ and $2^\lambda=\lambda^+$ at
the single cardinal $\lambda$; the theorem derives the graph from them in ZFC,
without forcing and without large cardinals. The chromatic number $\mu$ is at
most $\lambda$; chromatic number $\lambda^+$ is the subject of Theorem 3.1
($\lambda$ singular, the same hypotheses) and Theorem 3.2 ($\square_\lambda$
and $\lambda^{<\lambda}=\lambda$, after adding a Cohen subset of $\lambda$),
both on the source card. The abstract states the theorem for uncountable
$\lambda$, and the proof treats countable $\lambda$ as trivial.

**Proof sketch.** The paper's argument, paraphrased (pp. 15–16), for
uncountable $\lambda$. By a theorem of the paper's reference [10], quoted and
not proved here, $\square_\lambda$ and $2^\lambda=\lambda^+$ give the
Ostaszewski square of Definition 2.1 (p. 4): a $\square_\lambda$-sequence
$\langle C_\alpha:\alpha<\lambda^+\rangle$ that also guesses. For every limit
$\theta<\lambda$, every sequence $\langle A_i:i<\theta\rangle$ of cofinal
subsets of $\lambda^+$ and every club $D\subseteq\lambda^+$, some $C_\alpha$ of
order type $\theta$ has its least point in $D$ and, for every $i<\theta$, its
$(i+1)$-st point in $A_i$ and a point of $D$ strictly between its $i$-th and
$(i+1)$-st points.

For an infinite regular $\kappa<\lambda$, the vertices are the
$\alpha<\lambda^+$ whose club $C_\alpha$ has order type $\kappa$, and
$\alpha<\delta$ are joined when $\alpha\in C_\delta$ and
$\min(C_\alpha)>\sup(C_\delta\cap\alpha)$. The argument of Theorem 3.1
(pp. 11–14) is rerun with this sequence. The guessing property defeats every
coloring with $\kappa$ colors, so the chromatic number exceeds $\kappa$. The
earlier neighbours of a vertex $\delta$ all lie in $C_\delta$, so the coloring
number is at most $\kappa^+$. Coherence lets countable proper colorings of the
initial segments be extended from one segment to the next, through successor
and limit stages, so every initial segment is countably chromatic, and a
subgraph on fewer than $\lambda^+$ vertices lies inside one initial segment
because $\lambda^+$ is regular. This gives chromatic and coloring number
$\kappa^+$. The print states that this settles every successor $\mu\le\lambda$;
the case used below, $\mu=\aleph_1$, is $\kappa=\omega$.

For a limit $\mu\le\lambda$, the graph is the union of these graphs over the
infinite regular $\kappa<\mu$, which lie on disjoint vertex sets: a coloring
with fewer than $\mu$ colors fails on one of the pieces, every vertex has fewer
than $\mu$ earlier neighbours, and a small subgraph is countably colored piece
by piece (Claims 3.3.1 and 3.3.2, p. 16). Finite and countable $\mu$ are
straightforward.

**Read depth.** Claims checked: the statement and the definitions it uses were
read clause by clause on the page images of the copy (pp. 1, 3, 11 and 15). The
proof (pp. 15–16) and the argument of Theorem 3.1 it reruns (pp. 11–14) were
read for their structure only; no step was checked. Nothing here is
independently reviewed.

**Dependencies.** Definition 2.1 (p. 4), and the theorem of the paper's
reference [10] (A. Rinot, *The Ostaszewski square, and homogeneous Souslin
trees*, listed there as accepted by the Israel Journal of Mathematics) that
for uncountable $\lambda$ the hypotheses give a sequence as in Definition 2.1;
the paper quotes it without proof. The proof of Theorem 3.1 (pp. 11–14), whose
argument is rerun.

**Bears on.**

- [[../wiki/problems/graph_coloring/E0918/_index|Problem 918]]: with
  $\lambda=\aleph_\omega$ and $\mu=\aleph_1$ the theorem gives, under
  $\square_{\aleph_\omega}$ and $2^{\aleph_\omega}=\aleph_{\omega+1}$, a graph
  on $\aleph_{\omega+1}$ vertices of chromatic number $\aleph_1$ whose
  subgraphs on $\aleph_\omega$ vertices are all countably chromatic: a yes to
  the second question. Both hypotheses hold when $0^\sharp$ does not exist and
  $\aleph_\omega$ is a strong limit cardinal, by the results of Jensen that
  the proof of Corollary 3.5 invokes (p. 17), and so in the constructible
  universe. Relative to the consistency of ZF, ZFC therefore does not refute
  the second question, as
  [[../wiki/problems/graph_coloring/E0918/claims/2014_08_05_rinot|the problem's claim page]]
  records. The theorem gives no model without such a graph, and it does not
  address the first question.

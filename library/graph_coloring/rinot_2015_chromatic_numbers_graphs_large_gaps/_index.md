---
name: graph_coloring/rinot_2015_chromatic_numbers_graphs_large_gaps
title: "Rinot: Chromatic numbers of graphs — large gaps"
desc: |
  Shows that if square_lambda and 2^lambda = lambda^+ hold, then for every
  cardinal kappa <= lambda some graph of size lambda^+ has chromatic number
  kappa while all its smaller subgraphs are countably chromatic, and gives
  such graphs of chromatic number lambda^+ when lambda is singular and, from
  square_lambda and lambda^{<lambda} = lambda, after adding a Cohen subset of
  lambda.
license: unstated
created: 2026-10-14T22:51:38Z
updated: 2026-10-14T23:06:55Z
---

# Rinot: Chromatic numbers of graphs — large gaps

[[graph_coloring/_index|..]]

[[graph_coloring/rinot_2015_chromatic_numbers_graphs_large_gaps/theorem_3_3|theorem_3_3]]: Proves that if square_lambda and 2^lambda = lambda^+ hold for an infinite
cardinal lambda, then for every cardinal mu <= lambda some graph on lambda^+
vertices has chromatic and coloring number mu while every subgraph on fewer
than lambda^+ vertices is countably chromatic.

***

A. Rinot, *Chromatic numbers of graphs — large gaps*, Combinatorica **35**
(2015), 215–233, doi:10.1007/s00493-014-3074-7.

The copy read for this card is not the journal edition. It is the author's own
typeset copy (LaTeX, 18 pages numbered 1–18, without the journal's header or
pagination), served at <https://www.assafrinot.com/files/rinot12.pdf>. Its
first page is dated April 12, 2013, and its reference list gives two cited
papers as "accepted", so it predates the journal edition. The two editions were
not compared: the journal's wording, numbering and pages may differ, and labels
and pages on this card and its result page are the copy's own. The copy prints
no copyright or license notice, and no terms were read for the author's page.
Crossref's record for the journal edition's DOI (read 2026-10-14) lists only
Springer's text-and-data-mining license, but it concerns the journal edition,
not the copy read; the term is unstated.

Source: <https://www.assafrinot.com/files/rinot12.pdf>.

**What the paper proves.** A graph $G$ is $(\aleph_0,\kappa)$-chromatic when
its chromatic number is $\kappa$ and every subgraph on fewer than $|G|$
vertices is countably chromatic (abstract, p. 1). The graphs are built from
sequences of clubs: given clubs $C_\alpha\subseteq\alpha$, the vertices are
certain limit ordinals, and $\alpha<\delta$ are joined when
$\alpha\in C_\delta$ and $\min(C_\alpha)>\sup(C_\delta\cap\alpha)$ (p. 2).
Coherence of the sequence keeps the small subgraphs countably chromatic, and
guessing properties of the sequence raise the chromatic number. Section 2
obtains the sequences: from $\square_\lambda$ and $2^\lambda=\lambda^+$ for
singular $\lambda$ (Theorem 2.2, p. 4), and from $\square_\lambda$ with
$\lambda^{<\lambda}=\lambda$ after adding one Cohen subset of $\lambda$
(Theorem 2.3, p. 8). Section 3 builds the graphs, whose coloring number equals
their chromatic number:

- Theorem 3.1 (p. 11): if $\square_\lambda$ and $2^\lambda=\lambda^+$ hold for
  a singular $\lambda$, some graph of size $\lambda^+$ has chromatic and
  coloring number $\lambda^+$ while all its subgraphs on fewer than
  $\lambda^+$ vertices are countably chromatic.
- Theorem 3.2 (p. 14): if $\lambda^{<\lambda}=\lambda$ and $\square_\lambda$
  hold, such a graph of size and chromatic number $\lambda^+$ exists after
  adding one Cohen subset of $\lambda$.
- [[graph_coloring/rinot_2015_chromatic_numbers_graphs_large_gaps/theorem_3_3|Theorem 3.3]]
  (p. 15): if $\square_\lambda$ and $2^\lambda=\lambda^+$ hold for an infinite
  $\lambda$, then for every cardinal $\mu\le\lambda$ some graph of size
  $\lambda^+$ has chromatic and coloring number $\mu$ while all its subgraphs
  on fewer than $\lambda^+$ vertices are countably chromatic. This is the main
  result as the abstract states it, there for uncountable $\lambda$.
- Corollary 3.4 (p. 16): from $\square_{\omega_1}$ and CH, the
  $\sigma$-closed forcing $\mathrm{Add}(\omega_1,1)$, of size $\aleph_1$, adds
  an $(\aleph_0,\aleph_2)$-chromatic graph of size $\aleph_2$. This is
  Theorem 3.2 at $\lambda=\aleph_1$, and the paper sets it beside
  Baumgartner's forcing construction (pp. 16–17).
- Corollary 3.5 (p. 17): if $0^\sharp$ does not exist, every singular strong
  limit cardinal $\lambda$ carries an $(\aleph_0,\lambda^+)$-chromatic graph
  of size $\lambda^+$, since Jensen's results then give $\square_\lambda$ and
  $2^\lambda=\lambda^+$ and Theorem 3.1 applies.

**Read status.** Claims checked for Theorem 3.3, the result the corpus
consumes: its statement (p. 15) and the definitions it uses, of
$(\aleph_0,\kappa)$-chromatic graphs (p. 1), of $\square_\lambda$ and
$\mathrm{CH}_\lambda$ (p. 3) and of the coloring number (p. 11), were read
clause by clause on the page images of the copy. The abstract, the Main Result
(p. 3), Definition 2.1 (p. 4), Theorems 2.2, 2.3, 3.1 and 3.2 and Corollaries
3.4 and 3.5 were read on the page images too. The proofs were read for their
structure only, and no step was checked. Nothing here is independently
reviewed.

**Connections.** In the constructible universe, where GCH and
$\square_{\aleph_\omega}$ hold, Theorem 3.3 with $\lambda=\aleph_\omega$ and
$\mu=\aleph_1$ gives the graph asked for in
[[graph_coloring/erdos_1968_chromatic_number_infinite_graphs/problem_1|Problem 1 of Erdős and Hajnal (1968)]],
with chromatic number exactly $\aleph_1$.

**Bears on.** [[../wiki/problems/graph_coloring/E0918/_index|#918]]:
[[graph_coloring/rinot_2015_chromatic_numbers_graphs_large_gaps/theorem_3_3|Theorem 3.3]]
with $\lambda=\aleph_\omega$ and $\mu=\aleph_1$ answers the second question yes
under $\square_{\aleph_\omega}$ and $2^{\aleph_\omega}=\aleph_{\omega+1}$, which
hold in the constructible universe, so ZFC does not refute that question; the
paper gives no model without such a graph. Corollary 3.4 (p. 16) gives a model
in which the first question has a positive answer: force with
$\mathrm{Add}(\omega_1,1)$ over a model of $\square_{\omega_1}$ and CH, such as
the constructible universe. The paper compares this with Baumgartner's
construction (pp. 16–17).

No file of this source is held: no license on record permits its redistribution,
and the card cites the edition it names above.

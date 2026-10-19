---
name: set_theory/hajnal_komjath_2003_simultaneous_chromatic_number
title: "Hajnal–Komjáth: Some remarks on the simultaneous chromatic number"
desc: |
  Shows that adding a Cohen subset of kappa, where kappa^{<kappa} = kappa,
  makes every graph of chromatic number kappa^+ edge-colorable with kappa^+
  colors so that every partition of its vertices into at most kappa parts has
  a part spanning all colors (one Cohen real suffices at aleph_1), with
  related ZFC, diamond-plus and consistency results.
license: reserved
created: 2026-10-14T22:51:38Z
updated: 2026-10-14T23:06:55Z
---

# Hajnal–Komjáth: Some remarks on the simultaneous chromatic number

[[set_theory/_index|..]]

[[set_theory/hajnal_komjath_2003_simultaneous_chromatic_number/theorem_1|theorem_1]]: Proves that if kappa^{<kappa} = kappa, then after adding one Cohen subset of
kappa every graph of chromatic number kappa^+ has an edge coloring with
kappa^+ colors such that every partition of its vertices into at most kappa
parts has a part spanning edges of every color.

***

A. Hajnal and P. Komjáth, *Some remarks on the simultaneous chromatic number*,
Combinatorica **23** (2003), no. 1, 89–104, doi:10.1007/s00493-003-0015-2.
The paper was received on 13 August 2000 (p. 89).

The copy read for this card is the publisher's PDF of the journal edition, from
SpringerLink: 16 pages, printed pp. 89–104. It prints "©2003 János Bolyai
Mathematical Society" at the foot of its first page and no license, every other
right reserved. Crossref's record for the DOI (read 2026-10-14) agrees: it names
Springer Science and Business Media LLC as publisher and lists only Springer's
text-and-data-mining license, no Creative Commons license. Labels and pages
below are the journal's.

Source: <https://doi.org/10.1007/s00493-003-0015-2>.

**The property studied.** For a graph $X$ on a vertex set $V$ and cardinals
$\lambda,\kappa$, the paper writes $P(X,\lambda,\kappa)$ when the edges of $X$
can be colored with $\lambda$ colors so that, whenever $V$ is split into fewer
than $\kappa$ parts, some part spans edges of every color; $Q(\kappa)$ says that
$P(X,\kappa,\kappa)$ holds for every graph $X$ of chromatic number exactly
$\kappa$ (p. 91). The abstract poses $Q(\aleph_1)$ as an "as yet unsolved"
conjecture (p. 89). The introduction (pp. 89–90) recalls that Todorčević proved
$P(X,\aleph_1,\aleph_1)$ in ZFC for the complete graph $X$ on $\aleph_1$
vertices, and says that the authors' method does not show $Q(\aleph_1)$
independent.

**Result consumed.**
[[set_theory/hajnal_komjath_2003_simultaneous_chromatic_number/theorem_1|Theorem 1]]
(p. 91, proof p. 92): if $\kappa^{<\kappa}=\kappa$ and one Cohen subset of
$\kappa$ is added, then $Q(\kappa^+)$ holds in the extension. At
$\kappa=\omega$ the hypothesis holds outright, so adding one Cohen real to any
model of ZFC gives a model in which every graph of chromatic number $\aleph_1$
has the edge coloring that Problem 1176 asks for. The result page states what
the theorem covers and what it leaves open.

**Other results.**

- Theorem 2 (p. 92): if $\mu^{<\mu}=\mu$ and more than $\kappa$ Cohen subsets
  of $\mu$ are added, then in the extension every graph on $\kappa$ of
  chromatic number $\tau>\mu$ satisfies $P(X,\mu,\tau)$.
- Theorem 3 (p. 93): under GCH, if $\kappa$ is strongly inaccessible and more
  than $\kappa$ Cohen subsets of $\kappa$ are added, then in the extension
  $P(X,\kappa,\kappa)$ holds for every $\kappa$-chromatic graph $X$ on
  $\kappa$ whose initial segments $X|\alpha$ ($\alpha<\kappa$) have chromatic
  numbers bounded below $\kappa$.
- Theorem 4 (p. 94): under $\diamondsuit^+$, every graph $X$ on $\omega_1$ of
  chromatic number $\aleph_1$ has an edge coloring $F:X\to\omega_1$ that takes
  every value on the edges inside every $A\subseteq\omega_1$ inducing an
  uncountably chromatic subgraph; in particular $P(X,\omega_1,\omega_1)$
  holds.
- Theorem 5 (p. 95): it is consistent that $2^{\aleph_0}=\aleph_2$ and that
  some graph $X$ on $\omega_1$ of chromatic number $\aleph_1$ has, for every
  $F:X\to2$, an $\aleph_1$-chromatic $A\subseteq\omega_1$ on whose edges $F$
  takes one value. This defeats the hereditary form of Theorem 4 for that
  graph, not $P(X,\omega_1,\omega_1)$.
- Theorem 6 (p. 98): if a measurable cardinal is consistent, then it is
  consistent that some inaccessible $\kappa$ (weakly inaccessible in the
  introduction's account, p. 90) carries a graph $X$ on $\kappa$ of chromatic
  number $\kappa$ such that for every $F:X\to\omega_1$ some countably
  chromatic $A\subseteq\kappa$ leaves $F$ bounded below $\omega_1$ on the
  edges with both ends outside $A$; as the introduction notes, this makes
  $P(X,\omega_1,\omega_1)$ fail.
- Theorem 7 (p. 98): in ZFC, if $\operatorname{Chr}(X)=\kappa>\omega$ and
  $\tau$ is a cardinal, some graph $Y$ with the same finite induced subgraphs
  as $X$ satisfies $P(Y,\tau,\kappa)$.
- Theorem 8 (p. 101): in ZFC, (a) $P([\kappa]^2,\kappa,\kappa)$ holds when
  $\kappa$ is inaccessible or the successor of a regular cardinal, the
  successor case being, as the proof says, a special case of a theorem of
  Todorčević; (b) $P([\lambda^+]^2,\mu,\lambda^+)$ holds for singular
  $\lambda$ and every $\mu<\lambda$.
- Theorem 9 (p. 102): in ZFC,
  $P(\mathrm{Sh}_n(\exp_n(\kappa)),\kappa,\kappa^+)$ holds for $2\le n<\omega$
  and infinite $\kappa$, where $\mathrm{Sh}_n$ is the $n$-shift graph and
  $\exp_n$ the $n$-fold iterated power (both defined on p. 91).

**Read status.** Claims checked for Theorem 1: its statement and the
definitions of $P$ and $Q$ it uses (p. 91) were read clause by clause on the
page images, as were the statements of Theorems 2–9 summarized above and the
abstract and introduction (pp. 89–91). The proof of Theorem 1 (p. 92) was read
for its structure only, and no step of any proof was checked. Nothing here is
independently reviewed.

**Connections.** The question the paper works on is
[[set_theory/erdos_1975_set_systems_having_large_chromatic_number/problem_3|Problem 3 of Erdős, Galvin and Hajnal (1975)]],
the paper's reference [1], which asks whether $Q(\kappa)$ holds for every
infinite $\kappa$; its case $\kappa=\aleph_1$ is Problem 1176. Soukup's 2015
handout records that case as consistent by adding a single Cohen real and cites
this paper for it
([[set_theory/soukup_2015_open_problems_around_uncountable_graphs/conjecture_6_1|its Conjecture 6.1]]);
Theorem 1 with $\kappa=\omega$ is that result.

**Bears on.** [[../wiki/problems/set_theory/E1176/_index|#1176]]:
[[set_theory/hajnal_komjath_2003_simultaneous_chromatic_number/theorem_1|Theorem 1]]
with $\kappa=\omega$ gives the problem's statement, for every graph of
chromatic number $\aleph_1$, after one Cohen real is added to any model of ZFC,
so ZFC does not refute it; the paper leaves open whether ZFC proves it.
Theorem 8(a) with $\kappa=\omega_1$ proves the statement in ZFC for the
complete graph on $\aleph_1$ vertices, and Theorem 4 proves it under
$\diamondsuit^+$ for every graph on $\omega_1$ of chromatic number $\aleph_1$,
in a hereditary form that Theorem 5 shows can fail. Theorem 6 concerns a graph
of inaccessible chromatic number and says nothing about chromatic number
$\aleph_1$.

No file of this source is held: no license on record permits its redistribution,
and the card cites the edition it names above.

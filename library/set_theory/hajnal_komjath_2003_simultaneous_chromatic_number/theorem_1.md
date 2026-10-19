---
name: set_theory/hajnal_komjath_2003_simultaneous_chromatic_number/theorem_1
title: "Hajnal–Komjáth Theorem 1 — Q(κ⁺) after adding a Cohen subset of κ"
desc: |
  Proves that if kappa^{<kappa} = kappa, then after adding one Cohen subset of
  kappa every graph of chromatic number kappa^+ has an edge coloring with
  kappa^+ colors such that every partition of its vertices into at most kappa
  parts has a part spanning edges of every color.
created: 2026-10-14T22:51:38Z
updated: 2026-10-14T22:51:38Z
---

***

**Source.** A. Hajnal and P. Komjáth, *Some remarks on the simultaneous
chromatic number*, Combinatorica **23** (2003), 89–104: Theorem 1, p. 91, with
the definitions it uses on the same page and its proof on p. 92. Pages are the
journal's; the edition read is named on the
[[set_theory/hajnal_komjath_2003_simultaneous_chromatic_number/_index|source card]].

**Definitions** (p. 91). A graph is a pair $(V,X)$ with $X\subseteq[V]^2$, and
its chromatic number $\operatorname{Chr}(V,X)$ is the least cardinal $\mu$ for
which some $f:V\to\mu$ gives the two ends of every edge different values. For
cardinals $\lambda$ and $\kappa$, $P(X,\lambda,\kappa)$ says that some
$F:X\to\lambda$ has the following property: whenever
$V=\bigcup_{i<\mu}V_i$ with $\mu<\kappa$, there is $i<\mu$ such that $F$ takes
every value below $\lambda$ on $X\cap[V_i]^2$. $Q(\kappa)$ says that
$P(X,\kappa,\kappa)$ holds for every graph $(V,X)$ with
$\operatorname{Chr}(V,X)=\kappa$.

**Statement.** Let $\kappa$ be an infinite cardinal with
$\kappa^{<\kappa}=\kappa$. Force over the ground model with the functions from
an ordinal below $\kappa$ into $\kappa$, ordered by extension; this adds one
Cohen-generic function $G:\kappa\to\kappa$, which the statement calls adding a
Cohen subset of $\kappa$ (the forcing is written out at the start of the
proof, p. 92). Then $Q(\kappa^+)$ holds in the extension: every graph of
chromatic number exactly $\kappa^+$ has an edge coloring with $\kappa^+$ colors
such that, for every partition of its vertex set into at most $\kappa$ parts,
some single part spans edges of all $\kappa^+$ colors.

**Scope.**

- *Hypothesis.* Only $\kappa^{<\kappa}=\kappa$ in the ground model, so
  $\kappa$ is regular. For $\kappa=\omega$ it holds in ZFC, the forcing is
  Cohen forcing and adds one Cohen real, and nothing else is assumed: no CH,
  GCH, large cardinal or other principle.
- *Graphs covered.* Every graph of the extension whose chromatic number there
  is exactly $\kappa^+$, whatever the size of its vertex set and whether or
  not it lies in the ground model: the proof starts from an arbitrary such
  graph of the extension (p. 92).
- *Partitions covered.* Every partition of the vertex set into at most
  $\kappa$ parts, finite partitions included; one part receives all
  $\kappa^+$ colors.
- *The case of Problem 1176.* With $\kappa=\omega$: in the extension of any
  model of ZFC by one Cohen real, every graph of chromatic number $\aleph_1$
  has an edge coloring with $\aleph_1$ colors such that every partition of its
  vertices into countably many parts has a part spanning edges of every color.
  So if ZFC is consistent, then so is ZFC together with this statement, and
  ZFC does not refute it.
- *Not covered.* Whether the statement holds in ZFC, in the ground model
  before the Cohen subset is added, or in models not obtained this way. The
  abstract calls $Q(\aleph_1)$ "as yet unsolved" (p. 89), and the
  introduction says that the authors' method "does not give a proof of the
  independence of $Q(\aleph_1)$" (p. 90). The theorem reaches only the
  chromatic numbers $\kappa^+$ with $\kappa^{<\kappa}=\kappa$, so not limit
  cardinals, for example; the paper treats inaccessible $\kappa$ separately,
  in Theorems 3 and 6. Nor does it assert the stronger hereditary form of
  Theorem 4, in which every uncountably chromatic induced subgraph receives
  every color.

**Proof sketch.** The paper's argument, paraphrased (p. 92). In the ground
model fix, for each $\gamma<\kappa$, a map $f_\gamma:\kappa^+\to\kappa^+$ such
that every ordinal below any $\alpha<\kappa^+$ equals $f_\gamma(\alpha)$ for
some $\gamma<\kappa$; this is possible because each such $\alpha$ has at most
$\kappa$ elements. Given a graph of the extension with chromatic number
$\kappa^+$, split its vertices into independent sets $A_\alpha$
($\alpha<\kappa^+$). An edge joining $A_\beta$ to $A_\alpha$ with $\beta<\alpha$
has $\beta=f_\gamma(\alpha)$ for some $\gamma$; take the least stage
$\delta\ge\gamma$ at which the initial segment of the generic function decides
that edge and the classes of its ends, and color the edge
$f_{G(\delta)}(\alpha)$. So the generic's next value, read through the
ground-model enumeration of $\alpha$, chooses the color.

Given a partition of the vertices into parts $B_i$ ($i<\kappa$), each vertex is
forced into its part by some condition of the generic filter. The forcing has
only $\kappa$ conditions, since $\kappa^{<\kappa}=\kappa$, so some set $L$ of
vertices sharing one condition $p$ and one part $B_i$ is still
$\kappa^+$-chromatic. For a target color $\xi$, the paper uses this to find
$\alpha>\xi$ such that the vertices of $L$ in $A_\alpha$ are joined to vertices
of $L$ in $\kappa$ many earlier classes, one of which is $A_\beta$ with
$\beta=f_\delta(\alpha)$ for some $\delta$ at least the length of $p$. Extending
the condition that decides such an edge by one more value $\tau$ with
$f_\tau(\alpha)=\xi$ forces that edge, which lies inside $B_i$, to receive color
$\xi$, and from this the paper concludes that every color occurs inside $B_i$.

**Read depth.** Claims checked: the statement and the definitions of $P$ and
$Q$ were read clause by clause on the page image of p. 91. The proof on p. 92
was read for its structure only; no step was checked. Nothing here is
independently reviewed.

**Dependencies.** None within the paper; the proof uses only the basic
machinery of forcing. The property $P$ is the direct form of Definition 6.2 of
[[set_theory/erdos_1975_set_systems_having_large_chromatic_number/problem_3|Erdős, Galvin and Hajnal (1975)]],
the paper's reference [1].

**Bears on.**

- [[../wiki/problems/set_theory/E1176/_index|Problem 1176]]: the case
  $\kappa=\omega$ is the problem's statement in the extension of any model of
  ZFC by one Cohen real, for every graph of chromatic number $\aleph_1$ in
  that extension. It shows that ZFC does not refute the statement, the result
  recorded on
  [[../wiki/problems/set_theory/E1176/claims/2003_01_01_hajnal_komjath|the problem's claim page]],
  and it leaves open whether ZFC proves it.

---
name: set_theory/darby_1999_negative_partition_relations_ordinals/theorem_6_1
title: "Theorem 6.1 (p. 221): ω^α ↛ (ω^α, 6)^2 for α additively but not multiplicatively indecomposable, and ω^α ↛ (ω^α, 4)^2 when ᾱ is not multiplicatively indecomposable either"
desc: |
  Darby's main theorem: ω^{ω^γ} ↛ (ω^{ω^γ}, 6)^2 when the countable γ is a sum
  of at least two indecomposables and ω^{ω^γ} ↛ (ω^{ω^γ}, 4)^2 when it is a
  sum of at least three, by colorings with small cliques in one color and no
  set of full order type in the other.
created: 2026-10-14T22:55:45Z
updated: 2026-10-14T22:55:45Z
---

***

**Source.** Carl Darby, *Negative partition relations for ordinals
$\omega^{\omega^\alpha}$* (1999): Theorem 6.1 and its proof, p. 221; the
introduction's Theorem 1.1, p. 206; Lemmas 3.4 (p. 211), 3.6 (p. 212), 5.14
(p. 219) and 5.15 (p. 220). The edition is identified on the
[[set_theory/darby_1999_negative_partition_relations_ordinals/_index|source card]].

**Statement.** Let $\alpha<\omega_1$ be additively indecomposable (AI) but not
multiplicatively indecomposable (MI). Then
$\omega^\alpha\not\to(\omega^\alpha,6)^2$: the pairs from $\omega^\alpha$ can
be split into two classes so that no set of order type $\omega^\alpha$ has all
its pairs in the first class and no set of six elements has all its pairs in
the second. If moreover $\bar\alpha$, the product of all but the last factor
of the multiplicative normal form of $\alpha$, is not MI, then
$\omega^\alpha\not\to(\omega^\alpha,4)^2$, in the same sense with four
elements in place of six. The terms are those of the
[[set_theory/darby_1999_negative_partition_relations_ordinals/definitions|definitions page]].

**Exponent form.** Every AI ordinal is $\omega^\gamma$ for some $\gamma$. For
$\gamma>0$ with additive normal form $\gamma_0+\cdots+\gamma_k$, the
multiplicative normal form of $\omega^\gamma$ is
$\omega^{\gamma_0}\cdots\omega^{\gamma_k}$. So $\omega^\gamma$ is not MI
exactly when $k\ge1$, and the product
$\omega^{\gamma_0}\cdots\omega^{\gamma_{k-1}}$ of all but its last factor is
not MI exactly when $k\ge2$. The
theorem therefore says: for every countable $\gamma$ that is a sum of at least
two additively indecomposable ordinals,
$\omega^{\omega^\gamma}\not\to(\omega^{\omega^\gamma},6)^2$, and for every
countable $\gamma$ that is a sum of at least three,
$\omega^{\omega^\gamma}\not\to(\omega^{\omega^\gamma},4)^2$. This translation
is made here.

The introduction's Theorem 1.1 (p. 206) states the result in this exponent
form, with the paper's letter $\alpha$ for $\gamma$: the 6-relation for
$\gamma=\gamma_0+\gamma_1$ with $\gamma_0\ge\gamma_1$, and the 4-relation for
$\gamma=\gamma_0+\gamma_1+\gamma_2$ with $\gamma_0\ge\gamma_1\ge\gamma_2$. It
does not say that the terms are nonzero; with nonzero terms, such sums are
exactly the ordinals with at least two, respectively three, terms in their
additive normal form (a check made here), so the two statements agree. The
abstract (p. 205) states the result for multiplicatively decomposable $\alpha$,
in the notation of Theorem 6.1. At $\gamma=2=1+1$ the theorem gives
$\omega^{\omega^2}\not\to(\omega^{\omega^2},6)^2$, which disproves the
conjecture that the paper attributes to Erdős and Hajnal and to Galvin and
Larson (p. 206, citing its [3] and [6]):
$\omega^{\omega^\gamma}\to(\omega^{\omega^\gamma},n)^2$ for every finite $n$
and every countable $\gamma$.

**Notation of Problem 592.** Theorem 6.1's $\alpha$ is the $\beta$ of
[[../wiki/problems/set_theory/E0592/_index|Problem 592's page]], and the
$\gamma$ above is that page's $\gamma$ and the $\beta$ of Schipperus's paper.

**Proof pointer.** The proof (p. 221) colors the pairs of the set $G_\alpha$,
whose lexicographic order type is $\omega^\alpha$ (Lemma 2.9), by the coloring
$\Delta$ of Definition 3.3, or, when $\bar\alpha$ is not MI, by $\Gamma$ of
Definition 3.5. Two lemmas bound the cliques of the second color: a set all of
whose pairs lie in $\Delta_1$ has at most five members (Lemma 3.4), and a set
all of whose pairs lie in $\Gamma_1$ has at most three (Lemma 3.6). Two lemmas
exclude sets of full order type in the first color: for $\alpha$ AI but not MI,
every $W\subseteq G_\alpha$ of order type $\omega^\alpha$ contains a pair in
$\Delta_1$ (Lemma 5.14), and if $\bar\alpha$ is not MI either, such a $W$
contains a pair in $\Gamma_1$ (Lemma 5.15). The clique bounds come from
tracking, along a clique $a_0,a_1,\ldots$, where the coordinates of each later
member can lie relative to the box coordinates of the earlier ones. The
realization lemmas choose the segments of $a$ and $b$ alternately as maximal
prefixes of suitable subsets of $W$, using Galvin's prefixes and good sets
(§ 4, Definitions 4.1 and 4.3, Lemmas 4.2 and 4.5) and the $(k,n)$ sets of
Definition 5.8 (§ 5). Not reconstructed here.

**Source correction.** The proof paragraph prints "If $\bar\alpha$ is MI then
the partition $[G_\alpha]^2=\Gamma_0\cup\Gamma_1$ is defined", "if $\alpha$ is
MI then $W$ contains a pair in $\Delta_1$" and "If $\bar\alpha$ is MI, then by
Lemma 5.15"; Definition 3.5 and Lemmas 5.14 and 5.15 need "not MI" in each
place, as the statement of the theorem has it. This is a filing observation,
not an author erratum.

**Read depth.** Claims checked: Theorem 6.1, its proof paragraph, Theorem 1.1,
the abstract and the statements of Lemmas 3.4, 3.6, 5.14 and 5.15 were read
clause by clause on the page images. The proofs of the four lemmas and the
machinery of §§ 4--5 were looked through on the page images and no step was
checked. Nothing here is independently reviewed.

**Dependencies.** Within the paper: Definitions 2.1, 2.8, 3.1--3.3 and 3.5,
Lemma 2.9, and Lemmas 3.4, 3.6, 5.14 and 5.15. The prefix and good-set tools of
§ 4 are credited to Galvin's circulated lecture notes (University of Colorado,
1971; the paper's [5]), which have no card in the library.

**Bears on.**

- [[../wiki/problems/set_theory/E0118/_index|#118]]: at $\alpha=\omega^2$
  the theorem gives $\omega^{\omega^2}\not\to(\omega^{\omega^2},6)^2$, the
  negative half of the problem's counterexample $\omega^{\omega^2}$ with
  $n=6$; the positive half is the paper's
  [[set_theory/darby_1999_negative_partition_relations_ordinals/theorem_6_2|Theorem 6.2]] (p. 221),
  stated there without proof.
- [[../wiki/problems/set_theory/E0592/_index|#592]]: in the problem's notation
  it gives $\omega^\beta\not\to(\omega^\beta,6)^2$ for $\beta=\omega^\gamma$
  with $\gamma$ a sum of at least two indecomposables, and
  $\omega^\beta\not\to(\omega^\beta,4)^2$ for at least three. It decides no
  case of the problem's triangle relation. At exactly three summands, the
  problem's undecided case, it gives independently the negative 4-relation
  that the problem page takes from Schipperus's Theorem 29(2).

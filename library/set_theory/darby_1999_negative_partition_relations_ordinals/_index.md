---
name: set_theory/darby_1999_negative_partition_relations_ordinals
title: "Darby: Negative partition relations for ordinals ω^{ω^α}"
desc: |
  Darby's 1999 proof that ω^α ↛ (ω^α, 6)^2 for every countable α that is
  additively but not multiplicatively indecomposable, and ω^α ↛ (ω^α, 4)^2
  when α has at least three multiplicative factors, by explicit colorings of
  finite sequences; it states without proof Darby's ω^{ω^2} → (ω^{ω^2}, 3)^2
  and conjectures a positive answer in the three-summand case of Problem 592.
license: reserved
created: 2026-10-14T22:55:45Z
updated: 2026-10-14T23:06:55Z
---

# Darby: Negative partition relations for ordinals ω^{ω^α}

[[set_theory/_index|..]]

[[set_theory/darby_1999_negative_partition_relations_ordinals/definitions|definitions]]: States Darby's representation of ω^α by finite increasing sequences, his
level prefixes with box and triangle coordinates, and the pair colorings Δ
and Γ, whose second colors have no 6-clique and no 4-clique.

[[set_theory/darby_1999_negative_partition_relations_ordinals/theorem_6_1|theorem_6_1]]: Darby's main theorem: ω^{ω^γ} ↛ (ω^{ω^γ}, 6)^2 when the countable γ is a sum
of at least two indecomposables and ω^{ω^γ} ↛ (ω^{ω^γ}, 4)^2 when it is a
sum of at least three, by colorings with small cliques in one color and no
set of full order type in the other.

[[set_theory/darby_1999_negative_partition_relations_ordinals/theorem_6_2|theorem_6_2]]: Records that Darby's paper states ω^{ω^2} → (ω^{ω^2}, 3)^2 as its author's
Theorem 6.2, in a list of results it neither proves nor gives references
for, and combines it with Theorem 6.1 to place ω^{ω^2} in neither of its
two classes.

***

Carl Darby, *Negative partition relations for ordinals
$\omega^{\omega^\alpha}$*, Journal of Combinatorial Theory, Series B **76**
(1999), 205--222, doi:10.1006/jctb.1999.1903; received 7 November 1996. Cited
as [Da99] on Problem 118's page.

The copy read for this card is the publisher's PDF from ScienceDirect, in the
journal's open archive: 18 pages, printed pp. 205--222 = PDF pp. 1--18
(printed p. $n$ is PDF p. $n-204$), typeset, with a text layer whose
mathematical symbols come out as punctuation, so the statements below were
read on rendered page images. The file prints "Copyright © 1999 by Academic
Press. All rights of reproduction in any form reserved." at the foot of its
first page (p. 205). The Crossref record
(<https://api.crossref.org/works/10.1006/jctb.1999.1903>, read 2026-10-14)
names Elsevier BV as publisher and lists only Elsevier's text-and-data-mining
user license and its open-archive user license, with no Creative Commons
license: every other right reserved.

**Notation.** The paper writes $\alpha\to(\beta,\gamma)^2$ for the ordinary
partition relation and $\alpha\not\to(\beta,\gamma)^2$ for its negation
(p. 205). A nonzero ordinal is additively indecomposable (AI) when it is not
the sum of two smaller ordinals, and an AI ordinal is multiplicatively
indecomposable (MI) when it is not the product of two smaller ordinals; for an
AI ordinal $\alpha$, $\bar\alpha$ is the product of all but the last factor of
its multiplicative normal form (p. 207). The paper's partition ordinals are the
countable $\alpha$ with $\alpha\to(\alpha,n)^2$ for every finite $n$, and its
anti-partition ordinals those with $\alpha\not\to(\alpha,3)^2$ (p. 205);
Schipperus's Definition 2 calls $\alpha$ a partition ordinal as soon as
$\alpha\to(\alpha,3)^2$. The letter $\alpha$ has two roles: the abstract,
§§ 2--5 and Theorem 6.1 write $\omega^\alpha$, while the title, Theorem 1.1,
Theorems 6.3--6.5 and Conjectures 6.8--6.9 write $\omega^{\omega^\alpha}$, whose
$\alpha$ is Schipperus's $\beta$ and Problem 592's $\gamma$. Theorem 6.1's
$\alpha$ is Problem 592's $\beta$.

**Main result.**
[[set_theory/darby_1999_negative_partition_relations_ordinals/theorem_6_1|Theorem 6.1]]
(p. 221, announced as Theorem 1.1 on p. 206): for countable $\alpha$ AI but not
MI, $\omega^\alpha\not\to(\omega^\alpha,6)^2$, and if moreover $\bar\alpha$ is
not MI, $\omega^\alpha\not\to(\omega^\alpha,4)^2$. In the exponent form, for
every countable $\gamma$ that is a sum of at least two additively
indecomposable ordinals,
$\omega^{\omega^\gamma}\not\to(\omega^{\omega^\gamma},6)^2$, and for at least
three, $\omega^{\omega^\gamma}\not\to(\omega^{\omega^\gamma},4)^2$. At
$\gamma=2$ this is $\omega^{\omega^2}\not\to(\omega^{\omega^2},6)^2$, which
disproves the conjecture that p. 206 attributes to Erdős and Hajnal
([[set_theory/erdos_1974_unsolved_solved_problems_set_theory/_index|Unsolved and solved problems in set theory]],
the paper's [3]) and to Galvin and Larson
([[set_theory/galvin_nd_pinning_countable_ordinals/_index|Pinning countable ordinals]],
its [6]): $\omega^{\omega^\gamma}\to(\omega^{\omega^\gamma},n)^2$ for every
finite $n$ and every countable $\gamma$.

**Method.** $\omega^\alpha$ is represented by a set $G_\alpha$ of finite
increasing sequences of natural numbers in lexicographic order, built by
recursion along fixed fundamental sequences (Definitions 2.1 and 2.8,
Lemma 2.9). A coordinate of a sequence is a box coordinate when the initial
segment ending there is a level prefix, or when it is the last coordinate, and
a triangle coordinate when that segment is a sub-level prefix (Definitions
3.1--3.2). Two colorings of pairs, $\Delta$ and $\Gamma$, ask how the segments
of two disjoint sequences interleave and which segments hold box or triangle
coordinates (Definitions 3.3 and 3.5). Lemmas 3.4 and 3.6 bound the cliques of
the second color by five and three; Lemmas 5.14 and 5.15 show that every subset
of $G_\alpha$ of order type $\omega^\alpha$ has a pair of the second color,
using the prefixes and good sets of an unpublished paper of Galvin (§ 4) and
the $(k,n)$ sets of § 5. The definitions are restated on
[[set_theory/darby_1999_negative_partition_relations_ordinals/definitions|the definitions page]].

**Other results listed in § 6.** After Theorem 6.1 the paper gives "a
chronologically ordered list" of results it calls recent (p. 221): Theorem 6.2
(Darby), $\omega^{\omega^2}\to(\omega^{\omega^2},3)^2$; Theorem 6.3
(Schipperus), $\omega^{\omega^\alpha}\to(\omega^{\omega^\alpha},3)^2$ when
$\alpha$ is AI or has two terms in its additive normal form; Theorem 6.4
(Schipperus), the failure of the triangle relation when that normal form has
at least four terms; Theorem 6.5 (Larson),
$\omega^{\omega^\alpha}\not\to(\omega^{\omega^\alpha},5)^2$ for two terms;
Theorem 6.6 (Larson), $\omega^{\omega^2}\to(\omega^{\omega^2},4)^2$; and
Theorem 6.7 (Darby),
$\omega^{\omega^{\omega^\alpha}}\not\to(\omega^{\omega^{\omega^\alpha}},k)^2$
for successor $\alpha$ and every $k$ with $k\to(4)^3_{2^{32}}$. None of these
is proved in the paper, and its reference list (p. 222) names no work of
Darby's or Schipperus's and none of Larson's after 1980. The paper concludes
that Theorem 6.2 with its own results exhibits $\omega^{\omega^2}$ as neither a
partition ordinal nor an anti-partition ordinal
([[set_theory/darby_1999_negative_partition_relations_ordinals/theorem_6_2|Theorem 6.2's page]]).

**Questions and conjectures (pp. 221--222).** For $\alpha$ not AI the paper
names two unresolved cases of $\omega^{\omega^\alpha}$: two terms, where it
asks whether the 4-relation holds (yes at $\alpha=2$ by Theorem 6.6), and three
terms, where it asks whether
$\omega^{\omega^\alpha}\to(\omega^{\omega^\alpha},3)^2$ or
$\omega^{\omega^\alpha}$ is an anti-partition ordinal. Conjecture 6.8 is the
4-relation for two terms. Conjecture 6.9, quoted: "If $\alpha$ has ANF
$\alpha=\alpha_0+\alpha_1+\alpha_2$ then
$\omega^{\omega^\alpha}\to(\omega^{\omega^\alpha},3)^2$." Conjecture 6.10
concerns the least $k$ with $T_n(\alpha)\not\to(T_n(\alpha),k)^2$ along the
towers $T_n(\alpha)=\omega^{T_{n-1}(\alpha)}$, and Conjecture 6.11 says that a
countable $\alpha>\omega^\omega$ is a partition ordinal exactly when
$\alpha=\omega^\alpha$.

**Source corrections.** Definition 3.2 prints "$g\restriction(i=1)=g$" for
$g\restriction(i+1)=g$, Definition 3.5 prints "$A_3{}^\frown AA_4$" for
$A_3{}^\frown A_4$, and the proof of Theorem 6.1 reads "MI" three times where
the definitions and lemmas it cites need "not MI"; the affected pages say so.
Theorem 6.4 prints its relation as
$\omega^{\omega^\alpha}\not\to(\omega^{\omega^\alpha},3)^3$, with superscript
3, while the next paragraph counts these ordinals as anti-partition ordinals,
the relation for pairs, and says $k>3$ where Theorem 6.4 has $k\ge3$. These are
filing observations, not an author erratum.

Read status: claims checked. The abstract (p. 205), Theorem 1.1 (p. 206), the
normal-form notation and Definition 2.1 (p. 207), Definitions 2.4, 2.6 and 2.8
and Lemma 2.9 (pp. 208--209), Definitions 3.1--3.3 (p. 210), Lemma 3.4
(p. 211), Definition 3.5 and Lemma 3.6 (p. 212), Lemmas 5.14 and 5.15
(pp. 219--220), Theorem 6.1 with its proof paragraph, Theorems 6.2--6.7 and the
discussion after them (p. 221), Conjectures 6.8--6.11 and the reference list
(p. 222) were read clause by clause on the page images. The proofs of Lemmas
3.4, 3.6, 5.14 and 5.15 and the machinery of §§ 4--5 were looked through on the
page images and no proof step was checked. Nothing here is independently
reviewed.

**Connections.**
[[set_theory/schipperus_2010_countable_partition_ordinals/_index|Schipperus's Countable partition ordinals]]
reports (p. 1197) that its negative relations for finite exponents are due
independently to Darby and to its author, and that Darby proved
$\omega^{\omega^2}\to(\omega^{\omega^2},3)^2$ independently. This paper proves
the 6- and 4-relations for every countable exponent with at least two,
respectively three, terms, and lists the failure of the triangle relation for
four or more terms as Schipperus's Theorem 6.4, without proving it. Erdős
reported Darby's counterexample in 1995, from a letter of Laver
([[graph_coloring/erdos_1995_problems_combinatorial_set_theory/section_1|Erdős 1995, § 1]]).

**Bears on.** [[../wiki/problems/set_theory/E0118/_index|#118]]: Theorem 6.1 at
$\alpha=\omega^2$ is $\omega^{\omega^2}\not\to(\omega^{\omega^2},6)^2$, the
negative half of the problem's counterexample; the positive half is Theorem
6.2, stated under Darby's name without proof (p. 221).
[[../wiki/problems/set_theory/E0591/_index|#591]]: Theorem 6.2 is the
problem's relation, stated without proof or reference, so the paper supplies
no proof of it. [[../wiki/problems/set_theory/E0592/_index|#592]]: in the
problem's notation Theorem 6.1 gives $\omega^\beta\not\to(\omega^\beta,6)^2$
for $\beta=\omega^\gamma$ with $\gamma$ a sum of at least two indecomposables,
and $\omega^\beta\not\to(\omega^\beta,4)^2$ for at least three, deciding no
case of the problem's triangle relation; for exactly three summands, the
problem's undecided case, the paper asks the question (p. 222) and conjectures
a positive answer (Conjecture 6.9), and its coloring $\Gamma$ is an explicit
published witness of the 4-relation there.

**Results.**

- [[set_theory/darby_1999_negative_partition_relations_ordinals/definitions|Definitions 2.1--3.5]]
  (pp. 207--212): the representation $G_\alpha$, level prefixes, box and
  triangle coordinates, and the colorings $\Delta$ and $\Gamma$ with their
  clique bounds.
- [[set_theory/darby_1999_negative_partition_relations_ordinals/theorem_6_1|Theorem 6.1]]
  (p. 221): the 6- and 4-relations, with Lemmas 3.4, 3.6, 5.14 and 5.15.
- [[set_theory/darby_1999_negative_partition_relations_ordinals/theorem_6_2|Theorem 6.2]]
  (p. 221): $\omega^{\omega^2}\to(\omega^{\omega^2},3)^2$, stated without
  proof.

No file of this source is held: no license on record permits its redistribution,
and the card cites the edition it names above.

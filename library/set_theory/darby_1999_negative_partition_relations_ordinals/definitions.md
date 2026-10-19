---
name: set_theory/darby_1999_negative_partition_relations_ordinals/definitions
title: "Definitions 2.1–3.5 (pp. 207–212): the representation G_α, box and triangle coordinates, and the colorings Δ and Γ"
desc: |
  States Darby's representation of ω^α by finite increasing sequences, his
  level prefixes with box and triangle coordinates, and the pair colorings Δ
  and Γ, whose second colors have no 6-clique and no 4-clique.
created: 2026-10-14T22:55:45Z
updated: 2026-10-14T22:55:45Z
---

***

**Source.** Carl Darby, *Negative partition relations for ordinals
$\omega^{\omega^\alpha}$* (1999): the notation of p. 206, the normal forms and
Definition 2.1 (p. 207), Definitions 2.4 and 2.6 (p. 208), Definition 2.8 and
Lemma 2.9 (p. 209), Definitions 3.1--3.3 and the segment convention (p. 210),
Lemma 3.4 (p. 211), Definition 3.5 and Lemma 3.6 (p. 212). The edition is
identified on the
[[set_theory/darby_1999_negative_partition_relations_ordinals/_index|source card]].
Everything below is restated in the corpus's words.

**Sequences (pp. 206, 208).** $(\omega)^{<\omega}_<$ is the set of finite
strictly increasing sequences of natural numbers, identified with the finite
subsets of $\omega$. For such a sequence $s$, $s_i$ is its $i$th coordinate,
counting from $0$, and $s\restriction i$ its initial segment of length $i$;
$s\preceq g$ says that $s$ is an initial segment of $g$, and $s\prec g$ a
proper one. Sets of sequences carry the lexicographic order, and
$\mathrm{otp}(A)$ is the order type of $A$ in that order. Write $s\ll p$ when
$\max s<\min p$, with $\max\emptyset=-1$ and $\min\emptyset=\omega$; for a set
$G$ of sequences, $G(s)$ is the set of members of $G$ that extend $s$
(Definition 2.4); and for sets $F,E$ of sequences,
$F^\frown E=\{f^\frown e: f\in F,\ e\in E,\ f\ll e\}$ (Definition 2.6).

**Normal forms (p. 207).** A nonzero ordinal is additively indecomposable (AI)
when it is not the sum of two smaller ordinals. Every ordinal has a unique
additive normal form $\alpha=\alpha_0+\cdots+\alpha_k$ with AI terms
$\alpha_0\ge\cdots\ge\alpha_k$, and the paper writes
$\tilde\alpha=\alpha_0+\cdots+\alpha_{k-1}$ and $\alpha'=\alpha_k$, with
$\tilde\alpha=0$ and $\alpha'=\alpha$ when $\alpha$ is AI. An AI ordinal is
multiplicatively indecomposable (MI) when it is not the product of two smaller
ordinals. Every AI ordinal is uniquely a product $\alpha=\alpha_0\cdots\alpha_k$
of MI ordinals $\alpha_0\ge\cdots\ge\alpha_k$, and the paper writes
$\bar\alpha=\alpha_0\cdots\alpha_{k-1}$ and $\hat\alpha=\alpha_k$, with
$\bar\alpha=1$ and $\hat\alpha=\alpha$ when $\alpha$ is MI. MI ordinals have the
form $\omega^\beta$ with $\beta$ AI, and an MI ordinal $\omega^\beta$ is
exponentially indecomposable (EI) when $\beta$ is MI.

**Fundamental sequences (Definition 2.1).** For countable $\alpha>0$ the
sequence $S(\alpha)=\langle S(\alpha)_m:m<\omega\rangle$ is any cofinal
sequence in $\alpha$ if $\alpha$ is EI; $S(\alpha)_m=\omega^{\bar\beta\cdot
S(\hat\beta)_m}$ if $\alpha=\omega^\beta$ is MI but not EI;
$S(\alpha)_m=\bar\alpha\cdot S(\hat\alpha)_m$ if $\alpha$ is AI but not MI;
$S(\alpha)_m=\tilde\alpha+S(\alpha')_m$ if $\alpha$ is a limit but not AI; and
$S(\alpha)_m=\alpha-1$ if $\alpha$ is a successor.

**The representation (Definition 2.8, Lemma 2.9).** Put $G_0=\{\emptyset\}$
and, for countable $\alpha>0$,

$$
G_\alpha=\bigcup_{m<\omega}\{\langle m\rangle\}^\frown G_{S(\alpha)_m}.
$$

Lemma 2.9 states, for every countable $\alpha$: (i)
$\mathrm{otp}(G_\alpha)=\omega^\alpha$; (ii) if $\alpha_0+\cdots+\alpha_k$ is
the additive normal form of $\alpha$, then
$G_\alpha=G_{\alpha_k}{}^\frown\cdots{}^\frown G_{\alpha_0}$; (iii) if
$s\preceq g\in G_\alpha$, then $G_\alpha(s)=\{s\}^\frown G_\beta$ and
$\mathrm{otp}(G_\alpha(s))=\omega^\beta$ for some $\beta\le\alpha$, with
$\beta=\alpha$ exactly when $s=\emptyset$.

**Level prefixes and coordinates (Definitions 3.1--3.2).** Let $\alpha$ be AI
but not MI. A sequence $s$ is a *level prefix* in $G_\alpha$ when
$\mathrm{otp}(G_\alpha(s))=\omega^\gamma$ for some $\gamma$ whose last additive
term is $\gamma'=\bar\alpha$; the paper notes that then
$G_\alpha(s)=\{s\}^\frown G_{\bar\alpha}{}^\frown G_{\tilde\gamma}$. If
$\bar\alpha$ is not MI either, a sequence $t$ is a *sub-level prefix* in
$G_\alpha$ when $t=s^\frown r$ with $s$ a level prefix in $G_\alpha$ and $r$ a
level prefix in $G_{\bar\alpha}$. For $g\in G_\alpha$, the coordinate $g_i$ is
a *box coordinate* of $g$ when it is the last coordinate of $g$ or when
$g\restriction(i+1)$ is a level prefix in $G_\alpha$; when $\bar\alpha$ is not
MI, $g_i$ is a *triangle coordinate* of $g$ when $g\restriction(i+1)$ is a
sub-level prefix in $G_\alpha$.

**Segments (p. 210).** Two disjoint sequences $p$ and $q$ cut each other into
segments $p=p_0{}^\frown\cdots{}^\frown p_k$ and
$q=q_0{}^\frown\cdots{}^\frown q_l$, where $l=k$ or $l=k-1$,
$p_i\ll q_i\ll p_{i+1}$ for $i<k$, and $p_k\ll q_k$ when $l=k$. The two
colorings below are conditions on these segments.

**The coloring $\Delta$ (Definition 3.3).** Let $\alpha$ be AI but not MI. A
pair $\{a,b\}$ of members of $G_\alpha$ belongs to $\Delta_1$ when the two can
be written as $a=A_0{}^\frown A_1{}^\frown A_2{}^\frown A_3$ and
$b=B_0{}^\frown B_1{}^\frown B_2$ so that:

- $A_0\ll B_0\ll A_1\ll B_1\ll A_2\ll B_2\ll A_3$;
- $A_0$ and $A_3$ each contain a box coordinate of $a$, and $A_1$ and $A_2$
  contain none;
- $A_1$ and $A_2$ are nonempty; and
- each of $B_0$, $B_1$ and $B_2$ contains a box coordinate of $b$.

Every other pair belongs to $\Delta_0$. Lemma 3.4: a set of members of
$G_\alpha$ all of whose pairs lie in $\Delta_1$ has at most five members.

**The coloring $\Gamma$ (Definition 3.5).** Let $\alpha$ be AI with
$\bar\alpha$ not MI. A pair $\{a,b\}$ of members of $G_\alpha$ belongs to
$\Gamma_1$ when the two can be written as
$a=A_0{}^\frown A_1{}^\frown A_2{}^\frown A_3{}^\frown A_4$ and
$b=B_0{}^\frown B_1{}^\frown B_2{}^\frown B_3$ so that:

- $A_0\ll B_0\ll A_1\ll B_1\ll A_2\ll B_2\ll A_3\ll B_3\ll A_4$;
- $A_0$ and $A_4$ each contain a box coordinate of $a$, and $A_1$, $A_2$ and
  $A_3$ contain none;
- $A_2$ contains a triangle coordinate of $a$, and $A_1$ and $A_3$ contain
  none;
- $A_1$ and $A_3$ are nonempty; and
- each of $B_0$, $B_1$, $B_2$ and $B_3$ contains a box coordinate of $b$.

Every other pair belongs to $\Gamma_0$. Lemma 3.6: a set of members of
$G_\alpha$ all of whose pairs lie in $\Gamma_1$ has at most three members.

**Source correction.** Definition 3.2 prints "$g\restriction(i=1)=g$" for the
clause that $g_i$ is the last coordinate, $g\restriction(i+1)=g$, and
Definition 3.5 prints "$A_3{}^\frown AA_4$" for $A_3{}^\frown A_4$. These are
filing observations, not an author erratum.

**Comparison with Schipperus's patterns.** Record each segment of $a$ by the
deepest kind of coordinate the definition requires it to hold: 3 for a box
coordinate, 2 for a triangle coordinate without a box coordinate, 1 for
neither, with every segment of $b$ at the top level. A $\Gamma_1$ pair then has
the word $A_3,B_3,A_1,B_3,A_2,B_3,A_1,B_3,A_3$, the word recorded for
Schipperus's Theorem 32 (three summands, against a four-clique) on
[[set_theory/schipperus_2010_countable_partition_ordinals/theorem_29|his Theorem 29 page]].
A $\Delta_1$ pair, in two levels, has the word $A_2,B_2,A_1,B_2,A_1,B_2,A_2$,
with one interior $A_1$ segment fewer than the word recorded there for his
Theorem 31. This compares words only: whether Darby's box and triangle
coordinates agree with Schipperus's levels of a cut piece is not examined here.

**Read depth.** Claims checked: the definitions, Lemma 2.9 and the statements
of Lemmas 3.4 and 3.6 were read clause by clause on the page images
(pp. 206--212). The proofs of Lemmas 2.9, 3.4 and 3.6 were looked through and
not checked. Nothing here is independently reviewed.

**Dependencies.** None outside the paper. The colorings are used in
[[set_theory/darby_1999_negative_partition_relations_ordinals/theorem_6_1|Theorem 6.1]].

**Bears on.** [[../wiki/problems/set_theory/E0592/_index|#592]]: $\Gamma$ is a
published coloring of $[G_\alpha]^2$ witnessing
$\omega^{\omega^\gamma}\not\to(\omega^{\omega^\gamma},4)^2$ when $\gamma$ is a
sum of three or more indecomposables, the problem's undecided case among them,
with the kind of each cut segment defined through box and triangle coordinates.
The [[../wiki/research/erdos_592/pattern_level_obstruction|pattern-level note]]
asks for such a source definition to calibrate the negative patterns against.

---
name: research/erdos_1219/evidence/verify/connections_hajnal_s_conjecture_1a_triples_review
title: "Independent review of the connections section: Hajnal's Conjecture 1A: triples"
desc: |
  Refutation review of the section "Hajnal's Conjecture 1A: triples" and the
  lead it files. The endgame lemma, the (P1) transfer, the (P2) reduction and
  the (P3) counting obstruction survive; the restatement of (P3) as the
  constancy of one pair coloring is refuted-as-stated, leaving the conditional
  "positive outcome proves the conjecture" without its bridge; a parenthetical
  reason under (P2) is refuted-as-stated with its conclusion intact. One
  required correction, two suggested, five notes.
created: 2026-09-28T19:10:08Z
updated: 2026-09-28T20:42:32Z
---

***

## Subject and independence

**Role.** Independent reviewer working in a fresh context from the
assignment alone; took no part in writing the reviewed section, the lead,
the Tools section or the reconstruction pages. Charge: refutation.

**Subject.** The page `wiki/research/erdos_1219/connections.md` as it stood at
2026-09-28T13:50:48Z, section `## Hajnal's Conjecture 1A: triples`, lines
286--445 (the H2 at line 286 to the line before the H2 `## Problem 1218` at line
446), and the lead page
`wiki/research/leads/triple_canonization_for_hajnal_conjecture/_index.md`
(151 lines, whole page), both as of that time.

**Reading.** The section and the lead in full, every sentence. The page's
Scope paragraph (lines 19--37) and its Tools section (lines 39--108) as
inputs: the interface (T1) was confirmed at each use (hypotheses on
$\kappa$, $\mu(i)$, $\lambda_i$, $A_i$, the arity of $F$, the conclusions
(1A), (1B), (2)); (T2) and (T3) are not used by the section and were not
checked. The three reconstruction pages
`wiki/research/erdos_1219/lemma_1_1_reconstruction.md`,
`wiki/research/erdos_1219/theorem_1_2_reconstruction.md` and
`wiki/research/erdos_1219/corollary_1_3_reconstruction.md` in full, as
premises at their standing; the section's uses of clauses (1A), (1B), (2),
of the argument for clause (3), of the proof-internal first thinning, and
of Steps 1, 2, 5 and 7 of the theorem page were checked against their
stated hypotheses. The statement paragraph of
`wiki/problems/set_theory/E1219/_index.md` (lines 17--23; the page has no
Statement heading; its Current assessment, Progress and Known Results
sections were not read). The result page
`library/set_theory/shelah_1975_notes_partition_calculus/conjecture_1a.md`
and the provenance and read-status paragraphs of the Shelah library card.
The held Shelah scan, PDF pp. 2--5 (printed pp. 1258--1261), on page images
rendered at 130 dpi: the statement of Lemma 1.1 with its Remark, the proof
on pp. 1259--1260, Theorem 1.2 with its proof, Corollary 1.3 with its
Remark, and Conjecture 1A with its Remark. The held Komjáth survey, PDF
pp. 2--3 (printed pp. 419--420), text layer: Problems 3, 4 and 5 with their
commentary. The wiki pages named in the assignment.

**Exposures.** None to excluded content. A directory listing made to
locate the target path showed the file names of other records under
`wiki/research/erdos_1219/evidence/verify/`; none was opened. A working
tree status listing showed the names of untracked review files in a
sibling research folder; none was opened.

## Restatement

Throughout, H is the hypothesis
$\aleph_\omega<2^{\aleph_{n(0)}}<2^{\aleph_{n(1)}}<\cdots$ for a sequence
$(n(k))_{k<\omega}$ of natural numbers, $\chi=\sum_{n<\omega}2^{\aleph_n}$,
and a coloring is a map $f:[\chi]^3\to\{0,1\}$. The blocks are those of the
theorem page at $\lambda=\aleph_\omega$, $\kappa=\omega$: cardinals
$\mu(i)<\aleph_\omega$ ($i<\omega$), strictly increasing and cofinal in
$\aleph_\omega$, each above $\aleph_{n(0)}$, with $2^{\mu(i)}$ strictly
increasing and $2^{\mu(i)}>\aleph_\omega$; $\lambda_i=(2^{\mu(i)})^+$; and
a partition $\chi=\bigsqcup_{i<\omega}A_i$ with $|A_i|=\lambda_i$. The
pattern of a triple meeting the blocks $i\le j\le k$ is $(i,j,k)$. For a
family of sets $B_i\subseteq A_i$, $E_j=\bigcup_{i<j}B_i$.

- **S1 (target; not a claim).** Conjecture 1A: under H, every coloring
  $f$ has $X\subseteq\chi$ with $|X|=\aleph_\omega$ and $f\equiv0$ on
  $[X]^3$, or $Q\subseteq\chi$ with $|Q|=4$ and $f\equiv1$ on $[Q]^3$. The
  section attributes to the Remark on printed p. 1261 the unproved
  assertion $\chi\not\to(\aleph_\omega,5)^3$ and to the survey, p. 419,
  the record that the conjecture is unproven.
- **S2 (the canonization statement; a definition).** A coloring $f$
  satisfies (C) when there are $S_i,T_i\subseteq A_i$ ($i<\omega$) with
  $|S_i|=\mu(i)$, $f\equiv0$ on $[S_i]^3$, $T_i$ a three-element set with
  $f(T_i)=1$, such that with $B_i=S_i\cup T_i$: (P1) for all $i<j<k$ the
  value $f(\{a,b,c\})$ is the same for all $a\in S_i$, $b\in S_j$,
  $c\in S_k$; (P2) for all $i<j$ the value $f(\{a,a',b\})$ is the same for
  all $\{a,a'\}\in[B_i]^2$ and $b\in B_j$; (P3) for all $i<j$ the value
  $f(\{a,b,b'\})$ is the same for all $a\in B_i$ and $\{b,b'\}\in[B_j]^2$.
- **S3 (endgame lemma).** Under H, with the blocks fixed: if every
  coloring $f$ satisfying (i) no four-element $Q$ has $f\equiv1$ on
  $[Q]^3$, and (ii) no $i<\omega$ and no $X\subseteq A_i$ with
  $|X|=\aleph_\omega$ has $f\equiv0$ on $[X]^3$, satisfies (C), then
  Conjecture 1A holds. Imported: $\omega\to(\omega)^3_2$ and
  $\omega\to(\omega)^2_2$.
- **S4 (remark on the triples $T_i$).** Let $f_0$ give color $1$ exactly
  to the triples of pattern $(i,i,j)$ with $i<j$. Then (a) $f_0$ has no
  four-element set homogeneous in color $1$; (b) every set of size
  $\aleph_\omega$ homogeneous in color $0$ lies, up to finitely many
  points, inside one block; (c) $f_0$ "shows that the case $\eta_2=1$,
  $\varepsilon=0$ cannot be handled without the $T_i$".
- **S5 (application of the lemma).** Let $\tilde f:A^3\to2$ be the
  symmetric extension of $f$, $0$ on tuples with a repeated entry, and
  let $P_i(\langle B_l:l\le i\rangle,\langle a_j:i<j<\omega\rangle)$ hold
  when $B_i=S\cup T$ with $|S|=\mu(i)$, $f\equiv0$ on $[S]^3$ and $T$ a
  triple of color $1$ (the section adds "together with whatever (P2)
  turns out to need"). For a coloring with (i) and (ii), and given the
  imported relation $(2^\mu)^+\to(\mu^+,4)^3$ for infinite $\mu$, the
  realizability hypothesis (H) holds for these $P_i$, so (T1) applies and
  Lemma 1.1 yields $a^*_i\in A_i$ and $B_i\subseteq A_i$ with (1A), (1B)
  and (2).
- **S6 (P1).** For $i<j<k$, $a\in B_i$, $b,b'\in B_j$, $c,c'\in B_k$:
  $f(\{a,b,c\})=f(\{a,b',c'\})$. The map sending $a\in S_i$ to the
  sequence $\langle f(\{a,b,c\}):i<j<k\rangle$ has at most $2^{\aleph_0}$
  values; when $2^{\aleph_0}<\mu(i)$ for every $i$, replacing each $S_i$
  by a fiber of size $\mu(i)$ and keeping $T_i$ gives (P1) while (1A),
  (1B) and (2) survive; $2^{\aleph_0}<\mu(i)$ for every $i$ can be
  arranged through the choice of $\mu_0$ in Step 1 exactly when
  $2^{\aleph_0}<\aleph_\omega$, and when $2^{\aleph_0}>\aleph_\omega$ the
  fiber argument fails.
- **S7 (P2, first half).** For $i<j$, $\{a,a'\}\in[B_i]^2$ and $b\in B_j$:
  $f(\{a,a',b\})=f(\{a,a',a^*_j\})$. Hence (P2) holds if and only if, for
  every $i$, the coloring
  $c_i(\{a,a'\})=\langle f(\{a,a',a^*_j\}):j>i\rangle$ of $[B_i]^2$, with
  at most $2^{\aleph_0}$ colors, is constant; the lemma's thinnings do not
  provide this, so it must be a conjunct of $P_i$, realized inside every
  $C\subseteq A_i$ with $|C|=\lambda_i$.
- **S8 (P2, the Erdős--Rado discussion).** When $2^{\aleph_0}\le\mu(i)$,
  the imported relation $(2^\mu)^+\to(\mu^+)^2_\mu$ gives $C'\subseteq C$
  with $|C'|=\mu(i)^+$ on which $c_i$ is constant; (S8a) inside $C'$ the
  relation $(2^\mu)^+\to(\mu^+,4)^3$ "cannot be applied again ($|C'|$ is
  not of that form)"; (S8b) a triple of color $1$ inside $C'$ is not
  guaranteed; a $c_i$-homogeneous set of size $\lambda_i$ cannot be asked
  because $\lambda_i$ is a successor cardinal; so the route needs the
  block statement (BS2): in every $C\subseteq A_i$ of size $\lambda_i$,
  for every coloring of $[C]^2$ with at most $2^{\aleph_0}$ colors, there
  is $S\cup T$ as in (C) on which that coloring is constant, or $f$ has a
  four-element set of color $1$; (BS2) is left open.
- **S9 (P3, what the lemma gives).** (S9a) No clause of Lemma 1.1
  relates $f(\{a,b,b'\})$, with $\{b,b'\}\subseteq B_j$ and $a\in E_j$, to
  any other value. (S9b) "(P3) says that
  $d_j(\{b,b'\})=\langle f(\{a,b,b'\}):a\in E_j\rangle$, a coloring of
  $[B_j]^2$ with at most $2^{|E_j|}=2^{\mu(j-1)}$ colors, is constant."
- **S10 (P3, the counting obstruction).** For $j\ge1$,
  $2^{\mu(j-1)}\ge2^{\aleph_{n(0)}}>\aleph_\omega>\mu(j)$; the
  Erdős--Rado relation at the block size $\lambda_j$ would need
  $2^{\mu(j)}\ge2^{2^{\mu(j-1)}}$; when $2^{\mu(j)}<2^{2^{\mu(j-1)}}$
  there is a coloring of $[\lambda_j]^2$ with $2^{\mu(j-1)}$ colors and no
  homogeneous triple; choosing smaller earlier blocks does not remove the
  obstruction, because the $\mu(i)$ are cofinal in $\aleph_\omega$; whether
  the particular $d_j$ induced by an $f$ with (i) admits a homogeneous
  $S_j\cup T_j$ is the open gap.
- **S11 (falsification checks).** The endgame uses only the values on the
  $B_i$ and the two Ramsey theorems; its cases are exhaustive; the block
  sizes are those of Theorem 1.2, so (T1) applies; the Remark after
  Lemma 1.1 was not read; the three-color form of Theorem 1.2 gives
  nothing for the triple relation.
- **S12 (conditional deductions of the next investigation).** (S12a) If
  every $f$ with (i) and (ii) forces, in every full-size subset of $A_j$,
  a set $S_j\cup T_j$ on which $d_j$ is constant, then, with (BS2), the
  conjecture holds under $2^{\aleph_0}<\aleph_\omega$ by the endgame
  lemma. (S12b) A coloring $f$ defeating (P3) in every choice of
  $S_j\cup T_j$ "shows that a proof of the conjecture cannot pass through
  canonization over the lower blocks"; the lead: "shows that no proof
  passes through canonization over the lower blocks".
- **S13 (outcome sentence).** The endgame lemma reduces the conjecture to
  (C); the lemma supplies (P1) under $2^{\aleph_0}<\aleph_\omega$ and half
  of (P2), and nothing of (P3).

The lead page restates S1 (Target and status evidence), S2 and S3 (Route
and established inputs), S6, S7 and S9a (What the lemma supplies), the
imported inputs (Provisional premises), S9b and S10 (The consequential
gap), and S12 with the removal of $2^{\aleph_0}<\aleph_\omega$ as a later
step (Next step). Its frontmatter marks the lead a candidate, unreviewed,
and its closing sentence disclaims any status change.

## Checklist

- **Quantifiers and scope.** Defect found. S9b drops the quantifier over
  $a\in B_i$: (P3) demands constancy in the pair $\{b,b'\}$ and constancy
  in $a$ within each lower block, while the constancy of $d_j$ gives only
  the first (F1). (C) asks (P3) for $a\in B_i\supseteq T_i$, although only
  $a\in S_i$ is used by the endgame and only that much is deliverable by
  thinning (F1). S12b's "no proof passes" is a universal statement about
  proofs that the negative outcome does not support (F2). The (P3)
  question also depends on the admissible lower sequence through $E_j$,
  which the wording "induced by an $f$" hides (F7). The endgame lemma's
  quantifiers are correct.
- **Circularity.** None. (C) is a structural sufficient condition; the
  endgame lemma proves the implication from (C) to the target without
  using the target, and nothing in the section derives (C) from the
  conjecture.
- **Model and convention changes.** Pass. The passage from $f$ on
  $[\chi]^3$ to the symmetric $\tilde f$ on $A^3$ and the identification of
  $\chi$ with the union of the blocks are proved transfers (Step 2(c),
  (d) of the theorem page); the pattern convention is used consistently;
  the reading of $2^{\chi+\kappa}<\operatorname{cf}\mu(i)$ as
  $2^{\aleph_0}<\mu(i)$ is correct because every $\mu(i)$ is an
  $\aleph_m$ with $m<\omega$, hence regular.
- **Finite and statistical overreach.** Pass; nothing finite or
  statistical is used.
- **Uniformity.** Pass. The bound $2^{\aleph_0}$ on the fiber maps in S6
  and S7 does not depend on $i$; the requirement $2^{\aleph_0}<\mu(i)$ is
  stated for every $i$ and met by one choice of $\mu_0$; the color count
  $2^{\mu(j-1)}$ in S10 depends on $j$ as stated, and the obstruction is
  argued for every $j\ge1$.
- **Extremal conclusions.** Inapplicable; no infimum, supremum or
  sharpness claim is made.
- **Consequences and composition.** Defects found. S12a claims a
  conclusion whose bridge from the constancy of $d_j$ to (P3) is missing
  (F1). S8a gives a false reason for a true consequence (F3). S13's "the
  lemma supplies (P1)" also consumes the imported triple relation through
  (H), which the Outcome sentence does not carry (F8). Every other
  "hence" was checked separately and follows.
- **Computation.** Inapplicable; no computation is used or claimed.
- **Reproduction.** Inapplicable; no rerun instruction or coverage claim
  is made.
- **Source and verdict fidelity.** Pass with two unverifiable items. The
  Remark on printed p. 1261, the survey's record on p. 419, the note
  $2^\kappa\not\to(3)^2_\kappa$ under Problem 5 on p. 420, and the Remark
  after Lemma 1.1 on p. 1258 read on the held pages as the section
  reports them. The attribution of $(2^\mu)^+\to(\mu^+,4)^3$ to Erdős,
  Hajnal and Rado (1965) cannot be checked in the read set, and the pages
  say so ("not held"). The sentences citing a search "recorded on the
  problem page (2026-09-27)" and an "assessment dated 2026-09-27" refer
  to excluded text and were not checked. The standing sentences
  (author-recorded, unreviewed, no status change, no tier) claim nothing
  beyond author-recorded.

## Weakest steps

**W1: the reduction of (P3) to the constancy of $d_j$ (S9b), and the
bridge in S12a.** Fix $i<j$. (P3) at $(i,j)$ says: there is
$h_1(i,j)\in\{0,1\}$ with $f(\{a,b,b'\})=h_1(i,j)$ for all $a\in B_i$ and
all $\{b,b'\}\in[B_j]^2$. Write $v_{b,b'}:E_j\to2$ for
$a\mapsto f(\{a,b,b'\})$, so $d_j(\{b,b'\})=v_{b,b'}$. Then (P3) for all
$i<j$ is the conjunction of (P3a) $d_j$ is constant on $[B_j]^2$, with
common value $v_j$, and (P3b) $v_j$ is constant on each $B_i$, $i<j$.
Constancy of $d_j$ is (P3a) alone. (P3a) does not imply (P3b): if
$\varphi:\chi\to2$ takes both values on some $B_i$ and $f(\{a,b,b'\})$ is
$\varphi(a)$ on every triple of pattern $(i,j,j)$, $i<j$, whatever $f$ does
elsewhere, then $d_j(\{b,b'\})=\varphi\restriction E_j$ for every pair,
so $d_j$ is constant for every choice of $B_j$, while (P3) fails at
$(i,j)$. Now compose with the lemma. Neither (P3a) nor (P3b) is provided
by any clause of Lemma 1.1 (S9a is correct, and (P3b) is equally
uncovered: the lemma canonizes an element of $B_i$ against one point
$a^*_j$ of each higher block, never against a pair). If (P3a) is
obtained, as S12a supposes, (P3b) for $a\in S_i$ follows by an extra
fiber step: the map $a\mapsto\langle v_j(a):j>i\rangle$ on $S_i$ has at
most $2^{\aleph_0}$ values, so under $2^{\aleph_0}<\mu(i)$ a fiber of size
$\mu(i)$ exists, and it may be taken jointly with the (P1) fiber of S6.
(P3b) for $a\in T_i$ cannot be obtained by thinning: $T_i$ is three fixed
points chosen at stage $i$, before any $B_j$ with $j>i$ exists, from
information that contains one point of each higher block and therefore
cannot see any pair in $B_j$. The endgame lemma uses (P3) only for
$a\in S_i$: in the case $\eta_1=1$ the single lower point may be taken in
$S_i$, and the final case uses the $S_i$ alone. So (C) with (P3)
restricted to $a\in S_i$ still supports the endgame, and S12a holds for
that restricted (C) after the extra fiber step, under the hypothesis
$2^{\aleph_0}<\aleph_\omega$ it already carries. As written, with (P3)
over $B_i$ and with the bridge absent, S12a does not follow.

**W2: the (P1) transfer through the argument of clause (3) (S6).** By
(1B) at the blocks $(j,k)$ with the one-element sequence $(a)$ from
$B_i$, $i<j$: $\tilde f(b,c,a)=\tilde f(b',c',a)$ for $b,b'\in B_j$,
$c,c'\in B_k$, which is the joint independence of $f(\{a,b,c\})$ from $b$
and $c$. The residual map $H_i$ on $S_i$ is indexed by the countably many
pairs $(j,k)$ with $i<j<k<\omega$ and takes values in $2$, so it has at
most $2^{\aleph_0}$ values. Since $\mu(i)=\aleph_m$ for some $m<\omega$,
$\mu(i)$ is regular, and if $2^{\aleph_0}<\mu(i)$ then $S_i$, a union of
at most $2^{\aleph_0}<\operatorname{cf}\mu(i)$ fibers, has a fiber of size
$\mu(i)$; call it $S'_i$ and put $B'_i=S'_i\cup T_i$. (1A) and (1B) are
universal over the $B_i$ and survive; $P_i$ holds for $B'_i$ because it
depends on $B_i$ alone and $S'_i\cup T_i$ has the required shape; the
value $H_i(a)$ was independent of the choice of $b\in B_j$, $c\in B_k$, so
it is unchanged on $B'_j$, $B'_k$; hence (P1) holds on the $S'_i$. The
condition $2^{\aleph_0}<\mu(i)$ for all $i$ is arranged by taking $\mu_0$
above $2^{\aleph_0}$ in Step 1 when $2^{\aleph_0}<\aleph_\omega$; when
$2^{\aleph_0}>\aleph_\omega$ no $\mu(i)<\aleph_\omega$ exceeds
$2^{\aleph_0}$; $2^{\aleph_0}=\aleph_\omega$ is excluded by the
cofinality of $2^{\aleph_0}$ being uncountable, so "exactly when" is
right. The step does not invoke clause (3) as stated, whose heredity
hypothesis the property fails (dropping a point of $T$ from a same-size
subset destroys the color-$1$ triple); it reuses the reconstruction's
fiber argument with the thinning confined to $S_i$, which is sound (F4).

**W3: the endgame lemma (S3).** Let $f$ satisfy (i) and (ii) and (C).
Ramsey for triples on $g:[\omega]^3\to2$ gives an infinite $I$ with
constant value $\varepsilon$; Ramsey for pairs, twice, gives an infinite
$I'\subseteq I$ with $h_1\equiv\eta_1$ and $h_2\equiv\eta_2$ on $[I']^2$.
If $\varepsilon=1$: four indices of $I'$ and one point of each $S$ give a
four-element set all of whose triples have three distinct block indices
in $I'\subseteq I$, hence color $1$. If $\eta_2=1$: for $i<j$ in $I'$,
$T_i\cup\{b\}$ with $b\in B_j$ has the triple $T_i$ of color $1$ and three
triples with two points in $T_i\subseteq B_i$ and one in $B_j$, of color
$h_2(i,j)=1$ by (P2) as quantified over $[B_i]^2$. If $\eta_1=1$: one
point $a\in B_i$ and $T_j$ give $T_j$ of color $1$ and three triples with
one point in $B_i$ and a pair from $T_j\subseteq B_j$, of color
$h_1(i,j)=1$ by (P3). Otherwise $\varepsilon=\eta_1=\eta_2=0$ and
$X=\bigcup_{i\in I'}S_i$ is homogeneous in color $0$: a triple inside one
$S_i$ has color $0$ by the choice of $S_i$, and a triple across blocks has
pattern $(i,i,j)$, $(i,j,j)$ or $(i,j,k)$ with $i<j<k$ in $I'$ and color
$\eta_2$, $\eta_1$ or $\varepsilon$. The $S_i$ are disjoint and $I'$ is
unbounded in $\omega$, so $|X|=\sum_{i\in I'}\mu(i)=\aleph_\omega$. The
case split is exhaustive, and colorings without (i) or (ii) satisfy the
conjecture directly. The lemma is correct. Its proof needs (P2) only for
$b\in S_j$ and (P3) only for $a\in S_i$, which is what W1 uses.

## Strongest attack

- **S3.** Attempted: making the four-element sets degenerate by letting
  $T_i$ meet $S_i$ (irrelevant, as the blocks are disjoint and the sets
  used have four points in two or four blocks); using (P2) or (P3) at
  pairs from $T$ (available, since (C) quantifies over $[B_i]^2$ and
  $[B_j]^2$); making $|X|<\aleph_\omega$ (impossible, $I'$ is infinite and
  the $\mu(i)$ are cofinal); finding the conjecture inside the hypothesis
  (it is not: (C) is a statement about sets in blocks, and a counterexample
  to the conjecture with (i) and (ii) would simply fail (C)). All failed.
- **S4.** (a) and (b) were re-derived: a four-element set homogeneous in
  color $1$ would need every triple to have exactly two points in its
  lowest block, which no distribution of four points over blocks achieves;
  a set homogeneous in color $0$ with two points in a block $i$ has no
  point above block $i$ and at most one point in each block below it. For
  (c), the attack is that $f_0$ violates hypothesis (ii) (each block is
  homogeneous in color $0$), so it lies outside the endgame lemma and
  defeats no implication the section states; what it shows is that the
  canonical values on the $S_i$ alone are compatible with both outcomes
  in the case $\eta_2=1$, $\varepsilon=0$. As a statement about the proof
  mechanism, (c) survives (F5).
- **S5.** Attempted: breaking (H). Inside every $C\subseteq A_\alpha$ with
  $|C|=\lambda_\alpha=(2^{\mu(\alpha)})^+$, the imported relation with
  $\mu=\mu(\alpha)$ and (i) give a set of size $\mu(\alpha)^+$ homogeneous
  in color $0$, which contains one of size $\mu(\alpha)$; (ii) gives a
  triple of color $1$ because $|C|>\aleph_\omega$; the union has size
  $\mu(\alpha)$. The lemma's remaining hypotheses are those (T1) verifies.
  The types over a set include patterns with repeated entries, on which
  $\tilde f$ is $0$; harmless. Failed, conditionally on the imported
  relation.
- **S6.** See W2. Attempted: an uncountable index set for $H_i$ (no, the
  pairs $(j,k)$ are countable); a singular $\mu(i)$ (no, below
  $\aleph_\omega$ every infinite cardinal is regular); loss of (2) under
  thinning (no, $P_i$ depends on $B_i$ alone). Failed.
- **S7.** Attempted: the link between $b\in B_j$ and $a^*_j$ is not among
  the lemma's conclusions (1A), (1B), (2); (1B) relates one point of $B_i$
  to $a^*_j$, not a pair. The section names the proof-internal first
  thinning of the lemma page, which gives $b$ and $a^*_j$ the same type
  over $E_j$ and hence $\tilde f(b,a,a')=\tilde f(a^*_j,a,a')$; the
  reconstruction states this as its labeled fact (T1). The "if and only
  if" then holds, and the count of colors is $2^{\aleph_0}$. Failed (F6).
- **S8a.** Refuted-as-stated. Under $2^{\aleph_0}=\aleph_2$, $n(0)=1$ and
  $2^{\aleph_2}>2^{\aleph_1}$, Step 1 gives $\mu(0)=\aleph_2$, the
  hypothesis $2^{\aleph_0}\le\mu(0)$ of the sentence holds, and
  $|C'|=\aleph_3=(2^{\aleph_0})^+$ is of the form $(2^\nu)^+$ with
  $\nu=\aleph_0$, so the relation applies again. The consequence survives
  for a different reason: whenever $\mu(i)=2^\nu$, then
  $\nu<\aleph_{n(0)}<\mu(i)$ (otherwise $2^\nu>\aleph_\omega$), so the
  relation yields a set of color $0$ of size $\nu^+<\mu(i)$, and S8b
  already defeats the approach.
- **S8b.** Attempted: a triple of color $1$ inside $C'$ is guaranteed by
  (ii) only for sets of size at least $\aleph_\omega$, and
  $\mu(i)^+<\aleph_\omega$; a homogeneous set of size $\lambda_i$ for a
  two-valued coloring of $[\lambda_i]^2$ is refuted by the Sierpiński
  coloring restricted from $2^{2^{\mu(i)}}\ge\lambda_i$, as $\lambda_i$ is
  a successor. Failed.
- **S9a.** Attempted: each of (1A), (1B), (3) was checked for a tuple with
  two entries from one block and one from a lower block; none covers it.
  The proof-internal second thinning relates $f(\{a,b,a^*_j\})$ to
  $f(\{a,b',a^*_j\})$ for $b,b'\in B_j$, a single pair type, not
  $[B_j]^2$. Failed.
- **S9b.** Refuted-as-stated; witness in W1.
- **S10.** Re-derived: $|E_j|=\sum_{i<j}\mu(i)=\mu(j-1)$ for $j\ge1$
  since each $|B_i|=\mu(i)$; the Erdős--Rado relation
  $(2^\theta)^+\to(\theta^+)^2_\theta$ with $\theta=2^{\mu(j-1)}$ needs
  $\lambda_j\ge(2^\theta)^+$, that is $2^{\mu(j)}\ge2^{2^{\mu(j-1)}}$;
  otherwise $\lambda_j\le2^\theta$, and the coloring of $[{}^\theta2]^2$
  by the least coordinate where two functions differ has no homogeneous
  triple (three functions cannot be pairwise distinct at one coordinate
  with two values), which is $2^\theta\not\to(3)^2_\theta$ restricted to
  $\lambda_j$ points; a block $i$ with $\mu(i)\ge\aleph_{n(0)}$ has
  $2^{\mu(i)}>\aleph_\omega$, and all but finitely many blocks are such.
  Attempted: the bound $2^{\mu(j-1)}$ is an upper bound on the colors of
  $d_j$, which the section already concedes by leaving the induced $d_j$
  open. Failed.
- **S11.** Re-derived with W3 and (T1). Failed.
- **S12a.** Proof defective; statement unresolved; see W1 and F1.
- **S12b.** Proof defective; statement unresolved; a negative outcome refutes
  (H) for the property that carries (P3), hence (C) as the route's sufficient
  condition for that $f$ and those blocks. It does not exclude a proof through a
  different canonical form (constancy on the $S_i$ after thinning, constancy up
  to a small exceptional set, a different block decomposition or a different
  parameter set), so the universal "no proof passes through canonization over
  the lower blocks" is unsupported (F2).
- **S13.** Attempted: "supplies (P1)" without its imported input; the
  Outcome sentence carries only $2^{\aleph_0}<\aleph_\omega$, while the
  realizability (H) behind (P1) also consumes $(2^\mu)^+\to(\mu^+,4)^3$,
  which the section's next-investigation paragraph and the lead's
  provisional premises do carry. Survives as author-recorded with that
  qualification (F8).

## Premises

- **(T1), Tools section of the connections page, lines 46--61.**
  Interface: $\kappa$ infinite regular; $\mu(i)$ infinite, strictly
  increasing, $\mu(0)\ge\kappa$, $2^{\mu(i)}$ strictly increasing;
  $\lambda_i=(2^{\mu(i)})^+$; $A_i$ pairwise disjoint of size $\lambda_i$;
  $F:A^n\to2$ of finitely many places; then Lemma 1.1 applies with
  $\chi=2$, $F_0=F_1=F$ and any $P_\alpha$ satisfying (H), yielding
  (1A), (1B), (2) with $|B_i|\le\mu(i)$. Its proof (Steps 2(a) and 5 of
  the theorem page) is another reviewer's subject; here confirmed:
  $\kappa=\omega$, $\mu(0)>\aleph_{n(0)}\ge\aleph_0$, $n=3$, the blocks of
  Step 2.
- **Lemma 1.1 reconstruction** (premise at its standing). Used: clauses
  (1A), (1B), (2) as stated on its Statement section; the labeled
  proof-internal fact (T1) (first thinning: every $b\in B_\alpha$ has the
  type of $a^*_\alpha$ over $E_\alpha$); the fiber argument of its Clause
  (3) section with its reading of the hypotheses. Read in full.
- **Theorem 1.2 reconstruction** (premise at its standing). Used: Step 1
  (the $\mu(i)$, with $\mu(i)>\rho_i\ge\mu_0$ and $\mu(i)\ge\kappa$),
  Step 2 (the blocks and $\chi=\bigsqcup A_i$), Step 5 (the hypotheses of
  the lemma), Step 7 (the size of a union of the $S_i$ over an unbounded
  index set). Read in full.
- **Corollary 1.3 reconstruction** (premise at its standing). Used: the
  hypotheses of Theorem 1.2 at $\lambda=\aleph_\omega$ under H, with
  $\mu_0=\aleph_{n(0)}$, and $\chi=\sum_{n<\omega}2^{\aleph_n}$. Read in
  full.
- **Conjecture 1A result page**
  ([[../library/set_theory/shelah_1975_notes_partition_calculus/conjecture_1a|conjecture_1a]]).
  Statement and Remark as recorded; matches the held page image, printed
  p. 1261.
- **Shelah (1975)**, held scan
  ([[../library/set_theory/shelah_1975_notes_partition_calculus/_index|library card]]),
  PDF pp. 2--5 on page images. Lemma 1.1 with its Remark (p. 1258), the
  proof (pp. 1259--1260) including the one-sentence treatment of (3),
  Theorem 1.2, Corollary 1.3 and its Remark (p. 1260), Conjecture 1A and
  its Remark (p. 1261). Read at statement depth for the statements the
  section cites; the proofs were read to confirm the reconstruction's
  labels, not re-verified.
- **Komjáth (2025)**, held PDF
  ([[../library/set_theory/komjath_2025_erdos_hajnal_problem_list/_index|library card]]),
  printed pp. 419--420 in the text layer: Problem 3 with the record of
  Hajnal's conjecture as unproven; Problem 5 with
  "$2^\kappa\not\to(3)^2_\kappa$ holds in general".
- **Imported, not held.** Ramsey's theorem $\omega\to(\omega)^3_2$ and
  $\omega\to(\omega)^2_2$ (standard; used in S3). Erdős--Rado
  $(2^\mu)^+\to(\mu^+)^2_\mu$ for infinite $\mu$ (standard; used in S8 and
  S10 as a known relation). The unbalanced triple relation
  $(2^\mu)^+\to(\mu^+,4)^3$ for infinite $\mu$ (used in S5; its
  attribution to Erdős, Hajnal and Rado 1965 is not checkable here and is
  flagged on both pages as to be located; the Remark on p. 1261, which
  asserts that every previously known case of $\lambda\to(\mu,\mu)^2$ also
  gives $\lambda\to(\mu,4)^3$, is consistent with it but proves nothing).
  $2^\theta\not\to(3)^2_\theta$ (held in the survey and re-derived above).
- **Explicit assumptions of the route.** H; the blocks of Step 2;
  $2^{\aleph_0}<\aleph_\omega$ for S6 and the Erdős--Rado step of S8; the
  block statement (BS2); the (P3) question. No batch acceptance order
  applies.

## Findings

- **F1 (required). Location:** connections page, (P3) bullet, "(P3) says
  that $d_j(\{b,b'\})=\langle f(\{a,b,b'\}):a\in E_j\rangle$, a coloring
  of $[B_j]^2$ with at most $2^{|E_j|}=2^{\mu(j-1)}$ colors, is
  constant."; Next investigation, "A positive outcome, with the block
  statement for (P2), proves the conjecture under
  $2^{\aleph_0}<\aleph_\omega$ by the endgame lemma."; lead page, The
  consequential gap and Next step 1, "admits in every full-size subset of
  $A_j$ a set $S_j\cup T_j$ on which the induced pair coloring is
  constant. A positive outcome, with the block statement behind (P2),
  proves the conjecture under $2^{\aleph_0}<\aleph_\omega$ by the endgame
  lemma." **Defect:** (P3) is the conjunction of the constancy of $d_j$ on
  $[B_j]^2$ and the constancy of its value on each lower $B_i$; the
  sentence keeps only the first, and the conditional conclusion has no
  bridge for the second. **Witness:** the coloring of W1 with
  $f(\{a,b,b'\})=\varphi(a)$ on every triple of pattern $(i,j,j)$,
  $\varphi$ not constant on $B_i$: $d_j$ is constant for every $B_j$ and
  (P3) fails. **Replacement:** state (P3) in (C) for $a\in S_i$ (the
  endgame lemma uses it only there), and record that a positive outcome
  gives (P3) so restricted only after thinning each $S_i$ to a fiber of
  $a\mapsto\langle v_j(a):j>i\rangle$, at most $2^{\aleph_0}$ values, which
  has size $\mu(i)$ under $2^{\aleph_0}<\mu(i)$ and is taken jointly with
  the (P1) fiber; or else pose the (P3) question with the value of $d_j$
  required to be constant on each lower $B_i$, which is (P3) itself as a
  block statement. Either way, say which.
- **F2 (suggested). Location:** connections page, Next investigation, "a
  negative outcome, a coloring $f$ defeating (P3) in every choice of
  $S_j\cup T_j$, shows that a proof of the conjecture cannot pass through
  canonization over the lower blocks"; lead page, Next step 1, "A negative
  outcome shows that no proof passes through canonization over the lower
  blocks". **Defect:** the negative outcome refutes the realizability of
  the property carrying (P3), hence (C) for that $f$ and those blocks; it
  says nothing about other canonical forms, decompositions or parameter
  sets. **Witness:** none needed; the claim is a universal statement about
  proofs with no argument. **Replacement:** "shows that (C) fails for
  this $f$ on these blocks, so the route as formulated is closed; whether
  a weaker canonical form or another decomposition serves is not
  decided".
- **F3 (suggested). Location:** connections page, (P2) bullet, "inside
  which the relation $(2^\mu)^+\to(\mu^+,4)^3$ cannot be applied again
  ($|C'|$ is not of that form)". **Defect:** false when $\mu(i)=2^\nu$ for
  an infinite $\nu$, a case the sentence's own hypothesis
  $2^{\aleph_0}\le\mu(i)$ allows. **Witness:** $2^{\aleph_0}=\aleph_2$,
  $n(0)=1$, $2^{\aleph_2}>2^{\aleph_1}$, $\mu(0)=\aleph_2$,
  $|C'|=\aleph_3=(2^{\aleph_0})^+$. **Replacement:** "inside which the
  relation $(2^\mu)^+\to(\mu^+,4)^3$ applies only when $\mu(i)=2^\nu$, and
  then yields a set of color $0$ of size $\nu^+<\mu(i)$, since
  $\nu<\aleph_{n(0)}<\mu(i)$".
- **F4 (note). Location:** connections page, (P1) bullet, "Clause (3)'s
  heredity hypothesis is met by thinning $S_i$ alone and keeping $T_i$";
  lead page, "clause (3) removes the remaining dependence when its
  hypothesis $2^{\chi+\kappa}<\operatorname{cf}\mu(i)$ holds".
  **Defect:** the property is not hereditary under same-size subsets in
  the reconstruction's reading, so clause (3) as stated does not apply;
  what is used, soundly, is the reconstruction's fiber argument with the
  thinning confined to $S_i$ (W2). **Replacement:** "the fiber argument of
  clause (3) applies with the thinning confined to $S_i$, which keeps
  $P_i$; the heredity hypothesis of (3) as stated is not needed".
- **F5 (note). Location:** connections page, after the endgame proof, "it
  shows that the case $\eta_2=1$, $\varepsilon=0$ cannot be handled
  without the $T_i$". **Defect:** $f_0$ violates hypothesis (ii) of the
  endgame lemma, so it defeats no implication the section states.
  **Replacement:** "it shows that the canonical values on the $S_i$ alone
  do not decide that case: $f_0$ realizes $\varepsilon=\eta_1=0$,
  $\eta_2=1$ with no color-$1$ four-element set and no color-$0$ set of
  the form $\bigcup S_i$".
- **F6 (note). Location:** connections page, (P2) bullet, "By (1A) at $j$
  with $\bar a=(a,a')$ and the first thinning of the lemma page".
  **Defect:** the first thinning is a proof-internal fact of the
  reconstruction, outside the interface (T1) lists; it is essential here,
  because $P_i$ must be phrased with the points $a_j$ available at stage
  $i$. **Replacement:** add to (T1) the fact that every $b\in B_\alpha$
  has the type of $a^*_\alpha$ over $E_\alpha$, or cite the
  reconstruction's labeled fact by name.
- **F7 (note). Location:** connections page, (P2) bullet, "So (P2) needs a
  block statement of its own: in every $C\subseteq A_i$ of size
  $\lambda_i$, for every coloring of $[C]^2$ with at most $2^{\aleph_0}$
  colors"; Next investigation and lead Next step 1, the (P3) question
  "induced by an $f$". **Defect:** (BS2) quantifies over all colorings,
  stronger than the route needs, which is the one coloring $c_i$
  determined by $f$ and the points $a^*_j$; and the (P3) question depends
  on the admissible lower sequence through $E_j$, not on $f$ and $C$
  alone. **Replacement:** "is supplied by" for "needs", and "for every
  admissible lower sequence and every full-size $C$" in the (P3)
  question.
- **F8 (note). Location:** connections page, Outcome, "the lemma supplies
  (P1) under $2^{\aleph_0}<\aleph_\omega$". **Defect:** the realizability
  (H) behind (P1) also consumes the unheld relation
  $(2^\mu)^+\to(\mu^+,4)^3$, carried elsewhere on both pages but not in
  this sentence. **Replacement:** "supplies (P1) under
  $2^{\aleph_0}<\aleph_\omega$ and the imported triple relation".

## Verdict

- S1: not a claim (the target). S2: not a claim (a definition).
- S3, the endgame lemma: refutation-failed.
- S4, the remark on the triples $T_i$: refutation-failed, with the scope
  of (c) narrowed as in F5.
- S5, the application of (T1) with the properties $P_i$:
  refutation-failed, conditionally on the imported relation
  $(2^\mu)^+\to(\mu^+,4)^3$, which is not held.
- S6, (P1) under $2^{\aleph_0}<\aleph_\omega$: refutation-failed, with
  the wording of F4.
- S7, the reduction of (P2) to the constancy of $c_i$: refutation-failed.
- S8a, the parenthetical "cannot be applied again": refuted-as-stated;
  its consequence S8b stands.
- S8b, the rest of the Erdős--Rado discussion and the need for (BS2):
  refutation-failed.
- S9a, no clause of the lemma reaches (P3): refutation-failed.
- S9b, "(P3) says that $d_j$ is constant": refuted-as-stated, witness in
  W1.
- S10, the counting obstruction for (P3): refutation-failed.
- S11, the falsification checks: refutation-failed.
- S12a, positive outcome plus (BS2) proves the conjecture under
  $2^{\aleph_0}<\aleph_\omega$: proof defective; statement unresolved. The
  bridge is missing (F1); it is supplied for (P3) restricted to $a\in S_i$
  by the extra fiber step of W1, after which the corrected statement
  follows.
- S12b, a negative outcome excludes every proof through canonization over
  the lower blocks: proof defective; statement unresolved (F2).
- S13, the outcome sentence: refutation-failed as author-recorded, with
  the qualification of F8.

The lead page inherits these verdicts at the sentences that restate S3,
S6, S7, S9b, S10 and S12; its provisional-premises list is accurate, and
its standing sentences claim nothing beyond author-recorded.

**Limitations.** The relation $(2^\mu)^+\to(\mu^+,4)^3$ and the
Erdős--Rado and Ramsey relations are imported, not held, and were not
verified beyond their statements; the attribution of the triple relation
was not checked. The sentences that cite the problem page's dated search
and assessment were not checked, as that text is excluded. The proofs of
(T1), (T2), (T3) and of the reconstruction pages are other reviewers'
subjects and were used only through their stated interfaces.

This focused review assigns no tier and changes no status.

---
name: research/erdos_49/evidence/verify/connections_problem_416_an_asymptotic_formula_for_the_totien_review
title: "Independent review of the connections section: Problem 416: an asymptotic formula for the totient count"
desc: |
  Focused refutation review of the Problem 416 section of the connections page
  as it stood on 2026-09-28T13:50:48Z: of ten statements, eight are
  refutation-failed, one is refuted-as-stated (the two-sided order of magnitude
  attributed to Lemma 4.1 alone) and one is descriptive and unchecked; one
  required correction, two suggested, one note.
created: 2026-09-28T18:11:36Z
updated: 2026-09-28T18:20:40Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context, commissioned for
refutation, who took no part in writing the connections page, the folder's
reconstruction pages or the leads they carry; the assignment text was the
only briefing, and no review, grade, assessment or standing text about the
subject was read.

**Subject.** Path `wiki/research/erdos_49/connections.md` as it stood on
2026-09-28T13:50:48Z, the section headed "Problem 416: an asymptotic formula for
the totient count", lines 444--467 (from its H2 heading to the line before the
next H2 at line 468). The section names no lead page. The page's "Outcomes at a
glance" paragraph (beginning at line 44) says "Problem 416: fails", which agrees
with the section's outcome; it is not part of the subject.

**Reading.**

- The subject section in full.
- The page's frontmatter, preamble and "Notation and the inputs used"
  (lines 1--111) in full, as inputs whose proofs another reviewer checks;
  the interfaces of (L4) and (F) were confirmed at each use below.
- The page's Problem 417 section (lines 283--443), because the subject
  consumes its Proposition 2: the proposition's statement and proof were
  read to fix its interface and to see which inputs its proof cites; the
  proof itself is another reviewer's subject and was not re-derived.
- The folder's
  [[research/erdos_49/lemma_4_1_reconstruction|Lemma 4.1]],
  [[research/erdos_49/lemma_5_1_reconstruction|Lemma 5.1]] and
  [[research/erdos_49/theorem_1_2_reconstruction|Theorem 1.2]]
  reconstruction pages in the same state, in full, as premises at the
  standing the commission states.
- The Statement paragraph of
  [[problems/arithmetic_functions/E0416/_index|Problem 416]] (lines 19--21 of the
  problem page), and nothing else of that page except the exposure below.
- The library card
  [[../library/arithmetic_functions/ford_1998_distribution_totients/_index|Ford (1998)]]
  in full, and the held PDF (43 physical pages, whose printed page numbers
  coincide with the physical ones): Theorems 1 and 2 (p. 2), the remark on
  Erdős's question (p. 3), Theorem 8 with the definition of $V(x;k)$
  (p. 4), the candidate set (5.13)--(5.17) (p. 25), the closing sentence
  of the proof of Theorem 2 (p. 26) and the closing paragraphs of §7
  (p. 39). The conversion beside the PDF served only to locate these
  passages; the PDF text is what was read.
- `docs/verification.md` ("Grading and claim standing", both audit
  checklists and "Whole-claim report"), `docs/approach_vetting.md`,
  `docs/evidence.md` ("Source fidelity") and `docs/math_authoring.md`.

**Exposures.**

1. A structural listing of the problem page above its Current assessment,
   taken to find the Statement paragraph, printed the frontmatter line
   `status: open` and the first line of the page's Status paragraph, which
   says the first question is answered yes. No other standing, Progress,
   Known Results or Current assessment text of that page was read.
2. To check the section's sentence about the folder index of the Problem
   416 reconstruction, [[research/erdos_416/_index|that index]] was read
   in full. It carries standing text about that folder's own
   reconstruction pages (review verdicts and applied corrections) and the
   acceptance of a Lean proof of the doubling law; none of it concerns the
   subject section or this folder.
3. Directory listings showed the file names of the existing reviews and
   grade in this folder's `evidence/verify/`, of untracked reviews of other
   sections of the same page written in parallel in that directory, and of
   untracked review files in another folder; none was opened.

## Restatement

Conventions. $V(x)$ counts the totients $\le x$;
$\mathcal W(x)=\{\varphi(n):n\le x\}$ and $W(x)=\#\mathcal W(x)$, written
$V'(x)$ on Problem 417; $Z(x)$ is Ford's function as the Theorem 1.2 page
defines it; $A(v)$ is the number of preimages of a totient $v$; $V_k(x)$
counts the totients $v\le x$ with $A(v)=k$, and $V(x;k)$ the totients
$\le x$ all of whose preimages are divisible by $k$ (Ford's (1.1) and
p. 4); an integer $n$ is *convenient* for a totient $d$ with preimages
$n_1,\ldots,n_k$ when $d\varphi(n)$ is a totient whose preimages are
exactly $n_1n,\ldots,n_kn$. "Large $x$" means $x$ beyond a threshold
depending on the fixed parameters.

- **S1** (target). The second question of Problem 416 asks for an
  asymptotic formula for $V(x)$; the first asks whether $V(2x)/V(x)\to2$.
- **S2** (target, descriptive). The problem page's current assessment,
  dated 2026-09-27, records the second question as open, the first as
  proved by an accepted Lean proof, and Ford's Theorem 1 as the best
  formula-type result.
- **S3.** (L4) is the lower-bound half of Ford's order of magnitude
  $V(x)\asymp Z(x)$. Here (L4) says: for fixed totients $d_1,d_2$ and
  fixed $D\ge\max\{d_1,d_2\}$ there are an absolute $K\ge1$, a constant
  $c_D>0$ and a threshold $x_0(D)$ such that for $x\ge x_0(D)$ at least
  $c_DZ(x)$ integers $n$ satisfy $\varphi(n)\le x/D$, $n$ convenient for
  $d_1$ and for $d_2$, and $n/\varphi(n)\le K$.
- **S4.** Proposition 2 of the page recovers $W(x)\asymp V(x)\asymp Z(x)$
  for large $x$ from (L4).
- **S5.** Beyond S3 and S4, nothing in the folder's inputs (T1), (T3),
  (L4), (F), (P) or its reconstructed results transports to the second
  question.
- **S6.** The count in (L4) is $\gg_DZ(x)$ with an unspecified constant,
  and a lower bound of this kind yields no asymptotic formula for $V(x)$.
- **S7.** For every finite list of totients $d$ (seeds), the union of the
  families $\{d\varphi(n):n\text{ convenient for }d\}$ misses whole
  classes of totients.
- **S8.** Ford remarks in §7 of the held paper that an asymptotic formula
  for $V(x)$ would require the asymptotics of $V_k(x)/V(x)$ and
  $V(x;k)/V(x)$ for every $k$.
- **S9.** The folder index of the Problem 416 reconstruction states the
  same gap, an order of magnitude but no formula, from the doubling-law
  side.
- **S10** (outcome). The transfer to the second question of Problem 416
  fails, because the mechanism is an order-of-magnitude construction.

## Checklist

- **Quantifiers and scope.** Pass. Every bound in the section is eventual
  ("for large $x$"), matching the thresholds $x\ge x_0(D)$ of (L4) and the
  range of Ford's Theorem 1; "any finite list of seeds" and "for every
  $k$" carry the quantifiers the argument needs. The sentence "A
  lower-bound construction gives an order of magnitude, never a formula"
  is a universal over all lower-bound constructions; F3 scopes it to this
  mechanism.
- **Circularity.** Pass. Nothing is deduced from an asymptotic formula.
  Ford's Theorem 2, which this review uses to complete the obstruction, is
  proved by Ford's §5 construction, independently of any formula.
- **Model and convention changes.** Pass. $V(x)$ is the same object on the
  problem page, on the Ford card and on this page; $W(x)=V'(x)$ by the
  page's Notation section; "convenient" is the notion the Lemma 5.1 page
  defines; Ford's classes $V_k$ and $V(x;k)$ are used with Ford's meaning
  but are undefined on the page (F4).
- **Finite and statistical overreach.** Pass. The section uses no finite
  evidence. The preimage sets quoted under Weakest steps illustrate a
  general proof; they are not the proof.
- **Uniformity.** Pass. The section says that $c_D$ is unspecified and
  depends on $D$, as the Lemma 4.1 page records, with possible dependence
  on $d_1,d_2$ as well. The strongest attack below records that (L4) gives
  nothing when the seed bound $D$ grows with $x$, a uniformity the section
  correctly does not claim.
- **Extremal conclusions.** Inapplicable: the section asserts no infimum,
  supremum, attained value or sharpness.
- **Consequences and composition.** Fail at S4 (F1, required): the
  two-sided order $W\asymp V\asymp Z$ composes the lower bound from (L4)
  with the upper half of (F), Ford's Theorem 1, which is not part of (L4);
  the section's own first clause, calling (L4) the lower-bound half, says
  as much. Incomplete from S7 to S10 (F3, suggested): "miss whole classes"
  blocks a formula only when the missed classes carry a positive
  proportion of the totients, which is Ford's Theorem 2; the section does
  not state this clause, although its outcome also follows from S6 alone.
- **Computation.** Inapplicable to the section, which computes nothing.
  The review's own exact witness, the preimage sets of the totients $1$,
  $2$, $4$, $6$ and $54$, is recorded under Weakest steps and checks by
  hand.
- **Reproduction.** Inapplicable: the section carries no rerun instruction
  or coverage claim.
- **Source and verdict fidelity.** Pass with a suggested correction (F2).
  Ford's remark is where the section says, on p. 39 inside §7 (pp.
  35--39), and says what the section says, except that Ford writes it as
  a belief ("I believe that ... will require simultaneously determining")
  and that the phrase "miss whole classes of totients" is Ford's from a
  later sentence of the same paragraph, where he writes "may miss". The
  characterization of the Problem 416 folder index is faithful (read
  under the disclosed exposure). S2 characterizes excluded text and was
  not checked.

## Weakest steps

**W1: the order-of-magnitude chain behind S4.** Apply (L4) with
$d_1=d_2=1$ and $D=K$. The interface allows it: $1$ is a totient, its
preimages are exactly $1$ and $2$ (since $\varphi(1)=\varphi(2)=1$ and
$\varphi(m)\ge2$ for $m\ge3$), and $K\ge1=\max\{d_1,d_2\}$. For
$x\ge x_0(K)$ there are at least $c_KZ(x)$ integers $n$ with
$\varphi(n)\le x/K$, convenient for $1$, and $n\le K\varphi(n)\le x$.
Convenience for $1$ says that the preimages of $\varphi(n)$ are exactly $n$
and $2n$, so $n$ is the least preimage, $n\mapsto\varphi(n)$ is injective
on the set, and each value lies in $\mathcal W(x)$; hence $W(x)\ge c_KZ(x)$.
Next, $\mathcal W(x)$ is a set of totients $\le x$, because
$\varphi(n)\le n\le x$, so $W(x)\le V(x)$. Finally $V(x)\le C_1Z(x)$ for
large $x$ is the upper half of Ford's Theorem 1 (p. 2), which reads

$$
V(x)=\frac{x}{\log x}\exp\bigl\{C(\log_3x-\log_4x)^2+D\log_3x
-(D+\tfrac12-2C)\log_4x+O(1)\bigr\},
$$

Ford's $D$ being the page's $C'$, so that $V(x)=Z(x)e^{O(1)}$. The chain

$$
c_KZ(x)\le W(x)\le V(x)\le C_1Z(x)
$$

is correct and is exactly what the proof of Proposition 2 writes. Only its
left inequality comes from (L4); the right one is (F), which that proof
cites by name. (L4) is a lower bound on the size of one set of integers and
carries no upper bound for $V$. That is the defect in S4 (F1).

**W2: the obstruction behind S7.** Fix a totient $d$ with preimages
$n_1<\cdots<n_k$, so $A(d)=k$. If $n$ is convenient for $d$, the preimages
of $d\varphi(n)$ are exactly $n_1n,\ldots,n_kn$, which are $k$ distinct
integers, so $A(d\varphi(n))=k$. Hence the family of $d$ lies inside the
multiplicity class $\{v:A(v)=k\}$, and the union of the families of a
finite seed list lies inside the union of finitely many multiplicity
classes. Multiplicity is unbounded on totients: every $n\le x$ has
$\varphi(n)\le x$, so the sum of $A(v)$ over the totients $v\le x$ is at
least $\lfloor x\rfloor$, while $V(x)\le C_1Z(x)=o(x)$ by Ford's Theorem 1
(the exponent of $Z$ is $o(\log_2x)$); thus the largest multiplicity of a
totient $\le x$ is at least $\lfloor x\rfloor/V(x)\to\infty$. So some
multiplicity $k'$ outside the finite list occurs, and the whole nonempty
class $\{v:A(v)=k'\}$ is missed: S7 holds. Concretely, the seeds the page
uses, $1$ (preimages $1,2$) and $2^{18}\cdot257$ (eight preimages, all
even), have multiplicities $2$ and $8$, and every totient of multiplicity
$3$, such as $2$ (preimages $3,4,6$), $44$ (preimages $69,92,138$) and
$56$ (preimages $87,116,174$), is missed. Ford's own example (p. 39) shows
the loss inside one class: the seeds $4$ (preimages $5,8,10,12$) and $6$
(preimages $7,9,14,18$) both have multiplicity $4$, and their families are
disjoint, since a common member would have least preimage $5n=7n'$ and
greatest preimage $12n=18n'$, forcing $n/n'=7/5=3/2$. What turns S7 into
an obstruction to a formula is a clause the section does not state: the
missed class has positive relative density, $V_{k'}(x)\gg V(x)$ for
$x\ge x_0(d')$ whenever $A(d')=k'$, which is Ford's Theorem 2 (p. 2, on
the card). With it, the union of the families counts at most $(1-c)V(x)$
totients $\le x$ for large $x$, so no asymptotic formula for $V(x)$ can be
read off the families (F3). Without it, missing whole classes is
compatible with a formula, since a missed class of relative density zero
costs nothing.

**W3: the constant behind S6.** (L4) delivers $V(x)\ge W(x)\ge c_DZ(x)$
with $c_D$ unknown, so it locates $V(x)$ at best between $c_DZ(x)$ and
Ford's $C_1Z(x)$. A sharpened count of the same family with an explicit
constant would still not be a formula: by W2 the family is a proper
positive-proportion part of the totients, and $Z(x)$ itself is not
asymptotic to $V(x)$ by any held result, Theorem 1 giving only
$V(x)=Z(x)e^{O(1)}$. Ford states the same limit of the method on p. 3: the
proof of Theorem 1 "falls short of" even $V(cx)\sim cV(x)$. So S6 stands,
and S10 already follows from S6 alone.

## Strongest attack

- **S1.** Compared with the Statement paragraph of the problem page, which
  asks whether $V(2x)/V(x)\to2$ and whether there is an asymptotic formula
  for $V(x)$. Exact match; no attack available.
- **S2.** Describes text outside the commissioned read set; not attacked.
- **S3.** Attack: (L4) might be a different construction from the one
  behind Ford's lower bound, or might give no lower bound for $V$. Both
  fail. Ford's candidate set on p. 25, (5.13)--(5.16), consists of the
  $n=p_0\cdots p_L>x^{9/10}$ with $\varphi(n)\le x/d$, the system
  $\mathcal S_L(\boldsymbol\xi)$, $\log_2p_i\ge(1+\omega_i)\log_2p_{i+1}$
  and $p_L\ge\max(d+2,17)$; that is the candidate set of the Lemma 4.1
  page with $d$ renamed $D$, (5.17) is its lower bound, and the proof of
  Theorem 2 ends (p. 26) with the sentence that the lower bound in
  Theorem 1 follows by taking $d=1$ and multiplicity $2$. Directly, (L4)
  with $d_1=d_2=1$ and $D=1$ gives $c_1Z(x)$ totients $\varphi(n)\le x$,
  distinct because $n$ is the least preimage of each, so $V(x)\gg Z(x)$.
- **S4.** The attack succeeded: the proof of Proposition 2 cites (F) for
  $V(x)\le C_1Z(x)$; see W1 and F1.
- **S5.** Attack: find something in the folder that yields more than an
  order of magnitude for $V(x)$. (T1) and (T3) bound $P(x;k)$, the number
  of $n\le x$ with $\varphi(n)=\varphi(n+k)$, by $Bx/(\log x)^2$ for
  $k\le\log x$ (Theorem 1.2 page, input (B)); summed over $k\le\log x$
  this bounds the near-neighbor collisions by $Bx/\log x$, while
  $W(x)=x/(\log x)^{1+o(1)}$ (input (D) there) says that almost every
  $n\le x$ collides with some $m<n$, so near-neighbor collisions are a
  vanishing part of what $W$ or $V$ counts. Lemma 5.1 and Theorem 1.2
  compare monotone subsets with $W(x)$, not $W$ or $V$ with $x$. (P) is
  one seed. A growing seed list, all totients $d\le D(x)$ with
  $D(x)\to\infty$, would need (L4) uniformly in $D$, which (L4) does not
  state: $c_D$ and $x_0(D)$ depend on $D$. The attack fails.
- **S6.** Attack: the constant might be pinned somewhere in the chain. The
  Lemma 4.1 page records "$c_D>0$ and $x_0(D)$", possibly depending also
  on $d_1,d_2$, from an imported count "$\gg_DZ(x)$"; nothing pins $c_D$.
  Fails.
- **S7.** Attack: with $n$ unrestricted, the family of the seed $1$ is the
  whole set of totients and misses nothing, so the statement is true only
  for convenient $n$. That is the section's context ("the count of
  convenient integers"), and under that reading the proof in W2 is
  complete. Fails, with a wording note in F2.
- **S8.** Attack: the remark might be elsewhere or say something else. It
  is on p. 39 inside §7 (pp. 35--39) and reads "I believe that obtaining
  the asymptotic formula for $V(x)$ will require simultaneously
  determining the asymptotics of $V_k(x)/V(x)$ (more will be said in
  section 8) and $V(x;k)/V(x)$ for each $k$"; three sentences later Ford
  writes that the Section 5 construction "may miss whole classes of
  totients with multiplicity $k$". The section's paraphrase drops "I
  believe", "simultaneously" and "may" (F2). Otherwise faithful; fails.
- **S9.** The cited index says, under its heading for the second question:
  open; Ford's Theorem 1 gives $V(x)$ up to a factor $e^{O(1)}$; the
  doubling law adds regularity but no formula, since multiplying $V$ by
  $e^{\sin\log\log x}$ preserves $V(2x)\sim2V(x)$ (checked:
  $\log\log2x-\log\log x\to0$). Faithful; fails.
- **S10.** Follows from S6, and from S7 once F3's clause is added. Fails.

## Premises

- **(L4)**, [[research/erdos_49/lemma_4_1_reconstruction|Lemma 4.1]]:
  fixed totients $d_1,d_2$ and fixed $D\ge\max\{d_1,d_2\}$; an absolute
  $K$; $c_D>0$ and $x_0(D)$, possibly depending on $d_1,d_2$; for
  $x\ge x_0(D)$ at least $c_DZ(x)$ integers $n$ with (i)
  $\varphi(n)\le x/D$, (ii) $n$ convenient for $d_1$ and for $d_2$, (iii)
  $n/\varphi(n)\le K$. A premise at the standing the commission states; the
  page itself records that its counting steps (F1) and (F2) are imported
  from Ford and not reconstructed. Read in full; used within its
  hypotheses at every point above ($d_1=d_2=1$ with $D=K$ or $D=1$).
- **Convenient integers**,
  [[research/erdos_49/lemma_5_1_reconstruction|Lemma 5.1]]: the definition
  restated above. Read in full; only the definition is used.
- **$Z(x)$**, [[research/erdos_49/theorem_1_2_reconstruction|Theorem 1.2]]:
  Ford's function with $C=0.817814\ldots$ and $C'=2.17696874\ldots$; its
  exponent is $o(\log_2x)$, so $Z(x)=o(x)$ (used in W2); inputs (B), the
  uniform collision bound, and (D), Erdős's count of totient values, of
  that page are used in the attack on S5. Read in full.
- **Proposition 2** of the connections page (Problem 417 section):
  $V(x)\le C\,V'(x)$ for large $x$; its proof yields $W(x)\ge c_KZ(x)$
  from (L4) and cites (F) for $V(x)\le C_1Z(x)$. Statement and proof read;
  the proof is another reviewer's subject.
- **(F)**, Ford's Theorem 1, held PDF p. 2, displayed in W1: with Ford's
  $D$ equal to the page's $C'$, $V(x)=Z(x)e^{O(1)}$. Read at statement
  level against the PDF; the consequences the Notation section draws from
  it are another reviewer's subject, and only the upper bound
  $V(x)\le C_1Z(x)$ is used here.
- **Ford's Theorem 2**, p. 2: for every $\varepsilon>0$, if $A(d)=k$ then
  $V_k(x)\gg_\varepsilon d^{-1-\varepsilon}V(x)$ for $x\ge x_0(d)$.
  Statement level; used only in this review's completion of the
  obstruction (F3), not by the section.
- **Ford's Theorem 8 and $V(x;k)$**, p. 4: $V(x;k)$ counts the totients
  $\le x$ all of whose preimages are divisible by $k$; if some totient $d$
  has all preimages divisible by $k$ then
  $V(x;k)\gg_\varepsilon d^{-1-\varepsilon}V(x)$. Statement level; needed
  only to read S8.
- **Ford's §5 and §7** (pp. 25, 26 and 39) and the p. 3 remark on Erdős's
  question: read as quoted above.
- **Problem 416 Statement**, lines 19--21 of the problem page: read.
- **Problem 416 folder index**: read in full under the disclosed exposure;
  used only for S9.

## Findings

- **F1** (required). Location: "**What transports.** (L4) is the
  lower-bound half of Ford's order of magnitude; Proposition 2 above even
  recovers $W(x)\asymp V(x)\asymp Z(x)$ from it." Defect: the two-sided
  order is not recovered from (L4). (L4) yields only $W(x)\ge c_KZ(x)$;
  the upper bound $V(x)\le C_1Z(x)$ that closes the chain is the upper
  half of (F), Ford's Theorem 1, which the proof of Proposition 2 cites
  separately; and the sentence contradicts its own first clause. Witness:
  the last line of that proof, "with (F),
  $V(x)\le C_1Z(x)\le(C_1/c_K)W(x)$". Replacement: "(L4) is the
  lower-bound half of Ford's order of magnitude; the proof of Proposition
  2 above recovers $W(x)\ge c_KZ(x)$ from it and, with the upper bound of
  (F), $W(x)\asymp V(x)\asymp Z(x)$. Nothing more."
- **F2** (suggested). Location: "the families $d\varphi(n)$ built from any
  finite list of seeds $d$ miss whole classes of totients, as Ford himself
  remarks in §7 of the held paper when he writes that an asymptotic
  formula would require the asymptotics of $V_k(x)/V(x)$ and
  $V(x;k)/V(x)$ for every $k$." Defect: two of Ford's qualifiers are
  dropped and two of his sentences are merged. On p. 39 Ford writes "I
  believe that obtaining the asymptotic formula for $V(x)$ will require
  simultaneously determining the asymptotics of $V_k(x)/V(x)$ ... and
  $V(x;k)/V(x)$ for each $k$", a stated belief, and three sentences later
  that the Section 5 construction "may miss whole classes of totients with
  multiplicity $k$"; the section states both as fact and attributes the
  second to the first. The restriction to convenient $n$ is also left
  implicit. The mathematical claim is provable (W2), so the page can carry
  it as its own observation. Replacement: "the families $d\varphi(n)$, $n$
  convenient for $d$, built from any finite list of seeds $d$ lie in
  finitely many multiplicity classes and so miss whole classes of totients
  (a seed with $k$ preimages produces only totients with exactly $k$
  preimages, and multiplicity is unbounded because $V(x)=o(x)$); Ford
  says as much in §7 of the held paper (p. 39), where he writes that he
  believes an asymptotic formula will require simultaneously determining
  the asymptotics of $V_k(x)/V(x)$ and $V(x;k)/V(x)$ for each $k$, and
  that the Section 5 construction may miss whole classes of totients of a
  given multiplicity."
- **F3** (suggested). Location: "A lower-bound construction gives an order
  of magnitude, never a formula: the count of convenient integers is
  $\gg_DZ(x)$ with an unspecified constant, and the families $d\varphi(n)$
  built from any finite list of seeds $d$ miss whole classes of totients".
  Defect: as an obstruction to a formula, "miss whole classes" needs the
  clause that the missed classes carry a positive proportion of the
  totients; a construction missing only classes of relative density zero
  could still give a formula. The clause is Ford's Theorem 2 on the card:
  if $A(d')=k'$ then $V_{k'}(x)\gg V(x)$ for $x\ge x_0(d')$, so the union
  of finitely many seed families counts at most $(1-c)V(x)$ totients
  $\le x$ for large $x$. The opening sentence is also a universal about
  all lower-bound constructions. Replacement: "This lower-bound
  construction gives at most an order of magnitude, not a formula: the
  count of convenient integers is $\gg_DZ(x)$ with an unspecified
  constant, and the families built from any finite list of seeds miss
  whole multiplicity classes, each a positive proportion of all totients
  by Ford's Theorem 2 on the card, so that together they count at most
  $(1-c)V(x)$ totients $\le x$."
- **F4** (note). $V_k(x)$ and $V(x;k)$ are used in the section without a
  definition anywhere on the page; the Notation section defines $V$,
  $\mathcal W$, $W$, $P$, $P_0$, $P_1$, $c(k)$, $Z$ and "convenient" only.
  Add "where $V_k(x)$ counts the totients $\le x$ with exactly $k$
  preimages and $V(x;k)$ those all of whose preimages are divisible by
  $k$", or point to the card's rows for Theorems 2 and 8.

## Verdict

- S1: refutation-failed.
- S2: not a mathematical claim within this review's remit; it describes
  excluded text and was not checked.
- S3: refutation-failed.
- S4: refuted-as-stated; the corrected sentence of F1, the lower bound from
  (L4) and the two-sided order with (F), holds.
- S5: refutation-failed.
- S6: refutation-failed.
- S7: refutation-failed, by this review's proof in W2; the section's cited
  support is imprecise (F2).
- S8: refutation-failed, with the dropped qualifiers of F2.
- S9: refutation-failed.
- S10: refutation-failed; the outcome follows from S6 alone and, with F3's
  clause, from S7.

Limitations. S2 and the phrase "the best formula-type result" characterize
the problem page's assessment and the literature, both outside the
commissioned read set, and were not checked; no web search was made. The
proofs of (L4), of Proposition 2 and of the Notation section's consequences
of (F) were not re-derived here beyond their interfaces. Ford's Theorems 1,
2 and 8 were read at statement level; their proofs were not checked. This
focused review assigns no tier and changes no status.

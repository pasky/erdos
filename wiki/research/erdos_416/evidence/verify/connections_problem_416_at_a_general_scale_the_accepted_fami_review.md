---
name: research/erdos_416/evidence/verify/connections_problem_416_at_a_general_scale_the_accepted_fami_review
title: "Independent review of the connections section: Problem 416 at a general scale: the accepted family with another scale"
desc: |
  Refutation-failed for the two lemmas, the conditional general-scale
  proposition, the scale-free remark, the block-mean and product
  corollaries and the positive-outcome sentence; refuted-as-stated for the
  claim that the cluster interval stands for every c other than 2, since
  the accepted law settles every integer power of 2; one required
  correction, two suggested, five notes.
created: 2026-09-28T18:30:24Z
updated: 2026-09-28T20:40:27Z
---

***

## Subject and independence

The reviewer is an independent reviewer working in a fresh context from
this assignment alone, took no part in writing the reviewed pages or any
page of the Problem 416 folder, and had no contact with their authors. The
charge is refutation of author-recorded mathematics; no tier is assigned
and no status changes.

Subject, by path and date: the source as it stood on 2026-09-28T13:50:48Z
(the tip of the default branch at the time of review, called "the commit"
below), path `wiki/research/erdos_416/connections.md`, the H2 section at
line 342, lines 342–453, whose heading on the page reads "Problem 416 at a
general scale: the accepted family with another balance". The assignment
names the section "... with another scale"; the page carries no section of
that name, and the section reviewed is the one at that position whose
content the assignment describes (Lemmas 416.1 and 416.2, Proposition
416.3, the two remarks, the block-mean paragraph, the outcome). Lead page:
`wiki/research/leads/general_scale_totient_doubling/_index.md` at the same
commit, whole page.

Read, and at what depth:

- The section, in full, every displayed and inline formula rederived; the
  lead page, in full.
- The page's shared sections as inputs only (lines 1–90: Purpose and
  standing, Notation, Imported inputs, The search), with their interfaces
  confirmed at each use; the bodies of the page's other sections were not
  read (their headings were seen while locating the section).
- The four reconstruction pages of the folder at the same commit, in full,
  as premises: `kruer_kohlmeyer_lemma_2_1_reconstruction.md`,
  `kruer_kohlmeyer_lemma_5_1_reconstruction.md`,
  `kruer_kohlmeyer_theorem_1_1_reconstruction.md` and
  `zeraoulia_theorem_1_1_reconstruction.md`.
- The Statement of `wiki/problems/arithmetic_functions/E0416/_index.md` (lines
  19–20).
- Library: the card of the write-up
  ([[../library/arithmetic_functions/kruer_kohlmeyer_2026_doubling_law_distinct_totient_values/_index|Kruer and Kohlmeyer (2026)]])
  and its four result pages; the card of
  [[../library/arithmetic_functions/ford_1998_distribution_totients/_index|Ford (1998)]];
  the head of the card of
  [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|Guy (2004)]]
  through its provenance paragraph; the head of the card of
  [[../library/arithmetic_functions/zeraoulia_2026_fixed_scale_limit_points_distinct_totients/_index|Zeraoulia (2026)]].
- Held PDFs: the write-up, text of pp. 1–5 and the page image of p. 4
  (§4.3 and §5); Ford (1998), text of pp. 1–4 (§1.2 on p. 3); Guy (2004),
  section B36 on printed p. 139 (PDF p. 157) on the page image and in the
  text layer.
- `docs/verification.md` (Whole-claim report, Audit checklist, Grading and
  claim standing, both the shared and the Erdos-specific forms),
  `docs/approach_vetting.md`, `docs/evidence.md` "Source fidelity",
  `docs/math_authoring.md`.

Exposures, disclosed: (1) lines 22–60 of the problem page (its Status,
Provenance of the proof file and Source paragraphs) reached the reviewer
while locating the Statement, which has no heading of its own; (2) the
write-up's card was printed whole, so its accepted-file paragraph, its
formal-statement-and-acceptance paragraph, its Read status, Overview and
Relation to E416 reached the reviewer, as did the Standing lines of its
four result pages; (3) the Ford card was printed whole (it has no separate
provenance paragraph), and the Zeraoulia card's Bears on, Read status and
Overview were printed with its provenance; (4) the environment showed
the repository's recent commit subjects and a tree listing that named the
files under `evidence/verify/`, none of which was opened. No review, grade,
folder index, Current assessment, Known results or acceptance section of
the folder was read; no web search was made; nothing among the private working files
was read.

## Restatement

Conventions throughout: $V(x)$ is the number of integers $n$ with
$1\le n\le x$ that are values of Euler's function (preimage unrestricted,
each value once), $T(x)$ the set of them, $R_c(x)=V(cx)/V(x)$; limits are
as real $x\to\infty$ unless said otherwise; $g=o(h)$ means for every
$\theta>0$ eventually $|g|\le\theta h$. A retained family at endpoint $y$
is a finite set $P_y$ with a map $f_y\colon P_y\to T(y)$, with
$A_y=|P_y|$, $M_y=V(y)-|f_y(P_y)|$, $E_y=A_y-|f_y(P_y)|$; (3) is
$M_y\le\varepsilon V(y)+V(y^{99/100})$ eventually, (4) is $E_y=o(V(y))$,
and $B_y$ counts $a\in P_y$ with $f_y(a)\le y/2$.

- **S1 (target and provenance).** The general-scale variant is: for every
  fixed real $c>1$, $R_c(x)\to c$. It is Erdős's question, recorded in
  Guy's B36 and in §1.2 of Ford's paper, where Ford says the method of his
  Theorem 1 falls short of it. It is not a clause of the catalog statement,
  whose first question is the case $c=2$ and whose second is an asymptotic
  formula. For $c\ne2$ the folder holds only the preprint's reconstructed
  claim: $c$ is a limit point of $R_c(n)$ over the integers and the set of
  limit points is a closed interval $[\alpha_c,\beta_c]$ of unknown width.
- **S2 (Lemma 416.1).** For finite sets $T_0\subseteq T$, any finite $P$
  and map $f\colon P\to T$, with $P_0=f^{-1}(T_0)$, $I=f(P)$,
  $I_0=f(P_0)$, $M=|T|-|I|$, $M_0=|T_0|-|I_0|$, $E=|P|-|I|$,
  $E_0=|P_0|-|I_0|$, and for every real $c\ge1$:
  $\bigl||T|-c|T_0|\bigr|\le\bigl||P|-c|P_0|\bigr|+\max(1,c-1)(M+E)$.
- **S3 (Lemma 416.2).** For real $c>0$ (implicit; the section fixes $c$ as
  a scale), $v>0$, $w\ge0$, $0\le\delta\le1/2$: if $|w-cv|\le\delta w$
  then $|w/v-c|\le2c\delta$.
- **S4 (Proposition 416.3).** Fix $c>1$. Hypothesis: for every
  $0<\varepsilon<1/2$ there are retained families $(P_y,f_y)$, one for
  each large real $y$, satisfying (3) with that $\varepsilon$, (4), and
  (5$_c$): $A_y-cB^{(c)}_y=o(A_y)$ where
  $B^{(c)}_y=\#\{a\in P_y:f_y(a)\le y/c\}$. Conclusion: $R_c(x)\to c$ as
  real $x\to\infty$.
- **S5 (first remark).** (3) and (4) do not involve $c$. Hence the
  $\varepsilon$-indexed families of the accepted Lean file, whose (3) and
  (4) the write-up identifies with kernel-accepted declarations, satisfy
  the first two hypotheses of S4 for every $c>1$, and at that standing the
  general-scale law at a given $c$ follows from (5$_c$) for those
  families.
- **S6 (second remark, conditional).** Premise: (5) at $c=2$ comes from a
  mass $H(y)>0$ with $A_y/H(y)\to1$ and $B_y/H(y)\to1/2$, the pairs lying
  above cores $b$ with $\log b\le G(y)=o(\log y)$. Conditional claim: if
  the pairs above each core $b$ are the primes $p$ in a range (an
  interval) whose upper end is $y/b$ for $p-1$, equivalently $y$ for the
  value $b(p-1)$ (the page writes "with $b(p-1)$ in a range whose upper
  end is $y/b$", see F2), then $B^{(c)}_y/H(y)\to1/c$ by the uniformity
  $\pi(u/c)/\pi(u)\to1/c$ for $u\ge y^{1-o(1)}$, so (5$_c$) holds for
  every $c>1$. Whether the accepted development counts in this way is not
  established.
- **S7 (block mean).** For $c=2^{1/m}$, $m\ge2$, and every real $x\ge1$,
  $\prod_{j=0}^{m-1}R_c(c^jx)=V(2x)/V(x)$, which tends to $2$ by the
  accepted law; so the geometric mean of $R_c$ over any $m$ consecutive
  scales tends to $c$, an exact finite-block form of the preprint's
  block-mean step; this yields near-hits and no width control.
- **S8 (product constraint).** For $c=\sqrt2$, $\alpha_c\beta_c=2$: a
  sequence realizing $\alpha_c$ at $x$ realizes $2/\alpha_c$ at $cx$ and
  symmetrically; this does not force $\alpha_c=\beta_c$.
- **S9 (what it does not give, first three clauses).** No asymptotic
  formula for $V$ (the mass depends on $\varepsilon$), no rate, and no
  prose proof, since (3) and (4) keep the standing of the accepted file.
- **S10 (what it does not give, fourth clause; lead's Consequential gap).**
  Section: "nothing for $c\ne2$ until (5$_c$) is verified, so the
  preprint's dichotomy stands for every $c\ne2$", that is, for every
  $c\ne2$ it remains undecided whether $R_c\to c$ or the cluster set is a
  nondegenerate interval. Lead: "Without it the reconstructed cluster
  interval $[\alpha_c,\beta_c]$ stands for every $c\ne2$; the accepted
  $c=2$ law adds only that for $c=2^{1/m}$ the geometric mean ... tends to
  $c$".
- **S11 (next investigation, positive outcome).** If the accepted file's
  top-prime ranges and count are scale-free, then (5$_c$) holds for every
  $c>1$ by the argument of S6, hence by S4 $V(cx)\sim cV(x)$ for all
  $c>1$ at the standing of the accepted file plus an author-checked
  generalization, and the reconstructed cluster interval collapses to
  $\{c\}$ for every $c$.
- **S12 (next investigation, negative outcome).** "a negative one shows the
  family's prime ranges tied to the scale $2$, so that a general-scale
  family needs its own estimates (3)–(5)".
- **S13 (standing sentences).** Section: "Transfers conditionally, with the
  premise (5$_c$) explicit"; lead: every result author-recorded, the
  proposition conditional, the lead a candidate and unreviewed, the
  standing of (3) and (4) the site's kernel acceptance with no prose
  proof, the file not held and not built.

## Checklist

- **Quantifiers and scope.** S4's order is sound: for each $\delta$ an
  $\varepsilon$ and its family are chosen, then $y$ is taken large, and the
  conclusion is about $V$ alone (W1). S7 and S8 pass from integer to real
  limits through clause 3 of the preprint's reconstruction. The universal
  "for every $c\ne2$" of S10 fails at every integer power of $2$ (F1).
  Verdict: one defect, F1.
- **Circularity.** None. The target $R_c\to c$ is nowhere assumed; the
  accepted $c=2$ law is used only where the section says so (S7, S8, and
  it is what refutes S10).
- **Model and convention changes.** $V$ and $T$ are the problem page's;
  the write-up's (3) and (4) are transported verbatim;
  $T(y/c)\subseteq T(y)$ is finite for $c>1$; Guy's $\Phi$ is the same
  count (with a slip of the source noted under Premises). No substitution
  of a relaxed system. Verdict: clean.
- **Finite and statistical overreach.** No finite computation or heuristic
  average is used as a proof. Verdict: inapplicable, clean.
- **Uniformity.** The constants $\max(1,c-1)$ and $2c$ depend on the fixed
  $c$ only; the thresholds of the $o(\cdot)$ terms depend on
  $\varepsilon$ and the family, as stated. In S6 the prime-number-theorem
  uniformity is in $u\to\infty$ for fixed $c$ and is correct, but the
  written argument omits the negligibility of the lower ends of the prime
  ranges, which W2 derives from the $c=2$ balance (F2). Verdict: one
  suggested correction, F2.
- **Extremal conclusions.** $\alpha_c\beta_c=2$ is checked in the claim's
  own units, the limit inferior and superior of the ratio, with
  $\alpha_c\ge1$ and $\beta_c$ finite supplied by the preprint's
  reconstruction (W3). Verdict: clean.
- **Consequences and composition.** S4 inherits exactly the standing of
  (3), (4) and the hypothesis (5$_c$), all stated. The "hence" of S10 is
  false (F1); the "shows" of S12 overreaches (F3). Verdict: F1 required,
  F3 suggested.
- **Computation.** None in the section. The only numerals, the line number
  63482 and the card's identifiers, were checked against the write-up's
  §6 table and the card. Verdict: inapplicable, clean.
- **Reproduction.** No rerun commands or coverage claims. Verdict:
  inapplicable.
- **Source and verdict fidelity.** Guy B36 records "Erdős conjectures that
  $\Phi(cy)/\Phi(y)\to c$" (page image); Ford §1.2 records "Erdős has
  asked if $V(cx)\sim cV(x)$ for each fixed $c>1$" and "The method of
  proof of Theorem 1, however, falls short of answering Erdős' question"
  (p. 3); the write-up's §4.3 says what the section says it says (page
  image), and its §6 table places `power_corePairs_count_asymptotic` at
  line 63482. The standing sentences (S13) claim no more than
  author-recorded. "Erdős posed with it" is not verifiable in the read set
  (F8). Verdict: clean, with one unverified provenance clause.

## Weakest steps

**W1: Step 4 of Proposition 416.3 with the constant $\max(1,c-1)$.** Put
$\kappa=\max(1,c-1)$ and $D^{(c)}_y=A_y-cB^{(c)}_y$. Since $f_y$ maps into
$T(y)$ and $T(y/c)=T(y)\cap[1,y/c]$, $P_0=f_y^{-1}(T(y/c))$ is exactly
the set of pairs with value at most $y/c$, so S2 with $T=T(y)$,
$T_0=T(y/c)$ gives
$|V(y)-cV(y/c)|\le|D^{(c)}_y|+\kappa M_y+\kappa E_y$. By (4) with
$\theta=1$, eventually $E_y\le V(y)$, so
$A_y=|f_y(P_y)|+E_y\le2V(y)$; with (5$_c$), for every $\theta$ eventually
$|D^{(c)}_y|\le\theta A_y\le2\theta V(y)$, so $D^{(c)}_y=o(V(y))$. By (3),
$\kappa M_y\le\kappa\varepsilon V(y)+\kappa V(y^{99/100})$ eventually, and
$V(y^{99/100})/V(y)\le(\log y)/(c_0y^{1/100})\to0$ by $V(z)\le z$ and
Chebyshev. Hence eventually

$$
|V(y)-cV(y/c)|\le\kappa\varepsilon V(y)+r(y),\qquad r(y)=o(V(y)).
$$

Given $\delta>0$, choose $\varepsilon<\min(1/2,\delta/(2\kappa))$ and the
family for it; then $\kappa\varepsilon<\delta/2$ and $r(y)\le(\delta/2)V(y)$
for $y\ge Y(\delta)$, so $|V(y)-cV(y/c)|\le\delta V(y)$ there; with
$y=cx$, $|V(cx)-cV(x)|\le\delta V(cx)$ for $x\ge Y(\delta)/c$. For
$\eta>0$ take $\delta=\min(1/2,\eta/(4c))$ and $X=\max(1,Y(\delta)/c)$:
for $x\ge X$, $V(x)\ge1$, and S3 with $w=V(cx)$, $v=V(x)$ gives
$|R_c(x)-c|\le2c\delta\le\eta/2<\eta$. The family and its thresholds
depend on $\delta$; the final sentence is about $V$ alone. The step
composes with S2 (finite sets: $P_y$ is finite by definition, $T(y)$ is
finite) and S3 (its cap $\delta\le1/2$ is enforced by the choice of
$\delta$).

**W2: the conditional deduction of S6, including the lower ends.** Let the
cores at endpoint $y$ be a finite set $\mathcal B_y$ with
$\log b\le G(y)$, and suppose the pairs above $b$ are the primes $p$ with
$\ell_b<p\le u_b+1$, $u_b=y/b$, so that $b(p-1)\le y$ is the upper end.
Then $a_b:=\#\{p\}=\pi(u_b+1)-\pi(\ell_b)$ and, for $c>1$,
$b^{(c)}_b:=\#\{p:b(p-1)\le y/c\}=(\pi(u_b/c+1)-\pi(\ell_b))^+$, with
$A_y=\sum_ba_b$ and $B^{(c)}_y=\sum_bb^{(c)}_b$. Since
$u_b\ge ye^{-G(y)}=y^{1-o(1)}\to\infty$, the prime number theorem gives
$\pi(u_b/c+1)=(1/c+o(1))\pi(u_b+1)$ uniformly over $b\in\mathcal B_y$.
Write $x_b=\pi(\ell_b)/\pi(u_b+1)\in[0,1]$ and $w_b=\pi(u_b+1)$. Then
$a_b=w_b(1-x_b)$ and $b^{(c)}_b=w_b(1/c-x_b+o(1))^+$. If every $\ell_b$ is
negligible, $x_b=o(1)$ uniformly, and $B^{(c)}_y=(1/c+o(1))A_y$ at once.
The section's sentence "by the same uniformity" presupposes this and does
not say it; but it follows from the premise. The $c=2$ balance
$B_y/A_y\to1/2$ reads
$\sum_bw_b\bigl[(1/2-x_b+o(1))^+-(1-x_b)/2\bigr]=o(A_y)$, and the bracket
is at most $-\min(x_b,1-x_b)/2+o(1)$ in every case ($x_b\le1/2$ gives
$-x_b/2$; $x_b>1/2$ gives $-(1-x_b)/2$), so
$\sum_bw_b\min(x_b,1-x_b)=o(A_y)$. For any $c>1$ the defect
$b^{(c)}_b-a_b/c$ equals $-w_bx_b(1-1/c)$ when $x_b\le1/c$ and
$-w_b(1-x_b)/c$ when $x_b>1/c$, and in each case its size is at most
$w_b\min(x_b,1-x_b)$ (checked on the four cases $x_b\lessgtr1/2$,
$x_b\lessgtr1/c$; for $1/2<x_b\le1/c$, which needs $c<2$,
$x_b(1-1/c)\le1-x_b$ because both sides meet at $x_b=1/c$ with
$(c-1)/c^2\le(c-1)/c$). Summing, $B^{(c)}_y-A_y/c=o(A_y)$, which is
(5$_c$). So the conclusion of S6 is correct under the interval reading of
its hypothesis together with the $c=2$ balance already in its premise; a
non-interval range tied to the scale $2$, such as the primes with
$p-1\in(u_b/4,u_b/2]\cup(3u_b/4,u_b]$, satisfies the $c=2$ balance and
violates (5$_4$), which is why the hypothesis must be an interval with the
stated upper end.

**W3: $\alpha_c\beta_c=2$ for $c=\sqrt2$.** By the preprint's
reconstruction, $1\le R_c(n)\le K_c$ for large integers $n$, so
$\alpha_c=\liminf_nR_c(n)$ and $\beta_c=\limsup_nR_c(n)$ are finite with
$\alpha_c\ge1>0$, both are subsequential limits, and the set of
subsequential limits over the reals equals $[\alpha_c,\beta_c]$ (clause 3).
Take integers $n_k\to\infty$ with $R_c(n_k)\to\alpha_c$. Since $c^2=2$,
$R_c(n_k)R_c(cn_k)=V(2n_k)/V(n_k)\to2$ by the accepted law, so
$R_c(cn_k)\to2/\alpha_c$ along the real sequence $cn_k\to\infty$; hence
$2/\alpha_c\in[\alpha_c,\beta_c]$ and $\alpha_c\beta_c\ge2$. The same with
$\beta_c$ gives $2/\beta_c\ge\alpha_c$, so $\alpha_c\beta_c\le2$. The
constraint $\alpha_c\beta_c=2$ with $\alpha_c\le\sqrt2\le\beta_c$ is met by
every $[\alpha,2/\alpha]$ with $1\le\alpha\le\sqrt2$, so it does not force
$\alpha_c=\beta_c$; the log-periodic shape $R_c(x)=c\,e^{a\sin(\pi\log_cx)}$
satisfies $R_c(x)R_c(cx)=c^2=2$ identically and shows the constraint alone
has no more content.

## Strongest attack

- **S1.** Attack: find the variant absent from the cited sources, or the
  catalog statement containing it. Guy's B36 (page image) records the
  conjecture $\Phi(cy)/\Phi(y)\to c$; Ford's §1.2 (p. 3) records the
  question for each fixed $c>1$ and the "falls short" sentence; the
  catalog statement asks $c=2$ and an asymptotic formula only. Failed. The
  clause "posed with it" could not be attacked or confirmed (F8).
- **S2.** Attack: break the identity or the bounds at $c>2$ or $c=1$. The
  identity $|T|-c|T_0|=(|P|-c|P_0|)+(M-cM_0)-(E-cE_0)$ follows from
  $|T|=|I|+M$, $|T_0|=|I_0|+M_0$, $|I|=|P|-E$, $|I_0|=|P_0|-E_0$; with
  $0\le M_0\le M$ and $c\ge1$, $M-cM_0\in[-(c-1)M,M]$, so
  $|M-cM_0|\le\max(1,c-1)M$, and likewise for $E$ since $0\le E_0\le E$ by
  the fiber sum; equality at $M_0=M$ shows the constant is the best of
  this form for $c>2$.
  Failed.
- **S3.** Attack: the boundary $\delta=1/2$ and $c$ large. With
  $\delta=1/2$, $w\le2cv$ and $|w/v-c|\le c=2c\delta$, attained at
  $w=2cv$; sharp, not false. For $c\le0$ the hypothesis forces $w=0$ and
  the conclusion fails at $c<0$, which is the unstated range (F6). Failed
  for the scales in use.
- **S4.** Attack: a family satisfying (3), (4), (5$_c$) for every
  $\varepsilon$ with $R_c\not\to c$. W1 is a complete deduction with the
  thresholds tracked; the only places where $c$ enters are the inclusion
  $T(y/c)\subseteq T(y)$, the identification of $P_0$ (both need only
  $c>1$ and $f_y(P_y)\subseteq T(y)$), the constants and (5$_c$). Failed.
- **S5.** Attack: a hidden $c$ in (3) or (4). $M_y$ and $E_y$ are defined
  from $P_y$, $f_y$ and $T(y)$ alone. The identification of (3), (4) with
  the declarations rests on the write-up's word, which the statement
  carries by "at that standing". Failed; wording note F7.
- **S6.** Attack: ranges balanced at $c=2$ but not at $c=4$. The
  non-interval witness of W2 does exactly that, so the hypothesis must be
  an interval with upper end $y/b$ for $p-1$; under that reading W2 proves
  the conclusion, closing the lower-end gap the sentence leaves open.
  Attack on the literal words "$b(p-1)$ in a range whose upper end is
  $y/b$": as a formal conditional it still yields (5$_c$) (the same prime
  number theorem step with $u_b=y/b^2$), but it describes pairs with
  values up to $y/b$, not the family of the write-up (F2). Failed under
  the intended reading.
- **S7.** Attack: an $x$ where the product is not $V(2x)/V(x)$, or a scale
  block without a near-hit. The product telescopes exactly for every real
  $x\ge1$ since $c^m=2$; near-hits follow from the block mean by the
  preprint's three-case argument with the unit-jump bound (7). Failed.
- **S8.** W3. Failed.
- **S9.** Attack: extract a rate or a formula from S4. The mass $H(y)$
  enters only through (5$_c$), which is an $o(\cdot)$ statement for each
  $\varepsilon$-family; nothing quantitative survives the choice of
  $\varepsilon$ against $\delta$. Failed.
- **S10.** Attack: an integer power of $2$. With $c=4$,
  $R_4(x)=R_2(2x)R_2(x)\to2\cdot2=4$ by the accepted law at $2x$ and at
  $x$; so $\mathcal C_4=\{4\}$, $\alpha_4=\beta_4=4$, the dichotomy is
  decided in its first horn and the interval is degenerate, with no
  premise. By induction $R_{2^m}(x)\to2^m$ for every integer $m\ge1$, and
  for $c=2^{k/m}$ the product over $m$ consecutive scales tends to $2^k$.
  Succeeded: refuted-as-stated (F1).
- **S11.** Attack: a positive outcome without (5$_c$). Scale-free interval
  ranges with a scale-free count are exactly the hypothesis of W2, which
  gives (5$_c$); S4 then gives the law; $R_c\to c$ makes the cluster set
  $\{c\}$. Failed.
- **S12.** Attack: a negative outcome after which the accepted family still
  satisfies (5$_c$). Nothing in the outcome excludes a different count of
  the same pairs giving (5$_c$); the sentence's "shows ... needs" is not a
  deduction (F3). Not a mathematical claim; wording finding only.
- **S13.** Attack: a sentence claiming independent standing. None found;
  every result is marked author-recorded or conditional, and the file's
  standing is stated as the site's acceptance. Failed.

## Premises

- [[research/erdos_416/kruer_kohlmeyer_lemma_2_1_reconstruction|Lemma 2.1 reconstruction]]:
  interface used, finite $T_0\subseteq T$, $f\colon P\to T$, the exact
  identity, $0\le M_0\le M$, $0\le E_0\le E$, and the identification
  $P_0=\{a:f_y(a)\le y/2\}$ when $T_0=T(y/2)$, generalized here to $y/c$;
  read in full; used within its hypotheses.
- [[research/erdos_416/kruer_kohlmeyer_theorem_1_1_reconstruction|Theorem 1.1 reconstruction]]:
  Steps 1–5 with their thresholds, Proposition 4.1 as an imported premise
  with its $\varepsilon$-dependence and the $o(\cdot)$ convention,
  Chebyshev's bound, the §4.3 gloss (which places the upper end at
  $b(p-1)\le y$), and its closing sketch of the $T_0=T(y/c)$ variant; read
  in full.
- [[research/erdos_416/kruer_kohlmeyer_lemma_5_1_reconstruction|Lemma 5.1 reconstruction]]:
  the $c=2$ case of S3 and the role of the cap; read in full.
- [[research/erdos_416/zeraoulia_theorem_1_1_reconstruction|Preprint reconstruction]]:
  clauses 1–3 of its statement, $1\le R_c\le K_c$ eventually, the
  unit-jump bound (7), and the coincidence of the real and integer cluster
  sets; read in full; it imports Ford's Theorem 1 at statement level and
  Chebyshev's bound.
- The write-up (Kruer and Kohlmeyer, 2026), held PDF: §1 definitions, §2
  Lemma 2.1 and displays (1)–(2), §4 Proposition 4.1 with (3)–(5) and
  §4.3, §5, §6 line table; text of pp. 1–5, image of p. 4. Its card:
  provenance (URL, 94,397 bytes, hash) and the accepted file's URL, size
  and hash; the four result pages' statements. The accepted Lean file is
  not held; its standing is the site's kernel acceptance as the card
  records, and no declaration of it was read beyond its line number by
  anyone in the read set.
- Ford (1998), held PDF, §1.2 p. 3: Erdős's question for each fixed $c>1$
  and the "falls short" sentence; text of pp. 1–4.
- Guy (2004), held PDF, B36 on printed p. 139 (PDF p. 157), page image:
  "Erdős conjectures that $\Phi(cy)/\Phi(y)\to c$, and that this, if true,
  may be the best substitute that one can find for an asymptotic formula
  for $\Phi(y)$", with $\Phi(y)$ described as the number of $n$ for which
  $\phi(x)=n$ has a solution, although the book prints it as $y-\#(y)$
  with $\#(y)$ its count of even nontotients, a slip of the source that
  the section does not inherit.
- Problem 416 statement (page lines 19–20): the two catalog questions.
- Chebyshev's bound and the prime number theorem in the form
  $\pi(u/c)/\pi(u)\to1/c$ for fixed $c>1$: textbook results, the latter
  used only inside the conditional S6 and in W2.

## Findings

- **F1 (required).** Location, section "What it does not give": "nothing
  for $c\ne2$ until (5$_c$) is verified, so the preprint's dichotomy
  stands for every $c\ne2$"; lead "Consequential gap": "Without it the
  reconstructed cluster interval $[\alpha_c,\beta_c]$ stands for every
  $c\ne2$; the accepted $c=2$ law adds only that for $c=2^{1/m}$ the
  geometric mean ... tends to $c$"; and the section's paragraph "What the
  accepted $c=2$ law adds without any premise, for $c=2^{1/m}$ with
  $m\ge2$", which omits the integer powers. Defect: the accepted law
  settles the general-scale variant at every $c=2^m$, $m\ge1$ an integer.
  Witness: $c=4$, $V(4x)/V(x)=\bigl(V(4x)/V(2x)\bigr)\bigl(V(2x)/V(x)\bigr)\to4$
  as real $x\to\infty$, so $\alpha_4=\beta_4=4$ and the dichotomy is
  decided; by induction $V(2^mx)/V(x)\to2^m$. Replacement: write "for
  every $c>1$ that is not an integer power of $2$" in both sentences,
  drop "only" in the lead, and add to the "What the accepted $c=2$ law
  adds" paragraph: for $c=2^m$ with an integer $m\ge2$ the law gives
  $V(cx)/V(x)\to c$ outright by telescoping, at the standing of the
  accepted file, and for $c=2^{k/m}$ the product over $m$ consecutive
  scales tends to $2^k$. The Target sentence "For $c\ne2$ the problem
  page's assessment finds only the preprint's claim" describes a page
  outside this review's read set; whatever that page finds, the
  mathematics settles the integer powers of $2$, and the sentence should
  not read as if they were open.
- **F2 (suggested).** Location, section second remark and lead
  "Provisional premises": "if the pairs above a core $b$ are the primes
  $p$ with $b(p-1)$ in a range whose upper end is $y/b$". Defect (i): the
  upper end $y/b$ belongs to $p-1$; the value $b(p-1)$ has upper end $y$,
  as the Theorem 1.1 page's gloss has it; as written the pairs above $b$
  carry values only up to $y/b$. Defect (ii): "by the same uniformity of
  the prime number theorem" needs the lower ends of the prime ranges to be
  negligible against $y/b$ in aggregate, which the sentence does not say;
  W2 derives it from the $c=2$ balance in the premise under the interval
  reading, and shows a non-interval range for which the $c=2$ balance
  holds and (5$_4$) fails. Replacement: "if the pairs above a core $b$ are
  the primes $p$ in an interval whose upper end is $y/b$ for $p-1$, so
  that $b(p-1)\le y$, then the $c=2$ balance forces the lower ends to be
  negligible in aggregate, and $B^{(c)}_y/H(y)\to1/c$ by the uniformity
  ...".
- **F3 (suggested).** Location, section and lead "Next investigation" /
  "Next step": "a negative one shows the family's prime ranges tied to the
  scale $2$, so that a general-scale family needs its own estimates
  (3)–(5)". Defect: a negative outcome closes the section's route to
  (5$_c$) for the accepted family; it does not show (5$_c$) false for that
  family, since a different count of the same pairs could give it, so it
  does not show that a new family is needed. Replacement: "a negative one
  closes this route: (5$_c$) for the accepted family would then need an
  argument of its own, or a differently balanced family with its own
  estimates (3)–(5)".
- **F4 (note).** Location: "The prose deduction of the doubling law uses
  $c=2$ in exactly one place, the balance estimate (5)." The scale also
  enters Lemma 2.1's specialization ($T_0=T(y/2)$), Lemma 5.1 (the
  constant $4$) and the constants of Steps 4–5, as a parameter that the two
  lemmas generalize; (5) is the only place where it enters as a hypothesis
  on the family. Suggested wording: "uses $c=2$ as a hypothesis on the
  family in exactly one place".
- **F5 (note).** Location: "$c=2$ is that page's display (2)". At $c=2$
  Lemma 416.1 is the Lemma 2.1 page's Statement (the write-up's display
  (1)); the page's display (2) is the totient specialization.
- **F6 (note).** Lemma 416.2 states no range for $c$; its proof needs
  $c>0$ (for $c\le0$ the hypothesis forces $w=0$ and the conclusion fails
  when $c<0$). In context $c>1$; write "for real $c>0$".
- **F7 (note).** "the single balance statement (5$_c$) for that family":
  the accepted file supplies one family per $\varepsilon$, and (5$_c$) is
  needed for each, as Proposition 416.3 states; and "whose (3) and (4) are
  the kernel-accepted declarations" identifies the write-up's summary with
  the declarations on the write-up's word, which "at that standing" is
  meant to cover and could say.
- **F8 (note).** "that Erdős posed with it": the read set records the
  question in Ford's §1.2 ("Erdős has asked") and Guy's B36 ("Erdős
  conjectures"); neither places it beside the $c=2$ question, and the 1974
  paper is outside the read set. Unverified provenance, not an error
  found.

## Verdict

- S1: refutation-failed for the checkable clauses; the clause "posed with
  it" is unverified in the read set (F8).
- S2 (Lemma 416.1): refutation-failed.
- S3 (Lemma 416.2): refutation-failed, with the implicit range $c>0$
  (F6).
- S4 (Proposition 416.3): refutation-failed; the deduction is complete
  from its stated hypotheses, and its standing is that of (3), (4) and the
  unproved (5$_c$).
- S5 (first remark): refutation-failed (F7 wording).
- S6 (second remark): refutation-failed under the interval reading of its
  hypothesis, with the lower-end step supplied in W2; the hypothesis
  sentence is misstated (F2).
- S7 (block mean): refutation-failed.
- S8 (product constraint): refutation-failed.
- S9 (no formula, no rate, no prose proof): refutation-failed.
- S10 (the dichotomy and the interval stand for every $c\ne2$; the law
  adds only the block mean): refuted-as-stated, witness $c=4$ (F1).
- S11 (positive outcome): refutation-failed.
- S12 (negative outcome): not a mathematical claim; its "shows"
  overreaches (F3).
- S13 (standing sentences): refutation-failed.

Limitations: the accepted Lean file is not held, so (3), (4) and the
$c=2$ form of (5) enter at the site's kernel acceptance as the folder
records, and nothing here examines them; the conditional S6 was checked as
an implication, and whether its antecedent describes the accepted family
remains, as the section says, not established; the prime number theorem
and Chebyshev's bound were taken as textbook results; the preprint's
reconstruction and the three write-up reconstructions were taken as
established at their recorded standing and only their interfaces were
confirmed. This focused review assigns no tier and changes no status.

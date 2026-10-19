---
name: research/erdos_18/evidence/verify/connections_problem_859_the_density_of_n_representing_a_fixe_review
title: "Independent review of the connections section: Problem 859: the density of n representing a fixed t"
desc: |
  Refutation review of the Problem 859 section of the connections page as of
  2026-09-28T13:50:48Z: the target restatement, the single-seed transfer, its
  polynomial floor and the h-independence clause survive (refutation-failed);
  the status report is outside the read set; two suggested wording findings,
  one note, zero required corrections.
created: 2026-09-28T18:10:16Z
updated: 2026-09-28T18:10:16Z
---

***

## Subject and independence

The reviewer acted as an independent reviewer in a fresh context, given only
the commissioning assignment, and took no part in writing the connections
page, the reconstruction pages or any other page of the folder. The charge was
refutation of the author-recorded mathematics of one section.

Subject: the repository as it stood at 2026-09-28T13:50:48Z (the default
branch's state at the time), page `wiki/research/erdos_18/connections.md`,
section `## Problem 859: the density of n representing a fixed t`, lines
716–735 (the next H2, `## Other divisor problems examined`, is line 736). No
separate lead page was named; the section targets
`wiki/problems/divisors/E0859/_index.md`.

Read, and at what depth:

- The section, lines 716–735, in full, several times.
- The page's shared sections as inputs: the opening paragraph and the
  Conventions paragraph (lines 15–45) in full, and the Shared lemmas section
  (lines 47–243) in full, used only to confirm the conventions for practical
  numbers and $h$; the section under review invokes none of Lemmas A–D.
- Reconstruction pages as premises, as of 2026-09-28T13:50:48Z:
  [[research/erdos_18/doorn_proposition_4_1_reconstruction|the Proposition 4.1 page]]
  in full;
  [[research/erdos_18/doorn_lemma_3_1_reconstruction|the Lemma 3.1 page]]
  through its Definitions and Statement;
  [[research/erdos_18/hughes_lemma_4_reconstruction|the Lemma 4 page]]
  through its Definitions and Statement.
- The Statement block of `wiki/problems/divisors/E0859/_index.md` (lines 14–29, the
  text before the `**Status.**` label at line 30) and nothing else of that
  page.
- The provenance paragraph of
  [[../library/divisors/doorn_2026_practical_numbers_egyptian_fractions/_index|the van Doorn (2026) card]],
  the Statement section of its Proposition 4.1 result page, and physical
  pp. 5–6 of the held PDF in text extraction (Proposition 4.1, its proof and
  Lemma 5.1).
- `docs/verification.md` sections "Grading and claim standing", "Audit
  checklist" (shared and Erdos-specific) and "Whole-claim report";
  `docs/approach_vetting.md`; `docs/evidence.md` "Source fidelity";
  `docs/math_authoring.md`.

Not read: the folder's `_index.md`; everything under any `evidence/` folder,
including every existing review and grade; the E0859 page beyond its Statement
block (status, provenance of the proof file, current assessment, progress,
known results, linked library material); any other problem page; other
sections' reviews; anything among the private working files or outside the repository; the
web. Exposure: none.

## Restatement

The section uses the folder's conventions: a positive integer $N$ is
*practical* when every integer $1\le m\le N$ is a sum of distinct positive
divisors of $N$, and $h(N)$ is the least number of distinct divisors that
suffices for every such $m$ (Lemma 3.1 page, Definitions). Throughout,
$S_t=\{n\in\mathbb N: t\text{ is a sum of distinct divisors of }n\}$ and
$d_t$ is its density.

- **S1 (target, restated from the problem page).** For each integer $t\ge1$,
  $d_t$ is the density of $S_t$; the question is whether there exist
  constants $c_1,c_2>0$ with $d_t\sim c_1(\log t)^{-c_2}$ as $t\to\infty$.
- **S2 (recorded status, reported).** The problem page records the status
  *disproved*, by a Lean counterexample the bounty site approved on 21
  September 2026 and uncertified as of 2026-09-22, whose content is stated
  as: $-\log d_t/\log\log t$ has lower limit $\delta=0.0860\ldots$ as
  $t\to\infty$, while $(\log t)^{\delta}d_t\to0$.
- **S3 (outcome).** The target is resolved, and the folder's mechanisms bear
  on it in neither direction.
- **S4 (transfer lemma).** If $N$ is practical and $N\ge t$, then every
  multiple of $N$ lies in $S_t$.
- **S5 (consequence).** Hence $d_t\ge1/N$ for such $N$, in particular for the
  least practical $N\ge t$ that a construction of the folder supplies.
- **S6 (quantitative floor).** For the construction of Proposition 4.1 that
  $N$ lies in $[t,t^2)$, so the bound obtained is at least $1/t^{2}$ (the
  section's phrase is "$\ge1/t^{2}$ at best"), and a bound of this size says
  nothing at the scale $(\log t)^{-\delta}$.
- **S7 (characterization of the disproof).** The accepted disproof's lower
  estimate uses practical seeds inside a tilted prime-pattern law, read only
  at the level of structure, as seeds of a density argument and not through
  $h$; the reconstructed bounds on $h$ neither supply nor replace that step.
- **S8 (conclusion).** "No transfer exists."

## Checklist

- **Quantifiers and scope.** S1 reproduces the Statement block faithfully:
  the page's "$t\ge1$", "$n\in\mathbb N$", "constants $c_1,c_2>0$" and "as
  $t\to\infty$" are carried or implicit in "$\sim$". S4 is universal in
  practical $N\ge t$ and in the multiple; checked. S6 omits the hypothesis
  $t\ge x_0$ under which Proposition 4.1 supplies its $N$; harmless for the
  asymptotic conclusion (F1). S2's "lower limit" cannot be checked here
  (outside the read set). Pass with the note in F1.
- **Circularity.** None: S4 is proved from the definition of practicality,
  S5 from S4 and the density of an arithmetic progression, S6 from
  Proposition 4.1's interval; nothing assumes the target. Pass.
- **Model and convention changes.** The section's practicality is the Lemma
  3.1 page's ($m\le N$), which is what S4 needs; "density" is read as natural
  density, and $S_t$ has one (Weakest step W1). The folder's fresh-set $h$
  plays no role in $S_t$. Pass.
- **Finite and statistical overreach.** Inapplicable: no finite computation
  and no averaging heuristic is used as a proof.
- **Uniformity.** The only imported constant is Proposition 4.1's $x_0$,
  uniform in $p_*$ on its page; the section uses only the interval
  $[t,t^2)$, so no parameter dependence is at issue. Pass.
- **Extremal conclusions.** The sentence "$\ge1/t^{2}$ at best" states an
  extremum in the wrong direction: $1/t^2$ is the floor guaranteed by
  $N<t^2$ (the worst case), and the best case of any seed $N\ge t$ is $1/t$.
  The inequality itself is correct. Finding F1 (suggested).
- **Consequences and composition.** Each "so" was checked separately: S4
  implies S5 (density of $N\mathbb N$ is $1/N$ and $S_t$ has a density);
  S5 with Proposition 4.1 implies S6; S6 implies "says nothing at the scale
  $(\log t)^{-\delta}$" since $t^{-2}=o((\log t)^{-\delta})$; S7's
  "not through $h$" follows from the definition of $S_t$ (W3). The closing
  "No transfer exists" claims more than the composition proves (F2). Pass
  with F2.
- **Computation.** The only figures are $\delta=0.0860\ldots$, quoted from
  the excluded status text, and the interval $[t,t^2)$. The quoted constant
  agrees with $1-(1+\log\log2)/\log2=0.08607\ldots$, the exponent in the
  classical count of integers with a divisor in $[y,2y]$, which is consistent
  with the structure S7 describes; this agreement is the reviewer's own
  check, not a verification of the excluded text. Pass.
- **Reproduction.** Inapplicable: the section carries no rerun command,
  coverage claim or executable evidence.
- **Source and verdict fidelity.** Proposition 4.1 is cited for
  "$N\in[t,t^2)$": the reconstruction page, the library result page's
  Statement section and the PDF (p. 5) all state $x\le n<x^2$ for
  $x\ge x_0$ and every odd prime $p_*$; faithful, with the omitted
  $x\ge x_0$ noted in F1. S1 is faithful to the Statement block. S2 and S7
  characterize the problem page's status text and the accepted disproof,
  both outside the read set; they are hedged in the section ("uncertified as
  of 2026-09-22", "read only at the level of structure") and are recorded
  here as unverified (F3). Pass within the read set.

## Weakest steps

**W1: S4 and the existence of $d_t$ (S4 to S5).** Let $N$ be practical
with $N\ge t$. By the definition, $t=\sum_{d\in D}d$ for a set $D$ of
distinct divisors of $N$. For every multiple $n=kN$, each $d\in D$ divides
$n$, so $n\in S_t$; this is S4. For S5 one needs $S_t$ to have a density.
$n\in S_t$ exactly when $\operatorname{lcm}(D)\mid n$ for some set $D$ of
distinct positive integers with $\sum D=t$; the family of such $D$ is finite
(partitions of $t$ into distinct parts), so $S_t$ is a finite union of
arithmetic progressions $\operatorname{lcm}(D)\mathbb N$ and has a natural
density by inclusion–exclusion. Since $N\mathbb N\subseteq S_t$ and
$\#\{n\le x:N\mid n\}/x\to1/N$, $d_t\ge1/N$. The same inequality holds for
the lower density if "density" were read that way. Composition: S5 is used
only through the least seed of a construction; every seed satisfies $N\ge t$,
so no seed gives more than $1/t$.

**W2: S6, the floor from Proposition 4.1.** The premise's interface: there
are $E\ge4$ and $x_0>e^e$ such that for every real $x\ge x_0$ and every odd
prime $p_*$ there is a practical $n$ with $x\le n<x^2$, $2^E\parallel n$,
$p_*\nmid n$ and $h(n)\le c_0(\log\log x)^2-1$. With $x=t\ge x_0$ and any
$p_*$, the first term $n_j\ge t$ of the chain is the section's "least
practical $N\ge t$ of the construction", and $N<t^2$ gives $d_t\ge1/N>1/t^2$.
Independently of that claimed result, the folder's factorial seed gives the
same conclusion unconditionally: with $n$ least such that $n!\ge t$,
$(n-1)!<t$ gives $n!<nt$, so $d_t\ge1/n!>1/(nt)$; and the power of two
$2^{\lceil\log_2t\rceil}<2t$ is practical (binary expansion), so
$d_t>1/(2t)$ for every $t\ge1$. All of these are polynomial in $1/t$, and
$t^{-1}=o((\log t)^{-\delta})$ for every $\delta>0$, so the conclusion "says
nothing at the scale $(\log t)^{-\delta}$" holds for every seed-based bound,
not only the one from Proposition 4.1.

**W3: S7's clause "not through $h$".** Membership of $n$ in $S_t$ depends
only on whether $t$ is representable by distinct divisors of $n$, never on
how many divisors are used. A practical seed $N$ contributes through the
representability of $t\le N$, which is the definition of practicality; any
value of $h(N)$ is compatible with the same $S_t$. Hence no bound on $h$
can enlarge, shrink or estimate $S_t$, and the clause "the reconstructed
bounds on $h$ neither supply nor replace that step" is forced by the
definition, whatever the structure of the accepted disproof.

## Strongest attack

**Against S3 and S8 (a transfer at logarithmic scale).** The attack tries to
produce, from the folder's mechanisms alone, a lower bound
$d_t\gg(\log t)^{-c}$, which would make the mechanisms bear on the target.
$S_t$ is closed under multiples, so it contains every $n$ that has a
practical divisor in $[t,2t]$, and the folder does supply practicality
criteria: the consequence clause of Lemma 4 (consecutive divisors of ratio at
most two), Lemma A's valuation criterion, and Lemma 3.1's extension step.
One can therefore describe a subset of $S_t$ by prime patterns, for instance
$n$ with $v_2(n)\ge a$ and a $2^a$-smooth divisor in $[t,2t]$, all of whose
odd prime factors are below $2^{v_2(n)}$. Counting such $n$ to logarithmic
precision requires a density theorem for integers with a divisor in a
prescribed interval under a prime-pattern constraint; nothing of that kind is
among the reconstructed mechanisms, and the practicality criteria of the
folder are special cases of the classical criterion the accepted disproof
would use as its seed condition anyway. Any bound reached this way would also
be no stronger than the recorded lower estimate, so it could not bear on a
resolved target. The attack fails against S3 and against S8 read as the
section's conclusion; it shows only that S8's absolute wording ("exists")
outruns what the section argues, which is F2.

**Against S4 (the reading of "sum of distinct divisors").** If the problem's
phrase required at least two summands, a practical $N$ with $t\mid N$ might
represent $t$ only by the single divisor $t$. Under that reading $S_1$ would
be empty and $d_1=0$, which makes the problem degenerate; the one-summand
reading is forced, and under it S4 holds as proved in W1. The attack fails.

**Against S5 and S6 (the direction of the inequality and the hypothesis).**
$N<t^2$ gives $1/N>1/t^2$, so "$\ge1/t^2$" is correct and even strict; the
phrase "at best" is the defect (F1). For $t<x_0$ Proposition 4.1 supplies
nothing, but the factorial and power-of-two seeds of W2 give the same
polynomial floor for every $t$, so the omitted hypothesis cannot change the
conclusion. The attack yields the wording finding only.

**Against S2 (internal consistency of the reported disproof).** If
$d_t\sim c_1(\log t)^{-c_2}$ with $c_1,c_2>0$, then
$-\log d_t/\log\log t\to c_2$, so the recorded lower limit forces
$c_2=\delta$, and then $(\log t)^{\delta}d_t\to c_1\ne0$, contradicting the
recorded $(\log t)^{\delta}d_t\to0$. So the two recorded facts do refute S1's
asymptotic; the deduction "the target is resolved" is valid given them. The
facts themselves, the approval date and the certification status are outside
the read set and were not verified (F3).

## Premises

- [[research/erdos_18/doorn_proposition_4_1_reconstruction|Proposition 4.1 (van Doorn), reconstruction]]:
  interface as quoted in W2; standing on its page *claimed*
  (author-recorded reconstruction of a claimed result); read in full. The
  section uses only the interval $x\le n<x^2$ and the existence of the chain's
  first term above $x$. Library: the Statement section of the result page and
  physical p. 5 of the held PDF (text extraction) agree with the
  reconstruction's statement; held.
- [[research/erdos_18/doorn_lemma_3_1_reconstruction|Lemma 3.1 (van Doorn), reconstruction]]:
  Definitions (practical numbers, $h$) and Statement read; standing
  *claimed*; only the definitions are consumed by the section.
- [[research/erdos_18/hughes_lemma_4_reconstruction|Lemma 4 (Hughes), reconstruction]]:
  Definitions and Statement read; used only in the Strongest attack as a
  practicality criterion; not consumed by the section.
- Shared lemmas A–D of the connections page: read as inputs; not consumed by
  the section (Lemma A's practicality of $n!$ and of powers of two is used in
  W2 only through the elementary binary-expansion fact).
- Problem page `wiki/problems/divisors/E0859/_index.md`, Statement block only:
  the definition of $d_t$ and the asked asymptotic, as restated in S1.
- Library card
  [[../library/divisors/doorn_2026_practical_numbers_egyptian_fractions/_index|van Doorn (2026)]]:
  provenance paragraph read (seven-page PDF, printed and PDF pages coincide,
  not refereed, not on arXiv as of 2026-09-27); held.
- Explicit assumptions of this review: natural density is meant by "density"
  (W1 shows $S_t$ has one); the one-summand reading of "sum of distinct
  divisors" (Strongest attack).

## Findings

- **F1 (suggested).** Location, lines 727–729: "the constructions of this
  folder give $d_t\ge1/N$ for the least practical $N\ge t$ of the
  construction, which is $\ge1/t^{2}$ at best (Proposition 4.1 places $N$ in
  $[t,t^2)$)". Defect: "at best" names the wrong extremum. From $N\in[t,t^2)$
  the bound is at least $1/t^2$ in the worst case and at most $1/t$ in the
  best, and the folder's other seeds are better than $1/t^2$: the least
  $n!\ge t$ satisfies $n!<nt$, and $2^{\lceil\log_2t\rceil}<2t$ gives
  $d_t>1/(2t)$. The hypothesis $t\ge x_0$ of Proposition 4.1 is also
  unstated. Witness: any $t\ge1$ with $N=2^{\lceil\log_2t\rceil}$, a practical
  seed with $1/N>1/(2t)\gg1/t^2$. Proposed replacement: "which is at least
  $1/t^{2}$ (Proposition 4.1 places $N$ in $[t,t^2)$ once $t\ge x_0$) and at
  most $1/t$ for any seed $N\ge t$, so polynomial in $1/t$ whatever the
  construction, and says nothing at the scale $(\log t)^{-\delta}$".
- **F2 (suggested).** Location, line 734: "No transfer exists." Defect: a
  universal negative that the section's argument does not establish; what is
  shown is that the single-seed transfer gives only a polynomial floor and
  that $h$ is irrelevant to $S_t$ by definition. The folder's practicality
  criteria could serve as a seed condition inside a density argument, though
  that would yield nothing new for a resolved target. Witness: the Strongest
  attack's prime-pattern subset of $S_t$, which is a transfer of a
  mechanism, only not one that bears on the target. Proposed replacement:
  "No transfer was found: the seed bound is polynomial in $1/t$, and $h$ does
  not enter $d_t$."
- **F3 (note).** Location, lines 720–723 and 730–734: the status report
  (approval on 21 September 2026, uncertified as of 2026-09-22, the two
  recorded facts about $d_t$) and the characterization of the accepted
  disproof ("practical seeds inside a tilted prime-pattern law"). Defect:
  none found; these characterize text outside the commissioned read set and
  are recorded as unverified by this review. Their internal logic checks
  (Strongest attack, S2). Proposed replacement: none.

## Verdict

- S1: **refutation-failed**. The restatement matches the problem page's
  Statement block in every quantifier.
- S2: not a mathematical claim of the section but a report of the problem
  page's status text, outside the read set and unverified here; the deduction
  it carries (the two recorded facts refute the asked asymptotic) is
  **refutation-failed**.
- S3: **refutation-failed** as an assessment: "resolved" rests on S2, and
  "bear on it in neither direction" is supported by S4–S7 and survived the
  Strongest attack.
- S4: **refutation-failed**; re-derived in W1 from the definition of
  practicality.
- S5: **refutation-failed**; re-derived in W1, including the existence of
  $d_t$.
- S6: **refutation-failed** for the inequality $d_t\ge1/N>1/t^2$ and for
  "says nothing at the scale $(\log t)^{-\delta}$"; the phrase "at best" is a
  wording defect (F1), not an error in the mathematics.
- S7: **refutation-failed** for the clause "not through $h$; the
  reconstructed bounds on $h$ neither supply nor replace that step", which
  follows from the definition of $S_t$ (W3); the description of the accepted
  disproof's structure is unverified within the read set (F3).
- S8: **refutation-failed** read as the section's conclusion that no
  transfer of the folder's mechanisms bears on Problem 859; as an absolute
  sentence it claims more than the section argues (F2).

Limitations. The review is confined to the commissioned read set: the
problem page's status, the accepted disproof and its certification were not
examined, so every verdict that mentions "resolved" is conditional on the
page's recorded status being as the section reports it. Proposition 4.1 was
used at its recorded standing (*claimed*); the polynomial floor of S6 does not
depend on it, since the factorial and power-of-two seeds give the same
conclusion unconditionally. No computation was needed beyond the arithmetic
shown. This focused review assigns no tier and changes no status.

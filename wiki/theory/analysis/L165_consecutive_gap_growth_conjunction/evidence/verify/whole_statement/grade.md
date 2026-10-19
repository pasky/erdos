---
name: theory/analysis/L165_consecutive_gap_growth_conjunction/evidence/verify/whole_statement/grade
title: Grade of the consecutive-gap conjunction examination
desc: Independent PASS grade of the complete frozen L165 examination, including its mathematical scope, report contract, actual reading, independence and preservation.
tags: []
sources: []
created: 2026-10-16T04:55:23Z
updated: 2026-10-16T04:55:23Z
---

# Grade of the consecutive-gap conjunction examination

***

**PASS.** The original whole-statement examination meets the report contract
and independence requirements for the complete frozen L165 conjunction and
its implication for the supplied mean-normalized modified Statement of Problem
1221. Its mathematical verdict, **refutation-failed**, is accepted at precisely
that scope. Each assertion and contract ruling is recorded below. No defect
requires a partial disposition or a hold at the recorded dependency reading.

Original project work and this independent assessment are credited to Plasma AI. Grading date: **2026-10-16 UTC**.

## Subject and independence

The subject is the original eight-file examination delivery, frozen on
2026-10-15 at 22:29:05.281749 UTC. Its underlying mathematical subject was
frozen on 2026-10-15 at 21:10:27.616818 UTC and examined that day. The originals,
including every marked omission, were read in full. This grade assesses those
originals, rather than a later rendering or the current L165 card.

| Original file | Reading and assessed scope |
| --- | --- |
| [report.md](report.md) | Complete report, including every contract part, checklist ruling, independence assertion and final verdict. |
| [keeper.md](keeper.md) | Complete analytic keeper, Sections 1–7; all derivations, witnesses, diagnostics and reconstruction instructions. |
| [claim.md.txt](../../assets/whole_statement_subject/claim.md.txt) | Complete supplied L165 statement and Conventions and scope. |
| [proof.md.txt](../../assets/whole_statement_subject/proof.md.txt) | Complete supplied mathematical argument and consequence sentences. |
| [premises.md.txt](../../assets/whole_statement_subject/premises.md.txt) | Complete supplied L163/L164 statements and Conventions and scope; no premise proofs. |
| [premise_standing.md.txt](../../assets/whole_statement_subject/premise_standing.md.txt) | Exact frozen generated-standing rows for the two consumed premises. |
| [catalog.md.txt](../../assets/whole_statement_subject/catalog.md.txt) | Complete supplied Statement, Statement (modified), Notes and Formulation excerpts, at the source boundary stated below. |
| [live_dependencies.json](../../assets/whole_statement_subject/live_dependencies.json) | Original final narrow dependency observation and its comparisons with the frozen interfaces. |

Their mathematical identifiers are
`wiki/theory/analysis/L165_consecutive_gap_growth_conjunction/_index.md`,
`wiki/theory/analysis/L165_consecutive_gap_growth_conjunction/_proof.md`,
`wiki/theory/analysis/L163_all_sequence_span_ratio/_index.md`,
`wiki/theory/analysis/L164_all_sequence_span_deviations/_index.md`, and the
selected formulation sections of `wiki/problems/analysis/E1221/_index.md`.
The preserved extracts specify the examined text; these identifiers do not
extend coverage to omitted sections or subsequent text.

**Grader.** Independent fresh-context grader, assigned model gpt-6-astra with
maximum reasoning effort, distinct from both the subject author and the
original reviewer. This grading context neither constructed nor previously
built on the subject. The commission charged the grader to find a mathematical,
contract or eligibility defect. Reading the original report and the reviewer's
own continuation was expressly part of grading that report; neither was
accepted as an instruction or as evidence of correctness by itself.

**Reviewer eligibility: PASS.** The original assignment was a distinct, fresh
review under a refutation charge. Its input contained the frozen mathematical
extracts and the permitted operating material, without author preparation or
an earlier assessment. The supplied original primary records support this
separation. The preliminary exchange contained an operating acknowledgement
and no mathematics. All 30 recorded examination calls were matched to their
returns; the displayed returns, supplied instructions and later continuations
were examined for their actual content. The continuations carry the reviewer's
own work. No incoming mathematical steering, excluded verdict, surrounding
mathematical search, other working context, or external source acquisition is
shown. The recorded reading and writing remain within the original assignment.

All five mathematical extracts were displayed completely before the substantive
assessment. The final report and keeper were also displayed completely. Initial
truncation affected operating reading; subsequent reads supplied the missing
required portions. Merely issuing a read command or computing an identity was
not counted as seeing the file. The final dependency file was assembled from
a fully displayed earlier selection and a fresh, displayed equality comparison
of the complete selected interfaces; this distinction is retained in the
provenance assessment. Its bytes agree with the final observation.

The original empty subscription observations support the recorded separation;
they do not establish that an uninspected communication store was empty. The
narrow settings corroborate the declared model and isolation route but are not
a substitute for the actual-read audit. No excluded exposure is identified in
the supplied record, so there is no exposure requiring an immateriality waiver.
The ruling concerns the supplied complete primary record of this examination;
it does not purport to observe unrecorded conduct or inaccessible internal
reasoning.

**Grading isolation: PASS.** The grader read the supplied frozen packet and
its original provenance, the identified operating rules, and the permitted
current dependency selection. No current L165 standing, surrounding
mathematical material, prior grade, author composition or outside source was
read. The input identities matched before use and the frozen originals remain
unchanged. Empty subscription observations support this reading record. No
excluded exposure occurred in this grading. The separate operational trust
comparison assigned to the commissioning authority is not certified here.

## Exact restatement and assertion rulings

Let $\mathcal A$ be all infinite sequences in $\mathbb R/\mathbb Z$, including
repetitions, and let $\mathcal D$ be its subfamily of sequences with distinct
terms. For positive integers $n\ge r$, retain all first-$n$ labels, order them
by position with arrival index breaking ties, and extend ordered lifts by
$y_{i+n}=y_i+1$. Define $M_n^{(r)}$ and $m_n^{(r)}$ as the maximum and minimum
of $y_{i+r}-y_i$ over all $n$ starting labels. These are forward sums of $r$
consecutive gaps on a circle of circumference one. If the minimum is zero,
the ratio is $+\infty$; the maximum is positive.

The exact quantifier order is
$\exists c\in\mathbb R_{>0}\ \exists r_0\in\mathbb Z_{>0}\
\forall r\in\mathbb Z_{\ge r_0}\ \forall X\in\mathcal A$.
For this one pair of absolute constants the three separate assertions are

$$
\limsup_n(nM_n^{(r)}-r)\ge c\sqrt{\log r},\qquad
\limsup_n(r-nm_n^{(r)})\ge c\sqrt{\log r},\qquad
\limsup_n\frac{M_n^{(r)}}{m_n^{(r)}}
\ge1+\frac{\log r}{200r}.
$$

The logarithm is natural. Each limit holds $r$ fixed and uses integer $n\ge r$.
No common subsequence or uniform onset time in $n$ is asserted. For either
$\mathcal F=\mathcal A$ or $\mathcal F=\mathcal D$, the quantities are

$$
\Lambda_r^{\mathcal F}=\inf_{X\in\mathcal F}\limsup_n nM_n^{(r)},\qquad
\lambda_r^{\mathcal F}=\sup_{X\in\mathcal F}\liminf_n nm_n^{(r)},\qquad
\mu_r^{\mathcal F}=\inf_{X\in\mathcal F}\limsup_n
\frac{M_n^{(r)}}{m_n^{(r)}}.
$$

Optimization follows each sequence limit. The sequence may depend on $r$;
$c$ and $r_0$ may not. For every integer $r\ge r_0$ the claimed bounds are

$$
\Lambda_r^{\mathcal F}-r\ge c\sqrt{\log r},\qquad
r-\lambda_r^{\mathcal F}\ge c\sqrt{\log r},\qquad
r(\mu_r^{\mathcal F}-1)\ge\frac{\log r}{200}.
$$

Each expression tends to $+\infty$ through the positive integers, for each
family. In particular the $\mathcal A$ conclusions answer the supplied
mean-normalized modified Statement. This is the original report's scope.

| Examined assertion | Grade | Accepted scope and reason |
| --- | --- | --- |
| Cyclic definitions, multiplicity and positivity of the maximum | PASS | The exact span sum is $r$, including zero gaps and the closing gap. No $0/0$ arises. |
| One absolute real $c>0$ and integer $r_0$ for the conjunction | PASS | The maximum of the two premise thresholds is independent of both $X$ and $r$; increasing it to at least two preserves eventual scope. |
| Upper-span deviation limsup | PASS | Exactly L164's first universal clause in the same model. |
| Lower-span deviation limsup | PASS | Exactly L164's second, separate universal clause; no simultaneous-time strengthening. |
| Ratio limsup with coefficient $1/200$ | PASS | Exactly the independent L163 clause, including the zero-minimum convention. |
| Tail identities converting deviations | PASS | Translation by finite $r$ and reversal to a limit inferior are derived from tail suprema and infima. |
| Bound for $\Lambda_r^{\mathcal F}-r$, both families | PASS | Infimum of values each at least $r+c\sqrt{\log r}$. |
| Bound for $r-\lambda_r^{\mathcal F}$, both families | PASS | Supremum of values each at most $r-c\sqrt{\log r}$. |
| Bound for $r(\mu_r^{\mathcal F}-1)$, both families | PASS | Infimum of actual paired-ratio limsups, followed by multiplication by positive $r$. |
| Restriction from $\mathcal A$ to $\mathcal D$ | PASS | Both infima increase and the supremum decreases. Only these inequalities are established. |
| Divergence of $\Lambda_r^{\mathcal F}-r$, both families | PASS | The uniform lower bound exceeds every real target for all sufficiently large integer $r$. |
| Divergence of $r-\lambda_r^{\mathcal F}$, both families | PASS | The same target argument applies after the correctly directed supremum bound. |
| Divergence of $r(\mu_r^{\mathcal F}-1)$, both families | PASS | The logarithmic lower bound has the required eventual divergence. |
| Auxiliary real finiteness and nonempty families | PASS | The keeper's single explicit distinct dyadic sequence gives $r\le\Lambda\le2r$, $r/2\le\lambda\le r$, $1\le\mu\le2$. Individual sequence limsups may remain infinite. |
| Coincident-point and full-turn calculations | PASS | The keeper counts exactly $r$ unit spans for the constant sequence when $n>r$; at $n=r$ every span is one. |
| Dyadic-prefix attack and its claimed discrimination | PASS | The specified single sequence has exact-grid deviations zero, but infinitely many intermediate prefixes with deviations $r/2,r/4$ and ratio two. |
| Delayed scalar and alternating-time diagnostics | PASS | They refute the indicated inference rules. The report expressly makes no claim that these scalar families are circle sequences. |
| Implication for the supplied modified Problem 1221 | PASS | The supplied Notes fix the $r$-gap/start-label convention, all-sequence family and normalization used by L165. |
| Original report's full mathematical verdict | PASS | **refutation-failed** for the preserved conjunction and exact implication, with the two native interfaces at their recorded standing. |
| Original reconstruction and preservation assertions | PASS | The exact originals and manifests agree; the analytic reconstruction uses retained mathematical inputs and no missing executable. |
| Original independence and coverage assertions | PASS | Supported at the expressly stated reading depth by the original primary record, including repaired operating-read truncation and the final interface comparison. |

These are rulings on assertions already made in the original delivery, not new
claim identifiers or a replacement examination. Outside-scope historical,
stronger-constant, optimality, attainment, family-equality and kernel assertions
receive no mathematical warrant from this grade.

## Assessment of the weakest steps and strongest attacks

The grader reproduced the indispensable keeper reasoning below to test the
existing examination. None of these calculations supplies a new premise or
repairs the frozen proof.

### Objects, boundary cases and the geometric attack

For the keeper's $g_i=y_{i+1}-y_i$, periodicity gives $g_i\ge0$ and
$\sum_{i=1}^n g_i=1$. In
$\sum_i\sum_{j=0}^{r-1}g_{i+j}$ each gap occurs once for each of the $r$
values of $j$. Therefore the sum of spans is exactly $r$, and
$0\le m_n^{(r)}\le r/n\le M_n^{(r)}\le1$. This establishes the definitions
without relying on an unproved catalog assertion. Rotation permutes the spans;
coincident labels are retained. At $n=r$ the lifted span is one even though
its endpoint residues agree. Shortest circle distance would give a different
observable and fails this check.

For the constant repeated sequence and $n>r$, one gap is one and the others
are zero. Exactly $r$ spans contain the unit gap. The keeper's values
$M=1$, $m=0$, deviations $n-r,r$, and infinite ratio follow exactly. The
bounded second deviation creates no contradiction: for fixed real $c>0$,
$c\sqrt{\log r}\le r$ eventually.

The dyadic sequence in keeper Section 2 is a realizable attempt to defeat the
universal claim. Between a grid of $N=2^k$ points and the next complete grid,
every gap is either $1/N$ or $1/(2N)$. Hence each span lies between
$r/(2N)$ and $r/N$. For $N\le n<2N$ this gives $nm\ge r/2$,
$nM<2r$ and $M/m\le2$. Along complete grids all deviations vanish and the
ratio is one. After the first $N/2$ midpoint insertions, the two contiguous
runs have $N$ short gaps and $N/2$ long gaps. When $N\ge2r$, each run contains
$r$ gaps, giving $M=r/N$, $m=r/(2N)$ at $n=3N/2$. The exact deviations are
$r/2$ and $r/4$, and the ratio is two. The reported liminf counterexample and
failed limsup attack are therefore valid. This same witness establishes the
claimed finite outer extrema, without asserting their exact values.

### Tail identities, uniformity and outer optimization

At fixed $r$, let $u_n=nM_n^{(r)}$ and $v_n=nm_n^{(r)}$. The second sequence
lies in $[0,r]$. On each tail,

$$
\sup_{n\ge K}(u_n-r)=\sup_{n\ge K}u_n-r,\qquad
\sup_{n\ge K}(r-v_n)=r-\inf_{n\ge K}v_n.
$$

The first identity remains valid at an infinite supremum; the second uses
only bounded real quantities. Passing to the limits of the tails proves
exactly the two identities used in the report. In particular the lower-span
conclusion concerns $\liminf v_n$. There is no replacement by a limsup and
no indeterminate subtraction of infinities.

Set $a=c\sqrt{\log r}$ and $b=\log r/200$. For each $X$, the consumed
interfaces give $U_X\ge r+a$, $V_X\le r-a$, and $Q_X\ge1+b/r$, where
$U_X,V_X,Q_X$ are the three sequence limits. Taking the indicated outer
infimum, supremum and infimum retains these inequalities. A strict violation
by an outer extremum would force some member to violate the same common
bound. This holds even when an extremum is unattained or the selected sequence
changes with $r$. Restriction to $\mathcal D$ has the directions printed in
the proof; subtracting its supremum from $r$ reverses that inequality once.
No quotient of separately optimized numerator and denominator appears.

The strongest attack in the original report targets precisely an illicit
exchange of these operations. For the keeper's
$f_k(n)=0$ when $n<k$ and $f_k(n)=a>0$ otherwise, each individual limsup is
$a$, while for every finite $n$ the pointwise infimum over $k$ is zero.
Thus $\inf_k\limsup_n f_k(n)=a$ and
$\limsup_n\inf_k f_k(n)=0$. For $h_k=r-f_k$ with $0<a\le r$, the
corresponding values are $r-a$ and $r$. This exact diagnostic exposes the
failure mechanism; it is not asserted to satisfy the geometric constraints.
It cannot defeat the frozen proof, which applies a bound to each infinite
sequence before optimizing. The geometric dyadic attack supplies an actual
circle-sequence test alongside this scalar diagnostic. Together they are
substantive attacks, not agreement with a displayed answer.

### Conjunction, divergence and the formulation bridge

The two deviation clauses share the absolute $c$ supplied by L164. L163's
threshold and L164's threshold can be replaced by their maximum. This operation
does not intersect witnessing subsequences. Alternating scalar excursions, as
specified in the keeper, indeed have positive separate limsups and a zero
pointwise minimum; that rejected inference is absent here. The logarithmic
ratio improvement is supplied by L163. The square-root deviations alone yield
only corresponding square-root-scale ratio information through the mean
inequality, so the report correctly identifies the ratio premise as essential.

For every real $T>0$, all integers $r$ sufficiently larger than $r_0$,
$\exp((T/c)^2)$ and $\exp(200T)$ satisfy $a>T$ and $b>T$. This verifies
each stated divergence, with no monotonicity assertion and no exchange of the
$n$ and $r$ limits. It also checks the distinction between a real target and
the integer eventual range.

The catalog extract's modified Statement and Notes specify circumference one,
forward spans through $r$ gaps, extrema over cyclic starting labels and outer
extrema over all infinite sequences after the sequence limits. The Notes
resolve the displayed maximum/minimum subscripts and the phrase about
consecutive points at exactly this convention. The algebraic identities
$r(\Lambda_r/r-1)=\Lambda_r-r$ and
$r(1-\lambda_r/r)=r-\lambda_r$ give the stated normalized coordinates.
The ratio coordinate is already $r(\mu_r-1)$. Thus the claimed implication
has the correct domain, operation order and units. The supplied text's
historical explanation is not needed to establish that correspondence.

## Premises and current reading

The consumed list is derived from the frozen proof and every consequence:
exactly **L163 and L164**. L163 supplies the ratio clause for every sequence,
and L164 supplies both separate deviation clauses with one absolute positive
constant. The other deductions are the elementary identities and order
arguments assessed above. The catalog is the specified formulation target,
not an additional native theorem or external-source premise.

The original final reading was on 2026-10-15 at 22:26:35.670409 UTC. The grader's
permitted current reading was on **2026-10-16 at 03:50:41.816039 UTC**. It was
restricted to each premise's `id`, `status`, `tier`, `standing`, `depends_on`,
complete statement, Conventions and scope, and exact generated row in
`wiki/standing.md`.

| Premise | Status | Tier | Standing | Declared dependencies | Comparison with the frozen interface |
| --- | --- | --- | --- | --- | --- |
| L163 | proved | 1 | field absent; generated row empty | `[]` | Complete statement agrees after YAML block-scalar dedent; conventions and exact row agree. |
| L164 | proved | 1 | field absent; generated row empty | `[]` | Complete statement agrees after YAML block-scalar dedent; conventions and exact row agree. |

All selected fields also agree with the original final observation. No stale
mark, changed premise, missing field needed by the application or pending tier
was returned. This discharges the current-standing condition at this reading.
It does not certify undisplayed acceptance narratives or future standing.

The interfaces agree on repeated terms, tie order, lifts, $r$ forward gaps,
integer $n\ge r$, natural logarithms and absolute parameter dependence. L163
has the exact extended-ratio convention. L164 requires no division by a
minimum. Their half-open counting-arc conventions are recorded but no lemma
from their omitted proofs is consumed. No full premise proof re-audit or
batch promotion is part of this grade. No external classical-paper theorem,
historical quotation or source-credit assertion is used as a premise; original
publication reading depth is unread.

## Complete report-contract rulings

The governing requirements are `docs/verification.md`, Report contract,
Whole-claim report, Independence and the assignment, and Grading and claim
standing, together with its verification adapter. The original report uses
identifiable sections for all seven governing parts.

| Contract part | Grade | Finding |
| --- | --- | --- |
| Subject and independence | PASS | Exact frozen subjects, dates, conventions, paths, exclusions and actual reading are stated and supported by original provenance. Reviewer and grader are distinct eligible contexts. |
| Restatement | PASS | Every quantifier, model convention, limit direction, optimization order, family qualification and eventual domain is preserved. |
| Checklist | PASS | All ten governing items, seven shared modes and twelve named patterns receive explicit findings, assessed below. |
| Weakest steps | PASS | Three consequential steps are independently derived: tail identities, extrema in their own units, and uniform conjunction with the formulation bridge. |
| Strongest attack | PASS | Delayed near-optimization targets a real invalid exchange, with exact diagnostic values; the realizable dyadic attack and boundary cases test the geometric scope. Their failure against the actual statement is explained. |
| Premises | PASS | The consumed list is complete, interfaces have the needed clauses, and the original and current permitted readings satisfy standing. Source and proof-depth boundaries are explicit. |
| Verdict and grading | PASS | The complete mathematical verdict is **refutation-failed**, without an asserted disproof, self-grade or strengthened conclusion. This distinct grade records acceptance at the same scope. |

### Governing Erdos checklist

| Item | Grade | Assessment of the original finding |
| --- | --- | --- |
| Quantifiers and scope | PASS | Universal sequence scope comes from the premises; only sufficiently large integer $r$ is claimed. Repetitions, zero minima, separate limsups and finite-prefix removal are explicit. |
| Circularity | PASS | The composition uses L163/L164 at their accepted interfaces and elementary deductions; it never assumes L165 to establish them. Their proofs are outside the commissioned depth. |
| Model and convention changes | PASS | Actual lifted spans are retained; no shortest-distance, distinct-only or averaged model is substituted. The modified formulation is explicitly identified. |
| Finite and statistical overreach | PASS | Exact examples discriminate inference rules and establish existence, without proving universal asymptotics by samples. Statistical and correlated-sample inference are inapplicable. |
| Uniformity | PASS | Constants are absolute; onset times may depend on $X,r$. No limit/extremum exchange or common witnessing time is used. |
| Extremal conclusions | PASS | Bounds use the exact three coordinates. Nonemptiness and real finiteness are witnessed; attainment, optimality and equality of family extrema are not asserted. |
| Consequences and composition | PASS | Each extremal bound, restriction inequality, divergence, positivity assertion and formulation implication is checked separately. No required interface clause is missing. |
| Computation | PASS | Correctly inapplicable to the mathematical warrant: there is no numerical algorithm, enumeration, enclosure or capped mathematical routine. Mechanical provenance comparisons confer no mathematical credit. |
| Reproduction | PASS | Keeper Section 7 reconstructs all required analytic steps from preserved inputs. No missing executable or cached numerical result is needed. |
| Source and verdict fidelity | PASS | The report's exact modified-formulation match and full verdict agree with its evidence. Original-publication fidelity is expressly unexamined. This grade characterizes the original report itself, not uninspected acceptance prose. |

### Shared canonical failure modes

| Mode | Grade | Assessment |
| --- | --- | --- |
| Almost all upgraded to all | PASS | Every consumed bound already covers every sequence; no exceptional family is discarded. |
| Induction presupposing termination | PASS | Inapplicable to the conjunction; each stage of the auxiliary dyadic construction is explicitly finite. |
| Probabilistic or averaging heuristic presented as proof | PASS | The mean bound is an exact double count over actual gaps. No probabilistic inference occurs. |
| Circular use of an equivalent statement | PASS | The two accepted native premises and the elementary order deductions have explicit roles; the conclusion is not its own premise. |
| Exceptional sets dropped from density arguments | PASS | Inapplicable: no density argument or discarded repeated-point class occurs. |
| Finite verification cited beyond its coverage | PASS | The examples have only their stated diagnostic and existence roles. |
| Relaxed or averaged convergence substituted for actual objects | PASS | Every sequence limit uses its actual extremal spans and actual paired ratio. The mean identity is not a surrogate dynamical model. |

### Named patterns

| Pattern | Grade | Assessment |
| --- | --- | --- |
| Model-class transport instead of entailment | PASS | No axiom-system extension is classified. Family restriction uses literal inclusion; the formulation bridge identifies the same quantities and quantifiers. |
| Infinite-family uniformity from finite instances | PASS | Absolute constants are inherited from the universal premise clauses, never inferred from the examples. |
| Extremal claims in their own units | PASS | The three normalized coordinates and the ratio formed before optimization are checked explicitly. |
| Consequence sentences are claim surfaces | PASS | All mathematical consequences in the selected proof and keeper are covered in the assertion table. Historical source claims are outside the reported warrant. |
| Hypotheses carried through quantified arguments | PASS | Fixed $r$, nonempty families, positive maximum and bounded scaled minima are established; no hidden attainment, onset uniformity or scalar realizability is assumed. |
| Composition inherits its unproved premises | PASS | Both actual consumed interfaces supply every needed clause at the recorded current standing. No source proof is silently claimed as re-audited. |
| Reproducibility notes are claims | PASS | The retained definitions and keeper instructions suffice for the analytic reconstruction performed here. There is no mathematical execution command to replay. |
| Verifier quotations are claims | PASS | Inapplicable within the original blind mathematical input, which contained no previous verdict. Applicable to this grade: its characterization matches the complete original report and keeper. No current card characterization is examined. |
| Verdict words spelled in full | PASS | The accepted ruling is **refutation-failed**, consistently distinct from **refuted-as-stated**. |
| Certified-bracket functions fail loudly | PASS | Inapplicable: no bracket function, numerical cap or period-window routine supports the verdict. |
| A checking leg needs a failing input | PASS | No executable mathematical leg exists. The written attacks discriminate concrete failures: full turns versus shortest distances, grids versus an all-prefix claim, delayed families versus exchanged limits. |
| A gate must rerun rather than read caches | PASS | Inapplicable to the mathematical warrant; no gate or cached output is offered as proof. Provenance was checked from original bytes and displayed returns, not only a success summary. |

Evidence coverage remains analytic composition from accepted native interfaces.
The statistical discipline is inapplicable. There is no computational batch or
second examination cycle requiring a structurally different numerical route.
This is grading of the existing examination, not a replacement cycle.

## Preservation, reproduction and limits

The exact original eight-file delivery, its original input and delivery
manifests, the historical reviewer's commission and continuation, and the
supplied complete primary provenance have been preserved without alteration.
Split originals were concatenated only in their declared order with no added
separator. Original input copies agree with the returned mathematical
extracts; the original delivery inventory agrees with the preserved originals.
All existing `[cut]` markers remain. No omitted source was reconstructed and
no later mathematical bytes are included in the accepted subject.

For mathematical reproduction from an ordinary clone, the eight linked files
are the complete required package. Read the statement, proof and premise
interfaces; verify the finite cyclic count and two dyadic prefix calculations
in keeper Sections 1–2; check the uniform quantifiers in Section 3; derive the
tail identities and order inequalities in Section 4; check each divergence and
family inequality in Section 5; and compare the exact modified Statement and
Notes with Section 6. Section 7 supplies that route in the original keeper.
The grader followed these derivations. No private program, numerical output or
original publication is needed for these mathematical checks. The primary
provenance supports the independence facts summarized here and is preserved
separately from the public mathematical evidence.

The original private mechanical success counts were not adopted as theorem
certificates. The grader independently matched calls and returns, inspected
displayed coverage, checked original custody and compared the permitted current
interfaces. Parser outputs distinguish displayed bytes from internal command
records and do not infer unread bytes from successful exit codes. The original
material is retained with those findings and their limits.

**Accepted scope.** PASS covers the whole frozen L165 examination, including
the conjunction, both families' extremal and divergence consequences, and the
implication at the supplied mean-normalized modified formulation. Its accepted
mathematical verdict remains **refutation-failed**. There is no unresolved
contract or mathematical coverage gap within that scope.

This grade does not re-audit L163/L164 proofs, certify historical wording or
source credit, answer the literal printed first two expressions, prove a
coefficient $1/100$, establish optimality, attainment or equality between
families, or grant Lean credit or catalog acceptance. It supplies no warrant
for text written after the frozen delivery. Preservation and filing must retain
the complete assessed package; a favorable summary alone is insufficient.

---
name: theory/analysis/L165_consecutive_gap_growth_conjunction/evidence/verify/whole_statement/report
title: Whole-statement examination of the consecutive-gap conjunction
desc: Whole-statement adversarial examination of L165 and its implication for the supplied mean-normalized modified E1221 formulation.
tags: []
sources: []
created: 2026-10-15T23:40:25Z
updated: 2026-10-15T23:40:25Z
---

# Whole-statement examination of the consecutive-gap conjunction

***

## Subject and independence

**Subject.** The complete selected mathematical statement, conventions and
proof of L165, including every extremal and divergence consequence and the
claimed implication for the supplied mean-normalized modified Statement of
E1221. The subject was frozen on 2026-10-15 at 21:10:27.616818 UTC and examined
on 2026-10-15 UTC. Its canonical identifiers are
`wiki/theory/analysis/L165_consecutive_gap_growth_conjunction/_index.md`,
`wiki/theory/analysis/L165_consecutive_gap_growth_conjunction/_proof.md`, and
`wiki/problems/analysis/E1221/_index.md`, the last restricted to the supplied
Statement, Statement (modified), Notes and Formulation text. The selected bytes
are preserved below; marked omissions are not part of the examined subject.

**Reviewer.** Independent fresh-context mathematical reviewer, assigned model
gpt-6-astra with maximum reasoning effort, neither an author of nor a
collaborator on the subject. This context had not previously constructed or
built on L165. Mathematical examination and independent derivations are
attributed to Plasma AI. This is a review, not a grade or tier assertion.

**Exact inputs and reading depth.** All five supplied mathematical extracts
were read in full:

| Preserved input | Examined content |
| --- | --- |
| [Claim](../../assets/whole_statement_subject/claim.md.txt) | Complete L165 statement and Conventions and scope, including consequence sentences. |
| [Proof](../../assets/whole_statement_subject/proof.md.txt) | Complete selected L165 mathematical argument. |
| [Premises](../../assets/whole_statement_subject/premises.md.txt) | Complete L163 and L164 statements and Conventions and scope; neither full proof. |
| [Frozen premise standing](../../assets/whole_statement_subject/premise_standing.md.txt) | Exactly the supplied L163 and L164 standing rows. |
| [Catalog formulation](../../assets/whole_statement_subject/catalog.md.txt) | Supplied formulation and contextual excerpts; no original publication or linked source was opened. |

The only live mathematical reading was the permitted selection of L163 and
L164 metadata, complete statements, Conventions and scope, and their exact
rows in `wiki/standing.md`. The
[selected live interfaces](../../assets/whole_statement_subject/live_dependencies.json)
preserve that reading and its comparison with the frozen premises. No full
underlying card, proof, verification narrative, other row, or own-standing
material was displayed. The dependency reading is detailed under Premises.

Operating reading comprised `README.md`; the introduction, Claims, Evidence,
Tiers and Erdos-specific Project claims of `docs/anatomy.md`;
`docs/verification.md`, `docs/approach_vetting.md`, `docs/evidence.md`,
`docs/math_authoring.md` and `docs/weaving.md` in full; `campaign/AGENTS.md`
and `campaign/guides/verification.md` in full; the Reading section of
`campaign/guides/research.md`; and `campaign/stations/surveyor/README.md`.
Root `AGENTS.md` was supplied as instructions. The exact operating charter,
steps, declared settings, installed operating guidance, selected-reading helper
and check scripts were inspected only as operating law. Their examples and
links supplied no mathematical premises or permission to expand the reading.
The declared settings and operating-file identities were checked against the
commissioned manifests before use.

**Isolation facts.** The first mathematical reading was the supplied frozen
extraction. The subject was never re-extracted from a card or changing tree.
Identity comparisons before and during the examination found the input bytes
unchanged. No author preparation, prior report, grade, other working context,
excluded correspondence, surrounding mathematical search or web content was
read. No excluded exposure occurred in this examination. The observed
subscription tables were empty at the initial, intermediate and final
boundaries; inbox contents were not inspected and are not inferred to be empty.
Isolation claims rest on these actual read facts, not on configuration flags
alone. The subject was not edited or repaired.

**Independent evidence.** The [analytic keeper](keeper.md) contains the full
derivations, concrete circle-sequence attacks and scalar diagnostics. Section 7
gives the reconstruction procedure using the preserved inputs. No numerical
search, author evidence program, executable mathematical checker, or kernel
proof is part of the verdict. Mechanical identity and text comparisons do not
serve as mathematical evidence.

## Restatement

Let $\mathcal A$ contain every infinite sequence of labeled points on the
unit-circumference circle, including repetitions. Let $\mathcal D$ contain
those sequences with pairwise distinct terms. For positive integers $n\ge r$,
sort the first $n$ labels by position and then arrival index, choose ordered
lifts within one turn, and extend them by $y_{i+n}=y_i+1$. Take the largest
and smallest of the $n$ forward spans $y_{i+r}-y_i$, denoting them by
$M_n^{(r)}$ and $m_n^{(r)}$. A zero minimum gives ratio $+\infty$;
the maximum is always positive. Every limit in $n$ holds $r$ fixed.

The assertion is that one absolute $c>0$ and one absolute integer threshold
$r_0$ work for every integer $r\ge r_0$ and every $X\in\mathcal A$:

$$
\limsup_n(nM_n^{(r)}-r)\ge c\sqrt{\log r},\qquad
\limsup_n(r-nm_n^{(r)})\ge c\sqrt{\log r},
$$

and

$$
\limsup_n\frac{M_n^{(r)}}{m_n^{(r)}}
\ge1+\frac{\log r}{200r}.
$$

The two one-sided limsups, and the ratio limsup, need not have a common
witnessing subsequence. Logarithms are natural. A sequence used in an
optimization may change with $r$; neither $c$ nor $r_0$ may do so.

For each nonempty family $\mathcal F\in\{\mathcal A,\mathcal D\}$,
form the outer extrema only after the sequence limits:

$$
\Lambda_r^{\mathcal F}=\inf_{X\in\mathcal F}
\limsup_n nM_n^{(r)},\qquad
\lambda_r^{\mathcal F}=\sup_{X\in\mathcal F}
\liminf_n nm_n^{(r)},\qquad
\mu_r^{\mathcal F}=\inf_{X\in\mathcal F}
\limsup_n\frac{M_n^{(r)}}{m_n^{(r)}}.
$$

For all integer $r\ge r_0$ the claimed consequences are

$$
\Lambda_r^{\mathcal F}-r\ge c\sqrt{\log r},\qquad
r-\lambda_r^{\mathcal F}\ge c\sqrt{\log r},\qquad
r(\mu_r^{\mathcal F}-1)\ge\frac{\log r}{200}.
$$

Each of these three expressions tends to positive infinity as $r$ tends to
infinity through the integers. The $\mathcal A$ conclusions answer exactly
the supplied modified Statement when read with its supplied Notes. There is no
assertion of small-$r$ bounds, optimal constants, attained extrema, or equality
of the $\mathcal A$ and $\mathcal D$ extrema.

## Weakest steps

### 1. Converting a lower deviation to the correct limit inferior

The cyclic gap sum gives $0\le v_n=nm_n^{(r)}\le r$. At every tail,

$$
\sup_{n\ge K}(r-v_n)=r-\inf_{n\ge K}v_n.
$$

Taking the limit over tails therefore gives
$\limsup_n(r-v_n)=r-\liminf_n v_n$, with no undefined infinity
arithmetic. A lower bound $a$ on this limsup is an upper bound $r-a$ on
the sequence's limit inferior. Replacing that limit inferior by a limit
superior would be unjustified. For the maximum, translation by the finite
number $r$ commutes with the limsup, including an infinite limsup. Keeper
Sections 1 and 4 derive both facts from the definitions.

### 2. Taking outer extrema in their own units

Fix $r$, set $a=c\sqrt{\log r}$ and $b=\log r/200$, and write
$U_X=\limsup nM_n^{(r)}$, $V_X=\liminf nm_n^{(r)}$ and
$Q_X=\limsup M_n^{(r)}/m_n^{(r)}$. The supplied universal bounds give
$U_X\ge r+a$, $V_X\le r-a$ and $Q_X\ge1+b/r$ for every $X$.
Thus their infimum, supremum and infimum, respectively, obey those same bounds
over either nonempty family. The ratio is formed for one sequence before
taking its infimum; no quotient of separately optimized quantities is used.

Restriction to $\mathcal D$ increases the two infima and decreases the
supremum. The sign of $r-\lambda$ consequently gives the required lower
bound. No attainment or equality between families is used. Keeper Section 2
also constructs one distinct sequence proving the outer quantities finite;
Sections 4 and 5 prove the order operations without exchanging a limit and an
outer extremum.

### 3. Uniform conjunction and the formulation bridge

L163 supplies an absolute threshold for the ratio; L164 supplies absolute
$c>0$ and a threshold for both separate deviations. Taking the maximum of the
thresholds gives an absolute common threshold. There is no intersection of
three sets of witnessing times. No uniform onset time in $n$ is assumed.

The modified Statement's supplied Notes define the observables as the largest
and smallest sums of $r$ consecutive gaps. They therefore identify its
displayed maximum and minimum with the extrema over starting labels, and its
distance with the forward lifted arc, rather than a shortest circle distance.
Its outer family and order of operations are the $\mathcal A$ definitions
above. The exact algebraic normalization is

$$
r(\Lambda_r/r-1)=\Lambda_r-r,\qquad
r(1-\lambda_r/r)=r-\lambda_r.
$$

Both these lower bounds and the ratio lower bound diverge in the stated units.
Keeper Sections 3, 5 and 6 check the quantifiers, eventual divergence and every
part of this dictionary. No assertion about an original publication is needed
for that implication.

## Strongest attack and other attempted refutations

The strongest compositional attack was to choose a different near-optimal
sequence for each $r$, with excursions occurring arbitrarily late, and use
that freedom to push an outer extremum below the claimed bound. This would
succeed against an argument that first optimized a finite prefix and then took
a limit. The keeper supplies exact delayed scalar families demonstrating that
the two orders of operations can disagree: an infimum of limsups equal to
$a>0$ can coexist with a limsup of pointwise infima equal to zero; the
supremum/liminf counterpart fails in the opposite direction. These diagnostics
are explicitly not claimed to be realizable circle sequences. They identify
the suspected invalid inference, rather than pretend to refute the geometry.

The attack fails against the frozen proof because the outer bounds are obtained
from an inequality already valid for every infinite sequence at that fixed
$r$. The defining order property of an infimum or supremum prevents any
member, including one selected separately for each $r$, from crossing the
common bound. No limiting exchange or common onset time is required. This
argument also covers unattained extrema and infinite individual limsups.

A concrete geometric attempt uses the distinct sequence obtained by successively
inserting dyadic gap midpoints from left to right. At $n=2^k\ge r$ all
spans have length $r/n$, so both deviations are zero and the ratio is one at
infinitely many prefixes. But at $n=3\cdot2^{k-1}$, for $2^{k-1}\ge r$,
the exact deviations are $r/2$ and $r/4$ and the ratio is two. This is an
actual counterexample to a stronger liminf or all-prefix version, and a failed
counterexample to the stated limsup version. The construction and exact gap
counts are preserved in keeper Section 2.

Other attacks addressed full turns at $n=r$, coincident labels and zero
minima, shortest-distance substitution, reversed subclass inequalities, use of
separate subsequences as a common one, derivation of the logarithmic ratio from
only the square-root deviation bounds, and accidental use of the printed
normalization. Keeper Sections 1, 3–6 retain their exact calculations and
failure mechanisms. None finds a defect in the frozen conjunction. These are
checks of the supplied composition; they do not re-audit either premise proof.

## Premises

The consumed native list was derived from the frozen proof and its consequence
sentences: exactly L163 and L164. L163 supplies the universal ratio bound with
coefficient $1/200$; L164 supplies the two separate universal deviation bounds
with one absolute positive constant. No other native proposition or external
literature theorem is needed by the implication to the supplied modified
Statement. Elementary cyclic counting, tail-limit identities, order properties
and logarithmic growth are derived in the keeper.

The live interfaces and exact standing rows were read on **2026-10-15 at
22:26:35.670409 UTC**, using the authorized selection of the then-current
commissioning tree. The selected metadata and `wiki/standing.md` rows agreed:

| Premise | Canonical statement path | Status | Tier | Standing field | Declared dependencies |
| --- | --- | --- | --- | --- | --- |
| L163 | `wiki/theory/analysis/L163_all_sequence_span_ratio/_index.md` | proved | 1 | absent; standing row empty | `[]` |
| L164 | `wiki/theory/analysis/L164_all_sequence_span_deviations/_index.md` | proved | 1 | absent; standing row empty | `[]` |

Both complete statement fields match the frozen premise text after removal of
YAML block-scalar indentation. Both Conventions and scope sections and both
standing rows match the supplied frozen interfaces. No changed interface,
missing required field, stale mark or pending tier was returned by the allowed
reading. The exact selected data and comparison are preserved in
[live_dependencies.json](../../assets/whole_statement_subject/live_dependencies.json).
This satisfies the commissioned current-premise requirement at this reading;
it is not a claim about undisplayed verification narratives or later standing.

The application uses the same family of all sequences, the same unit circle,
integer $n\ge r$, repeated labels and tie order, forward $r$-gap spans,
lift extension, logarithm, and separate limit quantifiers in both premises.
L163's zero-minimum ratio convention is exactly L165's. L164's application
divides by no minimum. The half-open counting-arc convention in the premise
interfaces is recorded but no counting theorem from their omitted proofs is
consumed here. This is not a batch review; the native premise proofs and their
independent acceptance records are taken at their permitted current standing,
not re-reviewed or self-promoted.

**Source boundary.** The catalog snapshot was read in full as supplied
formulation context. Its cited historical inequalities, source quotations,
normalization history and source-credit assertions were not checked against
the publications. Original-source reading depth is therefore unread, and no
external-source theorem is treated as independently verified here. The
formulation comparison uses the supplied modified Statement and Notes as its
specified target, not the truth of their historical explanations. No
unprovided source assertion is necessary to that comparison. The assertion
that the page records a normalization issue is supported by the supplied
Notes; the correctness of that historical account is outside this verdict.

## Checklist

The ten Erdos-specific items below govern the checklist. The following two
subsections also account explicitly for every shared canonical mode and named
pattern, without treating the absence of a computation or an excluded source
audit as successful coverage of it.

### Erdos-specific checklist

| Item | Finding |
| --- | --- |
| Quantifiers and scope | No defect found. One absolute pair of constants works for all sufficiently large integer $r$ and every sequence. Limits hold $r$ fixed, discard only the finite prefix $n<r$, and require no common subsequence. The exact-grid example distinguishes limsup from liminf. |
| Circularity | No defect found in the assessed composition. The only native premises are L163 and L164 at their supplied interfaces; their live dependency metadata is empty. The cyclic identity, limit identities and extremal deductions do not assume L165. Premise proofs were not re-audited. |
| Model and convention changes | No defect found relative to the supplied conventions. Repeated labels, wraparound, full turns, forward $r$-gap spans and the all-sequence family are retained. The modified-formulation dictionary is explicit; original-source fidelity is outside scope. |
| Finite and statistical overreach | No defect found. The universal argument is analytic from the two interfaces. Concrete examples test failure modes and supply one existence witness, never universal statistical evidence. No sampling or correlation inference occurs. |
| Uniformity | No defect found. Only the maximum of two absolute thresholds is taken. Sequence-dependent onset times, separate optimizing sequences for different $r$, and nonattainment are all allowed. No limit, sum or outer extremum is interchanged improperly. |
| Extremal conclusions | No defect found. The infima, supremum and ratio are checked in the exact mean-normalized units. Nonemptiness and finiteness have an explicit distinct-point witness. No attainment, optimality or equality of family extrema is claimed. |
| Consequences and composition | No defect found. Each family bound, each divergence, the positivity assertion and the modified-question consequence are separately derived. Every consumed native clause is supplied at the required strength. |
| Computation | Inapplicable as a mathematical evidence mode: no numerical algorithm, finite enumeration, certificate, enclosure or resource-limited computation carries the verdict. All exact calculations are exposed in the keeper. |
| Reproduction | Analytic reconstruction is supplied in keeper Section 7, with exact frozen inputs and complete example specifications. There is no mathematical rerun command or cached computational success on which the verdict relies. |
| Source and verdict fidelity | The match to the supplied modified formulation is checked, with its interpretive conventions stated. Original-source claims and previous-verifier characterizations are excluded and unverified. This report uses full verdict words and asserts no grade. |

### Shared canonical failure modes

1. **Almost all upgraded to all:** no defect found. Both consumed universal
   interfaces already quantify over every sequence; no exceptional set is
   discarded.
2. **Induction presupposing termination:** inapplicable to the frozen proof.
   The auxiliary dyadic construction uses finitely many insertions at each
   explicitly finite stage; its existence does not presume a limiting claim.
3. **Probabilistic or averaging heuristics as proofs:** no defect found. The
   mean-span inequality follows from an exact finite double count, not an
   expectation, typical-case heuristic or probabilistic estimate.
4. **Circular use of an equivalent statement:** no defect found in the
   composition. The two native universal bounds are explicit accepted
   premises, not covertly inferred from L165; the derived outer-extremum
   assertions are proved by order. Omitted premise proofs are outside scope.
5. **Exceptional sets dropped from density arguments:** inapplicable. There
   is no density argument or removed sequence class; repetitions remain.
6. **Finite verification extended beyond base coverage:** no defect found.
   The examples are not offered as verification over all sequences or all
   parameters. The universal conclusion comes from the quantified interfaces
   and analytic deductions.
7. **Relaxed or averaged convergence substituted for actual objects:** no
   defect found. The finite mean inequality is only an inequality about the
   actual spans. All limiting functionals use the actual extrema, including
   actual paired ratios for each sequence.

### Named patterns

1. **Model-class transport instead of entailment:** no unsupported transport
   found. No axiom-system extension or certificate-class classification occurs.
   The only family comparison uses literal set inclusion, and the formulation
   bridge identifies the same observables and quantifiers.
2. **Infinite-family uniformity from finitely many instances:** no defect
   found. The constants are inherited from explicitly universal premise
   interfaces; the examples do not establish them.
3. **Extremal claims in their own units:** no defect found. Each bound is
   checked as $\Lambda-r$, $r-\lambda$, or $r(\mu-1)$, without replacing
   ratio extrema by separate optimizations or neighboring absolute quantities.
4. **Consequence sentences are claim surfaces:** no defect found. Positivity,
   the family bounds, restriction inequalities, three divergences and exact
   modified-question implication are all checked. The source-history boundary
   is expressly excluded rather than silently included in the conclusion.
5. **Hypotheses carried through quantified arguments:** no defect found.
   Nonempty families, fixed $r$ during each limit, bounded scaled minima and
   positive maximum are established. No global onset time or realizability of
   the scalar diagnostics is assumed.
6. **Composition inherits unproved premises:** no missing consumed clause
   found. L163 and L164 supply exactly the universal interfaces used and both
   have current tier 1 with no stale mark in the permitted reading. Their full
   proofs are not claimed as newly verified.
7. **Reproducibility notes are claims:** no computational reproducibility
   assertion is made. The keeper's reconstruction procedure names retained
   inputs and reconstructs the finite identities and order argument without
   an external or private executable input.
8. **Verifier quotations are claims:** inapplicable within the blinded
   subject. Own-standing text and prior reports were excluded. Their
   characterization is not certified; no prior verifier ruling is quoted.
9. **Verdict words spelled in full:** satisfied. The verdict is
   **refutation-failed**; no ambiguous initials or self-grading are used.
10. **Certified brackets fail loudly:** inapplicable. No bracket routine,
    floating-point bound, iteration cap or period-window computation is used.
11. **A harness leg needs a failing input:** inapplicable to executable
    mathematics because no such leg exists. The analytic attacks have concrete
    discriminatory examples: complete grids defeat the liminf replacement,
    full turns defeat shortest distances, and delayed scalar families defeat
    interchanged optimizations.
12. **Caches cannot substitute for re-execution:** inapplicable to the
    mathematical warrant. No gate result or cached computation is relied on.
    Identity comparisons support input provenance only, not theorem truth.

The neighboring correlated-sample discipline is inapplicable: there is no
statistical inference. Evidence coverage is explicitly separated between
analytic composition, concrete diagnostic examples, accepted native premise
interfaces, and unexamined original sources.

## Verdict and grading

**refutation-failed.** Under the commissioned reliance on L163 and L164 at
their supplied and matching live interfaces, the complete frozen L165
statement and proof survive the documented attacks. The two premises meet the
required current standing at the recorded reading. No false clause, invalid
deduction or missing load-bearing interface was found. The conjunction proves
the three requested divergences for the supplied mean-normalized modified
Statement over all infinite circle sequences, and also supplies the stated
distinct-family consequences.

This verdict does not re-audit L163 or L164, certify an original publication's
wording or historical interpretation, settle source credit, or answer the
literal printed first two expressions in place of the specified modified
question. It certifies no stronger coefficient, optimality, attained extremum,
equality between sequence-family extrema, or formal proof. It concerns only
the preserved frozen bytes, not later changes to the statement or argument.

No grade, claim promotion or catalog acceptance is asserted here. A distinct
eligible grader must judge the full report contract and independence and record
pass or void. The report, keeper and exact mathematical snapshots together are
the review product; a short favorable summary is not a substitute for them.

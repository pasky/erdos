---
name: theory/analysis/L164_all_sequence_span_deviations/evidence/verify/whole_statement/report
title: "Whole-statement review of the one-sided discrepancy bounds"
desc: Whole-statement adversarial examination of the two supplied all-sequence one-sided discrepancy bounds and their separate extremal consequences.
created: 2026-10-15T20:39:29Z
updated: 2026-10-15T20:39:29Z
---

# Whole-statement review of the one-sided discrepancy bounds

***

## Subject and independence

**Reviewer:** an independent mathematical reviewer in a fresh context, with
model disclosed as `gpt-6-astra`. The reviewer neither authored nor
collaborated on the supplied argument and had not previously built on it in
this context. The assignment was to find a counterexample, invalid inference,
missing essential hypothesis, or canonical failure mode, rather than to
confirm the author's conclusion. This is a mathematical examination, not a
grade or an author repair.

**Examination date:** 2026-10-15. **Subject freeze:**
2026-10-15T09:49:19.072889+00:00. The exact subject is the supplied prepared
extraction, preserved verbatim in the files below. The
[supplied subject manifest](../../assets/whole_statement/returned/assets/review/subject/manifest.json) records its scope,
conventions, selected source ranges and cut marker. Its payload identities
were checked before examination and after preservation. The frozen subject
was not changed. These checks establish agreement with the supplied packet;
the canonical pages were not opened to independently reconstruct that packet.

The table gives the manifest's canonical locators. A coordinate range has an
inclusive beginning and an exclusive end. Every listed payload was read in
full, including its proofs; a selected range is not a claim to have read the
entire canonical page.

| Preserved payload | Canonical source and selected range |
| --- | --- |
| [Catalog statement](../../assets/whole_statement/returned/assets/review/subject/catalog_statement.md.txt) | `wiki/problems/analysis/E1221/_index.md`, 25:1 to 95:1; the two Statement sections |
| [Model and theorem](../../assets/whole_statement/returned/assets/review/subject/model_and_theorem.md.txt) | `wiki/research/erdos_1221/all_sequence_composition.md`, 31:1 to 86:1; Target, model, quantifiers and composed theorem |
| [Lemma 2.1](../../assets/whole_statement/returned/assets/review/subject/lemma_2_1.md.txt) | `wiki/research/erdos_1221/ko26b_lemma_2_1_reconstruction.md`, 28:1 to 246:1; definitions, hypothesis, both comparisons and uniformity proof |
| [All-sequence transfers](../../assets/whole_statement/returned/assets/review/subject/all_sequence_transfer.md.txt) | `wiki/research/erdos_1221/all_sequence_composition.md`, 141:1 to 150:1, 166:1 to 189:24, and 193:1 to 197:1; labels/lifts, covering, localization and positivity, with the supplied cuts |
| [Closing comparisons](../../assets/whole_statement/returned/assets/review/subject/one_sided_comparison.md.txt) | `wiki/research/erdos_1221/all_sequence_composition.md`, 249:1 to 272:1; The one-sided parts |
| [Lemma 6.1](../../assets/whole_statement/returned/assets/review/subject/lemma_6_1.md.txt) | `wiki/research/erdos_1221/ko26b_lemma_6_1_reconstruction.md`, 27:1 to 115:1; definitions, statement and entire proof |
| [Lemma 6.2](../../assets/whole_statement/returned/assets/review/subject/lemma_6_2.md.txt) | `wiki/research/erdos_1221/ko26b_lemma_6_2_reconstruction.md`, 31:1 to 163:1; definitions, statement and entire proof |
| [Lemma 6.3](../../assets/whole_statement/returned/assets/review/subject/lemma_6_3.md.txt) | `wiki/research/erdos_1221/ko26b_lemma_6_3_reconstruction.md`, 27:1 to 99:1; definitions, statement and entire proof |
| [Proposition 6.4](../../assets/whole_statement/returned/assets/review/subject/proposition_6_4.md.txt) | `wiki/research/erdos_1221/ko26b_proposition_6_4_reconstruction.md`, 32:1 to 136:1; definitions, statement and entire proof |
| [Lemma 7.2](../../assets/whole_statement/returned/assets/review/subject/lemma_7_2.md.txt) | `wiki/research/erdos_1221/ko26b_lemma_7_2_reconstruction.md`, 40:1 to 182:1; definitions, Theorem 7.1 interface, statement and entire proof |
| [Local planar proof](../../assets/whole_statement/returned/assets/review/subject/halasz_bound.md.txt) | `wiki/research/erdos_1221/halasz_planar_l1_bound.md`, 34:1 to 183:1 and 200:1 to 219:1; entire theorem proof and Anchored-box conventions |
| [Provenance and scope](../../assets/whole_statement/returned/assets/review/subject/provenance_and_scope.md.txt) | Supplied bibliographic and scope map; no canonical mathematical page was substituted for it |

The manifest itself was also read in full. This is the complete mathematical
read set. Links, source markers and bibliography entries were used only as
locators. No author's plans or memory, prior verdict, native claim ledger,
canonical mathematical page, full-page original, external paper, internet
search, or other review context was consumed. There was no excluded
communication or search exposure. Subscription checks returned an empty table;
the accepted operating settings specified blind, sealed, local operation
without synchronization or descendants. No messages or feeds were read, and
no additional reviewer was delegated work. These observations support
isolation; the empty subscription table alone is not claimed to prove it.

The separately frozen operating files were checked against their supplied
manifest before reliance. The repository operating reading was: `AGENTS.md`
as supplied by the harness; `README.md`, `docs/verification.md`,
`campaign/AGENTS.md`, and `campaign/guides/verification.md` in full;
`docs/anatomy.md` at Claims, Evidence, Tiers and Erdos-specific Project
claims; and only Reading in `campaign/guides/research.md`.
`docs/evidence.md`, `docs/math_authoring.md` and `docs/weaving.md` were
also read in full. The permitted generated charter, three core steps,
effective settings, command help and runtime/continuation skill documents
were read; the four supplied scripts were inspected without execution.
The template's source and pin fields were inspected. The live agent
configuration was excluded. No examples or links in operating documents
expanded the mathematical read set.

The independent reasoning and exact symbolic attack inputs are retained in
[review_derivations.md](review_derivations.md). No mathematical verification depends on
software, a numerical experiment, a compiler, a cached result or an author's
checker. The report below incorporates those derivations separately for each
of its four conclusion surfaces.

## Restatement of each conclusion

The circle is $\mathbb T=\mathbb R/\mathbb Z$ with circumference one.
For every infinite sequence $X=(x_i)_{i\ge1}$, repetitions permitted, order
the first $n$ labels by position and then by index at ties. On the real
periodic lift $y_{i+n}=y_i+1$, the $r$-span for $n\ge r$ is
$y_{i+r}-y_i$. Its maximum and minimum over the $n$ starting labels are
$M_n^{(r)}$ and $m_n^{(r)}$. The $n$ nonnegative gaps sum to one, and the
$n$ spans sum to $r$. Counts include multiplicity; counting arcs are
oriented $(x,x+\ell]$ with $\ell<1$. Span arcs of length zero and one
retain their empty-arc and full-turn meanings. All logarithms here are
natural.

The four surfaces examined are the following. The same absolute $c>0$ and
absolute integer $r_0$ serve all of them.

**Upper sequence theorem.** For every integer $r\ge r_0$ and every such
sequence $X$,

$$
\limsup_{n\to\infty}\bigl(nM_n^{(r)}-r\bigr)
\ge c\sqrt{\log r}.
\tag{U}
$$

**Lower sequence theorem.** For every integer $r\ge r_0$ and every such
sequence $X$,

$$
\limsup_{n\to\infty}\bigl(r-nm_n^{(r)}\bigr)
\ge c\sqrt{\log r}.
\tag{L}
$$

The two large deviations need not occur at the same times. The sequence may
be chosen differently for each $r$. Constants and $r_0$ cannot depend on
that choice; the onset in $n$ of a contrary eventual hypothesis may depend
on it.

**Infimum consequence and its divergence.** With
$\Lambda_r=\inf_X\limsup_n nM_n^{(r)}$ over precisely the same family,
for every integer $r\ge r_0$,

$$
\Lambda_r-r\ge c\sqrt{\log r},
\qquad \Lambda_r-r\longrightarrow+\infty\quad(r\to\infty).
\tag{I}
$$

**Supremum consequence and its divergence.** With
$\lambda_r=\sup_X\liminf_n nm_n^{(r)}$, for every integer $r\ge r_0$,

$$
r-\lambda_r\ge c\sqrt{\log r},
\qquad r-\lambda_r\longrightarrow+\infty\quad(r\to\infty).
\tag{S}
$$

The last limits are through positive integers. These are the supplied
modified first two expressions. The ratio assertion and $M/0$ convention
were read as context, but no ratio verdict is given. The literal original
first two growth expressions and equality of the constants for distinct
versus unrestricted sequences are outside this examination.

## Weakest steps and their composition

### 1. Transport under only one-sided control

The precise danger is to reuse Lemma 2.1 with an unjustified two-sided
error budget. The two exact gap configurations in derivations section 1
show that a one-sided bound with $A=1$ can coexist with opposite error
$r$. Thus the stronger hypothesis cannot be silently imported.

The actual derivation survives: at an integer time the centered spans
sum to zero, so bounding either their positive mass or their negative
mass by $A$ bounds their total absolute mass by $2A$. At real time $t$
the change of center adds exactly the permitted floor error; a
$kr$-span then has total deviation at most $2kA+kr/t$ over all labels.
In the forward/backward walk, the second collection of errors is summed
over an injective subset of the later label set. This yields
$\sum|\eta|\le4kA+2kr/t$, even for repeated positions. Translating
each atom changes the integrated interval indicator by at most
$2|\eta|$, proving the stated $8kA+4kr/t$ error in Lemma 6.2.

The $r$-fold span cover remains valid with zero and full-turn arcs.
Pairing arcs ending at the same point and keeping the nonzero mean at
real times proves $Z_t(r)\le A$ by exact cancellation of the floor
error. Both full inequalities of Lemma 2.1 were separately rederived
under their own hypothesis, including the shrinking direction and
endpoint inclusions. No use of those stronger inequalities is smuggled
into the one-sided chain.

The independent recurrence calculation in derivations section 1 gives
admissible absolute choices $C_2=e^{20}$ and $C_3=468$ for Proposition
6.4. It bounds the complete product of scale factors, all additive
errors, and the final descent uniformly for $0\le D\le S$. In
particular the uncountable supremum over $D$ has a single onset time;
there is no inference from separately eventual bounds.

### 2. The complete planar proof, including its constant

Derivations section 2 recomputes the one-dimensional triangular Haar
coefficient, the rectangle coefficient (H0), the empty-interior bound
(H1), the absolute coefficient sum (H2), the binary-digit product rule
(H3) and every subset size in the Riesz-product remainder (H4).
Multiplicity and dyadic boundaries are retained throughout.

The linear pairing is at least $\sqrt{n+1}/10240$; the entire remainder
is at most $1/20480$. The test function's norm is less than
$20001/10000$. The exact inequality
$20480\cdot20001<41000\cdot10000$ then proves the stated
$c_H=1/41000$, including small $M$ and without relying on an unprovided
paper.

The zero-coordinate attack does invalidate equality almost everywhere
of the two anchored counting conventions. For $(0,0)$ their $L^1$
norms are $3/4$ and $1/4$. It does not invalidate the supplied
alternative: the offending contributions are constant in at least
one coordinate, so all tensor Haar coefficients agree. Every term
tested by the Riesz product has the verified tensor-Haar form, and
the same area term retains the total number $M$. The lower bound
therefore holds for the convention consumed by Lemma 7.2.

### 3. Localization and the absolute closing quantifiers

The planar points have time coordinate $i/N$, so they remain distinct
even when circle positions coincide. The chosen half-open arc gives
first coordinates in $(0,1]$. The count in a planar box is exactly
the count in the prefix $\lfloor Nv\rfloor$, and the difference of
area terms has norm $|M_a-L|/4$.

The lower estimate is
$\int\|G_a\|_1\,da\ge(c_H/2)\sqrt{\log(L/2)}-B/4$.
The upper estimate is
$B+L/N+n_0(n_0+L)/N$. The good localization set is allowed to depend
on $N$; both scalar bounds hold for every $N$, so no common
localization point or exchange of limits and integrals is needed.
The early strip uses the trivial prefix count, not an $r$-span
assertion for $n<r$. Derivations section 3 gives $S_0=64$ and
$c_4=1/205000$ as absolute choices.

For either fixed one-sided alternative, take
$A=c\sqrt{\log r}$ with $c=c_4/(4C_3)$. The independent choice
$r_0=\lceil\exp(\max(64,c^{-2}))\rceil$ satisfies all size
conditions and gives $\log S\ge(\log r)/3$. Proposition 6.4 and
Lemma 7.2 would then force $c_4/4\ge c_4/\sqrt3$, a contradiction.
The deduction is written separately for (U) and (L) in derivations
section 3. These conservative constants substantiate the claimed
absolute dependence; no optimality is asserted.

Each conclusion incorporates the preceding reasoning as follows.

| Conclusion | Weak steps used and final composition |
| --- | --- |
| (U) | Steps 1--3, with the positive centered-span mass bounded by the upper-span hypothesis; a contrary upper limsup gives that hypothesis eventually. |
| (L) | Steps 1--3, with the negative centered-span mass bounded by the lower-span hypothesis; the same constants and contradiction apply independently. |
| (I) | The entire proof of (U), then the infimum of its universal lower bounds in the exact $nM$ units; the logarithmic lower bound diverges. |
| (S) | The entire proof of (L), then $\limsup(r-nm)=r-\liminf nm$ and the supremum of the resulting upper bounds on $\liminf nm$; its deficit lower bound diverges. |

## Strongest attempted refutations and their disposition

| Conclusion | Strongest retained attack | Disposition |
| --- | --- | --- |
| (U) | At $n=r^2+r$, put $r$ consecutive zero gaps and $r^2$ gaps of length $1/r^2$. Then the upper error is one while the lower error is $r$. This attacks a possible same-$A$ import of Lemma 2.1 or a hidden positive-span assumption. | The stronger import is false, but is not made. The proof uses the label walk with the independently established total absolute error. Zero spans do not impair label injectivity, the integrated indicator bound or the covering identity. |
| (L) | At the same $n$, put $g_1=(r+n-1)/(nr)$ and $g_i=(r-1)/(nr)$ otherwise. The lower error is one and the upper error is $r$. This attacks the other direction of the same possible hidden hypothesis. | The proof does not require an upper bound with budget one. The zero-sum identity turns lower control into the total-error estimate needed by the walk, with the same constants. |
| (I) | Try to exploit a sequence with infinitely many perfect-grid prefixes, or allow the sequence optimizing the infimum to change with $r$, to remove the lower bound. | The explicitly enumerated dyadic sequence has upper scaled-span liminf $r$ but limsup $2r$. More generally the bound is proved for every sequence separately before taking the infimum, with common $c,r_0$. Neither perfect subsequences nor unattained infima defeat it. |
| (S) | Attack the sign and choice of limit in subtracting the scaled minimum from $r$. For the same dyadic sequence the scaled minimum has liminf $r/2$ but limsup $r$. | The incorrect subtraction from the limsup would give zero, whereas the actual deviation limsup is $r/2$. The subject uses subtraction from the liminf, then the correct supremum inequality. |

The finite gap witnesses test a purported local implication; they do not
purport to satisfy a contrary eventual hypothesis for an infinite
sequence. Their precise domain and the calculations are retained in
derivations section 1. The dyadic sequence and its four exact limiting
values are derived in section 3, in the claim's own span units. They
check the limiting conventions and finiteness, not sharp values of the
extrema.

Additional serious attacks covered all-coincident labels, empty and
full-turn span arcs, noninteger comparison times, $D$ tending to zero,
dyadic and zero-coordinate planar boundaries, cancellation of the Riesz
linear term, a localization good set varying with $N$, and a late-time
threshold depending on $D$ or on the sequence. The retained derivations
give the mathematical reason each failed. No actual counterexample or
unsupported essential deduction in the assigned proof was found.

## Premises, interfaces, and reading depth

The premise list was derived from the supplied statements, full proofs and
consequences, rather than accepted from the manifest's empty native-premise
list. No native L-claim is consumed. That census was checked on 2026-10-15
at this verdict's preparation. No ledger read was authorized or performed;
there is no pending native dependency standing on which this verdict is
conditional. The two conclusions do not depend on the ratio clause or on
the distinct-point version of the theorem.

All essential specialized mathematical premises are supplied and examined
internally in the following acyclic order. The reading depth of each
supplied proof in this table is **proof verified**, meaning the whole
specified deduction in the extraction, not its source publication.

| Internal interface | Exact required hypotheses and conclusion | Role and verification order |
| --- | --- | --- |
| Circle model | Ordered labels, nonnegative gaps summing to one, periodic lifts and multiplicity counts | Establishes the mean identity and the label interpretation before any estimate. |
| Lemma 2.1 | (2.1) with $A\ge1$, fixed $D,E>0$, integer $k\ge1$, $q=E/(kr)<1$, sufficiently late real times; conclusions (2.2), (2.3) and bounded-$D$ uniformity | Entire assigned lemma checked under its own hypothesis; only its walk and averaging identity are consumed by Lemma 6.2. |
| Lemma 6.1 | One fixed eventual integer-time alternative (6.1), $A\ge1$, $kr<\lfloor t\rfloor$; total displacement deviation at most $2kA+kr/t$ | Supplies the error interface absent from the stronger Lemma 2.1 hypothesis. |
| Lemma 6.2 | Same one-sided hypothesis, fixed $D,E,k$, $q<1$, late times and short counting arcs; (6.5) with error $qD+8kA+4kr/t$ | Uses the label walk and Lemma 6.1, not the pointwise bounds in (2.1). |
| Lemma 6.3 and its extension | Same one-sided hypothesis, $\lfloor t\rfloor>r$; $Z_t(r)\le A$ | Uses the covering identity, the real-time mean and Lemma 6.1. Empty/full-turn arcs were checked directly. |
| Proposition 6.4 | $A\ge1$, $r\ge C_2A$, $S=\sqrt{Ar}/\log^2(r/A)$; one late integer threshold for the whole range $0\le D\le S$, with norm at most $C_3A$ | Follows the finite scale chain, terminal Lemma 6.3 bound, descent and integer mean-zero identity. |
| Local planar theorem | Any list of $M\ge1$ points in $[0,1]^2$, multiplicity allowed; $L^1$ discrepancy at least $\sqrt{\log M}/41000$ in either stated anchored convention | Complete (H0)--(H4), constant calculation and boundary extension checked independently of the circle chain. |
| Lemma 7.2 | $S\ge S_0$, $B\ge1$, and one late integer threshold for (7.1) at every $D\in[0,S]$; $B\ge c_4\sqrt{\log S}$ | Consumes the supplied local planar theorem as Theorem 7.1, with its exact normalization and endpoint convention. |
| Closing comparisons | Each contrary limsup separately, fixed $r$ sufficiently large, $A=c\sqrt{\log r}$ | Consumes Proposition 6.4 and Lemma 7.2 with common absolute constants, yielding (U) and (L) separately. |
| Extremal consequences | Definitions of $\Lambda_r$, $\lambda_r$ over all fixed infinite sequences, and the respective theorem | (I) follows (U); (S) follows (L). Their divergences follow their own uniform lower bounds. |

The elementary integration tools are used with explicit scope: finite atom
sums and bounded measurable functions justify the integrations; the
positive-part inequality is pointwise; the measure estimate in localization
follows from integrating over a superlevel set; and the dual norm bound
follows from $|D\Gamma|\le|D|\|\Gamma\|_\infty$. There is no
unstated probabilistic, equidistribution or external discrepancy premise.

The source record is kept separate from these local proof judgments:

* S. Korsky, *A resolution of the de Bruijn--Erdos consecutive-gap problem*,
  arXiv:2609.07196v2, **unrefereed**, Sections 2--3 and 6--8, supplies the
  attribution reported in the packet. The relevant local labels are Lemma
  2.1 (p. 4), Lemma 6.1 (p. 10), Lemma 6.2 (p. 11), Lemma 6.3 and
  Proposition 6.4 (p. 12), and Lemma 7.2 (p. 13). The publication itself
  was **unread**. Its distinct-point theorem is not an established premise
  for the all-sequence extension; all required local deductions were checked.
* Halász's planar theorem is credited through D. Bilyk, *On Roth's
  orthogonal function method in discrepancy theory*, Uniform Distribution
  Theory 6 (2011), no. 1, 143--184, Sections 2 and 4, with the coefficient,
  product and Riesz-product locators given in the supplied provenance.
  That publication was **unread**. The required theorem was proved by
  the supplied local argument, which was checked in full; neither a paper
  citation nor an unprovided proof replaced any of its deductions.
* G. Larcher, *On the star discrepancy of sequences in the unit interval*,
  arXiv:1407.2094v1, Lemma 2.1 and Section 3, is mentioned in the supplied
  provenance for a finite-list method. That source was **unread**, and
  no finite-list theorem from it is consumed by this one-sided argument.
* The catalog statement was read only in the supplied excerpt. The
  external catalog and its current standing were not inspected.

These bibliographic identifiers and source locators are preserved as
provided, not independently certified against the publications. The supplied
provenance credits the original local proof with constants and composition
to Plasma AI; that credit and the unrefereed qualification are preserved.
No source-proof fidelity judgment beyond the supplied extraction is made.

## Complete checklist

The four columns below refer separately to (U), (L), (I) including its
divergence, and (S) including its divergence. Shared deductions are
incorporated as described above; a consequence does not receive a verdict
merely because the theorem next to it survived.

### Canonical failure modes

| Failure mode | Upper sequence (U) | Lower sequence (L) | Infimum consequence (I) | Supremum consequence (S) |
| --- | --- | --- | --- | --- |
| Almost all quietly upgraded to all | No failure: arbitrary label sequences, including repetitions. | No failure: same unrestricted domain. | No failure: infimum over the same full domain. | No failure: supremum over the same full domain. |
| Induction presupposes termination | No failure: the scale chain has explicit finite length. | No failure: same finite chain. | Inapplicable to the extremal step; inherited chain is checked. | Inapplicable to the extremal step; inherited chain is checked. |
| Probabilistic or averaging heuristics as proof | No failure: exact integration, injection and positive-part inequalities. | No failure: negative mass is controlled by an exact zero sum. | No failure: order property of the infimum, not typical behavior. | No failure: exact limit identity and order property of the supremum. |
| Circular use of an equivalent target | No failure: the planar theorem is independently supplied and rederived. | No failure: the lower conclusion is not inferred by assuming the upper one. | No failure: consumes (U) only after its proof. | No failure: consumes (L) only after its proof. |
| Exceptional sets dropped from density arguments | No failure: boundary sets are null in the precise integrals; good-set measure retained. | No failure: same accounted exceptions, with no distinctness exception. | No failure: no exceptional sequence is discarded. | No failure: no exceptional sequence is discarded. |
| Finite verification overreach | No failure: general analytic proof; finite gap witnesses only test an interface. | No failure: same distinction. | No failure: dyadic example checks units and finiteness, not the universal bound. | No failure: dyadic example tests limit signs, not the universal bound. |
| Averaged or relaxed convergence substituted for actual objects | No failure: label injection and exact span/count transfer connect the objects. | No failure: same transfer without positive-span assumption. | No failure: actual span limits are used. | No failure: actual minimum-span limits are used. |

### Named patterns

| Named pattern | Upper sequence (U) | Lower sequence (L) | Infimum consequence (I) | Supremum consequence (S) |
| --- | --- | --- | --- | --- |
| Model-class transport instead of entailment | No failure: no axiom-system extension; the model transfer is explicitly proved on labels. | No failure: the same actual transfer is checked. | No failure: the extremum has exactly the sequence domain proved. | No failure: the extremum has exactly the sequence domain proved. |
| Uniformity from finitely many instances | No failure: explicit absolute constants and common-in-$D$ threshold. | No failure: same constants for the second alternative. | No failure: $c,r_0$ fixed before the infimum. | No failure: $c,r_0$ fixed before the supremum. |
| Extremal claims in their own units | No failure: the maximum is the lifted $r$-span; no ratio surrogate. | No failure: the minimum is the lifted $r$-span, including zero. | No failure: $\inf_X\limsup nM$ checked; finite range $[r,2r]$. | No failure: $\sup_X\liminf nm$ checked; range contained in $[0,r]$. |
| Consequence sentences are claim surfaces | No failure: the corresponding consequence is checked separately in (I). | No failure: the corresponding consequence is checked separately in (S). | No failure: inequality and divergence both derived. | No failure: inequality and divergence both derived. |
| Carry the hypotheses actually used | No failure: (2.1) is not imported; real-time and arc-length conditions retained. | No failure: only one fixed alternative is assumed; upper control is not added. | No failure: uniformity and nonempty family supplied; attainment unnecessary. | No failure: bounded scaled minima and correct limit operation supplied. |
| Composition inherits unproved premises | No failure: every essential specialized premise is proved in the supplied chain. | No failure: same complete internal chain, independently specialized. | No failure: consumes the assessed full (U), not a partial result. | No failure: consumes the assessed full (L), not a partial result. |
| Reproducibility notes are claims | No failure: exact symbolic inputs and full derivations retained; no numerical pass count. | No failure: exact lower-control witness and derivations retained. | No failure: specified dyadic sequence and limiting calculations retained. | No failure: the same exact sequence exposes the limiting-sign distinction. |
| Verifier quotations are claims | Inapplicable: no prior verdict or standing text supplied or relied on. | Inapplicable for the same reason. | Inapplicable for the same reason. | Inapplicable for the same reason. |
| Verdict words spelled in full | The verdict below is refutation-failed. | The verdict below is refutation-failed. | The verdict below is refutation-failed. | The verdict below is refutation-failed. |
| Certified-bracket routines fail loudly | Inapplicable: no numeric enclosure routine. | Inapplicable: no numeric enclosure routine. | Inapplicable: no numeric enclosure routine. | Inapplicable: no numeric enclosure routine. |
| Harness leg without a failing input | Inapplicable: no computational leg; exact attempted-refutation inputs are retained. | Inapplicable: no computational leg; exact attempted-refutation inputs are retained. | Inapplicable: no computational leg. | Inapplicable: no computational leg. |
| Gate reads caches instead of rerunning | Inapplicable: no mathematical gate or cached computation is a premise. | Inapplicable for the same reason. | Inapplicable for the same reason. | Inapplicable for the same reason. |

The classification/entailment aspect of the first named pattern is
inapplicable because there is no axiom-system extension. Its relevant
model-transfer concern is addressed by the explicit label, lift and count
arguments. The correlated-samples discipline is inapplicable: all
integrations and superlevel estimates are deterministic identities or
inequalities, with no statistical samples. Evidence coverage matches the
full analytic derivations; the finite witnesses carry only their stated
interface and convention coverage.

### Erdos-specific audit checklist

| Item | Upper sequence (U) | Lower sequence (L) | Infimum consequence (I) | Supremum consequence (S) |
| --- | --- | --- | --- | --- |
| Quantifiers and scope | No failure: every $X$, every integer $r\ge r_0$, limsup in $n$. | No failure: same quantifiers; zero spans allowed. | No failure: same $r$ range, separate infimum and divergence. | No failure: same $r$ range, separate supremum and divergence. |
| Circularity | No failure: acyclic chain and independent local planar proof. | No failure: acyclic chain; neither sequence theorem is assumed. | No failure: follows the already assessed (U). | No failure: follows the already assessed (L). |
| Model and convention changes | No failure: repeated labels, lifts, full turns and short counting arcs checked. | No failure: same conventions and no illicit positivity. | No failure: definitions match the theorem's coordinates and family. | No failure: definitions match, including liminf. |
| Finite and statistical overreach | No failure: infinite-family algebra and analytic inequalities. | No failure: same, with negative-part rather than positive-part control. | No failure: dyadic example not claimed to optimize the infimum. | No failure: dyadic example not claimed to optimize the supremum. |
| Uniformity | No failure: explicit $C_2,C_3,c_4,S_0,c,r_0$ and justified time thresholds. | No failure: identical absolute choices. | No failure: no exchange of the limit and the infimum. | No failure: no exchange of the limit and the supremum. |
| Extremal conclusions | No failure: finite prefix maximum and its true limsup. | No failure: finite prefix minimum and its true deviation limsup. | No failure: order inequality, nonempty family and finiteness checked. | No failure: sign reversal, boundedness and supremum order checked. |
| Consequences and composition | No failure: all essential interfaces and the closing contradiction checked. | No failure: second fixed alternative checked through the entire chain. | No failure: own lower bound and divergence checked. | No failure: own lower bound and divergence checked. |
| Computation | Inapplicable: no mathematical software or approximation. | Inapplicable for the same reason. | Inapplicable for the same reason. | Inapplicable for the same reason. |
| Reproduction | Full manual derivation and exact symbolic witnesses retained. | Full manual derivation and exact symbolic witnesses retained. | Exact sequence and extremal deduction retained. | Exact sequence, limit identity and extremal deduction retained. |
| Source and verdict fidelity | Supplied proof fully checked; source publications unread and qualification preserved. | Same exact reading depth and limitation. | No previous ruling or external status used. | No previous ruling or external status used. |

## Verdicts and limitations

| Assigned conclusion | Mathematical verdict |
| --- | --- |
| Upper sequence theorem (U), for all sequences with repeated points allowed | **refutation-failed** |
| Its separate infimum lower bound and divergence (I) | **refutation-failed** |
| Lower sequence theorem (L), for all sequences with repeated points allowed | **refutation-failed** |
| Its separate supremum deficit lower bound and divergence (S) | **refutation-failed** |

The full assigned internal chain also survived examination: both inequalities
and the walk of Lemma 2.1 under its own hypothesis; Lemmas 6.1--6.3;
Proposition 6.4 including the continuum of scales; the entire planar proof
with $c_H=1/41000$ and both anchored conventions; Lemma 7.2 including
localization; the all-sequence interfaces, full-turn cover and positivity
issues; and both closing comparisons. Their component verdict is
**refutation-failed** at exactly those hypotheses and scopes. No unfinished
mathematical obligation in the commissioned scope is retained.

These verdicts cover the frozen extraction only. They do not cover later
edits, the ratio clause, the literal original first two expressions, an
optimal constant, an attained extremum, or the excluded proofs and standing
of any source publication. This is not a Lean or computational certificate.
No tier, problem-status, acceptance or grading assertion is made. A distinct
fresh grader must assess this report's contract and independence.

## Rebuilding the examination

The report, `review_derivations.md`, and the thirteen files under `../../assets/whole_statement/returned/assets/review/subject/`
(the manifest plus twelve payloads) are the complete mathematical package.
Their relative links remain usable when retained together in an ordinary
clone. The manifest's source ranges explain the extraction's relation to the
canonical pages; a reader need not retrieve a private archive or an
unprovided publication to follow the assessed argument.

To reproduce the reasoning, read the preserved model and hypotheses, then
follow derivations section 1 through the two gap witnesses, label walks,
floor-error cancellation and explicit scale constants. Follow section 2
from the Haar integral through the exact integer comparison for 41000,
including the $(0,0)$ convention witness. Follow section 3 through the two
localization bounds, the common constants and the separate limit/extremum
operations. The dyadic sequence is completely specified there, and each
limiting value is derived from its displayed prefix sizes. No executable
command, generated data, numerical stopping condition or software dependency
is required.

This is one noncomputational examination, not a claimed second independent
cycle. The structurally disjoint computational reproduction requirement is
therefore inapplicable; no author calculation or cached success is being
rerun in place of an independent argument.

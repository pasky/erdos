---
desc: |
  Independent pass-or-void grade of the complete frozen Problem 173 review,
  its isolation, proof coverage, executable evidence and adoption limits.
---

# Grade of the whole-conclusion review of Problem 173

***

## Subject and decision

**Grade: PASS. Mathematical verdict accepted: refutation-failed.** The
complete frozen report meets the commissioned report and independence
contract for the whole conclusion stated below. This is the distinct grader's
judgment, not the report's verdict repeated as a premise. The warrant remains
conditional on the durable filing specified at the end of this grade.

**Examination date:** 2026-10-17 UTC. **Mathematical subject freeze date:**
2026-10-17. **Report delivery date:** 2026-10-17. The project mathematics is
attributed to Plasma AI. The reviewer and grader are separate, fresh-context
examiners, neither an author of nor a substantive collaborator on the
subject; the grader did not produce the reviewed report. The disclosed model
for each assignment is gpt-6-astra. Model identity is not the basis of the
independence ruling.

The report graded is the unchanged submitted report assigned the durable
snapshot path
`wiki/research/leads/equilateral_two_scale/evidence/assets/whole_conclusion/submitted_review.md`.
Its maintained public presentation is to be
`wiki/research/leads/equilateral_two_scale/evidence/verify/whole_conclusion/review.md`.
This grade's intended home is the same verification directory's `grade.md`.
These are filing destinations; their existence in an adopted checkout was
not presumed or checked by this closed examination.

The mathematical target is the statement at
`wiki/problems/discrete_geometry/E0173/_index.md`, original lines 24--27,
and the candidate conclusion and seven-step proof at
`wiki/research/leads/equilateral_two_scale/_index.md`, original lines
69--83, 91--97, 103--135 and 137--164. Its other native inputs are the
following exact supplied excerpts, not the current original pages.

| Original page under `wiki/research/leads/equilateral_two_scale/` | Original retained lines | Snapshot filename under the asset home's `native_subject/` |
| --- | --- | --- |
| `_index.md` | 69--83, 91--97, 103--135, 137--164 | `whole_conclusion.md` |
| `unit_templates.md` | 22--273 | `unit_templates.md` |
| `rigidity_extension.md` | 26--222 | `rigidity_extension.md` |
| `transcendental_scales.md` | 112--114, 129--137, 231--259, 341--379, 383--397, 400--445, 452--473 | `template_conversion.md` |
| `binary_transfer.md` | 26--62, 64--210 | `binary_transfer.md` |
| `circle_exclusion.md` | 32--196, 199--282 | `circle_exclusion.md` |
| `spectral_exclusion.md` | 22--139, 145--200, 229--236, 256--301 | `spectral_exclusion.md` |

The problem statement snapshot is `native_subject/problem_statement.md`.
The asset home in this table is
`wiki/research/leads/equilateral_two_scale/evidence/assets/whole_conclusion/`;
its `subject_manifest.json` records this path and line mapping, the freeze
date and the uniform omission marker. Source editions and exact external
interfaces are identified below. The fourteen mathematical excerpts, the
complete report and its full keeper were read, together with the allowed
assignment and isolation evidence. No later subject repair is covered.

The grader's supporting derivations are retained at
`wiki/research/leads/equilateral_two_scale/evidence/assets/whole_conclusion/keepers/grader_derivations.md`.
They document actual attempts to break the critical arguments and additional
checks of the consequences. The unchanged executable is
`wiki/research/leads/equilateral_two_scale/evidence/assets/whole_conclusion/keepers/bessel_bounds.py`;
its exact inputs are literal in the program. Reproduction commands and the
observed positive and negative results appear below.

## Restatement and assessed surfaces

For every map $c:\mathbb R^2\to\{-1,1\}$, let $M(c)$ consist of the
positive lengths for which no monochromatic equilateral triangle of that
side occurs. The conclusion is $|M(c)|\le1$, and every set of three distinct
points that is not equilateral has a monochromatic congruent copy. This
includes every collinear triple of distinct points. No regularity of $c$ is
assumed. The possible exception depends on $c$ and need not exist.

Equivalently, for every real $x>0$, $x\ne1$, and every such coloring, some
$p\in\mathbb C$, $u\in S^1$ and $r\in\{1,x\}$ satisfy

$$
c(p)=c(p+ru)=c(p+ru\omega),\qquad \omega=e^{i\pi/3}.
$$

The measurable conclusion says more than occurrence of one copy: for every
non-equilateral triangle the monochromatic placements have positive measure
for plane area times arc length. The proof uses direct motions. The finite
forcing construction works for either chosen orientation of a target;
reflection invariance of the coloring is not assumed. The requirement of
three distinct points excludes repeated-vertex degeneracies but includes
collinearity.

The following judgments are parts of the one whole-conclusion grade. They
are not allocations of claim IDs or separate promotions of source lemmas.

| Assessed surface | Grade and exact warranted scope |
| --- | --- |
| Whole arbitrary-coloring conclusion and all-real two-scale formulation | **PASS; refutation-failed.** Every positive unequal real ratio, not merely algebraic or almost every ratio, and the non-equilateral, collinear and at-most-one-congruence-class consequences are covered. |
| Finite forcing and its measure interface | **PASS; refutation-failed.** Both implications, six direct target motions, six genuine equilateral triples, possible coincidences between different named vertices, and positive-measure propagation were checked. |
| Exact-carrier equivalence | **PASS; refutation-failed.** Finite real-closed constraints and compactness establish the existence equivalence at each real ratio. No injective realization of unrelated vertices is required. |
| Finite-cover Theorem 1 and the all-finite template conversion | **PASS; refutation-failed.** The transcendental finite-function-field argument, its finite quotient, Proposition 8 and the rational-coefficient conversion supply the needed template; the algebraic case uses the number-field lemma within its hypotheses. |
| Haar rigidity and its nonzero pair-correlation corollary | **PASS; refutation-failed.** The supplied source deductions and their specialization to $F_x(i)$ were examined as proof. R0 is discharged for the application and is not an unproved assumption of this grade. Zero-displacement correlation is not claimed to be preserved. |
| Binary transfer | **PASS; refutation-failed.** The conditional forward statement for a countable family with algebraic sides, its two-scale all-real specialization with rigidity supplied, and the reverse measurable-to-arbitrary implication have their stated coverage. The reverse direction gives no measurable completion of the exceptional null set. |
| Measurable exclusion and positive-measure corollary | **PASS; refutation-failed.** The outer ratios, their endpoints, the central unequal-ratio interval, and every non-equilateral measurable consequence are covered, including collinear triples. |
| Report's auxiliary controls and checked quantitative consequences | **PASS at their stated scope.** The half-open-strip single-scale avoider, null-circle control, failed generic projection, rational-angle condition, Bessel infimum bound and global-minimum statement are justified. They do not refute the frozen conclusion. The ratio-one strengthening is **refuted-as-stated** by the strip construction. |
| Keeper's finite arithmetic and rejection claim | **PASS.** The nine retained rational enclosures, fixed scalar margins and deliberate false-upper-bound failure were reproduced. This is not a computational proof of the whole-plane theorem. |
| Optional two-element template proof, unused alternative spectral route, and full proper-unit-distance-coloring result | Outside standalone acceptance scope. Their text was supplied and read; the report expressly does not offer independent acceptance of those whole alternative results. Only the interfaces consumed by the main proof are warranted here. |

The carrier and transfer statements are implications between the existence
of avoiders. They do not assert that such avoiders exist. The conclusion
$|M(c)|\le1$ likewise does not manufacture a missing length. The report's
explicit strip construction separately establishes the endpoint example.

## Independence and exposure ruling

**Reviewer eligibility: PASS. Grader eligibility: PASS.** The review was a
separate refutation assignment on a frozen extraction. Its assignment
excluded author plans, working explanations, prior or sibling judgments,
original subject pages, message channels and outside searches. The report
and screened reviewer account identify actual reading as the fourteen
supplied mathematical excerpts and permitted operating instructions, with
no known excluded exposure. That is more specific than a claim that an
isolation flag was enabled.

The supplied primary operator facts corroborate a blind, sealed assignment,
empty subscriptions before and after startup, unchanged frozen inputs and
configuration, and only private continuation and delivery files changed by
the terminal automatic custody operation. They show no subject edit or
out-of-scope authored path. Under the procedural adapter, that custody action
is not mathematical collaboration. The operator's facts contain no eligibility
judgment; this paragraph supplies the grader's independent judgment.

The content test also passes. The report's attacks, derivations, constants
and limitations can be accounted for by the allowed proof, explicit source
interfaces and its own retained calculations. No reported finding requires
an excluded communication; no evidence indicates that such a communication
selected an attack or weakened the refutation charge. **There is no
disclosed or evidenced excluded exposure to excuse, and no materiality waiver
is being used.** This finding is based on the supplied assignment, reviewer
account, custody facts and report; subscription and identity receipts do not
prove unseen behavior. Raw logs need not become public evidence, and their
absence from the public record is not a defect.

The grader is distinct from author and reviewer and entered this assignment
without participation in the subject or report. The grading read set contained
the report under examination, its permitted original mathematical inputs,
inert primary assignment evidence, screened isolation evidence and operating
rules. The grader read no author advocacy, unrelated report, administrative
packet check, original subject page, other account, message inbox, repository
gate output, network page or theorem-prover artifact. Own subscription
checks were empty. No excluded exposure is known. The identities of the
allowed inputs were checked and remained unchanged. The evidence and the
report were assessed without editing the frozen subject or delivery.

Source access was text-only. Neither examiner inspected a PDF or figure.
This limits source-fidelity assertions, not the mathematical assessment of
the exact text supplied. The finite coordinate reconstruction removes the
need to read Jelínek's figure. The same model in the two isolated assignments
neither creates nor defeats their independence.

## Report-contract grading

Both `docs/verification.md` and `campaign/guides/verification.md` were
applied in full. Section references below are to the unchanged submitted
report; its line ranges distinguish the report's location from the original
subject line ranges above.

| Required contract part | Grade and finding |
| --- | --- |
| Subject block and exact subjects | **PASS.** Lines 12--81 identify roles, freeze and examination dates, original paths and retained sections, exact subject scope, independent code and evidence locations; the reproduction section gives concrete commands. The extraction fixes what was assessed. The filing condition below supplies durable destinations without pretending they already exist. |
| Independence, allowed and actual material, exclusions and exposure | **PASS.** The report distinguishes allowed reading, actual whole-excerpt reading and text-only source access. The independent ruling above checks those disclosures against the primary assignment and custody evidence. |
| Restatement, part (a) | **PASS.** Lines 82--136 preserve arbitrary coloring, all real positive unequal ratios, distinct vertices including collinearity, direct-motion conventions, per-coloring exception and the positive-measure consequence. |
| Checklist, part (b) | **PASS.** Lines 1172--1221 give an explicit finding for all ten Erdos items, all seven canonical modes and all twelve named patterns. Their substance is graded item by item below. |
| Weakest steps, part (c) | **PASS.** Lines 245--723 rederive three consequential links: the finite quotient/template, conditional singularity and multiple averaging, and the pair-preserving sample. They contain the actual algebra, conditional estimates and exceptional-set arguments, not just references to agreement. |
| Strongest attack, part (d) | **PASS.** Lines 1068--1131 explain why finite generation, conditional coset concentration, null-circle shortcuts, a generic projection and the equal-ratio endpoint would break weaker arguments. The algebraic and collision attacks have force at load-bearing inferences; the controls have their exact, different hypotheses. |
| Premises, part (e), and verification order | **PASS.** Lines 137--244 derive an acyclic consumed chain, distinguish internal proofs from external theorem boundaries, and find no established native L-premise. No frozen or prospective ledger tier substitutes for a required live reading. The same dependency census was independently checked in this grade. |
| Independent evidence and reproduction | **PASS.** The mathematical reasoning is retained; the keeper's exact source and literal inputs were supplied and reproduced, with optimized negative-control failure. No scratch-only or cached computation supplies the warrant. |
| Distinct-route and repeated-review rules | **PASS as inapplicable to the special requirement.** This is one whole mathematical conclusion with a finite scalar leg, not a computational batch or an explicitly commissioned second review cycle. The grader's replay is not advertised as another independent numerical algorithm. |
| Mathematical verdict, scope and full wording | **PASS.** Lines 1222--end use **refutation-failed**, preserve the external boundaries and exclude later repairs, formalization, novelty, current public status and PDF fidelity. No mere proof failure is called a disproof. |
| Durable evidence and admissible editorial maintenance | **PASS for the delivered content, conditional on filing.** The exact report, subject snapshots, independent derivations, keeper and literal inputs are preserved in the delivery. The lawful durable adoption conditions below remain outstanding. A private location alone is not a public warrant. |

## Weakest steps and strongest attack: the grader's checks

The complete derivations are in the
[retained grading derivations](../../assets/whole_conclusion/keepers/grader_derivations.md).
The following are the three most consequential checks of whether the
report's reasoning actually defeats its stated attacks.

**Finite quotient.** The unit-span algebra can be non-Noetherian, so finite
ambient function-field degree alone is insufficient. The report instead
obtains a common finite-dimensional rational-transform range. Independently
expanding the product-cover factor gives coefficients
$(V(a)-V(c))/(a-c)$, $V(a)-W(c)/(a-c)$ and
$V(c)+W(a)/(a-c)$, which force $V=W=0$. Dense branch products justify
these as rational identities. Properness at infinity makes multiplication
by $T$ descend to the finite-dimensional image. For any $d+1$
representatives, clearing a dependence over $E(T)$ and removing common
powers of $T-a$ gives a nonzero relation after reduction modulo $T-a$.
Thus the quotient dimension bound survives even an infinitely generated
algebra. Localizations that kill a quotient already contradict normalization;
in a nonzero quotient the Cayley denominators are actual units. This was the
strongest attempted break and it failed for a mathematical reason, not for
lack of a numerical counterexample.

**Conditional singularity and averaging.** Positive conditional coset mass
is an invariant sampled quantity, so ergodicity makes it a constant and
forces finitely many equal-mass cosets. The equivariant centers use their
probability kernels, avoiding an unjustified measurable quotient selector.
The earlier-ordinal assertion applies in the new center factor because the
induction is universal and the earlier tower is unchanged. Test counts and
coefficient bins are fixed before choosing the small frequency. All
conditional pair estimates hold before selecting the fiber-dependent index
set. Counting at most $m^2$ phase products gives a collision lower bound
strictly greater than $(0.95^2-0.1)/m^2$, against an upper bound
$1/(4m^2)$. The tower terminates by separability. The every-Følner and
finite-shift limiting order in the multiple-average argument, including zero
exponents, was independently checked. These checks defeat a genuine
conditioning or quantifier-order failure.

**Measurable sampling.** Spectral support on ordinary characters identifies
continuous vectors, but positivity of the projection comes from the separate
Koopman factor argument. The discarded spectral component contributes zero
only at nonzero displacements; the constant in the sign identity remains
$1$. The equality set of the nonnegative polynomial $Q$ contains both
endpoint signs, which thresholding preserves. Countable-range Borel
approximants give representatives for each fixed translation; Tonelli and a
countable intersection over templates and spatial disks produce one usable
sample. The proof never asserts one exceptional set valid at every point or
a pointwise action of the uncountable group. A generic conditional projection
fails the supplied six-sign control, but it lacks the proved pair identity.

Other essential deductions were also attacked. The direct coordinate motions
and their positive-measure Jacobian handle collinear targets and orientation.
Exact real-closed constraints, not approximate distances, give the carrier
converse. The Bessel table was separated from the ODE, zero-spacing,
monotonicity and limiting spectral arguments; the latter retain mass at
infinity. The central-interval classification uses cyclotomic traces for all
orders. The null boundary cannot be discarded at every circle center; its
positive circle intersection at every one of its own points is what permits
the two-step area contradiction. The final perimeter inference uses the
precise external boundary definition and hypotheses. Rescaling and every
stated triangle consequence were checked separately.

No supplied proof step is repaired by this grade. The additional derivations
make explicit why the report's checks work; they do not change a statement,
replace a missing essential assumption, or expand an omitted alternative
route into an accepted result.

## Consumed premises and source boundaries

**Dependency reading date: 2026-10-17 UTC.** The grader derived consumption
from the complete frozen statement, proofs and consequence sentences, not
from the manifest's declaration alone. No native L-claim is used as an
established premise. Accordingly there is no native ledger row whose live
tier must be read, no stale mark to waive, and no pending promotion assumed.
The closed read set authorized no live-ledger channel, and none was used.
R0 is an intermediate consequence of the internally examined rigidity proof.

The dependency order is finite forcing and elementary/classical interfaces;
finite-cover/template and the source rigidity lemmas; extended Haar rigidity
and its pair corollary; binary transfer; the independent measurable exclusion;
then rescaling and the whole triangle conclusion. The source relative-
singularity lemma has its own strictly earlier-ordinal induction, and the
multiple-average lemma reduces the number of exponents. Neither uses the
final two-scale conclusion. The measurable exclusion does not depend on the
arbitrary-coloring conclusion. The reverse transfer and carrier converse
use finite compactness independently of the forward rigidity route.

| Source or boundary | Exact consumed interface, reading and warrant |
| --- | --- |
| OpenAI, *The Euclidean plane is not five-colorable*, September 23, 2026 Math Release | The supplied transcription at `library/discrete_geometry/openai_2026_euclidean_plane_not_five_colorable/openai_2026_euclidean_plane_not_five_colorable.md`, original lines 83--545 and selected bibliography, and its bibliographic identity were read in full at the supplied depth. Lemmas 2.4--2.7, 3.1--3.5 and the used Section 4 interfaces were examined as mathematical proofs and checked over the required fields. The number-field step is used only with a finite number field; the finite template replaces its transcendental use. No source-card acceptance, external formalization or uninspected theorem is a premise. This does not certify PDF fidelity or the rest of the manuscript. |
| Jelínek, Kynčl, Stolař and Valla, *Monochromatic triangles in two-colored plane*, arXiv:math/0701940v1, January 31, 2007 | The supplied conventions at original lines 48--54 and Lemma 1.3/Corollary 1.4 with proof at lines 72--94 were read. The two finite forcing implications were checked against the explicit coordinates, with positive sides, distinct and possibly collinear vertices, direct motions and their measure interface. The later Combinatorica publication is not the edition inspected; no figure fidelity is claimed. |
| Lahti, *Federer's characterization of sets of finite perimeter in metric spaces*, arXiv:1804.11216v1, April 27, 2018 | The supplied `main.tex` excerpt was read: Euclidean introduction, Theorem 1.1, metric hypotheses, definitions and formulas (2.2)--(2.4), macros and selected bibliography. Theorem 1.1 is used on Euclidean balls with complete metric, doubling Borel regular Lebesgue measure and the $(1,1)$-Poincare inequality. The boundary is exactly positive upper density of both classes. Empty boundary gives finite perimeter, (2.4) gives zero perimeter and (2.2) forces one color null on every ball. Statements and specialization were checked; original proofs remain an explicit external boundary. |
| Real-closed fields and algebra | Elementary transfer is only of finite polynomial constraints over a real-closed subfield of $\mathbb R$. Product compactness, König's lemma, linear extension and finite-dimensional operator algebra are used at their stated classical strengths. No compact topology on the coefficient field or Noetherian hypothesis is assumed. |
| Amenability, spectral and probability facts | Countable abelian groups and their extensions provide invariant means and Følner averages. The spectral theorem is for the discrete abelian carrier; Bochner is applied only after extension to $\mathbb R$ or $\mathbb R^2$. Disintegration and ergodic decomposition use standard probability models and a countable action. The source locates these in Bekka--de la Harpe--Valette, February 23, 2007 author manuscript, D.2.2, D.3.1, G.2.1, G.2.2(ii), G.5.1, and Tao's February 4, 2008 lecture, Theorem 4/Remark 5. Those external pages were not opened; the authorized classical statements and their exact applications are the boundary. |
| Classical analysis | Density differentiation, Fubini--Tonelli, translation continuity, Plancherel, the smooth area formula and ordinary Fourier uniqueness are used with measurable or bounded functions in the displayed domains. The Bessel defining series, its differentiated ODE/identities, decay and Wirtinger inequality have the stated classical roles; DLMF 10.2.2, 10.2.1 and 10.17.3 are supplied locators, not pages inspected by the grader. The specific inequalities and the all-argument deductions were checked directly. |
| Cyclotomic facts | Primitive-root trace averages $2\mu(m)/\varphi(m)$ supply an all-order classification. The permissible trace pairs, actual exceptional angles and their position outside the central interval were rederived. No finite numerical denominator search stands in for this argument. |

The original proofs of these identified classical external theorems are not
recursively certified. Their authorized use at matched hypotheses is not a
pending project claim. This grade gives no general source-proof coverage
label to unread parts of a source, and no source-owned theorem acquires a
native L-identity by being used here.

## Keeper reproduction and exact coverage

The keeper uses only standard-library `Fraction` arithmetic and factorials.
It evaluates the fixed Taylor polynomials by descending Horner evaluation,
checks the nine literal rational rows, the alternating-tail ratio used in
the finite enclosures, and the displayed scalar margins. Its inequalities
are explicit failure branches, not bare assertions. No repository module,
private source, PDF, cached summary, file output or numerical search is used.

The grader reproduced the unchanged submitted bytes at their supplied copy
location, with a memory ceiling, lower scheduling priority and isolated
Python. This substitutes only the permitted copy's path and the local Python
3 executable for the future filing path; it does not change the script or
mathematical inputs. The ordinary-clone commands, from the repository root,
are:

```sh
python3 -I wiki/research/leads/equilateral_two_scale/evidence/assets/whole_conclusion/keepers/bessel_bounds.py
python3 -I -O wiki/research/leads/equilateral_two_scale/evidence/assets/whole_conclusion/keepers/bessel_bounds.py --negative-control
```

The first execution exited zero and verified all nine enclosures. Its energy
margins were $15583/100000000$ and $3/62500$, with exclusion gap $1/375$.
The second exited one and reported `row 0: S_20 < upper fails`. It changes
the first upper bound to $-2601/10000$ while preserving a nonempty proposed
interval, so it is a meaningful false inequality in the stated domain. The
failure survived Python optimization. Both runs completed promptly; a few
seconds is an adequate ordinary runtime expectation.

This replay accepts the report's finite arithmetic and failing-input claims.
It is not evidence of an independent second numerical algorithm, and it
alone supplies none of the infinite-range Bessel, spectral, field, circle or
whole-plane arguments. Those bridges were examined mathematically. The
future public paths and their clone-relative execution remain adoption
facts to check when filed; this grade does not claim the displayed future
paths were executed before they existed.

## Checklist grades

### Erdos-specific checklist

| Item | Grade and substantive finding |
| --- | --- |
| Quantifiers and scope | **PASS.** All real $x>0$, $x\ne1$, arbitrary colorings, per-coloring exception, positive sides and distinct collinear vertices are retained. Weak almost-everywhere conclusions remain intermediate until existence of a weak avoider is contradicted. |
| Circularity | **PASS.** The dependency order, universal earlier-ordinal induction, separable tower termination and exponent-count induction have foundations independent of the desired conclusion. |
| Model and convention changes | **PASS.** Exact carrier constraints, continuous spectral support, the Koopman factor and $Q$ endpoint equality prove the transfers. Direct motions and density-boundary conventions are consistent. |
| Finite and statistical overreach | **PASS.** Finite forcing is a universal finite implication. Rational arithmetic is connected to all arguments by analytic proofs. The conditional estimates are exact inequalities, not sampled empirical evidence. |
| Uniformity | **PASS.** The rational-transform space precedes translated functionals; bin counts precede frequency selection; simultaneous pair estimates precede the choice of indices. Every-Følner convergence and countable sampling intersections have the needed quantifiers. Constants may depend on fixed $x$ and cover data. |
| Extremal conclusions | **PASS.** The actual infimum in the ratio coordinates is bounded with gap $1/375$. Strict pointwise inequalities are weakened correctly under an infimum. Energy proves the stated minimum; no unproved sharpness or universal exceptional side is claimed. |
| Consequences and composition | **PASS.** Exact-carrier equivalence, all-real transfer, measurable positive measure, arbitrary non-equilateral and collinear conclusions and rescaling were individually checked. No unproved R0 remains load-bearing. |
| Computation | **PASS at finite scope.** Literal rows, exact arithmetic, fixed ranges, nonzero failure exits and the valid-domain negative control were inspected and reproduced. There is no iterative enclosure that can silently exhaust a cap. |
| Reproduction | **PASS for the supplied bytes; durable paths conditional.** Both stated behaviors were reproduced at the permitted copies. All executable inputs are retained in the program; no cache or repository gate is credited as mathematics. |
| Source and verdict fidelity | **PASS at the disclosed source scope.** Exact editions, source interfaces, hypotheses and text-only limits are retained. The report's whole verdict is justified within that scope and is not inflated into PDF, kernel, novelty or public-status acceptance. |

### Canonical failure modes

| Mode | Grade and finding |
| --- | --- |
| Almost all quietly upgraded to all | **PASS.** Tonelli handles parameter-dependent sample exceptions. Excluding a weak avoider's existence proves the arbitrary statement; exceptional placements are not simply deleted. |
| Induction presupposing termination | **PASS.** Tower termination has an uncountable-orthogonality contradiction. Other inductions use a strictly earlier ordinal or fewer exponents. |
| Probabilistic or averaging heuristics presented as proof | **PASS.** Moment tests, Markov bounds, finite union bounds, collision counts and mean ergodicity are supplied with the required order of limits. |
| Circular use of an equivalent statement | **PASS.** Finite forcing proves equivalence; neither equivalent target is assumed in the finite-cover or rigidity proof. |
| Exceptional sets dropped from density arguments | **PASS.** The boundary is kept until the two-step area argument makes it empty. A plane-null set is not presumed null on each centered circle. Mass at infinity is kept in the spectral argument. |
| Finite verification exceeding coverage | **PASS.** The keeper checks a finite rational table. The ODE, energy and argument split supply all $t,x$ in the claimed ranges; cyclotomic traces supply all orders in the central case. |
| Relaxed or averaged system replacing actual objects | **PASS.** The actual pair identity and $Q=0$ force opposite endpoint signs before rounding. A generic relaxed field or projection is explicitly shown insufficient. |

### Named patterns

| Pattern | Grade and finding |
| --- | --- |
| Model-class transport instead of entailment | **PASS.** Exact polynomial constraints and separately proved field/group hypotheses justify transport. The transcendental number-field substitution is replaced by a proof, not vocabulary. Novelty of an axiom extension is inapplicable. |
| Infinite-family uniformity from finitely many instances | **PASS.** Uniformity follows from a fixed finite rational space, finitely many selections and compactness, or every-Følner convergence. No finite ratio sample supports all real ratios. |
| Extremal claims in their own units | **PASS.** Bounds concern $J_0(t)+J_0(xt)$ and its infimum in the stated ratio, not neighboring counts or exit codes. |
| Consequence sentences as claim surfaces | **PASS.** Every commissioned triangle and measure consequence, the carrier equivalence and the checked auxiliary angle/minimum claims have separate deductions. Unused alternatives remain outside standalone acceptance. |
| Carry hypotheses used by quantified arguments | **PASS.** Countability, density, real closedness, divisibility, bounded approximation data, fixed finite covers and distinct vertices are supplied at each use. No uniform bounded inventory over all ratios is invented. |
| Composition inherits unproved premises | **PASS.** Every consumed rigidity deduction is included and examined; ordinary external theorems are explicitly bounded. Neither source labels nor provisional local claims supply a missing bridge. |
| Reproducibility notes are claims | **PASS with the stated path qualification.** Source, inputs, arithmetic, exit behavior and runtime were checked. Future filing-path resolution is still an adoption condition, not an execution claim. |
| Verifier quotations are claims | **PASS.** The grader checked the report's actual final verdict and limitations, rather than a parent characterization. No earlier review ruling is consumed by the mathematical proof. Later paraphrases must preserve this grade's scope. |
| Verdict words spelled in full | **PASS.** The accepted main verdict is **refutation-failed**. **Refuted-as-stated** applies only to the explicitly false equal-ratio strengthening. **Proof defective; statement unresolved** would apply to a proof-only failure; none was found in the commissioned route. |
| Certified-bracket functions fail loudly | **PASS at applicable scope.** Bounds are fixed rational Taylor sums with a proved tail. There is no iterative cap or periodic window. Domain/inequality failures return nonzero, and the false bound was rejected. |
| A leg with no failing input is decoration | **PASS.** The retained executable rejects the concrete false upper bound under optimized Python. The rest of the evidence consists of derivations with actual hypotheses, not unconditional success checks. |
| A gate reading caches instead of rerunning is defective | **PASS as an absent mechanism.** No gate supports the verdict. The keeper recomputed its polynomials and margins afresh; no cached success was used. |

The neighboring correlated-sample discipline is inapplicable to statistical
inference: no empirical samples or independence-based confidence estimates
are used. Dependence in the phase lists is explicitly allowed by the $m^2$
product count. The neighboring evidence-coverage discipline is satisfied by
separating finite arithmetic, analytic proofs, text-only source inspection
and later filing facts.

## Verdict, standing and remaining adoption conditions

**PASS for the complete report contract and independence. The accepted
mathematical verdict for the frozen whole conclusion is refutation-failed.**
No counterexample, missing essential hypothesis, unproved consumed project
premise or invalid composition was found. This is not merely acceptance of a
conditional implication assuming the rigidity statement: that
statement's supplied proof and required specialization are covered.

This PASS supplies the whole-conclusion independent mathematical review
warrant for the exact frozen native conclusion. On lawful durable filing it
supports tier-1 standing of that exact conclusion under the repository's
tier law. It neither assigns tiers to every auxiliary literature result nor
creates or edits a native claim card. There is no Lean or tier-2 warrant.
The grading judgment is this examiner's; custody or filing by the parent
adds no mathematical judgment and cannot convert a void report into a pass.

The following conditions remain for adoption:

1. File the unchanged submitted report, this grade, the retained grading
   derivations and exact keeper in the stated durable homes. Preserve the
   submitted report snapshot even if its public presentation receives the
   mechanical editorial maintenance permitted by the verification standard;
   disclose that maintenance on the owning record.
2. File the eight exact native subject excerpts and path/date manifest so an
   ordinary clone identifies the mathematical text actually examined. Retain
   the necessary source editions and proof text lawfully at their canonical
   or snapshot homes, with attribution and license obligations respected.
   Private source transcriptions, private identity receipts, assignments and
   isolation accounts are not a blanket public-copy package. The grade's
   exact external interfaces and text-only reading limits must remain visible.
3. Check the adopted paths and clone-relative keeper commands against the
   preserved bytes. No changed mathematical check may silently replace this
   keeper. Ordinary adoption checks establish repository custody and
   mechanics; they add no mathematical coverage.
4. Reconcile the owning page's standing with the exact accepted subject and
   disclose any subsequent substantive difference. A later repaired or
   strengthened whole statement is a new frozen subject and cannot inherit
   this report or grade. This grade requires no mathematical repair to the
   examined statement.
5. Preserve the separation between this accepted whole-conclusion review,
   original-source proof coverage, outside community acceptance and the
   owner's catalog/status decision. The mathematical review requirement for
   this frozen solution is discharged by this PASS; actual public filing
   and status adoption have not been performed by the grader.

There is no unresolved mathematical input request within the commissioned
read set. The remaining conditions concern lawful durable evidence and
adoption of the unchanged subject. The grade does not determine current
public problem status, novelty, PDF fidelity, omitted source results,
formalization fidelity or the truth of a future revision.

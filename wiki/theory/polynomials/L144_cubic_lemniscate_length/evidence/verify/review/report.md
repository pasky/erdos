---
name: theory/polynomials/L144_cubic_lemniscate_length/evidence/verify/review/report
desc: Whole-statement adversarial examination of the frozen cubic lemniscate bound and equality classification, with explicit source boundaries and failed diagnostic limitations.
created: 2026-10-15T23:40:25Z
updated: 2026-10-15T23:40:25Z
---

# theory/polynomials/L144_cubic_lemniscate_length/evidence/verify/review/report

***

## Subject and independence

**Mathematical verdict: refutation-failed**, for the frozen cubic statement and
its supplied proof under the external source premises identified below. This
is a mathematical examination, not its own grade or a tier assertion. The
distinct grader must adjudicate the disclosed import exposure and the weight
of the failed optional calibration checks.

The subject is the complete extracted statement, all eight proof sections,
the complete evidence description and checker, and the supplied
Eremenko–Hayman text, headed *On the length of lemniscates*, through Lemma 6
with bibliography. The source mathematics
was frozen on **2026-10-15 at 14:29:00 UTC**; the supplied neutral extraction
was prepared that day at **15:09:22 UTC**. The examination date is
**2026-10-15**. No conclusion here concerns later changes.

The preserved subject paths, relative to this report, are:

| Path | Assessed content |
| --- | --- |
| [assets/subject/statement.md](assets/subject/statement.md) | Entire statement, including its quantifiers and convention. |
| [assets/subject/proof.md](assets/subject/proof.md) | Entire proof, sections 1–8. |
| [assets/subject/evidence_description.md](assets/subject/evidence_description.md) | All supplied execution and coverage claims. |
| [assets/subject/evidence/main.py](assets/subject/evidence/main.py) | Complete 342-line checker. |
| [assets/subject/source_eremenko_hayman_lemmas_1_to_6.md](assets/subject/source_eremenko_hayman_lemmas_1_to_6.md) | Locator for the complete supplied source excerpt, 218 lines; the excerpt itself is not reproduced. |

The project-owned mathematical copies preserve the delivered bytes, including
extraction cut markers. The copyrighted source excerpt is cited by its locator
instead of being reproduced; its actual reading depth and scope remain below.
The intended filing home is
`wiki/theory/polynomials/L144_cubic_lemniscate_length/evidence/verify/review/`;
the paths above travel with this record. The copied `assets/subject/runtime/`
is execution support, not an additional mathematical subject. The
[independent derivations](derivations.md), [diagnostic](independent_check.py),
[exact diagnostic inputs](assets/diagnostic_inputs.json), and
[reproduction instructions](reproduction.md) are part of this examination.
Original project mathematics is credited to Plasma AI. Source mathematics
retains the authorship of Alexandre Eremenko and Walter Hayman.

The reviewer was assigned a fresh adversarial context, was neither an author
nor a construction collaborator, and had not built on this result. The
disclosed model is gpt-6-astra. The assignment sought a counterexample,
unsupported essential deduction, or canonical failure mode. No earlier review,
sibling verdict, author plan, live claim standing, or research narrative was
supplied or read. There was no web search, outside-worktree source reading,
native subagent, synchronization, or message-inbox/feed read. Subscription
checks at the first boundary, after startup, and at the examination boundary
all returned empty tables. That is evidence about wiring, not proof of what
was read.

The full statement, proof, checker, evidence description, and supplied source
excerpt were actually read. The complete verification standard and its
campaign adapter, the required anatomy sections, evidence instructions,
authoring and weaving instructions, and commissioned operating context were
also read. Runtime reading included the complete `Checker` and parser
implementation, package import surfaces, constants, CLI wrappers, and copied
project specification. Other supplied runtime modules and the lockfile were
identity checked and used as import support, not individually audited as
repository tools. The supplied installed python-flint API capture was read;
its links and examples were not followed or executed.

**Exposure disclosure.** An initial environment-only probe, before any
mathematical execution, used Python on standard input from the checkout root.
Despite the intended `PYTHONPATH`, Python's initial search entry selected the
live checkout's `tools` package rather than the frozen copy. This implicitly
imported excluded implementation bytes. Only environment identities were
printed; no live module source or mathematical corpus text was displayed, and
no corpus command or mathematical check was invoked. The exposure was disclosed
immediately. A repeated probe with safe-path mode selected the frozen package.
Both mathematical executions subsequently verified the correct package path
in their own process. The first import is not erased by this remedy; its
materiality remains for the distinct grader to rule on.

The supplied inputs remained unchanged under the recorded identity checks.
No frozen proof, checker, input, or public corpus file was edited. The original
source PDF and the underlying books were outside the read set. This is
text-only inspection of the commissioned corrected-1999-preprint excerpt,
not a claim of independently checked PDF transcription fidelity.

## Restatement

For a monic complex polynomial $p$, let $\ell(p)$ be the Euclidean arclength
of the geometric set $\{z\in\mathbb C:|p(z)|=1\}$. For every real
$a$ with $0<a\le2^{-1/3}$, set $c=\sqrt{1-4a^6}$ using the nonnegative
real square root. Then

$$
\ell(z^3+3a^2z-c)
<L_0:=\ell(z^3-1)
=\frac{2\pi\Gamma(1/3)}{\Gamma(2/3)^2}.
$$

For every monic polynomial of degree exactly three with complex coefficients,
$\ell(p)\le L_0$. Equality holds if and only if there exist
$z_0\in\mathbb C$ and $w\in\mathbb C$ with $|w|=1$ such that
$p(z)=(z-z_0)^3-w$. The strict family statement excludes $a=0$; that
auxiliary endpoint gives equality. The endpoint $a=2^{-1/3}$, where $c=0$,
is included. The geometric length is not replaced by a different multiplicity
convention at ramification points.

## Findings on all proof components

| Component | Finding and warrant |
| --- | --- |
| Section 1: reduction to the family | Lemmas 4 and 5 supply existence of a maximizer with unit-modulus critical values. The translation and unit rotation preserve monicity and length. The algebraic normalization below covers both $b=0$ and $u=0$. This is an existential reduction for the upper bound, not by itself uniqueness. |
| Section 2: length integral | Inverse-branch arclength substitution counts each regular preimage once. Finitely many critical points do not add length; their local exponents are $-1/2$, or $-2/3$ at the cubic branch point. Conjugation justifies the factor two. |
| Section 3: root identities | Expansion and the symmetric-root construction give the displayed inverse-derivative formula and scaling. Resolvent and cube-root choices do not change the multiset. See derivation 3 and the finite quadratic-division attack. |
| Section 4: comparison and constant | Parseval and endpoint domination justify the increasing series for $\Phi$. The independent beta/gamma calculation below gives the exact value. The scaling in $L=\Phi+aI$ has the correct power of $a$. |
| Section 5: small parameters | The near graph, omitted complement, tail constant, head subtraction, singular window, and symmetry factors were independently derived. All thirteen full parameter boxes passed the rerun. The inclusion of zero is only in the enclosure formulas. See derivation 2. |
| Section 6: larger parameters | The singular-window estimate has the correct chord and integral constants. Its guards and the full rerun cover the endpoint and upper-integration extension. All accepted parameter boxes use their entire intervals. See derivation 3. |
| Section 7: coverage and conclusion | The two explicit overlap checks passed; the adaptive cover checked consecutive endpoints and its final endpoint. Finite sums are bounds over boxes, not samples. The control's omitted positive terms give the correct lower-bound direction. |
| Section 8: equality classification | The source's local deformation applies to every extremal polynomial. Local degree preserves simple critical points; centered cubic coefficients remain bounded during critical-value transport. The open/closed and endpoint arguments exclude all $u\ne0$ maximizers. The $u=0$ and converse cases are checked separately. See derivation 1. |

For the normalization, write a translated cubic as $z^3-3u^2z+b$. A unit
rotation of the variable together with the inverse cubic phase of the value
makes $b\le0$ real. Unit-modulus critical values imply

$$
\operatorname{Re}(b\overline{u^3})=0,
\qquad b^2+4|u|^6=1.
$$

When $b<0$, $u^3$ is imaginary, and one of the rotations fixing $b$ makes
$u=\pm ia$, $a=|u|$. When $b=0$, an arbitrary phase rotation is available;
when $u=0$, $b=-1$. Thus the stated closed parameter interval is exactly
the needed normalized class. No scale change has been introduced.

For the constant, the three inverse derivatives of $z^3=s$ sum to
$|s|^{-2/3}$. Therefore

$$
\begin{aligned}
L_0
&=\int_0^{2\pi}2^{-2/3}|\cos(\theta/2)|^{-2/3}\,d\theta\\
&=2^{1/3}B(1/2,1/6)
=\frac{2\pi\Gamma(1/3)}{\Gamma(2/3)^2}.
\end{aligned}
$$

The last equality uses
$\Gamma(1/6)\Gamma(2/3)=2^{2/3}\sqrt\pi\Gamma(1/3)$.
For $c<1$, absolute convergence of the binomial series gives Parseval;
for $c\ge1/2$, the identity
$|c+e^{i\theta}|^2=(1-c)^2+c|1+e^{i\theta}|^2$ supplies an integrable
majorant proportional to $|1+e^{i\theta}|^{-2/3}$. Thus the endpoint
passage is justified. The nonzero coefficient at degree one proves strict
increase, including comparison to the endpoint. Finally,
$G_a(s)=a^{-2}G_1(s/a^3)$ and $|ds|=a^3|d\sigma|$ give
$L(a)-\Phi(c)=aI(a)$ exactly.

### A false sentence in the supplied source excerpt

The final paragraph of the supplied proof of Lemma 4 says that the length
tends to zero as the root vector $Z$ tends to infinity. Taken literally, this
sentence is false. Let $Z_R=(R,R,R)$ and $p_R(z)=(z-R)^3$ for real
$R\to\infty$. Then $\|Z_R\|\to\infty$, but $E(p_R)$ is the circle
$|z-R|=1$ and has constant length $2\pi$.

The preceding source argument concerns **root diameter**, which remains zero
in this witness. A compactness argument for existence must first normalize
translations, for example by putting one root at zero. Bounded root diameter
then bounds the normalized root vector. The frozen native proof consumes
Lemma 4's existence and continuity statements, not the false unnormalized
asymptotic sentence; its own section 8 explicitly centers its cubics. This
finding limits any claim to have verified every sentence of the source proof.
It is not a counterexample to the commissioned cubic statement or to the
stated source theorem. With no PDF inspection, this record does not decide
whether the wording error is in the print or its supplied transcription.

## Weakest steps and strongest attempted refutation

The three independent weakest-step derivations are retained in
[derivations.md](derivations.md):

1. The source deformation for **any** maximizer, its monic normalization and
   preservation of ramification, and the cubic compactness argument extending
   local moves to the circle without collisions.
2. The uniform small-parameter bound, including the scaled graph, both tail
   constants, the signed head subtraction, and the square-root window.
3. Branch-independent root enclosures, signed rectangle sums, exhausted-depth
   behavior, the large-parameter singular window, and the endpoint extensions
   and full parameter cover.

The strongest attack was to separate the existence of one normalized maximizer
from classification of every maximizer. A second possible failure was that
local deformations could fail to reach the circle because of coefficient
escape or coalescing critical values. The supplied source construction and
the explicit identities $b=(t+w)/2$, $|u|^3=|w-t|/4$ defeat both attacks
when the chosen arc avoids the fixed value. The remaining $u=0$ family
independently has equality only at $|b|=1$. This supplies the required
entailment rather than assuming that an existential result classifies all
extremizers.

The strongest computational attack used a prescribed exact root and quadratic
division to challenge the Cardano enclosures across cuts and near critical
values. It found no conflicting root-density value in its finite domain.
The four failed calibration equalities, described below, are failures of the
reviewer's optional diagnostic assertions; they do not supply an inequality
contradicting an author's enclosing bound.

## Computational findings and reproduction

The complete frozen checker was executed with no quick mode and no cached
results, using one thread, python-flint 0.9.0, and the installed CPython
3.14.6 environment. The running process verified its environment prefix,
frozen `tools` import, standard-library `typing` import, and python-flint
version before executing the unchanged file. The only execution substitutions
were the commissioned file relocation/runtime import and an operating wrapper
that printed and checked those identities, then invoked the unchanged main
file with its original argument list.

The run exited **0**, with **22 checks passed**, in about five minutes
(observed elapsed time approximately 288 seconds). Its results were:

| Quantity | Observed result |
| --- | --- |
| $L_0$ | Displayed as $9.17972422234316$ with enclosing print radius $2.77\cdot10^{-15}$. |
| Small-parameter cover | Thirteen boxes; reported largest upper bound for $I(a)$ was $-0.216023$ with print radius $1.23\cdot10^{-7}$. |
| Small-parameter regular pieces | 1,930,449; explicit head, window, and tail terms are additional. |
| Large-parameter cover | 591 consecutive accepted boxes; each passed the strict $L_0-1/100$ test. |
| Large-parameter regular pieces | 2,581,149; explicit windows are additional. |
| Reported minimum margin | $0.0114301$ with print radius $4.80\cdot10^{-8}$; the proof uses every box's individual comparison, not this summary. |
| Control at $\beta=1/2$ | The displayed enclosing bounds imply the conservative interval $8.1746135\le L\le8.1829017$. |

The distinct diagnostic route starts from an exact Gaussian-rational root
$r$, sets $s=r^3+3a^2r$, and finds the other roots from
$z^2+rz+r^2+3a^2$. It never chooses a Cardano resolvent or takes a cube root.
The 128-bit inverse-derivative sums for 60 prescribed inputs lay inside the
64-bit Cardano density balls for twelve boxes. All generated inputs were
checked to lie in their corresponding boxes. Cases cover both signs of real
and imaginary cuts, near-critical values, general complex values, scaling,
and zero linear coefficient. This attacks the root-generation implementation;
it shares the ball library and does not independently validate that library
or prove uniformity over the parameter ranges.

The diagnostic also confirmed the analytic instance $G_1(0)=2/3$, rejected
the deliberately wrong value $4/3$, checked the finite numerator and zero
denominator at $s=2i$, and observed nonfinite density there. Its nonfinite
depth-cap, invalid-window, and unresolved-cover inputs produced the required
failure behavior.

**The diagnostic as a whole exited 1:** four of its 48 checks failed. They
are the finite-cap exact endpoint equality and the three signed-rectangle
exact endpoint equalities. The driver required exact ideal endpoints even
though a constructed arb radius may round outward. Such equality is stronger
than the required enclosure inequality. The independent signed-rectangle
derivation establishes the relevant inequalities without these tests.

Actual endpoint values for those four assertions were not printed, so no exact
numerical cause or size of their discrepancy is asserted here. Their failed
status is retained; the unchanged driver is not advertised as a passing
certificate. No third mathematical execution or repaired diagnostic was run.
A corrected instrumented diagnostic would be a separate record if its added
coverage is wanted. The [reproduction instructions](reproduction.md) distinguish
the successful full run from this reproducible failed diagnostic.

## Premises and source boundaries

The premise census was derived from the full extracted statement and proof,
including their consequence sentences. **No native L-claim is used as an
established premise.** The self-reference supplies definitions already
present in the extraction. The research-sketch link identifies provenance for
algebra reproduced in section 1; it supplies no additional theorem. Those
definitions are meaningful independently of the truth of L144. No live ledger
read was authorized or performed, and there is no pending native dependency
standing to substitute for a current one.

| Source or tool boundary | Exact consumed content, specialization, and actual reading depth |
| --- | --- |
| Eremenko–Hayman, corrected 1999 preprint as commissioned, Lemma 4 | Continuity of lemniscate length in coefficients and existence of a maximum among monic polynomials of fixed positive degree; used at degree three in sections 1 and 8. Entire supplied statement and proof read. **Claims checked; proof partially verified**, not every source sentence verified, in particular because of the unnormalized-root-vector sentence identified above. The theorem statement is an identified external premise. |
| Same source, Lemma 5 | Existence of an extremal polynomial all of whose finite critical points lie on its lemniscate, equivalently whose critical values have modulus one. Entire supplied statement and proof read. **Claims checked; proof partially verified.** The local deformation deductions needed for the cubic equality proof were examined through the external Beltrami boundaries. The general-degree endpoint transport is not separately reconstructed; the native cubic argument supplies its own compactness. |
| Actual local construction in the proof of Lemma 5 | For any extremizer and an off-circle critical value isolated from the others, there is a local monic deformation moving that value alone and keeping length maximal. Entire construction and its subharmonicity argument read and its essential deductions independently rederived in derivation 1. Preservation of simple critical points follows from local degree under the two homeomorphisms. |
| Carleson–Gamelin, *Complex Dynamics* (1993), Chapter I, Theorems 7.4 and 7.6, as invoked in the supplied source | Existence and analytic parameter dependence of the normalized solution of the compactly supported Beltrami equation with coefficient norm less than one. The source invocation and the application hypotheses were checked. The original book and proofs are **unread**, outside the supplied set. This is an explicit external theorem boundary; no local proof of it is claimed. |
| Ahlfors, *Lectures on quasiconformal mappings* (1966), p. 9, as cited by the source | Quasiregular composition/Beltrami chain rule. Original text **unread**. The displayed identity used here is independently obtained by the Wirtinger chain rule in derivation 1; the source's reference is not extended to unexamined claims. |
| Source's internal inputs to Lemma 4 | Lemmas 1–3 and the invocations of Cartan's covering bound and Hille, *Analytic Functions Theory*, vol. 2, Theorem 12.2.1. Their supplied text and interfaces were read; the original cited works were not. They are internal to the identified external Lemma 4 premise, not separately certified local results. |
| Standard analysis | Local inverse-branch substitution, Parseval, dominated and monotone convergence, the beta integral and gamma duplication, the subharmonic maximum principle, and compactness/connectedness. The relevant hypotheses and specializations are checked in this report and derivations. No additional native result is being assumed. |
| python-flint 0.9.0 arb/acb | Real and complex enclosing balls; directed enclosing endpoints and unions; enclosing elementary, root, trigonometric, and gamma operations. The supplied installed API documentation and checker calls were read. No independent verification of the library implementation or its transcendental algorithms is claimed. |

The supplied Lemma 6 and its following connectedness remark were read but are
not consumed. Neither the source's general linear-in-degree bound nor its
quadratic extremizer theorem is a premise of the cubic argument. The review
is neither a batch nor a commissioned second review cycle; no prior-cycle
attack comparison was supplied or inferred.

## Checklist

### Canonical failure modes

| Item | Verdict and reason |
| --- | --- |
| “Almost all” upgraded to “all” | Not found. Full parameter balls, explicit endpoint handling, and an arbitrary-maximizer argument cover the quantified domains. |
| Induction presupposing termination | Not found. Critical-value transport uses open/closed compactness; numerical caps either retain a proved rectangle or fail. No successful termination is assumed to establish truth. |
| Probabilistic or averaging heuristics as proof | Inapplicable. No probabilistic inference occurs; Parseval and the three-root average are exact identities and inequalities. |
| Circular use of an equivalent statement | Not found. Existence of a maximizer is external; it does not assume its value. The family bound determines the value before uniqueness is deduced. |
| Exceptional sets dropped from density arguments | No density argument occurs. The analogous finite singular sets in the length integrals are explicitly integrated, not discarded from upper bounds. |
| Finite verification claimed beyond its reach | Not found in the uniform checker. Each piece bounds an entire box. The independent 60-point diagnostic is explicitly only finite testing. |
| Relaxed or averaged convergence substituted for actual objects | Not found. The inverse-root density is exactly geometric arclength, and coefficient continuity is applied to actual monic cubics. |

### Named patterns

| Item | Verdict and reason |
| --- | --- |
| Model-class transport instead of entailment | No axiom-system extension is involved. The relevant transformed-family entailment is proved by length-preserving normalization; existential reduction is kept distinct from all-maximizer classification. |
| Infinite-family uniformity from finitely many instances | Not found. Constants and interval inputs are uniform on their specified boxes; tail and singular estimates supply the infinite-family bridge. |
| Extremal conclusions in the claim's own units | Checked in Euclidean arclength with monic leading coefficient. Source existence is explicit, the gamma value is evaluated in those units, and equality transformations have unit scale. |
| Consequence sentences as claim surfaces | Checked separately: strict family bound, every-cubic upper bound, and both directions of equality. The source-excerpt asymptotic sentence has the explicit counterexample above. |
| Carry hypotheses used by quantified arguments | Checked. Positivity of $a$, the two critical-value cases, distinctness along the arc, coefficient boundedness after translation, and the small-parameter graph conditions are all retained. |
| Composition inherits unsupported premises | No missing native premise found. Source existence, continuity, and the stronger local deformation interface are stated at their actual strength. External Beltrami and ball-library boundaries remain explicit. |
| Reproducibility notes are claims | Full authorized relocated execution reproduced its numerical statements. The original live path was not read or executed; the exact authorized substitution is documented. The diagnostic's nonzero outcome is disclosed rather than reported as a pass. |
| Verifier quotations are claims | Inapplicable to this frozen extraction: no earlier verifier ruling or standing text was supplied. No live card was consulted to manufacture this check. |
| Verdict words in full | Satisfied. The report uses refutation-failed for the commissioned target and distinguishes it from a disproof or defective-proof verdict. |
| Certified-bracket functions fail loudly | Analytically checked. Nonfinite depth exhaustion raises; unresolved parameter cover records failure. The corresponding diagnostic failure inputs behaved correctly. Finite depth-cap acceptance retains a rectangle bound; its failed exact-equality calibration is not used as a pass. No periodic phase statistic is involved. |
| Every checking leg has a meaningful failing input | Checked. Nonnegative $I$ bounds or inadequate length margins fail the full obligations; coverage mismatches fail tiling. Exact diagnostic rejection inputs are retained. Wrong-factor density $4/3$ at zero is rejected. Four overstrict calibration assertions actually failed and remain identified as defective diagnostic tests. |
| A gate must rerun rather than read cached success | Satisfied for the evidence used. The full checker recomputed its pieces and cover; the diagnostic recomputed its roots. Neither reads a cached mathematical success summary. No repository gate is claimed. |

### Erdos-specific checklist

| Item | Verdict and reason |
| --- | --- |
| Quantifiers and scope | Covered: all positive family parameters through $c=0$, all monic complex cubics, and the exact if-and-only-if equality classification. |
| Circularity | No circular premise found; the source premises and internal sequence are stated above. |
| Model and convention changes | Normalization, inverse-root counting, scaling, and monicity are checked; no relaxed model replaces the lemniscate. |
| Finite and statistical overreach | No statistical claims. Uniform interval certification is distinguished from the finite diagnostic. |
| Uniformity | Parameter dependence, singular limits, series limits, branch choices, and all explicit tail/window constants are justified. |
| Extremal conclusions | Existence, upper bound, attainment, and uniqueness were separately examined in length units. |
| Consequences and composition | All three conclusions compose through the explicit external interfaces; the source wording error is not silently imported. |
| Computation | Full ranges and failure exits checked; finite rectangles are proved bounds. The failed auxiliary equality tests and missing endpoint diagnostics are disclosed. |
| Reproduction | Full rerun succeeded; independent diagnostic rerun failed in the four specified tests. Exact code, inputs, transformations, and rerun commands are retained. |
| Source and verdict fidelity | Source hypotheses and actual reading depths are recorded. No PDF, original-book, prior-review, or tier coverage is invented. |

The neighboring discipline about correlated statistical samples is inapplicable
because there is no statistical inference. Evidence coverage is checked under
the supplied anatomy/evidence contract: the computation certifies only its
integral bounds, and the written mathematics supplies their connection to the
complete statement.

## Verdict, limits, and remaining ownership

**refutation-failed** is the mathematical finding for the complete frozen
cubic assertion and its supplied proof, relying on the identified external
source theorems and the documented ball-arithmetic contract. The strict
family inequality, exact gamma value, universal upper bound, and equality
classification have each been examined. No counterexample to them or
unsupported essential inference was found. The false unnormalized asymptotic
sentence in the supporting excerpt is retained at its actual, nonconsumed
scope.

The distinct grader owns acceptance of this examination. In particular, the
initial live-package import requires an explicit materiality ruling; this
report does not supply one. The optional diagnostic's four failed exact
equalities cannot be cited as successful enclosure calibration. Their actual
endpoint discrepancies remain unmeasured in the retained output. If further
calibration is required, the coordinator must commission a new, instrumented
record; this examination does not silently repair and rerun its frozen keeper.

There is no outstanding native-premise standing read. Original-PDF fidelity,
proofs of the external Beltrami theorems, and verification of the ball library
are outside the authorized scope and remain the stated external boundaries.
The coordinator owns durable filing of the unchanged subject and keeper
package, distinct grading, and any additional commissioned work. Private
delivery and successful execution alone confer no mathematical tier.

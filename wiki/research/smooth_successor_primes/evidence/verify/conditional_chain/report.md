---
name: research/smooth_successor_primes/evidence/verify/conditional_chain/report
title: "Conditional squarefree-pair implication: independent examination"
desc: Whole-statement adversarial examination of the conditional smooth-successor implication, with a counterexample to its unrestricted auxiliary dyadic formulation.
created: 2026-10-16T04:10:53Z
updated: 2026-10-16T04:16:14Z
---

# Conditional squarefree-pair implication: independent examination

***

## Subject and independence

**Subject.** The frozen implication from the explicit hypotheses P and E,
through the signed Type II estimate, successor-prime extraction and
Hypothesis A+, to the eventual real-variable squarefree version of the
Problem 824 bound. Frozen on 15 October 2026; examined on 15 October 2026 UTC.
The reviewer is an independent mathematical reviewer, using GPT-6 Astra
at its maximum reasoning setting. This is an adversarial examination,
not authorship, a grading of another report, or a claim of an unconditional
solution.

**Finding.** The verdict on the conditional implication is
**refutation-failed**. There is a separate **refuted-as-stated** finding for
the unrestricted formulation of the auxiliary “Dyadic bound”: a product-size
condition alone does not imply it. The complete proof does establish the
balanced specialization actually used in the successor extraction. The
distinction, exact asymptotic witness, and limits of this verdict are below.

The assessed mathematical bytes are retained in this package. The paths in
the second column identify their source subjects; those live paths were not
opened, and no conclusion is asserted about later versions.

| Retained frozen input | Repository-relative source identity and assessed scope |
| --- | --- |
| [signed_type_ii.md](../../assets/conditional_chain_subject/signed_type_ii.md.txt) | wiki/research/smooth_successor_primes/signed_type_ii.md; all supplied text, lines 1–481, including P and the entire signed proof. |
| [extraction.md](../../assets/conditional_chain_subject/extraction.md.txt) | wiki/research/smooth_successor_primes/successor_prime_extraction.md; all supplied text, lines 1–422, including every Type I, sieve and balanced-composite deduction. |
| [product_reduction.md](../../assets/conditional_chain_subject/product_reduction.md.txt) | wiki/research/smooth_successor_primes/li_zhuang_reduction.md; all supplied text, lines 1–165, including both final quantifier paragraphs. |
| [catalog_statement.md](../../assets/conditional_chain_subject/catalog_statement.md.txt) | wiki/problems/arithmetic_functions/E0824/_index.md; the supplied statement only, not its standing. |
| [source_sections_2_6_7.md](../../assets/conditional_chain_subject/source_sections_2_6_7.md.txt) | library/arithmetic_functions/openai_2026_weighted_dilation_graphs_smooth_shifted_primes_totient_fibers/openai_2026_weighted_dilation_graphs_smooth_shifted_primes_totient_fibers.md; all supplied Sections 2, 6 and 7 and bibliography, lines 1–752. |
| [README.md](../../assets/conditional_chain_subject/README.md.txt) and [read_set.json](../../assets/conditional_chain_subject/read_set.json) | The supplied neutral scope and source-identification metadata, both read in full. |

The retained mathematical reasoning is [the signed keeper](signed_keeper.md),
[the extraction keeper](extraction_keeper.md), and
[the counting keeper](counting_keeper.md).
[The premise account](premises.md) is an integral part of this report's
restatement and dependency account, not an optional reference. There is no
mathematical program, sampled experiment, or cached computational result on
which the verdict depends.

The examination began from the supplied frozen subject and operating rules.
No authorship or collaboration on this subject occurred in the review
context. No author advice, prior review, sibling verdict, review inventory,
live ledger, source-card standing, external search, or excluded mathematical
material was read. No descendants or other reviewer threads were used. The
subscription observations were empty; the inbox remained sealed and no feed
was opened. Empty subscriptions support this account of isolation but do not
by themselves establish what was read.

The commissioned mathematical read set was exactly the seven retained inputs
above, all of which were read fully. The allowed operating set consisted of
the enumerated static repository guidance, its frozen copies, the rendered
charter and steps, configuration and accepted settings, command help and the
four named local operating skills. Actual operating content reads were:

- The supplied root AGENTS instructions, README, both complete verification
  contracts in docs/verification.md and campaign/guides/verification.md,
  campaign/AGENTS.md, docs/evidence.md, docs/approach_vetting.md,
  docs/math_authoring.md and docs/weaving.md, all in full.
- docs/anatomy.md, lines 1–177, 253–397 and 1061–1165, covering Claims,
  Evidence, Tiers and Project claims; campaign/guides/research.md, lines
  1–115, including its full Reading section.
- The supplied manifest, accepted settings, review configuration, command help,
  three step texts, four station script texts, and radio and memory skill
  texts in full. Scripts were inspected, not executed. The rendered charter
  was read in full; its on-disk context and pin, selected template keys, and
  the relevant resource and lifecycle portions of the recursive-operation
  skill were inspected. Partial displays of those optional operating texts
  are not represented as complete readings.
- The reviewer's own continuation and retained reasoning. The remaining
  enumerated operating pages and the wiki skill were byte-checked only,
  without content reading. Links in all these texts were not followed.

The delivered files matched the supplied manifest, and all fourteen
enumerated static operating sources matched their frozen copies. The
mathematical subject stayed unchanged. Those administrative observations
provide identity evidence, not mathematical evidence.

One procedural fact is retained for the distinct grader: the accepted-settings
file was displayed alongside the manifest before its identity comparison.
The subsequent comparison matched exactly. It contained operational settings;
no excluded mathematical exposure was observed. This read-order fact was
disclosed through the permitted outbound channel. Some initial oversized
displays were truncated; complete nontruncated readings subsequently covered
every mathematical input and both verification contracts. The reviewer does
not rule on eligibility or the materiality of the procedural disclosure.
Detailed command receipts remain private, separate from this mathematical
record.

## Restatement

For a positive integer n, let sigma(n) be the sum of its positive divisors.
For real x define

$$
h(x)=\#\{(a,b)\in\mathbb N^2:1\le a<b<x,\ (a,b)=1,\
\sigma(a)=\sigma(b)\},
$$

and let h_sf(x) count just those pairs in which a and b are both squarefree.
The pair is counted once, in the order a<b. The convention includes the
positive integer 1 as squarefree; no diagonal pair is counted.

Assume the complete P and E statements restated in
[the premise account](premises.md). In particular P is uniform shift
cancellation for both signs of a nonzero shift, with the entire stated
endpoint coefficient and support class, all the stated character and Mellin
parameters, the harmonic factor 1/z, and the required conjugations. Its
discrepancy condition is imposed on the actual restricted alpha sequence;
it includes principal and imprimitive characters. The distinguished slot is
an integer rough above W, not necessarily a prime. Group counts count
distinct divisors, whereas band lists allow repeated primes. E includes the
full candidate-mass, proxy-discrepancy and proxy-density statements at the
uniformities used, the block sieve, and the precise Section 2 classical and
elementary estimates. P and E are hypotheses, not findings of this report.

With the fixed group and band data of the signed page, for every fixed
D_*,b_*,C>0 satisfying eta_*<b_*/4 and fixed smooth compactly supported Psi,
there is a fixed discrepancy exponent B such that, for all sufficiently
large real x, all scales UV comparable to x with
x^(b_*)<=U,V<=x^(1-b_*), and all permitted sequences alpha,beta,

$$
\sum_{\substack{m\asymp U,\ n\asymp V\\ mn=2u-1}}
A(u)\Psi(u/x)\alpha_m\beta_n
\ll x(\log x)^{-D_*}.
$$

Beta is arbitrary within its coefficient bound. Alpha is rough-supported
and satisfies the stipulated discrepancy after its actual interval cuts.
All constant dependence and the definitions of A, the groups, the bands and
the exceptional interval are those stated explicitly in the premise account.
This is the signed intermediate deduction, not another assumed premise.

The complete extraction then asserts that for every fixed 0<delta<1/4
there exist c,C_A,C_w>0 and a threshold such that every sufficiently large
real x has at least

$$
c\,x(\log x)^{-C_A-1}\exp(-C_w\sqrt{\log x})
$$

distinct primes p in [2x-1,4x-1] with P^+(p+1)<=x^delta.
Here P^+(1)=1 and P^-(1)=infinity; smooth means that every prime factor
is at most the cutoff, and rough means that every prime factor exceeds it.
All fixed parameters precede x tending to infinity.

Consequently A+ says that for every fixed 0<delta<1/4 and eta>0 there is
a threshold y_0(delta,eta) such that for every real y>=y_0 at least
y^(1-eta) primes p<=5y satisfy P^+(p+1)<=y^delta. No effectiveness or
uniformity as delta tends to zero is asserted.

The terminal implication is

$$
(\mathrm P)\ \&\ (\mathrm E)
\quad\Longrightarrow\quad
\forall\epsilon>0\ \exists x_0\ \forall x\in\mathbb R,\ x\ge x_0:
\quad h(x)\ge h_{\rm sf}(x)>x^{2-\epsilon}.
$$

This is the eventual interpretation of the catalog's exponent notation.
Neither an almost-all set of x nor a subsequence suffices. The terminal
products satisfy the strict upper endpoint, coprimality, equal divisor sums,
and squarefreeness simultaneously.

## Weakest steps and complete deduction coverage

Three written rederivations cover the consequential analytic and combinatorial
bridges. Their full details are retained, including unsuccessful attacks;
the summaries here identify the points on which composition depends.

### 1. Signed Type II from the actual endpoint hypothesis

The [signed keeper](signed_keeper.md) starts before Cauchy's inequality.
The group-part tail is at most

$$
xL^{O(1)}\exp\{-b_*L^{1-d}/4+O(\sqrt L)\},
$$

which is negligible because d<0.47. The finite slot-allocation invariant
gives E L^(-C_s)<=e<=E, where E=U L^(-K_0). Products of one-dimensional
Fourier norms, not a fixed-dimensional lemma in a growing dimension, keep
the total coefficient mass and the residual coefficient bound polynomial
in L independently of K_0. The diagonal after Cauchy is controlled by
fixed second and sixth divisor moments, permitting K_0 to be chosen only
after those costs are known.

For the off-diagonal the exact signed identities are

$$
m'-m=-2ek,\qquad h'-h=-kn,\qquad
mh'-m'h=k,\qquad z=m'h,\quad z+k=mh'.
$$

The converse uses roughness and |k|<W to get gcd(m,k)=1. The congruence
m'=m modulo 2|k| gives integral e; the positive cutoff imposes e>0.
Divisibility then gives integral positive n=(2eh-1)/m.
Character orthogonality is valid because m,m' are units
modulo 2|k|. Thus the correspondence has no missing divisibility, sign or
positivity assumption.

After separation, the discrepancy-bearing endpoint still contains the
original restricted alpha. All new characters, twists and residual
coefficients are explicit members of P's endpoint class. The factors
z^(i(varrho+xi_3))(z+k)^(-i varrho), and the conjugations recorded in the
keeper, match the original square norm. Multiplying the smooth test by
its argument converts the unweighted correlation to Z times P; omitting
this Z would lose the scale of the estimate. Both signs of k are used.
The choice order is fixed geometry and saving, then K_0, post-Cauchy
Fourier costs and D_0, then B. The derivation needs no extra premise.

### 2. Complete successor extraction, including the balanced sieve

The [extraction keeper](extraction_keeper.md) derives Type I in the unit
class 2^(-1), including the principal coprimality error, the primitive
conductor decomposition, the large-sieve factor 1/R and the small-conductor
Siegel–Walfisz bound. Its exact conclusion is

$$
\sum_{\substack{d\le x^\vartheta\\d\ {\rm odd,\ squarefree}}}|r(d)|
\ll xL^{-D}+X_A L^{-18}
\quad(\vartheta<1/2,\ D>0\ {\rm fixed}).
$$

The block-sieve construction is checked with absolute coefficients at most
one and level z^(4h+2). Full-cell proxy mass matching handles principal
characters; the supplied discrepancy holds for all actual interval cuts.
The local density transfer from 2u+1 to 2u-1 uses
log(2u-1)/L=1+O(1/L), not an assumed distribution of shifted primes.
The finite-simplex minimum-coordinate identity supplies precisely the
subtracted composite density D_b1(1)-1. The remainder 1 is the one-prime
term. The least-prime bins include repeated prime factors and all endpoints
of the claimed support; their Type I remainders have no divisor multiplicity
loss because pd has a unique prime factor above W.

For the balanced part, both prime-proxy replacements are justified,
including the second with an arbitrary bounded first proxy. The mask
majorant keeps the entire integer slot in D_1, counts exactly one distinct
mark per group, and allows nonsquarefree D_1. The successor congruences are
mn=-1 modulo D_1 and modulo a banned odd prime. They have phi(D_1) and
l-1 unit-pair solutions respectively, while the roughness failure mn=0
has 2l-1 solutions. These two prime-level failures are disjoint.

For M_i=O(x^0.54), D_1<=x^(1/20) and D=x^(10theta)<=x^(1/20), the
lattice errors after assignment summation are at most
x^0.64 L^C H_Q^mic, negligible compared with X_A V(W)^2.
The main term is bounded by

$$
xV(W)^2V(x^\theta)H_Q^{\rm mic}H_P\ll X_A V(W)^2.
$$

The exact inequality
H_P>=product_(group p)(1+q/(p-1))>=1 supplies the mask compensation.
This proves the complete balanced specialization with its constant fixed
before kappa, b_1, j_**, S and the analytic precisions. It also identifies
exactly where an unrestricted dyadic formulation fails.

Choose early geometry, the candidate prefix, j',theta and j_0; then choose
kappa with C_bal kappa<mathfrak S/4; then b_1, j_**, and a finite mesh.
Choose Type II saving and its K_0,D_0,B next, and finally S>2B+3.
The proxy coefficient bound stays one independently of S, so this order is
acyclic. The resulting prime mass is at least mathfrak S X_A/(5L).
The maximum summand exp(C_w sqrt L) and injectivity of u -> 2u-1 give
the asserted distinct-prime count. Since p+1=2u, the extra factor 2 is
also below x^delta eventually. Setting x=y and comparing logarithms
proves A+ for every sufficiently large real y.

### 3. Products, overlap deletion and gcd fibers

The [counting keeper](counting_keeper.md) uses only A+ and elementary
integer arithmetic. For 0<epsilon<1 fix B>=8/epsilon,
eta=epsilon/16, delta=1/(2B), y=(log x)^B, and
k=floor(log x/log(5y+1)). There are
M>=(log x)^(B(1-eta)) eligible primes, and their distinct k-subset
products give

$$
N=\binom Mk,\qquad
\log N\ge(1-\eta-1/B)\log x-o(\log x).
$$

They are squarefree and strictly below x, while their sigma values are
at most x and sqrt(log x)-smooth. The number U of possible values obeys
log U=o(log x). Cauchy's inequality gives at least N^2/U ordered
equal-value pairs.

With t=ceil(eta k), the fraction of all product pairs sharing at least
t primes is at most 2^k(2k/M)^t=o(1/U). Deleting them leaves at least
N^2/(2U) equal-value pairs and removes the diagonal. Writing a=gu,b=gv
then gives g<x^eta. Squarefreeness makes g,u,v pairwise coprime, so
sigma(g) cancels and sigma(u)=sigma(v). For each unordered reduced
pair and each g there are at most two ordered preimages; the total
fiber is at most 2x^eta. Consequently

$$
h_{\rm sf}(x)\ge\frac{N^2}{4Ux^\eta},\qquad
\log h_{\rm sf}(x)\ge(2-3\eta-2/B)\log x-o(\log x).
$$

Since 3eta+2/B<=7epsilon/16<epsilon, the strict bound follows.
The floor in k and the choice 5y+1 preserve b<x for real x, including
integer x. The final identity h(x)=h(ceil x), and the same for h_sf,
is correct for this strict endpoint. Larger epsilon follow from any
smaller fixed loss in (0,1).

### Coverage of supplied source reconstructions

All essential deductions, not just the displayed substitutions, were
examined. Source Section 6 was compared with every stage of the signed
proof. Source Section 7 was read through candidate mass, Type I, the
preliminary sieve, proxy construction, local densities, away-from-balance
subtraction, the full mask/CRT/sieve argument and the final parameter
choices. Every use of an assumed E result was compared with its actual
statement and the supplied local proof. Section 2's consumed moment,
Fourier, harmonic-character and block-sieve arguments were checked at
their displayed scopes; their external classical boundaries remain
explicit. The unused derivative and mean-square statements were read
but are not certified as additional conclusions of this report.

The entire counting exposition and the catalog formulation were checked,
including the two last real-variable quantifier paragraphs. No original
classical proof, omitted proof of P, or original PDF fidelity is claimed.
Those are boundaries of the commission, not deductions silently omitted
from the conditional chain.

## Strongest attack and exact witness

The separate “Dyadic bound” at extraction lines 256–266 writes only the
condition M_1 M_2 comparable to x. Its proof later uses M_i<<x^0.54.
The heading “Balanced composites” and its surrounding application explain
the intended balanced use, but the isolated unrestricted assertion is false.

Take x=2^j tending to infinity, the dyad m in [1,2), and n in [2x,4x).
Then m=1 is W-rough by convention and M_1M_2=2x meets the written
product-size condition. Smooth compact support gives Psi(1)=Psi(2)=0;
every nonzero candidate term has x<u<2x and belongs to this n dyad.
Thus the displayed sum is exactly

$$
S_W=\sum_{P^-(2u-1)>W}A(u)\Psi(u/x).
$$

Type I and the same block sieve, with cutoff W and
h=2 ceil((log log x)^2), give

$$
S_W\sim\mathfrak S X_A V(W),\qquad
\frac{S_W}{X_A V(W)^2}
\sim\mathfrak S e^{\gamma_E}\sqrt{\log x}\longrightarrow\infty.
$$

The sieve level is x^o(1) and its absolute error is
O(xL^(-D)+X_A L^(-18)), smaller than the displayed main term when
D>C_A+10. The [extraction keeper](extraction_keeper.md), subsection 6,
retains the complete argument, including endpoints. This is an asymptotic
mathematical witness under the E inputs, not a numerical search or an
assumption that primes themselves have positive density.

Accordingly the unrestricted auxiliary formulation is **refuted-as-stated**.
If the balanced restriction is understood as inherited from the preceding
paragraph, the assertion has exactly the specialization proved in the
keeper and the witness is outside that specialization. Both readings are
reported explicitly. No stronger unrestricted lemma is accepted here.
The actual successor proof only uses balanced dyads, whose complete proof
survives. Therefore this witness does not refute the commissioned terminal
implication and does not establish that its essential proof is defective.

The reusable failure is loss of a roughness factor when a variable
degenerates to 1: a product-size condition does not keep a two-variable
sieve inside the range in which both density savings and the lattice
error are uniform. Future use of this display outside balanced dyads would
require a different estimate. No search for such uses outside the frozen
subject was performed.

Other serious attacks were the signed determinant converse, normalization
by Z, the growing number of Fourier variables, a possible circular choice
of discrepancy and proxy precision, nonsquarefree D_1, equality of sigma
after gcd cancellation, and large fibers of the reduced-pair map. The
three keepers retain why each fails on the hypotheses actually supplied.
These attacks do not rely on agreement with an author's computation.

## Checklist

The following gives every canonical bullet and named pattern in
docs/verification.md, followed by every Erdos-specific item. Applicable
findings concern this conditional implication; the auxiliary scope defect
is retained wherever it bears on an item. Inapplicable modes are identified
explicitly rather than treated as successful tests.

### Canonical failure modes

| Item | Verdict and reason |
| --- | --- |
| Almost all quietly upgraded to all | **refutation-failed.** The extraction is eventual for every real x, A+ for every real y, and the counting argument evaluates A+ at y=(log x)^B. No density-one set or subsequence is substituted. |
| Induction presupposing termination | **refutation-failed.** The slot allocation has a specified finite O(log log x) list; its residual invariant is proved through that list. The final counting proof uses no open-ended iteration. |
| Probabilistic or averaging heuristics presented as proofs | **refutation-failed.** Mask expectations are exact finite product identities used in pointwise majorants; block-sieve independent probabilities evaluate multiplicative main terms. Collision and overlap estimates are deterministic inequalities. |
| Circular use of an equivalent statement | **refutation-failed.** P/E are exposed antecedents. Signed Type II, Type I and extraction precede A+, which precedes counting. The parameter order has no feedback through proxy size. |
| Exceptional sets dropped from density arguments | **refutation-failed.** Group tails, coprimality errors, cut cells, repeated prime factors, least-prime boundaries, balanced squares, the diagonal and large-support overlaps all have explicit bounds or inclusion rules. |
| Finite verification beyond base-case coverage | **Inapplicable.** No finite mathematical computation or case table supports an asymptotic assertion. Administrative byte comparisons establish identity only. |
| Relaxed or averaged convergence substituted for actual objects | **refutation-failed.** The exact determinant correspondence, Type II proxy errors, pointwise mask majorant and gcd fiber bound each provide the required transfer to the original integers and pairs. |

### Named canonical patterns

| Pattern | Verdict and reason |
| --- | --- |
| Model-class transport instead of entailment | **Inapplicable as a classification claim.** No extension of an axiom system is classified. The relevant analytic sign and proxy transfers are explicitly proved in the keepers, rather than inferred from similar notation. |
| Infinite uniformity from finite instances | **refutation-failed for the needed implication.** Constants independent of j_**, S and kappa are justified at their exact uses; thresholds may depend on fixed choices. The broader dyadic range has the **refuted-as-stated** witness above, not finite support for a uniform claim. |
| Extremal claims in their own units | **refutation-failed for the pair bound.** The exponent is computed for actual unordered reduced pairs with the 2x^eta fiber cost, not merely for products or collisions. The auxiliary comparison is tested in its own units S_W/(X_A V(W)^2), which diverge under the unrestricted reading. No optimality or attained supremum is asserted. |
| Consequence sentences as claim surfaces | **refutation-failed for the terminal consequences; the unrestricted dyadic formulation is refuted-as-stated.** Weighted-to-distinct-prime counting, p+1 smoothness, A+, the interval containment, strict real-x counting, and the exponent interpretation are checked individually. The characterization of Li–Zhuang Theorem 1.4 is limited to supplied wording and arithmetic interval containment; original-source fidelity is unavailable. |
| Carry actual quantified hypotheses | **refutation-failed for the needed chain.** Full P endpoint classes and signs, E uniformities, actual interval cuts, fixed-parameter order and squarefreeness are carried. Balance is required by the dyadic proof and is present at every use; its omission from an isolated unrestricted formulation is the recorded scope defect. |
| Composition inherits unproved premises | **refutation-failed as a conditional theorem.** P and E, including classical inputs, remain explicit assumptions; neither is promoted to a conclusion. No essential extra native premise was found. Treating this report as unconditional would exceed its finding. |
| Reproducibility notes are claims | **refutation-failed for the retained written route.** Exact frozen inputs and all three written derivations are supplied; the route below needs no unavailable program or external extraction. No numerical pass count is claimed. Public adoption is an owner obligation, not an accomplished fact here. |
| Verifier quotations are claims | **Inapplicable to the supplied subject.** No prior report or quoted ruling was supplied or read, and standing prose was excluded. A distinct grader or integrator must check any future characterization against this report. |
| Verdict words spelled in full | **Satisfied.** Mathematical verdicts are written as refutation-failed and refuted-as-stated, with their different scopes. No abbreviation conflates them. |
| Certified-bracket functions fail loudly | **Inapplicable.** There is no numerical bracket, enclosure, iteration-cap computation or periodic-phase routine in this examination. |
| Every computational leg has a failing input | **Inapplicable to mathematics.** No computational leg is offered as mathematical evidence. The concrete asymptotic witness above, rather than an always-passing script, tests the dyadic assertion. |
| Gates rerun rather than read caches | **Inapplicable.** The verdict relies on no repository gate or cached mathematical output. Administrative identity checks read current bytes and confer no mathematical standing. |

### Erdos-specific checklist

| Item | Verdict and reason |
| --- | --- |
| Quantifiers and scope | **refutation-failed for the full conditional conclusion.** Every fixed epsilon, sufficiently large real x, strict a<b<x and every pair condition are retained. No uniform threshold as delta tends to zero is needed. The unrestricted auxiliary range is separately **refuted-as-stated**. |
| Circularity | **refutation-failed.** The logical order and the order of fixed choices are explicit. A+ is proved from P/E, not borrowed as an unconditional result; the counting proof then uses A+ at one fixed specialization for each epsilon. |
| Model and convention changes | **refutation-failed.** Both shift signs, inverse-2 versus negative inverse-2 residue classes, character conjugations, harmonic normalization, integer slots, repeated band factors and distinct group counts are checked. Squarefreeness is constructed in the terminal products rather than assumed of the analytic candidates. |
| Finite and statistical overreach | **Inapplicable as a source of evidence.** There are no finite computations or statistical samples. Exact finite mask expectations and deterministic Cauchy inequalities are proved identities or bounds. |
| Uniformity | **refutation-failed on every consumed range.** The Fourier exponents precede K_0 where required; the later separation costs precede B; proxy magnitude is independent of S; C_bal precedes kappa. All asymptotic operations keep the stated positive-power parameters fixed. Product-size-only dyadic uniformity fails by the witness. |
| Extremal conclusions | **refutation-failed.** The claimed exponent is obtained in actual pair-count units with an explicit margin epsilon-(3eta+2/B)>0. No sharp threshold, optimal constant or attained extremum is asserted. |
| Consequences and composition | **refutation-failed for P/E to the catalog bound.** All analytic and counting interfaces are supplied at their needed strength; the false unrestricted auxiliary scope is not used. Source-characterization and antecedent-truth limitations are retained. |
| Computation | **Inapplicable.** No mathematical interpreter check was run or needed. There are no floating-point, arithmetic-overflow, sampled-range, cap-exhaustion or failure-exit claims to certify. |
| Reproduction | **refutation-failed for this written assessment.** The package carries the exact seven assessed inputs and full independent keeper arguments. Relative links and the reading route permit reconstruction without another checkout, an omitted PDF or a mathematical program. |
| Source and verdict fidelity | **Qualified at the exact supplied depth.** The local transcription and exposition were checked in full; original classical sources and PDFs were not supplied or read. Source statements remain explicit E hypotheses and source-owned deductions retain attribution. No prior verifier ruling or live problem standing is claimed. This is not an original-source fidelity audit. |

The two neighboring disciplines are also accounted for. There is no
statistical inference or correlated sampling to justify under
docs/approach_vetting.md. Under the evidence contract, the identity checks
have administrative coverage only; the three written keepers cover the
conditional deductions stated above, and neither they nor this report
certify omitted antecedent proofs or original-source fidelity.

## Premises and source boundaries

The premise census was derived from the actual frozen statements, proofs
and consequence sentences. It found no native L-claim consumed as an
established premise. No live ledger reading was authorized or performed,
and no pending native grade is being used prospectively. This finding
does not come solely from the empty metadata list. The actual dependency
account at this examination date is P/E, signed Type II and Type I,
the complete successor extraction, A+, then the counting reduction.
All the internal deductions are examined here in that acyclic order.

[The premise account](premises.md) records the complete P statement and
coefficient classes, the exact E clauses, and the PNT, Mertens,
Siegel–Walfisz and multiplicative large-sieve forms, their source and
version locators, exact specializations and reading depths. The supplied
classical statements were checked against their uses; the original
classical works were unread. The local moment, Fourier, harmonic-character,
block-sieve and density reconstructions consumed here were examined at
their displayed scope. Ford–Halberstam and Buchstab are credited behind
supplied local constructions, rather than invoked as unspecified stronger
external theorems.

The weighted-dilation source is OpenAI's unrefereed
Weighted dilation graphs, smooth shifted primes and totient fibers,
24 September 2026 release. Only the supplied Sections 2, 6 and 7 and
bibliography were read; Sections 3–5 and the proof of P are outside this
examination. The supplied P is the operative conditional hypothesis;
its stated identification with Theorem 5.1 is not a PDF-fidelity finding.

The successor application and counting reduction are attributed to
Shisheng Li and Zhong Zhuang. The latter is identified as Theorem 1.3
and Section 3, pages 1–3 of the 11 October 2026 draft
Coprime pairs with equal sum of divisors, assuming smooth shifted primes,
following Pollack and Pomerance after Erdos. The complete counting
argument supplied here is project exposition, credited with its parameter
checks to Plasma AI. That entire exposition is examined; the original
Li–Zhuang PDF was not supplied and is not certified. The extraction's
last sentence about Theorem 1.4 supplies a source characterization, not
a new premise: the interval inclusion is checked, while the external
theorem's original wording remains unread.

No additional essential premise beyond the explicit P/E interfaces was
found for the terminal implication. The balanced range needed for its
dyadic estimate is already supplied by the actual factor range; accepting
an arbitrary-dyad estimate would add an invalid assertion. Truth of P/E,
original-source fidelity and live external acceptance are unresolved
boundaries, not hidden warrants for an unconditional result.

## Reproduction and retained evidence

Keep this report, the three keepers, the premise account and the seven
files in the retained subject directory together. The retained assets are copies of the supplied neutral extraction with only the mechanical
maintenance listed on the record index, including its omission markers and
metadata with the private revision removed. They are not a new extraction from a source revision.
This permits the owner to file a complete, ordinary-clone-readable
assessment without depending on private runtime state.

The written reproduction route is:

1. Read the seven retained inputs and the exact assumptions in premises.md.
   Compare the statement to the real-x restatement above.
2. Recompute the allocation invariant, signed determinant correspondence,
   endpoint factors and choice order in signed_keeper.md. Only P's displayed
   bound and the stated fixed-moment/Fourier inputs are assumed at that bridge.
3. Follow extraction_keeper.md through Type I, the proxy and density
   interfaces, both composite ranges, the entire mask/CRT/Euler-product
   bound, and the exact unrestricted-dyad witness. Confirm the two uses have
   different ranges before drawing a verdict.
4. Follow counting_keeper.md through the binomial estimate, collision
   count, overlap deletion and gcd fibers. Check both strict inequalities
   and the final two quantifier paragraphs against the retained exposition.

There is no executable rerun command because there is no mathematical
computation in this evidence. No attempt is made to turn administrative
byte equality into proof. All the retained formulas use the displayed
inputs rather than source-revision lookups, generated views, unavailable
evidence runtimes or previous reports.

## Verdict, limits and grading

**refutation-failed** for the complete commissioned implication from
the explicit P and E hypotheses to
h(x)>=h_sf(x)>x^(2-epsilon), for every fixed epsilon>0 and all sufficiently
large real x with all stated pair conditions. The full deductions and
the required source-proof reconstructions were examined at their supplied
interfaces. No essential additional premise or unsupported inference was
found in the actual balanced application.

**refuted-as-stated** for the isolated unrestricted “Dyadic bound” with
only M_1M_2 comparable to x. Its exact witness is m=1 and
S_W/(X_A V(W)^2) tending to infinity. If balance is inherited from the
surrounding section, the retained proof verifies that inherited
specialization. The report accepts no unrestricted reading and asserts
no disproof of the terminal catalog implication.

This examination establishes neither P nor E, does not certify the omitted
weighted-dilation argument or any original classical proof, performs no PDF
fidelity comparison, and awards no tier or unconditional conclusion about
Problem 824. It covers only the retained frozen text. There is no unfinished
essential deduction inside that conditional scope; external assumption
truth, original-source fidelity and acceptance remain outside it.

A distinct grader must decide report-contract compliance, independence,
the procedural disclosure's materiality and the weight of these scoped
findings. The authorized owner must preserve the complete package, resolve
the auxiliary wording before relying on it elsewhere, and assess any
affected consumers within an authorized scope. Public filing and grading
are not completed by this private examination.

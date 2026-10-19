---
name: problems/discrepancy/E0176/evidence/verify/kitamura/grade
title: "E176 whole-proof examination: independent grade"
desc: Independent grading of the unchanged whole-proof examination of E176 discrepancy bounds, finite minima, one-term cases, and exponential consequences.
created: 2026-10-15T23:59:17Z
updated: 2026-10-16T00:10:49Z
---

# E176 whole-proof examination: independent grade

## Subject, independence and decision

**Grade: PASS for each of the nine assigned conclusions and PASS for the
unchanged report as a whole.** The report's mathematical verdict is
**refutation-failed** on each surface. This grade finds its review warrant
valid within the commissioned scope. It makes no Lean, kernel, compiler,
public standing, problem-status or publication claim.

**Examination date:** 2026-10-15 UTC. **Role:** independent grader, with
disclosed model profile gpt-6-astra, in a fresh isolated context distinct from
both the subject author and the original reviewer. The grader neither
constructed the mathematical subject nor participated in the reviewed
examination. No sibling grade, author inspection account, expected result or
commissioner independence ruling was supplied. The commission charged this
assignment to find grounds to void the report. No excluded exposure occurred
during this grading; no incoming steering was consumed.

The subject is the exact returned [report](../../assets/kitamura/reviewed/report.md), its
[literal driver](../../assets/kitamura/reviewed/rerun.py), [independent finite
program](../../assets/kitamura/reviewed/finite/independent.py), positive and negative inputs, all
retained results and witnesses, and the complete unchanged subject snapshot
under [reviewed/subject](../../assets/kitamura/reviewed/subject/manifest.json). The mathematical
snapshot was frozen on 2026-10-15 at 13:17:10.123503 UTC; the returned report's
freeze record is dated 15:29:39 UTC; the grading packet was prepared at
16:42:24 UTC. The commissioned later grading pin, rather than either older
identity alone, was checked against the rendered charter and resolved. The
operating instructions were separately identity-checked. Those custody facts
and the exact source map are retained privately, separate from this
mathematical account.

All 39 returned delivery files are preserved unchanged at `reviewed/`. All
31 delivered subject files agree byte-for-byte with their original-subject
counterparts. Every substantive report, keeper and subject text was read
completely, including both analytic source slices, all five small-case Lean
files, all 17 runtime import files, and the complete finite data. The full
original-record inventory was inspected to the depths stated below and in
the private custody account. Original instructions and communications were
read as historical evidence only. The report has not been repaired or
rewritten, and no finding here supplies a missing part on behalf of its
author.

The grading standard is the unabridged `docs/verification.md`, including
“Report contract,” “Independent routes and repeated review,” the canonical
failure modes and named patterns, and the Erdős-specific whole-claim
contract and checklist; together with the complete
`campaign/guides/verification.md` adapter. `docs/evidence.md` was read before
the fresh mathematical runs. No repository battery or formal execution was
used as evidence.

## Separate conclusion grades

Use the report's exact convention: for each positive integer length $n$,
every coloring $f:\{0,\ldots,n-1\}\to\{-1,1\}$ must admit integers
$a\geq0,d\geq1$ with $a+(k-1)d<n$ and

$$
\left|\sum_{j=0}^{k-1}f(a+jd)\right|\geq\ell.
$$

$N(k,\ell)$ is the least **positive** successful length, when one exists.
Set

$$
T_2(k)=\frac{2(k^2-1)(k-1)(2k+1)}{k-3},\qquad
T_s(k)=\frac43(k^2-k+1)(k-1)(k(k-1)+1).
$$

The divisions are real divisions before the floor. Translation to
$\{1,\ldots,n\}$ changes neither the property nor its minimum. The target
correspondence is `ell_two` and `ell_sqrt_k`; `ell_ck` is not covered.

| Surface | Exact conclusion graded | Review-warrant grade | Mathematical verdict and reason |
| --- | --- | --- | --- |
| 1 | Every integer $k\geq5$: existence and $N(k,2)\leq\lfloor T_2(k)\rfloor+1$. | **PASS** | **refutation-failed**. The normalized Fourier identity, unweighted consequence of the pair-energy bound, exact wrap loss and positive strict gap are all supplied. Existence precedes least-value selection. |
| 2 | Every integer $k\geq2$: existence and $N(k,\sqrt{k})\leq\lfloor T_s(k)\rfloor+1$. | **PASS** | **refutation-failed**. The exact weighted identity, both weight sums, integer-square cap $k-1$, strict gap and minimum bridge are supplied independently of surface 1. |
| 3 | $N(2,2)=3$, with failure at every smaller positive length. | **PASS** | **refutation-failed**. Pigeonhole gives the upper value; opposite signs give the boundary witness. Exact rerun and partition counts cover every lower length. |
| 4 | $N(3,2)=9$, with failure at every smaller positive length. | **PASS** | **refutation-failed**. Complete partition inclusion-exclusion yields zero avoiders at 9 and positive counts at all smaller lengths, with concrete witnesses and a justified sign/AP bridge. |
| 5 | $N(4,2)=13$, with failure at every smaller positive length. | **PASS** | **refutation-failed**. Balanced four-block recurrence classifies all candidates; the difference-four AP first enters at length 13 and eliminates them. Fresh counts reproduce all lower cases. |
| 6 | $N(1,2)$ does not exist at any positive length. | **PASS** | **refutation-failed**. Every one-term sum has magnitude one, for every coloring, start and positive difference; every positive interval has colorings. |
| 7 | The actual positive minimum $N(1,1)=1$. | **PASS** | **refutation-failed**. At length one, $a=0,d=1$ is admissible and attains equality. One is the least positive length. No guarded fallback is used. |
| 8 | Every integer $k\geq2$: $N(k,2)\leq16^k$. | **PASS** | **refutation-failed**. Surface 1 and a uniform rounding/comparison argument cover $k\geq5$; surfaces 3–5 cover exactly 2, 3 and 4. The nonexistent one-term target is excluded. |
| 9 | Every integer $k\geq1$: $N(k,\sqrt{k})\leq64^k$. | **PASS** | **refutation-failed**. Surface 2 and its own uniform comparison cover $k\geq2$; surface 7 supplies the actual positive base at 1. |

These are grades of the returned examination. They do not extend to any
unseen correction, another version of a source, or an expanded claim.

## Original independence warrant

The independence ruling rests on the primary records, not the report's
self-description. The retained launch, original operating, native-session,
continuation, residual-execution and historical Git records were assessed
together. Derived navigation and equality checks locate and corroborate
those records; they do not replace them.

The original launch created a separate local, blind, sealed, no-sync
assignment with zero descendant authority and a refutation charge. Its
exact mathematical extraction and separately frozen operating inputs were
present before startup. The native inventory contains a generic readiness
probe and the review's own three-step context. The probe received the root
instructions and a content-free response request; it performed no tool
calls. The main context's visible incoming user material consists of the
root instructions and the three commissioned step prompts. Their assignment
and step bodies match the frozen original charter and steps. The visible
developer material is general operating guidance, not mathematical steering.
The visible replacement contexts at both compactions preserve those same
received messages; they introduce no other review or author advocacy.
Opaque internal fields were not decoded.

All 91 recorded tool-call commands were inspected as data for their actual
read, execution and write scopes. The substantive source-reading outputs
corroborate the reported complete reading, including the full 1702-line
Basic slice, 964-line Sqrt slice, finite files and 17 runtime files. The
recorded commands do not open an inbox, read a feed or sibling context,
extract canonical mathematics, merge a parent, browse, launch descendants,
run Lean, or execute a repository battery. Large report-writing commands
write the reviewer's own report and continuation; they are not incoming
evidence. The original reviewer consulted only the permitted operating
context, frozen subject, own outputs and authorized boundary commands.
Repository utilities defined in the supplied import closure were read but
were not invoked by the finite checker.

Preflight, post-start and settled-return subscription receipts are empty.
The startup sent receipt is empty; the settled receipt contains the
reviewer's outbound delivery notice. These facts concern subscriptions and
outbound traffic respectively. They do **not** establish an empty inbox.
The original private inbox dump is unavailable. The relevant independence
question is whether excluded material reached the review context. The
visible received-context record, exact assignment comparisons, complete
command inventory, lack of inbox/read ingress, and the corroborating
isolation receipts jointly supply sufficient evidence of separation here.
No excluded received text, mathematical encouragement or directed attack
was identified. Nothing in the report requires an excluded source to
explain its content or refutation direction.

**Sufficiency and materiality ruling:** the unavailable inbox is an explicit
evidentiary limit, not evidence that it was empty and not an established
contamination. On the supplied primary record, independence is sufficiently
supported. No exposure requiring a materiality waiver or fresh reviewer is
shown. This ruling does not certify unrecorded private state, and a contrary
primary record would require reassessment; it is not a favorable
commissioner ruling imported into this grade.

The historical Git record supplies the original review's complete
post-input change inventory. Its single iteration-end automatic commit
adds 45 files: one own-memory file, 39 delivery files and five own-work
files, all under the reviewer's own memory or plans. The headless record
and settled return corroborate that order and the clean completed return.
No corpus or input path occurs in that change inventory. Under the adapter's
express automatic-continuation rule, this is an engine action bearing on
neither independence nor scope. Operator setup and input preparation before
review startup are not misattributed to reviewer tool actions. Neither
that commit nor a finish receipt supplies a mathematical verdict.

The original reviewer is therefore eligible on the supplied record. Using
the same disclosed model profile for separate fresh assignments does not
make the grader the author or reviewer. This assignment assesses one review
and its internal disjoint computational route; it claims no second
independent review cycle.

## Mathematical adjudication and adversarial checks

### Common Fourier, Fejér and model interfaces

The report rederives the common identities rather than citing an unexamined
Cassels or Turán result. I checked the actual normalization: with
$\widehat f(t)=n^{-1}\sum_a f(a)\omega^{-ta}$, geometric orthogonality
gives inversion and $\sum_t|\widehat f(t)|^2=1$. Consequently the cyclic
second moment is

$$
M_d=\sum_t|\widehat f(t)|^2
       \left|\sum_{j=0}^{k-1}(\omega^t)^{jd}\right|^2.
$$

There is no extra factor of $n$. The geometric proof uses $n>0$, not
primality or invertibility of $d$. Repeated cyclic residues do not defeat
the identity, and $n=1$ has just the diagonal orthogonality case.

For a unit $z$, expansion of the report's pair energy over
$p,q=0,\ldots,k-1$ and $r,s=0,\ldots,D$ gives

$$
Q=k^2+2\sum_{d=1}^{D}\left(1-\frac d{D+1}\right)|G_d(z)|^2
  \geq k(D+1).
$$

For each positive difference $d$, exactly $D+1-d$ pairs have
$r-s=d$, and the same number have $r-s=-d$. Their magnitudes agree by
conjugation. Each $p=q$ term contributes $D+1$ after normalization;
coincident powers do not remove this contribution. Thus both the factor
two and the diagonal lower bound survive. Multiplication by the
nonnegative Fourier masses preserves the bound with total mass one.
The unweighted inequality follows because the weights lie in $[0,1]$.
The report also exposes a nontrivial numerical check at
$k=2,D=4,z=-1$: weighted energy $16/5$, pair energy $52/5$.
This is a normalization attack, not a finite substitute for the identity.

The decisive transfer is the wrap estimate. If $m=(k-1)d$, the number
of starts with $a+m\geq n$ is exactly $\min(n,m)$. Under failure of
the ordinary target, the non-wrapping squared sum is at most $b$, while
all cyclic squared sums are at most $k^2$. Therefore

$$
M_d\leq b+(k^2-b)\frac{\min(n,(k-1)d)}n
     \leq b+(k^2-b)\frac{(k-1)d}n.
$$

The second inequality remains valid when every start wraps. Its coefficient
is nonnegative on the used domains. The endpoint $a+(k-1)d=n$ wraps;
it is never admitted as an ordinary AP. Failure of target 2 gives integer
cap $b=1$; failure of the non-strict square-root target gives
$S^2<k$, hence integer cap $b=k-1$. Squaring is reversible because
both sides are nonnegative. In particular a four-term sum of 2 meets
$\sqrt4$; it must not be excluded as an equality case.

For a non-wrapping start every term is its canonical representative in
$[0,n)$. The Fin/ZMod bijection preserves the sums and normalized
averages, and the squared complex norm of an embedded integer is its real
square. Translation by one is a bijection of ordinary APs with the same
positive difference. These bridges are actual implications, not an
identification of cyclic and ordinary progressions.

The report's strongest attack is substantive: the alternating coloring at
$k=5,n=6$ has ordinary five-term sums of magnitude one, while even
cyclic differences give magnitude five. It refutes the shortcut from large
cyclic energy to an ordinary conclusion. It does not refute the stated
bound, whose wrap loss is paid in full. The period-four example
$(-1,-1,1,1)$ similarly tests the first admissible difference-four
endpoint. The original report already contains both witnesses and the
reason the full proof survives them.

### The two polynomial conclusions and minimum selection

For discrepancy 2, put $D=2k$. The lower average is $(k+1)/4$.
The upper average under failure is

$$
1+\frac{(k^2-1)(k-1)(2k+1)}{2n}.
$$

Their difference is exactly

$$
\frac{k-3}{4}\left(1-\frac{T_2(k)}n\right).
$$

This is positive for every integer $k\geq5$ and $n>T_2(k)$.
At $k=5$, $T_2=1056$: equality gives no contradiction, whereas
the prescribed length 1057 gives gap $1/2114$. This verifies that the
report's floor-plus-one step preserves the needed strict inequality.

For the square-root target let $K=k(k-1)$,
$A=(k^2-k+1)(k-1)$, and $D=2K$. Direct finite summation gives

$$
\sum_{d=1}^{D}w_d=D/2,\qquad
\sum_{d=1}^{D}d w_d=D(D+2)/6.
$$

Subtracting the weighted wrap upper bound from the weighted moment lower
bound yields

$$
\frac K2-\frac{2AK(K+1)}{3n}
=\frac K2\left(1-\frac{T_s(k)}n\right)>0.
$$

Here $K>0$ is guaranteed by $k\geq2$. At $k=2$, the threshold
is 12 and the gap at 13 is $1/13$. The report does not consume the
discrepancy-2 polynomial theorem at this step: only the common identities
and model bridge are reused. Natural subtractions and coercions agree
with the displayed real differences on their expressly stated domains.

For each positive threshold $T$, $B=\lfloor T\rfloor+1$ is a
positive integer strictly greater than $T$, including integral $T$.
The contradiction first establishes a successful length $B$. Only then
does well-ordering give a least positive successful length at most $B$.
The source properties require positivity, so the in-range `Nat.find`
selection agrees with that minimum. `N176` below its $k\geq5$ guard
and `N176Sqrt` below its $k\geq2$ guard return fallback zero; neither
branch proves existence or a positive minimum. The report distinguishes
these meanings explicitly.

For surface 1 the report's three weakest-step groups are normalized
Fourier moments; the pair-energy identity and multiplicities; and wrap,
strict gap and minimum transport. For surface 2 they are the weighted
identity; integer cap with exact weight sums and gap; and ordinary,
non-strict, floor/minimum transport. Each group is rederived in the frozen
report and composes correctly with its neighbors. These are not gaps
filled by this grade.

### Finite minima and structurally disjoint reproduction

The report proves the Boolean-code/sign-coloring bridge. Encoding the
positive signs as binary digits gives a bijection with codes below
$2^n$; every sign coloring is represented. For $k\geq2$, an ordinary
AP contained in $[0,n)$ necessarily has $1\leq d<n$, so the source's
bounded difference enumeration loses none. Its endpoint guard ensures
every term is in range. The zero-length case contains one coloring and
no AP and is recorded as a failure only; it is not a positive minimum.

The author route enumerates sign tuples, constructs APs as equally spaced
subsets, and compares them to bounded start/difference enumeration. The
independent route changes both the objects counted and the arithmetic
primitive. For $k=2,3$, failure of target 2 is exactly absence of a
monochromatic AP. Endpoint interpolation generates the constraints. The
product of their complementary indicators expands into inclusion-exclusion
over subsets of constraints. Each chosen subset imposes equality classes
on vertices and admits $2^c$ assignments, where $c$ is its number of
classes. Aggregating signed coefficients by canonical partitions is exact;
merging labels by their minimum preserves that canonical representation.
The program performs this recurrence over the complete finite edge list,
not over sign tuples.

Conditional counts fix prefix signs, reject inconsistent class assignments,
and contribute $2^{\text{free classes}}$. They therefore construct the
first lexicographic witness without the author's sign-loop stopping rule.
The full endpoint inventories, coefficient polynomials and branch counts
are retained. At the upper lengths the polynomials are

$$
q^3-3q^2+2q
$$

and

$$
q^9-16q^7+21q^6+42q^5-101q^4+58q^3+5q^2-10q.
$$

Both evaluate to zero at $q=2$. This evaluated identity is warranted by
the full finite recurrence and its mathematical reduction, not by quoting
those coefficients alone.

For $k=4$, missing target 2 forces every four-term AP sum to be zero.
Subtracting consecutive length-four blocks forces $f(i+4)=f(i)$.
For lengths 4 through 6, the six balanced four-symbol seeds are all
possibilities and only difference one occurs. At length 7 the
progression $0,2,4,6$ forces opposite entries two positions apart, so
the seed is $(u,v,-u,-v)$, with four choices. Through length 12 every
admissible difference is at most 3: odd differences visit all four
residues and difference two visits an opposite pair twice. Every such
sum is zero. At length 13, $0,4,8,12$ has sum $4u\ne0$.
Thus the program's empty seed list at 13 encodes a proved obstruction,
not an assumed answer. No four-term AP exists below length 4.

The complete fresh census is:

| $k$ | Lengths in order | Avoiding counts in that order |
| --- | --- | --- |
| 2 | 0 through 3 | 1, 2, 2, 0 |
| 3 | 0 through 9 | 1, 2, 4, 6, 10, 14, 20, 16, 6, 0 |
| 4 | 0 through 13 | 1, 2, 4, 8, 6, 6, 6, 4, 4, 4, 4, 4, 4, 0 |

The endpoint inventory is independently checked against
$mn-(k-1)m(m+1)/2$, where
$m=\max(0,\lfloor(n-1)/(k-1)\rfloor)$. This follows by summing the
$n-(k-1)d$ legal starts over $1\leq d\leq m$. The first avoiding
witnesses at lengths 2, 8 and 12 are respectively $(-1,1)$, two
repetitions of $(-1,-1,1,1)$, and three repetitions of that block.
Every earlier positive length has a positive avoiding count and a retained
witness; no appeal merely to the immediately preceding length is needed.

The frozen report's weakest steps for surface 3 are code coverage,
pigeonhole upper bound and opposite-sign lower bound. For surface 4 they
are the monochromatic equivalence, partition inclusion-exclusion, and
zero/positive counts with witnesses. For surface 5 they are the period-four
recurrence, difference-two seed reduction, and the exact first
difference-four obstruction. All are explained and independently derived
in the report. Its attempted smaller minima fail with counts 2, 6 and 4;
the possible surviving upper-length colorings are excluded by the separate
partition or recurrence reasoning. This tests the original sign-enumeration
failure class by a structurally different route.

### One-term results and consequence dependencies

For surface 6, a one-term sum is always a single sign. Increasing the
interval length or difference cannot make its magnitude 2. For surface 7,
$a=0,d=1$ at length one has endpoint zero and magnitude one, which
meets the non-strict target. Requiring a second distinct point for this
one-term AP or substituting a guarded source zero changes the subject.
These are the weakest deductions and strongest attempted convention
attacks in the frozen report; their elementary direct proofs cover every
stated sign and length.

For surface 8 the report uses, for $k\geq5$,

$$
T_2(k)\leq18k^3,\qquad
\lfloor T_2(k)\rfloor+1\leq19k^3\leq16^k.
$$

The factor estimates use $k-3\geq k/3>0$, and the final comparison
uses $k\leq2^k$ and $19\leq2^k$ only where $k\geq5$.
The induction $k+1\leq2k\leq2^{k+1}$, with base one, justifies the
first inequality uniformly in the parameter. The verified minima 3, 9
and 13 cover exactly $k=2,3,4$. The strongest domain attack would
leave one of these bases unsupported or include $k=1$; neither happens.

For surface 9 the separate estimates are

$$
T_s(k)\leq\tfrac43 k^5,\qquad
\lfloor T_s(k)\rfloor+1\leq3k^5\leq64^k
\quad(k\geq2).
$$

Here the three factors are bounded by $k^2,k,k^2$, and
$3\leq2^k$ is used only for $k\geq2$. The actual minimum at
$k=1$ gives $1\leq64$. The report never uses either the false
inequality $3\leq2^1$ or fallback zero to fill that base. For each
exponential its three weakest groups are the appropriate polynomial
existence result, rounding and uniform comparison, and the exact remaining
bases. Their dependencies are tested before the consequences below.

## Execution and reproduction claims

The original records corroborate actual author, independent and negative
executions, including the exact package-relative command and its direct
independent counterpart. The residual products include their concrete
results and import traces; they agree with the returned data. I did not
substitute these historical successes for a new execution.

The complete 39-file returned directory was reconstructed byte-exact in
the grader's authorized scratch. From that directory I executed both
shell blocks under the report's “Reproduction” heading literally, with
`REVIEW_SCRATCH` set to a separate absolute scratch directory. All
environment clearing, `nice -n 10`, one-thread variables, `uv run
--no-sync`, `-B`, file arguments and script contents were preserved. The
source map, real command, working directory, times, exits and stdout/stderr
are retained privately. Execution on 2026-10-15 UTC produced:

| Run | Observed result |
| --- | --- |
| Literal `rerun.py` command | Exit 0; about 0.19 seconds; fresh author, independent and control executions completed sequentially. |
| Actual unchanged author script | Exit 0; 28 rows, 17,421 sign tuples; its four diagnostics per case printed. |
| Independent positive input | Exit 0; all 28 count/witness rows and certificates equal the retained data. |
| Independent false-minimum input under `python -O` | Exit 1; false minima 2, 8, 12 rejected with respectively 2, 6, 4 avoiders. |
| Literal direct independent command | Exit 0; about 0.04 seconds; its complete JSON equals the retained independent result. |
| Actual script import origins | Exactly the 17 supplied `tools` files; no substitution of the live repository package. |

Fresh mathematical products are retained at
[fresh/author_results.json](../../assets/kitamura/fresh/author_results.json),
[fresh/independent_results.json](../../assets/kitamura/fresh/independent_results.json),
[fresh/negative_results.json](../../assets/kitamura/fresh/negative_results.json) and
[fresh/direct.json](../../assets/kitamura/fresh/direct.json). Required code and exact input files
remain unchanged at `reviewed/`; the report's commands run from that
directory in an ordinary clone with the declared prepared Python
environment. The commands select disposable output explicitly and do not
write into the reviewed snapshot. No scratch-only mathematical code is
needed to reconstruct the results.

The driver executes the generators before comparing their outputs; it
does not accept stored success. Its explicit `require` checks survive
optimization. The independent program uses exact integers, rejects
unsupported input domains, and has explicit nonzero failure paths. Its
retained negative input is genuinely false in each of the three cases,
and the optimized run demonstrably rejects it. The false-input controls
exercise the minimum claims, not every internal consistency guard.

The author's re-evaluation of its own chosen witness uses the same AP
predicate as its discovery loop. That internal diagnostic has no
additional independence weight. The report explicitly distinguishes the
two author enumerations from independent reproduction, gives hypothetical
invalid inventory/witness data as failure conditions rather than claiming
those mutations were executed, and retains the separate partition and
recurrence derivations and direct witness validation. I do not read its
12-check banner as 12 independent proofs. The finite warrant rests on
the complete census, its reductions, the disjoint reproduction and the
actual false-minimum controls. No tautological diagnostic is needed to
establish any of the nine conclusions.

## Premises, reading depth and order

The premise set was derived from the frozen statement, proof, source
interfaces and consequence sentences, not accepted from an author's list.
**Dependency reading for this grade, 2026-10-15 UTC:** no native claim or
ledger row is consumed. A live ledger read is both unnecessary and outside
the commission. No pending external grade is treated as an established
premise. The source's conditional scalar helpers are discharged internally
before the unconditional bounds; an unexecuted `native_decide` is not a
premise of the finite warrant.

| Exact retained interface | Actual grading reading and ruling |
| --- | --- |
| `reviewed/report.md`, all 838 lines | Whole report, including all nine restatements, derivations, per-conclusion attacks, dependency table, checklists, commands and limits. Contract and claims assessed against actual primary records. |
| `reviewed/subject/statement.md.txt`, `proof.md.txt`, `exponential_consequences.md.txt` | Whole texts, respectively 24, 148 and 15 lines. Every conclusion and consequence examined in the exact ordinary-AP convention. |
| `reviewed/subject/source/nk2_basic.lean.txt`, lines 1–1702 | Whole static text. Wrapping/ordinary sums through line 244; pair energy through 739; finite Fourier/moments through 1108; Fin/ZMod bridge through 1324; threshold, good-length and least-value definitions through the final public bound. Essential mathematical deductions verified; no elaboration or axiom audit. |
| `reviewed/subject/source/nksqrtk_sqrt.lean.txt`, lines 1–964 | Whole static text. Weights and multiplicities through 260; weighted moments and ordinary existence through 766; floor and least-number interface through 964. Common Basic mathematics is used, not its discrepancy-2 conclusion. |
| `SmallKCommon.lean.txt`, `K1.lean.txt`, `K2.lean.txt`, `K3.lean.txt`, `K4.lean.txt` under `reviewed/subject/source/` | Whole static texts, 45, 27, 23, 23 and 23 lines. Boolean-code guard, all-lower-length meaning and one-term model inspected. Finite claims re-established without executing source decisions. |
| `reviewed/subject/finite/small_cases.py.txt` and fixture; `reviewed/finite/` code, inputs and all data; `reviewed/rerun.py` | Whole code and complete data, including endpoint inventories, coefficient polynomials, conditional counts, recurrence seeds and first witnesses. Exact author rerun and independent reproduction freshly executed. |
| All 17 `reviewed/subject/tools_runtime/` files | Whole text and import/initialization behavior inspected. Actual imports confirmed in the script run. Uncalled repository utilities carry no mathematical or tool-correctness warrant. |
| Subject manifests and provenance | Whole supplied custody/scope information inspected; all allowed identities checked. Unlisted archive equality, full-source/build fidelity and license text inspection remain outside coverage. |
| Original operating, launch, continuation, two native sessions, historical Git and restored residual records | Full inventory inspected; actual received material, command scopes, substantive reading outputs, actual executions and continuation-commit paths assessed. Opaque fields not decoded; original inbox unavailable. These are review-warrant evidence, not theorem premises. |

The grading order is common identities/model bridges, then surfaces 1 and
2 separately, then surfaces 3–7, followed by surface 8 using 1 and 3–5,
and surface 9 using 2 and 7. Every consumed internal conclusion passes
before its consumer. There is no arrow from surface 1 to surface 2, and
the finite minima consume neither polynomial bound. Neither numerical
comparison in the exponentials would alone validate this composition.

## Complete report-contract adjudication

| Contract part | Grade and reason |
| --- | --- |
| Assignment and exact subject | **PASS.** Refutation charge, frozen neutral extraction, separately frozen instructions, explicit permitted read set and private delivery surface. Source and returned bytes agree with their supplied identities. No unresolved subject defect. |
| Subject and independence | **PASS.** Paths, freeze date, role/model, scope, actual reading, exclusions and exposure claim are explicit. The primary-record assessment above supplies the independent warrant. |
| Restatement, separately for all nine | **PASS.** Every domain, positive length/difference, absolute non-strict target, existence/minimum qualification and real-before-floor operation is preserved. |
| Checklist | **PASS.** Every canonical mode, named pattern and governing Erdős item has an explicit verdict. The tables below adjudicate their substance, including inapplicable modes. |
| Weakest steps, separately for all nine | **PASS.** The frozen report names at most three groups per conclusion and supplies the actual derivations and surrounding composition. The mathematical sections above check them; a table of labels alone was not credited. |
| Strongest attack, separately for all nine | **PASS.** Cyclic-only counterexamples, strict floor/equality boundaries, attempted smaller minima, surviving recurrence candidates, one-term convention changes and consequence-domain gaps are all concretely attacked and resolved in the frozen report. |
| Premises and reading depth | **PASS.** Precise source interfaces and whole/limited reading are identified; all essential common deductions are internal, native premise set empty, and the batch order is acyclic. |
| Computation, required disjoint route and durable keepers | **PASS.** Complete bounded inputs and witnesses, genuinely different partition/recurrence algorithms, mathematical reductions, actual literal rerun and optimized negative controls are retained. Private delivery is sufficient at this stage under the adapter. |
| Verdict, limitations and attribution | **PASS.** Nine full `refutation-failed` verdicts, no formal-execution overclaim, explicit archive/source limits and proper source/preparation/project credits. This grade concerns exactly the unchanged returned report. |

### Canonical failure modes

These rulings apply to all nine surfaces; the applicability distinctions
identify which operations occur in each proof.

| Required mode | Adjudication of the report |
| --- | --- |
| “Almost all” upgraded to “all” | **PASS: not found.** Each fixed coloring has the exact moment identities; all finite assignments are counted; one-term proofs and parameter comparisons are universal on their stated domains. |
| Induction presupposing termination | **PASS: not found.** Partition expansion and prefix construction have explicit finite bounds; $k\leq2^k$ has a base and valid successor step. Other conclusions need no termination premise. |
| Probabilistic or averaging heuristics as proofs | **PASS: not found.** Finite exact sums, nonnegative unit-mass weights and pointwise wrap estimates justify every average. No sampled inference is made. |
| Circular use of an equivalent target | **PASS: not found.** Pair positivity precedes moment bounds, success precedes minimum selection, recurrence obstruction proves the zero seed case, and dependencies are ordered. |
| Exceptional sets dropped from density arguments | **PASS: density form inapplicable.** The relevant finite exceptional starts are explicitly counted and charged in the wrap error; none are dropped. |
| Finite verification beyond its coverage | **PASS: not found.** The census proves the three bounded minima. Polynomial, exponential and one-term universal statements have separate symbolic arguments. |
| Relaxed or averaged system replacing actual objects | **PASS: no convergence claim; transfer risk discharged.** Non-wrapping transport and strict gaps give ordinary APs; Boolean and interval translations preserve the exact model. |

### Named patterns

| Required pattern | Adjudication of the report |
| --- | --- |
| Model-class transport instead of entailment | **PASS.** No axiom-extension classification occurs. The applicable cyclic/ordinary, Fin/ZMod, Boolean/sign and translated-interval implications are actually proved. |
| Uniformity inferred from finitely many instances | **PASS.** Both gaps and both exponential comparisons retain their full parameter dependence; the census is never extrapolated. |
| Extremal claims in the claim's own units | **PASS.** Exact minima are checked as positive interval lengths with upper proofs and every smaller length accounted for. General bounds are not called sharp; fallback zero is excluded. |
| Consequence sentences are claim surfaces | **PASS.** All nine conclusions, the two exponentials and every floor/minimum/model transfer are explicit and separately attacked. |
| Carry hypotheses actually used | **PASS.** Positivity of $n,d,k-3,K$, sign-valued maps, integer-square caps, finite domains and real divisions appear where needed. One-term cases are separate. |
| Composition inherits unproved premises | **PASS.** No missing consumed clause was found. Surface 2 uses common identities independently of surface 1; consequences consume only prior passing surfaces. |
| Reproducibility notes are claims | **PASS.** Both literal command blocks were freshly executed from unchanged bytes. Their stated domain, imports, exits and output equality were observed. The obsolete author docstring path is expressly not the assessed command. |
| Verifier quotations are claims | **PASS.** Prior verifier quotations are inapplicable to the original blind subject; no earlier ruling is imported. This grade checks the returned report's actual verdict words and scope rather than a characterization from another account. |
| Verdict words spelled in full | **PASS.** `refutation-failed` appears separately on every surface and is not conflated with `refuted-as-stated` or `proof defective; statement unresolved`. |
| Certified-bracket functions fail loudly | **PASS: enclosure form inapplicable.** No approximation, capped enclosure or periodic numerical integration occurs. Exact bounded computation rejects malformed or unsupported inputs explicitly. |
| A harness leg with no failing input is decoration | **PASS for the substantive evidence.** Each finite minimum has an actual false input rejected under optimization; incorrect retained counts, witnesses or import origins cause explicit disagreement. The same-predicate author witness diagnostic supplies no additional weight, as explained above. The report's hypothetical bad inventory/witness examples are not falsely described as executed tests. |
| A gate reading caches instead of rerunning is defective | **PASS: no such gate is relied on.** The driver executes author and independent generators and controls before comparisons. Saved concrete data are fixtures, not success receipts. |

The neighboring correlated-sample discipline is inapplicable: there is no
sampling or statistical confidence argument. The evidence-coverage
discipline is satisfied by the explicit separation of static proof reading,
bounded computation and formal execution. This is the first examination;
the second-cycle distinct-attack requirement is inapplicable. The separate
structural-disjointness requirement for its computational batch is met.

### Erdős-specific whole-claim checklist

| Governing item | Adjudication of the report |
| --- | --- |
| Quantifiers and scope | **PASS.** Every coloring, parameter domain, positive minimum and endpoint/equality convention is retained; zero length is a finite control only. |
| Circularity | **PASS.** No target or equivalent target is assumed; the claimed upper values are computed or proved, and minimum selection follows existence. |
| Model and convention changes | **PASS.** Complete bridges are supplied and challenged by explicit cyclic-only and period-four examples. |
| Finite and statistical overreach | **PASS.** The finite domain is exactly 28 rows; no statistical inference occurs and symbolic proofs cover the infinite families. |
| Uniformity | **PASS.** All exchanges are finite; gap constants and error terms remain explicit in $k,n$; exponential comparisons cover the whole stated domains. |
| Extremal conclusions | **PASS.** The actual positive minimum is established in interval-length units, with all lower cases for exact minima and no unsupported optimality claim. |
| Consequences and composition | **PASS.** Both exponentials and their different bases are checked after the respective passing premises; source fallback and a shared source filename are not substituted for an implication. |
| Computation | **PASS for surfaces 3–5 and their finite inputs to 8.** Exact integer domains, full inventories/witnesses and nonzero optimized controls are retained. It is inapplicable as proof support for the analytic and one-term conclusions. |
| Reproduction | **PASS.** Literal fresh execution and direct independent execution agree on complete data; partition and recurrence reductions supply the required different primitive. Purely mathematical deductions have retained derivations. |
| Source and verdict fidelity | **PASS within the extraction.** The report identifies exact external versions and credits, covers only the supplied mathematical text, and expressly withholds archive, license and formal-build warranties. |

## Limits, credits and disposition

No essential mathematical premise or required report-contract component
remains unprovided within this commission. The historical inbox remains
unavailable; the explicit sufficiency ruling above is the basis for passing
independence despite that limit. The retained private primary-record
account states the scope of that ruling and permits its reassessment.

Kenta Kitamura / KitaKen1 owns the original source mechanism. The supplied
Codex 5.5 and ChatGPT 5.5 Pro preparation-assistance credits are preserved.
Plasma AI receives the supplied extraction, finite probe and exponential
deduction credits, and the independent derivation, reproduction and grading
work here. The report's external source versions and qualifications remain
unchanged in its subject and provenance records.

This grade does not establish equality with the unlisted second archive's
Basic file, fidelity of complete source archives, inspection of license
texts, Lean elaboration, `native_decide` execution, compiler or kernel
trust, or a reported build. It does not certify uncalled runtime utilities,
other finite parameters, stronger exponential domains, sharpness of the
general bounds, or bytes written after the frozen delivery.

The private frozen handoff is complete for grading. Public normalization,
durable corpus filing and any authorized standing decision belong to the
responsible integrator and acceptance process. Private records, paths,
hashes and chronological diagnostics remain private. No repaired or
expanded subject inherits this PASS.

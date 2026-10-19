---
name: research/graph_ramsey_interfaces/butterfly_degree_sum_certificate/evidence/verify/whole_conclusion/report
title: Whole-conclusion examination of the E1033 certificate
desc: |
  Independent whole-conclusion examination of the frozen E1033 construction,
  including finite realization, all-order padding, exact arithmetic,
  checker limitations and the catalog asymptotic consequence.
created: 2026-10-15T04:32:53Z
updated: 2026-10-15T04:32:53Z
---

# Whole-conclusion examination of the E1033 certificate

***

## Subject and independence

**Role:** independent whole-conclusion examiner, charged to find a
counterexample, an unsupported essential deduction, or a failure of the
verification contract. **Disclosed model:** gpt-6-astra. **Examination dates:**
2026-10-14 and 2026-10-15 UTC. **Subject freeze:** 2026-10-14 at
23:31:08.459536 UTC. Project mathematics is credited to Plasma AI.

The subject is the entire assertion that every integer $n\ge 10^{13}$ admits
a finite simple undirected graph on exactly $n$ vertices with more than
$n^2/4$ edges and all triangle degree sums strictly below $183n/125$, together
with its asserted implication for the supplied formulation of Problem 1033.
Degrees are ordinary vertex degrees, edges are unordered pairs of distinct
vertices, and isolated vertices are permitted.

The following are the source paths identified by the commission and the
preserved extracts actually read. The extracts, not other text at the source
paths, define this examination. The [subject manifest](../../assets/review_subject/manifest.json)
records their mapping and freeze time. Every omission is marked `[cut]`.

| Source identified by the commission | Assessed snapshot and depth |
| --- | --- |
| `wiki/research/graph_ramsey_interfaces/butterfly_degree_sum_certificate/_index.md` | [Argument](../../assets/review_subject/argument.md.txt), entire extract: assertion, Exact parameters and realization, Every sufficiently large order, Scope and evidence. |
| `wiki/problems/extremal_graph_theory/E1033/_index.md` | [Catalog question](../../assets/review_subject/catalog_question.md.txt), entire extract: Statement and the supplied minimum convention from Formulation. |
| `wiki/research/graph_ramsey_interfaces/butterfly_degree_sum_certificate/evidence/_index.md` | [Evidence description](../../assets/review_subject/evidence_description.md.txt), entire extract. |
| `wiki/research/graph_ramsey_interfaces/butterfly_degree_sum_certificate/evidence/main.py` | [Frozen checker](../../assets/review_subject/evidence/main.py), complete code. |
| `wiki/research/graph_ramsey_interfaces/butterfly_degree_sum_certificate/evidence/assets/parameters.json` | [Parameters](../../assets/review_subject/evidence/assets/parameters.json), complete input. |

Independent derivations are retained below. The computational keepers are
[integer_recount.py](integer_recount.py), which derives integer cardinality
coefficients before normalizing, and
[adversarial_controls.py](adversarial_controls.py), with the exact
[control inputs](assets/controls.json). Their commands and limits appear under
Computation and reproduction.

The examiner did not author, collaborate on, or previously build on the
certificate. The review began in a fresh context with the commission and
operating instructions. Prior exposure within this examination consisted only
of its own reading of the same frozen extracts and its own continuation.
There was no earlier-cycle report. The configuration specified blind and sealed
operation with synchronization disabled. Subscription checks after startup,
before mathematical reading, and at the examination boundaries returned empty
tables. These facts support isolation; an empty table alone does not establish
what was read.

The allowed mathematical reading was exactly the manifest and the five
extracts above, all read completely. Their listed byte identities were checked
before mathematical reading and on recovery; the frozen inputs remained
unchanged. No canonical mathematical page, source archive, author working
material, prior verdict, ledger, message inbox, feed, or web source was opened.
No excluded communication or search exposure occurred. There was no
mathematical steering, encouragement or preferred verdict from an author or
collaborator.

Operating reading comprised the supplied root `AGENTS.md` instructions;
`README.md`; `docs/anatomy.md` through Claims, Research, Evidence and Tiers,
and its Project claims and Research provisions; the complete
`docs/verification.md` and `campaign/guides/verification.md` contracts;
`campaign/AGENTS.md`; the Reading section of `campaign/guides/research.md`;
and `docs/evidence.md`, `docs/math_authoring.md` and `docs/weaving.md`.
The rendered commission, step instructions, effective settings, operating
skills and scripts were inspected within the commissioned scope. Of the
permitted runtime package, only `tools/__init__.py` and
`tools/core/harness.py` were source-inspected. The enumerated import closure
and operating files were checked against the commissioned identities;
runtime imports were infrastructure, not additional mathematical reading.
Native agent configuration was excluded and was not opened. Private isolation
records retain the operational details; they are not mathematical premises.

## Restatement

For every integer $n\ge n_0=10^{13}$, the frozen construction must produce
some $G$ with

$$
|V(G)|=n,\qquad e(G)>\frac{n^2}{4},\qquad
\max_{uvw\text{ a triangle in }G}
\bigl(d_G(u)+d_G(v)+d_G(w)\bigr)<\frac{183}{125}n.
$$

The catalog asks to estimate $h(n)$ and, in particular, asks whether
$h(n)\ge (2(\sqrt3-1)-o(1))n$. Its supplied convention makes $h(n)$ the
minimum, over all graphs in this edge-density class, of their maximum
triangle degree sum. The certificate must therefore imply the strict upper
bound $h(n)<183n/125$ for every $n\ge n_0$, and must contradict the displayed
asymptotic lower bound. It need not determine the optimum of $h(n)$ or finish
the broader estimation problem.

## Weakest steps

### 1. Finite realization, exact counts and actual triangles

Write $M=10000$, $(w_A,w_B,w_C,w_D,w_E)=(4273,2471,709,1274,1273)$,
$q=4352$ and $r=3011$. All these are positive integers,
$\sum_i w_i=M$, and $q,r<M$. For any integer $s\ge1$, take disjoint tagged
sets

$$
V_i=\{i\}\times\{1,\ldots,w_i\}
\times\mathbb Z/M\mathbb Z\times\{1,\ldots,s\}.
$$

Thus $|V_i|=w_iMs$ and the total order is $N=M^2s$. This supplies
integrality and distinctness of the vertices directly. It is a finite set
construction, not a limit object or an assertion that prescribed fractional
degrees must be realizable.

For a cross-part edge, its part names specify which residue is subtracted
from which. An $AC$ edge is the unordered pair of its endpoints satisfying
$z_C-z_A\in\{0,\ldots,q-1\}$ modulo $M$. It is not required to satisfy a
second condition with $A$ and $C$ interchanged. Each unordered cross-part
pair has exactly one such test. Distinct part pairs are disjoint edge
classes, and no within-part edges are added. Consequently the graph has no
loops or multiple edges and is undirected.

Fix an $A$ vertex. The map $u\mapsto z_A+u$ is injective on
$\{0,\ldots,q-1\}$ modulo $M$, since $q\le M$. Each selected residue class
of $C$ contains $w_Cs$ vertices, giving $qw_Cs$ neighbors. Conversely, for a
fixed $C$ vertex the allowed $A$ residues are $z_C-u$ for those same $q$
distinct values of $u$; there are $qw_As$ neighbors. The reversed orientation
therefore has the asserted count without an assumption that the two residue
sets coincide. The identical translation argument with $r$ gives $rw_Es$
neighbors from $D$ into $E$ and $rw_Ds$ in the reverse direction.

The phrase about equal degrees on each side of $DE$ consequently means
constant degrees within each side. Raw degrees into the opposite part are
different when $w_D\ne w_E$. The formulas in the frozen argument have this
correct meaning.

Count degrees in integer units $d(v)=sD_i$ for $v\in V_i$:

| Part | Integer expression for $D_i$ | Value |
| --- | --- | ---: |
| $A$ | $M(w_B+w_D+w_E)+qw_C$ | 53265568 |
| $B$ | $M(w_A+w_C)$ | 49820000 |
| $C$ | $Mw_B+qw_A$ | 43306096 |
| $D$ | $Mw_A+rw_E$ | 46563003 |
| $E$ | $Mw_A+rw_D$ | 46566014 |

For a supported pair with density numerator $p$, count from its first part:
$w_iMs$ vertices each have $pw_js$ neighbors. Its number of edges is
$M s^2 p w_iw_j$, with each edge counted once. The six contributions to
$S=e(G)/(Ms^2)$ are

| Pair | Contribution to $S$ |
| --- | ---: |
| $AB$ | 105585830000 |
| $BC$ | 17519390000 |
| $AD$ | 54438020000 |
| $AE$ | 54395290000 |
| $AC$ | 13184632064 |
| $DE$ | 4883245822 |

They sum to $S=250006407886$. Since $N^2=M^4s^2$, this gives

$$
\frac{e(G)}{N^2}=\frac{S}{M^3}
=\frac14+\frac{3203943}{500000000000}.
$$

There is no factor-of-two ambiguity: the edge count used one orientation of
each supported part pair, whereas summing vertex degrees would count every
edge twice. The integer recount derives the edge count without using that
degree sum.

Independence of the parts forces every triangle to use three distinct parts.
The ten possible triples have the following exact support test:

| Triple | Required pair missing, or supported |
| --- | --- |
| $ABC$ | Supported. |
| $ABD$ | $BD$ missing. |
| $ABE$ | $BE$ missing. |
| $ACD$ | $CD$ missing. |
| $ACE$ | $CE$ missing. |
| $ADE$ | Supported. |
| $BCD$ | $BD$ and $CD$ missing. |
| $BCE$ | $BE$ and $CE$ missing. |
| $BDE$ | $BD$ and $BE$ missing. |
| $CDE$ | $CD$ and $CE$ missing. |

This lists support triples, not all triples of vertices in those parts. An
actual $ABC$ triangle consists of an $AC$ edge and any vertex of $B$;
an actual $ADE$ triangle consists of a $DE$ edge and any vertex of $A$.
Their numbers are respectively

$$
M^2s^3q w_Aw_Bw_C
\quad\hbox{and}\quad
M^2s^3r w_Aw_Dw_E.
$$

Both are positive. In particular, vertices with $j=t=1$ and residue zero
in each of the three indicated parts give explicit examples of both types.
There are no further triangles, and residue correlations cannot create a
missing support edge.

The degree sum is constant on each actual triangle type. Dividing by $N$,
the two values are

$$
T_1=\frac{146391664}{10^8}=\frac{9149479}{6250000},
\qquad
T_2=\frac{146394585}{10^8}=\frac{29278917}{20000000}.
$$

Thus $T_2>T_1$ and the maximum over actual triangles of this graph is $T_2N$.
The strict margins in the claim's normalized units are

$$
\frac{183}{125}-T_1=\frac{521}{6250000}>0,
\qquad
\frac{183}{125}-T_2=\frac{1083}{20000000}>0.
$$

These calculations verify the frozen degree and edge formulas and the
triangle assertion for every integer $s\ge1$.

### 2. Rounding, isolated vertices and a uniform cutoff

Put $U=M^2=10^8$. For an arbitrary integer $n\ge n_0$, integer division
gives $n=sU+t$ with $0\le t<U$ and $s\ge100000$. Hence $N=sU$ is an
admissible construction order, $N\le n$, and $N>n-U$. Adding exactly $t$
isolated vertices produces order $n$ without changing any edge, old degree,
or old triangle, and creates no new triangle.

The danger is loss of density when the denominator changes from $N^2$ to
$n^2$. This loss is bounded for every remainder, including $t=U-1$.
Because $n\ge n_0>U$, both $N/n$ and $1-U/n$ are positive, so squaring
preserves the strict inequality. Also $U/n\le U/n_0=10^{-5}$. With
$\rho=S/M^3$,

$$
\frac{e(G)}{n^2}
=\rho\left(\frac Nn\right)^2
>\rho\left(1-\frac Un\right)^2
\ge\rho(1-10^{-5})^2.
$$

The exact excess of this last lower bound over $1/4$ is

$$
\rho(1-10^{-5})^2-\frac14
=\frac{56311313716831544}{4\cdot10^{22}}>0.
$$

Equivalently, before canceling the cutoff units, the integer test is
$4S(n_0-U)^2-M^3n_0^2>0$. Its value is
$563113137168315440000000000000000$, as independently recounted.
The passage from the cutoff to larger integers is the displayed order
comparison, not an extrapolation from sampled orders. At a multiple of $U$
the strict relation $N>n-U$ still holds; no endpoint is lost.

Every surviving triangle has degree sum at most $T_2N$, and

$$
T_2N<\frac{183}{125}N\le\frac{183}{125}n.
$$

Thus both strict requirements survive padding at every integer in the
commissioned range. All constants are fixed independently of $n$.

### 3. The minimum convention and the asymptotic negation

The supplied minimum is meaningful in the relevant range. There are finitely
many labeled simple graphs on $n$ vertices, and the complete graph belongs
to the density class for $n>2$. To check that each eligible graph has a
triangle without importing an external theorem, suppose it were
triangle-free. For an edge $uv$, the neighbor sets of $u$ and $v$ are
disjoint, so $d(u)+d(v)\le n$. Summing over edges yields
$\sum_vd(v)^2\le ne$. The elementary inequality
$(\sum_vd(v))^2\le n\sum_vd(v)^2$, obtained by summing squared degree
differences, and $\sum_vd(v)=2e$ give $4e^2\le n^2e$. When $e>0$ this
implies $e\le n^2/4$, a contradiction. Each maximum is therefore over a
nonempty finite set, and the minimum is attained over a nonempty finite
class. A threshold works for every eligible graph exactly when it is no
larger than each graph's maximum triangle degree sum, so this minimum is
precisely the largest universally guaranteed value in the catalog convention.

This is routine reconstruction of the catalog definition's domain, not a
new construction replacing the frozen proof. Likewise, the explicit tagged
sets, reverse-residue bijection, monotonicity and epsilon argument here
expand elementary inferences of the supplied argument. No alternative
proof was substituted for a defective essential step.

Our graph belongs to exactly the class minimized over. Therefore
$h(n)$ is no larger than its maximum triangle degree sum, and
$h(n)<183n/125$ for every $n\ge n_0$. This is an upper estimate for $h(n)$;
no assertion of its optimum follows.

For the irrational comparison, $433/125>0$ and $2\sqrt3>0$, and

$$
433^2=187489<187500=12\cdot125^2.
$$

Taking positive square roots and subtracting $2$ gives
$b=183/125<c=2(\sqrt3-1)$. Let $\delta=c-b>0$. If an asymptotic lower
bound of the proposed form held, there would be a real function
$\varepsilon(n)\to0$ and an order beyond which
$h(n)/n\ge c-\varepsilon(n)$. For sufficiently large $n$ also
$|\varepsilon(n)|<\delta/2$, giving
$h(n)/n>c-\delta/2>b$, contrary to the constructed upper bound. Oscillation
or a change of sign of $\varepsilon$ does not avoid this contradiction.
Equivalently, the eventual upper bound implies
$\limsup h(n)/n\le b<c$, incompatible with the proposed lower limit.

The explicit proposed inequality in the supplied catalog statement is
therefore negated. The broader instruction to estimate $h(n)$ receives this
upper estimate; the certificate does not settle the optimum or provide a
complete asymptotic evaluation.

## Strongest attack

The strongest attempted refutation was to break the passage from fractional
parameters to an undirected simple graph with the claimed degrees. The
arithmetic checker does not supply that passage. In particular, a mistaken
requirement to apply the same residue interval in both orientations would
give different neighborhoods and destroy the density calculation. For $AC$,
$z_A=9999$ and $z_C=0$ give the allowed difference $1$, while the reversed
difference is $9999$, outside the interval. The frozen construction uses
part labels to select one orientation, so that pair is one undirected edge;
it is not subjected to both tests. The reverse neighborhood is a translate
of the negated interval, still containing exactly $4352$ residues. The
explicit finite sets and both bijections above defeat this attack for all
$s$, rather than for finitely many example graphs.

The next attack targeted remainders just below a construction order and a
possible unjustified monotonicity step. The strict bound $N>n-U$, positivity
before squaring, and the exact positive cutoff margin cover every remainder
and every larger $n$. The separate minimum and epsilon arguments defeat
convention drift and a weakened reading of the asymptotic consequence.

An adversarial input attack did succeed against a stronger interpretation of
the checker: its successful exit does not validate all construction-domain
assumptions for arbitrary JSON. Negating $M$ and every part and density
numerator leaves every rational weight and density unchanged, and also
leaves $M^2$ unchanged. The frozen checker accepts that input, although its
negative integer parameters do not specify the finite sets in the proof.
The retained `sign_reversed_domain` control demonstrates this in ordinary
and optimized Python. The supplied input has positive integer parameters,
verified directly and by the integer recount, so this is a coverage
limitation of the arithmetic checker, not a counterexample to the frozen
assertion or an essential gap in its analytic proof.

## Computation and reproduction

The complete frozen checker was executed against its exact supplied input
using the commissioned byte-identical mirror and relative asset layout. The
actual invocation and exit record remain in private execution records. This
was a **mirror replay, not execution at the canonical source path**. It exited
zero, with the exact edge surplus and both triangle sums reproduced. No
prior output, cached success, or stated check count was used as a substitute
for execution. The canonical-path command in the evidence description was
not tested here; adoption of that source requires its own canonical replay.

The code uses `Fraction`, exhausts the ten triples of five part labels,
compares the displayed exact values, and checks the strict rational
inequalities. `Checker.finish()` returns one after a failed check and zero
only after a nonempty successful run, and the program passes that return
value to `sys.exit`. Neither it nor the independent keepers use bare
assertions for mathematical checks. Ordinary and `python -O` controls
confirmed that reported failures produce nonzero exits.

There are two material limits to the frozen checker. First, its handshaking
equality is forced by the shared accumulation: each pair contributes
$p w_iw_j$ to the edge density and twice that amount to the weighted degree
sum. There is no well-formed parameter input that makes this diagnostic
fail while those updates remain as written. It has no independent evidentiary
weight. The finite graph argument establishes the actual degree and edge
counts without relying on that diagnostic. Second, the code is a checker of
the fixed rational certificate, not a complete validator of positive integer
construction parameters, unique pair encodings, or arbitrary JSON schemas.
The sign-reversal witness exposes this distinction exactly.

The independent integer recount uses explicit per-part residue-class counts
and six unordered-edge counts, then clears denominators. It does not update
normalized degrees and edge density together as the frozen checker does.
An error in converting actual vertex cardinalities to normalized quantities
or in the factor of two in edge counting is therefore addressed at a
different interface. Agreement of the arithmetic alone would still not prove
the realization or all-order transfer; those have the independent written
arguments above. No giant graph was enumerated, and no finite residue model
is being used as a universal proof.

The full exact controls are in `assets/controls.json`. Each mutation below
is relative to the supplied input; it is diagnostic evidence, not a new
mathematical subject. Observed exit behavior was the same with and without
`-O`:

| Input | Frozen checker exit | Integer recount exit | Purpose |
| --- | ---: | ---: | --- |
| Supplied parameters | 0 | 0 | Replay and independent recount. |
| $w_A=4274$ | 1 | 1 | Detect incorrect total part size. |
| $q=10001$ | 1 | 1 | Detect a density outside the residue range. |
| Add supported pair $BD$ with numerator $1$ | 1 | 1 | Detect altered support. |
| $q=4351$ | 1 | 1 | Detect an off-by-one residue count in the displayed identities. |
| Comparison bound $14639/10000$ | 1 | 1 | Detect a failed strict triangle margin. |
| Comparison bound $3/2$ | 1 | 1 | Detect a failed irrational comparison. |
| Cutoff $10^{12}$ | 1 | 1 | Detect failure of the sufficient padding inequality. |
| Cutoff $10^8$ | 1 | 1 | Detect the missing positivity domain for padding. |
| Negate denominator and all part and pair numerators | 0 | 1 | Exhibit the frozen checker's unvalidated construction domain. |

The control driver requires both the expected return code and the named
failed obligation for each rejection. An unrelated crash cannot substitute
for a meaningful failing test. For example, if the frozen program returned
zero on the too-small triangle bound, or the recount accepted the negative
denominator, the driver itself would exit nonzero. These controls demonstrate
failure signaling and particular coverage boundaries; they do not exhaust
all possible malformed inputs. The lower-cutoff rejection is not asserted
to disprove a graph-existence statement at that different cutoff.

The control driver also has a retained failing input of its own:
[wrong_expectation.json](assets/wrong_expectation.json) incorrectly expects
the frozen checker to reject the supplied valid parameters. The driver
exited one on this specification, both in ordinary and optimized Python.
This tests its rejection path without changing either checker or treating
a successful arithmetic run as a failed mathematical certificate.

From an ordinary clone containing the filed package, run the following at
the repository root. The first command executes the assessed checker
snapshot, preserving its exact relative input layout. The remaining commands
run the independent keepers. The scripts read their retained inputs by path;
the control driver writes only to the explicitly selected disposable scratch
directory and starts fresh computations for every case.

```sh
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH="$PWD"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
export VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1
certificate_dir=wiki/research/graph_ramsey_interfaces/butterfly_degree_sum_certificate
review_dir="$certificate_dir/evidence/verify/whole_conclusion"
nice -n10 uv run --no-sync python \
  "$certificate_dir/evidence/assets/review_subject/evidence/main.py"
nice -n10 uv run --no-sync python "$review_dir/integer_recount.py"
nice -n10 uv run --no-sync python "$review_dir/adversarial_controls.py" \
  --scratch tmp/e1033_whole_conclusion_controls
```

The deliberately false specification is rerun separately below. Each command
is expected to exit **one**, with the incorrect expected rejection identified:

```sh
nice -n10 uv run --no-sync python "$review_dir/adversarial_controls.py" \
  --controls "$review_dir/assets/wrong_expectation.json" \
  --scratch tmp/e1033_whole_conclusion_wrong_expectation
nice -n10 uv run --no-sync python -O "$review_dir/adversarial_controls.py" \
  --controls "$review_dir/assets/wrong_expectation.json" \
  --scratch tmp/e1033_whole_conclusion_wrong_expectation_optimized
```

These require the repository's existing local Python environment and its
`tools` package, specified by `pyproject.toml` and `uv.lock`. No network,
optimization search, generated witness, array library, or external source is
needed. The individual arithmetic runs took less than a second in the
examined environment; the sequential controls took a few seconds. Runtime
observations are not part of the mathematical warrant. The private mirror
and retained snapshot were compared byte-for-byte with the supplied code
and input; the commands above express the clone-relative reproduction route,
not a claim that these public destinations had already been adopted.

## Checklist

The following covers every item of the Erdos-specific checklist.

| Item | Finding |
| --- | --- |
| Quantifiers and scope | No defect found. Integer division covers every $n\ge10^{13}$, with no exceptional residue. The limit consequence is checked separately. |
| Circularity | No defect found. Neither the target construction nor its asymptotic consequence is assumed. There is no induction requiring an unproved termination property. |
| Model and convention changes | No defect found in the proof. Tagged finite sets and residue bijections realize the fractional expressions. The checker alone does not establish this transfer. |
| Finite and statistical overreach | No defect found. The support enumeration is exhaustive for its fixed five-label domain. Uniformity in $s$ and $n$ is proved algebraically; no statistical inference is used. |
| Uniformity | No defect found. $M$, weights, residue counts, margin and cutoff are independent of $n$. Positivity and monotonicity justify the cutoff comparison on the entire claimed range. |
| Extremal conclusions | No defect found. The maximum for the constructed graph is computed in degree-sum-per-order units, and the catalog minimum is well-defined. Only an upper estimate for that minimum is deduced. |
| Consequences and composition | No defect found. Realization, strict surplus, padding, triangle bounds, minimum convention and asymptotic contradiction are each supplied at the strength used. |
| Computation | Fixed-input arithmetic reproduced exactly. The shared-accumulation diagnostic and arbitrary-input domain limitation are disclosed and receive no additional warrant. Retained controls give genuine failures, including under optimization. |
| Reproduction | Required mapped mirror replay and independent keepers were freshly executed from retained inputs. Canonical source-path execution was not performed and is not claimed. |
| Source and verdict fidelity | The conclusion is matched to the supplied catalog text, including its broader estimate request. No current external catalog state or excluded review characterization is asserted. Verdict words are written in full. |

The neutral canonical modes are also explicit:

| Canonical mode | Finding |
| --- | --- |
| Almost all upgraded to all | Not present: the floor/remainder argument is universal over the stated integers. |
| Induction presupposing termination | Inapplicable: no induction or unbounded search is used; the displayed finite product sets define the graph. |
| Probabilistic or averaging heuristics as proof | Not present: all counts and inequalities are deterministic and exact. The squared-degree inequality used for the definition is an algebraic inequality, not a heuristic average. |
| Circular use of an equivalent target | Not present: the construction is explicit, and the lower bound is contradicted only after verifying its hypotheses. |
| Exceptional sets dropped from density arguments | Not present: all remainders $0\le t<U$ and all added isolated vertices are accounted for. |
| Finite verification beyond base-case coverage | Not present: infinite coverage rests on residue translation and monotonicity, not the executed arithmetic or controls alone. |
| Relaxed or averaged objects substituted for actual objects | Not present in the proof: the two-sided integer degree counts are realized by simple graphs. The checker-domain control prevents assigning this coverage to arithmetic replay. |

Every named pattern in the neutral checklist has the following disposition:

| Named pattern | Finding |
| --- | --- |
| Model-class transport instead of entailment | The axiom-system classification issue is inapplicable: no logical-system extension is claimed. The relevant concrete-model transfer is proved under Weakest steps 1. |
| Uniformity over an infinite family from finite instances | Not present: fixed constants and exact arguments cover all $s\ge1$ and all $n\ge n_0$. |
| Extremal claims in their own units | Checked using $T_i=(\sum D_i)/M^2$ and the catalog minimum of actual triangle degree sums. No optimum or sharpness is claimed. |
| Consequence sentences as claim surfaces | Checked independently: the strict density after padding, the bound on $h(n)$, the irrational comparison, and the negation of the asymptotic assertion all follow. The broader estimate request is not declared completely resolved. |
| Carry hypotheses used by a quantified argument | All used hypotheses are retained: positive integer part data and modulus, residue ranges, integer $s\ge1$, $n\ge n_0>U$, simplicity and permission for isolates. |
| Composition inherits unproved premises | No missing established premise was found. The elementary reconstructions are stated, and no unprovided native or external theorem is silently consumed. |
| Reproducibility notes are claims | The exact mapped replay was run and its coverage inspected. The public source-path command remains outside this execution claim. The stated runtime scale is consistent with the observed runs. |
| Verifier quotations are claims | Inapplicable to the admitted mathematical subject: standing and earlier review text were excluded, and no earlier verifier ruling is quoted or relied on. Their fidelity is not certified here. |
| Verdict words spelled in full | The verdict is refutation-failed, never an ambiguous abbreviation. |
| Certified-bracket functions fail loudly | Inapplicable: there are no numerical enclosures, periodic windows or iteration-capped approximation routines. Computation uses exact integers and rationals. |
| A leg with no failing input is decoration | The frozen handshaking diagnostic is redundant and receives no independent weight. The actual graph counts are derived directly. Both retained keeper legs have concrete failing controls; the control driver also checks the failure labels. |
| A gate reading caches instead of rerunning is defective | Not present in the warrant: the checker and keepers rerun their calculations. Logs are disposable records, never inputs to acceptance tests. No repository-wide gate is claimed as mathematical evidence. |

The neighboring statistical-discipline requirement is inapplicable because
there are no samples or probabilistic conclusions. Proof and executable
coverage are matched explicitly above. Source fidelity is limited to the
prepared supplied text; no literature proof or present-day catalog source
was inspected beyond it.

## Premises

The dependency finding was made from the complete frozen assertion, argument,
scope and consequence sentences, code and input, and rechecked at verdict
filing on 2026-10-15 UTC. No native L-claim and no source-owned external
theorem is consumed as an established premise. There is therefore no
dependency tier, stale mark, pending grade or batch acceptance order to
report. No ledger was read; an empty inventory was established from the
mathematics rather than inferred from an author's list.

The catalog extract supplies the target and its definition, not a premise
theorem. Its meaningfulness in this range is established above. Elementary
finite-set counting, modular translations, integer division, ordered-field
inequalities and the positive real square root are the foundations used.
The support, integer parameters and exact input values are displayed and
checked. Runtime package code supplies execution and failure signaling, not
an additional mathematical premise. There is no assumed conditional lemma,
unread source-proof interface or omitted essential construction lemma on
which the verdict depends.

## Verdict and grading

**refutation-failed** for the whole frozen certificate: its finite simple
graph realization, exact counts and strict margins, existence for every
integer $n\ge10^{13}$ after padding, and negation of the displayed
asymptotic lower bound under the supplied minimum convention all survive the
commissioned attacks.

This conclusion includes the checker limitations described above. Successful
arithmetic replay alone would not warrant it. It covers only the preserved
mathematical text and exact code/input, not omitted text, later repairs or
future changes. It does not determine the optimum of $h(n)$, establish
stronger constants, assess novelty, verify unrelated source proofs, or supply
Lean acceptance. No giant graph enumeration, optimization campaign, current
source search or repository-wide gate was performed. The broad estimate
request is distinguished from the definite proposed inequality throughout.

This is the examiner's mathematical verdict, not a grade or a tier assertion.
A grader distinct from both author and examiner must assess the complete
contract and independence record. Delivery itself changes no public standing.

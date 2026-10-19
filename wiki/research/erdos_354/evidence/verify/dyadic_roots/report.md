---
name: research/erdos_354/evidence/verify/dyadic_roots/report
title: "Dyadic-root completeness: whole-conclusion examination"
desc: |
  Adversarial examination of the dyadic-root single-ray theorem, arbitrary
  finite deletions, and the existential-base consequence for E0354(ii), using
  the accepted indexed dyadic theorem. Records the exact source boundary and
  an exposure requiring a distinct grader's materiality ruling.
created: 2026-10-15T02:28:16Z
updated: 2026-10-15T02:28:16Z
---

***

## Subject and independence

**Examination date:** 2026-10-14 UTC. **Reviewer:** mathematical reviewer,
GPT-6-astra, commissioned to refute the entire conclusion. The reviewer neither
authored nor helped construct the frozen argument and had no exposure to it
before this examination. Project examination work is attributed to Plasma AI.
The source-record exposure described under **Premises** requires a distinct
grader's materiality ruling; this report makes no ruling about its own
eligibility or contract acceptance.

**Frozen subject:** the extraction frozen at
2026-10-14T17:08:39.381721Z. The full proof subject is the D1 mathematical
subsection preserved in
`wiki/research/erdos_354/evidence/assets/dyadic_root_subject/argument.md`,
including its imported premise and consequence sentence. The original catalog
statement and formulation come from
`wiki/problems/additive_bases/E0354/_index.md`. The examination covers every
integer $m\ge2$, every real $t>0$, every prescribed first index, every finite
deletion, distinct-value completeness, and the exact existential-base
consequence. It does not examine the universal-base question, a full E0349
classification, historical novelty, or another candidate proof.

All five preserved files below were read in full. Their unchanged extraction
bytes, including the uniform `[cut]` markers, are part of this record. The
[public manifest](../../assets/dyadic_root_subject/manifest.json) records the
freeze date and source mapping. The argument snapshot itself is the assigned
public proof subject: it preserves the complete mathematical D1 subsection,
without the surrounding account. No inference is drawn from omitted text.

| Preserved extraction | Original public path and reading scope |
| --- | --- |
| [target.md](../../assets/dyadic_root_subject/target.md) | `wiki/problems/additive_bases/E0354/_index.md`, Statement and Formulation only. |
| [argument.md](../../assets/dyadic_root_subject/argument.md) | `wiki/research/erdos_354/evidence/assets/dyadic_root_subject/argument.md`, complete D1 extraction; premise at lines 3–12, deduction at lines 16–42, consequence at lines 44–47. |
| [premise_statement.md](../../assets/dyadic_root_subject/premise_statement.md) | `library/additive_bases/jenw1n_2026_erdos_354_part_i_lean_proof/target.md`, exact indexed theorem and supplied definition/fidelity interface. |
| [premise_warrant.md](../../assets/dyadic_root_subject/premise_warrant.md) | `wiki/problems/additive_bases/E0354/claims/2026_09_11_jenw1n.md`, four metadata fields and the first Acceptance paragraph. |
| [premise_replay.md](../../assets/dyadic_root_subject/premise_replay.md) | `library/number_theory/conjectures_io_2026_lean_solutions_erdos_problems/evidence/verify/receipt_e0354_815c1d5f.md`, supplied replay receipt body. |

The mathematical read set was these files and their manifest, followed by the
two narrowly authorized current dependency paths listed under **Premises**.
The known over-read at the latter boundary is disclosed there. Operating reads
were the commissioned repository guidance: `README.md`; the Claims, Evidence,
Tiers, Naming and Project claims portions of `docs/anatomy.md` and its
introductory conventions; `docs/verification.md`; `docs/evidence.md`;
`docs/approach_vetting.md`; `docs/math_authoring.md`; `docs/weaving.md`;
`campaign/AGENTS.md`; `campaign/guides/verification.md`; and the Reading
section of `campaign/guides/research.md`, with the supplied operating context.
Their examples and links did not enlarge the mathematical read set.

An empty subscription table was checked before mathematical reading. No incoming
inter-node messages, web results, author plans, sibling reports, or earlier
examinations of this deduction were read. No source URL was opened. The subject
remained fixed; it was not repaired or replaced. The independent reasoning and
exact attack examples are retained below. There is no mathematical code or
numerical sampling leg. The external proof was neither read in full nor replayed
here.

## Restatement

Write $\mathbb N_0=\{0,1,2,\ldots\}$. For an integer $m\ge2$, put
$\gamma_m=2^{1/m}$, the positive real root, and
$a_n=\lfloor t\gamma_m^n\rfloor$ for $n\in\mathbb N_0$ and $t>0$.
The single-ray assertion, including its strengthening, is:

$$
\begin{gathered}
\forall m\in\mathbb Z_{\ge2}\ \forall t>0\ \forall L\in\mathbb Z\quad
\forall F\subset\mathbb Z\text{ finite},\quad
\exists H\in\mathbb N_0\ \forall N\in\mathbb Z,\ N\ge H,\\
\exists V\subset
\bigl(\{a_n:n\in\mathbb N_0,\ n\ge L\}\setminus F\bigr)
\text{ finite},\qquad N=\sum_{v\in V}v.
\end{gathered}
$$

Thus each integer value is used at most once. Allowing an integer lower bound
$L<0$ merely leaves the nonnegative-index sequence unrestricted. In particular,
the assertion covers either starting-index convention $0$ or $1$ and every
later tail. Only integer deleted values matter; other deleted objects cannot
equal a sequence value. A finite deletion of indexed occurrences is also
allowed, by taking a tail beyond their indices. The proof below handles that
deletion simultaneously with $F$.

The threshold may depend on $t,m,L,F$. In the frozen proof, $L$ and $F$
influence the preliminary choice $j$, and the imported theorem then supplies
$H(t,m,j)$. Completeness is eventual; there is no assertion about every small
integer or a numerical uniform threshold.

The consequence under examination has the quantifier order

$$
\exists\gamma\in(1,2)\ \forall\alpha,\beta>0,\quad
\alpha/\beta\notin\mathbb Q\ \Longrightarrow\quad
I_{\alpha,\beta,\gamma}\text{ is eventually complete},
$$

where
$I_{\alpha,\beta,\gamma}(2n)=\lfloor\alpha\gamma^n\rfloor$ and
$I_{\alpha,\beta,\gamma}(2n+1)=\lfloor\beta\gamma^n\rfloor$.
Here completeness uses finite sets of positions in $I$. The frozen argument
actually claims this conclusion at the single fixed base $\sqrt2$ for all
positive $\alpha,\beta$, without the ratio restriction. This is distinct from
a statement for every real base in $(1,2)$. The catalog wording in the target
snapshot does not decide between those formulations.

## Weakest steps

### 1. A valid shift exists for all parameters

The root and floor arguments must hold for every $m$, including composite $m$,
and for arbitrarily small $t$. If $\gamma_m=p/q$ with coprime positive
integers $p,q$, then $p^m=2q^m$. Consequently $q^m$ divides $p^m$, so
$q=1$. But a positive integer has $m$th power either $1$ or at least $4$
when $m\ge2$, never $2$. Hence $\gamma_m$ is irrational. From
$\gamma_m^m=2$ and monotonicity of the $m$th power on positive reals,
$1<\gamma_m<2$.

Let $\gamma=\gamma_m$, $\delta=\gamma-1>0$, and
$M=\max(F\cup\{0\})$. Choose a nonnegative integer $j\ge L$ so large
that

$$
t\gamma^j>\max\{M+1,\delta^{-1}\}.
$$

Such a $j$ exists: $\gamma^j=(1+\delta)^j\ge1+j\delta$ for
nonnegative integers $j$, which is unbounded. One can require $j\ge1$ as
well when using the starting-index convention $1$. For every $n\ge j$,

$$
t\gamma^{n+1}-t\gamma^n=t\gamma^n\delta>1,
\qquad a_{n+1}\ge a_n+1,
\qquad a_j\ge M+1.
$$

The floor inequality follows from
$t\gamma^{n+1}>t\gamma^n+1$ and
$\lfloor x+1\rfloor=\lfloor x\rfloor+1$. It follows that all the
values $a_n$ with $n\ge j$ are positive, avoid $F$, and are pairwise
distinct. No estimate is asserted uniformly as $m$ grows or $t$ varies.

Set $u=t\gamma^j$ and $v=t\gamma^{j+1}$. Both are positive, and
$u/v=1/\gamma$ is irrational: a rational nonzero reciprocal would make
$\gamma$ rational. These are precisely the hypotheses of the imported
indexed theorem. In particular, the arbitrary coefficient $t$ introduces no
exceptional arithmetic class.

This expands the frozen choice of $j$ and its elementary floor and root
inferences. The explicit sufficient inequality for $j$ is a reconstruction of
the stated “large enough” choice, not a different proof route or an added
theorem premise.

### 2. The indexed representations really use distinct surviving values

Apply the imported theorem to these fixed $u,v$. It supplies an integer
threshold $K$ such that every integer $N\ge K$ has finite sets
$R,S\subset\mathbb N_0$ with

$$
N=\sum_{r\in R}\lfloor u2^r\rfloor+
  \sum_{s\in S}\lfloor v2^s\rfloor.
$$

The theorem allows $R$ and $S$ to overlap. That causes no problem after the
transport. The equalities $\gamma^m=2$ give, exactly,

$$
\lfloor u2^r\rfloor=a_{j+mr},\qquad
\lfloor v2^s\rfloor=a_{j+1+ms}.
$$

Each index map is injective. If their images intersected, then
$j+mr=j+1+ms$, so $m(r-s)=1$, impossible for an integer $m\ge2$.
Thus the finite union

$$
B=\{j+mr:r\in R\}\cup\{j+1+ms:s\in S\}
$$

contains each transported index exactly once, with every index at least $j$.
The equality of sums is therefore

$$
N=\sum_{n\in B}a_n=\sum_{v\in\{a_n:n\in B\}}v.
$$

The second equality uses the injectivity of $n\mapsto a_n$ on the chosen
tail, proved in step 1. Without it, the equality of a sum over indices and a
sum over values could fail. All these values lie outside $F$.

Taking $H=\max\{0,K\}$ proves the restated conclusion. The order of
choices is $m,t,L,F$, then $j$, then $u,v,K$, then the representations for
all $N\ge H$. The chosen tail is independent of $N$; this is not a
separate tail chosen for each desired sum.

For a finite set $D\subset\mathbb N_0$ of deleted occurrences, increase the
prescribed lower bound to
$\max\{L,1+\max(D\cup\{-1\})\}$. Every selected index then avoids
$D$ as well. Deleting finitely many distinct values is already the arbitrary
$F$ case. This supplies the claimed strong completeness under both conventions.
It does not infer strong completeness from ordinary completeness: the source
theorem is applied anew to the coefficients obtained after each deletion and
shift.

The finite-set image and sum equalities, the explicit quantifier order, and
the indexed-deletion specialization reconstruct the frozen argument's stated
transport and “either convention” conclusion. No substantive missing lemma
or replacement argument was found in these steps.

### 3. The existential consequence uses one fixed base

Take $m=2$ once and for all, so $\gamma=\sqrt2\in(1,2)$ is fixed
before $\alpha$ and $\beta$. For any $\alpha>0$, step 2 with
$t=\alpha$ and no deletions supplies representations by distinct values on
the $\alpha$ ray. If $B$ is the corresponding finite set of ray indices,
then $\{2n:n\in B\}$ is a finite set of positions of
$I_{\alpha,\beta,\sqrt2}$ with the same sum. It uses no position from the
$\beta$ ray.

This proves the asserted consequence for every positive $\beta$, irrespective
of $\alpha/\beta$. Values shared by the two rays cannot invalidate a
representation using only the first ray. The same representation also works
if the two rays are viewed as a set of integer values. Changing the first
index to $1$ is covered by the corresponding tail in step 1.

This is the exact inclusion argument behind “Adding the beta ray preserves
completeness.” It preserves the required global existential quantifier. It
does not provide a theorem for an arbitrary real $\gamma\in(1,2)$: the
proof specifically uses an integer $m$ with $\gamma^m=2$.

## Strongest attack and exact failed witnesses

The strongest attack was that an indexed completeness theorem may rely on
equal summands at different positions, making its transfer to distinct integer
values invalid. This risk occurs inside the actual parameter family: at
$m=2,t=1$, the terms at indices $0$ and $1$ are both $1$. Taking
$u=1,v=\sqrt2$ satisfies the source's irrational-ratio hypothesis, but
the representation using both zeroth source terms repeats the value $1$.
Irrationality alone does not prevent the collision.

There is no general implication from indexed completeness to distinct-value
completeness. As an exact auxiliary counterexample to that proposed shortcut,
take two indexed copies of $3^k$ for every $k\ge0$. Finite indexed sums
represent every nonnegative integer by its ternary digits $0,1,2$. Distinct
values give only sums of different powers of $3$ and miss $2\cdot3^k$ for
every $k$: a larger power already exceeds that integer, while

$$
\sum_{i=0}^{k}3^i=\frac{3^{k+1}-1}{2}<2\cdot3^k.
$$

This auxiliary example is a counterexample to the generic shortcut, not to
the commissioned theorem. The frozen argument does not use that shortcut. Its
single shifted tail has pairwise distinct values, and the two transported
residue classes are disjoint. The source theorem is applied only after those
properties have been secured. Thus even a source representation choosing both
ray terms at the same source exponent becomes a sum of distinct original
values. The attack fails for the frozen proof for the exact reasons in steps
1 and 2.

A separate attack targeted the finite-deletion conclusion. Ordinary
completeness does not survive arbitrary finite deletion: the values
$1,2,4,8,\ldots$ represent every nonnegative integer, but removing $1$
leaves only even sums and misses arbitrarily large odd integers. This is also
an exact negative control for dropping $m\ge2$: with $m=1,t=1$, it is
the very single ray under discussion. At that excluded endpoint the proposed
source ratio is rational and the residue classes are not disjoint. For
$m\ge2$, the frozen proof instead changes the coefficients after the
deletion and reapplies the theorem. It never assumes a deletion property of
the source theorem. The negative control therefore does not refute the actual
argument.

Further boundary attacks found no omitted case. The maximum of
$F\cup\{0\}$ exists even when $F$ is empty, includes the zero boundary,
and bounds every deleted integer value. A large $L$ and an arbitrarily large
finite deleted value both affect $j$ before the source application. Very small
$t$ or large $m$ can delay the increasing tail, but cannot prevent it because
$t>0$ and $\gamma-1>0$. Dropping $t>0$ would be fatal: $t=0$ gives only
zero sums. These boundary controls test hypotheses; none enlarges the theorem's
domain.

The uniformity attack is also exact. No threshold can work for all finite
deleted value sets: for any proposed common threshold choose an integer
$K\ge1$ above it and delete $F=\{1,\ldots,K\}$. Every remaining
nonnegative value is zero or exceeds $K$, so $K$ is not representable. The
frozen statement avoids that false uniform strengthening. No claim that a
threshold must depend on each individual parameter separately is needed.

Finally, the consequence was attacked for reversal of $\exists\gamma$ and
$\forall\alpha,\beta$, and for accidentally applying the source theorem
to the pair $(\alpha,\beta)$ at base $\sqrt2$. Step 3 exhibits one fixed
base; step 1 applies the source theorem at base $2$ to
$(t\gamma^j,t\gamma^{j+1})$. Neither quantifier reversal nor wrong-base
application occurs. No counterexample or unsupported essential inference was
found in the commissioned conclusion.

## Premises

### Exact external interface and reading depth

There is one substantive theorem premise, derived from the actual proof and
its consequence rather than from a list of citations:

$$
\forall u,v>0,\ u/v\notin\mathbb Q\ \Longrightarrow\quad
\exists K\in\mathbb Z\ \forall N\in\mathbb Z,\ N\ge K,\quad
N=\sum_{r\in R}\lfloor u2^r\rfloor+
  \sum_{s\in S}\lfloor v2^s\rfloor
$$

for suitable finite $R,S\subset\mathbb N_0$. The finite sets may overlap
and equal integer values in the two indexed rays may count separately. No
strong-completeness, distinct-value, or smaller-base theorem is imported.
The specialization is exactly $u=t\gamma^j$, $v=t\gamma^{j+1}$,
whose hypotheses are checked in step 1.

The source is the accepted external result recorded as the first part of
E0354, with formal target `Erdos354.erdos_354.parts.i` and answer `True`.
The theorem's displayed type `True ↔ P` yields the required proposition $P$
by its forward implication. The supplied definitions identify finite sets of
interleaving positions with the pair of finite exponent sets, by the maps
$r\mapsto2r$ and $s\mapsto2s+1$. They identify “every sufficiently large
integer” with the eventual natural-number formulation without changing any
large positive target.

The source/version locator is Conjectures.io record
`815c1d5f-3afb-4430-8e2c-260d9038f5b0`, with the task, external source
versions, and ports identified in **Task**, **Environment**, and **Port** of
the preserved replay snapshot. The acceptance record reports a repository
rebuild on Lean v4.34.1 and an empty-environment kernel replay. The receipt
records its successful replay on 2026-10-14T01:08:29Z, target and statement
definition agreement, and exactly `propext`, `Classical.choice`, and
`Quot.sound` as target axioms. The site's own certification is not the basis
used here.

Reading depth is **claims checked**: the exact displayed theorem, its supplied
definition interface, the permitted acceptance paragraph, and the replay
record were inspected. The full imported proof is **unread**. The source
statement snapshot and the replay snapshot identify different
formal-conjectures version locators. Both explicitly describe the same
mathematical indexed conclusion, and the current claim interface agrees with
it. This examination does not assert byte identity between those two external
versions or independently recheck their definitional closures; it relies on
the identified acceptance and statement check for the replayed task.

This is the nonrecursive external-source boundary permitted by
`docs/verification.md`, **Premises and source boundaries**. The acceptance and
receipt support precisely the indexed premise used, at its recorded
accepted/formalized standing. They are not acceptance evidence for the new
dyadic-root deduction. The absence of a fresh imported-proof audit or replay
is explicit, not a stronger theorem assumed silently. The elementary root,
growth, floor and finite-set arguments are rederived above. No native L-claim
is consumed, and no native ledger row or native tier is imported.

### Current dependency reading and exposure

At final filing on 2026-10-14 at 17:49 UTC, the then-current commissioning
revision was resolved, and the following two paths were read at that same
revision, without synchronization:

- `wiki/problems/additive_bases/E0354/claims/2026_09_11_jenw1n.md`,
  the fields `status`, `claim`, `scope`, `evidence`, its Claim/Covers
  statement interface, and its first Acceptance paragraph.
- `library/number_theory/conjectures_io_2026_lean_solutions_erdos_problems/evidence/verify/receipt_e0354_815c1d5f.md`,
  the supplied replay receipt path.

The permitted metadata reads `status: accepted`, `claim: proved`,
`scope: partial`, and `evidence: [formalized]`. “Partial” limits the source
claim to the first, base-$2$ question; its Covers paragraph explicitly
excludes strong completeness, the set-union formulation and the second
question. These exclusions agree with the frozen interface and are respected
by the deduction. The four metadata fields and first Acceptance paragraph
match the frozen warrant; the current replay receipt's body matches the
preserved replay extraction. No difference in the consumed statement or
warrant, and no pending source acceptance, was found in the permitted fields.

**Exposure during the dependency examination.** At 17:31:12 UTC on the same
date, the extraction of the current claim page selected whole labelled
sections rather than only the permitted statement interface and first Acceptance
paragraph. After the statement it
displayed a source-proof description involving coefficient rescaling, binary
digit criteria, and a joining/disjointness argument. After the first Acceptance
paragraph it displayed additional site-certification, manual-review and
prior-art claims; historical catalog-standing statements; a note concerning
an unrun second kernel; and historical source-version retrieval and
reconstruction statements. Those additional passages were outside the
commissioned reading boundary.

The exposure was disclosed immediately to the commissioning party. A corrected
selection at 17:32:57 UTC checked only the authorized interfaces and first
Acceptance paragraph. No linked proof, source file or other review was opened.
The additional passages are not used as a premise or as acceptance evidence
in this report. Their materiality remains for a distinct grader to decide;
this report does not treat the corrected extraction as erasing the exposure.
The exact content categories and the point at which they were received are
recorded here so that the ruling can address their possible influence.

### Reproduction boundary

The five preserved snapshots and the derivations and attack witnesses in this
report reconstruct the assessed deduction from an ordinary clone. Interpret
relative links printed inside a verbatim snapshot against the original public
path in its manifest; those printed links are not additional material examined
here. The mathematical checks are the displayed exact inequalities, index
maps, and positional-expansion witnesses. No computational rerun command or
code is needed for them.

The imported receipt describes an earlier replay command and a solution and
port with restricted holding. That command was not rerun; the solution,
driver, port and underlying Lean proof were not inspected. The five-file
package does not supply an ordinary-clone reproduction of that external
replay. It preserves the prior acceptance warrant and its exact theorem
interface, which is the external premise boundary of this examination.
There is no new kernel or computational certification here.

## Checklist

The following verdicts concern the complete D1 deduction and its stated
consequence, with the external-proof boundary just described. “No defect found”
records an examination result, not a grader's contract judgment.
Every row applies to both conclusions. Steps 1–2 establish the single-ray
statement with finite deletion; step 3 then uses it for the consequence,
without an additional theorem premise.

### Erdos-specific checklist

| Item | Verdict and reason |
| --- | --- |
| Quantifiers and scope | No defect found. Steps 1–2 fix one tail before all large targets and cover every $m\ge2,t>0,L,F$. They assert eventual completeness, not coverage of all small integers. Step 3 fixes the base before both coefficients. |
| Circularity | No defect found. The external base-$2$ theorem has strictly the recorded interface; growth, injectivity and inclusions are proved without assuming the single-ray conclusion. No induction assumes completeness or termination. |
| Model and convention changes | No defect found. The index-to-value transfer is justified by two disjoint index maps and an injective tail. Both starting-index conventions and both finite-deletion conventions are accounted for. |
| Finite and statistical overreach | Inapplicable to the proof: no finite experiment, density estimate, averaging heuristic or statistical sample supports it. The attack examples above refute proposed shortcuts; no finite evidence is extrapolated to an infinite theorem. |
| Uniformity | No defect found. $j$ depends on the prescribed parameters, and the external threshold depends on the resulting coefficients. No numerical uniformity or exchange of limits is asserted. The arbitrary-$F$ uniformity counterexample is retained. |
| Extremal conclusions | Inapplicable. There is no sharp threshold, optimal base, infimum, supremum or attainment assertion. The fixed root is a witness, not an extremizer. |
| Consequences and composition | No defect found at the stated source standing. Source hypotheses, exact power identities, pairwise disjointness and positivity are established before composition. Step 3 separately checks the consequence. The universal-base reading receives no verdict. |
| Computation | Inapplicable to the new deduction. All arithmetic and examples are exact and exposed in prose. No numeric enclosure, range-enumeration result or executable checker is used. The external replay has only its recorded acceptance weight. |
| Reproduction | The noncomputational derivations and all five exact inputs are retained. No new rerun is claimed. The prior replay command and full external proof remain outside the execution and inspection coverage, explicitly recorded above. |
| Source and verdict fidelity | The permitted external statement, warrant and live interface agree at the strength used. No earlier verdict on D1 is imported. The source-record over-read is disclosed and requires independent materiality adjudication. The verdict words below are written in full. |

### General canonical modes

| Mode | Explicit disposition |
| --- | --- |
| “Almost all” upgraded to “all” | Absent. The source gives every sufficiently large target; all parameter values satisfy the checked specialization. No exceptional parameter set is discarded. |
| Induction presupposing termination | Absent. Tail existence follows from an explicit unbounded lower bound for $\gamma^j$; no search is assumed to terminate because completeness is desired. |
| Probabilistic or averaging heuristics treated as proof | Absent from D1. No claim about the methods of the unread imported proof is made. |
| Circular use of an equivalent statement | Absent. Neither the single-ray statement nor its existential consequence is a premise. Ordinary definitions of subset sums do not assert completeness. |
| Exceptional sets dropped from density arguments | Inapplicable. There is no density argument. Positivity and irrationality are verified for every chosen pair of source coefficients. |
| Finite verification treated as more than base-case coverage | Absent. The proof is symbolic for arbitrary parameters; the finite illustrative collisions are not cited as a universal verification. |
| Relaxed or averaged convergence substituted for the objects | Absent. Every transported term equals an actual floor term, and the finite index-to-value map preserves the sum exactly. |

### Named patterns

| Pattern | Explicit disposition |
| --- | --- |
| Model-class transport instead of entailment | No model-class classification is used. The relevant convention transfer is an explicit injective sum-preserving map, not an analogy of formulas or terminology. |
| Uniformity over an infinite family from finite instances | Absent. The argument works for arbitrary $m,t,L,F$ with parameter-dependent choices, and no experiment supplies a uniform constant. |
| Extremal claims in the claim's own units | Inapplicable. No extremal claim is made. The finite maximum of $F\cup\{0\}$ is an ordinary finite-set bound whose existence is proved by finiteness. |
| Consequence sentences are claim surfaces | Checked independently in step 3 and in the quantifier attack. The witness $\sqrt2$ proves the existential reading, with the stronger all-positive-pairs statement at that fixed base. |
| Carry the hypotheses used by a quantified argument | Checked. Finiteness of $F$ supplies its bound; $t>0$ and $\gamma>1$ supply growth; integer $m\ge2$ supplies irrationality and disjoint classes. No boundedness of the entire parameter family is used. |
| A composition inherits its unproved premises | Checked at the exact external boundary. Only indexed dyadic completeness is imported; all strengthening steps are supplied above. The full imported proof retains its recorded acceptance and has not gained a new audit from this examination. |
| Reproducibility notes are claims | No new execution or passing-run claim is made. Reconstruction of the deduction uses the retained snapshots and exact derivations; the external replay command is explicitly not re-executed or certified here. |
| Verifier quotations are claims | No previous examination of D1 is quoted or characterized. Descriptions of the imported acceptance are confined to the supplied first Acceptance paragraph and replay record. Broader material inadvertently displayed is disclosed, not adopted as warrant. |
| Verdict words spelled in full | Satisfied in this report: the mathematical verdict is written as **refutation-failed**. No abbreviated verdict or self-awarded grade is used. |
| Certified brackets fail loudly | Inapplicable. No numerical bracket, enclosure routine, iteration cap or phase window occurs. |
| A harness leg without a failing input is decoration | Inapplicable. No computational mathematical leg was manufactured. The exact collision, multiplicity and deletion examples expose real failures of the candidate shortcuts. Preservation checks are not used as mathematical evidence. |
| A gate reading caches instead of rerunning is defective | No new gate or replay is claimed. Prior external acceptance is used openly under the source-premise rule; cached output is not presented as a new execution. |

The neighboring coverage discipline is met by distinguishing the symbolic
deduction from the unread external proof and its unreplayed acceptance record.
The correlated-sample discipline is inapplicable because there is no statistical
inference. This is neither a computational batch nor a second review cycle;
there is no disjoint computational reproduction obligation to discharge.

## Verdict and grading

**Mathematical verdict for the complete single-ray theorem and its finite-deletion
strengthening: refutation-failed.** Under the exact accepted external indexed
dyadic theorem, the frozen argument proves eventual completeness by distinct
integer values for every $m\ge2$, $t>0$, prescribed first index and finite
deleted set. Its routine inference reconstructions are displayed above; no
substantive missing lemma, stronger imported premise or replacement proof is
used.

**Mathematical verdict for the stated existential-base consequence:
refutation-failed.** The single base $\gamma=\sqrt2$ works for all positive
$\alpha,\beta$, and therefore for the irrational-ratio pairs in the
commissioned formulation. No conclusion about every real base in $(1,2)$,
the entire ambiguous catalog question, a wider classification or novelty is
warranted by this report.

These are mathematical findings about the preserved subject, not a grade or a
standing decision. A distinct eligible grader must assess the complete report
and rule on the disclosed source-record exposure before this report is relied
on as an independently accepted examination. The imported proof's full audit
and a new Lean replay remain outside the report's coverage. No native tier or
project-solution standing is asserted.

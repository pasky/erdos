---
name: research/leads/exceptional_widths_shifted_omega/evidence/verify/width_counterexample/report
title: Examination of the exceptional-width construction for omega
desc: >-
  Independent examination of the exceptional-width counterexample for omega,
  including density, real endpoints, external premises, and the limits of its
  formulation remarks.
created: 2026-10-15T02:28:16Z
updated: 2026-10-15T02:28:16Z
---

# Examination of the exceptional-width construction for omega

***

## Subject and independence

This is an independent whole-conclusion mathematical examination for Plasma AI,
dated **2026-10-14 UTC**. The reviewer was neither the author of nor a
collaborator on the construction, had no prior exposure to it before this
examination, and worked from a fresh review context charged to find a
counterexample, missing hypothesis, unsupported inference, or quantifier error.
The disclosed reviewer model was GPT-6-Astra. This report makes mathematical
findings; it does not grade itself or assign verification standing.

The mathematical subject was frozen on **2026-10-14 at
17:27:31.684793 UTC**. Its five exact extractions are preserved in
`wiki/research/leads/exceptional_widths_shifted_omega/evidence/assets/width_subject/`.
Every filename in the first column below denotes a file in that folder. The
[public manifest](../../assets/width_subject/manifest.json) records the mapping
and the uniform `[cut]` marker.

| Preserved input | Original subject or source identified in the supplied packet | Reading depth |
| --- | --- | --- |
| [argument.md](../../assets/width_subject/argument.md) | The preserved argument itself is the named mathematical subject. The underlying author account was not supplied or examined. | Whole extraction, including every consequence sentence. |
| [target.md](../../assets/width_subject/target.md) | `wiki/problems/arithmetic_functions/E0122/_index.md`, modified Statement and its sequence interpretation. | Whole extraction. |
| [premise_statement.md](../../assets/width_subject/premise_statement.md) | `library/arithmetic_functions/erdos_1997_locally_repeated_values_arithmetic_functions_iv/lemma_1.md`, Lemma 1 statement. | Whole extraction; all clauses compared with the source excerpt. |
| [premise_source.md](../../assets/width_subject/premise_source.md) | `library/arithmetic_functions/erdos_1997_locally_repeated_values_arithmetic_functions_iv/erdos_1997_locally_repeated_values_arithmetic_functions_iv.md`, Lemma 1 excerpt from the held transcription. | Whole supplied statement; no source proof or page image. |
| [premise_warrant.md](../../assets/width_subject/premise_warrant.md) | Supplied reading-depth record concerning the same source. The supplied manifest gives no separate original repository path for this record. | Whole extraction. |

These paths identify the assessed snapshots, not a later version of a problem
page, library page, or author account. The input identities were checked before
reading and again when completing this report. The mathematical read set was
exactly these five extractions and their supplied manifest. The full argument,
statement, and dependency records in that set were read. The cut markers were
not treated as information about omitted text.

Operating reading comprised the supplied charter, effective settings and
steps; the repository README; the Claims, Evidence, Tiers, and Project claims
sections of `docs/anatomy.md`; all of `docs/verification.md`,
`docs/evidence.md`, `docs/math_authoring.md`, `docs/weaving.md`,
`campaign/AGENTS.md`, and `campaign/guides/verification.md`; the Reading section
of `campaign/guides/research.md`; and the permitted native operating
instructions. Those instructions did not expand the mathematical read set.

The subscription checks were empty, receiving channels remained sealed, and
automatic synchronization was disabled. No author working context, prior
examination, current ledger, sibling material, message inbox, source-link
target, or web search was read. No excluded communication or search exposure
occurred. The reviewer used only this examination's own preparation notes
between its stages. The recorded source reading depth is a dependency input,
not an earlier verdict on this construction.

The independent mathematical evidence is the derivations and attacks in this
report. No computation supports the verdict, so there is no mathematical
program or computational rerun command. A reader can reconstruct the assessed
argument from the five retained inputs and reproduce every calculation below
without a private archive or additional source. The external theorem boundary
is stated explicitly in **Premises**.

## Restatement and interpretation

Write $\mathbb N_{>0}=\{1,2,\ldots\}$ and let $\omega(n)$ count distinct prime
divisors, with $\omega(1)=0$. For a positive width $F$ and $x\ge1$, define

$$
R_F(x)=\frac{1}{F(x)}
\#\{n\in\mathbb N_{>0}:x<n+\omega(n)<x+F(x)\}.
$$

The construction claims the existence of a positive, in fact integer-valued,
function $F:[1,\infty)\to(0,\infty)$ and a set $S\subseteq\mathbb N_{>0}$
such that

$$
\lim_{x\to\infty}F(x)=\infty,
\qquad
\lim_{N\to\infty}\frac{|S\cap[1,N]|}{N}=1,
\qquad
\lim_{\substack{n\to\infty\\n\in S}}
\frac{F(n)}{\omega(n)}=0,
$$

while $R_F(x)\le7$ for every sufficiently large real $x$. The set $S$ is
fixed; it is not chosen anew for each error tolerance. The first limit is at
all real locations, whereas the smallness assertion is only along $S$ at the
integers. Counts are of inputs $n$, including different inputs with the same
shifted value, and both interval endpoints are open.

Under the supplied interpretation, the modified target for $f=\omega$ asks
whether every admissible $F$ admits a sequence $x_k\to\infty$ with
$R_F(x_k)\to\infty$. A single admissible $F$ bounded as above negates that
universal assertion. The frozen text writes $F(n)$ in the hypothesis and
$F(x)$ in the conclusion without declaring the domain of $x$. The construction
covers both the integer-location reading, using the restriction of $F$, and
the real-location reading, using its specified floor extension. It uses the
commissioned natural-density-one meaning of “almost all”; it does not claim
the cofinite or everywhere-small meaning. No monotonicity is assumed.

The supplied interpretation turns the phrase about infinitely many $x$ into a
limit along a sequence. In fact the stated choices on the initial intervals
also give a global bound for $x\ge1$, as shown below, so a sequence confined to
a bounded subset of this domain cannot evade the counterexample either.

Only the negative answer for $\omega$ under these conventions is at issue.
There is no classification of other functions, conclusion for $\tau$,
historical novelty finding, or resolution of a uniform-width or monotone-width
variant. The literal assertion in the final formulation remark about excluding
this particular $F$ is examined separately below.

## Premises and source boundary

The dependency census was derived from the frozen proof and its consequences.
It contains **no native L-claim**. No live claim-standing read was needed or
authorized. On the examination date, the premise interface assessed was the
one preserved in the five inputs; no ledger standing was inferred from a
source-owned theorem or its reading-depth label.

The non-elementary estimate used is Lemma 1 of Erdős, Pomerance and Sárközy,
*On locally repeated values of certain arithmetic functions, IV*,
*The Ramanujan Journal* **1** (1997), 227–241, statement on printed
pp. 229–230, DOI 10.1023/A:1009723712317. The library statement and supplied
transcription excerpt agree in their hypotheses, definitions, strict
inequality, and absolute-constant assertion. Their typography does not change
any consumed clause.

| Source clause | Specialization actually consumed |
| --- | --- |
| $x\ge1$ and $m\le x^{1/2}$ | $x=X\ge2$ and $m=1$, so the size condition holds. |
| $h\in\mathbb Z$ and $n\equiv h\pmod m$ | Take $h=0$; every integer lies in this residue class modulo $1$. |
| $f$ nonnegative and additive | $f=\omega$; the prime divisors of coprime factors are disjoint, proving additivity, and all values are nonnegative. |
| $f(p^\alpha)=0$ for $p\mid m$ | Vacuous because no prime divides $1$. |
| $K=\max_{p^\alpha\le X} f(p^\alpha)$ | The maximum is nonempty for $X\ge2$ and equals $1$, because $\omega(p^\alpha)=1$. |
| $A=\sum_{p\le X}f(p)/p$ | Exactly $A(X)=\sum_{p\le X}1/p$. |
| Absolute constant independent of all parameters | One fixed $C>0$ works for every $X\ge2$, hence for every dyadic index used below. |

Consequently the imported interface is

$$
\sum_{1\le n\le X}(\omega(n)-A(X))^2
\le C X(A(X)+1)\qquad(X\ge2). \tag{1}
$$

The supplied strict inequality implies this weak inequality in the consumed
range. The review relies on (1) as the identified published external premise;
it does not provide an independent proof of EPS97 Lemma 1. The supplied
reading-depth record labels its coverage “Claims checked”: the statement and
remarks were checked against printed pages, and the proof on pp. 230–232 was
read but not checked step by step. It records no independent review. That is
the record's coverage, not this reviewer's. This reviewer read
only the two supplied statement forms and that record, with no PDF inspection
and no proof inspection. No local independent certification of the source
proof is asserted.

There is an unused degeneracy in the general statement as supplied. At
$x=2$, $m=1$, $h=0$, and $f\equiv0$, all its stated hypotheses hold, but
$K=A=0$ and its strict conclusion reads $0<0$. Thus that unrestricted strict
statement, interpreted literally, is **refuted-as-stated** by this exact
witness. Also, the displayed maximum has an empty index set for $1\le x<2$
unless a convention is added. Neither issue is used by the construction:
$X\ge2$, $K=1$, and $A(X)\ge1/2$ throughout. The verdict about the construction
consumes only (1), not the unused zero-function or empty-maximum cases. This
observation concerns the supplied text; it does not claim a fresh inspection
of the printed source or a replacement proof of its positive-$K$ instance.

The other explicit external premise is Euler's theorem

$$
\sum_{p\le X}\frac1p\longrightarrow\infty.
$$

It is used only to make $A_j$, and hence $H_j$, tend to infinity and to make
the ratios in the next section vanish. No asymptotic formula for $A(X)$, prime
number theorem, or probabilistic normal-order theorem is imported. The bound
$A(X)\le1+\log X$ follows by comparison with the harmonic sum. Euler's
divergence is relied upon as the expressly permitted classical theorem, not
reproved here. The further finite-product inequality used solely to attack
the formulation remark is derived in full below.

## Weakest steps

The following three reconstructions fill in routine inequalities, counts and
limit quantifiers in the frozen argument. They do not replace its strategy or
repair an essential missing lemma. The additional lemma missing from the
literal final remark is kept separate in **Formulation remark**.

### 1. From the external moment estimate to a usable dyadic scale

Put $I_j=[2^j,2^{j+1})\cap\mathbb N_{>0}$ and use the frozen definitions

$$
X_j=2^{j+2}=4\cdot2^j,\qquad A_j=A(X_j),\qquad
H_j=\lceil A_j^{3/4}\rceil.
$$

Euler's divergence gives $A_j\to\infty$. The ceiling satisfies

$$
A_j^{3/4}\le H_j\le A_j^{3/4}+1,
\qquad
\frac{H_j}{A_j}\le A_j^{-1/4}+A_j^{-1}\longrightarrow0. \tag{2}
$$

Also $A_j\le1+(j+2)\log2$, so $H_j+1=o(2^j)$. Choose a single integer
$j_0\ge1$ sufficiently large that, for every $j\ge j_0$,

$$
H_j\ge1,\qquad H_j\le A_j/2,\qquad
2^{j+1}+H_j+1<2^{j+2}. \tag{3}
$$

Only existence of this finite cutoff is needed. No numerical cutoff or
unproved effective rate is being claimed.

For the frozen set
$D_j=\{n\in\mathbb N_{>0}:n\le X_j,\ |\omega(n)-A_j|>H_j\}$,
each member contributes more than $H_j^2$ to the sum in (1). Therefore

$$
\frac{|D_j|}{2^j}
\le4C\frac{A_j+1}{H_j^2}
\le4C(A_j^{-1/2}+A_j^{-3/2})
\longrightarrow0. \tag{4}
$$

This is a deterministic consequence of (1), not a sampling or independence
argument. The constant is fixed as $j$ varies. In particular, (4) is strong
enough for both exceptional-set uses; neither requires a summable sequence of
error proportions.

### 2. From sparse bad inputs to a bound at every location

For each $u\in I_j$, let $b_j(u)$ count inputs $n\in D_j$ with
$u<n+\omega(n)<u+H_j+1$, exactly as in the frozen text. For a fixed input let
$m=n+\omega(n)\in\mathbb Z$. The possible integer left endpoints satisfy

$$
u<m<u+H_j+1
\quad\Longleftrightarrow\quad
m-H_j\le u\le m-1.
$$

There are exactly $H_j$ such integers before restricting to $I_j$, so the
frozen upper bound of $H_j+1$ is safe. This counts each input separately;
collisions of shifted values do not invalidate the incidence count. Thus

$$
\sum_{u\in I_j}b_j(u)\le(H_j+1)|D_j|. \tag{5}
$$

For $E_j=\{u\in I_j:b_j(u)>H_j+1\}$, integrality gives

$$
(H_j+2)|E_j|
\le\sum_{u\in E_j}b_j(u)
\le(H_j+1)|D_j|,
\qquad |E_j|\le|D_j|. \tag{6}
$$

This remains valid when either set is empty. It imposes no lower bound on
$|E_j|$.

Now fix $j\ge j_0$ and $u\in I_j\setminus E_j$. A positive integer counted
in $(u,u+H_j+1)$ satisfies

$$
n\le n+\omega(n)<u+H_j+1
<2^{j+1}+H_j+1<X_j. \tag{7}
$$

Hence no counted input lies beyond the range of the source estimate. If it is
not in $D_j$, then $A_j-H_j\le\omega(n)\le A_j+H_j$, and therefore

$$
u-A_j-H_j<n<u+2H_j+1-A_j. \tag{8}
$$

The interval in (8) has length $3H_j+1$ and contains at most $3H_j+2$
integers, which is the deliberately loose bound used by the frozen proof.
The counted inputs in $D_j$ number at most $H_j+1$ because $u\notin E_j$.
These two disjoint classes exhaust the count by (7), giving at most
$4H_j+3$ inputs. No injectivity or monotonicity of $n+\omega(n)$ is used.

Define the frozen $F$ precisely by using $u=\lfloor x\rfloor$. For
$u\in I_j$ with $j\ge j_0$, set $F(x)=H_j$ off $E_j$ and
$F(x)=2(u+1)$ on $E_j$. For $1\le u<2^{j_0}$ use $F(x)=2(u+1)$.
These cases cover every $x\ge1$ and give positive widths.

Off $E_j$, $u\le x<u+1$ implies

$$
(x,x+H_j)\subseteq(u,u+H_j+1),
\qquad R_F(x)\le4+\frac3{H_j}\le7. \tag{9}
$$

The left endpoint remains open even at $x=u$; the right endpoint inclusion
uses the strict inequality $x<u+1$. An exact integer or dyadic boundary is
assigned to its new floor cell and satisfies the same argument there.

On the other branch, including all early cells, any counted input satisfies

$$
1\le n<x+2(u+1)<3(u+1).
$$

There are at most $3(u+1)-1$ such positive integers, whence

$$
R_F(x)\le\frac{3(u+1)-1}{2(u+1)}<\frac32. \tag{10}
$$

This is why positivity of the input domain and nonnegativity of $\omega$ are
essential. There is no appeal to concentration at an exceptional location.
Equations (9) and (10) prove the promised uniform bound; with the specified
initial branch they in fact give $R_F(x)\le7$ for every $x\ge1$.

### 3. Density-one admissibility and the exact target implication

Here is the dyadic density argument with its partial-block quantifier. If
$T_j\subseteq I_j$ and $|T_j|=o(2^j)$, then for every $\varepsilon>0$ there
is $J$ with $|T_j|\le\varepsilon2^j$ for all $j\ge J$. Given
$2^k\le N<2^{k+1}$,

$$
\left|\left(\bigcup_{j\ge j_0}T_j\right)\cap[1,N]\right|
\le C_J+\varepsilon\sum_{j=J}^k2^j
\le C_J+2\varepsilon N. \tag{11}
$$

The finite constant $C_J$ vanishes after division by $N$; then
$\varepsilon$ is arbitrary. No equidistribution inside the last block is
needed. In particular an adversary may put all of that block's exceptional
points near its beginning without defeating (11).

Apply (11) first to $E_j$, using (4) and (6), and separately to
$B_j=D_j\cap I_j$, using (4). These are different uses of the bad-input
estimate: the first controls locations with crowded bad images, and the
second controls the values of $\omega$ at the integer arguments of $F$.
Define

$$
E=\bigcup_{j\ge j_0}E_j,\qquad
B=\bigcup_{j\ge j_0}B_j,\qquad
S=\mathbb N_{>0}\setminus\bigl([1,2^{j_0})\cup E\cup B\bigr).
$$

Both $E$ and $B$ have natural density zero, and $S$ has natural density one.
For $n\in S\cap I_j$, the definitions and (3) give

$$
F(n)=H_j,\qquad
\omega(n)\ge A_j-H_j\ge A_j/2>0,
\qquad
\frac{F(n)}{\omega(n)}\le2\frac{H_j}{A_j}\longrightarrow0. \tag{12}
$$

The upper bound is uniform over $n$ in each good part of a block. Given any
positive tolerance, (2) supplies one block index beyond which (12) holds
for every $n\in S$. This is ordinary convergence along the fixed set $S$,
not just convergence of averages. The undefined ratio at $n=1$ is removed by
a finite exclusion and is never used.

Finally, both possible widths tend to infinity as their locations do.
Indeed $j\to\infty$ when $x\to\infty$, $H_j\to\infty$, and
$2(\lfloor x\rfloor+1)\to\infty$. For any prescribed lower bound, choose
a single tail on which both branches exceed it. This proves the everywhere
real limit of $F$ without discarding $E$.

Thus one and the same $F$ satisfies all the admissibility quantifiers and
obstructs the target conclusion at every location in its domain. In particular
there is no sequence of real or integer locations tending to infinity along
which $R_F$ diverges. This is exactly the required negation for $f=\omega$;
it makes no assertion about the rest of the classification question.

## Strongest attacks and findings

The strongest attack on the core conclusion was to combine two possible
losses: a density-zero set of bad inputs might produce very crowded images at
many locations, and counted inputs might lie beyond $X_j$ or cross a floor
boundary. Merely removing the bad inputs would not prove an everywhere bound.
Equations (5)–(7) show why that attack fails here: each bad input has bounded
incidence with integer windows, the exceptional location set absorbs every
window exceeding the threshold, and nonnegativity forces all remaining
counted inputs inside the controlled range. At the absorbed locations the
width changes and the independent positive-input bound (10) applies. No
exceptional location is dropped from the final estimate.

A separate attack concentrated every exceptional set at the start of its
dyadic block and chose $N$ just beyond that concentration. Equation (11)
still bounds its contribution by $2\varepsilon N$ plus a fixed finite term.
This defeats a possible sparse-block-to-natural-density error. Applying it
separately to $B_j$ prevents the mistake of using sparsity of output locations
as if it implied typicality of $\omega(u)$ at those locations.

The endpoint attack tested $x=u$, $x$ immediately below $u+1$, and the exact
boundary $x=2^{j+1}$, allowing many inputs to share an image. The incidence
equivalence and (8)–(10) preserve the open endpoints and multiplicities in all
these cases. The extra unit in the integer window is enough for the entire
real cell. None of these attacks refuted the main construction.

### Formulation remark: a literal exclusion needs an additional lemma

The final sentence of `argument.md`, lines 104–106, asserts that the added
condition $F(n)=o(\log\log n)$ everywhere “would prohibit this construction,”
then says the argument does not decide that variant. The second statement is
an appropriate scope limit. The first has a stronger literal reading:
**the particular constructed $F$ fails that added condition**. That reading
is not established by the frozen proof.

The exact missing interface is the infinitude of $E$. This is not just an
objection to omitted wording. For this $F$, one can identify the issue exactly:

$$
F(n)=o(\log\log n)\text{ as }n\to\infty\text{ through all integers}
\quad\Longleftrightarrow\quad E\text{ is finite}. \tag{13}
$$

Here is an elementary diagnostic derivation of (13), independent of any
unstated asymptotic theorem. For $Y\ge e$, put $s=1+1/\log Y$. For $p\le Y$
we have $p^{s-1}\le e$, and positivity and unique factorization give

$$
\begin{aligned}
A(Y)
&\le e\sum_{p\le Y}p^{-s}
 \le e\log\prod_{p\le Y}(1-p^{-s})^{-1}\\
&\le e\log\sum_{n=1}^{\infty}n^{-s}
 \le e\log\left(1+\frac1{s-1}\right)
 =e\log(1+\log Y).
\end{aligned} \tag{14}
$$

The finite product expands into the sum over integers whose prime factors
belong to its finite prime set; this is a subseries of the displayed positive
series. The final series bound is the integral comparison for $t^{-s}$.
Thus no Euler product theorem or prime asymptotic is being cited in (14).

For $n\in I_j\setminus E_j$ this gives
$F(n)=H_j=O((\log(j+2))^{3/4})$, whereas
$\log\log n\ge\log(j\log2)$. Therefore
$F(n)/\log\log n\to0$ uniformly off $E$. On an unbounded sequence in $E$,
however, $F(n)=2(n+1)$ and this quotient tends to infinity. Finite early choices
affect neither conclusion. This proves (13).

The frozen estimates (4)–(6) are all upper bounds. They permit an empty $E_j$
and supply no lower bound forcing $E$ to be infinite. The literal exclusion
therefore needs, for example, the additional assertion

$$
\forall J\ \exists j\ge J\ \exists u\in I_j:
b_j(u)>H_j+1. \tag{15}
$$

No proof of (15) is supplied. This examination has not proved (15), disproved
it, or introduced another theorem to settle it. An empty-exceptional-set
possibility is a witness to the missing inference, **not** a counterexample
asserted for the actual arithmetic function $\omega$.

Accordingly the literal assertion that the constructed $F$ is excluded by
the everywhere $o(\log\log n)$ condition has the verdict **proof defective;
statement unresolved**. Read merely as a warning that the current proof has
not established that stronger admissibility requirement, the remark is
appropriate. Neither reading invalidates (1)–(12): the main counterexample
works whether $E$ is finite or infinite. The diagnostic (13)–(14) exposes the
missing lemma; it does not repair it or resolve the uniform-width variant.

## Checklist

The entries below are mathematical audit observations, not a self-grade of
this report. They cover the governing Erdos checklist and explicitly address
every canonical mode and named pattern in `docs/verification.md`.

### Erdos checklist

| Item | Finding |
| --- | --- |
| Quantifiers and scope | No core defect found. (11)–(12) give one density-one integer set; the width limit and count bound hold at every real location in the tail. The integer restriction, sequence interpretation, positive inputs, finite prefix, and open endpoints are addressed explicitly. |
| Circularity | No target or equivalent assertion is assumed. Definitions of $D_j$, $b_j$, $E_j$, and $F$ are finite at each index and contain no recursive termination claim. |
| Model and convention changes | The floor extension is proved by inclusion (9); the actual inputs are counted with multiplicity. No averaged or abstract substitute is used for the pointwise bound. The density-one convention is an explicit restriction of the verdict. |
| Finite and statistical overreach | No finite experiment or statistical sample is used. The moment estimate is an external theorem, and (4)–(6) are deterministic inequalities. Correlated-sample issues are inapplicable. |
| Uniformity | $C$ in (1) is fixed; all tail choices in (2)–(4) are uniform in $u$. Bounds $7$ and $3/2$ are independent of $j$, $u$, and $x$. The partial-block estimate (11) controls arbitrary integer cutoffs. |
| Extremal conclusions | The relevant quantity is count divided by the actual width, checked in (9)–(10). No optimum, sharp constant, or attainment claim is made. |
| Consequences and composition | The negation of the universal-$F$ target follows from one admissible bounded construction. The literal uniform-width exclusion has the separate missing interface (15); it is not warranted by the core proof. No omitted native premise is consumed. |
| Computation | Inapplicable: no mathematical program, numerical enclosure, parameter search, or finite certificate supports the verdict. Short arithmetic and infinite arguments are retained in full. |
| Reproduction | The exact five inputs and all independent derivations are retained. No computational rerun or cached-success claim is made; no external executable input is needed. |
| Source and verdict fidelity | The two supplied source statements agree and their consumed positive-$K$ specialization is exact. The unused strict-zero degeneracy is witnessed explicitly. Source proof coverage is not upgraded, the literal formulation caveat is qualified, and all mathematical verdicts are written in full. |

### Canonical modes

| Canonical failure mode | Finding |
| --- | --- |
| Almost all upgraded to all | Not present in the core: $S$ is used only for smallness, while the width limit and both count branches are proved everywhere. |
| Induction presupposing termination | Inapplicable: no induction, iterative search, or stopping rule is used. |
| Probabilistic or averaging heuristics presented as proofs | Not present: the moment bound is an identified theorem and the subsequent averaging is exact finite double counting. |
| Circular use of an equivalent statement | Not present: neither exceptional-set sparsity nor the bounded normalized count is used to establish itself. |
| Exceptional sets dropped from density arguments | Not present in the core: $E$ and $B$ are both retained, their densities proved separately, and $E$ receives its own everywhere count bound. |
| Finite verification overreach | Inapplicable: the proof contains no finite verification claimed to settle an infinite assertion. |
| Relaxed or averaged convergence substituted for actual objects | Not present: (9), (10), and (12) concern the actual $F$, actual shifted inputs, and fixed set $S$. |

### Named patterns

| Named pattern | Finding |
| --- | --- |
| Model-class transport instead of entailment | Inapplicable as an axiom-system classification issue. The actual mathematical transfers here are established in (7)–(12), not inferred from matching vocabulary. |
| Uniformity over an infinite family from finitely many instances | Not present: every dyadic index beyond one cutoff is covered symbolically. The sole imported constant is independent of the index. |
| Extremal claims in their own units | The normalized ratios are computed with the branch's own $F$ in (9)–(10). Sharpness and attainment are not claimed. |
| Consequence sentences are claim surfaces | Applied: the main negation survives, but the literal exclusion in the last sentence requires (15). The report does not give that sentence an unqualified favorable verdict. |
| Carry hypotheses used by quantified arguments | All consumed source hypotheses, positivity, integer images, and the uniform cutoff are checked. Infinitude of $E$, needed for the stronger literal aside, is not available and is not silently assumed. |
| Composition inherits unproved premises | The imported estimate and Euler divergence remain explicit external boundaries. No native claim is consumed. The missing lemma (15) affects only the literal exclusion assertion and is not repaired here. |
| Reproducibility notes are claims | No executable rerun or passing-check count is claimed. The retained snapshots and explicit derivations supply the noncomputational reproduction route. |
| Verifier quotations are claims | No prior construction verdict is quoted or relied upon. The supplied source-depth record is reported only at its actual scope; grading and standing statements outside the extraction were not read. |
| Verdict words spelled in full | The verdicts refutation-failed, refuted-as-stated, and proof defective; statement unresolved are written in full and attached to distinct, explicitly named surfaces below. |
| Certified-bracket functions fail loudly | Inapplicable: no numerical routine or enclosure with a resource cap is used. |
| A harness leg with no failing input is decoration | Inapplicable: there is no mathematical test harness or artificial always-passing leg. The mathematical attacks have explicit possible failure mechanisms, and the supplied strict-zero statement has the concrete failing input above. |
| A gate reading caches instead of rerunning is defective | Inapplicable: no mathematical verdict rests on a gate, cached computation, or success summary. File-identity checks establish only subject identity. |

The evidence-coverage discipline is satisfied by identifying the independent
derivations, external theorem boundary, and unresolved ancillary inference.
The neighboring discipline about correlated statistical samples is inapplicable
because no statistical inference is made. This is one noncomputational review,
not a computational batch or a repeated independent cycle; the corresponding
extra reproduction and second-cycle requirements are inapplicable.

## Verdict and grading

| Assessed surface | Mathematical verdict and limit |
| --- | --- |
| The complete exceptional-width construction and its negative answer for $f=\omega$ under the stated natural-density-one convention | **refutation-failed.** The supplied proof establishes the everywhere width divergence, density-one integer smallness, and uniformly bounded normalized counts for all sufficiently large real locations. Its finite initial choices also make the normalized count bounded over the whole stated domain. This relies on the expressly identified external estimate (1) and Euler's divergence. |
| The final remark read as asserting that this particular $F$ cannot satisfy everywhere $o(\log\log n)$ | **proof defective; statement unresolved.** The exact missing lemma is (15), equivalently infinitude of $E$ for this construction. The weaker reading that the proof does not establish the stronger width requirement is supported. No uniform-width or monotone-width problem is resolved. |
| The unused universal strict-inequality wording in the supplied EPS97 statement, including $f\equiv0$ | **refuted-as-stated** at $x=2$, $m=1$, $h=0$, $f\equiv0$. This finding does not refute or independently prove the positive-$K$ specialization (1) consumed by the construction. |

There is therefore no unqualified favorable verdict on every sentence of the
packet. The core construction has no unresolved load-bearing deduction in the
reviewed argument beyond its declared external theorem reliance; the literal
ancillary exclusion has the precise proof gap stated above. No new proof has
been substituted for that gap. The source-proof limit, formulation dependence,
and the unexamined variants remain explicit.

A separate eligible grader must assess the report's independence, coverage,
contract compliance, and the treatment of these distinct surfaces before any
standing decision. This report awards no tier, makes no claim of independent
certification of the EPS97 proof, and covers no bytes written after the frozen
subject.

# Independent review of the matching-prime-gap-window conditional

## Subject and independence

**Frozen subject:** `wiki/research/prime_binary_new_attack/matching_gap_windows.md`, its entire supplied mathematical body, together with the prime-indexing convention in the Statement of `wiki/problems/irrationality/E0251/_index.md`. The freeze and examination dates are 2026-10-16 UTC. The reviewed project argument is credited to Plasma AI.

**Scope:** the definitions and convergence, identities (1)–(4), their proofs, the sufficient tail condition, the separation formulation, the fixed-denominator exclusion criterion, and the final paragraph's limitations. This is an examination of a conditional proposition, not a claimed solution of Problem 251.

**Reviewer:** an independent reviewer in a fresh context, neither an author of nor a collaborator on the subject, with no earlier construction or verification context for it. The mathematical input allowed and actually read was the supplied frozen extraction alone. Its verbatim retained copy is [the subject snapshot](../../assets/matching_gap_windows/subject.md). No original subject page, contextual link, author notes, other review, dependency ledger, or external mathematical source was opened. No mathematical communication or excluded mathematical material was received. Incoming communication remained closed, and the checked subscription table was empty. The assignment's general motivational material supplied no mathematical premise.

The operating reading included the supplied review instructions; `AGENTS.md`; `README.md`; Claims, Evidence, Tiers, and Project claims in `docs/anatomy.md`; `docs/verification.md` in full; the isolated-review, campaign, reading, delivery and closeout operating rules; the relevant statement-scope, source-fidelity, review, and executable-evidence sections of `docs/evidence.md`; and the permitted local command, configuration, skill and computation-wrapper instructions. Operating examples and links were not treated as additional mathematical inputs. Their commissioned identities were checked before use. The supplied subject remained unchanged throughout the examination, and its retained copy was checked byte for byte.

**Provenance limit:** the supplied extraction has no internal revision label or heading naming the main source page. Its attribution to the source paths and freeze date above rests on the explicit commission. The originals were excluded, so this report makes no independent extraction-fidelity claim. The preserved snapshot fixes precisely the text examined; the review does not cover omitted text or later repairs. The separate grader must assess the adequacy of this provenance basis.

The independent derivations, exact witnesses, and their verification are retained below. This is a noncomputational examination: no executable mathematical check, cached result, or numerical approximation is used, and no code or runtime input is needed to reproduce the reasoning.

## Restatement

Let $p_n$ be the $n$th prime, with $p_1=2$, and define, for integers $n\ge1$,

$$
S=\sum_{n\ge1}\frac{p_n}{2^n},\qquad
g_n=p_{n+1}-p_n,\qquad
G_n=\sum_{j\ge0}\frac{g_{n+j}}{2^{j+1}}.
$$

The sums converge, $S=2+G_1$, and $G_{n+1}=2G_n-g_n$. Suppose

$$
S=\frac{a}{2^s d}
$$

in lowest terms, where $a$ is an integer, $s$ is a nonnegative integer, and $d$ is a positive odd integer. The integer interpretation of $s$ is the dyadic-factor convention in the reduced denominator. The intermediate claims are $dG_n\in\mathbb Z$ for $n\ge s+1$, and

$$
G_n\in\frac2d\mathbb Z
\quad\text{for }n\ge\max(s+2,3).
$$

For every integer triple $m>n\ge\max(s+2,3)$ and $K\ge1$, assume both

$$
g_{n+j}=g_{m+j}\quad(0\le j<K)
$$

and

$$
|G_{n+K}-G_{m+K}|<B,\qquad B=\frac{2^{K+1}}d.
$$

The conclusion is $G_n=G_m$ and $G_{n+K}=G_{m+K}$. For $d>1$ it additionally gives $\operatorname{ord}_d(2)\mid(m-n)$, where the order is the least positive exponent giving residue $1$ modulo $d$.

All tails are positive. Thus $G_{n+K}<B$ and $G_{m+K}<B$ together suffice for the absolute-difference hypothesis. Under the same rationality, index and matching-window assumptions, and with $d>1$, failure of the order divisibility forces $|G_{n+K}-G_{m+K}|\ge B$.

The fixed-denominator criterion has the following quantifiers. Fix an odd $d>1$. If, for every index cutoff $N$, there are integers $m>n\ge N$ and $K\ge1$ with matching windows, the specified small-tail condition, and $\operatorname{ord}_d(2)\nmid(m-n)$, then $S$ has no reduced rational denominator with odd part $d$. The difference bound suffices; the two individual tail bounds are a stronger sufficient hypothesis. The window length may depend on the pair and on $d$. The smaller index $n$, not merely $m$ or the window endpoint, must be unbounded for this stated criterion to cover every possible $s$.

No existence theorem for these pairs is asserted. A construction for one $d$ does not settle other odd denominators, and the order argument supplies no obstruction for $d=1$. The final paragraph warns that repetitions alone leave tail and index-class obligations, and that replacing equality by congruences leaves a finite-window contribution. The word “nonzero” in that last warning is examined separately below.

## Weakest steps

### 1. Convergence and the identities concern the actual primes

No prime-distribution theorem is imported. Here is an elementary derivation of enough growth control. For a positive integer $N$, put $C_N=\binom{2N}{N}$. The central coefficient is the largest among the $2N+1$ coefficients whose sum is $4^N$, so

$$
C_N\ge\frac{4^N}{2N+1}.
$$

Counting multiples of prime powers in the factorials gives, for a prime $q$,

$$
v_q(C_N)=\sum_{r\ge1}
\left(\left\lfloor\frac{2N}{q^r}\right\rfloor
-2\left\lfloor\frac{N}{q^r}\right\rfloor\right).
$$

Each summand is $0$ or $1$, and it vanishes when $q^r>2N$. Consequently $q^{v_q(C_N)}\le2N$. Multiplying over the primes at most $2N$ yields

$$
\frac{4^N}{2N+1}\le C_N\le(2N)^{\pi(2N)},
\qquad
\pi(2N)\ge
\frac{2N\log2-\log(2N+1)}{\log(2N)}.
$$

At $N=t^2$, the last lower bound divided by $t$ tends to infinity. Thus $\pi(2t^2)\ge t$ and $p_t\le2t^2$ for all sufficiently large integers $t$. This also establishes that arbitrarily many primes exist. The finitely many smaller indices can be absorbed in a constant. Hence $p_t=O(t^2)$ and $g_t\le p_{t+1}=O((t+1)^2)$. The resulting polynomially weighted geometric series converge; for example, the successive-term ratio for $t^2/2^t$ is eventually bounded strictly below $1$. This proves convergence of $S$ and every $G_n$ without any unexamined source premise.

Splitting the absolutely convergent series, for every fixed $n,K$,

$$
G_n=\sum_{j=0}^{K-1}\frac{g_{n+j}}{2^{j+1}}+2^{-K}G_{n+K}. \tag{R1}
$$

Its $K=1$ instance proves the recurrence. Independently summing the prime differences gives

$$
G_n=2^{n-1}S-A_n,\qquad
A_n=p_n+\sum_{i=1}^{n-1}2^{n-1-i}p_i\in\mathbb Z. \tag{R2}
$$

At $n=1$, this is $G_1=S-2$. These manipulations use ordinary sums of the actual primes; no averaged or substitute sequence supplies convergence. Their validity at every fixed index does not provide the uniform small-tail estimate needed to construct the proposed pairs.

### 2. The two cutoffs and the strict lattice separation

For $n\ge3$, the last two summands of $A_n$ are $p_n+p_{n-1}$, an even number. All earlier summands have an even coefficient. Therefore $A_n$ is even for $n\ge3$. In contrast, $A_2=p_2+p_1=5$ is odd.

Under the rationality hypothesis, (R2) becomes

$$
dG_n=2^{n-1-s}a-dA_n. \tag{R3}
$$

For $n\ge s+1$ this is integral. For $n\ge s+2$ its first term is even, and for $n\ge3$ its second term is even. This independently establishes precisely the asserted safe range $n\ge\max(s+2,3)$ for (1). It also checks the exceptional first prime gap without assuming parity at an invalid index. The cutoffs are sufficient; the subject makes no assertion that they are minimal in every denominator case.

Let

$$
W_{n,K}=\sum_{j=0}^{K-1}\frac{g_{n+j}}{2^{j+1}}.
$$

Equation (R1), applied at $n$ and $m$, gives the full identity

$$
G_n-G_m=W_{n,K}-W_{m,K}
+2^{-K}(G_{n+K}-G_{m+K}). \tag{R4}
$$

The matching-window hypothesis makes the finite contribution exactly zero, including when the windows overlap. Both initial tails lie in $(2/d)\mathbb Z$, so write $G_n-G_m=2z/d$ with $z\in\mathbb Z$. Then

$$
G_{n+K}-G_{m+K}=\frac{2^{K+1}}d z. \tag{R5}
$$

The strict tail bound is exactly $|z|<1$. It forces $z=0$, giving both claimed equalities. There is no estimate hidden in this argument and no loss of a factor of two. A nonzero lattice point at the endpoint would have $|z|=1$; replacing the strict inequality by a weak one is not justified by this proof.

### 3. Modular order and the conditional consequences

Taking fractional parts in (R2) gives $\{G_n\}=\{2^{n-1}S\}$. If $G_n=G_m$, their fractional parts agree, and, in the permitted range,

$$
d\mid a\,2^{n-1-s}(2^{m-n}-1).
$$

The reduced denominator gives $\gcd(a,d)=1$, and oddness gives $\gcd(2,d)=1$. Cancellation modulo $d$ therefore gives $2^{m-n}\equiv1\pmod d$.

For completeness, the order implication does not need an external group-theoretic theorem. Among finitely many residues of powers of the invertible residue $2$, two coincide. Cancelling the smaller power produces a positive exponent with residue $1$. Let $o$ be the least such exponent. Dividing $m-n$ by $o$, a nonzero remainder would be a smaller positive exponent with residue $1$. Thus $o\mid(m-n)$. This works for composite odd $d$ as well as prime $d$. The subject invokes this order only for $d>1$.

Every gap is positive, hence every tail is positive. If $0<x,y<B$, then $|x-y|<B$. This proves the stated individual-tail sufficient condition; it is not a necessary condition. In particular, a small difference alone does not bound either tail individually.

With the rationality and index conditions fixed, the contrapositive of

$$
\bigl((2)\ \text{and}\ |G_{n+K}-G_{m+K}|<B\bigr)
\ \Longrightarrow\ \operatorname{ord}_d(2)\mid(m-n)
$$

is exactly the displayed separation formulation. This is the valid scope of “Equivalently”: the modular implication and that contrapositive are equivalent. Neither a reverse implication from large separation nor equivalence with the two individual-tail bounds follows. The stronger tail-equality conclusion was established separately by (R5).

Finally, suppose the fixed-$d$ pair criterion holds and assume a rational value with that odd denominator part. Its $s$ is a fixed finite integer. Choose a pair with $n\ge\max(s+2,3)$, which the unbounded-smaller-index quantifier allows. The proposition contradicts the stipulated failure of order divisibility. The argument excludes every numerator and every $s$ for that fixed $d$; it does not construct the pairs. For $d=1$, congruence modulo $1$ cannot give a contradiction, although the lattice and equality conclusions still apply.

## Strongest attacks and exact witnesses

### Lattice escape, early indices, and the endpoint

The strongest direct attack on the proposition was to seek a surviving finite contribution or a nonzero lattice difference smaller than the claimed spacing. Equation (R4) exposes every finite term, and (2) cancels all of them. Equation (R3) supplies the claimed spacing at both indices. A counterexample satisfying these hypotheses would then require a nonzero integer $z$ with $|z|<1$. This attack fails for the stated proposition.

The following exact stress tests show why simply dropping a guard from that reasoning would fail. They are explicitly **not prime counterexamples**. For $D\in\{8,16\}$, define an increasing integer sequence $q_1=2$ with gaps $h_1=1$, $h_r=2$ for $r\ge2$ except $h_5=2+D$. Write $T=\sum_{r\ge1}q_r/2^r$ and $U_r=\sum_{j\ge0}h_{r+j}/2^{j+1}$. Direct geometric summation gives

$$
T=\frac72+\frac{D}{32},\qquad
U_r=2+\frac{D}{2^{6-r}}\quad(2\le r\le5),\qquad U_r=2\quad(r\ge6).
$$

All rows below have $d=1$, $K=1$, and equal windows $h_n=h_m=2$, so the stated threshold is $4$.

| Guard being removed | $D$ | $T$ and $s$ | $(n,m)$ | $(U_n,U_m)$ | $(U_{n+1},U_{m+1})$ |
| --- | ---: | --- | --- | --- | --- |
| The floor $n\ge3$ | $16$ | $4$, $s=0$ | $(2,3)$ | $(3,4)$ | $(4,6)$ |
| The floor $n\ge s+2$ | $8$ | $15/4$, $s=2$ | $(3,4)$ | $(3,4)$ | $(4,6)$ |
| Strictness of the bound | $16$ | $4$, $s=0$ | $(3,4)$ | $(4,6)$ | $(6,10)$ |

In the first two rows the later-tail difference is $2<4$, but initial tails differ. In the third it is exactly $4$, and both initial indices meet the original cutoff. Every such sequence has $q_5=9$, so none satisfies the prime convention. These witnesses demonstrate failures of weakened arithmetic arguments, not necessity or optimality claims for the actual primes, and they do not refute the frozen proposition.

The boundary cases $K=1$, $d=1$, $s=0$, composite odd $d$, and overlapping windows introduce no exception to the original derivation. Another attempted overreach is the existence of individually small tails for a short fixed window: at every index at least $2$, all following gaps are at least $2$, so $G_r\ge2$. If $2^K\le d$, the two individual strict bounds cannot hold. This makes that sufficient condition unavailable at those parameters, not the conditional theorem false. The difference bound must not be conflated with it.

### Congruences do not guarantee cancellation, but can allow it

For arbitrary windows, multiply (R4) by $2^K$. The finite contribution is the integer

$$
C_{n,m,K}=\sum_{j=0}^{K-1}
2^{K-1-j}(g_{n+j}-g_{m+j}),
$$

and

$$
2^K(G_n-G_m)=C_{n,m,K}+G_{n+K}-G_{m+K}. \tag{R6}
$$

Congruences modulo a positive integer $q$ imply a divisibility condition on $C_{n,m,K}$, not its vanishing. They also do not imply its nonvanishing. In particular, unequal windows can have the same weighted sum.

A small witness uses actual prime indices $n=4$, $m=10$, $K=2$. The initial primes are

$$
2,3,5,7,11,13,17,19,23,29,31,37.
$$

The windows are $(4,2)$ and $(2,6)$, unequal and componentwise congruent modulo $2$, but

$$
C_{4,10,2}=2(4-2)+(2-6)=0.
$$

The same phenomenon occurs for an odd congruence modulus. Take $n$ to be the index of $359$ and $m$ the index of $521$. The consecutive-prime triples are

$$
(359,367,373),\qquad (521,523,541).
$$

Their windows $(8,6)$ and $(2,18)$ are unequal and componentwise congruent modulo $3$, whereas

$$
C_{n,m,2}=2(8-2)+(6-18)=0.
$$

Here is a direct verification of the prime data, so this witness needs no source or search. The six numbers are indivisible by $2,3,5$. Their remainders for the other possible prime divisors are below; a dash means the divisor exceeds the square root and need not be tested.

| Number | mod $7$ | mod $11$ | mod $13$ | mod $17$ | mod $19$ | mod $23$ |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| $359$ | $2$ | $7$ | $8$ | $2$ | — | — |
| $367$ | $3$ | $4$ | $3$ | $10$ | $6$ | — |
| $373$ | $2$ | $10$ | $9$ | $16$ | $12$ | — |
| $521$ | $3$ | $4$ | $1$ | $11$ | $8$ | — |
| $523$ | $5$ | $6$ | $3$ | $13$ | $10$ | — |
| $541$ | $2$ | $2$ | $8$ | $14$ | $9$ | $12$ |

The intervening odd numbers are composite:

$$
\begin{gathered}
361=19^2,\quad363=3\cdot121,\quad365=5\cdot73,\\
369=3\cdot123,\quad371=7\cdot53,\\
525=3\cdot175,\quad527=17\cdot31,\quad529=23^2,\quad531=3\cdot177,\\
533=13\cdot41,\quad535=5\cdot107,\quad537=3\cdot179,\quad539=7\cdot77.
\end{gathered}
$$

Thus a literal assertion that substituting congruences necessarily introduces a **nonzero** finite contribution is false, even for actual primes and an odd modulus. The correct general limitation is that the contribution is **not guaranteed to vanish**. These witnesses concern that unconditional algebraic assertion only: they do not establish rationality of $S$, the cutoff for its unknown $s$, or any required small-tail bound. They are not counterexamples to the main conditional theorem.

For contrast, an exact non-prime example shows that the uncontrolled contribution can break the proposed argument under congruence modulo the denominator's odd part. Let $h_1=1$, $h_2=2$, $h_3=10$, and thereafter let $h_r=4$ for even $r\ge4$ and $h_r=6$ for odd $r\ge5$. With $q_1=2$ as before, geometric summation gives

$$
T=\frac{29}{6},\qquad U_3=\frac{22}{3},\quad U_4=\frac{14}{3},\quad U_5=\frac{16}{3}.
$$

Take $n=3$, $m=4$, $K=1$, $s=1$, $d=3$. The gaps $10$ and $4$ agree modulo $3$, and the later-tail difference is $2/3<4/3$, but $U_3\ne U_4$ and $\operatorname{ord}_3(2)=2$ does not divide $1$. The finite contribution in (R6) is $6$. This sequence has $q_4=15$ and is not a prime sequence. It shows that the available parity, rationality and recurrence argument cannot replace equality by congruence without another ingredient; it asserts no counterexample for primes under that weaker hypothesis.

### Repetition, residue classes, and the final route criterion

The final paragraph's substantive warning survives: (R6) leaves an infinite-tail difference to control, and a count of matching windows alone specifies no distribution among the index residue classes. No supplied premise imposes the needed tail bound or different classes. This is a limit of the proposed deduction, not a theorem that prime windows can never furnish such information.

The reference to critical-length obstructions was not followed. The only obstruction content assessed is the immediately supplied explanation about exact cancellation and the remaining tail difference; no unseen result is imported by that link. The phrase about arbitrarily large indices is justified for the stated uniform treatment of unknown $s$, not as a necessity claim about every possible method for excluding rational values.

## Premises and dependency findings

The dependency assessment was made from the frozen statement, proof and every consequence sentence on 2026-10-16 UTC. No native L-claim is consumed as an established premise. No live ledger row or pending grade is therefore needed, and none was read. The prime-indexing convention is supplied definitional material. The contextual links identify the problem and a related obstruction discussion; their truth or standing is not used.

There is no imported source-owned theorem. Convergence is established above by elementary binomial-coefficient and prime-factor arithmetic; the series, parity, modular-cancellation and order steps are also rederived above. There is no external-source interface whose proof is silently assumed. The allowed and actual external mathematical source reading is empty.

The unresolved assumptions are precisely the rationality premise, the matching windows and required index range, and the strict tail bound. In the exclusion criterion the unresolved input is the existence of the specified pairs with unbounded smaller index for each chosen $d$. These are hypotheses of the implication, not certified assertions. The order argument does not address $d=1$. No batch acceptance ordering, source-proof reconstruction, formalization, or problem-status conclusion is involved.

## Checklist

### Canonical failure modes

| Item | Applicability and finding |
| --- | --- |
| “Almost all” upgraded to “all” | No such upgrade. The proof covers every triple satisfying the stated hypotheses; pair existence is not asserted. |
| Induction presupposing termination | Inapplicable. The finite split (R1) and ordinary integer division do not require a termination premise. |
| Probabilistic or averaging heuristics used as proofs | Inapplicable. The proof and attacks use exact arithmetic and convergent series. |
| Circular use of an equivalent target | No failure found. Rationality and the tail bound are explicit conditional hypotheses; neither tail equality nor order divisibility is assumed. |
| Exceptional sets dropped from density arguments | Inapplicable. There is no density claim or exceptional-set argument. |
| Finite verification overreach | No failure found. The finite prime witnesses address the nonzero-contribution wording only. No finite list proves pair existence or the infinite conditional. |
| Convergence of a relaxed system substituted for actual objects | No failure found. Actual-prime convergence is proved above. The non-prime stress tests are explicitly confined to weakened arithmetic arguments. |

### Named canonical patterns

| Item | Applicability and finding |
| --- | --- |
| Model-class transport instead of entailment | No classification extension is asserted. The proof uses actual prime properties, and the abstract-sequence witnesses are not transported into prime counterexamples. |
| Uniformity over an infinite family from finite instances | No failure found. The algebra holds for every permitted $n,m,K,d$. Fixed-$d$ pair existence remains a universally quantified hypothesis; the witnesses establish no uniform prime-tail estimate. |
| Extremal claims in their own units | No prime extremum or optimal threshold is claimed. The endpoint is tested in the exact units $2^{K+1}/d$, including the value $4$ in the stress test. Arithmetic tightness is not promoted to prime-specific sharpness. |
| Consequence sentences are claim surfaces | Examined separately. Positivity sufficiency, the modular contrapositive and the fixed-$d$ exclusion follow. Universal nonzeroness in the final warning fails as detailed above. |
| Carry hypotheses used by quantified arguments | No missing hypothesis in the conditional. The integer indices, both cutoffs, exact equality, strict tail bound, and $d>1$ qualification are retained. The exclusion criterion needs unbounded $n$, not just a large endpoint. |
| A composition inherits its unproved premises | No hidden L-claim or source theorem is consumed. Pair existence and tail estimates remain owed for an application; the implication does not discharge them. |
| Reproducibility notes are claims | No executable or success-count claim occurs in the subject. The retained mathematical derivations and witness verification are complete without a runtime dependency. |
| Verifier quotations are claims | Inapplicable to the supplied subject: no prior verdict was supplied or used. Excluded standing or review summaries have not been checked. |
| Verdict words spelled in full | The verdicts below distinguish the main conditional from the literal nonzeroness reading and use full words. No grade or tier is asserted. |
| Certified-bracket functions fail loudly | Inapplicable. No numerical enclosure or iteration cap is used. |
| A check with no failing input is decoration | No executable check is offered. The attacks have explicit failure surfaces: removed cutoffs, a weak endpoint inequality, and a required nonzero contribution contradicted by zero. |
| A gate reading caches instead of rerunning is defective | Inapplicable. No gate or cached output is used as mathematical evidence. |

### Erdos-specific checklist

| Item | Applicability and finding |
| --- | --- |
| Quantifiers and scope | The original conditional's full index and denominator ranges survive. The fixed-$d$ criterion requires pairs beyond every cutoff in the smaller index. The final “nonzero” wording cannot have a universal reading. |
| Circularity | No failure found. The target equalities and order conclusion are deduced, not assumed. Rationality is an exposed antecedent. |
| Model and convention changes | The prime indexing starts at $2$ and is used in $G_1=S-2$. Abstract sequences appear only as explicitly limited stress tests. |
| Finite and statistical overreach | No statistical evidence or finite-to-infinite extrapolation is used. The congruence witnesses refute only a universal finite-contribution assertion. |
| Uniformity | Series operations are justified by actual convergence. No exchange of an uncontrolled parameter limit with a sum occurs. No uniform tail estimate is claimed. |
| Extremal conclusions | No unattested prime infimum, supremum or attainment claim is present. The lattice endpoint is checked exactly, without claiming prime-specific sharpness. |
| Consequences and composition | The positive-tail sufficient condition, modular contrapositive and fixed-$d$ implication are valid at their stated strength. The last warning needs “potentially nonzero,” as witnessed. |
| Computation | No executable or approximate computation is used. Exact formulas and all finite witness arithmetic are exposed above. The prime witnesses satisfy only the properties expressly attributed to them. |
| Reproduction | All derivations can be rebuilt from the retained extraction and this report. No cached result or inaccessible runtime input is required. |
| Source and verdict fidelity | Source identity rests on the commissioned extraction, with the provenance limit stated above. No unseen obstruction theorem, outside announcement, prior verdict or standing is invoked. |

The related discipline concerning correlated statistical samples is inapplicable. Evidence coverage is confined to the arguments and witnesses stated here; no claim is made about omitted subject text, current pages, or Problem 251 as a whole.

## Verdict and grading

**The conditional matching-window proposition, identities (1)–(4), and the precise numerical and fixed-denominator consequences: refutation-failed.** The proof survives the attacks on convergence, indexing, parity, cancellation, the strict threshold, modular order, and quantifier composition. No counterexample satisfying its full prime, rationality, index, matching-window and tail hypotheses has been established, and no load-bearing inference remains unsupported in the derivation above.

**The final sentence, if read as asserting that congruence necessarily makes the finite-window contribution nonzero: refuted-as-stated.** The actual-prime windows above have zero contribution despite being unequal and congruent, including modulo an odd integer. The sound warning is loss of guaranteed cancellation, not guaranteed nonzeroness. This localized wording finding is not a disproof of the main conditional proposition and does not show that its proof is defective. A reading of the sentence as merely warning of a potentially nonzero term survives; this report does not endorse its literal universal strengthening.

No conclusion here supplies the missing prime-window construction, resolves the case $d=1$, or solves Problem 251. The report covers only the supplied frozen mathematical text. The provenance limitation and the distinction between the two readings of the final warning remain explicit for the separate grader. This reviewer supplies no grade or tier.

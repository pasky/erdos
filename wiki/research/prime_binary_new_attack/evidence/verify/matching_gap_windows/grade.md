---
name: research/prime_binary_new_attack/evidence/verify/matching_gap_windows/grade
title: Grade of the matching-prime-gap-window review
desc: "Independent grade of the matching-prime-gap-window review, including its conditional scope and localized wording refutation."
created: 2026-10-16T16:08:36Z
updated: 2026-10-16T16:08:36Z
---

# Grade of the matching-prime-gap-window review

## Decision and assessed subject

**The review passes the report and independence contracts for the supplied mathematical surfaces, with the separate verdicts below.** The matching-window conditional and its qualified consequences are **refutation-failed**. The final assertion of a necessarily nonzero finite-window contribution is **refuted-as-stated** on that literal, unconditional reading. The latter finding does not defeat the matching-window proof. No existence theorem for the required prime windows, result for every denominator, or solution of Problem 251 is accepted.

**Mathematical subject:** `wiki/research/prime_binary_new_attack/matching_gap_windows.md`, its entire supplied mathematical body, and the prime-indexing convention from the Statement of `wiki/problems/irrationality/E0251/_index.md`, frozen on 2026-10-16 UTC. The controlling assessed text is [the subject snapshot](../../assets/matching_gap_windows/subject.md), including its two uniform omission markers and notation preface. References to snapshot lines below refer to that unchanged 102-line extraction, not to the current source page. Project mathematics is credited to Plasma AI.

**Review assessed:** `wiki/research/prime_binary_new_attack/evidence/verify/matching_gap_windows/review.md`, completed on 2026-10-16 at 13:56:05.917 UTC, as preserved in [the unchanged submitted review](../../assets/matching_gap_windows/review.md). This grade was examined and written on 2026-10-16 UTC. The preserved subject and submitted report distinguish the assessed text from any same-day or later edits to their public homes.

**Grader:** a fresh-context independent grader, distinct from both the author and the reviewer, with no earlier role in constructing, collaborating on, or reviewing this subject. The disclosed reviewer and grader model configurations were both gpt-6-astra. Eligibility rests on their separate contexts and actual input boundaries. This is a grade of the submitted review, not a countersign, a second independent review cycle, or a grade of the grader's own new claim.

The accepted warrant is mathematical. The subject, submitted review and the derivations below contain all inputs needed to reproduce it. No executable mathematical check, numerical search, cached result, theorem-prover output or repository gate supports this grade. Finite arithmetic is checked directly below; it does not require an artificial executable.

## Independence, assignment and provenance

The grading inputs were the unchanged subject and complete report; the complete as-launched reviewer commission and its three step contracts; the screened reviewer reading and isolation account; and separately labeled custody evidence containing exact-copy facts, effective-configuration comparisons, subscription records, the primary provenance request and its delivery boundary, and post-input changed paths. All eight supplied inputs were read in full. The commission and reproduced instructions were assessed as assignment evidence, without treating their examples or links as further read authority.

The grading operating reading comprised the supplied instructions; `AGENTS.md`; `README.md`; Claims, Evidence, Tiers, Naming and Project claims in `docs/anatomy.md`; `docs/verification.md` and the verification adapter in full; the campaign guidance, the Reading rule, and Prepare the review extraction; the relevant statement-scope, source-fidelity, mathematical-review and local-evidence rules in `docs/evidence.md`; and permitted operating identity, skill, configuration and command documentation. Operating identities were checked against the commissioned sources. Neither the reviewer nor the grader used the original corpus pages, the linked obstruction page, author working notes, sibling mathematical material, a dependency ledger, external mathematical sources or the web. The grader did not read the excluded administrative packet check or any gate output.

The as-launched assignment explicitly charged the reviewer to find a counterexample, unsupported essential inference or canonical failure mode, covered the entire supplied body and its consequences, required the full neutral contract and both checklists, and withheld grading authority from the reviewer. The report actually follows that charge: it exposes the complete finite contribution, tests the index and strictness guards, checks convergence for primes, and finds a concrete defect in the final sentence. Its positive verdict does not rest on agreement with an author's output.

The reviewer was assigned a fresh, isolated context and reports no authorship, collaboration or prior subject context. The primary effective-configuration records support the stated closed communication and read boundaries; the only recorded agent-configuration change was a project-trust entry, not an instruction override. Empty subscription records and the absence of synchronization support isolation but do not alone establish what was read. The actual reading account, unchanged keeper, communication evidence and absence of conflicting mathematical exposure supply the additional basis for accepting independence. The grader likewise checked an empty subscription table and kept incoming communication closed.

The following limitations require separate rulings.

- **Extraction labeling — sufficient subject identity.** The extraction lacks its own revision label and a heading naming the main source page. The reviewer disclosed this and did not claim to have compared it to excluded originals. The actual commission explicitly binds the extraction to the named paths and freeze date. Separate custody evidence identifies the source body, two administrative cuts and notation preface, and records exact equality of the delivered extraction, frozen prepared copy and retained keeper. The grader also compared its keeper to the supplied extraction byte for byte. Together these identify the assessed subject sufficiently under the snapshot rule. An internal label would be redundant identity metadata here, not a missing mathematical hypothesis. This ruling accepts the supplied custody binding; it is not an independent audit of omitted source material or a claim that the grader opened the originals.
- **Provenance communication — no mathematical steering.** The primary outgoing request asks only for a content-free binding record and expressly excludes mathematical steering or an earlier verdict. The supplied primary listing and delivery account show that no parent reply was sent or delivered. The additional binding was recorded in custody evidence and was never added to the reviewer's input. It can resolve the grader's identity question without having influenced the reviewer's reasoning. No missing reply or unseen clarification is used as a premise.
- **Changed paths and path spelling — no substantive scope breach.** The complete supplied post-input changed-path list contains only the reviewer's continuation, subject keeper and report. Those changes are within its authorized private delivery; the automatic continuation commit adds no broader mathematical work. The disclosed use of an absolute spelling for one write reached the correct authorized report and was checked immediately. That spelling violated an operating form rule, but changed neither the subject nor the input boundary. It has no mathematical or independence materiality.
- **General motivational material — no subject premise.** The assignment's motivational announcements supplied no matching-window proof step, relevant theorem or earlier verdict on this subject. None is consumed in the report or grade. Their presence did not determine an attack direction or weaken the refutation charge, and gives no warrant for the announcements themselves.
- **Grader's administrative filename exposure — immaterial.** During initial operating identification, before reading the mathematical packet, the grader listed administrative filenames more broadly than necessary. No file contents, mathematical claims, reports, verdicts or private conversations were displayed. The event was disclosed through the permitted outbound channel and the enumeration was not repeated. Under the neutral content test, it supplied no fact that could explain a mathematical finding, no attack guidance and no reason to relax the charge. It does not contaminate this grade. The record does not claim that no wider filename enumeration occurred.

The reviewer and grader remained separated from the construction of the subject. No unresolved material exposure is established by this packet. Raw configuration, message and operating records remain private; their necessary independence facts and the rulings above are retained here. The absence of raw public logs is not a reproducibility defect for this noncomputational examination.

## Restatement and surface decisions

Let $p_n$ be the $n$th prime, with $p_1=2$, and for positive integer $n$ put

$$
S=\sum_{n\ge1}\frac{p_n}{2^n},\qquad
 g_n=p_{n+1}-p_n,\qquad
 G_n=\sum_{j\ge0}\frac{g_{n+j}}{2^{j+1}}.
$$

The series converge and the tails are positive. Suppose $S=a/(2^s d)$ is reduced, with integer $a$, nonnegative integer $s$, and positive odd integer $d$. For every integer $m>n\ge\max(s+2,3)$ and integer $K\ge1$, write $B=2^{K+1}/d$. If the two length-$K$ gap windows agree entry by entry and the absolute difference of their endpoint tails is less than $B$, both the initial tails and the endpoint tails are equal. For $d>1$ this also forces $\operatorname{ord}_d(2)\mid(m-n)$.

Both individual endpoint tails being less than $B$ is a stronger sufficient hypothesis for the difference bound. With the same rationality, index and matching assumptions and $d>1$, failure of order divisibility forces an endpoint difference at least $B$.

For any fixed odd $d>1$, the exclusion criterion asks for such matching pairs beyond every cutoff in the smaller index $n$, with the required small-tail hypothesis and with nondivisible displacement. The window length may depend on the pair and on $d$. If these pairs exist, no reduced rational value of $S$ has odd denominator part $d$. This assumes the pairs; it does not supply them. Individual small-tail bounds give the stated sufficient form, and the original strict difference bound also suffices directly by the conditional theorem.

In the following table, **pass** grades the report's treatment of a surface, not the truth of every sentence on the page. In particular, a correctly substantiated negative verdict passes. All listed positive verdicts retain the hypotheses just stated.

| Assessed surface and snapshot location | Grade | Mathematical verdict and exact scope |
| --- | --- | --- |
| Prime convention, well-defined series and convergence, lines 1–3 and 17–23 | **pass** | **refutation-failed**. The report proves sufficient growth control for the actual primes and justifies each series operation. |
| $S=2+G_1$ and $G_{n+1}=2G_n-g_n$, line 23 | **pass** | **refutation-failed** for every positive integer index. The first prime and all coefficients are accounted for. |
| $dG_n$ integral for $n\ge s+1$, lines 24–25 | **pass** | **refutation-failed** under reduced rationality and the stated integer convention. |
| The even lattice (1), lines 25–34 | **pass** | **refutation-failed** for $n\ge\max(s+2,3)$. These are sufficient cutoffs; no prime-specific minimality assertion is accepted. |
| Exact cancellation and both tail equalities, lines 38–52 and 59–67 | **pass** | **refutation-failed** under the exact matching and strict bound. Overlap, $K=1$ and $d=1$ cause no exception. |
| Fractional-part identity and multiplicative-order conclusion (4), lines 52–75 | **pass** | **refutation-failed**, with $d>1$ for the order conclusion. Composite odd denominators are included. |
| Tail positivity and the two individual-tail sufficient bounds, lines 77–78 | **pass** | **refutation-failed**. Sufficiency is accepted; necessity or equivalence to the difference bound is not asserted. |
| The separation formulation, lines 78–83 | **pass** | **refutation-failed** with all inherited assumptions. “Equivalently” is valid as contraposition of the order implication, not as an equivalence with individual-tail sufficiency or the stronger tail-equality conclusion. |
| Fixed-$d$ rational-denominator exclusion, lines 87–91 | **pass** | **refutation-failed** as a conditional implication. The smaller index must be unbounded in the stated criterion. No pair construction or simultaneous result for all $d$ is accepted. |
| Unknown preperiod and the separate $d=1$ obligation, lines 89–92 | **pass** | **refutation-failed** at the stated route scope. An unbounded smaller index handles every unknown finite $s$; congruence modulo $1$ supplies no contradiction. This is not a necessity theorem about every conceivable irrationality argument. |
| No supplied pair theorem; repetition and counting alone leave obligations, lines 94–97 | **pass** | **refutation-failed** as a description of what this argument supplies. No theorem that prime-window methods can never work is asserted or accepted. |
| Explicit obstruction explanation, lines 98–100 | **pass** | **refutation-failed** for the stated fact that cancellation leaves an infinite-tail difference requiring a bound. No additional result behind the contextual link is within this grade. |
| Congruence is weaker than equality and loses guaranteed cancellation, lines 100–102 | **pass** | **refutation-failed** for this algebraic warning. The finite contribution is not guaranteed to vanish; this is not a disproof of every possible prime-specific congruence argument. |
| Necessarily nonzero finite contribution, literal reading of lines 101–102 | **pass** | **refuted-as-stated** as an unconditional assertion. Unequal congruent actual-prime windows have zero contribution. This does not refute a rationality-conditioned prime theorem or the main matching-window proposition. |

No supplied positive surface has the verdict **proof defective; statement unresolved**: its relevant deductions are complete. That verdict would be appropriate for an unsupported inference without a disproof, and must not replace the localized, witnessed nonzeroness refutation or be applied to the surviving conditional. Broader claims behind contextual links, actual pair existence and a solution of Problem 251 are outside the accepted surfaces; no pass or tier is silently extended to them.

## Independent examination of the weakest steps

### 1. Convergence, exact indexing and the rational lattice

A possible hidden premise was an unprovided theorem on prime growth. The report removes that dependence. To check its argument, take $C_N=\binom{2N}{N}$. It is the largest of $2N+1$ nonnegative binomial coefficients with sum $4^N$, so $C_N\ge4^N/(2N+1)$. For each prime $q$, its factorial valuation is

$$
v_q(C_N)=\sum_{r\ge1}\left(
\left\lfloor\frac{2N}{q^r}\right\rfloor
-2\left\lfloor\frac{N}{q^r}\right\rfloor\right).
$$

Each summand is either zero or one and vanishes beyond $q^r\le2N$. Thus $v_q(C_N)\le\lfloor\log_q(2N)\rfloor$ and $q^{v_q(C_N)}\le2N$. All prime factors are at most $2N$, yielding

$$
\pi(2N)\log(2N)\ge2N\log2-\log(2N+1).
$$

At $N=t^2$ the right side divided by $t\log(2t^2)$ tends to infinity, so $\pi(2t^2)\ge t$ eventually. This establishes arbitrarily many primes and $p_t\le2t^2$ eventually, without assuming a distribution theorem. It follows that $p_t=O(t^2)$ and $g_t=O((t+1)^2)$. Polynomially weighted geometric series converge, including each fixed-index gap tail. No uniform estimate in a varying window parameter is extracted from this fact.

There are two independent ways to locate the potentially dangerous factor of two. Splitting a tail after $K$ entries gives

$$
G_r=\sum_{j=0}^{K-1}\frac{g_{r+j}}{2^{j+1}}+2^{-K}G_{r+K}. \tag{G1}
$$

Direct summation of the prime differences gives

$$
G_r=2^{r-1}S-A_r,\qquad
A_r=p_r+\sum_{i=1}^{r-1}2^{r-1-i}p_i. \tag{G2}
$$

For example, the finite difference sum through $g_{r+J}$ is

$$
-\frac{p_r}{2}+\sum_{j=1}^{J}\frac{p_{r+j}}{2^{j+1}}
+\frac{p_{r+J+1}}{2^{J+1}},
$$

and its last term tends to zero by the growth bound. This verifies (G2) without assuming the recurrence's indexing. In particular $A_1=2$, so $G_1=S-2$, and the $K=1$ case of (G1) gives the recurrence.

Iteration of that recurrence also expresses $G_r$ as $2^{r-1}(S-2)$ minus an integer. Hence $dG_r$ is integral once $r\ge s+1$. For $r\ge\max(s+2,3)$, its predecessor has an integral $dG_{r-1}$ and an even gap $g_{r-1}$, so

$$
dG_r=2dG_{r-1}-dg_{r-1}\in2\mathbb Z.
$$

The report's direct parity check agrees: $A_2=5$, while for $r\ge3$ the two odd primes $p_r+p_{r-1}$ give an even sum and all earlier terms of $A_r$ have even coefficients. Under rationality, (G2) becomes $dG_r=2^{r-1-s}a-dA_r$. Both sufficient cutoffs are thus justified. The exceptional first gap has not been treated as even.

### 2. Exact cancellation, strict separation and modular order

To try to break the matching argument, retain every finite term before cancelling. Define

$$
C_{n,m,K}=\sum_{j=0}^{K-1}2^{K-1-j}(g_{n+j}-g_{m+j}).
$$

Equation (G1) gives the exact identity

$$
2^K(G_n-G_m)=C_{n,m,K}+G_{n+K}-G_{m+K}. \tag{G3}
$$

Matching windows make $C_{n,m,K}=0$, even when the windows overlap. The rational lattice gives $G_n-G_m=2z/d$ for an integer $z$, so

$$
G_{n+K}-G_{m+K}=\frac{2^{K+1}}d z=Bz. \tag{G4}
$$

A counterexample to the asserted equality, under all its hypotheses, would require a nonzero integer $z$ of absolute value less than one. This attack fails by an exact contradiction. It checks the claimed threshold in its own units and also proves the second tail equality. A weak bound would leave $z=\pm1$ available to this arithmetic argument; no claim that those endpoint cases occur for primes is needed.

By (G2), equality of the initial tails makes $2^{m-1}S-2^{n-1}S$ integral. In the permitted range this yields

$$
d\mid a\,2^{n-1-s}(2^{m-n}-1).
$$

The reduced numerator and oddness of $d$ make both cancelled factors units modulo $d$. Therefore $2^{m-n}\equiv1\pmod d$. A positive order exists because two powers of the invertible residue $2$ coincide in the finite residue set. Division of $m-n$ by its least positive order leaves a remainder whose power is also $1$; minimality forces remainder zero. This verifies the order conclusion for arbitrary odd $d>1$, not merely prime $d$.

The separation consequence can be checked directly as well as by contraposition: if order divisibility fails, initial tails cannot be equal. Then $z\ne0$ in (G4), so the endpoint difference has absolute value at least $B$. There is no converse asserting tail equality from order divisibility, and no equivalence between small difference and individually small tails.

### 3. Quantified application and the finite-contribution warning

For positive $x,y<B$, one has $\lvert x-y\rvert<B$. Since each gap is positive, this applies to the two tails. At indices at least two, all gaps are at least two, and their geometric weights sum to one; thus $G_r\ge2$. The report correctly observes that the two individual strict bounds cannot hold when $2^K\le d$. This is a restriction on that sufficient antecedent, not an obstruction to the difference bound or a counterexample to the conditional theorem.

Fix odd $d>1$ and assume the pair criterion. Under any hypothesized rational value with that odd denominator part, $s$ is a fixed finite integer. Taking a pair beyond $\max(s+2,3)$ puts it within the theorem and contradicts its required nondivisible displacement. The proof needs no uniform bound on $s$, $K$ or the individual primes. It does need the smaller index $n$ beyond each cutoff. A large $m$ with bounded $n$ would not discharge this criterion. No argument here constructs the pairs or removes the separate dyadic-denominator obligation.

For congruent windows modulo a positive integer $q$, (G3) supplies $q\mid C_{n,m,K}$, not $C_{n,m,K}=0$ or $C_{n,m,K}\ne0$. The actual-prime witnesses below distinguish these possibilities. This exposes the exact defect in the literal final sentence while preserving the useful warning about loss of guaranteed cancellation.

The repetition and counting warnings likewise concern information supplied by this argument. A sufficiently large occurrence count in a specified finite index range could exceed the capacity of a single residue class. No such quantitative premise is supplied here. The accepted warning is therefore a missing inference in this route, not a universal prohibition on counting arguments.

## Strongest attacks and verification of the witnesses

The report's strongest attack on the core concerns whether an uncancelled finite term, wrong cutoff, or missing factor of two permits a nonzero tail difference below the threshold. Equations (G1)–(G4) rule this out for the frozen hypotheses. Its strongest successful attack concerns the final consequence sentence: unequal congruent prime windows can have equal weighted sums. Both attacks address the actual assertion; neither is just another agreement check.

### Actual-prime zero-contribution witnesses

The initial prime list in the report is correct: $2,3,5,7,11,13,17,19,23,29,31,37$. For the odd candidates up to $37$, trial division by the primes at most their square roots, namely $2,3,5$, suffices. The omitted odd composites in this range are $9,15,21,25,27,33,35$, each visibly divisible by $3$ or $5$; all intervening even numbers greater than two are composite. This verifies both prime identities and consecutive indexing.

Consequently $n=4$, $m=10$, $K=2$ give gap windows $(4,2)$ and $(2,6)$, unequal but componentwise congruent modulo two. Their weighted contributions agree:

$$
C_{4,10,2}=2(4-2)+(2-6)=0.
$$

Conversely, the same verified data give the one-entry windows $g_4=4$ and $g_5=2$, congruent modulo two with contribution $C_{4,5,1}=2$. Thus congruence guarantees neither vanishing nor nonvanishing even on actual prime windows. Algebraically, the length-two form $2x+y$ has the nontrivial kernel $(t,-2t)$, which can consist of multiples of a prescribed modulus. These observations concern automatic finite-window cancellation only, without any rationality or small-tail assertion.

The odd-modulus example is also exact. The triples $(359,367,373)$ and $(521,523,541)$ are consecutive-prime triples. The six numbers are odd, have digit sums respectively $17,16,13,8,10,10$, and do not end in $0$ or $5$. The following quotient-and-remainder pairs independently check every remaining relevant trial divisor. Each entry $(u,v)$ means the number equals the column prime times $u$, plus $v$; a dash marks a divisor above the square root.

| Number | $7$ | $11$ | $13$ | $17$ | $19$ | $23$ |
| ---: | --- | --- | --- | --- | --- | --- |
| $359$ | $(51,2)$ | $(32,7)$ | $(27,8)$ | $(21,2)$ | — | — |
| $367$ | $(52,3)$ | $(33,4)$ | $(28,3)$ | $(21,10)$ | $(19,6)$ | — |
| $373$ | $(53,2)$ | $(33,10)$ | $(28,9)$ | $(21,16)$ | $(19,12)$ | — |
| $521$ | $(74,3)$ | $(47,4)$ | $(40,1)$ | $(30,11)$ | $(27,8)$ | — |
| $523$ | $(74,5)$ | $(47,6)$ | $(40,3)$ | $(30,13)$ | $(27,10)$ | — |
| $541$ | $(77,2)$ | $(49,2)$ | $(41,8)$ | $(31,14)$ | $(28,9)$ | $(23,12)$ |

The cutoff list is exhaustive: $359<19^2$, each of $367,373,521,523$ is less than $23^2$, and $541<29^2$. The only prime divisors requiring testing are therefore exactly those covered by the table and $2,3,5$. Every displayed remainder is nonzero.

For consecutive primality, the intervening odd integers are accounted for by

$$
\begin{gathered}
361=19^2,\quad363=3\cdot121,\quad365=5\cdot73,\quad
369=3\cdot123,\quad371=7\cdot53,\\
525=3\cdot175,\quad527=17\cdot31,\quad529=23^2,\quad531=3\cdot177,\\
533=13\cdot41,\quad535=5\cdot107,\quad537=3\cdot179,\quad539=7\cdot77.
\end{gathered}
$$

Every other intervening integer is even; between $521$ and $523$ only $522$ occurs. Thus the two gap windows are $(8,6)$ and $(2,18)$. They are unequal and componentwise congruent modulo three, but

$$
2(8-2)+(6-18)=0.
$$

Both witnesses use the actual prime sequence and refute universal nonzeroness of the finite contribution. They do not establish rationality of $S$, an unknown preperiod bound, or a small-tail condition. If the final sentence were instead proposed as a theorem under all those additional hypotheses, these finite witnesses alone would not disprove it. That stronger conditional disproof is not the report's verdict and is not accepted here.

### Guard stress tests have only their stated force

For the first family of non-prime tests, let $q_1=2$, $h_1=1$, and $h_r=2$ for $r\ge2$ except $h_5=2+D$, where $D$ is $8$ or $16$. Define $q_{r+1}=q_r+h_r$, and let $T$ and $U_r$ be its analogues of $S$ and $G_r$. Direct summation gives

$$
U_1=\frac32+\frac{D}{32},\qquad
T=\frac72+\frac{D}{32},\qquad
U_r=2+\frac{D}{2^{6-r}}\quad(2\le r\le5),\qquad U_r=2\quad(r\ge6).
$$

For $D=16$, $(U_2,U_3,U_4,U_5)=(3,4,6,10)$ and $T=4$. For $D=8$, $(U_3,U_4,U_5)=(3,4,6)$ and $T=15/4$. These values reproduce each report row: dropping the index-three floor or the $s+2$ floor permits a later difference $2<4$ with unequal initial tails, while weakening the strict inequality permits a later difference $4$ with unequal initial tails at otherwise permitted indices. The windows in each row are the single gap $2$. Since $q_5=9$, none is a prime counterexample. The report claims only failures of weakened arithmetic arguments, and that limited claim is accepted. No necessity or optimality theorem for primes follows from these tests.

For the second non-prime example, the eventual gaps alternate $4,6$, starting at index four. Their tails solve

$$
U_4=2+\frac12U_5,\qquad U_5=3+\frac12U_4,
$$

so $U_4=14/3$ and $U_5=16/3$. Prepending gaps $10,2,1$ gives $U_3=22/3$, $U_2=14/3$, $U_1=17/6$, hence $T=29/6$. At $n=3,m=4,K=1,s=1,d=3$, the gaps $10$ and $4$ agree modulo three and the later difference is $2/3<4/3$. Yet the initial difference is $8/3$, the finite contribution is $6$, and order two does not divide displacement one. Equation (G3) checks numerically as $2(8/3)=6-2/3$. This sequence has $q_4=15$. It refutes the equality-to-congruence substitution within the available arithmetic framework, while leaving any stronger prime-specific theorem unassessed. The report preserves that distinction.

These reconstructions verify all retained witness arithmetic needed for the grade. No optional stress test is counted as a disproof of a statement it does not satisfy.

## Premises and report-contract findings

The dependency inventory was derived from the entire subject, including its consequence sentences, and checked on 2026-10-16 UTC. It contains no native L-claim used as an established premise. No live ledger reading or pending native grade is needed, and none was obtained. Prime indexing is supplied definitional material; the convergence proof makes the infinite sequence and sums meaningful without relying on an unproved local assertion.

No source-owned theorem is imported. Elementary prime factorization, factorial valuation, geometric-series arithmetic, parity, modular cancellation and the finite-residue order argument are either derived in the report or ordinary elementary arithmetic used transparently. There is no unread literature interface being represented as checked. The external mathematical reading set and its actual reading depth are empty.

Rationality, reduced denominator form, the index range, exact window equality, and the strict bound are exposed hypotheses. The fixed-$d$ pair-existence assertion is likewise an unresolved antecedent. The problem link identifies the intended application. The obstruction link supplies no unseen premise: only the explicit tail-difference explanation is assessed. Any attempt to cite an additional result from that page would need its own exact statement and warrant.

For the compound argument, the verification order is acyclic: convergence and identities, then integrality and parity, then matching-tail equality, then order, then separation and denominator exclusion. The congruence warning is checked from the full finite-window identity independently of rationality. These are deductions inside one supplied argument, not an omitted batch of native premise rows. The report's shared sections unambiguously cover each surface; their adequacy is assessed as follows.

| Contract requirement | Grade of the delivered report |
| --- | --- |
| Subject and conventions | **pass**. The opening names the paths, freeze date, prime convention, complete supplied scope and exact snapshot. The labeling limitation is resolved as above, without claiming excluded source-fidelity coverage. |
| Independence and actual reading | **pass**. Role eligibility, allowed and actual reads, unchanged extraction, communication boundary and exposure account are stated and supported by the primary packet evidence. |
| Restatement, part (a) | **pass** for every table surface. The report retains integer domains, both cutoffs, strictness, odd denominator and $d>1$ qualification, unbounded smaller index, unresolved existence, and the two readings of the final warning. |
| Checklist, part (b) | **pass**. Every canonical mode, named pattern and Erdos-specific item has an explicit verdict; the substantive adequacy is checked item by item below. |
| Weakest steps, part (c) | **pass**. Three grouped derivations cover prime convergence and identities, the lattice/cancellation threshold, and modular order with its consequences. The final warning's finite contribution is separately derived in the attack section. |
| Strongest attack, part (d) | **pass**. The lattice escape attack addresses a real failure mode; guard and endpoint witnesses show its guards have content. Actual-prime congruence witnesses establish the precise negative finding. Non-prime tests keep their limited force. |
| Dependencies, part (e) | **pass**. The stated empty native-premise set agrees with the subject. Explicit antecedents are not treated as certified facts; no unexamined theorem or circular promotion is consumed. |
| Verdict and grading | **pass**. The report distinguishes the surviving conditional, the literal wording refutation, the surviving weaker warning and the unresolved application. It makes no grade or tier assertion of its own. This separate grade supplies the accepted judgment. |
| Retained evidence and reproduction | **pass**, subject to durable adoption. The exact subject and full derivations/witnesses suffice; the reconstruction above checks the report's arithmetic and coverage claims. No executable or cached result is missing. |
| Computational batch and second-cycle requirements | Inapplicable. The review is noncomputational and this assignment is grading, not a second-cycle reliability claim. No structurally disjoint implementation or prior-cycle attack packet is required. |

## Checklist grading

The following findings apply to each surface in the decision table. The localized nonzeroness failure is identified wherever it matters; inapplicability elsewhere is not used to erase it.

### Canonical failure modes

| Required mode | Grade and substantive finding |
| --- | --- |
| Almost all upgraded to all | **pass**. All triples satisfying the explicit hypotheses are covered algebraically. The report does not infer pair existence or discard exceptional indices. |
| Induction presupposing termination | **pass; inapplicable**. Finite tail splitting and least-positive-order division do not assume the result or a stopping event. |
| Probabilistic or averaging heuristics presented as proofs | **pass; inapplicable**. No probabilistic evidence supports any accepted surface. The binomial maximum bound is an exact finite inequality. |
| Circular use of an equivalent statement | **pass**. Rationality is a stated antecedent; equality and order divisibility are deduced. The exclusion criterion does not assume irrationality. |
| Exceptional sets dropped from density arguments | **pass; inapplicable**. No density argument occurs; both index cutoffs remain explicit. |
| Finite verification cited beyond base-case coverage | **pass**. Finite prime witnesses disprove a universal finite-contribution assertion. The infinite positive results have full algebraic proofs, not extrapolation from examples. |
| Relaxed-system convergence substituted for actual objects | **pass**. Prime convergence is proved for the actual sequence. Abstract sequences are used only to test the stated arithmetic proof guards. |

### Named canonical patterns

| Required pattern | Grade and substantive finding |
| --- | --- |
| Model-class transport instead of entailment | **pass; no classification extension is asserted**. Non-prime examples are not transported into prime counterexamples. The congruence warning is checked through the exact identity. |
| Uniformity over an infinite family from finite instances | **pass**. No sampled family establishes a uniform bound. Each $n,m,K,d$ is treated by the same exact deduction under its hypotheses; no uniform small-tail estimate is asserted. |
| Extremal claims in their own units | **pass**. The nonzero lattice spacing and endpoint are checked as $B=2^{K+1}/d$. No prime-specific sharpness, infimum, supremum or attainment theorem is claimed. |
| Consequence sentences are claim surfaces | **pass**. Positivity sufficiency, separation, fixed-$d$ exclusion, route limits and both readings of the final warning receive separate decisions. The literal nonzeroness reading is **refuted-as-stated**. |
| Carry hypotheses actually used by quantified arguments | **pass**. Integer indices, parity range, unknown preperiod, exact matching, strictness and oddness all survive the restatement. Unbounded smaller index is not replaced by a large endpoint. |
| A composition inherits its unproved premises | **pass**. Pair existence and tail control remain open antecedents for an application. No source or local claim is cited for a clause it does not supply. |
| Reproducibility notes are claims | **pass**. The report's noncomputational reproduction claim is supported by the exact algebra, witness data, complete divisor ranges and composite witnesses. It claims no executable pass count. |
| Verifier quotations are claims | **pass** for this grade's characterization of the supplied report. Its actual positive and negative verdicts, limits and absence of a self-awarded tier agree with the account here. Prior-review summaries and excluded standing text were not part of the review's subject and receive no coverage. |
| Verdict words spelled in full | **pass**. The report and this grade distinguish **refutation-failed**, **refuted-as-stated**, and **proof defective; statement unresolved** without an ambiguous shared abbreviation. |
| Certified-bracket functions fail loudly | **pass; inapplicable**. No enclosure routine, iteration cap or numerical certification is used. |
| A harness leg with no failing input is decoration | **pass; no executable leg is offered**. The mathematical attacks have real failure conditions: nonzero integer below one, guard removals and a claimed nonzero weighted sum equal to zero. The exhibited tests are not tautologies. |
| A gate reading caches instead of rerunning is defective | **pass; inapplicable**. No gate, cached output or success log carries a mathematical verdict. |

### Erdos-specific checklist

| Required item | Grade and substantive finding |
| --- | --- |
| Quantifiers and scope | **pass**. The decision table records every domain and inherited qualification. The only literal universal wording failure is isolated with its witness. |
| Circularity | **pass**. The conditional assumes rationality, not the desired equality or contradiction. The deduction order is acyclic. |
| Model and convention changes | **pass**. The initial prime $2$, the first gap and positive-index convention are used correctly. All artificial sequences are explicitly labeled. |
| Finite and statistical overreach | **pass**. No statistics or finite-to-infinite inference supports the positive theorem. Exact finite counterexamples serve only their stated negative assertion. |
| Uniformity | **pass**. Convergent series are split at fixed finite indices. No uncontrolled interchange of limits or uniform bound on the desired pairs is taken. |
| Extremal conclusions | **pass**. Threshold arithmetic is exact and no prime optimality claim is inferred from the abstract endpoint example. |
| Consequences and composition | **pass**. Each consequence is separately checked, and the missing existence bridge remains missing. The final nonzeroness sentence cannot be accepted literally. |
| Computation | **pass** at noncomputational scope. All finite arithmetic, divisor cutoffs, intervening composites and geometric tails used by the verdict are reconstructible and checked above. No floating-point or uncertified enclosure is involved. |
| Reproduction | **pass**, conditional on the named snapshots and report reaching durable homes. There is no source-code omission because no executable mathematical check was invoked. |
| Source and verdict fidelity | **pass** with the stated snapshot scope. The source attribution rests on explicit commissioned custody; no excluded original or linked theorem is claimed to have been inspected. The report's verdicts are represented at their actual strength. |

Correlated-sample inference is inapplicable. The evidence-coverage discipline is satisfied by retaining the precise derivations and limiting each witness to the property it verifies. The complete checklists reveal no additional missing mandatory warrant.

## Warrant, exact correction and adoption conditions

As the eligible separate grader, I accept the review and assert **tier-1 warrant for the positive mathematical surfaces in the decision table**, at exactly their stated conditional scope, once the durable-custody conditions below are met. The local warning about obligations is accepted at its explicit argument scope, not as a new impossibility theorem. This is no blanket positive verdict on the literal full body: its final necessary-nonzeroness assertion has the accepted negative verdict **refuted-as-stated**. No tier-1 truth warrant is assigned to that assertion, and no new claim identity is created by this grade.

The source note can retain the valid warning through one narrowly specified correction. In the final prose sentence under **What would finish this route**, replace the single occurrence of these exact bytes:

```text
nonzero finite-window contribution that this argument does not control.
```

with:

```text
potentially nonzero finite-window contribution that this argument does not control.
```

This is the occurrence at snapshot line 102. The authorization is confined to that body-text replacement, outside any `statement:` field. It changes guaranteed nonzeroness to the loss of guaranteed cancellation already derived in the report. It changes no hypothesis, displayed formula, proof step, bound, matching requirement or fixed-denominator criterion. The positive acceptance survives this specified correction under `docs/verification.md`, Grading and claim standing, provided the owning page discloses where its current wording differs from the reviewed text. The frozen subject and submitted review must remain unchanged: neither assessed the later replacement bytes as a new subject.

The word “Equivalently” requires the scoped interpretation stated in the decision table: contraposition of the order implication under the inherited hypotheses. It licenses no equivalence to the individual-tail sufficient condition, reverse order implication, or existence assertion. Likewise, the final route warnings do not import every result from the linked obstruction page. These are scope rulings on the supplied argument, not authorization to strengthen a statement.

Any change to a `statement:` field, to the mathematical statement's meaning, or beyond the specified body correction is not accepted as a repaired statement by this grade. A changed statement needs a newly frozen subject and fresh blind review; it remains author-recorded until the new warrant is obtained. A fresh card or stronger corollary cannot acquire coverage merely by citing the present page-level review.

The durable-custody conditions are:

1. Retain the assessed subject, unchanged submitted review and exact submitted grade under `wiki/research/prime_binary_new_attack/evidence/assets/matching_gap_windows/`, as `subject.md`, `review.md` and `grade.md`. Keep all mathematical derivations and witnesses supporting the decisions available from an ordinary clone.
2. File the review and this grade at `wiki/research/prime_binary_new_attack/evidence/verify/matching_gap_windows/review.md` and `grade.md`, with resolvable snapshot references. Any permitted publication edits preserve scope, dates, findings and verdicts, and are enumerated on the record's index page as the standard requires. Private custody and runtime material are not copied into public assets.
3. On the owning page, record the exact positive scope and the localized negative finding, and disclose the specified correction if made. Preserve the necessary provenance and exposure/materiality facts in the verification record and owning standing where applicable. The integrator records this grader's accepted judgment and adds no tier assertion of its own.
4. Keep the mathematical obligations visible: the required prime pairs with the strict tail and displacement properties remain unconstructed; each relevant odd denominator must be addressed for an irrationality conclusion; $d=1$ requires another argument. Nothing here changes Problem 251's standing as a whole or supplies Lean coverage.

A private handoff alone is not a public, clone-reconstructible warrant. The conditional tier assertion takes effect only upon that adoption; no corpus standing is changed by the grader. The report's identity-label limitation has been adjudicated, and no further mathematical input is required to grade this frozen packet. Adoption, any exact body correction and the unresolved prime-window construction remain distinct obligations.

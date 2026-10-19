---
name: research/erdos_354/evidence/verify/lead_rational_ratio_dyadic_floor_descent_rereview
title: "Blind re-review of the lead rational_ratio_dyadic_floor_descent"
desc: |
  Blind refutation re-review of the rational-ratio descent lead and the
  connections section it rests on: Lemma 354.1, Proposition 354.2,
  Corollary 354.3, Lemma 354.4, the constants, the two obstructions and
  every certificate figure survive (refutation-failed) under independent
  recomputation; the lead's "outside Corollary 354.3" is unproved for the
  two square-root pairs and its gap definition drops "at least". Two
  required corrections, four suggested, notes.
created: 2026-10-02T17:13:00Z
updated: 2026-10-02T17:13:00Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context (model: Claude Fable
5.1), given only the commissioning assignment. The reviewer took no part
in writing the lead, the connections page, the reconstruction pages or
their evidence, and read no review, grade or standing text of any of them.
Charge: refutation. This record carries no tier; a distinct grader records
pass or void for its contract.

**Subject.** The tree as it stood on 2026-10-02. The subject is a blind
extraction, kept outside the repository, of two pages on that date: the lead
page `wiki/research/leads/rational_ratio_dyadic_floor_descent/_index.md` with
its review-status fields and its "Current review" section removed, and the
connections page `wiki/research/erdos_354/connections.md` with its
review-report sentences cut. Every statement examined below is quoted or
paraphrased from the extraction's text as it stands. A first attempt at this
re-review, whose extraction carried the earlier verdicts, was stopped before
completion and its output discarded; this record is from a blind extraction
frozen on 2026-10-02 and kept outside the repository.

**Other reading, all from the tree of the frozen date.** Operating instructions:
`docs/verification.md`, `docs/evidence.md`, `docs/research.md`,
`docs/approach_vetting.md`, `docs/math_authoring.md`, whole. Mathematics the
route rests on, under `wiki/research/erdos_354/`:
`yu_chen_normalization_reconstruction.md` (whole; items 1--6 and the reduction
re-derived), `yu_chen_theorem_5_1_reconstruction.md` (whole; Steps 1--6
re-derived), `yu_chen_lemma_2_1_reconstruction.md`,
`yu_chen_lemma_2_2_reconstruction.md`, `yu_chen_lemma_2_3_reconstruction.md`
(whole; proofs read), `yu_chen_theorem_reconstruction.md` (whole; Step 2
re-derived), `yu_chen_fe_reconstruction.md`, `yu_chen_bg_reconstruction.md`,
`yu_chen_windows_reconstruction.md`, `yu_chen_db_reconstruction.md` (whole;
statements and the places where irrationality and good rationals enter read,
proofs not re-derived), and `evidence/_index.md` (the description of the entry
point; its standing lines skipped). Library:
`library/additive_bases/yu_chen_2026_erdos_problem_354_i_strong_completeness_two_dyadic_floor_sequences/theorem.md`
(whole) and the heading lines of its `_index.md`; the canonical conversion
beside that PDF at its Section 3 (hypotheses, (3.1)), Subsection 3.3, Theorem
5.1 with (5.2), Sections 6--7 and Appendix A (the mask table);
`library/additive_bases/fan_2026_strongly_complete_sets_conjecture_erdos/remark_4_2.md`
(Statement, Proof pointer, Dependencies, Bears on) and the canonical conversion
beside the Fan PDF at the paragraph of (1.9) stating Hegyvári's conjecture and
his proved case;
`library/additive_bases/hegyvari_1991_complete_sequences/_index.md`
(digest and results); the result lines of
`library/additive_bases/hegyvari_1994_sumset_certain_sets/_index.md` and
the statement lines of
`library/additive_bases/jenw1n_2026_erdos_354_part_i_lean_proof/_index.md`,
`library/additive_bases/jenw1n_2026_erdos_354_part_i_lean_proof/target.md`
and
`library/additive_bases/kitamura_2026_lean_proof_erdos_problem_354_ii/_index.md`,
located by search. Problem page `wiki/problems/additive_bases/E0354/_index.md`: the
Statement and Formulation paragraphs; the "Current assessment", "Progress and
known results" and "Linked library material" sections were not read.

**Exclusions and exposures.** The live lead page, the live connections
page, every file under an `evidence/verify/` folder and all review-status
text were excluded. Four exposures occurred, none of them mathematics
absent from the subject: (1) while copying the frontmatter and heading
skeleton of an existing record in this folder, its `desc` field and its
heading and finding-location lines were printed; the `desc` summarizes
that record's verdicts on an earlier revision of the same pages. No
finding below is taken from it; each verdict rests on the derivations and
computations recorded here, and the grader rules on materiality by the
content test of `docs/verification.md`. (2) The problem page's "Status"
paragraph and its frontmatter `desc`, which record the site-accepted Lean
answer to the first question, were printed with the Statement; the lead
itself states the same fact. (3) One remnant line of the folder evidence
index naming a report count and "no tier is assigned" was printed. (4) The
lead's evidence entry point
`wiki/research/leads/rational_ratio_dyadic_floor_descent/evidence/main.py`
was executed as a black box (its code and the evidence index were not
read): exit status 0, "ALL CHECKS PASS (23 checks)", with the certificate
lines agreeing with the independent recomputation below. (5) A read-only
`wiki lint` run after this record was written printed the pending index
rows of this folder and of another folder, including the `desc` lines of
two re-review records on other leads; none concerns this subject, and the
run changed no file.

**Computation.** Two independent checks were written from the
mathematical statements, not from repository code, and kept in scratch;
their methods are stated here so a reader can rerun them. First, the
certificates: weights $a_i=\lfloor2^i\alpha\rfloor$,
$b_i=\lfloor2^i\beta\rfloor$ computed exactly (integer division for a
rational coefficient, `isqrt(m << 2i)` for $\sqrt m$), the subset sums of
the first $n$ layers kept as one Python integer bitset
(`P |= P << w`), and the certificate located as the least index $A$ at
which the bit string holds $b_n$ consecutive ones, reported at the least
$n\ge1$ where one exists. This differs from a table- or set-based subset
sum enumeration in its primitive. Second, the certificate lemma of the
Theorem 5.1 page: the mask table transcribed from Appendix A of the source
conversion (twelve templates, 125 nodes, 113 links), each node's two
offsets reconstructed as linear forms in $(p,q)$ with constants, condition
1 (constants differ by one, in $[0,22]$) checked directly, conditions 2
and 3 checked for every choice of the form entering the maximum and the
minimum, positivity on the open cone $q<p<2q$ decided by
$2a+b\ge0$, $a+b\ge0$, $(a,b)\ne(0,0)$ for the form $ap+bq$, over all
four third-digit pairs. Result: no failure. The routine for the first
check is:

```python
def certificate(alpha, beta, max_depth):      # alpha, beta: floor2n(i)
    P = 1
    for n in range(0, max_depth + 1):
        if n >= 1:
            b_n = beta(n)
            s = bin(P)[2:][::-1]              # s[j] == "1" iff j in P_n
            A = s.find("1" * b_n)
            if A >= 0:
                return n, A, b_n
        P |= P << alpha(n)
        P |= P << beta(n)
    return None
```

## Restatement

The lead attacks Hegyvári's conjecture, as Fan's preprint and the problem
page record it, in the cases left open after the irrational-ratio theorem
and Hegyvári's one-dyadic case: $\alpha/\beta$ rational and not a power of
$2$, neither coefficient a dyadic rational. After a dyadic rescaling the
ratio is $p/q\in(1,2)$ in lowest terms, $\alpha=p\gamma$, $\beta=q\gamma$,
$\gamma$ not dyadic. The route transports the Yu--Chen permanent descent:
Theorem 5.1 (a long exact doubling block followed by a nonzero conversion
lowers the modular run invariant $h$ of every later layer by one, with
completeness when $h\le1$) uses only the interlacing of the two rays and
the digit recurrence, with the constant $K_*(p,q)=2q(p-1)+4(p+q)+64$
computed from the reduced pair of the block's first layer. At a rational
ratio that reduced pair is $(p,q)$ at every exact layer
($qa_s=pb_s$), so a common zero run of the conversions of length at least
$L_0=\lceil\log_2K_*\rceil-1$ starting at an exact layer gives one
descent, and a run of $L(p,q)=L_0+\lceil\log_2p\rceil$ zeros in the
expansion of $\gamma$ produces such a common run. Hence: Lemma 354.1
(incompleteness of a normalized non-dyadic pair forces an event in
$(n,4n]$ for all large $n$), Proposition 354.2 (infinitely many runs of
$L(p,q)$ zeros in a non-dyadic $\gamma$ give completeness of the
normalized sequence), Corollary 354.3 (strong completeness of
$A_{\alpha,\beta}$, hence for almost every $\gamma$ on each rational-ratio
line, by Borel), and Lemma 354.4 (a run of $b_n$ consecutive subset sums
of the first $n$ layers of a normalized pair certifies completeness),
with exact certificates for five pinned pairs and thirty-two pairs
$(3\cdot2^T/d,2\cdot2^T/d)$. The gap is the set of coefficients with only
finitely many qualifying common runs, which contains every rational
$\gamma$ of small odd denominator part and uncountably many irrationals;
for them the irrational-case continuation fails because a rational ratio
has finitely many good rational approximants and lies in the compact set
$\mathcal C_k$, so that returns between exact layers can cost two events.

## Statements and verdicts

- **S1, the target** (lead, "Target and status evidence"; connections,
  "Target"). *Refutation-failed* for the mathematics: Fan's conversion at
  (1.9) states the conjecture exactly as the lead does ($\alpha\not\sim
  \beta$, at least one coefficient not a dyadic rational, dyadic rational
  meaning $\alpha\sim n$ for a nonzero integer $n$) and records
  Hegyvári's proved case as "exactly one of $\alpha,\beta$ is a dyadic
  rational"; the reduction to $p/q\in(1,2)$, $q\ge2$, $\alpha=p\gamma$,
  $\beta=q\gamma$ is correct, as is the Bézout remark that $\gamma$ is
  dyadic exactly when both coefficients are (the dyadic rationals with
  $0$ form the ring $\mathbb Z[1/2]$). The sentences reporting what the
  problem page's Current assessment records are *not a mathematical
  claim* and were outside the read set; the grader or integrator checks
  them. Rescaling one coefficient by a nonnegative power of $2$ replaces
  the set by a subset, so strong completeness transfers upward, as the
  connections page says.
- **S2, nothing about the ratio enters Sections 1--6** (lead, "Route and
  established inputs"; connections, "Where irrationality enters").
  *Refutation-failed.* Re-derived: items 1--4 and 6 of the normalization
  page use only $N<M<2N$, $N\ge2$; item 5 uses only that the conversions
  are not eventually zero, which fails exactly when both coefficients are
  dyadic (then $\alpha=a_{n_0}2^{-n_0}$); items 1--3 use irrationality
  only to exclude $2^k\alpha_0/\beta_0=1$. Theorem 5.1's Steps 1--5 use
  $\gcd(p,q)=1$, $q<p<2q$, $S_n<d(p+q)$ and the interlacing: Step 1's
  covering of $[F,(p+q)(K-1)-F]$ (the residue choice $qy\equiv z\bmod p$
  with $0\le y<p$ and the reflection), Step 2's two bounds on
  $(z-\sigma_0-f)/d$, (4.1) as $64d-42\ge22d$, the chain union from
  $L_1\le p+2q$ and $U_s\ge7p+6q$, (4.3) as $20d-13>0$, and Step 5's
  mesh and projection all check; the source's Section 3 and Theorem 5.1
  carry the same hypotheses and constant. The certificate lemma, the one
  finite input, holds under the independent check described above. Only
  (5.2) brings in the layer index, through $p\le a_n<2^n(M+1)$.
- **S3, Lemma 354.1.** *Refutation-failed.* Infinitely many events as in
  S2; Step 2 of the theorem page consumes Theorem 5.1, (5.2) and the
  infinitude of events only: a qualifying pair $n<m$ with
  $m-n\ge2n+C_M$ gives $K=2^{m-n}\ge K_*$ by (5.2), the permanent bound
  $h_t\le\max(0,h_n-1)$ for $t\ge m+3$ with completeness if $h_n\le1$, so
  under incompleteness infinitely many qualifying pairs would give a
  strictly decreasing integer sequence bounded below by $2$; and with
  $m<3n'+C_M$ for the last event $n'\le n$ and $n\ge n_0=\max(t_1,C_M)$
  the successor event lies in $(n,4n]$.
- **S4, Proposition 354.2.** *Refutation-failed.* (ii): $\delta_s=qa_s-pb_s
  =-q\{2^s\alpha\}+p\{2^s\beta\}$ since $q2^s\alpha=p2^s\beta$; on a common
  zero run of length $L'\ge\log_2p$ from $s$ both fractional parts are
  below $2^{-L'}$, so $|\delta_s|<p2^{-L'}\le1$ and $\delta_s=0$. (iii):
  with $x=\{2^s\gamma\}<2^{-L}$ and $2^L\ge p$, $\{2^s\alpha\}=px<
  2^{-(L-\lceil\log_2p\rceil)}=2^{-L_0}$ and likewise for $\beta$, so the
  conversions vanish on $[s,s+L_0)$; $L_0>\log_2p$ because $K_*>4p$.
  (iv): the maximal common run $[s',s'+L'-1]\supseteq[s,s+L_0)$ is finite,
  its start is exact by (ii), and the Section 3 hypotheses hold at
  $n=s'$, $\ell=L'+1$, $K=2^\ell\ge2^{L_0+1}=2^{\lceil\log_2K_*\rceil}\ge
  K_*$, with $r=s'+L'+4$. (v): infinitely many distinct maximal runs since
  the starts tend to infinity and each run is finite; reading the bound
  of run $j$ at $t=s'_{j+1}\ge s'_j+L'_j+4$ gives the descent. The
  equality of exact layers with $\{2^s\gamma\}<1/p$ (connections, first
  bullet) is also right: with $2^s\gamma=I+x$, $\delta_s=q\lfloor px\rfloor
  -p\lfloor qx\rfloor$, and $\gcd(p,q)=1$ with $0\le\lfloor px\rfloor<p$
  forces $\lfloor px\rfloor=0$.
- **S5, Corollary 354.3 and the almost-every consequence.**
  *Refutation-failed.* The normalization of items 1--3 needs only
  $2^k\alpha_0/\beta_0\ne1$; the normalized pair has ratio $p/q$ and
  $\gamma'=2^v\gamma$, a shift of the expansion, so the hypothesis
  survives; the reduction gives completeness of
  $A_{\alpha,\beta}\setminus F$ for every finite $F$. Normal numbers to
  base $2$ contain every finite block infinitely often and are irrational,
  so the full-measure statement follows from Borel's theorem, which the
  lead names as imported.
- **S6, the constants.** *Refutation-failed.* $K_*(3,2)=92$,
  $\lceil\log_292\rceil=7$, $L_0=6$, $L=8$; $K_*(5,4)=132$,
  $\lceil\log_2132\rceil=8$, $L_0=7$, $L=10$; $K_*(5,3)=120$,
  $\lceil\log_2120\rceil=7$, $L_0=6$, $L=9$; $2^{\lceil\log_2K_*\rceil}=128$
  at ratio $3/2$.
- **S7, Lemma 354.4.** *Refutation-failed.* With $\Lambda_0=b_n$ consecutive
  integers from $A$ and weights $c_0=b_n<c_1=a_n<c_2=b_{n+1}<\cdots$ of
  indices at least $n$, $c_{j+1}\le2c_j$ by item 4, adjoining $c_j\le
  \Lambda_j$ yields $\Lambda_j+c_j$ consecutive integers from $A$ because
  the two intervals abut or overlap, and $\Lambda_{j+1}\ge2c_j\ge c_{j+1}$
  keeps the invariant; the lengths diverge, so every integer at least $A$
  is a subset sum of distinct weights, which are distinct nonzero elements
  of the set. The sentence attributing this to the mesh lemma "with gap 1"
  is loose: $b_n$ consecutive integers have span $b_n-1$, one short of the
  mesh lemma's hypothesis $\operatorname{span}(W)\ge c$; the count
  argument the proof actually gives replaces it (Suggested corrections).
- **S8, the five pinned certificates** (connections, after Lemma 354.4;
  lead, fourth bullet). *Refutation-failed.* Independent recomputation:
  $(48/5,32/5)$, normalized with $N=6$, $M=9$, least depth $9$, least
  start $1423$, $b_9=3276$; $(48/7,32/7)$: $9$, $577$, $2340$;
  $(80/9,64/9)$: $7$, $445$, $910$; $(6\sqrt2,4\sqrt2)$: $7$, $183$,
  $724$; $(5\sqrt2,3\sqrt2)$: $3$, $18$, $33$. All five pairs are
  normalized.
- **S9, the sweep.** *Refutation-failed.* The odd $d$ with $5\le d\le99$
  not divisible by $3$ number $32$; the least normalizing $T$ gives the
  pairs the page names for $d=23,89,91$ ($T=6,8,8$); all $32$ certify by
  depth $12$, $29$ of them by depth $9$, and the three exceptions are
  $d=23$ at depth $10$ from $2139$ with $b_{10}=5698$, $d=89$ at depth
  $12$ from $11036$ with $b_{12}=23563$, $d=91$ at depth $11$ from $4323$
  with $b_{11}=11522$, exactly as stated.
- **S10, the controls.** *Refutation-failed.* $(\sqrt{50},\sqrt{20})$ is
  normalized ($N=4$, $M=7$) and certifies at depth $6$ (from $77$ with
  $b_6=286$). $(5/2,5)$ has no certificate to depth $16$, and cannot have
  one at any depth: its weights are $2$ and $5\cdot2^k$, each power
  twice, so every subset sum is $\equiv0$ or $2\pmod5$ and no three
  consecutive integers are represented, which is also the incompleteness
  the page asserts.
- **S11, "outside every held source."** *Refutation-failed within the read
  set.* The Yu--Chen theorem and the site-accepted Lean statement concern
  irrational ratios; the base-$\sqrt\varphi$ Lean proof concerns another
  base; Fan's preprint proves no two-ray completeness and records
  Hegyvári's one-dyadic case; Hegyvári 1991 gives a measure dichotomy and
  a completeness criterion, Hegyvári 1994 incompleteness constructions and
  typicality for a dyadic $\alpha$; none proves completeness of a pair
  with rational ratio and two non-dyadic coefficients. Sources not held
  are outside the sentence's scope.
- **S12, "outside Corollary 354.3"** (lead, fourth bullet; connections,
  "none of these pairs is covered by Proposition 354.2"). For the
  thirty-five rational pairs *refutation-failed*: $\{2^s\gamma\}\ge1/d$
  bounds every zero run of $1/d$ by $\lceil\log_2d\rceil-1\le6<8$ for
  $d\le99$, and the maximal runs are $2$ for $16/5$ and $16/7$ and $3$
  for $16/9$ (ratio $5/4$, where $10$ is needed). For $(6\sqrt2,4\sqrt2)$
  and $(5\sqrt2,3\sqrt2)$: *proof defective; statement unresolved*.
  Whether $2\sqrt2$ has infinitely many runs of eight zeros, or $\sqrt2$
  of nine, is an open question (both hold if $\sqrt2$ is normal), so the
  lead's "outside Corollary 354.3" asserts for these two pairs something
  unproved; the connections page's wording, "not known to have infinitely
  many such runs", is the supported one (Required corrections, R1).
- **S13, the gap paragraph** (lead, "The consequential gap"; connections,
  first bullet). The defining sentence "only finitely many maximal common
  zero runs of length $\lceil\log_2K_*\rceil-1$ at exact layers" is
  *refuted-as-stated* under its literal reading and correct with "at
  least": at ratio $3/2$, $\gamma=1/511$ has conversions zero on
  $[9j,9j+6]$ and nonzero at $9j+7$, $9j+8$, so its maximal common zero
  runs at exact layers all have length exactly $7$, none has length $6$,
  and the literal sentence places $1/511$ in the gap while the same
  paragraph says it is covered by Corollary 354.3 (Required corrections,
  R2). Every other claim of the paragraph is *refutation-failed*: at an
  exact layer a common run of length at least $L_0$ means
  $p\{2^s\gamma\}<2^{-L_0}$, hence $\{2^s\gamma\}<2^{-\lceil\log_2K_*\rceil}$;
  a rational $\gamma$ with odd denominator part $v$ has
  $\{2^s\gamma\}\ge1/v$ for large $s$, so $v\le2^{\lceil\log_2K_*\rceil}$
  ($128$ at ratio $3/2$, $256$ at $5/4$) excludes such runs, which covers
  every certified rational pair ($d\le99$, $v=5,7$ at ratio $3/2$, $v=9$
  at ratio $5/4$); an irrational $\gamma$ whose expansion has no zero run
  of length $\lceil\log_2K_*\rceil$ is excluded too, and there are
  uncountably many; $\gamma=24/7$ has $\{2^s\gamma\}\in\{3/7,6/7,5/7\}$,
  never below $1/3$, with $\delta_s=2,1,1$ as stated; and a run shorter
  than $L_0$ gives $K\le2^{L_0}<K_*$, so Theorem 5.1 does not apply with
  the fixed constant.
- **S14, the two obstructions** (lead, "The consequential gap";
  connections, second bullet). *Refutation-failed.* A reduced
  $p'/q'\ne p/q$ has $|p/q-p'/q'|\ge1/(qq')$, so $|p/q-p'/q'|<1/q'^2$
  forces $q'<q$: finitely many good rationals, so (DB), which needs a
  good denominator at least $2^n\beta$, and the crossing denominator
  $D(b)$ for $b>q$ are unavailable. With $2^J\le p<2^{J+1}$, $p/2^J$ and
  $q/2^J$ are sums of at most $k$ elements of $\{2^{-j}\}$ with
  $q/2^J>1/2$, so $p/q\in\mathcal C_k$ once $k$ is at least the number of
  ones in $p$ and $q$. The witness: for $x=\{2^s\gamma\}\in[1/4,1/3)$ at
  ratio $3/2$, $\lfloor6x\rfloor=1$, $\lfloor4x\rfloor=1$,
  $\lfloor12x-2\rfloor=1$, $\lfloor8x-2\rfloor=0$, so the conversions are
  $(1,1),(1,0)$, $U=3$, $V=2$, $\delta_{s+2}=4\delta_s+2U-3V=0$, and
  $\{2^{s+2}\gamma\}=4x-1<1/3$ is the next exact layer after the
  nonexact $s+1$: two events per return. The finite-event decay then only
  bounds the missing count by $e^{-aK_n}$ with $K_n\gg\log n$ under
  bounded spacing, a polynomially small fraction.
- **S15, "pair by pair certifiable but not uniformly proved."**
  *Refutation-failed* as a statement about this route; whether another
  source settles these coefficients is outside the read set.
- **S16, the next step** (lead, "Next step"). The identity
  $a_{n+i}=2^ia_n+r_i$ holds with $r_i=\lfloor2^i\{2^n\alpha\}\rfloor$,
  the integer whose binary digits are the conversions $u_n,\ldots,
  u_{n+i-1}$; for rational $\gamma$ with odd denominator part $v$ these
  digits are eventually periodic with the order of $2$ modulo $v$ as a
  period, but $r_i$ itself is not periodic in $i$ (Suggested corrections,
  S3). "Each positive case is a proved instance" is *refutation-failed*
  through Lemma 354.4. The outcome sentences are plans, *not a
  mathematical claim*; the conditional that an incomplete pair with
  rational ratio, not a power of $2$, and two non-dyadic coefficients
  would refute the conjecture is correct.
- **S17, "Provisional premises."** "The a.e. statement imports Borel's
  normal number theorem" is *refutation-failed*. The section omits the
  premises the route actually consumes (Premises below; Suggested
  corrections, S1).

## Checklist

- Quantifiers and scope: one defect, the dropped "at least" in the gap
  definition (S13); the "almost every" of Corollary 354.3 is never upgraded
  to "every", and the lead's "every coefficient with long zero runs" means
  infinitely many runs, as the statement says.
- Circularity: none; the descent is applied forward from each qualifying
  block and incompleteness enters only as the hypothesis of an infinite
  descent.
- Model and convention changes: none; the normalized tails and the
  original set are connected by the reduction, re-derived.
- Finite and statistical overreach: none; each certificate is claimed
  for its own pair only, and the controls are controls.
- Uniformity: the constant $K_*(p,q)$ is fixed by the ratio and the
  length condition (5.2) is not used, as stated; $C_M$ depends on $M$
  only.
- Extremal conclusions: the depths and starts are least values, confirmed
  in the claim's own units.
- Consequences and composition: the lead's "outside Corollary 354.3" for
  the two square-root pairs overstates (S12); every other "hence" checks.
- Computation: exact arithmetic throughout the recomputation; the
  claimed figures match.
- Reproduction: the lead's entry point exits $0$ with $23$ passing checks;
  its coverage claim ("the pinned pairs, a sweep over thirty-two rational
  coefficients, and an incomplete control pair") matches its printed
  lines and the recomputation.
- Source and verdict fidelity: the conjecture, its proved case, Section 3,
  Theorem 5.1, (5.2) and Appendix A agree with the source conversions;
  verdict quotations are outside this reviewer's subject.

## Weakest steps

- **W1, exactness at the start of a maximal run.** The descent needs the
  reduced pair $(p,q)$ at the layer where Theorem 5.1 is applied, which
  is the start $s'$ of the maximal common run, not the position $s$ of the
  run in $\gamma$. Re-derived: the run from $s'$ has length
  $L'\ge L_0>\log_2p$, so $|\delta_{s'}|<p2^{-L'}<1$ and $\delta_{s'}=0$.
  Without this the constant would be that of a nonexact layer's reduced
  pair, which grows with the layer.
- **W2, the length of the induced common run.** $x<2^{-L}$ gives
  $px<2^{-L_0}$ only because $2^{\lceil\log_2p\rceil}\ge p$; the lead's
  $L=L_0+\lceil\log_2p\rceil$ is exactly what is needed, and the common run
  then has length at least $L_0$, giving $K=2^{L'+1}\ge2^{L_0+1}
  =2^{\lceil\log_2K_*\rceil}\ge K_*$. Here $2^{L_0+1}$ is used, not
  $2^{L_0}<K_*$; the proof's $\ell=L'+1$ counts the block of $L'$ exact
  pairs plus the layer of the nonzero conversion, matching Section 3.
- **W3, the finite certificate.** Everything above rests on the
  certificate lemma, a finite statement about 125 nodes. Rechecked
  independently from the source conversion, including the four-choice
  reading of conditions 2 and 3; it holds.

## Strongest attack

The attack sought a coefficient that satisfies the hypothesis of
Proposition 354.2 or sits inside the lead's gap set while the mechanism
misbehaves, and a certificate figure that fails exact recomputation. (a)
At ratio $3/2$ the pair $(1536/511,1024/511)$, normalized with $N=2$,
$M=3$, has exact layers and maximal common zero runs exactly where
Proposition 354.2 predicts ($[0,6]$, $[9,15]$), $h_n=0$ for $0\le n\le20$,
and a certificate at depth $2$: consistent. (b) The gap pair
$(192/23,128/23)$ has $h_n$ equal to $0,0,2,2,0,1,1,1,0,\ldots$ for
$n\le16$ and no common zero run longer than $2$ in that range, so the
fixed-constant descent indeed never fires there, yet the pair certifies
at depth $10$: the gap is a limit of the mechanism, not evidence of
incompleteness, as the lead says. (c) The sharper threshold: a common run
of length at least $L_0$ at an exact layer requires
$\{2^s\gamma\}<2^{-L_0}/p$, so odd parts $v<p2^{L_0}$, that is $v\le191$
at ratio $3/2$, are excluded, not only $v\le128$; the page's bound is
implied and its "in particular" clauses survive. Conversely
$\gamma=1/193$ at ratio $3/2$ has, at every $s$ with
$\{2^s\gamma\}=1/193$ (infinitely many, by periodicity), a maximal common
run of length exactly $6=L_0$ starting at an exact layer (the preceding
conversion is nonzero since $\{2^{s-1}\gamma\}=97/193$), so the descent
of Proposition 354.2's proof applies, while $\gamma$ has no run of eight
zeros and Corollary 354.3's hypothesis fails: the corollary's sufficient
condition is weaker than the mechanism, which is no error (Notes). (d)
The certificates of all thirty-nine pairs were recomputed exactly; none
fails. The attack on the mathematics failed; the two findings are wording
defects (S12, S13).

## Premises

The route consumes, in order of load: the normalization page's items
1--6 and reduction; Lemmas 2.1--2.3; Theorem 5.1 with its certificate
table and (5.2); Step 2 of the theorem page; the definitions of good
rationals, (DB), $D(b)$ and $\mathcal C_k$ from the digit-budget, windows
and bounded-spacing pages for the two obstructions; Borel's normal number
theorem (standard, imported) for the almost-every clause; and Fan's
preprint (held, p. 4) with the problem page's assessment for the
statement of the conjecture and Hegyvári's proved case. All repository
inputs are author-recorded reconstructions of an unrefereed manuscript;
their current standing was outside this review's read set and is for the
grader to read at filing. Within this review the consumed deductions of
the normalization page, the three lemmas, Theorem 5.1 and Step 2 of the
theorem page were re-derived and the certificate table was rechecked, so
the transport stands on them as mathematics; it stands on nothing else.
The site-attested Hegyvári case delimits the target and is consumed by no
proof. No external premise is unread except the problem page's
assessment sentences, which this reviewer could not open.

## Required corrections

- **R1.** Lead, "Route and established inputs", fourth bullet, final
  clause. Replace "all outside every held source and outside Corollary
  354.3." with "all outside every held source and none covered by
  Corollary 354.3: the rational coefficients have no zero run of the
  required length, and $\sqrt2$ is not known to have infinitely many."
- **R2.** Lead, "The consequential gap", first sentence. Replace
  "Coefficients $\gamma$ with only finitely many maximal common zero runs
  of length $\lceil\log_2K_*\rceil-1$ at exact layers:" with "Coefficients
  $\gamma$ with only finitely many maximal common zero runs of length at
  least $\lceil\log_2K_*\rceil-1$ at exact layers:".

## Suggested corrections

- **S1.** Lead, "Provisional premises". After the first sentence add:
  "The transport imports, as author-recorded reconstructions of an
  unrefereed manuscript, items 1--6 and the reduction of the
  normalization page, Lemmas 2.1--2.3, Theorem 5.1 with the Appendix A
  certificate (finite data rechecked by the folder's evidence) and Step 2
  of the theorem page; Lemma 354.4 and the certificates rest on the
  normalization page alone."
- **S2.** Connections page, paragraph after the proof of Lemma 354.4,
  first sentence. Replace "This is the mesh lemma of the Lemma 2.2 page
  with gap $1$, as the digit-budget page uses it," with "This is the
  abutting case of the mesh lemma of the Lemma 2.2 page with gap $1$: the
  $b_n$ consecutive integers have span $b_n-1$, one short of the lemma's
  hypothesis, which the count argument above replaces; the digit-budget
  page uses the lemma with span at least the next weight,".
- **S3.** Lead, "Next step", first sentence. Replace "with a periodic
  correction $r_i$" with "with the correction
  $r_i=\lfloor2^i\{2^n\alpha\}\rfloor$, the integer whose binary digits
  are the eventually periodic conversions". The same phrase on the
  connections page ("Next investigation", first direction) takes the same
  replacement.
- **S4.** Lead, "Target and status evidence". After "as Hegyvári's
  (site-attested, paper not held)" add "and recorded in Fan's preprint
  (held, p. 4)", which the held source states.

## Notes

- **N1.** The hypothesis of Proposition 354.2 can be weakened without
  changing its proof: it suffices that the expansions of $p\gamma$ and
  $q\gamma$ have infinitely many common runs of $L_0=\lceil\log_2K_*\rceil
  -1$ zeros, since such a run starts at an exact layer by (ii) and
  supplies the block of (iv) directly. The example $\gamma=1/193$ at ratio
  $3/2$ (Strongest attack, (c)) is complete by this reading and outside
  Corollary 354.3 as stated. The exact rational threshold for the gap set
  is $v<p2^{L_0}$, that is odd $v\le191$ at ratio $3/2$ and $v\le639$ at
  ratio $5/4$.
- **N2.** Lemma 1 of the held Hegyvári 1991 paper, as its card records
  it, is a finite completeness criterion for the same two-ray sets (an
  interval $[k,a_p]$ of subset sums with $k$ below two weight
  differences). It is a relative of Lemma 354.4 that the connections page
  does not mention when it names van Doorn's Lemma 5 as the single-ray
  analog; citing it beside Lemma 354.4 would place the certificate idea
  in the held literature.
- **N3.** "Period the order of $2$ modulo $v$" (connections, "Next
  investigation") is a period, not necessarily the least one: for
  $\gamma=1/9$ and $p=3$ the digits of $3\gamma=1/3$ have period $2$ while
  the order of $2$ modulo $9$ is $6$.
- **N4.** The controls in the lead's entry point include two checks on
  the structure of $(5/2,5)$ ("beta-ray is the shifted alpha-ray",
  "merged multiset at most doubles from the second term") besides the
  absence of a certificate; the incompleteness itself follows from the
  residues modulo $5$ (S10) and needs no depth bound.
- **N5.** The extraction's "Provisional premises" ends with a sentence
  pointing to a "Current review" section that the extraction removed;
  this is a consequence of the cut, not a defect of the page.

## Verdict

**Mathematics: refutation-failed** for Lemma 354.1, Proposition 354.2,
Corollary 354.3 with its almost-every clause, Lemma 354.4, the constants
$L(3,2)=8$, $L(5,4)=10$, $L(5,3)=9$, the two obstructions with the
two-event witness, and the certificate figures of all thirty-nine pairs
(five pinned pairs, thirty-two sweep pairs with the three deep
denominators, two controls), each under the independent derivations and
recomputations recorded above.
**Refuted-as-stated**, as wording only: the gap set's defining sentence in
the lead, which drops "at least" and under its literal reading contains
the coefficient $1/511$ that the paragraph itself calls covered (R2).
**Proof defective; statement unresolved**: the lead's "outside Corollary
354.3" for $(6\sqrt2,4\sqrt2)$ and $(5\sqrt2,3\sqrt2)$, which asserts an
open property of $\sqrt2$ (R1). The route as written stands on the
author-recorded reconstructions it names, re-derived here at the
deductions it consumes, and claims nothing beyond them once R1 and R2 are
made. The lead's conclusion that Hegyvári's conjecture remains open on
this route for the coefficients of its gap set, pair by pair certifiable
and not uniformly proved, is correct as a statement about the route.

**Limitations.** No tier is asserted. The standing of the reconstruction
pages, the lead's evidence index and code, the problem page's assessment
and every filed review were outside the read set; the exposures listed
under Subject and independence are disclosed for the grader's materiality
ruling. The independent checks were written from the mathematical
statements and kept in scratch; their methods and the one routine that
carries the certificate figures are recorded above for rerun, and the
certificate-lemma check is reproducible from Appendix A of the source
conversion by the stated cone criterion. Whether a source outside the
library settles any of the gap coefficients was not searched.

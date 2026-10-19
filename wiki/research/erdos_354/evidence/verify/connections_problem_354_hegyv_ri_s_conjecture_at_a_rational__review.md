---
name: research/erdos_354/evidence/verify/connections_problem_354_hegyv_ri_s_conjecture_at_a_rational__review
title: "Independent review of the connections section: Problem 354: Hegyvári's conjecture at a rational ratio"
desc: |
  Refutation review of the rational-ratio section and its lead: Lemma
  354.1, Proposition 354.2, Corollary 354.3 and Lemma 354.4 survive
  (refutation-failed); the bounded-run obstruction and the lead's gap
  paragraph are refuted-as-stated, since rational coefficients with long
  zero runs are covered by the page's own corollary and exact layers need
  not exist; the depth-nine sweep sentence fails exact recomputation for
  three denominators. Three required corrections, one suggested, four
  notes.
created: 2026-09-28T18:31:00Z
updated: 2026-09-28T20:40:46Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context, given only the
commissioning assignment. The reviewer took no part in writing the
connections page, the lead, the reconstruction pages or their evidence,
and read no earlier review of any of them. Charge: refutation.

**Subject.** The page `wiki/research/erdos_354/connections.md` as it stood at
2026-09-28T13:50:48Z, section "## Problem 354: Hegyvári's conjecture at a
rational ratio", lines 59--291 (from its H2 heading to the next H2 at line 292),
together with the lead page
`wiki/research/leads/rational_ratio_dyadic_floor_descent/_index.md` as of the
same time, read in full. The page's shared preamble (lines 1--58: purpose,
standing, notation, the definitions of complete, strongly complete, normalized
pair, conversions, events, $P_n$, $D_n$, $h_n$, dyadic rational, Hegyvári's
conjecture) was read as an input.

**Premises read in full** (reconstruction pages as of the same time, treated as
established at their reviewed standing):
`yu_chen_normalization_reconstruction.md`,
`yu_chen_theorem_5_1_reconstruction.md`, `yu_chen_theorem_reconstruction.md`,
`yu_chen_fe_reconstruction.md`, `yu_chen_windows_reconstruction.md`,
`yu_chen_bg_reconstruction.md`, `yu_chen_db_reconstruction.md`,
`yu_chen_lemma_2_1_reconstruction.md`, `yu_chen_lemma_2_2_reconstruction.md`,
`yu_chen_lemma_2_3_reconstruction.md`. The two Fan and two Geneson
reconstruction pages were not read; the section does not use them.

**Other reading.** Problem page `wiki/problems/additive_bases/E0354/_index.md`:
the Statement block (lines 21--33). Library: the Yu--Chen card's
provenance and read-status paragraphs and its `theorem.md` statement
section; the Fan card's provenance and read-status paragraphs and the
`remark_4_2.md` statement section; the Hegyvári 1991 card. Held PDFs
(text layer): Yu--Chen pp. 1--7 (Theorem, scope, Sections 1--7 with the
Section 3 hypotheses, Theorem 5.1, (5.2), Section 6) and pp. 13--14
(Section 11); Fan v5 p. 4 (Hegyvári's conjecture, (1.9)) and p. 20
(Remark 4.2); Hegyvári 1991 pp. 7--9 (Theorem, Lemmas 1 and 2). Wiki:
`docs/verification.md` sections "Grading and claim standing", both audit
checklists and "Whole-claim report"; `docs/approach_vetting.md`;
`docs/evidence.md` "Source fidelity"; `docs/math_authoring.md`.

**Computation.** Every certificate figure quoted in the section and every
witness below was recomputed independently in exact arithmetic (rational
coefficients as fractions, quadratic coefficients through integer square
roots, subset sums as bit sets, the failing and one passing case
cross-checked with a set-based implementation). The lead's evidence
folder was neither read nor run.

**Exposures.** Three, none of them a review, grade or assessment text:
(1) a directory listing of `wiki/research/erdos_354/` as of that time showed
the file names under `evidence/verify/`, including one review file per
reconstruction page and `grade.md`; no content was read. (2) Lines 35--48 of the
problem page (the Formulation paragraph after the Statement) were displayed
while extracting the statement. (3) The Yu--Chen `theorem.md` page's Proof
pointer, Dependencies and Bears-on sections and the card's overview paragraph
were displayed with the statement; the Bears-on section carries the site's
acceptance record for the first question. Nothing under any `evidence/` folder,
no Current assessment, Known results or standing text, and no web source was
read.

## Restatement

Throughout, a *normalized pair* has
$N=\lfloor\beta\rfloor<M=\lfloor\alpha\rfloor<2N$ and $N\ge2$, which forces
$1<\alpha/\beta<2$; $u_i,v_i\in\{0,1\}$ are the
binary digits of $\alpha,\beta$ at position $i+1$; a *common zero run* is
an index interval on which $u_i=v_i=0$; $\delta_s=qa_s-pb_s$; a layer is
*exact* when $\delta_s=0$.

- **S1 (setup).** Hegyvári's conjecture: $A_{\alpha,\beta}$ is complete
  whenever $\alpha/\beta$ is not a power of $2$ and at least one of
  $\alpha,\beta$ is not a dyadic rational. The section takes as open the
  cases with $\alpha/\beta$ rational, not a power of $2$, neither
  coefficient dyadic. Multiplying one coefficient by a nonnegative power
  of $2$ replaces $A_{\alpha,\beta}$ by a subset whose strong completeness
  implies that of the original; the ratio becomes $p/q\in(1,2)$ in lowest
  terms with $q\ge2$; with $\gamma=\beta/q$, both coefficients are dyadic
  exactly when $\gamma$ is.
- **S2 (inventory of irrationality).** Item 5 of the normalization page
  needs only that the conversions are not eventually zero, which fails
  exactly when both coefficients are dyadic; items 1--4, 6 and the
  reduction hold whenever the ratio is not a power of $2$; the three
  finite lemmas and Theorem 5.1 with its certificate are ratio-free;
  $K_*$ is computed from the reduced pair of the layer where the theorem
  is applied and only (5.2) involves the layer index; Step 2 of the
  theorem page consumes only Theorem 5.1 and the infinitude of events;
  finite-event decay holds for every normalized pair; irrationality is
  consumed only by the windows page (good rationals of unbounded
  denominator) and by Step 2 of the bounded-spacing page
  ($\theta\notin\mathcal C_k$).
- **S3 (Lemma 354.1).** For every normalized pair not consisting of two
  dyadic rationals: if the normalized sequence is incomplete, then only
  finitely many pairs of consecutive events $n<m$ satisfy
  $m-n\ge2n+C_M$ with $C_M=16(M+1)^2$, and there is $n_0$ such that every
  $n\ge n_0$ has an event in $(n,4n]$.
- **S4 (Proposition 354.2).** For a normalized pair with rational ratio
  $p/q$ in lowest terms and $\gamma=\beta/q$, put
  $K_*(p,q)=2q(p-1)+4(p+q)+64$ and
  $L(p,q)=\lceil\log_2K_*\rceil-1+\lceil\log_2p\rceil$. If $\gamma$ is
  not dyadic and its binary expansion has infinitely many runs of at
  least $L(p,q)$ consecutive zeros, then every sufficiently large integer
  lies in $\bigcup_nP_n$.
- **S5 (Corollary 354.3).** For $\alpha,\beta>0$ with rational ratio not
  a power of $2$, $p/q$ the reduced form of the unique $2^k\alpha/\beta$
  in $(1,2)$ and $\gamma=\beta/q$: if $\gamma$ is not dyadic and has
  infinitely many runs of $L(p,q)$ zeros, then $A_{\alpha,\beta}$ is
  strongly complete. Hence for each fixed rational ratio $p/q\in(1,2)$,
  $A_{p\gamma,q\gamma}$ is strongly complete for Lebesgue-almost every
  $\gamma>0$ (Borel's normal number theorem imported).
- **S6 (constants).** $L(3,2)=8$ with $K_*=92$, $L(5,4)=10$ with
  $K_*=132$, $L(5,3)=9$ with $K_*=120$; $A_{3\gamma,2\gamma}$ is strongly
  complete for every non-dyadic $\gamma$ with infinitely many runs of
  eight zeros; for irrational $\gamma$ these pairs have two irrational
  coefficients and a rational ratio, outside every proved case.
- **S7 (Lemma 354.4).** For a normalized pair, if for some $n\ge1$ the
  set $P_n$ contains the $b_n$ consecutive integers $A,\ldots,A+b_n-1$,
  then every integer at least $A$ lies in some $P_t$; hence
  $A_{\alpha,\beta}$ is complete and so is the problem's indexed
  multiset for this pair.
- **S8 (pinned certificates).** $(48/5,32/5)$ at depth $9$ from $1423$
  with $b_9=3276$; $(48/7,32/7)$ at depth $9$ from $577$ with
  $b_9=2340$; $(80/9,64/9)$ at depth $7$ from $445$ with $b_7=910$;
  $(6\sqrt2,4\sqrt2)$ at depth $7$ from $183$ with $b_7=724$;
  $(5\sqrt2,3\sqrt2)$ at depth $3$ from $18$ with $b_3=33$; the control
  $(\sqrt{50},\sqrt{20})$ at depth $6$; no certificate for $(5/2,5)$ to
  depth $16$; none of the certified pairs is covered by S4.
- **S9 (sweep).** Every pair $(3\gamma,2\gamma)$ with $\gamma=2^T/d$, for
  the thirty-two odd $d$ with $5\le d\le99$ not divisible by $3$,
  normalized by the least $T$, is certified by depth $9$.
- **S10 (obstruction 1).** Every rational $\gamma$ and uncountably many
  irrationals have bounded zero runs; for them the descent has no long
  exact block and the conjecture stays open except pair by pair;
  $\{2^s\gamma\}<1/p$ is exactly $\delta_s=0$; such coefficients still
  have exact layers, but the blocks after them are shorter than
  $\log_2K_*$, which Steps 1 and 4 of Theorem 5.1 need.
- **S11 (obstruction 2).** A rational $\theta=p/q$ has only finitely many
  good rationals (a reduced $p'/q'\ne\theta$ good forces $q'<q$), so (DB)
  is empty for large $n$, $D(b)$ does not exist for $b>q$ and (10.2) is
  unavailable; $\theta\in\mathcal C_k$ once $k$ is at least the number of
  binary ones in $p$ and in $q$; at $\theta=3/2$ every $s$ with
  $\{2^s\gamma\}\in[1/4,1/3)$ is exact, has conversions $(1,1)$, $(1,0)$
  at $s,s+1$, and $s+2$ is exact again: a two-event return; bounded
  spacing is therefore not contradictory by itself, and (FE) only bounds
  the missing count by a polynomially small fraction under bounded
  spacing.
- **S12 (obstruction 3).** Corollary 354.3 is a full-measure statement on
  each rational-ratio line; the exceptional set contains every pair with
  rational coefficients; Hegyvári's 1991 dichotomy is neither used nor
  sharpened.
- **S13 (next investigation).** For rational $\gamma=m/v$ with $v$ odd
  the conversions are eventually periodic with period the order of $2$
  modulo $v$; blocks satisfy $a_{n+i}=2^ia_n+r_i$ with periodic $r_i$;
  whether analogs of the coefficient interval and node connection exist
  is the question; conditional outcomes; extension of the certificate
  search.
- **S14 (outcome).** The transfer list: Lemma 354.1 for every non-dyadic
  normalized pair, Proposition 354.2 and Corollary 354.3 for almost every
  coefficient on every rational-ratio line, Lemma 354.4 with certified
  pairs; open for the bounded-run coefficients.
- **S15 (lead).** Target and reduction as in S1; the route through the
  Theorem 5.1 page, the normalization and the three lemmas; summaries of
  S3--S7 and S9; provisional premises, including the sentence that the
  Theorem 5.1 reconstruction "is not among the filed reviews"; the
  consequential gap as in S10 and S11; next step as in S13; unreviewed
  standing.

## Checklist

- **Quantifiers and scope.** S3--S7 carry their quantifiers exactly
  (every finite $F$, every normalized pair, infinitely many runs, almost
  every $\gamma$ per line). S10 and S12 fail: "every rational $\gamma$"
  is excluded from the descent (S10) and "the exceptional set contains
  every pair with rational coefficients" (S12) are false; witness
  $\gamma=1/511$ at ratio $3/2$ (F1). "Such coefficients still have exact
  layers" (S10) is false; witness $\gamma=24/7$ (F2). Defect.
- **Circularity.** None. The descent uses Theorem 5.1 as an external
  premise; incompleteness is assumed only for contradiction and never
  fed back into Theorem 5.1's hypotheses. Pass.
- **Model and convention changes.** The set $A_{\alpha,\beta}$ of
  Hegyvári's conjecture (Fan's (1.9)) and the problem's indexed multiset
  are kept apart; the scaling reduction of S1 is proved (a subset whose
  strong completeness transfers upward); the Section 3 convention that
  the exact block has $\ell$ pairs at indices $n,\ldots,n+\ell-1$ with
  zero conversions at $n,\ldots,n+\ell-2$ is matched by $\ell=L'+1$ in
  (iv). Pass; note F7 on the Target paragraph's reliance on assessment
  text outside this read set.
- **Finite and statistical overreach.** Each certificate is claimed for
  its own pair only, and the a.e. statement rests on Borel's theorem, not
  on the sample. The sweep sentence S9 overclaims coverage: three of the
  thirty-two pairs are not certified by depth $9$ under the stated
  criterion (F3). Defect.
- **Uniformity.** $K_*(p,q)$ and $L(p,q)$ depend on the reduced ratio
  only and the section says so; the a.e. statement is stated per line
  and S12 explicitly disclaims uniformity over pairs. Pass.
- **Extremal conclusions.** The values $L(3,2)=8$, $L(5,4)=10$,
  $L(5,3)=9$ and the three $K_*$ recompute exactly; no sharpness is
  claimed for $L(p,q)$ (it is not sharp: at ratio $3/2$ a run of seven
  zeros with $\{2^s\gamma\}<1/192$ already yields $\ell\ge7$,
  $K\ge128\ge92$).
  The boundary of the excluded set is misplaced in S10 (F1). Defect in
  the obstruction text only.
- **Consequences and composition.** Every "hence" in S3--S7 was
  re-derived (Weakest steps). The composition Proposition 354.2 plus
  normalization plus reduction supplies each consumed clause at its
  stated strength. The lead's premise sentence about the filed reviews is
  contradicted (F4). Defect in the lead's standing prose only.
- **Computation.** Exact arithmetic reproduces every pinned figure of S8
  (depths, starting values and $b_n$) and both controls; the identity
  $\delta_s=q\lfloor px\rfloor-p\lfloor qx\rfloor$ with
  $x=\{2^s\gamma\}$, hence $\delta_s=0\iff x<1/p$, and the
  $(1,1),(1,0)$ two-event return at $3/2$ were checked on exact grids.
  The sweep fails for $d=23,89,91$ (F3). Defect.
- **Reproduction.** The lead's evidence is excluded from this review and
  was not run; the recomputation used only the criterion stated in Lemma
  354.4 and the normalization stated in S9. The pinned figures match to
  the digit, so the conventions agree; the sweep mismatch is recorded
  with exact figures for the integrator to rerun (F3).
- **Source and verdict fidelity.** $K_*$, $B_*$, $F$, $C_M$, (5.2),
  Theorem 5.1, Section 6's qualifying gap and Section 11.2's
  $\mathcal A,\mathcal S_k,\mathcal C_k$ match the held Yu--Chen text
  layer; Hegyvári's conjecture and the "exactly one dyadic" attribution
  match Fan v5 p. 4 and Yu--Chen p. 1; the 1991 dichotomy matches the
  held paper's Theorem (p. 7). The lead's characterization of the filed
  reviews does not match the commissioned premise (F4); the attribution
  of the incomplete multiset $(5/2,5)$ could not be checked (F8, note).

## Weakest steps

**W1: from a zero run of $\gamma$ to the Section 3 hypotheses**
(Proposition 354.2, (iii)--(iv)). Let $\{2^s\gamma\}<2^{-L}$ with
$L=L(p,q)$. Since $L\ge\lceil\log_2p\rceil$, $p\{2^s\gamma\}<p2^{-L}\le1$,
so $\{2^s\alpha\}=\{p\cdot2^s\gamma\}=p\{2^s\gamma\}$, and
$p\{2^s\gamma\}<p2^{-L}\le2^{\lceil\log_2p\rceil-L}=2^{-L_0}$
with $L_0=\lceil\log_2K_*\rceil-1$, and $\{2^s\beta\}=q\{2^s\gamma\}$ is
smaller still. The digits of $\alpha$ at positions $s+1,\ldots,s+L_0$
vanish exactly when $\{2^s\alpha\}<2^{-L_0}$, so $u_i=v_i=0$ for
$i\in[s,s+L_0)$: a common zero run of length $L_0\ge6$. Its maximal
extension $[s',s'+L'-1]$ is finite by (i), so the conversion at index
$s'+L'$ is nonzero. Exactness at $s'$: $q\alpha=p\beta$ gives
$\delta_{s'}=-q\{2^{s'}\alpha\}+p\{2^{s'}\beta\}$, and $L'\ge L_0>\log_2p$
gives $|\delta_{s'}|<p2^{-L'}<1$, so $\delta_{s'}=0$, $a_{s'}=dp$,
$b_{s'}=dq$ with $d=D_{s'}$ because $\gcd(p,q)=1$. The Section 3
hypotheses read: zero conversions at $n,\ldots,n+\ell-2$ and a nonzero
one at $n+\ell-1$. With $n=s'$ the zero indices are $s',\ldots,s'+L'-1$,
so $n+\ell-2=s'+L'-1$, $\ell=L'+1$, and the nonzero index is
$s'+L'=n+\ell-1$: the count is right, and
$K=2^{L'+1}\ge2^{L_0+1}=2^{\lceil\log_2K_*\rceil}\ge K_*$. Theorem 5.1
then applies at layer $s'$ with $r=s'+L'+4$. The step composes with (v)
because $r$ is explicit, so the next block can be chosen beyond it.

**W2: the descent chain** (Proposition 354.2, (v)). Infinitely many $s$
give infinitely many maximal common runs, since each maximal run is a
finite interval and contains only finitely many $s$. Choose
$s'_{j+1}\ge s'_j+L'_j+4$. Under incompleteness, every $h_{s'_j}\ge2$
(Theorem 5.1 gives completeness from $h\le1$), and Theorem 5.1 at block
$j$ gives $h_t\le h_{s'_j}-1$ for all $t\ge s'_j+L'_j+4$, in particular
$t=s'_{j+1}$: a strictly decreasing sequence of integers bounded below by
$2$. Nothing about monotonicity of $h_t$ between blocks is used, only the
permanent bound. The step is sound.

**W3: the transports of Lemma 354.1 and Corollary 354.3.** Step 2 of the
theorem page consumes: for consecutive events $n<m$ with
$m-n\ge2n+C_M$, zero conversions at $n,\ldots,m-2$ and a nonzero one at
$m-1$ (the definition of events), (5.2) to get $K\ge K_*$ from
$p\le a_n<2^n(M+1)$ and $K_*<16p^2$, Theorem 5.1, incompleteness to force
$h_n\ge2$ at every qualifying $n$, and the existence of a successor event
for every event. The only one of these that the irrational case supplied
through irrationality is the last, and "not both dyadic" supplies it: if
the conversions vanished from $n_0$ on, $\alpha=a_{n_0}2^{-n_0}$ and
$\beta=b_{n_0}2^{-n_0}$ would both be dyadic. Lemma 354.1 holds. For
Corollary 354.3, items 1--3 exclude the value $1$ for $2^k\alpha/\beta$,
which the hypothesis "not a power of $2$" does, and produce
$(2^u\alpha,2^v\beta)$ with $u-v=k$; the normalized pair's coefficient is
$2^v\beta/q=2^v\gamma$, whose fractional digits are those of $\gamma$
shifted left by $v$, so runs at positions $s+1,\ldots,s+L$ with $s\ge v$
become runs at positions $s-v+1,\ldots,s-v+L$; infinitely many survive
and non-dyadicity is preserved. The reduction then needs only items 3
and 4, which hold for every normalized pair. Sound.

## Strongest attack

- **S1.** Attempted to break the scaling reduction by a finite deletion:
  if $F$ is deleted from $A_{\alpha,\beta}$, then
  $A_{2^k\alpha,\beta}\setminus F\subseteq A_{\alpha,\beta}\setminus F$
  and completeness passes upward; and to break the Bézout step by
  $\gamma=0$: excluded since $\beta>0$. Failed.
- **S2.** Searched every premise page for a further use of
  irrationality: the normalization proof uses it to exclude the ratio
  $1$ and in item 5; the DB page's scope names the windows page; the FE
  page is unconditional; the BG page needs (10.2) and
  $\theta\notin\mathcal C_k$. No hidden use found. Failed.
- **S3 (Lemma 354.1).** Tried to find a hypothesis of Theorem 5.1 that a
  rational ratio violates: none, the theorem's inputs being the
  interlacing and the certificate. Tried to make the successor event
  fail: excluded by "not both dyadic". Failed.
- **S4 (Proposition 354.2).** Attacks: an off-by-one between the run
  length and $\ell$ (W1: exact); exactness asserted at $s$ rather than at
  the maximal run's start $s'$ (the run at $s'$ is longer, so (ii)
  applies at $s'$); the case where one of $\alpha,\beta$ is dyadic though
  $\gamma$ is not (nothing in (i)--(v) needs both non-dyadic, and then
  the run of the dyadic coefficient is infinite while the common run is
  still finite); a run of $\gamma$ inside its integer part (finitely
  many, irrelevant). A numerical sanity check on
  $(3072/511,2048/511)$ found maximal common zero runs of length $7$ at
  $s=8,17,26,\ldots$, all exact, $K=256\ge92$, and a Lemma 354.4
  certificate at depth $9$. Failed.
- **S5 (Corollary 354.3).** Attacks: $k<0$, where $\beta$ is scaled
  (handled by the shift, W3); the a.e. claim (normal numbers contain
  every block infinitely often, and normal implies non-dyadic). Failed.
- **S6.** Recomputed the constants; $K_*=92,132,120$ and $L=8,10,9$.
  Failed.
- **S7 (Lemma 354.4).** Attacks: the base case needs $c_0\le\Lambda_0$,
  which is the equality $b_n=b_n$; the inductive inequality
  $\Lambda_{j+1}\ge2c_j\ge c_{j+1}$ uses item 4 exactly; completeness of
  the set needs distinct values, which item 4 supplies; the multiset
  statement is the reduction with $F=\emptyset$. Failed.
- **S8.** Recomputed all pinned certificates: exact matches, including
  the least starting value of each certified interval; the control
  certifies at depth $6$ from $77$ with $b_6=286$; $(5/2,5)$ (not a
  normalized pair, all subset sums congruent to $0$ or $2$ modulo $5$)
  has no certificate to depth $16$. Failed.
- **S9.** Recomputed the sweep: $d=23,89,91$ are not certified by depth
  $9$ (F3). Succeeded.
- **S10.** Produced a rational $\gamma$ with infinitely many runs of
  $L(3,2)$ zeros ($\gamma=1/511$) and a bounded-run $\gamma$ with no
  exact layer ($\gamma=24/7$) (F1, F2). Succeeded.
- **S11.** Checked the good-rational bound $|\theta-p'/q'|\ge1/(qq')$,
  the membership $p/q\in\mathcal C_k$ (both $p/2^J$ and $q/2^J$ are sums
  of at most $k$ elements of $\mathcal A$ and $q/2^J>1/2$ because
  $q>p/2\ge2^{J-1}$), and the two-event return on an exact grid of
  $x\in[1/4,1/3)$: $u_s=\lfloor6x\rfloor=1$, $v_s=\lfloor4x\rfloor=1$,
  $u_{s+1}=\lfloor12x-2\rfloor=1$, $v_{s+1}=\lfloor8x-2\rfloor=0$,
  $\delta_{s+2}=4\delta_s+2\cdot3-3\cdot2=0$. Failed; wording note F5.
- **S12.** The "every pair with rational coefficients" clause falls with
  F1; the dichotomy sentence matches the held 1991 paper. Succeeded on
  the one clause.
- **S13.** Not a claim; the period statement is a period, not always
  the minimal one (note F6).
- **S14.** Inherits F1 through "bounded-run"; the transfer list itself
  stands. Wording note F6.
- **S15.** The gap paragraph inherits F1; the premise sentence F4.

## Premises

- Normalization page (`yu_chen_normalization_reconstruction.md`):
  items 1--6 and the reduction; interface confirmed: items 1--3 use
  irrationality only to exclude the value $1$; item 5 uses only that the
  conversions are not eventually zero; items 4 and 6 and the reduction
  hold for every normalized pair. Read in full.
- Theorem 5.1 page (`yu_chen_theorem_5_1_reconstruction.md`): hypotheses
  of Section 3 (layer $n\ge0$, $a_n=dp$, $b_n=dq$, $\gcd(p,q)=1$, zero
  conversions at $n,\ldots,n+\ell-2$, nonzero at $n+\ell-1$,
  $K=2^\ell\ge K_*=2q(p-1)+4(p+q)+64$), conclusion
  $h_t\le\max(0,h_n-1)$ for $t\ge n+\ell+3$ and completeness if
  $h_n\le1$; (5.2) with $C_M=16(M+1)^2$. Its scope statement (inputs:
  the three lemmas, the certificate, the interlacing) was checked against
  the proof. Read in full; the certificate table itself not reread.
- Theorem page (`yu_chen_theorem_reconstruction.md`): Step 2 (bounded
  spacing with $R=4$) and its inputs as listed in W3. Read in full.
- Lemma 2.2 page: the consequence for weights $c_{i+1}\le2c_i$ with
  initial span at least $c_1$. Lemmas 2.1 and 2.3: read for the
  interfaces Theorem 5.1 cites. Read in full.
- FE page: (FE) and (FE-R) unconditional for normalized pairs. DB page:
  (DB) needs incompleteness, $n\ge1$ and a good denominator at least
  $2^n\beta$. Windows page: $D(b)$ and (10.2) need incompleteness and
  irrationality. BG page: the sets $\mathcal A,\mathcal S_k,\mathcal C_k$
  and Step 2's need for $\theta\notin\mathcal C_k$. All read in full.
- External: Borel's normal number theorem (imported by the section;
  standard, not reproved here). Dirichlet's theorem is not used by the
  section.
- Sources: Yu--Chen manuscript, held; text layer read at pp. 1--7 and
  13--14 (definitions, Section 3, Theorem 5.1, (5.2), Section 6, Section
  11.2). Fan, arXiv:2607.14071 v5, held; p. 4 and p. 20 read. Hegyvári
  1991, held; pp. 7--9 read (the Theorem, Lemmas 1--2). Hegyvári 1989,
  not held; the "exactly one dyadic" case is attested only through Fan
  p. 4 and Yu--Chen p. 1.
- Assumptions of this review: the reconstruction pages are established at
  their reviewed standing (commissioned premise); the lead's evidence is
  excluded, so its criterion and outputs are unknown here.

## Findings

**F1 (required).** Location: section, "What it does not give", first
bullet, "every rational $\gamma$, whose expansion is eventually periodic,
and uncountably many irrationals have bounded runs. For them the descent
has no long exact block to act on, and Hegyvári's conjecture stays open
except pair by pair through Lemma 354.4"; third bullet, "the exceptional
set contains every pair with rational coefficients"; the Outcome's "open
for the bounded-run coefficients"; lead, "The consequential gap",
"Coefficients $\gamma$ whose binary expansion has bounded zero runs:
every rational $\gamma$ (eventually periodic expansion) ... For them the
exact blocks after exact layers are too short for Theorem 5.1 ...
Hegyvári's conjecture therefore stays open for these coefficients".
Defect: bounded zero runs do not exclude a coefficient from Proposition
354.2, whose hypothesis is infinitely many runs of the fixed length
$L(p,q)$; a coefficient with runs bounded by $L(p,q)$ and infinitely many
runs of exactly $L(p,q)$ satisfies it, and rational coefficients of this
kind exist. Witness: $\gamma=1/511$ at ratio $3/2$. Since $2^9\equiv1$
modulo $511$, the expansion is $0.(000000001)$ repeated: infinitely many
runs of exactly eight zeros, $L(3,2)=8$, and $\gamma$ is not dyadic
($511=7\cdot73$). Corollary 354.3 with $k=0$, $p/q=3/2$, $\gamma=\beta/2$
makes $A_{3/511,2/511}$ strongly complete; this pair has rational
coefficients, ratio $3/2$ and no dyadic coefficient, so it lies in the
class the page calls open. Mechanism check on the normalized pair
$(3072/511,2048/511)$ ($N=4$, $M=6$): maximal common zero runs of length
$7$ start at $s=8,17,26,\ldots$, each exact, so $\ell=8$ and
$K=256\ge92$; a Lemma 354.4 certificate exists at depth $9$ from $516$
with $b_9=2052$. Likewise $\gamma=1/257$ (period $16$, eight zeros then
eight ones), whose normalized pair $(1536/257,1024/257)$ certifies at
depth $5$ from $41$ with $b_5=127$; and every $\gamma=1/v$ with odd
$v>256$, since $\{2^s/v\}=1/v<2^{-8}$ whenever $2^s\equiv1$ modulo $v$.
What is true: for $\gamma=m/v$ in lowest terms with $v$ odd,
$\{2^s\gamma\}\ge1/v$, so a zero run of length $R$ forces $v>2^R$; a
qualifying block needs a common zero run of length
$\lceil\log_2K_*\rceil-1$ at an exact layer, hence
$\{2^s\gamma\}<2^{-\lceil\log_2K_*\rceil}$, hence
$v>2^{\lceil\log_2K_*\rceil}$ ($v>128$ at ratio $3/2$). Proposed
replacement for the first bullet: "The short-block coefficients.
Proposition 354.2 acts through a common zero run of the conversions of
length at least $\lceil\log_2K_*\rceil-1$ at an exact layer, which a run
of $L(p,q)$ zeros in $\gamma$ guarantees; a coefficient with only
finitely many such common runs is outside the descent. For a rational
$\gamma=m/v$ in lowest terms with $v$ odd, $\{2^s\gamma\}\ge1/v$, so a
zero run of length $R$ forces $v>2^R$: every rational $\gamma$ with
$v\le2^{\lceil\log_2K_*\rceil}$ ($v\le128$ at ratio $3/2$), in
particular every pair certified below, and uncountably many irrationals
are outside, while $\gamma=1/511$ at ratio $3/2$ has infinitely many runs
of eight zeros and is covered by Corollary 354.3. For the coefficients
outside, Hegyvári's conjecture stays open except pair by pair through
Lemma 354.4." For the third bullet: "the exceptional set contains every
pair whose $\gamma$ has an odd denominator at most
$2^{\lceil\log_2K_*\rceil}$". The Outcome, the lead's gap paragraph and
the lead's `desc` ("the bounded-run coefficients as the remaining gap")
change accordingly.

**F2 (required).** Location: section, first bullet, "Since
$\{2^s\gamma\}<1/p$ is exactly the condition $\delta_s=0$, such
coefficients still have exact layers, but the blocks after them have
length below $\log_2K_*$"; lead, "the exact blocks after exact layers are
too short for Theorem 5.1". Defect: the equivalence is correct
($\delta_s=q\lfloor px\rfloor-p\lfloor qx\rfloor$ with
$x=\{2^s\gamma\}$, zero exactly when $\lfloor px\rfloor=0$), but it does
not give existence: a bounded-run coefficient may have no exact layer.
Witness: $\gamma=24/7$ at ratio $3/2$, normalized pair $(72/7,48/7)$
($N=6$, $M=10$). The doubling orbit of $\{\gamma\}=3/7$ is
$\{3/7,6/7,5/7\}$, all at least $1/3$, so $\{2^s\gamma\}<1/3$ never
holds; $\delta_s=2a_s-3b_s$ takes the values $2,1,1$ periodically and is
never $0$. The obstruction survives (with no exact layer Theorem 5.1 has
even less to act on), but the sentence is false. Proposed replacement:
"exact layers occur exactly at the $s$ with $\{2^s\gamma\}<1/p$, possibly
nowhere ($\gamma=24/7$ at ratio $3/2$ has none), and where they occur the
common zero runs after them are too short for Theorem 5.1, which needs
$K\ge K_*$ for its coefficient interval (Step 1) and node connection
(Step 4)".

**F3 (required).** Location: section, after Lemma 354.4, "and every pair
$(3\gamma,2\gamma)$ with $\gamma=2^T/d$ for the thirty-two odd
denominators $5\le d\le99$ not divisible by $3$, normalized by the least
$T$, by depth $9$"; lead, "thirty-two further pairs $(3\gamma,2\gamma)$
with $\gamma=2^T/d$". Defect: under the criterion of Lemma 354.4 ($P_n$
contains $b_n$ consecutive integers for some $n\le9$) and the least $T$
making $(3\cdot2^T/d,2\cdot2^T/d)$ normalized, exact recomputation
certifies twenty-nine of the thirty-two pairs by depth $9$ and not the
other three. Witness: $d=23$, $T=6$, pair $(192/23,128/23)$: the longest
run of consecutive integers in $P_9$ has length $2826$ (from $2139$)
against $b_9=2849$; the first certificate is at depth $10$ from $2139$
with $b_{10}=5698$. $d=89$, $T=8$, pair $(768/89,512/89)$: the longest
run in $P_9$ has length $22$ against $b_9=2945$; first certificate at
depth $12$ from $11036$ with $b_{12}=23563$. $d=91$, $T=8$, pair
$(768/91,512/91)$: the longest run in $P_9$ has length $22$ against
$b_9=2880$; first certificate at depth $11$ from $4323$ with
$b_{11}=11522$. Larger $T$ (up to $10$) gives no certificate to depth
$12$ for any of the three. The same code reproduces every pinned figure
of S8 to the digit, and the $d=23$ and $d=5$ cases were cross-checked
with a set-based implementation, so the conventions agree with the
section's. The lead's evidence was not read; if it applies another
criterion or normalization, the sentence must say which. Proposed
replacement: "by depth $12$" after the evidence is rerun to that depth,
or "twenty-nine of them by depth $9$, and $d=23,89,91$ at depths $10$,
$12$ and $11$".

**F4 (suggested).** Location: lead, "Provisional premises", "the
manuscript is unrefereed and the reconstruction of that page is not among
the filed reviews". Defect: the commissioned premise of this review is
that the reconstruction pages were independently reviewed as of
2026-09-28T05:03:27Z, and the folder listing as of 2026-09-28T13:50:48Z (file
names only, see Exposures) contains one review file per reconstruction page,
including the Theorem 5.1 page. The sentence understates the premise's standing;
its content and verdict were not read here. Proposed replacement: name the
review's standing as the folder records it, or drop the clause.

**F5 (note).** Location: section, second bullet, "Under a rational ratio
the bounded event spacing of Lemma 354.1 is therefore not contradictory
by itself"; lead, "a rational ratio lies in the compact set
$\mathcal C_k$". The first sentence asserts that the reconstructed
bounded-spacing argument yields no contradiction, not that bounded
spacing, incompleteness and a rational ratio are jointly consistent
(which would be a counterexample to the conjecture); "the argument of
the bounded-spacing page yields no contradiction from it" is the
supportable form. The second should carry its quantifier: "lies in
$\mathcal C_k$ for every $k$ at least the number of binary ones in $p$
and in $q$".

**F6 (note).** Location: section, "Outcome", "Lemma 354.1 for every
non-dyadic normalized pair"; "Next investigation", "eventually periodic
with period the order of $2$ modulo $v$". The first is ambiguous
shorthand for "not consisting of two dyadic rationals" (the lead states
it correctly). The second names a period; the minimal period of the
joint conversion sequence divides it (for $\gamma=1/3$ at ratio $3/2$ the
$u_i$ are constant).

**F7 (note).** Location: section, "Target", "so the open cases are those
with $\alpha/\beta$ rational, not a power of $2$, and neither coefficient
a dyadic rational". The deduction treats the irrational-ratio case of the
conjecture (completeness of the set $A_{\alpha,\beta}$) as closed by the
site-accepted answer to the first question (the indexed multiset). The
multiset-to-set bridge is not automatic when a value is shared by the two
rays, though it holds for a proof that gives strong completeness of the
tails. The Current assessment that the sentence paraphrases is outside
this read set; the integrator should confirm what the accepted proof
states. The section's own results do not depend on this sentence.

**F8 (note).** Location: section, "Hegyvári's incomplete multiset
$(5/2,5)$ receives no certificate to depth $16$, as it must not". The
multiset is incomplete (every subset sum is congruent to $0$ or $2$
modulo $5$), but the attribution could not be checked from the read set
(the 1989 paper is not held), and $(5/2,5)$ is not a normalized pair
($\lfloor5/2\rfloor<\lfloor5\rfloor$), so Lemma 354.4 does not apply to
it; the control tests only the search's negative path.

## Verdict

- S1: refutation-failed (with note F7 on the assessment-dependent
  clause).
- S2: refutation-failed.
- S3 (Lemma 354.1): refutation-failed.
- S4 (Proposition 354.2): refutation-failed.
- S5 (Corollary 354.3): refutation-failed.
- S6 (constants and the outside-proved-cases sentence):
  refutation-failed.
- S7 (Lemma 354.4): refutation-failed.
- S8 (pinned certificates and controls): refutation-failed.
- S9 (the depth-nine sweep): refuted-as-stated (F3).
- S10 (obstruction 1): refuted-as-stated (F1, F2); the obstruction it
  intends, that coefficients with only short common zero runs are outside
  Theorem 5.1's reach, stands once restated.
- S11 (obstruction 2): refutation-failed (wording note F5).
- S12 (obstruction 3): the rational-coefficients clause
  refuted-as-stated (F1); the uniformity and dichotomy clauses
  refutation-failed.
- S13 (next investigation): not a claim.
- S14 (outcome): refutation-failed for the transfer list; its
  "bounded-run" clause inherits F1.
- S15 (lead): the route summary refutation-failed; the consequential-gap
  paragraph refuted-as-stated (F1); the premise sentence on the filed
  reviews is not a mathematical claim and is contradicted by the
  commissioned premise (F4).

**Limitations.** The lead's evidence and every filed review were excluded
and not read; the recomputation used the criterion stated on the page.
The Current assessment of Problem 354 was not read, so the Target
paragraph's case split was checked only against the sources named. The
Hegyvári 1989 paper is not held. Theorem 5.1 and the other reconstruction
pages were taken as premises at their reviewed standing and their proofs
were not re-verified beyond their interfaces. This focused review assigns
no tier and changes no status.

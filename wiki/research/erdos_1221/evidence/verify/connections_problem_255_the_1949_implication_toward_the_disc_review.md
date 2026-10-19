---
name: research/erdos_1221/evidence/verify/connections_problem_255_the_1949_implication_toward_the_disc_review
title: "Independent review of the connections section: Problem 255: the 1949 implication toward the discrepancy theorem"
desc: |
  Refutation review of Proposition 255.1 and the section's transfer,
  obstruction, dependency and conditional sentences as they stood on
  2026-09-28T13:50:48Z: all twelve restated statements are refutation-failed;
  zero required corrections, one suggested wording repair and four notes.
created: 2026-09-28T19:13:42Z
updated: 2026-09-28T19:13:42Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context, given only the
assignment text; the reviewer took no part in writing the connections
page, the reconstruction pages, the problem page or the library cards, and
had no contact with their author. Charge: refutation. The review is
noncomputational; no code was written or run.

**Subject.** Page `wiki/research/erdos_1221/connections.md` as it stood on
2026-09-28T13:50:48Z, section "Problem 255: the 1949 implication toward the
discrepancy theorem", lines 45--194 (the H2 heading at line 45 through the line
before the next H2 at line 195). No lead page is named for this section. The
page's shared preamble (purpose and standing, notation; lines 1--43) was read as
the source of the conventions the section uses.

**Reading.**

- The section, clause by clause; Proposition 255.1 re-derived in full.
- Reconstruction pages in the same state, read in full as premises:
  [[research/erdos_1221/ko26b_lemma_4_2_reconstruction|Lemma 4.2 with Theorem 4.1]],
  [[research/erdos_1221/ko26b_theorem_1_1_reconstruction|Theorem 1.1 of the 2026 preprint]],
  [[research/erdos_1221/ko26a_theorem_1_1_reconstruction|Theorem 1.1 of the 2026 note]],
  [[research/erdos_1221/ko26b_proposition_3_1_reconstruction|Proposition 3.1]],
  [[research/erdos_1221/ko26b_lemma_7_2_reconstruction|Lemma 7.2 with Theorem 7.1]] and
  [[research/erdos_1221/dber49_inequality_5_7_reconstruction|(5.1) and (5.7)]].
- [[problems/discrepancy/E0255/_index|Problem 255]]: the Statement section.
- Library: the
  [[../library/analysis/debruijn_erdos_1949_sequences_points_circle/_index|1949 card]]
  (provenance and contents) and its
  [[../library/analysis/debruijn_erdos_1949_sequences_points_circle/conjecture_p17|conjecture page]];
  the 1949 PDF on its page images for printed pp. 14 and 17; the
  [[../library/discrepancy/schmidt_1972_irregularities_distribution/_index|Schmidt 1972 card]]
  and that PDF's introduction (pp. 63--64) and reference list; the
  [[../library/analysis/korsky_2026_resolution_debruijn_erdos_consecutive_gap_problem/_index|Korsky 2026 card]]
  (provenance paragraph), its Theorem 1.1 result page (statement section)
  and that PDF's Section 4 (Theorem 4.1, its derivation, Lemma 4.2),
  Theorem 7.1 and references [9]--[11], as the source of the imported
  theorems the section names; the library tree listing, to confirm which
  sources are held.
- `docs/verification.md` (Grading and claim standing, Audit checklist,
  Whole-claim report and the Erdos-specific checklist),
  `docs/approach_vetting.md`, `docs/evidence.md` "Source fidelity" and
  `docs/math_authoring.md`.

**Exposure.** The problem page E0255 is short and was read whole, so its
Current assessment, Progress, Known Results and generated library-links
block reached the reviewer in addition to the Statement; the Progress
paragraph summarizes the transfer under review. No finding rests on that
text; the section's description of the page was checked only against the
Statement and the reference block. No evidence folder, review, grade,
folder index, workspace file or web source was read.

## Restatement

Conventions (from the page's preamble, confirmed against Section 1 of the
1949 note on p. 14). A sequence $a=(a_1,a_2,\ldots)$ on the circle
$\mathbb T$ of circumference $1$, coincident terms allowed; the first $n$
terms cut $n$ gaps, of length $0$ between coincident terms; an $r$-span is
the sum of $r$ cyclically consecutive gaps; $M_n^r(a)$ and $m_n^r(a)$ are
the largest and smallest $r$-spans; $\Lambda_r(a)=\limsup_n nM_n^r(a)$,
$\lambda_r(a)=\liminf_n nm_n^r(a)$ and $\mu_r(a)=\limsup_n M_n^r(a)/m_n^r(a)$;
$\Lambda_r=\inf_a\Lambda_r(a)$, $\lambda_r=\sup_a\lambda_r(a)$ and
$\mu_r=\inf_a\mu_r(a)$ over all sequences. For an arc $I$,
$N_n(I)=\#\{i\le n:\ a_i\in I\}$ counts indices with multiplicity and
$D_n(I)=N_n(I)-n|I|$. The mean-normalized conjecture says that
$\Lambda_r-r$, $r-\lambda_r$ and $r(\mu_r-1)$ tend to infinity with $r$.

- **S1 (Proposition 255.1, displayed bounds).** For every sequence $a$
  on $\mathbb T$, coincident terms allowed, and every real $K$ such that
  $|D_n(I)|\le K$ for every $n\ge1$ and every half-open arc $I$: for every
  integer $r\ge1$ and every integer $n>r$, $nM_n^r(a)\le r+K-1$ and
  $nm_n^r(a)\ge r-K+1$.
- **S2 (Proposition 255.1, consequences).** Under the hypothesis of S1:
  for every $r\ge1$, $\Lambda_r-r\le\Lambda_r(a)-r\le K-1$ and
  $r-\lambda_r\le r-\lambda_r(a)\le K-1$; for every $r\ge K$,
  $r(\mu_r-1)\le r(\mu_r(a)-1)\le 2(K-1)r/(r-K+1)$, and the right side
  tends to $2(K-1)$ as $r\to\infty$; so the three mean-normalized
  expressions are bounded in $r$.
- **S3 (the implication).** Each single part of the mean-normalized
  conjecture implies that no sequence on $\mathbb T$ has $\sup_I|D_n(I)|$,
  over half-open arcs $I$, bounded in $n$; a bound $K$ on
  $|D_n([0,\alpha))|$ for all $\alpha$ and $n$ gives the bound $2K$ on
  every arc and conversely; so the conclusion is the 1945 theorem, that no
  sequence has $\sup_\alpha|D_n([0,\alpha))|$ bounded in $n$.
- **S4 (passage between arc types).** If $|D_n(I)|\le K$ for all
  half-open arcs at stage $n$, then also for open and closed arcs and for
  complements of arcs; and $K\ge1$.
- **S5 (obstruction: no fixed interval).** The conclusion of S3 is
  $\limsup_n\sup_I|D_n(I)|=\infty$; the fixed-interval conclusion of
  Problem 255, one $I$ with $\limsup_n|D_n(I)|=\infty$, is not reached by
  this proof, and no page of the folder bears on the passage from a
  moving arc to a fixed one.
- **S6 (obstruction: no rate).** With a nondecreasing $K(n)\to\infty$ in
  place of $K$ the same proof gives $nM_n^r(a)\le r+K(n)-1$ and
  $nm_n^r(a)\ge r-K(n)+1$ at each stage; through Proposition 255.1 no
  growth rate of the discrepancy in $n$ follows from the conjecture and
  none feeds it; coupling $r$ to a point count is what Lemma 4.2 of the
  2026 preprint adds.
- **S7 (circularity of the only route to the premise).** The fixed-$r$
  lower bounds (5.7) and Theorem 1.1 of the 2026 note give values of
  $r(\mu_r-1)$ bounded in $r$; the growth is claimed only by Theorem 1.1
  of the 2026 preprint, whose ratio part consumes Theorem 4.1 (a
  finite-list form of Schmidt's theorem with the constant $1/16$, derived
  by the source from Larcher's proof) and whose one-sided parts consume
  Halász's planar $L^1$ theorem; deriving the 1945 theorem from that claim
  through Proposition 255.1 proves nothing new; a proof of one part that
  avoids discrepancy lower bounds would give a new proof of the 1945
  theorem, and none is in the sources read.
- **S8 (scope).** The 2026 claim is over sequences of distinct points, so
  through Proposition 255.1 it would exclude only just-distributed
  sequences of distinct points.
- **S9 (reverse edge).** Lemma 4.2 turns the bound (3.1) of Proposition
  3.1 into a list of $\lfloor S\rfloor$ points all of whose prefixes have
  counting error at most $B$, and Theorem 4.1 supplies the contradiction;
  Lemma 7.2 does the same with Halász's theorem; Schmidt's part VI (held)
  is a different theorem from the planar theorem of part VII; neither part
  VII, Larcher 2015 nor Halász 1981 is held.
- **S10 (next investigation, conditional).** Filing Larcher 2015 and
  Halász 1981 and checking the two imported statements as used would, if
  positive, close the two import gaps; if negative, leave the growth
  statement of the ratio part standing through part VII with an
  unspecified constant and remove the warrant for the coefficient
  $1/100$; neither outcome changes Problem 255.
- **S11 (target and source characterizations).** Problem 255 asks whether
  every sequence in $[0,1]$ has an interval $I$ with
  $\limsup_N|D_N(I)|=\infty$; Schmidt's part VI shows that the set of
  $\alpha$ with $D_n([0,\alpha))$ bounded is countable; the remark on
  p. 14 of the 1949 note says that the 1945 theorem would follow from the
  conjecture that $r(\mu_r-1)$ is unbounded.
- **S12 (outcome).** The remark transfers as an implication; it yields
  nothing new for Problem 255, which is proved and stronger; the
  mathematical dependency runs the other way.

## Checklist

- **Quantifiers and scope.** Pass. S1 is universal in the sequence, in
  $r\ge1$ and in $n>r$ with one $K$; S2's third bound carries its explicit
  range $r\ge K$; S3 names the mean-normalized reading, under which each
  part is a limit statement in $r$; S8 discloses the distinct-point
  restriction of the 2026 claim. The one loose spot is "stay bounded" for
  the third expression over the finitely many $r<K$, which the displays
  do not cover (F2; the statement is true).
- **Circularity.** Pass. Proposition 255.1 uses no discrepancy theorem
  and no statement equivalent to its conclusion. The section's own
  circularity claim (S7) was checked from the other side: each imported
  input of the 2026 route implies the 1945 theorem directly (Strongest
  attack, S7).
- **Model and convention changes.** Pass. The 1949 family (numbers mod
  $1$, coincidences allowed), the proposition's family and the counting
  with multiplicity agree; the passage between half-open, open, closed
  and wrapping arcs is proved (S4); the identification of the unit
  interval of Problem 255 and of the 1945 theorem with the circle affects
  only terms equal to $1$ and is harmless (Weakest step 3, F5).
- **Finite and statistical overreach.** Inapplicable: no finite
  verification, sampling or heuristic enters.
- **Uniformity.** Pass. One constant $K$ serves every $n$ and every arc;
  the bounds of S1 hold for all $r$ with the same $K$; the limit $2(K-1)$
  is a limit in $r$ at fixed $K$; S6 correctly states that a
  stage-dependent $K(n)$ gives no control of the limits in $n$ (its
  wording is the subject of F1).
- **Extremal conclusions.** Pass. The directions
  $\Lambda_r\le\Lambda_r(a)$, $\lambda_r\ge\lambda_r(a)$ and
  $\mu_r\le\mu_r(a)$ follow from the definitions as infimum, supremum and
  infimum; finiteness of $\mu_r$ for $r<K$ is supplied here (Weakest
  step 2).
- **Consequences and composition.** Pass with notes. Every "hence" was
  checked separately (Strongest attack). The imported statements are
  consumed at exactly the strength the premise pages state; the
  description of Theorem 4.1 as a quantitative form of "the proved
  conclusion of Problem 255" names the wrong statement (F3), and "the
  only claimed proof" is a literature claim (F4).
- **Computation.** Inapplicable beyond hand arithmetic: the identity
  $(r+K-1)/(r-K+1)=1+2(K-1)/(r-K+1)$ and the monotonicity of
  $r/(r-K+1)$ on $r\ge K$ were checked by hand.
- **Reproduction.** Inapplicable: the section carries no evidence code,
  rerun line or coverage claim.
- **Source and verdict fidelity.** Pass. The p. 14 remark and the Section
  6 wording were read on the 1949 page images; Schmidt's definitions
  ($Z(n,\alpha)$ counts $\xi_i<\alpha$, $D(n,\alpha)=|Z(n,\alpha)-n\alpha|$),
  the corollary (at most countable) and the attribution of the
  measure-zero result to part I (Quart. J. Math. 19 (1968), 181--191)
  were read on the held part VI; Theorem 4.1, its derivation, Lemma 4.2,
  Theorem 7.1 and the references to Schmidt VII, Halász 1981 and Larcher
  2015 were read in the held 2026 preprint and agree with the section's
  citations. The 1945 paper is not held; the section's statement of its
  content matches the held part VI's introduction, which it does not cite
  (F5). Every standing sentence says author-recorded and nothing more.

## Weakest steps

**1. The two counts inside a span (S1).** Fix $r\ge1$ and $n>r$. Order
the first $n$ terms cyclically by position, coincident terms by index, as
entries $e_1,\ldots,e_n$; the gap $g_k$ is the clockwise distance from the
position of $e_k$ to that of $e_{k+1}$ (indices mod $n$), zero between
coincident entries, and $\sum_kg_k=1$. The $r$-span starting at $p=e_k$
has length $|J|=g_k+\cdots+g_{k+r-1}\in[0,1]$, the clockwise distance
from $p$ to $q=e_{k+r}$, and $q\ne p$ as entries because $0<r<n$. Let $U$
be the open clockwise arc of length $|J|$ from the position of $p$ (empty
when $|J|=0$; the circle minus that position when $|J|=1$) and $V$ the
closed one (a point; the whole circle). The entries
$e_{k+1},\ldots,e_{k+r-1}$ are the only entries other than $p$ and $q$
whose positions can lie in $U$: every other entry has its position on the
closed complementary arc from $q$ back to $p$, which is disjoint from $U$
(when $|J|=1$ that complementary arc is the single position of $p$,
excluded from $U$). So $N_n(U)\le r-1$, and with $D_n(U)\ge-K$ from S4,
$n|J|\le N_n(U)+K\le r-1+K$; when $|J|=0$ this reads $0\le K$. The $r+1$
entries $e_k,\ldots,e_{k+r}$ are distinct, as $r+1\le n$, and their
positions lie in $V$, so $N_n(V)\ge r+1$, and $D_n(V)\le K$ gives
$r+1-n|J|\le K$. Taking the largest and the smallest span gives S1. Both
counts are exact in the worst case (all $r-1$ inner entries strictly
inside, no extra coincidences), so the bounds cannot be sharpened without
more hypotheses. Composition: S1 feeds S2 stage by stage, with
$n\to\infty$ taken only afterwards, so the $K(n)$ variant of S6 is
immediate.

**2. The ratio bound and the range $r<K$ (S2).** For $r\ge K$ and $n>r$,
S1 gives $m_n^r(a)\ge(r-K+1)/n\ge1/n>0$, so every span ratio at stage
$n$ is finite and
$M_n^r(a)/m_n^r(a)\le(r+K-1)/(r-K+1)=1+2(K-1)/(r-K+1)$; the upper limit
in $n$ obeys the same bound, and multiplying by $r$ gives the display. On
$r\ge K$ the factor $r/(r-K+1)$ is nonincreasing (its derivative has the
sign of $1-K\le0$, by $K\ge1$ from S4), so the bound is at most $2K(K-1)$
there and tends to $2(K-1)$. The section's "stay bounded" also needs
$r(\mu_r-1)<\infty$ for the finitely many $r<K$, which the displays do
not give. It holds: for the note's Section 2 sequence
$b_k=\log_2(2k-1)$ reduced mod $1$ the gaps at stage $n$ are
$\log_2((j+1)/j)$ for $n\le j\le2n-1$ (p. 14 of the note), so
$M_n^1(b)/m_n^1(b)\to2$, and every $r$-span lies between $rm_n^1(b)$ and
$rM_n^1(b)$, whence $\mu_r\le\mu_r(b)\le2$ and $r(\mu_r-1)\le r$ for
every $r$. For the "tend to infinity" form of the conjecture the tail
$r\ge K$ alone suffices. Recorded as F2.

**3. From arcs on the circle to the 1945 theorem (S3).** Identify
$\mathbb T$ with $[0,1)$. For $0\le\alpha\le\beta\le1$,
$[0,\beta)\setminus[0,\alpha)=[\alpha,\beta)$ has length $\beta-\alpha$,
so $D_n([\alpha,\beta))=D_n([0,\beta))-D_n([0,\alpha))$ exactly and the
anchored bound $K$ gives $2K$; a wrapping half-open arc is the complement
of such an arc, with counting error of opposite sign; the other endpoint
type $(\alpha,\beta]$ is the limit of
$[\alpha+\varepsilon,\beta+\varepsilon)$, which has the same terms and
the same length for small $\varepsilon$. Conversely $[0,\alpha)$ is a
half-open arc. The 1945 theorem as the held part VI states it (p. 63):
$Z(n,\alpha)$ counts $i\le n$ with $\xi_i<\alpha$, and
$D(n)=\sup_\alpha|Z(n,\alpha)-n\alpha|$ cannot remain bounded, for a
sequence in the unit interval. The section's proposition lives on the
circle. A sequence in $[0,1)$ is a sequence on $\mathbb T$ with the same
anchored counts. A sequence in $[0,1]$ with bounded counting error $K$ on
intervals has at most $K$ terms equal to $1$ in all (the closed interval
$[1,1]$ has counting error equal to that count), so moving them to $0$
changes every count by at most $K$ and preserves boundedness; hence the
circle statement and the interval statement are equivalent, and S3 is
the 1945 theorem. Recorded as F5 (a missing clause, not a gap).

## Strongest attack

- **S1.** Constructed the extreme configurations the proof must survive:
  all $n=r+1$ terms coincident (spans of length $1$ and $0$; the bounds
  demand $K\ge n$, and a short arc around the common position at stage
  $n$ indeed forces $K\ge n$); a span wrapping the whole circle ($|J|=1$,
  $U$ the circle minus a point, $V$ the circle with $D_n(\mathbb T)=0$);
  a span of length $0$; entries coincident with $p$ or $q$ but outside the
  block $e_k,\ldots,e_{k+r}$ (they lie in $V$, not in $U$, and only
  help); non-integer $K$; the stage $n=r+1$ where the block is the whole
  list. Equally spaced points at one stage with $K=1$ force every span to
  equal $r/n$, which the bounds reproduce exactly. No configuration
  violates either bound. Failed.
- **S2, S3.** Tried the literal reading of the conjecture: there
  $r(1-\lambda_r)\to-\infty$, so the second literal part is false and
  implies anything; the section names the mean-normalized reading, and
  the third expression is the same under both, so nothing is gained.
  Tried the range $r<K$ for the third expression (closed in Weakest
  step 2). Tried the wrapping arcs and the endpoint types in the
  factor-$2$ equivalence, and the interval-versus-circle setting (closed
  in Weakest step 3). Failed.
- **S4.** Tried the degenerate arcs: the empty arc and the whole circle
  have counting error $0$; the closed single point $[x,x]$ has error equal
  to the multiplicity at $x$, bounded by $K$ through the passage from
  $(x-\varepsilon,x]$. The bound $K\ge1$ comes from $[a_1,a_1+\varepsilon)$
  at $n=1$. Failed.
- **S5.** The obstruction is a scope statement (the arcs used are the
  spans of stage $n$ and move with $n$) and claims no impossibility; the
  equivalence of "no $K$" with $\limsup_n\sup_I|D_n(I)|=\infty$ holds
  because $\sup_I|D_n(I)|\le n$ is finite at each stage. The
  reconstruction pages read concern spans and short arcs only, so the
  sentence that no page of the folder bears on the fixed-interval passage
  is accurate. Failed.
- **S6.** Tried to make the stage-$n$ bounds with $K(n)$ say something
  after all: with $K(n)=\lceil\log n\rceil$ and $r=1$ the upper bound
  $nM_n^1(a)\le\log n+1$ is a genuine constraint at every stage, so the
  clause "say nothing once $K(n)>r$" is literally false for the upper
  bound; but the bullet's claim, that Proposition 255.1 transmits no rate
  into or out of the limits $\Lambda_r$, $\lambda_r$, $\mu_r$, stands,
  because $\sup_n(r+K(n)-1)=\infty$. The unqualified "nor feeds the
  conjecture" contradicts the section's own reverse edge unless read as
  "through Proposition 255.1". Wording, not mathematics: F1. Failed as a
  claim about the proposition.
- **S7.** Tried to break the circularity claim by asking whether either
  imported input is weaker than the 1945 theorem. Theorem 4.1 as used: if
  a sequence in $[0,1)$ had $|Z(n,u)-nu|\le K$ for all $n$ and $u$, every
  prefix list of length $L$ would have $H_L\le K$, against
  $H_L\ge\frac1{16}\log L$ for $L\ge L_0$; so Theorem 4.1 implies the 1945
  theorem outright. Halász's theorem as used: for a list $z_1,\ldots,z_L$
  the planar set $\{(z_i,i/L)\}$ has $|D_{\mathcal P}(u,v)|\le H_L+1$ for
  all $(u,v)$ (the count in the box is $Z(\lfloor Lv\rfloor,u)$ up to the
  endpoint convention, which does not change the supremum, and
  $|\lfloor Lv\rfloor u-Luv|\le1$), so its $L^1$ norm is at most $H_L+1$
  and $H_L\ge c_H\sqrt{\log L}-1$, which again implies the 1945 theorem.
  Both inputs are strictly stronger than the conclusion, so the
  derivation through Proposition 255.1 is circular as the section says.
  The values $r(\mu_r-1)\ge1$ from (5.7) and $r(\mu_r-1)\ge1+1/(r^2-1)$,
  at most $4/3$, from the 2026 note are bounded, as stated. The word
  "only" is a literature claim (F4). Failed.
- **S8.** Tried to extend the exclusion to coincident sequences by
  perturbation; the section does not claim this and defers it to the
  Problem 1221 section, so there is nothing to refute. Failed.
- **S9.** Checked the interfaces against the Lemma 4.2, Proposition 3.1
  and Lemma 7.2 pages (they match) and the library tree (no Schmidt VII,
  no Larcher, no Halász 1981; the held Halász papers are the 1973 random
  polynomial paper and the 1977 concentration-function paper). The phrase
  "quantitative form of the proved conclusion of Problem 255" names the
  wrong statement (F3). Failed.
- **S10.** Tested the negative branch: with the qualitative form
  $H_L\ge c\log L-1$ in place of $\frac1{16}\log L$, the ratio proof with
  $A=(\log r)/C$ gives $B=\frac3C\log r+O(1)$ against
  $c\log\lfloor S\rfloor=\frac c2\log r-O(\log\log r)$, a contradiction
  once $C>6/c$; so the growth statement survives with the coefficient
  $1/C$ for an unspecified $C$, exactly as stated. Failed.
- **S11.** Read the p. 14 remark and the p. 17 conjecture on the page
  images ("we conjecture that $r(\mu_r-1)$ is unbounded. From this the
  theorem of Mrs van Aardenne-Ehrenfest would follow"); read Schmidt's
  definitions and corollary on the held part VI. "Countable" for "at most
  countable" is not a discrepancy. Failed.
- **S12.** A summary of S3, S5 and S9; nothing separate to attack.
  Failed.

## Premises

- **de Bruijn--Erdős 1949, Section 1 definitions, p. 14 remark and
  Section 6 conjecture.** Held (image-only PDF; read on the page images
  of printed pp. 14 and 17). Interface: constants over all sequences of
  numbers mod $1$, coincidences allowed; "we conjecture that
  $r(\mu_r-1)$ is unbounded. From this the theorem of Mrs van
  Aardenne-Ehrenfest would follow" (p. 14); the three expressions
  $r(\Lambda_r-1)$, $r(1-\lambda_r)$, $r(\mu_r-1)$ "tend to infinity"
  (p. 17). The conjecture page's mean-normalized reading is taken as that
  page states it.
- **(5.1) and (5.7), reconstruction.** Premise page, read in full.
  Interface used: $\mu_r\ge1+1/r$ for every $r\ge1$ over all sequences,
  coincident points allowed. Used in S7 only as a bound that is bounded
  in $r$.
- **Theorem 1.1 of the 2026 note, reconstruction.** Premise page, read
  in full. Interface: $\mu_r\ge1+r/(r^2-1)$ for $r\ge2$ over sequences of
  distinct points; a fixed-$r$ statement with no uniformity in $r$. Used
  in S7 as a bound that is bounded in $r$.
- **Theorem 1.1 of the 2026 preprint, reconstruction.** Premise page,
  read in full. Interface: three bounds over sequences of distinct points
  for $r\ge r_0$; two imported and unchecked inputs (Theorem 4.1 and
  Theorem 7.1); the ratio part's margin $3/100<1/32$ rests on the constant
  $1/16$. Used in S7--S10 within these hypotheses.
- **Lemma 4.2 with Theorem 4.1, reconstruction.** Premise page, read in
  full. Interface: (4.1) with $B\ge1$, $S\ge2$ at all large integer times
  and $\lfloor S\rfloor\ge L_0$ give $B\ge\frac1{16}\log\lfloor S\rfloor$;
  Theorem 4.1 as used ($H_L\ge\frac1{16}\log L$ for every list, $L\ge L_0$)
  with the source's derivation from Larcher's Section 3; the page's
  authored remark that the qualitative form follows from Schmidt VII. S9
  and S10 use exactly these.
- **Proposition 3.1, reconstruction.** Premise page, read in full.
  Interface: (3.1) at all large $t$, uniform in $x$ and $0\le D\le S$.
  Named in S9 only.
- **Lemma 7.2 with Theorem 7.1, reconstruction.** Premise page, read in
  full. Interface: the $L^1$ bound (7.1) with $S\ge S_0$ and $B\ge1$ gives
  $B\ge c_4\sqrt{\log S}$; Theorem 7.1 as used (unnormalized $L^1$ bound
  $c_H\sqrt{\log M}$), source not held. Used in S7 and S9.
- **Schmidt 1972, part VI.** Held; card provenance, introduction
  (pp. 63--64) and reference list read on the PDF. Interface:
  $U=(0,1]$, $Z(n,\alpha)=\#\{i\le n:\ 0\le\xi_i<\alpha\}$,
  $D(n,\alpha)=|Z(n,\alpha)-n\alpha|$, $S(\infty)$ the set of $\alpha$
  with $D(n,\alpha)$ bounded; Corollary: $S(\infty)$ is at most countable;
  part I (Quart. J. Math. 19 (1968), 181--191) showed measure zero; van
  Aardenne-Ehrenfest showed $D(n)=\sup_\alpha D(n,\alpha)$ cannot remain
  bounded. Used in S3, S5 and S11.
- **Korsky 2026, resolution.** Held (arXiv v2); card provenance
  paragraph, Theorem 1.1 result page statement, PDF Section 4, Theorem
  7.1 and references [9]--[11] read. Interface: as on the reconstruction
  pages; references: Schmidt VII, Acta Arith. 21 (1972), 45--50; Halász
  1981, pp. 79--94; Larcher, J. Complexity 31 (2015), 474--485,
  arXiv:1407.2094. Used to confirm S7, S9 and S10.
- **Problem 255.** Statement section read; the section's paraphrase
  matches it.
- **Not held.** Van Aardenne-Ehrenfest 1945; Schmidt part I (1968) and
  part VII (1972); Larcher 2015; Halász 1981. The section's sentences
  about them rest on the held part VI's introduction and on the held 2026
  preprint's references, and claim no more than those accounts.
- No batch acceptance order applies; no local claim card is consumed.

## Findings

- **F1 (suggested).** Location: bullet "No rate, in either direction",
  "which say nothing once $K(n)>r$; the constants
  $\Lambda_r,\lambda_r,\mu_r$ are limits in $n$ at fixed $r$, so a growth
  rate of the discrepancy in $n$ neither follows from nor feeds the
  conjecture." Defect: the stage-$n$ upper bound $nM_n^r(a)\le r+K(n)-1$
  is a real constraint whenever $r+K(n)-1<n$, and the lower bound is one
  while $K(n)<r+1$; what the bounds fail to control are the limits in
  $n$, because $K(n)\to\infty$. The unqualified "nor feeds the
  conjecture" is contradicted by the section's reverse edge, where the
  claimed resolution consumes a discrepancy growth rate through Lemma
  4.2. Witness: $K(n)=\lceil\log n\rceil$, $r=1$: the bound says the
  largest gap at stage $n$ is at most $(\log n+1)/n$. Replacement: "which
  bound nothing in the limit because $K(n)\to\infty$: the constants
  $\Lambda_r,\lambda_r,\mu_r$ are limits in $n$ at fixed $r$, so through
  Proposition 255.1 a growth rate of the discrepancy in $n$ neither
  follows from the conjecture nor feeds it."
- **F2 (note).** Location: "so all three expressions of the
  mean-normalized conjecture stay bounded." Defect: the displays bound
  $r(\mu_r-1)$ only for $r\ge K$; boundedness over all $r$ needs
  $\mu_r<\infty$ for $r<K$, which the proof does not say. Witness: none;
  the statement is true (Weakest step 2). Replacement: append "for
  $r\ge K$, and for the finitely many $r<K$ because $\mu_r\le2$ by the
  Section 2 sequence, whose $r$-spans lie between $r$ times its smallest
  and $r$ times its largest gap", or write "are bounded for all large
  $r$, so none tends to infinity".
- **F3 (note).** Location: "The quantitative form of the proved
  conclusion of Problem 255 is an input of the claimed resolution".
  Defect: Theorem 4.1 and Halász's theorem quantify the uniform 1945
  statement (a bound over all intervals and all lists), not the
  fixed-interval conclusion of Problem 255, which the section's first
  bullet distinguishes from it. Witness: the finite-list bound says
  nothing about one fixed interval. Replacement: "A quantitative form of
  the 1945 theorem, the uniform statement that Problem 255's conclusion
  strengthens, is an input of the claimed resolution".
- **F4 (note).** Location: "Circular through the only claimed proof of
  the premise" and "the growth is claimed only by" the 2026 preprint.
  Defect: "only" is a claim about the literature that the section's
  reading cannot warrant; the closing sentence of the same bullet already
  scopes itself to "the sources read". Replacement: "the only claimed
  proof in the sources held", in both places.
- **F5 (note).** Location: Target paragraph, "van Aardenne-Ehrenfest's
  'just distributions' theorem of 1945, that no sequence has
  $\sup_\alpha|D_n([0,\alpha))|$ bounded in $n$", and the proof's closing
  "so this is the 1945 theorem in its original form". Defect: the 1949
  note names the theorem without stating it and the 1945 paper is not
  held; the content given matches the held part VI's introduction
  (p. 63), which the section does not cite for it; and the proposition
  lives on the circle while the theorem and Problem 255 live on the unit
  interval, an identification the section does not mention. Witness:
  none; the identification is harmless (Weakest step 3). Replacement:
  cite Schmidt's part VI, p. 63, for the statement, and add "a sequence
  in $[0,1]$ with bounded counting error has at most $K$ terms equal to
  $1$, so the interval and circle forms are equivalent".

## Verdict

- S1: refutation-failed.
- S2: refutation-failed; F2 supplies the omitted finite range.
- S3: refutation-failed.
- S4: refutation-failed.
- S5: refutation-failed.
- S6: refutation-failed as a claim about Proposition 255.1; its wording
  is repaired by F1.
- S7: refutation-failed; F4 qualifies "only".
- S8: refutation-failed.
- S9: refutation-failed; F3 renames the quantified statement.
- S10: refutation-failed as a conditional; its negative branch rests on
  the Lemma 4.2 page's authored remark and on Schmidt VII, which is not
  held.
- S11: refutation-failed.
- S12: refutation-failed.

Limitations. The review is confined to the section, the premise pages
and the held sources named above; the standing of the reconstruction
pages is taken as the assignment gives it, and their proofs were not
re-audited. The 1945 paper, Schmidt's parts I and VII, Larcher 2015 and
Halász 1981 are not held, so the section's sentences about their content
were checked against the held secondary accounts only. The review is
noncomputational. This focused review assigns no tier and changes no
status.

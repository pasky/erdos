---
name: research/leads/totient_binary_series/evidence/verify/lead_totient_binary_series_review_grade
title: "Distinct grade of the blind review of the lead totient_binary_series"
desc: |
  Grades the blind first review of the binary totient lead as it stood on
  2026-10-03: the report passes; every verdict is re-derived and agreed, with
  the valuation census, the window census, the classification search, the
  continued-fraction prefix, the retained witnesses and the identities
  recomputed by the grader's own code; the one required correction is
  accepted as proposed, three suggested corrections are accepted (one with
  modified text), one is rejected and one is added; the lead is reviewed
  once the required text lands, research state ready; no tier is assigned.
created: 2026-10-03T07:54:57Z
updated: 2026-10-03T07:54:57Z
---

***

## Subject and independence

**Paths and date.** The tree as it stood on 2026-10-03. The subject is the
blind extraction, kept outside the repository, of the lead page
`wiki/research/leads/totient_binary_series/_index.md` on that date, with
its lead fields and its review-report sentences removed; with it, as the
report names them, the lead folder's mathematical subpages
(`analytic_sources.md`, `progression_means.md`, `window_cost.md` and the
pages under `arithmetical_windows/`, `integer_interpolation/` and
`sparse_transforms/`), its evidence pages and programs, and the retained
assets under `integer_interpolation/evidence/assets/` and
`sparse_transforms/evidence/assets/`, read from the tree of that date. The
grader checked the freeze without reading the removed text, by a script
that reports only counts, frontmatter key names and the extraction's own
lines: of the extraction's 1,005 lines, 1,000 occur in order in the
committed page, the five exceptions being lines of paragraphs from which a
sentence was cut (the opening paragraph of Target and standing, the
Duverney citation paragraph and the direct-reconstruction paragraph of
Route one, the opening paragraph of Prior work and reading limits, and the
odd-kernel feasibility paragraph of Remaining links); the committed page's
frontmatter has exactly the keys `research_state` and `review_status`
beyond the extraction's, and 49 of its lines are absent from the
extraction, consistent with the cut the report describes. Every path the
report names is present in the tree of that date.

**Report.**
[[research/leads/totient_binary_series/evidence/verify/lead_totient_binary_series_review|The blind review]]
(1,050 lines): Subject and independence, Restatement, Statements and
verdicts T1--T3, N1--N6, C1--C3, D1--D6, R1a--R1f, R2a--R2d, R3a--R3e,
E1--E4, F1--F3, P1 and L1--L19 (sixty labels), Checklist, Weakest steps
1--3, Strongest attack, Premises, Required corrections (one), Suggested
corrections 1--4, Notes (the lead's evidence programs with their commands
and outputs; the reviewer's checks described by method with their outputs),
Verdict.

**What the grader read, and at what depth.** The extraction in full at
proof depth: the tail integers and the residue formula, Propositions 3 and
3′ with the carry dynamics, the tail-certificate bounds, Lemma D and Lemma
R, the Duverney reconstruction and the $L$, $\exp L$ and $\mathsf U$
identities, the termwise-block obstruction, Proposition 4 and its
analytic consequences, the factorial cousin, Lemma 5 and the two-adic
mirror, the finite observations, and every criterion of Remaining links
re-derived by hand. The report in full, including its quoted outputs.
Mathematics only, from the tree of that date: the three top-level
subpages, the two arithmetical-windows pages, the eight
integer-interpolation pages and the four sparse-transforms pages in full,
with every proof re-derived; the four evidence index pages in full; the
evidence programs run, not read; the three asset files read by the
grader's scripts; the library result pages
`library/irrationality/kaneko_2026_refinements_erdos_s_irrationality_criterion_certain/theorem_1.md`,
`theorem_3.md` and `corollary_2.md`,
`library/irrationality/bell_2026_mahler_series_multiplicative_coefficients/theorem_1_3.md`,
the Duverney card's body with `theoreme.md` and `lemme.md`, the Erdős
1948 card's body and the first 140 lines of its transcription, and the
Erdős 1988 card's body; the Statement block of
`wiki/problems/irrationality/E0249/_index.md`, together with the Formulation,
Status, Source, References and Formalization paragraphs above its Current
assessment, which the grader's extraction command printed (an exposure,
recorded below). Operating instructions: `docs/verification.md`, the
review-record parts of `docs/evidence.md`, `docs/research.md` ("Lead
pages" and the Erdos-specific sections), `docs/approach_vetting.md` and
`docs/math_authoring.md`. Shape model for this record:
the grade of another lead's re-review,
shape only. Not read: the live lead page, the extraction's cut logs beyond
their key names and counts, every other record under any
`evidence/verify/` folder, the card and proof of L16 under `wiki/theory/`,
the held PDFs, and all review-status, standing and "Current review" text.

**Computation.** With the grader's own scripts, kept outside the
repository, written from the definitions and organized differently from
the lead's programs (a Python-integer recurrence modulo $2^{64}$
cross-checked against a windowed sum, a distinct-prime-factor sieve for the
windows, Euclid's algorithm on exact fractions, 130-digit decimal
arithmetic, and exact replays of the assets): valuation census to $10^7$
with largest valuation 29 and the cap unreached; hits $72,45,21,9$ at
excess $0,1,2,3$; records $(16,4)$, $(28,6)$, $(64,10)$, $(88,12)$,
$(2146743,28)$, $(2786632,29)$, each a carry tie; 71 excess-positive
indices in $[16,10^7]$ with filter survivors $64,204,512,1632$, and
$N=3,5,10$ below 16 with $\Phi_N=8,40,1392$; per-dyadic-block counts
$2,0,2,4,2,2,4,3,3,5,3,2,3,2,3,5,6,10,9$ for $J=5,\ldots,23$ and $1$ in
the partial block; $P(v_2(\Phi_N)\ge k)\,2^k=10.21,10.24,10.26,10.32,
10.34,9.65$ at $k=6,8,10,12,15,20$, giving an expected count $101.3$
against $5\ln X=80.6$ and the observed $71$. Window census: 240, last at
31790, truncated-run statistic 20 over $N\ge32767$. Classification search
to $n\le200000$: only $(5,3)$; $\Phi_{17}=16\cdot11203$;
$8\mid\Phi_{5+200h}$ for $h\le1999$; $v_2(\Phi_N)=2$ at $N=5^3,5^5,5^7$;
$v_2(\Phi_{64})=10$; $L=\operatorname{lcm}(55,\ldots,64)=13632589333440$
with $L/64=213009208335$ and $v_2(L)=6$; the nine primes
$\equiv1\pmod{128}$; $p=647\equiv-1\pmod{36}$ with totients
$(417962,124416,163200)$ and signed sum $-130346\equiv2\pmod4$; $N=15131$
prime with valuation 1 and $N=89013=3\cdot29671$ with valuation 2;
$127/96>56/45$ and $\tfrac76\cdot\tfrac{16}{15}=\tfrac{56}{45}$; the
primes $2^e+1$ at $e=4,8,16$ have $v_2(\Phi_n)=4,4,6$, below $e+1$.
Continued fraction at $M=40000$: common prefix 11759 beginning
$1;2,1,2,1,1,2,1,12$, largest quotient 15531 at index 7055, last common
convergent's denominator of 6018 digits, determinant one, both bounds
strictly inside the cylinder; at $M=4000$ the quick-mode figures 1171,
3281 at 911 and 599 digits; the bounds certify
$1.3676308019850223507905$. Identities at 130 digits: $41/32<S\le45/32$;
$S-(\tfrac12+\sum\mu(d)/(2^d-1)^2)=5\cdot10^{-129}$;
$\sum_{k\le400}A(2^{-k})-2=-4\cdot10^{-121}$; Lemma 5 at $N=10$ within
$3\cdot10^{-118}$; Proposition 4 on the grid $p=(2,3)$, $t=(1,2)$,
$w=(1,-1)$, $N=29$ within $7\cdot10^{-125}$ with coefficient ratios
$3,2,2$ at $s=1000,1006,2401$; $R_6=0.941457$; the dropped tail at
$N=50$, $H=10$ equal to $0.0455$ inside $[0.00735,0.0605]$; the small
values $U_k(n)=18,26,24,56,54,112$; the $k=3$ carry witness with
$v=2672$, $W_3=0$, cost 47 and $\Lambda=0.3506$; the $k=4$ witness
$(18,40,170)$ with $v=112$, $W_4=0$; the $J=B=4$ example $(56,88,144)$
with $W=0$, $v=-5230$, $u=-3824$, $C=42$; $z=2e_4-e_5$ with $u=0$, $v=-4$,
$W=58$, $C=31$; the phase example $C_{\rm odd}=5$, $\epsilon=1/10$; at
$J=32$, $\mathcal K_J=\{17,19\}$, $D_{17}=21$, $D_{19}=20$, $G=1$,
$a_{64}=16$, $a_{43}=21$; the prime sieve at $Q=15,21,30,70,210,2310$
with $G_Q^2\mid D_Q$, $D_Q>2^{2\varphi(Q)-4}/P^2$, $M_Q>S$,
$R_Q\ge2^{-q}$ and $\Psi_{21}(2)=2359=7\cdot337$;
$\sum_{l\ge1}(A+l)^22^{-l}=A^2+4A+6$; the pentagonal gaps at $k=3,4,5$;
$c_5=3/5$, $c_{25}=16/25$ and $\sum_{d\mid n}dc_d=\varphi(n)$ through 30.
Assets: the $k=3$ and $k=64$ certificates replay (right inverses,
predecessor obstructions, all eight target solutions with their costs,
supports, ratios and exclusions, 2433103 and 7581571381774 at $k=64$);
all 33 carry witnesses replay with $v\equiv0$, $W_k=0$ and their costs,
including 293166 and 282876 at $k=384$; the five gap witnesses satisfy
(G1)--(G2) with the recorded heights and central coefficients, only
$(100,20)$ fails the reversed cutoff $n\ge k+2$, and the certified
exclusions are $11433$, $1152083$, $290856$, $3597545$, $555695$. The
lead's six evidence commands were rerun from the repository root; their
outputs equal the record's quoted lines, with 19, 20, 55, 11, 16 and 112
checks passing.

**Independence facts, by role.** The grader is a distinct grader in a
fresh context (model: Claude Fable 5.1), given only the grading
assignment, distinct from the author of the lead, its subpages, programs
and assets and from the reviewer; the grader took no part in writing any
of them or the report. The grader is not blind, as a grader need not be,
and read the report in full. The grader's own exposure, recorded for the
record: the problem page's `status: open` field and its Status paragraph;
the subpages' `research_state` and `review_status` keys and their
"author-recorded and unreviewed" sentences; the progression-means page's
sentence placing L16 at tier 0; the Duverney card's and its two result
pages' Verification sections, which report a review and a grade of a
Problem 250 reconstruction with their verdict words; the evidence index
pages' and library pages' sentences that no independent review is
claimed. None of these states a verdict on this route, and nothing in this
grade comes from them.

**Materiality rulings.** The report lists six exposures; each is ruled on
here by the content test of `docs/verification.md`. (1) The problem page's
Status sentence: immaterial, it states that the problem is open, which the
lead itself says. (2) The subpages' lead-metadata keys: immaterial, they
say only that no review exists, which the assignment itself stated, and
the report's research-state judgment is made from the body. (3) The
"author-recorded" sentences: immaterial, no finding. (4) The shape model's
`desc`, about another lead: immaterial. (5) The Duverney card's sentence on
an earlier focused review of its Problem 250 specialization: immaterial,
another subject. (6) The three standing descriptors that survived the cut:
immaterial, no finding. Nothing in the report could only have come from
these, and no attack's direction followed them: the exhaustive
classification search, the attack on Theorem 4's quadratic-residue inputs,
the recount of the census and the recomputation of the continued fraction
are what a refutation charge on the lead's held links takes without
prompting.

## Report checks

A report passes when its subject block resolves (date, paths and the
extraction's relation to them), it states independence facts and
exposures, restates the route with its quantifiers, gives a verdict on
every mathematical statement of the extraction with the verdict words in
full, states its cycle, and names no person, seat, session or harness.
**The report passes.**

- Independence: stated by role and model, with the refutation charge, the
  first-review status ("the route's first review: no earlier review of
  this lead exists"), the allowed and actual reading from the tree of the
  frozen date with its depth, the exclusions, the six exposures, and the
  statement that no communication beyond the assignment reached the
  reviewer.
- Subject: frozen by the lead page's path and the date, with the
  extraction's cut described (lead fields and review-report sentences
  removed, 1,005 lines, eleven sections) and every subpage, program and
  asset named by path; the freeze is verified above by counts.
- Coverage: the sixty labels give a verdict on every mathematical statement
  of the extraction; the grader found no mathematical sentence without
  one. The items read as non-claims (T2, R3a, P1, L19, the labeling of
  D3) are rightly so classed, each with its mathematical content checked.
  One reading-status sentence carries no label: the Route one remark that
  Bell and Smertnig's paper "is a reading lead, not a checked obstruction
  here", which the lead's own analytic sources page and fourth paragraph
  of Target and standing supersede. It is not a mathematical statement,
  so coverage is complete; a suggested correction is added below.
- Verdict words: refutation-failed is written in full at each of its 56
  occurrences; refuted-as-stated is written in full twice (L5 and the
  Verdict); neither is abbreviated; proof defective; statement unresolved
  does not occur, rightly, since no proof failed.
- Names: none of a person, seat, session, channel, tool harness or private
  path; no commit id or hash (the external manuscript's commit is
  mentioned as a fact about the lead's citation and not reproduced); the
  model is named as the existing records name it; the thirteen lines wider
  than 80 columns are the frontmatter name, paths in the reading list and
  quoted program output.
- The checklist gives a verdict on all ten Erdos items; the three weakest
  steps are re-derived rather than paraphrased; the strongest attack is
  real (an exhaustive search for a second excess pair, the external inputs
  of Theorem 4, a recount of the census by another route, and the
  continued fraction by Euclid's algorithm alone); the premises part names
  L16 as the one native claim consumed, leaves its standing unreported
  because the card lay outside the read set and asserts no tier, lists
  the external theorems with their reading depths, and states the
  explicit unproved estimates on which the route's conclusion would rest.
  A lead review asserts no tier, so an unreported dependency standing is
  not a defect here; the grader records that the progression-means page
  itself places L16 at tier 0, author-recorded.
- Reproducibility: the six rerun lines are quoted with their outputs, and
  the grader's reruns reproduce them line for line; the reviewer's own
  census, window, continued-fraction, certificate, witness and identity
  figures are all reproduced by the grader's code. The report discloses an
  off-by-one in its first window census and the corrected agreement.

## Verdicts re-derived

Each verdict of the report was re-derived by the grader; "agree" records
that the grader's derivation reaches the same verdict. Labels are the
report's; a label covers the family of statements the report puts under
it.

### Target and standing

**T1.** Agree, refutation-failed. $\varphi(n)\le n$ gives absolute
convergence and $S<2$ strictly since $\varphi(3)=2<3$; the partial sum
through six is $41/32$ and $T_6\le8$, so $S\le45/32$; the grader's
130-digit value and the bounds at $M=40000$ certify the stated prefix.

**T2.** Agree, not a mathematical claim beyond the withdrawal's reason,
which holds: $1\equiv1\pmod{10^6}$, so a bound on a modulus bounds no
least representative without $N\ge M$.

**T3.** Agree, refutation-failed as a description of Theorem 1 of the
interpolation page and Corollary 12 of the shadows page; the geometry
page's Linnik bound is the matter of suggested correction 1.

### Notation and the tail integers

**N1--N3.** Agree, refutation-failed. Splitting the top term gives both
recurrences and $\sum_j(N+j)2^{-j}=N+2$; $I_N=b(2^NS-\Phi_N)$ is a
positive integer at most $b(N+2)$ with $b$ times the recurrence of $T_N$;
Lemma 2 follows by induction on $m$ from $\Phi_N=2^m\Phi_{N-m}+\Phi_{N,m}$,
and with $2^m>b(N+2)$ the residue of $-b\Phi_{N,m}$ is $I_N$ itself.

**N4.** Agree, refutation-failed. For $N\ge4$, $9/8\le\Phi_N/2^N<S<2$
(checked exactly through $N=60$), so $v_2(\Phi_N)\le N-1$ and Lemma 2
gives $2^m\mid I_N$, whence $2^m\le b(N+2)$; the stated supremum bound
$\log_2(3b)$ is valid, $\log_2(3b/2)$ being sharper, as the report
notes.

**N5.** Agree, refutation-failed. When $b(N+2)<2^N$,
$v_2(I_N)<N\le v_2(a2^N)$, so $v_2(b\Phi_N)=v_2(I_N)$ and the odd-part
bound follows; the exclusions for one index, infinitely many indices and
unbounded excess follow, the last because the hypothesis holds for every
large $N$ at fixed $b$.

**N6.** Agree, refutation-failed. Off a tie $a_N=\min(u_N,1+a_{N-1})\le
u_N<\log_2N$ because $\varphi(N)<N$; at a tie $a_N=u+v_2(x+y)$; the six
records to $10^7$ are ties in the grader's census.

### A sufficient tail certificate and its actual limitation

**C1--C2.** Agree, refutation-failed. The certificate inequality puts
$bT_N$ off the integers; $\varphi(n)/n\ge\prod_{i\le r}i/(i+1)=1/(r+1)\ge
1/(1+\log_2n)$ and $x/(1+\log_2x)$ increases for $x\ge2$; the upper bound
sums $(N+j)2^{-j}$; the grader's values at $N=50$, $H=10$ sit inside the
two bounds; the threshold follows from the lower bound.

**C3.** Agree, refutation-failed. Lemma A (a prime $3\bmod4$ or a
semiprime cofactor on the reduced class, by Dirichlet) and Lemma B's count
$\sum_{i<m}v_2(\varphi(g_i))\ge m(m-3)/2$ against $\log_2M+E_m+m/2$ were
re-derived; the page's representative caveat is right.

### The dyadic rung and what a progression can certify

**D1.** Agree, refutation-failed. Proposition 3′ at $b'=1$; one
excess-positive index forces $v\ge N-\log_2(N+2)$, and infinitely many
exclude every $v$.

**D2.** Agree, refutation-failed. The grader's census returns 71 indices,
$\Phi_3=8$, $\Phi_5=40$, $\Phi_{10}=1392$, no other excess-positive
$N<16$, and $N-\log_2(N+2)=2786610.59$ at the record.

**D3.** Agree, not a claim, with the reviewer's objection confirmed: the
empirical law $P(v_2(\Phi_N)\ge k)\approx10.3\cdot2^{-k}$ predicts about
five indices per dyadic block, $101$ through $10^7$, against $71$
observed and $5\ln X=80.6$; five per natural logarithm is not what the
distribution suggests.

**D4.** Agree, refutation-failed. Lemma 1 (a cofactor of valuation at most
$v_2(\varphi(g))+2$), Theorem 2 (primes $q_j\equiv1\pmod{2^B}$ isolate one
term), Corollary 3's (7)--(8) and Theorem 4 ($p\equiv-1\pmod{4M}$ with
roots of $t\delta_j$ supplied by reciprocity and the supplementary laws)
were re-derived; the selected term has valuation
$v_2(c_{j_0})+v_2(\varphi(t))+1$.

**D5.** Agree, refutation-failed. Every step re-derived: $m=e+1$,
$\varphi(n)=2^e$, $\varphi(n-1)=2^{e-1}$, the digit count $2^r-1=2^s$,
$z\equiv7\pmod8$ coprime to 15, the three values of $\varphi(z)$,
$z=7\times$ Fermat primes at least 17, and $127/96>56/45$; the exhaustive
search to $n\le200000$ finds only $(5,3)$; the primes $2^e+1$ at $e=8,16$
have valuations 4 and 6.

**D6.** Agree, refutation-failed. The filter is the $i=0$ case of (8);
the recomputed survivors are $64,204,512,1632$; Theorem 4 at $n_0=64$
gives valuation $5+1=6$ on its class; the CRT data, the nine primes and the
$p=647$ witness reproduce.

### Route one: Duverney's sparse product

**R1a.** Agree, refutation-failed. The pentagonal gaps are $k-1$ before
and $2k$ after $n_k$ (checked at $k=3,4,5$); $|J_k|\le|\delta||q|^{-k}
(A^2+4A+6)$ with $A=n_k+k$; $q^k\mid\delta a(n_k)$ with
$a(n_k)=(-1)^k(a+bn_k)$ eventually nonzero; this matches the library
lemma page's Steps 3, 6 and 7.

**R1b--R1c.** Agree, refutation-failed. $dc_d=(\mu*\mu*\mathrm{id})(d)$
from $\sum_{d\mid n}dc_d=\varphi(n)$ (checked through 30), $c_5=3/5$ and
$c_{25}=16/25$; $\exp L$ has positive coefficients; the Dirichlet series
of $\varphi$ is $\zeta(s-1)/\zeta(s)$; the four $\mathsf U$ identities are
convolutions with $1$ or $\mu$.

**R1d.** Agree, refutation-failed. Proposition 1 forces $e_1=-1$, $e_p=1$
and the impossible $pq(1-e_{pq})=2(p+q-1)$; in Theorem 2 only $r(p-1)/p$
and $r^p/p!$ are non-$p$-integral at degree $mp$, every other
contribution using indices below $p$ because $d\ge m$, and Wilson and
Fermat give the unit $2r$; the prefactor's unit at degree $h$ carries the
valuation to $mp+h$.

**R1e.** Agree, refutation-failed. Identity (1) by coefficient comparison;
$2^{-q}\le R_Q$; (6) from the valuation formula; the nonprimitive prime is
$P$ with exponent one; $G_Q^2\mid D_Q$ because only the $d=Q$ summand
carries $\ell$; both cases of Theorem 3; the grader's exact checks at six
values of $Q$ confirm, with $\Psi_{21}(2)=7\cdot337$.

**R1f.** Agree, refutation-failed. $\Lambda(P)=\sum_ip_iT_{N-i}$,
$u\equiv2$ and $v\equiv b_N\pmod{2^k}$, $E_0(P)$, Lemma 3's parity, the
truncation transfer and Proposition 4 were re-derived; the five witnesses
replay with their heights, central coefficients and exclusions, and only
$(100,20)$ has a reversed coefficient at $n=k$.

### Route two: Erdős's arithmetic tails

**R2a.** Agree as source fidelity. The transcription shows the CRT block
$d(x+j+yA)\equiv0\pmod{t^{j+1}}$, the average controlling a block of
$10\log n$ terms and $d(r)<r$ for the far tail; the p. 66 and p. 102
quotations on the cards say what the lead says.

**R2b.** Agree, refutation-failed. $2^k\mid b\varphi(N+k)$ gives
$2^k\le b\varphi(N+k)<b(N+k)<b(N+k+2)$; the stronger block gives
$2^{k+1}<N+k$.

**R2c.** Agree, refutation-failed. The grader's sieve census returns 240,
last 31790, statistic 20; "necessary" is correct for the certificate that
uses the upper bound; the proposed rewording is adjudicated below.

**R2d.** Agree, refutation-failed. Lemmas C and D of the window page were
re-derived; the withdrawn inference was indeed invalid.

### Route three: the dilation argument

**R3a.** Agree, not a claim of the lead; the external manuscript's
correctness is explicitly not assessed; its commit identifier is the
matter of suggested correction 4.

**R3b.** Agree, refutation-failed. $\varphi(p_e)\varphi(m)=\varphi(p_em)
\varphi(g)/g$ with $s=jp_e-t_e\ge1$; competing dilations decay like
$2^{-s/(p-1)}$ against $2^{-(s+t)/p}$, ratio $C2^{-s/(p(p-1))}$; the
expansion checks to $10^{-124}$ on the grid $p=(2,3)$, and the ratios
$3,2,2$ at $s=1000,1006,2401$ are explained by the gcd factor.

**R3c.** Agree, refutation-failed. $\kappa_Q(a)$ with its Euler product,
the refinement formula at a fresh prime, the anchor-cutoff-prime separation
with $\eta$, Lemma 2a's explicit error and Corollary 3's refinement to a
modulus divisible by every $p_e^2$ were re-derived; the kernel $A(s)-h_s$
is nonzero with a summable first moment.

**R3d.** Agree, refutation-failed. Lemma 4's two bounds, the cases $c<p$
and $c>p$, and Corollary 5 at $c=p$ ($H_N=pk+1$ on
$2^k<N\le2^{k+1/p}$, a fixed first shift $s_k$, a one-coefficient kernel
in Lemma 2a, a first term above $D\gamma/8$, other dilations
$O(N^{-1/(p-1)})$) were re-derived.

**R3e.** Agree, refutation-failed. $1-1/p\le R_n<1-1/(2p)+5/(4p(p+1))<1$
for $p\ge3$; $R_6=0.941457$ at $p=7$.

### Exact identities retained for later use

**E1--E2.** Agree, refutation-failed. One-line Möbius inversions;
$\sum_d\mu(d)/(2^d-1)=1/2$ supplies the constant; residuals below
$10^{-120}$; $A_{(p)}(x)=(p-1)A(x^p)+A_{(p)}(x^p)$ from
$\varphi(pn)\in\{(p-1)\varphi(n),p\varphi(n)\}$, iterated.

**E3--E4.** Agree, refutation-failed. Rearrangement by absolute
convergence and the displayed geometric sums, checked at $N=10$ to
$10^{-118}$; the $d>N$ terms are $O(1)$; the two-adic series converges in
$\mathbb Z_2$ and no equality of limits is asserted.

### Finite observations

**F1.** Agree, refutation-failed. All figures recomputed: $72,45,21,9$,
the six records, each a carry tie.

**F2.** Agree, refutation-failed. Prefix 11759, largest quotient 15531 at
index 7055, 6018 digits, determinant one, strict containment; the cylinder
argument is right, a rational strictly inside having denominator at least
the convergent's.

**F3.** Agree, refutation-failed. The $k=3$ and $k=64$ certificates replay
(right inverses, obstructions, costs 109 and 2433103, exclusion
7581571381774); the nine orders' values in the computation table match the
evidence program's output.

### Prior work and reading limits

**P1.** Agree, a reading record. The KST remark is right (Corollary 3
groups by totient values in the exponent); the grader did not inspect the
external web pages either.

### Remaining links and next constructions

**L1.** Agree, refutation-failed. The fresh-prime construction gives
$-e_{j_*}$ modulo every prime; the $p=2$ vectors are
$\mathbb Q$-independent; a prime dividing the index would make the image
modulo it a proper subspace.

**L2--L3.** Agree, refutation-failed. $u\equiv2$ from $n\ge k+2$; $v$
reduces to the nonpositive-shift equations; the tail
$\sum_{j>k}(2\varphi(j)+\sum_ny_n\varphi(n+j))2^{-j}$ gives
$2^{-k}C_k(y)$; $2a$ and $2a-bc_0$ are nonzero residues below $2^k$
because $1<S<2$ and $c_0$ is even.

**L4.** Agree, refutation-failed. $p_{N-n}=y_n$, $p_N=2$,
$E_0(P)=C_k(y)2^{-k}$, $b_N=c_0$; the replay confirms that four of the
five witnesses meet $n\ge k+2$.

**L5.** Agree, refuted-as-stated. Lemma 4a and Proposition 4 of the
geometry page, updated 2026-09-19, bound the separating primes and the
solution's support and coefficients by $\exp(Ck^2\log(k+2))$ through
Linnik's theorem, and the interpolation index page states that bound. On
the narrower reading that Theorem 1's own Dirichlet proof retains no
bound the sentence is true, so the correction removes an ambiguity, not a
mathematical error.

**L6.** Agree, refutation-failed. Lemma 1's identity, Proposition 2's
residue argument ($|c|a<\tfrac3{10}bC_k$), the two-congruence
equivalence, Theorem 4's character count and Proposition 4a's forced
character $U_k(n)/2^{k+L}$ with at most two good indices were re-derived;
the $k=3$ and $k=4$ witnesses and the small $U_k(n)$ reproduce.

**L7.** Agree, refutation-failed. Proposition 1 ($|c|a<2^d$),
Proposition 3 through the span theorem on the shifts $-d+2,\ldots,J$,
Proposition 5's inversion modulo $2^{d-1}$, and the zero-$u$ bound
$\|z\|_w\ge2^{J+1}$ from $|\sum_nz_n\Phi_n|\ge2$ were re-derived.

**L8.** Agree, refutation-failed. Proposition 6's exact valuation $s+t$
against $|b\Lambda|\le2^sb_{\rm odd}D/2^J$; Corollaries 7 and 8; the
$J=B=4$ example and the $z=2e_4-e_5$ figures reproduce.

**L9.** Agree, refutation-failed. Parities $(1,0)$ and $(0,1)$ at the two
primes, an odd gcd, the two-term cost below $2^J(2J+2)(3J+2)/g$, and the
comparison family's $\|z\|_1\ge H$ from (18).

**L10.** Agree, refutation-failed. $I_n\equiv2A_n\pmod4$ for odd $b$,
identity (21), $\epsilon=b/2^{J+2}$ and $C\ge2^{J+1}/b$; the half-integer
pairing gives $C\ge1/(2\epsilon)$.

**L11.** Agree, refutation-failed. Lemma 2's fiber count, Lemma 3's (2),
Lemma 5's exponent $J'-3J+2B+4$ with $(5J')^6$, Theorem 6's class maxima,
Lemma 10's cross vectors of cost at most $18(R+J+2)^3$, Propositions 11
and 14 and Corollaries 7a, 12 and 15 were re-derived; every reverse
implication assumes irrationality, as stated.

**L12.** Agree, refutation-failed. Legendre's theorem and (2) give
Proposition 8; the lead's `shadows.py` in quick mode confirms the quotient
bound at $J=33$ against $J=32$ and the denominator bound at $J=19950$
against $J=19951$.

**L13.** Agree, refutation-failed. The Gaussian transference
$\lambda\delta<(d+4)\log2/\pi$, the dual coset (3), the norm identity (7),
Lemma 3 at $d=2$, Theorem 4's quotient by the shadow-zero subspace and the
bound (9); the exposed example gives $C_{\rm odd}=5$, $\epsilon=1/10$.

**L14.** Agree, refutation-failed. Proposition 2's chain re-derived with
its constants ($26\delta2^JH$, $31\delta H$, $38\delta H^2$,
$152\delta H^2$), the oddness of $G$, the integral omitted term
$(q+1)\Phi_n/4$ and the doubling $f_{n+1}=2f_n$ below $1/3$; Theorem 3's
dyadic-factor comparison (10); the $J=32$ structural values reproduce.

**L15.** Agree, refutation-failed. $bT_N=bU_J(N)/2^J+bT_{N+J}/2^J$ with
$0<bT_{N+J}/2^J\le2^{-C}$; $|e(x)-e(y)|\le2\pi|x-y|$; divisors of $b$
inherit the exclusion; $e(bT_N)=e(b2^NS)$.

**L16.** Agree, refutation-failed conditional on KST Theorem 3 as
extracted. The mass $O(x_j^{d+1})$ is $o(2^{z_j}x_j)$, the supports are
$o(x_j/z_j)$, item 3 is the gap condition, the series equals the integer
$Ag_0$; (22) follows from $N+h+u+1\le(N+h+1)(u+1)$; nonnegative $G$ is
excluded.

**L17.** Agree, refutation-failed. The mean-square identity (9),
$E_1,E_2<1/(64k^{3/2})<\kappa/(4\ell^{3/2})$,
$\sigma_{\min}\ge\kappa X^{3/2}/4$, Corollary 3's $256k^3/\kappa<512k^3$
and the two bidiagonal examples were re-derived.

**L18.** Agree, refutation-failed conditional on Bell--Smertnig Theorem
1.3 and KST Theorems 1, 3 and Corollary 2 as extracted.
$\chi(\ell)=(\ell-1)/\ell^r$ has infinite image; the fixed filter's
coefficient at $2^{j_0}m$ is $c_{j_0}\varphi(m)$; the orbit bounds
(16)--(17); the obstruction (20) holds in both parities of $N$.

**L19.** Agree, non-claims that accurately summarize what remains open.

**Checklist, weakest steps, strongest attack, premises.** Agree. The ten
verdicts are supported; steps 1--3 are re-derived above under L2--L8, D5
and L14; the attack's figures (only $(5,3)$ to 200000, the census, the
continued fraction) reproduce by the grader's own code; no ledger row is
consumed as a tier-bearing premise, L16's statement having been re-derived
from the progression-means page; the explicit unproved estimates are as
the extraction states them.

## Corrections

Each correction was adjudicated against the extraction, the subpages and
the grader's recomputation; locations quote the extraction, which is the
committed text of that date.

**Required 1 (L5).** Accepted as proposed. Remaining links and next
constructions, the paragraph following the display of $\Lambda_k$, its
last sentence: replace "All existence quantifiers in the proof precede
any limit in $k$; the Dirichlet primes used to show solvability have no
retained uniform bound." with

> All existence quantifiers in the proof precede any limit in $k$. The
> only retained quantitative version, Proposition 4 of the
> [[research/leads/totient_binary_series/integer_interpolation/geometry|geometry
> page]], uses Linnik's theorem to produce a solution with
> $C_k(y)\le\exp(Ck^2\log(k+2))$ for an effective absolute constant
> $C$; this is far above the required $o(2^k)$.

Basis: L5; the text matches (14) of the geometry page, and the
interpolation folder's index page already states the bound. The sentence
is not load-bearing, so the correction changes no standing.

**Suggested 1.** Accepted, with the page's wiki-link added. Target and
standing, third paragraph, after "The proof does not bound its support or
coefficients.": insert

> An effective bound, $\exp(O(k^2\log(k+2)))$ by Linnik's theorem, is on
> the
> [[research/leads/totient_binary_series/integer_interpolation/geometry|geometry
> page]]; it is too large to use.

Basis: as Required 1; the paragraph has no nearby link to that page.

**Suggested 2.** Accepted as proposed. The dyadic rung, the paragraph
after Lemma D: replace the sentence beginning "The evidence's valuation
distribution suggests about $5\ln X$" and ending "not a theorem." with

> The evidence's valuation distribution, roughly
> $P(v_2(\Phi_N)\ge k)\approx10\cdot2^{-k}$ for $k\ge6$, would predict
> about five excess-positive indices in each dyadic block of $N$; the
> observed blocks through $10^7$ hold between zero and ten, 71 in all.
> Both figures are observations, not theorems.

Basis: D3 and the grader's census: $P(v_2(\Phi_N)\ge k)\,2^k$ lies
between $10.2$ and $10.3$ for $6\le k\le15$, the dyadic blocks hold
between $0$ and $10$ indices, and the law predicts about $101$ against
the observed $71$; "about $5\ln X$", that is $80.6$, is not what the
distribution suggests.

**Suggested 3.** Accepted with modified text. The reviewer's clause "the
least block length at which the crude upper bound $(N+H+2)2^{-H}$ on the
discarded tail can fall below one" is not exact: at $N=2^J-2$ the block
length is $J_0=J$ and the bound at $H=J$ equals $1+J/2^J>1$. Route two,
the one-large-prime window paragraph: replace the clause after the comma,
"a necessary lower bound on the block length for the stated crude-tail
certificate", with

> a block length below which the crude upper bound $(N+H+2)2^{-H}$ on
> the discarded tail cannot fall below one; the displayed lower bound
> forces only $H>\log_2(bN)-\log_2(1+\log_2N)$.

Basis: $H\le J_0-1<\log_2(N+2)$ gives $2^H<N+2$, so the bound exceeds
one; the clarification the reviewer asks for is kept, and the sentence
no longer invites the reading R2c describes.

**Suggested 4.** Rejected. Convention 9 (Paths and dates, not hashes)
admits an external repository's commit where a record relies on that
exact external content; the sentence names the file and the sections read
at that revision, the structural description that follows was read from
it, and a GitHub manuscript has no release or DOI to prefer. The
progression-means page pins the same revision in its link. The identifier
stays as it is.

**Added (suggested).** Route one, the paragraph ending with the Mellin
transform: the sentence "Bell and Smertnig's 2026 paper on multiplicative
Mahler series is a reading lead, not a checked obstruction here." predates
the analytic sources page and contradicts the fourth paragraph of Target
and standing. Replace it with

> The
> [[research/leads/totient_binary_series/analytic_sources|analytic sources
> page]] checks Bell and Smertnig's 2026 theorem: $A$ is not $k$-Mahler
> for any $k\ge2$; this excludes no modular or other non-Mahler
> functional-equation construction.

Basis: L18 and the analytic sources page's section on the exact Mahler
consequence. The sentence is a reading-status remark, not a load-bearing
statement, so the correction is suggested, not required.

**Notes.** The report's description of the reviewer's checks agrees with
the grader's independent recomputation at every figure, and the quoted
evidence outputs are reproduced line for line; no in-place edit of the
report is needed. Two observations outside the subject, flagged for the
maintainers and not corrections to the lead page: `analytic_sources.md`
carries two SHA-256 digests of held PDFs, which convention 9 reserves to
the Git LFS pointers; and the Erdős 1948 source card's summary writes
$k=[(\log n)^{1/2}]$ where the transcription reads $(\log n)^{1/10}$.

**Rejected or downgraded.** Suggested correction 4 is rejected; nothing is
downgraded.

## Outcome

- [[research/leads/totient_binary_series/_index|totient_binary_series]]:
  **reviewed**, once the required text is landed exactly as stated; the
  accepted suggested texts are wording changes outside the route's
  load-bearing statements. Every statement the route rests on is
  refutation-failed under the report and the grader's re-derivation: the
  tail integers and the residue formula, the valuation criterion with its
  odd-part and dyadic forms, the carry dynamics, the isolation theorems
  and the classification with its sole pair $(5,3)$, the progression-mean
  separation with its explicit error bound and the fixed-grid
  obstruction, the integer span theorem and the complete-tail criteria in
  their central-zero, central-free, aggregated, two-depth and homogeneous
  forms, the shadow and flatness results, the phase transference and the
  short-support localization, the logarithmic-product and prime-sieve
  obstructions, the gap-multiplier criterion with its Euler calibration,
  the Kaneko--Suzuki--Tachiya and Bell--Smertnig specializations
  (conditional on the extracted source statements), the retained
  identities and every finite figure. The route's conclusion is
  conditional on the unproved estimates the page lists (unbounded excess,
  or infinitely many excess-positive indices for the dyadic rung;
  $\liminf\Gamma_k/2^k=0$ or one of its weaker forms;
  $\limsup\epsilon_J2^J=\infty$ along powers of two; a signed sparse
  multiplier meeting the source hypotheses; a construction forcing a
  nonzero null kernel), each stated as open at every point where it is
  used; no native claim is consumed as a tier-bearing premise, and the
  external theorems are consumed at the reading depths the pages state.
- research_state: **ready**. The body names bounded next investigations
  whose inputs are in the folder: the finite exact phase test (11) of the
  localization page at chosen $(M,J)$, needing only totients through
  $3J$ and the two checkable structural conditions; the conditioned
  residue count (8) of the two-depth page on explicit bounded slices; the
  structured-multiplier system (8) of the gap-multiplier page, with the
  retained witnesses as seeds; and the odd-kernel minimum on $[J,2J]$
  along powers of two, whose feasibility is proved. No stated prerequisite
  is missing; nothing is deferred; the target is unresolved and the route
  is live, so nothing is closed.

No tier is assigned and no status changes.

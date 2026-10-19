---
name: research/leads/totient_binary_series/evidence/verify/lead_totient_binary_series_review
title: "Blind review of the lead totient_binary_series"
desc: |
  Blind first-cycle refutation review of the binary totient lead and its
  proof sketch: the tail integers, the 2-adic criterion and its dyadic
  rung, the progression-certificate rigidity and classification, the
  progression means, the integer interpolation with its carry, two-depth,
  shadow and phase criteria, the three routes, the retained identities and
  the finite observations survive (refutation-failed) under re-derivation
  and independent recomputation; one required correction (a sentence that
  denies a bound its own subpage retains), four suggested, notes with the
  exact commands and outputs.
created: 2026-10-03T07:28:29Z
updated: 2026-10-03T07:28:29Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context (model: Claude Fable
5.1), given only the review assignment and the frozen extraction named
below. The charge was refutation. This is the route's first review: no
earlier review of this lead exists, there is no second-cycle material,
and the attacks recorded here are the first cycle's.

**Frozen subject.** The tree as it stood on 2026-10-03. The subject is
the blind extraction `lead.md` of the lead page
`wiki/research/leads/totient_binary_series/_index.md`, prepared outside
the repository on 2026-10-03 by cutting the page's lead fields
(`research_state`, `review_status`, `last_reviewed`) and its
review-report sentences; the extraction's own cut logs were not opened.
The extraction has 1,005 lines in the sections Target and standing,
Notation and the tail integers, A sufficient tail certificate, The dyadic
rung, Route one, Route two, Route three, Exact identities, Finite
observations, Prior work and reading limits, and Remaining links and next
constructions. Statements are cited below by section and sentence, never
transcribed.

**Allowed material actually read, with depth.** All paths are
repository-relative and were read as they stood on 2026-10-03.

- `wiki/research/leads/totient_binary_series/analytic_sources.md`,
  `progression_means.md`, `window_cost.md`: complete, every proof
  re-derived.
- `wiki/research/leads/totient_binary_series/arithmetical_windows/_index.md`,
  `arithmetical_windows/classification.md`,
  `arithmetical_windows/evidence/_index.md`: complete, every proof
  re-derived; `arithmetical_windows/evidence/main.py` was run, not read.
- `wiki/research/leads/totient_binary_series/integer_interpolation/_index.md`,
  `computation.md`, `carry_criterion.md`, `two_depth_carries.md`,
  `shadows.md`, `phase_transference.md`, `phase_localization.md`,
  `geometry.md`, `evidence/_index.md`: complete, every proof re-derived;
  `evidence/main.py`, `evidence/carry.py` and `evidence/shadows.py` were
  run, not read; the assets `evidence/assets/k003.json.gz`,
  `evidence/assets/k064.json.gz` and `evidence/assets/carry_witnesses.json`
  were read by the reviewer's scripts.
- `wiki/research/leads/totient_binary_series/sparse_transforms/_index.md`,
  `gap_multipliers.md`, `logarithmic_products.md`, `prime_sieve.md`,
  `evidence/_index.md`: complete, every proof re-derived;
  `sparse_transforms/evidence/main.py` was run, not read;
  `sparse_transforms/evidence/assets/witnesses.json` was read by script.
- `wiki/research/leads/totient_binary_series/evidence/_index.md`:
  complete; `evidence/main.py`: the docstring, the fixed expectations of
  both modes, the valuation, window and continued-fraction routines and
  the start of `main()` were read (lines 1 to 330), and the program was
  run in quick mode.
- `wiki/problems/irrationality/E0249/_index.md`: the Statement block only, the
  text above the heading `## Current assessment` (lines 1 to 83).
- Library result pages and source cards, mathematics only:
  `library/irrationality/kaneko_2026_refinements_erdos_s_irrationality_criterion_certain/theorem_1.md`,
  `theorem_3.md`, `corollary_2.md` (complete);
  `library/irrationality/bell_2026_mahler_series_multiplicative_coefficients/theorem_1_3.md`
  (complete);
  `library/irrationality/duverney_1995_irrationalite_q_analogue_zeta_2/_index.md`
  (body), `theoreme.md` and `lemme.md` (bodies through Step 7 of the
  lemma's proof);
  `library/irrationality/erdos_1948_arithmetical_properties_lambert_series/_index.md`
  (body) and the transcription
  `erdos_1948_arithmetical_properties_lambert_series.md` (lines 1 to 140,
  the whole proof for the divisor function);
  `library/irrationality/erdos_1988_irrationality_certain_series_problems_results/_index.md`
  (body, the quoted passages of printed p. 102).
- `wiki/research/leads/periodic_cell_face_certificates/evidence/verify/lead_periodic_cell_face_certificates_rereview.md`:
  frontmatter (lines 1 to 20) and its heading list only, for the shape
  of this record; its verdicts were not read.
- Operating instructions: `docs/verification.md`, `docs/evidence.md`,
  `docs/research.md`, `docs/approach_vetting.md`,
  `docs/math_authoring.md`, complete.

**Not read.** The live lead page `_index.md`; any problem page's Current
assessment; the claim card and proof of L16 under `wiki/theory/` (the
progression-means page restates its mean formula, refinement formula and
separation theorem with their proof mechanism, which were re-derived
there); any `evidence/verify/` record of any page; the held PDFs; the
extraction's cut logs.

**Exposures, each disclosed.**

1. The E0249 Statement block carries a `**Status.** Open` sentence with
   the date of a status search. Its content, that no proof or disproof
   was found, is the ordinary premise of a lead and added no mathematics.
2. The subpages' frontmatter carries lead-metadata keys:
   `research_state: ready` and `review_status: unreviewed` on
   `arithmetical_windows/_index.md`, `arithmetical_windows/classification.md`,
   `analytic_sources.md`, `integer_interpolation/_index.md`,
   `carry_criterion.md`, `two_depth_carries.md`, `shadows.md`,
   `phase_transference.md`, `phase_localization.md`, `geometry.md` and
   `sparse_transforms/_index.md`; `review_status: unreviewed` on
   `window_cost.md`, `progression_means.md`, `gap_multipliers.md`,
   `logarithmic_products.md`, `prime_sieve.md` and `computation.md`.
   They were skipped in substance; they say only that no review exists,
   which the assignment itself states, and they did not direct any
   attack. The research-state judgment at the end of this record is made
   from the body under the "Lead pages" rule, not from these keys.
3. Sentences of the form "author-recorded and unreviewed", "no
   independent review or native tier is claimed", "author-checked finite
   coverage", and the progression-means sentence placing L16 at tier 0,
   were skipped; they carry no finding about the mathematics.
4. The model record's `desc` summarizes its own verdict on a different
   lead; it was read for shape only and is immaterial here.
5. The Duverney source card's body carries one sentence reporting an
   earlier focused review of its Problem 250 specialization, with its
   verdict word; a different subject, immaterial to this route. The
   `theoreme.md` and `lemme.md` bodies carry "author-recorded" phrases,
   skipped.
6. The extraction itself retains three standing descriptors that
   survived the cut: "records its complete author proof" (Target and
   standing, on L16), "author-recorded results" (The dyadic rung, on the
   classification) and "author-recorded finite computation" (Finite
   observations). They influenced nothing.

No communication reached the reviewer besides the assignment, and no
search outside the listed paths was made.

**Independent computation.** The reviewer's checks are scratch scripts
kept in the review's working storage outside the repository; the Notes
section states each script's method and its exact output so that the
check can be rebuilt from the description. Their routes differ from the
lead's programs: the valuation census uses a vectorized windowed sum
modulo 2^64 instead of the sequential recurrence, the window census uses
a distinct-prime-factor sieve instead of the largest and second-largest
prime factor arrays, the certificate replays use `sympy` totients, and
the identities were tested with 120-digit arithmetic. This record
asserts no tier, and a scratch implementation is not offered as
recomputation evidence for one; the lead's own evidence programs were
also run and their outputs recorded.

## Restatement

The lead's target is the exact question of Problem 249: whether
$S=\sum_{n\ge1}\varphi(n)2^{-n}$ is irrational. The page claims no proof
or disproof. Its route consists of (i) exact consequences of a
hypothetical rational value $S=a/b$: the tail integers $I_N=bT_N$ with
$1\le I_N\le b(N+2)$, the residue formula modulo $2^m$, and the
valuation bound $v_2(\Phi_N)\le\log_2(b(N+2))$, so that unbounded
$v_2(\Phi_N)-\log_2N$ proves irrationality and infinitely many
excess-positive indices exclude a dyadic value; (ii) a proof that no
whole-progression eventual divisibility assertion can supply such
indices beyond $(n,m)=(5,3)$; (iii) a separation theorem for progression
means of nonzero absolutely summable totient kernels, with a precise
obstruction for fixed dilation grids; (iv) an integer interpolation
theorem giving, at every order $k$, finitely supported integers $y_n$
with $u\equiv2$, $v\equiv0\pmod{2^k}$ and $|uS-v|\le C_k(y)2^{-k}$, so
that a family with $C_k(y)=o(2^k)$ would prove irrationality, together
with weaker carry, two-depth, homogeneous odd-kernel, two-shadow and
phase criteria, two of which are proved equivalent to irrationality on
specified supports; (v) scoped obstructions to literal prime sieves,
logarithmic products and fixed dyadic filters, and a conditional signed
sparse-multiplier target under the Kaneko--Suzuki--Tachiya criterion;
(vi) finite observations to $10^7$ and a certified continued-fraction
prefix. Every quantitative estimate that would close the route is stated
as open.

## Statements and verdicts

Each label names the extraction's section and the sentence or display
it covers; a statement may cover a family of claims of the same shape.
Verdict words are written in full.

### Target and standing

- **T1** (first paragraph: convergence, the value, $S<2$, the certified
  prefix). Refutation-failed. $\varphi(n)\le n$ gives absolute convergence
  and $S<\sum n2^{-n}=2$ strictly because $\varphi(3)=2<3$; the partial sum
  through six is $41/32$ and $T_6\le8$ gives $S\le45/32$; 120-digit
  summation gives $1.36763080198502235079\ldots$, matching the stated
  prefix and the finite observations.
- **T2** (second paragraph: the route is open, the withdrawn single-index
  obstruction, what the next construction must do). Not a mathematical
  claim, except the withdrawal's reason, which is correct: a class modulo
  $M$ has a positive member below $M$ ($1\equiv1\pmod{10^6}$), so a bound
  on $M$ bounds no least representative without $N\ge M$.
- **T3** (third paragraph: the constructive link exists at every order,
  its proof bounds neither support nor coefficients, the shadow page's
  reverse implication is not for the full-vector cost). Refutation-failed
  as a description of Theorem 1 of the interpolation page and Corollary
  12 of the shadows page; see L1, L11. A suggested addition is filed: the
  geometry page retains an effective but useless bound.

### Notation and the tail integers

- **N1** (definitions of $\Phi_N$, $T_N$, both recurrences, $0<T_N\le N+2$).
  Refutation-failed. $2^NS=\Phi_N+\sum_{j\ge1}\varphi(N+j)2^{-j}$; the
  recurrences follow by splitting the top term; $\sum_j(N+j)2^{-j}=N+2$.
- **N2** (Lemma 1, tail integers). Refutation-failed. $I_N=b(2^NS-\Phi_N)$
  is an integer, positive since $T_N>0$, at most $b(N+2)$; the recurrence
  is $b$ times that of $T_N$; integrality of all $I_N$ is equivalent to
  that of $I_0=bS$ by the integer recurrence.
- **N3** (Lemma 2, residue formula, and the interval consequence).
  Refutation-failed. $\Phi_N=2^m\Phi_{N-m}+\Phi_{N,m}$ by splitting at
  $n\le N-m$; induction on $m$ gives $I_N=2^mI_{N-m}-b\Phi_{N,m}$; with
  $2^m>b(N+2)$ the least nonnegative residue of $-b\Phi_{N,m}$ is $I_N$
  itself, in $[1,b(N+2)]$.
- **N4** (Proposition 3 and its supremum criterion). Refutation-failed.
  For $N\ge4$, $9/8\le\Phi_N/2^N<S<2$ forces $m=v_2(\Phi_N)\le N-1$, so
  $2^m\mid\Phi_{N,m}$ and Lemma 2 give $2^m\mid I_N$, whence
  $2^m\le b(N+2)$. The bound in fact holds at $N=3$ too, and the supremum
  is bounded by $\log_2(3b/2)$, sharper than the stated $\log_2(3b)$;
  neither affects the criterion.
- **N5** (Proposition 3′, the odd-part bound, the ladder of sub-targets
  $b'=1,3,5,\ldots$). Refutation-failed. $1\le I_N<2^N\le v_2$-wise below
  $a2^N$ gives $v_2(b\Phi_N)=v_2(I_N)\le\log_2(b(N+2))$; subtracting
  $v=v_2(b)$ gives the odd-part bound; the exclusion statements for one
  index, infinitely many, and unbounded excess follow, the last using
  $v_2(\Phi_N)\le N-1$ to satisfy the hypothesis.
- **N6** (Carry dynamics: the min rule, the tie rule $a_N=u+v_2(x+y)$,
  every $N\ge2$ with $a_N\ge\log_2N$ is a tie, termwise clearing cannot
  witness). Refutation-failed. $\Phi_N=2\Phi_{N-1}+\varphi(N)$ with
  $v_2(\varphi(N))<\log_2N$ since $\varphi(N)<N$; off a tie
  $a_N\le u_N<\log_2N$. The six records to $10^7$ are all ties (Notes).

### A sufficient tail certificate and its actual limitation

- **C1** (the $(B_N,\varepsilon_N)$ certificate). Refutation-failed.
  $|bT_N-bB_N|\le b\varepsilon_N<\operatorname{dist}(bB_N,\mathbb Z)$
  puts $bT_N$ off the integers.
- **C2** (two-sided bound on the dropped tail and the threshold
  $H>\log_2(bN)-\log_2(1+\log_2N)$). Refutation-failed.
  $\varphi(n)/n\ge\prod_{i\le r}i/(i+1)=1/(r+1)$ with $p_i\ge i+1$ and
  $r\le\log_2n$; $x/(1+\log_2x)$ increases for $x\ge2$; the upper bound is
  $\sum_{j>H}(N+j)2^{-j}$. Checked numerically at $N=50$, $H=10$ (Notes).
- **C3** (the window page's modulus lower bound and what it does not
  bound). Refutation-failed. Lemma A (small-valuation cofactors by
  Dirichlet) and the count $\sum_{i<m}v_2(\varphi(g_i))\ge m(m-3)/2$
  against $\log_2M+E_m+m/2$ were re-derived; the page correctly states
  that no least-representative bound follows without $N\ge M$.

### The dyadic rung and what a progression can certify

- **D1** (Lemma D). Refutation-failed. It is Proposition 3′ at $b'=1$
  with hypothesis $2^N>2^v(N+2)$; one excess-positive index forces
  $v\ge N-\log_2(N+2)$.
- **D2** (the finite counts: 71 excess-positive indices in $[16,10^7]$,
  $N=3,5,10$ by hand, the record $N=2786632$ with valuation 29 excluding
  $v\le2786610$). Refutation-failed. Independently recomputed by a
  windowed sum modulo $2^{64}$: 71 indices, $\Phi_3=8$, $\Phi_5=40$,
  $\Phi_{10}=1392$, no other excess-positive $N<16$, and
  $N-\log_2(N+2)=2786610.59$ at the record (Notes).
- **D3** (the sentence "suggests about $5\ln X$ excess-positive indices
  below $X$"). Not a mathematical claim, labeled an observation; but the
  constant does not follow from the printed distribution. The empirical
  tail law $P(v_2(\Phi_N)\ge k)\approx10\cdot2^{-k}$ predicts about five
  indices per dyadic block, about $7\ln X\approx100$ at $10^7$, against
  the observed 71 (3.7 per block). A suggested correction is filed.
- **D4** (Lemma R: $2^m\le\min\{4\varphi(\gcd(n,M)),2\varphi(n)\}$ and
  $m\le i+v_2(\varphi(n-i))+1$, allowing cancellation, valid for $n<M$).
  Refutation-failed. Re-derived from the arithmetical-windows page:
  Lemma 1 (prime or semiprime cofactor with valuation at most
  $v_2(\varphi(g))+2$), Theorem 2 (fresh primes $q_j\equiv1\pmod{2^B}$
  isolate one term), Corollary 3, and Theorem 4 (prime squares $tp^2$ with
  $p\equiv-1\pmod{4M}$ and quadratic reciprocity for the roots). External
  inputs: Dirichlet, quadratic reciprocity.
- **D5** (the classification: existence iff the position inequalities
  for $n\ge m$; the sole pair $(5,3)$ with actual divisibility and excess,
  realized by $5\pmod{200}$; arbitrary Fermat primes handled).
  Refutation-failed. Every step re-derived, including the binary-digit
  count $2^r-1=2^s$, the $z\equiv7\pmod8$ and $\gcd(z,15)=1$ reductions,
  the three values of $\varphi(z)$, and the ratio contradiction
  $127/96>56/45$. An exhaustive search to $n\le200000$ finds only
  $(5,3)$; $\Phi_{17}=16\cdot11203$; $8\mid\Phi_{5+200h}$ for
  $h\le1999$ (Notes).
- **D6** (the coarse filter and its four indices; the example at 64 with
  the family $64p^2$ of valuation six; the sufficiency direction).
  Refutation-failed. $2^m\le4\varphi(\gcd(n,M))$ gives the necessary
  $2^{v_2(\varphi(n))+2}>n+2$; recomputation returns exactly
  $64,204,512,1632$; Theorem 4 at position zero with $n_0=64$ gives
  valuation $5+1=6$; the explicit prime-parameter family's CRT data were
  recomputed (Notes).

### Route one: Duverney's sparse product

- **R1a** (the description of Duverney's lemma and the direct $J_k$
  reconstruction). Refutation-failed. Pentagonal exponents give $k-1$
  zeros before $n_k$ and $2k$ after; $|J_k|\le|\delta||q|^{-k}((n_k+k)^2
  +4(n_k+k)+6)\to0$ from $\sum_{l\ge1}(A+l)^22^{-l}=A^2+4A+6$; then
  $q^k\mid\delta a(n_k)$ with $a(n_k)=(-1)^k(a+bn_k)$ polynomially
  bounded and eventually nonzero. Matches the library lemma page.
- **R1b** (the identities for $L$, $\exp L$, $c_p=(p-2)/p$,
  $c_{p^2}=(p-1)^2/p^2$, the Mellin transform, positivity of $\exp L$).
  Refutation-failed. $dc_d=\mu*\mu*\mathrm{id}$ from $\sum_{d\mid n}dc_d
  =\varphi(n)$; local factors computed; $\Gamma(s)\zeta(s-1)/\zeta(s)$ is
  the Dirichlet series of $\varphi$.
- **R1c** (the $\mathsf U$, $\mathsf U^{-1}$ frame for the three Lambert
  constants). Refutation-failed. Each of the four displayed identities is
  a Dirichlet convolution with $1$ or $\mu$ at the coefficient level.
- **R1d** (the two logarithmic-product obstructions). Refutation-failed.
  Proposition 1: $\varphi(p)=\psi_e(p)$ forces $e_1=-1$, $e_p=1$, then
  $pq(1-e_{pq})=2(p+q-1)$ is impossible for $p,q\ge5$. Theorem 2: at
  degree $mp$ only $r(p-1)/p$ and $r^p/p!$ are non-$p$-integral and
  $p!$ times their sum is $\equiv2r\pmod p$ by Wilson and Fermat, so the
  valuation is exactly $-1$; the prefactor adds nothing at degree $mp+h$.
- **R1e** (the prime-sieve obstruction $M_Q>S$ and
  $D_Q(M_Q-S)>2^{2P-9}/P^2$). Refutation-failed. The sieve identity
  $M_Q(x)=\sum_{(n,Q)=1}A(x^n)$, the remainder bounds
  $2^{-q}\le R_Q$, the cyclotomic valuation formula, $G_Q^2\mid D_Q$ and
  the two cases $3\nmid Q$, $3\mid Q$ (Bertrand) were re-derived; exact
  checks at $Q=15,21,30,70,210,2310$ confirm $G_Q^2\mid D_Q$ and the
  bounds (Notes).
- **R1f** (the gap-multiplier criterion survives; its finite form and the
  interpolation form are coefficient reversals; Euler's product gives the
  sigma case with a quadratic tail bound). Refutation-failed. The exact
  form $\Lambda(P)=\sum_ip_iT_{N-i}$, the congruences $u\equiv2$,
  $v\equiv b_N$, the bound $E_0(P)$, Lemma 3's parity, the truncation
  transfer and Proposition 4 on rational $F$ were re-derived; the five
  witnesses were replayed, and the reversal of $(100,20)$ has a nonzero
  coefficient at $n=20$ while the other four lie in $n\ge k+2$ (Notes).

### Route two: Erdős's arithmetic tails

- **R2a** (the description of the 1948 method and the two historical
  remarks). Refutation-failed as source fidelity: the transcription shows
  the CRT block $d(x+j+yA)\equiv0\pmod{t^{j+1}}$, the average
  $\sum_yd(\vartheta+yA)<cn\log n/A$ controlling a block of $10\log n$
  terms, and $d(r)<r$ for the far tail; the p. 66 and p. 102 quotations
  on the cards say what the lead says.
- **R2b** (the sharper elementary obstruction: a termwise block
  $2^j\mid b\varphi(N+j)$ cannot coexist with the crude-tail requirement
  $2^k>b(N+k+2)$). Refutation-failed. The last divisibility gives
  $2^k\le b\varphi(N+k)<b(N+k)$; the stronger block gives
  $2^{k+1}<N+k$, contradicting the requirement a fortiori.
- **R2c** (one-large-prime windows: 240 indices, the last at 31790, none
  with $N\ge2^{15}-1$, truncated-run statistic 20; $J_0$ "a necessary
  lower bound on the block length for the stated crude-tail
  certificate"). Refutation-failed. An independent census by a
  distinct-prime-factor sieve returns 240, last 31790, statistic 20
  (Notes). The phrase is correct for the certificate that bounds the tail
  by $(N+H+2)2^{-H}<1/b$, which needs $H>\log_2(N+2)$; a wording
  clarification is suggested, since the lower tail bound forces only
  $H>\log_2N-\log_2(1+\log_2N)$.
- **R2d** (the withdrawal of the exhaustion inference: residues modulo a
  product, not the prime-power lcm; a large modulus does not exclude a
  chosen member). Refutation-failed. Lemmas C and D of the window page
  were re-derived; the inference withdrawn was indeed invalid.

### Route three: the dilation argument

- **R3a** (the description of the external Problem 252 manuscript's
  structure, with correctness not assessed). Not a mathematical claim of
  the lead; it is a description of an external argument whose
  correctness the page explicitly does not assess. The citation names
  the external repository's commit; see the suggested corrections.
- **R3b** (Proposition 4: the expansion $\Lambda(N)=\sum_sA_N(s)\varphi(N+s)$,
  the lower bound $|A_N(s)|\ge\tfrac12(\varphi(p)/p)2^{-(s+t)/p}$ on
  $s\equiv-t\pmod p$ for $s\ge s_0$ uniformly in $N$, integrality of
  $b\Lambda(N)$). Refutation-failed. From
  $\varphi(p_e)\varphi(m)=\varphi(p_em)\varphi(g)/g$; competing dilations
  decay like $2^{-s/(p-1)}$ against $2^{-s/p}$, ratio
  $C2^{-s/(p(p-1))}$. Checked to $10^{-117}$ on the grid $p=(2,3)$,
  $t=(1,2)$, $w=(1,-1)$, $N=29$ (Notes).
- **R3c** (what follows analytically: coefficients independent of $N$ on a
  progression divisible by every $p_e^2$, the summable first moment, and
  the progression-mean theorem forbidding a fixed finite correction with
  $o(N)$ remainder). Refutation-failed. The mean
  $\kappa_Q(a)=\sum_{(d,Q)\mid a}\mu(d)(d,Q)/d^2$ and its Euler product,
  the refinement formula at a fresh prime $\ell$, the anchor-cutoff-prime
  separation with $\eta=|d_{s_*}|/[4\ell(1-\ell^{-2})]$, Lemma 2a's
  explicit error, and Corollary 3 were re-derived in full.
- **R3d** (the truncation at $H=\lceil c\log_2N\rceil$: remainder to
  infinity for $c<p$, to zero for $c>p$, positive limsup at $c=p$ by
  freezing the cutoff on $2^k<N\le2^{k+1/p}$). Refutation-failed. Lemma 4's
  bounds $2V(N+H+2p)2^{-H/p}$ and $\alpha N2^{-H/p}/(2(1+\log_2N))$ and
  Corollary 5's constant $|w_{e_*}|\varphi(p)\kappa_Q(0)/(8p)$ were
  re-derived, including $H_N=pk+1$ on the frozen interval and the single
  coefficient kernel in Lemma 2a.
- **R3e** (the factorial cousin $\sum\varphi(n)/n!$ is irrational).
  Refutation-failed. At $n+1=p>b$ prime, $1-1/p\le R_n<1-1/(2p)+5/(4p(p+1))<1$;
  numerically $R_6=0.94146$ at $p=7$ (Notes).

### Exact identities retained for later use

- **E1** (the three identities for $A(x)$, $\sum_kA(x^k)$ and $S$, with the
  cototient and sigma readings). Refutation-failed. One-line Möbius
  inversions; $\sum_d\mu(d)/(2^d-1)=1/2$ supplies the constant; the
  numerical residuals are below $10^{-119}$ (Notes).
- **E2** (the identity $A_{(p)}(x)=(p-1)\sum_{k\ge1}A(x^{p^k})$ and the
  even part of $S$). Refutation-failed. From
  $\varphi(pn)\in\{(p-1)\varphi(n),p\varphi(n)\}$ and iteration.
- **E3** (Lemma 5, the Möbius form of $T_N$, its odd denominators and the
  $O(1)$ control of the $d>N$ terms). Refutation-failed. Rearrangement by
  absolute convergence; the inner geometric sums evaluate as displayed;
  checked at $N=10$ to $10^{-117}$ (Notes).
- **E4** (the two-adic mirror and the denominator-growth remark).
  Refutation-failed. $2^d/(1-2^d)^2=\sum_kk2^{dk}$ converges in
  $\mathbb Z_2$ and the Möbius sum is $\sum\varphi(n)2^n$; the page draws
  no equality between the real and two-adic limits.

### Finite observations

- **F1** (the record list, the hit counts 72, 45, 21, 9, every record a
  carry tie). Refutation-failed. All recomputed independently, the six
  records included, by the windowed-sum census (Notes).
- **F2** (every rational value has a denominator of at least 6018 decimal
  digits; the bounds at $M=40000$ share 11759 partial quotients).
  Refutation-failed. Recomputed from $\Phi_{40000}/2^{40000}$ and
  $(\Phi_{40000}+40002)/2^{40000}$: common prefix 11759, largest quotient
  15531 at index 7055, last common convergent's denominator 6018 digits,
  determinant one, both bounds strictly inside the cylinder (Notes). The
  cylinder argument on the evidence page is correct: a rational strictly
  inside has denominator at least the convergent's.
- **F3** (the interpolation certificates: least full-image endpoints at
  nine orders, 36 central-zero solutions, cost 2433103 at $k=64$ with
  normalized bound $2433103/2^{64}$). Refutation-failed. All four $k=64$
  solutions and all four $k=3$ solutions satisfy their 128 or 6
  equations with independently computed totients; the costs match; the
  best $k=64$ cost excludes denominators through 7581571381774 (Notes).

### Prior work and reading limits

- **P1** (the Plectis page, issue 5037, the KST exponent target,
  Duverney 1993 and Nesterenko unread, the manuscript's checking level).
  Not a mathematical claim; a reading record. The KST remark is correct:
  Corollary 3 of that paper groups by totient values in the exponent. The
  external web pages were not inspected here.

### Remaining links and next constructions

- **L1** (Theorem 1 of the interpolation page: the normalized
  shifted-totient vectors span $\mathbb Z^r$ beyond every cutoff; the
  central-zero system (1) is solvable at every $k\ge3$).
  Refutation-failed. For each prime $p$ and coordinate $j_*$ the primes
  $q_j\equiv1\pmod{2p}$ and $t\equiv-1\pmod{2p}$, $t\equiv s_{j_*}-s_j
  \pmod{q_j}$ give $v(t-s_{j_*})\equiv-e_{j_*}\pmod p$; the $p=2$ vectors
  are $\mathbb Q$-independent, and a prime dividing the index would make
  the image modulo $p$ a proper subspace.
- **L2** (the displays for $\Lambda_k$, $u\equiv2$, $v\equiv0\pmod{2^k}$,
  $|\Lambda_k|\le C_k(y)2^{-k}$, and the exclusion $bC_k(y)<2^k$).
  Refutation-failed. $v=\sum y_n\Phi_n$ reduces to the nonpositive-shift
  equations through $\Phi_n\equiv\sum_{r<k}2^r\varphi(n-r)$; the tail is
  $\sum_{j>k}(2\varphi(j)+\sum_ny_n\varphi(n+j))2^{-j}$; the residue $2a$
  is nonzero below $2^k$.
- **L3** (the central-free system and Proposition 3). Refutation-failed.
  $c_0$ even, $2a-bc_0\ne0$ since $1<S<2$, and $|2a-bc_0|<b(4+|c_0|)<bC_k(y)$.
- **L4** (composition with the gap-multiplier criterion; four of five
  witnesses meet the stricter cutoff; $(100,20)$ does not).
  Refutation-failed. $p_{N-n}=y_n$, $p_N=2$, $E_0(P)=C_k(y)2^{-k}$,
  $b_N=c_0$; the replay confirms the support statement (Notes).
- **L5** (the sentence "the Dirichlet primes used to show solvability have
  no retained uniform bound"). Refuted-as-stated. The geometry page,
  dated 2026-09-19, retains Lemma 4a and Proposition 4: by Linnik's
  theorem the separating indices satisfy $n_i\le\exp(C_0k\log(pk+2))$,
  and the central-zero system has a solution with
  $\Gamma_k\le C_k(y)\le\exp(Ck^2\log(k+2))$ and support endpoint of the
  same order. The bound is useless for $o(2^k)$, but it is retained. A
  required correction is filed.
- **L6** (the aggregated carry criterion: the two aggregates, the
  identical tail bound, $\Gamma^*_k\le\Gamma_k$, witnesses about $2k^2$,
  the refuted uniform Fourier condition). Refutation-failed. Lemma 1's
  identity $\Lambda=2^{-k}W_k+\rho_k$, Proposition 2's residue argument
  with $|c|a<\tfrac3{10}bC_k$, the two-congruence equivalence under
  $2^L>C_k$, Theorem 4's character count and Proposition 4a's forced
  character $U_k(n)/2^{k+L}$ with at most two good indices were all
  re-derived; the $k=3$ witness $-e_5-e_6+e_{11}$ was recomputed.
- **L7** (the separate-depth criterion: exclusion when $bC_J<2^J$ and
  $3b\le2^{d+1}$; $d$ logarithmic; mixed integer image with $c=1$; the
  odd-pairing residue repair; a zero-$u$ repair vector costs at least
  $2^{J+1}$). Refutation-failed. Proposition 1 uses $v_2$ of $ca$ against
  $2^d$; Proposition 3 reads $\Phi_n/2$ modulo $2^{d-1}$ and $U_J(n)/2$
  through the span theorem on shifts $-d+2,\ldots,J$; Proposition 5
  inverts the odd pairing modulo $Q=2^{d-1}$; the zero-$u$ bound follows
  from $|\sum z_n\Phi_n|\ge2$ and $\sum z_nT_n=2^{-J}\sum z_nT_{n+J}$.
- **L8** (the homogeneous scalar-kernel criterion: $|uS-v|\le C/2^J$,
  $2^B\mid u$, $v_2(v)=1$, exact valuation $v_2(b)+1$ of $au-bv$, the
  family condition, the equal-cutoff bound $bC<2^{J+1}$, the general
  version with $W$). Refutation-failed. Proposition 6, Corollaries 7 and
  8 re-derived; the example $J=B=4$, $z=e_4+e_8-e_{12}$ gives
  $(U_4)=(56,88,144)$, $W=0$, $v=-5230$, $u=-3824$, $C=42$ (Notes).
- **L9** (odd kernel feasibility on $[J,2J]$ for large $J$ with
  $5\nmid J$ via two reduced classes modulo 20; the two-term vector's cost
  of order $J^22^J/g$; the positive-row comparison family).
  Refutation-failed. Parities $(A,V)\equiv(1,0)$ at a prime
  $n_1\equiv3\pmod4$, $n_1\equiv-J\pmod5$ and $(0,1)$ at $n_2=p-J$ with
  $p\equiv3\pmod4$, $p\equiv J\pmod5$; the fixed-modulus prime number
  theorem is an external input at its stated depth; the family
  $\widetilde V_i=Hi+1$ has every odd kernel vector of $\ell^1$ norm at
  least $H$.
- **L10** (the Fourier phase identity under rationality and the lower
  bound $C\ge2^{J+1}/b$). Refutation-failed. For odd $b$ and $n\ge4$,
  $I_n\equiv2A_n\pmod4$ gives $\theta_*V_n\equiv A_n/2-bT_{n+J}/2^{J+2}$;
  the half-integer pairing argument gives $C\ge1/(2\epsilon)$.
- **L11** (the shadows page: two non-proportional shadows exclude
  $b<2^J/C$; rounding against zero-shadow vectors gives an odd vector at
  polynomial extra cost; irrationality supplies $O(J^4)$ odd vectors on
  $[B_J,3J]$ along powers of two; the converse with $B_J\to\infty$; the
  determinant-scaled reverse construction with $R=J+O(\log J)$).
  Refutation-failed. Lemma 2's collision count, Lemma 3's approximation
  (2), Lemma 5's chaining exponent $J'-3J+2B+4$, Theorem 6's class-maximum
  argument, Lemma 10's cross vectors, Propositions 11 and 14 and
  Corollaries 7a, 12 and 15 were re-derived; no step assumes more than
  it states.
- **L12** (a flat depth is a terminal rational or an exceptionally good
  convergent; non-flatness for $B=4$, $33\le J\le19950$). Refutation-failed.
  Proposition 8 follows from Legendre's theorem and (2); the finite range
  was replayed by the lead's `shadows.py` (Notes).
- **L13** (phase comparison: $1/(2\epsilon_J)\le C_{\rm odd}<3/\epsilon_J
  +O(J^{9/2})$ on linearly growing supports; equivalence of
  $C_{\rm odd}=o(2^J)$ with $\epsilon_J2^J\to\infty$). Refutation-failed.
  The index-two Gaussian transference $\lambda\delta<(d+4)\log2/\pi$ was
  re-derived from the Poisson identity; the dual coset identification
  uses that $\ker_{\mathbb Z}V$ is primitive; Theorem 4's reduction to the
  two-dimensional shadow quotient and bound (9) give the stated order.
- **L14** (phase localization: the short-support equivalence
  $S\notin\mathbb Q\iff\limsup_{J=2^m}\epsilon_J2^J=\infty$, the inputs
  $\varphi(3k)=2\varphi(2k)$ and two fixed-modulus prime choices, the
  finite test over odd $q\le26M(3J+2)$). Refutation-failed. Proposition
  2's chain was re-derived: the minor argument giving $|\theta-r/G|\le E$,
  the integers $q_t=Qa_t$ by the gcd hypothesis, the odd $q$ with
  $|q|\le26\delta2^JH$, the identity (9) with the omitted integer term
  $(q+1)\Phi_n/4$, and the doubling of residuals $f_{n+1}=2f_n$ below
  $1/3$; Theorem 3's dyadic-factor comparison (10) is correct. The $J=32$
  structural values $D_{17}=21$, $D_{19}=20$ were recomputed (Notes).
- **L15** (the one-window phase formulation and the exponential-sum
  reformulation). Refutation-failed. $bT_N=bU_J(N)/2^J+bT_{N+J}/2^J$ with
  $0<bT_{N+J}/2^J\le2^{-C}$ places the residue in the top interval;
  $|e(x)-e(y)|\le2\pi|x-y|$; a saving for $b$ excludes every divisor of
  $b$; $e(bT_N)=e(b2^NS)$.
- **L16** (the signed sparse-multiplier target under KST Theorem 3 and
  the bound (22)). Refutation-failed, conditional on Theorem 3 as the
  library extraction states it. With $a(n)=Bv_n$, $b(n)=-Ag_n$,
  $z_j=\lceil(d+2)\log_2x_j\rceil$, the mass $O(x_j^{d+1})$ is
  $o(2^{z_j}x_j)$, the supports are $o(x_j/z_j)$, the gap condition is
  item 3, and the series equals the integer $Ag_0$; (22) follows from
  $N+h+u+1\le(N+h+1)(u+1)$. Nonnegative $G$ is excluded as stated.
- **L17** (the geometry page: Proposition 1's rounding bound (2)-(3),
  the singular-value bound $\sigma_{\min}(A)\ge X^{3/2}/(4\zeta(2))$ for
  $X\ge\lceil4096k^2\log(k+2)\rceil$ and $R=2\ell X+\ell+k-1$, the real
  contribution below $512k^3$, the two unimodular counterexamples).
  Refutation-failed. The mean-square identity (9) over the $\ell$ classes,
  the error constants $E_1,E_2<1/(64k^{3/2})<\kappa/(4\ell^{3/2})$, and
  $(R+k+2)\sqrt M\|x_0\|_2\le256k^3/\kappa$ were re-derived; the
  bidiagonal examples have the stated solutions.
- **L18** (analytic sources: $F$ is not $k$-Mahler for any $k$; the
  fixed-filter support obstruction; transcendence of finite odd-orbit
  subseries; the positive-transfer obstruction). Refutation-failed,
  conditional on Bell--Smertnig Theorem 1.3 and KST Theorem 3 and
  Corollary 2 as extracted. $\chi(\ell)=(\ell-1)/\ell^r$ has infinite
  image for every $r$; the filter's coefficient at $2^{j_0}m$ is
  $c_{j_0}\varphi(m)$; the orbit bounds (16)-(17) hold; the elementary
  obstruction (20) is exact in both parities of $N$.
- **L19** (the closing sentences: the irrationality target is
  unsupported; the listed open constructions and their shared-parameter
  obligation). Not a mathematical claim beyond what is checked above; the
  page's own account of what remains open is accurate.

## Checklist

Verdicts against the Erdos audit checklist, applied to the proof sketch
as the extraction states it.

- **Quantifiers and scope.** Pass. The page keeps "infinitely many
  excess-positive indices" (dyadic rung) apart from "unbounded excess"
  (full criterion), limsup apart from limit (Corollary 5, Theorem 3 of
  the localization), every-member apart from selected-member
  (Lemma R, the classification), and subsequence equivalences apart from
  all-depth statements (shadows, localization). No almost-all is read as
  all.
- **Circularity.** Pass. No argument assumes irrationality except the
  reverse implications that say so (Theorem 6 part 2, Corollaries 12 and
  15, the localization's Theorem 3), and those are presented as
  equivalences, not constructions. The one-window phase identity
  $e(bT_N)=e(b2^NS)$ is labeled a reformulation.
- **Model and convention changes.** Pass. The progression-mean argument
  works with the actual kernels and exact means; the fixed-grid
  obstruction is applied only to the fixed-grid family; the shadows and
  phase quotients are exact lattices, with rounding costs bounded, not
  relaxed systems.
- **Finite and statistical overreach.** Pass, with one soft spot. Every
  finite count is labeled finite; the continued-fraction exclusion is
  stated as a finite exclusion. The "about $5\ln X$" rate is labeled an
  observation, but its constant is not derived from the printed data
  (D3); a suggested correction is filed. No statistical inference is
  drawn from the correlated samples.
- **Uniformity.** Pass. The uniform statements have their parameter
  dependence stated: Proposition 4's $s_0$ depends only on the grid
  data; Corollary 3 of the geometry page is uniform in $X$ with
  constants independent of $X$; Lemma 2a's error is explicit in
  $R,T,X,H$; the interpolation theorem is explicitly non-uniform in $k$.
- **Extremal conclusions.** Pass. Costs are reported as upper bounds for
  feasible vectors, never as minima; the one minimum claim (leading
  coefficient two is least) is proved by the parity lemma; the box minima
  are stated as minima over their boxes only.
- **Consequences and composition.** Pass, one defect in a consequence
  sentence. Every "hence" was attacked separately; all hold except the
  sentence refuted in L5, which asserts the absence of a bound that a
  subpage of the same lead retains. The composition of the interpolation
  theorem with the gap-multiplier criterion inherits exactly the stated
  open estimate and nothing is presented as unconditional.
- **Computation.** Pass. Exact integers, fractions and integer
  comparisons are used wherever a decision is made; the accumulator cap
  is checked; the independent recomputations agree on every figure.
- **Reproduction.** Pass. The rerun lines were executed verbatim from the
  repository root (quick modes where offered) and passed; their figures
  were reproduced by structurally different scratch routes (Notes).
- **Source and verdict fidelity.** Pass. The Duverney, Erdős 1948 and
  Erdős 1988 descriptions match the library cards and the transcription;
  the KST and Bell--Smertnig hypotheses are quoted at their actual
  strength, and the specializations are correct.

## Weakest steps

1. **The route's load-bearing gap is quantitative, not logical.** Every
   sufficient criterion on the page (Proposition 3, Lemma D, Proposition
   2 of the interpolation page, Propositions 2 and 3 of the carry page,
   Corollary 7 of the two-depth page, Proposition 1 of the shadows page,
   Corollary 5 of the phase page) is a correct implication whose
   antecedent is an unproved growth or smallness estimate. Re-derived:
   each antecedent is stated with its exact quantifier, and the page
   never passes from a finite witness or a qualitative existence theorem
   to the estimate. The chain is sound and conditional.
2. **The classification's exclusion of Fermat primes beyond the known
   list.** The step from $\varphi(z)=3\cdot2^{e-3}$ with $z\equiv7\pmod8$
   to $z=7\times$(Fermat primes $\ge17$) and the ratio bound
   $z/\varphi(z)<56/45$ against $\ge127/96$ was the most intricate
   elementary argument; re-derived in full, including the two digit-count
   identities and the exclusion of $p=3\cdot2^h+1$ for $h\ge2$. It holds
   for every $e\ge8$ with no assumption on which Fermat numbers are prime.
3. **The localization's Proposition 2.** The passage from a small phase
   $\theta$ to an odd dyadic numerator $q$ uses two integer-minor
   arguments whose thresholds ($18\delta HD_*<1$, $15\delta H^3<1$) must
   be met simultaneously, the oddness of $G$ to preserve the half-integer
   target, and the exact identity (9) whose omitted term
   $(q+1)\Phi_n/4$ is integral only for odd $q$. Each threshold was
   recomputed from the stated inequalities; the constants 26, 31, 38 and
   152 hold with room, and the doubling of residuals needs $38\delta H^2
   <1/3$, which $18\delta H^3<1$ and $H\ge14$ give.

## Strongest attack

The strongest attack sought a counterexample to the rigidity claim that
no whole-progression certificate can deliver excess-positive indices
other than $(5,3)$, since a single further pair would reopen the dyadic
rung by eventual divisibility. The attack had two prongs. First, an
exhaustive search over $n\le200000$ for pairs $(n,m)$ with
$2^m\mid\Phi_n$, $2^m>n+2$ and all position inequalities
$m\le i+v_2(\varphi(n-i))+1$ returned only $(5,3)$; the search is
independent of the page's Fermat-prime reasoning and covers every pair
the theorem's necessity direction could admit in that range. Second, the
necessity direction itself was attacked at its external inputs: Theorem
4 needs a prime $p\equiv-1\pmod{4M}$ with prescribed residues modulo the
auxiliary primes $q_j$, and the roots $a_j$ exist only if $t\delta_j$ is
a square modulo $q_j$; with $q_j\equiv1\pmod{2^{\max(B,3)}t|\delta_j|}$
every odd prime factor of $t\delta_j$, and also $-1$ and $2$, are
squares modulo $q_j$ by reciprocity and the supplementary laws, and
$q_j\nmid t\delta_j$ since $q_j>t|\delta_j|$. The attack failed: the
construction is correct, and the family $N=tp^2-s_{j_0}$ has the exact
valuation $v_2(c_{j_0})+v_2(\varphi(t))+1$ at the selected term with
every other term divisible by $2^{e+1}$.

A second attack targeted the dyadic-rung count itself: a windowed-sum
census that never forms the recurrence reproduced the 71 indices, the
four filter survivors, the six records and their carry ties, so no
accumulator or off-by-one defect in the lead's program hides a
miscount. A third attack targeted the certified continued-fraction
exclusion by recomputing both rational bounds and their expansions with
Euclid's algorithm alone: the common prefix, the largest quotient, the
6018-digit denominator and the strict cylinder containment all agree.

The only successful attack is on a sentence, not a theorem: the claim
that the Dirichlet primes have no retained uniform bound is contradicted
by the geometry page's Linnik bound (L5). It changes no standing: the
retained bound is $\exp(O(k^2\log k))$, far above the $o(2^k)$ the
criterion needs, so the route's open estimate is exactly as the page
describes it elsewhere.

## Premises

**Local claims consumed.** L16 (the totient kernel separation theorem)
is consumed by the progression-mean obstruction (R3c, R3d) and by the
geometry page's singular-value bound through Lemma 2a. Its statement
and proof mechanism were re-derived from the progression-means page;
its card was outside this review's read set, so its live standing is not
reported here and no tier is asserted for anything that consumes it. No
other native claim is consumed.

**External premises, with the reading depth the pages state.**

- Dirichlet's theorem on primes in reduced progressions: consumed by the
  isolation theorems, the classification, the integer span theorem and
  the geometry page; statement inspected, proof not rechecked.
- Quadratic reciprocity with its supplementary laws: consumed by
  Theorem 4 of the arithmetical-windows page; statement inspected.
- The prime number theorem in progressions for the fixed moduli 20, 4
  and 36: consumed by Proposition 9 of the two-depth page, Corollary 15
  of the shadows page and Lemma 1 of the localization; statements
  inspected.
- Linnik's theorem with an effective exponent: consumed by Lemma 4a and
  Proposition 4 of the geometry page; statement inspected.
- Bertrand's postulate: consumed by the prime-sieve obstruction and the
  geometry page; the 1932 source statement inspected.
- Euler's pentagonal number theorem and Théorème 2 of Duverney 1993:
  consumed by the calibration and by the library lemma; the lead's own
  $J_k$ reconstruction removes the 1993 criterion from the comparison.
- Kaneko--Suzuki--Tachiya Theorems 1 and 3 and Corollary 2: consumed by
  the signed-multiplier target and the odd-orbit transcendence;
  statements checked against the page images per the library pages,
  proof routes read, no complete source-proof reconstruction.
- Bell--Smertnig Theorem 1.3: consumed by the non-Mahler specialization;
  statement compared with the source image per the library page, with
  external classifications unreread.

**Explicit assumptions and what remains unproved.** The conclusion
"$S$ is irrational" rests on none of the above; it rests on one of the
following unproved estimates, each stated as open by the page: unbounded
$v_2(\Phi_N)-\log_2N$, or infinitely many excess-positive indices for
the dyadic rung; $\liminf\Gamma_k/2^k=0$ or the weaker
$\Gamma^*_k$, $\Gamma^{(1)}_{d,J}$, $\kappa_{B,J}$ versions;
$\limsup_{J=2^m}\epsilon_J2^J=\infty$; a signed sparse multiplier $G$
meeting the KST hypotheses; or a construction forcing a nonzero null
kernel from rationality. The route as written stands on these as
premises for its conclusion and on nothing hidden: every implication
that uses one of them is marked conditional, and no conditional
conclusion is presented as unconditional.

## Required corrections

One. **Remaining links and next constructions, the paragraph that
follows the display of $\Lambda_k$, its last sentence**, which reads
"All existence quantifiers in the proof precede any limit in $k$; the
Dirichlet primes used to show solvability have no retained uniform
bound." Replace it with:

> All existence quantifiers in the proof precede any limit in $k$. The
> only retained quantitative version, Proposition 4 of the
> [[research/leads/totient_binary_series/integer_interpolation/geometry|geometry
> page]], uses Linnik's theorem to produce a solution with
> $C_k(y)\le\exp(Ck^2\log(k+2))$ for an effective absolute constant
> $C$; this is far above the required $o(2^k)$.

Reason: the sentence denies a bound that the lead's own geometry page,
dated 2026-09-19, retains (L5). The correction changes no mathematical
standing, since the retained bound does not approach the criterion.

## Suggested corrections

One. **Target and standing, third paragraph, the sentence "The proof
does not bound its support or coefficients."** Append:

> An effective bound, $\exp(O(k^2\log(k+2)))$ by Linnik's theorem, is on
> the geometry page; it is too large to use.

Two. **The dyadic rung, the paragraph after Lemma D, the sentence
beginning "The evidence's valuation distribution suggests about
$5\ln X$".** Replace it with:

> The evidence's valuation distribution, roughly
> $P(v_2(\Phi_N)\ge k)\approx10\cdot2^{-k}$ for $k\ge6$, would predict
> about five excess-positive indices in each dyadic block of $N$; the
> observed blocks through $10^7$ hold between zero and ten, 71 in all.
> Both figures are observations, not theorems.

Reason: the constant five per $\ln X$ cannot be read off the printed
distribution; the direct extrapolation is about five per dyadic block,
roughly $7\ln X$, above the observed count (D3, Notes).

Three. **Route two, the one-large-prime window paragraph, the sentence
"The finite evidence tests this property with $J=J_0(N)=\lceil\log_2
(N+2)\rceil$, a necessary lower bound on the block length for the stated
crude-tail certificate."** Replace the clause after the comma with:

> the least block length at which the crude upper bound $(N+H+2)2^{-H}$
> on the discarded tail can fall below one; the lower tail bound above
> forces only $H>\log_2N-\log_2(1+\log_2N)$.

Reason: "necessary" is true of the certificate that uses the upper
bound, but the paragraph's own displayed lower bound forces a weaker
threshold, and a reader can take "necessary" to refer to it (R2c).

Four. **Route three, the first sentence**, which names the external
Problem 252 manuscript by its repository commit identifier. Either state
in that sentence that the exact revision is relied on because the
structural description that follows was read from it, or cite the
manuscript by its announcement date (8 September 2026) and file name
alone. Reason: convention 9 (Paths and dates, not hashes) admits an
external commit only where a record relies on that exact external
content; the page says only the argument's structure is used, so the
reliance should be explicit or the identifier dropped (R3a).

## Notes

All commands were run from the repository root on 2026-10-03 against
the tree as it stood that day. Outputs are quoted exactly, trimmed to
the lines that carry a figure used above.

### The lead's evidence programs

```sh
uv run --no-sync python wiki/research/leads/totient_binary_series/evidence/main.py --quick
```

```text
mode=quick X=1000000 M=4000
one-large-prime windows of length ceil(log2(N + 2)): 240, last at
  N = 31790, longest truncated run for N >= 32767: 18
valuation m, count on [X/2, X], count / (total * 2^-m):
   6     35717    4.572
   7     17873    4.575
  10      2224    4.555
S = 1.367630801985022...; certified prefix length 1171
largest certified partial quotient 3281 at index 911
denominator of the last certified convergent has 599 decimal digits
ALL CHECKS PASS (19 checks)
```

```sh
uv run --no-sync python wiki/research/leads/totient_binary_series/arithmetical_windows/evidence/main.py
```

```text
  [ok] seed Phi_64 has exact valuation ten
  [ok] prime-square signed sum has exact valuation one
  [ok] the CRT class puts a fresh prime at each unwanted position
ALL CHECKS PASS (20 checks)
```

```sh
uv run --no-sync python wiki/research/leads/totient_binary_series/integer_interpolation/evidence/main.py
```

```text
  k=64: minimum R=194; best retained C=2433103,
  ratio=2433103/18446744073709551616, support=[66, 386, 284],
  max|y|=314, denominators excluded through 7581571381774
ALL CHECKS PASS (55 checks)
```

```sh
uv run --no-sync python wiki/research/leads/totient_binary_series/integer_interpolation/evidence/carry.py --quick
uv run --no-sync python wiki/research/leads/totient_binary_series/integer_interpolation/evidence/shadows.py --quick
```

```text
ALL CHECKS PASS (11 checks)
  [ok] finite corollary: quotient bound holds at J=33 and fails at J=32
  [ok] finite corollary: denominator bound holds at J=19950 and fails
       at J=19951
  [ok] finite corollary: all four inequalities hold at every J=33..19950
ALL CHECKS PASS (16 checks)
```

```sh
uv run --no-sync python wiki/research/leads/totient_binary_series/sparse_transforms/evidence/main.py
```

```text
  [ok] Q=21: nonprimitive cyclotomic prime occurs and is removed
ALL CHECKS PASS (112 checks)
```

### The reviewer's independent checks

The scripts live in the review's working storage outside the
repository and read only the paths named in the subject. Each is
described by its method so that it can be rebuilt.

**Valuation census.** Sieve $\varphi$ to $10^7+64$ with `numpy`; form
$\Phi_N\bmod2^{64}$ as the windowed sum $\sum_{i<64}\varphi(N-i)2^i$ in
`uint64` with wraparound, never through the recurrence; take trailing
zeros; control against exact integers for $N\le300$.

```text
control: windowed valuations agree with exact Phi_N for N<=300
max valuation for 1<=N<=X: 29  (cap 64 hit: 0 )
hits excess>=0 on [16,X]: 72
hits excess>=1 on [16,X]: 45
hits excess>=2 on [16,X]: 21
hits excess>=3 on [16,X]: 9
excess-positive count on [16,X]: 71
excess-positive meeting 2^(v2(phi(N))+2) > N+2: [64, 204, 512, 1632]
excess-positive N<16: [3, 5, 10] with Phi_3,Phi_5,Phi_10 = 8 40 1392
records (N, v_2(Phi_N)): [(16, 4), (28, 6), (64, 10), (88, 12),
  (2146743, 28), (2786632, 29)]
  N=16: v2(phi(N))=3, 1+v2(Phi_(N-1))=3, tie=True, excess=0.000
  N=28: v2(phi(N))=2, 1+v2(Phi_(N-1))=2, tie=True, excess=1.193
  N=64: v2(phi(N))=5, 1+v2(Phi_(N-1))=5, tie=True, excess=4.000
  N=88: v2(phi(N))=3, 1+v2(Phi_(N-1))=3, tie=True, excess=5.541
  N=2146743: v2(phi(N))=6, 1+v2(Phi_(N-1))=6, tie=True, excess=6.966
  N=2786632: v2(phi(N))=4, 1+v2(Phi_(N-1))=4, tie=True, excess=7.590
largest record N=2786632: N - log2(N+2) = 2786610.590
empirical P(v_2(Phi_N) >= k) * 2^k:  k=6: 10.212  k=10: 10.257
  k=15: 10.338  k=20: 9.647
heuristic expected excess-positive count from empirical tail law:
  101.3  vs 5 ln X = 80.6
```

Per dyadic block $[2^{J-1}-1,2^J-2]$ the 71 indices fall as
$2,0,2,4,2,2,4,3,3,5,3,2,3,2,3,5,6,10,9$ for $J=5,\ldots,23$ and $1$ in
the partial block $J=24$.

**Window census.** Sieve the number of distinct prime factors to
$10^7+25$; for the block of each $J$ subtract the indicators of the
primes $p\le J$; a window is full when the $J$ indicators after $N$ all
equal one; the truncated run is the run of ones from $N+1$ scanned to
the block end plus $J$. The reviewer's first vectorized version tested
the window $N,\ldots,N+J-1$ by an off-by-one and reported the last index
as 31791; the corrected version, a direct per-$N$ census to 40000, and
the lead's own routine called directly on $N\le40000$ (returning
`(240, 31790, 14)`) all agree.

```text
total one-large-prime windows N<=X: 240  last N: 31790
truncated-run statistic over N >= 32767 : 20
```

**Continued fraction.** Exact $\Phi_{40000}$ by the recurrence; Euclid's
algorithm on both bounds; convergents of the common prefix.

```text
depth M = 40000  common prefix length = 11759
first terms: [1, 2, 1, 2, 1, 1, 2, 1, 12]
largest quotient in common prefix: 15531 at 0-based index 7055
denominator digits of last common convergent: 6018
determinant |p1 q0 - p0 q1| = 1
both bounds strictly inside cylinder: True
decimal prefix of lower bound: 1367630801985022
```

**Interpolation certificates.** Decompress `k003.json.gz` and
`k064.json.gz`; recompute every equation with `sympy` totients and every
cost from the coefficients.

```text
k=64 B=66 status=full_image minimal_R=194 (128 shifts)
  right_inverse: R=194 eqs_ok=True matches_record=True nonzero=129
  coset_R258: R=258 eqs_ok=True recomputed_cost=11921743 nonzero=193
  coset_R386: R=386 eqs_ok=True recomputed_cost=2433103 nonzero=284
    support=[66,386] max|y|=314
  coset_R514: R=514 eqs_ok=True recomputed_cost=2731713 nonzero=294
  best cost 2433103; b_max = floor((2^k-1)/cost) = 7581571381774;
    ratio cost/2^k = 1.319e-13
k=3 exposed example row products (s=-2..3): [0, 0, 0, -2, -2, -4]
  cost = 109
```

**Gap-multiplier witnesses and sieve denominators.** Rebuild each dense
$P$, convolve with $\varphi$, test (G1), (G2), height, central
coefficient and the reversed support; reduce $M_Q$ exactly and compute
$\Psi_Q(2)$ with `sympy`.

```text
(N,k)=(100,20): G1=True G2=True height=11 central=-58 deg_P0=80
  reversed_support_in_n>=k+2=False
(N,k)=(160,28): G1=True G2=True height=18 central=230 deg_P0=130
  reversed_support_in_n>=k+2=True
(N,k)=(300,28): G1=True G2=True height=26 central=192 deg_P0=155 True
(N,k)=(300,32): G1=True G2=True height=27 central=62 deg_P0=170 True
(N,k)=(900,32): G1=True G2=True height=67 central=-7726 deg_P0=186 True
Q=30: P=5 q=7 G_Q^2|D_Q=True D_Q>2^(2phi-4)/P^2=True M_Q>S=True
  R_Q>=2^-q=True D_Q*R_Q=3.2645971e+15 bound 2^(2P-9)/P^2=0.08
Q=210: P=7 q=11 all True D_Q*R_Q=1.8660869e+122 bound=0.65306122
Q=2310: P=11 q=13 all True D_Q*R_Q=2.7986309e+1385 bound=67.702479
Q=21, Q=70, Q=15: all True
```

**Classification and window data.** Exact $\Phi_n\bmod2^{64}$ to
$4\cdot10^5$; search all $(n,m)$ with $2^m\mid\Phi_n$, $2^m>n+2$ and
the position inequalities; recompute the arithmetical-window constants.

```text
pairs (n,m) with 2^m|Phi_n, 2^m>n+2 and all position inequalities,
  n<=200000: [(5, 3)]
Phi_17 = 179248 = 16 * 11203 remainder 0
8 | Phi_N for all N=5+200h, h=1..1999: True
v_2(Phi_N) for N=5^(2t+1), t=1..3: [2, 2, 2]
v_2(Phi_64) = 10  Phi_64 mod 2048 = 1024
L = lcm(55..64) = 13632589333440  L/64 = 213009208335  v2(L) = 6
q_i prime and 1 mod 128: True
CRT class modulus and residue match the evidence account: True
prime-square witness p=647: phi(N),phi(N-1),phi(N+1) =
  (417962, 124416, 163200)  signed sum = -130346, mod 4 = 2
N=15131: prime, v2(Phi_N)=1   N=89013: 3*29671, v2(Phi_N)=2
J=32: D_17 = 21  D_19 = 20  a_64 = 16  a_43 = 21
J=4 example: U_4(4),U_4(8),U_4(12) = 56 88 144  W = 0  v = -5230
  u = -3824
k=3 carry witness: v = 2672  W_3 = 0
```

**Identities.** 120-digit `mpmath` arithmetic with $\varphi$ to 3000.

```text
S = 1.36763080198502235079050814621
S - (1/2 + sum mu(d)/(2^d-1)^2) = 0.0
sum_k A(2^-k) over k<=400 - 2 = -1.1618e-120
Lemma 5 at N=10: T_10 - formula = -4.0895e-118
Prop 4: Lambda(N) - sum_s A_N(s) phi(N+s) = -2.3239e-117
  (grid p=(2,3), t=(1,2), w=(1,-1), N=29)
  s=1000: |A_N(s)| / ((1/2)(phi(p)/p) 2^(-(s+t)/p)) = 3.0
  s=1006: ratio = 2.0   s=2401: ratio = 2.0
factorial cousin p=7: R_6 = 0.941457670724  in [1-1/7, 1): True
tail N=50,H=10: 0.04552350962  lower 0.007349365129  upper 0.060546875
41/32 < S <= 45/32: True
```

## Verdict

**Refutation-failed** for the route as the extraction states it, with
one consequence sentence **refuted-as-stated** (L5) and no mathematical
statement refuted or left with a defective proof. Every held link was
re-derived: the tail integers and the residue formula, the valuation
criterion and its odd-part and dyadic forms, the carry dynamics, the
isolation theorems and the exact classification with its sole pair
$(5,3)$, the progression-mean separation with its explicit error bound
and the fixed-grid obstruction at the critical scale $c=p$, the integer
span theorem and the complete-tail criteria in their central-zero,
central-free, aggregated, two-depth and homogeneous forms, the two-shadow
and flatness results with their reverse implications, the phase
transference and the short-support localization equivalence, the
logarithmic-product and prime-sieve obstructions, the gap-multiplier
criterion with its Euler calibration, the KST and Bell--Smertnig
specializations, the retained identities, and every finite figure.

The route's conclusion remains conditional on one of the unproved
estimates listed under Premises; the page says so at every point. The
external inputs are consumed at the reading depth the pages state, and
no conclusion about $S$ depends on them unconditionally.

Under the "Lead pages" rule, a ready lead's bounded next investigation
must have its necessary inputs. The body names several bounded next
investigations whose inputs are in the tree: the finite exact phase test
(11) of the localization page at chosen $(M,J)$, which needs only
totients through $3J$; the conditioned residue count of the two-depth
page on explicit bounded slices; the structured-multiplier system (8) of
the gap-multiplier page; and the odd-kernel minimum on $[J,2J]$ along
powers of two, whose feasibility is proved. The body therefore warrants
the research state `ready`, once the required correction is applied; it
does not warrant `blocked`, since no stated prerequisite is missing, and
not `closed`, since the target is unresolved and the route is live. This
record asserts no tier: it is a first-cycle review of a lead, not of a
claim card, and its scratch recomputations are reported, not retained as
evidence.

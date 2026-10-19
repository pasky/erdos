---
name: research/erdos_1221/evidence/verify/connections_problem_480_the_clustering_constant_and_the_sect_review
title: "Independent review of the connections section: Problem 480: the clustering constant and the Section 4 count"
desc: |
  Refutation review of the Problem 480 section: Proposition 480.1, the
  interval bound 1/log 4, the incomparability of C and omega and the descent
  analysis survive attack, while the sharpness paragraph's argument is
  defective (its exact description of the log sequence's first n terms and
  smallest gap fails unless n is a power of 2; the limit survives). One
  required correction, one suggested change, two notes.
created: 2026-09-28T19:18:54Z
updated: 2026-09-28T20:46:21Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context, given only the
commissioning assignment. The reviewer took no part in writing the page,
the reconstructions or the library cards, and read no review, grade,
assessment or standing text beyond the exposures listed below. Charge:
refutation of the author-recorded mathematics of one section.

**Subject.** Page `wiki/research/erdos_1221/connections.md` as it stood on
2026-09-28T13:50:48Z, section "Problem 480: the clustering constant and the
Section 4 count", lines 195--332 (the H2 heading at line 195 to the line before
the next H2 at line 333). Within it: the Target paragraph (197--220),
Proposition 480.1 with its proof (225--276; the sharpness paragraph is
271--276), the obstruction paragraph (278--284), the three "What it does not
give" bullets (286--318), the Next investigation (319--326) and the Outcome
(328--331). Lead pages: none named by the assignment; the section targets
[[problems/number_theory/E0480/_index|Problem 480]] and touches
[[problems/analysis/E1221/_index|Problem 1221]] only through the folder's notation.

**Reading and depth.**

- The section, clause by clause, and the page's shared opening (lines
  1--43: purpose, notation, the 1949 constants, the counting notation) as
  inputs.
- [[research/erdos_1221/dber49_inequality_4_3_reconstruction|The (4.3) reconstruction]]
  in full, as a premise at its reviewed standing; the definitions,
  statement, Section 8 argument and imported-inputs list of
  [[research/erdos_1221/ko26b_theorem_1_1_reconstruction|the Theorem 1.1 reconstruction]],
  to check the section's "discrepancy route" sentence.
- The Statement of Problem 480 (lines 15--25 of its page).
- The provenance paragraphs of
  [[../library/number_theory/chung_1984_irregularities_distribution/_index|the chapter's card]]
  and of
  [[../library/analysis/debruijn_erdos_1949_sequences_points_circle/_index|the note's card]];
  the Statement sections of the result pages
  [[../library/number_theory/chung_1984_irregularities_distribution/theorem_1|Theorem 1]],
  [[../library/number_theory/chung_1984_irregularities_distribution/theorem_2|Theorem 2]],
  [[../library/analysis/debruijn_erdos_1949_sequences_points_circle/inequality_4_3|(4.3)]]
  and
  [[../library/analysis/debruijn_erdos_1949_sequences_points_circle/section_2_r_equals_1|Section 2]].
- The held PDFs on rendered page images: the note's printed pp. 14--17 in
  full (Sections 1, 2, 4, 5 and 6, each clause read); the chapter's
  printed pp. 181--183 (introduction, display (1), the definition of $C$,
  Theorems 1, 2 and 3 with the definition of $u_m$), p. 211 (the proof of
  Theorem 1 from Theorem 3) and pp. 220--221 (closing remarks), each
  clause read; pp. 184--211 by text extracted from the page images and
  searched for the heading that opens the proof of Theorem 3, the
  sentence that closes it, and any citation of the 1949 note, not read
  clause by clause.
- `docs/verification.md` ("Grading and claim standing", the canonical
  failure modes, "Whole-claim report", "Audit checklist"),
  `docs/approach_vetting.md`, `docs/evidence.md` "Source fidelity" and
  `docs/math_authoring.md`.

**Exposures.** Four, disclosed here.

1. Locating the Statement of Problem 480 displayed its Formulation
   paragraph and a fragment of a status paragraph (lines 26--56 of the
   problem page, with the lines containing the words "status" and
   "assessment" filtered out): the fragment records the chapter's
   Theorem 1 constant, that Theorem 2 makes it best possible, the
   acceptance venues and the site's label. Nothing in it is used below
   beyond what the page images of pp. 182--183 establish independently.
2. A string search of the note's card for "480.1" returned one line (line
   135), which says the passage to the interval "is reconciled
   (author-recorded) as Proposition 480.1"; it confirms the section's
   pointer claim, and nothing else of that card outside its provenance
   paragraphs was read.
3. The two reconstruction pages carry a "Standing" paragraph, and the
   cards and result pages carry "Read status" and "Read depth"
   paragraphs, which were displayed with the allowed text; they say the
   pages are author-recorded and, for the preprint, that no acceptance
   evidence was found. They played no part in the verdicts.
4. No web search, no evidence folder, no `_index.md`, no Current
   assessment and no other section's review was read.

## Restatement

Conventions of the section: $x_1,x_2,\ldots\in[0,1]$; for $k\ge2$,
$g_k=\min_{1\le i<j\le k}|x_i-x_j|$ (zero when two of the first $k$
terms coincide); $\omega(\bar x)=\liminf_{n\to\infty}ng_n$;
$C(\bar x)=\inf_{n\ge1}\liminf_{m\to\infty}n|x_{m+n}-x_m|$; on the circle
of circumference $1$, $m_n^1(a)$ is the smallest of the $n$ gaps cut by
$a_1,\ldots,a_n$ (coincident points allowed, gap $0$) and
$\lambda_1(a)=\liminf_nnm_n^1(a)$.

- **S1 (target, imported).** Problem 480 asks whether every sequence in
  $[0,1]$ has $C(\bar x)\le5^{-1/2}$; the chapter's Theorem 1 gives
  $C(\bar x)\le\alpha=(1+\sum_{k\ge1}F_{2k}^{-1})^{-1}=0.39441967\ldots$
  for every sequence in $[0,1]$, and its Theorem 2 gives
  $C(\bar x^*)=\alpha$ for the Fibonacci-digit sequence, so $\alpha$ is
  best possible.
- **S2 (source characterization).** The chapter's introduction attributes
  to the 1949 note the bound $\omega(\bar x)\le1/\log4$ (its display
  (1)), and $\omega$ is the interval counterpart of $\lambda_1(a)$.
- **S3 (Proposition 480.1, finite form).** For every sequence in $[0,1]$
  and every integer $n\ge1$ there is an integer $k$ with $n<k\le2n$ and
  $kg_k\le\tau'_n$, where
  $\tau'_n=\bigl(2\sum_{k=n+1}^{2n}1/k-1/(n+1)\bigr)^{-1}$.
- **S4 (limit form).** $\tau'_n\to1/\log4$, hence every sequence in
  $[0,1]$ has $\omega(\bar x)\le1/\log4$.
- **S5 (sharpness).** The sequence $x_k=\{\log_2(2k-1)\}$ has
  $\omega(\bar x)=1/\log4$. The proof offered: its first $n$ terms are
  the numbers $\log_2(k/n)$, $n\le k\le2n-1$, in increasing order; hence
  its $n-1$ interior gaps are $\log_2((k+1)/k)$, $n\le k\le2n-2$; the
  smallest is $\log_2((2n-1)/(2n-2))$; and $ng_n\to1/\log4$.
- **S6 (obstruction).** Reading $[0,1]$ as the circle of circumference
  $1$ adds the wrap gap $y_1+1-y_N$, which can be the smallest gap, so
  $m_n^1(a)\le g_n$ and (4.3) bounds a quantity that is at most $g_n$;
  therefore the circle statement does not transfer by itself.
- **S7 (comparison of bounds).** The interval argument uses $N-1$
  adjacent pairs and $y_N-y_1\le1$ in place of $N$ cyclic windows and
  total length $1$; $\tau'_n$ exceeds the circle's
  $\tau_n^{(1)}=(2\sum_{k=n+1}^{2n}1/k)^{-1}$, the reciprocals differing
  by $1/(n+1)$, and both tend to $1/\log4$.
- **S8 (incomparability).** Nothing transfers to Problem 480: $C$ and
  $\omega$ are not comparable. Witnesses: prepending a copy of its first
  term to the chapter's extremal sequence gives $\omega=0$ and
  $C=\alpha$; the chapter's introduction remarks that consecutive terms
  nearly equal infinitely often leave $\omega$ large when they occur far
  out, so $C$ can be small with $\omega$ large; in particular
  $|x_{m+1}-x_m|=m^{-1/2}$ at infinitely many $m$ gives $C=0$ without
  constraining $\omega$.
- **S9 (descent).** The chapter's proof of Theorem 1 (p. 211) uses only
  the pairs of an increasing subsequence of the order permutation of $N$
  consecutive terms, the lower bound
  $(1+\epsilon)\alpha/|\pi(i_{k+1})-\pi(i_k)|$ from the negated lag
  hypothesis, and the value $u_m$ of Theorem 3, proved on pp. 188--210;
  the 1949 count uses all adjacent pairs, the bound $\varrho/k_i^*$ and
  the multiplicity bound $2$; no step of Section 4 of the note enters
  Theorem 3; Theorem 3 is reconstructed nowhere in the corpus; so the
  "descent" is a resemblance of shape, not a dependency.
- **S10 (no reverse transfer).** No held source addresses whether a
  permutation extremal problem could sharpen (4.3) for $r\ge2$; for $r=1$
  the bound is sharp; the growth of $r-\lambda_r$ claimed by the 2026
  preprint comes from its discrepancy argument, not from a sharper count.
- **S11 (next investigation).** Reading a later paper by the chapter's
  authors would settle what its circle measure is; not a mathematical
  claim.
- **S12 (outcome).** The section fails as a route to Problem 480 and
  proves the background transfer of the $1/\log4$ bound to the interval.

## Checklist

- **Quantifiers and scope.** S3 and S4 carry their quantifiers explicitly
  (every sequence, every $n\ge1$, some $k$ in $(n,2n]$; the lower limit
  along $k_n\to\infty$ bounds the lower limit of the full sequence). S8's
  "ignores any finite set of indices" is exactly the lower limit in $m$
  for each fixed lag, and prepending a term is an index shift for every
  lag. S5 asserts an exact description of the first $n$ terms for every
  $n$; it holds only when $n$ is a power of $2$ (F1). Verdict: one
  defect, F1; the rest pass.
- **Circularity.** None. S3 is proved from the sorted list directly; S5
  uses only the sequence; nothing assumes the target.
- **Model and convention changes.** S3 makes the circle-to-interval
  change correctly ($N-1$ windows, span $y_N-y_1\le1$). S5 transports the
  note's statement of the cyclic order of $a_1,\ldots,a_n$ modulo $1$ to
  the actual values in $[0,1]$ without a bridge (F1). S6 defeats only the
  identity embedding of $[0,1]$ into the circle; a scaled embedding
  transfers the limit statement (F2). Verdict: F1 required, F2 suggested.
- **Finite and statistical overreach.** None: the finite-$n$ bound is
  proved for every $n$ and the limit is taken analytically. The
  reviewer's numerical checks below are sanity checks and carry no
  weight in the verdicts.
- **Uniformity.** $\tau'_n$ depends on $n$ only; the constant $1/\log4$
  is the same for every sequence; no exchange of limits occurs. Pass.
- **Extremal conclusions.** Sharpness of $1/\log4$ was recomputed in the
  claim's own units ($ng_n$ for the log sequence, exact gap formulas):
  the limit holds, the section's exact formulas do not (F1). "$\alpha$ is
  best possible" is the chapter's Theorem 2, read on the page image. Pass
  for the conclusions, defect in the S5 argument.
- **Consequences and composition.** "Hence $\omega\le1/\log4$" follows
  from S3 (checked). "Not comparable" is established by the two
  witnesses, both re-derived. "So neither bound transfers" follows. S9's
  characterization of p. 211 was checked clause by clause; its "no step
  of Section 4 enters Theorem 3" was checked by a citation search of
  pp. 184--211 (limitation recorded). Pass.
- **Computation.** The section has no evidence code. The reviewer's
  checks used exact rationals for $\tau'_n$ and floating point for the
  gaps with exact identification of the gap formulas; the $n=3$ witness
  of F1 is exact. Pass.
- **Reproduction.** Inapplicable: the section states no rerun commands or
  coverage claims.
- **Source and verdict fidelity.** Display (1), the definition of $C$,
  Theorems 1--3 and the proof on p. 211 match the section's account. The
  page range "pp. 188--210" is right: the heading "An upper bound on
  $u_m$" opens at the foot of p. 188 and the proof of Theorem 3 closes on
  p. 210. S5 cites the Section 2 page for a statement that page and the
  note make only modulo $1$ (F1). S8's "remarks that $C$ can be small" is
  the section's inference from the chapter's sentence, which precedes the
  definition of $C$ (F4, note). Cross-reference claims about the folder
  index, the card of the chapter, the Current assessment and the Problem
  480 page's leads lie outside the read set and are unverified.

## Weakest steps

**W1 (S5, the sharpness computation; defective as written).** Write
$a_k=\{\log_2(2k-1)\}$. The note proves (p. 14) that modulo $1$ the
points $a_1,\ldots,a_n$ are the residues of $\log_2n,\ldots,\log_2(2n-1)$,
so on the circle the $n$ gaps in cyclic order are $\log_2((k+1)/k)$ for
$n\le k\le2n-1$, the last being the arc from $\{\log_2(2n-1)\}$ to
$\{\log_2(2n)\}=\{\log_2n\}$. The values in $[0,1)$ are the fractional
parts: with $2^j\le n<2^{j+1}$, the point for $k$ is $\log_2(k/2^j)$ when
$n\le k<2^{j+1}$ and $\log_2(k/2^{j+1})$ when $2^{j+1}\le k\le2n-1$. These
equal $\log_2(k/n)$ exactly when $n=2^j$. For $n=3$ the first three terms
are $0$, $\log_2(3/2)=0.5849\ldots$ and $\log_2(5/4)=0.3219\ldots$; the
section's list $\log_2(3/3)$, $\log_2(4/3)$, $\log_2(5/3)$ is $0$,
$0.4150\ldots$, $0.7369\ldots$. The interval's $n-1$ interior gaps are the
$n$ circle gaps minus the one arc that contains the point $0$: with $P$
the unique power of $2$ in $[n,2n-1]$, the missing arc is
$\log_2(P/(P-1))$ when $P>n$ and $\log_2(2n/(2n-1))$ when $P=n$. Since
$\log_2((k+1)/k)$ decreases in $k$, the smallest circle gap is
$\log_2(2n/(2n-1))$, and

$$
g_n=\begin{cases}\log_2\dfrac{2n}{2n-1}, & n\text{ not a power of }2,\\[1ex]
\log_2\dfrac{2n-1}{2n-2}, & n\text{ a power of }2.\end{cases}
$$

For $n=3$: $g_3=\log_2(6/5)$ and $3g_3=0.789\ldots$, against the section's
$\log_2(5/4)$ and $0.965\ldots$. The section's description is therefore
false for every $n$ that is not a power of $2$. The conclusion survives:
in both cases $\log_2(2n/(2n-1))\le g_n\le\log_2((2n-1)/(2n-2))$ for
$n\ge2$, because the interior gaps are a subset of the circle gaps
missing exactly one of them, and $n\log_2(1+1/(2n-1))$ and
$n\log_2(1+1/(2n-2))$ both tend to $1/(2\log2)=1/\log4$. A shorter repair
needs no computation: $g_n\ge m_n^1(a)$ always, so
$\omega(\bar x)\ge\lambda_1(a)=1/\log4$ by the Section 2 value, and S4
gives the reverse inequality.

**W2 (S3, the multiplicity identity; sound).** Each of the $N-1=2n-1$
windows $i$ has exactly one value $k_i^*\in\{n+1,\ldots,2n\}$, so
$\sum_{k=n+1}^{2n}\varepsilon_k=2n-1$. For $k\ge n+2$, $k_i^*=k$ forces
$k\in\{k_i,k_{i+1}\}$, and the position $j$ with $k_j=k$ lies in the
windows $j-1$ and $j$ only, so $\varepsilon_k\le2$. Expanding the right
side of the section's identity, the coefficient of $1/k$ for $k\ge n+2$
is $2-(2-\varepsilon_k)=\varepsilon_k$, and the coefficient of $1/(n+1)$
is $2-1+\sum_{k=n+2}^{2n}(2-\varepsilon_k)=(2n-1)-\sum_{k\ge n+2}\varepsilon_k$,
which is $\varepsilon_{n+1}$.
Each term $(2-\varepsilon_k)(1/(n+1)-1/k)$ is a product of two
nonnegative factors, so
$\sum_i1/k_i^*\ge2\sum_{k=n+1}^{2n}1/k-1/(n+1)=1/\tau'_n>0$ (the right
side is at least $2/(n+1)-1/(n+1)$). With the hypothesis $kg_k>\varrho$
on $(n,2n]$: the indices $k_i\ne k_{i+1}$ are both at most $k_i^*$, so
$y_{i+1}-y_i\ge g_{k_i^*}>\varrho/k_i^*$, and summing the $N-1\ge1$
strict inequalities gives $1\ge y_N-y_1>\varrho/\tau'_n$. So
$\varrho<\tau'_n$, and $\varrho=\tau'_n$ is impossible: some
$k\in(n,2n]$ has $kg_k\le\tau'_n$. At $n=1$ this reads $2g_2\le2$, true.
Composition with S4: $k_n\in(n,2n]$ forces $k_n\to\infty$, every
subsequential limit of $k_ng_{k_n}$ is one of $kg_k$, so
$\liminf_kkg_k\le\liminf_nk_ng_{k_n}\le\lim_n\tau'_n=1/\log4$.

**W3 (S6, the obstruction; true as stated, narrower than it reads).**
Under the identity embedding the circle gaps at stage $n$ are the $n-1$
interior gaps and the wrap gap $1-y_N+y_1$, so
$m_n^1(a)=\min(g_n,1-y_N+y_1)\le g_n$, and (4.3) gives an upper bound on
$\liminf_nnm_n^1(a)$, which says nothing about $\liminf_nng_n$ from
above. That is correct. But the circle statement does transfer the limit
bound by scaling: fix $\delta>0$ and put $a_i=x_i/(1+\delta)$ on the
circle of circumference $1$. The points lie in $[0,1/(1+\delta)]$, so the
wrap gap is at least $\delta/(1+\delta)$, while the interior gaps are the
interval's gaps divided by $1+\delta$ and $g_n\le1/(n-1)$ by pigeonhole.
Hence $m_n^1(a)=g_n/(1+\delta)$ for all $n\ge1+1/\delta$, and (4.3) at
$r=1$, which allows coincident points, gives
$\liminf_nng_n\le(1+\delta)/\log4$. Letting $\delta\to0$ proves S4 from
the circle statement alone. The re-run count is still what supplies the
finite-$n$ bound $\tau'_n$, which the scaling argument does not give.

## Strongest attack

- **S1, S2.** Attack: misquotation. The page images of pp. 181--183 show
  display (1) with the value $0.72135\ldots$ attributed to the note as
  reference [2], the definition of $C$ with the infimum over $n$ and the
  lower limit over $m$, Theorem 1 with the stated constant, and Theorem 2
  with both displays. Failed.
- **S3.** Attack: a configuration where the multiplicity bound or the
  window count fails. Positions $1$ and $N$ lie in one window each, so
  $\varepsilon_k\in\{0,1,2\}$, and the identity absorbs every pattern; the
  adversarial pattern ($\varepsilon_{n+1}=1$, $\varepsilon_k=2$ for
  $k\ge n+2$) makes the inequality an equality and gives exactly
  $\tau'_n$, so no pattern beats the bound. Attack: coincident terms; then
  $g_k=0$ for large $k$ and the statement is trivial. Attack: the boundary
  $n=1$; verified directly. A search over random sequences, the log
  sequence and the golden-ratio sequence for $n$ up to $200$ found no $n$
  without a qualifying $k$. Failed.
- **S4.** Attack: the lower limit along a subsequence. Handled in W2.
  Failed.
- **S5.** Attack: compute the first three terms. The section's
  description of the points and of the smallest gap is false at $n=3$
  (W1); the limit conclusion survives by the sandwich in W1. Succeeded
  against the proof, not against the statement.
- **S6.** Attack: exhibit a transfer the obstruction does not block. The
  scaled embedding of W3 transfers S4 from (4.3) directly. The sentence
  is literally about the identity embedding, where the wrap gap is a
  genuine obstruction, so the sentence stands; the framing that the
  passage needed the re-run count does not (F2).
- **S7.** Attack: arithmetic. With $S_n=\sum_{k=n+1}^{2n}1/k$,
  $\tau'_n=(2S_n-1/(n+1))^{-1}>(2S_n)^{-1}=\tau_n^{(1)}$ and
  $1/(n+1)\to0$; at $n=10$ the values are $0.802\ldots$ and
  $0.747\ldots$. Failed.
- **S8.** Attack on the first witness: prepending changes $C$. For each
  lag $n$ the shifted sequence has
  $|x'_{m+n}-x'_m|=|x^*_{m+n-2}-x^*_{m-2}|$ for $m\ge2$, so the lower
  limits agree and $C=\alpha$ by Theorem 2, while $g_k=0$ for $k\ge2$
  gives $\omega=0$. Attack on the second witness: a sequence with $C=0$
  and $\omega=1/\log4$ must exist for the claim to have content. The log
  sequence itself is one: for $m$ not a power of $2$ no integer lies in
  $(\log_2(2m-1),\log_2(2m+1)]$, so
  $|a_{m+1}-a_m|=\log_2((2m+1)/(2m-1))\to0$, the lag-$1$ lower limit is
  $0$ and $C=0$, while $\omega=1/\log4$ by S5 as repaired in W1. The
  $m^{-1/2}$ example: $C\le\liminf_m|x_{m+1}-x_m|=0$, and the condition is
  compatible with $\omega>0$ since $m^{-1/2}>c/(m+1)$ for large $m$.
  Failed.
- **S9.** Attack: find a use of the note inside the proof of Theorem 3.
  The extracted text of pp. 184--211 contains no citation of reference
  [2], no occurrence of the note's authors' names and no occurrence of
  "1949"; the note is cited on p. 181 only. The proof on p. 211 uses the
  telescoping sum $1\ge\sum_k(x_{M+\pi(i_{k+1})}-x_{M+\pi(i_k)})$ over an
  increasing subsequence, the bound
  $\alpha(1+\epsilon)/|\pi(i_{k+1})-\pi(i_k)|$ and $u(\pi)>(1-\delta)/\alpha$
  from Theorem 3, as the section says. Failed within the read set.
- **S10.** Attack: the "discrepancy route" attribution. The Theorem 1.1
  reconstruction derives $\limsup_n(r-nm_n^{(r)})\ge c\sqrt{\log r}$ from
  its Proposition 6.4 and Lemma 7.2, the latter resting on an imported
  planar $L^1$ discrepancy theorem; no sharpened count of the 1949 kind
  appears. Failed. The "no held source" clause is unverifiable here.
- **S12.** Attack: overclaim. The Outcome claims exactly S4 and the
  incomparability, both surviving. Failed.

## Premises

- **(4.3) reconstruction**,
  [[research/erdos_1221/dber49_inequality_4_3_reconstruction|the page]],
  read in full. Interface used: for every sequence on the circle of
  circumference $1$, coincident points allowed, and every $n\ge1$ there
  is $k\in(n,2n]$ with $km_k^1(a)\le\tau_n^{(1)}$, hence
  $\lambda_1(a)\le1/\log4$; also the shape of the identity that S3
  reuses. The section uses it within these hypotheses; W3 uses it with
  coincident points allowed, which the page states.
- **Theorem 1.1 reconstruction**,
  [[research/erdos_1221/ko26b_theorem_1_1_reconstruction|the page]],
  definitions, statement, Section 8 argument and imported-inputs list.
  Interface used: the one-sided bound on $r-nm_n^{(r)}$ over sequences of
  distinct points comes from Proposition 6.4 and Lemma 7.2 with an
  imported planar discrepancy theorem. Used only to check S10's
  attribution.
- **The 1949 note**, held, image-only, printed pp. 14--17 read on the
  page images. Interface: Section 1 definitions; Section 2, the cyclic
  order of $a_1,\ldots,a_n$ modulo $1$ as the residues of
  $\log_2n,\ldots,\log_2(2n-1)$ and the gap lengths $\log_2((k+1)/k)$;
  Section 4, the $r=1$ count with $k_i^*=\max(k_i,k_{i+1},n+1)$, the
  multiplicities $\varepsilon_k\in\{0,1,2\}$ and the display ending in
  $\tau_n$. The result pages
  [[../library/analysis/debruijn_erdos_1949_sequences_points_circle/inequality_4_3|(4.3)]]
  and
  [[../library/analysis/debruijn_erdos_1949_sequences_points_circle/section_2_r_equals_1|Section 2]]
  state these consistently with the images.
- **The 1984 chapter**, held, image-only. Read on page images: printed
  pp. 181--183 (introduction with display (1) and its attribution to
  reference [2], the sentence on nearly equal consecutive terms, the
  definition of $C$, Theorems 1, 2, 3 and $u_m$), p. 211 (Theorem 1 from
  Theorem 3) and pp. 220--221; pp. 184--211 by extracted text searched
  for the proof's boundaries and citations. The result pages
  [[../library/number_theory/chung_1984_irregularities_distribution/theorem_1|Theorem 1]]
  and
  [[../library/number_theory/chung_1984_irregularities_distribution/theorem_2|Theorem 2]]
  state the theorems consistently with the images.
- **Problem 480**, Statement only: the inequality with $5^{-1/2}$, the
  infimum over positive integers $n$, the lower limit over $m$.
- No batch acceptance order applies; no local claim card is consumed.

## Findings

- **F1 (required).** Location: lines 271--276, "the first $n$ terms of
  $x_k=\{\log_2(2k-1)\}$ are the numbers $\log_2(k/n)$, $n\le k\le2n-1$,
  in increasing order (the Section 2 page), so the $n-1$ interior gaps
  are $\log_2\frac{k+1}k$ for $n\le k\le2n-2$, the smallest is
  $\log_2\frac{2n-1}{2n-2}$". Defect: the note's Section 2 statement is a
  statement modulo $1$ (the cyclic order on the circle); the fractional
  parts equal $\log_2(k/n)$ only when $n$ is a power of $2$, and for
  other $n$ the interior gaps omit a different circle gap, so the
  smallest interior gap is $\log_2(2n/(2n-1))$. Witness: $n=3$; the first
  three terms are $0$, $\log_2(3/2)$, $\log_2(5/4)$, the interior gaps are
  $\log_2(5/4)$ and $\log_2(6/5)$, and $g_3=\log_2(6/5)$, not
  $\log_2(5/4)$. The conclusion $ng_n\to1/\log4$ is true (W1). Proposed
  replacement: "For the sharpness, the interior gaps of the first $n$
  terms of $x_k=\{\log_2(2k-1)\}$ are $n-1$ of the $n$ circle gaps of the
  Section 2 sequence, which are $\log_2\frac{k+1}k$ for $n\le k\le2n-1$
  (Section 2 of the note, p. 14), so
  $\log_2\frac{2n}{2n-1}\le g_n\le\log_2\frac{2n-1}{2n-2}$ and
  $ng_n\to1/(2\log2)=1/\log4$." Or, shorter: "$g_n\ge m_n^1(a)$ since the
  interior gaps are among the circle gaps, so
  $\omega(\bar x)\ge\lambda_1(a)=1/\log4$ by the Section 2 page, and the
  proposition gives the reverse inequality."
- **F2 (suggested).** Location: lines 278--280, "The circle statement
  does not transfer by itself: reading $[0,1]$ as the circle adds the
  wrap gap $y_1+1-y_N$, which can be the smallest gap, so
  $m_n^1(a)\le g_n$ and (4.3) bounds the wrong side." Defect: the
  obstruction defeats only the identity embedding; the scaled embedding
  $a_i=x_i/(1+\delta)$ of W3 transfers the limit bound $\omega\le1/\log4$
  from (4.3) in three lines, so the passage the card left unreconciled
  has a bridge that needs no re-run of the count. What the re-run adds is
  the finite-$n$ bound $\tau'_n$. Proposed replacement: "The circle
  statement does not transfer under the identity embedding: ... bounds
  the wrong side. Scaling the sequence into a circle of circumference
  $1+\delta$ makes the wrap gap at least $\delta/(1+\delta)$, so for
  large $n$ the smallest circle gap is the smallest interior gap and
  (4.3) gives $\omega\le(1+\delta)/\log4$ for every $\delta>0$; that
  transfers the limit but not a finite-$n$ bound, which the interval
  count above supplies."
- **F3 (note).** Location: lines 251--252, "$x_k$ is $y_j$ for exactly
  one $j$". Under coincident values $x_k$ equals $y_j$ as a value for
  several $j$; the argument needs the position, $k=k_j$ for exactly one
  $j$, which is what the preceding clause ($k_i^*=k$ forces
  $k\in\{k_i,k_{i+1}\}$) uses. Replace with "$k=k_j$ for exactly one
  $j$". No effect on the proof.
- **F4 (note).** Location: lines 296--298, "the chapter's introduction,
  as the card of the chapter records, remarks that $C$ can be small
  while $\omega$ stays large". The chapter's sentence (p. 182) says that
  a sequence can have two consecutive terms very nearly equal infinitely
  often and still have $\omega$ large when the pairs occur far out, and
  that this happens for the log sequence; it introduces $C$ afterward as
  the remedy. The conclusion about $C$ is the section's inference (valid,
  since $C\le\liminf_m|x_{m+1}-x_m|$), not the chapter's wording. Suggest
  "remarks that consecutive terms can be nearly equal infinitely often
  while $\omega$ stays large, which makes $C$ small". The card's
  recording of the remark was not read.

## Verdict

- S1: not a claim (imported statement of the problem and of Theorems 1
  and 2); the characterization is faithful to the page images.
- S2: refutation-failed.
- S3: refutation-failed.
- S4: refutation-failed.
- S5: proof defective; statement unresolved. The stated description of
  the first $n$ terms and of the smallest gap is false for every $n$
  that is not a power of $2$ (F1); the statement $\omega(\bar x)=1/\log4$
  for the log sequence is established by the reviewer's sandwich in W1
  and is also asserted by the chapter, so the required correction
  replaces the argument, not the claim.
- S6: refutation-failed as stated (identity embedding), with F2.
- S7: refutation-failed.
- S8: refutation-failed.
- S9: refutation-failed within the read set.
- S10: refutation-failed for the checkable clauses; "addressed by no held
  source" was not checked.
- S11: not a claim.
- S12: refutation-failed.

Limitations: the proof of Theorem 3 (pp. 188--210) was searched for
citations in extracted text and not read clause by clause, so "no step of
Section 4 enters Theorem 3" is confirmed only to the depth of a citation
search; the clauses about the folder index, the card of the chapter, the
Current assessment, the Problem 480 page's leads and the holdings of the
library are outside the read set and carry no verdict; the numerical
checks are sanity checks over finitely many sequences and support nothing
beyond the derivations above. This focused review assigns no tier and
changes no status.

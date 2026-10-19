---
name: research/erdos_18/evidence/verify/connections_problem_1099_sums_of_powers_of_consecutive_divis_review
title: "Independent review of the connections section: Problem 1099: sums of powers of consecutive divisor ratios"
desc: |
  Refutation-failed for the two-sided factorial bound, its limit form and the
  corollary on Erdős's question (1.2); refuted-as-stated for the two prose
  sentences that call the correction term uniformly tiny; one required
  correction and four notes.
created: 2026-09-28T18:11:21Z
updated: 2026-09-28T18:11:21Z
---

***

## Subject and independence

The reviewer acted as an independent reviewer in a fresh context, given only
the commissioning assignment, and took no part in writing the connections
page, its shared lemmas, or the reconstruction pages of the folder. The
charge was refutation.

The subject is page `wiki/research/erdos_18/connections.md` as it stood at
2026-09-28T13:50:48Z, section "## Problem 1099: sums of powers of consecutive
divisor ratios", lines 586–692 (the next H2 heading is at line 693). No separate
lead page was named; the section is the whole subject. The section's target is
[[problems/divisors/E1099/_index|Problem 1099]].

Reading, with depth:

- The section, clause by clause. The page's preamble and Conventions (lines
  1–46) and the Shared lemmas section (lines 47–243) as inputs: Lemma A in
  full, since the section uses its ratio-two conclusion for $n!$; Lemmas B,
  C, C′ and D for their interfaces only, as the section does not use them.
  The Sources section (lines 794–805).
- [[research/erdos_18/hughes_corollary_3_reconstruction|The Corollary 3 reconstruction]]
  in full, as the premise whose statement the section consumes, and
  [[research/erdos_18/hughes_lemma_4_reconstruction|the Lemma 4 reconstruction]]
  in full, for the ratio-two property of $n!$. Both are consumed at the
  standing the assignment states: independently reviewed as of
  2026-09-28T05:03:27Z with corrections applied since.
- The Statement block of the Problem 1099 page (lines 1–45, with the
  frontmatter status line filtered out of the read).
- [[../library/divisors/hughes_2026_sums_distinct_divisors_factorials/theorem_2|The Theorem 2 page]]
  of the Hughes card in full, and physical p. 2 of the held Hughes PDF
  (Theorem 2 as quoted, display (1), Corollary 3 with its proof, Lemma 4)
  in its extracted text.
- The provenance paragraph and result list of
  [[../library/additive_bases/erdos_1981_problems_results_additive_multiplicative_number_theory/_index|Erdős (1981)]]
  and physical p. 171 of the held PDF, read on the page image, for the
  definitions (1.1) and (1.2) and the candidates sentence.
- `docs/verification.md` ("Report contract", "Grading and claim standing",
  "Audit checklist", and the Erdos-specific "Whole-claim report" and "Audit
  checklist"), `docs/approach_vetting.md`, the "Source fidelity" section of
  `docs/evidence.md`, and `docs/math_authoring.md`.

Not held and not read: Vose (1984), Tenenbaum (1987), Berend and Harmse
(1993), the erdosproblems.com page and its discussion thread. Their
characterizations in the section could not be checked here.

Exposures, disclosed in full: (1) the card `_index.md` of
[[../library/divisors/hughes_2026_sums_distinct_divisors_factorials/_index|Hughes (2026)]]
was read whole, including its Overview and Bears-on paragraphs, beyond the
provenance paragraph the assignment allows; those paragraphs concern
Problem 18, not Problem 1099, and carry no verdict on this section. (2) In
locating the Statement block, the reviewer saw the heading list of the
Problem 1099 page (`## Current assessment`, `## Progress`,
`## Known Results`) without reading any of their content. (3) A search of
the whole connections page for the strings "Tenenbaum", "aif.1083" and
"Berend" returned matching lines from other sections (lines 283, 438, 494,
504–507, 520, 540, 572, 701 and 751–753), truncated to 120 characters and
used only to confirm that the section's "cited above" resolves to a
citation at line 494. Nothing under any `evidence/` folder, no Current
assessment, Known results, standing or acceptance text, nothing among the private
working files, and no web search reached the reviewer.

## Restatement

Notation, from the page's Conventions and the Corollary 3 page: $N=n!$;
$1=d_1<\cdots<d_{\tau(N)}=N$ are its divisors; a *pair* is $(d_i,d_{i+1})$
with ratio $r_i=d_{i+1}/d_i$; $h_\alpha(N)=\sum_i(r_i-1)^\alpha$; $\lg$ is
$\log_2$; for real $x\ge2^{16}$, $\varepsilon_x=x^{-(\lg x/2-\lg\lg x)}$, so
$\varepsilon_{2^{16}}=2^{-64}$ and $(\varepsilon_j)_{j\ge2^{16}}$ is
decreasing; the window of index $j\ge2$ is $[\sqrt{(j-1)!},\sqrt{j!}]$;
$j_0=2^{16}$ and $T=\sqrt{(j_0-1)!}$, a constant of about $10^{143600}$. The
*mirror* of the pair $(d,b)$ is $(N/b,N/d)$.

- **S1.** For every real $\alpha>1$ the series
  $C(\alpha)=4\sum_{j\ge j_0}(4\varepsilon_j)^{\alpha-1}(\tfrac12\log j+\log2)$
  converges.
- **S2.** For every real $\alpha>1$ and every integer $n\ge T$,
  $2\sum_{d=1}^{n-1}d^{-\alpha}\le h_\alpha(n!)\le2\zeta(\alpha)+C(\alpha)$.
  The proof asserts the lower bound for every integer $n\ge4$.
- **S3.** For every $\alpha>1$,
  $2\zeta(\alpha)\le\liminf_nh_\alpha(n!)\le\limsup_nh_\alpha(n!)\le2\zeta(\alpha)+C(\alpha)$.
- **S4.** (a) For every integer $j\ge2^{16}$ and every $\alpha>1$,
  $(4\varepsilon_j)^{\alpha-1}\le2^{-62(\alpha-1)}$. (b) $C(2)<10^{-10}$.
  (c) The prose around them: "For $\alpha\ge1+\eta$ the correction is tiny"
  (lines 625–626) and "the explicit value $2\zeta(\alpha)+O(2^{-62(\alpha-1)})$"
  (line 673), read as a reader must read them: $C(\alpha)$ is small against
  $2\zeta(\alpha)$ whenever $\alpha$ is bounded away from $1$, with an
  implied constant that does not depend on $\alpha$.
- **S5.** For every integer $n\ge T$,
  $-1\le\sum_id_{i+1}/d_i-\tau(n!)-\log n!\le\zeta(2)+\tfrac12C(2)-1$, the
  sum running over the $\tau(n!)-1$ pairs; hence the quantity of Erdős's
  question (1.2) is bounded along the factorials.
- **S6.** Scope: the transported argument gives nothing for
  $L_x=\mathrm{lcm}(1,\dots,x)$, because Corollary 3 is a statement about
  $n!$, and nothing about $\liminf$ over all $n$ beyond the literature.
- **S7.** Attributions: the Problem 1099 page records status proved with
  references to Erdős (1981) and Vose (1984) and has no compiled
  assessment; the site page attributes the solution to Vose, quotes Erdős's
  remark as "would be good candidates", calls the factorial and lcm cases
  unknown, and carries a comment of 2 July 2026; Tenenbaum's 1987
  Théorème 1 covers factorials, least common multiples and primorials;
  Berend and Harmse (p. 570) record the same; the section's argument is
  Tenenbaum's Théorème 2 with the displayed inequality; Berend and Harmse
  (p. 572) note the extension; only the explicit value appears new, with
  no search made.

## Checklist

- **Quantifiers and scope.** S2 is stated for integers $n\ge T$ and its
  proof uses $n\ge T$ exactly once, in the bottom zone ("every integer up to
  $\lceil T\rceil\le n$ divides $N$"), which follows from $n\ge T$ for
  integer $n$; the lower bound is proved for $n\ge4$; S3 is the limit form
  of S2; S5 carries the $n\ge T$ qualifier. The limits are along the
  factorials only, as stated. Defect in S4(c): a bound presented as uniform
  in $\alpha$ is not uniform (F1). Pass except F1.
- **Circularity.** None. The proof uses Lemma A (a self-contained valuation
  argument), the imported Corollary 3, and elementary inequalities; no
  statement equivalent to the target is assumed. Pass.
- **Model and convention changes.** $h_\alpha$ is the problem page's
  function. The mirror map is a bijection of consecutive pairs preserving
  the ratio (a divisor strictly between $N/b$ and $N/d$ would give one
  strictly between $d$ and $b$). The windows are those of the Corollary 3
  page. No relaxed or averaged system replaces the actual objects. Pass.
- **Finite and statistical overreach.** No finite computation is cited as
  proof. $C(2)<10^{-10}$ is a statement about a convergent series and is
  rederived below by hand ($C(2)<3.3\cdot10^{-13}$) and numerically
  ($C(2)\approx3.7\cdot10^{-14}$). Pass.
- **Uniformity.** The constants in S2 are explicit and depend only on
  $\alpha$. The descriptive sentences S4(c) hide the $\alpha$-dependence of
  $C(\alpha)$, which is unbounded as $\alpha\to1^+$. Fail for S4(c), pass
  otherwise.
- **Extremal conclusions.** The limits inferior and superior are taken in
  the claim's own units; the lower limit $2\zeta(\alpha)$ is the limit of
  the exact lower bounds $2\sum_{d<n}d^{-\alpha}$; no sharpness is claimed.
  Pass. (A sharper form of S5 exists; see F2, not a defect.)
- **Consequences and composition.** Each "so" and "hence" was rederived: S3
  from S2; S5 from S2 at $\alpha=2$ and the identity
  $\sum_i\log r_i=\log N$; the upper bound from the three zones. Corollary 3
  is applied with all its hypotheses supplied ($j\ge2^{16}$, $n\ge j$,
  consecutive divisors of $n!$, geometric mean in window $j$); Lemma A is
  applied to $n!$, which its statement covers. Pass.
- **Computation.** The section carries no code. Its numerical assertions
  ($\varepsilon_{2^{16}}=2^{-64}$, the summand bound, $C(2)<10^{-10}$) were
  rederived. Pass.
- **Reproduction.** No rerun commands or coverage claims are made.
  Inapplicable; the reviewer's own checks are described under Weakest steps
  and Strongest attack.
- **Source and verdict fidelity.** The Corollary 3 interface matches
  physical p. 2 of the held Hughes PDF. Erdős's (1.1) and (1.2) match the
  held 1981 paper (p. 171). The quoted phrase "would be good candidates"
  does not match that paper's wording (F3). The sentence "has no compiled
  assessment" is stale as of 2026-09-28T13:50:48Z (F4). The characterizations of
  Tenenbaum (1987) and of Berend and Harmse (1993) come from text layers of
  papers not held and are marked as such in the section; they could not be
  checked (F5). Pass with notes.

## Weakest steps

**W1: the three zones cover every pair exactly once, and the two outer zones
are runs of consecutive integers.** Bottom: $d<T$. Top: $b>N/T$. Middle:
$d\ge T$ and $b\le N/T$. A pair outside the bottom zone has $d\ge T$, and
one outside the top zone has $b\le N/T$, so the three zones cover all pairs,
and the middle zone is disjoint from both by definition. A pair in both
outer zones would have $r=b/d>(N/T)/T=n!/(j_0-1)!\ge(j_0+1)j_0>2$, since
$n\ge T>j_0+1$; Lemma A gives $r\le2$ for every pair of $n!$. In the bottom
zone, $d<T$ and $n\ge T$ with $n$ an integer give $d+1\le\lceil T\rceil\le n$,
so $d+1$ divides $n!$ and is the next divisor: the zone is
$\{(d,d+1):1\le d\le\lfloor T\rfloor\}$ and contributes
$\sum_{d\le\lfloor T\rfloor}d^{-\alpha}<\zeta(\alpha)$. In the top zone,
$e=N/b$ is an integer below $T$, so $e+1$ divides $N$ and the mirror pair is
$(e,e+1)$, whence $r-1=1/e$; the zone is the mirror image of the bottom zone
and contributes the same sum. ($T$ is irrational, since $(j_0-1)!$ is not a
square by Bertrand's postulate, so $d<T$ and $d\le\lfloor T\rfloor$ agree;
nothing depends on this.)

**W2: the middle zone through Corollary 3.** For a middle pair with
$db\le N$, $g=\sqrt{db}$ satisfies $g>d\ge T$ and $g\le\sqrt N$. For one
with $db>N$, the mirror pair has geometric mean $N/g<\sqrt N$, and $N/g\ge T$
because $g<b\le N/T$. The windows $j_0\le j\le n$ have union
$[\sqrt{(j_0-1)!},\sqrt{n!}]=[T,\sqrt N]$, consecutive windows sharing an
endpoint, so $\min(g,N/g)$ lies in some window $j$ with $j_0\le j\le n$; at
a shared endpoint either index may be chosen, and one choice per pair is
fixed. Corollary 3, applied to the pair itself or to its mirror (a
consecutive pair of divisors of $n!$ with the same ratio), gives
$\log r\le3\varepsilon_j$. With $u=\varepsilon_j\le2^{-64}$,
$r-1\le e^{3u}-1\le3ue^{3u}<4u$, and $r-1\le2\log r$ on $[1,2]$ (the
function $2\log r-(r-1)$ vanishes at $1$ and has derivative $2/r-1\ge0$
there), so $(r-1)^\alpha=(r-1)^{\alpha-1}(r-1)$ is at most
$(4\varepsilon_j)^{\alpha-1}\cdot2\log r$. Now fix $j$. The pairs assigned to
$j$ through their own mean have $\log d\ge\log g-\tfrac12\log2$, hence
$\log d\ge\tfrac12\log(j-1)!-\tfrac12\log2$, and
$\log b\le\tfrac12\log j!+\tfrac12\log2$, so their spans $[\log d,\log b]$
lie in an interval of length $\tfrac12\log j+\log2$; spans of distinct
consecutive pairs have disjoint interiors, so $\sum\log r$ over this family
is at most that length. The pairs assigned to $j$ through their mirror have
spans inside the interval from $\log N-\tfrac12\log j!-\tfrac12\log2$ to
$\log N-\tfrac12\log(j-1)!+\tfrac12\log2$, again of length
$\tfrac12\log j+\log2$, again with disjoint interiors. Each pair is assigned
once, so window $j$ contributes at most
$(4\varepsilon_j)^{\alpha-1}\cdot2\cdot2(\tfrac12\log j+\log2)$, the summand
of $C(\alpha)$, and the middle zone contributes at most $C(\alpha)$.
Convergence of $C(\alpha)$: by display (1) of the Corollary 3 page,
$\log(1/\varepsilon_j)=(1-o(1))(\log j)^2/(2\log2)$, so for fixed $\alpha>1$
the factor $(4\varepsilon_j)^{\alpha-1}$ is eventually below $j^{-3}$ and the
summand below $j^{-2}$; the series converges. Altogether
$h_\alpha(n!)<2\zeta(\alpha)+C(\alpha)$ for every integer $n\ge T$, which is
the upper bound of S2.

**W3: the lower bound and the corollary.** For $1\le d\le n-1$ both $d$ and
$d+1$ divide $n!$, so $(d,d+1)$ is a pair contributing $d^{-\alpha}$, and
its mirror contributes the same. A pair $(d,d+1)$ equals the mirror of
$(d',d'+1)$ only if $d(d'+1)=N=d'(d+1)$, that is $d=d'$ and $d(d+1)=n!$,
impossible for $d\le n-1$ when $n\ge4$ because $n(n-1)<n!$; at $n=3$ the
pair $(2,3)$ of $6$ is its own mirror, which is why the proof says $n\ge4$.
So $h_\alpha(n!)\ge2\sum_{d=1}^{n-1}d^{-\alpha}$ for $n\ge4$, and S3 follows
from S2 by letting $n\to\infty$. For S5,
$\sum_i\log r_i=\log(d_{\tau(N)}/d_1)=\log N$ and $\sum_i1=\tau(N)-1$, so
$\sum_ir_i-\tau(N)-\log N=\sum_i(r_i-1-\log r_i)-1$; for $r\ge1$,
$0\le r-1-\log r\le\tfrac12(r-1)^2$ (the derivative of
$\tfrac12(r-1)^2-(r-1)+\log r$ is $(r-1)^2/r\ge0$), so the sum lies in
$[0,\tfrac12h_2(N)]\subseteq[0,\zeta(2)+\tfrac12C(2)]$ for $n\ge T$. The
display of S5 follows. Erdős's (1.2), read on p. 171 of the held paper, is
$\liminf_{n\to\infty}(\sum d_{i+1}/d_i-\tau(n)-\log n)<\infty$; boundedness
along the factorials implies it.

## Strongest attack

- **S1.** Tried to make the series diverge for $\alpha$ close to $1$ using
  only the weaker bound $\varepsilon_j\le j^{-4}$, which the section itself
  disclaims; with the exact formula (1) the terms are eventually below
  $j^{-2}$ for every fixed $\alpha>1$. Failed.
- **S2, upper bound.** Attacked every boundary of the zone decomposition: a
  pair with $d<T\le b$ (bottom, $b=d+1$); a pair with $db=N$ (own mean
  $\sqrt N$, the top of window $n$); a middle pair with $db>N$ whose mirror
  mean must reach $T$ (it does, since $\sqrt{db}<b\le N/T$); a pair
  straddling $N/T$ (top zone by definition); a geometric mean on a shared
  window endpoint (either index is admissible; one is fixed). Tried to make
  one window carry more than two families or a pair count twice: each pair
  is assigned exactly once, and the mirror of a pair assigned through its
  own mean is either assigned through its mirror, to the same window in the
  other family, or lies in an outer zone. Tried a computational
  counterexample: for $4\le n\le26$, $h_2(n!)$ exceeds $2\zeta(2)+C(2)$
  (for example $h_2(10!)=3.779$ and $h_2(26!)=3.398$ against $3.290$), so
  the bound is false below the threshold; but the statement is claimed only
  for $n\ge T$, the bottom-zone step is exactly where $n\ge T$ is used, and
  the excess $h_2(n!)-2\sum_{d<n}d^{-2}$ falls from $0.75$ at $n=9$ to
  $0.19$ at $n=26$, as the middle-zone bound predicts. Failed.
- **S2, lower bound.** The self-mirror pair at $n=3$ is excluded by the
  hypothesis $n\ge4$; checked exactly for $4\le n\le26$. Failed.
- **S3.** Follows from S2. Failed.
- **S4(c).** Succeeded; see F1. The summand bound is uniform in $j$, but the
  sum of $\tfrac12\log j+\log2$ over $j$ diverges, so no constant $K$
  independent of $\alpha$ satisfies $C(\alpha)\le K\cdot2^{-62(\alpha-1)}$.
- **S5.** Attacked the sign and the count of pairs ($\tau(N)-1$, not
  $\tau(N)$), and the inequality $r-1-\log r\le\tfrac12(r-1)^2$ for $r$ up
  to $2$; all hold. Checked exactly for $4\le n\le10$ that the difference
  equals $\sum_i(r_i-1-\log r_i)-1$ and can be negative ($-0.011$ at
  $n=4$), consistent with the lower bound $-1$; Erdős's printed strict
  inequality $\sum d_{i+1}/d_i>\tau(n)+\log n$ fails at small $n$, but the
  section does not assert it. Failed.
- **S6.** Corollary 3 needs consecutive divisors of $n!$; consecutive
  divisors of $L_x$ need not be consecutive divisors of any $n!$, so the
  gap bound does not transfer to $L_x$ and the scope sentence stands.
  Failed.
- **S7.** The checkable parts (status, references, (1.1), (1.2)) agree with
  the held sources; two wording defects (F3, F4); the rest is not checkable
  here (F5).

## Premises

- **Lemma A** (connections page, lines 52–78; shared lemma, author-recorded,
  another reviewer's subject). Interface used: consecutive divisors of $n!$
  have ratio at most $2$, for every $n\ge1$. Confirmed at use: the section
  applies it to $N=n!$ only. Read in full.
- **The Corollary 3 reconstruction** (premise, established at the standing
  the assignment states). Interface: for integers $j\ge2^{16}$ and $n\ge j$,
  and consecutive divisors $a<b$ of $n!$ with
  $\sqrt{(j-1)!}\le\sqrt{ab}\le\sqrt{j!}$, $\log(b/a)\le3\varepsilon_j$;
  with the definition of $\varepsilon_x$, display (1), the monotonicity of
  $(\varepsilon_j)_{j\ge2^{16}}$ and $\varepsilon_j\le2^{-64}$. It imports
  the Berend–Harmse estimate second-hand from Hughes; the 1993 paper is not
  held. Every use in the section supplies $j_0\le j\le n$ and a consecutive
  pair of $n!$ whose geometric mean lies in window $j$. Read in full.
- **The Lemma 4 reconstruction.** Read in full; only its
  compilation-supplied ratio-two proof for $n!$ overlaps with what the
  section uses, through Lemma A.
- **Hughes (2026), held.** Physical p. 2 read in extracted text: Theorem 2
  as quoted, display (1), Corollary 3 and its proof, Lemma 4. They agree
  with the reconstruction and with the card's Theorem 2 page.
- **Erdős (1981), held.** Physical p. 171 read on the page image: (1.1)
  defines $h_\alpha(n)=\sum_{i=1}^{\tau(n)-1}(d_{i+1}/d_i-1)^\alpha$ and
  asks, for every $\alpha>1$, for a constant $C_\alpha$ and infinitely many
  $n$ with $h_\alpha(n)<C_\alpha$; the candidates sentence reads "$n!$ or
  the least common multiple of the integers not exceeding $n$ seem to be
  good candidates for integers with (1.1) bounded above"; (1.2) is
  $\liminf_{n\to\infty}(\sum d_{i+1}/d_i-\tau(n)-\log n)<\infty$.
- **Problem 1099 page, Statement block.** The definition of $h_\alpha$
  agrees with the section; the block records status proved and the
  references [Er81h] and [Vo84].
- **Not held.** Vose (1984); Tenenbaum (1987); Berend and Harmse (1993); the
  site page. The section's statements about them stay at the author's
  text-layer reading.

## Findings

**F1 (required).** Location: lines 625–626, "For $\alpha\ge1+\eta$ the
correction is tiny: $(4\varepsilon_j)^{\alpha-1}\le2^{-62(\alpha-1)}$, and
$C(2)<10^{-10}$", and lines 672–673, "Only the explicit value
$2\zeta(\alpha)+O(2^{-62(\alpha-1)})$ appears to be new". Defect: the
summand bound holds for each $j$, but the factor $\tfrac12\log j+\log2$ is
not summable, so the bound on the summand says nothing about the size of
$C(\alpha)$ when $\alpha$ is near $1$; the $O$-term cannot carry an absolute
constant, and with an $\alpha$-dependent constant it says only
$O_\alpha(1)$. Exactly: as $\alpha\to1^+$ every term of $C(\alpha)$
increases to $4(\tfrac12\log j+\log2)$, so $C(\alpha)\to\infty$ by monotone
convergence. Witness: $C(5/4)\approx20.3$, above the main term
$2\zeta(5/4)\approx9.19$ and about $9\cdot10^5$ times
$2^{-62/4}\approx2.2\cdot10^{-5}$; $C(1.1)\approx7.9\cdot10^4$;
$C(3/2)\approx1.8\cdot10^{-4}$; $C(2)\approx3.7\cdot10^{-14}$ (partial sums
over $2^{16}\le j<3\cdot10^6$ in floating point plus an integral tail, which
is accurate to the digits shown because the summand varies by a factor
$1+O(\log j/j)$ per step). Proposed replacement: "The correction is small
only when $\alpha$ is bounded away from $1$: for every $j$,
$(4\varepsilon_j)^{\alpha-1}\le2^{-62(\alpha-1)}$, so
$C(\alpha)\le2^{62\eta}C(1+\eta)\,2^{-62(\alpha-1)}$ for $\alpha\ge1+\eta$,
with $C(2)<10^{-10}$ and $C(3/2)<10^{-3}$; but $C(5/4)\approx20$ exceeds
$2\zeta(5/4)$, and $C(\alpha)\to\infty$ as $\alpha\to1^+$." And in the
novelty sentence, "the explicit bound $2\zeta(\alpha)+C(\alpha)$, with
$C(\alpha)=O_\eta(2^{-62(\alpha-1)})$ for $\alpha\ge1+\eta$".

**F2 (note).** Location: lines 652–661, the corollary. Not a defect: the
interval $[-1,\zeta(2)+\tfrac12C(2)-1]$ is correct but discards what the
proof of S2 already shows. The outer zones contribute exactly
$2\sum_{d\le\lfloor T\rfloor}(1/d-\log(1+1/d))=2\gamma+O(1/T)$ to
$\sum_i(r_i-1-\log r_i)$ and the middle zone between $0$ and
$\tfrac12C(2)$, so for $n\ge T$ the difference equals
$2\gamma-1+\theta+O(1/T)$ with $0\le\theta\le\tfrac12C(2)<2\cdot10^{-14}$;
in particular it is positive and essentially constant along the
factorials. Optional sharpening.

**F3 (note).** Location: line 593, the quotation "would be good
candidates". The held 1981 paper (p. 171) reads "seem to be good candidates
for integers with (1.1) bounded above". Whether the site page misquotes or
the section does could not be decided here, as the site was not read.
Proposed replacement: quote the held wording, or drop the quotation marks
and attribute the paraphrase to the site.

**F4 (note).** Location: lines 590–591, "has no compiled assessment"
(repeated in the section's last paragraph, lines 687–691, as a request to
add one). As of 2026-09-28T13:50:48Z the Problem 1099 page carries a
`## Current assessment` heading (line 46; its content was not read, so it
may be a placeholder), and the page's `updated` stamp (08:32:32Z) postdates
the connections page's (08:22:56Z). Proposed replacement: reconcile the
sentence and the Next-investigation item with the page's current state.

**F5 (note; a limitation, not a defect).** Location: lines 596–602 and
663–672, the characterizations of Tenenbaum's Théorème 1 and Théorème 2 and
of Berend and Harmse's pp. 570 and 572. These rest on text layers of papers
the library does not hold and are marked as such in the section and in the
Sources section; they were not checkable within the read set and remain
author-recorded. The section's own instruction to read the page images
before any problem page relies on them is the right next step.

## Verdict

- S1 (convergence of $C(\alpha)$): refutation-failed.
- S2 (two-sided bound for $n\ge T$, lower bound for $n\ge4$):
  refutation-failed.
- S3 (limit inferior and superior along $n!$): refutation-failed.
- S4(a) and S4(b) (summand bound; $C(2)<10^{-10}$): refutation-failed.
- S4(c) (the correction uniformly tiny; $O(2^{-62(\alpha-1)})$ with an
  absolute constant): refuted-as-stated, witness $\alpha=5/4$ (F1).
- S5 (the corollary on Erdős's (1.2) along $n!$): refutation-failed.
- S6 (scope sentence): refutation-failed.
- S7 (attributions): the parts checkable against held sources agree, with
  two wording defects (F3, F4); the unheld-source characterizations are not
  mathematical claims of this section and were not checkable (F5).

Required corrections: one (F1). Limitations: the threshold
$T=\sqrt{(2^{16}-1)!}$ is about $10^{143600}$, so S2 says nothing about any
factorial that can be computed, and the bound is in fact false for
$4\le n\le26$; the limit statements S3 and S5 are unaffected. The
Berend–Harmse estimate enters second-hand through the Corollary 3 page and
was consumed at that page's standing, not re-derived. The numerical values
in F1 are floating-point computations by the reviewer; the hand bound
$C(2)\le16\sum_{j\ge2^{16}}j^{-15/4}<3.3\cdot10^{-13}$ (from
$\varepsilon_j\le j^{-4}$ and $\tfrac12\log j+\log2\le j^{1/4}$ for
$j\ge2^{16}$) and the divergence $C(\alpha)\to\infty$ as $\alpha\to1^+$ are
exact. This focused review assigns no tier and changes no status.

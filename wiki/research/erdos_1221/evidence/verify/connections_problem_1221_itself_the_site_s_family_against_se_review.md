---
name: research/erdos_1221/evidence/verify/connections_problem_1221_itself_the_site_s_family_against_se_review
title: "Independent review of the connections section: Problem 1221 itself: the site's family against sequences of distinct points"
desc: |
  Fresh-context refutation review of the extension of the 2026 consecutive-gap
  lower bounds from sequences of distinct points to the site's family. Every
  statement survives (refutation-failed): zero required corrections, two
  suggested wording corrections (the "same r_0" clause of deduction 1221.3 and
  the description of the imported Theorem 4.1 in premise (P)) and four notes.
created: 2026-09-28T19:22:07Z
updated: 2026-10-13T05:28:09Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context, given only the
commissioning assignment. The reviewer took no part in writing the
connections page, the lead page or the reconstruction pages, and read no
review, grade, current assessment or standing text about them. Charge:
refutation.

**Subject.** The repository as it stood on 2026-09-28T13:50:48Z.

- `wiki/research/erdos_1221/connections.md`, section "## Problem 1221
  itself: the site's family against sequences of distinct points", lines
  333--518 (the H2 at line 333 up to the line before the next H2 at line
  519): Target (line 335), The two families (344), Where distinctness enters
  (361), Proposition 1221.1 with proof (401--449), Proposition 1221.2 with
  proof (451--472), Conditional deduction 1221.3 (474--493), What it does not
  give (495), Next investigation (505), Outcome (515).
- `wiki/research/leads/consecutive_gap_bounds_coincident_points/_index.md`,
  the whole page (its route rests on the section).

**Read, and at what depth.**

- The section, read in full and re-derived line by line; the page's preamble
  (lines 1--44: purpose, standing sentence, notation) as the shared input.
- The lead page in full.
- Reconstruction pages in the same state, taken as premises at their
  standing and read in full: the preprint's Lemma 2.1, Proposition 3.1,
  Lemma 4.2 with Theorem 4.1, Lemmas 6.1--6.3, Proposition 6.4, Lemma 7.2
  with Theorem 7.1 and Theorem 1.1; the note's Lemma 3.1 (with Lemma 2.1),
  Proposition 4.1 and Theorem 1.1; the balanced-stick Theorem 2 page in
  full; the three 1949 pages (Section 3, (4.3), (5.1)/(5.7)) through their
  Definitions and Statement sections.
- The problem page `wiki/problems/analysis/E1221/_index.md`: the Statement and
  Formulation paragraphs only (lines 14--82).
- Library material: the two 2026 cards and their Theorem 1.1 result pages;
  the held PDFs of the 2026 note (all eight pages, text layer) and the 2026
  preprint (all sixteen pages, text layer), and page 2 of the retained 1949
  scan (Section 1) as a page image.
- Guidance: `docs/verification.md` ("Whole-claim report", "Audit
  checklist", "Grading and claim standing" and the shared checklist),
  `docs/approach_vetting.md`, `docs/evidence.md` "Source fidelity",
  `docs/math_authoring.md`.

**Exposures.** (1) The file names under
`wiki/research/erdos_1221/evidence/verify/` were listed to locate the output
path; none of those files was opened. (2) The two library cards were read
whole, so their "Read status" and "Relation to Problem 1221" paragraphs,
which carry the sources' own standing (claimed, unrefereed, no acceptance
evidence found), reached the reviewer; the result pages' "Hypotheses and
fidelity" and "Bears on" sections likewise. None of this concerns the
standing of the section under review, and no review or grade of any page
was read. (3) Larcher 2015 and Halász 1981 are not held and were not read.
Nothing among the private working files, no web search, no `_index.md` of the folder, no
Current assessment or Known Results text.

## Restatement

Throughout, $\mathcal D$ is the family of sequences of distinct points on
$\mathbb T=\mathbb R/\mathbb Z$ and $\mathcal A$ the family of all
sequences (the site's family): coincident terms allowed, a gap of length
$0$ between coincident terms, and a ratio with denominator $0$ read as
$+\infty$. For a sequence $a$, $M_n^{(r)}(a)$ and $m_n^{(r)}(a)$ are the
largest and smallest sums of $r$ cyclically consecutive gaps cut by the
first $n$ terms ($n\ge r$); $\Lambda_r$, $\lambda_r$, $\mu_r$ carry a
superscript "all" or "dist" for the family over which the outer infimum or
supremum runs.

- **S1 (families).** Because $\mathcal D\subseteq\mathcal A$, for every
  $r\ge1$: $\mu_r^{\mathrm{all}}\le\mu_r^{\mathrm{dist}}$,
  $\Lambda_r^{\mathrm{all}}\le\Lambda_r^{\mathrm{dist}}$ and
  $\lambda_r^{\mathrm{all}}\ge\lambda_r^{\mathrm{dist}}$. The upper bound
  $\mu_r\le1+c'\log r/r$ of Theorem 2 of the balanced-stick preprint (at the
  standing of its reconstruction: for $r\ge2+c\log2$, Theorem 3 imported),
  proved on a sequence of distinct points, holds for $\mu_r^{\mathrm{all}}$.
  The 1949 bounds $\Lambda_r\ge1/\log(1+1/r)$,
  $\lambda_r\le\frac r{r+1}/\log(1+1/r)$ and $\mu_r\ge1+1/r$ hold over
  $\mathcal A$ as their reconstructions state them. The lower bounds of the
  two 2026 sources are stated over $\mathcal D$ and do not transfer by
  inclusion.
- **S2 (model).** At time $n$ the first $n$ terms are listed in cyclic order
  by position, coincident terms by index. The cyclic sequence of the $n$ gap
  lengths (some possibly $0$) does not depend on the tie-break. An $r$-span
  is a sum of $r$ consecutive gaps of the listing, equivalently the
  clockwise distance along the listing from a term to the term $r$ places
  later. $N_n(I)=\#\{i\le n:\ x_i\in I\}$ counts indices. A term inserted
  at an occupied position is placed last in its tie group and splits the
  gap that starts at the previous last term of the group into a zero piece
  and the old gap; hence every insertion splits exactly one gap into two
  consecutive pieces $x,y\ge0$ and changes no other gap or adjacency.
- **S3 (inventory of distinctness).** In the reconstructed arguments,
  distinctness is used (a) to make every span positive, which matters only
  for the finiteness of ratios and is supplied at all late times by the
  contradiction hypotheses ($R_n\le\rho$ for $n\ge N_1$ in the note;
  $\limsup_nM_n/m_n<1+\log r/(100r)$ in Section 5 of the preprint), while
  the one-sided hypotheses (6.1) need no positive span; (b) in Lemma 4.2
  only, through the least distance $\delta$ between distinct points of
  $P_{n_0}$ and the interval holding exactly $L$ points; and (c) nowhere
  else: Lemma 2.1 (index-set bijections, positional displacement bounds,
  averaging with multiplicity), Proposition 3.1 (terminal bounds (3.2) by
  cyclic rank), Lemma 6.1 (zero-sum identity), Lemma 6.2, Lemma 6.3
  (covering identity with empty arcs for zero spans), Proposition 6.4,
  Lemma 7.2 (distinct second coordinates $i/N$), and the note's three pages
  (one insertion splits one gap; all inequalities use gaps $\ge0$).
- **S4 (Proposition 1221.1, existence part).** Let $(x_n)\in\mathcal A$,
  $B\ge1$, $S\ge2$, $n_0\ge1$, and suppose
  $|N_n((x,x+D/n])-D|\le B$ for every integer $n\ge n_0$, every
  $x\in\mathbb T$ and every real $0\le D\le S$. Put $L=\lfloor S\rfloor$.
  Then there are an integer $L'$ with $L-B\le L'\le L+B$ and a list
  $z_1,\ldots,z_{L'}\in(0,1)$, repetitions allowed, such that for every
  $1\le j\le L'$ and every $u\in[0,1]$,
  $|\#\{i\le j:\ z_i<u\}-ju|\le B$, that is, $H_{L'}(z)\le B$.
- **S5 (Proposition 1221.1, bridge and last sentence).** If for every
  $M\ge L_0$ and every list of $M$ pairwise distinct entries in $[0,1)$ one
  has $H_M\ge\frac1{16}\log M$, then the same bound holds for every list of
  $M\ge L_0$ entries in $[0,1)$ with repetitions. Consequently, under the
  hypotheses of S4 and this conditional, $B\ge\frac1{16}\log(L-B)$ whenever
  $L-B\ge L_0$.
- **S6 (Proposition 1221.2).** For every integer $r\ge2$ and every
  $a\in\mathcal A$,
  $\limsup_{n\to\infty}M_n^{(r)}(a)/m_n^{(r)}(a)\ge1+r/(r^2-1)$
  (ratio $+\infty$ where $m_n^{(r)}=0$); proved by the note's chain
  (Lemma 2.1, Lemma 3.1, Proposition 4.1, Theorem 1.1) read with gaps
  $\ge0$.
- **S7 (deduction 1221.3).** Let (P) be the premise that the preprint's
  reconstructed chain, with its two imports (Theorem 4.1 and Theorem 7.1)
  taken as stated, is a proof of the preprint's Theorem 1.1 over
  $\mathcal D$. Then the same chain with Proposition 1221.1 in place of
  Lemma 4.2 proves, for every $a\in\mathcal A$ and every $r$ beyond an
  absolute threshold, $\limsup_n(nM_n^{(r)}-r)\ge c\sqrt{\log r}$,
  $\limsup_n(r-nm_n^{(r)})\ge c\sqrt{\log r}$ and
  $\limsup_nM_n^{(r)}/m_n^{(r)}\ge1+\log r/(100r)$, with the same $c$ and
  the same $1/100$; the page writes "with the same constants $c$, $r_0$ and
  $1/100$". Hence, under (P), all three parts of the mean-normalized
  conjecture hold for the site's family. The deduction is author-recorded
  and (P) is exactly the standing of the claim.
- **S8 (limitations).** Nothing on the page proves
  $\mu_r^{\mathrm{all}}=\mu_r^{\mathrm{dist}}$ or the analogs for
  $\Lambda_r$, $\lambda_r$; under (P) one has
  $\log r/(100r)\le\mu_r^{\mathrm{all}}-1$ and
  $\mu_r^{\mathrm{all}}\le\mu_r^{\mathrm{dist}}\le1+c'\log r/r$ for large
  $r$; the extension is the corpus's reading of the reconstructions,
  asserted by no source and covered by no review.
- **S9 (lead page).** The lead restates S1 and S4--S7 as its route, records
  (P) and the conditional conclusion "with the same constants", names the
  displacement bookkeeping of Lemma 2.1 and the covering identity of Lemma
  6.3 as the two tie-break-sensitive steps, states that no source asserts
  the extension, and states that neither outcome of the proposed
  fresh-context check changes the status of the problem. Its frontmatter
  records `research_state: candidate` and `review_status: unreviewed`.

## Checklist

- **Quantifiers and scope.** Pass. S4's hypothesis is "for all integers
  $n\ge n_0$", and every application in the proof is at a time
  $n=m_j\ge n_0+1$ or $n=N>n_0$ with $0\le D\le S$; the eventual bound
  $R_n\le\rho$ in S6 follows from the strict limsup inequality; the
  conclusions of S6 and S7 are over every sequence of $\mathcal A$; the
  $L'=0$ boundary of S4 is vacuous and harmless (F5).
- **Circularity.** Pass. The bridge in S5 assumes the imported bound for
  distinct lists and derives it for repeated lists by perturbation; no
  target statement is assumed. Proposition 1221.2 assumes the negation of
  its conclusion, as the note does.
- **Model and convention changes.** Pass, this being the item the section
  is about. The multiset model (S2) is checked below to give exactly the
  site's $M_n^{(r)}$, $m_n^{(r)}$; every reconstructed step was re-read
  with the tie-break, and the two places where the tie-break meets
  positions (the moves of Lemma 2.1, the covering identity of Lemma 6.3)
  are re-derived under "Weakest steps". The convention $M/0=+\infty$ is
  stated where used.
- **Finite and statistical overreach.** Not applicable: no finite case
  stands in for a universal statement and no averaging heuristic is used.
- **Uniformity.** Pass with one correction (F1). The absolute constants of
  Proposition 3.1 and Lemma 7.2 and the threshold logic of Sections 5 and 8
  are untouched by the extension except for the ratio threshold, which the
  subtraction of $B$ inside the logarithm may enlarge; "the same $r_0$" is
  not established, "an absolute threshold" is.
- **Extremal conclusions.** Pass. The inequalities of S1 are the correct
  directions for an infimum or supremum over a larger family; S8 correctly
  leaves $\mu_r^{\mathrm{all}}<\mu_r^{\mathrm{dist}}$ open.
- **Consequences and composition.** Pass. The composition in S7 consumes
  Proposition 3.1 at integer times (interface: (2.1) for all large real
  $t$, $A\ge1$, $r\ge C_0A$), Proposition 1221.1 (interface: (4.1) at all
  integers $n\ge n_0$), the bridge (interface: Theorem 4.1 for distinct
  lists), and Sections 6--8 unchanged; each interface is supplied at its
  stated strength. (P) must include the truth of the two imports for the
  conclusion to be unconditional on them; the wording "proves ... with its
  two imported inputs as stated" carries this, and F2 records the one
  misdescription of an import.
- **Computation.** Not applicable: the section has no evidence program and
  claims none.
- **Reproduction.** Not applicable for the same reason; the reviewer's own
  re-derivations are retained below.
- **Source and verdict fidelity.** Pass with one correction (F2). Both 2026
  sources state their theorems over sequences of distinct points (abstracts
  and Theorem 1.1 of each, text layer); the 1949 note's Section 1 takes
  "numbers mod 1" defining $n$ intervals of total length $1$ without a
  distinctness clause (page image); Theorem 4.1 of the preprint is stated
  for every list in $[0,1)$, not only distinct lists; the standing
  sentences of the section and the lead claim author-recorded standing
  only.

## Weakest steps

**W1. The prefix identity and the two-arc bound in Proposition 1221.1.**
Fix $a$ with $(a,a+w]\cap Q=\emptyset$ and with neither $a$ nor $a+w$ a
position of any of the first $N$ terms; such $a$ exist because the excluded
set has measure at most $n_0w<1$ plus finitely many points. Let
$m_1<\cdots<m_{L'}\le N$ be the indices of the terms in $J=(a,a+w]$ and
$z_i=(x_{m_i}-a)/w$, measured along the arc, so $z_i\in(0,1)$. Fix
$1\le j\le L'$ and $n=m_j$. The indices $i\le n$ with $x_i\in J$ are exactly
$m_1,\ldots,m_j$, and $x_{m_i}\in(a,a+uw]$ if and only if $z_i\le u$; hence
$\#\{i\le j:\ z_i\le u\}=N_n((a,a+uw])$ for $0\le u\le1$, whether or not
some of the $z_i$ coincide. Apply the hypothesis at time $n\ge n_0+1$ to the
arc $(a,a+uw]$ of length $D/n$ with $D=nuw\le Nw=L\le S$, and to the arc
$(a+uw,a+w]$ of length $D'/n$ with $D'=n(1-u)w\le S$, whose count is
$j-N_n((a,a+uw])$. With $f(u)=N_n((a,a+uw])-nuw$ the two bounds read
$|f(u)|\le B$ and $|f(1)-f(u)|\le B$, and

$$
\#\{i\le j:\ z_i\le u\}-ju=f(u)-uf(1)=(1-u)f(u)-u\bigl(f(1)-f(u)\bigr),
$$

whose absolute value is at most $(1-u)B+uB=B$. The convention $z_i<u$
gives the left limit of a function bounded by $B$, so the same bound. The
step needs only that the terms in $J$ have indices greater than $n_0$
(so that every prefix time $m_j$ is a time where (4.1) holds), which the
choice of $a$ supplies; the original Lemma 4.2's $\delta$ and its interval
with exactly $L$ points are not used. This composes with the chain exactly
as Lemma 4.2 did: Proposition 3.1 supplies (4.1) at every large integer
time, and the list feeds Theorem 4.1 with $L'\ge L-B$ in place of $L$.

**W2. The perturbation bridge.** Let $z_1,\ldots,z_M\in[0,1)$, and let
$\delta$ satisfy $M^2\delta<\eta$, $M\delta<1-\max_iz_i$ and $M\delta<$ the
least distance between distinct values. Each value $v$ taken by $m\ge2$
entries is spread, in list order, over $v,v+\delta,\ldots,v+(m-1)\delta$.
The new entries lie in $[0,1)$, and the blocks $[v,v+(m-1)\delta]$ of
different values are disjoint from each other and from every unrepeated
value, so the new list is distinct. Fix a prefix $j$ and write
$F(u)=\#\{i\le j:\ z_i<u\}-ju$, $F'$ for the new list. For $u$ outside every
$(v,v+(m-1)\delta]$ each block counts identically for $F$ and $F'$, so
$F'(u)=F(u)$. For $u\in(v,v+(m-1)\delta]$, the prefix holds $m_j\le m$
entries of value $v$, the first $m_j$ of the spread positions (this is
where "in list order" matters), and exactly
$c(u)=\#\{k\le m_j:\ v+(k-1)\delta<u\}\in[1,m_j]$ of them lie below $u$;
all other entries count as at $u=v$. So

$$
F'(u)=F(v)+c(u)-j(u-v),\qquad
F(v)-j(m-1)\delta\ \le\ F'(u)\ \le\ F(v)+m_j=F(v^+),
$$

and $|F'(u)|\le H_M(z)+M^2\delta<H_M(z)+\eta$, since $F(v)$ and $F(v^+)$
are a value and a one-sided limit of $F$ on $[0,1]$. Hence
$H_M(z')\le H_M(z)+\eta$, and the imported bound for the distinct list $z'$
gives $H_M(z)\ge\frac1{16}\log M-\eta$ for every $\eta>0$. Applied with
$M=L'\ge L-B\ge L_0$:
$B\ge H_{L'}(z)\ge\frac1{16}\log L'\ge\frac1{16}\log(L-B)$. The bridge is
logically superfluous, since the reconstruction and the
source state Theorem 4.1 for every list in $[0,1)$, but it is correct and
makes the deduction robust to the weaker reading of the import.

**W3. The note's chain with a zero piece, and the two tie-break-sensitive
identities.** (i) Under the tie-break of S2, the cyclic gap sequence is
well defined and an insertion at an occupied position replaces the gap
$\ell$ after the group by the consecutive pair $0,\ell$. Lemma 2.1 of the
note compares any $r$-block after a split $\ell=x+y$, $x,y\ge0$, with a
block before it by replacing a single piece by $\ell$ or merging both and
adjoining a neighbor; both moves need only $\ell\ge x,y$. Lemma 3.1 part 1
uses $m_{n+1}\ge M_{n+1}/\rho$ (finite ratio, given by $R_{n+1}\le\rho$),
the $r$-blocks $W_i\ge qM_n$, the $(r+1)$-runs $U_i\le M_n$ by merging, and
$h_j=U-W\le\alpha M_n$, all valid for nonnegative gaps including $h_r=0$;
part 2 exhibits after the first split of a marked gap an $r$-block of
length at most $h_j+(r-2)\alpha M_n$, again with nonnegative pieces.
Proposition 4.1 counts gaps as objects (ancestors, descendants, active
gaps, protected blocks) and uses lengths only through Lemma 3.1 and the
monotonicity of $M$; Theorem 1.1 uses the mean identity $M_n\ge r/n$, true
because there are exactly $n$ gaps at time $n$ counting zeros. Under the
"last in the group" convention a zero gap is in fact never split (the gap
after the last term of a group is positive), so the sentence about a zero
gap split into two zero pieces describes a case that does not arise (F3);
the accounting would absorb it anyway. (ii) Terminal bound (3.2): the
terms with positions in an arc $(x,x+\ell]$ form a contiguous block of the
cyclic listing cut at $x$; if $r+1$ of them exist, the first and the
$(r+1)$-th are $r$ places apart and their span is less than $\ell$; for
the lower bound, with $p_0$ the last term at a position $\le x$ (cut at
$x$), the next $r$ terms lie in $(x,\,p_0+(r+b_t)/t]$. (iii) Covering
identity of Lemma 6.3: for $x$ at no term's position, $y_i$ has rank at
most $r$ in the listing cut at $x$ exactly when $y_{i-r}$ is not in the
segment of the listing from the cut to $y_i$, that is, exactly when $x$ lies
in the arc $(y_{i-r},y_i]$ of length $S_{i-r}$; when $S_{i-r}=0$ the arc is
empty and $y_{i-r},\ldots,y_{i-1}$ all precede $y_i$ in the cut listing, so
$y_i$ has rank at least $r+1$. Hence the arcs cover every non-endpoint
$x$ exactly $r$ times. (iv) Lemma 2.1 of the preprint: $F_s$ and $B_s$ are
bijections of the index set of $P_s$, the displacement of $F_s$ at a term
is the sum of $k$ consecutive $r$-spans, all in the (2.1) range, and
$N_t(I)\le N_{t_+}(J+u)$ counts images of distinct indices at distinct
indices; the averaging is an exchange of integrals over indices. Nothing
in (i)--(iv) uses distinct positions.

## Strongest attack

- **S1.** Attempted: find a direction in which inclusion fails. It cannot:
  an infimum over a superset is at most, a supremum at least. The upper
  bound is a value at one sequence of $\mathcal D$, hence an upper bound for
  the infimum over $\mathcal A$. Failed.
- **S2.** Attempted: exhibit two tie-breaks giving different gap sequences
  or an insertion that splits two gaps or none. A group of $k$ coincident
  terms is contiguous in every tie-break and contributes $k-1$ zero gaps
  between the same two positive neighbors; an insertion at a new position
  splits the gap containing it, at an occupied position the gap after the
  group. Failed.
- **S3.** Attempted: find a step that reads an $r$-span as a distance
  between distinct positions or divides by a single gap. The only divisions
  are by $m_n$ (finite ratio hypotheses) and by $D$, $\ell$, $t$ (scales);
  the only uses of "the point $r$ places later" are through the listing.
  Failed; the inventory is complete for the pages named.
- **S4.** Attempted: put an early term into $J$, or a term at $a+w$, or two
  coincident terms in $J$ so that a prefix count and the arc count differ.
  The first two are excluded by the choice of $a$; the third leaves
  $\#\{i\le j:\ z_i\le u\}=N_{m_j}((a,a+uw])$ intact because both sides count
  indices. Attempted: break $D'\le S$ for the complementary arc;
  $D'\le nw\le L$. Failed.
- **S5.** Attempted: a list whose $H$ jumps under every small perturbation.
  The change of a prefix error on a spread block is bounded by
  $j(m-1)\delta\le M^2\delta$, and the all-equal list, the extreme case,
  has $H_M\ge M/2$ before and after. Failed.
- **S6.** Attempted: a sequence with coincident terms whose ratio stays
  below $1+r/(r^2-1)$; a zero gap only lowers some $r$-spans, so the
  ratio worsens. Attempted: an insertion at a group boundary that splits a
  marked zero gap "between" marked gaps and escapes Lemma 3.1's block; under
  the convention the split gap is the one starting at the group's last
  term, a definite gap, and both pieces are consecutive, so part 2 applies
  verbatim. Failed.
- **S7.** Attempted: make the subtraction of $B$ inside the logarithm
  matter. With $B=\frac3{100}\log r+O(1)$ and $\lfloor S\rfloor$ of order
  $\sqrt{r\log r}/\log^2r$,
  $\log(\lfloor S\rfloor-B)=\log\lfloor S\rfloor+o(1)$, and
  $\frac3{100}<\frac1{32}$ still contradicts for large $r$; the
  one-sided parts use no distinctness at all. The only surviving point is
  that the ratio threshold may move (F1). Failed as a refutation.
- **S8.** Attempted: derive $\mu_r^{\mathrm{all}}=\mu_r^{\mathrm{dist}}$
  by perturbing a coincident sequence to a distinct one; the limsup is
  taken as $n\to\infty$, where gaps fall below any fixed perturbation
  scale, so no such transfer follows from the page, and the page claims
  none. Failed.
- **S9.** Attempted: find a sentence of the lead claiming more than the
  section proves. "With the same constants" inherits F1; "proved
  replacement" in the desc is a wording point (F6). Failed.

## Premises

- **Preprint Lemma 2.1 page** (`ko26b_lemma_2_1_reconstruction`): interface
  (2.1) for all large real $t$ with $A\ge1$, moves by $kr$ places, (2.2) and
  (2.3) for $q=E/(kr)<1$, threshold uniform for $D$ in a bounded range.
  Read in full. Source pp. 4--5 read in the text layer; held.
- **Preprint Proposition 3.1 page**: interface (2.1), $A\ge1$, $r\ge C_0A$;
  conclusion (3.1) at all large $t$, uniform in $x$ and $0\le D\le S$. Read
  in full. Source pp. 6--7, text layer; held.
- **Preprint Lemma 4.2 page with Theorem 4.1**: Theorem 4.1 stated for
  every list in $[0,1)$ of length $L\ge L_0$ (matches the source, p. 7);
  Lemma 4.2 needs (4.1) at all large integers and uses $\delta$ and an
  $L$-span, the two distinctness uses the section names. Read in full.
  Source pp. 7--8, text layer; held. Larcher 2015: not held, not read.
- **Preprint Lemmas 6.1--6.3, Proposition 6.4, Lemma 7.2 with Theorem 7.1,
  Theorem 1.1 pages**: interfaces (6.1) with $A\ge1$, (6.2), (6.5),
  $Z_t(r)\le A$, (6.7) with $r\ge C_2A$, (7.1) with $S\ge S_0$, $B\ge1$;
  Theorem 7.1 for every set of $M\ge2$ points of $[0,1]^2$. Read in full.
  Source pp. 2, 9--15, text layer; held. Halász 1981: not held, not read.
- **Note Lemma 3.1 (with Lemma 2.1), Proposition 4.1, Theorem 1.1 pages**:
  interfaces $R_n\le\rho$ eventually, $\eta\in(0,1)$,
  $\beta=(r-1)(\rho-1+\eta)\in(0,1)$, $n+1\ge2r$, $N\ge\max(N_1,2r)$. Read
  in full. Source pp. 2--7 read in the text layer (whole note); held.
- **Balanced-stick Theorem 2 page**: $\mu_r\le1+c'\log r/r$ for
  $r\ge2+c\log2$ on the van der Corput or golden-ratio sequence, both of
  distinct points; Theorem 3 imported. Read in full; the PDF was not
  opened, the transfer by inclusion needing only the statement.
- **1949 pages** (Section 3, (4.3), (5.1)/(5.7)): definitions and statements
  over every sequence with intervals of length $0$ allowed and ratio
  $+\infty$ where $m=0$. Read through their Statement sections. Source
  Section 1 checked on the page image (PDF p. 2); held.
- **Problem page E1221**: Statement and Formulation paragraphs only. The
  section's references to "remaining gap (5)", to the folder index and to
  "status open", and the lead's references to the dated Current assessment
  and to filed reconstruction reviews, lie outside this review's read set
  and are recorded as unverified here, not as findings.

## Findings

- **F1 (suggested).** Location: deduction 1221.3, lines 479--481, "proves
  the three bounds of Theorem 1.1, with the same constants $c$, $r_0$ and
  $1/100$, for every sequence on $\mathbb T$"; the lead, line 104, "with the
  same constants". Defect: the argument shows the same $c$ (Section 8 is
  unchanged) and the same $1/100$ (the comparison $\frac3{100}<\frac1{32}$
  is unchanged), but the ratio threshold now has to satisfy
  $\lfloor S\rfloor-B\ge L_0$ and $B<\frac1{16}\log(\lfloor S\rfloor-B)$,
  strictly stronger than the original $\lfloor S\rfloor\ge L_0$ and
  $B<\frac1{16}\log\lfloor S\rfloor$; since $r_0$ is an unspecified
  existential constant, "the same $r_0$" is not something the chain
  establishes. Witness: any $r$ at which the original comparison holds with
  margin less than $\frac1{16}\log(1-B/\lfloor S\rfloor)^{-1}$. Proposed
  replacement: "with the same $c$ and the same coefficient $1/100$, and an
  absolute threshold in place of $r_0$".
- **F2 (suggested).** Location: deduction 1221.3, lines 477--478, "with its
  two imported inputs as stated there (Theorem 4.1 for lists of distinct
  entries and Halász's Theorem 7.1)". Defect: the Lemma 4.2 page, like the
  source (p. 7), states Theorem 4.1 for every list $z_1,\ldots,z_L\in[0,1)$;
  "for lists of distinct entries" is not the statement there. The slip is
  harmless, since (P) with the weaker import is a weaker premise and the
  bridge of Proposition 1221.1 restores the general case. Proposed
  replacement: "(Theorem 4.1, stated there for every list in $[0,1)$, of
  which only the case of distinct entries is needed, and Halász's Theorem
  7.1)".
- **F3 (note).** Location: proof of Proposition 1221.2, "a zero gap may
  later be split into two zero pieces, which the descendant accounting
  treats like any split". Under the section's own tie-break (a new
  coincident term comes last and splits the gap after the group) the gap
  split is always positive, so a zero gap is never split. The sentence
  describes a case that does not arise; the accounting would absorb it, so
  nothing depends on it. Proposed replacement: "a zero piece is never split
  again under this tie-break".
- **F4 (note).** Location: "Where distinctness enters", second bullet, "The
  least distance $\delta$ ... used to keep early terms out of the short
  interval and to produce an interval with exactly $L$ terms". The
  exactly-$L$ interval in Lemma 4.2 uses distinctness (the half-open
  $L$-span arc, translated by a small $\varepsilon$), not $\delta$;
  $\delta$ serves the early-term exclusion only. Both uses are replaced,
  so the inventory's conclusion stands.
- **F5 (note).** Location: Proposition 1221.1, statement. When $B\ge L$,
  $L'=0$ is possible and the list is empty; the last sentence's condition
  $L-B\ge L_0$ excludes this, but the existence part could say "$L'\ge1$
  when $L>B$".
- **F6 (note).** Location: the lead's `desc`, "a proved replacement for the
  short-interval list lemma". The body calls Proposition 1221.1
  author-recorded with proof; "proved" in the summary reads as a standing
  word. Proposed replacement: "an author-recorded replacement, with proof".

## Verdict

- S1 (families): refutation-failed.
- S2 (model): refutation-failed.
- S3 (inventory of distinctness): refutation-failed; F3 and F4 are wording
  notes on the inventory, not gaps in it.
- S4 (Proposition 1221.1, existence part): refutation-failed; F5.
- S5 (Proposition 1221.1, bridge and last sentence): refutation-failed.
- S6 (Proposition 1221.2): refutation-failed.
- S7 (deduction 1221.3): refutation-failed for the deduction with its
  constants clause read as "absolute constants, the same $c$ and $1/100$";
  the clause "the same $r_0$" is not established by the argument (F1), and
  the description of the import in (P) is inexact (F2).
- S8 (limitations): refutation-failed.
- S9 (lead page): refutation-failed; inherits F1 and carries F6.

Limitations: the two external imports (Theorem 4.1 as derived from Larcher's
proof; Halász's Theorem 7.1) were not checked, exactly as the section and
the lead disclose; the reconstruction pages were used as premises at their
standing and only their use with gaps $\ge0$ was re-derived; the
statements about the problem page's Current assessment, its remaining gap
(5), the folder index and the filed reviews lie outside the commissioned
read set and are neither confirmed nor contradicted here. Required
corrections: none. This focused review assigns no tier and changes no
status.

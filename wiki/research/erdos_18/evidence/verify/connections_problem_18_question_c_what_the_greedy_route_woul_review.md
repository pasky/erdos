---
name: research/erdos_18/evidence/verify/connections_problem_18_question_c_what_the_greedy_route_woul_review
title: "Independent review of the connections section: Problem 18, question (c): what the greedy route would need"
desc: |
  Refutation review of the question (c) section: the necessary condition,
  the natural profile, the mean-gap floor and the Berend-Harmse comparison
  survive; the consequence "C = 2 is impossible for the greedy route" is
  proved only for the natural profile (one required correction), and three
  assessment sentences need weaker wording (suggested).
created: 2026-09-28T18:13:26Z
updated: 2026-09-28T18:13:26Z
---

***

## Subject and independence

Role: independent reviewer in a fresh context, commissioned for refutation
of this section only. The reviewer took no part in writing the page, the
reconstruction pages or the library cards, and read no review, grade,
standing or acceptance record of this folder.

Subject: path `wiki/research/erdos_18/connections.md` as it stood at
2026-09-28T13:50:48Z, section "## Problem 18, question (c): what the greedy
route would need", lines 551-585 (from its H2 heading to the line before the
Problem 1099 heading), on
[[research/erdos_18/connections|the connections page]]. The assignment names no
separate lead page; the section is the whole subject.

What was read, and at what depth:

- The section, lines 551-585, in full and repeatedly.
- The page's front matter, opening paragraph and Conventions paragraph
  (lines 1-45) and the Shared lemmas section (lines 47-243) as inputs:
  Lemmas A, B, C, C' and D. The section consumes only Lemma B's interface;
  Lemma B's proof is another reviewer's subject. The definition of
  $(\mathrm H_c)$ at lines 450-452, inside the question (a) section, was
  read because the section cites it (see the exposures).
- Reconstruction pages as of the same time, in full, as premises:
  [[research/erdos_18/hughes_theorem_1_reconstruction|Theorem 1]],
  [[research/erdos_18/hughes_corollary_3_reconstruction|Corollary 3]],
  [[research/erdos_18/hughes_remark_6_reconstruction|Remark 6]],
  [[research/erdos_18/hughes_lemma_4_reconstruction|Lemma 4]] and
  [[research/erdos_18/doorn_lemma_3_2_reconstruction|Lemma 3.2]].
- The Statement paragraph of [[problems/divisors/E0018/_index|Problem 18]]
  (lines 19-29 of the problem page).
- Library: the provenance paragraphs of
  [[../library/divisors/hughes_2026_sums_distinct_divisors_factorials/_index|Hughes (2026)]]
  (lines 1-57 of the card, which include its Read status and Bears on
  paragraphs) and the statement sections of its result pages `theorem_1`,
  `theorem_2` (with the paper's Corollary 3) and `remark_6`; the opening and
  provenance paragraphs and "The statement verified" of
  [[../library/divisors/jenw1n_2026_lean_proof_erdos_problem_18b/_index|the accepted-proof record]]
  (lines 1-59 of the card) and the Source, Statement, Formal statement,
  "How the file closes the target (structure only)" and Dependencies
  sections of
  [[../library/divisors/jenw1n_2026_lean_proof_erdos_problem_18b/target|its target page]]
  (lines 1-68); the held Hughes PDF, full text layer (pp. 1-5) and the page
  images of pp. 2 and 5.
- Guidance: `docs/verification.md` "Grading and claim standing", "Audit
  checklist" (the canonical failure modes and the Erdos list) and
  "Whole-claim report"; `docs/approach_vetting.md`; `docs/evidence.md`
  "Source fidelity"; `docs/math_authoring.md`.

Exposures: (1) the search that located the $(\mathrm H_c)$ definition
printed fragments of lines 454-544 of the question (a) section (the label
of transfer (18a.1), "with $c\le4$ after decreasing $c$", "necessarily
$c\le2\log2+o(1)$", "$\kappa_{\min}(x)=$", "A proof of $(\mathrm H_c)$ for
any $c>0$ gives exponent 2"), and lines 445-449 and 454-458 (the statement
of (18a.1)) were displayed with the definition; none of it is used here.
(2) A heading search of the problem page printed its front matter line
`status: open` and the first line of its Status paragraph ("Open for the
exact three-part question. The second question,"); nothing further of its
Status, Current assessment, Known results or Linked library material text
was read. (3) The Hughes card's Bears on paragraph and the accepted-proof
card's opening paragraph carry acceptance and supersession sentences about the
sources (site verification and certification dates; "superseded by the
site-accepted proof"); they were read inside the provenance paragraphs and
are not used as standing here. (4) The reconstruction pages' Standing
paragraphs were read as parts of those pages. (5) Directory listings showed
the names of other review files under this folder's `evidence/verify/` and
of untracked files in other folders; none was opened. No web search was
made.

## Restatement

Throughout, $N=n!$, $h$ is the page's $h$ (over $1\le m\le N$), the window
of index $j$ is $[\sqrt{(j-1)!},\sqrt{j!}]$, and a *profile* is a pair
$(T,\delta)$ admissible in Lemma B: $T\ge2$, $2T\le\sqrt N$,
$\delta\colon[T,\sqrt N]\to(0,1/8]$ nonincreasing, with
$\sigma(\ell)=\log(1/\delta(e^\ell/2))$ on $[\log(2T),\tfrac12\log N]$.
"The greedy route" is Lemma B applied to $n!$, which is how the section
introduces it. Line numbers refer to the page as of 2026-09-28T13:50:48Z.

- **S1** (target; lines 553-555). Question (c) asks whether
  $h(n!)<(\log n)^{O(1)}$. The known bounds are $h(n!)\gg(\log n)^2$
  (Remark 6) and, for every $\varepsilon>0$, $h(n!)<n^{\varepsilon}$ for
  all large $n$ (the accepted answer to (b)). The clause "the page records
  it as open" describes excluded text and is not checked here.
- **S2** (necessary condition and natural profile; lines 557-562). If
  Lemma B with some profile gives $h(n!)\ll(\log n)^C$, then
  $\int_{\log(2T)}^{\frac12\log n!}d\ell/\sigma(\ell)\ll(\log n)^C$, over
  a range of length $\sim\tfrac12n\log n$. The profile
  $\sigma(\ell)=\ell/(\log n)^{C-1}$ (the natural profile) has integral
  $\sim(\log n)^C$ and is the hypothesis that every pair of consecutive
  divisors $d<b$ of $n!$ with geometric mean $g=\sqrt{db}\in[T,\sqrt N]$
  satisfies $\log(b/d)\le\tfrac12(2g)^{-1/(\log n)^{C-1}}$, a ratio
  $1+O(g^{-1/(\log n)^{C-1}})$.
- **S3** (demand at the middle; lines 562-563). For the natural profile,
  at $g=\sqrt{n!}$ the demanded $\delta$ is $\exp(-n/(2(\log n)^{C-2}))$
  to leading order in the exponent.
- **S4** (mean-gap floor; lines 563-568). Some pair of consecutive
  divisors $d<b$ of $n!$ whose geometric mean lies in (or at the edge of)
  the window of index $n$, hence in $[T,\sqrt N]$, has
  $\log(b/d)\ge\tfrac12\log n/\tau(n!)$; since
  $\log\tau(n!)\asymp n/\log n$, this is $\exp(-O(n/\log n))$.
- **S5** (consequence; lines 568-569). "Hence $C=2$ is impossible for the
  greedy route, consistent with Remark 6." Narrow reading: the natural
  profile with $C=2$ violates Lemma B's hypothesis at the window of index
  $n$. Reading as written: no admissible profile gives
  $h(n!)\ll(\log n)^2$ through Lemma B.
- **S6** (characterization of $C=3$; lines 569-572). The natural profile
  with $C=3$ asks the largest gap to match the mean gap of S4 up to a
  constant factor in the exponent at every scale; this is the factorial
  analog of $(\mathrm H_c)$, of the same mean-gap character. Here
  $(\mathrm H_c)$ (page lines 450-452) reads: there are $c>0$ and $x_0$
  such that for every $x\ge x_0$, every pair of consecutive divisors $d<b$
  of $L_x$ with $x\le\sqrt{db}\le\sqrt{L_x}$ satisfies
  $\log(b/d)\le(db)^{-c/(2\log x)}$.
- **S7** (Berend-Harmse comparison; lines 572-574). The gap the imported
  estimate guarantees at the window of index $n$,
  $\varepsilon_n=\exp(-(1-o(1))(\log n)^2/(2\log2))$, is exponentially
  wider than the $C=3$ demand of S3, which is why Theorem 1 gives
  $n/\log n$.
- **S8** (the accepted proof; lines 576-583). The accepted proof of (b)
  does not run through a gap profile: read at the level of its top-level
  theorem statements, it reduces the target to a Fourier-decay (dyadic
  mixing) property on $\mathbb Z/2^J$, closer to the character-sum
  criterion of Lemma 3.2 than to a greedy count, and nothing about divisor
  gaps is extracted from that reading.
- **S9** (outcome; lines 583-584). Open; the greedy route to (c) is a
  mean-gap problem for the divisors of $n!$ at least as hard as
  $(\mathrm H_c)$.
- **S10** (framing; line 557). "Lemma B is the only mechanism of this
  folder aimed at $n!$." A description of the folder, not mathematics.

## Checklist

- **Quantifiers and scope.** One failure: S5 quantifies over "the greedy
  route" while its argument treats one profile family (F1). S4 is a
  genuine existence statement inside Lemma B's range: the pair at the top
  edge brackets $\sqrt N$, its mirror pair brackets $\sqrt N$ too, so the
  two coincide and $db=N$ (W1). Elsewhere the statements are asymptotic in
  $n$ with $C$ fixed, as written.
- **Circularity.** None. Remark 6 and the floor of S4 are different counts
  (subset counting against pigeonhole on gap lengths); S5 cites Remark 6
  for consistency only.
- **Model and convention changes.** The page's $h$ (over $m\le N$)
  dominates the site's $h$, every bound is stated for the page's $h$, and
  Remark 6's counting works for either, so nothing is lost. S6 and S9
  compare formula shapes (a profile linear in $\ell$) with $(\mathrm H_c)$
  without an entailment in either direction (F4).
- **Finite and statistical overreach.** None; no finite data or heuristic
  average is used as a proof.
- **Uniformity.** The $(1+o(1))$ and $(1-o(1))$ factors dropped from the
  exponents in S3 and S7 do not affect the comparisons, which are between
  exponents of different orders (N1). The constant in
  $\log\tau(n!)\ll n/\log n$ is absolute (Remark 6 page). The phrase "at
  every scale" in S6 is not uniform (F2).
- **Extremal conclusions.** The floor of S4 is computed in the claim's own
  units, the logarithmic ratio of consecutive divisors, from a covering
  count: at most $\tau(n!)-1$ consecutive pairs cover a window of
  logarithmic length $\tfrac12\log n$.
- **Consequences and composition.** Each "hence" was attacked on its own.
  S5's reading as written does not follow (F1); S8's main clause asserts a
  property of an unread proof body (F3); S9's comparison has no bridge
  (F4).
- **Computation.** Inapplicable: the section computes nothing. The
  reviewer's numerical checks (the constant $c_\tau$ and the capped-profile
  integral below) are illustrative and carry no verdict.
- **Reproduction.** Inapplicable: no rerun instruction or coverage claim.
- **Source and verdict fidelity.** Remark 6 page: $\log\tau(n!)\ll n/\log n$
  is proved there, as cited. Corollary 3 page and Hughes p. 2 (page image):
  display (1) gives
  $\log(1/\varepsilon_n)=\frac{(\log n)^2}{2\log2}\bigl(1-\frac{2\log(\log n/\log2)}{\log n}\bigr)$,
  so S7's value is the leading order. Target page: its structure section
  describes the mixing property as Fourier decay of an $r$-fold product of
  the measure on $\mathbb Z/2^J$ at odd frequencies and says the body was
  not read; the section's paraphrase matches, but its categorical "does not
  run through a gap profile" is stronger than the read record (F3). Lemma
  3.2 page: a character-sum criterion, as named. Problem 18 statement:
  question (c) quoted correctly. "The page records it as open": excluded,
  not checked.

## Weakest steps

**W1: the floor of S4, re-derived.** Let $x_1<\dots<x_k$ be the divisors
of $n!$ in $W=[\sqrt{(n-1)!},\sqrt{n!}]$, let $x_0$ be the largest divisor
below $\sqrt{(n-1)!}$ and $x_{k+1}$ the smallest above $\sqrt{n!}$; $n!$ is
not a square for $n\ge2$ because a prime in $(n/2,n]$ has exponent one. For
$n\ge3$ the divisors $1$ and $n!$ lie outside $W$, so $k\le\tau(n!)-2$, and
the $k+1\le\tau(n!)-1$ consecutive pairs $(x_i,x_{i+1})$ cover $W$, whose
logarithmic length is $\tfrac12\log n$; one pair has
$\log(x_{i+1}/x_i)\ge\tfrac12\log n/(\tau(n!)-1)>\tfrac12\log n/\tau(n!)$.
Its geometric mean is in Lemma B's range: for $1\le i\le k-1$ both ends are
in $W$; for $i=0$, the ratio-two property gives $x_0\ge x_1/2$, so
$\sqrt{x_0x_1}\ge\sqrt{(n-1)!/2}\ge T$ for large $n$ when
$\log T=o(n\log n)$; for $i=k$ the pair brackets $\sqrt N$, and so does its
mirror $(N/x_{k+1},N/x_k)$, a pair of consecutive divisors by the
order-reversing bijection, so the two pairs coincide and $x_kx_{k+1}=N$.
Finally $\log\tau(n!)\le c_1n/\log n$ (Remark 6 page) gives
$\tfrac12\log n/\tau(n!)\ge\exp(-c_1n/\log n)$ for large $n$. The lower
bound $\log\tau(n!)\gg n/\log n$ (the primes in $(n/2,n]$, each of exponent
one, number $\gg n/\log n$ by Chebyshev) is true but is not needed for the
form $\exp(-O(n/\log n))$.

**W2: S5 on the narrow reading.** For the natural profile with $C=2$,
$\delta(g)=(2g)^{-1/\log n}$; on and near $W$ every $g\ge\sqrt{(n-1)!/2}$
gives
$\delta(g)\le\exp(-(\tfrac12\log(n-1)!+\tfrac12\log2)/\log n)=\exp(-(1+o(1))n/2)$.
The pair of W1 has $\log(b/d)\ge\exp(-c_1n/\log n)>\tfrac12\exp(-(1+o(1))n/2)$
for large $n$, so Lemma B's hypothesis fails. This is exactly what the
"hence" proves; the reading as written is the subject of the strongest
attack.

**W3: S2, necessity and translation.** Lemma B's bound is
$3I+\log_2\sigma(\tfrac12\log N)+2\log_2(2T)+5$ with $I$ the integral, and
every term is nonnegative because $\sigma\ge\log8$; so $h(n!)\ll(\log n)^C$
from Lemma B forces $I\ll(\log n)^C$. For the natural profile,
$I=(\log n)^{C-1}\log\bigl(\tfrac12\log n!/\log(2T)\bigr)$; admissibility
needs $\sigma\ge\log8$ on the range, that is
$\log(2T)\ge\log8\cdot(\log n)^{C-1}$, and at that threshold
$I=(\log n)^C(1+O(\log\log n/\log n))$ while the other terms are
$O((\log n)^{C-1})$. The translation to gaps is exact:
$\delta(g)=e^{-\sigma(\log(2g))}=(2g)^{-1/(\log n)^{C-1}}$, and the
hypothesis $\log(b/d)\le\tfrac12\delta(\sqrt{db})$ is the stated ratio
bound. At $g=\sqrt{n!}$,
$\log(1/\delta)=(\log2+\tfrac12\log n!)/(\log n)^{C-1}=(1+o(1))\,n/(2(\log n)^{C-2})$
by Stirling, which is S3.

## Strongest attack

Against S5 as written: exhibit an admissible profile whose integral is
$O((\log n)^2)$ and whose gap demand the floor of S4 does not contradict.
Put $c_\tau=\sum_{k\ge1}\log(1+1/k)/k\approx1.2577$, fix $0<c<c_\tau$
(say $c=1/2$), and take

$$
\sigma(\ell)=\min\Bigl(\frac{\ell}{\log n},\ \frac{cn}{\log n}\Bigr),
\qquad \log(2T)=\log8\cdot\log n .
$$

This $\sigma$ is nondecreasing and at least $\log8$ on the range, so
$\delta=e^{-\sigma}$ is nonincreasing with values in $(0,1/8]$, and
$2\log_2(2T)=O(\log n)$. Splitting the integral at $\ell=cn$,

$$
\int_{\log(2T)}^{\frac12\log n!}\frac{d\ell}{\sigma}
=\log n\cdot\log\frac{cn}{\log8\cdot\log n}
+\frac{\log n}{cn}\Bigl(\tfrac12\log n!-cn\Bigr)
\le\Bigl(1+\frac1{2c}\Bigr)(\log n)^2 ,
$$

so Lemma B would give $h(n!)\le3(1+1/(2c))(\log n)^2+O(\log n)$ if its
hypothesis held. That hypothesis demands, for every consecutive pair with
geometric mean in $[e^{cn}/2,\sqrt N]$, that
$\log(b/d)\le\tfrac12\exp(-cn/\log n)$. The floor of S4 says only that some
pair at the window of index $n$ has
$\log(b/d)\ge\tfrac12\log n/\tau(n!)=\exp(-(c_\tau+o(1))\,n/\log n)$, where
$\log\tau(n!)=(c_\tau+o(1))\,n/\log n$ follows from $v_p(n!)=\lfloor n/p\rfloor$
for $p>\sqrt n$, the prime number theorem applied to the primes in each
$(n/(k+1),n/k]$, a contribution $O(\sqrt n\log n)$ from $p\le\sqrt n$ and
$O((\log K/K)\,n/\log n)$ from the primes with $n/p>K$. Since $c<c_\tau$,
the floor lies below the demand: the section's obstruction does not exclude
this profile, hence does not exclude exponent $2$ for Lemma B. Whether the
demand holds is a maximal-gap question about the divisors of $n!$ in the
windows of index $j\asymp n$ that nothing in the folder decides. The attack
succeeds against the reading as written and fails against the narrow
reading (W2).

What the counting does prove, for every admissible profile: the pair of W1
forces $\delta(g)\ge\log n/\tau(n!)$ at some $g\ge\sqrt{(n-1)!/2}$, hence,
$\sigma$ being nondecreasing, $\sigma(\ell)\le\log\tau(n!)$ for all
$\ell\le\log(2g)$, and
$\log(2g)\ge\tfrac12\log n!-\tfrac12\log n+\tfrac12\log2$.
Therefore

$$
\int_{\log(2T)}^{\frac12\log n!}\frac{d\ell}{\sigma}
\ \ge\ \frac{\tfrac12\log n!-\tfrac12\log n-\log(2T)}{\log\tau(n!)}
\ =\ \Bigl(\frac1{2c_\tau}-o(1)\Bigr)(\log n)^2
$$

whenever $\log T=o(n\log n)$; so the greedy route cannot beat exponent $2$,
which is what Remark 6 gives for every route, and Lemma B's bound is never
below $(3/(2c_\tau)-o(1))(\log n)^2\approx1.19\,(\log n)^2$. This is the
correct content of the "hence" sentence (F1).

Attacks on the other statements. S2 and S3 were re-derived (W3) and
survive. S4 survives (W1); the attack that the extremal pair might fall
outside Lemma B's range fails by the mirror argument. S7 compares exponents
of orders $(\log n)^2$ and $n/\log n$ and survives; the clause on Theorem 1
matches the Theorem 1 page, whose lower-range count is
$\sum_j\tfrac12\log j/s_j$ with $s_j\sim(\log j)^2/(2\log2)$. S6, S8 and S9
are assessment sentences; the attacks on their wording are F2, F3 and F4.

## Premises

- Lemma B (page lines 87-159): shared lemma, author-recorded, proof not
  this review's subject. Interface consumed: the shape of the bound
  $3I+\log_2\sigma(\tfrac12\log N)+2\log_2(2T)+5$ and the hypothesis on
  pairs with $T\le\sqrt{db}\le\sqrt N$, $\delta\le1/8$ nonincreasing,
  $\sigma\ge\log8$. The ratio-two property of $n!$ it needs is proved on
  the Lemma 4 page.
- Theorem 1 reconstruction: facts (i) and (ii) on bracketing divisors, the
  windows, and $s_j\sim(\log j)^2/(2\log2)$; read in full; premise at its
  recorded standing (proved modulo the second-hand Berend-Harmse import).
- Corollary 3 reconstruction: $\varepsilon_j$, display (1), and the
  Berend-Harmse estimate in the form the Hughes preprint prints (the 1993
  paper is not held); read in full and checked against Hughes p. 2.
- Remark 6 reconstruction: $h(n!)\gg(\log n)^2$ and
  $\log\tau(n!)\ll n/\log n$ from Chebyshev's upper bound; read in full and
  checked against Hughes pp. 4-5.
- Lemma 4 reconstruction: the greedy step and the ratio-two property of
  $n!$; read in full.
- Lemma 3.2 reconstruction: the character-sum criterion, a *claimed* result
  of the van Doorn note; only its nature (Fourier-analytic residue
  representation) is used by S8; read in full.
- Problem 18 Statement: question (c) as quoted.
- Hughes (2026) card and result pages `theorem_1`, `theorem_2`, `remark_6`:
  provenance (arXiv:2609.10902v1, held PDF) and statements; text layer
  pp. 1-5 and page images pp. 2 and 5 read.
- The accepted-proof card and target page: provenance (a Conjectures.io
  record;
  proof file not held, not built here) and the target statement; the
  structure section read at the depth it declares (statements only, body
  unread).
- Standard facts used without a page: Stirling's formula; Chebyshev's
  bounds on $\pi(x)$; and, for the reviewer's constant $c_\tau$ only, the
  prime number theorem, which no verdict depends on.

## Findings

**F1 (required).** Location: lines 568-569, "Hence $C=2$ is impossible for
the greedy route, consistent with Remark 6". Defect: the argument shows
that the natural profile $\sigma(\ell)=\ell/\log n$ violates Lemma B's
hypothesis at the window of index $n$; it does not show that Lemma B cannot
give $h(n!)\ll(\log n)^2$ with another profile, which is what "impossible
for the greedy route" asserts. Witness: the capped profile of the strongest
attack, admissible, with integral at most $(1+1/(2c))(\log n)^2$ and a
demand of $\tfrac12\exp(-cn/\log n)$ at the top windows for any
$c<c_\tau\approx1.26$, which the floor $\exp(-(c_\tau+o(1))n/\log n)$ does
not contradict. Proposed replacement: "Hence the natural profile with $C=2$
is inadmissible, and no admissible profile does better than exponent $2$:
the pair above forces $\sigma\le\log\tau(n!)$ on all but the last
$\tfrac12\log n+O(1)$ of the range, so the integral is at least
$(1/(2c_\tau)-o(1))(\log n)^2$ with
$c_\tau=\sum_{k\ge1}\log(1+1/k)/k\approx1.26$, consistent with Remark 6.
Whether a profile capped at $\sigma=cn/\log n$ with $c<c_\tau$, whose
integral is $O((\log n)^2)$, satisfies the hypothesis is a maximal-gap
question that the counting leaves open."

**F2 (suggested).** Location: lines 569-572, "$C=3$ asks the largest gap
to match this mean gap up to a constant in the exponent at every scale".
Defect: the natural profile with $C=3$ demands $\exp(-\ell/(\log n)^2)$ at
scale $\ell=\log(2g)$, which matches the mean gap up to a constant only for
$\ell\asymp n\log n$ (windows of index $j\asymp n$), the constant depending
on $\ell/(n\log n)$; below that the demand is much weaker than mean-gap
matching. Witness: for $\log\prod_{n/2<p\le n}p\le\ell\le\tfrac12\log n!$,
a range starting at $(\tfrac12+o(1))n$, every subset $S$ of the primes in
$(n/2,n]$ times a divisor of $n!/\prod_{n/2<p\le n}p$ chosen by the
ratio-two property of that cofactor (Lemma A applies to it) gives a divisor
of $n!$ in $[e^\ell,2e^\ell]$, and distinct $S$ give distinct divisors; so
at least $2^{\pi(n)-\pi(n/2)}=\exp(\Theta(n/\log n))$ divisors lie in every
such interval and the mean gap there is $\exp(-\Theta(n/\log n))$, while
the demand at $\ell=n$ (window index about $2n/\log n$) is only
$\exp(-n/(\log n)^2)$. Proposed replacement: "matches the mean gap up to a
constant in the exponent throughout the windows of index $j\asymp n$, and
asks less below them".

**F3 (suggested).** Location: lines 576-579, "The accepted proof of (b)
does not run through a gap profile: its structure, read only at the level
of theorem statements on the accepted target page, is a Fourier-decay
property ...". Defect: the categorical main clause asserts a property of
the proof body, which the target page states was not read; the read record
supports only that the top-level reduction is to a Fourier-decay property.
Witness: the target page's own sentence "the body was not read". Proposed
replacement: "As far as its top-level statements show, the accepted proof
of (b) does not run through a gap profile: ...".

**F4 (suggested).** Location: lines 583-584, "the greedy route to (c) is a
mean-gap problem for the divisors of $n!$ at least as hard as
$(\mathrm H_c)$". Defect: "at least as hard" asserts a comparison for which
no reduction is given in either direction. $(\mathrm H_c)$ at $x=n$
transfers to $n!$ only at scales $g\le\sqrt{L_n/2}=e^{(1/2+o(1))n}$: the
divisors of $L_n$ divide $n!$, so a consecutive pair $d<b$ of $n!$ sits
inside a consecutive pair $d_1\le d<b\le b_1$ of $L_n$ with
$d_1b_1\in[db/2,2db]$ by the ratio-two property of $L_n$, and inherits its
gap bound there; this covers only the bottom of the factorial range, and a
factorial gap hypothesis says nothing about $L_x$. Proposed replacement:
"of the same mean-gap character as $(\mathrm H_c)$; neither hypothesis is
known to imply the other".

**N1 (note).** Lines 563 and 573 write the demanded gap
$\exp(-n/(2(\log n)^{C-2}))$ and the Berend-Harmse gap
$\exp(-(\log n)^2/(2\log2))$ without the factors $(1+o(1))$ and $(1-o(1))$
in the exponent (Stirling:
$\tfrac12\log n!=\tfrac12n\log n-\tfrac12n+O(\log n)$; display (1) of the
Corollary 3 page). Harmless for the comparisons made.

**N2 (note).** Line 559 uses $\ell_0$ without defining it; Lemma B's lower
limit is $\log(2T)$.

**N3 (note).** Line 557, "Lemma B is the only mechanism of this folder
aimed at $n!$": Lemma A's factorial clause, Lemma C' and the Theorem 1
reconstruction also concern $n!$; the sentence means the only mechanism
that could reach question (c), and could say so.

**N4 (note).** Line 568, "the primes in $(n/2,n]$ give the lower bound":
this uses Chebyshev's lower bound $\pi(n)-\pi(n/2)\gg n/\log n$, which no
page in the read set proves; the argument does not use the lower bound.

## Verdict

- S1: refutation-failed for the mathematical content (the two bounds); the
  clause "the page records it as open" lies outside the read set and is
  unchecked.
- S2: refutation-failed.
- S3: refutation-failed (to leading order in the exponent; N1).
- S4: refutation-failed.
- S5: proof defective; statement unresolved, on the reading the words carry
  ("no admissible profile gives $h(n!)\ll(\log n)^2$ through Lemma B"; F1);
  refutation-failed on the narrow reading ("the natural profile with $C=2$
  is inadmissible").
- S6: refutation-failed at the windows of index $j\asymp n$; the clause "at
  every scale" is refuted-as-stated as a uniform statement (F2), which
  affects no bound.
- S7: refutation-failed.
- S8: proof defective; statement unresolved for the main clause "does not
  run through a gap profile" (asserted beyond the read record; F3); the
  paraphrase of the target page's structure is faithful.
- S9: proof defective; statement unresolved for "at least as hard as
  $(\mathrm H_c)$" (no reduction in either direction; F4); "open" is not
  contested.
- S10: not a claim.

Limitations: the review did not read the accepted proof file, the
Berend-Harmse paper (not held) or any excluded page; the constant $c_\tau$
is the reviewer's own derivation and enters only the replacement text
proposed in F1, where any $c<c_\tau$ suffices for the witness. This focused
review assigns no tier and changes no status.

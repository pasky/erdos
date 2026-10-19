---
name: research/erdos_49/evidence/verify/connections_notation_and_the_inputs_used_review
title: "Independent review of the connections section: Notation and the inputs used"
desc: |
  Refutation-failed for every checked statement of the section (the two
  elementary notation facts, the three transcribed source inputs, Ford's
  theorem with its three consequences, and the explicit totient's eight even
  preimages); one required correction, the symbol C_2 used with two meanings.
created: 2026-09-28T18:13:44Z
updated: 2026-09-28T20:43:42Z
---

***

## Subject and independence

Role: independent reviewer in a fresh context, given only the assignment;
the reviewer took no part in writing the connections page, the
reconstruction pages or any other page of the folder. Charge: refutation
of the author-recorded statements of one section.

Subject: `wiki/research/erdos_49/connections.md` as it stood on
2026-09-28T13:50:48Z, section "Notation and the inputs used", lines 58--111
(from its H2 heading to the line before the H2 "Problem 1004: distinct totients
on a consecutive block"). No lead page is named in the assignment and the
section names none; the two leads linked from the page's introduction were not
read.

Read, and at what depth:

- The section, clause by clause; the page's introduction and Standing
  paragraph (lines 14--57) for the standing convention they set, and the
  list of H2 headings; no other section of the page.
- The six reconstruction pages of the folder in the same state, in full:
  Theorem 3.1, Theorem 3.3, Lemma 3.2, Lemma 4.1, Lemma 5.1, Theorem 1.2.
- Pollack, Pomerance and Treviño (2013): the card's provenance and
  contents, its Theorem 1.2 result page, and the second card's Theorem 3.1
  and Theorem 3.3 result pages (statements); the held 17-page manuscript,
  pp. 2 and 5--10 on the text layer and pp. 6--8 on the page images.
- Ford (1998): the card's digest; the held 43-page copy, p. 2 (Theorem 1
  and the constants (1.3)--(1.6)) on the page image and the text layer.
- Problem 417: the Statement.
- `docs/verification.md` ("Grading and claim standing", "Audit checklist:
  the canonical failure modes", "Whole-claim report", "Audit checklist"),
  `docs/approach_vetting.md`, `docs/evidence.md` ("Source fidelity"),
  `docs/math_authoring.md`.
- An independent enumeration of the preimages of $2^{18}\cdot257$, written
  for this review from the divisor recursion the Lemma 5.1 page describes
  and cross-checked against brute force over $m\le2\cdot10^5$ for every
  totient value up to $3000$; not filed.

Exposures: the Problem 417 page was printed from its top through its
"Progress" section, so its "Current assessment" paragraph (which records no
assessment) and a "Progress" paragraph naming an author-recorded transfer
from another folder were seen; neither bears on this section and neither
was used. The two result pages of the second card carry a "Living
verification: needs review" line, seen. The folder listing showed the file
names under `evidence/verify/` (a grade and six reconstruction reviews);
none was opened. Nothing among the private working files was read and no web search was
made.

## Restatement

Conventions throughout: $\varphi$ is Euler's function; $n$ and $m$ range
over positive integers; $\log_j$ is the $j$-th iterated natural logarithm.

- **S1 (elementary notation facts).** With $V(x)$ the number of totients in
  $[1,x]$, $\mathcal W(x)=\{\varphi(n):n\le x\}$ and $W(x)=\#\mathcal W(x)$
  for real $x$: (a) $W(x)\le V(x)$ for every real $x$; (b) the function
  Problem 417 calls $V'(x)$ is $W(x)$.
- **S2 (definitions by reference).** $P(x;k)$ for natural $k$ splits as
  $P_0(x;k)+P_1(x;k)$, with $P_0$ counting the solutions of the Theorem A
  form and $P_1$ the rest; $c(k)$ is the coefficient (3.2) of the source,
  defined for even $k$; $Z(x)$ is Ford's function, with exponent
  $C(\log_3x-\log_4x)^2+C'\log_3x-(C'+\tfrac12-2C)\log_4x$; and $n$ is
  convenient for a totient $d$ with preimages $n_1,\ldots,n_k$ when
  $d\varphi(n)$ is a totient whose preimages are exactly $n_1n,\ldots,n_kn$.
  These are definitions; what is checkable is their agreement with the
  pages and the source they cite.
- **S3 (T1).** There is an $x_0$ independent of $k$ such that for every
  $x>x_0$ and every natural number $k\le\exp((\log x)^{1/3})$,
  $P_1(x;k)<x/\exp((\log x)^{1/3})$. Standing sentence: a published theorem
  whose proof the source labels a sketch; the reconstruction page records
  the sketch and its one written deduction only.
- **S4 (T3).** Fix a function $\varepsilon(x)>0$ with $\varepsilon(x)\to0$
  and $x^{\varepsilon(x)}\to\infty$. As $x\to\infty$, uniformly over even
  $k$ with $2\le k\le x^{\varepsilon(x)}$,
  $P_0(x;k)\le(16C_2+o(1))c(k)x/(\log x)^2$, with $C_2$ the source's
  twin-prime constant; and for every even $k$,
  $1/(2k)\le c(k)\le3\cdot7^{3+2\omega(k)}\prod_{p\mid k,\,p>2}\frac{p-1}{p-2}\cdot\frac1k$.
  Standing sentence: reconstructed modulo Selberg's sieve as the source
  states it and Evertse's bound inside Lemma 3.2. Further: for every odd
  $k$ and every $x$, $P_0(x;k)=0$.
- **S5 (L4).** For every pair of totients $d_1,d_2$ and every
  $D\ge\max\{d_1,d_2\}$ there are an absolute constant $K\ge1$ (the same
  for all $d_1,d_2,D$), a constant $c_D>0$ and a threshold $x_0(D)$ such
  that for every $x\ge x_0(D)$ at least $c_DZ(x)$ integers $n$ satisfy
  $\varphi(n)\le x/D$, $n$ convenient for $d_1$ and for $d_2$, and
  $n/\varphi(n)\le K$. Standing sentence: a published lemma whose two
  counting steps import Ford's lower-bound argument; the reconstruction is
  partial.
- **S6 (F).** Ford's Theorem 1 gives $V(x)=Z(x)e^{O(1)}$ for large $x$.
  Consequences: (a) there is an absolute $C_1$ with $V(x)\le C_1Z(x)$ for
  all large $x$; (b) for each fixed real $\mu\ge1$,
  $Z(x/\mu)/Z(x)\to1/\mu$ as $x\to\infty$; (c) there is an absolute
  constant (written $C_2$ on the page) such that for each fixed $\mu\ge1$
  there is an $x_2(\mu)$ with $V(x/\mu)\le(C_2/\mu)V(x)$ for all
  $x\ge x_2(\mu)$.
- **S7 (P).** $2^{18}\cdot257=67371008$ is a totient with exactly eight
  preimages, the eight integers listed on the Lemma 5.1 page, and all eight
  are even; the enumeration was repeated for the page by the same divisor
  recursion, and neither run is filed as evidence.

## Checklist

- **Quantifiers and scope.** Pass. S3 carries "absolute $x_0$" and the
  $k$-range as the source states them (p. 6); S4 fixes $\varepsilon$ before
  the uniformity claim and keeps the source's "uniformly in $k$"; S5 keeps
  the order fixed pair, fixed $D$, then constants; S6 states "for large
  $x$", "for each fixed $\mu\ge1$" and a $\mu$-dependent threshold with a
  $\mu$-independent constant; S7 is a finite statement.
- **Circularity.** Pass. The section states inputs and elementary
  consequences; nothing in it is assumed in its own derivation.
- **Model and convention changes.** Fail in one place (F1): the symbol
  $C_2$ names the source's twin-prime constant in S4 and a fresh absolute
  constant in S6, and the section never defines the S4 meaning. The
  conventions $V$, $W$, $V'$ and $Z$ (with $C'$ for Ford's $D$) agree with
  Problem 417, the Theorem 1.2 page and Ford's p. 2.
- **Finite and statistical overreach.** Pass. S7 is used only as a finite
  fact about one totient, and the section draws no infinite conclusion
  from it.
- **Uniformity.** Pass. In S6(c) the constant is absolute and the threshold
  depends on $\mu$, as re-derived below; in S5 the constants may be labeled
  by $D$ alone (W3); in S3 and S4 the uniformity is the source's.
- **Extremal conclusions.** Inapplicable. The section asserts no infimum,
  supremum or sharpness; the least and greatest preimages belong to the
  Lemma 5.1 page, which this review consumes as a premise.
- **Consequences and composition.** Pass with a remark (F2): the "hence"
  of S6(c) also consumes the lower half of Ford's $e^{O(1)}$, which the
  quoted theorem supplies but the "two consequences" sentence does not
  list.
- **Computation.** Pass. $2^{18}\cdot257=67371008$; the eight preimages
  were re-enumerated independently, each was checked by evaluating
  $\varphi$, and all are divisible by $4$.
- **Reproduction.** Pass. The section states no rerun command; its one
  computational claim (S7) was reproduced from the stated method with a
  cross-check that would have failed on a missed or spurious preimage.
- **Source and verdict fidelity.** Pass. S3, S4 and S5 match the source
  word for word in their hypotheses and bounds (pp. 6--8 on the page
  images); S6's quotation matches Ford's Theorem 1 (p. 2); the definition
  of convenient matches the source's p. 2; each standing sentence matches
  the Standing paragraph of the reconstruction page it describes; the
  Problem 417 notation matches that page's Statement.

## Weakest steps

**W1: the limit $Z(x/\mu)/Z(x)\to1/\mu$ (S6(b)).** Write
$Z(x)=(x/\log x)\exp E(x)$ with
$E(x)=C(\log_3x-\log_4x)^2+C'\log_3x-(C'+\tfrac12-2C)\log_4x$. Then

$$
\frac{Z(x/\mu)}{Z(x)}=\frac1\mu\cdot\frac{\log x}{\log x-\log\mu}\cdot
\exp\bigl(E(x/\mu)-E(x)\bigr),
$$

and the middle factor tends to $1$. For the exponent, put
$\delta_2=\log_2(x/\mu)-\log_2x=\log(1-\log\mu/\log x)=O(1/\log x)$; then
$\delta_3=\log_3(x/\mu)-\log_3x=\log(1+\delta_2/\log_2x)=O(1/(\log x\log_2x))$
and
$\delta_4=\log_4(x/\mu)-\log_4x=\log(1+\delta_3/\log_3x)=O(\delta_3/\log_3x)$.
With $a=\log_3x-\log_4x$ and $\delta=\delta_3-\delta_4$, the square changes
by $2a\delta+\delta^2=O(\log_3x/(\log x\log_2x))\to0$, and the two linear
terms change by $O(\delta_3)+O(\delta_4)\to0$. So $E(x/\mu)-E(x)\to0$ and
the limit is $1/\mu$. The page's justification ("whose change under
$x\mapsto x/\mu$ tends to $0$") names the conclusion rather than this
estimate; the estimate is what is needed, because $a\to\infty$, so a
change of the arguments that is merely $o(1)$ would not suffice.

**W2: the deduction $V(x/\mu)\le(C_2/\mu)V(x)$ (S6(c)).** From Ford,
$c_0Z(x)\le V(x)\le C_1Z(x)$ for $x\ge x_1$ with absolute $c_0,C_1>0$. For
$x\ge\mu x_1$ and large enough that $Z(x/\mu)\le2Z(x)/\mu$ (W1),

$$
V(x/\mu)\le C_1Z(x/\mu)\le\frac{2C_1}{\mu}Z(x)\le\frac{2C_1}{c_0\mu}V(x),
$$

so the constant $2C_1/c_0$ is absolute and only the threshold depends on
$\mu$. The lower bound $c_0Z(x)\le V(x)$ is indispensable: without it the
chain ends at $Z(x)$, not at $V(x)$. It is available from the quoted
$V(x)=Z(x)e^{O(1)}$, which is two-sided, but it is not one of the "two
consequences" the page lists (F2).

**W3: the labeling $c_D$, $x_0(D)$ in S5.** The source writes $\gg_D$, and
the Lemma 4.1 page warns that the constants may also depend on $d_1,d_2$.
The section's labeling is nevertheless correct as stated: for fixed $D$ the
pairs of totients $d_1,d_2\le D$ are finitely many, so the minimum of the
per-pair constants and the maximum of the per-pair thresholds depend on
$D$ alone and serve every pair at once. The clause $K\ge1$ follows from
$n/\varphi(n)\ge1$ on the set of $n$ the lemma supplies, which is nonempty
for $x\ge x_0(D)$ because $c_DZ(x)>0$. Neither remark is used elsewhere in
the section.

## Strongest attack

- **S1.** Attack: find a real $x$ with $W(x)>V(x)$, or a mismatch with
  Problem 417's symbols. Failed: every $\varphi(n)$ with $n\le x$ is a
  totient at most $n\le x$, so $\mathcal W(x)\subseteq\mathcal V\cap[1,x]$;
  Problem 417 defines $V'(x)=\#\{\varphi(m):1\le m\le x\}$, which is $W(x)$
  literally, and its $V(x)$ is the section's.
- **S2.** Attack: a definition that differs from its cited page or from
  the source. Failed: the split and $c(k)$ are those of the Theorem 3.3
  page and of the source's (3.2); $Z(x)$ is that of the Theorem 1.2 page,
  which is the source's p. 7 display with $C'$ where Ford writes $D$, both
  $2.17696874\ldots$; "convenient" is the source's p. 2 definition
  ("$n_1n,\ldots,n_kn$ and no others"). Residual: the letter $k$ counts
  preimages here and is the shift elsewhere (F4, note).
- **S3.** Attack: a strengthened quantifier, a changed exponent or range.
  Failed: the source's Theorem 3.1 (p. 6) reads "For $x>x_0$, we have
  $P_1(x;k)<x/\exp((\log x)^{1/3})$, uniformly for natural numbers
  $k\le\exp((\log x)^{1/3})$"; the section's "absolute $x_0$" is what
  "uniformly" means. Second attack: the standing sentence claims a
  reconstruction that does not exist. Failed: it says the opposite, and it
  matches the Theorem 3.1 page. Residual: that page also records a gap in
  the source's sketch (F3, note).
- **S4.** Attack: a wrong constant or range in the transcription. Failed
  for the bound, the range and the two-sided estimate of $c(k)$ (p. 6, page
  image). Attack on the odd-$k$ clause: exhibit odd $k$ and $j$ with
  $\gamma(j)=\gamma(j+k)$. Failed: $j$ and $j+k$ have opposite parity, so
  exactly one is even and their prime supports differ; hence no solution
  has the Theorem A form and $P_0(x;k)=0$. Attack on the symbol: $C_2$ is
  used before it is defined and is redefined in S6 (F1).
- **S5.** Attack: the section drops a dependence (on $d_1,d_2$) or invents
  one ($K\ge1$). Failed by W3.
- **S6.** Attack on (b): choose $\mu$ so that the exponent's change does
  not vanish. Failed: the change is $O(\log_3x/(\log x\log_2x))$ for every
  fixed $\mu$ (W1). Attack on (c): make the constant depend on $\mu$.
  Failed: W2 gives the absolute constant $2C_1/c_0$. Attack on the stated
  inputs: derive (c) from (a) and (b) alone. This succeeds only in showing
  that a third input, the lower half of Ford's theorem, is consumed (F2);
  the page quotes that theorem two-sided, so the conclusion stands.
- **S7.** Attack: a ninth preimage, or an odd one. Failed: the independent
  recursion over the primes $p$ with $p-1\mid67371008$ returns exactly the
  eight listed integers, each with $\varphi$ equal to $67371008$ and each
  divisible by $4$; on all totient values up to $3000$ the same recursion
  agrees with brute force over $m\le2\cdot10^5$, and the base case that
  adjoins $2m$ to an odd preimage $m$ was exercised there. By hand: an odd
  preimage would need $257^2$ in it and $2^{10}$ from the Fermat primes
  below $257$, which supply at most $2\cdot4\cdot16=2^7$; so none exists.

## Premises

- [[research/erdos_49/theorem_3_1_reconstruction|Theorem 3.1 reconstruction]]:
  interface, the statement of S3 and the standing "record of a sketch";
  read in full.
- [[research/erdos_49/theorem_3_3_reconstruction|Theorem 3.3 reconstruction]]:
  interface, Theorem A, the split $P_0+P_1$, $c(k)$ for even $k$, $C_2$,
  the statement of S4 and its standing; read in full.
- [[research/erdos_49/lemma_3_2_reconstruction|Lemma 3.2 reconstruction]]:
  interface, the count $3\cdot7^{3+2\omega(k)}$ behind the upper bound on
  $c(k)$; read in full.
- [[research/erdos_49/lemma_4_1_reconstruction|Lemma 4.1 reconstruction]]:
  interface, the statement of S5 with its caveat on the constants and its
  standing "partial"; read in full.
- [[research/erdos_49/lemma_5_1_reconstruction|Lemma 5.1 reconstruction]]:
  interface, the definition of convenient and the enumeration of the
  preimages of $d_1$ and $d_2$; read in full.
- [[research/erdos_49/theorem_1_2_reconstruction|Theorem 1.2 reconstruction]]:
  interface, the definition of $Z(x)$ and step 2 (odd $k$); read in full.
- [[../library/primes/pollack_et_al_2013_sets_monotonicity_euler_totient_function/_index|Pollack, Pomerance and Treviño (2013)]]:
  held, the 17-page author manuscript; p. 2 (convenient), p. 6 (Theorems
  3.1 and 3.3, Lemma 3.2, Remark 3.1), p. 7 (proof of Theorem 3.3; Ford's
  order of magnitude and $Z(x)$), p. 8 (constants (4.1)--(4.2), Lemma 4.1),
  pp. 9--10 (Lemma 5.1, proof of Theorem 1.2), on the text layer, with
  pp. 6--8 also on the page images.
- [[../library/arithmetic_functions/ford_1998_distribution_totients/_index|Ford (1998)]]:
  held, a 43-page copy whose acknowledgment records a corrected
  lower-bound proof; interface used, Theorem 1 with (1.3)--(1.6): p. 2 on
  the page image and the text layer, nothing else read.
- [[problems/arithmetic_functions/E0417/_index|Problem 417]]: Statement only.
- No local claim card is consumed; the section carries no `depends_on`.

## Findings

- **F1 (required).** Location: "(T3) ...
  $P_0(x;k)\le(16C_2+o(1))c(k)x/(\log x)^2$" and "(F) ... hence
  $V(x/\mu)\le(C_2/\mu)V(x)$ for $x\ge x_2(\mu)$ with an absolute $C_2$".
  Defect: one symbol, two constants. In (T3) $C_2$ is the source's
  twin-prime constant $2\prod_{p>2}(1-(p-1)^{-2})=1.32\ldots$, which the
  section never defines; in (F) "an absolute $C_2$" introduces a different
  constant. Read with the (T3) meaning, the (F) inequality becomes the
  unproved numerical claim $V(x/\mu)\le(1.32\ldots/\mu)V(x)$; read with the
  (F) meaning, the (T3) bound loses its constant. Witness: the two displays
  quoted. Replacement: in (T3) add "where $C_2=2\prod_{p>2}(1-(p-1)^{-2})$
  is the twin-prime constant in the source's normalization (Theorem 3.3
  page)", and in (F) rename the constant, for instance to $C_3$, carrying
  the rename to every later use on the page.
- **F2 (suggested).** Location: "(F) ... Two consequences are used: ...;
  hence $V(x/\mu)\le(C_2/\mu)V(x)$". Defect: the "hence" consumes a third
  fact, $Z(x)\le c_0^{-1}V(x)$ for large $x$ (the lower half of Ford's
  $e^{O(1)}$), which the quoted theorem supplies but the sentence does not
  list; and the reason given for $Z(x/\mu)/Z(x)\to1/\mu$ states the
  conclusion about the exponent rather than the estimate that proves it.
  Witness: W1 and W2. Replacement: "Three consequences are used: absolute
  $c_0,C_1$ with $c_0Z(x)\le V(x)\le C_1Z(x)$ for large $x$; and for each
  fixed $\mu\ge1$, $Z(x/\mu)/Z(x)\to1/\mu$, because $\log(x/\mu)\sim\log x$
  and $\log_3(x/\mu)-\log_3x=O(1/(\log x\log_2x))$, so the exponent of $Z$,
  whose leading term is $C(\log_3x-\log_4x)^2$, changes by
  $O(\log_3x/(\log x\log_2x))\to0$; hence ...".
- **F3 (note).** Location: "(T1) ... the reconstruction records the sketch
  and its one written deduction only." The Theorem 3.1 page also records
  that the source's sketch does not dispose of the solutions with $p\mid m$
  (for $k=2$: $n=4,8,32$), which $P_1(x;k)$ counts. The sentence is
  accurate, and the page consumes the theorem as published, but a consumer
  weighing (T1) would want the recorded gap named here.
- **F4 (note).** Location: "convenient for a totient $d$ with preimages
  $n_1,\ldots,n_k$". The letter $k$ is the shift everywhere else in the
  section. Harmless, and the Lemma 5.1 page and the source's p. 2 use the
  same letter; "$n_1,\ldots,n_r$" would remove the overload.

## Verdict

- S1 (elementary notation facts): refutation-failed.
- S2 (definitions by reference): not a claim; each definition agrees with
  its cited page and with the source.
- S3 (T1, transcription and standing sentence): refutation-failed.
- S4 (T3, transcription, $c(k)$ bounds, standing sentence, odd $k$):
  refutation-failed; F1 required, a rename and a definition, with no change
  to the mathematics.
- S5 (L4, transcription with $K\ge1$ and standing sentence):
  refutation-failed.
- S6 (Ford's theorem and its three consequences): refutation-failed; F2
  suggested.
- S7 (the eight even preimages): refutation-failed.

Limitations. The proofs of Theorems 3.1 and 3.3 and of Lemma 4.1 were not
re-examined: the section consumes them as published results at the scope
the reconstruction pages record, and those pages are premises of this
review. Ford's Theorem 1 was checked as a statement against the held copy;
its proof was not read. The enumeration behind S7 is the reviewer's own
run of the same method, not a filed evidence record. Whether the later
sections of the page use $C_2$ in one sense or both was not examined,
since those sections lie outside this review's read set.

This focused review assigns no tier and changes no status.

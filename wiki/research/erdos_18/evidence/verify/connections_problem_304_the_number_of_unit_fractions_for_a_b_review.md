---
name: research/erdos_18/evidence/verify/connections_problem_304_the_number_of_unit_fractions_for_a_b_review
title: "Independent review of the connections section: Problem 304: the number of unit fractions for a/b"
desc: |
  Refutation review of the Problem 304 section and the factorial unit-fraction
  lead as of 2026-09-28T13:50:48Z: Lemma C, Lemma C', (304.1), (304.2), (304.3),
  the reduction, the factorial obstruction and the lead's (293.1) survive
  (refutation-failed); the extension-chain obstruction consumes Lemma D at an
  interface that is false without a fixed-seed hypothesis (proof defective;
  statement unresolved). One required correction, one suggested, five notes.
created: 2026-09-28T17:56:46Z
updated: 2026-09-28T20:40:17Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context, given only the review
assignment; the reviewer took no part in writing the connections page, the
lead page, the reconstruction pages or the library cards, and had read none of
them before this assignment. Charge: refutation.

**Frozen subject.** The repository as it stood at 2026-09-28T13:50:48Z (the
default branch's state at the time of review; the worktree used was checked out
at that state and its tree was unchanged while the subject was read). Page
`wiki/research/erdos_18/connections.md`, section
"## Problem 304: the number of unit fractions for a/b", lines 244–344 (the H2
at line 244 through the line before the next H2 at line 345). Lead page
`wiki/research/leads/factorial_unit_fraction_transfer/_index.md`, whole page.

**Read, and at what depth.** The section and the lead page in full. On the
connections page: the frontmatter, preamble and Conventions (lines 1–46) and
the Shared lemmas section (lines 47–243, Lemmas A, B, C, C′ and D) as inputs.
The proofs of the shared lemmas belong to another reviewer; their interfaces
were confirmed at each use, and the proofs of Lemma C, Lemma C′ and the
consumed Lemma 3.1 were nevertheless re-derived in full because the lead rests
on them. Lemma D's proof was read to locate the source of the interface defect
reported below. The page's closing section "Sources read for this page" (lines
794–804) was read as the inputs listing. Reconstruction pages as of the same
time, treated as premises at their recorded standing:
`hughes_lemma_4_reconstruction.md`, `hughes_theorem_1_reconstruction.md`,
`hughes_corollary_3_reconstruction.md`, `hughes_remark_6_reconstruction.md`,
`doorn_lemma_3_1_reconstruction.md` and
`doorn_proposition_4_1_reconstruction.md`, all read whole; Lemma 3.1 was
re-derived, Remark 6's counting was re-derived in outline, and Theorem 1,
Corollary 3 and Proposition 4.1 were read for their statements and interfaces
only. Problem pages: the Statement and Formulation paragraphs of
`wiki/problems/unit_fractions/E0304/_index.md`,
`wiki/problems/unit_fractions/E0293/_index.md` and
`wiki/problems/divisors/E0018/_index.md`, nothing else on them. Library: the
provenance paragraphs and "The statement verified" paragraph of the JenW1N
card and the Source, Statement and Formal statement of its `target` page; the
provenance paragraph and generated link rows of the van Doorn (2026) card and
the Source and Statement of its `theorem_1_2` page; the Statement and Source of
the van Doorn–Tang `theorem_1_1` page. Held PDFs: the van Doorn (2026) note
(its SHA-256 matches the card), pp. 1 and 6 read on page images and the whole
text layer; the van Doorn–Tang paper, p. 2 read on the page image and pp. 1–3
in the text layer. Wiki guidance: `docs/verification.md` sections "Report
contract", "Grading and claim standing" and "Erdos-specific" (which holds
"Whole-claim report" and "Audit checklist"), `docs/evidence.md` "Source
fidelity", `docs/approach_vetting.md` and `docs/math_authoring.md`.

**Exposures.** Three, none used: (1) a grep for bold labels on the three
problem pages printed the first line of each page's Status paragraph (E0304
line 33, E0293 line 39, E0018 line 31), which is status text outside the read
set; (2) listing the target directory of this report showed the file names of
other reviews and of a grade file under `evidence/verify/`, none of which was
opened; (3) the Formulation paragraphs of E0304 and E0293, which qualify the
statements (no coprimality condition; the reading $m>1$ of "minimal integer"),
were read together with the statements. Nothing under any `evidence/` folder,
no Current assessment, Known results or acceptance text, no folder
`_index.md`, no other section's review, nothing outside the repository and no
web search was used. The Target paragraph's account of the Problem 304 page's
Current assessment is therefore reported as unverified, not as checked.

## Restatement

**Conventions.** For practical $N$, $h(N)$ is the least $k$ such that every
integer $1\le m\le N$ is a sum of at most $k$ distinct divisors of $N$, a fresh
set for each $m$. For integers $1\le a<b$, $N(a,b)$ is the least number of
distinct unit fractions with denominators above $1$ summing to $a/b$, and
$N(b)=\max_{1\le a<b}N(a,b)$. $D_k$ is the set of denominators occurring in
some $1=1/n_1+\cdots+1/n_k$ with $1\le n_1<\cdots<n_k$, and
$v(k)=\min\{m>1:m\notin D_k\}$. Logarithms are natural. These are the page's
conventions. They agree with the Statement of Problem 304 (whose maximum runs
over all $1\le a<b$ with no coprimality condition), with the reading of
Problem 293 recorded in its Formulation, and, for $h$, with the formal
statement described on the accepted target page, a supremum over $1\le m\le n$
of the least size of a divisor set having $m$ among its subset sums, which is
the same number since a minimal such set sums to $m$ exactly.

**S1 (Lemma C, the transfer).** For all integers $n\ge b\ge2$ with $n$
practical and every integer $1\le a<b$: $a/b$ is a sum of at most $2h(n)$
distinct unit fractions with denominators above $1$; each denominator either
divides $n$ (so is at most $n$) or is $bn/e$ for a divisor $e$ of $n$ and
exceeds $n$; and if $b\nmid n$ then no denominator equals $b$. In particular
$N(b)\le2h(n)$ for every practical $n\ge b$.

**S2 (Lemma C′).** For every sufficiently large integer $b$: let $n$ be the
least integer with $n!\ge b$ and $p$ the least prime not dividing $n$; put
$N=n!$ if $b\nmid n!$, and $N=p^{j}(n-1)!$ with $j=\lceil\log n/\log p\rceil$
if $b\mid n!$. Then $N$ is practical, $N\ge b$, $b\nmid N$, and
$h(N)\le\max\bigl(h(n!),\,h((n-1)!)+\lceil\log_2n\rceil\bigr)$.

**S3 ((304.1), conditional).** Premise: for every $\varepsilon>0$ there is
$n_0(\varepsilon)$ with $h(n!)<n^{\varepsilon}$ for all $n\ge n_0(\varepsilon)$
(the accepted formal statement, consumed at its recorded standing).
Conclusion: for every $\varepsilon>0$ there is $b_0(\varepsilon)$ such that
$N(b)\le2(\log b)^{\varepsilon}$ for every integer $b\ge b_0(\varepsilon)$; the
thresholds are ineffective. Side sentences: the bound is below Vose's
$\ll\sqrt{\log b}$ for every $\varepsilon<1/2$; the transfer is uniform in
$a$; "for all large $b$" follows from "for all large $n$" because $n$ is
nondecreasing in $b$; the site's $m<N$ convention only lowers $h$; and Lemma C
uses only representations of integers at most $n-1$.

**S4 ((304.2), conditional).** Premise: Theorem 1 of the Hughes
reconstruction, $h(n!)\le(2\log2+o(1))\,n/\log n$. Conclusion:
$N(b)\le(4\log2+o(1))\log b/(\log\log b)^2$ as $b\to\infty$; this is smaller
than Erdős's 1950 bound $\ll\log b/\log\log b$ by a factor $\log\log b$ and
larger than Vose's.

**S5 ((304.3), claimed).** Premise: Proposition 4.1 of the van Doorn
reconstruction, at its standing *claimed*. Conclusion: for every integer
$b\ge x_0$, $N(b)\le2c_0(\log\log b)^2-2$ with $c_0=14/\log2$, which implies
the note's Theorem 1.2.

**S6 (reduction).** For $b\ge2$,
$N(b)\le2\min\{h(N):N\ \text{practical},\ N\ge b\}$; hence if for every large
$b$ there is a practical $N$ with $b\le N\le\exp((\log b)^{C})$ and
$h(N)\le C'\log\log N$ for absolute $C,C'$, then $N(b)\ll\log\log b$.

**S7 (factorial obstruction).** Since $h(n!)\ge c(\log n)^2$ for all large $n$
(Remark 6), every bound obtained by applying S1 with $N=n!\ge b$ has
$2h(n!)\gg(\log\log b)^2$; so no bound on $h(n!)$, however sharp, yields
$N(b)=o((\log\log b)^2)$ through Lemma C.

**S8 (extension-chain obstruction, as written).** "Lemma D shows that every
certificate built from Lemma 3.1 extensions is at least
$(1/(2\log2)-o(1))(\log\log N)^2$." Read with the consumed Lemma D: for every
chain $n_0$ practical, $n_{j+1}=A_jn_j$ ($0\le j<J$), each step certified by
Lemma 3.1 at cost $L_j$, one has
$\sum_{j<J}L_j\ge(1/(2\log2)-o(1))(\log\log n_J)^2$ with an $o(1)$ that tends
to $0$ as $n_J\to\infty$ uniformly over all such chains; hence the certified
bound $h(n_0)+\sum_jL_j$ on $h(n_J)$ is never below that quantity.

**S9 (consequence sentences).** Both reconstructed mechanisms stop at exponent
$2$ for this target, and the exponent, not the factor $2$ of Lemma C, is the
obstruction; a bound $h(N)\ll(\log\log N)^2$ along a sequence reaching every
scale leaves the conjecture open by a factor $\log\log b$; a positive answer
to the exponent-one question (for every large $b$, a practical
$N\in[b,\exp((\log b)^{O(1)})]$ with $h(N)\ll\log\log N$) proves the
conjecture through Lemma C; Lemma D and Remark 6 show that neither mechanism
of the folder can supply such $N$, so a new certificate of practicality is
needed.

**S10 (lead, (293.1), conditional on the premise of S3).** For every
$\varepsilon>0$ there is $k_0(\varepsilon)$ with
$v(k)\ge\exp((k/5)^{1/\varepsilon})$ for all $k\ge k_0(\varepsilon)$; hence
$v(k)\ge\exp(k^{A})$ for every fixed $A>0$ and all large $k$. Route: S2 and S1
write $(b-1)/b$ as at most $2h(N)\le4n^{\varepsilon}$ distinct unit fractions
with denominators above $1$, none equal to $b$; adjoining $1/b$ gives a
decomposition of $1$ containing $b$; the nesting $D_k\subseteq D_{k+1}$
($k\ge2$) and $v(k)\to\infty$ finish.

**S11 (standing and input sentences, section and lead).** The inputs are part
(b) at the standing of the site acceptance, Lemma C, Lemma C′ (consuming
Lemma 3.1 as an elementary argument, not on the note's authority), Lemma A,
and the refereed nesting lemma; nothing on the lead depends on the claimed
van Doorn chain; there is no gap inside the deduction; both target questions
are the exact site questions; (304.1) "is the first consequence of the
accepted part (b) outside Problem 18"; and the standing of (304.1) "is that of
part (b)".

## Checklist

- **Quantifiers and scope.** S1–S7, S10: pass. Every "for all large" is an
  existential threshold in the right order (for every $\varepsilon$ there is a
  threshold, then for all $b$ beyond it); S3 is uniform in $a$ because S1 is.
  S8: fail. The sentence quantifies over every Lemma 3.1 certificate, and the
  consumed Lemma D statement makes its $o(1)$ uniform over all chains; a
  one-step chain from a large factorial seed violates it (Finding F1). S9's
  "neither mechanism of this folder" passes when read at the folder's two
  mechanisms (factorials; the note's chain from a seed bounded independently
  of the scale), which is the reading F6 asks to be written.
- **Circularity.** Pass. No statement uses its own conclusion; the premises
  (part (b), Theorem 1, Proposition 4.1, Remark 6, Lemma D) are external to
  the deductions that consume them, and the reduction S6 is stated as a
  sufficient condition, not as a proof of the conjecture.
- **Model and convention changes.** Pass. The $h$ transported is the fresh-set
  $h$ over $1\le m\le n$, which is the note's $h$, the reconstruction pages'
  $h$ and the formal `practicalH` described on the target page; S1 needs only
  representations of integers at most $n-1$, so it also holds under the site's
  $m<N$ convention. The note's $N(a,b)$ omits "denominators above $1$", but
  $a/b<1$ excludes the denominator $1$, so the note's, the page's and the
  problem's definitions agree. Problem 293 is consumed under the $m>1$ reading
  that its Formulation records, not under the defective literal wording (F7).
- **Finite and statistical overreach.** Inapplicable, except that the numeric
  threshold $n\ge14$ in S3 was re-derived ($n\ge10$ already suffices).
- **Uniformity.** S3: pass (uniform in $a$; ineffective in $b$ and said so on
  the lead). S4: pass (the $o(1)$ is Theorem 1's, uniform in $m$). S5: pass
  ($x_0$ independent of $p_*$ on the Proposition 4.1 page). S8: fail (F1: the
  floor is uniform only over chains with a bounded seed, or after subtracting
  $(\log\log n_0)^2$).
- **Extremal conclusions.** Pass. The minimum in S6 is over positive integers
  and is attained; the maximum defining $N(b)$ is over finitely many $a$ and
  is bounded uniformly by S1; no sharpness is claimed.
- **Consequences and composition.** S3, S4 and S5 inherit and state the
  standing of their premises; S6, S7 and the Lemma C clauses of S9 were
  re-derived; S8's "hence" clause is exactly the defect of F1; S5's "which is
  the note's Theorem 1.2" is an implication of a bound stronger by $2$ (F4);
  S2 consumes Lemma 3.1 within its hypotheses (W1); S10 consumes the nesting
  lemma at $k\ge2$ and $v(k)\to\infty$ at every $k$, both within the refereed
  statements. The priority sentence and the "standing is that of part (b)"
  sentence are consequence surfaces that overreach slightly (F2, F5).
- **Computation.** Pass; nothing beyond arithmetic. Re-derived: $4\log2$ in
  S4; the threshold $n\ge14$ in S3; $\log n\ge\tfrac12\log\log b$ whenever
  $n!\ge b$ and $n\ge3$ (S7); $(k/5)^{1/\varepsilon}\ge k^{A}$ for
  $\varepsilon=1/(2A)$ and $k\ge25$ (S10); $c_0/(1/(2\log2))\approx28$ as
  quoted in the Lemma D commentary.
- **Reproduction.** Inapplicable; the subject carries no rerun commands or
  coverage claims.
- **Source and verdict fidelity.** Pass for everything checkable in this
  remit: Lemma C matches Lemma 5.1 of the note in statement and proof (p. 6,
  page image); the recorded Theorem 1.2 matches p. 1; Erdős's 1950 bound as
  quoted in S4 matches the note's p. 1; the nesting lemma ($k\ge2$) and
  Theorem 1.1 ($v(k)\ge e^{ck^2}$ for all $k\ge1$) match van Doorn–Tang p. 2;
  the accepted statement matches the target page's Statement and Formal
  statement; the acceptance facts quoted on the lead match the card's
  provenance paragraph. Not checkable here: the Target paragraph's account of
  the problem page's Current assessment (excluded reading) and the priority
  sentence "first consequence" (F2).

## Weakest steps

**W1 (S2: the prescribed-denominator step and the Lemma 3.1 interface).**
Case $b\mid n!$. The prime $p$ exists with $p\le n-1$ for $n\ge3$: if every
prime up to $n-1$ divided $n$, their product would divide $n$, but that
product exceeds $n$ for $n\ge4$, and for $n=3$ the prime $2$ does not divide
$3$. Since $j\ge\log n/\log p$, $p^{j}\ge n$ and $N=p^{j}(n-1)!\ge n!\ge b$.
For $0\le i<j$ put $n'=p^{i}(n-1)!$, practical by induction from Lemma A
($(n-1)!$ is a factorial). Lemma 3.1 with $A=p$ and $L=1$ needs every residue
modulo $p$ to be a sum of at most one divisor of $n'$, not divisible by $p$,
with total at most $n'$: the residue $0$ is the empty sum, and a residue
$1\le c\le p-1\le n-2$ is the divisor $c$ of $(n-1)!$, hence of $n'$, with
$p\nmid c$ and $c<n'$. So $pn'$ is practical with $h(pn')\le h(n')+1$, and
after $j$ steps $h(N)\le h((n-1)!)+j\le h((n-1)!)+\lceil\log_2n\rceil$ because
$p\ge2$. If $b\mid N$ then, with $b\mid n!$,
$b\mid\gcd\bigl(n\,(n-1)!,\,p^{j}(n-1)!\bigr)=(n-1)!\gcd(n,p^{j})=(n-1)!$
since $p\nmid n$, so $b\le(n-1)!<b$ by the minimality of $n$, a
contradiction. Lemma 3.1 itself was re-derived: for $n'<m<pn'$ choose the
prescribed $s\equiv m\pmod p$ with $0\le s\le n'$; then $(m-s)/p$ is an
integer in $[1,n'-1]$, a sum of at most $h(n')$ distinct divisors $e_i$ of
$n'$; the $pe_i$ divide $pn'$, are divisible by $p$ and so are disjoint from
the summands of $s$; the cases $m\le n'$ and $m=pn'$ are immediate.

**W2 (S3: from $n!\ge b>(n-1)!$ to $n<\log b$, and the threshold).** For
$m\ge1$, $\log m!=\sum_{k\le m}\log k\ge\int_1^m\log t\,dt=m\log m-m+1$, so
$\log b>\log(n-1)!>(n-1)(\log(n-1)-1)$, and $(n-1)(\log(n-1)-1)>n$ is the
inequality $\log(n-1)>2+1/(n-1)$, true for $n\ge10$ ($\log9=2.197>2.111$) and
in particular for the page's $n\ge14$. With $N=n!$ in S1 the representations
needed are of $q\le n!-1$ and $r\le b-1\le n!-1$, inside the range of the
accepted statement, so for every $a$
$N(a,b)\le2h(n!)<2n^{\varepsilon}<2(\log b)^{\varepsilon}$ once
$n\ge\max(n_0(\varepsilon),10)$, which $b>\max(n_0-1,9)!$ guarantees because
$n$ is nondecreasing in $b$ and $(n-1)!<b$ forces $n\ge n_0$ when
$b>(n_0-1)!$. The page's "once $b>(n_0-1)!$" omits the second requirement
(F3), which "for large $b$" absorbs.

**W3 (S7 and S8: the two obstructions).** For S7: if $n!\ge b$ and $n\ge3$
then $\log b\le\log n!\le n\log n$, so
$\log\log b\le\log n+\log\log n\le2\log n$, and Remark 6 gives
$2h(n!)\ge2c(\log n)^2\ge(c/2)(\log\log b)^2$ for every factorial $N=n!\ge b$
with $n$ large; since $n\to\infty$ with $b$, the bound $N(b)\le2h(n!)$ is
never $o((\log\log b)^2)$. For S8 the consumed Lemma D was re-derived: the
first inequality $L_j\ge\log A_j/\log(\tau(n_j)+1)$ holds because distinct
residues need distinct representing subsets and
$\sum_{i\le L}\binom Ti\le(T+1)^{L}$; the second, through Wigert's bound and
the left Riemann sum of the decreasing $\log\ell/\ell$, gives, for every
$\eta>0$ and every chain,

$$
\sum_{j<J}L_j\ \ge\ \frac{(\log\log n_J)^2-(\log\log n_0)^2}{2(\log2+\eta)}
-C(\eta),
$$

with $C(\eta)$ independent of the chain. This is the floor
$(1/(2\log2)-o(1))(\log\log n_J)^2$ exactly when $(\log\log n_0)^2$ is
$o((\log\log n_J)^2)$, in particular for a seed bounded independently of the
scale, which the chain of the note has ($n_0\le2^{E}(2Q(k_0))^{k_0}$ on the
Proposition 4.1 page). Lemma D's proof drops the $(\log\log n_0)^2$ term in
the case $j(\eta)=0$ as if it were $O_\eta(1)$; it is not, and the stated
uniformity over all chains fails (F1).

## Strongest attack

**S1.** Attempts: make two denominators coincide (within the first group the
$n/d_i$ are distinct because the $d_i$ are; within the second the $bn/e_j$
are distinct because the $e_j$ are; across groups the first are at most $n$
and the second exceed $n$ because $e_j\le r<b$); produce the denominator $1$
(needs $d_i=n$, but $d_i\le q\le an/b<n$); make $bn/e_j$ non-integral
($e_j\mid n$); push $r$ outside the range of $h(n)$ ($r\le b-1\le n-1$);
defeat the last clause with $b=n$ (then $b\mid n$ and nothing is claimed).
Every attempt fails; the lemma matches Lemma 5.1 of the note line for line.

**S2.** Attempts: force $b\mid N$ in the second case (defeated by the gcd
computation in W1); break the residue hypothesis of Lemma 3.1 (defeated in
W1); make $p$ exceed $n-1$ (impossible for $n\ge3$); make $N<b$ ($p^{j}\ge n$
forbids it); make $j$ exceed $\lceil\log_2n\rceil$ ($p\ge2$ forbids it). All
fail.

**S3.** Attempts: a mismatch between the accepted $h$ and the $h$ of Lemma C
(both are the fresh-set supremum over $1\le m\le n!$; Lemma C uses $m\le n!-1$
only); a wrong direction in the strict inequality
($N(b)\le2h(n!)<2n^{\varepsilon}$); a threshold gap (F3, absorbed by "for
large $b$"); a dependence of the bound on $a$ (none: S1 is uniform in $a$).
All fail. The conclusion stays conditional on the premise and the section
says so.

**S4.** Attempt: the asymptotic $n/\log n=(1+o(1))\log b/(\log\log b)^2$.
From $(n-1)!<b\le n!$ and Stirling in the weak form, $\log b=(1+o(1))n\log n$,
so $\log\log b=\log n+\log\log n+o(1)=(1+o(1))\log n$ and
$n=(1+o(1))\log b/\log\log b$, whence the claim. Fails.

**S5.** Attempt: an interface mismatch with Proposition 4.1. Its page states
$E\ge4$, $x_0>e^{e}$, every real $x\ge x_0$ and every odd prime $p_*$, a
practical $n$ with $x\le n<x^2$, $p_*\nmid n$ and
$h(n)\le c_0(\log\log x)^2-1$, with $x_0$ independent of $p_*$. At $x=b$, an
integer at least $x_0>15$, Lemma C applies with $n\ge b\ge2$ and gives
$N(b)\le2c_0(\log\log b)^2-2$, which implies the note's
$N(b)\le2c_0(\log\log b)^2$. Fails; the standing *claimed* is carried.

**S6.** Attempt: the window. If $b\le N\le\exp((\log b)^{C})$ then
$\log\log N\le C\log\log b$, so $h(N)\le C'\log\log N$ gives
$N(b)\le2CC'\log\log b$. Fails.

**S7.** Attempts: choose $n!$ far above $b$ (then $(\log n)^2$ only grows);
choose $n$ small (impossible, $n\to\infty$ with $b$); dispute
$\log n\gg\log\log b$ (W3 gives $\log n\ge\tfrac12\log\log b$). All fail.

**S8.** The attack succeeds against the sentence as written. Witness: for
$m\ge3$ let $n_0=m!$ (practical by Lemma A), $J=1$, $A_0=2$, $L_0=1$. The
residue $1$ modulo $2$ is the divisor $1$ of $m!$, odd, with total $1\le m!$,
and the residue $0$ is the empty sum, so Lemma 3.1 certifies $n_1=2\cdot m!$
practical with $h(n_1)\le h(m!)+1$. Here $\sum_jL_j=1$ and
$\sum_j\log A_j/\log(\tau(n_j)+1)<1$, while
$(1/(2\log2))(\log\log n_1)^2$ exceeds $25$ at $m=100$ and tends to infinity
with $m$. So the displayed inequality of the consumed Lemma D fails for every
large $m$, and no $o(1)$ uniform over all chains exists. For the "hence"
reading (the certified bound $h(n_0)+\sum_jL_j$), the sentence with an
unbounded seed would assert, at $J=0$, that every practical $n_0$ has
$h(n_0)\ge(1/(2\log2)-o(1))(\log\log n_0)^2$, which no page proves and which
is not known; so that reading is unsupported rather than refuted. With the
seed bounded independently of the scale, which the note's chain satisfies,
the floor holds by W3, and the section's conclusion for the note's mechanism
stands.

**S9.** Attempt: exhibit a mechanism of the folder that escapes both
obstructions. The factorial mechanism is blocked by S7 and the note's chain
by the corrected S8. The greedy expansion of Lemma 4 applied to a
non-factorial ratio-two integer such as $L_x$ (Lemma A) is not blocked by
either: the counting floor for $L_x$ is only $\gg\log\log L_x$, because
$\log\tau(L_x)\asymp x/\log x$ while $\log L_x\asymp x$. The section's
sentences do not claim to block it, but "neither mechanism of this folder"
and "needs a new certificate of practicality" leave the scope implicit (F6).
The attack fails against the sentences as scoped to factorials and the
note's chain.

**S10.** Attempts: use the nesting below its range (the decomposition
containing $b$ has at least two terms for $b\ge3$, and the lemma holds for
$k\ge2$); leave small $m$ uncovered (every $2\le m<b_0(\varepsilon)$ lies in
$D_k$ for large $k$ because $v(k)\to\infty$); break the count
($2h(N)+1<4(\log b)^{\varepsilon}+1\le5(\log b)^{\varepsilon}$ for $b\ge e$,
using $h((n-1)!)<(n-1)^{\varepsilon}$ and
$\lceil\log_2n\rceil\le n^{\varepsilon}$ for large $n$); break the final step
($(k/5)^{1/\varepsilon}\ge k^{A}$ for $\varepsilon=1/(2A)$ and $k\ge25$). All
fail against the lead's own sketch;
the full proof on the connections page's Problem 293 section is outside this
read set and was not examined.

**S11.** The priority sentence cannot be attacked or confirmed from the read
set (F2); the sentence "its standing is that of part (b)" is attacked by
noting that the transfer and the deduction are author-recorded and
unreviewed, so the standing is at most that of part (b) (F5); "exact site
questions" is attacked for Problem 293 by its own Formulation (F7). The
remaining input sentences were checked against the cards and pages named
above and hold.

## Premises

- **Part (b) of Problem 18** (accepted formal statement). Interface: for every
  $\varepsilon>0$, $h(n!)<n^{\varepsilon}$ for all sufficiently large $n$,
  with $h$ the fresh-set supremum over $1\le m\le n!$. Source: the JenW1N
  Conjectures.io record, a web record holding a Lean proof file, not held and
  not built here; read on the card's provenance paragraph and the target
  page's Statement and Formal statement (claims checked; no proof read).
  Consumed as an explicit hypothesis of S3 and S10 at its recorded standing.
- **Theorem 1 (Hughes)**, reconstruction page. Interface:
  $h(n!)\le(2\log2+o(1))n/\log n$. Read for statement and interface; the page
  imports the Berend–Harmse estimate second-hand through Corollary 3, whose
  page was read for its statement. Consumed by S4 at that standing.
- **Remark 6 (Hughes)**, reconstruction page. Interface: an absolute $c>0$
  with $h(n!)\ge c(\log n)^2$ for all large $n$. Read whole; the counting
  argument re-derived in outline (Chebyshev is the only import). Consumed by
  S7 and S9.
- **Lemma 4 (Hughes)**, reconstruction page. Interface: the greedy step for a
  ratio-two integer and the compilation-supplied ratio-two property of $n!$.
  Read whole. Consumed through Lemma A.
- **Lemma 3.1 (van Doorn)**, reconstruction page. Interface: $A\ge2$, $n$
  practical, every residue modulo $A$ a sum of at most $L$ distinct divisors
  of $n$ with total at most $n$ and no summand divisible by $A$ (empty sum
  allowed); then $An$ is practical and $h(An)\le h(n)+L$. Read whole and
  re-derived (W1); elementary. Consumed by S2 with $A=p$, $L=1$ and by Lemma
  D's hypothesis.
- **Proposition 4.1 (van Doorn)**, reconstruction page, standing *claimed*.
  Interface as quoted under S5. Read for statement and interface; proof not
  re-derived. Consumed by S5 only; S8 uses the bound on its seed
  $n_0\le2^{E}(2Q(k_0))^{k_0}$.
- **Lemma A** (shared, connections page). Interface: $n!$ and $(n-1)!$ are
  practical with the ratio-two property. Interface confirmed for factorials
  (the $v_2$ hypothesis holds for $n\ge4$, and $n\le3$ by inspection); proof
  belongs to another reviewer.
- **Lemma D** (shared, connections page). Interface as quoted under S8; read
  whole to locate the defect of F1; proof belongs to another reviewer. Its
  import, Wigert's maximal order of $\tau$, is standard and was not checked.
- **Lemma 5.1 and Theorem 1.2 of the van Doorn note**, held PDF (digest
  matches the card). Lemma 5.1, p. 6: statement and proof read on the page
  image; they coincide with Lemma C. Theorem 1.2, p. 1: statement read on the
  page image; matches the result page. The proof of Theorem 1.3 on p. 6 was
  read for the way the nesting lemma is used.
- **Lemma 2.1 and Theorem 1.1 of van Doorn–Tang**, held PDF, refereed
  (version of record cited on the result page). Lemma 2.1:
  $D_k\subseteq D_{k+1}$ for all $k\ge2$; Theorem 1.1: $v(k)\ge e^{ck^2}$
  for all $k\ge1$. Statements read on the p. 2 page image; proofs not
  checked. Consumed by S10.
- **Problem statements** E0304, E0293, E0018 (Statement and Formulation
  paragraphs only). Interfaces: $N(a,b)$ with denominators above $1$ and no
  coprimality; $v(k)$ under the $m>1$ reading; the site's $h$ over $1\le m<N$.

## Findings

**F1 (required).** Location: section, paragraph "What it does not give, and
why": "Along the extension chains of the van Doorn note it is impossible too:
Lemma D shows that every certificate built from Lemma 3.1 extensions is at
least $(1/(2\log2)-o(1))(\log\log N)^2$." The same claim on the lead, "What
the route cannot give": "certificates built from Lemma 3.1 extensions are
never below $(1/(2\log2)-o(1))(\log\log N)^2$." Defect: a hypothesis dropped
and a uniformity overstated. The floor holds only for chains whose seed is
bounded independently of the scale (or, in general, with $(\log\log n_0)^2$
subtracted); the consumed Lemma D statement asserts its $o(1)$ "uniformly
over all such chains", and its own commentary paragraph has the missing
words "from a fixed seed". Witness: the one-step chain $n_0=m!$, $A_0=2$,
$L_0=1$ of the Strongest attack, for which $\sum_jL_j=1$ while
$(1/(2\log2)-o(1))(\log\log n_1)^2\to\infty$; at $J=0$ the "hence" clause
would be an unproved universal lower bound on $h$ over practical numbers.
Consequence for the section: the obstruction blocks the note's chain, whose
seed is bounded, and every fixed-seed certificate, which is what the
paragraph's first clause names; it does not block "every certificate".
Proposed replacement (section): "Lemma D shows that every certificate built
from Lemma 3.1 extensions from a seed bounded independently of the scale,
as the note's chain is, is at least $(1/(2\log2)-o(1))(\log\log N)^2$." The
lead's sentence takes the same qualifier. Lemma D's statement should carry
the qualifier too, or state the floor as

$$
\sum_{j<J}L_j\ \ge\ \Bigl(\frac1{2\log2}-o(1)\Bigr)
\bigl((\log\log n_J)^2-(\log\log n_0)^2\bigr)-O(1);
$$

that repair belongs to Lemma D's reviewer.

**F2 (suggested).** Location: section, after (304.1): "is the first
consequence of the accepted part (b) outside Problem 18." Defect: a priority
claim with no recorded search; the page's "Sources read" lists none for it,
and the note itself (p. 1) says that bounds on $h(n)$ transfer to $N(b)$, so
the consequence is immediate to anyone holding both results. Witness: none
possible inside the read set, which is the point. Proposed replacement: "is
the first consequence of the accepted part (b) drawn in this corpus; no
search for an earlier one was made."

**F3 (note).** Location: section, proof of (304.1): "once $b>(n_0-1)!$."
Defect: the step $n<\log b$ uses $n\ge14$, which $b>(n_0-1)!$ ensures only
when $n_0\ge14$. Witness: $n_0(\varepsilon)=5$ (if the accepted threshold
were that small) and $b=25$ give $n=5>\log25$. Harmless under the statement's
"for large $b$". Proposed replacement: "once $b>\max(n_0-1,13)!$."

**F4 (note).** Location: section, (304.3): "which is the note's Theorem 1.2."
The derived bound is $2c_0(\log\log b)^2-2$, stronger by $2$ than the
recorded Theorem 1.2. Proposed replacement: "which implies the note's Theorem
1.2."

**F5 (note).** Location: section, after (304.1): "Its standing is that of
part (b)." The transfer and the deduction are author-recorded and unreviewed,
so the standing of (304.1) is at most that of part (b); the sentence's second
half says so, and the lead's desc is exact. Proposed replacement: "Its
standing is at most that of part (b)".

**F6 (note).** Location: section, "Next investigation": "Lemma D and Remark 6
show that neither mechanism of this folder can supply it, so it needs a new
certificate of practicality." The factorial obstruction is specific to $n!$
(through $\tau(n!)$) and the chain obstruction to fixed-seed Lemma 3.1
chains; the greedy expansion of Lemma 4 on another ratio-two family, such as
$L_x$ from Lemma A, is not covered, since its counting floor is only
$\gg\log\log N$. Proposed replacement: name the two blocked mechanisms and
add that the greedy route on non-factorial ratio-two integers is untested by
these obstructions.

**F7 (note).** Location: lead, "Targets and status evidence": "Both questions
are the exact site questions; no variant is substituted." For Problem 293 the
lead uses the $m>1$ reading that the problem page's Formulation records as a
correction of the defective literal wording. Proposed replacement: "Both
questions are the site questions, Problem 293 under the $m>1$ reading its
page records."

## Verdict

- S1 (Lemma C): refutation-failed.
- S2 (Lemma C′): refutation-failed.
- S3 ((304.1)): refutation-failed, as a deduction conditional on the accepted
  part (b) at its recorded standing; the implication is proved, the
  antecedent is assumed, and no conditional conclusion reads as
  unconditional.
- S4 ((304.2)): refutation-failed, conditional on Theorem 1 at its standing.
- S5 ((304.3)): refutation-failed, as a deduction from Proposition 4.1, which
  stays *claimed*; the derived bound is stronger by $2$ than the sentence
  says (F4).
- S6 (reduction): refutation-failed.
- S7 (factorial obstruction): refutation-failed.
- S8 (extension-chain obstruction, as written): proof defective; statement
  unresolved. The consumed Lemma D display is false as stated (witness in
  F1); the sentence's "every certificate" is unsupported for unbounded seeds
  and proved for seeds bounded independently of the scale, which covers the
  note's chain and the section's conclusion about it.
- S9 (consequence sentences): refutation-failed at the folder's two
  mechanisms, with the scope to be written out (F1, F6).
- S10 ((293.1), lead): refutation-failed against the lead's sketch,
  conditional on part (b); the full proof on the Problem 293 section was
  outside the read set.
- S11 (standing and input sentences): refutation-failed for the input
  sentences checked; the priority sentence is unverifiable here (F2), and
  two standing sentences overreach by a word (F5, F7).

Limitations: the proofs of the shared lemmas are another reviewer's charge and
were re-derived here only where the lead rests on them (C, C′, Lemma 3.1) or
where an interface failed (D); the Berend–Harmse import, Wigert's bound, the
van Doorn–Tang proofs and the Lean file were not examined; the Target
paragraph's account of the problem page's Current assessment was not checked;
no computation was needed. This focused review assigns no tier and changes
no status.

---
name: problems/unit_fractions/E0312
title: Problem 312
desc: |
  Asks whether, for some $c>0$, every large enough finite multiset of positive
  integers with reciprocal sum above $K$ has a subset whose reciprocal sum lies
  in $(1-e^{-cK},1]$.
tags:
- Number theory
- Unit fractions
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-08T02:16:54Z
---

# Problem 312

[[problems/unit_fractions/_index|..]]

***

**Statement.** Does there exist some $c>0$ such that, for any $K>1$, whenever
$A$ is a sufficiently large finite multiset of positive integers with
$\sum_{n\in A}\frac{1}{n}>K$ there exists some $S\subseteq A$ such that

$$
1-e^{-cK} < \sum_{n\in S}\frac{1}{n}\leq 1?
$$

**Formulation.** The site's wording, accessed 2026-09-18
(page last edited 20 January 2026). $A$ is a finite multiset of positive
integers, $S$ a submultiset, and the sums count multiplicity; write
$R(A)=\sum_{n\in A}1/n$ and $\varepsilon(A)=1-\max\{R(S):S\subseteq A,\
R(S)\le1\}$ for the deficit of the best subsum not exceeding $1$, so the
question asks whether $R(A)>K$ forces $\varepsilon(A)<e^{-cK}$. The 1980
monograph puts the size condition on the number of terms ("for fixed
$\alpha$ and $t$ sufficiently large, if $\sum_{k=1}^t1/s_k>\alpha$"); the
site's "sufficiently large finite multiset" renders it; Korsky's theorem
below has no size condition and instead requires $K\ge K_0$. Multiplicity
matters: with distinct denominators the problem is different (a
dense-set version is Problem 310).

**Status.** Open. The site labeled it OPEN. Erdős and Graham state the bound
with $c/K^2$ in place of $e^{-cK}$, in the monograph, without proof or
reference. The best bound found is Korsky's
$\varepsilon(A)\le\exp(-c\sqrt{K\log K})$ for $R(A)>K\ge K_0$. It appears in an
arXiv preprint of July 2026, whose second version, of October 2026, simplifies
the proof and keeps the theorem. The first version's acknowledgment declares
extensive assistance from GPT-5.5 Pro, and the second's says that GPT-5.5 Pro
carried out the Fourier analysis that completes the argument. The preprint has
no journal record, and its author states that no journal submission is planned.
Korsky's bound settles no instance of the question, so it has no claim page. A
construction shows that no bound better than $\exp(-(1+o(1))K\log K)$ holds for
all multisets (the site's thread; display (1.4) of the preprint's first
version). The conjectured exponential rate is open. No proof,
disproof or proof claim for it was found in the search whose scope the Current
assessment records. This is a bounded negative finding.

**Source.** [erdosproblems.com/312](https://www.erdosproblems.com/312),
accessed 2026-09-18: the problem page (labeled OPEN, with the site's
standard note that no finite computation can settle it; source key [ErGr80]
without a page; last edited 20 January 2026; "Formalised statement? Yes"),
its eight-comment discussion thread and its empty proof-claim tab. The
site thanks Mehtaab Sawhney. Cite as: T. F. Bloom, Erdős Problem #312,
https://www.erdosproblems.com/312, accessed 2026-09-18.

**References.**

- [ErGr80] Erdős, P. and Graham, R. L., Old and new problems and results in
  combinatorial number theory. Monographies de L'Enseignement Mathématique
  28, Université de Genève (1980), printed p. 40 (the site gives no page).
  Library home:
  [[../library/number_theory/erdos_1980_old_new_problems_results_combinatorial_number_theory/_index|erdos_1980_old_new_problems_results_combinatorial_number_theory]].
- [Ko26] Korsky, S., A stretched-exponential bound for an Erdős--Graham
  unit-fraction problem. arXiv:2607.04157v1 (5 July 2026; title page dated
  7 July 2026), 27 pages. The v2 of 8 October 2026 (10 pages; title page
  dated 7 July 2026) is retitled *Approximating $1$ by sums of unit
  fractions*; its arXiv comment says it substantially simplifies v1, and its
  Theorem 1, p. 1, states Theorem 1.1 of v1 with the same hypotheses and
  bound. Library home:
  [[../library/unit_fractions/korsky_2026_stretched_exponential_bound_erdos_graham_unit/_index|korsky_2026_stretched_exponential_bound_erdos_graham_unit]];
  result page for Theorem 1.1.

**Formalization.** Statement only. The file
[`ErdosProblems/312.lean`](https://github.com/google-deepmind/formal-conjectures/blob/d5ba143cc2fafd48cc6d5b6320a3aab287c38df7/FormalConjectures/ErdosProblems/312.lean)
of formal-conjectures (main, 2026-09-18; the link is pinned to that
commit) declares `erdos_312`, under `category research
open` with proof `sorry`, as the equivalence of `answer(sorry)` with the
following: there is a real $c>0$ such that for every real $K>1$ there is
an $N_0$ with the property that for every $n\ge N_0$ and every function
$a$ from `Fin n` to the natural numbers whose reciprocals (cast to the
reals) sum to more than $K$, some `Finset (Fin n)` has reciprocal sum
strictly above $1-\exp(-cK)$ and at most $1$. It encodes the multiset as
a function on `Fin n` with $n\ge N_0$ (the monograph's
condition on the number of terms) and does not require `a i ≥ 1`; no
audit of the encoding against the site's statement is recorded. The
community database (teorth/erdosproblems, `data/problems.yaml`,
2026-09-18) records status open (31 August 2025), a formalized
statement (24 September 2025), formal status unformalized and no OEIS
entry. No external Lean artifact is linked from the thread.

## Current assessment

**The question (site formulation of 2026-09-18).** The statement
above; OPEN, last edited 20 January 2026; source [ErGr80]. The whole
commentary is one sentence, saying that Erdős and Graham knew the
statement with $c/K^2$ in place of $e^{-cK}$. The thread (eight comments,
none verified by the site): 18 August 2025, Kovač introduces $R(A)$ and
$\epsilon(A)$ and the example
below showing $\epsilon(A)\ge e^{-(1+o(1))R(A)\log R(A)}$ along a sequence
of multisets, asking how optimal the exponential form is; 18 October 2025,
Kovač reports that Gemini Deep Research and ChatGPT found no closely
related literature (the linked transcript is not a source and is not
cited on this page);
24 June 2026, Korsky announces a forthcoming preprint proving
$\varepsilon(A)\le\exp(-c\sqrt{K\log K})$ and sketches the simpler
$\exp(-c\sqrt K)$ argument (maximal subsum, compression to a stable
multiset, a sparse activation lemma proved by Fourier analysis), with an
acknowledgment that the Fourier details were performed by GPT-5.5 and a
caution that they deserve close checking; 7 July 2026, the arXiv
link; 9 July 2026, four comments in which Kovač questions the paper's
terminology as machine-written and its crediting of sources, another
commenter quotes the paper's AI acknowledgment and asks whether the author
inspected the argument closely, and Korsky replies that this is their most
AI-involved paper, that the author reviewed it personally over several weeks and
is confident in the result, that the section and idea names were produced
by GPT-5.5, and that the author has no plans to send it to a journal. The
proof-claim tab is
empty. The community database says open.

**Origin.** Printed p. 40 of the 1980 monograph: "Is it true that there is
a $c>0$ such that
for fixed $\alpha$ and $t$ sufficiently large, if $\sum_{k=1}^t1/s_k>\alpha$
then for some choice of $\varepsilon_k=0$ or $1$,
$0\le1-\sum_{k=1}^t\varepsilon_k/s_k<e^{-c\alpha}$? We know only $c/\alpha^2$
as an upper bound at present." The $c/\alpha^2$ bound is stated without
proof or reference, and no published proof of it was located; Korsky's
introduction attributes it to the monograph (v1: "They proved the polynomial
estimate $\varepsilon(A)\ll K^{-2}$"; v2 says the same). It is recorded on
this page as the proposers' attested bound, not as a compiled result.

**Best known bound (a preprint claim).** Korsky's
[[../library/unit_fractions/korsky_2026_stretched_exponential_bound_erdos_graham_unit/theorem_1_1|Theorem 1.1]]
(arXiv v1, p. 1; Theorem 1 of v2, p. 1): there are absolute constants
$c>0$ and $K_0$ such that every finite multiset $A$ of positive integers
with $R(A)>K\ge K_0$ satisfies $\varepsilon(A)\le\exp(-c\sqrt{K\log K})$,
that is, some submultiset has reciprocal sum in
$[1-\exp(-c\sqrt{K\log K}),1]$. The proof of v1 (Sections 2--4 and two
appendices, 24 pages) removes a maximal subsum, compresses the remainder
into a multiset $C$ with multiplicities $m_n<P^-(n)$ whose subsums lift to
$A$ and avoid $(1-N^{-2},1)$ with $N=1/\varepsilon(A)$, and shows by a
sparse-activation local-limit estimate that such a $C$ has reciprocal mass
$R(C)\ll(\log N)^2/\log\log N$; since $R(C)>K-1$, this gives
$\log N\gg\sqrt{K\log K}$. The v2 of 8 October 2026 (10 pages) keeps the
compression, with the forbidden interval $(1-N^{-1},1)$, and replaces the
activation package, its appendices and the rough-number sieve by one
estimate for a group of denominators whose ratios $m_n/n$ lie within a factor
$4$ (Lemma 2, p. 3). Its bound depends on the largest number of the
group's denominators that divide a single integer at most $N^3$, and Section
5 proves it with a random subsum: near frequency zero its characteristic
function is compared with a normal one, and at larger frequencies that
divisor count bounds it. Elementary divisor counts for primes and composites
(Section 4) then give the same $R(C)\ll x^2/\log x$ with $x=\log N$. The v2
omits the barrier display (1.4) and the citation of the site's page. The
theorem and its proof's conclusion are unchanged, so v2 changes nothing this
page records about the problem's standing. Read depth: in v1, claims checked
for the theorem, the barrier display and the two compression lemmas, with
their proofs, and the analytic core in outline only; v2 read in full, its
compression and counting followed and its Fourier estimate in outline only.
Acceptance: none. The paper is an unrefereed preprint. The acknowledgment of
v1 declares that the author was assisted by GPT-5.5 Pro extensively during
the development and writing of the manuscript, in particular in filling in
technical details (the author claims the conceptual reductions and proof
strategy and takes responsibility). The acknowledgments of v2 say that the
author, inspired by Liu and Sawhney's random reciprocal sums and Croot's
Fourier argument, formulated the compression and the random-sum
construction, that GPT-5.5 Pro carried out the Fourier analysis needed to
complete the argument, and that the author reviewed, modified and verified
the arguments and takes full responsibility. The thread disputes the paper's
provenance and crediting as described above, and the author states that it
will not be submitted to a journal. The site's page does not cite it. It is
recorded on this page as the best bound found, with that provenance, and its
correctness is neither confirmed nor doubted on this page.

**The barrier.** Let $A_z$ contain $p-1$ copies of $1/p$ for every prime
$p\le z$ (Kovač, 18 August 2025; display (1.4) of Korsky's v1, which v2
omits). No submultiset has reciprocal sum exactly $1$, all subsums lie on a
lattice of spacing $1/\prod_{p\le z}p=e^{-(1+o(1))z}$, and
$R(A_z)\sim z/\log z$, so
$\varepsilon(A_z)\ge\exp(-(1+o(1))R(A_z)\log R(A_z))$. Any bound valid for
all multisets is therefore at best $\exp(-(1+o(1))K\log K)$; the
conjectured $e^{-cK}$ is compatible with it, and the truth lies between
$\exp(-(1+o(1))K\log K)$ (worst case at least this large) and
$\exp(-c\sqrt{K\log K})$. The argument is elementary and is recorded as
the sources give it, not independently rechecked.

**Formal statements.** The formal-conjectures statement is summarized under
Formalization; nothing beyond it exists.

**Search scope.** The problem, discussion and proof-claim
pages; the community database record; the formal-conjectures file at the
pinned commit; the arXiv listing for 2607.04157 (v1 only on 2026-09-18; v1
and v2 on 2026-10-13; no journal reference) and Crossref bibliographic
queries for the titles of v1 and v2 (no record); the Semantic Scholar record
(rate-limited, no data); arXiv API searches for abstracts naming unit
fractions and Graham (seven records, none on this deficit question),
Egyptian fractions with subset sums or multisets (one unrelated record) and
"Erdos problem" with the problem number (none); the monograph's p. 40; one
general web search (Korsky's arXiv pages, a Wikipedia article on a different
Erdős--Graham problem, a Discrete Analysis paper on Egyptian fractions of
Problem 297's kind; nothing else). Not searched: MathSciNet, zbMATH, Google
Scholar full text, X. Nothing found proves the exponential bound or
refutes it; this is a bounded negative finding.

**Remaining gaps.** (1) Korsky's analytic core, in both versions, is
recorded in outline only, and the paper is unrefereed and unreviewed; it is
the only source for the stretched exponential. (2) The monograph's $c/K^2$
has no located proof. (3) Whether the true worst-case rate is exponential in
$K$ or of order $K\log K$ in the exponent is open. (4) The formal
statement's encoding was not audited.

## Progress and known results

- Erdős and Graham (1980, printed p. 40): the question; the bound $c/K^2$
  stated without proof.
- Korsky (2026, preprint):
  [[../library/unit_fractions/korsky_2026_stretched_exponential_bound_erdos_graham_unit/theorem_1_1|Theorem 1.1]]
  of v1 (Theorem 1 of v2), $\varepsilon(A)\le\exp(-c\sqrt{K\log K})$ for
  $R(A)>K\ge K_0$; display (1.4) of v1, the barrier
  $\exp(-(1+o(1))K\log K)$ from the prime multisets.
- Related: the dense-subset version with bounded denominators,
  [[problems/unit_fractions/E0310/_index|Problem 310]]; the near-one subsums of
  $\{1,\ldots,N\}$ of [[problems/unit_fractions/E0311/_index|Problem 311]]; the
  exact representations of $1$ from short intervals of
  [[problems/unit_fractions/E0286/_index|Problem 286]].
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/number_theory/erdos_1980_old_new_problems_results_combinatorial_number_theory/_index|erdos_1980_old_new_problems_results_combinatorial_number_theory]]
- [[../library/unit_fractions/korsky_2026_stretched_exponential_bound_erdos_graham_unit/_index|korsky_2026_stretched_exponential_bound_erdos_graham_unit]]
- [[../library/unit_fractions/korsky_2026_stretched_exponential_bound_erdos_graham_unit/theorem_1_1|korsky_2026_stretched_exponential_bound_erdos_graham_unit / theorem_1_1]]

<!-- END problem library links -->

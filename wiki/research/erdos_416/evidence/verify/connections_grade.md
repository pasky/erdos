---
name: research/erdos_416/evidence/verify/connections_grade
title: "Distinct grade of the Problem 416 connections reviews"
desc: |
  Distinct grade of the seven focused reviews of the Problem 416 connections
  page and its two leads as they stood on 2026-09-28T13:50:48Z: all seven
  pass, ten corrections accepted as C1-C10, every other finding downgraded or
  rejected with its reason, both leads reviewed; no tier.
created: 2026-09-28T19:48:03Z
updated: 2026-09-28T19:48:03Z
---

***

## Subject

**Date.** 2026-09-28T13:50:48Z: the repository as it stood then, the tip of
the default branch when the reviews were written (called "the commit"
below); every page below was read at that commit with `git show`, and the
reports as the working-tree files at grading.

**Page graded**, repository-relative path at that commit:
`wiki/research/erdos_416/connections.md`
([[research/erdos_416/connections|the connections page]]): its shared
sections (Purpose and standing, Notation, Imported inputs, The search;
lines 1–90) as the inputs every section consumes, and its seven reviewed
H2 sections, "Problem 417: the two counts of distinct totients"
(lines 91–341), "Problem 416 at a general scale: the accepted family with
another balance" (lines 342–453; the commissions named it "with another
scale", and the page has exactly one general-scale section), "Problem 821:
large fibers versus repeated representations" (lines 454–492), "Problem
694: the extreme fiber ratio" (lines 493–518), "Problem 51: the
least-preimage ratio" (lines 519–561), "Problem 49 and the monotone-set
reconstructions: shared inputs" (lines 563–591) and "Shifted collisions:
Problems 1003 and 1004 and the two totient leads" (lines 592–621). The
closing section "Other pages checked" (lines 623–659) has no report and is
not graded.

**Leads graded**, at the same commit:

- `wiki/research/leads/distinct_totient_preimage_ratio/_index.md`
  ([[research/leads/distinct_totient_preimage_ratio/_index|the Problem 417 lead]]),
  whose route is the Problem 417 section;
- `wiki/research/leads/general_scale_totient_doubling/_index.md`
  ([[research/leads/general_scale_totient_doubling/_index|the general-scale lead]]),
  whose route is the general-scale section.

**Reports graded**, the seven focused reviews filed in this folder, each
naming the commit above as its subject and read in full:

- [[research/erdos_416/evidence/verify/connections_problem_417_the_two_counts_of_distinct_totients_review|the Problem 417 review]];
- [[research/erdos_416/evidence/verify/connections_problem_416_at_a_general_scale_the_accepted_fami_review|the general-scale review]];
- [[research/erdos_416/evidence/verify/connections_problem_821_large_fibers_versus_repeated_represe_review|the Problem 821 review]];
- [[research/erdos_416/evidence/verify/connections_problem_694_the_extreme_fiber_ratio_review|the Problem 694 review]];
- [[research/erdos_416/evidence/verify/connections_problem_51_the_least_preimage_ratio_review|the Problem 51 review]];
- [[research/erdos_416/evidence/verify/connections_problem_49_and_the_monotone_set_reconstructions__review|the Problem 49 review]];
- [[research/erdos_416/evidence/verify/connections_shifted_collisions_problems_1003_and_1004_and_th_review|the shifted-collisions review]].

**What was read, and at what depth.** `docs/verification.md`, the sections
"Independence and the assignment", "Exact subjects and durable evidence",
"Report contract", "Grading and claim standing", "Whole-claim report" and
"Audit checklist", in full. The seven reports in full, then the page and
the two leads in full. The folder's reconstruction pages at the commit
where a finding needed them: Step 1 of
[[research/erdos_416/zeraoulia_theorem_1_1_reconstruction|the preprint's Theorem 1.1 page]]
(the range of the derivative bound, for C1); the family description, the
"Actual values" bullet and the "Uniform prime counting" gloss of
[[research/erdos_416/kruer_kohlmeyer_theorem_1_1_reconstruction|the Theorem 1.1 page]]
(for C5 and the Problem 694 and 821 verdicts); the Source, Standing,
Statement and Specialization sections of
[[research/erdos_416/kruer_kohlmeyer_lemma_2_1_reconstruction|the Lemma 2.1 page]]
(for the general-scale review's note F5). Outside the reviewers' read
sets, as the grader who is not blind: the Problem 49 folder at the commit,
its index (the "Connections and leads" paragraph), its connections page
(the outcomes paragraph, Propositions 2, 3 and 4 with their proofs, the
parallel-derivation paragraph and the closing section), its Theorem 1.2
page (the imported inputs and the deduction from input (C)) and its Lemma
4.1 page (the statement, the imported counts and the proof of (iii)); the
problem pages of 416 (statement, status, references and current
assessment), 417 (headings), 51 and 821 (statement, current assessment,
progress and known results), 1004 (statement and progress) and 694
(statement and status); and the held sources in their text conversions,
each at the locators the findings cite: Ford (1998), the paragraph after
Table 1, §1.2 with Theorem 4 and the general-scale remark, Theorem 8 in
§1.3 and the closing paragraphs of §7 with the witness list; the 17-page
manuscript of Pollack, Pomerance and Treviño (2013), the definition of a
convenient number with its attribution, Theorems 3.1 and 3.3, the order
of magnitude on its p. 7, Lemma 4.1 and the proof of Theorem 1.2; the
five-page note behind Problem 694, Proposition 3.1 with its proof; Maier
and Pomerance (1988), the closing paragraphs of §5; Erdős (1974), the
passage on printed p. 201, and Erdős (1979), the closing problems; the
corollaries of Baker and Harman (1998) and Lichtman (2022) with their
exponents. No page image was needed: no adjudicated finding rests on a
display the text layer could garble. No other review, grade or evidence
folder was read; nothing outside the repository was consulted.

**Independence facts, by role.** The grader is a distinct fresh context
given only the grading assignment: neither the author of the page, the
leads or any reconstruction page, nor the reviewer who wrote any of the
seven reports, nor a collaborator of either, with no communication with
either. Every adjudication below was made against the page, the leads,
the sources and the grader's own computation; the reports' derivations
were re-derived, not trusted. Under the folder's rule the grader is
identified by role only.

**The grader's computation.** Two programs written for this grade, kept
in scratch and described here so the figures can be redone. The first
sieves Euler's function in exact integer arithmetic for all
$n\le6.2\cdot10^7$, which covers every preimage of every totient
$v\le10^7$ (an argument with at most nine distinct prime factors has
$n/\varphi(n)\le\prod_{p\le23}p/(p-1)<6.12$, and one with ten or more has
$\varphi(n)\ge\varphi(2\cdot3\cdots29)>10^9$), and tabulates for every
totient $v\le10^7$ its least preimage, the number of its preimages and
the greatest common divisor $g(v)$ of all of them, so that $v\in S(k)$
exactly when $k\mid g(v)$. The second enumerates all preimages of a given
$d$ by recursion over the odd primes $p$ with $p-1\mid d$, handling the
power of $2$ separately, and was validated against brute force for every
$d\le3000$. Reproduced exactly: the four rows $(V,V',V_0)$ at
$x=10^4,\dots,10^7$; $\max r=2.0355$ at $v=5888$ up to $10^6$ and
$4158795/2037248=2.04138\ldots$ at $v=2037248$ up to $10^7$; the ten
totients $v\le10^7$ with $r(v)>2$; the four proportions in
$(5\cdot10^6,10^7]$, the last being $5/794194$; $|S(3)\cap[1,10^7]|=2069$;
$S(k)\cap[1,10^7]=\emptyset$ for $k\in\{2,4,6,8,10,12,15,20,21,35,45,105\}$;
$g(v)$ odd for every totient $v\le10^7$, with $129005$ distinct values
having two distinct prime factors and $977$ three, and
$\max g(v)/\varphi(g(v))=19/12$ at $v=116964$; the preimage sets of $54$,
$216$, $324$, $540$, $580$, $46240$, $103240$, $116964$, $5888$, $6$,
$48$, $2^{18}\cdot257$ and $2^{18}\cdot257+28$; the primes $5\le r<200$
with $54(r-1)\in S(3)$, exactly $79$ and $107$; and, for the Problem 821
review's illustration, $g(48)=11$ against six primes $p$ with
$p-1\mid48$, the largest fiber $1023$ among totients $t\le300000$, and
$t=276480$ with $769$ preimages against $34$ primes $p$ with $p-1\mid t$
and $d(t)=96$.

**Materiality rulings on the disclosed exposures.** Each report discloses
reads beyond its allowed set. The content test (whether anything in the
report could only have come from the exposure, or whether an attack's
direction or the charge's strength followed it) gives immaterial in all
seven cases. (1) The Problem 417 review saw the problem page's assessment
and progress sections and a card's living-verification line; its
derivations (the scale sum, the tail below $y_0$, the crossing argument,
the $S(4)$ witness with its eight preimages, the sieve) appear in none of
them, and the progress section restates the section's results without a
verdict. (2) The general-scale review saw the problem page's status and
provenance paragraphs, two cards whole and a tree listing that named this
folder's files, none opened; its required finding, the telescoping at
$c=4$, is its own arithmetic, and the standing it characterizes is what
the section's own standing sentences state. (3) The Problem 821 review saw
the problem page's headings and its status field only. (4) The Problem 694
review saw the problem page's status and the first two paragraphs of its
assessment, the note's card whole, two card summaries and two problem
statements; it marks the one check that used the status paragraph, which
this grade repeated directly (the page records solved (Lean), the
five-page note, two external Lean developments read as text, and no
refereed publication or independent review); its required finding is the
witness $r=5$, its own. (5) The Problem 51 review saw the problem page
whole and the reconstruction pages' standing paragraphs; its one finding
resting on that text, F8, is downgraded below on a separate ground, and
its required findings come from its own sieve and derivation. (6) The
Problem 49 review read four pages of the Problem 49 folder outside its
commissioned set; they are the subjects of the section's claims, so the
commission could not be discharged without them, their standing text is
author-recorded and carries no verdict on the section, and the review's
findings are checked here against those pages directly. (7) The
shifted-collisions review saw standing text of the two leads, the
reconstruction page, two result pages and the Problem 249 statement
block; none concerns the section and none is used.

## Reports graded

**The Problem 417 review: pass.** The subject block names the commit, the
page, the section's line range and the lead, all of which resolve; the
role, the allowed and actually read material and two exposures are
stated. The restatement carries every quantifier of the eight statement
groups (real $x\ge1$ in Lemma 417.1, the integer and real cluster sets and
the clause "under (W)" in Proposition 417.2, "an unbounded set of $x$" in
Theorem 417.3, the "for all $y\ge y_1$" premise of Proposition 417.4, the
two hypotheses of the frame, the finite range of the numbers). All ten
checklist items carry an explicit verdict, three of them failing at the
two sentences the review refutes. The three weakest steps are re-derived
in full: the sum of $V$ along the scales $x(2/3)^j$ with the derivative
bound itself re-derived from the reconstruction's Step 1, the tail below
$y_0$ and the contradiction with an explicit threshold, and the crossing
argument with the threshold $n_0\ge e^2$ that the page omits. The
strongest attack is real for every statement, and two of them succeed
with exact witnesses (Ford's $k=4$ witness against the support clause of
(H2); $v=5888$, $x=11900$ against the finite-range sentence). The premises
name each source interface with its locator and reading depth, and the
verdict is given per statement with the two refutation words in full.

**The general-scale review: pass.** The subject resolves the commission's
heading against the page's and names the commit, the line range and the
lead; four exposures are disclosed. The restatement gives the thirteen
statements with their quantifiers, including the order of choices in
Proposition 416.3 and the exact conditional of the second remark. All ten
items carry explicit verdicts. The weakest steps are re-derived: Step 4 of
the proposition with every threshold tracked, the conditional deduction of
(5$_c$) including the lower ends of the prime ranges that the page leaves
implicit, and the product constraint $\alpha_c\beta_c=2$ from the
accepted law. The strongest attack is real and succeeds against the
universal "for every $c\ne2$" with the witness $c=4$; the attacks on the
lemmas, the proposition and the block mean are recorded with their
failures. The premises give each reconstruction page, the write-up, Ford,
Guy and the problem statement with reading depth, and the verdict is per
statement.

**The Problem 821 review: pass.** Subject, role, read set and two
borderline exposures are stated and the commit and line range resolve.
The restatement carries the target's quantifiers ("for every
$\epsilon>0$", "infinitely many"), the divisor bound in its eventual
form, and the collapse with the hypothesis the sentence omits. All ten
items carry explicit verdicts, three marked inapplicable with reasons.
The weakest steps are re-derived: the fiber injection into the divisors of
$t$ with a proof of $d(t)=t^{o(1)}$, the collapse under both readings of
"top prime" with the witnesses $t=48$ and $t=6$, and the two-sided
inequality between the pair fiber and the $\varphi$-fiber. The strongest
attack seeks a family with a fiber above $d(t)$ and identifies the one
escape (records with repeated core values), which the premise closes. The
premises record Ford, Baker and Harman, Lichtman and Erdős at statement
depth with locators, and the verdict is per statement.

**The Problem 694 review: pass.** Subject and line range resolve; five
exposures are disclosed with the one check that used exposed text marked.
The restatement carries the nine statements with their quantifiers,
including the $\varepsilon$-proportion's range and the "every prime
$r\nmid ab$" of the propagation sentence. All ten items carry explicit
verdicts. The weakest steps are re-derived: the propagation sentence fails
at $r=5$ with an exact enumeration; the sparseness of the extreme fibers
is derived in the problem's own units; the conditional typical-ratio
statement is derived with its premise set named. The strongest attack is
real (collisions inside the pair family against the obstruction; the
statements of Problems 417 and 51 against the catalog sentence) and
succeeds against S8 with a hand-checkable witness. The premises give the
note, Ford, the 2013 manuscript and the Problem 417 section with reading
depth, and the verdict is per statement.

**The Problem 51 review: pass.** Subject and line range resolve; two
exposures are disclosed and the one finding resting on them is marked.
The restatement carries twelve statements with quantifiers, including the
integer index $K$ of the reformulation. All ten items carry explicit
verdicts. The weakest steps are re-derived: which moduli lift the cap
(with the exact bound $15/8$ for two odd primes and the witnesses $580$,
$116964$, $103240$ from the reviewer's own sieve), the dichotomy behind
the necessity sentence, and the reformulation with the confinement of
$V_0$. The strongest attack is real for every statement and succeeds
against the cap sentence and the necessity sentence. The premises give
Ford's Theorem 8 and §7, Guy's B36 and the page's inputs with reading
depth, and the verdict is per statement with the three verdict forms
written in full.

**The Problem 49 review: pass.** Subject and line range resolve; four
exposures are disclosed, including a bug found and fixed in the reviewer's
own enumerator. The restatement carries ten statements with their scope
(every finite $N$ for the obstruction, every real $x$ for the identity of
counts, the exact pair for the reversed sentence). All ten items carry
explicit verdicts. The weakest steps are re-derived: the bridge from Lemma
4.1 to $V\ll V'$ with the seed $1$ and the role of each clause, the
obstruction at every $N$, and the two clauses of the p. 7 sentence. The
strongest attack is real and succeeds against the index bookkeeping
sentence at the pinned commit. The premises record each source and folder
page with reading depth, and the verdict is per statement.

**The shifted-collisions review: pass.** Subject and line range resolve
and the two leads are named; the exposures are disclosed. The restatement
carries eight statements with the conventions of the retained family and
the two collision equations. All ten items carry explicit verdicts, four
marked inapplicable with reasons. The weakest steps are re-derived: the
split of $P(x;k)$ into a pair-form part bounded by $2E_{2x}$ and a part
(4) cannot see; the linear distance between pair collisions of cores with
different radicals, with exact witnesses; and the reindexing construction
showing that the value set decides neither problem. The strongest attack
re-derives the manuscript's uniform bound including odd shifts and its
$c(k)$ bound. The premises give the write-up, the reconstruction's Step 2,
the manuscript, the problem statements and the leads with reading depth,
and the verdict is per statement.

## Corrections

**C1.** Page: the connections page. Location: "Imported inputs, at their
standing", bullet (F), the clause "$|\psi_c'(t)|\le K'/t$ for
$\psi_c(t)=\Psi(c^t)$, $c^t\ge e^e$". Replace "$c^t\ge e^e$" with
"$\log(c^t)\ge e^e$". Basis: Step 1 of the preprint's Theorem 1.1 page
puts $u=\log(c^t)$ and derives the bound under "for $u\ge e^e$"; for
$e^e\le c^t<e^{e^e}$ the term $\log_4(c^t)=\log\log\log u$ is negative and
its derivative $1/(t\log u\log\log u)$ is unbounded as
$\log\log u\to0^+$, so the bullet claims the bound on a range where it is
not proved. Step 4 of Theorem 417.3 applies the bound only for
$z\ge x^{1/2}$ with $x$ large, so no proof changes. The Problem 417
review's suggested finding F3, accepted because the imported input is
misquoted.

**C2.** Page: the connections page. Location: "Reformulation and
finite-range numbers (exploratory)". (a) The hypothesis "(H2) for each
fixed $u\in(0,1]$ and $t\ge1$, $\#\{v\le ux:r(v)\le t\}/V(ux)\to G(t)$ for
a distribution function $G$ on $[1,\infty)$ with $G(t)=1$ for $t\ge2$".
Replace with: "(H2) for each fixed $u\in(0,1]$ and $t\ge1$,
$\#\{v\le ux:r(v)\le t\}/V(ux)\to G(t)$ for a nondecreasing function $G$
on $[1,\infty)$ with values in $[0,1]$". (b) The display's second limit,
"$\frac{V_0(x)}{V(x)}\to\int_1^2\bigl(1-G(t)\bigr)\frac{dt}{t^2}$".
Replace the upper limit $2$ with $\infty$. (c) "Next investigation" item
2, after "are the tools." Insert: "No support bound is available: by (F8)
at $k=4$ with Ford's witness $2^{18}\cdot257$, every $v\in S(4)$ other
than a power of $2$ has $r(v)>2$, since its least preimage $m$ has
$4\mid m$ and an odd prime factor, so $m/\varphi(m)>2$; hence
$1-G(2)\ge c_4>0$ for any limiting $G$, and the law to prove or refute is
(H2) without a support bound." Basis: the eight preimages of
$2^{18}\cdot257$ are $135268352$, $143722624$, $169085440$, $179653280$,
$202902528$, $215583936$, $253628160$ and $269479920$, all divisible by
$16$, so (F8) gives $V(x;4)\ge c_4V(x)$ for large $x$; a least preimage
$m$ with $4\mid m$ that is not a power of $2$ has
$m/\varphi(m)=2\prod_{p\mid m,\,p>2}p/(p-1)>2$, and if $m$ is a power of
$2$ then $v$ is; so $\#\{v\le x:r(v)>2\}\ge c_4V(x)-\log_2x-1$, and (H2)
at $u=1$, $t=2$ forces $G(2)\le1-c_4<1$. The frame's deduction uses no
support bound, and $\int_0^1(1-G(1/u))\,du=\int_1^\infty(1-G(t))\,dt/t^2$
by $t=1/u$. The Problem 417 review's required finding F1.

**C3.** Page: the connections page. Location: the same paragraph, "so in
this range every element counted by $V_0(x)$ lies in $(x/2,x]$." Replace
with: "so in this range every element counted by $V_0(x)$ lies in
$(x/2.0414,x]$, and only the ten totients $v\le10^7$ with $r(v)>2$
($5888$, $10496$, $17408$, $276736$, $2037248$, $5268992$, $5331968$,
$6983168$, $8043008$ and $8749568$) can fall in $(x/2.0414,x/2]$." Basis:
an element $v$ counted by $V_0(x)$ has $x<f_{\min}(v)\le2.0414\,v$, so
$v>x/2.0414$ and nothing more; witness $v=5888$ with $f_{\min}(v)=11985$
and $x=11900$, where $v\le x<f_{\min}(v)$ and $v\le5950=x/2$, and every
integer $x\in[11776,11984]$ does the same. The grader's sieve finds
exactly the ten totients listed. The page's own maximum $2.0414>2$
already contradicts the sentence. The Problem 417 review's required
finding F2.

**C4.** Pages: the connections page and the general-scale lead. (a) The
section "What it does not give", the clause "nothing for $c\ne2$ until
(5$_c$) is verified, so the preprint's dichotomy stands for every
$c\ne2$". Replace with: "nothing for $c$ outside the integer powers of $2$
until (5$_c$) is verified, so the preprint's dichotomy stands for every
$c>1$ that is not an integer power of $2$". (b) The paragraph "What the
accepted $c=2$ law adds without any premise, for $c=2^{1/m}$ with
$m\ge2$", after its last sentence ending "does not make the interval
degenerate." Append: "For $c=2^m$ with an integer $m\ge2$ the same
telescoping settles the variant outright at the standing of the accepted
file: $V(2^mx)/V(x)=\prod_{i=0}^{m-1}V(2^{i+1}x)/V(2^ix)\to2^m$ as real
$x\to\infty$, so the cluster set is $\{c\}$; and for $c=2^{k/m}$ the
product of $R_c$ over $m$ consecutive scales tends to $2^k$." (c) The
Target paragraph, the sentence ending "and the cluster set is a closed
interval of unknown width." Append before the period: "; the integer
powers of $2$ are settled by the accepted law by telescoping, as recorded
below". (d) The lead, "Consequential gap", "Without it the reconstructed
cluster interval $[\alpha_c,\beta_c]$ stands for every $c\ne2$; the
accepted $c=2$ law adds only that for $c=2^{1/m}$ the geometric mean of
$V(cx)/V(x)$ over $m$ consecutive scales tends to $c$ (for $m=2$,
$\alpha_c\beta_c=2$), which gives near-hits and no width control."
Replace with: "Without it the reconstructed cluster interval
$[\alpha_c,\beta_c]$ stands for every $c>1$ that is not an integer power
of $2$; the accepted $c=2$ law settles $c=2^m$ for every integer $m\ge1$
by telescoping, and for $c=2^{1/m}$ adds that the geometric mean of
$V(cx)/V(x)$ over $m$ consecutive scales tends to $c$ (for $m=2$,
$\alpha_c\beta_c=2$), which gives near-hits and no width control." (e) The
lead, "Target and exact question", the sentence ending "and the cluster
set is a closed interval of unknown width." Append before the period: ";
the integer powers of $2$ are settled by the accepted law by telescoping
(Consequential gap)". Basis: the accepted law is $V(2y)/V(y)\to2$ as real
$y\to\infty$ (the Theorem 1.1 page's display (6) is stated for real
$x$), so with $y=2x$,
$V(4x)/V(x)=\bigl(V(4x)/V(2x)\bigr)\bigl(V(2x)/V(x)\bigr)\to4$, the
dichotomy is decided in its first horn at $c=4$, and induction gives every
integer power. The general-scale review's required finding F1.

**C5.** Pages: the connections page and the general-scale lead. (a) The
section's second remark, "if the pairs above a core $b$ are the primes $p$
with $b(p-1)$ in a range whose upper end is $y/b$, then
$B^{(c)}_y/H(y)\to1/c$ by the same uniformity of the prime number theorem
($\pi(u/c)/\pi(u)\to1/c$ uniformly for $u\ge y^{1-o(1)}$), and (5$_c$)
holds for every $c>1$." Replace with: "if the pairs above a core $b$ are
the primes $p$ in an interval whose upper end is $y/b$ for $p-1$, so that
$b(p-1)\le y$, then the $c=2$ balance forces the lower ends of these
intervals to be negligible in aggregate, and $B^{(c)}_y/H(y)\to1/c$ by
the same uniformity of the prime number theorem ($\pi(u/c)/\pi(u)\to1/c$
uniformly for $u\ge y^{1-o(1)}$), so (5$_c$) holds for every $c>1$."
(b) The lead, "Provisional premises", "If the pairs above a core $b$ are
the primes $p$ with $b(p-1)$ in a range whose upper end is $y/b$, then
$B^{(c)}_y/H(y)\to1/c$ follows from the uniformity
$\pi(u/c)/\pi(u)\to1/c$ for $u\ge y^{1-o(1)}$, and (5$_c$) holds for every
$c>1$." Replace with: "If the pairs above a core $b$ are the primes $p$ in
an interval whose upper end is $y/b$ for $p-1$, so that $b(p-1)\le y$,
then the $c=2$ balance forces the lower ends to be negligible in
aggregate, $B^{(c)}_y/H(y)\to1/c$ follows from the uniformity
$\pi(u/c)/\pi(u)\to1/c$ for $u\ge y^{1-o(1)}$, and (5$_c$) holds for every
$c>1$." Basis: the Theorem 1.1 page's gloss of §4.3 has the pairs above
$b$ as "the primes $p$ in a range with $b(p-1)\le y$", the write-up's
value window; as written the sentence describes pairs whose values stop
at $y/b$. The lower-end step, which the sentence needs and omits, was
re-derived by the grader: with $w_b=\pi(u_b+1)$, $u_b=y/b$,
$x_b=\pi(\ell_b)/w_b$ for the lower end $\ell_b$, the counts are
$a_b=w_b(1-x_b)$ and $b^{(c)}_b=w_b(1/c-x_b+o(1))^+$ uniformly in $b$; the
$c=2$ balance $B_y/A_y\to1/2$ reads
$\sum_bw_b\bigl[(1/2-x_b+o(1))^+-(1-x_b)/2\bigr]=o(A_y)$, and the bracket
is at most $-\min(x_b,1-x_b)/2+o(1)$, so
$\sum_bw_b\min(x_b,1-x_b)=o(A_y)$; for every $c>1$ the defect
$|b^{(c)}_b-a_b/c|$ is at most $w_b\min(x_b,1-x_b)$ in each of the cases
$x_b\le1/c$ and $x_b>1/c$, whence $B^{(c)}_y-A_y/c=o(A_y)$. A non-interval
range such as $p-1\in(u_b/4,u_b/2]\cup(3u_b/4,u_b]$ satisfies the $c=2$
balance and violates (5$_4$), so the interval hypothesis carries the
conclusion. The general-scale review's suggested finding F2, accepted
because the sentence as written misdescribes the family.

**C6.** Pages: the connections page and the general-scale lead. (a) The
section's "Next investigation", "a negative one shows the family's prime
ranges tied to the scale $2$, so that a general-scale family needs its own
estimates (3)–(5)." (b) The lead's "Next step", the same sentence. Replace
both with: "a negative one closes this route: (5$_c$) for the accepted
family would then need an argument of its own, or a differently balanced
family with its own estimates (3)–(5)." Basis: a negative outcome (the
file's top-prime ranges or its count not scale-free) closes the deduction
of (5$_c$) through the second remark; it does not show (5$_c$) false for
the accepted family, since (5$_c$) is a statement about that family's pair
counts that a different argument could establish, so it does not show
that a new family is needed. The page's purpose paragraph promises for
each outcome "what each outcome would establish"; the sentence claims
more than the outcome establishes. The general-scale review's suggested
finding F3.

**C7.** Page: the connections page. Location: the Problem 694 section,
"The one shared device is the note's Proposition 3.1, that a collision
$\varphi(a)=\varphi(b)$ propagates to the values $(r-1)n$ for primes
$r\nmid ab$: this is the multiplication by convenient integers behind
Ford's Theorem 8 and the Problem 49 folder's Lemma 4.1, and the witness
$d=54$ of Theorem 417.3 propagates the same way." Replace with: "The one
shared device is the existence half of the multiplication by convenient
integers behind Ford's Theorem 8 and the Problem 49 folder's Lemma 4.1:
the note's Proposition 3.1 observes that a collision
$\varphi(a)=\varphi(b)=n$ gives $(r-1)n$ the preimages $ra$ and $rb$ for
every prime $r\nmid ab$, and needs nothing about the other preimages of
$(r-1)n$, whose absence is what convenient means. The witness $d=54$ of
Theorem 417.3 does not propagate this way: $54(r-1)$ lies in $S(3)$ only
when $r$ is convenient for $54$, and $54\cdot(5-1)=216=\varphi(7\cdot37)$
shows that $r=5$ is not; the propagation Theorem 417.3 would need is the
exact-preimage clause of Ford's §7, which is Theorem 8 itself." Basis:
the grader's enumeration gives $216$ nineteen preimages ($247$, $259$,
$327$, $333$, $351$, $399$, $405$, $436$, $494$, $518$, $532$, $648$,
$654$, $666$, $684$, $702$, $756$, $798$, $810$), of which $259=7\cdot37$,
$247=13\cdot19$ and $436=4\cdot109$ are prime to $3$; $324=\varphi(652)$
with $652=4\cdot163$; $540=\varphi(541)$ with $541$ prime; among the
primes $5\le r<200$ only $r=79$ and $r=107$ give $54(r-1)\in S(3)$. The
2013 manuscript defines $n$ convenient for $d$ by "$d\varphi(n)$ is a
totient with preimages $n_1n,\dots,n_kn$ and no others", and Ford's §7
proof of Theorem 8 needs that $\varphi(b)d$ "has only the pre-images
$bm_i$"; the note's Proposition 3.1 and its proof use only that $ra$ and
$rb$ are preimages. Read with the propagation it follows, the sentence
asserts $54(r-1)\in S(3)$ for every prime $r\ge5$, which is false; read
as the bare collision, it says nothing about the property Theorem 417.3
uses. The Problem 694 review's required finding F1 with its suggested
finding F2 folded in, since the two clauses form one sentence.

**C8.** Page: the connections page. Location: the Problem 51 section,
"So the $S(k)$ device is capped at the ratio $2$ of $k=4$ unless a
modulus with two odd prime factors admits a witness, which no held source
or computation supplies: the computation of the Problem 417 section finds
no totient up to $10^7$ all of whose preimages are divisible by $6$,
$10$, $12$, $15$, $20$, $21$, $35$ or $45$, and
$\max_{v\le10^7}r(v)=2.0414$. In this range the least-preimage ratio does
not grow at all." Replace with: "So the $S(k)$ device is capped at the
ratio $2$ of $k\in\{2,4,8\}$ unless a modulus $k$ with $k/\varphi(k)>2$
admits a witness, that is, an even modulus with an odd prime factor (the
least are $6$, ratio $3$, and $10$, ratio $5/2$) or an odd modulus with
at least three distinct prime factors, small enough (the least is $105$,
ratio $35/16$; two odd primes give at most $15/8$). No held source or
computation supplies one. Moduli with two or three distinct odd prime
factors do admit witnesses in the sieve's range ($580$, with preimages
$649=11\cdot59$ and $1298$ only; $116964$, with preimages $3^3\cdot19^3$
and its double, ratio $19/12$; $103240$, with preimages $11\cdot59\cdot179$
and its double), but their primes are large, and up to $10^7$ the device
certifies at most $r\ge19/12$; the sieve of the Problem 417 section,
extended for this section, finds no totient up to $10^7$ all of whose
preimages are divisible by $6$, $10$, $12$, $15$, $20$, $21$, $35$ or
$45$, and $\max_{v\le10^7}r(v)=2.0414$. In this range the maximum ratio
moves only from $2.0355$ to $2.0414$ between $10^6$ and $10^7$." Basis:
on $S(k)$ the device certifies exactly
$r\ge k/\varphi(k)=\prod_{p\mid k}p/(p-1)$, a function of the distinct
primes of $k$; $15/\varphi(15)=15/8<2$ and an
odd modulus with two prime factors gives at most $15/8$, while
$6/\varphi(6)=3$, $10/\varphi(10)=5/2$ and $105/\varphi(105)=35/16$ exceed
$2$, so the page's condition is neither necessary nor sufficient. The
grader's sieve, complete for every preimage of every totient $v\le10^7$,
gives the preimage sets $\{649,1298\}$, $\{185193,370386\}$ and
$\{116171,232342\}$ of $580$, $116964$ and $103240$, so
$580\in S(11\cdot59)$, $116964\in S(3^3\cdot19^3)$ and
$103240\in S(11\cdot59\cdot179)$; $g(v)$ is odd for every totient
$v\le10^7$, takes $129005$ distinct values with two distinct prime factors
and $977$ with three, and $\max_vg(v)/\varphi(g(v))=19/12$; the eight
moduli and $105$ have no witness up to $10^7$; and $\max r$ is $2.0355$
at $10^6$ and $2.0414$ at $10^7$, so "does not grow at all" is false as
written. The moduli figure appears nowhere in the Problem 417 section's
computation paragraph, so it is attributed to the extended sieve. The
Problem 51 review's required findings F1 and F2, with its suggested F4
and its note F6 folded in.

**C9.** Page: the connections page. Location: the Problem 51 section,
"Next investigation", "A positive answer needs totients all of whose
preimages carry small prime factors without a common one, a structure
outside the $V(x;k)$ classification; the finite question whether some
totient has all preimages divisible by $15$ (or by $6$) is the natural
first test, and a segmented computation of $\max r(v)$ to
$10^9$–$10^{10}$ would show whether the ratio ever exceeds the level of
Ford's witnesses." Replace with: "A positive answer needs totients all of
whose preimages carry many small prime factors: either the preimages
share a divisor $k$ with many distinct prime factors, the $V(x;k)$
classification, where the witnessed moduli so far have $k/\varphi(k)\le2$,
or they do not, a structure outside that classification; the finite
question whether some totient has all preimages divisible by $6$ or by
$10$ (Ford's open cases) or by $105$, the least moduli with
$k/\varphi(k)>2$, is the natural first test, and a segmented computation
of $\max r(v)$ to $10^9$–$10^{10}$ would show whether $\max_{v\le x}r(v)$
grows with $x$ at all beyond its value $2.0414$ at $10^7$, and in
particular whether it reaches $5/2$ or $3$, the ratios a witness for $10$
or $6$ would force." Basis: if $r$ is unbounded, choose $v_K$ with
$r(v_K)>K$ and let $g_K$ be the greatest common divisor of the preimages
of $v_K$; either $\omega(g_K)$ is unbounded along a subsequence, which is
the $V(x;k)$ route, or it is bounded, in which case the shared part
contributes a bounded factor to every $m/\varphi(m)$ and the large ratio
comes from primes not shared by all preimages; the page asserts the
second branch as necessary without excluding the first, and nothing held
excludes it (Ford's remark on $k=6$ is stated as unproved and concerns one
modulus; composite moduli have witnesses, C8). Since $r(v)>K$ forces
$m/\varphi(m)=\prod_{p\mid m}p/(p-1)>K$ for every preimage $m$, "many
small prime factors" is what is established. A witness for $15$ would
certify only $r\ge15/8<2$ and would not lift the cap. "The level of
Ford's witnesses" is at most $2$ as an $S(k)$ level and at most
$r(2^{18}\cdot257)=257/128=2.0078\ldots$ (least preimage
$2^{11}\cdot257^2=135268352$) as a ratio, both below the section's own
$2.0414$, so the proposed computation's question is already answered. The
Problem 51 review's required finding F3 with its suggested F5 folded in.

**C10.** Page: the connections page. Location: the Problem 49 section.
(a) Target, "whose index names Problems 416 and 417 as leads." Replace
with: "whose index records the outcomes for Problems 416 and 417 and
points to its connections page and to the lead
distinct_totient_preimage_ratio." (b) Outcome, "No transfer; the shared
inputs are recorded, and the lead sentence of the Problem 49 index for 416
and 417 is answered by this page." Replace with: "No transfer; the shared
inputs are recorded." (c) The closing paragraph, "The Problem 49 folder
index no longer names 416 and 417 as bare leads; its
[[research/erdos_49/connections|connections page]] assesses them, reaching
the Problem 417 statements independently from Lemma 4.1 and pointing at the
lead distinct_totient_preimage_ratio as the single carrier of that route."
Replace with: "The Problem 49 folder's
[[research/erdos_49/connections|connections page]] assesses Problems 416 and
417, reaching the Problem 417 statements independently from Lemma 4.1 and
pointing at the lead distinct_totient_preimage_ratio as the single carrier
of that route." Basis: the Problem 49 index at the commit, in its
"Connections and leads" paragraph, names no lead for 416 or 417; it says
the Problem 417 route is carried by the lead
distinct_totient_preimage_ratio and that the transfers to 1003, 416, 694,
51, 821, 415, 850 and 931 are recorded with their outcomes on its
connections page. The Target and Outcome sentences are therefore false at
the commit, and the closing paragraph corrects them by a chronology ("no
longer"), which a retained page should not carry (`AGENTS.md` convention
3, Timelessness). The Problem 49 review's suggested finding F3, accepted
because two sentences are false at the reviewed commit.

## Rejected and downgraded findings

No finding is rejected as wrong: every finding was checked against the
page, the leads, the sources or the grader's computation and found right
in substance. The findings below are not accepted as corrections, for the
reasons given; "optional" means that the reviewer's replacement is
accurate and may be adopted, but that the page is not wrong without it.

**The Problem 417 review.** F4 (note), downgraded to optional: Ford's
Theorem 4 reads "If $\theta$ is admissible, $y\ge x^\theta$ and the
multiplicity $k$ is possible", and the page's paraphrase in Proposition
417.4's remark and the lead's (P1) drops "admissible"; the theorem is
cited as motivation only, and "for $y\ge x^\theta$" with $\theta$ unnamed
reads as "for suitable $\theta$"; inserting "for admissible $\theta$" is
exact. F5 (note), downgraded to optional: the held §5 of Maier and
Pomerance gives $V'(x)=(x/\log x)\exp\{(C+o(1))(\log\log\log x)^2\}$ for
their $V'$, the same growth type as their theorem for $V$ and not an
$\asymp$ statement, so "of the same order as $V$" overstates by the
$o(1)$ in the exponent; the remark is a notational warning outside every
proof, and "with the same growth type as $V$ in their theorem" is exact.
F6 (note), downgraded to optional: the "Consequently" of Proposition
417.2 depends on $\beta<\infty$, which the same sentence supplies under
(W); making the dependence explicit is a clarity edit. F7 (note),
retained as a note: the page retains no code for its exploratory
computation and states no rerun line; the figures were reproduced by the
reviewer and again by this grade, and the exploratory label stands. F8
(note), downgraded to optional: the grader checked the Problem 49
connections page at the commit, whose Proposition 2 gives the bounded
ratio and, in the paragraph after its proof, the cluster interval, whose
Proposition 3 gives the limit superior above $1$ from the seed
$2^{18}\cdot257$, and whose Proposition 4 gives the limit inferior above
$1$ under its window premise, named there (W) and identified with the
lead's (P1); the lead's cross-reference is accurate in substance, and only
the placement of the cluster interval is unstated; "with an explicit
limit" in the lead's next step reads as "with the limit expressed through
$G$", which is what (P2) gives.

**The general-scale review.** F4 (note), downgraded to optional: the
scale enters the two lemmas as a parameter that Lemma 416.1 and Lemma
416.2 generalize, and enters the family as a hypothesis only in (5); "uses
$c=2$ as a hypothesis on the family in exactly one place" is the exact
form. F5 (note), downgraded to optional: at $c=2$ Lemma 416.1 is the Lemma
2.1 page's Statement (the write-up's display (1)), and that page calls
its totient specialization the write-up's display (2); the sentence
"$c=2$ is that page's display (2)" names the specialization where the
general statement is meant, harmlessly. F6 (note), downgraded to
optional: Lemma 416.2 is used only for the fixed scale $c>1$ of its
section; "for real $c>0$" may be added. F7 (note), downgraded to optional:
"the single balance statement (5$_c$) for that family" is one statement
per $\varepsilon$-family, as Proposition 416.3 states, and "at that
standing" carries the identification of (3) and (4) with the declarations
on the write-up's word; both are wording. F8 (note), resolved: the
provenance clause "that Erdős posed with it" is supported by the held
Erdős (1979) paper, which closes with "It is not certain that there is a
genuine asymptotic formula for $\Phi(X)$ but perhaps
$\Phi(CX)/\Phi(X)\to C$ holds for every $C>0$", posing the general-scale
question beside the asymptotic-formula question of the catalog statement;
the 1974 passage on p. 201 has only the $c=2$ question; the section may
cite the 1979 paper for the clause.

**The Problem 821 review.** F1 (note), downgraded to optional: the
sentence's own reference to the pair map $f_y(b,p)=b(p-1)$ fixes the
families it means; "for every family of such pairs" is exact. F2
(suggested), downgraded to optional: the section's "top prime" is the
write-up's term, a prime exceeding every prime of the record and hence
not dividing $m/p$, so under the page's convention the collapse sentence
is right; the reviewer's witness $t=6$, $m=9$, $m'=18$ shows what the
sentence would say of an arbitrary preimage whose largest prime factor
divides it twice, which is not a pair of the family at all, and the
conclusion (at most $d(t)+\omega(t)$ pairs for the whole fiber) survives
under either reading; the replacement is exact and may be adopted. F3
(note), downgraded to optional: $\delta=0.2961$ is the source's
$\beta$ and Corollary 1 gives more than $m^{0.7039}$ preimages; the page
leaves $\delta$ unnamed and relies on the exponents only through
"exceeds $t^{0.7}$", which both corollaries support. F4 (note), rejected
as a defect: the grader read the Problem 821 page at the commit, whose
Current assessment says "No current assessment is recorded" and that the
page "records no current literature search or independent assessment of
proof coverage", its Progress and Known Results paragraphs recording
author-recorded transfers from research folders; the connections page
uses "compiled" for literature compilation throughout (the Problem 417
section says "no compiled progress" of a page that also carries a
Progress paragraph), so "the page is not compiled" is right in the page's
sense. F5 (note), downgraded to optional: a uniform upper bound
$g\le1$ would imply (4) and is false for every odd prime, so "neither
implying nor implied by a bound on $g$" holds for every bound that
exists; "neither yielding a lower bound for $g$ nor contradicted by one"
is the intended sense.

**The Problem 694 review.** F3 (suggested), downgraded to optional: "the
object of Problem 417" reads as that problem's subject matter, least
preimages measured against values, and the sentence points at the Problem
417 section, whose pair-family bullet records the exact relation (a
typical bound gives only $R\ll1$); read strictly the two clauses
conflict, and the replacement, which names what Problems 417 and 51 ask,
is exact. F4 (note), downgraded to optional: the 2013 manuscript
attributes the convenient-number observation and the almost-all-primes
theorem to Erdős and proves its Lemma 4.1 by Ford's methods, and Ford's
§7 uses the device for Theorem 8; "the shared device is Ford's" names the
use the page cites, and "Erdős's, as Ford's Theorem 8 and the 2013
manuscript use it" is exact. F5 (note), downgraded to optional: the
constant is $2K(\varepsilon)$ in the Problem 417 section and
$K(\varepsilon)$ here, neither specified; the $\varepsilon$-proportion's
range is all but $(\varepsilon+o(1))V(y)$ of the totients $v\le y$ for
large $y$; and the premise set beyond the record bound is carried by the
pointer to the Problem 417 section; the replacement is exact. F6 (note),
downgraded to optional: the link labeled "Theorem 2.1 on its card"
resolves to the note's result page `theorem_2_1`; "on its result page"
is exact. F7 (note), downgraded to optional: the estimates (3)–(5)
tolerate an exceptional set of $\varepsilon V(y)+o(V(y))$ values and do
not average; the grader re-derived the reviewer's bound that the totients
$n\le x$ with fiber ratio at least $c\log\log x$ number
$O(x\exp(-(\log x)^{c'}))$ for some $c'>0$, through $M\le2n^2$ for the
largest preimage $M$, Mertens' bound for $M/\varphi(M)$ and the count of
integers with many distinct prime factors, so the extreme fibers lie
inside the exceptional allowance; "average away" is loose and the
replacement is exact.

**The Problem 51 review.** F7 (note), downgraded to optional: "many prime
factors" should read "many distinct prime factors", since $k/\varphi(k)$
depends only on the distinct primes of $k$, and "and at $k=11$" is
redundant after "at the prime powers". F8 (note, from exposed text),
rejected as a defect on the ground given for the Problem 821 review's F4:
the Problem 51 page at the commit records no current assessment and no
literature search; its Progress paragraph paraphrases this section and
its Known Results paragraph records the Problem 49 folder's failed
transfer, both author-recorded transfers, so "not compiled beyond Guy's
B36 form" is right in the page's sense of compilation.

**The Problem 49 review.** F1 (suggested), downgraded to optional: the
Theorem 1.2 page's input (C) is "$W(x)\asymp Z(x)$", used only through
$x/\log x=o(W(x))$, while (W) on the connections page is
$V(x)\asymp V'(x)$; both are clauses of the one p. 7 sentence
"$V(x)\asymp W(x)\asymp Z(x)$" and are equivalent under (F), so "the same
input (W)" names the shared source sentence; the replacement, which says
which clause each page consumes and at what strength, is exact. F2
(suggested), downgraded to optional: "Lemma 4.1(iii) ..., $n/\varphi(n)$
bounded on Ford's candidate set with two counts imported from Ford's §5"
names clause (iii), which that page proves, and the two imported counts,
which supply clauses (i) and (ii); the grader re-derived the bridge (the
Problem 49 connections page's Proposition 2): with the seed $d_1=d_2=1$
and $D=K$, clause (ii) makes $n\mapsto\varphi(n)$ injective on the
supplied set, clauses (i) and (iii) put $n\le x$, and (F) supplies
$V\le C_1Z$; the sentence does not say that (ii) carries the injectivity
or that (F) closes the last step, and naming Proposition 2 would help,
but nothing it says is false. F4 (note), downgraded to optional: $S(4)$
occurs in Remark (ii) after Theorem 417.3, not in the theorem; "of Remark
(ii) to Theorem 417.3" is exact.

**The shifted-collisions review.** F1 (suggested), downgraded to
optional: the sentence's three stated reasons (no rate, no reference to
$k$, summed over all values) are true features of (4) and support "does
not bound $P(x;k)$"; the primary reason the reviewer supplies, that
$P(x;k)$ counts arguments of every shape while (4) sees only the pair-form
arguments and bounds even that part only by $o(V(x))$, is a completion
and may be adopted. F2 (suggested), downgraded to optional: the grader
checked the Problem 1004 page at the commit, which records Theorem 3.1
with its range $k\le\exp((\log x)^{1/3})$ and Theorem 3.3 with its
$c(k)$ bound for even $k\le x^{\varepsilon(x)}$, whose combination is the
manuscript's sentence "$\ll x/(\log x)^2$, uniformly for $k\le\log x$"
in its proof of Theorem 1.2; "records at" is loose for an upper bound,
and the replacement is exact. F3 (note), downgraded to optional: the
qualifier "only when the pairs differ" is vacuous for $k\ge1$, since one
record per core makes equal pairs give $k=0$. F4 (note), downgraded to
optional: the fibers of $f_y$ run over the retained values, which the
write-up keeps above $y^{99/100}$; "summed over the fibers of $f_y$" is
exact. F5 (note), downgraded to optional: the block of Problem 1004
starts at some $n\le x$ and may end above $x$; for the every-$c$ question
the readings agree. F6 (note), downgraded to optional: the lead's
criterion is stated for the scaled partial sum $\Phi_N$ and passes through
the tail integers; "partial and tail sums" is exact. F7 (note), retained
as a note: the native-note lead names a sibling lead on distinct totient
blocks from collision bounds, outside the review's read set; the
obstruction applies to any lead built on consecutive distinctness, so the
outcome is unaffected.

## Graded verdicts

**Problem 417: the two counts of distinct totients** (statements as the
Problem 417 review numbers them). S1, Lemma 417.1: refutation-failed; the
grader re-derived (a) from $\varphi(m)\le m$, (b) from the primes, and
(c) as $|R(n+1)-R(n)|\le A/B^2\le n/B^2$, within the page's bound. S2,
Proposition 417.2: refutation-failed under (W), which the statement
lists; the crossing argument was re-derived with the threshold
$n_0\ge e^2$ that the page omits harmlessly. S3, Theorem 417.3:
refutation-failed; the grader re-derived Steps 1–5, the witness
$\varphi^{-1}(54)=\{81,162\}$ by enumeration, the scale sum with
$C_1=2^{1+K'}e^{2K}$ under the derivative bound on its proved range (C1),
and the contradiction with $\eta=c/(6C_1)$. S4, Proposition 417.4:
refutation-failed as a conditional on its stated premise. S5(a), the
pair-family upper bound: refutation-failed; S5(b) is not a claim. S6(a),
the frame's deduction without a support bound: refutation-failed; S6(b),
the support clause $G(t)=1$ for $t\ge2$ and the upper limit $2$:
refuted-as-stated, corrected by C2. S7(a), the finite-range numbers:
refutation-failed, every figure reproduced; S7(b), the sentence placing
every element of $V_0(x)$ in $(x/2,x]$: refuted-as-stated, corrected by
C3. S8, the lead's route, inputs, premises and gap: refutation-failed,
with its cross-reference to the Problem 49 connections page checked by
the grader.

**Problem 416 at a general scale** (statements as the general-scale
review numbers them). S1, the target and its provenance:
refutation-failed, the clause "posed with it" now supported by Erdős
(1979). S2, Lemma 416.1, and S3, Lemma 416.2: refutation-failed, both
re-derived. S4, Proposition 416.3: refutation-failed as a conditional
from (3), (4) and (5$_c$); the grader re-derived Step 4 with
$\kappa=\max(1,c-1)$ and the choice $\varepsilon<\min(1/2,\delta/(2\kappa))$.
S5, the scale-free remark: refutation-failed. S6, the second remark:
refutation-failed under the interval reading of its hypothesis, whose
wording C5 corrects. S7, the block mean, and S8, $\alpha_c\beta_c=2$:
refutation-failed, both re-derived. S9, no formula, no rate, no prose
proof: refutation-failed. S10, the dichotomy and the interval stand for
every $c\ne2$: refuted-as-stated, witness $c=4$, corrected by C4. S11,
the positive outcome: refutation-failed. S12, the negative outcome: not a
claim, its wording corrected by C6. S13, the standing sentences:
refutation-failed.

**Problem 821: large fibers versus repeated representations** (as the
Problem 821 review numbers them). S1, the target and literature chain:
refutation-failed, the corollaries checked at the held sources. S2, the
content of (4): refutation-failed. S3, the fiber bound
$|f_y^{-1}(t)|\le\#\{p:p-1\mid t\}\le d(t)$: refutation-failed,
re-derived. S4, $g(t)>t^{0.7}$ infinitely often: refutation-failed. S5,
the collapse: refutation-failed under the write-up's convention for the
top prime. S6, the obstruction: refutation-failed. S7, Ford's Theorem 2
against (4): refutation-failed. S8, the route on the problem page:
refutation-failed. S9, the outcome: not a claim.

**Problem 694: the extreme fiber ratio** (as the Problem 694 review
numbers them). S1, the target, and S2, the status characterization:
refutation-failed, the latter checked against the problem page. S3, the
obstruction: refutation-failed. S4, the conditional typical-ratio
statement: refutation-failed as a conditional. S5, no catalog problem asks
it: refutation-failed for Problems 417, 51 and 694. S6, the pointer to
Problem 417: not a claim. S7, Proposition 3.1 and its identification with
the convenient-integer device: refutation-failed for the proposition,
with the identification corrected by C7. S8, the witness $54$ propagates
the same way: refuted-as-stated, witness $216=\varphi(259)$, corrected by
C7. S9, the outcome: refutation-failed for "no bearing" and "not the
reconstructions'".

**Problem 51: the least-preimage ratio** (as the Problem 51 review
numbers them). S1, the target: not a claim. S2, the reformulation, S3,
what the pair family gives, S4, the $S(k)$ lower bound, S5, the route
restriction, and S6, the account of Ford's §7 with the Carmichael
parenthetical: refutation-failed, each re-derived. S7, the cap sentence:
refuted-as-stated, corrected by C8. S8, the finite-range figures:
refutation-failed, every figure reproduced. S9, the necessity sentence:
proof defective; statement unresolved, corrected by C9. S10, the proposed
computation: not a claim, its question corrected by C9. S11, the
negative-answer confinement: refutation-failed. S12, the outcome: not a
claim.

**Problem 49 and the monotone-set reconstructions** (as the Problem 49
review numbers them). S1, the target: refutation-failed. S2, the
obstruction: refutation-failed. S3, $W=V'$, and S4, the third count:
refutation-failed, the witness $x=6$ checked. S5, the shared input:
refutation-failed under the reading that (W) names the p. 7 sentence. S6,
the reversed pair, and S7, $d_1\in S(4)$: refutation-failed, both
preimage sets enumerated by the grader. S8, the route through Lemma 4.1:
refutation-failed, the bridge re-derived. S9, the index bookkeeping:
refuted-as-stated at the commit, corrected by C10. S10, the closing
paragraph's characterizations: refutation-failed, its chronology
removed by C10.

**Shifted collisions: Problems 1003 and 1004 and the two totient leads**
(as the shifted-collisions review numbers them). S1 through S8:
refutation-failed; the grader checked the three problem statements, the
manuscript's sentence in its proof of Theorem 1.2, and the witnesses
$\varphi(13)=\varphi(28)=12$, $\varphi(37)=\varphi(76)=36$ and
$\varphi(61)=\varphi(124)=60$.

**The leads.**

- [[research/leads/distinct_totient_preimage_ratio/_index|distinct_totient_preimage_ratio]]:
  reviewed. Its route rests on Lemma 417.1, Proposition 417.2 (with (W)
  or the Problem 49 folder's route for the finite upper endpoint) and
  Theorem 417.3, all refutation-failed; on Proposition 417.4 as a
  conditional under (P1); on the frame as the lead states it, without the
  support clause, which is the refutation-failed S6(a); and on the
  finite-range numbers, reproduced. The two refuted sentences of the
  section, S6(b) and S7(b), are not carried by the lead, and the
  imported-input misquotation C1 has no effect on the proofs. No
  correction changes the lead's text.
- [[research/leads/general_scale_totient_doubling/_index|general_scale_totient_doubling]]:
  reviewed, with corrections C4, C5 and C6 applying to its text. Its
  route rests on Lemma 416.1, Lemma 416.2, Proposition 416.3 and the
  scale-free remark, all refutation-failed, with (5$_c$) an explicit
  premise and the second remark its plausibility argument,
  refutation-failed under the interval reading that C5 writes out. The
  refuted sentence S10 sits in the lead's "Consequential gap" as a
  description of what remains without the premise, not as a step of the
  route; C4 corrects it, and the lead's positive next step is unchanged.

No tier is assigned and no status changes.

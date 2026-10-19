---
name: research/erdos_49/evidence/verify/connections_problem_821_totients_of_very_large_multiplicity_review
title: "Independent review of the connections section: Problem 821: totients of very large multiplicity"
desc: |
  Refutation-failed for all four statements of the section: the target
  restatement, the multiplicity-preserving transfer identified with Ford's
  Theorem 2, the obstruction, and the failed outcome. Zero required
  corrections; two suggested additions and three notes.
created: 2026-09-28T18:19:29Z
updated: 2026-09-28T18:19:29Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context, commissioned for
refutation, who took no part in writing the connections page or any page of
the folder. The writer of the section is called the author below.

**Subject.** Page `wiki/research/erdos_49/connections.md` as it stood on
2026-09-28T13:50:48Z, section "## Problem 821: totients of very large
multiplicity", lines 542--561 (the H2 heading at line 542 through the blank line
561; the next H2 is at line 562). The section names no lead page; the page's
"Outcomes at a glance" lists Problem 821 among the failed transfers and carries
no lead for it.

**Independence facts.** The reviewer was given only this assignment, read
the subject in the pinned state through read-only git, ran no generator
and no gate, and wrote nothing but this report. Not read: the folder's
`_index.md`; anything under the folder's `evidence/` (the grade and the six
reconstruction reviews); the Current assessment, Progress, Known Results and
Linked library material sections of the problem page; any other section's
review; anything among the private working files; the web.

**Read set and depth.**

- The section, lines 542--561, clause by clause; the page's shared parts,
  lines 1--111 (frontmatter, introduction, Standing, Outcomes at a glance,
  Notation and the inputs used), read as inputs whose interfaces were
  confirmed at each use.
- [[research/erdos_49/lemma_5_1_reconstruction|Lemma 5.1 page]],
  [[research/erdos_49/lemma_4_1_reconstruction|Lemma 4.1 page]] and
  [[research/erdos_49/theorem_1_2_reconstruction|Theorem 1.2 page]], each
  in full, as premises at their recorded standing.
- [[problems/arithmetic_functions/E0821/_index|Problem 821]]: the unheaded
  statement body only (statement, status line, source line, reference list,
  formalization pointer); the later headings were seen in a heading listing
  and their content was not read.
- [[../library/arithmetic_functions/ford_1998_distribution_totients/_index|Ford (1998)]]:
  the whole card (it has no result pages), and the held PDF: pp. 1--5 on
  the text layer, pp. 2--3 on the page images (Theorem 2 and the paragraph
  on multiplicities $A(m)\ge m^{c_4}$), pp. 24--26 on the text layer (the
  lower-bound argument for Theorem 2), and reference entries [1], [8], [10].
- [[../library/primes/pollack_et_al_2013_sets_monotonicity_euler_totient_function/_index|Pollack, Pomerance and Treviño (2013)]]:
  the whole card and the whole
  [[../library/primes/pollack_et_al_2013_sets_monotonicity_euler_totient_function/theorem_1_2|Theorem 1.2 result page]];
  the held author manuscript: p. 2 and p. 8 on the page images (the
  definition of a convenient integer; Lemma 4.1), pp. 8--9 on the text
  layer (the proof of Lemma 4.1 and Lemma 5.1).
- Guidance: `docs/verification.md` sections "Grading and claim standing",
  "Audit checklist" (shared and Erdos-specific) and "Whole-claim report";
  `docs/approach_vetting.md`; `docs/evidence.md` "Source fidelity";
  `docs/math_authoring.md`.

**Exposures.** Three, all names or headings rather than content: (1) a
tree listing of the folder showed the filenames under `evidence/verify/`
(the grade and six reconstruction reviews), none opened; (2) a heading
listing of the problem page showed its four later section titles, none
opened; (3) working-tree status listings showed filenames of untracked
reviews of other sections of this page and of other research folders, none
opened. Beyond the allowed "provenance paragraphs and statement sections",
the two library cards and the Theorem 1.2 result page were read whole; none
of that text is standing, acceptance or assessment text.

## Restatement

Conventions: $\varphi$ is the totient function; a totient is a value of
$\varphi$; the preimages of a totient $v$ are the integers $m$ with
$\varphi(m)=v$, and their number is the multiplicity of $v$, written $A(v)$
by Ford and $g(v)$ by the problem page. $V(x)$ counts the totients in
$[1,x]$, $V_k(x)$ those with multiplicity $k$, and $Z(x)$ is Ford's
function as defined on the Theorem 1.2 page. An integer $n$ is convenient
for a totient $d$ with preimages $n_1,\ldots,n_k$ when $d\varphi(n)$ is a
totient whose preimages are exactly $n_1n,\ldots,n_kn$.

- **S1 (target).** Problem 821 asks: for every $\epsilon>0$, are there
  infinitely many $n$ with $g(n)>n^{1-\epsilon}$? The quantifier order is
  "for every $\epsilon$, infinitely many $n$", and the problem's status is
  open. The section adds two bibliographic sentences: the corpus page is
  compiled no further than its statement, and the known results the page
  references come from shifted primes without large prime factors.
- **S2 (what transports).** (a) For every totient $d$ of multiplicity $k$
  and every $n$ convenient for $d$, the totient $d\varphi(n)$ has
  multiplicity exactly $k$. (b) Consequently, for every $k$ that is the
  multiplicity of some totient $d$, there are $c_d>0$ and $x_0(d)$ with
  $V_k(x)\ge c_dV(x)$ for all $x\ge x_0(d)$: each attained multiplicity is
  attained on a positive proportion of the totients. (c) Statement (b) is
  Ford's Theorem 2 and is recorded on the Ford card.
- **S3 (obstruction).** (a) The convenient-integer construction preserves
  multiplicity exactly: the preimage set of $d\varphi(n)$ is
  $\{n_1n,\ldots,n_kn\}$. (b) Hence the construction cannot produce a
  totient whose multiplicity exceeds that of its seed, so witnesses for
  Problem 821 must come from a different mechanism, which the section
  describes as many primes $p$ with $p-1$ dividing one fixed smooth number.
- **S4 (outcome).** Neither mechanism of the reconstruction (the uniform
  collision bounds (T1), (T3) and the convenient-integer construction (L4))
  transfers anything to Problem 821: the connection fails.

## Checklist

- **Quantifiers and scope.** Pass. S1 keeps the problem page's order (for
  every $\epsilon$, infinitely many $n$). S2(b) is per multiplicity, with a
  constant and threshold depending on the seed $d$, which is what Ford's
  Theorem 2 provides ($x\ge x_0(d)$); "positive proportion" is a bound for
  all large $x$, not a limit inferior statement in disguise. S3(a) holds
  for every convenient $n$ without exception, being the definition.
- **Circularity.** Pass. The deduction in S2 rests on Lemma 4.1 and on
  Ford's Theorem 1 through (F), neither of which is equivalent to S2(b);
  S3(a) is definitional.
- **Model and convention changes.** Pass. The problem page's $g(n)$, Ford's
  $A(m)$ and the page's "preimages" are the same object. "Convenient" is
  the definition of the source's p. 2, reproduced on the Lemma 5.1 page and
  in the page's Notation. The proportion is stated against $V(x)$; the
  construction counts against $Z(x)$, and (F) supplies $V(x)\le C_1Z(x)$.
- **Finite and statistical overreach.** Pass. The section uses no finite
  computation; the explicit pair (P) of the page's inputs is not consumed
  here.
- **Uniformity.** Pass, with note F4. No uniformity in $k$ or $d$ is
  claimed; the constants of S2(b) depend on $d$, as in Ford's Theorem 2.
- **Extremal conclusions.** Pass. The only exact-value sentence is the
  multiplicity equality of S2(a) and S3(a), which is the definition of
  convenience; the products $n_in$ are distinct because the $n_i$ are.
- **Consequences and composition.** Pass, with finding F1. The "so" of
  S2(b) composes Lemma 4.1 (whose two counting steps are imported from
  Ford's paper and not reconstructed) with (F); the section asserts nothing
  beyond the published Theorem 2, to which it attributes the statement.
- **Computation.** Inapplicable: the section computes nothing.
- **Reproduction.** Inapplicable: the section carries no rerun line and no
  coverage claim.
- **Source and verdict fidelity.** Pass. Theorem 2 was checked on the page
  image of Ford's p. 2; the definition of convenience on the manuscript's
  p. 2 image; Lemma 4.1 on its p. 8 image; the card's transcription of
  Theorem 2 matches the source. The section carries no standing sentence of
  its own, and the page's Standing records everything as author-recorded.

## Weakest steps

**W1: the "so" of S2(b), re-derived from the page's inputs.** Let $d$ be a
totient with preimages $n_1<\cdots<n_k$. Lemma 4.1 admits $d_1=d_2=d$ and
$D=d$, since nothing in its statement requires $d_1\ne d_2$ and
$D\ge\max\{d_1,d_2\}$ holds with equality. It gives $c_d>0$ and $x_0(d)$
such that for $x\ge x_0(d)$ at least $c_dZ(x)$ integers $n$ satisfy
$\varphi(n)\le x/d$ and are convenient for $d$. For each such $n$,
$v_n=d\varphi(n)\le x$ is a totient with exactly $k$ preimages by S2(a). The
map $n\mapsto v_n$ is injective on these $n$: if $v_n=v_{n'}$, the two
preimage sets $\{n_in\}$ and $\{n_in'\}$ coincide, so their least elements
coincide, $n_1n=n_1n'$, and $n=n'$ (the Lemma 5.1 page's Step 1 uses the
same device). Hence $V_k(x)\ge c_dZ(x)$, and by (F), $V(x)\le C_1Z(x)$ for
$x\ge x_1$, so $V_k(x)\ge(c_d/C_1)V(x)$ for $x\ge\max\{x_0(d),x_1\}$. The
step composes correctly with the surrounding argument; it inherits Lemma
4.1's imported counting steps (F1), (F2), which the section covers by
citing the published theorem rather than by claiming a proof.

**W2: the obstruction S3(b) blocks the target.** Fix $\epsilon>0$. Let
$v=d\varphi(n)$ with $n$ convenient for $d$, and suppose $v$ is a witness,
$g(v)>v^{1-\epsilon}$. Then $g(d)=g(v)>v^{1-\epsilon}\ge d^{1-\epsilon}$
because $\varphi(n)\ge1$, so the seed $d$ is already a witness for the same
$\epsilon$. Moreover a fixed seed yields only finitely many witnesses,
since $g(d)>(d\varphi(n))^{1-\epsilon}$ forces
$\varphi(n)<g(d)^{1/(1-\epsilon)}/d$. So infinitely many witnesses from the
construction require infinitely many seeds that are witnesses themselves:
the construction cannot lower the exponent, and if every totient $d$
satisfies $g(d)\le d^{1-\epsilon_0}$ then so does every output. Iterating
the construction changes nothing, because the multiplicity is invariant
under it. The obstruction therefore defeats the implication "the
construction yields Problem 821 witnesses" at that implication's own
hypotheses.

**W3: the identification with Ford's Theorem 2 and the mechanism
parenthetical.** Ford's p. 2 states, immediately before Theorem 2, that "if
there exists $m$ with $A(m)=k$, then a positive proportion of totients have
multiplicity $k$", and Theorem 2 reads: for every $\varepsilon>0$, if
$A(d)=k$ then $V_k(x)\gg_\varepsilon d^{-1-\varepsilon}V(x)$ for
$x\ge x_0(d)$. Ford's proof (pp. 24--25) takes the candidate set $B$ of
integers $n=p_0\cdots p_L$ with $\varphi(n)\le x/d$ and $p_L\ge\max(d+2,17)$,
the same set as Lemma 4.1's with $D=d$, calls $n_1=nd_i$ the trivial
solutions of $d\varphi(n)=\varphi(n_1)$, and records $A(d\varphi(n))=\kappa$
for each $n\in B$ without a nontrivial solution, that is, for each
convenient $n$; the count of the others is bounded by half of $B$. So the
mechanism the section names is exactly the mechanism of Theorem 2. Ford's
p. 3 attributes the existence of infinitely many totients with
$A(m)\ge m^{c_4}$ to Erdős's 1935 paper (his [8], the problem page's
[Er35b]) and the record $c_4=0.7039$ to his [1], whose title is "Shifted
primes without large prime factors", and states that Erdős conjectured
every $c_4<1$ admissible, which is Problem 821. This is consistent with the
section's characterization of the known results.

## Strongest attack

- **S1.** Tried a quantifier mismatch (the problem asking for infinitely
  many $n$ that work for every $\epsilon$, or for a single $\epsilon$). The
  problem page reads "for every $\epsilon>0$, there exist infinitely many
  $n$", exactly the section's order. Tried a mismatch in the object counted
  ($g(n)$ against the section's "preimages"): they coincide. Failed. The
  bibliographic sentences were checked as far as the read set allows (note
  F3).
- **S2.** Tried to break the "so" at four points: distinctness of the
  totients $d\varphi(n)$ (settled by the least preimage, W1); the use of
  Lemma 4.1 with $d_1=d_2$ and $D=d$ (within its hypotheses); a proportion
  of $Z(x)$ mistaken for a proportion of $V(x)$ (bridged by (F)); and the
  multiplicity $k=1$, where the seed would be a counterexample to the
  conjecture that no totient has multiplicity 1 (Ford's Theorem 2 covers
  every $d$, and Ford's Theorem 5 is his own reading of that case). Tried
  to catch a misquotation of Theorem 2 on the page image: the section's
  sentence is Ford's own qualitative gloss. Failed.
- **S3.** Tried three ways around the obstruction. (i) The non-convenient
  elements of Ford's candidate set: for such $n$ the totient $d\varphi(n)$
  has the $k$ trivial preimages $n_in$ (coprimality holds because every
  prime $p$ dividing a preimage of $d$ has $p-1\mid d$, so $p<p_L$) and at
  least one more, so its multiplicity exceeds $k$; but the mechanism only
  bounds the number of such $n$ from above and gives no lower bound on the
  excess or on how many there are, while the target needs a multiplicity
  above $(d\varphi(n))^{1-\epsilon}$; nothing follows. (ii) Seeds growing
  with $x$: the output multiplicity is still $g(d)$, so W2 applies
  verbatim, uniformity or not. (iii) Iteration: multiplicity is invariant.
  Failed. The parenthetical mechanism description was tested against
  Ford's p. 3 and the reference titles and stands as a description.
- **S4.** Tried to make the first mechanism transfer. Let $v$ be a totient
  with $g=g(v)$ preimages; every preimage $m$ satisfies
  $m=v\cdot m/\varphi(m)$, so all lie in $[1,x]$ with $x\ll v\log\log v$ by
  the elementary bound $m/\varphi(m)\ll\log\log m$. Split $[1,x]$ into
  blocks of $\lfloor\log x\rfloor$ consecutive integers; a block holding
  $r$ preimages holds $r-1$ pairs $(m,m+k)$ with $1\le k\le\log x$ and
  $\varphi(m)=\varphi(m+k)$, each counted once by $P(x;k)$. The Theorem 1.2
  page's (B), deduced there from (T1) and (T3), gives
  $\sum_{k\le\log x}P(x;k)\le Bx/\log x$, while the pairs number at least
  $g-x/\lfloor\log x\rfloor-1$; hence $g(v)\ll v\log\log v/\log v$. That is
  an upper bound, far weaker than the unconditional bound the source quotes
  on its p. 2 (the maximal multiplicity up to $x$ is at most
  $x/L(x)^{1+o(1)}$ with $L(x)=\exp(\log x\log_3x/\log_2x)$), and the target
  asks for a lower bound. Nothing transfers. Failed.

## Premises

- **Lemma 4.1** ([[research/erdos_49/lemma_4_1_reconstruction|page]],
  read in full; source Lemma 4.1, manuscript p. 8, held, statement read on
  the page image and proof on the text layer). Interface: fixed totients
  $d_1,d_2$ and fixed $D\ge\max\{d_1,d_2\}$; an absolute $K$; constants
  $c_D>0$ and $x_0(D)$ with at least $c_DZ(x)$ integers $n$ satisfying
  $\varphi(n)\le x/D$, convenience for $d_1$ and $d_2$, and
  $n/\varphi(n)\le K$, for $x\ge x_0(D)$. Standing: author-recorded partial
  reconstruction; its counting steps (F1), (F2) are imported from Ford's
  paper. Used here with $d_1=d_2=D=d$, within the hypotheses.
- **Lemma 5.1 page** ([[research/erdos_49/lemma_5_1_reconstruction|page]],
  read in full). Used for the definition of convenience and for the
  injectivity device (least preimage); its explicit pair is not consumed.
- **Theorem 1.2 page**
  ([[research/erdos_49/theorem_1_2_reconstruction|page]], read in full).
  Used for the definition of $Z(x)$ and, in the attack on S4 only, for its
  deduction (B): $P(x;k)\le Bx/(\log x)^2$ for $x\ge x_1$ and $k\le\log x$.
- **(F)** Ford's Theorem 1 as recorded in the page's inputs, used only as
  $V(x)\le C_1Z(x)$ for large $x$; the theorem's statement was read on
  Ford's p. 2 image, its proof not read.
- **Ford's Theorem 2** (card
  [[../library/arithmetic_functions/ford_1998_distribution_totients/_index|Ford (1998)]],
  held PDF): statement on p. 2 (page image); the proof's mechanism on
  pp. 24--25 (text layer); the p. 3 paragraph on $A(m)\ge m^{c_4}$ (page
  image); references [1], [8], [10] (text layer). The card's transcription
  of Theorem 2 matches the source.
- **The source's definition of convenience** (card
  [[../library/primes/pollack_et_al_2013_sets_monotonicity_euler_totient_function/_index|Pollack, Pomerance and Treviño (2013)]],
  held author manuscript, p. 2 page image), including its attribution of
  the "almost all primes are convenient" result to Erdős. The card's
  provenance paragraph records the manuscript's origin and byte count.
- **Problem 821** ([[problems/arithmetic_functions/E0821/_index|page]]): the
  statement body only, read clause by clause.
- No batch acceptance order applies; no computation was run.

## Findings

- **F1 (suggested).** Location: lines 550--552, "For convenient $n$ the
  multiplicity of $d\varphi(n)$ equals that of $d$, so each attained
  multiplicity is attained on a positive proportion of totients". Defect:
  the "so" is a transfer whose bridge is not written: Lemma 4.1 with
  $d_1=d_2=D=d$, the injectivity of $n\mapsto d\varphi(n)$ on convenient
  $n$, and (F). Witness: none; the bridge is valid and re-derived in W1.
  Proposed replacement: "...equals that of $d$; Lemma 4.1 with
  $d_1=d_2=D=d$ supplies $\ge c_dZ(x)$ convenient $n$ with
  $d\varphi(n)\le x$, distinct because the least preimage $n_1n$ determines
  $n$, so by (F) each attained multiplicity is attained on a positive
  proportion of totients, the proportion depending on $d$; this is Ford's
  Theorem 2, already on the Ford card."
- **F2 (suggested).** Location: lines 550--560, the section as a whole
  against the page's introduction, which follows two mechanisms. Defect:
  the section dismisses only the convenient-integer construction and says
  nothing about the collision bounds (T1), (T3), so the outcome "Fails" is
  argued for one of the two mechanisms. Witness: the derivation under S4 in
  the Strongest attack, which shows the collision bounds yield only the
  upper bound $g(v)\ll v\log\log v/\log v$. Proposed addition after the
  obstruction paragraph: "The collision bounds are upper bounds on
  coincidences $\varphi(n)=\varphi(n+k)$ at shifts $k\le\log x$; on a
  multiplicity they give at most $g(v)\ll v\log\log v/\log v$, weaker than
  the known unconditional bound, and the target asks for a lower bound, so
  they transfer nothing."
- **F3 (note).** Location: lines 546--548, "The corpus page is not compiled
  beyond the statement (open); the known results it references come from
  shifted primes without large prime factors." Defect: none found; the
  sentence characterizes content outside this review's read set (the
  problem page's later sections). Checked within the read set: the
  statement body's status line reads Open; the references [BaHa98] and
  [Li22] carry "shifted primes without large prime factors" in their
  titles; Ford's p. 3 attributes $A(m)\ge m^{c_4}$ to the 1935 paper of
  [Er35b] and the record exponent to [BaHa98]. The reference [LuPo11], by
  its title, concerns an arithmetic function arising from the conjecture on
  multiplicity 1 and is not a shifted-prime result. Proposed: none
  required; if the page's Known Results section reports [LuPo11], write
  "the lower bounds it references".
- **F4 (note).** Location: lines 551--552, "a positive proportion of
  totients; this is Ford's Theorem 2". The proportion depends on the seed:
  Theorem 2 reads $V_k(x)\gg_\varepsilon d^{-1-\varepsilon}V(x)$ for
  $x\ge x_0(d)$, and the section's sentence is Ford's own qualitative gloss
  from the same page. No uniformity is claimed, so nothing is wrong.
  Proposed: optionally add "with a constant depending on $d$".
- **F5 (note).** Location: lines 554--556, "The construction never
  increases a multiplicity: the preimages of $d\varphi(n)$ are exactly the
  $k$ products $n_in$." Exact for the construction's output, the convenient
  $n$. Ford's candidate set, the same set as Lemma 4.1's with $D=d$, also
  contains non-convenient $n$, for which $d\varphi(n)$ has the $k$ trivial
  preimages and at least one more; the mechanism discards them by an upper
  bound on their number and gives no lower bound on their excess
  multiplicity, so they yield nothing for the target either. Proposed: none
  required.

## Verdict

- **S1:** refutation-failed. The restatement matches the problem page's
  statement in quantifier order and in the object counted; the two
  bibliographic sentences are consistent with the statement page and with
  Ford's p. 3 and were not checked further (F3).
- **S2:** refutation-failed. S2(a) is the definition of convenience; S2(b)
  follows from Lemma 4.1 with $d_1=d_2=D=d$, the least-preimage injectivity
  and (F), as re-derived in W1; S2(c) matches Ford's Theorem 2 on the page
  image and the card's transcription.
- **S3:** refutation-failed. The obstruction is exact for every convenient
  $n$, and it defeats the implication it is set against at that
  implication's own hypotheses (W2); the three ways around it fail.
- **S4:** refutation-failed. Neither mechanism transfers: the construction
  by W2, the collision bounds because they yield only an upper bound on a
  multiplicity (Strongest attack, S4); the section argues only the former
  (F2).

**Limitations.** S2(b) rests on Lemma 4.1, whose two counting steps are
imported from Ford's paper and not reconstructed in the folder, and on
Ford's published Theorem 2, whose proof was read for its mechanism only
(pp. 24--25) and not verified. The bibliographic clause of S1 was checked
only against the statement page and Ford's p. 3. The formalization pointer
on the problem page was not compared with the section. This focused review
assigns no tier and changes no status.

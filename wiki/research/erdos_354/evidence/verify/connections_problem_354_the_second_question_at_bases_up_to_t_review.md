---
name: research/erdos_354/evidence/verify/connections_problem_354_the_second_question_at_bases_up_to_t_review
title: "Independent review of the connections section: Problem 354: the second question at bases up to the plastic number"
desc: |
  Refutation-failed for the index bridge, the constant arithmetic, the
  two-per-interval count (Proposition 354.5), the conditional deduction
  354.6 with its two addenda, Proposition 354.7 with its consequences,
  the four "what it does not give" statements and the lead's
  restatements; the closure clause of the next step ("closes the route at
  that base") is proof defective, statement unresolved, on both pages.
  One required correction, four suggested, three notes.
created: 2026-09-28T18:21:58Z
updated: 2026-09-28T18:21:58Z
---

***

## Subject and independence

Role: independent reviewer in a fresh context, commissioned for
refutation, given only the assignment; the reviewer took no part in
writing the connections page, the lead page or the reconstruction pages
and had no earlier contact with the Problem 354 folder.

Subject: the repository as it stood at 2026-09-28T13:50:48Z. The section
"## Problem 354: the second question at bases up to the plastic number" of
`wiki/research/erdos_354/connections.md`, lines 292--439 (line 440 is blank and
the next H2 is at line 441); the page's shared preamble, lines 17--58, as the
notation input; and the lead page
`wiki/research/leads/small_base_two_ray_distance_divergence/_index.md`,
whole page, as of the same time.

Read, and at what depth:

- The section and the lead page, every sentence, each proof re-derived.
- Reconstruction pages, whole, as premises at their reviewed standing:
  [[research/erdos_354/fan_remark_4_2_reconstruction|the Remark 4.2 page]]
  (definitions, the in-source statement of Theorem 1.1, the observation
  with its proof),
  [[research/erdos_354/geneson_theorem_9_reconstruction|the Theorem 9 page]]
  (Lemma 10 as imported, Proposition 11 with its proof),
  [[research/erdos_354/geneson_corollary_12_reconstruction|the Corollary 12 page]]
  (statement and proof) and
  [[research/erdos_354/yu_chen_theorem_reconstruction|the theorem page]]
  (Step 4, the index bridge).
- Held PDFs, text layer: Fan, arXiv:2607.14071v5, pp. 1--5 (Theorem
  1.1, the observation, Corollary 1.2, (1.8), (1.9), the sentence placing
  $M_\rho=2$ on $(1,\rho_0]$) and pp. 19--21 (Remarks 4.1 and 4.2);
  Geneson, arXiv:2609.25107v1, pp. 11--13 (Theorem 9, Lemma 10,
  Proposition 11 with proof, Corollary 12 with proof). Cards:
  [[../library/additive_bases/fan_2026_strongly_complete_sets_conjecture_erdos/_index|Fan (2026)]]
  and
  [[../library/additive_bases/geneson_2026_deletion_thresholds_exponential_examples_complete_sequences/_index|Geneson (2026)]]
  with their result pages `remark_4_2`, `theorem_9`, `corollary_12`.
- The Statement paragraphs of [[problems/additive_bases/E0354/_index|Problem 354]]
  and [[problems/additive_bases/E0349/_index|Problem 349]].
- `docs/verification.md` (Grading and claim standing, both audit
  checklists, Whole-claim report), `docs/approach_vetting.md`,
  `docs/evidence.md` "Source fidelity", `docs/math_authoring.md`.

Exposure: the Problem 354 page has no "## Statement" heading, and the
slice printed to find its statement (lines 1--60) ran past it into the
Formulation paragraph and the first lines of the Status paragraph (the
site's label and the accepted answer to the first question); the
Problem 349 page's one-line Status ("Open") was printed with its
statement. The two source cards and the three result pages were printed
whole, so their Overview, Read status, Proof pointer and Bears on
paragraphs were seen beyond the provenance and statement parts the
assignment names. None of this text carries a verdict on the section or
the lead, and none of it was used. Nothing under `evidence/`, no folder
`_index.md`, no Current assessment or Known results, and no review of
another section was read.

## Restatement

Conventions, from the page's preamble and the Remark 4.2 page:
$\mathbb N=\{1,2,\ldots\}$. A set $A\subseteq\mathbb N$ is *complete* if
every sufficiently large integer is a sum of distinct elements of $A$
and *strongly complete* if $A\setminus B$ is complete for every finite
$B\subseteq A$. Condition (1.5) for $A$ is
$\sum_{a\in A}\|a\theta\|=\infty$ for every
$\theta\in\mathbb R\setminus\mathbb Z$.
A sequence (the problem's interleaving) is complete if every
sufficiently large integer is a sum of terms with distinct indices. For
$\gamma\in(1,2)$ and $\alpha,\beta>0$,

$$
A^\gamma_{\alpha,\beta}=\{\lfloor\alpha\gamma^n\rfloor,
\lfloor\beta\gamma^n\rfloor:n\ge0\}\setminus\{0\},\qquad
I_k=(\gamma^k,\gamma^{k+1}],
$$

$S(t)=\{\lfloor t\gamma^n\rfloor:n\ge0\}\setminus\{0\}$ is the value set
of one ray, and $\rho_0=1.3247\ldots$ is the real root of $x^3=x+1$.

- **S1** (index bridge, Target paragraph). For every $\gamma\in(1,2)$
  and $\alpha,\beta>0$: if the set $A^\gamma_{\alpha,\beta}$ is complete,
  then the interleaving of $(\lfloor\alpha\gamma^n\rfloor)_{n\ge0}$ and
  $(\lfloor\beta\gamma^n\rfloor)_{n\ge0}$ is complete with indices used
  at most once.
- **S2** (Target paragraph, arithmetic of the preprint's constants).
  With $u_\rho=\lceil\rho(\rho-1)\rceil$,
  $v_\rho=\lceil\rho^3/(\rho+1)\rceil$ and
  $M_\rho=\min\{2u_\rho+1,2v_\rho\}$: $M_\rho=2$ for every
  $1<\rho\le\rho_0$. Hence, on the preprint's Theorem 1.1, every
  $A\subseteq\mathbb N$ with (1.5) and at least two elements in
  $(\rho^k,\rho^{k+1}]$ for all large $k$ is strongly complete at such
  $\rho$.
- **S3** (Proposition 354.5). For every $\gamma\in(1,2)$ and
  $\alpha,\beta>0$ there is $k_0$ such that for every $k\ge k_0$ the
  value set of each ray meets $I_k$ in exactly one element, and
  $|A^\gamma_{\alpha,\beta}\cap I_k|$ is $2$ if
  $\alpha/\beta\notin\gamma^{\mathbb Z}$ and $1$ if
  $\alpha/\beta\in\gamma^{\mathbb Z}$.
- **S4** (Conditional deduction 354.6). Let $\gamma\in(1,\rho_0]$,
  $\alpha,\beta>0$ and $\alpha/\beta\notin\gamma^{\mathbb Z}$. Under (P1),
  Fan's Theorem 1.1 exactly as transcribed on the Remark 4.2 page, and
  (P2), $A^\gamma_{\alpha,\beta}$ satisfies (1.5): the set
  $A^\gamma_{\alpha,\beta}$ is strongly complete and the interleaving is
  complete.
- **S5** (addenda to 354.6). (a) If $S(\alpha)$ or $S(\beta)$ satisfies
  (1.5), so does $A^\gamma_{\alpha,\beta}$. (b) If
  $A^\gamma_{\alpha,\beta}$ is strongly complete, it satisfies (1.5); so
  (P2) is necessary for strong completeness of the set, and is exactly
  what a proof of strong completeness at base $\gamma$ must supply.
- **S6** (Proposition 354.7). Let $\gamma\in(1,2)$ be a Pisot or Salem
  number whose minimal polynomial $P$ satisfies
  $x^{\deg P}P(1/x)=P(x)$ and $P(1)=-q$ for an integer $q\ge5$. Then
  there are $\alpha,\beta>0$ with $\beta/\alpha\ne r\gamma^k$ for all
  $r\in\mathbb Q$ and $k\in\mathbb Z$ such that
  $\lfloor\alpha\gamma^n\rfloor$ and $\lfloor\beta\gamma^n\rfloor$ are
  even for every $n\ge0$; consequently $\alpha/\beta\notin\mathbb Q$,
  neither floor sequence is a tail of the other, the interleaving and
  the set $A^\gamma_{\alpha,\beta}$ are incomplete, and
  $\sum_{a\in A^\gamma_{\alpha,\beta}}\|a/2\|<\infty$.
- **S7** (paragraph after 354.7). Geneson's base is the case $q=5$. At
  every base of S6 lying in $(1,\rho_0]$, (P2) fails for the constructed
  pair and that pair, whose ratio is irrational, is incomplete, so
  "every irrational-ratio pair is complete" is false at that base; at
  every base of S6 in $(1,2)$ the every-base reading of the second
  question is answered no. (Asserted and not used: every Salem number
  has a reciprocal minimal polynomial.)
- **S8** (first bullet of "What it does not give"). (P2) is proved at
  no base and fails at the bases of S6. For a rational base
  $\gamma=p'/q'\in(1,\rho_0]$ and $t>0$: $S(t)$ fails (1.5) at
  $\theta=1/2$ if and only if $\lfloor t\gamma^n\rfloor$ is even for all
  large $n$, if and only if $\{\eta\gamma^n\}<1/2$ for all large $n$
  where $t=2\eta$; this is of the type of Mahler's open question on
  $\{\xi(3/2)^n\}$; no held source addresses it; (1.5) at irrational
  $\theta$ is a further condition; nothing is known at a transcendental
  base.
- **S9** (second bullet). If $\alpha/\beta\in\gamma^{\mathbb Z}$ then
  $A^\gamma_{\alpha,\beta}$ is the value set of one ray with one element
  in each large $I_k$, Theorem 1.1 as stated does not apply, and the
  problem's multiset carries every value twice; if $\gamma\in\mathbb Q$
  and $\alpha/\beta\notin\mathbb Q$ then
  $\alpha/\beta\notin\gamma^{\mathbb Z}$.
- **S10** (fourth bullet). If $S(t)$ is complete for every $t>0$ at base
  $\gamma$, then every $S(t)$ is strongly complete, hence satisfies
  (1.5), hence (P2) holds for every pair; the two-ray question is then
  trivial, and the route has content only at a base where (1.5) can be
  proved for every ray without proving completeness.
- **S11** (Next investigation on the section, Next step on the lead).
  (a) For a ray $S(t)$, (1.5) at every rational $\theta\notin\mathbb Z$
  is: for every $q\ge2$ there are infinitely many $n$ with
  $q\nmid\lfloor t\gamma^n\rfloor$. (b) If every single ray at a fixed
  rational base $\gamma\in(1,\rho_0]$ satisfies (1.5), then with (P1)
  every pair with irrational ratio has $A^\gamma_{\alpha,\beta}$ strongly
  complete, answering the reading "for some $\gamma$" through the pair.
  (c) If some $t>0$ and $q\ge2$ have $q\mid\lfloor t\gamma^n\rfloor$ for
  all large $n$, then there is an incomplete single ray at that rational
  base, new for Problem 349, and this closes the route at that base.
- **S12** (lead page). The lead restates S2, S3, S4 with (P1) and (P2)
  as provisional premises, S6, S7, S8, S9, S10 and S11 in the forms
  quoted under Findings. Its own additions are the target formulation
  (the second question in the reading "for some $\gamma$": a base at
  which, for all $\alpha,\beta>0$ with $\alpha/\beta$ irrational, every
  sufficiently large integer is
  $\sum_{s\in S}\lfloor\gamma^s\alpha\rfloor+\sum_{t\in T}\lfloor\gamma^t\beta\rfloor$
  for finite $S,T$), the premise sentence "(P2) is necessary for strong
  completeness, so it is what any proof must supply", and the standing
  sentence that nothing on the page changes a status or assigns a tier.

## Checklist

- **Quantifiers and scope.** S3 is an eventual statement and holds; its
  proof states the threshold as $k\ge m_0$, which is false when the
  index offset $j$ exceeds $m_0$ (F1). S4 keeps "for all large $k$" and
  "$\ge M$" as Theorem 1.1 requires. S7 quantifies over a set shown
  nonempty by the $q=5$ base. S11(c) turns "one ray fails (1.5)" into
  "the route is closed", which would need (P2) to fail for an
  irrational-ratio pair (F2). The lead's "any proof" widens the object
  of S5(b) (F4). Otherwise clean.
- **Circularity.** None. S10 uses "every ray complete" only to conclude
  (P2) and says the two-ray question is then trivial rather than
  drawing anything from the route.
- **Model and convention changes.** The set $A^\gamma_{\alpha,\beta}$
  stands in for the problem's multiset; the bridge S1 is stated and
  valid in the one direction used (set complete implies interleaving
  complete). Incompleteness in S6 is proved for both objects directly.
  Fan's $\mathbb T\setminus\{0\}$ and the page's
  $\mathbb R\setminus\mathbb Z$ agree. Clean.
- **Finite and statistical overreach.** None; no finite computation is
  offered for an infinite statement, and Fan's random-set remark is not
  used.
- **Uniformity.** The thresholds of S3 and the "large $k$" of S4 depend
  on $\alpha,\beta,\gamma$ and no uniformity is claimed. Clean.
- **Extremal conclusions.** $M_\gamma=2$ is checked in its own units:
  $u_\gamma=v_\gamma=1$ exactly on $(1,\rho_0]$ and $v_\gamma=2$
  immediately above $\rho_0$. Clean.
- **Consequences and composition.** Every "hence" of S6 checked. S4
  consumes Theorem 1.1 at $M=M_\rho=2$, where the growth exponent is
  $0$ and the "in particular" clause supplies strong completeness.
  Three consequence sentences do not follow as written: "closes this
  route at that base" (F2), "gives an incomplete single ray" for the
  coefficient found (F3), and the lead's "what any proof must supply"
  (F4).
- **Computation.** The constants ($\rho_0$, $\varphi(\varphi-1)=1$,
  $5/4$, $9/7$, $13/10\le\rho_0$, $5/(2q)\le1/2$ exactly when $q\ge5$)
  were rechecked by hand and in exact rational arithmetic where
  rational; the witness of F1 was computed in exact rationals. Clean.
- **Reproduction.** The section and the lead state no rerun command and
  no coverage claim; inapplicable.
- **Source and verdict fidelity.** Theorem 1.1, the observation, (1.5),
  (1.8), (1.9) and the $\rho_0$ sentence match Fan pp. 3--4 clause by
  clause; Proposition 11 and Lemma 10 match Geneson p. 11; the Corollary
  12 argument with $q$ in place of $5$ matches pp. 12--13 step for step.
  The section's and the lead's description of what the Current
  assessment records (Corollary 12 for "every $\gamma$", a Lean
  candidate at $\gamma=\sqrt\varphi$ for "some $\gamma$") is outside the
  read set and is not checked here. Clean where checkable.

## Weakest steps

**1. The threshold in the proof of S3.** Fix $\gamma\in(1,2)$ and
$\alpha>0$; let $j\in\mathbb Z$ satisfy $\gamma^j<\alpha\le\gamma^{j+1}$
and put $\alpha^*=\alpha\gamma^{-j}\in(1,\gamma]$, so
$\lfloor\alpha\gamma^n\rfloor=\lfloor\alpha^*\gamma^{n+j}\rfloor$ for
$n\ge0$. Since $\alpha^*>1$ there is $m_1$ with $(\alpha^*-1)\gamma^m\ge1$
for all $m\ge m_1$, and then
$\alpha^*\gamma^m\ge\gamma^m+1\ge\lfloor\gamma^m\rfloor+1$, so
$\gamma^m<\lfloor\alpha^*\gamma^m\rfloor\le\gamma^{m+1}$. Hence the
term of index $m-j$ lies in $I_m$ whenever $m\ge m_1$ *and* $m\ge j$; the
proof's sentence "the term of index $m-j$ lies in $I_m$" presupposes the
second condition without stating it. A term of index $n'$ with
$n'+j\ge m_1$ lies in $I_{n'+j}$ and in no other $I_k$; one with
$n'+j<m_1$ is at most $\gamma^{n'+j+1}\le\gamma^{m_1}$ and lies in no
$I_k$ with $k\ge m_1$. So for $k\ge\max(m_1,j)$ the ray meets $I_k$ in
exactly the value $\lfloor\alpha^*\gamma^k\rfloor$, while for
$m_1\le k<j$, which occurs when $j>m_1$, it meets $I_k$ in nothing. With
$\beta^*$ likewise: if $\alpha^*\ne\beta^*$ then
$|\alpha^*-\beta^*|\gamma^k\ge1$ for large $k$, and $x\ge y+1$ gives
$\lfloor x\rfloor\ge\lfloor y\rfloor+1$, so the two values differ; if
$\alpha^*=\beta^*$ they coincide for every $k$. Finally
$\alpha^*/\beta^*=(\alpha/\beta)\gamma^{j'-j}\in(\gamma^{-1},\gamma)$ and
the only integer power of $\gamma$ in that interval is $1$, so
$\alpha^*=\beta^*$ exactly when $\alpha/\beta\in\gamma^{\mathbb Z}$. S3
follows with $k_0$ the largest of the two $m_1$'s, $j$, $j'$ and the
distinctness threshold. The proof as filed is repaired by one clause
(F1); the statement is unaffected.

**2. The $q\ge5$ step and the automorphism in S6.** Proposition 11 on
the Theorem 9 page, stated for every Pisot or Salem $\gamma$ with
$P(1)=-q$, $q\ge3$, gives $\eta>0$ with $3/(4q)<\{\eta\gamma^n\}<5/(4q)$
for all $n\ge1$. Put $\alpha=2\eta\gamma$ and $\beta=\alpha(1+\gamma)$.
For $n\ge0$, $\alpha\gamma^n=2\eta\gamma^{n+1}$ with $n+1\ge1$, and
$\lfloor2x\rfloor=2\lfloor x\rfloor+\lfloor2\{x\}\rfloor$ with
$2\{x\}<5/(2q)\le1/2$, so the floor is even. Next
$\beta\gamma^n=2(\eta\gamma^{n+1}+\eta\gamma^{n+2})=2(I+\sigma)$ with
$I\in\mathbb Z$ and
$\sigma=\{\eta\gamma^{n+1}\}+\{\eta\gamma^{n+2}\}\in(3/(2q),5/(2q))$;
then $\lfloor\beta\gamma^n\rfloor=2I+\lfloor2\sigma\rfloor$ and
$2\sigma<5/q\le1$ exactly when $q\ge5$. At $q=4$ the bound $2\sigma<5/4$
allows $\lfloor2\sigma\rfloor=1$ and the argument gives nothing, so the
hypothesis is consumed at its exact strength. Ratio: $P$ is irreducible
with roots $\gamma$ and, by reciprocity, $\gamma^{-1}$, so
$\gamma\mapsto\gamma^{-1}$ defines an isomorphism
$\mathbb Q(\gamma)\to\mathbb Q(\gamma^{-1})=\mathbb Q(\gamma)$, an
automorphism $\tau$. If $1+\gamma=r\gamma^k$ with $r\in\mathbb Q$ and
$k\in\mathbb Z$, then $r\ne0$, $\tau$ gives $1+\gamma^{-1}=r\gamma^{-k}$,
and the quotient $(1+\gamma)/(1+\gamma^{-1})=\gamma$ equals
$\gamma^{2k}$, impossible for $\gamma>1$ and integer $k$ (this uses
$\gamma\ne\gamma^{-1}$, true as $\gamma>1$). The case $k=0$ gives
$\beta/\alpha\notin\mathbb Q$; a tail relation
$\lfloor\beta\gamma^n\rfloor=\lfloor\alpha\gamma^{n+k}\rfloor$ for all $n$
gives $|\beta-\alpha\gamma^k|\gamma^n<1$ for all $n$, hence
$\beta=\alpha\gamma^k$, excluded with $r=1$; symmetrically for the other
direction. All values even makes every finite sum even, so the
interleaving and the set are incomplete, and
$\sum_{a\in A^\gamma_{\alpha,\beta}}\|a/2\|=0$. S6 holds as stated. A side
derivation: a Pisot number with reciprocal minimal polynomial has every
conjugate $\theta\ne\gamma$ in the open unit disk with $1/\theta$ also a
conjugate, so $1/\theta=\gamma$, the degree is $2$, and
$\gamma=(a+\sqrt{a^2-4})/2\ge(3+\sqrt5)/2>2$; the Pisot alternative in
S6 is vacuous on $(1,2)$ (F6).

**3. The bookkeeping of (P2): sufficient, necessary, closable.** (a)
$S(\alpha)\subseteq A^\gamma_{\alpha,\beta}$ and the summands
$\|a\theta\|$ are nonnegative, so divergence for the ray gives
divergence for the pair; S5(a) holds. (b) The observation on p. 3 of
Fan, re-derived: if $\sum_{a\in A}\|a\theta\|<\infty$ for some
$\theta\notin\mathbb Z$, drop the finitely many $a\le N_0$ to make the
tail sum less than $\|\theta\|/2$; strong completeness represents $n$
and $n+1$ by distinct elements above $N_0$ for all large $n$, so
$\|\theta\|\le\|n\theta\|+\|(n+1)\theta\|<\|\theta\|$; S5(b) holds. (c)
The closure in S11(c): suppose $q\mid\lfloor t\gamma^n\rfloor$ for all
$n\ge n_0$. For any $\beta$, the sum of $A^\gamma_{t,\beta}$ at
$\theta=1/q$ splits into the part over $S(t)$, which is finite, and the
part over $S(\beta)\setminus S(t)$, which diverges exactly when $S(\beta)$
has infinitely many elements not divisible by $q$ (such elements avoid
the late part of $S(t)$). So (P2) for the pair $(t,\beta)$ fails at
$\theta=1/q$ only if $S(\beta)$ is itself bad, and the section produces
no bad $\beta$ with $\beta/t\notin\mathbb Q$: the device of Corollary 12,
$\beta=t(1+\gamma)$, has $\beta/t\in\mathbb Q$ at a rational base, and
the section's own remark $\gamma^{\mathbb Z}\subseteq\mathbb Q$ shows
that any pairing inside $\mathbb Q(\gamma)=\mathbb Q$ has rational ratio.
A bad ray therefore defeats the single-ray sufficient condition S5(a)
and not the premise (P2) of S4; the closure clause is unsupported (F2).
Separately, the ray $S(t)$ itself need not be incomplete: its early
terms may supply the missing residues; the ray that is certainly
incomplete is $S(t\gamma^{n_0})$, all of whose elements are divisible by
$q$ (F3).

## Strongest attack

- S1: tried to defeat the index choice through a value produced by both
  rays or by two indices of one ray. Distinct values receive distinct
  (ray, index) labels whatever the choice, and zero terms are excluded
  from the set and harmless in the sum; the bridge holds. No converse is
  used anywhere.
- S2: tried the endpoint $\rho=\rho_0$ and the neighborhood above it.
  At $\rho_0$, $\rho_0^3/(\rho_0+1)=1$ so $v_{\rho_0}=1$, and
  $\rho_0(\rho_0-1)=0.4302\ldots$ so $u_{\rho_0}=1$; just above,
  $v_\rho=2$ and $M_\rho=3$. Exact rational check at $5/4$, $9/7$,
  $13/10$: all give $(u,v,M)=(1,1,2)$. The arithmetic holds; the
  theorem behind it is (P1) and is not reviewed.
- S3: tried an exceptional pair at an irrational base ($\gamma$ with
  $\alpha/\beta=\gamma^{-3}$), the boundary $\alpha^*=\gamma$, and a
  value equal to $\gamma^{k+1}$ when that is an integer; the count is
  $1$ or $2$ as stated in every case. The one break is the proof's
  threshold: with $\gamma=5/4$ and $\alpha=(5/4)^{21}$ one has $j=20$,
  $\alpha^*=5/4$, and the least $m_0$ with
  $\alpha^*\gamma^m\ge\lfloor\gamma^m\rfloor+1$ for all $m\ge m_0$ is
  $6$ (it fails at $m=5$: $3.81\ldots<4$; holds at $m=6$: $4.76\ldots\ge4$;
  holds for $m\ge7$ since $(1/4)(5/4)^m\ge1$), yet every value of the ray
  is at least $\lfloor\alpha\rfloor=108>\gamma^{20}=86.7\ldots$, so the
  ray has no term in $I_k$ for $6\le k\le19$. The statement survives;
  the proof's sentence does not (F1).
- S4: tried every interface of Theorem 1.1: "exactly two" against
  "$\ge M$" (fine); $M=M_\rho$ against a possible need for $M>M_\rho$
  (the theorem allows $M\ge M_\rho$, exponent $0$); (1.5) as a set
  condition (matches (P2)); $A\subseteq\mathbb N$ (zero removed);
  $\theta\in\mathbb T\setminus\{0\}$ against $\mathbb R\setminus\mathbb Z$
  (same); the endpoint $\rho_0$ (included). The deduction survives as a
  conditional.
- S5: tried a set that is complete but fails (1.5), to break necessity:
  $\{2^k:k\ge0\}$ has $\|2^k/2\|=0$ for $k\ge1$, so the sum at
  $\theta=1/2$ is $1/2$; it is complete and not strongly complete, and
  the observation's hypothesis is strong completeness, so S5(b) as the
  section words it survives. The same example refutes the lead's wider
  wording in general (F4).
- S6: tried $q=4$ (the $\beta$-terms are not controlled, so the
  hypothesis $q\ge5$ is exactly what is used), a non-reciprocal $P$
  (the automorphism disappears; excluded by hypothesis), and the Pisot
  alternative (vacuous on $(1,2)$, F6). Survives.
- S7: checked that Geneson's polynomial meets S6: exponents
  $18,12,\ldots,6,0$ are symmetric under $e\mapsto18-e$, $P(1)=1-7+1=-5$,
  and $\gamma\in(6/5,13/10)$ with $13/10<\rho_0$, so the base set of S7
  is nonempty in $(1,\rho_0]$ and the pair meets the second question's
  hypothesis. Survives.
- S8: tried to separate the set sum from the sequence sum through
  repeated values; a ray's values are strictly increasing once
  $t\gamma^n(\gamma-1)\ge1$, so only finitely many repeat. The
  equivalences hold. The Mahler comparison and "no held source" are not
  checkable in the read set.
- S9: tried $\alpha/\beta=\gamma^k$ with $k\ne0$: the $|k|$ initial values
  of the longer ray occur once in the multiset, so "every value twice"
  is imprecise (F7); the rest holds, and Theorem 1.1 with $M=1<2$ is
  indeed inapplicable as stated.
- S10: tried the two completeness conventions for a ray (set versus
  sequence); tails of a ray have distinct values, and a tail is the ray
  of $t\gamma^K$, so strong completeness follows under either. Survives.
- S11: (a) holds since $\|ma/q\|=0$ if $q\mid m$ and $\ge1/q$ otherwise
  for $\gcd(a,q)=1$. (b) holds at a rational base, where the exceptional
  set is empty; but "a positive outcome" must be the full (1.5), not the
  rational-$\theta$ case the same sentence describes (F5). (c) does not
  follow: see Weakest step 3 (F2, F3); novelty for Problem 349 is not
  checkable in the read set.
- S12: the lead's restatements agree with the section; its premise
  sentence widens S5(b) (F4) and its Next step carries F2, F3 and F5.

## Premises

- (P1) Fan, *Strongly complete sets and a conjecture of Erdős*,
  arXiv:2607.14071v5, Theorem 1.1, p. 3; held; text layer read. Interface
  confirmed: $\rho>1$; integer $M\ge M_\rho$; $A\subseteq\mathbb N$ with
  (1.5) and $|A\cap(\rho^k,\rho^{k+1}]|\ge M$ for all large $k$;
  conclusion $q_{A\setminus F}(n)/n^{(M-M_\rho)\log_\rho2}\to\infty$ for
  every finite $F\subseteq A$, in particular strong completeness. Proof
  (Sections 2--4) not read, as commissioned; a preprint. The
  transcription on the Remark 4.2 page matches clause by clause.
- Fan, p. 4: $M_\rho=2$ for $1<\rho\le\rho_0$ with $\rho_0$ the real root
  of $\rho^3=\rho+1$, $1.324717957\ldots$; re-derived. The observation on
  p. 3 (strong completeness implies (1.5)); re-derived. Definitions
  (1.5), (1.8), (1.9), p. 4; Remark 4.2, p. 20, interface only.
- Geneson, *Deletion thresholds and exponential examples for complete
  sequences*, arXiv:2609.25107v1, Lemma 10 and Proposition 11, p. 11,
  proof of Proposition 11, pp. 11--12, Corollary 12 with proof,
  pp. 12--13; held; text layer read. Lemma 10 is Dubickas's Theorem 6,
  not held, imported as quoted.
- Reconstruction pages at their reviewed standing (as of 2026-09-28T05:03:27Z
  with corrections since): the Remark 4.2 page (the observation's
  proof, the in-source statements); the Theorem 9 page (Proposition 11
  for general $q\ge3$, consumed by S6 at $q\ge5$; the location
  $6/5<\gamma<13/10$); the Corollary 12 page (the $q=5$ instance of S6
  and the tail and parity consequences, followed step for step with
  general $q$); the theorem page (Step 4, the index bridge of S1). All
  read whole; each used inside its stated hypotheses.
- Problem 354, Statement: the multiset reading with indices used at most
  once, and the second question "What if $2$ is replaced by some
  $\gamma\in(1,2)$?". Problem 349, Statement: for which $t,\alpha>0$ the
  sequence $\lfloor t\alpha^n\rfloor$ is complete, sums of distinct
  integers of that form.
- Explicit assumptions: (P1) and (P2) as named on both pages. No batch
  acceptance order applies.

## Findings

**F1** (suggested). Location, proof of Proposition 354.5: "so for
$k\ge m_0$ the $\alpha$-ray has exactly one term in $I_k$, namely
$\lfloor\alpha^*\gamma^k\rfloor$". Defect: the term of index $k-j$ exists
only for $k\ge j$, and $m_0$ is chosen without reference to $j$; for
$m_0\le k<j$ the ray has no term in $I_k$. Witness: $\gamma=5/4$,
$\alpha=(5/4)^{21}$, $j=20$, least admissible $m_0=6$, no term of the
ray in $I_k$ for $6\le k\le19$ (Strongest attack, S3). Replacement:
"so for $k\ge\max(m_0,j)$ the $\alpha$-ray has exactly one term in
$I_k$", or choose $m_0\ge\max(j,0)$ when it is introduced. The
statement is unaffected.

**F2** (required). Location, section "Next investigation": "a negative
outcome, a coefficient with all late terms divisible by $q$, gives an
incomplete single ray at a rational base below the golden ratio, which
is new for Problem 349 and closes this route at that base"; lead "Next
step": "gives an incomplete single ray at a rational base below the
golden ratio, new for Problem 349, and closes the route at that base".
Defect: the route of both pages is deduction 354.6, whose premise (P2)
concerns the two-ray set; a single bad ray defeats only the sufficient
condition "every single ray satisfies (1.5)" and leaves (P2) for
irrational-ratio pairs open. Witness: Weakest step 3(c); at a rational
base the Corollary 12 pairing $\beta=t(1+\gamma)$ has rational ratio,
and no bad pair with irrational ratio is produced. Replacement: "and
closes the single-ray sufficient condition at that base; (P2) for
irrational-ratio pairs then needs a direct argument, or a second bad
coefficient with irrational ratio to the first, which would give an
incomplete pair as Proposition 354.7 does".

**F3** (suggested). Location, the same two sentences, "gives an
incomplete single ray". Defect: the ray with the coefficient found need
not be incomplete, since its finitely many early terms can supply the
residues that the late terms lack; the incomplete ray is the one with
the shifted coefficient $t\gamma^{n_0}$, every term of which is divisible
by $q$. Witness for the inference form: base $2$, $t=1$, $q=2$: every
term with $n\ge1$ is even and $\{2^n\}$ is complete, while $\{2^n:n\ge1\}$
is not. Replacement: "gives an incomplete single ray (that of the
coefficient $t\gamma^{n_0}$, all of whose terms are divisible by $q$)".

**F4** (suggested). Location, lead "Provisional premises": "(P2) is
necessary for strong completeness, so it is what any proof must
supply". Defect: necessity is for strong completeness of the set, not
for the lead's target, completeness of the interleaving; a proof of the
target by another route need not supply (P2). Witness for the general
principle: $\{2^k:k\ge0\}$ is complete and fails (1.5) at $\theta=1/2$.
Replacement: "so it is what any proof of strong completeness must
supply".

**F5** (suggested). Location, section "Next investigation": "attempt
(1.5) for every single ray, beginning with rational $\theta$: ... A
positive outcome, together with (P1), gives strong completeness"; lead
"Next step", the same shape. Defect: the outcome that feeds S4 is the
full (1.5), every $\theta\notin\mathbb Z$; the sentence's colon
describes only the rational-$\theta$ case, which the preceding bullet
itself calls insufficient. Replacement: "A positive outcome for every
$\theta\notin\mathbb Z$, together with (P1), ...".

**F6** (note). Location, Proposition 354.7: "Let $\gamma\in(1,2)$ be a
Pisot or Salem number whose minimal polynomial $P$ is reciprocal"; lead:
"every reciprocal Pisot or Salem base". A Pisot number with a reciprocal
minimal polynomial is a quadratic unit $\ge(3+\sqrt5)/2$ (Weakest step
2), so the Pisot alternative is empty on $(1,2)$. Not an error; the
hypothesis could read "Salem number" alone.

**F7** (note). Location, second bullet: "the problem's multiset has
every value twice". For $\alpha/\beta=\gamma^k$ with $k\ne0$, the $|k|$
initial values of the longer ray occur once. Replacement: "every value
of the shorter ray twice" or "every sufficiently large value twice".

**F8** (note). Three sentences claim what the read set cannot check:
"which is new for Problem 349" (novelty), "no held source addresses it"
(library coverage), and the description of the Current assessment in
the Target paragraphs of both pages. Two wordings read wider than what
is proved: the Outcome's "marks the bases where (P2) fails" reads as a
characterization where only some bases are given ("marks bases"); and
the Target's "every set with two elements in each large $\rho$-adic
interval" is Theorem 1.1's "at least two", which the proof of S4
applies correctly.

## Verdict

- S1 (index bridge): **refutation-failed**.
- S2 (constants; $M_\rho=2$ on $(1,\rho_0]$): **refutation-failed**; the
  theorem it feeds is (P1), a preprint statement not reviewed here.
- S3 (Proposition 354.5): **refutation-failed**; the filed proof carries
  the threshold defect F1, repaired by one clause, and the statement is
  re-derived in full above.
- S4 (Conditional deduction 354.6): **refutation-failed** as a
  conditional on (P1) and (P2), which remain unproved; it establishes
  nothing unconditionally, as both pages say.
- S5 (addenda): **refutation-failed** in the section's wording; the
  lead's widening to "any proof" is F4.
- S6 (Proposition 354.7): **refutation-failed**, resting on Proposition
  11 and through it on Dubickas's theorem as quoted, not held; the Pisot
  alternative is vacuous (F6).
- S7 (bases where (P2) fails; the every-base reading): **refutation-failed**.
- S8 (first bullet): **refutation-failed** for its mathematical
  equivalences; the Mahler comparison, "no held source" and the
  transcendental remark are not adjudicated.
- S9 (exceptional pairs): **refutation-failed**, with the wording of F7.
- S10 (redundancy): **refutation-failed**.
- S11(a), S11(b) (the rational-$\theta$ formulation; the positive
  outcome): **refutation-failed**, with the clarification F5.
- S11(c) (the negative outcome): "gives an incomplete single ray at that
  base" **refutation-failed** once read for the shifted coefficient
  (F3); "closes this route at that base", on both pages, **proof
  defective; statement unresolved** (F2): a bad single ray is not shown
  to defeat (P2) for any irrational-ratio pair, and no argument either
  way is available in the read set.
- S12 (lead page): **refutation-failed** for its restatements; its own
  premise sentence carries F4 and its Next step carries F2, F3 and F5.

Limitations: (P1) is consumed at statement level and its proof was not
read; Dubickas's theorem is not held and enters only as Geneson quotes
it; the section's characterizations of the Current assessment and its
novelty and library-coverage claims lie outside the read set. This
focused review assigns no tier and changes no status.

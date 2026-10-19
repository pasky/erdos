---
name: research/erdos_49/evidence/verify/connections_problem_417_totients_below_x_against_totients_of_review
title: "Independent review of the connections section: Problem 417: totients below x against totients of integers below x"
desc: |
  Refutation review of the Problem 417 section of the Problem 49 connections
  page. All eight mathematical statements (Propositions 2, 3 and 4, the
  cluster interval, the conditional consequence, the sieve claim and the two
  obstructions) survive attack: refutation-failed for each. Zero required
  corrections; two suggested wording and locator fixes; three notes.
created: 2026-09-28T18:18:56Z
updated: 2026-09-28T18:21:23Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context, given only the
commissioned assignment. The reviewer took no part in writing the
connections page, the reconstruction pages, the lead, or any problem or
library page, and had no communication with their authors. Charge:
refutation.

**Frozen subject.** Page `wiki/research/erdos_49/connections.md` as it stood on
2026-09-28T13:50:48Z, section "## Problem 417: totients below x against totients
of integers below x", lines 283--443 (from the H2 heading to the line before the
next H2 at line 444). That state was the branch head at review time. Lead page:
`wiki/research/leads/distinct_totient_preimage_ratio/_index.md` in the same
state, read in full.

**Read, all in the pinned state.** The section, clause by clause. The
page's shared section "Notation and the inputs used" (lines 58--111) and
its introduction (lines 1--57), as inputs whose interfaces were confirmed
at each use. The reconstruction pages `lemma_4_1_reconstruction.md`,
`lemma_5_1_reconstruction.md` and `theorem_1_2_reconstruction.md` in
`wiki/research/erdos_49/`, in full, as premises at their reviewed
standing. The Statement of `wiki/problems/arithmetic_functions/E0417/_index.md`.
The provenance paragraphs of the cards
[[../library/arithmetic_functions/ford_1998_distribution_totients/_index|Ford (1998)]]
and
[[../library/primes/pollack_et_al_2013_sets_monotonicity_euler_totient_function/_index|Pollack, Pomerance and Treviño (2013)]],
and the Statement section of the latter's Theorem 1.2 result page. The held
PDFs: the 17-page author manuscript of Pollack, Pomerance and Treviño,
pp. 7--10 on the text layer and p. 8 (Lemma 4.1) on the page image; Ford's
43-page corrected version, theorem statements pp. 2--4 (p. 3 on the page
image), section 5 pp. 24--26 (text layer; Lemma 5.2 statement), and p. 39
(page image). The wiki pages named by the assignment. Two independent
computations were run in a scratch directory outside the repository and
are not filed: the divisor-recursion enumeration of the preimages of the
seed totient (with a brute-force cross-check of the recursion on every
totient up to 3000) and a sieve of Euler's function to $6\cdot10^6$.

**Exposures.** Three, disclosed: (1) the read of the E0417 Statement
printed the page head through its Current assessment, Progress and Known
Results sections (excluded standing text); their content was that the
problem page carries author-recorded notes citing this section and the
Problem 416 connections page, and it is used below only in Finding F4,
which records that the section's description of the problem page is stale in the
pinned state; (2) the lead page's frontmatter fields `research_state` and
`review_status` were read with the page; (3) a file listing of
`wiki/research/erdos_49/` showed the names of the files under its
`evidence/verify/` folder; none was opened. No web search was made; no
`_index.md` of the folder, no evidence page, no review or grade, and no page of
the Problem 416 folder was read.

## Restatement

Notation: $V(x)$ is the number of totients $\le x$; $\mathcal W(x)$ is the
set of values $\varphi(m)$ with $1\le m\le x$, $W(x)=\#\mathcal W(x)$, and
the problem writes $V'(x)$ for $W(x)$; $Z(x)$ is Ford's function; an
integer $n$ is convenient for a totient $d$ with preimages $n_1,\dots,n_k$
when $d\varphi(n)$ is a totient whose preimages are exactly
$n_1n,\dots,n_kn$. Since $\varphi(m)\le m$, $\mathcal W(x)$ is a subset of
the totients $\le x$, so $V(x)-V'(x)$ is the number of totients $\le x$ all
of whose preimages exceed $x$.

- **S1 (Proposition 2).** There is an absolute constant $C$ such that
  $V(x)\le C\,V'(x)$ for every sufficiently large real $x$; hence
  $\limsup_{x\to\infty}V(x)/V'(x)<\infty$. Claimed proof inputs: (L4) with
  $d_1=d_2=1$ and $D=K$, and $V(x)\le C_1Z(x)$ from (F).
- **S2 (cluster interval).** With $R(x)=V(x)/V'(x)$: for all large $x$ and
  every $0<h\le1$, $|R(x+h)-R(x)|\le(1+C)/W(x)$, which tends to $0$; the
  set of limit points of $R(x)$ as $x\to\infty$ is a closed interval
  $[\ell_1,\ell_2]$ with $1\le\ell_1\le\ell_2\le C$ (possibly degenerate);
  in particular an infinite limit is excluded.
- **S3 (Proposition 3).** There are absolute constants $c'\in(0,1)$ and
  $J\ge1$ such that for every sufficiently large $x$ some
  $y\in[2^{-J}x,x]$ satisfies $V(y)-V'(y)\ge c'V(y)$; hence
  $\limsup_{x\to\infty}V(x)/V'(x)\ge1/(1-c')>1$. Claimed proof inputs: (L4)
  with $d_1=d_2=D=d=2^{18}\cdot257$; (P), that all eight preimages of $d$
  are even; both consequences of (F).
- **S4 (consequence).** $\ell_2>1$; if $\lim V(x)/V'(x)$ exists it exceeds
  $1$; the existence question is untouched.
- **S5 (computation, author-recorded, not filed).** Every totient
  $v\le10^6$ has an odd preimage, established by a sieve over
  $m\le6\cdot10^6$.
- **S6 (obstruction).** Premise (W): for every totient $d$ and every real
  $\lambda>1$ there are $c(d,\lambda)>0$ and $t_0(d,\lambda)$ such that for
  $t\ge t_0$ at least $c(d,\lambda)Z(t)$ integers $n$ are convenient for $d$
  and satisfy $t/\lambda<\varphi(n)\le t$. The section asserts that (W) is
  not deducible from (L4) as stated (with (F)) for any fixed $\lambda$,
  because the only available subtraction leaves a lower bound with an
  unspecified constant minus a count at the smaller scale bounded above by
  $V(t/\lambda)\asymp V(t)/\lambda$.
- **S7 (Proposition 4, conditional).** If (W) holds for $d=2$ and
  $\lambda=3/2$, then $V(x)-V'(x)\ge cV(x)$ for all large $x$ with an
  absolute $c>0$, so $\liminf_{x\to\infty}V(x)/V'(x)>1$.
- **S8 (obstruction).** The inputs of the proof of S3 (a lower bound
  $E(t)\ge cV(t)$ for the count $E$ of all-even totients, $E\le V$, and
  (F)) do not force $E(y)-E(y/2)\gg V(y)$ at every scale, so that method
  gives no limit inferior without (W) or another input.
- **S9 (characterizations, not mathematics).** The paragraph "Parallel
  derivation" characterizes the Problem 416 connections page and the lead
  (seed $54$ with preimages $81$ and $162$; premise (P1) as "(W) in
  multiplicity form"; "independent checks of one another"); the premise
  paragraph locates Ford's Theorem 4 "on the Ford card" and describes it;
  the paragraph "Next investigation" records two readings of Ford's
  section 5 as points to verify; the Target paragraph describes the corpus
  problem page and the site's page.

## Checklist

- **Quantifiers and scope.** Pass. Every statement is eventual ("for large
  $x$") where its proof is, and S3 is stated in the exact form the proof
  delivers (some $y$ in every block $[2^{-J}x,x]$, not every $y$). The
  limit superior (S3) and limit inferior (S7) are kept apart, S7 is
  conditional in its heading and its statement, and S4 says which question
  is answered and under which condition. The strictness needed in S3 (every
  preimage of an all-even totient $v\in(y/2,y]$ is $\ge2v>y$) and in S7
  ($3n\ge3\varphi(n)>x$) holds.
- **Circularity.** Pass. Nothing assumes a target. S1 rederives Ford's
  $V\asymp W$ from (L4), whose counting steps (F1)--(F2) are Ford's own
  section 5 argument; that is a shared source, not a circle, and the page
  says so ("at the scope the reconstruction pages record").
- **Model and convention changes.** Pass. $V$ and $V'=W$ match the problem
  statement; "convenient" matches the source's p. 2 convention as recorded
  on the Lemma 5.1 page; (L4) is applied to the actual integers it counts,
  with no averaged or relaxed substitute; the seed's preimage set was
  recomputed (see Computation).
- **Finite and statistical overreach.** Pass. The sieve (S5) is used only
  descriptively ("all-even totients are rare among small totients") and
  is labeled author-recorded and not filed; no finite computation stands in
  for a proof.
- **Uniformity.** Pass. With the seeds fixed ($1$, $2$, $2^{18}\cdot257$),
  $c_K$, $c_d$, $C_1$, $C_2$, $J$ and $c'$ are absolute; $K$ is absolute by
  the source's statement (iii) and by the reconstruction's proof, which
  uses only $p_L\ge17$ and Ford's Lemma 3.8, so the choice $D=K$ in S1 is
  legitimate; the $\mu$-dependence of the threshold in (F) is stated
  ($x_2(\mu)$) and only fixed $\mu=2$ and $\mu=2^{J+1}$ are used. S7's
  constant depends on (W)'s $c(2,3/2)$, as stated.
- **Extremal conclusions.** Pass. The bounds on $\ell_1,\ell_2$ and the
  value $1/(1-c')$ are computed in the ratio's own units; $\ell_1,\ell_2$
  exist because $R$ is bounded (S1) and $R\ge1$.
- **Consequences and composition.** Pass for the mathematics, with the
  characterizations in S9 handled under Findings. Each "hence" was checked
  separately (S4 from S2 and S3; the display $V(y)-V'(y)\ge E(y)-E(y/2)$;
  $V(y)/V'(y)\ge1/(1-c')$ from $V'\le(1-c')V$). The composition inherits
  the partial reconstruction of (L4) and says so in the page's standing.
- **Computation.** Pass. The reviewer's own enumeration finds exactly the
  eight preimages listed on the Lemma 5.1 page, all even, with least
  preimage $2^{11}\cdot257^2=135268352$; the only candidate prime not
  among $2,3,5,17,257,65537$ is $2^{15}\cdot257+1=8421377=1123\cdot7499$,
  composite, which is what makes an odd preimage impossible. The preimages
  of $1$, $2$ and $54$ are $\{1,2\}$, $\{3,4,6\}$ and $\{81,162\}$. Exact
  integer arithmetic throughout.
- **Reproduction.** Pass with a limitation. The section states no rerun
  commands and files nothing; the reviewer reran the substance of both
  author-recorded computations independently. The sieve to $6\cdot10^6$
  (whose range holds every preimage of every totient $\le10^6$, since
  $\varphi(m)\le10^6<m/6$ would need nine distinct prime factors and then
  $\varphi(m)>3\cdot10^7$) finds $180184$ totients $\le10^6$, every one
  with an odd preimage; the count agrees with Ford's Table 1 entry
  $V(10^6)=180{,}184$.
- **Source and verdict fidelity.** Pass for every mathematical quotation:
  Ford's Theorem 1 (p. 2) matches (F); the source's Lemma 4.1 (p. 8, page
  image) matches (L4) and admits $d_1=d_2$ and $d_1=1$ ("Fix natural
  numbers $d_1,d_2\in\mathcal V$"); the source's p. 7 states
  $V(x)\asymp W(x)\asymp Z(x)$ as quoted; Ford's Theorem 4 (p. 3, page
  image) reads as the section describes it, and Ford's p. 39 records
  $d=2^{18}\cdot257$ as a totient all of whose preimages are divisible by
  $2$, $4$ and $8$. One locator is wrong (F1) and two characterizations
  overreach (F2, F3).

## Weakest steps

**W1 (the doubling consequence of (F), used in S3 and S7).** Write
$Z(x)=(x/\log x)\exp g(x)$ with
$g=C(\ell_3-\ell_4)^2+C'\ell_3-(C'+\tfrac12-2C)\ell_4$ and
$\ell_k=\log_kx$. For fixed $\mu>1$, $\log(x/\mu)=\log x-\log\mu$, so
$\ell_2(x/\mu)=\ell_2(x)-\varepsilon$ with
$\varepsilon=(1+o(1))\log\mu/\log x$; then
$\ell_3(x/\mu)=\ell_3(x)-(1+o(1))\varepsilon/\ell_2$ and
$\ell_4(x/\mu)=\ell_4(x)-(1+o(1))\varepsilon/(\ell_2\ell_3)$. The change of
$(\ell_3-\ell_4)^2$ is $2(\ell_3-\ell_4)\Delta+\Delta^2$ with
$\Delta=O(1/(\log x\,\ell_2))$, hence $O(\ell_3/(\log x\,\ell_2))\to0$; the
linear terms change by $o(1)$ as well. So $g(x/\mu)-g(x)\to0$ and
$Z(x/\mu)/Z(x)=\mu^{-1}(1+o(1))$. With $V=Ze^{O(1)}$ in both directions,
$V(x/\mu)\le C_1Z(x/\mu)\le(2C_1/\mu)Z(x)\le(C_2/\mu)V(x)$ for
$x\ge x_2(\mu)$, $C_2$ absolute. This is exactly the form S3 and S7 use.

**W2 (the dyadic pigeonhole in S3).** From (L4) at $d_1=d_2=D=d$ and (P),
$E(t)\ge c_dZ(t)\ge cV(t)$ for $t\ge t_1$, $c=c_d/C_1$. Fix $J$ with
$C_22^{-J-1}\le c/2$ (possible since $c,C_2$ are absolute). For $x$ with
$x/2^{J+1}\ge t_1$ and $x\ge x_2(2^{J+1})$,
$E(x)-E(x/2^{J+1})\ge cV(x)-V(x/2^{J+1})\ge cV(x)-\tfrac c2V(x)=\tfrac c2V(x)$,
using only $E(x)\ge cV(x)$ and the trivial $E\le V$ at the lower scale.
The telescoping sum of the $J+1$ dyadic increments equals the left side,
so some $j\le J$ has $E(x/2^j)-E(x/2^{j+1})\ge cV(x)/(2(J+1))$, and
$V(x)\ge V(x/2^j)$ turns this into $c'V(y)$ at $y=x/2^j$. The bridge to
the ratio is the elementary display: an all-even totient $v\in(y/2,y]$ has
every preimage $m$ even, so $\varphi(m)\le m/2$, $m\ge2v>y$, and $v$ is
counted by $V(y)$ but not by $V'(y)$. Hence $V(y)-V'(y)\ge E(y)-E(y/2)$.
The step is sound; its constants are absolute.

**W3 (the admissibility of the degenerate inputs to (L4) in S1).** The
source's Lemma 4.1 fixes "natural numbers $d_1,d_2\in\mathcal V$" and
$D\ge\max\{d_1,d_2\}$, with $K$ "an absolute constant". Neither
distinctness of $d_1,d_2$ nor $d_i>1$ is required, and Ford himself takes
$d=1$, $k=2$ to deduce his Theorem 5 from Theorem 2. Convenience for $1$
(preimages $1,2$) says $\varphi(n)$ has preimages exactly $n,2n$, so $n$
is the least preimage and $n\mapsto\varphi(n)$ is injective on the (L4)
set. With $D=K$: (iii) and (i) give $n\le K\varphi(n)\le x$, so the
$\ge c_KZ(x)$ values $\varphi(n)$ are distinct members of $\mathcal W(x)$.
Since $K$ does not depend on $D$ (the reconstruction's bound uses only
$p_L\ge17$ and Ford's Lemma 3.8), $c_K$ and $x_0(K)$ are absolute. Then
$V(x)\le C_1Z(x)\le(C_1/c_K)W(x)$. Sound.

## Strongest attack

- **S1.** Tried to break the injectivity (a second $n'$ with
  $\varphi(n')=\varphi(n)$ inside the set) and the containment $n\le x$;
  both are closed by the definition of convenience and by (iii) with
  $D=K$. Tried the quantifier order of $K$: if $K$ depended on $D$ the
  choice $D=K$ would be circular; the source states $K$ absolute and the
  reconstruction proves it independent of $D$. Failed.
- **S2.** Tried to make $V$ or $W$ jump by more than one on an interval of
  length at most one: impossible, since the new totients or the new
  arguments $m$ are integers in that interval. Tried to break the
  increment bound: with $V(x+h)=V+a$, $W(x+h)=W+b$, $a,b\in\{0,1\}$,
  $|R(x+h)-R(x)|=|aW-bV|/(W(W+b))\le V/W^2\le C/W$, so the stated
  $(1+C)/W$ holds with room. Tried to defeat the intermediate-value
  argument with a value $\ell\in(\ell_1,\ell_2)$ that $R$ skips: walking
  by unit steps from a large $x_a$ with $R(x_a)<\ell$ to a larger $x_b$
  with $R(x_b)>\ell$ (or the reverse) passes within one increment of
  $\ell$, and the increments tend to $0$. Failed.
- **S3.** Tried to find an odd preimage of $2^{18}\cdot257$: every prime
  $p$ dividing a preimage has $p-1\mid2^{18}\cdot257$, the only candidates
  beyond $2,3,5,17,257,65537$ are $2^a\cdot257+1$ for $0\le a\le18$, and
  the single one not visibly composite, $8421377$, factors as
  $1123\cdot7499$; so $257$ enters only as $257^2$, the remaining $2^{10}$
  needs the factor $2$ since $3,5,17$ contribute at most $2^7$, and every
  preimage is even. Tried to break the strictness $m\ge2v>y$: for even $m$,
  $\varphi(m)=2^{a-1}\varphi(m')\le m/2$. Tried to make
  $V(x/2^{J+1})$ large relative to $V(x)$: W1 bounds it by
  $(c/2)V(x)$. Failed.
- **S4.** Follows from S2 and S3 by definition of $\ell_2$. Failed.
- **S5.** Reran: no totient $\le10^6$ without an odd preimage. Failed.
- **S6.** Tried to deduce (W) at $\lambda=3/2$ from (L4) and (F): the
  convenient $n$ with $\varphi(n)\le t/(D\lambda)$ number at most
  $V(dt/(D\lambda))\le C_1(1+o(1))(d/(D\lambda))Z(t)$, so the window
  $(t/(D\lambda),t/D]$ holds at least $(c_D-C_1d/(D\lambda)+o(1))Z(t)$
  convenient integers; this is positive only for $\lambda$ large in terms
  of the unspecified $c_D$, and a lacunary placement of the convenient
  integers (mass $\approx CZ(t_k)$ at $\varphi(n)\approx t_k/D$, scales
  $t_{k+1}=\lambda^2t_k$) satisfies the (L4) interface at every $t$ with
  $c_D=C/\lambda^2$ while emptying the window at $t=\lambda t_k$. So (W)
  at a fixed $\lambda$ does not follow from the interface. The obstruction
  stands; the reviewer notes that a window form for some large
  $\lambda=\lambda(d)$ does follow, which the section's wording "no fixed
  $\lambda$ is forced to work" leaves room for. Failed.
- **S7.** Tried to use $n$ from (W) whose totient $2\varphi(n)$ has a
  preimage $\le x$: the preimages are exactly $3n,4n,6n$ and
  $3n\ge3\varphi(n)>x$. Tried $2\varphi(n)>x$: excluded by
  $\varphi(n)\le x/2$. Injectivity through the least preimage $3n$. The
  passage $Z(x/2)\ge Z(x)/3$ is W1. Failed.
- **S8.** Constructed the consistent burst: $E(t)=V(t)$ up to $y/2$ and
  flat to $y$ satisfies $E(y)\ge cV(y)$ whenever
  $c\le V(y/2)/V(y)\approx\tfrac12$, while $E(y)-E(y/2)=0$; the inputs of
  S3 admit it. The obstruction stands as stated ("cannot be upgraded ...
  without (W)" reads as a statement about this method, and S6's
  counter-placement shows the method's inputs do not exclude it). Failed.

## Premises

- **(L4), the source's Lemma 4.1.** Interface: fix totients
  $d_1,d_2\in\mathcal V$ and $D\ge\max\{d_1,d_2\}$; for $x\ge x_0(D)$ at
  least $c_DZ(x)$ integers $n$ satisfy $\varphi(n)\le x/D$, convenience for
  both, and $n/\varphi(n)\le K$ with $K$ absolute. Source: Pollack,
  Pomerance and Treviño, author manuscript, p. 8 (statement read on the
  page image) and pp. 8--9 (proof, text layer); held. Reconstruction:
  [[research/erdos_49/lemma_4_1_reconstruction|Lemma 4.1 page]], read in
  full; partial, with (F1) and (F2) imported from Ford's section 5 and not
  checked against Ford by the corpus. Used at $(1,1,K)$ and $(d,d,d)$,
  both inside the interface.
- **(F), Ford's Theorem 1.** Interface:
  $V(x)=(x/\log x)\exp\{C(\log_3x-\log_4x)^2+D\log_3x-(D+\tfrac12-2C)\log_4x+O(1)\}$,
  with Ford's $D$ the page's $C'$. Source: held corrected version, p. 2
  (text layer); card provenance read. The two consequences the page uses
  were re-derived in W1.
- **(P), the seed.** Interface: $d=2^{18}\cdot257$ has exactly eight
  preimages, all even, least $135268352$. Source:
  [[research/erdos_49/lemma_5_1_reconstruction|Lemma 5.1 page]] (read in
  full) and the reviewer's own enumeration; Ford's p. 39 (page image)
  lists the same $d$ for $k\in\{2,4,8\}$.
- **Ford's Theorem 4.** Interface: if $\theta$ is admissible, $y\ge x^\theta$
  and the multiplicity $k$ is possible, then
  $V_k(x+y)-V_k(x)\asymp V(x+y)-V(x)\asymp\frac{y}{x+y}V(x+y)$; hence
  $V(cx)-V(x)\asymp_cV(x)$ for fixed $c>1$; introduced by "a simple
  modification of the proof of Theorems 1 and 2". Source: held, p. 3 (page
  image). Not on the Ford card (F1). Used only in the (W) discussion.
- **Ford's Theorem 8 and its proof remark.** Interface: if $d$ is a
  totient all of whose preimages are divisible by $k$ then
  $V(x;k)\gg_\varepsilon d^{-1-\varepsilon}V(x)$; the remark on p. 39
  derives it from the section 5 lower-bound argument. Source: held, p. 3
  (text layer) and p. 39 (page image). Used only in the characterization
  of the parallel derivation.
- **Ford's section 5 (pp. 24--26, text layer; Lemma 5.2 statement).** Read
  to check the two readings in "Next investigation": the prime number
  theorem count of $p_0$ for a fixed cofactor appears explicitly in the
  bound for the exceptional sets $\mathcal B_j$ (p. 25), while the lower
  bound (5.17) for $\#\mathcal B$ is cited to Corollary 3.5 and Lemma 5.2
  and carries the $p_0$ count in its factor $x/(d\log(x/d))$; the excluded
  fraction decays through $\exp\{(L-j+1)(M/9-M/2C-\dots)\}$ with
  $M=M_2+[(\log d)^{1/9}]$. Both readings are consistent with the text at
  the level the section claims (plausibility, points to verify).
- **Problem statement.** [[problems/arithmetic_functions/E0417/_index|E0417]],
  Statement only (see Exposures): $V'(x)=\#\{\varphi(m):1\le m\le x\}$,
  $V(x)=\#\{\varphi(m)\le x:1\le m\}$; does $\lim V(x)/V'(x)$ exist, and is
  it $>1$. Matches the section's Target paragraph.
- **Lead page.**
  [[research/leads/distinct_totient_preimage_ratio/_index|distinct totient preimage ratio]],
  read in full; its description of the Problem 416 connections page
  (Proposition 417.2, Theorem 417.3 with seed $54$ and preimages $81$ and
  $162$, Proposition 417.4 under (P1)) is consistent with the section's
  "Parallel derivation" paragraph; the Problem 416 pages themselves were
  not read.
- **Elementary inputs.** Chebyshev's bound $\pi(x)\gg x/\log x$; the
  preimage sets of $1$, $2$ and $54$; $\varphi(m)\le m/2$ for even $m$.

## Findings

- **F1 (suggested; source locator).** Location: "Ford's Theorem 4, on the
  Ford card (short intervals $y\ge x^\theta$ for $V_k(x+y)-V_k(x)$, stated
  by Ford to follow from a simple modification of the proofs of his
  Theorems 1 and 2)". Defect: the Ford card in the pinned state lists Theorems
  1, 2, 5--7, 8, 9 and 10--11 and has no result pages; Theorem 4 is not on the
  card. Witness: the card's "Results to transcribe" list. The description itself
  is faithful to p. 3 of the held paper, which also carries the hypotheses
  "$\theta$ admissible" and "the multiplicity $k$ is possible". Proposed
  replacement: "Ford's Theorem 4 (p. 3 of the held paper; not among the results
  the card lists)", carrying the two hypotheses if the statement is quoted.
- **F2 (suggested; standing wording).** Location: "so the two pages are
  independent checks of one another". Defect: in this corpus
  "independent" names a fresh-context reviewer separated from authorship;
  the two pages are author-recorded derivations written in the same
  campaign, and both rest on Ford's section 5 construction ((F1)--(F2) of
  (L4) and Theorem 8, which Ford's p. 39 derives from that argument), so
  the sentence claims a standing the retained record does not give.
  Witness: the page's own standing paragraph ("not independently
  reviewed") and Ford's p. 39. Proposed replacement: "so the two pages are
  parallel derivations from different recorded inputs; neither is an
  independent review of the other".
- **F3 (note; characterization).** Location: "whose premise (P1), the
  short-interval form of Ford's Theorem 8, is the premise (W) above in
  multiplicity form". Defect: (P1) concerns $V(x;k)$, totients all of whose
  preimages are divisible by $k$, which Ford separates from the
  multiplicity counts $V_k(x)$ of Theorems 2 and 4; and (W) implies (P1)
  (take $d=54$, $\lambda=3/2$) while the converse is not claimed, so "is
  ... in ... form" overstates an equivalence. Proposed replacement: "whose
  premise (P1), the short-interval form of Ford's Theorem 8, follows from
  (W) at $d=54$ and $\lambda=3/2$".
- **F4 (note; stale description, from a disclosed exposure).** Location:
  "The corpus page is not yet compiled beyond the statement". Defect: in the
  pinned state the problem page (updated after this page) carries Progress and
  Known Results sections that cite this section, so the sentence is stale in
  that state. Proposed replacement: drop the clause or date it.
- **F5 (note; overstated attribution).** Location: "(W) is the
  intermediate statement that modification produces for convenient
  integers". Defect: Ford's p. 3 claims only Theorem 4 from the
  modification and states no window count for convenient integers; the
  sentence asserts as fact what an unwritten argument would yield.
  Proposed replacement: "would produce", keeping the following sentence
  "It is a premise here, not a result."

No required correction.

## Verdict

- S1 (Proposition 2): refutation-failed.
- S2 (cluster interval, infinite limit excluded): refutation-failed.
- S3 (Proposition 3): refutation-failed.
- S4 ($\ell_2>1$; a limit, if it exists, exceeds $1$): refutation-failed.
- S5 (every totient $\le10^6$ has an odd preimage): refutation-failed;
  reproduced independently.
- S6 ((W) not deducible from (L4) as stated at any fixed $\lambda$):
  refutation-failed, as a statement about the recorded interface.
- S7 (Proposition 4, conditional on (W) at $d=2$, $\lambda=3/2$):
  refutation-failed; the antecedent is assumed, not certified.
- S8 (the method of Proposition 3 gives no limit inferior): refutation-failed,
  as a statement about that method's inputs.
- S9 (characterizations): not mathematical claims; Findings F1--F5 apply.

Limitations. Every proposition inherits the standing of (L4), whose
counting steps (F1)--(F2) are imported from Ford's section 5 and were not
checked against Ford by the corpus or by this review; the reconstruction
pages were taken as premises at their reviewed standing. The site's page
for Problem 417 and the Problem 416 folder's pages were not read, so the
Target paragraph's account of the site and the "Parallel derivation"
paragraph's account of that folder were checked only against the lead page
and the held sources. The two computations were rerun in scratch and are
not filed. This focused review assigns no tier and changes no status.

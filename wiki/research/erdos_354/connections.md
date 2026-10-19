---
name: research/erdos_354/connections
title: "Connections of the Problem 354 reconstructions: Hegyvári's rational-ratio cases, the second question at small bases, and Problems 349, 348, 254 and 124"
desc: |
  Assesses the connections of the reconstructed Problem 354 proofs: the
  Yu--Chen descent transported to rational ratios (strong completeness for
  almost every coefficient on each rational-ratio line, and certified pairs),
  the conditional route to the second question through Fan's criterion at
  bases up to the plastic number, with its divergence premise explicit and
  the Salem bases where it fails, the dyadic-root transfer to Problem 349,
  and the remaining obstructions for Problems 348, 254 and 124.
created: 2026-09-28T06:40:00Z
updated: 2026-10-19T04:19:07Z
---

[[research/erdos_354/_index|..]]

***

**Purpose and standing.** This page draws the connections from the
author-recorded reconstructions in
[[research/erdos_354/_index|the Problem 354 folder]] to the rest of the
corpus. Each section names its exact target with the target's current
assessment, states what the reconstructed mechanism gives when transported,
with a proof where one is given here, states what it does not give and why,
and names the next investigation with what each outcome would establish.
Every new statement below is author-recorded, and no status or tier changes.
The earlier section subjects were independently reviewed on
2026-09-28T13:50:48Z in seven focused reports, graded in
[[research/erdos_354/evidence/verify/connections_grade|the connections grade]],
which assigns no tier. The current page also includes the separate
[[theory/additive_bases/L33_dyadic_root_floor_completeness/_index|dyadic-root deduction L33]];
those reports do not cover that deduction or its consequences here. L33
retains its own author-recorded standing. The reconstruction reviews in
the folder cover their named reconstruction subjects, not every transfer
on this page. The notation is the folder's: for $\alpha,\beta>0$,

$$
A_{\alpha,\beta}=\{\lfloor2^n\alpha\rfloor,\lfloor2^n\beta\rfloor:n\ge0\}
\setminus\{0\},
$$

a set is *complete* if every sufficiently large integer is a sum of distinct
elements and *strongly complete* if it stays complete after every finite
deletion; a *normalized pair* has
$N=\lfloor\beta\rfloor<M=\lfloor\alpha\rfloor<2N$ and $N\ge2$, with weights
$a_i=\lfloor2^i\alpha\rfloor$,
$b_i=\lfloor2^i\beta\rfloor$, conversions $u_i=a_{i+1}-2a_i$,
$v_i=b_{i+1}-2b_i$ (the binary digits of $\alpha$ and $\beta$ at position
$i+1$), events at the positions after a nonzero conversion, prefix sums
$P_n$, moduli $D_n=\gcd(a_n,b_n)$ and the modular run invariant $h_n$, all as
on the
[[research/erdos_354/yu_chen_normalization_reconstruction|normalization page]];
$K_*$, $C_M$ and the hypotheses of Section 3 are those of the
[[research/erdos_354/yu_chen_theorem_5_1_reconstruction|Theorem 5.1 page]].
A *dyadic rational* is a nonzero integer times a power of $2$. Hegyvári's
conjecture, as the problem page and Fan's preprint record it, says that
$A_{\alpha,\beta}$ is complete whenever $\alpha/\beta$ is not a power of $2$
and at least one of $\alpha,\beta$ is not a dyadic rational; Fan's condition
(1.5) for a set $A\subseteq\mathbb N$ is $\sum_{a\in A}\|a\theta\|=\infty$
for every $\theta\in\mathbb R\setminus\mathbb Z$, and Fan's constants $M_\rho$
and $M_\rho^*$ are as on the
[[research/erdos_354/fan_remark_4_2_reconstruction|Remark 4.2 page]].

## Problem 354: Hegyvári's conjecture at a rational ratio

**Target.** [[problems/additive_bases/E0354/_index|Problem 354]], whose Current
assessment records the first question as answered yes on a
Conjectures.io-accepted Lean proof for base $2$ and irrational ratio, lists
Hegyvári's conjecture as open, and names its rational-ratio cases as untouched
by every 2026 source (remaining gap (5)). The case in which exactly one of
$\alpha,\beta$ is a dyadic rational is Hegyvári's own
(erdosproblems.com-attested, the 1989 paper not held), so the open cases are
those with $\alpha/\beta$ rational, not a power of $2$, and neither coefficient
a dyadic rational. After multiplying one coefficient by a power of $2$, which
replaces $A_{\alpha,\beta}$ by a subset whose strong completeness implies that
of the original set, the ratio lies in $(1,2)$; write it as $p/q$ in lowest
terms, so $q<p<2q$ and $q\ge2$, and put $\gamma=\beta/q$, so that
$\alpha=p\gamma$ and $\beta=q\gamma$. Both coefficients are dyadic rationals
exactly when $\gamma$ is one: if $p\gamma,q\gamma$ are dyadic then so is
$\gamma=x(p\gamma)+y(q\gamma)$ for integers $x,y$ with $xp+yq=1$.

**Where irrationality enters the reconstructed argument** (author-recorded
reading of the folder's pages). Item 5 of the normalization page (the event
set is infinite) uses only that the conversions are not eventually zero,
which fails exactly when both coefficients are dyadic rationals; items 1--4
and 6 and the reduction hold for every pair whose ratio is not a power of
$2$. The three finite lemmas and Theorem 5.1 with its certificate use
nothing about the ratio: the constant $K_*=2q(p-1)+4(p+q)+64$ of the
Section 3 hypotheses is computed from the reduced pair $(p,q)$ of the layer
at which the theorem is applied, and only the length condition (5.2), which
bounds that pair by $p\le a_n<2^n(M+1)$, brings in the layer index. Step 2
of the [[research/erdos_354/yu_chen_theorem_reconstruction|theorem page]]
uses Theorem 5.1 and the infinitude of events only. The
[[research/erdos_354/yu_chen_fe_reconstruction|finite-event decay]] holds
for every normalized pair. Irrationality is consumed in exactly two places:
the [[research/erdos_354/yu_chen_windows_reconstruction|windows page]]
needs good rationals of unbounded denominator, and Step 2 of the
[[research/erdos_354/yu_chen_bg_reconstruction|bounded-spacing page]] needs
$\theta\notin\mathcal C_k$.

**What transports.** The descent survives with a fixed constant.

*Lemma 354.1 (bounded event spacing from incompleteness; author-recorded).*
Let $(\alpha,\beta)$ be a normalized pair that is not a pair of dyadic
rationals. If the normalized sequence is incomplete, then only finitely many
pairs of consecutive events $n<m$ satisfy $m-n\ge2n+C_M$, and there is $n_0$
such that every $n\ge n_0$ has an event in $(n,4n]$.

*Proof.* If the conversions vanished from some index $n_0$ on, then
$\alpha=a_{n_0}2^{-n_0}$ and $\beta=b_{n_0}2^{-n_0}$ as in item 5 of the
normalization page, against the hypothesis; so the event set is infinite.
Step 2 of the theorem page now applies word for word, since it consumes
only Theorem 5.1 and the infinitude of events. $\square$

*Proposition 354.2 (the descent at a rational ratio; author-recorded).* Let
$(\alpha,\beta)$ be a normalized pair with rational ratio $p/q$ in lowest
terms, and let $\gamma=\beta/q$. Put

$$
K_*(p,q)=2q(p-1)+4(p+q)+64,\qquad
L(p,q)=\lceil\log_2K_*(p,q)\rceil-1+\lceil\log_2p\rceil .
$$

If $\gamma$ is not a dyadic rational and the binary expansion of $\gamma$
contains infinitely many runs of at least $L(p,q)$ consecutive zeros, then
every sufficiently large integer lies in $\bigcup_nP_n$.

*Proof.* (i) By the Bézout remark above, $\gamma$ not dyadic means that
$\alpha,\beta$ are not both dyadic, so the conversions are not eventually
zero and every common zero run, an index interval on which $u_i=v_i=0$, is
finite.

(ii) *Exactness.* For every $s$ the integer $\delta_s=qa_s-pb_s$ equals
$-q\{2^s\alpha\}+p\{2^s\beta\}$, because $q\cdot2^s\alpha=p\cdot2^s\beta$.
The digits of $\alpha$ at positions $s+1,\ldots,s+L'$ vanish exactly when
$\{2^s\alpha\}<2^{-L'}$, and likewise for $\beta$. So on a common zero run
of length $L'\ge\log_2p$ starting at $s$, $|\delta_s|<p\,2^{-L'}\le1$, hence
$\delta_s=0$: $a_s/b_s=p/q$, and as $\gcd(p,q)=1$ the reduced pair of layer
$s$ in the Section 3 hypotheses is $(p,q)$ itself, with $d=D_s$.

(iii) *From runs of $\gamma$ to common runs.* Let $\{2^s\gamma\}<2^{-L}$
with $L=L(p,q)$. Since $p\{2^s\gamma\}<p\,2^{-L}\le1$, the fractional part
of $2^s\alpha=p\cdot2^s\gamma$ is $p\{2^s\gamma\}<2^{-(L-\lceil\log_2p\rceil)}$,
and the same holds for $\beta$ because $q<p$. So the conversions vanish on
$[s,s+L_0)$ with $L_0=L-\lceil\log_2p\rceil=\lceil\log_2K_*\rceil-1$; note
$L_0\ge\log_2K_*-1>\log_2(4p)-1>\log_2p$, as $K_*>4p$.

(iv) *One descent.* Let $[s',s'+L'-1]$ be the maximal common zero run
containing $[s,s+L_0)$, so $L'\ge L_0$; it is finite by (i), so the
conversion at index $s'+L'$ is nonzero, and by (ii) layer $s'$ has reduced
pair $(p,q)$. The Section 3 hypotheses hold at $n=s'$ with $\ell=L'+1$ and
$K=2^\ell\ge2^{L_0+1}=2^{\lceil\log_2K_*\rceil}\ge K_*(p,q)$. Theorem 5.1
gives $h_t\le\max(0,h_{s'}-1)$ for all $t\ge s'+L'+4$, and completeness if
$h_{s'}\le1$.

(v) *Iteration.* The runs of $\gamma$ start at positions tending to
infinity and each maximal common run is a finite interval, so there are
infinitely many maximal common runs of length at least $L_0$; choose a
sequence of them with $s'_{j+1}\ge s'_j+L'_j+4$. If the sequence were
incomplete, then $h_{s'_j}\ge2$ for every $j$ and
$h_{s'_{j+1}}\le h_{s'_j}-1$, a strictly decreasing sequence of integers
bounded below by $2$. Hence the sequence is complete. $\square$

Unlike the irrational case, no relation between the run length and its
position is needed: the constant $K_*(p,q)$ is fixed by the ratio, and the
length condition (5.2) is not used.

*Corollary 354.3 (almost every coefficient on a rational-ratio line;
author-recorded).* Let $\alpha,\beta>0$ have a rational ratio that is not a
power of $2$; let $p/q$ be the reduced form of the unique $2^k\alpha/\beta$
in $(1,2)$ and $\gamma=\beta/q$. If $\gamma$ is not a dyadic rational and
its binary expansion contains infinitely many runs of $L(p,q)$ zeros, then
$A_{\alpha,\beta}$ is strongly complete. In particular, for each fixed
rational ratio in $(1,2)$, the set $A_{p\gamma,q\gamma}$ is strongly
complete for Lebesgue-almost every $\gamma>0$, since almost every real
number is normal to base $2$ (Borel; imported) and so contains every finite
block of digits infinitely often.

*Proof.* Fix a finite $F\subseteq\mathbb Z$. Items 1--3 of the normalization
page give $u,v\ge0$ with $(2^u\alpha,2^v\beta)$ normalized and all values
above $\max(F\cup\{0\})$; only the exclusion of the value $1$ for
$2^k\alpha/\beta$ used irrationality there, and it holds because the ratio
is not a power of $2$. The normalized ratio is the $2^k\alpha/\beta$ in
$(1,2)$, that is $p/q$, and the normalized pair's $\gamma$ is
$2^v\beta/q=2^v\gamma$, whose expansion is that of $\gamma$ shifted, so it
is not dyadic and keeps infinitely many runs of $L(p,q)$ zeros. Proposition
354.2 makes the normalized sequence complete, and the reduction on the
normalization page turns this into completeness of
$A_{\alpha,\beta}\setminus F$. $\square$

For the smallest ratios the constants are $L(3,2)=8$ ($K_*=92$),
$L(5,4)=10$ ($K_*=132$) and $L(5,3)=9$ ($K_*=120$): for instance
$A_{3\gamma,2\gamma}$ is strongly complete for every non-dyadic $\gamma$
whose binary expansion has infinitely many runs of eight zeros. These pairs
have two irrational coefficients whenever $\gamma$ is irrational, so they
lie outside Hegyvári's proved case and outside the irrational-ratio theorem
of the Conjectures.io-accepted proof and of the Yu--Chen manuscript.

*Lemma 354.4 (finite certificate; author-recorded).* Let $(\alpha,\beta)$
be a normalized pair. If for some $n\ge1$ the set $P_n$ contains the $b_n$
consecutive integers $A,A+1,\ldots,A+b_n-1$, then every integer at least
$A$ lies in some $P_t$; in particular $A_{\alpha,\beta}$ is complete and the
interleaved sequence of the problem is complete for this pair.

*Proof.* List the weights of indices at least $n$ in increasing order,
$c_0=b_n<c_1=a_n<c_2=b_{n+1}<\cdots$; by item 4 of the normalization page
$c_{j+1}\le2c_j$. If a set of subset sums contains the $\Lambda$ consecutive
integers from $A$ and $c\le\Lambda$ is a further weight, adjoining it gives
the $\Lambda+c$ consecutive integers from $A$. Starting from $\Lambda_0=b_n=c_0$
and adjoining $c_0,c_1,\ldots$ in turn, the lengths satisfy
$\Lambda_{j+1}=\Lambda_j+c_j\ge2c_j\ge c_{j+1}$, so every weight is
admissible and the lengths tend to infinity. The last sentence is the
reduction on the normalization page. $\square$

This is the abutting case of the mesh lemma of the
[[research/erdos_354/yu_chen_lemma_2_2_reconstruction|Lemma 2.2 page]] with
gap $1$: the $b_n$ consecutive integers have span $b_n-1$, one short of the
lemma's hypothesis, which the count argument above replaces, while the
[[research/erdos_354/yu_chen_db_reconstruction|digit-budget page]] applies
the lemma with span at least the next weight; it turns completeness of one
pair into a finite computation. The
[[research/leads/rational_ratio_dyadic_floor_descent/evidence/_index|evidence of the lead]]
computes the subset sums exactly and records the following certificates,
each for a pair outside every held source: $(48/5,32/5)$, that is
$(3\gamma,2\gamma)$ with $\gamma=16/5$, at depth $n=9$ from $1423$ with
$b_9=3276$; $(48/7,32/7)$ at depth $9$ from $577$ with $b_9=2340$;
$(80/9,64/9)$, ratio $5/4$, at depth $7$ from $445$ with $b_7=910$;
$(6\sqrt2,4\sqrt2)$ at depth $7$ from $183$ with $b_7=724$;
$(5\sqrt2,3\sqrt2)$, ratio $5/3$, at depth $3$ from $18$ with $b_3=33$; and
every pair $(3\gamma,2\gamma)$ with $\gamma=2^T/d$ for the thirty-two odd
denominators $5\le d\le99$ not divisible by $3$, normalized by the least
$T$, by depth $12$: twenty-nine of them by depth $9$, and $d=23$, $89$ and
$91$, the pairs $(192/23,128/23)$, $(768/89,512/89)$ and $(768/91,512/91)$,
at depths $10$, $12$ and $11$, from $2139$, $11036$ and $4323$ with
$b_{10}=5698$, $b_{12}=23563$ and $b_{11}=11522$. The rational coefficients
have periodic expansions without zero runs of the required length (eight,
nine or ten), and $\sqrt2$ is not known to have infinitely many such runs,
so none of these pairs is known to be covered by Proposition 354.2; each
certificate is a proof of completeness for its own pair and nothing more.
The control pair $(\sqrt{50},\sqrt{20})$, of irrational ratio, certifies
at depth $6$, and Hegyvári's incomplete multiset $(5/2,5)$ receives no
certificate to depth $16$, as it must not.

**What it does not give.**

- The short-block coefficients. Proposition 354.2 acts through a maximal
  common zero run of the conversions of length at least
  $\lceil\log_2K_*\rceil-1$ at an exact layer, which a run of $L(p,q)$
  zeros in $\gamma$ guarantees; a coefficient with only finitely many such
  runs is outside the descent. Exact layers occur exactly at the $s$ with
  $\{2^s\gamma\}<1/p$, possibly nowhere ($\gamma=24/7$ at ratio $3/2$ has
  none: $\delta_s$ runs through $2,1,1$), and at an exact layer a common
  zero run of that length forces $\{2^s\gamma\}<2^{-\lceil\log_2K_*\rceil}$.
  For a rational $\gamma$ whose denominator in lowest terms has odd part
  $v$, $\{2^s\gamma\}\ge1/v$ for all large $s$, so every rational $\gamma$
  with $v\le2^{\lceil\log_2K_*\rceil}$ ($v\le128$ at ratio $3/2$), in
  particular every rational pair certified below, and uncountably many
  irrationals are outside the descent, while $\gamma=1/511$ at ratio $3/2$
  has infinitely many runs of exactly eight zeros and is covered by
  Corollary 354.3. For the coefficients outside, Hegyvári's conjecture
  stays open except pair by pair through Lemma 354.4, since Theorem 5.1
  needs $K\ge K_*$ for its coefficient interval (Step 1) and node
  connection (Step 4).
- The rest of the irrational-case argument does not transfer, for two
  precise reasons. First, a rational $\theta=p/q$ has only finitely many
  good rationals: a reduced $p'/q'\ne\theta$ has $|\theta-p'/q'|\ge1/(qq')$,
  so $|\theta-p'/q'|<1/q'^2$ forces $q'<q$; hence the digit budget (DB),
  which needs a good denominator at least $2^n\beta$, is empty for large
  $n$, and the crossing denominator $D(b)$ of the windows page does not
  exist for $b>q$, so (10.2) is unavailable. Second, $\theta=p/q$ lies in
  $\mathcal C_k$ as soon as $k$ is at least the number of ones in the binary
  expansions of $p$ and of $q$: with $2^J$ the largest power of $2$ in
  $p$, both $p/2^J$ and $q/2^J$ lie in $\mathcal S_k$ and $q/2^J>1/2$. So
  the neighborhood argument of Step 2 of the bounded-spacing page fails,
  and it fails for a reason: at $\theta=3/2$, whenever
  $\{2^s\gamma\}\in[1/4,1/3)$ the layer $s$ is exact, the conversions at
  $s$ and $s+1$ are $(1,1)$ and $(1,0)$, and $\delta_{s+2}=4\delta_s+qU-pV$
  with $U=3$, $V=2$ vanishes again: a return between exact layers costing
  two events, for every such $s$. Under a rational ratio the bounded event
  spacing of Lemma 354.1 is therefore not contradictory by itself; the
  finite-event decay still holds but only bounds the missing count by a
  polynomially small fraction under bounded spacing.
- No uniformity over pairs. Corollary 354.3 is a full-measure statement on
  each rational-ratio line; the exceptional set contains every pair with
  rational coefficients whose $\gamma$ has odd denominator part at most
  $2^{L(p,q)}$, and Hegyvári's 1991 dichotomy (for fixed $\alpha$, the
  incomplete $\beta$ form a set of measure $0$ or $\infty$) is neither used
  nor sharpened.

**Next investigation.** Two directions, recorded as the lead
[[research/leads/rational_ratio_dyadic_floor_descent/_index|rational_ratio_dyadic_floor_descent]].
First, a descent for coefficients with bounded runs: for rational
$\gamma=m/v$ with $v$ odd the conversions are eventually periodic with
period the order of $2$ modulo $v$, so a block of consecutive layers
satisfies $a_{n+i}=2^ia_n+r_i$ with the correction
$r_i=\lfloor2^i\{2^n\alpha\}\rfloor$, the integer whose binary digits are
the eventually periodic conversions; whether a coefficient interval and a
connection certificate exist for such blocks, in place of the exact block
$d\{px+qy\}$, is the question. A positive outcome would prove Hegyvári's
conjecture for every pair with rational coefficients and rational ratio,
and the general bounded-run case would remain; a negative outcome, an
incomplete pair found by the search below, would refute the conjecture.
Second, the certificate search of Lemma 354.4 is cheap and exact;
extending it over families of rational and quadratic coefficients turns
each positive case into a proved instance, and a pair with no certificate
to a large depth is the first candidate for an incompleteness argument
through Folkman-type gaps.

**Outcome.** Transfers: Lemma 354.1 for every non-dyadic normalized pair,
Proposition 354.2 and Corollary 354.3 for almost every coefficient on every
rational-ratio line, and Lemma 354.4 with certified pairs; open for the
short-block coefficients, with the two obstructions above.

## Problem 354: the second question at bases up to the plastic number

**Target.** The second question of
[[problems/additive_bases/E0354/_index|Problem 354]], "What if $2$ is replaced by
some $\gamma\in(1,2)$?", whose reading the Current assessment leaves
unfixed: under "for every $\gamma$" it is claimed no by Geneson's
Corollary 12, graded sound by the internal review recorded on its problem
page, its sign-off pending. Under "for some $\gamma$", Kitamura's proof at
$\sqrt\varphi$ remains pending. The separate author-recorded
[[theory/additive_bases/L33_dyadic_root_floor_completeness/_index|L33]]
deduces strong completeness of every single ray at $\gamma=2^{1/m}$,
$m\ge2$, from the accepted dyadic theorem. In particular $\sqrt2$
supplies the existential conclusion; its claim page, separate from this
author argument, awaits an outside sign-off. For $\gamma\in(1,2)$ and
$\alpha,\beta>0$ write

$$
A^\gamma_{\alpha,\beta}=\{\lfloor\alpha\gamma^n\rfloor,
\lfloor\beta\gamma^n\rfloor:n\ge0\}\setminus\{0\};
$$

completeness of this set implies completeness of the problem's interleaved
sequence, by the choice of one index per value as on the theorem page. The
folder index names the door: Fan's Theorem 1.1 has $M_\rho=2$ for
$1<\rho\le\rho_0=1.3247\ldots$, the real root of $x^3=x+1$, so at such a
base every set with two elements in each large $\rho$-adic interval and
(1.5) is strongly complete, on the preprint's claim.

**What transports.** The per-interval count is a theorem; the divergence
condition is the premise.

*Proposition 354.5 (two elements per $\gamma$-adic interval;
author-recorded).* Let $\gamma\in(1,2)$ and $\alpha,\beta>0$. For all
sufficiently large $k$, each of the two rays has exactly one term in
$I_k=(\gamma^k,\gamma^{k+1}]$, and $|A^\gamma_{\alpha,\beta}\cap I_k|$
equals $2$ if $\alpha/\beta\notin\gamma^{\mathbb Z}$ and $1$ otherwise.

*Proof.* Let $j$ be the integer with $\gamma^j<\alpha\le\gamma^{j+1}$ and
$\alpha^*=\alpha\gamma^{-j}\in(1,\gamma]$. For $n\ge0$ and $m=n+j$,
$\alpha\gamma^n=\alpha^*\gamma^m\in(\gamma^m,\gamma^{m+1}]$. Since
$(\alpha^*-1)\gamma^m\to\infty$, there is $m_0$ with
$\alpha^*\gamma^m\ge\lfloor\gamma^m\rfloor+1$ for $m\ge m_0$, and then
$\gamma^m<\lfloor\alpha^*\gamma^m\rfloor\le\gamma^{m+1}$: the term of index
$m-j$ lies in $I_m$. Every other term of index $n'\ge0$ lies in $I_{n'+j}$
if $n'+j\ge m_0$ and is at most $\gamma^{m_0}$ otherwise, so for
$k\ge\max(m_0,j)$ the $\alpha$-ray has exactly one term in $I_k$, namely
$\lfloor\alpha^*\gamma^k\rfloor$. The same holds for $\beta$ with
$\beta^*\in(1,\gamma]$. If $\alpha^*\ne\beta^*$ then
$|\alpha^*-\beta^*|\gamma^k\ge1$ for large $k$ and the two floors differ;
if $\alpha^*=\beta^*$ they coincide for every $k$. Finally
$\alpha^*=\beta^*$ exactly when $\alpha/\beta$ is an integer power of
$\gamma$, by the uniqueness of the representative in $(1,\gamma]$.
$\square$

*Conditional deduction 354.6 (author-recorded).* Let
$\gamma\in(1,\rho_0]$ and $\alpha,\beta>0$ with
$\alpha/\beta\notin\gamma^{\mathbb Z}$. Assume (P1) Fan's Theorem 1.1 as
stated on the Remark 4.2 page (a preprint claim whose proof, Sections 2--4
of the source, is not reconstructed in the corpus) and (P2) that
$A^\gamma_{\alpha,\beta}$ satisfies (1.5). Then $A^\gamma_{\alpha,\beta}$
is strongly complete, and the interleaving of the two floor sequences is
complete. Argument: $u_\gamma=\lceil\gamma(\gamma-1)\rceil=1$ because
$0<\gamma(\gamma-1)<\varphi(\varphi-1)=1$, and
$v_\gamma=\lceil\gamma^3/(\gamma+1)\rceil=1$ because $\gamma^3\le\gamma+1$
on $(1,\rho_0]$; so $M_\gamma=\min\{3,2\}=2$, Proposition 354.5 supplies
$|A^\gamma_{\alpha,\beta}\cap(\gamma^k,\gamma^{k+1}]|=2=M_\gamma$ for all
large $k$, and (P1) applies with $\rho=\gamma$, $M=2$ under (P2).
Premise (P2) follows from (1.5) for either single ray, since a superset of
a set with divergent sums has divergent sums, and it is necessary for
strong completeness by the observation reconstructed on the Remark 4.2
page; so (P2) is exactly what a proof of strong completeness at base
$\gamma$ must supply.

*Proposition 354.7 (Corollary 12 at every reciprocal Pisot or Salem base
with $P(1)\le-5$; author-recorded).* Let $\gamma\in(1,2)$ be a Pisot or
Salem number whose minimal polynomial $P$ is reciprocal,
$x^{\deg P}P(1/x)=P(x)$, with $P(1)=-q$ for an integer $q\ge5$. Then there
are $\alpha,\beta>0$ with $\beta/\alpha\ne r\gamma^k$ for all
$r\in\mathbb Q$ and $k\in\mathbb Z$ such that every term of both floor
sequences $\lfloor\alpha\gamma^n\rfloor$, $\lfloor\beta\gamma^n\rfloor$ is
even. Hence $\alpha/\beta$ is irrational, neither sequence is a tail of the
other, the interleaving and the set $A^\gamma_{\alpha,\beta}$ are
incomplete, and $A^\gamma_{\alpha,\beta}$ fails (1.5) at $\theta=1/2$.

*Proof.* The proof on the
[[research/erdos_354/geneson_corollary_12_reconstruction|Corollary 12 page]]
with $q$ in place of $5$. Proposition 11 of the
[[research/erdos_354/geneson_theorem_9_reconstruction|Theorem 9 page]],
stated there for every Pisot or Salem number with $P(1)=-q$, $q\ge3$, gives
$\eta>0$ with $3/(4q)<\{\eta\gamma^n\}<5/(4q)$ for $n\ge1$; put
$\alpha=2\eta\gamma$ and $\beta=\alpha(1+\gamma)$. The $\alpha$-terms are
even since $5/(4q)<1/2$; the $\beta$-terms are even since the sum of two
fractional parts lies in $(3/(2q),5/(2q))\subset(0,1/2)$, which is where
$q\ge5$ enters. The ratio condition uses only that $P$ is reciprocal and
minimal, through the automorphism $\gamma\mapsto\gamma^{-1}$ of
$\mathbb Q(\gamma)$, and the tail and parity conclusions follow as on that
page. $\square$

Geneson's base is the case $q=5$. Every Salem number has a reciprocal
minimal polynomial (a standard fact, not needed here since reciprocity is
assumed). At every such base in $(1,\rho_0]$, premise (P2) fails for the
pair constructed and the pair is incomplete, so no route can make every
irrational-ratio pair complete there; at every such base in $(1,2)$ the
every-base reading of the second question is answered no, as Corollary 12
answers it at one base.

**What it does not give.**

- The two-per-interval estimate alone does not establish premise (P2).
  At the dyadic-root bases, the separate
  [[theory/additive_bases/L33_dyadic_root_floor_completeness/_index|L33]]
  gives strongly complete single rays, so this route is unnecessary there.
  Premise (P2) fails for the pairs constructed in Proposition 354.7.
  At a rational base $\gamma=p'/q'\in(1,\rho_0]$ (such as $5/4$,
  $9/7$ or $13/10$), its failure at $\theta=1/2$ for a single ray means
  that $\lfloor t\gamma^n\rfloor$ is even for all large $n$, that is
  $\{\eta\gamma^n\}<1/2$ for all large $n$ with $t=2\eta$, a question of the
  same type as Mahler's open question on $\{\xi(3/2)^n\}$; no held source
  addresses it, and (1.5) at irrational $\theta$ is a further condition.
  At a transcendental base nothing is known here either way.
- The exceptional pairs $\alpha/\beta\in\gamma^{\mathbb Z}$. There
  $A^\gamma_{\alpha,\beta}$ is a single ray with one element per interval,
  Theorem 1.1 does not apply, and the problem's multiset has every
  sufficiently large value twice; at a rational base the exceptional set
  is empty, because $\gamma^{\mathbb Z}\subseteq\mathbb Q$ while
  $\alpha/\beta$ is irrational.
- Standing. The deduction inherits (P1): the criterion is a preprint claim
  read at statement level, and no reconstruction or review of Theorem 1.1
  exists in the corpus.
- Redundancy at a base where every ray is complete. If every single
  sequence $\lfloor t\gamma^n\rfloor$ is complete at base $\gamma$, then
  every such sequence is strongly complete (its tails are the sequences of
  the coefficients $t\gamma^K$), so (P2) holds for every pair, but the
  two-ray question is then trivial. The route has content only at a base
  where (1.5) can be established for every ray without proving
  completeness; none is known here.

**Next investigation.** Fix one rational base in $(1,\rho_0]$ and attempt
(1.5) for every single ray, beginning with rational $\theta$: for every
$q\ge2$ and every $t>0$, infinitely many $n$ with
$q\nmid\lfloor t\gamma^n\rfloor$. A positive outcome, together with (P1),
gives strong completeness of $A^\gamma_{\alpha,\beta}$ for every pair with
irrational ratio at that base, an answer to the reading "for some
$\gamma$" in which the pair, not a single ray, carries the completeness; a
negative outcome, a coefficient with all late terms divisible by $q$,
gives an incomplete single ray at a rational base below the golden ratio
(the ray of the coefficient $t\gamma^{n_0}$, every term of which is
divisible by $q$), which is new for
[[problems/additive_bases/E0349/_index|Problem 349]] and closes the single-ray
sufficient condition at that base; premise (P2) for the irrational-ratio
pairs then needs a direct argument, or a second bad coefficient with
irrational ratio to the first, which would give an incomplete pair as
Proposition 354.7 does. This is recorded as the lead
small_base_two_ray_distance_divergence.

**Outcome.** Transfers conditionally: Proposition 354.5 is proved,
deduction 354.6 makes the divergence premise (P2) and the criterion (P1)
explicit, and Proposition 354.7 marks the bases where (P2) fails and
extends the negative answer to the every-base reading to each of them.

## Problem 349: single rays and the digit recurrence

**Target.** [[problems/additive_bases/E0349/_index|Problem 349]] asks for which
$t,\alpha>0$ the sequence $\lfloor t\alpha^n\rfloor$ is complete. Its page
records the status open on six partial claim pages, none of which settles the
question: Graham's 1964 determination is accepted, and van Doorn's preprint,
Geneson's Salem-base counterexample and three others are pending. The held
sources record Graham's 1964 characterization for $0<t<1$, $1<\alpha<2$, van
Doorn's 2026 extension settling every base $\alpha\ge\varphi$ together
with the elementary integer-base cases (van Doorn's Propositions 1 and 2:
no base outside $[1,2]$ and, at base $2$, only $t=2^{-k}$ gives a
complete sequence), and Geneson's Theorem 9, which refutes the conjectured
completeness for all $t>0$ and $1<\alpha<\varphi$ at one Salem base. The
folder index suggests the Yu--Chen mechanism might bear on integer-base
instances.

**What transports.** At $\gamma=2^{1/m}$, $m\ge2$,
[[theory/additive_bases/L33_dyadic_root_floor_completeness/_index|L33]]
applies the accepted dyadic theorem to indices $j+mr$ and $j+1+ms$.
The coefficient ratio is $\gamma^{-1}$, which is irrational. A late
tail has strictly increasing positive floors, so the two indexed rays
produce distinct values and survive every finite deletion. Thus every
$t>0$ gives a strongly complete single ray at these bases.

This grouping is special to a base with an integral power equal to $2$.
The ungrouped Yu--Chen recurrence does not give the arbitrary-base
classification. The integer-base instances are settled and trivial in
the direction that mechanism proves:
at base $2$ a single ray has $a_{j}-\sum_{i<j}a_i=a_0+\sum_{i<j}u_i>0$ (the
identity of item 6 on the normalization page), so its subset sums below
$a_n$ number at most $2^n$ while $a_n\ge a_02^n$, and the mesh lemma's
hypothesis, a span at least the next weight, never holds; the interlacing
of two rays, $b_i<a_i<2b_i\le b_{i+1}$, is what makes every weight at most
twice its predecessor, and the whole argument rests on it. At a
non-integer base the digit recurrence $a_{i+1}=2a_i+u_i$ with
$u_i\in\{0,1\}$ is absent, and with it the exact doubling blocks, the
coefficient interval $d\{px+qy\}$, the certificate and the modular
invariant. The single-ray analog of Lemma 354.4 is van Doorn's Lemma 5
(held), which the corpus already records.

A separate reading of scope concerns Proposition 11 on the
[[research/erdos_354/geneson_theorem_9_reconstruction|Theorem 9 page]] is
stated and proved for every Pisot or Salem number whose minimal polynomial
has $P(1)\le-3$, so at every such base in $(1,\varphi)$, if any besides
Geneson's exists, there are arbitrarily large $t$ with every
$\lfloor t\gamma^n\rfloor$ even and the sequence incomplete; the source
states Theorem 9 at one base and Proposition 11 in this generality, so this
adds no mathematics.

**What it does not give.** L33 does not classify arbitrary pairs
$(t,\alpha)$ and gives no uniform effective completeness threshold. The
loss of an exact doubling recurrence remains an obstruction at general
noninteger bases; it is not an obstruction at the dyadic roots after
regrouping.

**Next investigation.** An extension to other bases needs an actual
replacement for that recurrence or a different completeness criterion.
The negative outcome of the previous section's investigation would add
an incomplete ray at a rational base.

**Outcome.** The dyadic theorem transfers to all coefficients at the
bases $2^{1/m}$ with the standing of L33. The Geneson reconstruction
bears on incomplete rays exactly as its source card records. Neither
gives the full parameter classification.

## Problem 348: deletion thresholds

**Target.** [[problems/additive_bases/E0348/_index|Problem 348]] asks for which
$0\le m<n$ a complete sequence stays complete after removing any $m$
elements and fails after removing any $n$. Its page records the status
claimed (answered) on
[[problems/additive_bases/E0348/claims/2026_09_09_geneson|Geneson's pending full claim]],
the preprint's classification $m\in\{0,1\}$; the Geneson card records
Theorem 1, that classification, as a preprint claim read for structure only.
The folder index names the problem only as a further target of the same
preprint.

**What transports.** Nothing. The reconstructed pages concern Theorem 9 and
Corollary 12, not Theorem 1, and the Yu--Chen mechanism produces
completeness after every finite deletion: the sets $A_{\alpha,\beta}$ of
its theorem satisfy the first property for every $m$ and the second for no
$n$, so they are examples for no pair $(m,n)$. The problem's content, the
exclusion of $m\ge2$, is an incompleteness mechanism (Geneson's
central-interval Theorem 2 and Lemma 4), for which the folder holds
no reconstruction and the descent argument has no counterpart.

**What it does not give.** Any of the classification, in either
direction.

**Next investigation.** None from this folder. A reconstruction of
Geneson's Sections 2--4 would be a separate compilation task; the card
records that this proof was read for structure only.

**Outcome.** Fails; the only link is the shared source.

## Problem 254 and the threshold $M_2^*$

**Target.** [[problems/integer_sequences/E0254/_index|Problem 254]] asks whether
$A\subseteq\mathbb N$ with $|A\cap(x,2x]|\to\infty$ and
$\sum_{n\in A}\|\theta n\|=\infty$ for every $\theta\in(0,1)$ is complete.
Its page records the problem as solved, with the question proved, on
[[problems/integer_sequences/E0254/claims/2026_07_15_fan|Fan's full claim]],
accepted on Boris Alexeev's built and audited Lean formalization of the
preprint's six-per-interval version; the preprint's Corollary 1.2, at five
elements in every large dyadic interval, is not built, and Snyder's Lean proof
of the statement as posed is a pending full claim. The Fan card records
Corollary 1.2, strong completeness under (1.5) and at least five elements in
every large dyadic interval, as the preprint's confirmation of the conjecture
in strong form, with the proof of Theorem 1.1 unread. The folder reconstructs
Fan's Remarks 4.1 and 4.2, which use Corollary 1.2 as a statement, so the
bound $M_2^*\le5$ below rests on that unbuilt corollary; the built
six-per-interval criterion certifies only $M_2^*\le6$.

**What transports.** Two things, neither toward the proof.

- Sharpness of the growth hypothesis. The reconstructed
  [[research/erdos_354/fan_remark_4_1_reconstruction|Remark 4.1 at base two]]
  proves that $A=\{2^k+1:k\ge1\}$ satisfies (1.5), has exactly one element
  in every $(2^k,2^{k+1}]$ with $k\ge1$, and is incomplete. So the
  hypothesis $|A\cap(x,2x]|\to\infty$ of Problem 254 cannot be weakened to
  one element in every large dyadic interval, while Corollary 1.2 weakens
  it to five; the exact threshold $M_2^*$ lies in $\{2,3,4,5\}$ and is
  open in the source.
- A two-per-interval family. By the reconstructed
  [[research/erdos_354/fan_remark_4_2_reconstruction|Remark 4.2]], every
  $A_{\alpha,\beta}$ with $\alpha/\beta$ not a power of $2$ and one
  coefficient not a dyadic rational satisfies (1.5) and has two elements
  in every large dyadic interval. The Yu--Chen theorem, if it stands,
  makes these sets strongly complete when the ratio is irrational, and
  Corollary 354.3 does so for almost every coefficient on each
  rational-ratio line: a family outside the reach of Corollary 1.2 and
  consistent with $M_2^*=2$, the value that Remark 4.2 shows would imply
  Hegyvári's conjecture. Fan's Proposition 4.3 (its statement read in the
  canonical conversion of the source's Section 4) says that the preprint's
  three-component criterion cannot give $M_2^*\le4$ and that a different
  mechanism may be needed; the descent is
  a different mechanism, but it consumes the digit recurrence of two
  rays, not the per-interval count, so it says nothing about a general
  set with two elements per dyadic interval.

Also, item 6 of the normalization page, the gap bound
$\operatorname{gap}(P_n)\le N$ from $c_{j+1}-\sum_{i\le j}c_i\le c_0$, is
the two-ray instance of the Burr--Erdős lemma that Fan records as
Lemma 2.1 (bounded $\Delta(S)$ makes the subset sums syndetic); the
corpus holds neither Burr--Erdős nor a general proof.

**What it does not give.** Nothing toward Problem 254 itself: the folder
holds no reconstruction of Theorem 1.1 or of the three-component
criterion (Theorem 2.2) behind it, and the descent does not extend to
sets without the digit structure.

**Next investigation.** None from this folder. The compilation task for
Problem 254 is a reconstruction of Fan's Theorem 2.2 with Sections 3--4,
which would also fix the standing of premise (P1) above; for $M_2^*$, the
question whether a two-per-interval set with (1.5) can be incomplete has
no candidate in the corpus, every incomplete two-ray set known with one
coefficient not a dyadic rational (Hegyvári 1989, Jiang--Ma, Fang--He, all
erdosproblems.com-attested) having a ratio that is a power of $2$ and hence a
single ray as a set, while a pair of dyadic rationals fails (1.5).

**Outcome.** Transfers the sharpness example and the two-per-interval
family as author-recorded context for $M_2^*$; fails as a route to
Problem 254.

## Problem 124: mixed power sets

**Target.** [[problems/diophantine_problems/E0124/_index|Problem 124]] asks
whether, for integers $3\le d_1<\cdots<d_r$ with $\sum_i1/(d_i-1)\ge1$,
every large integer is a sum of at most one element from each
$P(d_i,0)$, the sums of distinct powers of $d_i$, and the same with
$P(d_i,k)$ when the $d_i$ are coprime. Its page records the status open on
four partial claim pages: Burr, Erdős, Graham and Li 1996 and Bergelson and
Simmons 2015 are accepted, and Alexeev's Lean proof of the first question and
[[problems/diophantine_problems/E0124/claims/2026_09_09_fan|Fan's Theorem 1.5]]
are pending. The Fan card records Theorem 1.5 (v5, p. 7) at statement level
only; the theorem says that for a nonempty finite
$D\subseteq\mathbb N_{\ge2}$ with no two elements powers of the same
integer, $\bigcup_{d\in D}\{d^n\}$ is strongly complete whenever
$D=D_1\cup D_2\cup C$ is a partition into nonempty parts with $\gcd(C)=1$
and $\sum_{d\in D_i}1/(d-1)\ge1$ for $i=1,2$, one component fewer than the
Bergelson--Simmons theorem as the source states it. The folder index names
the problem only as a further target of the same preprint.

**What transports.** Nothing. The objects are single-coefficient rays
$\{d^n\}$ at distinct integer bases at least $3$, without floors; the
descent needs two rays at base $2$ with the digit recurrence and the
interlacing $b_i<a_i<2b_i\le b_{i+1}$, none of which a power set has.
Fan's Theorem 1.5 is not reconstructed, and its proof (the source's
Section 7) runs through the three-component criterion, not through
anything in the folder. The only shared step is elementary: the
bounded-$\Delta$ argument that makes subset sums syndetic, which is
Fan's Lemma 2.1 and, for two rays, item 6 of the normalization page; that
is a resemblance of tools, not a transfer of a result.

**What it does not give.** Anything about either question of the problem.

**Next investigation.** None from this folder; the compilation task is a
reconstruction of Theorem 1.5 with Theorem 2.2.

**Outcome.** Fails.

## No further consumer

**The mechanism at its actual scope.** The reusable content of the folder
is a descent: for two interlaced base-$2$ rays, a long exact doubling
block followed by a nonzero digit lowers the modular run invariant of
every later layer, with a finite certificate making the descent uniform;
its inputs are the interlacing, the digit recurrence and a reduced ratio
$(p,q)$ at the block's first layer with $K\ge K_*(p,q)$. A consumer would
be recognized by a set that is a union of two rays $\lfloor2^n\alpha\rfloor$,
$\lfloor2^n\beta\rfloor$ up to finitely many elements, or by a question
about subset sums of such a set.

**The search.** The problems, research and theory trees were searched for
complete and strongly complete sequences, subset sums of distinct terms,
floors of geometric sequences, dyadic intervals and the named authors.
Beyond the targets above, the corpus holds:
[[problems/additive_bases/E0343/_index|Problem 343]] and
[[problems/additive_bases/E0344/_index|Problem 344]] (subcompleteness under a
density condition; proved), [[problems/additive_bases/E0345/_index|Problem 345]]
(thresholds of completeness of the powers $n^k$; open, on polynomial
sequences), [[problems/additive_bases/E0346/_index|Problem 346]] (strongly
complete sequences that lose completeness under every infinite deletion;
solved), [[problems/additive_bases/E0347/_index|Problem 347]] (a sequence with
ratio tending to $2$ whose cofinite subsequences have subset sums of
density $1$; proved), [[problems/additive_bases/E0351/_index|Problem 351]]
(strong completeness of $p(n)+1/n$; proved),
[[problems/integer_sequences/E0253/_index|Problem 253]] (disproved by Cassels),
[[problems/diophantine_problems/E0246/_index|Problem 246]] and
[[problems/diophantine_problems/E0123/_index|Problem 123]] (sums of distinct
$a^kb^l$ and $a^kb^lc^m$; proved) and
[[problems/diophantine_problems/E0125/_index|Problem 125]] (disproved). None
consumes the descent: the resolved ones need nothing, Problem 345 concerns
polynomial sequences, and the two-ray sets are not examples for Problem
347, since their sorted terms have ratios alternating near $\alpha/\beta$
and $2\beta/\alpha$ and so do not tend to $2$; for Problem 346, refuted by
a counterexample, the ratios decide nothing, since its hypotheses ask that
completeness be lost under every infinite deletion, which the descent does
not address and which fails for the pair $(3\sqrt2,3)$ after the deletion
of $\{3\cdot2^m:m\ge4,\ 4\mid m\}$; a single ray, whose ratios tend to
$2$, has at most $2^n$ subset sums below $a_n\ge\lfloor\alpha\rfloor2^n$
and both problems are resolved. The separate
[[theory/additive_bases/L33_dyadic_root_floor_completeness/_index|L33]]
and its [[research/leads/dyadic_root_floor_completeness/_index|research account]]
concern dyadic-root single rays, using the accepted two-ray theorem
through exponent regrouping.

**Outcome.** No further consumer of the direct descent is identified
among these targets. The separate dyadic-root application to Problem
349 is described above; it does not supply an arbitrary-base descent.

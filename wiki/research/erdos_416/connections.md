---
name: research/erdos_416/connections
title: "Connections of the Problem 416 reconstructions: the two distinct-totient counts, the general scale, and the multiplicity problems"
desc: |
  Assesses the connections from the reconstructed doubling-law and
  cluster-interval arguments to the rest of the corpus: the cluster-interval
  structure and a proved limsup > 1 for the ratio of Problem 417 (a lead),
  the reduction of the general-scale law to one balance estimate for the
  accepted family (a lead), and the precise obstructions for Problems 821,
  694, 51, 49, 1003, 1004 and the two totient leads.
created: 2026-09-28T06:18:00Z
updated: 2026-10-19T04:19:07Z
---

[[research/erdos_416/_index|..]]

***

**Purpose and standing.** This page draws the connections from the
author-recorded reconstructions in
[[research/erdos_416/_index|the Problem 416 folder]] to the rest of the corpus.
Each section names its exact target with the status the target's page records,
states what the reconstructed mechanism gives when transported, with a proof
where one is given here, states what it does not give and why, and names the
next investigation with what each outcome would establish. Every new statement
below is author-recorded, no status or tier changes, and each imported input
keeps the standing its library page records. The statements were independently
reviewed as they stood on 2026-09-28T13:50:48Z by seven focused reviews graded
in
[[research/erdos_416/evidence/verify/connections_grade|the connections grade]],
which passes all seven and accepts ten corrections, C1--C10, since applied; it
assigns no tier. After the review, the Target paragraphs of the Problem 417,
416, 821 and 51 sections were updated to the standing their problem pages
record; no statement or proof changed. The literature was not searched beyond
the held corpus, so no novelty is claimed for the statements proved here.

**Notation.** For real $x$, $T(x)$ is the set of totient values in $[1,x]$
and $V(x)=|T(x)|$, as on the reconstruction pages. Following
[[problems/arithmetic_functions/E0417/_index|Problem 417]],
$V'(x)=\#\{\varphi(m):1\le m\le x\}$ counts the distinct totients of the
integers up to $x$. For a totient $v$ let $f_{\min}(v)$ be its least
preimage and $r(v)=f_{\min}(v)/v\ge1$ its least-preimage ratio; for
$k\ge1$ let $V(x;k)$ be Ford's count of the totients in $[1,x]$ all of
whose preimages are divisible by $k$, and $S(k)$ the set of such totients.
$\pi(x)$ counts the primes up to $x$, and $c_0>0$ is Chebyshev's constant,
$\pi(x)\ge c_0x/\log x$ for $x\ge2$.

**Imported inputs, at their standing.**

- (F) Ford's Theorem 1 in the form used on
  [[research/erdos_416/zeraoulia_theorem_1_1_reconstruction|the preprint's page]]:
  $V(x)=M(x)e^{E(x)}$ with $|E(x)|\le K$ for $x\ge x_1$, where
  $M(x)=(x/\log x)e^{\Psi(x)}$, together with that page's Step 1 bound
  $|\psi_c'(t)|\le K'/t$ for $\psi_c(t)=\Psi(c^t)$, $\log(c^t)\ge e^e$, with
  $K'=2C+D+|D+\tfrac12-2C|$. Refereed source at statement level; the
  derivative bound is author-recorded there.
- (F8) Ford's Theorem 8
  ([[../library/arithmetic_functions/ford_1998_distribution_totients/_index|card]],
  §1.3 of the held conversion): if $d$ is a totient all of whose
  preimages are divisible by $k$, then
  $V(x;k)\gg_\varepsilon d^{-1-\varepsilon}V(x)$.
  Ford calls it a trivial corollary of the proof of Theorem 2, and the
  paper's §7 lists the witnesses $d=2^{18}\cdot257$ for $k\in\{2,4,8\}$, $d=54$
  for $k\in\{3,9\}$, $d=12500$ for $k=5$, $d=294$ for $k=7$ and $d=110$
  for $k=11$, with none found for $k=6$ or $k=10$. Statement-level import;
  the witness $d=54$ is verified below.
- (W) The order of magnitude $V(x)\asymp V'(x)$. Page 7 of the held
  17-page manuscript of Pollack, Pomerance and Treviño
  ([[../library/primes/pollack_et_al_2013_sets_monotonicity_euler_totient_function/_index|card]])
  states that Ford showed $V(x)\asymp W(x)\asymp Z(x)$ for large $x$, with
  $W$ their name for $V'$ and $Z$ the main term of Theorem 1, citing
  §§4–5 of the corrected arXiv version of Ford's paper. Ford's theorems as
  held do not mention $V'$, and Ford's §5 was not reread here, so (W) is
  imported as the cited authors' reading of Ford. A second route to
  $V\ll V'$ is Lemma 4.1(iii) of the same manuscript, reconstructed with two
  imported counts on
  [[research/erdos_49/lemma_4_1_reconstruction|the Problem 49 folder's page]].
- (KK) The write-up's Proposition 4.1, estimates (3)–(5), at the standing
  recorded on
  [[research/erdos_416/kruer_kohlmeyer_theorem_1_1_reconstruction|the Theorem 1.1 page]]:
  kernel acceptance of a Lean file that is not held, with no prose proof.

**The search.** The problems, research and theory trees were searched for
Euler's function, totient values and preimages, the counting function $V$
and the sum-of-divisors analogs. The hits are the arithmetic-function
problems named below, [[problems/primes/E0049/_index|Problem 49]] with its
research folder, the irrationality problems 249, 250 and 252 with the
claim L16, and pages where $\varphi$ denotes another function. The library
cards of the totient literature (Erdős 1935, Maier–Pomerance 1988, Ford
1998, Pollack–Pomerance–Treviño 2013, Graham–Holt–Pomerance 1999, Ford
2020, Li 2026, the Problem 694 note, Baker–Harman 1998 and Lichtman 2022)
were read at card level, and the conversions of Ford 1998, Maier–Pomerance
1988 and the 2013 manuscript were read where they are cited.

## Problem 417: the two counts of distinct totients

**Target.** [[problems/arithmetic_functions/E0417/_index|Problem 417]] asks
whether $\lim V(x)/V'(x)$ exists and whether it is greater than $1$. The
page records the status open with no claim page, records the results of this
section under its Progress, and records under its Current assessment Theorem
2.2 of the OpenAI release, which bears on the problem without claiming it; no
status search was made here beyond the held corpus, whose only statements
about $V'$ are (W) and a remark of Maier and Pomerance recorded next. Write
$R(x)=V(x)/V'(x)$ and $V_0(x)=V(x)-V'(x)$.
A notational trap: the closing section of Maier and Pomerance
([[../library/arithmetic_functions/maier_1988_number_distinct_values_euler_s_function/_index|card]],
§5 of the held conversion) writes $V'(x)$ for
$\#\{\varphi(n)\le x:n>x\}$, a different count of the same order as $V$,
and writes $V_0(x)$ for the cardinality of $\{\varphi(n)\le x:n>x\}$ minus
$\{\varphi(n):n\le x\}$, which is the $V_0$ here; the authors call a lower
bound for it a harder question that their methods do not give.

**Lemma 417.1 (elementary facts, author-recorded).**

- (a) $V'(x)=\#\{v\in T(x):f_{\min}(v)\le x\}$ and
  $V_0(x)=\#\{v\in T(x):f_{\min}(v)>x\}$; hence $R(x)\ge1$ and
  $R(x)=R(\lfloor x\rfloor)$.
- (b) $V'(n+1)-V'(n)\in\{0,1\}$ for integers $n$, and
  $V'(x)\ge\pi(x)\ge c_0x/\log x$ for $x\ge2$.
- (c) For integers $n\ge2$,
  $|R(n+1)-R(n)|\le2n/V'(n)^2\le(2/c_0^2)(\log n)^2/n$.

*Proof.* (a) Since $\varphi(m)\le m$, every value of an argument $m\le x$
lies in $T(x)$, and $v\in T(x)$ is such a value exactly when its least
preimage is at most $x$; both counts depend on $x$ through
$\lfloor x\rfloor$. (b) Passing from $n$ to $n+1$ adds one argument, hence
at most one value; the primes $p\le x$ give the distinct values
$\varphi(p)=p-1$. (c) Put $A=V(n)$, $B=V'(n)$,
$\delta=V(n+1)-V(n)\in\{0,1\}$ and $\epsilon=V'(n+1)-V'(n)\in\{0,1\}$.
Then $R(n+1)-R(n)=(B\delta-A\epsilon)/(B(B+\epsilon))$, so
$|R(n+1)-R(n)|\le(B+A)/B^2\le2A/B^2\le2n/B^2$, using $B\le A\le n$; (b)
gives the last bound. $\square$

**Proposition 417.2 (the cluster interval; transfer of Step 7).** Let
$\alpha=\liminf_nR(n)$ and $\beta=\limsup_nR(n)$ over the integers, in
$[1,\infty]$. The set of subsequential limits of $R(n)$ is the closed
interval $[\alpha,\beta]$, the same set is obtained as $x\to\infty$ through
the reals, and $\beta<\infty$ under (W). Consequently exactly one of the
following holds: $R(x)$ converges; or $R$ has continuum many limit points.

*Proof.* By Lemma 417.1(c) the adjacent variation $|R(n+1)-R(n)|$ tends
to $0$. Step 7 of
[[research/erdos_416/zeraoulia_theorem_1_1_reconstruction|the preprint's page]]
uses nothing else: for finite $y$ with $\alpha<y<\beta$ and any $n_0$
there are $n_1,n_2>n_0$ with $R(n_1)<y<R(n_2)$, and the last index $n$ of
the block between them on the initial side of $y$ has $y$ between $R(n)$
and $R(n+1)$, so $|R(n)-y|\le(2/c_0^2)(\log n_0)^2/n_0$; letting
$n_0\to\infty$ makes $y$ a limit point. The endpoints are limit points by
definition, finite or not, and the cluster set is closed, so it is
$[\alpha,\beta]$. By 417.1(a), $R(x)=R(\lfloor x\rfloor)$, so the real and
integer cluster sets coincide. Under (W), $R$ is bounded and
$\beta<\infty$. If $\alpha=\beta$ the sequence converges; if
$\alpha<\beta$ the interval is nondegenerate, hence uncountable. $\square$

Nothing about totients enters beyond the unit jumps and the trivial lower
bound for $V'$: this is the preprint's Lemma 3.1 and Theorem 3.4 with $V'$
in the denominator.

**Theorem 417.3 (the ratio exceeds one infinitely often;
author-recorded).** There is $\eta>0$ such that $V_0(x)\ge\eta V(x)$ for
arbitrarily large $x$. Hence $\beta=\limsup_xR(x)\ge1/(1-\eta)>1$, and if
the limit asked for in Problem 417 exists, it exceeds $1$.

Inputs: (F), (F8) with $k=3$ and $d=54$, and Chebyshev's bound.

*Proof.* Step 1, the witness. The preimages of $54$ are exactly $81$ and
$162$. If $\varphi(m)=54=2\cdot3^3$ with $m$ odd and $3\mid m$, write
$m=3^tm''$ with $m''$ odd and $3\nmid m''$; then
$\varphi(m)=2\cdot3^{t-1}\varphi(m'')$ forces $\varphi(m'')=3^{4-t}$, an
odd value, so $m''=1$, $t=4$ and $m=81$. If $m$ is odd and $3\nmid m$,
each odd prime factor $q$ of $m$ contributes the even factor $q-1$ to
$\varphi(m)$, so $m=q^e$ for one odd prime $q$ with $q^{e-1}(q-1)=54$,
which forces $e=1$ and $q=55$, not prime ($e=2$ has no solution and
$e\ge3$ needs $q^2\mid54$). If $m=2^bm'$ is even with $m'$ odd and
$b\ge1$, then $\varphi(m)=2^{b-1}\varphi(m')$; as $54$ carries one factor
$2$ and $\varphi(m')$ is even unless $m'=1$, which gives a power of $2$,
we get $b=1$, $\varphi(m')=54$ with $m'$ odd, $m'=81$ and $m=162$. Both
preimages are divisible by $3$, so (F8) with $k=3$ gives $c>0$ and $x_0$
with $V(x;3)\ge cV(x)$ for $x\ge x_0$.

Step 2, the least preimage on $S=S(3)$. If every preimage $m$ of $v$ is
divisible by $3$, then $m/\varphi(m)\ge3/2$ for each, so
$f_{\min}(v)\ge\tfrac32v$. Hence every $v\in S$ with $2x/3<v\le x$ has
$f_{\min}(v)>x$, and by 417.1(a)

$$
V_0(x)\ \ge\ N(x):=\#\{v\in S:\ 2x/3<v\le x\}.
$$

Step 3, a geometric decomposition. Put $\lambda=3/2$. The intervals
$(x/\lambda^{j+1},x/\lambda^j]$, $j\ge0$, partition $(0,x]$, so

$$
V(x;3)=\sum_{j\ge0}N(x/\lambda^j),
$$

a finite sum since $1\notin S$ (its preimage $1$ is not divisible by $3$)
and so $N(z)=0$ for $z<2$.

Step 4, the sum of $V$ along the geometric sequence. There is a constant
$C_1$, depending only on Ford's constants, with
$\sum_{j\ge0}V(x/\lambda^j)\le(3C_1+o(1))V(x)$. For the $j$ with
$z=x/\lambda^j\ge x^{1/2}$ and $x$ large, (F) gives

$$
\frac{V(z)}{V(x)}\le e^{2K}\,\frac zx\,\frac{\log x}{\log z}\,
e^{\Psi(z)-\Psi(x)}\le2e^{2K}\lambda^{-j}e^{\Psi(z)-\Psi(x)},
$$

and with $x=\lambda^t$, $z=\lambda^{t'}$, $t'\ge t/2$, the derivative
bound of (F) gives

$$
|\Psi(z)-\Psi(x)|=|\psi_\lambda(t')-\psi_\lambda(t)|\le K'\log(t/t')\le K'\log2.
$$

So $V(x/\lambda^j)\le C_1\lambda^{-j}V(x)$ with $C_1=2^{1+K'}e^{2K}$, and
these $j$ contribute at most $C_1V(x)/(1-1/\lambda)=3C_1V(x)$. The
remaining $j$, at most $\log_\lambda x+1$ of them, have
$V(x/\lambda^j)\le x/\lambda^j\le x^{1/2}$, contributing
$O(x^{1/2}\log x)=o(V(x))$ by $V(x)\ge\pi(x+1)\ge c_0x/\log x$.

Step 5, conclusion. Suppose $N(y)\le\eta V(y)$ for all $y\ge y_0$, with
$\eta=c/(6C_1)$. For $x\ge y_0$ the blocks with $x/\lambda^j<y_0$ lie in
$(0,y_0)$ and contribute at most $V(y_0)$ to the sum of Step 3, so

$$
V(x;3)\le\eta\sum_{j\ge0}V(x/\lambda^j)+V(y_0)
\le\bigl(\tfrac c2+o(1)\bigr)V(x)+V(y_0)<cV(x)
$$

for large $x$, contradicting Step 1. Hence $N(y)>\eta V(y)$ for
arbitrarily large $y$, and for those $y$,
$V'(y)=V(y)-V_0(y)\le(1-\eta)V(y)$, that is $R(y)\ge1/(1-\eta)$. The last
sentence of the statement is Proposition 417.2: if the limit exists it
equals $\beta$. $\square$

Remarks. (i) The constant $\eta=c/(6C_1)$ depends on the implied constant
of (F8) at $d=54$ and on Ford's $O(1)$, neither of which is explicit, so
$\eta$ is not numerical. (ii) Any of Ford's witnesses serves. With $k=4$
and $d=2^{18}\cdot257$ one has $f_{\min}(v)\ge2v$ on $S(4)$, the blocks
are dyadic, and the doubling law of
[[research/erdos_416/kruer_kohlmeyer_theorem_1_1_reconstruction|the Theorem 1.1 page]]
replaces Step 4 by $\sum_jV(x/2^j)\sim2V(x)$; the proof above uses only
the refereed inputs. (iii) The mechanism is the lower bound on every
preimage that the sets $S(k)$ carry; the reconstructed pages supply the
bookkeeping (unit jumps for 417.2, the derivative bound for Step 4) and
not the arithmetic.

**Proposition 417.4 (conditional).** If $N(y)\ge\eta'V(y)$ for all large
$y$, then $\liminf R\ge1/(1-\eta')>1$. The premise is the short-interval
form of (F8); Ford's Theorem 4, which Ford obtains by a simple modification
of the proofs of Theorems 1 and 2 and which gives
$V_k(x+y)-V_k(x)\asymp(y/(x+y))V(x+y)$ for $y\ge x^\theta$ and possible
multiplicities $k$, makes the same localization plausible for $V(x;k)$,
but the held paper does not state it. *Proof.* Immediate from Step 2.
$\square$ Neither this nor Theorem 417.3 decides whether the limit exists.

**What it does not give.**

- The existence of the limit. Steps 1–6 of the preprint's argument locate
  $c$ as a limit point through $\log V(c^t)=t\log c+\eta_c(t)+O(1)$ and
  the exact telescoping of consecutive quotients. $R=V/V'$ compares two
  functions at one scale, no product of consecutive values of $R$
  telescopes, and no asymptotic for $V'$ beyond (W) is held, so no
  candidate value is produced and the near-hit mechanism does not
  transfer.
- The pair family. A retained pair $(b,p)$ with core $b=\varphi(m_0)$ from
  a record $m_0=a\prod_jp_j$ gives the value $v=b(p-1)$ the preimage
  $m_0p$, so $f_{\min}(v)\le(m_0/b)\,(p/(p-1))\,v$. If the retained records
  had $m_0/\varphi(m_0)\le K(\varepsilon)$ (plausible from the record
  conditions, which resemble the spacing conditions under which Lemma
  4.1(iii) of the Problem 49 folder bounds $n/\varphi(n)$, but stated in
  no held text), then all but $(\varepsilon+o(1))V(y)$ totients $v\le y$
  would satisfy $f_{\min}(v)\le2K(\varepsilon)v$, which gives again only
  $R\ll1$: an upper bound on least preimages cannot produce the lower
  bounds that $V_0$ counts.

**Reformulation and finite-range numbers (exploratory).** By 417.1(a),
$V_0(x)=\#\{v\in T(x):r(v)>x/v\}$, so the limit in Problem 417 is a
statement about the joint distribution of $v/x$ and $r(v)$ over the
totients $v\le x$. Suppose (H1) $V(ux)/V(x)\to u$ for each fixed
$u\in(0,1]$, the general-scale law of the next section, known only for
$u$ a power of $1/2$; and (H2) for each fixed $u\in(0,1]$ and $t\ge1$,
$\#\{v\le ux:r(v)\le t\}/V(ux)\to G(t)$ for a nondecreasing function $G$ on
$[1,\infty)$ with values in $[0,1]$. Then, bracketing the indicator
$1[r(v)\le x/v]$ on $(u_{i-1}x,u_ix]$ between $1[r(v)\le1/u_i]$ and
$1[r(v)\le1/u_{i-1}]$ over a grid and refining it,

$$
\frac{V'(x)}{V(x)}\to\int_0^1G(1/u)\,du,\qquad
\frac{V_0(x)}{V(x)}\to\int_1^\infty\bigl(1-G(t)\bigr)\frac{dt}{t^2},
$$

and $R(x)$ converges to the reciprocal of the first integral. This is a
frame, not a route: it names the two limits it assumes, and (H2) is
exactly the least-preimage distribution that no held source studies.

A computation made for this page sieves Euler's function for all
$n\le6.2\cdot10^7$, which covers every preimage of every totient
$v\le10^7$: an integer with at most nine distinct prime factors has
$n/\varphi(n)\le\prod_{p\le23}p/(p-1)<6.12$, and one with ten or more has
$\varphi(n)\ge\varphi(2\cdot3\cdot5\cdots29)>10^9$. It gives, as
$(x;V(x),V'(x),V_0(x);R(x))$:
$(10^4;2374,2160,214;1.0991)$, $(10^5;20254,18412,1842;1.1000)$,
$(10^6;180184,163861,16323;1.0996)$ and
$(10^7;1634372,1485793,148579;1.1000)$, so $V_0/V$ is $0.0901$, $0.0909$,
$0.0906$ and $0.0909$. Every totient $v\le10^7$ has $r(v)\le2.0414$, the
maximum at $v=2037248=\varphi(3\cdot5\cdot17\cdot47\cdot347)$ with
$f_{\min}(v)=4158795$ (up to $10^6$ the maximum is $2.0355$ at
$v=5888=\varphi(3\cdot5\cdot17\cdot47)$), so in this range every element counted
by $V_0(x)$ lies in $(x/2.0414,x]$, and only the ten totients $v\le10^7$ with
$r(v)>2$ ($5888$, $10496$, $17408$, $276736$, $2037248$, $5268992$, $5331968$,
$6983168$, $8043008$ and $8749568$) can fall in $(x/2.0414,x/2]$. Among the
totients in $(5\cdot10^6,10^7]$ the proportions with $r(v)\ge1.1$, $1.25$, $1.5$
and $2$ are $0.319$, $0.266$, $0.194$ and $0.00001$. The sets behind Theorem
417.3 are far smaller than $V_0$: $V(10^7;3)/V(10^7)\approx0.0013$, and no
totient up to $10^7$ has all preimages divisible by $4$ (Ford's witness
$2^{18}\cdot257$ exceeds $10^7$). The near-constancy $R(x)\approx1.10$ over
three decades is a finite observation that proves nothing about the limit; it is
recorded as the value a limit-existence proof would have to meet.

**Next investigation.**

1. The short-interval form of (F8): show $V(x;3)-V(2x/3;3)\gg V(x)$, or
   the $k=4$ form on $(x/2,x]$, by localizing Ford's §5 construction as
   Ford's Theorem 4 does for $V_k$. A positive outcome makes Proposition
   417.4 unconditional, $R(x)\ge1+\eta'$ for all large $x$; a negative
   one, a proof that $S(3)\cap(2x/3,x]$ is $o(V(x))$ along a sequence,
   would mean (F8) is carried by other blocks at those scales and would
   send the argument to another witness set.
2. The limit itself: prove or refute a limiting law (H2) for $r(v)$ over
   totients, for which Ford's Theorems 10–11 and the classification by
   $V(x;k)/V(x)$ Ford proposes for the asymptotic formula are the tools. No
   support bound is available: by (F8) at $k=4$ with Ford's witness
   $2^{18}\cdot257$, every $v\in S(4)$ other than a power of $2$ has $r(v)>2$,
   since its least preimage $m$ has $4\mid m$ and an odd prime factor, so
   $m/\varphi(m)>2$; hence $1-G(2)\ge c_4>0$ for any limiting $G$, and the law
   to prove or refute is (H2) without a support bound. With (H1) this gives the
   limit and its value through the frame above; a proof that $V_0(x)/V(x)$
   oscillates answers the first question negatively and, by 417.2, gives
   continuum many limit points.
3. Extend the computation to $10^9$–$10^{10}$ by a segmented sieve of least
   preimages, on the model of the preprint's §8 computation of $V$: a
   drift of $R$ away from $1.10$ would show that the observed constancy is
   a small-range effect.

**Outcome.** Transfers in part: the cluster-interval structure transfers
with proof (Proposition 417.2), and the ratio exceeds $1$ infinitely often
(Theorem 417.3), so the second question's answer is yes whenever the
first's is; the existence of the limit is untouched. Filed as the lead
[[research/leads/distinct_totient_preimage_ratio/_index|distinct_totient_preimage_ratio]].

## Problem 416 at a general scale: the accepted family with another balance

**Target.** The variant of [[problems/arithmetic_functions/E0416/_index|Problem 416]]
that Erdős posed with it, $V(cx)/V(x)\to c$ for every fixed $c>1$,
recorded in Guy's B36
([[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|card]])
and in §1.2 of Ford's paper, which says that the method of the paper's
Theorem 1 falls short of it. It is not a clause of the erdosproblems.com
statement, whose first question is $c=2$, answered as the problem page records,
and whose second is the asymptotic formula; the problem page records the
standing claimed, through the OpenAI release's pending full claim on the second
question. The variant itself is settled: the problem page records the same
release's fixed-scale law, $V(cx)/V(x)\to c$ for every fixed real $c>0$, as
[[problems/arithmetic_functions/E0416/claims/2026_09_25_openai|an accepted partial claim]]
on its built and audited Lean declaration. It supersedes this section's
reduction as a route to the variant, as the closed lead
[[research/leads/general_scale_totient_doubling/_index|general_scale_totient_doubling]]
records; the reduction stays recorded below. Before the release, the only claim
for $c\ne2$ was the preprint's, reconstructed in this folder: $c$ is a limit
point of $V(cn)/V(n)$ and the cluster set is a closed interval of unknown width;
the integer powers of $2$ are settled by the accepted doubling law by
telescoping, as recorded below.

**What transports.** The prose deduction of the doubling law uses $c=2$ in
exactly one place, the balance estimate (5). Two lemmas make this precise.

*Lemma 416.1 (finite counting inequality at scale $c$).* In the setting of
[[research/erdos_416/kruer_kohlmeyer_lemma_2_1_reconstruction|the Lemma 2.1 page]]
(finite $T_0\subseteq T$, $f\colon P\to T$, $P_0=f^{-1}(T_0)$, and the
counts $M,M_0,E,E_0$), for every real $c\ge1$,

$$
\bigl|\,|T|-c|T_0|\,\bigr|\le\bigl|\,|P|-c|P_0|\,\bigr|+\max(1,c-1)\,(M+E).
$$

*Proof.* The exact identity of that page reads
$|T|-c|T_0|=(|P|-c|P_0|)+(M-cM_0)-(E-cE_0)$. Since $0\le M_0\le M$, the
number $M-cM_0$ lies in $[-(c-1)M,M]$, so $|M-cM_0|\le\max(1,c-1)M$;
likewise for $E$. $\square$ For $1\le c\le2$ the constant is $1$, and
$c=2$ is that page's display (2).

*Lemma 416.2 (relative error controls the quotient at scale $c$).* If
$v>0$, $w\ge0$, $0\le\delta\le1/2$ and $|w-cv|\le\delta w$, then
$|w/v-c|\le2c\delta$.

*Proof.* From $(1-\delta)w\le cv$ and $\delta\le1/2$, $w\le2cv$, so
$|w/v-c|=|w-cv|/v\le\delta w/v\le2c\delta$. $\square$

*Proposition 416.3 (conditional general-scale law).* Fix $c>1$. Suppose
that for every $0<\varepsilon<1/2$ there are retained families
$(P_y,f_y)$, one for each large real $y$, satisfying (3) and (4) of
Proposition 4.1 and

$$
\text{(5}_c\text{)}\qquad A_y-cB^{(c)}_y=o(A_y),\qquad
B^{(c)}_y=\#\{a\in P_y:\ f_y(a)\le y/c\}.
$$

Then $V(cx)/V(x)\to c$ as real $x\to\infty$.

*Proof.* Follow Steps 1–5 of
[[research/erdos_416/kruer_kohlmeyer_theorem_1_1_reconstruction|the Theorem 1.1 page]]
with $T_0=T(y/c)$. Step 1 is Lemma 416.1, with
$|P|-c|P_0|=A_y-cB^{(c)}_y=:D^{(c)}_y$ because
$P_0=f_y^{-1}(T(y/c))$ is the set of pairs with value at most $y/c$. Step
2 is unchanged. Step 3 gives $D^{(c)}_y=o(V(y))$ from (5$_c$) and
$A_y\le2V(y)$. In Step 4, for a given $\delta>0$ choose
$\varepsilon<\min(1/2,\delta/(2\max(1,c-1)))$; then
$|V(y)-cV(y/c)|\le\max(1,c-1)\varepsilon V(y)+o(V(y))\le\delta V(y)$ for
all large $y$, that is $|V(cx)-cV(x)|\le\delta V(cx)$. Step 5 is
Lemma 416.2 with $w=V(cx)$, $v=V(x)$ and $\delta=\min(1/2,\eta/(4c))$,
giving $|V(cx)/V(x)-c|\le\eta/2$. $\square$

Two remarks. First, (3) and (4) do not mention $c$: they concern one
family at one scale. So the family the accepted file constructs, whose (3)
and (4) are the kernel-accepted declarations named on the Theorem 1.1
page, serves for every $c$, and the general-scale law at a given $c$
reduces, at that standing, to the single balance statement (5$_c$) for
that family. Second, per the write-up's §4.3 as read on the Theorem 1.1
page, (5) comes from a common mass $H(y)$ with $A_y/H(y)\to1$ and
$B_y/H(y)\to1/2$ over cores $b$ with $\log b\le G(y)=o(\log y)$; if the pairs
above a core $b$ are the primes $p$ in an interval whose upper end is $y/b$ for
$p-1$, so that $b(p-1)\le y$, then the $c=2$ balance forces the lower ends of
these intervals to be negligible in aggregate, and $B^{(c)}_y/H(y)\to1/c$ by the
same uniformity of the prime number theorem ($\pi(u/c)/\pi(u)\to1/c$ uniformly
for $u\ge y^{1-o(1)}$), so (5$_c$) holds for every $c>1$. Whether the accepted
development counts in this way is not established: the file is not held, and the
mass is defined only there.

What the accepted $c=2$ law adds without any premise, for $c=2^{1/m}$
with $m\ge2$: the exact identity
$\prod_{j=0}^{m-1}R_c(c^jx)=V(2x)/V(x)\to2$ shows that the geometric mean
of $R_c$ over any $m$ consecutive scales tends to $c$, a finite-block form
of the preprint's Step 2 with no error term. As in the preprint this
yields near-hits and no width control; for $m=2$ it forces
$\alpha_c\beta_c=2$ for the reconstructed cluster interval
$[\alpha_c,\beta_c]$ (a sequence realizing $\alpha_c$ at $x$ realizes
$2/\alpha_c$ at $cx$, and symmetrically), which does not make the interval
degenerate. For $c=2^m$ with an integer $m\ge2$ the same telescoping settles the
variant outright at the standing of the accepted file:
$V(2^mx)/V(x)=\prod_{i=0}^{m-1}V(2^{i+1}x)/V(2^ix)\to2^m$ as real $x\to\infty$,
so the cluster set is $\{c\}$; and for $c=2^{k/m}$ the product of $R_c$ over $m$
consecutive scales tends to $2^k$.

**What it does not give.** No asymptotic formula, since the mass depends
on $\varepsilon$ as the Theorem 1.1 page explains; no rate; nothing for $c$
outside the integer powers of $2$ until (5$_c$) is verified, so the preprint's
dichotomy stands for every $c>1$ that is not an integer power of $2$; and no
prose proof, since (3) and (4) keep the standing of the accepted file.

**Next investigation.** Obtain the accepted file (its URL, size and hash
are on the write-up's card), read the definition of the pair family, the
mass $H(y)$ and the declaration `power_corePairs_count_asymptotic` (line
63482 in the write-up's map) with its dependencies, and determine whether
the top-prime ranges and the count are scale-free. A positive outcome
gives (5$_c$) for every $c>1$ by the same argument, hence
$V(cx)\sim cV(x)$ for all $c>1$ at the standing of the accepted file plus
an author-checked generalization, collapsing the reconstructed cluster
interval to $\{c\}$ for every $c$; a negative one closes this route: (5$_c$) for
the accepted family would then need an argument of its own, or a differently
balanced family with its own estimates (3)–(5).

**Outcome.** Transfers conditionally, with the premise (5$_c$) explicit.
Filed as the lead
[[research/leads/general_scale_totient_doubling/_index|general_scale_totient_doubling]].

## Problem 821: large fibers versus repeated representations

**Target.** [[problems/arithmetic_functions/E0821/_index|Problem 821]]: with
$g(n)=\#\{m:\varphi(m)=n\}$, is $g(n)>n^{1-\epsilon}$ for infinitely
many $n$, for every $\epsilon>0$? Its page records the standing claimed,
with the question proved, through
[[problems/arithmetic_functions/E0821/claims/2026_09_24_openai|the OpenAI release's pending full claim]]
of 24 September 2026, beside Baker and Harman's accepted partial claim and
Lichtman's pending one. Its references record the chain from Erdős 1935 (some
positive exponent) through Baker–Harman 1998 (values with more than
$m^{1-\beta}$ preimages, $\beta=0.2961$, Corollary 1 on
[[../library/arithmetic_functions/baker_1998_shifted_primes_without_large_prime_factors/_index|the card]])
to Lichtman 2022 (values with at least $m^{0.7156}$ preimages,
Corollary 1.3 on
[[../library/arithmetic_functions/lichtman_2022_primes_arithmetic_progressions_large_moduli_shifted/_index|the card]]),
all from smooth shifted primes; the gap the accepted results leave is the
exponent $1-\epsilon$ for every $\epsilon$.

**What the mechanism gives, and why it is nothing.** The collision
estimate (4) bounds $\sum_t(|f_y^{-1}(t)|-1)$ over the fibers of the pair
map $f_y(b,p)=b(p-1)$. The fiber over a value $t$ consists of pairs
$(b,p)$ with $p$ prime and $p-1\mid t$, so
$|f_y^{-1}(t)|\le\#\{p:p-1\mid t\}\le d(t)=t^{o(1)}$ for every family.
Problem 821 concerns $g(t)$, which the sources above show exceeds
$t^{0.7}$ infinitely often. Two preimages $m,m'$ with the same top prime
$p$ and cores of equal totient, $\varphi(m/p)=\varphi(m'/p)$, are one
pair, so the pair count of a value collapses its fiber under $\varphi$ to
a divisor-bounded number. Hence (4) is a statement about a quantity that
is $t^{o(1)}$ for every value, neither implying nor implied by a bound on
$g$; the coverage (3) concerns which values are represented, not how
often; and the direction of Problem 821, lower bounds for extreme fibers,
is the opposite of what a family built to keep fibers small on average
can supply. Ford's Theorem 2, a positive proportion of totients for every
possible multiplicity, is consistent with (4) for the same reason.

**Next investigation.** None through this mechanism; the route on the
problem page is the smooth-shifted-prime one and does not count the value
set.

**Outcome.** Fails: different objects, pair representations bounded by
the divisor function against preimages.

## Problem 694: the extreme fiber ratio

**Target.** [[problems/arithmetic_functions/E0694/_index|Problem 694]] asks for
$\max f_{\max}(n)/f_{\min}(n)$ over totient values $n\le x$. The page
records the erdosproblems.com status solved (Lean), qualified: the asymptotic
$(e^\gamma+o(1))\log\log x$ rests on a five-page note
([[../library/arithmetic_functions/gpt_5_5_pro_2026_totient_fibre_extremes/theorem_2_1|Theorem 2.1 on its card]])
and two external Lean developments read as text, with no refereed
publication or independent review held.

**What the mechanism gives.** Nothing for the question: $f_{\max}$ is
invisible to the pair family, whose pairs each supply one preimage, and
the extreme ratio comes from the extreme fibers that (3)–(5) average
away. What it would give under the unverified bounded-record premise of
the Problem 417 section is a typical-ratio statement,
$f_{\min}(v)\le K(\varepsilon)v$ for all but an $\varepsilon$-proportion
of totients, which no erdosproblems.com problem asks and which is the object of
Problem 417. The one shared device is the existence half of the multiplication
by convenient integers behind Ford's Theorem 8 and the Problem 49 folder's Lemma
4.1: the note's Proposition 3.1 observes that a collision
$\varphi(a)=\varphi(b)=n$ gives $(r-1)n$ the preimages $ra$ and $rb$ for every
prime $r\nmid ab$, and needs nothing about the other preimages of $(r-1)n$,
whose absence is what convenient means. The witness $d=54$ of Theorem 417.3 does
not propagate this way: $54(r-1)$ lies in $S(3)$ only when $r$ is convenient for
$54$, and $54\cdot(5-1)=216=\varphi(7\cdot37)$ shows that $r=5$ is not; the
propagation Theorem 417.3 would need is the exact-preimage clause of Ford's §7,
which is Theorem 8 itself.

**Outcome.** Fails: no bearing on a solved question; the shared device is
Ford's, not the reconstructions'.

## Problem 51: the least-preimage ratio

**Target.** [[problems/arithmetic_functions/E0051/_index|Problem 51]]: is there
an infinite set $A$ of totients with $f_{\min}(a)/a\to\infty$ along $A$?
Its page records the status open, with
[[problems/arithmetic_functions/E0051/claims/2026_01_11_colossal_noob|a rejected full claim]]
and Guy's B36 form of the question (for every $\epsilon$ an $n$ with
$\varphi(n)=m<\epsilon n$ and no smaller preimage of $m$).

**Reformulation (author-recorded).** Problem 51 has a positive answer if
and only if $r$ is unbounded on the totients. If totients $v_K$ with
$r(v_K)>K$ exist for every $K$, then, each $r(v)$ being a finite number,
only finitely many $K$ share a given $v_K$, so an increasing subsequence
with $r\to\infty$ is a set $A$; the converse is the definition.

**What the mechanism gives.** Nothing: the pair family gives upper bounds
$f_{\min}(v)\le m_0p$ on covered values, and Problem 51 needs lower
bounds. The one lower-bound device available, the sets $S(k)$ of the
Problem 417 section, gives $r(v)\ge k/\varphi(k)$ on $S(k)$ and reaches
$r\to\infty$ only through moduli $k$ with many prime factors, that is,
only if $V(x;k)>0$ for such $k$. Ford's §7 finds witnesses for $k\le11$
only at the prime powers and at $k=11$, none for $6$ or $10$, and writes
that there may be no totient all of whose preimages are divisible by $6$
(its nonexistence would imply Carmichael's conjecture, since a totient
with a unique preimage has that preimage divisible by $6$). So the $S(k)$ device
is capped at the ratio $2$ of $k\in\{2,4,8\}$ unless a modulus $k$ with
$k/\varphi(k)>2$ admits a witness, that is, an even modulus with an odd prime
factor (the least are $6$, ratio $3$, and $10$, ratio $5/2$) or an odd modulus
with at least three distinct prime factors, small enough (the least is $105$,
ratio $35/16$; two odd primes give at most $15/8$). No held source or
computation supplies one. Moduli with two or three distinct odd prime factors do
admit witnesses in the sieve's range ($580$, with preimages $649=11\cdot59$ and
$1298$ only; $116964$, with preimages $3^3\cdot19^3$ and its double, ratio
$19/12$; $103240$, with preimages $11\cdot59\cdot179$ and its double), but their
primes are large, and up to $10^7$ the device certifies at most $r\ge19/12$; the
sieve of the Problem 417 section, extended for this section, finds no totient up
to $10^7$ all of whose preimages are divisible by $6$, $10$, $12$, $15$, $20$,
$21$, $35$ or $45$, and $\max_{v\le10^7}r(v)=2.0414$. In this range the maximum
ratio moves only from $2.0355$ to $2.0414$ between $10^6$ and $10^7$.

**Next investigation.** A positive answer needs totients all of whose preimages
carry many small prime factors: either the preimages share a divisor $k$ with
many distinct prime factors, the $V(x;k)$ classification, where the witnessed
moduli so far have $k/\varphi(k)\le2$, or they do not, a structure outside that
classification; the finite question whether some totient has all preimages
divisible by $6$ or by $10$ (Ford's open cases) or by $105$, the least moduli
with $k/\varphi(k)>2$, is the natural first test, and a segmented computation of
$\max r(v)$ to $10^9$–$10^{10}$ would show whether $\max_{v\le x}r(v)$ grows
with $x$ at all beyond its value $2.0414$ at $10^7$, and in particular whether
it reaches $5/2$ or $3$, the ratios a witness for $10$ or $6$ would force. A
negative answer to Problem 51 ($r$ bounded by $K$) would, through 417.1(a),
confine the totients counted by $V_0(x)$ to $(x/K,x]$.

**Outcome.** Fails: no transfer; the shared object yields only the $S(k)$
cap and a finite-range observation.

## Problem 49 and the monotone-set reconstructions: shared inputs

**Target.** [[problems/primes/E0049/_index|Problem 49]]: open for the exact
clause, whether the primes are a largest subset of $[1,N]$ with strictly
increasing totients; the asymptotic and $o(N)$ clauses are proved, and
Theorem 1.2 of Pollack, Pomerance and Treviño is reconstructed under
[[research/erdos_49/_index|the Problem 49 folder]], whose index records the
outcomes for Problems 416 and 417 and points to its connections page and to the
lead distinct_totient_preimage_ratio.

**What transports.** No transfer to the open clause: exact extremality at
a finite $N$ is untouched by counting functions. The relation runs the
other way. The folder's $W(x)$ is Problem 417's $V'(x)$ (Maier and
Pomerance's $V'$ is a third, different count); its Theorem 1.2
reconstruction consumes the same input (W) as the boundedness in
Proposition 417.2; and its reversed pair $d_1=2^{18}\cdot257<d_2=d_1+28$,
with the least preimage of $d_1$ above the largest preimage of $d_2$, has
$d_1$ equal to Ford's witness for $k=4$, an element of the set $S(4)$ of
Theorem 417.3. Lemma 4.1(iii) of that folder, $n/\varphi(n)$ bounded on
Ford's candidate set with two counts imported from Ford's §5, is the route
to $V\ll V'$ that does not rest on (W) as the cited authors' reading.

**Outcome.** No transfer; the shared inputs are recorded.

The Problem 49 folder's [[research/erdos_49/connections|connections page]]
assesses Problems 416 and 417, reaching the Problem 417 statements independently
from Lemma 4.1 and pointing at the lead distinct_totient_preimage_ratio as the
single carrier of that route.

## Shifted collisions: Problems 1003 and 1004 and the two totient leads

**Targets.** [[problems/arithmetic_functions/E1003/_index|Problem 1003]]
(infinitely many $n$ with $\varphi(n)=\varphi(n+1)$; open),
[[problems/arithmetic_functions/E1004/_index|Problem 1004]] (a block of length
$(\log x)^c$ below $x$ with pairwise distinct totients, for every $c$;
open, with the unreviewed candidate
[[research/leads/totient_blocks_native_note/_index|totient_blocks_native_note]]),
and [[problems/irrationality/E0249/_index|Problem 249]] (irrationality of
$\sum\varphi(n)/2^n$; open, with the editable sketch
[[research/leads/totient_binary_series/_index|totient_binary_series]]).

**Why nothing transfers.** The write-up's collisions are equalities
$b(p-1)=b'(p'-1)$ between two representations of one value; the problems'
collisions are equalities $\varphi(n)=\varphi(n+k)$ between the values at
two arguments. A shifted collision between two arguments of pair form,
$n=m_0p$ and $n+k=m_0'p'$, is a pair collision only when the pairs
differ, and (4) counts pair collisions with no rate and no reference to
$k$, summed over all values up to $y$, so it does not bound
$P(x;k)=\#\{n\le x:\varphi(n)=\varphi(n+k)\}$, which the Problem 1004
page records at $x/(\log x)^2$ uniformly for $k\le\log x$ from the 2013
manuscript; conversely, pair collisions need not come from arguments at
bounded distance, so those bounds do not give (4). Both leads use the
values $\varphi(n)$ as a sequence indexed by $n$ (the $2$-adic valuations
of tail sums for Problem 249, consecutive distinctness for Problem 1004),
and the counting function of the value set carries no information about
the index. The objects are shared; the mechanism is not.

**Outcome.** Fails, with the obstruction that representation collisions
and argument collisions are different equations.

## Other pages checked

- Value sets of other functions.
  [[problems/arithmetic_functions/E0418/_index|Problem 418]] (integers not of the
  form $n-\varphi(n)$; proved) and
  [[problems/arithmetic_functions/E0822/_index|Problem 822]] (positive density of
  the values of $n+\varphi(n)$; proved) concern value sets but ask nothing
  about the regularity of their counting functions, and both are
  resolved. No erdosproblems.com problem asks for the counting function of the
  values of $\sigma$, so Ford's Theorem 14, the analogs of Theorems
  1–4, 8 and 10–13 for $\sigma$ and similar functions, which would carry
  Proposition 417.2 and the preprint's argument over verbatim, has no
  consumer here.
- [[problems/arithmetic_functions/E0048/_index|Problem 48]] (common values of
  $\varphi$ and $\sigma$; proved) builds its common values explicitly;
  [[problems/arithmetic_functions/E0050/_index|Problem 50]] (the distribution
  function of $\varphi(n)/n$),
  [[problems/arithmetic_functions/E0408/_index|Problem 408]],
  [[problems/arithmetic_functions/E0409/_index|Problem 409]] and
  [[problems/arithmetic_functions/E0411/_index|Problem 411]] (iterates),
  [[problems/arithmetic_functions/E0415/_index|Problem 415]] (ordering patterns
  of consecutive values),
  [[problems/arithmetic_functions/E0456/_index|Problem 456]] (the least $m$ with
  $n\mid\varphi(m)$), [[problems/arithmetic_functions/E0828/_index|Problem 828]]
  ($\varphi(n)\mid n+a$) and
  [[problems/arithmetic_functions/E1064/_index|Problem 1064]] ($\varphi(n)$
  against $\varphi(n-\varphi(n))$; proved) involve $\varphi$ at
  arguments, not the set of its values.
- Pages where $\varphi$ is a notation for something else or enters only
  as a weight ([[problems/integer_sequences/E0220/_index|Problem 220]],
  [[problems/integer_sequences/E0971/_index|Problem 971]],
  [[problems/irrationality/E0999/_index|Problem 999]],
  [[problems/additive_combinatorics/E0787/_index|Problem 787]] and the geometric
  and graph pages the search returned), and the theory claim
  [[theory/irrationality/L16_totient_kernel_separation/_index|L16]]
  (kernel separation for the binary series), have no object in common
  with the mechanisms.

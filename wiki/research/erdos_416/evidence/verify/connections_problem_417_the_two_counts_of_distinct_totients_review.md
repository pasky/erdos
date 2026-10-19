---
name: research/erdos_416/evidence/verify/connections_problem_417_the_two_counts_of_distinct_totients_review
title: "Independent review of the connections section: Problem 417: the two counts of distinct totients"
desc: |
  Refutation-failed for Lemma 417.1, Proposition 417.2, Theorem 417.3 and
  Proposition 417.4 and for the lead page's route; refuted-as-stated for the
  frame's clause G(t) = 1 for t >= 2, which Ford's Theorem 8 at k = 4
  contradicts, and for the finite-range sentence placing every element of
  V_0(x) in (x/2, x]. Two required corrections, one suggested, five notes.
created: 2026-09-28T18:31:28Z
updated: 2026-10-07T21:41:29Z
---

***

## Subject and independence

The reviewer worked in a fresh context from the commissioned assignment
alone and took no part in writing the reviewed pages, the reconstruction
pages, the lead page or the problem page. The charge was refutation of the
author-recorded mathematics; agreement was not the goal.

Subject, as it stood on 2026-09-28T13:50:48Z:

- `wiki/research/erdos_416/connections.md`, the section "Problem 417: the
  two counts of distinct totients", lines 91-341 (from its H2 heading to
  the line before the next H2), read in full against the shared sections of
  the same page (Purpose and standing, Notation, Imported inputs, The
  search; lines 1-90), whose interfaces were confirmed at each use.
- `wiki/research/leads/distinct_totient_preimage_ratio/_index.md`, the
  lead page whose route rests on that section, read in full.

Premises read as inputs at their recorded standing:
[[research/erdos_416/zeraoulia_theorem_1_1_reconstruction|the preprint's Theorem 1.1 reconstruction]]
(read in full; Steps 1, 3 and 7 re-derived because the section imports
them) and
[[research/erdos_416/kruer_kohlmeyer_theorem_1_1_reconstruction|the doubling-law reconstruction]]
(read in full; used by the section only in Remark (ii) and in the pair
family obstruction). The Statement paragraph of
[[problems/arithmetic_functions/E0417/_index|Problem 417]] was read. The cards of
[[../library/arithmetic_functions/ford_1998_distribution_totients/_index|Ford (1998)]],
[[../library/arithmetic_functions/maier_1988_number_distinct_values_euler_s_function/_index|Maier and Pomerance (1988)]]
and
[[../library/primes/pollack_et_al_2013_sets_monotonicity_euler_totient_function/_index|Pollack, Pomerance and Treviño (2013)]]
were read. In the held PDFs: Ford's Theorems 1, 2, 4, 8, 10 and 11 (§§1.1-1.4,
pp. 2-3) and his §7 (pp. 38-39) in text extraction; the 2013 manuscript's
Theorem 1.2 with the definition of $W(x)$ (p. 2) and its §4 opening with
footnote 1 (p. 7) in text extraction; the Maier-Pomerance §5 (journal
p. 275) on the page image of the scanned PDF, since its text extraction is
empty. The wiki pages named in the assignment were read at the named
sections. Nothing under any `evidence/` folder was read.

Exposures: the Statement of Problem 417 is a bold paragraph, not a heading,
so the first sixty lines of the problem page were printed to find it; they
include the page's "Current assessment" and "Progress" sections. The
Progress section restates the two results of the reviewed section and names
the lead; it carries no verdict and did not affect this review. The 2013
card was read whole, including its "Living verification" line. No other
excluded content reached the reviewer; no web search was made.

Independent computation: an exact sieve of Euler's function to
$6.2\cdot10^7$ and an exact inverse-totient enumeration were written and run
by the reviewer, independently of the page's unretained computation; their
mathematical content is recorded below.

## Restatement

Conventions: $T(x)$ is the set of totient values in $[1,x]$, $V(x)=|T(x)|$,
$V'(x)=\#\{\varphi(m):1\le m\le x\}$, $R=V/V'$, $V_0=V-V'$, $f_{\min}(v)$
the least preimage of the totient $v$, $r(v)=f_{\min}(v)/v$, $S(k)$ the
set of totients all of whose preimages are divisible by $k$, $V(x;k)$ the
number of them in $[1,x]$, $\pi$ the prime-counting function, $c_0$
Chebyshev's constant. The imports are (F): $V(x)=M(x)e^{E(x)}$ with
$|E(x)|\le K$ for $x\ge x_1$, $M(x)=(x/\log x)e^{\Psi(x)}$, with the
derivative bound $|\psi_c'(t)|\le K'/t$ for $\psi_c(t)=\Psi(c^t)$ on the
range where $\log(c^t)\ge e^e$; (F8): if $d$ is a totient all of whose
preimages are divisible by $k$, then
$V(x;k)\gg_\varepsilon d^{-1-\varepsilon}V(x)$ for all large $x$; (W):
$V(x)\asymp V'(x)$ for large $x$.

- S1 (Lemma 417.1). For real $x\ge1$: (a) $V'(x)$ counts the $v\in T(x)$
  with $f_{\min}(v)\le x$ and $V_0(x)$ those with $f_{\min}(v)>x$, so
  $R(x)\ge1$ and $R(x)=R(\lfloor x\rfloor)$; (b) for every integer $n\ge1$,
  $V'(n+1)-V'(n)\in\{0,1\}$, and for real $x\ge2$,
  $V'(x)\ge\pi(x)\ge c_0x/\log x$; (c) for every integer $n\ge2$,
  $|R(n+1)-R(n)|\le2n/V'(n)^2\le(2/c_0^2)(\log n)^2/n$.
- S2 (Proposition 417.2). With $\alpha=\liminf_nR(n)$ and
  $\beta=\limsup_nR(n)$ in $[1,\infty]$, the set of subsequential limits of
  $(R(n))_{n\ge1}$ is exactly $[\alpha,\beta]$; the set of subsequential
  limits of $R(x)$ as real $x\to\infty$ is the same set; under (W),
  $\beta<\infty$. Consequence: either $R(x)$ converges or $R$ has continuum
  many limit points, the two cases exclusive.
- S3 (Theorem 417.3). There is $\eta>0$ such that $V_0(x)\ge\eta V(x)$ for
  an unbounded set of $x$; hence $\limsup_xR(x)\ge1/(1-\eta)>1$, and if
  $\lim R$ exists it exceeds $1$. Inputs: (F) with the derivative bound,
  (F8) at $k=3$ with $d=54$, Chebyshev. Intermediate claims: the preimages
  of $54$ are exactly $81$ and $162$; $v\in S(3)$ implies
  $f_{\min}(v)\ge\tfrac32v$ and so $V_0(x)\ge N(x)=\#(S(3)\cap(2x/3,x])$;
  $V(x;3)=\sum_{j\ge0}N(x(2/3)^j)$; $\sum_{j\ge0}V(x(2/3)^j)\le(3C_1+o(1))V(x)$
  with $C_1=2^{1+K'}e^{2K}$; and the contradiction with $\eta=c/(6C_1)$.
  Remarks: $\eta$ is not numerical; any of Ford's witnesses serves, and
  with $k=4$ the doubling law would replace the geometric sum; the
  mechanism is the preimage lower bound carried by $S(k)$.
- S4 (Proposition 417.4). If there are $\eta'>0$ and $y_1$ with
  $N(y)\ge\eta'V(y)$ for all $y\ge y_1$, then $R(y)\ge1/(1-\eta')$ for all
  $y\ge y_1$ and $\liminf R\ge1/(1-\eta')>1$. The premise is described as
  the short-interval form of (F8), motivated by Ford's Theorem 4 and not
  stated in the held paper.
- S5 (stated obstructions). (a) A retained pair $(b,p)$ with core
  $b=\varphi(m_0)$ and prime $p\nmid m_0$ gives $v=b(p-1)$ the preimage
  $m_0p$, so $f_{\min}(v)\le(m_0/b)\,(p/(p-1))\,v$; a hypothetical bound
  $m_0/\varphi(m_0)\le K(\varepsilon)$ on the records would give
  $f_{\min}(v)\le2K(\varepsilon)v$ for all but $(\varepsilon+o(1))V(y)$
  totients $v\le y$, which yields only $R\ll1$. (b) The preprint's near-hit
  mechanism (telescoping of consecutive quotients along $c^j$ against the
  logarithmic profile) does not transfer to $R$, because $R$ compares two
  functions at one scale and no asymptotic for $V'$ beyond (W) is held.
- S6 (the frame). (a) Under (H1): $V(ux)/V(x)\to u$ for each fixed
  $u\in(0,1]$, and (H2): for each fixed $u\in(0,1]$ and $t\ge1$,
  $\#\{v\le ux:r(v)\le t\}/V(ux)\to G(t)$ for a nondecreasing
  $G\colon[1,\infty)\to[0,1]$, one has $V'(x)/V(x)\to\int_0^1G(1/u)\,du$,
  $V_0(x)/V(x)\to\int_1^\infty(1-G(t))\,dt/t^2$, and $R(x)$ converges to the
  reciprocal of the first integral. (b) The page's additional clause in
  (H2), $G(t)=1$ for $t\ge2$, with the upper limit $2$ in the $V_0$
  integral.
- S7 (finite range). (a) A sieve to $6.2\cdot10^7$ covers every preimage of
  every totient $v\le10^7$; at $x=10^4,10^5,10^6,10^7$ the values of
  $(V,V',V_0;R)$ are $(2374,2160,214;1.0991)$, $(20254,18412,1842;1.1000)$,
  $(180184,163861,16323;1.0996)$, $(1634372,1485793,148579;1.1000)$, with
  $V_0/V=0.0901,0.0909,0.0906,0.0909$; $r(v)\le2.0414$ for all totients
  $v\le10^7$, attained at $v=2037248$ with $f_{\min}=4158795$, and
  $r(v)\le2.0355$ for $v\le10^6$, attained at $v=5888$ with
  $f_{\min}=11985$; among the totients in $(5\cdot10^6,10^7]$ the
  proportions with $r\ge1.1,1.25,1.5,2$ are $0.319,0.266,0.194,0.00001$;
  $V(10^7;3)/V(10^7)\approx0.0013$; no totient up to $10^7$ lies in $S(4)$.
  (b) The consequence sentence: in this range every element counted by
  $V_0(x)$ lies in $(x/2,x]$.
- S8 (the lead page). The route summary: S2 with inputs (unit jumps of
  $V'$, $V'\ge\pi$, Step 7 of the preprint's reconstruction, (W) or Lemma
  4.1(iii) of the 2013 manuscript for $\beta<\infty$); S3 with inputs ((F8)
  at $d=54$ with verified preimages, (F) with the derivative bound,
  Chebyshev; the doubling law not needed); S6(a) as a frame; the numbers of
  S7(a); the provisional premises (P1) (the short-interval form of (F8),
  giving $\liminf R>1$ through S4) and (P2) (a limiting distribution of $r$
  with the general-scale law, giving the limit and its value); the gap
  (existence of the limit) and the next steps. Also a cross-reference
  asserting that the Problem 49 connections page derives the same
  statements independently.

## Checklist

- Quantifiers and scope. Pass for S1-S4: "arbitrarily large $x$" in S3 is
  exactly what Step 5 proves (the negation of "for all $y\ge y_0$" for
  every $y_0$), the limit superior is never upgraded to a limit inferior,
  and S4 keeps its "for all large $y$" premise. S2's dichotomy needs
  $\beta<\infty$, which the statement supplies under (W) (F6). Fail for
  S7(b): a finite-range "every" that the page's own maximum ratio
  $2.0414>2$ already contradicts (F2).
- Circularity. Pass. No target statement or equivalent is assumed; Step 5
  of S3 is a contradiction from an explicit negation of the conclusion, and
  the imported (F8) is a theorem about $V(x;3)$, not about $V_0$.
- Model and convention changes. Pass for the objects: the section's $V$ and
  $V'$ are the problem page's, Ford's $V(x;k)$ is quoted with his
  definition, the 2013 manuscript's $W$ is $V'$, and the Maier-Pomerance
  $V_0$ equals the section's $V_0$ (a totient with no preimage $\le x$ has
  all its preimages $>x$). Fail for S6(b): the clause $G(t)=1$ for $t\ge2$
  substitutes a bounded-support model for a distribution that the imported
  (F8) at $k=4$ forces to have mass above $2$ (F1).
- Finite and statistical overreach. Pass for S3 and for the page's own
  warning that the near-constancy $R\approx1.10$ proves nothing. Fail for
  S6(b) and S7(b): the support bound on $G$ and the interval $(x/2,x]$ are
  finite-range observations promoted to a hypothesis and a sentence that
  the held inputs refute.
- Uniformity. Pass. $C_1$ and $\eta$ depend only on Ford's constants and the
  implied constant of (F8) at $d=54$, as Remark (i) says; the $o(1)$ of
  Step 4 is uniform in $j$ (it bounds a sum), and the derivative bound is
  applied only where $z\ge x^{1/2}$ with $x$ large, inside its range. The
  imported-input bullet misstates that range by one exponential (F3),
  without effect on the use.
- Extremal conclusions. Pass. The limit superior bound $1/(1-\eta)$ follows
  from the unbounded set of $y$ with $R(y)\ge1/(1-\eta)$; the finite-range
  maxima of $r$ were recomputed in the claim's own units (exact ratios of
  integers) and agree.
- Consequences and composition. Pass for "if the limit exists it exceeds
  $1$" (S2 gives that the limit equals $\beta$) and for "either the limit
  exists or continuum many limit points" under (W). Fail for the "so" of
  S7(b) (F2). The lead's composition of S2, S3 and S4 names each consumed
  input at its strength; its cross-reference to another page was not
  checked (F8).
- Computation. Pass. Every number of S7(a) was reproduced by an independent
  exact sieve (integer arithmetic, no floating point except in the printed
  ratios): the four rows, the $V_0/V$ values, both record ratios with their
  witnesses, the four proportions, $V(10^7;3)=2069$ against
  $V(10^7)=1634372$, and $S(4)\cap[1,10^7]=\emptyset$. The covering bound
  was rechecked: $\prod_{p\le23}p/(p-1)=6.1129\ldots<6.12$ and
  $\varphi(2\cdot3\cdots29)=1021870080>10^9$.
- Reproduction. Pass with a note. The page states no rerun line and retains
  no code for its computation; the numbers were reproduced from the stated
  description alone (F7).
- Source and verdict fidelity. Pass for (F8): Ford's Theorem 8 is in §1.3,
  worded "a trivial corollary to the proof of Theorem 2", and his §7 lists
  exactly the witnesses the section quotes with "except $k=6$ and $k=10$".
  Pass for (W): p. 7 of the 2013 manuscript states $V(x)\asymp W(x)\asymp Z(x)$
  for large $x$ citing [8, §§4, 5] with the footnote that [8] is the
  corrected arXiv version. Pass for the Maier-Pomerance §5 (journal p. 275)
  reading of $V'$ and $V_0$. Two characterizations overstate slightly:
  Ford's Theorem 4 is quoted without "$\theta$ admissible" (F4), and the
  Maier-Pomerance $V'$ is called "of the same order as $V$" where the
  source gives the same growth type with a $(C+o(1))$ exponent (F5).

## Weakest steps

**W1: Step 4 of Theorem 417.3, the sum of $V$ along the scales $x(2/3)^j$.**
Re-derived. Let $\lambda=3/2$, $x$ large, and $z=x/\lambda^j\ge x^{1/2}$.
Then $z\ge x_1$ and $\log z\ge\tfrac12\log x$, so by (F)

$$
\frac{V(z)}{V(x)}=\frac{M(z)}{M(x)}e^{E(z)-E(x)}
\le e^{2K}\cdot\frac zx\cdot\frac{\log x}{\log z}\cdot e^{\Psi(z)-\Psi(x)}
\le2e^{2K}\lambda^{-j}e^{\Psi(z)-\Psi(x)}.
$$

Write $x=\lambda^t$ and $z=\lambda^{t'}$ with $t'=t-j\ge t/2$. Since
$\Psi(\lambda^s)=\psi_\lambda(s)$ and $|\psi_\lambda'(s)|\le K'/s$ for
$\log(\lambda^s)\ge e^e$, which holds on all of $[t',t]$ once
$x^{1/2}\ge e^{e^e}$, the mean value bound gives
$|\Psi(z)-\Psi(x)|\le K'\int_{t'}^t ds/s=K'\log(t/t')\le K'\log2$. Hence
$V(z)\le2^{1+K'}e^{2K}\lambda^{-j}V(x)=C_1\lambda^{-j}V(x)$, and summing
over all $j\ge0$ gives at most $C_1V(x)/(1-\lambda^{-1})=3C_1V(x)$. The
$j$ with $1\le x/\lambda^j<x^{1/2}$ number at most $\log_\lambda x+1$ and
each has $V(x/\lambda^j)\le x^{1/2}$, contributing $O(x^{1/2}\log x)$,
which is $o(V(x))$ against $V(x)\ge\pi(x+1)\ge c_0x/\log x$. The derivative
bound itself was re-derived from the reconstruction's Step 1: with
$u=\log(c^t)$, $d\log_3(c^t)/dt=1/(t\log u)$ and
$d\log_4(c^t)/dt=1/(t\log u\log\log u)$, so for $u\ge e^e$ the difference
of the two derivatives lies in $[0,1/(t\log u)]$,
$0\le\log_4\le\log_3=\log\log u$, and
$|\psi_c'(t)|\le(2C\log\log u+D+|D+\tfrac12-2C|)/(t\log u)\le K'/t$ using
$\log\log u\le\log u$ and $\log u\ge1$; the constant is independent of $c$.

**W2: Step 5 of Theorem 417.3, the tail below $y_0$ and the contradiction.**
Re-derived. Assume $N(y)\le\eta V(y)$ for all $y\ge y_0$, with
$\eta=c/(6C_1)$ and $c$, $x_0$ from (F8) at $k=3$. Fix $x\ge y_0$ and let
$j_0$ be the least $j$ with $x/\lambda^{j}<y_0$. For $j<j_0$,
$N(x/\lambda^j)\le\eta V(x/\lambda^j)$. For $j\ge j_0$ the blocks
$(x/\lambda^{j+1},x/\lambda^j]$ are disjoint subsets of
$(0,x/\lambda^{j_0}]\subset(0,y_0)$, so their $N$-values sum to
$\#(S(3)\cap(0,x/\lambda^{j_0}])\le V(y_0)$. Therefore

$$
V(x;3)\le\eta\sum_{j\ge0}V(x/\lambda^j)+V(y_0)
\le\eta(3C_1+o(1))V(x)+V(y_0)=(c/2+o(1))V(x)+V(y_0),
$$

which is below $cV(x)$ once $V(x)>2V(y_0)/c$ and the $o(1)$ is below
$c/4$, contradicting $V(x;3)\ge cV(x)$ for $x\ge x_0$. So for every $y_0$
some $y\ge y_0$ has $N(y)>\eta V(y)$; by Step 2, $V_0(y)\ge N(y)$, hence
$V'(y)<(1-\eta)V(y)$ and $R(y)>1/(1-\eta)$. Step 2 was rechecked: $3\mid m$
gives $m/\varphi(m)=\prod_{p\mid m}p/(p-1)\ge3/2$, with equality exactly at
the powers of $3$, so for $v\in S(3)$ and $2x/3<v\le x$,
$f_{\min}(v)\ge\tfrac32v>x$. Equality occurs at $v=54$ itself
($f_{\min}=81$), which does not disturb the strict inequality.

**W3: Lemma 417.1(c) and the crossing argument of Proposition 417.2.**
Re-derived. With $A=V(n)$, $B=V'(n)$, $\delta,\epsilon\in\{0,1\}$,
$R(n+1)-R(n)=(B\delta-A\epsilon)/(B(B+\epsilon))$, so
$|R(n+1)-R(n)|\le\max(B,A)/B^2\le n/B^2$, better than the page's $2n/B^2$;
with $B\ge c_0n/\log n$ this is at most $(1/c_0^2)(\log n)^2/n\to0$. For
$\alpha<y<\beta$ and $n_0\ge8$: $\liminf<y$ gives infinitely many $n$ with
$R(n)<y$ and $\limsup>y$ infinitely many with $R(n)>y$, so there are
$n_1,n_2>n_0$ on opposite sides of $y$; if $n_1<n_2$ let $n$ be the largest
integer in $[n_1,n_2)$ with $R(n)<y$, so $R(n+1)\ge y$; the other order is
symmetric. Then
$|R(n)-y|\le|R(n+1)-R(n)|\le(2/c_0^2)(\log n)^2/n\le(2/c_0^2)(\log n_0)^2/n_0$,
the last step because $(\log t)^2/t$ decreases for $t\ge e^2$; the page
omits this threshold, harmlessly since $n_0\to\infty$. Hence every $y$ in
$(\alpha,\beta)$ is a limit point; $\alpha$ and $\beta$ are limit points in
$[1,\infty]$ by definition; the cluster set is closed; so it is
$[\alpha,\beta]$. The real-variable statement follows from
$R(x)=R(\lfloor x\rfloor)$. The
dichotomy: if $\beta<\infty$ (from (W), since $V\ll V'$ bounds $R$) then
$\alpha=\beta$ means convergence and $\alpha<\beta$ means an uncountable
cluster set; without (W) the case $\alpha=\beta=\infty$ ($R\to\infty$)
would be a third alternative.

## Strongest attack

- S1. Attacked at small $n$, where $V'(n)$ is small: the bound uses only
  $V'(n)\ge\pi(n)\ge1$ and unit jumps of both counts, and $V(n)\le n$;
  nothing fails. Refutation failed.
- S2. Attacked the endpoint cases: $\beta=\infty$ without (W) leaves the
  interval $[\alpha,\infty]$ and the dichotomy survives except when
  $\alpha=\beta=\infty$; the statement supplies $\beta<\infty$ under (W),
  so the dichotomy holds as stated under its listed input (F6). Attacked
  the crossing with $n_2<n_1$: symmetric. Refutation failed.
- S3. Attacked the witness: the preimage set of $54$ was enumerated exactly
  by the inverse-totient recursion and is $\{81,162\}$. Attacked the range
  of the derivative bound: the imported bullet says $c^t\ge e^e$ but the
  reconstruction proves it for $\log(c^t)\ge e^e$; Step 4 uses it only for
  $z\ge x^{1/2}$ with $x$ large, so the misstatement has no effect (F3).
  Attacked the possibility that $V(x;3)$ is carried by blocks far below
  $x$ at every scale, defeating $N(x)\gg V(x)$ along every sequence: Step 5
  shows exactly that the geometric decay of $V$ along $x(2/3)^j$ makes
  this impossible at all large $x$ simultaneously; the argument leaves
  open, correctly, that $N(y)/V(y)$ may be small along some sequence, which
  is why the theorem states an unbounded set of $y$ and not all large $y$.
  Attacked the hypothesis of (F8): Ford states it for a totient $d$ all of
  whose preimages are divisible by $k$, with no explicit range; the
  section reads it for large $x$, the weakest reading, consistent with its
  origin in the proof of Theorem 2 ("$x\ge x_0(d)$"). Refutation failed.
- S4. The deduction is one line from Step 2; the only attack is on the
  premise, which the page marks as unproved. Refutation failed.
- S5(a). Verified the inequality: $\varphi(m_0p)=\varphi(m_0)(p-1)=v$ since
  $p\nmid m_0$, and $m_0p=(m_0/b)(p/(p-1))v$. Verified that an upper bound
  $f_{\min}(v)\le Lv$ off an $(\varepsilon+o(1))V(y)$ exceptional set gives
  only $V(y)\le(1+O(\varepsilon))V'(Ly)$, that is $R(Ly)\ll_L1$, and no
  lower bound for $V_0$. Refutation failed. S5(b) is a judgment about a
  method, not a claim.
- S6(a). Re-derived the bracketing on a grid $0=u_0<u_1<\dots<u_n=1$: on
  $(u_{i-1}x,u_ix]$, $x/v\in[1/u_i,1/u_{i-1})$, so
  $1[r(v)\le1/u_i]\le1[r(v)\le x/v]\le1[r(v)\le1/u_{i-1}]$, with the first
  block bounded above by $V(u_1x)\sim u_1V(x)$; (H2) at $(u_i,1/u_i)$ and
  $(u_{i-1},1/u_i)$ with (H1) turns each block count into
  $G(1/u_i)(u_i-u_{i-1})V(x)+o(V(x))$, and $G(1/u)$ is monotone in $u$, so
  both Riemann sums converge to $\int_0^1G(1/u)\,du$. No support bound on
  $G$ is used, and $V_0/V\to1-\int_0^1G(1/u)\,du=\int_1^\infty(1-G(t))\,dt/t^2$
  by $t=1/u$. Refutation failed for the deduction.
- S6(b). Refuted. By (F8) at $k=4$ with Ford's $d=2^{18}\cdot257$, whose
  eight preimages $135268352$, $143722624$, $169085440$, $179653280$,
  $202902528$, $215583936$, $253628160$, $269479920$ were enumerated
  exactly and are all divisible by $8$, $V(x;4)\ge c_4V(x)$ for large $x$.
  If $v\in S(4)$ and $m=f_{\min}(v)$, then
  $m/\varphi(m)=2\prod_{p\mid m,\,p>2}p/(p-1)>2$ unless $m$ is a power of $2$,
  in which case $v$ is a power of $2$. So
  $\#\{v\le x:r(v)>2\}\ge V(x;4)-\log_2x-1\ge c_4V(x)-O(\log x)$, and
  (H2) at $u=1$, $t=2$ would force $G(2)\le1-c_4<1$. No $G$ with $G(t)=1$
  for $t\ge2$ can satisfy (H2); the frame's antecedent is refuted by the
  page's own imported input, and the $V_0$ integral's upper limit $2$ is
  wrong for any admissible $G$.
- S7(a). Reproduced exactly (Computation above). Refutation failed.
- S7(b). Refuted. $v=5888=\varphi(3\cdot5\cdot17\cdot47)$ has preimages
  $11985$, $12032$, $12784$, $15040$, $15980$, $18048$, $19176$, $22560$,
  $23970$, so $f_{\min}(v)=11985$ as the page records. For $x=11900$:
  $v\le x$, $f_{\min}(v)>x$, so $v$ is counted by $V_0(x)$, and
  $v\le5950=x/2$. Every integer $x$ in $[11776,11984]$ is a witness, and
  each of the ten totients $v\le10^7$ with $r(v)>2$ ($5888$, $10496$,
  $17408$, $276736$, $2037248$, $5268992$, $5331968$, $6983168$, $8043008$,
  $8749568$) gives a range of such $x$; at the page's own record,
  $v=2037248$ and $x=4100000$ do the same.
- S8. The lead's summaries were checked sentence by sentence against the
  section and carry the same qualifications; the inputs named for S2 and
  S3 are the ones the proofs use; (P1) and (P2) are stated as premises with
  their exact consequences. The attack that succeeds against the section
  (S6(b)) does not reach the lead, which states the frame without the
  support clause. Two sentences could not be tested here (F8). Refutation
  failed.

## Premises

- Ford's Theorem 1 as (F): a two-sided $O(1)$ statement for large $x$,
  stated on the reconstruction page and on the Ford card; the held PDF is
  the author's corrected text (p. 2 read in text extraction). The
  derivative bound $|\psi_c'(t)|\le K'/t$ for $\log(c^t)\ge e^e$ is the
  reconstruction's author-recorded Step 1, re-derived in W1. Held.
- Ford's Theorem 8 as (F8): §1.3, p. 3, "If $d$ is a totient, all of whose
  pre-images are divisible by $k$, then
  $V(x;k)\gg_\varepsilon d^{-1-\varepsilon}V(x)$", introduced as a trivial
  corollary to the proof of Theorem 2 (which is
  stated for $x\ge x_0(d)$), with the proof remark and the witness list in
  §7, p. 39. Read in text extraction. Held. The witnesses $54$ (preimages
  $81$, $162$) and $2^{18}\cdot257$ (eight preimages, all divisible by
  $8$) were verified exactly here.
- Ford's Theorem 4: p. 3, "If $\theta$ is admissible, $y\ge x^\theta$ and
  the multiplicity $k$ is possible, then
  $V_k(x+y)-V_k(x)\asymp V(x+y)-V(x)\asymp(y/(x+y))V(x+y)$", cited by the
  section as motivation only. Read in text extraction. Held.
- (W): p. 7 of the held 17-page manuscript of Pollack, Pomerance and
  Treviño, "$V(x)\asymp W(x)\asymp Z(x)$" for large $x$ with
  $W(x)=\#\{\varphi(n):n\le x\}$ (Theorem 1.2, p. 2) and footnote 1 naming the
  corrected arXiv version of
  Ford's paper. Read in text extraction. Imported by the section as the
  cited authors' reading of Ford; used only for $\beta<\infty$. Held. The
  alternative route through Lemma 4.1(iii) on the Problem 49 folder's page
  lies outside the commissioned read set and was not checked.
- Maier and Pomerance, §5, journal p. 275: $V'(x)$ for
  $\#\{\varphi(n)\le x:n>x\}$ with
  $V'(x)=(x/\log x)\exp\{(C+o(1))(\log\log\log x)^2\}$, and $V_0(x)$ for the
  cardinality of $\{\varphi(n)\le x:n>x\}$ minus
  $\{\varphi(n):n\le x\}$, "a harder question", with "our methods do not
  give a good lower bound for $V_0(x)$". Read on the page image. Held.
- Chebyshev's bound $\pi(y)\ge c_0y/\log y$ for $y\ge2$: standard.
- The preprint's Theorem 1.1 reconstruction: Steps 1, 3 and 7 consumed;
  their statements taken at their reviewed standing and re-derived where
  the section relies on them. The doubling-law reconstruction: consumed
  only in Remark (ii) and S5(a); its Proposition 4.1 has no held prose
  proof, and nothing in S1-S4 depends on it.
- Problem 417's Statement: $V'(x)=\#\{\phi(m):1\le m\le x\}$,
  $V(x)=\#\{\phi(m)\le x:1\le m\}$; does $\lim V(x)/V'(x)$ exist, and is it
  $>1$. The section's target matches it.

## Findings

- F1 (required). Location: "Reformulation and finite-range numbers
  (exploratory)", the hypothesis "(H2) for each fixed $u\in(0,1]$ and
  $t\ge1$, $\#\{v\le ux:r(v)\le t\}/V(ux)\to G(t)$ for a distribution
  function $G$ on $[1,\infty)$ with $G(t)=1$ for $t\ge2$", the display
  "$V_0(x)/V(x)\to\int_1^2(1-G(t))\,dt/t^2$", and "Next investigation" item
  2. Defect: the clause $G(t)=1$ for $t\ge2$ contradicts the section's
  imported (F8) at $k=4$; every $v\in S(4)$ other than a power of $2$ has
  $r(v)>2$, so a positive proportion of totients have $r(v)>2$ and any
  limiting $G$ has $1-G(2)\ge c_4>0$. Witness: Ford's $d=2^{18}\cdot257$
  with its eight preimages, all divisible by $8$, listed under S6(b).
  Replacement: drop the clause, keep $G$ a nondecreasing function
  $[1,\infty)\to[0,1]$, write the second limit as
  $\int_1^\infty(1-G(t))\,dt/t^2$, and in item 2 record that (F8) at
  $k=4$ already bounds $G(2)$ away from $1$, so the limiting law to prove
  or refute is (H2) without a support bound.
- F2 (required). Location: "so in this range every element counted by
  $V_0(x)$ lies in $(x/2,x]$". Defect: false; $r(v)\le2.0414$ gives only
  $v>x/2.0414$ for $v$ counted by $V_0(x)$, and the ten totients
  $v\le10^7$ with $r(v)>2$ each supply values of $x$ with $v\le x/2$.
  Witness: $v=5888$, $f_{\min}(v)=11985$, $x=11900$. Replacement: "so in
  this range every element counted by $V_0(x)$ lies in $(x/2.0414,x]$, and
  only the ten totients with $r(v)>2$ can fall in $(x/2.0414,x/2]$".
- F3 (suggested). Location: imported input (F), "for
  $\psi_c(t)=\Psi(c^t)$, $c^t\ge e^e$". Defect: the reconstruction's Step 1
  proves the bound for $u=\log(c^t)\ge e^e$, that is $c^t\ge e^{e^e}$; for
  $e^e\le c^t<e^{e^e}$ the term $\log_4(c^t)$ is negative and its
  derivative $1/(t\log u\log\log u)$ is unbounded as $\log\log u\to0$. No
  effect on Step 4, which uses the bound only for $z\ge x^{1/2}$ with $x$
  large. Replacement: "$\log(c^t)\ge e^e$".
- F4 (note). Location: Proposition 417.4, "gives
  $V_k(x+y)-V_k(x)\asymp(y/(x+y))V(x+y)$ for $y\ge x^\theta$ and possible
  multiplicities $k$", and the lead's (P1) paragraph. Defect: Ford's
  Theorem 4 requires $\theta$ admissible (his definition, with $0.525$
  admissible by Baker, Harman and Pintz); the paraphrase drops the
  hypothesis. Replacement: add "for admissible $\theta$".
- F5 (note). Location: the Target paragraph, "a different count of the
  same order as $V$". Defect: the held §5 gives
  $V'(x)=(x/\log x)\exp\{(C+o(1))(\log\log\log x)^2\}$, the same growth
  type as the paper's theorem for $V$, not a $\asymp$ statement; the
  source also says "a good lower bound". Replacement: "a different count
  with the same growth type as $V$ in their theorem".
- F6 (note). Location: Proposition 417.2, "Consequently exactly one of the
  following holds". Defect: the dichotomy needs $\beta<\infty$ to exclude
  $R\to\infty$; the statement lists that under (W) in the same sentence,
  so the dependence is visible but the "Consequently" reads as
  unconditional. Replacement: "Consequently, under (W), exactly one...".
- F7 (note). Location: "A computation made for this page". Defect: no code
  or rerun line is retained; the numbers were reproduced here from the
  description alone. No change required for exploratory numbers; a
  retained script would let the next investigation's item 3 start from a
  checked baseline.
- F8 (note). Location: the lead page, "The same three unconditional
  statements and the conditional one are derived independently on the
  Problem 49 connections page (Propositions 2, 3 and 4) ...", and "answers
  both questions of Problem 417 with an explicit limit". Defect: the first
  sentence refers to a page outside the commissioned read set and was not
  checked; its count (four statements, three propositions) is ambiguous.
  The second overstates: under (P2) the limit is $1/\int_0^1G(1/u)\,du$,
  explicit only when $G$ is. Replacement: name which proposition carries
  which statement; write "with the limit expressed through $G$".

## Verdict

- S1 (Lemma 417.1): refutation-failed.
- S2 (Proposition 417.2): refutation-failed; the dichotomy holds under (W),
  which the statement lists.
- S3 (Theorem 417.3): refutation-failed, with the imported (F8) at its
  statement-level standing and the derivative bound at the reconstruction's
  author-recorded standing.
- S4 (Proposition 417.4): refutation-failed, as a conditional on its stated
  premise.
- S5(a) (the pair-family upper bound and its consequence): refutation-failed.
  S5(b) (the near-hit mechanism does not transfer): not a claim.
- S6(a) (the frame's deduction from (H1) and (H2) without a support bound):
  refutation-failed. S6(b) (the clause $G(t)=1$ for $t\ge2$ and the upper
  limit $2$): refuted-as-stated.
- S7(a) (the finite-range numbers): refutation-failed. S7(b) (every element
  counted by $V_0(x)$ lies in $(x/2,x]$): refuted-as-stated.
- S8 (the lead page's route, inputs, premises and gap): refutation-failed;
  its cross-reference to the Problem 49 connections page is unverified
  here.

Limitations: Ford's Theorems 1, 4 and 8 and the 2013 manuscript's (W) were
read at statement level in text extraction and not re-proved; the Problem
49 folder's pages were outside the read set; the constants $c$, $K$, $K'$
and hence $\eta$ are not numerical, as the section says; the finite-range
reproduction covers $v\le10^7$ only. The two refuted sentences lie in the
exploratory paragraph and bear no weight on S1-S4 or on the lead's route.
This focused review assigns no tier and changes no status.

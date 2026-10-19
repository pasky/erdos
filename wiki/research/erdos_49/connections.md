---
name: research/erdos_49/connections
title: Connections from the monotone-totient reconstruction to other problems
desc: |
  Assesses, as mathematics, what the reconstructed collision bounds and the
  convenient-integer construction give for Problems 1004, 1003, 417, 416,
  694, 51, 821, 415, 850 and 931 and for the open clause of Problem 49:
  author-recorded transfers with their proofs and gaps, and the precise
  obstruction wherever a transfer fails.
created: 2026-09-28T06:16:37Z
updated: 2026-10-19T04:19:07Z
---

[[research/erdos_49/_index|..]]

***

This page follows the two mechanisms of the reconstructed proof of Theorem
1.2 of Pollack, Pomerance and Treviño into the rest of the corpus and asks,
for each candidate target, what they give when transported, what they do
not give, and what the next investigation is. The first mechanism is the
pair of uniform collision bounds: the sketch-level
[[research/erdos_49/theorem_3_1_reconstruction|Theorem 3.1]] for the
unstructured solutions of $\varphi(n)=\varphi(n+k)$ and the reconstructed
[[research/erdos_49/theorem_3_3_reconstruction|Theorem 3.3]] for the
structured ones, with the $S$-unit count of
[[research/erdos_49/lemma_3_2_reconstruction|Lemma 3.2]] behind it. The
second is the convenient-integer construction of
[[research/erdos_49/lemma_4_1_reconstruction|Lemma 4.1]], which multiplies
one totient with known preimages into $\gg Z(x)$ totients with known
preimages, and its use through reversed pairs in
[[research/erdos_49/lemma_5_1_reconstruction|Lemma 5.1]] and the
[[research/erdos_49/theorem_1_2_reconstruction|proof of Theorem 1.2]].

**Standing.** Every statement proved on this page is author-recorded, changing
no problem status. The statements were independently reviewed as they stood on
2026-09-28T13:50:48Z by eleven focused reviews, one per section, graded in
[[research/erdos_49/evidence/verify/connections_grade|the connections grade]],
which passes all eleven and accepts twelve corrections, C1--C12, since applied;
it assigns no tier. Since the review, the Target paragraphs were updated to the
standing their problem pages record, the Problem 1003 one restated without a
date, and the first next investigation of the Problem 1004 section was reworded
to match; this touches no examined statement, proof, code or input. Each
statement is deduced from the source theorems as published, at the scope the
reconstruction pages record, and each such input is named where it is consumed.
The candidate connections were assessed on the mathematics, by checking
hypotheses, quantifier order, uniformity and the actual objects, not on shared
vocabulary; connections that fail are kept with their obstruction.

**Outcomes at a glance.** Problem 1004: transfers for every exponent below
2 (Proposition 1), open at and above 2. Problem 1003: fails. Problem 417:
transfers (bounded ratio, Proposition 2; limit superior above 1,
Proposition 3) and transfers conditionally (limit inferior above 1,
Proposition 4). Problem 416: fails. Problem 694: transfers (Proposition 5),
but the target is solved. Problems 51, 821, 415, 850 and 931: fail. The
open clause of Problem 49: nothing transfers. The Problem 1004 route is
carried by the new lead
[[research/leads/distinct_totient_blocks_from_collision_bounds/_index|distinct totient blocks from collision bounds]];
the Problem 417 route is carried by the lead
[[research/leads/distinct_totient_preimage_ratio/_index|distinct totient preimage ratio]],
written in parallel from the Problem 416 reconstruction, whose statements
this page reaches independently from this folder's own inputs.

## Notation and the inputs used

$\varphi$ is Euler's function, a *totient* is a value of $\varphi$, and the
*preimages* of a totient $v$ are the integers $m$ with $\varphi(m)=v$. For
real $x$ let

$$
V(x)=\#\{v\le x:v\text{ a totient}\},\qquad
\mathcal W(x)=\{\varphi(n):n\le x\},\qquad W(x)=\#\mathcal W(x),
$$

so that $W(x)\le V(x)$; Problem 417 writes $V'(x)$ for $W(x)$. For a
natural number $k$, $P(x;k)=\#\{n\le x:\varphi(n)=\varphi(n+k)\}$ splits as
$P_0(x;k)+P_1(x;k)$, the structured solutions of Theorem A and the rest, as
on the Theorem 3.3 page, and $c(k)$ is the coefficient defined there.
$Z(x)$ is Ford's function, defined on the Theorem 1.2 page. An integer $n$
is *convenient* for a totient $d$ with preimages $n_1,\ldots,n_k$ when
$d\varphi(n)$ is a totient whose preimages are exactly $n_1n,\ldots,n_kn$
(Lemma 5.1 page).

The inputs consumed below, at their actual scope:

- **(T1)** Theorem 3.1 of the source: there is an absolute $x_0$ such that
  $P_1(x;k)<x/\exp((\log x)^{1/3})$ for $x>x_0$, uniformly for natural
  numbers $k\le\exp((\log x)^{1/3})$. A published theorem whose proof the
  source gives as a sketch; the reconstruction records the sketch and its
  one written deduction only.
- **(T3)** Theorem 3.3 of the source: for even $k$ with
  $2\le k\le x^{\varepsilon(x)}$, where $\varepsilon(x)\to0$ and
  $x^{\varepsilon(x)}\to\infty$, $P_0(x;k)\le(16C_2+o(1))c(k)x/(\log x)^2$
  uniformly in $k$, where $C_2=2\prod_{p>2}(1-(p-1)^{-2})$ is the
  twin-prime constant in the source's normalization (Theorem 3.3 page), and
  $\frac1{2k}\le c(k)\le\Bigl(3\cdot7^{3+2\omega(k)}\prod_{p\mid k,\ p>2}\frac{p-1}{p-2}\Bigr)\frac1k$.
  Reconstructed modulo Selberg's sieve as the source states it and
  Evertse's bound inside Lemma 3.2. For odd $k$, $P_0(x;k)=0$ (Theorem 1.2
  page, step 2).
- **(L4)** Lemma 4.1 of the source: for fixed totients $d_1,d_2$ and fixed
  $D\ge\max\{d_1,d_2\}$ there are an absolute $K\ge1$, a constant $c_D>0$
  and $x_0(D)$ such that for $x\ge x_0(D)$ at least $c_DZ(x)$ integers $n$
  satisfy $\varphi(n)\le x/D$, $n$ convenient for $d_1$ and for $d_2$, and
  $n/\varphi(n)\le K$. A published lemma whose two counting steps import
  Ford's lower-bound argument; the reconstruction is partial.
- **(F)** Ford's Theorem 1, on the card
  [[../library/arithmetic_functions/ford_1998_distribution_totients/_index|Ford (1998)]]:
  $V(x)=Z(x)e^{O(1)}$ for large $x$. Three consequences are used: there
  are absolute $c_0,C_1>0$ with $c_0Z(x)\le V(x)\le C_1Z(x)$ for large
  $x$; and for each fixed $\mu\ge1$, $Z(x/\mu)/Z(x)\to1/\mu$, because
  $\log(x/\mu)\sim\log x$ and
  $\log_3(x/\mu)-\log_3x=O(1/(\log x\log_2x))$, so the exponent of $Z$,
  whose leading term is $C(\log_3x-\log_4x)^2$, changes by
  $O(\log_3x/(\log x\log_2x))\to0$; hence $V(x/\mu)\le(C_3/\mu)V(x)$ for
  $x\ge x_2(\mu)$ with an absolute $C_3$.
- **(P)** The explicit totient $d_1=2^{18}\cdot257=67371008$, whose eight
  preimages are enumerated on the Lemma 5.1 page; all eight are even. The
  enumeration was repeated for this page by the same divisor recursion, with
  the same result; both runs are author-recorded and not filed as evidence.

## Problem 1004: distinct totients on a consecutive block

**Target.** [[problems/arithmetic_functions/E1004/_index|Problem 1004]] asks: for
fixed $c>0$ and all large $x$, is there $n\le x$ such that
$\varphi(n+1),\ldots,\varphi(n+\lfloor(\log x)^c\rfloor)$ are pairwise
distinct? Its page records the status open for every $c$. Its one claim,
[[problems/arithmetic_functions/E1004/claims/2026_04_29_aditya|the anonymous note's pending partial claim]],
asserts the almost-all form for every $c<2$, and the note is also kept as the
unreviewed candidate
[[research/leads/totient_blocks_native_note/_index|totient_blocks_native_note]].
Its current assessment records that the cited sources state no growing-block
existence theorem, and its Progress records the uniform bounds (T1) and (T3)
as the relevant inputs and this page's deduction for $c<2$, Proposition 1
below.

**What transports.** The union bound over the $\binom L2$ shifts of a block
of length $L$, fed with (T1), (T3) and the upper bound on $c(k)$, gives the
following. The proof is complete relative to (T1) and (T3).

**Proposition 1** (author-recorded). Let $L=L(x)$ be integer-valued with
$2\le L(x)\le(\log x)^2/(\log\log x)^{50}$. Then the number of integers
$1\le n\le x$ for which $\varphi(n+1),\ldots,\varphi(n+L)$ are *not*
pairwise distinct is $o(x)$. In particular, for every fixed $c<2$ and all
large $x$, all but $o(x)$ of the $n\le x$ have
$\varphi(n+1),\ldots,\varphi(n+\lfloor(\log x)^c\rfloor)$ pairwise
distinct, so Problem 1004 has an affirmative answer for every $c<2$.

*Proof.* Let $x$ be large, $L=L(x)$, and $y=x+L\le2x$. Let $B(x,L)$ count
the integers $1\le n\le x$ with $\varphi(n+i)=\varphi(n+j)$ for some
$1\le i<j\le L$.

*Step 1: reduction to shifted collisions.* If $n$ is counted, put $m=n+i$
and $h=j-i$; then $1\le h\le L-1$, $m\le x+L-h\le y$ and
$\varphi(m)=\varphi(m+h)$, so $m$ is counted by $P(y;h)$. Given $(m,h)$,
$n=m-i$ with $1\le i\le L-h$, at most $L-h$ values. Hence

$$
B(x,L)\le\sum_{h=1}^{L-1}(L-h)P(y;h)\le L\sum_{h=1}^{L-1}P(y;h).
$$

*Step 2: the uniform inputs.* For large $x$,
$L\le(\log x)^2\le\exp((\log y)^{1/3})$, so (T1) gives
$P_1(y;h)<y\exp(-(\log y)^{1/3})$ for every $1\le h\le L-1$. Take
$\varepsilon(y)=(\log y)^{-1/2}$: then $\varepsilon(y)\to0$,
$y^{\varepsilon(y)}=\exp(\sqrt{\log y})\to\infty$, and
$L\le(\log x)^2\le y^{\varepsilon(y)}$ for large $x$, so (T3) gives, for
every even $h\le L-1$ and large $x$,
$P_0(y;h)\le(16C_2+1)c(h)\,y/(\log y)^2$, the $o(1)$ being uniform in $h$.
For odd $h$, $P_0(y;h)=0$. With $S(L)=\sum_{h\le L,\ h\text{ even}}c(h)$,

$$
\sum_{h=1}^{L-1}P(y;h)\le
L\,y\exp\bigl(-(\log y)^{1/3}\bigr)+(16C_2+1)S(L)\frac{y}{(\log y)^2}.
$$

*Step 3: the average of $c(h)$.* By the upper bound in (T3),
$c(h)\le3\cdot7^3\,g(h)/h$ with
$g(h)=49^{\omega(h)}\prod_{p\mid h,\ p>2}\frac{p-1}{p-2}$, a nonnegative
multiplicative function with $g(2^a)=49$ and $g(p^a)=49\frac{p-1}{p-2}$
for $p>2$ and all $a\ge1$. For $L\ge3$,

$$
\sum_{h\le L}\frac{g(h)}{h}
\le\prod_{p\le L}\Bigl(1+\sum_{a\ge1}\frac{g(p^a)}{p^a}\Bigr)
=\prod_{p\le L}\Bigl(1+\frac{g(p)}{p-1}\Bigr)
=50\prod_{3\le p\le L}\Bigl(1+\frac{49}{p-2}\Bigr)
\le50\exp\Bigl(49\sum_{3\le p\le L}\frac1{p-2}\Bigr),
$$

and
$\sum_{3\le p\le L}1/(p-2)\le\sum_{p\le L}1/p+\sum_{p\ge3}2/(p(p-2))=\log\log L+O(1)$
by Mertens' theorem. Hence $S(L)\le A_0(\log L)^{49}$ for $L\ge3$ with an
absolute constant $A_0$, and enlarging $A_0$ covers $L=2$, where the sum is
$c(2)$.

*Step 4: conclusion.* Since $y\le2x$ and $\log y\ge\log x$,

$$
B(x,L)\le2x\Bigl[(\log x)^4\exp\bigl(-(\log x)^{1/3}\bigr)
+(16C_2+1)A_0\frac{L(\log L)^{49}}{(\log x)^2}\Bigr]
$$

for large $x$ (using $L\le(\log x)^2$ in the first term). The first bracket
term tends to $0$. In the second, $L\le(\log x)^2/(\log\log x)^{50}$ and
$\log L\le2\log\log x$ give
$L(\log L)^{49}/(\log x)^2\le2^{49}/\log\log x\to0$. So $B(x,L)=o(x)$, and
all but $o(x)$ of the $n\le x$ have the block pairwise distinct. For fixed
$c<2$, $L=\lfloor(\log x)^c\rfloor$ satisfies the hypothesis for large $x$.
$\square$

**What it does not give.** The range $c\ge2$, for a reason internal to the
method. The first-moment bound of Step 1 is fed with the termwise upper
bound $P_0(y;h)\le(16C_2+o(1))c(h)y/(\log y)^2$, and (T3) also proves
$c(h)\ge1/(2h)$ for even $h$; so whatever average bound for $c(h)$ is
used, the bound on $B(x,L)$ obtained in Step 4 is at least of order
$L\log L\cdot x/(\log x)^2$, which is not $o(x)$ once $L\log L\gg(\log x)^2$.
The anonymous note's sharper average $\sum_{h\le L}c(h)\ll\log L$ would
extend Proposition 1 exactly to the $L$ with $L\log L=o((\log x)^2)$, for
instance $L\le(\log x)^2/(\log\log x)^{1+\delta}$ for fixed $\delta>0$, and
to no $L\ge\kappa(\log x)^2/\log\log x$ with fixed $\kappa>0$. This is a
limit of the union bound, not a proved obstruction to the target: it would
become one only with a matching lower bound $P_0(x;h)\gg c(h)x/(\log x)^2$,
which is a prime-pair statement (both $ar+1$ and $br+1$ prime) and is not
available. If that lower bound holds, as the Hardy--Littlewood heuristic
predicts, the expected number of collisions inside a block of length $L$ at
a random start $n\le x$ is at least of order $L\log L/(\log x)^2$. A first
moment does not decide how many blocks are collision-free. Under a Poisson
model for the positions of collisions, for $c>2$ almost all blocks contain
a collision and only atypical starts can answer the question, and the same
model predicts a longest collision-free block below $x$ of length
$(\log x)^{3+o(1)}$, so under it the every-$c$ form would fail for $c>3$.
The model is a heuristic and is stated here as such. An exploratory
computation (a sieve of $\varphi$ and a sliding window over $1\le m\le N$;
author-recorded, not filed) found the longest block of consecutive integers
with pairwise distinct totients below $N=10^5,10^6,10^7$ to have lengths
$111$, $194$ and $321$, against $(\log N)^2=133,191,260$ and
$(\log N)^3/\log\log N=625,1004,1506$; the range is far too short to
separate the exponents, and the observation was made after the heuristic
was written, not predicted by it.

**Relation to the retained note.** The note preserved under
[[research/leads/totient_blocks_native_note/_index|totient_blocks_native_note]]
claims the same $c<2$ corollary by the same union bound, with the average
$\sum_{h\le L}c(h)\ll\log L$ it asserts on its pp. 2--3. Proposition 1
needs no average estimate beyond the crude $(\log L)^{49}$ of Step 3, which
follows from the bound on $c(k)$ that (T3) itself states, so the $c<2$
answer rests on (T1) and (T3) alone. The erdosproblems.com discussion thread for
the problem, read on 2026-09-28, carries the note and a reader's remark that the
statement is implicit in the source paper; the erdosproblems.com problem page,
last edited 12 April 2026, records neither.

**Next investigation.** (1) Proposition 1, whose only inputs are (T1) and
(T3), was reviewed with this page (see Standing), and the problem page
records the $c<2$ answer under its Progress; it does not note that the source
gives (T1)'s proof as a sketch. (2) For $c\ge2$ the question becomes
whether the collision set
$\mathcal C_L=\{m:\varphi(m)=\varphi(m+h)\text{ for some }1\le h<L\}$ has
gaps of length $L$ below $x$. A positive result for some $c\ge2$ would need
more than first moments: either a lower bound for the number of gaps (a
second-moment or sieve argument exploiting that structured collisions have
the shape $m=jq$, $m+h=(j+h)p$ with $q=br+1$ and $p=ar+1$ prime), or a
construction of a start $n$ avoiding every such shape. A negative result
for some $c$, showing that every block of length $(\log x)^c$ below $x$
contains a collision, would refute the every-$c$ expectation and needs a
lower bound for collisions, hence a prime-pair input. The route is carried
by the lead
[[research/leads/distinct_totient_blocks_from_collision_bounds/_index|distinct totient blocks from collision bounds]].

**Outcome.** Transfers for every $c<2$; open for $c\ge2$.

## Problem 1003: the unit shift

**Target.** [[problems/arithmetic_functions/E1003/_index|Problem 1003]] asks
whether $\varphi(n)=\varphi(n+1)$ has infinitely many solutions. The problem
page records the question as open, with Li's Corollary 1.5, a preprint result,
as the strongest unit-shift upper bound and Ford's infinitude results for even
shifts divisible by a fixed large integer.

**What transports.** Only upper bounds, in the wrong direction. (T1) with
$k=1$ gives $P(x;1)=P_1(x;1)<x/\exp((\log x)^{1/3})$ for large $x$, the
bound of Erdős, Pomerance and Sárközy recorded on the problem page and
weaker than Yamada's and Li's. The structured family of Theorem A is empty
for $k=1$: it needs $j$ and $j+1$ with the same prime factors, and
consecutive integers are coprime (Theorem 1.2 page, step 2). Nothing in
the reconstruction constructs a solution.

**What it does not give, and why.** Infinitude is an existence statement.
The reconstructed bounds on $P(x;k)$, (T1) and (T3), are upper bounds; the
reconstructed lower bounds, (L4) and Lemma 5.1, count convenient integers
and missing totient values, and neither constrains $\varphi(n+1)$ for any
$n$ it counts. The one construction in the source chain, Theorem A,
produces solutions of $\varphi(n)=\varphi(n+k)$ only from pairs $j,j+k$
with equal radicals, which forces $k$ even; this is the structural reason
the even-shift results of Ford (2020) do not reach $k=1$, and the
reconstruction adds no way around it.

**Next investigation.** None from this mechanism. **Outcome.** Fails: the
bounds on $P(x;k)$ are upper bounds, the lower-bound inputs count other
objects, and the only constructive ingredient needs an even shift.

## Problem 417: totients below x against totients of integers below x

**Target.** [[problems/arithmetic_functions/E0417/_index|Problem 417]] asks whether
$\lim V(x)/V'(x)$ exists and whether it is $>1$, where $V'(x)=W(x)$ counts
the distinct values $\varphi(m)$, $1\le m\le x$, and $V(x)$ counts the
totients $\le x$. Its page records the status open with no claim page; its
Current assessment records Theorem 2.2 of the OpenAI release, which bears on
the problem without claiming it, and its Progress records the results of the
Problem 416 folder's connections page. The erdosproblems.com page, read on
2026-09-28, records that Erdős suggested in 1998 that the limit may be infinite,
and its discussion thread is undecided about whether the ratio is bounded.

**What transports, unconditionally.** Three statements.

**Proposition 2** (author-recorded; the boundedness that the source quotes
from Ford on its p. 7, rederived from (L4)). There is an absolute constant
$C$ with $V(x)\le C\,V'(x)$ for all large $x$; so
$\limsup_{x\to\infty}V(x)/V'(x)<\infty$.

*Proof.* The totient $1$ has preimages exactly $1$ and $2$. Apply (L4) with
$d_1=d_2=1$ and $D=K$ (allowed, as $K\ge1=\max\{d_1,d_2\}$): for
$x\ge x_0(K)$ there are at least $c_KZ(x)$ integers $n$ with
$\varphi(n)\le x/K$, $n$ convenient for $1$, and $n/\varphi(n)\le K$. For
each such $n$, $n\le K\varphi(n)\le x$, so $\varphi(n)\in\mathcal W(x)$; and
convenience for $1$ says that $\varphi(n)$ is a totient whose preimages are
exactly $n$ and $2n$, so $n$ is its least preimage and $n\mapsto\varphi(n)$
is injective on this set. Hence $W(x)\ge c_KZ(x)$, and with (F),
$V(x)\le C_1Z(x)\le(C_1/c_K)W(x)$. $\square$

Since $V$ and $W$ are nondecreasing integer-valued functions that increase
by at most $1$ across any interval of length at most $1$, and both exceed
$c_0x/\log x$ by Chebyshev's bound applied to the values $p-1$ of the
primes $p\le x$, the ratio $R(x)=V(x)/W(x)$ satisfies
$|R(x+h)-R(x)|\le(1+C)/W(x)\to0$ for $0<h\le1$; a bounded function whose
unit-step increments tend to $0$ has every value between its limit
inferior and limit superior as a limit point. So the set of limit points of
$V(x)/V'(x)$ is a closed interval $[\ell_1,\ell_2]$ with
$1\le\ell_1\le\ell_2\le C$, exactly as the cluster-interval argument
reconstructed on
[[research/erdos_416/zeraoulia_theorem_1_1_reconstruction|the Problem 416 research page]]
gives for $V(cx)/V(x)$; the Problem 416 folder index already notes that the
argument applies once the ratio is bounded. Erdős's suggestion of an
infinite limit, as erdosproblems.com reports it, is excluded by Proposition 2.

**Proposition 3** (author-recorded). $\limsup_{x\to\infty}V(x)/V'(x)>1$.
More precisely, there are absolute constants $c'>0$ and $J\ge1$ such that
for every large $x$ some $y\in[2^{-J}x,x]$ has $V(y)-V'(y)\ge c'V(y)$.

*Proof.* Let $d=d_1=2^{18}\cdot257$ from (P), with preimages
$n_1<\cdots<n_8$, all even. Let $E(t)$ count the totients $v\le t$ all of
whose preimages are even.

*All-even totients are a positive proportion.* Apply (L4) with
$d_1=d_2=d$ and $D=d$: for $t\ge x_0(d)$ there are at least $c_dZ(t)$
integers $n$ with $\varphi(n)\le t/d$, convenient for $d$. For each,
$v=d\varphi(n)\le t$ is a totient whose preimages are exactly
$n_1n,\ldots,n_8n$, all even; and $n\mapsto d\varphi(n)$ is injective,
since $n_1n$ is the least preimage of $d\varphi(n)$. Hence
$E(t)\ge c_dZ(t)\ge cV(t)$ for $t\ge t_1$, with $c=c_d/C_1$ by (F).

*All-even totients in the top half have no preimage below $y$.* If $m$ is
even then $\varphi(m)\le m/2$, so every preimage of an all-even totient $v$
is at least $2v$. If $y/2<v\le y$, every preimage of $v$ exceeds $y$, so
$v\notin\mathcal W(y)$ while $v$ is counted by $V(y)$. Hence, for every $y$,

$$
V(y)-V'(y)\ge E(y)-E(y/2).
$$

*A dyadic scale where the increment is large.* By (F) with $\mu=2^{J+1}$,
$V(x/2^{J+1})\le C_32^{-J-1}V(x)$ for large $x$; fix $J$ with
$C_32^{-J-1}\le c/2$. For $x$ so large that $x/2^{J+1}\ge t_1$,

$$
\sum_{j=0}^{J}\bigl(E(x/2^j)-E(x/2^{j+1})\bigr)=E(x)-E(x/2^{J+1})
\ge cV(x)-V(x/2^{J+1})\ge\tfrac c2V(x),
$$

so some $j\in\{0,\ldots,J\}$ has
$E(x/2^j)-E(x/2^{j+1})\ge cV(x)/(2(J+1))\ge cV(x/2^j)/(2(J+1))$. With
$y=x/2^j$ and $c'=c/(2(J+1))$, the displayed inequality gives
$V(y)-V'(y)\ge c'V(y)$, that is, $V(y)/V'(y)\ge1/(1-c')$. Since $y\to\infty$
with $x$, $\limsup V(x)/V'(x)\ge1/(1-c')>1$. $\square$

So $\ell_2>1$: if the limit exists, it exceeds $1$. This answers the second
question of Problem 417 conditionally on the first; the first (existence)
is untouched. The search for small seeds is worth recording: a sieve over
$m\le6\cdot10^6$ (author-recorded, not filed) found no totient $\le10^6$
without an odd preimage, so all-even totients are rare among small
totients, and the source's $d_1$ is the seed used.

**What transports conditionally.** The natural strengthening is a limit
inferior above $1$, and it follows from one window-form premise.

**Premise (W)** (not proved here). For every totient $d$ and every real
$\lambda>1$ there are $c(d,\lambda)>0$ and $t_0(d,\lambda)$ such that for
$t\ge t_0$ at least $c(d,\lambda)Z(t)$ integers $n$ are convenient for $d$
and satisfy $t/\lambda<\varphi(n)\le t$.

(L4) is the case of a one-sided range $\varphi(n)\le t$; (W) asks for the
same count in a multiplicative window. It cannot be deduced from (L4) as
stated, because (L4) gives a lower bound with an unspecified constant
$c_D$ and the window count is that lower bound minus a count at the
smaller scale that is only bounded above (by $V(t/\lambda)\asymp V(t)/\lambda$),
so no fixed $\lambda$ is forced to work. Ford's Theorem 4, on p. 3 of the
paper held by the Ford card and not among the results the card lists (for
admissible $\theta$, $y\ge x^\theta$ and a possible multiplicity $k$,
$V_k(x+y)-V_k(x)\asymp V(x+y)-V(x)\asymp\frac{y}{x+y}V(x+y)$, stated by
Ford to follow from a simple modification of the proofs of Theorems 1
and 2), is the short-interval form of the multiplicity count that the same
construction proves; (W) is the intermediate statement that modification
produces for convenient integers. It is a premise here, not a result.

**Proposition 4** (author-recorded, conditional on (W)). If (W) holds for
the totient $d=2$ and $\lambda=3/2$, then $V(x)-V'(x)\gg V(x)$, so
$\liminf_{x\to\infty}V(x)/V'(x)>1$.

*Proof.* The totient $2$ has preimages exactly $3,4,6$. By (W) with $t=x/2$
and $\lambda=3/2$, for large $x$ at least $c(2,3/2)Z(x/2)\ge c''Z(x)$
integers $n$ are convenient for $2$ with $x/3<\varphi(n)\le x/2$ (using
(F) for $Z(x/2)\ge Z(x)/3$). For each, $v=2\varphi(n)\le x$ is a totient
whose preimages are exactly $3n,4n,6n$; the least, $3n\ge3\varphi(n)>x$, so
$v\notin\mathcal W(x)$; and $n\mapsto2\varphi(n)$ is injective. Hence
$V(x)-V'(x)\ge c''Z(x)\ge(c''/C_1)V(x)$. $\square$

**What it does not give, and why.** Existence of the limit: nothing here
controls the width $\ell_2-\ell_1$, exactly as the doubling-law folder
records for $V(cx)/V(x)$. Proposition 3 cannot be upgraded to a limit
inferior without (W), because $E$ could in principle grow in bursts,
leaving $E(y)-E(y/2)=o(V(y))$ along a sequence of scales.

**Parallel derivation.** The same three unconditional statements, and the
same conditional one, are proved independently on
[[research/erdos_416/connections|the connections page of the Problem 416 folder]]
(its Propositions 417.2 and 417.4 and Theorem 417.3), from Ford's Theorem
8 at statement level with the seed $54$, whose preimages $81$ and $162$
are both divisible by $3$, and a geometric sequence of scales; that page
carries the lead
[[research/leads/distinct_totient_preimage_ratio/_index|distinct totient preimage ratio]],
whose premise (P1), the short-interval form of Ford's Theorem 8, is the
premise (W) above in multiplicity form. The proofs here use only the
inputs this folder reconstructs, (L4) and the seed (P), so the two pages
are independent checks of one another; no second lead is opened for the
same target and route.

**Next investigation.** Prove (W) by carrying Ford's short-interval
modification through the construction behind (L4). Two readings of Ford's
§5, in the held conversion, make this plausible and are the points to
verify: the largest prime $p_0$ of a candidate $n=p_0p_1\cdots p_L$ is
counted, for fixed $p_1\cdots p_L$, by the prime number theorem in a range
fixed by $\varphi(n)\le x/d$, so restricting $p_0-1$ to a window of ratio
$\lambda$ costs a factor depending on $\lambda$ only; and the exclusion of
the non-trivial solutions of $d\varphi(n)=\varphi(n_1)$ is an upper bound
whose fraction of the candidate set decays in the parameter $M_2$, so it
survives restriction to the window once $M_2$ is enlarged. A positive
outcome gives $\ell_1>1$ and settles the second question of Problem 417 in
the form: the ratio stays above a fixed constant greater than $1$ for all
large $x$. A negative outcome, $\ell_1=1$, would mean that along some
scales almost every totient $\le x$ has a preimage $\le x$, which
Proposition 3 shows cannot hold at all scales. The route is carried by the
parallel lead named above.

**Outcome.** Transfers (Propositions 2 and 3); transfers conditionally
(Proposition 4).

## Problem 416: an asymptotic formula for the totient count

**Target.** The second question of
[[problems/arithmetic_functions/E0416/_index|Problem 416]], an asymptotic formula
for $V(x)$. Its page records the standing claimed, through
[[problems/arithmetic_functions/E0416/claims/2026_09_25_openai_formula|the OpenAI release's pending full claim]]
of an asymptotic equivalent for $V(x)$ whose coefficient has no closed form,
with the first question ($V(2x)/V(x)\to2$) answered by two accepted partial
claims and Ford's Theorem 1 as the best formula-type result before the
release.

**What transports.** (L4) is the lower-bound half of Ford's order of
magnitude; the proof of Proposition 2 above recovers $W(x)\ge c_KZ(x)$ from
it and, with the upper bound of (F), $W(x)\asymp V(x)\asymp Z(x)$. Nothing
more.

**What it does not give, and why.** A lower-bound construction gives an
order of magnitude, never a formula: the count of convenient integers is
$\gg_DZ(x)$ with an unspecified constant, and the families $d\varphi(n)$
built from any finite list of seeds $d$ miss whole classes of totients, as
Ford remarks in §7 of the held paper, writing of the belief that an
asymptotic formula will require the asymptotics of $V_k(x)/V(x)$ and
$V(x;k)/V(x)$ for every $k$. The folder index of the
[[research/erdos_416/_index|Problem 416 reconstruction]] states the same
gap from the doubling-law side.

**Outcome.** Fails: the mechanism is an order-of-magnitude construction.

## Problem 694: the ratio of the largest to the smallest preimage

**Target.** [[problems/arithmetic_functions/E0694/_index|Problem 694]] asks for
the size of $\max_{v\le x}f_{\max}(v)/f_{\min}(v)$ over totients $v$, where
$f_{\max},f_{\min}$ are the largest and smallest preimages; the current
assessment records it as solved, with $(e^\gamma+o(1))\log\log x$ from a
five-page note filed on
[[../library/arithmetic_functions/gpt_5_5_pro_2026_totient_fibre_extremes/theorem_2_1|its library card]],
whose Proposition 3.1 observes that one collision $\varphi(a)=\varphi(b)$
with $a>b$ gives infinitely many totients with ratio at least $a/b$.

**What transports.** The convenient-integer construction preserves the whole
preimage set up to the common factor $n$, hence preserves this ratio
exactly, and does so on a positive proportion of totients.

**Proposition 5** (author-recorded). For every totient $d$ with preimages
$n_1<\cdots<n_k$, the number of totients $v\le x$ with
$f_{\max}(v)/f_{\min}(v)=n_k/n_1$ is at least $c_dZ(x)\gg_dV(x)$ for
$x\ge x_0(d)$.

*Proof.* Apply (L4) with $d_1=d_2=d$ and $D=d$. Each of the $\ge c_dZ(x)$
integers $n$ obtained has $\varphi(n)\le x/d$, so $v=d\varphi(n)\le x$, and
$v$ is a totient whose preimages are exactly $n_1n,\ldots,n_kn$; thus
$f_{\max}(v)/f_{\min}(v)=n_kn/(n_1n)=n_k/n_1$. Distinct $n$ give distinct
$v$, since $n_1n$ is the least preimage of $v$. $\square$

So every ratio that occurs at all occurs on a positive proportion of the
totients up to $x$, which strengthens the note's Proposition 3.1 from
"infinitely many with ratio at least $a/b$" to "a positive proportion with
ratio exactly $f_{\max}(n)/f_{\min}(n)$, hence at least $a/b$", where
$n=\varphi(a)=\varphi(b)$. The
[[research/erdos_416/connections|Problem 416 connections page]] identifies
the note's device with the same multiplication by convenient integers,
from the other side.

**What it does not give.** Anything about the maximum: (L4) fixes the seed
$d$ before $x$ grows, so the ratios it produces are bounded, while the
extremal ratio grows like $\log\log x$ through seeds that grow with $x$.

**Outcome.** Transfers, but the target is solved; Proposition 5 is a
further result for the problem page, not a route.

## Problem 51: totients whose smallest preimage is large

**Target.** [[problems/arithmetic_functions/E0051/_index|Problem 51]] asks for an
infinite set of totients $a$ whose least preimage $n_a$ has
$n_a/a\to\infty$. Its page records the status open, with
[[problems/arithmetic_functions/E0051/claims/2026_01_11_colossal_noob|a rejected full claim]].

**What transports.** From a seed totient $d$ with least preimage $n_1$, the
$\gg_dV(x)$ totients $v=d\varphi(n)\le x$ of Proposition 5 have least
preimage $n_1n$ and

$$
\frac{n_v}{v}=\frac{n_1n}{d\varphi(n)}=\frac{n_1}{d}\cdot\frac{n}{\varphi(n)}
\in\Bigl[\frac{n_1}{d},\,K\frac{n_1}{d}\Bigr]
$$

by clause (iii) of (L4). So every attained ratio $n_1/d$ is attained, up to
the bounded factor $K$, on a positive proportion of totients.

**What it does not give, and why.** Growth. The transported ratio is
bounded by $Kn_1/d$ for a fixed seed, and a family of seeds $d_j$ with
$n_1(d_j)/d_j\to\infty$ is the question itself. The bound $n/\varphi(n)\le K$
is not incidental: it comes from the sizes of the primes in Ford's
candidate set (the proof of (iii) on the Lemma 4.1 page), and replacing
those primes by small ones to make $n/\varphi(n)$ large would break the
convenience count, which is Ford's argument for exactly that set. In the
other direction the mechanism gives an upper bound of the wrong kind: the
totients it constructs have least-preimage ratio bounded, which is
consistent with either answer.

**Outcome.** Fails: the mechanism transports a ratio within a bounded
factor and cannot create unbounded ratios.

## Problem 821: totients of very large multiplicity

**Target.** [[problems/arithmetic_functions/E0821/_index|Problem 821]] asks
whether, for every $\epsilon>0$, infinitely many $n$ have more than
$n^{1-\epsilon}$ preimages. Its page records the standing claimed, through
[[problems/arithmetic_functions/E0821/claims/2026_09_24_openai|the OpenAI release's pending full claim]];
the known results it references, Baker and Harman's accepted partial claim
and Lichtman's pending one, come from shifted primes without large prime
factors.

**What transports.** For convenient $n$ the multiplicity of $d\varphi(n)$
equals that of $d$, so each attained multiplicity is attained on a positive
proportion of totients; this is Ford's Theorem 2, already on the Ford card.

**What it does not give, and why.** The construction never increases a
multiplicity: the preimages of $d\varphi(n)$ are exactly the $k$ products
$n_in$. Large multiplicity needs totients with many preimages in the first
place, which is a different mechanism (many primes $p$ with $p-1$ dividing
a fixed smooth number).

**Outcome.** Fails.

## Problem 415: ordering patterns of consecutive totients

**Target.** [[problems/arithmetic_functions/E0415/_index|Problem 415]] defines
$F(n)$ as the largest $k$ such that every one of the $k!$ orderings occurs
among $\varphi(m+1),\ldots,\varphi(m+k)$ for some $m$ with $m+k\le n$, and
asks whether $F(n)=(c+o(1))\log\log\log n$, whether the decreasing pattern
is always the first to fail, and whether the pattern of
$\varphi(1),\ldots,\varphi(k)$ is the most frequent. Its page records the
standing claimed, with the answer disproved, through
[[problems/arithmetic_functions/E0415/claims/2026_04_19_chojecki|Chojecki's pending full claim]],
which answers all three questions no; Pollack, Pomerance and Treviño's 2012
asymptotic for monotone runs, which answers the first question no, is an
accepted partial claim.

**What transports.** Proposition 1 says that for $c<2$ almost every block
of length $(\log x)^c$ carries pairwise distinct totients, hence a strict
total order: each such block realizes exactly one of the $L!$ patterns.

**What it does not give, and why.** The pattern questions live at lengths
of order $\log\log\log n$, far below the collision scale, and they ask that
*every* pattern occur; a collision bound says nothing about which pattern a
block realizes. Controlling the order of consecutive totients is a
construction problem in which small, medium and large primes are handled
separately, the method of the source's §8, which is not part of this
reconstruction.

**Background for the problem page, outside this reconstruction.** Theorem
1.5 of the same source, recorded as a statement on the primes card
[[../library/primes/pollack_et_al_2013_sets_monotonicity_euler_totient_function/_index|Pollack, Pomerance and Treviño (2013)]],
gives the longest run of consecutive integers in $[1,x]$ on which
$\varphi$ is nonincreasing the length $\log_3x/\log_6x+O(\log_3x/(\log_6x)^2)$.
A strictly decreasing run is nonincreasing, and $F(n)$ requires the
decreasing pattern of length $F(n)$ to occur, so
$F(n)\le(1+o(1))\log_3n/\log_6n=o(\log_3n)$: the first question has a
negative answer for every $c>0$. The erdosproblems.com page for the problem,
read on 2026-09-28 and last edited 28 May 2026, records this consequence of the
source paper; the corpus page, accessed 2026-09-04, does not yet.

**Outcome.** Fails for the pattern questions; the background note is a
library-level fact for the page compilers, not a transfer.

## Problems 850 and 931: pairs with the same prime factors

**Target.** [[problems/primes/E0850/_index|Problem 850]] asks whether two distinct
integers $x,y$ can have $x,y$, then $x+1,y+1$, then $x+2,y+2$ with the
same prime factors in each pair;
[[problems/diophantine_problems/E0931/_index|Problem 931]] asks whether two
disjoint products of at least three consecutive integers can have the same
prime factors only finitely often. Both corpus pages are open and not
compiled beyond the statement.

**What transports.** Lemma 3.2 says that for each natural number $k$ at most
$3\cdot7^{3+2\omega(k)}$ natural numbers $j$ have $\gamma(j)=\gamma(j+k)$. Take
$x<y$, the conditions being symmetric, and $k=y-x\ge1$; for positive $x$ each of
the three conditions says that $j=x,x+1,x+2$ is such a $j$. Under the
erdosproblems.com wording, over all integers, the same bound holds, because an
entry $0$ or $\pm1$ forces $x=y$ or a failing pair, and the lemma's injection
$j\mapsto((j+k)/k,-j/k)$ counts every integer $j\notin\{0,-k\}$ with
$\gamma(|j|)=\gamma(|j+k|)$. So for each fixed difference $k$ there are at most
$3\cdot7^{3+2\omega(k)}$ candidates $x$, boundedly many in terms of $\omega(k)$.

**What it does not give, and why.** Existence or nonexistence: the union
over all $k$ is unbounded, and the lemma counts pairs at one difference
without seeing the interaction between the three consecutive conditions,
which is the whole content of Problem 850. For Problem 931 the objects are
products of blocks, not pairs at a fixed difference, so the lemma's
hypothesis is not even met. The tool behind the lemma, Evertse's bound for
$u+v=1$ in $S$-units, is a standard input for such problems, but the
transported statement adds nothing to it.

**Outcome.** Fails.

## Problem 49: the remaining clause

[[problems/primes/E0049/_index|Problem 49]] retains one open clause, whether the
primes are a largest subset of $\{1,\ldots,N\}$ with strictly increasing
totients. Nothing on this page bears on it. The reconstructed bound
$M^\uparrow(x)\le(1-c)W(x)$ exceeds $\pi(x)$ by a factor tending to
infinity and is superseded by Tao's rate; the reversed pairs of Lemma 5.1
constrain sets whose totients may repeat, while a strict set already has
distinct totients and is bounded by $W(x)$ for the elementary reason on the
folder index; and the clause is an exact finite question, which none of
the asymptotic mechanisms here addresses. The folder index maps the three
clauses.
